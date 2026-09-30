## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.3.7.0.0
-  __TEXT.__text: 0x1200e54
-  __TEXT.__auth_stubs: 0x20f0
-  __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x778ec
-  __TEXT.__cstring: 0x90fb9
-  __TEXT.__gcc_except_tab: 0x6dcc4
-  __TEXT.__oslogstring: 0x15ffe
-  __TEXT.__unwind_info: 0x38c80
-  __TEXT.__eh_frame: 0x11b4
+8.3.8.0.0
+  __TEXT.__text: 0x125a4f0
+  __TEXT.__auth_stubs: 0x2140
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__const: 0x77e6c
+  __TEXT.__cstring: 0x915bf
+  __TEXT.__gcc_except_tab: 0x6e1e4
+  __TEXT.__oslogstring: 0x1611d
+  __TEXT.__unwind_info: 0x39338
+  __TEXT.__eh_frame: 0x2488
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3630
-  __AUTH_CONST.__auth_got: 0x1080
+  __AUTH_CONST.__auth_got: 0x10a8
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71f68
+  __AUTH_CONST.__const: 0x71c88
   __AUTH_CONST.__cfstring: 0x7f60
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
   __AUTH.__thread_bss: 0x16c
-  __DATA.__data: 0x6850
-  __DATA.__bss: 0xad98
+  __DATA.__data: 0x6890
+  __DATA.__bss: 0xad60
   __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__common: 0x38
-  __DATA_DIRTY.__bss: 0xfa0
+  __DATA_DIRTY.__bss: 0xee0
+  __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 72514
-  Symbols:   84893
-  CStrings:  15674
+  Functions: 72874
+  Symbols:   85357
+  CStrings:  15689
 
