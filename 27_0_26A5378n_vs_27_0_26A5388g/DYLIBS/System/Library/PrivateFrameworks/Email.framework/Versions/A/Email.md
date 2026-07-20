## Email

> `/System/Library/PrivateFrameworks/Email.framework/Versions/A/Email`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-3895.100.17.0.0
-  __TEXT.__text: 0xef060
-  __TEXT.__objc_methlist: 0xd984
-  __TEXT.__gcc_except_tab: 0x1bf40
+3897.100.8.1.1
+  __TEXT.__text: 0xef28c
+  __TEXT.__objc_methlist: 0xd94c
+  __TEXT.__gcc_except_tab: 0x1bfa4
   __TEXT.__const: 0x18cc
-  __TEXT.__cstring: 0xc86f
+  __TEXT.__cstring: 0xc8af
   __TEXT.__oslogstring: 0x6bb3
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x170

   __TEXT.__swift5_capture: 0x48
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8450
+  __TEXT.__unwind_info: 0x8440
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19a8
-  __DATA_CONST.__objc_classlist: 0x5b0
+  __DATA_CONST.__const: 0x19b8
+  __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68d8
+  __DATA_CONST.__objc_selrefs: 0x68c0
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x488
+  __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0x1e8
   __DATA_CONST.__got: 0xd60
-  __AUTH_CONST.__const: 0x54d0
-  __AUTH_CONST.__cfstring: 0xaaa0
-  __AUTH_CONST.__objc_const: 0x17df8
+  __AUTH_CONST.__const: 0x54f0
+  __AUTH_CONST.__cfstring: 0xab00
+  __AUTH_CONST.__objc_const: 0x17cd8
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xa68
-  __AUTH.__objc_data: 0x1020
-  __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0xd10
+  __AUTH.__objc_data: 0x2a0
+  __AUTH.__data: 0x158
+  __DATA.__objc_ivar: 0xd08
   __DATA.__data: 0x29e8
-  __DATA.__bss: 0x21e0
-  __DATA_DIRTY.__objc_data: 0x2b28
-  __DATA_DIRTY.__data: 0x240
-  __DATA_DIRTY.__bss: 0xcd0
+  __DATA.__bss: 0x21d0
+  __DATA_DIRTY.__objc_data: 0x3858
+  __DATA_DIRTY.__data: 0x268
+  __DATA_DIRTY.__bss: 0xce0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5399
-  Symbols:   11943
-  CStrings:  2225
+  Functions: 5397
+  Symbols:   11934
+  CStrings:  2228
 
