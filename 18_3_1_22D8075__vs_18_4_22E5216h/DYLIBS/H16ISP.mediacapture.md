## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.415.0.0.0
-  __TEXT.__text: 0x1c155c
-  __TEXT.__auth_stubs: 0x3390
+3.509.0.0.0
+  __TEXT.__text: 0x1b24fc
+  __TEXT.__auth_stubs: 0x3180
   __TEXT.__init_offsets: 0x18
-  __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x6494
-  __TEXT.__const: 0x22bcc
-  __TEXT.__cstring: 0x196f7
-  __TEXT.__oslogstring: 0x1b4a6
-  __TEXT.__unwind_info: 0x3e88
-  __TEXT.__eh_frame: 0x98
+  __TEXT.__objc_methlist: 0x268
+  __TEXT.__const: 0x236af
+  __TEXT.__oslogstring: 0x1c4ce
+  __TEXT.__cstring: 0x185e5
+  __TEXT.__gcc_except_tab: 0x64f8
+  __TEXT.__unwind_info: 0x3ca0
+  __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x1c61
-  __TEXT.__objc_methtype: 0x124e
-  __TEXT.__objc_stubs: 0x1f60
-  __DATA_CONST.__got: 0x3158
-  __DATA_CONST.__const: 0x86d0
+  __TEXT.__objc_methname: 0x1cbd
+  __TEXT.__objc_methtype: 0x105f
+  __TEXT.__objc_stubs: 0x1f80
+  __DATA_CONST.__got: 0x3238
+  __DATA_CONST.__const: 0xa270
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x808
+  __DATA_CONST.__objc_selrefs: 0x8a0
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x19d8
+  __AUTH_CONST.__auth_got: 0x18d0
   __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x2460
+  __AUTH_CONST.__const: 0x2718
   __AUTH_CONST.__cfstring: 0x9c00
-  __AUTH_CONST.__objc_const: 0xae0
+  __AUTH_CONST.__objc_const: 0x880
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x269620
-  __DATA.__bss: 0xf9
+  __DATA.__data: 0x334648
+  __DATA.__bss: 0x1f1
   __DATA.__common: 0x54
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x108
-  __DATA_DIRTY.__bss: 0x934
-  __DATA_DIRTY.__common: 0x5528
+  __DATA_DIRTY.__data: 0x118
+  __DATA_DIRTY.__bss: 0x94c
+  __DATA_DIRTY.__common: 0x5558
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA
   - /System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth
   - /System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore
-  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore
+  - /System/Library/PrivateFrameworks/CMCaptureDevice.framework/CMCaptureDevice
   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5846
-  Symbols:   9561
-  CStrings:  6394
+  Functions: 5459
+  Symbols:   8905
+  CStrings:  6465
 
