## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-383.0.0.0.0
-  __TEXT.__text: 0x13578
-  __TEXT.__auth_stubs: 0x9c0
+384.0.0.0.0
+  __TEXT.__text: 0x13704
+  __TEXT.__auth_stubs: 0xa00
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_stubs: 0x1c40
-  __TEXT.__objc_methlist: 0xb34
+  __TEXT.__objc_stubs: 0x1ca0
+  __TEXT.__objc_methlist: 0xb44
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x260d
-  __TEXT.__oslogstring: 0x1bd2
+  __TEXT.__cstring: 0x2631
+  __TEXT.__oslogstring: 0x1c0c
   __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__objc_methname: 0x41ab
+  __TEXT.__objc_methname: 0x41c1
   __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methtype: 0x79a
+  __TEXT.__objc_methtype: 0x82f
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x3f0
-  __DATA_CONST.__auth_got: 0x4f0
+  __TEXT.__unwind_info: 0x3f8
+  __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0xd38
   __DATA_CONST.__cfstring: 0x2600

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x1e88
-  __DATA.__objc_selrefs: 0xb98
+  __DATA.__objc_selrefs: 0xba0
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0xfc
+  __DATA.__data: 0x104
   __DATA.__bss: 0xf0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 07927DDB-301D-33FE-BA1D-DCFBB45F6A13
-  Functions: 439
-  Symbols:   466
-  CStrings:  1483
+  UUID: 194537E1-1B6B-397E-BB99-2B6E8B3D4A50
+  Functions: 441
+  Symbols:   471
+  CStrings:  1487
 
Symbols:
+ _dispatch_assert_queue$V2
+ _dispatch_queue_get_label
+ _htMonitorConnectionQueueLabel
+ _strlen
+ _strncmp
Functions:
~ sub_10000cf34 : 8 -> 260
+ sub_10000d040
~ _updateHTForegroundTrackingState : 848 -> 876
+ sub_100013ef4
CStrings:
+ "HTMonitor shared page accessed on the incorrect queue: %s"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}20@0:8i16"
+ "com.apple.htmonitor.connectionqueue"
+ "getSharedPageFromPid:"

```
