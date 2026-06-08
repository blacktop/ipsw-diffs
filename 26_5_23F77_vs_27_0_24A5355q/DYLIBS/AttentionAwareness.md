## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-242.100.2.0.0
-  __TEXT.__text: 0x39558
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x274c
-  __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0x844
-  __TEXT.__oslogstring: 0x5646
-  __TEXT.__cstring: 0x3f8a
-  __TEXT.__unwind_info: 0xcb0
-  __TEXT.__objc_classname: 0x5dc
-  __TEXT.__objc_methname: 0x52c0
-  __TEXT.__objc_methtype: 0x191a
-  __TEXT.__objc_stubs: 0x43e0
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0xe70
-  __DATA_CONST.__objc_classlist: 0x118
+261.0.0.0.1
+  __TEXT.__text: 0x37478
+  __TEXT.__objc_methlist: 0x2824
+  __TEXT.__const: 0x200
+  __TEXT.__gcc_except_tab: 0x86c
+  __TEXT.__oslogstring: 0x5834
+  __TEXT.__cstring: 0x4129
+  __TEXT.__unwind_info: 0xd50
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xe48
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1460
+  __DATA_CONST.__objc_selrefs: 0x1448
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x4c8
-  __AUTH_CONST.__const: 0x3c8
-  __AUTH_CONST.__cfstring: 0x1d00
-  __AUTH_CONST.__objc_const: 0x50d0
+  __DATA_CONST.__got: 0x208
+  __AUTH_CONST.__const: 0x428
+  __AUTH_CONST.__cfstring: 0x1d80
+  __AUTH_CONST.__objc_const: 0x52c0
+  __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x54c
-  __DATA.__data: 0xae0
-  __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_data: 0x820
-  __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x138
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x554
+  __DATA.__data: 0xae4
+  __DATA.__bss: 0x98
+  __DATA_DIRTY.__objc_data: 0x870
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B4B55AD9-08D7-3B46-9064-735106CEA300
-  Functions: 954
-  Symbols:   3644
-  CStrings:  2361
+  UUID: B6C4BCC4-20B3-3B8B-89A2-80BC0C32C573
+  Functions: 975
+  Symbols:   3717
+  CStrings:  1090
 
