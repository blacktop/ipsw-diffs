## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.332.0.0.0
-  __TEXT.__text: 0x447938
-  __TEXT.__auth_stubs: 0x4cf0
+32023.330.0.0.0
+  __TEXT.__text: 0x446280
+  __TEXT.__auth_stubs: 0x4c60
   __TEXT.__init_offsets: 0x48
-  __TEXT.__const: 0x1b0420
-  __TEXT.__cstring: 0x32435f
+  __TEXT.__const: 0x1b03f0
+  __TEXT.__cstring: 0x3242b4
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x4a90
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0xb2a60
-  __AUTH_CONST.__auth_got: 0x2678
+  __TEXT.__unwind_info: 0x4a88
+  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__const: 0xb2a48
+  __AUTH_CONST.__auth_got: 0x2630
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__const: 0x8cd8
   __AUTH.__thread_vars: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 7719
-  Symbols:   3042
-  CStrings:  93875
+  Functions: 7708
+  Symbols:   3025
+  CStrings:  93871
 
Symbols:
+ __ZN4llvm3air12MachOBuilder24getOrCreateObjectSymbolsERN10llvm_utils16PackedMCStreamerENS_8ArrayRefIPKNS1_14ModuleLocationEEEPKNS1_10DescriptorE
- __ZN4llvm12LoopAnalysis3KeyE
- __ZN4llvm16AnalysisResolver12findImplPassEPNS_4PassEPKvRNS_8FunctionE
- __ZN4llvm19LoopInfoWrapperPass2IDE
- __ZN4llvm22TracepointLoopCallInst7classofEPKNS_11InstructionE
- __ZN4llvm33initializeLoopInfoWrapperPassPassERNS_12PassRegistryE
- __ZN4llvm3air12MachOBuilder24getOrCreateObjectSymbolsERN10llvm_utils16PackedMCStreamerEPKNS1_15object_iterator10value_typeE
- __ZN4llvm3air19dropAIRDyldLibTableERNS_6ModuleE
- __ZN4llvm3air19dropAIRDyldStrTableERNS_6ModuleE
- __ZN4llvm3air20dropAIRDyldFlatTableERNS_6ModuleE
- __ZN4llvm9MCContext16createTempSymbolEv
- __ZN7metalfe11GPUArchiver18keepPackingSymbolsERN4llvm11raw_ostreamE
- __ZN7metalfe12METADatabase24KEEP_PACKING_SYMBOLS_KEYE
- __ZNK4llvm10BasicBlock14getFirstNonPHIEv
- __ZNK4llvm12LoopInfoBaseINS_10BasicBlockENS_4LoopEE18getLoopsInPreorderEv
- __ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE12getLoopLatchEv
- __ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE16getLoopPreheaderEv
- __ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE19getUniqueExitBlocksERNS_15SmallVectorImplIPS1_EE
- __ZNSt3__111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE
CStrings:
+ "32023.330"
+ "cannot materialize module in '"
- "32023.332"
- "KeepPackingSymbols"
- "bool metalfe::GPUArchiver::keepPackingSymbols(llvm::raw_ostream &)"
- "cannot materialize metadata in '"
- "cannot read 'META::KeepPackingSymbols': "
- "cannot write 'META::KeepPackingSymbols': "

```
