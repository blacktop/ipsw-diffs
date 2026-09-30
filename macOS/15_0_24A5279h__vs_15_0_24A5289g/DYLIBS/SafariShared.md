## SafariShared

> `/System/iOSSupport/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared`

```diff

-619.1.18.11.1
-  __TEXT.__text: 0x153f94
-  __TEXT.__auth_stubs: 0x1a10
-  __TEXT.__objc_methlist: 0xe87c
-  __TEXT.__const: 0x5a558
-  __TEXT.__gcc_except_tab: 0x1c67c
-  __TEXT.__cstring: 0x172dc
-  __TEXT.__ustring: 0xc642
-  __TEXT.__oslogstring: 0xd669
+619.1.20.11.1
+  __TEXT.__text: 0x153c6c
+  __TEXT.__auth_stubs: 0x1b00
+  __TEXT.__objc_methlist: 0xe8d4
+  __TEXT.__const: 0x5a5e8
+  __TEXT.__gcc_except_tab: 0x1c5dc
+  __TEXT.__cstring: 0x16e76
+  __TEXT.__ustring: 0xc1c8
+  __TEXT.__oslogstring: 0xda06
   __TEXT.__dlopen_cstrs: 0xe9
-  __TEXT.__unwind_info: 0x9d18
-  __TEXT.__objc_classname: 0x2933
-  __TEXT.__objc_methname: 0x2c235
-  __TEXT.__objc_methtype: 0xb40e
-  __TEXT.__objc_stubs: 0x185e0
-  __DATA_CONST.__got: 0xf70
-  __DATA_CONST.__const: 0x12ee0
-  __DATA_CONST.__objc_classlist: 0x958
+  __TEXT.__unwind_info: 0x9cd8
+  __TEXT.__objc_classname: 0x2965
+  __TEXT.__objc_methname: 0x2c3cc
+  __TEXT.__objc_methtype: 0xb443
+  __TEXT.__objc_stubs: 0x18700
+  __DATA_CONST.__got: 0xf90
+  __DATA_CONST.__const: 0x12f30
+  __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x85e0
+  __DATA_CONST.__objc_selrefs: 0x8640
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x7c0
-  __DATA_CONST.__objc_arraydata: 0xb38
-  __AUTH_CONST.__auth_got: 0xd20
+  __DATA_CONST.__objc_superrefs: 0x7c8
+  __DATA_CONST.__objc_arraydata: 0x728
+  __AUTH_CONST.__auth_got: 0xd98
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x24b8
-  __AUTH_CONST.__cfstring: 0x154e0
-  __AUTH_CONST.__objc_const: 0x1e8d8
-  __AUTH_CONST.__objc_arrayobj: 0x300
+  __AUTH_CONST.__const: 0x24d8
+  __AUTH_CONST.__cfstring: 0x14380
+  __AUTH_CONST.__objc_const: 0x1e9c0
+  __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x42e0
-  __DATA.__objc_ivar: 0x123c
+  __AUTH.__objc_data: 0x4330
+  __DATA.__objc_ivar: 0x1244
   __DATA.__data: 0x2c80
-  __DATA.__bss: 0xa90
+  __DATA.__bss: 0xa70
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__data: 0x10

   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7948
-  Symbols:   19842
-  CStrings:  3049
+  Functions: 7939
+  Symbols:   19868
+  CStrings:  2949
 
Symbols:
+ -[WBSFormMetadataController textFieldFocused:inFrame:textFieldMetadata:formMetadata:].cold.1
+ -[WBSFrequentlyVisitedSitesController _frequentlyVisitedSitesDidLoadHistory]
+ -[WBSPerSitePreferencesSQLiteStore removeAllPreferenceValues:]
+ -[WBSSpotlightReindexingBackgroundSystemTaskManager .cxx_destruct]
+ -[WBSSpotlightReindexingBackgroundSystemTaskManager init]
+ -[WBSSpotlightReindexingBackgroundSystemTaskManager registerAndSubmitRequestForTask:]
+ -[WBSSpotlightReindexingBackgroundSystemTaskManager registerAndSubmitRequestForTask:].cold.1
+ -[WBSStartPageSectionManager suggestionsDataSourceSections]
+ OBJC_IVAR_$_WBSSiriIntelligenceDonor._reindexingBackgroundSystemTaskManager
+ OBJC_IVAR_$_WBSSpotlightReindexingBackgroundSystemTaskManager._internalQueue
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_WBSSpotlightReindexingBackgroundSystemTaskManager
+ _OBJC_METACLASS_$_WBSSpotlightReindexingBackgroundSystemTaskManager
+ _WBSPrivacyReportStartPageDataPreferenceKey
+ _WBSSafariBookmarksSyncAgentCloudTabsConsentWasUpdatedNotificationName
+ __112-[WBSSiriIntelligenceDonor _indexCoreSpotlightData:filterDeletedHistoryItems:onDispatchQueue:completionHandler:]_block_invoke.169
+ __114-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:withAcknowledgementHandler:]_block_invoke.156
+ __114-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:withAcknowledgementHandler:]_block_invoke.156.cold.1
+ __114-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:withAcknowledgementHandler:]_block_invoke.157
+ __114-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:withAcknowledgementHandler:]_block_invoke.157.cold.1
+ __53-[WBSPerSitePreferencesSQLiteStore removeAllSyncData]_block_invoke.125
+ __53-[WBSPerSitePreferencesSQLiteStore removeAllSyncData]_block_invoke.125.cold.1
+ __62-[WBSPerSitePreferencesSQLiteStore removeAllPreferenceValues:]_block_invoke.cold.1
+ __85-[WBSSpotlightReindexingBackgroundSystemTaskManager registerAndSubmitRequestForTask:]_block_invoke.cold.1
+ __87-[WBSSiriIntelligenceDonor donateSafariBookmarksToCoreSpotlight:withCompletionHandler:]_block_invoke.137
+ __87-[WBSSiriIntelligenceDonor donateSafariBookmarksToCoreSpotlight:withCompletionHandler:]_block_invoke.145
+ __89-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:withAcknowledgementHandler:]_block_invoke.151
+ __89-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:withAcknowledgementHandler:]_block_invoke.151.cold.1
+ __89-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:withAcknowledgementHandler:]_block_invoke.153
+ __89-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:withAcknowledgementHandler:]_block_invoke_2.cold.1
+ __OBJC_$_INSTANCE_METHODS_WBSSpotlightReindexingBackgroundSystemTaskManager
+ __OBJC_$_INSTANCE_VARIABLES_WBSSpotlightReindexingBackgroundSystemTaskManager
+ __OBJC_CLASS_RO_$_WBSSpotlightReindexingBackgroundSystemTaskManager
+ __OBJC_METACLASS_RO_$_WBSSpotlightReindexingBackgroundSystemTaskManager
+ ___59-[WBSStartPageSectionManager suggestionsDataSourceSections]_block_invoke
+ ___62-[WBSPerSitePreferencesSQLiteStore removeAllPreferenceValues:]_block_invoke
+ ___85-[WBSSpotlightReindexingBackgroundSystemTaskManager registerAndSubmitRequestForTask:]_block_invoke
+ ___85-[WBSSpotlightReindexingBackgroundSystemTaskManager registerAndSubmitRequestForTask:]_block_invoke_2
+ ___89-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:withAcknowledgementHandler:]_block_invoke_2
+ ___block_descriptor_32_e70_"WBSStartPageSectionDescriptor"16?0"WBSStartPageSectionDescriptor"8l
+ ___block_descriptor_40_e8_32bs_e34_v16?0"BGNonRepeatingSystemTask"8ls32l8
+ __block_literal_global.127
+ __block_literal_global.140
+ __block_literal_global.155
+ __block_literal_global.171
+ __block_literal_global.267
+ __block_literal_global.71
+ _objc_msgSend$registerAndSubmitRequestForTask:
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$setExpirationHandler:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setRequiresExternalPower:
+ _objc_msgSend$setResourceIntensive:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTaskExpiredWithRetryAfter:error:
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$taskRequestForIdentifier:
- _WBSDisplayTextForCreditCardNumber
- _WBSLastDigitsOfCreditCardNumber
- __112-[WBSSiriIntelligenceDonor _indexCoreSpotlightData:filterDeletedHistoryItems:onDispatchQueue:completionHandler:]_block_invoke.165
- __114-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:withAcknowledgementHandler:]_block_invoke.152
- __114-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:withAcknowledgementHandler:]_block_invoke.152.cold.1
- __114-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:withAcknowledgementHandler:]_block_invoke.153
- __114-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:withAcknowledgementHandler:]_block_invoke.153.cold.1
- __53-[WBSPerSitePreferencesSQLiteStore removeAllSyncData]_block_invoke.122
- __53-[WBSPerSitePreferencesSQLiteStore removeAllSyncData]_block_invoke.122.cold.1
- __87-[WBSSiriIntelligenceDonor donateSafariBookmarksToCoreSpotlight:withCompletionHandler:]_block_invoke.136
- __87-[WBSSiriIntelligenceDonor donateSafariBookmarksToCoreSpotlight:withCompletionHandler:]_block_invoke.144
- __89-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:withAcknowledgementHandler:]_block_invoke.150
- __89-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:withAcknowledgementHandler:]_block_invoke.150.cold.1
- __ZGVZ45WBSAllowedCreditCardNumberSeparatorCharactersE10separators
- __ZL13isMaestroCardmlb
- __ZL16creditCardLabels22CreditCardStringNumber
- __ZL22gregorianDateFromPartslll
- __ZL9isJCBCardmlb
- __ZZ36WBSLocaleForCreditCardExpirationDateE33localeForCreditCardExpirationDate
- __ZZ36WBSLocaleForCreditCardExpirationDateE4once
- __ZZ45WBSAllowedCreditCardNumberSeparatorCharactersE10separators
- ___WBSLocaleForCreditCardExpirationDate_block_invoke
- __block_literal_global.136
- __block_literal_global.163
- __block_literal_global.261
- _objc_msgSend$setMonth:
- _objc_msgSend$setYear:
CStrings:
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/SafariShared_iosmac/SafariShared/FrequentlyVisitedSites/WBSFrequentlyVisitedSitesController.mm"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/SafariShared_iosmac/SafariShared/History/Service/WBSHistoryServiceURLCompletion.mm"
+ "@\"WBSStartPageSectionDescriptor\"16@?0@\"WBSStartPageSectionDescriptor\"8"
+ "DELETE FROM preference_values"
+ "PrivacyReportStartPageData"
+ "com.apple.SafariBookmarksSyncAgent.CloudTabsConsentWasUpdated"
+ "com.apple.SafariShared.%!@(MISSING).%!p(MISSING)"
+ "com.apple.SafariShared.SpotlightReindexing"
+ "v16@?0@\"BGNonRepeatingSystemTask\"8"
- " -"
- "%!l(MISSING)d"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/SafariShared_iosmac/SafariShared/FrequentlyVisitedSites/WBSFrequentlyVisitedSitesController.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/SafariShared_iosmac/SafariShared/History/Service/WBSHistoryServiceURLCompletion.mm"
- "AMEX"
- "American Express"
- "American Express (credit card type for filling)"
- "Carte Blanche"
- "CarteBlanche"
- "China UnionPay"
- "China UnionPay card"
- "ChinaUnionPay"
- "Diner's Club"
- "Diner's Club International"
- "Diners Club"
- "Diners Club International"
- "Discover"
- "Discover Card"
- "Discover card"
- "En Route"
- "EnRoute"
- "InstaPayment"
- "InstaPayment card"
- "JCB"
- "JCB card"
- "Maestro"
- "Maestro card"
- "Master Card"
- "MasterCard"
- "Mastercard"
- "Mastercard (credit card type for filling)"
- "Switch"
- "Visa"
- "Visa (credit card name)"
- "Visa (credit card type for filling)"
- "caduca"
- "caducidad"
- "card #"
- "card holder"
- "card number"
- "card type"
- "card verification"
- "card#"
- "cardholder"
- "cardnum"
- "cardnumber"
- "cardtype"
- "cc num"
- "cc type"
- "ccnum"
- "ccnumber"
- "cctype"
- "ccv2"
- "cid"
- "codice di sicurezza"
- "credit card no"
- "credit card number"
- "creditcardno"
- "creditcardnumber"
- "cvc"
- "cvc2"
- "cvn"
- "cvv"
- "cvv2"
- "cvvx"
- "data de validade"
- "date d'expiration"
- "en_US"
- "expdate"
- "expira"
- "expiration"
- "expiration date"
- "expirationdate"
- "expire"
- "expires"
- "expiry"
- "gift card"
- "gift code"
- "giftcard"
- "giftcode"
- "health card"
- "kartenmarke"
- "kartennummer"
- "kreditkartennummer"
- "library card"
- "loyalty card"
- "loyaltycard"
- "name des karteninhabers"
- "name on card"
- "name on credit card"
- "nameoncard"
- "newcreditcardnumber"
- "nom du titulaire de la carte"
- "nombre en la tarjeta"
- "nome sulla carta"
- "numero carta di credito"
- "numero della carta di credito"
- "pan"
- "payment type"
- "rewards card"
- "rewardscard"
- "scadenza"
- "security code"
- "sicherheitscode"
- "titolare carta"
- "titolare della carta"
- "titolare della carta di credito"
- "titular de la tarjeta"
- "user profile"

```
