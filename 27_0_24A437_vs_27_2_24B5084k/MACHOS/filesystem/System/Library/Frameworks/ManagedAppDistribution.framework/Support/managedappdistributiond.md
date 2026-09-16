## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-4.0.44.0.0
-  __TEXT.__text: 0x69d2e4
-  __TEXT.__auth_stubs: 0x7060
-  __TEXT.__objc_stubs: 0x48c0
-  __TEXT.__objc_methlist: 0x141c
-  __TEXT.__const: 0x3ffb0
+4.1.9.0.0
+  __TEXT.__text: 0x6a24b4
+  __TEXT.__auth_stubs: 0x7070
+  __TEXT.__objc_stubs: 0x48e0
+  __TEXT.__objc_methlist: 0x1424
+  __TEXT.__const: 0x40070
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xf25d
+  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__cstring: 0xfdfd
   __TEXT.__objc_classname: 0x1db6
   __TEXT.__objc_methtype: 0x18e5
   __TEXT.__dlopen_cstrs: 0xc8
-  __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__objc_methname: 0x6ad5
-  __TEXT.__constg_swiftt: 0x75b8
-  __TEXT.__swift5_typeref: 0x659c
-  __TEXT.__oslogstring: 0x15d82
-  __TEXT.__swift5_proto: 0x19f0
-  __TEXT.__swift5_types: 0xa80
-  __TEXT.__swift_as_entry: 0xc38
-  __TEXT.__swift_as_ret: 0x19e4
-  __TEXT.__swift_as_cont: 0x3554
+  __TEXT.__objc_methname: 0x6af5
+  __TEXT.__constg_swiftt: 0x75cc
+  __TEXT.__swift5_typeref: 0x651c
+  __TEXT.__oslogstring: 0x15ef2
+  __TEXT.__swift5_proto: 0x19ec
+  __TEXT.__swift5_types: 0xa7c
+  __TEXT.__swift_as_entry: 0xc40
+  __TEXT.__swift_as_ret: 0x19f8
+  __TEXT.__swift_as_cont: 0x3584
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__unwind_info: 0x14008
-  __TEXT.__eh_frame: 0x3a1a0
-  __DATA_CONST.__const: 0x2f008
+  __TEXT.__unwind_info: 0x14600
+  __TEXT.__eh_frame: 0x3a470
+  __DATA_CONST.__const: 0x2f588
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__auth_got: 0x3840
-  __DATA_CONST.__got: 0x1f58
-  __DATA_CONST.__auth_ptr: 0x5e60
-  __DATA.__objc_const: 0x6f00
-  __DATA.__objc_selrefs: 0x17f0
-  __DATA.__objc_data: 0x1ea8
-  __DATA.__data: 0x10f58
-  __DATA.__common: 0xef0
+  __DATA_CONST.__auth_got: 0x3848
+  __DATA_CONST.__got: 0x1f70
+  __DATA_CONST.__auth_ptr: 0x1ae8
+  __DATA.__objc_const: 0x6f08
+  __DATA.__objc_selrefs: 0x1800
+  __DATA.__objc_data: 0x1ea0
+  __DATA.__data: 0x10f78
+  __DATA.__common: 0xef8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16573
-  Symbols:   3265
-  CStrings:  4061
+  Functions: 16667
+  Symbols:   3269
+  CStrings:  4095
 
