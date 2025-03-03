## QueryParser

> `/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser`

```diff

-2333.18.0.8.0
-  __TEXT.__text: 0x9eda8
-  __TEXT.__auth_stubs: 0x19c0
-  __TEXT.__objc_methlist: 0x6d8
-  __TEXT.__const: 0x11ce
-  __TEXT.__gcc_except_tab: 0xb870
-  __TEXT.__oslogstring: 0x3108
-  __TEXT.__cstring: 0x8a7c
+2333.7.0.1.0
+  __TEXT.__text: 0xa16b8
+  __TEXT.__auth_stubs: 0x19a0
+  __TEXT.__objc_methlist: 0x8f4
+  __TEXT.__const: 0x120e
+  __TEXT.__gcc_except_tab: 0xbedc
+  __TEXT.__oslogstring: 0x32b1
+  __TEXT.__cstring: 0x8b5e
   __TEXT.__ustring: 0x10a
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x3230
-  __TEXT.__objc_classname: 0xb5
-  __TEXT.__objc_methname: 0x21d3
-  __TEXT.__objc_methtype: 0x3b2
-  __TEXT.__objc_stubs: 0x2960
-  __DATA_CONST.__got: 0x420
-  __DATA_CONST.__const: 0x2318
-  __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__unwind_info: 0x32d8
+  __TEXT.__objc_classname: 0xeb
+  __TEXT.__objc_methname: 0x262d
+  __TEXT.__objc_methtype: 0x465
+  __TEXT.__objc_stubs: 0x2c00
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0x2390
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb90
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0xc60
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x18d0
-  __AUTH_CONST.__auth_got: 0xcf8
+  __AUTH_CONST.__auth_got: 0xce8
   __AUTH_CONST.__auth_ptr: 0x68
   __AUTH_CONST.__const: 0x1c88
-  __AUTH_CONST.__cfstring: 0xd3a0
-  __AUTH_CONST.__objc_const: 0xb50
+  __AUTH_CONST.__cfstring: 0xd440
+  __AUTH_CONST.__objc_const: 0x10a0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_intobj: 0x1410
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__objc_doubleobj: 0x110
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x90
-  __DATA.__data: 0xa70
-  __DATA.__bss: 0x178
+  __AUTH_CONST.__objc_doubleobj: 0xf0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__data: 0xae0
+  __DATA.__bss: 0x1a0
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x270
+  __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2126
-  Symbols:   3412
-  CStrings:  2649
+  Functions: 2175
+  Symbols:   3478
+  CStrings:  2729
 
Symbols:
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_NSUUID
+ _kQPParseAttributeGenericEventKindKey
+ _kQPQUOutputTokenIsSelfKey
+ _objc_retain_x27
- _CFErrorCopyUserInfo
- _CFErrorGetCode
- _CFErrorGetDomain
CStrings:
+ "\x03"
+ "\a"
+ "%@%s to %s"
+ "@\"NSArray\"16@0:8"
+ "@\"NSNumber\""
+ "@\"NSNumber\"16@0:8"
+ "@56@0:8@16{_NSRange=QQ}24@40@48"
+ "A961F9B4-F844-4261-8740-BA91F44C6393"
+ "Embedding Error: Unable to generate embedding"
+ "GluedU2Output"
+ "INTENT: %@, unsafeConf: %.2f, EmbeddingQ: %@\n"
+ "ModifiedToken"
+ "Not using ECR output names, emails and phone number for text:%@"
+ "QUUnderstandingOutput"
+ "QueryParserManager init: requestedLocale=%@ currentLocale=%@ loaded=%d"
+ "QueryParserManager: nlp parsing unavailable - falling back to default date parsing"
+ "QueryParserManager: unknown language %@"
+ "T@\"NSArray\",&,N,V_argIdsForToken"
+ "T@\"NSArray\",&,N,V_argIdsForTokens"
+ "T@\"NSArray\",&,N,V_argScoresForToken"
+ "T@\"NSArray\",&,N,V_argScoresForTokens"
+ "T@\"NSArray\",&,N,V_tokenRanges"
+ "T@\"NSArray\",&,N,V_tokens"
+ "T@\"NSArray\",R,N"
+ "T@\"NSNumber\",&,N,V_confidenceScore"
+ "T@\"NSNumber\",&,N,V_intentId"
+ "T@\"NSNumber\",&,N,V_safetyScore"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSString\",&,N,V_token"
+ "TQ,N,V_embeddingsTime"
+ "TQ,N,V_predictionTime"
+ "TQ,R,N"
+ "T{_NSRange=QQ},N,V_tokenRange"
+ "[QPNLU] Embedding preheat failed (%@) (time=%.6fms)"
+ "[QPNLU] Embedding preheat failed (time=time=%.6fms) (%@)"
+ "[QPNLU] Embedding preheat succeeded (time=%.6fms)"
+ "[QPNLU] Embedding preheat succeeded (time=time=%.6fms)"
+ "[QPNLU] Lexeme: %@ Type: %@"
+ "[QPNLU][qid=%ld] Empty photo embedding string from parser"
+ "[QPNLU][qid=%ld] Generated embedding data (time=%.6fms)"
+ "[QPNLU][qid=%ld] Semantic search is not supported for this keyboard (\"%@\") and locale languge (\"%@\")"
+ "[QPNLU][qid=%ld] Starting U2 parse - identifier=%@ context=%ld queryLen=%ld"
+ "[QPNLU][qid=%ld] nlp parsing disabled for locale=%@"
+ "[QPNLU][qid=%ld] not generating query embedding due to failed string check in non-CJK"
+ "[QPNLU][qid=%ld] skipping embedding generation for the same queryID (error: %d)"
+ "[QPNLU][qid=%ld] starting m_parser parse with new:%d u2:%d llm:%d embeddings:%d queryLen:%ld"
+ "_argIdsForToken"
+ "_argIdsForTokens"
+ "_argScoresForToken"
+ "_argScoresForTokens"
+ "_confidenceScore"
+ "_embeddingsTime"
+ "_intentId"
+ "_predictionTime"
+ "_safetyScore"
+ "_token"
+ "_tokenRange"
+ "_tokenRanges"
+ "_tokens"
+ "addIndex:"
+ "argIdsForToken"
+ "argScores"
+ "argScoresForToken"
+ "compare:"
+ "enumerateIndexesUsingBlock:"
+ "generateEmbeddingForTextInputs:extendedContextLength:queryID:clientBundleID:timeout:useCLIPSafety:workCost:error:"
+ "initWithToken:tokenRange:argIdsForToken:argScoresForToken:"
+ "initWithUUIDString:"
+ "kQPGenericEvent"
+ "kQPQUOutputTokenIsSelf"
+ "loadAllParametersForClient:"
+ "logForTrigger:queryID:"
+ "logTriggerForCodepathID:queryID:"
+ "removeAllIndexes"
+ "setArgIdsForToken:"
+ "setArgIdsForTokens:"
+ "setArgScoresForToken:"
+ "setArgScoresForTokens:"
+ "setConfidenceScore:"
+ "setEmbeddingsTime:"
+ "setIntentId:"
+ "setPredictionTime:"
+ "setSafetyScore:"
+ "setToken:"
+ "setTokenRange:"
+ "setTokenRanges:"
+ "setTokens:"
+ "token"
+ "tokenRange"
+ "unordered_map::at: key not found"
+ "v24@0:8Q16"
+ "v24@?0Q8^B16"
+ "v32@0:8@16q24"
+ "v32@0:8{_NSRange=QQ}16"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
+ "{_NSRange=\"location\"Q\"length\"Q}"
+ "{_NSRange=QQ}16@0:8"
- " to "
- "Embedding preheat failed (%@)"
- "Embedding preheat failed (time=time=%.2lldns) (%@)"
- "Embedding preheat succeeded (time=%.2fms)"
- "Embedding preheat succeeded (time=time=%.2lldns)"
- "INTENT: %@, unsafeConf: %.2f\n"
- "QueryParserManager: default date parsing"
- "QueryParserManager: loaded %@"
- "QueryParserManager: unknown language"
- "[QPNLU][qid=%ld] Empty photo embedding string"
- "[QPNLU][qid=%ld] Generated embedding data (time=%.2lldns)"
- "[QPNLU][qid=%ld] Semantic search is not supported for this keyboard(\"%@\") and locale languge(\"%@\")"
- "[QPNLU][qid=%ld] not generating query embedding due to failed string check"
- "[QPNLU][qid=%ld] starting m_parser parse with u2:%d and llm:%d embeddings:%d"
- "config loaded identifier(%@) context(%ld)"
- "generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:useCLIPSafety:workCost:error:"
- "timeIntervalSinceDate:"

```
