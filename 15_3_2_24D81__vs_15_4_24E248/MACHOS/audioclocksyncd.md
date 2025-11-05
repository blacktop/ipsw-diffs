## audioclocksyncd

> `/usr/libexec/audioclocksyncd`

```diff

-1330.2.0.0.0
-  __TEXT.__text: 0x28dbc
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0x4040
-  __TEXT.__objc_methlist: 0x268c
-  __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0x253d
-  __TEXT.__cstring: 0x274a
-  __TEXT.__gcc_except_tab: 0x474
-  __TEXT.__objc_methname: 0x6e9a
-  __TEXT.__objc_classname: 0x409
-  __TEXT.__objc_methtype: 0xcb8
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__auth_got: 0x280
+1340.12.0.0.0
+  __TEXT.__text: 0x29e10
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_stubs: 0x4060
+  __TEXT.__objc_methlist: 0x2960
+  __TEXT.__const: 0xe0
+  __TEXT.__oslogstring: 0x2840
+  __TEXT.__cstring: 0x2762
+  __TEXT.__gcc_except_tab: 0x4f0
+  __TEXT.__objc_methname: 0x6ece
+  __TEXT.__objc_classname: 0x40a
+  __TEXT.__objc_methtype: 0xcc5
+  __TEXT.__unwind_info: 0x920
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0xb88
   __DATA_CONST.__cfstring: 0x2060

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x5330
-  __DATA.__objc_selrefs: 0x1530
-  __DATA.__objc_ivar: 0x3f4
+  __DATA.__objc_const: 0x4ed0
+  __DATA.__objc_selrefs: 0x15b0
+  __DATA.__objc_ivar: 0x400
   __DATA.__objc_data: 0xc80
   __DATA.__data: 0x360
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x108
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D876925-41E9-3BCC-91D4-BB9AA1F3DD18
-  Functions: 886
-  Symbols:   122
-  CStrings:  2005
+  UUID: 946E57E0-F087-382C-8A96-95771B5F79E0
+  Functions: 1061
+  Symbols:   123
+  CStrings:  2014
 
Symbols:
+ _os_parse_boot_arg_int
CStrings:
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockDiagnosticsManager.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockStatistics.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockManager.mm"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockSync.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDDaemonService.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKernelClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKextNotifier.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDUserFilteredClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPManager.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPPort.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/TSDDaemon.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/XPC/TSDDaemonServiceServer.m"
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
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockDiagnosticsManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockStatistics.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockManager.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockSync.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDDaemonService.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKernelClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKextNotifier.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDUserFilteredClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPPort.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/TSDDaemon.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/XPC/TSDDaemonServiceServer.m"
- "1330.2"
- "numArgs == 4"
- "numArgs == 7"
- "v32@0:8I16I20^{ScalarArgsArray=[16Q]I}24"

```
