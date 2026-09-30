## com.apple.driver.AppleHIDTransportMailbox

> `com.apple.driver.AppleHIDTransportMailbox`

```diff

-9140.6.0.0.0
-  __TEXT.__const: 0xb5 sha256:c549ab945d8c3509598e975fb30e429768963f86330e3a48ad72ab7c555d1a34
-  __TEXT.__cstring: 0x25b7 sha256:f9502a23484540c3e1fe49514a9c732c1f39104584a4914e4824bc09fda7ddbd
-  __TEXT_EXEC.__text: 0x134b0 sha256:08c8707a48f698a51edda08291032261ba8c98987a7c865a0704497271fa15e4
+10100.34.0.0.0
+  __TEXT.__const: 0xda sha256:9fcd593b938d3c203403b8dc68d404c8712baf693dc97a5a6da927efe097cc6a
+  __TEXT.__cstring: 0x2de9 sha256:958e18919aa94d079468cbc4009aeaf064d644808f474355b9316ec2704dc5ed
+  __TEXT_EXEC.__text: 0x16420 sha256:99b2ab10789392141a317abab082d139e23b9381a3a3f16f8e7737c396b4cd75
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:31e0a352f4b791a5ad4f48ad97cafd6157a85e3a05f50ab14f6f16e49ce415fc
+  __DATA.__data: 0xc8 sha256:0a630c98994af0b68239c7f7462827f5b0abfbf08476e3a85cd0def5fdf636c9
   __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
-  __DATA_CONST.__auth_got: 0x1a8 sha256:bbfb617753c2ec82e8628447f4d620db76cf52f5a98742f820b2aaf8e30e0c0d
-  __DATA_CONST.__got: 0xc0 sha256:7e83113fdf2434af77ad9dc34d822320d642c80fb2ad3e971da62fd657b30a7e
-  __DATA_CONST.__mod_init_func: 0x10 sha256:8769b02c91deaa97022b7295adca0d16675ef445db9f2d00ee9912409dfe2224
-  __DATA_CONST.__mod_term_func: 0x10 sha256:7b936c118c52db8576e9bab2977fe276a23c7c0c942cf184fbac152ffc00af1a
-  __DATA_CONST.__const: 0x1118 sha256:8d27381244b1e886e48ddff1a8852d8578119d54ce4cb00e8859271f805b93fc
-  __DATA_CONST.__kalloc_type: 0x80 sha256:932dbbd26326dca766a9107957c40193ac45149976c901499d516500d9060f50
-  UUID: A7F3D386-05AF-3B9E-A2D9-29452811CE3E
-  Functions: 311
+  __DATA_CONST.__mod_init_func: 0x10 sha256:ea52894c1a0866ded3ab8987327bee0d60fa0eda395728b5da27cf080352af60
+  __DATA_CONST.__mod_term_func: 0x10 sha256:2abc3d4cd6b51a8dfbd403f58c42a178d5ea34aed68c0ac08389cf9e3293bdd7
+  __DATA_CONST.__const: 0x11d8 sha256:4d66cd56cf171f17314bbc1f4161f05b5c03de1df3af06d1b19856f22df2724f
+  __DATA_CONST.__kalloc_type: 0x80 sha256:82d67b9213dff4d9230b363ca398e5a9916cce9d8ae68c6389d6c98620d8a1a1
+  __DATA_CONST.__auth_got: 0x1c8 sha256:246421e7e52c1720390e7a1f48de23ff7a5976c46a15bd0512490f03ab96324f
+  __DATA_CONST.__got: 0xc0 sha256:d28213a9bcc605d989608d6358707e85e639cfcef807b269597fe628596e2431
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
