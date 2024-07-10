## AudioDSP

> `/System/Library/Components/AudioDSP.component/Contents/MacOS/AudioDSP`

```diff

-747.117.0.0.0
-  __TEXT.__text: 0x774670
+747.124.0.0.0
+  __TEXT.__text: 0x778efc
   __TEXT.__auth_stubs: 0x4660
   __TEXT.__objc_stubs: 0x1080
   __TEXT.__objc_methlist: 0x254
-  __TEXT.__const: 0x80f90
-  __TEXT.__gcc_except_tab: 0x59884
-  __TEXT.__cstring: 0x73003
-  __TEXT.__oslogstring: 0x3d38c
+  __TEXT.__const: 0x80f80
+  __TEXT.__gcc_except_tab: 0x59c48
+  __TEXT.__cstring: 0x731d0
+  __TEXT.__oslogstring: 0x3d4a7
   __TEXT.__objc_methname: 0x11f7
   __TEXT.__objc_classname: 0x13b
   __TEXT.__objc_methtype: 0x1140
   __TEXT.__dlopen_cstrs: 0x9e
-  __TEXT.__unwind_info: 0x25d70
+  __TEXT.__unwind_info: 0x260a8
   __TEXT.__eh_frame: 0xb8
   __DATA_CONST.__auth_got: 0x2348
   __DATA_CONST.__got: 0x428
-  __DATA_CONST.__auth_ptr: 0x448
-  __DATA_CONST.__const: 0x43af0
-  __DATA_CONST.__cfstring: 0x23760
+  __DATA_CONST.__auth_ptr: 0x450
+  __DATA_CONST.__const: 0x43ee0
+  __DATA_CONST.__cfstring: 0x23700
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 30765
+  Functions: 30925
   Symbols:   1481
-  CStrings:  12611
+  CStrings:  12625
 
Symbols:
+ __ZN8AudioDSP4Core11HeadTracker10InitializeENSt3__18optionalIbEE
- __ZN8AudioDSP4Core11HeadTracker10InitializeEv
CStrings:
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/CoreAudioUtility/Source/Utility/CALegacyLog.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/AUSpatialCapture/SCTwoInputMixer.hpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/AUSpatialCapture/SpatialCapture.mm"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/AudioMeter/dsp/DspLibAudioMeter.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassKoenig/dsp/DspLibBassKoenig.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibBassQueen.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibMitigationAdaptation.h"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquad.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquad.h"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquadDesigns.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BuzzKill/dsp/DspLibBuzzKill.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BuzzKill/dsp/DspLibBuzzKillClasses.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ControlFreak/dsp/DspLibControlFreak.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FFT/dsp/DspLibFFT.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FFT/dsp/DspLibFFT.h"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FourBandRandomOrderLrFilterBank/dsp/DspLibFourBandRandomOrderLrFilterBank.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/HilbertTransform/dsp/DspLibHilbertTransform.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessMeter/dsp/DspLibLoudnessMeter.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessNormalizer/dsp/DspLibLoudnessNormalizer.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceMeasurement.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceModels.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ModelFit.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1PilotTone.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1TestToneGenerator.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/PowerGuard/dsp/DspLibPowerGuardClasses.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceMeasurement.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceModels.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ModelFit.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerModel/dsp/DspLibLoudspeakerModel.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerModel/dsp/DspLibLoudspeakerModelParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LowFlow/dsp/DspLibLowFlowAnalysisPath.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueck.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueckKernel.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MozartCompressor/dsp/DspLibMozartCompressor.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/NotchFilterBank/dsp/DspLibNotchFilterBank.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuard.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuardAdmittanceFilterCoeffSet.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/RMS/dsp/DspLibRMS.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/SampleRateConverter/dsp/DspLibSampleRateConverter.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ThermalSpeakerProtection/dsp/DspLibThermalSpeakerProtection.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Utilities/DspLibBase.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Utilities/DspLibBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/VirtualBass/dsp/DspLibNonLinearDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/VirtualBass/dsp/DspLibVirtualBass.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_FIRMatrix.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_HRIRdatabase.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/VoiceProcessor_v2.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/VoiceProcessor_v2.h"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDSPChains/vpSetupDownlinkDSPChain.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDSPChains/vpSetupUplinkDSPChain.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_DefaultsOverride.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_FileInjection.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_FileSaving.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_Logging.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_Loopback.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDesktop_v2.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpInitialize/vpInitializeDownlink.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpInitialize/vpInitializeUplink.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpInitialize/vpProperties.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpInitialize/vpTuningHelper.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpProcessing/vpProcessUplink_v2.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v3/vpProcessDownlink_v3.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v3/vpProcessUplink_v3.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v4/vpProcessDownlink_v4.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v4/vpProcessUplink_v4.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v5/vpProcessUplink_v5.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v6/VoiceProcessor_v6.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v6/vpProcessUplink_v6.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/IO_Node_Audio_Capturer_Factory.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/IO_Node_Audio_Injector_Factory.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/components/CPU_Profiler+Node_Decorator.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/dsp/Graph.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Graph.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Node.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Node_Socket.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Parameter_Exchange.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Port.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Property_Exchange.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/nodes/Far_End_Voice_Proc_Node.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/nodes/Mic_Ref_Sync_Node.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/ports/Audio_Buffer_Port.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/ports/Audio_Ring_Buffer_Port.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/wires/Audio_Converter_Wire.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/wires/Audio_Pass_Through_Wire.cpp"
+ "21:56:39"
+ "21:56:43"
+ "21:56:57"
+ "22:02:59"
+ "22:03:04"
+ "22:03:16"
+ "@@ Strips Jul  2 2024 21:50:01"
+ "AUSMMatrixMix.cpp"
+ "ChangeStreamFormat"
+ "EQGainLimit"
+ "EQGainOffset"
+ "EQNotchGainLimit"
+ "EQNotchQ"
+ "HW REF Bluetooth HLC 2 channels State"
+ "InHeadGaindB"
+ "Jul  2 2024"
+ "application bundle ID"
+ "assertion failure: system status service is null"
+ "create system status manager"
+ "in-head parameter dictionary"
+ "not active"
+ "reference port Bluetooth HLC 2 channels state"
+ "scratchBuffer.size() == numNonLFEChannels * effectiveNumInputChannels"
+ "std::string_view vp::reflect_type_name() [T = vp::vx::System_Status_Manager]"
+ "std::string_view vp::reflect_value_name() [V = vp::vx::Property_ID::Ref_Port_Bluetooth_HLC_2ch_State]"
+ "vp_ref_port_bluetooth_HLC_2ch_state"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/CoreAudioUtility/Source/Utility/CALegacyLog.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/AUSpatialCapture/SCTwoInputMixer.hpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/AUSpatialCapture/SpatialCapture.mm"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/AudioMeter/dsp/DspLibAudioMeter.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassKoenig/dsp/DspLibBassKoenig.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibBassQueen.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibMitigationAdaptation.h"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquad.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquad.h"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquadDesigns.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BuzzKill/dsp/DspLibBuzzKill.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BuzzKill/dsp/DspLibBuzzKillClasses.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ControlFreak/dsp/DspLibControlFreak.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FFT/dsp/DspLibFFT.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FFT/dsp/DspLibFFT.h"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FourBandRandomOrderLrFilterBank/dsp/DspLibFourBandRandomOrderLrFilterBank.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/HilbertTransform/dsp/DspLibHilbertTransform.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessMeter/dsp/DspLibLoudnessMeter.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessNormalizer/dsp/DspLibLoudnessNormalizer.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceMeasurement.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceModels.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ModelFit.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1PilotTone.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1TestToneGenerator.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/PowerGuard/dsp/DspLibPowerGuardClasses.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceMeasurement.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceModels.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ModelFit.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerModel/dsp/DspLibLoudspeakerModel.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerModel/dsp/DspLibLoudspeakerModelParameters.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LowFlow/dsp/DspLibLowFlowAnalysisPath.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueck.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueckKernel.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MozartCompressor/dsp/DspLibMozartCompressor.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/NotchFilterBank/dsp/DspLibNotchFilterBank.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuard.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuardAdmittanceFilterCoeffSet.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/RMS/dsp/DspLibRMS.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/SampleRateConverter/dsp/DspLibSampleRateConverter.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ThermalSpeakerProtection/dsp/DspLibThermalSpeakerProtection.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Utilities/DspLibBase.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Utilities/DspLibBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/VirtualBass/dsp/DspLibNonLinearDevice.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/VirtualBass/dsp/DspLibVirtualBass.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_FIRMatrix.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_HRIRdatabase.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/VoiceProcessor_v2.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/VoiceProcessor_v2.h"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDSPChains/vpSetupDownlinkDSPChain.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDSPChains/vpSetupUplinkDSPChain.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_DefaultsOverride.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_FileInjection.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_FileSaving.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_Logging.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDebugFeatures/vpDebug_Loopback.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpDesktop_v2.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpInitialize/vpInitializeDownlink.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpInitialize/vpInitializeUplink.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpInitialize/vpProperties.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpInitialize/vpTuningHelper.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v2/vpProcessing/vpProcessUplink_v2.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v3/vpProcessDownlink_v3.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v3/vpProcessUplink_v3.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v4/vpProcessDownlink_v4.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v4/vpProcessUplink_v4.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v5/vpProcessUplink_v5.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v6/VoiceProcessor_v6.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/VoiceProcessor_v6/vpProcessUplink_v6.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/IO_Node_Audio_Capturer_Factory.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/IO_Node_Audio_Injector_Factory.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/components/CPU_Profiler+Node_Decorator.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/dsp/Graph.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Graph.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Node.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Node_Socket.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Parameter_Exchange.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Port.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/Property_Exchange.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/nodes/Far_End_Voice_Proc_Node.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/nodes/Mic_Ref_Sync_Node.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/ports/Audio_Buffer_Port.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/ports/Audio_Ring_Buffer_Port.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/wires/Audio_Converter_Wire.cpp"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AudioDSP/Source/AudioDSP/VoiceProcessor/vp/vx/io/wires/Audio_Pass_Through_Wire.cpp"
- "18:34:59"
- "18:35:02"
- "18:35:18"
- "18:41:54"
- "18:42:00"
- "18:42:14"
- "@@ Strips Jun 14 2024 18:27:58"
- "InHeadGain"
- "Jun 14 2024"
- "UpdateSpatializationAlgorithm"
- "changeNumberOfOutputChannels"
- "std::string_view vp::reflect_value_name() [V = (vp::vx::Property_ID)92]"

```
