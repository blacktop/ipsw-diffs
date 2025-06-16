## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0xc9708
+2333.55.0.0.0
+  __TEXT.__text: 0xc9624
   __TEXT.__auth_stubs: 0x1bd0
   __TEXT.__objc_methlist: 0xc590
-  __TEXT.__const: 0xc22
+  __TEXT.__const: 0xc6a
   __TEXT.__gcc_except_tab: 0x2e94
-  __TEXT.__cstring: 0x11eb2
+  __TEXT.__cstring: 0x11e22
   __TEXT.__oslogstring: 0x6d15
   __TEXT.__ustring: 0x3c
   __TEXT.__dlopen_cstrs: 0x3f1

   __TEXT.__unwind_info: 0x31e0
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_classname: 0xf9f
-  __TEXT.__objc_methname: 0x1cd40
-  __TEXT.__objc_methtype: 0x21b8
-  __TEXT.__objc_stubs: 0xf920
+  __TEXT.__objc_methname: 0x1cd35
+  __TEXT.__objc_methtype: 0x21a3
+  __TEXT.__objc_stubs: 0xf900
   __DATA_CONST.__got: 0x780
   __DATA_CONST.__const: 0x4cd0
   __DATA_CONST.__objc_classlist: 0x448

   __DATA_CONST.__objc_arraydata: 0xd20
   __AUTH_CONST.__auth_got: 0xdf8
   __AUTH_CONST.__const: 0x1768
-  __AUTH_CONST.__cfstring: 0x119a0
+  __AUTH_CONST.__cfstring: 0x11960
   __AUTH_CONST.__objc_const: 0x121c0
   __AUTH_CONST.__objc_arrayobj: 0xa20
   __AUTH_CONST.__objc_intobj: 0x750

   __AUTH.__objc_data: 0x1310
   __AUTH.__data: 0x3a0
   __DATA.__objc_ivar: 0xb50
-  __DATA.__data: 0xa90
+  __DATA.__data: 0xa48
   __DATA.__bss: 0x1230
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__data: 0x1c

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E6D9E817-5620-37A7-93BF-1F12A8A72F47
+  UUID: C0DC3F7F-FC8F-36A1-A723-A5CF512D0D62
   Functions: 5315
-  Symbols:   16971
-  CStrings:  11680
+  Symbols:   16970
+  CStrings:  11675
 
Symbols:
+ +[CSUserQuery skipTextSemanticSearchForSearchString:queryContext:skipReason:]
+ ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.712
+ ___94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.762
+ ___block_literal_global.474
+ ___block_literal_global.596
+ ___block_literal_global.625
+ ___block_literal_global.714
+ _objc_msgSend$skipTextSemanticSearchForSearchString:queryContext:skipReason:
+ _queryStringWithQueryContext:searchString:options:.onceAttributesToken.711
- +[CSUserQuery skipTextSemanticSearchForSearchString:tokenCount:queryContext:skipReason:]
- ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.720
- ___94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.770
- ___block_literal_global.482
- ___block_literal_global.604
- ___block_literal_global.633
- ___block_literal_global.722
- _objc_msgSend$containsCJK
- _objc_msgSend$skipTextSemanticSearchForSearchString:tokenCount:queryContext:skipReason:
- _queryStringWithQueryContext:searchString:options:.onceAttributesToken.719
Functions:
~ +[CSUserQuery skipTextSemanticSearchForSearchString:tokenCount:queryContext:skipReason:] -> +[CSUserQuery skipTextSemanticSearchForSearchString:queryContext:skipReason:] : 460 -> 328
~ +[CSUserQuery parseResultWithSearchString:parseOptions:queryContext:isZKW:] : 6368 -> 6272
CStrings:
+ "skipTextSemanticSearchForSearchString:queryContext:skipReason:"
- "B48@0:8@16@24@32^@40"
- "kMDUserQueryDictionaryQueryTokenCountKey"
- "query does not match length criteria (tokenCount: %u, normalizedQueryLength: %lu, containsCJK: %d)"
- "skipTextSemanticSearchForSearchString:tokenCount:queryContext:skipReason:"

```
