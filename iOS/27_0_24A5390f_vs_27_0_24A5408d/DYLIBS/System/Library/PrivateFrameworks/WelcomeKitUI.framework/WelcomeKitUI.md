## WelcomeKitUI

> `/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI`

```diff

-1426.0.0.0.0
-  __TEXT.__text: 0x14324
-  __TEXT.__objc_methlist: 0x1ac4
+1428.0.3.0.0
+  __TEXT.__text: 0x14560
+  __TEXT.__objc_methlist: 0x1ae4
   __TEXT.__const: 0x92
-  __TEXT.__cstring: 0x4df0
+  __TEXT.__cstring: 0x4ec0
   __TEXT.__gcc_except_tab: 0x2ac
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__unwind_info: 0x608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0xb68
   __DATA_CONST.__got: 0x2d0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x4c20
+  __AUTH_CONST.__cfstring: 0x4ce0
   __AUTH_CONST.__objc_const: 0x37f8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 494
-  Symbols:   1678
-  CStrings:  643
+  Functions: 497
+  Symbols:   1682
+  CStrings:  649
 
Symbols:
+ -[WLCompletedViewController viewDidAppear:]
+ -[WLOnboardingViewController viewDidAppear:]
+ -[WLTransferringViewController viewDidAppear:]
+ GCC_except_table5
Functions:
~ -[WLCompletedViewController initWithWelcomeController:context:imported:] : 924 -> 960
~ -[WLCompletedViewController viewDidLoad] : 324 -> 356
+ -[WLCompletedViewController viewDidAppear:]
~ -[WLOnboardingViewController viewDidLoad] : 96 -> 128
+ -[WLOnboardingViewController viewDidAppear:]
~ -[WLTransferringViewController viewDidLoad] : 256 -> 288
+ -[WLTransferringViewController viewDidAppear:]
~ -[WLTransferringViewController setIsImporting:] : 220 -> 284
~ -[WLWelcomeController _pushViewController:andRemovePreviousTopmostViewControllerWithCompletion:] : 600 -> 660
CStrings:
+ "%@ creating Completed pane. title='%@', imported=%d"
+ "%@ pane switched to Importing. title='%@'"
+ "%@ showing pane %@ (replacing %@). migration_state=%ld"
+ "%@ viewDidAppear"
+ "%@ viewDidAppear. isImporting=%d"
+ "%@ viewDidLoad"
```
