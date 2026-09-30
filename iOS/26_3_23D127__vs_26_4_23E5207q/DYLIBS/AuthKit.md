## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.326.4.1.0
-  __TEXT.__text: 0x189ecc
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_methlist: 0xe72c
-  __TEXT.__const: 0x69f8
-  __TEXT.__cstring: 0xffb1
-  __TEXT.__gcc_except_tab: 0xa464
-  __TEXT.__oslogstring: 0x12f42
+525.475.13.1.0
+  __TEXT.__text: 0x1966b8
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__objc_methlist: 0xef5c
+  __TEXT.__const: 0x6a48
+  __TEXT.__cstring: 0x1076f
+  __TEXT.__gcc_except_tab: 0xa798
+  __TEXT.__oslogstring: 0x13afa
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4358
-  __TEXT.__objc_classname: 0x1d89
-  __TEXT.__objc_methname: 0x23b8e
-  __TEXT.__objc_methtype: 0x47ed
-  __TEXT.__objc_stubs: 0x101a0
-  __DATA_CONST.__got: 0xaa0
-  __DATA_CONST.__const: 0xa448
-  __DATA_CONST.__objc_classlist: 0x688
+  __TEXT.__unwind_info: 0x4528
+  __TEXT.__objc_classname: 0x1e34
+  __TEXT.__objc_methname: 0x25057
+  __TEXT.__objc_methtype: 0x492d
+  __TEXT.__objc_stubs: 0x10b20
+  __DATA_CONST.__got: 0xac8
+  __DATA_CONST.__const: 0xa6a8
+  __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x74b0
+  __DATA_CONST.__objc_selrefs: 0x78a8
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x418
+  __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x630
-  __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x109c0
-  __AUTH_CONST.__objc_const: 0x26e28
+  __AUTH_CONST.__auth_got: 0x640
+  __AUTH_CONST.__const: 0x1410
+  __AUTH_CONST.__cfstring: 0x11560
+  __AUTH_CONST.__objc_const: 0x28238
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
-  __AUTH.__objc_data: 0x2c60
-  __DATA.__objc_ivar: 0x1098
+  __AUTH.__objc_data: 0x2ad0
+  __DATA.__objc_ivar: 0x1154
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6f8
-  __DATA_DIRTY.__objc_data: 0x14f0
-  __DATA_DIRTY.__bss: 0x2b0
+  __DATA_DIRTY.__objc_data: 0x1860
+  __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34986F66-57F6-3E1C-AEB2-8C937903AE31
-  Functions: 5596
-  Symbols:   21171
-  CStrings:  12330
+  UUID: 64914DAB-690D-35BE-8D8A-A2DE53551ADB
+  Functions: 5766
+  Symbols:   21821
+  CStrings:  12801
 
