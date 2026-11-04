## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.922.4.0.0
-  __TEXT.__text: 0x58c6d8
+32023.925.8.0.0
+  __TEXT.__text: 0x58dc18
   __TEXT.__init_offsets: 0x50
-  __TEXT.__const: 0x2d2688
-  __TEXT.__cstring: 0x5eb44b
+  __TEXT.__const: 0x2d26b8
+  __TEXT.__cstring: 0x5eb51e
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x7f58
+  __TEXT.__unwind_info: 0x7f88
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x10ab38
+  __DATA_CONST.__const: 0x10ab40
   __DATA_CONST.__weak_got: 0x178
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xb5d8
+  __AUTH_CONST.__const: 0xb648
   __AUTH_CONST.__weak_auth_got: 0x140
-  __AUTH_CONST.__auth_got: 0x29a0
+  __AUTH_CONST.__auth_got: 0x29b8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x18
   __DATA.__data: 0x568
-  __DATA.__common: 0xd
+  __DATA.__common: 0x15
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x2340
   __DATA_DIRTY.__common: 0x388

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 9583
-  Symbols:   3770
-  CStrings:  28548
+  Functions: 9600
+  Symbols:   3777
+  CStrings:  28552
 
Symbols:
+ __ZN4llvm11Instruction10moveBeforeEPS0_
+ __ZN4llvm24ConstantFoldInstOperandsEPNS_11InstructionENS_8ArrayRefIPNS_8ConstantEEERKNS_10DataLayoutEPKNS_17TargetLibraryInfoE
+ __ZN4llvm3air29AIRResolveRequireConstantPass3runERNS_6ModuleERNS_15AnalysisManagerIS2_JEEE
+ __ZN4llvm3air32AIRDiagnosticInfoNonConstantExpr2DKE
+ __ZNK4llvm10BasicBlock27getFirstNonPHIOrDbgOrAllocaEv
+ __ZNK4llvm3air32AIRDiagnosticInfoNonConstantExpr5printERNS_17DiagnosticPrinterE
+ __ZTVN4llvm3air32AIRDiagnosticInfoNonConstantExprE
CStrings:
+ "32023.925"
+ "AIR-NT 32023.925"
+ "AIR-PACK 32023.925 (metalfe-32023.925.8)"
+ "StringRef llvm::getTypeName() [DesiredTypeName = llvm::air::AIRResolveRequireConstantPass]"
+ "air-resolve-require-constant"
+ "air.require_constant"
+ "expression could not be resolved to a constant at device compile time"
- "32023.922"
- "AIR-NT 32023.922"
- "AIR-PACK 32023.922 (metalfe-32023.922.4)"
```
