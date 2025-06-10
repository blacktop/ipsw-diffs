## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-1340.12.0.0.0
-  __TEXT.__cstring: 0x32b0
-  __TEXT.__os_log: 0x7798
+1400.53.0.0.0
+  __TEXT.__cstring: 0x368d
+  __TEXT.__os_log: 0x8568
   __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x31c94
+  __TEXT_EXEC.__text: 0x35008
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
-  __DATA.__common: 0x638
+  __DATA.__common: 0x688
   __DATA.__bss: 0x39
-  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__auth_got: 0x408
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0xf8
-  __DATA_CONST.__mod_term_func: 0xf8
-  __DATA_CONST.__const: 0xbda0
-  __DATA_CONST.__kalloc_type: 0xbc0
+  __DATA_CONST.__mod_init_func: 0x100
+  __DATA_CONST.__mod_term_func: 0x100
+  __DATA_CONST.__const: 0xc550
+  __DATA_CONST.__kalloc_type: 0xd00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 6CCC918C-4B0E-3972-B2D2-928A2ADC22FE
-  Functions: 1389
+  UUID: 07446F90-4C49-3E05-8D9B-23B2ADAED30E
+  Functions: 1458
   Symbols:   0
-  CStrings:  635
+  CStrings:  699
 
CStrings:
+ "  %s(%s): Packet info from mbuf: messageType %s sequence %u now %llu timesynctime %llu"
+ " IOTimeSyncFamily assertion FailIfNULLWithAction \"%s\" failed in %s at line %d goto Exit. "
+ " IOTimeSyncFamily assertion FailIfWithAction \"%s\" failed in %s at line %d goto Exit. "
+ "!fPersistentUserFilteredClocks->setObject(userID, mapping)"
+ "!mapping->init(userID, *clockID)"
+ "%s::%s %u\n"
+ "/Library/Caches/com.apple.xbs/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
+ "12111112122212121122222212121111111112111"
+ "121111121222121212112212112212111121111211112222222111111121222222221"
+ "12122"
+ "12222"
+ "2222222222222222221"
+ "Dropping %llu packets from sequence diff (%llu -> %llu)"
+ "Failed clockID num allocation\n"
+ "Failed persistent clock mapping allocation\n"
+ "Failed to add mapping for persistent clock\n"
+ "Failed to allocate tsn capture lock\n"
+ "Failed to remove user filtered clock on cleanup: %llx\n"
+ "Failed to remove user filtered clock: %llx, Error: %d (0x%X)\n"
+ "First t1 timestamp = %llu"
+ "First t2 timestamp = %llu"
+ "IOTimeSyncPersistentUserClockMapping"
+ "Init user clock map failed\n"
+ "Injected pdelay %llu for frameType = %u"
+ "MAC address data length length is smaller (%u) than expected (%u)"
+ "Maximum timestamp, resetting replay"
+ "NULL == clockIDNum"
+ "NULL == fPersistentUserFilteredClocks"
+ "NULL == fPersistentUserFilteredClocksLock"
+ "NULL == mapping"
+ "NULL == userID"
+ "NULL clockID\n"
+ "NULL userID\n"
+ "Negative reference count (%i) for persistent user filtered clock: %s\n"
+ "Persistent clock doesn't exist: %s\n"
+ "Persistent user filtered clock already exists: %s\n"
+ "Persistent user filtered clock does not exist: %s\n"
+ "Resetting Propagation Delay Injection"
+ "Starting timestamp replay"
+ "Stopped timestamp replay"
+ "Stopping timestamp replay"
+ "TSNBSDTestInterface"
+ "Unexpected packet == nullptr"
+ "Unexpected sync received on GM"
+ "Unexpected timestamp == nullptr"
+ "[%u] delay request Replayed t3 = %llu -> %llu"
+ "[%u] delay request Replayed t4 = %llu -> %llu"
+ "[%u] delay response Replayed t4 = %llu -> %llu"
+ "[%u] follow up Replayed t1, %llu -> %llu"
+ "[%u] sync Replayed t1, %llu -> %llu"
+ "[%u] sync Replayed t2, %llu -> %llu"
+ "fPersistentUserFilteredClocks->getObject(userID)"
+ "fReferenceCount < 0"
+ "failed to allocate persistent user clocks dict\n"
+ "failed to allocate persistent user clocks lock\n"
+ "getTransmitTimestamp(packet, &timestamp, &futurePermitted) == kIOReturnSuccess"
+ "kIOReturnSuccess != removeUserFilteredClock(*clockID)"
+ "length == packetLength"
+ "payload != nullptr"
+ "site.IOTimeSyncPersistentUserClockMapping"
+ "site.TSNBSDTestInterface"
+ "site.TSNBSDTestInterfaceReplayTimestamps"
+ "site.TSReplayTimestamps"
+ "stop"
+ "timestamp != nullptr"
+ "timesync_rand_pdelay_base_ms"
+ "timesync_rand_pdelay_period"
+ "timesync_rand_pdelay_range_ms"
- "  %s(%s): Packet info from mbuf: messageType %s sequence %u packetTimestamp %llu now %llu timesynctime %llu packetTimestampValid %d interfaceProvidesTimestamps %d"
- "121111121222121211222222121211111112111"
- "Failed to allocate lock\n"
- "IOTimeSyncDaemonClientBase::stop %u\n"

```