Symbols:
+ __ZNKSt3__14__fs10filesystem4path10__filenameEv
+ __ZNKSt3__14__fs10filesystem4path13__parent_pathEv
+ __ZNSt3__14__fs10filesystem8__removeERKNS1_4pathEPNS_10error_codeE
+ _fmodf
+ _logf
CStrings:
+ " already exists"
+ " must be 0D tensor of mps native type values or 1D tensor of mps native type values or unranked tensor of mps native type values, but got "
+ " must be 4D/5D memref of 32-bit float or 16-bit float or 8-bit signed integer or 8-bit unsigned integer values, but got "
+ "Attempting to attach an interface to an unregistered operation "
+ "Call to ZinTensorFormatGetSizeInBytes API failed.\n"
+ "Compressed node set must be larger that 1"
+ "Error in getting tensor format size in bytes"
+ "Error: Cannot find the populated ANECIR file %!s(MISSING)"
+ "Error: Could not complete optimized dynamic conv lowering. Failure when lowering NEKernelRasterizer."
+ "Error: The number of generated ANECIR files doesn't match the number of functions in the MLIR module."
+ "Error: Unable to merge with cast\n"
+ "Failed to set mir info when lowering NECrossCorrelation with optimization."
+ "Failure in graph manipulation when creating NEConv layers during optimized lowering of NECrossCorrelation layer"
+ "Force the pass to overwrite any files that already exist. Testing only."
+ "Graph manipulation failure during SplitKernelTensor."
+ "If true, the ANEC macho procedure will follow the MPS host function name. If false, it will use the ANEC region symbol name instead."
+ "Invalid attribute `file_path` in property conversion: "
+ "Invalid attribute `file_symbol` in property conversion: "
+ "Invalid attribute `offset` in property conversion: "
+ "Invalid attribute `result_type` in property conversion: "
+ "Invalid multi-procedure plist from the source MLIR-MPS"
+ "Kernel input layer must be of the type NEKernelRasterizer when performing optimized lowering of NECrossCorrelation"
+ "MIR Prepare Layers: Dynamic conv lowering failed!\n"
+ "Mismatch of optional return type and operand element type."
+ "Missing destination directory"
+ "NECrossCorrelation layer must have 2 incoming layers."
+ "Optimized NEKernelRasterizer lowering only works for UnfoldedChannels kernel rasterizer type."
+ "Optional return type cannot be a float type."
+ "Preserving outputs did not converge."
+ "Proposed region could not be verified\n"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::(anonymous namespace)::ConvertElementwiseUnary<mlir::mps::ReciprocalSquareRootOp, mlir::anec::Rsqrt>]"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::UpgraderInterface::Trait<Empty>]"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::detail::GetCoordOpGenericAdaptorBase::Properties]"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::detail::ReadDataFromFileOpGenericAdaptorBase::Properties]"
+ "The directory in which to place generated plists and the weights file."
+ "The pass will add `name` attribute to every anec op, which correspond to the unit name. It's only usefull for debugging. If false, all those attributes are erased."
+ "The prefix name for the generated plists and the weights file."
+ "Unsupported ANE architecture"
+ "Write multi function output for ANEC dialect"
+ "WriteMultiFunctionPass"
+ "ZinTensorFormatGetSizeInBytes API call returned error"
+ "ZinTensorFormatGetSizeInBytes API call was unsuccessful.\n"
+ "ZinTensorFormatGetSizeInBytes() failed"
+ "_ane_region_"
+ "arithmeticBinaryTileKernelType"
+ "cast_pattern"
+ "destination-directory"
+ "erase\n"
+ "expected key entry for file_path in DictionaryAttr to set Properties."
+ "expected key entry for offset in DictionaryAttr to set Properties."
+ "failed to downgrade: requested target version is {0}, axis != 1 only supported from version {1}"
+ "failed to downgrade: requested target version is {0}, but return type other than si32 is only supported from version {1}"
+ "family"
+ "file_path"
+ "file_symbol"
+ "incorrect version of the operation"
+ "merge_cast"
+ "mps.read_data_from_file"
+ "mps.reciprocal_square_root"
+ "network"
+ "op_pattern"
+ "output_file_name_prefix"
+ "plist"
+ "procedure_name"
+ "requires attribute 'file_path'"
+ "result_type"
+ "use-function-name-for-anec-procedure"
+ "weights"
+ "write-multi-function"
- " exists already."
- " inputs, "
- " outputs)"
- "/Library/Caches/com.apple.xbs/Sources/ANECompiler/ext/mlir/mlir-mps/src/Dialect/ANEC/Serde/Builder.cpp"
- "Bundle name of the framework or application owning the model being compiled.If not provided, no debug info will be added to the plist."
- "Call to ZinTensorFormatGetSize API failed.\n"
- "Error: Could not successfully MLIR converted output file \"%!s(MISSING)\"."
- "Force the pass to overwrite any files that already exist. DANGER"
- "Generate ANEC IR ProcedureList (single macho)"
- "Missing filename and directory, one or the other must be specified."
- "Only support uint8, int8, fp16, and fp32"
- "StringRef llvm::getTypeName() [DesiredTypeName = mlir::(anonymous namespace)::ConvertElementwiseUnary<mlir::mps::ReverseSquareRootOp, mlir::anec::Rsqrt>]"
- "StringRef llvm::getTypeName() [DesiredTypeName = mlir::anec::(anonymous namespace)::WriteProcedureListPlistPass]"
- "The directory in which to place generated plists."
- "The filename for the plist to be produced."
- "The number of ANE I/O exceededs fvmlib limit of 255 total ("
- "The pass add `name` attribute to every anec op, which correspond to the unit name. It's only usefull for debugging. If false, all those attributes are erased."
- "Write the ANEC dialect to a plist"
- "WriteA11LegacyPlistPass"
- "WriteA12PlistPass"
- "WriteA13PlistPass"
- "WriteA14PlistPass"
- "WriteA15PlistPass"
- "WriteA16PlistPass"
- "WriteA17PlistPass"
- "ZinTensorFormatGetSize API call returned error"
- "ZinTensorFormatGetSize API call was unsuccessful.\n"
- "ZinTensorFormatGetSize() failed"
- "_A11Legacy_region_"
- "_A12_region_"
- "_A13_region_"
- "_A14_region_"
- "_A15_region_"
- "_A16_region_"
- "_A17_region_"
- "__ane_proc_op"
- "anec-enable-procedurelist"
- "archive"
- "bundle-name"
- "cl::location(x) specified more than once!"
- "data_size"
- "mpsx.file_backed_constant"
- "network.weights"
- "plist-directory"
- "plist-filename"
- "requires attribute 'archive'"
- "requires attribute 'data_size'"
- "write-A11Legacy-plist"
- "write-A12-plist"
- "write-A13-plist"
- "write-A14-plist"
- "write-A15-plist"
- "write-A16-plist"
- "write-A17-plist"

```
