## AudioDSP

> `/System/Library/Components/AudioDSP.component/Contents/MacOS/AudioDSP`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-881.108.0.0.0
-  __TEXT.__text: 0x3b6db0
-  __TEXT.__realtime: 0x16b400
-  __TEXT.__auth_stubs: 0x4000
-  __TEXT.__objc_stubs: 0x1720
+881.112.0.0.0
+  __TEXT.__text: 0x3b7550
+  __TEXT.__realtime: 0x16b528
+  __TEXT.__auth_stubs: 0x4040
+  __TEXT.__objc_stubs: 0x1740
   __TEXT.__objc_methlist: 0x414
-  __TEXT.__const: 0xa4490
-  __TEXT.__cstring: 0x35909
-  __TEXT.__gcc_except_tab: 0x32884
-  __TEXT.__oslogstring: 0x333ea
-  __TEXT.__objc_methname: 0x13b8
+  __TEXT.__const: 0xa44a0
+  __TEXT.__cstring: 0x357f8
+  __TEXT.__gcc_except_tab: 0x32970
+  __TEXT.__oslogstring: 0x33593
+  __TEXT.__objc_methname: 0x13ce
   __TEXT.__objc_classname: 0xf4
   __TEXT.__objc_methtype: 0xadf
-  __TEXT.__unwind_info: 0xf0b8
+  __TEXT.__unwind_info: 0xf0e0
   __TEXT.__eh_frame: 0xf8
-  __DATA_CONST.__const: 0x316b8
-  __DATA_CONST.__cfstring: 0x21080
+  __DATA_CONST.__const: 0x316c0
+  __DATA_CONST.__cfstring: 0x210c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x2010
+  __DATA_CONST.__auth_got: 0x2030
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x890
-  __DATA.__objc_selrefs: 0x6d0
+  __DATA.__objc_selrefs: 0x6d8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2fc0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 11981
-  Symbols:   1321
-  CStrings:  11909
+  Symbols:   1325
+  CStrings:  11917
 
Symbols:
+ _BNNSGraphCompileOptionsSetFileWriteFSyncBarrier
+ _BNNSGraphCompileOptionsSetOutputPathWithPermissionsAndProtectionClass
+ _BNNSGraphCompileOptionsSetPreallocateOutputFile
+ _NSTemporaryDirectory
+ _sparse_set_matrix_property
- _BNNSGraphCompileOptionsSetOutputPath
CStrings:
+ "%25s:%-5d Failed to create matrix"
+ "%25s:%-5d Failed to set real-time safe mode on matrix"
+ "%25s:%-5d cached BNNS IR '%s' is unreadable (%s) -- removing stale entry (likely PROTECTION_CLASS_F key purge after reboot)"
+ "%25s:%-5d cached BNNS IR '%s' open failed (%s) -- leaving entry in place"
+ "%25s:%-5d failed to remove stale cache '%s': %s"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassKoenig/dsp/DspLibBassKoenig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibBassQueen.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibMitigationAdaptation.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BuzzKill/dsp/DspLibBuzzKill.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ControlFreak/dsp/DspLibControlFreak.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FFT/dsp/DspLibFFT.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FourBandRandomOrderLrFilterBank/dsp/DspLibFourBandRandomOrderLrFilterBank.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessMeter/dsp/DspLibLoudnessMeter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessNormalizer/dsp/DspLibLoudnessNormalizer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceMeasurement.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceModels.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ModelFit.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1PilotTone.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1TestToneGenerator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceMeasurement.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceModels.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerModel/dsp/DspLibLoudspeakerModelParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LowFlow/dsp/DspLibLowFlowAnalysisPath.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueck.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueckKernel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MozartCompressor/dsp/DspLibMozartCompressor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuard.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuardAdmittanceFilterCoeffSet.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/RMS/dsp/DspLibRMS.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/SampleRateConverter/dsp/DspLibSampleRateConverter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ThermalSpeakerProtection/dsp/DspLibThermalSpeakerProtection.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Utilities/DspLibBase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/VirtualBass/dsp/DspLibVirtualBass.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_FIRMatrix.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jl5ZkO/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_HRIRdatabase.cpp"
+ "19:22:41"
+ "19:22:51"
+ "19:23:07"
+ "AULoudspeakerSystemIDV2::Initialize failed — algorithm is null (gInstanceCounter=%u)"
+ "AudioCapture/AUSM"
+ "DeviceState"
+ "Jul 11 2026"
+ "[%s|%s] Capture directory exists but is not writable: %@"
+ "[%s|%s] Failed to prepare a writable capture directory."
+ "isWritableFileAtPath:"
- "%25s:%-5d exists() failed for primary cache '%s': %s"
- "%25s:%-5d exists() failed for secondary cache '%s': %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassKoenig/dsp/DspLibBassKoenig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibBassQueen.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibMitigationAdaptation.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BuzzKill/dsp/DspLibBuzzKill.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ControlFreak/dsp/DspLibControlFreak.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FFT/dsp/DspLibFFT.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FourBandRandomOrderLrFilterBank/dsp/DspLibFourBandRandomOrderLrFilterBank.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessMeter/dsp/DspLibLoudnessMeter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessNormalizer/dsp/DspLibLoudnessNormalizer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceMeasurement.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceModels.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ModelFit.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1PilotTone.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1TestToneGenerator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceMeasurement.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceModels.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerModel/dsp/DspLibLoudspeakerModelParameters.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LowFlow/dsp/DspLibLowFlowAnalysisPath.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueck.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueckKernel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MozartCompressor/dsp/DspLibMozartCompressor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuard.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuardAdmittanceFilterCoeffSet.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/RMS/dsp/DspLibRMS.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/SampleRateConverter/dsp/DspLibSampleRateConverter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ThermalSpeakerProtection/dsp/DspLibThermalSpeakerProtection.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Utilities/DspLibBase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/VirtualBass/dsp/DspLibVirtualBass.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_FIRMatrix.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Px26Sq/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_HRIRdatabase.cpp"
- "00:45:32"
- "00:45:42"
- "00:45:58"
- "Jun 27 2026"
```
