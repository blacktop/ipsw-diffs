## com.apple.driver.AppleHIDTransportMailbox

> `com.apple.driver.AppleHIDTransportMailbox`

```diff

-9140.6.0.0.0
-  __TEXT.__const: 0xb5
-  __TEXT.__cstring: 0x25b7
-  __TEXT_EXEC.__text: 0x134b0
+10100.34.0.0.0
+  __TEXT.__const: 0xda
+  __TEXT.__cstring: 0x2de9
+  __TEXT_EXEC.__text: 0x16420
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x1118
+  __DATA_CONST.__const: 0x11d8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: A7F3D386-05AF-3B9E-A2D9-29452811CE3E
-  Functions: 311
+  __DATA_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0xc0
+  UUID: 441C20C3-BF5D-30B7-8FD3-AB19B58F9232
+  Functions: 333
   Symbols:   0
-  CStrings:  252
+  CStrings:  285
 
CStrings:
+ "\"[%s::%s] Invalid message read from the FIFO ID %u, interface ID %u, report ID 0x%02X, transfer ID 0x%02X: invalid checksum (read: 0x%08X, calculated: 0x%08X)\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %u, interface ID %u: header size too large\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %u, interface ID %u: message exceeds capacity %llu bytes\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %u, interface ID %u: read beyond message boundary\" @%s:%d"
+ "\"[%s::%s] Invalid message type received: %d from polling FIFO\" @%s:%d"
+ "121111121222121211111112112121111111121121121121121121121121121121121121121121121121121121121121121121121121121121121121121121121122212221222122212221222122212221222122212221222122212221222122212222111111211121"
+ "1211111212221212111112111221121111111111111222"
+ "NULL"
+ "Off Without Reset"
+ "Watermark"
+ "[0x%llx][%llx][%s::%s]: Blocking polling FIFO %d (%s)"
+ "[0x%llx][%llx][%s::%s]: Creating polling FIFO '%s' on the first pollData call"
+ "[0x%llx][%llx][%s::%s]: Deferring creation of polling FIFO '%s' until the first pollData call"
+ "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainFifo: Failed to block polling FIFO %d (%s), ret=0x%08X (%s)"
+ "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainFifo: drain already active"
+ "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainFifo: polling FIFO %s not found"
+ "[0x%llx][%llx][%s::%s]: ERROR!! endDrainFifo: no drain in progress"
+ "[0x%llx][%llx][%s::%s]: ERROR!! endDrainFifo: polling FIFO %s not found"
+ "[0x%llx][%llx][%s::%s]: ERROR!! pollData failed with ret=0x%08X (%s)"
+ "[0x%llx][%llx][%s::%s]: ERROR!! pollData: FIFO %s requires blocking dequeue but beginDrainFifo was not called"
+ "[0x%llx][%llx][%s::%s]: ERROR!! polling FIFO %s not found"
+ "[0x%llx][%llx][%s::%s]: Polling FIFO '%s' configured with blocking consume"
+ "[0x%llx][%llx][%s::%s]: Polling data buffer full, current write offset %llu, data size %llu, max data size %llu"
+ "[0x%llx][%llx][%s::%s]: Polling succeeds, wrote %llu bytes to the buffer"
+ "[0x%llx][%llx][%s::%s]: Running out of space during polling, buffer size is %llu, written size is %llu"
+ "[0x%llx][%llx][%s::%s]: Unblocking polling FIFO %d (%s)"
+ "[0x%llx][%llx][%s::%s]: beginDrainFifo: FIFO %s drain started"
+ "[0x%llx][%llx][%s::%s]: beginDrainFifo: FIFO %s is empty, skipping drain"
+ "[0x%llx][%llx][%s::%s]: endDrainFifo: FIFO %s drain ended"
+ "[0x%llx][%llx][%s::%s]: pollData: draining FIFO %d (%s), type=%d, maxDataSize=%llu"
+ "_maxRegularReadFifoUsage"
+ "_maxRegularReadFifoUsage && _interfaceReportSizePerFifo && _interfaceReportCountPerFifo"
+ "beginDrainFifo"
+ "blockPollingFifo"
+ "bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow."
+ "createPollingFifo"
+ "endDrainFifo"
+ "pollData"
+ "processPollingData"
+ "unblockPollingFifo"
+ "writePollingMessageToBuffer"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: header size too large\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: invalid checksum\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: message exceeds capacity %llu bytes\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: read beyond message boundary\" @%s:%d"
- "121111121222121211111112112121111111121121121121121121121121121121121121121121121121121121121121121121121121121121121121121121121122212121212121212121212121212121212211111121112"
- "121111121222121211111211122112111111111111222"
- "_maxIopToApFifoUsage"
- "_maxIopToApFifoUsage && _interfaceReportSizePerFifo && _interfaceReportCountPerFifo"

```
