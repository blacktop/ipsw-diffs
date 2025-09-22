## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-521.1.1.0.0
-  __TEXT.__text: 0x174aa0
+525.125.2.1.0
+  __TEXT.__text: 0x176640
   __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0xd944
+  __TEXT.__objc_methlist: 0xda04
   __TEXT.__const: 0x69c8
-  __TEXT.__cstring: 0xf1f4
-  __TEXT.__oslogstring: 0x1175a
-  __TEXT.__gcc_except_tab: 0x9b20
+  __TEXT.__cstring: 0xf19c
+  __TEXT.__oslogstring: 0x11785
+  __TEXT.__gcc_except_tab: 0x9a7c
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x4038
-  __TEXT.__objc_classname: 0x1c15
-  __TEXT.__objc_methname: 0x21cf2
-  __TEXT.__objc_methtype: 0x45bb
-  __TEXT.__objc_stubs: 0xf040
+  __TEXT.__unwind_info: 0x4008
+  __TEXT.__objc_classname: 0x1c33
+  __TEXT.__objc_methname: 0x21e45
+  __TEXT.__objc_methtype: 0x4639
+  __TEXT.__objc_stubs: 0xf660
   __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0xa0c8
-  __DATA_CONST.__objc_classlist: 0x620
+  __DATA_CONST.__const: 0x9ff8
+  __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e80
+  __DATA_CONST.__objc_selrefs: 0x6ef0
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x2c8
   __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH_CONST.__const: 0x1200
-  __AUTH_CONST.__cfstring: 0xf9a0
-  __AUTH_CONST.__objc_const: 0x25230
+  __AUTH_CONST.__const: 0x1320
+  __AUTH_CONST.__cfstring: 0xf7a0
+  __AUTH_CONST.__objc_const: 0x25210
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH.__objc_data: 0x2620
-  __DATA.__objc_ivar: 0xfd0
+  __AUTH.__objc_data: 0x2670
+  __DATA.__objc_ivar: 0xfc4
   __DATA.__data: 0x1900
-  __DATA.__bss: 0x628
+  __DATA.__bss: 0x6c8
   __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB17DD95-D73A-38F9-B964-3EF3B82F5990
-  Functions: 5280
-  Symbols:   20051
-  CStrings:  11654
+  UUID: 0219D278-D2E9-34D4-8E72-22ADB3B24ED4
+  Functions: 5303
+  Symbols:   20153
+  CStrings:  11630
 
