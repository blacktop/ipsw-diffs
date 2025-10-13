## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5378.0.0.0.0
-  __TEXT.__text: 0x169c0
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0x1150
+5379.0.0.0.0
+  __TEXT.__text: 0x16f0c
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_stubs: 0x2060
+  __TEXT.__objc_methlist: 0x1188
   __TEXT.__const: 0x548
-  __TEXT.__gcc_except_tab: 0x2ac
-  __TEXT.__objc_methname: 0x2d62
+  __TEXT.__gcc_except_tab: 0x298
+  __TEXT.__objc_methname: 0x2e78
   __TEXT.__cstring: 0x1448
-  __TEXT.__oslogstring: 0x1fae
-  __TEXT.__objc_classname: 0x20d
-  __TEXT.__objc_methtype: 0x443
+  __TEXT.__oslogstring: 0x206e
+  __TEXT.__objc_classname: 0x207
+  __TEXT.__objc_methtype: 0x45c
   __TEXT.__dlopen_cstrs: 0x1ac
   __TEXT.__constg_swiftt: 0x468
   __TEXT.__swift5_typeref: 0x608

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x58
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__unwind_info: 0x710
   __TEXT.__eh_frame: 0x7a8
-  __DATA_CONST.__auth_got: 0x5b8
-  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__got: 0x370
   __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0xa30
+  __DATA_CONST.__const: 0xa80
   __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x21b0
-  __DATA.__objc_selrefs: 0xba8
-  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_const: 0x21e0
+  __DATA.__objc_selrefs: 0xbe0
+  __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0xd10
   __DATA.__data: 0x678
   __DATA.__bss: 0x160

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5E7DDF46-F037-3F14-8AA1-21063A5CD216
-  Functions: 557
-  Symbols:   345
-  CStrings:  979
+  UUID: EB874FD9-A62D-304B-B01D-E32C1C4AFBC9
+  Functions: 563
+  Symbols:   347
+  CStrings:  991
 
Symbols:
+ _OBJC_CLASS_$_BuddySafetySettingsPresenterSession
+ _OBJC_CLASS_$_NSThread
+ _OBJC_METACLASS_$_BuddySafetySettingsPresenterSession
+ _objc_opt_respondsToSelector
- _OBJC_CLASS_$_BuddySafetySettingsViewControllerSession
- _OBJC_METACLASS_$_BuddySafetySettingsViewControllerSession
CStrings:
+ "@\"<BuddySafetySettingsPresenterSessionDelegate>\""
+ "@\"AISSafetySettingsContext\""
+ "@\"AISSafetySettingsFlowPresenter\""
+ "AISSafetySettingsFlowPresenter"
+ "AISSafetySettingsFlowPresenterDelegate"
+ "B20@0:8B16"
+ "BuddySafetySettingsPresenterSession"
+ "Safety session presentation session did finish. Forwarding to delegate %{public}@"
+ "Safety session presentation session will present with navigation controller %@"
+ "Safety settings flow presenter does not exist"
+ "Safety settings runtime dependency does not exist"
+ "Safety settings underlying classes lack local only checks"
+ "T@\"<BuddySafetySettingsPresenterSessionDelegate>\",W,N,V_delegate"
+ "T@\"AISSafetySettingsContext\",&,N,V_context"
+ "T@\"AISSafetySettingsFlowPresenter\",&,N,V_presenter"
+ "_context"
+ "_presenter"
+ "context"
+ "isMainThread"
+ "presentSafetySettingsWithContext:navigationController:"
+ "presentWithNavigationController:"
+ "presenter"
+ "runtimeDependencyExists"
+ "safetySettingsPresenterSessionDidFinishWithViewControllersToRemove:"
+ "setContext:"
+ "setPresenter:"
+ "shouldPresentSafetySettingsUsingOnlyLocalChecksWithContext:completionHandler:"
+ "shouldPresentSafetySettingsUsingOnlyLocalChecksWithHasCompletedInitialRun:"
+ "shouldPresentSafetySettingsWithContext:completion:"
+ "shouldPresentSafetySettingsWithHasCompletedInitialRun:delegate:completion:"
+ "v24@0:8@\"UINavigationController\"16"
+ "v36@0:8B16@\"<BuddySafetySettingsPresenterSessionDelegate>\"20@?<v@?@\"<BuddySafetySettingsPresenterSession>\">28"
+ "v36@0:8B16@20@?28"
- "@\"<BuddySafetySettingsViewControllerSession>\"28@0:8@\"<BuddySafetySettingsViewControllerSessionDelegate>\"16B24"
- "@\"<BuddySafetySettingsViewControllerSessionDelegate>\""
- "@\"UIViewController\""
- "@\"UIViewController\"16@0:8"
- "@28@0:8@16B24"
- "AISSafetySettingsViewController"
- "AISSafetySettingsViewControllerDelegate"
- "BuddySafetySettingsViewControllerSession"
- "Safety session view controller session did finish. Forwarding to delegate %{public}@"
- "Safety settings underlying classes do not exit"
- "T@\"<BuddySafetySettingsViewControllerSessionDelegate>\",W,N,V_delegate"
- "T@\"UIViewController\",&,N,V_viewController"
- "_viewController"
- "safetySettingsViewControllerSessionDidFinishWithViewControllersToRemove:"
- "setViewController:"
- "shouldPresentSafetySettingsWithContext:completionHandler:"
- "shouldPresentSafetySettingsWithHasCompletedInitialRun:completion:"
- "viewController"
- "viewControllerSessionWithDelegate:hasCompletedInitialRun:"

```
