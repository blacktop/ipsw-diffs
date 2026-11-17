## EmbeddedAcousticRecognition

> `/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition`

```diff

-3610.5.1.0.0
-  __TEXT.__text: 0xb6b00c
-  __TEXT.__objc_methlist: 0x6f14
+3610.7.2.0.0
+  __TEXT.__text: 0xb6baac
+  __TEXT.__objc_methlist: 0x6f44
   __TEXT.__const: 0x5efc8
-  __TEXT.__gcc_except_tab: 0xc3510
+  __TEXT.__gcc_except_tab: 0xc3568
   __TEXT.__cstring: 0x805b9
-  __TEXT.__oslogstring: 0x3b6d
+  __TEXT.__oslogstring: 0x3c3d
   __TEXT.__ustring: 0xa8
   __TEXT.__dlopen_cstrs: 0xc8
   __TEXT.__constg_swiftt: 0x13c

   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift_as_cont: 0x6c
   __TEXT.__swift5_capture: 0x154
-  __TEXT.__unwind_info: 0x3f860
+  __TEXT.__unwind_info: 0x3f898
   __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x3888
+  __DATA_CONST.__objc_selrefs: 0x38a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x408
   __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__got: 0x818
   __AUTH_CONST.__const: 0x4b170
   __AUTH_CONST.__cfstring: 0x3820
-  __AUTH_CONST.__objc_const: 0xecd0
+  __AUTH_CONST.__objc_const: 0xed70
   __AUTH_CONST.__weak_auth_got: 0x60
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_got: 0x2298
   __AUTH.__thread_vars: 0x378
   __AUTH.__thread_bss: 0xae8
-  __DATA.__objc_ivar: 0xa7c
+  __DATA.__objc_ivar: 0xa8c
   __DATA.__data: 0xf90
   __DATA.__common: 0x17d
   __DATA_DIRTY.__objc_data: 0x3800

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 40497
-  Symbols:   60773
-  CStrings:  20143
+  Functions: 40508
+  Symbols:   60789
+  CStrings:  20146
 
Symbols:
+ -[EARCaesuraSilencePosteriorGenerator _applyQuietMode]
+ -[EARCaesuraSilencePosteriorGenerator initWithConfigFile:samplingRate:queue:quietRowsPerCompute:quietResumeAfterSilenceMs:]
+ -[EARCaesuraSilencePosteriorGenerator quietResumeAfterSilenceMs]
+ -[EARCaesuraSilencePosteriorGenerator quietRowsPerCompute]
+ _OBJC_IVAR_$_EARCaesuraSilencePosteriorGenerator._quietResumeAfterSilenceMs
+ _OBJC_IVAR_$_EARCaesuraSilencePosteriorGenerator._quietRowsPerCompute
+ _OBJC_IVAR_$_EARCaesuraSilencePosteriorGenerator._requestedQuietResumeMs
+ _OBJC_IVAR_$_EARCaesuraSilencePosteriorGenerator._requestedQuietRows
+ __ZN5kaldi22OnlineNnetForwardInput16IsRowIndependentERKNS_5nnet14NnetE
+ __ZN5kaldi22OnlineNnetForwardInput18SetStrictBatchSizeEi
+ __ZN6quasar25SilencePosteriorGenerator17setRowsPerComputeEi
+ __ZN6quasar25SilencePosteriorGenerator18enableFrameByFrameEv
+ __ZNK5kaldi22OnlineNnetForwardInput29SupportsStrictBatchSizeChangeEv
+ __ZNK6quasar25SilencePosteriorGenerator15numBufferedRowsEv
+ __ZNK6quasar25SilencePosteriorGenerator22supportsRowsPerComputeEv
+ __ZNSt3__120dynamic_pointer_castB9foe220106IN5kaldi5nnet117Nnet1InferenceNetENS1_17FeedForwardNetItfEEENS_10shared_ptrIT_EERKNS5_IT0_EE
+ ___block_descriptor_68_ea8_32w40c62_ZTSNSt3__110shared_ptrIN6quasar25SilencePosteriorGeneratorEEE_e5_v8?0l
- ___block_descriptor_56_ea8_32w40c62_ZTSNSt3__110shared_ptrIN6quasar25SilencePosteriorGeneratorEEE_e5_v8?0l
CStrings:
+ "EARSPG: quiet mode on rows=%lu resumeAfterSilenceMs=%lu"
+ "EARSPG: quiet mode summary rows=%d frames=%llu quietFrames=%llu nnetCalls=%llu toActive=%llu toQuiet=%llu"
+ "EARSPG: quiet mode unavailable for %{public}@"
```