Symbols:
+ +[AKUserInformation(Updates) _advancedSecurityFields]
+ +[AKUserInformation(Updates) _ageFields]
+ +[AKUserInformation(Updates) _coreIdentityFields]
+ +[AKUserInformation(Updates) _emailFields]
+ +[AKUserInformation(Updates) _featureFlagFields]
+ +[AKUserInformation(Updates) _guitarfishFields]
+ +[AKUserInformation(Updates) _managedFields]
+ +[AKUserInformation(Updates) _securityFields]
+ +[AKUserInformation(Updates) isFieldUpdateableForAccountWithAltDSID:fieldName:]
+ +[AKUserInformation(Updates) userInformationForUpdates]
+ +[NSDate(AuthKit) ak_dateFromRFC2822String:]
+ -[AKAccountManager isEligibleForSafetyScreenForAccount:]
+ -[AKAccountManager lastSettingsRedirectDateForAccount:]
+ -[AKAccountManager setIsEligibleForSafetyScreen:forAccount:]
+ -[AKAccountManager setLastSettingsRedirectDate:forAccount:]
+ -[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]
+ -[AKAppleIDAuthenticationController updateUserInformationWithContext:userInformation:completion:]
+ -[AKDevice bootSessionUUID]
+ -[AKSafetyScreenManager .cxx_destruct]
+ -[AKSafetyScreenManager _hasSeenSafetyScreenForAccount:]
+ -[AKSafetyScreenManager _safetyScreenEligibilityForAccount:]
+ -[AKSafetyScreenManager _setSafetyScreenSeen:forAccount:]
+ -[AKSafetyScreenManager accountManager]
+ -[AKSafetyScreenManager initWithAccountManager:]
+ -[AKSafetyScreenManager init]
+ -[AKSafetyScreenManager markSafetyScreenSeenForAccount:]
+ -[AKSafetyScreenManager setAccountManager:]
+ -[AKSafetyScreenManager shouldShowSafetyScreenForAccount:]
+ -[AKUserInformation adpBlockMode]
+ -[AKUserInformation isEligibleForSafetyScreen]
+ -[AKUserInformation setAdpBlockMode:]
+ -[AKUserInformation setIsEligibleForSafetyScreen:]
+ -[AKUserInformation(Updates) _getAdvancedSecurityFields]
+ -[AKUserInformation(Updates) _getAgeAndDemographicsFields]
+ -[AKUserInformation(Updates) _getCoreIdentityFields]
+ -[AKUserInformation(Updates) _getEmailFields]
+ -[AKUserInformation(Updates) _getFeatureFlagFields]
+ -[AKUserInformation(Updates) _getGuitarfishFields]
+ -[AKUserInformation(Updates) _getManagedAccountFields]
+ -[AKUserInformation(Updates) _getSecurityFields]
+ -[AKUserInformation(Updates) hasUpdateableFieldsForAccountWithAltDSID:]
+ -[AKUserInformation(Updates) updateableFieldNamesForAccountWithAltDSID:]
+ -[AKUserInformation(Updates) validateForUpdatesWithContext:error:]
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table129
+ GCC_except_table137
+ GCC_except_table140
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table159
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table213
+ GCC_except_table217
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table238
+ GCC_except_table240
+ GCC_except_table260
+ GCC_except_table261
+ GCC_except_table283
+ GCC_except_table300
+ GCC_except_table301
+ GCC_except_table302
+ GCC_except_table337
+ GCC_except_table338
+ GCC_except_table45
+ GCC_except_table93
+ _AKAdditionalInfoKey
+ _AKHTTPResponseHeaderGenericServerTimeKey
+ _AKLastSettingsRedirectDateKey
+ _AKPropertySafetyScreenEligibility
+ _AKPropertySafetyScreenSeenKey
+ _AKURLBagKeyADPBlockMode
+ _AKURLBagKeyUpdateUserInfo
+ _AKUserInfoADPBlockModeKey
+ _AKUserInfoAccountNameKey
+ _AKUserInfoAgeOfMajorityKey
+ _AKUserInfoAliasesKey
+ _AKUserInfoAuthorizedAppsVersionKey
+ _AKUserInfoBeneficiaryLastModifiedKey
+ _AKUserInfoCanBeBeneficiaryKey
+ _AKUserInfoCanBeCustodianKey
+ _AKUserInfoCanHaveBeneficiaryKey
+ _AKUserInfoCanHaveCustodianKey
+ _AKUserInfoCountryCodeKey
+ _AKUserInfoCustodianEnabledKey
+ _AKUserInfoCustodianLastModifiedKey
+ _AKUserInfoFamilyNameKey
+ _AKUserInfoForwardingEmailKey
+ _AKUserInfoGivenNameKey
+ _AKUserInfoHasUsedSignInWithAppleKey
+ _AKUserInfoIsAppleManagedAccountKey
+ _AKUserInfoIsLegacyStudentKey
+ _AKUserInfoIsSeniorKey
+ _AKUserInfoIsSiwaEnabledKey
+ _AKUserInfoIsUnderageKey
+ _AKUserInfoLoginHandlesKey
+ _AKUserInfoManagedOrgNameKey
+ _AKUserInfoManagedOrgTypeKey
+ _AKUserInfoMasterKeyIDKey
+ _AKUserInfoNotificationEmailAvailableKey
+ _AKUserInfoNotificationEmailKey
+ _AKUserInfoPhoneAsAppleIDKey
+ _AKUserInfoPreviousSelectedEmailKey
+ _AKUserInfoPreviouslyWantedPrivateEmailKey
+ _AKUserInfoPrimaryEmailKey
+ _AKUserInfoPrivateAttestationKey
+ _AKUserInfoReachableEmailsKey
+ _AKUserInfoRepairStateKey
+ _AKUserInfoSafetyScreenEligibilityKey
+ _AKUserInfoSecurityKeysKey
+ _AKUserInfoSecurityLevelKey
+ _AKUserInfoTrustedPhonesKey
+ _AKUserInfoUserAgeRangeKey
+ _AKUserInfoVettedPrimaryEmailKey
+ _OBJC_CLASS_$_AKSafetyScreenManager
+ _OBJC_IVAR_$_AKSafetyScreenManager._accountManager
+ _OBJC_IVAR_$_AKUserInformation._adpBlockMode
+ _OBJC_IVAR_$_AKUserInformation._isEligibleForSafetyScreen
+ _OBJC_METACLASS_$_AKSafetyScreenManager
+ __OBJC_$_CLASS_METHODS_AKUserInformation(Updates)
+ __OBJC_$_INSTANCE_METHODS_AKSafetyScreenManager
+ __OBJC_$_INSTANCE_METHODS_AKUserInformation(Updates)
+ __OBJC_$_INSTANCE_VARIABLES_AKSafetyScreenManager
+ __OBJC_$_PROP_LIST_AKSafetyScreenManager
+ __OBJC_CLASS_RO_$_AKSafetyScreenManager
+ __OBJC_METACLASS_RO_$_AKSafetyScreenManager
+ ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.324
+ ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.323
+ ___116-[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]_block_invoke
+ ___116-[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]_block_invoke.293
+ ___116-[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]_block_invoke.294
+ ___116-[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]_block_invoke_2
+ ___27-[AKDevice bootSessionUUID]_block_invoke
+ ___40+[AKUserInformation(Updates) _ageFields]_block_invoke
+ ___42+[AKUserInformation(Updates) _emailFields]_block_invoke
+ ___44+[AKUserInformation(Updates) _managedFields]_block_invoke
+ ___44+[NSDate(AuthKit) ak_dateFromRFC2822String:]_block_invoke
+ ___44+[NSDate(AuthKit) ak_dateFromRFC2822String:]_block_invoke_2
+ ___45+[AKUserInformation(Updates) _securityFields]_block_invoke
+ ___47+[AKUserInformation(Updates) _guitarfishFields]_block_invoke
+ ___48+[AKUserInformation(Updates) _featureFlagFields]_block_invoke
+ ___49+[AKUserInformation(Updates) _coreIdentityFields]_block_invoke
+ ___49-[AKConfiguration shouldEnableAttestationLogging]_block_invoke
+ ___53+[AKUserInformation(Updates) _advancedSecurityFields]_block_invoke
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.344
+ ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.300
+ ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.149
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.304
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.305
+ ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.315
+ ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.346
+ ___71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.299
+ ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.357
+ ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.347
+ ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.256
+ ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.364
+ ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.358
+ ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.334
+ ___72-[AKUserInformation(Updates) updateableFieldNamesForAccountWithAltDSID:]_block_invoke
+ ___73-[AKAppleIDAuthenticationController _authenticateWithContext:completion:]_block_invoke.258
+ ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.353
+ ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke.297
+ ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.356
+ ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.278
+ ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.125
+ ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.129
+ ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.130
+ ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke_2.136
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.341
+ ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.272
+ ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.332
+ ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.301
+ ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke.284
+ ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.316
+ ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.307
+ ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke.283
+ ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.333
+ ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke.281
+ ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.322
+ ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.318
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.351
+ ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.321
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.339
+ ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.352
+ ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.303
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.327
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.328
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.329
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.330
+ ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.331
+ ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.349
+ ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.262
+ ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.263
+ ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.354
+ ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.306
+ ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.313
+ ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.348
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.320
+ ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.336
+ ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.312
+ ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.311
+ ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.319
+ ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.355
+ ___block_descriptor_40_e8_32s_e35_B24?0"NSString"8"NSDictionary"16ls32l8
+ ___block_literal_global.192
+ ___block_literal_global.227
+ ___block_literal_global.228
+ ___block_literal_global.230
+ ___block_literal_global.252
+ ___block_literal_global.265
+ ___block_literal_global.275
+ ___block_literal_global.277
+ ___block_literal_global.280
+ ___block_literal_global.3
+ ___block_literal_global.343
+ ___block_literal_global.421
+ ___block_literal_global.645
+ ___block_literal_global.647
+ ___block_literal_global.649
+ ___block_literal_global.651
+ ___block_literal_global.653
+ ___block_literal_global.656
+ ___block_literal_global.658
+ ___os_log_helper_16_2_3_8_112_8_64_8_64
+ __advancedSecurityFields.fields
+ __advancedSecurityFields.onceToken
+ __ageFields.fields
+ __ageFields.onceToken
+ __coreIdentityFields.fields
+ __coreIdentityFields.onceToken
+ __emailFields.fields
+ __emailFields.onceToken
+ __featureFlagFields.fields
+ __featureFlagFields.onceToken
+ __guitarfishFields.fields
+ __guitarfishFields.onceToken
+ __managedFields.fields
+ __managedFields.onceToken
+ __securityFields.fields
+ __securityFields.onceToken
+ _ak_dateFromRFC2822String:.formatter
+ _ak_dateFromRFC2822String:.onceToken
+ _bootSessionUUID._bootSessionUUID
+ _bootSessionUUID.onceToken
+ _objc_msgSend$_advancedSecurityFields
+ _objc_msgSend$_ageFields
+ _objc_msgSend$_coreIdentityFields
+ _objc_msgSend$_emailFields
+ _objc_msgSend$_featureFlagFields
+ _objc_msgSend$_getAdvancedSecurityFields
+ _objc_msgSend$_getAgeAndDemographicsFields
+ _objc_msgSend$_getCoreIdentityFields
+ _objc_msgSend$_getEmailFields
+ _objc_msgSend$_getFeatureFlagFields
+ _objc_msgSend$_getGuitarfishFields
+ _objc_msgSend$_getManagedAccountFields
+ _objc_msgSend$_getSecurityFields
+ _objc_msgSend$_guitarfishFields
+ _objc_msgSend$_hasSeenSafetyScreenForAccount:
+ _objc_msgSend$_managedFields
+ _objc_msgSend$_safetyScreenEligibilityForAccount:
+ _objc_msgSend$_securityFields
+ _objc_msgSend$_setSafetyScreenSeen:forAccount:
+ _objc_msgSend$_updateUserInformationWithContext:userInformation:isServerOperation:completion:
+ _objc_msgSend$accountAliases
+ _objc_msgSend$accountName
+ _objc_msgSend$adpBlockMode
+ _objc_msgSend$ageOfMajority
+ _objc_msgSend$appleIDCountryCode
+ _objc_msgSend$birthDay
+ _objc_msgSend$birthMonth
+ _objc_msgSend$birthYear
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$forwardingEmail
+ _objc_msgSend$hasUpdateableFieldsForAccountWithAltDSID:
+ _objc_msgSend$hasUsedAuthorization
+ _objc_msgSend$initWithAccountManager:
+ _objc_msgSend$initWithLocaleIdentifier:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$isEligibleForSafetyScreenForAccount:
+ _objc_msgSend$isFieldUpdateableForAccountWithAltDSID:fieldName:
+ _objc_msgSend$isLegacyStudent
+ _objc_msgSend$isNotificationEmailAvailable
+ _objc_msgSend$isSenior
+ _objc_msgSend$isUnderage
+ _objc_msgSend$loginHandles
+ _objc_msgSend$managedOrganizationName
+ _objc_msgSend$managedOrganizationType
+ _objc_msgSend$notificationEmail
+ _objc_msgSend$phoneAsAppleID
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$previouslySelectedEmail
+ _objc_msgSend$previouslyWantedPrivateEmail
+ _objc_msgSend$primaryEmailAddress
+ _objc_msgSend$privateAttestationEnabled
+ _objc_msgSend$reachableEmails
+ _objc_msgSend$repairState
+ _objc_msgSend$setAdpBlockMode:
+ _objc_msgSend$setIsEligibleForSafetyScreen:
+ _objc_msgSend$trustedPhoneNumbers
+ _objc_msgSend$updateUserInformationWithContext:userInformation:completion:
+ _objc_msgSend$updateableFieldNamesForAccountWithAltDSID:
+ _objc_msgSend$userAgeRange
+ _objc_msgSend$vettedPrimaryEmail
+ _objc_msgSend$webAccessEnabled
+ _shouldEnableAttestationLogging.configState
+ _shouldEnableAttestationLogging.onceToken
- +[AKAppleIDAuthenticationController sensitiveTokenKeysForFullRedaction]
- -[AKAccountManager edpStateForAccount:]
- -[AKAccountManager edpStateValueForAccount:]
- -[AKAccountManager idmsEDPTokenIdForAccount:]
- -[AKAccountManager passwordVersionForAccount:]
- -[AKAccountManager setEDPState:forAccount:]
- -[AKAccountManager setIdMSEDPTokenId:forAccount:]
- -[AKAccountManager setPasswordVersion:forAccount:]
- -[AKAccountManager setSRPProtocol:forAccount:]
- -[AKAccountManager srpProtocolForAccount:]
- -[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]
- -[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]
- -[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]
- -[AKAppleIDServerResourceLoadDelegate attachEDPToken]
- -[AKAppleIDServerResourceLoadDelegate setAttachEDPToken:]
- -[AKConfiguration baaTimeDelta]
- -[AKConfiguration setBaaTimeDelta:]
- -[AKFeatureManager isSecurePakeEnabled]
- -[AKUserInformation edpState]
- -[AKUserInformation idmsEDPTokenId]
- -[AKUserInformation passwordVersion]
- -[AKUserInformation setEdpState:]
- -[AKUserInformation setIdmsEDPTokenId:]
- -[AKUserInformation setPasswordVersion:]
- -[AKUserInformation setSrpProtocol:]
- -[AKUserInformation srpProtocol]
- GCC_except_table106
- GCC_except_table110
- GCC_except_table130
- GCC_except_table131
- GCC_except_table132
- GCC_except_table139
- GCC_except_table143
- GCC_except_table147
- GCC_except_table150
- GCC_except_table154
- GCC_except_table156
- GCC_except_table157
- GCC_except_table168
- GCC_except_table172
- GCC_except_table176
- GCC_except_table181
- GCC_except_table198
- GCC_except_table209
- GCC_except_table210
- GCC_except_table214
- GCC_except_table215
- GCC_except_table235
- GCC_except_table237
- GCC_except_table257
- GCC_except_table258
- GCC_except_table274
- GCC_except_table288
- GCC_except_table289
- GCC_except_table290
- GCC_except_table327
- GCC_except_table331
- GCC_except_table342
- GCC_except_table343
- GCC_except_table344
- GCC_except_table345
- GCC_except_table346
- GCC_except_table99
- _AKDeviceAdditionalInfoKey
- _AKEDPIdMSRecoveryTokenKey
- _AKEDPStateHeaderKey
- _AKEDPStateKey
- _AKEDPTokenHeaderKey
- _AKIdMSEDPTokenIdKey
- _AKInformationSecurityLevelKey
- _AKPasswordVersionHeaderKey
- _AKPasswordVersionKey
- _AKRequestBodyEDPAttemptsRemaining
- _AKRequestBodyEDPCountOfDBRRecordsMatchedToNewestRecoveryKey
- _AKRequestBodyEDPCountOfRecordIdentities
- _AKRequestBodyEDPIdentityHash
- _AKRequestBodyEDPPasswordVersionMatchesIdms
- _AKRequestBodyEDPPrimary
- _AKRequestBodyEDPRecovery
- _AKRequestBodyEDPStashedRecoveryTokenMatchesEscrow
- _AKRequestBodyEDPState
- _AKSRPIterationCountKey
- _AKSRPIterationHeaderKey
- _AKSRPProtocolHeaderKey
- _AKSRPProtocolKey
- _AKSRPSaltHeaderKey
- _AKSRPSaltKey
- _AKURLBagKeyEDPComplete
- _AKURLBagKeyEDPMigration
- _AKURLBagKeyRemoveEDPToken
- _AKURLBagKeySendRecoveryTokenEmail
- _AKURLBagKeyStoreEDPToken
- _OBJC_IVAR_$_AKAppleIDServerResourceLoadDelegate._attachEDPToken
- _OBJC_IVAR_$_AKFeatureManager._cachedSecurePakeEnabled
- _OBJC_IVAR_$_AKUserInformation._edpState
- _OBJC_IVAR_$_AKUserInformation._idmsEDPTokenId
- _OBJC_IVAR_$_AKUserInformation._passwordVersion
- _OBJC_IVAR_$_AKUserInformation._srpProtocol
- __AKActiveHMECount
- __AKInActiveHMECount
- __AKInformationAccountNameKey
- __AKInformationAdditionalInfoKey
- __AKInformationAgeOfMajority
- __AKInformationAliasesKey
- __AKInformationAppleIDCountryCodeKey
- __AKInformationApplicationsListVersionKey
- __AKInformationAuthorizationEnabledKey
- __AKInformationBeneficiaryLastModified
- __AKInformationCanBeBeneficiary
- __AKInformationCanBeCustodian
- __AKInformationCanHaveBeneficiary
- __AKInformationCanHaveCustodian
- __AKInformationCustodianEnabled
- __AKInformationCustodianLastModified
- __AKInformationFamilyNameKey
- __AKInformationForwardingEmailKey
- __AKInformationGivenNameKey
- __AKInformationGroupKitEligibilityKey
- __AKInformationHasMDMKey
- __AKInformationHmeMappingsKey
- __AKInformationIsLegacyStudentKey
- __AKInformationIsSeniorKey
- __AKInformationIsSiwaEnabledKey
- __AKInformationIsUnderageKey
- __AKInformationMakoAccountKey
- __AKInformationManagedOrganizationNameKey
- __AKInformationManagedOrganizationNotificationEmailAvailableKey
- __AKInformationManagedOrganizationNotificationEmailKey
- __AKInformationManagedOrganizationTypeKey
- __AKInformationMasterKeyIDKey
- __AKInformationPreviousEmailSelectedAsPrivateKey
- __AKInformationPreviousSelectedEmailKey
- __AKInformationPrimaryEmailKey
- __AKInformationPrimaryVettedEmailKey
- __AKInformationPrivateAttestationEnabledKey
- __AKInformationReachableEmailsKey
- __AKInformationRepairStateKey
- __AKInformationUserAgeRangeKey
- __AKIsEligibleToMigrateToChildKey
- __AKLoginHandlesKey
- __AKSecurityKeysKey
- __AKTrustedPhoneNumbersKey
- __OBJC_$_CLASS_METHODS_AKUserInformation
- __OBJC_$_INSTANCE_METHODS_AKUserInformation
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.322
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.321
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.343
- ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.298
- ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.159
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.302
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.303
- ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.313
- ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.345
- ___71+[AKAppleIDAuthenticationController sensitiveTokenKeysForFullRedaction]_block_invoke
- ___71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.297
- ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.356
- ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.346
- ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.264
- ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.366
- ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.360
- ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.332
- ___73-[AKAppleIDAuthenticationController _authenticateWithContext:completion:]_block_invoke.266
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.352
- ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke.295
- ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.355
- ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.286
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.128
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.136
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.138
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.140
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.145
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke_2.146
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke_4
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.339
- ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke
- ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.357
- ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke
- ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.359
- ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.280
- ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.330
- ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.299
- ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke.292
- ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.314
- ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.305
- ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke.291
- ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.331
- ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke.289
- ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.320
- ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.316
- ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke
- ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.358
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.349
- ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.319
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.335
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.351
- ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.301
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.325
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.326
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.327
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.328
- ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.329
- ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.348
- ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.270
- ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.271
- ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.353
- ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.304
- ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.311
- ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.347
- ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.318
- ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.334
- ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.310
- ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.309
- ___96-[AKAppleIDAuthenticationController updateUserInformationForAltDSID:userInformation:completion:]_block_invoke
- ___96-[AKAppleIDAuthenticationController updateUserInformationForAltDSID:userInformation:completion:]_block_invoke.293
- ___96-[AKAppleIDAuthenticationController updateUserInformationForAltDSID:userInformation:completion:]_block_invoke_2
- ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.317
- ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.354
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32bs40bs48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.221
- ___block_literal_global.234
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.246
- ___block_literal_global.273
- ___block_literal_global.283
- ___block_literal_global.285
- ___block_literal_global.288
- ___block_literal_global.342
- ___block_literal_global.430
- _objc_msgSend$aaf_toBase64EncodedString
- _objc_msgSend$edpStateForAccount:
- _objc_msgSend$fetchEDPTokenWithCompletion:
- _objc_msgSend$performEdpCompleteKeyDropWithAltDSID:completion:
- _objc_msgSend$performEdpMigrationWithAltDSID:completion:
- _objc_msgSend$performRemoveEdpTokenWithAltDSID:completion:
- _objc_msgSend$sensitiveTokenKeysForFullRedaction
- _objc_msgSend$setEdpState:
- _objc_msgSend$setIdmsEDPTokenId:
- _objc_msgSend$setPasswordVersion:
- _objc_msgSend$setSrpProtocol:
- _objc_msgSend$stateControllerWithContext:
- _sensitiveTokenKeysForFullRedaction.onceToken
- _sensitiveTokenKeysForFullRedaction.sensitiveTokenKeys
CStrings:
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
+ "@\"AKAccountManager\""
+ "AKSafetyScreenManager"
+ "Account with altDSID %{mask.hash}@ has unsupported security level %lu for user info updates"
+ "Authentication context is required"
+ "Authentication error missing AltDSID"
+ "B24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "Calling out to remote auth service to update user information for: %{mask.hash}@"
+ "Calling out to remote auth service to update user information on server for: %{mask.hash}@"
+ "Date"
+ "EEE, dd MMM yyyy HH:mm:ss zzz"
+ "Exception caught when fetching safety screen eligibility: %@"
+ "Exception caught when fetching safety screen seen property: %@. Defaulting to YES to minimize screen display"
+ "Exception caught when setting safety screen eligibility: %@"
+ "Failed to fetch account for altDSID %{mask.hash}@: %@"
+ "Incompatible security level for account updates"
+ "No updateable fields provided for account with altDSID %{mask.hash}@"
+ "Safety screen eligibility for account: %@ (source: additionalInfo)"
+ "Safety screen eligibility for account: %@ (source: direct property)"
+ "Safety screen eligibility for account: NO (not found)"
+ "T@\"AKAccountManager\",&,N,V_accountManager"
+ "T@\"NSNumber\",C,N,V_adpBlockMode"
+ "T@\"NSNumber\",C,N,V_isEligibleForSafetyScreen"
+ "Update user info failed with error: %{public}@"
+ "Updates"
+ "User information is required"
+ "_accountManager"
+ "_adpBlockMode"
+ "_advancedSecurityFields"
+ "_ageFields"
+ "_coreIdentityFields"
+ "_emailFields"
+ "_featureFlagFields"
+ "_getAdvancedSecurityFields"
+ "_getAgeAndDemographicsFields"
+ "_getCoreIdentityFields"
+ "_getEmailFields"
+ "_getFeatureFlagFields"
+ "_getGuitarfishFields"
+ "_getManagedAccountFields"
+ "_getSecurityFields"
+ "_guitarfishFields"
+ "_hasSeenSafetyScreenForAccount:"
+ "_isEligibleForSafetyScreen"
+ "_managedFields"
+ "_safetyScreenEligibilityForAccount:"
+ "_securityFields"
+ "_setSafetyScreenSeen:forAccount:"
+ "_updateUserInformationWithContext:userInformation:isServerOperation:completion:"
+ "accountManager"
+ "adpBlockMode"
+ "adpUserInfo"
+ "ak_dateFromRFC2822String:"
+ "bootSessionUUID"
+ "en_US_POSIX"
+ "filteredArrayUsingPredicate:"
+ "hasUpdateableFieldsForAccountWithAltDSID:"
+ "initWithAccountManager:"
+ "initWithLocaleIdentifier:"
+ "initWithUTF8String:"
+ "isEligibleForSafetyScreen"
+ "isEligibleForSafetyScreenForAccount:"
+ "isFieldUpdateableForAccountWithAltDSID:fieldName:"
+ "kern.bootsessionuuid"
+ "lastSettingsRedirectDate"
+ "lastSettingsRedirectDateForAccount:"
+ "markSafetyScreenSeenForAccount:"
+ "predicateWithBlock:"
+ "safetyScreenEligibility"
+ "safetyScreenSeen"
+ "setAccountManager:"
+ "setAdpBlockMode:"
+ "setIsEligibleForSafetyScreen:"
+ "setIsEligibleForSafetyScreen:forAccount:"
+ "setLastSettingsRedirectDate:forAccount:"
+ "shouldShowSafetyScreenForAccount:"
+ "updateUserInfo"
+ "updateUserInformationWithContext:userInformation:completion:"
+ "updateableFieldNamesForAccountWithAltDSID:"
+ "userInformationForUpdates"
+ "v40@0:8@\"AKAppleIDAuthenticationContext\"16@\"AKUserInformation\"24@?<v@?B@\"NSError\">32"
+ "v44@0:8@16@24B32@?36"
+ "validateForUpdatesWithContext:error:"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tedpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tidmsEDPTTokenId: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
- "<REDACTED>"
- "Calling out to remote auth service to perform EDP complete key drop"
- "Calling out to remote auth service to perform EDP migration"
- "Calling out to remote auth service to update user information for: %@"
- "EDP token being attached as a header."
- "Exception caught when fetching edpState property: %@"
- "Exception caught when fetching passwordVersion property: %@"
- "Exception caught when fetching srpProtocol property: %@"
- "Exception caught when fetching the idMSEDPTokenId property: %@"
- "Failed to fetch the EDP token due to %@, therefore it cannot be attached as a header."
- "Feature SecurePake enabled - %@"
- "Not sending EDP token as a header."
- "Rejecting out-of-range EDP state (%@)."
- "Result of EDP complete remote call result: %{BOOL}d and error: %@"
- "Result of EDP migration remote call result: %{BOOL}d and error: %@"
- "SecurePake"
- "Signing request with EDP headers."
- "T@\"NSNumber\",&,N"
- "T@\"NSNumber\",C,N,V_edpState"
- "T@\"NSNumber\",C,N,V_passwordVersion"
- "T@\"NSString\",C,N,V_idmsEDPTokenId"
- "T@\"NSString\",C,N,V_srpProtocol"
- "TB,N,V_attachEDPToken"
- "TB,R,N,GisSecurePakeEnabled"
- "X-Apple-I-EDP-Iters"
- "X-Apple-I-EDP-PV"
- "X-Apple-I-EDP-S"
- "X-Apple-I-EDP-SP"
- "X-Apple-I-EDP-Salt"
- "X-Apple-I-RT"
- "_attachEDPToken"
- "_cachedSecurePakeEnabled"
- "_edpState"
- "_idmsEDPTokenId"
- "_passwordVersion"
- "_srpProtocol"
- "aaf_toBase64EncodedString"
- "ar"
- "attachEDPToken"
- "authkit/edp-complete"
- "authkit/edp-migration"
- "authkit/remove-edp-token"
- "baaTimeDelta"
- "cri"
- "edpComplete"
- "edpMigration"
- "edpPrimary"
- "edpRecovery"
- "edpState"
- "edpStateForAccount:"
- "edpStateValueForAccount:"
- "edpToken"
- "edpTokenId"
- "edpmc"
- "edprtme"
- "edps"
- "fetchEDPTokenWithCompletion:"
- "hmeMappings"
- "idmsEDPTokenId"
- "idmsEDPTokenIdForAccount:"
- "ih"
- "isSecurePakeEnabled"
- "passwordVersion"
- "passwordVersionForAccount:"
- "performEdpCompleteKeyDropWithAltDSID:completion:"
- "performEdpCompleteKeyDropWithAltDSID:error:"
- "performEdpMigrationWithAltDSID:completion:"
- "performEdpMigrationWithAltDSID:error:"
- "performRemoveEdpTokenWithAltDSID:completion:"
- "performRemoveEdpTokenWithAltDSID:error:"
- "pv"
- "pvmi"
- "removeEdpToken"
- "securePakeEnabled"
- "sendRecoveryTokenEmail"
- "sensitiveTokenKeysForFullRedaction"
- "setAttachEDPToken:"
- "setBaaTimeDelta:"
- "setEDPState:forAccount:"
- "setEdpState:"
- "setIdMSEDPTokenId:forAccount:"
- "setIdmsEDPTokenId:"
- "setPasswordVersion:"
- "setPasswordVersion:forAccount:"
- "setSRPProtocol:forAccount:"
- "setSrpProtocol:"
- "sp"
- "srpProtocol"
- "srpProtocolForAccount:"
- "storeEdpToken"

```
