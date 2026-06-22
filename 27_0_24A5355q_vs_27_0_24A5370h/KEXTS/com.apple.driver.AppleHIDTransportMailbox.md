## com.apple.driver.AppleHIDTransportMailbox

> `com.apple.driver.AppleHIDTransportMailbox`

```diff

-10100.34.0.0.0
-  __TEXT.__const: 0xda sha256:9fcd593b938d3c203403b8dc68d404c8712baf693dc97a5a6da927efe097cc6a
-  __TEXT.__cstring: 0x2de9 sha256:958e18919aa94d079468cbc4009aeaf064d644808f474355b9316ec2704dc5ed
-  __TEXT_EXEC.__text: 0x16420 sha256:99b2ab10789392141a317abab082d139e23b9381a3a3f16f8e7737c396b4cd75
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:0a630c98994af0b68239c7f7462827f5b0abfbf08476e3a85cd0def5fdf636c9
-  __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
-  __DATA_CONST.__mod_init_func: 0x10 sha256:ea52894c1a0866ded3ab8987327bee0d60fa0eda395728b5da27cf080352af60
-  __DATA_CONST.__mod_term_func: 0x10 sha256:2abc3d4cd6b51a8dfbd403f58c42a178d5ea34aed68c0ac08389cf9e3293bdd7
-  __DATA_CONST.__const: 0x11d8 sha256:4d66cd56cf171f17314bbc1f4161f05b5c03de1df3af06d1b19856f22df2724f
-  __DATA_CONST.__kalloc_type: 0x80 sha256:82d67b9213dff4d9230b363ca398e5a9916cce9d8ae68c6389d6c98620d8a1a1
-  __DATA_CONST.__auth_got: 0x1c8 sha256:246421e7e52c1720390e7a1f48de23ff7a5976c46a15bd0512490f03ab96324f
-  __DATA_CONST.__got: 0xc0 sha256:d28213a9bcc605d989608d6358707e85e639cfcef807b269597fe628596e2431
-  UUID: 441C20C3-BF5D-30B7-8FD3-AB19B58F9232
-  Functions: 333
+10100.38.1.0.0
+  __TEXT.__const: 0x11d sha256:1d4293604c4bc63255ba0ee108a70dc664689c63657ad19e410e7519394840a9
+  __TEXT.__cstring: 0x33cc sha256:32e91241d93bf9f1f4c6df22ed653edac9452c3fe6be5896b47ac75fa5c90d97
+  __TEXT_EXEC.__text: 0x18058 sha256:14a8722075e60aca60c36173b22be5e3b007c073c290a7ea73d1f304dacb55e5
+  __TEXT_EXEC.__auth_stubs: 0x440 sha256:d20f61b45dd4433fca7e40aedcff1e5072a614538d6e11844e768d7b786a6eec
+  __DATA.__data: 0xc8 sha256:7108109af7227f4590e03da0fbe95ea44c02dbb6b7a4ca3449c5e2949682496b
+  __DATA.__common: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
+  __DATA_CONST.__mod_init_func: 0x10 sha256:ee437b642067b0f8d390d89275b5874ba76cab08ab7e04ff223ea97e4aa69038
+  __DATA_CONST.__mod_term_func: 0x10 sha256:77ed3fca79a52560fca0205467ec19a25ca0e24db929aee42d5eac12b712434b
+  __DATA_CONST.__const: 0x13d8 sha256:29c1d17659d86700f2b843676b7b5e2ceaed064e08a422469d19939f996ddd25
+  __DATA_CONST.__kalloc_type: 0xc0 sha256:ee9e8e88c26f301bd33fd9983e4610f4fc8ffdf550ada48962b1fad08756aaa4
+  __DATA_CONST.__auth_got: 0x220 sha256:1b462468b787971c441c872bdfaa54ed53d22a1e5e167ab905e6d1e9d87e3a05
+  __DATA_CONST.__got: 0xd0 sha256:207bb5dc5b74d848aaed47bbaa2632c4d52252b26dea039187cc28f9c467adde
+  UUID: D8A4E179-C703-3E43-910C-A56225D92DFE
+  Functions: 366
   Symbols:   0
-  CStrings:  285
+  CStrings:  308
 
CStrings:
+ "1211111212221212111111121121211111111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211222122212221222122212221222122212221222122212221222122212221222122221111112111211222"
+ "12111112122212121111121112211211111111111112221"
+ "121112111112"
+ "NonPollingFifoDrainEventSource"
+ "[0x%llx][%llx][%s::%s]: Creating polling FIFO '%s' on the first drainPollingFifo call"
+ "[0x%llx][%llx][%s::%s]: Deferring creation of polling FIFO '%s' until the first drainPollingFifo call"
+ "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainPollingFifo: Failed to block polling FIFO %d (%s), ret=0x%08X (%s)"
+ "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainPollingFifo: drain already active"
+ "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainPollingFifo: polling FIFO %s not found"
+ "[0x%llx][%llx][%s::%s]: ERROR!! drain failed with ret=0x%08X (%s)"
+ "[0x%llx][%llx][%s::%s]: ERROR!! drainPollingFifo failed with ret=0x%08X (%s)"
+ "[0x%llx][%llx][%s::%s]: ERROR!! drainPollingFifo: FIFO %s requires blocking dequeue but beginDrainPollingFifo was not called"
+ "[0x%llx][%llx][%s::%s]: ERROR!! dropped frame for interface %u (reportSize=%u, writable=%u, total dropped=%u)"
+ "[0x%llx][%llx][%s::%s]: ERROR!! endDrainPollingFifo: no drain in progress"
+ "[0x%llx][%llx][%s::%s]: ERROR!! endDrainPollingFifo: polling FIFO %s not found"
+ "[0x%llx][%llx][%s::%s]: ERROR!! failed to allocate input report logging buffer (%u bytes)"
+ "[0x%llx][%llx][%s::%s]: ERROR!! invalid interfaceID %u"
+ "[0x%llx][%llx][%s::%s]: ERROR!! slow path triggered: %u bytes buffered exceeds %llu bytes available in output buffer. Per-entry drain is suboptimal; increase user-client output buffer to >= logging buffer capacity (%u bytes)."
+ "[0x%llx][%llx][%s::%s]: allocated input report logging buffer (%u bytes, watermark %u bytes)"
+ "[0x%llx][%llx][%s::%s]: beginDrainPollingFifo: FIFO %s drain started"
+ "[0x%llx][%llx][%s::%s]: beginDrainPollingFifo: FIFO %s is empty, skipping drain"
+ "[0x%llx][%llx][%s::%s]: drainPollingFifo: draining FIFO %d (%s), type=%d, maxDataSize=%llu"
+ "[0x%llx][%llx][%s::%s]: drained %u bytes, %u bytes remaining (slow path)"
+ "[0x%llx][%llx][%s::%s]: drained %u bytes, 0 bytes remaining"
+ "[0x%llx][%llx][%s::%s]: endDrainPollingFifo: FIFO %s drain ended"
+ "[0x%llx][%llx][%s::%s]: interface %u %s, mask=0x%08X"
+ "[0x%llx][%llx][%s::%s]: interface %u, reportSize=%u, entrySize=%u, readable=%u/%u"
+ "[0x%llx][%llx][%s::%s]: released input report logging buffer"
+ "[0x%llx][%llx][%s::%s]: watermark reached (readable=%u, watermark=%u), notifying user clients"
+ "[0x%llx][%llx][%s::%s]: wrote %llu bytes, %u bytes remaining"
+ "_nonPollingFifoDrainEventSource"
+ "beginDrainPollingFifo"
+ "disabled"
+ "drainInputReportLoggingBuffer"
+ "drainInputReportLoggingBufferEntries"
+ "drainPollingFifo"
+ "enableInputReportLogging"
+ "enabled"
+ "endDrainPollingFifo"
+ "site.NonPollingFifoDrainEventSource"
+ "writeToInputReportLoggingBuffer"
- "121111121222121211111112112121111111121121121121121121121121121121121121121121121121121121121121121121121121121121121121121121121122212221222122212221222122212221222122212221222122212221222122212222111111211121"
- "1211111212221212111112111221121111111111111222"
- "[0x%llx][%llx][%s::%s]: Creating polling FIFO '%s' on the first pollData call"
- "[0x%llx][%llx][%s::%s]: Deferring creation of polling FIFO '%s' until the first pollData call"
- "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainFifo: Failed to block polling FIFO %d (%s), ret=0x%08X (%s)"
- "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainFifo: drain already active"
- "[0x%llx][%llx][%s::%s]: ERROR!! beginDrainFifo: polling FIFO %s not found"
- "[0x%llx][%llx][%s::%s]: ERROR!! endDrainFifo: no drain in progress"
- "[0x%llx][%llx][%s::%s]: ERROR!! endDrainFifo: polling FIFO %s not found"
- "[0x%llx][%llx][%s::%s]: ERROR!! pollData failed with ret=0x%08X (%s)"
- "[0x%llx][%llx][%s::%s]: ERROR!! pollData: FIFO %s requires blocking dequeue but beginDrainFifo was not called"
- "[0x%llx][%llx][%s::%s]: beginDrainFifo: FIFO %s drain started"
- "[0x%llx][%llx][%s::%s]: beginDrainFifo: FIFO %s is empty, skipping drain"
- "[0x%llx][%llx][%s::%s]: endDrainFifo: FIFO %s drain ended"
- "[0x%llx][%llx][%s::%s]: pollData: draining FIFO %d (%s), type=%d, maxDataSize=%llu"
- "beginDrainFifo"
- "endDrainFifo"
- "pollData"

```
