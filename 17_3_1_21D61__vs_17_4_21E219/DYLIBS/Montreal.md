## Montreal

> `/System/Library/PrivateFrameworks/Montreal.framework/Montreal`

```diff

-178.0.0.0.0
-  __TEXT.__text: 0x1effc4
-  __TEXT.__auth_stubs: 0x18e0
+178.1.0.0.0
+  __TEXT.__text: 0x1e6360
+  __TEXT.__auth_stubs: 0x1960
   __TEXT.__init_offsets: 0x48
   __TEXT.__objc_methlist: 0x2064
-  __TEXT.__gcc_except_tab: 0x1c3cc
-  __TEXT.__const: 0x42b8
-  __TEXT.__cstring: 0x33a8
-  __TEXT.__oslogstring: 0x380
-  __TEXT.__unwind_info: 0x6108
+  __TEXT.__gcc_except_tab: 0x1cbd8
+  __TEXT.__const: 0x4298
+  __TEXT.__cstring: 0x3243
+  __TEXT.__oslogstring: 0x3d2
+  __TEXT.__unwind_info: 0x61a8
   __TEXT.__eh_frame: 0xd4
   __TEXT.__objc_classname: 0x393
-  __TEXT.__objc_methname: 0x63fe
+  __TEXT.__objc_methname: 0x6412
   __TEXT.__objc_methtype: 0x1611
   __TEXT.__objc_stubs: 0x4a00
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x860
+  __DATA_CONST.__const: 0x840
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3c30
   __DATA_CONST.__objc_selrefs: 0x1470
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x350
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__const: 0x8580
   __AUTH_CONST.__objc_intobj: 0x270

   __AUTH_CONST.__objc_const: 0xd20
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0xc88
+  __AUTH_CONST.__auth_got: 0xcc8
   __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x350
-  __DATA.__objc_superrefs: 0x108
   __DATA.__objc_ivar: 0x338
   __DATA.__data: 0xb20
   __DATA.__thread_vars: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E387B349-3010-3E37-B431-57DD659FC6F8
-  Functions: 4426
-  Symbols:   749
-  CStrings:  2201
+  UUID: 436752A9-6A19-3CB6-855E-F95374D6F382
+  Functions: 4459
+  Symbols:   757
+  CStrings:  2190
 
Symbols:
+ _CFURLCopyFragment
+ __ZN4E5RT10E5Compiler11GetCompilerEv
+ __ZN4E5RT10E5Compiler7CompileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_17E5CompilerOptionsE
+ __ZN4E5RT14ProgramLibrary20GetExportedFunctionsEv
+ __ZN4E5RT17E5CompilerOptions17SetMilEntryPointsERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE
+ __ZN4E5RT17E5CompilerOptions22SetPreferredCpuBackendERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN4E5RT17E5CompilerOptions28SetComputeDeviceTypesAllowedERKNSt3__16vectorINS_17ComputeDeviceTypeENS1_9allocatorIS3_EEEE
+ __ZN4E5RT17E5CompilerOptions6CreateEv
+ __ZN4E5RT24ExecutionStreamOperation26CreatePreCompiledComputeOpERKNS_33PrecompiledComputeOpCreateOptionsE
+ __ZN4E5RT33PrecompiledComputeOpCreateOptions16SetOperationNameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN4E5RT33PrecompiledComputeOpCreateOptions6CreateENSt3__110shared_ptrIKNS_15ProgramFunctionEEE
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc
- __ZNK4E5RT14TensorDataType6IsTypeIfEEbv
- __ZNK4E5RT16TensorDescriptor20GetTensorDataTypeRefEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
CStrings:
+ ".mil"
+ "Inconsistent state sizes for: %s"
+ "Logic error, unexpected state input name: %s"
+ "Number of states (%zu) isn't a multiple of batch size (%d)"
+ "T@\"NSString\",?,R,C"
+ "Unable to execute Espresso network"
+ "unordered_map::at: key not found"
- "Fulllayer"
- "Invalid input type, only float are currently supported"
- "Recurrent"
- "Unable to exceute Espresso network"
- "_c_in"
- "_h_in"
- "_k_s_in"
- "_r_c_in"
- "_r_h_in"
- "_v_s_in"
- "full sequence MRLModelRecognizeTopN"
- "incremental MRLModelRecognizeIncrementalTopN"
- "incremental internalMRLModelRecognizeIncremental"
- "rnn bias "
- "sequence MRLModelRecognize"
- "sequence MRLModelRecognizeVectors"
- "sequence MRLModelRecognizeVectorsIncremental"
- "sequence MRLModelRecognizeVectorsIncrementalTopN"
- "sequence MRLModelRecognizeVectorsTopN"

```
