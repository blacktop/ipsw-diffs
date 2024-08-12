## feedbackd

> `/usr/libexec/feedbackd`

```diff

-124.3.0.0.0
-  __TEXT.__text: 0x63234
-  __TEXT.__auth_stubs: 0x1b60
+127.0.0.0.0
+  __TEXT.__text: 0x63c10
+  __TEXT.__auth_stubs: 0x1b70
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__const: 0x14f0
-  __TEXT.__cstring: 0x27d1
+  __TEXT.__const: 0x1500
+  __TEXT.__cstring: 0x2831
   __TEXT.__objc_methname: 0x144e
-  __TEXT.__swift5_typeref: 0xbc9
-  __TEXT.__swift5_capture: 0x4b0
+  __TEXT.__swift5_typeref: 0xc2b
+  __TEXT.__swift5_capture: 0x4c0
   __TEXT.__constg_swiftt: 0xa84
-  __TEXT.__swift5_reflstr: 0xa4e
-  __TEXT.__swift5_fieldmd: 0x7c8
+  __TEXT.__swift5_reflstr: 0xa6e
+  __TEXT.__swift5_fieldmd: 0x7e0
   __TEXT.__oslogstring: 0x1ee8
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x120

   __TEXT.__swift5_entry: 0x8
   __TEXT.__info_plist: 0x3fe
   __TEXT.__unwind_info: 0x12a0
-  __TEXT.__eh_frame: 0x3198
-  __DATA_CONST.__auth_got: 0xdb0
-  __DATA_CONST.__got: 0x690
+  __TEXT.__eh_frame: 0x3190
+  __DATA_CONST.__auth_got: 0xdb8
+  __DATA_CONST.__got: 0x6b0
   __DATA_CONST.__auth_ptr: 0x3d0
-  __DATA_CONST.__const: 0x16b8
+  __DATA_CONST.__const: 0x1720
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x1f48
   __DATA.__objc_selrefs: 0x590
   __DATA.__objc_data: 0x8e8
-  __DATA.__data: 0x19a8
+  __DATA.__data: 0x19c8
   __DATA.__bss: 0x1d90
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1263
-  Symbols:   747
-  CStrings:  684
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1268
+  Symbols:   760
+  CStrings:  686
 
Symbols:
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO13photosCleanupyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO17notesAudioSummaryyA2EmFWC
+ _$sSKsSS7ElementRtzrlE6joined9separatorS2S_tF
+ _$sSayxGSKsMc
+ _$ss31withCheckedThrowingContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5Error_pGXEtYaKlF
+ _$ss31withCheckedThrowingContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5Error_pGXEtYaKlFTu
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _$sScC12continuation8functionScCyxq_GSccyxq_G_SStcfC
CStrings:
+ "Notes Audio Summary"
+ "com.apple.centralized-feedback.evaluation.universal"

```