Symbols:
+ +[AWRGBFaceDetectionEvent supportsSecureCoding]
+ +[AWScheduler sharedRGBFaceDetectScheduler]
+ -[AVFoundationEngine registerForOperation:activateRGBFaceDetection:identifier:]
+ -[AVFoundationReceiver activateRGBFaceDetection]
+ -[AVFoundationReceiver initForReceiver:activateRGBFaceDetection:]
+ -[AVFoundationReceiver setActivateRGBFaceDetection:]
+ -[AWAttentionAwareService getRGBFaceDetectScheduler]
+ -[AWAttentionAwareService getSupportedEvents]
+ -[AWAttentionAwarenessConfiguration lenientPollingTimeoutMarginMs]
+ -[AWAttentionAwarenessConfiguration setLenientPollingTimeoutMarginMs:]
+ -[AWAttentionAwarenessConfiguration setUseLenientPollingTimeout:]
+ -[AWAttentionAwarenessConfiguration useLenientPollingTimeout]
+ -[AWAttentionSampler lastDisplayOnTime]
+ -[AWAttentionSampler setLastDisplayOnTime:]
+ -[AWClientPollWaiter initWithClient:configuration:queue:block:]
+ -[AWPollWaiterConfiguration lenientPollingTimeoutMarginMs]
+ -[AWPollWaiterConfiguration setLenientPollingTimeoutMarginMs:]
+ -[AWPollWaiterConfiguration setTimeout:]
+ -[AWPollWaiterConfiguration setUseLenientPollingTimeout:]
+ -[AWPollWaiterConfiguration timeout]
+ -[AWPollWaiterConfiguration useLenientPollingTimeout]
+ -[AWRGBFaceDetectionEvent description]
+ -[AWRGBFaceDetectionEvent encodeWithCoder:]
+ -[AWRGBFaceDetectionEvent faceDetectionScore]
+ -[AWRGBFaceDetectionEvent initWithCoder:]
+ -[AWRGBFaceDetectionEvent initWithTimestamp:tagIndex:faceMetadata:]
+ -[AWRGBFaceDetectionEvent isMetadataValid]
+ -[AWRGBFaceDetectionEvent metadataType]
+ -[AWRGBFaceDetectionEvent validateMask]
+ -[AWScheduler allowRGBFaceDetect]
+ -[AWScheduler shouldActiveRGBFaceDetectForStreaming]
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table168
+ GCC_except_table172
+ GCC_except_table188
+ GCC_except_table207
+ GCC_except_table209
+ GCC_except_table213
+ GCC_except_table234
+ GCC_except_table238
+ GCC_except_table270
+ GCC_except_table294
+ GCC_except_table348
+ GCC_except_table360
+ GCC_except_table379
+ GCC_except_table443
+ GCC_except_table444
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table514
+ GCC_except_table52
+ GCC_except_table520
+ GCC_except_table529
+ GCC_except_table533
+ GCC_except_table54
+ GCC_except_table542
+ GCC_except_table546
+ GCC_except_table56
+ GCC_except_table613
+ GCC_except_table637
+ GCC_except_table714
+ GCC_except_table82
+ GCC_except_table857
+ GCC_except_table883
+ GCC_except_table887
+ GCC_except_table891
+ GCC_except_table894
+ GCC_except_table896
+ GCC_except_table898
+ GCC_except_table899
+ GCC_except_table909
+ GCC_except_table911
+ GCC_except_table916
+ GCC_except_table922
+ GCC_except_table924
+ _AVCaptureDeviceTypeBuiltInUltraWideAngleMetadataCamera
+ _OBJC_CLASS_$_AWPollWaiterConfiguration
+ _OBJC_CLASS_$_AWRGBFaceDetectionEvent
+ _OBJC_IVAR_$_AVFoundationEngine._shouldRunRGBFaceDetection
+ _OBJC_IVAR_$_AVFoundationReceiver._activateRGBFaceDetection
+ _OBJC_IVAR_$_AWAttentionAwareService._listener
+ _OBJC_IVAR_$_AWAttentionAwarenessConfiguration._lenientPollingTimeoutMarginMs
+ _OBJC_IVAR_$_AWAttentionAwarenessConfiguration._useLenientPollingTimeout
+ _OBJC_IVAR_$_AWAttentionSampler._lastDisplayOnTime
+ _OBJC_IVAR_$_AWPollWaiterConfiguration._lenientPollingTimeoutMarginMs
+ _OBJC_IVAR_$_AWPollWaiterConfiguration._timeout
+ _OBJC_IVAR_$_AWPollWaiterConfiguration._useLenientPollingTimeout
+ _OBJC_IVAR_$_AWRGBFaceDetectionEvent._faceDetectionScore
+ _OBJC_IVAR_$_AWRGBFaceDetectionEvent._metadataType
+ _OBJC_IVAR_$_AWRGBFaceDetectionEvent._metadataValid
+ _OBJC_IVAR_$_AWRemoteClient._useLenientPollingTimeout
+ _OBJC_IVAR_$_AWScheduler._allowRGBFaceDetect
+ _OBJC_IVAR_$_AWScheduler._faceDetectMask
+ _OBJC_METACLASS_$_AWPollWaiterConfiguration
+ _OBJC_METACLASS_$_AWRGBFaceDetectionEvent
+ __OBJC_$_CLASS_METHODS_AWRGBFaceDetectionEvent
+ __OBJC_$_CLASS_PROP_LIST_AWRGBFaceDetectionEvent
+ __OBJC_$_INSTANCE_METHODS_AWPollWaiterConfiguration
+ __OBJC_$_INSTANCE_METHODS_AWRGBFaceDetectionEvent
+ __OBJC_$_INSTANCE_VARIABLES_AWPollWaiterConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AWRGBFaceDetectionEvent
+ __OBJC_$_PROP_LIST_AWPollWaiterConfiguration
+ __OBJC_$_PROP_LIST_AWRGBFaceDetectionEvent
+ __OBJC_CLASS_PROTOCOLS_$_AWRGBFaceDetectionEvent
+ __OBJC_CLASS_RO_$_AWPollWaiterConfiguration
+ __OBJC_CLASS_RO_$_AWRGBFaceDetectionEvent
+ __OBJC_METACLASS_RO_$_AWPollWaiterConfiguration
+ __OBJC_METACLASS_RO_$_AWRGBFaceDetectionEvent
+ ___31-[AWScheduler initWithOptions:]_block_invoke.55
+ ___31-[AWScheduler initWithOptions:]_block_invoke.57
+ ___31-[AWScheduler initWithOptions:]_block_invoke.61
+ ___43+[AWScheduler sharedRGBFaceDetectScheduler]_block_invoke
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke.39
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke.41
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_2.40
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_2.42
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_3.43
+ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.76
+ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.80
+ ___50-[AWPearlAttentionStreamer initForUnitTest:queue:]_block_invoke.53
+ ___50-[AWPearlAttentionStreamer initForUnitTest:queue:]_block_invoke_2.54
+ ___52-[AWScheduler shouldActiveRGBFaceDetectForStreaming]_block_invoke
+ ___54-[AVFoundationEngine startOperationForReceiver:reply:]_block_invoke.33
+ ___54-[AVFoundationEngine startOperationForReceiver:reply:]_block_invoke.34
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke.49
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_2.50
+ ___63-[AWClientPollWaiter initWithClient:configuration:queue:block:]_block_invoke
+ ___67-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:]_block_invoke.75
+ ___83-[AWPearlAttentionStreamer streamEventWithBlock:options:operationStartFailedBlock:]_block_invoke.75
+ ___99-[AVFoundationEngine captureOutput:didOutputMetadataObjects:forMetadataObjectTypes:fromConnection:]_block_invoke.45
+ ___Block_byref_object_copy_.1040
+ ___Block_byref_object_copy_.1119
+ ___Block_byref_object_copy_.1632
+ ___Block_byref_object_copy_.2050
+ ___Block_byref_object_copy_.2309
+ ___Block_byref_object_copy_.607
+ ___Block_byref_object_copy_.738
+ ___Block_byref_object_dispose_.1041
+ ___Block_byref_object_dispose_.1120
+ ___Block_byref_object_dispose_.1633
+ ___Block_byref_object_dispose_.2051
+ ___Block_byref_object_dispose_.2310
+ ___Block_byref_object_dispose_.608
+ ___Block_byref_object_dispose_.739
+ ___block_descriptor_48_e8_32s40s_e47_v32?0"NSString"8"AVFoundationReceiver"16^B24ls32l8s40l8
+ ___block_literal_global.100
+ ___block_literal_global.1065
+ ___block_literal_global.1143
+ ___block_literal_global.154
+ ___block_literal_global.1570
+ ___block_literal_global.159
+ ___block_literal_global.1649
+ ___block_literal_global.182
+ ___block_literal_global.2070
+ ___block_literal_global.222
+ ___block_literal_global.23.450
+ ___block_literal_global.2345
+ ___block_literal_global.2422
+ ___block_literal_global.2704
+ ___block_literal_global.28
+ ___block_literal_global.280
+ ___block_literal_global.285
+ ___block_literal_global.296
+ ___block_literal_global.3
+ ___block_literal_global.305
+ ___block_literal_global.318
+ ___block_literal_global.33
+ ___block_literal_global.454
+ ___block_literal_global.57
+ ___block_literal_global.736
+ ___block_literal_global.895
+ ___doesPlatformSupportExclaveHW_block_invoke
+ ___doesPlatformSupportRGBFaceDetect_block_invoke
+ ___isPearlDisabledViaAccessibility_block_invoke.322
+ ___registerForPrefsChange_block_invoke.287
+ ___registerForPrefsChange_block_invoke_2.289
+ _awQueue.onceToken.157
+ _awQueue.queue.156
+ _doesPlatformSupportExclaveHW.onceToken
+ _doesPlatformSupportExclaveHW.value
+ _doesPlatformSupportRGBFaceDetect.answer
+ _doesPlatformSupportRGBFaceDetect.onceToken
+ _getMetadataTypeDescription
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$activateRGBFaceDetection
+ _objc_msgSend$getRGBFaceDetectScheduler
+ _objc_msgSend$getSupportedEvents
+ _objc_msgSend$initForReceiver:activateRGBFaceDetection:
+ _objc_msgSend$initWithClient:configuration:queue:block:
+ _objc_msgSend$lastDisplayOnTime
+ _objc_msgSend$lenientPollingTimeoutMarginMs
+ _objc_msgSend$registerForOperation:activateRGBFaceDetection:identifier:
+ _objc_msgSend$setLastDisplayOnTime:
+ _objc_msgSend$setLenientPollingTimeoutMarginMs:
+ _objc_msgSend$setUseLenientPollingTimeout:
+ _objc_msgSend$sharedRGBFaceDetectScheduler
+ _objc_msgSend$shouldActiveRGBFaceDetectForStreaming
+ _objc_msgSend$useLenientPollingTimeout
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x8
+ _sharedManager.manager.1144
+ _sharedManager.onceToken.1142
+ _sharedRGBFaceDetectScheduler.RGBFaceDetectScheduler
+ _sharedRGBFaceDetectScheduler.onceToken
- -[AVFoundationEngine registerForOperation:activateAttentionDetection:activateEyeRelief:activatePersonDetection:identifier:]
- -[AVFoundationReceiver activateAttentionDetection]
- -[AVFoundationReceiver activateEyeRelief]
- -[AVFoundationReceiver activatePersonDetection]
- -[AVFoundationReceiver initForReceiver:activateAttentionDetection:activateEyeRelief:activatePersonDetection:]
- -[AVFoundationReceiver setActivateAttentionDetection:]
- -[AVFoundationReceiver setActivateEyeRelief:]
- -[AVFoundationReceiver setActivatePersonDetection:]
- -[AWAttentionSampler lastFaceBounds]
- -[AWAttentionSampler lastPersonID]
- -[AWAttentionSampler setLastFaceBounds:]
- -[AWAttentionSampler setLastPersonID:]
- -[AWClientPollWaiter initWithClient:timeout:queue:block:]
- -[AWFaceDetectAttentionEvent faceBounds]
- -[AWFaceDetectAttentionEvent personID]
- GCC_except_table114
- GCC_except_table115
- GCC_except_table162
- GCC_except_table163
- GCC_except_table182
- GCC_except_table201
- GCC_except_table203
- GCC_except_table227
- GCC_except_table231
- GCC_except_table263
- GCC_except_table287
- GCC_except_table344
- GCC_except_table356
- GCC_except_table375
- GCC_except_table433
- GCC_except_table434
- GCC_except_table47
- GCC_except_table49
- GCC_except_table506
- GCC_except_table51
- GCC_except_table512
- GCC_except_table517
- GCC_except_table521
- GCC_except_table53
- GCC_except_table530
- GCC_except_table534
- GCC_except_table605
- GCC_except_table629
- GCC_except_table706
- GCC_except_table79
- GCC_except_table838
- GCC_except_table864
- GCC_except_table868
- GCC_except_table872
- GCC_except_table875
- GCC_except_table877
- GCC_except_table879
- GCC_except_table880
- GCC_except_table890
- GCC_except_table892
- GCC_except_table897
- GCC_except_table903
- GCC_except_table905
- _AVCaptureDeviceTypeBuiltInInfraredMetadataCamera
- _CMTimeMake
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_IVAR_$_AVFoundationEngine._demoMode
- _OBJC_IVAR_$_AVFoundationEngine._shouldRunAttentionDetect
- _OBJC_IVAR_$_AVFoundationEngine._shouldRunEyeRelief
- _OBJC_IVAR_$_AVFoundationEngine._shouldRunPersonDetection
- _OBJC_IVAR_$_AVFoundationEngine._videoDataOutput
- _OBJC_IVAR_$_AVFoundationOperation._demoMode
- _OBJC_IVAR_$_AVFoundationReceiver._activateAttentionDetection
- _OBJC_IVAR_$_AVFoundationReceiver._activateEyeRelief
- _OBJC_IVAR_$_AVFoundationReceiver._activatePersonDetection
- _OBJC_IVAR_$_AWAttentionSampler._lastFaceBounds
- _OBJC_IVAR_$_AWAttentionSampler._lastPersonID
- _OBJC_IVAR_$_AWFaceDetectAttentionEvent._faceBounds
- _OBJC_IVAR_$_AWFaceDetectAttentionEvent._personID
- ___31-[AWScheduler initWithOptions:]_block_invoke.47
- ___31-[AWScheduler initWithOptions:]_block_invoke.49
- ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke.63
- ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke.65
- ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_2.64
- ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_2.66
- ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_3.67
- ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.67
- ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.70
- ___50-[AWPearlAttentionStreamer initForUnitTest:queue:]_block_invoke.11
- ___50-[AWPearlAttentionStreamer initForUnitTest:queue:]_block_invoke.15
- ___50-[AWPearlAttentionStreamer initForUnitTest:queue:]_block_invoke_2.12
- ___54-[AVFoundationEngine startOperationForReceiver:reply:]_block_invoke.54
- ___54-[AVFoundationEngine startOperationForReceiver:reply:]_block_invoke_2.58
- ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke.7
- ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_2.8
- ___57-[AWClientPollWaiter initWithClient:timeout:queue:block:]_block_invoke
- ___67-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:]_block_invoke.69
- ___83-[AWPearlAttentionStreamer streamEventWithBlock:options:operationStartFailedBlock:]_block_invoke.34
- ___99-[AVFoundationEngine captureOutput:didOutputMetadataObjects:forMetadataObjectTypes:fromConnection:]_block_invoke.68
- ___Block_byref_object_copy_.1041
- ___Block_byref_object_copy_.1141
- ___Block_byref_object_copy_.1652
- ___Block_byref_object_copy_.2076
- ___Block_byref_object_copy_.2338
- ___Block_byref_object_copy_.590
- ___Block_byref_object_copy_.723
- ___Block_byref_object_dispose_.1042
- ___Block_byref_object_dispose_.1142
- ___Block_byref_object_dispose_.1653
- ___Block_byref_object_dispose_.2077
- ___Block_byref_object_dispose_.2339
- ___Block_byref_object_dispose_.591
- ___Block_byref_object_dispose_.724
- ___block_descriptor_56_e8_32s40r48r_e15_v32?0816^B24lr40l8s32l8r48l8
- ___block_descriptor_88_e8_32s40bs48r56r64r72r80r_e5_v8?0lr48l8s32l8r56l8r64l8r72l8r80l8s40l8
- ___block_literal_global.1080
- ___block_literal_global.1164
- ___block_literal_global.151
- ___block_literal_global.156
- ___block_literal_global.1590
- ___block_literal_global.1668
- ___block_literal_global.183
- ___block_literal_global.20
- ___block_literal_global.2096
- ___block_literal_global.220
- ___block_literal_global.2370
- ___block_literal_global.25
- ___block_literal_global.2739
- ___block_literal_global.277
- ___block_literal_global.282
- ___block_literal_global.294
- ___block_literal_global.302
- ___block_literal_global.312
- ___block_literal_global.457
- ___block_literal_global.58
- ___block_literal_global.721
- ___block_literal_global.77
- ___block_literal_global.877
- ___isPearlDisabledViaAccessibility_block_invoke.319
- ___registerForPrefsChange_block_invoke.284
- ___registerForPrefsChange_block_invoke_2.287
- _awQueue.onceToken.154
- _awQueue.queue.153
- _objc_msgSend$boolForKey:
- _objc_msgSend$getStreamerOptionsWithMask:
- _objc_msgSend$initForReceiver:activateAttentionDetection:activateEyeRelief:activatePersonDetection:
- _objc_msgSend$initWithClient:timeout:queue:block:
- _objc_msgSend$initWithSuiteName:
- _objc_msgSend$isAttentionDetectionSupported
- _objc_msgSend$lastFaceBounds
- _objc_msgSend$lastPersonID
- _objc_msgSend$lockForConfiguration:
- _objc_msgSend$registerForOperation:activateAttentionDetection:activateEyeRelief:activatePersonDetection:identifier:
- _objc_msgSend$setActiveVideoMaxFrameDuration:
- _objc_msgSend$setActiveVideoMinFrameDuration:
- _objc_msgSend$setAttentionDetectionEnabled:
- _objc_msgSend$setLastFaceBounds:
- _objc_msgSend$setLastPersonID:
- _objc_msgSend$unlockForConfiguration
- _sharedManager.manager.1165
- _sharedManager.onceToken.1163
CStrings:
+ "%13.5f: AD metadata received on a AWRGBFaceDetectionEvent class, not passing it to client %@"
+ "%13.5f: Attention detection session started ER %s, AD/FD %s"
+ "%13.5f: BiometricKit timeout detected for lenient polling client %@"
+ "%13.5f: Combined metadata received on a AWRGBFaceDetectionEvent class, not passing it to client %@"
+ "%13.5f: Device doesn't support pearl/RGB face detect"
+ "%13.5f: ER metadata received on a AWRGBFaceDetectionEvent class, not passing it to client %@"
+ "%13.5f: IR and RGB face detect cannot be started in parallel, only starting IR face detect"
+ "%13.5f: Lenient polling: client fallback timer %13.5f (original %13.5f + %13.5f margin)"
+ "%13.5f: MD metadata received on a AWRGBFaceDetectionEvent class, not passing it to client %@"
+ "%13.5f: No clients are requesting RGB face detect, abort"
+ "%13.5f: RGB face detect can only be run in streaming mode"
+ "%13.5f: RGB metadata received on a AWFaceDetectAttentionEvent class, not passing it to client %@"
+ "%13.5f: Timeout: %f AWAttentionSamplerActivateAttentionDetection: %s"
+ "%13.5f: Using AVFoundation for RGB Face detect operations"
+ "%13.5f: cancelling polling for client %@"
+ "%13.5f: sysctlbyname(kern.exclaves_status): %s"
+ "%30s:%-4d: %13.5f: %@ faceDetectStateChanged %s pitch: %13.5f yaw: %13.5f roll: %13.5f orientation: %@ distance: %13.5f faceDetectionScore: %f"
+ "%30s:%-4d: %13.5f: %d active RGB Face detect clients"
+ "%30s:%-4d: %13.5f: Attention detection session started ER %s, AD/FD %s"
+ "%30s:%-4d: %13.5f: BiometricKit timeout detected for lenient polling client %@"
+ "%30s:%-4d: %13.5f: Client side timer fired for poll timeout"
+ "%30s:%-4d: %13.5f: Lenient polling: client fallback timer %13.5f (original %13.5f + %13.5f margin)"
+ "%30s:%-4d: %13.5f: Timeout: %f AWAttentionSamplerActivateAttentionDetection: %s"
+ "%30s:%-4d: %13.5f: Using AVFoundation for RGB Face detect operations"
+ "%30s:%-4d: %13.5f: cancelling polling for client %@"
+ "-[AWRGBFaceDetectionEvent validateMask]"
+ "<%@: %p> (identifier: %@ samplingInterval: %13.5f samplingDelay: %13.5f sampleWhileAbsent: %s retroactiveTimeoutMode: %s pollingFilter: %s continuousFaceDetectMode: %s unityStream: %s useLenientPollingTimeout: %s activateEyeRelief: %s activateAttentionDetection: %s activateMotionDetection: %s attentionLostTimeouts: %@ nonSampledAttentionLostTimeoutEnabled %s nonSampledAttentionLostTimeout %13.5f notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ tagIndex %llu)"
+ "<%@: %p> (identifier: %@ samplingInterval: %13.5f, samplingDelay: %13.5f, sampleWhileAbsent: %s, retroactiveTimeoutMode: %s, pollingFilter: %s, continuousFaceDetectMode: %s, activateAttentionDetection: %s, activateEyeRelief: %s, activateMotionDetection: %s, unityStream: %s, useLenientPollingTimeout: %s, lenientPollingTimeoutMarginMs: %llu, attentionLostTimeouts: %@ nonSampledAttentionLostTimeoutEnable: %s nonSampledAttentionLostTimeout: %13.5f notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ %@)"
+ "<%@: %p> (timestamp: %13.5f metadataValid %u metadataType: %@ faceDetectionScore: %13.5f %@)"
+ "DeviceSupportsAutoDim"
+ "RGB"
+ "RGB scheduler"
+ "RGBFaceDetect|"
+ "allowRGBFaceDetect"
+ "kern.exclaves_status"
+ "lenientPollingTimeoutMarginMs"
+ "self.eventMask == AWAttentionEventMaskRGBFaceDetect"
+ "useLenientPollingTimeout"
+ "v32@?0@\"NSString\"8@\"AVFoundationReceiver\"16^B24"
+ "\xb1"
- "\t"
- " Client already started an operation with the same options"
- "#16@0:8"
- "%13.5f: Attention detection session started ER %s, AD/FD %s PD %s"
- "%13.5f: Cancelling current stream and starting a new one as stream options have changed"
- "%13.5f: Could not lock configuration for device %@ error: %@"
- "%13.5f: Device doesn't support pearl"
- "%13.5f: Options have changed, restarting AVFCapture session with new options"
- "%13.5f: Streaming options have changed, cancelling current operation and starting a new one with updated options"
- "%13.5f: Timeout: %f AWAttentionSamplerActivateAttentionDetection: %s AWAttentionSamplerActivatePersonDetection: %s"
- "%13.5f: cancelling polling for client %@ with"
- "%30s:%-4d: %13.5f: %@ faceDetectStateChanged %s pitch: %13.5f yaw: %13.5f roll: %13.5f orientation: %@ distance: %13.5f eyeReliefFaceState:%@ faceDetectionScore: %f"
- "%30s:%-4d: %13.5f: Attention detection session started ER %s, AD/FD %s PD %s"
- "%30s:%-4d: %13.5f: Cancelling current stream and starting a new one as stream options have changed"
- "%30s:%-4d: %13.5f: Options have changed, restarting AVFCapture session with new options"
- "%30s:%-4d: %13.5f: Streaming options have changed, cancelling current operation and starting a new one with updated options"
- "%30s:%-4d: %13.5f: Timeout: %f AWAttentionSamplerActivateAttentionDetection: %s AWAttentionSamplerActivatePersonDetection: %s"
- "%30s:%-4d: %13.5f: cancelling polling for client %@ with"
- ".cxx_destruct"
- "<%@: %p> (identifier: %@ samplingInterval: %13.5f samplingDelay: %13.5f sampleWhileAbsent: %s retroactiveTimeoutMode: %s pollingFilter: %s continuousFaceDetectMode: %s unityStream: %s activateEyeRelief: %s activateAttentionDetection: %s activateMotionDetection: %s activatePersonDetection: %s attentionLostTimeouts: %@ nonSampledAttentionLostTimeoutEnabled %s nonSampledAttentionLostTimeout %13.5f notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ tagIndex %llu)"
- "<%@: %p> (identifier: %@ samplingInterval: %13.5f, samplingDelay: %13.5f, sampleWhileAbsent: %s, retroactiveTimeoutMode: %s, pollingFilter: %s, continuousFaceDetectMode: %s, activateAttentionDetection: %s, activateEyeRelief: %s, activateMotionDetection: %s, unityStream: %s, attentionLostTimeouts: %@ nonSampledAttentionLostTimeoutEnable: %s nonSampledAttentionLostTimeout: %13.5f notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ %@)"
- "@"
- "@\"<AVFoundationReceiving>\""
- "@\"<AVFoundationUnitTestEventReceiving>\""
- "@\"<AVFoundationUnitTestStreamerCreating>\""
- "@\"<AVFoundationUnitTestStreamerCreating>\"16@0:8"
- "@\"<AWFrameworkClient>\""
- "@\"<AWSchedulerObserver>\""
- "@\"<AWUnitTestSampler>\""
- "@\"<AWUnitTestSampler>\"16@0:8"
- "@\"<BKDevicePearlDelegate>\""
- "@\"<CarPlayStateObserving>\""
- "@\"<LockScreenStateObserving>\""
- "@\"<MotionActivityObserving>\""
- "@\"<NSCopying>\""
- "@\"<NSXPCProxyCreating>\""
- "@\"<PearlCameraInterfaceMessaging>\""
- "@\"<SamplingOperation>\""
- "@\"<ScreenStateObserving>\""
- "@\"<StreamingOperation>\""
- "@\"AVCaptureDevice\""
- "@\"AVCaptureDeviceInput\""
- "@\"AVCaptureMetadataOutput\""
- "@\"AVCaptureSession\""
- "@\"AVCaptureVideoDataOutput\""
- "@\"AVFoundationEngine\""
- "@\"AVFoundationUnitTestSession\""
- "@\"AWAttentionAwarenessClient\""
- "@\"AWAttentionAwarenessConfiguration\""
- "@\"AWAttentionEvent\""
- "@\"AWAttentionSampler\""
- "@\"AWAttentionStreamer\""
- "@\"AWClientPollWaiter\""
- "@\"AWSampleLogger\""
- "@\"AWScheduler\""
- "@\"AWUnitTestFaceDetectOperation\""
- "@\"AWUnitTestPearlDevice\""
- "@\"BKDevicePearl\""
- "@\"BKFaceDetectOperation\""
- "@\"BMBiomeScheduler\""
- "@\"BMStream\""
- "@\"BPSSink\""
- "@\"CMMotionActivityManager\""
- "@\"CarPlayStateObserver\""
- "@\"LockScreenStateObserver\""
- "@\"MotionActivityObserver\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\"16@0:8"
- "@\"NSError\"24@0:8@\"NSString\"16"
- "@\"NSError\"27@0:8d16{?=BBB}24"
- "@\"NSError\"35@0:8@?<v@?@\"AWAttentionEvent\">16{?=BBB}24@?<v@?@\"NSError\">27"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNotificationCenter\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSOperationQueue\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"ScreenStateObserver\""
- "@16@0:8"
- "@19@0:8{?=BBB}16"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@27@0:8d16{?=BBB}24"
- "@28@0:8@16B24"
- "@28@0:8B16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@35@0:8@?16{?=BBB}24@?27"
- "@36@0:8@16B24B28B32"
- "@40@0:8:16@24@32"
- "@40@0:8d16Q24Q32"
- "@40@0:8d16Q24^{AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}32"
- "@40@0:8d16Q24^{AWRemoteMetadata=qqQB}32"
- "@40@0:8d16Q24d32"
- "@43@0:8Q16@?24{?=BBB}32@?35"
- "@48@0:8@16Q24@32@?40"
- "@48@0:8d16Q24Q32^{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}}40"
- "@68@0:8@16@24@32i40@44@52^@60"
- "@?"
- "@?16@0:8"
- "AA - Received frame of EyeRelief data"
- "AVCaptureMetadataOutputObjectsDelegate"
- "AVCaptureMetadataOutputObjectsDelegatePrivate"
- "AVFoundationDeliverStreamingEvent"
- "AVFoundationEngine"
- "AVFoundationOperation"
- "AVFoundationReceiver"
- "AVFoundationReceiving"
- "AVFoundationSession"
- "AVFoundationUnitTestEventReceiving"
- "AVFoundationUnitTestSession"
- "AVFoundationUnitTestStreamerCreating"
- "AWAVFoundationAttentionStreamer"
- "AWAttentionAwareService"
- "AWAttentionAwarenessClient"
- "AWAttentionAwarenessClientConfig"
- "AWAttentionAwarenessConfiguration"
- "AWAttentionEvent"
- "AWAttentionLostEvent"
- "AWAttentionSampler"
- "AWAttentionStreamer"
- "AWClientPollWaiter"
- "AWClientPreferences"
- "AWDigitizerButtonKeyboardAttentionEvent"
- "AWEventStatistics"
- "AWFaceDetectAttentionEvent"
- "AWFrameworkClient"
- "AWPearlAttentionSampler"
- "AWPearlAttentionStreamer"
- "AWPersistentDataExists:"
- "AWPersistentDataManager"
- "AWRemoteAttentionEvent"
- "AWRemoteClient"
- "AWSampleLogData"
- "AWSampleLogger"
- "AWScheduler"
- "AWSchedulerObserver"
- "AWServiceManager"
- "AWServiceObserver"
- "AWUnitTestFaceDetectOperation"
- "AWUnitTestPearlDevice"
- "AWUnitTestSampler"
- "B"
- "B16@0:8"
- "B19@0:8{?=BBB}16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B24@0:8^i16"
- "B24@0:8^{?=QQQQ[0{?={?=dQQQQQQQBBBB}Qii}]}16"
- "B24@0:8d16"
- "B27@0:8@\"NSObject<OS_dispatch_queue>\"16{?=BBB}24"
- "B27@0:8@16{?=BBB}24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8^i16^@24"
- "B36@0:8@16B24^@28"
- "B36@0:8@16i24^@28"
- "B36@0:8B16^@20@?28"
- "B40@0:8d16^@24^@32"
- "B44@0:8@16B24B28B32@36"
- "B48@0:8d16@24@?32^@40"
- "B56@0:8^{__IOHIDEvent=}16Q24^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32^{__IOHIDService=}40@48"
- "BKDeviceDelegate"
- "BKDevicePearlDelegate"
- "BKFaceDetectOperationDelegate"
- "BKFaceDetectStateInfoCategory"
- "BKOperationDelegate"
- "BLSBacklightStateObserving"
- "BiokitOperation"
- "CARSessionObserving"
- "CarPlay"
- "CarPlayStateObserver"
- "CarPlayStateObserving"
- "Connected"
- "Could not lock device configuration to set frame rate"
- "DSLPublisher"
- "LockScreenStateChanging:"
- "LockScreenStateObserver"
- "LockScreenStateObserving"
- "MotionActivityObserver"
- "MotionActivityObserving"
- "MotionStateChanging:"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "PD"
- "PearlCameraInterfaceMessaging"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8Q16"
- "Q24@0:8^B16"
- "Q28@0:8Q16B24"
- "SamplingOperation"
- "ScreenStateObserver"
- "ScreenStateObserving"
- "SessionDidStartRunningNotification:"
- "SessionDidStopRunningNotification:"
- "SessionInterruptionEndedNotification:"
- "SessionRuntimeErrorNotification:"
- "SessionWasInterruptedNotification:"
- "State"
- "StreamingOperation"
- "T#,R"
- "T@\"<AVFoundationReceiving>\",&,N,V_receiver"
- "T@\"<AWSchedulerObserver>\",W,N,V_observer"
- "T@\"<BKDevicePearlDelegate>\",W,N,V_delegate"
- "T@\"<NSCopying>\",C,N,V_tag"
- "T@\"AWAttentionAwarenessConfiguration\",C,N"
- "T@\"AWAttentionEvent\",R,&,N"
- "T@\"AWAttentionSampler\",R,N,V_attentionSampler"
- "T@\"AWSampleLogger\",&,N,V_sampleLogger"
- "T@\"AWUnitTestPearlDevice\",W,N,V_unitTestDevice"
- "T@\"NSArray\",R,N,V_motionData"
- "T@\"NSDictionary\",C,N"
- "T@\"NSMutableArray\",&,N,V_lastMotionData"
- "T@\"NSNumber\",&,D,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSSet\",C,D,N"
- "T@\"NSSet\",C,N,V_buttonDisplayUUIDs"
- "T@\"NSSet\",C,N,V_digitizerDisplayUUIDs"
- "T@\"NSSet\",C,N,V_keyboardDisplayUUIDs"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_displayUUID"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSUUID\",R,N,V_clientId"
- "T@,R,N,V_associatedObject"
- "T@,R,N,V_tag"
- "T@?,C,V_operationEndableCallback"
- "T@?,C,V_stateChangedCallback"
- "TB,N,V_activateAttentionDetection"
- "TB,N,V_activateEyeRelief"
- "TB,N,V_activateMotionDetect"
- "TB,N,V_activatePersonDetection"
- "TB,N,V_continuousFaceDetectMode"
- "TB,N,V_lastFaceMetadataValid"
- "TB,N,V_nonSampledAttentionLostTimeoutEnable"
- "TB,N,V_pollingClient"
- "TB,N,V_pollingFilter"
- "TB,N,V_retroactiveTimeoutMode"
- "TB,N,V_running"
- "TB,N,V_sampleSucceeded"
- "TB,N,V_sampleWhileAbsent"
- "TB,N,V_unityStream"
- "TB,R"
- "TB,R,N,GisMetadataValid,V_metadataValid"
- "TB,R,N,V_activateAttentionDetection"
- "TB,R,N,V_activateEyeRelief"
- "TB,R,N,V_activateMotionDetect"
- "TB,R,N,V_allowFaceDetect"
- "TB,R,N,V_allowHIDEvents"
- "TB,R,N,V_allowMotionDetect"
- "TB,R,N,V_buttonPressed"
- "TB,R,N,V_invalid"
- "TB,R,N,V_isDeviceOnLockScreen"
- "TB,R,N,V_isDeviceStationary"
- "TB,R,N,V_unitTestMode"
- "TB,R,N,V_unitTestSampling"
- "TB,V_facePresent"
- "TB,V_pearlError"
- "TQ,D,N"
- "TQ,N,V_attentionLostEventMask"
- "TQ,N,V_cumulativeSamplingTime"
- "TQ,N,V_eventMask"
- "TQ,N,V_lastFaceState"
- "TQ,N,V_lastMetadataType"
- "TQ,N,V_lastMotionResult"
- "TQ,N,V_lastOrientation"
- "TQ,N,V_lastPersonID"
- "TQ,N,V_lastPollTimeoutTime"
- "TQ,N,V_lastPositiveDetectTime"
- "TQ,N,V_lastTriggerTime"
- "TQ,N,V_notificationMask"
- "TQ,N,V_samplingInterval"
- "TQ,N,V_samplingStartTime"
- "TQ,N,V_samplingSuppressedMask"
- "TQ,N,V_streamingStartTime"
- "TQ,R"
- "TQ,R,N,V_eventMask"
- "TQ,R,N,V_faceState"
- "TQ,R,N,V_metadataType"
- "TQ,R,N,V_motionResult"
- "TQ,R,N,V_orientation"
- "TQ,R,N,V_personID"
- "TQ,R,N,V_samplingDelay"
- "TQ,R,N,V_samplingInterval"
- "TQ,R,N,V_senderID"
- "TQ,V_clientCount"
- "T^{?=QQQ},V_sampleStatsPtr"
- "Td,N,V_lastDistance"
- "Td,N,V_lastPitch"
- "Td,N,V_lastRoll"
- "Td,N,V_lastYaw"
- "Td,N,V_nonSampledAttentionLostTimeout"
- "Td,N,V_samplingDelay"
- "Td,N,V_samplingInterval"
- "Td,N,V_streamingDuration"
- "Td,R,N,V_attentionLostTimeout"
- "Td,R,N,V_distance"
- "Td,R,N,V_pitch"
- "Td,R,N,V_roll"
- "Td,R,N,V_timestamp"
- "Td,R,N,V_yaw"
- "Tf,N,V_lastFaceDetectionScore"
- "Tf,R,N,V_faceDetectionScore"
- "Ti,N,V_currentState"
- "Ti,R,N,V_clientIndex"
- "Tq,R,N,V_usage"
- "Tq,R,N,V_usagePage"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_lastFaceBounds"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_faceBounds"
- "UTF8String"
- "UUID"
- "Vv16@0:8"
- "^v"
- "^{?=QQQ}"
- "^{?=QQQ}16@0:8"
- "^{?=dQQQQQQQBBBB}"
- "^{?=dQQQQQQQBBBB}36@0:8@16i24^@28"
- "^{AWNotification_s=}32@0:8@16@?24"
- "^{_NSZone=}16@0:8"
- "_AVFoundationEngine"
- "_AVFoundationSession"
- "_activateAttentionDetection"
- "_activateEyeRelief"
- "_activateMotionDetect"
- "_activatePersonDetection"
- "_activeEventMask"
- "_activeOperationNotification"
- "_addedClientLogData"
- "_allowFaceDetect"
- "_allowHIDEvents"
- "_allowMotionDetect"
- "_allowedHIDEventsForRemoteEvent"
- "_associatedObject"
- "_attentionAwareFeaturesEnabledNotification"
- "_attentionLostEventMask"
- "_attentionLostEventMaskExplicitlySet"
- "_attentionLostTimeout"
- "_attentionLostTimeoutDictionary"
- "_attentionLostTimeouts"
- "_attentionLostTimeoutsSec"
- "_attentionSampler"
- "_attentionStreamer"
- "_attentionStreamerRunning"
- "_awInitTimer"
- "_awQueue"
- "_buttonDisplayUUIDs"
- "_buttonPressed"
- "_callbackBlock"
- "_callbackQueue"
- "_carPlayConnected"
- "_carPlayStateObserver"
- "_carplayCallbacks"
- "_client"
- "_clientBlock"
- "_clientCount"
- "_clientEventBlock"
- "_clientEventQueue"
- "_clientId"
- "_clientIndex"
- "_clientLogData"
- "_clientNotifBlock"
- "_clientNotifQueue"
- "_clientQueue"
- "_clientStreamingBlock"
- "_clientStreamingQueue"
- "_clients"
- "_configuration"
- "_connect"
- "_connection"
- "_continuousFaceDetectMode"
- "_createUnitTestScheduler"
- "_cumulativeSamplingTime"
- "_currentOperation"
- "_currentOptions"
- "_currentState"
- "_deadlineTimer"
- "_delegate"
- "_demoMode"
- "_device"
- "_deviceEvent"
- "_digitizerDisplayUUIDs"
- "_displayCallbacks"
- "_displayNotifyToken"
- "_displayOn"
- "_displayState"
- "_displayUUID"
- "_distance"
- "_enrollOrMatchOperationUnderway"
- "_errorState"
- "_eventDelivered"
- "_eventDeliveryQueue"
- "_eventMask"
- "_eyeReliefStarted"
- "_faceBounds"
- "_faceDetectStreamer"
- "_faceDetectionScore"
- "_faceFound"
- "_facePresent"
- "_faceState"
- "_filteredPollingEventDelivered"
- "_finished"
- "_finishingOperation"
- "_finishingPresenceOperation"
- "_getQueue"
- "_identifier"
- "_input"
- "_interestedInHIDEvent:mask:metadata:senderID:displayUUID:"
- "_interruptedStreamingClients"
- "_invalid"
- "_invalidated"
- "_invokeRequiringClient:error:block:"
- "_isAttentionAwareFeaturesEnabled"
- "_isDeviceOnLockScreen"
- "_isDeviceStationary"
- "_isSamplingClient"
- "_keyboardDisplayUUIDs"
- "_lastAttentionState"
- "_lastConfig"
- "_lastDistance"
- "_lastErrorTime"
- "_lastEvent"
- "_lastFaceBounds"
- "_lastFaceDetectionScore"
- "_lastFaceMetadataValid"
- "_lastFaceState"
- "_lastLogDate"
- "_lastLogTime"
- "_lastMetadataType"
- "_lastMotionData"
- "_lastMotionResult"
- "_lastOperation"
- "_lastOrientation"
- "_lastPersonID"
- "_lastPitch"
- "_lastPollTimeoutTime"
- "_lastPositiveDetectTime"
- "_lastRoll"
- "_lastTriggerTime"
- "_lastYaw"
- "_loadAbsTime"
- "_lockScreenStateObserver"
- "_lockToken"
- "_logFeatureEnablement"
- "_matchOrEnrollOperationActive"
- "_metadataOutput"
- "_metadataType"
- "_metadataValid"
- "_motionActivityManager"
- "_motionActivityObserver"
- "_motionData"
- "_motionResult"
- "_nextDeadline"
- "_nextTagIndex"
- "_nonSampledAttentionLostTimeout"
- "_nonSampledAttentionLostTimeoutEnable"
- "_nonSampledAttentionTimer"
- "_nonSampledAttentionTimerResumed"
- "_notificationBlock"
- "_notificationCenter"
- "_notificationMask"
- "_notifyBlocks"
- "_notifyQueues"
- "_notifyToken"
- "_observer"
- "_operationCreateTime"
- "_operationEndableCallback"
- "_operationQueue"
- "_operationStalledTimer"
- "_operationState"
- "_orientation"
- "_outputPowerLog"
- "_outstandingClientLogData"
- "_pearlDevice"
- "_pearlError"
- "_pendingPresenceOperation"
- "_personID"
- "_pitch"
- "_pollState"
- "_pollWaiter"
- "_pollingClient"
- "_pollingFilter"
- "_pollsRequested"
- "_powerLogQueue"
- "_proxy"
- "_queue"
- "_receiver"
- "_receivers"
- "_remoteClientProxy"
- "_remoteSamplerProxy"
- "_resetAttentionLostTimer"
- "_retroactiveTimeoutMode"
- "_roll"
- "_running"
- "_sampleLogger"
- "_sampleStats"
- "_sampleStatsPtr"
- "_sampleSucceeded"
- "_sampleWhileAbsent"
- "_samplesRequested"
- "_samplesSucceeded"
- "_samplingDelay"
- "_samplingDelayExplicitlySet"
- "_samplingInterval"
- "_samplingStartTime"
- "_samplingSuppressedMask"
- "_scheduler"
- "_schedulers"
- "_screenStateObserver"
- "_senderID"
- "_serviceObservers"
- "_session"
- "_sessionQueue"
- "_sessionRunning"
- "_setClientConfig:shouldReset:error:"
- "_shm_obj"
- "_shouldRunAttentionDetect"
- "_shouldRunEyeRelief"
- "_shouldRunPersonDetection"
- "_signpostLogged"
- "_sink"
- "_smarCoverCallbacks"
- "_smartCoverClosed"
- "_spoofedNotification"
- "_startSession"
- "_started"
- "_stateChangedCallback"
- "_stats"
- "_stopSession"
- "_stream"
- "_streamingClients"
- "_streamingDuration"
- "_streamingStartTime"
- "_streamingTimer"
- "_supportedEvents"
- "_supportedEventsNotify"
- "_supportedEventsValid"
- "_suspensionCount"
- "_tag"
- "_tagIndex"
- "_tagMap"
- "_tagRefCount"
- "_timebase"
- "_timeout"
- "_timer"
- "_timerResumed"
- "_timestamp"
- "_transaction"
- "_unitTest"
- "_unitTestController"
- "_unitTestDevice"
- "_unitTestMode"
- "_unitTestOperation"
- "_unitTestSampling"
- "_unitTester"
- "_unityStream"
- "_usage"
- "_usagePage"
- "_useAVFoundation"
- "_videoDataOutput"
- "_yaw"
- "activatePersonDetection"
- "addClient:"
- "addClient:clientConfig:clientIndex:clientId:unitTestMode:reply:subscribeForStreamingEvents:"
- "addInput:"
- "addObject:"
- "addObserver:"
- "addObserverForName:object:queue:usingBlock:"
- "addOutput:"
- "addStreamingClient:withIdentifier:"
- "addTag:"
- "allKeys"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "appendFormat:"
- "appendString:"
- "armEvents"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "associatedObject"
- "attentionLostTimeoutDictionary"
- "attentionSampler"
- "attentionStreamerRunning"
- "auditToken"
- "autorelease"
- "availableDevices"
- "awDeliverFaceFound"
- "awDeliverStreamingEvent"
- "awFinishWithReason:"
- "awSetFaceDetectError:"
- "awSetFaceFound"
- "backlight:activatingWithEvent:"
- "backlight:deactivatingWithEvent:"
- "backlight:didChangeAlwaysOnEnabled:"
- "backlight:didCompleteUpdateToState:forEvent:"
- "backlight:didCompleteUpdateToState:forEvents:abortedEvents:"
- "backlight:performingEvent:"
- "boolForKey:"
- "boolValue"
- "calculateTimeDelta:endTime:timebase:"
- "cameraActivityNotification:data:forOperation:"
- "canActiveOperationBeEnded"
- "canAddInput:"
- "canAddOutput:"
- "canDeliverPollingEvent"
- "canOperationBeEndedForClient"
- "canRunMotionDetect"
- "cancel"
- "cancelActiveOperation:"
- "cancelEventStream"
- "cancelEventStreamWithMask:"
- "cancelFaceDetect:"
- "cancelFaceDetectStream:withIdentifier:"
- "cancelFaceDetectStreamWithError:"
- "cancelFaceDetectStreamWithReply:"
- "cancelNotification:"
- "cancelPollForAttentionWithError:"
- "cancelStalledTimer"
- "cancelUnitTestStream"
- "cancelledConnectionAttemptOnTransport:"
- "captureOutput:didOutputMetadataObjects:forMetadataObjectTypes:fromConnection:"
- "captureOutput:didOutputMetadataObjects:fromConnection:"
- "carPlayStateChanging:"
- "checkIfOptionsHaveChanged:"
- "checkIfTimeoutHasChanged:"
- "checkPreconditions:"
- "class"
- "client:attentionStateChange:"
- "client:event:"
- "client:pollEventType:event:"
- "clientCount"
- "clientCountChangedFrom:to:forScheduler:"
- "clientId"
- "clientIndex"
- "clientStateWithConnection:index:error:"
- "closeWithConnection:index:error:"
- "code"
- "compare:"
- "componentsJoinedByString:"
- "confidence"
- "configuration"
- "conformsToProtocol:"
- "connect"
- "connect:"
- "connection"
- "containsObject:"
- "containsValueForKey:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "crashWithReply:"
- "createAVFoundationOperation"
- "createNewSamplingOperation"
- "createPresenceDetectOperationWithError:"
- "createPresenceDetectOperationWithTimeout:options:"
- "cumulativeSamplingTime"
- "currentConnection"
- "currentState"
- "d"
- "d16@0:8"
- "d40@0:8Q16Q24{mach_timebase_info=II}32"
- "date"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decrementTagIndexRefCount:"
- "defaultCenter"
- "delegate"
- "deleteCharactersInRange:"
- "deliverEvent:"
- "deliverNotification:"
- "deliverPearlDeviceEvent:"
- "deliverPearlDeviceState:"
- "deliverPollEventType:event:"
- "demoMode"
- "describeMotionData:"
- "device:matchEventOccurred:"
- "device:pearlEventOccurred:"
- "device:pearlStateChanged:"
- "deviceWithDescriptor:error:"
- "devices"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "discoverySessionWithDeviceTypes:mediaType:position:"
- "domain"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "eventBody"
- "eyeRelief"
- "eyeReliefStatus"
- "f"
- "f16@0:8"
- "faceBounds"
- "faceDetectStalled:"
- "faceDetected"
- "facePresent"
- "fakeDataForDemoMode"
- "finishDeadlineComputationWithOptions:"
- "finishingFaceDetect:"
- "firstObject"
- "floatValue"
- "getDebugPreferences:"
- "getEventMaskDescription:"
- "getFaceDetectScheduler"
- "getLastEvent:"
- "getMotionDetectScheduler"
- "getStatsWithBlock:"
- "getStreamerOptions"
- "getStreamerOptionsWithMask:"
- "getStreamingSessionAndStartRunning:"
- "getSupportedEventsWithReply:"
- "getUnitTestSamplerWithReply:"
- "handleNotification:"
- "handleNotification:notification:"
- "hasConfidence"
- "hasDistance"
- "hasOrientation"
- "hasPayingAttention"
- "hasPitchAngle"
- "hasRollAngle"
- "hasYawAngle"
- "hash"
- "i16@0:8"
- "i32@0:8@16^@24"
- "incrementTagIndexRefCount:"
- "init"
- "initAWPersistentDataHeader:"
- "initForReceiver:activateAttentionDetection:activateEyeRelief:activatePersonDetection:"
- "initForUnitTest:queue:"
- "initForUnitTest:useAVFoundation:"
- "initWithCallbackQueue:observer:"
- "initWithClient:timeout:queue:block:"
- "initWithCoder:"
- "initWithDevice:error:"
- "initWithIdentifier:targetQueue:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithOptions:"
- "initWithProxy:connection:clientConfig:clientIndex:clientId:scheduler:error:"
- "initWithQueue:"
- "initWithQueue:forUnitTest:"
- "initWithSuiteName:"
- "initWithTimestamp:tagIndex:attentionLostTimeout:"
- "initWithTimestamp:tagIndex:eventMask:"
- "initWithTimestamp:tagIndex:eventMask:digitizerButtonKeyboardMetadata:"
- "initWithTimestamp:tagIndex:faceMetadata:"
- "initWithTimestamp:tagIndex:remoteMetadata:"
- "initialize"
- "initializeClientState"
- "initializePreferences"
- "initializeStreamingTimer"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "invalid"
- "invalidate"
- "invalidateRemoteClientWithError:"
- "invalidateWithError:"
- "invalidateWithHandler:"
- "invalidateWithoutQueue"
- "invokeClientBlock:event:"
- "invokeRequiringClient:error:block:"
- "invokeSampler:"
- "invokeWithService:"
- "isAttentionAwareFeaturesEnabled"
- "isAttentionDetectionSupported"
- "isDeviceOnLockScreen"
- "isDeviceStationary"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMatchOrEnrollOperationRunning"
- "isMemberOfClass:"
- "isMetadataValid"
- "isOperationActive"
- "isOperationActive:"
- "isProxy"
- "isRunning"
- "isStreamerRunningWithMask:"
- "isStreamingClient"
- "isValidIndexForConnection:index:error:"
- "lastDistance"
- "lastEvent"
- "lastFaceBounds"
- "lastFaceDetectionScore"
- "lastFaceMetadataValid"
- "lastFaceState"
- "lastMetadataType"
- "lastMotionData"
- "lastMotionResult"
- "lastOrientation"
- "lastPersonID"
- "lastPitch"
- "lastPollTimeoutTime"
- "lastPositiveDetectTime"
- "lastRoll"
- "lastTriggerTime"
- "lastYaw"
- "length"
- "listener:shouldAcceptNewConnection:"
- "loadPersistentData"
- "lockForConfiguration:"
- "lockScreenStateChanging:"
- "logEvent:"
- "logStreamComplete:identifier:duration:ERActivated:"
- "minimumAttentionSamplerErrorRetryTime"
- "mode"
- "motionActivityChanging:"
- "motionDetect"
- "motionDetectState"
- "motionMatrix"
- "nextAttentionLostTime:"
- "nextFreeIndex"
- "nextSampleTimeForSamplingInterval:ignoreDisplayState:"
- "nextSamplingTimeForSamplingInterval:"
- "nextTimerForTime:"
- "notify:"
- "notifyClientOfStreamingEvent:"
- "notifyEvent:"
- "notifyEvent:timestamp:"
- "notifyEvent:timestamp:metadata:"
- "notifyHIDEvent:mask:timestamp:senderID:displayUUID:"
- "notifyPollEventType:event:"
- "notifyStreamingClientOfInterruption:"
- "notifyStreamingEvent:"
- "notifySupportedEventsChangedWithQueue:block:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openWithConnection:error:"
- "operation:captureInterrupted:"
- "operation:faceDetectStateChanged:"
- "operation:finishedWithReason:"
- "operation:motionDetectStateChanged:"
- "operation:presenceStateChanged:"
- "operation:stateChanged:"
- "operationBackend"
- "operationEndableCallback"
- "outputPowerLog"
- "outputPowerLogWithReply:"
- "payingAttention"
- "pearlAttentionSamplerErrorOccurred"
- "pearlError"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personID"
- "pingWithReply:"
- "pitchAngle"
- "pollForAttentionWithTimeout:event:error:"
- "pollForAttentionWithTimeout:queue:block:error:"
- "pollWithTimeout:reply:"
- "powerLogName:event:"
- "processHIDEvent:mask:timestamp:senderID:"
- "processHIDEvent:mask:timestamp:senderID:displayUUID:"
- "processIdentifier"
- "processInfo"
- "processName"
- "q"
- "q16@0:8"
- "raise:format:"
- "rangeOfString:"
- "receiveMetadata:type:"
- "receiveNotificationOfName:notification:"
- "receiveStreamingEvent"
- "receiver"
- "reevaluate"
- "reevaluateConfig"
- "registerForOperation:activateAttentionDetection:activateEyeRelief:activatePersonDetection:identifier:"
- "release"
- "removeAllObjects"
- "removeInvalidClients"
- "removeInvalidClientsWithConnection:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeStreamingClientwithIdentifier:"
- "resetAttentionLostTimeoutWithError:"
- "resetAttentionLostTimerWithReply:"
- "resetInterruptedStreamingClientWithIdentifier:"
- "resetStats"
- "respondsToSelector:"
- "resume"
- "resumeWithError:"
- "retain"
- "retainCount"
- "rollAngle"
- "running"
- "sampleLogger"
- "sampleStartedWithDeadline:"
- "sampleStatsPtr"
- "samplingStartTime"
- "samplingSuppressedMask"
- "screenStateChanging:"
- "self"
- "sendDeviceEvent:"
- "sendDeviceState:"
- "sendFaceDetectStateChangeMetadata:"
- "sendNotification:"
- "sendOperationEndReason:"
- "serviceInterrupted"
- "session:didUpdateConfiguration:"
- "sessionDidConnect:"
- "sessionDidDisconnect:"
- "setAVFoundationDelegate:"
- "setActivateAttentionDetection:"
- "setActivateEyeRelief:"
- "setActivateMotionDetect:"
- "setActivatePersonDetection:"
- "setActiveVideoMaxFrameDuration:"
- "setActiveVideoMinFrameDuration:"
- "setAllowedHIDEventsForRemoteEvent:"
- "setAttentionDetectionEnabled:"
- "setAttentionLostEventMask:"
- "setAttentionLostTimeout:"
- "setAttentionLostTimeoutDictionary:"
- "setAttentionLostTimeouts:"
- "setButtonDisplayUUIDs:"
- "setCarPlayConnected:"
- "setCarPlayConnected:reply:"
- "setCarPlayState:"
- "setCarplayStateChangedCallback:"
- "setClientAsInterrupted:forKey:"
- "setClientConfig:shouldReset:reply:"
- "setClientCount:"
- "setConfiguration:"
- "setConfiguration:shouldReset:"
- "setConfiguration:shouldReset:error:"
- "setContinuousFaceDetectMode:"
- "setCumulativeSamplingTime:"
- "setCurrentState:"
- "setDebugPreference:reply:"
- "setDelegate:"
- "setDigitizerDisplayUUIDs:"
- "setDisplayCallback:"
- "setDisplayState:"
- "setDisplayState:reply:"
- "setDisplayStateWithMask:displayState:"
- "setDistance:"
- "setErrorState:"
- "setEventHandlerWithQueue:block:"
- "setEventMask:"
- "setEventStreamerWithQueue:block:"
- "setExportedInterface:"
- "setExportedObject:"
- "setEyeRelief:"
- "setEyeReliefStatus:"
- "setFacePresent:"
- "setIdentifier:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsAttentionAwareFeaturesEnabled:"
- "setKeyboardDisplayUUIDs:"
- "setLastDistance:"
- "setLastFaceBounds:"
- "setLastFaceDetectionScore:"
- "setLastFaceMetadataValid:"
- "setLastFaceState:"
- "setLastMetadataType:"
- "setLastMotionData:"
- "setLastMotionResult:"
- "setLastOrientation:"
- "setLastPersonID:"
- "setLastPitch:"
- "setLastPollTimeoutTime:"
- "setLastPositiveDetectTime:"
- "setLastRoll:"
- "setLastTriggerTime:"
- "setLastYaw:"
- "setMetadataObjectTypes:"
- "setMetadataObjectsDelegate:queue:"
- "setMode:"
- "setMotionDetect:"
- "setNonSampledAttentionLostTimeout:"
- "setNonSampledAttentionLostTimeoutEnable:"
- "setNotificationHandler:"
- "setNotificationHandler:withMask:"
- "setNotificationHandlerWithQueue:block:"
- "setNotificationMask:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObserver:"
- "setOperationEndableCallback:"
- "setPearlError:"
- "setPearlErrorState:"
- "setPearlErrorState:reply:"
- "setPollingClient:"
- "setPollingFilter:"
- "setQueue:"
- "setReceiver:"
- "setRemoteObjectInterface:"
- "setRetroactiveTimeoutMode:"
- "setRunning:"
- "setSampleLogger:"
- "setSampleState:"
- "setSampleState:deliverEvent:"
- "setSampleState:deliverEvent:reply:"
- "setSampleState:reply:"
- "setSampleStatsPtr:"
- "setSampleSucceeded:"
- "setSampleWhileAbsent:"
- "setSamplingDelay:"
- "setSamplingInterval:"
- "setSamplingStartTime:"
- "setSamplingSuppressedMask:"
- "setSmartCoverCallback:"
- "setSmartCoverClosed:"
- "setSmartCoverClosed:reply:"
- "setSmartCoverState:"
- "setSmartCoverStateWithMask:smartCoverState:"
- "setStateChangedCallback:"
- "setStreamingDuration:"
- "setStreamingStartTime:"
- "setTag:"
- "setTimeout:"
- "setUnitTestDevice:"
- "setUnitTestMode"
- "setUnitTestMode:"
- "setUnityStream:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "setWithSet:"
- "setupBiomeStream"
- "setupNotificationsForCenter"
- "sharedAVFoundationSession"
- "sharedAttentionService"
- "sharedBacklight"
- "sharedClientConfig"
- "sharedDevice"
- "sharedEngine"
- "sharedLogger"
- "sharedManager"
- "sharedMotionDetectScheduler"
- "sharedSampler"
- "sharedScheduler"
- "sharedStatistics"
- "sharedUnitTestScheduler"
- "shouldActivateAttentionDetectForStreaming"
- "shouldActivateAttentionDetectionForSampling"
- "shouldActivateEyeReliefForStreaming"
- "shouldActivateMotionDetectForSampling"
- "shouldInitBeSent"
- "shouldSample:"
- "shouldSample:withDeadline:withOptions:"
- "sinkWithCompletion:receiveInput:"
- "sortedArrayUsingSelector:"
- "startActivityUpdatesToQueue:withHandler:"
- "startDeadlineComputation"
- "startOperationForReceiver:reply:"
- "startPresenceDetectOperation:"
- "startRunning"
- "startStalledTimerForOperation:"
- "startStream"
- "startStreamWithError:"
- "startUnitTestStream:options:"
- "startUpdate"
- "startWithError:"
- "startWithReply:"
- "startedConnectionAttemptOnTransport:"
- "starting"
- "state"
- "stateChangedCallback"
- "stationary"
- "stopRunning"
- "stopStreaming"
- "streamEventWithBlock:options:operationStartFailedBlock:"
- "streamEventsWithMask:block:options:operationStartFailedBlock:"
- "streamFaceDetectEvents"
- "streamFaceDetectEventsWithOptions:"
- "streamFaceDetectEventsWithReply:"
- "streamingCompleteWithidentifier:duration:ERActivated:"
- "streamingDuration"
- "streamingStartTime"
- "string"
- "stringWithFormat:"
- "subscribeOn:"
- "substringFromIndex:"
- "substringToIndex:"
- "superclass"
- "supportedEvents"
- "supportedEventsString"
- "supportsSecureCoding"
- "suspendWithError:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "tag"
- "tagForIndex:"
- "timeout"
- "timeoutOccurred"
- "triggerFaceDetectWithDeadline:options:"
- "truncateAWPersistentData:error:"
- "type"
- "unitTestController"
- "unitTestDevice"
- "unitTestMode"
- "unitTestSampler"
- "unitTestSampling"
- "unlockForConfiguration"
- "unregisterForOperation:"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "updateDataForClient:deadline:"
- "updateDeadlinesForTime:"
- "updateEventTimesForMask:timestamp:"
- "updateFaceState:"
- "updateFaceState:withFaceMetadata:"
- "updateSamplingDeadline:forClient:"
- "updateState:"
- "updateSuppressedMaskWithDisplayState:smartCoverClosed:carPlayConnected:"
- "updateWithConfig:"
- "userInfo"
- "v16@0:8"
- "v19@0:8{?=BBB}16"
- "v200@0:8{AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}16"
- "v20@0:8B16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@\"<AVFoundationUnitTestEventReceiving>\"16"
- "v24@0:8@\"<PearlCameraInterfaceMessaging>\"16"
- "v24@0:8@\"AWAttentionEvent\"16"
- "v24@0:8@\"CARSession\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<AWUnitTestSampler>\">16"
- "v24@0:8@?<v@?@\"AWAttentionEvent\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?Q>16"
- "v24@0:8@?<v@?{?=QQQ}>16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8^{?=QQQQ[0{?={?=dQQQQQQQBBBB}Qii}]}16"
- "v24@0:8^{?=QQQ}16"
- "v24@0:8^{AWNotification_s=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v27@0:8Q16{?=BBB}24"
- "v28@0:8@\"<BLSBacklightStateObservable>\"16B24"
- "v28@0:8@\"BKOperation\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v28@0:8B16B20B24"
- "v28@0:8Q16B24"
- "v28@0:8i16^{AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}20"
- "v31@0:8B16Q20{?=BBB}28"
- "v32@0:8@\"<BLSBacklightStateObservable>\"16@\"BLSBacklightChangeEvent\"24"
- "v32@0:8@\"AVMetadataObject\"16@\"NSString\"24"
- "v32@0:8@\"BKDevice\"16@\"BKMatchEvent\"24"
- "v32@0:8@\"BKDevice\"16q24"
- "v32@0:8@\"BKOperation\"16@\"BKFaceDetectStateInfo\"24"
- "v32@0:8@\"BKOperation\"16@\"BKMotionDetectStateInfo\"24"
- "v32@0:8@\"BKOperation\"16q24"
- "v32@0:8@\"CARSession\"16@\"CARSessionConfiguration\"24"
- "v32@0:8@\"NSString\"16@\"NSNotification\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8@?16Q24"
- "v32@0:8B16B20@?24"
- "v32@0:8B16B20@?<v@?@\"NSError\">24"
- "v32@0:8Q16@\"AWAttentionEvent\"24"
- "v32@0:8Q16@24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v32@0:8Q16Q24"
- "v36@0:8@\"AWAttentionAwarenessConfiguration\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16Q24B32"
- "v36@0:8i16^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}iiiB)20@28"
- "v40@0:8@\"<BLSBacklightStateObservable>\"16q24@\"BLSBacklightChangeEvent\"32"
- "v40@0:8@\"AVCaptureOutput\"16@\"NSArray\"24@\"AVCaptureConnection\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16q24@32"
- "v40@0:8Q16Q24@\"AWScheduler\"32"
- "v40@0:8Q16Q24@32"
- "v40@0:8Q16Q24^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32"
- "v44@0:8Q16@24Q32B40"
- "v48@0:8@\"<BLSBacklightStateObservable>\"16q24@\"NSArray\"32@\"NSArray\"40"
- "v48@0:8@\"AVCaptureOutput\"16@\"NSArray\"24@\"NSSet\"32@\"AVCaptureConnection\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16q24@32@40"
- "v48@0:8^{__IOHIDEvent=}16Q24Q32^{__IOHIDService=}40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v56@0:8^{__IOHIDEvent=}16Q24Q32^{__IOHIDService=}40@48"
- "v60@0:8@\"<AWFrameworkClient>\"16@\"AWAttentionAwarenessConfiguration\"24i32@\"NSUUID\"36B44@?<v@?@\"<AWRemoteClient>\"i@\"NSError\">48B56"
- "v60@0:8@16@24i32@36B44@?48B56"
- "validateAWPersistentDataHeader:"
- "validateMask"
- "validateWithError:"
- "valueForEntitlement:"
- "valueForKey:"
- "yawAngle"
- "zone"
- "{?=\"AWAttentionSamplerActivateAttentionDetection\"B\"AWAttentionSamplerActivateMotionDetection\"B\"AWAttentionSamplerActivatePersonDetection\"B}"
- "{?=\"AWAttentionStreamerActivateEyeRelief\"B\"AWAttentionStreamerActivateAttentionDetection\"B\"AWAttentionStreamerActivatePersonDetection\"B}"
- "{?=\"sampleCount\"Q\"pollCount\"Q\"singleShotCount\"Q}"
- "{?=BBB}16@0:8"
- "{?=BBB}24@0:8Q16"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{mach_timebase_info=\"numer\"I\"denom\"I}"
- "\x91"

```
