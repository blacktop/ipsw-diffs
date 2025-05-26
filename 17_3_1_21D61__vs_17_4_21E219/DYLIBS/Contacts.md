## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3631.0.0.0.0
-  __TEXT.__text: 0x17f19c
-  __TEXT.__auth_stubs: 0x2e70
-  __TEXT.__objc_methlist: 0x157dc
-  __TEXT.__const: 0x1140
-  __TEXT.__gcc_except_tab: 0x26b8
-  __TEXT.__cstring: 0xd04a
-  __TEXT.__oslogstring: 0x65f7
+3632.6.0.0.0
+  __TEXT.__text: 0x180724
+  __TEXT.__auth_stubs: 0x2eb0
+  __TEXT.__objc_methlist: 0x15b4c
+  __TEXT.__const: 0x11f0
+  __TEXT.__gcc_except_tab: 0x27fc
+  __TEXT.__cstring: 0xd4ca
+  __TEXT.__oslogstring: 0x67be
   __TEXT.__dlopen_cstrs: 0x33e
   __TEXT.__ustring: 0x12
-  __TEXT.__constg_swiftt: 0xcec
-  __TEXT.__swift5_typeref: 0xb6f
+  __TEXT.__constg_swiftt: 0xcf4
+  __TEXT.__swift5_typeref: 0xba9
   __TEXT.__swift5_reflstr: 0x61f
   __TEXT.__swift5_fieldmd: 0x700
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x344
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x7a44
-  __TEXT.__eh_frame: 0x1c88
-  __TEXT.__objc_classname: 0x386e
-  __TEXT.__objc_methname: 0x2507f
-  __TEXT.__objc_methtype: 0x4558
-  __TEXT.__objc_stubs: 0x1aa20
-  __DATA_CONST.__got: 0xd58
-  __DATA_CONST.__const: 0x5a30
-  __DATA_CONST.__objc_classlist: 0xe80
+  __TEXT.__unwind_info: 0x7bdc
+  __TEXT.__eh_frame: 0x1d18
+  __TEXT.__objc_classname: 0x3959
+  __TEXT.__objc_methname: 0x25561
+  __TEXT.__objc_methtype: 0x45f4
+  __TEXT.__objc_stubs: 0x1ad20
+  __DATA_CONST.__got: 0xd70
+  __DATA_CONST.__const: 0x5a20
+  __DATA_CONST.__objc_classlist: 0xeb0
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x260
+  __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c498
-  __DATA_CONST.__objc_selrefs: 0x8208
+  __DATA_CONST.__objc_const: 0x1c958
+  __DATA_CONST.__objc_selrefs: 0x82f0
+  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_classrefs: 0x1168
+  __DATA_CONST.__objc_superrefs: 0x878
   __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__cfstring: 0xcac0
-  __AUTH_CONST.__const: 0x6170
-  __AUTH_CONST.__objc_const: 0xbe78
+  __AUTH_CONST.__cfstring: 0xcb60
+  __AUTH_CONST.__const: 0x61e0
+  __AUTH_CONST.__objc_const: 0xc100
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__auth_ptr: 0x88
-  __AUTH_CONST.__auth_got: 0x1748
+  __AUTH_CONST.__auth_got: 0x1768
   __AUTH.__data: 0x5e8
-  __AUTH.__objc_data: 0x4bc8
-  __DATA.__objc_protorefs: 0xb0
-  __DATA.__objc_classrefs: 0x1138
-  __DATA.__objc_superrefs: 0x858
-  __DATA.__objc_ivar: 0xf9c
+  __AUTH.__objc_data: 0x4c70
+  __DATA.__objc_ivar: 0xfd0
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x2bb8
-  __DATA.__bss: 0x2130
-  __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0x4f10
+  __DATA.__data: 0x2d50
+  __DATA.__bss: 0x1cb0
+  __DATA.__common: 0x50
+  __DATA_DIRTY.__objc_data: 0x5050
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x5f0
+  __DATA_DIRTY.__bss: 0xaa0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10745
-  Symbols:   30962
-  CStrings:  9590
+  Functions: 10820
+  Symbols:   31138
+  CStrings:  9690
 
