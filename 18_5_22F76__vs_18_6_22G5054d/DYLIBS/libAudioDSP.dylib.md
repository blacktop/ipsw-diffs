## libAudioDSP.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`

```diff

-747.607.0.0.0
+747.701.0.0.0
   __TEXT.__text: 0x73f0b0
   __TEXT.__auth_stubs: 0x47c0
   __TEXT.__objc_methlist: 0x564
-  __TEXT.__const: 0x7d830
-  __TEXT.__cstring: 0x6e77a
+  __TEXT.__const: 0x7d8c0
+  __TEXT.__cstring: 0x6e83a
   __TEXT.__dlopen_cstrs: 0xf3
   __TEXT.__gcc_except_tab: 0x57af0
-  __TEXT.__oslogstring: 0x38324
+  __TEXT.__oslogstring: 0x376dc
   __TEXT.__swift5_typeref: 0xd9
   __TEXT.__swift5_capture: 0xd4
   __TEXT.__constg_swiftt: 0xc4

   __AUTH.__objc_data: 0x388
   __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x33b8
+  __DATA.__data: 0x3328
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x2a08
   __DATA.__common: 0x154

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 451027CF-1226-3454-A8A7-4DAC25C70923
+  UUID: 55980B17-DAE1-3AC3-948F-54478469F71E
   Functions: 24671
   Symbols:   64798
-  CStrings:  20761
+  CStrings:  20755
 
CStrings:
+ "%25s:%-5d ASSERTION FAILURE: "
+ "%25s:%-5d EXCEPTION (%d): \"BlockSize not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"ECOutScale not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"FFT2Mel matrix not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve BlockSize.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve ECleeScale.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve ECoutScale.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve HangA01.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve HangA10.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve InputName from (%s).\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve InputName.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve InputOutputStates.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve InputScale.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve ModelNetPath.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve ModelNetPathBase.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve NumContextFrames.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve NumLayers.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve NumStates from InputOutputStates.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve OutputName from (%s).\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve OutputName.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve WaitFrames.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve activation function (Function) from dictionary Activation.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve forgetting factor Lambda_TC.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve layer type (Type) from dictionary LayerDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve output data type (DataType) from dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve sample rate.\""
+ "%25s:%-5d EXCEPTION (%d): \"Failed to retrieve threshold.\""
+ "%25s:%-5d EXCEPTION (%d): \"Input state %s size (%zu) not matching the output state size %s (%zu).\""
+ "%25s:%-5d EXCEPTION (%d): \"KalmanObservationStd not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"KalmanProcessStd not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"LambdaPSD_TC not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"MCLPOutScale not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing DataType from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary (%s).\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary Activation.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary Bias from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary DataType from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary DataType.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary InputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing dictionary: %s\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar Alpha from dictionary Activation.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar Beta from dictionary Activation.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataBias from dictionary Bias.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataBias from dictionary InputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataBias from dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataBias from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataScale from dictionary Bias.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataScale from dictionary InputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataScale from dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar DataScale from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar Size from dictionary InputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing scalar Size from dictionary OutputVectorDescriptor.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing vector Data from dictionary Bias.\""
+ "%25s:%-5d EXCEPTION (%d): \"Missing vector Data from dictionary Weights.\""
+ "%25s:%-5d EXCEPTION (%d): \"NeuralNet implementation not initialized.\""
+ "%25s:%-5d EXCEPTION (%d): \"NeuralNet output size (%u) is not matching the number of FFT bins (%u).\""
+ "%25s:%-5d EXCEPTION (%d): \"NeuralNetBNNS: Layer (%u), bias size (%lu) is not matching the weight output vector size (%lu).\""
+ "%25s:%-5d EXCEPTION (%d): \"NeuralNetBNNS: Layer (%u), filter not created.\""
+ "%25s:%-5d EXCEPTION (%d): \"NeuralNetBNNS: Layer (%u), number of weights (%lu) is not matching the required number of weights (%lu).\""
+ "%25s:%-5d EXCEPTION (%d): \"No MIL fallback option available\""
+ "%25s:%-5d EXCEPTION (%d): \"NumContextFrames not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"NumInputChannels not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"Number of weights in Data (%lu) does not match the required number of weights (%lu).\""
+ "%25s:%-5d EXCEPTION (%d): \"SampleRate not loaded\""
+ "%25s:%-5d EXCEPTION (%d): \"StreamingMode (%u) is out of range, a value smaller than (%d) is expected.\""
+ "%25s:%-5d EXCEPTION (%d): \"Unable to load BNNS Context\""
+ "%25s:%-5d EXCEPTION (%d): \"WaitFrames not loaded.\""
+ "%25s:%-5d EXCEPTION (%d): \"mInputSize is wrong.\""
+ "%25s:%-5d EXCEPTION (%d): \"mInputSize of NeuralNet (%u) is not matching the feature vector size (%u).\""
+ "%25s:%-5d EXCEPTION (%d): \"unable to compile program %s\""
+ "/AppleInternal/Library/BuildRoots/4~B2QuugAHRlH0yzpSLI74luF2lEKsm7sZPfSZQfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "/AppleInternal/Library/BuildRoots/4~B2QuugAHRlH0yzpSLI74luF2lEKsm7sZPfSZQfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "09:06:01"
+ "09:06:07"
+ "09:06:25"
+ "@@ Strips Jun  3 2025 08:53:23"
+ "Jun  3 2025"
- "%25s:%-5d ASSERTION FAILURE [(!(fftSize > 1024 * 4)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!(fftSize > 2048 * 4)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!(nDftBuffers > 256)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!(nDftBuffers > 64)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mBufferCapacity == 0 || other.mBuffers[i].mDataByteSize <= mBufferCapacity) != 0 is false]: "
- "%25s:%-5d EXCEPTION (%d) [!validContext is false]: \"Unable to load BNNS Context\""
- "%25s:%-5d EXCEPTION (%d) [(mInputSize != mNumMelBands*2) is false]: \"mInputSize is wrong.\""
- "%25s:%-5d EXCEPTION (%d) [(mInputSize != mNumMelBands*mNumContextFrames*(1+mDeltaFeature)) is false]: \"mInputSize is wrong.\""
- "%25s:%-5d EXCEPTION (%d) [activationDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Activation.\""
- "%25s:%-5d EXCEPTION (%d) [activationFunction_ref.get_cf() == nullptr is false]: \"Failed to retrieve activation function (Function) from dictionary Activation.\""
- "%25s:%-5d EXCEPTION (%d) [biasDataType_ref.get_cf() == nullptr is false]: \"Missing dictionary DataType from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d) [biasDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Bias from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"BlockSize not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"ECOutScale not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"FFT2Mel matrix not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve BlockSize.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve ECleeScale.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve ECoutScale.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve HangA01.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve HangA10.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve InputScale.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve NumContextFrames.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve NumLayers.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve WaitFrames.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve forgetting factor Lambda_TC.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve sample rate.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve threshold.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"KalmanObservationStd not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"KalmanProcessStd not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"LambdaPSD_TC not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"MCLPOutScale not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Alpha from dictionary Activation.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Beta from dictionary Activation.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary Bias.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary InputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary Bias.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary InputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Size from dictionary InputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Size from dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing vector Data from dictionary Bias.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing vector Data from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"NumContextFrames not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"NumInputChannels not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"SampleRate not loaded\""
- "%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"WaitFrames not loaded.\""
- "%25s:%-5d EXCEPTION (%d) [inState.size() != outState.size() is false]: \"Input state %s size (%zu) not matching the output state size %s (%zu).\""
- "%25s:%-5d EXCEPTION (%d) [inputDataType_ref.get_cf() == nullptr is false]: \"Missing dictionary DataType.\""
- "%25s:%-5d EXCEPTION (%d) [inputDescDict_ref.get_cf() == nullptr is false]: \"Missing dictionary InputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [inputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputName from (%s).\""
- "%25s:%-5d EXCEPTION (%d) [inputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputName.\""
- "%25s:%-5d EXCEPTION (%d) [ioStates_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputOutputStates.\""
- "%25s:%-5d EXCEPTION (%d) [layer.mBiasVector.size() != weightsSizeOutput is false]: \"NeuralNetBNNS: Layer (%u), bias size (%lu) is not matching the weight output vector size (%lu).\""
- "%25s:%-5d EXCEPTION (%d) [layer.mWeightsQuantized.size() != weightsNumberOfCoefficients is false]: \"NeuralNetBNNS: Layer (%u), number of weights (%lu) is not matching the required number of weights (%lu).\""
- "%25s:%-5d EXCEPTION (%d) [layerType_ref.get_cf() == nullptr is false]: \"Failed to retrieve layer type (Type) from dictionary LayerDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [mDNNLayer[layerIdx].mFilter == nullptr is false]: \"NeuralNetBNNS: Layer (%u), filter not created.\""
- "%25s:%-5d EXCEPTION (%d) [mGraph.data == nullptr is false]: \"unable to compile program %s\""
- "%25s:%-5d EXCEPTION (%d) [mInputSize != featureVectorSize is false]: \"mInputSize of NeuralNet (%u) is not matching the feature vector size (%u).\""
- "%25s:%-5d EXCEPTION (%d) [mOutputSize != mNumFFTBins is false]: \"NeuralNet output size (%u) is not matching the number of FFT bins (%u).\""
- "%25s:%-5d EXCEPTION (%d) [modelNetExt == \".ir\" is false]: \"No MIL fallback option available\""
- "%25s:%-5d EXCEPTION (%d) [modelNetPathBase_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPathBase.\""
- "%25s:%-5d EXCEPTION (%d) [modelNetPathRelative_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPath.\""
- "%25s:%-5d EXCEPTION (%d) [modelNetPath_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPath.\""
- "%25s:%-5d EXCEPTION (%d) [modelPlistInfo.streamingMode_int >= static_cast<UInt32>(StreamingMode::NumModes) is false]: \"StreamingMode (%u) is out of range, a value smaller than (%d) is expected.\""
- "%25s:%-5d EXCEPTION (%d) [nnLayers[i].mWeightsQuantized.size() != weightsNumberOfCoefficients is false]: \"Number of weights in Data (%lu) does not match the required number of weights (%lu).\""
- "%25s:%-5d EXCEPTION (%d) [numStates_ref.get_cf() == nullptr is false]: \"Failed to retrieve NumStates from InputOutputStates.\""
- "%25s:%-5d EXCEPTION (%d) [outputDataType_ref.get_cf() == nullptr is false]: \"Failed to retrieve output data type (DataType) from dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [outputDescDict_ref.get_cf() == nullptr is false]: \"Missing dictionary OutputVectorDescriptor.\""
- "%25s:%-5d EXCEPTION (%d) [outputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve OutputName from (%s).\""
- "%25s:%-5d EXCEPTION (%d) [outputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve OutputName.\""
- "%25s:%-5d EXCEPTION (%d) [pNeuralNetImpl == nullptr is false]: \"NeuralNet implementation not initialized.\""
- "%25s:%-5d EXCEPTION (%d) [state_ref.get_cf() == nullptr is false]: \"Missing dictionary (%s).\""
- "%25s:%-5d EXCEPTION (%d) [topLevelDict_ref.get_cf() == nullptr is false]: \"Missing dictionary: %s\""
- "%25s:%-5d EXCEPTION (%d) [weightsDataType_ref.get_cf() == nullptr is false]: \"Missing DataType from dictionary Weights.\""
- "%25s:%-5d EXCEPTION (%d) [weightsDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Weights.\""
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "05:06:45"
- "05:06:50"
- "05:07:01"
- "@@ Strips Apr 19 2025 04:56:46"
- "Apr 19 2025"

```
