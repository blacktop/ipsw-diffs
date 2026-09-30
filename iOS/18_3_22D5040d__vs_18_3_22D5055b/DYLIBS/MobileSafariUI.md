## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-620.2.3.0.0
-  __TEXT.__text: 0x1f30ec
+620.2.4.10.7
+  __TEXT.__text: 0x1f3bac
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0x19734
+  __TEXT.__objc_methlist: 0x197cc
   __TEXT.__const: 0x7d6
-  __TEXT.__gcc_except_tab: 0x1ac68
-  __TEXT.__cstring: 0xc563
+  __TEXT.__gcc_except_tab: 0x1ac54
+  __TEXT.__cstring: 0xc603
   __TEXT.__dlopen_cstrs: 0x774
-  __TEXT.__oslogstring: 0x8a60
+  __TEXT.__oslogstring: 0x8cb6
   __TEXT.__ustring: 0x10a6
   __TEXT.__swift5_proto: 0x4
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xc588
-  __TEXT.__objc_classname: 0x4401
-  __TEXT.__objc_methname: 0x69c78
-  __TEXT.__objc_methtype: 0x15429
-  __TEXT.__objc_stubs: 0x46140
-  __DATA_CONST.__got: 0x2708
-  __DATA_CONST.__const: 0x84b0
-  __DATA_CONST.__objc_classlist: 0x958
+  __TEXT.__unwind_info: 0xc5b8
+  __TEXT.__objc_classname: 0x4419
+  __TEXT.__objc_methname: 0x69df6
+  __TEXT.__objc_methtype: 0x15478
+  __TEXT.__objc_stubs: 0x462c0
+  __DATA_CONST.__got: 0x2720
+  __DATA_CONST.__const: 0x84d0
+  __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x9e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14f08
+  __DATA_CONST.__objc_selrefs: 0x14f68
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x738
+  __DATA_CONST.__objc_superrefs: 0x740
   __DATA_CONST.__objc_arraydata: 0x278
   __AUTH_CONST.__auth_got: 0xd88
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x2ac8
-  __AUTH_CONST.__cfstring: 0xbd80
-  __AUTH_CONST.__objc_const: 0x41520
+  __AUTH_CONST.__const: 0x2b28
+  __AUTH_CONST.__cfstring: 0xbe20
+  __AUTH_CONST.__objc_const: 0x41670
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x1eb0
+  __AUTH.__objc_data: 0x1f00
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x23c4
+  __DATA.__objc_ivar: 0x23d4
   __DATA.__data: 0x7860
-  __DATA.__bss: 0x510
+  __DATA.__bss: 0x520
   __DATA.__common: 0x2
   __DATA_DIRTY.__objc_data: 0x3f20
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x520
+  __DATA_DIRTY.__bss: 0x530
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SafariCore.framework/SafariCore
   - /System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11611
-  Symbols:   13724
-  CStrings:  19950
+  Functions: 11628
+  Symbols:   13745
+  CStrings:  19988
 
Symbols:
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
CStrings:
+ ", UUID is nil"
+ ", group is nil"
+ "@\"RBSAssertion\""
+ "Already in tab group."
+ "Assertion %@ is invalidated"
+ "Did switch to tab group: %{public}@%{public}@%{public}@"
+ "Failed to acquire assertion %@, error: %@"
+ "Failed to invalidate assertion %@, error: %@"
+ "FinishTaskInterruptable"
+ "MobileSafari BackgroundTasks: %@"
+ "ProcessAssertion"
+ "ProcessAssertionManager"
+ "T@\"ProcessAssertionManager\",R,N"
+ "Will switch tab group for change to cloud tabs enabled."
+ "Will switch tab group for change to web view fullscreen."
+ "Will switch tab group to visible group."
+ "Will switch to local tab group because current browsing mode is unavailable."
+ "Will switch to local tab group because start page collection visibility was toggled."
+ "Will switch to local tab group for external link."
+ "Will switch to local tab group for navigation intent handling."
+ "Will switch to local tab group for web clip."
+ "_acquireAssertionIfNeeded"
+ "_assertion"
+ "_didEnterBackgroundNotification"
+ "_hasNoTasks"
+ "_invalidateAssertion"
+ "_lock"
+ "_taskIdentifiers"
+ "acquireWithInvalidationHandler:"
+ "attributeWithDomain:name:"
+ "com.apple.common"
+ "currentProcess"
+ "explanation"
+ "initWithExplanation:target:attributes:"
+ "invalidateBackgroundTaskWithTaskIdentifier:"
+ "invalidateWithError:"
+ "registerBackgroundTaskWithTaskIdentifier:"
+ "sfWebExtensionsController:pinTab:"
+ "v24@?0@\"RBSAssertion\"8@\"NSError\"16"
+ "v32@0:8@\"SFWebExtensionsController\"16@\"<WBSWebExtensionTab>\"24"
- "Background task expired while waiting for cloud tabs to synchronize"
- "sfWebExtensionsController:duplicateTab:"

```
