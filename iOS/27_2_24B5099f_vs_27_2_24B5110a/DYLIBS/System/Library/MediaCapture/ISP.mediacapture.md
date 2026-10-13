## ISP.mediacapture

> `/System/Library/MediaCapture/ISP.mediacapture`

```diff

-20.106.4.0.0
-  __TEXT.__text: 0x1ee5a8
+20.109.0.0.0
+  __TEXT.__text: 0x1f1094
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x5dc8
-  __TEXT.__const: 0x28fad
-  __TEXT.__oslogstring: 0x23982
-  __TEXT.__cstring: 0x1accd
-  __TEXT.__unwind_info: 0x6868
+  __TEXT.__gcc_except_tab: 0x5e40
+  __TEXT.__const: 0x2903d
+  __TEXT.__oslogstring: 0x2409e
+  __TEXT.__cstring: 0x1aeeb
+  __TEXT.__unwind_info: 0x6910
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa290
+  __DATA_CONST.__const: 0xa2c8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0x8e0
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x3bd8
-  __AUTH_CONST.__const: 0x2580
+  __DATA_CONST.__got: 0x3c20
+  __AUTH_CONST.__const: 0x2670
   __AUTH_CONST.__cfstring: 0xace0
   __AUTH_CONST.__objc_const: 0x8a0
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x18c8
+  __AUTH_CONST.__auth_got: 0x18d0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x5b06f8
+  __DATA.__data: 0x5b0708
   __DATA.__common: 0x5e50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6143
-  Symbols:   7851
-  CStrings:  7124
+  Functions: 6180
+  Symbols:   7888
+  CStrings:  7175
 
Symbols:
+ GCC_except_table596
+ GCC_except_table601
+ GCC_except_table618
+ GCC_except_table621
+ GCC_except_table628
+ GCC_except_table631
+ GCC_except_table638
+ GCC_except_table667
+ GCC_except_table669
+ GCC_except_table693
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table790
+ GCC_except_table825
+ GCC_except_table829
+ GCC_except_table831
+ GCC_except_table836
+ GCC_except_table838
+ GCC_except_table843
+ GCC_except_table849
+ GCC_except_table853
+ GCC_except_table858
+ GCC_except_table862
+ GCC_except_table881
+ GCC_except_table885
+ GCC_except_table910
+ GCC_except_table925
+ _SavageCamInterfaceCheckPersonalizationStatus
+ __ZL21ISPCaptureGroupCreatePK13__CFAllocatorP22OpaqueFigCaptureDevicePN3ISP9ISPDeviceEPK9__CFArrayPP40OpaqueFigCaptureSynchronizedStreamsGroup
+ __ZL25SecureAlgorithmSetEnabledPK14__CFDictionaryPK10__CFStringPb
+ __ZL34ExclaveSetRGBDeviceModelsParameterP16ISPCaptureDeviceP16ISPCaptureStream
+ __ZN3ISP29ISPGraphExclavePerceptionNode19onMessageProcessingEPNS_21ISPFilterGraphMessageE
+ __ZN3ISP29ISPGraphExclavePerceptionNodeC1EPNS_9ISPDeviceEjb
+ __ZN3ISP29ISPGraphExclavePerceptionNodeC2EPNS_9ISPDeviceEjb
+ __ZN3ISP29ISPGraphExclavePerceptionNodeD0Ev
+ __ZN3ISP29ISPGraphExclavePerceptionNodeD1Ev
+ __ZN3ISP43ISPGraphExclaveDeviceProximityDetectionNode19onMessageProcessingEPNS_21ISPFilterGraphMessageE
+ __ZN3ISP43ISPGraphExclaveDeviceProximityDetectionNode27runDeviceProximityDetectionEPNS_21ISPFilterGraphMessageEb
+ __ZN3ISP43ISPGraphExclaveDeviceProximityDetectionNodeC1EPNS_9ISPDeviceEj
+ __ZN3ISP43ISPGraphExclaveDeviceProximityDetectionNodeC2EPNS_9ISPDeviceEj
+ __ZN3ISP43ISPGraphExclaveDeviceProximityDetectionNodeD0Ev
+ __ZN3ISP43ISPGraphExclaveDeviceProximityDetectionNodeD1Ev
+ __ZN3ISPL28StringifyPerceptionObjectIDsEP48ISPExclaveCoreChRunKitPerceptionWithObjectIDRslt
+ __ZN3ISPL31StringifyPerceptionReturnStatusE22PerceptionReturnStatus
+ __ZN3ISPL50ObjectDetectionDictionarySetSentToPerceptionStatusEPK14__CFDictionaryP48ISPExclaveCoreChRunKitPerceptionWithObjectIDRslt
+ __ZNSt3__13setIiNS_4lessIiEENS_9allocatorIiEEE6insertB9fqe220106ERKi
+ __ZNSt3__16__treeIiNS_4lessIiEENS_9allocatorIiEEE14__tree_deleterclB9fqe220106EPNS_11__tree_nodeIiPvEE
+ __ZNSt3__16__treeIiNS_4lessIiEENS_9allocatorIiEEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSA_SA_
+ __ZNSt3__16__treeIiNS_4lessIiEENS_9allocatorIiEEE7destroyEPNS_11__tree_nodeIiPvEE
+ __ZTIN3ISP29ISPGraphExclavePerceptionNodeE
+ __ZTIN3ISP43ISPGraphExclaveDeviceProximityDetectionNodeE
+ __ZTSN3ISP29ISPGraphExclavePerceptionNodeE
+ __ZTSN3ISP43ISPGraphExclaveDeviceProximityDetectionNodeE
+ __ZTVN3ISP29ISPGraphExclavePerceptionNodeE
+ __ZTVN3ISP43ISPGraphExclaveDeviceProximityDetectionNodeE
+ _kFigCaptureStreamDetectedObjectKey_SentToPerceptionThumbnailChannel
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureDeviceProximityDetectionConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureDeviceProximityDetectionEnabled
+ _kFigCaptureStreamMetadataOutputKey_SecureDetectedProximityDevices
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_ConfidenceLevel
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_DeviceID
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_DeviceType
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_PoseMatrix
+ _kFigCaptureStreamSecureDetectedProximityDevicesKey_DevicesArray
+ _kFigCaptureStreamSecureDeviceProximityDetectionConfigurationKey_DeviceTypes
+ _kFigCaptureStreamSecureDeviceProximityDetectionConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionTestModeEnabled
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionThumbnailChannelMetadataObjectTypes
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionThumbnailChannelTargetFrameRate
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_TargetFrameRate
- GCC_except_table595
- GCC_except_table600
- GCC_except_table617
- GCC_except_table620
- GCC_except_table626
- GCC_except_table630
- GCC_except_table637
- GCC_except_table666
- GCC_except_table668
- GCC_except_table692
- GCC_except_table781
- GCC_except_table782
- GCC_except_table787
- GCC_except_table819
- GCC_except_table826
- GCC_except_table828
- GCC_except_table830
- GCC_except_table834
- GCC_except_table835
- GCC_except_table844
- GCC_except_table846
- GCC_except_table855
- GCC_except_table859
- GCC_except_table878
- GCC_except_table882
- GCC_except_table907
- GCC_except_table922
- _kFigCaptureStreamMetadataOutputConfigurationKey_SVDResultEnabled
- _kFigCaptureStreamMetadataOutputKey_SVDResult
- _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_TargetFrameRate
- _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_TestMode
- _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_ThumbnailStreamMetadataObjectTypes
- _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_ThumbnailStreamTargetFrameRate
CStrings:
+ "%s - Failed to set device models parameter ret=0x%08X\n"
+ "%s - SavageCamInterfaceCheckPersonalizationStatus err 0x%08X\n"
+ "%s - Skipping unpersonalized secure camera channel: %d\n"
+ "%s - Sync group %d has no HW master stream available - not advertising group\n"
+ "%s - Sync group %d has only %d stream - not advertising as a sync group\n"
+ "%s - chan %d - cameraModuleDescription 0x%08X malformed status entry, stateValue %p typeID %lu (expected %lu), failing closed\n"
+ "%s - chan %d - could not allocate lookup key, failing closed\n"
+ "%s - chan %d - no platform info/statuses dict, info not available, failing closed\n"
+ "%s - chan %d - personalization status unavailable (0x%08X), failing closed\n"
+ "%s - cropTypeCount=%u\n"
+ "%s - exceeded result array space... dropping objectID=%u\n"
+ "%s - failed to allocate detected devices array\n"
+ "%s - failed to configure perception err=%u\n"
+ "%s - failed to create dictionary for device=%d\n"
+ "%s - failed to extract device type at idx=%ld\n"
+ "%s - failed to set device models channel=%u err=%u\n"
+ "%s - failed to set device models parameter ret=0x%08x\n"
+ "%s - invalid device type at idx=%ld\n"
+ "%s - invalid device types value\n"
+ "%s - invalid number of device types: maximum=%u received=%ld\n"
+ "%s - invalid object dictionary keyIndex=%zu arrayIndex=%ld\n"
+ "%s - invalid objects array keyIndex=%zu\n"
+ "%s - invalid sensor channel=%u\n"
+ "%s - missing detected objects dictionary for reqid=0x%08x\n"
+ "%s - need to specify at least one device type\n"
+ "%s - no device types were configured\n"
+ "%s - objectIDs=( %s )\n"
+ "%s - perception failed to run err=%u reqid=0x%08x\n"
+ "%s - perception returned '%s' for reqid=0x%08x\n"
+ "ConfigureFrameworkPerceptionSettings"
+ "DPD"
+ "DeviceProximityDetectionResultCreateDictionaryRepresentation"
+ "ExclavePrepareDeviceModelsParameterCommand"
+ "ExclaveSetDeviceModelsParameter"
+ "ExclaveSetRGBDeviceModelsParameter"
+ "IsSensorNotPersonalized"
+ "ObjectDetectionDictionarySetSentToPerceptionStatus"
+ "SecureDeviceProximityDetectionSetConfiguration"
+ "SecureDeviceProximityDetectionSetDeviceTypes"
+ "TestModePopulateMockPerceptionResult"
+ "detections error"
+ "device proximity detection"
+ "failed to run device proximity detection reqid=0x%08x err=%u success=%{bool}d\n"
+ "frame skipped"
+ "perception"
+ "perception objectIDs=( %s )\n"
+ "queueing failed"
+ "runkit device proximity detection ch=%u publishResult=%{bool}d reqid=0x%08x\n"
+ "running perception ch=%u testMode=%{bool}d reqid=0x%08x\n"
+ "shared memory mapping issue"
+ "skipped by decimation"
+ "success"
- "thumbnail stream"
```
