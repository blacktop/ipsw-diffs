## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-517.0.0.0.0
-  __TEXT.__text: 0xda1ac
+518.1.0.0.0
+  __TEXT.__text: 0xda914
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0xd7ac
+  __TEXT.__objc_methlist: 0xd7fc
   __TEXT.__const: 0x6af0
-  __TEXT.__cstring: 0xe9d6
-  __TEXT.__oslogstring: 0x113b2
-  __TEXT.__gcc_except_tab: 0x5798
+  __TEXT.__cstring: 0xefa3
+  __TEXT.__oslogstring: 0x11521
+  __TEXT.__gcc_except_tab: 0x57b8
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x16c
-  __TEXT.__unwind_info: 0x4028
-  __TEXT.__objc_classname: 0x1c02
-  __TEXT.__objc_methname: 0x2185e
+  __TEXT.__unwind_info: 0x4030
+  __TEXT.__objc_classname: 0x1c14
+  __TEXT.__objc_methname: 0x219b2
   __TEXT.__objc_methtype: 0x452a
-  __TEXT.__objc_stubs: 0xede0
-  __DATA_CONST.__got: 0xa08
-  __DATA_CONST.__const: 0x7ee8
-  __DATA_CONST.__objc_classlist: 0x618
+  __TEXT.__objc_stubs: 0xee60
+  __DATA_CONST.__got: 0xa10
+  __DATA_CONST.__const: 0x8038
+  __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6da8
+  __DATA_CONST.__objc_selrefs: 0x6dd8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x1d8
   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x11b0
-  __AUTH_CONST.__cfstring: 0xf1a0
-  __AUTH_CONST.__objc_const: 0x250c0
-  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__cfstring: 0xf640
+  __AUTH_CONST.__objc_const: 0x25190
+  __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x2530
-  __DATA.__objc_ivar: 0xfc4
+  __AUTH.__objc_data: 0x2580
+  __DATA.__objc_ivar: 0xfc8
   __DATA.__data: 0x18a0
   __DATA.__bss: 0x650
   __DATA_DIRTY.__objc_data: 0x17c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F81FA263-6AB6-38BC-B11D-B59E38BA06B5
-  Functions: 6152
-  Symbols:   21437
-  CStrings:  11454
+  UUID: F45016B7-60B5-3E7B-8B9A-8EBA39A85043
+  Functions: 6164
+  Symbols:   21509
+  CStrings:  11547
 
