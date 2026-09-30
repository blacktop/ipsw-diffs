## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-1450.2.0.0.0
-  __TEXT.__cstring: 0x3e62 sha256:023fba5a681fe0576de7ae82317f0d6cf52361d8acc16818ae59a71ccf2ea07c
-  __TEXT.__os_log: 0x89ce sha256:95b0cd073398f3e6bad839eef076a278919c1655157e0430bc09dd3d66c1a76f
-  __TEXT.__const: 0x1d8 sha256:e42e48fadd9878068d64bc4eef3c36bf823c254d5a7f7c349fbf4f646dff9bc7
-  __TEXT_EXEC.__text: 0x30ca0 sha256:a575f1b5eb5d8b50779bd7becb6ae7063feae56207900b4441e68d8edfc5c1ca
+1500.96.0.0.0
+  __TEXT.__cstring: 0x3eaa sha256:f914e53a2befe17b81c1bce271c1411545ace798da2ea8d1f6718e352da868d1
+  __TEXT.__os_log: 0x8af5 sha256:bd07103116c667cce45e5b589c336806e38d78a1986e9bf0c93b04e695d6beb8
+  __TEXT.__const: 0x1e8 sha256:0374f1ed9e3a847c756289199b6a08fe2f97f4e3001e69827957bddff0e23120
+  __TEXT_EXEC.__text: 0x311c4 sha256:9733797e1278f9161914a76da8e0e6df62651247ce98410269cfe7792696948e
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xd4 sha256:f7beb4da12b49bb0a20393b7e11036ca7f6947c3109d544c772a46fc92c3c838
+  __DATA.__data: 0xd0 sha256:c4e361482c5875321113b9cf3a5603a039d85631d5ea292b2b778d1a93f2f107
   __DATA.__common: 0x688 sha256:256984cb62bc879971463ff0ff7567042dc95d8b0fb2bc676f246c2293c77ae8
-  __DATA.__bss: 0x41 sha256:98ce42deef51d40269d542f5314bef2c7468d401ad5d85168bfab4c0108f75f7
-  __DATA_CONST.__auth_got: 0x410 sha256:9dc7ee061d0d5d0ea3da2a448b4399af3d7ed0124bfa9c94a0ac5d0923ce91b2
-  __DATA_CONST.__got: 0xc0 sha256:9c6b1b0dce6283d66938af858733da8e3ad7a48f515f8850ec1264552cc86145
-  __DATA_CONST.__auth_ptr: 0x8 sha256:c1a58a10b09f9151fadb60e9f3b5a3863efe2f12cef5615c7ff9be0c640b57eb
-  __DATA_CONST.__mod_init_func: 0x100 sha256:62bcc578e0316901903b11b293b255bef6f6c3dbecd09cb4940048e5dc627cab
-  __DATA_CONST.__mod_term_func: 0x100 sha256:4c3e11804155eae09427c9400816a8282d673b8ead9433e0d30238b78f35360c
-  __DATA_CONST.__const: 0xc550 sha256:8f5844af57add1c5f550f613c8fe50c683bc56ff8f689bbfe1c6e9df23ae1c4d
-  __DATA_CONST.__kalloc_type: 0xe00 sha256:7f925e7b9577fadb9a5e08b387aeccdbeb4ca82545a05244aee29d9768b30a11
-  __DATA_CONST.__kalloc_var: 0x280 sha256:9b8e987e22591390ba2b5b45659a14a683ad9cd983dfab2b871ff81aeb598ebf
-  UUID: CF66D3C2-EE87-3278-8A38-FBF9BC7265CB
-  Functions: 1483
+  __DATA.__bss: 0x39 sha256:65a16cb7861335d5ace3c60718b5052e44660726da4cd13bb745381b235a1785
+  __DATA_CONST.__mod_init_func: 0x100 sha256:1eef909d6d857411dbbd4fdc834d6aa6769e96d9992a0518d16de0ffaff129da
+  __DATA_CONST.__mod_term_func: 0x100 sha256:c53a4175773efa90edc72f498cdcf8c1afb87637ecaecad5b61a44da9f8653c7
+  __DATA_CONST.__const: 0xc550 sha256:5d50b32371951e83f68dba9e7aa98fc4d6f7c616018378ee9ea4864517862e6e
+  __DATA_CONST.__kalloc_type: 0xe00 sha256:afcac1da53de26166fd8fe0e5593869ef115051571fa690ea501e9dcc0b9886d
+  __DATA_CONST.__kalloc_var: 0x280 sha256:96b0686649eec0698a918c1f4cfd32e88a8a67da115774875a9be9a409d06884
+  __DATA_CONST.__auth_got: 0x408 sha256:2ab7e7372d09eec82335b1a58944b1056e35280fdd5003605b00a83dbc25061d
+  __DATA_CONST.__got: 0xc0 sha256:2bb37d38d0b604b364601b4b46d507ff248b9037edb505f7481aec1ca965d4db
+  __DATA_CONST.__auth_ptr: 0x8 sha256:9058f2e22a0e1f0de3afbc9a54168f9813f9e39aaa03d5ee87bf91dc64606b89
+  UUID: 4BB0EC7F-BDA9-3CF1-88A1-4E70B88250AE
+  Functions: 1486
   Symbols:   0
