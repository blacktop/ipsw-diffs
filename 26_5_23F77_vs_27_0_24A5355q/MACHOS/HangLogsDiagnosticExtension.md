## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-398.2.0.0.0
-  __TEXT.__text: 0x140b8
-  __TEXT.__auth_stubs: 0x9d0
+412.0.0.0.0
+  __TEXT.__text: 0x13370
+  __TEXT.__auth_stubs: 0xa30
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_stubs: 0x1ca0
-  __TEXT.__objc_methlist: 0xb64
-  __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x2664
-  __TEXT.__oslogstring: 0x1c0c
-  __TEXT.__objc_classname: 0xb2
-  __TEXT.__gcc_except_tab: 0x1d0
-  __TEXT.__objc_methname: 0x42e9
-  __TEXT.__objc_methtype: 0x82f
+  __TEXT.__objc_stubs: 0x1cc0
+  __TEXT.__objc_methlist: 0xbac
+  __TEXT.__const: 0x260
+  __TEXT.__cstring: 0x26c0
+  __TEXT.__oslogstring: 0x1cb8
+  __TEXT.__gcc_except_tab: 0x1cc
+  __TEXT.__objc_classname: 0xa2
+  __TEXT.__objc_methname: 0x4405
+  __TEXT.__objc_methtype: 0x852
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x440
-  __DATA_CONST.__auth_got: 0x4f8
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0xd40
-  __DATA_CONST.__cfstring: 0x2620
+  __TEXT.__unwind_info: 0x400
+  __DATA_CONST.__const: 0xd50
+  __DATA_CONST.__cfstring: 0x2660
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1ee8
-  __DATA.__objc_selrefs: 0xbb8
-  __DATA.__objc_ivar: 0x21c
+  __DATA_CONST.__auth_got: 0x528
+  __DATA_CONST.__got: 0x1c8
+  __DATA.__objc_const: 0x1f78
+  __DATA.__objc_selrefs: 0xbe0
+  __DATA.__objc_ivar: 0x228
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x104
+  __DATA.__data: 0x10c
   __DATA.__bss: 0xf0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D2D2B3A-C05F-34C8-9F2C-0D539C3332A7
-  Functions: 453
-  Symbols:   468
-  CStrings:  1496
+  UUID: 397B551B-F191-36A1-9C10-81FC84195914
+  Functions: 455
+  Symbols:   477
+  CStrings:  1514
 
Symbols:
+ _HANGTRACER_HUD_LAYER_REFRESH_NOTIFICATION
+ _dispatch_source_cancel
+ _kHTPrefsHUDClientsEnabled
+ _kHTPrefsHUDOpacity
+ _notify_post
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _strndup
- _objc_retain_x27
CStrings:
+ "@\"NSObject<OS_dispatch_source>\""
+ "@40@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}16Q24@32"
+ "HangTracerEnableHUDClients"
+ "HangTracerHUDOpacity"
+ "T@\"NSObject<OS_dispatch_source>\",R,V_app_exit_source"
+ "TB,R,V_areHUDClientsEnabled"
+ "TI,R,V_hudOpacityLevel"
+ "_app_exit_source"
+ "_areHUDClientsEnabled"
+ "_hudOpacityLevel"
+ "app_exit_source"
+ "areHUDClientsEnabled"
+ "com.apple.da.hud_layer_refresh"
+ "getHangHistoryRecords: SignpostInterval has nil BundleIdOverride attribute (beginEvent=%{public}@, attributes=%{public}@), skipping interval"
+ "hudOpacityLevel"
+ "initHTMonitorPidHangEvent:shmemSize:appExitSource:"
+ "initPropertyAreHUDClientsEnabled:"
+ "initPropertyHUDOpacity:"
+ "strndup failed for serviceName"
+ "\xf0\xf0Q!f!"
- "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}16Q24"
- "initHTMonitorPidHangEvent:shmem_size:"
- "\xf0\xf0A!f!"

```
