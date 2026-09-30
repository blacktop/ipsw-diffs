## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2387.1.0.0.0
-  __TEXT.__text: 0x155ef0
+2391.1.0.0.0
+  __TEXT.__text: 0x15658c
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0xf018
-  __TEXT.__const: 0x2a00
-  __TEXT.__cstring: 0x30f4f
+  __TEXT.__objc_methlist: 0xf048
+  __TEXT.__const: 0x2a10
+  __TEXT.__cstring: 0x30fdf
   __TEXT.__gcc_except_tab: 0x4ccc
-  __TEXT.__oslogstring: 0x9afb
+  __TEXT.__oslogstring: 0x9c7b
   __TEXT.__ustring: 0x8d6
   __TEXT.__dlopen_cstrs: 0xd1
   __TEXT.__swift5_typeref: 0x1e6

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x94
-  __TEXT.__unwind_info: 0x33a8
+  __TEXT.__unwind_info: 0x33b8
   __TEXT.__objc_classname: 0x14eb
-  __TEXT.__objc_methname: 0x2b95c
-  __TEXT.__objc_methtype: 0x3119
-  __TEXT.__objc_stubs: 0x1cd20
+  __TEXT.__objc_methname: 0x2ba12
+  __TEXT.__objc_methtype: 0x312b
+  __TEXT.__objc_stubs: 0x1ce20
   __DATA_CONST.__got: 0x2098
   __DATA_CONST.__const: 0xfcf8
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8ec0
+  __DATA_CONST.__objc_selrefs: 0x8ee8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0x1248
   __AUTH_CONST.__auth_got: 0xe80
-  __AUTH_CONST.__const: 0x2818
-  __AUTH_CONST.__cfstring: 0x2b380
+  __AUTH_CONST.__const: 0x2870
+  __AUTH_CONST.__cfstring: 0x2b3a0
   __AUTH_CONST.__objc_const: 0x185a8
   __AUTH_CONST.__objc_intobj: 0x32b8
   __AUTH_CONST.__objc_doubleobj: 0x2a0

   __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0x153c
   __DATA.__data: 0x1238
-  __DATA.__bss: 0xc28
+  __DATA.__bss: 0xc38
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x23f0
   __DATA_DIRTY.__data: 0x298
-  __DATA_DIRTY.__bss: 0x4c80
+  __DATA_DIRTY.__bss: 0x4c70
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7CFDC385-77EB-36E2-B415-DC60F96184F4
-  Functions: 6400
-  Symbols:   22152
-  CStrings:  19524
+  UUID: F3A5F0D4-D9BF-3F1C-8D48-7799FB5B67CB
+  Functions: 6410
+  Symbols:   22171
+  CStrings:  19532
 
