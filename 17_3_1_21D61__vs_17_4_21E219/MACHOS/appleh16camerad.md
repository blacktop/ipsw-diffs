## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-1.300.0.0.0
-  __TEXT.__text: 0x6a518
-  __TEXT.__auth_stubs: 0x1b80
-  __TEXT.__objc_stubs: 0x1100
+2.403.0.0.0
+  __TEXT.__text: 0x6f308
+  __TEXT.__auth_stubs: 0x1ce0
+  __TEXT.__objc_stubs: 0x13a0
   __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__const: 0x2e70
-  __TEXT.__gcc_except_tab: 0x1da0
-  __TEXT.__cstring: 0x7b77
-  __TEXT.__oslogstring: 0x3f3d
+  __TEXT.__gcc_except_tab: 0x1e1c
+  __TEXT.__const: 0x2b60
+  __TEXT.__cstring: 0x808c
+  __TEXT.__oslogstring: 0x46ed
   __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x11e5
-  __TEXT.__objc_methtype: 0xf00
-  __TEXT.__unwind_info: 0x129c
+  __TEXT.__objc_methname: 0x1587
+  __TEXT.__objc_methtype: 0xf39
+  __TEXT.__unwind_info: 0x1350
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xdd0
-  __DATA_CONST.__got: 0x9a0
+  __DATA_CONST.__auth_got: 0xe80
+  __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0xe180
-  __DATA_CONST.__cfstring: 0x2ba0
+  __DATA_CONST.__const: 0x4cf0
+  __DATA_CONST.__cfstring: 0x2f20
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x808
-  __DATA.__objc_selrefs: 0x4c0
-  __DATA.__objc_classrefs: 0x158
-  __DATA.__objc_superrefs: 0x18
+  __DATA.__objc_selrefs: 0x568
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x109be0
-  __DATA.__bss: 0x178
+  __DATA.__data: 0x1c1be0
+  __DATA.__bss: 0x180
   __DATA.__common: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth
   - /System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit

   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
   - /usr/lib/libFDR.dylib
   - /usr/lib/libIOAccessoryManager.dylib

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 40E63567-809A-3C5E-A867-9C7672C9F29E
-  Functions: 1564
-  Symbols:   800
-  CStrings:  2020
+  UUID: BDC4531C-4D33-3AF4-8223-A732A7EBDF51
+  Functions: 1592
+  Symbols:   832
+  CStrings:  2162
 
