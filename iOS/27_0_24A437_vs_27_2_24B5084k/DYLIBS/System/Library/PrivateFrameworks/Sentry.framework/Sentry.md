## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

-11.0.0.0.0
-  __TEXT.__text: 0xfccc
+12.0.0.0.0
+  __TEXT.__text: 0xfdc8
   __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0xec
-  __TEXT.__cstring: 0x14cc
-  __TEXT.__oslogstring: 0x1dbc
-  __TEXT.__gcc_except_tab: 0x3ac
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__cstring: 0x14ec
+  __TEXT.__oslogstring: 0x1d9e
+  __TEXT.__gcc_except_tab: 0x3a0
+  __TEXT.__unwind_info: 0x598
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4a0
+  __DATA_CONST.__const: 0x4c8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa70
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x1240
-  __AUTH_CONST.__objc_const: 0x19d0
+  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__objc_const: 0x19f0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x14c
+  __DATA.__objc_ivar: 0x150
   __DATA.__data: 0xe8
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 457
-  Symbols:   1150
-  CStrings:  303
+  Functions: 459
+  Symbols:   1155
+  CStrings:  302
 
Symbols:
+ _OBJC_IVAR_$_STYWorkflowResponsivenessMonitorHelper._allowListSyncQueue
+ ___51-[STYWorkflowResponsivenessMonitorHelper allowList]_block_invoke
+ ___57-[STYWorkflowResponsivenessMonitorHelper updateAllowList]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ _objc_retain_x9
Functions:
~ -[STYWorkflowResponsivenessMonitorHelper allowList] : 8 -> 228
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:] : 2864 -> 2656
~ -[STYWorkflowResponsivenessMonitorHelper init] : 892 -> 920
~ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke_2 : 1256 -> 1368
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.490
+ ___51-[STYWorkflowResponsivenessMonitorHelper allowList]_block_invoke
~ -[STYWorkflowResponsivenessMonitorHelper updateAllowList] : 852 -> 948
+ ___57-[STYWorkflowResponsivenessMonitorHelper updateAllowList]_block_invoke
~ -[STYWorkflowResponsivenessMonitorHelper .cxx_destruct] : 116 -> 128
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.5 : 52 -> 96
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.6 : 96 -> 52
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.10 : 52 -> 100
- -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.11
CStrings:
+ "com.apple.sentry.signpostsMonitor.WorkflowResponsivenessAllowList"
- "App launch threshold enforced"
- "ApplicationFirstFramePresentation"
```
