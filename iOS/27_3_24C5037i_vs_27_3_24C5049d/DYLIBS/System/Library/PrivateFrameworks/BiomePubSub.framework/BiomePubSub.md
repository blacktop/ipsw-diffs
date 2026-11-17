## BiomePubSub

> `/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub`

```diff

-259.2.0.2.0
-  __TEXT.__text: 0x3e9dc
+259.5.0.0.0
+  __TEXT.__text: 0x3e938
   __TEXT.__objc_methlist: 0x5894
   __TEXT.__const: 0x1000
   __TEXT.__cstring: 0x116f
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[BPSSink completeWithError:] : 584 -> 580
~ -[BPSSink requestNextEvents] : 256 -> 252
~ -[BPSDrivableSink requestNextEvents] : 292 -> 288
~ -[BPSDrivableSink completeWithError:] : 324 -> 320
~ -[BPSSink subscribeTo:] : 344 -> 340
~ -[BPSDrivableSink subscribeTo:] : 344 -> 340
~ -[BPSSink cancel] : 312 -> 308
~ -[_BPSMerged applyDownstreamWhileLocked:apply:] : 232 -> 228
~ -[_BPSAbstractOrderedMerge _completeWhileLockedWithCompletion:] : 276 -> 272
~ -[_BPSAbstractOrderedMerge receiveCompletion:atIndex:] : 596 -> 592
~ -[_BPSAbstractOrderedMerge flushBufferAndRequestMoreWhileLocked] : 668 -> 664
~ -[_BPSFlatMapOuter receiveCompletion:] : 820 -> 812
~ -[_BPSFlatMapOuter requestDemand:] : 1516 -> 1504
~ -[_BPSFlatMapOuter receiveInnerInput:index:] : 528 -> 520
~ -[_BPSFlatMapOuter receiveInnerCompletion:index:] : 1036 -> 1028
~ -[_BPSAbstractCombineLatest receiveInput:atIndex:] : 716 -> 712
~ -[_BPSAbstractCombineLatest receiveCompletion:atIndex:] : 1008 -> 1000
~ -[BPSSink _cancel] : 96 -> 92
~ -[BPSDrivableSink cancel] : 312 -> 308
~ -[BPSDrivableSink _cancel] : 96 -> 92
~ -[_BPSAbstractZip receiveSubscription:index:] : 668 -> 664
~ -[_BPSAbstractZip receiveInput:index:] : 1328 -> 1324
~ -[_BPSAbstractZip lockSendCompletion:index:] : 460 -> 456
~ -[_BPSInnerConduit offerInput:] : 260 -> 256
~ -[BPSPassThroughSubject startWithSubscriber:] : 96 -> 92
~ -[BPSPassThroughSubject nextEvent] : 180 -> 176
~ -[BPSPassThroughSubject reset] : 116 -> 112
~ -[BPSPassThroughSubject bookmark] : 92 -> 88
~ -[BPSPassThroughSubject applyBookmark:] : 92 -> 88
~ -[BPSPassThroughSubject sendCompletion] : 104 -> 100
~ -[BPSPassThroughSubject sendEvent:] : 132 -> 128
~ -[_BPSAbstractCorrelateOrderedMerge _completeWhileLockedWithCompletion:] : 276 -> 272
~ -[_BPSAbstractCorrelateOrderedMerge receiveCompletion:atIndex:] : 596 -> 592
~ -[_BPSAbstractCorrelateOrderedMerge flushBufferAndRequestMoreWhileLocked] : 812 -> 808
~ ___38-[BPSFuture initWithAttemptToFulfill:]_block_invoke : 468 -> 464
~ -[BPSFuture startWithSubscriber:] : 96 -> 92
~ -[BPSFuture nextEvent] : 164 -> 160
~ -[BPSFuture completed] : 84 -> 80
~ -[BPSFuture reset] : 84 -> 80
~ -[_BPSInnerFutureConduit requestDemand:] : 452 -> 448
~ -[_BPSInnerFutureConduit fulfill:] : 344 -> 340
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyp_Tg5 : 260 -> 284
```
