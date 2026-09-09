## cameraispd

> `/usr/libexec/cameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

 20.77.0.0.0
-  __TEXT.__text: 0x7ce40
-  __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_stubs: 0xf80
+  __TEXT.__text: 0x7e754
+  __TEXT.__auth_stubs: 0x1f90
+  __TEXT.__objc_stubs: 0x11e0
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x18e0
+  __TEXT.__gcc_except_tab: 0x1a2c
   __TEXT.__const: 0x2c18
-  __TEXT.__cstring: 0x77aa
+  __TEXT.__cstring: 0x7c83
   __TEXT.__oslogstring: 0x5fd3
-  __TEXT.__objc_methname: 0x1295
+  __TEXT.__objc_methname: 0x13f2
   __TEXT.__objc_classname: 0x88
   __TEXT.__objc_methtype: 0x1067
-  __TEXT.__unwind_info: 0x1248
-  __DATA_CONST.__const: 0x9a28
-  __DATA_CONST.__cfstring: 0x2bc0
+  __TEXT.__unwind_info: 0x12c0
+  __DATA_CONST.__const: 0x9ac0
+  __DATA_CONST.__cfstring: 0x3060
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0xfa0
-  __DATA_CONST.__got: 0xc98
+  __DATA_CONST.__auth_got: 0xfd8
+  __DATA_CONST.__got: 0xcd8
   __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x5c8
-  __DATA.__objc_selrefs: 0x4f8
+  __DATA.__objc_selrefs: 0x590
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x3bdde0
-  __DATA.__common: 0xf
+  __DATA.__data: 0x3be2c0
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1561
-  Symbols:   918
-  CStrings:  1844
+  Functions: 1578
+  Symbols:   933
+  CStrings:  1916
 
Symbols:
+ _AnalyticsSendEventLazy
+ _IOSurfaceGetBytesPerRow
+ _IOSurfaceGetHeight
+ _IOSurfaceGetWidth
+ _OBJC_CLASS_$_ABDMetadata
+ _OBJC_CLASS_$_ABDProcessor
+ ___cxa_atexit
+ _kFigCaptureStreamMetadata_AEApertureActiveSignals
+ _kFigCaptureStreamMetadata_AEInputSignals
+ _kFigCaptureStreamMetadata_AESignals
+ _kFigCaptureStreamMetadata_ApertureDiameter
+ _kFigCaptureStreamMetadata_ApertureHealth
+ _kFigCaptureStreamMetadata_ISPApertureData
+ _kFigCaptureStreamMetadata_MagneticInterferenceMitigated
+ _kFigCaptureStreamMetadata_SensorSigningSignatureRect
+ _kFigCaptureStreamMetadata_TargetFNumber
+ _kFigCaptureStreamMetadata_TemporalNoiseReductionMachineLearningImageRegistrationEnabled
+ _kFigCaptureStreamMetadata_TimewarpActualFrameRate
+ _kFigCaptureStreamMetadata_TimewarpDecimationLevel
+ _kFigCaptureStreamMetadata_TimewarpDecimationTag
+ _kFigCaptureStreamMetadata_TimewarpDesiredFrameRate
+ _kFigCaptureStreamMetadata_TimewarpSequenceCaptureID
+ _kFigCaptureStreamMetadata_TimewarpShouldSkipFrame
+ _work_interval_join_port
+ _work_interval_leave
- _kFigCaptureStreamMetadata_AD
- _kFigCaptureStreamMetadata_AH
- _kFigCaptureStreamMetadata_ActiveSignals
- _kFigCaptureStreamMetadata_IAD
- _kFigCaptureStreamMetadata_IREnabled
- _kFigCaptureStreamMetadata_InputSignals
- _kFigCaptureStreamMetadata_MIM
- _kFigCaptureStreamMetadata_RatioNumber
- _kFigCaptureStreamMetadata_Signals
- _kFigCaptureStreamProperty_SSSR
CStrings:
+ "%s took %llu usec"
+ "%s%s-%04d.raw"
+ "%s: ABDNet: Received %lu buffers (%lu)"
+ "/usr/local/share/firmware/isp/dcs_v6x_isp_fw.bin"
+ "/var/mobile/Media/DCIM/%s-ABD-"
+ "@\"NSDictionary\"8@?0"
+ "ABDNet: ABDProcessor not available - is ISPKit missing?"
+ "ABDNet: Bad inputs"
+ "ABDNet: Created pixel buffer: %zux%zu[%zu]"
+ "ABDNet: Dump input buffers"
+ "ABDNet: Dump output buffers"
+ "ABDNet: Execution"
+ "ABDNet: Extra info version mismatch: expected %d, got %d"
+ "ABDNet: Not familiar with this buffer. Not copying it anymore"
+ "ABDNet: Surface"
+ "ABDNet: Surface ID: %d, %zux%zu[%zu] - received %dx%d[%d]"
+ "ABDNet: Unknown configuration ID %d"
+ "ABDNet: disabled by environment"
+ "ABDNet: expected %d buffers, got %d"
+ "ABDNetDumpRate"
+ "ABDNetEnable"
+ "ABDNetPeriodic event: %@"
+ "ABDNetPriodic analytics: unknown resolution! w=%zu, h=%zu"
+ "ABDNetProcessot invalid"
+ "ABDNetVerbose"
+ "AGain"
+ "DGain"
+ "EffectiveFPS"
+ "ExposureIntegrationTime"
+ "ExposureTime"
+ "FrontCameraRenoModuleSerialNumString"
+ "GLFramesInPeriod"
+ "InferenceTime"
+ "InputResolution"
+ "LLFramesInPeriod"
+ "LuxLevel"
+ "Mapping: 0x%llx to %@"
+ "ModelReloaded"
+ "ModelSwitched"
+ "ModelSwitchesInPeriod"
+ "ModelType"
+ "SIFR"
+ "SmartTapAlgorithmMetadata"
+ "TotalGain"
+ "TotalLatency"
+ "com.apple.applecamerad.ABDNetPeriodic"
+ "com.apple.isp.frontrenocamerapower"
+ "com.apple.isp.frontrenocamerasensorconfig"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "inferenceTime"
+ "input"
+ "lastProcessingStats"
+ "modelReloaded"
+ "nameOfConfig:"
+ "noiseAddbackFactor"
+ "now"
+ "numberWithDouble:"
+ "numberWithFloat:"
+ "numberWithUnsignedLong:"
+ "numberWithUnsignedLongLong:"
+ "output"
+ "outputRaw"
+ "process:into:configId:metadata:"
+ "raw"
+ "setAnalogGain:"
+ "setBufferHeight:"
+ "setBufferMap"
+ "setBufferWidth:"
+ "setHrdRatio:"
+ "setLuxLevel:"
+ "setTotalGain:"
+ "unsignedLongLongValue"
+ "v32@?0@8@16^B24"
- "ISPABDProcessor: ISPKit support not available"
```
