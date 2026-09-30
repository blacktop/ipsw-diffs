## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3405.8.1.0.0
-  __TEXT.__text: 0x69098
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x3518
+3406.5.1.0.0
+  __TEXT.__text: 0x69750
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0x3538
   __TEXT.__const: 0xf8
   __TEXT.__dlopen_cstrs: 0x296
   __TEXT.__gcc_except_tab: 0x1358
-  __TEXT.__cstring: 0x9f24
-  __TEXT.__oslogstring: 0xbd31
-  __TEXT.__unwind_info: 0x1108
-  __TEXT.__objc_classname: 0x424
-  __TEXT.__objc_methname: 0xa091
+  __TEXT.__cstring: 0x9fc7
+  __TEXT.__oslogstring: 0xbe08
+  __TEXT.__unwind_info: 0x1110
+  __TEXT.__objc_classname: 0x441
+  __TEXT.__objc_methname: 0xa0ea
   __TEXT.__objc_methtype: 0xfe4
-  __TEXT.__objc_stubs: 0x81e0
-  __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x1b68
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__objc_stubs: 0x8220
+  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__const: 0x1b90
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2730
+  __DATA_CONST.__objc_selrefs: 0x2740
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x5b0
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x4100
-  __AUTH_CONST.__objc_const: 0x4300
+  __AUTH_CONST.__cfstring: 0x4140
+  __AUTH_CONST.__objc_const: 0x4390
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x190
+  __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x350
   __DATA.__data: 0x230
   __DATA.__bss: 0x20

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D65F7E73-BD5D-35C8-A37C-A67C59312C57
-  Functions: 1414
-  Symbols:   5244
-  CStrings:  4140
+  UUID: FFC30F39-486D-31BE-8310-68CCE152D6C5
+  Functions: 1417
+  Symbols:   5259
+  CStrings:  4152
 
Symbols:
+ +[UAFCoreAnalyticsInstrumenter logUAFAssetSetState:assetSpecifiersAndVersions:]
+ +[UAFCoreAnalyticsInstrumenter sendCAEvent:assetSpecifier:assetVersion:]
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_UAFCoreAnalyticsInstrumenter
+ _OBJC_METACLASS_$_UAFCoreAnalyticsInstrumenter
+ __OBJC_$_CLASS_METHODS_UAFCoreAnalyticsInstrumenter
+ __OBJC_CLASS_RO_$_UAFCoreAnalyticsInstrumenter
+ __OBJC_METACLASS_RO_$_UAFCoreAnalyticsInstrumenter
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.436
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.437
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.447
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.448
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.394
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.379
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.401
+ ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.364
+ ___72+[UAFCoreAnalyticsInstrumenter sendCAEvent:assetSpecifier:assetVersion:]_block_invoke
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.417
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.449
+ ___block_descriptor_56_e8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ ___block_literal_global.322
+ ___block_literal_global.328
+ ___block_literal_global.392
+ _objc_msgSend$logUAFAssetSetState:assetSpecifiersAndVersions:
+ _objc_msgSend$sendCAEvent:assetSpecifier:assetVersion:
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.433
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.434
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.444
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.445
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.391
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.376
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.398
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.361
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.414
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.446
- ___block_literal_global.317
- ___block_literal_global.325
- ___block_literal_global.389
- ___block_literal_global.394
CStrings:
+ "%s Emitting asset set state CA event for %{public}@"
+ "%s Emitting asset set state CA event for specifier: %{public}@ with version: %{public}@ from asset set: %{public}@"
+ "%s Sent asset set state CA event for %{public}@"
+ "+[UAFCoreAnalyticsInstrumenter logUAFAssetSetState:assetSpecifiersAndVersions:]"
+ "@\"NSDictionary\"8@?0"
+ "UAFCoreAnalyticsInstrumenter"
+ "com.apple.MobileAsset.CN.Guardrail"
+ "com.apple.uaf.AssetSetState"
+ "logUAFAssetSetState:assetSpecifiersAndVersions:"
+ "sendCAEvent:assetSpecifier:assetVersion:"

```
