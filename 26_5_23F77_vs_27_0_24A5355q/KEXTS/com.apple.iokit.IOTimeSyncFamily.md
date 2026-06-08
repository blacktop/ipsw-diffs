## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-1450.2.0.0.0
-  __TEXT.__cstring: 0x3e62
-  __TEXT.__os_log: 0x89ce
-  __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x30ca0
+1500.96.0.0.0
+  __TEXT.__cstring: 0x3eaa
+  __TEXT.__os_log: 0x8af5
+  __TEXT.__const: 0x1e8
+  __TEXT_EXEC.__text: 0x311c4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xd4
+  __DATA.__data: 0xd0
   __DATA.__common: 0x688
-  __DATA.__bss: 0x41
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__bss: 0x39
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
   __DATA_CONST.__const: 0xc550
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: CF66D3C2-EE87-3278-8A38-FBF9BC7265CB
-  Functions: 1483
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_ptr: 0x8
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
