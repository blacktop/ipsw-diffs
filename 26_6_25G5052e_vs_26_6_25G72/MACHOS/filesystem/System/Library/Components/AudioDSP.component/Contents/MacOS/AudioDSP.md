## AudioDSP

> `/System/Library/Components/AudioDSP.component/Contents/MacOS/AudioDSP`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-819.603.0.0.0
-  __TEXT.__text: 0x5b7838
-  __TEXT.__auth_stubs: 0x4660
+819.701.0.0.0
+  __TEXT.__text: 0x5b7a28
+  __TEXT.__auth_stubs: 0x4670
   __TEXT.__objc_stubs: 0x1740
   __TEXT.__objc_methlist: 0x45c
-  __TEXT.__gcc_except_tab: 0x3d890
+  __TEXT.__gcc_except_tab: 0x3d8a8
   __TEXT.__const: 0xda380
   __TEXT.__cstring: 0x3a14e
-  __TEXT.__oslogstring: 0x36836
+  __TEXT.__oslogstring: 0x37364
   __TEXT.__objc_methname: 0x1405
   __TEXT.__objc_classname: 0x108
   __TEXT.__objc_methtype: 0xc84
   __TEXT.__unwind_info: 0x168f8
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x2340
+  __DATA_CONST.__auth_got: 0x2348
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x2f8
   __DATA_CONST.__const: 0x334c8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 20195
-  Symbols:   1496
-  CStrings:  12756
+  Symbols:   1497
+  CStrings:  12760
 
