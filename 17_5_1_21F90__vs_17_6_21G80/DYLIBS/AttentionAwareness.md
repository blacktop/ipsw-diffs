## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-158.120.15.0.0
-  __TEXT.__text: 0x31e2c
+158.140.2.0.0
+  __TEXT.__text: 0x32ca8
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x1e40
+  __TEXT.__objc_methlist: 0x1f18
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x668
-  __TEXT.__oslogstring: 0x4450
-  __TEXT.__cstring: 0x3695
-  __TEXT.__unwind_info: 0xbd0
+  __TEXT.__gcc_except_tab: 0x674
+  __TEXT.__oslogstring: 0x44b2
+  __TEXT.__cstring: 0x37e0
+  __TEXT.__unwind_info: 0xc0c
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x4b60
-  __TEXT.__objc_methtype: 0x1490
-  __TEXT.__objc_stubs: 0x4060
+  __TEXT.__objc_classname: 0x561
+  __TEXT.__objc_methname: 0x4e3a
+  __TEXT.__objc_methtype: 0x152f
+  __TEXT.__objc_stubs: 0x4240
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0xd80
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5dc0
-  __DATA_CONST.__objc_selrefs: 0x1230
+  __DATA_CONST.__objc_const: 0x6120
+  __DATA_CONST.__objc_selrefs: 0x12b0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x1d0
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__cfstring: 0x1b60
-  __AUTH_CONST.__objc_const: 0xdc0
+  __DATA_CONST.__objc_classrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __AUTH_CONST.__cfstring: 0x1b80
+  __AUTH_CONST.__objc_const: 0xe50
   __AUTH_CONST.__const: 0x3e8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x498
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x498
-  __DATA.__data: 0x908
-  __DATA.__bss: 0x70
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x4dc
+  __DATA.__data: 0x9c8
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 883
-  Symbols:   3392
-  CStrings:  1872
+  Functions: 909
+  Symbols:   3502
+  CStrings:  1927
 
