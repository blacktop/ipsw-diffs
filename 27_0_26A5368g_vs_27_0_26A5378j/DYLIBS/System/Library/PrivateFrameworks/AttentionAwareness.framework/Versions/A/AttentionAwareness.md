## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/Versions/A/AttentionAwareness`

```diff

-  __TEXT.__text: 0x1f654
+  __TEXT.__text: 0x1f398
   __TEXT.__objc_methlist: 0x188c
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x45c

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__got: 0x130
   __AUTH_CONST.__const: 0xb58
   __AUTH_CONST.__cfstring: 0x1880
   __AUTH_CONST.__objc_const: 0x30c0
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ ___31-[AWScheduler initWithOptions:]_block_invoke : 292 -> 284
~ -[AWScheduler addClient:] : 980 -> 964
~ -[AWScheduler removeInvalidClientsWithConnection:] : 712 -> 700
~ -[AWScheduler armEvents] : 1316 -> 1292
~ -[AWScheduler resetInterruptedStreamingClientWithIdentifier:] : 592 -> 584
~ -[AWScheduler addStreamingClient:withIdentifier:] : 1372 -> 1356
~ -[AWScheduler removeStreamingClientwithIdentifier:] : 1004 -> 988
~ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke : 560 -> 552
~ -[AWScheduler cancelFaceDetectStream:withIdentifier:] : 1556 -> 1532
~ -[AWScheduler setClientAsInterrupted:forKey:] : 632 -> 624
~ -[AWScheduler shouldActivateAttentionDetectionForSampling] : 440 -> 432
~ -[AWScheduler shouldActivateAttentionDetectForStreaming] : 440 -> 432
~ -[AWScheduler shouldActiveRGBFaceDetectForStreaming] : 440 -> 432
~ -[AWScheduler shouldActivateEyeReliefForStreaming] : 440 -> 432
~ -[AWScheduler shouldActivateMotionDetectForSampling] : 440 -> 432
~ ___25-[AWEventStatistics init]_block_invoke : 1052 -> 1044
~ -[AWPersistentDataManager loadPersistentData] : 2304 -> 2288
~ ___45-[AWPersistentDataManager loadPersistentData]_block_invoke : 1012 -> 996
~ -[AWPersistentDataManager openWithConnection:error:] : 664 -> 656
~ -[AWPersistentDataManager closeWithConnection:index:error:] : 568 -> 560
~ __ZN27AttentionServiceEventFilter6filterEPvP14__IOHIDServiceP12__IOHIDEvent : 1440 -> 1432
~ -[AWAttentionAwareService clientCountChangedFrom:to:forScheduler:] : 640 -> 632
~ ___67-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:]_block_invoke : 768 -> 760
~ -[AWRemoteClient initializeClientState] : 880 -> 872
~ ___53-[AWRemoteClient _setClientConfig:shouldReset:error:]_block_invoke : 592 -> 584
~ -[AWRemoteClient reevaluateConfig] : 492 -> 484
~ ___52-[AWRemoteClient setClientConfig:shouldReset:reply:]_block_invoke : 480 -> 472
~ -[AWRemoteClient deliverNotification:] : 528 -> 520
~ -[AWRemoteClient deliverEvent:] : 572 -> 564
~ -[AWRemoteClient deliverPollEventType:event:] : 536 -> 528
~ -[AWRemoteClient updateEventTimesForMask:timestamp:] : 588 -> 580
~ -[AWRemoteClient notifyEvent:timestamp:metadata:] : 1732 -> 1716
~ -[AWRemoteClient _resetAttentionLostTimer] : 544 -> 536
~ ___40-[AWRemoteClient pollWithTimeout:reply:]_block_invoke : 1036 -> 1020
~ -[AWRemoteClient nextAttentionLostTime:] : 928 -> 920
~ -[AWRemoteClient nextSampleTime] : 472 -> 464
~ -[AWRemoteClient shouldInitBeSent] : 508 -> 500
~ -[AWRemoteClient updateDeadlinesForTime:] : 3904 -> 3840
~ -[AWRemoteClient nextTimerForTime:] : 936 -> 920
~ _updateDeadline : 788 -> 772
~ ___32-[AWRemoteClient pingWithReply:]_block_invoke : 336 -> 328
~ ___registerForPrefsChange_block_invoke_2 : 1704 -> 1680
~ ___38-[AWServiceManager invokeWithService:]_block_invoke_2 : 448 -> 440
~ -[AWClientPollWaiter initWithClient:configuration:queue:block:] : 1264 -> 1256
~ ___63-[AWClientPollWaiter initWithClient:configuration:queue:block:]_block_invoke : 320 -> 312
~ ___48-[AWAttentionAwarenessClientConfig updateState:]_block_invoke_2 : 572 -> 564
~ ___43-[AWAttentionAwarenessClientConfig addTag:]_block_invoke : 484 -> 476
~ ___62-[AWAttentionAwarenessClientConfig incrementTagIndexRefCount:]_block_invoke : 732 -> 724
~ ___62-[AWAttentionAwarenessClientConfig decrementTagIndexRefCount:]_block_invoke : 1144 -> 1128
~ -[AWAttentionAwarenessClient notifyStreamingEvent:] : 484 -> 476
~ ___48-[AWAttentionAwarenessClient serviceInterrupted]_block_invoke_3 : 560 -> 552
~ -[AWSampleLogger streamingCompleteWithidentifier:duration:ERActivated:] : 620 -> 612
~ ___37-[AWSampleLogger powerLogName:event:]_block_invoke : 776 -> 760
~ -[AWSampleLogger updateDataForClient:deadline:] : 1016 -> 1008
~ -[AWSampleLogger shouldSample:] : 1652 -> 1628
~ -[AWSampleLogger sampleStartedWithDeadline:] : 764 -> 748
~ -[AWSampleLogger sampleSucceeded] : 572 -> 564
~ +[AWSampleLogger client:attentionStateChange:] : 512 -> 504
~ +[AWSampleLogger client:event:] : 588 -> 580
~ +[AWSampleLogger client:pollEventType:event:] : 596 -> 588
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/Client/ClientHelpers.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/Client/FrameworkClient.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/Client/SimpleFrameworkTypes.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/EventFilter/EventFilter.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/Shared/Utils.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/XPCService/CoreService/AttentionAwareService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/XPCService/CoreService/EventStatistics.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/XPCService/CoreService/PersistentDataManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/XPCService/CoreService/RemoteClient.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/XPCService/CoreService/SampleLogger.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OufbET/Sources/AttentionAwareness/Framework/XPCService/CoreService/Scheduler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/Client/ClientHelpers.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/Client/FrameworkClient.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/Client/SimpleFrameworkTypes.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/EventFilter/EventFilter.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/Shared/Utils.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/XPCService/CoreService/AttentionAwareService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/XPCService/CoreService/EventStatistics.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/XPCService/CoreService/PersistentDataManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/XPCService/CoreService/RemoteClient.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/XPCService/CoreService/SampleLogger.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k71lhv/Sources/AttentionAwareness/Framework/XPCService/CoreService/Scheduler.m"

```
