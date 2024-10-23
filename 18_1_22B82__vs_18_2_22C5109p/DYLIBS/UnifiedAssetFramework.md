## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3401.21.3.11.2
-  __TEXT.__text: 0x5f140
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x2e0c
+3402.53.1.1.3
+  __TEXT.__text: 0x619d4
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0x3024
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x10d0
-  __TEXT.__cstring: 0x8fef
-  __TEXT.__oslogstring: 0xa4dd
+  __TEXT.__gcc_except_tab: 0x10f4
+  __TEXT.__cstring: 0x9314
+  __TEXT.__oslogstring: 0xa83c
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__unwind_info: 0xfd8
-  __TEXT.__objc_classname: 0x3f5
-  __TEXT.__objc_methname: 0x93aa
-  __TEXT.__objc_methtype: 0xe3d
-  __TEXT.__objc_stubs: 0x77e0
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x1960
-  __DATA_CONST.__objc_classlist: 0x150
+  __TEXT.__unwind_info: 0x1050
+  __TEXT.__objc_classname: 0x411
+  __TEXT.__objc_methname: 0x96e3
+  __TEXT.__objc_methtype: 0xeac
+  __TEXT.__objc_stubs: 0x7a00
+  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__const: 0x19c8
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23c8
+  __DATA_CONST.__objc_selrefs: 0x2480
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x578
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__cfstring: 0x3bc0
-  __AUTH_CONST.__objc_const: 0x41d0
+  __AUTH_CONST.__cfstring: 0x3de0
+  __AUTH_CONST.__objc_const: 0x4460
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x314
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x334
   __DATA.__data: 0x230
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1297
-  Symbols:   1874
-  CStrings:  3320
+  Functions: 1339
+  Symbols:   1925
+  CStrings:  3396
 