Symbols:
+ _sparse_set_matrix_property
Functions:
~ sub_d7028 : 3136 -> 3336
~ sub_1bca04 -> sub_1bcacc : 1336 -> 1632
CStrings:
+ "%25s:%-5d EXCEPTION (%d) [!validContext is false]: \"Unable to load BNNS Context\""
+ "%25s:%-5d EXCEPTION (%d) [(mInputSize != mNumMelBands*2) is false]: \"mInputSize is wrong.\""
+ "%25s:%-5d EXCEPTION (%d) [(mInputSize != mNumMelBands*mNumContextFrames*(1+mDeltaFeature)) is false]: \"mInputSize is wrong.\""
+ "%25s:%-5d EXCEPTION (%d) [activationDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Activation.\""
+ "%25s:%-5d EXCEPTION (%d) [activationFunction_ref.get_cf() == nullptr is false]: \"Failed to retrieve activation function (Function) from dictionary Activation.\""
+ "%25s:%-5d EXCEPTION (%d) [biasDataType_ref.get_cf() == nullptr is false]: \"Missing dictionary DataType from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d) [biasDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Bias from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"BlockSize not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"ECOutScale not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"FFT2Mel matrix not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve BlockSize.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve ECleeScale.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve ECoutScale.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve HangA01.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve HangA10.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve InputScale.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve NumContextFrames.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve NumLayers.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve WaitFrames.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve forgetting factor Lambda_TC.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve sample rate.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve threshold.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"KalmanObservationStd not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"KalmanProcessStd not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"LambdaPSD_TC not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"MCLPOutScale not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Alpha from dictionary Activation.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Beta from dictionary Activation.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary Bias.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary InputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary Bias.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary InputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Size from dictionary InputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Size from dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing vector Data from dictionary Bias.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing vector Data from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"NumContextFrames not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"NumInputChannels not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"SampleRate not loaded\""
+ "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"WaitFrames not loaded.\""
+ "%25s:%-5d EXCEPTION (%d) [inState.size() != outState.size() is false]: \"Input state %s size (%zu) not matching the output state size %s (%zu).\""
+ "%25s:%-5d EXCEPTION (%d) [inputDataType_ref.get_cf() == nullptr is false]: \"Missing dictionary DataType.\""
+ "%25s:%-5d EXCEPTION (%d) [inputDescDict_ref.get_cf() == nullptr is false]: \"Missing dictionary InputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [inputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputName from (%s).\""
+ "%25s:%-5d EXCEPTION (%d) [inputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputName.\""
+ "%25s:%-5d EXCEPTION (%d) [ioStates_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputOutputStates.\""
+ "%25s:%-5d EXCEPTION (%d) [layer.mBiasVector.size() != weightsSizeOutput is false]: \"NeuralNetBNNS: Layer (%u), bias size (%lu) is not matching the weight output vector size (%lu).\""
+ "%25s:%-5d EXCEPTION (%d) [layer.mWeightsQuantized.size() != weightsNumberOfCoefficients is false]: \"NeuralNetBNNS: Layer (%u), number of weights (%lu) is not matching the required number of weights (%lu).\""
+ "%25s:%-5d EXCEPTION (%d) [layerType_ref.get_cf() == nullptr is false]: \"Failed to retrieve layer type (Type) from dictionary LayerDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [mDNNLayer[layerIdx].mFilter == nullptr is false]: \"NeuralNetBNNS: Layer (%u), filter not created.\""
+ "%25s:%-5d EXCEPTION (%d) [mGraph.data == nullptr is false]: \"unable to compile program %s\""
+ "%25s:%-5d EXCEPTION (%d) [mInputSize != featureVectorSize is false]: \"mInputSize of NeuralNet (%u) is not matching the feature vector size (%u).\""
+ "%25s:%-5d EXCEPTION (%d) [mOutputSize != mNumFFTBins is false]: \"NeuralNet output size (%u) is not matching the number of FFT bins (%u).\""
+ "%25s:%-5d EXCEPTION (%d) [modelNetExt == \".ir\" is false]: \"No MIL fallback option available\""
+ "%25s:%-5d EXCEPTION (%d) [modelNetPathBase_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPathBase.\""
+ "%25s:%-5d EXCEPTION (%d) [modelNetPathRelative_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPath.\""
+ "%25s:%-5d EXCEPTION (%d) [modelNetPath_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPath.\""
+ "%25s:%-5d EXCEPTION (%d) [modelPlistInfo.streamingMode_int >= static_cast<UInt32>(StreamingMode::NumModes) is false]: \"StreamingMode (%u) is out of range, a value smaller than (%d) is expected.\""
+ "%25s:%-5d EXCEPTION (%d) [nnLayers[i].mWeightsQuantized.size() != weightsNumberOfCoefficients is false]: \"Number of weights in Data (%lu) does not match the required number of weights (%lu).\""
+ "%25s:%-5d EXCEPTION (%d) [numStates_ref.get_cf() == nullptr is false]: \"Failed to retrieve NumStates from InputOutputStates.\""
+ "%25s:%-5d EXCEPTION (%d) [outputDataType_ref.get_cf() == nullptr is false]: \"Failed to retrieve output data type (DataType) from dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [outputDescDict_ref.get_cf() == nullptr is false]: \"Missing dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d) [outputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve OutputName from (%s).\""
+ "%25s:%-5d EXCEPTION (%d) [outputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve OutputName.\""
+ "%25s:%-5d EXCEPTION (%d) [pNeuralNetImpl == nullptr is false]: \"NeuralNet implementation not initialized.\""
+ "%25s:%-5d EXCEPTION (%d) [state_ref.get_cf() == nullptr is false]: \"Missing dictionary (%s).\""
+ "%25s:%-5d EXCEPTION (%d) [topLevelDict_ref.get_cf() == nullptr is false]: \"Missing dictionary: %s\""
+ "%25s:%-5d EXCEPTION (%d) [weightsDataType_ref.get_cf() == nullptr is false]: \"Missing DataType from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d) [weightsDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Weights.\""
+ "%25s:%-5d Failed to create matrix"
+ "%25s:%-5d Failed to set real-time safe mode on matrix"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/AUSpatialCapture/SCTwoInputMixer.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/AUSpatialCapture/SpatialCapture.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassKoenig/dsp/DspLibBassKoenig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibBassQueen.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibMitigationAdaptation.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquad.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquad.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquadDesigns.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BuzzKill/dsp/DspLibBuzzKill.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ControlFreak/dsp/DspLibControlFreak.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FFT/dsp/DspLibFFT.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FourBandRandomOrderLrFilterBank/dsp/DspLibFourBandRandomOrderLrFilterBank.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/HilbertTransform/dsp/DspLibHilbertTransform.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessMeter/dsp/DspLibLoudnessMeter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessNormalizer/dsp/DspLibLoudnessNormalizer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceMeasurement.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceModels.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ModelFit.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1PilotTone.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1TestToneGenerator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/PowerGuard/dsp/DspLibPowerGuardClasses.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceMeasurement.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceModels.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerModel/dsp/DspLibLoudspeakerModelParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LowFlow/dsp/DspLibLowFlowAnalysisPath.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueck.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueckKernel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MozartCompressor/dsp/DspLibMozartCompressor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuard.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuardAdmittanceFilterCoeffSet.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/RMS/dsp/DspLibRMS.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/SampleRateConverter/dsp/DspLibSampleRateConverter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ThermalSpeakerProtection/dsp/DspLibThermalSpeakerProtection.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Utilities/DspLibBase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/VirtualBass/dsp/DspLibVirtualBass.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_FIRMatrix.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oUEOU0/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_HRIRdatabase.cpp"
+ "20:20:31"
+ "20:20:36"
+ "20:20:58"
+ "20:21:00"
+ "20:21:08"
+ "20:26:57"
+ "20:27:03"
+ "20:27:20"
+ "Jul 11 2026"
- "%25s:%-5d EXCEPTION (%d): \"BlockSize not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"ECOutScale not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"FFT2Mel matrix not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve BlockSize.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve ECleeScale.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve ECoutScale.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve HangA01.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve HangA10.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve InputName from (%s).\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve InputName.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve InputOutputStates.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve InputScale.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve ModelNetPath.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve ModelNetPathBase.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve NumContextFrames.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve NumLayers.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve NumStates from InputOutputStates.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve OutputName from (%s).\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve OutputName.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve WaitFrames.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve activation function (Function) from dictionary Activation.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve forgetting factor Lambda_TC.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve layer type (Type) from dictionary LayerDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve output data type (DataType) from dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve sample rate.\""
- "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve threshold.\""
- "%25s:%-5d EXCEPTION (%d): \"Input state %s size (%zu) not matching the output state size %s (%zu).\""
- "%25s:%-5d EXCEPTION (%d): \"KalmanObservationStd not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"KalmanProcessStd not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"LambdaPSD_TC not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"MCLPOutScale not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing DataType from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary (%s).\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary Activation.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary Bias from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary DataType from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary DataType.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary InputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing dictionary: %s\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar Alpha from dictionary Activation.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar Beta from dictionary Activation.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataBias from dictionary Bias.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataBias from dictionary InputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataBias from dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataBias from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataScale from dictionary Bias.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataScale from dictionary InputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataScale from dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataScale from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar Size from dictionary InputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing scalar Size from dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing vector Data from dictionary Bias.\""
- "%25s:%-5d EXCEPTION (%d): \"Missing vector Data from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d): \"NeuralNet implementation not initialized.\""
- "%25s:%-5d EXCEPTION (%d): \"NeuralNet output size (%u) is not matching the number of FFT bins (%u).\""
- "%25s:%-5d EXCEPTION (%d): \"NeuralNetBNNS: Layer (%u), bias size (%lu) is not matching the weight output vector size (%lu).\""
- "%25s:%-5d EXCEPTION (%d): \"NeuralNetBNNS: Layer (%u), filter not created.\""
- "%25s:%-5d EXCEPTION (%d): \"NeuralNetBNNS: Layer (%u), number of weights (%lu) is not matching the required number of weights (%lu).\""
- "%25s:%-5d EXCEPTION (%d): \"No MIL fallback option available\""
- "%25s:%-5d EXCEPTION (%d): \"NumContextFrames not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"NumInputChannels not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"Number of weights in Data (%lu) does not match the required number of weights (%lu).\""
- "%25s:%-5d EXCEPTION (%d): \"SampleRate not loaded\""
- "%25s:%-5d EXCEPTION (%d): \"StreamingMode (%u) is out of range, a value smaller than (%d) is expected.\""
- "%25s:%-5d EXCEPTION (%d): \"Unable to load BNNS Context\""
- "%25s:%-5d EXCEPTION (%d): \"WaitFrames not loaded.\""
- "%25s:%-5d EXCEPTION (%d): \"mInputSize is wrong.\""
- "%25s:%-5d EXCEPTION (%d): \"mInputSize of NeuralNet (%u) is not matching the feature vector size (%u).\""
- "%25s:%-5d EXCEPTION (%d): \"unable to compile program %s\""
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/AUSpatialCapture/SCTwoInputMixer.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/AUSpatialCapture/SpatialCapture.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassKoenig/dsp/DspLibBassKoenig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibBassQueen.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BassQueen/dsp/DspLibMitigationAdaptation.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquad.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquad.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Biquad/dsp/DspLibBiquadDesigns.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/BuzzKill/dsp/DspLibBuzzKill.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ControlFreak/dsp/DspLibControlFreak.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FFT/dsp/DspLibFFT.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/FourBandRandomOrderLrFilterBank/dsp/DspLibFourBandRandomOrderLrFilterBank.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/HilbertTransform/dsp/DspLibHilbertTransform.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessMeter/dsp/DspLibLoudnessMeter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudnessNormalizer/dsp/DspLibLoudnessNormalizer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceMeasurement.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ImpedanceModels.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1ModelFit.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1PilotTone.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/LoudspeakerSystemIDV1/dsp/DspLibLoudspeakerSystemIDV1TestToneGenerator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV1/PowerGuard/dsp/DspLibPowerGuardClasses.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceMeasurement.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerManagerV2/LoudspeakerSystemIDV2/dsp/DspLibLoudspeakerSystemIDV2ImpedanceModels.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LoudspeakerModel/dsp/DspLibLoudspeakerModelParameters.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/LowFlow/dsp/DspLibLowFlowAnalysisPath.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueck.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MeisterStueck/dsp/DspLibMeisterStueckKernel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/MozartCompressor/dsp/DspLibMozartCompressor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuard.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/PeakPowerGuard/dsp/DspLibPeakPowerGuardAdmittanceFilterCoeffSet.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/RMS/dsp/DspLibRMS.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/SampleRateConverter/dsp/DspLibSampleRateConverter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/ThermalSpeakerProtection/dsp/DspLibThermalSpeakerProtection.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/Utilities/DspLibBase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/VirtualBass/dsp/DspLibVirtualBass.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_FIRMatrix.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jS3z6s/Sources/AudioDSP/Source/AudioDSP/InternalAudioUnits/Effects/DspLib/XTC/dsp/DspLibXTC_HRIRdatabase.cpp"
- "06:38:15"
- "06:38:19"
- "06:38:39"
- "06:38:42"
- "06:38:49"
- "06:44:10"
- "06:44:16"
- "06:44:30"
- "Jun 17 2026"
```
