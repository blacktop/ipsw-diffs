## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.114.0.0.0
-  __TEXT.__text: 0x1a8db4
-  __TEXT.__auth_stubs: 0x3230
+3.316.903.0.0
+  __TEXT.__text: 0x1bbe10
+  __TEXT.__auth_stubs: 0x3320
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x5d50
-  __TEXT.__const: 0x2167c
-  __TEXT.__cstring: 0x195b3
-  __TEXT.__oslogstring: 0x1aa99
-  __TEXT.__unwind_info: 0x3b50
-  __TEXT.__eh_frame: 0x110
+  __TEXT.__const: 0x228cc
+  __TEXT.__oslogstring: 0x1c1b7
+  __TEXT.__cstring: 0x1a6ba
+  __TEXT.__gcc_except_tab: 0x5cc0
+  __TEXT.__unwind_info: 0x3c40
+  __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x1ca1
-  __TEXT.__objc_methtype: 0x11e8
-  __TEXT.__objc_stubs: 0x1fa0
-  __DATA_CONST.__got: 0x3118
-  __DATA_CONST.__const: 0x69d8
+  __TEXT.__objc_methname: 0x1c61
+  __TEXT.__objc_methtype: 0x11fa
+  __TEXT.__objc_stubs: 0x1f60
+  __DATA_CONST.__got: 0x3208
+  __DATA_CONST.__const: 0x84d0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x818
+  __DATA_CONST.__objc_selrefs: 0x808
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x1928
-  __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x2130
-  __AUTH_CONST.__cfstring: 0x9540
-  __AUTH_CONST.__objc_const: 0xae0
+  __AUTH_CONST.__auth_got: 0x19a0
+  __AUTH_CONST.__auth_ptr: 0xa0
+  __AUTH_CONST.__const: 0x2808
+  __AUTH_CONST.__cfstring: 0x9780
+  __AUTH_CONST.__objc_const: 0x808
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x208370
-  __DATA.__bss: 0xd9
-  __DATA.__common: 0x58
+  __DATA.__data: 0x2195f8
+  __DATA.__bss: 0xf9
+  __DATA.__common: 0x54
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x118
-  __DATA_DIRTY.__bss: 0x990
-  __DATA_DIRTY.__common: 0x53a0
+  __DATA_DIRTY.__data: 0x110
+  __DATA_DIRTY.__bss: 0x920
+  __DATA_DIRTY.__common: 0x5420
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer
+  - /System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5546
-  Symbols:   9091
-  CStrings:  6246
+  Functions: 5685
+  Symbols:   9151
+  CStrings:  6395
 
