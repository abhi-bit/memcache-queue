class MemQueue(object):
    def __init__(self, name, memcacheClient):
        self.name = name
        self.mcClient = memcacheClient

        self.lastRead = 'mq_%s_last_read' % name
        lastRead = self.mcClient.get(self.lastRead)
        if not lastRead:
            self.mcClient.set(self.lastRead, 0)

        self.lastAdded = 'mq_%s_last_added' % name
        lastAdded = self.mcClient.get(self.lastAdded)
        if not lastAdded:
            self.mcClient.set(self.lastAdded, 0)

    def get(self):
        if len(self) > 0:
            lastRead = self.mcClient.incr(self.lastRead)
            value = self.mcClient.get('mq_%s_%s' % (self.name, lastRead))
            self.mcClient.delete('mq_%s_%s' % (self.name, lastRead))
            return value
        else:
            return None

    def add(self, value):
        lastAdded = self.mcClient.incr(self.lastAdded)
        self.mcClient.set('mq_%s_%s' % (self.name, lastAdded), value)

    def __len__(self):
        lastAdded = self.mcClient.get(self.lastAdded)
        lastRead = self.mcClient.get(self.lastRead)
        length = lastAdded - lastRead
        if length < 0:
            length = 0
        return length

