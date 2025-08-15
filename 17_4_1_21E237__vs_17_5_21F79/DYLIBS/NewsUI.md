## NewsUI

> `/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI`

```diff

-5345.2.0.0.0
-  __TEXT.__text: 0x34aa8
+5407.3.0.0.0
+  __TEXT.__text: 0x35504
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x42d8
+  __TEXT.__objc_methlist: 0x4310
   __TEXT.__const: 0x260
-  __TEXT.__cstring: 0x1f08
-  __TEXT.__gcc_except_tab: 0x6b4
-  __TEXT.__oslogstring: 0x965
+  __TEXT.__cstring: 0x1fa9
+  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__oslogstring: 0xa0c
   __TEXT.__ustring: 0x17a
-  __TEXT.__unwind_info: 0x10ac
-  __TEXT.__objc_classname: 0x13af
-  __TEXT.__objc_methname: 0xf909
-  __TEXT.__objc_methtype: 0x3641
-  __TEXT.__objc_stubs: 0x9860
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x1910
+  __TEXT.__unwind_info: 0x1160
+  __TEXT.__objc_classname: 0x13c9
+  __TEXT.__objc_methname: 0xfbb5
+  __TEXT.__objc_methtype: 0x372c
+  __TEXT.__objc_stubs: 0x9960
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x1988
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x358
+  __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf590
-  __DATA_CONST.__objc_selrefs: 0x2d18
-  __DATA_CONST.__objc_protorefs: 0x1c0
-  __DATA_CONST.__objc_classrefs: 0x678
+  __DATA_CONST.__objc_const: 0xf970
+  __DATA_CONST.__objc_selrefs: 0x2d50
+  __DATA_CONST.__objc_protorefs: 0x1c8
+  __DATA_CONST.__objc_classrefs: 0x680
   __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__objc_const: 0x24e0
-  __AUTH_CONST.__const: 0xd20
-  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__objc_const: 0x2528
+  __AUTH_CONST.__const: 0xd40
+  __AUTH_CONST.__cfstring: 0x1240
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__auth_got: 0x388
   __AUTH.__objc_data: 0xe10
-  __DATA.__objc_ivar: 0x5ec
-  __DATA.__data: 0x2820
-  __DATA.__bss: 0x90
+  __DATA.__objc_ivar: 0x5f0
+  __DATA.__data: 0x2880
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x1770
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 21F5DBA6-2816-34CB-8DA9-29649B69D605
-  Functions: 1655
-  Symbols:   7063
-  CStrings:  3622
+  UUID: 32CB22FE-0C43-35C0-8A75-1BBA4D6EA521
+  Functions: 1665
+  Symbols:   7107
+  CStrings:  3657
 
Symbols:
+ +[NUErrorMessageFactory errorMessageForArticleViewWithOfflineReason:]
+ +[NUErrorMessageFactory errorMessageForTitle:subtitle:]
+ -[NUANFContextLoader fallbackAssetForImageRequest:original:]
+ -[NUANFContextLoader initWithANFContent:flintResourceManager:networkReachability:host:resourceURLTranslator:headline:]
+ -[NUANFContextLoader networkReachability]
+ -[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]
+ -[NUArticlePrefetcher prefetchArticleID:headline:completion:]
+ GCC_except_table12
+ GCC_except_table22
+ GCC_except_table32
+ _FCCachedThumbnailForHeadline
+ _FCErrorDomain
+ _OBJC_CLASS_$_FCInterestToken
+ _OBJC_IVAR_$_NUANFContextLoader._networkReachability
+ __OBJC_$_CLASS_METHODS_NUErrorMessageFactory
+ __OBJC_$_PROP_LIST_FCNetworkReachabilityType
+ __OBJC_$_PROP_LIST_NUArticleViewControllerFactory.538
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCNetworkReachabilityType
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FCNetworkReachabilityType
+ __OBJC_$_PROTOCOL_REFS_FCNetworkReachabilityType
+ __OBJC_LABEL_PROTOCOL_$_FCNetworkReachabilityType
+ __OBJC_PROTOCOL_$_FCNetworkReachabilityType
+ __OBJC_PROTOCOL_REFERENCE_$_FCNetworkReachabilityType
+ ___33-[NUCoreAssembly loadInRegistry:]_block_invoke_25
+ ___38-[NUArticleViewController viewDidLoad]_block_invoke.78
+ ___49-[NUANFArticleDataProvider reloadArticleIfNeeded]_block_invoke.47
+ ___59-[NUANFArticleDataProvider loadContextWithCompletionBlock:]_block_invoke.23
+ ___59-[NUANFArticleDataProvider loadContextWithCompletionBlock:]_block_invoke.25
+ ___59-[NUANFArticleDataProvider loadContextWithCompletionBlock:]_block_invoke_2.18
+ ___59-[NUANFArticleDataProvider loadContextWithCompletionBlock:]_block_invoke_2.18.cold.1
+ ___59-[NUANFArticleDataProvider loadContextWithCompletionBlock:]_block_invoke_2.24
+ ___60-[NUANFContextLoader fallbackAssetForImageRequest:original:]_block_invoke
+ ___61-[NUArticlePrefetcher prefetchArticleID:headline:completion:]_block_invoke
+ ___61-[NUArticlePrefetcher prefetchArticleID:headline:completion:]_block_invoke.23
+ ___61-[NUArticlePrefetcher prefetchArticleID:headline:completion:]_block_invoke.cold.1
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke.32
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke.32.cold.1
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke.33
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke.34
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke_2
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke_3
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke_4
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke_6
+ ___69-[NUArticlePrefetcher _prefetchDataProviderWithArticleID:completion:]_block_invoke_7
+ ___70-[NUANFArticleDataProvider setupAssetPrefetchRequestEventsWithEvents:]_block_invoke.51
+ ___block_descriptor_40_e8_32bs_e23_v24?0B8B12"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e23_v24?0B8B12"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r_e52_v32?0"SXContext"8"NUANFAssetLoader"16"NSError"24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e33_v16?0"<NUArticleDataProvider>"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e55_v32?0"SXContext"8"<NUFontRegistrator>"16"NSError"24ls32l8s40l8s64l8s48l8s56l8
+ ___block_literal_global.168
+ ___block_literal_global.191
+ ___block_literal_global.201
+ ___block_literal_global.209
+ ___block_literal_global.224
+ ___block_literal_global.236
+ ___block_literal_global.243
+ ___block_literal_global.27
+ ___block_literal_global.282
+ ___block_literal_global.285
+ ___block_literal_global.289
+ ___block_literal_global.293
+ ___block_literal_global.297
+ ___block_literal_global.305
+ ___block_literal_global.309
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.316
+ ___block_literal_global.317
+ ___block_literal_global.322
+ ___block_literal_global.334
+ ___block_literal_global.338
+ ___block_literal_global.346
+ ___block_literal_global.354
+ ___block_literal_global.389
+ ___block_literal_global.393
+ ___block_literal_global.409
+ ___block_literal_global.412
+ ___block_literal_global.431
+ ___block_literal_global.435
+ ___block_literal_global.489
+ ___block_literal_global.499
+ ___block_literal_global.508
+ ___block_literal_global.515
+ ___block_literal_global.525
+ ___block_literal_global.847
+ ___block_literal_global.855
+ ___block_literal_global.880
+ ___block_literal_global.887
+ ___block_literal_global.896
+ ___block_literal_global.899
+ ___block_literal_global.902
+ ___block_literal_global.908
+ ___block_literal_global.911
+ ___block_literal_global.930
+ ___block_literal_global.936
+ ___block_literal_global.944
+ ___block_literal_global.947
+ ___block_literal_global.950
+ ___block_literal_global.953
+ ___block_literal_global.955
+ ___block_literal_global.958
+ _objc_msgSend$_accessibilitySetOpaqueElementScrollsContentIntoView:
+ _objc_msgSend$_prefetchDataProviderWithArticleID:completion:
+ _objc_msgSend$addPrefetchInterestInArticleID:headline:
+ _objc_msgSend$allResourcesForImageIdentifier:
+ _objc_msgSend$fallbackAssetForImageRequest:original:
+ _objc_msgSend$initWithANFContent:flintResourceManager:networkReachability:host:resourceURLTranslator:headline:
+ _objc_msgSend$initWithCallbackQueue:removeInterestBlock:
+ _objc_msgSend$initWithConfiguration:configurationManager:contentHostDirectory:privateDataHostDirectory:privateDataActionProvider:networkBehaviorMonitor:networkReachability:appActivityMonitor:desiredHeadlineFieldOptions:feedUsage:deviceIsiPad:backgroundTaskable:privateDataSyncAvailability:pptContext:options:
+ _objc_msgSend$metadata
+ _objc_msgSend$removePrefetchInterestInArticleID:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$thumbnailImageIdentifier
- -[NUANFContextLoader fallbackResourceForImageRequest:originalResource:]
- -[NUANFContextLoader initWithANFContent:flintResourceManager:host:resourceURLTranslator:headline:]
- -[NUErrorMessageFactory errorMessageForTitle:subtitle:]
- GCC_except_table27
- GCC_except_table28
- __OBJC_$_PROP_LIST_NUArticleViewControllerFactory.529
- ___38-[NUArticleViewController viewDidLoad]_block_invoke.72
- ___59-[NUANFArticleDataProvider loadContextWithCompletionBlock:]_block_invoke.19
- ___59-[NUANFArticleDataProvider loadContextWithCompletionBlock:]_block_invoke.24
- ___59-[NUANFArticleDataProvider loadContextWithCompletionBlock:]_block_invoke_2.23
- ___70-[NUANFArticleDataProvider setupAssetPrefetchRequestEventsWithEvents:]_block_invoke.47
- ___71-[NUANFContextLoader fallbackResourceForImageRequest:originalResource:]_block_invoke
- ___71-[NUANFContextLoader fallbackResourceForImageRequest:originalResource:]_block_invoke_2
- ___71-[NUANFContextLoader fallbackResourceForImageRequest:originalResource:]_block_invoke_3
- ___71-[NUANFContextLoader fallbackResourceForImageRequest:originalResource:]_block_invoke_4
- ___82-[NUArticlePrefetcher keyedOperationQueue:performAsyncOperationForKey:completion:]_block_invoke.25
- ___82-[NUArticlePrefetcher keyedOperationQueue:performAsyncOperationForKey:completion:]_block_invoke.25.cold.1
- ___82-[NUArticlePrefetcher keyedOperationQueue:performAsyncOperationForKey:completion:]_block_invoke.26
- ___82-[NUArticlePrefetcher keyedOperationQueue:performAsyncOperationForKey:completion:]_block_invoke_2
- ___82-[NUArticlePrefetcher keyedOperationQueue:performAsyncOperationForKey:completion:]_block_invoke_3
- ___82-[NUArticlePrefetcher keyedOperationQueue:performAsyncOperationForKey:completion:]_block_invoke_4
- ___82-[NUArticlePrefetcher keyedOperationQueue:performAsyncOperationForKey:completion:]_block_invoke_6
- ___82-[NUArticlePrefetcher keyedOperationQueue:performAsyncOperationForKey:completion:]_block_invoke_7
- ___block_descriptor_64_e8_32s40s48r_e40_v24?0"SXContext"8"NUANFAssetLoader"16ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e33_v16?0"<NUArticleDataProvider>"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e55_v32?0"SXContext"8"<NUFontRegistrator>"16"NSError"24ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.160
- ___block_literal_global.184
- ___block_literal_global.194
- ___block_literal_global.202
- ___block_literal_global.214
- ___block_literal_global.226
- ___block_literal_global.231
- ___block_literal_global.259
- ___block_literal_global.26
- ___block_literal_global.272
- ___block_literal_global.276
- ___block_literal_global.280
- ___block_literal_global.283
- ___block_literal_global.284
- ___block_literal_global.287
- ___block_literal_global.288
- ___block_literal_global.292
- ___block_literal_global.296
- ___block_literal_global.300
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.312
- ___block_literal_global.325
- ___block_literal_global.329
- ___block_literal_global.337
- ___block_literal_global.341
- ___block_literal_global.376
- ___block_literal_global.380
- ___block_literal_global.395
- ___block_literal_global.399
- ___block_literal_global.402
- ___block_literal_global.403
- ___block_literal_global.460
- ___block_literal_global.470
- ___block_literal_global.479
- ___block_literal_global.486
- ___block_literal_global.496
- ___block_literal_global.831
- ___block_literal_global.839
- ___block_literal_global.850
- ___block_literal_global.857
- ___block_literal_global.866
- ___block_literal_global.869
- ___block_literal_global.872
- ___block_literal_global.878
- ___block_literal_global.881
- ___block_literal_global.893
- ___block_literal_global.900
- ___block_literal_global.906
- ___block_literal_global.914
- ___block_literal_global.917
- ___block_literal_global.920
- ___block_literal_global.925
- ___block_literal_global.928
- _objc_msgSend$fallbackResourceForImageRequest:originalResource:
- _objc_msgSend$initWithANFContent:flintResourceManager:host:resourceURLTranslator:headline:
- _objc_msgSend$initWithConfiguration:configurationManager:contentHostDirectory:privateDataHostDirectory:privateDataActionProvider:networkBehaviorMonitor:appActivityMonitor:desiredHeadlineFieldOptions:feedUsage:deviceIsiPad:backgroundTaskable:privateDataSyncAvailability:pptContext:options:
- _objc_msgSend$largestImageResourceForImageIdentifier:
- _objc_retain_x10
CStrings:
+ "+"
+ "-[NUArticlePrefetcher prefetchArticleID:headline:completion:]_block_invoke"
+ "@\"<FCNetworkBehaviorMonitor>\"16@0:8"
+ "@\"<FCNetworkReachabilityType>\""
+ "@\"<FCNetworkReachabilityType>\"16@0:8"
+ "Article data loader did fail loading context, articleID=%{public}@, error=%{public}@"
+ "Article data loader did not reload rapid-updates because network is not reachable"
+ "FCNetworkReachabilityType"
+ "T@\"<FCNetworkBehaviorMonitor>\",R,N"
+ "T@\"<FCNetworkReachabilityType>\",R,N"
+ "T@\"<FCNetworkReachabilityType>\",R,N,V_networkReachability"
+ "_accessibilitySetOpaqueElementScrollsContentIntoView:"
+ "_prefetchDataProviderWithArticleID:completion:"
+ "addSurfacedByArticleListID:"
+ "allResourcesForImageIdentifier:"
+ "applyConditionalScore:"
+ "cellularRadioAccessTechnology"
+ "conditionalScore"
+ "contentHostDirectoryURL"
+ "fallbackAssetForImageRequest:original:"
+ "fetchAppWidgetConfigurationWithTodayLiteConfig:additionalFields:completion:"
+ "initWithANFContent:flintResourceManager:networkReachability:host:resourceURLTranslator:headline:"
+ "initWithCallbackQueue:removeInterestBlock:"
+ "initWithConfiguration:configurationManager:contentHostDirectory:privateDataHostDirectory:privateDataActionProvider:networkBehaviorMonitor:networkReachability:appActivityMonitor:desiredHeadlineFieldOptions:feedUsage:deviceIsiPad:backgroundTaskable:privateDataSyncAvailability:pptContext:options:"
+ "isCloudKitReachable"
+ "isCoread"
+ "isNetworkReachableViaWiFi"
+ "isNetworkUsageInexpensive"
+ "markAsEvergreen"
+ "modificationDate"
+ "networkReachabilityConnectivityDidChange:"
+ "prefetch unexpectedly cancelled for article ID %@"
+ "prefetchArticleID:headline:completion:"
+ "reverseObjectEnumerator"
+ "setVerticalOffset:"
+ "storageSize"
+ "surfacedByArticleListIDs"
+ "thumbnailImageIdentifier"
+ "v24@0:8@\"<FCNetworkReachabilityObserving>\"16"
+ "v24@0:8@\"<FCNetworkReachabilityType>\"16"
+ "v24@?0B8B12@\"NSError\"16"
+ "v32@?0@\"SXContext\"8@\"NUANFAssetLoader\"16@\"NSError\"24"
+ "v36@0:8B16@\"NSDictionary\"20@?<v@?@\"<FCNewsAppConfiguration>\"@\"NSDictionary\"@\"NSData\"@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v40@0:8@\"NSString\"16@\"<FCHeadlineProviding>\"24@?<v@?@\"FCInterestToken\"@\"NSError\">32"
+ "verticalOffset"
- "*"
- "@\"FCNetworkBehaviorMonitor\"16@0:8"
- "T@\"FCNetworkBehaviorMonitor\",R,N"
- "fallbackResourceForImageRequest:originalResource:"
- "fetchAppWidgetConfigurationWithAdditionalFields:completion:"
- "initWithANFContent:flintResourceManager:host:resourceURLTranslator:headline:"
- "initWithConfiguration:configurationManager:contentHostDirectory:privateDataHostDirectory:privateDataActionProvider:networkBehaviorMonitor:appActivityMonitor:desiredHeadlineFieldOptions:feedUsage:deviceIsiPad:backgroundTaskable:privateDataSyncAvailability:pptContext:options:"
- "largestImageResourceForImageIdentifier:"
- "surfacedByArticleListID"
- "v24@0:8@\"FCNetworkReachability\"16"
- "v24@?0@\"SXContext\"8@\"NUANFAssetLoader\"16"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"<FCNewsAppConfiguration>\"@\"NSDictionary\"@\"NSError\">24"

```
