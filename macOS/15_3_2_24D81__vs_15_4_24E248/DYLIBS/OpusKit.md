## OpusKit

> `/System/Library/PrivateFrameworks/Slideshows.framework/Versions/A/Frameworks/OpusKit.framework/Versions/A/OpusKit`

```diff

-1557.21.0.0.0
-  __TEXT.__text: 0x846bc
+1557.24.0.0.0
+  __TEXT.__text: 0x84554
   __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0xa298
+  __TEXT.__objc_methlist: 0xaf14
   __TEXT.__const: 0x410
   __TEXT.__cstring: 0x79be
-  __TEXT.__gcc_except_tab: 0x192c
-  __TEXT.__unwind_info: 0x2aa0
+  __TEXT.__gcc_except_tab: 0x1934
+  __TEXT.__unwind_info: 0x2a50
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x143e
   __TEXT.__objc_methname: 0x152bd
   __TEXT.__objc_methtype: 0x373f
   __TEXT.__objc_stubs: 0x10a20
-  __DATA_CONST.__got: 0xc50
-  __DATA_CONST.__const: 0xec8
+  __DATA_CONST.__got: 0xc60
+  __DATA_CONST.__const: 0xe88
   __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b68
+  __DATA_CONST.__objc_selrefs: 0x5ec0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x4f8
   __AUTH_CONST.__auth_got: 0x5a8
   __AUTH_CONST.__const: 0x2fd0
   __AUTH_CONST.__cfstring: 0x8a40
-  __AUTH_CONST.__objc_const: 0x18738
+  __AUTH_CONST.__objc_const: 0x17080
   __AUTH_CONST.__objc_intobj: 0x1bf0
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_floatobj: 0x30

   - /System/Library/PrivateFrameworks/Slideshows.framework/Versions/A/Frameworks/OpusFoundation.framework/Versions/A/OpusFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6EFCAD6E-4C84-3E6C-BAD9-C3B0A291CC85
-  Functions: 3896
-  Symbols:   9758
+  UUID: E94FE3A7-34AF-3882-897A-E1EBFD9FE725
+  Functions: 3879
+  Symbols:   9768
   CStrings:  6977
 
Symbols:
+ +[OKDocumentsManager defaultManager].cold.1
+ +[OKMediaManager defaultManager].cold.1
+ +[OKProducerManager defaultManager].cold.1
+ +[OKRuntime currentPlatform].cold.1
+ +[OKRuntime opusKitBundle].cold.1
+ +[OKSettings transactionsManager].cold.1
+ +[OKWidgetMediaViewProxy shouldDrawRegionOfInterest].cold.1
+ -[OKDocumentsManager localDocumentsDirectoryURL].cold.1
+ -[OKMediaFileSystemItem parseDate:].cold.1
+ -[OKMediaProducerItem parseDate:].cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Clusters/OKMediaClusterPredicate.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Clusters/OKMediaEventClusterPredicate.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Document/OKDocument.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Document/OKDocumentMovieExporter.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Document/OKDocumentViewController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Document/OKDocumentsManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Gestures/OKActionBinding.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Javascript/OKJavaScriptConsole.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Javascript/OKJavaScriptContext.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Media/FileSystem/OKMediaFileSystemItem.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Media/OKMediaItem.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Media/OKMediaItemMetadata.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Media/Producer/OKMediaProducerItem.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentCanvas.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentCouch.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentCouchStep.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentNavigator.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentPage.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentWidget.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Navigators/OKNavigatorViewController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Pages/OKPageViewController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Producer/OKProducer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Producer/OKProducerManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Producer/OKProducerPlugin.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Settings/OKSettings.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Settings/OKSettingsUtility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetMediaView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetMicaDocument.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetSpriteEmitterView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetWebView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Clusters/OKMediaClusterPredicate.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Clusters/OKMediaEventClusterPredicate.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Document/OKDocument.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Document/OKDocumentMovieExporter.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Document/OKDocumentViewController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Document/OKDocumentsManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Gestures/OKActionBinding.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Javascript/OKJavaScriptConsole.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Javascript/OKJavaScriptContext.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Media/FileSystem/OKMediaFileSystemItem.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Media/OKMediaItem.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Media/OKMediaItemMetadata.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Media/Producer/OKMediaProducerItem.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentCanvas.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentCouch.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentCouchStep.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentNavigator.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentPage.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Model/OKDocumentWidget.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Navigators/OKNavigatorViewController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Pages/OKPageViewController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Producer/OKProducer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Producer/OKProducerManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Producer/OKProducerPlugin.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Settings/OKSettings.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Settings/OKSettingsUtility.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetMediaView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetMicaDocument.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetSpriteEmitterView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SlideshowOSX/OpusKit/Framework/Widgets/OKWidgetWebView.m"

```