-  CStrings:  721
+  CStrings:  724
 
CStrings:
+ "  %s(%s): *** DISCARDING STALE LINK %s EVENT *** (sequence %lld <= last processed %lld)"
+ "  %s(%s): Boot-arg timesync_ts_mode overriding %s%d mode from %d to %d"
+ "  %s(%s): Dropped %s message of type %s sequence %u port %u egress timed packet to %s\n"
+ "  %s(%s): Dropped %s message of type %s sequence %u port %u egress timed packet to %s and the timestamp was 0\n"
+ "  %s(%s): Dropped %s message of type %s sequence %u port %u egress timed packet to %s with error 0x%08x\n"
+ "  %s(%s): Failed to transmit %s message of type %s sequence %u port %u egress timed packet to %s with error 0x%08x\n"
+ "  %s(%s): PTP packet reception timing: WiFi HW timestamp: %llu, SW receive time: %llu, Delay: %llu ns (%llu ms)\n"
+ "  %s(%s): Packet info from mbuf: messageType %s sequence %u port %u now %llu timesynctime %llu"
+ "  %s(%s): TSNInterface: %s%d timestamping support updated to %d"
+ "  %s(%s): Transmitted %s message of type %s sequence %u port %u egress timed packet to %s but the timestamp (%llu) is in the future\n"
+ "  %s(%s): Transmitted %s message of type %s sequence %u port %u egress timed packet to %s but the timestamp (%llu) is invalid\n"
+ "  %s(%s): Transmitted %s message of type %s sequence %u port %u egress timed packet to %s but the timestamp was 0\n"
+ "  %s(%s): WARNING: PTP packet reception delay exceeds %llu ms threshold! WiFi HW timestamp: %llu, SW receive time: %llu, Delay: %llu ns (%llu ms)\n"
+ "  %s(%s): determineTimestampingSupport: %s%d original timestamping mode from WiFi driver = %d"
+ "  %s(%s): mbufTransmitCallback:  packet %p type=%s sequence: %u port %u timestamp %llu status 0x%08x dropped %u"
+ "  %s(%s): transmitTimeSyncPacket: packet %p messageType %s sequence %u port %u timestamp %llu"
+ "12111112122212121111211111122111"
+ "121111121222121211112111111221112222112"
+ "121111121222121211112111111221112222112111222222"
+ "1211111212221212111121111112211122221121112222222"
+ "121111121222121212112221211222221211112111121111222222211"
+ "1211111212221212121122212112222212111121111211112222222111"
+ "121111121222121212112221211222221211112111121111222222211111112122222"
+ "12111112122212121211222121122222121111211112111122222221111111212222211"
+ "12111112122212121211222121122222121111211112111122222221111111212222222221"
+ "Boot-arg set PTP packet reception delay threshold to %u ms\n"
+ "Boot-arg timesync_ts_mode=%d out of range (%d-%d), ignoring"
+ "Boot-arg timesync_ts_mode=%d out of range (%d-%d), ignoring\n"
+ "ClockName"
+ "ClockTransportType"
+ "Failed to allocate properties dictionary\n"
+ "Failed to allocate service lock\n"
+ "NULL == fClockIDLock"
+ "NULL == fIOTimeSyncServiceLock"
+ "NULL == properties"
+ "Timeout waiting for timesync node to match, _timesyncNode=%p\n"
+ "timesync_rx_delay_threshold_ms"
- "  %s(%s): *** DISCARDING STALE LINK %s EVENT *** (sequence %lld < last processed %lld)"
- "  %s(%s): Dropped %s message of type %s sequence %u egress timed packet to %s\n"
- "  %s(%s): Dropped %s message of type %s sequence %u egress timed packet to %s and the timestamp was 0\n"
- "  %s(%s): Dropped %s message of type %s sequence %u egress timed packet to %s with error 0x%08x\n"
- "  %s(%s): Failed to transmit %s message of type %s sequence %u egress timed packet to %s with error 0x%08x\n"
- "  %s(%s): Packet info from mbuf: messageType %s sequence %u now %llu timesynctime %llu"
- "  %s(%s): STALE EVENT DETECTED but fix disabled: %s (seq=%lld < last=%lld)"
- "  %s(%s): STALE messageClients DETECTED but fix disabled: %s (seq=%lld < last=%lld)"
- "  %s(%s): TimeSync: [Scenario A] DOWN event (seq=%lld) delay complete"
- "  %s(%s): TimeSync: [Scenario A] DOWN event (seq=%lld) delaying %d ms before lock"
- "  %s(%s): TimeSync: [Scenario B] DOWN event (seq=%lld) delay complete"
- "  %s(%s): TimeSync: [Scenario B] DOWN event (seq=%lld) delaying %d ms after stopTimeSyncCallbackThread"
- "  %s(%s): Transmitted %s message of type %s sequence %u egress timed packet to %s but the timestamp (%llu) is in the future\n"
- "  %s(%s): Transmitted %s message of type %s sequence %u egress timed packet to %s but the timestamp (%llu) is invalid\n"
- "  %s(%s): Transmitted %s message of type %s sequence %u egress timed packet to %s but the timestamp was 0\n"
- "  %s(%s): mbufTransmitCallback:  packet %p type=%s sequence: %u timestamp %llu status 0x%08x dropped %u"
- "  %s(%s): transmitTimeSyncPacket: packet %p messageType %s sequence %u timestamp %llu"
- "121111121222121211111111122111"
- "1211111212221212111111111221112222112"
- "1211111212221212111111111221112222112111222222"
- "12111112122212121111111112211122221121112222222"
- "12111112122212121211221211222221211112111121111222222211"
- "121111121222121212112212112222212111121111211112222222111"
- "1211111212221212121122121122222121111211112111122222221111111212222"
- "121111121222121212112212112222212111121111211112222222111111121222211"
- "121111121222121212112212112222212111121111211112222222111111121222222221"
- "Boot-arg specifying timestamp mode override %d which is outside supported range of %d to %d\n"
- "Interface %s%d specified timestamp mode %d but overridden with %d due to boot-arg\n"
- "TimeSync: Invalid delay1 value %d, using 0\n"
- "TimeSync: Invalid delay2 value %d, using 0\n"
- "TimeSync: Link state fix initialized: enabled=%d, delay1=%dms, delay2=%dms\n"
- "timesync_linkstate_delay1"
- "timesync_linkstate_delay2"
- "timesync_linkstate_fix"

```
