## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore`

```diff

-619.1.18.11.1
-  __TEXT.__text: 0xd28bc
+619.1.20.11.1
+  __TEXT.__text: 0xd4058
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0x8f8c
+  __TEXT.__objc_methlist: 0x8fa4
   __TEXT.__const: 0x61a
-  __TEXT.__gcc_except_tab: 0x5d6c
-  __TEXT.__cstring: 0xf545
-  __TEXT.__ustring: 0x24fc
-  __TEXT.__oslogstring: 0x8b9b
+  __TEXT.__gcc_except_tab: 0x5f04
+  __TEXT.__cstring: 0xfa25
+  __TEXT.__ustring: 0x2976
+  __TEXT.__oslogstring: 0x8c7b
   __TEXT.__dlopen_cstrs: 0xf3
   __TEXT.__swift5_typeref: 0x28d
   __TEXT.__swift5_capture: 0xe0

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x4578
+  __TEXT.__unwind_info: 0x4630
   __TEXT.__eh_frame: 0x2a8
-  __TEXT.__objc_classname: 0x1521
-  __TEXT.__objc_methname: 0x1f1b2
-  __TEXT.__objc_methtype: 0x32b5
-  __TEXT.__objc_stubs: 0xf8c0
-  __DATA_CONST.__got: 0xa70
-  __DATA_CONST.__const: 0x1bf0
+  __TEXT.__objc_classname: 0x1546
+  __TEXT.__objc_methname: 0x1f219
+  __TEXT.__objc_methtype: 0x32ca
+  __TEXT.__objc_stubs: 0xf9a0
+  __DATA_CONST.__got: 0xa80
+  __DATA_CONST.__const: 0x1c08
   __DATA_CONST.__objc_classlist: 0x4a8
-  __DATA_CONST.__objc_catlist: 0x148
+  __DATA_CONST.__objc_catlist: 0x150
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d18
+  __DATA_CONST.__objc_selrefs: 0x5d48
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x3c0
-  __DATA_CONST.__objc_arraydata: 0x2668
+  __DATA_CONST.__objc_arraydata: 0x2a78
   __AUTH_CONST.__auth_got: 0xe88
   __AUTH_CONST.__auth_ptr: 0xf8
-  __AUTH_CONST.__const: 0x5050
-  __AUTH_CONST.__cfstring: 0x168c0
-  __AUTH_CONST.__objc_const: 0xfe30
+  __AUTH_CONST.__const: 0x50d0
+  __AUTH_CONST.__cfstring: 0x17ac0
+  __AUTH_CONST.__objc_const: 0xfe40
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x498
+  __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH.__objc_data: 0x1ee0
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x914
   __DATA.__data: 0xcf0
-  __DATA.__bss: 0xa80
+  __DATA.__bss: 0xab0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xff0
   __DATA_DIRTY.__bss: 0x118

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4758
-  Symbols:   10925
-  CStrings:  3242
+  Functions: 4792
+  Symbols:   10990
+  CStrings:  3349
 
Symbols:
+ +[NSRelativeDateTimeFormatter(WBSNSRelativeDateTimeFormatterExtras) safari_suggestionsRelativeDateTimeFormatter]
+ -[NSBundle(SafariCoreExtras) safari_isPasswordsMenuBarAppBundle]
+ -[NSRelativeDateTimeFormatter(WBSNSRelativeDateTimeFormatterExtras) safari_suggestionsLocalizedStringRelativeToNowForDate:]
+ -[WBSAnalyticsLogger didEnableTheaterModeSBA]
+ -[WBSAnalyticsLogger didTogglePIPFromTheaterMode]
+ -[WBSAnalyticsLogger didVisitWebpageSBAWithUserOptedIn:]
+ -[WBSSQLiteDatabase _openWithFlags:useLock:vfs:error:]
+ -[WBSSQLiteDatabase _openWithFlags:useLock:vfs:error:].cold.1
+ -[WBSSavedAccount _setUser:password:].cold.2
+ GCC_except_table412
+ GCC_except_table415
+ GCC_except_table426
+ GCC_except_table431
+ GCC_except_table434
+ GCC_except_table47
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSRelativeDateTimeFormatter
+ _USLocaleIdentifier
+ _WBSAllowedCreditCardNumberSeparatorCharacters
+ _WBSCreditCardCardholderFieldLabels
+ _WBSCreditCardCompositeExpirationDateFieldLabels
+ _WBSCreditCardNumberFieldLabels
+ _WBSCreditCardSecurityCodeFieldLabels
+ _WBSCreditCardTypeFieldLabels
+ _WBSCreditCardTypeFromNumber
+ _WBSCreditCardTypeFromNumberAllowingPartialMatch
+ _WBSCreditCardTypeLocalizedName
+ _WBSCreditCardTypeLocalizedNameForGeneratingCardNames
+ _WBSCreditCardTypeSynonyms
+ _WBSDisplayTextForCreditCardNumber
+ _WBSExpirationDateWithDayMonthYear
+ _WBSIgnorePasswordGenerationIsDisallowedByRequirementsKey
+ _WBSLastDigitsOfCreditCardNumber
+ _WBSLocaleForCreditCardExpirationDate
+ _WBSNonCreditCardCardNumberFieldLabels
+ _WBSNormalizedCreditCardNumber
+ _WBSPasswordsMenuBarAppBundleIdentifier
+ __112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke.305
+ __126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.338
+ __126-[WBSSavedAccountStore _relyingPartyURLForPasskeyCredentialIdentifierOnInternalQueue:credentialIdentifiersToAutoFillPasskeys:]_block_invoke.405
+ __145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.366
+ __145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.367
+ __147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.430
+ __147-[WBSSavedAccountStore _loadSavedAccountsWithPasswordsFromKeychainData:forGroupID:withDictionaryForSavedAccountsWithPasswords:fromRecentlyDeleted:]_block_invoke.203
+ __147-[WBSSavedAccountStore _loadSavedAccountsWithPasswordsFromKeychainData:forGroupID:withDictionaryForSavedAccountsWithPasswords:fromRecentlyDeleted:]_block_invoke_2.205
+ __147-[WBSSavedAccountStore _loadSavedAccountsWithPasswordsFromKeychainData:forGroupID:withDictionaryForSavedAccountsWithPasswords:fromRecentlyDeleted:]_block_invoke_3.206
+ __147-[WBSSavedAccountStore _loadSavedAccountsWithPasswordsFromKeychainData:forGroupID:withDictionaryForSavedAccountsWithPasswords:fromRecentlyDeleted:]_block_invoke_4.209
+ __53-[WBSSavedAccountStore _fetchSignInWithAppleAccounts]_block_invoke.229
+ __54-[WBSSavedAccountStore changeSavedAccountWithRequest:]_block_invoke.278
+ __56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.350
+ __56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.350.cold.1
+ __56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.354
+ __60-[WBSAnalyticsLogger _sendEventAddingVersionInfo:baseEvent:]_block_invoke.768
+ __66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.374
+ __66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.378
+ __69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.349
+ __86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.396
+ __86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.400
+ __86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.373
+ __88-[WBSSavedAccountStore _updateCachedSignInWithAppleAccountsOnInternalQueueWithAccounts:]_block_invoke.237
+ __90-[WBSSavedAccountStore _performLegacySidecarModificationWithChangeRequest:toSavedAccount:]_block_invoke.281
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSRelativeDateTimeFormatter_$_WBSNSRelativeDateTimeFormatterExtras
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSRelativeDateTimeFormatter_$_WBSNSRelativeDateTimeFormatterExtras
+ __OBJC_$_CATEGORY_NSRelativeDateTimeFormatter_$_WBSNSRelativeDateTimeFormatterExtras
+ __ZGVZ45WBSAllowedCreditCardNumberSeparatorCharactersE10separators
+ __ZL13isMaestroCardmlb
+ __ZL16creditCardLabels22CreditCardStringNumber
+ __ZL22gregorianDateFromPartslll
+ __ZL25suddenTerminationDisabler
+ __ZL29suddenTerminationDisablerLock
+ __ZL35temporarilyDisableSuddenTerminationv
+ __ZL39suddenTerminationDisablerDispatchSource
+ __ZL9isJCBCardmlb
+ __ZZ36WBSLocaleForCreditCardExpirationDateE33localeForCreditCardExpirationDate
+ __ZZ36WBSLocaleForCreditCardExpirationDateE4once
+ __ZZ45WBSAllowedCreditCardNumberSeparatorCharactersE10separators
+ __ZZL50ignorePasswordGenerationIsDisallowedByRequirementsvE4once
+ __ZZL50ignorePasswordGenerationIsDisallowedByRequirementsvE50ignorePasswordGenerationIsDisallowedByRequirements
+ ___50-[WBSSavedAccountStore knownWebsiteNamesDidChange]_block_invoke
+ ___56-[WBSAnalyticsLogger didVisitWebpageSBAWithUserOptedIn:]_block_invoke
+ ___60-[WBSSavedAccountStore knownWebsiteNamesDidChangeOnDomains:]_block_invoke
+ ___68-[WBSSavedAccountStore _updateShowServiceNamesInPasswordsPreference]_block_invoke
+ ___76-[WBSSavedAccountStore setShouldShowServiceNamesForPasswordAndPasskeyItems:]_block_invoke_2
+ ___WBSLocaleForCreditCardExpirationDate_block_invoke
+ ____ZL35temporarilyDisableSuddenTerminationv_block_invoke
+ ____ZL50ignorePasswordGenerationIsDisallowedByRequirementsv_block_invoke
+ __block_literal_global.101
+ __block_literal_global.1025
+ __block_literal_global.1093
+ __block_literal_global.1230
+ __block_literal_global.1232
+ __block_literal_global.1237
+ __block_literal_global.1239
+ __block_literal_global.1241
+ __block_literal_global.1243
+ __block_literal_global.1245
+ __block_literal_global.1247
+ __block_literal_global.1249
+ __block_literal_global.1251
+ __block_literal_global.1253
+ __block_literal_global.1255
+ __block_literal_global.1257
+ __block_literal_global.1259
+ __block_literal_global.1306
+ __block_literal_global.1327
+ __block_literal_global.1329
+ __block_literal_global.1331
+ __block_literal_global.1333
+ __block_literal_global.1335
+ __block_literal_global.1337
+ __block_literal_global.1381
+ __block_literal_global.1383
+ __block_literal_global.1385
+ __block_literal_global.1393
+ __block_literal_global.1395
+ __block_literal_global.1397
+ __block_literal_global.157
+ __block_literal_global.163
+ __block_literal_global.170
+ __block_literal_global.175
+ __block_literal_global.177
+ __block_literal_global.179
+ __block_literal_global.181
+ __block_literal_global.183
+ __block_literal_global.196
+ __block_literal_global.208
+ __block_literal_global.212
+ __block_literal_global.217
+ __block_literal_global.221
+ __block_literal_global.234
+ __block_literal_global.236
+ __block_literal_global.251
+ __block_literal_global.253
+ __block_literal_global.259
+ __block_literal_global.265
+ __block_literal_global.324
+ __block_literal_global.326
+ __block_literal_global.337
+ __block_literal_global.358
+ __block_literal_global.369
+ __block_literal_global.377
+ __block_literal_global.390
+ __block_literal_global.425
+ __block_literal_global.445
+ __block_literal_global.593
+ __block_literal_global.65
+ __block_literal_global.745
+ __block_literal_global.753
+ __block_literal_global.77
+ __block_literal_global.770
+ __block_literal_global.782
+ __block_literal_global.79
+ __block_literal_global.791
+ __block_literal_global.800
+ __block_literal_global.81
+ __block_literal_global.819
+ __block_literal_global.820
+ __block_literal_global.83
+ __block_literal_global.86
+ __block_literal_global.88
+ __block_literal_global.888
+ __block_literal_global.897
+ __block_literal_global.903
+ __block_literal_global.94
+ __block_literal_global.989
+ __block_literal_global.991
+ _objc_msgSend$_openWithFlags:useLock:vfs:error:
+ _objc_msgSend$dateByAddingComponents:toDate:options:
+ _objc_msgSend$hasInternalContent
+ _objc_msgSend$isDateInYesterday:
+ _objc_msgSend$localizedStringForDate:relativeToDate:
+ _objc_msgSend$processName
+ _objc_msgSend$safari_isPasswordsMenuBarAppBundle
+ _objc_msgSend$setDateTimeStyle:
+ _objc_msgSend$setMonth:
+ _objc_msgSend$setYear:
+ _objc_msgSend$year
- +[WBSFeatureAvailability isDifferentPrivateBrowsingSearchEngineEnabled]
- +[WBSFeatureAvailability isEnhancedPrivateBrowsingEnabled]
- +[WBSFeatureAvailability isProfileStartPageCustomizationEnabled]
- +[WBSFeatureAvailability isSearchUIRefinementsEnabled]
- -[WBSAnalyticsLogger didToggleTheaterModeSBA]
- -[WBSAnalyticsLogger didVisitWebpageSBA]
- -[WBSSQLiteDatabase _openWithFlags:vfs:error:]
- -[WBSSQLiteDatabase _openWithFlags:vfs:error:].cold.1
- GCC_except_table411
- GCC_except_table420
- GCC_except_table425
- GCC_except_table430
- __112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke.298
- __126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.331
- __126-[WBSSavedAccountStore _relyingPartyURLForPasskeyCredentialIdentifierOnInternalQueue:credentialIdentifiersToAutoFillPasskeys:]_block_invoke.398
- __145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.359
- __145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.360
- __147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.424
- __147-[WBSSavedAccountStore _loadSavedAccountsWithPasswordsFromKeychainData:forGroupID:withDictionaryForSavedAccountsWithPasswords:fromRecentlyDeleted:]_block_invoke.200
- __147-[WBSSavedAccountStore _loadSavedAccountsWithPasswordsFromKeychainData:forGroupID:withDictionaryForSavedAccountsWithPasswords:fromRecentlyDeleted:]_block_invoke_2.202
- __147-[WBSSavedAccountStore _loadSavedAccountsWithPasswordsFromKeychainData:forGroupID:withDictionaryForSavedAccountsWithPasswords:fromRecentlyDeleted:]_block_invoke_3.203
- __147-[WBSSavedAccountStore _loadSavedAccountsWithPasswordsFromKeychainData:forGroupID:withDictionaryForSavedAccountsWithPasswords:fromRecentlyDeleted:]_block_invoke_4.206
- __53-[WBSSavedAccountStore _fetchSignInWithAppleAccounts]_block_invoke.225
- __54-[WBSSavedAccountStore changeSavedAccountWithRequest:]_block_invoke.274
- __56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.343
- __56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.343.cold.1
- __56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.347
- __60-[WBSAnalyticsLogger _sendEventAddingVersionInfo:baseEvent:]_block_invoke.765
- __66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.367
- __66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.371
- __69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.342
- __86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.389
- __86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.393
- __86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.366
- __88-[WBSSavedAccountStore _updateCachedSignInWithAppleAccountsOnInternalQueueWithAccounts:]_block_invoke.233
- __90-[WBSSavedAccountStore _performLegacySidecarModificationWithChangeRequest:toSavedAccount:]_block_invoke.277
- ___62-[WBSSavedAccountStore _notifyClientsAboutWebsiteNamesChanges]_block_invoke_2
- ___64+[WBSFeatureAvailability isProfileStartPageCustomizationEnabled]_block_invoke
- __block_literal_global.102
- __block_literal_global.1022
- __block_literal_global.1090
- __block_literal_global.1227
- __block_literal_global.1229
- __block_literal_global.1234
- __block_literal_global.1236
- __block_literal_global.1238
- __block_literal_global.1240
- __block_literal_global.1242
- __block_literal_global.1244
- __block_literal_global.1246
- __block_literal_global.1248
- __block_literal_global.1250
- __block_literal_global.1252
- __block_literal_global.1254
- __block_literal_global.1256
- __block_literal_global.1303
- __block_literal_global.1324
- __block_literal_global.1326
- __block_literal_global.1328
- __block_literal_global.1330
- __block_literal_global.1332
- __block_literal_global.1334
- __block_literal_global.1378
- __block_literal_global.1380
- __block_literal_global.1382
- __block_literal_global.1390
- __block_literal_global.1392
- __block_literal_global.1394
- __block_literal_global.154
- __block_literal_global.167
- __block_literal_global.169
- __block_literal_global.174
- __block_literal_global.176
- __block_literal_global.178
- __block_literal_global.180
- __block_literal_global.193
- __block_literal_global.205
- __block_literal_global.209
- __block_literal_global.214
- __block_literal_global.218
- __block_literal_global.230
- __block_literal_global.232
- __block_literal_global.245
- __block_literal_global.247
- __block_literal_global.255
- __block_literal_global.261
- __block_literal_global.312
- __block_literal_global.317
- __block_literal_global.330
- __block_literal_global.351
- __block_literal_global.355
- __block_literal_global.370
- __block_literal_global.383
- __block_literal_global.419
- __block_literal_global.439
- __block_literal_global.590
- __block_literal_global.66
- __block_literal_global.742
- __block_literal_global.750
- __block_literal_global.767
- __block_literal_global.779
- __block_literal_global.78
- __block_literal_global.788
- __block_literal_global.797
- __block_literal_global.80
- __block_literal_global.812
- __block_literal_global.816
- __block_literal_global.82
- __block_literal_global.87
- __block_literal_global.885
- __block_literal_global.889
- __block_literal_global.89
- __block_literal_global.895
- __block_literal_global.95
- __block_literal_global.986
- __block_literal_global.988
- _objc_msgSend$_openWithFlags:vfs:error:
- _objc_msgSend$disableSuddenTerminationForAccountStoreLoad
- _objc_msgSend$enableSuddenTerminationForAccountStoreLoad
- _objc_msgSend$isEnhancedPrivateBrowsingEnabled
- isProfileStartPageCustomizationEnabled.isProfileStartPageCustomizationEnabled
- isProfileStartPageCustomizationEnabled.onceToken
CStrings:
+ " -"
+ "%!l(MISSING)d"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/SafariCore/FoundationExtras/WBSCoreNSBundleExtras.m"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/SafariCore/Preferences/WBSSearchEnginePreferenceObserver.m"
+ "?nolock=1"
+ "AMEX"
+ "American Express"
+ "American Express (credit card type for filling)"
+ "AuthenticationServicesAgent"
+ "Carte Blanche"
+ "CarteBlanche"
+ "China UnionPay"
+ "China UnionPay card"
+ "ChinaUnionPay"
+ "Diner's Club"
+ "Diner's Club International"
+ "Diners Club"
+ "Diners Club International"
+ "Discover"
+ "Discover Card"
+ "Discover card"
+ "En Route"
+ "EnRoute"
+ "InstaPayment"
+ "InstaPayment card"
+ "JCB"
+ "JCB card"
+ "Maestro"
+ "Maestro card"
+ "Master Card"
+ "MasterCard"
+ "Mastercard"
+ "Mastercard (credit card type for filling)"
+ "Switch"
+ "Today (Frequently Visited)"
+ "Visa"
+ "Visa (credit card name)"
+ "Visa (credit card type for filling)"
+ "WBSIgnorePasswordGenerationIsDisallowedByRequirements"
+ "Yesterday"
+ "caduca"
+ "caducidad"
+ "card #"
+ "card holder"
+ "card number"
+ "card type"
+ "card verification"
+ "card#"
+ "cardholder"
+ "cardnum"
+ "cardnumber"
+ "cardtype"
+ "cc num"
+ "cc type"
+ "ccnum"
+ "ccnumber"
+ "cctype"
+ "ccv2"
+ "cid"
+ "codice di sicurezza"
+ "com.apple.Safari.SmartBrowsingAssistant.didEnableTheaterMode"
+ "com.apple.Safari.SmartBrowsingAssistant.didTogglePIPFromTheaterMode"
+ "com.apple.SafariCore.WBSSQLiteStatement"
+ "credit card no"
+ "credit card number"
+ "creditcardno"
+ "creditcardnumber"
+ "cvc"
+ "cvc2"
+ "cvn"
+ "cvv"
+ "cvv2"
+ "cvvx"
+ "data de validade"
+ "date d'expiration"
+ "en_US"
+ "expdate"
+ "expira"
+ "expiration"
+ "expiration date"
+ "expirationdate"
+ "expire"
+ "expires"
+ "expiry"
+ "file:%!s(MISSING)"
+ "gift card"
+ "gift code"
+ "giftcard"
+ "giftcode"
+ "health card"
+ "kartenmarke"
+ "kartennummer"
+ "kreditkartennummer"
+ "library card"
+ "loyalty card"
+ "loyaltycard"
+ "name des karteninhabers"
+ "name on card"
+ "name on credit card"
+ "nameoncard"
+ "newcreditcardnumber"
+ "nom du titulaire de la carte"
+ "nombre en la tarjeta"
+ "nome sulla carta"
+ "numero carta di credito"
+ "numero della carta di credito"
+ "optedIn"
+ "pan"
+ "payment type"
+ "rewards card"
+ "rewardscard"
+ "scadenza"
+ "security code"
+ "sicherheitscode"
+ "titolare carta"
+ "titolare della carta"
+ "titolare della carta di credito"
+ "titular de la tarjeta"
+ "user profile"
+ "y"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/SafariCore/FoundationExtras/WBSCoreNSBundleExtras.m"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/SafariCore/Preferences/WBSSearchEnginePreferenceObserver.m"
- "Easily guessed password, previously shared passkey"
- "Easily guessed password, previously shared passkey and password"
- "Easily guessed, previously shared"
- "Easily guessed, previously shared password"
- "EnableLockedPrivateBrowsing"
- "EnableSafariProfileStartPageCustomization"
- "Reused password, previously shared passkey"
- "Reused password, previously shared passkey and password"
- "Reused, previously shared"
- "Reused, previously shared password"
- "com.apple.Safari.SmartBrowsingAssistant.didToggleTheaterMode"

```