Symbols:
+ +[EMQuery _sortDescriptorsByNormalizingLegacyKeyPaths:]
+ -[EMBaseMessageListItem searchRelevanceScore]
+ -[EMBaseMessageListItem setSearchRelevanceScore:]
+ -[EMDiagnosticInfoGatherer databaseStatisticsForcingRefresh:completionHandler:]
+ -[EMMessageListItemChange searchRelevanceScore]
+ -[EMMessageListItemChange setSearchRelevanceScore:]
+ -[EMThread searchRelevanceScore]
+ -[EMThread setSearchRelevanceScore:]
+ OBJC_IVAR_$_EMBaseMessageListItem._searchRelevanceScore
+ OBJC_IVAR_$_EMMessageListItemChange._searchRelevanceScore
+ OBJC_IVAR_$_EMThread._searchRelevanceScore
+ _EMMessageListItemKeyPathSearchRelevanceScore
+ _EMPersistenceStatisticsKeyCalculatedAt
+ _EMUserDefaultNeverCollectIndexingDiagnostics
+ ___55+[EMQuery _sortDescriptorsByNormalizingLegacyKeyPaths:]_block_invoke
+ _objc_msgSend$databaseStatisticsForcingRefresh:completionHandler:
+ _objc_msgSend$searchRelevanceScore
+ _objc_msgSend$setSearchRelevanceScore:
+ _objc_msgSend$sortDescriptorWithKey:ascending:selector:
+ _sortDescriptorsByNormalizingLegacyKeyPaths:.onceToken
+ _sortDescriptorsByNormalizingLegacyKeyPaths:.sLegacyKeyPathAliases
- -[CSSearchableItem(SFMailRankingSignals) em_isSemanticMatch]
- -[CSSearchableItem(SFMailRankingSignals) em_isSyntacticMatch]
- -[EMBaseMessageListItem searchRelevanceRank]
- -[EMBaseMessageListItem setSearchRelevanceRank:]
- -[EMMessageListItemChange searchRelevanceRank]
- -[EMMessageListItemChange setSearchRelevanceRank:]
- -[EMSearchResultMetadata .cxx_destruct]
- -[EMSearchResultMetadata initWithRankingSignals:rankPosition:]
- -[EMSearchResultMetadata rankPosition]
- -[EMSearchResultMetadata rankingSignals]
- -[EMThread searchRelevanceRank]
- -[EMThread setSearchRelevanceRank:]
- OBJC_IVAR_$_EMBaseMessageListItem._searchRelevanceRank
- OBJC_IVAR_$_EMMessageListItemChange._searchRelevanceRank
- OBJC_IVAR_$_EMSearchResultMetadata._rankPosition
- OBJC_IVAR_$_EMSearchResultMetadata._rankingSignals
- OBJC_IVAR_$_EMThread._searchRelevanceRank
- _EMMessageListItemKeyPathSearchRelevanceRank
- _OBJC_CLASS_$_EMSearchResultMetadata
- _OBJC_METACLASS_$_EMSearchResultMetadata
- __OBJC_$_INSTANCE_METHODS_EMSearchResultMetadata
- __OBJC_$_INSTANCE_VARIABLES_EMSearchResultMetadata
- __OBJC_$_PROP_LIST_CSSearchableItem_$_SFMailRankingSignals
- __OBJC_$_PROP_LIST_EMSearchResultMetadata
- __OBJC_CLASS_RO_$_EMSearchResultMetadata
- __OBJC_METACLASS_RO_$_EMSearchResultMetadata
- _objc_msgSend$em_isSemanticMatch
- _objc_msgSend$em_isSyntacticMatch
- _objc_msgSend$searchRelevanceRank
- _objc_msgSend$setSearchRelevanceRank:
CStrings:
+ "%@\n\tConversationID:%@\n\tSubject:%@\n\tSenderList:%@\n\tToList:%@\n\tCCList:%@\n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)\n\tFlags:%@\n\tConversationNotificationLevel:%ld\n\tCategory:%@\n\tBusinessLogoID:%@\n\tIsVIP:%@\n\tIsBlocked:%@\n\tSearchResultType:%ld\n\tSearchRelevanceScore:%@\n\tUnsubscribeType:%ld\n\tDate:%@\n\tDisplayDate:%@\n\tMailboxes:%@\n\tCount:%lu"
+ "%@\n\tConversationID:%@\n\tSubject:%@\n\tSenderList:%@\n\tToList:%@\n\tCCList:%@\n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)\n\tFlags:%@\n\tConversationNotificationLevel:%ld\n\tCategory:%@\n\tBusinessLogoID:%@\n\tIsVIP:%@\n\tIsBlocked:%@\n\tSearchResultType:%ld\n\tSearchRelevanceScore:%@\n\tUnsubscribeType:%ld\n\tDate:%@\n\tDisplayDate:%@\n\tMailboxes:%@\n\tCount:%lu\n\tSupportsArchiving:%@ \n\tShouldArchive:%@\n\tdisplayMessageItemID:%@"
+ "%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tCategory:%@\n\tBusinessID:%llu\n\tBusinessLogoID:%@\n\tisAuthenticated:%@\n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceScore:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)"
+ "%@\n\tObjectID:%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tCategory:%@\n\tBusinessID:%llu\n\tBusinessLogoID:%@\n\tisAuthenticated:%@\n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceScore:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tRemind Me:%@ \n\tFollow Up:%@ \n\tSummary:%@ \n\tGenerated Summary:%@ (isUrgent = %@)\n\tSupportsArchiving:%@ \n\tShouldArchive:%@"
+ "%@ \n\tConversationID:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceScore:%@ \n\tunsubscribeType:%ld \n\tDate:%@ \n\tSupports Archiving:%@ \n\tShould Archive By Default:%@"
+ "EFPropertyKey_searchRelevanceScore"
+ "NeverCollectIndexingDiagnostics"
+ "calculatedAt"
+ "searchRelevanceScore"
+ "searchRelevanceScore: %@"
- "%@\n\tConversationID:%@\n\tSubject:%@\n\tSenderList:%@\n\tToList:%@\n\tCCList:%@\n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)\n\tFlags:%@\n\tConversationNotificationLevel:%ld\n\tCategory:%@\n\tBusinessLogoID:%@\n\tIsVIP:%@\n\tIsBlocked:%@\n\tSearchResultType:%ld\n\tSearchRelevanceRank:%@\n\tUnsubscribeType:%ld\n\tDate:%@\n\tDisplayDate:%@\n\tMailboxes:%@\n\tCount:%lu"
- "%@\n\tConversationID:%@\n\tSubject:%@\n\tSenderList:%@\n\tToList:%@\n\tCCList:%@\n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)\n\tFlags:%@\n\tConversationNotificationLevel:%ld\n\tCategory:%@\n\tBusinessLogoID:%@\n\tIsVIP:%@\n\tIsBlocked:%@\n\tSearchResultType:%ld\n\tSearchRelevanceRank:%@\n\tUnsubscribeType:%ld\n\tDate:%@\n\tDisplayDate:%@\n\tMailboxes:%@\n\tCount:%lu\n\tSupportsArchiving:%@ \n\tShouldArchive:%@\n\tdisplayMessageItemID:%@"
- "%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tCategory:%@\n\tBusinessID:%llu\n\tBusinessLogoID:%@\n\tisAuthenticated:%@\n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceRank:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)"
- "%@\n\tObjectID:%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tCategory:%@\n\tBusinessID:%llu\n\tBusinessLogoID:%@\n\tisAuthenticated:%@\n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceRank:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tRemind Me:%@ \n\tFollow Up:%@ \n\tSummary:%@ \n\tGenerated Summary:%@ (isUrgent = %@)\n\tSupportsArchiving:%@ \n\tShouldArchive:%@"
- "%@ \n\tConversationID:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceRank:%@ \n\tunsubscribeType:%ld \n\tDate:%@ \n\tSupports Archiving:%@ \n\tShould Archive By Default:%@"
- "EFPropertyKey_searchRelevanceRank"
- "searchRelevanceRank: %@"
```
