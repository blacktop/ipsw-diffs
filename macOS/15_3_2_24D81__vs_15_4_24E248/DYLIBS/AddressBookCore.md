## AddressBookCore

> `/System/Library/PrivateFrameworks/AddressBookCore.framework/Versions/A/AddressBookCore`

```diff

-2695.400.2.0.0
-  __TEXT.__text: 0xebef4
+2695.500.71.0.0
+  __TEXT.__text: 0xec224
   __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x11408
-  __TEXT.__const: 0x1c4
+  __TEXT.__objc_methlist: 0x128bc
+  __TEXT.__const: 0x1d4
   __TEXT.__cstring: 0xc77f
-  __TEXT.__gcc_except_tab: 0x3d7c
+  __TEXT.__gcc_except_tab: 0x3f0c
   __TEXT.__oslogstring: 0x5707
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__unwind_info: 0x5548
+  __TEXT.__unwind_info: 0x5690
   __TEXT.__objc_classname: 0x2cae
   __TEXT.__objc_methname: 0x23326
   __TEXT.__objc_methtype: 0x3614

   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x90d8
+  __DATA_CONST.__objc_selrefs: 0x91b8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x688
   __DATA_CONST.__objc_arraydata: 0x148
   __AUTH_CONST.__auth_got: 0x830
   __AUTH_CONST.__const: 0x5b40
   __AUTH_CONST.__cfstring: 0xe300
-  __AUTH_CONST.__objc_const: 0x1c1b0
+  __AUTH_CONST.__objc_const: 0x19bd8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C6142A2-BBD2-3EBA-B69B-6FD81C2CA1A4
-  Functions: 7080
-  Symbols:   17633
+  UUID: 980C3D38-4192-3B11-99AB-708A0FB1B915
+  Functions: 7247
+  Symbols:   17820
   CStrings:  11028
 
Symbols:
+ +[ABACAccountPersistenceBackend os_log].cold.1
+ +[ABACInProcessAccountStore log].cold.1
+ +[ABAccount os_log].cold.1
+ +[ABAccount(ABCDContainer) os_log_deprecated].cold.1
+ +[ABAccountBackupOperation os_log].cold.1
+ +[ABAccountComparer os_log].cold.1
+ +[ABAccountComponentsValidationHelper os_log].cold.1
+ +[ABAccountDataDeletionOperation os_log].cold.1
+ +[ABAccountFactory os_log].cold.1
+ +[ABAccountMigrationOperation os_log].cold.1
+ +[ABAccountMigrator os_log].cold.1
+ +[ABAccountRepository os_log].cold.1
+ +[ABAccountStatus(Factory) networkActivityStatus].cold.1
+ +[ABAccountStatus(Factory) noStatus].cold.1
+ +[ABAccountsTracing tracingScheduler].cold.1
+ +[ABAddressBook os_log].cold.1
+ +[ABAddressBook os_log_activation].cold.1
+ +[ABAddressBook os_log_locking].cold.1
+ +[ABAddressBook os_log_saving].cold.1
+ +[ABAddressBook os_log_setup].cold.1
+ +[ABAddressBook os_log_triage].cold.1
+ +[ABAddressBook recordClassFromUniqueId:].cold.1
+ +[ABAddressBookChangesNotifier os_log].cold.1
+ +[ABApplicationServices isRunningInContactsApplication].cold.1
+ +[ABCDRecordMapper sharedInstance].cold.1
+ +[ABCDSmartGroup(AddressBook) os_log].cold.1
+ +[ABCN(PropertyDescription) alertTonesDescription].cold.1
+ +[ABCN(PropertyDescription) alternateBirthdayComponentsDescription].cold.1
+ +[ABCN(PropertyDescription) birthdayComponentsDescription].cold.1
+ +[ABCN(PropertyDescription) companyNameDescription].cold.1
+ +[ABCN(PropertyDescription) creationDateDescription].cold.1
+ +[ABCN(PropertyDescription) departmentDescription].cold.1
+ +[ABCN(PropertyDescription) displayStyleDescription].cold.1
+ +[ABCN(PropertyDescription) emailAddressesDescription].cold.1
+ +[ABCN(PropertyDescription) firstNameDescription].cold.1
+ +[ABCN(PropertyDescription) identifierDescription].cold.1
+ +[ABCN(PropertyDescription) instantMessagAddressesDescription].cold.1
+ +[ABCN(PropertyDescription) jobTitleDescription].cold.1
+ +[ABCN(PropertyDescription) lastNameDescription].cold.1
+ +[ABCN(PropertyDescription) linkIdentifierDescription].cold.1
+ +[ABCN(PropertyDescription) maidenNameDescription].cold.1
+ +[ABCN(PropertyDescription) middleNameDescription].cold.1
+ +[ABCN(PropertyDescription) nameOrderDescription].cold.1
+ +[ABCN(PropertyDescription) nameSuffixDescription].cold.1
+ +[ABCN(PropertyDescription) nameTitleDescription].cold.1
+ +[ABCN(PropertyDescription) nicknameDescription].cold.1
+ +[ABCN(PropertyDescription) noteDescription].cold.1
+ +[ABCN(PropertyDescription) otherDateComponentsDescription].cold.1
+ +[ABCN(PropertyDescription) otherDatesDescription].cold.1
+ +[ABCN(PropertyDescription) phoneNumbersDescription].cold.1
+ +[ABCN(PropertyDescription) phonemeDataDescription].cold.1
+ +[ABCN(PropertyDescription) phoneticCompanyNameDescription].cold.1
+ +[ABCN(PropertyDescription) phoneticFirstNameDescription].cold.1
+ +[ABCN(PropertyDescription) phoneticLastNameDescription].cold.1
+ +[ABCN(PropertyDescription) phoneticMiddleNameDescription].cold.1
+ +[ABCN(PropertyDescription) postalAddressesDescription].cold.1
+ +[ABCN(PropertyDescription) preferredApplePersonaIdentifierDescription].cold.1
+ +[ABCN(PropertyDescription) preferredForNameDescription].cold.1
+ +[ABCN(PropertyDescription) preferredForPhotoDescription].cold.1
+ +[ABCN(PropertyDescription) preferredLikenessSourceDescription].cold.1
+ +[ABCN(PropertyDescription) relatedNamesDescription].cold.1
+ +[ABCN(PropertyDescription) ringtoneDescription].cold.1
+ +[ABCN(PropertyDescription) socialProfilesDescription].cold.1
+ +[ABCN(PropertyDescription) sortingFirstNameDescription].cold.1
+ +[ABCN(PropertyDescription) sortingLastNameDescription].cold.1
+ +[ABCN(PropertyDescription) texttoneDescription].cold.1
+ +[ABCN(PropertyDescription) urlAddressesDescription].cold.1
+ +[ABCNContact preferredPhotoComparator].cold.1
+ +[ABCNContactNameOrderImpl defaultNewContactOrder].cold.1
+ +[ABCNContactNameOrderImpl defaultOrder].cold.1
+ +[ABCNContactNameOrderImpl firstNameFirstOrder].cold.1
+ +[ABCNContactNameOrderImpl isChineseJapaneseKoreanContact:].cold.1
+ +[ABCNContactNameOrderImpl lastNameFirstOrder].cold.1
+ +[ABCNContactNameSorting firstNameFirstComparator].cold.1
+ +[ABCNContactNameSorting lastNameFirstComparator].cold.1
+ +[ABCNGroup identifierProvider].cold.1
+ +[ABCNLabeledValue emptyEntries].cold.1
+ +[ABCNLabeledValue identifierProvider].cold.1
+ +[ABCNMultiValueDiff emptyDiff].cold.1
+ +[ABDataSourceExternalNotificationObserver log].cold.1
+ +[ABDateHelper calendarWithOffsetFromGMT:].cold.1
+ +[ABDateHelper gmtCalendar].cold.1
+ +[ABDateHelper gregorianCalendarInGMT].cold.1
+ +[ABDateHelper gregorianCalendar].cold.1
+ +[ABDateHelper localCalendar].cold.1
+ +[ABDefaultAccountPermissions defaultAccountPermissions].cold.1
+ +[ABDefaultAccountPreference os_log].cold.1
+ +[ABDelegateAccessAccountCollection os_log].cold.1
+ +[ABDictionaryImporter migration].cold.1
+ +[ABDirectoryServicesAccountConfiguration log].cold.1
+ +[ABDirectoryServicesConnectivityTest log].cold.1
+ +[ABDistributedNotificationListener os_log].cold.1
+ +[ABExchangeLabelsConstraint emailLabels].cold.1
+ +[ABExchangeLabelsConstraint otherDatesLabels].cold.1
+ +[ABExchangeLabelsConstraint propertyToInitialLabelDictionary].cold.1
+ +[ABExchangeLabelsConstraint unsupportedProperties].cold.1
+ +[ABExchangeLabelsConstraint urlLabels].cold.1
+ +[ABFileServices sharedInstance].cold.1
+ +[ABFileUtilities sharedInstance].cold.1
+ +[ABGroup userInterfaceComparator].cold.1
+ +[ABImportsAddressBookData os_log].cold.1
+ +[ABInstantMessageService textChatURITemplatesByServiceKey].cold.1
+ +[ABLegacyIMSearchElementTransformer sharedLegacyIMTransformer].cold.1
+ +[ABLibraryDirectoryImageTask _cacheAvailableLibraryImagesPeopleFolders].cold.1
+ +[ABMetadataOperationController checksumMode].cold.1
+ +[ABMetadataOperationController operationQueue].cold.1
+ +[ABMetadataOperationController os_log].cold.1
+ +[ABMetadataOperationController sharedIgnoredDirectories].cold.1
+ +[ABMetadataOperationController shouldDisableValidation].cold.1
+ +[ABMetadataType group].cold.1
+ +[ABMetadataType info].cold.1
+ +[ABMetadataType person].cold.1
+ +[ABPersistentStoreCoordinatorCache os_log].cold.1
+ +[ABPerson os_log].cold.1
+ +[ABPropertyDefaults defaultToPropertyDictionary].cold.1
+ +[ABPushNotificationCenter log].cold.1
+ +[ABRecord typeOfProperty:withAddressBook:].cold.1
+ +[ABRemoteImageLoader sharedRemoteImageLoader].cold.1
+ +[ABSchedulers distributedNotificationPreprocessingScheduler].cold.1
+ +[ABSearchElementTransformer sharedTransformer].cold.1
+ +[ABSimilarRecordMerger os_log].cold.1
+ +[ABSmartGroup os_log].cold.1
+ +[ABSocialProfileURLParser servicesDictionary].cold.1
+ +[ABStringTokenizer isCharacterNonBreaking:].cold.1
+ +[ABSyncManager os_log].cold.1
+ +[ABSyncManager sharedSyncManager].cold.1
+ +[ABSyncStandbyOperation log].cold.1
+ +[ABTargetedAccountComponentValidationHelper os_log].cold.1
+ +[ABUserDefaults log].cold.1
+ +[ABXPCACAccountStore os_log].cold.1
+ +[ABXPCACAccountStore sharedACAccountStore].cold.1
+ +[CNPendingMigrationManager log].cold.1
+ +[CNPendingMigrationManager pendingAccountMigrationsStore].cold.1
+ +[PHXSource migrationLog].cold.1
+ +[PHXSource syncLog].cold.1
+ -[ABAddressBook accountsDidChangePriv:].cold.1
+ -[ABAddressBook nts_meUniqueIdsFromInfos:].cold.1
+ -[ABAddressBook validateMetaData].cold.1
+ -[ABCDContact(MergingInternalAdditions) _messagingServiceNameKeyPath].cold.1
+ -[ABCNFirstNameFirstNameOrder nameKeys].cold.1
+ -[ABCNFirstNameFirstNameOrder phoneticNameKeys].cold.1
+ -[ABCNLastNameFirstNameOrder nameKeys].cold.1
+ -[ABCNLastNameFirstNameOrder phoneticNameKeys].cold.1
+ -[ABCNPhoneNumbersDescription equivalentLabelSets].cold.1
+ -[ABCNPropertyDescription equivalentLabelSets].cold.1
+ -[ABManagedObjectContext logCallStack:].cold.1
+ -[ABPerson valueSanitizer].cold.1
+ -[ABRecord valueSanitizer].cold.1
+ -[PHXSource migrationLog:].cold.1
+ ABAddressBookCoreFrameworkBundle.cold.1
+ ABAddressBookFrameworkBundle.cold.1
+ ABGroupCreate.cold.1
+ ABIsAccessGranted.cold.1
+ ABPersonCreate.cold.1
+ ABPersonCreateWithVCardRepresentation.cold.1
+ ABProcessIsWhitelistedForServer.cold.1
+ ABPropertyForValueVisibilityDefaultKey.cold.1
+ ABSocialProfileStandardServices.cold.1
+ ABValueVisibilityDefaultKeyForProperty.cold.1
+ ABValueVisibilityDefaultKeys.cold.1
+ GCC_except_table174
+ GCC_except_table182
+ GCC_except_table188
+ GCC_except_table194
+ GCC_except_table208
+ GCC_except_table214
+ GCC_except_table220
+ GCC_except_table225
+ GCC_except_table245
+ __43+[ABXPCACAccountStore sharedACAccountStore]_block_invoke.cold.1
+ _cachedABPersonProperties.cold.1
+ _typeOfABPersonProperty.cold.1
+ initACAccount.cold.1
+ initACAccountTypeIdentifierCardDAV.cold.1
+ initACAccountTypeIdentifierCardDAVLegacy.cold.1
+ initACAccountTypeIdentifierExchange.cold.1
+ initACAccountTypeIdentifierLDAP.cold.1
+ initACMonitoredAccountStore.cold.1
+ initCNCDIOSLegacyIdentifierRegistrar.cold.1
+ initCNCDIOSLegacyIdentifierXPCRegistrar.cold.1
+ initCNChangesNotifier.cold.1
+ initCNContactFormatter.cold.1
+ initCNContactsEnvironment.cold.1
+ initCNPostalAddress.cold.1
+ initNSBitmapImageRep.cold.1
+ initNSImage.cold.1
+ initNSImageInterpolationHigh.cold.1
+ initkACDiscoverPropertiesDiscoverConnectionPropertiesKey.cold.1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABAddressBook.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABAddressBookC.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABAddressBookHackery.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABAddressBook_MailSearch.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABCDRecord.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABDictionaryImporter.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABGroup.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABImageLoading.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABInfo.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABLog.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABMetadataAddOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABMetadataOperationController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABMultiValueCoreDataWrapper.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABNameCollisionMap.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABNetworkController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABPerson.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABPersonSorting.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABRecord.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABRecordMover.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABRecordVCardAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABSearchElement.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABSearchOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABSmartGroup.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/PHXSource.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBookUI/ABAllGroup.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBookUI/ABMergePeopleCommand.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/Contacts/ABCNContactDiff.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/Contacts/ABCNLegacyAddressBookDataMapper.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABAddressBook.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABAddressBookC.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABAddressBookHackery.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABAddressBook_MailSearch.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABCDRecord.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABDictionaryImporter.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABGroup.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABImageLoading.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABInfo.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABLog.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABMetadataAddOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABMetadataOperationController.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABMultiValueCoreDataWrapper.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABNameCollisionMap.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABNetworkController.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABPerson.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABPersonSorting.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABRecord.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABRecordMover.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABRecordVCardAdditions.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABSearchElement.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABSearchOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/ABSmartGroup.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBook/PHXSource.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBookUI/ABAllGroup.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/AddressBookUI/ABMergePeopleCommand.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/Contacts/ABCNContactDiff.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AddressBook/Framework/Contacts/ABCNLegacyAddressBookDataMapper.m"

```
