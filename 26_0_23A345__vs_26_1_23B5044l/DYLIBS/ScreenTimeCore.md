## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-605.0.1.0.0
-  __TEXT.__text: 0xbea64
+605.1.8.0.0
+  __TEXT.__text: 0xba940
   __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x8ba0
+  __TEXT.__objc_methlist: 0x8ba8
   __TEXT.__const: 0x2028
-  __TEXT.__cstring: 0xa748
-  __TEXT.__oslogstring: 0xa19f
-  __TEXT.__gcc_except_tab: 0x1d00
+  __TEXT.__cstring: 0xa6a8
+  __TEXT.__oslogstring: 0x9a2f
+  __TEXT.__gcc_except_tab: 0x1b90
   __TEXT.__constg_swiftt: 0x8b4
   __TEXT.__swift5_typeref: 0xba4
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x556
-  __TEXT.__swift5_fieldmd: 0x720
+  __TEXT.__swift5_reflstr: 0x536
+  __TEXT.__swift5_fieldmd: 0x708
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x1ac
   __TEXT.__swift5_types: 0x9c

   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2ea8
+  __TEXT.__unwind_info: 0x2e48
   __TEXT.__eh_frame: 0x1628
-  __TEXT.__objc_classname: 0x18c6
-  __TEXT.__objc_methname: 0x16dab
-  __TEXT.__objc_methtype: 0x251c
-  __TEXT.__objc_stubs: 0xd920
-  __DATA_CONST.__got: 0xb90
-  __DATA_CONST.__const: 0x1af0
-  __DATA_CONST.__objc_classlist: 0x608
+  __TEXT.__objc_classname: 0x18d3
+  __TEXT.__objc_methname: 0x16ef6
+  __TEXT.__objc_methtype: 0x24f8
+  __TEXT.__objc_stubs: 0xd5c0
+  __DATA_CONST.__got: 0xbc8
+  __DATA_CONST.__const: 0x1b38
+  __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x1f0
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b40
-  __DATA_CONST.__objc_protorefs: 0x118
+  __DATA_CONST.__objc_selrefs: 0x4b98
+  __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x470
-  __DATA_CONST.__objc_arraydata: 0x250
+  __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb40
-  __AUTH_CONST.__const: 0x1d60
-  __AUTH_CONST.__cfstring: 0x8cc0
-  __AUTH_CONST.__objc_const: 0x10588
+  __AUTH_CONST.__const: 0x1cc0
+  __AUTH_CONST.__cfstring: 0x8ce0
+  __AUTH_CONST.__objc_const: 0x10640
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x30c8
+  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH.__objc_data: 0x3118
   __AUTH.__data: 0x340
   __DATA.__objc_ivar: 0x620
-  __DATA.__data: 0x1bf8
+  __DATA.__data: 0x1b98
   __DATA.__bss: 0x3550
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x13c8

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9F44CF3A-5E83-3C8C-AAD3-89B5B1321CA3
-  Functions: 4626
-  Symbols:   12008
-  CStrings:  7021
+  UUID: FA689B80-799F-3BA3-AC60-378C2BE014EF
+  Functions: 4584
+  Symbols:   11880
+  CStrings:  7001
 
