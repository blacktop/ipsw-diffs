## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2274.0.3.0.0
-  __TEXT.__text: 0x9d4a8
-  __TEXT.__auth_stubs: 0x1960
-  __TEXT.__objc_methlist: 0x991c
+2274.8.2.0.0
+  __TEXT.__text: 0x9d6f8
+  __TEXT.__auth_stubs: 0x1950
+  __TEXT.__objc_methlist: 0x990c
   __TEXT.__const: 0x90c
   __TEXT.__cstring: 0xcd12
   __TEXT.__gcc_except_tab: 0x1a54

   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2774
+  __TEXT.__unwind_info: 0x2778
   __TEXT.__eh_frame: 0x120
-  __TEXT.__objc_classname: 0xbc2
-  __TEXT.__objc_methname: 0x16ba4
+  __TEXT.__objc_classname: 0xbdc
+  __TEXT.__objc_methname: 0x16a28
   __TEXT.__objc_methtype: 0x1b1e
-  __TEXT.__objc_stubs: 0xd040
+  __TEXT.__objc_stubs: 0xcfc0
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x3b90
-  __DATA_CONST.__objc_classlist: 0x320
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xb7b0
-  __DATA_CONST.__objc_selrefs: 0x5c00
+  __DATA_CONST.__objc_selrefs: 0x5be0
   __DATA_CONST.__objc_arraydata: 0x958
   __AUTH_CONST.__const: 0x1378
-  __AUTH_CONST.__cfstring: 0xd420
-  __AUTH_CONST.__objc_const: 0x2cd8
+  __AUTH_CONST.__cfstring: 0xd440
+  __AUTH_CONST.__objc_const: 0x2d20
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x708
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0xcc0
-  __AUTH.__objc_data: 0x960
+  __AUTH_CONST.__auth_got: 0xcb8
+  __AUTH.__objc_data: 0x9b0
   __AUTH.__data: 0x300
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x400
-  __DATA.__objc_superrefs: 0x268
-  __DATA.__objc_ivar: 0x988
+  __DATA.__objc_superrefs: 0x270
+  __DATA.__objc_ivar: 0x980
   __DATA.__data: 0xd18
   __DATA.__bss: 0xb90
   __DATA_DIRTY.__objc_data: 0x15e0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4289
-  Symbols:   13365
-  CStrings:  7516
+  Functions: 4294
+  Symbols:   13359
+  CStrings:  7509
 
