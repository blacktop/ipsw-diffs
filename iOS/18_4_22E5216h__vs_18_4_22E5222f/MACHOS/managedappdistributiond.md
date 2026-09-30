## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-2.4.18.0.0
-  __TEXT.__text: 0x5335ec
-  __TEXT.__auth_stubs: 0x56e0
+2.4.20.0.0
+  __TEXT.__text: 0x5361b8
+  __TEXT.__auth_stubs: 0x56f0
   __TEXT.__objc_stubs: 0x1a80
   __TEXT.__objc_methlist: 0x2134
-  __TEXT.__const: 0x3acb4
+  __TEXT.__const: 0x3aca4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x5ff7
-  __TEXT.__cstring: 0xafa5
-  __TEXT.__oslogstring: 0xd46e
+  __TEXT.__objc_methname: 0x6024
+  __TEXT.__cstring: 0xb475
+  __TEXT.__oslogstring: 0xd56e
   __TEXT.__objc_classname: 0x403
   __TEXT.__objc_methtype: 0x1558
   __TEXT.__gcc_except_tab: 0x4e8

   __TEXT.__swift5_typeref: 0x481e
   __TEXT.__swift5_proto: 0x143c
   __TEXT.__swift5_types: 0x84c
-  __TEXT.__swift_as_entry: 0x920
-  __TEXT.__swift_as_ret: 0xffc
+  __TEXT.__swift_as_entry: 0x924
+  __TEXT.__swift_as_ret: 0x1034
   __TEXT.__swift5_protos: 0x8c
-  __TEXT.__unwind_info: 0xf2a8
-  __TEXT.__eh_frame: 0x2ef70
-  __DATA_CONST.__auth_got: 0x2b80
-  __DATA_CONST.__got: 0x1928
-  __DATA_CONST.__auth_ptr: 0x1a48
-  __DATA_CONST.__const: 0x28dd8
+  __TEXT.__unwind_info: 0xea30
+  __TEXT.__eh_frame: 0x2f208
+  __DATA_CONST.__auth_got: 0x2b88
+  __DATA_CONST.__got: 0x1930
+  __DATA_CONST.__auth_ptr: 0x1a50
+  __DATA_CONST.__const: 0x28d98
   __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0x170

   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x57a8
-  __DATA.__objc_selrefs: 0x1bd8
+  __DATA.__objc_selrefs: 0x1be8
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x1cb8
   __DATA.__data: 0xd030
   __DATA.__bss: 0x27290
-  __DATA.__common: 0xb60
+  __DATA.__common: 0xb68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets

   - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 13620
-  Symbols:   2576
-  CStrings:  3468
+  Functions: 13642
+  Symbols:   2580
+  CStrings:  3488
 
Symbols:
+ _$s14MarketplaceKit11FeatureFlagO15webDistributionyA2CmFWC
+ _$s22ManagedAppDistribution02isabC7EnabledSbyF
+ _OBJC_CLASS_$_AXBackBoardServer
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
CStrings:
+ "Any installed marketplaces will be managed by the developer and may give them access to your data."
+ "By allowing this developer, you will be able to install their marketplaces on your iPhone."
+ "Feature flag should have prevented daemon launch!"
+ "ManagedAppDistribution.DeveloperApproval.AppInstallation.Body"
+ "ManagedAppDistribution.DeveloperApproval.AppInstallation.Title"
+ "ManagedAppDistribution.DeveloperApproval.Body"
+ "ManagedAppDistribution.DeveloperApproval.FollowUp.Text"
+ "ManagedAppDistribution.DeveloperApproval.UnavailableFeatures.Body"
+ "ManagedAppDistribution.DeveloperApproval.UnavailableFeatures.Title"
+ "ManagedAppDistribution.DeveloperApproval.YourData.Body"
+ "ManagedAppDistribution.DeveloperApproval.YourData.Title"
+ "ManagedAppDistribution.Marketplace.NotAllowed.Message"
+ "ManagedAppDistribution.Marketplace.NotAllowed.Title"
+ "Marketplace Installation"
+ "You attempted to install “@@appName@@” from “@@domain@@”. Your device settings don't allow marketplaces to be installed by the developer “@@developerName@@” from the web. @@learnMoreLink@@"
+ "Your installation settings on this iPhone don’t allow marketplaces by “@@name@@” to be installed from the web. You can change this in Settings."
+ "[%@] Ineligible for distribution from %{public}s"
+ "[%@] Install bundle ID was incorrect type or missing"
+ "[%@][%{public}s] Overriding install priority due to SAM"
+ "currentGuidedAccessModeAndSessionApp:"
+ "server"
- "defaultDistributor"

```
