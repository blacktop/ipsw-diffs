## AXMediaUtilities

> `/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities`

```diff

-164.0.0.0.0
-  __TEXT.__text: 0xc7270
+165.0.0.0.0
+  __TEXT.__text: 0xc6b58
   __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__objc_methlist: 0xb4b4
-  __TEXT.__const: 0x16c2
-  __TEXT.__gcc_except_tab: 0x57dc
+  __TEXT.__objc_methlist: 0xb46c
+  __TEXT.__const: 0x16b2
+  __TEXT.__gcc_except_tab: 0x566c
   __TEXT.__cstring: 0xa6fc
-  __TEXT.__oslogstring: 0x51c3
+  __TEXT.__oslogstring: 0x5207
   __TEXT.__dlopen_cstrs: 0xc72
   __TEXT.__ustring: 0x422
   __TEXT.__swift5_typeref: 0x2f8

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x8c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__unwind_info: 0x3818
+  __TEXT.__unwind_info: 0x37f0
   __TEXT.__eh_frame: 0x3c8
   __TEXT.__objc_classname: 0x1435
-  __TEXT.__objc_methname: 0x1c482
-  __TEXT.__objc_methtype: 0x3ce6
-  __TEXT.__objc_stubs: 0x12da0
-  __DATA_CONST.__got: 0xe20
+  __TEXT.__objc_methname: 0x1c3c7
+  __TEXT.__objc_methtype: 0x3cd5
+  __TEXT.__objc_stubs: 0x12ce0
+  __DATA_CONST.__got: 0xe18
   __DATA_CONST.__const: 0x2780
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6180
+  __DATA_CONST.__objc_selrefs: 0x6140
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x6b8
   __AUTH_CONST.__auth_got: 0xf18
-  __AUTH_CONST.__const: 0x1d38
+  __AUTH_CONST.__const: 0x1d58
   __AUTH_CONST.__cfstring: 0xcc40
-  __AUTH_CONST.__objc_const: 0x14328
+  __AUTH_CONST.__objc_const: 0x142e8
   __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH_CONST.__objc_doubleobj: 0x290
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x3db0
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0xebc
+  __DATA.__objc_ivar: 0xeb8
   __DATA.__data: 0xe38
   __DATA.__bss: 0x1d30
   __DATA.__common: 0x80

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B0778A4E-5B4C-37CA-8F81-BAD850065D34
-  Functions: 5161
-  Symbols:   16979
-  CStrings:  9539
+  UUID: 15B54B82-01E0-3AC8-AD1D-961211A35295
+  Functions: 5157
+  Symbols:   16960
+  CStrings:  9527
 
Symbols:
+ -[AXMDataSonifier _centsForNormalizedFrequency:]
+ -[AXMDataSonifier _playAudioPlayer]
+ -[AXMDataSonifier _setupAudioPlayerBasedAudioChain]
+ -[AXMDataSonifier _setupFMBasedAudioChain]
+ -[AXMDataSonifier _startAudioEngineIfNeeded]
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table55
+ GCC_except_table77
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table94
+ GCC_except_table95
+ _OBJC_IVAR_$_AXMDataSonifier._fadeDuration
+ ___47-[AXMDataSonificationManager setLiveModeValue:]_block_invoke
+ ___48-[AXMDataSonificationManager endLiveModeSession]_block_invoke
+ ___50-[AXMDataSonificationManager beginLiveModeSession]_block_invoke
+ ___block_literal_global.34
+ _objc_msgSend$_centsForNormalizedFrequency:
+ _objc_msgSend$_playAudioPlayer
+ _objc_msgSend$_setupAudioPlayerBasedAudioChain
+ _objc_msgSend$_setupFMBasedAudioChain
+ _objc_msgSend$_startAudioEngineIfNeeded
- -[AXMDataSonifier _initializeCompressor]
- -[AXMDataSonifier _initializeLowpassFilter]
- -[AXMDataSonifier _setupMultiSeriesAudioChain]
- -[AXMDataSonifier _setupSingleSeriesAudioChain]
- -[AXMDataSonifier beginLiveContinuousToneSession].cold.1
- -[AXMDataSonifier compressor]
- -[AXMDataSonifier lowpassCutoff]
- -[AXMDataSonifier lowpassFilter]
- -[AXMDataSonifier playAudioPlayer]
- -[AXMDataSonifier setCompressor:]
- -[AXMDataSonifier setLowpassCutoff:]
- -[AXMDataSonifier setLowpassFilter:]
- GCC_except_table43
- GCC_except_table48
- GCC_except_table54
- GCC_except_table62
- GCC_except_table74
- GCC_except_table75
- GCC_except_table76
- GCC_except_table87
- GCC_except_table89
- GCC_except_table90
- GCC_except_table91
- GCC_except_table97
- GCC_except_table98
- _OBJC_CLASS_$_AVAudioUnitEQ
- _OBJC_IVAR_$_AXMDataSonifier._compressor
- _OBJC_IVAR_$_AXMDataSonifier._lowpassFilter
- _objc_msgSend$_initializeLiveToneDataSource
- _objc_msgSend$_setupMultiSeriesAudioChain
- _objc_msgSend$_setupSingleSeriesAudioChain
- _objc_msgSend$bands
- _objc_msgSend$code
- _objc_msgSend$initWithNumberOfBands:
- _objc_msgSend$liveContinuousDataTone
- _objc_msgSend$liveTonePlaybackCallbackRenderingContext
- _objc_msgSend$playAudioPlayer
- _objc_msgSend$setFilterType:
- _objc_msgSend$setFrequency:
CStrings:
+ "Attempted to start audio engine while engine is currently running"
+ "Attempting to play audio player while currently playing"
+ "Audio player node failed to play: %@"
+ "Failed to start audio engine: %@"
+ "_centsForNormalizedFrequency:"
+ "_fadeDuration"
+ "_playAudioPlayer"
+ "_setupAudioPlayerBasedAudioChain"
+ "_setupFMBasedAudioChain"
+ "_startAudioEngineIfNeeded"
- "@\"AVAudioUnitEQ\""
- "T@\"AVAudioUnitEQ\",&,N,V_lowpassFilter"
- "T@\"AVAudioUnitEffect\",&,N,V_compressor"
- "_compressor"
- "_initializeCompressor"
- "_initializeLowpassFilter"
- "_lowpassFilter"
- "_setupMultiSeriesAudioChain"
- "_setupSingleSeriesAudioChain"
- "audio player node failed to play"
- "bands"
- "code"
- "compressor"
- "error starting audio output: %@"
- "failed to render audio buffer"
- "failed to start audio engine"
- "initWithNumberOfBands:"
- "lowpassFilter"
- "playAudioPlayer"
- "setCompressor:"
- "setFilterType:"
- "setLowpassFilter:"

```