Symbols:
+ +[CN(CNContainerPropertyDescription) containerProviderIdentifierDescription]
+ +[CN(CNContainerPropertyDescription) containerProviderMetadataDescription]
+ +[CNContactProviderManager isConnectionForContactProvider:]
+ +[CNContactProviderModerator log]
+ +[CNContactProviderModerator synchronizeAllUsingSession:]
+ +[CNContactProviderSession supportsSecureCoding]
+ +[CNContactStore(Favorites) isXPCDataMapperStoreForFavorites:]
+ +[CNContactStore(Spotlight) isXPCDataMapperStoreForSpotlight:]
+ +[CNContactVCardWritingAdapter descriptorForAllSupportedKeysWithOptions:]
+ +[CNContainer(Predicates_Private) predicateForContainerWithProviderIdentifier:]
+ +[CNProviderMetadata log]
+ +[CNProviderMetadata supportsSecureCoding]
+ +[CNXPCContactsSupport os_log]
+ +[CNXPCContactsSupport serviceProtocolInterface]
+ +[CNXPCContactsSupport sharedInstance]
+ +[CNiOSABContainerProviderIdentifierPredicate supportsSecureCoding]
+ +[CNiOSContactProviderDataMapper os_log]
+ -[CNAPITriageLogger request:encounteredError:].cold.1
+ -[CNContactProvider .cxx_destruct]
+ -[CNContactProvider contactStore]
+ -[CNContactProvider contactsSupport]
+ -[CNContactProvider containerIdentifier]
+ -[CNContactProvider currentSession]
+ -[CNContactProvider disableExtensionWithBundleIdentifier:completionHandler:]
+ -[CNContactProvider disableWithCompletionHandler:]
+ -[CNContactProvider enableExtensionWithBundleIdentifier:completionHandler:]
+ -[CNContactProvider enableWithCompletionHandler:]
+ -[CNContactProvider endSession]
+ -[CNContactProvider fetchExtensionCountWithError:]
+ -[CNContactProvider fetchExtensionItemsWithError:]
+ -[CNContactProvider init]
+ -[CNContactProvider isAlmond]
+ -[CNContactProvider isEnabled]
+ -[CNContactProvider isSessionRunning]
+ -[CNContactProvider lock]
+ -[CNContactProvider providerStore]
+ -[CNContactProvider requestExtensionCommand:completionHandler:]
+ -[CNContactProvider setContactsSupport:]
+ -[CNContactProvider setCurrentSession:]
+ -[CNContactProvider setIsAlmond:]
+ -[CNContactProvider setProviderStore:]
+ -[CNContactProvider startSession:]
+ -[CNContactProvider synchronizeUsingSession:completionHandler:]
+ -[CNContactProviderManager .cxx_destruct]
+ -[CNContactProviderManager clientBundleIdentifier]
+ -[CNContactProviderManager disableExtensionWithBundleIdentifier:error:]
+ -[CNContactProviderManager enableExtensionWithBundleIdentifier:error:]
+ -[CNContactProviderManager fetchExtensionCount]
+ -[CNContactProviderManager fetchExtensionItems]
+ -[CNContactProviderManager getActualBundleIdentifier:]
+ -[CNContactProviderManager initWithAuditToken:]
+ -[CNContactProviderManager initWithAuditToken:].cold.1
+ -[CNContactProviderManager isExtensionEnabledWithBundleIdentifier:]
+ -[CNContactProviderManager moderator]
+ -[CNContactProviderManager providerContainer]
+ -[CNContactProviderManager providerHost]
+ -[CNContactProviderManager requestHostExtensionCommand:error:]
+ -[CNContactProviderManager setModerator:]
+ -[CNContactProviderManager setProviderHost:]
+ -[CNContactProviderManager synchronizeUsingSession:error:]
+ -[CNContactProviderManager synchronizeUsingSession:error:].cold.1
+ -[CNContactProviderModerator .cxx_destruct]
+ -[CNContactProviderModerator cache]
+ -[CNContactProviderModerator evictPromiseForBundleIdentifier:]
+ -[CNContactProviderModerator host]
+ -[CNContactProviderModerator initWithHost:]
+ -[CNContactProviderModerator lock]
+ -[CNContactProviderModerator synchronizeUsingSession:bundleIdentifier:]
+ -[CNContactProviderModerator synchronizeUsingSession:bundleIdentifier:].cold.1
+ -[CNContactProviderSession .cxx_destruct]
+ -[CNContactProviderSession copyWithZone:]
+ -[CNContactProviderSession description]
+ -[CNContactProviderSession encodeWithCoder:]
+ -[CNContactProviderSession initWithCoder:]
+ -[CNContactProviderSession init]
+ -[CNContactProviderSession isEqual:]
+ -[CNContactProviderSession progress]
+ -[CNContactProviderSession setProgress:]
+ -[CNContactProviderSession setSynchronizationReason:]
+ -[CNContactProviderSession synchronizationReason]
+ -[CNContactStoreConfiguration isContactProvider]
+ -[CNContactStoreConfiguration setIsContactProvider:]
+ -[CNContainer initWithIdentifier:name:type:iOSLegacyIdentifier:accountIdentifier:enabled:permissions:externalIdentifier:externalModificationTag:externalSyncTag:externalSyncData:constraintsPath:meIdentifier:restrictions:guardianRestricted:lastSyncDate:providerIdentifier:providerMetadata:]
+ -[CNContainer providerIdentifier]
+ -[CNContainer providerMetadata]
+ -[CNContainerProviderIdentifierDescription CNValueForContainer:]
+ -[CNContainerProviderIdentifierDescription isWritable]
+ -[CNContainerProviderIdentifierDescription key]
+ -[CNContainerProviderIdentifierDescription setCNValue:onContainer:]
+ -[CNContainerProviderIdentifierDescription valueClass]
+ -[CNContainerProviderIdentifierDescription(iOSAB) abPropertyID]
+ -[CNContainerProviderMetadataDescription CNValueForContainer:]
+ -[CNContainerProviderMetadataDescription isWritable]
+ -[CNContainerProviderMetadataDescription key]
+ -[CNContainerProviderMetadataDescription setCNValue:onContainer:]
+ -[CNContainerProviderMetadataDescription valueClass]
+ -[CNContainerProviderMetadataDescription(iOSAB) ABValueFromCNValue:]
+ -[CNContainerProviderMetadataDescription(iOSAB) CNValueFromABValue:]
+ -[CNContainerProviderMetadataDescription(iOSAB) abPropertyID]
+ -[CNDataMapperConfiguration contactProviderManager]
+ -[CNDataMapperConfiguration isContactProvider]
+ -[CNDataMapperConfiguration setContactProviderManager:]
+ -[CNDataMapperConfiguration setIsContactProvider:]
+ -[CNDataMapperContactStore isContactProvider]
+ -[CNMockContactsLogger XPCConnectionWasInterruptedForService:]
+ -[CNMockContactsLogger XPCConnectionWasInvalidatedForService:]
+ -[CNMockContactsLogger gettingBackgroundColor:]
+ -[CNMutableContainer providerIdentifier]
+ -[CNMutableContainer providerMetadata]
+ -[CNMutableContainer setProviderIdentifier:]
+ -[CNMutableContainer setProviderMetadata:]
+ -[CNNicknameProviderTestDouble nicknameAsContactForContact:]
+ -[CNPredicate suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:].cold.2
+ -[CNProviderMetadata .cxx_destruct]
+ -[CNProviderMetadata copyWithZone:]
+ -[CNProviderMetadata dataRepresentation]
+ -[CNProviderMetadata dataRepresentation].cold.1
+ -[CNProviderMetadata encodeWithCoder:]
+ -[CNProviderMetadata initWithCoder:]
+ -[CNProviderMetadata initWithDataRepresentation:]
+ -[CNProviderMetadata initWithDataRepresentation:].cold.1
+ -[CNProviderMetadata initWithPage:syncAnchor:]
+ -[CNProviderMetadata initWithVersion:page:syncAnchor:]
+ -[CNProviderMetadata initWithVersion:page:syncAnchor:].cold.1
+ -[CNProviderMetadata isEqual:]
+ -[CNProviderMetadata pageData]
+ -[CNProviderMetadata setPageData:]
+ -[CNProviderMetadata setSyncAnchorData:]
+ -[CNProviderMetadata setVersion:]
+ -[CNProviderMetadata syncAnchorData]
+ -[CNProviderMetadata version]
+ -[CNXPCConnection .cxx_destruct]
+ -[CNXPCConnection dealloc]
+ -[CNXPCConnection initWithConnection:interface:logger:]
+ -[CNXPCConnection remoteResultForSelector:error:]
+ -[CNXPCConnection remoteResultForSelector:param1:error:]
+ -[CNXPCConnection remoteResultForSelector:param1:param2:error:]
+ -[CNXPCConnection remoteResultForSelector:parameters:error:]
+ -[CNXPCConnection serviceProxy]
+ -[CNXPCContactsSupport .cxx_destruct]
+ -[CNXPCContactsSupport initWithConnection:]
+ -[CNXPCContactsSupport init]
+ -[CNXPCContactsSupport logger]
+ -[CNXPCContactsSupport requestExtensionCommand:error:]
+ -[CNXPCContactsSupport serviceConnection]
+ -[CNXPCContactsSupport serviceProxy]
+ -[CNiOSABContainerProviderIdentifierPredicate .cxx_destruct]
+ -[CNiOSABContainerProviderIdentifierPredicate cn_copyContainersInAddressBook:error:]
+ -[CNiOSABContainerProviderIdentifierPredicate description]
+ -[CNiOSABContainerProviderIdentifierPredicate encodeWithCoder:]
+ -[CNiOSABContainerProviderIdentifierPredicate includesDisabledContainers]
+ -[CNiOSABContainerProviderIdentifierPredicate initWithCoder:]
+ -[CNiOSABContainerProviderIdentifierPredicate initWithProviderIdentifier:]
+ -[CNiOSABContainerProviderIdentifierPredicate providerIdentifier]
+ -[CNiOSContactProviderDataMapper .cxx_destruct]
+ -[CNiOSContactProviderDataMapper accountsMatchingPredicate:error:]
+ -[CNiOSContactProviderDataMapper accountsMatchingPredicate:error:].cold.1
+ -[CNiOSContactProviderDataMapper authorizedKeysForContactKeys:error:]
+ -[CNiOSContactProviderDataMapper authorizedKeysForContactKeys:error:].cold.1
+ -[CNiOSContactProviderDataMapper contactCountForFetchRequest:error:]
+ -[CNiOSContactProviderDataMapper contactCountForFetchRequest:error:].cold.1
+ -[CNiOSContactProviderDataMapper contactObservableForFetchRequest:]
+ -[CNiOSContactProviderDataMapper containersMatchingPredicate:error:]
+ -[CNiOSContactProviderDataMapper defaultContainerIdentifier]
+ -[CNiOSContactProviderDataMapper encodedContactsCursorForFetchRequest:cursorCleanupBlock:error:]
+ -[CNiOSContactProviderDataMapper executeSaveRequest:error:]
+ -[CNiOSContactProviderDataMapper executeSaveRequest:response:authorizationContext:error:]
+ -[CNiOSContactProviderDataMapper fetchContactsForFetchRequest:error:batchHandler:]
+ -[CNiOSContactProviderDataMapper fetchEncodedContactsForFetchRequest:error:cancelationToken:batchHandler:]
+ -[CNiOSContactProviderDataMapper groupsMatchingPredicate:error:]
+ -[CNiOSContactProviderDataMapper initWithConfiguration:]
+ -[CNiOSContactProviderDataMapper initWithConfiguration:addressBook:]
+ -[CNiOSContactProviderDataMapper meContactIdentifiers:]
+ -[CNiOSContactProviderDataMapper meContactIdentifiers:].cold.1
+ -[CNiOSContactProviderDataMapper policyForContainerWithIdentifier:error:]
+ -[CNiOSContactProviderDataMapper policyWithDescription:error:]
+ -[CNiOSContactProviderDataMapper requestAccessForEntityType:completionHandler:]
+ -[CNiOSContactProviderDataMapper requestAccessForEntityType:error:]
+ -[CNiOSContactProviderDataMapper serverSearchContainersMatchingPredicate:error:]
+ -[CNiOSContactProviderDataMapper serverSearchContainersMatchingPredicate:error:].cold.1
+ -[CNiOSContactProviderDataMapper shouldLogContactsAccess]
+ -[CNiOSContactProviderDataMapper subgroupsOfGroupWithIdentifier:error:]
+ -[CNiOSContactProviderDataMapper subgroupsOfGroupWithIdentifier:error:].cold.1
+ -[CNiOSContactProviderDataMapper updateManagedConfiguration]
+ -[_CNContactsLogger XPCConnectionWasInterruptedForService:]
+ -[_CNContactsLogger XPCConnectionWasInterruptedForService:].cold.1
+ -[_CNContactsLogger XPCConnectionWasInvalidatedForService:]
+ GCC_except_table29
+ GCC_except_table54
+ OBJC_IVAR_$_CNContainer._providerIdentifier
+ OBJC_IVAR_$_CNContainer._providerMetadata
+ _ABAddressBookCopySourceWithProviderIdentifier
+ _CNContactProviderSynchronizationReasonAppContainerHasChanges
+ _CNContactProviderSynchronizationReasonAppRequested
+ _CNContactProviderSynchronizationReasonExtensionWasEnabled
+ _CNContactProviderSynchronizationReasonScheduledEvent
+ _CNContactsSupportServiceName
+ _CNContainerProviderIdentifierKey
+ _CNContainerProviderMetadataKey
+ _CNDataMapperContactProviderServiceName
+ _CNWatchdogEventSuggestionsTimeout
+ _OBJC_CLASS_$_CNContactProvider
+ _OBJC_CLASS_$_CNContactProviderManager
+ _OBJC_CLASS_$_CNContactProviderModerator
+ _OBJC_CLASS_$_CNContactProviderSession
+ _OBJC_CLASS_$_CNContainerProviderIdentifierDescription
+ _OBJC_CLASS_$_CNContainerProviderMetadataDescription
+ _OBJC_CLASS_$_CNProviderMetadata
+ _OBJC_CLASS_$_CNXPCConnection
+ _OBJC_CLASS_$_CNXPCContactsSupport
+ _OBJC_CLASS_$_CNiOSABContainerProviderIdentifierPredicate
+ _OBJC_CLASS_$_CNiOSContactProviderDataMapper
+ _OBJC_CLASS_$__TtC8Contacts21CNContactProviderHost
+ _OBJC_CLASS_$__TtC8Contacts22CNContactProviderCache
+ _OBJC_IVAR_$_CNContactProvider._contactsSupport
+ _OBJC_IVAR_$_CNContactProvider._currentSession
+ _OBJC_IVAR_$_CNContactProvider._isAlmond
+ _OBJC_IVAR_$_CNContactProvider._lock
+ _OBJC_IVAR_$_CNContactProvider._providerStore
+ _OBJC_IVAR_$_CNContactProviderManager._clientBundleIdentifier
+ _OBJC_IVAR_$_CNContactProviderManager._moderator
+ _OBJC_IVAR_$_CNContactProviderManager._providerHost
+ _OBJC_IVAR_$_CNContactProviderModerator._cache
+ _OBJC_IVAR_$_CNContactProviderModerator._host
+ _OBJC_IVAR_$_CNContactProviderModerator._lock
+ _OBJC_IVAR_$_CNContactProviderSession._progress
+ _OBJC_IVAR_$_CNContactProviderSession._synchronizationReason
+ _OBJC_IVAR_$_CNContactStoreConfiguration._isContactProvider
+ _OBJC_IVAR_$_CNDataMapperConfiguration._contactProviderManager
+ _OBJC_IVAR_$_CNDataMapperConfiguration._isContactProvider
+ _OBJC_IVAR_$_CNDataMapperContactStore._isContactProvider
+ _OBJC_IVAR_$_CNProviderMetadata._pageData
+ _OBJC_IVAR_$_CNProviderMetadata._syncAnchorData
+ _OBJC_IVAR_$_CNProviderMetadata._version
+ _OBJC_IVAR_$_CNXPCConnection._connection
+ _OBJC_IVAR_$_CNXPCConnection._logger
+ _OBJC_IVAR_$_CNXPCConnection._serviceProxy
+ _OBJC_IVAR_$_CNXPCContactsSupport._logger
+ _OBJC_IVAR_$_CNXPCContactsSupport._serviceConnection
+ _OBJC_IVAR_$_CNXPCContactsSupport._serviceProxy
+ _OBJC_IVAR_$_CNXPCDataMapper._serviceConnection
+ _OBJC_IVAR_$_CNiOSABContainerProviderIdentifierPredicate._providerIdentifier
+ _OBJC_IVAR_$_CNiOSContactProviderDataMapper._contactProviderManager
+ _OBJC_IVAR_$_CNiOSContactProviderDataMapper._dataMapper
+ _OBJC_IVAR_$_CNiOSContactProviderDataMapper._managedConfiguration
+ _OBJC_METACLASS_$_CNContactProvider
+ _OBJC_METACLASS_$_CNContactProviderManager
+ _OBJC_METACLASS_$_CNContactProviderModerator
+ _OBJC_METACLASS_$_CNContactProviderSession
+ _OBJC_METACLASS_$_CNContainerProviderIdentifierDescription
+ _OBJC_METACLASS_$_CNContainerProviderMetadataDescription
+ _OBJC_METACLASS_$_CNProviderMetadata
+ _OBJC_METACLASS_$_CNXPCConnection
+ _OBJC_METACLASS_$_CNXPCContactsSupport
+ _OBJC_METACLASS_$_CNiOSABContainerProviderIdentifierPredicate
+ _OBJC_METACLASS_$_CNiOSContactProviderDataMapper
+ _OBJC_METACLASS_$__TtC8Contacts21CNContactProviderHost
+ _OBJC_METACLASS_$__TtC8Contacts22CNContactProviderCache
+ _SGErrorDomain
+ __CLASS_PROPERTIES__TtC8Contacts22CNContactProviderCache
+ __DATA__TtC8Contacts21CNContactProviderHost
+ __DATA__TtC8Contacts22CNContactProviderCache
+ __INSTANCE_METHODS__TtCV8Contacts40_CNContactProviderExtensionConfiguration14ExportedObject
+ __IVARS__TtC8Contacts21CNContactProviderHost
+ __IVARS__TtC8Contacts22CNContactProviderCache
+ __IVARS__TtCV8Contacts40_CNContactProviderExtensionConfiguration14ExportedObject
+ __METACLASS_DATA__TtC8Contacts21CNContactProviderHost
+ __METACLASS_DATA__TtC8Contacts22CNContactProviderCache
+ __OBJC_$_CLASS_METHODS_CNContactProviderManager
+ __OBJC_$_CLASS_METHODS_CNContactProviderModerator
+ __OBJC_$_CLASS_METHODS_CNContactProviderSession
+ __OBJC_$_CLASS_METHODS_CNProviderMetadata
+ __OBJC_$_CLASS_METHODS_CNXPCContactsSupport
+ __OBJC_$_CLASS_METHODS_CNiOSABContainerProviderIdentifierPredicate
+ __OBJC_$_CLASS_METHODS__TtC8Contacts22CNContactProviderCache
+ __OBJC_$_CLASS_PROP_LIST_CNContactProviderModerator
+ __OBJC_$_CLASS_PROP_LIST_CNContactProviderSession
+ __OBJC_$_CLASS_PROP_LIST_CNProviderMetadata
+ __OBJC_$_INSTANCE_METHODS_CNContactProvider
+ __OBJC_$_INSTANCE_METHODS_CNContactProviderManager
+ __OBJC_$_INSTANCE_METHODS_CNContactProviderModerator
+ __OBJC_$_INSTANCE_METHODS_CNContactProviderSession
+ __OBJC_$_INSTANCE_METHODS_CNContainerProviderIdentifierDescription(iOSAB)
+ __OBJC_$_INSTANCE_METHODS_CNContainerProviderMetadataDescription(iOSAB)
+ __OBJC_$_INSTANCE_METHODS_CNProviderMetadata
+ __OBJC_$_INSTANCE_METHODS_CNXPCConnection
+ __OBJC_$_INSTANCE_METHODS_CNXPCContactsSupport
+ __OBJC_$_INSTANCE_METHODS_CNiOSABContainerProviderIdentifierPredicate
+ __OBJC_$_INSTANCE_METHODS_CNiOSContactProviderDataMapper
+ __OBJC_$_INSTANCE_METHODS__TtC8Contacts21CNContactProviderHost
+ __OBJC_$_INSTANCE_METHODS__TtC8Contacts22CNContactProviderCache
+ __OBJC_$_INSTANCE_VARIABLES_CNContactProvider
+ __OBJC_$_INSTANCE_VARIABLES_CNContactProviderManager
+ __OBJC_$_INSTANCE_VARIABLES_CNContactProviderModerator
+ __OBJC_$_INSTANCE_VARIABLES_CNContactProviderSession
+ __OBJC_$_INSTANCE_VARIABLES_CNProviderMetadata
+ __OBJC_$_INSTANCE_VARIABLES_CNXPCConnection
+ __OBJC_$_INSTANCE_VARIABLES_CNXPCContactsSupport
+ __OBJC_$_INSTANCE_VARIABLES_CNiOSABContainerProviderIdentifierPredicate
+ __OBJC_$_INSTANCE_VARIABLES_CNiOSContactProviderDataMapper
+ __OBJC_$_PROP_LIST_CNContactProvider
+ __OBJC_$_PROP_LIST_CNContactProviderManager
+ __OBJC_$_PROP_LIST_CNContactProviderModerator
+ __OBJC_$_PROP_LIST_CNContactProviderSession
+ __OBJC_$_PROP_LIST_CNContactsLoggerProvider.98
+ __OBJC_$_PROP_LIST_CNKeyboardStateMonitor.85
+ __OBJC_$_PROP_LIST_CNProviderMetadata
+ __OBJC_$_PROP_LIST_CNXPCConnection
+ __OBJC_$_PROP_LIST_CNXPCContactsSupport
+ __OBJC_$_PROP_LIST_CNiOSABContainerProviderIdentifierPredicate
+ __OBJC_$_PROP_LIST_CNiOSContactProviderDataMapper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CNXPCContactsSupportProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CNXPCContactsSupportService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNXPCContactsSupportProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNXPCContactsSupportService
+ __OBJC_$_PROTOCOL_REFS_CNXPCContactsSupportProtocol
+ __OBJC_$_PROTOCOL_REFS_CNXPCContactsSupportService
+ __OBJC_CLASS_PROTOCOLS_$_CNContactProviderSession
+ __OBJC_CLASS_PROTOCOLS_$_CNProviderMetadata
+ __OBJC_CLASS_PROTOCOLS_$_CNXPCContactsSupport
+ __OBJC_CLASS_PROTOCOLS_$_CNiOSABContainerProviderIdentifierPredicate
+ __OBJC_CLASS_PROTOCOLS_$_CNiOSContactProviderDataMapper
+ __OBJC_CLASS_RO_$_CNContactProvider
+ __OBJC_CLASS_RO_$_CNContactProviderManager
+ __OBJC_CLASS_RO_$_CNContactProviderModerator
+ __OBJC_CLASS_RO_$_CNContactProviderSession
+ __OBJC_CLASS_RO_$_CNContainerProviderIdentifierDescription
+ __OBJC_CLASS_RO_$_CNContainerProviderMetadataDescription
+ __OBJC_CLASS_RO_$_CNProviderMetadata
+ __OBJC_CLASS_RO_$_CNXPCConnection
+ __OBJC_CLASS_RO_$_CNXPCContactsSupport
+ __OBJC_CLASS_RO_$_CNiOSABContainerProviderIdentifierPredicate
+ __OBJC_CLASS_RO_$_CNiOSContactProviderDataMapper
+ __OBJC_LABEL_PROTOCOL_$_CNXPCContactsSupportProtocol
+ __OBJC_LABEL_PROTOCOL_$_CNXPCContactsSupportService
+ __OBJC_METACLASS_RO_$_CNContactProvider
+ __OBJC_METACLASS_RO_$_CNContactProviderManager
+ __OBJC_METACLASS_RO_$_CNContactProviderModerator
+ __OBJC_METACLASS_RO_$_CNContactProviderSession
+ __OBJC_METACLASS_RO_$_CNContainerProviderIdentifierDescription
+ __OBJC_METACLASS_RO_$_CNContainerProviderMetadataDescription
+ __OBJC_METACLASS_RO_$_CNProviderMetadata
+ __OBJC_METACLASS_RO_$_CNXPCConnection
+ __OBJC_METACLASS_RO_$_CNXPCContactsSupport
+ __OBJC_METACLASS_RO_$_CNiOSABContainerProviderIdentifierPredicate
+ __OBJC_METACLASS_RO_$_CNiOSContactProviderDataMapper
+ __OBJC_PROTOCOL_$_CNXPCContactsSupportProtocol
+ __OBJC_PROTOCOL_$_CNXPCContactsSupportService
+ __OBJC_PROTOCOL_REFERENCE_$_CNXPCContactsSupportService
+ __PROPERTIES__TtC8Contacts22CNContactProviderCache
+ __PROTOCOLS__TtCV8Contacts40_CNContactProviderExtensionConfiguration14ExportedObject
+ __PROTOCOLS__TtCV8Contacts40_CNContactProviderExtensionConfiguration14ExportedObject.1
+ __PROTOCOL_INSTANCE_METHODS__TtP8Contacts37CNContactProviderExtensionXPCProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP8Contacts37CNContactProviderExtensionXPCProtocol_
+ __PROTOCOL__TtP8Contacts37CNContactProviderExtensionXPCProtocol_
+ ___25+[CNProviderMetadata log]_block_invoke
+ ___30+[CNXPCContactsSupport os_log]_block_invoke
+ ___31-[CNContactProvider endSession]_block_invoke
+ ___33+[CNContactProviderModerator log]_block_invoke
+ ___34-[CNContactProvider startSession:]_block_invoke
+ ___37-[CNContactProvider isSessionRunning]_block_invoke
+ ___38+[CNXPCContactsSupport sharedInstance]_block_invoke
+ ___40+[CNiOSContactProviderDataMapper os_log]_block_invoke
+ ___47-[CNContactProviderManager initWithAuditToken:]_block_invoke
+ ___50-[CNContactStore(Spotlight) verifyIndexWithError:]_block_invoke.17
+ ___50-[CNContactStore(Spotlight) verifyIndexWithError:]_block_invoke.cold.1
+ ___54-[CNXPCContactsSupport requestExtensionCommand:error:]_block_invoke
+ ___55-[CNXPCConnection initWithConnection:interface:logger:]_block_invoke
+ ___55-[CNXPCConnection initWithConnection:interface:logger:]_block_invoke_2
+ ___55-[CNXPCConnection initWithConnection:interface:logger:]_block_invoke_3
+ ___57+[CNContactProviderModerator synchronizeAllUsingSession:]_block_invoke
+ ___60-[CNXPCConnection remoteResultForSelector:parameters:error:]_block_invoke
+ ___62-[CNContactProviderModerator evictPromiseForBundleIdentifier:]_block_invoke
+ ___63-[CNContactProvider requestExtensionCommand:completionHandler:]_block_invoke
+ ___63-[CNContactProvider synchronizeUsingSession:completionHandler:]_block_invoke
+ ___67-[CNContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:]_block_invoke.15
+ ___67-[CNContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:]_block_invoke.cold.1
+ ___71-[CNContactProviderModerator synchronizeUsingSession:bundleIdentifier:]_block_invoke
+ ___71-[CNContactProviderModerator synchronizeUsingSession:bundleIdentifier:]_block_invoke.5
+ ___71-[CNContactProviderModerator synchronizeUsingSession:bundleIdentifier:]_block_invoke.7
+ ___71-[CNContactProviderModerator synchronizeUsingSession:bundleIdentifier:]_block_invoke.7.cold.1
+ ___74+[CN(CNContainerPropertyDescription) containerProviderMetadataDescription]_block_invoke
+ ___76+[CN(CNContainerPropertyDescription) containerProviderIdentifierDescription]_block_invoke
+ ___98-[CNPredicate(Suggested) suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:]_block_invoke.107
+ ___98-[CNPredicate(Suggested) suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:]_block_invoke.91
+ ___98-[CNPredicate(Suggested) suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:]_block_invoke.cold.1
+ ___block_descriptor_64_e8_32s40s48s56w_e17_v16?0"NSError"8ls32l8s40l8s48l8w56l8
+ ___block_descriptor_64_e8_32s40s48s56w_e8_v16?08ls32l8s40l8s48l8w56l8
+ ___block_literal_global.111
+ ___block_literal_global.146
+ ___block_literal_global.149
+ ___block_literal_global.153
+ ___block_literal_global.155
+ ___block_literal_global.158
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.171
+ ___block_literal_global.177
+ ___block_literal_global.181
+ ___block_literal_global.184
+ ___block_literal_global.187
+ ___block_literal_global.190
+ ___block_literal_global.193
+ ___block_literal_global.196
+ ___block_literal_global.199
+ ___block_literal_global.202
+ ___block_literal_global.205
+ ___block_literal_global.208
+ ___block_literal_global.211
+ ___block_literal_global.214
+ ___block_literal_global.217
+ ___block_literal_global.226
+ ___block_literal_global.229
+ ___block_literal_global.232
+ ___block_literal_global.235
+ ___block_literal_global.238
+ ___block_literal_global.241
+ ___block_literal_global.244
+ ___block_literal_global.247
+ ___block_literal_global.250
+ ___block_literal_global.253
+ ___block_literal_global.256
+ ___block_literal_global.259
+ ___block_literal_global.262
+ ___block_literal_global.265
+ ___block_literal_global.268
+ ___block_literal_global.271
+ ___block_literal_global.274
+ ___block_literal_global.277
+ ___block_literal_global.280
+ ___block_literal_global.283
+ ___block_literal_global.286
+ ___block_literal_global.289
+ ___block_literal_global.292
+ ___block_literal_global.295
+ ___block_literal_global.298
+ ___block_literal_global.301
+ ___block_literal_global.307
+ ___block_literal_global.310
+ ___block_literal_global.313
+ ___block_literal_global.319
+ ___block_literal_global.322
+ ___block_literal_global.325
+ ___block_literal_global.328
+ ___block_literal_global.331
+ ___block_literal_global.334
+ ___block_literal_global.337
+ ___block_literal_global.340
+ ___block_literal_global.343
+ ___block_literal_global.346
+ ___block_literal_global.349
+ ___block_literal_global.353
+ ___block_literal_global.355
+ ___block_literal_global.358
+ ___block_literal_global.361
+ ___block_literal_global.364
+ ___block_literal_global.367
+ ___block_literal_global.370
+ ___block_literal_global.373
+ ___block_literal_global.376
+ ___block_literal_global.379
+ ___block_literal_global.382
+ ___block_literal_global.385
+ ___block_literal_global.388
+ ___block_literal_global.391
+ ___block_literal_global.394
+ ___block_literal_global.402
+ ___block_literal_global.406
+ ___block_literal_global.518
+ ___block_literal_global.61
+ ___block_literal_global.618
+ ___block_literal_global.620
+ ___block_literal_global.637
+ ___block_literal_global.650
+ ___block_literal_global.674
+ ___block_literal_global.703
+ ___block_literal_global.709
+ ___block_literal_global.714
+ ___block_literal_global.746
+ ___block_literal_global.765
+ ___block_literal_global.808
+ ___block_literal_global.823
+ ___block_literal_global.837
+ __unnamed_array_storage.32
+ __unnamed_array_storage.57
+ _allContainerProperties.cn_once_object_19
+ _allContainerProperties.cn_once_token_19
+ _block_copy_helper.57
+ _block_copy_helper.63
+ _block_descriptor.59
+ _block_descriptor.65
+ _block_destroy_helper.58
+ _block_destroy_helper.64
+ _containerProviderIdentifierDescription.cn_once_object_17
+ _containerProviderIdentifierDescription.cn_once_token_17
+ _containerProviderMetadataDescription.cn_once_object_18
+ _containerProviderMetadataDescription.cn_once_token_18
+ _get_witness_table 8Contacts26CNContactProviderExtensionRzlAA01_bcD13ConfigurationVyxG0D10Foundation03AppdE0HPyHC.2
+ _kABSourceProviderIdentifierProperty
+ _kABSourceProviderMetadataProperty
+ _objc_msgSend$XPCConnectionWasInterruptedForService:
+ _objc_msgSend$XPCConnectionWasInvalidatedForService:
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$contactProviderManager
+ _objc_msgSend$contactsSupport
+ _objc_msgSend$containerProviderIdentifierDescription
+ _objc_msgSend$containerProviderMetadataDescription
+ _objc_msgSend$descriptorForAllSupportedKeysWithOptions:
+ _objc_msgSend$evictPromiseForBundleIdentifier:
+ _objc_msgSend$includePronouns
+ _objc_msgSend$initWithConnection:
+ _objc_msgSend$initWithConnection:interface:logger:
+ _objc_msgSend$initWithIdentifier:name:type:iOSLegacyIdentifier:accountIdentifier:enabled:permissions:externalIdentifier:externalModificationTag:externalSyncTag:externalSyncData:constraintsPath:meIdentifier:restrictions:guardianRestricted:lastSyncDate:providerIdentifier:providerMetadata:
+ _objc_msgSend$initWithProviderIdentifier:
+ _objc_msgSend$initWithVersion:page:syncAnchor:
+ _objc_msgSend$isContactProvider
+ _objc_msgSend$isXPCDataMapperStoreForFavorites:
+ _objc_msgSend$isXPCDataMapperStoreForSpotlight:
+ _objc_msgSend$pageData
+ _objc_msgSend$providerIdentifier
+ _objc_msgSend$providerMetadata
+ _objc_msgSend$recordExceptionForEvent:
+ _objc_msgSend$remoteResultForSelector:error:
+ _objc_msgSend$remoteResultForSelector:param1:error:
+ _objc_msgSend$remoteResultForSelector:param1:param2:error:
+ _objc_msgSend$remoteResultForSelector:parameters:error:
+ _objc_msgSend$serviceConnection
+ _objc_msgSend$serviceProxy
+ _objc_msgSend$setIsContactProvider:
+ _objc_msgSend$setPageData:
+ _objc_msgSend$setProviderIdentifier:
+ _objc_msgSend$setProviderMetadata:
+ _objc_msgSend$setSyncAnchorData:
+ _objc_msgSend$setSyncTimeout:
+ _objc_msgSend$setVersion:
+ _objc_msgSend$statusForEvent:
+ _objc_msgSend$syncAnchorData
+ _objc_msgSend$watchdog
+ _sharedInstance.cn_once_object_3
+ _sharedInstance.cn_once_token_3
+ _suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:.cn_once_object_6
+ _suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:.cn_once_token_6
+ _swift_unknownObjectRetain_n
+ _symbolic $s8Contacts26CNContactProviderExtensionP
+ _symbolic $s8Contacts37CNContactProviderExtensionXPCProtocolP
+ _symbolic 8Contacts37CNContactProviderExtensionXPCProtocol_p
+ _symbolic SaySo11CNContainerCG
+ _symbolic SaySo15CNKeyDescriptor_pG
+ _symbolic So24CNContactProviderSessionC
+ _symbolic _____ 8Contacts21CNContactProviderHostC
+ _symbolic _____ 8Contacts22CNContactProviderCacheC
+ _symbolic _____ 8Contacts31CNContactProviderExtensionPointO
+ _symbolic _____ 8Contacts40_CNContactProviderExtensionConfigurationV
+ _symbolic _____ 8Contacts40_CNContactProviderExtensionConfigurationV14ExportedObjectC
+ _symbolic _____y_____G s15CollectionOfOneV 19ExtensionFoundation04_AppD8IdentityV
+ _symbolic _____yxG 8Contacts40_CNContactProviderExtensionConfigurationV
+ _symbolic _____yx_G 8Contacts40_CNContactProviderExtensionConfigurationV14ExportedObjectC
+ _writableContainerProperties.cn_once_object_20
+ _writableContainerProperties.cn_once_token_20
- +[CNContactStore(Favorites) isXPCDataMapperStore:]
- +[CNContactStore(Spotlight) isXPCDataMapperStore:]
- +[CNContactVCardWritingAdapter descriptorForAllSupportedKeys]
- +[CNContactsProviderDataMapper os_log]
- +[CNContactsProviderManager isConnectionForContactsProvider:]
- +[CNContactsProviderModerator log]
- +[CNContactsProviderModerator synchronizeAllUsingSession:]
- +[CNContactsProviderSession supportsSecureCoding]
- -[CNAggregateContactStore requestExtensionCommand:error:]
- -[CNContactStore requestExtensionCommand:error:]
- -[CNContactStore(Spotlight) synchronousRemoteObjectProxyForContactsXPCService]
- -[CNContactStoreConfiguration isContactsProvider]
- -[CNContactStoreConfiguration setIsContactsProvider:]
- -[CNContactsProvider .cxx_destruct]
- -[CNContactsProvider contactStore]
- -[CNContactsProvider containerIdentifier]
- -[CNContactsProvider currentSession]
- -[CNContactsProvider disableExtensionWithBundleIdentifier:completionHandler:]
- -[CNContactsProvider disableWithCompletionHandler:]
- -[CNContactsProvider enableExtensionWithBundleIdentifier:completionHandler:]
- -[CNContactsProvider enableWithCompletionHandler:]
- -[CNContactsProvider endSession]
- -[CNContactsProvider fetchExtensionCountWithError:]
- -[CNContactsProvider fetchExtensionItemsWithError:]
- -[CNContactsProvider init]
- -[CNContactsProvider isAlmond]
- -[CNContactsProvider isEnabled]
- -[CNContactsProvider isSessionRunning]
- -[CNContactsProvider lock]
- -[CNContactsProvider providerStore]
- -[CNContactsProvider requestExtensionCommand:completionHandler:]
- -[CNContactsProvider setCurrentSession:]
- -[CNContactsProvider setIsAlmond:]
- -[CNContactsProvider setProviderStore:]
- -[CNContactsProvider startSession:]
- -[CNContactsProvider synchronizeUsingSession:completionHandler:]
- -[CNContactsProviderDataMapper .cxx_destruct]
- -[CNContactsProviderDataMapper accountsMatchingPredicate:error:]
- -[CNContactsProviderDataMapper accountsMatchingPredicate:error:].cold.1
- -[CNContactsProviderDataMapper authorizedKeysForContactKeys:error:]
- -[CNContactsProviderDataMapper authorizedKeysForContactKeys:error:].cold.1
- -[CNContactsProviderDataMapper contactCountForFetchRequest:error:]
- -[CNContactsProviderDataMapper contactCountForFetchRequest:error:].cold.1
- -[CNContactsProviderDataMapper contactObservableForFetchRequest:]
- -[CNContactsProviderDataMapper containersMatchingPredicate:error:]
- -[CNContactsProviderDataMapper defaultContainerIdentifier]
- -[CNContactsProviderDataMapper encodedContactsCursorForFetchRequest:cursorCleanupBlock:error:]
- -[CNContactsProviderDataMapper executeSaveRequest:error:]
- -[CNContactsProviderDataMapper executeSaveRequest:response:authorizationContext:error:]
- -[CNContactsProviderDataMapper fetchContactsForFetchRequest:error:batchHandler:]
- -[CNContactsProviderDataMapper fetchEncodedContactsForFetchRequest:error:cancelationToken:batchHandler:]
- -[CNContactsProviderDataMapper groupsMatchingPredicate:error:]
- -[CNContactsProviderDataMapper initWithConfiguration:]
- -[CNContactsProviderDataMapper initWithConfiguration:addressBook:]
- -[CNContactsProviderDataMapper meContactIdentifiers:]
- -[CNContactsProviderDataMapper meContactIdentifiers:].cold.1
- -[CNContactsProviderDataMapper policyForContainerWithIdentifier:error:]
- -[CNContactsProviderDataMapper policyWithDescription:error:]
- -[CNContactsProviderDataMapper requestAccessForEntityType:completionHandler:]
- -[CNContactsProviderDataMapper requestAccessForEntityType:error:]
- -[CNContactsProviderDataMapper serverSearchContainersMatchingPredicate:error:]
- -[CNContactsProviderDataMapper serverSearchContainersMatchingPredicate:error:].cold.1
- -[CNContactsProviderDataMapper shouldLogContactsAccess]
- -[CNContactsProviderDataMapper subgroupsOfGroupWithIdentifier:error:]
- -[CNContactsProviderDataMapper subgroupsOfGroupWithIdentifier:error:].cold.1
- -[CNContactsProviderDataMapper updateManagedConfiguration]
- -[CNContactsProviderManager .cxx_destruct]
- -[CNContactsProviderManager clientBundleIdentifier]
- -[CNContactsProviderManager disableExtensionWithBundleIdentifier:error:]
- -[CNContactsProviderManager enableExtensionWithBundleIdentifier:error:]
- -[CNContactsProviderManager fetchExtensionCount]
- -[CNContactsProviderManager fetchExtensionItems]
- -[CNContactsProviderManager getActualBundleIdentifier:]
- -[CNContactsProviderManager initWithAuditToken:]
- -[CNContactsProviderManager initWithAuditToken:].cold.1
- -[CNContactsProviderManager isExtensionEnabledWithBundleIdentifier:]
- -[CNContactsProviderManager moderator]
- -[CNContactsProviderManager providerContainer]
- -[CNContactsProviderManager providerHost]
- -[CNContactsProviderManager requestHostExtensionCommand:error:]
- -[CNContactsProviderManager setModerator:]
- -[CNContactsProviderManager setProviderHost:]
- -[CNContactsProviderManager synchronizeUsingSession:error:]
- -[CNContactsProviderManager synchronizeUsingSession:error:].cold.1
- -[CNContactsProviderModerator .cxx_destruct]
- -[CNContactsProviderModerator cache]
- -[CNContactsProviderModerator host]
- -[CNContactsProviderModerator initWithHost:]
- -[CNContactsProviderModerator lock]
- -[CNContactsProviderModerator synchronizeUsingSession:bundleIdentifier:]
- -[CNContactsProviderSession .cxx_destruct]
- -[CNContactsProviderSession copyWithZone:]
- -[CNContactsProviderSession description]
- -[CNContactsProviderSession encodeWithCoder:]
- -[CNContactsProviderSession initWithCoder:]
- -[CNContactsProviderSession init]
- -[CNContactsProviderSession isEqual:]
- -[CNContactsProviderSession progress]
- -[CNContactsProviderSession setProgress:]
- -[CNContactsProviderSession setSynchronizationReason:]
- -[CNContactsProviderSession synchronizationReason]
- -[CNContainer initWithIdentifier:name:type:iOSLegacyIdentifier:accountIdentifier:enabled:permissions:externalIdentifier:externalModificationTag:externalSyncTag:externalSyncData:constraintsPath:meIdentifier:restrictions:guardianRestricted:lastSyncDate:]
- -[CNDataMapperConfiguration contactsProviderManager]
- -[CNDataMapperConfiguration isContactsProvider]
- -[CNDataMapperConfiguration setContactsProviderManager:]
- -[CNDataMapperConfiguration setIsContactsProvider:]
- -[CNDataMapperContactStore isContactsProvider]
- -[CNDataMapperContactStore requestExtensionCommand:error:]
- -[CNMockContactsLogger XPCConnectionWasInterrupted]
- -[CNMockContactsLogger XPCConnectionWasInvalidated]
- -[CNXPCDataMapper dealloc]
- -[CNXPCDataMapper remoteResultForSelector:error:]
- -[CNXPCDataMapper remoteResultForSelector:parameters:error:]
- -[CNXPCDataMapper remoteResultForSelector:query:error:]
- -[CNXPCDataMapper remoteResultForSelector:query:queryParameter:error:]
- -[CNXPCDataMapper requestExtensionCommand:error:]
- -[_CNContactsLogger XPCConnectionWasInterrupted]
- -[_CNContactsLogger XPCConnectionWasInterrupted].cold.1
- -[_CNContactsLogger XPCConnectionWasInvalidated]
- GCC_except_table110
- GCC_except_table47
- GCC_except_table65
- _CNContactsProviderSynchronizationReasonAppContainerHasChanges
- _CNContactsProviderSynchronizationReasonAppRequested
- _CNContactsProviderSynchronizationReasonExtensionWasEnabled
- _CNContactsProviderSynchronizationReasonScheduledEvent
- _CNDataMapperContactsProviderServiceName
- _OBJC_CLASS_$_CNContactsProvider
- _OBJC_CLASS_$_CNContactsProviderDataMapper
- _OBJC_CLASS_$_CNContactsProviderManager
- _OBJC_CLASS_$_CNContactsProviderModerator
- _OBJC_CLASS_$_CNContactsProviderSession
- _OBJC_CLASS_$__TtC8Contacts22CNContactsProviderHost
- _OBJC_CLASS_$__TtC8Contacts23CNContactsProviderCache
- _OBJC_IVAR_$_CNContactStoreConfiguration._isContactsProvider
- _OBJC_IVAR_$_CNContactsProvider._currentSession
- _OBJC_IVAR_$_CNContactsProvider._isAlmond
- _OBJC_IVAR_$_CNContactsProvider._lock
- _OBJC_IVAR_$_CNContactsProvider._providerStore
- _OBJC_IVAR_$_CNContactsProviderDataMapper._contactsProviderManager
- _OBJC_IVAR_$_CNContactsProviderDataMapper._dataMapper
- _OBJC_IVAR_$_CNContactsProviderDataMapper._managedConfiguration
- _OBJC_IVAR_$_CNContactsProviderManager._clientBundleIdentifier
- _OBJC_IVAR_$_CNContactsProviderManager._moderator
- _OBJC_IVAR_$_CNContactsProviderManager._providerHost
- _OBJC_IVAR_$_CNContactsProviderModerator._cache
- _OBJC_IVAR_$_CNContactsProviderModerator._host
- _OBJC_IVAR_$_CNContactsProviderModerator._lock
- _OBJC_IVAR_$_CNContactsProviderSession._progress
- _OBJC_IVAR_$_CNContactsProviderSession._synchronizationReason
- _OBJC_IVAR_$_CNDataMapperConfiguration._contactsProviderManager
- _OBJC_IVAR_$_CNDataMapperConfiguration._isContactsProvider
- _OBJC_IVAR_$_CNDataMapperContactStore._isContactsProvider
- _OBJC_IVAR_$_CNXPCDataMapper._connection
- _OBJC_METACLASS_$_CNContactsProvider
- _OBJC_METACLASS_$_CNContactsProviderDataMapper
- _OBJC_METACLASS_$_CNContactsProviderManager
- _OBJC_METACLASS_$_CNContactsProviderModerator
- _OBJC_METACLASS_$_CNContactsProviderSession
- _OBJC_METACLASS_$__TtC8Contacts22CNContactsProviderHost
- _OBJC_METACLASS_$__TtC8Contacts23CNContactsProviderCache
- __CLASS_PROPERTIES__TtC8Contacts23CNContactsProviderCache
- __DATA__TtC8Contacts22CNContactsProviderHost
- __DATA__TtC8Contacts23CNContactsProviderCache
- __INSTANCE_METHODS__TtCV8Contacts41_CNContactsProviderExtensionConfiguration14ExportedObject
- __IVARS__TtC8Contacts22CNContactsProviderHost
- __IVARS__TtC8Contacts23CNContactsProviderCache
- __IVARS__TtCV8Contacts41_CNContactsProviderExtensionConfiguration14ExportedObject
- __METACLASS_DATA__TtC8Contacts22CNContactsProviderHost
- __METACLASS_DATA__TtC8Contacts23CNContactsProviderCache
- __OBJC_$_CLASS_METHODS_CNContactsProviderManager
- __OBJC_$_CLASS_METHODS_CNContactsProviderModerator
- __OBJC_$_CLASS_METHODS_CNContactsProviderSession
- __OBJC_$_CLASS_METHODS__TtC8Contacts23CNContactsProviderCache
- __OBJC_$_CLASS_PROP_LIST_CNContactsProviderModerator
- __OBJC_$_CLASS_PROP_LIST_CNContactsProviderSession
- __OBJC_$_INSTANCE_METHODS_CNContactsProvider
- __OBJC_$_INSTANCE_METHODS_CNContactsProviderDataMapper
- __OBJC_$_INSTANCE_METHODS_CNContactsProviderManager
- __OBJC_$_INSTANCE_METHODS_CNContactsProviderModerator
- __OBJC_$_INSTANCE_METHODS_CNContactsProviderSession
- __OBJC_$_INSTANCE_METHODS__TtC8Contacts22CNContactsProviderHost
- __OBJC_$_INSTANCE_METHODS__TtC8Contacts23CNContactsProviderCache
- __OBJC_$_INSTANCE_VARIABLES_CNContactsProvider
- __OBJC_$_INSTANCE_VARIABLES_CNContactsProviderDataMapper
- __OBJC_$_INSTANCE_VARIABLES_CNContactsProviderManager
- __OBJC_$_INSTANCE_VARIABLES_CNContactsProviderModerator
- __OBJC_$_INSTANCE_VARIABLES_CNContactsProviderSession
- __OBJC_$_PROP_LIST_CNContactsLoggerProvider.97
- __OBJC_$_PROP_LIST_CNContactsProvider
- __OBJC_$_PROP_LIST_CNContactsProviderDataMapper
- __OBJC_$_PROP_LIST_CNContactsProviderManager
- __OBJC_$_PROP_LIST_CNContactsProviderModerator
- __OBJC_$_PROP_LIST_CNContactsProviderSession
- __OBJC_$_PROP_LIST_CNKeyboardStateMonitor.84
- __OBJC_CLASS_PROTOCOLS_$_CNContactsProviderDataMapper
- __OBJC_CLASS_PROTOCOLS_$_CNContactsProviderSession
- __OBJC_CLASS_RO_$_CNContactsProvider
- __OBJC_CLASS_RO_$_CNContactsProviderDataMapper
- __OBJC_CLASS_RO_$_CNContactsProviderManager
- __OBJC_CLASS_RO_$_CNContactsProviderModerator
- __OBJC_CLASS_RO_$_CNContactsProviderSession
- __OBJC_METACLASS_RO_$_CNContactsProvider
- __OBJC_METACLASS_RO_$_CNContactsProviderDataMapper
- __OBJC_METACLASS_RO_$_CNContactsProviderManager
- __OBJC_METACLASS_RO_$_CNContactsProviderModerator
- __OBJC_METACLASS_RO_$_CNContactsProviderSession
- __PROPERTIES__TtC8Contacts23CNContactsProviderCache
- __PROTOCOLS__TtCV8Contacts41_CNContactsProviderExtensionConfiguration14ExportedObject
- __PROTOCOLS__TtCV8Contacts41_CNContactsProviderExtensionConfiguration14ExportedObject.1
- __PROTOCOL_INSTANCE_METHODS__TtP8Contacts38CNContactsProviderExtensionXPCProtocol_
- __PROTOCOL_METHOD_TYPES__TtP8Contacts38CNContactsProviderExtensionXPCProtocol_
- __PROTOCOL__TtP8Contacts38CNContactsProviderExtensionXPCProtocol_
- ___19-[CNContainer hash]_block_invoke
- ___19-[CNContainer hash]_block_invoke_10
- ___19-[CNContainer hash]_block_invoke_11
- ___19-[CNContainer hash]_block_invoke_12
- ___19-[CNContainer hash]_block_invoke_13
- ___19-[CNContainer hash]_block_invoke_14
- ___19-[CNContainer hash]_block_invoke_15
- ___19-[CNContainer hash]_block_invoke_16
- ___19-[CNContainer hash]_block_invoke_2
- ___19-[CNContainer hash]_block_invoke_3
- ___19-[CNContainer hash]_block_invoke_4
- ___19-[CNContainer hash]_block_invoke_5
- ___19-[CNContainer hash]_block_invoke_6
- ___19-[CNContainer hash]_block_invoke_7
- ___19-[CNContainer hash]_block_invoke_8
- ___19-[CNContainer hash]_block_invoke_9
- ___21-[CNPhoneNumber hash]_block_invoke
- ___21-[CNPhoneNumber hash]_block_invoke_2
- ___22-[CNLabeledValue hash]_block_invoke
- ___22-[CNLabeledValue hash]_block_invoke_2
- ___22-[CNLabeledValue hash]_block_invoke_3
- ___23-[CNContainer isEqual:]_block_invoke
- ___23-[CNContainer isEqual:]_block_invoke_10
- ___23-[CNContainer isEqual:]_block_invoke_11
- ___23-[CNContainer isEqual:]_block_invoke_12
- ___23-[CNContainer isEqual:]_block_invoke_13
- ___23-[CNContainer isEqual:]_block_invoke_14
- ___23-[CNContainer isEqual:]_block_invoke_15
- ___23-[CNContainer isEqual:]_block_invoke_16
- ___23-[CNContainer isEqual:]_block_invoke_2
- ___23-[CNContainer isEqual:]_block_invoke_3
- ___23-[CNContainer isEqual:]_block_invoke_4
- ___23-[CNContainer isEqual:]_block_invoke_5
- ___23-[CNContainer isEqual:]_block_invoke_6
- ___23-[CNContainer isEqual:]_block_invoke_7
- ___23-[CNContainer isEqual:]_block_invoke_8
- ___23-[CNContainer isEqual:]_block_invoke_9
- ___23-[CNSocialProfile hash]_block_invoke
- ___23-[CNSocialProfile hash]_block_invoke_2
- ___23-[CNSocialProfile hash]_block_invoke_3
- ___23-[CNSocialProfile hash]_block_invoke_4
- ___23-[CNSocialProfile hash]_block_invoke_5
- ___23-[CNSocialProfile hash]_block_invoke_6
- ___23-[CNSocialProfile hash]_block_invoke_7
- ___24-[CNLabelValuePair hash]_block_invoke
- ___24-[CNLabelValuePair hash]_block_invoke_2
- ___25-[CNPhoneNumber isEqual:]_block_invoke
- ___25-[CNPhoneNumber isEqual:]_block_invoke_2
- ___26-[CNLabeledValue isEqual:]_block_invoke
- ___26-[CNLabeledValue isEqual:]_block_invoke_2
- ___26-[CNLabeledValue isEqual:]_block_invoke_3
- ___26-[CNLabeledValue isEqual:]_block_invoke_4
- ___32-[CNContactsProvider endSession]_block_invoke
- ___34+[CNContactsProviderModerator log]_block_invoke
- ___35-[CNContactsProvider startSession:]_block_invoke
- ___38+[CNContactsProviderDataMapper os_log]_block_invoke
- ___38-[CNContactsProvider isSessionRunning]_block_invoke
- ___38-[CNSocialProfile isEqual:ignoreURLs:]_block_invoke
- ___38-[CNSocialProfile isEqual:ignoreURLs:]_block_invoke_2
- ___38-[CNSocialProfile isEqual:ignoreURLs:]_block_invoke_3
- ___38-[CNSocialProfile isEqual:ignoreURLs:]_block_invoke_4
- ___38-[CNSocialProfile isEqual:ignoreURLs:]_block_invoke_5
- ___38-[CNSocialProfile isEqual:ignoreURLs:]_block_invoke_6
- ___38-[CNSocialProfile isEqual:ignoreURLs:]_block_invoke_7
- ___48-[CNContactsProviderManager initWithAuditToken:]_block_invoke
- ___52-[CNXPCDataMapper initWithConfiguration:connection:]_block_invoke
- ___52-[CNXPCDataMapper initWithConfiguration:connection:]_block_invoke_2
- ___52-[CNXPCDataMapper initWithConfiguration:connection:]_block_invoke_3
- ___58+[CNContactsProviderModerator synchronizeAllUsingSession:]_block_invoke
- ___58-[CNDataMapperContactStore requestExtensionCommand:error:]_block_invoke
- ___60-[CNXPCDataMapper remoteResultForSelector:parameters:error:]_block_invoke
- ___64-[CNContactsProvider requestExtensionCommand:completionHandler:]_block_invoke
- ___64-[CNContactsProvider synchronizeUsingSession:completionHandler:]_block_invoke
- ___72-[CNContactsProviderModerator synchronizeUsingSession:bundleIdentifier:]_block_invoke
- ___72-[CNContactsProviderModerator synchronizeUsingSession:bundleIdentifier:]_block_invoke.5
- ___72-[CNContactsProviderModerator synchronizeUsingSession:bundleIdentifier:]_block_invoke.7
- ___72-[CNContactsProviderModerator synchronizeUsingSession:bundleIdentifier:]_block_invoke.7.cold.1
- ___78-[CNContactStore(Spotlight) synchronousRemoteObjectProxyForContactsXPCService]_block_invoke
- ___78-[CNContactStore(Spotlight) synchronousRemoteObjectProxyForContactsXPCService]_block_invoke_2
- ___78-[CNContactStore(Spotlight) synchronousRemoteObjectProxyForContactsXPCService]_block_invoke_3
- ___98-[CNPredicate(Suggested) suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:]_block_invoke_3
- ___block_descriptor_49_e8_32s40s_e5_B8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e8_v16?08ls32l8s40l8s48l8
- ___block_literal_global.150
- ___block_literal_global.152
- ___block_literal_global.156
- ___block_literal_global.157
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.163
- ___block_literal_global.165
- ___block_literal_global.168
- ___block_literal_global.170
- ___block_literal_global.172
- ___block_literal_global.174
- ___block_literal_global.178
- ___block_literal_global.180
- ___block_literal_global.183
- ___block_literal_global.189
- ___block_literal_global.192
- ___block_literal_global.195
- ___block_literal_global.201
- ___block_literal_global.204
- ___block_literal_global.207
- ___block_literal_global.210
- ___block_literal_global.213
- ___block_literal_global.216
- ___block_literal_global.219
- ___block_literal_global.222
- ___block_literal_global.228
- ___block_literal_global.231
- ___block_literal_global.234
- ___block_literal_global.237
- ___block_literal_global.240
- ___block_literal_global.243
- ___block_literal_global.246
- ___block_literal_global.249
- ___block_literal_global.252
- ___block_literal_global.255
- ___block_literal_global.258
- ___block_literal_global.261
- ___block_literal_global.264
- ___block_literal_global.267
- ___block_literal_global.270
- ___block_literal_global.273
- ___block_literal_global.276
- ___block_literal_global.282
- ___block_literal_global.285
- ___block_literal_global.288
- ___block_literal_global.291
- ___block_literal_global.294
- ___block_literal_global.297
- ___block_literal_global.300
- ___block_literal_global.303
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.312
- ___block_literal_global.315
- ___block_literal_global.318
- ___block_literal_global.321
- ___block_literal_global.324
- ___block_literal_global.327
- ___block_literal_global.330
- ___block_literal_global.333
- ___block_literal_global.336
- ___block_literal_global.339
- ___block_literal_global.342
- ___block_literal_global.345
- ___block_literal_global.348
- ___block_literal_global.351
- ___block_literal_global.354
- ___block_literal_global.357
- ___block_literal_global.360
- ___block_literal_global.363
- ___block_literal_global.366
- ___block_literal_global.369
- ___block_literal_global.372
- ___block_literal_global.375
- ___block_literal_global.378
- ___block_literal_global.381
- ___block_literal_global.384
- ___block_literal_global.387
- ___block_literal_global.390
- ___block_literal_global.393
- ___block_literal_global.416
- ___block_literal_global.420
- ___block_literal_global.522
- ___block_literal_global.617
- ___block_literal_global.619
- ___block_literal_global.636
- ___block_literal_global.649
- ___block_literal_global.65
- ___block_literal_global.673
- ___block_literal_global.706
- ___block_literal_global.712
- ___block_literal_global.717
- ___block_literal_global.745
- ___block_literal_global.764
- ___block_literal_global.807
- ___block_literal_global.822
- ___block_literal_global.836
- ___block_literal_global.92
- __unnamed_array_storage.36
- __unnamed_array_storage.61
- _allContainerProperties.cn_once_object_17
- _allContainerProperties.cn_once_token_17
- _block_copy_helper.58
- _block_copy_helper.64
- _block_descriptor.60
- _block_descriptor.66
- _block_destroy_helper.59
- _block_destroy_helper.65
- _get_witness_table 8Contacts27CNContactsProviderExtensionRzlAA01_bcD13ConfigurationVyxG0D10Foundation03AppdE0HPyHC.2
- _keypath_get.7Tm
- _objc_msgSend$XPCConnectionWasInterrupted
- _objc_msgSend$XPCConnectionWasInvalidated
- _objc_msgSend$accountContainers
- _objc_msgSend$backgroundScheduler
- _objc_msgSend$contactsProviderManager
- _objc_msgSend$descriptorForAllSupportedKeys
- _objc_msgSend$finishWithResult:error:
- _objc_msgSend$initWithIdentifier:name:type:iOSLegacyIdentifier:accountIdentifier:enabled:permissions:externalIdentifier:externalModificationTag:externalSyncTag:externalSyncData:constraintsPath:meIdentifier:restrictions:guardianRestricted:lastSyncDate:
- _objc_msgSend$isContactsProvider
- _objc_msgSend$isXPCDataMapperStore:
- _objc_msgSend$providerStore
- _objc_msgSend$resultWithFuture:timeout:
- _objc_msgSend$setIsContactsProvider:
- _objc_msgSend$synchronousRemoteObjectProxyForContactsXPCService
- _suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:.cn_once_object_4
- _suggestedContactsWithSortOrder:keysToFetch:mutableObjects:service:error:.cn_once_token_4
- _swift_unknownObjectRelease_n
- _symbolic $s8Contacts27CNContactsProviderExtensionP
- _symbolic $s8Contacts38CNContactsProviderExtensionXPCProtocolP
- _symbolic 8Contacts38CNContactsProviderExtensionXPCProtocol_p
- _symbolic So25CNContactsProviderSessionC
- _symbolic _____ 8Contacts22CNContactsProviderHostC
- _symbolic _____ 8Contacts23CNContactsProviderCacheC
- _symbolic _____ 8Contacts32CNContactsProviderExtensionPointO
- _symbolic _____ 8Contacts41_CNContactsProviderExtensionConfigurationV
- _symbolic _____ 8Contacts41_CNContactsProviderExtensionConfigurationV14ExportedObjectC
- _symbolic _____yxG 8Contacts41_CNContactsProviderExtensionConfigurationV
- _symbolic _____yx_G 8Contacts41_CNContactsProviderExtensionConfigurationV14ExportedObjectC
- _writableContainerProperties.cn_once_object_18
- _writableContainerProperties.cn_once_token_18
CStrings:
+ "\x02!\x17\x11\x13"
+ "\"Q"
+ "-[CNContainer predicateForContainerWithProviderIdentifier:]"
+ "@\"<CNXPCContactsSupportService>\""
+ "@\"CNContactProviderManager\""
+ "@\"CNContactProviderModerator\""
+ "@\"CNContactProviderSession\""
+ "@\"CNProviderMetadata\""
+ "@\"CNXPCConnection\""
+ "@\"CNXPCContactsSupport\""
+ "@\"_TtC8Contacts21CNContactProviderHost\""
+ "@148@0:8@16@24q32i40@44B52@56@64@72@80@88@96@104Q112B120@124@132@140"
+ "@32@0:8:16^@24"
+ "@40@0:8:16@24^@32"
+ "@48@0:8:16@24@32^@40"
+ "CNContactProvider"
+ "CNContactProviderManager"
+ "CNContactProviderModerator"
+ "CNContactProviderSession"
+ "CNContainerProviderIdentifierDescription"
+ "CNContainerProviderMetadataDescription"
+ "CNProviderMetadata"
+ "CNXPCConnection"
+ "CNXPCContactsSupport"
+ "CNXPCContactsSupportProtocol"
+ "CNXPCContactsSupportService"
+ "CNiOSABContainerProviderIdentifierPredicate"
+ "CNiOSContactProviderDataMapper"
+ "Can't construct Array with count < 0"
+ "Clearing existing sync session for %{public}@"
+ "ContactProvider"
+ "CoreSuggestions call timed out recently; will not attempt to augment results"
+ "CoreSuggestions call timed out; results may not be augmented in subsequent calls"
+ "Could not obtain contacts service proxy for Spotlight query, error = %@"
+ "Created provider container %{public}s with provider identifier %{public}s for %{public}s app"
+ "Division by zero"
+ "Division results in an overflow"
+ "Error archiving CNProviderMetadata: %@"
+ "Error unarchiving Core Data value into CNProviderMetadata: %@"
+ "Failed due to some XPC connection error with extension %{public}s for %{public}s app, extension proxy might not conform to CNContactProviderExtensionXPCProtocol."
+ "Failed to delete provider container %{public}s with provider identifier %{public}s for %{public}s app, error = %{public}s"
+ "Failed to find provider container with provider identifier %{public}s for %{public}s app, error = %{public}s"
+ "Index out of range"
+ "Insufficient space allocated to copy string contents"
+ "Provider metadata has a higher version number than we know how to handle: %ld"
+ "Range requires lowerBound <= upperBound"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<CNXPCContactsSupportService>\",R,N,V_serviceProxy"
+ "T@\"CNContactProviderManager\",&,N,V_contactProviderManager"
+ "T@\"CNContactProviderModerator\",&,N,V_moderator"
+ "T@\"CNContactProviderSession\",&,N,V_currentSession"
+ "T@\"CNContactProviderSession\",&,N,V_session"
+ "T@\"CNProviderMetadata\",C,D,N"
+ "T@\"CNProviderMetadata\",R,C,N,V_providerMetadata"
+ "T@\"CNXPCConnection\",R,N,V_serviceConnection"
+ "T@\"CNXPCContactsSupport\",&,N,V_contactsSupport"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSData\",&,N,V_pageData"
+ "T@\"NSData\",&,N,V_syncAnchorData"
+ "T@\"NSString\",?,&,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C,N,V_providerIdentifier"
+ "T@\"_TtC8Contacts21CNContactProviderHost\",&,N,V_providerHost"
+ "T@\"_TtC8Contacts21CNContactProviderHost\",R,N,V_host"
+ "T@\"_TtC8Contacts22CNContactProviderCache\",N,R"
+ "T@,R,N,V_serviceProxy"
+ "TB,?,R"
+ "TB,?,R,N"
+ "TB,N,V_isContactProvider"
+ "TB,R,N,V_isContactProvider"
+ "Tq,N,V_version"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "XPCConnectionWasInterruptedForService:"
+ "XPCConnectionWasInvalidatedForService:"
+ "_TtC8Contacts21CNContactProviderHost"
+ "_TtC8Contacts22CNContactProviderCache"
+ "_TtP8Contacts37CNContactProviderExtensionXPCProtocol_"
+ "_contactProviderManager"
+ "_contactsSupport"
+ "_isContactProvider"
+ "_pageData"
+ "_providerIdentifier"
+ "_providerMetadata"
+ "_serviceConnection"
+ "_syncAnchorData"
+ "arrayWithObjects:"
+ "com.apple.contact.provider.extension"
+ "com.apple.contactsd.contact-provider"
+ "com.apple.contactsd.support"
+ "contactProviderManager"
+ "contactsSupport"
+ "containerProviderIdentifierDescription"
+ "containerProviderMetadataDescription"
+ "descriptorForAllSupportedKeysWithOptions:"
+ "evictPromiseForBundleIdentifier:"
+ "includePronouns"
+ "initWithConnection:"
+ "initWithConnection:interface:logger:"
+ "initWithIdentifier:name:type:iOSLegacyIdentifier:accountIdentifier:enabled:permissions:externalIdentifier:externalModificationTag:externalSyncTag:externalSyncData:constraintsPath:meIdentifier:restrictions:guardianRestricted:lastSyncDate:providerIdentifier:providerMetadata:"
+ "initWithPage:syncAnchor:"
+ "initWithProviderIdentifier:"
+ "initWithVersion:page:syncAnchor:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isConnectionForContactProvider:"
+ "isContactProvider"
+ "isXPCDataMapperStoreForFavorites:"
+ "isXPCDataMapperStoreForSpotlight:"
+ "pageData"
+ "predicateForContainerWithProviderIdentifier:"
+ "providerContainer for %{public}s"
+ "providerIdentifier"
+ "providerIdentifier == %@"
+ "providerMetadata"
+ "recordExceptionForEvent:"
+ "remoteResultForSelector:error:"
+ "remoteResultForSelector:param1:error:"
+ "remoteResultForSelector:param1:param2:error:"
+ "remoteResultForSelector:parameters:error:"
+ "serviceConnection"
+ "serviceProxy"
+ "setContactProviderManager:"
+ "setContactsSupport:"
+ "setIsContactProvider:"
+ "setPageData:"
+ "setProviderIdentifier:"
+ "setProviderMetadata:"
+ "setSyncAnchorData:"
+ "setSyncTimeout:"
+ "setVersion:"
+ "statusForEvent:"
+ "syncAnchorData"
+ "v32@0:8@\"CNContactProviderSession\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"CNContactProviderSession\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "watchdog"
- "\x02!\x17\x11\x11"
- "\x12Q"
- "@\"CNContactsProviderManager\""
- "@\"CNContactsProviderModerator\""
- "@\"CNContactsProviderSession\""
- "@\"_TtC8Contacts22CNContactsProviderHost\""
- "@132@0:8@16@24q32i40@44B52@56@64@72@80@88@96@104Q112B120@124"
- "CNContactsProvider"
- "CNContactsProviderDataMapper"
- "CNContactsProviderManager"
- "CNContactsProviderModerator"
- "CNContactsProviderSession"
- "ContactsProvider"
- "Created provider container %{public}s with external identifier %{public}s for %{public}s app"
- "Error: service connection interupted"
- "Error: service connection invalidated"
- "Failed due to some XPC connection error with extension %{public}s for %{public}s app, extension proxy might not conform to CNContactsProviderExtensionXPCProtocol."
- "Failed to delete provider container %{public}s with external identifier %{public}s for %{public}s app, error = %{public}s"
- "Failed to find provider container with external identifier %{public}s for %{public}s app, error = %{public}s"
- "T@\"CNContactsProviderManager\",&,N,V_contactsProviderManager"
- "T@\"CNContactsProviderModerator\",&,N,V_moderator"
- "T@\"CNContactsProviderSession\",&,N,V_currentSession"
- "T@\"CNContactsProviderSession\",&,N,V_session"
- "T@\"NSString\",&,N"
- "T@\"_TtC8Contacts22CNContactsProviderHost\",&,N,V_providerHost"
- "T@\"_TtC8Contacts22CNContactsProviderHost\",R,N,V_host"
- "T@\"_TtC8Contacts23CNContactsProviderCache\",N,R"
- "TB,N,V_isContactsProvider"
- "TB,R,N,V_isContactsProvider"
- "Tq,N,V_contactBatchCount"
- "XPCConnectionWasInterrupted"
- "XPCConnectionWasInvalidated"
- "_TtC8Contacts22CNContactsProviderHost"
- "_TtC8Contacts23CNContactsProviderCache"
- "_TtP8Contacts38CNContactsProviderExtensionXPCProtocol_"
- "_contactsProviderManager"
- "_isContactsProvider"
- "accountContainers"
- "com.apple.contacts.provider.extension"
- "com.apple.contactsd.contacts-provider"
- "contactsProviderManager"
- "descriptorForAllSupportedKeys"
- "finishWithResult:error:"
- "initWithIdentifier:name:type:iOSLegacyIdentifier:accountIdentifier:enabled:permissions:externalIdentifier:externalModificationTag:externalSyncTag:externalSyncData:constraintsPath:meIdentifier:restrictions:guardianRestricted:lastSyncDate:"
- "isConnectionForContactsProvider:"
- "isContactsProvider"
- "isXPCDataMapperStore:"
- "resultWithFuture:timeout:"
- "setContactsProviderManager:"
- "setIsContactsProvider:"
- "synchronousRemoteObjectProxyForContactsXPCService"
- "v32@0:8@\"CNContactsProviderSession\"16@?<v@?@\"NSError\">24"
- "v40@0:8@\"CNContactsProviderSession\"16@\"NSString\"24@?<v@?@\"NSError\">32"

```
