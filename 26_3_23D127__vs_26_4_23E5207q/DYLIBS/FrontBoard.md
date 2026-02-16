## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

-1000.3.4.100.0
-  __TEXT.__text: 0x8cd34
-  __TEXT.__auth_stubs: 0xfd0
+1000.4.9.0.0
+  __TEXT.__text: 0x8a574
+  __TEXT.__auth_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x5b38
   __TEXT.__const: 0x324
-  __TEXT.__cstring: 0xb23c
+  __TEXT.__cstring: 0xb299
   __TEXT.__oslogstring: 0x5ec2
-  __TEXT.__gcc_except_tab: 0x18c8
+  __TEXT.__gcc_except_tab: 0x1448
   __TEXT.__dlopen_cstrs: 0x20a
-  __TEXT.__unwind_info: 0x21f8
+  __TEXT.__unwind_info: 0x2308
   __TEXT.__objc_classname: 0x11cf
-  __TEXT.__objc_methname: 0xf78b
+  __TEXT.__objc_methname: 0xf845
   __TEXT.__objc_methtype: 0x3847
-  __TEXT.__objc_stubs: 0xb100
+  __TEXT.__objc_stubs: 0xb1e0
   __DATA_CONST.__got: 0x8f8
-  __DATA_CONST.__const: 0x2728
+  __DATA_CONST.__const: 0x2730
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37a8
+  __DATA_CONST.__objc_selrefs: 0x37e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0x8e20
-  __AUTH_CONST.__objc_const: 0xb900
+  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__cfstring: 0x8f00
+  __AUTH_CONST.__objc_const: 0xb920
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x964
+  __DATA.__objc_ivar: 0x968
   __DATA.__data: 0x1d40
   __DATA.__bss: 0x1e8
   __DATA_DIRTY.__objc_data: 0xeb0
-  __DATA_DIRTY.__bss: 0x1b8
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 143A3C5E-0E2A-39AF-B655-82D362E7C7E6
-  Functions: 3051
-  Symbols:   10520
-  CStrings:  6040
+  UUID: E2228469-9DA8-3EED-BEFF-9ED77B47196B
+  Functions: 3191
+  Symbols:   11034
+  CStrings:  6061
 
Symbols:
+ +[FBWorkspaceDomain supportsPrimitiveAttributes]
+ +[FBWorkspaceDomain supportsPrimitiveAttributes].cold.1
+ GCC_except_table10
+ GCC_except_table23
+ GCC_except_table64
+ _BSPathForSystemDirectory
+ _FBLogShutdown
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._prefetch
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ ___33-[FBSystemService initWithQueue:]_block_invoke.33
+ ___33-[FBSystemService initWithQueue:]_block_invoke_2.35
+ ___46-[FBSystemService shutdownWithOptions:origin:]_block_invoke_7.cold.1
+ ___46-[FBSystemService shutdownWithOptions:origin:]_block_invoke_8
+ ___46-[FBSystemService shutdownWithOptions:origin:]_block_invoke_9
+ ___48+[FBWorkspaceDomain supportsPrimitiveAttributes]_block_invoke
+ ___54-[FBWorkspaceDomain endpointInjectorTargetingProcess:]_block_invoke.118
+ ___63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.180
+ ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.204
+ ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.207
+ ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.217
+ ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.233
+ ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.235
+ ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke_2.236
+ ___86-[FBSystemService _terminateProcesses:forReason:andReport:withDescription:completion:]_block_invoke.93
+ ___block_descriptor_49_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_literal_global.266
+ ___block_literal_global.312
+ ___block_literal_global.98
+ ___getCBControllerClass_block_invoke.cold.2
+ _objc_msgSend$LPMCompletionTimeoutSeconds
+ _objc_msgSend$activateWithCompletion:
+ _objc_msgSend$bs_jobLabel
+ _objc_msgSend$bs_safeDictionaryForKey:
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$stringByAppendingPathComponent:
+ _supportsPrimitiveAttributes.__PrimitiveAttributeSupported
+ _supportsPrimitiveAttributes.onceToken
- -[FBWorkspaceDomain _initWithCoupler:specification:].cold.3
- GCC_except_table4
- GCC_except_table41
- GCC_except_table42
- _CoreBluetoothLibrary
- _CoreBluetoothLibrary.cold.1
- _FBOpenAppSystemServiceExecuteCallOut.cold.5
- ___33-[FBSystemService initWithQueue:]_block_invoke.30
- ___33-[FBSystemService initWithQueue:]_block_invoke_2.32
- ___46-[FBSystemService shutdownWithOptions:origin:]_block_invoke_5.cold.1
- ___54-[FBWorkspaceDomain endpointInjectorTargetingProcess:]_block_invoke.109
- ___63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.171
- ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.198
- ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.201
- ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.211
- ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.227
- ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke.229
- ___79-[FBSystemService openApplication:withOptions:originator:requestID:completion:]_block_invoke_2.230
- ___86-[FBSystemService _terminateProcesses:forReason:andReport:withDescription:completion:]_block_invoke.87
- ___block_literal_global.260
- ___block_literal_global.303
- ___block_literal_global.74
- ___getCBControllerLowPowerModeCompletionTimeoutSecondsSymbolLoc_block_invoke
- _getCBControllerLowPowerModeCompletionTimeoutSecondsSymbolLoc.ptr
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "Entitlements"
+ "GetBluetoothTimeout"
+ "LPMCompletionTimeoutSeconds"
+ "LaunchPrefetch"
+ "RBSPrefetchPageAttribute"
+ "RunningBoard/runningboardEntitlementsConfiguration.plist"
+ "_prefetch"
+ "activateWithCompletion:"
+ "bs_jobLabel"
+ "bs_safeDictionaryForKey:"
+ "com.apple.pagein-prefetching"
+ "com.apple.runningboard.pagein-prefetching"
+ "dictionaryWithContentsOfFile:"
+ "file-read-data"
+ "fileSystemRepresentation"
+ "stringByAppendingPathComponent:"
- "CBControllerLowPowerModeCompletionTimeoutSeconds"
- "const NSInteger getCBControllerLowPowerModeCompletionTimeoutSeconds(void)"

```
