## H16ISPServices

> `/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices`

```diff

-3.415.0.0.0
-  __TEXT.__text: 0x24e34
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__gcc_except_tab: 0x594
-  __TEXT.__cstring: 0x78e9
-  __TEXT.__const: 0x58
-  __TEXT.__unwind_info: 0x478
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__auth_ptr: 0x10
+3.509.0.0.0
+  __TEXT.__text: 0x10b48
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__gcc_except_tab: 0x5b8
+  __TEXT.__cstring: 0x6269
+  __TEXT.__const: 0x98
+  __TEXT.__oslogstring: 0x5bd
+  __TEXT.__unwind_info: 0x268
+  __DATA_CONST.__got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__cfstring: 0x120
+  __DATA.__data: 0x8
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
-  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore
+  - /System/Library/PrivateFrameworks/CMCaptureDevice.framework/CMCaptureDevice
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libIOAccessoryManager.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 535
-  Symbols:   1053
-  CStrings:  1472
+  Functions: 129
+  Symbols:   270
+  CStrings:  1459
 
Symbols:
+ _CFDataGetLength
+ _CFDictionaryContainsKey
+ _CGPointMakeWithDictionaryRepresentation
+ _CGPointZero
+ _CGRectZero
+ _CMTimeGetSeconds
+ _CMTimeMake
+ _FigCFDictionaryGetCGRectIfPresent
+ _FigCFEqual
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ __Z20FigMotionGetGravityZPK14__CFDictionaryPf
+ __Z30FigMotionComputePrincipalPointPK14__CFDictionaryffdiiiihP7CGPoint
+ __Z37FigMotionAdjustPointForSphereMovementPK14__CFDictionaryffdP7CGPoint
+ __Z37FigMotionComputeAverageSpherePositionPK14__CFDictionarydP11FigPosition
+ __Z38FigMotionCalculateAdjustedLensPositionPK14__CFDictionaryfP26CameraCharacterizationDatafPf
+ __Z39FigMotionCalculateAdjustedFocusPositionffPi
+ __Z41FigMotionComputeLensPositionScalingFactorPK14__CFDictionaryiiiiPf
+ __os_log_default
+ __os_log_error_impl
+ _kFigCapturePortType_FrontFacingSuperWideCamera
+ _kFigCaptureStreamMetadata_CurrentFocusPosition
+ _kFigCaptureStreamMetadata_FrameRollingShutterSkew
+ _kFigCaptureStreamMetadata_ISPHallData
+ _kFigCaptureStreamMetadata_ISPMotionData
+ _kFigCaptureStreamMetadata_OpticalCenter
+ _kFigCaptureStreamMetadata_PortType
+ _kFigCaptureStreamMetadata_RawCropRect
+ _kFigCaptureStreamMetadata_SensorRawValidBufferRect
+ _kFigCaptureStreamMetadata_TotalSensorCropRect
+ _kFigCaptureStreamMetadata_ValidBufferRect
+ _os_log_create
+ _os_log_type_enabled
- __NSConcreteStackBlock
- __os_crash
- _ispirexclavekitmodule_ispirexclavekit__copy
- _ispirexclavekitmodule_ispirexclavekit__destruct
- _ispirexclavekitmodule_ispirexclavekit__server_start_owned
- _ispirexclavekitmodule_ispirexclavekit__server_stop
- _ispirexclavekitmodule_ispirexclavekit_init
- _ispirexclavekitmodule_ispirexclavekit_init_static
- _ispirexclavekitmodule_ispirexclavekit_sendcmdadsettings
- _ispirexclavekitmodule_ispirexclavekit_sendcmdaeflickerfreqset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeframeratemaxget
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeframeratemaxset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeframerateminget
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeframerateminset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaegaincapset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeinitsettingget
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeinitsettinggetv2
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeintegrationgainset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeintegrationgainsetv2
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeintegrationtimemaxset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeupdateresume
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeupdatesuspend
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchalgoenable
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchconfigurationstatusread
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchdpcset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchinfoset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchinfoset2
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchisconcurrent
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchlscset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchpdpset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitad
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitae
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitaev2
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitanst
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitattn
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkiter
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitfd
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitisp
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchsensormetadata
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchsensormetadata2
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchsensormetadatav3
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchstart
- _ispirexclavekitmodule_ispirexclavekit_sendcmdchstop
- _ispirexclavekitmodule_ispirexclavekit_sendcmddebugcapability
- _ispirexclavekitmodule_ispirexclavekit_sendcmdexclavebootarg
- _ispirexclavekitmodule_ispirexclavekit_sendcmdexclavechcameraconfigset
- _ispirexclavekitmodule_ispirexclavekit_sendcmdexclavechpropertyread
- _ispirexclavekitmodule_ispirexclavekit_sendcmdexclavechpropertywrite
- _ispirexclavekitmodule_ispirexclavekit_sendcmdexclaveisphwirq
- _ispirexclavekitmodule_ispirexclavekit_sendcmdexfiltration
- _ispirexclavekitmodule_ispirexclavekit_sendcmdinfiltration
- _ispirexclavekitmodule_ispirexclavekit_sendcmdoff
- _ispirexclavekitmodule_ispirexclavekit_sendcmdon
- _ispirexclavekitmodule_ispirexclavekit_server_start
- _isprgbexclavekitmodule_isprgbexclavekit__copy
- _isprgbexclavekitmodule_isprgbexclavekit__destruct
- _isprgbexclavekitmodule_isprgbexclavekit__server_start_owned
- _isprgbexclavekitmodule_isprgbexclavekit__server_stop
- _isprgbexclavekitmodule_isprgbexclavekit_init
- _isprgbexclavekitmodule_isprgbexclavekit_init_static
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdaeflickerfreqset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeframeratemaxget
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeframeratemaxset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeframerateminget
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeframerateminset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaegaincapset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeinitsettingget
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeinitsettinggetv2
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeintegrationgainset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeintegrationgainsetv2
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeintegrationtimemaxset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeupdateresume
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeupdatesuspend
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchalgoenable
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchalgoframerate
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchdpcset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchinfoset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchinfoset2
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchisconcurrent
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchlscset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchpdpset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitae
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitaev2
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitanst
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitanstv150
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitisp
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchsensormetadata
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchsensormetadata2
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchsensormetadatav3
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchstart
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchstop
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmddebugcapability
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdexclavebootarg
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdexclavechcameraconfigset
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdexclavechpropertyread
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdexclavechpropertywrite
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdexclaveisphwirq
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdexfiltration
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdinfiltration
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdoff
- _isprgbexclavekitmodule_isprgbexclavekit_sendcmdon
- _isprgbexclavekitmodule_isprgbexclavekit_server_start
- _printf
- _tb_client_connection_activate
- _tb_client_connection_create_with_endpoint
- _tb_client_connection_create_with_endpoint_static
- _tb_client_connection_destruct
- _tb_client_connection_message_construct
- _tb_client_connection_message_destruct
- _tb_connection_send_query
- _tb_endpoint_set_interface_identifier
- _tb_message_complete
- _tb_message_configure_received
- _tb_message_construct
- _tb_message_decode_bool
- _tb_message_decode_f32
- _tb_message_decode_s16
- _tb_message_decode_s32
- _tb_message_decode_s8
- _tb_message_decode_u16
- _tb_message_decode_u32
- _tb_message_decode_u64
- _tb_message_decode_u8
- _tb_message_destruct
- _tb_message_encode_bool
- _tb_message_encode_f32
- _tb_message_encode_s16
- _tb_message_encode_s32
- _tb_message_encode_s8
- _tb_message_encode_u16
- _tb_message_encode_u32
- _tb_message_encode_u64
- _tb_message_encode_u8
- _tb_service_connection_activate
- _tb_service_connection_create_with_endpoint
- _tb_service_connection_destruct
- _tb_service_connection_message_configure_reply
- _tb_transport_message_buffer_wrap_buffer
CStrings:
+ "%s - Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f].\n"
+ "%s - Could not find any CropRect in the metadata dictionary!\n"
+ "%s - Empty ISP motion data\n"
+ "%s - ExposureTime missing from metadata\n"
+ "%s - Extracting only the first %d ISP Hall samples\n"
+ "%s - FrameRollingShutterSkew missing from metadata\n"
+ "%s - ISP Hall data size did not match expected number of bytes.\n"
+ "%s - ISP Hall data version is not supported.\n"
+ "%s - ISP motion data not available\n"
+ "%s - ISP motion data size did not match expected number of bytes.\n"
+ "%s - ISP motion data version is not supported.\n"
+ "%s - Invalid ISP Hall data\n"
+ "%s - Invalid ISP motion data\n"
+ "%s - Invalid lens coefficients!\n"
+ "%s - Invalid parameter!\n"
+ "%s - LensPositionScalingFactor disagrees by %.2f%% in horizontal (%f) and vertical (%f)\n"
+ "%s - NULL metadata dictionary\n"
+ "%s - No CurrentFocusPosition!\n"
+ "%s - No metadata dictionary!\n"
+ "%s - RawCropRect found in metadata dictionary but malformed!\n"
+ "%s - Sensor crop rect height is not strictly positive!\n"
+ "%s - Sensor crop rect width is not strictly positive!\n"
+ "%s - SensorRawValidBufferRect found in metadata dictionary but malformed!\n"
+ "%s - TotalSensorCropRect found in metadata dictionary but malformed!\n"
+ "%s - Unsupported Hall data version %d\n"
+ "%s - binningFactorHorizontal is not strictly positive!\n"
+ "%s - binningFactorVertical is not strictly positive!\n"
+ "%s - metadataDict is null!\n"
+ "%s - metadataDict or adjustedPrincipalPointOut is null!\n"
+ "FigMotionAdjustPointForSphereMovement"
+ "FigMotionCalculateAdjustedLensPosition"
+ "FigMotionComputeAverageSpherePosition"
+ "FigMotionComputeAverageSpherePositionForTimes"
+ "FigMotionComputeLensPositionScalingFactor"
+ "FigMotionComputePrincipalPoint"
+ "FigMotionGetGravityZ"
+ "FigMotionGetISPHallData"
+ "FigMotionGetSensorValidCropRect"
+ "FigMotionISPHallDataFromCFData"
+ "FigMotionISPMotionDataFromCFData"
+ "com.apple.isp"
+ "general"
- "/Library/Caches/com.apple.xbs/Binaries/AppleH16CameraInterface_NoKext/install/TempContent/Objects/AppleH16CameraInterface.build/H16ISPServices.build/DerivedSources/ExclaveKitIRISPMgrInterface_tightbeam.c"
- "/Library/Caches/com.apple.xbs/Binaries/AppleH16CameraInterface_NoKext/install/TempContent/Objects/AppleH16CameraInterface.build/H16ISPServices.build/DerivedSources/ExclaveKitRGBISPMgrInterface_tightbeam.c"
- "TB_ASSERT: (err == TB_ERROR_SUCCESS) && \"tb_service_connection_message_configure_reply failed\""
- "TB_ASSERT: (server->sendcmdadsettings != NULL) && \"implementation for sendCmdAdSettings is not present\""
- "TB_ASSERT: (server->sendcmdaeflickerfreqset != NULL) && \"implementation for sendCmdAEFlickerFreqSet is not present\""
- "TB_ASSERT: (server->sendcmdchaeframeratemaxget != NULL) && \"implementation for sendCmdChAEFrameRateMaxGet is not present\""
- "TB_ASSERT: (server->sendcmdchaeframeratemaxset != NULL) && \"implementation for sendCmdChAEFrameRateMaxSet is not present\""
- "TB_ASSERT: (server->sendcmdchaeframerateminget != NULL) && \"implementation for sendCmdChAEFrameRateMinGet is not present\""
- "TB_ASSERT: (server->sendcmdchaeframerateminset != NULL) && \"implementation for sendCmdChAEFrameRateMinSet is not present\""
- "TB_ASSERT: (server->sendcmdchaegaincapset != NULL) && \"implementation for sendCmdChAEGainCapSet is not present\""
- "TB_ASSERT: (server->sendcmdchaeinitsettingget != NULL) && \"implementation for sendCmdChAEInitSettingGet is not present\""
- "TB_ASSERT: (server->sendcmdchaeinitsettinggetv2 != NULL) && \"implementation for sendCmdChAEInitSettingGetV2 is not present\""
- "TB_ASSERT: (server->sendcmdchaeintegrationgainset != NULL) && \"implementation for sendCmdChAEIntegrationGainSet is not present\""
- "TB_ASSERT: (server->sendcmdchaeintegrationgainsetv2 != NULL) && \"implementation for sendCmdChAEIntegrationGainSetV2 is not present\""
- "TB_ASSERT: (server->sendcmdchaeintegrationtimemaxset != NULL) && \"implementation for sendCmdChAEIntegrationTimeMaxSet is not present\""
- "TB_ASSERT: (server->sendcmdchaeupdateresume != NULL) && \"implementation for sendCmdChAEUpdateResume is not present\""
- "TB_ASSERT: (server->sendcmdchaeupdatesuspend != NULL) && \"implementation for sendCmdChAEUpdateSuspend is not present\""
- "TB_ASSERT: (server->sendcmdchalgoenable != NULL) && \"implementation for sendCmdChAlgoEnable is not present\""
- "TB_ASSERT: (server->sendcmdchalgoframerate != NULL) && \"implementation for sendCmdChAlgoFrameRate is not present\""
- "TB_ASSERT: (server->sendcmdchconfigurationstatusread != NULL) && \"implementation for sendCmdChConfigurationStatusRead is not present\""
- "TB_ASSERT: (server->sendcmdchdpcset != NULL) && \"implementation for sendCmdChDPCSet is not present\""
- "TB_ASSERT: (server->sendcmdchinfoset != NULL) && \"implementation for sendCmdChInfoSet is not present\""
- "TB_ASSERT: (server->sendcmdchinfoset2 != NULL) && \"implementation for sendCmdChInfoSet2 is not present\""
- "TB_ASSERT: (server->sendcmdchisconcurrent != NULL) && \"implementation for sendCmdChIsConcurrent is not present\""
- "TB_ASSERT: (server->sendcmdchlscset != NULL) && \"implementation for sendCmdChLscSet is not present\""
- "TB_ASSERT: (server->sendcmdchpdpset != NULL) && \"implementation for sendCmdChPdpSet is not present\""
- "TB_ASSERT: (server->sendcmdchrunkitad != NULL) && \"implementation for sendCmdChRunKitAD is not present\""
- "TB_ASSERT: (server->sendcmdchrunkitae != NULL) && \"implementation for sendCmdChRunKitAE is not present\""
- "TB_ASSERT: (server->sendcmdchrunkitaev2 != NULL) && \"implementation for sendCmdChRunKitAEV2 is not present\""
- "TB_ASSERT: (server->sendcmdchrunkitanst != NULL) && \"implementation for sendCmdChRunKitANST is not present\""
- "TB_ASSERT: (server->sendcmdchrunkitanstv150 != NULL) && \"implementation for sendCmdChRunKitANSTV150 is not present\""
- "TB_ASSERT: (server->sendcmdchrunkitattn != NULL) && \"implementation for sendCmdChRunKitAttn is not present\""
- "TB_ASSERT: (server->sendcmdchrunkiter != NULL) && \"implementation for sendCmdChRunKitER is not present\""
- "TB_ASSERT: (server->sendcmdchrunkitfd != NULL) && \"implementation for sendCmdChRunKitFD is not present\""
- "TB_ASSERT: (server->sendcmdchrunkitisp != NULL) && \"implementation for sendCmdChRunKitISP is not present\""
- "TB_ASSERT: (server->sendcmdchsensormetadata != NULL) && \"implementation for sendCmdChSensorMetadata is not present\""
- "TB_ASSERT: (server->sendcmdchsensormetadata2 != NULL) && \"implementation for sendCmdChSensorMetadata2 is not present\""
- "TB_ASSERT: (server->sendcmdchsensormetadatav3 != NULL) && \"implementation for sendCmdChSensorMetadataV3 is not present\""
- "TB_ASSERT: (server->sendcmdchstart != NULL) && \"implementation for sendCmdChStart is not present\""
- "TB_ASSERT: (server->sendcmdchstop != NULL) && \"implementation for sendCmdChStop is not present\""
- "TB_ASSERT: (server->sendcmddebugcapability != NULL) && \"implementation for sendCmdDebugCapability is not present\""
- "TB_ASSERT: (server->sendcmdexclavebootarg != NULL) && \"implementation for sendCmdExclaveBootArg is not present\""
- "TB_ASSERT: (server->sendcmdexclavechcameraconfigset != NULL) && \"implementation for sendCmdExclaveChCameraConfigSet is not present\""
- "TB_ASSERT: (server->sendcmdexclavechpropertyread != NULL) && \"implementation for sendCmdExclaveChPropertyRead is not present\""
- "TB_ASSERT: (server->sendcmdexclavechpropertywrite != NULL) && \"implementation for sendCmdExclaveChPropertyWrite is not present\""
- "TB_ASSERT: (server->sendcmdexclaveisphwirq != NULL) && \"implementation for sendCmdExclaveISPHWIRQ is not present\""
- "TB_ASSERT: (server->sendcmdexfiltration != NULL) && \"implementation for sendCmdExfiltration is not present\""
- "TB_ASSERT: (server->sendcmdinfiltration != NULL) && \"implementation for sendCmdInfiltration is not present\""
- "TB_ASSERT: (server->sendcmdoff != NULL) && \"implementation for sendCmdOff is not present\""
- "TB_ASSERT: (server->sendcmdon != NULL) && \"implementation for sendCmdOn is not present\""
- "TB_FATAL: invalid value: unexpected case value, %llx"
- "TB_FATAL: invalid value: unexpected case value, %llx (%s:%d)\n"
- "TB_FATAL: unrecognized selector: %llu"
- "TB_FATAL: unrecognized selector: %llu (%s:%d)\n"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
