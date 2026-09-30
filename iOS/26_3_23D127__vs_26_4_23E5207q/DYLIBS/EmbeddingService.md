## EmbeddingService

> `/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService`

```diff

-3505.14.1.0.0
-  __TEXT.__text: 0x1a50
-  __TEXT.__auth_stubs: 0x370
+3520.57.3.0.0
+  __TEXT.__text: 0x1d20
+  __TEXT.__auth_stubs: 0x340
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x2cc
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x15e
   __TEXT.__oslogstring: 0x197
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__unwind_info: 0xf0
   __TEXT.__objc_classname: 0x33
   __TEXT.__objc_methname: 0x7fa
   __TEXT.__objc_methtype: 0x18a

   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x4f8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 347386FB-15E9-3660-8CF2-990E4A1C4BF1
+  UUID: FD27787A-FC73-32CD-9FBD-D7798380F6A3
   Functions: 38
-  Symbols:   265
+  Symbols:   262
   CStrings:  184
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x8
Functions:
~ -[QUEmbeddingOutput setEmbedding:] : 12 -> 64
~ -[QUEmbeddingOutput setTokens:] : 12 -> 64
~ -[QUEmbeddingOutput setTokenRanges:] : 12 -> 64
~ -[QUEmbeddingOutput setSubtokens:] : 12 -> 64
~ -[QUEmbeddingOutput setSubtokenLenForTokens:] : 12 -> 64
~ +[QUEmbeddingService log] : 160 -> 176
~ ___25+[QUEmbeddingService log]_block_invoke : 108 -> 112
~ +[QUEmbeddingService signpostLog] : 160 -> 176
~ ___33+[QUEmbeddingService signpostLog]_block_invoke : 108 -> 112
~ +[QUEmbeddingService setTestEmbeddings:] : 16 -> 64
~ +[QUEmbeddingService testEmbeddings] : 12 -> 60
~ ___34+[QUEmbeddingService isUnitTested]_block_invoke : 204 -> 212
~ -[QUEmbeddingService initWithLocale:version:] : 344 -> 348
~ -[QUEmbeddingService dealloc] : 168 -> 172
~ -[QUEmbeddingService icuRangeOfString:range:query:] : 520 -> 516
~ -[QUEmbeddingService rangeOfSubtoken:range:query:] : 252 -> 256
~ -[QUEmbeddingService loadWithCompletionHandler:] : 676 -> 700
~ ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke_2 : 116 -> 120
~ ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke.99 : 228 -> 236
~ ___61-[QUEmbeddingService getEmbeddingForQuery:completionHandler:]_block_invoke.101 : 2528 -> 2644
~ -[QUEmbeddingService setLocale:] : 12 -> 64
~ -[QUEmbeddingService setVersion:] : 12 -> 64
~ -[QUEmbeddingService setCdmClient:] : 12 -> 64

```
