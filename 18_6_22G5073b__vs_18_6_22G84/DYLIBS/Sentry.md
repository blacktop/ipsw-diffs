## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

 1.20.42.0.0
-  __TEXT.__text: 0x106cc
+  __TEXT.__text: 0x107d8
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0xe4
-  __TEXT.__cstring: 0x1426
-  __TEXT.__oslogstring: 0x1c31
-  __TEXT.__gcc_except_tab: 0x474
+  __TEXT.__cstring: 0x1448
+  __TEXT.__oslogstring: 0x1c4f
+  __TEXT.__gcc_except_tab: 0x490
   __TEXT.__unwind_info: 0x490
   __TEXT.__objc_classname: 0x1b1
   __TEXT.__objc_methname: 0x2e56

   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__cfstring: 0x11e0
   __AUTH_CONST.__objc_const: 0x19b0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x140

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 32C0E130-1F9D-3406-96A9-B728FC8ABD46
-  Functions: 442
-  Symbols:   1657
-  CStrings:  988
+  UUID: 70FBD1A9-0A6B-30ED-8BFE-70880C09142C
+  Functions: 443
+  Symbols:   1659
+  CStrings:  991
 
Symbols:
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.14
+ GCC_except_table222
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.490
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.491
+ ___block_literal_global.482
+ ___block_literal_global.557
- GCC_except_table221
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.484
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.488
- ___block_literal_global.479
- ___block_literal_global.554
Functions:
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:] : 2140 -> 2348
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.3 : 144 -> 60
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.4 : 60 -> 144
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.8 : 100 -> 60
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.9
CStrings:
+ "App launch threshold enforced"
+ "ApplicationFirstFramePresentation"

```
