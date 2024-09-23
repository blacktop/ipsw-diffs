## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-580.6.21.0.0
-  __TEXT.__text: 0x78bfb4
+580.11.21.1.0
+  __TEXT.__text: 0x790a08
   __TEXT.__auth_stubs: 0x4e80
-  __TEXT.__objc_methlist: 0x2a424
-  __TEXT.__const: 0x150568
-  __TEXT.__cstring: 0xbe263
-  __TEXT.__oslogstring: 0x101e80
-  __TEXT.__gcc_except_tab: 0x3d4c
-  __TEXT.__dlopen_cstrs: 0x67e
+  __TEXT.__objc_methlist: 0x2a60c
+  __TEXT.__const: 0x150598
+  __TEXT.__cstring: 0xbe73d
+  __TEXT.__oslogstring: 0x102a5b
+  __TEXT.__gcc_except_tab: 0x3d74
+  __TEXT.__dlopen_cstrs: 0x6d8
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xc318
-  __TEXT.__objc_classname: 0x74f8
-  __TEXT.__objc_methname: 0x9174c
+  __TEXT.__unwind_info: 0xc368
+  __TEXT.__objc_classname: 0x7512
+  __TEXT.__objc_methname: 0x91f0c
   __TEXT.__objc_methtype: 0x1395d
-  __TEXT.__objc_stubs: 0x3fd20
-  __DATA_CONST.__got: 0x5ea8
-  __DATA_CONST.__const: 0xa5a8
-  __DATA_CONST.__objc_classlist: 0x1890
+  __TEXT.__objc_stubs: 0x3fee0
+  __DATA_CONST.__got: 0x5ed8
+  __DATA_CONST.__const: 0xa5f0
+  __DATA_CONST.__objc_classlist: 0x1898
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12168
+  __DATA_CONST.__objc_selrefs: 0x12218
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x1710
+  __DATA_CONST.__objc_superrefs: 0x1718
   __DATA_CONST.__objc_arraydata: 0x3580
   __AUTH_CONST.__auth_got: 0x2750
   __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x3d30
-  __AUTH_CONST.__cfstring: 0x41300
-  __AUTH_CONST.__objc_const: 0x860e0
-  __AUTH_CONST.__objc_intobj: 0x4e48
+  __AUTH_CONST.__const: 0x3dd0
+  __AUTH_CONST.__cfstring: 0x41540
+  __AUTH_CONST.__objc_const: 0x86618
+  __AUTH_CONST.__objc_intobj: 0x4e60
   __AUTH_CONST.__objc_arrayobj: 0x2520
-  __AUTH_CONST.__objc_doubleobj: 0x9b0
-  __AUTH_CONST.__objc_floatobj: 0x200
+  __AUTH_CONST.__objc_doubleobj: 0x9c0
+  __AUTH_CONST.__objc_floatobj: 0x230
   __AUTH_CONST.__objc_dictobj: 0x1798
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x941c
+  __DATA.__objc_ivar: 0x9490
   __DATA.__data: 0x4878
   __DATA.__crash_info: 0x40
-  __DATA.__common: 0x1050
-  __DATA.__bss: 0x19a0
-  __DATA_DIRTY.__objc_data: 0xefb0
+  __DATA.__common: 0x1070
+  __DATA.__bss: 0x19f0
+  __DATA_DIRTY.__objc_data: 0xf000
   __DATA_DIRTY.__data: 0xfb8
   __DATA_DIRTY.__common: 0x1000
-  __DATA_DIRTY.__bss: 0xa50
+  __DATA_DIRTY.__bss: 0xa28
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 20776
-  Symbols:   26402
-  CStrings:  51393
+  Functions: 20838
+  Symbols:   26468
+  CStrings:  51514
 
