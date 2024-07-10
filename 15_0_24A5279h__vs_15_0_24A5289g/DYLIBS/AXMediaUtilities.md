## AXMediaUtilities

> `/System/Library/PrivateFrameworks/AXMediaUtilities.framework/Versions/A/AXMediaUtilities`

```diff

-143.0.0.0.0
-  __TEXT.__text: 0xb803c
-  __TEXT.__auth_stubs: 0x1a60
-  __TEXT.__objc_methlist: 0x9d90
+144.0.0.0.0
+  __TEXT.__text: 0xb9048
+  __TEXT.__auth_stubs: 0x1a70
+  __TEXT.__objc_methlist: 0x9e20
   __TEXT.__const: 0x160e
-  __TEXT.__cstring: 0x94fc
-  __TEXT.__oslogstring: 0x35e1
-  __TEXT.__gcc_except_tab: 0x46ac
+  __TEXT.__cstring: 0x946c
+  __TEXT.__oslogstring: 0x36bc
+  __TEXT.__gcc_except_tab: 0x48ac
   __TEXT.__dlopen_cstrs: 0x7d0
   __TEXT.__ustring: 0x422
   __TEXT.__swift5_typeref: 0x2f8

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x8c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__unwind_info: 0x3178
+  __TEXT.__unwind_info: 0x3218
   __TEXT.__eh_frame: 0x470
-  __TEXT.__objc_classname: 0x1263
-  __TEXT.__objc_methname: 0x18c93
-  __TEXT.__objc_methtype: 0x393e
-  __TEXT.__objc_stubs: 0x10660
-  __DATA_CONST.__got: 0xbe0
+  __TEXT.__objc_classname: 0x1264
+  __TEXT.__objc_methname: 0x18e73
+  __TEXT.__objc_methtype: 0x3932
+  __TEXT.__objc_stubs: 0x10760
+  __DATA_CONST.__got: 0xbd0
   __DATA_CONST.__const: 0x1348
   __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5650
+  __DATA_CONST.__objc_selrefs: 0x5688
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x6b8
-  __AUTH_CONST.__auth_got: 0xd48
+  __AUTH_CONST.__auth_got: 0xd50
   __AUTH_CONST.__auth_ptr: 0x1a0
-  __AUTH_CONST.__const: 0x2b78
-  __AUTH_CONST.__cfstring: 0xb900
-  __AUTH_CONST.__objc_const: 0x12c08
+  __AUTH_CONST.__const: 0x2ba8
+  __AUTH_CONST.__cfstring: 0xb8e0
+  __AUTH_CONST.__objc_const: 0x12d18
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_doubleobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x3bd0
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0xcfc
+  __DATA.__objc_ivar: 0xd18
   __DATA.__data: 0xd50
   __DATA.__bss: 0x1af0
   __DATA.__common: 0x80

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4578
-  Symbols:   10629
-  CStrings:  1857
+  Functions: 4596
+  Symbols:   10674
+  CStrings:  1856
 
Symbols:
+ -[AXMDataSonifier _centsForFrequency:]
+ -[AXMDataSonifier _initializeAudioPlayerNode]
+ -[AXMDataSonifier _initializePitchShifter]
+ -[AXMDataSonifier _keyPitchesForContinuousSeries:]
+ -[AXMDataSonifier _normalizedKeyPitchForFrequency:]
+ -[AXMDataSonifier _setupContinuousAudioChain]
+ -[AXMDataSonifier _setupDiscreteAudioChain]
+ -[AXMDataSonifier beginUpdatingPitch]
+ -[AXMDataSonifier currentContinuousPlaybackPosition]
+ -[AXMDataSonifier currentDiscretePlaybackPosition]
+ -[AXMDataSonifier currentPlaybackTime]
+ -[AXMDataSonifier keyPitchForTime:]
+ -[AXMDataSonifier keyPitchUpdateTimer]
+ -[AXMDataSonifier keyPitches]
+ -[AXMDataSonifier pitchShifter]
+ -[AXMDataSonifier playAudioPlayer]
+ -[AXMDataSonifier playFrequencyAtTime:]
+ -[AXMDataSonifier player]
+ -[AXMDataSonifier setContinuousPlaybackPosition:]
+ -[AXMDataSonifier setCurrentPlaybackTime:]
+ -[AXMDataSonifier setDiscretePlaybackPosition:]
+ -[AXMDataSonifier setKeyPitchUpdateTimer:]
+ -[AXMDataSonifier setKeyPitches:]
+ -[AXMDataSonifier setPitchShifter:]
+ -[AXMDataSonifier setPlayer:]
+ -[AXMDataSonifier shouldIncrementToPitch:by:]
+ GCC_except_table100
+ GCC_except_table101
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table94
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table97
+ OBJC_IVAR_$_AXMDataSonifier._currentPlaybackTime
+ OBJC_IVAR_$_AXMDataSonifier._keyPitchUpdateTimer
+ OBJC_IVAR_$_AXMDataSonifier._keyPitches
+ OBJC_IVAR_$_AXMDataSonifier._pitchShifter
+ OBJC_IVAR_$_AXMDataSonifier._player
+ OBJC_IVAR_$_AXMDataSonifier.audiographPlaybackDuration
+ OBJC_IVAR_$_AXMDataSonifier.buffer
+ OBJC_IVAR_$_AXMDataSonifier.maxFrequency
+ OBJC_IVAR_$_AXMDataSonifier.minFrequency
+ _CACurrentMediaTime
+ _OBJC_EHTYPE_$_NSException
+ __23-[AXMDataSonifier play]_block_invoke.154
+ __31-[AXMDataSonifier endScrubbing]_block_invoke.170
+ ___37-[AXMDataSonifier beginUpdatingPitch]_block_invoke
+ ___47-[AXMDataSonifier setDiscretePlaybackPosition:]_block_invoke
+ ___49-[AXMDataSonifier setContinuousPlaybackPosition:]_block_invoke
+ ___block_descriptor_72_ea8_32r40r48r56w_e17_v16?0"NSTimer"8l
+ ___copy_helper_block_ea8_32r40r48r56w
+ ___destroy_helper_block_ea8_32r40r48r56w
+ _objc_msgSend$_centsForFrequency:
+ _objc_msgSend$_initializeAudioPlayerNode
+ _objc_msgSend$_initializePitchShifter
+ _objc_msgSend$_keyPitchesForContinuousSeries:
+ _objc_msgSend$_normalizedKeyPitchForFrequency:
+ _objc_msgSend$_setupContinuousAudioChain
+ _objc_msgSend$_setupDiscreteAudioChain
+ _objc_msgSend$beginUpdatingPitch
+ _objc_msgSend$currentContinuousPlaybackPosition
+ _objc_msgSend$currentDiscretePlaybackPosition
+ _objc_msgSend$currentPlaybackTime
+ _objc_msgSend$keyPitchForTime:
+ _objc_msgSend$keyPitchUpdateTimer
+ _objc_msgSend$pitchShifter
+ _objc_msgSend$playAudioPlayer
+ _objc_msgSend$playFrequencyAtTime:
+ _objc_msgSend$setContinuousPlaybackPosition:
+ _objc_msgSend$setCurrentPlaybackTime:
+ _objc_msgSend$setDiscretePlaybackPosition:
+ _objc_msgSend$setOverlap:
+ _objc_msgSend$setVolume:
+ _objc_msgSend$shouldIncrementToPitch:by:
- -[AXMDataSonifier _initializeAudioUnits]
- -[AXMDataSonifier _initializeEcho]
- -[AXMDataSonifier _initializeReverb]
- -[AXMDataSonifier _renderContinuousAudioForSeries:]
- -[AXMDataSonifier echoMix]
- -[AXMDataSonifier echo]
- -[AXMDataSonifier isReverbBypassed]
- -[AXMDataSonifier reverbMix]
- -[AXMDataSonifier reverb]
- -[AXMDataSonifier setEcho:]
- -[AXMDataSonifier setEchoMix:]
- -[AXMDataSonifier setReverb:]
- -[AXMDataSonifier setReverbMix:]
- -[AXMDataSonifier updateReverbPreset:]
- GCC_except_table34
- GCC_except_table36
- GCC_except_table37
- GCC_except_table39
- GCC_except_table41
- GCC_except_table47
- GCC_except_table49
- GCC_except_table51
- GCC_except_table55
- GCC_except_table77
- GCC_except_table78
- GCC_except_table83
- GCC_except_table84
- GCC_except_table86
- GCC_except_table90
- OBJC_IVAR_$_AXMDataSonifier._echo
- OBJC_IVAR_$_AXMDataSonifier._reverb
- _OBJC_CLASS_$_AVAudioUnitDistortion
- _OBJC_CLASS_$_AVAudioUnitReverb
- __23-[AXMDataSonifier play]_block_invoke.157
- __31-[AXMDataSonifier endScrubbing]_block_invoke.176
- ___39-[AXMDataSonifier setPlaybackPosition:]_block_invoke
- _objc_msgSend$_initializeAudioUnits
- _objc_msgSend$_initializeCompressor
- _objc_msgSend$_initializeEcho
- _objc_msgSend$_initializeLowpassFilter
- _objc_msgSend$_initializeReverb
- _objc_msgSend$_renderContinuousAudioForSeries:
- _objc_msgSend$bypass
- _objc_msgSend$connect:to:format:
- _objc_msgSend$engine
- _objc_msgSend$initWithSampleRate:envelope:keyPitches:
- _objc_msgSend$loadFactoryPreset:
- _objc_msgSend$outputNode
- _objc_msgSend$setWetDryMix:
- _objc_msgSend$wetDryMix
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AccessibilityMediaUtilities/AXMediaUtilities/source/ImageTools.m"
+ "bassTone"
+ "wav"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AccessibilityMediaUtilities/AXMediaUtilities/source/ImageTools.m"
- "Error stopping audio playback"
- "Error: IO audio unit is running but we aren't in a scrubbing or playback session -- investigate."
- "failed to start audio engine"

```
