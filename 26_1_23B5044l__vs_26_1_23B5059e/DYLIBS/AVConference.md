## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2175.9.2.0.0
-  __TEXT.__text: 0x796360
-  __TEXT.__auth_stubs: 0x5620
-  __TEXT.__objc_methlist: 0x35bc0
+2175.12.1.0.0
+  __TEXT.__text: 0x797700
+  __TEXT.__auth_stubs: 0x5630
+  __TEXT.__objc_methlist: 0x35c28
   __TEXT.__const: 0xc780
-  __TEXT.__cstring: 0x8f509
-  __TEXT.__oslogstring: 0x10f1f7
+  __TEXT.__cstring: 0x8f85a
+  __TEXT.__oslogstring: 0x10f5e1
   __TEXT.__gcc_except_tab: 0x2aac
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x10898
+  __TEXT.__unwind_info: 0x108c0
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7dda0
-  __TEXT.__objc_methtype: 0x282af
-  __TEXT.__objc_stubs: 0x4ee80
+  __TEXT.__objc_methname: 0x7df42
+  __TEXT.__objc_methtype: 0x282e0
+  __TEXT.__objc_stubs: 0x4ef20
   __DATA_CONST.__got: 0x1a60
-  __DATA_CONST.__const: 0x6b10
+  __DATA_CONST.__const: 0x6b38
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x169e8
+  __DATA_CONST.__objc_selrefs: 0x16a10
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
-  __AUTH_CONST.__auth_got: 0x2b28
+  __AUTH_CONST.__auth_got: 0x2b30
   __AUTH_CONST.__const: 0x3c88
-  __AUTH_CONST.__cfstring: 0x26400
-  __AUTH_CONST.__objc_const: 0x63770
+  __AUTH_CONST.__cfstring: 0x26480
+  __AUTH_CONST.__objc_const: 0x63870
   __AUTH_CONST.__objc_intobj: 0x4a10
   __AUTH_CONST.__objc_arrayobj: 0x1b48
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x6c90
+  __DATA.__objc_ivar: 0x6cb0
   __DATA.__data: 0x78b0
   __DATA.__bss: 0xd78
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8517BE3D-B554-3DDC-934E-BE1559312E5D
-  Functions: 31600
-  Symbols:   97446
-  CStrings:  57261
+  UUID: 3DFD4134-1C4B-3EEA-9E63-27BE92A89B00
+  Functions: 31615
+  Symbols:   97499
+  CStrings:  57300
 
