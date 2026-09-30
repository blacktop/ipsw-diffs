## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-518.1.0.0.0
-  __TEXT.__text: 0xda914
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0xd7fc
-  __TEXT.__const: 0x6af0
-  __TEXT.__cstring: 0xefa3
-  __TEXT.__oslogstring: 0x11521
-  __TEXT.__gcc_except_tab: 0x57b8
+520.0.0.0.0
+  __TEXT.__text: 0x173728
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0xd8f4
+  __TEXT.__const: 0x69c0
+  __TEXT.__cstring: 0xf1c6
+  __TEXT.__oslogstring: 0x11539
+  __TEXT.__gcc_except_tab: 0x9af0
+  __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x1b8
-  __TEXT.__dlopen_cstrs: 0x16c
-  __TEXT.__unwind_info: 0x4030
-  __TEXT.__objc_classname: 0x1c14
-  __TEXT.__objc_methname: 0x219b2
-  __TEXT.__objc_methtype: 0x452a
-  __TEXT.__objc_stubs: 0xee60
-  __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__const: 0x8038
+  __TEXT.__unwind_info: 0x4018
+  __TEXT.__objc_classname: 0x1c15
+  __TEXT.__objc_methname: 0x21c83
+  __TEXT.__objc_methtype: 0x45bb
+  __TEXT.__objc_stubs: 0xefc0
+  __DATA_CONST.__got: 0xa38
+  __DATA_CONST.__const: 0xa0a8
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6dd8
+  __DATA_CONST.__objc_selrefs: 0x6e60
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0x1d8
-  __AUTH_CONST.__auth_got: 0x6f8
-  __AUTH_CONST.__const: 0x11b0
-  __AUTH_CONST.__cfstring: 0xf640
-  __AUTH_CONST.__objc_const: 0x25190
+  __DATA_CONST.__objc_arraydata: 0x2c8
+  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__const: 0x11e0
+  __AUTH_CONST.__cfstring: 0xf940
+  __AUTH_CONST.__objc_const: 0x25218
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x2580
-  __DATA.__objc_ivar: 0xfc8
-  __DATA.__data: 0x18a0
-  __DATA.__bss: 0x650
-  __DATA_DIRTY.__objc_data: 0x17c0
-  __DATA_DIRTY.__bss: 0x278
+  __AUTH_CONST.__objc_dictobj: 0x3e8
+  __AUTH.__objc_data: 0x2620
+  __DATA.__objc_ivar: 0xfd0
+  __DATA.__data: 0x1900
+  __DATA.__bss: 0x628
+  __DATA_DIRTY.__objc_data: 0x1720
+  __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F45016B7-60B5-3E7B-8B9A-8EBA39A85043
-  Functions: 6164
-  Symbols:   21509
-  CStrings:  11547
+  UUID: 2AA3C586-7242-3CF4-939B-3AAA102043FA
+  Functions: 5269
+  Symbols:   20019
+  CStrings:  11635
 
