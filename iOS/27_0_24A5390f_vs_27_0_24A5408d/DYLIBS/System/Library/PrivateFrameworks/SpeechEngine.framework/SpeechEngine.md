## SpeechEngine

> `/System/Library/PrivateFrameworks/SpeechEngine.framework/SpeechEngine`

```diff

-3600.76.1.0.0
-  __TEXT.__text: 0x12f514
+3600.85.2.0.0
+  __TEXT.__text: 0x133470
   __TEXT.__objc_methlist: 0xdc
-  __TEXT.__const: 0xe380
-  __TEXT.__cstring: 0x5521
-  __TEXT.__swift5_typeref: 0x390c
-  __TEXT.__constg_swiftt: 0x5180
-  __TEXT.__swift5_reflstr: 0x39c6
-  __TEXT.__swift5_fieldmd: 0x4768
+  __TEXT.__const: 0xe3f0
+  __TEXT.__cstring: 0x5771
+  __TEXT.__swift5_typeref: 0x3948
+  __TEXT.__constg_swiftt: 0x518c
+  __TEXT.__swift5_reflstr: 0x3b06
+  __TEXT.__swift5_fieldmd: 0x4838
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_proto: 0x9ec
   __TEXT.__swift5_types: 0x470
-  __TEXT.__swift_as_entry: 0x404
-  __TEXT.__swift_as_ret: 0x410
+  __TEXT.__swift_as_entry: 0x414
+  __TEXT.__swift_as_ret: 0x424
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__swift_as_cont: 0xb98
-  __TEXT.__swift5_capture: 0x1ab8
-  __TEXT.__oslogstring: 0x412f
-  __TEXT.__unwind_info: 0x5df8
-  __TEXT.__eh_frame: 0xdf94
+  __TEXT.__swift_as_cont: 0xc00
+  __TEXT.__swift5_capture: 0x1a48
+  __TEXT.__oslogstring: 0x417f
+  __TEXT.__unwind_info: 0x5f00
+  __TEXT.__eh_frame: 0xe394
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xbec0
-  __AUTH_CONST.__objc_const: 0x5038
-  __AUTH_CONST.__auth_got: 0x1988
+  __AUTH_CONST.__const: 0xbe28
+  __AUTH_CONST.__objc_const: 0x5158
+  __AUTH_CONST.__auth_got: 0x1990
   __AUTH.__objc_data: 0xe8
   __AUTH.__data: 0xe80
-  __DATA.__data: 0x2a68
+  __DATA.__data: 0x2968
   __DATA.__bss: 0x13630
-  __DATA.__common: 0x3e0
+  __DATA.__common: 0x400
   __DATA_DIRTY.__objc_data: 0x6e8
-  __DATA_DIRTY.__data: 0x59d0
+  __DATA_DIRTY.__data: 0x59f0
   __DATA_DIRTY.__common: 0x198
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9065
-  Symbols:   2500
-  CStrings:  899
+  Functions: 9128
+  Symbols:   2498
+  CStrings:  914
 
Symbols:
+ _NSUnderlyingErrorKey
+ ___swift_closure_destructor.395Tm
+ ___swift_closure_destructor.44Tm
+ ___swift_closure_destructor.553Tm
+ ___swift_closure_destructor.98Tm
+ ___swift_memcpy196_8
+ ___swift_memcpy249_8
+ ___swift_memcpy88_8
+ _swift_release_x6
+ _symbolic SJ
+ _symbolic Say_____GSg s7Float16V
+ _symbolic ScTy__________G 12SpeechEngine0A18TokenPostProcessorC s5NeverO
+ _symbolic ScTy___________pGSg 12SpeechEngine0A22TranscriptionProcessorC s5ErrorP
+ _symbolic _____ 12SpeechEngine0A30TranscriptionProcessingOptionsV
+ _symbolic _____IeAgHr_ 12SpeechEngine0A18TokenPostProcessorC
+ _symbolic _____y__________G s17_NativeDictionaryV 12SpeechEngine12SystemConfigO20DetokenizerModelTypeO 10Foundation3URLV
- _OUTLINED_FUNCTION_369
- _OUTLINED_FUNCTION_370
- _OUTLINED_FUNCTION_371
- _OUTLINED_FUNCTION_372
- _OUTLINED_FUNCTION_373
- _OUTLINED_FUNCTION_374
- _OUTLINED_FUNCTION_375
- _OUTLINED_FUNCTION_376
- ___swift_closure_destructor.385Tm
- ___swift_closure_destructor.43Tm
- ___swift_closure_destructor.517Tm
- ___swift_closure_destructor.97Tm
- ___swift_memcpy185_8
- ___swift_memcpy232_8
- ___swift_memcpy96_8
- _symbolic _____Sg 12SpeechEngine0A22TranscriptionProcessorC
- _symbolic _____Sgz_Xx 12SpeechEngine0A22TranscriptionProcessorC
- _symbolic _____ySSG s10ArraySliceV
CStrings:
+ " ms  [accumulated retriever inference time]"
+ " ms  [max single Retriever.run]"
+ " ms  [retrieverTime / callCount]"
+ "%s: finish: adding %ld padding elements to %ld written elements to reach multiple of %ld elements"
+ "%s: finish: total written elements %ld"
+ "Final shortlist: %{sensitive}s, size: %{public}ld, retrievalCallCount: %{public}ld, accumulatedRetrieverMs: %{public}f"
+ "Model does not expect %s; skipping Gumbel noise preparation."
+ "Model expects gumbel_noise but gumbelFile is not configured"
+ "Model expects gumbel_noise but gumbelNoiseValues is nil"
+ "Retriever avg/call: "
+ "Retriever peak/call:"
+ "Retriever time:     "
+ "Tokenizer reset triggered at %ld ms"
+ "accumulated retriever inference time (Retriever.run)"
+ "aggregatedRetrievalLatencyMs"
+ "max duration of a single Retriever.run call"
+ "retrieverAvgCallMs"
+ "retrieverPeakCallMs"
+ "retrieverTime / retriever call count"
+ "retrieverTimeMs"
+ "retrieverValidInputCount"
+ "writePaddingChunkSize requires paddingProvider"
- " tokens at a time."
- "AudioTokenizer: endAudio: Adding %ld padding samples to %ld received samples to reach multiple of %ld samples"
- "Final shortlist: %{sensitive}s, size: %{public}ld"
- "Remove unrecognized command: %{private}s"
- "Tokenizer silence reset triggered at %ld ms"
- "Tokenizer time reset triggered at %ld ms"
- "Transcribe only the words heard in the audio. The audio might include the words"
```
