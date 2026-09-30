## libLLVM.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libLLVM.dylib`

```diff

-32023.921.0.0.0
-  __TEXT.__text: 0x1f20490
+32023.921.5.0.0
+  __TEXT.__text: 0x1f25f0c
   __TEXT.__init_offsets: 0x66c
-  __TEXT.__const: 0x3fae640
-  __TEXT.__cstring: 0x114cc9
+  __TEXT.__const: 0x3fae670
+  __TEXT.__cstring: 0x114cea
   __TEXT.__oslogstring: 0x181
-  __TEXT.__unwind_info: 0x2c5f0
+  __TEXT.__unwind_info: 0x2c648
   __TEXT.__eh_frame: 0x3800
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x1cc868
+  __DATA_CONST.__const: 0x1cc870
   __DATA_CONST.__weak_got: 0x598
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x613f8
+  __AUTH_CONST.__const: 0x614b8
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0xce0
   __AUTH_CONST.__auth_got: 0x9a0

   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0xe75
   __DATA.__data: 0x24a0
-  __DATA.__bss: 0x7090
-  __DATA.__common: 0x81f
+  __DATA.__bss: 0x7080
+  __DATA.__common: 0x827
   __DATA_DIRTY.__data: 0x538
   __DATA_DIRTY.__bss: 0x43460
   __DATA_DIRTY.__common: 0xc098

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 71503
-  Symbols:   21898
-  CStrings:  43089
+  Functions: 71560
+  Symbols:   21905
+  CStrings:  43090
 
Symbols:
+ __ZN4llvm17DivergenceTracker24markControlDependentPhisEPKNS_11InstructionEPNS_10BasicBlockENSt3__18functionIFvPKNS_5ValueEEEE
+ __ZNK4llvm19TargetTransformInfo21getCopyLikeDstSrcLocsEPKNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo21isIgnorableMemLikeDefEPKNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo23getSafeMemLikeAccessLocEPKNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo26getSafeStoreLikeStoredValsEPNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo27isRewritableMemLikeMiscInstEPKNS_11InstructionE
+ __ZNK4llvm19TargetTransformInfo30rewriteMemLikeWithAddressSpaceEPNS_11InstructionEj
CStrings:
+ "32023.921.5"
+ "Apple LLVM version 32023.921.5"
+ "LLVM version 32023.921.5"
+ "llvm-mc (based on LLVM 32023.921.5)"
+ "tensor_element_addrspace"
- "32023.921"
- "Apple LLVM version 32023.921"
- "LLVM version 32023.921"
- "llvm-mc (based on LLVM 32023.921)"
```