Symbols:
+ +[AKFollowUpController followUpPostAnalyticsInfoWithIdentifier:telemetryFlowID:error:]
+ -[AKAccountManager appleAccountConsentVersionForAccount:]
+ -[AKAccountManager setConsentVersion:forAccount:]
+ -[AKDevice effectiveUserIdentifier]
+ -[AKDevice setEffectiveUserIdentifier:]
+ -[AKFollowUpController addFollowUpItems:telemetryFlowID:error:]
+ -[AKFollowUpController clearNotificationsForItem:telemetryFlowID:error:]
+ -[AKFollowUpController removeAllFollowUpItems:telemetryFlowID:]
+ -[AKFollowUpController removeFollowUpItems:telemetryFlowID:error:]
+ -[AKFollowUpController removeFollowUpItemsWithIdentifiers:telemetryFlowID:error:]
+ -[AKFollowUpController sendEventForFollowUpWithError:eventName:success:telemetryFlowID:error:]
+ -[AKFollowUpTearDownContext setTelemetryFlowID:]
+ -[AKFollowUpTearDownContext telemetryFlowID]
+ -[NSMutableURLRequest(AuthKit) ak_addEffectiveUserIdentifierHeader]
+ GCC_except_table118
+ GCC_except_table122
+ GCC_except_table124
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table147
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table154
+ GCC_except_table157
+ GCC_except_table161
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table170
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table188
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table208
+ GCC_except_table209
+ GCC_except_table210
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table247
+ GCC_except_table248
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table270
+ GCC_except_table278
+ GCC_except_table279
+ GCC_except_table281
+ GCC_except_table282
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table332
+ GCC_except_table333
+ GCC_except_table334
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table339
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table342
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table51
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table88
+ _AAFMediaTypeApplePlist
+ _AAFMediaTypeJSON
+ _AAFMediaTypePlist
+ _AAFMediaTypeTextJSON
+ _AAFMediaTypeTextPlist
+ _AAFMediaTypeXML
+ _AKADPCountriesKey
+ _AKADPCountryStatusKey
+ _AKADPStatusDescriptionKey
+ _AKAccountPropertyFirstName
+ _AKAccountPropertyLastName
+ _AKAppleAccountConsentValueKey
+ _AKAppleAccountConsentVersionKey
+ _AKAppleAccountPrivacyConsentKey
+ _AKAppleIDPasskeyRelyingPartyIdentifier
+ _AKAttestationSignerKeychainAccessGroup
+ _AKAttestationSignerKeychainLabel
+ _AKAuthModeTimeStamp
+ _AKCompanionKeyEnvelopeAltDSIDKey
+ _AKCompanionKeyEnvelopeContinuationKey
+ _AKCompanionKeyEnvelopeMachineIDKey
+ _AKCompanionKeyEnvelopePasswordResetKey
+ _AKCompanionKeyEnvelopeUsernameKey
+ _AKContinuationTokenCreationKey
+ _AKCredentialPasswordKey
+ _AKCredentialUserKey
+ _AKDataAccessAnalyticsOptInTimeStamp
+ _AKDeviceInfoKey
+ _AKFollowUpADPUpsellIdentifier
+ _AKFollowUpAccountRefreshTimestamp
+ _AKFollowUpExtensionTypeAccount
+ _AKFollowUpExtensionTypeData
+ _AKFollowUpNotifyingAppId
+ _AKFollowUpPayloadActionAKActionKey
+ _AKFollowUpPayloadActionAKNativeFollowUpActionKey
+ _AKFollowUpPayloadActionAppleAccountrootKey
+ _AKFollowUpPayloadActionLocalUrlKey
+ _AKFollowUpPayloadActionSafarLinkKey
+ _AKFollowUpPayloadActionUrlKey
+ _AKFollowUpPayloadActionsKey
+ _AKFollowUpPayloadBadgeOnlyKey
+ _AKFollowUpPayloadBodyKey
+ _AKFollowUpPayloadBundleIconNameKey
+ _AKFollowUpPayloadBundlePathKey
+ _AKFollowUpPayloadNotificationAlertnateButtonKey
+ _AKFollowUpPayloadNotificationBannerAlertKey
+ _AKFollowUpPayloadNotificationDefaultButtonKey
+ _AKFollowUpPayloadNotificationDelayKey
+ _AKFollowUpPayloadNotificationDismissKey
+ _AKFollowUpPayloadNotificationForceNotificationKey
+ _AKFollowUpPayloadNotificationFrequencyKey
+ _AKFollowUpPayloadNotificationKey
+ _AKFollowUpPayloadNotificationSpringboardAlertActionOnlyKey
+ _AKFollowUpPayloadNotificationSpringboardAlertKey
+ _AKFollowUpPayloadNotifyingAppIDKey
+ _AKFollowUpPayloadOmitBadgeKey
+ _AKFollowUpPayloadPriorityKey
+ _AKFollowUpPayloadTitleKey
+ _AKFollowUpPayloadZeroActionKey
+ _AKFollowUpPushMessageCommandKey
+ _AKFollowUpThreatNotificationIdMSExtensionType
+ _AKFollowUpThreatNotificationIdMSIdentifier
+ _AKFollowUpThreatNotificationIdentifier
+ _AKHTTPHeaderEffectiveUserIdentifier
+ _AKHeartbeatTokenCreationKey
+ _AKInheritanceDataSelectionAllKey
+ _AKInheritanceDataSelectionBundlesKey
+ _AKInheritanceDataSelectionDescriptionKey
+ _AKInheritanceDataSelectionIdentifierKey
+ _AKInheritanceDataSelectionNameKey
+ _AKInheritanceDataSelectionOthersKey
+ _AKInheritanceDataSelectionTypeKey
+ _AKLostModeKey
+ _AKMachineIdKey
+ _AKNextLivenessNonce
+ _AKPasswordResetTokenCreationKey
+ _AKPersistRecoveryKeyTypeKey
+ _AKPersistRecoveryKeyVerifierKey
+ _AKPiggybackPayloadPakeKey
+ _AKPiggybackingAltDSIDKey
+ _AKPiggybackingCommandKey
+ _AKPiggybackingStepKey
+ _AKPiggybackingTransactionIDKey
+ _AKPiggybackingTransactionIDNKey
+ _AKPrivateEmail3rdPartyOriginIdentifier
+ _AKPrivateEmailClientKey
+ _AKPrivateEmailContextAltDSIDKey
+ _AKPrivateEmailContextKeyKey
+ _AKPrivateEmailContextProxiedAppKey
+ _AKPrivateEmailContextProxiedAppNameKey
+ _AKPrivateEmailContextProxiedBundleIdentifierKey
+ _AKPrivateEmailContextUpgradeBundleIdentifierKey
+ _AKPrivateEmailMetadataStringKey
+ _AKPrivateEmailOriginIdentifierKey
+ _AKPrivateEmailOriginTypeKey
+ _AKPrivateEmailSafariOriginIdentifier
+ _AKPropertyAgeOfMajority
+ _AKPropertyAppleIDCountryCode
+ _AKPropertyAuthorizationEmailSelection
+ _AKPropertyAuthorizationEnabled
+ _AKPropertyBeneficiaryAccount
+ _AKPropertyBeneficiaryLastModified
+ _AKPropertyBeneficiaryListVersion
+ _AKPropertyCanBeBeneficiary
+ _AKPropertyCanBeCustodian
+ _AKPropertyCanHaveBeneficiary
+ _AKPropertyCanHaveCustodian
+ _AKPropertyCustodianEnabled
+ _AKPropertyCustodianLastModified
+ _AKPropertyCustodianListVersion
+ _AKPropertyDemoAccount
+ _AKPropertyFidoAccount
+ _AKPropertyForwardingEmail
+ _AKPropertyHasMDM
+ _AKPropertyIsNotificationEmailAvailable
+ _AKPropertyIsSiwaEnabled
+ _AKPropertyManagedOrganizationName
+ _AKPropertyManagedOrganizationType
+ _AKPropertyNotificationEmail
+ _AKPropertyPendingDOB
+ _AKPropertyPhoneAsAppleID
+ _AKPropertyPrimaryEmailAddress
+ _AKPropertyPrivateAttestationEnabled
+ _AKPropertyPrivateEmailSelection
+ _AKPropertyReachableEmailAddresses
+ _AKPropertyUserAgeRange
+ _AKPropertyUserIsSenior
+ _AKPropertyUserUnderage
+ _AKPropertyVettedPrimaryEmail
+ _AKRemoteDeviceRemovalReasonKey
+ _AKRemoteUIServiceBundleID
+ _AKSatoriWarmUpTimeStamp
+ _AKSerialNumberKey
+ _AKTVDeprecatedStartProgressAnimationType
+ _AKTVDidStartServerAuthorizationType
+ _AKTVDidTapNotificationType
+ _AKTVFetchAppIconReplyType
+ _AKTVFetchAppIconType
+ _AKTVTypeKey
+ _AKUIServiceBundleIdentifier
+ _DeviceIdentityLibraryCore
+ _MAX_ERROR_STACK
+ _MobileActivationLibraryCore
+ _OBJC_CLASS_$_AAAFollowUpAnalyticsInfo
+ _OBJC_IVAR_$_AKDevice._effectiveUserIdentifier
+ _OBJC_IVAR_$_AKFollowUpTearDownContext._telemetryFlowID
+ _SDeviceIdentityCreateHostSignature
+ __AKAOSUIFrameworkPath
+ __AKAbsintheErrorWithCode
+ __AKAccountAccessTelemetryOptInFFOverrideKey
+ __AKAccountMigrationContextPendingDOBKey
+ __AKActiveHMECount
+ __AKAddExperimentalModeHeader
+ __AKAddHS2CreateHeader
+ __AKAddTestAccountHeader
+ __AKAddTestApplicationHeader
+ __AKAgeRangeSettingsCacheInternalChangeNotification
+ __AKAlertImageDark
+ __AKAllowPhoneNumberAccounts
+ __AKAlwaysShowWelcome
+ __AKAnisetteDataMachineIDKey
+ __AKAnisetteDataOneTimePasswordKey
+ __AKAnisetteDataRoutingInfoKey
+ __AKAppIDKey
+ __AKAppInfoCredentialCreationDateKey
+ __AKAppInfoCredentialOriginKey
+ __AKAppInfoIdentifierKey
+ __AKAppInfoNameKey
+ __AKAppInfoPrimaryClientIDKey
+ __AKAppInfoScopesKey
+ __AKAppInfoStateKey
+ __AKAppInfoTransferStateKey
+ __AKAppMetadataInfoTeamsKey
+ __AKAppMetadataInfoVersionKey
+ __AKAppNameKey
+ __AKAppProvidedDataKey
+ __AKAppServerName
+ __AKAppStoreIconName
+ __AKAppStorePath
+ __AKAppleIDIconName
+ __AKAppleIDPasskeyAltDSIDKey
+ __AKAppleIDPasskeyAppProvidedDataKey
+ __AKApplicationNonceKey
+ __AKApplicationStateKey
+ __AKApplicationVersion
+ __AKAskToBuy
+ __AKAttestationErrorCreate
+ __AKAttestationErrorCreateWithUnderlyingError
+ __AKAttestationValidityDefaultMinutes
+ __AKAuthenticationRequestUUIDHeaderFieldKey
+ __AKAuthorizationAccountKey
+ __AKAuthorizationDaemonConnectionCreate
+ __AKAuthorizationDemoMode
+ __AKAuthorizationIsEligibleForUpgradeFromPasswordKey
+ __AKAuthorizationIsSilentAppTransferKey
+ __AKAuthorizationShouldHideCreateOptionKey
+ __AKAuthorizationStatusKey
+ __AKAutocycleAppsInTiburon
+ __AKAutocycleAppsInWebTakeover
+ __AKBackoffDuration
+ __AKBackoffIssuedAt
+ __AKBase64PaddingString
+ __AKBeneficiaryLiveOnKey
+ __AKBeneficiaryManifestAccessibleBundleInformationKey
+ __AKBeneficiaryManifestManifestOptionsKey
+ __AKBeneficiaryUUIDListKey
+ __AKBiometricRatchetIdentifierKey
+ __AKBundleIDKey
+ __AKBundleInformationBundleDescriptionKey
+ __AKBundleInformationBundleIdentifierKey
+ __AKBundleInformationBundleNameKey
+ __AKBundleInformationBundleTypeKey
+ __AKBundleInformationOtherInfoKey
+ __AKByPassCustodianDeviceCheckKey
+ __AKCLIExecutionModeValue
+ __AKCarrierUtilitiesQueue
+ __AKClientAuthenticatedExternallyWithPasswordKey
+ __AKClientBundleID
+ __AKClientIDKey
+ __AKCloudPartitionKey
+ __AKConfigurationDidChangeNotification
+ __AKContactKeyVerificationKey
+ __AKContextDataKey
+ __AKContinuationHeaderPrefix
+ __AKCriticalAccountEditsKey
+ __AKCustodianAADataKey
+ __AKCustodianAltDSIDKey
+ __AKCustodianCLIMode
+ __AKCustodianDaemonConnectionCreate
+ __AKCustodianEmbargoEndFeedbackKey
+ __AKCustodianEncryptedPRKCKey
+ __AKCustodianErrorCodeKey
+ __AKCustodianIdMSDataKey
+ __AKCustodianLastDataSyncTimestampKey
+ __AKCustodianNotificationActionKey
+ __AKCustodianOwnerAppleIDKey
+ __AKCustodianOwnerCustodianAltDSIDKey
+ __AKCustodianOwnerDeviceKey
+ __AKCustodianPushTokenKey
+ __AKCustodianRecoverySessionIDKey
+ __AKCustodianRecoveryStepKey
+ __AKCustodianRecoveryTokenKey
+ __AKCustodianSetupTokenKey
+ __AKCustodianTransactionIDKey
+ __AKCustodianUUIDKey
+ __AKCustodianUUIDListKey
+ __AKCustodianWrappingKeyRKC
+ __AKDataKey
+ __AKDeleteEntry
+ __AKDevTeamAppsKey
+ __AKDevTeamKey
+ __AKDevTeamPrivateEmailKey
+ __AKDevTeamUserIDKey
+ __AKDeviceListDeltaOperationAdd
+ __AKDeviceListDeltaOperationDelete
+ __AKDeviceSafetyRestrictionReasonOverrideKey
+ __AKDisablePETCode
+ __AKDisablePiggybacking
+ __AKEncrypedSessionKeyHeaderKey
+ __AKExternalAuthTokenKey
+ __AKFIDOContextChallengeKey
+ __AKFIDOContextCredentialNameKey
+ __AKFIDOContextCredentialsKey
+ __AKFIDOContextDisplayNameKey
+ __AKFIDOContextIncorrectKeyPresentedMessage
+ __AKFIDOContextOriginalChallengeKey
+ __AKFIDOContextParameterChallengeKey
+ __AKFIDOContextParameterCredentialIDsKey
+ __AKFIDOContextParameterRelyingPartyIDKey
+ __AKFIDOContextPromptBodyKey
+ __AKFIDOContextPromptHeaderKey
+ __AKFIDOContextPromptTitleKey
+ __AKFIDOContextRelyingPartyIdentifierKey
+ __AKFIDOContextUseAlternativeKeysIcon
+ __AKFIDOContextUserIdentifierKey
+ __AKFakeAuthSuccess
+ __AKFidoAuthenticationResponseAuthenticatorDataKey
+ __AKFidoAuthenticationResponseChallengeKey
+ __AKFidoAuthenticationResponseClientDataKey
+ __AKFidoAuthenticationResponseCredentialNameKey
+ __AKFidoAuthenticationResponseRelyingPartyIdentifierKey
+ __AKFidoAuthenticationResponseSignatureKey
+ __AKFidoAuthenticationResponseUserIdentifierKey
+ __AKFidoRegistrationResponseClientDataKey
+ __AKFidoRegistrationResponseCredentialIDKey
+ __AKFidoRegistrationResponseCredentialNameKey
+ __AKFidoRegistrationResponseRelyingPartyIdentifierKey
+ __AKFidoRegistrationResponseUserIdentifierKey
+ __AKFidoResponseAttestationsDataKey
+ __AKFidoResponseChallengeKey
+ __AKFindMyDeviceName
+ __AKForceSilentBurnCDPRepairEnabled
+ __AKForceSilentEscrowRecordRepairEnabled
+ __AKForceSilentEscrowRecordRepairEnabledV2
+ __AKGuardianHeartbeatTokenHeaderKey
+ __AKHTTPHeaderAbsinthe
+ __AKHTTPHeaderAcceptedSLAVersion
+ __AKHTTPHeaderAcceptedTermsKey
+ __AKHTTPHeaderAlternateIdentityAuthorization
+ __AKHTTPHeaderAppProvidedContext
+ __AKHTTPHeaderAppleID
+ __AKHTTPHeaderAppleIDUserMode
+ __AKHTTPHeaderBiometryType
+ __AKHTTPHeaderCDPStatus
+ __AKHTTPHeaderCFUState
+ __AKHTTPHeaderCKRequest
+ __AKHTTPHeaderCircleStatus
+ __AKHTTPHeaderCompanionClientInfo
+ __AKHTTPHeaderCompanionMID
+ __AKHTTPHeaderCompanionOTP
+ __AKHTTPHeaderCompanionRoutingInfo
+ __AKHTTPHeaderConfigurationMode
+ __AKHTTPHeaderContinutationKey
+ __AKHTTPHeaderContinutationPresenceKey
+ __AKHTTPHeaderCountry
+ __AKHTTPHeaderCreateInfo
+ __AKHTTPHeaderCustodianRecoveryToken
+ __AKHTTPHeaderCustodianSyncAction
+ __AKHTTPHeaderDataCenterKey
+ __AKHTTPHeaderDeviceID
+ __AKHTTPHeaderDeviceMode
+ __AKHTTPHeaderDeviceModel
+ __AKHTTPHeaderEphemeralAuth
+ __AKHTTPHeaderExecutionModeKey
+ __AKHTTPHeaderFidoRecoveryToken
+ __AKHTTPHeaderGuardianIdentityAuthorization
+ __AKHTTPHeaderGuardianServiceAuthorization
+ __AKHTTPHeaderIdentityAuthorization
+ __AKHTTPHeaderLocalUsersHasAppleIDLogin
+ __AKHTTPHeaderLocale
+ __AKHTTPHeaderLoggedInServices
+ __AKHTTPHeaderMLB
+ __AKHTTPHeaderOTStatus
+ __AKHTTPHeaderOfferSecurityUpgradeKey
+ __AKHTTPHeaderPAC
+ __AKHTTPHeaderPRKRequest
+ __AKHTTPHeaderPasswordResetKey
+ __AKHTTPHeaderPhoneInfo
+ __AKHTTPHeaderPhoneNumber
+ __AKHTTPHeaderProvisioningDeviceID
+ __AKHTTPHeaderProxiedClientInfo
+ __AKHTTPHeaderProxiedDeviceCountry
+ __AKHTTPHeaderProxiedDeviceICSCIntent
+ __AKHTTPHeaderProxiedDeviceID
+ __AKHTTPHeaderProxiedDevicePRKRequest
+ __AKHTTPHeaderProxiedDeviceSerialNumber
+ __AKHTTPHeaderProxiedIdentityAuthorization
+ __AKHTTPHeaderProxiedMID
+ __AKHTTPHeaderProxiedOTP
+ __AKHTTPHeaderProxiedRoutingInfo
+ __AKHTTPHeaderROM
+ __AKHTTPHeaderReAuthenticationKey
+ __AKHTTPHeaderRequestContextKey
+ __AKHTTPHeaderResponseAccept
+ __AKHTTPHeaderResponseContentType
+ __AKHTTPHeaderSKUCountry
+ __AKHTTPHeaderSerialNumber
+ __AKHTTPHeaderServiceAuthorization
+ __AKHTTPHeaderShortLivedToken
+ __AKHTTPHeaderShowWarranty
+ __AKHTTPHeaderSupportedLanguage
+ __AKHTTPHeaderTelemetryDeviceSessionID
+ __AKHTTPHeaderTelemetryFlowID
+ __AKHTTPHeaderTestApplication
+ __AKHTTPHeaderTimeZone
+ __AKHTTPHeaderTimeZoneOffset
+ __AKHTTPHeaderValueJSON
+ __AKHTTPHeaderWalrusDeviceRegionKey
+ __AKHTTPHeaderWalrusStatusKey
+ __AKHTTPResponseHeaderSwitchURLDataKey
+ __AKHasSharedAccountsKey
+ __AKHeartbeatTokenHeaderKey
+ __AKHideInternalBuildHeader
+ __AKHideSeedBuildHeader
+ __AKIDMSCertificateLeafOID
+ __AKIDMSEnvironmentKey
+ __AKIdentityCreationTimeKey
+ __AKIdentityTokenDurationKey
+ __AKIdentityTokenHeaderKey
+ __AKIdentityTokenKey
+ __AKIdentityValueKey
+ __AKIdmsWalrusStatusOverrideKey
+ __AKImprovementOptIn
+ __AKInActiveHMECount
+ __AKInformationAccountNameKey
+ __AKInformationAdditionalInfoKey
+ __AKInformationAgeOfMajority
+ __AKInformationAliasesKey
+ __AKInformationAppleIDCountryCodeKey
+ __AKInformationApplicationsListVersionKey
+ __AKInformationAuthorizationEnabledKey
+ __AKInformationBeneficiaryLastModified
+ __AKInformationCanBeBeneficiary
+ __AKInformationCanBeCustodian
+ __AKInformationCanHaveBeneficiary
+ __AKInformationCanHaveCustodian
+ __AKInformationCustodianEnabled
+ __AKInformationCustodianLastModified
+ __AKInformationFamilyNameKey
+ __AKInformationForwardingEmailKey
+ __AKInformationGivenNameKey
+ __AKInformationGroupKitEligibilityKey
+ __AKInformationHasMDMKey
+ __AKInformationHmeMappingsKey
+ __AKInformationIsLegacyStudentKey
+ __AKInformationIsSeniorKey
+ __AKInformationIsSiwaEnabledKey
+ __AKInformationIsUnderageKey
+ __AKInformationMachineIDKey
+ __AKInformationMachineIDListKey
+ __AKInformationMakoAccountKey
+ __AKInformationManagedOrganizationNameKey
+ __AKInformationManagedOrganizationNotificationEmailAvailableKey
+ __AKInformationManagedOrganizationNotificationEmailKey
+ __AKInformationManagedOrganizationTypeKey
+ __AKInformationMasterKeyIDKey
+ __AKInformationOperationKey
+ __AKInformationPreviousEmailSelectedAsPrivateKey
+ __AKInformationPreviousSelectedEmailKey
+ __AKInformationPrimaryEmailKey
+ __AKInformationPrimaryVettedEmailKey
+ __AKInformationPrivateAttestationEnabledKey
+ __AKInformationReachableEmailsKey
+ __AKInformationReasonKey
+ __AKInformationRepairStateKey
+ __AKInformationSerialNumberKey
+ __AKInformationTimestampKey
+ __AKInformationUserAgeRangeKey
+ __AKInheritanceContextAccessCodeKey
+ __AKInheritanceContextAccessKeyKey
+ __AKInheritanceContextAltDSIDKey
+ __AKInheritanceContextBeneficiaryIdentifierKey
+ __AKInheritanceContextBeneficiarySetupTokenKey
+ __AKInheritanceContextFirstNameKey
+ __AKInheritanceContextIdentityTokenKey
+ __AKInheritanceContextLastNameKey
+ __AKInheritanceContextManifestKey
+ __AKInheritanceContextPasswordNameKey
+ __AKInternalSiwADefaultHME
+ __AKIsAuthorizingForSharedSIWAAccountKey
+ __AKIsCustodianSyncActionKey
+ __AKIsEligibleToMigrateToChildKey
+ __AKLastIDMSEnvironment
+ __AKLastLocale
+ __AKLoginHandlesKey
+ __AKMaskingStyleKey
+ __AKNonceKey
+ __AKOOPUIModeKey
+ __AKOverrideAttestationLoggingKey
+ __AKPiggbackingIDMSPresenceOverride
+ __AKPiggbackingLocalPresenceOverride
+ __AKPrefsDomain
+ __AKPreviousPTXID
+ __AKPrivateEmailClientAppNameKey
+ __AKPrivateEmailDomainHeaderFieldKey
+ __AKPrivateEmailOriginHeaderFieldKey
+ __AKPropertyAdditionalInfoKey
+ __AKPropertyAliasesKey
+ __AKPropertyDSIDKey
+ __AKPropertyLegacyAltDSID
+ __AKPropertyLoginHandlesKey
+ __AKPropertySecurityKeysKey
+ __AKPropertyServicesKey
+ __AKPropertyTrustedPhoneNumbersKey
+ __AKProtoAccountContextAgeRange
+ __AKProtoAccountContextGivenNameKey
+ __AKProtoAccountContextLastNameKey
+ __AKProtoAccountContextShouldForceShieldUI
+ __AKProxiedBundleID
+ __AKRecordBuildVersionKey
+ __AKRequestedScopesKey
+ __AKSafeCast
+ __AKScaleKey
+ __AKSecurityKeysKey
+ __AKServerBackoffSuiteName
+ __AKServerTimeAdjustmentConfigKey
+ __AKServiceIDKey
+ __AKServiceNamePiggyback
+ __AKSessionKeyHeaderKey
+ __AKSfrChosenBootPathExtension
+ __AKSfrManifestData
+ __AKSfrManifestLength
+ __AKSharedAccountKey
+ __AKSharedSIWAAccountGroupIDKey
+ __AKSharedSIWAAccountShareTokenKey
+ __AKShouldForceBaaValidationKey
+ __AKShouldForceHasSOSActiveDeviceKey
+ __AKShouldForceSOSNeededKey
+ __AKShouldReqeustPiggybackingPresenceEnforcement
+ __AKShouldRequestToArmDeviceToAllowPCSKeyUploadKey
+ __AKSignInWithAppleAccountAdamIDKey
+ __AKSignInWithAppleAccountClientIDKey
+ __AKSignInWithAppleAccountCreationDateKey
+ __AKSignInWithAppleAccountHasEULAKey
+ __AKSignInWithAppleAccountKey
+ __AKSignInWithAppleAccountLocalizedAppDeveloperNameKey
+ __AKSignInWithAppleAccountLocalizedAppNameKey
+ __AKSignInWithAppleAccountPrivacyPolicyURLKey
+ __AKSignInWithAppleAccountPrivateEmailKey
+ __AKSignInWithAppleAccountShareInfoGroupIDKey
+ __AKSignInWithAppleAccountShareInfoIsCurrentUserKey
+ __AKSignInWithAppleAccountShareInfoKey
+ __AKSignInWithAppleAccountShareInfoParticipantHandleKey
+ __AKSignInWithAppleAccountShareInfoParticipantIDKey
+ __AKSignInWithAppleAccountShareInfoParticipantNameKey
+ __AKSignInWithAppleAccountSharedScopesKey
+ __AKSignInWithAppleAccountTeamIDKey
+ __AKSignInWithAppleAccountUserIDKey
+ __AKSignInWithAppleAltDSIDKey
+ __AKSignInWithAppleCurrentGroupKey
+ __AKSignInWithAppleGroupsKey
+ __AKSignInWithAppleSimulateAccountSharingResponseKey
+ __AKSigningSessionConfigurationKeyAbsintheEnable
+ __AKSigningSessionConfigurationKeyBAAInterval
+ __AKSigningSessionConfigurationKeyConfigurations
+ __AKSigningSessionHeaderKeyAbsintheError
+ __AKSigningSessionHeaderKeyAbsintheV1
+ __AKSigningSessionHeaderKeyBAAAttestation
+ __AKSigningSessionHeaderKeyBAAAvailability
+ __AKSigningSessionHeaderKeyBAAClientInfoSignature
+ __AKSigningSessionHeaderKeyBAAClientTime
+ __AKSigningSessionHeaderKeyBAADeviceIdSignature
+ __AKSigningSessionHeaderKeyBAAError
+ __AKSigningSessionHeaderKeyBAALocalUUIDSignature
+ __AKSigningSessionHeaderKeyBAAPayloadHash
+ __AKSigningSessionHeaderKeyBAAProvisioningIdSignature
+ __AKSigningSessionHeaderKeyBAASignature
+ __AKSigningSessionHeaderKeyBAASignedPayloadHash
+ __AKSigningSessionHeaderKeyBAAUnerlyingErrors
+ __AKSigningSessionHeaderKeyHostBAAAttestation
+ __AKSigningSessionHeaderKeyHostBAAError
+ __AKSigningSessionHeaderKeyHostBAASignedPayloadHash
+ __AKSigningSessionProxyHeaderKeyAbsintheError
+ __AKSigningSessionProxyHeaderKeyAbsintheV1
+ __AKSigningSessionProxyHeaderKeyBAAAttestation
+ __AKSigningSessionProxyHeaderKeyBAAClientInfoSignature
+ __AKSigningSessionProxyHeaderKeyBAAError
+ __AKSigningSessionProxyHeaderKeyBAASignature
+ __AKSimulateAuthorizationForSharedAccountKey
+ __AKStateKey
+ __AKStrongDeviceIdentityMarkerKey
+ __AKSuppressHSA2Suggestions
+ __AKSuppressModalSheetsInMacBuddy
+ __AKSymmetricKeyDaemonConnectionCreate
+ __AKTeamIDKey
+ __AKTelemetryOptIn
+ __AKTelemetryOptInGracePeriodOverride
+ __AKTransactionIDKey
+ __AKTrustedPhoneNumbersKey
+ __AKURLBagKey
+ __AKURLBagKeyAllURLs
+ __AKURLBagKeyAllowListDomainsForSharingKey
+ __AKURLBagKeyAppleOwnedDomainsConfig
+ __AKURLBagKeyBAAConfig
+ __AKURLBagKeyBAAConfigCertToUse
+ __AKURLBagKeyBAAConfigCertValidityDays
+ __AKURLBagKeyBaaEnabled
+ __AKURLBagKeyBackgroundiCloudSignInConfigKey
+ __AKURLBagKeyClientBackoffDisabled
+ __AKURLBagKeyConfigurations
+ __AKURLBagKeyContinuationHeaderPrefixKey
+ __AKURLBagKeyCustodianCodeConfig
+ __AKURLBagKeyDisablePSCreateAndForgetLink
+ __AKURLBagKeyEasyStudentSignInDisabled
+ __AKURLBagKeyEnableSIWAChildAgeAttestationKey
+ __AKURLBagKeyEnvironments
+ __AKURLBagKeyFirstPartyURLEntitlementCheckDisabled
+ __AKURLBagKeyGrandSlamEndpointIdentifiers
+ __AKURLBagKeyInheritanceConfig
+ __AKURLBagKeyIsInlineFlowSupportedConfig
+ __AKURLBagKeyIsPhoneNumberSupportedConfig
+ __AKURLBagKeyMIDDriftTTRDisabled
+ __AKURLBagKeyPasskeyCleanupDisabled
+ __AKURLBagKeySecurityUpgradeServiceNamesKey
+ __AKURLBagKeySettingsInlineLogoViewDisabled
+ __AKURLBagKeyTTRConfigurations
+ __AKURLBagKeyTokenCacheDisabled
+ __AKURLBagKeyTrustedDeviceListHashDisabled
+ __AKURLBagKeyUrl
+ __AKURLBagKeyiForgotAppleIDLocked
+ __AKURLConfigurationKeyUIType
+ __AKURLConfigurationKeyUrl
+ __AKURLSessionConfigurationID
+ __AKURLSessionTimeout
+ __AKUseWebAuthenticationForIDPKey
+ __AKWalrusDefaultConfigDictionary
+ __NextTestBundleIdentifier
+ __OBJC_$_CLASS_METHODS_AKFollowUpController
+ ___63-[AKFollowUpController addFollowUpItems:telemetryFlowID:error:]_block_invoke
+ ___63-[AKFollowUpController removeAllFollowUpItems:telemetryFlowID:]_block_invoke
+ ___66-[AKFollowUpController removeFollowUpItems:telemetryFlowID:error:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48r_e31_v32?0"FLFollowUpItem"8Q16^B24ls32l8r48l8s40l8
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_0_1_4_0
+ ___os_log_helper_16_0_1_4_2
+ ___os_log_helper_16_0_1_8_0
+ ___os_log_helper_16_0_2_4_0_8_0
+ ___os_log_helper_16_0_2_8_0_4_2
+ ___os_log_helper_16_0_2_8_0_8_0
+ ___os_log_helper_16_0_3_8_0_8_0_4_2
+ ___os_log_helper_16_0_4_4_0_4_0_4_0_4_0
+ ___os_log_helper_16_0_5_4_0_4_0_4_0_4_0_4_0
+ ___os_log_helper_16_0_7_4_0_8_0_4_0_4_0_4_0_4_0_4_0
+ ___os_log_helper_16_2_1_8_32
+ ___os_log_helper_16_2_1_8_64
+ ___os_log_helper_16_2_1_8_66
+ ___os_log_helper_16_2_2_4_0_8_64
+ ___os_log_helper_16_2_2_4_2_8_66
+ ___os_log_helper_16_2_2_8_0_8_64
+ ___os_log_helper_16_2_2_8_0_8_66
+ ___os_log_helper_16_2_2_8_112_8_64
+ ___os_log_helper_16_2_2_8_32_4_0
+ ___os_log_helper_16_2_2_8_32_8_64
+ ___os_log_helper_16_2_2_8_64_4_0
+ ___os_log_helper_16_2_2_8_64_8_0
+ ___os_log_helper_16_2_2_8_64_8_64
+ ___os_log_helper_16_2_2_8_64_8_66
+ ___os_log_helper_16_2_2_8_66_8_64
+ ___os_log_helper_16_2_2_8_66_8_66
+ ___os_log_helper_16_2_3_8_0_4_2_8_66
+ ___os_log_helper_16_2_3_8_112_8_64_8_0
+ ___os_log_helper_16_2_3_8_64_4_0_8_64
+ ___os_log_helper_16_2_3_8_64_8_112_8_64
+ ___os_log_helper_16_2_3_8_64_8_64_8_64
+ ___os_log_helper_16_2_3_8_64_8_66_8_64
+ ___os_log_helper_16_2_3_8_66_8_64_8_0
+ ___os_log_helper_16_2_4_8_112_8_64_8_112_8_64
+ ___os_log_helper_16_3_1_8_65
+ ___os_log_helper_16_3_2_4_0_8_65
+ ___os_log_helper_16_3_2_8_65_8_64
+ ___os_log_helper_16_3_2_8_65_8_65
+ ___os_log_helper_16_3_2_8_65_8_66
+ __defaultTestBundleIdentifier
+ __getNSValueBytes
+ _aaf_unfair_lock_perform
+ _aaf_unfair_lock_perform_with_result
+ _ak_unfair_lock_perform
+ _ak_unfair_lock_perform_with_result
+ _allowSkipPinningOnInternalHardware
+ _audit_stringAAAFoundationSwift
+ _audit_stringAppStoreComponents
+ _audit_stringAuthenticationServices
+ _audit_stringBiometricSupport
+ _audit_stringCoreCDP
+ _audit_stringCoreCDPUI
+ _audit_stringCoreFollowUp
+ _audit_stringDeviceCheckInternal
+ _audit_stringKeychainCircle
+ _audit_stringProximityAppleIDSetupUI
+ _audit_stringRemoteUI
+ _audit_stringSetupAssistant
+ _audit_stringUIKit
+ _audit_stringUserManagement
+ _checkPinningPolicy
+ _getDeviceIdentityCreateHostSignatureSymbolLoc
+ _getDeviceIdentityIsSupportedSymbolLoc
+ _getDeviceIdentityIssueClientCertificateWithCompletionSymbolLoc
+ _getMAEGetActivationStateWithErrorSymbolLoc
+ _getkMAActivationStateUnactivated
+ _getkMAActivationStateUnactivatedSymbolLoc
+ _getkMAOptionsBAAKeychainAccessGroup
+ _getkMAOptionsBAAKeychainAccessGroupSymbolLoc
+ _getkMAOptionsBAAKeychainLabel
+ _getkMAOptionsBAAKeychainLabelSymbolLoc
+ _getkMAOptionsBAAOIDDeviceOSInformation
+ _getkMAOptionsBAAOIDDeviceOSInformationSymbolLoc
+ _getkMAOptionsBAAOIDSToInclude
+ _getkMAOptionsBAAOIDSToIncludeSymbolLoc
+ _getkMAOptionsBAAOIDUCRTDeviceIdentifiers
+ _getkMAOptionsBAAOIDUCRTDeviceIdentifiersSymbolLoc
+ _getkMAOptionsBAAValidity
+ _getkMAOptionsBAAValiditySymbolLoc
+ _kAAFClearFollowupEvent
+ _kAAFPostFollowupEvent
+ _launchedForAuthenticationServicesKey
+ _memcpy
+ _objc_msgSend$addFollowUpItems:telemetryFlowID:error:
+ _objc_msgSend$analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:
+ _objc_msgSend$clearNotificationsForItem:telemetryFlowID:error:
+ _objc_msgSend$followUpPostAnalyticsInfoWithIdentifier:telemetryFlowID:error:
+ _objc_msgSend$removeAllFollowUpItems:telemetryFlowID:
+ _objc_msgSend$removeFollowUpItems:telemetryFlowID:error:
+ _objc_msgSend$removeFollowUpItemsWithIdentifiers:telemetryFlowID:error:
+ _objc_msgSend$sendEventForFollowUpWithError:eventName:success:telemetryFlowID:error:
+ _objc_msgSend$setCfuType:
+ _objc_msgSend$setDeviceSessionID:
+ _objc_msgSend$setFlowID:
+ _objc_msgSend$setPostedReasonError:
- +[AAFAnalyticsEvent(AuthKit) ak_analyticsEventWithContext:eventName:error:].cold.1
- +[AKAbsintheSigner sharedSigner].cold.1
- +[AKAccountManager performWithinPersonaForAccount:withBlock:].cold.1
- +[AKAccountManager performWithinPersonaForAccount:withBlock:].cold.2
- +[AKAccountManager personaIDIfCurrentPersonaIsDataSeparated].cold.1
- +[AKAccountManager sharedInstance].cold.1
- +[AKAgeRangeSettingsExtractor defaultConfigDictionary].cold.1
- +[AKAgeRangeSettingsExtractor defaultConfigDictionary].cold.2
- +[AKAgeRangeSettingsExtractor extractAgeRangeConfigFromGlobalConfig:].cold.1
- +[AKAgeRangeSettingsExtractor extractAgeRangeConfigFromGlobalConfig:].cold.2
- +[AKAlertHandler sharedInstance].cold.1
- +[AKAnalyticsReporterRTC rtcAnalyticsReporter].cold.1
- +[AKAnalyticsSender sendAnalyticsEvent:context:account:error:].cold.1
- +[AKAnalyticsSender sendAnalyticsEvent:withError:].cold.1
- +[AKAnisetteProvisioningClientInterface XPCInterface].cold.1
- +[AKAnisetteProvisioningDaemonInterface XPCInterface].cold.1
- +[AKAppleIDAuthenticationClientInterface XPCInterface].cold.1
- +[AKAppleIDAuthenticationController sensitiveAuthenticationKeys].cold.1
- +[AKAppleIDAuthenticationController sensitiveTokenKeysForFullRedaction].cold.1
- +[AKAppleIDAuthenticationController sensitiveTokenKeys].cold.1
- +[AKAppleIDAuthenticationController tokenDictionaryKeys].cold.1
- +[AKAppleIDAuthenticationDaemonInterface XPCInterface].cold.1
- +[AKAppleIDServerResourceLoadDelegate sharedController].cold.1
- +[AKAppleIDSigningDaemonInterface XPCInterface].cold.1
- +[AKAttestationSigner sharedSigner].cold.1
- +[AKAuthorizationAgeValidator isValidAgeForRequest:account:].cold.1
- +[AKAuthorizationAgeValidator isValidAgeForRequest:account:].cold.2
- +[AKAuthorizationAgeValidator isValidAgeForRequest:account:].cold.3
- +[AKAuthorizationClientInterface XPCInterface].cold.1
- +[AKAuthorizationController _matchURLProcessingSet:url:].cold.1
- +[AKAuthorizationController _matchURLProcessingSet:url:].cold.2
- +[AKAuthorizationController isURLFromAllowListDomainsForSharingKey:].cold.1
- +[AKAuthorizationController isURLFromAppleOwnedDomain:].cold.1
- +[AKAuthorizationController sharedController].cold.1
- +[AKAuthorizationDaemonInterface XPCInterface].cold.1
- +[AKAuthorizationNotificationHandlerInterface XPCInterface].cold.1
- +[AKAuthorizationNotificationService _sharedService].cold.1
- +[AKAuthorizationPresenterHostInterface XPCInterface].cold.1
- +[AKAuthorizationStateBroadcastHandlerInterface XPCInterface].cold.1
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.1
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.2
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.3
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.4
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.5
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.6
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.7
- +[AKAuthorizationValidator canPerformAuthorizationRequest:error:].cold.8
- +[AKAuthorizationValidator canPerformPasswordRequest:error:].cold.1
- +[AKAuthorizationValidator canPerformPasswordRequest:error:].cold.2
- +[AKAutoBugCapture triggerAutoBugCaptureWithSubType:andBundleID:userInfo:].cold.1
- +[AKAutoBugCapture triggerAutoBugCaptureWithSubType:andBundleID:userInfo:].cold.2
- +[AKBiometricRatchetUtility resultForNonArmingFromError:].cold.1
- +[AKBiometricRatchetUtility resultForNonArmingFromError:].cold.2
- +[AKBiometricRatchetUtility resultForSuccessfulArmingFromResponse:].cold.1
- +[AKBiometricRatchetUtility setRatchetIdentifier:].cold.1
- +[AKCDPFactory walrusStatusLiveValue].cold.1
- +[AKCDPFactory walrusStatus].cold.1
- +[AKCDPFactory walrusStatus].cold.2
- +[AKCDPFactory webAccessChangeControllerForTargetStatus:].cold.1
- +[AKCDPFactory webAccessStatusLiveValue].cold.1
- +[AKCDPFactory webAccessStatus].cold.1
- +[AKCarouselAlertClientConnection sharedConnection].cold.1
- +[AKCarrierBundleUtilities sharedInstance].cold.1
- +[AKCircleRequestPayload _dictionaryWithPlistData:].cold.1
- +[AKCircleRequestPayload payloadWithResponseData:forCircleStep:].cold.1
- +[AKCircleRequestPayload payloadWithResponseData:forCircleStep:].cold.2
- +[AKCircleRequestPayload payloadWithResponseData:forCircleStep:].cold.3
- +[AKCircleRequestPayload payloadWithResponseData:forCircleStep:].cold.4
- +[AKCommandLineURLSession sharedServerUIURLSession].cold.1
- +[AKConfiguration sharedConfiguration].cold.1
- +[AKCustodianDaemonInterface XPCInterface].cold.1
- +[AKDevice _currentDeviceAuthenticationMode].cold.1
- +[AKDevice _systemVersionDictionary].cold.1
- +[AKDevice currentDevice].cold.1
- +[AKDevice deviceWithSerializedData:].cold.1
- +[AKDevice didConfirmDeviceWasActivated].cold.1
- +[AKDevice didConfirmDeviceWasActivated].cold.2
- +[AKDevice systemContainerURL].cold.1
- +[AKFLFollowUpController sharedInstance].cold.1
- +[AKFeatureManager sharedManager].cold.1
- +[AKFidoAuthorizationController isFidoUserCancelError:].cold.1
- +[AKFollowUpProviderFactory sharedAuthKitFollowupProvider].cold.1
- +[AKGlobalConfig sharedInstance].cold.1
- +[AKIORegistryReader sharedInstance].cold.1
- +[AKLAContextValidator validateExternalizedContext:error:].cold.1
- +[AKLAContextValidator validateExternalizedContext:error:].cold.2
- +[AKLoginCodeNotificationBuilder buildLoginCodeNotificationWithTitle:body:footer:loginCode:].cold.1
- +[AKLoginPresenterHostInterface XPCInterface].cold.1
- +[AKMasterToken tokenWithExternalizedVersion:lifetime:].cold.1
- +[AKMediaServicesController sharedInstance].cold.1
- +[AKNativeAccountRecoveryController requestForRecoveryCompletionWithContext:recoveredInfo:recoveryError:].cold.1
- +[AKNetworkObserver sharedNetworkObserver].cold.1
- +[AKPasswordResetPresenterHostInterface XPCInterface].cold.1
- +[AKPrivateEmailClientInterface XPCInterface].cold.1
- +[AKPrivateEmailDaemonInterface XPCInterface].cold.1
- +[AKPrivateEmailPresenterHostInterface XPCInterface].cold.1
- +[AKPrivateEmailValidator canPerformRequestWithAccount:error:].cold.1
- +[AKPrivateEmailValidator canPerformRequestWithAccount:error:].cold.2
- +[AKSecurityHelper signData:withKey:error:].cold.1
- +[AKSecurityHelper signData:withKey:error:].cold.2
- +[AKSymmetricKeyDaemonInterface XPCInterface].cold.1
- +[AKToken idmsTokenWithBase64String:].cold.1
- +[AKToken tokenWithBase64String:].cold.1
- +[AKURLBag _currentBagsUnderLockWithBlock:].cold.1
- +[AKURLBag sharedBag].cold.1
- +[AKURLSession _urlBagCache].cold.1
- +[AKWalrusConfigProvider sharedInstance].cold.1
- +[NSArray(AuthKit) ak_arrayWithJSONResponseData:].cold.1
- +[NSArray(AuthKit) ak_arrayWithJSONResponseData:].cold.2
- +[NSArray(AuthKit) ak_arrayWithJSONResponseData:].cold.3
- +[NSData(AuthKit) ak_dataWithBase64UrlEncodedString:].cold.1
- +[NSDate(AuthKit) _dateFormatter].cold.1
- +[NSMutableURLRequest(AuthKit) ak_anisetteHeadersWithCompanionData:].cold.1
- +[NSMutableURLRequest(AuthKit) ak_anisetteHeadersWithData:].cold.1
- +[NSMutableURLRequest(AuthKit) ak_proxiedAnisetteHeadersWithData:].cold.1
- +[NSString(AuthKit) ak_base64EncodedJsonFromObject:].cold.1
- +[NSXPCInterface(NSXPCInterface_AKRemoteViewServiceInterface) remoteViewServiceInterface].cold.1
- +[NSXPCInterface(NSXPCInterface_AKRemoteViewSessionInterface) remoteViewSessionInterface].cold.1
- -[AAFAnalyticsEvent(AuthKit) ak_updateTelemetryIdWithAccount:].cold.1
- -[AAFAnalyticsEvent(AuthKit) ak_updateWithAuthenticationResults:authContext:error:].cold.1
- -[AKAbsintheSigner _createSigningContextWithCompletionHandler:].cold.1
- -[AKAbsintheSigner _destroySigningContext].cold.1
- -[AKAbsintheSigner _generateSignatureForRequest:completionHandler:].cold.1
- -[AKAbsintheSigner _generateSignatureForRequest:completionHandler:].cold.2
- -[AKAbsintheSigner _sessionInfoFromCertificateData:].cold.1
- -[AKAbsintheSigner _sessionInfoFromCertificateData:].cold.2
- -[AKAbsintheSigner _sessionInfoFromCertificateData:].cold.3
- -[AKAccountManager DSIDForAccount:].cold.1
- -[AKAccountManager _aliasesForiCloudAccount:].cold.1
- -[AKAccountManager _aliasesForiCloudAccount:].cold.2
- -[AKAccountManager _altDSIDForiCloudAccount:].cold.1
- -[AKAccountManager _altDSIDForiCloudAccount:].cold.2
- -[AKAccountManager _credentialForAccount:].cold.1
- -[AKAccountManager _idmsWalrusStatusForAccount:].cold.1
- -[AKAccountManager _isAccountEligibleForSecurityUpgrade:ofServiceType:].cold.1
- -[AKAccountManager _isAccountEligibleForSecurityUpgrade:ofServiceType:].cold.2
- -[AKAccountManager _isSilentBurnCDPRepairEnabledForAccount:].cold.1
- -[AKAccountManager _isSilentEscrowRecordRepairEnabledForAccount:].cold.1
- -[AKAccountManager _isSilentEscrowRecordRepairEnabledForAccountV2:].cold.1
- -[AKAccountManager _removeAllRawPasswordCaches].cold.1
- -[AKAccountManager _removeTokenForKeys:forAccount:].cold.1
- -[AKAccountManager _removeTokenKey:forAccount:].cold.1
- -[AKAccountManager _reportTokenWithName:forAccount:error:].cold.1
- -[AKAccountManager _reportTokenWithTelemetryID:account:telemetryFlowID:error:].cold.1
- -[AKAccountManager _reportTokenWithTelemetryID:account:telemetryFlowID:error:].cold.2
- -[AKAccountManager _reportTokenWithTelemetryID:account:telemetryFlowID:error:].cold.3
- -[AKAccountManager _saveAccount:error:].cold.1
- -[AKAccountManager _saveAccount:error:].cold.2
- -[AKAccountManager _setTokenCreationTimeForToken:tokenID:account:credential:].cold.1
- -[AKAccountManager _setTokenCreationTimeForToken:tokenID:account:credential:].cold.2
- -[AKAccountManager _setTokenCreationTimeForToken:tokenID:account:credential:].cold.3
- -[AKAccountManager _shouldBlockAuthorizationForPersona:].cold.1
- -[AKAccountManager _telemetryDeviceSessionIDForAccount:].cold.1
- -[AKAccountManager _tokenWithName:forAccount:error:].cold.1
- -[AKAccountManager _tokenWithName:forAccount:error:].cold.2
- -[AKAccountManager _tokenWithName:forAccount:error:].cold.3
- -[AKAccountManager _triggerSilentTTRFor:].cold.1
- -[AKAccountManager accountAccessTelemetryOptInDateForAccount:].cold.1
- -[AKAccountManager accountAccessTelemetryOptInForAccount:].cold.1
- -[AKAccountManager accountAccessTelemetryOptInForAccount:].cold.2
- -[AKAccountManager accountImprovementOptInForAccount:].cold.1
- -[AKAccountManager accountImprovementOptInValueForAccount:].cold.1
- -[AKAccountManager accountImprovementOptInValueForAccount:].cold.2
- -[AKAccountManager activeiCloudPrivateEmailCountForAccount:].cold.1
- -[AKAccountManager additionalInfoForAccount:].cold.1
- -[AKAccountManager adpCohortForAccount:].cold.1
- -[AKAccountManager ageOfMajorityForAccount:].cold.1
- -[AKAccountManager aliasesForAccount:].cold.1
- -[AKAccountManager allTokensForAccount:error:].cold.1
- -[AKAccountManager altDSIDForAccount:].cold.1
- -[AKAccountManager appleIDAccountType].cold.1
- -[AKAccountManager appleIDCountryCodeForAccount:].cold.1
- -[AKAccountManager authKitAccountTypeWithError:].cold.1
- -[AKAccountManager authenticationModeForAccount:].cold.1
- -[AKAccountManager authorizationUsedForAccount:].cold.1
- -[AKAccountManager beneficiaryInfoForAccount:].cold.1
- -[AKAccountManager beneficiaryLastModifiedForAccount:].cold.1
- -[AKAccountManager beneficiaryListVersionForAccount:].cold.1
- -[AKAccountManager birthYearForAccount:].cold.1
- -[AKAccountManager canAttestAgeForAccount:].cold.1
- -[AKAccountManager canBeBeneficiaryForAccount:].cold.1
- -[AKAccountManager canBeCustodianForAccount:].cold.1
- -[AKAccountManager canHaveBeneficiaryForAccount:].cold.1
- -[AKAccountManager canHaveCustodianForAccount:].cold.1
- -[AKAccountManager clearDeviceRemovalReasonFromAccount:].cold.1
- -[AKAccountManager configDataVersionForAccount:].cold.1
- -[AKAccountManager configValue:forAccount:].cold.1
- -[AKAccountManager custodianEnabledForAccount:].cold.1
- -[AKAccountManager custodianInfosForAccount:].cold.1
- -[AKAccountManager custodianLastModifiedForAccount:].cold.1
- -[AKAccountManager custodianListVersionForAccount:].cold.1
- -[AKAccountManager deletedDevicesCacheExpiryOffsetForAccount:].cold.1
- -[AKAccountManager demoAccountForAccount:].cold.1
- -[AKAccountManager deviceListVersionForAccount:].cold.1
- -[AKAccountManager deviceRemovalReasonForAccount:].cold.1
- -[AKAccountManager edpStateForAccount:].cold.1
- -[AKAccountManager edpStateValueForAccount:].cold.1
- -[AKAccountManager familyNameForAccount:].cold.1
- -[AKAccountManager forwardingEmailForAccount:].cold.1
- -[AKAccountManager get3PRegulatoryOverride:].cold.1
- -[AKAccountManager givenNameForAccount:].cold.1
- -[AKAccountManager groupKitEligibilityForAccount:].cold.1
- -[AKAccountManager hasMDMForAccount:].cold.1
- -[AKAccountManager hasModernRecoveryKeyForAccount:].cold.1
- -[AKAccountManager hasPersonaAvailableForAltDSID:].cold.1
- -[AKAccountManager hasPrimaryiCloudAccountForAltDSID:].cold.1
- -[AKAccountManager hasSOSActiveDeviceForAccount:].cold.1
- -[AKAccountManager iCloudAccountType].cold.1
- -[AKAccountManager idmsEDPTokenIdForAccount:].cold.1
- -[AKAccountManager idmsWalrusStatusForAccount:].cold.1
- -[AKAccountManager idmsWalrusStatusForAccount:].cold.2
- -[AKAccountManager inactiveiCloudPrivateEmailCountForAccount:].cold.1
- -[AKAccountManager isAskToBuyForAccount:].cold.1
- -[AKAccountManager isBeneficiaryForAccount:].cold.1
- -[AKAccountManager isEligibleToMigrateToChildForAccount:].cold.1
- -[AKAccountManager isFidoForAccount:].cold.1
- -[AKAccountManager isFulliCloudAccount:].cold.1
- -[AKAccountManager isNotificationEmailAvailableForAccount:].cold.1
- -[AKAccountManager isPasscodeAuthEnabledForAccount:].cold.1
- -[AKAccountManager isPasscodeAuthForAccount:].cold.1
- -[AKAccountManager isPrimaryiCloudAccount:].cold.1
- -[AKAccountManager isPrimaryiCloudAccount:].cold.2
- -[AKAccountManager isPrimaryiCloudAccountEmailVerified:].cold.1
- -[AKAccountManager isPrimaryiCloudAccountEmailVerified:].cold.2
- -[AKAccountManager isProximityAuthEligible:].cold.1
- -[AKAccountManager isSOSNeededForAccount:].cold.1
- -[AKAccountManager isSignOutInProgress:].cold.1
- -[AKAccountManager isSilentBurnCDPRepairEnabledForAccount:].cold.1
- -[AKAccountManager isSilentBurnCDPRepairEnabledForAccount:].cold.2
- -[AKAccountManager isSilentEscrowRecordRepairEnabledForAccount:].cold.1
- -[AKAccountManager isSilentEscrowRecordRepairEnabledForAccount:].cold.2
- -[AKAccountManager isSilentEscrowRecordRepairEnabledForAccountV2:].cold.1
- -[AKAccountManager isSilentEscrowRecordRepairEnabledForAccountV2:].cold.2
- -[AKAccountManager isSiwaEnabledForChildAccount:].cold.1
- -[AKAccountManager loginHandlesForAccount:].cold.1
- -[AKAccountManager managedOrganizationNameForAccount:].cold.1
- -[AKAccountManager managedOrganizationTypeForAccount:].cold.1
- -[AKAccountManager markedForSignOutForAccount:].cold.1
- -[AKAccountManager mdmInformationRequiredForAccount:].cold.1
- -[AKAccountManager needsRepairForAccount:].cold.1
- -[AKAccountManager nextLivenessNonce:].cold.1
- -[AKAccountManager notificationEmailForAccount:].cold.1
- -[AKAccountManager passkeyEligibleForAccount:].cold.1
- -[AKAccountManager passkeyPresentForAccount:].cold.1
- -[AKAccountManager passkeyRegistrationAttemptDateForAccount:].cold.1
- -[AKAccountManager passkeysDeletionAttemptDateForAccount:].cold.1
- -[AKAccountManager passkeysInKeychainCountForAccount:].cold.1
- -[AKAccountManager passwordVersionForAccount:].cold.1
- -[AKAccountManager phoneAsAppleIDForAccount:].cold.1
- -[AKAccountManager piggybackingApprovalEligible:].cold.1
- -[AKAccountManager previousAccountInfoRefreshDateForAccount:].cold.1
- -[AKAccountManager primaryEmailAddressForAccount:].cold.1
- -[AKAccountManager privateAttestationEnabledForAccount:].cold.1
- -[AKAccountManager protoAccountType].cold.1
- -[AKAccountManager reachableEmailAddressesForAccount:].cold.1
- -[AKAccountManager removeAllPasswordResetTokens].cold.1
- -[AKAccountManager renewDeviceSessionIDForAccount:].cold.1
- -[AKAccountManager renewDeviceSessionIDForAccount:].cold.2
- -[AKAccountManager renewDeviceSessionIDForAccount:].cold.3
- -[AKAccountManager renewDeviceSessionIDForAccount:].cold.4
- -[AKAccountManager repairStateForAccount:].cold.1
- -[AKAccountManager resetAccountImprovementOptInForAccount:error:].cold.1
- -[AKAccountManager resetAccountImprovementOptInForAccount:error:].cold.2
- -[AKAccountManager resetAccountImprovementOptInForAccount:error:].cold.3
- -[AKAccountManager securityKeysForAccount:].cold.1
- -[AKAccountManager securityLevelForAccount:].cold.1
- -[AKAccountManager selectedAuthorizationEmailForAccount:].cold.1
- -[AKAccountManager selectedPrivateEmailForAccount:].cold.1
- -[AKAccountManager serverExperimentalFeaturesForAccount:].cold.1
- -[AKAccountManager set3PRegulatoryOverride:forAccount:].cold.1
- -[AKAccountManager setADPCohort:forAccount:].cold.1
- -[AKAccountManager setADPCohort:forAccount:].cold.2
- -[AKAccountManager setAccountAccessTelemetryOptIn:forAccount:error:].cold.1
- -[AKAccountManager setAccountAccessTelemetryOptIn:forAccount:error:].cold.2
- -[AKAccountManager setAccountAccessTelemetryOptIn:forAccount:error:].cold.3
- -[AKAccountManager setAccountAccessTelemetryOptIn:forAccount:error:].cold.4
- -[AKAccountManager setAccountImprovementOptIn:forAccount:error:].cold.1
- -[AKAccountManager setAccountImprovementOptIn:forAccount:error:].cold.2
- -[AKAccountManager setAccountImprovementOptIn:forAccount:error:].cold.3
- -[AKAccountManager setAccountImprovementOptIn:forAccount:error:].cold.4
- -[AKAccountManager setActiveiCloudPrivateEmailCount:forAccount:].cold.1
- -[AKAccountManager setAdditionalInfo:forAccount:].cold.1
- -[AKAccountManager setAgeOfMajority:forAccount:].cold.1
- -[AKAccountManager setAliases:forAccount:].cold.1
- -[AKAccountManager setAltDSID:forAccount:].cold.1
- -[AKAccountManager setAltDSID:forAccount:].cold.2
- -[AKAccountManager setAppleIDCountryCode:forAccount:].cold.1
- -[AKAccountManager setAskToBuy:forAccount:].cold.1
- -[AKAccountManager setAuthenticationMode:forAccount:].cold.1
- -[AKAccountManager setAuthorizationUsed:forAccount:].cold.1
- -[AKAccountManager setBeneficiary:forAccount:].cold.1
- -[AKAccountManager setBeneficiaryInfo:forAccount:].cold.1
- -[AKAccountManager setBeneficiaryLastModified:forAccount:].cold.1
- -[AKAccountManager setBeneficiaryListVersion:forAccount:].cold.1
- -[AKAccountManager setBirthYear:forAccount:].cold.1
- -[AKAccountManager setCanAttestAge:forAccount:].cold.1
- -[AKAccountManager setCanBeBeneficiary:forAccount:].cold.1
- -[AKAccountManager setCanBeCustodian:forAccount:].cold.1
- -[AKAccountManager setCanHaveBeneficiary:forAccount:].cold.1
- -[AKAccountManager setCanHaveCustodian:forAccount:].cold.1
- -[AKAccountManager setConfigDataVersion:forAccount:].cold.1
- -[AKAccountManager setConfigValue:forKey:forAccount:].cold.1
- -[AKAccountManager setCredentialStorageOption:forAccount:].cold.1
- -[AKAccountManager setCustodianEnabled:forAccount:].cold.1
- -[AKAccountManager setCustodianInfos:forAccount:].cold.1
- -[AKAccountManager setCustodianLastModified:forAccount:].cold.1
- -[AKAccountManager setCustodianListVersion:forAccount:].cold.1
- -[AKAccountManager setDSID:forAccount:].cold.1
- -[AKAccountManager setDSID:forAccount:].cold.2
- -[AKAccountManager setDSID:forAccount:].cold.3
- -[AKAccountManager setDeletedDevicesCacheExpiryOffset:forAccount:].cold.1
- -[AKAccountManager setDemoAccount:forAccount:].cold.1
- -[AKAccountManager setDeviceListVersion:forAccount:].cold.1
- -[AKAccountManager setDeviceRemovalReason:onAccount:].cold.1
- -[AKAccountManager setDeviceRemovalReason:onAccount:].cold.2
- -[AKAccountManager setEDPState:forAccount:].cold.1
- -[AKAccountManager setFamilyName:forAccount:].cold.1
- -[AKAccountManager setFido:forAccount:].cold.1
- -[AKAccountManager setForwardingEmail:forAccount:].cold.1
- -[AKAccountManager setGivenName:forAccount:].cold.1
- -[AKAccountManager setGroupKitEligibility:forAccount:].cold.1
- -[AKAccountManager setHasMDM:forAccount:].cold.1
- -[AKAccountManager setHasModernRecoveryKey:forAccount:].cold.1
- -[AKAccountManager setHasSOSActiveDevice:forAccount:].cold.1
- -[AKAccountManager setIdMSEDPTokenId:forAccount:].cold.1
- -[AKAccountManager setIdmsWalrusStatus:forAccount:].cold.1
- -[AKAccountManager setInactiveiCloudPrivateEmailCount:forAccount:].cold.1
- -[AKAccountManager setIsEligibleToMigrateToChild:forAccount:].cold.1
- -[AKAccountManager setIsNotificationEmailAvailable:forAccount:].cold.1
- -[AKAccountManager setIsProximityAuthEligible:forAccount:].cold.1
- -[AKAccountManager setIsSiwaEnabled:forChildAccount:].cold.1
- -[AKAccountManager setLoginHandles:forAccount:].cold.1
- -[AKAccountManager setMDMInformationRequired:forAccount:].cold.1
- -[AKAccountManager setManagedOrganizationName:forAccount:].cold.1
- -[AKAccountManager setManagedOrganizationType:forAccount:].cold.1
- -[AKAccountManager setMarkedForSignOut:forAccount:].cold.1
- -[AKAccountManager setNotificationEmail:forAccount:].cold.1
- -[AKAccountManager setPasscodeAuth:forAccount:].cold.1
- -[AKAccountManager setPasscodeAuthEnabled:forAccount:].cold.1
- -[AKAccountManager setPasskeyEligible:forAccount:].cold.1
- -[AKAccountManager setPasskeyPresent:forAccount:].cold.1
- -[AKAccountManager setPasskeyRegistrationAttemptDateForAccount:forAccount:].cold.1
- -[AKAccountManager setPasskeysDeletionAttemptDate:forAccount:].cold.1
- -[AKAccountManager setPasskeysInKeychainCount:forAccount:].cold.1
- -[AKAccountManager setPasswordVersion:forAccount:].cold.1
- -[AKAccountManager setPendingDOB:forAccount:].cold.1
- -[AKAccountManager setPhoneAsAppleID:forAccount:].cold.1
- -[AKAccountManager setPiggybackingApprovalEligible:forAccount:].cold.1
- -[AKAccountManager setPreviousAccountInfoRefreshDate:forAccount:].cold.1
- -[AKAccountManager setPrimaryEmailAddress:forAccount:].cold.1
- -[AKAccountManager setPrivateAttestationEnabled:forAccount:].cold.1
- -[AKAccountManager setReachableEmailAddresses:forAccount:].cold.1
- -[AKAccountManager setRepairState:forAccount:].cold.1
- -[AKAccountManager setSOSNeeded:forAccount:].cold.1
- -[AKAccountManager setSRPProtocol:forAccount:].cold.1
- -[AKAccountManager setSecurityKeys:forAccount:].cold.1
- -[AKAccountManager setSecurityLevel:forAccount:].cold.1
- -[AKAccountManager setSelectedAuthorizationEmail:forAccount:].cold.1
- -[AKAccountManager setSelectedPrivateEmail:forAccount:].cold.1
- -[AKAccountManager setServerExperimentalFeatures:forAccount:].cold.1
- -[AKAccountManager setSharingGroupLastNotificationDate:forAccount:].cold.1
- -[AKAccountManager setSignOutInProgress:forAccount:].cold.1
- -[AKAccountManager setSilentBurnCDPRepairEnabled:forAccount:].cold.1
- -[AKAccountManager setSilentEscrowRecordRepairEnabled:forAccount:].cold.1
- -[AKAccountManager setSilentEscrowRecordRepairEnabledV2:forAccount:].cold.1
- -[AKAccountManager setTelemetryDeviceSessionID:forAccount:].cold.1
- -[AKAccountManager setTrustedPhoneNumbers:forAccount:].cold.1
- -[AKAccountManager setUserAgeRange:forAccount:].cold.1
- -[AKAccountManager setUserIsSenior:forAccount:].cold.1
- -[AKAccountManager setUserUnderage:forAccount:].cold.1
- -[AKAccountManager setVerifiedPrimaryEmail:forAccount:].cold.1
- -[AKAccountManager setWebAccessEnabled:forAccount:].cold.1
- -[AKAccountManager sharingGroupLastNotificationDateForAccount:].cold.1
- -[AKAccountManager shieldSignInOrCreateFlows].cold.1
- -[AKAccountManager shieldSignInOrCreateFlows].cold.2
- -[AKAccountManager srpProtocolForAccount:].cold.1
- -[AKAccountManager telemetryDeviceSessionIDForAccount:].cold.1
- -[AKAccountManager tokenCreationDateWithIdentifier:forAccount:error:].cold.1
- -[AKAccountManager tokenCreationDateWithIdentifier:forAccount:error:].cold.2
- -[AKAccountManager tokenCreationDateWithIdentifier:forAccount:error:].cold.3
- -[AKAccountManager tokenCreationTimeStampWithIdentifier:forAccount:error:].cold.1
- -[AKAccountManager tokenCreationTimeStampWithIdentifier:forAccount:error:].cold.2
- -[AKAccountManager tokenCreationTimeStampWithIdentifier:forAccount:error:].cold.3
- -[AKAccountManager transportableAuthKitAccount:].cold.1
- -[AKAccountManager trustedPhoneNumbersForAccount:].cold.1
- -[AKAccountManager updateAccountAccessTelemetryOptInTimestampForAccount:withOptIn:].cold.1
- -[AKAccountManager updateAuthModeTimestampForAccount:].cold.1
- -[AKAccountManager updateSatoriWarmUpTimestampForAccount:].cold.1
- -[AKAccountManager userAgeRangeForAccount:].cold.1
- -[AKAccountManager userIsSeniorForAccount:].cold.1
- -[AKAccountManager userUnderAgeForAccount:].cold.1
- -[AKAccountManager verifiedPrimaryEmailForAccount:].cold.1
- -[AKAccountManager webAccessEnabledForAccount:].cold.1
- -[AKAccountRecoveryStepChangePassword _beginChangePasswordWithResponse:model:completion:].cold.1
- -[AKAccountRecoveryStepChangePassword _beginChangePasswordWithResponse:model:completion:].cold.2
- -[AKAccountRecoveryStepChangePassword _verifyNewPasswordWithRowID:confirmRowID:model:completion:].cold.1
- -[AKAccountRecoveryStepSMSVerificationCode _beginSMSCodeVerificationWithResponse:model:completion:].cold.1
- -[AKAccountRecoveryStepSMSVerificationCode _beginSMSCodeVerificationWithResponse:model:completion:].cold.2
- -[AKAccountRecoveryStepSMSVerificationCode _beginSMSCodeVerificationWithResponse:model:completion:].cold.3
- -[AKAccountRecoveryStepSMSVerificationCode _beginSMSCodeVerificationWithResponse:model:completion:].cold.4
- -[AKAccountRecoveryStepVerifyAppleID _beginVerifyAppleIDWithResponse:model:completion:].cold.1
- -[AKAccountRecoveryStepVerifyAppleID _verifyAppleIDWithModel:completion:].cold.1
- -[AKAccountRecoveryStepVerifyPhoneNumber _beginVerifyPhoneNumberWithResponse:model:completion:].cold.1
- -[AKAccountRecoveryStepVerifyPhoneNumber _processPhoneNumber:response:model:completion:].cold.1
- -[AKAccountRecoveryStepVerifyPhoneNumber _processPhoneNumber:response:model:completion:].cold.2
- -[AKAccountRecoveryStepVerifyPhoneNumber _verifyPhoneNumberWithModel:completion:].cold.1
- -[AKAccountRecoveryStepiCloudSecurityCode _verifyLocalSecretWithModel:completion:].cold.1
- -[AKAccountRecoveryStepiCloudSecurityCode _verifyPinViewWithResponse:model:completion:].cold.1
- -[AKAccountRecoveryStepiCloudSecurityCode _verifyRemoteSecretWithRecoveryContext:recoveredInfo:recoveryError:model:completion:].cold.1
- -[AKAccountRecoveryStepiCloudSecurityCode _verifyRemoteSecretWithServerInfo:model:completion:].cold.1
- -[AKAccountRecoveryStepiCloudSecurityCode cdpContext:promptForAdoptionOfMultipleICSC:].cold.1
- -[AKAccountRecoveryStepiCloudSecurityCode cdpContext:promptForBeneficiaryAccessKeyWithCompletion:].cold.1
- -[AKAccountRecoveryStepiCloudSecurityCode cdpContext:promptForICSCWithIsNumeric:numericLength:isRandom:validator:].cold.1
- -[AKAccountRecoveryStepiCloudSecurityCode cdpContext:promptForInteractiveAuthenticationWithCompletion:].cold.1
- -[AKAgeRangeSettingsCache _configurationValueForKey:].cold.1
- -[AKAgeRangeSettingsCache _setConfigurationValue:forKey:].cold.1
- -[AKAgeRangeSettingsCache _updateAgeRangeSettings].cold.1
- -[AKAgeRangeSettingsCache updateAgeRangeCacheWithGlobalConfig:].cold.1
- -[AKAgeRangeSettingsCache updateAgeRangeCacheWithGlobalConfig:].cold.2
- -[AKAgeRangeSettingsCache updateAgeRangeCacheWithGlobalConfig:].cold.3
- -[AKAgeRangeSettingsProvider refreshAgeRangeWithCompletion:].cold.1
- -[AKAlertHandler showAlert:primaryAction:altAction:cancelAction:].cold.1
- -[AKAlertHandler showAlert:primaryAction:altAction:cancelAction:].cold.2
- -[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:error:].cold.1
- -[AKAnisetteProvisioningController anisetteDataForURLRequest:completion:].cold.1
- -[AKAnisetteProvisioningController attestationDataForRequestData:error:].cold.1
- -[AKAnisetteProvisioningController fetchAnisetteDataAndProvisionIfNecessary:error:].cold.1
- -[AKAnisetteProvisioningController handleAttestationResponseWithResponseData:completion:].cold.1
- -[AKAnisetteProvisioningController handleAttestationResponseWithResponseData:completion:].cold.2
- -[AKAnisetteProvisioningController handleAttestationResponseWithResponseData:completion:].cold.3
- -[AKAppleIDAuthenticationCommandLineContext _collectAndHandleTermsAndConditionsWithResponseDictionary:configuration:completion:].cold.1
- -[AKAppleIDAuthenticationCommandLineContext _handleServerUIBirthdayVerificationWithResponseDictionary:configuration:completion:].cold.1
- -[AKAppleIDAuthenticationCommandLineContext _handleServerUIPasswordVerificationWithResponseDictionary:configuration:completion:].cold.1
- -[AKAppleIDAuthenticationCommandLineContext _handleServerUIPhoneVerificationWithResponseDictionary:configuration:completion:].cold.1
- -[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:].cold.1
- -[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:].cold.2
- -[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:].cold.3
- -[AKAppleIDAuthenticationCommandLineContext _jsonPostbackDictionaryForCode:numberId:].cold.1
- -[AKAppleIDAuthenticationCommandLineContext _presentServerUIWithConfiguration:completion:].cold.1
- -[AKAppleIDAuthenticationCommandLineContext _promptForBirthday].cold.1
- -[AKAppleIDAuthenticationCommandLineContext _promptUserForSelectionWithTrustedNumbers:].cold.1
- -[AKAppleIDAuthenticationContext _interpolatedReason].cold.1
- -[AKAppleIDAuthenticationContext _sanitizedCopy].cold.1
- -[AKAppleIDAuthenticationContext _setPassword:].cold.1
- -[AKAppleIDAuthenticationContext _updateWithValuesFromContext:].cold.1
- -[AKAppleIDAuthenticationContext _updateWithValuesFromContext:].cold.2
- -[AKAppleIDAuthenticationContext isConfiguredForTokenUpgrade].cold.1
- -[AKAppleIDAuthenticationContext isContextEligibleForPasscodeAuth].cold.1
- -[AKAppleIDAuthenticationContext presentLoginAlertWithError:title:message:completion:].cold.1
- -[AKAppleIDAuthenticationContext setRequestedNewAccountAgeRange:].cold.1
- -[AKAppleIDAuthenticationContextManager _clientSideContextForServerContext:].cold.1
- -[AKAppleIDAuthenticationContextManager _clientSideContextForServerContext:].cold.2
- -[AKAppleIDAuthenticationContextManager activateProximitySession:context:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager activateProximitySession:context:completion:].cold.2
- -[AKAppleIDAuthenticationContextManager dismissBasicLoginUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager dismissNativeRecoveryUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager dismissProximityPairingUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager dismissProximityPairingUIForContext:completion:].cold.2
- -[AKAppleIDAuthenticationContextManager dismissProximityPairingUIForContext:completion:].cold.3
- -[AKAppleIDAuthenticationContextManager dismissSecondFactorUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager dismissServerProvidedUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager eraseAnisetteForContext:withCompletion:].cold.1
- -[AKAppleIDAuthenticationContextManager fetchAnisetteDataForContext:provisionIfNecessary:withCompletion:].cold.1
- -[AKAppleIDAuthenticationContextManager fetchPeerAttestationDataForContext:withRequest:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager legacyAnisetteDataForContext:DSID:withCompletion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentBasicLoginUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentFidoAuthForContext:fidoContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentFidoAuthForContext:fidoContext:completion:].cold.2
- -[AKAppleIDAuthenticationContextManager presentFidoAuthForContext:fidoContext:completion:].cold.3
- -[AKAppleIDAuthenticationContextManager presentKeepUsingUIForContext:appleID:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentKeepUsingUIForContext:appleID:completion:].cold.2
- -[AKAppleIDAuthenticationContextManager presentKeepUsingUIForContext:appleID:completion:].cold.3
- -[AKAppleIDAuthenticationContextManager presentLoginAlertForContext:withError:title:message:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentNativeRecoveryUIForContext:recoveryContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentProximityBroadcastUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentProximityBroadcastUIForContext:completion:].cold.2
- -[AKAppleIDAuthenticationContextManager presentProximityBroadcastUIForContext:completion:].cold.3
- -[AKAppleIDAuthenticationContextManager presentProximityPairingUIForContext:verificationCode:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentProximityPairingUIForContext:verificationCode:completion:].cold.2
- -[AKAppleIDAuthenticationContextManager presentProximityPairingUIForContext:verificationCode:completion:].cold.3
- -[AKAppleIDAuthenticationContextManager presentProximityPinCodeUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentProximityPinCodeUIForContext:completion:].cold.2
- -[AKAppleIDAuthenticationContextManager presentProximityPinCodeUIForContext:completion:].cold.3
- -[AKAppleIDAuthenticationContextManager presentSecondFactorAlertForContext:withError:title:message:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentSecondFactorUIForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager presentServerProvidedUIForContext:withConfiguration:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager provisionAnisetteForContext:withCompletion:].cold.1
- -[AKAppleIDAuthenticationContextManager registerContext:].cold.1
- -[AKAppleIDAuthenticationContextManager registerContext:].cold.2
- -[AKAppleIDAuthenticationContextManager shouldContinueWithAuthenticationResults:error:forContextID:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager showProximityErrorForContext:completion:].cold.1
- -[AKAppleIDAuthenticationContextManager showProximityErrorForContext:completion:].cold.2
- -[AKAppleIDAuthenticationContextManager syncAnisetteForContext:withSIMData:completion:].cold.1
- -[AKAppleIDAuthenticationController activeLoginCode:].cold.1
- -[AKAppleIDAuthenticationController authenticateWithContext:completion:].cold.1
- -[AKAppleIDAuthenticationController authenticateWithContext:completion:].cold.2
- -[AKAppleIDAuthenticationController dealloc].cold.1
- -[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:].cold.1
- -[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:].cold.1
- -[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:].cold.1
- -[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:].cold.1
- -[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:].cold.1
- -[AKAppleIDAuthenticationController isDevicePasscodeProtected:].cold.1
- -[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:].cold.1
- -[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:].cold.1
- -[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:].cold.1
- -[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:].cold.1
- -[AKAppleIDPasskeyAuthenticationController _authorizationControllerForAccount:].cold.1
- -[AKAppleIDPasskeyAuthenticationController _onqueue_authorizationController:didCompleteWithAuthorization:error:].cold.1
- -[AKAppleIDPasskeyAuthenticationController _onqueue_authorizationController:didCompleteWithAuthorization:error:].cold.2
- -[AKAppleIDPasskeyAuthenticationController _onqueue_authorizationController:didCompleteWithAuthorization:error:].cold.3
- -[AKAppleIDPasskeyAuthenticationController _onqueue_authorizationController:didCompleteWithAuthorization:error:].cold.4
- -[AKAppleIDPasskeyAuthenticationController _onqueue_createPasskeyWithContext:completion:].cold.1
- -[AKAppleIDPasskeyAuthenticationController _onqueue_createPasskeyWithContext:completion:].cold.2
- -[AKAppleIDPasskeyAuthenticationController _onqueue_createPasskeyWithContext:completion:].cold.3
- -[AKAppleIDPasskeyAuthenticationController _onqueue_createPasskeyWithContext:completion:].cold.4
- -[AKAppleIDPasskeyAuthenticationController _onqueue_createPasskeyWithContext:completion:].cold.5
- -[AKAppleIDPasskeyAuthenticationController _popPasskeyRequestStateForController:].cold.1
- -[AKAppleIDPasskeyAuthenticationController _pushPasskeyRequestState:forController:].cold.1
- -[AKAppleIDPasskeyController remoteServiceDidInterrupt].cold.1
- -[AKAppleIDPasskeyController remoteServiceDidInvalidate].cold.1
- -[AKAppleIDRecoveryController _beginAccountRecoveryWithModel:completion:].cold.1
- -[AKAppleIDRecoveryController _logResponse:].cold.1
- -[AKAppleIDRecoveryController _processResponse:model:withCompletion:].cold.1
- -[AKAppleIDServerResourceLoadDelegate _fetchApplicationNameForBundleId:].cold.1
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.1
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.2
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.3
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.4
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.5
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.6
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.7
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.8
- -[AKAppleIDServerResourceLoadDelegate _signRequest:].cold.9
- -[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:].cold.1
- -[AKAppleIDServerResourceLoadDelegate decorateWithPrivateEmailContext:].cold.1
- -[AKAppleIDServerResourceLoadDelegate signRequest:].cold.1
- -[AKAppleIDServerResourceLoadDelegate signRequestWithBasicHeaders:].cold.1
- -[AKAppleIDServerResourceLoadDelegate signRequestWithBasicHeaders:].cold.2
- -[AKAppleIDServerResourceLoadDelegate signRequestWithBasicHeaders:].cold.3
- -[AKAppleIDServerResourceLoadDelegate signRequestWithBasicHeaders:].cold.4
- -[AKAppleIDServerResourceLoadDelegate signRequestWithBasicHeaders:].cold.5
- -[AKAppleIDServerResourceLoadDelegate signRequestWithCommonHeaders:].cold.1
- -[AKAppleIDServerResourceLoadDelegate signRequestWithCommonHeaders:].cold.2
- -[AKAppleIDServerResourceLoadDelegate signRequestWithCommonHeaders:].cold.3
- -[AKAppleIDServerResourceLoadDelegate signRequestWithCommonHeaders:].cold.4
- -[AKAppleIDServerResourceLoadDelegate signRequestWithCommonHeaders:].cold.5
- -[AKAppleIDServerResourceLoadDelegate updateWithAuthResults:].cold.1
- -[AKAppleIDServerResourceLoadDelegate updateWithAuthResults:].cold.2
- -[AKAppleIDServerResourceLoadDelegate updateWithAuthResults:].cold.3
- -[AKAppleIDServerResourceLoadDelegate updateWithAuthResults:].cold.4
- -[AKAppleIDServerResourceLoadDelegate updateWithAuthResults:].cold.5
- -[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:].cold.1
- -[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:].cold.1
- -[AKAppleIDSession _generateAppleIDHeadersForRequest:error:].cold.1
- -[AKAppleIDSession _generateAppleIDHeadersForRequest:error:].cold.2
- -[AKAppleIDSession _generateAppleIDHeadersForRequest:error:].cold.3
- -[AKAppleIDSession _generateAppleIDHeadersForRequest:error:].cold.4
- -[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:].cold.1
- -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.1
- -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.2
- -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.3
- -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.4
- -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.5
- -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.6
- -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.7
- -[AKAppleIDSession _handleURLSwitchingResponse:forRequest:withCompletion:].cold.1
- -[AKAppleIDSession _handleURLSwitchingResponse:forRequest:withCompletion:].cold.2
- -[AKAppleIDSession appleIDHeadersUsingAnisetteWithCompletion:].cold.1
- -[AKAppleIDSession appleIDHeadersUsingAnisetteWithCompletion:].cold.2
- -[AKAppleIDSession appleIDHeadersWithCompletion:].cold.1
- -[AKAppleIDSession appleIDHeadersWithCompletion:].cold.2
- -[AKAppleIDSession handleResponse:forRequest:shouldRetry:].cold.1
- -[AKAppleIDSession shouldDenyRequestForURL:task:].cold.1
- -[AKAppleIDSession shouldDenyRequestForURL:task:].cold.2
- -[AKAppleIDSession shouldDenyRequestForURL:task:].cold.3
- -[AKAppleIDSigningController _connectionInterrupted].cold.1
- -[AKAppleIDSigningController _connectionInvalidated].cold.1
- -[AKAppleIDSigningController attestationDataForRequest:completion:].cold.1
- -[AKAppleIDSigningController(Convenience) _parseDERCertificatesFromChain:error:].cold.1
- -[AKAppleIDSigningController(Convenience) _parseDERCertificatesFromChain:error:].cold.2
- -[AKAttestationSigner _attestationWithCertificates:error:].cold.1
- -[AKAttestationSigner _signatureForData:withReferenceKey:error:].cold.1
- -[AKAttestationSigner _signatureForData:withReferenceKey:error:].cold.2
- -[AKAttestationSigner signatureForData:options:completion:].cold.1
- -[AKAttestationSigner signaturesForData:options:completion:].cold.1
- -[AKAuthHandlerImpl buildReauthenticationContextFromContext:error:].cold.1
- -[AKAuthorizationAppSignInDiscovery dealloc].cold.1
- -[AKAuthorizationController _allowListDomainsForSharingKey].cold.1
- -[AKAuthorizationController _appleOwnedDomains].cold.1
- -[AKAuthorizationController _nativeTakeoverURLs].cold.1
- -[AKAuthorizationController _sharedKeyInfo].cold.1
- -[AKAuthorizationController dealloc].cold.1
- -[AKAuthorizationCredential initWithServerResponse:].cold.1
- -[AKAuthorizationDaemonConnection _connectionInterruptionHandler].cold.1
- -[AKAuthorizationDaemonConnection _connectionInvalidationHandler].cold.1
- -[AKAuthorizationDaemonConnection dealloc].cold.1
- -[AKAuthorizationPresentationContext _addPresenterParameters].cold.1
- -[AKBaseDaemonConnection _connectionInterruptionHandler].cold.1
- -[AKBaseDaemonConnection _connectionInvalidationHandler].cold.1
- -[AKBaseDaemonConnection dealloc].cold.1
- -[AKBaseFollowupManager synchronizeFollowUpsWithServerPayload:altDSID:error:].cold.1
- -[AKBaseFollowupManager teardownFollowUpWithContext:completion:].cold.1
- -[AKBiometricRatchetController armWithContext:completion:].cold.1
- -[AKBiometricRatchetController armWithContext:completion:].cold.2
- -[AKBiometricRatchetController currentRachetState].cold.1
- -[AKBiometricRatchetController currentRachetState].cold.2
- -[AKBiometricRatchetController isDTOEnabled].cold.1
- -[AKCDPFactory isManateeAvailable].cold.1
- -[AKCarrierBundleUtilities phoneBundleInfoWithAdditionalInfo:error:].cold.1
- -[AKCommandLineURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:].cold.1
- -[AKCommandLineURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:].cold.2
- -[AKCommandLineUtilities _hostURL].cold.1
- -[AKCommandLineUtilities errorFromServerResponseBody:].cold.1
- -[AKCommandLineUtilities errorFromServerResponseBody:].cold.2
- -[AKCommandLineUtilities errorFromServerResponseBody:].cold.3
- -[AKCommandLineUtilities mutableJSONRequestForURL:].cold.1
- -[AKCompanionKeyEnvelope initWithCoder:].cold.1
- -[AKConfiguration configurationValueForKey:useDomain:].cold.1
- -[AKConfiguration setConfigurationValue:forKey:].cold.1
- -[AKConfiguration setDomainConfigurationValue:forKey:].cold.1
- -[AKCoordinatedDataBlock start].cold.1
- -[AKCustodianController dealloc].cold.1
- -[AKCustodianDaemonConnection _connectionInterruptionHandler].cold.1
- -[AKCustodianDaemonConnection _connectionInvalidationHandler].cold.1
- -[AKCustodianDaemonConnection dealloc].cold.1
- -[AKDevice isBiometricAuthCapable].cold.1
- -[AKDevice isBiometricAuthCapable].cold.2
- -[AKDevice isInCircle].cold.1
- -[AKDevice isInternalBuild].cold.1
- -[AKDevice isMultiUserMode].cold.1
- -[AKDevice isProtectedWithPasscode].cold.1
- -[AKDevice isSeedBuild].cold.1
- -[AKDevice isStrongDeviceIdentitySupported].cold.1
- -[AKDevice isVirtualMachine].cold.1
- -[AKDevice phoneNumber].cold.1
- -[AKDevice serializedData].cold.1
- -[AKDeviceListDeltaMessagePayload _operationFromPayloadValue:].cold.1
- -[AKDeviceListDeltaMessagePayload _operationFromPayloadValue:].cold.2
- -[AKDeviceListResponse updateWithDeviceRestrictionState:].cold.1
- -[AKDeviceSafetyRestrictionState initWithResponse:error:].cold.1
- -[AKDeviceSafetyRestrictionState initWithResponse:error:].cold.2
- -[AKDictionaryBackedModel initWithValues:].cold.1
- -[AKDictionaryBackedModel objectForKey:].cold.1
- -[AKFeatureManager init].cold.1
- -[AKFeatureManager init].cold.10
- -[AKFeatureManager init].cold.11
- -[AKFeatureManager init].cold.12
- -[AKFeatureManager init].cold.13
- -[AKFeatureManager init].cold.14
- -[AKFeatureManager init].cold.15
- -[AKFeatureManager init].cold.16
- -[AKFeatureManager init].cold.17
- -[AKFeatureManager init].cold.18
- -[AKFeatureManager init].cold.19
- -[AKFeatureManager init].cold.2
- -[AKFeatureManager init].cold.20
- -[AKFeatureManager init].cold.21
- -[AKFeatureManager init].cold.22
- -[AKFeatureManager init].cold.23
- -[AKFeatureManager init].cold.24
- -[AKFeatureManager init].cold.25
- -[AKFeatureManager init].cold.26
- -[AKFeatureManager init].cold.27
- -[AKFeatureManager init].cold.28
- -[AKFeatureManager init].cold.29
- -[AKFeatureManager init].cold.3
- -[AKFeatureManager init].cold.30
- -[AKFeatureManager init].cold.31
- -[AKFeatureManager init].cold.32
- -[AKFeatureManager init].cold.33
- -[AKFeatureManager init].cold.34
- -[AKFeatureManager init].cold.4
- -[AKFeatureManager init].cold.5
- -[AKFeatureManager init].cold.6
- -[AKFeatureManager init].cold.7
- -[AKFeatureManager init].cold.8
- -[AKFeatureManager init].cold.9
- -[AKFidoAuthorizationController _populateCustomStringsFromContext:].cold.1
- -[AKFidoAuthorizationController _requestFromContext:].cold.1
- -[AKFidoAuthorizationController authorizationController:didCompleteWithAuthorization:].cold.1
- -[AKFidoAuthorizationController authorizationController:didCompleteWithAuthorization:].cold.2
- -[AKFidoAuthorizationController authorizationController:didCompleteWithAuthorization:].cold.3
- -[AKFidoAuthorizationController authorizationController:didCompleteWithAuthorization:].cold.4
- -[AKFidoAuthorizationController authorizationController:didCompleteWithError:].cold.1
- -[AKFollowUpFactoryImpl _extensionIDFromPayload:].cold.1
- -[AKFollowUpFactoryImpl _itemFromPayload:pushMessageInfo:withAltDSID:].cold.1
- -[AKFollowUpFactoryImpl _itemFromPayload:pushMessageInfo:withAltDSID:].cold.2
- -[AKFollowUpFactoryImpl _itemFromPayload:pushMessageInfo:withAltDSID:].cold.3
- -[AKFollowUpFactoryImpl _notificationFromPayload:pushMessageInfo:].cold.1
- -[AKFollowUpFactoryImpl _notificationFromPayload:pushMessageInfo:].cold.2
- -[AKFollowUpFactoryImpl _notificationFromPayload:pushMessageInfo:].cold.3
- -[AKFollowUpSynchronizer shouldSynchronizeForAccount:].cold.1
- -[AKFollowUpSynchronizer synchronizeFollowUpsForAccount:error:].cold.1
- -[AKFollowUpSynchronizer synchronizeFollowUpsForAccount:inStore:error:].cold.1
- -[AKInheritanceController _setupBeneficiaryAliasWithInheritanceContext:completion:].cold.1
- -[AKLiveValue _onqueue_updateValue].cold.1
- -[AKLoginPresenter authenticationRequestFinishedWithResults:password:additionalData:error:].cold.1
- -[AKLoginPresenter presentOOPLoginUIWithContext:completion:].cold.1
- -[AKLoginPresenter presentOOPLoginUIWithContext:completion:].cold.2
- -[AKLoginPresenter presentOOPLoginUIWithContext:completion:].cold.3
- -[AKLoginPresenter presentOOPLoginUIWithContext:completion:].cold.4
- -[AKMasterToken externalizedVersion].cold.1
- -[AKMasterToken updateWithHTTPURLResponse:].cold.1
- -[AKMasterToken updateWithHTTPURLResponse:].cold.2
- -[AKMasterToken updateWithHTTPURLResponse:].cold.3
- -[AKMediaServicesController cancelAppIconRequestForBundleID:completion:].cold.1
- -[AKNativeAccountRecoveryController _mapICSCRecoveryResultsToAuthKit:].cold.1
- -[AKNativeAccountRecoveryController _mapICSCRecoveryResultsToAuthKit:].cold.2
- -[AKNativeAccountRecoveryController presentNativeRecoveryUIWithCompletion:].cold.1
- -[AKNativeAccountRecoveryController presentNativeRecoveryUIWithCompletion:].cold.2
- -[AKPrivateEmailClientImpl presentPrivateEmailUIForContext:completion:].cold.1
- -[AKServerBackoffController reportTelemetryForContext:backoffType:].cold.1
- -[AKServerBackoffHelper isBackoffSupported].cold.1
- -[AKSignInWithAppleController remoteServiceDidInterrupt].cold.1
- -[AKSignInWithAppleController remoteServiceDidInvalidate].cold.1
- -[AKSymmetricKeyDaemonConnection _connectionInterruptionHandler].cold.1
- -[AKSymmetricKeyDaemonConnection _connectionInvalidationHandler].cold.1
- -[AKSymmetricKeyDaemonConnection dealloc].cold.1
- -[AKURLConfiguration initWithDictionary:device:].cold.1
- -[AKURLDataTask _completeWithError:].cold.1
- -[AKURLSession URLSession:dataTask:didReceiveData:].cold.1
- -[AKURLSession URLSession:dataTask:didReceiveData:].cold.2
- -[AKURLSession URLSession:didBecomeInvalidWithError:].cold.1
- -[AKURLSession URLSession:didReceiveChallenge:completionHandler:].cold.1
- -[AKURLSession _unsafe_retryTaskIfPossible:].cold.1
- -[AKURLSession _unsafe_retryTaskIfPossible:].cold.2
- -[AKURLSession _unsafe_retryTaskIfPossible:].cold.3
- -[AKURLSession beginDataTaskWithRequest:completionHandler:].cold.1
- -[AKURLSession init].cold.1
- -[AKUserInformation _parseBeneficiaryInfo:].cold.1
- -[AKUserInformation _parseBeneficiaryInfo:].cold.2
- -[AKUserInformation _parseBeneficiaryInfo:].cold.3
- -[AKUserInformation _parseCustodianInfo:].cold.1
- -[AKUserInformation _parseCustodianInfo:].cold.2
- -[AKUserInformation _parseCustodianInfo:].cold.3
- -[AKUserInformation criticalAccountEditsAllowed].cold.1
- -[AKUserInformation initWithResponseBody:].cold.1
- -[AKUserInformation initWithResponseBody:].cold.10
- -[AKUserInformation initWithResponseBody:].cold.11
- -[AKUserInformation initWithResponseBody:].cold.12
- -[AKUserInformation initWithResponseBody:].cold.13
- -[AKUserInformation initWithResponseBody:].cold.14
- -[AKUserInformation initWithResponseBody:].cold.15
- -[AKUserInformation initWithResponseBody:].cold.16
- -[AKUserInformation initWithResponseBody:].cold.17
- -[AKUserInformation initWithResponseBody:].cold.18
- -[AKUserInformation initWithResponseBody:].cold.19
- -[AKUserInformation initWithResponseBody:].cold.2
- -[AKUserInformation initWithResponseBody:].cold.20
- -[AKUserInformation initWithResponseBody:].cold.21
- -[AKUserInformation initWithResponseBody:].cold.22
- -[AKUserInformation initWithResponseBody:].cold.23
- -[AKUserInformation initWithResponseBody:].cold.24
- -[AKUserInformation initWithResponseBody:].cold.25
- -[AKUserInformation initWithResponseBody:].cold.26
- -[AKUserInformation initWithResponseBody:].cold.27
- -[AKUserInformation initWithResponseBody:].cold.28
- -[AKUserInformation initWithResponseBody:].cold.29
- -[AKUserInformation initWithResponseBody:].cold.3
- -[AKUserInformation initWithResponseBody:].cold.30
- -[AKUserInformation initWithResponseBody:].cold.31
- -[AKUserInformation initWithResponseBody:].cold.32
- -[AKUserInformation initWithResponseBody:].cold.33
- -[AKUserInformation initWithResponseBody:].cold.34
- -[AKUserInformation initWithResponseBody:].cold.35
- -[AKUserInformation initWithResponseBody:].cold.36
- -[AKUserInformation initWithResponseBody:].cold.37
- -[AKUserInformation initWithResponseBody:].cold.38
- -[AKUserInformation initWithResponseBody:].cold.39
- -[AKUserInformation initWithResponseBody:].cold.4
- -[AKUserInformation initWithResponseBody:].cold.40
- -[AKUserInformation initWithResponseBody:].cold.41
- -[AKUserInformation initWithResponseBody:].cold.42
- -[AKUserInformation initWithResponseBody:].cold.43
- -[AKUserInformation initWithResponseBody:].cold.44
- -[AKUserInformation initWithResponseBody:].cold.45
- -[AKUserInformation initWithResponseBody:].cold.5
- -[AKUserInformation initWithResponseBody:].cold.6
- -[AKUserInformation initWithResponseBody:].cold.7
- -[AKUserInformation initWithResponseBody:].cold.8
- -[AKUserInformation initWithResponseBody:].cold.9
- -[AKWalrusConfigProvider _extractWalrusConfigWithAccountCountry:fromGlobalConfig:].cold.1
- -[AKWalrusConfigProvider _extractWalrusConfigWithAccountCountry:fromGlobalConfig:].cold.2
- -[AKWalrusConfigProvider getWalrusConfigWithCompletion:].cold.1
- -[NSDictionary(AuthKit) hasValueAtKey:ofType:].cold.1
- -[NSDictionary(AuthKit) hasValueAtKey:ofType:].cold.2
- -[NSMutableURLRequest(AuthKit) ak_addAttestationDataHeaders].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addBiometryTypeHeaderWithValue:].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addCreateInformationHeaderWithValue:].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addExecutionModeHeader:].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addExperimentModeHeader].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addLoggedInServicesHeaderForServices:].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addPhoneInformationHeaderWithValue:].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addPhoneNumberHeader].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addProxiedAttestationHeaders:].cold.1
- -[NSMutableURLRequest(AuthKit) ak_addWalrusStatusHeader].cold.1
- -[NSMutableURLRequest(AuthKit) ak_setBodyWithParameters:].cold.1
- -[NSMutableURLRequest(AuthKit) ak_setJSONBodyWithParameters:].cold.1
- -[NSMutableURLRequest(AuthKit) ak_setJSONBodyWithParameters:].cold.2
- -[NSString(AuthKit) ak_safeBase64String].cold.1
- -[_AKAnisetteProviderProxy eraseAnisetteForContext:withCompletion:].cold.1
- -[_AKAnisetteProviderProxy fetchAnisetteDataForContext:provisionIfNecessary:withCompletion:].cold.1
- -[_AKAnisetteProviderProxy fetchPeerAttestationDataForContext:withRequest:completion:].cold.1
- -[_AKAnisetteProviderProxy legacyAnisetteDataForContext:DSID:withCompletion:].cold.1
- -[_AKAnisetteProviderProxy provisionAnisetteForContext:withCompletion:].cold.1
- -[_AKAnisetteProviderProxy syncAnisetteForContext:withSIMData:completion:].cold.1
- GCC_except_table104
- GCC_except_table108
- GCC_except_table134
- GCC_except_table137
- GCC_except_table140
- GCC_except_table145
- GCC_except_table148
- GCC_except_table152
- GCC_except_table159
- GCC_except_table160
- GCC_except_table165
- GCC_except_table166
- GCC_except_table169
- GCC_except_table175
- GCC_except_table179
- GCC_except_table182
- GCC_except_table183
- GCC_except_table184
- GCC_except_table186
- GCC_except_table189
- GCC_except_table190
- GCC_except_table192
- GCC_except_table193
- GCC_except_table201
- GCC_except_table217
- GCC_except_table220
- GCC_except_table222
- GCC_except_table223
- GCC_except_table224
- GCC_except_table226
- GCC_except_table228
- GCC_except_table229
- GCC_except_table230
- GCC_except_table231
- GCC_except_table232
- GCC_except_table233
- GCC_except_table234
- GCC_except_table238
- GCC_except_table240
- GCC_except_table260
- GCC_except_table261
- GCC_except_table277
- GCC_except_table291
- GCC_except_table292
- GCC_except_table293
- GCC_except_table294
- GCC_except_table295
- GCC_except_table296
- GCC_except_table297
- GCC_except_table298
- GCC_except_table299
- GCC_except_table300
- GCC_except_table301
- GCC_except_table302
- GCC_except_table330
- GCC_except_table373
- GCC_except_table45
- GCC_except_table93
- GCC_except_table95
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- _SDeviceIdentityIsSupported.cold.1
- _SDeviceIdentityIssueClientCertificateWithCompletion.cold.1
- _SMAEGetActivationStateWithError.cold.1
- __AKAttestationOptionsFromOptions.cold.1
- __AKAttestationOptionsFromOptions.cold.2
- __AKAttestationOptionsFromOptions.cold.3
- __AKAttestationOptionsFromOptions.cold.4
- __AKAttestationOptionsFromOptions.cold.5
- __AKAttestationOptionsFromOptions.cold.6
- __AKLocalizedString.cold.1
- __AKLogFido.cold.1
- __AKLogHme.cold.1
- __AKLogNto.cold.1
- __AKLogPasskey.cold.1
- __AKLogSiwa.cold.1
- __AKLogSystem.cold.1
- __AKLogSystemQuery.cold.1
- __AKLogUserInteraction.cold.1
- __AKSignpostGetNanoseconds.cold.1
- __AKSignpostLogSystem.cold.1
- __AKTrafficLogSubsystem.cold.1
- __AKTriageLogSystem.cold.1
- __ASAuthorizationAllSupportedPublicKeyCredentialDescriptorTransports.cold.1
- __BYSetupAssistantNeedsToRun.cold.1
- ___100-[AKAppleIDPasskeyAuthenticationController canCreateiCloudKeychainPasskeyForAccount:withCompletion:]_block_invoke.50.cold.1
- ___100-[AKAppleIDPasskeyAuthenticationController canCreateiCloudKeychainPasskeyForAccount:withCompletion:]_block_invoke.50.cold.2
- ___100-[AKAppleIDPasskeyAuthenticationController canCreateiCloudKeychainPasskeyForAccount:withCompletion:]_block_invoke.cold.1
- ___100-[AKAppleIDPasskeyAuthenticationController canCreateiCloudKeychainPasskeyForAccount:withCompletion:]_block_invoke.cold.2
- ___100-[AKAppleIDPasskeyAuthenticationController canCreateiCloudKeychainPasskeyForAccount:withCompletion:]_block_invoke.cold.3
- ___100-[AKAuthorizationController performAuthorizationWithContext:withUserProvidedInformation:completion:]_block_invoke.cold.1
- ___102-[AKAppleIDSigningController(Convenience) _additionalAttestationHeadersForRequest:options:completion:]_block_invoke.cold.1
- ___102-[AKAppleIDSigningController(Convenience) _additionalAttestationHeadersForRequest:options:completion:]_block_invoke.cold.2
- ___102-[AKAppleIDSigningController(Convenience) _additionalAttestationHeadersForRequest:options:completion:]_block_invoke.cold.3
- ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.80.cold.1
- ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.81.cold.1
- ___105+[AKNativeAccountRecoveryController requestForRecoveryCompletionWithContext:recoveredInfo:recoveryError:]_block_invoke.cold.1
- ___105-[AKAccountRecoveryStepiCloudSecurityCode cdpContext:promptForRecoveryKeyWithSecretValidator:completion:]_block_invoke.cold.1
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke_2.cold.1
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke_2.cold.1
- ___109-[AKAccountRecoveryStepiCloudSecurityCode cdpRecoveryFlowContext:promptForRemoteSecretWithDevices:validator:]_block_invoke.cold.1
- ___109-[AKAccountRecoveryStepiCloudSecurityCode cdpRecoveryFlowContext:promptForRemoteSecretWithDevices:validator:]_block_invoke.cold.2
- ___120-[AKAccountRecoveryStepiCloudSecurityCode cdpContext:promptForRemoteSecretWithDevices:offeringRemoteApproval:validator:]_block_invoke.cold.1
- ___120-[AKAccountRecoveryStepiCloudSecurityCode cdpContext:promptForRemoteSecretWithDevices:offeringRemoteApproval:validator:]_block_invoke.cold.2
- ___134-[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:]_block_invoke.137.cold.1
- ___134-[AKAppleIDAuthenticationCommandLineContext _handleServerUISMSVerificationWithResponseDictionary:statusCode:configuration:completion:]_block_invoke.cold.1
- ___23-[AKConfiguration init]_block_invoke.cold.1
- ___28+[AKURLSession _urlBagCache]_block_invoke.cold.1
- ___30+[AKDevice systemContainerURL]_block_invoke.cold.1
- ___30+[AKDevice systemContainerURL]_block_invoke.cold.2
- ___31-[AKURLSession cancelDataTask:]_block_invoke.cold.1
- ___33-[AKIORegistryReader sfrManifest]_block_invoke.cold.1
- ___33-[AKIORegistryReader sfrManifest]_block_invoke.cold.2
- ___33-[AKIORegistryReader sfrManifest]_block_invoke.cold.3
- ___37+[AKCDPFactory walrusStatusLiveValue]_block_invoke.cold.1
- ___40+[AKCDPFactory webAccessStatusLiveValue]_block_invoke.cold.1
- ___41-[AKAccountManager servicesUsingAccount:]_block_invoke.cold.1
- ___43-[AKAuthorizationController _sharedKeyInfo]_block_invoke.53.cold.1
- ___43-[AKAuthorizationController _sharedKeyInfo]_block_invoke.cold.1
- ___43-[AKUserInformation _parseBeneficiaryInfo:]_block_invoke.cold.1
- ___45-[AKCarouselAlertClientConnection connection]_block_invoke.cold.1
- ___45-[AKCarouselAlertClientConnection connection]_block_invoke_2.cold.1
- ___47-[AKAccountManager setAccount:inUse:byService:]_block_invoke.cold.1
- ___47-[AKAuthorizationController _appleOwnedDomains]_block_invoke.25.cold.1
- ___47-[AKAuthorizationController _appleOwnedDomains]_block_invoke.cold.1
- ___47-[AKFollowUpController addFollowUpItems:error:]_block_invoke
- ___48-[AKAuthorizationController _nativeTakeoverURLs]_block_invoke.20.cold.1
- ___48-[AKAuthorizationController _nativeTakeoverURLs]_block_invoke.cold.1
- ___48-[AKCarouselAlertClientConnection dismissAlert:]_block_invoke_2.cold.1
- ___49-[AKAccountManager accountTypeForTypeIdentifier:]_block_invoke.cold.1
- ___50-[AKFollowUpController removeFollowUpItems:error:]_block_invoke
- ___52-[AKAccountManager _fetchAllAccountsWithType:error:]_block_invoke.cold.1
- ___52-[AKAccountManager _fetchAllAccountsWithType:error:]_block_invoke.cold.2
- ___52-[AKBiometricRatchetController stateWithCompletion:]_block_invoke.cold.1
- ___53-[AKFidoAuthorizationController _requestFromContext:]_block_invoke.cold.1
- ___53-[AKFidoAuthorizationController _requestFromContext:]_block_invoke.cold.2
- ___53-[AKFidoAuthorizationController _requestFromContext:]_block_invoke.cold.3
- ___55-[AKServerBackoffController configureFromHeaderFields:]_block_invoke.cold.1
- ___56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.15.cold.1
- ___56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.16.cold.1
- ___56-[AKAnisetteProvisioningController eraseWithCompletion:]_block_invoke.16.cold.2
- ___57+[AKURLSession sharedURLSessionWithDenyVirtualInterfaces]_block_invoke.cold.1
- ___57+[AKURLSession sharedURLSessionWithDenyVirtualInterfaces]_block_invoke.cold.2
- ___57+[AKURLSession sharedURLSessionWithDenyVirtualInterfaces]_block_invoke.cold.3
- ___57-[AKDeviceListResponse updateWithDeviceRestrictionState:]_block_invoke.cold.1
- ___57-[AKDeviceListResponse updateWithDeviceRestrictionState:]_block_invoke.cold.2
- ___57-[AKFidoAuthorizationController _authRequestFromContext:]_block_invoke.cold.1
- ___57-[AKFidoAuthorizationController _authRequestFromContext:]_block_invoke.cold.2
- ___57-[AKFidoAuthorizationController _authRequestFromContext:]_block_invoke.cold.3
- ___59-[AKAlertHandler _showAlertForPasscodeSetupWithCompletion:]_block_invoke_2.cold.1
- ___59-[AKAppleIDAuthenticationContextManager unregisterContext:]_block_invoke.cold.1
- ___59-[AKAttestationSigner signatureForData:options:completion:]_block_invoke.cold.1
- ___59-[AKAttestationSigner signatureForData:options:completion:]_block_invoke.cold.2
- ___59-[AKAuthorizationController _allowListDomainsForSharingKey]_block_invoke.28.cold.1
- ___59-[AKAuthorizationController _allowListDomainsForSharingKey]_block_invoke.cold.1
- ___60-[AKAgeRangeSettingsProvider refreshAgeRangeWithCompletion:]_block_invoke.cold.1
- ___60-[AKAgeRangeSettingsProvider refreshAgeRangeWithCompletion:]_block_invoke.cold.2
- ___60-[AKAlertHandler _showAlertForInvalidContextWithCompletion:]_block_invoke.46.cold.1
- ___60-[AKAlertHandler _showAlertForInvalidContextWithCompletion:]_block_invoke.cold.1
- ___60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.6.cold.1
- ___60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.8.cold.1
- ___60-[AKAnisetteProvisioningController provisionWithCompletion:]_block_invoke.8.cold.2
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.343.cold.1
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.343.cold.2
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.cold.1
- ___60-[AKAttestationSigner signaturesForData:options:completion:]_block_invoke.31.cold.1
- ___60-[AKAttestationSigner signaturesForData:options:completion:]_block_invoke.cold.1
- ___60-[AKAttestationSigner signaturesForData:options:completion:]_block_invoke.cold.2
- ___60-[AKLoginPresenter presentOOPLoginUIWithContext:completion:]_block_invoke.cold.1
- ___60-[AKLoginPresenter presentOOPLoginUIWithContext:completion:]_block_invoke.cold.2
- ___61-[AKAlertHandler _showAlertForUnverifiedEmailWithCompletion:]_block_invoke_2.cold.1
- ___61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke.cold.1
- ___61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke.cold.2
- ___61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke_2.5.cold.1
- ___61-[AKClientConnectionLifecycleManager activeServiceConnection]_block_invoke_2.cold.1
- ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.116.cold.1
- ___62-[AKAlertHandler _showAlertForCannotFindServerWithCompletion:]_block_invoke_2.cold.1
- ___62-[AKAlertHandler _showAlertForUnderageAccount:withCompletion:]_block_invoke_2.cold.1
- ___62-[AKAppleIDAuthenticationContext _handleSecondFactorCodeEntry]_block_invoke.cold.1
- ___62-[AKAppleIDAuthenticationContext _handleSecondFactorCodeEntry]_block_invoke.cold.2
- ___62-[AKAppleIDAuthenticationContext _handleSecondFactorCodeEntry]_block_invoke.cold.3
- ___62-[AKAppleIDSession _reportOnRequest:response:attestationData:]_block_invoke.cold.1
- ___63-[AKAbsintheSigner _createSigningContextWithCompletionHandler:]_block_invoke.10.cold.1
- ___63-[AKAbsintheSigner _createSigningContextWithCompletionHandler:]_block_invoke.cold.1
- ___63-[AKAbsintheSigner _createSigningContextWithCompletionHandler:]_block_invoke.cold.2
- ___63-[AKAbsintheSigner _createSigningContextWithCompletionHandler:]_block_invoke.cold.3
- ___63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.13.cold.1
- ___63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke.13.cold.2
- ___63-[AKAnisetteProvisioningController syncWithSIMData:completion:]_block_invoke_2.cold.1
- ___63-[AKClientConnectionLifecycleManager teardownServiceConnection]_block_invoke.cold.1
- ___63-[AKCustodianController revokeCustodianWithContext:completion:]_block_invoke.6.cold.1
- ___63-[AKCustodianController revokeCustodianWithContext:completion:]_block_invoke_2.cold.1
- ___63-[AKSignInWithAppleController fetchEULAForClientID:completion:]_block_invoke.cold.1
- ___63-[AKWalrusController removeAllPCSAuthCredentialWithCompletion:]_block_invoke_2.cold.1
- ___64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.50.cold.1
- ___64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.50.cold.2
- ___64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.cold.1
- ___64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.cold.2
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.42.cold.1
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.42.cold.2
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.42.cold.3
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.42.cold.4
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.42.cold.5
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.36.cold.1
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.36.cold.2
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.36.cold.3
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.36.cold.4
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.36.cold.5
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.cold.1
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.cold.2
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.cold.3
- ___64-[AKSignInWithAppleController leaveGroupWithContext:completion:]_block_invoke.cold.1
- ___65-[AKAlertHandler _showAlertForAccountNotSupportedWithCompletion:]_block_invoke_2.cold.1
- ___65-[AKAlertHandler _showAlertForMissingAppleAccountWithCompletion:]_block_invoke_2.cold.1
- ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke_2.cold.1
- ___66+[AKFollowUpSynchronizer updateSynchronizeTimeForAccount:inStore:]_block_invoke.cold.1
- ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.cold.1
- ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke.103.cold.1
- ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke.103.cold.2
- ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke_2.cold.1
- ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.115.cold.1
- ___67-[AKAlertHandler _showAlertForManagedAccount:error:withCompletion:]_block_invoke_2.cold.1
- ___67-[AKAppleIDSigningController attestationDataForRequest:completion:]_block_invoke.cold.1
- ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke.105.cold.1
- ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke.105.cold.2
- ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke_2.cold.1
- ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.111.cold.1
- ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.cold.1
- ___67-[AKSignInWithAppleController fetchAccountsWithContext:completion:]_block_invoke.cold.1
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.302.cold.1
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.303.cold.1
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.303.cold.2
- ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.109.cold.1
- ___68-[AKSignInWithAppleController revokeAcccountWithContext:completion:]_block_invoke.cold.1
- ___68-[AKSignInWithAppleController unshareAccountWithContext:completion:]_block_invoke.cold.1
- ___69-[AKAppleIDAuthenticationController clearSessionCacheWithCompletion:]_block_invoke_2.cold.1
- ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke_2.cold.1
- ___69-[AKAuthorizationController getCredentialStateForRequest:completion:]_block_invoke.cold.1
- ___69-[AKAuthorizationController getCredentialStateForRequest:completion:]_block_invoke.cold.2
- ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.113.cold.1
- ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.104.cold.1
- ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.33.cold.1
- ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.33.cold.2
- ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke_2.cold.1
- ___70-[AKAppleIDAuthenticationController deviceListWithContext:completion:]_block_invoke.cold.1
- ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke_2.cold.1
- ___70-[AKAuthorizationController beginAuthorizationWithContext:completion:]_block_invoke.cold.1
- ___70-[AKAuthorizationController getCredentialStateForClientID:completion:]_block_invoke.cold.1
- ___70-[AKAuthorizationController getCredentialStateForClientID:completion:]_block_invoke.cold.2
- ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.4.cold.1
- ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.5.cold.1
- ___70-[AKCustodianController initiateCustodianSetupWithContext:completion:]_block_invoke.1.cold.1
- ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.118.cold.1
- ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.78.cold.1
- ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.79.cold.1
- ___71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke_2.cold.1
- ___71-[AKAuthorizationController cancelAuthorizationWithContext:completion:]_block_invoke.cold.1
- ___71-[AKAuthorizationController revokeAuthorizationWithContext:completion:]_block_invoke.cold.1
- ___71-[AKBaseFollowupManager _alignedInsertionCandidates:withExistingItems:]_block_invoke.24.cold.1
- ___71-[AKBaseFollowupManager _alignedInsertionCandidates:withExistingItems:]_block_invoke.24.cold.2
- ___71-[AKBaseFollowupManager _alignedInsertionCandidates:withExistingItems:]_block_invoke.24.cold.3
- ___71-[AKBaseFollowupManager _alignedInsertionCandidates:withExistingItems:]_block_invoke.cold.1
- ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.108.cold.1
- ___71-[AKSignInWithAppleController fetchSharedGroupsWithContext:completion:]_block_invoke.cold.1
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.36.cold.1
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.36.cold.2
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke_2.cold.1
- ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.cold.1
- ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.264.cold.1
- ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke_2.cold.1
- ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.cold.1
- ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.332.cold.1
- ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke_2.cold.1
- ___72-[AKAppleIDPasskeyController setupAppleIDPasskeyWithContext:completion:]_block_invoke.cold.1
- ___72-[AKAuthorizationController performAuthorizationWithContext:completion:]_block_invoke.cold.1
- ___72-[AKSignInWithAppleController performHealthCheckWithContext:completion:]_block_invoke.cold.1
- ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.28.cold.1
- ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.28.cold.2
- ___73-[AKAnisetteProvisioningController _attestationDataForRequestData:error:]_block_invoke.cold.1
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.352.cold.1
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.cold.1
- ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke_2.cold.1
- ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.cold.1
- ___73-[AKAppleIDPasskeyController appleIDPasskeyStatusWithContext:completion:]_block_invoke.cold.1
- ___73-[AKAppleIDPasskeyController verifyAppleIDPasskeyWithContext:completion:]_block_invoke.cold.1
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.128.cold.1
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.133.cold.1
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.136.cold.1
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.140.cold.1
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.cold.1
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.66.cold.1
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke_2.cold.1
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke_2.cold.2
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78.cold.2
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.80.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.81.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.81.cold.2
- ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke_2.cold.1
- ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke_2.cold.2
- ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke_2.cold.3
- ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke_2.cold.4
- ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke_2.cold.5
- ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke_2.cold.6
- ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke_2.cold.7
- ___73-[AKAuthorizationController continueAuthorizationWithContext:completion:]_block_invoke.cold.1
- ___73-[AKCarouselAlertClientConnection presentAlertWithDictionary:completion:]_block_invoke_2.cold.1
- ___73-[AKURLSession beginAuthenticationDataTaskWithRequest:completionHandler:]_block_invoke.cold.1
- ___73-[AKURLSession beginAuthenticationDataTaskWithRequest:completionHandler:]_block_invoke.cold.2
- ___73-[AKURLSession beginAuthenticationDataTaskWithRequest:completionHandler:]_block_invoke.cold.3
- ___73-[AKURLSession beginAuthenticationDataTaskWithRequest:completionHandler:]_block_invoke.cold.4
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.339.cold.1
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.cold.1
- ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.355.cold.1
- ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.cold.1
- ___74-[AKAppleIDSession _handleURLSwitchingResponse:forRequest:withCompletion:]_block_invoke.cold.1
- ___74-[AKAppleIDSession _handleURLSwitchingResponse:forRequest:withCompletion:]_block_invoke.cold.2
- ___74-[AKCustodianController updateCustodianRecoveryKeyWithContext:completion:]_block_invoke.7.cold.1
- ___74-[AKCustodianController updateCustodianRecoveryKeyWithContext:completion:]_block_invoke_2.cold.1
- ___74-[AKSignInWithAppleController cancelAppIconRequestForClientID:completion:]_block_invoke.cold.1
- ___74-[AKSignInWithAppleController performTokenRotationWithContext:completion:]_block_invoke.cold.1
- ___74-[AKSymmetricKeyController registerForSymmetricKeyWithContext:completion:]_block_invoke.20.cold.1
- ___75-[AKAbsintheSigner _establishSessionWithInfo:sessionURL:completionHandler:]_block_invoke.cold.1
- ___75-[AKAbsintheSigner _establishSessionWithInfo:sessionURL:completionHandler:]_block_invoke.cold.2
- ___75-[AKAbsintheSigner _establishSessionWithInfo:sessionURL:completionHandler:]_block_invoke.cold.3
- ___75-[AKAbsintheSigner _establishSessionWithInfo:sessionURL:completionHandler:]_block_invoke.cold.4
- ___75-[AKAbsintheSigner _establishSessionWithInfo:sessionURL:completionHandler:]_block_invoke.cold.5
- ___75-[AKAbsintheSigner _establishSessionWithInfo:sessionURL:completionHandler:]_block_invoke.cold.6
- ___75-[AKAppleIDPasskeyController unenrollAppleIDPasskeyWithContext:completion:]_block_invoke.cold.1
- ___75-[AKAuthorizationController _nativeTakeoverEndpointsWithCompletionHandler:]_block_invoke.22.cold.1
- ___75-[AKAuthorizationController _nativeTakeoverEndpointsWithCompletionHandler:]_block_invoke.22.cold.2
- ___75-[AKAuthorizationController _nativeTakeoverEndpointsWithCompletionHandler:]_block_invoke.cold.1
- ___75-[AKBiometricRatchetController isCriticalEditAllowedForAltDSID:completion:]_block_invoke.cold.1
- ___75-[AKCustodianController fetchCustodianRecoveryTokenWithContext:completion:]_block_invoke.14.cold.1
- ___75-[AKCustodianController fetchCustodianRecoveryTokenWithContext:completion:]_block_invoke.cold.1
- ___75-[AKNativeAccountRecoveryController presentNativeRecoveryUIWithCompletion:]_block_invoke.cold.1
- ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.106.cold.1
- ___75-[AKSignInWithAppleController fetchAppIconForClientID:iconSize:completion:]_block_invoke.cold.1
- ___76-[AKAccountManager removeContinuationTokenForAccount:telemetryFlowID:error:]_block_invoke.cold.1
- ___76-[AKAppleIDAuthenticationContext isConfiguredForTokenUpgradeWithCompletion:]_block_invoke.cold.1
- ___76-[AKAppleIDAuthenticationContext isConfiguredForTokenUpgradeWithCompletion:]_block_invoke.cold.2
- ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.357.cold.1
- ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.cold.1
- ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.cold.1
- ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.330.cold.1
- ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke_2.cold.1
- ___76-[AKSignInWithAppleController shareAccountWithContext:withGroup:completion:]_block_invoke.cold.1
- ___77-[AKAnisetteProvisioningController attestationDataForRequestData:completion:]_block_invoke.cold.1
- ___77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke.23.cold.1
- ___77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke.23.cold.2
- ___77-[AKAnisetteProvisioningController legacyAnisetteDataForDSID:withCompletion:]_block_invoke_2.cold.1
- ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.cold.1
- ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke_2.cold.1
- ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke_2.cold.1
- ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke_2.cold.1
- ___77-[AKAuthorizationController storeAuthorization:forProxiedRequest:completion:]_block_invoke.cold.1
- ___77-[AKCustodianController fetchCustodianDataRecoveryKeyWithContext:completion:]_block_invoke.15.cold.1
- ___77-[AKCustodianController fetchCustodianDataRecoveryKeyWithContext:completion:]_block_invoke.cold.1
- ___77-[AKCustodianController startCustodianRecoveryRequestWithContext:completion:]_block_invoke.cold.1
- ___77-[AKInheritanceController setupBeneficiaryWithInheritanceContext:completion:]_block_invoke_2.cold.1
- ___78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.cold.1
- ___78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.cold.2
- ___78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.cold.3
- ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke_2.cold.1
- ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.331.cold.1
- ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke_2.cold.1
- ___78-[AKAuthorizationController continueFetchingIconForRequestContext:completion:]_block_invoke.cold.1
- ___78-[AKInheritanceController removeBeneficiaryWithInheritanceContext:completion:]_block_invoke_2.cold.1
- ___78-[AKInheritanceController updateBeneficiaryWithInheritanceContext:completion:]_block_invoke_2.cold.1
- ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.107.cold.1
- ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke_2.cold.1
- ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke_2.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.157.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.162.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.cold.2
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_2.159.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_2.159.cold.2
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_3.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_3.cold.2
- ___79-[AKCustodianController fetchCustodianRecoveryCodeConfigurationWithCompletion:]_block_invoke.cold.1
- ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.34.cold.1
- ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.34.cold.2
- ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke_2.cold.1
- ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke_2.cold.1
- ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.356.cold.1
- ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.cold.1
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.349.cold.1
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.350.cold.1
- ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke_2.cold.1
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.337.cold.1
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke_2.cold.1
- ___80-[AKAuthorizationController getPresentationContextForRequestContext:completion:]_block_invoke.cold.1
- ___81-[AKAnisetteProvisioningController shouldAllowReprovisionForHostName:completion:]_block_invoke.cold.1
- ___81-[AKAnisetteProvisioningController shouldAllowReprovisionForHostName:completion:]_block_invoke.cold.2
- ___81-[AKAnisetteProvisioningController shouldAllowReprovisionForHostName:completion:]_block_invoke.cold.3
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.351.cold.1
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.cold.1
- ___81-[AKCustodianController startCustodianRecoveryTransactionWithContext:completion:]_block_invoke.12.cold.1
- ___81-[AKCustodianController startCustodianRecoveryTransactionWithContext:completion:]_block_invoke.cold.1
- ___81-[AKInheritanceController fetchManifestOptionsWithInheritanceContext:completion:]_block_invoke_2.cold.1
- ___82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.25.cold.1
- ___82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.26.cold.1
- ___82-[AKAnisetteProvisioningController fetchPeerAttestationDataForRequest:completion:]_block_invoke.26.cold.2
- ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.cold.1
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.325.cold.1
- ___82-[AKNativeAccountRecoveryController cdpContext:performSilentRecoveryTokenRenewal:]_block_invoke.cold.1
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.327.cold.1
- ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke_2.cold.1
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.58.cold.1
- ___83-[AKInheritanceController _setupBeneficiaryAliasWithInheritanceContext:completion:]_block_invoke_2.cold.1
- ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.119.cold.1
- ___83-[AKSignInWithAppleController fetchSignInWithApplePrivateEmailCountWithCompletion:]_block_invoke.cold.1
- ___83-[AKWalrusController PCSAuthContextForWebSessionIdentifier:serviceName:completion:]_block_invoke_2.cold.1
- ___84-[AKAlertHandler _showAlertForInsufficientSecurityLevelWithError:completionHandler:]_block_invoke_2.cold.1
- ___84-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:error:]_block_invoke.17.cold.1
- ___84-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:error:]_block_invoke.cold.1
- ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke_2.cold.1
- ___85-[AKAppleIDPasskeyAuthenticationController appleIDPasskeysForAccount:withCompletion:]_block_invoke.61.cold.1
- ___85-[AKAppleIDPasskeyAuthenticationController appleIDPasskeysForAccount:withCompletion:]_block_invoke.61.cold.2
- ___85-[AKAppleIDPasskeyAuthenticationController appleIDPasskeysForAccount:withCompletion:]_block_invoke.cold.1
- ___85-[AKAppleIDPasskeyAuthenticationController appleIDPasskeysForAccount:withCompletion:]_block_invoke.cold.2
- ___85-[AKAppleIDPasskeyAuthenticationController appleIDPasskeysForAccount:withCompletion:]_block_invoke.cold.3
- ___85-[AKAuthorizationController fetchAppleIDAuthorizeHTMLResponseTemplateWithCompletion:]_block_invoke.cold.1
- ___85-[AKSignInWithAppleController deleteAllItemsFromDepartedGroupWithContext:completion:]_block_invoke.cold.1
- ___86-[AKAuthorizationController primaryApplicationInformationForWebServiceWithInfo:error:]_block_invoke.cold.1
- ___86-[AKSignInWithAppleController participantRemovedWithContext:participantID:completion:]_block_invoke.cold.1
- ___87-[AKAppleIDPasskeyAuthenticationController deleteAllPasskeysForAccount:withCompletion:]_block_invoke.67.cold.1
- ___87-[AKAppleIDPasskeyAuthenticationController deleteAllPasskeysForAccount:withCompletion:]_block_invoke.67.cold.2
- ___87-[AKAppleIDPasskeyAuthenticationController deleteAllPasskeysForAccount:withCompletion:]_block_invoke.cold.1
- ___87-[AKAppleIDPasskeyAuthenticationController deleteAllPasskeysForAccount:withCompletion:]_block_invoke.cold.2
- ___87-[AKAppleIDPasskeyAuthenticationController deleteAllPasskeysForAccount:withCompletion:]_block_invoke.cold.3
- ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.353.cold.1
- ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.cold.1
- ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.cold.1
- ___89-[AKCustodianController sendEmbargoEndNotificationFeedbackWithContext:urlKey:completion:]_block_invoke.16.cold.1
- ___89-[AKCustodianController sendEmbargoEndNotificationFeedbackWithContext:urlKey:completion:]_block_invoke.cold.1
- ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke_2.cold.1
- ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke_2.cold.1
- ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.318.cold.1
- ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke_2.cold.1
- ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.334.cold.1
- ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke_2.cold.1
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.85.cold.1
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.85.cold.2
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.cold.1
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.cold.2
- ___91-[AKAppleIDSigningController(Convenience) _additionalAbsintheHeadersForRequest:completion:]_block_invoke.cold.1
- ___91-[AKAppleIDSigningController(Convenience) _additionalAbsintheHeadersForRequest:completion:]_block_invoke.cold.2
- ___91-[AKAppleIDSigningController(Convenience) _additionalAbsintheHeadersForRequest:completion:]_block_invoke.cold.3
- ___91-[AKAuthorizationController establishConnectionWithNotificationHandlerEndpoint:completion:]_block_invoke.cold.1
- ___92-[AKAnisetteProvisioningController fetchAnisetteDataAndProvisionIfNecessary:withCompletion:]_block_invoke.cold.1
- ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke_2.cold.1
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.54.cold.1
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke_2.cold.1
- ___93-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:withCompletion:]_block_invoke.cold.1
- ___93-[AKAnisetteProvisioningController _fetchAnisetteDataAndProvisionIfNecessary:withCompletion:]_block_invoke.cold.2
- ___93-[AKAuthorizationController establishConnectionWithStateBroadcastHandlerEndpoint:completion:]_block_invoke.cold.1
- ___94-[AKAccountRecoveryStepiCloudSecurityCode _verifyRemoteSecretWithServerInfo:model:completion:]_block_invoke.cold.1
- ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke_2.cold.1
- ___96-[AKAppleIDAuthenticationCommandLineContext _beginDataTaskWithRequest:configuration:completion:]_block_invoke.155.cold.1
- ___96-[AKAppleIDAuthenticationCommandLineContext _beginDataTaskWithRequest:configuration:completion:]_block_invoke.cold.1
- ___96-[AKAppleIDAuthenticationController updateUserInformationForAltDSID:userInformation:completion:]_block_invoke_2.cold.1
- ___97-[AKAccountRecoveryStepChangePassword _verifyNewPasswordWithRowID:confirmRowID:model:completion:]_block_invoke.cold.1
- ___97-[AKAccountRecoveryStepiCloudSecurityCode cdpContext:presentRecoveryKeyWithValidator:completion:]_block_invoke.cold.1
- ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.317.cold.1
- ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke_2.cold.1
- ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.354.cold.1
- ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.cold.1
- ___99-[AKAccountRecoveryStepiCloudSecurityCode cdpContext:promptForRecoveryKeyWithValidator:completion:]_block_invoke.cold.1
- ___AKUnregisterAllAppleIDs_block_invoke.cold.1
- ___block_descriptor_48_e8_32s40r_e31_v32?0"FLFollowUpItem"8Q16^B24ls32l8r40l8
- ___getAAFPhoneNumberFormatterClass_block_invoke.cold.1
- ___getASAuthorizationControllerClass_block_invoke.cold.1
- ___getASAuthorizationPlatformPublicKeyCredentialProviderClass_block_invoke.cold.1
- ___getASAuthorizationPlatformPublicKeyCredentialRegistrationClass_block_invoke.cold.1
- ___getASAuthorizationPlatformPublicKeyCredentialRegistrationRequestClass_block_invoke.cold.1
- ___getASAuthorizationPublicKeyCredentialParametersClass_block_invoke.cold.1
- ___getASAuthorizationSecurityKeyPublicKeyCredentialAssertionClass_block_invoke.cold.1
- ___getASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequestClass_block_invoke.cold.1
- ___getASAuthorizationSecurityKeyPublicKeyCredentialDescriptorClass_block_invoke.cold.1
- ___getASAuthorizationSecurityKeyPublicKeyCredentialProviderClass_block_invoke.cold.1
- ___getASAuthorizationSecurityKeyPublicKeyCredentialRegistrationClass_block_invoke.cold.1
- ___getASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequestClass_block_invoke.cold.1
- ___getASCAdamIDClass_block_invoke.cold.1
- ___getASCArtworkClass_block_invoke.cold.1
- ___getASCLockupRequestClass_block_invoke.cold.1
- ___getASCLockupViewGroupClass_block_invoke.cold.1
- ___getBYLicenseAgreementClass_block_invoke.cold.1
- ___getCDPAccountClass_block_invoke.cold.1
- ___getCDPContextClass_block_invoke.cold.1
- ___getCDPFollowUpContextClass_block_invoke.cold.1
- ___getCDPFollowUpControllerClass_block_invoke.cold.1
- ___getCDPKeychainSyncClass_block_invoke.cold.1
- ___getCDPRecoveryControllerClass_block_invoke.cold.1
- ___getCDPStateControllerClass_block_invoke.cold.1
- ___getCDPStateUIControllerClass_block_invoke.cold.1
- ___getCDPUIAccountRecoveryControllerClass_block_invoke.cold.1
- ___getCDPUIControllerClass_block_invoke.cold.1
- ___getCDPUIStatusChangeControllerClass_block_invoke.cold.1
- ___getCDPWalrusStateControllerClass_block_invoke.cold.1
- ___getCDPWebAccessStateControllerClass_block_invoke.cold.1
- ___getDCBAASigningControllerClass_block_invoke.cold.1
- ___getFLFollowUpActionClass_block_invoke.cold.1
- ___getFLFollowUpControllerClass_block_invoke.cold.1
- ___getFLFollowUpItemClass_block_invoke.cold.1
- ___getFLFollowUpNotificationClass_block_invoke.cold.1
- ___getFLHSA2LoginNotificationClass_block_invoke.cold.1
- ___getFLHSA2PasswordResetNotificationClass_block_invoke.cold.1
- ___getKCAESGCMDuplexSessionClass_block_invoke.cold.1
- ___getKCJoiningAcceptAccountCircleDelegateClass_block_invoke.cold.1
- ___getKCJoiningAcceptSessionClass_block_invoke.cold.1
- ___getKCJoiningRequestSecretSessionClass_block_invoke.cold.1
- ___getPASUIDependentViewPresenterClass_block_invoke.cold.1
- ___getRUIParserClass_block_invoke.cold.1
- ___getRUIXMLParserDelegateClass_block_invoke.cold.1
- ___getUMUserManagerClass_block_invoke.cold.1
- __isFaceIDPlatform.cold.1
- _fputc
- _fputs
- _getASAuthorizationErrorCanceled.cold.1
- _getASAuthorizationErrorDomain.cold.1
- _getASAuthorizationPublicKeyCredentialAttestationKindDirect.cold.1
- _getASAuthorizationPublicKeyCredentialResidentKeyPreferencePreferred.cold.1
- _getASCArtworkCropBoundingBox.cold.1
- _getASCArtworkDecorationNone.cold.1
- _getASCArtworkDecorationRoundedRect.cold.1
- _getASCArtworkFormatPNG.cold.1
- _getASCArtworkTemplateKeyCrop.cold.1
- _getASCArtworkTemplateKeyFormat.cold.1
- _getASCArtworkTemplateKeyHeight.cold.1
- _getASCArtworkTemplateKeyWidth.cold.1
- _getASCLockupContextSignInWithApple.cold.1
- _getASCOSEAlgorithmIdentifierES256.cold.1
- _getCDPIDMSPasswordResetKey.cold.1
- _getCDPIDMSRecordMIDKey.cold.1
- _getCDPStateErrorDomain.cold.1
- _getCDPWalrusStateChangeNotification.cold.1
- _getCDPWebAccessStateChangeNotification.cold.1
- _getFLGroupIdentifierAccount.cold.1
- _getFLGroupIdentifierNoGroup.cold.1
- _getFLHSA2ActionChangePassword.cold.1
- _getFLNotificationOptionBannerAlert.cold.1
- _getFLNotificationOptionExtensionActions.cold.1
- _getFLNotificationOptionExtensionForNotification.cold.1
- _getFLNotificationOptionForce.cold.1
- _getFLNotificationOptionSpringboardAlert.cold.1
- _getFLNotificationOptionSpringboardAlertActionOnly.cold.1
- _getNSDocumentTypeDocumentAttribute.cold.1
- _getNSHTMLTextDocumentType.cold.1
- _get_ASCLockupKeyAdamID.cold.1
- _get_ASCLockupKeyDeveloperName.cold.1
- _get_ASCLockupKeyIcon.cold.1
- _get_ASCLockupKeyShortName.cold.1
- _get_ASCLockupKeyTitle.cold.1
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$removeFollowUpItemsWithIdentifiers:error:
- _objc_release_x1
- _objc_release_x10
- _objc_release_x19
- _objc_release_x20
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_release_x8
- _objc_release_x9
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "\n"
+ "/Applications/App Store.app"
+ "/System/Library/PrivateFrameworks/AOSUI.framework"
+ "1.2.840.113635.100.6.27.2"
+ "<%@:%p> identifier: %@, action: %@, altDSID: %@, txnid: %@, telemetryFlowID: %@"
+ "AKDisablePET"
+ "AKIDMSEnvironment"
+ "AKUseWebAuthenticationForIDP"
+ "AppIcon"
+ "AppleID"
+ "Attempting to fetch consent version without an account"
+ "B32@0:8^@16@\"NSString\"24"
+ "B32@0:8^@16@24"
+ "B40@0:8@\"FLFollowUpItem\"16@\"NSString\"24^@32"
+ "B40@0:8@\"NSArray\"16@\"NSString\"24^@32"
+ "Device status - ITK %@"
+ "LAUNCHED_FOR_AUTHENTICATION_SESSION"
+ "T@\"NSString\",C,N,V_effectiveUserIdentifier"
+ "X-Apple-Baa-S"
+ "X-Apple-I-MD-EUID"
+ "X-Apple-I-MD-LU-S"
+ "X-Apple-I-PrivacyConsent-Value"
+ "X-Apple-I-PrivacyConsent-Version"
+ "X-Apple-Proxied-Baa-S"
+ "_effectiveUserIdentifier"
+ "_embargoEndFeedback"
+ "addFollowUpItems:telemetryFlowID:error:"
+ "ak_addEffectiveUserIdentifierHeader"
+ "analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:"
+ "appleAccountConsentVersionForAccount:"
+ "application/x-apple-plist"
+ "application/xml"
+ "clearNotificationsForItem:telemetryFlowID:error:"
+ "com.apple.Home"
+ "com.apple.idms.config.privacy.appleid.consent"
+ "effectiveUserIdentifier"
+ "followUpPostAnalyticsInfoWithIdentifier:telemetryFlowID:error:"
+ "hmeMappings"
+ "others"
+ "removeAllFollowUpItems:telemetryFlowID:"
+ "removeFollowUpItems:telemetryFlowID:error:"
+ "removeFollowUpItemsWithIdentifiers:telemetryFlowID:error:"
+ "sendEventForFollowUpWithError:eventName:success:telemetryFlowID:error:"
+ "setCfuType:"
+ "setConsentVersion:forAccount:"
+ "setDeviceSessionID:"
+ "setEffectiveUserIdentifier:"
+ "setFlowID:"
+ "setPostedReasonError:"
+ "softlink:o:fw:AAAFoundationSwift"
+ "softlink:o:fw:AppStoreComponents"
+ "softlink:o:fw:AuthenticationServices"
+ "softlink:o:fw:BiometricSupport"
+ "softlink:o:fw:CoreCDP"
+ "softlink:o:fw:CoreCDPUI"
+ "softlink:o:fw:CoreFollowUp"
+ "softlink:o:fw:DeviceCheckInternal"
+ "softlink:o:fw:KeychainCircle"
+ "softlink:o:fw:ProximityAppleIDSetupUI"
+ "softlink:o:fw:RemoteUI"
+ "softlink:o:fw:SetupAssistant"
+ "softlink:o:fw:UIKit"
+ "softlink:o:fw:UserManagement"
+ "text/plist"
+ "text/x-json"
+ "v52@0:8@16@24B32@36^@44"
- "<%@:%p> identifier: %@, action: %@, altDSID: %@, txnid: %@"
- "Continuity push detected."
- "Device status: %@ - ALT: %@"

```
