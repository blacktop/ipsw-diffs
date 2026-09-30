## libLLVM.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libLLVM.dylib`

```diff

-32023.921.0.0.0
-  __TEXT.__text: 0x20296ac
+32023.921.4.0.0
+  __TEXT.__text: 0x202f09c
   __TEXT.__init_offsets: 0x68c
-  __TEXT.__const: 0x4191200
-  __TEXT.__cstring: 0x11940a
+  __TEXT.__const: 0x4191230
+  __TEXT.__cstring: 0x11942b
   __TEXT.__oslogstring: 0x181
-  __TEXT.__unwind_info: 0x2d410
+  __TEXT.__unwind_info: 0x2d468
   __TEXT.__eh_frame: 0x3800
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x273418
+  __DATA_CONST.__const: 0x273420
   __DATA_CONST.__weak_got: 0x598
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x66660
+  __AUTH_CONST.__const: 0x66750
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0xce0
   __AUTH_CONST.__auth_got: 0x990

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 72766
-  Symbols:   21893
-  CStrings:  43511
+  Functions: 72829
+  Symbols:   21900
+  CStrings:  43512
 
Symbols:
+ __ZN4llvm17DivergenceTracker24markControlDependentPhisEPKNS_11InstructionEPNS_10BasicBlockENSt3__18functionIFvPKNS_5ValueEEEE
+ __ZNK4llvm19TargetTransformInfo21getCopyLikeDstSrcLocsEPKNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo21isIgnorableMemLikeDefEPKNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo23getSafeMemLikeAccessLocEPKNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo26getSafeStoreLikeStoredValsEPNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo27isRewritableMemLikeMiscInstEPKNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo30rewriteMemLikeWithAddressSpaceEPNS_11InstructionEj
CStrings:
+ "32023.921.4"
+ "Apple LLVM version 32023.921.4"
+ "LLVM version 32023.921.4"
+ "llvm-mc (based on LLVM 32023.921.4)"
+ "tensor_element_addrspace"
- "32023.921"
- "Apple LLVM version 32023.921"
- "LLVM version 32023.921"
- "llvm-mc (based on LLVM 32023.921)"
```
