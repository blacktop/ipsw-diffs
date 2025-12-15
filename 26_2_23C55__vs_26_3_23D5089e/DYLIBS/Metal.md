## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

```diff

-370.64.2.0.0
-  __TEXT.__text: 0x1daee0
+371.5.0.0.0
+  __TEXT.__text: 0x1dae58
   __TEXT.__auth_stubs: 0x1d10
   __TEXT.__objc_methlist: 0x1dfb4
-  __TEXT.__gcc_except_tab: 0xb410
-  __TEXT.__cstring: 0x2252c
+  __TEXT.__gcc_except_tab: 0xb40c
+  __TEXT.__cstring: 0x22506
   __TEXT.__const: 0x2d160
   __TEXT.__oslogstring: 0x1e66
   __TEXT.__ustring: 0x1be

   - /usr/lib/libcompression.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 170CAA47-530E-39B3-98D1-2262F0FF9B93
+  UUID: 05D321E6-D56B-348D-9070-8DFA2B820E66
   Functions: 12959
   Symbols:   40793
-  CStrings:  15883
+  CStrings:  15882
 
Symbols:
+ ___block_literal_global.1992
+ ___block_literal_global.2018
- ___block_literal_global.1993
- ___block_literal_global.2019
Functions:
~ __ZN17MTLLibraryBuilder35initLibraryContainerWithRequestDataEP19MTLLibraryContainerR21MTLLibraryRequestDataP11objc_objectU13block_pointerFvvE : 2804 -> 2772
~ __ZL16downgradeRequestPK26MTLCompilerFunctionRequestjPU27objcproto16OS_dispatch_data8NSObjectRK12MTLUINT256_tP11objc_objectU13block_pointerFv16MTLCompilerErrorS4_PKcE : 780 -> 764
~ __ZN17MTLLibraryBuilder17newLibraryWithDAGEP8NSStringP7NSArrayIPU22objcproto11MTLFunction11objc_objectEU13block_pointerFvPU21objcproto10MTLLibrary11objc_objectP7NSErrorEbNSt3__110shared_ptrINSD_6vectorI21stitchedAirDescriptorNSD_9allocatorISG_EEEEEEmPS2_IPU27objcproto16MTLBinaryArchive11objc_objectESM_P11objc_object : 1928 -> 1912
~ -[_MTLFunctionInternal newSpecializedFunctionWithDescriptor:destinationArchive:functionCache:sync:compilerTask:completionHandler:] : 2512 -> 2496
~ -[MTLCompiler generateMachOWithID:binaryEntries:machOSpecializedData:machOType:Path:platform:bitcodeList:compilerTask:completionHandler:] : 3940 -> 3924
~ -[MTLCompiler createBinaryArchiveAsRecompileTarget:compilerTask:completionHandler:] : 632 -> 616
~ -[MTLCompiler compileFunctionRequestInternal:frameworkLinking:linkDataSize:reflectionOnly:compilerTask:completionHandler:] : 9156 -> 9144
~ -[MTLCompiler compileStatelessFunctionRequest:reflectionOnly:compilerTask:completionHandler:] : 3292 -> 3280
CStrings:
+ "00:33:54"
+ "Dec  6 2025"
+ "Dec  6 2025 00:33:54"
- "19:11:32"
- "MTL_DISABLE_MULTITHREADED_COMPILATION"
- "Nov  8 2025"
- "Nov  8 2025 19:11:32"

```
