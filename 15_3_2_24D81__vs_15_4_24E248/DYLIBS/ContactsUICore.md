## ContactsUICore

> `/System/Library/PrivateFrameworks/ContactsUICore.framework/Versions/A/ContactsUICore`

```diff

-3647.400.1.0.0
-  __TEXT.__text: 0xc0104
+3647.500.41.0.0
+  __TEXT.__text: 0xbe1e8
   __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_methlist: 0x614c
-  __TEXT.__const: 0x4014
-  __TEXT.__oslogstring: 0x3562
-  __TEXT.__cstring: 0x596e
+  __TEXT.__objc_methlist: 0x6f8c
+  __TEXT.__const: 0x4084
+  __TEXT.__oslogstring: 0x3662
+  __TEXT.__cstring: 0x55be
   __TEXT.__gcc_except_tab: 0x810
   __TEXT.__dlopen_cstrs: 0x51
-  __TEXT.__constg_swiftt: 0xa34
-  __TEXT.__swift5_typeref: 0x1668
+  __TEXT.__constg_swiftt: 0xab4
+  __TEXT.__swift5_typeref: 0x173e
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x9cf
-  __TEXT.__swift5_fieldmd: 0x8fc
+  __TEXT.__swift5_reflstr: 0xa2f
+  __TEXT.__swift5_fieldmd: 0x984
   __TEXT.__swift5_assocty: 0x570
-  __TEXT.__swift5_proto: 0x378
-  __TEXT.__swift5_types: 0xbc
+  __TEXT.__swift5_proto: 0x3b4
+  __TEXT.__swift5_types: 0xcc
+  __TEXT.__swift_as_entry: 0xf0
+  __TEXT.__swift_as_ret: 0xc4
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_capture: 0x3e8
-  __TEXT.__unwind_info: 0x3288
-  __TEXT.__eh_frame: 0x1698
+  __TEXT.__swift5_capture: 0x11c
+  __TEXT.__unwind_info: 0x3468
+  __TEXT.__eh_frame: 0x1a7c
   __TEXT.__objc_classname: 0x1a8e
   __TEXT.__objc_methname: 0x1222a
   __TEXT.__objc_methtype: 0x2f0b
   __TEXT.__objc_stubs: 0xc640
-  __DATA_CONST.__got: 0xe08
-  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__got: 0xe78
+  __DATA_CONST.__const: 0xec0
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bd0
+  __DATA_CONST.__objc_selrefs: 0x3c88
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x1058
-  __AUTH_CONST.__const: 0x56a0
+  __AUTH_CONST.__const: 0x5160
   __AUTH_CONST.__cfstring: 0x2560
-  __AUTH_CONST.__objc_const: 0xfce8
+  __AUTH_CONST.__objc_const: 0xe3a0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0xc48
   __AUTH.__data: 0x890
   __DATA.__objc_ivar: 0x598
-  __DATA.__data: 0x28a8
-  __DATA.__bss: 0x7340
-  __DATA.__common: 0xe8
+  __DATA.__data: 0x29c0
+  __DATA.__bss: 0x7ac0
+  __DATA.__common: 0xf0
   __DATA_DIRTY.__objc_data: 0x2d50
   __DATA_DIRTY.__data: 0xc8
   __DATA_DIRTY.__bss: 0x210

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0D71EDEC-E76C-3E78-AB63-2AD3D37FA787
-  Functions: 4815
-  Symbols:   8351
-  CStrings:  4456
+  UUID: C716C0A7-89FC-395A-878F-5B263AF0DAF9
+  Functions: 4961
+  Symbols:   8542
+  CStrings:  4440
 
Symbols:
+ +[CNCapabilities shouldUseLegacyMessages].cold.1
+ +[CNHandle keyTypeMapping].cold.1
+ +[CNHandle(INPersonHandle) inPersonHandleTypeMap].cold.1
+ +[CNHandle(TUHandle) tuHandleTypeMap].cold.1
+ +[CNLSApplicationWorkspace inProcessLaunchServices].cold.1
+ +[CNLSApplicationWorkspace remoteAdapter].cold.1
+ +[CNUIContactPropertyRanker bestPropertyComparator].cold.1
+ +[CNUICoreContactFetchRequestAccumulator resultOfFetchRequest:fromStore:].cold.3
+ +[CNUICoreContactFetchRequestAccumulator resultOfFetchRequest:fromStore:].cold.4
+ +[CNUICoreEditAuthorizationCheck log].cold.1
+ +[CNUICoreLogProvider actions_os_log].cold.1
+ +[CNUICoreLogProvider color_os_log].cold.1
+ +[CNUICoreLogProvider corerecents_os_log].cold.1
+ +[CNUICoreLogProvider likenesses_os_log].cold.1
+ +[CNUICoreLogProvider static_identity_os_log].cold.1
+ +[CNUIIDSRequest IDSResponseQueue].cold.1
+ +[CNUIImageProvider imageForResource:template:onCacheMiss:].cold.1
+ +[CNUIInteractionDonor log].cold.1
+ +[CNUIMeContactMonitor log].cold.1
+ +[CNUISnowglobeUtilities enableGroupPhoto].cold.1
+ +[CNUIStaticIdentity ktStore].cold.1
+ +[CNUIUserActionCacheKeyGenerator os_log].cold.1
+ +[CNUIUserActionItemComparator preferredLabelScoreForUserAction:].cold.1
+ +[CNUIUserActionListDataSource allActionTypes].cold.1
+ +[CNUIUserActionListDataSource os_log].cold.1
+ +[CNUIUserActionListModel emptyModel].cold.1
+ +[CNUIUserActionTargetDiscovering os_log].cold.1
+ +[CNUIUserActivityManager log].cold.1
+ +[CNUIUserActivityRestorer log].cold.1
+ +[NSURL(ContactsUI) log].cold.1
+ +[_CNUILikenessCache log].cold.1
+ -[CNTUCallProviderManager providerManagerQueue].cold.1
+ -[CNUICoreContactAggregateValueFilter contactByFilteringOutPropertyValueOfContact:].cold.2
+ -[CNUICoreContactAggregateValueFilter initWithValueFilters:].cold.2
+ -[CNUICoreContactEdit initWithOriginalContact:modifiedContact:].cold.3
+ -[CNUICoreContactEdit initWithOriginalContact:modifiedContact:].cold.4
+ -[CNUICoreContactEditingSession addContacts:].cold.2
+ -[CNUICoreContactEditingSession removeContacts:].cold.2
+ -[CNUICoreContactEditingSession updateContacts:].cold.2
+ -[CNUICoreContactNicknameValueFilter contactByFilteringOutPropertyValueOfContact:].cold.2
+ -[CNUICoreContactNoteValueFilter contactByFilteringOutPropertyValueOfContact:].cold.2
+ -[CNUICoreContactPhotoValueFilter contactByFilteringOutPropertyValueOfContact:].cold.2
+ -[CNUICoreContactRefetcher initWithContactStore:contactsToRefetch:keysToFetch:].cold.4
+ -[CNUICoreContactRefetcher initWithContactStore:contactsToRefetch:keysToFetch:].cold.5
+ -[CNUICoreContactRefetcher initWithContactStore:contactsToRefetch:keysToFetch:].cold.6
+ -[CNUICoreContactRelationshipsFilter contactByFilteringOutPropertyValueOfContact:].cold.2
+ -[CNUICoreContactScratchpad initWithEdits:].cold.2
+ -[CNUICoreContactScratchpad scratchpadByAddingContacts:].cold.2
+ -[CNUICoreContactScratchpad scratchpadByKeepingContacts:].cold.2
+ -[CNUICoreContactScratchpad scratchpadByRemovingContacts:].cold.2
+ -[CNUICoreContactStoreProductionFacade initWithContactStore:].cold.2
+ -[CNUICoreContactStoreTestFacade initWithContacts:].cold.2
+ -[CNUICoreContactStoreTestFacade initWithMeContact:contacts:].cold.2
+ -[CNUICoreContactTypeAssessor initWithFamilyInfo:].cold.2
+ -[CNUICoreContactTypeAssessor initWithFamilyInfoFuture:].cold.2
+ -[CNUICoreFamilyElement initWithFamilyMember:matchingContacts:].cold.3
+ -[CNUICoreFamilyElement initWithFamilyMember:matchingContacts:].cold.4
+ -[CNUICoreFamilyInfo initWithMeContact:elements:].cold.2
+ -[CNUICoreFamilyInfoRetriever initWithMainContactStoreFacade:fetchFamilyCircleRequest:matchFamilyMembersWithContacts:schedulerProvider:].cold.4
+ -[CNUICoreFamilyInfoRetriever initWithMainContactStoreFacade:fetchFamilyCircleRequest:matchFamilyMembersWithContacts:schedulerProvider:].cold.5
+ -[CNUICoreFamilyInfoRetriever initWithMainContactStoreFacade:fetchFamilyCircleRequest:matchFamilyMembersWithContacts:schedulerProvider:].cold.6
+ -[CNUICoreFamilyMemberContactItem initWithContactIdentifier:formattedName:imageData:isUnreachable:isProposed:contactType:whitelistStatus:hasBeenPersisted:].cold.3
+ -[CNUICoreFamilyMemberContactItem initWithContactIdentifier:formattedName:imageData:isUnreachable:isProposed:contactType:whitelistStatus:hasBeenPersisted:].cold.4
+ -[CNUICoreFamilyMemberContactsController initWithFamilyMember:modelFetcher:familyMemberContactsUpdator:schedulerProvider:].cold.5
+ -[CNUICoreFamilyMemberContactsController initWithFamilyMember:modelFetcher:familyMemberContactsUpdator:schedulerProvider:].cold.6
+ -[CNUICoreFamilyMemberContactsController initWithFamilyMember:modelFetcher:familyMemberContactsUpdator:schedulerProvider:].cold.7
+ -[CNUICoreFamilyMemberContactsController initWithFamilyMember:modelFetcher:familyMemberContactsUpdator:schedulerProvider:].cold.8
+ -[CNUICoreFamilyMemberContactsModel initWithItems:].cold.2
+ -[CNUICoreFamilyMemberContactsModelRetriever initWithContactStoreFacade:familyInfoFetcher:downtimeContainerFetcher:schedulerProvider:].cold.4
+ -[CNUICoreFamilyMemberContactsModelRetriever initWithContactStoreFacade:familyInfoFetcher:downtimeContainerFetcher:schedulerProvider:].cold.5
+ -[CNUICoreFamilyMemberContactsModelRetriever initWithContactStoreFacade:familyInfoFetcher:downtimeContainerFetcher:schedulerProvider:].cold.6
+ -[CNUICoreFamilyMemberContactsStore initWithFamilyMemberScopedContactStoreFacade:familyMember:contactsSyncTrigger:schedulerProvider:].cold.4
+ -[CNUICoreFamilyMemberContactsStore initWithFamilyMemberScopedContactStoreFacade:familyMember:contactsSyncTrigger:schedulerProvider:].cold.5
+ -[CNUICoreFamilyMemberContactsStore initWithFamilyMemberScopedContactStoreFacade:familyMember:contactsSyncTrigger:schedulerProvider:].cold.6
+ -[CNUICoreFamilyMemberContactsStore updateContactListByAddingContacts:].cold.2
+ -[CNUICoreFamilyMemberContactsStore updateContactListByRemovingContacts:].cold.2
+ -[CNUICoreFamilyMemberContactsStore updateContactWhitelistByAddingContacts:].cold.2
+ -[CNUICoreFamilyMemberContactsStore updateContactWhitelistByRemovingContacts:].cold.2
+ -[CNUICoreFamilyMemberWhitelistedContactsController initWithModelFetcher:familyMemberContactsUpdator:familyMemberScopedContactStoreFacade:mainContactStoreFacade:schedulerProvider:].cold.10
+ -[CNUICoreFamilyMemberWhitelistedContactsController initWithModelFetcher:familyMemberContactsUpdator:familyMemberScopedContactStoreFacade:mainContactStoreFacade:schedulerProvider:].cold.6
+ -[CNUICoreFamilyMemberWhitelistedContactsController initWithModelFetcher:familyMemberContactsUpdator:familyMemberScopedContactStoreFacade:mainContactStoreFacade:schedulerProvider:].cold.7
+ -[CNUICoreFamilyMemberWhitelistedContactsController initWithModelFetcher:familyMemberContactsUpdator:familyMemberScopedContactStoreFacade:mainContactStoreFacade:schedulerProvider:].cold.8
+ -[CNUICoreFamilyMemberWhitelistedContactsController initWithModelFetcher:familyMemberContactsUpdator:familyMemberScopedContactStoreFacade:mainContactStoreFacade:schedulerProvider:].cold.9
+ -[CNUICoreInMemoryWhitelistedContactsDataSourceDecorator initWithDataSource:familyInfoRetriever:schedulerProvider:].cold.4
+ -[CNUICoreInMemoryWhitelistedContactsDataSourceDecorator initWithDataSource:familyInfoRetriever:schedulerProvider:].cold.5
+ -[CNUICoreInMemoryWhitelistedContactsDataSourceDecorator initWithDataSource:familyInfoRetriever:schedulerProvider:].cold.6
+ -[CNUICoreMainWhitelistedContactsController initWithModelFetcher:mainContactStoreFacade:downtimeContainerFetcher:schedulerProvider:].cold.5
+ -[CNUICoreMainWhitelistedContactsController initWithModelFetcher:mainContactStoreFacade:downtimeContainerFetcher:schedulerProvider:].cold.6
+ -[CNUICoreMainWhitelistedContactsController initWithModelFetcher:mainContactStoreFacade:downtimeContainerFetcher:schedulerProvider:].cold.7
+ -[CNUICoreMainWhitelistedContactsController initWithModelFetcher:mainContactStoreFacade:downtimeContainerFetcher:schedulerProvider:].cold.8
+ -[CNUICoreProposedContactsFetchingDecorator initWithModelFetcher:familyInfoFetcher:schedulerProvider:].cold.4
+ -[CNUICoreProposedContactsFetchingDecorator initWithModelFetcher:familyInfoFetcher:schedulerProvider:].cold.5
+ -[CNUICoreProposedContactsFetchingDecorator initWithModelFetcher:familyInfoFetcher:schedulerProvider:].cold.6
+ -[CNUIMeContactMonitor initWithComparisonStrategy:contactStore:notificationCenter:schedulerProvider:].cold.3
+ -[CNUIMeContactMonitor initWithComparisonStrategy:contactStore:notificationCenter:schedulerProvider:].cold.4
+ -[CNUIUserActionDisambiguationModeler thirdPartyActionsForContactProperty:].cold.1
+ -[CNUIUserActionItem targetHandle].cold.1
+ -[CNUIUserActionListDataSource initWithDiscoveringEnvironment:].cold.1
+ -[CNUIUserActionTargetDiscovering thirdPartyTargetsForBundleIdentifier:].cold.1
+ -[CNUIUserActivityManager initWithContactStore:applicationWorkspace:interactionDonor:].cold.4
+ -[CNUIUserActivityManager initWithContactStore:applicationWorkspace:interactionDonor:].cold.5
+ -[CNUIUserActivityManager initWithContactStore:applicationWorkspace:interactionDonor:].cold.6
+ CNUIBitmapContextCreate.cold.1
+ CNUIEmptyPixelImageGet.cold.1
+ GCC_except_table78
+ __51+[CNUIContactPropertyRanker bestPropertyComparator]_block_invoke_3.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_project_boxed_opaque_existential_0
+ _associated conformance 14ContactsUICore13ContactEntityV10AppIntents019PersonRepresentableD0AaD0eD0
+ _associated conformance 14ContactsUICore15ContactLikenessV10SilhouetteV10CodingKeys33_5227BE09AE8B8E75610652C4D42689FCLLOSHAASQ
+ _associated conformance 14ContactsUICore15ContactLikenessV10SilhouetteV10CodingKeys33_5227BE09AE8B8E75610652C4D42689FCLLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 14ContactsUICore15ContactLikenessV10SilhouetteV10CodingKeys33_5227BE09AE8B8E75610652C4D42689FCLLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 14ContactsUICore15ContactLikenessV8MonogramV10CodingKeys33_EB99F8354C6B21EC9FF31242ADAE23D3LLOSHAASQ
+ _associated conformance 14ContactsUICore15ContactLikenessV8MonogramV10CodingKeys33_EB99F8354C6B21EC9FF31242ADAE23D3LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 14ContactsUICore15ContactLikenessV8MonogramV10CodingKeys33_EB99F8354C6B21EC9FF31242ADAE23D3LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _symbolic SccySb_______pt_____G s5ErrorP s5NeverO
+ _symbolic _____ 14ContactsUICore15ContactLikenessV10SilhouetteV
+ _symbolic _____ 14ContactsUICore15ContactLikenessV10SilhouetteV10CodingKeys33_5227BE09AE8B8E75610652C4D42689FCLLO
+ _symbolic _____ 14ContactsUICore15ContactLikenessV8MonogramV
+ _symbolic _____ 14ContactsUICore15ContactLikenessV8MonogramV10CodingKeys33_EB99F8354C6B21EC9FF31242ADAE23D3LLO
+ _symbolic ______p s5ErrorP
+ _symbolic _____ySbSgG 10AppIntents15IntentParameterC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14ContactsUICore15ContactLikenessV10SilhouetteV10CodingKeys33_5227BE09AE8B8E75610652C4D42689FCLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14ContactsUICore15ContactLikenessV8MonogramV10CodingKeys33_EB99F8354C6B21EC9FF31242ADAE23D3LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 14ContactsUICore15ContactLikenessV10SilhouetteV10CodingKeys33_5227BE09AE8B8E75610652C4D42689FCLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 14ContactsUICore15ContactLikenessV8MonogramV10CodingKeys33_EB99F8354C6B21EC9FF31242ADAE23D3LLO
+ _symbolic _____y_____Sg______pG 7Combine6FutureC 14ContactsUICore15ContactLikenessV10SilhouetteV s5ErrorP
+ _symbolic _____y_____Sg______pG 7Combine6FutureC 14ContactsUICore15ContactLikenessV8MonogramV s5ErrorP
+ _symbolic _____y_____Sg______pGIegn_ s6ResultOsRi_zrlE 14ContactsUICore15ContactLikenessV10SilhouetteV s5ErrorP
+ _symbolic _____y_____Sg______pGIegn_ s6ResultOsRi_zrlE 14ContactsUICore15ContactLikenessV8MonogramV s5ErrorP
+ _symbolic _____y_____Sg______pGSg 7Combine6FutureC 14ContactsUICore15ContactLikenessV10SilhouetteV s5ErrorP
+ _symbolic _____y_____Sg______pGSg 7Combine6FutureC 14ContactsUICore15ContactLikenessV8MonogramV s5ErrorP
+ get_witness_table 10AppIntents21IntentResultContainerVy14ContactsUICore012ContactFetchD6EntityVs5NeverOA2HGAA12ReturnsValueHPyHC.13
+ get_witness_table 10AppIntents21IntentResultContainerVy14ContactsUICore018ContactAvatarFetchD6EntityVs5NeverOA2HGAA12ReturnsValueHPyHC.36
+ get_witness_table 10AppIntents21IntentResultContainerVy14ContactsUICore13ContactEntityVs5NeverOA2HGAA05OpensC0HPyHC.25
+ get_witness_table 10AppIntents21IntentResultContainerVy14ContactsUICore13ContactEntityVs5NeverOA2HGAA12ReturnsValueHPyHC.26
+ get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA05OpensC0HPyHC.35
+ get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.10
+ get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.7
+ initFTiMessageStatus.cold.1
+ initIDSCopyIDForEmailAddress.cold.1
+ initIDSCopyIDForPhoneNumberWithOptions.cold.1
+ initIDSServiceNameFaceTime.cold.1
+ initIDSServiceNameFaceTimeMultiway.cold.1
+ initIDSServiceNameiMessage.cold.1
+ initNSImage.cold.1
+ initNSWorkspace.cold.1
+ initPKPeerPaymentGetSendPaymentSensitiveURL.cold.1
+ initPKPeerPaymentIsAvailable.cold.1
+ initPRLikeness.cold.1
+ initPRMonogram.cold.1
+ initRTTTelephonyUtilities.cold.1
+ initSTManagementState.cold.1
+ initSTRemotePasscodeController.cold.1
+ initTUCallCapabilities.cold.1
+ initTUCallCapabilitiesFaceTimeAvailabilityChangedNotification.cold.1
+ initTUCallCenter.cold.1
+ initTUCallProviderManager.cold.1
+ initTUConversationMember.cold.1
+ initTUDialRequest.cold.1
+ initTUHandle.cold.1
+ initTUJoinConversationRequest.cold.1
+ keypath_get.4Tm
+ objectdestroy.30Tm
+ objectdestroy.7Tm
+ sIntentForActionType_block_invoke.cold.1
- GCC_except_table79
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_ContactsUICore
- _swift_initStackObject
- _symbolic SSIego_
- _symbolic SiIegd_
- _symbolic SiIegr_
- _symbolic So9CNContactC
- _symbolic _____ 10Foundation4DataV
- _symbolic _____ s5UInt8V
- _symbolic _____ySbG 10AppIntents15IntentParameterC
- _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
- get_witness_table 10AppIntents21IntentResultContainerVy14ContactsUICore012ContactFetchD6EntityVs5NeverOA2HGAA12ReturnsValueHPyHC.9
- get_witness_table 10AppIntents21IntentResultContainerVy14ContactsUICore018ContactAvatarFetchD6EntityVs5NeverOA2HGAA12ReturnsValueHPyHC.32
- get_witness_table 10AppIntents21IntentResultContainerVy14ContactsUICore13ContactEntityVs5NeverOA2HGAA05OpensC0HPyHC.21
- get_witness_table 10AppIntents21IntentResultContainerVy14ContactsUICore13ContactEntityVs5NeverOA2HGAA12ReturnsValueHPyHC.22
- get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA05OpensC0HPyHC.31
- get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.3
- get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.4
- objectdestroy.115Tm
CStrings:
+ "%s Cache is over capacity (%ld/%ld)"
+ "%s Caching likeness for %s (%s)"
+ "%s Couldn't find cached likeness for %s (%s"
+ "%s Found cached %s for %s"
+ "%s Removing cache entry for %s"
+ "Error unwrapping likeness data (%s): %@"
+ "Error unwrapping likeness metadata (%s): unexpectedly nil"
+ "Registered ContactEntityProvider.key"
+ "Registered ContactEntityProvider.key with intentActionPerformer"
+ "Unwrapping likeness data (%s): %ld bytes"
+ "app-intent-dependency"
- "Cache is over capacity (%ld/%ld)"
- "Caching likeness for %s (%s)"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Error unwrapping likeness metadata: unexpectedly nil"
- "Fatal error"
- "Found cached %s for %s"
- "Insufficient space allocated to copy string contents"
- "Not enough bits to represent the passed value"
- "Removing cache entry for %s"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
