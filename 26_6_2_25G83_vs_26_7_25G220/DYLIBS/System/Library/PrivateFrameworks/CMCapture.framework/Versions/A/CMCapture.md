## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture`

```diff

 665.140.6.0.0
-  __TEXT.__text: 0x37e4dc
+  __TEXT.__text: 0x37ff70
   __TEXT.__auth_stubs: 0x3e20
-  __TEXT.__objc_methlist: 0x24974
-  __TEXT.__cstring: 0x58a68
+  __TEXT.__objc_methlist: 0x24b24
+  __TEXT.__cstring: 0x58e35
   __TEXT.__const: 0x142b78
   __TEXT.__gcc_except_tab: 0x1358
   __TEXT.__oslogstring: 0x25692
   __TEXT.__dlopen_cstrs: 0x1e4
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x8dd8
+  __TEXT.__unwind_info: 0x8df0
   __TEXT.__objc_classname: 0x4d82
-  __TEXT.__objc_methname: 0x81311
+  __TEXT.__objc_methname: 0x81a35
   __TEXT.__objc_methtype: 0xeb64
-  __TEXT.__objc_stubs: 0x32cc0
-  __DATA_CONST.__got: 0x5c38
-  __DATA_CONST.__const: 0x5350
+  __TEXT.__objc_stubs: 0x32f80
+  __DATA_CONST.__got: 0x5cc0
+  __DATA_CONST.__const: 0x5390
   __DATA_CONST.__objc_classlist: 0x1178
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfd50
+  __DATA_CONST.__objc_selrefs: 0xfe00
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1068
-  __DATA_CONST.__objc_arraydata: 0x14c0
+  __DATA_CONST.__objc_arraydata: 0x14d8
   __AUTH_CONST.__auth_got: 0x1f20
   __AUTH_CONST.__const: 0x4e10
-  __AUTH_CONST.__cfstring: 0x34f80
-  __AUTH_CONST.__objc_const: 0x67488
-  __AUTH_CONST.__objc_intobj: 0x36d8
+  __AUTH_CONST.__cfstring: 0x35340
+  __AUTH_CONST.__objc_const: 0x677b8
+  __AUTH_CONST.__objc_intobj: 0x3738
   __AUTH_CONST.__objc_arrayobj: 0x10f8
   __AUTH_CONST.__objc_doubleobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x1ae0
-  __DATA.__objc_ivar: 0x7b48
+  __DATA.__objc_ivar: 0x7b90
   __DATA.__data: 0x263c
   __DATA.__common: 0xb20
   __DATA_DIRTY.__objc_data: 0x93d0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21461
-  Symbols:   42749
-  CStrings:  29735
+  Functions: 21513
+  Symbols:   42857
+  CStrings:  29812
 
Symbols:
+ -[BWMultiStreamCameraSourceNode setDeviceProximityDetectionDeviceTypes:]
+ -[BWMultiStreamCameraSourceNode setDeviceProximityDetectionTargetFrameRate:]
+ -[BWMultiStreamCameraSourceNode setLightSourceEstimationAmbientLuminance:]
+ -[BWMultiStreamCameraSourceNode setLightSourceEstimationTargetFrameRate:]
+ -[BWSecureMetadataOutputConfiguration deviceProximityDetectionDeviceTypes]
+ -[BWSecureMetadataOutputConfiguration deviceProximityDetectionEnabled]
+ -[BWSecureMetadataOutputConfiguration deviceProximityDetectionTargetFrameRate]
+ -[BWSecureMetadataOutputConfiguration lightSourceEstimationAmbientLuminance]
+ -[BWSecureMetadataOutputConfiguration lightSourceEstimationEnabled]
+ -[BWSecureMetadataOutputConfiguration lightSourceEstimationTargetFrameRate]
+ -[BWSecureMetadataOutputConfiguration perceptionTestModeEnabled]
+ -[BWSecureMetadataOutputConfiguration perceptionThumbnailChannelMetadataObjectTypes]
+ -[BWSecureMetadataOutputConfiguration perceptionThumbnailChannelTargetFrameRate]
+ -[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionDeviceTypes:]
+ -[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionEnabled:]
+ -[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionTargetFrameRate:]
+ -[BWSecureMetadataOutputConfiguration setLightSourceEstimationAmbientLuminance:]
+ -[BWSecureMetadataOutputConfiguration setLightSourceEstimationEnabled:]
+ -[BWSecureMetadataOutputConfiguration setLightSourceEstimationTargetFrameRate:]
+ -[BWSecureMetadataOutputConfiguration setPerceptionTestModeEnabled:]
+ -[BWSecureMetadataOutputConfiguration setPerceptionThumbnailChannelMetadataObjectTypes:]
+ -[BWSecureMetadataOutputConfiguration setPerceptionThumbnailChannelTargetFrameRate:]
+ -[FigCaptureCameraSourcePipeline setDeviceProximityDetectionDeviceTypes:]
+ -[FigCaptureCameraSourcePipeline setDeviceProximityDetectionTargetFrameRate:]
+ -[FigCaptureCameraSourcePipeline setLightSourceEstimationAmbientLuminance:]
+ -[FigCaptureCameraSourcePipeline setLightSourceEstimationTargetFrameRate:]
+ -[FigCaptureDisplayLayout isRushmoreVisible]
+ -[FigCaptureDisplayLayout setRushmoreVisible:]
+ -[FigMetadataObjectCaptureConnectionConfiguration deviceProximityDetectionDeviceTypes]
+ -[FigMetadataObjectCaptureConnectionConfiguration deviceProximityDetectionTargetFrameRate]
+ -[FigMetadataObjectCaptureConnectionConfiguration lightSourceEstimationAmbientLuminance]
+ -[FigMetadataObjectCaptureConnectionConfiguration lightSourceEstimationTargetFrameRate]
+ -[FigMetadataObjectCaptureConnectionConfiguration metadataIdentifiersForPerceptionThumbnailChannel]
+ -[FigMetadataObjectCaptureConnectionConfiguration perceptionTestModeEnabled]
+ -[FigMetadataObjectCaptureConnectionConfiguration setDeviceProximityDetectionDeviceTypes:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setDeviceProximityDetectionTargetFrameRate:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setLightSourceEstimationAmbientLuminance:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setLightSourceEstimationTargetFrameRate:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setMetadataIdentifiersForPerceptionThumbnailChannel:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setPerceptionTestModeEnabled:]
+ BWCreateSampleBufferWithDeviceProximityDetectionDictionary
+ BWCreateSampleBufferWithLightSourceEstimationDictionary
+ GCC_except_table434
+ GCC_except_table480
+ GCC_except_table530
+ GCC_except_table535
+ GCC_except_table540
+ GCC_except_table542
+ GCC_except_table544
+ OBJC_IVAR_$_BWMultiStreamCameraSourceNode._deviceProximityDetectionOutput
+ OBJC_IVAR_$_BWMultiStreamCameraSourceNode._lightSourceEstimationOutput
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._deviceProximityDetectionDeviceTypes
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._deviceProximityDetectionEnabled
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._deviceProximityDetectionTargetFrameRate
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._lightSourceEstimationAmbientLuminance
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._lightSourceEstimationEnabled
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._lightSourceEstimationTargetFrameRate
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._perceptionTestModeEnabled
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._perceptionThumbnailChannelMetadataObjectTypes
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._perceptionThumbnailChannelTargetFrameRate
+ OBJC_IVAR_$_FigCaptureDisplayLayout._rushmoreVisible
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._deviceProximityDetectionDeviceTypes
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._deviceProximityDetectionTargetFrameRate
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._lightSourceEstimationAmbientLuminance
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._lightSourceEstimationTargetFrameRate
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._metadataIdentifiersForPerceptionThumbnailChannel
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._perceptionTestModeEnabled
+ _BWCreateSampleBufferWithDeviceProximityDetectionDictionary
+ _BWCreateSampleBufferWithLightSourceEstimationDictionary
+ _FigCaptureClientApplicationIdentifierPerceptiond
+ _FigCaptureClientApplicationIdentifierRushmore
+ _FigCaptureMetadataObjectConfigurationRequiresDeviceProximityDetection
+ _FigCaptureMetadataObjectConfigurationRequiresLightSourceEstimation
+ _kFigCaptureSampleBufferAttachmentKey_DeviceProximityDetection
+ _kFigCaptureSampleBufferAttachmentKey_LightSourceEstimation
+ _kFigCaptureSourceAttributeKey_SupportedMetadataObjectTypesForPerceptionThumbnailChannel
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureDeviceProximityDetectionConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureDeviceProximityDetectionEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureLightSourceEstimationConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureLightSourceEstimationEnabled
+ _kFigCaptureStreamMetadataOutputKey_SecureDetectedProximityDevices
+ _kFigCaptureStreamMetadataOutputKey_SecureLightSourceEstimation
+ _kFigCaptureStreamSecureDeviceProximityDetectionConfigurationKey_DeviceTypes
+ _kFigCaptureStreamSecureDeviceProximityDetectionConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamSecureLightSourceEstimationConfigurationKey_AmbientLuminance
+ _kFigCaptureStreamSecureLightSourceEstimationConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionTestModeEnabled
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionThumbnailChannelMetadataObjectTypes
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionThumbnailChannelTargetFrameRate
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_TargetFrameRate
+ _kFigMetadataIdentifier_QuickTimeMetadataDeviceProximityDetection
+ _kFigMetadataIdentifier_QuickTimeMetadataLightSourceEstimation
+ _multiStreamCameraSourceNode_secureDeviceProximityDetectionServiceQueueCallback
+ _multiStreamCameraSourceNode_secureLightSourceEstimationServiceQueueCallback
+ _objc_msgSend$deviceProximityDetectionDeviceTypes
+ _objc_msgSend$deviceProximityDetectionEnabled
+ _objc_msgSend$deviceProximityDetectionTargetFrameRate
+ _objc_msgSend$isRushmoreVisible
+ _objc_msgSend$lightSourceEstimationAmbientLuminance
+ _objc_msgSend$lightSourceEstimationEnabled
+ _objc_msgSend$lightSourceEstimationTargetFrameRate
+ _objc_msgSend$metadataIdentifiersForPerceptionThumbnailChannel
+ _objc_msgSend$perceptionTestModeEnabled
+ _objc_msgSend$perceptionThumbnailChannelMetadataObjectTypes
+ _objc_msgSend$perceptionThumbnailChannelTargetFrameRate
+ _objc_msgSend$setDeviceProximityDetectionDeviceTypes:
+ _objc_msgSend$setDeviceProximityDetectionEnabled:
+ _objc_msgSend$setDeviceProximityDetectionTargetFrameRate:
+ _objc_msgSend$setLightSourceEstimationAmbientLuminance:
+ _objc_msgSend$setLightSourceEstimationEnabled:
+ _objc_msgSend$setLightSourceEstimationTargetFrameRate:
+ _objc_msgSend$setMetadataIdentifiersForPerceptionThumbnailChannel:
+ _objc_msgSend$setPerceptionTestModeEnabled:
+ _objc_msgSend$setPerceptionThumbnailChannelMetadataObjectTypes:
+ _objc_msgSend$setPerceptionThumbnailChannelTargetFrameRate:
+ _objc_msgSend$setRushmoreVisible:
- GCC_except_table428
- GCC_except_table474
- GCC_except_table523
- GCC_except_table524
- GCC_except_table534
- GCC_except_table536
- GCC_except_table538
- _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_TargetFrameRate
CStrings:
+ "(New Bugs)"
+ ", deviceProximityDetection:{deviceTypes: %@"
+ ", lightSourceEstimation:{ambientLuminance:%d"
+ ", metadataIdentifiersForPerception:%lu, testMode:%d"
+ ", targetFrameRate:%.2f}"
+ "1706882"
+ "AVMetadataObjectTypeDeviceProximityDetection"
+ "AVMetadataObjectTypeLightSourceEstimation"
+ "DeviceProximityDetection"
+ "H19"
+ "H19 Camera"
+ "J804"
+ "J833"
+ "J834"
+ "LightSourceEstimation"
+ "SupportedMetadataObjectTypesForPerceptionThumbnailChannel"
+ "T1251"
+ "T@\"NSArray\",C,N,V_deviceProximityDetectionDeviceTypes"
+ "T@\"NSArray\",C,N,V_metadataIdentifiersForPerceptionThumbnailChannel"
+ "T@\"NSSet\",C,N,V_deviceProximityDetectionDeviceTypes"
+ "T@\"NSSet\",C,N,V_perceptionThumbnailChannelMetadataObjectTypes"
+ "TB,N,GisRushmoreVisible,V_rushmoreVisible"
+ "TB,N,V_deviceProximityDetectionEnabled"
+ "TB,N,V_lightSourceEstimationEnabled"
+ "TB,N,V_perceptionTestModeEnabled"
+ "TI,N,V_lightSourceEstimationAmbientLuminance"
+ "Tf,N,V_deviceProximityDetectionTargetFrameRate"
+ "Tf,N,V_lightSourceEstimationTargetFrameRate"
+ "_deviceProximityDetectionDeviceTypes"
+ "_deviceProximityDetectionEnabled"
+ "_deviceProximityDetectionOutput"
+ "_deviceProximityDetectionTargetFrameRate"
+ "_lightSourceEstimationAmbientLuminance"
+ "_lightSourceEstimationEnabled"
+ "_lightSourceEstimationOutput"
+ "_lightSourceEstimationTargetFrameRate"
+ "_metadataIdentifiersForPerceptionThumbnailChannel"
+ "_perceptionTestModeEnabled"
+ "_perceptionThumbnailChannelMetadataObjectTypes"
+ "_perceptionThumbnailChannelTargetFrameRate"
+ "_rushmoreVisible"
+ "com.apple.ClockFacePosters.DimensionalAnalogPosterExtension"
+ "com.apple.Motif"
+ "com.apple.MotifTools"
+ "com.apple.Rushmore"
+ "com.apple.fatool"
+ "com.apple.pebblefusiond"
+ "com.apple.peopleawarenessd"
+ "com.apple.perceptiond"
+ "deviceProximityDetection"
+ "deviceProximityDetectionDeviceTypes"
+ "deviceProximityDetectionEnabled"
+ "deviceProximityDetectionSupported"
+ "deviceProximityDetectionTargetFrameRate"
+ "isRushmoreVisible"
+ "lightSourceEstimation"
+ "lightSourceEstimationAmbientLuminance"
+ "lightSourceEstimationEnabled"
+ "lightSourceEstimationTargetFrameRate"
+ "metadataIdentifiersForPerceptionThumbnailChannel"
+ "perceptionTestModeEnabled"
+ "perceptionThumbnailChannelMetadataObjectTypes"
+ "perceptionThumbnailChannelSupported"
+ "perceptionThumbnailChannelTargetFrameRate"
+ "rushmore: 1"
+ "rushmoreVisible"
+ "setDeviceProximityDetectionDeviceTypes:"
+ "setDeviceProximityDetectionEnabled:"
+ "setDeviceProximityDetectionTargetFrameRate:"
+ "setLightSourceEstimationAmbientLuminance:"
+ "setLightSourceEstimationEnabled:"
+ "setLightSourceEstimationTargetFrameRate:"
+ "setMetadataIdentifiersForPerceptionThumbnailChannel:"
+ "setPerceptionTestModeEnabled:"
+ "setPerceptionThumbnailChannelMetadataObjectTypes:"
+ "setPerceptionThumbnailChannelTargetFrameRate:"
+ "setRushmoreVisible:"
```