Symbols:
+ +[SPSearchAppEntity metadataSpecialCasedAppEntityBundles]
+ +[SSResultBuilder getWhitespaceCharacterAtIndex:ofString:]
+ +[SSSectionBuilderHandler cachedValueForKey:cache:computeHandler:]
+ +[SSSectionBuilderHandler defaultAppURLForResult:typeCache:urlCache:]
+ +[SSSectionBuilderHandler filterResultsFromSections:queryContext:]
+ -[SPKResponse debugDescription]
+ _SPQueryKindToSFSpotlightBrowsingSearchScope
+ ___block_literal_global.553
+ _objc_msgSend$corespotlightFinished
+ _objc_msgSend$delayResponse:forQuery:
+ _objc_msgSend$filterResultsFromSections:queryContext:
+ _objc_msgSend$getWhitespaceCharacterAtIndex:ofString:
+ _objc_msgSend$metadataFinished
+ _objc_msgSend$metadataSpecialCasedAppEntityBundles
+ _objc_msgSend$noChangeInResultsSinceLastResponse
+ _objc_msgSend$parsecFinished
+ _objc_msgSend$queryResponseComplete
- +[SSResultBuilder getCharacterIfWhitespaceAtIndex:ofString:]
- ___block_literal_global.552
- _objc_msgSend$getCharacterIfWhitespaceAtIndex:ofString:
CStrings:
+ "<response:[%@][%@], userQuery:%@, queryId:%lu, topHitIsIn:%d, noChange:%d, parsec:%d, metadata:%d, corespotlight:%d, complete:%d, sections:%@>"
+ "@40@0:8@16@24@?32"
+ "[SpotlightRanking] [SearchTool] [Dedupe] %lu events from SearchIndexer with domainIdentifier %@ in favor of Mail result with identifier %@"
+ "[SpotlightRanking] [SearchTool] [Dedupe] event from SearchIndexer with identifier %@ in favor of Mail result with domainIdentifier %@"
+ "[SpotlightRanking] [SearchTool] [Dedupe] removing FolderEntity (from notes bundle) as NoteEntity is present at a higher rank."
+ "[SpotlightRanking] [SearchTool] [Dedupe] result %@ with MDItemContentURL"
+ "[SpotlightRanking] [SearchTool] [Dedupe] result %@ with com_apple_mail_messageID=%@"
+ "[SpotlightRanking] [SearchTool] [Dedupe] result %@ with com_apple_mail_message_id_header=%@"
+ "[SpotlightRanking] [SearchTool] [Dedupe] result %@ with eventMessageIdentifier"
+ "[SpotlightRanking] [SearchTool] [Featurization] [Calendar] ID:%@, title:%@, calendarEventRecipientsEmailAddresses: %d, personMatchInRecipient:%d, personMatchInAuthor:%d, personMatchOtherThanRecipient:%d."
+ "[SpotlightRanking] [SearchTool] [Featurization] [Calendar] [PerfectMatch] Found one on one search term in the calendar item with id %@."
+ "[SpotlightRanking] [SearchTool] [Featurization] [Calendar] [PerfectMatch] ID:%@, title:%@, Perfect match for one on one meeting queries with single recipient calendar item. Either no person token or person tokens matched in author/recipient."
+ "[SpotlightRanking] [SearchTool] [Featurization] [Files] ID:%@, title:%@ Marked document as AllSearchTermMatch due to perfect keyword match score."
+ "[SpotlightRanking] [SearchTool] [Featurization] [Mail] For ID:%@, subject:%@, found meCard email:%@ match in additionalRecipients"
+ "[SpotlightRanking] [SearchTool] [Featurization] [Mail] For ID:%@, subject:%@, found meCard email:%@ match in primaryRecipients"
+ "[SpotlightRanking] [SearchTool] [Post-filtering] qid=[%llu] query=[%@] filter based on pre-extraction date name=[%@] bundle=%@ identifier=%@ startDate=%@"
+ "[SpotlightRanking] [SearchTool] [Post-filtering] query=%@ filter %lu result for [%@]"
+ "[SpotlightRanking] [SearchTool] [Post-filtering] query=%@ filter result identifier=%@ due to absolute threshold"
+ "[SpotlightRanking] [SearchTool] [Post-filtering] query=%@ filter result identifier=%@ due to absolute threshold on L2. score=%f threshold=%f"
+ "[SpotlightRanking] [SearchTool] [Post-filtering] query=%@ filter result identifier=%@ due to perfect match document availability."
+ "[SpotlightRanking] [SearchTool] [Post-filtering] query=%@ filter result identifier=%@ due to perfect title match freeform availability."
+ "[SpotlightRanking] [SearchTool] [Post-filtering] query=%@ filter result identifier=%@ due to perfect title match note availability."
+ "[SpotlightRanking] [SearchTool] [Post-filtering] query=%@ filter result identifier=%@ due to perfect title match reminders availability."
+ "[SpotlightRanking] [SearchTool] [Post-filtering] query=%@ filter result identifier=%@ due to singular condition"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] [Wallet] for future-seeking or card event query=%@, filtered wallet item with title=%@ identifier=%@ MDItemIdentifier=%@ due to non-null transaction type"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] [Wallet] for future-seeking query=%@ at queryTime=%f, filtered event with title=%@ identifier=%@ MDItemIdentifier=%@ walletBoardingPassDepartureDateTime=%@ as the result is in the past"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] [Wallet] for future-seeking query=%@, filtered wallet item with title=%@ identifier=%@ MDItemIdentifier=%@ due to expiration date = %@ in the past"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] [Wallet] for past-seeking query=%@ at queryTime=%f, filtered with title=%@ identifier=%@ MDItemIdentifier=%@ walletBoardingPassDepartureDateTime=%@ as the result is in the future"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] [Wallet] for query=%@, filtered with title=%@ identifier=%@ MDItemIdentifier=%@ due to unexpected QU predicted intent for boarding pass"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] qid=[%llu] query=%@ filter %d-days-old Mail and Messages results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for event type and future intent mostRecentTimeToQueryInMinutesForFreshness=%ld"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] qid=[%llu] query=%@ filter %d-days-old results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for event type and future intent mostRecentTimeToQueryInMinutesForFreshness=%ld"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] qid=[%llu] query=%@ filter %d-days-old results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for future intent without event type mostRecentTimeToQueryInMinutesForFreshness=%ld"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] qid=[%llu] query=%@ filter %d-month(s)-old Mail and Messages results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for future intent without event type mostRecentTimeToQueryInMinutesForFreshness=%ld"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] qid=[%llu] query=[%@] filter contact result [%@] for non contact intent"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] qid=[%llu] query=[%@] filter phone call history [%@] identifier=%@ for non phone/contact intent"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] qid=[%llu] query=[%@] filter result [%@] bundle=%@ identifier=%@ MDItemIdentifier=%@ for next/last startDueDateToNowInSeconds=%ld"
+ "[SpotlightRanking] [SearchTool] [Pre-filtering] qid=[%llu][bundle=\"%@\"][query=\"%@\"][type=%d][id=\"%@\"] filter result (\"%@\") for low embeddingSimilarity=%0.2f (< %.2f) and low pommesL1Score=%0.2f (< %.2f)"
+ "[SpotlightRanking] [SearchTool] [Sorting] %@ query=%@ identifier=%@ name=[%@] due to %@"
+ "cachedValueForKey:cache:computeHandler:"
+ "defaultAppURLForResult:typeCache:urlCache:"
+ "delayResponse:forQuery:"
+ "filterResultsFromSections:queryContext:"
+ "getWhitespaceCharacterAtIndex:ofString:"
+ "metadataSpecialCasedAppEntityBundles"
- "[SpotlightRanking] [SearchTool] %@ query=%@ identifier=%@ name=[%@] due to %@"
- "[SpotlightRanking] [SearchTool] [Calendar] ID:%@, title:%@, calendarEventRecipientsEmailAddresses: %d, personMatchInRecipient:%d, personMatchInAuthor:%d, personMatchOtherThanRecipient:%d."
- "[SpotlightRanking] [SearchTool] [Calendar] [PerfectMatch] Found one on one search term in the calendar item with id %@."
- "[SpotlightRanking] [SearchTool] [Calendar] [PerfectMatch] ID:%@, title:%@, Perfect match for one on one meeting queries with single recipient calendar item. Either no person token or person tokens matched in author/recipient."
- "[SpotlightRanking] [SearchTool] [Files] ID:%@, title:%@ Marked document as AllSearchTermMatch due to perfect keyword match score."
- "[SpotlightRanking] [SearchTool] [Filtering] qid=[%llu] query=[%@] filter based on pre-extraction date name=[%@] bundle=%@ identifier=%@ startDate=%@"
- "[SpotlightRanking] [SearchTool] [Filtering] query=%@ filter result identifier=%@ due to absolute threshold"
- "[SpotlightRanking] [SearchTool] [Filtering] query=%@ filter result identifier=%@ due to absolute threshold on L2. score=%f threshold=%f"
- "[SpotlightRanking] [SearchTool] [Filtering] query=%@ filter result identifier=%@ due to perfect match document availability."
- "[SpotlightRanking] [SearchTool] [Filtering] query=%@ filter result identifier=%@ due to perfect title match freeform availability."
- "[SpotlightRanking] [SearchTool] [Filtering] query=%@ filter result identifier=%@ due to perfect title match note availability."
- "[SpotlightRanking] [SearchTool] [Filtering] query=%@ filter result identifier=%@ due to perfect title match reminders availability."
- "[SpotlightRanking] [SearchTool] [Filtering] query=%@ filter result identifier=%@ due to singular condition"
- "[SpotlightRanking] [SearchTool] [Mail] For ID:%@, subject:%@, found meCard email:%@ match in additionalRecipients"
- "[SpotlightRanking] [SearchTool] [Mail] For ID:%@, subject:%@, found meCard email:%@ match in primaryRecipients"
- "[SpotlightRanking] [SearchTool] [Wallet] for future-seeking or card event query=%@, filtered wallet item with title=%@ identifier=%@ MDItemIdentifier=%@ due to non-null transaction type"
- "[SpotlightRanking] [SearchTool] [Wallet] for future-seeking query=%@ at queryTime=%f, filtered event with title=%@ identifier=%@ MDItemIdentifier=%@ walletBoardingPassDepartureDateTime=%@ as the result is in the past"
- "[SpotlightRanking] [SearchTool] [Wallet] for future-seeking query=%@, filtered wallet item with title=%@ identifier=%@ MDItemIdentifier=%@ due to expiration date = %@ in the past"
- "[SpotlightRanking] [SearchTool] [Wallet] for past-seeking query=%@ at queryTime=%f, filtered with title=%@ identifier=%@ MDItemIdentifier=%@ walletBoardingPassDepartureDateTime=%@ as the result is in the future"
- "[SpotlightRanking] [SearchTool] [Wallet] for query=%@, filtered with title=%@ identifier=%@ MDItemIdentifier=%@ due to unexpected QU predicted intent for boarding pass"
- "[SpotlightRanking] [SearchTool] dedupe %lu events from SearchIndexer with domainIdentifier %@ in favor of Mail result with identifier %@"
- "[SpotlightRanking] [SearchTool] dedupe event from SearchIndexer with identifier %@ in favor of Mail result with domainIdentifier %@"
- "[SpotlightRanking] [SearchTool] dedupe result %@ with MDItemContentURL"
- "[SpotlightRanking] [SearchTool] dedupe result %@ with com_apple_mail_messageID=%@"
- "[SpotlightRanking] [SearchTool] dedupe result %@ with com_apple_mail_message_id_header=%@"
- "[SpotlightRanking] [SearchTool] dedupe result %@ with eventMessageIdentifier"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=%@ filter %d-days-old Mail and Messages results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for event type and future intent mostRecentTimeToQueryInMinutesForFreshness=%ld"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=%@ filter %d-days-old results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for event type and future intent mostRecentTimeToQueryInMinutesForFreshness=%ld"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=%@ filter %d-days-old results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for future intent without event type mostRecentTimeToQueryInMinutesForFreshness=%ld"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=%@ filter %d-month(s)-old Mail and Messages results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for future intent without event type mostRecentTimeToQueryInMinutesForFreshness=%ld"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=[%@] filter contact result [%@] for non contact intent"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=[%@] filter phone call history [%@] identifier=%@ for non phone/contact intent"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=[%@] filter result [%@] bundle=%@ identifier=%@ MDItemIdentifier=%@ for next/last startDueDateToNowInSeconds=%ld"
- "[SpotlightRanking] [SearchTool] qid=[%llu][bundle=\"%@\"][query=\"%@\"][type=%d][id=\"%@\"] filter result (\"%@\") for low embeddingSimilarity=%0.2f (< %.2f) and low pommesL1Score=%0.2f (< %.2f)"
- "[SpotlightRanking] [SearchTool] query=%@ filter %lu result for [%@]"
- "[SpotlightRanking] [SearchTool] removing FolderEntity (from notes bundle) as NoteEntity is present at a higher rank."
- "getCharacterIfWhitespaceAtIndex:ofString:"

```
