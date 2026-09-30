## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3500.92.1.0.0
-  __TEXT.__text: 0x6f984
+3500.96.1.0.0
+  __TEXT.__text: 0x6fb38
   __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x34a8
+  __TEXT.__objc_methlist: 0x34b8
   __TEXT.__const: 0x110
   __TEXT.__dlopen_cstrs: 0x296
   __TEXT.__gcc_except_tab: 0x14ac
-  __TEXT.__cstring: 0xab76
-  __TEXT.__oslogstring: 0xd294
-  __TEXT.__unwind_info: 0x11f0
+  __TEXT.__cstring: 0xab86
+  __TEXT.__oslogstring: 0xd2de
+  __TEXT.__unwind_info: 0x1250
   __TEXT.__objc_classname: 0x45d
-  __TEXT.__objc_methname: 0x9a82
+  __TEXT.__objc_methname: 0x9afd
   __TEXT.__objc_methtype: 0x1091
-  __TEXT.__objc_stubs: 0x7ca0
+  __TEXT.__objc_stubs: 0x7ce0
   __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x1c68
+  __DATA_CONST.__const: 0x1c60
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2578
+  __DATA_CONST.__objc_selrefs: 0x2588
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x608
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x4600
+  __AUTH_CONST.__cfstring: 0x4620
   __AUTH_CONST.__objc_const: 0x4270
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 428FF6DA-6D3D-3BE0-B2D8-F45C2EAFF684
+  UUID: 2BAB2E0D-C863-30CD-BC9C-85C141484DB8
   Functions: 1442
-  Symbols:   5301
-  CStrings:  4285
+  Symbols:   5305
+  CStrings:  4290
 
Symbols:
+ -[UAFAssetSetManager assetSetInfo:]
+ GCC_except_table73
+ GCC_except_table85
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.326
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.448
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.459
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.407
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.409
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.392
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.349
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.417
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.406
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.401
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.402
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.403
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.424
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.404
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.433
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.461
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.319
+ ___block_literal_global.310
+ ___block_literal_global.397
+ ___block_literal_global.405
+ ___block_literal_global.409
+ ___block_literal_global.413
+ ___block_literal_global.416
+ _kUAFConfigFileURL
+ _kUAFPallasURL
+ _kUAFPopulation
+ _objc_msgSend$assetSetInfo:
+ _objc_msgSend$endAtomicLocksSync:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:
- GCC_except_table74
- GCC_except_table86
- ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.317
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.450
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.461
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.408
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.410
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.393
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.340
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.418
- ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.409
- ___74+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]_block_invoke.377
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.404
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.405
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.406
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.427
- ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.407
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.434
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.462
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.310
- ___block_descriptor_72_e8_32s40s48s56s_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.301
- ___block_literal_global.400
- ___block_literal_global.406
- ___block_literal_global.412
- ___block_literal_global.414
- ___block_literal_global.417
CStrings:
+ "%s %{public}@: Downgrade condition encountered for %{public}@: %{public}@"
+ "assetSetInfo:"
+ "downgrade error"
+ "endAtomicLocksSync:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:"

```
