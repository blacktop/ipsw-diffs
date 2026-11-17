## MTLCompiler

> `/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler`

```diff

-384.5.0.0.0
-  __TEXT.__text: 0xb7c00
-  __TEXT.__gcc_except_tab: 0xa6c4
+384.7.0.0.0
+  __TEXT.__text: 0xb7fc4
+  __TEXT.__gcc_except_tab: 0xa6dc
   __TEXT.__const: 0x1288
-  __TEXT.__cstring: 0x9841
-  __TEXT.__oslogstring: 0x4e7
-  __TEXT.__unwind_info: 0x3350
+  __TEXT.__cstring: 0x9922
+  __TEXT.__oslogstring: 0x53d
+  __TEXT.__unwind_info: 0x3358
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2155
-  Symbols:   3451
-  CStrings:  1653
+  Functions: 2157
+  Symbols:   3452
+  CStrings:  1660
 
Symbols:
+ GCC_except_table327
+ GCC_except_table333
+ GCC_except_table337
+ GCC_except_table342
+ GCC_except_table352
+ GCC_except_table355
+ GCC_except_table358
+ GCC_except_table360
+ GCC_except_table368
+ GCC_except_table374
+ GCC_except_table376
+ GCC_except_table379
+ GCC_except_table393
+ GCC_except_table404
+ GCC_except_table428
+ GCC_except_table432
+ GCC_except_table441
+ GCC_except_table447
+ GCC_except_table459
+ GCC_except_table468
+ GCC_except_table475
+ GCC_except_table489
+ GCC_except_table491
+ GCC_except_table504
+ GCC_except_table506
+ GCC_except_table512
+ GCC_except_table518
+ GCC_except_table529
+ GCC_except_table532
+ GCC_except_table535
+ GCC_except_table538
+ __ZNSt3__16vectorIPcNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
- GCC_except_table326
- GCC_except_table332
- GCC_except_table336
- GCC_except_table341
- GCC_except_table350
- GCC_except_table353
- GCC_except_table356
- GCC_except_table359
- GCC_except_table366
- GCC_except_table373
- GCC_except_table375
- GCC_except_table378
- GCC_except_table391
- GCC_except_table402
- GCC_except_table427
- GCC_except_table431
- GCC_except_table437
- GCC_except_table445
- GCC_except_table458
- GCC_except_table465
- GCC_except_table474
- GCC_except_table487
- GCC_except_table490
- GCC_except_table502
- GCC_except_table505
- GCC_except_table510
- GCC_except_table514
- GCC_except_table525
- GCC_except_table531
- GCC_except_table534
- GCC_except_table536
Functions:
~ __ZL22parseFunctionConstantsRN4llvm11LLVMContextEPKcmPj : 336 -> 368
~ __ZN17MTLCompilerObject20storeToBinaryArchiveEP29MTLBuildBinariesRequestHeadermRK20ReadModuleParametersRK24BackendCompilationOutput15MTLFunctionTypeR21FrameworkPassesOutputRKP20MTLOpaqueGPUArchiverPPc : 1740 -> 1928
~ __ZN17MTLCompilerObject13generateMachOEPKvmU13block_pointerFvjS1_mPKcE : 4844 -> 5468
+ __ZL22parseFunctionConstantsRN4llvm11LLVMContextEPKcmPj.cold.1
+ __ZN17MTLCompilerObject13generateMachOEPKvmU13block_pointerFvjS1_mPKcE.cold.1
CStrings:
+ "Failed to allocate MachO binary request entries"
+ "Failed to allocate function constants"
+ "Invalid pipeline archiver unit id"
+ "Invalid visible function request count"
+ "MachO entry %llu reflection block out of bounds"
+ "Unknown linked bitcode hash in MachO binary request"
+ "Visible function hashes do not match the tools list"
```
