## OpusKit

> `/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusKit.framework/OpusKit`

```diff

-1703.1.160.0.0
-  __TEXT.__text: 0xae124
+1704.0.100.0.0
+  __TEXT.__text: 0xae168
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_methlist: 0xe578
   __TEXT.__const: 0x4a5
-  __TEXT.__cstring: 0x990f
-  __TEXT.__gcc_except_tab: 0x2438
+  __TEXT.__cstring: 0xa55d
+  __TEXT.__gcc_except_tab: 0x2510
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x3a58
-  __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x1b19
   __TEXT.__objc_methname: 0x1c1c0
   __TEXT.__objc_methtype: 0x4cd4

   - /System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusFoundation.framework/OpusFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2D0D69DB-DE0A-39E5-9DF6-94C8F8B10FD2
-  Functions: 4996
+  UUID: 44593BD0-F131-3118-B1F9-301ECFAFEEEE
+  Functions: 4997
   Symbols:   17528
   CStrings:  8661
 
Functions:
+ sub_27583d8e0
~ -[OKTransitionParallaxPush _transitionInView:fromSubview:toSubview:wasInteractive:duration:doEaseIn:doEaseOut:isCompleting:wasCancelled:fromProgress:completionHandler:] : 972 -> 960
~ +[OKSettings exportClassSettings:toJavaScriptContext:] : 1252 -> 1240
~ +[OKSettingsUtility pointFromObject:] : 188 -> 248
~ +[OKSettingsUtility sizeFromObject:] : 188 -> 248
~ +[OKSettingsUtility coordinateLocationFromObject:] : 188 -> 228
~ +[OKSettingsUtility offsetFromObject:] : 188 -> 248
~ -[OKMediaItemMetadata writeToFileURL:] : 708 -> 680
~ -[OKPageUXViewController widgetViewsInDisplayRect:displaySet:andWarmupRect:warmupSet:] : 1036 -> 1040
~ -[OKPageUXViewController hasWidgetFocused] : 272 -> 268
~ -[OKMediaAspectRatioClusterPredicate evaluateItems:progressBlock:] : 1224 -> 1220
~ ___72-[OKProducerManager pluginWithIdentifier:progressBlock:completionBlock:]_block_invoke_2 : 764 -> 752
~ ___137-[OKProducerManager createPresentationWithPluginIdentifier:guidelines:mediaFeeder:mediaItemLookupDelegate:progressBlock:completionBlock:]_block_invoke : 2576 -> 2560
~ ___214-[OKProducerManager createDocumentAtFileURL:withPluginIdentifier:guidelines:mediaURLs:mediaItemLookupDelegate:flattenMedia:flattenProducer:prepareCaches:format:keepOpen:documentClass:progressBlock:completionBlock:]_block_invoke_5 : 332 -> 320
~ -[OKProducer prepareLiveAuthoringIfNeeded:error:] : 308 -> 304
~ -[OKPresentationViewControllerProxy updateDisplayResolution] : 572 -> 556
~ +[OKPresentationViewControllerProxy setupJavascriptContext:] : 1908 -> 1900
~ +[OKNavigatorViewControllerProxy setupJavascriptContext:] : 1660 -> 1656
~ -[OKDynamicAttachment initWithSettings:] : 332 -> 344
~ +[OKNavigatorLinearViewController supportedSettings] : 976 -> 972
~ -[OKNavigatorLinearViewController gotoPageWithName:animated:completion:] : 376 -> 380
~ -[OKNavigatorCollectionViewControllerProxy prepareAdjacentPages:withDirection:] : 984 -> 976
~ -[OKNavigatorCollectionViewControllerProxy prepareAdjacentPagesForScrolling] : 124 -> 132
~ -[OKNavigatorCollectionViewLayout itemClosestToCenter] : 436 -> 416
~ -[OKNavigatorScrollViewControllerProxy insertElement:inList:] : 116 -> 108
~ +[OKNavigatorScrollViewControllerProxy setupJavascriptContext:] : 732 -> 728
~ -[OKNavigatorScrollViewControllerProxy setTilt:] : 100 -> 96
~ +[OKPageViewController setupJavascriptContext:] : 1488 -> 1480
~ -[OKWidgetContainerView pointInside:withEvent:] : 344 -> 340
~ +[OKWidgetViewProxy supportedSettings] : 4424 -> 4404
~ -[OKWidgetViewProxy updateTransforms] : 304 -> 272
~ +[OKWidgetViewProxy setupJavascriptContext:] : 2396 -> 2380
~ -[OKWidgetViewProxy dictionaryProxy:objectForKey:] : 520 -> 516
~ -[OKWidgetView pointInside:withEvent:] : 368 -> 364
~ -[OKPanGenerator _updatePanSteps] : 1684 -> 1580
~ -[OKWidgetGridViewCondensedLayout indexPathsForItemsInRect:] : 996 -> 1124
~ -[OKWidgetGridViewCondensedLayout prepareLayout] : 924 -> 932
~ -[OKWidgetGridViewCondensedLayout targetContentOffsetForProposedContentOffset:withScrollingVelocity:] : 656 -> 640
~ ___47-[OKResourcesDiskCacheManager removeAllCaches:]_block_invoke : 120 -> 124
~ ___53-[OKResourcesDiskCacheManager removeMediaItem:error:]_block_invoke : 120 -> 124
~ ___64-[OKResourcesDiskCacheManager removeMetadataForMediaItem:error:]_block_invoke : 144 -> 148
~ ___66-[OKResourcesDiskCacheManager removeThumbnailsForMediaItem:error:]_block_invoke : 144 -> 148
~ -[OKRoundProgressView increaseUIProgress:] : 228 -> 224
~ -[OKActionBindingProxy performAction:] : 260 -> 256
~ -[OKClickWheelView initButtons] : 1472 -> 1468
~ ___32-[OKVideoPlayerController pause]_block_invoke : 96 -> 92
CStrings:
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Caches/OKResourcesDiskCacheManager.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Clusters/OKMediaClusterPredicate.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Clusters/OKMediaEventClusterPredicate.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Couch/OKCouchController.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Document/OKDocument.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Document/OKDocumentsManager.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Feeders/OKMediaFeeder.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Filters/OKWidgetBasicFilter.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Gestures/OKActionBinding.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Javascript/OKJavaScriptConsole.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Javascript/OKJavaScriptContext.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Materials/OKImageResourceLoader.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Materials/OKMaterial.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Materials/OKMicaResourceLoader.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Materials/OKResourceLoader.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Media/FileSystem/OKMediaFileSystemItem.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Media/OKMediaItem.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Media/OKMediaItemMetadata.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Media/PhotoKit/OKMediaPhotoKitItem.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Media/Producer/OKMediaProducerItem.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationCanvas.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationCouch.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationCouchStep.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationFeeder.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationMaterial.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationNavigator.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationPage.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationWidget.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Navigators/OKNavigatorScrollViewController.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Navigators/OKNavigatorViewController.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/OpusKit.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Pages/OKPageUXViewController.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Pages/OKPageViewController.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Presentation/OKPresentation.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Presentation/OKPresentationViewController.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Presets/OKProducerPresetsManager.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Producer/OKProducer.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Producer/OKProducerManager.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Producer/OKProducerPlugin.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Settings/OKSettings.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Settings/OKSettingsUtility.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Synopsis/OKSynopsisInterpreter.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Synopsis/OKSynopsisView.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetCameraView.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetGridViewCondensedLayout.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetMediaView.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetMicaDocument.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetSpriteEmitterView.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetView.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetWebView.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Caches/OKResourcesDiskCacheManager.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Clusters/OKMediaClusterPredicate.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Clusters/OKMediaEventClusterPredicate.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Couch/OKCouchController.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Document/OKDocument.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Document/OKDocumentsManager.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Feeders/OKMediaFeeder.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Filters/OKWidgetBasicFilter.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Gestures/OKActionBinding.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Javascript/OKJavaScriptConsole.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Javascript/OKJavaScriptContext.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Materials/OKImageResourceLoader.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Materials/OKMaterial.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Materials/OKMicaResourceLoader.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Materials/OKResourceLoader.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Media/FileSystem/OKMediaFileSystemItem.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Media/OKMediaItem.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Media/OKMediaItemMetadata.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Media/PhotoKit/OKMediaPhotoKitItem.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Media/Producer/OKMediaProducerItem.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationCanvas.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationCouch.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationCouchStep.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationFeeder.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationMaterial.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationNavigator.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationPage.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Model/OKPresentationWidget.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Navigators/OKNavigatorScrollViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Navigators/OKNavigatorViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/OpusKit.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Pages/OKPageUXViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Pages/OKPageViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Presentation/OKPresentation.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Presentation/OKPresentationViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Presets/OKProducerPresetsManager.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Producer/OKProducer.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Producer/OKProducerManager.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Producer/OKProducerPlugin.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Settings/OKSettings.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Settings/OKSettingsUtility.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Synopsis/OKSynopsisInterpreter.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Synopsis/OKSynopsisView.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetCameraView.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetGridViewCondensedLayout.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetMediaView.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetMicaDocument.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetSpriteEmitterView.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetView.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusKit/Framework/Widgets/OKWidgetWebView.m"

```
