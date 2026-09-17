## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-1501.7.0.0.0
-  __TEXT.__cstring: 0x4425
-  __TEXT.__os_log: 0x8ea3
+1510.7.0.0.0
+  __TEXT.__cstring: 0x449d
+  __TEXT.__os_log: 0x90fe
   __TEXT.__const: 0x1e8
-  __TEXT_EXEC.__text: 0x337a4
+  __TEXT_EXEC.__text: 0x33ddc
   __TEXT_EXEC.__auth_stubs: 0x820
   __DATA.__data: 0xd0
   __DATA.__common: 0x688
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0x15410
+  __DATA_CONST.__const: 0x15430
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1778
-  Symbols:   3025
-  CStrings:  745
+  Functions: 1783
+  Symbols:   3038
+  CStrings:  756
 
Symbols:
+ _ZN23TSNWiFiControlInterface11wifiChipsetEP9IOService
+ __ZL26chipsetForBundleIdentifierP8OSString
+ __ZN15TSNBSDInterface34setUntimestampedGeneralMessageMaskEj
+ __ZN23TSNWiFiControlInterface11wifiChipsetEP9IOService
+ __ZN23TSNWiFiControlInterface43untimestampedGeneralMessageMaskForInterfaceEP9IOService
+ __ZZN15TSNBSDInterface22logInterfaceStatisticsEvE11_os_log_fmt_2
+ __ZZN15TSNBSDInterface22transmitTimeSyncPacketEP9TSNPacketyE11_os_log_fmt_5
+ __ZZN15TSNBSDInterface34setUntimestampedGeneralMessageMaskEjE11_os_log_fmt
+ __ZZN15TSNBSDInterface34setUntimestampedGeneralMessageMaskEjE11_os_log_fmt_0
+ __ZZN15TSNBSDInterface4initE18TSNEthernetAddressP8OSStringt16TSNInterfaceType22TSNTimestampingSupportP8IOMapperbP12OSDictionaryE11_os_log_fmt_5
+ __ZZN23TSNWiFiControlInterface11wifiChipsetEP9IOServiceE11_os_log_fmt
+ __ZZN23TSNWiFiControlInterface11wifiChipsetEP9IOServiceE11_os_log_fmt_0
+ __ZZN23TSNWiFiControlInterface11wifiChipsetEP9IOServiceE11_os_log_fmt_1
CStrings:
+ "  %s(%s): Egress Untimestamped Packet Count: %u, Count since last log entry: %u (timestamping type %u, untimestamped general message mask 0x%x)\n"
+ "  %s(%s): Failed to transmit message of type %s untimestamped packet with error 0x%08x\n"
+ "  %s(%s): Ignoring platform mask 0x%x, boot-arg set mask 0x%x\n"
+ "  %s(%s): No provider, cannot identify the Wi-Fi driver"
+ "  %s(%s): Skip egress timestamp request for general messages, mask 0x%x\n"
+ "  %s(%s): Wi-Fi driver CFBundleIdentifier is \"%s\", chipset %s"
+ "12111112122212121211222121122222121111211112111122222221111111212222222"
+ "1211111212221212121122212112222212111121111211112222222111111121222222211"
+ "1211111212221212121122212112222212111121111211112222222111111121222222222221"
+ "<unreadable>"
+ "Skip egress timestamp request for general messages, mask 0x%x\n"
+ "TransmittedEgressUntimestampedCounter"
+ "UntimestampedGeneralMessageMask"
+ "timesync_untimestamped_general"
- "121111121222121212112221211222221211112111121111222222211111112122222"
- "12111112122212121211222121122222121111211112111122222221111111212222211"
- "12111112122212121211222121122222121111211112111122222221111111212222222221"
```
