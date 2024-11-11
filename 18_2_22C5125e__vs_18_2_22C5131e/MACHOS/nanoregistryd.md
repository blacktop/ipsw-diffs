## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-989.4.4.0.0
-  __TEXT.__text: 0xf5a68
+989.4.5.2.0
+  __TEXT.__text: 0xf7bf8
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x106c0
-  __TEXT.__objc_methlist: 0xbc38
-  __TEXT.__const: 0x678
-  __TEXT.__gcc_except_tab: 0x24d4
-  __TEXT.__objc_methname: 0x1b3e0
-  __TEXT.__cstring: 0xd100
-  __TEXT.__oslogstring: 0x1331c
-  __TEXT.__objc_classname: 0x214f
+  __TEXT.__objc_stubs: 0x109e0
+  __TEXT.__objc_methlist: 0xbd80
+  __TEXT.__const: 0x688
+  __TEXT.__gcc_except_tab: 0x24fc
+  __TEXT.__objc_methname: 0x1b69a
+  __TEXT.__cstring: 0xd1a7
+  __TEXT.__oslogstring: 0x13a3c
+  __TEXT.__objc_classname: 0x2168
   __TEXT.__objc_methtype: 0x490b
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x3858
+  __TEXT.__unwind_info: 0x38d8
   __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0xc20
+  __DATA_CONST.__got: 0xc48
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4920
-  __DATA_CONST.__cfstring: 0xb9e0
-  __DATA_CONST.__objc_classlist: 0x798
+  __DATA_CONST.__const: 0x4a38
+  __DATA_CONST.__cfstring: 0xba40
+  __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x3c8
+  __DATA_CONST.__objc_superrefs: 0x3d0
   __DATA_CONST.__objc_intobj: 0xdb0
   __DATA_CONST.__objc_doubleobj: 0xb0
   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x1bdd0
-  __DATA.__objc_selrefs: 0x5890
-  __DATA.__objc_ivar: 0x1130
-  __DATA.__objc_data: 0x4bf0
+  __DATA.__objc_const: 0x1bf88
+  __DATA.__objc_selrefs: 0x5958
+  __DATA.__objc_ivar: 0x1140
+  __DATA.__objc_data: 0x4c40
   __DATA.__data: 0x19d8
-  __DATA.__bss: 0x498
+  __DATA.__bss: 0x4a8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 5553
-  Symbols:   678
-  CStrings:  8420
+  Functions: 5593
+  Symbols:   683
+  CStrings:  8475
 
Symbols:
+ _ASAttributeContentVersion
+ _NRCompatibilityIndexLatestAssetURLKey
+ _OBJC_CLASS_$_MAAsset
+ _OBJC_CLASS_$_MAAssetQuery
+ _OBJC_CLASS_$_MADownloadOptions
CStrings:
+ "35"
+ "EPMobileAssetAutoTrigger"
+ "EPMobileAssetAutoTrigger: Asset %!{(MISSING)public}@ failed to be purged with result %!l(MISSING)u and error %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: Asset %!{(MISSING)public}@ purged successfully"
+ "EPMobileAssetAutoTrigger: Asset catalog download for %!{(MISSING)public}@ completed successfully"
+ "EPMobileAssetAutoTrigger: Asset catalog download for %!{(MISSING)public}@ completed with result %!l(MISSING)u and error %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: Cooldown elapsed; triggering scan"
+ "EPMobileAssetAutoTrigger: Cooldown has not elapsed; deferring scan"
+ "EPMobileAssetAutoTrigger: Download of newest asset failed with result %!l(MISSING)u and error %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: Downloading asset catalog for %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: Init"
+ "EPMobileAssetAutoTrigger: Latest asset in query is %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: Newest available asset %!{(MISSING)public}@ downloaded to %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: Newest available asset %!{(MISSING)public}@ is already downloaded and located at %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: Newest available asset %!{(MISSING)public}@ is not present; starting download"
+ "EPMobileAssetAutoTrigger: Purging now out-of-date asset, %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: Query returned %!l(MISSING)u assets"
+ "EPMobileAssetAutoTrigger: getLastAssetUpdateCheckInterval: %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: kSBSLockStateNotifyKey received"
+ "EPMobileAssetAutoTrigger: notify_get_state UI Unlocked ***FAILED*** and returned %!l(MISSING)d"
+ "EPMobileAssetAutoTrigger: notify_registery_dispatch UI Unlocked notification ***FAILED*** and returned %!l(MISSING)d"
+ "EPMobileAssetAutoTrigger: setLastAssetUpdateCheckDate: %!{(MISSING)public}@"
+ "EPMobileAssetAutoTrigger: updateCompatibilityIndexAsset completed successfully"
+ "EPMobileAssetAutoTrigger: updateCompatibilityIndexAsset failed with error: %!{(MISSING)public}@"
+ "NRMobileAssetManager — Query for %!{(MISSING)public}@, installed assets only: %!s(MISSING)"
+ "NRMobileAssetManager — Query returned no assets"
+ "NanoRegistry-989.4.5.2"
+ "absoluteString"
+ "assetDownloadQueue"
+ "assetId"
+ "attributes"
+ "com.apple.MobileAsset.NanoRegistryPairingCompatibilityIndex"
+ "com.apple.nanoregistry.assetDownloadQueue"
+ "downloadAssetCatalogFor:userInitiated:withCompletion:"
+ "getLastAssetUpdateCheckInterval"
+ "getLatestAssetFromQueryResults:"
+ "getLocalFileUrl"
+ "initWithType:"
+ "lastAssetUpdateCheckDate"
+ "logAsset"
+ "mobileAssetDownloadOptionsUserInitiated:"
+ "purgeWithError:"
+ "queryAndGetLatestAssetForAssetType:installedAssetsOnly:withCompletion:"
+ "queryMetaData:"
+ "results"
+ "returnTypes:"
+ "setAllowDaemonConnectionRetries:"
+ "setAllowsCellularAccess:"
+ "setDisableUI:"
+ "setDiscretionary:"
+ "setLastAssetUpdateCheckDate:"
+ "startCatalogDownload:options:completionWithError:"
+ "startDownload:completionWithError:"
+ "updateAssetFor:onQueue:userInitiated:withCompletion:"
+ "updateCompatibilityIndexAssetOnQueue:userInitiated:withCompletion:"
+ "v16@?0@\"MAAsset\"8"
+ "v24@?0q8@\"NSError\"16"
- "250"
- "NanoRegistry-989.4.4"

```
