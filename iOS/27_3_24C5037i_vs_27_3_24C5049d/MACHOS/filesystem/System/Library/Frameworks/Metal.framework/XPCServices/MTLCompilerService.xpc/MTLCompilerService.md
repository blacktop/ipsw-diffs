## MTLCompilerService

> `/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`

```diff

-384.5.0.0.0
-  __TEXT.__text: 0x4740
-  __TEXT.__auth_stubs: 0x670
+384.7.0.0.0
+  __TEXT.__text: 0x5aa8
+  __TEXT.__auth_stubs: 0x680
   __TEXT.__gcc_except_tab: 0x320
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x457
-  __TEXT.__cstring: 0x544
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__oslogstring: 0x455
+  __TEXT.__cstring: 0x9f4
+  __TEXT.__unwind_info: 0x3d8
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0xb8
   __DATA.__data: 0x560
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 129
-  Symbols:   307
-  CStrings:  78
+  Functions: 164
+  Symbols:   313
+  CStrings:  133
 
Symbols:
+ GCC_except_table38
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table68
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __ZL13MTLBlobRejectPKc
+ __ZNK18MTLRequestBlobView12checkCStringEyy
+ _memchr
- GCC_except_table36
- GCC_except_table41
- GCC_except_table46
- GCC_except_table47
- GCC_except_table54
- GCC_except_table58
- GCC_except_table62
- GCC_except_table65
- GCC_except_table66
CStrings:
+ "Invalid request data"
+ "Request blob validation failed: %{public}s"
+ "airScript"
+ "archiveID"
+ "archiveID header does not fit requestSize"
+ "archiveID.archiverBasePath"
+ "archiverBasePath"
+ "binaryArchiveID"
+ "binaryRequest.bitCode"
+ "binaryRequest.functionName"
+ "binaryRequest.pluginData"
+ "buildBinaries header does not fit requestSize"
+ "buildLibraryFromSource header does not fit requestSize"
+ "builtin header does not fit requestSize"
+ "builtinScript"
+ "cispi header does not fit requestSize"
+ "cispi.funcInfo"
+ "cispi.funcInfo.arguments"
+ "cispi.funcInfo.moduleIndex"
+ "cispi.funcNames"
+ "cispi.module.bitCode"
+ "cispi.moduleInfo"
+ "dylibInstallName"
+ "entries array exceeds requestSize"
+ "entry.airScript"
+ "entry.binary"
+ "entry.bitCode"
+ "entry.bitcodeHashList"
+ "entry.hashes"
+ "entry.reflectionBlock"
+ "entry.tools"
+ "gpuCompilerSPIOptions"
+ "hashes"
+ "header does not fit requestSize"
+ "libFromSource.align overflow"
+ "libFromSource.linkedAir"
+ "libFromSource.linkedAir blobSize"
+ "libFromSource.linkedAir size prefix"
+ "libFromSource.options"
+ "libFromSource.options cstring"
+ "libFromSource.source"
+ "libFromSource.source cstring"
+ "libFromSource.unaligned blob"
+ "linkData"
+ "mtlScript"
+ "overrideTriple"
+ "pipelineArchUnitId"
+ "pipelineData"
+ "pipelineList"
+ "privateVisibleFunctionRequests"
+ "requestData"
+ "sandboxExt"
+ "specializedName"
+ "tools"
+ "uniqueBitcodeList"
+ "visibleFunctionGroup"
+ "visibleFunctionRequests"
- "Invalid request data size"
- "Request data size insufficient for operation"
```
