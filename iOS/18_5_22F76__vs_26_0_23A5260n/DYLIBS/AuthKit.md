## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-493.463.1.0.0
-  __TEXT.__text: 0xd2a58
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_methlist: 0xd08c
-  __TEXT.__const: 0x2871
-  __TEXT.__cstring: 0xe2de
-  __TEXT.__oslogstring: 0x106e4
-  __TEXT.__gcc_except_tab: 0x5480
+512.1.3.0.0
+  __TEXT.__text: 0xda1c8
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_methlist: 0xd8d4
+  __TEXT.__const: 0x6af0
+  __TEXT.__cstring: 0xeaa2
+  __TEXT.__oslogstring: 0x11213
+  __TEXT.__gcc_except_tab: 0x5730
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x16c
-  __TEXT.__unwind_info: 0x3db0
-  __TEXT.__objc_classname: 0x1ad4
-  __TEXT.__objc_methname: 0x20712
-  __TEXT.__objc_methtype: 0x43ca
-  __TEXT.__objc_stubs: 0xe640
-  __DATA_CONST.__got: 0x9c0
-  __DATA_CONST.__const: 0x5ca0
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __TEXT.__unwind_info: 0x4018
+  __TEXT.__objc_classname: 0x1c2f
+  __TEXT.__objc_methname: 0x21a37
+  __TEXT.__objc_methtype: 0x456d
+  __TEXT.__objc_stubs: 0xec80
+  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__const: 0x7f18
+  __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x1e8
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ab0
-  __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x3a0
+  __DATA_CONST.__objc_selrefs: 0x6da8
+  __DATA_CONST.__objc_protorefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __AUTH_CONST.__auth_got: 0x6e8
-  __AUTH_CONST.__const: 0x10f0
-  __AUTH_CONST.__cfstring: 0xea20
-  __AUTH_CONST.__objc_const: 0x23958
+  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__const: 0x1170
+  __AUTH_CONST.__cfstring: 0xf220
+  __AUTH_CONST.__objc_const: 0x255a8
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x2300
-  __DATA.__objc_ivar: 0xf48
-  __DATA.__data: 0x1720
-  __DATA.__bss: 0x638
-  __DATA_DIRTY.__objc_data: 0x1770
-  __DATA_DIRTY.__bss: 0x248
+  __AUTH.__objc_data: 0x25d0
+  __DATA.__objc_ivar: 0xfe8
+  __DATA.__data: 0x18a0
+  __DATA.__bss: 0x640
+  __DATA_DIRTY.__objc_data: 0x17c0
+  __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
-  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
-  - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
+  - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B1019DC-B71B-3F3A-8A2E-ACE0D94BA74B
-  Functions: 5945
-  Symbols:   20572
-  CStrings:  11073
+  UUID: 14683BC9-92B2-35B7-9113-96C26C4FEE34
+  Functions: 6164
+  Symbols:   21487
+  CStrings:  11467
 
