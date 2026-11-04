## ISP.mediacapture

> `/System/Library/MediaCapture/ISP.mediacapture`

```diff

-20.111.0.0.0
-  __TEXT.__text: 0x1f1094
+20.203.1.0.0
+  __TEXT.__text: 0x1f0d4c
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x5e40
-  __TEXT.__const: 0x2903d
-  __TEXT.__oslogstring: 0x2409e
-  __TEXT.__cstring: 0x1aeeb
+  __TEXT.__gcc_except_tab: 0x5dec
+  __TEXT.__const: 0x2905d
+  __TEXT.__oslogstring: 0x23f09
+  __TEXT.__cstring: 0x1aec0
   __TEXT.__unwind_info: 0x6910
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa2c8
+  __DATA_CONST.__const: 0xa2e8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0x8e0
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x3c20
-  __AUTH_CONST.__const: 0x2670
-  __AUTH_CONST.__cfstring: 0xace0
+  __DATA_CONST.__got: 0x3c30
+  __AUTH_CONST.__const: 0x2690
+  __AUTH_CONST.__cfstring: 0xad00
   __AUTH_CONST.__objc_const: 0x8a0
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x18d0
+  __AUTH_CONST.__auth_got: 0x18d8
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x5b0708
+  __DATA.__data: 0x5b0910
   __DATA.__common: 0x5e50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
-  - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6180
-  Symbols:   7888
-  CStrings:  7175
+  Functions: 6179
+  Symbols:   7889
+  CStrings:  7171
 
Symbols:
+ GCC_except_table558
+ GCC_except_table595
+ GCC_except_table600
+ GCC_except_table617
+ GCC_except_table620
+ GCC_except_table626
+ GCC_except_table668
+ GCC_except_table670
+ GCC_except_table688
+ GCC_except_table694
+ GCC_except_table786
+ GCC_except_table791
+ GCC_except_table823
+ GCC_except_table826
+ GCC_except_table830
+ GCC_except_table832
+ GCC_except_table834
+ GCC_except_table839
+ GCC_except_table841
+ GCC_except_table844
+ GCC_except_table848
+ GCC_except_table851
+ GCC_except_table854
+ GCC_except_table859
+ GCC_except_table863
+ GCC_except_table882
+ GCC_except_table886
+ GCC_except_table911
+ GCC_except_table926
+ __ZL19IsSecureANDKEnabledP16ISPCaptureDeviceP16ISPCaptureStream
+ __ZL25SetActiveClientAuditTokenPKvP16ISPCaptureStreamP15ISPCaptureGroupP16ISPCaptureDevice
+ __ZN20GMCProcessorInternal28updatePCECalibWithGMCResultsERK12_GMC_ResultsRK18GMCInnerStatisticsRK26sCIspCmdChPearlCalibrationRS6_P19ISPAnalyticsGMCInfo15ePearlHWVersion
+ __ZN3ISP26ISPFrameReceiverBufferPool12activatePoolEv
+ __ZN3ISP9ISPDevice25SetActiveClientAuditTokenEPK13audit_token_t
+ __ZZL19IsSecureANDKEnabledP16ISPCaptureDeviceP16ISPCaptureStreamE19enabledWithDefaults
+ __ZZL19IsSecureANDKEnabledP16ISPCaptureDeviceP16ISPCaptureStreamE9onceToken
+ __ZZL25SetActiveClientAuditTokenPKvP16ISPCaptureStreamP15ISPCaptureGroupP16ISPCaptureDeviceE18kInvalidAuditToken
+ ____ZL19IsSecureANDKEnabledP16ISPCaptureDeviceP16ISPCaptureStream_block_invoke
+ _audit_token_to_pid
+ _kFigCaptureDeviceProperty_ActiveClientAuditToken
+ _kFigCaptureStreamSecureFaceIDConfigurationKey_MatchOperationTrigger
+ _kFigCaptureStreamSecureFaceIDConfigurationKey_MatchSequenceType
+ _kill
+ _sandbox_check_by_audit_token
- GCC_except_table38
- GCC_except_table560
- GCC_except_table596
- GCC_except_table601
- GCC_except_table618
- GCC_except_table621
- GCC_except_table627
- GCC_except_table667
- GCC_except_table669
- GCC_except_table691
- GCC_except_table693
- GCC_except_table784
- GCC_except_table790
- GCC_except_table822
- GCC_except_table825
- GCC_except_table829
- GCC_except_table831
- GCC_except_table833
- GCC_except_table836
- GCC_except_table840
- GCC_except_table843
- GCC_except_table847
- GCC_except_table849
- GCC_except_table853
- GCC_except_table858
- GCC_except_table862
- GCC_except_table881
- GCC_except_table885
- GCC_except_table910
- GCC_except_table925
- _CVPixelBufferPoolScanIOSurfaces
- _SavageCamInterfaceCheckPersonalizationStatus
- __ZL17SetClientIsActivePKvP16ISPCaptureStreamP15ISPCaptureGroupP16ISPCaptureDevice
- __ZL21ISPCaptureGroupCreatePK13__CFAllocatorP22OpaqueFigCaptureDevicePN3ISP9ISPDeviceEPK9__CFArrayPP40OpaqueFigCaptureSynchronizedStreamsGroup
- __ZN20GMCProcessorInternal28updatePCECalibWithGMCResultsERK12_GMC_ResultsRK18GMCInnerStatisticsbRK26sCIspCmdChPearlCalibrationRS6_P19ISPAnalyticsGMCInfo15ePearlHWVersion
- __ZN3ISP26ISPFrameReceiverBufferPool12activatePoolEb
- __ZN3ISP26ISPFrameReceiverBufferPool19PreMapClientSurfaceEj
- __ZN3ISP9ISPDevice21ISP_SetDriverPropertyEjj
- __ZN3ISP9ISPDevice23ISP_PreMapClientSurfaceEj
- __ZN3ISP9ISPDevice33ISP_ReleasePreMappedClientSurfaceEj
- __ZN3ISPL41MyCVPixelBufferPoolScanIOSurfacesCallbackEP11__IOSurfacePNS_26ISPFrameReceiverBufferPoolE
- __ZNK14GMCInitializer9isFrontAFEv
- _kFigCaptureDeviceProperty_ClientIsActive
CStrings:
+ "%s - ActiveClient audit_token cleared\n"
+ "%s - ActiveClient audit_token set: 0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x\n"
+ "%s - GMC controller failed, status: %d\n"
+ "%s - GMC controller succeeded, running ISF...\n"
+ "%s - HueMap output does not support enable after stream has started without it\n"
+ "%s - SetActiveClientAuditToken: unexpected CFData length %ld (expected %zu)\n"
+ "%s - enabledWithDefaults %{bool}d\n"
+ "%s - procName:%s / audit_token:0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x\n"
+ "ISPCaptureDevice: ActiveClientAuditToken is INVALID_AUDIT_TOKEN_VALUE, clearing\n"
+ "ISPCaptureDevice: set kFigCaptureDeviceProperty_ActiveClientAuditToken\n"
+ "IsSecureANDKEnabled_block_invoke"
+ "SetActiveClientAuditToken"
+ "isp.EnableAndk"
- "%s - Front camera supports auto-focus: %d\n"
- "%s - GMC controller succeeded and front camera supports auto-focus, running ISF...\n"
- "%s - HueMap output does not support enable/disable after stream has started\n"
- "%s - ISP_PreMapClientSurface failed: 0x%08X\n"
- "%s - SavageCamInterfaceCheckPersonalizationStatus err 0x%08X\n"
- "%s - Skipping unpersonalized secure camera channel: %d\n"
- "%s - Sync group %d has no HW master stream available - not advertising group\n"
- "%s - Sync group %d has only %d stream - not advertising as a sync group\n"
- "%s - chan %d - cameraModuleDescription 0x%08X malformed status entry, stateValue %p typeID %lu (expected %lu), failing closed\n"
- "%s - chan %d - could not allocate lookup key, failing closed\n"
- "%s - chan %d - no platform info/statuses dict, info not available, failing closed\n"
- "%s - chan %d - personalization status unavailable (0x%08X), failing closed\n"
- "%s - procNameForCIL:%s / audit_token:0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x\n"
- "ISPCaptureDevice: set kFigCaptureDeviceProperty_ClientIsActive, isClientActive=%d, res=0x%08X\n\n"
- "ISPFrameReceiverBufferPool::%s - ISP_PreMapClientSurface failed: 0x%08X\n"
- "IsSensorNotPersonalized"
- "PreMapClientSurface"
```
