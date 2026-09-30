## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount`

```diff

-1007.230.0.0.0
-  __TEXT.__text: 0x1bb4d8
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0x8e54
-  __TEXT.__const: 0x44d50
-  __TEXT.__cstring: 0xbfc6
-  __TEXT.__oslogstring: 0xd774
-  __TEXT.__gcc_except_tab: 0x20d8
+1007.460.0.0.0
+  __TEXT.__text: 0x1bfc44
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x9e28
+  __TEXT.__const: 0x44d10
+  __TEXT.__cstring: 0xd10e
+  __TEXT.__oslogstring: 0xdbf9
+  __TEXT.__gcc_except_tab: 0x20a0
   __TEXT.__dlopen_cstrs: 0x287
-  __TEXT.__unwind_info: 0x2598
-  __TEXT.__eh_frame: 0xc0
-  __TEXT.__objc_classname: 0x1c35
-  __TEXT.__objc_methname: 0x133f4
-  __TEXT.__objc_methtype: 0x2ad1
-  __TEXT.__objc_stubs: 0xad00
-  __DATA_CONST.__got: 0xb28
-  __DATA_CONST.__const: 0x2160
-  __DATA_CONST.__objc_classlist: 0x730
+  __TEXT.__unwind_info: 0x2900
+  __TEXT.__eh_frame: 0xb8
+  __TEXT.__objc_classname: 0x1ca0
+  __TEXT.__objc_methname: 0x1388c
+  __TEXT.__objc_methtype: 0x2bae
+  __TEXT.__objc_stubs: 0xaf80
+  __DATA_CONST.__got: 0xb58
+  __DATA_CONST.__const: 0x2410
+  __DATA_CONST.__objc_classlist: 0x740
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4480
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x47a0
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x4c8
-  __AUTH_CONST.__const: 0xb510
-  __AUTH_CONST.__cfstring: 0xb0e0
-  __AUTH_CONST.__objc_const: 0x219e8
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__const: 0xb5d0
+  __AUTH_CONST.__cfstring: 0xb960
+  __AUTH_CONST.__objc_const: 0x20830
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x1e50
-  __DATA.__objc_ivar: 0xab0
-  __DATA.__data: 0x13f8
-  __DATA.__bss: 0x3e0
-  __DATA.__common: 0xa28
+  __AUTH.__objc_data: 0x1f10
+  __AUTH.__data: 0x28
+  __DATA.__objc_ivar: 0xac8
+  __DATA.__data: 0x1468
+  __DATA.__bss: 0x400
+  __DATA.__common: 0xa20
   __DATA_DIRTY.__objc_data: 0x2990
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8EAD76C1-09A5-3A75-8F59-009AE4316B02
-  Functions: 3983
-  Symbols:   9870
-  CStrings:  7824
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  UUID: FF85CD48-92F0-30A8-BEA0-F9C469754E35
+  Functions: 4272
+  Symbols:   10356
+  CStrings:  8029
 
Symbols:
+ +[AAAbsintheSigner _contextCreationBlock].cold.1
+ +[AAAbsintheSigner _setContextCreationBlock:].cold.1
+ +[AAAbsintheSigner sharedSigner].cold.1
+ +[AAAccountManager sharedManager].cold.1
+ +[AAAccountUserNotificationDaemonInterface XPCInterface].cold.1
+ +[AAAnalyticsRTCReporter reporter].cold.1
+ +[AACertificatePinner sharedPinner].cold.1
+ +[AACloudPolicyRestrictions _managedIcloudPolicyIdentifierForDataclass].cold.1
+ +[AACustodianDaemonInterface XPCInterface].cold.1
+ +[AACustodianUpdateRequestContext supportsSecureCoding]
+ +[AADataclassManager dataclassBundleMap].cold.1
+ +[AADataclassManager sharedManager].cold.1
+ +[AADeviceInfo currentInfo].cold.1
+ +[AADeviceInfo isInternalBuild].cold.1
+ +[AADeviceInfo isMultiUserMode].cold.1
+ +[AADeviceModelHelper isDeviceEqualTo:].cold.2
+ +[AAFlowPresenterHostInterface XPCInterface].cold.1
+ +[AALoginContextManager sharedManager].cold.1
+ +[AALoginContextTransientStorage sharedStorage].cold.1
+ +[AALoginPluginManager sharedInstance].cold.1
+ +[AAMessagingService sharedService].cold.1
+ +[AAPreferences customMaintenanceIntervalMinutes]
+ +[AAPreferences isCustomMaintenanceIntervalEnabled]
+ +[AAPreferences isLCInviteAcceptanceEnabled]
+ +[AAPreferences setCustomMaintenanceIntervalEnabled:]
+ +[AAPreferences setCustomMaintenanceIntervalMinutes:]
+ +[AAPreferences setLCInviteAcceptanceEnabled:]
+ +[AARemoteServer sharedServerWithNoUrlCache].cold.1
+ +[AARemoteServer sharedServer].cold.1
+ +[AAURLConfiguration remoteServer].cold.1
+ +[AAURLConfiguration setRemoteServer:].cold.1
+ +[AAURLProtocol canInitWithRequest:].cold.1
+ +[AAURLSession sharedPinningOnlySession].cold.1
+ +[AAURLSession sharedPinningSession].cold.1
+ +[AAURLSession sharedSessionWithNoUrlCache].cold.1
+ +[AAURLSession sharedSession].cold.1
+ +[AAURLSession sharedSigningSession].cold.1
+ +[AAURLSessionContext _relevantHTTPStatusCodes].cold.1
+ +[AAUniversalLinkHelper stringForBenefiaryMessagesURLWithUUID:].cold.1
+ +[AAUniversalLinkHelper stringForCustodianMessagesURLWithUUID:].cold.1
+ +[NSError(AppleAccount) aa_errorWithServerResponse:].cold.1
+ +[NSOperationQueue(AppleAccount) aa_operationQueueWithUnderlyingQueue:].cold.1
+ +[NSURL(AppleAccount) aa_URLWithEndpoint:].cold.1
+ -[AAAbsintheContext R6XtwiyjL3q2:error:].cold.2
+ -[AAAbsintheContext TgBfoO2wtF5L:error:].cold.2
+ -[AAAbsintheContext TgBfoO2wtF5L:error:].cold.3
+ -[AAAbsintheSigner _contextQueue_contextWithCompletion:].cold.1
+ -[AAAbsintheSigner _contextWithCompletion:].cold.1
+ -[AAAbsintheSigner signatureForData:completion:].cold.1
+ -[AAAccountUserNotificationDaemonConnection remoteObjectProxyWithErrorHandler:].cold.1
+ -[AAAccountUserNotificationDaemonConnection synchronousRemoteObjectProxyWithErrorHandler:].cold.1
+ -[AAAppleAccountInformationCache _deleteProfilePictureCache]
+ -[AAAppleAccountInformationCache _deleteProfilePictureCache].cold.1
+ -[AAAppleAccountInformationCache _deleteProfilePictureCache].cold.2
+ -[AAAppleAccountInformationCache _deleteProfilePictureCache].cold.3
+ -[AAAppleAccountInformationCache _fetchPrimaryAccountSignInState]
+ -[AAAppleAccountInformationCache _getProfilePictureCacheURL]
+ -[AAAppleAccountInformationCache _needsMigration]
+ -[AAAppleAccountInformationCache _needsMigration].cold.1
+ -[AAAppleAccountInformationCache _setSignedInState:]
+ -[AAAppleAccountInformationCache clearNonSecureAAPrefsDomain]
+ -[AAAppleAccountInformationCache clearNonSecureAAPrefsDomain].cold.1
+ -[AAAppleAccountInformationCache migrateToPrimaryAccountSignInState]
+ -[AAAppleAccountInformationCache primaryAccountSignInState]
+ -[AAAppleAccountInformationCache resetAccountInfoToSignedOutState]
+ -[AAAppleAccountInformationCache setFullName:]
+ -[AAAppleAccountInformationCache updateAccountInformationCacheForAppleAccount:]
+ -[AACustodianController availableRecoveryFactorsWithCompletion:].cold.1
+ -[AACustodianController cancelCustodianRecoveryWithContext:completion:]
+ -[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]
+ -[AACustodianController localContactsForCustodians:completion:]
+ -[AACustodianController removeCustodianWithContext:completion:]
+ -[AACustodianController stopBeingCustodianWithContext:completion:]
+ -[AACustodianDaemonConnection remoteObjectProxyWithErrorHandler:].cold.1
+ -[AACustodianDaemonConnection synchronousRemoteObjectProxyWithErrorHandler:].cold.1
+ -[AACustodianInvitationResponseContext altDSID]
+ -[AACustodianInvitationResponseContext setAltDSID:]
+ -[AACustodianInvitationResponseContext setTelemetryFlowID:]
+ -[AACustodianInvitationResponseContext telemetryFlowID]
+ -[AACustodianMessageInviteContext initWithLocalContact:custodianID:upsell:].cold.1
+ -[AACustodianRecoveryRequestContext isAccountRecovery]
+ -[AACustodianRecoveryRequestContext setIsAccountRecovery:]
+ -[AACustodianSetupRequestContext altDSID]
+ -[AACustodianSetupRequestContext setAltDSID:]
+ -[AACustodianSetupRequestContext setTelemetryFlowID:]
+ -[AACustodianSetupRequestContext telemetryFlowID]
+ -[AACustodianUpdateRequestContext .cxx_destruct]
+ -[AACustodianUpdateRequestContext altDSID]
+ -[AACustodianUpdateRequestContext custodianID]
+ -[AACustodianUpdateRequestContext encodeWithCoder:]
+ -[AACustodianUpdateRequestContext initWithCoder:]
+ -[AACustodianUpdateRequestContext initWithCustodianID:]
+ -[AACustodianUpdateRequestContext setAltDSID:]
+ -[AACustodianUpdateRequestContext setTelemetryFlowID:]
+ -[AACustodianUpdateRequestContext telemetryFlowID]
+ -[AADaemonController cacheLoginResponse:forAccount:completion:].cold.1
+ -[AADaemonController cacheLoginResponse:forAccount:completion:].cold.2
+ -[AADaemonController fetchCachedLoginResponseForAccount:completion:].cold.1
+ -[AADaemonController handleAppleAccountDeleteForAccount:completion:].cold.1
+ -[AADaemonController handleAppleAccountDeleteForAccount:completion:].cold.2
+ -[AADataclassManager _filteredDataclassesForAccountClass:].cold.1
+ -[AADataclassManager _shouldProvisionNotesForAccount:].cold.2
+ -[AADataclassManager _shouldProvisionRemindersForAccount:].cold.2
+ -[AADataclassManager _shouldShowDataclassWhenAppIsRemoved:].cold.1
+ -[AADataclassManager canAutoEnableDataclass:forAccount:].cold.1
+ -[AADataclassManager canAutoEnableDataclass:forAccount:].cold.2
+ -[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:].cold.1
+ -[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:].cold.2
+ -[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:].cold.3
+ -[AADataclassManager filteredServerProvidedFeatures:forAccount:].cold.2
+ -[AADataclassManager filteredServerProvidedFeatures:forAccount:].cold.3
+ -[AADataclassManager shouldProvisionDataclass:forAccount:].cold.1
+ -[AADataclassManager shouldProvisionDataclass:forAccount:].cold.2
+ -[AADependentAuthenticationUIRequest initWithAltDSID:].cold.1
+ -[AADeviceProvisioningSession initWithAccount:].cold.1
+ -[AAFollowUpController dismissFollowUpWithIdentifier:completion:].cold.1
+ -[AAFollowUpController dismissFollowUpWithIdentifier:error:].cold.2
+ -[AAFollowUpController pendingFollowUpWithIdentifier:completion:].cold.1
+ -[AAFollowUpController pendingFollowUpWithIdentifier:completion:].cold.2
+ -[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:].cold.3
+ -[AAFollowUpController postFollowUpWithIdentifier:userInfo:error:].cold.4
+ -[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:].cold.1
+ -[AAFollowUpController(Convenience) _pendingFollowUpItemsWithIdentifier:forAccount:completion:].cold.1
+ -[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:].cold.1
+ -[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:].cold.2
+ -[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:].cold.1
+ -[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:].cold.2
+ -[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:].cold.3
+ -[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:].cold.2
+ -[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:].cold.1
+ -[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:].cold.2
+ -[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:].cold.1
+ -[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:].cold.2
+ -[AAFollowUpController(Convenience) postFollowUpWithIdentifier:forAccount:userInfo:completion:].cold.1
+ -[AAFollowUpController(Convenience) postFollowUpWithIdentifier:forAccount:userInfo:completion:].cold.2
+ -[AAInheritanceController fetchAllHealthInfoWithCompletion:].cold.1
+ -[AAInheritanceController fetchBenefactorsWithCompletion:].cold.1
+ -[AAInheritanceController fetchBeneficiariesWithCompletion:].cold.1
+ -[AAInheritanceController fetchInvitationWithBeneficiaryID:completion:].cold.1
+ -[AAInheritanceController fetchInvitationsWithCompletion:].cold.1
+ -[AAInheritanceController fetchManifestOptionsForContact:completion:].cold.1
+ -[AAInheritanceController fetchManifestOptionsForContact:completion:].cold.2
+ -[AAInheritanceController fetchSuggestedBeneficiariesWithCompletion:].cold.1
+ -[AAInheritanceController isRecipient:capableOf:completion:].cold.1
+ -[AAInheritanceController isRecipient:capableOf:completion:].cold.2
+ -[AAInheritanceController isRecipient:capableOf:completion:].cold.3
+ -[AAInheritanceController presentInheritanceInvitationUIWithBeneficiaryID:completion:].cold.1
+ -[AAInheritanceController presentInheritanceInvitationUIWithBeneficiaryID:completion:].cold.2
+ -[AAInheritanceController removeAccessCodeForContactInfo:completion:].cold.1
+ -[AAInheritanceController removeAccessCodeForContactInfo:completion:].cold.2
+ -[AAInheritanceController removeBenefactor:completion:].cold.1
+ -[AAInheritanceController removeBenefactor:completion:].cold.2
+ -[AAInheritanceController removeBeneficiary:manifest:completion:].cold.1
+ -[AAInheritanceController removeBeneficiary:manifest:completion:].cold.2
+ -[AAInheritanceController removeInvitation:completion:].cold.1
+ -[AAInheritanceController respondToInvitation:accepted:completion:].cold.1
+ -[AAInheritanceController sendInvitationToContact:completion:].cold.1
+ -[AAInheritanceController sendInvitationToContact:completion:].cold.2
+ -[AAInheritanceController setupBeneficiaryAliasWithAccessKey:password:firstName:lastName:authToken:completion:].cold.1
+ -[AAInheritanceController setupBeneficiaryAliasWithAccessKey:password:firstName:lastName:authToken:completion:].cold.2
+ -[AAInheritanceController setupBeneficiaryAliasWithAccessKey:password:firstName:lastName:authToken:completion:].cold.3
+ -[AAInheritanceController setupBeneficiaryAliasWithAccessKey:password:firstName:lastName:authToken:completion:].cold.4
+ -[AAInheritanceController setupBeneficiaryManifest:contactInfo:setupAuthToken:completion:].cold.1
+ -[AAInheritanceController setupBeneficiaryManifest:contactInfo:setupAuthToken:completion:].cold.2
+ -[AAInheritanceController setupBeneficiaryManifest:contactInfo:setupAuthToken:completion:].cold.3
+ -[AAInheritanceController setupBeneficiaryManifest:contactInfo:setupAuthToken:completion:].cold.4
+ -[AAInheritanceController updateAccessCodeForContactInfo:completion:].cold.1
+ -[AAInheritanceController updateAccessCodeForContactInfo:completion:].cold.2
+ -[AAInheritanceController updateBeneficiaryManifest:contactInfo:completion:].cold.1
+ -[AAInheritanceController updateBeneficiaryManifest:contactInfo:completion:].cold.2
+ -[AAInheritanceController updateBeneficiaryManifest:contactInfo:completion:].cold.3
+ -[AAInheritanceMessageInviteContext initWithLocalContact:beneficiaryID:].cold.2
+ -[AAMessagingDestination description]
+ -[AAMessagingDestination initWithHandle:].cold.5
+ -[AAMessagingDestination initWithHandle:].cold.6
+ -[AAMessagingService _optionsDictionaryWithResponseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:sendFromHandleUri:]
+ -[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:]
+ -[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:].cold.1
+ -[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:].cold.2
+ -[AAPendingIDSMessage initCustodianMessageFrom:data:sentToHandleUri:]
+ -[AAPendingIDSMessage initInheritanceMessageFrom:data:sentToHandleUri:]
+ -[AAPendingIDSMessage sentToHandleUri]
+ -[AAPrimaryAccountUpdater initWithAccount:].cold.1
+ -[AARemoteServer _fetchConfigurationAndResponseWithCompletion:].cold.1
+ -[AARemoteServer configurationWithCompletion:].cold.2
+ -[AARemoteServer(Deprecated) authenticateAccount:completion:].cold.1
+ -[AARemoteServer(Deprecated) authenticateAccount:completion:].cold.2
+ -[AARemoteServer(Deprecated) loginDelegates:parameters:completion:].cold.1
+ -[AARemoteServer(Deprecated) loginDelegates:parameters:completion:].cold.2
+ -[AARemoteServer(Deprecated) registerAccount:withHSA:completion:].cold.1
+ -[AARemoteServer(Deprecated) registerAccount:withHSA:completion:].cold.2
+ -[AARemoteServerConfigurationCache initWithConfiguration:response:].cold.1
+ -[AARemoteServerConfigurationCache initWithConfiguration:response:].cold.2
+ -[AASecondaryAuthenticationRequest initWithDSID:primaryToken:].cold.1
+ -[AASecondaryAuthenticationRequest initWithDSID:primaryToken:].cold.2
+ -[AASetupAssistantService _doHSADeviceProvisioningSynchronizationWithDSID:data:].cold.1
+ -[AASetupAssistantService _doHSADeviceProvisioningSynchronizationWithDSID:data:].cold.2
+ -[AASetupAssistantService _doHSADeviceProvisioningWithDSID:data:].cold.1
+ -[AASetupAssistantService _doHSADeviceProvisioningWithDSID:data:].cold.2
+ -[AASetupAssistantService _doHSADeviceReprovisioningWithDSID:].cold.1
+ -[AASignOutFlowController _delegate_startSignOutFlowForAccount:completion:]
+ -[AASignOutFlowController _delegate_startSignOutFlowForAccount:completion:].cold.1
+ -[AASignOutFlowController _startSignOutOfferFlow:completion:]
+ -[AASignOutFlowController _startSignOutOfferFlow:completion:].cold.1
+ -[AASignOutFlowController isBetterSignOutFeatureEnabled]
+ -[AASignOutFlowController signOutAppleAccount:completion:].cold.1
+ -[AAURLConfiguration initWithDictionary:].cold.1
+ -[AAURLConfiguration preProxTermsEnabled]
+ -[AAURLProtocol _normalizedRequestForURL:].cold.1
+ -[AAURLProtocol initWithRequest:cachedResponse:client:].cold.1
+ -[AAURLProtocol startLoading].cold.1
+ -[AAURLProtocol stopLoading].cold.1
+ -[AAURLSession URLSession:dataTask:didReceiveData:].cold.1
+ -[AAURLSession URLSession:dataTask:didReceiveData:].cold.2
+ -[AAURLSession URLSession:dataTask:didReceiveData:].cold.3
+ -[AAURLSession URLSession:didBecomeInvalidWithError:].cold.1
+ -[AAURLSession URLSession:didBecomeInvalidWithError:].cold.2
+ -[AAURLSession URLSession:task:didCompleteWithError:].cold.1
+ -[AAURLSession URLSession:task:didCompleteWithError:].cold.2
+ -[AAURLSession _enqueueRequest:completion:].cold.1
+ -[AAURLSession _enqueueRequest:completion:].cold.2
+ -[AAURLSession _initRequiringSigning:requiresPinning:requiresUrlCache:].cold.1
+ -[AAURLSession _sessionQueue_dequeueTask:withResponse:error:].cold.2
+ -[AAURLSession _sessionQueue_dequeueTask:withResponse:error:].cold.3
+ -[AAURLSession _sessionQueue_enqueueTask:completion:].cold.2
+ -[AAURLSession _sessionQueue_enqueueTask:completion:].cold.3
+ -[AAURLSession _sessionQueue_updateTask:withData:].cold.1
+ -[AAURLSession _sessionQueue_updateTask:withData:].cold.2
+ -[AAURLSession bodyTaskWithRequest:completion:].cold.1
+ -[AAURLSession bodyTaskWithRequest:completion:].cold.2
+ -[AAURLSession bodyTaskWithURL:completion:].cold.1
+ -[AAURLSession bodyTaskWithURL:completion:].cold.2
+ -[AAURLSession dataTaskWithRequest:completion:].cold.1
+ -[AAURLSession dataTaskWithRequest:completion:].cold.2
+ -[AAURLSession dataTaskWithURL:completion:].cold.2
+ -[AAURLSession dataTaskWithURL:completion:].cold.3
+ -[AAURLSession initForProxiedDevice:anisetteDataProvider:].cold.1
+ -[AAURLSessionContext URLSession:task:getAppleIDHeadersForResponse:completionHandler:].cold.1
+ -[AAURLSessionContext URLSession:task:getAppleIDHeadersForResponse:completionHandler:].cold.2
+ -[AAURLSessionContext _additionalHeadersForRequest:completion:].cold.1
+ -[AAVersionUpdater _performVersionUpdate:].cold.1
+ -[ACAccount(AADOBRepairState) aa_needsDOBRepair]
+ -[ACAccount(AADOBRepairState_Internal) aa_dobRepairState]
+ -[ACAccount(AADOBRepairState_Internal) aa_setDOBRepairState:]
+ -[ACAccount(AppleAccount) aa_setAccountClass:].cold.2
+ -[ACAccount(AppleAccount) aa_updateWithProvisioningResponse:].cold.1
+ -[NSArray(AppleAccount) aa_filter:].cold.1
+ -[NSArray(AppleAccount) aa_firstObjectPassingTest:].cold.1
+ -[NSArray(AppleAccount) aa_map:].cold.1
+ -[NSArray(AppleAccount) aa_mapNullable:].cold.1
+ -[NSDictionary(AppleAccount) aa_dictionaryByAddingEntriesFromDictionary:].cold.1
+ -[NSString(AAMessage) _phoneNumberDetector].cold.1
+ -[NSString(AppleAccount) aa_base64String].cold.1
+ -[NSURLSessionConfiguration(AppleAccount) aa_registerProtocolClass:].cold.1
+ -[NSURLSessionConfiguration(AppleAccount) aa_unregisterProtocolClass:].cold.1
+ -[_AABasicGetRequest urlRequest].cold.1
+ -[_AAURLSessionConfigurationTask _initiateSessionTaskWithConfiguration:].cold.3
+ -[_AAURLSessionConfigurationTask _invokeCompletionWithData:response:error:].cold.1
+ -[_AAURLSessionConfigurationTask initWithSession:request:completion:].cold.1
+ -[_AAURLSessionConfigurationTask initWithSession:request:completion:].cold.2
+ -[_AAURLSessionConfigurationTask initWithSession:request:completion:].cold.3
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table132
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table25
+ GCC_except_table65
+ GCC_except_table78
+ GCC_except_table89
+ GCC_except_table93
+ GCC_except_table97
+ OBJC_IVAR_$_AACustodianInvitationResponseContext._altDSID
+ OBJC_IVAR_$_AACustodianInvitationResponseContext._telemetryFlowID
+ OBJC_IVAR_$_AACustodianRecoveryRequestContext._isAccountRecovery
+ OBJC_IVAR_$_AACustodianSetupRequestContext._altDSID
+ OBJC_IVAR_$_AACustodianSetupRequestContext._telemetryFlowID
+ OBJC_IVAR_$_AACustodianUpdateRequestContext._altDSID
+ OBJC_IVAR_$_AACustodianUpdateRequestContext._custodianID
+ OBJC_IVAR_$_AACustodianUpdateRequestContext._telemetryFlowID
+ OBJC_IVAR_$_AAPendingIDSMessage._sentToHandleUri
+ _AAAccountStoreLogSystem.cold.1
+ _AAAgeAttestationErrorDomain
+ _AACustodianSystemStateErrorDomain
+ _AADeviceListLogSystem.cold.1
+ _AAFollowUpIdentifierChildProtoConnect
+ _AALogSystem.cold.1
+ _AANotificationHandlerMap.cold.1
+ _AANotificationQueue.cold.1
+ _AASignOutLogSystem.cold.1
+ _AASignOutLogSystem.log
+ _AASignOutLogSystem.onceToken
+ _AASignpostGetNanoseconds.cold.1
+ _AASignpostLogSystem.cold.1
+ _AAURLSessionCreateSession.cold.1
+ _AAURLSessionCreateSession.cold.2
+ _CFNumberCreate
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _OBJC_CLASS_$_AACustodianUpdateRequestContext
+ _OBJC_CLASS_$_AADOBRepairStateUpdater
+ _OBJC_METACLASS_$_AACustodianUpdateRequestContext
+ _OBJC_METACLASS_$_AADOBRepairStateUpdater
+ _PROTOCOLS_AADOBRepairStateUpdater.2
+ __53-[AACustodianController repairCustodians:completion:]_block_invoke.138
+ __53-[AACustodianController repairCustodians:completion:]_block_invoke.138.cold.1
+ __53-[AACustodianController repairCustodians:completion:]_block_invoke.139
+ __53-[AACustodianController repairCustodians:completion:]_block_invoke.139.cold.1
+ __56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.106
+ __56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.106.cold.1
+ __56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.107
+ __56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.107.cold.1
+ __58-[AASignOutFlowController signOutAppleAccount:completion:]_block_invoke.35
+ __58-[AASignOutFlowController signOutAppleAccount:completion:]_block_invoke.35.cold.1
+ __58-[AASignOutFlowController signOutAppleAccount:completion:]_block_invoke.42
+ __60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.46
+ __60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.46.cold.1
+ __61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.110
+ __61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.110.cold.1
+ __61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.111
+ __61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.111.cold.1
+ __62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.48
+ __62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.48.cold.1
+ __63-[AACustodianController localContactsForCustodians:completion:]_block_invoke.142
+ __63-[AACustodianController localContactsForCustodians:completion:]_block_invoke.145
+ __63-[AACustodianController localContactsForCustodians:completion:]_block_invoke.cold.1
+ __63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.36
+ __63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.36.cold.1
+ __63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.37
+ __63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.37.cold.1
+ __63-[AAURLSessionContext _additionalHeadersForRequest:completion:]_block_invoke.cold.1
+ __64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.134
+ __64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.134.cold.1
+ __64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.135
+ __64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.135.cold.1
+ __64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.116
+ __64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.116.cold.1
+ __64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.117
+ __64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.117.cold.1
+ __64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.57
+ __64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.57.cold.1
+ __65-[AASignOutFlowController _preflightSignOutOfAccount:completion:]_block_invoke.48
+ __66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke.42
+ __66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke.42.cold.1
+ __66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.63
+ __66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.63.cold.1
+ __66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.140
+ __66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.140.cold.1
+ __66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.141
+ __66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.141.cold.1
+ __66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.25
+ __66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.25.cold.1
+ __66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.27
+ __66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.27.cold.1
+ __66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.38
+ __66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.38.cold.1
+ __66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.39
+ __66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.39.cold.1
+ __67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.53
+ __67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.53.cold.1
+ __70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.108
+ __70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.108.cold.1
+ __70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.109
+ __70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.109.cold.1
+ __70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.67
+ __70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.67.cold.1
+ __71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.98
+ __71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.98.cold.1
+ __71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.99
+ __71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.114
+ __71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.114.cold.1
+ __71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.115
+ __71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.115.cold.1
+ __71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.112
+ __71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.112.cold.1
+ __71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.113
+ __73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.61
+ __73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.61.cold.1
+ __74-[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]_block_invoke.95
+ __74-[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]_block_invoke.95.cold.1
+ __74-[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]_block_invoke.cold.1
+ __74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.33
+ __74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.33.cold.1
+ __75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.71
+ __75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.71.cold.1
+ __75-[AASignOutFlowController _delegate_startSignOutFlowForAccount:completion:]_block_invoke_2.cold.1
+ __77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.72
+ __77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.75
+ __77-[AACustodianController reSendCustodianInvitationWithCustodianID:completion:]_block_invoke.120
+ __77-[AACustodianController reSendCustodianInvitationWithCustodianID:completion:]_block_invoke.120.cold.1
+ __88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.103
+ __88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.103.cold.1
+ __AASignOutLogSystem
+ __Block_copy
+ __Block_release
+ __DATA_AADOBRepairStateUpdater
+ __INSTANCE_METHODS_AADOBRepairStateUpdater
+ __METACLASS_DATA_AADOBRepairStateUpdater
+ __OBJC_$_CATEGORY_ACAccount_$_AADOBRepairState
+ __OBJC_$_CLASS_METHODS_AACustodianUpdateRequestContext
+ __OBJC_$_CLASS_PROP_LIST_AACustodianUpdateRequestContext
+ __OBJC_$_INSTANCE_METHODS_AACustodianUpdateRequestContext
+ __OBJC_$_INSTANCE_METHODS_ACAccount(AADOBRepairState|AADOBRepairState_Internal|AppleID|AppleIDInternal|AppleAccount|AppleAccount_Deprecated|AppleAccount_Internal)
+ __OBJC_$_INSTANCE_VARIABLES_AACustodianUpdateRequestContext
+ __OBJC_$_PROP_LIST_AACustodianUpdateRequestContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AADOBRepairStateUpdaterProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AADOBRepairStateUpdaterProtocol
+ __OBJC_$_PROTOCOL_REFS_AADOBRepairStateUpdaterProtocol
+ __OBJC_CLASS_PROTOCOLS_$_AACustodianUpdateRequestContext
+ __OBJC_CLASS_RO_$_AACustodianUpdateRequestContext
+ __OBJC_LABEL_PROTOCOL_$_AADOBRepairStateUpdaterProtocol
+ __OBJC_METACLASS_RO_$_AACustodianUpdateRequestContext
+ __OBJC_PROTOCOL_$_AADOBRepairStateUpdaterProtocol
+ __PROTOCOLS_AADOBRepairStateUpdater
+ ___145-[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:]_block_invoke
+ ___40-[AAContactsProvider fetchMyCustodians:]_block_invoke_2
+ ___46-[AAContactsProvider fetchMyCachedCustodians:]_block_invoke_2
+ ___47-[AAContactsProvider fetchMyHealthyCustodians:]_block_invoke_2
+ ___54-[AAContactsProvider fetchMyWalrusEligibleCustodians:]_block_invoke_2
+ ___63-[AACustodianController localContactsForCustodians:completion:]_block_invoke
+ ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke
+ ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke
+ ___71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke
+ ___74-[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]_block_invoke
+ ___75-[AASignOutFlowController _delegate_startSignOutFlowForAccount:completion:]_block_invoke
+ ___75-[AASignOutFlowController _delegate_startSignOutFlowForAccount:completion:]_block_invoke_2
+ ___85-[AAContactsProvider fetchWalrusEligibleCustodiansForExpansionCohortsWithCompletion:]_block_invoke_2
+ ____AASignOutLogSystem_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48bs_e17_v16?0"NSError"8l
+ ___block_descriptor_80_e8_32s40s48bs56r_e17_v16?0"NSError"8l
+ ___block_descriptor_80_e8_32s40s48bs56r_e28_v24?0"NSUUID"8"NSError"16l
+ ___block_descriptor_80_e8_32s40s48bs56r_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_80_e8_32s40s48bs56r_e49_v24?0"AACustodianDataRecoveryKeys"8"NSError"16l
+ ___getIDSSendMessageOptionFromIDKeySymbolLoc_block_invoke
+ ___swift_reflection_version
+ __block_literal_global.37
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_AppleAccount
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_AppleAccount
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_AppleAccount
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_AppleAccount
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_AppleAccount
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_AppleAccount
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_AppleAccount
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_AppleAccount
+ _getIDSSendMessageOptionFromIDKey
+ _getIDSSendMessageOptionFromIDKeySymbolLoc
+ _kAAAccountDOBRepairStateKey
+ _kAAAnalyticsEventCustodianDecodeIDSMessage
+ _kAAAnalyticsEventCustodianExitAccountRecoveryScreen
+ _kAAAnalyticsEventCustodianExitCustodianDetails
+ _kAAAnalyticsEventCustodianHealthCheckCustodian
+ _kAAAnalyticsEventCustodianHealthCheckIncompleteInvitationResendInvitationAcceptanceMessage
+ _kAAAnalyticsEventCustodianHealthCheckOwner
+ _kAAAnalyticsEventCustodianHealthCheckOwnerConfirmCustodianWithServer
+ _kAAAnalyticsEventCustodianHealthCheckOwnerFinalizeSetupWithServer
+ _kAAAnalyticsEventCustodianHealthCheckOwnerSendRecoveryInfoMessage
+ _kAAAnalyticsEventCustodianHealthCheckOwnerUpdatedCustodianRecord
+ _kAAAnalyticsEventCustodianOpenAccountRecoveryScreen
+ _kAAAnalyticsEventCustodianOpenCustodianDetails
+ _kAAAnalyticsEventCustodianRecoveryCancel
+ _kAAAnalyticsEventCustodianRecoveryExperimentalHasCachedCustodianList
+ _kAAAnalyticsEventCustodianRecoveryFetchAPSToken
+ _kAAAnalyticsEventCustodianRecoveryInitializeWithServer
+ _kAAAnalyticsEventCustodianRecoveryOwnerCreateSession
+ _kAAAnalyticsEventCustodianRecoveryOwnerFetchCustodianRecoveryKeys
+ _kAAAnalyticsEventCustodianRecoveryOwnerValidateCode
+ _kAAAnalyticsEventCustodianSetupAcceptSharedRecoveryInfo
+ _kAAAnalyticsEventCustodianSetupAccountEligibilityCheck
+ _kAAAnalyticsEventCustodianSetupAccountNotEligible
+ _kAAAnalyticsEventCustodianSetupCleanupDeleteCustodianshipRecordFromCloud
+ _kAAAnalyticsEventCustodianSetupCleanupDeleteRecoveryKeyByCustodianIDFromSecurity
+ _kAAAnalyticsEventCustodianSetupCleanupDeleteRecoveryKeyByOctagonIDFromSecurity
+ _kAAAnalyticsEventCustodianSetupCleanupRevokeCustodianFromServer
+ _kAAAnalyticsEventCustodianSetupCustodianUpdatedCustodianshipRecord
+ _kAAAnalyticsEventCustodianSetupFamilyMemberCheck
+ _kAAAnalyticsEventCustodianSetupFinalizeSetupWithServer
+ _kAAAnalyticsEventCustodianSetupInvitationProcessedForManualAccept
+ _kAAAnalyticsEventCustodianSetupNewCustodian
+ _kAAAnalyticsEventCustodianSetupOwnerGenerateCustodianRecoveryKey
+ _kAAAnalyticsEventCustodianSetupOwnerGenerateEncryptedCPRK
+ _kAAAnalyticsEventCustodianSetupOwnerRemovedCustodian
+ _kAAAnalyticsEventCustodianSetupOwnerStoredCustodianRecordToCloud
+ _kAAAnalyticsEventCustodianSetupOwnerUpdatedCustodianRecord
+ _kAAAnalyticsEventCustodianSetupProcessAcceptCreateRecoveryInfoShare
+ _kAAAnalyticsEventCustodianSetupProcessAcceptFetchRecoveryInfo
+ _kAAAnalyticsEventCustodianSetupProcessAcceptSendRecoveryInfoMessage
+ _kAAAnalyticsEventCustodianSetupProcessDeclineCleanup
+ _kAAAnalyticsEventCustodianSetupProcessFinalizeSetupMessage
+ _kAAAnalyticsEventCustodianSetupProcessInvitation
+ _kAAAnalyticsEventCustodianSetupProcessInvitationAcceptanceResponse
+ _kAAAnalyticsEventCustodianSetupProcessInvitationDeclineResponse
+ _kAAAnalyticsEventCustodianSetupProcessNotReachable
+ _kAAAnalyticsEventCustodianSetupProcessRemoveCustodian
+ _kAAAnalyticsEventCustodianSetupProcessSharedRecoveryInfo
+ _kAAAnalyticsEventCustodianSetupResendInvitation
+ _kAAAnalyticsEventCustodianSetupRespondToInvite
+ _kAAAnalyticsEventCustodianSetupSendAutoAcceptInvitationMessage
+ _kAAAnalyticsEventCustodianSetupSendFinalizeSetupMessage
+ _kAAAnalyticsEventCustodianSetupSendInvitation
+ _kAAAnalyticsEventCustodianSetupSendInvitationAcceptanceMessage
+ _kAAAnalyticsEventCustodianSetupSendInvitationDeclineMessage
+ _kAAAnalyticsEventCustodianSetupSendRemovalMessageToCustodian
+ _kAAAnalyticsEventCustodianSetupStopBeingCustodian
+ _kAAAnalyticsEventCustodianSetupStoreInvitationToCloud
+ _kAAAnalyticsEventCustodianSystemSync
+ _kAAAnalyticsEventFetchUserInfo
+ _kAAAnalyticsPRKPresence
+ _kAAProtocolPrefCustomMaintenanceIntervalEnabled
+ _kAAProtocolPrefCustomMaintenanceIntervalMinutes
+ _kAAProtocolPrefLCInviteAcceptance
+ _kAAProtocolPrimaryAccountSignInStateKey
+ _kCFBooleanFalse
+ _objc_allocWithZone
+ _objc_msgSend$_delegate_startSignOutFlowForAccount:completion:
+ _objc_msgSend$_deleteProfilePictureCache
+ _objc_msgSend$_fetchPrimaryAccountSignInState
+ _objc_msgSend$_getProfilePictureCacheURL
+ _objc_msgSend$_needsMigration
+ _objc_msgSend$_optionsDictionaryWithResponseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:sendFromHandleUri:
+ _objc_msgSend$_setSignedInState:
+ _objc_msgSend$_startSignOutOfferFlow:completion:
+ _objc_msgSend$aa_fullName
+ _objc_msgSend$cancelCustodianRecoveryWithContext:completion:
+ _objc_msgSend$clearNonSecureAAPrefsDomain
+ _objc_msgSend$fetchCustodianRecoveryKeysWithContext:completion:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$initCustodianMessageFrom:data:sentToHandleUri:
+ _objc_msgSend$initInheritanceMessageFrom:data:sentToHandleUri:
+ _objc_msgSend$initWithCustodianID:
+ _objc_msgSend$isBetterSignOutFeatureEnabled
+ _objc_msgSend$localContactsForCustodians:completion:
+ _objc_msgSend$messageService:didReceiveMessage:fromID:sentToHandleUri:
+ _objc_msgSend$primaryAccountSignInState
+ _objc_msgSend$removeCustodianWithContext:completion:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$sentToHandleUri
+ _objc_msgSend$setFullName:
+ _objc_msgSend$setRecoverySessionID:
+ _objc_msgSend$setType:
+ _objc_msgSend$signOutFlowController:startSignOutForAccount:completion:
+ _objc_msgSend$stopBeingCustodianWithContext:completion:
+ _objc_opt_self
+ _swift_bridgeObjectRelease
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ getIDSSendMessageOptionFromIDKey.cold.1
+ getIDSSendMessageOptionFromIDKeySymbolLoc.ptr
- +[AAPreferences isAppleAccountInformationCacheEnabled]
- -[AAAppleAccountInformationCache .cxx_destruct]
- -[AAMessagingService _optionsDictionaryWithResponseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:]
- -[AAMessagingService sendMessage:destinations:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:]
- -[AAMessagingService sendMessage:destinations:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:].cold.1
- -[AAMessagingService sendMessage:destinations:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:].cold.2
- -[AAPendingIDSMessage initCustodianMessageFrom:data:]
- -[AAPendingIDSMessage initInheritanceMessageFrom:data:]
- -[AASignOutFlowController _preflightSignOutOfAccount:completion:].cold.1
- GCC_except_table103
- GCC_except_table107
- GCC_except_table111
- GCC_except_table115
- GCC_except_table118
- GCC_except_table123
- GCC_except_table19
- GCC_except_table58
- GCC_except_table61
- GCC_except_table74
- GCC_except_table81
- GCC_except_table84
- GCC_except_table88
- GCC_except_table91
- GCC_except_table95
- GCC_except_table99
- OBJC_IVAR_$_AAAppleAccountInformationCache._accountFullName
- OBJC_IVAR_$_AAAppleAccountInformationCache._isSignedIn
- OBJC_IVAR_$_AAAppleAccountInformationCache._profilePictureCacheURL
- _OUTLINED_FUNCTION_8
- __52-[AACustodianController removeCustodian:completion:]_block_invoke.33
- __52-[AACustodianController removeCustodian:completion:]_block_invoke.33.cold.1
- __52-[AACustodianController removeCustodian:completion:]_block_invoke.34
- __52-[AACustodianController removeCustodian:completion:]_block_invoke.34.cold.1
- __53-[AACustodianController repairCustodians:completion:]_block_invoke.132
- __53-[AACustodianController repairCustodians:completion:]_block_invoke.132.cold.1
- __53-[AACustodianController repairCustodians:completion:]_block_invoke.133
- __53-[AACustodianController repairCustodians:completion:]_block_invoke.133.cold.1
- __55-[AACustodianController stopBeingCustodian:completion:]_block_invoke.35
- __55-[AACustodianController stopBeingCustodian:completion:]_block_invoke.35.cold.1
- __55-[AACustodianController stopBeingCustodian:completion:]_block_invoke.36
- __55-[AACustodianController stopBeingCustodian:completion:]_block_invoke.36.cold.1
- __56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.100
- __56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.100.cold.1
- __56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.101
- __56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.101.cold.1
- __58-[AASignOutFlowController signOutAppleAccount:completion:]_block_invoke.41
- __58-[AASignOutFlowController signOutAppleAccount:completion:]_block_invoke_2.cold.1
- __60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.44
- __60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.44.cold.1
- __61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.104
- __61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.104.cold.1
- __61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.105
- __61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.105.cold.1
- __62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.46
- __62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.46.cold.1
- __64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.128
- __64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.128.cold.1
- __64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.129
- __64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.129.cold.1
- __64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.110
- __64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.110.cold.1
- __64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.111
- __64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.111.cold.1
- __64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.55
- __64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.55.cold.1
- __65-[AASignOutFlowController _preflightSignOutOfAccount:completion:]_block_invoke.45
- __66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke.40
- __66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke.40.cold.1
- __66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.61
- __66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.61.cold.1
- __66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.134
- __66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.134.cold.1
- __66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.135
- __66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.135.cold.1
- __66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.24
- __66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.24.cold.1
- __66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.26
- __66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.26.cold.1
- __67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.51
- __67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.51.cold.1
- __68-[AACustodianController cancelCustodianRecoveryWithSessionID:error:]_block_invoke.cold.1
- __70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.102
- __70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.102.cold.1
- __70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.103
- __70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.103.cold.1
- __70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.66
- __70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.66.cold.1
- __71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.108
- __71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.108.cold.1
- __71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.109
- __71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.109.cold.1
- __71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.106
- __71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.106.cold.1
- __71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.107
- __73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.59
- __73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.59.cold.1
- __74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.31
- __74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.31.cold.1
- __75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.70
- __75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.70.cold.1
- __76-[AACustodianController fetchCustodianRecoveryKeysWithSessionID:completion:]_block_invoke.95
- __76-[AACustodianController fetchCustodianRecoveryKeysWithSessionID:completion:]_block_invoke.95.cold.1
- __76-[AACustodianController fetchCustodianRecoveryKeysWithSessionID:completion:]_block_invoke.cold.1
- __77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.71
- __77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.74
- __77-[AACustodianController reSendCustodianInvitationWithCustodianID:completion:]_block_invoke.114
- __77-[AACustodianController reSendCustodianInvitationWithCustodianID:completion:]_block_invoke.114.cold.1
- __88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.99
- __88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.99.cold.1
- __OBJC_$_CATEGORY_ACAccount_$_AppleID
- __OBJC_$_INSTANCE_METHODS_ACAccount(AppleID|AppleIDInternal|AppleAccount|AppleAccount_Deprecated|AppleAccount_Internal)
- __OBJC_$_INSTANCE_VARIABLES_AAAppleAccountInformationCache
- ___127-[AAMessagingService sendMessage:destinations:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:]_block_invoke
- ___52-[AACustodianController removeCustodian:completion:]_block_invoke
- ___55-[AACustodianController stopBeingCustodian:completion:]_block_invoke
- ___76-[AACustodianController fetchCustodianRecoveryKeysWithSessionID:completion:]_block_invoke
- ___block_descriptor_64_e8_32bs40r_e28_v24?0"NSUUID"8"NSError"16l
- ___block_descriptor_64_e8_32bs40r_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_64_e8_32bs40r_e49_v24?0"AACustodianDataRecoveryKeys"8"NSError"16l
- _kAAAnalyticsEventCustodianRecovery
- _objc_msgSend$_localContactsForCustodians:
- _objc_msgSend$_optionsDictionaryWithResponseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:
- _objc_msgSend$cancelCustodianRecoveryWithSessionID:error:
- _objc_msgSend$initCustodianMessageFrom:data:
- _objc_msgSend$initInheritanceMessageFrom:data:
- _objc_msgSend$messageService:didReceiveMessage:fromID:
- _objc_msgSend$removeCustodian:completion:
- _objc_msgSend$stopBeingCustodian:completion:
CStrings:
+ "%s Initializing with email uri"
+ "%s Initializing with phone number uri"
+ "/System/AppleInternal/Library/Frameworks/Contacts.framework/Contacts"
+ "/System/AppleInternal/Library/Frameworks/IDS.framework/IDS"
+ "@\"NSUUID\"76@0:8@\"NSData\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40B48@\"NSSet\"52@\"NSSet\"60^@68"
+ "@52@0:8@16B24@28@36@44"
+ "@76@0:8@16@24@32@40B48@52@60^@68"
+ "AAAgeAttestationErrors"
+ "AAAppleAccountInformationCache - Reset to signed out state."
+ "AACustodianSystemStateError"
+ "AACustodianUpdateRequestContext"
+ "AACustomMaintenanceIntervalEnabled"
+ "AACustomMaintenanceIntervalMinutes"
+ "AADOBRepairState"
+ "AADOBRepairStateUpdater"
+ "AADOBRepairStateUpdaterProtocol"
+ "AADOBRepairState_Internal"
+ "AALCInviteAcceptance"
+ "AAPrimaryAccountSignInState"
+ "AASignOuFlowController: Error starting the sign out flow"
+ "AASignOutFlowController: Calling delegate to start Sign Out/Erase flow for account: %@"
+ "AASignOutFlowController: Delegate (%@) does not respond to selector startSignOutForAccount. Proceeding with Sign Out flow."
+ "AASignOutFlowController: SignOut start failed to completed with error: %@"
+ "Account sign in state exists. Nothing to migrate."
+ "AppleAccount daemon connection for returning local contacts returned an error: %@"
+ "Calling daemon service to get localContacts For Custodians"
+ "Cleared Apple Account Information Properties from AAPrefsDomain."
+ "Custodian recovery canceled with error: %@"
+ "CustodianRecoveryRequestContext with ownerAppleID: %@ \nsessionID: %@ \nrecoveryCode: %@ \ncustodianUUID: %@ \nrecoveryToken: %@ \ncliMode: %i \ndataOnly: %@, recordBuildVersion: %@, flowID: %@, altDSID: %@, isAccountRecovery: %@"
+ "Destination: %@, Type: %li, URI: %@"
+ "END [%lld] %fs: CancelCustodianRecovery  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "IDSSendMessageOptionFromIDKey"
+ "Initialized AppleAccount information."
+ "LCInvite: isEnabled in Defaults: %{BOOL}d"
+ "Profile picture cache could not be deleted. Error: %@"
+ "Profile picture cache deleted successfully."
+ "Profile picture cache does not exist."
+ "SignOutRedesign"
+ "SignOutRedesign feature flag turned off. Not showing the Erase/Sign out offer. Continuing with Sign Out."
+ "T@\"NSNumber\",N,Saa_setDOBRepairState:"
+ "T@\"NSString\",R,C,N,V_sentToHandleUri"
+ "T@\"NSUUID\",R,C,N,V_custodianID"
+ "TB,N,V_isAccountRecovery"
+ "_delegate_startSignOutFlowForAccount:completion:"
+ "_deleteProfilePictureCache"
+ "_fetchPrimaryAccountSignInState"
+ "_getProfilePictureCacheURL"
+ "_isAccountRecovery"
+ "_needsMigration"
+ "_optionsDictionaryWithResponseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:sendFromHandleUri:"
+ "_sentToHandleUri"
+ "_setSignedInState:"
+ "_startSignOutOfferFlow:completion:"
+ "aa_dobRepairState"
+ "aa_needsDOBRepair"
+ "aa_setDOBRepairState:"
+ "cancelCustodianRecoveryWithContext:completion:"
+ "clearNonSecureAAPrefsDomain"
+ "com.apple.AAFollowUpIdentifier.childProtoConnect"
+ "com.apple.appleaccount.custodian.decodeIDSMessage"
+ "com.apple.appleaccount.custodian.healthcheck.custodian"
+ "com.apple.appleaccount.custodian.healthcheck.incompleteinvitation.custodianResendInvitationAcceptanceMessage"
+ "com.apple.appleaccount.custodian.healthcheck.owner"
+ "com.apple.appleaccount.custodian.healthcheck.owner.confirmCustodianWithServer"
+ "com.apple.appleaccount.custodian.healthcheck.owner.finalizeSetupWithServer"
+ "com.apple.appleaccount.custodian.healthcheck.owner.sendRecoveryInfoMessage"
+ "com.apple.appleaccount.custodian.healthcheck.ownerUpdatedCustodianRecord"
+ "com.apple.appleaccount.custodian.recovery.cancel"
+ "com.apple.appleaccount.custodian.recovery.experimental.deviceHasCachedCustodianList"
+ "com.apple.appleaccount.custodian.recovery.fetchAPSToken"
+ "com.apple.appleaccount.custodian.recovery.initializeSessionWithServer"
+ "com.apple.appleaccount.custodian.recovery.ownerCreateSession"
+ "com.apple.appleaccount.custodian.recovery.ownerFetchCustodianRecoveryKeys"
+ "com.apple.appleaccount.custodian.recovery.ownerValidateCode"
+ "com.apple.appleaccount.custodian.setup.acceptSharedRecoveryInfo"
+ "com.apple.appleaccount.custodian.setup.accountEligibilityCheck"
+ "com.apple.appleaccount.custodian.setup.accountNotEligible"
+ "com.apple.appleaccount.custodian.setup.cleanup.deleteCustodianshipRecordFromCloud"
+ "com.apple.appleaccount.custodian.setup.cleanup.deleteRecoveryKeyByCustodianIDFromSecurity"
+ "com.apple.appleaccount.custodian.setup.cleanup.deleteRecoveryKeyByOctagonIDFromSecurity"
+ "com.apple.appleaccount.custodian.setup.cleanup.revokeCustodianFromServer"
+ "com.apple.appleaccount.custodian.setup.custodianUpdatedCustodianshipRecord"
+ "com.apple.appleaccount.custodian.setup.familyMemberCheck"
+ "com.apple.appleaccount.custodian.setup.finalizeSetupWithServer"
+ "com.apple.appleaccount.custodian.setup.invitationProcessedForManualAccept"
+ "com.apple.appleaccount.custodian.setup.newCustodian"
+ "com.apple.appleaccount.custodian.setup.ownerGenerateCustodianRecoveryKey"
+ "com.apple.appleaccount.custodian.setup.ownerGenerateEncryptedCPRK"
+ "com.apple.appleaccount.custodian.setup.ownerStoredCustodianRecordToCloud"
+ "com.apple.appleaccount.custodian.setup.ownerUpdatedCustodianRecord"
+ "com.apple.appleaccount.custodian.setup.processAccept.createRecoveryInfoShare"
+ "com.apple.appleaccount.custodian.setup.processAccept.fetchRecoveryInfo"
+ "com.apple.appleaccount.custodian.setup.processAccept.sendRecoveryInfoMessage"
+ "com.apple.appleaccount.custodian.setup.processDecline.cleanup"
+ "com.apple.appleaccount.custodian.setup.processFinalizeSetupMessage"
+ "com.apple.appleaccount.custodian.setup.processInvitation"
+ "com.apple.appleaccount.custodian.setup.processInvitationAcceptanceResponse"
+ "com.apple.appleaccount.custodian.setup.processInvitationDeclineResponse"
+ "com.apple.appleaccount.custodian.setup.processNotReachable"
+ "com.apple.appleaccount.custodian.setup.processRemoveCustodian"
+ "com.apple.appleaccount.custodian.setup.processSharedRecoveryInfo"
+ "com.apple.appleaccount.custodian.setup.remove.sendRemovalMessageToCustodian"
+ "com.apple.appleaccount.custodian.setup.resendInvitation"
+ "com.apple.appleaccount.custodian.setup.respondToInvite"
+ "com.apple.appleaccount.custodian.setup.sendAutoAcceptInvitationMessage"
+ "com.apple.appleaccount.custodian.setup.sendFinalizeSetupMessage"
+ "com.apple.appleaccount.custodian.setup.sendInvitation"
+ "com.apple.appleaccount.custodian.setup.sendInvitationAcceptanceMessage"
+ "com.apple.appleaccount.custodian.setup.sendInvitationDeclineMessage"
+ "com.apple.appleaccount.custodian.setup.stopBeingCustodian"
+ "com.apple.appleaccount.custodian.setup.storeInvitationToCloud"
+ "com.apple.appleaccount.custodian.systemSync"
+ "com.apple.appleaccount.custodian.ui.exitAccountRecovery"
+ "com.apple.appleaccount.custodian.ui.exitCustodianDetails"
+ "com.apple.appleaccount.custodian.ui.openAccountRecovery"
+ "com.apple.appleaccount.custodian.ui.openCustodianDetails"
+ "com.apple.appleaccount.fetchUserInfo"
+ "customMaintenanceIntervalMinutes"
+ "dobRepairState"
+ "fetchCustodianRecoveryKeysWithContext:completion:"
+ "fileExistsAtPath:"
+ "initCustodianMessageFrom:data:sentToHandleUri:"
+ "initInheritanceMessageFrom:data:sentToHandleUri:"
+ "initWithCustodianID:"
+ "isAccountRecovery"
+ "isBetterSignOutFeatureEnabled"
+ "isCustomMaintenanceIntervalEnabled"
+ "localContactsForCustodians:completion:"
+ "messageService:didReceiveMessage:fromID:sentToHandleUri:"
+ "migrateToPrimaryAccountSignInState"
+ "preProxTermsEnabled"
+ "primaryAccountSignInState"
+ "prkPresence"
+ "removeCustodianWithContext:completion:"
+ "removeItemAtPath:error:"
+ "resetAccountInfoToSignedOutState"
+ "sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:"
+ "sentToHandleUri"
+ "setCustomMaintenanceIntervalEnabled:"
+ "setCustomMaintenanceIntervalMinutes:"
+ "setFullName:"
+ "setIsAccountRecovery:"
+ "setLCInviteAcceptanceEnabled:"
+ "signOutFlowController:startSignOutForAccount:completion:"
+ "signout"
+ "stopBeingCustodianWithContext:completion:"
+ "terms-pre-prox-setup"
+ "typeof (((typeof (IDSSendMessageOptionFromIDKey) (*)(void))0)()) getIDSSendMessageOptionFromIDKey(void)"
+ "updateAccountInformationCacheForAppleAccount:"
+ "updateDOBRepairStateWithSettings:completionHandler:"
+ "v32@0:8@\"AACustodianRecoveryRequestContext\"16@?<v@?@\"AACustodianDataRecoveryKeys\"@\"NSError\">24"
+ "v32@0:8@\"AACustodianRecoveryRequestContext\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AACustodianUpdateRequestContext\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "🎒AAMessagingService: received data %@ from %@, sentToHandleUri: %@ and context %@. Calling delegates"
- "@\"NSUUID\"68@0:8@\"NSData\"16@\"NSArray\"24@\"NSString\"32B40@\"NSSet\"44@\"NSSet\"52^@60"
- "@44@0:8@16B24@28@36"
- "@68@0:8@16@24@32B40@44@52^@60"
- "AAMessagingService: received data %@ from %@ and context %@. Calling delegates"
- "Custodian recovery canceled with result: %i, error: %@"
- "CustodianRecoveryRequestContext with ownerAppleID: %@ \nsessionID: %@ \nrecoveryCode: %@ \ncustodianUUID: %@ \nrecoveryToken: %@ \ncliMode: %i \ndataOnly: %@, recordBuildVersion: %@, flowID: %@, altDSID: %@"
- "INHERITANCE_ADDED_MESSAGES_BUBBLE_TITLE"
- "T@\"NSString\",R,N,V_accountFullName"
- "T@\"NSString\",R,N,V_profilePictureCacheURL"
- "TB,R,V_isSignedIn"
- "_accountFullName"
- "_isSignedIn"
- "_optionsDictionaryWithResponseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:"
- "_profilePictureCacheURL"
- "com.apple.appleaccount.CustodianRecovery"
- "initCustodianMessageFrom:data:"
- "initInheritanceMessageFrom:data:"
- "isAppleAccountInformationCacheEnabled"
- "messageService:didReceiveMessage:fromID:"
- "sendMessage:destinations:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:"
- "v32@0:8@\"NSString\"16@?<v@?@\"AACustodianDataRecoveryKeys\"@\"NSError\">24"

```
