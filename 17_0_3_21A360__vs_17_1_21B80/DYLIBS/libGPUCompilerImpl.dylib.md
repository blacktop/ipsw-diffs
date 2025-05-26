## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.34.1.0.0
-  __TEXT.__text: 0x3a92d0
-  __TEXT.__auth_stubs: 0x4900
+32023.47.0.0.0
+  __TEXT.__text: 0x3d623c
+  __TEXT.__auth_stubs: 0x48c0
   __TEXT.__init_offsets: 0x48
-  __TEXT.__const: 0x167174
-  __TEXT.__cstring: 0x28c819
-  __TEXT.__unwind_info: 0x5a68
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x9bd78
-  __AUTH_CONST.__const: 0x8bc8
+  __TEXT.__const: 0x167680
+  __TEXT.__cstring: 0x28c4e9
+  __TEXT.__unwind_info: 0x4a7c
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0x9bdb0
+  __AUTH_CONST.__const: 0x79c8
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__auth_got: 0x2468
+  __AUTH_CONST.__auth_got: 0x2448
   __AUTH.__const_weak: 0x858
   __AUTH.__got_weak: 0x18
   __DATA.__got_weak: 0x838
   __DATA.__data: 0x1c
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x11
-  __DATA.__common: 0x22
-  __DATA.__bss: 0x6e9
+  __DATA.__common: 0x11
+  __DATA.__bss: 0x19
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__common: 0x608
-  __DATA_DIRTY.__bss: 0x1768
+  __DATA_DIRTY.__common: 0x380
+  __DATA_DIRTY.__bss: 0x2110
   - /usr/lib/libLLVM.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libllvm-lmdb.dylib
-  Functions: 9228
-  Symbols:   2755
-  CStrings:  14733
+  Functions: 7581
+  Symbols:   2748
+  CStrings:  14695
 
