## MTLCompiler

> `/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__DATA.__data`

```diff

-382.5.0.0.0
-  __TEXT.__text: 0xb7430
-  __TEXT.__gcc_except_tab: 0xa51c
-  __TEXT.__const: 0x1278
-  __TEXT.__cstring: 0x96db
+382.5.3.0.0
+  __TEXT.__text: 0xb7a58
+  __TEXT.__gcc_except_tab: 0xa548
+  __TEXT.__const: 0x1288
+  __TEXT.__cstring: 0x96e7
   __TEXT.__oslogstring: 0x4e7
-  __TEXT.__unwind_info: 0x2f38
+  __TEXT.__unwind_info: 0x2f58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __AUTH_CONST.__const: 0x16b0
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__weak_auth_got: 0x50
-  __AUTH_CONST.__auth_got: 0x10e8
+  __AUTH_CONST.__auth_got: 0x10f8
   __DATA.__data: 0x474
   __DATA.__common: 0x26
   __DATA.__bss: 0xa28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2137
-  Symbols:   3459
-  CStrings:  1638
+  Functions: 2144
+  Symbols:   3468
+  CStrings:  1639
 
Symbols:
+ __ZN4llvm10AllocaInst25getDeferredStaticSizeCallEv
+ __ZN4llvm11Instruction10moveBeforeEPS0_
+ __ZN4llvm12DenseMapBaseINS_13SmallDenseMapIPNS_8CallInstENS_6detail13DenseSetEmptyELj4ENS_12DenseMapInfoIS3_vEENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_E11try_emplaceIJRS5_EEENSt3__14pairINS_16DenseMapIteratorIS3_S5_S7_S9_Lb0EEEbEERKS3_DpOT_
+ __ZN4llvm12DenseMapBaseINS_13SmallDenseMapIPNS_8CallInstENS_6detail13DenseSetEmptyELj4ENS_12DenseMapInfoIS3_vEENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_E18moveFromOldBucketsEPS9_SC_
+ __ZN4llvm12DenseMapBaseINS_13SmallDenseMapIPNS_8CallInstENS_6detail13DenseSetEmptyELj4ENS_12DenseMapInfoIS3_vEENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_E20InsertIntoBucketImplIS3_EEPS9_RKS3_RKT_SD_
+ __ZN4llvm13SmallDenseMapIPNS_8CallInstENS_6detail13DenseSetEmptyELj4ENS_12DenseMapInfoIS2_vEENS3_12DenseSetPairIS2_EEE4growEj
+ __ZN4llvm14SmallSetVectorIPNS_8CallInstELj4EED2Ev
+ __ZN4llvm9SetVectorIPNS_8CallInstENS_11SmallVectorIS2_Lj4EEENS_13SmallDenseSetIS2_Lj4ENS_12DenseMapInfoIS2_vEEEEE6insertERKS2_
+ __ZNK4llvm12DenseMapBaseINS_13SmallDenseMapIPNS_8CallInstENS_6detail13DenseSetEmptyELj4ENS_12DenseMapInfoIS3_vEENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_E15LookupBucketForIS3_EEbRKT_RPKS9_
CStrings:
+ "stride0_i32"
```
