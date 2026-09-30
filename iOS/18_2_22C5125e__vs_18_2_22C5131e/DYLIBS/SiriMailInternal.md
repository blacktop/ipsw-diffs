## SiriMailInternal

> `/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal`

```diff

-3402.28.1.0.0
-  __TEXT.__text: 0xed30c
-  __TEXT.__auth_stubs: 0x4290
-  __TEXT.__const: 0x65b0
-  __TEXT.__cstring: 0x2554
-  __TEXT.__constg_swiftt: 0x22f0
-  __TEXT.__swift5_typeref: 0x38b6
-  __TEXT.__swift5_fieldmd: 0x1bb4
-  __TEXT.__oslogstring: 0x6987
+3402.31.3.0.0
+  __TEXT.__text: 0xf59b4
+  __TEXT.__auth_stubs: 0x4360
+  __TEXT.__const: 0x67a0
+  __TEXT.__cstring: 0x26f4
+  __TEXT.__constg_swiftt: 0x2434
+  __TEXT.__swift5_typeref: 0x3b38
+  __TEXT.__swift5_fieldmd: 0x1cc4
+  __TEXT.__oslogstring: 0x6af7
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x1b83
-  __TEXT.__swift5_assocty: 0x4f0
-  __TEXT.__swift5_proto: 0x2d0
-  __TEXT.__swift5_types: 0x1ac
+  __TEXT.__swift5_reflstr: 0x1c93
+  __TEXT.__swift5_assocty: 0x508
+  __TEXT.__swift5_proto: 0x2e8
+  __TEXT.__swift5_types: 0x1c0
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x80
-  __TEXT.__swift5_capture: 0x5e8
-  __TEXT.__unwind_info: 0x2e10
-  __TEXT.__eh_frame: 0x6130
+  __TEXT.__swift5_capture: 0x6d4
+  __TEXT.__unwind_info: 0x3098
+  __TEXT.__eh_frame: 0x67bc
   __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0xa4a
+  __TEXT.__objc_methname: 0xc76
   __TEXT.__objc_methtype: 0x1d1
-  __DATA_CONST.__got: 0x11c8
+  __DATA_CONST.__got: 0x1368
   __DATA_CONST.__const: 0x140
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x308
+  __DATA_CONST.__objc_selrefs: 0x3d8
   __DATA_CONST.__objc_protorefs: 0x60
-  __AUTH_CONST.__auth_got: 0x2148
-  __AUTH_CONST.__auth_ptr: 0x1878
-  __AUTH_CONST.__const: 0x2640
-  __AUTH_CONST.__objc_const: 0x2818
+  __AUTH_CONST.__auth_got: 0x21b0
+  __AUTH_CONST.__auth_ptr: 0x1850
+  __AUTH_CONST.__const: 0x2a78
+  __AUTH_CONST.__objc_const: 0x28f0
   __AUTH.__objc_data: 0x7a0
-  __AUTH.__data: 0x2ff0
-  __DATA.__data: 0x2800
-  __DATA.__bss: 0x5a80
-  __DATA.__common: 0x258
+  __AUTH.__data: 0x3108
+  __DATA.__data: 0x29a0
+  __DATA.__bss: 0x5d90
+  __DATA.__common: 0x260
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4459
-  Symbols:   2370
-  CStrings:  868
+  Functions: 4644
+  Symbols:   2488
+  CStrings:  912
 
Symbols:
+ _MDItemAdditionalRecipientEmailAddresses
+ _MDItemAdditionalRecipientPersons
+ _MDItemAdditionalRecipients
+ _MDItemAuthorEmailAddresses
+ _MDItemAuthorPersons
+ _MDItemAuthors
+ _MDItemContentCreationDate
+ _MDItemContentType
+ _MDItemHiddenAdditionalRecipientEmailAddresses
+ _MDItemHiddenAdditionalRecipientPersons
+ _MDItemHiddenAdditionalRecipients
+ _MDItemIsLikelyJunk
+ _MDItemIsUrgent
+ _MDItemMailboxes
+ _MDItemPrimaryRecipientEmailAddresses
+ _MDItemPrimaryRecipientPersons
+ _MDItemPrimaryRecipients
+ _MDItemRecipientEmailAddresses
+ _MDItemRecipients
+ _MDItemSnippet
+ _MDItemSubject
+ _MDItemTextContent
+ _MDMailDateReceived
+ _MDMailFlagged
+ _MDMailMessageID
+ _MDMailPriority
+ _MDMailRead
+ _MDMailRepliedTo
+ _OBJC_CLASS_$_CSPerson
+ _OBJC_CLASS_$_CSSearchableItem
+ _OBJC_CLASS_$_CSUserQuery
+ _OBJC_CLASS_$_CSUserQueryContext
+ _OBJC_CLASS_$_EMGeneratedSummary
+ _OBJC_CLASS_$_EMInternalPreferences
+ _OBJC_CLASS_$_NSComparisonPredicate
+ _OBJC_CLASS_$_NSCompoundPredicate
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSExpression
+ _OBJC_CLASS_$_NSPredicate
CStrings:
+ "#GetMail CatchUp is disabled, not fetching email summaries for %!l(MISSING)d messages"
+ "#GetMail CatchUp is enabled, fetch email summaries for %!l(MISSING)d messages"
+ "#GetMail applying date time range of past month"
+ "#ReadMailActingFlow user asked for general inbox read or general summary and CatchUp is enabled, read their highlights first"
+ "#ReadingUtil.fetchMailHighlights"
+ "#ReadingUtil.fetchMailHighlights found %!l(MISSING)d results"
+ "#ReadingUtil.fetchMailHighlights query string: %!s(MISSING)"
+ "FetchMailHighlights"
+ "ReadMail#HighlightsIntro"
+ "ReadMail#HighlightsSegue"
+ "ReadMail#ReadHighlight"
+ "_TtC16SiriMailInternal14CSQueryBuilder"
+ "andPredicateWithSubpredicates:"
+ "attributeSet"
+ "authorEmailAddresses"
+ "authorNames"
+ "authors"
+ "consideredUrgentHourLimit"
+ "ef_dateHoursAgo:"
+ "execute(queryString:)"
+ "expressionForConstantValue:"
+ "expressionForKeyPath:"
+ "handles"
+ "initWithLeftExpression:rightExpression:modifier:type:options:"
+ "initWithQueryString:queryContext:"
+ "initWithTimeIntervalSince1970:"
+ "isRequestToSummarize"
+ "isSingleHighlight"
+ "kMDItemEmailConversationID"
+ "orPredicateWithSubpredicates:"
+ "predicateFormat"
+ "predicates"
+ "preferenceEnabled:"
+ "public.email-message"
+ "setBundleIDs:"
+ "setCompletionHandler:"
+ "setEnableInstantAnswers:"
+ "setFetchAttributes:"
+ "setFoundItemsHandler:"
+ "setMaxCount:"
+ "start"
+ "timeIntervalSinceReferenceDate"
+ "uniqueIdentifier"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"NSError\"8"
- "#GetMail CatchUp is disabled, not fetching email summaries for messages"
- "#GetMail CatchUp is enabled, fetch email summaries for messages"

```
