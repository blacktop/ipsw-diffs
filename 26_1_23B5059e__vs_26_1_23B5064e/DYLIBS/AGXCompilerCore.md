## AGXCompilerCore

> `/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore`

```diff

-341.9.1.0.0
-  __TEXT.__text: 0x225ecc
-  __TEXT.__auth_stubs: 0x2710
+341.11.0.0.0
+  __TEXT.__text: 0x2263c8
+  __TEXT.__auth_stubs: 0x2750
   __TEXT.__const: 0x39d48
-  __TEXT.__cstring: 0x1a8f0
-  __TEXT.__oslogstring: 0x40f
-  __TEXT.__unwind_info: 0x3ce0
+  __TEXT.__cstring: 0x1a962
+  __TEXT.__oslogstring: 0x46f
+  __TEXT.__unwind_info: 0x3ce8
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_methname: 0xa2
   __TEXT.__objc_stubs: 0x100

   __DATA_CONST.__const: 0x7bc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1390
+  __AUTH_CONST.__auth_got: 0x13b0
   __AUTH_CONST.__const: 0x6ed88
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH.__data: 0x50

   __AUTH.__thread_bss: 0x30
   __DATA.__data: 0x80
   __DATA.__bss: 0x3d28
-  __DATA_DIRTY.__bss: 0xe38
+  __DATA_DIRTY.__bss: 0xe18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E8B0E3D-C015-37E1-96C1-B2E3192C9082
-  Functions: 7011
-  Symbols:   18893
-  CStrings:  4486
+  UUID: 4875C895-28AA-3235-8E56-2F8AD5B62748
+  Functions: 7012
+  Symbols:   18896
+  CStrings:  4489
 
Symbols:
+ __ZL14isStringMDNodePN4llvm8MetadataEPKc.315
+ __ZL15_agcFieldStringINSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEES6_RKS6_RKT_.332
+ __ZL15_agcFieldStringIjENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKS6_RKT_.333
+ __ZL16_agcIndentedLineNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEj.334
+ __ZL22tryChangeOwnerToMobilePKc
+ __ZN17AGCLLVMUserObject12hoistAllocasEPN4llvm10BasicBlockERNS0_14ilist_iteratorINS0_12ilist_detail12node_optionsINS0_11InstructionELb0ELb0EvEELb0ELb0EEES2_
+ __ZN4llvm10AllocaInst25getDeferredStaticSizeCallEv
+ __ZN4llvm11Instruction10moveBeforeERNS_10BasicBlockENS_14ilist_iteratorINS_12ilist_detail12node_optionsIS0_Lb0ELb0EvEELb0ELb0EEE
+ __ZN4llvm12DenseMapBaseINS_13SmallDenseMapIPNS_8CallInstENS_6detail13DenseSetEmptyELj8ENS_12DenseMapInfoIS3_vEENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_E18moveFromOldBucketsEPS9_SC_
+ __ZN4llvm13SmallDenseMapIPNS_8CallInstENS_6detail13DenseSetEmptyELj8ENS_12DenseMapInfoIS2_vEENS3_12DenseSetPairIS2_EEE4growEj
+ __ZNK4llvm12DenseMapBaseINS_13SmallDenseMapIPNS_8CallInstENS_6detail13DenseSetEmptyELj8ENS_12DenseMapInfoIS3_vEENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_E15LookupBucketForIS3_EEbRKT_RPKS9_
+ __ZNKSt3__110error_code7messageEv
+ __ZZN6AGCEnv18getStatusVariablesEPmE11status_vars
+ ___block_literal_global.212
+ _strerror
- __ZGVZN6AGCEnv18getStatusVariablesEvE11status_vars
- __ZL14isStringMDNodePN4llvm8MetadataEPKc.314
- __ZL15_agcFieldStringINSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEES6_RKS6_RKT_.331
- __ZL15_agcFieldStringIjENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKS6_RKT_.332
- __ZL16_agcIndentedLineNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEj.333
- __ZN17AGCLLVMUserObject12hoistAllocasEPN4llvm10BasicBlockERNS0_14ilist_iteratorINS0_12ilist_detail12node_optionsINS0_11InstructionELb0ELb0EvEELb0ELb0EEE
- __ZN6AGCEnv18getStatusVariablesEv
- __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEEC2B8nn200100ESt16initializer_listIS2_E
- __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEED1B8nn200100Ev
- __ZZN6AGCEnv18getStatusVariablesEvE11status_vars
- ___block_literal_global.211
CStrings:
+ "AGC: %s:%d:%s: *** Failed to change owner uid to 501: %s, with error code %d (%s)\n"
+ "AGC: %s:%d:%s: *** Failed to create: %s, with error code %d (%s)\n"
+ "AGC: %s:%d:%s: *** Failed to open: %s, with error code %d (%s)\n"
+ "AGC: AGC: %s:%d:%s: *** Failed to change owner uid to 501: %s, with error code %d (%s)\n"
+ "AGC: AGC: %s:%d:%s: *** Failed to create: %s, with error code %d (%s)\n"
+ "AGC: AGC: %s:%d:%s: *** Failed to open: %s, with error code %d (%s)\n"
+ "tryChangeOwnerToMobile"
- "AGC: %s:%d:%s: *** Failed to create: %s, with error code %d\n"
- "AGC: %s:%d:%s: *** Failed to modify: %s, with error code %d\n"
- "AGC: AGC: %s:%d:%s: *** Failed to create: %s, with error code %d\n"
- "AGC: AGC: %s:%d:%s: *** Failed to modify: %s, with error code %d\n"

```