Symbols:
+ +[AKAnalyticsSender sendAnalyticsEvent:context:account:error:]
+ +[AKAnalyticsSender sendAnalyticsEvent:context:account:error:].cold.1
+ +[AKAnalyticsSender sendAnalyticsEvent:withError:]
+ +[AKAnalyticsSender sendAnalyticsEvent:withError:].cold.1
+ -[AKAccountManager renewDeviceSessionIDForAccount:]
+ -[AKAccountManager renewDeviceSessionIDForAccount:].cold.1
+ -[AKAccountManager renewDeviceSessionIDForAccount:].cold.2
+ -[AKAccountManager renewDeviceSessionIDForAccount:].cold.3
+ -[AKAccountManager renewDeviceSessionIDForAccount:].cold.4
+ -[AKAgeRangeSettingsProvider authController]
+ -[AKAgeRangeSettingsProvider setAuthController:]
+ -[AKFeatureManager init].cold.34
+ -[AKFeatureManager isAuthenticationTelemetryEnabled]
+ GCC_except_table117
+ GCC_except_table121
+ GCC_except_table130
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table153
+ GCC_except_table159
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table176
+ GCC_except_table187
+ GCC_except_table198
+ GCC_except_table201
+ GCC_except_table224
+ GCC_except_table246
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table277
+ GCC_except_table321
+ GCC_except_table331
+ GCC_except_table373
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table96
+ _OBJC_CLASS_$_AKAnalyticsSender
+ _OBJC_IVAR_$_AKFeatureManager._cachedAuthenticationTelemetryEnabled
+ _OBJC_METACLASS_$_AKAnalyticsSender
+ __OBJC_$_CLASS_METHODS_AKAnalyticsSender
+ __OBJC_CLASS_RO_$_AKAnalyticsSender
+ __OBJC_METACLASS_RO_$_AKAnalyticsSender
+ ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.322
+ ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.321
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.343
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.343.cold.1
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.343.cold.2
+ ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.298
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.302
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.302.cold.1
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.303
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.303.cold.1
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.303.cold.2
+ ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.313
+ ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.345
+ ___71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.297
+ ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.346
+ ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.264
+ ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.264.cold.1
+ ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.364
+ ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.358
+ ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.332
+ ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.332.cold.1
+ ___73-[AKAppleIDAuthenticationController _authenticateWithContext:completion:]_block_invoke.266
+ ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.352
+ ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.352.cold.1
+ ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke.295
+ ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.286
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.339
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.339.cold.1
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.340
+ ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.355
+ ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.355.cold.1
+ ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.357
+ ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.357.cold.1
+ ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.280
+ ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.330
+ ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.330.cold.1
+ ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.299
+ ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke.292
+ ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.314
+ ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.305
+ ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke.291
+ ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.331
+ ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.331.cold.1
+ ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke.289
+ ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.320
+ ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.316
+ ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.356
+ ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.356.cold.1
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.349
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.349.cold.1
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.350
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.350.cold.1
+ ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.319
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.335
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.337
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.337.cold.1
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.338
+ ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.351
+ ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.351.cold.1
+ ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.301
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.325
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.325.cold.1
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.326
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.327
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.327.cold.1
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.328
+ ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.329
+ ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.348
+ ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.270
+ ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.271
+ ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.353
+ ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.353.cold.1
+ ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.304
+ ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.311
+ ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.347
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.318
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.318.cold.1
+ ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.334
+ ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.334.cold.1
+ ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.310
+ ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.309
+ ___96-[AKAppleIDAuthenticationController updateUserInformationForAltDSID:userInformation:completion:]_block_invoke.293
+ ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.317
+ ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.317.cold.1
+ ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.354
+ ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.354.cold.1
+ ___block_descriptor_80_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.273
+ ___block_literal_global.283
+ ___block_literal_global.285
+ ___block_literal_global.288
+ ___block_literal_global.342
+ _kAKAnalyticsEventAuthMasterKey
+ _kAKAnalyticsEventAuthMasterKeyStart
+ _kAKAnalyticsEventAuthServerUI
+ _kAKAnalyticsEventAuthServerUIStart
+ _kAKAnalyticsEventAuthentication
+ _kAKAnalyticsEventAuthenticationStart
+ _kAKAnalyticsEventBiometricAuth
+ _kAKAnalyticsEventDeviceAuth
+ _kAKAnalyticsEventDeviceAuthStart
+ _kAKAnalyticsEventFederatedAuth
+ _kAKAnalyticsEventFederatedAuthStart
+ _kAKAnalyticsEventInteractiveAuth
+ _kAKAnalyticsEventInteractiveAuthStart
+ _kAKAnalyticsEventPasscodeAuth
+ _kAKAnalyticsEventPasswordlessAuth
+ _kAKAnalyticsEventPasswordlessAuthStart
+ _kAKAnalyticsEventPiggybackingAccepting
+ _kAKAnalyticsEventPiggybackingAcceptingStart
+ _kAKAnalyticsEventPiggybackingCancellation
+ _kAKAnalyticsEventPiggybackingCircleRequest
+ _kAKAnalyticsEventPiggybackingCircleRequestStart
+ _kAKAnalyticsEventPiggybackingEscapeHatch
+ _kAKAnalyticsEventPiggybackingProcessPushPayload
+ _kAKAnalyticsEventPiggybackingProcessPushPayloadStart
+ _kAKAnalyticsEventPiggybackingProximityDetection
+ _kAKAnalyticsEventPiggybackingProximityDetectionStart
+ _kAKAnalyticsEventPiggybackingRequesting
+ _kAKAnalyticsEventPiggybackingRequestingStart
+ _kAKAnalyticsEventPiggybackingSecretGeneration
+ _kAKAnalyticsEventPiggybackingVerificationFailure
+ _kAKAnalyticsEventSRPAuthentication
+ _kAKAnalyticsEventSRPAuthenticationStart
+ _kAKAnalyticsEventSecondFactorPrompt
+ _kAKAnalyticsEventSecondFactorPromptStart
+ _kAKAnalyticsEventSecondFactorValidation
+ _kAKAnalyticsEventSecondFactorValidationStart
+ _kAKAnalyticsEventSecurityUpgrade
+ _kAKAnalyticsEventSecurityUpgradeStart
+ _kAKAnalyticsEventShouldContinueAuth
+ _kAKAnalyticsEventShouldContinueAuthStart
+ _kAKAnalyticsFieldHasProxiedDevice
+ _kAKAnalyticsFieldLocalSecretType
+ _kAKAnalyticsFieldProximityChannelAvailable
+ _kAKAnalyticsFieldSecureChannelType
+ _objc_msgSend$ak_updateWithAuthenticationResults:authContext:error:
+ _objc_msgSend$isAuthenticationTelemetryEnabled
+ _objc_msgSend$sendAnalyticsEvent:context:account:error:
+ _objc_msgSend$setNeedsNewAppleID:
- GCC_except_table118
- GCC_except_table129
- GCC_except_table139
- GCC_except_table142
- GCC_except_table144
- GCC_except_table155
- GCC_except_table158
- GCC_except_table163
- GCC_except_table174
- GCC_except_table178
- GCC_except_table181
- GCC_except_table188
- GCC_except_table200
- GCC_except_table221
- GCC_except_table225
- GCC_except_table227
- GCC_except_table248
- GCC_except_table264
- GCC_except_table267
- GCC_except_table270
- GCC_except_table288
- GCC_except_table323
- GCC_except_table368
- GCC_except_table51
- GCC_except_table84
- GCC_except_table88
- GCC_except_table97
- _AKAuthEventType_SECOND_FACTOR_PIGGYBACK_ESCAPE_FAILURE
- _AKAuthEventType_SECOND_FACTOR_PIGGYBACK_ESCAPE_SMS_SUCCESS
- _AKAuthEventType_SECOND_FACTOR_PIGGYBACK_FAILURE
- _AKAuthEventType_SECOND_FACTOR_PIGGYBACK_TRANSITION
- _AKAuthEventType_SECOND_FACTOR_SERVER_UI
- _AKAuthEventType_SRP_AUTH_FAILURE
- _AKAuthEventType_UNKNOWN
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.318
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.317
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.339
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.339.cold.1
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.339.cold.2
- ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.294
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.298
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.298.cold.1
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.299
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.299.cold.1
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.299.cold.2
- ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.309
- ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.341
- ___71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.293
- ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.342
- ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.260
- ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.260.cold.1
- ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.360
- ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.354
- ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.328
- ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.328.cold.1
- ___73-[AKAppleIDAuthenticationController _authenticateWithContext:completion:]_block_invoke.262
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.348
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.348.cold.1
- ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke.291
- ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.282
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.335
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.335.cold.1
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.336
- ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.351
- ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.351.cold.1
- ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.353
- ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.353.cold.1
- ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.276
- ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.326
- ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.326.cold.1
- ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.295
- ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke.288
- ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.310
- ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.301
- ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke.287
- ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.327
- ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.327.cold.1
- ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke.285
- ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.316
- ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.312
- ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.352
- ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.352.cold.1
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.345
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.345.cold.1
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.346
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.346.cold.1
- ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.315
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.331
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.333
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.333.cold.1
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.334
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.347
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.347.cold.1
- ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.297
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.321
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.321.cold.1
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.322
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.323
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.323.cold.1
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.324
- ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.325
- ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.344
- ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.266
- ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.267
- ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.349
- ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.349.cold.1
- ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.300
- ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.307
- ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.343
- ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.314
- ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.314.cold.1
- ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.330
- ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.330.cold.1
- ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.306
- ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.305
- ___96-[AKAppleIDAuthenticationController updateUserInformationForAltDSID:userInformation:completion:]_block_invoke.289
- ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.313
- ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.313.cold.1
- ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.350
- ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.350.cold.1
- ___block_literal_global.269
- ___block_literal_global.279
- ___block_literal_global.281
- ___block_literal_global.284
- ___block_literal_global.338
CStrings:
+ "AKAnalyticsSender"
+ "Analytics event is nil, skipping analytics"
+ "Analytics event name is nil, skipping analytics"
+ "Attempting to renew device session ID when it is not missing. Not permitted."
+ "Attempting to renew device session ID without an account"
+ "AuthenticationTelemetry"
+ "Created a new device session id: %@"
+ "Failed to save account after renewing device session ID: %@"
+ "Feature Authentication Telemetry enabled - %@"
+ "T@\"AKAppleIDAuthenticationController\",&,N,V_authController"
+ "TB,R,N,GisAuthenticationTelemetryEnabled"
+ "_cachedAuthenticationTelemetryEnabled"
+ "authController"
+ "authenticationTelemetryEnabled"
+ "com.apple.authkit.authMasterKey"
+ "com.apple.authkit.authMasterKeyStart"
+ "com.apple.authkit.authServerUI"
+ "com.apple.authkit.authServerUIStart"
+ "com.apple.authkit.authentication"
+ "com.apple.authkit.authenticationStart"
+ "com.apple.authkit.biometricAuth"
+ "com.apple.authkit.deviceAuth"
+ "com.apple.authkit.deviceAuthStart"
+ "com.apple.authkit.federatedAuth"
+ "com.apple.authkit.federatedAuthStart"
+ "com.apple.authkit.interactiveAuth"
+ "com.apple.authkit.interactiveAuthStart"
+ "com.apple.authkit.passcodeAuth"
+ "com.apple.authkit.passwordlessAuth"
+ "com.apple.authkit.passwordlessAuthStart"
+ "com.apple.authkit.piggybackingAccepting"
+ "com.apple.authkit.piggybackingAcceptingStart"
+ "com.apple.authkit.piggybackingCancellation"
+ "com.apple.authkit.piggybackingCircleRequest"
+ "com.apple.authkit.piggybackingCircleRequestStart"
+ "com.apple.authkit.piggybackingEscapeHatch"
+ "com.apple.authkit.piggybackingProcessPushPayload"
+ "com.apple.authkit.piggybackingProcessPushPayloadStart"
+ "com.apple.authkit.piggybackingProximityDetection"
+ "com.apple.authkit.piggybackingProximityDetectionStart"
+ "com.apple.authkit.piggybackingRequesting"
+ "com.apple.authkit.piggybackingRequestingStart"
+ "com.apple.authkit.piggybackingSecretGeneration"
+ "com.apple.authkit.piggybackingVerificationFailure"
+ "com.apple.authkit.secondFactorPrompt"
+ "com.apple.authkit.secondFactorPromptStart"
+ "com.apple.authkit.secondFactorValidation"
+ "com.apple.authkit.secondFactorValidationStart"
+ "com.apple.authkit.securityUpgrade"
+ "com.apple.authkit.securityUpgradeStart"
+ "com.apple.authkit.shouldContinueAuth"
+ "com.apple.authkit.shouldContinueAuthStart"
+ "com.apple.authkit.srpAuthentication"
+ "com.apple.authkit.srpAuthenticationStart"
+ "hasProxiedDevice"
+ "isAuthenticationTelemetryEnabled"
+ "localSecretType"
+ "proximityChannelAvailable"
+ "renewDeviceSessionIDForAccount:"
+ "secureChannelType"
+ "sendAnalyticsEvent:context:account:error:"
+ "sendAnalyticsEvent:withError:"
+ "setAuthController:"
- "AUTH_EVENT_TYPE_UNKNOWN"
- "SECOND_FACTOR_PIGGYBACK_ESCAPE_FAILURE"
- "SECOND_FACTOR_PIGGYBACK_ESCAPE_SMS_SUCCESS"
- "SECOND_FACTOR_PIGGYBACK_FAILURE"
- "SECOND_FACTOR_PIGGYBACK_TRANSITION"
- "SECOND_FACTOR_SERVER_UI"
- "SRP_AUTH_FAILURE"

```
