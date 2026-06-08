## EmbeddingService

> `/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService`

```diff

-3525.3.5.0.0
-  __TEXT.__text: 0x1d20
-  __TEXT.__auth_stubs: 0x340
+3600.26.10.1.2
+  __TEXT.__text: 0x1a24
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x2cc
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x15e
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x162
   __TEXT.__oslogstring: 0x197
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x33
-  __TEXT.__objc_methname: 0x7fa
-  __TEXT.__objc_methtype: 0x18a
-  __TEXT.__objc_stubs: 0x700
-  __DATA_CONST.__got: 0x60
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x4f8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 948CBAB6-905A-3B25-BAEC-E45C4C0C672F
+  UUID: F20D0F81-0B54-30FA-BEF1-2598E03B0A3C
   Functions: 38
-  Symbols:   262
-  CStrings:  184
+  Symbols:   265
+  CStrings:  33
 
Symbols:
+ _OBJC_CLASS_$_CDMClient$loadHelper_x8
+ __OBJC_$_PROP_LIST_QUEmbeddingOutput.76
+ ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke.98
+ ___61-[QUEmbeddingService getEmbeddingForQuery:completionHandler:]_block_invoke.100
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x8
- __OBJC_$_PROP_LIST_QUEmbeddingOutput.77
- ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke.99
- ___61-[QUEmbeddingService getEmbeddingForQuery:completionHandler:]_block_invoke.101
- _gotLoadHelper_x8$_OBJC_CLASS_$_CDMClient
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
Functions:
~ -[QUEmbeddingOutput setEmbedding:] : 64 -> 12
~ -[QUEmbeddingOutput setTokens:] : 64 -> 12
~ -[QUEmbeddingOutput setTokenRanges:] : 64 -> 12
~ -[QUEmbeddingOutput setSubtokens:] : 64 -> 12
~ -[QUEmbeddingOutput setSubtokenLenForTokens:] : 64 -> 12
~ +[QUEmbeddingService log] : 176 -> 160
~ ___25+[QUEmbeddingService log]_block_invoke : 112 -> 108
~ +[QUEmbeddingService signpostLog] : 176 -> 160
~ ___33+[QUEmbeddingService signpostLog]_block_invoke : 112 -> 108
~ +[QUEmbeddingService setTestEmbeddings:] : 64 -> 16
~ +[QUEmbeddingService testEmbeddings] : 60 -> 12
~ ___34+[QUEmbeddingService isUnitTested]_block_invoke : 212 -> 204
~ -[QUEmbeddingService initWithLocale:version:] : 348 -> 344
~ -[QUEmbeddingService dealloc] : 172 -> 168
~ -[QUEmbeddingService icuRangeOfString:range:query:] : 516 -> 520
~ -[QUEmbeddingService rangeOfSubtoken:range:query:] : 256 -> 252
~ -[QUEmbeddingService loadWithCompletionHandler:] : 700 -> 676
~ ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke_2 : 120 -> 116
~ ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke.99 -> ___48-[QUEmbeddingService loadWithCompletionHandler:]_block_invoke.98 : 236 -> 228
~ -[QUEmbeddingService getEmbeddingForQuery:completionHandler:] : 672 -> 624
~ ___61-[QUEmbeddingService getEmbeddingForQuery:completionHandler:]_block_invoke.101 -> ___61-[QUEmbeddingService getEmbeddingForQuery:completionHandler:]_block_invoke.100 : 2644 -> 2532
~ -[QUEmbeddingService setLocale:] : 64 -> 12
~ -[QUEmbeddingService setVersion:] : 64 -> 12
~ -[QUEmbeddingService setCdmClient:] : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"CDMClient\""
- "@\"MLMultiArray\""
- "@\"MLMultiArray\"16@0:8"
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSLocale\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "QUEmbeddingOutput"
- "QUEmbeddingService"
- "T#,R"
- "T@\"CDMClient\",&,N,V_cdmClient"
- "T@\"MLMultiArray\",&,N,V_embedding"
- "T@\"MLMultiArray\",R,N"
- "T@\"NSArray\",&,N,V_subtokenLenForTokens"
- "T@\"NSArray\",&,N,V_subtokens"
- "T@\"NSArray\",&,N,V_tokenRanges"
- "T@\"NSArray\",&,N,V_tokens"
- "T@\"NSArray\",R,N"
- "T@\"NSLocale\",&,N,V_locale"
- "T@\"NSString\",&,N,V_version"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "UTF8String"
- "Vv16@0:8"
- "^S"
- "^{UCollator=}"
- "^{_NSZone=}16@0:8"
- "_cdmClient"
- "_embedding"
- "_icuCollator"
- "_icuPatternBuffer"
- "_icuQueryBuffer"
- "_locale"
- "_subtokenLenForTokens"
- "_subtokens"
- "_tokenRanges"
- "_tokens"
- "_version"
- "addObject:"
- "appendString:"
- "array"
- "arrayWithCapacity:"
- "autorelease"
- "cdmClient"
- "characterAtIndex:"
- "characterIsMember:"
- "class"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "description"
- "embedding"
- "embeddingDim"
- "embeddingTensor"
- "errorWithDomain:code:userInfo:"
- "getCharacters:range:"
- "getEmbeddingForQuery:completionHandler:"
- "getReturnValue:"
- "hash"
- "icuRangeOfString:range:query:"
- "init"
- "initWithLocale:version:"
- "initWithShape:dataType:error:"
- "invocationWithMethodSignature:"
- "invokeWithTarget:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isUnitTested"
- "languageCode"
- "length"
- "loadWithCompletionHandler:"
- "locale"
- "localeIdentifier"
- "log"
- "methodSignatureForSelector:"
- "numToken"
- "numberWithFloat:"
- "numberWithInt:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processEmbeddingRequest:completionHandler:"
- "punctuationCharacterSet"
- "rangeOfString:options:range:"
- "rangeOfString:options:range:locale:"
- "rangeOfSubtoken:range:query:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setCdmClient:"
- "setEmbedding:"
- "setLocale:"
- "setObject:atIndexedSubscript:"
- "setSelector:"
- "setSubtokenLenForTokens:"
- "setSubtokens:"
- "setTestEmbeddings:"
- "setTokenRanges:"
- "setTokens:"
- "setVersion:"
- "setupWithLocale:embeddingVersion:completionHandler:"
- "signpostLog"
- "string"
- "subarrayWithRange:"
- "substringFromIndex:"
- "subtokenLenForTokens"
- "subtokens"
- "subwordTokenChain"
- "subwordTokenEmbedding"
- "subwordTokens"
- "superclass"
- "testEmbeddings"
- "tokenIndex"
- "tokenRanges"
- "tokens"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@?24"
- "value"
- "valueWithRange:"
- "values"
- "version"
- "whitespaceCharacterSet"
- "zone"
- "{_NSRange=QQ}48@0:8@16{_NSRange=QQ}24@40"

```