Symbols:
+ _CFPropertyListCreateDeepCopy
+ _CVAFaceTrackingLiteCopyDecodedOutput
+ _TSPDumpOptions_CollectAriadnePlists
+ _TSPDumpOptions_CollectOsLogs
+ _TSPDumpOptions_CollectOsSignposts
+ _TSPDumpOptions_CollectTrials
+ _TSPDumpOptions_NoSymbolicate
+ _TSPDumpOptions_ReasonString
+ _TSPDumpOptions_ScrubOutput
+ _TSPDumpOptions_TargetPID
+ __Z14ComputeLensPSFhhhtttt
+ __Z15NearestNeighborRK11MatrixNxPtsILj2EdES2_PS_ILj1EdEPS_ILj1EjE
+ __Z20ComputeOpticalCenterhhhttttffjjdb
+ __ZN10ImageUtils12CornerfinderERK11MatrixNxPtsILj2EdERK6MatrixIdEjjPS1_PS0_ILj1EbESA_SA_
+ __ZN10ImageUtils17DetectArucoMarkerERK6MatrixIdEPj
+ __ZN10ImageUtils18FindMarkersOnImageERK6MatrixIdERKNS_15MarkerFinderOptEPNSt3__16vectorINS_6MarkerENS7_9allocatorIS9_EEEEPNS8_INS_4RectENSA_ISE_EEEE
+ __ZN10ImageUtils18SubPixelRefinementERKNS_11BoardConfigERK6MatrixIdERK11MatrixNxPtsILj2EdEd
+ __ZN10ImageUtils23GetInitialGuessLineScanERKNSt3__16vectorI11MatrixNxPtsILj2EjENS0_9allocatorIS3_EEEERKNS1_IS2_ILj2EdENS4_IS9_EEEERKS9_RKNS_11BoardConfigERK6MatrixIdEjPS9_PS2_ILj3EdEPS3_
+ __ZN10ImageUtils24DetectAndTrackChessBoardERKNSt3__16vectorI6MatrixIdENS0_9allocatorIS3_EEEERKNS_11BoardConfigEdjPNS1_I11MatrixNxPtsILj2EdENS4_ISD_EEEEPNS1_ISC_ILj3EdENS4_ISH_EEEEPbSL_PS6_PNS1_ISC_ILj2EjENS4_ISN_EEEE
+ __ZN24ISPExclaveSensorMetadataC1EP28sCIspMetaDataSharedExclaveAEP31sCIspMetaDataSharedExclaveInputP39sCIspMetaDataSharedExclaveIntrinsicData
+ __ZN24ISPExclaveSensorMetadataC2EP28sCIspMetaDataSharedExclaveAEP31sCIspMetaDataSharedExclaveInputP39sCIspMetaDataSharedExclaveIntrinsicData
+ __ZN26H16ISPGraphExclaveANDKNode19onMessageProcessingEPN6H16ISP24H16ISPFilterGraphMessageE
+ __ZN26H16ISPGraphExclaveANDKNodeC2EPN6H16ISP12H16ISPDeviceEj14ExclaveKitType
+ __ZN29H16ISPGraphExclaveRGBANDKNode16runANDKAlgorithmEPN6H16ISP24H16ISPFilterGraphMessageE
+ __ZN29H16ISPGraphExclaveRGBANDKNodeC1EPN6H16ISP12H16ISPDeviceEj
+ __ZN29H16ISPGraphExclaveRGBANDKNodeC2EPN6H16ISP12H16ISPDeviceEj
+ __ZN6H16ISP12H16ISPDevice17PowerOnExclaveKitEj
+ __ZN6H16ISP12H16ISPDevice18PowerOffExclaveKitEj
+ __ZN6H16ISP12H16ISPDevice19LoadOCClCalDataFileEv
+ __ZN6H16ISP12H16ISPDevice19SetMaximumFrameRateEjjb
+ __ZN6H16ISP12H16ISPDevice19SetMinimumFrameRateEjjb
+ __ZN6H16ISP12H16ISPDevice20ISP_GetLowMemoryModeEPb
+ __ZN6H16ISP12H16ISPDevice25SetExclaveTargetFrameRateEjf
+ __ZN6H16ISP12H16ISPDevice27GetDriverPerformanceMetricsEP27ISPDriverPerformanceMetrics
+ __ZN6H16ISP12H16ISPDevice41ISP_DCS_SetAudioBufferReceiverCallbackPtrEPFvP10__CVBuffer6CMTimeE
+ __ZN6H16ISP12H16ISPDevice43ISP_DCS_SetAudioBufferReceiverCallbackBlockEU13block_pointerFvP10__CVBuffer6CMTimeE
+ __ZN6H16ISP12H16ISPDevice48ISP_DCS_SetAudioBufferReceiverMessageCallbackPtrEPFvjjjE
+ __ZN6H16ISP12H16ISPDevice50ISP_DCS_SetAudioBufferReceiverMessageCallbackBlockEU13block_pointerFvjjjE
+ __ZN6H16ISP19H16ISPFrameReceiver28registerEPipeReceiveCallbackEPFiPvjPNS_23H16ISPEPipeResultStructEES1_
+ __ZN6H16ISP20DCSAudioAccelManager14SetCallbackPtrEPFvP10__CVBuffer6CMTimeE
+ __ZN6H16ISP20DCSAudioAccelManager16SetCallbackBlockEU13block_pointerFvP10__CVBuffer6CMTimeE
+ __ZN6H16ISP20DCSAudioAccelManager21SetMessageCallbackPtrEPFvjjjE
+ __ZN6H16ISP20DCSAudioAccelManager23SetMessageCallbackBlockEU13block_pointerFvjjjE
+ __ZN6H16ISP22H16ISPExclaveGraphNode14ConclaveClientEv
+ __ZN6H16ISP22H16ISPExclaveGraphNode15GetModuleParamsEv
+ __ZN6H16ISP22H16ISPExclaveGraphNode7ChannelEv
+ __ZN6H16ISP22H16ISPExclaveGraphNode7VerboseEv
+ __ZN6H16ISP22H16ISPExclaveGraphNode9ISPDeviceEv
+ __ZN6H16ISP22H16ISPExclaveGraphNodeC1E19H16ISPGraphNodeTypePNS_12H16ISPDeviceEj14ExclaveKitType
+ __ZN6H16ISP22H16ISPExclaveGraphNodeC2E19H16ISPGraphNodeTypePNS_12H16ISPDeviceEj14ExclaveKitType
+ __ZN6H16ISP24dictionaryCreateDeepCopyEPK14__CFDictionary
+ __ZN6H16ISP27g_ProjectorSettings_CentaurE
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode17updateObjectDictsEPNS_24H16ISPFilterGraphMessageE45isprgbexclavekitmodule_perceptionreturnstatus
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode29AddSecureTrackedFacesMetadataEPNS_24H16ISPFilterGraphMessageE60isprgbexclavekitmodule_ispexclavecorechrunkitfaceprocessrsltb
+ __ZN6H16ISP36H16ISPGraphExclaveSensorMetadataNode10computePTSEy
+ __ZN6H16ISP36H16ISPGraphExclaveSensorMetadataNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP36H16ISPGraphExclaveSensorMetadataNodeC2EPNS_12H16ISPDeviceEj14ExclaveKitType
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeC2EPNS_12H16ISPDeviceEj14ExclaveKitType
+ __ZN6H16ISP37H16ISPGraphExclaveObjectDetectionNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP37H16ISPGraphExclaveObjectDetectionNodeC2EPNS_12H16ISPDeviceEjPKj14ExclaveKitType
+ __ZN6H16ISP38H16ISPGraphExclaveIRSensorMetadataNode18sendSensorMetadataEP24ISPExclaveSensorMetadata
+ __ZN6H16ISP38H16ISPGraphExclaveIRSensorMetadataNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP38H16ISPGraphExclaveIRSensorMetadataNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNode18runMotionDetectionEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP39H16ISPGraphExclaveIRObjectDetectionNode14InvokeEKRunKitEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP39H16ISPGraphExclaveIRObjectDetectionNodeC1EPNS_12H16ISPDeviceEjPKj
+ __ZN6H16ISP39H16ISPGraphExclaveIRObjectDetectionNodeC2EPNS_12H16ISPDeviceEjPKj
+ __ZN6H16ISP39H16ISPGraphExclaveRGBSensorMetadataNode18sendSensorMetadataEP24ISPExclaveSensorMetadata
+ __ZN6H16ISP39H16ISPGraphExclaveRGBSensorMetadataNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP39H16ISPGraphExclaveRGBSensorMetadataNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode29AddAttentionDetectionMetadataEPNS_24H16ISPFilterGraphMessageEP50ispirexclavekitmodule_ispexclavecorechrunkitadrsltyb
+ __ZN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNode18runMotionDetectionEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNode14InvokeEKRunKitEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNodeC1EPNS_12H16ISPDeviceEjPKj
+ __ZN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNodeC2EPNS_12H16ISPDeviceEjPKj
+ __ZN8CppUtils22MachTimeToMicrosecondsEyPy
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__119piecewise_constructE
+ __ZTI26H16ISPGraphExclaveANDKNode
+ __ZTI29H16ISPGraphExclaveRGBANDKNode
+ __ZTIN6H16ISP32H16ISPGraphExclavePerceptionNodeE
+ __ZTIN6H16ISP36H16ISPGraphExclaveSensorMetadataNodeE
+ __ZTIN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeE
+ __ZTIN6H16ISP37H16ISPGraphExclaveObjectDetectionNodeE
+ __ZTIN6H16ISP38H16ISPGraphExclaveIRSensorMetadataNodeE
+ __ZTIN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeE
+ __ZTIN6H16ISP39H16ISPGraphExclaveIRObjectDetectionNodeE
+ __ZTIN6H16ISP39H16ISPGraphExclaveRGBSensorMetadataNodeE
+ __ZTIN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeE
+ __ZTIN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNodeE
+ __ZTS26H16ISPGraphExclaveANDKNode
+ __ZTS29H16ISPGraphExclaveRGBANDKNode
+ __ZTSN6H16ISP32H16ISPGraphExclavePerceptionNodeE
+ __ZTSN6H16ISP36H16ISPGraphExclaveSensorMetadataNodeE
+ __ZTSN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeE
+ __ZTSN6H16ISP37H16ISPGraphExclaveObjectDetectionNodeE
+ __ZTSN6H16ISP38H16ISPGraphExclaveIRSensorMetadataNodeE
+ __ZTSN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeE
+ __ZTSN6H16ISP39H16ISPGraphExclaveIRObjectDetectionNodeE
+ __ZTSN6H16ISP39H16ISPGraphExclaveRGBSensorMetadataNodeE
+ __ZTSN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeE
+ __ZTSN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNodeE
+ __ZTV26H16ISPGraphExclaveANDKNode
+ __ZTV29H16ISPGraphExclaveRGBANDKNode
+ __ZTVN6H16ISP32H16ISPGraphExclavePerceptionNodeE
+ __ZTVN6H16ISP36H16ISPGraphExclaveSensorMetadataNodeE
+ __ZTVN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeE
+ __ZTVN6H16ISP37H16ISPGraphExclaveObjectDetectionNodeE
+ __ZTVN6H16ISP38H16ISPGraphExclaveIRSensorMetadataNodeE
+ __ZTVN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeE
+ __ZTVN6H16ISP39H16ISPGraphExclaveIRObjectDetectionNodeE
+ __ZTVN6H16ISP39H16ISPGraphExclaveRGBSensorMetadataNodeE
+ __ZTVN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeE
+ __ZTVN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNodeE
+ ___strncpy_chk
+ _dgels_
+ _dumpTailspinInBackground
+ _dumpTailspinOnDispatchQueue
+ _dumpTailspinSync
+ _fsync
+ _ispirexclavekitmodule_ispirexclavekit__destruct
+ _ispirexclavekitmodule_ispirexclavekit__server_start_owned
+ _ispirexclavekitmodule_ispirexclavekit__server_stop
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdadsettings
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeinitsettinggetv2
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeintegrationgainsetv2
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchdpcset
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchisconcurrent
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitaev2
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitmdv2
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchsensormetadatav3
+ _ispirexclavekitmodule_ispirexclavekit_sendcmddebugcapability
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdexfiltration
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdinfiltration
+ _isprgbexclavekitmodule_isprgbexclavekit__destruct
+ _isprgbexclavekitmodule_isprgbexclavekit__server_start_owned
+ _isprgbexclavekitmodule_isprgbexclavekit__server_stop
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeinitsettinggetv2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeintegrationgainsetv2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchdpcset
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchisconcurrent
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchpdpset
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitaev2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitandk
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitmd
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitmdv2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitperception
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchsensormetadatav3
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchsetperceptionframerate
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmddebugcapability
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdexfiltration
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdinfiltration
+ _kFigCaptureStreamDetectedMotion
+ _kFigCaptureStreamDetectedObjectKey_SentToPerceptionThumbnailChannel
+ _kFigCaptureStreamFaceTrackingConfigurationKey_NetworkFailureThresholdMultiplier
+ _kFigCaptureStreamFaceTrackingConfigurationKey_NumTrackedFaces
+ _kFigCaptureStreamLMAConfigurationKey_EdgeDetectionEnabled
+ _kFigCaptureStreamLMAConfigurationKey_FaceRequired
+ _kFigCaptureStreamMetadataOutputConfigurationKey_LMAConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_LMAEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_MotionEstimationEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SVDResultEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_StreamingFaceTrackingConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_StreamingFaceTrackingEnabled
+ _kFigCaptureStreamMetadataOutputKey_FaceFound
+ _kFigCaptureStreamMetadataOutputKey_MotionEstimation
+ _kFigCaptureStreamMetadataOutputKey_SVDResult
+ _kFigCaptureStreamMetadataOutputKey_StreamingTrackedFaces
+ _kFigCaptureStreamMetadata_FaceDistance
+ _kFigCaptureStreamMetadata_FaceOccluded
+ _kFigCaptureStreamStreamingFaceKey_FaceIndex
+ _kFigCaptureStreamStreamingFaceKey_Found
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_FaceOcclusionDetectionEnabled
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_ThumbnailStreamMetadataObjectTypes
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_ThumbnailStreamTargetFrameRate
+ _notify_is_valid_token
+ _notify_register_dispatch
+ _os_variant_has_internal_diagnostics
+ _strerror
+ _strrchr
+ _tailspin_dump_output_with_options
+ _tailspin_dump_output_with_options_sync
+ _tb_client_connection_destruct
+ _tb_endpoint_set_interface_identifier
+ _tb_service_connection_destruct
- __Z18StopExclaveStreamsP19H16ISPCaptureDeviceP19H16ISPCaptureStream
- __ZN6H16ISP12H16ISPDevice18SetDeskViewEnabledEjb
- __ZN6H16ISP12H16ISPDevice19SetMaximumFrameRateEjj
- __ZN6H16ISP12H16ISPDevice19SetMinimumFrameRateEjj
- __ZN6H16ISP12H16ISPDevice38ISP_DCS_SetAudioBufferReceiverCallbackEU13block_pointerFvP10__CVBuffer6CMTimeE
- __ZN6H16ISP19H16ISPFrameReceiver28registerEPipeReceiveCallbackEPFiPvyjPNS_23H16ISPEPipeResultStructEES1_
- __ZN6H16ISP20DCSAudioAccelManager11SetCallbackEU13block_pointerFvP10__CVBuffer6CMTimeE
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNode10onActivateEv
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNode12onDeactivateEv
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNode15AddANSTMetadataEPNS_24H16ISPFilterGraphMessageEP29H16ISPExclaveANSTResultStructy
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNodeC1EPNS_12H16ISPDeviceEj
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNodeC2EPNS_12H16ISPDeviceEj
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNodeD0Ev
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNodeD1Ev
- __ZN6H16ISP35H16ISPGraphExclaveFaceDetectionNodeD2Ev
- __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode29AddAttentionDetectionMetadataEPNS_24H16ISPFilterGraphMessageEP50ispirexclavekitmodule_ispexclavecorechrunkitadrslty
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- __ZTIN6H16ISP35H16ISPGraphExclaveFaceDetectionNodeE
- __ZTSN6H16ISP35H16ISPGraphExclaveFaceDetectionNodeE
- __ZTVN6H16ISP35H16ISPGraphExclaveFaceDetectionNodeE
- __os_log_fault_impl
- _kCVAFaceTracking_UseTongue
- _kFigCaptureStreamMetadataOutputKey_SecureDetectedFaces
- _kFigCaptureStreamProperty_DeskViewEnabled
- _tb_message_configure_recieved
- _tb_message_construct
- _tb_message_destruct
- _tb_transport_message_buffer_wrap_buffer
CStrings:
+ "\tDefault calibration from NVM: deice is not ready or no ToF channel found"
+ "\tSerial nubmers size mismatch"
+ "\tValidting SN (registry vs cache)"
+ "%!s(MISSING) -  In concurrent streaming mode - Skip configuring Exclave AE\n"
+ "%!s(MISSING) - ANDK Graph Node Message invalid\n"
+ "%!s(MISSING) - AudioAccel streaming enabled, start streaming with updated testMode\n"
+ "%!s(MISSING) - AudioAccel streaming enabled, stop streaming with previous testMode\n"
+ "%!s(MISSING) - Camera Channel not supported for EK\n"
+ "%!s(MISSING) - Cannot find metadata dictionary!\n"
+ "%!s(MISSING) - Conclave setup failed\n"
+ "%!s(MISSING) - Could not access module parameters for channel=%!u(MISSING)!\n"
+ "%!s(MISSING) - Failed to open file: %!s(MISSING) %!s(MISSING)\n"
+ "%!s(MISSING) - Failed to power on Exclave Kit, fatal\n"
+ "%!s(MISSING) - Failed to run ANDK algorithm, ret=0x%!X(MISSING)\n"
+ "%!s(MISSING) - Failed to stop exclave streams, res=0x%!x(MISSING)\n"
+ "%!s(MISSING) - Got an unsupported perception object string! Skipping.\n"
+ "%!s(MISSING) - Invalid Focal Length received from FW! Falling back to 1.0 for focalLength\n"
+ "%!s(MISSING) - Invalid RGB conclave client handle\n"
+ "%!s(MISSING) - Invalid poolID=%!d(MISSING)\n"
+ "%!s(MISSING) - Invalid poolType=%!d(MISSING)\n"
+ "%!s(MISSING) - Power OFF EK Success\n"
+ "%!s(MISSING) - Power ON EK Success\n"
+ "%!s(MISSING) - Secure Metadata configuration prop invalid\n"
+ "%!s(MISSING) - [Exclaves] Skipping configuring Exclave graph, Exclave Algorithms are not enabled!\n"
+ "%!s(MISSING) - [Exclaves] Skipping configuring Exclave graph, Exclave Kit is not configured!\n"
+ "%!s(MISSING) - [Exclaves]: Cannot get initial AE settings, ipcRet %!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: Cannot get initial AE settings, ipcRet %!d(MISSING) tberr %!d(MISSING) ch %!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: Cannot set FaceID AttentionDetection Periocular support to %!{(MISSING)bool}d\n"
+ "%!s(MISSING) - [Exclaves]: Cannot set FaceID AttentionDetection attention requirement to true\n"
+ "%!s(MISSING) - [Exclaves]: Could not allocate face dictionary! Skipping!\n"
+ "%!s(MISSING) - [Exclaves]: Could not allocate hand dictionary! Skipping!\n"
+ "%!s(MISSING) - [Exclaves]: Could not allocate head dictionary! Skipping!\n"
+ "%!s(MISSING) - [Exclaves]: Could not allocate human body dictionary! Skipping!\n"
+ "%!s(MISSING) - [Exclaves]: Could not allocate human full body dictionary! Skipping!\n"
+ "%!s(MISSING) - [Exclaves]: Could not allocate memory for detected objects info dictionary!\n"
+ "%!s(MISSING) - [Exclaves]: EK IR CMD off failed, tberr=%!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: EK IR CMD on failed, tberr=%!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: EK RGB CMD on failed, tberr=%!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: Face ID PreCheck uxFeedback=0x%!X(MISSING) readiness=%!s(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) index: %!z(MISSING)u AngleInfoRoll: %!f(MISSING) Rect[%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)] Confidence %!f(MISSING) \n"
+ "%!s(MISSING) - [Exclaves]: IR EK Object Detection RunKit failed, tberr=%!d(MISSING) EK result=%!{(MISSING)bool}d\n"
+ "%!s(MISSING) - [Exclaves]: IR Face Detection IDL Success!: channel=%!u(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: ISP Mgr IR CH Start Failed, result=%!d(MISSING) \n"
+ "%!s(MISSING) - [Exclaves]: Invalid IR Client Handle!\n"
+ "%!s(MISSING) - [Exclaves]: Invalid RGB Client Handle!\n"
+ "%!s(MISSING) - [Exclaves]: Number of Face Detections requested is %!u(MISSING), Secure ANST maximum support is %!u(MISSING), truncating output!\n"
+ "%!s(MISSING) - [Exclaves]: Number of Hand Detections requested is %!u(MISSING), Secure ANST maximum support is %!u(MISSING), truncating output!\n"
+ "%!s(MISSING) - [Exclaves]: Number of Head Detections requested is %!u(MISSING), Secure ANST maximum support is %!u(MISSING), truncating output!\n"
+ "%!s(MISSING) - [Exclaves]: Number of requested objects: HumanBody=%!u(MISSING), HumanFullBody=%!u(MISSING), DogBody=%!u(MISSING), DogHead=%!u(MISSING), CatBody=%!u(MISSING), CatHead=%!u(MISSING)! Max ANST Supported Objects is %!u(MISSING), truncating output!\n"
+ "%!s(MISSING) - [Exclaves]: Number of requested objects: HumanFaces=%!u(MISSING), HumanHeads=%!u(MISSING), HumanBody=%!u(MISSING), HumanFullBody=%!u(MISSING), HumanHands=%!u(MISSING), DogBody=%!u(MISSING), DogHead=%!u(MISSING), CatBody=%!u(MISSING), CatHead=%!u(MISSING)!\n"
+ "%!s(MISSING) - [Exclaves]: ObjectID=%!u(MISSING), GroupID=%!u(MISSING) has an INVALID category!\n"
+ "%!s(MISSING) - [Exclaves]: Perception - Frame was skipped!\n"
+ "%!s(MISSING) - [Exclaves]: Perception - Frame was unable to be queued!\n"
+ "%!s(MISSING) - [Exclaves]: RGB EK Object Detection RunKit failed, tberr=%!d(MISSING) EK result=%!{(MISSING)bool}d\n"
+ "%!s(MISSING) - [Exclaves]: RGB Object Detection IDL Success: channel=%!u(MISSING), numfaces=%!u(MISSING), numobjects=%!u(MISSING), valid=%!u(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: RGB concurrent cmd Failed\n"
+ "%!s(MISSING) - [Exclaves]: Runkit Object Detection channel=%!d(MISSING), reqID=0x%!X(MISSING), pts=%!l(MISSING)lu\n"
+ "%!s(MISSING) - [Exclaves]: Send RGB Perception Framerate failed!, result=%!d(MISSING), channel=%!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: Skipped processing object detection algorithm!\n"
+ "%!s(MISSING) - [Exclaves]: Skipping perception transfer!\n"
+ "%!s(MISSING) - [Exclaves]: Unable to power off Exclave Kit\n"
+ "%!s(MISSING) - [Exclaves]: Unable to stop EK RGB Channel, tberr=%!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: channel %!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: failed to get channel distortion info! Extrinsics info for this channel will not be correct!\n"
+ "%!s(MISSING) - [Exclaves]: failed to get pearl camera calibration info!\n"
+ "%!s(MISSING) - [Exclaves]: send to perception IDL failed, tberr=%!u(MISSING) ipcret=%!{(MISSING)bool}d\n"
+ "%!s(MISSING) - [Exclaves]: ~H16ISPGraphExclaveAutoExposureNode\n"
+ "%!s(MISSING) - [Exclaves]:%!s(MISSING) Successfully stopped EK channel %!d(MISSING) \n"
+ "%!s(MISSING) - channel %!d(MISSING) meta output:%!s(MISSING) exclave FD:%!s(MISSING) AD:%!s(MISSING) ER:%!s(MISSING) FT:%!s(MISSING) PreCheck:%!s(MISSING) FDOD:%!s(MISSING) PO:%!s(MISSING) MD:%!s(MISSING) DPD:%!s(MISSING) BaselineStreaming:%!s(MISSING)\n"
+ "%!s(MISSING) - channel=%!u(MISSING) failed to enable filtration\n"
+ "%!s(MISSING) - channel=%!u(MISSING) failed to enable skip frame dump\n"
+ "%!s(MISSING) - channel=%!u(MISSING) failed to register for preference notifications\n"
+ "%!s(MISSING) - channel=%!u(MISSING) failed to set replay control\n"
+ "%!s(MISSING) - channel=%!u(MISSING) failed to set yuv dump control\n"
+ "%!s(MISSING) - creating graph node channel=%!u(MISSING) type=%!d(MISSING) ektype=%!d(MISSING)\n"
+ "%!s(MISSING) - failed to allocate dictionary\n"
+ "%!s(MISSING) - failed to create preferences queue\n"
+ "%!s(MISSING) - failed to get camera time ret=0x%!x(MISSING)\n"
+ "%!s(MISSING) - failed to get isp counter frequency ret=0x%!x(MISSING)\n"
+ "%!s(MISSING) - failed to set target frame rate channel=%!u(MISSING) framerate=%!f(MISSING) ret=0x%!x(MISSING)\n"
+ "%!s(MISSING) - invalid notification queue\n"
+ "%!s(MISSING) - unable to get kext exclave status ret=0x%!x(MISSING)\n"
+ "%!s(MISSING) - unrecognized motion trigger result\n"
+ "%!s(MISSING) : Load override %!s(MISSING) cal data: Size = %!l(MISSING)d (== %!l(MISSING)d ?); Status = %!x(MISSING)\n"
+ "%!s(MISSING) : Status = %!x(MISSING); OCCl (%!s(MISSING)) data - %!s(MISSING) \n"
+ "%!s(MISSING) OCCl is not a dict (FDR2.0?), Unauthorized swap or No OCCl data (perhaps cuz the device does not support OCCl) [error]: %!s(MISSING) \n"
+ "/usr/local/share/firmware/isp/2325_01XX.dat"
+ "/usr/local/share/firmware/isp/OCCl-cmca.DAT"
+ "/usr/local/share/firmware/isp/OCCl-cmcd.DAT"
+ "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
+ "ANDK algorithm did not run for reqid: 0x%!x(MISSING)\n"
+ "ANDK algorithm ran for reqid: 0x%!x(MISSING)\n"
+ "ANDK runkit ch=%!u(MISSING) reqid=0x%!x(MISSING)\n"
+ "AddFaceIDMetadata"
+ "AddSecureTrackedFacesMetadata"
+ "AttachCatBodiesDict"
+ "AttachCatHeadsDict"
+ "AttachDogBodiesDict"
+ "AttachDogHeadsDict"
+ "AttachFacesDict"
+ "AttachHeadsDict"
+ "AttachHumanBodiesDict"
+ "AttachHumanFullBodiesDict"
+ "AttachHumanHandsDict"
+ "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
+ "BackTeleCameraModuleSerialNumString"
+ "Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading OCCl calibration data\n"
+ "DCSAudioAccelKeyMessageCallback_Private"
+ "DCSAudioAccelMessageCallback_Private"
+ "DCSAudioAccelTimeReference_Private"
+ "DCSAudioAccelTimeReference_absoluteTime_Private"
+ "DCSAudioAccelTimeReference_ispTime_Private"
+ "DCSDataFileLoad_FilePath_Private"
+ "DCSDataFileLoad_FileType_Private"
+ "DCSDataFileLoad_Private"
+ "DepthToPosition_Private"
+ "Dump tailspin end ...\n"
+ "Dump tailspin to %!s(MISSING) begin ...\n"
+ "EnableDepthToPositionMetadata"
+ "EnableSPDMetadata"
+ "Error sending sCIspCmdChCropSet command: 0x%!X(MISSING)\n"
+ "Error sending sCIspCmdChOutputConfigSet command: 0x%!X(MISSING)\n"
+ "ExclaveApplyFiltrationDebugPreferences"
+ "ExclaveInitCaptureDevice"
+ "ExclaveRegisterPreferenceNotifications"
+ "Failed ANDK runkit IDL\n"
+ "FormatIndex %!d(MISSING) doesn't support SIFR mode\n"
+ "FrontCameraModuleSerialNumString exists - load OCCl calibration data\n\n"
+ "GenerateRGBObjectDictionary"
+ "GetModuleParams"
+ "H16ISPDevice::GetCameraConfig()\n"
+ "H16ISPExclaveGraphNode"
+ "H16ISPGraphExclaveObjectDetectionNode"
+ "IRMotionDetectionResultCreateDictionaryRepresentation"
+ "ISPDebugDumpSkipFrame"
+ "ISPDebugFiltration"
+ "ISPDebugReplayCtl"
+ "ISPDebugYUVDumpCtl"
+ "Invalid RGB conclave client handle\n"
+ "InvokeEKRunKit"
+ "Load Data File command failed, error: 0x%!X(MISSING), path: %!s(MISSING), type: 0x%!x(MISSING)\n\n"
+ "LoadOCClCalDataFile"
+ "Markers.cpp"
+ "MotionDetectionResultCreateDictionaryRepresentation"
+ "OCCl"
+ "PowerOffExclaveKit"
+ "PowerOnExclaveKit"
+ "PrintInvalidANSTDetections"
+ "RGBMotionDetectionResultCreateDictionaryRepresentation"
+ "Received frame drop request: channel=%!d(MISSING) frameDropRequestEnabled=%!d(MISSING) frameCount=%!d(MISSING)\n"
+ "SIFRControlMode_Private"
+ "ScanPointsOnLine"
+ "SecureIRBaselineStreamingEnabled_Private"
+ "SecureRGBBaselineStreamingEnabled_Private"
+ "Sending data buffer failed, result=0x%!X(MISSING)\n"
+ "Sending shared buffer failed, result=0x%!X(MISSING)\n"
+ "Shared Depth to Position Debug"
+ "SolveUsingQR"
+ "SplitPhotodiode_Private"
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecoreadsettings__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreAdSettings\""
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechdpcset__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChDPCSet\""
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechsensormetadatav3__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChSensorMetadataV3\""
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorefiltration__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreFiltration\""
+ "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechdpcset__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChDPCSet\""
+ "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechsensormetadatav3__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChSensorMetadataV3\""
+ "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorefiltration__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreFiltration\""
+ "TB_ASSERT: (server->sendcmdadsettings != NULL) && \"implementation for sendCmdAdSettings is not present\""
+ "TB_ASSERT: (server->sendcmdchaeinitsettinggetv2 != NULL) && \"implementation for sendCmdChAEInitSettingGetV2 is not present\""
+ "TB_ASSERT: (server->sendcmdchaeintegrationgainsetv2 != NULL) && \"implementation for sendCmdChAEIntegrationGainSetV2 is not present\""
+ "TB_ASSERT: (server->sendcmdchdpcset != NULL) && \"implementation for sendCmdChDPCSet is not present\""
+ "TB_ASSERT: (server->sendcmdchisconcurrent != NULL) && \"implementation for sendCmdChIsConcurrent is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitaev2 != NULL) && \"implementation for sendCmdChRunKitAEV2 is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitandk != NULL) && \"implementation for sendCmdChRunKitANDK is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitmdv2 != NULL) && \"implementation for sendCmdChRunKitMDV2 is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitperception != NULL) && \"implementation for sendCmdChRunKitPerception is not present\""
+ "TB_ASSERT: (server->sendcmdchsensormetadatav3 != NULL) && \"implementation for sendCmdChSensorMetadataV3 is not present\""
+ "TB_ASSERT: (server->sendcmdchsetperceptionframerate != NULL) && \"implementation for sendCmdChSetPerceptionFrameRate is not present\""
+ "TB_ASSERT: (server->sendcmddebugcapability != NULL) && \"implementation for sendCmdDebugCapability is not present\""
+ "TB_ASSERT: (server->sendcmdexfiltration != NULL) && \"implementation for sendCmdExfiltration is not present\""
+ "TB_ASSERT: (server->sendcmdinfiltration != NULL) && \"implementation for sendCmdInfiltration is not present\""
+ "Tailspin with reason '%!@(MISSING)' stored at path %!s(MISSING)\n"
+ "Unable to allocate a replacement buffer (poolID = CHAN_%!d(MISSING)_%!s(MISSING), actual poolID = %!d(MISSING), buffer pool pointer = %!p(MISSING))\n"
+ "Unable to locate surface ID %!d(MISSING)\n"
+ "Unable to store tailspin with reason '%!@(MISSING)' at path %!s(MISSING)\n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) CVAFaceTrackingLiteCopyDecodedOutput failed, err=0x%!X(MISSING) \n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) RunKit FT reqID:0x%!x(MISSING) channel %!d(MISSING)\n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) Skipped processing secure face tracking algorithm\n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::onActivate\n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::onDeactivate\n"
+ "[Exclaves] H16ISPGraphExclaveSyncNode::%!s(MISSING) Message Drop Timeout!, requestid=0x%!X(MISSING)\n"
+ "[Exclaves] H16ISPGraphExclaveSyncNode::%!s(MISSING) Message Drop due to above queue size!, requestid=0x%!X(MISSING)\n"
+ "[Exclaves]: AE init settings aeCounter %!l(MISSING)lu Exp %!u(MISSING) ExpTime %!d(MISSING) ReqID %!l(MISSING)lu SensorAG %!d(MISSING) SensorDG %!d(MISSING) IspDG %!d(MISSING) VFrameSize %!d(MISSING) VFrameTime %!d(MISSING) Channel=%!u(MISSING)\n"
+ "[Exclaves]: H16ISPGraphAutoExposureNode::%!s(MISSING) Debug AE results: reqID %!l(MISSING)lu aeCounter %!l(MISSING)lu exp %!d(MISSING) ET %!d(MISSING) Sensor AG %!d(MISSING) Sensor DG %!d(MISSING) ISP DG %!d(MISSING)\n"
+ "[Exclaves]: H16ISPGraphAutoExposureNode::%!s(MISSING) Debug AE results: reqID %!l(MISSING)lu aeCounter %!l(MISSING)lu exp %!d(MISSING) ET %!d(MISSING) Sensor AG %!d(MISSING) Sensor DG %!d(MISSING) ISP DG %!d(MISSING) ipcresult=%!{(MISSING)bool}d\n"
+ "[Exclaves]: H16ISPGraphAutoExposureNode::%!s(MISSING) In concurrent mode, skip apply AE Settings to FW\n"
+ "[Exclaves]: H16ISPGraphAutoExposureNode::%!s(MISSING) cannot set exclave AE configurations to firmware, res=0x%!X(MISSING)\n"
+ "[Exclaves]: H16ISPGraphAutoExposureNode::onActivate\n"
+ "[Exclaves]: H16ISPGraphAutoExposureNode::onDeactivate\n"
+ "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) EK AE RunKit CamChan %!d(MISSING), requestID=0x%!X(MISSING)\n"
+ "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) EK AE RunKit Failed for reqID 0x%!X(MISSING) ipcret %!d(MISSING)\n"
+ "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) EK RunKit AE Failed for reqID 0x%!X(MISSING) ipcret %!d(MISSING)\n"
+ "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) EK RunKit AE skipped for reqID 0x%!X(MISSING)\n"
+ "[Exclaves]: H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) EK Face Kit Runkit failed, tberr %!d(MISSING) ipcRet %!d(MISSING)\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%!s(MISSING) Cannot allocate CFDictionary channel=%!d(MISSING)\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%!s(MISSING) EK IR ISP Manager RunKit failed, tberr=%!d(MISSING) ipcret=%!{(MISSING)bool}d\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%!s(MISSING) EK RGB ISP Manager RunKit failed, tberr=%!d(MISSING) ipcret=%!{(MISSING)bool}d\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%!s(MISSING) Invalid IR Client Handle\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%!s(MISSING) RunKit ISP Mgr reqID 0x%!X(MISSING) frameID=%!U(MISSING)\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%!s(MISSING) Skipped processing ISPManager algoProcessing %!d(MISSING)\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::onActivate\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::onDeactivate\n"
+ "[Exclaves]: Projector Settings : ProbeMode %!d(MISSING) StrobeMode %!d(MISSING) StrobePulseWidth %!f(MISSING) StrobeCurrentPercentage %!f(MISSING)\n"
+ "[Exclaves]: RGB Face Tracking: channel=%!u(MISSING)\n"
+ "[Exclaves]: Sending ANST results to perception!\n"
+ "[Exclaves]: Sent IR cmd on!\n"
+ "[Exclaves]: Sent RGB Perception Framerate=%!d(MISSING) channel=%!d(MISSING)\n"
+ "[Exclaves]: Skip configuring initial AE settings, ipcRet %!d(MISSING)\n"
+ "[Exclaves]: Skip configuring initial AE settings, ipcRet %!d(MISSING) ch %!d(MISSING)\n"
+ "[TAILSPIN]Failed to complete file name with strftime!\n"
+ "[TAILSPIN]Failed to create CFString for reason: %!s(MISSING)\n"
+ "[TAILSPIN]Failed to create directory %!s(MISSING): %!d(MISSING)!\n"
+ "[TAILSPIN]Failed to open(\"%!s(MISSING)\", O_RDWR | O_CREAT, 0644): %!s(MISSING)!\n"
+ "[TAILSPIN]dirAndPrefix is longer than PATH_MAX\n"
+ "[TAILSPIN]time function failed!\n"
+ "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
+ "_%!Y(MISSING).%!m(MISSING).%!d(MISSING)_%!H(MISSING)-%!M(MISSING)-%!S(MISSING)%!z(MISSING).tailspin"
+ "backTeleCameraModuleSerialNumString exists - load OCCl calibration data\n\n"
+ "ch%!u(MISSING): invalid sensor metadata\n"
+ "cleanupMessageList"
+ "cmca"
+ "cmcd"
+ "com.apple.isp.preference-notify"
+ "com.apple.isp.preferences.queue"
+ "computePTS"
+ "creating directory %!s(MISSING)\n"
+ "creating tailspin file %!s(MISSING)\n"
+ "direction.GetNumOfPoints()==1"
+ "dumpTailspinWithOptionsOnQueue %!s(MISSING) %!@(MISSING) %!p(MISSING) %!p(MISSING)\n"
+ "failed to run ir motion detection reqid=0x%!x(MISSING) tberr=%!u(MISSING) ipcret=%!{(MISSING)bool}d hasvalidresult=%!{(MISSING)bool}d\n"
+ "failed to run rgb motion detection reqid=0x%!x(MISSING) tberr=%!u(MISSING) ipcret=%!{(MISSING)bool}d hasvalidresult=%!{(MISSING)bool}d\n"
+ "failed to send IR sensor metadata tberr=%!u(MISSING) result=%!{(MISSING)bool}d frameid=%!u(MISSING)\n"
+ "failed to send rgb sensor metadata tberr=%!u(MISSING) result=%!{(MISSING)bool}d frameid=%!u(MISSING)\n"
+ "invalid IR conclave client handle\n"
+ "invalid RGB conclave client handle\n"
+ "invalid ir conclave client handle\n"
+ "invalid rgb conclave client handle\n"
+ "ir runkit motion detection ch=%!u(MISSING) reqid=0x%!x(MISSING)\n"
+ "isSifrFrameDecimated"
+ "maxPt.GetNumOfPoints()==1"
+ "numberWithBool:"
+ "pH16ISPDevice->ISP_SendBuffers failed, result=0x%!X(MISSING)\n"
+ "rgb runkit motion detection ch=%!u(MISSING) reqid=0x%!x(MISSING)\n"
+ "sendSensorMetadata"
+ "sending sensor metadata channel=%!u(MISSING) frameid=%!u(MISSING) concurrentmode=%!d(MISSING)\n"
+ "sending sensor metadata channel=%!u(MISSING) frameid=%!u(MISSING) concurrentmode=%!d(MISSING) \n"
+ "sensorSifrBayerBinFactor"
+ "sensorSifrQuadraBinFactor"
+ "sifrBinHeight"
+ "sifrBinWidth"
+ "startPt.GetNumOfPoints()==1"
+ "updateObjectDicts"
+ "v12@?0B8"
+ "v12@?0i8"
- "\tDefault calibration from NVM: device is not ready or no ToF channel found"
- "\tSerial numbers sized mismatch"
- "\tValidating SN (registry vs cache)"
- "%!s(MISSING) - AudioAccel testMode must updated, will take effect when next streaming enable event\n"
- "%!s(MISSING) - AudioAccelFrame[%!d(MISSING)] sampleTimeStamp = %!l(MISSING)lu ms accOoPlane[0]=%!u(MISSING) accInPlane[0]=%!u(MISSING)\n"
- "%!s(MISSING) - Buffer: IOSurface=0x%!X(MISSING), Size=%!z(MISSING)u, poolID=%!d(MISSING), poolType=%!s(MISSING)\n"
- "%!s(MISSING) - BufferReceivedProc called. bufferCount=%!d(MISSING)\n"
- "%!s(MISSING) - Cannot deactivate Exclave buffer pool, exclave algos are enabled!\n"
- "%!s(MISSING) - Client notification\n"
- "%!s(MISSING) - Failed to open file: %!s(MISSING)\n"
- "%!s(MISSING) - Ignore testMode configuration until hw available, must match stream enable setting for dev platform\n"
- "%!s(MISSING) - Metadata configuration prop invalid\n"
- "%!s(MISSING) - SetCallback = %!l(MISSING)lu\n"
- "%!s(MISSING) - Unable to get kext exclave status\n"
- "%!s(MISSING) - [Exclaves] H16ISPFrameReceiver - pH16ISPDevice->ISP_GetCameraTime failed, result=0x%!X(MISSING)\n\n"
- "%!s(MISSING) - [Exclaves] channel %!d(MISSING)\n"
- "%!s(MISSING) - [Exclaves] ~H16ISPGraphExclaveAutoExposureNode\n"
- "%!s(MISSING) - [Exclaves]: Cannot get initial AE settings, result %!d(MISSING)\n"
- "%!s(MISSING) - [Exclaves]: EK IR CMD off failed %!d(MISSING)\n"
- "%!s(MISSING) - [Exclaves]: EK RGB Channel stop failed %!d(MISSING) \n"
- "%!s(MISSING) - [Exclaves]: ISP Mgr IR CH Start Failed, result %!d(MISSING) \n"
- "%!s(MISSING) - [Exclaves]: Successfully stopped EK channel %!d(MISSING)\n"
- "%!s(MISSING) - [Exclaves]: camChannel %!d(MISSING)\n"
- "%!s(MISSING) - [Exclaves]: sending IR CMD ON to EK failed!\n"
- "%!s(MISSING) - [Exclaves]: sending RGB CMD ON to EK failed!\n"
- "%!s(MISSING) - [Exclaves]: ~H16ISPGraphExclaveFaceDetectionNode\n"
- "%!s(MISSING) - audioAccel: version = %!u(MISSING) frames=%!u(MISSING) fwTimeStamp=%!l(MISSING)lu ms\n"
- "%!s(MISSING) - callback = %!l(MISSING)lu MyAudioAccelCallback = %!l(MISSING)lu\n"
- "%!s(MISSING) - channel %!d(MISSING) meta output:%!s(MISSING) exclave FD:%!s(MISSING) AD:%!s(MISSING) ER:%!s(MISSING) FT:%!s(MISSING) PC:%!s(MISSING) FDOD:%!s(MISSING) PO:%!s(MISSING) BaselineStreaming: %!s(MISSING)\n"
- "%!s(MISSING) - error: 0x%!X(MISSING)\n"
- ".bin"
- ".plist"
- "2 "
- "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
- "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?}^{DCSAudioAccelManager}}16"
- "C "
- "D "
- "Error sending sCIspCmdChCropSet command: 0x%!X(MISSING)"
- "Error sending sCIspCmdChOutputConfigSet command: 0x%!X(MISSING)"
- "F "
- "H16ISPGraphExclaveFaceDetectionNode"
- "HITH "
- "INVALID"
- "KPD "
- "M "
- "O "
- "R "
- "Received frame drop request: channel=%!d(MISSING) frameDropRequestEnabled=%!d(MISSING) frameCount=%!d(MISSING)"
- "S "
- "SFTM "
- "SMVH "
- "SMVP "
- "SMVS "
- "SMVSK "
- "SPD "
- "SR+ "
- "STR "
- "SecureIRBaselineStreamingEnabled"
- "SecureRGBBaselineStreamingEnabled"
- "Sending data buffer failed, result=0x%!X(MISSING)"
- "Sending shared buffer failed, result=0x%!X(MISSING)"
- "SetCallback"
- "SetDeskViewEnabled"
- "UNKNOWN"
- "Unable to allocate a replacement buffer (poolID = CHAN_%!d(MISSING)_%!s(MISSING), actual poolID = %!d(MISSING), buffer pool pointer = %!p(MISSING))"
- "Unable to locate surface ID %!d(MISSING)"
- "VdspSpecialization.hpp"
- "[Exclaves] Error sending sensor metadata\n"
- "[Exclaves] H16ISPGraphAutoExposureNode::%!s(MISSING) Debug AE results: reqID %!l(MISSING)lu aeCounter %!l(MISSING)lu exp %!d(MISSING) ET %!d(MISSING) ag %!d(MISSING) dg %!d(MISSING)\n"
- "[Exclaves] H16ISPGraphAutoExposureNode::%!s(MISSING) cannot set exclave AE configurations to firmware, res=0x%!X(MISSING)\n"
- "[Exclaves] H16ISPGraphAutoExposureNode::onActivate\n"
- "[Exclaves] H16ISPGraphAutoExposureNode::onDeactivate\n"
- "[Exclaves] H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) EK AE RunKit CamChan %!d(MISSING), requestID=0x%!X(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) EK AE RunKit Failed, ipcret %!d(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) EK RunKit AE Failed for reqID 0x%!X(MISSING) ipcret %!d(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) No IR sensor metadata found! Unable to run AE!\n"
- "[Exclaves] H16ISPGraphExclaveAutoExposureNode::%!s(MISSING) No RGB sensor metadata found! Unable to run AE!\n"
- "[Exclaves] H16ISPGraphExclaveISPManagerNode::%!s(MISSING) Cannot allocate CFDictionary channel=%!d(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveISPManagerNode::%!s(MISSING) EK IR ISP Manager RunKit failed, tberr= %!d(MISSING) ipcret=%!d(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveISPManagerNode::%!s(MISSING) Invalid IR Client Handle\n"
- "[Exclaves] H16ISPGraphExclaveISPManagerNode::%!s(MISSING) RunKit ISP Mgr reqID 0x%!X(MISSING) frameID=%!U(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveISPManagerNode::%!s(MISSING) Skipped processing ISPManager algoProcessing %!d(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveISPManagerNode::onActivate\n"
- "[Exclaves] H16ISPGraphExclaveISPManagerNode::onDeactivate\n"
- "[Exclaves] H16ISPGraphExclaveSyncNode::cleanupMessageList Message Drop Timeout!, requestid=0x%!X(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveSyncNode::cleanupMessageList Message Drop due to above queue size!, requestid=0x%!X(MISSING)\n"
- "[Exclaves]: AE init on channel=%!u(MISSING)\n"
- "[Exclaves]: H16ISPGraphExclaveFaceDetectionNode::%!s(MISSING) EK ANST RunKit failed, tberr=%!d(MISSING) ipcret=%!d(MISSING)\n"
- "[Exclaves]: H16ISPGraphExclaveFaceDetectionNode::%!s(MISSING) EK FD RunKit failed, tberr=%!d(MISSING) ipcret=%!d(MISSING)\n"
- "[Exclaves]: H16ISPGraphExclaveFaceDetectionNode::%!s(MISSING) Invalid IR Client Handle\n"
- "[Exclaves]: H16ISPGraphExclaveFaceDetectionNode::%!s(MISSING) Invalid RGB Client Handle\n"
- "[Exclaves]: H16ISPGraphExclaveFaceDetectionNode::%!s(MISSING) Runkit FD reqID 0x%!X(MISSING) channel %!d(MISSING)\n"
- "[Exclaves]: H16ISPGraphExclaveFaceDetectionNode::%!s(MISSING) Skipped processing face detection algorithm\n"
- "[Exclaves]: H16ISPGraphExclaveFaceDetectionNode::%!s(MISSING) Unable to add ANST Metadata res=0x%!X(MISSING) channel=%!d(MISSING)\n"
- "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%!s(MISSING) EK RGB ISP Manager RunKit failed\n"
- "[Exclaves]: H16ISPGraphFaceDetectionNode::onActivate\n"
- "[Exclaves]: H16ISPGraphFaceDetectionNode::onDeactivate\n"
- "[Exclaves]: IR AE Runkit IDL Success: channel=%!u(MISSING)\n"
- "[Exclaves]: IR Face Detection IDL Success: channel=%!u(MISSING)\n"
- "[Exclaves]: RGB Face Detection IDL Success: channel=%!u(MISSING) numfaces %!d(MISSING) numobjects %!d(MISSING) valid %!d(MISSING)\n"
- "[Exclaves]: Sent IR command on!\n"
- "[Exclaves]: Sync Node not found!\n"
- "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?}^{DCSAudioAccelManager}}"
- "adjustForImageRotation:"
- "calibration"
- "nCols2%! (MISSING)== 1"
- "nRows2%! (MISSING)== 1"
- "pH16ISPDevice->ISP_SendBuffers failed, result=0x%!X(MISSING)"
- "reference"
- "setCameraToPlatformTransform:"
- "setWmcamToMcamExtrinsics:"
- "spotDB"
- "vDSPImgfir"
- "~H16ISPGraphExclaveFaceDetectionNode"

```
