## com.apple.driver.AppleHIDTransportMailbox

> `com.apple.driver.AppleHIDTransportMailbox`

```diff

-  __TEXT.__const: 0x11d
-  __TEXT.__cstring: 0x33cc
-  __TEXT_EXEC.__text: 0x18058
-  __TEXT_EXEC.__auth_stubs: 0x440
+  __TEXT.__const: 0x125
+  __TEXT.__cstring: 0x3357
+  __TEXT_EXEC.__text: 0x17c98
+  __TEXT_EXEC.__auth_stubs: 0x420
   __DATA.__data: 0xc8
-  __DATA.__common: 0x88
+  __DATA.__common: 0x60
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x13d8
-  __DATA_CONST.__kalloc_type: 0xc0
-  __DATA_CONST.__auth_got: 0x220
-  __DATA_CONST.__got: 0xd0
-  Functions: 366
+  __DATA_CONST.__const: 0x12e0
+  __DATA_CONST.__kalloc_type: 0x80
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0xc0
+  Functions: 357
   Symbols:   0
-  CStrings:  308
+  CStrings:  307
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
CStrings:
+ "\"[%s::%s] Invalid message type received: %d from polling FIFO %s\" @%s:%d"
+ "1211111212221212111111121121211111111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211222122212221222122212221222122212221222122212221222122212221222122221111112211121222"
+ "12111112122212121111121112211211111111111111222"
+ "[0x%llx][%llx][%s::%s]: Deferring creation of polling FIFO '%s' until the first drainPollingFifoNonGated call"
+ "[0x%llx][%llx][%s::%s]: Draining FIFO %d (%s), type=%d, maxDataSize=%llu"
+ "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainPollingFifo: polling FIFO %d (%s) is already busy"
+ "[0x%llx][%llx][%s::%s]: ERROR!! drainPollingFifoNonGated failed with ret=0x%08X (%s), wrote %llu bytes"
+ "[0x%llx][%llx][%s::%s]: Peek %llu bytes from %s to AP FIFO %s"
+ "_sharedMemoryManager->isFifoAcquired(pollingFifoInfo->fifoID)"
+ "drainPollingFifoNonGated"
+ "drainPollingFifoNonGated_block_invoke"
+ "msgBuffer"
+ "peekPollingFifoMessagesNonGated"
+ "pollingFifoInfo && pollingFifoInfo->fifoCreated"
+ "readMessage"
- "\"[%s::%s] Invalid message type received: %d from polling FIFO\" @%s:%d"
- "1211111212221212111111121121211111111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211222122212221222122212221222122212221222122212221222122212221222122221111112111211222"
- "12111112122212121111121112211211111111111112221"
- "121112111112"
- "NonPollingFifoDrainEventSource"
- "[0x%llx][%llx][%s::%s]: Deferring creation of polling FIFO '%s' until the first drainPollingFifo call"
- "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainPollingFifo: drain already active"
- "[0x%llx][%llx][%s::%s]: ERROR!! drainPollingFifo failed with ret=0x%08X (%s)"
- "[0x%llx][%llx][%s::%s]: ERROR!! drainPollingFifo: FIFO %s requires blocking dequeue but beginDrainPollingFifo was not called"
- "[0x%llx][%llx][%s::%s]: ERROR!! dropped frame for interface %u (reportSize=%u, writable=%u, total dropped=%u)"
- "[0x%llx][%llx][%s::%s]: ERROR!! polling FIFO %s not found"
- "[0x%llx][%llx][%s::%s]: drainPollingFifo: draining FIFO %d (%s), type=%d, maxDataSize=%llu"
- "_nonPollingFifoDrainEventSource"
- "drainPollingFifo"
- "processPollingData"
- "site.NonPollingFifoDrainEventSource"

```
