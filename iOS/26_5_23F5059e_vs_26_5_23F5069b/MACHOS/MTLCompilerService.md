## MTLCompilerService

> `/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService`

```diff

-372.17.0.0.0
-  __TEXT.__text: 0x41bc
-  __TEXT.__auth_stubs: 0x680
+373.2.0.0.0
+  __TEXT.__text: 0x4550
+  __TEXT.__auth_stubs: 0x670
   __TEXT.__gcc_except_tab: 0x2c8
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x556
-  __TEXT.__oslogstring: 0x3d6
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x549
+  __TEXT.__oslogstring: 0x457
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x290
-  __DATA_CONST.__auth_got: 0x348
+  __TEXT.__unwind_info: 0x2a0
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__cfstring: 0x20

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 48037C62-4D20-3D19-94B6-3ACCF92A3A7B
-  Functions: 117
-  Symbols:   823
-  CStrings:  76
+  UUID: A9566FDC-B0E1-3EC4-910B-2053828CC91F
+  Functions: 129
+  Symbols:   883
+  CStrings:  80
 
Symbols:
+ /Library/Caches/com.apple.xbs/6951381C-D06D-48F6-B531-0DBE906DFD81/TemporaryDirectory.BfAciE/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLCompilerService.o
+ /Library/Caches/com.apple.xbs/6951381C-D06D-48F6-B531-0DBE906DFD81/TemporaryDirectory.BfAciE/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLCompilerServiceMain.o
+ /Library/Caches/com.apple.xbs/6951381C-D06D-48F6-B531-0DBE906DFD81/TemporaryDirectory.BfAciE/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLCompilerServiceTimer.o
+ /Library/Caches/com.apple.xbs/6951381C-D06D-48F6-B531-0DBE906DFD81/TemporaryDirectory.BfAciE/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLConnectionCtx.o
+ /Library/Caches/com.apple.xbs/6951381C-D06D-48F6-B531-0DBE906DFD81/TemporaryDirectory.BfAciE/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLSandboxExtensionContainer.o
+ /Library/Caches/com.apple.xbs/6951381C-D06D-48F6-B531-0DBE906DFD81/TemporaryDirectory.BfAciE/Sources/Metal/CompilerService/XPCService/
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table57
+ GCC_except_table58
+ _ZN18MTLCompilerService14messageHandlerEPU24objcproto13OS_xpc_object8NSObject.cold.2
+ _ZN18MTLCompilerService20assignContextToArrayERKNSt3__110shared_ptrI21MTLCompilationContextEE.cold.1
+ _ZN18MTLCompilerService22removeContextFromArrayERKNSt3__110shared_ptrI21MTLCompilationContextEE.cold.1
+ _ZN18MTLCompilerService24getConnectionCtxInstanceEyy.cold.1
+ _ZN23CompilerPluginInterfaceC2Ei.cold.2
+ __ZN18MTLCompilerService19validateLLVMVersionEyPU24objcproto13OS_xpc_object8NSObject
+ __ZN18MTLCompilerService19validatePluginIndexEjPU24objcproto13OS_xpc_object8NSObject
+ __ZN18MTLCompilerService19validateRequestTypeEj
+ __ZN18MTLCompilerService20validateConnectionIdEyPU24objcproto13OS_xpc_object8NSObject
+ __ZN18MTLCompilerService21validateConnectionCtxEP16MTLConnectionCtxPU24objcproto13OS_xpc_object8NSObject
+ __ZN18MTLCompilerService25validateRequestDataExistsEjPKvmPU24objcproto13OS_xpc_object8NSObject
+ __ZN18MTLCompilerService33validateRequestDataPointerAndSizeEPKvmPU24objcproto13OS_xpc_object8NSObject
+ _strnlen
- /Library/Caches/com.apple.xbs/4D94BED1-9519-4233-8B59-F7B38CF29BA1/TemporaryDirectory.QVs6Wb/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLCompilerService.o
- /Library/Caches/com.apple.xbs/4D94BED1-9519-4233-8B59-F7B38CF29BA1/TemporaryDirectory.QVs6Wb/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLCompilerServiceMain.o
- /Library/Caches/com.apple.xbs/4D94BED1-9519-4233-8B59-F7B38CF29BA1/TemporaryDirectory.QVs6Wb/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLCompilerServiceTimer.o
- /Library/Caches/com.apple.xbs/4D94BED1-9519-4233-8B59-F7B38CF29BA1/TemporaryDirectory.QVs6Wb/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLConnectionCtx.o
- /Library/Caches/com.apple.xbs/4D94BED1-9519-4233-8B59-F7B38CF29BA1/TemporaryDirectory.QVs6Wb/Binaries/Metal/install/TempContent/Objects/Metal.build/MTLCompilerService.build/Objects-normal/arm64e/MTLSandboxExtensionContainer.o
- /Library/Caches/com.apple.xbs/4D94BED1-9519-4233-8B59-F7B38CF29BA1/TemporaryDirectory.QVs6Wb/Sources/Metal/CompilerService/XPCService/
- GCC_except_table23
- GCC_except_table29
- GCC_except_table37
- GCC_except_table39
- GCC_except_table42
- GCC_except_table43
- GCC_except_table45
- GCC_except_table51
- ___error
- _asprintf_l
CStrings:
+ "Failed to configure temporary directory"
+ "Invalid connection index"
+ "Invalid context index"
+ "Invalid request data size"
+ "MTLCompiler path is NULL - unsupported configuration"
+ "Request data size insufficient for operation"
- "- Could not load compiler plugin at %s"
- "Failed to configure _CS_DARWIN_USER_TEMP_DIR: %{errno}d"

```