Symbols:
+ _AMFDRCreateInstanceString
+ _AMFDRSealingMapCopyLocalMinimalManifestForInstance
+ _CMTimeGetSeconds
+ _CMTimeMakeFromDictionary
+ _CVPixelBufferGetDataSize
+ _IOHIDEventGetFloatValue
+ _IOHIDEventGetType
+ _IOHIDEventSystemClientActivate
+ _IOHIDEventSystemClientCancel
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDEventSystemClientRegisterEventCallback
+ _IOHIDEventSystemClientSetCancelHandler
+ _IOHIDEventSystemClientSetDispatchQueue
+ _IOHIDEventSystemClientSetMatchingMultiple
+ _IOHIDEventSystemClientUnregisterEventCallback
+ _IOHIDEventSystemClientUnscheduleFromDispatchQueue
+ _IOHIDServiceClientCopyProperty
+ _OBJC_CLASS_$_ADPearlColorInFieldCalibrationExecutor
+ _OBJC_CLASS_$_ADPearlColorInFieldCalibrationExecutorParameters
+ _OBJC_CLASS_$_ADPearlColorInFieldCalibrationPipeline
+ _OBJC_CLASS_$_ADPearlColorInFieldCalibrationResult
+ _OBJC_CLASS_$_STActivityAttribution
+ _OBJC_CLASS_$_STMediaStatusDomainCameraCaptureAttribution
+ _OBJC_CLASS_$_STMediaStatusDomainCameraDescriptor
+ _OBJC_CLASS_$_STMediaStatusDomainPublisher
+ _bfpn_create_correction_model_from_fdr
+ _kFigCaptureStreamMetadata_AFStatusExtended
+ _matrix_identity_float3x3
+ _objc_retain_x9
+ _os_log_create
+ _proc_pidpath
+ _remove
+ _task_info
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "%@-%@"
+ "%s - Parsing ISPUnitInfo.plist\n"
+ "%s : Status = %08x; HPR - %s \n"
+ "%s : noHPR boot-arg set \n"
+ "%s No module or Unauthorized swap (cmpmStatus = 0x%x) or No CmPM data (perhaps cuz the device does not support CmPM) [error]: %s \n"
+ "%s [error]: %s \n"
+ "%s: AudioUnit Input Callback: accumulatedSize=%zd inputBufferByteSize=%d\n"
+ "%s: AudioUnitRender - status 0x%08x \n"
+ "%s: Can't create /var/mobile/Library/ISP \n"
+ "%s: Can't create /var/mobile/Library/ISP/CalData \n"
+ "%s: Could not create HID event system client\n"
+ "%s: Could not create a matching dictionary\n"
+ "%s: Could not create device matching array\n"
+ "%s: Could not create device matching dictionary\n"
+ "%s: Could not create device usage references\n"
+ "%s: Could not create primary usage references\n"
+ "%s: Could not open %s file"
+ "%s: IOHID Service Client Reference is NULL\n"
+ "%s: OK"
+ "%s: Writing GMC ISF file"
+ "%s: performRender - invalid context \n"
+ "%s: result = %d, outputPixelBufferRef = %lu\n"
+ "%s: type=0x%X, isOverride=%d, size=%u, isEarlyBoot=%d, status=%08x\n"
+ "/usr/local/share/firmware/isp/2224_01XX.dat"
+ "/usr/local/share/firmware/isp/3624_01XX.dat"
+ "/usr/local/share/firmware/isp/3624_02XX.dat"
+ "/usr/local/share/firmware/isp/4524_01XX.dat"
+ "/usr/local/share/firmware/isp/7324_01XX.dat"
+ "/usr/local/share/firmware/isp/7524_01XX.dat"
+ "/usr/local/share/firmware/isp/CmPM-DPCd.DAT"
+ "/usr/local/share/firmware/isp/CmPM-DPCm.DAT"
+ "/usr/local/share/firmware/isp/CmPM-brcl.DAT"
+ "/usr/local/share/firmware/isp/CmPM-brgd.DAT"
+ "/usr/local/share/firmware/isp/CmPM-dcnu.DAT"
+ "/usr/local/share/firmware/isp/Savage/FrontIRHPR.DER"
+ "/var/mobile/Library/ISP/"
+ "/var/mobile/Library/ISP/CalData"
+ "/var/mobile/Library/ISP/CalData/DCNUMetadata_0"
+ "/var/mobile/Library/ISP/CalData/DCNUPixbuf_0"
+ "/var/mobile/Library/ISP/Pearl/rgbpInterSession.plist"
+ "2.403"
+ "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}i^{__CFDictionary}^{H16ISPMotionManager}^{H16ISPServicesRemote}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II}16I24^{H16ISPServicesRemote=@@^?^v*}28"
+ "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}i^{__CFDictionary}^{H16ISPMotionManager}^{H16ISPServicesRemote}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II}16"
+ "BackCameraSNUM"
+ "BackCameraSNUM/BackSuperWideCameraSNUM exists - load FDR CmPM calibration data\n"
+ "BackSuperWideCameraSNUM"
+ "CmPM"
+ "ColorGdcCoeffs"
+ "ColorPixelSizeMm"
+ "Couldn't combine frontIR chipIDStr and uidStr"
+ "Couldn't create SavageChipID string ref"
+ "Couldn't create SavageUID string ref"
+ "Couldn't read BackCameraSNUM and BackSuperWideCameraSNUM. Sensor is hosed/disconnected. Skip loading FDR CmPM calibration data\n"
+ "Couldn't read SavageChipID"
+ "Couldn't read SavageUID"
+ "DPCd"
+ "DPCm"
+ "DeviceUsage"
+ "DeviceUsagePage"
+ "Failed to lock pixel buffer"
+ "Found FrontIR override (has highest precedence) HPR file - camChannel = %d"
+ "GetProcNameAndAuditToken"
+ "GetUnitInfoPropertyDict"
+ "H16ISPPhotometerManager: Could not create the audio unit instance\n"
+ "H16ISPServicesAssistant: setProperty %d complete (res=0x%08X)\n"
+ "H16ISPServicesRemoteIORegPropertyDataKey"
+ "H16ISPServicesRemoteIORegPropertyNameKey"
+ "IgnoreUnitInfoPlist"
+ "InitializeHIDEventSystemClientForALS"
+ "LoadFDRDataFileCMPM"
+ "LoadFrontIRHPRFile"
+ "LoadHPR"
+ "Multiplier"
+ "MyIOHIDEventCallback"
+ "No HPR file for frontIR found"
+ "Offset"
+ "Pearl Calibration (MI) finalization: No changes to PCECalib"
+ "Pearl Calibration (MI) finalization: final rotation: (%lf, %f, %f)"
+ "Pearl Calibration (MI): Already running algorithm"
+ "Pearl Calibration (MI): color frame not valid for algorithm"
+ "Pearl Calibration (MI): pearl frame not valid for algorithm"
+ "PearlVersion"
+ "Pixel buffer has invalid size"
+ "Pixel format mismatch"
+ "Placement"
+ "PrimaryUsage"
+ "PrimaryUsagePage"
+ "RgbpDisableCalibUpdating"
+ "SavageChipID"
+ "SavageUID"
+ "T@\"NSString\",?,R,C"
+ "WARNING: IR DC Offset calculated from sysconfig is out of range, defaulting to a global value\n"
+ "WARNING: VIR DC Offset calculated from sysconfig is out of range, defaulting to a global value\n"
+ "[%s]: Unknown error from proc_pidpath"
+ "[%s]: Unknown error from task_info"
+ "[%s]: procNameForCIL:%s / audit_token:0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x/0x%08x"
+ "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}i^{__CFDictionary}^{H16ISPMotionManager}^{H16ISPServicesRemote}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II}"
+ "adjustForImageRotation:"
+ "brcl"
+ "brgd"
+ "cameraCalibration"
+ "com.apple.isp"
+ "createInterSessionDataWithFactoryPearlToColorTransform:currentPearlToColorTransform:"
+ "crop:"
+ "dcnu"
+ "dictionaryRepresentation"
+ "initForEngineType:andExecutorParameters:"
+ "initWithPixelSize:gdcModel:cameraToPlatformTransform:"
+ "inputCallbackForGrimaldi_iPad"
+ "invalidate"
+ "isColorFrameValid:withMetadata:"
+ "isPearlFrameValid:withMetadata:"
+ "pearlToColorExtrinsics"
+ "preprocessInputColorFrame:pearlDepth:pearlPoses:pceCameraCalibration:pearlCameraCalibrationTransform:colorCameraCalibration:timestamp:"
+ "preprocessInputColorFrame:pearlNormalizedDX:pearlPoses:disparityNormalizationMultiplier:disparityNormalizationOffset:pceCameraCalibration:pearlCameraCalibrationTransform:colorCameraCalibration:timestamp:"
+ "referenceDimensions"
+ "rgbjDynamicFrameRate"
+ "scale:"
+ "services"
+ "setCameraToPlatformTransform:"
+ "setColorCameraCalibration:"
+ "setPearlCameraCalibration:"
+ "setReportTelemetry:"
+ "setWmcamToMcamExtrinsics:"
+ "updateForFrameWithDimensions:metadataDictionary:"
+ "updatePCECalibWithISF_block_invoke"
- "/usr/local/share/firmware/isp/7523_01XX.dat"
- "/usr/local/share/firmware/isp/h13_isp_fw.bin"
- "/usr/local/share/firmware/isp/h14_isp_fw.bin"
- "1.300"
- "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=^^{BufferPoolConfigurationStruct}IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}}^?^v^{H16ISPDeviceController}i^{__CFDictionary}^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II}16I24^{H16ISPServicesRemote=@@^?^v*}28"
- "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=^^{BufferPoolConfigurationStruct}IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}}^?^v^{H16ISPDeviceController}i^{__CFDictionary}^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II}16"
- "Error: ISP_OverrideSensorClockFrequency returned an error: 0x%08X\n"
- "H10ISPServicesAssistant: setProperty %d complete (res=0x%08X)\n"
- "H16ISP: Cannot cache bufferPoolInfo[%u][%u], result = 0x%08x"
- "Parsing ISPUnitInfo.plist \n"
- "Successfully set camera %d clock divider over-ride: 0x%08X\n"
- "^{H16ISPDevice={H16ISPDeviceCachedConfigs=^^{BufferPoolConfigurationStruct}IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}}^?^v^{H16ISPDeviceController}i^{__CFDictionary}^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II}"

```