Symbols:
+ +[AAFAnalyticsEvent(AuthKit) ak_analyticsEventWithRUITelemetryElement:eventName:error:]
+ +[AAFAnalyticsEvent(AuthKit) elementIndex:]
+ +[AAFAnalyticsEvent(AuthKit) encodeElementNameWithIndexPostFix:prefix:element:activeElements:]
+ +[AAFAnalyticsEvent(AuthKit) encodedElementNameWithDomainPrefix:element:activeElements:]
+ +[AAFAnalyticsEvent(AuthKit) encodedURLWithPrefix:url:]
+ +[AKAccountMigrationContext supportsSecureCoding]
+ +[AKAuthorizationAgeValidator _isAuthorizedCredentialState:]
+ +[AKAuthorizationAgeValidator isValidAgeForRequest:account:]
+ +[AKAuthorizationAgeValidator isValidAgeForRequest:account:].cold.1
+ +[AKAuthorizationAgeValidator isValidAgeForRequest:account:].cold.2
+ +[AKAuthorizationAgeValidator isValidAgeForRequest:account:].cold.3
+ +[AKAuthorizationController isURL:matchingAppleOwnedDomains:]
+ +[AKAuthorizationController isURLFromAllowListDomainsForSharingKey:]
+ +[AKAuthorizationController isURLFromAllowListDomainsForSharingKey:].cold.1
+ +[AKDevice _backupOSVersion]
+ +[AKDictionaryBackedModel supportsSecureCoding]
+ +[AKSymmetricKey supportsSecureCoding]
+ +[AKSymmetricKeyContext supportsSecureCoding]
+ +[AKSymmetricKeyDaemonInterface XPCInterface]
+ +[AKSymmetricKeyDaemonInterface XPCInterface].cold.1
+ +[AKURLConfiguration supportsSecureCoding]
+ +[NSDate(AuthKit) _dateFormatter].cold.1
+ -[AKAccountManager accountIdentifiableTelemetryForAccount:]
+ -[AKAccountManager accountImprovementOptInForAccount:]
+ -[AKAccountManager accountImprovementOptInForAccount:].cold.1
+ -[AKAccountManager accountImprovementOptInValueForAccount:]
+ -[AKAccountManager accountImprovementOptInValueForAccount:].cold.1
+ -[AKAccountManager accountImprovementOptInValueForAccount:].cold.2
+ -[AKAccountManager hasPrimaryiCloudAccountForAltDSID:].cold.1
+ -[AKAccountManager isEligibleToMigrateToChildForAccount:]
+ -[AKAccountManager isEligibleToMigrateToChildForAccount:].cold.1
+ -[AKAccountManager primaryiCloudAccountHasPendingDOB]
+ -[AKAccountManager resetAccountImprovementOptInForAccount:error:]
+ -[AKAccountManager resetAccountImprovementOptInForAccount:error:].cold.1
+ -[AKAccountManager resetAccountImprovementOptInForAccount:error:].cold.2
+ -[AKAccountManager resetAccountImprovementOptInForAccount:error:].cold.3
+ -[AKAccountManager setAccountImprovementOptIn:forAccount:error:]
+ -[AKAccountManager setAccountImprovementOptIn:forAccount:error:].cold.1
+ -[AKAccountManager setAccountImprovementOptIn:forAccount:error:].cold.2
+ -[AKAccountManager setAccountImprovementOptIn:forAccount:error:].cold.3
+ -[AKAccountManager setAccountImprovementOptIn:forAccount:error:].cold.4
+ -[AKAccountManager setIsEligibleToMigrateToChild:forAccount:]
+ -[AKAccountManager setIsEligibleToMigrateToChild:forAccount:].cold.1
+ -[AKAccountManager setPendingDOB:forAccount:]
+ -[AKAccountManager setPendingDOB:forAccount:].cold.1
+ -[AKAccountManager tokenCreationTimeStampWithIdentifier:forAccount:error:]
+ -[AKAccountManager tokenCreationTimeStampWithIdentifier:forAccount:error:].cold.1
+ -[AKAccountManager tokenCreationTimeStampWithIdentifier:forAccount:error:].cold.2
+ -[AKAccountManager tokenCreationTimeStampWithIdentifier:forAccount:error:].cold.3
+ -[AKAccountMigrationContext .cxx_destruct]
+ -[AKAccountMigrationContext copyWithZone:]
+ -[AKAccountMigrationContext debugDescription]
+ -[AKAccountMigrationContext encodeWithCoder:]
+ -[AKAccountMigrationContext initWithCoder:]
+ -[AKAccountMigrationContext initWithPendingDOB:]
+ -[AKAccountMigrationContext pendingDOB]
+ -[AKAppleIDAuthenticationContext accountMigrationContext]
+ -[AKAppleIDAuthenticationContext biometricSkipPasscodeFallback]
+ -[AKAppleIDAuthenticationContext idmsData]
+ -[AKAppleIDAuthenticationContext isConfiguredForAccountCreation]
+ -[AKAppleIDAuthenticationContext proxiedToken]
+ -[AKAppleIDAuthenticationContext requestedNewAccountAgeRange]
+ -[AKAppleIDAuthenticationContext setAccountMigrationContext:]
+ -[AKAppleIDAuthenticationContext setBiometricSkipPasscodeFallback:]
+ -[AKAppleIDAuthenticationContext setIdmsData:]
+ -[AKAppleIDAuthenticationContext setProxiedToken:]
+ -[AKAppleIDAuthenticationContext setRequestedNewAccountAgeRange:]
+ -[AKAppleIDAuthenticationContext setRequestedNewAccountAgeRange:].cold.1
+ -[AKAppleIDSession _canHandleAnisetteURLResponse:]
+ -[AKAttestationRequestData initWithRequestURL:signingDataHash:requiredHeaders:]
+ -[AKAttestationRequestData init]
+ -[AKAuthorizationController _allowListDomainsForSharingKey]
+ -[AKAuthorizationController _allowListDomainsForSharingKey].cold.1
+ -[AKAuthorizationController _sharedKeyInfo]
+ -[AKAuthorizationController _sharedKeyInfo].cold.1
+ -[AKAuthorizationPresentationContext iconTypeID]
+ -[AKBaseDaemonConnection .cxx_destruct]
+ -[AKBaseDaemonConnection XPCInterface]
+ -[AKBaseDaemonConnection _connectionInterruptionHandler]
+ -[AKBaseDaemonConnection _connectionInterruptionHandler].cold.1
+ -[AKBaseDaemonConnection _connectionInvalidationHandler]
+ -[AKBaseDaemonConnection _connectionInvalidationHandler].cold.1
+ -[AKBaseDaemonConnection _connection]
+ -[AKBaseDaemonConnection dealloc]
+ -[AKBaseDaemonConnection dealloc].cold.1
+ -[AKBaseDaemonConnection initWithListenerEndpoint:]
+ -[AKBaseDaemonConnection init]
+ -[AKBaseDaemonConnection listenerEndpoint]
+ -[AKBaseDaemonConnection machServiceName]
+ -[AKBaseDaemonConnection remoteObjectProxyWithErrorHandler:]
+ -[AKBaseDaemonConnection synchronousRemoteObjectProxyWithErrorHandler:]
+ -[AKConfiguration accountAccessTelemetryOptInFFOverride]
+ -[AKConfiguration setAccountAccessTelemetryOptInFFOverride:]
+ -[AKConfiguration setAccountAccessTelemetryOptInOverride:]
+ -[AKConfiguration setShouldEnableAccountImprovementOptIn:]
+ -[AKConfiguration shouldEnableAccountImprovementOptIn]
+ -[AKCredentialRequestContext _iconTypeID]
+ -[AKCredentialRequestContext set_iconTypeID:]
+ -[AKDictionaryBackedModel .cxx_destruct]
+ -[AKDictionaryBackedModel encodeWithCoder:]
+ -[AKDictionaryBackedModel initWithCoder:]
+ -[AKDictionaryBackedModel initWithValues:]
+ -[AKDictionaryBackedModel initWithValues:].cold.1
+ -[AKDictionaryBackedModel isEqual:]
+ -[AKDictionaryBackedModel objectForKey:]
+ -[AKDictionaryBackedModel objectForKey:].cold.1
+ -[AKDictionaryBackedModel objectForKey:as:]
+ -[AKDictionaryBackedModel parseValue:atKey:]
+ -[AKDictionaryBackedModel setValues:]
+ -[AKDictionaryBackedModel validObjectForKey:]
+ -[AKDictionaryBackedModel validationRequirements]
+ -[AKDictionaryBackedModel values]
+ -[AKFeatureManager init].cold.22
+ -[AKFeatureManager init].cold.23
+ -[AKFeatureManager init].cold.24
+ -[AKFeatureManager init].cold.25
+ -[AKFeatureManager init].cold.26
+ -[AKFeatureManager init].cold.27
+ -[AKFeatureManager init].cold.28
+ -[AKFeatureManager init].cold.29
+ -[AKFeatureManager init].cold.30
+ -[AKFeatureManager init].cold.31
+ -[AKFeatureManager init].cold.32
+ -[AKFeatureManager init].cold.33
+ -[AKFeatureManager isAccountImprovementProgramEnabled]
+ -[AKFeatureManager isAgeBasedAccountSupportEnabled]
+ -[AKFeatureManager isAgeMigrationEnabled]
+ -[AKFeatureManager isAuthKitSolariumFeatureEnabled]
+ -[AKFeatureManager isPRKHealingEnabled]
+ -[AKFeatureManager isPRKTokenGenerationEnabled]
+ -[AKFeatureManager isPhysicalDeviceBAAEnabled]
+ -[AKFeatureManager isPhysicalDeviceBAAValidationEnabled]
+ -[AKFeatureManager isRUITelemetryEnabled]
+ -[AKFeatureManager isSIWALandscapeModeEnabled]
+ -[AKFeatureManager isSecurePakeEnabled]
+ -[AKFeatureManager isServerBackoffOptInEnabled]
+ -[AKFeatureManager isThreatNotificationCFUEnabled]
+ -[AKFollowUpFactoryImpl _groupIdentifierFromPayload:]
+ -[AKFollowUpFactoryImpl _uniqueIdentifierFromPayload:]
+ -[AKProtoAccountContext initWithAgeRange:]
+ -[AKProtoAccountContext init]
+ -[AKProtoAccountContext setShouldForceShieldUI:]
+ -[AKProtoAccountContext shouldForceShieldUI]
+ -[AKProtoAccountShieldContext pendingDOB]
+ -[AKProtoAccountShieldContext setPendingDOB:]
+ -[AKServerRequestConfiguration setUrlConfiguration:]
+ -[AKServerRequestConfiguration urlConfiguration]
+ -[AKSymmetricKey .cxx_destruct]
+ -[AKSymmetricKey copyWithZone:]
+ -[AKSymmetricKey description]
+ -[AKSymmetricKey encodeWithCoder:]
+ -[AKSymmetricKey initFromSymmetricKey:]
+ -[AKSymmetricKey initWithCoder:]
+ -[AKSymmetricKey initWithKeyData:keySpecifier:keyDomain:]
+ -[AKSymmetricKey keyData]
+ -[AKSymmetricKey keyDomain]
+ -[AKSymmetricKey keySpecifier]
+ -[AKSymmetricKeyContext .cxx_destruct]
+ -[AKSymmetricKeyContext clientLabel]
+ -[AKSymmetricKeyContext copyWithZone:]
+ -[AKSymmetricKeyContext description]
+ -[AKSymmetricKeyContext encodeWithCoder:]
+ -[AKSymmetricKeyContext initWithCoder:]
+ -[AKSymmetricKeyContext initWithRequestedSubdomains:]
+ -[AKSymmetricKeyContext initWithRequestedSubdomains:clientLabel:]
+ -[AKSymmetricKeyContext requestedSubdomains]
+ -[AKSymmetricKeyController .cxx_destruct]
+ -[AKSymmetricKeyController initWithDaemonXPCEndpoint:]
+ -[AKSymmetricKeyController init]
+ -[AKSymmetricKeyController registerForSymmetricKeyWithContext:completion:]
+ -[AKSymmetricKeyDaemonConnection .cxx_destruct]
+ -[AKSymmetricKeyDaemonConnection _connectionInterruptionHandler]
+ -[AKSymmetricKeyDaemonConnection _connectionInterruptionHandler].cold.1
+ -[AKSymmetricKeyDaemonConnection _connectionInvalidationHandler]
+ -[AKSymmetricKeyDaemonConnection _connectionInvalidationHandler].cold.1
+ -[AKSymmetricKeyDaemonConnection _connection]
+ -[AKSymmetricKeyDaemonConnection dealloc]
+ -[AKSymmetricKeyDaemonConnection dealloc].cold.1
+ -[AKSymmetricKeyDaemonConnection initWithListenerEndpoint:]
+ -[AKSymmetricKeyDaemonConnection init]
+ -[AKSymmetricKeyDaemonConnection listenerEndpoint]
+ -[AKSymmetricKeyDaemonConnection remoteObjectProxyWithErrorHandler:]
+ -[AKSymmetricKeyDaemonConnection synchronousRemoteObjectProxyWithErrorHandler:]
+ -[AKURLBag _urlConfigurationAtKey:fromURLBag:]
+ -[AKURLBag allowListDomainsForSharingKey]
+ -[AKURLBag isAccountAccessTelemetryOptInEnabled]
+ -[AKURLBag isSIWAForPAAChildEnabled]
+ -[AKURLBag securePakeStepURL]
+ -[AKURLBag urlConfigurationForKey:fromCache:completion:]
+ -[AKURLConfiguration .cxx_destruct]
+ -[AKURLConfiguration encodeWithCoder:]
+ -[AKURLConfiguration initWithCoder:]
+ -[AKURLConfiguration initWithDictionary:]
+ -[AKURLConfiguration isBaaEnabled]
+ -[AKURLConfiguration uiType]
+ -[AKURLConfiguration url]
+ -[AKUserInformation isEligibleToMigrateToChild]
+ -[AKUserInformation setIsEligibleToMigrateToChild:]
+ -[NSDictionary(AuthKit) hasValueAtKey:ofType:]
+ -[NSDictionary(AuthKit) hasValueAtKey:ofType:].cold.1
+ -[NSDictionary(AuthKit) hasValueAtKey:ofType:].cold.2
+ -[NSMutableURLRequest(AuthKit) ak_addAuthorizationHeaderWithAltIdentityToken:forAltDSID:]
+ -[NSMutableURLRequest(AuthKit) ak_addJSONResponseAcceptHeader]
+ -[NSMutableURLRequest(AuthKit) ak_addServerBackoffOptInHeader:]
+ GCC_except_table110
+ GCC_except_table116
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table129
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table154
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table237
+ GCC_except_table238
+ GCC_except_table254
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table271
+ GCC_except_table272
+ GCC_except_table309
+ GCC_except_table310
+ GCC_except_table319
+ GCC_except_table320
+ GCC_except_table321
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table324
+ GCC_except_table325
+ GCC_except_table326
+ GCC_except_table364
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table89
+ _ACRTRoot_public_key
+ _AKAccountAccessTelemetryEnabledKey
+ _AKAccountImprovementErrorDomain
+ _AKAppleIDAuthenticationAppProvidedContextAgeMigration
+ _AKAppleIDAuthenticationAppProvidedContextConnectDependent
+ _AKAppleIDAuthenticationContextSpyglassSignOut
+ _AKAppleIDAuthenticationContextTokenHealing
+ _AKDidAccountRecovery
+ _AKFollowUpExtensionIdentifierThreatNotification
+ _AKGeneratePasswordResetKey
+ _AKIconTypeIDKey
+ _AKIsEligibleToMigrateToChildKey
+ _AKPrivateEmailControllerDidRegisterNewEmail
+ _AKPrivateEmailControllerDidUnregistredEmail
+ _AKRequestHeaderDebugErrorKey
+ _AKRequestHeaderDeviceTokenKey
+ _AKServerBackoffOptInHeaderKey
+ _AKSharedKeyChangeNotification
+ _AKSymmetricKeyMachService
+ _AKURLBagKeyAccountAccessOptInEnabled
+ _AKURLBagKeyCreateTeenAccount
+ _AKURLBagKeyDeviceBAADisabled
+ _AKURLBagKeyFollowUpAcknowledge
+ _AKURLBagKeySecurePakeStep
+ _AKURLBagKeyVMBAADisabled
+ _ApplePlatformBackportECCRootCAG1
+ _ApplePlatformBackportECCRootCAG1PublicKey
+ _ApplePlatformBackportECCRootCAG1SKID
+ _ApplePlatformBackportECCRootCAG1SPKI
+ _ApplePlatformBackportECCRootCAG1_public_key
+ _ApplePlatformBackportECCRootCAG1_skid
+ _ApplePlatformBackportECCRootCAG1_spki
+ _ApplePlatformBackportRSARootCAG1
+ _ApplePlatformBackportRSARootCAG1PublicKey
+ _ApplePlatformBackportRSARootCAG1SKID
+ _ApplePlatformBackportRSARootCAG1SPKI
+ _ApplePlatformBackportRSARootCAG1_public_key
+ _ApplePlatformBackportRSARootCAG1_skid
+ _ApplePlatformBackportRSARootCAG1_spki
+ _ApplePlatformBootstrapECCRootCAG1
+ _ApplePlatformBootstrapECCRootCAG1PublicKey
+ _ApplePlatformBootstrapECCRootCAG1SKID
+ _ApplePlatformBootstrapECCRootCAG1SPKI
+ _ApplePlatformBootstrapECCRootCAG1_public_key
+ _ApplePlatformBootstrapECCRootCAG1_skid
+ _ApplePlatformBootstrapECCRootCAG1_spki
+ _ApplePlatformCodeSigningECCRootCAG1
+ _ApplePlatformCodeSigningECCRootCAG1PublicKey
+ _ApplePlatformCodeSigningECCRootCAG1SKID
+ _ApplePlatformCodeSigningECCRootCAG1SPKI
+ _ApplePlatformCodeSigningECCRootCAG1_public_key
+ _ApplePlatformCodeSigningECCRootCAG1_skid
+ _ApplePlatformCodeSigningECCRootCAG1_spki
+ _ApplePlatformCodeSigningRSARootCAG1
+ _ApplePlatformCodeSigningRSARootCAG1PublicKey
+ _ApplePlatformCodeSigningRSARootCAG1SKID
+ _ApplePlatformCodeSigningRSARootCAG1SPKI
+ _ApplePlatformCodeSigningRSARootCAG1_public_key
+ _ApplePlatformCodeSigningRSARootCAG1_skid
+ _ApplePlatformCodeSigningRSARootCAG1_spki
+ _ApplePlatformDeveloperECCRootCAG1
+ _ApplePlatformDeveloperECCRootCAG1PublicKey
+ _ApplePlatformDeveloperECCRootCAG1SKID
+ _ApplePlatformDeveloperECCRootCAG1SPKI
+ _ApplePlatformDeveloperECCRootCAG1_public_key
+ _ApplePlatformDeveloperECCRootCAG1_skid
+ _ApplePlatformDeveloperECCRootCAG1_spki
+ _ApplePlatformDeveloperRSARootCAG1
+ _ApplePlatformDeveloperRSARootCAG1PublicKey
+ _ApplePlatformDeveloperRSARootCAG1SKID
+ _ApplePlatformDeveloperRSARootCAG1SPKI
+ _ApplePlatformDeveloperRSARootCAG1_public_key
+ _ApplePlatformDeveloperRSARootCAG1_skid
+ _ApplePlatformDeveloperRSARootCAG1_spki
+ _ApplePlatformECCRootCAG1
+ _ApplePlatformECCRootCAG1PublicKey
+ _ApplePlatformECCRootCAG1SKID
+ _ApplePlatformECCRootCAG1SPKI
+ _ApplePlatformECCRootCAG1_public_key
+ _ApplePlatformECCRootCAG1_skid
+ _ApplePlatformECCRootCAG1_spki
+ _ApplePlatformMultipurposeECCRootCAG1
+ _ApplePlatformMultipurposeECCRootCAG1PublicKey
+ _ApplePlatformMultipurposeECCRootCAG1SKID
+ _ApplePlatformMultipurposeECCRootCAG1SPKI
+ _ApplePlatformMultipurposeECCRootCAG1_public_key
+ _ApplePlatformMultipurposeECCRootCAG1_skid
+ _ApplePlatformMultipurposeECCRootCAG1_spki
+ _ApplePlatformMultipurposeRSARootCAG1
+ _ApplePlatformMultipurposeRSARootCAG1PublicKey
+ _ApplePlatformMultipurposeRSARootCAG1SKID
+ _ApplePlatformMultipurposeRSARootCAG1SPKI
+ _ApplePlatformMultipurposeRSARootCAG1_public_key
+ _ApplePlatformMultipurposeRSARootCAG1_skid
+ _ApplePlatformMultipurposeRSARootCAG1_spki
+ _ApplePlatformRSARootCAG1
+ _ApplePlatformRSARootCAG1PublicKey
+ _ApplePlatformRSARootCAG1SKID
+ _ApplePlatformRSARootCAG1SPKI
+ _ApplePlatformRSARootCAG1_public_key
+ _ApplePlatformRSARootCAG1_skid
+ _ApplePlatformRSARootCAG1_spki
+ _ApplePlatformTLSECCRootCAG1
+ _ApplePlatformTLSECCRootCAG1PublicKey
+ _ApplePlatformTLSECCRootCAG1SKID
+ _ApplePlatformTLSECCRootCAG1SPKI
+ _ApplePlatformTLSECCRootCAG1_public_key
+ _ApplePlatformTLSECCRootCAG1_skid
+ _ApplePlatformTLSECCRootCAG1_spki
+ _ApplePlatformTLSRSARootCAG1
+ _ApplePlatformTLSRSARootCAG1PublicKey
+ _ApplePlatformTLSRSARootCAG1SKID
+ _ApplePlatformTLSRSARootCAG1SPKI
+ _ApplePlatformTLSRSARootCAG1_public_key
+ _ApplePlatformTLSRSARootCAG1_skid
+ _ApplePlatformTLSRSARootCAG1_spki
+ _AppleRootCAG2SPKI
+ _AppleRootCAG2_skid
+ _AppleRootCAG2_spki
+ _AppleRootCAG3SPKI
+ _AppleRootCAG3_skid
+ _AppleRootCAG3_spki
+ _AppleRootCA_skid
+ _AppleRootCA_spki
+ _AppleRootFlags
+ _AppleRootSPKIs
+ _BASepAppRoot_public_key
+ _BASepAppRoot_skid
+ _BASepAppRoot_spki
+ _BASystemRoot_public_key
+ _BASystemRoot_skid
+ _BASystemRoot_spki
+ _BAUserRoot_public_key
+ _BAUserRoot_skid
+ _BAUserRoot_spki
+ _BlockedYonkers_spki
+ _CTEvaluateICDPFederation
+ _CTGetICDPFederationType
+ _DevICDPFederationRoot152PublicKey
+ _DevICDPFederationRoot152SKID
+ _DevICDPFederationRoot152_public_key
+ _DevICDPFederationRoot152_skid
+ _DevICDPFederationRoot4PublicKey
+ _DevICDPFederationRoot4SKID
+ _DevICDPFederationRoot4_public_key
+ _DevICDPFederationRoot4_skid
+ _ICDPFederationRoot101PublicKey
+ _ICDPFederationRoot101SKID
+ _ICDPFederationRoot101_public_key
+ _ICDPFederationRoot101_skid
+ _ICDPFederationRoot102PublicKey
+ _ICDPFederationRoot102SKID
+ _ICDPFederationRoot102_public_key
+ _ICDPFederationRoot102_skid
+ _ICDPFederationRoot103PublicKey
+ _ICDPFederationRoot103SKID
+ _ICDPFederationRoot103_public_key
+ _ICDPFederationRoot103_skid
+ _ICDPFederationRoot310PublicKey
+ _ICDPFederationRoot310SKID
+ _ICDPFederationRoot310_public_key
+ _ICDPFederationRoot310_skid
+ _ICDPFederationRoot500PublicKey
+ _ICDPFederationRoot500SKID
+ _ICDPFederationRoot500_public_key
+ _ICDPFederationRoot500_skid
+ _MFi4RootSPKI
+ _MFi4Root_public_key
+ _MFi4Root_skid
+ _MFi4Root_spki
+ _OBJC_CLASS_$_AKAccountMigrationContext
+ _OBJC_CLASS_$_AKAuthorizationAgeValidator
+ _OBJC_CLASS_$_AKBaseDaemonConnection
+ _OBJC_CLASS_$_AKDictionaryBackedModel
+ _OBJC_CLASS_$_AKSymmetricKey
+ _OBJC_CLASS_$_AKSymmetricKeyContext
+ _OBJC_CLASS_$_AKSymmetricKeyController
+ _OBJC_CLASS_$_AKSymmetricKeyDaemonConnection
+ _OBJC_CLASS_$_AKSymmetricKeyDaemonInterface
+ _OBJC_CLASS_$_AKURLConfiguration
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$__SFSymmetricKeySpecifier
+ _OBJC_IVAR_$_AKAccountManager._fetchAccountsLock
+ _OBJC_IVAR_$_AKAccountMigrationContext._pendingDOB
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._accountMigrationContext
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._biometricSkipPasscodeFallback
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._idmsData
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._proxiedToken
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._requestedNewAccountAgeRange
+ _OBJC_IVAR_$_AKAuthorizationPresentationContext._iconTypeID
+ _OBJC_IVAR_$_AKBaseDaemonConnection._connection
+ _OBJC_IVAR_$_AKBaseDaemonConnection._listenerEndpoint
+ _OBJC_IVAR_$_AKBaseDaemonConnection._unfairLock
+ _OBJC_IVAR_$_AKConfiguration._accountAccessTelemetryOptInFFOverride
+ _OBJC_IVAR_$_AKConfiguration._shouldEnableAccountImprovementOptIn
+ _OBJC_IVAR_$_AKCredentialRequestContext._iconTypeID
+ _OBJC_IVAR_$_AKDictionaryBackedModel._values
+ _OBJC_IVAR_$_AKFeatureManager._cachedAccountImprovementProgramEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedAgeBasedAccountSupportEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedAgeMigrationEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedIsAuthKitSolariumFeatureEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedPRKGenerationEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedPRKHealingEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedRUITelemetryEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedSIWALandscapeModeEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedSecurePakeEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedServerBackoffOptInEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedThreatNotificationCFUEnabled
+ _OBJC_IVAR_$_AKProtoAccountContext._shouldForceShieldUI
+ _OBJC_IVAR_$_AKServerRequestConfiguration._urlConfiguration
+ _OBJC_IVAR_$_AKSymmetricKey._keyData
+ _OBJC_IVAR_$_AKSymmetricKey._keyDomain
+ _OBJC_IVAR_$_AKSymmetricKey._keySpecifier
+ _OBJC_IVAR_$_AKSymmetricKeyContext._clientLabel
+ _OBJC_IVAR_$_AKSymmetricKeyContext._requestedSubdomains
+ _OBJC_IVAR_$_AKSymmetricKeyController._daemonConnection
+ _OBJC_IVAR_$_AKSymmetricKeyDaemonConnection._connection
+ _OBJC_IVAR_$_AKSymmetricKeyDaemonConnection._listenerEndpoint
+ _OBJC_IVAR_$_AKSymmetricKeyDaemonConnection._unfairLock
+ _OBJC_IVAR_$_AKURLConfiguration._isBaaEnabled
+ _OBJC_IVAR_$_AKURLConfiguration._uiType
+ _OBJC_IVAR_$_AKURLConfiguration._url
+ _OBJC_IVAR_$_AKUserInformation._isEligibleToMigrateToChild
+ _OBJC_METACLASS_$_AKAccountMigrationContext
+ _OBJC_METACLASS_$_AKAuthorizationAgeValidator
+ _OBJC_METACLASS_$_AKBaseDaemonConnection
+ _OBJC_METACLASS_$_AKDictionaryBackedModel
+ _OBJC_METACLASS_$_AKSymmetricKey
+ _OBJC_METACLASS_$_AKSymmetricKeyContext
+ _OBJC_METACLASS_$_AKSymmetricKeyController
+ _OBJC_METACLASS_$_AKSymmetricKeyDaemonConnection
+ _OBJC_METACLASS_$_AKSymmetricKeyDaemonInterface
+ _OBJC_METACLASS_$_AKURLConfiguration
+ _SEKProdRoot_public_key
+ _SEKProdRoot_skid
+ _SEKTestRoot_public_key
+ _SEKTestRoot_skid
+ _TestApplePlatformBackportECCRootCAG1
+ _TestApplePlatformBackportECCRootCAG1PublicKey
+ _TestApplePlatformBackportECCRootCAG1SKID
+ _TestApplePlatformBackportECCRootCAG1SPKI
+ _TestApplePlatformBackportECCRootCAG1_public_key
+ _TestApplePlatformBackportECCRootCAG1_skid
+ _TestApplePlatformBackportECCRootCAG1_spki
+ _TestApplePlatformBackportRSARootCAG1
+ _TestApplePlatformBackportRSARootCAG1PublicKey
+ _TestApplePlatformBackportRSARootCAG1SKID
+ _TestApplePlatformBackportRSARootCAG1SPKI
+ _TestApplePlatformBackportRSARootCAG1_public_key
+ _TestApplePlatformBackportRSARootCAG1_skid
+ _TestApplePlatformBackportRSARootCAG1_spki
+ _TestApplePlatformBootstrapECCRootCAG1
+ _TestApplePlatformBootstrapECCRootCAG1PublicKey
+ _TestApplePlatformBootstrapECCRootCAG1SKID
+ _TestApplePlatformBootstrapECCRootCAG1SPKI
+ _TestApplePlatformBootstrapECCRootCAG1_public_key
+ _TestApplePlatformBootstrapECCRootCAG1_skid
+ _TestApplePlatformBootstrapECCRootCAG1_spki
+ _TestApplePlatformCodeSigningECCRootCAG1
+ _TestApplePlatformCodeSigningECCRootCAG1PublicKey
+ _TestApplePlatformCodeSigningECCRootCAG1SKID
+ _TestApplePlatformCodeSigningECCRootCAG1SPKI
+ _TestApplePlatformCodeSigningECCRootCAG1_public_key
+ _TestApplePlatformCodeSigningECCRootCAG1_skid
+ _TestApplePlatformCodeSigningECCRootCAG1_spki
+ _TestApplePlatformCodeSigningRSARootCAG1
+ _TestApplePlatformCodeSigningRSARootCAG1PublicKey
+ _TestApplePlatformCodeSigningRSARootCAG1SKID
+ _TestApplePlatformCodeSigningRSARootCAG1SPKI
+ _TestApplePlatformCodeSigningRSARootCAG1_public_key
+ _TestApplePlatformCodeSigningRSARootCAG1_skid
+ _TestApplePlatformCodeSigningRSARootCAG1_spki
+ _TestApplePlatformDeveloperECCRootCAG1
+ _TestApplePlatformDeveloperECCRootCAG1PublicKey
+ _TestApplePlatformDeveloperECCRootCAG1SKID
+ _TestApplePlatformDeveloperECCRootCAG1SPKI
+ _TestApplePlatformDeveloperECCRootCAG1_public_key
+ _TestApplePlatformDeveloperECCRootCAG1_skid
+ _TestApplePlatformDeveloperECCRootCAG1_spki
+ _TestApplePlatformDeveloperRSARootCAG1
+ _TestApplePlatformDeveloperRSARootCAG1PublicKey
+ _TestApplePlatformDeveloperRSARootCAG1SKID
+ _TestApplePlatformDeveloperRSARootCAG1SPKI
+ _TestApplePlatformDeveloperRSARootCAG1_public_key
+ _TestApplePlatformDeveloperRSARootCAG1_skid
+ _TestApplePlatformDeveloperRSARootCAG1_spki
+ _TestApplePlatformECCRootCAG1
+ _TestApplePlatformECCRootCAG1PublicKey
+ _TestApplePlatformECCRootCAG1SKID
+ _TestApplePlatformECCRootCAG1SPKI
+ _TestApplePlatformECCRootCAG1_public_key
+ _TestApplePlatformECCRootCAG1_skid
+ _TestApplePlatformECCRootCAG1_spki
+ _TestApplePlatformMultipurposeECCRootCAG1
+ _TestApplePlatformMultipurposeECCRootCAG1PublicKey
+ _TestApplePlatformMultipurposeECCRootCAG1SKID
+ _TestApplePlatformMultipurposeECCRootCAG1SPKI
+ _TestApplePlatformMultipurposeECCRootCAG1_public_key
+ _TestApplePlatformMultipurposeECCRootCAG1_skid
+ _TestApplePlatformMultipurposeECCRootCAG1_spki
+ _TestApplePlatformMultipurposeRSARootCAG1
+ _TestApplePlatformMultipurposeRSARootCAG1PublicKey
+ _TestApplePlatformMultipurposeRSARootCAG1SKID
+ _TestApplePlatformMultipurposeRSARootCAG1SPKI
+ _TestApplePlatformMultipurposeRSARootCAG1_public_key
+ _TestApplePlatformMultipurposeRSARootCAG1_skid
+ _TestApplePlatformMultipurposeRSARootCAG1_spki
+ _TestApplePlatformRSARootCAG1
+ _TestApplePlatformRSARootCAG1PublicKey
+ _TestApplePlatformRSARootCAG1SKID
+ _TestApplePlatformRSARootCAG1SPKI
+ _TestApplePlatformRSARootCAG1_public_key
+ _TestApplePlatformRSARootCAG1_skid
+ _TestApplePlatformRSARootCAG1_spki
+ _TestApplePlatformTLSECCRootCAG1
+ _TestApplePlatformTLSECCRootCAG1PublicKey
+ _TestApplePlatformTLSECCRootCAG1SKID
+ _TestApplePlatformTLSECCRootCAG1SPKI
+ _TestApplePlatformTLSECCRootCAG1_public_key
+ _TestApplePlatformTLSECCRootCAG1_skid
+ _TestApplePlatformTLSECCRootCAG1_spki
+ _TestApplePlatformTLSRSARootCAG1
+ _TestApplePlatformTLSRSARootCAG1PublicKey
+ _TestApplePlatformTLSRSARootCAG1SKID
+ _TestApplePlatformTLSRSARootCAG1SPKI
+ _TestApplePlatformTLSRSARootCAG1_public_key
+ _TestApplePlatformTLSRSARootCAG1_skid
+ _TestApplePlatformTLSRSARootCAG1_spki
+ _TestAppleRootCAG2
+ _TestAppleRootCAG2SPKI
+ _TestAppleRootCAG2_skid
+ _TestAppleRootCAG2_spki
+ _TestAppleRootCAG3
+ _TestAppleRootCAG3SPKI
+ _TestAppleRootCAG3_skid
+ _TestAppleRootCAG3_spki
+ _TestAppleRootCA_skid
+ _TestAppleRootCA_spki
+ _TestAppleRootECC_skid
+ _TestAppleRootECC_spki
+ _UcrtRootSPKI
+ _UcrtRoot_public_key
+ _UcrtRoot_spki
+ _X509PolicyICDPFederation
+ __AKDictionaryBackedModelValues
+ __CFCopySystemVersionPlatformDictionary
+ __OBJC_$_CLASS_METHODS_AKAccountMigrationContext
+ __OBJC_$_CLASS_METHODS_AKAuthorizationAgeValidator
+ __OBJC_$_CLASS_METHODS_AKDictionaryBackedModel
+ __OBJC_$_CLASS_METHODS_AKSymmetricKey
+ __OBJC_$_CLASS_METHODS_AKSymmetricKeyContext
+ __OBJC_$_CLASS_METHODS_AKSymmetricKeyDaemonInterface
+ __OBJC_$_CLASS_METHODS_AKURLConfiguration
+ __OBJC_$_CLASS_PROP_LIST_AKAccountMigrationContext
+ __OBJC_$_CLASS_PROP_LIST_AKDictionaryBackedModel
+ __OBJC_$_CLASS_PROP_LIST_AKSymmetricKey
+ __OBJC_$_CLASS_PROP_LIST_AKSymmetricKeyContext
+ __OBJC_$_CLASS_PROP_LIST_AKURLConfiguration
+ __OBJC_$_INSTANCE_METHODS_AKAccountMigrationContext
+ __OBJC_$_INSTANCE_METHODS_AKBaseDaemonConnection
+ __OBJC_$_INSTANCE_METHODS_AKDictionaryBackedModel
+ __OBJC_$_INSTANCE_METHODS_AKSymmetricKey
+ __OBJC_$_INSTANCE_METHODS_AKSymmetricKeyContext
+ __OBJC_$_INSTANCE_METHODS_AKSymmetricKeyController
+ __OBJC_$_INSTANCE_METHODS_AKSymmetricKeyDaemonConnection
+ __OBJC_$_INSTANCE_METHODS_AKURLConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AKAccountMigrationContext
+ __OBJC_$_INSTANCE_VARIABLES_AKBaseDaemonConnection
+ __OBJC_$_INSTANCE_VARIABLES_AKDictionaryBackedModel
+ __OBJC_$_INSTANCE_VARIABLES_AKSymmetricKey
+ __OBJC_$_INSTANCE_VARIABLES_AKSymmetricKeyContext
+ __OBJC_$_INSTANCE_VARIABLES_AKSymmetricKeyController
+ __OBJC_$_INSTANCE_VARIABLES_AKSymmetricKeyDaemonConnection
+ __OBJC_$_INSTANCE_VARIABLES_AKURLConfiguration
+ __OBJC_$_PROP_LIST_AKAccountMigrationContext
+ __OBJC_$_PROP_LIST_AKBaseDaemonConnection
+ __OBJC_$_PROP_LIST_AKDictionaryBackedModel
+ __OBJC_$_PROP_LIST_AKSymmetricKey
+ __OBJC_$_PROP_LIST_AKSymmetricKeyContext
+ __OBJC_$_PROP_LIST_AKSymmetricKeyDaemonConnection
+ __OBJC_$_PROP_LIST_AKSymmetricKeyProtocol
+ __OBJC_$_PROP_LIST_AKURLConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKAccountManagerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKSymmetricKeyDaemonProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKSymmetricKeyProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKURLSessionProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKAccountManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKSymmetricKeyDaemonProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKSymmetricKeyProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKURLSessionProtocol
+ __OBJC_$_PROTOCOL_REFS_AKAccountManagerProtocol
+ __OBJC_$_PROTOCOL_REFS_AKSymmetricKeyDaemonProtocol
+ __OBJC_$_PROTOCOL_REFS_AKSymmetricKeyProtocol
+ __OBJC_$_PROTOCOL_REFS_AKURLSessionProtocol
+ __OBJC_CLASS_PROTOCOLS_$_AKAccountManager
+ __OBJC_CLASS_PROTOCOLS_$_AKAccountMigrationContext
+ __OBJC_CLASS_PROTOCOLS_$_AKDictionaryBackedModel
+ __OBJC_CLASS_PROTOCOLS_$_AKSymmetricKey
+ __OBJC_CLASS_PROTOCOLS_$_AKSymmetricKeyContext
+ __OBJC_CLASS_PROTOCOLS_$_AKURLConfiguration
+ __OBJC_CLASS_RO_$_AKAccountMigrationContext
+ __OBJC_CLASS_RO_$_AKAuthorizationAgeValidator
+ __OBJC_CLASS_RO_$_AKBaseDaemonConnection
+ __OBJC_CLASS_RO_$_AKDictionaryBackedModel
+ __OBJC_CLASS_RO_$_AKSymmetricKey
+ __OBJC_CLASS_RO_$_AKSymmetricKeyContext
+ __OBJC_CLASS_RO_$_AKSymmetricKeyController
+ __OBJC_CLASS_RO_$_AKSymmetricKeyDaemonConnection
+ __OBJC_CLASS_RO_$_AKSymmetricKeyDaemonInterface
+ __OBJC_CLASS_RO_$_AKURLConfiguration
+ __OBJC_LABEL_PROTOCOL_$_AKAccountManagerProtocol
+ __OBJC_LABEL_PROTOCOL_$_AKSymmetricKeyDaemonProtocol
+ __OBJC_LABEL_PROTOCOL_$_AKSymmetricKeyProtocol
+ __OBJC_LABEL_PROTOCOL_$_AKURLSessionProtocol
+ __OBJC_METACLASS_RO_$_AKAccountMigrationContext
+ __OBJC_METACLASS_RO_$_AKAuthorizationAgeValidator
+ __OBJC_METACLASS_RO_$_AKBaseDaemonConnection
+ __OBJC_METACLASS_RO_$_AKDictionaryBackedModel
+ __OBJC_METACLASS_RO_$_AKSymmetricKey
+ __OBJC_METACLASS_RO_$_AKSymmetricKeyContext
+ __OBJC_METACLASS_RO_$_AKSymmetricKeyController
+ __OBJC_METACLASS_RO_$_AKSymmetricKeyDaemonConnection
+ __OBJC_METACLASS_RO_$_AKSymmetricKeyDaemonInterface
+ __OBJC_METACLASS_RO_$_AKURLConfiguration
+ __OBJC_PROTOCOL_$_AKAccountManagerProtocol
+ __OBJC_PROTOCOL_$_AKSymmetricKeyDaemonProtocol
+ __OBJC_PROTOCOL_$_AKSymmetricKeyProtocol
+ __OBJC_PROTOCOL_$_AKURLSessionProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_AKSymmetricKeyDaemonProtocol
+ ___33+[NSDate(AuthKit) _dateFormatter]_block_invoke
+ ___37+[NSDate(AuthKit) ak_dateFromString:]_block_invoke
+ ___37-[AKBaseDaemonConnection _connection]_block_invoke
+ ___37-[AKBaseDaemonConnection _connection]_block_invoke_2
+ ___37-[AKBaseDaemonConnection _connection]_block_invoke_3
+ ___42-[AKDictionaryBackedModel initWithValues:]_block_invoke
+ ___42-[NSDate(AuthKit) ak_serverFriendlyString]_block_invoke
+ ___43+[AAFAnalyticsEvent(AuthKit) elementIndex:]_block_invoke
+ ___43-[AKAuthorizationController _sharedKeyInfo]_block_invoke
+ ___43-[AKAuthorizationController _sharedKeyInfo]_block_invoke.53
+ ___43-[AKAuthorizationController _sharedKeyInfo]_block_invoke.53.cold.1
+ ___43-[AKAuthorizationController _sharedKeyInfo]_block_invoke.cold.1
+ ___45+[AKSymmetricKeyDaemonInterface XPCInterface]_block_invoke
+ ___45-[AKSymmetricKeyDaemonConnection _connection]_block_invoke
+ ___45-[AKSymmetricKeyDaemonConnection _connection]_block_invoke_2
+ ___45-[AKSymmetricKeyDaemonConnection _connection]_block_invoke_3
+ ___52-[AKAccountManager _fetchAllAccountsWithType:error:]_block_invoke
+ ___52-[AKAccountManager _fetchAllAccountsWithType:error:]_block_invoke.cold.1
+ ___52-[AKAccountManager _fetchAllAccountsWithType:error:]_block_invoke.cold.2
+ ___56-[AKBaseDaemonConnection _connectionInvalidationHandler]_block_invoke
+ ___56-[AKURLBag urlConfigurationForKey:fromCache:completion:]_block_invoke
+ ___59-[AKAuthorizationController _allowListDomainsForSharingKey]_block_invoke
+ ___59-[AKAuthorizationController _allowListDomainsForSharingKey]_block_invoke.28
+ ___59-[AKAuthorizationController _allowListDomainsForSharingKey]_block_invoke.28.cold.1
+ ___59-[AKAuthorizationController _allowListDomainsForSharingKey]_block_invoke.cold.1
+ ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.116
+ ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.116.cold.1
+ ___64-[AKSymmetricKeyDaemonConnection _connectionInvalidationHandler]_block_invoke
+ ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.159
+ ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.115
+ ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.115.cold.1
+ ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.111
+ ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.111.cold.1
+ ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.109
+ ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.109.cold.1
+ ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.113
+ ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.113.cold.1
+ ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.104
+ ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.104.cold.1
+ ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.33
+ ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.33.cold.1
+ ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.33.cold.2
+ ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.118
+ ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.118.cold.1
+ ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.108
+ ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.108.cold.1
+ ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.35
+ ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.35.cold.1
+ ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.35.cold.2
+ ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.28
+ ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.28.cold.1
+ ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.28.cold.2
+ ___73-[AKAnisetteProvisioningController attestationDataForRequest:completion:]_block_invoke
+ ___74-[AKSymmetricKeyController registerForSymmetricKeyWithContext:completion:]_block_invoke
+ ___74-[AKSymmetricKeyController registerForSymmetricKeyWithContext:completion:]_block_invoke.20
+ ___74-[AKSymmetricKeyController registerForSymmetricKeyWithContext:completion:]_block_invoke.20.cold.1
+ ___74-[AKSymmetricKeyController registerForSymmetricKeyWithContext:completion:]_block_invoke.22
+ ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.106
+ ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.106.cold.1
+ ___77-[AKAnisetteProvisioningController attestationDataForRequestData:completion:]_block_invoke.29
+ ___77-[AKAuthorizationController storeAuthorization:forProxiedRequest:completion:]_block_invoke.36
+ ___78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.30
+ ___78-[AKAuthorizationController continueFetchingIconForRequestContext:completion:]_block_invoke.32
+ ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.107
+ ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.107.cold.1
+ ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.34
+ ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.34.cold.1
+ ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.34.cold.2
+ ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.119
+ ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.119.cold.1
+ ___85-[AKAuthorizationController fetchAppleIDAuthorizeHTMLResponseTemplateWithCompletion:]_block_invoke.30
+ ___86-[AKAuthorizationController primaryApplicationInformationForWebServiceWithInfo:error:]_block_invoke.34
+ ___91-[AKAuthorizationController establishConnectionWithNotificationHandlerEndpoint:completion:]_block_invoke.54
+ ___93-[AKAuthorizationController establishConnectionWithStateBroadcastHandlerEndpoint:completion:]_block_invoke.55
+ ___94+[AAFAnalyticsEvent(AuthKit) encodeElementNameWithIndexPostFix:prefix:element:activeElements:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e39_v24?0"AKAttestationData"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e40_v24?0"AKURLConfiguration"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e46_v24?0"<AKSymmetricKeyProtocol>"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e34_v24?0"NSDictionary"8"NSError"16lr32l8
+ ___block_descriptor_40_e8_32s_e5_8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e36_v32?0"RUITelemetryElement"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e5_8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e21_24?0"NSString"816ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e36_v32?0"RUITelemetryElement"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e5_8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32bs40r_e46_v24?0"<AKSymmetricKeyProtocol>"8"NSError"16lr40l8s32l8
+ ___block_literal_global.145
+ ___block_literal_global.220
+ ___block_literal_global.245
+ ___block_literal_global.27
+ ___block_literal_global.424
+ ___block_literal_global.52
+ ___getFLGroupIdentifierNoGroupSymbolLoc_block_invoke
+ __dateFormatter.dateFormatter
+ __dateFormatter.onceToken
+ __kCFSystemVersionProductVersionKey
+ _getFLGroupIdentifierNoGroup
+ _getFLGroupIdentifierNoGroup.cold.1
+ _getFLGroupIdentifierNoGroupSymbolLoc
+ _getFLGroupIdentifierNoGroupSymbolLoc.ptr
+ _icdpFederationAnchors
+ _isSeedBuild.isSeedBuild
+ _kAKAnalyticsEscapeOffer
+ _kAKAnalyticsEventActivateElement
+ _kAKAnalyticsEventLoadURL
+ _kAKAnalyticsEventLoadURLComplete
+ _kAKAnalyticsEventProcessHook
+ _kAKAnalyticsEventRenderUI
+ _kAKAnalyticsEventReportError
+ _kAKElementIdentifier
+ _kAKProcessHandlerKey
+ _kAKProcessHook
+ _numICDPRoots
+ _objc_exception_throw
+ _objc_msgSend$_allowListDomainsForSharingKey
+ _objc_msgSend$_backupOSVersion
+ _objc_msgSend$_canHandleAnisetteURLResponse:
+ _objc_msgSend$_groupIdentifierFromPayload:
+ _objc_msgSend$_iconTypeID
+ _objc_msgSend$_isAuthorizedCredentialState:
+ _objc_msgSend$_uniqueIdentifierFromPayload:
+ _objc_msgSend$_urlConfigurationAtKey:fromURLBag:
+ _objc_msgSend$_xpcConnection
+ _objc_msgSend$aaf_arrayAsCommaSeperatedString
+ _objc_msgSend$accountIdentifiableTelemetryForAccount:
+ _objc_msgSend$accountImprovementOptInForAccount:
+ _objc_msgSend$accountImprovementOptInValueForAccount:
+ _objc_msgSend$accountMigrationContext
+ _objc_msgSend$ak_addServerBackoffOptInHeader:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$authorizationUsedForAccount:
+ _objc_msgSend$compressUsingAlgorithm:error:
+ _objc_msgSend$elementIndex:
+ _objc_msgSend$encodeElementNameWithIndexPostFix:prefix:element:activeElements:
+ _objc_msgSend$encodedURLWithPrefix:url:
+ _objc_msgSend$existingStatus
+ _objc_msgSend$fetchAllowListDomainsForSharingKeyWithCompletion:
+ _objc_msgSend$fetchSharedKeyInfoWithCompletion:
+ _objc_msgSend$hash
+ _objc_msgSend$initWithAgeRange:
+ _objc_msgSend$initWithKeyData:keySpecifier:keyDomain:
+ _objc_msgSend$initWithPendingDOB:
+ _objc_msgSend$initWithRequestURL:signingDataHash:requiredHeaders:
+ _objc_msgSend$initWithRequestedSubdomains:clientLabel:
+ _objc_msgSend$isAuthKitSolariumFeatureEnabled
+ _objc_msgSend$isBaaEnabled
+ _objc_msgSend$isConfiguredForAccountCreation
+ _objc_msgSend$isSIWAForPAAChildEnabled
+ _objc_msgSend$isServerBackoffOptInEnabled
+ _objc_msgSend$isThreatNotificationCFUEnabled
+ _objc_msgSend$isURL:matchingAppleOwnedDomains:
+ _objc_msgSend$isValidAgeForRequest:account:
+ _objc_msgSend$objectForKey:as:
+ _objc_msgSend$parent
+ _objc_msgSend$parseValue:atKey:
+ _objc_msgSend$pathComponents
+ _objc_msgSend$pendingDOB
+ _objc_msgSend$primaryiCloudAccountHasPendingDOB
+ _objc_msgSend$registerForSymmetricKeyWithContext:completion:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$requestedNewAccountAgeRange
+ _objc_msgSend$setAccountMigrationContext:
+ _objc_msgSend$setIsEligibleToMigrateToChild:
+ _objc_msgSend$setRequestedNewAccountAgeRange:
+ _objc_msgSend$shouldEnableAccountImprovementOptIn
+ _objc_msgSend$urlConfigurationForKey:fromCache:completion:
+ _objc_msgSend$validationRequirements
+ _objc_msgSend$values
+ _timeFormatterLock
+ _xpc_connection_copy_invalidation_reason
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.9
- -[AKAccountManager _fetchAllAccountsWithType:error:].cold.1
- -[AKAccountManager _fetchAllAccountsWithType:error:].cold.2
- -[AKAccountManager _setTokenCreationTimeForToken:tokenID:account:credential:].cold.4
- -[AKAccountManager dependentAuthTokenForAccount:]
- -[AKAnisetteProvisioningController attestationDataForRequest:error:]
- -[AKAttestationSigner _attestationWithCertificates:error:].cold.2
- -[AKFeatureManager isSimpleProfilesEnabled]
- -[AKURLBag isDeviceBAADisabled]
- -[AKURLBag isIDSBAADisabled]
- -[AKURLBag isVMBAADisabled]
- GCC_except_table122
- GCC_except_table132
- GCC_except_table135
- GCC_except_table147
- GCC_except_table150
- GCC_except_table155
- GCC_except_table166
- GCC_except_table167
- GCC_except_table170
- GCC_except_table176
- GCC_except_table178
- GCC_except_table212
- GCC_except_table213
- GCC_except_table214
- GCC_except_table216
- GCC_except_table218
- GCC_except_table219
- GCC_except_table225
- GCC_except_table245
- GCC_except_table246
- GCC_except_table262
- GCC_except_table276
- GCC_except_table277
- GCC_except_table278
- GCC_except_table279
- GCC_except_table280
- GCC_except_table281
- GCC_except_table282
- GCC_except_table283
- GCC_except_table344
- GCC_except_table83
- GCC_except_table85
- GCC_except_table87
- GCC_except_table96
- _AKIdmsDependentAuthTokenKey
- _ApplePlatformBackportECCRootG1
- _ApplePlatformBackportECCRootG1PublicKey
- _ApplePlatformBackportECCRootG1SKID
- _ApplePlatformBackportECCRootG1SPKI
- _ApplePlatformBackportRSARootG1
- _ApplePlatformBackportRSARootG1PublicKey
- _ApplePlatformBackportRSARootG1SKID
- _ApplePlatformBackportRSARootG1SPKI
- _AppleRootCAPublicKey
- _AppleRootCASKID
- _AppleRootG2PublicKey
- _AppleRootG2SKID
- _AppleRootG2SPKI
- _AppleRootG3PublicKey
- _AppleRootG3SKID
- _AppleRootG3SPKI
- _BlockedYonkersPublicKey
- _MFi4RootSpki
- _OBJC_IVAR_$_AKAppleIDAuthenticationContext._needsNewChildAccount
- _SEKProdRoot
- _SEKProdRootSPKI
- _SEKTestRoot
- _SEKTestRootSPKI
- _TestApplePlatformBackportECCRootG1
- _TestApplePlatformBackportECCRootG1PublicKey
- _TestApplePlatformBackportECCRootG1SKID
- _TestApplePlatformBackportECCRootG1SPKI
- _TestApplePlatformBackportRSARootG1
- _TestApplePlatformBackportRSARootG1PublicKey
- _TestApplePlatformBackportRSARootG1SKID
- _TestApplePlatformBackportRSARootG1SPKI
- _TestAppleRootCAPublicKey
- _TestAppleRootCASKID
- _TestAppleRootECCPublicKey
- _TestAppleRootECCSKID
- _TestAppleRootG2
- _TestAppleRootG2PublicKey
- _TestAppleRootG2SKID
- _TestAppleRootG2SPKI
- _TestAppleRootG3
- _TestAppleRootG3PublicKey
- _TestAppleRootG3SKID
- _TestAppleRootG3SPKI
- _UcrtRootSpki
- __CFCopySystemVersionDictionary
- ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.110
- ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.110.cold.1
- ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.158
- ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.109
- ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.109.cold.1
- ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.105
- ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.105.cold.1
- ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.103
- ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.103.cold.1
- ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.107
- ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.107.cold.1
- ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.98
- ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.98.cold.1
- ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.32
- ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.32.cold.1
- ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.32.cold.2
- ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.112
- ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.112.cold.1
- ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.102
- ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.102.cold.1
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.34
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.34.cold.1
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.34.cold.2
- ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.29
- ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.29.cold.1
- ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.29.cold.2
- ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.100
- ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.100.cold.1
- ___77-[AKAnisetteProvisioningController attestationDataForRequestData:completion:]_block_invoke.30
- ___77-[AKAuthorizationController storeAuthorization:forProxiedRequest:completion:]_block_invoke.33
- ___78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.31
- ___78-[AKAuthorizationController continueFetchingIconForRequestContext:completion:]_block_invoke.29
- ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.101
- ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.101.cold.1
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.33
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.33.cold.1
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.33.cold.2
- ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.113
- ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.113.cold.1
- ___85-[AKAuthorizationController fetchAppleIDAuthorizeHTMLResponseTemplateWithCompletion:]_block_invoke.27
- ___86-[AKAuthorizationController primaryApplicationInformationForWebServiceWithInfo:error:]_block_invoke.31
- ___91-[AKAuthorizationController establishConnectionWithNotificationHandlerEndpoint:completion:]_block_invoke.48
- ___93-[AKAuthorizationController establishConnectionWithStateBroadcastHandlerEndpoint:completion:]_block_invoke.49
- ___block_literal_global.142
- ___block_literal_global.218
- ___block_literal_global.242
- ___block_literal_global.36
- ___block_literal_global.412
- __acrt_root_public_key
- __baa_sep_app_root_public_key
- __baa_sep_app_root_skid
- __baa_sep_app_root_spki
- __baa_system_root_public_key
- __baa_system_root_skid
- __baa_system_root_spki
- __baa_user_root_public_key
- __baa_user_root_skid
- __baa_user_root_spki
- __mfi4_root_pub_key
- __mfi4_root_skid
- __mfi4_root_spki
- __sek_prod_root_public_key
- __sek_prod_root_skid
- __sek_prod_root_spki
- __sek_test_root_public_key
- __sek_test_root_skid
- __sek_test_root_spki
- __ucrt_root_pub_key
- __ucrt_root_spki
- _objc_msgSend$initWithLocaleIdentifier:
- _objc_msgSend$isTokenCreationTimeEnabled
- _objc_msgSend$setTimeZone:
- _objc_msgSend$timeZoneForSecondsFromGMT:
CStrings:
+ "%@%@%@"
+ "%@_%@_%@"
+ "%@_%@_%lu"
+ "%{private}@ user allowed to perform request"
+ "%{private}@ user has a valid existing credential"
+ "-XPCInterface must be implemented by a subclass"
+ "-machServiceName must be implemented by a subclass"
+ "."
+ "<%@: %p {\n\tAgeRange: %lu, \n\tShouldForceShieldUI: %@, \n\tGivenName: %@, \n\tLastName: %@, \n}>"
+ "<%@: %p {\n\tPendingDOB: %@\n}>"
+ "<%@: %p {\n\tUUID: %@,\n\tusername: %@,\n\teditable-username: %@,\n\taltDSID: %@,\n\tDSID: %@,\n\tdependentAltDSID: %@,\n\tpassword: %@,\n\tservice-type: %ld,\n\tservice IDs: %@,\n\treason: %@\n\tephemeral: %@,\n\tpassword-only: %@,\n\tpasswordlessToken: %@,\n\tidmsDataToken: %@,\n\tauthentication-type: %@,\n\tauthenticationMode: %@, \n\tisMDMInfoRequired: %@, \n\tupdate-service-tokens: %@,\n\toffer-upgrade: %@,\n\toffer-upgrade-context: %@,\n\tproxying-for-app: %@,\n\tproxied-app-id: %@,\n\tproxied-device: %@,\n\tcompanion-device: %@\n\tmax-login-attempts: %@\n\tappleid-login-enabled: %@\n\thas-empty-password: %@\n\trequest-slt: %@\n\tshort-lived-token: %@\n\tidentity-token: %@\n\ttriggered-by-push: %@\n\tskip-alert: %@\n\tskip-reachability-check: %@\n\tattempt-index: %lu,\n\tmasterKey: %@,\n\tperformUIOutOfProcess: %@,\n\tbroadcastProximityAuthOnly: %@, \n\tVerifyCredentialReason: %@, \n\tEnablePasscodeAuth: %@, \n\tPasscodeOnlyPolicy: %@, \n\tSourceAltDSID: %@, \n\tServiceToken: %@, \n\tbiometricSkipPasscodeFallback: %@, \n\tisNativeTakeover: %@, \n\tignorePasswordCache: %@, \n\tisRequestedFromOOPViewService: %@, \n\tProxiedAppleID: %@, \n\ttelemetryDeviceSessionID: %@, \n\ttelemetryFlowID: %@, \n\tpiggybackingForTrustedDevice: %@, \n\tprotoAccountContextGivenName: %@, \n\taccountMigrationContextPendingDOB: %@, \n\tproxiedToken: %@, \n\tauthenticatableResource: %@, \n}>"
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tedpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tidmsEDPTTokenId: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n}>"
+ "<%@: %p> with \nKeyData: %@ \nKeySpecifier: %@ \nKeyDomain: %@"
+ "<%@: %p> with \nRequestedSubdomains: %@ \nClientLabel: %@"
+ "@\"ACAccount\"16@0:8"
+ "@\"ACAccount\"24@0:8@\"NSString\"16"
+ "@\"AKAccountMigrationContext\""
+ "@\"AKSymmetricKeyDaemonConnection\""
+ "@\"AKURLConfiguration\""
+ "@\"AKURLDataTask\"32@0:8@\"NSURLRequest\"16@?<v@?@\"NSData\"@\"NSURLResponse\"@\"NSError\">24"
+ "@\"NSData\"16@0:8"
+ "@\"_SFSymmetricKeySpecifier\""
+ "@\"_SFSymmetricKeySpecifier\"16@0:8"
+ "@24@?0@\"NSString\"8@16"
+ "@32@0:8@16#24"
+ "AKAccountImprovementErrorDomain"
+ "AKAccountManagerProtocol"
+ "AKAccountMigrationContext"
+ "AKAuthorizationAgeValidator"
+ "AKBaseDaemonConnection"
+ "AKDictionaryBackedModel"
+ "AKDictionaryBackedModel %@ is missing or has invalid value(s) at key(s): %@"
+ "AKDictionaryBackedModel initWithValues requires %@ for key %@, but got %@ instead"
+ "AKDictionaryBackedModel objectForKey: %@ is %@ but expected a(n) %@"
+ "AKDictionaryBackedModel objectForKey: %@ is missing"
+ "AKSymmetricKey"
+ "AKSymmetricKeyContext"
+ "AKSymmetricKeyController"
+ "AKSymmetricKeyDaemonConnection"
+ "AKSymmetricKeyDaemonInterface"
+ "AKSymmetricKeyDaemonProtocol"
+ "AKSymmetricKeyProtocol"
+ "AKURLConfiguration"
+ "AKURLSessionProtocol"
+ "Account Improvement Opt-In Override Enabled, approving Device Session ID vending..."
+ "Account Improvement Telemetry Opt-In detected, but we didn't have an existing device session ID, creating... %@"
+ "Account with pending %{private}@ has never used SIWA"
+ "Account with pending %{private}@ has not created an account with this developer before."
+ "AccountImprovementProgram"
+ "AgeBasedAccountSupport"
+ "AgeMigration"
+ "AgeMigrationEnabled"
+ "Allowed sharing key owned domains fetched"
+ "Allowed sharing key owned domains: %@"
+ "BAAValidation"
+ "BEGIN [%lld]: SymmetricKeyRegistration  enableTelemetry=YES "
+ "CFU"
+ "Calling out to remote SymmetricKey service to initiate register for context %@"
+ "Calling remote authentication service to perform check-in for altDSID: %{mask.hash}@ with reason: %lu"
+ "Checking if url is in allow list domain for sharing key"
+ "Connection to authorization service invalidated: %@"
+ "Connection to symmetric key service interrupted"
+ "Connection to symmetric key service invalidated"
+ "DOB"
+ "DeviceBAA"
+ "END [%lld] %fs:SymmetricKeyRegistration "
+ "EnableSIWAChildAgeAttestation"
+ "Exception caught when attempting to set pendingDOB property: %@"
+ "Excluding threat notification follow up from returned items because it is not supported."
+ "FLGroupIdentifierNoGroup"
+ "Failed to fetch allowed sharing key owned domains with XPC error: %@"
+ "Failed to fetch allowed sharing key owned domains with error: %@"
+ "Failed to fetch shared key info with error: %@"
+ "Failed to reset account improvement program opt-in"
+ "Failed to set account improvement program opt-in to %{BOOL}d"
+ "Feature AccountImprovementProgram enabled = %@"
+ "Feature AgeBasedAccountSupport enabled - %@"
+ "Feature AgeMigration enabled - %@"
+ "Feature AuthKit-Solarium is supported. Is AuthKit-Solarium enabled - %@"
+ "Feature LiveOnServerBackoffOptIn enabled - %@"
+ "Feature PRK Generation new flag enabled - %@"
+ "Feature PRKHealing enabled - %@"
+ "Feature RUI Telemetry enabled - %@"
+ "Feature SIWALandscapeMode enabled - %@"
+ "Feature SecurePake enabled - %@"
+ "Feature ThreatNotificationCFU enabled - %@"
+ "Fetching allowed sharing key owned domains..."
+ "Fetching shared key info..."
+ "Initiated SymmetricKey service returned an error: %{public}@"
+ "LiveOnServerBackoffOptIn"
+ "Logging altdsid : %@"
+ "NSDictionary failed hasValueAtKey %@"
+ "NSDictionary hasValueAtKey %@ expected %@ got %@"
+ "NSDictionary validateValues string is empty atKey %@"
+ "No URL for sharing key Apple ID Authorization"
+ "PRKHealing"
+ "PRKTokenGeneration"
+ "RUITelemetry"
+ "Requested new account age range set: %lu, configuring for new Apple Account"
+ "Requested to update username to %@ for altDSID: %{mask.hash}@"
+ "Result of remote symmetric key registration call: %@. Error: %{public}@"
+ "SIWALandscapeMode"
+ "SecurePake"
+ "Shared key info fetched"
+ "Shared key info: %@"
+ "Solarium"
+ "Successfully reset account improvement program opt-in"
+ "Successfully set account improvement program opt-in to %{BOOL}d"
+ "SwiftUI"
+ "SymmetricKeyRegistration"
+ "T@\"AKAccountMigrationContext\",&,N,V_accountMigrationContext"
+ "T@\"AKURLConfiguration\",&,N,V_urlConfiguration"
+ "T@\"NSArray\",R,C,N,V_requestedSubdomains"
+ "T@\"NSData\",R,N,V_keyData"
+ "T@\"NSDate\",&,N"
+ "T@\"NSDate\",R,C,N,V_pendingDOB"
+ "T@\"NSDictionary\",&,N,V_values"
+ "T@\"NSNumber\",C,N,V_isEligibleToMigrateToChild"
+ "T@\"NSString\",&,N,V_proxiedToken"
+ "T@\"NSString\",C,N,V_iconTypeID"
+ "T@\"NSString\",R,C,N,V_clientLabel"
+ "T@\"NSString\",R,C,N,V_iconTypeID"
+ "T@\"NSString\",R,C,N,V_keyDomain"
+ "T@\"NSURL\",R,C,N,V_url"
+ "T@\"_SFSymmetricKeySpecifier\",R,C,N"
+ "T@\"_SFSymmetricKeySpecifier\",R,C,N,V_keySpecifier"
+ "TB,N,V_biometricSkipPasscodeFallback"
+ "TB,N,V_shouldForceShieldUI"
+ "TB,R,N,GisAccountImprovementProgramEnabled"
+ "TB,R,N,GisAgeBasedAccountSupportEnabled"
+ "TB,R,N,GisAgeMigrationEnabled"
+ "TB,R,N,GisAuthKitSolariumFeatureEnabled"
+ "TB,R,N,GisPRKHealingEnabled"
+ "TB,R,N,GisPRKTokenGenerationEnabled"
+ "TB,R,N,GisPhysicalDeviceBAAEnabled"
+ "TB,R,N,GisPhysicalDeviceBAAValidationEnabled"
+ "TB,R,N,GisRUITelemetryEnabled"
+ "TB,R,N,GisSIWALandscapeModeEnabled"
+ "TB,R,N,GisSecurePakeEnabled"
+ "TB,R,N,GisServerBackoffOptInEnabled"
+ "TB,R,N,GisThreatNotificationCFUEnabled"
+ "TB,R,N,V_isBaaEnabled"
+ "TQ,N,V_requestedNewAccountAgeRange"
+ "TQ,R,N,V_uiType"
+ "ThreatNotificationUI"
+ "Tq,N,V_accountAccessTelemetryOptInFFOverride"
+ "Tq,N,V_shouldEnableAccountImprovementOptIn"
+ "URL is not in allow list domain for sharing key"
+ "Underage"
+ "Vv32@0:8@\"AKSymmetricKeyContext\"16@?<v@?@\"<AKSymmetricKeyProtocol>\"@\"NSError\">24"
+ "X-Apple-Alt-Identity-Token"
+ "X-Apple-I-LiveOnServerBackoffOptIn"
+ "_AKAccountAccessTelemetryOptInFFOverrideKey"
+ "_AKDictionaryBackedModelValues"
+ "_AKImprovementOptIn"
+ "_accountAccessTelemetryOptInFFOverride"
+ "_accountMigrationContext"
+ "_allowListDomainsForSharingKey"
+ "_backupOSVersion"
+ "_biometricSkipPasscodeFallback"
+ "_cachedAccountImprovementProgramEnabled"
+ "_cachedAgeBasedAccountSupportEnabled"
+ "_cachedAgeMigrationEnabled"
+ "_cachedIsAuthKitSolariumFeatureEnabled"
+ "_cachedPRKGenerationEnabled"
+ "_cachedPRKHealingEnabled"
+ "_cachedRUITelemetryEnabled"
+ "_cachedSIWALandscapeModeEnabled"
+ "_cachedSecurePakeEnabled"
+ "_cachedServerBackoffOptInEnabled"
+ "_cachedThreatNotificationCFUEnabled"
+ "_canHandleAnisetteURLResponse:"
+ "_clientLabel"
+ "_fetchAccountsLock"
+ "_groupIdentifierFromPayload:"
+ "_iconTypeID"
+ "_isAuthorizedCredentialState:"
+ "_isBaaEnabled"
+ "_isEligibleToMigrateToChild"
+ "_keyData"
+ "_keyDomain"
+ "_keySpecifier"
+ "_pendingDOB"
+ "_proxiedToken"
+ "_requestedNewAccountAgeRange"
+ "_requestedSubdomains"
+ "_sharedKeyInfo"
+ "_shouldEnableAccountImprovementOptIn"
+ "_shouldForceShieldUI"
+ "_uiType"
+ "_uniqueIdentifierFromPayload:"
+ "_urlConfiguration"
+ "_urlConfigurationAtKey:fromURLBag:"
+ "_values"
+ "aaf_arrayAsCommaSeperatedString"
+ "accountAccessTelemetryOptInFFOverride"
+ "accountIdentifiableTelemetryForAccount:"
+ "accountImprovementOptInForAccount:"
+ "accountImprovementOptInValueForAccount:"
+ "accountImprovementProgramEnabled"
+ "accountMigrationContext"
+ "ageBasedAccountSupportEnabled"
+ "ageMigration"
+ "ageMigrationEligible"
+ "ak_addAuthorizationHeaderWithAltIdentityToken:forAltDSID:"
+ "ak_addJSONResponseAcceptHeader"
+ "ak_addServerBackoffOptInHeader:"
+ "ak_analyticsEventWithRUITelemetryElement:eventName:error:"
+ "allowListDomainsForSharingKey"
+ "allowUnderageRequest %d hasUsedAuthorization %d isSIWAForPAAChildEnabled %d hasAuthorizedCredential %d"
+ "arrayWithArray:"
+ "authKitSolariumFeatureEnabled"
+ "biometricSkipPasscodeFallback"
+ "clientLabel"
+ "com.apple.ThreatNotificationUI.FollowUpExtension"
+ "com.apple.ThreatNotificationUI.FollowUpItem.general"
+ "com.apple.ak.privateemail.didRegisterNewEmail"
+ "com.apple.ak.privateemail.didUnregistredEmail"
+ "com.apple.ak.symmetrickey.xpc"
+ "com.apple.authkit.shared-key-change"
+ "com.apple.idms.config.privacy.appleaccount.access"
+ "com.apple.remoteUI.activateElement"
+ "com.apple.remoteUI.loadURL"
+ "com.apple.remoteUI.loadURLComplete"
+ "com.apple.remoteUI.processHook"
+ "com.apple.remoteUI.renderUI"
+ "com.apple.remoteUI.reportError"
+ "com.apple.remoteui"
+ "compressUsingAlgorithm:error:"
+ "connectDependent"
+ "createTeenAccount"
+ "didAccountRecovery"
+ "elementIdentifier"
+ "elementIndex:"
+ "enableAccountAccessOptIn"
+ "encodeElementNameWithIndexPostFix:prefix:element:activeElements:"
+ "encodedElementNameWithDomainPrefix:element:activeElements:"
+ "encodedURLWithPrefix:url:"
+ "escapeOffer"
+ "fetchAllowListDomainsForSharingKeyWithCompletion:"
+ "fetchSharedKeyInfoWithCompletion:"
+ "followUpAcknowledge"
+ "generatePrk"
+ "handlerKey"
+ "hasValueAtKey:ofType:"
+ "healing"
+ "hookName"
+ "iconTypeID"
+ "initFromSymmetricKey:"
+ "initWithAgeRange:"
+ "initWithKeyData:keySpecifier:keyDomain:"
+ "initWithPendingDOB:"
+ "initWithRequestURL:signingDataHash:requiredHeaders:"
+ "initWithRequestedSubdomains:"
+ "initWithRequestedSubdomains:clientLabel:"
+ "initWithValues:"
+ "isAccountAccessTelemetryOptInEnabled"
+ "isAccountImprovementProgramEnabled"
+ "isAgeBasedAccountSupportEnabled"
+ "isAgeMigrationEnabled"
+ "isAuthKitSolariumFeatureEnabled"
+ "isBaaEnabled"
+ "isConfiguredForAccountCreation"
+ "isEligibleToMigrateToChild"
+ "isEligibleToMigrateToChildForAccount:"
+ "isPRKHealingEnabled"
+ "isPRKTokenGenerationEnabled"
+ "isPhysicalDeviceBAAEnabled"
+ "isPhysicalDeviceBAAValidationEnabled"
+ "isRUITelemetryEnabled"
+ "isSIWAForPAAChildEnabled"
+ "isSIWALandscapeModeEnabled"
+ "isSecurePakeEnabled"
+ "isServerBackoffOptInEnabled"
+ "isThreatNotificationCFUEnabled"
+ "isURL:matchingAppleOwnedDomains:"
+ "isURLFromAllowListDomainsForSharingKey:"
+ "isValidAgeForRequest:account:"
+ "keyData"
+ "keyDomain"
+ "keySpecifier"
+ "objectForKey:as:"
+ "pRKHealingEnabled"
+ "pRKTokenGenerationEnabled"
+ "pakeStep"
+ "parent"
+ "parseValue:atKey:"
+ "pathComponents"
+ "pendingDOB"
+ "physicalDeviceBAAEnabled"
+ "physicalDeviceBAAValidationEnabled"
+ "primaryiCloudAccountHasPendingDOB"
+ "proxiedToken"
+ "registerForSymmetricKeyWithContext:completion:"
+ "removeObjectAtIndex:"
+ "requestedNewAccountAgeRange"
+ "requestedSubdomains"
+ "resetAccountImprovementOptInForAccount:error:"
+ "ruiTelemetryEnabled"
+ "securePakeEnabled"
+ "securePakeStepURL"
+ "serverBackoffOptInEnabled"
+ "setAccountAccessTelemetryOptInFFOverride:"
+ "setAccountAccessTelemetryOptInOverride:"
+ "setAccountImprovementOptIn:forAccount:error:"
+ "setAccountMigrationContext:"
+ "setBiometricSkipPasscodeFallback:"
+ "setIsEligibleToMigrateToChild:"
+ "setIsEligibleToMigrateToChild:forAccount:"
+ "setPendingDOB:"
+ "setPendingDOB:forAccount:"
+ "setProxiedToken:"
+ "setRequestedNewAccountAgeRange:"
+ "setShouldEnableAccountImprovementOptIn:"
+ "setShouldForceShieldUI:"
+ "setUrlConfiguration:"
+ "setValues:"
+ "set_iconTypeID:"
+ "shouldEnableAccountImprovementOptIn"
+ "shouldForceShieldUI"
+ "siwaLandscapeModeEnabled"
+ "spyglassSignOut"
+ "symmetrickey-authkit/registeration"
+ "threatNotificationCFUEnabled"
+ "tokenCreationTimeStampWithIdentifier:forAccount:error:"
+ "uiType"
+ "urlConfiguration"
+ "urlConfigurationForKey: %@"
+ "urlConfigurationForKey:fromCache:completion:"
+ "v24@0:8@\"AKURLDataTask\"16"
+ "v24@?0@\"<AKSymmetricKeyProtocol>\"8@\"NSError\"16"
+ "v24@?0@\"AKURLConfiguration\"8@\"NSError\"16"
+ "v32@?0@\"RUITelemetryElement\"8Q16^B24"
+ "validObjectForKey:"
+ "validationRequirements"
+ "values"
+ "x-apple-device-token"
- "%{private}@"
- "<%@: %p {\n\tGivenName: %@, \n\tLastName: %@, \n\tAgeRange: %lu, \n}>"
- "<%@: %p {\n\tUUID: %@,\n\tusername: %@,\n\teditable-username: %@,\n\taltDSID: %@,\n\tDSID: %@,\n\tdependentAltDSID: %@,\n\tpassword: %@,\n\tservice-type: %ld,\n\tservice IDs: %@,\n\treason: %@\n\tephemeral: %@,\n\tpassword-only: %@,\n\tpasswordlessToken: %@,\n\tidmsDataToken: %@,\n\tauthentication-type: %@,\n\tauthenticationMode: %@, \n\tisMDMInfoRequired: %@, \n\tupdate-service-tokens: %@,\n\toffer-upgrade: %@,\n\toffer-upgrade-context: %@,\n\tproxying-for-app: %@,\n\tproxied-app-id: %@,\n\tproxied-device: %@,\n\tcompanion-device: %@\n\tmax-login-attempts: %@\n\tappleid-login-enabled: %@\n\thas-empty-password: %@\n\trequest-slt: %@\n\tshort-lived-token: %@\n\tidentity-token: %@\n\ttriggered-by-push: %@\n\tskip-alert: %@\n\tskip-reachability-check: %@\n\tattempt-index: %lu,\n\tmasterKey: %@,\n\tperformUIOutOfProcess: %@,\n\tbroadcastProximityAuthOnly: %@, \n\tVerifyCredentialReason: %@, \n\tEnablePasscodeAuth: %@, \n\tPasscodeOnlyPolicy: %@, \n\tSourceAltDSID: %@, \n\tServiceToken: %@, \n\tisNativeTakeover: %@, \n\tignorePasswordCache: %@, \n\tisRequestedFromOOPViewService: %@, \n\tProxiedAppleID: %@, \n\ttelemetryDeviceSessionID: %@, \n\ttelemetryFlowID: %@, \n\tpiggybackingForTrustedDevice: %@, \n\tprotoAccountContextGivenName: %@, \n\tauthenticatableResource: %@, \n}>"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tedpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tidmsEDPTTokenId: %@,\n\tpiggybackingApprovalEligible: %@,\n}>"
- "Allowing underage user to perform request"
- "Calling remote authentication service to perform check-in for altDSID: %@ with reason: %lu"
- "Failed to BAA, failed to serialize: unknown error!"
- "Requested to update username to %@ for altDSID: %@"
- "SimpleProfiles"
- "TB,N,V_needsNewChildAccount"
- "TB,R,N,GisSimpleProfilesEnabled"
- "Token creation time is not enabled. Skipping token creation time update."
- "_needsNewChildAccount"
- "attestationDataForRequest:error:"
- "com.apple.gs.idms.dependent.auth"
- "dependentAuthTokenForAccount:"
- "disableIDSBAA"
- "en_US_POSIX"
- "initWithLocaleIdentifier:"
- "isDeviceBAADisabled"
- "isIDSBAADisabled"
- "isSimpleProfilesEnabled"
- "isVMBAADisabled"
- "setTimeZone:"
- "simpleProfilesEnabled"
- "timeZoneForSecondsFromGMT:"
- "yyyy'-'MM'-'dd'T'HH':'mm':'ss'Z'"

```
