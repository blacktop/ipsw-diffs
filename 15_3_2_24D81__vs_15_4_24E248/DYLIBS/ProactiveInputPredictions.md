## ProactiveInputPredictions

> `/System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/Versions/A/ProactiveInputPredictions`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x143d8
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0xc84
-  __TEXT.__gcc_except_tab: 0x848
+1276.10.4.0.0
+  __TEXT.__text: 0x14198
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_methlist: 0xd54
   __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x844
   __TEXT.__cstring: 0xb41
   __TEXT.__oslogstring: 0x1ae4
   __TEXT.__ustring: 0x2a
-  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__unwind_info: 0x4b8
   __TEXT.__objc_classname: 0x24b
   __TEXT.__objc_methname: 0x2fdc
   __TEXT.__objc_methtype: 0x8c3

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0x5d0
   __AUTH_CONST.__cfstring: 0x1380
-  __AUTH_CONST.__objc_const: 0x1980
+  __AUTH_CONST.__objc_const: 0x1820
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1CBD9515-BA2A-3523-A092-8AA6AD76DC4C
+  UUID: 5F4E618F-C4CF-3210-9FBE-9E220D7A174C
   Functions: 335
-  Symbols:   1140
+  Symbols:   1141
   CStrings:  963
 
Symbols:
+ __142-[PSGProactiveTriggerHandler _handlePortraitTrigger:localeIdentifier:bundleIdentifier:recipients:limit:timeoutSeconds:explanationSet:results:]_block_invoke.91
+ __25-[PSGInternalClient init]_block_invoke.13
+ __47-[PSGInputSuggester warmUpForLocaleIdentifier:]_block_invoke.15
+ __49-[PSGUtilities prewarmCacheForLocale:usingQueue:]_block_invoke.12
+ __55-[PSGInputSuggesterClient initWithStructuredInfoCache:]_block_invoke.55
+ __58-[PSGWordBoundaryFSTGrammar getOTAPathForProactiveBundle:]_block_invoke.28
+ __66-[PSGInputSuggesterClient inputSuggestionsWithRequest:completion:]_block_invoke.129
+ __72-[PSGUtilities localizedStringForKey:withLocale:onlyIfCached:wasCached:]_block_invoke.25
+ __Block_byref_object_copy_.1018
+ __Block_byref_object_copy_.333
+ __Block_byref_object_copy_.67
+ __Block_byref_object_copy_.711
+ __Block_byref_object_dispose_.1019
+ __Block_byref_object_dispose_.334
+ __Block_byref_object_dispose_.68
+ __Block_byref_object_dispose_.712
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne190102IPjS5_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __block_literal_global.103
+ __block_literal_global.12
+ __block_literal_global.125
+ __block_literal_global.15
+ __block_literal_global.310
+ __block_literal_global.394
+ __block_literal_global.432
+ __block_literal_global.57
+ __block_literal_global.73
+ __block_literal_global.750
+ __block_literal_global.88
+ __block_literal_global.91
+ __block_literal_global.914
+ _memcpy
+ sharedInstance._pasExprOnceResult.1009
+ sharedInstance._pasExprOnceResult.395
+ sharedInstance._pasExprOnceResult.409
+ sharedInstance._pasExprOnceResult.74
+ sharedInstance._pasExprOnceResult.780
+ sharedInstance._pasExprOnceResult.917
+ sharedInstance._pasOnceToken2.1008
+ sharedInstance._pasOnceToken2.393
+ sharedInstance._pasOnceToken2.408
+ sharedInstance._pasOnceToken2.72
+ sharedInstance._pasOnceToken2.916
- __142-[PSGProactiveTriggerHandler _handlePortraitTrigger:localeIdentifier:bundleIdentifier:recipients:limit:timeoutSeconds:explanationSet:results:]_block_invoke.85
- __25-[PSGInternalClient init]_block_invoke.7
- __47-[PSGInputSuggester warmUpForLocaleIdentifier:]_block_invoke.9
- __49-[PSGUtilities prewarmCacheForLocale:usingQueue:]_block_invoke.6
- __55-[PSGInputSuggesterClient initWithStructuredInfoCache:]_block_invoke.49
- __58-[PSGWordBoundaryFSTGrammar getOTAPathForProactiveBundle:]_block_invoke.22
- __66-[PSGInputSuggesterClient inputSuggestionsWithRequest:completion:]_block_invoke.123
- __72-[PSGUtilities localizedStringForKey:withLocale:onlyIfCached:wasCached:]_block_invoke.19
- __Block_byref_object_copy_.1022
- __Block_byref_object_copy_.331
- __Block_byref_object_copy_.61
- __Block_byref_object_copy_.714
- __Block_byref_object_dispose_.1023
- __Block_byref_object_dispose_.332
- __Block_byref_object_dispose_.62
- __Block_byref_object_dispose_.715
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne180100IPjS5_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __block_literal_global.105
- __block_literal_global.119
- __block_literal_global.307
- __block_literal_global.392
- __block_literal_global.429
- __block_literal_global.51
- __block_literal_global.6
- __block_literal_global.75
- __block_literal_global.752
- __block_literal_global.82
- __block_literal_global.85
- __block_literal_global.9
- __block_literal_global.919
- sharedInstance._pasExprOnceResult.1013
- sharedInstance._pasExprOnceResult.393
- sharedInstance._pasExprOnceResult.407
- sharedInstance._pasExprOnceResult.76
- sharedInstance._pasExprOnceResult.783
- sharedInstance._pasExprOnceResult.922
- sharedInstance._pasOnceToken2.1012
- sharedInstance._pasOnceToken2.391
- sharedInstance._pasOnceToken2.406
- sharedInstance._pasOnceToken2.74
- sharedInstance._pasOnceToken2.921
Functions:
~ -[PSGWordBoundaryFSTGrammar triggerAttributesForContext:localeIdentifier:] : 2800 -> 2772
~ -[PSGWordBoundaryFSTGrammar _getPrimingToken:transientTokenID:] : 548 -> 540
~ -[PSGInputSuggester logTimeoutForRequest:] : 172 -> 168
~ -[PSGInputSuggestionsRequest isEqualToRequest:] : 1336 -> 1068
~ -[PSGInputSuggestionsRequest initWithCoder:] : 2376 -> 2364
~ -[PSGInputSuggestionsRequest initWithResponseContext:conversationTurns:adaptationContextID:shouldDisableAutoCaps:isResponseContextBlacklisted:contextBeforeInput:markedText:selectedText:contextAfterInput:selectedRangeInMarkedText:localeIdentifier:bundleIdentifier:recipients:recipientNames:textContentType:availableApps:textualResponseLimit:structuredInfoLimit:totalSuggestionsLimit:] : 912 -> 896
~ -[PSGInputSuggestionsRequest initWithResponseContext:conversationTurns:adaptationContextID:shouldDisableAutoCaps:isResponseContextBlacklisted:contextBeforeInput:markedText:selectedText:contextAfterInput:selectedRangeInMarkedText:localeIdentifier:bundleIdentifier:recipients:textContentType:availableApps:textualResponseLimit:structuredInfoLimit:] : 872 -> 864
~ -[PSGInputSuggestionsRequest initWithResponseContext:conversationTurns:responseKitConversationTurns:adaptationContextID:shouldDisableAutoCaps:isResponseContextBlacklisted:contextBeforeInput:markedText:selectedText:contextAfterInput:selectedRangeInMarkedText:localeIdentifier:bundleIdentifier:recipients:recipientNames:textContentType:availableApps:textualResponseLimit:structuredInfoLimit:totalSuggestionsLimit:] : 600 -> 592
~ -[PSGInputSuggestionsRequest initWithResponseContext:conversationTurns:responseKitConversationTurns:adaptationContextID:shouldDisableAutoCaps:isResponseContextBlacklisted:contextBeforeInput:markedText:selectedText:contextAfterInput:selectedRangeInMarkedText:localeIdentifier:bundleIdentifier:recipients:recipientNames:textContentType:availableApps:textualResponseLimit:structuredInfoLimit:totalSuggestionsLimit:initiatingProcess:] : 924 -> 880
~ -[PSGInputSuggestionsExplanationSet initWithCoder:] : 252 -> 256
~ ___60-[PSGInputSuggestionsExplanationSet hasContactsServingError]_block_invoke_2 : 324 -> 328
~ -[PSGTextualResponseSuggestion isEqualToTextualSuggestion:] : 212 -> 184
~ -[PSGTextualResponseSuggestion initWithCoder:] : 220 -> 224
~ -[PSGInputSuggestionsResponse isEqualToResponse:] : 212 -> 184
~ -[PSGProactiveTriggerHandler handleTrigger:localeIdentifier:bundleIdentifier:recipients:recipientNames:availableApps:timeoutSeconds:fetchLimit:maxSuggestions:explanationSet:error:] : 1884 -> 1872
~ -[PSGProactiveTriggerHandler _handlePortraitTrigger:localeIdentifier:bundleIdentifier:recipients:limit:timeoutSeconds:explanationSet:results:] : 1960 -> 1956
~ -[PSGInputSuggestionsResponseItem isEqualToItem:] : 212 -> 184
~ -[PSGProactiveTrigger isEqualToTrigger:] : 228 -> 200
~ -[PSGProactiveTrigger initWithCoder:] : 388 -> 392
~ -[PSGInputSuggesterClient inputSuggestionsWithRequest:completion:] : 2876 -> 2880
~ -[PSGInputSuggesterClient _combineMLAndRKItems:mlItems:] : 1332 -> 1328
~ -[PSGInputSuggesterClient _fillSuggestionsForResponseItems:localeIdentifier:recipients:recipientNames:bundleIdentifier:timeoutSeconds:structuredInfoFetchLimit:availableApps:textualResponseLimit:structuredInfoLimit:totalSuggestionsLimit:explanationSet:error:] : 1388 -> 1412
~ -[PSGOperationalPredictedItem isEqualToItem:] : 372 -> 304
~ -[PSGOperationalPredictedItem initWithCoder:] : 440 -> 444
~ -[PSGStructuredInfoSuggestion isEqualToItem:] : 292 -> 244
~ -[PSGStructuredInfoSuggestion initWithCoder:] : 280 -> 284
~ -[PSGStructuredInfoSuggestion predictedValue] : 80 -> 92
~ __72-[PSGUtilities localizedStringForKey:withLocale:onlyIfCached:wasCached:]_block_invoke.19 -> __72-[PSGUtilities localizedStringForKey:withLocale:onlyIfCached:wasCached:]_block_invoke.25 : 800 -> 796
~ ___49-[PSGUtilities prewarmCacheForLocale:usingQueue:]_block_invoke : 76 -> 84

```