Symbols:
+ _kFigCaptureSampleBufferMetadata_CalibrationValidationStatuses
+ _kFigCaptureSampleBufferMetadata_InferenceInputDownscalingFactorMultiplier
+ _kFigCaptureSampleBufferMetadata_CoreRepairStatuses
+ _kVTTemporalFilterPropertyKey_FilterStrength
+ _kFigVideoStabilizationSampleBufferProcessorOption_UseCameraGeometry
+ _kFigAppleMakerNote_ModuleAndCalibrationValidationStatuses
+ _FigCaptureTempFileManagerStart
CStrings:
+ "<<<< FigCaptureTempFileUtilities >>>> %!s(MISSING): checking folder at URL %!@(MISSING)"
+ "setColorPostProcessingSkyEnhancementEnabled:"
+ "_streamingSessionAnalyticsMixWithOthersEnabled"
+ "Ti,N,V_calibrationValidationStatusCmPM"
+ "calibrationValidationStatusCmCl"
+ "<<<< FigCaptureSourceServer >>>> %!s(MISSING): %!d(MISSING):\"%!@(MISSING)\","
+ "_scheduleNextFileRemove"
+ "_workaroundToTurnTorchOnWhenStreamStartsIfNecessary"
+ "FigCaptureSourceDetachFromClient"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): %!@(MISSING) was replaced with used part"
+ "setStreamingSessionAnalyticsMixWithOthersEnabled:"
+ "setCalibrationValidationStatusFCCl:"
+ "_calibrationValidationStatusCmCl"
+ "Ti,N,V_calibrationValidationStatusCmCl"
+ "FrontCameraAssembly"
+ "rearCameraCalibrationValid"
+ "FigCaptureDeviceIORegValuesByKeys_block_invoke"
+ "TB,N,V_preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer"
+ "<<<< FigCaptureUtilities >>>> %!s(MISSING): Failed to query Core Repair status for component %!d(MISSING): %!@(MISSING)"
+ "_removeStaleTempFilesInFolderURL:"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Camera %!{(MISSING)public}@ indicates overriden calibration"
+ "Create Shared Device Vendor"
+ "void *CoreRepairCoreLibrary(void)"
+ "sSourceList(%!d(MISSING))"
+ "com.apple.coremedia.tempfileremover"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "capturetempfileutilities_trace"
+ "<<<< FigCaptureSourceServer >>>> %!s(MISSING): source %!p(MISSING) with connection (pid %!d(MISSING)) wasn't found!"
+ "<<<< FigCaptureTempFileUtilities >>>> Fig"
+ "CRComponentState soft_CRGetComponentState(CRComponentType, CFErrorRef *)"
+ "setCoreRepairStatusFrontCameraAssembly:"
+ "<<<< BWAudioSourceNode >>>> %!s(MISSING): Unable to set the audio channel layout with mChannelLayoutTag: %!d(MISSING) for cinematic audio mode"
+ "<<<< FigCaptureTempFileUtilities >>>> %!s(MISSING): Unable to remove file: %!@(MISSING), error = %!@(MISSING)"
+ "_streamingSessionAnalyticsAudioMixWithOthersEnabled"
+ "FigCaptureUtilities.m"
+ "<<<< FigCaptureSourceServer >>>> %!s(MISSING): associating source %!p(MISSING) with connection (pid %!d(MISSING)) (%!d(MISSING),%!d(MISSING))"
+ "makerNoteMetadata"
+ "timeIntervalSinceDate:"
+ "_coreRepairStatusFrontCameraAssembly"
+ "CmPMValidationStatus"
+ "<<<< BWAudioSourceNode >>>> %!s(MISSING): Cinematic Audio: AudioUnitSetProperty kAudioUnitProperty_AudioChannelLayout on the kAudioUnitScope_Output, channelLayout: %!@(MISSING)"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: Core Repair status for %!{(MISSING)public}@ indicated a mismatch"
+ "colorPostProcessingSkyEnhancementEnabled"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Camera %!@(MISSING) Pass"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: Camera %!{(MISSING)public}@ is unknown"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore"
+ "Error associating object with connection"
+ "_colorPostProcessingSkyEnhancementEnabled"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %!s(MISSING): %!@(MISSING): Setting CPP mode '%!d(MISSING)'"
+ "Ti,N,V_coreRepairStatusRearCameraAssembly"
+ "TB,N,V_streamingSessionAnalyticsMixWithOthersEnabled"
+ "<<<< FigCaptureUtilities >>>> %!s(MISSING): Cannot find camera driver service to query calibration validation statuses"
+ "setCalibrationValidationStatusCmCl:"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Device uses original modules for %!@(MISSING)"
+ "<<<< FigCaptureTempFileUtilities >>>> %!s(MISSING): could not get attributes of %!@(MISSING), error = %!@(MISSING)"
+ "<<<< ShaderPreloader >>>> %!s(MISSING): Prewarming CMIMAGING for FlexGTC..."
+ "FigCaptureTempFileUtilities.m"
+ "<<<< FigCaptureCameraParameters >>>> %!s(MISSING): Forcing %!@(MISSING):%!@(MISSING):%!@(MISSING):%!@(MISSING) to 0"
+ "<<<< FigCaptureTempFileUtilities >>>> %!s(MISSING): Removed file: %!{(MISSING)public}@"
+ "preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer"
+ "FigCaptureTempFileRemover"
+ "<<<< FigCaptureSourceServer >>>> %!s(MISSING): )\n"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: Camera %!{(MISSING)public}@ indicates failure with calibration"
+ "FCClValidationStatus"
+ "calibrationValidationStatusCmPM"
+ "_checkTimeSeconds"
+ "workaroundToTurnTorchOnWhenStreamStartsIfNecessary"
+ "fcdv_validateCoreRepairStatuses"
+ "_preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer"
+ "FigCaptureDeviceCoreRepairStatusesByKeys_block_invoke"
+ "+[BWFigCaptureDeviceVendor sharedCaptureDeviceVendorWithDefaultDeviceCreateFunction:]"
+ "<<<< FigCaptureSourceServer >>>> %!s(MISSING): calling disassociate for source %!p(MISSING) with connection (pid %!d(MISSING)), count = %!d(MISSING)"
+ "<<<< FigCaptureSourceServer >>>> %!s(MISSING): Keeping doomedSource %!p(MISSING) on sSourceList because source ia already attached to new client"
+ "RearCameraAssembly"
+ "doomedSource"
+ "Pass"
+ "Ti,N,V_coreRepairStatusFrontCameraAssembly"
+ "Ti,N,V_calibrationValidationStatusFCCl"
+ "calibrationValidationStatusFCCl"
+ "<<<< FigCaptureTempFileUtilities >>>> %!s(MISSING): file %!@(MISSING) is %!f(MISSING) seconds old (staletime = %!f(MISSING), stale = %!d(MISSING))"
+ "_calibrationValidationStatusCmPM"
+ "Query Device IOReg Values"
+ "streamingSessionAnalyticsMixWithOthersEnabled"
+ "coreRepairStatusRearCameraAssembly"
+ "CRGetComponentState"
+ "_calibrationValidationStatusFCCl"
+ "<<<< FigCaptureSourceServer >>>> %!s(MISSING): disassociating source %!p(MISSING) with connection (pid %!d(MISSING)) (%!d(MISSING),%!d(MISSING))"
+ "sPrewarmingSourceList(%!d(MISSING))"
+ "_collectedAnalyticsForModuleAndCalibrationValidationStatuses"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: Camera %!@(MISSING) is not available"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: Core Repair status for %!{(MISSING)public}@ indicated an issue"
+ "setWorkaroundToTurnTorchOnWhenStreamStartsIfNecessary:"
+ "<<<< FigCaptureSource >>>> %!s(MISSING): requested client audit token doesn't match source (source PID = %!d(MISSING))"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: Core Repair status for %!@(MISSING) is not available"
+ "setPreferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer:"
+ "_coreRepairStatusRearCameraAssembly"
+ "<<<< FigCaptureTempFileUtilities >>>> %!s(MISSING): Failed to get contents of folder at URL %!@(MISSING) (%!@(MISSING))"
+ "<<<< FigCaptureUtilities >>>> %!s(MISSING): Unknown DeviceIORegValue string: %!@(MISSING)"
+ "setCalibrationValidationStatusCmPM:"
+ "fccp_cameraParametersAdjustedForBadFrontCameraAssemblyStatus"
+ "<<<< FigCaptureUtilities >>>> %!s(MISSING): Failed to determine Core Repair component for %!@(MISSING)"
+ "<<<< FigCaptureSource >>>> %!s(MISSING): attaching client %!d(MISSING) for source %!p(MISSING)"
+ "TB,N,V_colorPostProcessingSkyEnhancementEnabled"
+ "description=CameraCapture-580.11.21.1"
+ "<< FigCaptureSessionServer >> %!s(MISSING): Server started! (took %!l(MISSING)f ms)"
+ "fcdv_validateCalibrationStatuses"
+ "<<<< FigCaptureCameraParameters >>>> %!s(MISSING): Making feature adjustments for front camera assembly status of %!d(MISSING)"
+ "Query CoreRepair Statuses"
+ "fcu_deviceIORegValueFromStringRepresentation"
+ "<<<< FigCaptureUtilities >>>> %!s(MISSING): %!@(MISSING) took %!f(MISSING)ms"
+ "<FigCaptureSource %!p(MISSING)> retainCount: %!l(MISSING)d%!s(MISSING), allocator: %!p(MISSING), type: %!@(MISSING), position: %!@(MISSING), active = %!d(MISSING), token = %!l(MISSING)ld, prewarmEnabled = %!d(MISSING), cbi = %!@(MISSING)"
+ "setCoreRepairStatusRearCameraAssembly:"
+ "com.apple.quicktime.apple-maker-note.91"
+ "_fileRemoverBlock"
+ "_rearCameraCalibrationValid"
+ "-[FigCaptureTempFileRemover _removeStaleTempFilesInFolderURL:]"
+ "TB,R,V_rearCameraCalibrationValid"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: Camera %!{(MISSING)public}@ indicates invalid calibration"
+ "_workaroundShouldTurnOnTorchWhenNextStreamStarts"
+ "<<<< FigCaptureSourceServer >>>> %!s(MISSING): %!@(MISSING) = (\n"
+ "<<<< FigCaptureSource >>>> %!s(MISSING): detaching client %!d(MISSING) from source %!p(MISSING)"
+ "_staleTimeSeconds"
+ "TB,N,V_workaroundToTurnTorchOnWhenStreamStartsIfNecessary"
+ "_folderList"
+ "coreRepairStatusFrontCameraAssembly"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): %!@(MISSING) was replaced with service part"
+ "css_dumpSourceArray"
- "makerNoteDict"
- "<< FigCaptureSessionServer >> %!s(MISSING): Server started!"
- "description=CameraCapture-580.6.21"
- "cameraCalibrationValid"
- "TB,R,V_cameraCalibrationValid"
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Cannot find camera driver, cameraDriverService=%!d(MISSING)"
- "-[BWFigCaptureDeviceVendor _isCameraCalibrationValid]"
- "_cameraCalibrationValid"
- "<FigCaptureSource %!p(MISSING)> retainCount: %!l(MISSING)d%!s(MISSING), allocator: %!p(MISSING), type: %!@(MISSING), position: %!@(MISSING)"
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: camera calibration validation was not successful, CmClValidationStatus = %!@(MISSING) ."
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Warning: camera calibration validation override, CmClValidationStatus = %!@(MISSING) ."

```
