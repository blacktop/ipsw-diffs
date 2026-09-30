## MusicUnderstanding

> `/System/Library/Frameworks/MusicUnderstanding.framework/MusicUnderstanding`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-12.0.0.0.0
-  __TEXT.__text: 0x102e98
+13.0.0.0.0
+  __TEXT.__text: 0xfdf40
   __TEXT.__objc_methlist: 0x160
-  __TEXT.__const: 0xceb8
-  __TEXT.__constg_swiftt: 0x44c4
-  __TEXT.__swift5_typeref: 0x3a52
+  __TEXT.__const: 0xc958
+  __TEXT.__constg_swiftt: 0x42b0
+  __TEXT.__swift5_typeref: 0x385a
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x40cc
-  __TEXT.__swift5_fieldmd: 0x3fe8
-  __TEXT.__swift5_assocty: 0xc70
-  __TEXT.__swift5_proto: 0x874
-  __TEXT.__swift5_types: 0x484
-  __TEXT.__swift_as_entry: 0x3bc
-  __TEXT.__swift_as_ret: 0x3d8
-  __TEXT.__swift_as_cont: 0x664
-  __TEXT.__cstring: 0xda1
-  __TEXT.__swift5_capture: 0x63c
-  __TEXT.__oslogstring: 0x66a
-  __TEXT.__swift5_protos: 0x58
+  __TEXT.__swift5_reflstr: 0x400c
+  __TEXT.__swift5_fieldmd: 0x3f5c
+  __TEXT.__swift5_assocty: 0xc00
+  __TEXT.__swift5_proto: 0x848
+  __TEXT.__swift5_types: 0x480
+  __TEXT.__swift_as_entry: 0x344
+  __TEXT.__swift_as_ret: 0x398
+  __TEXT.__swift_as_cont: 0x610
+  __TEXT.__cstring: 0xd51
+  __TEXT.__swift5_capture: 0x744
+  __TEXT.__oslogstring: 0x80a
+  __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__swift5_acfuncs: 0x3c
-  __TEXT.__unwind_info: 0x5520
-  __TEXT.__eh_frame: 0xbbf4
+  __TEXT.__unwind_info: 0x5330
+  __TEXT.__eh_frame: 0xb674
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c0
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c8
+  __DATA_CONST.__objc_selrefs: 0x1d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x8548
-  __AUTH_CONST.__objc_const: 0x3868
-  __AUTH_CONST.__auth_got: 0x15e0
-  __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0x3da8
-  __DATA.__data: 0x3ea0
-  __DATA.__bss: 0xfe90
-  __DATA.__common: 0x140
+  __AUTH_CONST.__const: 0x89a8
+  __AUTH_CONST.__objc_const: 0x35c8
+  __AUTH_CONST.__auth_got: 0x14b8
+  __AUTH.__objc_data: 0x2d0
+  __AUTH.__data: 0x3aa0
+  __DATA.__data: 0x3d78
+  __DATA.__bss: 0xf910
+  __DATA.__common: 0x128
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftDistributed.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7805
-  Symbols:   289
-  CStrings:  159
+  Functions: 7745
+  Symbols:   284
+  CStrings:  162
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
+ _objc_retain_x28
- _objc_release_x9
- _object_getClass
- _swift_distributedActor_remote_initialize
- _swift_distributed_actor_is_remote
- _swift_release_x9
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
- "MusicUnderstanding/MelSpectrogramModelInputProvider.swift"
- "com.apple.computationalmusicd"
```
