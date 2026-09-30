## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit`

```diff

-493.230.1.0.0
-  __TEXT.__text: 0x1ecdac
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0xb140
-  __TEXT.__const: 0x462c1
-  __TEXT.__cstring: 0xd2df
-  __TEXT.__oslogstring: 0xf886
-  __TEXT.__gcc_except_tab: 0x5448
+493.462.0.0.0
+  __TEXT.__text: 0x1f2af4
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_methlist: 0xce04
+  __TEXT.__const: 0x46291
+  __TEXT.__cstring: 0xdbf7
+  __TEXT.__oslogstring: 0xff78
+  __TEXT.__gcc_except_tab: 0x54ec
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x3a88
-  __TEXT.__eh_frame: 0xc0
-  __TEXT.__objc_classname: 0x18d5
-  __TEXT.__objc_methname: 0x1eaa9
-  __TEXT.__objc_methtype: 0x41a8
-  __TEXT.__objc_stubs: 0xd000
-  __DATA_CONST.__got: 0x818
-  __DATA_CONST.__const: 0x3f08
-  __DATA_CONST.__objc_classlist: 0x550
-  __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x1d8
+  __TEXT.__unwind_info: 0x3d60
+  __TEXT.__eh_frame: 0xb8
+  __TEXT.__objc_classname: 0x1a5b
+  __TEXT.__objc_methname: 0x1fe42
+  __TEXT.__objc_methtype: 0x439d
+  __TEXT.__objc_stubs: 0xdb80
+  __DATA_CONST.__got: 0x870
+  __DATA_CONST.__const: 0x4078
+  __DATA_CONST.__objc_classlist: 0x5b0
+  __DATA_CONST.__objc_catlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6300
+  __DATA_CONST.__objc_selrefs: 0x68b8
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x358
-  __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH_CONST.__const: 0xbfa0
-  __AUTH_CONST.__cfstring: 0xe080
-  __AUTH_CONST.__objc_const: 0x23bd8
-  __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH_CONST.__objc_dictobj: 0x1b8
+  __DATA_CONST.__objc_superrefs: 0x3a0
+  __DATA_CONST.__objc_arraydata: 0x1c0
+  __AUTH_CONST.__auth_got: 0x610
+  __AUTH_CONST.__const: 0xc0a0
+  __AUTH_CONST.__cfstring: 0xe660
+  __AUTH_CONST.__objc_const: 0x22fc8
+  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x3520
-  __DATA.__objc_ivar: 0xe8c
-  __DATA.__data: 0x17a8
+  __AUTH.__objc_data: 0x38e0
+  __DATA.__objc_ivar: 0xf20
+  __DATA.__data: 0x1868
   __DATA.__bss: 0x7f0
-  __DATA.__common: 0xa20
+  __DATA.__common: 0xa18
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BD0E0CC3-089A-39BA-937F-37CDE4086590
-  Functions: 5735
-  Symbols:   13406
-  CStrings:  10505
+  UUID: 797A1646-3109-3ECE-83B7-273D4610CBD4
+  Functions: 6013
+  Symbols:   13990
+  CStrings:  10871
 
Symbols:
+ +[ACAccount(AuthKitProto) createProtoAccountWithAgeRange:]
+ +[ACAccount(AuthKitProto) createProtoAccountWithGivenName:ageRange:]
+ +[AKAbsintheSigner sharedSigner].cold.1
+ +[AKAccountManager sharedInstance].cold.1
+ +[AKAgeRangeSettingsExtractor defaultConfigDictionary]
+ +[AKAgeRangeSettingsExtractor defaultConfigDictionary].cold.1
+ +[AKAgeRangeSettingsExtractor defaultConfigDictionary].cold.2
+ +[AKAgeRangeSettingsExtractor extractAgeRangeConfigFromGlobalConfig:]
+ +[AKAgeRangeSettingsExtractor extractAgeRangeConfigFromGlobalConfig:].cold.1
+ +[AKAgeRangeSettingsExtractor extractAgeRangeConfigFromGlobalConfig:].cold.2
+ +[AKAlertHandler sharedInstance].cold.1
+ +[AKAnalyticsReporterRTC rtcAnalyticsReporter].cold.1
+ +[AKAnisetteProvisioningClientInterface XPCInterface].cold.1
+ +[AKAnisetteProvisioningDaemonInterface XPCInterface].cold.1
+ +[AKAppleIDAuthenticationClientInterface XPCInterface].cold.1
+ +[AKAppleIDAuthenticationController sensitiveAuthenticationKeys].cold.1
+ +[AKAppleIDAuthenticationController sensitiveTokenKeysForFullRedaction].cold.1
+ +[AKAppleIDAuthenticationController sensitiveTokenKeys].cold.1
+ +[AKAppleIDAuthenticationController tokenDictionaryKeys].cold.1
+ +[AKAppleIDAuthenticationDaemonInterface XPCInterface].cold.1
+ +[AKAppleIDServerResourceLoadDelegate sharedController].cold.1
+ +[AKAppleIDSigningDaemonInterface XPCInterface].cold.1
+ +[AKAttestationSigner sharedSigner].cold.1
+ +[AKAuthenticatableResource supportsSecureCoding]
+ +[AKAuthorizationClientInterface XPCInterface].cold.1
+ +[AKAuthorizationController sharedController].cold.1
+ +[AKAuthorizationDaemonInterface XPCInterface].cold.1
+ +[AKAuthorizationNotificationHandlerInterface XPCInterface].cold.1
+ +[AKAuthorizationNotificationService _sharedService].cold.1
+ +[AKAuthorizationPresenterHostInterface XPCInterface].cold.1
+ +[AKAuthorizationStateBroadcastHandlerInterface XPCInterface].cold.1
+ +[AKCDPFactory walrusStatusLiveValue].cold.1
+ +[AKCDPFactory walrusStatus].cold.2
+ +[AKCDPFactory webAccessStatusLiveValue].cold.1
+ +[AKCarouselAlertClientConnection sharedConnection].cold.1
+ +[AKCarrierBundleUtilities sharedInstance].cold.1
+ +[AKCommandLineURLSession sharedServerUIURLSession].cold.1
+ +[AKConfiguration sharedConfiguration].cold.1
+ +[AKCustodianDaemonInterface XPCInterface].cold.1
+ +[AKDevice _systemVersionDictionary].cold.1
+ +[AKDevice currentDevice].cold.1
+ +[AKFLFollowUpController sharedInstance].cold.1
+ +[AKFeatureManager sharedManager].cold.1
+ +[AKFollowUpProviderFactory sharedAuthKitFollowupProvider].cold.1
+ +[AKGlobalConfig sharedInstance].cold.1
+ +[AKIORegistryReader sharedInstance].cold.1
+ +[AKLoginPresenterHostInterface XPCInterface].cold.1
+ +[AKMediaServicesController sharedInstance].cold.1
+ +[AKNetworkObserver sharedNetworkObserver].cold.1
+ +[AKPasswordResetPresenterHostInterface XPCInterface].cold.1
+ +[AKPrivateEmailClientInterface XPCInterface].cold.1
+ +[AKPrivateEmailDaemonInterface XPCInterface].cold.1
+ +[AKPrivateEmailPresenterHostInterface XPCInterface].cold.1
+ +[AKProtoAccountContext supportsSecureCoding]
+ +[AKProtoAccountShieldContext supportsSecureCoding]
+ +[AKRemoteViewServiceConfiguration configurationForHostWithBundleID:sceneID:remoteBundleID:]
+ +[AKRemoteViewServiceConfiguration configurationWithRemoteBundleID:]
+ +[AKRemoteViewServiceConfiguration configurationWithRemoteBundleID:remoteClassName:]
+ +[AKURLBag _currentBagsUnderLockWithBlock:].cold.1
+ +[AKURLBag sharedBag].cold.1
+ +[AKURLSession _urlBagCache].cold.1
+ +[AKWalrusConfigProvider sharedInstance].cold.1
+ +[NSXPCInterface(NSXPCInterface_AKRemoteViewServiceInterface) remoteViewServiceInterface].cold.1
+ +[NSXPCInterface(NSXPCInterface_AKRemoteViewSessionInterface) remoteViewSessionInterface].cold.1
+ -[ACAccount(AuthKitProto) dca_ageRange]
+ -[ACAccount(AuthKitProto) dca_givenName]
+ -[ACAccount(AuthKitProto) dca_setAgeRange:]
+ -[ACAccount(AuthKitProto) dca_setGivenName:]
+ -[ACAccount(AuthKitProto) initWithGivenName:ageRange:]
+ -[ACAccount(AuthKitProto) proto_ageRange]
+ -[ACAccount(AuthKitProto) proto_givenName]
+ -[ACAccount(AuthKitProto) proto_setAgeRange:]
+ -[ACAccount(AuthKitProto) proto_setGivenName:]
+ -[AKAccountManager _ageAttestationPhase1FeatureRestricted]
+ -[AKAccountManager _protoAccountWithError:]
+ -[AKAccountManager _telemetryDeviceSessionIDForAccount:]
+ -[AKAccountManager _telemetryDeviceSessionIDForAccount:].cold.1
+ -[AKAccountManager accountAccessTelemetryOptInForAccount:].cold.2
+ -[AKAccountManager dcaAccount]
+ -[AKAccountManager isSignOutInProgress:]
+ -[AKAccountManager isSignOutInProgress:].cold.1
+ -[AKAccountManager protoAccountType]
+ -[AKAccountManager protoAccountType].cold.1
+ -[AKAccountManager protoAccount]
+ -[AKAccountManager setAccountAccessTelemetryOptIn:forAccount:error:].cold.4
+ -[AKAccountManager setSignOutInProgress:forAccount:]
+ -[AKAccountManager setSignOutInProgress:forAccount:].cold.1
+ -[AKAccountManager shieldSignInOrCreateFlows]
+ -[AKAccountManager shieldSignInOrCreateFlows].cold.1
+ -[AKAccountManager shieldSignInOrCreateFlows].cold.2
+ -[AKAgeRangeSettings initWithU13Limit:u18Limit:]
+ -[AKAgeRangeSettings u13Limit]
+ -[AKAgeRangeSettings u18Limit]
+ -[AKAgeRangeSettingsCache .cxx_destruct]
+ -[AKAgeRangeSettingsCache _configurationValueForKey:]
+ -[AKAgeRangeSettingsCache _configurationValueForKey:].cold.1
+ -[AKAgeRangeSettingsCache _setConfigurationValue:forKey:]
+ -[AKAgeRangeSettingsCache _setConfigurationValue:forKey:].cold.1
+ -[AKAgeRangeSettingsCache _setU13AgeLimit:]
+ -[AKAgeRangeSettingsCache _setU18AgeLimit:]
+ -[AKAgeRangeSettingsCache _u13AgeLimit]
+ -[AKAgeRangeSettingsCache _u18AgeLimit]
+ -[AKAgeRangeSettingsCache _updateAgeRangeSettings]
+ -[AKAgeRangeSettingsCache _updateAgeRangeSettings].cold.1
+ -[AKAgeRangeSettingsCache ageRangeSettings]
+ -[AKAgeRangeSettingsCache clearAgeRangeCache]
+ -[AKAgeRangeSettingsCache dealloc]
+ -[AKAgeRangeSettingsCache init]
+ -[AKAgeRangeSettingsCache updateAgeRangeCacheWithGlobalConfig:]
+ -[AKAgeRangeSettingsCache updateAgeRangeCacheWithGlobalConfig:].cold.1
+ -[AKAgeRangeSettingsCache updateAgeRangeCacheWithGlobalConfig:].cold.2
+ -[AKAgeRangeSettingsCache updateAgeRangeCacheWithGlobalConfig:].cold.3
+ -[AKAgeRangeSettingsProvider .cxx_destruct]
+ -[AKAgeRangeSettingsProvider ageRangeCache]
+ -[AKAgeRangeSettingsProvider init]
+ -[AKAgeRangeSettingsProvider refreshAgeRangeWithCompletion:]
+ -[AKAgeRangeSettingsProvider refreshAgeRangeWithCompletion:].cold.1
+ -[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]
+ -[AKAnisetteProvisioningController _attestationDataForRequestData:error:]
+ -[AKAnisetteProvisioningController attestationDataForRequestData:completion:]
+ -[AKAnisetteProvisioningController attestationDataForRequestData:error:]
+ -[AKAnisetteProvisioningController attestationDataForRequestData:error:].cold.1
+ -[AKAnisetteProvisioningController connectionManager]
+ -[AKAnisetteProvisioningController initWithConnectionConfiguration:device:provider:]
+ -[AKAnisetteProvisioningController setConnectionManager:]
+ -[AKAnisetteProvisioningController shouldAllowReprovisionForHostName:completion:]
+ -[AKAppleIDAuthenticationContext authenticatableResource]
+ -[AKAppleIDAuthenticationContext isConfiguredForTokenUpgradeWithCompletion:]
+ -[AKAppleIDAuthenticationContext protoAccountContext]
+ -[AKAppleIDAuthenticationContext setAuthenticatableResource:]
+ -[AKAppleIDAuthenticationContext setProtoAccountContext:]
+ -[AKAppleIDAuthenticationController _authenticateWithContext:completion:]
+ -[AKAppleIDAuthenticationController _deviceListWithContext:completion:]
+ -[AKAppleIDAuthenticationController initWithConnectionConfiguration:]
+ -[AKAppleIDAuthenticationController initWithIdentifier:connectionConfiguration:]
+ -[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]
+ -[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:].cold.1
+ -[AKAppleIDServerResourceLoadDelegate _signRequestWithServerBackoffInfoHeader:]
+ -[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]
+ -[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:].cold.1
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.1
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.2
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.3
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.4
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.5
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.6
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.7
+ -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.8
+ -[AKAttestationRequestData clientName]
+ -[AKAttestationRequestData initWithSigningData:requiredHeaders:]
+ -[AKAttestationRequestData setClientName:]
+ -[AKAttestationRequestData signingDataHash]
+ -[AKAuthenticatableResource .cxx_destruct]
+ -[AKAuthenticatableResource copyWithZone:]
+ -[AKAuthenticatableResource description]
+ -[AKAuthenticatableResource encodeWithCoder:]
+ -[AKAuthenticatableResource initWithCoder:]
+ -[AKAuthenticatableResource initWithResourceType:resourceName:]
+ -[AKAuthenticatableResource init]
+ -[AKAuthenticatableResource resourceName]
+ -[AKAuthenticatableResource resourceType]
+ -[AKAuthenticatableResource setResourceName:]
+ -[AKAuthenticatableResource setResourceType:]
+ -[AKAuthorizationPresentationContext _addPresenterParameters].cold.1
+ -[AKBiometricRatchetContext initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:notInteractive:]
+ -[AKBiometricRatchetContext notInteractive]
+ -[AKClientConnectionLifecycleManager .cxx_destruct]
+ -[AKClientConnectionLifecycleManager activeServiceConnection]
+ -[AKClientConnectionLifecycleManager dealloc]
+ -[AKClientConnectionLifecycleManager initWithConfiguration:]
+ -[AKClientConnectionLifecycleManager init]
+ -[AKClientConnectionLifecycleManager serviceConnectionConfig]
+ -[AKClientConnectionLifecycleManager serviceConnection]
+ -[AKClientConnectionLifecycleManager setServiceConnection:]
+ -[AKClientConnectionLifecycleManager setServiceConnectionConfig:]
+ -[AKClientConnectionLifecycleManager setUnfairLock:]
+ -[AKClientConnectionLifecycleManager teardownServiceConnection]
+ -[AKClientConnectionLifecycleManager unfairLock]
+ -[AKCommandLineUtilities _hostURL].cold.1
+ -[AKConfiguration internalSiwADefaultHME]
+ -[AKConfiguration setInternalSiwADefaultHME:]
+ -[AKDevice _volumeGroupUUID].cold.3
+ -[AKDevice biometryType]
+ -[AKDevice isInternalBuild].cold.1
+ -[AKDevice isSeedBuild].cold.1
+ -[AKDevice isVirtualMachine].cold.1
+ -[AKDeviceListRequestContext proxiedBundleID]
+ -[AKDeviceListRequestContext setProxiedBundleID:]
+ -[AKFeatureManager init].cold.19
+ -[AKFeatureManager isAgeAttestationPhase1Enabled]
+ -[AKFeatureManager isServerBackoffEnabled]
+ -[AKProtoAccountContext .cxx_destruct]
+ -[AKProtoAccountContext ageRange]
+ -[AKProtoAccountContext copyWithZone:]
+ -[AKProtoAccountContext debugDescription]
+ -[AKProtoAccountContext encodeWithCoder:]
+ -[AKProtoAccountContext givenName]
+ -[AKProtoAccountContext initWithCoder:]
+ -[AKProtoAccountContext initWithGivenName:lastName:ageRange:]
+ -[AKProtoAccountContext lastName]
+ -[AKProtoAccountContext setAgeRange:]
+ -[AKProtoAccountContext setGivenName:]
+ -[AKProtoAccountContext setLastName:]
+ -[AKProtoAccountShieldContext .cxx_destruct]
+ -[AKProtoAccountShieldContext encodeWithCoder:]
+ -[AKProtoAccountShieldContext initWithCoder:]
+ -[AKProtoAccountShieldContext initWithContext:]
+ -[AKProtoAccountShieldContext protoAccount]
+ -[AKProtoAccountShieldContext setProtoAccount:]
+ -[AKRemoteViewServiceConfiguration init]
+ -[AKRemoteViewServiceConfiguration remoteBundleID]
+ -[AKRemoteViewServiceConfiguration remoteClassName]
+ -[AKRemoteViewServiceConfiguration setRemoteBundleID:]
+ -[AKRemoteViewServiceConfiguration setRemoteClassName:]
+ -[AKServerBackoffContext .cxx_destruct]
+ -[AKServerBackoffContext appServerName]
+ -[AKServerBackoffContext clientBundleID]
+ -[AKServerBackoffContext proxiedAppBundleID]
+ -[AKServerBackoffContext setAppServerName:]
+ -[AKServerBackoffContext setClientBundleID:]
+ -[AKServerBackoffContext setProxiedAppBundleID:]
+ -[AKServerBackoffContext setUrl:]
+ -[AKServerBackoffContext url]
+ -[AKServerBackoffController .cxx_destruct]
+ -[AKServerBackoffController _clientInfoForContext:]
+ -[AKServerBackoffController _clientInfoForContext:matchingClients:]
+ -[AKServerBackoffController _isBackoffSupported]
+ -[AKServerBackoffController _isStaleClientInfo:]
+ -[AKServerBackoffController _objectForKey:]
+ -[AKServerBackoffController _sanitizeServerBackoffInfoDict:]
+ -[AKServerBackoffController _serverBackoffDefaults]
+ -[AKServerBackoffController _setObject:forKey:]
+ -[AKServerBackoffController _shouldBackoffContext:matchingClients:]
+ -[AKServerBackoffController _updateServerBackoffInfoWithDictionary:]
+ -[AKServerBackoffController _updatedServerBackoffInfoForClients:cachedClients:]
+ -[AKServerBackoffController clearServerBackoffInfoCache]
+ -[AKServerBackoffController configureFromHeaderFields:]
+ -[AKServerBackoffController delegate]
+ -[AKServerBackoffController init]
+ -[AKServerBackoffController reportTelemetryForContext:backoffType:]
+ -[AKServerBackoffController reportTelemetryForContext:backoffType:].cold.1
+ -[AKServerBackoffController serverBackoffInfoCache]
+ -[AKServerBackoffController serverBackoffInfoForContext:]
+ -[AKServerBackoffController setDelegate:]
+ -[AKServerBackoffController shouldBackoffContext:]
+ -[AKServerBackoffHelper .cxx_destruct]
+ -[AKServerBackoffHelper _backoffContextFromRequest:]
+ -[AKServerBackoffHelper configureFromHeaderFields:]
+ -[AKServerBackoffHelper init]
+ -[AKServerBackoffHelper isBackoffSupported]
+ -[AKServerBackoffHelper isBackoffSupported].cold.1
+ -[AKServerBackoffHelper reportTelemetryForRequest:backoffType:]
+ -[AKServerBackoffHelper serverBackoffInfoForRequest:]
+ -[AKServerBackoffHelper shouldBackoffRequest:]
+ -[AKServerBackoffHelper urlAtKey:]
+ -[AKURLBag grandSlamEndpointIdentifiersWithCompletion:]
+ -[AKURLBag isClientBackoffDisabled]
+ -[AKURLBag isDeviceBAADisabled]
+ -[AKURLBag isVMBAADisabled]
+ -[AKURLSession _unsafe_retryTaskIfPossible:].cold.3
+ -[AKXPCConnectionConfiguration .cxx_destruct]
+ -[AKXPCConnectionConfiguration daemonXPCEndpoint]
+ -[AKXPCConnectionConfiguration description]
+ -[AKXPCConnectionConfiguration exportedInterface]
+ -[AKXPCConnectionConfiguration exportedObject]
+ -[AKXPCConnectionConfiguration machServiceName]
+ -[AKXPCConnectionConfiguration options]
+ -[AKXPCConnectionConfiguration remoteObjectInterface]
+ -[AKXPCConnectionConfiguration setDaemonXPCEndpoint:]
+ -[AKXPCConnectionConfiguration setExportedInterface:]
+ -[AKXPCConnectionConfiguration setExportedObject:]
+ -[AKXPCConnectionConfiguration setMachServiceName:]
+ -[AKXPCConnectionConfiguration setOptions:]
+ -[AKXPCConnectionConfiguration setRemoteObjectInterface:]
+ -[NSError(AuthKit) ak_isAppleIDSetupCancelError]
+ -[NSError(AuthKit) ak_isAppleIDSetupErrorWithCode:]
+ -[NSMutableURLRequest(AuthKit) ak_addBiometryTypeHeaderWithValue:]
+ -[NSMutableURLRequest(AuthKit) ak_addBiometryTypeHeaderWithValue:].cold.1
+ -[NSMutableURLRequest(AuthKit) ak_addCreateInformationHeaderWithValue:]
+ -[NSMutableURLRequest(AuthKit) ak_addCreateInformationHeaderWithValue:].cold.1
+ -[NSMutableURLRequest(AuthKit) ak_addServerBackoffInfoHeader:]
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table167
+ GCC_except_table171
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table180
+ GCC_except_table187
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table204
+ GCC_except_table226
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table275
+ GCC_except_table276
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table318
+ GCC_except_table319
+ GCC_except_table325
+ GCC_except_table326
+ GCC_except_table327
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table358
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table94
+ OBJC_IVAR_$_AKAccountManager._protoAccountType
+ OBJC_IVAR_$_AKAccountManager._protoAccountTypeLock
+ OBJC_IVAR_$_AKAgeRangeSettings._u13Limit
+ OBJC_IVAR_$_AKAgeRangeSettings._u18Limit
+ OBJC_IVAR_$_AKAgeRangeSettingsCache._ageRangeSettings
+ OBJC_IVAR_$_AKAgeRangeSettingsCache._notificationQueue
+ OBJC_IVAR_$_AKAgeRangeSettingsCache._notificationToken
+ OBJC_IVAR_$_AKAgeRangeSettingsCache._unfairLock
+ OBJC_IVAR_$_AKAgeRangeSettingsProvider._ageRangeCache
+ OBJC_IVAR_$_AKAgeRangeSettingsProvider._authController
+ OBJC_IVAR_$_AKAnisetteProvisioningController._connectionManager
+ OBJC_IVAR_$_AKAppleIDAuthenticationContext._authenticatableResource
+ OBJC_IVAR_$_AKAppleIDAuthenticationContext._protoAccountContext
+ OBJC_IVAR_$_AKAppleIDAuthenticationController._connectionManager
+ OBJC_IVAR_$_AKAttestationRequestData._clientName
+ OBJC_IVAR_$_AKAttestationRequestData._signingDataHash
+ OBJC_IVAR_$_AKAuthenticatableResource._resourceName
+ OBJC_IVAR_$_AKAuthenticatableResource._resourceType
+ OBJC_IVAR_$_AKBiometricRatchetContext._notInteractive
+ OBJC_IVAR_$_AKClientConnectionLifecycleManager._serviceConnection
+ OBJC_IVAR_$_AKClientConnectionLifecycleManager._serviceConnectionConfig
+ OBJC_IVAR_$_AKClientConnectionLifecycleManager._unfairLock
+ OBJC_IVAR_$_AKConfiguration._internalSiwADefaultHME
+ OBJC_IVAR_$_AKDeviceListRequestContext._proxiedBundleID
+ OBJC_IVAR_$_AKFeatureManager._cacheIsServerBackoffEnabled
+ OBJC_IVAR_$_AKFeatureManager._cachedAgeAttestationPhase1Enabled
+ OBJC_IVAR_$_AKProtoAccountContext._ageRange
+ OBJC_IVAR_$_AKProtoAccountContext._givenName
+ OBJC_IVAR_$_AKProtoAccountContext._lastName
+ OBJC_IVAR_$_AKProtoAccountShieldContext._protoAccount
+ OBJC_IVAR_$_AKRemoteViewServiceConfiguration._remoteBundleID
+ OBJC_IVAR_$_AKRemoteViewServiceConfiguration._remoteClassName
+ OBJC_IVAR_$_AKServerBackoffContext._appServerName
+ OBJC_IVAR_$_AKServerBackoffContext._clientBundleID
+ OBJC_IVAR_$_AKServerBackoffContext._proxiedAppBundleID
+ OBJC_IVAR_$_AKServerBackoffContext._url
+ OBJC_IVAR_$_AKServerBackoffController._delegate
+ OBJC_IVAR_$_AKServerBackoffController._serverBackoffLock
+ OBJC_IVAR_$_AKServerBackoffHelper._serverBackoffController
+ OBJC_IVAR_$_AKURLSession._serverBackoffHelper
+ OBJC_IVAR_$_AKXPCConnectionConfiguration._daemonXPCEndpoint
+ OBJC_IVAR_$_AKXPCConnectionConfiguration._exportedInterface
+ OBJC_IVAR_$_AKXPCConnectionConfiguration._exportedObject
+ OBJC_IVAR_$_AKXPCConnectionConfiguration._machServiceName
+ OBJC_IVAR_$_AKXPCConnectionConfiguration._options
+ OBJC_IVAR_$_AKXPCConnectionConfiguration._remoteObjectInterface
+ _ACAccountTypeIdentifierDCA
+ _AKCountriesKey
+ _AKLogFido.cold.1
+ _AKLogHme.cold.1
+ _AKLogPasskey.cold.1
+ _AKLogSiwa.cold.1
+ _AKLogSystem.cold.1
+ _AKLogSystemQuery.cold.1
+ _AKLogUserInteraction.cold.1
+ _AKProtoAccountResultKeyAgeRange
+ _AKProtoAccountResultKeyGivenName
+ _AKRemoteViewServiceUserInfoIndicatorKey
+ _AKRequestBodyProtoAccountAgeRange
+ _AKRequestBodyProtoAccountFirstName
+ _AKRequestBodyProtoAccountLastName
+ _AKServerBackoffInfoHeaderKey
+ _AKSignOutInProgressKey
+ _AKSignpostGetNanoseconds.cold.1
+ _AKSignpostLogSystem.cold.1
+ _AKTrafficLogSubsystem.cold.1
+ _AKTriageLogSystem.cold.1
+ _AKU13LimitKey
+ _AKU18LimitKey
+ _AKURLBagKeyAcessorySyncKey
+ _AKURLBagKeyPLTUpgradeEnabled
+ _AKURLBagKeyRecoveryThreatNotification
+ _AKURLBagKeySignout
+ _CFPreferencesCopyAppValue
+ _OBJC_CLASS_$_AKAgeRangeSettings
+ _OBJC_CLASS_$_AKAgeRangeSettingsCache
+ _OBJC_CLASS_$_AKAgeRangeSettingsExtractor
+ _OBJC_CLASS_$_AKAgeRangeSettingsProvider
+ _OBJC_CLASS_$_AKAuthenticatableResource
+ _OBJC_CLASS_$_AKClientConnectionLifecycleManager
+ _OBJC_CLASS_$_AKProtoAccountContext
+ _OBJC_CLASS_$_AKProtoAccountShieldContext
+ _OBJC_CLASS_$_AKServerBackoffContext
+ _OBJC_CLASS_$_AKServerBackoffController
+ _OBJC_CLASS_$_AKServerBackoffHelper
+ _OBJC_CLASS_$_AKXPCConnectionConfiguration
+ _OBJC_METACLASS_$_AKAgeRangeSettings
+ _OBJC_METACLASS_$_AKAgeRangeSettingsCache
+ _OBJC_METACLASS_$_AKAgeRangeSettingsExtractor
+ _OBJC_METACLASS_$_AKAgeRangeSettingsProvider
+ _OBJC_METACLASS_$_AKAuthenticatableResource
+ _OBJC_METACLASS_$_AKClientConnectionLifecycleManager
+ _OBJC_METACLASS_$_AKProtoAccountContext
+ _OBJC_METACLASS_$_AKProtoAccountShieldContext
+ _OBJC_METACLASS_$_AKServerBackoffContext
+ _OBJC_METACLASS_$_AKServerBackoffController
+ _OBJC_METACLASS_$_AKServerBackoffHelper
+ _OBJC_METACLASS_$_AKXPCConnectionConfiguration
+ _SOSCCIsSOSTrustAndSyncingEnabledCachedValue
+ __105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.364
+ __105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.363
+ __134-[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:]_block_invoke.97
+ __134-[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:]_block_invoke.97.cold.1
+ __37+[AKCDPFactory walrusStatusLiveValue]_block_invoke.70
+ __37+[AKCDPFactory walrusStatusLiveValue]_block_invoke.75
+ __37+[AKCDPFactory walrusStatusLiveValue]_block_invoke.79
+ __40+[AKCDPFactory webAccessStatusLiveValue]_block_invoke.83
+ __40+[AKCDPFactory webAccessStatusLiveValue]_block_invoke.86
+ __44-[AKConfiguration configurationValueForKey:]_block_invoke.125
+ __44-[AKURLSession _unsafe_retryTaskIfPossible:]_block_invoke.118
+ __55-[AKServerBackoffController configureFromHeaderFields:]_block_invoke.cold.1
+ __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.20
+ __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.20.cold.1
+ __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.21
+ __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.21.cold.1
+ __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.21.cold.2
+ __60-[AKAgeRangeSettingsProvider refreshAgeRangeWithCompletion:]_block_invoke.cold.1
+ __60-[AKAgeRangeSettingsProvider refreshAgeRangeWithCompletion:]_block_invoke.cold.2
+ __60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.8
+ __60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.8.cold.1
+ __60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.8.cold.2
+ __60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.391
+ __60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.391.cold.1
+ __60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.391.cold.2
+ __61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke.3
+ __61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke.4
+ __61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke.cold.1
+ __61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke.cold.2
+ __61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke_2.5
+ __61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke_2.5.cold.1
+ __61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke_2.cold.1
+ __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.17
+ __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.17.cold.1
+ __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.18
+ __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.18.cold.1
+ __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.18.cold.2
+ __63-[AKClientConnectionLifecycleManager teardownServiceConnection]_block_invoke.cold.1
+ __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke.58
+ __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.59
+ __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.59.cold.1
+ __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.59.cold.2
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.36
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.44
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.44.cold.1
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.44.cold.2
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.44.cold.3
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.44.cold.4
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.44.cold.5
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.47
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.38
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.38.cold.1
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.38.cold.2
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.38.cold.3
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.38.cold.4
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.38.cold.5
+ __64-[AKMediaServicesController appMetadataForBundleIDs:completion:]_block_invoke.57
+ __65-[AKAlertHandler _showAlertForMissingAppleAccountWithCompletion:]_block_invoke.59
+ __65-[AKAlertHandler _showAlertForMissingAppleAccountWithCompletion:]_block_invoke.59.cold.1
+ __65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.316
+ __65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.316.cold.1
+ __65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.317
+ __66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.175
+ __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.325
+ __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.325.cold.1
+ __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.328
+ __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.328.cold.1
+ __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.328.cold.2
+ __69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.342
+ __69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.342.cold.1
+ __69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.343
+ __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.53
+ __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.53.cold.1
+ __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.54
+ __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.54.cold.1
+ __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.54.cold.2
+ __70-[AKAppleIDAuthenticationController deviceListWithContext:completion:]_block_invoke.cold.1
+ __70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.395
+ __71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.312
+ __71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.312.cold.1
+ __71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.313
+ __72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.56
+ __72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.56.cold.1
+ __72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.56.cold.2
+ __72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.396
+ __72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.260.cold.1
+ __72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.422
+ __72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.422.cold.1
+ __72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.423
+ __72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.412
+ __72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.cold.1
+ __72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.380
+ __72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.380.cold.1
+ __73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.44
+ __73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.44.cold.1
+ __73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.44.cold.2
+ __73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.cold.1
+ __73-[AKAppleIDAuthenticationController _authenticateWithContext:completion:]_block_invoke.262
+ __73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.406
+ __73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.406.cold.1
+ __73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.68.cold.2
+ __73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.69.cold.1
+ __73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.70
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.85
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.85.cold.1
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.88
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.88.cold.1
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.88.cold.2
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.92
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.92.cold.1
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.92.cold.2
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.cold.1
+ __73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.cold.2
+ __73-[AKURLSession beginAuthenticationDataTaskWithRequest:completionHandler:]_block_invoke.cold.4
+ __74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.387
+ __74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.387.cold.1
+ __74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.388
+ __74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.409
+ __74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.409.cold.1
+ __76-[AKAppleIDAuthenticationContext isConfiguredForTokenUpgradeWithCompletion:]_block_invoke.cold.1
+ __76-[AKAppleIDAuthenticationContext isConfiguredForTokenUpgradeWithCompletion:]_block_invoke.cold.2
+ __76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.411
+ __76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.411.cold.1
+ __76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.378
+ __76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.378.cold.1
+ __77-[AKAnisetteProvisioningController attestationDataForRequestData:completion:]_block_invoke.45
+ __77-[AKAnisetteProvisioningController attestationDataForRequestData:completion:]_block_invoke.cold.1
+ __77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke.32
+ __77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke.32.cold.1
+ __77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke.32.cold.2
+ __77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.318
+ __77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.346
+ __77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.332
+ __78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.50
+ __78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.cold.1
+ __78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.cold.2
+ __78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.cold.3
+ __78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.379
+ __78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.379.cold.1
+ __79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.55
+ __79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.55.cold.1
+ __79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.55.cold.2
+ __79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.362
+ __80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.350
+ __80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.350.cold.1
+ __80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.351
+ __80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.410
+ __80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.410.cold.1
+ __80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.403
+ __80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.403.cold.1
+ __80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.404
+ __80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.404.cold.1
+ __80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.361
+ __80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.385
+ __80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.385.cold.1
+ __80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.386
+ __81-[AKAnisetteProvisioningController shouldAllowReprovisionForHostName:completion:]_block_invoke.cold.1
+ __81-[AKAnisetteProvisioningController shouldAllowReprovisionForHostName:completion:]_block_invoke.cold.2
+ __81-[AKAnisetteProvisioningController shouldAllowReprovisionForHostName:completion:]_block_invoke.cold.3
+ __81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.405
+ __81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.405.cold.1
+ __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.38
+ __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.38.cold.1
+ __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.39
+ __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.39.cold.1
+ __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.39.cold.2
+ __82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.322
+ __82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.371
+ __82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.371.cold.1
+ __82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.372
+ __83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.375
+ __83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.375.cold.1
+ __83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.376
+ __83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.377
+ __84-[AKAlertHandler _showAlertForInsufficientSecurityLevelWithError:completionHandler:]_block_invoke.81
+ __84-[AKAlertHandler _showAlertForInsufficientSecurityLevelWithError:completionHandler:]_block_invoke.81.cold.1
+ __84-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:error:]_block_invoke.22
+ __84-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:error:]_block_invoke.22.cold.1
+ __84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.402
+ __86-[AKAppleIDAuthenticationContext presentLoginAlertWithError:title:message:completion:]_block_invoke.616
+ __88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.407
+ __88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.407.cold.1
+ __89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.331
+ __90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.338
+ __90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.399
+ __90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.360
+ __90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.360.cold.1
+ __90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.382
+ __90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.382.cold.1
+ __91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.96
+ __91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.96.cold.1
+ __91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.96.cold.2
+ __91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.cold.1
+ __91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.cold.2
+ __92-[AKAnisetteProvisioningController fetchAnisetteDataAndProvisionIfNecessary:withCompletion:]_block_invoke.24
+ __92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.337
+ __93-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:withCompletion:]_block_invoke.29
+ __94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.336
+ __96-[AKAppleIDAuthenticationCommandLineContext _beginDataTaskWithRequest:configuration:completion:]_block_invoke.116
+ __96-[AKAppleIDAuthenticationCommandLineContext _beginDataTaskWithRequest:configuration:completion:]_block_invoke.116.cold.1
+ __97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.356
+ __97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.356.cold.1
+ __97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.357
+ __97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.357.cold.1
+ __98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.408
+ __98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.408.cold.1
+ __AKAgeCacheDomain
+ __AKU13Limit
+ __AKU18Limit
+ __OBJC_$_CATEGORY_ACAccount_$_AuthKitProto
+ __OBJC_$_CATEGORY_CLASS_METHODS_ACAccount_$_AuthKitProto
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ACAccount_$_AuthKitProto
+ __OBJC_$_CLASS_METHODS_AKAgeRangeSettingsExtractor
+ __OBJC_$_CLASS_METHODS_AKAuthenticatableResource
+ __OBJC_$_CLASS_METHODS_AKProtoAccountContext
+ __OBJC_$_CLASS_METHODS_AKProtoAccountShieldContext
+ __OBJC_$_CLASS_PROP_LIST_AKAuthenticatableResource
+ __OBJC_$_CLASS_PROP_LIST_AKProtoAccountContext
+ __OBJC_$_INSTANCE_METHODS_AKAgeRangeSettings
+ __OBJC_$_INSTANCE_METHODS_AKAgeRangeSettingsCache
+ __OBJC_$_INSTANCE_METHODS_AKAgeRangeSettingsProvider
+ __OBJC_$_INSTANCE_METHODS_AKAuthenticatableResource
+ __OBJC_$_INSTANCE_METHODS_AKClientConnectionLifecycleManager
+ __OBJC_$_INSTANCE_METHODS_AKProtoAccountContext
+ __OBJC_$_INSTANCE_METHODS_AKProtoAccountShieldContext
+ __OBJC_$_INSTANCE_METHODS_AKServerBackoffContext
+ __OBJC_$_INSTANCE_METHODS_AKServerBackoffController
+ __OBJC_$_INSTANCE_METHODS_AKServerBackoffHelper
+ __OBJC_$_INSTANCE_METHODS_AKXPCConnectionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AKAgeRangeSettings
+ __OBJC_$_INSTANCE_VARIABLES_AKAgeRangeSettingsCache
+ __OBJC_$_INSTANCE_VARIABLES_AKAgeRangeSettingsProvider
+ __OBJC_$_INSTANCE_VARIABLES_AKAuthenticatableResource
+ __OBJC_$_INSTANCE_VARIABLES_AKClientConnectionLifecycleManager
+ __OBJC_$_INSTANCE_VARIABLES_AKProtoAccountContext
+ __OBJC_$_INSTANCE_VARIABLES_AKProtoAccountShieldContext
+ __OBJC_$_INSTANCE_VARIABLES_AKServerBackoffContext
+ __OBJC_$_INSTANCE_VARIABLES_AKServerBackoffController
+ __OBJC_$_INSTANCE_VARIABLES_AKServerBackoffHelper
+ __OBJC_$_INSTANCE_VARIABLES_AKXPCConnectionConfiguration
+ __OBJC_$_PROP_LIST_ACAccount_$_AuthKitProto
+ __OBJC_$_PROP_LIST_AKAgeRangeSettings
+ __OBJC_$_PROP_LIST_AKAgeRangeSettingsCache
+ __OBJC_$_PROP_LIST_AKAgeRangeSettingsProvider
+ __OBJC_$_PROP_LIST_AKAuthenticatableResource
+ __OBJC_$_PROP_LIST_AKAuthenticatableResourceProtocol
+ __OBJC_$_PROP_LIST_AKClientConnectionLifecycleManager
+ __OBJC_$_PROP_LIST_AKProtoAccountContext
+ __OBJC_$_PROP_LIST_AKProtoAccountShieldContext
+ __OBJC_$_PROP_LIST_AKServerBackoffContext
+ __OBJC_$_PROP_LIST_AKServerBackoffController
+ __OBJC_$_PROP_LIST_AKServerBackoffHelper
+ __OBJC_$_PROP_LIST_AKXPCConnectionConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKAuthenticatableResourceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKServerBackoffControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKAuthenticatableResourceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKServerBackoffControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_AKAuthenticatableResourceProtocol
+ __OBJC_$_PROTOCOL_REFS_AKServerBackoffControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AKAuthenticatableResource
+ __OBJC_CLASS_PROTOCOLS_$_AKProtoAccountContext
+ __OBJC_CLASS_PROTOCOLS_$_AKServerBackoffHelper
+ __OBJC_CLASS_RO_$_AKAgeRangeSettings
+ __OBJC_CLASS_RO_$_AKAgeRangeSettingsCache
+ __OBJC_CLASS_RO_$_AKAgeRangeSettingsExtractor
+ __OBJC_CLASS_RO_$_AKAgeRangeSettingsProvider
+ __OBJC_CLASS_RO_$_AKAuthenticatableResource
+ __OBJC_CLASS_RO_$_AKClientConnectionLifecycleManager
+ __OBJC_CLASS_RO_$_AKProtoAccountContext
+ __OBJC_CLASS_RO_$_AKProtoAccountShieldContext
+ __OBJC_CLASS_RO_$_AKServerBackoffContext
+ __OBJC_CLASS_RO_$_AKServerBackoffController
+ __OBJC_CLASS_RO_$_AKServerBackoffHelper
+ __OBJC_CLASS_RO_$_AKXPCConnectionConfiguration
+ __OBJC_LABEL_PROTOCOL_$_AKAuthenticatableResourceProtocol
+ __OBJC_LABEL_PROTOCOL_$_AKServerBackoffControllerDelegate
+ __OBJC_METACLASS_RO_$_AKAgeRangeSettings
+ __OBJC_METACLASS_RO_$_AKAgeRangeSettingsCache
+ __OBJC_METACLASS_RO_$_AKAgeRangeSettingsExtractor
+ __OBJC_METACLASS_RO_$_AKAgeRangeSettingsProvider
+ __OBJC_METACLASS_RO_$_AKAuthenticatableResource
+ __OBJC_METACLASS_RO_$_AKClientConnectionLifecycleManager
+ __OBJC_METACLASS_RO_$_AKProtoAccountContext
+ __OBJC_METACLASS_RO_$_AKProtoAccountShieldContext
+ __OBJC_METACLASS_RO_$_AKServerBackoffContext
+ __OBJC_METACLASS_RO_$_AKServerBackoffController
+ __OBJC_METACLASS_RO_$_AKServerBackoffHelper
+ __OBJC_METACLASS_RO_$_AKXPCConnectionConfiguration
+ __OBJC_PROTOCOL_$_AKAuthenticatableResourceProtocol
+ __OBJC_PROTOCOL_$_AKServerBackoffControllerDelegate
+ ___31-[AKAgeRangeSettingsCache init]_block_invoke
+ ___45-[AKAgeRangeSettingsCache clearAgeRangeCache]_block_invoke
+ ___50-[AKAgeRangeSettingsCache _updateAgeRangeSettings]_block_invoke
+ ___55-[AKServerBackoffController configureFromHeaderFields:]_block_invoke
+ ___57-[AKServerBackoffController serverBackoffInfoForContext:]_block_invoke
+ ___57-[AKServerBackoffController serverBackoffInfoForContext:]_block_invoke_2
+ ___60-[AKAgeRangeSettingsProvider refreshAgeRangeWithCompletion:]_block_invoke
+ ___61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke
+ ___61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke_2
+ ___63-[AKClientConnectionLifecycleManager teardownServiceConnection]_block_invoke
+ ___68-[AKServerBackoffController _updateServerBackoffInfoWithDictionary:]_block_invoke
+ ___71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke
+ ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke
+ ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke
+ ___73-[AKAppleIDAuthenticationController _authenticateWithContext:completion:]_block_invoke
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke
+ ___76-[AKAppleIDAuthenticationContext isConfiguredForTokenUpgradeWithCompletion:]_block_invoke
+ ___77-[AKAnisetteProvisioningController attestationDataForRequestData:completion:]_block_invoke
+ ___78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke
+ ___81-[AKAnisetteProvisioningController shouldAllowReprovisionForHostName:completion:]_block_invoke
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke
+ ___block_descriptor_32_e11_B24?08Q16l
+ ___block_descriptor_40_e8_32r_e8_v12?0B8l
+ ___block_descriptor_48_e8_32s40bs_e20_v24?08"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e25_B24?0"NSDictionary"8Q16l
+ ___block_descriptor_48_e8_32s_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48bs_e42_v24?0"AKDeviceListResponse"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs56r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
+ __block_literal_global.114
+ __block_literal_global.152
+ __block_literal_global.172
+ __block_literal_global.175
+ __block_literal_global.195
+ __block_literal_global.198
+ __block_literal_global.229
+ __block_literal_global.390
+ __block_literal_global.409
+ __block_literal_global.68
+ __block_literal_global.73
+ __block_literal_global.82
+ __block_literal_global.85
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$_ageAttestationPhase1FeatureRestricted
+ _objc_msgSend$_attestationDataForRequestData:completion:
+ _objc_msgSend$_attestationDataForRequestData:error:
+ _objc_msgSend$_authenticateWithContext:completion:
+ _objc_msgSend$_backoffContextFromRequest:
+ _objc_msgSend$_clientInfoForContext:
+ _objc_msgSend$_clientInfoForContext:matchingClients:
+ _objc_msgSend$_configurationValueForKey:
+ _objc_msgSend$_deviceListWithContext:completion:
+ _objc_msgSend$_handleAnisetteReprovisionWithRequestURL:anisetteController:completion:
+ _objc_msgSend$_handleAnisetteURLResponse:forRequest:withCompletion:
+ _objc_msgSend$_isBackoffSupported
+ _objc_msgSend$_isStaleClientInfo:
+ _objc_msgSend$_objectForKey:
+ _objc_msgSend$_protoAccountWithError:
+ _objc_msgSend$_sanitizeServerBackoffInfoDict:
+ _objc_msgSend$_serverBackoffDefaults
+ _objc_msgSend$_setConfigurationValue:forKey:
+ _objc_msgSend$_setObject:forKey:
+ _objc_msgSend$_setU13AgeLimit:
+ _objc_msgSend$_setU18AgeLimit:
+ _objc_msgSend$_shouldBackoffContext:matchingClients:
+ _objc_msgSend$_signRequestWithServerBackoffInfoHeader:
+ _objc_msgSend$_telemetryDeviceSessionIDForAccount:
+ _objc_msgSend$_u13AgeLimit
+ _objc_msgSend$_u18AgeLimit
+ _objc_msgSend$_updateAgeRangeSettings
+ _objc_msgSend$_updateServerBackoffInfoWithDictionary:
+ _objc_msgSend$_updatedServerBackoffInfoForClients:cachedClients:
+ _objc_msgSend$activeServiceConnection
+ _objc_msgSend$ak_addServerBackoffInfoHeader:
+ _objc_msgSend$ak_isAppleIDSetupErrorWithCode:
+ _objc_msgSend$appServerName
+ _objc_msgSend$attestationDataForRequestData:error:
+ _objc_msgSend$authenticatableResource
+ _objc_msgSend$biometryType
+ _objc_msgSend$checkSignInOrCreateFlowShieldingWithCompletion:
+ _objc_msgSend$clientBundleID
+ _objc_msgSend$configurationWithRemoteBundleID:
+ _objc_msgSend$configureFromHeaderFields:
+ _objc_msgSend$connectionManager
+ _objc_msgSend$createProtoAccountWithAgeRange:
+ _objc_msgSend$daemonXPCEndpoint
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dca_setAgeRange:
+ _objc_msgSend$dca_setGivenName:
+ _objc_msgSend$defaultConfigDictionary
+ _objc_msgSend$didChangeValueForKey:
+ _objc_msgSend$exportedInterface
+ _objc_msgSend$exportedObject
+ _objc_msgSend$extractAgeRangeConfigFromGlobalConfig:
+ _objc_msgSend$givenNameForAccount:
+ _objc_msgSend$grandSlamEndpointIdentifiersWithCompletion:
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$initWithAccountType:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithConnectionConfiguration:device:provider:
+ _objc_msgSend$initWithIdentifier:connectionConfiguration:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithU13Limit:u18Limit:
+ _objc_msgSend$isAgeAttestationPhase1Enabled
+ _objc_msgSend$isBackoffSupported
+ _objc_msgSend$isClientBackoffDisabled
+ _objc_msgSend$isServerBackoffEnabled
+ _objc_msgSend$machServiceName
+ _objc_msgSend$protoAccount
+ _objc_msgSend$protoAccountType
+ _objc_msgSend$proto_ageRange
+ _objc_msgSend$proto_setAgeRange:
+ _objc_msgSend$proto_setGivenName:
+ _objc_msgSend$proxiedAppBundleID
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$reportTelemetryForContext:backoffType:
+ _objc_msgSend$reportTelemetryForRequest:backoffType:
+ _objc_msgSend$requestURL
+ _objc_msgSend$serverBackoffInfoForContext:
+ _objc_msgSend$serverBackoffInfoForRequest:
+ _objc_msgSend$serviceConnectionConfig
+ _objc_msgSend$setAppServerName:
+ _objc_msgSend$setAuthenticatableResource:
+ _objc_msgSend$setClientBundleID:
+ _objc_msgSend$setGivenName:forAccount:
+ _objc_msgSend$setMachServiceName:
+ _objc_msgSend$setProxiedAppBundleID:
+ _objc_msgSend$setRemoteBundleID:
+ _objc_msgSend$setRemoteClassName:
+ _objc_msgSend$setTelemetryDeviceSessionID:forAccount:
+ _objc_msgSend$setUrl:
+ _objc_msgSend$setUserAgeRange:forAccount:
+ _objc_msgSend$shieldSignInOrCreateFlowsWithError:
+ _objc_msgSend$shouldAllowReprovisionForHostName:completion:
+ _objc_msgSend$shouldBackoffContext:
+ _objc_msgSend$shouldBackoffRequest:
+ _objc_msgSend$teardownServiceConnection
+ _objc_msgSend$url
+ _objc_msgSend$userAgeRangeForAccount:
+ _objc_msgSend$willChangeValueForKey:
+ hasBridgeOS.cold.1
- -[AKAccountManager dcrtRenewalAttempted:]
- -[AKAccountManager dcrtRenewalAttempted:].cold.1
- -[AKAccountManager setDCRTRenewalAttempted:forAccount:]
- -[AKAccountManager telemetryDeviceSessionIDForAccount:].cold.2
- -[AKAccountManager telemetryDeviceSessionIDForAccount:].cold.3
- -[AKAnisetteProvisioningController _attestationDataForRequest:completion:]
- -[AKAnisetteProvisioningController _attestationDataForRequest:error:]
- -[AKAnisetteProvisioningController attestationDataForRequest:error:].cold.1
- -[AKAnisetteProvisioningController dealloc]
- -[AKAnisetteProvisioningController initWithDaemonXPCEndpoint:]
- -[AKAppleIDAuthenticationContext proximityAIDAHandler]
- -[AKAppleIDAuthenticationContext setProximityAIDAHandler:]
- -[AKAppleIDAuthenticationController initWithDaemonXPCEndpoint:]
- -[AKAppleIDAuthenticationController initWithIdentifier:daemonXPCEndpoint:]
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.1
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.2
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.3
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.4
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.5
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.6
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.7
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.8
- -[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:].cold.9
- -[AKAttestationRequestData bodyDataHash]
- -[AKBiometricRatchetContext initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:]
- -[AKFeatureManager isAABrandingEnabled]
- GCC_except_table116
- GCC_except_table120
- GCC_except_table124
- GCC_except_table127
- GCC_except_table132
- GCC_except_table136
- GCC_except_table137
- GCC_except_table139
- GCC_except_table144
- GCC_except_table146
- GCC_except_table150
- GCC_except_table153
- GCC_except_table154
- GCC_except_table161
- GCC_except_table164
- GCC_except_table166
- GCC_except_table170
- GCC_except_table174
- GCC_except_table177
- GCC_except_table181
- GCC_except_table183
- GCC_except_table184
- GCC_except_table191
- GCC_except_table221
- GCC_except_table222
- GCC_except_table223
- GCC_except_table225
- GCC_except_table229
- GCC_except_table231
- GCC_except_table251
- GCC_except_table252
- GCC_except_table268
- GCC_except_table271
- GCC_except_table285
- GCC_except_table286
- GCC_except_table287
- GCC_except_table288
- GCC_except_table289
- GCC_except_table323
- GCC_except_table351
- GCC_except_table83
- GCC_except_table95
- OBJC_IVAR_$_AKAnisetteProvisioningController._anisetteServiceConnection
- OBJC_IVAR_$_AKAnisetteProvisioningController._daemonXPCEndpoint
- OBJC_IVAR_$_AKAnisetteProvisioningController._unfairLock
- OBJC_IVAR_$_AKAppleIDAuthenticationContext._proximityAIDAHandler
- OBJC_IVAR_$_AKAppleIDAuthenticationController._authenticationServiceConnection
- OBJC_IVAR_$_AKAppleIDAuthenticationController._connectionLock
- OBJC_IVAR_$_AKAppleIDAuthenticationController._daemonXPCEndpoint
- OBJC_IVAR_$_AKAttestationRequestData._bodyDataHash
- OBJC_IVAR_$_AKFeatureManager._cachedAABrandingEnabled
- _AKDispatchingAlgorithmStateHeader
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- __105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.362
- __105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.361
- __134-[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:]_block_invoke.96
- __134-[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:]_block_invoke.96.cold.1
- __37+[AKCDPFactory walrusStatusLiveValue]_block_invoke.68
- __37+[AKCDPFactory walrusStatusLiveValue]_block_invoke.73
- __37+[AKCDPFactory walrusStatusLiveValue]_block_invoke.77
- __40+[AKCDPFactory webAccessStatusLiveValue]_block_invoke.81
- __40+[AKCDPFactory webAccessStatusLiveValue]_block_invoke.84
- __44-[AKConfiguration configurationValueForKey:]_block_invoke.122
- __44-[AKURLSession _unsafe_retryTaskIfPossible:]_block_invoke.117
- __55-[AKAnisetteProvisioningController _tearDownConnection]_block_invoke.cold.1
- __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.15
- __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.15.cold.1
- __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.16
- __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.16.cold.1
- __56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.16.cold.2
- __60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.4
- __60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.4.cold.1
- __60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.6.cold.2
- __60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.389
- __60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.389.cold.1
- __60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.389.cold.2
- __62-[AKAnisetteProvisioningController _anisetteServiceConnection]_block_invoke.56
- __62-[AKAnisetteProvisioningController _anisetteServiceConnection]_block_invoke.57
- __62-[AKAnisetteProvisioningController _anisetteServiceConnection]_block_invoke.57.cold.1
- __62-[AKAnisetteProvisioningController _anisetteServiceConnection]_block_invoke.58
- __62-[AKAnisetteProvisioningController _anisetteServiceConnection]_block_invoke_2.cold.1
- __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.12
- __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.12.cold.1
- __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.13
- __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.13.cold.1
- __63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.13.cold.2
- __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke.57
- __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.58
- __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.58.cold.1
- __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.58.cold.2
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.35
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.43
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.43.cold.1
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.43.cold.2
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.43.cold.3
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.43.cold.4
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.43.cold.5
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.46
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.37
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.37.cold.1
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.37.cold.2
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.37.cold.3
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.37.cold.4
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.37.cold.5
- __64-[AKMediaServicesController appMetadataForBundleIDs:completion:]_block_invoke.56
- __65-[AKAlertHandler _showAlertForMissingAppleAccountWithCompletion:]_block_invoke.66
- __65-[AKAlertHandler _showAlertForMissingAppleAccountWithCompletion:]_block_invoke.66.cold.1
- __65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.314
- __65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.314.cold.1
- __65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.315
- __66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.174
- __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.323
- __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.323.cold.1
- __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.326
- __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.326.cold.1
- __68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.326.cold.2
- __69-[AKAnisetteProvisioningController _attestationDataForRequest:error:]_block_invoke.37
- __69-[AKAnisetteProvisioningController _attestationDataForRequest:error:]_block_invoke.37.cold.1
- __69-[AKAnisetteProvisioningController _attestationDataForRequest:error:]_block_invoke.37.cold.2
- __69-[AKAnisetteProvisioningController _attestationDataForRequest:error:]_block_invoke.cold.1
- __69-[AKAppleIDAuthenticationController _authenticationServiceConnection]_block_invoke.403
- __69-[AKAppleIDAuthenticationController _authenticationServiceConnection]_block_invoke.cold.1
- __69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.340
- __69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.340.cold.1
- __69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.341
- __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.46
- __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.46.cold.1
- __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.47
- __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.47.cold.1
- __70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.47.cold.2
- __70-[AKAppleIDAuthenticationController deviceListWithContext:completion:]_block_invoke.312
- __70-[AKAppleIDAuthenticationController deviceListWithContext:completion:]_block_invoke.312.cold.1
- __70-[AKAppleIDAuthenticationController deviceListWithContext:completion:]_block_invoke.313
- __70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.393
- __72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.49
- __72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.49.cold.1
- __72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.49.cold.2
- __72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.394
- __72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.262
- __72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.420
- __72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.420.cold.1
- __72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.421
- __72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.378
- __72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.378.cold.1
- __73-[AKAnisetteProvisioningController attestationDataForRequest:completion:]_block_invoke.38
- __73-[AKAnisetteProvisioningController attestationDataForRequest:completion:]_block_invoke.cold.1
- __73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.408
- __73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.408.cold.1
- __73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.67
- __73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.67.cold.1
- __73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.67.cold.2
- __74-[AKAnisetteProvisioningController _attestationDataForRequest:completion:]_block_invoke.43
- __74-[AKAnisetteProvisioningController _attestationDataForRequest:completion:]_block_invoke.cold.1
- __74-[AKAnisetteProvisioningController _attestationDataForRequest:completion:]_block_invoke.cold.2
- __74-[AKAnisetteProvisioningController _attestationDataForRequest:completion:]_block_invoke.cold.3
- __74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.385
- __74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.385.cold.1
- __74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.386
- __74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.411
- __74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.411.cold.1
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.87
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.87.cold.1
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.87.cold.2
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.88
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.88.cold.1
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.88.cold.2
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.91
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.91.cold.1
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.91.cold.2
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.95
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.95.cold.1
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.95.cold.2
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.cold.1
- __74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke.cold.2
- __76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.413
- __76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.413.cold.1
- __76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.376
- __76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.376.cold.1
- __77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke.25
- __77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke.25.cold.1
- __77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke.25.cold.2
- __77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.316
- __77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.344
- __77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.330
- __78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.377
- __78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.377.cold.1
- __79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.48
- __79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.48.cold.1
- __79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.48.cold.2
- __79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.360
- __80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.348
- __80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.348.cold.1
- __80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.349
- __80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.412
- __80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.412.cold.1
- __80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.405
- __80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.405.cold.1
- __80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.406
- __80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.406.cold.1
- __80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.359
- __80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.381
- __80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.383.cold.1
- __80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.384
- __81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.407
- __81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.407.cold.1
- __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.31
- __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.31.cold.1
- __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.32
- __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.32.cold.1
- __82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.32.cold.2
- __82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.320
- __82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.369
- __82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.369.cold.1
- __82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.370
- __83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.373
- __83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.373.cold.1
- __83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.374
- __83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.375
- __84-[AKAlertHandler _showAlertForInsufficientSecurityLevelWithError:completionHandler:]_block_invoke.88
- __84-[AKAlertHandler _showAlertForInsufficientSecurityLevelWithError:completionHandler:]_block_invoke.88.cold.1
- __84-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:error:]_block_invoke.17
- __84-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:error:]_block_invoke.17.cold.1
- __84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.404
- __86-[AKAppleIDAuthenticationContext presentLoginAlertWithError:title:message:completion:]_block_invoke.610
- __88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.409
- __88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.409.cold.1
- __89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.329
- __90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.336
- __90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.397
- __90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.358
- __90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.358.cold.1
- __90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.380
- __90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.380.cold.1
- __92-[AKAnisetteProvisioningController fetchAnisetteDataAndProvisionIfNecessary:withCompletion:]_block_invoke.19
- __92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.335
- __93-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:withCompletion:]_block_invoke.22
- __94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.334
- __96-[AKAppleIDAuthenticationCommandLineContext _beginDataTaskWithRequest:configuration:completion:]_block_invoke.115
- __96-[AKAppleIDAuthenticationCommandLineContext _beginDataTaskWithRequest:configuration:completion:]_block_invoke.115.cold.1
- __97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.354
- __97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.354.cold.1
- __97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.355
- __97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.355.cold.1
- __98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.410
- __98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.410.cold.1
- ___36-[AKURLDataTask _completeWithError:]_block_invoke
- ___55-[AKAnisetteProvisioningController _tearDownConnection]_block_invoke
- ___62-[AKAnisetteProvisioningController _anisetteServiceConnection]_block_invoke
- ___62-[AKAnisetteProvisioningController _anisetteServiceConnection]_block_invoke_2
- ___69-[AKAnisetteProvisioningController _attestationDataForRequest:error:]_block_invoke
- ___69-[AKAppleIDAuthenticationController _authenticationServiceConnection]_block_invoke
- ___73-[AKAnisetteProvisioningController attestationDataForRequest:completion:]_block_invoke
- ___74-[AKAnisetteProvisioningController _attestationDataForRequest:completion:]_block_invoke
- ___74-[AKAppleIDSession _handleAnissetteURLResponse:forRequest:withCompletion:]_block_invoke
- ___block_descriptor_48_e8_32bs40r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
- __block_literal_global.113
- __block_literal_global.150
- __block_literal_global.170
- __block_literal_global.173
- __block_literal_global.193
- __block_literal_global.196
- __block_literal_global.230
- __block_literal_global.385
- __block_literal_global.388
- __block_literal_global.66
- __block_literal_global.71
- __block_literal_global.80
- __block_literal_global.83
- _objc_msgSend$_attestationDataForRequest:completion:
- _objc_msgSend$_attestationDataForRequest:error:
- _objc_msgSend$_handleAnissetteURLResponse:forRequest:withCompletion:
- _objc_msgSend$attestationDataForRequest:completion:
- _objc_msgSend$attestationDataForRequest:error:
- _objc_msgSend$initWithIdentifier:daemonXPCEndpoint:
- _objc_msgSend$isAABrandingEnabled
CStrings:
+ "/System/AppleInternal/Library/Frameworks/AAAFoundationSwift.framework/AAAFoundationSwift"
+ "/System/AppleInternal/Library/Frameworks/AppStoreComponents.framework/AppStoreComponents"
+ "/System/AppleInternal/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices"
+ "/System/AppleInternal/Library/Frameworks/CoreCDP.framework/CoreCDP"
+ "/System/AppleInternal/Library/Frameworks/CoreCDPUI.framework/CoreCDPUI"
+ "/System/AppleInternal/Library/Frameworks/CoreFollowUp.framework/CoreFollowUp"
+ "/System/AppleInternal/Library/Frameworks/DeviceCheckInternal.framework/DeviceCheckInternal"
+ "/System/AppleInternal/Library/Frameworks/KeychainCircle.framework/KeychainCircle"
+ "/System/AppleInternal/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication"
+ "/System/AppleInternal/Library/Frameworks/RemoteUI.framework/RemoteUI"
+ "/System/AppleInternal/Library/Frameworks/SetupAssistantFramework.framework/SetupAssistantFramework"
+ "/System/AppleInternal/Library/Frameworks/SystemAdministration.framework/SystemAdministration"
+ "/System/AppleInternal/Library/Frameworks/UserManagement.framework/UserManagement"
+ "3"
+ "<%@: %p {\n\tGivenName: %@, \n\tLastName: %@, \n\tAgeRange: %lu, \n}>"
+ "<%@: %p {\n\tUUID: %@,\n\tusername: %@,\n\teditable-username: %@,\n\taltDSID: %@,\n\tDSID: %@,\n\tpassword: %@,\n\tservice-type: %ld,\n\tservice IDs: %@,\n\treason: %@\n\tephemeral: %@,\n\tpassword-only: %@,\n\tpasswordlessToken: %@,\n\tidmsDataToken: %@,\n\tauthentication-type: %@,\n\tauthenticationMode: %@, \n\tisMDMInfoRequired: %@, \n\tupdate-service-tokens: %@,\n\toffer-upgrade: %@,\n\toffer-upgrade-context: %@,\n\tproxying-for-app: %@,\n\tproxied-app-id: %@,\n\tproxied-device: %@,\n\tcompanion-device: %@\n\tmax-login-attempts: %@\n\tappleid-login-enabled: %@\n\thas-empty-password: %@\n\trequest-slt: %@\n\tshort-lived-token: %@\n\tidentity-token: %@\n\ttriggered-by-push: %@\n\tskip-alert: %@\n\tskip-reachability-check: %@\n\tattempt-index: %lu,\n\tmasterKey: %@,\n\tperformUIOutOfProcess: %@,\n\tbroadcastProximityAuthOnly: %@, \n\tVerifyCredentialReason: %@, \n\tEnablePasscodeAuth: %@, \n\tPasscodeOnlyPolicy: %@, \n\tSourceAltDSID: %@, \n\tServiceToken: %@, \n\tisNativeTakeover: %@, \n\tignorePasswordCache: %@, \n\tisRequestedFromOOPViewService: %@, \n\tProxiedAppleID: %@, \n\ttelemetryDeviceSessionID: %@, \n\ttelemetryFlowID: %@, \n\tpiggybackingForTrustedDevice: %@, \n\tprotoAccountContextGivenName: %@, \n\tauthenticatableResource: %@, \n}>"
+ "<%@: %p> \n\treason: %@,\n\tcalloutReason: %@,\n\tdeeplinkURL: %@,\n\tfallbackToNoAuth: %@,\n\tseShortExpiration: %@,\n\tbeginRatchetTitle: %@,\n\tbeginRatchetBody: %@,\n\tshowsLocationWarning: %@,\n\tcountdownText: %@,\n\tfindMyErrorTitle: %@,\n\tfindMyErrorMessage: %@,\n\tnotInteractive: %@,\n"
+ "<%@:%p> serviceName: %@, options: %@, xpcEndpoint: %@"
+ "@\"<AKServerBackoffControllerDelegate>\""
+ "@\"AKAgeRangeSettings\""
+ "@\"AKAgeRangeSettingsCache\""
+ "@\"AKAuthenticatableResource\""
+ "@\"AKClientConnectionLifecycleManager\""
+ "@\"AKProtoAccountContext\""
+ "@\"AKServerBackoffController\""
+ "@\"AKServerBackoffHelper\""
+ "@\"AKXPCConnectionConfiguration\""
+ "@\"NSURL\"24@0:8@\"NSString\"16"
+ "@104@0:8@16@24@32B40B44@48@56B64@68@76@84@92B100"
+ "@24@0:8i16i20"
+ "@40@0:8@16@24Q32"
+ "AKAgeRangeDefaults"
+ "AKAgeRangeSettings"
+ "AKAgeRangeSettingsCache"
+ "AKAgeRangeSettingsCache - Missing dictionary!"
+ "AKAgeRangeSettingsExtractor"
+ "AKAgeRangeSettingsProvider"
+ "AKAgeRangeSettingsProvider - Missing global config result."
+ "AKAgeRangeSettingsProvider - global config fetch failed with %@"
+ "AKAttestationRequestData: signingDataHash: %@, headers: %@"
+ "AKAuthenticatableResource"
+ "AKAuthenticatableResourceProtocol"
+ "AKClientConnectionLifecycleManager"
+ "AKProtoAccountContext"
+ "AKProtoAccountShieldContext"
+ "AKServerBackoffContext"
+ "AKServerBackoffController"
+ "AKServerBackoffController - Unexpected backoff type"
+ "AKServerBackoffControllerDelegate"
+ "AKServerBackoffHelper"
+ "AKXPCConnectionConfiguration"
+ "AUTH_ERROR_ALERT_ACCOUNT_NOT_SUPPORTED_MESSAGE_REBRAND"
+ "AUTH_ERROR_ALERT_CREATE_PASSCODE_MESSAGE_WATCH_REBRAND"
+ "AUTH_ERROR_ALERT_MISSING_APPLE_ACCOUNT_MESSAGE_MACOS_REBRAND"
+ "AUTH_ERROR_ALERT_MISSING_APPLE_ACCOUNT_TITLE_REBRAND"
+ "AUTH_ERROR_ALERT_UNDERAGE_ACCOUNT_MESSAGE_REBRAND"
+ "AUTH_ERROR_ALERT_UNVERIFIED_EMAIL_MESSAGE_REBRAND"
+ "AgeAttestationPhase1"
+ "AgeAttestationPhase1Enabled"
+ "Allow reprovision for hostname: %{private}@, with keyword:  %{private}@"
+ "AppleIDSetupErrorDomain"
+ "AuthKitProto"
+ "B24@?0@8Q16"
+ "Cached age range configurations have changed. Clearing cache..."
+ "Calling out to remote auth service to see if we should shield sign in or create flows."
+ "Client does not have access to DCA account type, falling back on authentication controller"
+ "Connection (%@) to akd activated!"
+ "Connection (%@) to akd tearing down..."
+ "Connection (%@) to akd was interrupted!"
+ "Connection (%@) to akd was invalidated!"
+ "Creating connection with configuration: %@"
+ "Failed to attach Proto Account Information header"
+ "Failed to decode server backoff info header with error: %{private}@"
+ "Failed to load AKAgeRangeDefaults.json"
+ "Failed to parse AKAgeRangeDefaults.json: %@"
+ "Feature AgeAttestationPhase1 enabled - %@"
+ "Feature ServerBackoff enabled - %@"
+ "Fetch PLT upgrade config completed with status - %d and error -%{private}@"
+ "Fetched proto account: %@ with error: %@"
+ "Fetching device list failed with XPC error... retrying once!"
+ "Global config has no countries or target country. Defaulting to use local values."
+ "INLINE_PASSWORD_ALERT_MESSAGE_REBRAND"
+ "INLINE_PASSWORD_ALERT_TITLE_REBRAND"
+ "INLINE_PASSWORD_ALERT_USERNAME_PLACEHOLDER_REBRAND"
+ "No GS keywords returned from idMS, allowing reprovision request for hostname: %{private}@"
+ "No entry found for account country. Defaulting to US"
+ "PASSCODE_ALERT_MESSAGE_IPAD_REBRAND"
+ "Passcode protected: %@ _requirePassword: %@ missingCK: %@"
+ "Plt upgrade is enabled, setting plt"
+ "Refreshing age range"
+ "Reprovision not allowed, the requesting URL is not a GS endpoint."
+ "Reprovision request is not allow for hostname: %{private}@, because it does not contain any keyword from: %{private}@"
+ "Server backoff feature is disabled."
+ "ServerBackoff"
+ "Silent Authentication failed with XPC error... retrying once!"
+ "T@\"<AKServerBackoffControllerDelegate>\",W,N,V_delegate"
+ "T@\"ACAccount\",&,N,V_protoAccount"
+ "T@\"AKAgeRangeSettings\",R,N"
+ "T@\"AKAgeRangeSettingsCache\",R,N,V_ageRangeCache"
+ "T@\"AKAuthenticatableResource\",&,N,V_authenticatableResource"
+ "T@\"AKClientConnectionLifecycleManager\",&,N,V_connectionManager"
+ "T@\"AKProtoAccountContext\",&,N,V_protoAccountContext"
+ "T@\"AKXPCConnectionConfiguration\",&,N,V_serviceConnectionConfig"
+ "T@\"NSData\",R,N,V_signingDataHash"
+ "T@\"NSString\",C,N,Sproto_setGivenName:"
+ "T@\"NSString\",C,N,V_appServerName"
+ "T@\"NSString\",C,N,V_machServiceName"
+ "T@\"NSString\",C,N,V_proxiedAppBundleID"
+ "T@\"NSString\",C,N,V_proxiedBundleID"
+ "T@\"NSString\",C,N,V_remoteBundleID"
+ "T@\"NSString\",C,N,V_remoteClassName"
+ "T@\"NSString\",C,N,V_resourceName"
+ "T@\"NSURL\",C,N,V_url"
+ "T@\"NSXPCConnection\",&,N,V_serviceConnection"
+ "T@\"NSXPCInterface\",&,N,V_exportedInterface"
+ "T@\"NSXPCListenerEndpoint\",&,N,V_daemonXPCEndpoint"
+ "T@,&,N,V_exportedObject"
+ "TB,R,N,GisAgeAttestationPhase1Enabled"
+ "TB,R,N,GisServerBackoffEnabled"
+ "TB,R,N,V_notInteractive"
+ "TQ,N,Sproto_setAgeRange:"
+ "TQ,N,V_ageRange"
+ "TQ,N,V_options"
+ "Telemetry Opt-In Override Enabled, approving Device Session ID vending..."
+ "Telemetry Opt-In detected, but we didn't have an existing device session ID, creating... %@"
+ "Ti,R,N,V_u13Limit"
+ "Ti,R,N,V_u18Limit"
+ "Tq,N,V_internalSiwADefaultHME"
+ "Tq,N,V_resourceType"
+ "Tq,R,N"
+ "T{os_unfair_lock_s=I},N,V_unfairLock"
+ "U13"
+ "U13Limit"
+ "U18"
+ "U18Limit"
+ "Unexpected biometry type, cannot add header: %lu"
+ "Vv32@0:8@\"AKProtoAccountShieldContext\"16@?<v@?@\"NSError\"@\"NSDictionary\">24"
+ "X-Apple-I-Bio-Type"
+ "X-Apple-I-Create-Context"
+ "X-Apple-S-Backoff-Server-Info"
+ "_AKAgeRangeSettingsCacheChangeNotification"
+ "_AKInternalSiwADefaultHME"
+ "_ageAttestationPhase1FeatureRestricted"
+ "_ageRange"
+ "_ageRangeCache"
+ "_ageRangeSettings"
+ "_appServerName"
+ "_attestationDataForRequestData:completion:"
+ "_attestationDataForRequestData:error:"
+ "_authenticatableResource"
+ "_authenticateWithContext:completion:"
+ "_backoffContextFromRequest:"
+ "_cacheIsServerBackoffEnabled"
+ "_cachedAgeAttestationPhase1Enabled"
+ "_clientInfoForContext:"
+ "_clientInfoForContext:matchingClients:"
+ "_configurationValueForKey:"
+ "_connectionManager"
+ "_deviceListWithContext:completion:"
+ "_encodedByAKProtoAccountShieldContext"
+ "_handleAnisetteReprovisionWithRequestURL:anisetteController:completion:"
+ "_handleAnisetteURLResponse:forRequest:withCompletion:"
+ "_internalSiwADefaultHME"
+ "_isBackoffSupported"
+ "_isStaleClientInfo:"
+ "_machServiceName"
+ "_notInteractive"
+ "_notificationQueue"
+ "_objectForKey:"
+ "_options"
+ "_protoAccount"
+ "_protoAccountContext"
+ "_protoAccountType"
+ "_protoAccountTypeLock"
+ "_protoAccountWithError:"
+ "_proxiedBundleID"
+ "_remoteBundleID"
+ "_remoteClassName"
+ "_resourceName"
+ "_resourceType"
+ "_sanitizeServerBackoffInfoDict:"
+ "_serverBackoffController"
+ "_serverBackoffDefaults"
+ "_serverBackoffHelper"
+ "_serverBackoffLock"
+ "_serviceConnection"
+ "_serviceConnectionConfig"
+ "_setConfigurationValue:forKey:"
+ "_setObject:forKey:"
+ "_setU13AgeLimit:"
+ "_setU18AgeLimit:"
+ "_shouldBackoffContext:matchingClients:"
+ "_signRequestWithServerBackoffInfoHeader:"
+ "_signingDataHash"
+ "_telemetryDeviceSessionIDForAccount:"
+ "_u13AgeLimit"
+ "_u13Limit"
+ "_u18AgeLimit"
+ "_u18Limit"
+ "_updateAgeRangeSettings"
+ "_updateServerBackoffInfoWithDictionary:"
+ "_updatedServerBackoffInfoForClients:cachedClients:"
+ "_url"
+ "accessorySync"
+ "account.person.ageRange"
+ "account.person.name.firstName"
+ "account.person.name.lastName"
+ "activeServiceConnection"
+ "ageRange"
+ "ageRangeCache"
+ "ageRangeSettings"
+ "ak_addBiometryTypeHeaderWithValue:"
+ "ak_addCreateInformationHeaderWithValue:"
+ "ak_addServerBackoffInfoHeader:"
+ "ak_isAppleIDSetupCancelError"
+ "ak_isAppleIDSetupErrorWithCode:"
+ "appServerName"
+ "attestationDataForRequestData:error:"
+ "authenticatableResource"
+ "authkit/shield-sign-in-create-flows"
+ "b"
+ "biometryType"
+ "c"
+ "checkSignInOrCreateFlowShieldingWithCompletion:"
+ "clearAgeRangeCache"
+ "clearServerBackoffInfoCache"
+ "clientBackoffDisabled"
+ "com.apple.AuthKit.AgeRangeSettingsCache"
+ "com.apple.AuthKitUIService"
+ "com.apple.aaa.backoff.client"
+ "com.apple.aaa.backoff.server"
+ "com.apple.aaa.serverbackoff"
+ "com.apple.authkit.ageRangeNotifQueue"
+ "com.apple.authkit.remote-view-service.user-info-indicator"
+ "configurationForHostWithBundleID:sceneID:remoteBundleID:"
+ "configurationWithRemoteBundleID:"
+ "configurationWithRemoteBundleID:remoteClassName:"
+ "configureFromHeaderFields:"
+ "connectionManager"
+ "countries"
+ "createProtoAccountWithAgeRange:"
+ "createProtoAccountWithGivenName:ageRange:"
+ "daemonXPCEndpoint"
+ "dataWithContentsOfURL:"
+ "dateByAddingTimeInterval:"
+ "dcaAccount"
+ "dca_ageRange"
+ "dca_givenName"
+ "dca_setAgeRange:"
+ "dca_setGivenName:"
+ "defaultConfigDictionary"
+ "didChangeValueForKey:"
+ "disableDeviceBAA"
+ "disableVMBAA"
+ "exportedInterface"
+ "extractAgeRangeConfigFromGlobalConfig:"
+ "grandSlamEndpointIdentifiersWithCompletion:"
+ "gsEndpointIdentifiers"
+ "i16@0:8"
+ "idms"
+ "indexOfObject:"
+ "initWithAccountType:"
+ "initWithConfiguration:"
+ "initWithConnectionConfiguration:"
+ "initWithConnectionConfiguration:device:provider:"
+ "initWithGivenName:ageRange:"
+ "initWithGivenName:lastName:ageRange:"
+ "initWithIdentifier:connectionConfiguration:"
+ "initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:notInteractive:"
+ "initWithResourceType:resourceName:"
+ "initWithSigningData:requiredHeaders:"
+ "initWithSuiteName:"
+ "initWithU13Limit:u18Limit:"
+ "internalSiwADefaultHME"
+ "isAgeAttestationPhase1Enabled"
+ "isBackoffSupported"
+ "isClientBackoffDisabled"
+ "isConfiguredForTokenUpgradeWithCompletion:"
+ "isDeviceBAADisabled"
+ "isServerBackoffEnabled"
+ "isSignOutInProgress:"
+ "isVMBAADisabled"
+ "json"
+ "machServiceName"
+ "notInteractive"
+ "p"
+ "presentShieldWithContext:completionHandler:"
+ "protoAccount"
+ "protoAccountContext"
+ "protoAccountType"
+ "proto_ageRange"
+ "proto_givenName"
+ "proto_setAgeRange:"
+ "proto_setGivenName:"
+ "proxiedAppBundleID"
+ "proxiedBundleID"
+ "refreshAgeRangeWithCompletion:"
+ "remoteBundleID"
+ "remoteClassName"
+ "replaceObjectAtIndex:withObject:"
+ "reportTelemetryForContext:backoffType:"
+ "reportTelemetryForRequest:backoffType:"
+ "resourceName"
+ "resourceType"
+ "resourceType: %ld, resourceName: %@"
+ "serverBackoffEnabled"
+ "serverBackoffInfoCache"
+ "serverBackoffInfoForContext:"
+ "serverBackoffInfoForRequest:"
+ "serviceConnection"
+ "serviceConnectionConfig"
+ "setAgeRange:"
+ "setAppServerName:"
+ "setAuthenticatableResource:"
+ "setConnectionManager:"
+ "setDaemonXPCEndpoint:"
+ "setInternalSiwADefaultHME:"
+ "setMachServiceName:"
+ "setProtoAccount:"
+ "setProtoAccountContext:"
+ "setProxiedAppBundleID:"
+ "setProxiedBundleID:"
+ "setRemoteBundleID:"
+ "setRemoteClassName:"
+ "setResourceName:"
+ "setResourceType:"
+ "setServiceConnection:"
+ "setServiceConnectionConfig:"
+ "setSignOutInProgress:forAccount:"
+ "setUnfairLock:"
+ "setUrl:"
+ "shieldSignInOrCreateFlows"
+ "shieldSignInOrCreateFlowsWithError:"
+ "shouldAllowReprovisionForHostName:completion:"
+ "shouldBackoffContext:"
+ "shouldBackoffRequest:"
+ "signOutInProgress"
+ "signingDataHash"
+ "signout"
+ "teardownServiceConnection"
+ "threatNotification"
+ "u"
+ "u13Limit"
+ "u18Limit"
+ "unfairLock"
+ "updateAgeRangeCacheWithGlobalConfig:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8@?<v@?B>16"
+ "v24@?0@8@\"NSError\"16"
+ "v32@0:8@16Q24"
+ "willChangeValueForKey:"
+ "{<%@:%p>: type: %ld, identifier: %@,altDSID: %@, forceFetch: %d, fetchDeviceSafetyState: %d, os: %@, services: %@, untrusted: %d, family: %d, serialNumbers: %@, proxiedBundleID: %@, }"
+ "{os_unfair_lock_s=I}16@0:8"
- "<%@: %p {\n\tUUID: %@,\n\tusername: %@,\n\teditable-username: %@,\n\taltDSID: %@,\n\tDSID: %@,\n\tpassword: %@,\n\tservice-type: %ld,\n\tservice IDs: %@,\n\treason: %@\n\tephemeral: %@,\n\tpassword-only: %@,\n\tpasswordlessToken: %@,\n\tidmsDataToken: %@,\n\tauthentication-type: %@,\n\tauthenticationMode: %@, \n\tisMDMInfoRequired: %@, \n\tupdate-service-tokens: %@,\n\toffer-upgrade: %@,\n\toffer-upgrade-context: %@,\n\tproxying-for-app: %@,\n\tproxied-app-id: %@,\n\tproxied-device: %@,\n\tcompanion-device: %@\n\tmax-login-attempts: %@\n\tappleid-login-enabled: %@\n\thas-empty-password: %@\n\trequest-slt: %@\n\tshort-lived-token: %@\n\tidentity-token: %@\n\ttriggered-by-push: %@\n\tskip-alert: %@\n\tskip-reachability-check: %@\n\tattempt-index: %lu,\n\tmasterKey: %@,\n\tperformUIOutOfProcess: %@,\n\tbroadcastProximityAuthOnly: %@, \n\tVerifyCredentialReason: %@, \n\tEnablePasscodeAuth: %@, \n\tPasscodeOnlyPolicy: %@, \n\tSourceAltDSID: %@, \n\tServiceToken: %@, \n\tisNativeTakeover: %@, \n\tignorePasswordCache: %@, \n\tisRequestedFromOOPViewService: %@, \n\tProxiedAppleID: %@, \n\ttelemetryDeviceSessionID: %@, \n\ttelemetryFlowID: %@, \n\tpiggybackingForTrustedDevice: %@, \n}>"
- "<%@: %p> \n\treason: %@,\n\tcalloutReason: %@,\n\tdeeplinkURL: %@,\n\tfallbackToNoAuth: %@,\n\tseShortExpiration: %@,\n\tbeginRatchetTitle: %@,\n\tbeginRatchetBody: %@,\n\tshowsLocationWarning: %@,\n\tcountdownText: %@,\n\tfindMyErrorTitle: %@,\n\tfindMyErrorMessage: %@,\n"
- "@100@0:8@16@24@32B40B44@48@56B64@68@76@84@92"
- "AABranding"
- "AKAppleIDAuthenticationControllerXPCLock"
- "AKAttestationRequestData: bodyHash: %@, headers: %@"
- "AUTH_ERROR_ALERT_ACCOUNT_NOT_SUPPORTED_MESSAGE"
- "AUTH_ERROR_ALERT_CREATE_PASSCODE_MESSAGE_WATCH"
- "AUTH_ERROR_ALERT_MISSING_APPLE_ACCOUNT_MESSAGE_MACOS"
- "AUTH_ERROR_ALERT_MISSING_APPLE_ACCOUNT_TITLE"
- "AUTH_ERROR_ALERT_UNDERAGE_ACCOUNT_MESSAGE"
- "AUTH_ERROR_ALERT_UNVERIFIED_EMAIL_MESSAGE"
- "AppleAccount"
- "Client is attempting to access session identifier without opt-in!"
- "Connection to akd was interrupted!"
- "Connection to akd was invalidated."
- "Exception caught when fetching dcrtRenewalAttempted: %@"
- "Feature AABranding enabled - %@"
- "INLINE_PASSWORD_ALERT_MESSAGE"
- "INLINE_PASSWORD_ALERT_TITLE"
- "INLINE_PASSWORD_ALERT_USERNAME_PLACEHOLDER"
- "PASSCODE_ALERT_MESSAGE_IPAD"
- "Passcode protected: %@"
- "REBRAND"
- "T@\"NSData\",R,N,V_bodyDataHash"
- "T@?,N,V_proximityAIDAHandler"
- "TB,R,N,GisAABrandingEnabled"
- "Tearing down connection to akd..."
- "X-Apple-I-BC"
- "_REBRAND"
- "_attestationDataForRequest:completion:"
- "_attestationDataForRequest:error:"
- "_bodyDataHash"
- "_cachedAABrandingEnabled"
- "_connectionLock"
- "_handleAnissetteURLResponse:forRequest:withCompletion:"
- "_proximityAIDAHandler"
- "aaBrandingEnabled"
- "bodyDataHash"
- "dcrtRenewalAttempted"
- "dcrtRenewalAttempted:"
- "initWithIdentifier:daemonXPCEndpoint:"
- "initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:"
- "isAABrandingEnabled"
- "proximityAIDAHandler"
- "setDCRTRenewalAttempted:forAccount:"
- "setProximityAIDAHandler:"
- "{<%@:%p>: type: %ld, identifier: %@,altDSID: %@, forceFetch: %d, fetchDeviceSafetyState: %d, os: %@, services: %@, untrusted: %d, family: %d, serialNumbers: %@, }"

```
