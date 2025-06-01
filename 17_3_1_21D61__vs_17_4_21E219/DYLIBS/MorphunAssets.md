## MorphunAssets

> `/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets`

```diff

-3300.101.1.0.0
-  __TEXT.__text: 0x82bc
+3304.61.1.0.0
+  __TEXT.__text: 0x859c
   __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x420
+  __TEXT.__objc_methlist: 0x430
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x58c
-  __TEXT.__cstring: 0xbb7
+  __TEXT.__gcc_except_tab: 0x590
+  __TEXT.__cstring: 0xbba
   __TEXT.__oslogstring: 0xa32
-  __TEXT.__unwind_info: 0x2d4
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__objc_classname: 0x70
-  __TEXT.__objc_methname: 0xe70
+  __TEXT.__objc_methname: 0xeea
   __TEXT.__objc_methtype: 0x130
-  __TEXT.__objc_stubs: 0x10a0
+  __TEXT.__objc_stubs: 0x10e0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x208
-  __DATA_CONST.__objc_selrefs: 0x4d0
+  __DATA_CONST.__objc_selrefs: 0x4e0
+  __DATA_CONST.__objc_classrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__cfstring: 0x680
   __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x220
-  __DATA.__objc_classrefs: 0xc8
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x8
-  __DATA_DIRTY.__const: 0xe0
+  __DATA_DIRTY.__const: 0x60
   __DATA_DIRTY.__objc_const: 0x120
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x70
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D5F0668-3DCF-349B-8E7D-2402A190A4D1
-  Functions: 143
-  Symbols:   630
-  CStrings:  382
+  UUID: F6B13E31-3955-3518-83DE-D1D906B2D2BD
+  Functions: 144
+  Symbols:   633
+  CStrings:  384
 
Symbols:
+ +[MorphunAssets(MorphunAssetsPrivate) updateUAFAssetSetForUsageValue:]
+ ___71+[MorphunAssets onDemandDownloadForLocale:withProgress:withCompletion:]_block_invoke.275
+ ___block_descriptor_40_ea8_32bs_e11_v24?0d8Q16ls32l8
+ ___block_literal_global.314
+ ___block_literal_global.320
+ ___block_literal_global.334
+ __unnamed_array_storage.278
+ __unnamed_array_storage.296
+ __unnamed_array_storage.305
+ __unnamed_array_storage.307
+ __unnamed_array_storage.308
+ _objc_msgSend$assetNamed:
+ _objc_msgSend$initWithName:assetSets:usageAliases:
+ _objc_msgSend$observeAssetSet:queue:handler:
+ _objc_msgSend$retrieveAssetSet:usages:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$subscriptionsForSubscriber:
+ _objc_msgSend$unsubscribe:subscriptionNames:queue:completion:
+ _objc_msgSend$updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:
+ _objc_msgSend$updateUAFAssetSetForUsageValue:
- _OBJC_CLASS_$_UAFAssetSet
- ___71+[MorphunAssets onDemandDownloadForLocale:withProgress:withCompletion:]_block_invoke.251
- ___block_descriptor_40_ea8_32bs_e8_v16?0Q8ls32l8
- ___block_literal_global.287
- ___block_literal_global.290
- ___block_literal_global.294
- __unnamed_array_storage.254
- __unnamed_array_storage.272
- __unnamed_array_storage.281
- __unnamed_array_storage.283
- __unnamed_array_storage.284
- _objc_msgSend$getAsset:
- _objc_msgSend$getSubscriptions:
- _objc_msgSend$init:assetSets:usageAliases:
- _objc_msgSend$initWithAssetSet:usages:
- _objc_msgSend$refresh
- _objc_msgSend$unsubscribe:subscriptions:queue:completion:
- _objc_msgSend$updateAssets:policies:queue:progress:completion:
- _observeUAFAssetSet.siriUnderstandingAssetSetObserver
CStrings:
+ "assetNamed:"
+ "initWithName:assetSets:usageAliases:"
+ "observeAssetSet:queue:handler:"
+ "retrieveAssetSet:usages:"
+ "sharedManager"
+ "subscriptionsForSubscriber:"
+ "unsubscribe:subscriptionNames:queue:completion:"
+ "updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:"
+ "updateUAFAssetSetForUsageValue:"
+ "v24@?0d8Q16"
- "getAsset:"
- "getSubscriptions:"
- "init:assetSets:usageAliases:"
- "initWithAssetSet:usages:"
- "refresh"
- "unsubscribe:subscriptions:queue:completion:"
- "updateAssets:policies:queue:progress:completion:"
- "v16@?0Q8"

```
