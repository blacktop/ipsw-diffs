## libLLVM.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libLLVM.dylib`

```diff

-  __TEXT.__text: 0x20376c0
+  __TEXT.__text: 0x202d264
   __TEXT.__init_offsets: 0x68c
-  __TEXT.__const: 0x4191150
-  __TEXT.__cstring: 0x118e82
+  __TEXT.__const: 0x4191200
+  __TEXT.__cstring: 0x11940a
   __TEXT.__oslogstring: 0x181
-  __TEXT.__unwind_info: 0x2c878
+  __TEXT.__unwind_info: 0x2d400
   __TEXT.__eh_frame: 0x3800
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x273418
   __DATA_CONST.__weak_got: 0x598
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x66588
+  __AUTH_CONST.__const: 0x66660
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0xce0
   __AUTH_CONST.__auth_got: 0x990

   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0xe75
   __DATA.__data: 0x24a0
-  __DATA.__bss: 0x63f8
-  __DATA.__common: 0x7c7
+  __DATA.__bss: 0x3e20
+  __DATA.__common: 0x7b7
   __DATA_DIRTY.__data: 0x1208
-  __DATA_DIRTY.__bss: 0x43f90
-  __DATA_DIRTY.__common: 0xc0eb
+  __DATA_DIRTY.__bss: 0x46b60
+  __DATA_DIRTY.__common: 0xc0f3
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libllvm-flatbuffers.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 72687
-  Symbols:   21890
-  CStrings:  43487
+  Functions: 72762
+  Symbols:   21893
+  CStrings:  43512
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __ZN4llvm25runInferAddressSpacesPassERNS_8FunctionERNS_9AAResultsERNS_15AssumptionCacheEPKNS_13DominatorTreeERNS_9MemorySSAEPKNS_19TargetTransformInfoEj
+ __ZN4llvm26isSafeToCastConstAddrSpaceEPKNS_8ConstantEjj
+ __ZN4llvm29runInferAddressSpacesAnalysisERNS_8FunctionERKNS_15SmallVectorImplIjEERNS_9CallGraphERNS_9AAResultsERNS_15AssumptionCacheEPKNS_13DominatorTreeERNS_9MemorySSAEPKNS_19TargetTransformInfoEj
+ __ZNK4llvm5Value33stripGenericAddrspacePointerCastsEj
- __ZN4llvm25runInferAddressSpacesPassERNS_8FunctionERNS_15AssumptionCacheEPKNS_13DominatorTreeERNS_9MemorySSAEPKNS_19TargetTransformInfoEj
CStrings:
+ "32023.920"
+ "Apple LLVM version 32023.920"
+ "Average loop iteration count used to weight instruction bonuses inside loops"
+ "Average number of recursion iterations to weight bonuses to (mutually) recursive functions"
+ "Don't specialize functions that have less than this threshold number of instructions"
+ "Ignore costs when specializing functions"
+ "LLVM version 32023.920"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_AVG_LOOP_COUNT"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_AVG_RECURSION_COUNT"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_CONCRETE_SPEEDUP_FACTOR"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_DEPENDENCY_COST_DIVISOR"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_MAX_NUM_CALL_BONUS"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_MAX_PER_FUNC"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_PHI_PREDICTION_FACTOR"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_SMALL_FN_THRESHOLD"
+ "LLVM_SPECIALIZE_ADDRESS_SPACES_SPECIALIZE_ALL"
+ "The divisor which we reduce the cost of specializations computed from the dataflow"
+ "The factor by which to reduce the bonus of uses of a phi/select for each generic incoming value"
+ "The factor which we assume builtin functions are sped up by replacing a generic argument with a concrete one"
+ "The maximum allowed number of specializations for a single function"
+ "The maximum bonus factor for a function that has many call sites"
+ "llvm-mc (based on LLVM 32023.920)"
+ "specialize-addrspaces-avg-iters-count"
+ "specialize-addrspaces-avg-recursion-count"
+ "specialize-addrspaces-calls-bonus"
+ "specialize-addrspaces-concrete-speedup"
+ "specialize-addrspaces-dependency-divisor"
+ "specialize-addrspaces-force-specialize"
+ "specialize-addrspaces-max-per-func"
+ "specialize-addrspaces-phi-prediction-factor"
+ "specialize-addrspaces-size-threshold"
- "32023.917.2"
- "Apple LLVM version 32023.917.2"
- "LLVM version 32023.917.2"
- "Set the max specialization-inference iterations to perform"
- "llvm-mc (based on LLVM 32023.917.2)"
- "specialize-addrspaces-max-iter"

```
