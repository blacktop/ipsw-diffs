## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0xa3df8
-  __TEXT.__auth_stubs: 0x1e10
-  __TEXT.__objc_methlist: 0x3fb4
-  __TEXT.__const: 0x378
-  __TEXT.__cstring: 0x7c27
-  __TEXT.__oslogstring: 0xa18b
-  __TEXT.__gcc_except_tab: 0x4168
+2374.0.1.0.0
+  __TEXT.__text: 0xad328
+  __TEXT.__auth_stubs: 0x1ea0
+  __TEXT.__objc_methlist: 0x43f4
+  __TEXT.__const: 0x388
+  __TEXT.__cstring: 0x833d
+  __TEXT.__oslogstring: 0xa9c2
+  __TEXT.__gcc_except_tab: 0x4214
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x21a8
-  __TEXT.__objc_classname: 0x48e
-  __TEXT.__objc_methname: 0xd755
-  __TEXT.__objc_methtype: 0x22d8
-  __TEXT.__objc_stubs: 0xb020
-  __DATA_CONST.__got: 0x9e8
-  __DATA_CONST.__const: 0x3ab0
-  __DATA_CONST.__objc_classlist: 0x158
+  __TEXT.__unwind_info: 0x2230
+  __TEXT.__objc_classname: 0x4cf
+  __TEXT.__objc_methname: 0xea90
+  __TEXT.__objc_methtype: 0x24da
+  __TEXT.__objc_stubs: 0xb9c0
+  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__const: 0x3c30
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3300
+  __DATA_CONST.__objc_selrefs: 0x35b8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__objc_arraydata: 0x448
-  __AUTH_CONST.__auth_got: 0xf20
-  __AUTH_CONST.__const: 0xf68
-  __AUTH_CONST.__cfstring: 0x6c80
-  __AUTH_CONST.__objc_const: 0x5540
-  __AUTH_CONST.__objc_arrayobj: 0x330
-  __AUTH_CONST.__objc_intobj: 0x180
+  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_arraydata: 0x490
+  __AUTH_CONST.__auth_got: 0xf68
+  __AUTH_CONST.__const: 0x1028
+  __AUTH_CONST.__cfstring: 0x7680
+  __AUTH_CONST.__objc_const: 0x5ab0
+  __AUTH_CONST.__objc_arrayobj: 0x3d8
+  __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x404
-  __DATA.__data: 0x930
-  __DATA.__bss: 0x1a9
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__data: 0x220
-  __DATA_DIRTY.__bss: 0x4d0
-  __DATA_DIRTY.__common: 0x10
+  __DATA.__objc_ivar: 0x46c
+  __DATA.__data: 0x868
+  __DATA.__bss: 0x111
+  __DATA.__common: 0x4
+  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__data: 0x2e8
+  __DATA_DIRTY.__bss: 0x5b8
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 8B0A7328-BF3E-3726-86B5-334DBF60D688
-  Functions: 2681
-  Symbols:   9164
-  CStrings:  5522
+  UUID: C35F1554-2CCA-34E0-B623-9A7F735DDC9F
+  Functions: 2820
+  Symbols:   9600
+  CStrings:  5879
 
