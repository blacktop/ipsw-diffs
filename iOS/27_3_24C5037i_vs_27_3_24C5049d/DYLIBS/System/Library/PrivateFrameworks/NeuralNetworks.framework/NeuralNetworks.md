## NeuralNetworks

> `/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks`

```diff

 150.0.0.0.0
-  __TEXT.__text: 0x1f0f38
+  __TEXT.__text: 0x1f1fa4
   __TEXT.__objc_methlist: 0x151c
-  __TEXT.__const: 0x1dbb8
-  __TEXT.__cstring: 0xe1f3
+  __TEXT.__const: 0x1dce8
+  __TEXT.__cstring: 0xe423
   __TEXT.__oslogstring: 0x24a
   __TEXT.__gcc_except_tab: 0x198c
-  __TEXT.__constg_swiftt: 0x7ae0
-  __TEXT.__swift5_typeref: 0x8603
-  __TEXT.__swift5_reflstr: 0x418c
-  __TEXT.__swift5_fieldmd: 0x6f20
-  __TEXT.__swift5_builtin: 0x3ac
+  __TEXT.__constg_swiftt: 0x7afc
+  __TEXT.__swift5_typeref: 0x8623
+  __TEXT.__swift5_reflstr: 0x41dc
+  __TEXT.__swift5_fieldmd: 0x6f54
+  __TEXT.__swift5_builtin: 0x3c0
   __TEXT.__swift5_assocty: 0x1ce0
-  __TEXT.__swift5_proto: 0x1d34
-  __TEXT.__swift5_types: 0x830
+  __TEXT.__swift5_proto: 0x1d40
+  __TEXT.__swift5_types: 0x834
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__swift5_capture: 0xc94
-  __TEXT.__swift5_mpenum: 0x1d4
+  __TEXT.__swift5_mpenum: 0x1dc
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0xb488
+  __TEXT.__unwind_info: 0xb498
   __TEXT.__eh_frame: 0xc7e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__got: 0xd00
-  __AUTH_CONST.__const: 0x160c8
+  __AUTH_CONST.__const: 0x16178
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0xbd38
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x2170
+  __AUTH_CONST.__auth_got: 0x2178
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x6260
   __DATA.__objc_ivar: 0xd8
-  __DATA.__data: 0x4ac8
+  __DATA.__data: 0x4ad8
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x4b80

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16357
-  Symbols:   4586
-  CStrings:  1070
+  Functions: 16376
+  Symbols:   4591
+  CStrings:  1076
 
Symbols:
+ _get_enum_tag_for_layout_string 14NeuralNetworks20BackpropagationErrorO
+ _swift_release_x10
+ _symbolic SS13operationName_t
+ _symbolic _____ 14NeuralNetworks20BackpropagationErrorO
+ _type_layout_string 14NeuralNetworks20BackpropagationErrorO
CStrings:
+ "Encountered the operation `"
+ "Failed to differentiate through an operand of `"
+ "Failed to find gradients for the operation `"
+ "` that is using a non-differentiable scalar type. Ensure all differentiate paths are using floating point scalar types."
+ "` with no derivative. Ensure the values you are differentiating against are used in the computation, also ensure the layers being propagated through all have their `learningPhase` set to `training`."
+ "`. Ensure the values you are differentiating against are used in the computation."
```
