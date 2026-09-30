## CoreSuggestionsInternals

> `/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals`

```diff

-1271.11.0.0.0
-  __TEXT.__text: 0x262954
-  __TEXT.__auth_stubs: 0x25d0
-  __TEXT.__objc_methlist: 0x14314
-  __TEXT.__const: 0x749a
-  __TEXT.__gcc_except_tab: 0xb300
-  __TEXT.__cstring: 0x3092d
-  __TEXT.__oslogstring: 0x220d6
+1276.9.0.2.0
+  __TEXT.__text: 0x26297c
+  __TEXT.__auth_stubs: 0x25b0
+  __TEXT.__objc_methlist: 0x15724
+  __TEXT.__const: 0x748a
   __TEXT.__dlopen_cstrs: 0x336
+  __TEXT.__gcc_except_tab: 0xb294
+  __TEXT.__cstring: 0x3092c
+  __TEXT.__oslogstring: 0x22318
   __TEXT.__ustring: 0xc4
-  __TEXT.__unwind_info: 0x81e8
-  __TEXT.__objc_classname: 0x29d0
-  __TEXT.__objc_methname: 0x3b6b7
-  __TEXT.__objc_methtype: 0x708d
-  __TEXT.__objc_stubs: 0x2ab60
-  __DATA_CONST.__got: 0x2160
-  __DATA_CONST.__const: 0xb5a8
-  __DATA_CONST.__objc_classlist: 0xb18
+  __TEXT.__unwind_info: 0x80d8
+  __TEXT.__objc_classname: 0x29e3
+  __TEXT.__objc_methname: 0x3ba90
+  __TEXT.__objc_methtype: 0x70d3
+  __TEXT.__objc_stubs: 0x2ae20
+  __DATA_CONST.__got: 0x2180
+  __DATA_CONST.__const: 0xb538
+  __DATA_CONST.__objc_classlist: 0xb28
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcef0
+  __DATA_CONST.__objc_selrefs: 0xd0f8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x758
   __DATA_CONST.__objc_arraydata: 0x37c8
-  __AUTH_CONST.__auth_got: 0x1300
+  __AUTH_CONST.__auth_got: 0x12f0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x4a08
-  __AUTH_CONST.__cfstring: 0x258c0
-  __AUTH_CONST.__objc_const: 0x219a0
-  __AUTH_CONST.__objc_intobj: 0x1068
+  __AUTH_CONST.__cfstring: 0x25960
+  __AUTH_CONST.__objc_const: 0x1f9a0
+  __AUTH_CONST.__objc_intobj: 0x1278
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0xe58
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH.__objc_data: 0x2468
+  __AUTH.__objc_data: 0x2378
   __AUTH.__data: 0x200
-  __DATA.__objc_ivar: 0x1470
+  __DATA.__objc_ivar: 0x1478
   __DATA.__data: 0x1a60
-  __DATA.__bss: 0x748
+  __DATA.__bss: 0x758
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x4a88
+  __DATA_DIRTY.__objc_data: 0x4c18
   __DATA_DIRTY.__data: 0x388
-  __DATA_DIRTY.__bss: 0x9a00
+  __DATA_DIRTY.__bss: 0x99f0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9979
-  Symbols:   12745
-  CStrings:  18138
+  Functions: 9907
+  Symbols:   12771
+  CStrings:  18175
 
Symbols:
+ _DUExtractionAttributeKeyDetailedEventStatus
+ _DUExtractionAttributeValueEventStatusPendingConfirmation
+ _OBJC_CLASS_$_SGEntityTagsHelper
+ _OBJC_CLASS_$_SGEventSchemaCreator
+ _OBJC_METACLASS_$_SGEntityTagsHelper
+ _OBJC_METACLASS_$_SGEventSchemaCreator
- _fmod
- _fmodf
CStrings:
+ "\a\x1e"
+ "@\"PSUSummarizationPipeline\""
+ "@64@0:8@16@24@32@40B48B52B56B60"
+ "DetailedEventStatus"
+ "SGEKCalendarAdapter addEvent: New event not eligible for donation."
+ "SGEKCalendarAdapter: Checking eligibility of %@ event for calendar donation"
+ "SGEKCalendarAdapter: Checking eligibility of structured event donation to Calendar"
+ "SGEKCalendarAdapter: Event not belonging to structured event categories. Early returning as an eligible event."
+ "SGEKCalendarAdapter: Event reservationID present: %@"
+ "SGEKCalendarAdapter: Found nil structured category for tag: %@"
+ "SGEKCalendarAdapter: New event eligible for donation - %@"
+ "SGEntityTagsHelper"
+ "SGTicketedTransportationEventSchemaCreator: unidentified category of ticketed transportation - %@"
+ "T@\"NSNumber\",R,GmailCategories,V_mailCategories"
+ "^(?i)(fw|fwd|forward)\\s*:\\s*"
+ "_isMailCategoryUnsupportedForLLMExtraction:"
+ "_isStructuredEventEligibleForDonation:"
+ "_mailCategories"
+ "_newEventEligibleForDonation:"
+ "_shouldProcessMailMessage:havingSignificantSender:"
+ "_subjectResemblesForwardedMailSubjectForMail:"
+ "_summarizationPipeline"
+ "_transportationSchemaCreatorFromTransportType:"
+ "addEvent:%{sensitive}@ bailing because event is not valid for spotlight donation"
+ "deleteItemsWithIdentifiers:bundleId:"
+ "eventSourceMetadata"
+ "extractSchemasFromEntityTags:"
+ "filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:"
+ "flightArrivalTimeZone"
+ "flightDepartureTimeZone"
+ "hotelTimeZone"
+ "initWithContactStore:"
+ "isMessageCandidateForExtraction:"
+ "isTimePresentInDURawDateTime:"
+ "isValidEventForSpotlightDonation:"
+ "mailCategories"
+ "mlExtractionEnabledForTextMessage"
+ "processItem:receivedDate:positionInReceivedItems:"
+ "public.voice-audio"
+ "reservationIDPresentInEventSchema:"
+ "schemasInEntityTagsBelongsToPendingConfirmationEvent:"
+ "searchableItemsDidUpdate:"
+ "searchableItemsForIdentifiers:searchableItemsHandler:"
+ "setEventStatus:"
+ "setEventUpdateStatus:"
+ "setFlightArrivalAirportAddressSynonyms:"
+ "setFlightDepartureAirportAddressSynonyms:"
+ "setTimeIsUnknown:"
+ "shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:"
+ "startTimeIsUnknown"
+ "synonymAirportNamesForAirportCode:"
+ "update"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\">24"
- "\a\x1d"
- "@60@0:8@16@24@32@40B48B52B56"
- "CatchUp"
- "Event not complete. Not donating events to events bundle."
- "PrecomputeSmartReplies"
- "PrecomputeSmartRepliesMail"
- "_accessSummarizationPipelineForBundleId:block:"
- "author:"
- "handleDeletionOfItemsWithIdentifiers:bundleIdentifier:"
- "isAuthorTag"
- "mlExtractionEnabledForTextMessage:"
- "sharedPipelineWithContactStore:incomingBundleId:"
- "shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:"
- "unidentified category of ticketed transportation - %@"
- "v16@?0@\"PSUSummarizationPipeline\"8"

```
