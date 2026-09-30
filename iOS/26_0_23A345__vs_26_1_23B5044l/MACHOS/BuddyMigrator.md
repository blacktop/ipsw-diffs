## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5374.106.0.0.0
-  __TEXT.__text: 0x15bb4
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x1e40
-  __TEXT.__objc_methlist: 0x1068
-  __TEXT.__const: 0x538
-  __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__objc_methname: 0x2af2
-  __TEXT.__cstring: 0x13f8
-  __TEXT.__oslogstring: 0x1e7e
-  __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methtype: 0x2e7
-  __TEXT.__dlopen_cstrs: 0xfc
+5376.100.0.0.0
+  __TEXT.__text: 0x169c0
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_stubs: 0x1f80
+  __TEXT.__objc_methlist: 0x1158
+  __TEXT.__const: 0x548
+  __TEXT.__gcc_except_tab: 0x2ac
+  __TEXT.__objc_methname: 0x2d70
+  __TEXT.__cstring: 0x1448
+  __TEXT.__oslogstring: 0x1fae
+  __TEXT.__objc_classname: 0x20d
+  __TEXT.__objc_methtype: 0x443
+  __TEXT.__dlopen_cstrs: 0x1ac
   __TEXT.__constg_swiftt: 0x468
   __TEXT.__swift5_typeref: 0x608
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x58
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__unwind_info: 0x6a8
+  __TEXT.__unwind_info: 0x708
   __TEXT.__eh_frame: 0x7a8
-  __DATA_CONST.__auth_got: 0x590
-  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__auth_got: 0x5b8
+  __DATA_CONST.__got: 0x368
   __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0x9e0
+  __DATA_CONST.__const: 0xa38
   __DATA_CONST.__cfstring: 0xaa0
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1eb8
-  __DATA.__objc_selrefs: 0xb48
-  __DATA.__objc_ivar: 0xc4
-  __DATA.__objc_data: 0xc20
-  __DATA.__data: 0x4f8
-  __DATA.__bss: 0x140
+  __DATA.__objc_const: 0x21b8
+  __DATA.__objc_selrefs: 0xbb0
+  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_data: 0xd10
+  __DATA.__data: 0x678
+  __DATA.__bss: 0x160
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E1C1733B-9274-3EA9-9097-DF7A6DE1B29B
-  Functions: 536
-  Symbols:   334
-  CStrings:  937
+  UUID: A873D768-3F0B-308A-AE93-EEB53A313272
+  Functions: 557
+  Symbols:   346
+  CStrings:  980
 
Symbols:
+ _OBJC_CLASS_$_BuddySafetySettingsPresentationManager
+ _OBJC_CLASS_$_BuddySafetySettingsUIManager
+ _OBJC_CLASS_$_BuddySafetySettingsViewControllerSession
+ _OBJC_METACLASS_$_BuddySafetySettingsPresentationManager
+ _OBJC_METACLASS_$_BuddySafetySettingsUIManager
+ _OBJC_METACLASS_$_BuddySafetySettingsViewControllerSession
+ _kCCSkipKeyWebContentFiltering
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_retain_x3
+ _objc_retain_x9
+ _objc_storeWeak
CStrings:
+ "@\"<BuddySafetySettingsViewControllerSession>\"28@0:8@\"<BuddySafetySettingsViewControllerSessionDelegate>\"16B24"
+ "@\"<BuddySafetySettingsViewControllerSessionDelegate>\""
+ "@\"UIViewController\""
+ "@\"UIViewController\"16@0:8"
+ "@28@0:8@16B24"
+ "AISSafetySettingsContext"
+ "AISSafetySettingsController"
+ "AISSafetySettingsViewController"
+ "AISSafetySettingsViewControllerDelegate"
+ "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for auto-opt-in"
+ "BuddyMigrator: Queueing Safety Settings mini-buddy"
+ "BuddySafetySettingsPresentationManager"
+ "BuddySafetySettingsPresentationProvider"
+ "BuddySafetySettingsUIManager"
+ "BuddySafetySettingsUIProvider"
+ "BuddySafetySettingsViewControllerSession"
+ "Did check whether to present safety settings with result %d error %{public}@"
+ "Safety session view controller session did finish. Forwarding to delegate %{public}@"
+ "Safety settings underlying classes do not exit"
+ "T@\"<BuddySafetySettingsViewControllerSessionDelegate>\",W,N,V_delegate"
+ "T@\"UIViewController\",&,N,V_viewController"
+ "Will check whether to present safety settings"
+ "_delegate"
+ "_shouldLaunchMiniBuddyForSafetySettings"
+ "_viewController"
+ "contextWithHasCompletedInitialRun:"
+ "delegate"
+ "initWithFlowType:"
+ "initWithSafetySettingsContext:"
+ "safetySettingsDidFinishWithResult:viewControllersToRemove:error:"
+ "safetySettingsViewControllerSessionDidFinishWithViewControllersToRemove:"
+ "setDelegate:"
+ "setViewController:"
+ "shouldPresentSafetySettingsWithContext:completionHandler:"
+ "shouldPresentSafetySettingsWithHasCompletedInitialRun:completion:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI"
+ "v40@0:8@\"AISSafetySettingsResult\"16@\"NSArray\"24@\"NSError\"32"
+ "v40@0:8@16@24@32"
+ "viewController"
+ "viewControllerSessionWithDelegate:hasCompletedInitialRun:"
- "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for re-opt-in"

```