Symbols:
+ +[AVCAuditToken currentProcessToken]
+ -[AVCAuditToken isEqual:]
+ -[AVCRateController triggerDeferredDelegateCallbacks]
+ -[AVConferenceXPCServer appendClientAuditTokenToDictionary:clientAuditToken:]
+ -[VCAVFoundationCapture cameraFormatForWidthWithList:height:frameRate:formatList:].cold.1
+ -[VCAVFoundationCapture cameraFormatForWidthWithList:height:frameRate:formatList:].cold.2
+ -[VCAudioCaptionsSpeechTranslator addToCaptionTasksWithError:]
+ -[VCAudioCaptionsSpeechTranslator addToCaptionTasksWithError:].cold.1
+ -[VCAudioCaptionsSpeechTranslator addToCaptionTasksWithError:].cold.2
+ -[VCMediaStream initializeTransportSessionWithLocalNWEnpoint:clientAuditToken:error:]
+ -[VCMediaStream initializeTransportSessionWithLocalNWEnpoint:clientAuditToken:error:].cold.1
+ -[VCMediaStream setUpRTPWithLocalNWEndpoint:error:].cold.4
+ -[VCMediaStreamManager capabilitiesForStream:mediaProtocolArgs:xpcArguments:clientAuditToken:error:]
+ -[VCMediaStreamManager newMediaProtocolArgsWithMediaProtocolArgs:nwEndpoint:clientAuditToken:]
+ -[VCRateControlMLEnrollment cleanupTrainingDataFiles]
+ -[VCRateControlMLEnrollment removeFileAtPath:]
+ -[VCRateControlMLEnrollment removeFileAtPath:].cold.1
+ -[VCTransportSessionMultiLink initWithLocalEndpoint:clientAuditToken:handlerQueue:context:eventHandler:options:error:]
+ -[VCTransportSessionMultiLink initWithLocalEndpoint:clientAuditToken:handlerQueue:context:eventHandler:options:error:].cold.1
+ -[VCTransportSessionMultiLink initWithLocalEndpoint:clientAuditToken:handlerQueue:context:eventHandler:options:error:].cold.2
+ GCC_except_table87
+ _OBJC_IVAR_$_AVCRateController._isDelegateCallbackDeferralEnabled
+ _OBJC_IVAR_$_AVCRateController._isProbingSequenceRequestCallbackDeferred
+ _OBJC_IVAR_$_AVCRateController._isTargetBitrateChangedCallbackDeferred
+ _OBJC_IVAR_$_AVCRateController._probingSequenceID
+ _OBJC_IVAR_$_AVCRateController._probingSequenceSize
+ _OBJC_IVAR_$_AVCStatisticsCollector._processCompletionHandler
+ _OBJC_IVAR_$_AVCStatisticsCollector._processCompletionHandlerLock
+ _OBJC_IVAR_$_VCTransportSessionMultiLink._clientAuditToken
+ _VCStatisticsCollector_SetProcessCompleteHandler
+ _VCUtil_AuditTokenEqual
+ __AVCStatisticsCollector_SetProcessCompleteHandler
+ __VCAVFoundationCapture_maxFrameRateOfVideoDeviceFormat
+ ___26-[AVCRateController start]_block_invoke_2
+ ___28-[VCSession dispatchedStart]_block_invoke.611
+ ___28-[VCSession dispatchedStart]_block_invoke.612
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.203
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.204
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.204.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.231
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.231.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.231.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.234
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248.cold.3
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248.cold.4
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.276
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.290
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.290.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.290.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.298
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.298.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.298.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.303
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.318
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.334
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.334.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.349
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.360
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.360.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.367
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.367.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.374
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.374.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.381
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.381.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.388
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.388.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.395
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.395.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.402
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.402.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.409
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.420
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.431
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.433
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.441
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.307
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.326
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.353
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.353.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.416
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.416.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.427
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.427.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.439
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.311
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.311.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.328
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.328.cold.1
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.606
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.607
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.608
+ ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.624
+ ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.623
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.203
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.223
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.225
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.232
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.251
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.256
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.264
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.271
+ ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.278
+ ___64-[VCMediaStream handleMediaCallbackNotification:inData:outData:]_block_invoke.237
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.225
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.225.cold.1
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.225.cold.2
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.225.cold.3
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.225.cold.4
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.226
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.233
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.235
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke_2.227
+ ___block_descriptor_40_e8_32o_e518_v16?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBdIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
+ ___block_literal_global.279
+ ___block_literal_global.305
+ ___block_literal_global.309
+ ___block_literal_global.313
+ ___block_literal_global.320
+ ___block_literal_global.336
+ ___block_literal_global.351
+ ___block_literal_global.355
+ ___block_literal_global.369
+ ___block_literal_global.376
+ ___block_literal_global.383
+ ___block_literal_global.390
+ ___block_literal_global.397
+ ___block_literal_global.404
+ ___block_literal_global.411
+ ___block_literal_global.418
+ ___block_literal_global.422
+ ___block_literal_global.429
+ ___block_literal_global.437
+ _nw_parameters_set_source_application
+ _objc_msgSend$addToCaptionTasksWithError:
+ _objc_msgSend$appendClientAuditTokenToDictionary:clientAuditToken:
+ _objc_msgSend$capabilitiesForStream:mediaProtocolArgs:xpcArguments:clientAuditToken:error:
+ _objc_msgSend$cleanupTrainingDataFiles
+ _objc_msgSend$currentProcessToken
+ _objc_msgSend$initWithAuditToken:
+ _objc_msgSend$initWithLocalEndpoint:clientAuditToken:handlerQueue:context:eventHandler:options:error:
+ _objc_msgSend$initializeTransportSessionWithLocalNWEnpoint:clientAuditToken:error:
+ _objc_msgSend$newMediaProtocolArgsWithMediaProtocolArgs:nwEndpoint:clientAuditToken:
+ _objc_msgSend$triggerDeferredDelegateCallbacks
- -[VCAudioCaptionsSpeechTranslator startCaptionsWithError:].cold.1
- -[VCAudioCaptionsSpeechTranslator startCaptionsWithError:].cold.2
- -[VCAudioCaptionsSpeechTranslator startCaptionsWithError:].cold.3
- -[VCAudioCaptionsSpeechTranslator startCaptionsWithError:].cold.4
- -[VCAudioCaptionsSpeechTranslator startCaptionsWithError:].cold.5
- -[VCMediaStream initializeTransportSessionWithLocalNWEnpoint:error:]
- -[VCMediaStream initializeTransportSessionWithLocalNWEnpoint:error:].cold.1
- -[VCMediaStreamManager capabilitiesForStream:mediaProtocolArgs:xpcArguments:error:]
- -[VCMediaStreamManager newMediaProtocolArgsWithMediaProtocolArgs:nwEndpoint:]
- -[VCTransportSessionMultiLink initWithLocalEndpoint:handlerQueue:context:eventHandler:options:error:]
- -[VCTransportSessionMultiLink initWithLocalEndpoint:handlerQueue:context:eventHandler:options:error:].cold.1
- -[VCTransportSessionMultiLink initWithLocalEndpoint:handlerQueue:context:eventHandler:options:error:].cold.2
- GCC_except_table85
- _VCAudioReceiver_SendStartCallReport
- _VCAudioReceiver_SendStartCallReport.cold.1
- ___28-[VCSession dispatchedStart]_block_invoke.608
- ___28-[VCSession dispatchedStart]_block_invoke.609
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.200
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.201
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.201.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.222
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.225
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.225.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.225.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242.cold.3
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242.cold.4
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.270
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.284
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.284.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.284.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.292
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.292.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.292.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.297
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.312
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.328
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.328.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.343
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.354
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.354.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.361
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.361.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.368
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.368.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.375
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.375.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.382
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.382.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.389
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.389.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.396
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.396.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.403
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.414
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.425
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.427
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.429
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.301
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.320
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.347
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.347.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.410
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.410.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.421
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.421.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.433
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.305
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.305.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.322
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.322.cold.1
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.600
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.604
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.605
- ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.621
- ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.620
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.199
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.219
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.221
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.228
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.235
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.252
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.260
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.267
- ___56-[AVCVideoStream registerBlocksForDelegateNotifications]_block_invoke.274
- ___64-[VCMediaStream handleMediaCallbackNotification:inData:outData:]_block_invoke.234
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219.cold.1
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219.cold.2
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219.cold.3
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219.cold.4
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.220
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.227
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.229
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke_2.221
- ___block_literal_global.233
- ___block_literal_global.273
- ___block_literal_global.299
- ___block_literal_global.303
- ___block_literal_global.307
- ___block_literal_global.314
- ___block_literal_global.330
- ___block_literal_global.349
- ___block_literal_global.356
- ___block_literal_global.363
- ___block_literal_global.384
- ___block_literal_global.391
- ___block_literal_global.398
- ___block_literal_global.405
- ___block_literal_global.412
- ___block_literal_global.416
- ___block_literal_global.423
- ___block_literal_global.431
- _objc_msgSend$audioInterval
- _objc_msgSend$capabilitiesForStream:mediaProtocolArgs:xpcArguments:error:
- _objc_msgSend$initWithLocalEndpoint:handlerQueue:context:eventHandler:options:error:
- _objc_msgSend$initializeTransportSessionWithLocalNWEnpoint:error:
- _objc_msgSend$newMediaProtocolArgsWithMediaProtocolArgs:nwEndpoint:
CStrings:
+ " [%s] %s:%d %@(%p) Setting clientAuditToken on nw_connection"
+ " [%s] %s:%d %@(%p) isFinal=%d, isLocal=%d, streamToken=%ld, formattedText=%s"
+ " [%s] %s:%d Failed to delete filePath=%@ error=%@"
+ " [%s] %s:%d File does not exist at filePath=%@"
+ " [%s] %s:%d Setting clientAuditToken on nw_connection"
+ " [%s] %s:%d Successfully deleted filePath=%@"
+ " [%s] %s:%d isFinal=%d, isLocal=%d, streamToken=%ld, formattedText=%s"
+ " [%s] %s:%d matchFormats = %@"
+ " [%s] %s:%d sortedFormats = %@"
+ "-[AVCRateController triggerDeferredDelegateCallbacks]"
+ "-[VCAudioCaptions dumpCaptionsIfNeededForCaptionsTranscription:]"
+ "-[VCAudioCaptionsSpeechTranslator addToCaptionTasksWithError:]"
+ "-[VCMediaStream initializeTransportSessionWithLocalNWEnpoint:clientAuditToken:error:]"
+ "-[VCMediaStreamManager newMediaProtocolArgsWithMediaProtocolArgs:nwEndpoint:clientAuditToken:]"
+ "-[VCRateControlMLEnrollment removeFileAtPath:]"
+ "-[VCTransportSessionMultiLink initWithLocalEndpoint:clientAuditToken:handlerQueue:context:eventHandler:options:error:]"
+ "/rc_fl_data/training_data.db"
+ "2175.12.1"
+ "@56@0:8@16@24@32@40^@48"
+ "@72@0:8@16@24@32^v40^?48@56^@64"
+ "AFBUPENB"
+ "AVCRC [%s] %s:%d %@(%p) Deferred request probing sequence for mode=%d, targetBitrate=%u, probingSequenceSize=%u, probingSequenceID=%u"
+ "AVCRC [%s] %s:%d %@(%p) Deferred targetBitrate changed for mode=%d, targetBitrate=%u, rateChangeCounter=%u"
+ "AVCRC [%s] %s:%d Deferred request probing sequence for mode=%d, targetBitrate=%u, probingSequenceSize=%u, probingSequenceID=%u"
+ "AVCRC [%s] %s:%d Deferred targetBitrate changed for mode=%d, targetBitrate=%u, rateChangeCounter=%u"
+ "CLIENTAUDITTOKEN"
+ "VCMediaStream [%s] %s:%d %@(%p) clientAuditToken is nil"
+ "VCMediaStream [%s] %s:%d clientAuditToken is nil"
+ "_clientAuditToken"
+ "_isDelegateCallbackDeferralEnabled"
+ "_isProbingSequenceRequestCallbackDeferred"
+ "_isTargetBitrateChangedCallbackDeferred"
+ "_processCompletionHandler"
+ "_processCompletionHandlerLock"
+ "addToCaptionTasksWithError:"
+ "appendClientAuditTokenToDictionary:clientAuditToken:"
+ "capabilitiesForStream:mediaProtocolArgs:xpcArguments:clientAuditToken:error:"
+ "cleanupTrainingDataFiles"
+ "currentProcessToken"
+ "initWithLocalEndpoint:clientAuditToken:handlerQueue:context:eventHandler:options:error:"
+ "initializeTransportSessionWithLocalNWEnpoint:clientAuditToken:error:"
+ "newMediaProtocolArgsWithMediaProtocolArgs:nwEndpoint:clientAuditToken:"
+ "triggerDeferredDelegateCallbacks"
+ "v16@?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBdIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
+ "v24@0:8^{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BBB}}16"
+ "v56@0:8@16{?=[8I]}24"
+ "vcMediaStreamClientAuditToken"
- " [%s] %s:%d Perfect match format=%@"
- "-[VCMediaStream initializeTransportSessionWithLocalNWEnpoint:error:]"
- "-[VCMediaStreamManager newMediaProtocolArgsWithMediaProtocolArgs:nwEndpoint:]"
- "-[VCTransportSessionMultiLink initWithLocalEndpoint:handlerQueue:context:eventHandler:options:error:]"
- "2175.9.2"
- "@64@0:8@16@24^v32^?40@48^@56"
- "VCAudioReceiver_SendStartCallReport"
- "capabilitiesForStream:mediaProtocolArgs:xpcArguments:error:"
- "initWithLocalEndpoint:handlerQueue:context:eventHandler:options:error:"
- "initializeTransportSessionWithLocalNWEnpoint:error:"
- "newMediaProtocolArgsWithMediaProtocolArgs:nwEndpoint:"
- "v24@0:8^{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}}16"

```
