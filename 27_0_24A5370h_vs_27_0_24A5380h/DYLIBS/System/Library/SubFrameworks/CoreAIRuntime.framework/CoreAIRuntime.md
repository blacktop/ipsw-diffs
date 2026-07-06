## CoreAIRuntime

> `/System/Library/SubFrameworks/CoreAIRuntime.framework/CoreAIRuntime`

```diff

-  __TEXT.__text: 0x50ed5c
+  __TEXT.__text: 0x5283fc
   __TEXT.__objc_methlist: 0x2c34
-  __TEXT.__const: 0xe090
-  __TEXT.__constg_swiftt: 0x34c0
-  __TEXT.__swift5_typeref: 0x31bd
-  __TEXT.__swift5_reflstr: 0x2526
-  __TEXT.__swift5_fieldmd: 0x386c
+  __TEXT.__const: 0xde10
+  __TEXT.__constg_swiftt: 0x34e8
+  __TEXT.__swift5_typeref: 0x3175
+  __TEXT.__swift5_reflstr: 0x254d
+  __TEXT.__swift5_fieldmd: 0x3894
   __TEXT.__swift5_builtin: 0x244
   __TEXT.__swift5_assocty: 0x540
   __TEXT.__swift5_proto: 0x6ec
-  __TEXT.__swift5_types: 0x3e4
+  __TEXT.__swift5_types: 0x3e8
   __TEXT.__swift5_mpenum: 0x398
-  __TEXT.__cstring: 0xbda1
-  __TEXT.__swift5_capture: 0x11a4
+  __TEXT.__cstring: 0xbfd1
+  __TEXT.__swift5_capture: 0x1154
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x74
   __TEXT.__swift_as_cont: 0xd0
   __TEXT.__swift5_types2: 0x84
   __TEXT.__swift5_protos: 0xb8
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x6378
-  __TEXT.__eh_frame: 0x12248
+  __TEXT.__unwind_info: 0x5e20
+  __TEXT.__eh_frame: 0x12410
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x1b20
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xa288
-  __AUTH_CONST.__objc_const: 0x52c0
-  __AUTH_CONST.__auth_got: 0x14e0
-  __AUTH.__objc_data: 0x230
-  __AUTH.__data: 0x2400
-  __DATA.__data: 0x2068
-  __DATA.__bss: 0x8ba0
-  __DATA.__common: 0x168
+  __AUTH_CONST.__const: 0xa208
+  __AUTH_CONST.__objc_const: 0x52e0
+  __AUTH_CONST.__auth_got: 0x14f8
+  __AUTH.__data: 0xc78
+  __DATA.__data: 0x1de0
+  __DATA.__bss: 0x8b20
+  __DATA.__common: 0x90
+  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__data: 0x1a50
+  __DATA_DIRTY.__common: 0xe0
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7925
-  Symbols:   331
-  CStrings:  1013
+  Functions: 7990
+  Symbols:   334
+  CStrings:  1016
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_types2 : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _objc_retain_x12
+ _swift_retain_x11
+ _vDSP_mtrans
+ _vDSP_mtransD
+ _vDSP_vsmsa
- _objc_retain_x13
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ ", output.strides="
+ "CoreAIRuntime/ConcatKernel.swift"
+ "CoreAIRuntime/FastBlockwiseShiftScaleKernel.swift"
+ "CoreAIRuntime/FastMatMulKernel+SIMDBackend.swift"
+ "MatMulSIMDBackend does not support "
+ "Sub-byte concat requires contiguous input and output (got input.strides="
+ "This function's reshape implementation reads input values, but reshape(for:) only carries shape metadata. Use reshape(inputs:) to provide input values, or omit the explicit reshape call — the standard inference path re-runs reshape with real values on every call."
- "CallSiteLoc"
- "FileLineCol"
- "Fused"
- "NameLoc"

```
