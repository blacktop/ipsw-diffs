## AGXCompilerCore

> `/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore`

```diff

-  __TEXT.__text: 0x228aa8
-  __TEXT.__auth_stubs: 0x2820
+  __TEXT.__text: 0x2287b0
+  __TEXT.__auth_stubs: 0x2810
   __TEXT.__const: 0x39d38
-  __TEXT.__cstring: 0x1b071
+  __TEXT.__cstring: 0x1b026
   __TEXT.__oslogstring: 0x456
   __TEXT.__unwind_info: 0x3eb0
   __TEXT.__objc_methname: 0xa2

   __DATA_CONST.__const: 0x78f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1418
+  __AUTH_CONST.__auth_got: 0x1410
   __AUTH_CONST.__const: 0x706e8
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH.__data: 0x50

   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7261
-  Symbols:   19336
-  CStrings:  4566
+  Symbols:   19335
+  CStrings:  4564
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH.__data : content changed
Symbols:
- __ZN4llvm11raw_ostreamlsEm
Functions:
~ __ZN4llvm6detail9PassModelINS_6ModuleE29DeduplicateGlobalBindingsPassNS_17PreservedAnalysesENS_15AnalysisManagerIS2_JEEEJEE3runERS2_RS6_ : 2760 -> 1856
~ __ZL23pluginSupportsOSVersion12AGCOSVersion : 100 -> 120
~ __ZN27ReplaceTensorIntrinsicsPass36processVectorizedLoadStoreIntrinsicsERN4llvm6ModuleEP17AGCLLVMUserObjectP20AGCLLVMTargetBuilderRKNSt3__16vectorI22TensorOperationContextNS7_9allocatorIS9_EEEE : 4076 -> 4200
CStrings:
+ "start_offset"
+ "valid_count"
+ "valid_end"
- "' has type "
- ", duplicate '"
- ": "
- "First occurrence '"
- "Type mismatch for duplicate global bindings at binding index "

```
