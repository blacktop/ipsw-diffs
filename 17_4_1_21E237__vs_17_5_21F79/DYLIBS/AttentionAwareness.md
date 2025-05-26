## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-158.100.2.0.0
-  __TEXT.__text: 0x2c208
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x1ae0
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x520
-  __TEXT.__cstring: 0x31cf
-  __TEXT.__oslogstring: 0x3ba2
-  __TEXT.__unwind_info: 0xab4
+158.120.15.0.0
+  __TEXT.__text: 0x31e2c
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_methlist: 0x1e40
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x668
+  __TEXT.__oslogstring: 0x4450
+  __TEXT.__cstring: 0x3695
+  __TEXT.__unwind_info: 0xbd0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x40c
-  __TEXT.__objc_methname: 0x4350
-  __TEXT.__objc_methtype: 0x1212
-  __TEXT.__objc_stubs: 0x3740
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xcb8
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__objc_classname: 0x501
+  __TEXT.__objc_methname: 0x4b60
+  __TEXT.__objc_methtype: 0x1490
+  __TEXT.__objc_stubs: 0x4060
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0xd80
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5048
-  __DATA_CONST.__objc_selrefs: 0xff0
+  __DATA_CONST.__objc_const: 0x5dc0
+  __DATA_CONST.__objc_selrefs: 0x1230
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x180
-  __DATA_CONST.__objc_superrefs: 0xc8
-  __AUTH_CONST.__const: 0x3c8
-  __AUTH_CONST.__cfstring: 0x1a00
-  __AUTH_CONST.__objc_const: 0xc58
+  __DATA_CONST.__objc_classrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__cfstring: 0x1b60
+  __AUTH_CONST.__objc_const: 0xdc0
+  __AUTH_CONST.__const: 0x3e8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x478
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x3ec
-  __DATA.__data: 0x788
-  __DATA.__bss: 0x58
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x498
+  __DATA.__data: 0x908
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 793
-  Symbols:   3003
-  CStrings:  1693
+  Functions: 883
+  Symbols:   3392
+  CStrings:  1872
 