Symbols:
+ +[SpotlightReceiverConnectionManager sharedInstantManager]
+ +[SpotlightReceiverConnectionManager sharedInstantManager].cold.1
+ +[SpotlightReceiverConnectionManager sharedScheduledManager]
+ +[SpotlightReceiverConnectionManager sharedScheduledManager].cold.1
+ +[SpotlightSender jobForTextUnderstanding:]
+ +[SpotlightSender setupInstantSender]
+ +[SpotlightSender setupInstantSender].cold.1
+ +[SpotlightSender(SpotlightScheduledSender) addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:]
+ +[SpotlightSender(SpotlightScheduledSender) deleteSearchableItemsInJournalFd:atOffset:size:indexType:protectionClass:serialNumber:journalCookie:client:completionHandler:]
+ +[SpotlightSender(SpotlightScheduledSender) reset]
+ +[SpotlightSender(SpotlightScheduledSender) setupScheduledSender]
+ +[SpotlightSender(SpotlightScheduledSender) setupScheduledSender].cold.1
+ +[SpotlightSender(SpotlightScheduledSender) supportedConfigs]
+ +[SpotlightSender(SpotlightScheduledSender) suspend]
+ -[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:].cold.1
+ -[SPConcreteCoreSpotlightIndexer fetchMeCard:isNotCreateNewIndex:group:]
+ -[SPConcreteCoreSpotlightIndexer fetchMeCard:isNotCreateNewIndex:group:].cold.1
+ -[SPConcreteCoreSpotlightIndexer issuePhotosReindexIfNeeded:group:]
+ -[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:].cold.1
+ -[SPConcreteCoreSpotlightIndexer runOneFixup:group:]
+ -[SPConcreteCoreSpotlightIndexer runOtherFixups:state:]
+ -[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]
+ -[SPConcreteCoreSpotlightIndexer setHasPhotosOrText].cold.1
+ -[SPConcreteCoreSpotlightIndexer updateContainersAndScores:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsFromMe:fullName:emails:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsFromMeNot:fullName:emails:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsFromMeRanking:nameTokens:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsFromMeRankingNot:nameTokens:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMe:group:order:aliasName:fullName:nameTokens:givenNameTokens:nonGivenNameTokens:emails:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMe:nameTokens:alias:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMe:runOtherFixups:force:group:state:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeIfNotAlready:group:order:aliasName:fullName:nameTokens:givenNameTokens:nonGivenNameTokens:emails:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeIfNotAlready:group:state:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeNot:nameTokens:alias:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRanking:nameTokens:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingNot:nameTokens:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingOCR:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingOCRNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingOCRTextContentMatch:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingOCRTextContentMatchNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingPreExtraction:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingPreExtractionNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingSpan:fullName:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingSpanNot:fullName:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingTextContentMatch:nameTokens:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingTextContentMatchNot2:nameTokens:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingTextContentMatchNot:nameTokens:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingToken:nameTokens:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeRankingTokenNot:nameTokens:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeTextContentMatch:nameTokens:alias:onlyIfNotAlready:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeTextContentMatchNot:nameTokens:alias:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateEmailContentURLAttr:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateEmailLocalParts:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateGroups:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateIndexRankingDates:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateMeCardInfo:middleName:familyName:emailAddresses:isFirstTimeCheck:isNotCreateNewIndex:group:]
+ -[SPConcreteCoreSpotlightIndexer updateMeCardInfo:middleName:familyName:emailAddresses:isFirstTimeCheck:isNotCreateNewIndex:group:].cold.1
+ -[SPConcreteCoreSpotlightIndexer updateNotes:group:forceMerge:]
+ -[SPConcreteCoreSpotlightIndexer updateRankingDates:group:forceMerge:]
+ -[SPCoreSpotlightIndexer asyncOpenIndex:forInit:readOnly:]
+ -[SpotlightReceiverConfig .cxx_destruct]
+ -[SpotlightReceiverConfig INIntentClassNames]
+ -[SpotlightReceiverConfig bundleIDs]
+ -[SpotlightReceiverConfig client]
+ -[SpotlightReceiverConfig contentTypes]
+ -[SpotlightReceiverConfig disableBundleIDs]
+ -[SpotlightReceiverConfig disableContentTypes]
+ -[SpotlightReceiverConfig disableDomainIDs]
+ -[SpotlightReceiverConfig domainIDs]
+ -[SpotlightReceiverConfig donationAttributes]
+ -[SpotlightReceiverConfig excludeAttributes]
+ -[SpotlightReceiverConfig identifier]
+ -[SpotlightReceiverConfig includeDeletedItems]
+ -[SpotlightReceiverConfig includeLanguage]
+ -[SpotlightReceiverConfig includeUpdatedItems]
+ -[SpotlightReceiverConfig initForClient:]
+ -[SpotlightReceiverConfig name]
+ -[SpotlightReceiverConfig needsHTML]
+ -[SpotlightReceiverConfig needsText]
+ -[SpotlightReceiverConfig optionalAttributes]
+ -[SpotlightReceiverConfig priority]
+ -[SpotlightReceiverConfig processes]
+ -[SpotlightReceiverConfig requireBacklogItems]
+ -[SpotlightReceiverConfig requirePriorityItems]
+ -[SpotlightReceiverConfig requiredAttributes]
+ -[SpotlightReceiverConfig setBundleIDs:]
+ -[SpotlightReceiverConfig setContentTypes:]
+ -[SpotlightReceiverConfig setDisableBundleIDs:]
+ -[SpotlightReceiverConfig setDisableContentTypes:]
+ -[SpotlightReceiverConfig setDisableDomainIDs:]
+ -[SpotlightReceiverConfig setDomainIDs:]
+ -[SpotlightReceiverConfig setDonationAttributes:]
+ -[SpotlightReceiverConfig setExcludeAttributes:]
+ -[SpotlightReceiverConfig setINIntentClassNames:]
+ -[SpotlightReceiverConfig setIncludeDeletedItems:]
+ -[SpotlightReceiverConfig setIncludeLanguage:]
+ -[SpotlightReceiverConfig setIncludeUpdatedItems:]
+ -[SpotlightReceiverConfig setName:]
+ -[SpotlightReceiverConfig setNeedsHTML:]
+ -[SpotlightReceiverConfig setNeedsText:]
+ -[SpotlightReceiverConfig setOptionalAttributes:]
+ -[SpotlightReceiverConfig setPriority:]
+ -[SpotlightReceiverConfig setProcesses:]
+ -[SpotlightReceiverConfig setRequireBacklogItems:]
+ -[SpotlightReceiverConfig setRequirePriorityItems:]
+ -[SpotlightReceiverConfig setRequiredAttributes:]
+ -[SpotlightReceiverConfig setSupportedQuery:]
+ -[SpotlightReceiverConfig setTrackingAttributes:]
+ -[SpotlightReceiverConfig setUnsupportedQuery:]
+ -[SpotlightReceiverConfig setVersionName:]
+ -[SpotlightReceiverConfig setVersionValue:]
+ -[SpotlightReceiverConfig supportedQuery]
+ -[SpotlightReceiverConfig trackingAttributes]
+ -[SpotlightReceiverConfig unsupportedQuery]
+ -[SpotlightReceiverConfig versionName]
+ -[SpotlightReceiverConfig versionValue]
+ -[SpotlightReceiverConfig wantsBundleID:]
+ -[SpotlightReceiverConfig wantsContentType:]
+ -[SpotlightReceiverConfig wantsDomainID:]
+ -[SpotlightReceiverConfig wantsINIntentClassNames:]
+ -[SpotlightReceiverConnection configs]
+ -[SpotlightReceiverConnection deleteWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:completionHandler:]
+ -[SpotlightReceiverConnection indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]
+ -[SpotlightReceiverConnection initWithServiceName:client:configPath:]
+ -[SpotlightReceiverConnection primaryConfig]
+ -[SpotlightReceiverConnection reset]
+ -[SpotlightReceiverConnection resume]
+ -[SpotlightReceiverConnection setPrimaryConfig:]
+ -[SpotlightReceiverConnection startSetupForClient:configurationValues:]
+ -[SpotlightReceiverConnection suspend]
+ -[SpotlightReceiverConnection suspended]
+ -[SpotlightReceiverConnection updateConfigsForClient:configurationValues:]
+ -[SpotlightReceiverConnectionManager .cxx_destruct]
+ -[SpotlightReceiverConnectionManager clientConnection:]
+ -[SpotlightReceiverConnectionManager clients]
+ -[SpotlightReceiverConnectionManager connectionIdentifiers]
+ -[SpotlightReceiverConnectionManager initWithConnectionInfo:configurationInfo:]
+ -[SpotlightReceiverConnectionManager setConnectionIdentifiers:]
+ GCC_except_table1000
+ GCC_except_table1005
+ GCC_except_table1010
+ GCC_except_table1016
+ GCC_except_table1032
+ GCC_except_table1083
+ GCC_except_table1085
+ GCC_except_table1090
+ GCC_except_table1131
+ GCC_except_table1137
+ GCC_except_table1242
+ GCC_except_table1243
+ GCC_except_table1311
+ GCC_except_table1314
+ GCC_except_table1316
+ GCC_except_table1317
+ GCC_except_table1482
+ GCC_except_table1511
+ GCC_except_table159
+ GCC_except_table166
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table189
+ GCC_except_table19
+ GCC_except_table190
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table206
+ GCC_except_table22
+ GCC_except_table223
+ GCC_except_table225
+ GCC_except_table227
+ GCC_except_table238
+ GCC_except_table246
+ GCC_except_table27
+ GCC_except_table276
+ GCC_except_table283
+ GCC_except_table293
+ GCC_except_table30
+ GCC_except_table318
+ GCC_except_table32
+ GCC_except_table365
+ GCC_except_table366
+ GCC_except_table375
+ GCC_except_table376
+ GCC_except_table404
+ GCC_except_table41
+ GCC_except_table432
+ GCC_except_table435
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table447
+ GCC_except_table478
+ GCC_except_table487
+ GCC_except_table501
+ GCC_except_table506
+ GCC_except_table520
+ GCC_except_table521
+ GCC_except_table570
+ GCC_except_table571
+ GCC_except_table572
+ GCC_except_table597
+ GCC_except_table658
+ GCC_except_table682
+ GCC_except_table708
+ GCC_except_table712
+ GCC_except_table716
+ GCC_except_table744
+ GCC_except_table770
+ GCC_except_table787
+ GCC_except_table800
+ GCC_except_table824
+ GCC_except_table825
+ GCC_except_table833
+ GCC_except_table870
+ GCC_except_table940
+ GCC_except_table945
+ GCC_except_table951
+ GCC_except_table952
+ GCC_except_table954
+ GCC_except_table961
+ GCC_except_table974
+ GCC_except_table986
+ GCC_except_table995
+ _MDItemComment
+ _MDItemCreator
+ _MDItemDerivedIsFromMe
+ _MDItemDerivedIsFromMeRanking
+ _MDItemDerivedIsMeRanking
+ _MDItemDerivedIsMeRankingOCR
+ _MDItemDerivedIsMeRankingOCRTextContentMatch
+ _MDItemDerivedIsMeRankingPreExtraction
+ _MDItemDerivedIsMeRankingSpan
+ _MDItemDerivedIsMeRankingTextContentMatch
+ _MDItemDerivedIsMeRankingToken
+ _MDItemDescription
+ _MDItemEventCustomerNames
+ _MDItemEventName
+ _MDItemFileProviderFilename
+ _MDItemFilename
+ _MDItemLastEditorName
+ _MDItemSubject
+ _MDItemTitle
+ _MDItemUserSharedSentSender
+ _MDItemUserSharedSentSenderHandle
+ _OBJC_CLASS_$_SpotlightReceiverConfig
+ _OBJC_CLASS_$_SpotlightReceiverConnectionManager
+ _OBJC_IVAR_$_SpotlightReceiverConfig._INIntentClassNames
+ _OBJC_IVAR_$_SpotlightReceiverConfig._bundleIDs
+ _OBJC_IVAR_$_SpotlightReceiverConfig._client
+ _OBJC_IVAR_$_SpotlightReceiverConfig._contentTypes
+ _OBJC_IVAR_$_SpotlightReceiverConfig._disableBundleIDs
+ _OBJC_IVAR_$_SpotlightReceiverConfig._disableContentTypes
+ _OBJC_IVAR_$_SpotlightReceiverConfig._disableDomainIDs
+ _OBJC_IVAR_$_SpotlightReceiverConfig._domainIDs
+ _OBJC_IVAR_$_SpotlightReceiverConfig._donationAttributes
+ _OBJC_IVAR_$_SpotlightReceiverConfig._excludeAttributes
+ _OBJC_IVAR_$_SpotlightReceiverConfig._includeDeletedItems
+ _OBJC_IVAR_$_SpotlightReceiverConfig._includeLanguage
+ _OBJC_IVAR_$_SpotlightReceiverConfig._includeUpdatedItems
+ _OBJC_IVAR_$_SpotlightReceiverConfig._name
+ _OBJC_IVAR_$_SpotlightReceiverConfig._needsHTML
+ _OBJC_IVAR_$_SpotlightReceiverConfig._needsText
+ _OBJC_IVAR_$_SpotlightReceiverConfig._negativeSet
+ _OBJC_IVAR_$_SpotlightReceiverConfig._optionalAttributes
+ _OBJC_IVAR_$_SpotlightReceiverConfig._positiveSet
+ _OBJC_IVAR_$_SpotlightReceiverConfig._priority
+ _OBJC_IVAR_$_SpotlightReceiverConfig._processes
+ _OBJC_IVAR_$_SpotlightReceiverConfig._requireBacklogItems
+ _OBJC_IVAR_$_SpotlightReceiverConfig._requirePriorityItems
+ _OBJC_IVAR_$_SpotlightReceiverConfig._requiredAttributes
+ _OBJC_IVAR_$_SpotlightReceiverConfig._supportedQuery
+ _OBJC_IVAR_$_SpotlightReceiverConfig._trackingAttributes
+ _OBJC_IVAR_$_SpotlightReceiverConfig._unsupportedQuery
+ _OBJC_IVAR_$_SpotlightReceiverConfig._versionName
+ _OBJC_IVAR_$_SpotlightReceiverConfig._versionValue
+ _OBJC_IVAR_$_SpotlightReceiverConnection._configs
+ _OBJC_IVAR_$_SpotlightReceiverConnection._primaryConfig
+ _OBJC_IVAR_$_SpotlightReceiverConnection._suspended
+ _OBJC_IVAR_$_SpotlightReceiverConnectionManager._connectionIdentifiers
+ _OBJC_IVAR_$_SpotlightReceiverConnectionManager._connections
+ _OBJC_IVAR_$_SpotlightReceiverConnectionManager._state
+ _OBJC_METACLASS_$_SpotlightReceiverConfig
+ _OBJC_METACLASS_$_SpotlightReceiverConnectionManager
+ _SISetHasPhotos
+ _SISetHasText
+ __OBJC_$_CLASS_METHODS_SpotlightReceiverConnectionManager
+ __OBJC_$_CLASS_METHODS_SpotlightSender(SpotlightScheduledSender)
+ __OBJC_$_INSTANCE_METHODS_SpotlightReceiverConfig
+ __OBJC_$_INSTANCE_METHODS_SpotlightReceiverConnectionManager
+ __OBJC_$_INSTANCE_VARIABLES_SpotlightReceiverConfig
+ __OBJC_$_INSTANCE_VARIABLES_SpotlightReceiverConnectionManager
+ __OBJC_$_PROP_LIST_SpotlightReceiverConfig
+ __OBJC_$_PROP_LIST_SpotlightReceiverConnectionManager
+ __OBJC_CLASS_RO_$_SpotlightReceiverConfig
+ __OBJC_CLASS_RO_$_SpotlightReceiverConnectionManager
+ __OBJC_METACLASS_RO_$_SpotlightReceiverConfig
+ __OBJC_METACLASS_RO_$_SpotlightReceiverConnectionManager
+ __SICopyMeEmailAddresses
+ __SIGetMeFullName
+ __SIGetMeGivenNameTokens
+ __SIGetMeNonGivenNameTokens
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__110__pop_heapB8ne200100INS_17_ClassicAlgPolicyE22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
+ __ZNSt3__110__pop_heapB8ne200100INS_17_ClassicAlgPolicyE27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__114__split_bufferINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEERNS5_IS8_EEE17__destruct_at_endB8ne200100EPS8_
+ __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEERNS_9allocatorIS8_EEE17__destruct_at_endB8ne200100EPS8_
+ __ZNSt3__117__floyd_sift_downB8ne200100INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__117__floyd_sift_downB8ne200100INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocator_destroyB8ne200100INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEENS_16reverse_iteratorIPS9_EESD_EEvRT_T0_T1_
+ __ZNSt3__119__allocator_destroyB8ne200100INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEPS9_SB_EEvRT_T0_T1_
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEPSA_EEED2B8ne200100Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEPS9_EEvRT_T0_SE_SE_
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE22__base_destruct_at_endB8ne200100EPS8_
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE24__emplace_back_slow_pathIJS8_EEEPS8_DpOT_
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE9push_backB8ne200100EOS8_
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf
+ __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZSt9terminatev
+ __ZnwmSt19__type_descriptor_t
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1609
+ ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1461
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3193
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1578
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1586
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1592
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1598
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1601
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1593
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1599
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1602
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1602.cold.1
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1594
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1594.cold.1
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1600
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1647
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.cold.1
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.cold.2
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.cold.3
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke_2
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke_3
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke_3.cold.1
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke_3.cold.2
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2496
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2498
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2498.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2501
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2501.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2502
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2502.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2503
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1485
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1493
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1493.cold.1
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1489
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1490
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1491
+ ___127-[SpotlightReceiverConnection deleteWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:completionHandler:]_block_invoke
+ ___127-[SpotlightReceiverConnection deleteWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:completionHandler:]_block_invoke.339
+ ___127-[SpotlightReceiverConnection deleteWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:completionHandler:]_block_invoke.cold.1
+ ___154-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke
+ ___154-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke.338
+ ___154-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1401
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1401.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1401.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1420
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1422
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1422.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1422.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1425
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1425.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1425.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1428
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1421
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1313
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1313.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1313.cold.2
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1313.cold.3
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1313.cold.4
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1340
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1352
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1384
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1389
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1393
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1396
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1364
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1385
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1390
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1390.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1397
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1365
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_4.1366
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.319
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.320
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.327
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.328
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke_2
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke_3
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke_4
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke_4.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2230
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2243
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2252
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2256
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2261
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2262
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2263
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2275
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2279
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2280
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2287
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2291
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2293
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2293.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2294
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2296
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2296.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2297
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2299
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2299.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2303
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2305
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2306
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2311
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2311.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2311.cold.2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2312
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2316
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2319
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2324
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2331
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2332
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2337
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2337.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2337.cold.2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2239
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2248
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2283
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2288
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2307
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2307.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2317
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2320
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2320.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2334
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2334.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2341
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2240
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2240.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2318
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2318.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2342
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.2403
+ ___36-[SpotlightReceiverConnection reset]_block_invoke
+ ___36-[SpotlightReceiverConnection reset]_block_invoke.342
+ ___36-[SpotlightReceiverConnection reset]_block_invoke.cold.1
+ ___37+[SpotlightSender setupInstantSender]_block_invoke
+ ___37-[SpotlightReceiverConnection resume]_block_invoke
+ ___37-[SpotlightReceiverConnection resume]_block_invoke.341
+ ___37-[SpotlightReceiverConnection resume]_block_invoke.cold.1
+ ___38-[SpotlightReceiverConnection suspend]_block_invoke
+ ___38-[SpotlightReceiverConnection suspend]_block_invoke.340
+ ___38-[SpotlightReceiverConnection suspend]_block_invoke.cold.1
+ ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2487
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.587
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.587.cold.1
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.588
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.596
+ ___40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2454
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3204
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3205
+ ___41-[SpotlightReceiverConnection startSetup]_block_invoke.299
+ ___41-[SpotlightReceiverConnection startSetup]_block_invoke.299.cold.1
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2177
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2177.cold.1
+ ___48-[SpotlightReceiverConnection deleteFromBundle:]_block_invoke.357
+ ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1449
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2394
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2398
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2398.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2398.cold.2
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2399
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2399.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2400
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2400.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2401
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1731
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke_2
+ ___55-[SPConcreteCoreSpotlightIndexer runOtherFixups:state:]_block_invoke
+ ___55-[SpotlightReceiverConnection deleteAllUserActivities:]_block_invoke.353
+ ___58+[SpotlightReceiverConnectionManager sharedInstantManager]_block_invoke
+ ___58-[SPCoreSpotlightIndexer asyncOpenIndex:forInit:readOnly:]_block_invoke
+ ___58-[SpotlightReceiverConnection deleteFromBundle:sinceDate:]_block_invoke.356
+ ___59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.603
+ ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.265
+ ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.266
+ ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.270
+ ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.271
+ ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.279
+ ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.279.cold.1
+ ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.281
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2382
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2383
+ ___59-[SpotlightReceiverConnection purgeFromBundle:identifiers:]_block_invoke.349
+ ___60+[SpotlightReceiverConnectionManager sharedScheduledManager]_block_invoke
+ ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1155
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.286
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.287
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.293
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.293.cold.1
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1289
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1292
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1295
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.648
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.648.cold.1
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.649
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.649.cold.1
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.650
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.650.cold.1
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.651
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.655
+ ___62-[SpotlightReceiverConnection donateRelevantActions:bundleID:]_block_invoke.365
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.621
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.621.cold.1
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.625
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.625.cold.1
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.627
+ ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2378
+ ___65+[SpotlightSender(SpotlightScheduledSender) setupScheduledSender]_block_invoke
+ ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.1047
+ ___66-[SpotlightReceiverConnection deleteFromBundle:domainIdentifiers:]_block_invoke.348
+ ___67-[SPConcreteCoreSpotlightIndexer issuePhotosReindexIfNeeded:group:]_block_invoke
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2187
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2188
+ ___67-[SpotlightReceiverConnection deleteFromBundle:encodedIdentifiers:]_block_invoke.345
+ ___71-[SpotlightReceiverConnection addUserActions:bundleID:protectionClass:]_block_invoke.352
+ ___71-[SpotlightReceiverConnection startSetupForClient:configurationValues:]_block_invoke
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1149
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1150
+ ___72-[SPConcreteCoreSpotlightIndexer fetchMeCard:isNotCreateNewIndex:group:]_block_invoke
+ ___72-[SpotlightReceiverConnection deleteFromBundle:contentType:identifiers:]_block_invoke.347
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1539
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1539.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1543
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1543.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1544
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1558
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1559
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1563
+ ___76-[SPConcreteCoreSpotlightIndexer updateDerivedIsMeIfNotAlready:group:state:]_block_invoke
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1431
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1435
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1441
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1441.cold.1
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1436
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1065
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1070
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1104
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1110
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1112
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1114
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1114.cold.1
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1119
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1120
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1123
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1126
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1134
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1138
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1066
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1072
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1111
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1113
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1118
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.1075
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.1078
+ ___78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.613
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1188
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1189
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1196
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1196.cold.1
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2538
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2539
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2540
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2432
+ ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1298
+ ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2621
+ ___81-[SpotlightReceiverConnection deleteAllInteractionsWithBundleID:protectionClass:]_block_invoke.363
+ ___82-[SpotlightReceiverConnection indexFromBundle:protectionClass:items:itemsContent:]_block_invoke.329
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.258
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.258.cold.1
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.258.cold.2
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3192
+ ___85-[SPConcreteCoreSpotlightIndexer updateDerivedIsMe:runOtherFixups:force:group:state:]_block_invoke
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3141
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3141.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3143
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3145
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3145.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3146
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3147
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3147.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3148
+ ___87-[SpotlightReceiverConnection addInteraction:intentClassName:bundleID:protectionClass:]_block_invoke.360
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2706
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2713
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2733
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2767
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2771
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2775
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2795
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2807
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2820
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3014
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3015
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3022
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3026
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3027
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3031
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3035
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3054
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2714
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2799
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2821
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3076
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3080
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3111
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3112
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3116
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3129
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3134
+ ___90-[SpotlightReceiverConnection deleteInteractionsWithIdentifiers:bundleID:protectionClass:]_block_invoke.361
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1159
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1160
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2567
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2568
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.667
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.668
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.669
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.670
+ ___95-[SpotlightReceiverConnection deleteInteractionsWithGroupIdentifiers:bundleID:protectionClass:]_block_invoke.362
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1500
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1510
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1511
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2425
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2425.cold.1
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2426
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2430
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2431
+ ___99-[SpotlightReceiverConnection deleteUserActivitiesWithPersistentIdentifiers:bundleID:retainedData:]_block_invoke.354
+ ____sendPhotosReindexABCReport_block_invoke
+ ____sendPhotosReindexABCReport_block_invoke.cold.1
+ ___block_descriptor_100_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72r80r88r_e13_v24?0^8^B16lr72l8r80l8s32l8s40l8r88l8s48l8s56l8s64l8
+ ___block_descriptor_114_e8_32s40s48s56s64s72s80r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
+ ___block_descriptor_116_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_43_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r40r_e13_v24?0^8^B16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40ls32l8r40l8r48l8
+ ___block_descriptor_57_e8_32s40s48w_e18_v20?0^{__SI=}8C16lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_59_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56bs_e22_v20?0^{__CFData=}8i16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s_e18_v20?0^{__SI=}8C16ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_82_e8_32s40s48s56s64bs_e18_v20?0^{__SI=}8C16ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56r_e18_v20?0^{__SI=}8C16ls32l8s40l8r56l8s48l8
+ ___block_literal_global.1019
+ ___block_literal_global.1038
+ ___block_literal_global.1041
+ ___block_literal_global.1043
+ ___block_literal_global.1061
+ ___block_literal_global.1068
+ ___block_literal_global.1074
+ ___block_literal_global.1077
+ ___block_literal_global.1080
+ ___block_literal_global.1122
+ ___block_literal_global.1125
+ ___block_literal_global.1128
+ ___block_literal_global.1140
+ ___block_literal_global.1284
+ ___block_literal_global.1287
+ ___block_literal_global.1291
+ ___block_literal_global.1294
+ ___block_literal_global.1297
+ ___block_literal_global.1342
+ ___block_literal_global.1354
+ ___block_literal_global.1399
+ ___block_literal_global.1424
+ ___block_literal_global.1427
+ ___block_literal_global.1495
+ ___block_literal_global.1604
+ ___block_literal_global.1657
+ ___block_literal_global.1667
+ ___block_literal_global.2157
+ ___block_literal_global.2162
+ ___block_literal_global.2168
+ ___block_literal_global.217
+ ___block_literal_global.2173
+ ___block_literal_global.2190
+ ___block_literal_global.2192
+ ___block_literal_global.2194
+ ___block_literal_global.2214
+ ___block_literal_global.2227
+ ___block_literal_global.2229
+ ___block_literal_global.2233
+ ___block_literal_global.2258
+ ___block_literal_global.2282
+ ___block_literal_global.2290
+ ___block_literal_global.2340
+ ___block_literal_global.24
+ ___block_literal_global.2406
+ ___block_literal_global.2420
+ ___block_literal_global.2422
+ ___block_literal_global.2424
+ ___block_literal_global.2434
+ ___block_literal_global.2473
+ ___block_literal_global.2478
+ ___block_literal_global.2480
+ ___block_literal_global.2482
+ ___block_literal_global.2489
+ ___block_literal_global.25
+ ___block_literal_global.2525
+ ___block_literal_global.2563
+ ___block_literal_global.2570
+ ___block_literal_global.2654
+ ___block_literal_global.285
+ ___block_literal_global.289
+ ___block_literal_global.2939
+ ___block_literal_global.2944
+ ___block_literal_global.2949
+ ___block_literal_global.2954
+ ___block_literal_global.2959
+ ___block_literal_global.2964
+ ___block_literal_global.2969
+ ___block_literal_global.2974
+ ___block_literal_global.2979
+ ___block_literal_global.3151
+ ___block_literal_global.3203
+ ___block_literal_global.3216
+ ___block_literal_global.34
+ ___block_literal_global.3742
+ ___block_literal_global.38
+ ___block_literal_global.3801
+ ___block_literal_global.3850
+ ___block_literal_global.3858
+ ___block_literal_global.3860
+ ___block_literal_global.3897
+ ___block_literal_global.3904
+ ___block_literal_global.489
+ ___block_literal_global.532
+ ___block_literal_global.590
+ ___block_literal_global.619
+ ___block_literal_global.644
+ ___clang_call_terminate
+ ___cxa_begin_catch
+ ___isDebugVerboseMode_block_invoke
+ ___logForCSLogCategoryItems_block_invoke
+ ___processItemsForImportInner_block_invoke.3818
+ __sendPhotosReindexABCReport
+ _createEqualANDQueryForGivenNameTokens
+ _createEqualORQueryForFullNamePrefix
+ _createEqualORQueryPrefix
+ _createNotEqualANDQueryForFullNamePrefix
+ _createNotEqualANDQueryPrefix
+ _createNotEqualORQueryForGivenNameTokens
+ _dispatch_queue_get_label
+ _isDebugVerboseMode
+ _isDebugVerboseMode.cold.1
+ _isDebugVerboseMode.debugEnabled
+ _isDebugVerboseMode.onceToken
+ _logForCSLogCategoryItems
+ _logForCSLogCategoryItems.cold.1
+ _logForCSLogCategoryItems.onceToken
+ _logForCSLogCategoryItems.sQueryLog
+ _objc_msgSend$INIntentClassNames
+ _objc_msgSend$asyncOpenIndex:forInit:readOnly:
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$client
+ _objc_msgSend$clients
+ _objc_msgSend$configs
+ _objc_msgSend$connectionIdentifiers
+ _objc_msgSend$contentTypes
+ _objc_msgSend$copyNSStringOrDictArrayFromXPCArray:
+ _objc_msgSend$deleteWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:completionHandler:
+ _objc_msgSend$dictionary:setStringOrDictionaryArray:forKey:
+ _objc_msgSend$fetchLastClientStateForBundleID:clientStateName:options:completionHandler:
+ _objc_msgSend$fetchMeCard:isNotCreateNewIndex:group:
+ _objc_msgSend$indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:
+ _objc_msgSend$initForClient:
+ _objc_msgSend$initWithConnectionInfo:configurationInfo:
+ _objc_msgSend$initWithServiceName:client:configPath:
+ _objc_msgSend$isMessagesBundle:
+ _objc_msgSend$isTimeSensitive
+ _objc_msgSend$issuePhotosReindexIfNeeded:group:
+ _objc_msgSend$jobForTextUnderstanding:
+ _objc_msgSend$lastLoadedBundleVersion
+ _objc_msgSend$name
+ _objc_msgSend$needsHTML
+ _objc_msgSend$needsText
+ _objc_msgSend$primaryConfig
+ _objc_msgSend$priority
+ _objc_msgSend$reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:
+ _objc_msgSend$reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:group:forceMerge:
+ _objc_msgSend$reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:
+ _objc_msgSend$requiredAttributes
+ _objc_msgSend$reset
+ _objc_msgSend$runOneFixup:group:
+ _objc_msgSend$runOtherFixups:state:
+ _objc_msgSend$setContentTypes:
+ _objc_msgSend$setDisableBundleIDs:
+ _objc_msgSend$setDisableContentTypes:
+ _objc_msgSend$setDisableDomainIDs:
+ _objc_msgSend$setDomainIDs:
+ _objc_msgSend$setDonationAttributes:
+ _objc_msgSend$setExcludeAttributes:
+ _objc_msgSend$setHasPhotosOrText
+ _objc_msgSend$setINIntentClassNames:
+ _objc_msgSend$setIncludeDeletedItems:
+ _objc_msgSend$setIncludeLanguage:
+ _objc_msgSend$setIncludeUpdatedItems:
+ _objc_msgSend$setIsTimeSensitive:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNeedsHTML:
+ _objc_msgSend$setNeedsText:
+ _objc_msgSend$setOptionalAttributes:
+ _objc_msgSend$setProcesses:
+ _objc_msgSend$setRequireBacklogItems:
+ _objc_msgSend$setRequirePriorityItems:
+ _objc_msgSend$setRequiredAttributes:
+ _objc_msgSend$setSupportedQuery:
+ _objc_msgSend$setTrackingAttributes:
+ _objc_msgSend$setUnsupportedQuery:
+ _objc_msgSend$setVersionName:
+ _objc_msgSend$setVersionValue:
+ _objc_msgSend$setWantsHTML:
+ _objc_msgSend$setWantsText:
+ _objc_msgSend$setupInstantSender
+ _objc_msgSend$sharedInstantManager
+ _objc_msgSend$sharedScheduledManager
+ _objc_msgSend$startSetupForClient:configurationValues:
+ _objc_msgSend$suspended
+ _objc_msgSend$updateConfigsForClient:configurationValues:
+ _objc_msgSend$updateContainersAndScores:group:forceMerge:
+ _objc_msgSend$updateDerivedIsFromMe:fullName:emails:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsFromMeNot:fullName:emails:group:forceMerge:
+ _objc_msgSend$updateDerivedIsFromMeRanking:nameTokens:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsFromMeRankingNot:nameTokens:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMe:group:order:aliasName:fullName:nameTokens:givenNameTokens:nonGivenNameTokens:emails:
+ _objc_msgSend$updateDerivedIsMe:nameTokens:alias:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMe:runOtherFixups:force:group:state:
+ _objc_msgSend$updateDerivedIsMeIfNotAlready:group:order:aliasName:fullName:nameTokens:givenNameTokens:nonGivenNameTokens:emails:
+ _objc_msgSend$updateDerivedIsMeIfNotAlready:group:state:
+ _objc_msgSend$updateDerivedIsMeNot:nameTokens:alias:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRanking:nameTokens:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingNot:nameTokens:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingOCR:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingOCRNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingOCRTextContentMatch:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingOCRTextContentMatchNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingPreExtraction:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingPreExtractionNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingSpan:fullName:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingSpanNot:fullName:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingTextContentMatch:nameTokens:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingTextContentMatchNot2:nameTokens:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingTextContentMatchNot:nameTokens:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingToken:nameTokens:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeRankingTokenNot:nameTokens:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeTextContentMatch:nameTokens:alias:onlyIfNotAlready:group:forceMerge:
+ _objc_msgSend$updateDerivedIsMeTextContentMatchNot:nameTokens:alias:group:forceMerge:
+ _objc_msgSend$updateEmailContentURLAttr:group:forceMerge:
+ _objc_msgSend$updateEmailLocalParts:group:forceMerge:
+ _objc_msgSend$updateGroups:group:forceMerge:
+ _objc_msgSend$updateIndexRankingDates:group:forceMerge:
+ _objc_msgSend$updateMeCardInfo:middleName:familyName:emailAddresses:isFirstTimeCheck:isNotCreateNewIndex:group:
+ _objc_msgSend$updateNotes:group:forceMerge:
+ _objc_msgSend$updateRankingDates:group:forceMerge:
+ _objc_msgSend$wantsBundleID:
+ _objc_msgSend$wantsContentType:
+ _objc_msgSend$wantsINIntentClassNames:
+ _sConnectionManager
+ _setupInstantSender.onceToken
+ _setupScheduledSender.onceToken
+ _sharedInstantManager.onceToken
+ _sharedInstantManager.sInstantConnectionManager
+ _sharedScheduledManager.onceToken
+ _sharedScheduledManager.sScheduledConnectionManager
- +[SpotlightReceiverConnection setup]
- +[SpotlightReceiverConnection setup].cold.1
- +[SpotlightSender setup]
- -[CSThresholdedTrigger .cxx_destruct]
- -[CSThresholdedTrigger actionCounts]
- -[CSThresholdedTrigger countThreshold]
- -[CSThresholdedTrigger incrementAndCheckPerformActionForKey:]
- -[CSThresholdedTrigger initWithCountThreshold:timeInterval:]
- -[CSThresholdedTrigger lastActionDates]
- -[CSThresholdedTrigger setActionCounts:]
- -[CSThresholdedTrigger setCountThreshold:]
- -[CSThresholdedTrigger setLastActionDates:]
- -[CSThresholdedTrigger setTimeInterval:]
- -[CSThresholdedTrigger timeInterval]
- -[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]
- -[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:].cold.1
- -[SPConcreteCoreSpotlightIndexer fetchMeCard:isNotCreateNewIndex:]
- -[SPConcreteCoreSpotlightIndexer fetchMeCard:isNotCreateNewIndex:].cold.1
- -[SPConcreteCoreSpotlightIndexer issuePhotosReindexIfNeeded:]
- -[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]
- -[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:].cold.1
- -[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]
- -[SPConcreteCoreSpotlightIndexer updateContainersAndScores:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedFromToIsMeNameAdded:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedFromToIsMeNameUpdated:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedFromToMeEmailAdded:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedFromToMeEmailUpdated:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedIsFromToMe:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedIsMe:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedIsMe:nameTokens:alias:onlyIfNotAlready:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeIfNotAlready:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeNot:nameTokens:alias:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeTextContentMatch:nameTokens:alias:onlyIfNotAlready:]
- -[SPConcreteCoreSpotlightIndexer updateDerivedIsMeTextContentMatchNot:nameTokens:alias:]
- -[SPConcreteCoreSpotlightIndexer updateEmailContentURLAttr:]
- -[SPConcreteCoreSpotlightIndexer updateEmailLocalParts:]
- -[SPConcreteCoreSpotlightIndexer updateGroups:]
- -[SPConcreteCoreSpotlightIndexer updateIndexRankingDates:]
- -[SPConcreteCoreSpotlightIndexer updateMeCardInfo:middleName:familyName:emailAddresses:isFirstTimeCheck:isNotCreateNewIndex:]
- -[SPConcreteCoreSpotlightIndexer updateMeCardInfo:middleName:familyName:emailAddresses:isFirstTimeCheck:isNotCreateNewIndex:].cold.1
- -[SPConcreteCoreSpotlightIndexer updateNotes:]
- -[SPConcreteCoreSpotlightIndexer updateRankingDates:]
- -[SpotlightReceiverConnection INIntentClassNames]
- -[SpotlightReceiverConnection _wantsBundleID:]
- -[SpotlightReceiverConnection _wantsContentType:]
- -[SpotlightReceiverConnection bundleIDs]
- -[SpotlightReceiverConnection contentTypes]
- -[SpotlightReceiverConnection initWithServiceName:clientID:wantsText:wantsHTML:]
- GCC_except_table1050
- GCC_except_table1052
- GCC_except_table1057
- GCC_except_table107
- GCC_except_table1098
- GCC_except_table1104
- GCC_except_table1208
- GCC_except_table1209
- GCC_except_table1277
- GCC_except_table1280
- GCC_except_table1282
- GCC_except_table1283
- GCC_except_table1445
- GCC_except_table1474
- GCC_except_table158
- GCC_except_table162
- GCC_except_table163
- GCC_except_table168
- GCC_except_table17
- GCC_except_table170
- GCC_except_table171
- GCC_except_table179
- GCC_except_table196
- GCC_except_table200
- GCC_except_table21
- GCC_except_table211
- GCC_except_table219
- GCC_except_table23
- GCC_except_table249
- GCC_except_table256
- GCC_except_table266
- GCC_except_table291
- GCC_except_table311
- GCC_except_table339
- GCC_except_table348
- GCC_except_table349
- GCC_except_table35
- GCC_except_table377
- GCC_except_table392
- GCC_except_table405
- GCC_except_table408
- GCC_except_table417
- GCC_except_table420
- GCC_except_table451
- GCC_except_table460
- GCC_except_table474
- GCC_except_table479
- GCC_except_table493
- GCC_except_table494
- GCC_except_table543
- GCC_except_table544
- GCC_except_table545
- GCC_except_table6
- GCC_except_table627
- GCC_except_table651
- GCC_except_table677
- GCC_except_table681
- GCC_except_table685
- GCC_except_table713
- GCC_except_table73
- GCC_except_table739
- GCC_except_table756
- GCC_except_table769
- GCC_except_table793
- GCC_except_table794
- GCC_except_table802
- GCC_except_table839
- GCC_except_table878
- GCC_except_table9
- GCC_except_table913
- GCC_except_table914
- GCC_except_table920
- GCC_except_table921
- GCC_except_table922
- GCC_except_table923
- GCC_except_table928
- GCC_except_table941
- GCC_except_table962
- GCC_except_table967
- GCC_except_table972
- GCC_except_table983
- GCC_except_table999
- _MDItemContactKeywords
- _MDItemPrimaryRecipients
- _MDItemUserSharedReceivedRecipient
- _MDItemUserSharedReceivedRecipientHandle
- _MDItemUserSharedSentRecipient
- _MDItemUserSharedSentRecipientHandle
- _OBJC_CLASS_$_CSThresholdedTrigger
- _OBJC_IVAR_$_CSThresholdedTrigger._actionCounts
- _OBJC_IVAR_$_CSThresholdedTrigger._countThreshold
- _OBJC_IVAR_$_CSThresholdedTrigger._lastActionDates
- _OBJC_IVAR_$_CSThresholdedTrigger._timeInterval
- _OBJC_IVAR_$_SpotlightReceiverConnection._INIntentClassNames
- _OBJC_IVAR_$_SpotlightReceiverConnection._bundleIDs
- _OBJC_IVAR_$_SpotlightReceiverConnection._contentTypes
- _OBJC_IVAR_$_SpotlightReceiverConnection._negativeSet
- _OBJC_IVAR_$_SpotlightReceiverConnection._positiveSet
- _OBJC_METACLASS_$_CSThresholdedTrigger
- __OBJC_$_CLASS_METHODS_SpotlightReceiverConnection
- __OBJC_$_CLASS_METHODS_SpotlightSender
- __OBJC_$_INSTANCE_METHODS_CSThresholdedTrigger
- __OBJC_$_INSTANCE_VARIABLES_CSThresholdedTrigger
- __OBJC_$_PROP_LIST_CSThresholdedTrigger
- __OBJC_CLASS_RO_$_CSThresholdedTrigger
- __OBJC_METACLASS_RO_$_CSThresholdedTrigger
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110__pop_heapB8ne190102INS_17_ClassicAlgPolicyE22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
- __ZNSt3__110__pop_heapB8ne190102INS_17_ClassicAlgPolicyE27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__114__split_bufferINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEERNS5_IS8_EEE17__destruct_at_endB8ne190102EPS8_
- __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEERNS_9allocatorIS8_EEE17__destruct_at_endB8ne190102EPS8_
- __ZNSt3__114priority_queueINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_6vectorIS8_NS_9allocatorIS8_EEEE22_compareTopKCandidatesE4pushEOS8_
- __ZNSt3__117__floyd_sift_downB8ne190102INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__117__floyd_sift_downB8ne190102INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE22__base_destruct_at_endB8ne190102EPS8_
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
- __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke
- ___100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke.1539
- ___100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke.cold.1
- ___100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke.cold.2
- ___100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke.cold.3
- ___100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke_2
- ___100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke_3
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1503
- ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1358
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3044
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1472
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1480
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1486
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1492
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1495
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1487
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1493
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1496
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1496.cold.1
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1488
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1488.cold.1
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1494
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2350
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2352
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2352.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2355
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2355.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2356
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2356.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2357
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1382
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1390
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1390.cold.1
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1386
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1387
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1388
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1298
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1298.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1298.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1317
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1319
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1319.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1319.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1322
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1322.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1322.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1325
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1318
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1210
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1210.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1210.cold.2
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1210.cold.3
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1210.cold.4
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1237
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1249
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1281
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1286
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1290
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1293
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1261
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1282
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1287
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1287.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1294
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1262
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_4.1263
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke.268
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke.272
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke.273
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke_2
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke_2.274
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke_3
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke_4
- ___196-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:]_block_invoke_4.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2084
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2097
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2106
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2110
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2115
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2116
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2117
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2129
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2133
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2134
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2141
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2145
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2147
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2147.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2148
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2150
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2150.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2151
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2153
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2153.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2157
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2159
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2160
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2165
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2165.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2165.cold.2
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2166
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2173
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2176
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2181
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2188
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2189
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2194
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2194.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2194.cold.2
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2093
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2102
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2137
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2142
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2161
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2161.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2174
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2177
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2177.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2191
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2191.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2198
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2094
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2094.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2175
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2175.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2199
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.2260
- ___36+[SpotlightReceiverConnection setup]_block_invoke
- ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2341
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.482
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.482.cold.1
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.483
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.491
- ___40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2308
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3055
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3056
- ___41-[SpotlightReceiverConnection startSetup]_block_invoke.76
- ___41-[SpotlightReceiverConnection startSetup]_block_invoke.76.cold.1
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2031
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2031.cold.1
- ___48-[SpotlightReceiverConnection deleteFromBundle:]_block_invoke.116
- ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1346
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2251
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2255
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2255.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2255.cold.2
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2256
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2256.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2257
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2257.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2258
- ___55-[SpotlightReceiverConnection deleteAllUserActivities:]_block_invoke.112
- ___58-[SpotlightReceiverConnection deleteFromBundle:sinceDate:]_block_invoke.115
- ___59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.498
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.217
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.218
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.222
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.223
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.231
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.231.cold.1
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.233
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2239
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2240
- ___59-[SpotlightReceiverConnection purgeFromBundle:identifiers:]_block_invoke.108
- ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1052
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.238
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.239
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.245
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.245.cold.1
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1186
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1189
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1192
- ___61-[SPConcreteCoreSpotlightIndexer issuePhotosReindexIfNeeded:]_block_invoke
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.543
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.543.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.544
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.544.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.545
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.545.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.546
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.550
- ___62-[SpotlightReceiverConnection donateRelevantActions:bundleID:]_block_invoke.124
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.516
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.516.cold.1
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.520
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.520.cold.1
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.522
- ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2235
- ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.945
- ___66-[SPConcreteCoreSpotlightIndexer fetchMeCard:isNotCreateNewIndex:]_block_invoke
- ___66-[SpotlightReceiverConnection deleteFromBundle:domainIdentifiers:]_block_invoke.107
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2041
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2042
- ___67-[SpotlightReceiverConnection deleteFromBundle:encodedIdentifiers:]_block_invoke.104
- ___71-[SpotlightReceiverConnection addUserActions:bundleID:protectionClass:]_block_invoke.111
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1046
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1047
- ___72-[SpotlightReceiverConnection deleteFromBundle:contentType:identifiers:]_block_invoke.106
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1436
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1436.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1440
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1440.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1441
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1455
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1456
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1460
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1328
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1332
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1338
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1338.cold.1
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1333
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1002
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1008
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1010
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1012
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1012.cold.1
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1017
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1018
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1021
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1024
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1032
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1038
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.963
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.968
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1009
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1011
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1016
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.964
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.970
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.973
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.976
- ___78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.508
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1085
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1086
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1093
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1093.cold.1
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2389
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2390
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2391
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2286
- ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1195
- ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2472
- ___81-[SpotlightReceiverConnection deleteAllInteractionsWithBundleID:protectionClass:]_block_invoke.122
- ___82-[SpotlightReceiverConnection indexFromBundle:protectionClass:items:itemsContent:]_block_invoke.101
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.210
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.210.cold.1
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.210.cold.2
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3043
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2992
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2992.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2994
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2996
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2996.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2997
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2998
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2998.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2999
- ___87-[SpotlightReceiverConnection addInteraction:intentClassName:bundleID:protectionClass:]_block_invoke.119
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2557
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2564
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2584
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2618
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2622
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2626
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2646
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2658
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2671
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2865
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2866
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2873
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2877
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2878
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2882
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2886
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2905
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2565
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2650
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2672
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2927
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2931
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.2962
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.2963
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.2967
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.2980
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.2985
- ___90-[SpotlightReceiverConnection deleteInteractionsWithIdentifiers:bundleID:protectionClass:]_block_invoke.120
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1056
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1057
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2418
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2419
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.562
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.563
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.564
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.565
- ___95-[SpotlightReceiverConnection deleteInteractionsWithGroupIdentifiers:bundleID:protectionClass:]_block_invoke.121
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1397
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1407
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1408
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2279
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2279.cold.1
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2280
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2284
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2285
- ___99-[SpotlightReceiverConnection deleteUserActivitiesWithPersistentIdentifiers:bundleID:retainedData:]_block_invoke.113
- ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
- ___block_descriptor_49_e8_32s40w_e18_v20?0^{__SI=}8C16lw40l8s32l8
- ___block_descriptor_64_e8_32s40s_e18_v20?0^{__SI=}8C16ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs_e22_v20?0^{__CFData=}8B16ls32l8s56l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48r_e18_v20?0^{__SI=}8C16ls32l8s40l8r48l8
- ___block_descriptor_81_e8_32s40s48s56s64bs_e18_v20?0^{__SI=}8C16ls32l8s40l8s64l8s48l8s56l8
- ___block_descriptor_90_e8_32s40s48r56r64r_e13_v24?0^8^B16lr48l8r56l8r64l8s32l8s40l8
- ___block_descriptor_98_e8_32s40s48s56s64r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40ls32l8s40l8r64l8s48l8s56l8
- ___block_literal_global.1020
- ___block_literal_global.1023
- ___block_literal_global.1026
- ___block_literal_global.1040
- ___block_literal_global.1181
- ___block_literal_global.1184
- ___block_literal_global.1188
- ___block_literal_global.1191
- ___block_literal_global.1194
- ___block_literal_global.1239
- ___block_literal_global.1251
- ___block_literal_global.1289
- ___block_literal_global.1296
- ___block_literal_global.1321
- ___block_literal_global.1324
- ___block_literal_global.1498
- ___block_literal_global.15
- ___block_literal_global.1549
- ___block_literal_global.1559
- ___block_literal_global.2011
- ___block_literal_global.2016
- ___block_literal_global.2022
- ___block_literal_global.2027
- ___block_literal_global.2044
- ___block_literal_global.2046
- ___block_literal_global.2048
- ___block_literal_global.2051
- ___block_literal_global.2068
- ___block_literal_global.2081
- ___block_literal_global.2083
- ___block_literal_global.2087
- ___block_literal_global.2112
- ___block_literal_global.212
- ___block_literal_global.2136
- ___block_literal_global.2144
- ___block_literal_global.2193
- ___block_literal_global.2263
- ___block_literal_global.2274
- ___block_literal_global.2276
- ___block_literal_global.2278
- ___block_literal_global.2288
- ___block_literal_global.2327
- ___block_literal_global.2332
- ___block_literal_global.2334
- ___block_literal_global.2343
- ___block_literal_global.237
- ___block_literal_global.2379
- ___block_literal_global.241
- ___block_literal_global.2414
- ___block_literal_global.2421
- ___block_literal_global.2505
- ___block_literal_global.27
- ___block_literal_global.2790
- ___block_literal_global.2795
- ___block_literal_global.2800
- ___block_literal_global.2805
- ___block_literal_global.2810
- ___block_literal_global.2815
- ___block_literal_global.2820
- ___block_literal_global.2825
- ___block_literal_global.2830
- ___block_literal_global.3002
- ___block_literal_global.3054
- ___block_literal_global.3067
- ___block_literal_global.31
- ___block_literal_global.3631
- ___block_literal_global.3680
- ___block_literal_global.3688
- ___block_literal_global.3690
- ___block_literal_global.3727
- ___block_literal_global.3734
- ___block_literal_global.485
- ___block_literal_global.514
- ___block_literal_global.539
- ___block_literal_global.917
- ___block_literal_global.936
- ___block_literal_global.939
- ___block_literal_global.941
- ___block_literal_global.959
- ___block_literal_global.966
- ___block_literal_global.972
- ___block_literal_global.975
- ___block_literal_global.978
- ___processItemsForImportInner_block_invoke.3648
- _createEqualORQuery
- _createNotEqualANDQuery
- _objc_msgSend$_wantsBundleID:
- _objc_msgSend$_wantsContentType:
- _objc_msgSend$disabled
- _objc_msgSend$fetchLastClientStateForBundleID:clientStateName:completionHandler:
- _objc_msgSend$fetchMeCard:isNotCreateNewIndex:
- _objc_msgSend$initWithServiceName:clientID:wantsText:wantsHTML:
- _objc_msgSend$issuePhotosReindexIfNeeded:
- _objc_msgSend$lastLoadedContentVersion
- _objc_msgSend$openIndex:forInit:readOnly:
- _objc_msgSend$reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:
- _objc_msgSend$reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:
- _objc_msgSend$setup
- _objc_msgSend$timeInterval
- _objc_msgSend$updateContainersAndScores:
- _objc_msgSend$updateDerivedFromToMeEmailAdded:
- _objc_msgSend$updateDerivedFromToMeEmailUpdated:
- _objc_msgSend$updateDerivedIsMe:
- _objc_msgSend$updateDerivedIsMe:nameTokens:alias:onlyIfNotAlready:
- _objc_msgSend$updateDerivedIsMeIfNotAlready:
- _objc_msgSend$updateDerivedIsMeNot:nameTokens:alias:
- _objc_msgSend$updateDerivedIsMeTextContentMatch:nameTokens:alias:onlyIfNotAlready:
- _objc_msgSend$updateDerivedIsMeTextContentMatchNot:nameTokens:alias:
- _objc_msgSend$updateEmailContentURLAttr:
- _objc_msgSend$updateEmailLocalParts:
- _objc_msgSend$updateGroups:
- _objc_msgSend$updateIndexRankingDates:
- _objc_msgSend$updateMeCardInfo:middleName:familyName:emailAddresses:isFirstTimeCheck:isNotCreateNewIndex:
- _objc_msgSend$updateNotes:
- _objc_msgSend$updateRankingDates:
- _sAssetsConnection
- _sCoreDuetConnection
- _sCoreSpotlightConnection
- _sImagesConnection
- _sSpotlightSenderState
- _sSuggestionsConnection
- _setup.onceToken
CStrings:
+ "### RECEIVER %@ enable"
+ "### RECEIVER client: %@, supportedJobTypes: 0x%x bundleIDs: %@, contentTypes: %@, INIntentClassNames:  %@"
+ "### RECEIVER: starting setup for client %ld"
+ "### RECEIVER: starting setup for client %ld from plist config %@ "
+ "###_sendPhotosDeleteABCReport: Failed to auto-bug capture: %ld"
+ "###_sendPhotosDeleteABCReport: Photos deletion report: %@"
+ "#index fetch state dataLen:%ld bundle:%@"
+ "%@-%@"
+ "%@/%@.plist"
+ "(%@ && %@ && %@)"
+ "(%@ && %@)"
+ "(%@ || %@ || %@)"
+ "(%@ || (%@))"
+ "(%@!=\"%@*\"%@)"
+ "(%@!=*)"
+ "(%@) changeStateOfSearchableItemsWithUIDs (delete or purge), uti:%@, state:%ld, options:0x%lx, test/duet/suggestions/textunderstanding:%@/%@/%@/%@, identifiers/%ld:%@"
+ "(%@=\"%@*\"%@)"
+ "((%@!=1) && (%@!=*))"
+ "((%@) && %@)"
+ "((%@) || %@)"
+ "((%@=1) && (%@!=*))"
+ "((%@=1) && (%@=*))"
+ "((%@>0) && (%@!=*))"
+ "(((%@!=*) || (%@=0)) && (%@!=*))"
+ "*warn* Alias Name String is nil"
+ "*warn* Email Array is nil"
+ "*warn* Full Name String is nil"
+ "*warn* Given Name Tokens Array is nil"
+ "*warn* Non Given Name Tokens Array is nil"
+ "-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke"
+ "/System/Library/PrivateFrameworks/TextUnderstandingRuntime.framework"
+ "2374.0.1"
+ "@\"NSNumber\""
+ "@\"SpotlightReceiverConfig\""
+ "@\"SpotlightSenderState\""
+ "B32@0:8q16@24"
+ "B64@0:8@16@24@32@40B48B52@56"
+ "CSDisableBackgroundHarvestingForTextUnderstanding"
+ "CSDisableLocalFileProviderDaemonClient"
+ "Call to delete SPI"
+ "ClientState empty data"
+ "Couldn't run query to determine hasPhotos and hasText"
+ "DebugVerboseModeQuery"
+ "FileIndexer"
+ "IndexerDaemon"
+ "No known client: %@"
+ "Photos index version change"
+ "PhotosDelete"
+ "Reindex all class C"
+ "Reindex bundleIDs call -- all PCs"
+ "Running queue: %s"
+ "SIFetchCSClientState nil for bundleID:%@ retCode:%d"
+ "SpotlightReceiverConfig"
+ "SpotlightReceiverConnectionManager"
+ "SpotlightScheduledSender"
+ "SpotlightScheduledSender: deleteWithFd, client: %@"
+ "SpotlightScheduledSender: deleteWithSerialNumber, client: %@"
+ "SpotlightScheduledSender: indexWithSerialNumber, client: %@, configName: %@, priority: %@"
+ "SpotlightScheduledSender: spotlightReceiver disabling messages for adds"
+ "SpotlightScheduledSender: spotlightReceiver disabling messages for deletes"
+ "SpotlightScheduledSender: spotlightReceiver disabling messages for reset"
+ "SpotlightScheduledSender: spotlightReceiver disabling messages for resume"
+ "SpotlightScheduledSender: spotlightReceiver disabling messages for suspend"
+ "SpotlightScheduledSender: spotlightReceiver failed to create FD! fd: %d"
+ "SpotlightScheduledSender: spotlightReceiver status: %lld"
+ "SpotlightSender: Enabled client state changed from 0x%x to 0x%x"
+ "SpotlightSender: Removing cache file  %@"
+ "SpotlightSender: addInteraction, interaction: %p(%@), bundleID: %@, protectionClass: %@, client: %@"
+ "SpotlightSender: addUserActions, count: %d bundleID: %@, protectionClass: %@, client: %@"
+ "SpotlightSender: deleteAllInteractionsWithBundleID, bundleID: %@, protectionClass: %@, client: %@"
+ "SpotlightSender: deleteAllUserActivities bundleID: %@, client: %@"
+ "SpotlightSender: deleteDomainIdentifiersFromBundle, count: %d bundleID: %@, client: %@"
+ "SpotlightSender: deleteEncodedIdentifiersFromBundle, bundleID: %@, client: %@"
+ "SpotlightSender: deleteFromBundle, bundleID: %@, client: %@"
+ "SpotlightSender: deleteFromBundle, sinceDate: %@, bundleID: %@, client: %@"
+ "SpotlightSender: deleteIdentifiersFromBundle, count: %d bundleID: %@, contentType: %@ client: %@"
+ "SpotlightSender: deleteInteractionsWithGroupIdentifiers, bundleID: %@, protectionClass: %@, client: %@, identifiers number: %lu"
+ "SpotlightSender: deleteInteractionsWithIdentifiers, bundleID: %@, protectionClass: %@, client: %@, identifiers number: %lu"
+ "SpotlightSender: deleteUserActivities bundleID: %@, client: %@"
+ "SpotlightSender: donateRelevantActions data: %p, bundleID: %@ client: %@"
+ "SpotlightSender: identifiers: %@"
+ "SpotlightSender: purgeFromBundle, count: %d bundleID: %@, client: %@"
+ "T@\"NSArray\",C,N,V_bundleIDs"
+ "T@\"NSArray\",C,N,V_connectionIdentifiers"
+ "T@\"NSArray\",C,N,V_contentTypes"
+ "T@\"NSArray\",C,N,V_disableBundleIDs"
+ "T@\"NSArray\",C,N,V_disableContentTypes"
+ "T@\"NSArray\",C,N,V_disableDomainIDs"
+ "T@\"NSArray\",C,N,V_domainIDs"
+ "T@\"NSArray\",C,N,V_donationAttributes"
+ "T@\"NSArray\",C,N,V_excludeAttributes"
+ "T@\"NSArray\",C,N,V_optionalAttributes"
+ "T@\"NSArray\",C,N,V_processes"
+ "T@\"NSArray\",C,N,V_requiredAttributes"
+ "T@\"NSArray\",C,N,V_trackingAttributes"
+ "T@\"NSArray\",R,N"
+ "T@\"NSNumber\",C,N,V_versionValue"
+ "T@\"NSSet\",C,N,V_INIntentClassNames"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"NSString\",C,N,V_priority"
+ "T@\"NSString\",C,N,V_supportedQuery"
+ "T@\"NSString\",C,N,V_unsupportedQuery"
+ "T@\"NSString\",C,N,V_versionName"
+ "T@\"SpotlightReceiverConfig\",C,N,V_primaryConfig"
+ "TB,N,V_includeDeletedItems"
+ "TB,N,V_includeLanguage"
+ "TB,N,V_includeUpdatedItems"
+ "TB,N,V_needsHTML"
+ "TB,N,V_needsText"
+ "TB,N,V_requireBacklogItems"
+ "TB,N,V_requirePriorityItems"
+ "Tq,R,N,V_client"
+ "[qid=%ld][%@][rewrite] indexDependentTokenRewritesWithQueryString found %lu rewrites"
+ "[qid=%ld][%@][rewrite] number of topK terms that are inflated in memory from plist: bundleCount=%lu, termCount=%lu"
+ "[qid=%ld][%@][rewrite] rewriteQueryWithQueryString=%@"
+ "[qid=%ld][rewrite] Found %lu rewrite candidate"
+ "[qid=%ld][rewrite] Requesting rewrite candidates"
+ "[qid=%ld][rewrite] Rewrite finished hasResults:%@"
+ "[qid=%ld][rewrite] Rewrite gather ended hasResults:%@"
+ "[qid=%ld][rewrite] rewriteAllowed:%@ topHit:%@ live:%@"
+ "[qid=%ld][rewrite] rewriteQueryWithQueryString=%@ top_hit=%@"
+ "_ICItemDisplayName"
+ "_client"
+ "_configs"
+ "_connectionIdentifiers"
+ "_connections"
+ "_disableBundleIDs"
+ "_disableContentTypes"
+ "_disableDomainIDs"
+ "_dispatchToReceivers, bundleID:%@, options:0x%lx, test/duet/suggestions/textunderstanding:%@/%@/%@/%@"
+ "_dispatchToReceivers, deleteSearchableItemsWithEncodedIdentifiers, bundleID:%@, options:0x%lx, test/duet/suggestions/textunderstanding:%@/%@/%@/%@"
+ "_domainIDs"
+ "_donationAttributes"
+ "_excludeAttributes"
+ "_includeDeletedItems"
+ "_includeLanguage"
+ "_includeUpdatedItems"
+ "_kMDItem%@Version"
+ "_name"
+ "_needsHTML"
+ "_needsText"
+ "_optionalAttributes"
+ "_primaryConfig"
+ "_priority"
+ "_processes"
+ "_requireBacklogItems"
+ "_requirePriorityItems"
+ "_requiredAttributes"
+ "_state"
+ "_supportedQuery"
+ "_trackingAttributes"
+ "_unsupportedQuery"
+ "_versionName"
+ "_versionValue"
+ "aatrs"
+ "addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:"
+ "asyncOpenIndex:forInit:readOnly:"
+ "bootstrapping new index %@"
+ "capitalizedString"
+ "client"
+ "clientState && retCode == Success"
+ "cnm"
+ "com.apple.corespotlight.daemon.fileindexer"
+ "com.apple.corespotlight.receiver.textunderstandingd"
+ "com.apple.corespotlight.scheduled.receiver.textunderstandingd"
+ "com.apple.textunderstanding"
+ "configs"
+ "connectionIdentifiers"
+ "copyNSStringOrDictArrayFromXPCArray:"
+ "deleteSearchableItemsInJournalFd:atOffset:size:indexType:protectionClass:serialNumber:journalCookie:client:completionHandler:"
+ "deleteWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:completionHandler:"
+ "dictionary:setStringOrDictionaryArray:forKey:"
+ "disableBundleIDs"
+ "disableContentTypes"
+ "disableDomainIDs"
+ "domainIDs"
+ "donationAttributes"
+ "excludeAttributes"
+ "f-off"
+ "f-size"
+ "fetchLastClientStateForBundleID:clientStateName:options:completionHandler:"
+ "fetchMeCard:isNotCreateNewIndex:group:"
+ "fixup name: %@ version check failed, data class: %@, current version: %ld, target version: %lu, force: %d"
+ "fixup name: %@ version check passed, data class: %@, current version: %ld, target version: %lu, force: %d"
+ "fixup name: %@,  data class: %@, bundle ID: %@, dictionaries count: %d"
+ "fixup name: %@, data class: %@, bundle ID: %@, dictionaries count: %d"
+ "fixup runAllOtherFixups finished running"
+ "fixup runAllOtherFixups state: %ld"
+ "fixup updateDerivedIsMe force %d finished running"
+ "fixup updateDerivedIsMe state: %ld"
+ "fixup updateDerivedIsMeIfNotAlready force %d finished running"
+ "fixup updateDerivedIsMeIfNotAlready running force %d state %ld "
+ "includeDeletedItems"
+ "includeLanguage"
+ "includeUpdatedItems"
+ "index dropped %@"
+ "indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:"
+ "initForClient:"
+ "initWithConnectionInfo:configurationInfo:"
+ "initWithServiceName:client:configPath:"
+ "isTimeSensitive"
+ "issuePhotosReindexIfNeeded:group:"
+ "itype"
+ "j-cook"
+ "jobForTextUnderstanding:"
+ "jps"
+ "kMDItemHTMLContentData"
+ "kMDItemTextContent"
+ "kSPDerivedIsFromMe"
+ "kSPDerivedIsFromMeNot"
+ "kSPDerivedIsFromMeRanking"
+ "kSPDerivedIsFromMeRankingNot"
+ "kSPDerivedIsMeRanking"
+ "kSPDerivedIsMeRankingNot"
+ "kSPDerivedIsMeRankingOCR"
+ "kSPDerivedIsMeRankingOCRNot"
+ "kSPDerivedIsMeRankingOCRTextContentMatch"
+ "kSPDerivedIsMeRankingOCRTextContentMatchNot"
+ "kSPDerivedIsMeRankingPreExtraction"
+ "kSPDerivedIsMeRankingPreExtractionNot"
+ "kSPDerivedIsMeRankingSpan"
+ "kSPDerivedIsMeRankingSpanNot"
+ "kSPDerivedIsMeRankingTextContentMatch"
+ "kSPDerivedIsMeRankingTextContentMatchNot"
+ "kSPDerivedIsMeRankingTextContentMatchNot2"
+ "kSPDerivedIsMeRankingToken"
+ "kSPDerivedIsMeRankingTokenNot"
+ "kSPHasPhotos"
+ "kSPHasText"
+ "lastLoadedBundleVersion"
+ "name"
+ "needsHTML"
+ "needsText"
+ "optionalAttributes"
+ "primaryConfig"
+ "processes"
+ "q32@0:8q16@24"
+ "q84@0:8B16@20q28@36@44@52@60@68@76"
+ "reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:"
+ "reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:group:forceMerge:"
+ "reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:"
+ "requireBacklogItems"
+ "requirePriorityItems"
+ "requiredAttributes"
+ "requiresHTML"
+ "requiresText"
+ "retCode != Success"
+ "runOneFixup:group:"
+ "runOtherFixups:state:"
+ "s-num"
+ "setConnectionIdentifiers:"
+ "setContentTypes:"
+ "setDisableBundleIDs:"
+ "setDisableContentTypes:"
+ "setDisableDomainIDs:"
+ "setDomainIDs:"
+ "setDonationAttributes:"
+ "setExcludeAttributes:"
+ "setHasPhotosOrText"
+ "setINIntentClassNames:"
+ "setIncludeDeletedItems:"
+ "setIncludeLanguage:"
+ "setIncludeUpdatedItems:"
+ "setIsTimeSensitive:"
+ "setName:"
+ "setNeedsHTML:"
+ "setNeedsText:"
+ "setOptionalAttributes:"
+ "setPrimaryConfig:"
+ "setProcesses:"
+ "setRequireBacklogItems:"
+ "setRequirePriorityItems:"
+ "setRequiredAttributes:"
+ "setSupportedQuery:"
+ "setTrackingAttributes:"
+ "setUnsupportedQuery:"
+ "setVersionName:"
+ "setVersionValue:"
+ "setupInstantSender"
+ "setupScheduledSender"
+ "sharedInstantManager"
+ "sharedScheduledManager"
+ "startSetupForClient:configurationValues:"
+ "supportedBundles"
+ "supportedConfigs"
+ "supportedContentTypes"
+ "supportedDomains"
+ "supportedQuery"
+ "suspended"
+ "trackingAttributes"
+ "unsupportedBundles"
+ "unsupportedContentTypes"
+ "unsupportedDomains"
+ "unsupportedQuery"
+ "updateConfigsForClient:configurationValues:"
+ "updateContainersAndScores:group:forceMerge:"
+ "updateDerivedIsFromMe:fullName:emails:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsFromMeNot:fullName:emails:group:forceMerge:"
+ "updateDerivedIsFromMeRanking:nameTokens:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsFromMeRankingNot:nameTokens:group:forceMerge:"
+ "updateDerivedIsMe:group:order:aliasName:fullName:nameTokens:givenNameTokens:nonGivenNameTokens:emails:"
+ "updateDerivedIsMe:nameTokens:alias:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMe:runOtherFixups:force:group:state:"
+ "updateDerivedIsMeIfNotAlready:group:order:aliasName:fullName:nameTokens:givenNameTokens:nonGivenNameTokens:emails:"
+ "updateDerivedIsMeIfNotAlready:group:state:"
+ "updateDerivedIsMeNot:nameTokens:alias:group:forceMerge:"
+ "updateDerivedIsMeRanking:nameTokens:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMeRankingNot:nameTokens:group:forceMerge:"
+ "updateDerivedIsMeRankingOCR:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMeRankingOCRNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:"
+ "updateDerivedIsMeRankingOCRTextContentMatch:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMeRankingOCRTextContentMatchNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:"
+ "updateDerivedIsMeRankingPreExtraction:givenNameTokens:nonGivenNameTokens:alias:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMeRankingPreExtractionNot:givenNameTokens:nonGivenNameTokens:alias:group:forceMerge:"
+ "updateDerivedIsMeRankingSpan:fullName:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMeRankingSpanNot:fullName:group:forceMerge:"
+ "updateDerivedIsMeRankingTextContentMatch:nameTokens:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMeRankingTextContentMatchNot2:nameTokens:group:forceMerge:"
+ "updateDerivedIsMeRankingTextContentMatchNot:nameTokens:group:forceMerge:"
+ "updateDerivedIsMeRankingToken:nameTokens:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMeRankingTokenNot:nameTokens:group:forceMerge:"
+ "updateDerivedIsMeTextContentMatch:nameTokens:alias:onlyIfNotAlready:group:forceMerge:"
+ "updateDerivedIsMeTextContentMatchNot:nameTokens:alias:group:forceMerge:"
+ "updateEmailContentURLAttr:group:forceMerge:"
+ "updateEmailLocalParts:group:forceMerge:"
+ "updateGroups:group:forceMerge:"
+ "updateIndexRankingDates:group:forceMerge:"
+ "updateMeCardInfo:middleName:familyName:emailAddresses:isFirstTimeCheck:isNotCreateNewIndex:group:"
+ "updateNotes:group:forceMerge:"
+ "updateRankingDates:group:forceMerge:"
+ "v100@0:8i16Q20Q28Q36@44Q52@60@68q76@84@?92"
+ "v20@?0^{__CFData=}8i16"
+ "v28@0:8B16@20"
+ "v28@0:8B16B20B24"
+ "v32@0:8B16@20B28"
+ "v32@0:8B16B20@24"
+ "v36@0:8B16@20q28"
+ "v44@0:8B16@20B28@32B40"
+ "v44@0:8B16B20B24@28q36"
+ "v48@0:8B16@20@28@36B44"
+ "v52@0:8B16@20@28B36@40B48"
+ "v56@0:8B16@20@28@36@44B52"
+ "v60@0:8B16@20@28@36B44@48B56"
+ "v76@0:8i16Q20Q28Q36@44Q52@60@?68"
+ "v80@0:8@16@24@32Q40@48B56@60@68B76"
+ "v84@0:8i16Q20Q28Q36@44Q52@60q68@?76"
+ "v88@0:8@16@24@32Q40@48B56B60B64@68@76B84"
+ "v92@0:8@16@24@32Q40@48@56B64B68@72@80B88"
+ "v92@0:8i16Q20Q28Q36@44Q52@60@68@76@?84"
+ "versionName"
+ "versionValue"
+ "wantsBundleID:"
+ "wantsContentType:"
+ "wantsDomainID:"
+ "wantsINIntentClassNames:"
- "\""
- "### RECEIVER %@ setup from cache %@"
- "#index fetch state dataLen:%ld"
- "(%@) changeStateOfSearchableItemsWithUIDs (delete or purge), uti:%@, state:%ld, options:0x%lx, test/duet/suggestions/:%@/%@/%@, identifiers/%ld:%@"
- "((%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\") || (%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\") || (%@ = \"*\" ||%@ = \"*\" ||%@ = \"*\"))"
- "-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke"
- "2333.50.1"
- "@32@0:8q16d24"
- "@40@0:8@16q24B32B36"
- "CSThresholdedTrigger"
- "Enabled client state changed from 0x%x to 0x%x"
- "Removing cache file  %@"
- "SIFetchCSClientState canceled for bundleID:%@"
- "T@\"NSArray\",R,N,V_contentTypes"
- "T@\"NSMutableDictionary\",&,N,V_actionCounts"
- "T@\"NSMutableDictionary\",&,N,V_lastActionDates"
- "T@\"NSSet\",R,N,V_INIntentClassNames"
- "T@\"NSSet\",R,N,V_bundleIDs"
- "Td,N,V_timeInterval"
- "Tq,N,V_countThreshold"
- "[rewrite] qid=%ld Found %lu rewrite candidate"
- "[rewrite] qid=%ld Requesting rewrite candidates"
- "[rewrite] qid=%ld Rewrite finished hasResults:%@"
- "[rewrite] qid=%ld Rewrite gather ended hasResults:%@"
- "[rewrite] qid=%ld rewriteAllowed:%@ topHit:%@ live:%@"
- "[rewrite] qid=%ld rewriteQueryWithQueryString=%@ top_hit=%@"
- "[rewrite][%@] qid=%ld indexDependentTokenRewritesWithQueryString found %lu rewrites"
- "[rewrite][%@] qid=%ld number of topK terms that are inflated in memory from plist: bundleCount=%lu, termCount=%lu"
- "[rewrite][%@] qid=%ld rewriteQueryWithQueryString=%@"
- "_actionCounts"
- "_countThreshold"
- "_dispatchToReceivers, bundleID:%@, options:0x%lx, test/duet/suggestions:%@/%@/%@"
- "_dispatchToReceivers, deleteSearchableItemsWithEncodedIdentifiers, bundleID:%@, options:0x%lx, test/duet/suggestions:%@/%@/%@"
- "_lastActionDates"
- "_timeInterval"
- "_wantsBundleID:"
- "_wantsContentType:"
- "actionCounts"
- "addInteraction, interaction: %p(%@), bundleID: %@, protectionClass: %@, client: %@"
- "addUserActions, count: %d bundleID: %@, protectionClass: %@, client: %@"
- "bootstrapping new index"
- "client: %@, supportedJobTypes: 0x%x bundleIDs: %@, contentTypes: %@, INIntentClassNames:  %@"
- "countThreshold"
- "deleteAllInteractionsWithBundleID, bundleID: %@, protectionClass: %@, client: %@"
- "deleteAllUserActivities bundleID: %@, client: %@"
- "deleteDomainIdentifiersFromBundle, count: %d bundleID: %@, client: %@"
- "deleteEncodedIdentifiersFromBundle, bundleID: %@, client: %@"
- "deleteFromBundle, bundleID: %@, client: %@"
- "deleteFromBundle, sinceDate: %@, bundleID: %@, client: %@"
- "deleteIdentifiersFromBundle, count: %d bundleID: %@, contentType: %@ client: %@"
- "deleteInteractionsWithGroupIdentifiers, bundleID: %@, protectionClass: %@, client: %@, identifiers number: %lu"
- "deleteInteractionsWithIdentifiers, bundleID: %@, protectionClass: %@, client: %@, identifiers number: %lu"
- "deleteUserActivities bundleID: %@, client: %@"
- "donateRelevantActions data: %p, bundleID: %@ client: %@"
- "fetchLastClientStateForBundleID:clientStateName:completionHandler:"
- "fetchMeCard:isNotCreateNewIndex:"
- "fixup to start name: %@, current version: %ld, target version: %lu"
- "identifiers: %@"
- "incrementAndCheckPerformActionForKey:"
- "index dropped"
- "initWithCountThreshold:timeInterval:"
- "initWithServiceName:clientID:wantsText:wantsHTML:"
- "issuePhotosReindexIfNeeded:"
- "kSPDerivedIsFromToMe"
- "lastActionDates"
- "lastLoadedContentVersion"
- "purgeFromBundle, count: %d bundleID: %@, client: %@"
- "reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:completionValue:alwaysReindexWithCompletionAttribute:force:postFilter:"
- "reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:"
- "setActionCounts:"
- "setCountThreshold:"
- "setLastActionDates:"
- "setTimeInterval:"
- "setup"
- "timeInterval"
- "updateContainersAndScores:"
- "updateDerivedFromToIsMeNameAdded:"
- "updateDerivedFromToIsMeNameUpdated:"
- "updateDerivedFromToMeEmailAdded:"
- "updateDerivedFromToMeEmailUpdated:"
- "updateDerivedIsFromToMe:"
- "updateDerivedIsMe:"
- "updateDerivedIsMe:nameTokens:alias:onlyIfNotAlready:"
- "updateDerivedIsMeIfNotAlready:"
- "updateDerivedIsMeNot:nameTokens:alias:"
- "updateDerivedIsMeTextContentMatch:nameTokens:alias:onlyIfNotAlready:"
- "updateDerivedIsMeTextContentMatchNot:nameTokens:alias:"
- "updateEmailContentURLAttr:"
- "updateEmailLocalParts:"
- "updateGroups:"
- "updateIndexRankingDates:"
- "updateMeCardInfo:middleName:familyName:emailAddresses:isFirstTimeCheck:isNotCreateNewIndex:"
- "updateNotes:"
- "updateRankingDates:"
- "v20@?0^{__CFData=}8B16"
- "v36@0:8B16@20@28"
- "v56@0:8@16@24@32@40B48B52"
- "v68@0:8@16@24@32Q40@48B56@60"
- "v76@0:8@16@24@32Q40@48B56B60B64@68"

```
