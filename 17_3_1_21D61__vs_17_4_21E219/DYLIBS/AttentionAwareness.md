## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-137.60.2.0.0
-  __TEXT.__text: 0x2a904
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_methlist: 0x1a70
+158.100.2.0.0
+  __TEXT.__text: 0x2c208
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x1ae0
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x598
-  __TEXT.__cstring: 0x2c5d
-  __TEXT.__oslogstring: 0x396f
-  __TEXT.__unwind_info: 0xa90
+  __TEXT.__gcc_except_tab: 0x520
+  __TEXT.__cstring: 0x31cf
+  __TEXT.__oslogstring: 0x3ba2
+  __TEXT.__unwind_info: 0xab4
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x40c
-  __TEXT.__objc_methname: 0x40fc
-  __TEXT.__objc_methtype: 0x1200
-  __TEXT.__objc_stubs: 0x35e0
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0xc90
+  __TEXT.__objc_methname: 0x4350
+  __TEXT.__objc_methtype: 0x1212
+  __TEXT.__objc_stubs: 0x3740
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4ed8
-  __DATA_CONST.__objc_selrefs: 0xf98
-  __AUTH_CONST.__const: 0x388
-  __AUTH_CONST.__cfstring: 0x15a0
+  __DATA_CONST.__objc_const: 0x5048
+  __DATA_CONST.__objc_selrefs: 0xff0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __AUTH_CONST.__const: 0x3c8
+  __AUTH_CONST.__cfstring: 0x1a00
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x458
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x178
-  __DATA.__objc_superrefs: 0xc8
-  __DATA.__objc_ivar: 0x3d0
-  __DATA.__data: 0x780
+  __DATA.__objc_ivar: 0x3ec
+  __DATA.__data: 0x788
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 780
-  Symbols:   2948
-  CStrings:  1621
+  Functions: 793
+  Symbols:   3003
+  CStrings:  1693
 
