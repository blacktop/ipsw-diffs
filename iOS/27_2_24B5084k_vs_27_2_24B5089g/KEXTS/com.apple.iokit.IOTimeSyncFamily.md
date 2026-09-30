## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-1510.7.0.0.0
-  __TEXT.__cstring: 0x4004
-  __TEXT.__os_log: 0x8f3a
+1510.8.0.0.0
+  __TEXT.__cstring: 0x3eb8
+  __TEXT.__os_log: 0x8c04
   __TEXT.__const: 0x1e8
-  __TEXT_EXEC.__text: 0x31b7c
+  __TEXT_EXEC.__text: 0x30c48
   __TEXT_EXEC.__auth_stubs: 0x810
   __DATA.__data: 0xd0
   __DATA.__common: 0x688
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0xc550
-  __DATA_CONST.__kalloc_type: 0xe00
+  __DATA_CONST.__const: 0xc510
+  __DATA_CONST.__kalloc_type: 0xd40
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__auth_got: 0x408
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1492
+  Functions: 1474
   Symbols:   0
-  CStrings:  749
+  CStrings:  728
 
CStrings:
+ "121111121222121212112221211222221211112111121111222222211111112122222222222"
+ "getTransmitTimestamp(packet, &timestamp) == kIOReturnSuccess"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
- "1211111212221212121122212112222212111121111211112222222111111121222222222221"
- "12222"
- "2222222222222222221"
- "Dropping %llu packets from sequence diff (%llu -> %llu)"
- "First t1 timestamp = %llu"
- "First t2 timestamp = %llu"
- "Maximum timestamp, resetting replay"
- "Starting timestamp replay"
- "Stopped timestamp replay"
- "Stopping timestamp replay"
- "Unexpected sync received on GM"
- "[%u] delay request Replayed t3 = %llu -> %llu"
- "[%u] delay request Replayed t4 = %llu -> %llu"
- "[%u] delay response Replayed t4 = %llu -> %llu"
- "[%u] follow up Replayed t1, %llu -> %llu"
- "[%u] sync Replayed t1, %llu -> %llu"
- "[%u] sync Replayed t2, %llu -> %llu"
- "getTransmitTimestamp(packet, &timestamp, &futurePermitted) == kIOReturnSuccess"
- "length == packetLength"
- "payload != nullptr"
- "site.TSNBSDTestInterfaceReplayTimestamps"
- "site.TSReplayTimestamps"
```
