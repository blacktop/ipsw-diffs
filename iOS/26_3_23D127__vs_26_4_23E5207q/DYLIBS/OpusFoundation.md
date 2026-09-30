## OpusFoundation

> `/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusFoundation.framework/OpusFoundation`

```diff

-1703.1.160.0.0
-  __TEXT.__text: 0x2c5c8
+1704.0.100.0.0
+  __TEXT.__text: 0x2c560
   __TEXT.__auth_stubs: 0x1030
   __TEXT.__objc_methlist: 0x3ee0
   __TEXT.__const: 0x29c
-  __TEXT.__cstring: 0x1e82
+  __TEXT.__cstring: 0x20f8
   __TEXT.__gcc_except_tab: 0x4d8
   __TEXT.__unwind_info: 0xe40
   __TEXT.__objc_classname: 0x813

   __TEXT.__objc_methtype: 0x1fb1
   __TEXT.__objc_stubs: 0x83c0
   __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x7b0
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x78

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 232E27F4-960A-3436-A9A4-F134FE75D4A5
+  UUID: 78D5DCD4-6FCC-39BA-919D-32C839499DB9
   Functions: 1316
   Symbols:   5176
   CStrings:  2980
Symbols:
+ _objc_retain_x27
- _objc_retain_x8
Functions:
~ +[NSString(OFNSStringExtensions) shortTimeCodeStringWithDuration:] : 216 -> 212
~ _OFAVAssetTranscode : 1288 -> 1312
~ -[CALayer(OFCALayerExtensions) alignOnPixels] : 248 -> 232
~ -[CALayer(OFCALayerExtensions) containsLayer:] : 260 -> 256
~ __ParseNumbers : 388 -> 384
~ -[OFNSOperation _finish:] : 488 -> 484
~ -[OFPageViewController _handlePanGesture:] : 876 -> 880
~ -[OFPageViewController _fakeHandlePanGesture] : 876 -> 880
~ -[OFLRUCache init] : 184 -> 180
~ -[OFLRUCache dealloc] : 196 -> 176
~ -[OFLRUCache _promoteListElement:] : 84 -> 68
~ -[OFLRUCache _removeListElement:] : 168 -> 160
~ -[OFLRUCache setObject:forKey:] : 336 -> 316
~ -[OFLRUCache removeAllObjects] : 140 -> 136
~ -[OFLRUCache loadFromURL:] : 628 -> 608
~ -[OFImageCache purgeDiskCache:progressBlock:] : 972 -> 968
~ -[OFLocationCache initWithDiskCacheFilepath:] : 280 -> 284
~ -[OFUIWindowDraggingSession _finishPresentationViewWithCompletion:] : 1416 -> 1412
~ -[OFUIWindowDraggingSession endDragging:] : 724 -> 728
~ -[OFUIWindowDraggingSession objectsForPasteboardType:transcodeBlock:cache:] : 252 -> 244
~ +[OFTextConversion stringFromTextAlignment:] : 36 -> 44
~ +[OFTextConversion stringFromLigature:] : 36 -> 44
~ +[OFTextConversion stringAttributesWithAttributedString:scaleFactor:] : 236 -> 232
~ -[OFUITrackingPinchGestureRecognizer touchesMoved:withEvent:] : 744 -> 736
~ -[OFAudioRecorder _connectionWithMediaType:] : 412 -> 404
CStrings:
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Caching/OFImageCache.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Caching/OFLRUCache.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Caching/OFLocationCache.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Extensions/OFAVAssetExtensions.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Extensions/OFNSDataExtensions.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Extensions/OFNSFileManagerExtensions.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Extensions/OFNSURLExtensions.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Kit/OFUICollectionFlowView.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Kit/OFUIGridView.m"
+ "/Library/Caches/com.apple.xbs/9C9C894C-FFF8-45F2-879F-50721ED40CB1/TemporaryDirectory.WM1Vrj/Sources/SlideshowKit/OpusFoundation/Framework/Operations/OFNSOperation.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Caching/OFImageCache.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Caching/OFLRUCache.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Caching/OFLocationCache.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Extensions/OFAVAssetExtensions.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Extensions/OFNSDataExtensions.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Extensions/OFNSFileManagerExtensions.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Extensions/OFNSURLExtensions.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Kit/OFUICollectionFlowView.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Kit/OFUIGridView.m"
- "/Library/Caches/com.apple.xbs/Sources/SlideshowKit/OpusFoundation/Framework/Operations/OFNSOperation.m"

```