Symbols:
+ _$s14MarketplaceKit17FetchDataResponseV0E0O19isEUMarketplaceFlowyAESbcAEmFWC
+ _$s14MarketplaceKit19InstallSheetContextV19isEUMarketplaceFlowSbvg
+ _$s14MarketplaceKit19InstallSheetContextV6itemID07versionG06source4type6logKey12learnMoreURL014authenticationE4Data025showBiometricsForAppStoreC019isEUMarketplaceFlowACSS_SSSgAC6SourceOAC0C4TypeOS2S10Foundation0Q0VSgS2btcfC
+ _$s14MarketplaceKit23FetchPrivateDataRequestV0F0O19isEUMarketplaceFlowyA2EmFWC
+ _$s22ManagedAppDistribution0aB6StatusV6ReasonO014couldNotVerifyB2IDyA2EmFWC
+ _$s22ManagedAppDistribution19MessageRegistrationO011marketplaceB7CatalogyA2CmFWC
+ _$s22ManagedAppDistribution19MessageRegistrationO07managedB7CatalogyA2CmFWC
- _$s14MarketplaceKit19InstallSheetContextV6itemID07versionG06source4type6logKey12learnMoreURL014authenticationE4Data025showBiometricsForAppStoreC0ACSS_SSSgAC6SourceOAC0C4TypeOS2S10Foundation0Q0VSgSbtcfC
- _$s22ManagedAppDistribution19MessageRegistrationO10appCatalogyA2CmFWC
- _OBJC_CLASS_$_BSProcessHandle
CStrings:
+ "Allow “@@developerName@@” to Install the App Marketplace “@@marketplaceName@@”?"
+ "Any apps installed from the marketplace will be managed by the developer and may give them access to data from those apps."
+ "Any apps installed will be managed by the developer and may give them access to your child's data from those apps."
+ "Any installed apps will be managed by the developer and may give them access to your data from those apps."
+ "Ignoring unregistered notification for %{public}s - app is still installed"
+ "ManagedAppDistribution.AskForException.YourChildsData.Body.V2"
+ "ManagedAppDistribution.DeveloperApproval.App.UnavailableFeatures.Body.EU"
+ "ManagedAppDistribution.DeveloperApproval.App.UnavailableFeatures.Title.EU"
+ "ManagedAppDistribution.DeveloperApproval.App.YourData.Body.EU"
+ "ManagedAppDistribution.DeveloperApproval.UnavailableFeatures.Body.EU"
+ "ManagedAppDistribution.DeveloperApproval.UnavailableFeatures.Title.EU"
+ "ManagedAppDistribution.DeveloperApproval.YourData.Body.EU"
+ "ManagedAppDistribution.InstallSheet.DeveloperApproval.Title.EU"
+ "ManagedAppDistribution.InstallSheet.Web.App.Body.NoLink.EU"
+ "ManagedAppDistribution.NotAllowed.Message.NoSettingsReference.EU"
+ "ManagedAppDistribution.NotAllowed.iPad.Message.NoSettingsReference.EU"
+ "ManagedAppDistribution.ReplaceSheet.AppStore.Body.NoLink.EU"
+ "ManagedAppDistribution.ReplaceSheet.Marketplace.Alternative.Body.NoLink.EU"
+ "ManagedAppDistribution.ReplaceSheet.Marketplace.Body.NoLink.EU"
+ "ManagedAppDistribution.ReplaceSheet.Web.App.Alternative.Body.NoLink.EU"
+ "ManagedAppDistribution.ReplaceSheet.Web.App.Body.NoLink.EU"
+ "No pinned app declaration found with identifier '%{public}s'"
+ "Unavailable App Store Features"
+ "Updates and purchases in this app will be managed by the developer “@@developerName@@”. Subscriptions and other features may no longer be supported by “@@currentDistributorName@@”. The information below was provided by the developer."
+ "Updates and purchases in this app will be managed by the developer “@@developerName@@”. The information below was provided by the developer."
+ "You will be able to directly install apps by “@@name@@” on this iPad from the web."
+ "You will be able to directly install apps by “@@name@@” on this iPhone from the web."
+ "Your App Store account, stored payment method, subscription management, and refund requests will not be available."
+ "Your in-app purchases and future updates for this app will be managed by App Store. Subscriptions and other features may no longer be supported by “@@currentDistributorName@@”. The information below was provided by the developer."
+ "Your in-app purchases and future updates for this app will be managed by “@@marketplaceName@@”. Subscriptions and other App Store features may no longer be supported. The information below was provided by the developer."
+ "Your in-app purchases and future updates for this app will be managed by “@@marketplaceName@@”. Subscriptions and other features may no longer be supported by “@@currentDistributorName@@”. The information below was provided by the developer."
+ "[%@] Client %{public}s is entitled to no library; refusing registration"
+ "[%@] Install failed with error: %{public}@"
+ "[ProgressCache] Can't update portions for untracked progress %{public}s"
+ "[ProgressCache] Updating progress portions for %{public}s to %{public}s"
+ "handleLaunchRequest(_:requiredDistributor:)"
+ "https://silverbullet.itunes.apple.com/content/e172e47e6c6349a6a03e21b0e4080e2c/app.jetpack"
+ "profileConnectionDidReceiveAllowCloudSyncChangedNotification:userInfo:"
+ "setDefaultMediaTypeForCurrentProcess:"
- "Any installed apps will be managed by the developer and may give them access to your child's data."
- "ManagedAppDistribution.AskForException.YourChildsData.Body"
- "No pinned declaration found with identifier '%{public}s'"
- "http://silverbullet.itunes.apple.com/content/e172e47e6c6349a6a03e21b0e4080e2c/app.jetpack"
- "managedPackageInstallationTaskInit"
```
