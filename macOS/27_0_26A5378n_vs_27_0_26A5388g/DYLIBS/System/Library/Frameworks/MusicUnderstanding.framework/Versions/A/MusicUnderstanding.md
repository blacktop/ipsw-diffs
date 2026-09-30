## MusicUnderstanding

> `/System/Library/Frameworks/MusicUnderstanding.framework/Versions/A/MusicUnderstanding`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-12.0.0.0.0
-  __TEXT.__text: 0x105894
+13.0.0.0.0
+  __TEXT.__text: 0x100818
   __TEXT.__objc_methlist: 0x160
-  __TEXT.__const: 0xcf08
-  __TEXT.__constg_swiftt: 0x44c4
-  __TEXT.__swift5_typeref: 0x3a52
+  __TEXT.__const: 0xc998
+  __TEXT.__constg_swiftt: 0x42b0
+  __TEXT.__swift5_typeref: 0x385a
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x40cc
-  __TEXT.__swift5_fieldmd: 0x3fe8
-  __TEXT.__swift5_assocty: 0xc70
-  __TEXT.__swift5_proto: 0x874
-  __TEXT.__swift5_types: 0x484
-  __TEXT.__swift_as_entry: 0x3cc
-  __TEXT.__swift_as_ret: 0x3e8
-  __TEXT.__swift_as_cont: 0x670
-  __TEXT.__cstring: 0xde1
-  __TEXT.__swift5_capture: 0x694
-  __TEXT.__oslogstring: 0x66a
-  __TEXT.__swift5_protos: 0x58
+  __TEXT.__swift5_reflstr: 0x400c
+  __TEXT.__swift5_fieldmd: 0x3f5c
+  __TEXT.__swift5_assocty: 0xc00
+  __TEXT.__swift5_proto: 0x848
+  __TEXT.__swift5_types: 0x480
+  __TEXT.__swift_as_entry: 0x354
+  __TEXT.__swift_as_ret: 0x3a8
+  __TEXT.__swift_as_cont: 0x61c
+  __TEXT.__cstring: 0xd51
+  __TEXT.__swift5_capture: 0x79c
+  __TEXT.__oslogstring: 0x80a
+  __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__swift5_acfuncs: 0x3c
-  __TEXT.__unwind_info: 0x5578
-  __TEXT.__eh_frame: 0xbb84
+  __TEXT.__unwind_info: 0x5368
+  __TEXT.__eh_frame: 0xb60c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c8
+  __DATA_CONST.__objc_selrefs: 0x1d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x85e8
-  __AUTH_CONST.__objc_const: 0x3868
-  __AUTH_CONST.__auth_got: 0x1430
-  __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0x3da8
-  __DATA.__data: 0x3ea0
-  __DATA.__bss: 0xfe90
-  __DATA.__common: 0x140
+  __AUTH_CONST.__const: 0x8a48
+  __AUTH_CONST.__objc_const: 0x35c8
+  __AUTH_CONST.__auth_got: 0x1310
+  __AUTH.__objc_data: 0x2d0
+  __AUTH.__data: 0x3aa0
+  __DATA.__data: 0x3d78
+  __DATA.__bss: 0xf910
+  __DATA.__common: 0x128
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreML.framework/Versions/A/CoreML
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/PrivateFrameworks/XPCDistributed.framework/Versions/A/XPCDistributed
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftDistributed.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7856
-  Symbols:   235
-  CStrings:  160
+  Functions: 7789
+  Symbols:   231
+  CStrings:  162
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
- _object_getClass
- _swift_distributedActor_remote_initialize
- _swift_distributed_actor_is_remote
- _swift_task_isCurrentExecutor
- _swift_task_reportUnexpectedExecutor
CStrings:
+ "KeyAnalyzer: invalid accumulate shape (classCount: %ld, accumulator: %ld)"
+ "KeyAnalyzer: invalid flush shape (pending: %ld, accumulator: %ld, classCount: %ld)"
+ "KeyAnalyzer: pendingOverlap %ld not a multiple of classCount %ld"
+ "KeyAnalyzer: prediction scalars %ld too small for %ld frames × %ld classes"
+ "MelSpectrogramConverter: invalid DFT buffer sizes for windowLength %ld (time: %ld, freq: %ld, real: %ld, imag: %ld)"
+ "TESTBOT_IDENTITY_JSON"
- "Instrument activity range processing cancelled"
- "MusicUnderstanding/ComputationalMusicService.swift"
- "MusicUnderstanding/MelSpectrogramModelInputProvider.swift"
- "com.apple.computationalmusicd"
```