Symbols:
+ -[AWAttentionAwareService addClient:clientConfig:clientIndex:clientId:unitTestMode:reply:subscribeForStreamingEvents:]
+ -[AWAttentionSampler lastAttentionScore]
+ -[AWAttentionSampler lastFaceDetectionScore]
+ -[AWAttentionSampler setLastAttentionScore:]
+ -[AWAttentionSampler setLastFaceDetectionScore:]
+ -[AWAttentionStreamer streamEventsWithMask:block:options:operationStartFailedBlock:]
+ -[AWFaceDetectAttentionEvent attentionScore]
+ -[AWFaceDetectAttentionEvent faceDetectionScore]
+ -[AWPearlAttentionStreamer streamEventWithBlock:options:operationStartFailedBlock:]
+ -[AWRemoteClient clientId]
+ -[AWRemoteClient initWithProxy:connection:clientConfig:clientIndex:clientId:scheduler:error:]
+ -[AWRemoteClient invalidateWithoutQueue]
+ -[AWScheduler resetInterruptedStreamingClientWithIdentifier:]
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table137
+ GCC_except_table155
+ GCC_except_table157
+ GCC_except_table184
+ GCC_except_table213
+ GCC_except_table235
+ GCC_except_table268
+ GCC_except_table353
+ GCC_except_table359
+ GCC_except_table364
+ GCC_except_table368
+ GCC_except_table372
+ GCC_except_table377
+ GCC_except_table381
+ GCC_except_table385
+ GCC_except_table41
+ GCC_except_table452
+ GCC_except_table476
+ GCC_except_table552
+ GCC_except_table677
+ GCC_except_table706
+ GCC_except_table710
+ GCC_except_table713
+ GCC_except_table718
+ GCC_except_table735
+ GCC_except_table741
+ GCC_except_table743
+ GCC_except_table75
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_AWAttentionAwarenessClient._clientId
+ _OBJC_IVAR_$_AWAttentionAwarenessClient._streamingRunning
+ _OBJC_IVAR_$_AWAttentionSampler._lastAttentionScore
+ _OBJC_IVAR_$_AWAttentionSampler._lastFaceDetectionScore
+ _OBJC_IVAR_$_AWFaceDetectAttentionEvent._attentionScore
+ _OBJC_IVAR_$_AWFaceDetectAttentionEvent._faceDetectionScore
+ _OBJC_IVAR_$_AWPearlAttentionStreamer._activeOperationNotification
+ _OBJC_IVAR_$_AWPearlAttentionStreamer._matchOrEnrollOperationActive
+ _OBJC_IVAR_$_AWRemoteClient._clientId
+ __OBJC_$_PROP_LIST_NSObject.1328
+ __OBJC_$_PROP_LIST_NSObject.1736
+ __OBJC_$_PROP_LIST_NSObject.254
+ __OBJC_$_PROP_LIST_NSObject.380
+ __OBJC_$_PROP_LIST_NSObject.627
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWAttentionAwareService.628
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWFrameworkClient.1737
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWRemoteClient.629
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWUnitTestSampler.1149
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1329
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1738
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.255
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.381
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.630
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDeviceDelegate.256
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDevicePearlDelegate.257
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKFaceDetectOperationDelegate.258
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKOperationDelegate.259
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1330
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1739
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.260
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.382
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.631
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWAttentionAwareService.632
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWFrameworkClient.1740
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWRemoteClient.633
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AWUnitTestSampler.1150
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKDeviceDelegate.261
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKDevicePearlDelegate.262
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKFaceDetectOperationDelegate.263
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKOperationDelegate.264
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1331
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1741
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.265
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.383
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.634
+ __OBJC_$_PROTOCOL_REFS_AWFrameworkClient.1742
+ __OBJC_$_PROTOCOL_REFS_BKDeviceDelegate.266
+ __OBJC_$_PROTOCOL_REFS_BKDevicePearlDelegate.267
+ __OBJC_$_PROTOCOL_REFS_BKFaceDetectOperationDelegate.268
+ __OBJC_$_PROTOCOL_REFS_BKOperationDelegate.269
+ ___118-[AWAttentionAwareService addClient:clientConfig:clientIndex:clientId:unitTestMode:reply:subscribeForStreamingEvents:]_block_invoke
+ ___40-[AWRemoteClient invalidateWithoutQueue]_block_invoke
+ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.75
+ ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.78
+ ___50-[AWPearlAttentionStreamer initForUnitTest:queue:]_block_invoke.16
+ ___50-[AWPearlAttentionStreamer initForUnitTest:queue:]_block_invoke_2.17
+ ___54-[AWUnitTestFaceDetectOperation startStreamWithError:]_block_invoke_2
+ ___79-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:displayUUID:]_block_invoke.53
+ ___83-[AWPearlAttentionStreamer streamEventWithBlock:options:operationStartFailedBlock:]_block_invoke
+ ___83-[AWPearlAttentionStreamer streamEventWithBlock:options:operationStartFailedBlock:]_block_invoke.36
+ ___Block_byref_object_copy_.1001
+ ___Block_byref_object_copy_.1368
+ ___Block_byref_object_copy_.1644
+ ___Block_byref_object_copy_.455
+ ___Block_byref_object_copy_.565
+ ___Block_byref_object_copy_.765
+ ___Block_byref_object_dispose_.1002
+ ___Block_byref_object_dispose_.1369
+ ___Block_byref_object_dispose_.1645
+ ___Block_byref_object_dispose_.456
+ ___Block_byref_object_dispose_.566
+ ___Block_byref_object_dispose_.766
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_78_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___block_literal_global.1017
+ ___block_literal_global.130
+ ___block_literal_global.1386
+ ___block_literal_global.1670
+ ___block_literal_global.171
+ ___block_literal_global.1942
+ ___block_literal_global.216
+ ___block_literal_global.242
+ ___block_literal_global.247
+ ___block_literal_global.258
+ ___block_literal_global.270
+ ___block_literal_global.273
+ ___block_literal_global.346
+ ___block_literal_global.56
+ ___block_literal_global.563
+ ___block_literal_global.739
+ ___block_literal_global.77
+ ___block_literal_global.786
+ ___block_literal_global.945
+ ___getPearlDevice_block_invoke.221
+ ___isPearlDisabledViaAccessibility_block_invoke.277
+ ___registerForPrefsChange_block_invoke.248
+ ___registerForPrefsChange_block_invoke_2.251
+ __os_signpost_emit_with_name_impl
+ _getPearlDevice.onceToken.215
+ _getPearlDevice.result
+ _getPearlDevice.result.217
+ _objc_msgSend$UUID
+ _objc_msgSend$addClient:clientConfig:clientIndex:clientId:unitTestMode:reply:subscribeForStreamingEvents:
+ _objc_msgSend$attentionScore
+ _objc_msgSend$clientId
+ _objc_msgSend$faceDetectionScore
+ _objc_msgSend$initWithProxy:connection:clientConfig:clientIndex:clientId:scheduler:error:
+ _objc_msgSend$invalidateWithoutQueue
+ _objc_msgSend$lastAttentionScore
+ _objc_msgSend$lastFaceDetectionScore
+ _objc_msgSend$motionDetect
+ _objc_msgSend$resetInterruptedStreamingClientWithIdentifier:
+ _objc_msgSend$setLastAttentionScore:
+ _objc_msgSend$setLastFaceDetectionScore:
+ _objc_msgSend$streamEventWithBlock:options:operationStartFailedBlock:
+ _objc_msgSend$streamEventsWithMask:block:options:operationStartFailedBlock:
+ _objc_opt_respondsToSelector
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _sharedManager.manager.787
+ _sharedManager.onceToken.785
- -[AWAttentionAwareService addClient:clientConfig:clientIndex:unitTestMode:reply:subscribeForStreamingEvents:]
- -[AWAttentionStreamer streamEventsWithMask:block:options:]
- -[AWPearlAttentionStreamer streamEventWithBlock:options:]
- -[AWRemoteClient initWithProxy:connection:clientConfig:clientIndex:scheduler:error:]
- GCC_except_table122
- GCC_except_table123
- GCC_except_table127
- GCC_except_table134
- GCC_except_table152
- GCC_except_table154
- GCC_except_table176
- GCC_except_table209
- GCC_except_table229
- GCC_except_table262
- GCC_except_table343
- GCC_except_table349
- GCC_except_table354
- GCC_except_table358
- GCC_except_table362
- GCC_except_table367
- GCC_except_table371
- GCC_except_table375
- GCC_except_table39
- GCC_except_table442
- GCC_except_table466
- GCC_except_table541
- GCC_except_table664
- GCC_except_table689
- GCC_except_table69
- GCC_except_table693
- GCC_except_table697
- GCC_except_table700
- GCC_except_table704
- GCC_except_table705
- GCC_except_table722
- GCC_except_table74
- _OBJC_IVAR_$_AWPearlAttentionStreamer._sem
- _OBJC_IVAR_$_AWScheduler._userDefaults
- __OBJC_$_PROP_LIST_NSObject.1238
- __OBJC_$_PROP_LIST_NSObject.1609
- __OBJC_$_PROP_LIST_NSObject.240
- __OBJC_$_PROP_LIST_NSObject.362
- __OBJC_$_PROP_LIST_NSObject.588
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWAttentionAwareService.589
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWFrameworkClient.1610
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWRemoteClient.590
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AWUnitTestSampler.1064
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1239
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1611
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.241
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.363
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.591
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDeviceDelegate.242
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDevicePearlDelegate.243
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKFaceDetectOperationDelegate.244
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKOperationDelegate.245
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1240
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1612
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.246
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.364
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.592
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWAttentionAwareService.593
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWFrameworkClient.1613
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWRemoteClient.594
- __OBJC_$_PROTOCOL_METHOD_TYPES_AWUnitTestSampler.1065
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKDeviceDelegate.247
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKDevicePearlDelegate.248
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKFaceDetectOperationDelegate.249
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKOperationDelegate.250
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1241
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1614
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.251
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.365
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.595
- __OBJC_$_PROTOCOL_REFS_AWFrameworkClient.1615
- __OBJC_$_PROTOCOL_REFS_BKDeviceDelegate.252
- __OBJC_$_PROTOCOL_REFS_BKDevicePearlDelegate.253
- __OBJC_$_PROTOCOL_REFS_BKFaceDetectOperationDelegate.254
- __OBJC_$_PROTOCOL_REFS_BKOperationDelegate.255
- ___109-[AWAttentionAwareService addClient:clientConfig:clientIndex:unitTestMode:reply:subscribeForStreamingEvents:]_block_invoke
- ___49-[AWScheduler streamFaceDetectEventsWithOptions:]_block_invoke.69
- ___50-[AWPearlAttentionStreamer initForUnitTest:queue:]_block_invoke_7
- ___57-[AWPearlAttentionStreamer streamEventWithBlock:options:]_block_invoke
- ___79-[AWAttentionAwareService processHIDEvent:mask:timestamp:senderID:displayUUID:]_block_invoke.44
- ___Block_byref_object_copy_.1282
- ___Block_byref_object_copy_.1532
- ___Block_byref_object_copy_.293
- ___Block_byref_object_copy_.453
- ___Block_byref_object_copy_.532
- ___Block_byref_object_copy_.702
- ___Block_byref_object_copy_.926
- ___Block_byref_object_dispose_.1283
- ___Block_byref_object_dispose_.1533
- ___Block_byref_object_dispose_.294
- ___Block_byref_object_dispose_.454
- ___Block_byref_object_dispose_.533
- ___Block_byref_object_dispose_.703
- ___Block_byref_object_dispose_.927
- ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12ls32l8r40l8r48l8
- ___block_descriptor_70_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_literal_global.126
- ___block_literal_global.1300
- ___block_literal_global.1551
- ___block_literal_global.160
- ___block_literal_global.1804
- ___block_literal_global.240
- ___block_literal_global.245
- ___block_literal_global.256
- ___block_literal_global.268
- ___block_literal_global.271
- ___block_literal_global.327
- ___block_literal_global.52
- ___block_literal_global.530
- ___block_literal_global.680
- ___block_literal_global.721
- ___block_literal_global.867
- ___block_literal_global.944
- ___isPearlDisabledViaAccessibility_block_invoke.275
- ___registerForPrefsChange_block_invoke.246
- ___registerForPrefsChange_block_invoke_2.249
- _objc_msgSend$addClient:clientConfig:clientIndex:unitTestMode:reply:subscribeForStreamingEvents:
- _objc_msgSend$initWithProxy:connection:clientConfig:clientIndex:scheduler:error:
- _objc_msgSend$streamEventWithBlock:options:
- _objc_msgSend$streamEventsWithMask:block:options:
- _sharedManager.manager.722
- _sharedManager.onceToken.720
CStrings:
+ "\x012\xc1"
+ "\x03'!"
+ "\x04U\"\x11!"
+ "\x05\x11"
+ "\a1"
+ " Attention Aware Features turned OFF"
+ " Attention streamer not running"
+ " Cannot resume client if it isn't already suspended"
+ " Client already active"
+ " Client is already invalid"
+ " Client is not running in streaming mode"
+ " Client not allowed to crash the process"
+ " Client not entitled to unit test access"
+ " Client not entitled to use continuousFaceDetectMode"
+ " Client not entitled to use crash the process"
+ " Client not entitled to use motionDetect"
+ " Client not entitled to use pollWithTimeout"
+ " Client not entitled to use sampleWhileAbsent"
+ " Device doesn't support Pearl"
+ " Display OFF"
+ " Invalid config"
+ " Invalid mask to start a stream"
+ " Match or enroll operation ongoing"
+ " NIL identifer not allowed"
+ " No attention streamer found"
+ " No metadata selected"
+ " Not connected to server"
+ " Not creating client with nil identifier"
+ " Pearl is in error state"
+ " Platform doesn't support Motion detect"
+ " Polling already going on"
+ " Polling was cancelled"
+ " Smart cover closed"
+ " Streamer not running"
+ " Timeout less than 0 is invalid"
+ " Unable to fetch scheduler"
+ " Unable to get a suitable scheduler for client"
+ " Unable to start presence detect operation"
+ "!client.invalid"
+ "%30s:%-4d: %13.5f:  Info: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ attentionScore: %@faceDetectionScore: %@isCameraObstructed: %d"
+ "%30s:%-4d: %13.5f:  Info: Attention Aware Features set to %s"
+ "%30s:%-4d: %13.5f:  Info: Match or enroll operation initiated when a stream was running, cancelling stream and sending a notification to clients"
+ "%30s:%-4d: %13.5f:  Info: UNIT TEST: delivering %s event on queue %@ to %@"
+ "%30s:%-4d: %13.5f: Debug: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ distance: %@ eyeReliefFaceState:%@ frameNumber: %@attentionScore: %ffaceDetectionScore: %fisCameraObstructed: %d"
+ "%30s:%-4d: %13.5f: Debug: Pearl disabled via accessibility; disabling FaceDetect"
+ "%30s:%-4d: %13.5f: Debug: User toggled the Attention Aware Features flag to %s"
+ "%30s:%-4d: %13.5f: Error: Error %@ when starting streaming operation from BioKit"
+ "%30s:%-4d: %13.5f: Error: Match or enroll operation underway, not starting attention stream"
+ "-[AWAttentionAwareService addClient:clientConfig:clientIndex:clientId:unitTestMode:reply:subscribeForStreamingEvents:]_block_invoke"
+ "<%@: %p> (timestamp: %13.5f metadataValid %u pitch %13.5f yaw %13.5f roll %13.5f orientation %@ distance %13.5f faceState: %@ frameNumber: %13.5f metadataType: %@ motionData: %@ attentionScore: %13.5f faceDetectionScore: %13.5f isCameraObstructed: %u %@)"
+ "@\"NSError\"34@0:8@?<v@?@\"AWAttentionEvent\">16{?=BB}24@?<v@?@\"NSError\">26"
+ "@\"NSUUID\""
+ "@34@0:8@?16{?=BB}24@?26"
+ "@40@0:8d16Q24^{AWFaceDetectMetadata=BdddQdQdQ[16f]ffB}32"
+ "@42@0:8Q16@?24{?=BB}32@?34"
+ "@68@0:8@16@24@32i40@44@52^@60"
+ "AA: Face detect failed"
+ "AA: Face detect started"
+ "AA: Face detect success"
+ "AA: Motion detect started"
+ "AA: Motion detect success"
+ "AA: Streaming event received"
+ "AttentionAwareService.m"
+ "B56@0:8^{__IOHIDEvent=}16Q24^(?={AWFaceDetectMetadata=BdddQdQdQ[16f]ffB}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32Q40@48"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUUID\",R,N,V_clientId"
+ "Tf,N,V_lastAttentionScore"
+ "Tf,N,V_lastFaceDetectionScore"
+ "Tf,R,N,V_attentionScore"
+ "Tf,R,N,V_faceDetectionScore"
+ "UUID"
+ "_activeOperationNotification"
+ "_attentionScore"
+ "_clientId"
+ "_faceDetectionScore"
+ "_lastAttentionScore"
+ "_lastFaceDetectionScore"
+ "_matchOrEnrollOperationActive"
+ "_streamingRunning"
+ "addClient:clientConfig:clientIndex:clientId:unitTestMode:reply:subscribeForStreamingEvents:"
+ "attentionScore"
+ "clientId"
+ "com.apple.BiometricKit.activeOperation"
+ "f"
+ "f16@0:8"
+ "faceDetectionScore"
+ "initWithProxy:connection:clientConfig:clientIndex:clientId:scheduler:error:"
+ "invalidateWithoutQueue"
+ "lastAttentionScore"
+ "lastFaceDetectionScore"
+ "motionDetect"
+ "resetInterruptedStreamingClientWithIdentifier:"
+ "setLastAttentionScore:"
+ "setLastFaceDetectionScore:"
+ "streamEventWithBlock:options:operationStartFailedBlock:"
+ "streamEventsWithMask:block:options:operationStartFailedBlock:"
+ "v20@0:8f16"
+ "v28@0:8i16^{AWFaceDetectMetadata=BdddQdQdQ[16f]ffB}20"
+ "v36@0:8i16^(?={AWFaceDetectMetadata=BdddQdQdQ[16f]ffB}iii)20@28"
+ "v40@0:8Q16Q24^(?={AWFaceDetectMetadata=BdddQdQdQ[16f]ffB}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32"
+ "v60@0:8@\"<AWFrameworkClient>\"16@\"AWAttentionAwarenessConfiguration\"24i32@\"NSUUID\"36B44@?<v@?@\"<AWRemoteClient>\"i@\"NSError\">48B56"
+ "v60@0:8@16@24i32@36B44@?48B56"
- "\x01\"\xc1"
- "\x03'"
- "\x04U\"\x11"
- "\x05\x111"
- "\a\x11!"
- "%30s:%-4d: %13.5f:  Info: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ isCameraObstructed: %d"
- "%30s:%-4d: %13.5f:  Info: Pearl disabled via accessibility; disabling FaceDetect"
- "%30s:%-4d: %13.5f:  Info: UNIT TEST: delivering %s event"
- "%30s:%-4d: %13.5f:  Info: User toggled the Attention Aware Features flag to %s"
- "%30s:%-4d: %13.5f:  Info: pearlDisabledViaAccessibility set to %s"
- "%30s:%-4d: %13.5f: Debug: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ distance: %@ eyeReliefFaceState:%@ frameNumber: %@ isCameraObstructed: %d"
- "<%@: %p> (timestamp: %13.5f metadataValid %u pitch %13.5f yaw %13.5f roll %13.5f orientation %@ distance %13.5f faceState: %@ frameNumber: %13.5f metadataType: %@ motionData: %@ isCameraObstructed: %u %@)"
- "@\"NSError\"26@0:8@?<v@?@\"AWAttentionEvent\">16{?=BB}24"
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSUserDefaults\""
- "@26@0:8@?16{?=BB}24"
- "@28@0:8@16i24"
- "@34@0:8Q16@?24{?=BB}32"
- "@40@0:8d16Q24^{AWFaceDetectMetadata=BdddQdQdQ[16f]B}32"
- "@60@0:8@16@24@32i40@44^@52"
- "B56@0:8^{__IOHIDEvent=}16Q24^(?={AWFaceDetectMetadata=BdddQdQdQ[16f]B}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32Q40@48"
- "_sem"
- "_userDefaults"
- "addClient:clientConfig:clientIndex:unitTestMode:reply:subscribeForStreamingEvents:"
- "initWithProxy:connection:clientConfig:clientIndex:scheduler:error:"
- "streamEventWithBlock:options:"
- "streamEventsWithMask:block:options:"
- "v28@0:8i16^{AWFaceDetectMetadata=BdddQdQdQ[16f]B}20"
- "v36@0:8i16^(?={AWFaceDetectMetadata=BdddQdQdQ[16f]B}iii)20@28"
- "v40@0:8Q16Q24^(?={AWFaceDetectMetadata=BdddQdQdQ[16f]B}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32"
- "v52@0:8@\"<AWFrameworkClient>\"16@\"AWAttentionAwarenessConfiguration\"24i32B36@?<v@?@\"<AWRemoteClient>\"i@\"NSError\">40B48"
- "v52@0:8@16@24i32B36@?40B48"

```
