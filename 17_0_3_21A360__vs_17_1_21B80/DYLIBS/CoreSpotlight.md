## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2268.1.8.0.0
-  __TEXT.__text: 0x9c454
+2274.0.3.0.0
+  __TEXT.__text: 0x9d4a8
   __TEXT.__auth_stubs: 0x1960
-  __TEXT.__objc_methlist: 0x98f4
+  __TEXT.__objc_methlist: 0x991c
   __TEXT.__const: 0x90c
-  __TEXT.__cstring: 0xcbb2
-  __TEXT.__gcc_except_tab: 0x1a44
+  __TEXT.__cstring: 0xcd12
+  __TEXT.__gcc_except_tab: 0x1a54
   __TEXT.__dlopen_cstrs: 0x1d2
-  __TEXT.__oslogstring: 0x512e
+  __TEXT.__oslogstring: 0x5449
   __TEXT.__ustring: 0x28
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__swift5_reflstr: 0x67

   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2760
+  __TEXT.__unwind_info: 0x2774
   __TEXT.__eh_frame: 0x120
   __TEXT.__objc_classname: 0xbc2
-  __TEXT.__objc_methname: 0x16a96
-  __TEXT.__objc_methtype: 0x1b0a
-  __TEXT.__objc_stubs: 0xcfc0
+  __TEXT.__objc_methname: 0x16ba4
+  __TEXT.__objc_methtype: 0x1b1e
+  __TEXT.__objc_stubs: 0xd040
   __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x3b78
+  __DATA_CONST.__const: 0x3b90
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb780
-  __DATA_CONST.__objc_selrefs: 0x5be0
+  __DATA_CONST.__objc_const: 0xb7b0
+  __DATA_CONST.__objc_selrefs: 0x5c00
   __DATA_CONST.__objc_arraydata: 0x958
   __AUTH_CONST.__const: 0x1378
-  __AUTH_CONST.__cfstring: 0xd2a0
+  __AUTH_CONST.__cfstring: 0xd420
   __AUTH_CONST.__objc_const: 0x2cd8
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x708

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x400
   __DATA.__objc_superrefs: 0x268
-  __DATA.__objc_ivar: 0x984
+  __DATA.__objc_ivar: 0x988
   __DATA.__data: 0xd18
   __DATA.__bss: 0xb90
   __DATA_DIRTY.__objc_data: 0x15e0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4284
-  Symbols:   13347
-  CStrings:  7491
+  Functions: 4289
+  Symbols:   13365
+  CStrings:  7516
 
