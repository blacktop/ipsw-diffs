## NewsUI

> `/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI`

```diff

-5805.0.0.0.0
-  __TEXT.__text: 0x33558
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x633c
-  __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x1f88
-  __TEXT.__gcc_except_tab: 0x820
-  __TEXT.__oslogstring: 0xa55
+5861.1.0.0.0
+  __TEXT.__text: 0x388bc
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x6624
+  __TEXT.__const: 0x258
+  __TEXT.__cstring: 0x21be
+  __TEXT.__gcc_except_tab: 0x858
+  __TEXT.__oslogstring: 0xf46
   __TEXT.__ustring: 0x146
-  __TEXT.__unwind_info: 0x1090
-  __TEXT.__objc_classname: 0x1386
-  __TEXT.__objc_methname: 0xf4ae
-  __TEXT.__objc_methtype: 0x3603
-  __TEXT.__objc_stubs: 0x9360
-  __DATA_CONST.__got: 0x810
-  __DATA_CONST.__const: 0x18d0
-  __DATA_CONST.__objc_classlist: 0x3a8
+  __TEXT.__unwind_info: 0x1368
+  __TEXT.__objc_classname: 0x1415
+  __TEXT.__objc_methname: 0xfbb2
+  __TEXT.__objc_methtype: 0x3798
+  __TEXT.__objc_stubs: 0x9940
+  __DATA_CONST.__got: 0x830
+  __DATA_CONST.__const: 0x1918
+  __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x360
+  __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3658
-  __DATA_CONST.__objc_protorefs: 0x1c8
-  __DATA_CONST.__objc_superrefs: 0x2e8
+  __DATA_CONST.__objc_selrefs: 0x37d0
+  __DATA_CONST.__objc_protorefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x388
-  __AUTH_CONST.__const: 0xd20
-  __AUTH_CONST.__cfstring: 0x1240
-  __AUTH_CONST.__objc_const: 0xe048
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0xd60
+  __AUTH_CONST.__cfstring: 0x12e0
+  __AUTH_CONST.__objc_const: 0xe4d8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x5c8
-  __DATA.__data: 0x2880
+  __DATA.__objc_ivar: 0x600
+  __DATA.__data: 0x29a0
   __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0x1720
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__objc_data: 0x17c0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4AE95163-BEF1-340D-9BB5-917AD40A5692
-  Functions: 1629
-  Symbols:   6964
-  CStrings:  3586
+  UUID: FF3D408B-5F20-34B5-8875-BC940D2119B9
+  Functions: 1693
+  Symbols:   7189
+  CStrings:  3704
 
Symbols:
+ -[NUANFAssetLoader documentController]
+ -[NUANFAssetLoader initWithDocumentController:flintResourceManager:]
+ -[NUANFAssetLoader setDocumentController:]
+ -[NUANFResourceDataSource .cxx_destruct]
+ -[NUANFResourceDataSource assetLoader]
+ -[NUANFResourceDataSource configureWithDocumentController:assetLoader:]
+ -[NUANFResourceDataSource documentController]
+ -[NUANFResourceDataSource fallbackAssetForImageRequest:original:]
+ -[NUANFResourceDataSource fileURLForURL:onCompletion:onError:]
+ -[NUANFResourceDataSource headline]
+ -[NUANFResourceDataSource imageDecodingQueue]
+ -[NUANFResourceDataSource initWithNetworkReachability:resourceURLTranslator:headline:]
+ -[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]
+ -[NUANFResourceDataSource networkReachability]
+ -[NUANFResourceDataSource resourceURLTranslator]
+ -[NUANFResourceDataSource setAssetLoader:]
+ -[NUANFResourceDataSource setDocumentController:]
+ -[NUANFResourceDataSource translateURL:]
+ -[NUArticleHostViewController articleViewController:didDetectLiveUpdates:headline:]
+ -[NUArticleHostViewController liveCoverageDelegate]
+ -[NUArticleHostViewController reloadArticleWithLatestLiveCoverageContent]
+ -[NUArticleHostViewController setLiveCoverageDelegate:]
+ -[NUArticleScrollPositionManager headlineDidScroll:position:timeSpent:]
+ -[NUArticleScrollPositionManager headlineWillDisappear:position:timeSpent:]
+ -[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:]
+ -[NUArticleViewController latestLiveCoverageContext]
+ -[NUArticleViewController liveCoverageDelegate]
+ -[NUArticleViewController liveCoverageManager:didDetectNewContent:newPostCount:]
+ -[NUArticleViewController liveCoverageManager:didFailWithError:]
+ -[NUArticleViewController liveCoverageManager:didFailWithError:].cold.1
+ -[NUArticleViewController liveCoverageManager]
+ -[NUArticleViewController processScrollPositionForViewDisappearance]
+ -[NUArticleViewController reloadArticleWithLatestLiveCoverageContent]
+ -[NUArticleViewController reloadArticleWithLatestLiveCoverageContent].cold.1
+ -[NUArticleViewController setLatestLiveCoverageContext:]
+ -[NUArticleViewController setLiveCoverageDelegate:]
+ -[NUArticleViewController timeSpentInArticle]
+ -[NUArticleViewController updateScrollPosition]
+ -[NULiveCoverageManager .cxx_destruct]
+ -[NULiveCoverageManager applicationWillEnterForeground:]
+ -[NULiveCoverageManager articleDataProvider]
+ -[NULiveCoverageManager configuration]
+ -[NULiveCoverageManager countLiveBlogPostsInContext:]
+ -[NULiveCoverageManager dealloc]
+ -[NULiveCoverageManager delegate]
+ -[NULiveCoverageManager effectivePollingInterval]
+ -[NULiveCoverageManager hasInitializedPostCount]
+ -[NULiveCoverageManager initWithArticleDataProvider:configurationManager:]
+ -[NULiveCoverageManager isArticleCurrentlyLive:]
+ -[NULiveCoverageManager isPolling]
+ -[NULiveCoverageManager lastLiveBlogPostCount]
+ -[NULiveCoverageManager performPollingCheck]
+ -[NULiveCoverageManager pollingTimer]
+ -[NULiveCoverageManager processNewContext:]
+ -[NULiveCoverageManager schedulePollingTimer]
+ -[NULiveCoverageManager setDelegate:]
+ -[NULiveCoverageManager setHasInitializedPostCount:]
+ -[NULiveCoverageManager setInitialContext:]
+ -[NULiveCoverageManager setLastLiveBlogPostCount:]
+ -[NULiveCoverageManager setPollingTimer:]
+ -[NULiveCoverageManager shouldEnablePolling]
+ -[NULiveCoverageManager startPolling]
+ -[NULiveCoverageManager stopPollingTimer]
+ -[NULiveCoverageManager stopPolling]
+ GCC_except_table13
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table23
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table73
+ _NULiveCoverageLog
+ _NULiveCoverageLog.cold.1
+ _NULiveCoverageLog.once
+ _NULiveCoverageLog.result
+ _OBJC_CLASS_$_NUANFResourceDataSource
+ _OBJC_CLASS_$_NULiveCoverageManager
+ _OBJC_CLASS_$_SXComponents
+ _OBJC_CLASS_$_SXLatestLivePostScrollPosition
+ _OBJC_IVAR_$_NUANFAssetLoader._documentController
+ _OBJC_IVAR_$_NUANFResourceDataSource._assetLoader
+ _OBJC_IVAR_$_NUANFResourceDataSource._documentController
+ _OBJC_IVAR_$_NUANFResourceDataSource._headline
+ _OBJC_IVAR_$_NUANFResourceDataSource._imageDecodingQueue
+ _OBJC_IVAR_$_NUANFResourceDataSource._networkReachability
+ _OBJC_IVAR_$_NUANFResourceDataSource._resourceURLTranslator
+ _OBJC_IVAR_$_NUArticleHostViewController._liveCoverageDelegate
+ _OBJC_IVAR_$_NUArticleViewController._latestLiveCoverageContext
+ _OBJC_IVAR_$_NUArticleViewController._liveCoverageDelegate
+ _OBJC_IVAR_$_NUArticleViewController._liveCoverageManager
+ _OBJC_IVAR_$_NULiveCoverageManager._articleDataProvider
+ _OBJC_IVAR_$_NULiveCoverageManager._configuration
+ _OBJC_IVAR_$_NULiveCoverageManager._delegate
+ _OBJC_IVAR_$_NULiveCoverageManager._hasInitializedPostCount
+ _OBJC_IVAR_$_NULiveCoverageManager._lastLiveBlogPostCount
+ _OBJC_IVAR_$_NULiveCoverageManager._pollingTimer
+ _OBJC_METACLASS_$_NUANFResourceDataSource
+ _OBJC_METACLASS_$_NULiveCoverageManager
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __OBJC_$_INSTANCE_METHODS_NUANFResourceDataSource
+ __OBJC_$_INSTANCE_METHODS_NULiveCoverageManager
+ __OBJC_$_INSTANCE_VARIABLES_NUANFResourceDataSource
+ __OBJC_$_INSTANCE_VARIABLES_NULiveCoverageManager
+ __OBJC_$_PROP_LIST_NUANFResourceDataSource
+ __OBJC_$_PROP_LIST_NUArticleViewControllerFactory.573
+ __OBJC_$_PROP_LIST_NULiveCoverageManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCCacheInvalidating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NUArticleViewControllerLiveCoverageDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NULiveCoverageManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FCCacheInvalidating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NUArticleViewControllerLiveCoverageDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NULiveCoverageManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_NUArticleViewControllerLiveCoverageDelegate
+ __OBJC_$_PROTOCOL_REFS_NULiveCoverageManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_NUANFResourceDataSource
+ __OBJC_CLASS_RO_$_NUANFResourceDataSource
+ __OBJC_CLASS_RO_$_NULiveCoverageManager
+ __OBJC_LABEL_PROTOCOL_$_FCCacheInvalidating
+ __OBJC_LABEL_PROTOCOL_$_NUArticleViewControllerLiveCoverageDelegate
+ __OBJC_LABEL_PROTOCOL_$_NULiveCoverageManagerDelegate
+ __OBJC_METACLASS_RO_$_NUANFResourceDataSource
+ __OBJC_METACLASS_RO_$_NULiveCoverageManager
+ __OBJC_PROTOCOL_$_FCCacheInvalidating
+ __OBJC_PROTOCOL_$_NUArticleViewControllerLiveCoverageDelegate
+ __OBJC_PROTOCOL_$_NULiveCoverageManagerDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_NUArticleDataProvider
+ ___130-[NUArticleViewControllerFactory createArticleViewControllerWithArticle:issue:context:relativePriority:articleHostViewController:]_block_invoke_4
+ ___286-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:]_block_invoke
+ ___286-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:]_block_invoke_2
+ ___286-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:]_block_invoke_3
+ ___286-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:]_block_invoke_4
+ ___286-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:]_block_invoke_5
+ ___286-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:]_block_invoke_6
+ ___36-[NUArticleAssembly loadInRegistry:]_block_invoke_35
+ ___43-[NULiveCoverageManager processNewContext:]_block_invoke
+ ___44-[NULiveCoverageManager performPollingCheck]_block_invoke
+ ___47-[NUArticleViewController updateScrollPosition]_block_invoke
+ ___49-[NUANFArticleDataProvider reloadArticleIfNeeded]_block_invoke.51
+ ___53-[NULiveCoverageManager countLiveBlogPostsInContext:]_block_invoke
+ ___62-[NUANFResourceDataSource fileURLForURL:onCompletion:onError:]_block_invoke
+ ___62-[NUANFResourceDataSource fileURLForURL:onCompletion:onError:]_block_invoke_2
+ ___62-[NUANFResourceDataSource fileURLForURL:onCompletion:onError:]_block_invoke_3
+ ___62-[NUANFResourceDataSource fileURLForURL:onCompletion:onError:]_block_invoke_4
+ ___65-[NUANFResourceDataSource fallbackAssetForImageRequest:original:]_block_invoke
+ ___68-[NUANFAssetLoader initWithDocumentController:flintResourceManager:]_block_invoke
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_10
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_2
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_3
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_4
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_5
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_6
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_7
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_8
+ ___69-[NUANFResourceDataSource loadImagesForImageRequest:completionBlock:]_block_invoke_9
+ ___70-[NUANFArticleDataProvider setupAssetPrefetchRequestEventsWithEvents:]_block_invoke.55
+ ___NULiveCoverageLog_block_invoke
+ ___block_descriptor_32_e45_"NULiveCoverageManager"16?0"<TFResolver>"8l
+ ___block_descriptor_40_e8_32r_e40_B24?0"SXComponents"8"<SXComponent>"16lr32l8
+ ___block_descriptor_48_e8_32bs40w_e43_v24?0"<FCAssetDataProvider>"8"NSError"16lw40l8s32l8
+ ___block_literal_global.1004
+ ___block_literal_global.1007
+ ___block_literal_global.1026
+ ___block_literal_global.1032
+ ___block_literal_global.1040
+ ___block_literal_global.1043
+ ___block_literal_global.1046
+ ___block_literal_global.1049
+ ___block_literal_global.1051
+ ___block_literal_global.1054
+ ___block_literal_global.13
+ ___block_literal_global.189
+ ___block_literal_global.209
+ ___block_literal_global.219
+ ___block_literal_global.264
+ ___block_literal_global.283
+ ___block_literal_global.298
+ ___block_literal_global.303
+ ___block_literal_global.306
+ ___block_literal_global.310
+ ___block_literal_global.314
+ ___block_literal_global.318
+ ___block_literal_global.322
+ ___block_literal_global.326
+ ___block_literal_global.334
+ ___block_literal_global.338
+ ___block_literal_global.349
+ ___block_literal_global.373
+ ___block_literal_global.375
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.391
+ ___block_literal_global.396
+ ___block_literal_global.397
+ ___block_literal_global.400
+ ___block_literal_global.402
+ ___block_literal_global.414
+ ___block_literal_global.418
+ ___block_literal_global.419
+ ___block_literal_global.423
+ ___block_literal_global.426
+ ___block_literal_global.512
+ ___block_literal_global.522
+ ___block_literal_global.531
+ ___block_literal_global.538
+ ___block_literal_global.548
+ ___block_literal_global.63
+ ___block_literal_global.943
+ ___block_literal_global.976
+ ___block_literal_global.983
+ ___block_literal_global.992
+ ___block_literal_global.995
+ ___block_literal_global.998
+ _objc_msgSend$NSArray
+ _objc_msgSend$articleViewController:didDetectLiveUpdates:headline:
+ _objc_msgSend$components
+ _objc_msgSend$componentsForContainerComponentWithIdentifier:
+ _objc_msgSend$configuration
+ _objc_msgSend$configureWithDocumentController:assetLoader:
+ _objc_msgSend$countLiveBlogPostsInContext:
+ _objc_msgSend$didRefreshArticle:
+ _objc_msgSend$document
+ _objc_msgSend$effectivePollingInterval
+ _objc_msgSend$enumerateComponentsWithBlock:
+ _objc_msgSend$hasInitializedPostCount
+ _objc_msgSend$headlineDidScroll:position:timeSpent:
+ _objc_msgSend$headlineWillDisappear:position:timeSpent:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithArticleDataProvider:configurationManager:
+ _objc_msgSend$initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:
+ _objc_msgSend$initWithDocumentController:flintResourceManager:
+ _objc_msgSend$initWithNetworkReachability:resourceURLTranslator:headline:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isArticleCurrentlyLive:
+ _objc_msgSend$isPolling
+ _objc_msgSend$lastLiveBlogPostCount
+ _objc_msgSend$latestLiveCoverageContext
+ _objc_msgSend$liveCoverageActiveWindow
+ _objc_msgSend$liveCoverageCompleted
+ _objc_msgSend$liveCoverageDelegate
+ _objc_msgSend$liveCoverageManager
+ _objc_msgSend$liveCoverageManager:didDetectNewContent:newPostCount:
+ _objc_msgSend$liveCoverageManager:didFailWithError:
+ _objc_msgSend$liveCoverageModifiedDate
+ _objc_msgSend$liveCoveragePollingInterval
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$performPollingCheck
+ _objc_msgSend$pollingTimer
+ _objc_msgSend$processNewContext:
+ _objc_msgSend$processScrollPositionForViewDisappearance
+ _objc_msgSend$reloadArticleWithLatestLiveCoverageContent
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$schedulePollingTimer
+ _objc_msgSend$setDocumentController:
+ _objc_msgSend$setHasInitializedPostCount:
+ _objc_msgSend$setInitialContext:
+ _objc_msgSend$setLastLiveBlogPostCount:
+ _objc_msgSend$setLatestLiveCoverageContext:
+ _objc_msgSend$setLiveCoverageDelegate:
+ _objc_msgSend$setPollingTimer:
+ _objc_msgSend$shouldEnablePolling
+ _objc_msgSend$startPolling
+ _objc_msgSend$stopPolling
+ _objc_msgSend$stopPollingTimer
+ _objc_msgSend$timeSpentInArticle
+ _objc_msgSend$updateScrollPosition
+ _objc_retainAutoreleasedReturnValue
- -[NUANFAssetLoader context]
- -[NUANFAssetLoader initWithContext:flintResourceManager:]
- -[NUANFAssetLoader setContext:]
- -[NUANFContextLoader fallbackAssetForImageRequest:original:]
- -[NUANFContextLoader fileURLForURL:onCompletion:onError:]
- -[NUANFContextLoader imageDecodingQueue]
- -[NUANFContextLoader loadImagesForImageRequest:completionBlock:]
- -[NUANFContextLoader translateURL:]
- -[NUArticleScrollPositionManager setPosition:headline:]
- -[NUArticleViewController didRestoreScrollPosition]
- -[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:]
- -[NUArticleViewController setDidRestoreScrollPosition:]
- -[NUArticleViewController updateScrollPositionFromContext]
- GCC_except_table33
- GCC_except_table34
- GCC_except_table71
- _OBJC_IVAR_$_NUANFAssetLoader._context
- _OBJC_IVAR_$_NUANFContextLoader._imageDecodingQueue
- _OBJC_IVAR_$_NUArticleViewController._didRestoreScrollPosition
- __OBJC_$_PROP_LIST_NUArticleViewControllerFactory.548
- __OBJC_CLASS_PROTOCOLS_$_NUANFContextLoader
- ___266-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:]_block_invoke
- ___266-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:]_block_invoke_2
- ___266-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:]_block_invoke_3
- ___266-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:]_block_invoke_4
- ___266-[NUArticleViewController initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:]_block_invoke_5
- ___49-[NUANFArticleDataProvider reloadArticleIfNeeded]_block_invoke.47
- ___57-[NUANFAssetLoader initWithContext:flintResourceManager:]_block_invoke
- ___57-[NUANFContextLoader fileURLForURL:onCompletion:onError:]_block_invoke
- ___57-[NUANFContextLoader fileURLForURL:onCompletion:onError:]_block_invoke_2
- ___57-[NUANFContextLoader fileURLForURL:onCompletion:onError:]_block_invoke_3
- ___57-[NUANFContextLoader fileURLForURL:onCompletion:onError:]_block_invoke_4
- ___60-[NUANFContextLoader fallbackAssetForImageRequest:original:]_block_invoke
- ___61-[NUArticleViewController finalizeArticleLoadingWithContext:]_block_invoke.364
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_10
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_2
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_3
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_4
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_5
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_6
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_7
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_8
- ___64-[NUANFContextLoader loadImagesForImageRequest:completionBlock:]_block_invoke_9
- ___70-[NUANFArticleDataProvider setupAssetPrefetchRequestEventsWithEvents:]_block_invoke.51
- ___block_descriptor_56_e8_32s40bs48w_e43_v24?0"<FCAssetDataProvider>"8"NSError"16lw48l8s40l8s32l8
- ___block_literal_global.1000
- ___block_literal_global.1008
- ___block_literal_global.1011
- ___block_literal_global.1014
- ___block_literal_global.1017
- ___block_literal_global.1022
- ___block_literal_global.186
- ___block_literal_global.206
- ___block_literal_global.216
- ___block_literal_global.239
- ___block_literal_global.251
- ___block_literal_global.265
- ___block_literal_global.288
- ___block_literal_global.304
- ___block_literal_global.307
- ___block_literal_global.311
- ___block_literal_global.312
- ___block_literal_global.315
- ___block_literal_global.316
- ___block_literal_global.319
- ___block_literal_global.323
- ___block_literal_global.327
- ___block_literal_global.331
- ___block_literal_global.335
- ___block_literal_global.339
- ___block_literal_global.341
- ___block_literal_global.353
- ___block_literal_global.357
- ___block_literal_global.365
- ___block_literal_global.376
- ___block_literal_global.380
- ___block_literal_global.398
- ___block_literal_global.401
- ___block_literal_global.420
- ___block_literal_global.424
- ___block_literal_global.463
- ___block_literal_global.513
- ___block_literal_global.523
- ___block_literal_global.532
- ___block_literal_global.539
- ___block_literal_global.549
- ___block_literal_global.62
- ___block_literal_global.911
- ___block_literal_global.919
- ___block_literal_global.944
- ___block_literal_global.960
- ___block_literal_global.963
- ___block_literal_global.966
- ___block_literal_global.972
- ___block_literal_global.975
- ___block_literal_global.987
- ___block_literal_global.994
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$didRestoreScrollPosition
- _objc_msgSend$initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:
- _objc_msgSend$initWithContext:flintResourceManager:
- _objc_msgSend$setDidRestoreScrollPosition:
- _objc_msgSend$setPosition:headline:
- _objc_msgSend$updateScrollPositionFromContext
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x9
CStrings:
+ "\"2"
+ "#"
+ "*"
+ "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsUI/NUArticlePrefetcher.m"
+ "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsUI/NUArticleTextActivityItemSource.m"
+ "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsUI/NUDeviceTrait.m"
+ "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsUI/NUEmbedConfigurationOperation.m"
+ "@\"<FCNewsAppConfiguration>\""
+ "@\"<FCSportsEventProviding>\"16@0:8"
+ "@\"<NUArticleViewControllerLiveCoverageDelegate>\""
+ "@\"<NULiveCoverageManagerDelegate>\""
+ "@\"NULiveCoverageManager\""
+ "@\"NULiveCoverageManager\"16@?0@\"<TFResolver>\"8"
+ "@\"SXDocumentController\""
+ "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
+ "B24@?0@\"SXComponents\"8@\"<SXComponent>\"16"
+ "FCCacheInvalidating"
+ "Initial LiveBlog post count set to %ld"
+ "Live coverage content reloaded successfully"
+ "Live coverage detected %ld new posts"
+ "Live coverage entering foreground"
+ "Live coverage polling already active, skipping start"
+ "Live coverage polling check failed: %{public}@"
+ "Live coverage polling check received new context"
+ "Live coverage polling check returned nil context"
+ "Live coverage polling conditions no longer met, stopping"
+ "Live coverage polling disabled: article outside active window (%.0fs since modified, window is %.0fs)"
+ "Live coverage polling disabled: live coverage marked as completed"
+ "Live coverage polling disabled: low data mode enabled"
+ "Live coverage polling disabled: low power mode enabled"
+ "Live coverage polling disabled: no headline available"
+ "Live coverage polling disabled: no modified date available"
+ "Live coverage polling failed: %{public}@"
+ "Live coverage polling force enabled via internal settings"
+ "Live coverage polling not enabled, skipping start"
+ "Live coverage polling started, interval=%f"
+ "Live coverage polling stopped"
+ "LiveCoverage"
+ "LiveCoverage detected %ld new posts (total: %ld)"
+ "NSArray"
+ "NUANFResourceDataSource"
+ "NUArticleViewControllerLiveCoverageDelegate"
+ "NULiveCoverageManager"
+ "NULiveCoverageManagerDelegate"
+ "No latest context available for live coverage reload"
+ "Performing live coverage polling check"
+ "Processing new context: current post count=%ld, previous post count=%ld"
+ "T@\"<FCNewsAppConfiguration>\",R,N,V_configuration"
+ "T@\"<FCSportsEventProviding>\",R,C,N"
+ "T@\"<NUArticleViewControllerLiveCoverageDelegate>\",W,N,V_liveCoverageDelegate"
+ "T@\"<NULiveCoverageManagerDelegate>\",W,N,V_delegate"
+ "T@\"NSTimer\",&,N,V_pollingTimer"
+ "T@\"NULiveCoverageManager\",R,N,V_liveCoverageManager"
+ "T@\"SXContext\",&,N,V_latestLiveCoverageContext"
+ "T@\"SXDocumentController\",&,N,V_documentController"
+ "TB,N,V_hasInitializedPostCount"
+ "TB,R,N,GisPolling"
+ "Tq,N,V_lastLiveBlogPostCount"
+ "Using fake new post count: %ld"
+ "_documentController"
+ "_hasInitializedPostCount"
+ "_lastLiveBlogPostCount"
+ "_latestLiveCoverageContext"
+ "_liveCoverageDelegate"
+ "_liveCoverageManager"
+ "_pollingTimer"
+ "articleViewController:didDetectLiveUpdates:headline:"
+ "components"
+ "componentsForContainerComponentWithIdentifier:"
+ "configureWithDocumentController:assetLoader:"
+ "countLiveBlogPostsInContext:"
+ "didRefreshArticle:"
+ "document"
+ "effectivePollingInterval"
+ "enumerateComponentsWithBlock:"
+ "hasInitializedPostCount"
+ "headlineDidScroll:position:timeSpent:"
+ "headlineWillDisappear:position:timeSpent:"
+ "initWithArray:"
+ "initWithArticleDataProvider:configurationManager:"
+ "initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:liveCoverageManager:"
+ "initWithDocumentController:flintResourceManager:"
+ "initWithNetworkReachability:resourceURLTranslator:headline:"
+ "integerForKey:"
+ "invalidateCachesWithConfig:"
+ "isArticleCurrentlyLive:"
+ "isPolling"
+ "lastLiveBlogPostCount"
+ "latestLiveCoverageContext"
+ "liveCoverageActiveWindow"
+ "liveCoverageCompleted"
+ "liveCoverageDelegate"
+ "liveCoverageManager"
+ "liveCoverageManager:didDetectNewContent:newPostCount:"
+ "liveCoverageManager:didFailWithError:"
+ "liveCoverageModifiedDate"
+ "liveCoveragePollingInterval"
+ "localizedDescription"
+ "newsarticles.livecoverage.auto_reload_on_new_posts"
+ "newsarticles.livecoverage.fake_new_post_count"
+ "newsarticles.livecoverage.force_enable_polling"
+ "newsarticles.livecoverage.polling_interval_override"
+ "performPollingCheck"
+ "polling"
+ "pollingTimer"
+ "processNewContext:"
+ "processScrollPositionForViewDisappearance"
+ "reloadArticleWithLatestLiveCoverageContent"
+ "removeObserver:name:object:"
+ "schedulePollingTimer"
+ "setDocumentController:"
+ "setHasInitializedPostCount:"
+ "setInitialContext:"
+ "setLastLiveBlogPostCount:"
+ "setLatestLiveCoverageContext:"
+ "setLiveCoverageDelegate:"
+ "setPollingTimer:"
+ "shouldEnablePolling"
+ "sportsEvent"
+ "startPolling"
+ "stopPolling"
+ "stopPollingTimer"
+ "timeSpentInArticle"
+ "updateScrollPosition"
+ "v24@0:8@\"FCCacheInvalidationConfig\"16"
+ "v32@0:8@\"NULiveCoverageManager\"16@\"NSError\"24"
+ "v40@0:8@\"<FCHeadlineProviding>\"16@\"SXScrollPosition\"24d32"
+ "v40@0:8@\"NUArticleViewController\"16q24@\"<FCHeadlineProviding>\"32"
+ "v40@0:8@\"NULiveCoverageManager\"16@\"SXContext\"24q32"
+ "v40@0:8@16@24q32"
+ "v40@0:8@16q24@32"
+ "viewWillDisappear"
- "\"1"
- "+"
- "/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsUI/NUArticlePrefetcher.m"
- "/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsUI/NUArticleTextActivityItemSource.m"
- "/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsUI/NUDeviceTrait.m"
- "/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsUI/NUEmbedConfigurationOperation.m"
- "@\"FCPersonalizationData\"16@0:8"
- "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
- "T@\"FCPersonalizationData\",R,N"
- "TB,N,V_didRestoreScrollPosition"
- "_didRestoreScrollPosition"
- "didRestoreScrollPosition"
- "initWithArticleDataProvider:scrollViewController:appStateMonitor:keyCommandManager:loadingListeners:headerBlueprintProvider:debugSettingsProvider:videoPlayerViewControllerManager:articleScrollPositionManager:chromeControl:spotlightManager:"
- "initWithContext:flintResourceManager:"
- "personalizationData"
- "setDidRestoreScrollPosition:"
- "setPosition:headline:"
- "updateScrollPositionFromContext"
- "v32@0:8@\"SXScrollPosition\"16@\"<FCHeadlineProviding>\"24"

```
