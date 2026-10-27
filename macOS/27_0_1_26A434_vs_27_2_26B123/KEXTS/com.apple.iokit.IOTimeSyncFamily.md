## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-1501.7.0.0.0
-  __TEXT.__cstring: 0x4425
-  __TEXT.__os_log: 0x8ea3
+1510.9.0.0.0
+  __TEXT.__cstring: 0x432b
+  __TEXT.__os_log: 0x8dc8
   __TEXT.__const: 0x1e8
-  __TEXT_EXEC.__text: 0x34c98
+  __TEXT_EXEC.__text: 0x343c4
   __TEXT_EXEC.__auth_stubs: 0x820
   __DATA.__data: 0xd0
   __DATA.__common: 0x688
   __DATA.__bss: 0x39
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0x15410
-  __DATA_CONST.__kalloc_type: 0xe00
+  __DATA_CONST.__const: 0x153f0
+  __DATA_CONST.__kalloc_type: 0xd40
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1778
-  Symbols:   3025
-  CStrings:  745
+  Functions: 1765
+  Symbols:   3003
+  CStrings:  735
 
Symbols:
+ _ZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPy
+ _ZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPy
+ _ZN23TSNWiFiControlInterface11wifiChipsetEP9IOService
+ __ZL26chipsetForBundleIdentifierP8OSString
+ __ZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPy
+ __ZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPy
+ __ZN15TSNBSDInterface34setUntimestampedGeneralMessageMaskEj
+ __ZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPy
+ __ZN23TSNWiFiControlInterface11wifiChipsetEP9IOService
+ __ZN23TSNWiFiControlInterface43untimestampedGeneralMessageMaskForInterfaceEP9IOService
+ __ZZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyE11_os_log_fmt
+ __ZZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyE11_os_log_fmt_0
+ __ZZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyE11_os_log_fmt_1
+ __ZZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyE28logValidFlagOnSwTimestamping
+ __ZZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyE11_os_log_fmt
+ __ZZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyE11_os_log_fmt_0
+ __ZZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyE11_os_log_fmt_1
+ __ZZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyE11_os_log_fmt_2
+ __ZZN15TSNBSDInterface22logInterfaceStatisticsEvE11_os_log_fmt_2
+ __ZZN15TSNBSDInterface22transmitTimeSyncPacketEP9TSNPacketyE11_os_log_fmt_5
+ __ZZN15TSNBSDInterface34setUntimestampedGeneralMessageMaskEjE11_os_log_fmt
+ __ZZN15TSNBSDInterface34setUntimestampedGeneralMessageMaskEjE11_os_log_fmt_0
+ __ZZN15TSNBSDInterface4initE18TSNEthernetAddressP8OSStringt16TSNInterfaceType22TSNTimestampingSupportP8IOMapperbP12OSDictionaryE11_os_log_fmt_5
+ __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyE11_os_log_fmt
+ __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyE11_os_log_fmt_0
+ __ZZN23TSNWiFiControlInterface11wifiChipsetEP9IOServiceE11_os_log_fmt
+ __ZZN23TSNWiFiControlInterface11wifiChipsetEP9IOServiceE11_os_log_fmt_0
+ __ZZN23TSNWiFiControlInterface11wifiChipsetEP9IOServiceE11_os_log_fmt_1
- _Z11parsePacketP9TSNPacketPhm
- _ZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPb
- _ZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyPb
- __Z11parsePacketP9TSNPacketPhm
- __ZL22getMachReplayTimestampP35TSNBSDTestInterfaceReplayTimestampsh
- __ZN15TSNBSDInterface16shouldDropPacketEP9TSNPacket
- __ZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPb
- __ZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyPb
- __ZN19TSNBSDTestInterface16shouldDropPacketEP9TSNPacket
- __ZN19TSNBSDTestInterface17getNextReplaySyncEP25IOTimeSyncgPTPSyncPayload
- __ZN19TSNBSDTestInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPb
- __ZN19TSNBSDTestInterface20dockReplayTimestampsEP18TSReplayTimestamps
- __ZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPb
- __ZN19TSNBSDTestInterface20stopReplayTimestampsEv
- __ZN19TSNBSDTestInterface21resetReplayTimestampsEv
- __ZN19TSNBSDTestInterface21startReplayTimestampsEv
- __ZN19TSNBSDTestInterface4freeEv
- __ZZ11parsePacketP9TSNPacketPhmE11_os_log_fmt
- __ZZ11parsePacketP9TSNPacketPhmE11_os_log_fmt_0
- __ZZ11parsePacketP9TSNPacketPhmE11_os_log_fmt_1
- __ZZ11parsePacketP9TSNPacketPhmE11_os_log_fmt_2
- __ZZ11parsePacketP9TSNPacketPhmE11_os_log_fmt_3
- __ZZ11parsePacketP9TSNPacketPhmE11_os_log_fmt_4
- __ZZL16incrementInfoIdxP35TSNBSDTestInterfaceReplayTimestampsE11_os_log_fmt
- __ZZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPbE11_os_log_fmt
- __ZZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPbE11_os_log_fmt_0
- __ZZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPbE11_os_log_fmt_1
- __ZZN15TSNBSDInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPbE28logValidFlagOnSwTimestamping
- __ZZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt
- __ZZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_0
- __ZZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_1
- __ZZN15TSNBSDInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_2
- __ZZN19TSNBSDTestInterface16shouldDropPacketEP9TSNPacketE11_os_log_fmt
- __ZZN19TSNBSDTestInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPbE11_os_log_fmt
- __ZZN19TSNBSDTestInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPbE11_os_log_fmt_0
- __ZZN19TSNBSDTestInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPbE11_os_log_fmt_1
- __ZZN19TSNBSDTestInterface19getReceiveTimestampEP9TSNPacketP6__mbufPyPbE11_os_log_fmt_2
- __ZZN19TSNBSDTestInterface20dockReplayTimestampsEP18TSReplayTimestampsE20kalloc_type_view_544
- __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt
- __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_0
- __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_1
- __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_2
- __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_3
- __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_4
- __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_5
- __ZZN19TSNBSDTestInterface20getTransmitTimestampEP9TSNPacketPyPbE11_os_log_fmt_6
- __ZZN19TSNBSDTestInterface20stopReplayTimestampsEvE11_os_log_fmt
- __ZZN19TSNBSDTestInterface21startReplayTimestampsEvE11_os_log_fmt
- __ZZN19TSNBSDTestInterface4freeEvE20kalloc_type_view_147
- __ZZN19TSNBSDTestInterface4freeEvE20kalloc_type_view_150
CStrings:
+ "  %s(%s): Egress Untimestamped Packet Count: %u, Count since last log entry: %u (timestamping type %u, untimestamped general message mask 0x%x)\n"
+ "  %s(%s): Failed to transmit message of type %s untimestamped packet with error 0x%08x\n"
+ "  %s(%s): Ignoring platform mask 0x%x, boot-arg set mask 0x%x\n"
+ "  %s(%s): No provider, cannot identify the Wi-Fi driver"
+ "  %s(%s): Skip egress timestamp request for general messages, mask 0x%x\n"
+ "  %s(%s): Wi-Fi driver CFBundleIdentifier is \"%s\", chipset %s"
+ "12111112122212121211222121122222121111211112111122222221111111212222222"
+ "1211111212221212121122212112222212111121111211112222222111111121222222211"
+ "121111121222121212112221211222221211112111121111222222211111112122222222222"
+ "<unreadable>"
+ "Skip egress timestamp request for general messages, mask 0x%x\n"
+ "TransmittedEgressUntimestampedCounter"
+ "UntimestampedGeneralMessageMask"
+ "getTransmitTimestamp(packet, &timestamp) == kIOReturnSuccess"
+ "timesync_untimestamped_general"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
- "121111121222121212112221211222221211112111121111222222211111112122222"
- "12111112122212121211222121122222121111211112111122222221111111212222211"
- "12111112122212121211222121122222121111211112111122222221111111212222222221"
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