Symbols:
+ __ZN4llvm3air16NativeTargetInfoC1ERKNS_6TripleE
+ __ZN4llvm3air16NativeTargetInfoC2ERKNS_6TripleE
+ __ZN4llvm3air22createNativeTargetInfoERKNS_6TripleE
+ __ZN4llvm5airnt6Plugin9setTargetERKNS_6TripleE
+ __ZN7metalfe11GPUArchiver10canAddUnitEP7MDB_txnN4llvm5MachO12ArchitectureE
+ __ZN7metalfe11GPUArchiver12emitMetalLibEP7MDB_txnN4llvm5MachO12ArchitectureERNSt3__16vectorINS3_11SmallStringILj64EEENS6_9allocatorIS9_EEEE
+ __ZN7metalfe11GPUArchiver13addDescriptorEN4llvm5MachO12ArchitectureEPKNS1_12MemoryBufferERNS1_11raw_ostreamE
+ __ZN7metalfe11GPUArchiver7addToolEN4llvm5MachO12ArchitectureEjRKNS1_12VersionTupleERNS1_11raw_ostreamE
+ __ZN7metalfe11GPUArchiver7addUnitEN4llvm5MachO12ArchitectureEPKNS1_12MemoryBufferES6_S6_RNS1_11raw_ostreamE
+ __ZN7metalfe11GPUArchiver9emitImageEP7MDB_txnN4llvm5MachO12ArchitectureERNSt3__16vectorINS3_11SmallStringILj64EEENS6_9allocatorIS9_EEEE
+ __ZNK4llvm6object15MachOObjectFile11getHeader64Ev
+ __ZNK4llvm6object15MachOObjectFile7is64BitEv
+ __ZNK4llvm6object15MachOObjectFile9getHeaderEv
+ __ZNK4llvm6object20MachOUniversalBinary16getObjectForArchENS_9StringRefE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
- __ZN4llvm34ShouldNotRunFunctionPassesAnalysis3KeyE
- __ZN4llvm3air16NativeTargetInfoC1ERKNS_6TripleENS_5MachO14ImplementationE
- __ZN4llvm3air16NativeTargetInfoC2ERKNS_6TripleENS_5MachO14ImplementationE
- __ZN4llvm3air22createNativeTargetInfoERKNS_6TripleENS_5MachO14ImplementationE
- __ZN4llvm5MachO21getImplementationNameENS0_14ImplementationE
- __ZN4llvm5MachO25getImplementationFromNameENS_9StringRefE
- __ZN4llvm5MachO28getCPUTypeFromImplementationENS0_14ImplementationE
- __ZN4llvm5MachO33getArchitectureFromImplementationENS0_14ImplementationE
- __ZN4llvm5airnt6Plugin9setTargetERKNS_6TripleENS_5MachO14ImplementationE
- __ZN7metalfe11GPUArchiver10canAddUnitEP7MDB_txnN4llvm5MachO12ArchitectureENS4_14ImplementationE
- __ZN7metalfe11GPUArchiver12emitMetalLibEP7MDB_txnN4llvm5MachO12ArchitectureENS4_14ImplementationERNSt3__16vectorINS3_11SmallStringILj64EEENS7_9allocatorISA_EEEE
- __ZN7metalfe11GPUArchiver13addDescriptorEN4llvm5MachO12ArchitectureENS2_14ImplementationEPKNS1_12MemoryBufferERNS1_11raw_ostreamE
- __ZN7metalfe11GPUArchiver23normalizeImplementationEN4llvm5MachO12ArchitectureERNS2_14ImplementationE
- __ZN7metalfe11GPUArchiver7addToolEN4llvm5MachO12ArchitectureENS2_14ImplementationEjRKNS1_12VersionTupleERNS1_11raw_ostreamE
- __ZN7metalfe11GPUArchiver7addUnitEN4llvm5MachO12ArchitectureENS2_14ImplementationEPKNS1_12MemoryBufferES7_S7_RNS1_11raw_ostreamE
- __ZN7metalfe11GPUArchiver9emitImageEP7MDB_txnN4llvm5MachO12ArchitectureENS4_14ImplementationERNSt3__16vectorINS3_11SmallStringILj64EEENS7_9allocatorISA_EEEE
- __ZNK4llvm6object15MachOObjectFile10getCPUTypeEv
- __ZNK4llvm6object15MachOObjectFile11getFileTypeEv
- __ZNK4llvm6object15MachOObjectFile13getCPUSubTypeEv
- __ZNK4llvm6object20MachOUniversalBinary19getObjectForCpuTypeEjj
- __ZNK4llvm6object20MachOUniversalBinary21getMetalLibForCpuTypeEjj
- __ZTVN4llvm10CallbackVHE
CStrings:
+ "' arch"
+ "32023.47"
+ "?#"
+ "Architecture"
+ "MTLComputePipelineDescriptor"
+ "MTLFeatureSet"
+ "MTLFunction"
+ "MTLLibrary"
+ "MTLRenderPipelineDescriptor"
+ "bool metalfe::GPUArchiver::addDescriptor(llvm::MachO::Architecture, const llvm::MemoryBuffer *, llvm::raw_ostream &)"
+ "bool metalfe::GPUArchiver::addTool(llvm::MachO::Architecture, uint32_t, const llvm::VersionTuple &, llvm::raw_ostream &)"
+ "cannot add more units for arch '"
+ "g13c_a0"
+ "g13d_a0"
+ "g13g_a0"
+ "g13p_a0"
+ "g13s_a0"
+ "g14d_a0"
+ "g14g_a0"
+ "g14p_a0"
+ "g14s_a0"
+ "g16p_a0"
+ "g16p_b0"
+ "metalfe::GPUArchiverUnitId metalfe::GPUArchiver::addUnit(llvm::MachO::Architecture, const llvm::MemoryBuffer *, const llvm::MemoryBuffer *, const llvm::MemoryBuffer *, llvm::raw_ostream &)"
+ "pipeline built using objects of different archs: '"
+ "specialized"
+ "units for arch '"
- "' and impl '"
- "' arch/impl"
- "' for arch/impl '"
- "', "
- "(root)"
- ".aira"
- ".aird"
- ".airf"
- ".airo"
- ".airp"
- ".btnf"
- ".dylib"
- ".mtlp"
- ".rtlib"
- "32023.34"
- "APPLE_1_"
- "ArchImpl"
- "MH_CORE"
- "MH_DSYM"
- "MH_DYLIB"
- "MacOS"
- "StringRef llvm::getTypeName() [DesiredTypeName = llvm::InvalidateAnalysisPass<llvm::ShouldNotRunFunctionPassesAnalysis>]"
- "StringRef llvm::getTypeName() [DesiredTypeName = llvm::ShouldNotRunFunctionPassesAnalysis]"
- "T"
- "TvOS"
- "WatchOS"
- "XrOS"
- "_ios"
- "_iosmac"
- "_iossim"
- "_osx"
- "_read"
- "_sample"
- "_tvos"
- "_tvossim"
- "_watchos"
- "_write"
- "_xros"
- "_xrossim"
- "air-lld"
- "air-nt"
- "air-pack"
- "airr"
- "bool metalfe::GPUArchiver::addDescriptor(llvm::MachO::Architecture, llvm::MachO::Implementation, const llvm::MemoryBuffer *, llvm::raw_ostream &)"
- "bool metalfe::GPUArchiver::addTool(llvm::MachO::Architecture, llvm::MachO::Implementation, uint32_t, const llvm::VersionTuple &, llvm::raw_ostream &)"
- "cannot add descriptors to non-AIR implementation '"
- "cannot add more units for arch/impl '"
- "cpp_type"
- "depth2d"
- "hash"
- "iOS"
- "incompatible arch '"
- "key"
- "ld"
- "llong"
- "long"
- "mesh<"
- "metal"
- "metalfe::GPUArchiverUnitId metalfe::GPUArchiver::addUnit(llvm::MachO::Architecture, llvm::MachO::Implementation, const llvm::MemoryBuffer *, const llvm::MemoryBuffer *, const llvm::MemoryBuffer *, llvm::raw_ostream &)"
- "or '"
- "pipeline built using objects of different archs/impls: '"
- "private"
- "swift"
- "ullong"
- "units for arch/impl '"

```
