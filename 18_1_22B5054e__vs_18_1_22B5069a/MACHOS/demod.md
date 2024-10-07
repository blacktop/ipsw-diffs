## demod

> `/usr/libexec/demod`

```diff

-1445.40.10.0.0
-  __TEXT.__text: 0xd5400
-  __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_stubs: 0x177c0
-  __TEXT.__objc_methlist: 0xa990
+1445.40.14.0.0
+  __TEXT.__text: 0xd6b78
+  __TEXT.__auth_stubs: 0x1b30
+  __TEXT.__objc_stubs: 0x179e0
+  __TEXT.__objc_methlist: 0xaa88
   __TEXT.__const: 0x21e
-  __TEXT.__gcc_except_tab: 0x42f0
-  __TEXT.__cstring: 0xe0ea
-  __TEXT.__objc_methname: 0x1b85e
-  __TEXT.__oslogstring: 0x16e7c
-  __TEXT.__objc_classname: 0x1536
+  __TEXT.__gcc_except_tab: 0x42fc
+  __TEXT.__cstring: 0xe48a
+  __TEXT.__objc_methname: 0x1bade
+  __TEXT.__oslogstring: 0x1730c
+  __TEXT.__objc_classname: 0x1549
   __TEXT.__objc_methtype: 0x3657
   __TEXT.__swift5_typeref: 0x63
   __TEXT.__swift5_capture: 0x38
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2b28
+  __TEXT.__unwind_info: 0x2b60
   __TEXT.__eh_frame: 0xf8
-  __DATA_CONST.__auth_got: 0xdb0
-  __DATA_CONST.__got: 0xc28
+  __DATA_CONST.__auth_got: 0xda8
+  __DATA_CONST.__got: 0xc58
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2990
-  __DATA_CONST.__cfstring: 0xcc00
-  __DATA_CONST.__objc_classlist: 0x648
+  __DATA_CONST.__const: 0x29d0
+  __DATA_CONST.__cfstring: 0xce20
+  __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_intobj: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x7c8
-  __DATA_CONST.__objc_arrayobj: 0x3a8
+  __DATA_CONST.__objc_arraydata: 0x810
+  __DATA_CONST.__objc_arrayobj: 0x3d8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x17e28
-  __DATA.__objc_selrefs: 0x67e8
+  __DATA.__objc_const: 0x17ee8
+  __DATA.__objc_selrefs: 0x6888
   __DATA.__objc_ivar: 0x9d8
-  __DATA.__objc_data: 0x3f30
+  __DATA.__objc_data: 0x3f80
   __DATA.__data: 0x2698
   __DATA.__bss: 0x500
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4886
-  Symbols:   862
-  CStrings:  9393
+  Functions: 4923
+  Symbols:   865
+  CStrings:  9456
 
Symbols:
+ _MAGetPallasUrlForType
+ _MASetPallasUrlForType
+ _OBJC_CLASS_$_CSFFollowUp
+ _OBJC_CLASS_$_CSFGMOptIn
+ _OBJC_CLASS_$_MAAutoAsset
+ _OBJC_CLASS_$_MAAutoAssetSet
+ _kSecAttrAccessible
+ _kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
- _$s25CloudSubscriptionFeatures7GMOptInC07isOptedE0SbvsTj
- _$s25CloudSubscriptionFeatures7GMOptInC6sharedACvgZ
- _$s25CloudSubscriptionFeatures7GMOptInCMa
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCoreMIDI
CStrings:
+ "%!s(MISSING) - Enable OptedIn"
+ "/BackupData/greyMatter"
+ "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/com.apple.MobileStoreDemo.ThimbleLongLivedTokens"
+ "Applying bogus Pallas URL to disable update for asset: %!{(MISSING)public}@"
+ "Clearing bogus Pallas URL to enable update for asset: %!{(MISSING)public}@"
+ "Demod purging GreyMatter assets"
+ "DisableUserHomeDeepClean"
+ "EnableAIModelAutoUpdate"
+ "Failed to archive keychain items: %!{(MISSING)public}@"
+ "Failed to call eliminateAll() on asset: %!{(MISSING)public}@"
+ "Failed to call eliminateAtomic() on asset: %!{(MISSING)public}@"
+ "Failed to decrypt and unarchive keychain items."
+ "Failed to decrypt keychain archived data."
+ "Failed to encrypt and archive keychain items."
+ "Failed to encrypt keychain archived data."
+ "Failed to load bt keychain info from demo volume."
+ "Failed to preserve Thimble long-lived tokens."
+ "Failed to read data from file: %!{(MISSING)public}@ error: %!{(MISSING)public}@"
+ "Failed to read keychain items for key: %!{(MISSING)public}@"
+ "Failed to remove file: %!{(MISSING)public}@ error: %!{(MISSING)public}@"
+ "Failed to restore Thimble long-lived tokens."
+ "Failed to save keychain item: %!{(MISSING)public}@"
+ "Failed to set Pallas URL: %!l(MISSING)ld"
+ "Failed to unarchive keychain items: %!{(MISSING)public}@"
+ "Failed to unset Pallas URL: %!l(MISSING)ld"
+ "Failed to write data to file: %!{(MISSING)public}@ error: %!{(MISSING)public}@"
+ "GreyMatter opt-in status after iCloud account setup: %!{(MISSING)bool}d"
+ "GreyMatter opt-in status before iCloud account setup: %!{(MISSING)bool}d"
+ "MSDGreyMatterOpter"
+ "No input file for Thimble long-lived tokens found."
+ "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IF_Planner"
+ "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IF_PlannerOverrides"
+ "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Siri_Understanding"
+ "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Siri_UnderstandingNLOverrides"
+ "Preserving Thimble long-lived tokens stored in keychain!"
+ "Purging existing asset: %!{(MISSING)public}@"
+ "Received invalid keychain subject from caller: %!{(MISSING)public}@"
+ "Restoring Thimble long-lived tokens to keychain!"
+ "Timed out calling eliminateAll() on asset."
+ "Timed out calling eliminateAtomic() on asset."
+ "archiveAndEncryptKeychainItems:"
+ "com.apple.MobileAsset.UAF.FM.GenerativeModels"
+ "com.apple.MobileAsset.UAF.FM.Overrides"
+ "com.apple.MobileAsset.UAF.IF.Planner"
+ "com.apple.MobileAsset.UAF.IF.PlannerOverrides"
+ "com.apple.MobileAsset.UAF.Siri.Understanding"
+ "com.apple.MobileAsset.UAF.Siri.UnderstandingNLOverrides"
+ "com.apple.NetworkServiceProxy.PrivateAccessTokens.LongLivedTokens"
+ "configureAutoUpdate:"
+ "configureGreyMatterAutoUpdate"
+ "dataWithPropertyList:format:options:error:"
+ "decryptAndUnarchiveKeychainItems:"
+ "disableUserHomeDeepClean"
+ "eliminateAllForAssetType:completion:"
+ "eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:"
+ "enableAIModelAutoUpdate"
+ "greyMatter"
+ "https://foobar.apple.com"
+ "isItemGreyMatterBackup:"
+ "isOptedIn"
+ "preserveAndEncryptKeychainItemsForKey:toFile:"
+ "preservePrivateAccessTokens"
+ "purgeExistingAssetOfIdentifier:"
+ "purgeExistingAssets"
+ "restoreAndDecryptKeychainItemsForKey:fromFile:"
+ "restorePrivateAccessTokens"
+ "setHasEngagedWithCFU:"
+ "setIsOptedIn:"
+ "toggleAutoUpdate:forAssetOfIdentifier:"
+ "v24@?0@\"MAAutoAssetSelector\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
- "Enable isOptedIn"
- "Failed to decrypt keychain data file."
- "Failed to get keychain info to save."
- "Failed to read content of encrypted keychain data file"
- "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Handwriting_Synthesis"
- "Recieved invalid subject from caller."
- "Unable to read keychain data file."
- "Unable to restore BT keychain item for attributes: %!{(MISSING)public}@"

```