Symbols:
+ -[AWAttentionAwareService LockScreenStateChanging:]
+ -[AWAttentionAwareService MotionStateChanging:]
+ -[AWAttentionAwarenessConfiguration pollingFilter]
+ -[AWAttentionAwarenessConfiguration setPollingFilter:]
+ -[AWAttentionSampler operationEndableCallback]
+ -[AWAttentionSampler setOperationEndableCallback:]
+ -[AWRemoteClient canDeliverPollingEvent]
+ -[AWRemoteClient canOperationBeEndedForClient]
+ -[AWScheduler canActiveOperationBeEnded]
+ -[AWScheduler isDeviceOnLockScreen]
+ -[AWScheduler isDeviceStationary]
+ -[AWScheduler lockScreenStateChanging:]
+ -[AWScheduler motionActivityChanging:]
+ -[LockScreenStateObserver .cxx_destruct]
+ -[LockScreenStateObserver initWithCallbackQueue:observer:]
+ -[MotionActivityObserver .cxx_destruct]
+ -[MotionActivityObserver initWithCallbackQueue:observer:]
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table165
+ GCC_except_table176
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table220
+ GCC_except_table224
+ GCC_except_table255
+ GCC_except_table277
+ GCC_except_table322
+ GCC_except_table328
+ GCC_except_table347
+ GCC_except_table391
+ GCC_except_table392
+ GCC_except_table463
+ GCC_except_table469
+ GCC_except_table474
+ GCC_except_table478
+ GCC_except_table48
+ GCC_except_table482
+ GCC_except_table487
+ GCC_except_table491
+ GCC_except_table495
+ GCC_except_table50
+ GCC_except_table562
+ GCC_except_table586
+ GCC_except_table662
+ GCC_except_table75
+ GCC_except_table789
+ GCC_except_table814
+ GCC_except_table822
+ GCC_except_table827
+ GCC_except_table829
+ GCC_except_table830
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table847
+ GCC_except_table853
+ GCC_except_table855
+ _CARApplicationLocalizedNameKey_block_invoke.onceToken
+ _OBJC_CLASS_$_CMMotionActivityManager
+ _OBJC_CLASS_$_LockScreenStateObserver
+ _OBJC_CLASS_$_MotionActivityObserver
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_IVAR_$_AWAttentionAwareService._lockScreenStateObserver
+ _OBJC_IVAR_$_AWAttentionAwareService._motionActivityObserver
+ _OBJC_IVAR_$_AWAttentionAwarenessConfiguration._pollingFilter
+ _OBJC_IVAR_$_AWAttentionSampler._operationEndableCallback
+ _OBJC_IVAR_$_AWRemoteClient._filteredPollingEventDelivered
+ _OBJC_IVAR_$_AWRemoteClient._pollingFilter
+ _OBJC_IVAR_$_AWScheduler._isDeviceOnLockScreen
+ _OBJC_IVAR_$_AWScheduler._isDeviceStationary
+ _OBJC_IVAR_$_LockScreenStateObserver._callbackQueue
+ _OBJC_IVAR_$_LockScreenStateObserver._isDeviceOnLockScreen
+ _OBJC_IVAR_$_LockScreenStateObserver._lockToken
+ _OBJC_IVAR_$_LockScreenStateObserver._observer
+ _OBJC_IVAR_$_MotionActivityObserver._callbackQueue
+ _OBJC_IVAR_$_MotionActivityObserver._isDeviceStationary
+ _OBJC_IVAR_$_MotionActivityObserver._motionActivityManager
+ _OBJC_IVAR_$_MotionActivityObserver._observer
+ _OBJC_IVAR_$_MotionActivityObserver._operationQueue
+ _OBJC_METACLASS_$_LockScreenStateObserver
+ _OBJC_METACLASS_$_MotionActivityObserver
+ __OBJC_$_INSTANCE_METHODS_LockScreenStateObserver
+ __OBJC_$_INSTANCE_METHODS_MotionActivityObserver
+ __OBJC_$_INSTANCE_VARIABLES_LockScreenStateObserver
+ __OBJC_$_INSTANCE_VARIABLES_MotionActivityObserver
+ __OBJC_$_PROP_LIST_NSObject.1762
+ __OBJC_$_PROP_LIST_NSObject.2188
+ __OBJC_$_PROP_LIST_NSObject.357
+ __OBJC_$_PROP_LIST_NSObject.484
+ __OBJC_$_PROP_LIST_NSObject.749
+ __OBJC_$_PROP_LIST_NSObject.996
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFoundationReceiving.1219
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFoundationUnitTestEventReceiving.1220
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWAttentionAwareService.750
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWFrameworkClient.2189
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWRemoteClient.751
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWUnitTestSampler.1578
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LockScreenStateObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MotionActivityObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1763
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2190
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.358
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.485
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.752
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.997
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDeviceDelegate.359
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDevicePearlDelegate.360
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKFaceDetectOperationDelegate.361
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKOperationDelegate.362
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1764
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2191
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.363
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.486
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.753
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.998
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SamplingOperation.364
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_StreamingOperation.1221
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFoundationReceiving.1222
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFoundationUnitTestEventReceiving.1223
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWAttentionAwareService.754
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWFrameworkClient.2192
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWRemoteClient.755
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWUnitTestSampler.1579
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKDeviceDelegate.365
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKDevicePearlDelegate.366
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKFaceDetectOperationDelegate.367
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKOperationDelegate.368
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LockScreenStateObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MotionActivityObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1765
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2193
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.369
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.487
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.756
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.999
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SamplingOperation.370
+ __OBJC_$_PROTOCOL_METHOD_TYPES_StreamingOperation.1224
+ __OBJC_$_PROTOCOL_REFS_AWFrameworkClient.2194
+ __OBJC_$_PROTOCOL_REFS_BKDeviceDelegate.371
+ __OBJC_$_PROTOCOL_REFS_BKDevicePearlDelegate.372
+ __OBJC_$_PROTOCOL_REFS_BKFaceDetectOperationDelegate.373
+ __OBJC_$_PROTOCOL_REFS_BKOperationDelegate.374
+ __OBJC_CLASS_RO_$_LockScreenStateObserver
+ __OBJC_CLASS_RO_$_MotionActivityObserver
+ __OBJC_LABEL_PROTOCOL_$_LockScreenStateObserving
+ __OBJC_LABEL_PROTOCOL_$_MotionActivityObserving
+ __OBJC_METACLASS_RO_$_LockScreenStateObserver
+ __OBJC_METACLASS_RO_$_MotionActivityObserver
+ __OBJC_PROTOCOL_$_LockScreenStateObserving
+ __OBJC_PROTOCOL_$_MotionActivityObserving
+ ___118-[AWAttentionAwareService addClient:clientConfig:clientIndex:clientId:unitTestMode:reply:subscribeForStreamingEvents:]_block_invoke_2
+ ___31-[AWScheduler initWithOptions:]_block_invoke.67
+ ___31-[AWScheduler initWithOptions:]_block_invoke_2
+ ___47-[AWAttentionAwareService MotionStateChanging:]_block_invoke
+ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.85
+ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.88
+ ___51-[AWAttentionAwareService LockScreenStateChanging:]_block_invoke
+ ___57-[MotionActivityObserver initWithCallbackQueue:observer:]_block_invoke
+ ___57-[MotionActivityObserver initWithCallbackQueue:observer:]_block_invoke_2
+ ___57-[MotionActivityObserver initWithCallbackQueue:observer:]_block_invoke_3
+ ___58-[LockScreenStateObserver initWithCallbackQueue:observer:]_block_invoke
+ ___58-[LockScreenStateObserver initWithCallbackQueue:observer:]_block_invoke_2
+ ___67-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:]_block_invoke.55
+ ___Block_byref_object_copy_.1049
+ ___Block_byref_object_copy_.1422
+ ___Block_byref_object_copy_.1805
+ ___Block_byref_object_copy_.2086
+ ___Block_byref_object_copy_.580
+ ___Block_byref_object_copy_.692
+ ___Block_byref_object_dispose_.1050
+ ___Block_byref_object_dispose_.1423
+ ___Block_byref_object_dispose_.1806
+ ___Block_byref_object_dispose_.2087
+ ___Block_byref_object_dispose_.581
+ ___Block_byref_object_dispose_.693
+ ___block_descriptor_40_e8_32s_e26_v16?0"CMMotionActivity"8ls32l8
+ ___block_descriptor_40_e8_32w_e5_B8?0lw32l8
+ ___block_literal_global.1071
+ ___block_literal_global.126
+ ___block_literal_global.1359
+ ___block_literal_global.1439
+ ___block_literal_global.1822
+ ___block_literal_global.2117
+ ___block_literal_global.213
+ ___block_literal_global.2457
+ ___block_literal_global.309
+ ___block_literal_global.36
+ ___block_literal_global.449
+ ___block_literal_global.690
+ ___block_literal_global.858
+ ___block_literal_global.965
+ ___getPearlDevice_block_invoke.314
+ _getPearlDevice.onceToken.308
+ _getPearlDevice.result.310
+ _initWithCallbackQueue:observer:.onceToken
+ _objc_msgSend$LockScreenStateChanging:
+ _objc_msgSend$MotionStateChanging:
+ _objc_msgSend$canActiveOperationBeEnded
+ _objc_msgSend$canDeliverPollingEvent
+ _objc_msgSend$canOperationBeEndedForClient
+ _objc_msgSend$initWithCallbackQueue:observer:
+ _objc_msgSend$isDeviceOnLockScreen
+ _objc_msgSend$isDeviceStationary
+ _objc_msgSend$lockScreenStateChanging:
+ _objc_msgSend$motionActivityChanging:
+ _objc_msgSend$operationEndableCallback
+ _objc_msgSend$pollingFilter
+ _objc_msgSend$setOperationEndableCallback:
+ _objc_msgSend$startActivityUpdatesToQueue:withHandler:
+ _objc_msgSend$stationary
+ _sharedManager.manager.1072
+ _sharedManager.onceToken.1070
- GCC_except_table104
- GCC_except_table105
- GCC_except_table154
- GCC_except_table155
- GCC_except_table159
- GCC_except_table166
- GCC_except_table184
- GCC_except_table186
- GCC_except_table209
- GCC_except_table213
- GCC_except_table242
- GCC_except_table264
- GCC_except_table309
- GCC_except_table315
- GCC_except_table329
- GCC_except_table373
- GCC_except_table374
- GCC_except_table40
- GCC_except_table42
- GCC_except_table443
- GCC_except_table449
- GCC_except_table454
- GCC_except_table458
- GCC_except_table462
- GCC_except_table467
- GCC_except_table471
- GCC_except_table475
- GCC_except_table542
- GCC_except_table566
- GCC_except_table642
- GCC_except_table70
- GCC_except_table767
- GCC_except_table792
- GCC_except_table796
- GCC_except_table800
- GCC_except_table803
- GCC_except_table805
- GCC_except_table807
- GCC_except_table808
- GCC_except_table820
- GCC_except_table831
- GCC_except_table833
- __OBJC_$_PROP_LIST_NSObject.1715
- __OBJC_$_PROP_LIST_NSObject.2135
- __OBJC_$_PROP_LIST_NSObject.342
- __OBJC_$_PROP_LIST_NSObject.477
- __OBJC_$_PROP_LIST_NSObject.739
- __OBJC_$_PROP_LIST_NSObject.988
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFoundationReceiving.1183
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFoundationUnitTestEventReceiving.1184
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWAttentionAwareService.740
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWFrameworkClient.2136
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWRemoteClient.741
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWUnitTestSampler.1533
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1716
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2137
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.343
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.478
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.742
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.989
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDeviceDelegate.344
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDevicePearlDelegate.345
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKFaceDetectOperationDelegate.346
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKOperationDelegate.347
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1717
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2138
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.348
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.479
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.743
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.990
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SamplingOperation.349
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_StreamingOperation.1185
- __OBJC_$_PROTOCOL_METHOD_TYPES_AVFoundationReceiving.1186
- __OBJC_$_PROTOCOL_METHOD_TYPES_AVFoundationUnitTestEventReceiving.1187
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWAttentionAwareService.744
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWFrameworkClient.2139
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWRemoteClient.745
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWUnitTestSampler.1534
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKDeviceDelegate.350
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKDevicePearlDelegate.351
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKFaceDetectOperationDelegate.352
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKOperationDelegate.353
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1718
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2140
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.354
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.480
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.746
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.991
- __OBJC_$_PROTOCOL_METHOD_TYPES_SamplingOperation.355
- __OBJC_$_PROTOCOL_METHOD_TYPES_StreamingOperation.1188
- __OBJC_$_PROTOCOL_REFS_AWFrameworkClient.2141
- __OBJC_$_PROTOCOL_REFS_BKDeviceDelegate.356
- __OBJC_$_PROTOCOL_REFS_BKDevicePearlDelegate.357
- __OBJC_$_PROTOCOL_REFS_BKFaceDetectOperationDelegate.358
- __OBJC_$_PROTOCOL_REFS_BKOperationDelegate.359
- ___31-[AWScheduler initWithOptions:]_block_invoke.68
- ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.84
- ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.87
- ___67-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:]_block_invoke.53
- ___Block_byref_object_copy_.1014
- ___Block_byref_object_copy_.1380
- ___Block_byref_object_copy_.1758
- ___Block_byref_object_copy_.2034
- ___Block_byref_object_copy_.562
- ___Block_byref_object_copy_.672
- ___Block_byref_object_dispose_.1015
- ___Block_byref_object_dispose_.1381
- ___Block_byref_object_dispose_.1759
- ___Block_byref_object_dispose_.2035
- ___Block_byref_object_dispose_.563
- ___Block_byref_object_dispose_.673
- ___block_literal_global.1036
- ___block_literal_global.1318
- ___block_literal_global.136
- ___block_literal_global.1397
- ___block_literal_global.1775
- ___block_literal_global.206
- ___block_literal_global.2065
- ___block_literal_global.2379
- ___block_literal_global.296
- ___block_literal_global.41
- ___block_literal_global.442
- ___block_literal_global.670
- ___block_literal_global.847
- ___block_literal_global.956
- ___getPearlDevice_block_invoke.301
- _getPearlDevice.onceToken.295
- _getPearlDevice.result.297
- _sharedManager.manager.1037
- _sharedManager.onceToken.1035
CStrings:
+ "\x013\xc1"
+ "%30s:%-4d: %13.5f:  Info: Device %s on lock screen"
+ "%30s:%-4d: %13.5f:  Info: Device %s stationary"
+ "-[LockScreenStateObserver initWithCallbackQueue:observer:]"
+ "-[MotionActivityObserver initWithCallbackQueue:observer:]"
+ "<%@: %p> (identifier: %@ samplingInterval: %13.5f samplingDelay: %13.5f sampleWhileAbsent: %s retroactiveTimeoutMode: %s pollingFilter: %s continuousFaceDetectMode: %s unityStream: %s activateEyeRelief: %s activateAttentionDetection: %s activateMotionDetection: %s attentionLostTimeouts: %@ notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ tagIndex %llu)"
+ "<%@: %p> (identifier: %@ samplingInterval: %13.5f samplingDelay: %13.5f sampleWhileAbsent: %s retroactiveTimeoutMode: %s, pollingFilter: %s, continuousFaceDetectMode: %s, activateAttentionDetection: %s, activateEyeRelief: %s, activateMotionDetection: %s, unityStream: %s, attentionLostTimeouts: %@ notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ %@)"
+ "@\"<LockScreenStateObserving>\""
+ "@\"<MotionActivityObserving>\""
+ "@\"CMMotionActivityManager\""
+ "@\"LockScreenStateObserver\""
+ "@\"MotionActivityObserver\""
+ "@\"NSOperationQueue\""
+ "B8@?0"
+ "IS"
+ "IS NOT"
+ "LockScreenStateChanging:"
+ "LockScreenStateObserver"
+ "LockScreenStateObserver.m"
+ "LockScreenStateObserving"
+ "MotionActivityObserver"
+ "MotionActivityObserver.m"
+ "MotionActivityObserving"
+ "MotionStateChanging:"
+ "T@?,C,V_operationEndableCallback"
+ "TB,N,V_pollingFilter"
+ "TB,R,N,V_isDeviceOnLockScreen"
+ "TB,R,N,V_isDeviceStationary"
+ "_callbackQueue"
+ "_filteredPollingEventDelivered"
+ "_isDeviceOnLockScreen"
+ "_isDeviceStationary"
+ "_lockScreenStateObserver"
+ "_lockToken"
+ "_motionActivityManager"
+ "_motionActivityObserver"
+ "_operationEndableCallback"
+ "_operationQueue"
+ "_pollingFilter"
+ "callbackQueue != nil"
+ "canActiveOperationBeEnded"
+ "canDeliverPollingEvent"
+ "canOperationBeEndedForClient"
+ "com.apple.springboard.lockstate"
+ "initWithCallbackQueue:observer:"
+ "isDeviceOnLockScreen"
+ "isDeviceStationary"
+ "lockScreenStateChanging:"
+ "motionActivityChanging:"
+ "observer != nil"
+ "operationEndableCallback"
+ "pollingFilter"
+ "setOperationEndableCallback:"
+ "setPollingFilter:"
+ "startActivityUpdatesToQueue:withHandler:"
+ "stationary"
+ "v16@?0@\"CMMotionActivity\"8"
- "\x012\xc1"
- "<%@: %p> (identifier: %@ samplingInterval: %13.5f samplingDelay: %13.5f sampleWhileAbsent: %s retroactiveTimeoutMode: %s continuousFaceDetectMode: %s unityStream: %s activateEyeRelief: %s activateAttentionDetection: %s activateMotionDetection: %s attentionLostTimeouts: %@ notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ tagIndex %llu)"
- "<%@: %p> (identifier: %@ samplingInterval: %13.5f samplingDelay: %13.5f sampleWhileAbsent: %s retroactiveTimeoutMode: %s, continuousFaceDetectMode: %s, activateAttentionDetection: %s, activateEyeRelief: %s, activateMotionDetection: %s, unityStream: %s, attentionLostTimeouts: %@ notificationMask %@ mask %@ attentionLostEventMask %@ digitizerDisplayUUIDs %@ buttonDisplayUUIDs %@ keyboardDisplayUUIDs %@ %@)"

```
