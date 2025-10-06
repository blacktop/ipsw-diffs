## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-3557.1.0.0.0
-  __TEXT.__text: 0x2c5740
+5325.6.0.0.0
+  __TEXT.__text: 0x2c59ec
   __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_methlist: 0x28c88
+  __TEXT.__objc_methlist: 0x28c98
   __TEXT.__const: 0x1408
   __TEXT.__swift5_typeref: 0x89
-  __TEXT.__cstring: 0x46093
-  __TEXT.__oslogstring: 0xef64
+  __TEXT.__cstring: 0x46055
+  __TEXT.__oslogstring: 0xf004
   __TEXT.__gcc_except_tab: 0x362c
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x122
   __TEXT.__unwind_info: 0x9a9c
-  __TEXT.__objc_classname: 0x6a35
-  __TEXT.__objc_methname: 0x792f1
+  __TEXT.__objc_classname: 0x6a37
+  __TEXT.__objc_methname: 0x7931b
   __TEXT.__objc_methtype: 0xbaac
   __TEXT.__objc_stubs: 0x31120
   __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0xfe38
+  __DATA_CONST.__const: 0xfe90
   __DATA_CONST.__objc_classlist: 0x1918
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x6b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x61250
-  __DATA_CONST.__objc_selrefs: 0x126d0
+  __DATA_CONST.__objc_const: 0x612b0
+  __DATA_CONST.__objc_selrefs: 0x126d8
   __DATA_CONST.__objc_arraydata: 0xfc8
   __AUTH_CONST.__const: 0x4670
   __AUTH_CONST.__objc_const: 0x12650
-  __AUTH_CONST.__cfstring: 0x29920
+  __AUTH_CONST.__cfstring: 0x29940
   __AUTH_CONST.__objc_intobj: 0x1308
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0xbe0

   __DATA.__objc_protorefs: 0xa8
   __DATA.__objc_classrefs: 0x1e68
   __DATA.__objc_superrefs: 0x1380
-  __DATA.__objc_ivar: 0x3e1c
+  __DATA.__objc_ivar: 0x3e20
   __DATA.__data: 0x5118
   __DATA.__common: 0x8
   __DATA.__bss: 0x58

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E8739C06-43EF-35DF-B1BA-B5E7B9A09C26
-  Functions: 17808
-  Symbols:   57910
-  CStrings:  32994
+  UUID: 6DA41D97-C138-3547-9AF1-F49332578A45
+  Functions: 17810
+  Symbols:   57917
+  CStrings:  33000
 
Symbols:
+ -[FCNewsAppConfig widgetBackgroundInteractionEnabled]
+ -[FCSubscriptionController initWithSubscriptionList:tagController:puzzleTypeController:notificationController:purchaseProvider:configurationManager:appConfigurationManager:appActivityMonitor:userInfo:]
+ _OBJC_IVAR_$_FCSubscriptionController._userInfo
+ ___52-[FCBundleSubscription(Headlines) containsHeadline:]_block_invoke_3
+ ___54-[FCSubscriptionController _saveReadableSubscriptions]_block_invoke.516
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke.447
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_2.448
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_3.452
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_4.455
+ ___block_descriptor_40_e8_32s_e5_i8?0ls32l8
+ ___block_descriptor_48_e8_32s40w_e20_v24?0Q8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e34_v16?0"FCSubscriptionController"8ls32l8
+ ___block_literal_global.1190
+ ___block_literal_global.1257
+ ___block_literal_global.1332
+ ___block_literal_global.1334
+ ___block_literal_global.1336
+ ___block_literal_global.1344
+ ___block_literal_global.1355
+ ___block_literal_global.1360
+ ___block_literal_global.1365
+ ___block_literal_global.1370
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.461
+ ___block_literal_global.465
+ ___block_literal_global.468
+ ___block_literal_global.479
+ ___block_literal_global.481
+ ___block_literal_global.483
+ ___block_literal_global.850
+ ___block_literal_global.879
+ _objc_msgSend$initWithSubscriptionList:tagController:puzzleTypeController:notificationController:purchaseProvider:configurationManager:appConfigurationManager:appActivityMonitor:userInfo:
- -[FCSubscriptionController initWithSubscriptionList:tagController:puzzleTypeController:notificationController:purchaseProvider:configurationManager:appConfigurationManager:appActivityMonitor:]
- ___54-[FCSubscriptionController _saveReadableSubscriptions]_block_invoke.517
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke.448
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_2.449
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_3.453
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_4.456
- ___block_descriptor_40_e34_v16?0"FCSubscriptionController"8l
- ___block_literal_global.1184
- ___block_literal_global.1251
- ___block_literal_global.1326
- ___block_literal_global.1328
- ___block_literal_global.1330
- ___block_literal_global.1338
- ___block_literal_global.1349
- ___block_literal_global.1354
- ___block_literal_global.1359
- ___block_literal_global.1364
- ___block_literal_global.452
- ___block_literal_global.455
- ___block_literal_global.462
- ___block_literal_global.464
- ___block_literal_global.466
- ___block_literal_global.469
- ___block_literal_global.482
- ___block_literal_global.484
- ___block_literal_global.844
- ___block_literal_global.873
- _objc_msgSend$initWithSubscriptionList:tagController:puzzleTypeController:notificationController:purchaseProvider:configurationManager:appConfigurationManager:appActivityMonitor:
CStrings:
+ "\v"
+ "-[FCSubscriptionController initWithSubscriptionList:tagController:puzzleTypeController:notificationController:purchaseProvider:configurationManager:appConfigurationManager:appActivityMonitor:userInfo:]"
+ "Error when fetching purchase lookup record error=%{public}@"
+ "Found DawnburstD tabi configuration"
+ "createStatelessAggregatesWhichOnlyExistInLegacy2"
+ "initWithSubscriptionList:tagController:puzzleTypeController:notificationController:purchaseProvider:configurationManager:appConfigurationManager:appActivityMonitor:userInfo:"
+ "newsTabiConfigurationDawnburstD"
+ "priorStatelessAggregatesWithLegacyAggregates2"
+ "widgetBackgroundInteractionEnabled"
- "-[FCPurchaseLookupFetchOperation processFetchedResults:error:]_block_invoke"
- "-[FCSubscriptionController initWithSubscriptionList:tagController:puzzleTypeController:notificationController:purchaseProvider:configurationManager:appConfigurationManager:appActivityMonitor:]"
- "initWithSubscriptionList:tagController:puzzleTypeController:notificationController:purchaseProvider:configurationManager:appConfigurationManager:appActivityMonitor:"

```