Symbols:
+ +[CSInstantAnswers instantAnswersFallbackQueries:queryComponents:searchString:isShortQuery:]
+ +[CSInstantAnswers isInstantAnswersTriggeringQuery:isCJK:instantAnswerQueryMinLengthNonCJK:instantAnswerQueryMinLengthCJK:]
+ +[CSUserQuery(CSSuggestionBlending) dedupSuggestions:queryContextScopeIsToPerson:seenContactInfoToSuggestion:]
+ +[CSUserQuery(CSSuggestionBlending) dedupedSuggestions:queryContextScopeIsToPerson:options:]
+ +[CSUserQuery(CSSuggestionBlending) dedupedSuggestions:queryContextScopeIsToPerson:options:].cold.1
+ -[CSSearchQueryContext currentTokenScope]
+ -[CSSearchQueryContext setCurrentTokenScope:]
+ -[CSSuggestion(Person) mergeSuggestionAndUpdateLocalizedAttributedString:queryContextScopeIsToPerson:]
+ -[CSUserQuery queryStringWithQueryContext:searchString:options:].cold.8
+ GCC_except_table256
+ GCC_except_table268
+ GCC_except_table276
+ GCC_except_table281
+ GCC_except_table290
+ GCC_except_table291
+ GCC_except_table294
+ GCC_except_table299
+ GCC_except_table303
+ GCC_except_table308
+ GCC_except_table377
+ GCC_except_table378
+ GCC_except_table392
+ _MDItemHasTopHitAppShortcuts
+ _MDItemRunnableShortcutsPrimaryPhrase
+ _MDItemRunnableShortcutsTopHitBadge
+ _OBJC_IVAR_$_CSSearchQueryContext._currentTokenScope
+ ___21-[CSSearchQuery poll]_block_invoke.907
+ ___52-[CSSearchQuery processResultsData:protectionClass:]_block_invoke.949
+ ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.933
+ ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.514
+ ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.937
+ ___94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.545
+ ___block_literal_global.1113
+ ___block_literal_global.1205
+ ___block_literal_global.1207
+ ___block_literal_global.1291
+ ___block_literal_global.1354
+ ___block_literal_global.138
+ ___block_literal_global.1386
+ ___block_literal_global.140
+ ___block_literal_global.158
+ ___block_literal_global.28
+ ___block_literal_global.33
+ ___block_literal_global.41
+ ___block_literal_global.516
+ ___block_literal_global.61
+ ___block_literal_global.628
+ ___block_literal_global.75
+ ___block_literal_global.86
+ ___block_literal_global.870
+ ___block_literal_global.910
+ ___block_literal_global.914
+ __unnamed_array_storage.1124
+ __unnamed_array_storage.421
+ __unnamed_array_storage.490
+ __unnamed_array_storage.513
+ __unnamed_array_storage.519
+ __unnamed_array_storage.521
+ __unnamed_array_storage.611
+ _objc_msgSend$_extractEventDateToCompare:
+ _objc_msgSend$currentTokenScope
+ _objc_msgSend$dedupSuggestions:queryContextScopeIsToPerson:seenContactInfoToSuggestion:
+ _objc_msgSend$dedupedSuggestions:queryContextScopeIsToPerson:options:
+ _objc_msgSend$instantAnswersFallbackQueries:queryComponents:searchString:isShortQuery:
+ _objc_msgSend$isInstantAnswersTriggeringQuery:isCJK:instantAnswerQueryMinLengthNonCJK:instantAnswerQueryMinLengthCJK:
+ _objc_msgSend$mergeSuggestionAndUpdateLocalizedAttributedString:queryContextScopeIsToPerson:
+ _objc_msgSend$setCurrentTokenScope:
+ _overrideTokens.overrideTriggerPhraseSet
+ _queryStringWithQueryContext:searchString:options:.onceAttributesToken.513
- +[CSInstantAnswers instantAnswersFallbackQueries:queryComponents:searchString:]
- +[CSUserQuery(CSSuggestionBlending) dedupSuggestions:seenContactInfoToSuggestion:]
- +[CSUserQuery(CSSuggestionBlending) dedupedSuggestions:options:].cold.1
- -[CSSuggestion(Person) mergeSuggestionAndUpdateLocalizedAttributedString:]
- GCC_except_table254
- GCC_except_table266
- GCC_except_table274
- GCC_except_table279
- GCC_except_table288
- GCC_except_table289
- GCC_except_table292
- GCC_except_table295
- GCC_except_table301
- GCC_except_table302
- GCC_except_table373
- GCC_except_table374
- GCC_except_table390
- ___21-[CSSearchQuery poll]_block_invoke.900
- ___52-[CSSearchQuery processResultsData:protectionClass:]_block_invoke.942
- ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.926
- ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.520
- ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.930
- ___94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.551
- ___block_literal_global.1110
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.1198
- ___block_literal_global.1200
- ___block_literal_global.124
- ___block_literal_global.1284
- ___block_literal_global.1350
- ___block_literal_global.1382
- ___block_literal_global.21
- ___block_literal_global.29
- ___block_literal_global.49
- ___block_literal_global.522
- ___block_literal_global.54
- ___block_literal_global.625
- ___block_literal_global.65
- ___block_literal_global.70
- ___block_literal_global.856
- ___block_literal_global.903
- ___block_literal_global.907
- __unnamed_array_storage.1121
- __unnamed_array_storage.418
- __unnamed_array_storage.487
- __unnamed_array_storage.510
- __unnamed_array_storage.516
- __unnamed_array_storage.527
- __unnamed_array_storage.607
- __unnamed_array_storage.617
- _objc_msgSend$dedupSuggestions:seenContactInfoToSuggestion:
- _objc_msgSend$dedupedSuggestions:options:
- _objc_msgSend$instantAnswersFallbackQueries:queryComponents:searchString:
- _objc_msgSend$mergeSuggestionAndUpdateLocalizedAttributedString:
- _overrideTokens.flightTriggerPhraseSet
- _queryStringWithQueryContext:searchString:options:.onceAttributesToken.519
CStrings:
+ "\x01\x1e\x12\xf0t81\x12\x12"
+ "B44@0:8@16B24q28q36"
+ "[&$@_,.]+"
+ "[debug][instant answers][query] mailboxes = %@"
+ "[debug][instant answers][ranking]: Retrieved flight event for flightNumber = %@  was not added to candidate events"
+ "[debug][instant answers][ranking]: Retrieved hotel event for reservationID = %@ was not added to candidate events"
+ "[debug][instant answers][retrival]: Found flight event with number: %@%@ and departureTime: %@"
+ "[debug][instant answers][retrival]: Found hotel event with reservationId: %@, checkinDate: %@, checkinTime: %@"
+ "[debug][instant answers][retrival]: foundEvents count = %lu for userQuery = %@"
+ "[instant answers][fallback query]: searchString %@ identified as shortQuery, using %@ as fallback"
+ "[instant answers][query] triggering condition values: isCJK=%d, maxTokenLength=%ld, minTokenLength=%ld, allMinLengthTokensAreSymbols=%d"
+ "_kMDItemHasTopHitAppShortcuts"
+ "com_apple_shortcuts_runnable_primary_phrase"
+ "com_apple_shortcuts_runnable_top_hit_badge"
+ "currentTokenScope"
+ "date:"
+ "dedupSuggestions:queryContextScopeIsToPerson:seenContactInfoToSuggestion:"
+ "dedupedSuggestions:queryContextScopeIsToPerson:options:"
+ "from:"
+ "instantAnswersFallbackQueries:queryComponents:searchString:isShortQuery:"
+ "isInstantAnswersTriggeringQuery:isCJK:instantAnswerQueryMinLengthNonCJK:instantAnswerQueryMinLengthCJK:"
+ "kMDItemEventFlightDepartureAirportCode=\"%@\"cwd || kMDItemEventFlightArrivalAirportCode=\"%@\"cwd || kMDItemEventFlightCarrier=\"%@\"cwd"
+ "length <= %d AND NOT SELF MATCHES %@"
+ "mergeSuggestionAndUpdateLocalizedAttributedString:queryContextScopeIsToPerson:"
+ "setCurrentTokenScope:"
+ "subject:"
+ "to:"
- "\x01\x1f\x01\xf0d81\x12\x12"
- "dedupSuggestions:seenContactInfoToSuggestion:"
- "instantAnswersFallbackQueries:queryComponents:searchString:"
- "mergeSuggestionAndUpdateLocalizedAttributedString:"

```
