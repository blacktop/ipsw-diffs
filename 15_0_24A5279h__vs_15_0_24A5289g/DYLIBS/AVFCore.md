## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/Versions/A/AVFCore`

```diff

-2270.61.1.0.0
-  __TEXT.__text: 0x216138
-  __TEXT.__auth_stubs: 0x36f0
-  __TEXT.__objc_methlist: 0x1bbb8
+2270.65.1.0.0
+  __TEXT.__text: 0x2168d8
+  __TEXT.__auth_stubs: 0x3710
+  __TEXT.__objc_methlist: 0x1bc50
   __TEXT.__const: 0x358
-  __TEXT.__gcc_except_tab: 0x4f10
-  __TEXT.__cstring: 0x35f92
+  __TEXT.__gcc_except_tab: 0x4f00
+  __TEXT.__cstring: 0x3605c
   __TEXT.__oslogstring: 0x1f027
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x8fa8
-  __TEXT.__objc_classname: 0x662a
-  __TEXT.__objc_methname: 0x362fe
-  __TEXT.__objc_methtype: 0xaebf
-  __TEXT.__objc_stubs: 0x20760
-  __DATA_CONST.__got: 0x4b10
+  __TEXT.__unwind_info: 0x8fc8
+  __TEXT.__objc_classname: 0x6670
+  __TEXT.__objc_methname: 0x36391
+  __TEXT.__objc_methtype: 0xaee0
+  __TEXT.__objc_stubs: 0x207a0
+  __DATA_CONST.__got: 0x4b28
   __DATA_CONST.__const: 0x34c0
-  __DATA_CONST.__objc_classlist: 0x12c0
+  __DATA_CONST.__objc_classlist: 0x12c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaac0
+  __DATA_CONST.__objc_selrefs: 0xaad0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xdc0
+  __DATA_CONST.__objc_superrefs: 0xdc8
   __DATA_CONST.__objc_arraydata: 0x270
-  __AUTH_CONST.__auth_got: 0x1b88
-  __AUTH_CONST.__const: 0x3a08
-  __AUTH_CONST.__cfstring: 0x19ca0
-  __AUTH_CONST.__objc_const: 0x36e80
+  __AUTH_CONST.__auth_got: 0x1b98
+  __AUTH_CONST.__const: 0x3a10
+  __AUTH_CONST.__cfstring: 0x19d20
+  __AUTH_CONST.__objc_const: 0x36fd0
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x2d0
-  __AUTH.__objc_data: 0x2490
+  __AUTH.__objc_data: 0x24e0
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x25a8
+  __DATA.__objc_ivar: 0x25b8
   __DATA.__data: 0x1bd0
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x6c0

   - /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11303
-  Symbols:   28279
-  CStrings:  5062
+  Functions: 11314
+  Symbols:   28307
+  CStrings:  5065
 
Symbols:
+ +[AVMetricPlayerItemVariantSwitchStartEvent supportsSecureCoding]
+ -[AVAssetCustomURLBridgeForNSURLProtocol(NSURLProtocolUsageReporting) reportSuccessfulURLLoad]
+ -[AVMetricEventStream variantChangeStartEventWithFigMetricEvent:]
+ -[AVMetricHLSMediaSegmentRequestEvent indexFileURL]
+ -[AVMetricHLSMediaSegmentRequestEvent initWithDate:mediaTime:sessionID:indexFileURL:byteRange:isMapSegment:mediaType:mediaResourceRequestEvent:]
+ -[AVMetricPlayerItemVariantSwitchStartEvent dealloc]
+ -[AVMetricPlayerItemVariantSwitchStartEvent debugDescription]
+ -[AVMetricPlayerItemVariantSwitchStartEvent encodeWithCoder:]
+ -[AVMetricPlayerItemVariantSwitchStartEvent fromVariant]
+ -[AVMetricPlayerItemVariantSwitchStartEvent initWithCoder:]
+ -[AVMetricPlayerItemVariantSwitchStartEvent initWithDate:mediaTime:sessionID:fromVariant:toVariant:loadedTimeRanges:]
+ -[AVMetricPlayerItemVariantSwitchStartEvent loadedTimeRanges]
+ -[AVMetricPlayerItemVariantSwitchStartEvent toVariant]
+ GCC_except_table1017
+ GCC_except_table1021
+ GCC_except_table51
+ OBJC_IVAR_$_AVMetricHLSMediaSegmentRequestEvent._indexFileURL
+ OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchStartEvent._fromVariant
+ OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchStartEvent._loadedTimeRanges
+ OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchStartEvent._toVariant
+ _AVTelemetryGenerateID
+ _FigCAStatsReportingSubmitData
+ _OBJC_CLASS_$_AVMetricPlayerItemVariantSwitchStartEvent
+ _OBJC_METACLASS_$_AVMetricPlayerItemVariantSwitchStartEvent
+ __130-[AVContentKeySession(AVContentKeySessionPrivateUtilities) _invokeDelegateCallbackWithBlock:synchronouslyWhenDelegateQueueIsNULL:]_block_invoke.632
+ __143-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke.146
+ __92-[AVPlayerItem(AVMetricEventStreamPublisherInternal) getEventTimelineWithCompletionHandler:]_block_invoke.1433
+ __97-[AVContentKeySession makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:]_block_invoke.531
+ __OBJC_$_CLASS_METHODS_AVMetricPlayerItemVariantSwitchStartEvent
+ __OBJC_$_INSTANCE_METHODS_AVAssetCustomURLBridgeForNSURLProtocol(NSURLProtocolUsageReporting)
+ __OBJC_$_INSTANCE_METHODS_AVMetricPlayerItemVariantSwitchStartEvent
+ __OBJC_$_INSTANCE_VARIABLES_AVMetricPlayerItemVariantSwitchStartEvent
+ __OBJC_$_PROP_LIST_AVMetricPlayerItemVariantSwitchStartEvent
+ __OBJC_CLASS_RO_$_AVMetricPlayerItemVariantSwitchStartEvent
+ __OBJC_METACLASS_RO_$_AVMetricPlayerItemVariantSwitchStartEvent
+ ___52-[AVPlayerItem(AVPlayerItemSpeedRamp) setSpeedRamp:]_block_invoke
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1441
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1461
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1467
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1473
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1484
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1486
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1490
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1491
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1495
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1496
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1502
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1507
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1508
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1509
+ __avplayeritem_fpItemNotificationCallback_block_invoke_2.1492
+ __avplayeritem_fpItemNotificationCallback_block_invoke_2.1497
+ __avplayeritem_fpItemNotificationCallback_block_invoke_2.1504
+ __avplayeritem_fpItemNotificationCallback_block_invoke_3.1493
+ __avplayeritem_fpItemNotificationCallback_block_invoke_3.1505
+ __avplayeritem_fpItemNotificationCallback_block_invoke_4.1494
+ _kFigCAStatsReportingEventName_NSURLProtocolUsage
+ _kFigCAStatsReporting_PayloadKey_SuccessfulDataLoad
+ _objc_msgSend$initWithDate:mediaTime:sessionID:fromVariant:toVariant:loadedTimeRanges:
+ _objc_msgSend$initWithDate:mediaTime:sessionID:indexFileURL:byteRange:isMapSegment:mediaType:mediaResourceRequestEvent:
+ _objc_msgSend$reportSuccessfulURLLoad
+ _objc_msgSend$variantChangeStartEventWithFigMetricEvent:
+ _os_signpost_id_generate
+ initWithFigAsset:.sAVAssetCustomURLCallbacksForNSURLSession.226
- -[AVMetricHLSMediaSegmentRequestEvent initWithDate:mediaTime:sessionID:url:byteRange:isMapSegment:mediaType:mediaResourceRequestEvent:]
- -[AVPlayerItem(AVPlayerItemSpeedRamp) setSpeedRampData:]
- -[AVPlayerItem(AVPlayerItemSpeedRamp) speedRampData]
- GCC_except_table1016
- GCC_except_table1020
- GCC_except_table1024
- __130-[AVContentKeySession(AVContentKeySessionPrivateUtilities) _invokeDelegateCallbackWithBlock:synchronouslyWhenDelegateQueueIsNULL:]_block_invoke.629
- __92-[AVPlayerItem(AVMetricEventStreamPublisherInternal) getEventTimelineWithCompletionHandler:]_block_invoke.1441
- __97-[AVContentKeySession makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:]_block_invoke.528
- __OBJC_$_INSTANCE_METHODS_AVAssetCustomURLBridgeForNSURLProtocol
- ___52-[AVPlayerItem(AVPlayerItemSpeedRamp) speedRampData]_block_invoke
- ___56-[AVPlayerItem(AVPlayerItemSpeedRamp) setSpeedRampData:]_block_invoke
- __avplayeritem_fpItemNotificationCallback_block_invoke.1449
- __avplayeritem_fpItemNotificationCallback_block_invoke.1475
- __avplayeritem_fpItemNotificationCallback_block_invoke.1481
- __avplayeritem_fpItemNotificationCallback_block_invoke.1492
- __avplayeritem_fpItemNotificationCallback_block_invoke.1493
- __avplayeritem_fpItemNotificationCallback_block_invoke.1494
- __avplayeritem_fpItemNotificationCallback_block_invoke.1498
- __avplayeritem_fpItemNotificationCallback_block_invoke.1499
- __avplayeritem_fpItemNotificationCallback_block_invoke.1504
- __avplayeritem_fpItemNotificationCallback_block_invoke.1510
- __avplayeritem_fpItemNotificationCallback_block_invoke.1511
- __avplayeritem_fpItemNotificationCallback_block_invoke.1515
- __avplayeritem_fpItemNotificationCallback_block_invoke.1517
- __avplayeritem_fpItemNotificationCallback_block_invoke.1524
- __avplayeritem_fpItemNotificationCallback_block_invoke_2.1500
- __avplayeritem_fpItemNotificationCallback_block_invoke_2.1505
- __avplayeritem_fpItemNotificationCallback_block_invoke_2.1512
- __avplayeritem_fpItemNotificationCallback_block_invoke_3.1501
- __avplayeritem_fpItemNotificationCallback_block_invoke_3.1513
- __avplayeritem_fpItemNotificationCallback_block_invoke_4.1502
- _objc_msgSend$initWithDate:mediaTime:sessionID:url:byteRange:isMapSegment:mediaType:mediaResourceRequestEvent:
- _objc_msgSend$setSpeedRampData:
- initWithFigAsset:.sAVAssetCustomURLCallbacksForNSURLSession.223
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVDelegateUtilities.m"
+ "<AVMetricHLSMediaSegmentRequestEvent:%!p(MISSING) %!@(MISSING) indexFileURL:%!@(MISSING) isMapSegment:%!d(MISSING) mediaType:%!@(MISSING) mediaResourceRequestEvent:%!@(MISSING)>"
+ "<AVMetricPlayerItemVariantSwitchStartEvent:%!p(MISSING) %!@(MISSING) fromVariant:%!@(MISSING) toVariant:%!@(MISSING) loadedTimeRanges:%!@(MISSING)>"
+ "AVSampleBufferRenderSynchronizer init"
+ "Bug in client of AVContentKeySession: this AVContentKeyRequest (%!p(MISSING)) can no longer process key responses, as its managing AVContentKeySession was released"
+ "aivmov"
+ "indexFileURL"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVDelegateUtilities.m"
- "<AVMetricHLSMediaSegmentRequestEvent:%!p(MISSING) %!@(MISSING) isMapSegment:%!d(MISSING) mediaType:%!@(MISSING) mediaResourceRequestEvent:%!@(MISSING)>"
- "CMTIME_COMPARE_INLINE(sourceTimeRange.start, ==, kCMTimeZero)"
- "CMTIME_COMPARE_INLINE(targetTimeRange.start, ==, kCMTimeZero)"

```
