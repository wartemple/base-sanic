import logging
import time
import os


class EnhancedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler, logging.handlers.RotatingFileHandler):
    

    def custom_namer(self, default_name):
        base_filename, ext, date, count = default_name.split(".")
        return f"{base_filename}.{date}.{count}.{ext}"

    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None,
                delay=0, when='h', interval=1, utc=False):
        self.namer = self.custom_namer
        self.maxBytes = maxBytes
        logging.handlers.TimedRotatingFileHandler.__init__(self, filename=filename, when=when, interval=interval,backupCount=backupCount, encoding=encoding, delay=delay, utc=utc)


    def doRollover(self):
        # get from logging.handlers.TimedRotatingFileHandler.doRollover()
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        base_time_file_name = self.baseFilename + "." + time.strftime(self.suffix, timeTuple)
        # 从这开始是自定义
        if self.backupCount > 0:
            self.replace_old_log(base_time_file_name)
            for s in self.getFilesToDelete():
                os.remove(s)
            new_file_name = self.rotation_filename("%s.%d" % (base_time_file_name, 1))
            self.rotate(self.baseFilename, new_file_name)
        # 到这
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        #If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:           # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt
    
    def replace_old_log(self, base_time_file_name):
        for i in range(self.backupCount - 1, 0, -1):
            sfn = self.rotation_filename("%s.%d" % (base_time_file_name, i))
            dfn = self.rotation_filename("%s.%d" % (base_time_file_name, i + 1))
            if os.path.exists(sfn):
                if os.path.exists(dfn):
                    os.remove(dfn)
                os.rename(sfn, dfn)
    
    def set_file_name(self, file_name):
        dfn = self.rotation_filename(file_name)
        if os.path.exists(dfn):
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)

    def shouldRollover(self, record):
        return logging.handlers.TimedRotatingFileHandler.shouldRollover(self, record) or logging.handlers.RotatingFileHandler.shouldRollover(self, record)


    def getFilesToDelete(self):
        """删除当前文件夹中的相关多余文件"""
        result = []
        dirName, baseName = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        n, e = os.path.splitext(baseName)
        prefix = n + '.'
        plen = len(prefix)
        for fileName in fileNames:
            if fileName == baseName:
                continue
            suffix = fileName[plen:]
            parts = suffix.split('.')
            for part in parts:
                if self.extMatch.match(part):
                    result.append(os.path.join(dirName, fileName))
                    break
        if len(result) < self.backupCount:
            result = []
        else:
            result.sort()
            result = result[:len(result) - self.backupCount]
        return result