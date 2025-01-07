## AHTUserEventAgent

> `/System/Library/UserEventPlugins/AHTUserEventAgent.plugin/AHTUserEventAgent`

```diff

-8100.32.0.0.0
-  __TEXT.__text: 0x438c
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x940
-  __TEXT.__objc_methlist: 0x3c0
-  __TEXT.__cstring: 0x8fa
-  __TEXT.__objc_classname: 0x9b
+8140.4.0.0.0
+  __TEXT.__text: 0x4730
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x408
+  __TEXT.__cstring: 0x990
+  __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methtype: 0x368
-  __TEXT.__objc_methname: 0xbb1
+  __TEXT.__objc_methname: 0xca2
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__oslogstring: 0x42c
-  __TEXT.__unwind_info: 0x140
-  __DATA.__auth_got: 0x298
+  __TEXT.__unwind_info: 0x158
+  __DATA.__auth_got: 0x2a0
   __DATA.__got: 0x90
   __DATA.__const: 0x118
   __DATA.__cfstring: 0xa00

   __DATA.__objc_catlist: 0x8
   __DATA.__objc_protolist: 0x10
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xe08
-  __DATA.__objc_selrefs: 0x2e0
+  __DATA.__objc_const: 0xe38
+  __DATA.__objc_selrefs: 0x310
   __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x50
+  __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x190
   __DATA.__data: 0xc0
   __DATA.__objc_intobj: 0x4e0

   - /System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 100
-  Symbols:   119
-  CStrings:  356
+  Functions: 108
+  Symbols:   120
+  CStrings:  368
 
Symbols:
+ _dispatch_set_context
CStrings:
+ "\x13"
+ "-[AHTDeviceStats restartDailyCollectionTimer:]"
+ "-[AHTDeviceStats startDailyCollectionTimer]"
+ "-[AHTDeviceStats startDailyCollectionTimer]_block_invoke_2"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_dailyCollectionTimer"
+ "_dailyCollectionTimer"
+ "collectRepairHistoryInvalidationStat"
+ "dailyCollectionTimer"
+ "dailyStatsCollection"
+ "restartDailyCollectionTimer:"
+ "setDailyCollectionTimer:"
+ "startDailyCollectionTimer"

```
