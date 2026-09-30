## SpeechEngine

> `/System/Library/PrivateFrameworks/SpeechEngine.framework/Versions/A/SpeechEngine`

```diff

-3600.76.1.0.0
-  __TEXT.__text: 0x132bcc
+3600.85.2.0.0
+  __TEXT.__text: 0x136c5c
   __TEXT.__objc_methlist: 0xdc
-  __TEXT.__const: 0xe350
-  __TEXT.__cstring: 0x5521
-  __TEXT.__swift5_typeref: 0x390c
-  __TEXT.__constg_swiftt: 0x5180
-  __TEXT.__swift5_reflstr: 0x39c6
-  __TEXT.__swift5_fieldmd: 0x4768
+  __TEXT.__const: 0xe3c0
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
-  __TEXT.__swift_as_entry: 0x408
-  __TEXT.__swift_as_ret: 0x414
+  __TEXT.__swift_as_entry: 0x418
+  __TEXT.__swift_as_ret: 0x428
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__swift_as_cont: 0xba4
-  __TEXT.__swift5_capture: 0x1ab8
-  __TEXT.__oslogstring: 0x412f
-  __TEXT.__unwind_info: 0x5c18
-  __TEXT.__eh_frame: 0xe01c
+  __TEXT.__swift_as_cont: 0xc0c
+  __TEXT.__swift5_capture: 0x1a48
+  __TEXT.__oslogstring: 0x417f
+  __TEXT.__unwind_info: 0x5cc0
+  __TEXT.__eh_frame: 0xe3dc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xbec0
-  __AUTH_CONST.__objc_const: 0x5038
+  __AUTH_CONST.__const: 0xbe28
+  __AUTH_CONST.__objc_const: 0x5158
   __AUTH_CONST.__auth_got: 0x17f8
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
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9100
-  Symbols:   2456
-  CStrings:  899
+  Functions: 9143
+  Symbols:   2458
+  CStrings:  914
 
Symbols:
+ _NSUnderlyingErrorKey
+ ___swift_memcpy196_8
+ ___swift_memcpy249_8
+ ___swift_memcpy88_8
+ __swift_closure_destructor.395Tm
+ __swift_closure_destructor.44Tm
+ __swift_closure_destructor.553Tm
+ __swift_closure_destructor.98Tm
+ _symbolic SJ
+ _symbolic Say_____GSg s7Float16V
+ _symbolic ScTy__________G 12SpeechEngine0A18TokenPostProcessorC s5NeverO
+ _symbolic ScTy___________pGSg 12SpeechEngine0A22TranscriptionProcessorC s5ErrorP
+ _symbolic _____ 12SpeechEngine0A30TranscriptionProcessingOptionsV
+ _symbolic _____IeAgHr_ 12SpeechEngine0A18TokenPostProcessorC
+ _symbolic _____y__________G s17_NativeDictionaryV 12SpeechEngine12SystemConfigO20DetokenizerModelTypeO 10Foundation3URLV
- _OUTLINED_FUNCTION_373
- _OUTLINED_FUNCTION_374
- _OUTLINED_FUNCTION_375
- ___swift_memcpy185_8
- ___swift_memcpy232_8
- ___swift_memcpy96_8
- __swift_closure_destructor.385Tm
- __swift_closure_destructor.43Tm
- __swift_closure_destructor.517Tm
- __swift_closure_destructor.97Tm
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
