## ContactsAutocomplete

> `/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/Versions/A/ContactsAutocomplete`

```diff

-1341.400.1.0.0
-  __TEXT.__text: 0x5b3d8
-  __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_methlist: 0x38b4
-  __TEXT.__const: 0x306a
-  __TEXT.__oslogstring: 0x336c
-  __TEXT.__cstring: 0x2d13
+1341.500.41.0.0
+  __TEXT.__text: 0x5b6dc
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_methlist: 0x3f7c
+  __TEXT.__const: 0x2fda
+  __TEXT.__oslogstring: 0x33ac
+  __TEXT.__cstring: 0x2a83
   __TEXT.__gcc_except_tab: 0x670
   __TEXT.__constg_swiftt: 0xc84
   __TEXT.__swift5_typeref: 0xd3e

   __TEXT.__swift5_proto: 0x2dc
   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x14
+  __TEXT.__swift_as_entry: 0x64
+  __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1d40
-  __TEXT.__eh_frame: 0xb78
+  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__eh_frame: 0xc78
   __TEXT.__objc_classname: 0xfb5
-  __TEXT.__objc_methname: 0x98de
+  __TEXT.__objc_methname: 0x990d
   __TEXT.__objc_methtype: 0x1115
   __TEXT.__objc_stubs: 0x7e20
-  __DATA_CONST.__got: 0x7f8
-  __DATA_CONST.__const: 0x788
+  __DATA_CONST.__got: 0x820
+  __DATA_CONST.__const: 0x7f0
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2310
+  __DATA_CONST.__objc_selrefs: 0x2398
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x808
+  __AUTH_CONST.__auth_got: 0x7e8
   __AUTH_CONST.__const: 0x2f58
   __AUTH_CONST.__cfstring: 0x1c80
-  __AUTH_CONST.__objc_const: 0x9d08
+  __AUTH_CONST.__objc_const: 0x90d8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x9b8

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 65543E82-85EC-3AA2-A52E-89C24078518F
-  Functions: 2786
-  Symbols:   4733
-  CStrings:  2750
+  UUID: 631C1C43-3DCB-317E-9710-13CDE0FE05E2
+  Functions: 2789
+  Symbols:   4775
+  CStrings:  2740
 
Symbols:
+ +[CNAutocompleteFetchRequest makeTriageIdentifier].cold.1
+ +[CNAutocompleteInfrequentRecentResult comparators].cold.1
+ +[CNAutocompleteLocalContactResultTransformBuilder addressTypeForProperty:].cold.1
+ +[CNAutocompletePeopleSuggesterFeedback sharedInstance].cold.1
+ +[CNAutocompleteQueryCacheHelper cache_os_log].cold.1
+ +[CNAutocompleteRecentResult comparators].cold.1
+ +[CNAutocompleteResult comparators].cold.1
+ +[CNAutocompleteResult contactStoreForFetchingFullContacts].cold.1
+ +[CNAutocompleteResultTokenMatcher tokenizePhoneNumber:].cold.1
+ +[CNAutocompleteTokenMatcher tokensForNameString:].cold.1
+ +[_CNAPeopleSuggesterResultPrioritizer os_log].cold.1
+ CNALoggingContextDebug.cold.1
+ CNALoggingContextPerformance.cold.1
+ CNALoggingContextProbes.cold.1
+ CNALoggingContextSorting.cold.1
+ CNALoggingContextTriage.cold.1
+ _OBJC_CLASS_$_CNContactsUserDefaults
+ __115-[_CNAPeopleSuggesterResultPrioritizer applyPriorityOrderToResults:fetchRequest:andCompletePriorityResultsPromise:]_block_invoke.20
+ __76-[_CNAutocompletePeopleSuggesterPredictionSearchStrategyTask convertResults]_block_invoke.110
+ __76-[_CNAutocompletePeopleSuggesterPredictionSearchStrategyTask convertResults]_block_invoke.79
+ __76-[_CNAutocompletePeopleSuggesterPredictionSearchStrategyTask convertResults]_block_invoke.81
+ __84-[_CNAPeopleSuggesterResultPrioritizer partitionCandidatesForRanking:givenPrefixes:]_block_invoke.25
+ __84-[_CNAPeopleSuggesterResultPrioritizer partitionCandidatesForRanking:givenPrefixes:]_block_invoke.27
+ __84-[_CNAPeopleSuggesterResultPrioritizer partitionCandidatesForRanking:givenPrefixes:]_block_invoke.28
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ __block_literal_global.100
+ __block_literal_global.105
+ __block_literal_global.147
+ __block_literal_global.23
+ __block_literal_global.39
+ initABAutocompleteServerSearch.cold.1
+ initEKDirectorySearchOperation.cold.1
+ initEKDirectorySearchQuery.cold.1
+ initEKEphemeralCacheEventStoreProvider.cold.1
+ initEKEventStore.cold.1
+ initSGSuggestionsService.cold.1
+ init_PSAutocompleteSuggestion.cold.1
+ init_PSCNAutocompleteFeedback.cold.1
+ init_PSPredictionContext.cold.1
+ init_PSRecipient.cold.1
+ init_PSSuggester.cold.1
+ init_PSSuggestion.cold.1
- __115-[_CNAPeopleSuggesterResultPrioritizer applyPriorityOrderToResults:fetchRequest:andCompletePriorityResultsPromise:]_block_invoke.14
- __76-[_CNAutocompletePeopleSuggesterPredictionSearchStrategyTask convertResults]_block_invoke.104
- __76-[_CNAutocompletePeopleSuggesterPredictionSearchStrategyTask convertResults]_block_invoke.73
- __76-[_CNAutocompletePeopleSuggesterPredictionSearchStrategyTask convertResults]_block_invoke.75
- __84-[_CNAPeopleSuggesterResultPrioritizer partitionCandidatesForRanking:givenPrefixes:]_block_invoke.19
- __84-[_CNAPeopleSuggesterResultPrioritizer partitionCandidatesForRanking:givenPrefixes:]_block_invoke.21
- __84-[_CNAPeopleSuggesterResultPrioritizer partitionCandidatesForRanking:givenPrefixes:]_block_invoke.22
- ___swift_destroy_boxed_opaque_existential_1Tm
- __block_literal_global.141
- __block_literal_global.33
- __block_literal_global.94
- __block_literal_global.99
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_ContactsAutocomplete
CStrings:
+ "IDS declined to execute query. Continuing with empty status."
+ "sharedDefaults"
+ "shortNameFormatPrefersNicknames"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