Symbols:
+ +[AKBAAAttestationData supportsSecureCoding]
+ +[AKCDPFactory generatePDPBlobWithContext:completion:]
+ +[AKHomeDeviceContext contextForRemovalWithAltDSID:hkdIDs:]
+ +[AKHomeDeviceContext supportsSecureCoding]
+ +[AKPDPBlobGenerationContext _decodeSaltFromBase64:error:]
+ +[AKPDPBlobGenerationContext _generateVerifierWithPassword:salt:iteration:protocol:error:]
+ +[AKPDPBlobGenerationContext supportsSecureCoding]
+ +[AKPasswordVerifierGenerator generateVerifierForPassword:salt:iteration:protocol:error:]
+ +[NSMutableURLRequest(AuthKit) _ak_anisetteHeadersWithAnisetteData:midKey:otpKey:routingInfoKey:]
+ -[AKAccountManager idmsTrustedDevicesVersionForAccount:]
+ -[AKAccountManager setIdMSTrustedDevicesVersion:forAccount:]
+ -[AKAccountManager setTrustedDeviceId:forAccount:]
+ -[AKAccountManager trustedDeviceIdForAccount:]
+ -[AKAccountManager updatePasskeyCredentialsWithAltDSID:username:]
+ -[AKAnisetteData baaAttestationData]
+ -[AKAnisetteData setBaaAttestationData:]
+ -[AKAppleIDAuthenticationContext(ThirdPartyDeviceAuth) configureForThirdPartyDeviceAuthWithAppProvidedData:]
+ -[AKAppleIDAuthenticationController generatePDPBlobWithContext:completion:]
+ -[AKAppleIDAuthenticationController removeHomeDevicesWithContext:completion:]
+ -[AKAppleIDPasskeyAuthenticationController _setCredentialDataManager:]
+ -[AKAppleIDPasskeyAuthenticationController updatePasskeyCredentialWithUserHandle:newName:completion:]
+ -[AKAppleIDSession _addFailureInjectionHeadersIfNeeded:forRequestURL:]
+ -[AKAppleIDSession additionalHeadersForSigning]
+ -[AKAppleIDSession setAdditionalHeadersForSigning:]
+ -[AKAttestationRequestData provisionAnisetteIfNeeded]
+ -[AKAttestationRequestData setProvisionAnisetteIfNeeded:]
+ -[AKAuthorizationPresentationContext iconSystemName]
+ -[AKBAAAttestationData .cxx_destruct]
+ -[AKBAAAttestationData _addAnisetteHeaders:]
+ -[AKBAAAttestationData _addBAAHeaders:]
+ -[AKBAAAttestationData _convertedAttestationHeadersForProxiedDevice:]
+ -[AKBAAAttestationData _isValidBAAState]
+ -[AKBAAAttestationData additionalBAAHeaders]
+ -[AKBAAAttestationData allHeaders]
+ -[AKBAAAttestationData anisetteHeaders]
+ -[AKBAAAttestationData baaAltSignature]
+ -[AKBAAAttestationData baaAttestationHeaders]
+ -[AKBAAAttestationData baaCert]
+ -[AKBAAAttestationData baaDeviceToken]
+ -[AKBAAAttestationData baaError]
+ -[AKBAAAttestationData baaSignature]
+ -[AKBAAAttestationData baaTime]
+ -[AKBAAAttestationData baaVersion]
+ -[AKBAAAttestationData companionAttestationHeaders]
+ -[AKBAAAttestationData copyWithZone:]
+ -[AKBAAAttestationData description]
+ -[AKBAAAttestationData encodeWithCoder:]
+ -[AKBAAAttestationData headersForSigning]
+ -[AKBAAAttestationData hostBAAAltSignature]
+ -[AKBAAAttestationData hostBAACert]
+ -[AKBAAAttestationData hostBAAError]
+ -[AKBAAAttestationData hostBAASignature]
+ -[AKBAAAttestationData initWithCoder:]
+ -[AKBAAAttestationData initWithIsVirtualMachine:isInternalBuild:]
+ -[AKBAAAttestationData init]
+ -[AKBAAAttestationData internalDebugTime]
+ -[AKBAAAttestationData internalDigestNoBody]
+ -[AKBAAAttestationData internalDigest]
+ -[AKBAAAttestationData isInternalBuild]
+ -[AKBAAAttestationData isVM]
+ -[AKBAAAttestationData machineID]
+ -[AKBAAAttestationData oneTimePassword]
+ -[AKBAAAttestationData proxiedAttestationHeaders]
+ -[AKBAAAttestationData routingInfo]
+ -[AKBAAAttestationData setAdditionalBAAHeaders:]
+ -[AKBAAAttestationData setBaaAltSignature:]
+ -[AKBAAAttestationData setBaaCert:]
+ -[AKBAAAttestationData setBaaDeviceToken:]
+ -[AKBAAAttestationData setBaaError:]
+ -[AKBAAAttestationData setBaaSignature:]
+ -[AKBAAAttestationData setBaaTime:]
+ -[AKBAAAttestationData setBaaVersion:]
+ -[AKBAAAttestationData setHostBAAAltSignature:]
+ -[AKBAAAttestationData setHostBAACert:]
+ -[AKBAAAttestationData setHostBAAError:]
+ -[AKBAAAttestationData setHostBAASignature:]
+ -[AKBAAAttestationData setInternalDebugTime:]
+ -[AKBAAAttestationData setInternalDigest:]
+ -[AKBAAAttestationData setInternalDigestNoBody:]
+ -[AKBAAAttestationData setIsInternalBuild:]
+ -[AKBAAAttestationData setIsVM:]
+ -[AKBAAAttestationData setMachineID:]
+ -[AKBAAAttestationData setOneTimePassword:]
+ -[AKBAAAttestationData setRoutingInfo:]
+ -[AKBAAAttestationData setSigningError:]
+ -[AKBAAAttestationData setSigningErrorString:]
+ -[AKBAAAttestationData signingErrorString]
+ -[AKBAAAttestationData updateFromAnisetteData:]
+ -[AKConfiguration failureInjectionConfig]
+ -[AKConfiguration setFailureInjectionConfig:]
+ -[AKConfiguration(OSEligibility) isAdultAgeVerificationRequirementStateScreenTime]
+ -[AKConfiguration(OSEligibility) isAgeVerificationRequirementStateScreenTime]
+ -[AKConfiguration(OSEligibility) isChildAndTeenRestrictionRequirementStateMiniBuddy]
+ -[AKConfiguration(OSEligibility) isChildTeenAgeVerificationRequirementStateScreenTime]
+ -[AKConfiguration(OSEligibility) isUnverifiedAdultRestrictionRequirementStateMiniBuddy]
+ -[AKConfiguration(OSEligibility) setIsAdultAgeVerificationRequirementStateScreenTime:]
+ -[AKConfiguration(OSEligibility) setIsAgeVerificationRequirementStateScreenTime:]
+ -[AKConfiguration(OSEligibility) setIsChildAndTeenRestrictionRequirementStateMiniBuddy:]
+ -[AKConfiguration(OSEligibility) setIsChildTeenAgeVerificationRequirementStateScreenTime:]
+ -[AKConfiguration(OSEligibility) setIsUnverifiedAdultRestrictionRequirementStateMiniBuddy:]
+ -[AKCredentialRequestContext _iconSystemName]
+ -[AKCredentialRequestContext set_iconSystemName:]
+ -[AKDevice _chipID]
+ -[AKDevice _deviceUDID]
+ -[AKDevice _ecid]
+ -[AKDevice _generateLocalDeviceUserId]
+ -[AKDevice _generateStableIdForSDID:lduid:]
+ -[AKDevice _generatesecureDeviceIdWhenIsVM:deviceUDID:chipID:ecid:]
+ -[AKDevice localDeviceUserId]
+ -[AKDevice secureDeviceId]
+ -[AKDevice stableId]
+ -[AKDeviceListResponse idmsTrustedDevicesVersion]
+ -[AKDeviceListResponse setIdmsTrustedDevicesVersion:]
+ -[AKFailureInjectionConfig allowedDomains]
+ -[AKFailureInjectionConfig headerRepresentationForRequestURL:]
+ -[AKFailureInjectionConfig scenario]
+ -[AKFailureInjectionConfig systemFailures]
+ -[AKFailureInjectionConfig validationRequirements]
+ -[AKFeatureManager isDBRTwoEnabled]
+ -[AKFeatureManager isProxBAAEnabled]
+ -[AKFeatureManager isTrustedDeviceIdEnabled]
+ -[AKFeatureManager isVMProxBAAEnabled]
+ -[AKHomeDeviceContext .cxx_destruct]
+ -[AKHomeDeviceContext _identifier]
+ -[AKHomeDeviceContext altDSID]
+ -[AKHomeDeviceContext description]
+ -[AKHomeDeviceContext encodeWithCoder:]
+ -[AKHomeDeviceContext initWithAltDSID:operation:parameters:]
+ -[AKHomeDeviceContext initWithCoder:]
+ -[AKHomeDeviceContext operation]
+ -[AKHomeDeviceContext parameters]
+ -[AKHomeDeviceContext setAltDSID:]
+ -[AKHomeDeviceContext set_identifier:]
+ -[AKHomeDeviceController .cxx_destruct]
+ -[AKHomeDeviceController initWithService:]
+ -[AKHomeDeviceController init]
+ -[AKHomeDeviceController removeDevicesWithContext:completion:]
+ -[AKPDPBlobGenerationContext .cxx_destruct]
+ -[AKPDPBlobGenerationContext altDSID]
+ -[AKPDPBlobGenerationContext encodeWithCoder:]
+ -[AKPDPBlobGenerationContext initWithCoder:]
+ -[AKPDPBlobGenerationContext initWithPassword:clientInfo:telemetryFlowID:altDSID:error:]
+ -[AKPDPBlobGenerationContext initWithPassword:verifier:srpSalt:srpSaltData:srpIteration:srpPasswordVersion:srpProtocol:telemetryFlowID:altDSID:]
+ -[AKPDPBlobGenerationContext password]
+ -[AKPDPBlobGenerationContext srpIteration]
+ -[AKPDPBlobGenerationContext srpPasswordVersion]
+ -[AKPDPBlobGenerationContext srpProtocol]
+ -[AKPDPBlobGenerationContext srpSaltData]
+ -[AKPDPBlobGenerationContext srpSalt]
+ -[AKPDPBlobGenerationContext telemetryFlowID]
+ -[AKPDPBlobGenerationContext verifier]
+ -[AKRemoteDevice _initWithInfo:featureManager:]
+ -[AKRemoteDevice initWithInfo:featureManager:]
+ -[AKRemoteDevice secureDeviceId]
+ -[AKRemoteDevice setSecureDeviceId:]
+ -[AKRemoteDevice setTrustedDeviceId:]
+ -[AKRemoteDevice trustedDeviceId]
+ -[AKUserInformation idmsTrustedDevicesVersion]
+ -[AKUserInformation initWithResponseBody:featureManager:]
+ -[AKUserInformation setActiveHMECount:]
+ -[AKUserInformation setIdmsTrustedDevicesVersion:]
+ -[AKUserInformation setInActiveHMECount:]
+ -[AKUserInformation setTrustedDeviceId:]
+ -[AKUserInformation trustedDeviceId]
+ -[NSMutableURLRequest(AuthKit) ak_addLocalDeviceUserIdHeader]
+ -[NSMutableURLRequest(AuthKit) ak_addSDIDHeader]
+ -[NSMutableURLRequest(AuthKit) ak_addStableIdHeader]
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table114
+ GCC_except_table118
+ GCC_except_table140
+ GCC_except_table146
+ GCC_except_table150
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table195
+ GCC_except_table208
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table256
+ GCC_except_table276
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table309
+ GCC_except_table348
+ GCC_except_table354
+ GCC_except_table355
+ GCC_except_table368
+ GCC_except_table369
+ GCC_except_table370
+ GCC_except_table371
+ GCC_except_table372
+ _AKAnisetteCompanionHeaderPrefix
+ _AKAnisetteHeaderPrefix
+ _AKAnisetteProxiedHeaderPrefix
+ _AKAppleIDAuthenticationAppProvidedContextConnectSignedInDependent
+ _AKAppleIDAuthenticationAppProvidedContextHomeDeviceAuth
+ _AKAppleIDAuthenticationAppProvidedContextThirdPartyDeviceAuth
+ _AKAuthenticationThirdPartyDeviceDataKey
+ _AKBAACompanionHeaderPrefix
+ _AKBAAHeaderPrefix
+ _AKBAAProxiedHeaderPrefix
+ _AKClientInfoPasswordVersionKey
+ _AKHomeDeviceOperationRemove
+ _AKHomeKitDeviceIDsKey
+ _AKIDMSCompanionHeaderPrefix
+ _AKIDMSHeaderPrefix
+ _AKIDMSProxiedHeaderPrefix
+ _AKIconSystemNameKey
+ _AKIdMSTrustedDevicesVersionKey
+ _AKOSEDomainAdultAgeVerificationRequiredScreenTime
+ _AKOSEDomainAgeVerificationRequiredScreenTime
+ _AKOSEDomainChildAndTeenRestrictionRequiredMiniBuddy
+ _AKOSEDomainChildTeenAgeVerificationRequiredScreenTime
+ _AKOSEDomainUnverifiedAdultRestrictionRequiredMiniBuddy
+ _AKPasswordIterationKey
+ _AKPasswordProtocolKey
+ _AKPasswordSaltKey
+ _AKRequestHeaderTrueValue
+ _AKRequestInternalErrorHeaderKey
+ _AKRequestInternalTimeInfoHeaderKey
+ _AKRequestMachineTypeHeaderKey
+ _AKRequestMachineTypePhysicalValue
+ _AKRequestMachineTypeVirtualValue
+ _AKRequestSigningHeaderBAACompanionTokenKey
+ _AKRequestSigningHeaderBAADeviceTokenKey
+ _AKRequestSigningHeaderBAAProxiedTokenKey
+ _AKRequestSigningHeaderLocalUserUUIDKey
+ _AKRequestSigningHeaderMIDKey
+ _AKRequestSigningHeaderOTPKey
+ _AKRequestSigningHeaderRoutingInfo
+ _AKSecureDeviceIdKey
+ _AKThirdPartyDeviceDataKey
+ _AKTrustedDeviceIdKey
+ _AKURLBagKeyConnectToFamily
+ _AKURLBagKeyHomeAction
+ _AKURLBagKeyProxBAADisabled
+ _AppleIDAuthSupportCreateVerifier
+ _CMSAttributeParseAppleHashAgilityV2
+ _CMSGetCertificateUsingIssuerSerialNumber
+ _CMSParseEncapsulatedContent
+ _CMSParseSignedData
+ _OBJC_CLASS_$_AKBAAAttestationData
+ _OBJC_CLASS_$_AKFailureInjectionConfig
+ _OBJC_CLASS_$_AKHomeDeviceContext
+ _OBJC_CLASS_$_AKHomeDeviceController
+ _OBJC_CLASS_$_AKPDPBlobGenerationContext
+ _OBJC_CLASS_$_AKPasswordVerifierGenerator
+ _OBJC_IVAR_$_AKAnisetteData._baaAttestationData
+ _OBJC_IVAR_$_AKAppleIDPasskeyAuthenticationController._credentialDataManager
+ _OBJC_IVAR_$_AKAppleIDSession._additionalHeadersForSigning
+ _OBJC_IVAR_$_AKAttestationRequestData._provisionAnisetteIfNeeded
+ _OBJC_IVAR_$_AKAuthorizationPresentationContext._iconSystemName
+ _OBJC_IVAR_$_AKBAAAttestationData._additionalBAAHeaders
+ _OBJC_IVAR_$_AKBAAAttestationData._baaAltSignature
+ _OBJC_IVAR_$_AKBAAAttestationData._baaCert
+ _OBJC_IVAR_$_AKBAAAttestationData._baaDeviceToken
+ _OBJC_IVAR_$_AKBAAAttestationData._baaError
+ _OBJC_IVAR_$_AKBAAAttestationData._baaSignature
+ _OBJC_IVAR_$_AKBAAAttestationData._baaTime
+ _OBJC_IVAR_$_AKBAAAttestationData._baaVersion
+ _OBJC_IVAR_$_AKBAAAttestationData._hostBAAAltSignature
+ _OBJC_IVAR_$_AKBAAAttestationData._hostBAACert
+ _OBJC_IVAR_$_AKBAAAttestationData._hostBAAError
+ _OBJC_IVAR_$_AKBAAAttestationData._hostBAASignature
+ _OBJC_IVAR_$_AKBAAAttestationData._internalDebugTime
+ _OBJC_IVAR_$_AKBAAAttestationData._internalDigest
+ _OBJC_IVAR_$_AKBAAAttestationData._internalDigestNoBody
+ _OBJC_IVAR_$_AKBAAAttestationData._isInternalBuild
+ _OBJC_IVAR_$_AKBAAAttestationData._isVM
+ _OBJC_IVAR_$_AKBAAAttestationData._machineID
+ _OBJC_IVAR_$_AKBAAAttestationData._oneTimePassword
+ _OBJC_IVAR_$_AKBAAAttestationData._routingInfo
+ _OBJC_IVAR_$_AKBAAAttestationData._signingErrorString
+ _OBJC_IVAR_$_AKCredentialRequestContext._iconSystemName
+ _OBJC_IVAR_$_AKDeviceListResponse._idmsTrustedDevicesVersion
+ _OBJC_IVAR_$_AKFeatureManager._cachedIsDBRTwoEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedProxBAAEnabled
+ _OBJC_IVAR_$_AKFeatureManager._cachedVMProxBAAEnabled
+ _OBJC_IVAR_$_AKHomeDeviceContext._altDSID
+ _OBJC_IVAR_$_AKHomeDeviceContext._identifier
+ _OBJC_IVAR_$_AKHomeDeviceContext._operation
+ _OBJC_IVAR_$_AKHomeDeviceContext._parameters
+ _OBJC_IVAR_$_AKHomeDeviceController._authController
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._altDSID
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._password
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._srpIteration
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._srpPasswordVersion
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._srpProtocol
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._srpSalt
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._srpSaltData
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._telemetryFlowID
+ _OBJC_IVAR_$_AKPDPBlobGenerationContext._verifier
+ _OBJC_IVAR_$_AKRemoteDevice._secureDeviceId
+ _OBJC_IVAR_$_AKRemoteDevice._trustedDeviceId
+ _OBJC_IVAR_$_AKUserInformation._idmsTrustedDevicesVersion
+ _OBJC_IVAR_$_AKUserInformation._trustedDeviceId
+ _OBJC_METACLASS_$_AKBAAAttestationData
+ _OBJC_METACLASS_$_AKFailureInjectionConfig
+ _OBJC_METACLASS_$_AKHomeDeviceContext
+ _OBJC_METACLASS_$_AKHomeDeviceController
+ _OBJC_METACLASS_$_AKPDPBlobGenerationContext
+ _OBJC_METACLASS_$_AKPasswordVerifierGenerator
+ __AKAnisetteDataAttestationKey
+ __AKFailureInjectionAllowedDomainsKey
+ __AKFailureInjectionConfigKey
+ __AKFailureInjectionScenarioKey
+ __AKFailureInjectionSystemFailuresKey
+ __AKHTTPHeaderLDUID
+ __AKHTTPHeaderSDID
+ __AKHTTPHeaderStableID
+ __OBJC_$_CLASS_METHODS_AKBAAAttestationData
+ __OBJC_$_CLASS_METHODS_AKHomeDeviceContext
+ __OBJC_$_CLASS_METHODS_AKPDPBlobGenerationContext
+ __OBJC_$_CLASS_METHODS_AKPasswordVerifierGenerator
+ __OBJC_$_CLASS_PROP_LIST_AKBAAAttestationData
+ __OBJC_$_CLASS_PROP_LIST_AKHomeDeviceContext
+ __OBJC_$_CLASS_PROP_LIST_AKPDPBlobGenerationContext
+ __OBJC_$_INSTANCE_METHODS_AKAppleIDAuthenticationContext(SecondFactorSupport|LocationNotificationSupport|Accounts|ThirdPartyDeviceAuth)
+ __OBJC_$_INSTANCE_METHODS_AKBAAAttestationData
+ __OBJC_$_INSTANCE_METHODS_AKFailureInjectionConfig
+ __OBJC_$_INSTANCE_METHODS_AKHomeDeviceContext
+ __OBJC_$_INSTANCE_METHODS_AKHomeDeviceController
+ __OBJC_$_INSTANCE_METHODS_AKPDPBlobGenerationContext
+ __OBJC_$_INSTANCE_VARIABLES_AKBAAAttestationData
+ __OBJC_$_INSTANCE_VARIABLES_AKHomeDeviceContext
+ __OBJC_$_INSTANCE_VARIABLES_AKHomeDeviceController
+ __OBJC_$_INSTANCE_VARIABLES_AKPDPBlobGenerationContext
+ __OBJC_$_PROP_LIST_AKBAAAttestationData
+ __OBJC_$_PROP_LIST_AKFailureInjectionConfig
+ __OBJC_$_PROP_LIST_AKHomeDeviceContext
+ __OBJC_$_PROP_LIST_AKPDPBlobGenerationContext
+ __OBJC_CLASS_PROTOCOLS_$_AKBAAAttestationData
+ __OBJC_CLASS_PROTOCOLS_$_AKHomeDeviceContext
+ __OBJC_CLASS_PROTOCOLS_$_AKPDPBlobGenerationContext
+ __OBJC_CLASS_RO_$_AKBAAAttestationData
+ __OBJC_CLASS_RO_$_AKFailureInjectionConfig
+ __OBJC_CLASS_RO_$_AKHomeDeviceContext
+ __OBJC_CLASS_RO_$_AKHomeDeviceController
+ __OBJC_CLASS_RO_$_AKPDPBlobGenerationContext
+ __OBJC_CLASS_RO_$_AKPasswordVerifierGenerator
+ __OBJC_METACLASS_RO_$_AKBAAAttestationData
+ __OBJC_METACLASS_RO_$_AKFailureInjectionConfig
+ __OBJC_METACLASS_RO_$_AKHomeDeviceContext
+ __OBJC_METACLASS_RO_$_AKHomeDeviceController
+ __OBJC_METACLASS_RO_$_AKPDPBlobGenerationContext
+ __OBJC_METACLASS_RO_$_AKPasswordVerifierGenerator
+ ___101-[AKAppleIDPasskeyAuthenticationController updatePasskeyCredentialWithUserHandle:newName:completion:]_block_invoke
+ ___101-[AKAppleIDPasskeyAuthenticationController updatePasskeyCredentialWithUserHandle:newName:completion:]_block_invoke.73
+ ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.384
+ ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.385
+ ___52-[AKAppleIDServerResourceLoadDelegate _signRequest:]_block_invoke.146
+ ___54+[AKCDPFactory generatePDPBlobWithContext:completion:]_block_invoke
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.364
+ ___62-[AKFailureInjectionConfig headerRepresentationForRequestURL:]_block_invoke
+ ___62-[AKFailureInjectionConfig headerRepresentationForRequestURL:]_block_invoke_2
+ ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.154
+ ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.34
+ ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.366
+ ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.377
+ ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.38
+ ___72-[AKAnisetteProvisioningController refreshBAADeviceTokenWithCompletion:]_block_invoke.35
+ ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.367
+ ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.390
+ ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.380
+ ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.373
+ ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.376
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.76
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.77
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.90
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.91
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.92
+ ___74-[AKAppleIDAuthenticationController performPdpMigrationWithAltDSID:error:]_block_invoke.378
+ ___75-[AKAppleIDAuthenticationController generatePDPBlobWithContext:completion:]_block_invoke
+ ___75-[AKAppleIDAuthenticationController generatePDPBlobWithContext:completion:]_block_invoke.360
+ ___75-[AKAppleIDAuthenticationController generatePDPBlobWithContext:completion:]_block_invoke.361
+ ___77-[AKAnisetteProvisioningController attestationDataForRequestData:completion:]_block_invoke.30
+ ___77-[AKAppleIDAuthenticationController removeHomeDevicesWithContext:completion:]_block_invoke
+ ___77-[AKAppleIDAuthenticationController removeHomeDevicesWithContext:completion:]_block_invoke.391
+ ___77-[AKAppleIDAuthenticationController removeHomeDevicesWithContext:completion:]_block_invoke.392
+ ___78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.31
+ ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.36
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.370
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.371
+ ___80-[AKAppleIDAuthenticationController performPdpCompleteKeyDropWithAltDSID:error:]_block_invoke.379
+ ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.372
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.68
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.69
+ ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.369
+ ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.374
+ ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.368
+ ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.382
+ ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.383
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.98
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.64
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.65
+ ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.375
+ ___block_descriptor_40_e8_32bs_e42_v24?0"AKBAAAttestationData"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e25_B32?0"NSString"8Q16^B24ls32l8
+ ___block_descriptor_56_e8_32bs_e42_v24?0"AKBAAAttestationData"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e42_v24?0"AKBAAAttestationData"8"NSError"16lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e42_v24?0"AKBAAAttestationData"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32bs40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e42_v24?0"AKBAAAttestationData"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs_e42_v24?0"AKBAAAttestationData"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.106
+ ___block_literal_global.148
+ ___block_literal_global.363
+ ___block_literal_global.457
+ ___block_literal_global.735
+ ___block_literal_global.737
+ ___block_literal_global.739
+ ___block_literal_global.741
+ ___block_literal_global.743
+ ___block_literal_global.746
+ ___block_literal_global.748
+ ___block_literal_global.94
+ ___get_ASCredentialDataManagerWrapperClass_block_invoke
+ ___os_log_helper_16_2_3_8_0_8_112_8_64
+ ___os_log_helper_16_2_4_8_64_8_64_8_64_8_64
+ _get_ASCredentialDataManagerWrapperClass
+ _get_ASCredentialDataManagerWrapperClass.softClass
+ _kAKAdultAgeVerificationRequiredScreenTimeDomain
+ _kAKAgeVerificationRequiredScreenTimeDomain
+ _kAKChildAndTeenRestrictionRequiredMiniBuddyDomain
+ _kAKChildTeenAgeVerificationRequiredScreenTimeDomain
+ _kAKPDPBlobGenerationContextAltDSIDKey
+ _kAKPDPBlobGenerationContextPasswordKey
+ _kAKPDPBlobGenerationContextSRPIterationKey
+ _kAKPDPBlobGenerationContextSRPPasswordVersionKey
+ _kAKPDPBlobGenerationContextSRPProtocolKey
+ _kAKPDPBlobGenerationContextSRPSaltBase64Key
+ _kAKPDPBlobGenerationContextSRPSaltDataKey
+ _kAKPDPBlobGenerationContextTelemetryFlowIDKey
+ _kAKPDPBlobGenerationContextVerifierKey
+ _kAKUnverifiedAdultRestrictionRequiredMiniBuddyDomain
+ _objc_msgSend$_addAnisetteHeaders:
+ _objc_msgSend$_addBAAHeaders:
+ _objc_msgSend$_addFailureInjectionHeadersIfNeeded:forRequestURL:
+ _objc_msgSend$_ak_anisetteHeadersWithAnisetteData:midKey:otpKey:routingInfoKey:
+ _objc_msgSend$_chipID
+ _objc_msgSend$_convertedAttestationHeadersForProxiedDevice:
+ _objc_msgSend$_decodeSaltFromBase64:error:
+ _objc_msgSend$_deviceUDID
+ _objc_msgSend$_ecid
+ _objc_msgSend$_generateLocalDeviceUserId
+ _objc_msgSend$_generateStableIdForSDID:lduid:
+ _objc_msgSend$_generateVerifierWithPassword:salt:iteration:protocol:error:
+ _objc_msgSend$_generatesecureDeviceIdWhenIsVM:deviceUDID:chipID:ecid:
+ _objc_msgSend$_iconSystemName
+ _objc_msgSend$_initWithInfo:featureManager:
+ _objc_msgSend$_isValidBAAState
+ _objc_msgSend$additionalBAAHeaders
+ _objc_msgSend$additionalHeadersForSigning
+ _objc_msgSend$ak_addLocalDeviceUserIdHeader
+ _objc_msgSend$ak_addSDIDHeader
+ _objc_msgSend$ak_addStableIdHeader
+ _objc_msgSend$ak_errorsHeaderStringWithMessage
+ _objc_msgSend$allHeaders
+ _objc_msgSend$allowedDomains
+ _objc_msgSend$baaAltSignature
+ _objc_msgSend$baaAttestationData
+ _objc_msgSend$baaCert
+ _objc_msgSend$baaDeviceToken
+ _objc_msgSend$baaError
+ _objc_msgSend$baaSignature
+ _objc_msgSend$baaTime
+ _objc_msgSend$companionAttestationHeaders
+ _objc_msgSend$failureInjectionConfig
+ _objc_msgSend$generatePDPBlobWithCompletion:
+ _objc_msgSend$generatePDPBlobWithContext:completion:
+ _objc_msgSend$generateVerifierForPassword:salt:iteration:protocol:error:
+ _objc_msgSend$headerRepresentationForRequestURL:
+ _objc_msgSend$hostBAAAltSignature
+ _objc_msgSend$hostBAACert
+ _objc_msgSend$hostBAAError
+ _objc_msgSend$hostBAASignature
+ _objc_msgSend$initWithAltDSID:operation:parameters:
+ _objc_msgSend$initWithInfo:featureManager:
+ _objc_msgSend$initWithIsVirtualMachine:isInternalBuild:
+ _objc_msgSend$initWithPassword:verifier:srpSalt:srpSaltData:srpIteration:srpPasswordVersion:srpProtocol:telemetryFlowID:altDSID:
+ _objc_msgSend$initWithResponseBody:featureManager:
+ _objc_msgSend$initWithService:
+ _objc_msgSend$internalDebugTime
+ _objc_msgSend$internalDigest
+ _objc_msgSend$internalDigestNoBody
+ _objc_msgSend$isPhysicalDeviceBAAValidationEnabled
+ _objc_msgSend$isTrustedDeviceIdEnabled
+ _objc_msgSend$isVM
+ _objc_msgSend$localDeviceUserId
+ _objc_msgSend$operation
+ _objc_msgSend$parameters
+ _objc_msgSend$proxiedAttestationHeaders
+ _objc_msgSend$removeHomeDevicesWithContext:completion:
+ _objc_msgSend$reportPublicKeyCredentialUpdateForRelyingPartyIdentifier:userHandle:newName:completionHandler:
+ _objc_msgSend$scenario
+ _objc_msgSend$secureDeviceId
+ _objc_msgSend$setActiveHMECount:
+ _objc_msgSend$setAdditionalHeadersForSigning:
+ _objc_msgSend$setAppProvidedData:
+ _objc_msgSend$setIdmsTrustedDevicesVersion:
+ _objc_msgSend$setInActiveHMECount:
+ _objc_msgSend$setMachineID:
+ _objc_msgSend$setOneTimePassword:
+ _objc_msgSend$setRoutingInfo:
+ _objc_msgSend$setShouldShowNotifications:
+ _objc_msgSend$setSigningErrorString:
+ _objc_msgSend$setTrustedDeviceId:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$signingErrorString
+ _objc_msgSend$stableId
+ _objc_msgSend$stateControllerWithContext:
+ _objc_msgSend$systemFailures
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$updatePasskeyCredentialsWithAltDSID:username:
+ _objc_setProperty_atomic_copy
- -[AKFeatureManager isAppleIDPasskeyFeatureEnabled]
- -[AKFeatureManager refreshServerConfiguration]
- -[AKRemoteDevice _initWithInfo:]
- GCC_except_table104
- GCC_except_table108
- GCC_except_table116
- GCC_except_table144
- GCC_except_table151
- GCC_except_table153
- GCC_except_table154
- GCC_except_table167
- GCC_except_table172
- GCC_except_table180
- GCC_except_table186
- GCC_except_table192
- GCC_except_table194
- GCC_except_table203
- GCC_except_table209
- GCC_except_table218
- GCC_except_table230
- GCC_except_table248
- GCC_except_table251
- GCC_except_table255
- GCC_except_table257
- GCC_except_table296
- GCC_except_table299
- GCC_except_table302
- GCC_except_table321
- GCC_except_table351
- GCC_except_table357
- GCC_except_table358
- _AKRequestHeaderDeviceTokenKey
- _OBJC_IVAR_$_AKFeatureManager._cachedIsAppleIDPasskeyFeatureEnabled
- _OBJC_IVAR_$_AKFeatureManager._cachedServerControlConsentRepromptDisabled
- __OBJC_$_INSTANCE_METHODS_AKAppleIDAuthenticationContext(Accounts|SecondFactorSupport|LocationNotificationSupport)
- ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.381
- ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.382
- ___46-[AKFeatureManager refreshServerConfiguration]_block_invoke
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.361
- ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.152
- ___70-[AKAnisetteProvisioningController resetDeviceIdentityWithCompletion:]_block_invoke.33
- ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.363
- ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.374
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.37
- ___72-[AKAnisetteProvisioningController refreshBAADeviceTokenWithCompletion:]_block_invoke.34
- ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.364
- ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.387
- ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.377
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.370
- ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.373
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.72
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.73
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.84
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.86
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.87
- ___74-[AKAppleIDAuthenticationController performPdpMigrationWithAltDSID:error:]_block_invoke.375
- ___77-[AKAnisetteProvisioningController attestationDataForRequestData:completion:]_block_invoke.29
- ___78-[AKAnisetteProvisioningController _attestationDataForRequestData:completion:]_block_invoke.30
- ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.35
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.367
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.368
- ___80-[AKAppleIDAuthenticationController performPdpCompleteKeyDropWithAltDSID:error:]_block_invoke.376
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.369
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.64
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.65
- ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.366
- ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.371
- ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.365
- ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.379
- ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.380
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.94
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.60
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.61
- ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.372
- ___block_descriptor_40_e8_32bs_e39_v24?0"AKAttestationData"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e20_v24?08"NSError"16ls32l8
- ___block_descriptor_56_e8_32bs_e39_v24?0"AKAttestationData"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40bs48r_e39_v24?0"AKAttestationData"8"NSError"16lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e39_v24?0"AKAttestationData"8"NSError"16ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e39_v24?0"AKAttestationData"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48bs_e39_v24?0"AKAttestationData"8"NSError"16ls32l8s40l8s48l8
- ___block_literal_global.102
- ___block_literal_global.145
- ___block_literal_global.360
- ___block_literal_global.448
- ___block_literal_global.49
- ___block_literal_global.56
- ___block_literal_global.708
- ___block_literal_global.710
- ___block_literal_global.712
- ___block_literal_global.714
- ___block_literal_global.716
- ___block_literal_global.719
- ___block_literal_global.721
- ___block_literal_global.90
- _objc_msgSend$_initWithInfo:
- _objc_msgSend$configurationValueForKey:completion:
- _objc_msgSend$refreshServerConfiguration
CStrings:
+ "\t"
+ "%08X-%016llX"
+ "%@-%@"
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\tcanCreateSimpleProfiles: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\ttrustedDeviceId: %@,\n\tidmsTrustedDevicesVersion: %@, \n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpdpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
+ "<%@: %p; altDSID=%@, operation=%@, parameters=%@>"
+ "<%@:%p> Name: %@, SN: %@, SDID: %@, TrustedDeviceId: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Safety State' %@, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld "
+ "@\"<AKCredentialDataManagerProtocol>\""
+ "@\"<AKHomeDeviceControllerProtocol>\""
+ "@\"AKBAAAttestationData\""
+ "@24@0:8B16B20"
+ "@40@0:8B16@20I28Q32"
+ "@56@0:8@16@24@32@40^@48"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "ADULT_AGE_VERIFICATION_REQUIRED_SCREEN_TIME"
+ "AGE_VERIFICATION_REQUIRED_SCREEN_TIME"
+ "AKAnisetteData <%p>: {MID: %@ - OTP: %@ - RD: %@}, attestation - %@"
+ "AKAttestationRequestData: provision: %@, signingDataHash: %@, headers: %@"
+ "AKBAAAttestationData"
+ "AKFailureInjectionConfig"
+ "AKHomeDeviceContext"
+ "AKHomeDeviceController"
+ "AKHomeDeviceController - Removing %lu home devices for altDSID: %{mask.hash}@"
+ "AKPDPBlobGenerationContext"
+ "AKPasswordVerifierGenerator"
+ "Adult age verification required - setting AKOSEOptionRequireVerification flag"
+ "Attempting to create PDPBlobGenerationContext with SRP parameters in clientInfo - salt: %@, iteration: %@, version: %@, protocol: %@"
+ "B32@?0@\"NSString\"8Q16^B24"
+ "BAA Attesation data not available. Using pre-baa implementation headers for companion headers."
+ "BAA Attesation data not available. Using pre-baa implementation headers for proxied headers."
+ "BEGIN [%lld]: PDPBlobGeneration  enableTelemetry=YES "
+ "BEGIN [%lld]: RemoveHomeDevices  enableTelemetry=YES "
+ "CHILD_AND_TEEN_RESTRICTION_REQUIRED_MINI_BUDDY"
+ "CHILD_TEEN_AGE_VERIFICATION_REQUIRED_SCREEN_TIME"
+ "Calling out to remote auth service for PDP blob generation with altDSID: %{mask.hash}@"
+ "Calling out to remote auth service to removeHomeDevicesWithContext: %@"
+ "ChipID"
+ "CloudServices"
+ "CoreCDP stateController does not support generatePDPBlobWithCompletion:"
+ "DBR_TWO"
+ "Device IDs are required"
+ "END [%lld] %fs:PDPBlobGeneration  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "END [%lld] %fs:RemoveHomeDevices "
+ "Encountered incomplete Anisette data for device! %@"
+ "Encountered incomplete Anisette info! { M: %@, O: %@, R: %@ }"
+ "Exception caught while getting trusted device id: %@"
+ "Exception caught while setting trusted device id: %@"
+ "Failed to add \"%@\" header - localDeviceUserId is nil"
+ "Failed to add \"%@\" header - secureDeviceId is nil"
+ "Failed to add \"%@\" header - stableId is nil"
+ "Failed to convert userHandle to data"
+ "Failed to decode password salt from base64 string"
+ "Failed to generate SRP verifier: %@"
+ "Failed to generate stableId - SDID: %@, LDUID: %{mask.hash}@"
+ "Failed to get ChipID (%i) or ECID (%llu) for secureDeviceId"
+ "Failed to get UniqueDeviceID for virtual machine secureDeviceId"
+ "Failed to update passkey - Missing newName"
+ "Failed to update passkey - Missing userHandle"
+ "Failed to update passkey credential with error: %{private}@"
+ "Feature DBR_TWO enabled - %@"
+ "Feature ProximityBAA enabled - %@"
+ "Feature VMProximityBAA enabled - %@"
+ "Features mask value: %lu"
+ "Found BAA attestation data. Using it for getting companion headers."
+ "Found BAA attestation data. Using it for getting proxied headers."
+ "Generating SRP verifier with all required inputs present"
+ "Home device context is required"
+ "I16@0:8"
+ "Invalid state found, sending no BAA headers."
+ "LOCAL-USER-EMBEDDED"
+ "Missing SRP parameter(s) in clientInfo"
+ "Missing required inputs for verifier generation - password: %@, salt: %@, iteration: %@, protocol: %@"
+ "No altDSID available for account"
+ "PDP blob generation completed successfully"
+ "PDP blob generation completed with blob length=%lu error=%@"
+ "PDP blob generation failed: %@"
+ "PDP blob generation not supported"
+ "PDPBlobGeneration"
+ "Passkey credential update skipped: feature not enabled or platform not supported"
+ "Password is nil or empty - cannot generate PDP blob"
+ "ProximityBAA"
+ "Remote authentication service returned an error for removeHomeDevicesWithContext: %{public}@"
+ "Remove home devices completed successfully"
+ "Remove home devices failed with error: %{public}@"
+ "Remove home devices failed: %{public}@"
+ "Remove home devices failed: altDSID is required"
+ "Remove home devices failed: hkdIDs are required"
+ "RemoveHomeDevices"
+ "Result of remote PDP blob generation call - blob length: %lu, error: %@"
+ "SRP verifier generated successfully - %@"
+ "Successfully decoded salt from base64 - %@"
+ "Successfully generated SRP verifier"
+ "Successfully updated passkey credential for userHandle: %{mask.hash}@"
+ "T@\"AKBAAAttestationData\",&,N,V_baaAttestationData"
+ "T@\"NSArray\",C,N,V_additionalHeadersForSigning"
+ "T@\"NSData\",R,V_srpSaltData"
+ "T@\"NSData\",R,V_verifier"
+ "T@\"NSDictionary\",R,C"
+ "T@\"NSDictionary\",R,C,N,V_parameters"
+ "T@\"NSNumber\",C,N,V_activeHMECount"
+ "T@\"NSNumber\",C,N,V_inActiveHMECount"
+ "T@\"NSNumber\",R,V_srpIteration"
+ "T@\"NSNumber\",R,V_srpPasswordVersion"
+ "T@\"NSString\",C,N,V_iconSystemName"
+ "T@\"NSString\",C,N,V_idmsTrustedDevicesVersion"
+ "T@\"NSString\",C,N,V_secureDeviceId"
+ "T@\"NSString\",C,N,V_trustedDeviceId"
+ "T@\"NSString\",C,V_additionalBAAHeaders"
+ "T@\"NSString\",C,V_baaAltSignature"
+ "T@\"NSString\",C,V_baaCert"
+ "T@\"NSString\",C,V_baaDeviceToken"
+ "T@\"NSString\",C,V_baaError"
+ "T@\"NSString\",C,V_baaSignature"
+ "T@\"NSString\",C,V_baaTime"
+ "T@\"NSString\",C,V_baaVersion"
+ "T@\"NSString\",C,V_hostBAAAltSignature"
+ "T@\"NSString\",C,V_hostBAACert"
+ "T@\"NSString\",C,V_hostBAAError"
+ "T@\"NSString\",C,V_hostBAASignature"
+ "T@\"NSString\",C,V_internalDebugTime"
+ "T@\"NSString\",C,V_internalDigest"
+ "T@\"NSString\",C,V_internalDigestNoBody"
+ "T@\"NSString\",C,V_machineID"
+ "T@\"NSString\",C,V_oneTimePassword"
+ "T@\"NSString\",C,V_signingErrorString"
+ "T@\"NSString\",R,C,N,V_iconSystemName"
+ "T@\"NSString\",R,C,N,V_operation"
+ "T@\"NSString\",R,V_altDSID"
+ "T@\"NSString\",R,V_password"
+ "T@\"NSString\",R,V_srpProtocol"
+ "T@\"NSString\",R,V_srpSalt"
+ "T@\"NSString\",R,V_telemetryFlowID"
+ "TB,N,V_isInternalBuild"
+ "TB,N,V_isVM"
+ "TB,N,V_provisionAnisetteIfNeeded"
+ "TB,R,N,GisDBRTwoEnabled"
+ "TB,R,N,GisProxBAAEnabled"
+ "TB,R,N,GisTrustedDeviceIdEnabled"
+ "TB,R,N,GisVMProxBAAEnabled"
+ "TQ,V_routingInfo"
+ "Teen attached to family required - setting AKOSEOptionRequireTeenAttachedToFamily flag"
+ "ThirdPartyDeviceAuth"
+ "TrustedDeviceId"
+ "UNVERIFIED_ADULT_RESTRICTION_REQUIRED_MINI_BUDDY"
+ "UniqueChipID"
+ "VMProximityBAA"
+ "X-Apple-I"
+ "X-Apple-I-Companion"
+ "X-Apple-I-LDUID"
+ "X-Apple-I-Proxied"
+ "X-Apple-I-SDID"
+ "X-Apple-I-Stable-ID"
+ "X-Apple-I-Test-Behavior-"
+ "X-Apple-I-Test-Scenario"
+ "_AKConfigKeyVMType"
+ "_AKFailureInjectionConfig"
+ "_ASCredentialDataManagerWrapper"
+ "_addAnisetteHeaders:"
+ "_addBAAHeaders:"
+ "_addFailureInjectionHeadersIfNeeded:forRequestURL:"
+ "_additionalBAAHeaders"
+ "_additionalHeadersForSigning"
+ "_ak_anisetteHeadersWithAnisetteData:midKey:otpKey:routingInfoKey:"
+ "_attestationData"
+ "_baaAltSignature"
+ "_baaAttestationData"
+ "_baaCert"
+ "_baaDeviceToken"
+ "_baaError"
+ "_baaSignature"
+ "_baaTime"
+ "_baaVersion"
+ "_cachedIsDBRTwoEnabled"
+ "_cachedProxBAAEnabled"
+ "_cachedVMProxBAAEnabled"
+ "_chipID"
+ "_convertedAttestationHeadersForProxiedDevice:"
+ "_credentialDataManager"
+ "_decodeSaltFromBase64:error:"
+ "_deviceUDID"
+ "_ecid"
+ "_generateLocalDeviceUserId"
+ "_generateStableIdForSDID:lduid:"
+ "_generateVerifierWithPassword:salt:iteration:protocol:error:"
+ "_generatesecureDeviceIdWhenIsVM:deviceUDID:chipID:ecid:"
+ "_hostBAAAltSignature"
+ "_hostBAACert"
+ "_hostBAAError"
+ "_hostBAASignature"
+ "_iconSystemName"
+ "_idmsTrustedDevicesVersion"
+ "_initWithInfo:featureManager:"
+ "_internalDebugTime"
+ "_internalDigest"
+ "_internalDigestNoBody"
+ "_isInternalBuild"
+ "_isVM"
+ "_isValidBAAState"
+ "_parameters"
+ "_provisionAnisetteIfNeeded"
+ "_secureDeviceId"
+ "_setCredentialDataManager:"
+ "_signingErrorString"
+ "_srpIteration"
+ "_srpPasswordVersion"
+ "_srpSalt"
+ "_srpSaltData"
+ "_trustedDeviceId"
+ "additionalBAAHeaders"
+ "additionalHeadersForSigning"
+ "ak_addLocalDeviceUserIdHeader"
+ "ak_addSDIDHeader"
+ "ak_addStableIdHeader"
+ "allHeaders"
+ "allowedDomains"
+ "anisetteHeaders"
+ "authkit/pdp-blob-generation"
+ "authkit/remove-home-devices"
+ "baaAltSignature"
+ "baaAttestationData"
+ "baaAttestationHeaders"
+ "baaCert"
+ "baaDeviceToken"
+ "baaError"
+ "baaSignature"
+ "baaTime"
+ "baaVersion"
+ "companionAttestationHeaders"
+ "configureForThirdPartyDeviceAuthWithAppProvidedData:"
+ "connectSignedInDependent"
+ "connectToFamily"
+ "contextForRemovalWithAltDSID:hkdIDs:"
+ "dbrTwoEnabled"
+ "disableProxBAA"
+ "failureInjectionConfig"
+ "generatePDPBlobWithCompletion:"
+ "generatePDPBlobWithContext called"
+ "generatePDPBlobWithContext:completion:"
+ "generateVerifierForPassword:salt:iteration:protocol:error:"
+ "headerRepresentationForRequestURL:"
+ "headersForSigning"
+ "hkdIds"
+ "homeAction"
+ "homeDeviceAuth"
+ "hostBAAAltSignature"
+ "hostBAACert"
+ "hostBAAError"
+ "hostBAASignature"
+ "iconSystemName"
+ "idmsTDLVersion"
+ "idmsTrustedDevicesVersion"
+ "idmsTrustedDevicesVersionForAccount:"
+ "initWithAltDSID:operation:parameters:"
+ "initWithInfo:featureManager:"
+ "initWithIsVirtualMachine:isInternalBuild:"
+ "initWithPassword:clientInfo:telemetryFlowID:altDSID:error:"
+ "initWithPassword:verifier:srpSalt:srpSaltData:srpIteration:srpPasswordVersion:srpProtocol:telemetryFlowID:altDSID:"
+ "initWithResponseBody:featureManager:"
+ "initWithService:"
+ "internalDebugTime"
+ "internalDigest"
+ "internalDigestNoBody"
+ "isAdultAgeVerificationRequirementStateScreenTime"
+ "isAgeVerificationRequirementStateScreenTime"
+ "isChildAndTeenRestrictionRequirementStateMiniBuddy"
+ "isChildTeenAgeVerificationRequirementStateScreenTime"
+ "isDBRTwoEnabled"
+ "isProxBAAEnabled"
+ "isTrustedDeviceIdEnabled"
+ "isUnverifiedAdultRestrictionRequirementStateMiniBuddy"
+ "isVM"
+ "isVMProxBAAEnabled"
+ "localDeviceUserId"
+ "parameters"
+ "passwordIteration"
+ "passwordSalt"
+ "present"
+ "protocol"
+ "provisionAnisetteIfNeeded"
+ "proxBAAEnabled"
+ "proxiedAttestationHeaders"
+ "remove"
+ "removeDevicesWithContext:completion:"
+ "removeHomeDevicesWithContext:completion:"
+ "reportPublicKeyCredentialUpdateForRelyingPartyIdentifier:userHandle:newName:completionHandler:"
+ "scenario"
+ "secureDeviceId"
+ "setActiveHMECount:"
+ "setAdditionalBAAHeaders:"
+ "setAdditionalHeadersForSigning:"
+ "setBaaAltSignature:"
+ "setBaaAttestationData:"
+ "setBaaCert:"
+ "setBaaDeviceToken:"
+ "setBaaError:"
+ "setBaaSignature:"
+ "setBaaTime:"
+ "setBaaVersion:"
+ "setFailureInjectionConfig:"
+ "setHostBAAAltSignature:"
+ "setHostBAACert:"
+ "setHostBAAError:"
+ "setHostBAASignature:"
+ "setIdMSTrustedDevicesVersion:forAccount:"
+ "setIdmsTrustedDevicesVersion:"
+ "setInActiveHMECount:"
+ "setInternalDebugTime:"
+ "setInternalDigest:"
+ "setInternalDigestNoBody:"
+ "setIsAdultAgeVerificationRequirementStateScreenTime:"
+ "setIsAgeVerificationRequirementStateScreenTime:"
+ "setIsChildAndTeenRestrictionRequirementStateMiniBuddy:"
+ "setIsChildTeenAgeVerificationRequirementStateScreenTime:"
+ "setIsInternalBuild:"
+ "setIsUnverifiedAdultRestrictionRequirementStateMiniBuddy:"
+ "setIsVM:"
+ "setProvisionAnisetteIfNeeded:"
+ "setSecureDeviceId:"
+ "setShouldShowNotifications:"
+ "setSigningError:"
+ "setSigningErrorString:"
+ "setTrustedDeviceId:"
+ "setTrustedDeviceId:forAccount:"
+ "setWithObject:"
+ "set_iconSystemName:"
+ "signingErrorString"
+ "srpIteration"
+ "srpPasswordVersion"
+ "srpSalt"
+ "srpSaltBase64"
+ "srpSaltData"
+ "stableId"
+ "systemFailures"
+ "thirdPartyDeviceAuth"
+ "thirdPartyDeviceData"
+ "tpdd"
+ "trustedDeviceId"
+ "trustedDeviceIdEnabled"
+ "trustedDeviceIdForAccount:"
+ "unsignedLongValue"
+ "updateFromAnisetteData:"
+ "updatePasskeyCredentialWithUserHandle:newName:completion:"
+ "updatePasskeyCredentialsWithAltDSID:username:"
+ "v24@?0@\"AKBAAAttestationData\"8@\"NSError\"16"
+ "v32@0:8@\"AKAttestationRequestData\"16@?<v@?@\"AKBAAAttestationData\"@\"NSError\">24"
+ "v32@0:8@\"AKHomeDeviceContext\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"AKPDPBlobGenerationContext\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "vmProxBAAEnabled"
+ "x-apple-baa"
+ "x-apple-baa-companion"
+ "x-apple-baa-proxied"
+ "x-apple-companion-device-token"
+ "x-apple-debug-baa-error"
+ "x-apple-debug-time-info"
+ "x-apple-i"
+ "x-apple-i-companion"
+ "x-apple-i-device-type"
+ "x-apple-i-proxied"
+ "x-apple-proxied-device-token"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\tcanCreateSimpleProfiles: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpdpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
- "<%@:%p> Name: %@, SN: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Safety State' %@, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld "
- "AKAnisetteData <%p>: {MID: %@ - OTP: %@ - RD: %@}"
- "AKAttestationRequestData: signingDataHash: %@, headers: %@"
- "AppleIDPasskey"
- "Encountered incomplete Anisette data for proxied device! %@"
- "Encountered incomplete companion Anisette data! %@"
- "Failed to fetch server configuration for consent reprompt: %@"
- "Feature AppleIDPasskey is supported. Is AppleIDPasskey enabled - %@"
- "Privacy version saving disabled by server configuration"
- "T@\"NSNumber\",R,C,N,V_activeHMECount"
- "T@\"NSNumber\",R,C,N,V_inActiveHMECount"
- "TB,R,N,GisAppleIDPasskeyFeatureEnabled"
- "Updated server configuration for consent reprompt disabled: %@"
- "_cachedIsAppleIDPasskeyFeatureEnabled"
- "_cachedServerControlConsentRepromptDisabled"
- "_initWithInfo:"
- "appleIDPasskeyFeatureEnabled"
- "isAppleIDPasskeyFeatureEnabled"
- "refreshServerConfiguration"
- "v32@0:8@\"AKAttestationRequestData\"16@?<v@?@\"AKAttestationData\"@\"NSError\">24"

```
