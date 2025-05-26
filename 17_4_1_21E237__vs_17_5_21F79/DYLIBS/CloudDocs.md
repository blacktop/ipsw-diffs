## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-2720.100.117.0.0
-  __TEXT.__text: 0x8e908
-  __TEXT.__auth_stubs: 0x13a0
-  __TEXT.__objc_methlist: 0x5178
+2720.120.29.0.0
+  __TEXT.__text: 0x8ebb0
+  __TEXT.__auth_stubs: 0x1390
+  __TEXT.__objc_methlist: 0x51b0
   __TEXT.__const: 0x118
   __TEXT.__gcc_except_tab: 0x42f8
-  __TEXT.__cstring: 0xb216
-  __TEXT.__oslogstring: 0x9757
+  __TEXT.__cstring: 0xb238
+  __TEXT.__oslogstring: 0x9731
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2474
-  __TEXT.__objc_classname: 0xdb3
-  __TEXT.__objc_methname: 0x10957
-  __TEXT.__objc_methtype: 0x4136
-  __TEXT.__objc_stubs: 0xb080
+  __TEXT.__unwind_info: 0x2438
+  __TEXT.__objc_classname: 0xdc2
+  __TEXT.__objc_methname: 0x109d5
+  __TEXT.__objc_methtype: 0x4149
+  __TEXT.__objc_stubs: 0xb0c0
   __DATA_CONST.__got: 0x528
-  __DATA_CONST.__const: 0x27a8
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __DATA_CONST.__const: 0x27f8
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe248
-  __DATA_CONST.__objc_selrefs: 0x3b78
+  __DATA_CONST.__objc_const: 0xe290
+  __DATA_CONST.__objc_selrefs: 0x3b90
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_classrefs: 0x420
+  __DATA_CONST.__objc_classrefs: 0x428
   __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__cfstring: 0x5940
   __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__objc_const: 0x2840
+  __AUTH_CONST.__objc_const: 0x2888
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0x9e0
+  __AUTH_CONST.__auth_got: 0x9d8
   __AUTH.__objc_data: 0x1270
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x624
-  __DATA.__data: 0x11d8
-  __DATA.__bss: 0x240
+  __DATA.__data: 0x1200
+  __DATA.__bss: 0x218
   __DATA.__common: 0x0
-  __DATA_DIRTY.__objc_data: 0xa00
+  __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3190
-  Symbols:   10649
-  CStrings:  5468
+  Functions: 3197
+  Symbols:   10671
+  CStrings:  5471
 
Symbols:
+ +[BRPersonaUtils performWithPersonaID:block:]
+ +[BRXPCClientUtils executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:]
+ -[NSArray(BRAdditions) _br_minMaxWithMax:comparator:]
+ -[NSError(BRAdditions) br_errorDescription]
+ -[NSURL(BRAdditions_Private) br_isIgnoredByFileProviderWithError:]
+ _OBJC_CLASS_$_BRPersonaUtils
+ _OBJC_METACLASS_$_BRPersonaUtils
+ __OBJC_$_CLASS_METHODS_BRPersonaUtils
+ __OBJC_CLASS_RO_$_BRPersonaUtils
+ __OBJC_METACLASS_RO_$_BRPersonaUtils
+ ___53-[NSArray(BRAdditions) _br_minMaxWithMax:comparator:]_block_invoke
+ ___76+[BRXPCClientUtils executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:]_block_invoke
+ ___76+[BRXPCClientUtils executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:]_block_invoke_2
+ ___76+[BRXPCClientUtils executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:]_block_invoke_2.cold.1
+ ___block_descriptor_56_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48bs_e17_v16?0"NSError"8ls40l8s32l8s48l8
+ _objc_msgSend$_br_minMaxWithMax:comparator:
+ _objc_msgSend$br_isIgnoredByFileProviderWithError:
+ _objc_msgSend$executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:
+ _objc_msgSend$performWithPersonaID:block:
- -[NSArray(BRAdditions) _br_minMaxWithMax:comperator:]
- ___53-[NSArray(BRAdditions) _br_minMaxWithMax:comperator:]_block_invoke
- _objc_msgSend$_br_minMaxWithMax:comperator:
- _objc_msgSend$fp_prettyPath
- _openat
CStrings:
+ "+[BRXPCClientUtils executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:]_block_invoke_2"
+ "-[NSURL(BRAdditions_Private) br_isIgnoredByFileProviderWithError:]"
+ "2720.120.29"
+ "BRPersonaUtils"
+ "[CRIT] UNREACHABLE: Failed to adopt persona for _br_addDomain retry%@"
+ "_br_minMaxWithMax:comparator:"
+ "br_errorDescription"
+ "br_isIgnoredByFileProviderWithError:"
+ "executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:"
+ "performWithPersonaID:block:"
+ "v40@0:8Q16@?24@?32"
- "-[NSURL(BRAdditions_Private) br_isIgnoredByFileProvider]"
- "2720.100.117"
- "[NOTICE] URL has com.apple.fileprovider.detached attribute%@"
- "[WARNING] Failed with %d opening file at: %@%@"
- "_br_minMaxWithMax:comperator:"
- "com.apple.fileprovider.detached"
- "com.apple.fileprovider.detached#PN"
- "fp_prettyPath"

```