Symbols:
+ +[STCoreOrganizationSettings keyPathsForValuesAffectingIsCommunicationSafetyRestricted]
+ +[STCoreUser(UnmodeledProperties) keyPathsForValuesAffectingIsCommunicationSafetyRestricted]
+ +[STLocations diagnosticsDirectory]
+ +[STLog diagnostics]
+ -[STAltDistroAppInfoLoader .cxx_destruct]
+ -[STAltDistroAppInfoLoader _enqueueRequest:]
+ -[STAltDistroAppInfoLoader _startNextRequest]
+ -[STAltDistroAppInfoLoader fetchForAppBundleId:adamId:distributorBundleId:completionHandler:]
+ -[STAltDistroAppInfoLoader initWithAltDistroRequestsFetcher:]
+ -[STAltDistroAppInfoLoader init]
+ -[STAltDistroAppInfoLoader pendingRequests]
+ -[STAltDistroAppInfoLoader setPendingRequests:]
+ -[STAltDistroAppRequestData .cxx_destruct]
+ -[STAltDistroAppRequestData adamID]
+ -[STAltDistroAppRequestData bundleID]
+ -[STAltDistroAppRequestData completion]
+ -[STAltDistroAppRequestData distributorID]
+ -[STAltDistroAppRequestData request]
+ -[STAltDistroAppRequestData setAdamID:]
+ -[STAltDistroAppRequestData setBundleID:]
+ -[STAltDistroAppRequestData setCompletion:]
+ -[STAltDistroAppRequestData setDistributorID:]
+ -[STAltDistroAppRequestData setRequest:]
+ -[STAppInfoCache altDistroAppInfoLoader]
+ -[STAppInfoCache appInfoForBundleIdentifier:adamId:distributorId:]
+ -[STCoreOrganizationSettings isCommunicationSafetyRestricted]
+ -[STCoreOrganizationSettings setIsCommunicationSafetyRestricted:]
+ -[STCoreUser(UnmodeledInternal) setIsCommunicationSafetyRestricted:]
+ -[STCoreUser(UnmodeledProperties) isCommunicationSafetyRestricted]
+ -[STManagementState exportDatabaseToURL:error:]
+ GCC_except_table130
+ GCC_except_table136
+ GCC_except_table50
+ GCC_except_table60
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table90
+ GCC_except_table93
+ _ASCArtworkCropBoundingBox
+ _ASCArtworkFormatPNG
+ _ASCArtworkTemplateKeyCrop
+ _ASCArtworkTemplateKeyFormat
+ _ASCArtworkTemplateKeyHeight
+ _ASCArtworkTemplateKeyWidth
+ _ASCLockupContextAppDistributionInstall
+ _ASCLockupKindApp
+ _OBJC_CLASS_$_ASCAdamID
+ _OBJC_CLASS_$_ASCLockupRequest
+ _OBJC_CLASS_$_ASCLockupViewGroup
+ _OBJC_CLASS_$_STAltDistroAppInfoLoader
+ _OBJC_CLASS_$_STAltDistroAppRequestData
+ _OBJC_IVAR_$_STAltDistroAppInfoLoader._pendingRequests
+ _OBJC_IVAR_$_STAltDistroAppInfoLoader._requestsFetcher
+ _OBJC_IVAR_$_STAltDistroAppRequestData._adamID
+ _OBJC_IVAR_$_STAltDistroAppRequestData._bundleID
+ _OBJC_IVAR_$_STAltDistroAppRequestData._completion
+ _OBJC_IVAR_$_STAltDistroAppRequestData._distributorID
+ _OBJC_IVAR_$_STAltDistroAppRequestData._request
+ _OBJC_IVAR_$_STAppInfoCache._altDistroAppInfoLoader
+ _OBJC_METACLASS_$_STAltDistroAppInfoLoader
+ _OBJC_METACLASS_$_STAltDistroAppRequestData
+ __ASCLockupKeyAdamID
+ __ASCLockupKeyAgeRating
+ __ASCLockupKeyDeveloperName
+ __ASCLockupKeyIcon
+ __ASCLockupKeyShortName
+ __OBJC_$_INSTANCE_METHODS_STAltDistroAppInfoLoader
+ __OBJC_$_INSTANCE_METHODS_STAltDistroAppRequestData
+ __OBJC_$_INSTANCE_VARIABLES_STAltDistroAppInfoLoader
+ __OBJC_$_INSTANCE_VARIABLES_STAltDistroAppRequestData
+ __OBJC_$_PROP_LIST_STAltDistroAppInfoLoader
+ __OBJC_$_PROP_LIST_STAltDistroAppRequestData
+ __OBJC_CLASS_RO_$_STAltDistroAppInfoLoader
+ __OBJC_CLASS_RO_$_STAltDistroAppRequestData
+ __OBJC_METACLASS_RO_$_STAltDistroAppInfoLoader
+ __OBJC_METACLASS_RO_$_STAltDistroAppRequestData
+ ___39-[STManagementState isLocalUserManaged]_block_invoke.4
+ ___39-[STManagementState isLocalUserManaged]_block_invoke.4.cold.1
+ ___45-[STAltDistroAppInfoLoader _startNextRequest]_block_invoke
+ ___46-[STManagementState isRestrictionsPasscodeSet]_block_invoke.17
+ ___46-[STManagementState isRestrictionsPasscodeSet]_block_invoke.17.cold.1
+ ___47-[STManagementState exportDatabaseToURL:error:]_block_invoke
+ ___47-[STManagementState exportDatabaseToURL:error:]_block_invoke_2
+ ___47-[STManagementState isRestrictionsPasscodeSet:]_block_invoke.18
+ ___47-[STManagementState isRestrictionsPasscodeSet:]_block_invoke.18.cold.1
+ ___51-[STManagementState needsToSetRestrictionsPasscode]_block_invoke.19
+ ___51-[STManagementState needsToSetRestrictionsPasscode]_block_invoke.19.cold.1
+ ___61-[STManagementState isLocalUserManagedWithCompletionHandler:]_block_invoke.16
+ ___61-[STManagementState isLocalUserManagedWithCompletionHandler:]_block_invoke.16.cold.1
+ ___62-[STSetupClient collectPasscodeFromUserWithCompletionHandler:]_block_invoke.14
+ ___62-[STSetupClient collectPasscodeFromUserWithCompletionHandler:]_block_invoke.14.cold.1
+ ___66-[STAppInfoCache _fetchSyncedInstalledAppInfoForBundleIdentifier:]_block_invoke.230
+ ___66-[STAppInfoCache appInfoForBundleIdentifier:adamId:distributorId:]_block_invoke
+ ___66-[STAppInfoCache appInfoForBundleIdentifier:adamId:distributorId:]_block_invoke.cold.1
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.71
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.71.cold.1
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.71.cold.2
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.73
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.73.cold.1
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.75
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.75.cold.1
+ ___93-[STAltDistroAppInfoLoader fetchForAppBundleId:adamId:distributorBundleId:completionHandler:]_block_invoke
+ ___96-[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithCompletionHandler:]_block_invoke.23
+ ___96-[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithCompletionHandler:]_block_invoke.23.cold.1
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e31_v24?0"NSError"8"STAppInfo"16ls32l8s40l8s48l8
+ ___block_literal_global.21
+ ___block_literal_global.235
+ _objc_msgSend$_enqueueRequest:
+ _objc_msgSend$_lockupDictionaryForRequest:includingKeys:withCompletionBlock:
+ _objc_msgSend$_requestWithID:kind:context:appVersionId:distributorId:
+ _objc_msgSend$_startNextRequest
+ _objc_msgSend$altDistroAppInfoLoader
+ _objc_msgSend$bundleID
+ _objc_msgSend$completion
+ _objc_msgSend$exportDatabaseToURL:replyHandler:
+ _objc_msgSend$fetchForAppBundleId:adamId:distributorBundleId:completionHandler:
+ _objc_msgSend$initWithAltDistroRequestsFetcher:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$initWithNumberValue:
+ _objc_msgSend$isCommunicationSafetyRestricted
+ _objc_msgSend$keyPathsForValuesAffectingIsCommunicationSafetyReceivingRestricted
+ _objc_msgSend$keyPathsForValuesAffectingIsCommunicationSafetySendingRestricted
+ _objc_msgSend$makeURLWithSubstitutions:
+ _objc_msgSend$pendingRequests
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setCompletion:
+ _objc_msgSend$setIsCommunicationSafetyRestricted:
+ _objc_msgSend$setPendingRequests:
+ _objc_msgSend$setRequest:
- +[STCoreOrganizationSettings fetchOrCreateWithDictionaryRepresentation:inContext:error:].cold.1
- +[STCoreOrganizationSettings fetchOrCreateWithDictionaryRepresentation:inContext:error:].cold.2
- +[STCoreOrganizationSettings fetchOrCreateWithDictionaryRepresentation:inContext:error:].cold.3
- +[STCoreOrganizationSettings fetchOrCreateWithDictionaryRepresentation:inContext:error:].cold.4
- +[STCoreOrganizationSettings fetchOrCreateWithDictionaryRepresentation:inContext:error:].cold.5
- +[STCoreOrganizationSettings fetchOrCreateWithDictionaryRepresentation:inContext:error:].cold.6
- +[STCoreOrganizationSettings fetchOrCreateWithDictionaryRepresentation:inContext:error:].cold.7
- +[STCoreOrganizationSettings fetchOrCreateWithDictionaryRepresentation:inContext:error:].cold.8
- +[STRestrictionsFetcher _webContentFilterStateForWebFilterState:]
- -[STAdminPersistenceController newBackgroundContext].cold.1
- -[STAskClient askServiceClient]
- -[STAskClient dealloc]
- -[STAskClient setAskServiceClient:]
- -[STAskForTimeClient askServiceClient]
- -[STAskForTimeClient dealloc]
- -[STAskForTimeClient setAskServiceClient:]
- -[STAskServiceClient .cxx_destruct]
- -[STAskServiceClient approveExceptionForRequest:completionHandler:]
- -[STAskServiceClient approveExceptionForRequest:completionHandler:].cold.1
- -[STAskServiceClient connection]
- -[STAskServiceClient dealloc]
- -[STAskServiceClient fetchLastResponseForRequestedResourceIdentifier:usageType:withCompletionHandler:]
- -[STAskServiceClient handleAnswer:requestIdentifier:timeApproved:completionHandler:]
- -[STAskServiceClient handleAnswer:requestIdentifier:timeApproved:completionHandler:].cold.1
- -[STAskServiceClient initWithAlternateMachService]
- -[STAskServiceClient init]
- -[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]
- -[STAskServiceClient sendAskForTimeRequest:completionHandler:]
- -[STAskServiceClient sendAskForTimeRequest:completionHandler:].cold.1
- -[STAskServiceClient setConnection:]
- -[STCommunicationClient communicationServiceClient]
- -[STCommunicationClient setCommunicationServiceClient:]
- -[STCoreUser(UnmodeledInternal) setScreenTimeEnabled:].cold.3
- -[STCoreUser(UnmodeledInternal) unmodeledManagingOrganizationSettings].cold.1
- -[STCoreUser(UnmodeledInternal) unmodeledManagingOrganizationSettings].cold.2
- -[STCoreUser(UnmodeledProperties) isAppAndWebsiteActivityEnabled].cold.1
- -[STCoreUser(UnmodeledProperties) screenTimeEnabled].cold.2
- -[STDowntimeClient downtimeServiceClient]
- -[STDowntimeClient setDowntimeServiceClient:]
- -[STInstalledApp updateWithDictionaryRepresentation:].cold.2
- -[STManagementState needsToSetRestrictionsPasscode].cold.1
- -[STManagementState privateServiceClient]
- -[STManagementState setPrivateServiceClient:]
- -[STMutableRestrictions setWebContentFilterState:]
- -[STRestrictions webContentFilterState]
- -[STSetupClient setSetupServiceClient:]
- -[STSetupClient setupServiceClient]
- GCC_except_table123
- GCC_except_table134
- GCC_except_table34
- GCC_except_table37
- GCC_except_table40
- GCC_except_table43
- GCC_except_table61
- GCC_except_table62
- GCC_except_table77
- GCC_except_table80
- GCC_except_table83
- GCC_except_table86
- GCC_except_table89
- _NSDebugDescriptionErrorKey
- _NSDetailedErrorsKey
- _NSXPCStoreServerEndpointFactoryKey
- _OBJC_CLASS_$_NSException
- _OBJC_CLASS_$_STAskServiceClient
- _OBJC_IVAR_$_STAskClient._askServiceClient
- _OBJC_IVAR_$_STAskForTimeClient._askServiceClient
- _OBJC_IVAR_$_STAskServiceClient._connection
- _OBJC_IVAR_$_STCommunicationClient._communicationServiceClient
- _OBJC_IVAR_$_STDowntimeClient._downtimeServiceClient
- _OBJC_IVAR_$_STManagementState._privateServiceClient
- _OBJC_IVAR_$_STRestrictions._webContentFilterState
- _OBJC_IVAR_$_STSetupClient._setupServiceClient
- _OBJC_METACLASS_$_STAskServiceClient
- __OBJC_$_INSTANCE_METHODS_STAskServiceClient
- __OBJC_$_INSTANCE_VARIABLES_STAskServiceClient
- __OBJC_$_PROP_LIST_STAskServiceClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_STAskServiceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_STAskServiceProtocol
- __OBJC_CLASS_RO_$_STAskServiceClient
- __OBJC_LABEL_PROTOCOL_$_STAskServiceProtocol
- __OBJC_METACLASS_RO_$_STAskServiceClient
- __OBJC_PROTOCOL_$_STAskServiceProtocol
- __OBJC_PROTOCOL_REFERENCE_$_STAskServiceProtocol
- ___26-[STAskServiceClient init]_block_invoke
- ___26-[STAskServiceClient init]_block_invoke.22
- ___26-[STAskServiceClient init]_block_invoke.22.cold.1
- ___26-[STAskServiceClient init]_block_invoke.cold.1
- ___39-[STManagementState isLocalUserManaged]_block_invoke.7
- ___39-[STManagementState isLocalUserManaged]_block_invoke.7.cold.1
- ___46-[STManagementState isRestrictionsPasscodeSet]_block_invoke.20
- ___46-[STManagementState isRestrictionsPasscodeSet]_block_invoke.20.cold.1
- ___47-[STManagementState isRestrictionsPasscodeSet:]_block_invoke.21
- ___47-[STManagementState isRestrictionsPasscodeSet:]_block_invoke.21.cold.1
- ___47-[STManagementState isRestrictionsPasscodeSet:]_block_invoke.22
- ___47-[STManagementState isRestrictionsPasscodeSet:]_block_invoke.22.cold.1
- ___50-[STAdminPersistenceController saveContext:error:]_block_invoke
- ___50-[STAdminPersistenceController saveContext:error:]_block_invoke.cold.1
- ___50-[STAskServiceClient initWithAlternateMachService]_block_invoke
- ___50-[STAskServiceClient initWithAlternateMachService]_block_invoke.27
- ___50-[STAskServiceClient initWithAlternateMachService]_block_invoke.27.cold.1
- ___50-[STAskServiceClient initWithAlternateMachService]_block_invoke.cold.1
- ___51-[STManagementState needsToSetRestrictionsPasscode]_block_invoke.23
- ___51-[STManagementState needsToSetRestrictionsPasscode]_block_invoke.23.cold.1
- ___54-[STAdminPersistenceController performBackgroundTask:]_block_invoke_2
- ___59-[STManagementState triggerDowngradeMigrationWithOutError:]_block_invoke
- ___59-[STManagementState triggerDowngradeMigrationWithOutError:]_block_invoke_2
- ___61-[STAdminPersistenceController performBackgroundTaskAndWait:]_block_invoke_2
- ___61-[STManagementState isLocalUserManagedWithCompletionHandler:]_block_invoke.19
- ___61-[STManagementState isLocalUserManagedWithCompletionHandler:]_block_invoke.19.cold.1
- ___62-[STAskServiceClient sendAskForTimeRequest:completionHandler:]_block_invoke
- ___62-[STAskServiceClient sendAskForTimeRequest:completionHandler:]_block_invoke.33
- ___62-[STAskServiceClient sendAskForTimeRequest:completionHandler:]_block_invoke.cold.1
- ___62-[STManagementState screenTimeSyncStateWithCompletionHandler:]_block_invoke_3
- ___62-[STSetupClient collectPasscodeFromUserWithCompletionHandler:]_block_invoke.17
- ___62-[STSetupClient collectPasscodeFromUserWithCompletionHandler:]_block_invoke.17.cold.1
- ___66-[STAppInfoCache _fetchSyncedInstalledAppInfoForBundleIdentifier:]_block_invoke.226
- ___67-[STAskServiceClient approveExceptionForRequest:completionHandler:]_block_invoke
- ___67-[STAskServiceClient approveExceptionForRequest:completionHandler:]_block_invoke.34
- ___67-[STAskServiceClient approveExceptionForRequest:completionHandler:]_block_invoke.cold.1
- ___70-[STCoreUser(UnmodeledInternal) unmodeledManagingOrganizationSettings]_block_invoke
- ___70-[STCoreUser(UnmodeledInternal) unmodeledManagingOrganizationSettings]_block_invoke.cold.1
- ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.80
- ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.80.cold.1
- ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.80.cold.2
- ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.82
- ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.82.cold.1
- ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.84
- ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.84.cold.1
- ___76-[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]_block_invoke
- ___76-[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]_block_invoke.36
- ___76-[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]_block_invoke.36.cold.1
- ___76-[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]_block_invoke.cold.1
- ___84-[STAskForTimeClient handleAnswer:requestIdentifier:timeApproved:completionHandler:]_block_invoke.61
- ___84-[STAskForTimeClient handleAnswer:requestIdentifier:timeApproved:completionHandler:]_block_invoke.cold.1
- ___84-[STAskServiceClient handleAnswer:requestIdentifier:timeApproved:completionHandler:]_block_invoke
- ___84-[STAskServiceClient handleAnswer:requestIdentifier:timeApproved:completionHandler:]_block_invoke.35
- ___84-[STAskServiceClient handleAnswer:requestIdentifier:timeApproved:completionHandler:]_block_invoke.cold.1
- ___96-[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithCompletionHandler:]_block_invoke.26
- ___96-[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithCompletionHandler:]_block_invoke.26.cold.1
- ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
- ___block_literal_global.232
- ___block_literal_global.25
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_ScreenTimeCore
- _objc_msgSend$_validateCurrentOrganization:
- _objc_msgSend$_webContentFilterStateForWebFilterState:
- _objc_msgSend$applyDefaultUserPoliciesWithError:
- _objc_msgSend$applyUpdatedConfiguration:error:
- _objc_msgSend$askServiceClient
- _objc_msgSend$clearRestrictionsPasscodeWithError:
- _objc_msgSend$collectPasscodeFromUserWithCompletionHandler:
- _objc_msgSend$currentConfigurationForUser:error:
- _objc_msgSend$currentConfigurationWithError:
- _objc_msgSend$defaultSettingsForFamilyMemberOfType:
- _objc_msgSend$deleteAllWebHistoryForApplication:completionHandler:
- _objc_msgSend$deleteAllWebHistoryForApplication:profileIdentifier:completionHandler:
- _objc_msgSend$deleteWebHistoryDuringInterval:application:completionHandler:
- _objc_msgSend$deleteWebHistoryDuringInterval:application:profileIdentifier:completionHandler:
- _objc_msgSend$deleteWebHistoryForDomain:application:completionHandler:
- _objc_msgSend$deleteWebHistoryForDomain:application:profileIdentifier:completionHandler:
- _objc_msgSend$deleteWebHistoryForURL:application:completionHandler:
- _objc_msgSend$deleteWebHistoryForURL:application:profileIdentifier:completionHandler:
- _objc_msgSend$deleteWebHistoryForURLs:application:completionHandler:
- _objc_msgSend$deleteWebHistoryForURLs:application:profileIdentifier:completionHandler:
- _objc_msgSend$enableRemoteManagementForDSID:error:
- _objc_msgSend$fetchWithContext:error:
- _objc_msgSend$initWithAlternateMachService
- _objc_msgSend$initWithBundleIdentifier:
- _objc_msgSend$initWithSuiteName:
- _objc_msgSend$isContentPrivacyEnabledForDSID:error:
- _objc_msgSend$isDowntimeEnabledForUserID:
- _objc_msgSend$isRestrictionsPasscodeSetWithError:
- _objc_msgSend$isScreenTimeEnabledForLocalUserWithError:
- _objc_msgSend$isScreenTimeEnabledForRemoteUserWithDSID:error:
- _objc_msgSend$isWebContentRestricted:
- _objc_msgSend$lastCommunicationLimitsModificationDateForDSID:completionHandler:
- _objc_msgSend$mainThread
- _objc_msgSend$needsToSetRestrictionsPasscodeWithError:
- _objc_msgSend$permitWebFilterURL:pageTitle:error:
- _objc_msgSend$privateServiceClient
- _objc_msgSend$processSettingsChangesSinceHistoryToken:withCompletion:
- _objc_msgSend$raise:format:
- _objc_msgSend$respondToAskForTimeRequestWithIdentifier:answer:error:
- _objc_msgSend$setScreenTimeEnabledForLocalUser:error:
- _objc_msgSend$setScreenTimeEnabledForRemoteUserWithDSID:enabled:error:
- _objc_msgSend$setScreenTimeSyncEnabled:error:
- _objc_msgSend$setWebContentFilterState:
- _objc_msgSend$shouldAllowOneMoreMinuteForBundleIdentifier:error:
- _objc_msgSend$shouldAllowOneMoreMinuteForCategoryIdentifier:error:
- _objc_msgSend$shouldAllowOneMoreMinuteForWebDomain:error:
- _objc_msgSend$storeServerEndpointFactory
- _objc_msgSend$triggerDowngradeMigrationWithCompletionHandler:
- _objc_msgSend$webContentFilterState
CStrings:
+ "/private/var/tmp/ScreenTimeDiagnostics"
+ "128"
+ "<%p ID: %@ Name: %@ Developer: %@, AdamID: %llu, DistributorID: %@>"
+ "@\"<STAltDistroRequestFetcher>\""
+ "@\"ASCLockupRequest\""
+ "@\"NSMutableArray\""
+ "@\"STAltDistroAppInfoLoader\""
+ "Cannot fetch alt distro app info for bundle ID:%@ error:%@"
+ "Received app info from alt distro app info loader:%@"
+ "STAltDistroAppInfoLoader"
+ "STAltDistroAppRequestData"
+ "ScreenTimeLockups"
+ "T@\"ASCLockupRequest\",C,N,V_request"
+ "T@\"NSMutableArray\",&,V_pendingRequests"
+ "T@\"NSNumber\",C,N,V_adamID"
+ "T@\"NSString\",C,N,V_bundleID"
+ "T@\"STAltDistroAppInfoLoader\",R,N,V_altDistroAppInfoLoader"
+ "T@?,C,N,V_completion"
+ "_altDistroAppInfoLoader"
+ "_bundleID"
+ "_completion"
+ "_enqueueRequest:"
+ "_lockupDictionaryForRequest:includingKeys:withCompletionBlock:"
+ "_pendingRequests"
+ "_requestWithID:kind:context:appVersionId:distributorId:"
+ "_requestsFetcher"
+ "_startNextRequest"
+ "altDistroAppInfoLoader"
+ "appInfoForBundleIdentifier:adamId:distributorId:"
+ "bundleID"
+ "cloudSettings.isCommunicationSafetyRestricted"
+ "com.apple.AppStore"
+ "completion"
+ "data"
+ "diagnostics"
+ "diagnosticsDirectory"
+ "error"
+ "exportDatabaseToURL:error:"
+ "exportDatabaseToURL:replyHandler:"
+ "familySettings.isCommunicationSafetyRestricted"
+ "fetchForAppBundleId:adamId:distributorBundleId:completionHandler:"
+ "initWithAltDistroRequestsFetcher:"
+ "initWithName:"
+ "initWithNumberValue:"
+ "isCommunicationSafetyRestricted"
+ "keyPathsForValuesAffectingIsCommunicationSafetyRestricted"
+ "localSettings.isCommunicationSafetyRestricted"
+ "makeURLWithSubstitutions:"
+ "pendingRequests"
+ "setBundleID:"
+ "setCompletion:"
+ "setIsCommunicationSafetyRestricted:"
+ "setPendingRequests:"
+ "setRequest:"
+ "v24@?0@\"NSError\"8@\"STAppInfo\"16"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24"
- "<%p ID: %@ Name: %@ Developer: %@, AdamID: %llu>"
- "@\"STAskServiceClient\""
- "@\"STCommunicationServiceClient\""
- "@\"STDowntimeServiceClient\""
- "@\"STSetupServiceClient\""
- "A local user must have Cloud Settings."
- "Cloud organization could not be created: %{public}@"
- "Could not query screenTimeEnabled: %@"
- "Could not set screenTimeEnabled: %@"
- "Error handling answer for ask for more request : %{public}@"
- "Failed checking if restrictions paccode is set with error: %@."
- "Failed to execute search for existing settings: %{public}@"
- "Family organization does not exist: %{public}@"
- "Family settings indicated the user: (localUser, privacy: .public) is managed."
- "InstalledApp %@ without a UserDeviceState: %{public}@"
- "No current organizaiton in ST settings. Current settings will be recalculated."
- "No current organization could be derived. Results are unknown"
- "Returning STConversation early since Screen Time is OFF. Initializing STConversation asynchronously for bundle identifier: %{public}@"
- "STAdminPersistenceController.m"
- "STAskServiceClient"
- "STAskServiceClient.approveExceptionForRequest"
- "STAskServiceClient.handleAnswer"
- "STAskServiceClient.respondToAskForTimeRequestWithIdentifier"
- "STAskServiceClient.sendAskForTimeRequest"
- "STAskServiceProtocol"
- "Screen Time agent failed to process settings changes: %{public}@"
- "ScreenTime Multiple validation errors occurred."
- "ScreenTimeEnabled"
- "Settings created via the simplified agent path. Settings: %@"
- "Settings payload does not contain a class key: %{public}@"
- "Settings payload does not contain a user dsid and we could not find a local user: %{public}@"
- "Settings payload is not supported as a serialized object: %{public}@"
- "T@\"STAskServiceClient\",&,N,V_askServiceClient"
- "T@\"STCommunicationServiceClient\",&,N,V_communicationServiceClient"
- "T@\"STDowntimeServiceClient\",&,N,V_downtimeServiceClient"
- "T@\"STSetupServiceClient\",&,N,V_setupServiceClient"
- "The user: (localUser, privacy: .public) is using cloud settings."
- "There is already a settings object that matches: %{public}@."
- "There is not already a settings object that matches: %{public}@. A new one will be created"
- "There must be one Cloud Organization object."
- "There must be one Family Organization."
- "There must be one and only one Family Organization object."
- "Unable to find local user for:: %{public}@."
- "Unknown error"
- "_askServiceClient"
- "_communicationServiceClient"
- "_downtimeServiceClient"
- "_setupServiceClient"
- "_webContentFilterState"
- "_webContentFilterStateForWebFilterState:"
- "alternate askService connection interrupted"
- "alternate askService connection invalidated"
- "approveExceptionForRequest failed with error: %{public}@"
- "askService connection interrupted"
- "askService connection invalidated"
- "askServiceClient"
- "cannot fetch or create Local User Device state with simplified agent"
- "communicationServiceClient"
- "downtimeServiceClient"
- "failed to fetch local settings: %{public}@"
- "failed to fetch local settings: %{public}@. Current settings will be recalculated"
- "feature_decoupling"
- "handleAnswer failed with error: %{public}@"
- "handleAnswer failed with: %{public}@"
- "initWithAlternateMachService"
- "mainThread"
- "new background context is being called from a background thread"
- "q24@0:8Q16"
- "raise:format:"
- "sendAskForTimeRequest failed with error: %{public}@"
- "setAskServiceClient:"
- "setCommunicationServiceClient:"
- "setDowntimeServiceClient:"
- "setSetupServiceClient:"
- "setWebContentFilterState:"
- "setupServiceClient"
- "simplified_agent"
- "v48@0:8q16@\"NSUUID\"24@\"NSNumber\"32@?<v@?@\"NSError\">40"
- "webContentFilterState"

```
