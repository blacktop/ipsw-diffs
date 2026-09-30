## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Versions/A/Sentry`

```diff

-11.0.0.0.0
-  __TEXT.__text: 0x1af60
+12.0.0.0.0
+  __TEXT.__text: 0x1b064
   __TEXT.__objc_methlist: 0x1778
   __TEXT.__const: 0x174
-  __TEXT.__cstring: 0x1eca
-  __TEXT.__oslogstring: 0x3061
-  __TEXT.__gcc_except_tab: 0x408
-  __TEXT.__unwind_info: 0x9d8
+  __TEXT.__cstring: 0x1eea
+  __TEXT.__oslogstring: 0x3043
+  __TEXT.__gcc_except_tab: 0x400
+  __TEXT.__unwind_info: 0x9e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0xa8
   __DATA_CONST.__got: 0x3b0
   __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__cfstring: 0x1ea0
-  __AUTH_CONST.__objc_const: 0x31f0
+  __AUTH_CONST.__cfstring: 0x1e80
+  __AUTH_CONST.__objc_const: 0x3210
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_ivar: 0x200
   __DATA.__data: 0x3e8
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 766
-  Symbols:   1808
-  CStrings:  518
+  Functions: 768
+  Symbols:   1811
+  CStrings:  517
 
Symbols:
+ OBJC_IVAR_$_STYWorkflowResponsivenessMonitorHelper._allowListSyncQueue
+ ___51-[STYWorkflowResponsivenessMonitorHelper allowList]_block_invoke
+ ___57-[STYWorkflowResponsivenessMonitorHelper updateAllowList]_block_invoke
Functions:
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:] : 2360 -> 2144
~ -[STYWorkflowResponsivenessMonitorHelper init] : 940 -> 972
~ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke_2 : 1324 -> 1440
+ __46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.471
~ -[STYWorkflowResponsivenessMonitorHelper allowList] : 8 -> 228
+ ___51-[STYWorkflowResponsivenessMonitorHelper allowList]_block_invoke
~ -[STYWorkflowResponsivenessMonitorHelper updateAllowList] : 876 -> 980
+ ___57-[STYWorkflowResponsivenessMonitorHelper updateAllowList]_block_invoke
~ -[STYWorkflowResponsivenessMonitorHelper .cxx_destruct] : 116 -> 128
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.3 : 52 -> 96
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.4 : 96 -> 52
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.8 : 52 -> 108
- -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.9
CStrings:
+ "com.apple.sentry.signpostsMonitor.WorkflowResponsivenessAllowList"
- "App launch threshold enforced"
- "ApplicationFirstFramePresentation"
```