Symbols:
+ +[CSTopHitQuery sortSearchableItems:]
+ +[CSUserQuery sortSearchableItems:]
+ -[CSInternalSearchableIndex initWithName:protectionClass:bundleIdentifier:options:]
+ -[CSSearchQueryContext entitledAttributes]
+ -[CSSearchQueryContext setEntitledAttributes:]
+ -[CSUserQuery isTopHitQuery]
+ GCC_except_table15
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table252
+ GCC_except_table264
+ GCC_except_table272
+ GCC_except_table277
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table29
+ GCC_except_table293
+ GCC_except_table295
+ GCC_except_table300
+ GCC_except_table302
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table388
+ GCC_except_table41
+ GCC_except_table46
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table72
+ _OBJC_CLASS_$_CSInternalSearchableIndex
+ _OBJC_IVAR_$_CSSearchQueryContext._entitledAttributes
+ _OBJC_METACLASS_$_CSInternalSearchableIndex
+ __OBJC_$_INSTANCE_METHODS_CSInternalSearchableIndex
+ __OBJC_CLASS_RO_$_CSInternalSearchableIndex
+ __OBJC_METACLASS_RO_$_CSInternalSearchableIndex
+ ___21-[CSSearchQuery poll]_block_invoke.897
+ ___35+[CSUserQuery sortSearchableItems:]_block_invoke
+ ___37+[CSTopHitQuery sortSearchableItems:]_block_invoke
+ ___52-[CSSearchQuery processResultsData:protectionClass:]_block_invoke.939
+ ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.923
+ ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.313
+ ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.513
+ ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.927
+ ___94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.543
+ ___block_literal_global.1195
+ ___block_literal_global.1197
+ ___block_literal_global.1281
+ ___block_literal_global.315
+ ___block_literal_global.434
+ ___block_literal_global.439
+ ___block_literal_global.515
+ ___block_literal_global.597
+ ___block_literal_global.853
+ ___block_literal_global.860
+ ___block_literal_global.900
+ ___block_literal_global.904
+ __unnamed_array_storage.431
+ __unnamed_array_storage.436
+ __unnamed_array_storage.447
+ __unnamed_array_storage.450
+ __unnamed_array_storage.508
+ __unnamed_array_storage.520
+ __unnamed_array_storage.608
+ __unnamed_array_storage.609
+ _defaultSearchableIndex.onceToken.608
+ _defaultSearchableIndex.sDefaultInstance.607
+ _objc_msgSend$entitledAttributes
+ _objc_msgSend$setEntitledAttributes:
+ _objc_msgSend$sortSearchableItems:
+ _queryStringWithQueryContext:searchString:options:.onceAttributesToken.512
- +[CSTopHitQuery sortSearchableItemsByL2:]
- +[CSUserQuery sortSearchableItemsByL2:]
- -[CSSearchQueryContext allowDocumentUnderstandingEntitledAttributes]
- -[CSSearchQueryContext allowPhotosEntitledAttributes]
- -[CSSearchQueryContext allowSpotlightEntitledAttributes]
- -[CSSearchQueryContext setAllowDocumentUnderstandingEntitledAttributes:]
- -[CSSearchQueryContext setAllowPhotosEntitledAttributes:]
- -[CSSearchQueryContext setAllowSpotlightEntitledAttributes:]
- GCC_except_table14
- GCC_except_table247
- GCC_except_table249
- GCC_except_table256
- GCC_except_table268
- GCC_except_table276
- GCC_except_table28
- GCC_except_table281
- GCC_except_table291
- GCC_except_table294
- GCC_except_table297
- GCC_except_table303
- GCC_except_table306
- GCC_except_table308
- GCC_except_table375
- GCC_except_table376
- GCC_except_table377
- GCC_except_table378
- GCC_except_table392
- GCC_except_table40
- GCC_except_table49
- GCC_except_table53
- GCC_except_table57
- GCC_except_table65
- GCC_except_table69
- _OBJC_IVAR_$_CSSearchQueryContext._allowDocumentUnderstandingEntitledAttributes
- _OBJC_IVAR_$_CSSearchQueryContext._allowPhotosEntitledAttributes
- _OBJC_IVAR_$_CSSearchQueryContext._allowSpotlightEntitledAttributes
- ___21-[CSSearchQuery poll]_block_invoke.907
- ___39+[CSUserQuery sortSearchableItemsByL2:]_block_invoke
- ___41+[CSTopHitQuery sortSearchableItemsByL2:]_block_invoke
- ___52-[CSSearchQuery processResultsData:protectionClass:]_block_invoke.949
- ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.933
- ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.314
- ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.514
- ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.937
- ___94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.545
- ___block_literal_global.1205
- ___block_literal_global.1207
- ___block_literal_global.1291
- ___block_literal_global.316
- ___block_literal_global.435
- ___block_literal_global.440
- ___block_literal_global.516
- ___block_literal_global.590
- ___block_literal_global.863
- ___block_literal_global.870
- ___block_literal_global.910
- ___block_literal_global.914
- __unnamed_array_storage.432
- __unnamed_array_storage.437
- __unnamed_array_storage.448
- __unnamed_array_storage.451
- __unnamed_array_storage.509
- __unnamed_array_storage.521
- __unnamed_array_storage.611
- _defaultSearchableIndex.onceToken.601
- _defaultSearchableIndex.sDefaultInstance.600
- _objc_allocWithZone
- _objc_msgSend$allowDocumentUnderstandingEntitledAttributes
- _objc_msgSend$allowPhotosEntitledAttributes
- _objc_msgSend$allowSpotlightEntitledAttributes
- _objc_msgSend$setAllowDocumentUnderstandingEntitledAttributes:
- _objc_msgSend$setAllowPhotosEntitledAttributes:
- _objc_msgSend$setAllowSpotlightEntitledAttributes:
- _objc_msgSend$sortSearchableItemsByL2:
- _queryStringWithQueryContext:searchString:options:.onceAttributesToken.513
CStrings:
+ "CSInternalSearchableIndex"
+ "Ti,N,V_entitledAttributes"
+ "_entitledAttributes"
+ "entitledAttributes"
+ "setEntitledAttributes:"
+ "sortSearchableItems:"
- "SpotlightSodiumRanking"
- "TB,V_allowDocumentUnderstandingEntitledAttributes"
- "TB,V_allowPhotosEntitledAttributes"
- "TB,V_allowSpotlightEntitledAttributes"
- "_allowDocumentUnderstandingEntitledAttributes"
- "_allowPhotosEntitledAttributes"
- "_allowSpotlightEntitledAttributes"
- "allowDocumentUnderstandingEntitledAttributes"
- "allowPhotosEntitledAttributes"
- "allowSpotlightEntitledAttributes"
- "setAllowDocumentUnderstandingEntitledAttributes:"
- "setAllowPhotosEntitledAttributes:"
- "setAllowSpotlightEntitledAttributes:"
- "sortSearchableItemsByL2:"

```
