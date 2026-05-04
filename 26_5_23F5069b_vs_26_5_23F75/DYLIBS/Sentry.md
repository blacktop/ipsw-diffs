## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

 3.0.0.0.0
-  __TEXT.__text: 0x10b8c
+  __TEXT.__text: 0x10c8c
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_methlist: 0xd50
   __TEXT.__const: 0xe4
-  __TEXT.__cstring: 0x140f
-  __TEXT.__oslogstring: 0x1beb
-  __TEXT.__gcc_except_tab: 0x42c
+  __TEXT.__cstring: 0x1431
+  __TEXT.__oslogstring: 0x1c09
+  __TEXT.__gcc_except_tab: 0x444
   __TEXT.__unwind_info: 0x490
   __TEXT.__objc_classname: 0x1b1
   __TEXT.__objc_methname: 0x2e56

   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x11a0
+  __AUTH_CONST.__cfstring: 0x11c0
   __AUTH_CONST.__objc_const: 0x19b0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 458A9710-A6AD-387C-8269-701B91731CCC
-  Functions: 447
-  Symbols:   1664
-  CStrings:  985
+  UUID: 9D401CC3-58C0-3D1F-A50A-8C1CDC2F25AA
+  Functions: 448
+  Symbols:   1666
+  CStrings:  988
 
Symbols:
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.14
+ GCC_except_table220
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.481
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.482
+ ___block_literal_global.473
+ ___block_literal_global.548
- GCC_except_table219
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.475
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.479
- ___block_literal_global.470
- ___block_literal_global.545
Functions:
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:] : 2256 -> 2460
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.3 : 120 -> 52
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.4 : 52 -> 120
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.8 : 100 -> 52
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.9
CStrings:
+ "App launch threshold enforced"
+ "ApplicationFirstFramePresentation"

```
