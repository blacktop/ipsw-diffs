## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

-27060.1.0.0.0
-  __TEXT.__text: 0x9e8bc
+27062.0.0.0.0
+  __TEXT.__text: 0x9edac
   __TEXT.__const: 0x1978
-  __TEXT.__cstring: 0x12499
-  __TEXT.__unwind_info: 0x35b0
-  __DATA_CONST.__const: 0x5590
+  __TEXT.__cstring: 0x124de
+  __TEXT.__unwind_info: 0x35b8
+  __DATA_CONST.__const: 0x55b0
   __AUTH_CONST.__const: 0x2758
   __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x148

   __DATA_DIRTY.__bss: 0x1bc0
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 3421
-  Symbols:   3268
-  CStrings:  2243
+  Functions: 3423
+  Symbols:   3271
+  CStrings:  2244
 
Symbols:
+ __ZN3lsl6VectorIPKN5dyld46LoaderEE7reserveEy
+ __ZZNK5dyld46Loader17hasExportedSymbolER11DiagnosticsRNS_12RuntimeStateEPKcNS0_18ExportedSymbolModeENS0_12ResolverModeEPNS0_14ResolvedSymbolEbPN5dyld35ArrayIPKS0_EEENK3$_0clEv
+ ____ZN3lsl13MemoryManager22withReadOnlyTPROMemoryIZNK5dyld46Loader17hasExportedSymbolER11DiagnosticsRNS2_12RuntimeStateEPKcNS3_18ExportedSymbolModeENS3_12ResolverModeEPNS3_14ResolvedSymbolEbPN5dyld35ArrayIPKS3_EEE3$_0EEN13callback_impl11return_typeIDTadsrT_onclEE4typeESN__block_invoke
CStrings:
+ "/System/ExclaveKit/usr/lib/libobjc.A.dylib"
+ "27062"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Aug  5 21:46:56 PDT 2026; root:libignition-64~17995/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Wed Aug  5 21:46:56 PDT 2026; root:libignition-64~17995/libignition_core/RELEASE_ARM64E"
+ "{ProtectedStackReturnType=(?=QiB^v**^?{PseudoDylibSymbolLookup=QQ})}8@?0"
- "27060.1"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Jul 14 21:12:31 PDT 2026; root:libignition-64~11776/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Tue Jul 14 21:12:31 PDT 2026; root:libignition-64~11776/libignition_core/RELEASE_ARM64E"
- "{ProtectedStackReturnType=(?=QiB^v**^?)}8@?0"
```
