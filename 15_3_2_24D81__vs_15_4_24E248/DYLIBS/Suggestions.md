## Suggestions

> `/System/Library/PrivateFrameworks/Suggestions.framework/Versions/A/Suggestions`

```diff

 333.0.0.0.0
-  __TEXT.__text: 0x56670
+  __TEXT.__text: 0x56e9c
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x46fc
+  __TEXT.__objc_methlist: 0x4f18
   __TEXT.__const: 0x168
   __TEXT.__cstring: 0x389a
   __TEXT.__ustring: 0xc
-  __TEXT.__gcc_except_tab: 0xe8c
+  __TEXT.__gcc_except_tab: 0xea0
   __TEXT.__oslogstring: 0x54
   __TEXT.__dof_Suggestio: 0x2f7
-  __TEXT.__unwind_info: 0x1490
+  __TEXT.__unwind_info: 0x14e0
   __TEXT.__objc_classname: 0xa3f
   __TEXT.__objc_methname: 0xb3c0
   __TEXT.__objc_methtype: 0x2359

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f30
+  __DATA_CONST.__objc_selrefs: 0x32d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x578
   __AUTH_CONST.__const: 0x13a0
   __AUTH_CONST.__cfstring: 0x4820
-  __AUTH_CONST.__objc_const: 0xaf08
+  __AUTH_CONST.__objc_const: 0x9f80
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8C5019C-E2E9-3284-979A-0C391FAC25F7
-  Functions: 1730
-  Symbols:   4995
+  UUID: 98F90A17-FDB1-33B7-9F45-C74F624605DA
+  Functions: 1825
+  Symbols:   5102
   CStrings:  3671
 
Symbols:
+ +[SGTABPersonGeniusHelper _loadAccountsFramework].cold.1
+ +[SGTABPersonGeniusHelper _loadCoreRecentsFramework].cold.1
+ +[SGTABPersonGeniusHelper _userMailAccounts].cold.1
+ +[SGTCategory folderCategory].cold.1
+ +[SGTCategory othersCategory].cold.1
+ +[SGTCategory recentsCategory].cold.1
+ +[SGTCategory suggestionsCategory].cold.1
+ +[SGTCategory topHitCategory].cold.1
+ +[SGTDateSuggester dateCategory].cold.1
+ +[SGTDateSuggestion _minimalUsefulDateLength].cold.1
+ +[SGTFileLabelSuggestion labelsCategory].cold.1
+ +[SGTFileQueryGenius _attributeToScope].cold.1
+ +[SGTFileQueryGenius applicationsCategory].cold.1
+ +[SGTFileQueryGenius contentCategory].cold.1
+ +[SGTFileQueryGenius downloadedFromCategory].cold.1
+ +[SGTFileQueryGenius filenameCategory].cold.1
+ +[SGTFileQueryGenius filenameTypingScopeCategory].cold.1
+ +[SGTFileQueryGenius folderCategory].cold.1
+ +[SGTFileQueryGenius initialize].cold.1
+ +[SGTFileQueryGenius initialize].cold.2
+ +[SGTFileQueryGenius kindCategory].cold.1
+ +[SGTFileQueryGenius sentByCategory].cold.1
+ +[SGTFileQueryGenius sharedByCategory].cold.1
+ +[SGTFileQueryGenius tagCategory].cold.1
+ +[SGTFileQueryGenius topicCategory].cold.1
+ +[SGTHasAttachmentSuggester attachmentCategory].cold.1
+ +[SGTMailFlagColorSuggester flagColorsCategory].cold.1
+ +[SGTMailPrioritySuggester prioritiesCategory].cold.1
+ +[SGTMailQueryGenius _attributeToScope].cold.1
+ +[SGTMailQueryGenius didYouMeanCategory].cold.1
+ +[SGTMailQueryGenius messageCategory].cold.1
+ +[SGTMailQueryGenius peopleAttributes].cold.1
+ +[SGTMailQueryGenius peopleCategoryForRecipients].cold.1
+ +[SGTMailQueryGenius peopleCategory].cold.1
+ +[SGTMailQueryGenius subjectCategory].cold.1
+ +[SGTMailStatusSuggestion mailStatusCategory].cold.1
+ +[SGTMailboxSuggestion mailboxCategory].cold.1
+ +[SGTRecentsSuggester _checkInDefaultsGlobal:saveName:].cold.1
+ +[SGTRecentsSuggester _checkOutDefaultsGlobal:saveName:].cold.1
+ +[SGTRecentsSuggester _userInfoForThisProcess].cold.1
+ +[SGTSearchField unsafeBoldCharacterSet].cold.1
+ +[SGTSearchQuerySuggester defaultSortingAttributeNames].cold.1
+ +[SGTSpotlightSuggester defaultSortingAttributeNames].cold.1
+ +[SGTSuggester suggestersForMailsUsingSearchQueryIndex:].cold.1
+ +[SGTSuggestion fuzzyAttributesSet].cold.1
+ -[NSString(SGTAdditions) _sgt_untokenizedRangeTouchingSelectedRange:].cold.1
+ -[SGTABPersonGeniusHelper attributesForEmail].cold.1
+ -[SGTABPersonGeniusHelper attributesForFullname].cold.1
+ -[SGTABPersonGeniusHelper nameProperties].cold.1
+ -[SGTABPersonImageAsyncLoader addRelatedObject:].cold.1
+ -[SGTABPersonImageAsyncLoader startLoading].cold.1
+ -[SGTABPersonImageAsyncLoader startLoading].cold.2
+ -[SGTCompletionTableView mouseDown:].cold.1
+ -[SGTCompletionTableView mouseMoved:].cold.1
+ -[SGTFileLabelSuggester setInput:].cold.1
+ -[SGTFileQueryGenius suggester:filterSuggestions:forInput:].cold.1
+ -[SGTMailQueryGenius suggester:filterSuggestions:forInput:].cold.1
+ -[SGTMailStatus initWithStatusType:names:menuName:imageName:spotlightAttribute:].cold.1
+ -[SGTSearchField _openCompletionWindowAndUpdate:].cold.1
+ -[SGTSearchField _openCompletionWindowAndUpdate:].cold.2
+ -[SGTSearchField becomeFirstResponder].cold.1
+ -[SGTSearchField setSearchQueryIndex:].cold.1
+ -[SGTSearchField setStringValue:].cold.1
+ -[SGTSearchField updateFreeTextSuggestionsSuggestionRange:].cold.1
+ -[SGTSearchQuerySuggester searchQueryCollector:processQueryResults:processSuggestions:context:intermediateResults:].cold.1
+ -[SGTSearchQuerySuggester setInput:withGroup:].cold.1
+ -[SGTSpotlightCollector _forceQueryResults:].cold.1
+ -[SGTSpotlightCollector _queryDidFinish:].cold.1
+ -[SGTSpotlightCollector searchWithContext:].cold.1
+ -[SGTSpotlightCollectorReserved dealloc].cold.1
+ -[SGTSpotlightCollectorWarmingQueryReserved dealloc].cold.1
+ -[SGTSpotlightSuggester _forceQueryResults:].cold.1
+ -[SGTSpotlightSuggester _processQueryResults:intermediateResults:suggestionsCount:].cold.1
+ -[SGTSpotlightSuggester _queryDidFinish:].cold.1
+ -[SGTSpotlightSuggester setInput:].cold.1
+ -[SGTSpotlightSuggesterReserved dealloc].cold.1
+ -[SGTSpotlightSuggesterReserved dealloc].cold.2
+ -[SGTTokenTextView _updateCompletionWithRangeOfCompletion:selectedRange:byTyping:].cold.1
+ -[SGTTokenTextView replaceCharactersInRange:withAttributedString:].cold.1
+ SGTAddressBookAccessAllowed.cold.1
+ SGTCommonWords.cold.2
+ SGTCoreRecentsAccessAllowed.cold.1
+ SGTHasMessageFramework.cold.1
+ SGTImageNamed.cold.1
+ SGTImageNamed.cold.2
+ _CachingMDQueryCreateQueryStringWithOptions.cold.1
+ _MDQueryCreateQueryDictionaryWithOptionsDict_serially.cold.1
+ _MDQueryCreateQueryStringWrapper.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _SGTAppGetDefaultValues.cold.1
+ __37+[SGTMailStatusSuggestion initialize]_block_invoke.cold.1
+ __55+[SGTRecentsSuggester _checkInDefaultsGlobal:saveName:]_block_invoke.cold.1
+ __SGTTracingTrace_block_invoke.cold.1
+ __SGTTracingTrace_block_invoke.cold.2
+ ___CachingMDQueryCreateQueryStringWithOptions_block_invoke.50.cold.1
+ ____MDQueryCreateQueryStringWithOptions_block_invoke.cold.2
+ ____MDQueryCreateQueryString_block_invoke.cold.2
+ _sgtDefaultLog.cold.1
+ _sgtSignpostLog.cold.1
+ initECSubjectParser.cold.1
+ initECSubjectParser.cold.2
+ warmingQueriesQueue.cold.1

```
