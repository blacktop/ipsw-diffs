## AGXCompilerCore

> `/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__AUTH.__thread_vars`

```diff

-360.32.0.0.0
-  __TEXT.__text: 0x268f04
-  __TEXT.__const: 0x3a418
-  __TEXT.__cstring: 0x1c6e2
+360.34.5.0.0
+  __TEXT.__text: 0x26b308
+  __TEXT.__const: 0x3ae28
+  __TEXT.__cstring: 0x1c8e4
   __TEXT.__oslogstring: 0x5fc
-  __TEXT.__unwind_info: 0x47a0
+  __TEXT.__unwind_info: 0x47c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x7bb0
+  __DATA_CONST.__const: 0x7bc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0x40

   __AUTH_CONST.__const: 0x78040
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__weak_auth_got: 0xe8
-  __AUTH_CONST.__auth_got: 0x13d0
+  __AUTH_CONST.__auth_got: 0x13e8
   __AUTH.__data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8182
-  Symbols:   11081
-  CStrings:  4686
+  Functions: 8191
+  Symbols:   11092
+  CStrings:  4722
 
Symbols:
+ __ZN12AGCTelemetry6recordEPN4llvm6ModuleENS0_9StringRefE
+ __ZN14AGCMLTelemetry10floatTokenEPN4llvm4TypeE
+ __ZN14AGCMLTelemetry11formatTokenEN4llvm11GPUBaseInfo9MXUFormatEj
+ __ZN14AGCMLTelemetry9matrixKeyEjjjbPKcS1_S1_S1_
+ __ZN19AGCFeatureTelemetry4usedEPN4llvm6ModuleENS0_9StringRefE
+ __ZN4llvm11NamedMDNode10setOperandEjPNS_6MDNodeE
+ __ZN4llvm12DenseMapBaseINS_13SmallDenseMapINS_9StringRefENS_6detail13DenseSetEmptyELj16ENS_12DenseMapInfoIS2_vEENS3_12DenseSetPairIS2_EEEES2_S4_S6_S8_E18moveFromOldBucketsEPS8_SB_
+ __ZN4llvm13SmallDenseMapINS_9StringRefENS_6detail13DenseSetEmptyELj16ENS_12DenseMapInfoIS1_vEENS2_12DenseSetPairIS1_EEE4growEj
+ __ZN4llvm9StringMapIyNS_15MallocAllocatorEED2Ev
+ __ZNK4llvm11Instruction9getModuleEv
+ __ZNK4llvm11NamedMDNode7getNameEv
+ __ZNK4llvm12DenseMapBaseINS_13SmallDenseMapINS_9StringRefENS_6detail13DenseSetEmptyELj16ENS_12DenseMapInfoIS2_vEENS3_12DenseSetPairIS2_EEEES2_S4_S6_S8_E15LookupBucketForIS2_EEbRKT_RPKS8_
+ __ZNK4llvm9StringMapIN32SimdMatrixMultiplyAccumulatePass14OpLoweringInfoENS_15MallocAllocatorEE6lookupENS_9StringRefE
+ __ZTC23AGCLLVMGLFragmentShader4816_21AGCLLVMFragmentShader
+ __ZTC23AGCLLVMGLFragmentShader4816_30AGCLLVMStatelessFragmentObject
+ __ZTC24AGCLLVMAGPFragmentShader4816_21AGCLLVMFragmentShader
+ __ZTC24AGCLLVMAGPFragmentShader4816_30AGCLLVMStatelessFragmentObject
+ __ZTC28AGCLLVMAGPFragmentShaderGen34816_21AGCLLVMFragmentShader
+ __ZTC28AGCLLVMAGPFragmentShaderGen34816_30AGCLLVMStatelessFragmentObject
+ __ZTC28AGCLLVMAGPFragmentShaderGen44816_21AGCLLVMFragmentShader
+ __ZTC28AGCLLVMAGPFragmentShaderGen44816_30AGCLLVMStatelessFragmentObject
+ __ZTC28AGCLLVMAGPFragmentShaderGen64816_21AGCLLVMFragmentShader
+ __ZTC28AGCLLVMAGPFragmentShaderGen64816_30AGCLLVMStatelessFragmentObject
+ __ZTC29AGCLLVMUserIntersectionShader4816_25AGCLLVMIntersectionShader
+ __ZTC41AGCLLVMUserIFBEmulationIntersectionShader4816_25AGCLLVMIntersectionShader
+ __ZThn4816_N23AGCLLVMGLFragmentShaderD0Ev
+ __ZThn4816_N23AGCLLVMGLFragmentShaderD1Ev
+ __ZThn4816_N24AGCLLVMAGPFragmentShaderD0Ev
+ __ZThn4816_N24AGCLLVMAGPFragmentShaderD1Ev
+ __ZThn4816_N25AGCLLVMUserFragmentShaderD0Ev
+ __ZThn4816_N25AGCLLVMUserFragmentShaderD1Ev
+ __ZThn4816_N28AGCLLVMAGPFragmentShaderGen3D0Ev
+ __ZThn4816_N28AGCLLVMAGPFragmentShaderGen3D1Ev
+ __ZThn4816_N28AGCLLVMAGPFragmentShaderGen4D0Ev
+ __ZThn4816_N28AGCLLVMAGPFragmentShaderGen4D1Ev
+ __ZThn4816_N28AGCLLVMAGPFragmentShaderGen6D0Ev
+ __ZThn4816_N28AGCLLVMAGPFragmentShaderGen6D1Ev
+ __ZThn4816_N29AGCLLVMUserIntersectionShaderD0Ev
+ __ZThn4816_N29AGCLLVMUserIntersectionShaderD1Ev
+ __ZThn4816_N41AGCLLVMUserIFBEmulationIntersectionShaderD0Ev
+ __ZThn4816_N41AGCLLVMUserIFBEmulationIntersectionShaderD1Ev
+ __ZThn4816_NK25AGCLLVMUserFragmentShader17isRtPsoStateKnownEj
+ __ZThn4816_NK25AGCLLVMUserFragmentShader20isAnyPsoStateUnknownEv
- __ZNSt3__16vectorIPN4llvm4TypeENS_9allocatorIS3_EEE18__insert_with_sizeB9fqn220106INS_17_ClassicAlgPolicyEPKS3_SA_EENS_11__wrap_iterIPS3_EENSB_ISA_EET0_T1_l
- __ZNSt3__16vectorIPN4llvm5ValueENS_9allocatorIS3_EEE18__insert_with_sizeB9fqn220106INS_17_ClassicAlgPolicyEPKS3_SA_EENS_11__wrap_iterIPS3_EENSB_ISA_EET0_T1_l
- __ZTC23AGCLLVMGLFragmentShader4768_21AGCLLVMFragmentShader
- __ZTC23AGCLLVMGLFragmentShader4768_30AGCLLVMStatelessFragmentObject
- __ZTC24AGCLLVMAGPFragmentShader4768_21AGCLLVMFragmentShader
- __ZTC24AGCLLVMAGPFragmentShader4768_30AGCLLVMStatelessFragmentObject
- __ZTC28AGCLLVMAGPFragmentShaderGen34768_21AGCLLVMFragmentShader
- __ZTC28AGCLLVMAGPFragmentShaderGen34768_30AGCLLVMStatelessFragmentObject
- __ZTC28AGCLLVMAGPFragmentShaderGen44768_21AGCLLVMFragmentShader
- __ZTC28AGCLLVMAGPFragmentShaderGen44768_30AGCLLVMStatelessFragmentObject
- __ZTC28AGCLLVMAGPFragmentShaderGen64768_21AGCLLVMFragmentShader
- __ZTC28AGCLLVMAGPFragmentShaderGen64768_30AGCLLVMStatelessFragmentObject
- __ZTC29AGCLLVMUserIntersectionShader4768_25AGCLLVMIntersectionShader
- __ZTC41AGCLLVMUserIFBEmulationIntersectionShader4768_25AGCLLVMIntersectionShader
- __ZThn4768_N23AGCLLVMGLFragmentShaderD0Ev
- __ZThn4768_N23AGCLLVMGLFragmentShaderD1Ev
- __ZThn4768_N24AGCLLVMAGPFragmentShaderD0Ev
- __ZThn4768_N24AGCLLVMAGPFragmentShaderD1Ev
- __ZThn4768_N25AGCLLVMUserFragmentShaderD0Ev
- __ZThn4768_N25AGCLLVMUserFragmentShaderD1Ev
- __ZThn4768_N28AGCLLVMAGPFragmentShaderGen3D0Ev
- __ZThn4768_N28AGCLLVMAGPFragmentShaderGen3D1Ev
- __ZThn4768_N28AGCLLVMAGPFragmentShaderGen4D0Ev
- __ZThn4768_N28AGCLLVMAGPFragmentShaderGen4D1Ev
- __ZThn4768_N28AGCLLVMAGPFragmentShaderGen6D0Ev
- __ZThn4768_N28AGCLLVMAGPFragmentShaderGen6D1Ev
- __ZThn4768_N29AGCLLVMUserIntersectionShaderD0Ev
- __ZThn4768_N29AGCLLVMUserIntersectionShaderD1Ev
- __ZThn4768_N41AGCLLVMUserIFBEmulationIntersectionShaderD0Ev
- __ZThn4768_N41AGCLLVMUserIFBEmulationIntersectionShaderD1Ev
- __ZThn4768_NK25AGCLLVMUserFragmentShader17isRtPsoStateKnownEj
- __ZThn4768_NK25AGCLLVMUserFragmentShader20isAnyPsoStateUnknownEv
CStrings:
+ ".fgemm."
+ ".generic."
+ ".global."
+ ".igemm."
+ ".local."
+ ".specialized.p"
+ "16x16x32"
+ "16x32x16"
+ "16x32x32"
+ "16x8x16"
+ "16x8x32"
+ "32x16x16"
+ "32x16x32"
+ "32x32x16"
+ "32x32x32"
+ "8x16x16"
+ "8x16x32"
+ "8x8x8"
+ "agc.telemetry.feature.f32_local_atomics"
+ "agc.telemetry.feature.generic_address_space_use"
+ "agc.telemetry.feature.texture_multifetch"
+ "agc.telemetry.feature.texture_read_with_sampler"
+ "agc.telemetry.feature.tpu_integer_coordinates"
+ "agc.telemetry.ml.matrix."
+ "agc.telemetry.ml.quantization."
+ "fgemm"
+ "fp16"
+ "fp32"
+ "fp8_e4m3a"
+ "fp8_e4m3b"
+ "igemm"
+ "int16"
+ "int32"
+ "pack."
+ "unknown"
+ "unpack."
```