Symbols:
+ _OBJC_CLASS_$_UAFAssetSetConsistencyToken
+ _OBJC_METACLASS_$_UAFAssetSetConsistencyToken
+ __CFCopySystemVersionDictionaryValue
+ __kCFSystemVersionProductVersionKey
+ _close
+ _kUAFAssetSetConsistencyTokenVersion_1_0_0
+ _kUAFXPCConfigureAssetDelivery
+ _kUAFXPCLockIfUnchanged
+ _kUAFXPCUserInitiated
CStrings:
+ "\a\x11\x17"
+ "%!@(MISSING)#%!@(MISSING)"
+ "%!s(MISSING) %!{(MISSING)public}@: %!{(MISSING)public}@ Could not lock asset set %!{(MISSING)public}@ with atomic instance %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "%!s(MISSING) %!{(MISSING)public}@: Consistency Token %!@(MISSING) does not match installed roots %!@(MISSING)"
+ "%!s(MISSING) %!{(MISSING)public}@: Consistency Token %!@(MISSING) has an experiment in it but disableExperimentation is YES"
+ "%!s(MISSING) %!{(MISSING)public}@: Could not get configuration for asset set %!{(MISSING)public}@"
+ "%!s(MISSING) Can't unlock %!@(MISSING): already unlocked"
+ "%!s(MISSING) Captured device metadata for UAFAssetDailyStatusWithDeviceProperties event"
+ "%!s(MISSING) Could not construct auto asset set %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "%!s(MISSING) Could not get short term status for asset set %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "%!s(MISSING) Could not init asset set %!{(MISSING)public}@ with consistency token %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "%!s(MISSING) Decoding of asset set consistency token failed"
+ "%!s(MISSING) Decoding of asset set consistency token failed: unsupported version %!{(MISSING)public}@"
+ "%!s(MISSING) Decoding of the asset set experiment id failed"
+ "%!s(MISSING) Failed to lock %!@(MISSING): %!@(MISSING)"
+ "%!s(MISSING) Failed to unlock %!@(MISSING): %!@(MISSING)"
+ "%!s(MISSING) Locked %!@(MISSING)"
+ "%!s(MISSING) OS version for the metadata asset: %!{(MISSING)public}@"
+ "%!s(MISSING) Siri & Dictation are turned off, so using Feedback logger for logging asset status"
+ "%!s(MISSING) Unlocked %!@(MISSING)"
+ "+[UAFAssetSetMetadata OSVersion]_block_invoke"
+ "+[UAFAutoAssetManager invalidateAtomicInstance:assetSetName:queue:completion:]"
+ "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:]"
+ "+[UAFInstrumentationProvider getDeviceMetadata]"
+ "+[UAFPreinstalledAssetsCache populateCache:]"
+ "-[UAFAsset isPresentOnDevice]"
+ "-[UAFAssetSet initWithAssetSet:usages:configurationDirURLs:disableExperimentation:consistencyToken:]"
+ "-[UAFAssetSetConsistencyToken initWithCoder:]"
+ "-[UAFAssetSetConsistencyToken lock:]"
+ "-[UAFAssetSetConsistencyToken unlock:]"
+ "-[UAFAssetSetExperiment initWithCoder:]"
+ "-[UAFAutoAssetSet initWithAssetSetName:autoAssets:uuid:experiment:atomicInstance:error:]"
+ "-[UAFAutoAssetSet lockAutoAssets:error:]"
+ "/private/var/MobileAsset/AssetsV2/locks"
+ "@\"UAFAssetSetConsistencyToken\""
+ "@52@0:8@16@24@32B40@44"
+ "@56@0:8@16@24@32@40@48"
+ "@72@0:8@16@24@32@40@48@56^@64"
+ "Asset Set Consistency Token %!@(MISSING) for assetSet %!@(MISSING) with atomic instance %!@(MISSING) (%!@(MISSING)) experiment %!@(MISSING) preinstalledAssetsSummary %!@(MISSING)"
+ "Cannot invalidate a token without an underlying atomic instance"
+ "Cannot invalidate latest atomic instance"
+ "ConfigureAssetDelivery"
+ "Experiment '%!@(MISSING)' with assetSpecifiers %!@(MISSING)"
+ "LockIfUnchanged"
+ "T@\"NSSet\",&,N,V_preinstalledAssetsSummary"
+ "T@\"NSUUID\",R,N,V_uuid"
+ "T@\"UAFAssetSetConsistencyToken\",R,C,V_consistencyToken"
+ "T@\"UAFAssetSetExperiment\",&,N,V_experiment"
+ "TB,N,V_locked"
+ "Ti,N,V_fd"
+ "UAFAssetSetConsistencyToken"
+ "UserInitiated"
+ "_consistencyToken"
+ "_fd"
+ "_locked"
+ "_preinstalledAssetsSummary"
+ "atomic_instance_%!@(MISSING).locker"
+ "autoAssetSet:usages:uuid:autoAssets:experiment:atomicInstance:error:"
+ "com.apple.UnifiedAssetFramework.FoundUsageType."
+ "consistencyToken"
+ "fd"
+ "initWithAssetSet:usages:configurationDirURLs:disableExperimentation:consistencyToken:"
+ "initWithAssetSetName:autoAssets:uuid:experiment:atomicInstance:error:"
+ "initWithExperimentId:assetSpecifiers:"
+ "initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:"
+ "invalidate:completion:"
+ "invalidateAtomicInstance:assetSetName:queue:completion:"
+ "isPresentOnDevice"
+ "lock:"
+ "lockAutoAssets:error:"
+ "lockURL"
+ "mutableCopy"
+ "populateCache:"
+ "preinstalledAssetsSummary"
+ "processAssetSet:allAssets:"
+ "propertiesAsDictionary:"
+ "retrieveAssetSet:usages:consistencyToken:"
+ "retrieveAssetSet:usages:consistencyToken:queue:completion:"
+ "setExperiment:"
+ "setFd:"
+ "setLocked:"
+ "setPreinstalledAssetsSummary:"
+ "shared_locks"
+ "summary:"
+ "unlock:"
+ "unlocked"
+ "v56@0:8@16@24@32@40@?48"
- "\b\x11\x15"
- "%!s(MISSING) %!{(MISSING)public}@: %!{(MISSING)public}@ Could not lock asset set %!{(MISSING)public}@: %!{(MISSING)public}@"
- "%!s(MISSING) %!{(MISSING)public}@: Could not get configuration for for asset set %!{(MISSING)public}@"
- "%!s(MISSING) Apple Intelligence Assets GMS allowed state: %!{(MISSING)public}@"
- "+[UAFAssetSet isAssetValid:context:]"
- "+[UAFPreinstalledAssetsCache assetSpecifier:assetSetConfiguration:]_block_invoke"
- "+[UAFPreinstalledAssetsCache assetSpecifiersFromRoots:]_block_invoke"
- "-[UAFAssetSet initWithAssetSet:usages:configurationDirURLs:disableExperimentation:]"
- "-[UAFAutoAssetSet initWithAssetSetName:autoAssets:uuid:experiment:error:]"
- "-[UAFAutoAssetSet lockAutoAssets:]"
- "@44@0:8@16@24@32B40"
- "Ok to download or serve"
- "Should not download or serve"
- "assetNamed"
- "autoAssetSet:usages:uuid:autoAssets:experiment:error:"
- "initWithAssetSet:usages:configurationDirURLs:disableExperimentation:"
- "initWithAssetSetName:autoAssets:uuid:experiment:error:"
- "isAssetValid:context:"
- "lockAutoAssets:"

```
