## audioclocksyncd

> `/usr/libexec/audioclocksyncd`

```diff

-1330.2.0.0.0
-  __TEXT.__text: 0x25ef4
+1340.12.0.0.0
+  __TEXT.__text: 0x26f5c
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x3f80
-  __TEXT.__objc_methlist: 0x2674
-  __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x23ad
-  __TEXT.__cstring: 0x2366
-  __TEXT.__gcc_except_tab: 0x470
-  __TEXT.__objc_methname: 0x6e15
-  __TEXT.__objc_classname: 0x409
-  __TEXT.__objc_methtype: 0xcb8
-  __TEXT.__unwind_info: 0x720
+  __TEXT.__objc_stubs: 0x3fa0
+  __TEXT.__objc_methlist: 0x2948
+  __TEXT.__const: 0xd0
+  __TEXT.__oslogstring: 0x26b0
+  __TEXT.__cstring: 0x237e
+  __TEXT.__gcc_except_tab: 0x4f0
+  __TEXT.__objc_methname: 0x6e49
+  __TEXT.__objc_classname: 0x40a
+  __TEXT.__objc_methtype: 0xcc5
+  __TEXT.__unwind_info: 0x8d0
   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0xab8

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x5320
-  __DATA.__objc_selrefs: 0x14f0
-  __DATA.__objc_ivar: 0x3f4
+  __DATA.__objc_const: 0x4ec0
+  __DATA.__objc_selrefs: 0x1570
+  __DATA.__objc_ivar: 0x400
   __DATA.__objc_data: 0xc80
   __DATA.__data: 0x360
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x108
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 864
+  Functions: 1039
   Symbols:   137
-  CStrings:  1735
+  CStrings:  1744
 
Symbols:
+ _os_parse_boot_arg_int
- _objc_retain_x25
CStrings:
+ "\x01\x11\x14A"
+ "1340.12"
+ "TB,R,N,V_logNotifyTest"
+ "TSDClockSync _handleNotification kIOTimeSyncSyncNotificationGeneralSyncUpdate rateNumerator=%llu rateDenominator=%llu timeSyncAnchor=%llu domainAnchor=%llu"
+ "TSDClockSync _handleNotification kIOTimeSyncSyncNotificationPTPSyncUpdate cumulativeScaledRate=%llu inverseCumulativeScaledRate=%llu timeSyncAnchor=%llu domainAnchorHi=%llu domainAnchorLo=%llu grandmasterID=%llu localPortNumber=%u syncFlags=%u syncInfoValid=%u"
+ "TSDKernelClock _handleNotification kIOTimeSyncDomainNotificationEtEDelayStats localPortNumber=%u mean=%llu median=%llu stddev=%llu min=%llu max=%llu numberOfSamples=%u"
+ "TSDKernelClock _handleNotification notification=%u arg1=%llu arg2=%llu"
+ "TSDgPTPPort asyncNotificationsCallback notification=%u arg1=%llu arg2=%llu arg3=%llu arg4=%llu arg5=%llu arg6=%llu"
+ "_logNotifyTest"
+ "logNotifyTest"
+ "numArgs == 13"
+ "numArgs == 8"
+ "timesync_tsnotifytest"
+ "v32@0:8I16I20^{ScalarArgsArrayUserReference=[16Q]I}24"
- "\x01\x15A"
- "1330.2"
- "numArgs == 4"
- "numArgs == 7"
- "v32@0:8I16I20^{ScalarArgsArray=[16Q]I}24"

```
