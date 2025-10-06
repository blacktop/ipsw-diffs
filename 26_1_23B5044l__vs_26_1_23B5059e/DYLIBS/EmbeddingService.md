## EmbeddingService

> `/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService`

```diff

-3505.5.1.0.0
-  __TEXT.__text: 0x169c
-  __TEXT.__auth_stubs: 0x2b0
+3505.11.2.0.0
+  __TEXT.__text: 0x1a50
+  __TEXT.__auth_stubs: 0x370
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x2b4
+  __TEXT.__objc_methlist: 0x2cc
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x15b
+  __TEXT.__cstring: 0x15e
   __TEXT.__oslogstring: 0x197
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__unwind_info: 0xb8
   __TEXT.__objc_classname: 0x33
-  __TEXT.__objc_methname: 0x751
-  __TEXT.__objc_methtype: 0x150
-  __TEXT.__objc_stubs: 0x660
+  __TEXT.__objc_methname: 0x7fa
+  __TEXT.__objc_methtype: 0x18a
+  __TEXT.__objc_stubs: 0x700
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c8
+  __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x160
+  __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x498
+  __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__objc_const: 0x4f8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0xc4
+  __DATA.__objc_ivar: 0x2c
+  __DATA.__data: 0xc0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CA377AA-0A82-3255-B589-6D4208F1C857
-  Functions: 36
-  Symbols:   241
-  CStrings:  170
+  UUID: F15848B6-1967-34BC-9058-DF592CCAE0F8
+  Functions: 38
+  Symbols:   265
+  CStrings:  184
 
Symbols:
+ -[QUEmbeddingService icuRangeOfString:range:query:]
+ -[QUEmbeddingService rangeOfSubtoken:range:query:]
+ _OBJC_IVAR_$_QUEmbeddingService._icuCollator
+ _OBJC_IVAR_$_QUEmbeddingService._icuPatternBuffer
+ _OBJC_IVAR_$_QUEmbeddingService._icuQueryBuffer
+ ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke.99
+ ___61-[QUEmbeddingService getEmbeddingForQuery:completionHandler:]_block_invoke.101
+ ___block_descriptor_56_e8_32s40s48bs_e78_v24?0"SIRINLUEXTERNALSUBWORD_EMBEDDINGSubwordEmbeddingResponse"8"NSError"16ls48l8s32l8s40l8
+ _free
+ _malloc_type_realloc
+ _objc_msgSend$getCharacters:range:
+ _objc_msgSend$icuRangeOfString:range:query:
+ _objc_msgSend$languageCode
+ _objc_msgSend$rangeOfString:options:range:
+ _objc_msgSend$rangeOfSubtoken:range:query:
+ _objc_retain_x21
+ _ucol_close
+ _ucol_open
+ _ucol_setAttribute
+ _usearch_close
+ _usearch_following
+ _usearch_getMatchedLength
+ _usearch_openFromCollator
+ _usearch_setAttribute
+ _usearch_setOffset
- ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke.96
- ___61-[QUEmbeddingService getEmbeddingForQuery:completionHandler:]_block_invoke.98
- ___block_descriptor_64_e8_32s40s48s56bs_e78_v24?0"SIRINLUEXTERNALSUBWORD_EMBEDDINGSubwordEmbeddingResponse"8"NSError"16ls56l8s32l8s40l8s48l8
CStrings:
+ "3"
+ "^S"
+ "^{UCollator=}"
+ "_icuCollator"
+ "_icuPatternBuffer"
+ "_icuQueryBuffer"
+ "getCharacters:range:"
+ "icuRangeOfString:range:query:"
+ "languageCode"
+ "rangeOfString:options:range:"
+ "rangeOfSubtoken:range:query:"
+ "tr"
+ "{_NSRange=QQ}48@0:8@16{_NSRange=QQ}24@40"

```
