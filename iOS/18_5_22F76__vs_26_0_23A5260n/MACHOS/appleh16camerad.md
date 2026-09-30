## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-3.607.0.0.0
-  __TEXT.__text: 0x790ec
-  __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__objc_stubs: 0x1360
+4.12.4.0.0
+  __TEXT.__text: 0x80cd0
+  __TEXT.__auth_stubs: 0x1e40
+  __TEXT.__objc_stubs: 0x1420
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__gcc_except_tab: 0x21ec
-  __TEXT.__const: 0x2d60
-  __TEXT.__cstring: 0x842f
+  __TEXT.__gcc_except_tab: 0x2230
+  __TEXT.__const: 0x2d90
+  __TEXT.__cstring: 0x88fc
   __TEXT.__objc_classname: 0x89
-  __TEXT.__oslogstring: 0x5310
-  __TEXT.__objc_methname: 0x14ef
-  __TEXT.__objc_methtype: 0x105f
-  __TEXT.__unwind_info: 0x1440
-  __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0xf10
-  __DATA_CONST.__got: 0xad0
-  __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x9af0
-  __DATA_CONST.__cfstring: 0x3200
+  __TEXT.__oslogstring: 0x56ea
+  __TEXT.__objc_methname: 0x1567
+  __TEXT.__objc_methtype: 0x10b3
+  __TEXT.__unwind_info: 0x14c8
+  __TEXT.__eh_frame: 0xa0
+  __DATA_CONST.__auth_got: 0xf30
+  __DATA_CONST.__got: 0xb28
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__const: 0xa340
+  __DATA_CONST.__cfstring: 0x3280
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x5a8
-  __DATA.__objc_selrefs: 0x5f0
+  __DATA.__objc_selrefs: 0x620
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x331d60
+  __DATA.__data: 0x35cd78
   __DATA.__bss: 0x201
   __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9BA60A18-19AD-3691-BEDC-1E91028701AE
-  Functions: 1508
-  Symbols:   850
-  CStrings:  2319
+  UUID: 114C08F6-CDDC-3A84-9B9B-573AA6215AB2
+  Functions: 1614
+  Symbols:   865
+  CStrings:  2394
 
Symbols:
+ _OBJC_CLASS_$_CMDeviceImpactManager
+ _atan2f
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_time
+ _kFigCaptureStreamMetadata_AutoFocusConvergenceRequiresHigherFPSForPortType
+ _kFigCaptureStreamMetadata_ColorCorrectionMatrixDesaturationStrength
+ _kFigCaptureStreamMetadata_NominalColorCorrectionMatrix
+ _kFigCaptureStreamMetadata_PostDemosaicGain
+ _kFigCaptureStreamMetadata_PreDemosaicGain
+ _kFigCaptureStreamMetadata_PurpleHazeFlareIntensity
+ _kFigCaptureStreamMetadata_PurpleHazeMitigationEnabled
+ _kFigCaptureStreamMetadata_SmudgeDetectionConfidence
+ _kFigCaptureStreamMetadata_SynchronizedStreamsCameraControlsStatisticsPrimaryPortType
+ _kFigCaptureStreamMetadata_TemporalHomographyMatrix
+ _tanhf
- __Znwm
CStrings:
+ "%s - Buffer size does not match expected value (expected %zu, recv %lld)\n"
+ "%s - Device Impact Callback: impactType=%u date=%lld simulated=%d peakAccel=%f\n"
+ "%s - Device impact manager does not support querying for device impacts\n"
+ "%s - Device impact manager is NULL\n"
+ "%s - Device impact manager is unavailable, unable to query device impacts\n"
+ "%s - Failed to send device impacts samples, res=0x%08X\n"
+ "%s - H16ISPDevice is NULL\n"
+ "%s - LSCComputeSNFVerticalGains: null ptr! pRadialGainAsymScaleSet.\n"
+ "%s - Timeout: failed to query device impacts, releasing impact manager\n"
+ "%s - bypassDeviceImpactManagerInitialization!\n"
+ "/usr/local/share/firmware/isp/0225_01XX.dat"
+ "/usr/local/share/firmware/isp/1925_03XX.dat"
+ "4.12.4"
+ "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPDeviceImpactManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
+ "AWBComputedSecondBGain_Private"
+ "AWBComputedSecondGGain_Private"
+ "AWBComputedSecondRGain_Private"
+ "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPDeviceImpactManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
+ "CFLD:FLD #%07d  FLD::Process() ROI xywh:(%d %d)(%d %d) AfeDmaSize=%d tuning=%d\n"
+ "CFLD:FLD: Neon Mode\n"
+ "CFLD:FLD: Scalar Mode\n"
+ "CFLD:incompatible context version (expected %d, got %d)\n"
+ "ComputeBinnedXtalk"
+ "ComputeBinnedXtalkNeon"
+ "Could not set CIL Brightness to %u\n\n"
+ "DisableDropDetection"
+ "FLD.cpp"
+ "FLDProcessWrapper"
+ "Failed to report the ISP temperature statistics to analyticsd: %08X\n\n"
+ "GICComputeFromNVMApple"
+ "GetDeviceImpacts"
+ "GetDeviceImpacts_block_invoke"
+ "LSCComputeSNFVerticalGains"
+ "LSC_GET_BASE_U32_PT(chInfo[ch]) % (chInfo[ch]->gridCountX * chInfo[ch]->gridCountY) == 0"
+ "NTC_temperature_average"
+ "NTC_temperature_delta"
+ "NTC_temperature_max"
+ "NTC_temperature_min"
+ "NTC_temperature_range"
+ "NTC_temperature_start"
+ "NTC_temperature_stop"
+ "RGB-IR: %s: Invalid input: rows: %u, cols: %u.\n"
+ "SendDeviceImpacts"
+ "ShiftMapPostProcess"
+ "Timeout: failed to query device impacts\n"
+ "ZFProcessX1Wrapper"
+ "ZFProcessX2Wrapper"
+ "ZFRPC.cpp"
+ "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPDeviceImpactManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
+ "chInfo[ch]->gridCountX == chInfo[0]->gridCountX"
+ "chInfo[ch]->gridCountY == chInfo[0]->gridCountY"
+ "com.apple.applecamerad.CameraTemperatureVariation"
+ "defocusTh2 >= defocusTh1"
+ "h <= NROWSMAX"
+ "iCCl"
+ "imageSensor_temperature_average"
+ "imageSensor_temperature_delta"
+ "imageSensor_temperature_max"
+ "imageSensor_temperature_min"
+ "imageSensor_temperature_range"
+ "imageSensor_temperature_start"
+ "imageSensor_temperature_stop"
+ "impactType"
+ "isDeviceImpactAvailable"
+ "isSimulated"
+ "kGICMaxPerModuleX >= numXGIC"
+ "kGICMaxPerModuleY >= numYGIC"
+ "pAfe != nullptr"
+ "peakAcceleration"
+ "queryDeviceImpactsWithCompletion:"
+ "test"
+ "timeIntervalSince1970"
+ "v16@?0@\"NSArray\"8"
+ "w <= NCOLSMAX"
+ "~H16ISPDeviceImpactManager"
- "3.607"
- "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
- "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
- "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"

```
