## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

 1.20.42.0.0
-  __TEXT.__text: 0x107d8
+  __TEXT.__text: 0x106cc
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0xe4
-  __TEXT.__cstring: 0x1448
-  __TEXT.__oslogstring: 0x1c4f
-  __TEXT.__gcc_except_tab: 0x490
+  __TEXT.__cstring: 0x1426
+  __TEXT.__oslogstring: 0x1c31
+  __TEXT.__gcc_except_tab: 0x474
   __TEXT.__unwind_info: 0x490
   __TEXT.__objc_classname: 0x1b1
   __TEXT.__objc_methname: 0x2e56

   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x11e0
+  __AUTH_CONST.__cfstring: 0x11c0
   __AUTH_CONST.__objc_const: 0x19b0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x148
   __DATA.__data: 0xe8
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0x80
   __DATA.__common: 0x11
-  __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__bss: 0x90
-  __DATA_DIRTY.__common: 0x58
+  __DATA_DIRTY.__objc_data: 0x460
+  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 74901458-D24D-309F-A17A-CAF6AF75BCA4
-  Functions: 443
-  Symbols:   1659
-  CStrings:  991
+  UUID: F44AAC5C-A837-32C8-9BC5-54DB3D025F7B
+  Functions: 442
+  Symbols:   1657
+  CStrings:  988
 
Symbols:
+ GCC_except_table221
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.484
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.488
+ ___block_literal_global.479
+ ___block_literal_global.554
- -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.14
- GCC_except_table222
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.490
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.491
- ___block_literal_global.482
- ___block_literal_global.557
Functions:
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:] : 2348 -> 2140
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.3 : 60 -> 144
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.4 : 144 -> 60
~ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.8 : 60 -> 100
- -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.9
CStrings:
- "App launch threshold enforced"
- "ApplicationFirstFramePresentation"

```