Symbols:
+ +[AVFoundationEngine sharedEngine]
+ -[AVFoundationEngine .cxx_destruct]
+ -[AVFoundationEngine captureOutput:didOutputMetadataObjects:forMetadataObjectTypes:fromConnection:]
+ -[AVFoundationEngine handleNotification:notification:]
+ -[AVFoundationEngine initWithQueue:]
+ -[AVFoundationEngine isOperationActive:]
+ -[AVFoundationEngine registerForOperation:activateAttentionDetection:activateEyeRelief:identifier:]
+ -[AVFoundationEngine setupNotificationsForCenter]
+ -[AVFoundationEngine startOperationForReceiver:]
+ -[AVFoundationEngine unregisterForOperation:]
+ -[AVFoundationOperation .cxx_destruct]
+ -[AVFoundationOperation SessionDidStartRunningNotification:]
+ -[AVFoundationOperation SessionDidStopRunningNotification:]
+ -[AVFoundationOperation SessionInterruptionEndedNotification:]
+ -[AVFoundationOperation SessionRuntimeErrorNotification:]
+ -[AVFoundationOperation SessionWasInterruptedNotification:]
+ -[AVFoundationOperation State]
+ -[AVFoundationOperation Timeout]
+ -[AVFoundationOperation cancelActiveOperation:]
+ -[AVFoundationOperation checkIfOptionsHaveChanged:]
+ -[AVFoundationOperation checkIfTimeoutHasChanged:]
+ -[AVFoundationOperation createAVFoundationOperation]
+ -[AVFoundationOperation createPresenceDetectOperationWithTimeout:options:]
+ -[AVFoundationOperation fakeDataForDemoMode]
+ -[AVFoundationOperation initWithQueue:forUnitTest:]
+ -[AVFoundationOperation isOperationActive]
+ -[AVFoundationOperation operationBackend]
+ -[AVFoundationOperation receiveMetadata:type:]
+ -[AVFoundationOperation receiveNotificationOfName:notification:]
+ -[AVFoundationOperation receiveStreamingEvent]
+ -[AVFoundationOperation sendDeviceEvent:]
+ -[AVFoundationOperation sendDeviceState:]
+ -[AVFoundationOperation sendFaceDetectStateChangeMetadata:]
+ -[AVFoundationOperation sendOperationEndReason:]
+ -[AVFoundationOperation setDelegate:]
+ -[AVFoundationOperation startPresenceDetectOperation]
+ -[AVFoundationOperation timeoutOccured]
+ -[AVFoundationOperation unitTestSampler]
+ -[AVFoundationReceiver .cxx_destruct]
+ -[AVFoundationReceiver activateAttentionDetection]
+ -[AVFoundationReceiver activateEyeRelief]
+ -[AVFoundationReceiver initForReceiver:activateAttentionDetection:activateEyeRelief:]
+ -[AVFoundationReceiver receiver]
+ -[AVFoundationReceiver running]
+ -[AVFoundationReceiver setActivateAttentionDetection:]
+ -[AVFoundationReceiver setActivateEyeRelief:]
+ -[AVFoundationReceiver setReceiver:]
+ -[AVFoundationReceiver setRunning:]
+ -[AWAVFoundationAttentionStreamer .cxx_destruct]
+ -[AWAVFoundationAttentionStreamer attentionStreamerRunning]
+ -[AWAVFoundationAttentionStreamer cancelEventStream]
+ -[AWAVFoundationAttentionStreamer getStreamerOptions]
+ -[AWAVFoundationAttentionStreamer getStreamingSessionAndStartRunning]
+ -[AWAVFoundationAttentionStreamer initForUnitTest:queue:]
+ -[AWAVFoundationAttentionStreamer isAttentionAwareFeaturesEnabled]
+ -[AWAVFoundationAttentionStreamer receiveMetadata:type:]
+ -[AWAVFoundationAttentionStreamer receiveNotificationOfName:notification:]
+ -[AWAVFoundationAttentionStreamer receiveStreamingEvent]
+ -[AWAVFoundationAttentionStreamer sendNotification:]
+ -[AWAVFoundationAttentionStreamer setDisplayState:]
+ -[AWAVFoundationAttentionStreamer setDisplayStateFromNotification]
+ -[AWAVFoundationAttentionStreamer setIsAttentionAwareFeaturesEnabled:]
+ -[AWAVFoundationAttentionStreamer setNotificationHandler:]
+ -[AWAVFoundationAttentionStreamer setSmartCoverState:]
+ -[AWAVFoundationAttentionStreamer stopStreaming]
+ -[AWAVFoundationAttentionStreamer streamEventWithBlock:options:operationStartFailedBlock:]
+ -[AWAVFoundationAttentionStreamer unitTestController]
+ -[AWAVFoundationAttentionStreamer unitTestDevice]
+ -[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:]
+ -[AWDigitizerButtonKeyboardAttentionEvent initWithTimestamp:tagIndex:eventMask:digitizerButtonKeyboardMetadata:]
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table154
+ GCC_except_table159
+ GCC_except_table166
+ GCC_except_table186
+ GCC_except_table209
+ GCC_except_table21
+ GCC_except_table242
+ GCC_except_table264
+ GCC_except_table309
+ GCC_except_table315
+ GCC_except_table329
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table443
+ GCC_except_table449
+ GCC_except_table454
+ GCC_except_table458
+ GCC_except_table46
+ GCC_except_table462
+ GCC_except_table467
+ GCC_except_table471
+ GCC_except_table475
+ GCC_except_table542
+ GCC_except_table566
+ GCC_except_table642
+ GCC_except_table70
+ GCC_except_table767
+ GCC_except_table792
+ GCC_except_table796
+ GCC_except_table800
+ GCC_except_table803
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table808
+ GCC_except_table818
+ GCC_except_table820
+ GCC_except_table825
+ GCC_except_table831
+ GCC_except_table833
+ _AVCaptureDeviceTypeBuiltInInfraredMetadataCamera
+ _AVCaptureSessionDidStartRunningNotification
+ _AVCaptureSessionDidStopRunningNotification
+ _AVCaptureSessionInterruptionEndedNotification
+ _AVCaptureSessionRuntimeErrorNotification
+ _AVCaptureSessionWasInterruptedNotification
+ _AVMediaTypeMetadataObject
+ _AVMetadataObjectTypeEyeReliefStatus
+ _AVMetadataObjectTypeFace
+ _CMTimeMake
+ _OBJC_CLASS_$_AVCaptureDeviceDiscoverySession
+ _OBJC_CLASS_$_AVCaptureDeviceInput
+ _OBJC_CLASS_$_AVCaptureMetadataOutput
+ _OBJC_CLASS_$_AVCaptureSession
+ _OBJC_CLASS_$_AVFoundationEngine
+ _OBJC_CLASS_$_AVFoundationOperation
+ _OBJC_CLASS_$_AVFoundationReceiver
+ _OBJC_CLASS_$_AWAVFoundationAttentionStreamer
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_AVFoundationEngine._demoMode
+ _OBJC_IVAR_$_AVFoundationEngine._device
+ _OBJC_IVAR_$_AVFoundationEngine._input
+ _OBJC_IVAR_$_AVFoundationEngine._metadataOutput
+ _OBJC_IVAR_$_AVFoundationEngine._notificationCenter
+ _OBJC_IVAR_$_AVFoundationEngine._queue
+ _OBJC_IVAR_$_AVFoundationEngine._receivers
+ _OBJC_IVAR_$_AVFoundationEngine._session
+ _OBJC_IVAR_$_AVFoundationEngine._shouldRunAttentionDetect
+ _OBJC_IVAR_$_AVFoundationEngine._shouldRunEyeRelief
+ _OBJC_IVAR_$_AVFoundationEngine._signpostLogged
+ _OBJC_IVAR_$_AVFoundationOperation._AVFoundationEngine
+ _OBJC_IVAR_$_AVFoundationOperation._currentOptions
+ _OBJC_IVAR_$_AVFoundationOperation._delegate
+ _OBJC_IVAR_$_AVFoundationOperation._demoMode
+ _OBJC_IVAR_$_AVFoundationOperation._deviceEvent
+ _OBJC_IVAR_$_AVFoundationOperation._faceFound
+ _OBJC_IVAR_$_AVFoundationOperation._identifier
+ _OBJC_IVAR_$_AVFoundationOperation._notificationCenter
+ _OBJC_IVAR_$_AVFoundationOperation._operationState
+ _OBJC_IVAR_$_AVFoundationOperation._queue
+ _OBJC_IVAR_$_AVFoundationOperation._timeout
+ _OBJC_IVAR_$_AVFoundationOperation._unitTest
+ _OBJC_IVAR_$_AVFoundationReceiver._activateAttentionDetection
+ _OBJC_IVAR_$_AVFoundationReceiver._activateEyeRelief
+ _OBJC_IVAR_$_AVFoundationReceiver._receiver
+ _OBJC_IVAR_$_AVFoundationReceiver._running
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._AVFoundationEngine
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._attentionAwareFeaturesEnabledNotification
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._attentionStreamerRunning
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._callbackBlock
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._currentOptions
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._displayNotifyToken
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._displayOn
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._identifier
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._isAttentionAwareFeaturesEnabled
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._notificationBlock
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._queue
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._smartCoverClosed
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._unitTest
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._unitTestController
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._unitTester
+ _OBJC_IVAR_$_AWPearlAttentionSampler._signpostLogged
+ _OBJC_IVAR_$_AWRemoteClient._unityStream
+ _OBJC_METACLASS_$_AVFoundationEngine
+ _OBJC_METACLASS_$_AVFoundationOperation
+ _OBJC_METACLASS_$_AVFoundationReceiver
+ _OBJC_METACLASS_$_AWAVFoundationAttentionStreamer
+ __OBJC_$_CLASS_METHODS_AVFoundationEngine
+ __OBJC_$_INSTANCE_METHODS_AVFoundationEngine
+ __OBJC_$_INSTANCE_METHODS_AVFoundationOperation
+ __OBJC_$_INSTANCE_METHODS_AVFoundationReceiver
+ __OBJC_$_INSTANCE_METHODS_AWAVFoundationAttentionStreamer
+ __OBJC_$_INSTANCE_VARIABLES_AVFoundationEngine
+ __OBJC_$_INSTANCE_VARIABLES_AVFoundationOperation
+ __OBJC_$_INSTANCE_VARIABLES_AVFoundationReceiver
+ __OBJC_$_INSTANCE_VARIABLES_AWAVFoundationAttentionStreamer
+ __OBJC_$_PROP_LIST_AVFoundationEngine
+ __OBJC_$_PROP_LIST_AVFoundationReceiver
+ __OBJC_$_PROP_LIST_NSObject.1715
+ __OBJC_$_PROP_LIST_NSObject.2135
+ __OBJC_$_PROP_LIST_NSObject.342
+ __OBJC_$_PROP_LIST_NSObject.477
+ __OBJC_$_PROP_LIST_NSObject.739
+ __OBJC_$_PROP_LIST_NSObject.988
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFoundationReceiving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFoundationReceiving.1183
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFoundationUnitTestEventReceiving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFoundationUnitTestEventReceiving.1184
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWAttentionAwareService.740
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWFrameworkClient.2136
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWRemoteClient.741
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWUnitTestSampler.1533
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1716
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2137
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.343
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.478
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.742
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.989
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVCaptureMetadataOutputObjectsDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVCaptureMetadataOutputObjectsDelegatePrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDeviceDelegate.344
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDevicePearlDelegate.345
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKFaceDetectOperationDelegate.346
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKOperationDelegate.347
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1717
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2138
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.348
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.479
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.743
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.990
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SamplingOperation.349
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_StreamingOperation.1185
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVCaptureMetadataOutputObjectsDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVCaptureMetadataOutputObjectsDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFoundationReceiving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFoundationReceiving.1186
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFoundationUnitTestEventReceiving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFoundationUnitTestEventReceiving.1187
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWAttentionAwareService.744
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWFrameworkClient.2139
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWRemoteClient.745
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWUnitTestSampler.1534
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKDeviceDelegate.350
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKDevicePearlDelegate.351
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKFaceDetectOperationDelegate.352
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKOperationDelegate.353
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1718
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2140
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.354
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.480
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.746
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.991
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SamplingOperation.355
+ __OBJC_$_PROTOCOL_METHOD_TYPES_StreamingOperation.1188
+ __OBJC_$_PROTOCOL_REFS_AVCaptureMetadataOutputObjectsDelegate
+ __OBJC_$_PROTOCOL_REFS_AVCaptureMetadataOutputObjectsDelegatePrivate
+ __OBJC_$_PROTOCOL_REFS_AWFrameworkClient.2141
+ __OBJC_$_PROTOCOL_REFS_BKDeviceDelegate.356
+ __OBJC_$_PROTOCOL_REFS_BKDevicePearlDelegate.357
+ __OBJC_$_PROTOCOL_REFS_BKFaceDetectOperationDelegate.358
+ __OBJC_$_PROTOCOL_REFS_BKOperationDelegate.359
+ __OBJC_CLASS_PROTOCOLS_$_AVFoundationEngine
+ __OBJC_CLASS_PROTOCOLS_$_AVFoundationOperation
+ __OBJC_CLASS_PROTOCOLS_$_AWAVFoundationAttentionStreamer
+ __OBJC_CLASS_RO_$_AVFoundationEngine
+ __OBJC_CLASS_RO_$_AVFoundationOperation
+ __OBJC_CLASS_RO_$_AVFoundationReceiver
+ __OBJC_CLASS_RO_$_AWAVFoundationAttentionStreamer
+ __OBJC_LABEL_PROTOCOL_$_AVCaptureMetadataOutputObjectsDelegate
+ __OBJC_LABEL_PROTOCOL_$_AVCaptureMetadataOutputObjectsDelegatePrivate
+ __OBJC_LABEL_PROTOCOL_$_AVFoundationReceiving
+ __OBJC_LABEL_PROTOCOL_$_AVFoundationUnitTestEventReceiving
+ __OBJC_METACLASS_RO_$_AVFoundationEngine
+ __OBJC_METACLASS_RO_$_AVFoundationOperation
+ __OBJC_METACLASS_RO_$_AVFoundationReceiver
+ __OBJC_METACLASS_RO_$_AWAVFoundationAttentionStreamer
+ __OBJC_PROTOCOL_$_AVCaptureMetadataOutputObjectsDelegate
+ __OBJC_PROTOCOL_$_AVCaptureMetadataOutputObjectsDelegatePrivate
+ __OBJC_PROTOCOL_$_AVFoundationReceiving
+ __OBJC_PROTOCOL_$_AVFoundationUnitTestEventReceiving
+ ___31-[AWScheduler initWithOptions:]_block_invoke.65
+ ___31-[AWScheduler initWithOptions:]_block_invoke.68
+ ___34+[AVFoundationEngine sharedEngine]_block_invoke
+ ___48-[AVFoundationEngine startOperationForReceiver:]_block_invoke
+ ___48-[AVFoundationEngine startOperationForReceiver:]_block_invoke.51
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_2
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_3
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_4
+ ___49-[AVFoundationEngine setupNotificationsForCenter]_block_invoke_5
+ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.84
+ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.87
+ ___53-[AVFoundationOperation startPresenceDetectOperation]_block_invoke
+ ___54-[AVFoundationEngine handleNotification:notification:]_block_invoke
+ ___54-[AVFoundationEngine handleNotification:notification:]_block_invoke_2
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke.7
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_2
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_2.8
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_3
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_4
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_5
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_6
+ ___57-[AWAVFoundationAttentionStreamer initForUnitTest:queue:]_block_invoke_7
+ ___67-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:]_block_invoke
+ ___67-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:]_block_invoke.53
+ ___99-[AVFoundationEngine captureOutput:didOutputMetadataObjects:forMetadataObjectTypes:fromConnection:]_block_invoke
+ ___99-[AVFoundationEngine captureOutput:didOutputMetadataObjects:forMetadataObjectTypes:fromConnection:]_block_invoke.53
+ ___Block_byref_object_copy_.1014
+ ___Block_byref_object_copy_.1380
+ ___Block_byref_object_copy_.1758
+ ___Block_byref_object_copy_.2034
+ ___Block_byref_object_copy_.562
+ ___Block_byref_object_copy_.672
+ ___Block_byref_object_dispose_.1015
+ ___Block_byref_object_dispose_.1381
+ ___Block_byref_object_dispose_.1759
+ ___Block_byref_object_dispose_.2035
+ ___Block_byref_object_dispose_.563
+ ___Block_byref_object_dispose_.673
+ ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e15_v32?0816^B24lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e15_v32?0816^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.1036
+ ___block_literal_global.1318
+ ___block_literal_global.136
+ ___block_literal_global.1397
+ ___block_literal_global.1775
+ ___block_literal_global.206
+ ___block_literal_global.2065
+ ___block_literal_global.2379
+ ___block_literal_global.296
+ ___block_literal_global.41
+ ___block_literal_global.442
+ ___block_literal_global.670
+ ___block_literal_global.847
+ ___block_literal_global.956
+ ___getPearlDevice_block_invoke.301
+ __os_feature_enabled_impl
+ _dispatch_after
+ _getPearlDevice.onceToken.295
+ _getPearlDevice.result.297
+ _isSmartCoverEvent.flap1SensorIsEngaged
+ _isSmartCoverEvent.openSensorIsEngaged
+ _objc_msgSend$SessionDidStartRunningNotification:
+ _objc_msgSend$SessionDidStopRunningNotification:
+ _objc_msgSend$SessionInterruptionEndedNotification:
+ _objc_msgSend$SessionRuntimeErrorNotification:
+ _objc_msgSend$SessionWasInterruptedNotification:
+ _objc_msgSend$addInput:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$addOutput:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$canAddInput:
+ _objc_msgSend$canAddOutput:
+ _objc_msgSend$cancelUnitTestStream
+ _objc_msgSend$checkIfOptionsHaveChanged:
+ _objc_msgSend$checkIfTimeoutHasChanged:
+ _objc_msgSend$confidence
+ _objc_msgSend$createAVFoundationOperation
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$devices
+ _objc_msgSend$discoverySessionWithDeviceTypes:mediaType:position:
+ _objc_msgSend$fakeDataForDemoMode
+ _objc_msgSend$firstObject
+ _objc_msgSend$getStreamingSessionAndStartRunning
+ _objc_msgSend$handleNotification:notification:
+ _objc_msgSend$hasConfidence
+ _objc_msgSend$hasDistance
+ _objc_msgSend$hasOrientation
+ _objc_msgSend$hasPayingAttention
+ _objc_msgSend$hasPayingAttentionConfidence
+ _objc_msgSend$hasPitchAngle
+ _objc_msgSend$hasRollAngle
+ _objc_msgSend$hasYawAngle
+ _objc_msgSend$initForReceiver:activateAttentionDetection:activateEyeRelief:
+ _objc_msgSend$initWithDevice:error:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithTimestamp:tagIndex:eventMask:digitizerButtonKeyboardMetadata:
+ _objc_msgSend$isAttentionDetectionSupported
+ _objc_msgSend$isOperationActive
+ _objc_msgSend$isOperationActive:
+ _objc_msgSend$isRunning
+ _objc_msgSend$lockForConfiguration:
+ _objc_msgSend$payingAttention
+ _objc_msgSend$payingAttentionConfidence
+ _objc_msgSend$pitchAngle
+ _objc_msgSend$processHIDEvent:mask:timestamp:senderID:
+ _objc_msgSend$receiveMetadata:type:
+ _objc_msgSend$receiveNotificationOfName:notification:
+ _objc_msgSend$receiver
+ _objc_msgSend$registerForOperation:activateAttentionDetection:activateEyeRelief:identifier:
+ _objc_msgSend$rollAngle
+ _objc_msgSend$running
+ _objc_msgSend$sendDeviceEvent:
+ _objc_msgSend$sendDeviceState:
+ _objc_msgSend$sendFaceDetectStateChangeMetadata:
+ _objc_msgSend$sendOperationEndReason:
+ _objc_msgSend$setAVFoundationDelegate:
+ _objc_msgSend$setActiveVideoMaxFrameDuration:
+ _objc_msgSend$setActiveVideoMinFrameDuration:
+ _objc_msgSend$setAttentionDetectionEnabled:
+ _objc_msgSend$setMetadataObjectTypes:
+ _objc_msgSend$setMetadataObjectsDelegate:queue:
+ _objc_msgSend$setRunning:
+ _objc_msgSend$setupNotificationsForCenter
+ _objc_msgSend$sharedEngine
+ _objc_msgSend$startOperationForReceiver:
+ _objc_msgSend$startRunning
+ _objc_msgSend$startUnitTestStream:options:
+ _objc_msgSend$stopRunning
+ _objc_msgSend$stopStreaming
+ _objc_msgSend$timeoutOccured
+ _objc_msgSend$unitTestController
+ _objc_msgSend$unlockForConfiguration
+ _objc_msgSend$unregisterForOperation:
+ _objc_msgSend$userInfo
+ _objc_msgSend$yawAngle
+ _sharedEngine.engine
+ _sharedEngine.onceToken
+ _sharedManager.manager.1037
+ _sharedManager.onceToken.1035
+ _startAttentionAwarenessServer
+ _sysctlbyname
- -[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:displayUUID:]
- -[AWDigitizerButtonKeyboardAttentionEvent initWithTimestamp:tagIndex:digitizerButtonKeyboardMetadata:]
- GCC_except_table11
- GCC_except_table125
- GCC_except_table126
- GCC_except_table13
- GCC_except_table130
- GCC_except_table137
- GCC_except_table15
- GCC_except_table157
- GCC_except_table17
- GCC_except_table180
- GCC_except_table235
- GCC_except_table268
- GCC_except_table353
- GCC_except_table359
- GCC_except_table364
- GCC_except_table368
- GCC_except_table372
- GCC_except_table377
- GCC_except_table381
- GCC_except_table385
- GCC_except_table41
- GCC_except_table452
- GCC_except_table476
- GCC_except_table552
- GCC_except_table677
- GCC_except_table702
- GCC_except_table706
- GCC_except_table710
- GCC_except_table713
- GCC_except_table715
- GCC_except_table717
- GCC_except_table718
- GCC_except_table728
- GCC_except_table730
- GCC_except_table735
- GCC_except_table741
- GCC_except_table743
- GCC_except_table75
- GCC_except_table76
- _OBJC_IVAR_$_AWAttentionAwarenessClient._streamingRunning
- __OBJC_$_PROP_LIST_NSObject.1328
- __OBJC_$_PROP_LIST_NSObject.1736
- __OBJC_$_PROP_LIST_NSObject.254
- __OBJC_$_PROP_LIST_NSObject.380
- __OBJC_$_PROP_LIST_NSObject.627
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWAttentionAwareService.628
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWFrameworkClient.1737
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWRemoteClient.629
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWUnitTestSampler.1149
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1329
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1738
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.255
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.381
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.630
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDeviceDelegate.256
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDevicePearlDelegate.257
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKFaceDetectOperationDelegate.258
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKOperationDelegate.259
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1330
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1739
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.260
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.382
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.631
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWAttentionAwareService.632
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWFrameworkClient.1740
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWRemoteClient.633
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWUnitTestSampler.1150
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKDeviceDelegate.261
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKDevicePearlDelegate.262
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKFaceDetectOperationDelegate.263
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKOperationDelegate.264
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1331
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1741
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.265
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.383
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.634
- __OBJC_$_PROTOCOL_REFS_AWFrameworkClient.1742
- __OBJC_$_PROTOCOL_REFS_BKDeviceDelegate.266
- __OBJC_$_PROTOCOL_REFS_BKDevicePearlDelegate.267
- __OBJC_$_PROTOCOL_REFS_BKFaceDetectOperationDelegate.268
- __OBJC_$_PROTOCOL_REFS_BKOperationDelegate.269
- ___31-[AWScheduler initWithOptions:]_block_invoke.56
- ___31-[AWScheduler initWithOptions:]_block_invoke.59
- ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.75
- ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.78
- ___79-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:displayUUID:]_block_invoke
- ___79-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:displayUUID:]_block_invoke.53
- ___Block_byref_object_copy_.1001
- ___Block_byref_object_copy_.1368
- ___Block_byref_object_copy_.1644
- ___Block_byref_object_copy_.455
- ___Block_byref_object_copy_.565
- ___Block_byref_object_copy_.765
- ___Block_byref_object_dispose_.1002
- ___Block_byref_object_dispose_.1369
- ___Block_byref_object_dispose_.1645
- ___Block_byref_object_dispose_.456
- ___Block_byref_object_dispose_.566
- ___Block_byref_object_dispose_.766
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_80_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.1017
- ___block_literal_global.130
- ___block_literal_global.1386
- ___block_literal_global.1670
- ___block_literal_global.1942
- ___block_literal_global.216
- ___block_literal_global.346
- ___block_literal_global.563
- ___block_literal_global.739
- ___block_literal_global.77
- ___block_literal_global.786
- ___block_literal_global.9
- ___block_literal_global.945
- ___getPearlDevice_block_invoke.221
- _findDisplayUUID
- _getPearlDevice.onceToken.215
- _getPearlDevice.result.217
- _objc_msgSend$cancelFaceDetectStreamWithError:
- _objc_msgSend$initWithTimestamp:tagIndex:digitizerButtonKeyboardMetadata:
- _sharedManager.manager.787
- _sharedManager.onceToken.785
CStrings:
+ "\x02\x12#"
+ "\x032"
+ "\a"
+ " Client already started an operation with the same options"
+ " Unable to create Presence detect operation through AVFoundation"
+ " Unable to get a streaming session from AVFoundation"
+ "%30s:%-4d: %13.5f:  Info: AVFoundationOperation %@ initialized"
+ "%30s:%-4d: %13.5f:  Info: Asking for metadata types: %@"
+ "%30s:%-4d: %13.5f:  Info: Attention detection session started ER %s, AD/FD %s"
+ "%30s:%-4d: %13.5f:  Info: Attention streamer already running, don't start another operation"
+ "%30s:%-4d: %13.5f:  Info: Cancelling current stream and starting a new one as stream options have changed"
+ "%30s:%-4d: %13.5f:  Info: Looking for devices of types %@"
+ "%30s:%-4d: %13.5f:  Info: Notification %@ received"
+ "%30s:%-4d: %13.5f:  Info: Received metadata in %@ faceDetectStateChanged %s pitch: %f yaw: %f roll: %f orientation: %@ attentionScore: %ffaceDetectionScore: %f"
+ "%30s:%-4d: %13.5f:  Info: Registered receiver %@ for AVFoundation operation"
+ "%30s:%-4d: %13.5f:  Info: Runtime error received: %@"
+ "%30s:%-4d: %13.5f:  Info: Session that is already running has the same options that was requested by %@, not restarting session"
+ "%30s:%-4d: %13.5f:  Info: Session was interrupted before it got started, calling stop on the session immediately"
+ "%30s:%-4d: %13.5f:  Info: Streaming session was interrupted"
+ "%30s:%-4d: %13.5f:  Info: This method doesn't do anything, this is an empty stub"
+ "%30s:%-4d: %13.5f:  Info: Timeout: %f AWAttentionSamplerActivateAttentionDetection: %s"
+ "%30s:%-4d: %13.5f:  Info: Unregistering receiver %@, remaining receivers: %@"
+ "%30s:%-4d: %13.5f:  Info: User toggled the Attention Aware Features flag to %s"
+ "%30s:%-4d: %13.5f:  Info: Using device %@ for starting AVFoundation operations"
+ "%30s:%-4d: %13.5f:  Info: forceUseOfAVFoundationPath: %d, exclavesAvailable: %d areFeatureFlagsON: %d"
+ "%30s:%-4d: %13.5f: Debug: Delivering event to client %@"
+ "%30s:%-4d: %13.5f: Error: Could not log configuration for device %@ error: %@"
+ "%30s:%-4d: %13.5f: Error: Unable to add input to session"
+ "%30s:%-4d: %13.5f: Error: Unable to add output to session"
+ "%30s:%-4d: %13.5f: Error: Unable to get streaming session and start running"
+ "%30s:%-4d: %13.5f: Error: Unable to obtain device for streaming"
+ "%30s:%-4d: %13.5f: Error: Unable to obtain session for streaming"
+ "%30s:%-4d: %13.5f: Error: sysctlbyname(kern.exclaves_status): %s"
+ "-[AWAVFoundationAttentionStreamer setNotificationHandler:]"
+ "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/Client/DevelopmentMode.m"
+ "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/Shared/platform.m"
+ "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/AVFoundationEngine/AVFoundationEngine.m"
+ "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/AVFoundationEngine/AVFoundationHelper.m"
+ "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/Sampling/PearlAVFoundationInterface.m"
+ "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/Streaming/AVFoundationAttentionStreamer.m"
+ "<%@: %p> (identifier: %@ samplingInterval: %13.5f samplingDelay: %13.5f sampleWhileAbsent: %s retroactiveTimeoutMode: %s continuousFaceDetectMode: %s unityStream: %s activateEyeRelief: %s activateAttentionDetection: %s activateMotionDetection: %s attentionLostTimeouts: %@ notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ tagIndex %llu)"
+ "@\"<AVFoundationReceiving>\""
+ "@\"<AVFoundationUnitTestStreamerCreating>\""
+ "@\"<AWUnitTestSampler>\""
+ "@\"AVCaptureDevice\""
+ "@\"AVCaptureDeviceInput\""
+ "@\"AVCaptureMetadataOutput\""
+ "@\"AVCaptureSession\""
+ "@\"AVFoundationEngine\""
+ "@\"NSNotificationCenter\""
+ "@32@0:8@16B24B28"
+ "@48@0:8d16Q24Q32^{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}}40"
+ "AA - Calling startRunning"
+ "AA - Received frame of EyeRelief data"
+ "AA - Received frame of face detect data"
+ "AVCaptureMetadataOutputObjectsDelegate"
+ "AVCaptureMetadataOutputObjectsDelegatePrivate"
+ "AVFoundationAttentionSampler"
+ "AVFoundationAttentionStreamer"
+ "AVFoundationAttentionStreamer.m"
+ "AVFoundationEngine"
+ "AVFoundationOperation"
+ "AVFoundationReceiver"
+ "AVFoundationReceiving"
+ "AVFoundationUnitTestEventReceiving"
+ "AWAVFoundationAttentionStreamer"
+ "B18@0:8{?=BB}16"
+ "B24@0:8d16"
+ "B40@0:8@16B24B28@32"
+ "Could not lock device configuration to set frame rate"
+ "Face found"
+ "IS NOT RUNNING"
+ "IS RUNNING"
+ "ISPExclaves"
+ "ISPExclavesEnablement"
+ "Operation timed out"
+ "Runtime error"
+ "SessionDidStartRunningNotification:"
+ "SessionDidStopRunningNotification:"
+ "SessionInterruptionEndedNotification:"
+ "SessionRuntimeErrorNotification:"
+ "SessionWasInterruptedNotification:"
+ "T@\"<AVFoundationReceiving>\",&,N,V_receiver"
+ "TB,N,V_running"
+ "_AVFoundationEngine"
+ "_demoMode"
+ "_device"
+ "_deviceEvent"
+ "_faceFound"
+ "_input"
+ "_metadataOutput"
+ "_notificationCenter"
+ "_operationState"
+ "_receiver"
+ "_receivers"
+ "_running"
+ "_session"
+ "_shouldRunAttentionDetect"
+ "_shouldRunEyeRelief"
+ "_signpostLogged"
+ "_unitTestController"
+ "_unitTester"
+ "addInput:"
+ "addObserverForName:object:queue:usingBlock:"
+ "addOutput:"
+ "boolForKey:"
+ "canAddInput:"
+ "canAddOutput:"
+ "captureOutput:didOutputMetadataObjects:forMetadataObjectTypes:fromConnection:"
+ "captureOutput:didOutputMetadataObjects:fromConnection:"
+ "checkIfOptionsHaveChanged:"
+ "checkIfTimeoutHasChanged:"
+ "confidence"
+ "createAVFoundationOperation"
+ "defaultCenter"
+ "demoMode"
+ "devices"
+ "discoverySessionWithDeviceTypes:mediaType:position:"
+ "exclavesEnabled"
+ "fakeDataForDemoMode"
+ "firstObject"
+ "getStreamingSessionAndStartRunning"
+ "handleNotification:notification:"
+ "hasConfidence"
+ "hasDistance"
+ "hasOrientation"
+ "hasPayingAttention"
+ "hasPayingAttentionConfidence"
+ "hasPitchAngle"
+ "hasRollAngle"
+ "hasYawAngle"
+ "initForReceiver:activateAttentionDetection:activateEyeRelief:"
+ "initWithDevice:error:"
+ "initWithQueue:"
+ "initWithSuiteName:"
+ "initWithTimestamp:tagIndex:eventMask:digitizerButtonKeyboardMetadata:"
+ "isAttentionDetectionSupported"
+ "isOperationActive:"
+ "isRunning"
+ "kern.exclaves_status"
+ "lockForConfiguration:"
+ "payingAttention"
+ "payingAttentionConfidence"
+ "pitchAngle"
+ "processHIDEvent:mask:timestamp:senderID:"
+ "receiveMetadata:type:"
+ "receiveNotificationOfName:notification:"
+ "receiver"
+ "registerForOperation:activateAttentionDetection:activateEyeRelief:identifier:"
+ "rollAngle"
+ "running"
+ "sendDeviceEvent:"
+ "sendDeviceState:"
+ "sendFaceDetectStateChangeMetadata:"
+ "sendOperationEndReason:"
+ "setActiveVideoMaxFrameDuration:"
+ "setActiveVideoMinFrameDuration:"
+ "setAttentionDetectionEnabled:"
+ "setMetadataObjectTypes:"
+ "setMetadataObjectsDelegate:queue:"
+ "setReceiver:"
+ "setRunning:"
+ "setupNotificationsForCenter"
+ "sharedEngine"
+ "startOperationForReceiver:"
+ "startRunning"
+ "stopRunning"
+ "stopStreaming"
+ "timeoutOccured"
+ "unitTestController"
+ "unlockForConfiguration"
+ "unregisterForOperation:"
+ "userInfo"
+ "v168@0:8{AWFaceDetectMetadata=BdddQdQdQ[16f]ffB}16"
+ "v16@?0@\"NSNotification\"8"
+ "v32@0:8@\"AVMetadataObject\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@\"NSNotification\"24"
+ "v40@0:8@\"AVCaptureOutput\"16@\"NSArray\"24@\"AVCaptureConnection\"32"
+ "v40@0:8@16@24@32"
+ "v48@0:8@\"AVCaptureOutput\"16@\"NSArray\"24@\"NSSet\"32@\"AVCaptureConnection\"40"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8^{__IOHIDEvent=}16Q24Q32Q40"
+ "yawAngle"
- "<%@: %p> (identifier: %@ samplingInterval: %13.5f samplingDelay: %13.5f sampleWhileAbsent: %s retroactiveTimeoutMode: %s continuousFaceDetectMode: %s activateEyeRelief: %s activateAttentionDetection: %s activateMotionDetection: %s attentionLostTimeouts: %@ notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ tagIndex %llu)"
- "@40@0:8d16Q24^{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}}32"
- "_streamingRunning"
- "initWithTimestamp:tagIndex:digitizerButtonKeyboardMetadata:"

```
