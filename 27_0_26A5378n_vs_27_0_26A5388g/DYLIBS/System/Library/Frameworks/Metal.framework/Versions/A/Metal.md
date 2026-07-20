## Metal

> `/System/Library/Frameworks/Metal.framework/Versions/A/Metal`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-382.4.0.0.0
-  __TEXT.__text: 0x1f8778
-  __TEXT.__objc_methlist: 0x1f824
+382.5.0.0.0
+  __TEXT.__text: 0x1f8a94
+  __TEXT.__objc_methlist: 0x1f834
   __TEXT.__cstring: 0x23f0c
-  __TEXT.__gcc_except_tab: 0xc578
+  __TEXT.__gcc_except_tab: 0xc57c
   __TEXT.__const: 0x2d7b0
   __TEXT.__oslogstring: 0x2400
   __TEXT.__ustring: 0x1be
-  __TEXT.__unwind_info: 0x8e18
+  __TEXT.__unwind_info: 0x8e20
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x93f0
+  __DATA_CONST.__objc_selrefs: 0x9418
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xc38
-  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0xa68
-  __AUTH_CONST.__const: 0x6e98
+  __AUTH_CONST.__const: 0x6ed8
   __AUTH_CONST.__cfstring: 0x13640
-  __AUTH_CONST.__objc_const: 0x48450
+  __AUTH_CONST.__objc_const: 0x48480
   __AUTH_CONST.__weak_auth_got: 0x30
-  __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xef0
+  __AUTH_CONST.__auth_got: 0xef8
   __AUTH.__objc_data: 0x4420
-  __DATA.__objc_ivar: 0x2358
+  __DATA.__objc_ivar: 0x235c
   __DATA.__data: 0x4498
-  __DATA.__bss: 0x3c4
+  __DATA.__bss: 0x3e4
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x4240
   __DATA_DIRTY.__data: 0x108

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13962
-  Symbols:   26236
+  Functions: 13967
+  Symbols:   26249
   CStrings:  4694
 
Symbols:
+ -[_MTL4MachineLearningCommandEncoder agentMask]
+ OBJC_IVAR_$__MTL4MachineLearningCommandEncoder._agentMask
+ _ZN24MTLXPCCompilerConnection12setupSandboxEhb
+ _ZN30MTLLegacyXPCCompilerConnection12setupSandboxEhb
+ __ZN24MTLXPCCompilerConnection12setupSandboxEhb
+ __ZN26MTLArchiveLinkResolverImpl21readFlatbufferInPlaceEjRj
+ __ZN30MTLLegacyXPCCompilerConnection12setupSandboxEhb
+ __ZZN24MTLXPCCompilerConnection12setupSandboxEhbE15openCLOnceToken
+ __ZZN24MTLXPCCompilerConnection12setupSandboxEhbE23fromSourceSandboxTokens
+ __ZZN24MTLXPCCompilerConnection12setupSandboxEhbE23gpuArchiverSandboxToken
+ __ZZN24MTLXPCCompilerConnection12setupSandboxEhbE29fromSourceOpenCLSandboxTokens
+ __ZZN24MTLXPCCompilerConnection12setupSandboxEhbE9onceToken
+ __ZZN30MTLLegacyXPCCompilerConnection12setupSandboxEhbE15openCLOnceToken
+ __ZZN30MTLLegacyXPCCompilerConnection12setupSandboxEhbE23fromSourceSandboxTokens
+ __ZZN30MTLLegacyXPCCompilerConnection12setupSandboxEhbE23gpuArchiverSandboxToken
+ __ZZN30MTLLegacyXPCCompilerConnection12setupSandboxEhbE29fromSourceOpenCLSandboxTokens
+ __ZZN30MTLLegacyXPCCompilerConnection12setupSandboxEhbE9onceToken
+ ____ZN24MTLXPCCompilerConnection12setupSandboxEhb_block_invoke
+ ____ZN24MTLXPCCompilerConnection12setupSandboxEhb_block_invoke_2
+ ____ZN30MTLLegacyXPCCompilerConnection12setupSandboxEhb_block_invoke
+ ____ZN30MTLLegacyXPCCompilerConnection12setupSandboxEhb_block_invoke_2
+ _objc_msgSend$setAneBondedCompileMode:
+ _objc_msgSend$setAneProcedureExecutionMode:
+ _objc_msgSend$setEnableANEFWToFWSignal:
+ _objc_msgSend$setEnableANELateLatch:
+ _xpc_copy
- _ZN24MTLXPCCompilerConnection12setupSandboxEh
- _ZN30MTLLegacyXPCCompilerConnection12setupSandboxEh
- __ZN24MTLXPCCompilerConnection12setupSandboxEh
- __ZN26MTLArchiveLinkResolverImpl21readFlatbufferInPlaceEj
- __ZN30MTLLegacyXPCCompilerConnection12setupSandboxEh
- __ZZN24MTLXPCCompilerConnection12setupSandboxEhE23fromSourceSandboxTokens
- __ZZN24MTLXPCCompilerConnection12setupSandboxEhE23gpuArchiverSandboxToken
- __ZZN24MTLXPCCompilerConnection12setupSandboxEhE9onceToken
- __ZZN30MTLLegacyXPCCompilerConnection12setupSandboxEhE23fromSourceSandboxTokens
- __ZZN30MTLLegacyXPCCompilerConnection12setupSandboxEhE23gpuArchiverSandboxToken
- __ZZN30MTLLegacyXPCCompilerConnection12setupSandboxEhE9onceToken
- ____ZN24MTLXPCCompilerConnection12setupSandboxEh_block_invoke
- ____ZN30MTLLegacyXPCCompilerConnection12setupSandboxEh_block_invoke
CStrings:
+ "00:41:55"
+ "Jul 11 2026"
+ "Jul 11 2026 00:41:55"
- "03:00:10"
- "Jun 27 2026"
- "Jun 27 2026 03:00:10"
```
