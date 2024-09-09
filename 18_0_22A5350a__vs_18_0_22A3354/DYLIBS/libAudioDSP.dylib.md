## libAudioDSP.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`

```diff

 747.132.30.2.0
-  __TEXT.__text: 0x726980
-  __TEXT.__auth_stubs: 0x4420
+  __TEXT.__text: 0x726b18
+  __TEXT.__auth_stubs: 0x4430
   __TEXT.__objc_methlist: 0x2e4
   __TEXT.__gcc_except_tab: 0x558d8
   __TEXT.__const: 0x7c7e0
-  __TEXT.__oslogstring: 0x3683c
-  __TEXT.__cstring: 0x6dd42
+  __TEXT.__oslogstring: 0x37484
+  __TEXT.__cstring: 0x6dd6a
   __TEXT.__dlopen_cstrs: 0x191
   __TEXT.__unwind_info: 0x1fd88
   __TEXT.__eh_frame: 0xf0

   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x3f0
-  __AUTH_CONST.__auth_got: 0x2228
+  __AUTH_CONST.__auth_got: 0x2230
   __AUTH_CONST.__auth_ptr: 0x238
   __AUTH_CONST.__const: 0x34f90
   __AUTH_CONST.__cfstring: 0x22020

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 24709
-  Symbols:   26869
-  CStrings:  16224
+  Symbols:   26870
+  CStrings:  16232
 
Symbols:
+ __os_feature_enabled_simple_impl
CStrings:
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"WaitFrames not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve threshold.\""
+ "Aug  9 2024"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"NumInputChannels not loaded.\""
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mBufferCapacity == 0 || other.mBuffers[i].mDataByteSize <= mBufferCapacity) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [outputDescDict_ref.get_cf() == nullptr is false]: \"Missing dictionary OutputVectorDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [mDNNLayer[layerIdx].mFilter == nullptr is false]: \"NeuralNetBNNS: Layer (%!u(MISSING)), filter not created.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [ioStates_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputOutputStates.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [mOutputSize != mNumFFTBins is false]: \"NeuralNet output size (%!u(MISSING)) is not matching the number of FFT bins (%!u(MISSING)).\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"MCLPOutScale not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [mGraph.data == nullptr is false]: \"unable to compile program %!s(MISSING)\""
+ "18:33:27"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!(fftSize > 1024 * 4)) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar Beta from dictionary Activation.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve sample rate.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve ECleeScale.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [modelNetPathBase_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPathBase.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing vector Data from dictionary Weights.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar DataBias from dictionary Bias.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [outputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve OutputName.\""
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!(nDftBuffers > 256)) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar DataBias from dictionary OutputVectorDescriptor.\""
+ "SpeakerPlayback"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [biasDataType_ref.get_cf() == nullptr is false]: \"Missing dictionary DataType from dictionary Weights.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"KalmanProcessStd not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [modelPlistInfo.streamingMode_int >= static_cast<UInt32>(StreamingMode::NumModes) is false]: \"StreamingMode (%!u(MISSING)) is out of range, a value smaller than (%!d(MISSING)) is expected.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"ECOutScale not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar DataBias from dictionary Weights.\""
+ "@@ Strips Aug  9 2024 18:27:08"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve BlockSize.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [outputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve OutputName from (%!s(MISSING)).\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [inState.size() != outState.size() is false]: \"Input state %!s(MISSING) size (%!z(MISSING)u) not matching the output state size %!s(MISSING) (%!z(MISSING)u).\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [outputDataType_ref.get_cf() == nullptr is false]: \"Failed to retrieve output data type (DataType) from dictionary OutputVectorDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [pNeuralNetImpl == nullptr is false]: \"NeuralNet implementation not initialized.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [inputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputName.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [modelNetExt == \".ir\" is false]: \"No MIL fallback option available\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [modelNetPath_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPath.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar DataBias from dictionary InputVectorDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve InputScale.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar DataScale from dictionary Bias.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [topLevelDict_ref.get_cf() == nullptr is false]: \"Missing dictionary: %!s(MISSING)\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [inputDescDict_ref.get_cf() == nullptr is false]: \"Missing dictionary InputVectorDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [weightsDataType_ref.get_cf() == nullptr is false]: \"Missing DataType from dictionary Weights.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve HangA01.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [(mInputSize != mNumMelBands*2) is false]: \"mInputSize is wrong.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [mInputSize != featureVectorSize is false]: \"mInputSize of NeuralNet (%!u(MISSING)) is not matching the feature vector size (%!u(MISSING)).\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [weightsDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Weights.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [layerType_ref.get_cf() == nullptr is false]: \"Failed to retrieve layer type (Type) from dictionary LayerDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"LambdaPSD_TC not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar DataScale from dictionary Weights.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"BlockSize not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve ECoutScale.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve NumLayers.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [biasDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Bias from dictionary Weights.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve HangA10.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"FFT2Mel matrix not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [(mInputSize != mNumMelBands*mNumContextFrames*(1+mDeltaFeature)) is false]: \"mInputSize is wrong.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar DataScale from dictionary InputVectorDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [modelNetPathRelative_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPath.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar Alpha from dictionary Activation.\""
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!(fftSize > 2048 * 4)) != 0 is false]: "
+ "NanoMediaUI"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve WaitFrames.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve forgetting factor Lambda_TC.\""
+ "18:33:45"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [layer.mBiasVector.size() != weightsSizeOutput is false]: \"NeuralNetBNNS: Layer (%!u(MISSING)), bias size (%!l(MISSING)u) is not matching the weight output vector size (%!l(MISSING)u).\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [inputDataType_ref.get_cf() == nullptr is false]: \"Missing dictionary DataType.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [inputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputName from (%!s(MISSING)).\""
+ "/AppleInternal/Library/BuildRoots/c7268dd4-5656-11ef-b8ac-76625042721f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"KalmanObservationStd not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar Size from dictionary InputVectorDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"NumContextFrames not loaded.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [nnLayers[i].mWeightsQuantized.size() != weightsNumberOfCoefficients is false]: \"Number of weights in Data (%!l(MISSING)u) does not match the required number of weights (%!l(MISSING)u).\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [!validContext is false]: \"Unable to load BNNS Context\""
+ "/AppleInternal/Library/BuildRoots/c7268dd4-5656-11ef-b8ac-76625042721f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Failed to retrieve NumContextFrames.\""
+ "18:33:32"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [numStates_ref.get_cf() == nullptr is false]: \"Failed to retrieve NumStates from InputOutputStates.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar Size from dictionary OutputVectorDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"SampleRate not loaded\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [activationFunction_ref.get_cf() == nullptr is false]: \"Failed to retrieve activation function (Function) from dictionary Activation.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing scalar DataScale from dictionary OutputVectorDescriptor.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [layer.mWeightsQuantized.size() != weightsNumberOfCoefficients is false]: \"NeuralNetBNNS: Layer (%!u(MISSING)), number of weights (%!l(MISSING)u) is not matching the required number of weights (%!l(MISSING)u).\""
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!(nDftBuffers > 64)) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [err != noErr is false]: \"Missing vector Data from dictionary Bias.\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [state_ref.get_cf() == nullptr is false]: \"Missing dictionary (%!s(MISSING)).\""
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [activationDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Activation.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"LambdaPSD_TC not loaded.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve NumStates from InputOutputStates.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve threshold.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary DataType.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve NumContextFrames.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing vector Data from dictionary Weights.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar Alpha from dictionary Activation.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary (%!s(MISSING)).\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"NeuralNetBNNS: Layer (%!u(MISSING)), number of weights (%!l(MISSING)u) is not matching the required number of weights (%!l(MISSING)u).\""
- "Aug 12 2024"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar DataBias from dictionary Bias.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Number of weights in Data (%!l(MISSING)u) does not match the required number of weights (%!l(MISSING)u).\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve layer type (Type) from dictionary LayerDescriptor.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar DataScale from dictionary Weights.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary InputVectorDescriptor.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve OutputName from (%!s(MISSING)).\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve sample rate.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve WaitFrames.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar Size from dictionary OutputVectorDescriptor.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"No MIL fallback option available\""
- "15:28:19"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve InputName.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Unable to load BNNS Context\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve output data type (DataType) from dictionary OutputVectorDescriptor.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar DataBias from dictionary Weights.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"NeuralNet implementation not initialized.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve HangA10.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"MCLPOutScale not loaded.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Input state %!s(MISSING) size (%!z(MISSING)u) not matching the output state size %!s(MISSING) (%!z(MISSING)u).\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary DataType from dictionary Weights.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve activation function (Function) from dictionary Activation.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve InputOutputStates.\""
- "15:27:59"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve ModelNetPathBase.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"mInputSize is wrong.\""
- "/AppleInternal/Library/BuildRoots/f9f3b3b3-56f5-11ef-ab75-8ece77934383/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"StreamingMode (%!u(MISSING)) is out of range, a value smaller than (%!d(MISSING)) is expected.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"unable to compile program %!s(MISSING)\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar DataBias from dictionary InputVectorDescriptor.\""
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE: "
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"WaitFrames not loaded.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"ECOutScale not loaded.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"BlockSize not loaded.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve ECleeScale.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"NeuralNetBNNS: Layer (%!u(MISSING)), bias size (%!l(MISSING)u) is not matching the weight output vector size (%!l(MISSING)u).\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing DataType from dictionary Weights.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary OutputVectorDescriptor.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve NumLayers.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar DataBias from dictionary OutputVectorDescriptor.\""
- "@@ Strips Aug 12 2024 15:20:57"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar DataScale from dictionary InputVectorDescriptor.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"KalmanProcessStd not loaded.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve InputScale.\""
- "/AppleInternal/Library/BuildRoots/f9f3b3b3-56f5-11ef-ab75-8ece77934383/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"FFT2Mel matrix not loaded.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary Activation.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"NumContextFrames not loaded.\""
- "15:28:05"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"NeuralNet output size (%!u(MISSING)) is not matching the number of FFT bins (%!u(MISSING)).\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar Beta from dictionary Activation.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary: %!s(MISSING)\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"SampleRate not loaded\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"mInputSize of NeuralNet (%!u(MISSING)) is not matching the feature vector size (%!u(MISSING)).\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve forgetting factor Lambda_TC.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve HangA01.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"NeuralNetBNNS: Layer (%!u(MISSING)), filter not created.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary Bias from dictionary Weights.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar Size from dictionary InputVectorDescriptor.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve BlockSize.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve ModelNetPath.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing dictionary Weights.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar DataScale from dictionary Bias.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"NumInputChannels not loaded.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing vector Data from dictionary Bias.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve InputName from (%!s(MISSING)).\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Missing scalar DataScale from dictionary OutputVectorDescriptor.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve ECoutScale.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"Failed to retrieve OutputName.\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"KalmanObservationStd not loaded.\""

```