Symbols:
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _CVAFaceTrackingLiteCopyDecodedOutput
+ _FigCFEqual
+ _FigGetUpTime
+ _OBJC_CLASS_$_ADCameraCalibration
+ __Z20FigMotionGetGravityZPK14__CFDictionaryPf
+ __Z30FigMotionComputePrincipalPointPK14__CFDictionaryffdiiiihP7CGPoint
+ __Z37FigMotionAdjustPointForSphereMovementPK14__CFDictionaryffdP7CGPoint
+ __Z37FigMotionComputeAverageSpherePositionPK14__CFDictionarydP11FigPosition
+ __Z38FigMotionCalculateAdjustedLensPositionPK14__CFDictionaryfP26CameraCharacterizationDatafPf
+ __Z39FigMotionCalculateAdjustedFocusPositionffPi
+ __Z41FigMotionComputeLensPositionScalingFactorPK14__CFDictionaryiiiiPf
+ __ZN20GMCProcessorInternal21updatePCECalibWithISFEddddP22H16ISPAnalyticsGMCInfoRK26sCIspCmdChPearlCalibrationRS2_
+ __ZN26H16ISPGraphExclaveANDKNode19onMessageProcessingEPN6H16ISP24H16ISPFilterGraphMessageE
+ __ZN26H16ISPGraphExclaveANDKNodeC2EPN6H16ISP12H16ISPDeviceEj14ExclaveKitType
+ __ZN29H16ISPGraphExclaveRGBANDKNode16runANDKAlgorithmEPN6H16ISP24H16ISPFilterGraphMessageE
+ __ZN29H16ISPGraphExclaveRGBANDKNodeC1EPN6H16ISP12H16ISPDeviceEj
+ __ZN29H16ISPGraphExclaveRGBANDKNodeC2EPN6H16ISP12H16ISPDeviceEj
+ __ZN6H16ISP12H16ISPDevice10EnableHITHEjbbtt
+ __ZN6H16ISP12H16ISPDevice10EnableWSEGEjbhtt
+ __ZN6H16ISP12H16ISPDevice25ISP_GeneralProcessBuffersEP37H16ISPGeneralProcessBuffersArgsStructj
+ __ZN6H16ISP12H16ISPDevice25SetRationalFrameRateRangeEjbP29H16ISPRationalFrameRateStructS2_
+ __ZN6H16ISP12H16ISPDevice30SetExternalSyncConfigFrameRateEj29H16ISPRationalFrameRateStruct
+ __ZN6H16ISP12H16ISPDevice33EnableAWBMultiStatisticsAveragingEjb
+ __ZN6H16ISP19H16ISPFrameReceiverC1EPNS_12H16ISPDeviceEjP21H16ISPTNRConfigStruct29H16ISPRationalFrameRateStructS5_
+ __ZN6H16ISP19H16ISPFrameReceiverC2EPNS_12H16ISPDeviceEjP21H16ISPTNRConfigStruct29H16ISPRationalFrameRateStructS5_
+ __ZN6H16ISP21H16ISPJasperDepthNode13processJasperEyP10__CVBufferP14__CFDictionary
+ __ZN6H16ISP23DepthRearConfigurations8supportsEj
+ __ZN6H16ISP24DepthFrontConfigurations8supportsEj15ePearlHWVersion
+ __ZN6H16ISP26H16ISPPearlCalibrationNodeC1EPNS_12H16ISPDeviceEPFvRN3Isf10IsfHistoryER38H16ISPAnalyticsIsfHistoricalThresholdsPvEPFvRKS4_RKS6_S8_EPFvR26sCIspCmdChPearlCalibrationS8_Eb20kFigIsfStepDetectionPbP16RgbIrCalibrationS8_
+ __ZN6H16ISP26H16ISPPearlCalibrationNodeC2EPNS_12H16ISPDeviceEPFvRN3Isf10IsfHistoryER38H16ISPAnalyticsIsfHistoricalThresholdsPvEPFvRKS4_RKS6_S8_EPFvR26sCIspCmdChPearlCalibrationS8_Eb20kFigIsfStepDetectionPbP16RgbIrCalibrationS8_
+ __ZN6H16ISP30H16ISPPearlCalibrationNodeBaseC2EPNS_12H16ISPDeviceEb20kFigIsfStepDetectionb
+ __ZN6H16ISP31DepthFrontRotatedConfigurations8supportsEj15ePearlHWVersion
+ __ZN6H16ISP31H16ISPPearlCalibrationNode_RGBPC1EPNS_12H16ISPDeviceEPNS_20H16ISPServicesRemoteEbPK14__CFDictionarydb
+ __ZN6H16ISP31H16ISPPearlCalibrationNode_RGBPC2EPNS_12H16ISPDeviceEPNS_20H16ISPServicesRemoteEbPK14__CFDictionarydb
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode14updateTestModeEb
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode17updateObjectDictsEPNS_24H16ISPFilterGraphMessageE22PerceptionReturnStatus
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode19asyncUpdateTestModeEb
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNodeC1EPNS_12H16ISPDeviceEjb
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNodeC2EPNS_12H16ISPDeviceEjb
+ __ZN6H16ISP33H16ISPPearlCalibrationNode_RemoteC1EPNS_12H16ISPDeviceEPNS_20H16ISPServicesRemoteEb20kFigIsfStepDetectionbb
+ __ZN6H16ISP33H16ISPPearlCalibrationNode_RemoteC2EPNS_12H16ISPDeviceEPNS_20H16ISPServicesRemoteEb20kFigIsfStepDetectionbb
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode10onActivateEv
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode12onDeactivateEv
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode29AddSecureTrackedFacesMetadataEPNS_24H16ISPFilterGraphMessageERK37ISPExclaveCoreChRunKitFaceProcessRsltb
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeD0Ev
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeD1Ev
+ __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeD2Ev
+ __ZN6H16ISP35H16ISPTimeOfFlightColorSynchronizer8activateEPK8__CFDatajjPv
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNode18runMotionDetectionEPNS_24H16ISPFilterGraphMessageEb
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode17AddFaceIDMetadataEPNS_24H16ISPFilterGraphMessageEP28ISPExclaveCoreChRunKitADRsltb
+ __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNode10onActivateEv
+ __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNode12onDeactivateEv
+ __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeD0Ev
+ __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeD1Ev
+ __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeD2Ev
+ __ZNK11IsfInternal20getHistoryStatisticsERN3Isf20IsfHistoryStatisticsE
+ __ZNK11IsfInternal24getHistoryAxisStatisticsEiRN3Isf24IsfHistoryAxisStatisticsE
+ __ZNK18H16ISPFirmwareWork17IsInternalVariantEv
+ __ZNK3Isf20getHistoryStatisticsERNS_20IsfHistoryStatisticsE
+ __ZTI26H16ISPGraphExclaveANDKNode
+ __ZTI29H16ISPGraphExclaveRGBANDKNode
+ __ZTIN6H16ISP32H16ISPGraphExclavePerceptionNodeE
+ __ZTIN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeE
+ __ZTIN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeE
+ __ZTIN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeE
+ __ZTS26H16ISPGraphExclaveANDKNode
+ __ZTS29H16ISPGraphExclaveRGBANDKNode
+ __ZTSN6H16ISP32H16ISPGraphExclavePerceptionNodeE
+ __ZTSN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeE
+ __ZTSN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeE
+ __ZTSN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeE
+ __ZTV26H16ISPGraphExclaveANDKNode
+ __ZTV29H16ISPGraphExclaveRGBANDKNode
+ __ZTVN6H16ISP32H16ISPGraphExclavePerceptionNodeE
+ __ZTVN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeE
+ __ZTVN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeE
+ __ZTVN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeE
+ _kFigCaptureStreamDetectedObjectKey_SentToPerceptionThumbnailChannel
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SVDResultEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceIDReadinessConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceIDReadinessEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceTrackingConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceTrackingEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureMotionToWakeConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureMotionToWakeEnabled
+ _kFigCaptureStreamMetadataOutputKey_SVDResult
+ _kFigCaptureStreamMetadataOutputKey_SecureFaceIDReadiness
+ _kFigCaptureStreamMetadataOutputKey_SecureMotionToWake
+ _kFigCaptureStreamMetadataOutputKey_SecureTrackedFaces
+ _kFigCaptureStreamMetadata_PortType
+ _kFigCaptureStreamSecureFaceIDReadinessConfigurationKey_AttentionRequired
+ _kFigCaptureStreamSecureFaceIDReadinessConfigurationKey_PeriocularEnabled
+ _kFigCaptureStreamSecureFaceIDReadinessKey_CoachingStatus
+ _kFigCaptureStreamSecureFaceIDReadinessKey_Ready
+ _kFigCaptureStreamSecureFaceIDReadinessKey_UserEngagementStatus
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_NetworkFailureThresholdMultiplier
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_NumTrackedFaces
+ _kFigCaptureStreamSecureMotionToWakeConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamSecureMotionToWakeKey_DetectedMotion
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_FaceOcclusionDetectionEnabled
+ _kFigCaptureStreamStillImageCaptureNow_FrameParam_FocusPosition
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_TestMode
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_ThumbnailStreamMetadataObjectTypes
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_ThumbnailStreamTargetFrameRate
+ _kFigCaptureSynchronizedStreamsGroupProperty_AWBStatisticsAveragingEnabled
+ _objc_retainAutoreleaseReturnValue
+ _oidQCCompliance
+ _oidQCDisclosures
+ _oidQCEuRetentionPeriod
+ _oidQCLimitValue
+ _oidQCStatements
+ _oidQCSyntaxv1
+ _oidQCSyntaxv2
+ _oidQCType
+ _oidQCTypeEseal
+ _oidQCTypeEsign
+ _oidQCTypeWeb
+ _oidSemanticsIdEidasLegal
+ _oidSemanticsIdEidasNatural
+ _oidSemanticsIdLegal
+ _oidSemanticsIdNatural
+ _os_variant_allows_internal_security_policies
+ _os_variant_has_internal_content
- _FigMotionCalculateAdjustedLensPosition
- _FigMotionComputeLensPositionScalingFactor
- _FigMotionComputePrincipalPoint
- _FigMotionGetGravityZ
- __ZN12GMCProcessor20postProcessStereoGMCE12_GMC_Results26sCIspCmdChPearlCalibration18GMCInnerStatisticsyb
- __ZN20GMCProcessorInternal21updatePCECalibWithISFEddddRK26sCIspCmdChPearlCalibrationRS0_
- __ZN6H16ISP12H16ISPDevice10EnableHITHEjb
- __ZN6H16ISP12H16ISPDevice17isConclaveRunningEj
- __ZN6H16ISP19H16ISPFrameReceiverC1EPNS_12H16ISPDeviceEjP21H16ISPTNRConfigStructjj
- __ZN6H16ISP19H16ISPFrameReceiverC2EPNS_12H16ISPDeviceEjP21H16ISPTNRConfigStructjj
- __ZN6H16ISP21H16ISPJasperDepthNode13processJasperEPNS_24H16ISPFilterGraphMessageE
- __ZN6H16ISP22H16ISPExclaveGraphNode14ConclaveClientEv
- __ZN6H16ISP23DepthRearConfigurations8supportsEjPK24H16ISPPlatformInfoStruct
- __ZN6H16ISP26H16ISPPearlCalibrationNodeC1EPNS_12H16ISPDeviceEPFvRN3Isf10IsfHistoryER38H16ISPAnalyticsIsfHistoricalThresholdsPvEPFvRKS4_RKS6_S8_EPFvR26sCIspCmdChPearlCalibrationS8_Ebb20kFigIsfStepDetectionPbP16RgbIrCalibrationS8_
- __ZN6H16ISP26H16ISPPearlCalibrationNodeC2EPNS_12H16ISPDeviceEPFvRN3Isf10IsfHistoryER38H16ISPAnalyticsIsfHistoricalThresholdsPvEPFvRKS4_RKS6_S8_EPFvR26sCIspCmdChPearlCalibrationS8_Ebb20kFigIsfStepDetectionPbP16RgbIrCalibrationS8_
- __ZN6H16ISP30H16ISPPearlCalibrationNodeBase14dropPDEBuffersEPNS_24H16ISPFilterGraphMessageEt
- __ZN6H16ISP30H16ISPPearlCalibrationNodeBaseC2EPNS_12H16ISPDeviceEbb20kFigIsfStepDetectionb
- __ZN6H16ISP31H16ISPPearlCalibrationNode_RGBPC1EPNS_12H16ISPDeviceEPNS_20H16ISPServicesRemoteEbbPK14__CFDictionarydb
- __ZN6H16ISP31H16ISPPearlCalibrationNode_RGBPC2EPNS_12H16ISPDeviceEPNS_20H16ISPServicesRemoteEbbPK14__CFDictionarydb
- __ZN6H16ISP33H16ISPPearlCalibrationNode_RemoteC1EPNS_12H16ISPDeviceEPNS_20H16ISPServicesRemoteEbb20kFigIsfStepDetectionbb
- __ZN6H16ISP33H16ISPPearlCalibrationNode_RemoteC2EPNS_12H16ISPDeviceEPNS_20H16ISPServicesRemoteEbb20kFigIsfStepDetectionbb
- __ZN6H16ISP35H16ISPTimeOfFlightColorSynchronizer8activateEPK8__CFDatajj
- __os_crash
- _fmod
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
- _kFigCaptureStreamMetadata_AttentionConfidenceLevel
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
+ "%s - ANDK Graph Node Message invalid\n"
+ "%s - Camera Config Set Failed, err %d \n"
+ "%s - Cannot find metadata dictionary!\n"
+ "%s - Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f].\n"
+ "%s - Could not find any CropRect in the metadata dictionary!\n"
+ "%s - DetectedFaces=%u, TrackedFaces=%u\n"
+ "%s - Empty ISP motion data\n"
+ "%s - ExposureTime missing from metadata\n"
+ "%s - Extracting only the first %d ISP Hall samples\n"
+ "%s - Face ID PreCheck uxFeedback=0x%08X, hasAttention=%{bool}d, isUserEngaged=%{bool}d\n"
+ "%s - Failed to configure exclave auto exposure on channel=%u\n"
+ "%s - Failed to configure exclave camera settings on channel=%d\n"
+ "%s - Failed to get distortion data! Defaulting extrinsics to identity!\n"
+ "%s - Failed to run ANDK algorithm, ret=0x%X\n"
+ "%s - Failure in setting initial AE setting for channel %d, ret=0x%08X\n"
+ "%s - FrameRollingShutterSkew missing from metadata\n"
+ "%s - Got an unsupported perception object string! Skipping.\n"
+ "%s - ISP Hall data size did not match expected number of bytes.\n"
+ "%s - ISP Hall data version is not supported.\n"
+ "%s - ISP motion data not available\n"
+ "%s - ISP motion data size did not match expected number of bytes.\n"
+ "%s - ISP motion data version is not supported.\n"
+ "%s - Invalid Binning Mode! CISP_CAMERA_CONFIG_BINNING = %u\n"
+ "%s - Invalid ISP Hall data\n"
+ "%s - Invalid ISP motion data\n"
+ "%s - Invalid lens coefficients!\n"
+ "%s - Invalid parameter!\n"
+ "%s - LensPositionScalingFactor disagrees by %.2f%% in horizontal (%f) and vertical (%f)\n"
+ "%s - Missing output descriptors\n"
+ "%s - More than %d outputs\n"
+ "%s - NULL metadata dictionary\n"
+ "%s - No CurrentFocusPosition!\n"
+ "%s - No metadata dictionary!\n"
+ "%s - Processing session not prepared!\n"
+ "%s - RawCropRect found in metadata dictionary but malformed!\n"
+ "%s - Sensor crop rect height is not strictly positive!\n"
+ "%s - Sensor crop rect width is not strictly positive!\n"
+ "%s - SensorRawValidBufferRect found in metadata dictionary but malformed!\n"
+ "%s - TotalSensorCropRect found in metadata dictionary but malformed!\n"
+ "%s - Unexpected GMC type %d\n"
+ "%s - Unsupported Hall data version %d\n"
+ "%s - [Exclaves]: EK Face Kit Runkit failed, idl error=%d\n"
+ "%s - [Exclaves]: H16ISPGraphExclaveFaceTrackingNode::%s index: %zu AngleInfoRoll: %f Rect[%f %f %f %f] Confidence %f \n"
+ "%s - [Exclaves]: IR EK Object Detection RunKit failed, EK result=%{bool}d\n"
+ "%s - [Exclaves]: Perception - Frame was skipped!\n"
+ "%s - [Exclaves]: Perception - Frame was unable to be queued!\n"
+ "%s - [Exclaves]: RGB Face Tracking: channel=%u\n"
+ "%s - [Exclaves]: face tracking secondary process failed! idl error=%u\n"
+ "%s - [Exclaves]: perception failed to run idl error=%u\n"
+ "%s - baseline streaming frameRate=%f\n"
+ "%s - binningFactorHorizontal is not strictly positive!\n"
+ "%s - binningFactorVertical is not strictly positive!\n"
+ "%s - failed to allocate dictionary\n"
+ "%s - failed to extract %s target frame rate\n"
+ "%s - failed to extract buffer height\n"
+ "%s - failed to extract buffer width\n"
+ "%s - failed to update AE maximum frame rate ret=0x%08x\n"
+ "%s - failed to update AE minimum frame rate ret=0x%08x\n"
+ "%s - failed to update exclave frame rate ret=0x%08x\n"
+ "%s - failed to update still image configuration ret=0x%08x\n"
+ "%s - focalLength=%f, isValid=%hhu, modeBinW=%hhu, modeBinH=%hhu, centerX=%u, centerY=%u, requestID=0x%08X\n"
+ "%s - gdcPriDistDataAvailable was not set! Defaulting extrinsics to identity!\n"
+ "%s - illegal RPC access\n"
+ "%s - invalid %s target frame rate value\n"
+ "%s - invalid attempt to set negative %s target frame rate\n"
+ "%s - invalid configuration value\n"
+ "%s - invalid enablement value\n"
+ "%s - metadataDict is null!\n"
+ "%s - metadataDict or adjustedPrincipalPointOut is null!\n"
+ "%s - new intermediate tap output height failed buffer pool check ret=0x%08x\n"
+ "%s - new intermediate tap output width failed buffer pool check ret=0x%08x\n"
+ "%s - new output height=%d exceeds current buffer height=%d\n"
+ "%s - new output height=%d exceeds current buffer height=%u\n"
+ "%s - new output width=%d exceeds current buffer width=%d\n"
+ "%s - new output width=%d exceeds current buffer width=%u\n"
+ "%s - new primary scaler output height failed buffer pool check ret=0x%08x\n"
+ "%s - new primary scaler output width failed buffer pool check ret=0x%08x\n"
+ "%s - new secondary scaler output height failed buffer pool check ret=0x%08x\n"
+ "%s - new secondary scaler output width failed buffer pool check ret=0x%08x\n"
+ "%s - new still image output height failed buffer pool check ret=0x%08x\n"
+ "%s - new still image output width failed buffer pool check ret=0x%08x\n"
+ "%s - pixel buffer attributes not found\n"
+ "%s - still image buffer pool not found\n"
+ "%s - unrecognized motion trigger result\n"
+ "%s - volatile key must be specified as boolean\n"
+ "%s-Ch%d.DAT"
+ "/private/var/mobile/tmp/com.apple.cameracaptured/"
+ "/usr/local/share/firmware/isp/3525_02XX.dat"
+ "/usr/local/share/firmware/isp/7525_01XX.dat"
+ "/usr/local/share/firmware/isp/CmPM-CALm"
+ "/usr/local/share/firmware/isp/CmPM-DPCd"
+ "/usr/local/share/firmware/isp/CmPM-DPCm"
+ "/usr/local/share/firmware/isp/CmPM-brcl"
+ "/usr/local/share/firmware/isp/CmPM-brgd"
+ "/usr/local/share/firmware/isp/CmPM-dcnu"
+ "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
+ "ANDK runkit ch=%u reqid=0x%08x\n"
+ "AddFaceIDMetadata"
+ "AddSecureTrackedFacesMetadata"
+ "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
+ "BinningModeToFactor"
+ "CheckOutputHeightAgainstPool"
+ "CheckOutputWidthAgainstPool"
+ "ColorRangeForOutputWithMatrix"
+ "ConfigureFrameworkAutoExposure"
+ "ConfigureFrameworkCameraSettings"
+ "Correspondences"
+ "CurrentFrameRate: %f\n"
+ "DeactivateIntermediateTapOutputInFrameReceiver: EnableScalerOutput: res=0x%08X\n\n"
+ "EK ANDK RunKit Command failed, ret=%d\n"
+ "EXCLAVE_EMPTY_QUEUE_ENABLE ch 0x%x tailspinCode 0x%x"
+ "EXCLAVE_SOURCE_AE_REQ_LATE ch 0x%x tailspinCode 0x%x"
+ "EnableV5LTMMetadata"
+ "ExclavePreferenceClearValuesOnFirstLaunchInternal"
+ "ExclaveSetANDKFrameRateBucket"
+ "ExclaveSetMaximumAutoExposureFrameRate"
+ "ExclaveSetMaximumFrameRateNow"
+ "ExclaveSetMinimumAutoExposureFrameRate"
+ "ExclaveSetMinimumFrameRateNow"
+ "ExposureTime: %d (us)\n"
+ "FaceHeight"
+ "FaceWidth"
+ "FaceX"
+ "FaceY"
+ "Failed, too many events - Stop logging!.\n"
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
+ "FillExtrinsicCalibrationData"
+ "H16ISPGraphExclaveFaceTrackingSecondaryNode::onActivate\n"
+ "H16ISPGraphExclaveFaceTrackingSecondaryNode::onDeactivate\n"
+ "ISPDebugTreatPropertyWriteKeysAsVolatile"
+ "IsfDifferenceXMaxMin"
+ "IsfDifferenceXQ31"
+ "IsfDifferenceYMaxMin"
+ "IsfDifferenceYQ31"
+ "IsfDifferenceZMaxMin"
+ "IsfDifferenceZQ31"
+ "LSC_GET_BASE_U32_PT(chInfo1[ch]) % (chInfo1[ch]->gridCountX * chInfo1[ch]->gridCountY) == 0"
+ "LSC_GET_BASE_U32_PT(chInfo2[ch]) % (chInfo2[ch]->gridCountX * chInfo2[ch]->gridCountY) == 0"
+ "LuxLevel: %d\n"
+ "MotionDetectionResultCreateDictionaryRepresentation"
+ "Pearl Calibration (MI): Current session isn't suitable for algorithm (square color buffers)\n"
+ "Pearl Calibration (MI): Projector GMC hasn't completed yet\n"
+ "QuadraBinningFactor: %d\n"
+ "Savage/SavagePatch%s.DAT"
+ "SecureAlgorithmSetEnabled"
+ "SecureAlgorithmSetTargetFrameRate"
+ "SecureMotionToWakeSetConfiguration"
+ "SetAWBStatisticsAveragingEnabled - ActiveStreamsArray must not be Null\n"
+ "SetAWBStatisticsAveragingEnabled - failed to set AWBStatisticsAveraging, result = 0x%08X\n\n"
+ "SetMinimumFrameRateNow"
+ "Skip configuring initial AE settings, ch %d\n"
+ "StillImageConfigUpdateAtomically"
+ "TailspinNotification"
+ "TailspinNotification unknown messageType 0x%08x\n"
+ "TemperatureDiffSincePrevConvergence"
+ "TimeSincePrevConvergence"
+ "TriggeringReason"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%s CVAFaceTrackingLiteCopyDecodedOutput failed, err=0x%08X \n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%s RunKit FT reqID:0x%08x channel %d\n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%s Skipped processing secure face tracking algorithm\n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::onActivate\n"
+ "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::onDeactivate\n"
+ "[Exclaves]: Face crop score is %f (i.e., no face in FOV). Return empty dictionary\n"
+ "[Exclaves]: channel=%u runSecondaryProcessing=%{bool}d requestID=0x%08x\n"
+ "[Exclaves]: running perception ch=%u publishResult=%{bool}d reqid=0x%08x\n"
+ "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
+ "chInfo1[ch]->gridCountX == chInfo1[0]->gridCountX"
+ "chInfo1[ch]->gridCountY == chInfo1[0]->gridCountY"
+ "chInfo2[ch]->gridCountX == chInfo2[0]->gridCountX"
+ "chInfo2[ch]->gridCountY == chInfo2[0]->gridCountY"
+ "daemon"
+ "dumpTailspinInBackground dirAndPrefix %s reason %s requested but tailspins not supported\n"
+ "failed to run motion detection reqid=0x%08x err=%u hasValidResult=%{bool}d\n"
+ "initWithIntrinsics:cameraToPlatformTransform:pixelSize:referenceDimensions:distortionModel:"
+ "kH16ISPTailspinAEReqLate ch %u tailspinCode 0x%08x\n"
+ "kH16ISPTailspinExclaveEmptyQueue ch %u tailspinCode 0x%08x\n"
+ "motion to wake"
+ "object detection"
+ "oisSample: ts=0x%016llX  Xt=%-10.5f  Yt=%-10.5f  H1=%-5d  H2=%-5d  B1=%-5d  B2=%-5d  Xe=%-10.5f  Ye=%-10.5f  temp=%-5d\n           H1_bz_corr=%-10.5f  H2_bz_corr=%-10.5f  H1_to_um_X=%-10.5f  H1_to_um_Y=%-10.5f  H2_to_um_X=%-10.5f  H2_to_um_Y=%-10.5f  B1_to_um_X=%-10.5f\n           B1_to_um_Y=%-10.5f  B2_to_um_X=%-10.5f  B2_to_um_Y=%-10.5f  power=0x%04X  oisS1Temp=%-10.5f  oisS2Temp=%-10.5f \n"
+ "perception"
+ "runkit motion detection ch=%u publishResult=%{bool}d reqid=0x%08x\n"
+ "tailspinDir"
+ "updateObjectDicts"
- "%s - Camera Config Set Failed, ret %d \n"
- "%s - Conclave not running for EKType: %s\n"
- "%s - Could not set strobe state, res = 0x%x\n\n"
- "%s - Exclave algos are enabled but no conclaves are running!\n"
- "%s - Failed to configure exclave AE on channel=%d\n"
- "%s - Failure in setting initial AE setting for channel %d, res=0x%08X\n"
- "%s - IR-RGB\n"
- "%s - In concurrent streaming mode - Skip configuring Exclave AE\n"
- "%s - Stereo GMC reporting analytics\n"
- "%s - Stereo-GMC post processing done\n"
- "%s - [Exclaves]: IR EK Object Detection RunKit failed, tberr=%d EK result=%{bool}d\n"
- "%s - channel=%u failed to enable filtration\n"
- "%s - channel=%u failed to enable skip frame dump\n"
- "%s - channel=%u failed to set replay control\n"
- "%s - new intermediate tap output height=%d exceeds current buffer height=%u\n"
- "%s - new intermediate tap output width=%d exceeds current buffer width=%u\n"
- "%s - new primary scaler output height=%d exceeds current buffer height=%u\n"
- "%s - new primary scaler output width=%d exceeds current buffer width=%u\n"
- "%s - new secondary scaler output height=%d exceeds current buffer height=%u\n"
- "%s - new secondary scaler output width=%d exceeds current buffer width=%u\n"
- "%s - pixel buffer attributes not found for intermediate tap output\n"
- "%s - pixel buffer attributes not found for primary scaler output\n"
- "%s - pixel buffer attributes not found for secondary scaler output\n"
- "%s - pixel buffer height not found for intermediate tap output\n"
- "%s - pixel buffer height not found for primary scaler output\n"
- "%s - pixel buffer height not found for secondary scaler output\n"
- "%s - pixel buffer width not found for intermediate tap output\n"
- "%s - pixel buffer width not found for primary scaler output\n"
- "%s - pixel buffer width not found for secondary scaler output\n"
- "%s - unable to configure exclave graph, res=%d\n"
- "/Library/Caches/com.apple.xbs/Binaries/AppleH16CameraInterface_NoKext/install/TempContent/Objects/AppleH16CameraInterface.build/H16ISP.build/DerivedSources/ExclaveKitIRISPMgrInterface_tightbeam.c"
- "/Library/Caches/com.apple.xbs/Binaries/AppleH16CameraInterface_NoKext/install/TempContent/Objects/AppleH16CameraInterface.build/H16ISP.build/DerivedSources/ExclaveKitRGBISPMgrInterface_tightbeam.c"
- "/usr/local/share/firmware/isp/CmPM-CALm.DAT"
- "/usr/local/share/firmware/isp/CmPM-DPCd.DAT"
- "/usr/local/share/firmware/isp/CmPM-DPCm.DAT"
- "/usr/local/share/firmware/isp/CmPM-brcl.DAT"
- "/usr/local/share/firmware/isp/CmPM-brgd.DAT"
- "/usr/local/share/firmware/isp/CmPM-dcnu.DAT"
- "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
- "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
- "B3"
- "BA"
- "ColorRangeForOutput"
- "ConfigureExclaveAutoExposure"
- "ExclavePreferenceApplyFiltrationValues"
- "FlowAccumulate"
- "FlowAccumulateNeon64"
- "FlowAccumulateScalar"
- "FlowEstimateGainError"
- "H16ISPCaptureStreamStart - Failed to configure exclave graph: 0x%08X\n\n"
- "ISPDebugDumpSkipFrame"
- "ISPDebugFiltration"
- "ISPDebugReplayCtl"
- "PassCalibrationFrames"
- "Pearl Calibration (MI): Projector GMC hasn't completed yet - dropping depth/dx buffers\n"
- "RGB"
- "Savage/SavagePatch%s%s.DAT"
- "SetTorchLevel"
- "SetTorchManualParameters"
- "SetTorchSegmentParameters"
- "Skip configuring initial AE settings, resultStatus %d ch %d\n"
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
- "[Exclaves]: Face confidence is less than 0.0 (i.e., no face in FOV). Return empty dictionary\n"
- "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "com.apple.H16ispjasperdepthnode.activate"
- "failed, event-logging array is not set up correctly.\n"
- "generalProcess failed: outputDescriptor is NULL\n"
- "isConclaveRunning"
- "oisSample: ts=0x%016llX  Xt=%-10.5f  Yt=%-10.5f  H1=%-5d  H2=%-5d  B1=%-5d  B2=%-5d  Xe=%-10.5f  Ye=%-10.5f  temp=%-5d\n           H1_bz_corr=%-10.5f  H2_bz_corr=%-10.5f  H1_to_um_X=%-10.5f  H1_to_um_Y=%-10.5f  H2_to_um_X=%-10.5f  H2_to_um_Y=%-10.5f  B1_to_um_X=%-10.5f\n           B1_to_um_Y=%-10.5f  B2_to_um_X=%-10.5f  B2_to_um_Y=%-10.5f  power=0x%04X\n"
- "postProcessStereoGMC_block_invoke"

```
