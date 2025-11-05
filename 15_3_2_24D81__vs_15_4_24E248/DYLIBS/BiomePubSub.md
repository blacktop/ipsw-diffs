## BiomePubSub

> `/System/Library/PrivateFrameworks/BiomePubSub.framework/Versions/A/BiomePubSub`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x446f8
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x5464
+166.17.1.0.0
+  __TEXT.__text: 0x44dc4
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0x5874
   __TEXT.__const: 0xcc8
-  __TEXT.__cstring: 0x126f
+  __TEXT.__cstring: 0x124f
   __TEXT.__oslogstring: 0x6b8
   __TEXT.__gcc_except_tab: 0x280
   __TEXT.__dlopen_cstrs: 0x9c

   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1170
+  __TEXT.__unwind_info: 0x11a8
   __TEXT.__objc_classname: 0x99a
   __TEXT.__objc_methname: 0x5506
   __TEXT.__objc_methtype: 0xd0d

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1628
+  __DATA_CONST.__objc_selrefs: 0x1698
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x318
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x1908
-  __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0x15010
+  __AUTH_CONST.__cfstring: 0xee0
+  __AUTH_CONST.__objc_const: 0x14908
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x22b0
   __AUTH.__data: 0x580
   __DATA.__objc_ivar: 0x738
   __DATA.__data: 0x1520
   __DATA.__bss: 0x1940
-  __DATA.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D4766546-87D0-3AB1-A71C-27EFD9594DF5
-  Functions: 2266
-  Symbols:   5662
-  CStrings:  1778
+  UUID: AB7B45DF-78AC-32D1-AE96-49F1C1ABCC8C
+  Functions: 2321
+  Symbols:   5703
+  CStrings:  1776
 
Symbols:
+ +[BMBookmarkClasses sharedInstance].cold.1
+ +[BPSBuffer publisherWithPublisher:upstreams:bookmarkState:].cold.1
+ +[BPSCorrelate publisherWithPublisher:upstreams:bookmarkState:].cold.1
+ -[BPSCorrelationProducer requestDemand:].cold.1
+ -[BPSCountWindow initWithCapacity:aggregator:identifier:].cold.1
+ -[BPSCountWindow requestDemand:].cold.1
+ -[BPSDebounce initWithUpstream:for:getTimestamp:].cold.1
+ -[BPSFilterProducer requestDemand:].cold.1
+ -[BPSMulticast lazySubject].cold.1
+ -[BPSReduceProducer requestDemand:].cold.1
+ -[BPSSessionWindow requestDemand:].cold.1
+ -[BPSSessionWindowAssigner assignWindow:input:].cold.1
+ -[BPSSessionWindowAssigner initWithGap:timestamp:aggregator:].cold.1
+ -[BPSSlidingWindowAssigner initWithInterval:slide:timestamp:aggregator:].cold.1
+ -[BPSSlidingWindowAssigner initWithInterval:slide:timestamp:aggregator:].cold.2
+ -[BPSSubscriberList removeTicket:].cold.1
+ -[BPSSubscriberList removeTicket:].cold.2
+ -[BPSThrottle initWithUpstream:interval:latest:getTimestamp:].cold.1
+ -[BPSTimeWindowProducer requestDemand:].cold.1
+ -[BPSTimer initWithUpstream:interval:getTimestamp:].cold.1
+ -[BPSTumblingWindowAssigner initWithInterval:timestamp:aggregator:].cold.1
+ -[BPSWindow downstream].cold.1
+ -[_BPSAbstractCombineLatest receiveInput:atIndex:].cold.1
+ -[_BPSAbstractCombineLatest receiveInput:atIndex:].cold.2
+ -[_BPSAbstractCombineLatest receiveSubscription:atIndex:].cold.1
+ -[_BPSAbstractCombineLatest requestDemand:].cold.1
+ -[_BPSAbstractCorrelateOrderedMerge receiveInput:atIndex:].cold.1
+ -[_BPSAbstractCorrelateOrderedMerge receiveInput:atIndex:].cold.2
+ -[_BPSAbstractCorrelateOrderedMerge receiveSubscription:atIndex:].cold.1
+ -[_BPSAbstractCorrelateOrderedMerge requestDemand:].cold.1
+ -[_BPSAbstractOrderedMerge receiveInput:atIndex:].cold.1
+ -[_BPSAbstractOrderedMerge receiveInput:atIndex:].cold.2
+ -[_BPSAbstractOrderedMerge receiveSubscription:atIndex:].cold.1
+ -[_BPSAbstractOrderedMerge requestDemand:].cold.1
+ -[_BPSAbstractZip receiveInput:index:].cold.1
+ -[_BPSAbstractZip receiveSubscription:index:].cold.1
+ -[_BPSAbstractZip requestDemand:].cold.1
+ -[_BPSFlatMapOuter requestDemand:].cold.1
+ -[_BPSInnerConduit requestDemand:].cold.1
+ -[_BPSInnerFutureConduit requestDemand:].cold.1
+ -[_BPSMerged receiveInput:atIndex:].cold.1
+ -[_BPSMulticastInner requestDemand:].cold.1
+ -[_BPSWindowerInner requestDemand:].cold.1
+ -[_BPSWindowerInner requestDemand:key:identifier:].cold.1
+ _$sSo15BPSHandleEventsC8upstream19receiveSubscription0D6Output0D10Completion0D6Cancel0D7RequestAByxGSo12BPSPublisher_p_ySo15BPSSubscriptionCcSgyxcSgySo13BPSCompletionCcSgyycSgySo9BPSDemandacSgtcfcTOTf4gnnnnnn_n
+ _OBJC_$_PROP_LIST_BMBookmarkablePublisher.149
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSo15BPSHandleEventsC8upstream19receiveSubscription0D6Output0D10Completion0D6Cancel0D7RequestAByxGSo12BPSPublisher_p_ySo15BPSSubscriptionCcSgyxcSgySo13BPSCompletionCcSgyycSgySo9BPSDemandacSgtcfcTO
- _OBJC_$_PROP_LIST_BMBookmarkablePublisher.152
- _OUTLINED_FUNCTION_3
- _fmodf
- _swift_FORCE_LOAD_$_swiftFoundation.284
- _swift_isUniquelyReferenced_nonNull_native
CStrings:
- "CCReplicatedEntityEnumeratorBookmark"

```
