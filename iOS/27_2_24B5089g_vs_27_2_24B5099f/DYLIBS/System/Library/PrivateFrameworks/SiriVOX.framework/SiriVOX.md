## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX`

```diff

-3605.17.1.0.0
-  __TEXT.__text: 0x83fac
-  __TEXT.__objc_methlist: 0x8c78
+3605.18.1.0.0
+  __TEXT.__text: 0x847ac
+  __TEXT.__objc_methlist: 0x8cb0
   __TEXT.__const: 0x124
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x11acb
+  __TEXT.__cstring: 0x11b5e
   __TEXT.__swift5_capture: 0x78
   __TEXT.__swift5_reflstr: 0x16
-  __TEXT.__gcc_except_tab: 0x5cc
-  __TEXT.__oslogstring: 0x8c2d
+  __TEXT.__gcc_except_tab: 0x5e8
+  __TEXT.__oslogstring: 0x8ec0
   __TEXT.__dlopen_cstrs: 0xda
-  __TEXT.__unwind_info: 0x2c40
+  __TEXT.__unwind_info: 0x2c50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e38
+  __DATA_CONST.__objc_selrefs: 0x3e58
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x980
   __DATA_CONST.__got: 0x798
   __AUTH_CONST.__const: 0xc08
   __AUTH_CONST.__cfstring: 0x6020
-  __AUTH_CONST.__objc_const: 0x139a0
+  __AUTH_CONST.__objc_const: 0x13a28
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__auth_got: 0x6e8
   __AUTH.__objc_data: 0x4150
   __AUTH.__data: 0x38
-  __DATA.__objc_ivar: 0xcdc
+  __DATA.__objc_ivar: 0xce8
   __DATA.__data: 0x2260
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3179
-  Symbols:   6754
-  CStrings:  2276
+  Functions: 3186
+  Symbols:   6764
+  CStrings:  2286
 
Symbols:
+ -[SVXHomePodUIBridgeClientDelegate didPauseTTSForCurrentUserTurn]
+ -[SVXHomePodUIBridgeClientDelegate setDidPauseTTSForCurrentUserTurn:]
+ -[SVXSession currentActivationContext]
+ -[SVXSession speechSynthesizerDidFailStreamWithError:taskTracker:]
+ GCC_except_table2078
+ GCC_except_table2103
+ GCC_except_table2240
+ GCC_except_table2363
+ GCC_except_table2365
+ GCC_except_table2367
+ GCC_except_table2383
+ GCC_except_table2384
+ GCC_except_table2512
+ GCC_except_table2518
+ GCC_except_table2521
+ GCC_except_table2827
+ GCC_except_table2982
+ GCC_except_table3057
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._didPauseTTSForCurrentUserTurn
+ _OBJC_IVAR_$_SVXSpeechSynthesizer._streamTaskTrackers
+ _OBJC_IVAR_$_SVXSpeechSynthesizer._streamsWithFinishedPlayback
+ ___66-[SVXSession speechSynthesizerDidFailStreamWithError:taskTracker:]_block_invoke
+ ___71-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDetectedSpeechStart:]_block_invoke
+ ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceReceivedSpeechMitigationResult:]_block_invoke
- GCC_except_table2076
- GCC_except_table2099
- GCC_except_table2236
- GCC_except_table2358
- GCC_except_table2360
- GCC_except_table2362
- GCC_except_table2378
- GCC_except_table2379
- GCC_except_table2507
- GCC_except_table2511
- GCC_except_table2513
- GCC_except_table2820
- GCC_except_table2975
- GCC_except_table3050
CStrings:
+ "#Choreography - TTS was never paused for this turn, skipping resume"
+ "#Choreography - TTS was never paused, skipping legacy resume"
+ "%s Ignored because the stream does not belong to the current request. (_currentRequestUUID = %@, streamRequestUUID = %@)"
+ "%s Ignored failure of an unregistered stream. (streamId = %@, error = %@)"
+ "%s Response stream failed; ending the abandoned request. (_currentRequestUUID = %@, error = %@)"
+ "%s Stopping TTS for the active request with no current speaking context... (ttsSession = %@, activeTTSRequest = %@)"
+ "%s Stream errored after its audio finished; reporting success. (streamId = %@, error = %@)"
+ "%s error = %@, taskTracker = %@"
+ "-[SVXSession speechSynthesizerDidFailStreamWithError:taskTracker:]"
+ "-[SVXSession speechSynthesizerDidFailStreamWithError:taskTracker:]_block_invoke"
```
