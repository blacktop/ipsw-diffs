## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2330.7.1.0.0
-  __TEXT.__text: 0x1bf520
+2340.8.1.0.0
+  __TEXT.__text: 0x1bf638
   __TEXT.__auth_stubs: 0x3920
-  __TEXT.__objc_methlist: 0x1d84c
+  __TEXT.__objc_methlist: 0x1d86c
   __TEXT.__cstring: 0x2709a
   __TEXT.__const: 0x278
   __TEXT.__gcc_except_tab: 0x48e8

   __TEXT.__ustring: 0x18
   __TEXT.__unwind_info: 0x8f90
   __TEXT.__objc_classname: 0x6798
-  __TEXT.__objc_methname: 0x373be
+  __TEXT.__objc_methname: 0x373ca
   __TEXT.__objc_methtype: 0xadef
-  __TEXT.__objc_stubs: 0x21ac0
-  __DATA_CONST.__got: 0x4c88
+  __TEXT.__objc_stubs: 0x21ae0
+  __DATA_CONST.__got: 0x4c90
   __DATA_CONST.__const: 0x5b98
   __DATA_CONST.__objc_classlist: 0x12f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf58
+  __DATA_CONST.__objc_selrefs: 0xaf60
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xda0
   __DATA_CONST.__objc_arraydata: 0x258
   __AUTH_CONST.__auth_got: 0x1ca0
   __AUTH_CONST.__const: 0xf38
   __AUTH_CONST.__cfstring: 0x19300
-  __AUTH_CONST.__objc_const: 0x353f0
+  __AUTH_CONST.__objc_const: 0x35418
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1BE6ED91-432D-3181-A56A-BF981493E76A
-  Functions: 11759
-  Symbols:   40866
+  UUID: 30CCC563-578F-3DE0-9D24-598C75E725F1
+  Functions: 11760
+  Symbols:   40870
   CStrings:  17403
 
Symbols:
+ -[AVPixelBufferAttributesVideoOutputSettings decompressionProperties]
+ _OBJC_IVAR_$_AVMetricEventStream._weakSelf
+ _kFigAssetReaderExtractionOption_DecompressionProperties
+ _objc_msgSend$decompressionProperties
- _OBJC_IVAR_$_AVMetricEventStream._publishers
Functions:
~ -[AVPlayerItem(AVMetricEventStreamPublisherInternal) getEventTimelineWithCompletionHandler:] : 696 -> 712
~ -[AVAssetReaderTrackOutput _figAssetReaderExtractionOptions] : 952 -> 1004
~ -[AVMetricEventStream init] : 200 -> 208
~ -[AVMetricEventStream didReceiveEventForMetricEventTimeline:event:] : 176 -> 180
~ ___50-[AVMetricEventStream addPublisher:eventTimeline:]_block_invoke : 728 -> 688
~ _avmetric_didReceiveEvent : 4 -> 152
~ ___46-[AVMetricEventStream subscribeToMetricEvent:]_block_invoke : 236 -> 240
~ ___49-[AVMetricEventStream subscribeToAllMetricEvents]_block_invoke : 208 -> 212
+ -[AVPixelBufferAttributesVideoOutputSettings decompressionProperties]
~ -[AVPlayerItemIntegratedTimelinePeriodicObserver rescheduleObserverWithSnapshot:itemToSchedule:] : 1660 -> 1736
CStrings:
+ "decompressionProperties"
- "_publishers"

```
