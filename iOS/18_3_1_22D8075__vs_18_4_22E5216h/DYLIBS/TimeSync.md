## TimeSync

> `/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`

```diff

-1330.2.0.0.0
-  __TEXT.__text: 0x4fac0
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x5c28
-  __TEXT.__const: 0x258
-  __TEXT.__oslogstring: 0x3861
-  __TEXT.__cstring: 0x689d
-  __TEXT.__gcc_except_tab: 0xb4c
-  __TEXT.__unwind_info: 0x1478
-  __TEXT.__objc_classname: 0x9be
-  __TEXT.__objc_methname: 0xae9c
-  __TEXT.__objc_methtype: 0x14f1
-  __TEXT.__objc_stubs: 0x68a0
+1340.12.0.0.0
+  __TEXT.__text: 0x51894
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_methlist: 0x5fe8
+  __TEXT.__const: 0x288
+  __TEXT.__oslogstring: 0x3b64
+  __TEXT.__cstring: 0x68d0
+  __TEXT.__gcc_except_tab: 0xb84
+  __TEXT.__unwind_info: 0x1650
+  __TEXT.__objc_classname: 0x9bf
+  __TEXT.__objc_methname: 0xaed0
+  __TEXT.__objc_methtype: 0x14fe
+  __TEXT.__objc_stubs: 0x68c0
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0xbf0
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20c8
+  __DATA_CONST.__objc_selrefs: 0x2148
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x340
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x498
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x4f80
-  __AUTH_CONST.__objc_const: 0xbf40
+  __AUTH_CONST.__objc_const: 0xb930
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x824
+  __DATA.__objc_ivar: 0x830
   __DATA.__data: 0x488
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x1f40
   __DATA_DIRTY.__bss: 0xe8
   __DATA_DIRTY.__common: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2103
-  Symbols:   2644
-  CStrings:  3064
+  Functions: 2425
+  Symbols:   3040
+  CStrings:  3073
 
Symbols:
+ OBJC_IVAR_$__TSF_TSDgPTPPort._logNotifyTest
+ _objc_retain_x28
CStrings:
+ "\x01\x11\x14A"
+ "%@Records = np.rec.array(np.genfromtxt(%@, dtype=None, delimiter=',', names=True, encoding='utf-8'))\n\ntau = %@Records.observation_interval\n%@ = %@Records.%@\n\n%@\n"
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
+ "timeErrorRecords = np.rec.array(np.genfromtxt(%@, dtype=None, delimiter=',', names=True, encoding='utf-8'))\n\ntime = timeErrorRecords.time\ntimeError = timeErrorRecords.time_error\n\n"
+ "timesync_tsnotifytest"
+ "v32@0:8I16I20^{ScalarArgsArrayUserReference=[16Q]I}24"
- "\x01\x15A"
- "%@Records = np.recfromtxt(%@, dtype=None, delimiter=',', names=True, encoding='utf-8')\n\ntau = %@Records.observation_interval\n%@ = %@Records.%@\n\n%@\n"
- "numArgs == 4"
- "numArgs == 7"
- "timeErrorRecords = np.recfromtxt(%@, dtype=None, delimiter=',', names=True, encoding='utf-8')\n\ntime = timeErrorRecords.time\ntimeError = timeErrorRecords.time_error\n\n"
- "v32@0:8I16I20^{ScalarArgsArray=[16Q]I}24"

```
