## CoreML

> `/System/Library/Frameworks/CoreML.framework/Versions/A/CoreML`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.22.1.0.0
-  __TEXT.__text: 0x71e234
+3600.25.2.0.0
+  __TEXT.__text: 0x71e154
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x10340
   __TEXT.__const: 0x52203
   __TEXT.__dlopen_cstrs: 0x21e
-  __TEXT.__cstring: 0x2e851
+  __TEXT.__cstring: 0x2e84d
   __TEXT.__constg_swiftt: 0x1ec8
   __TEXT.__swift5_typeref: 0x21f0
   __TEXT.__swift5_builtin: 0x1e0

   __TEXT.__swift5_capture: 0xf88
   __TEXT.__swift_as_ret: 0x110
   __TEXT.__oslogstring: 0xb31e
-  __TEXT.__gcc_except_tab: 0x3ad6c
+  __TEXT.__gcc_except_tab: 0x3ad5c
   __TEXT.__ustring: 0x204
   __TEXT.__unwind_info: 0x103b8
   __TEXT.__eh_frame: 0x551c

   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x7d8
   __DATA_CONST.__objc_arraydata: 0x160
-  __DATA_CONST.__got: 0x1168
+  __DATA_CONST.__got: 0x11b8
   __AUTH_CONST.__const: 0x21d18
   __AUTH_CONST.__cfstring: 0xd3a0
   __AUTH_CONST.__objc_const: 0x23128

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 17065
   Symbols:   27345
-  CStrings:  4777
+  CStrings:  4776
 
Functions:
~ sub_18bf0a504 -> sub_18c082504 : 88 -> 80
~ sub_18bf0a738 -> sub_18c082730 : 24 -> 32
~ __ZN8Archiver17_IArchiveDiskImplC2ERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_10FileFormatE : 2364 -> 2132
~ __ZNK8Archiver17_IArchiveDiskImpl7getBlobERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 236 -> 244
~ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEC1ERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj : 460 -> 452
~ __ZN8Archiver17_IArchiveDiskImplD0Ev : 56 -> 64
~ __ZNK8Archiver17_IArchiveDiskImpl12isENMLFormatEv : 44 -> 36
~ __ZN6google8protobuf8internal15ThreadSafeArena23AllocateAlignedFallbackEmPKSt9type_info : 260 -> 268
~ __Block_byref_object_dispose_.22033 : 36 -> 28
~ __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEED2Ev : 208 -> 216
~ __ZN8Archiver13_OArchiveImplD0Ev : 24 -> 16
~ ___56+[MLBackgroundWatchdog watchdogWithTimeout:label:queue:]_block_invoke : 216 -> 224
CStrings:
+ " is not a valid .mlmodelc file because the first word is not recognizable. "
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Compute/CustomMetalOps/MLComputeFunction+ExecutionPolicy.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Core/MLTensor+Initializers.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/BinaryElementwiseArithmetic.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/Comparison.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/GatherScatter.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/Image.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/Indexing.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/LinearAlgebra.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/Logical.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/Reduction.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/TensorOperations.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Operations/Transformations.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Support/Preconditions.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/CoreML/Tensor/Support/ShapeInference.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/arena.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/io/coded_stream.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/io/zero_copy_stream.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/io/zero_copy_stream_impl_lite.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/map.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/message_lite.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/parse_context.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/stubs/stringpiece.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HMSMug/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/wire_format_lite.cc"
+ "3600.25.2"
- " is not a valid .mlmodelc file because the first word ("
- ") is not recognizable. "
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Compute/CustomMetalOps/MLComputeFunction+ExecutionPolicy.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Core/MLTensor+Initializers.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/BinaryElementwiseArithmetic.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/Comparison.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/GatherScatter.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/Image.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/Indexing.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/LinearAlgebra.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/Logical.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/Reduction.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/TensorOperations.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Operations/Transformations.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Support/Preconditions.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/CoreML/Tensor/Support/ShapeInference.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/arena.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/io/coded_stream.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/io/zero_copy_stream.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/io/zero_copy_stream_impl_lite.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/map.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/message_lite.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/parse_context.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/stubs/stringpiece.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.udjFWK/Sources/CoreML/coremltools-internal/deps/protobuf/src/google/protobuf/wire_format_lite.cc"
- "3600.22.1"
```
