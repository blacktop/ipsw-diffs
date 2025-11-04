## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.127.1.2.0
-  __TEXT.__text: 0x178b88
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0xdac4
-  __TEXT.__const: 0x69c8
-  __TEXT.__cstring: 0xf57f
-  __TEXT.__oslogstring: 0x118e3
-  __TEXT.__gcc_except_tab: 0x9ae8
+525.250.4.0.0
+  __TEXT.__text: 0x185030
+  __TEXT.__auth_stubs: 0xc10
+  __TEXT.__objc_methlist: 0xe494
+  __TEXT.__const: 0x69f8
+  __TEXT.__cstring: 0xfc0e
+  __TEXT.__gcc_except_tab: 0xa06c
+  __TEXT.__oslogstring: 0x128aa
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4050
-  __TEXT.__objc_classname: 0x1c33
-  __TEXT.__objc_methname: 0x220ca
-  __TEXT.__objc_methtype: 0x4655
-  __TEXT.__objc_stubs: 0xf760
-  __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0xa048
-  __DATA_CONST.__objc_classlist: 0x628
+  __TEXT.__unwind_info: 0x4260
+  __TEXT.__objc_classname: 0x1d7c
+  __TEXT.__objc_methname: 0x235c8
+  __TEXT.__objc_methtype: 0x47c0
+  __TEXT.__objc_stubs: 0xff40
+  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__const: 0xa318
+  __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f68
+  __DATA_CONST.__objc_selrefs: 0x7370
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x3e0
+  __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH_CONST.__const: 0x1320
-  __AUTH_CONST.__cfstring: 0xfc80
-  __AUTH_CONST.__objc_const: 0x25270
+  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__const: 0x1400
+  __AUTH_CONST.__cfstring: 0x10460
+  __AUTH_CONST.__objc_const: 0x26648
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
-  __AUTH.__objc_data: 0x28a0
-  __DATA.__objc_ivar: 0xfcc
+  __AUTH.__objc_data: 0x2c10
+  __DATA.__objc_ivar: 0x1068
   __DATA.__data: 0x1900
-  __DATA.__bss: 0x6e0
+  __DATA.__bss: 0x6f0
   __DATA_DIRTY.__objc_data: 0x14f0
-  __DATA_DIRTY.__bss: 0x2a0
+  __DATA_DIRTY.__bss: 0x2b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F58324DC-E428-37BF-87BE-935242D71057
-  Functions: 5327
-  Symbols:   20229
-  CStrings:  11741
+  UUID: C3DDEAD1-6593-3B7D-9209-02BB105FF9BE
+  Functions: 5539
+  Symbols:   20951
+  CStrings:  12153
 
Symbols:
+ +[AKOSEligibilityManager sharedManager]
+ +[AKSimpleProfileContext decodingClasses]
+ +[AKSimpleProfileContext supportsSecureCoding]
+ +[AKSimpleProfileContextCreate supportsSecureCoding]
+ +[AKSimpleProfileContextEdit supportsSecureCoding]
+ +[AKSimpleProfileContextUpgrade supportsSecureCoding]
+ +[NSError(AuthKit) ak_accountPrivacyConsentErrorWithCode:]
+ -[AKAccountManager _handleSaveResult:version:error:]
+ -[AKAccountManager _minimumConsentVersionForIdentifiableTelemetry]
+ -[AKAccountManager _setConsentVersionProperty:forAccount:error:]
+ -[AKAccountManager _shouldEnableIdentifiableTelemetryForConsentVersion:]
+ -[AKAccountManager _validateConsentVersion:error:]
+ -[AKAccountManager canCreateSimpleProfilesForAccount:]
+ -[AKAccountManager geoChangeRegisteredForAccount:]
+ -[AKAccountManager identifiableTelemetryAllowedForAccount:]
+ -[AKAccountManager matchingServiceAccountForAuthKitAccount:service:]
+ -[AKAccountManager safetyScreenSeenForAccount:]
+ -[AKAccountManager setAppleAccountConsentVersion:forAccount:error:]
+ -[AKAccountManager setCanCreateSimpleProfiles:forAccount:]
+ -[AKAccountManager setGeoChangeRegistered:forAccount:]
+ -[AKAccountManager setSafetyScreenSeen:forAccount:]
+ -[AKAccountManager simpleProfileAuthTokenForAccount:]
+ -[AKAppleIDAuthenticationContext appleAccountPrivacyBundleVersion]
+ -[AKAppleIDAuthenticationContext isConfiguredForProfileAuthentication]
+ -[AKAppleIDAuthenticationContext needsNewSimpleProfile]
+ -[AKAppleIDAuthenticationContext privacyBundleVersion]
+ -[AKAppleIDAuthenticationContext pvkToken]
+ -[AKAppleIDAuthenticationContext setAppleAccountPrivacyBundleVersion:]
+ -[AKAppleIDAuthenticationContext setPrivacyBundleVersion:]
+ -[AKAppleIDAuthenticationContext setPvkToken:]
+ -[AKAppleIDAuthenticationContext setSimpleProfileContext:]
+ -[AKAppleIDAuthenticationContext setTeenRequiredToConnectToFamily:]
+ -[AKAppleIDAuthenticationContext simpleProfileContext]
+ -[AKAppleIDAuthenticationContext teenRequiredToConnectToFamily]
+ -[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]
+ -[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]
+ -[AKAppleIDServerResourceLoadDelegate pvkToken]
+ -[AKAppleIDServerResourceLoadDelegate setPvkToken:]
+ -[AKAuthenticatableResource customShieldDetailText]
+ -[AKAuthenticatableResource customShieldTitle]
+ -[AKAuthenticatableResource setCustomShieldDetailText:]
+ -[AKAuthenticatableResource setCustomShieldTitle:]
+ -[AKConfiguration(OSEligibility) isAdultAgeVerificationRequirementStateMiniBuddy]
+ -[AKConfiguration(OSEligibility) isAdultAgeVerificationRequirementState]
+ -[AKConfiguration(OSEligibility) isGuardianAgeVerificationRequirementStateMiniBuddy]
+ -[AKConfiguration(OSEligibility) isGuardianAgeVerificationRequirementState]
+ -[AKConfiguration(OSEligibility) isTeenAttachedToFamilyRequirementState]
+ -[AKConfiguration(OSEligibility) isU18RestrictionRequirementState]
+ -[AKConfiguration(OSEligibility) isUnverifiedAdultRestrictionRequirementState]
+ -[AKConfiguration(OSEligibility) osEligibilityConfigValueForKey:]
+ -[AKConfiguration(OSEligibility) setIsAdultAgeVerificationRequirementState:]
+ -[AKConfiguration(OSEligibility) setIsAdultAgeVerificationRequirementStateMiniBuddy:]
+ -[AKConfiguration(OSEligibility) setIsGuardianAgeVerificationRequirementState:]
+ -[AKConfiguration(OSEligibility) setIsGuardianAgeVerificationRequirementStateMiniBuddy:]
+ -[AKConfiguration(OSEligibility) setIsTeenAttachedToFamilyRequirementState:]
+ -[AKConfiguration(OSEligibility) setIsU18RestrictionRequirementState:]
+ -[AKConfiguration(OSEligibility) setIsUnverifiedAdultRestrictionRequirementState:]
+ -[AKConfiguration(OSEligibility) setShouldFakeOSEligibility:]
+ -[AKConfiguration(OSEligibility) shouldFakeOSEligibility]
+ -[AKFeatureManager isPrivacyVersionSavingEnabled]
+ -[AKFeatureManager isSimpleProfilesEnabled]
+ -[AKFeatureManager shouldForceEnableSimpleProfilesUpgradeQR]
+ -[AKOSEligibilityManager _domainForString:]
+ -[AKOSEligibilityManager _isEligibleForDomain:]
+ -[AKOSEligibilityManager _isEnabledForDomain:]
+ -[AKOSEligibilityManager _stringForDomain:]
+ -[AKOSEligibilityManager _stringFromXPCArray:logPrefix:]
+ -[AKOSEligibilityManager eligibilityAnswerForDomain:]
+ -[AKOSEligibilityManager eligibilityAnswerForDomain:context:status:]
+ -[AKOSEligibilityManager featuresMaskValue]
+ -[AKOSEligibilityManager isAdultAgeVerificationRequiredMiniBuddy]
+ -[AKOSEligibilityManager isAdultAgeVerificationRequired]
+ -[AKOSEligibilityManager isEligibleForDomain:]
+ -[AKOSEligibilityManager isGuardianAgeVerificationRequiredMiniBuddy]
+ -[AKOSEligibilityManager isGuardianAgeVerificationRequired]
+ -[AKOSEligibilityManager isTeenAttachedToFamilyRequired]
+ -[AKOSEligibilityManager isU18RestrictionRequired]
+ -[AKOSEligibilityManager isUnverifiedAdultRestrictionRequired]
+ -[AKOSEligibilityManager refreshPolicies:]
+ -[AKOSEligibilityManager regulatoryCountryRegions]
+ -[AKSimpleProfileContext .cxx_destruct]
+ -[AKSimpleProfileContext _identifier]
+ -[AKSimpleProfileContext altDSID]
+ -[AKSimpleProfileContext encodeWithCoder:]
+ -[AKSimpleProfileContext initWithAltDSID:]
+ -[AKSimpleProfileContext initWithCoder:]
+ -[AKSimpleProfileContext setAltDSID:]
+ -[AKSimpleProfileContext set_identifier:]
+ -[AKSimpleProfileContextCreate .cxx_destruct]
+ -[AKSimpleProfileContextCreate ageCategory]
+ -[AKSimpleProfileContextCreate encodeWithCoder:]
+ -[AKSimpleProfileContextCreate imageID]
+ -[AKSimpleProfileContextCreate initWithCoder:]
+ -[AKSimpleProfileContextCreate initWithProfileName:sponsorAltDSID:imageID:ageCategory:]
+ -[AKSimpleProfileContextCreate profileName]
+ -[AKSimpleProfileContextCreate setAgeCategory:]
+ -[AKSimpleProfileContextCreate setImageID:]
+ -[AKSimpleProfileContextCreate setProfileName:]
+ -[AKSimpleProfileContextCreate sponsorAltDSID]
+ -[AKSimpleProfileContextDelete initWithAltDSID:]
+ -[AKSimpleProfileContextEdit .cxx_destruct]
+ -[AKSimpleProfileContextEdit ageCategory]
+ -[AKSimpleProfileContextEdit encodeWithCoder:]
+ -[AKSimpleProfileContextEdit imageID]
+ -[AKSimpleProfileContextEdit initWithAltDSID:]
+ -[AKSimpleProfileContextEdit initWithCoder:]
+ -[AKSimpleProfileContextEdit profileName]
+ -[AKSimpleProfileContextEdit setAgeCategory:]
+ -[AKSimpleProfileContextEdit setImageID:]
+ -[AKSimpleProfileContextEdit setProfileName:]
+ -[AKSimpleProfileContextUpgrade .cxx_destruct]
+ -[AKSimpleProfileContextUpgrade encodeWithCoder:]
+ -[AKSimpleProfileContextUpgrade followUpItemIdentifier]
+ -[AKSimpleProfileContextUpgrade initWithAltDSID:followUpIdentifier:]
+ -[AKSimpleProfileContextUpgrade initWithCoder:]
+ -[AKSimpleProfileContextUpgrade setFollowUpItemIdentifier:]
+ -[AKSimpleProfileContextUpgrade sponsorAltDSID]
+ -[AKSimpleProfileImageResponseGroup .cxx_destruct]
+ -[AKSimpleProfileImageResponseGroup groupTitle]
+ -[AKSimpleProfileImageResponseGroup images]
+ -[AKSimpleProfileImageResponseGroup parseValue:atKey:]
+ -[AKSimpleProfileImageResponseGroup setGroupTitle:]
+ -[AKSimpleProfileImageResponseGroup setImages:]
+ -[AKSimpleProfileImageResponseGroup validationRequirements]
+ -[AKSimpleProfileImageResponseImageMetadata .cxx_destruct]
+ -[AKSimpleProfileImageResponseImageMetadata imageDescription]
+ -[AKSimpleProfileImageResponseImageMetadata imageID]
+ -[AKSimpleProfileImageResponseImageMetadata imageURL]
+ -[AKSimpleProfileImageResponseImageMetadata setImageDescription:]
+ -[AKSimpleProfileImageResponseImageMetadata setImageID:]
+ -[AKSimpleProfileImageResponseImageMetadata setImageURL:]
+ -[AKSimpleProfileImageResponseImageMetadata validationRequirements]
+ -[AKSimpleProfileImagesResponse .cxx_destruct]
+ -[AKSimpleProfileImagesResponse description]
+ -[AKSimpleProfileImagesResponse imageGroups]
+ -[AKSimpleProfileImagesResponse parseValue:atKey:]
+ -[AKSimpleProfileImagesResponse setImageGroups:]
+ -[AKSimpleProfileImagesResponse validationRequirements]
+ -[AKSimpleProfileManager .cxx_destruct]
+ -[AKSimpleProfileManager _sendNotificationForProfilesDidChange]
+ -[AKSimpleProfileManager _setProfiles:forAccount:]
+ -[AKSimpleProfileManager account:isSponsorForProfile:]
+ -[AKSimpleProfileManager accountManager]
+ -[AKSimpleProfileManager authContextWithSponsor:simpleProfileContext:]
+ -[AKSimpleProfileManager canCreateSimpleProfilesForAccount:]
+ -[AKSimpleProfileManager featureManager]
+ -[AKSimpleProfileManager fetchUpgradeURLForSponsor:forSimpleProfile:completion:]
+ -[AKSimpleProfileManager initWithAccountManager:urlBag:urlSession:featureManager:]
+ -[AKSimpleProfileManager init]
+ -[AKSimpleProfileManager isQRCodeEnabledWithCompletion:]
+ -[AKSimpleProfileManager primaryAccountIsSponsorForProfile:]
+ -[AKSimpleProfileManager profileImageURLsWithCompletion:]
+ -[AKSimpleProfileManager profileImagesDataWithCompletion:]
+ -[AKSimpleProfileManager profileImagesWithCompletion:]
+ -[AKSimpleProfileManager setAccountManager:]
+ -[AKSimpleProfileManager setFeatureManager:]
+ -[AKSimpleProfileManager setUrlBag:]
+ -[AKSimpleProfileManager setUrlSession:]
+ -[AKSimpleProfileManager simpleProfilesForAccount:]
+ -[AKSimpleProfileManager simpleProfilesForPrimaryAccount]
+ -[AKSimpleProfileManager sortedProfilesFromArray:]
+ -[AKSimpleProfileManager urlBag]
+ -[AKSimpleProfileManager urlSession]
+ -[AKSimpleProfileModel .cxx_destruct]
+ -[AKSimpleProfileModel DSID]
+ -[AKSimpleProfileModel ageCategory]
+ -[AKSimpleProfileModel altDSID]
+ -[AKSimpleProfileModel imageID]
+ -[AKSimpleProfileModel imageId]
+ -[AKSimpleProfileModel imageURL]
+ -[AKSimpleProfileModel profileName]
+ -[AKSimpleProfileModel setAgeCategory:]
+ -[AKSimpleProfileModel setAltDSID:]
+ -[AKSimpleProfileModel setDSID:]
+ -[AKSimpleProfileModel setImageID:]
+ -[AKSimpleProfileModel setImageId:]
+ -[AKSimpleProfileModel setImageURL:]
+ -[AKSimpleProfileModel setProfileName:]
+ -[AKSimpleProfileModel setSponsorAltDSID:]
+ -[AKSimpleProfileModel sponsorAltDSID]
+ -[AKSimpleProfileModel validationRequirements]
+ -[AKURLSession beginAuthenticationDataTaskWithRequest:serviceErrorHandler:completionHandler:]
+ -[AKURLSession handleAuthenticationResponse:forRequest:forDataTask:withData:error:serviceErrorHandler:completionHandler:]
+ -[AKUserInformation canCreateSimpleProfiles]
+ -[AKUserInformation safetyScreenSeen]
+ -[AKUserInformation setCanCreateSimpleProfiles:]
+ -[AKUserInformation setSafetyScreenSeen:]
+ -[AKUserInformation setSimpleProfiles:]
+ -[AKUserInformation simpleProfiles]
+ -[NSMutableURLRequest(AuthKit) ak_addOSEligibilityHeader]
+ -[NSMutableURLRequest(AuthKit) ak_addOSEligibilityRegionHeader]
+ -[NSMutableURLRequest(AuthKit) ak_addPVKToken:]
+ GCC_except_table110
+ GCC_except_table130
+ GCC_except_table131
+ GCC_except_table132
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table146
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table176
+ GCC_except_table182
+ GCC_except_table209
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table216
+ GCC_except_table220
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table289
+ GCC_except_table290
+ GCC_except_table292
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table296
+ GCC_except_table297
+ GCC_except_table298
+ GCC_except_table327
+ GCC_except_table330
+ GCC_except_table331
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table348
+ GCC_except_table349
+ GCC_except_table350
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table353
+ GCC_except_table354
+ GCC_except_table95
+ GCC_except_table97
+ GCC_except_table99
+ _AKAccountPrivacyConsentErrorDomain
+ _AKAppleIDAuthenticationAppProvidedContextSimpleProfile
+ _AKGeoChangeRegisteredKey
+ _AKIdmsSimpleProfileAuthTokenKey
+ _AKOSEDomainAdultAgeVerificationRequired
+ _AKOSEDomainAdultAgeVerificationRequiredMiniBuddy
+ _AKOSEDomainGuardianAgeVerificationRequired
+ _AKOSEDomainGuardianAgeVerificationRequiredMiniBuddy
+ _AKOSEDomainTeenAttachedToFamilyRequired
+ _AKOSEDomainU18RestrictionRequired
+ _AKOSEDomainUnverifiedAdultRestrictionRequired
+ _AKPVKTokenKey
+ _AKPropertyCanCreateSimpleProfilesKey
+ _AKPropertyProfileAccountAltDSIDs
+ _AKPropertyProfileAccountName
+ _AKPropertyProfileAccountOwnerAltDSID
+ _AKPropertySimpleProfileAccounts
+ _AKSimpleProfileListChangedNotification
+ _AKSimpleProfileUpgradeQRCodeEnabled
+ _AKSimpleProfilesResultKey
+ _AKURLBagKeySimpleProfileCreate
+ _AKURLBagKeySimpleProfileDelete
+ _AKURLBagKeySimpleProfileEdit
+ _AKURLBagKeySimpleProfileImages
+ _AKURLBagKeySimpleProfileUpgradeCode
+ _AKUserInfoCanCreateSimpleProfilesKey
+ _AKUserInfoSafetyScreenSeenKey
+ _OBJC_CLASS_$_AKOSEligibilityManager
+ _OBJC_CLASS_$_AKSimpleProfileContext
+ _OBJC_CLASS_$_AKSimpleProfileContextCreate
+ _OBJC_CLASS_$_AKSimpleProfileContextDelete
+ _OBJC_CLASS_$_AKSimpleProfileContextEdit
+ _OBJC_CLASS_$_AKSimpleProfileContextUpgrade
+ _OBJC_CLASS_$_AKSimpleProfileImageResponseGroup
+ _OBJC_CLASS_$_AKSimpleProfileImageResponseImageMetadata
+ _OBJC_CLASS_$_AKSimpleProfileImagesResponse
+ _OBJC_CLASS_$_AKSimpleProfileManager
+ _OBJC_CLASS_$_AKSimpleProfileModel
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._appleAccountPrivacyBundleVersion
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._privacyBundleVersion
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._pvkToken
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._simpleProfileContext
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._teenRequiredToConnectToFamily
+ _OBJC_IVAR_$_AKAppleIDServerResourceLoadDelegate._pvkToken
+ _OBJC_IVAR_$_AKAuthenticatableResource._customShieldDetailText
+ _OBJC_IVAR_$_AKAuthenticatableResource._customShieldTitle
+ _OBJC_IVAR_$_AKFeatureManager._cachedPrivacyVersionSavingEnabled
+ _OBJC_IVAR_$_AKSimpleProfileContext._altDSID
+ _OBJC_IVAR_$_AKSimpleProfileContext._identifier
+ _OBJC_IVAR_$_AKSimpleProfileContextCreate._ageCategory
+ _OBJC_IVAR_$_AKSimpleProfileContextCreate._imageID
+ _OBJC_IVAR_$_AKSimpleProfileContextCreate._profileName
+ _OBJC_IVAR_$_AKSimpleProfileContextEdit._ageCategory
+ _OBJC_IVAR_$_AKSimpleProfileContextEdit._imageID
+ _OBJC_IVAR_$_AKSimpleProfileContextEdit._profileName
+ _OBJC_IVAR_$_AKSimpleProfileContextUpgrade._followUpItemIdentifier
+ _OBJC_IVAR_$_AKSimpleProfileImageResponseGroup._groupTitle
+ _OBJC_IVAR_$_AKSimpleProfileImageResponseGroup._images
+ _OBJC_IVAR_$_AKSimpleProfileImageResponseImageMetadata._imageDescription
+ _OBJC_IVAR_$_AKSimpleProfileImageResponseImageMetadata._imageID
+ _OBJC_IVAR_$_AKSimpleProfileImageResponseImageMetadata._imageURL
+ _OBJC_IVAR_$_AKSimpleProfileImagesResponse._imageGroups
+ _OBJC_IVAR_$_AKSimpleProfileManager._accountManager
+ _OBJC_IVAR_$_AKSimpleProfileManager._featureManager
+ _OBJC_IVAR_$_AKSimpleProfileManager._urlBag
+ _OBJC_IVAR_$_AKSimpleProfileManager._urlSession
+ _OBJC_IVAR_$_AKSimpleProfileModel._DSID
+ _OBJC_IVAR_$_AKSimpleProfileModel._ageCategory
+ _OBJC_IVAR_$_AKSimpleProfileModel._altDSID
+ _OBJC_IVAR_$_AKSimpleProfileModel._imageID
+ _OBJC_IVAR_$_AKSimpleProfileModel._imageId
+ _OBJC_IVAR_$_AKSimpleProfileModel._imageURL
+ _OBJC_IVAR_$_AKSimpleProfileModel._profileName
+ _OBJC_IVAR_$_AKSimpleProfileModel._sponsorAltDSID
+ _OBJC_IVAR_$_AKUserInformation._canCreateSimpleProfiles
+ _OBJC_IVAR_$_AKUserInformation._safetyScreenSeen
+ _OBJC_IVAR_$_AKUserInformation._simpleProfiles
+ _OBJC_METACLASS_$_AKOSEligibilityManager
+ _OBJC_METACLASS_$_AKSimpleProfileContext
+ _OBJC_METACLASS_$_AKSimpleProfileContextCreate
+ _OBJC_METACLASS_$_AKSimpleProfileContextDelete
+ _OBJC_METACLASS_$_AKSimpleProfileContextEdit
+ _OBJC_METACLASS_$_AKSimpleProfileContextUpgrade
+ _OBJC_METACLASS_$_AKSimpleProfileImageResponseGroup
+ _OBJC_METACLASS_$_AKSimpleProfileImageResponseImageMetadata
+ _OBJC_METACLASS_$_AKSimpleProfileImagesResponse
+ _OBJC_METACLASS_$_AKSimpleProfileManager
+ _OBJC_METACLASS_$_AKSimpleProfileModel
+ __AKHTTPHeaderOSEligibility
+ __AKHTTPHeaderOSEligibilityRegion
+ __AKSimpleProfileAgeCategoryKey
+ __AKSimpleProfileAltDSIDKey
+ __AKSimpleProfileContextAgeCategoryKey
+ __AKSimpleProfileContextAltDSIDKey
+ __AKSimpleProfileContextFollowUpIdentifierKey
+ __AKSimpleProfileContextIdentifierKey
+ __AKSimpleProfileContextImageIDKey
+ __AKSimpleProfileContextProfileNameKey
+ __AKSimpleProfileDSIDKey
+ __AKSimpleProfileImageIDKey
+ __AKSimpleProfileImageResponseKeyDescription
+ __AKSimpleProfileImageResponseKeyGroupTitle
+ __AKSimpleProfileImageResponseKeyImageID
+ __AKSimpleProfileImageResponseKeyImageURL
+ __AKSimpleProfileImageResponseKeyImages
+ __AKSimpleProfileImageResponseKeyProfileImages
+ __AKSimpleProfileImageURLKey
+ __AKSimpleProfileNameKey
+ __AKSimpleProfileSponsorAltDSIDKey
+ __AKSimpleProfileSponsorDSIDKey
+ __OBJC_$_CLASS_METHODS_AKOSEligibilityManager
+ __OBJC_$_CLASS_METHODS_AKSimpleProfileContext
+ __OBJC_$_CLASS_METHODS_AKSimpleProfileContextCreate
+ __OBJC_$_CLASS_METHODS_AKSimpleProfileContextEdit
+ __OBJC_$_CLASS_METHODS_AKSimpleProfileContextUpgrade
+ __OBJC_$_CLASS_PROP_LIST_AKSimpleProfileContext
+ __OBJC_$_INSTANCE_METHODS_AKConfiguration(OSEligibility)
+ __OBJC_$_INSTANCE_METHODS_AKOSEligibilityManager
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileContext
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileContextCreate
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileContextDelete
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileContextEdit
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileContextUpgrade
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileImageResponseGroup
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileImageResponseImageMetadata
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileImagesResponse
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileManager
+ __OBJC_$_INSTANCE_METHODS_AKSimpleProfileModel
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileContext
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileContextCreate
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileContextEdit
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileContextUpgrade
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileImageResponseGroup
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileImageResponseImageMetadata
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileImagesResponse
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileManager
+ __OBJC_$_INSTANCE_VARIABLES_AKSimpleProfileModel
+ __OBJC_$_PROP_LIST_AKSimpleProfileContext
+ __OBJC_$_PROP_LIST_AKSimpleProfileContextCreate
+ __OBJC_$_PROP_LIST_AKSimpleProfileContextEdit
+ __OBJC_$_PROP_LIST_AKSimpleProfileContextUpgrade
+ __OBJC_$_PROP_LIST_AKSimpleProfileImageResponseGroup
+ __OBJC_$_PROP_LIST_AKSimpleProfileImageResponseImageMetadata
+ __OBJC_$_PROP_LIST_AKSimpleProfileImagesResponse
+ __OBJC_$_PROP_LIST_AKSimpleProfileManager
+ __OBJC_$_PROP_LIST_AKSimpleProfileModel
+ __OBJC_CLASS_PROTOCOLS_$_AKSimpleProfileContext
+ __OBJC_CLASS_RO_$_AKOSEligibilityManager
+ __OBJC_CLASS_RO_$_AKSimpleProfileContext
+ __OBJC_CLASS_RO_$_AKSimpleProfileContextCreate
+ __OBJC_CLASS_RO_$_AKSimpleProfileContextDelete
+ __OBJC_CLASS_RO_$_AKSimpleProfileContextEdit
+ __OBJC_CLASS_RO_$_AKSimpleProfileContextUpgrade
+ __OBJC_CLASS_RO_$_AKSimpleProfileImageResponseGroup
+ __OBJC_CLASS_RO_$_AKSimpleProfileImageResponseImageMetadata
+ __OBJC_CLASS_RO_$_AKSimpleProfileImagesResponse
+ __OBJC_CLASS_RO_$_AKSimpleProfileManager
+ __OBJC_CLASS_RO_$_AKSimpleProfileModel
+ __OBJC_METACLASS_RO_$_AKOSEligibilityManager
+ __OBJC_METACLASS_RO_$_AKSimpleProfileContext
+ __OBJC_METACLASS_RO_$_AKSimpleProfileContextCreate
+ __OBJC_METACLASS_RO_$_AKSimpleProfileContextDelete
+ __OBJC_METACLASS_RO_$_AKSimpleProfileContextEdit
+ __OBJC_METACLASS_RO_$_AKSimpleProfileContextUpgrade
+ __OBJC_METACLASS_RO_$_AKSimpleProfileImageResponseGroup
+ __OBJC_METACLASS_RO_$_AKSimpleProfileImageResponseImageMetadata
+ __OBJC_METACLASS_RO_$_AKSimpleProfileImagesResponse
+ __OBJC_METACLASS_RO_$_AKSimpleProfileManager
+ __OBJC_METACLASS_RO_$_AKSimpleProfileModel
+ ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.330
+ ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.329
+ ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke
+ ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.368
+ ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.369
+ ___116-[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]_block_invoke.299
+ ___116-[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]_block_invoke.300
+ ___39+[AKOSEligibilityManager sharedManager]_block_invoke
+ ___50-[AKSimpleProfileImagesResponse parseValue:atKey:]_block_invoke
+ ___50-[AKSimpleProfileManager _setProfiles:forAccount:]_block_invoke
+ ___50-[AKSimpleProfileManager sortedProfilesFromArray:]_block_invoke
+ ___51-[AKSimpleProfileManager simpleProfilesForAccount:]_block_invoke
+ ___54-[AKSimpleProfileImageResponseGroup parseValue:atKey:]_block_invoke
+ ___54-[AKSimpleProfileManager profileImagesWithCompletion:]_block_invoke
+ ___56-[AKSimpleProfileManager isQRCodeEnabledWithCompletion:]_block_invoke
+ ___57-[AKSimpleProfileManager profileImageURLsWithCompletion:]_block_invoke
+ ___57-[AKSimpleProfileManager profileImageURLsWithCompletion:]_block_invoke.40
+ ___58-[AKSimpleProfileManager profileImagesDataWithCompletion:]_block_invoke
+ ___58-[AKSimpleProfileManager profileImagesDataWithCompletion:]_block_invoke.37
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.350
+ ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.306
+ ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.152
+ ___68-[AKAccountManager matchingServiceAccountForAuthKitAccount:service:]_block_invoke
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.310
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.311
+ ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.321
+ ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.352
+ ___71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.305
+ ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.363
+ ___72-[AKAccountManager _shouldEnableIdentifiableTelemetryForConsentVersion:]_block_invoke
+ ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.353
+ ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.262
+ ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.374
+ ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.364
+ ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.340
+ ___73-[AKAppleIDAuthenticationController _authenticateWithContext:completion:]_block_invoke.264
+ ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.359
+ ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke.303
+ ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.362
+ ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.284
+ ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.128
+ ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.136
+ ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.138
+ ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke_2.139
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.346
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.347
+ ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.278
+ ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.338
+ ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.307
+ ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke.290
+ ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.322
+ ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.313
+ ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke.289
+ ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.339
+ ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke.287
+ ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.328
+ ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.324
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.356
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.357
+ ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.327
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.343
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.344
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.345
+ ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.358
+ ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.309
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.333
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.334
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.335
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.336
+ ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.337
+ ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.355
+ ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.268
+ ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.269
+ ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.360
+ ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.312
+ ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.319
+ ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.354
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.326
+ ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.342
+ ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke
+ ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.366
+ ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.367
+ ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.318
+ ___93-[AKURLSession beginAuthenticationDataTaskWithRequest:serviceErrorHandler:completionHandler:]_block_invoke
+ ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.317
+ ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.325
+ ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.361
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e30_16?0"AKSimpleProfileModel"8l
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSURL"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s40l8r64l8s48l8s56l8
+ ___block_literal_global.214
+ ___block_literal_global.234
+ ___block_literal_global.236
+ ___block_literal_global.246
+ ___block_literal_global.271
+ ___block_literal_global.281
+ ___block_literal_global.283
+ ___block_literal_global.286
+ ___block_literal_global.349
+ ___block_literal_global.436
+ ___block_literal_global.45
+ ___block_literal_global.666
+ ___block_literal_global.668
+ ___block_literal_global.670
+ ___block_literal_global.672
+ ___block_literal_global.674
+ ___block_literal_global.677
+ ___block_literal_global.679
+ ___block_literal_global.76
+ ___os_log_helper_16_2_2_4_0_8_66
+ ___os_log_helper_16_2_3_8_64_8_0_8_0
+ ___os_log_helper_16_2_3_8_66_8_112_8_64
+ ___os_log_helper_16_3_3_8_64_8_0_4_1
+ __shouldEnableIdentifiableTelemetryForConsentVersion:.formatter
+ __shouldEnableIdentifiableTelemetryForConsentVersion:.onceToken
+ __xpc_type_array
+ _kAKAdultAgeVerificationRequiredDomain
+ _kAKAdultAgeVerificationRequiredMiniBuddyDomain
+ _kAKGuardianAgeVerificationRequiredDomain
+ _kAKGuardianAgeVerificationRequiredMiniBuddyDomain
+ _kAKShouldFakeOSEligibility
+ _kAKTeenAttachedToFamilyRequiredDomain
+ _kAKU18RestrictionRequiredDomain
+ _kAKUnverifiedAdultRestrictionRequiredDomain
+ _objc_msgSend$_domainForString:
+ _objc_msgSend$_handleSaveResult:version:error:
+ _objc_msgSend$_isEligibleForDomain:
+ _objc_msgSend$_isEnabledForDomain:
+ _objc_msgSend$_minimumConsentVersionForIdentifiableTelemetry
+ _objc_msgSend$_setConsentVersionProperty:forAccount:error:
+ _objc_msgSend$_shouldEnableIdentifiableTelemetryForConsentVersion:
+ _objc_msgSend$_stringForDomain:
+ _objc_msgSend$_stringFromXPCArray:logPrefix:
+ _objc_msgSend$_validateConsentVersion:error:
+ _objc_msgSend$account:isSponsorForProfile:
+ _objc_msgSend$ak_addJSONRequestHeader
+ _objc_msgSend$ak_addJSONResponseAcceptHeader
+ _objc_msgSend$ak_addOSEligibilityHeader
+ _objc_msgSend$ak_addOSEligibilityRegionHeader
+ _objc_msgSend$ak_addPVKToken:
+ _objc_msgSend$ak_arrayWithJSONResponseData:
+ _objc_msgSend$appendString:
+ _objc_msgSend$appleAccountConsentVersionForAccount:
+ _objc_msgSend$canCreateSimpleProfilesForAccount:
+ _objc_msgSend$decodingClasses
+ _objc_msgSend$eligibilityAnswerForDomain:
+ _objc_msgSend$eligibilityAnswerForDomain:context:status:
+ _objc_msgSend$featuresMaskValue
+ _objc_msgSend$fetchUpgradeURLForSponsor:forSimpleProfile:completion:
+ _objc_msgSend$groupTitle
+ _objc_msgSend$handleAuthenticationResponse:forRequest:forDataTask:withData:error:serviceErrorHandler:completionHandler:
+ _objc_msgSend$identifiableTelemetryAllowedForAccount:
+ _objc_msgSend$imageDescription
+ _objc_msgSend$imageGroups
+ _objc_msgSend$imageID
+ _objc_msgSend$imageURL
+ _objc_msgSend$images
+ _objc_msgSend$initWithAccountManager:urlBag:urlSession:featureManager:
+ _objc_msgSend$initWithValues:
+ _objc_msgSend$isAdultAgeVerificationRequired
+ _objc_msgSend$isConfiguredForProfileAuthentication
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isSimpleProfilesEnabled
+ _objc_msgSend$isTeenAttachedToFamilyRequired
+ _objc_msgSend$matchingServiceAccountForAuthKitAccount:service:
+ _objc_msgSend$needsNewSimpleProfile
+ _objc_msgSend$osEligibilityConfigValueForKey:
+ _objc_msgSend$profileImagesDataWithCompletion:
+ _objc_msgSend$pvkToken
+ _objc_msgSend$regulatoryCountryRegions
+ _objc_msgSend$setAgeCategory:
+ _objc_msgSend$setCanCreateSimpleProfiles:
+ _objc_msgSend$setFollowUpItemIdentifier:
+ _objc_msgSend$setImageID:
+ _objc_msgSend$setProfileName:
+ _objc_msgSend$setPvkToken:
+ _objc_msgSend$setSafetyScreenSeen:
+ _objc_msgSend$setSimpleProfileContext:
+ _objc_msgSend$set_identifier:
+ _objc_msgSend$shouldFakeOSEligibility
+ _objc_msgSend$shouldForceEnableSimpleProfilesUpgradeQR
+ _objc_msgSend$simpleProfileContext
+ _objc_msgSend$simpleProfilesForAccount:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$sortedProfilesFromArray:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:
+ _objc_msgSend$urlForKey:completion:
+ _objc_msgSend$validObjectForKey:
+ _os_eligibility_get_domain_answer
+ _xpc_array_get_count
+ _xpc_array_get_string
+ _xpc_dictionary_get_array
+ _xpc_get_type
- -[AKAccountManager _matchingServiceAccountForAuthKitAccount:service:]
- -[AKAccountManager accountIdentifiableTelemetryForAccount:]
- -[AKAccountManager setConsentVersion:forAccount:]
- -[AKURLSession beginAuthenticationDataTaskWithRequest:completionHandler:]
- GCC_except_table103
- GCC_except_table105
- GCC_except_table114
- GCC_except_table118
- GCC_except_table138
- GCC_except_table148
- GCC_except_table161
- GCC_except_table164
- GCC_except_table167
- GCC_except_table175
- GCC_except_table185
- GCC_except_table188
- GCC_except_table191
- GCC_except_table192
- GCC_except_table195
- GCC_except_table196
- GCC_except_table199
- GCC_except_table206
- GCC_except_table232
- GCC_except_table233
- GCC_except_table234
- GCC_except_table236
- GCC_except_table238
- GCC_except_table239
- GCC_except_table240
- GCC_except_table246
- GCC_except_table266
- GCC_except_table267
- GCC_except_table285
- GCC_except_table300
- GCC_except_table301
- GCC_except_table302
- GCC_except_table303
- GCC_except_table304
- GCC_except_table305
- GCC_except_table306
- GCC_except_table307
- GCC_except_table308
- GCC_except_table309
- GCC_except_table310
- GCC_except_table338
- GCC_except_table341
- GCC_except_table51
- GCC_except_table54
- __OBJC_$_INSTANCE_METHODS_AKConfiguration
- __OBJC_$_PROP_LIST_AKConfiguration
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.324
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.323
- ___116-[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]_block_invoke.293
- ___116-[AKAppleIDAuthenticationController _updateUserInformationWithContext:userInformation:isServerOperation:completion:]_block_invoke.294
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.344
- ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.300
- ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.149
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.304
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.305
- ___69-[AKAccountManager _matchingServiceAccountForAuthKitAccount:service:]_block_invoke
- ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.315
- ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.346
- ___71-[AKAppleIDAuthenticationController _deviceListWithContext:completion:]_block_invoke.299
- ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.357
- ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.347
- ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.256
- ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.364
- ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.358
- ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.334
- ___73-[AKAppleIDAuthenticationController _authenticateWithContext:completion:]_block_invoke.258
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.353
- ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke.297
- ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.356
- ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.278
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.125
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.129
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke.130
- ___73-[AKAppleIDServerResourceLoadDelegate signRequest:withCompletionHandler:]_block_invoke_2.136
- ___73-[AKURLSession beginAuthenticationDataTaskWithRequest:completionHandler:]_block_invoke
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.340
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.341
- ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.272
- ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.332
- ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.301
- ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke.284
- ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.316
- ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.307
- ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke.283
- ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.333
- ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke.281
- ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.322
- ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.318
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.350
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.351
- ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.321
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.337
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.338
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.339
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.352
- ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.303
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.327
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.328
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.329
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.330
- ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.331
- ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.349
- ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.262
- ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.263
- ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.354
- ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.306
- ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.313
- ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.348
- ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.320
- ___90-[AKAppleIDAuthenticationController persistRecoveryKeyWithContext:authContext:completion:]_block_invoke.336
- ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.312
- ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.311
- ___97-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:reason:completion:]_block_invoke.319
- ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.355
- ___block_descriptor_64_e8_32s40s48bs56r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr56l8s48l8s32l8s40l8
- ___block_literal_global.227
- ___block_literal_global.228
- ___block_literal_global.230
- ___block_literal_global.252
- ___block_literal_global.265
- ___block_literal_global.275
- ___block_literal_global.277
- ___block_literal_global.280
- ___block_literal_global.343
- ___block_literal_global.421
- ___block_literal_global.645
- ___block_literal_global.647
- ___block_literal_global.649
- ___block_literal_global.651
- ___block_literal_global.653
- ___block_literal_global.656
- ___block_literal_global.658
- _objc_msgSend$_matchingServiceAccountForAuthKitAccount:service:
- _objc_msgSend$accountIdentifiableTelemetryForAccount:
CStrings:
+ "      [%lu] ID:%@ URL:%@ Desc:%@\n"
+ "    [%lu] %@ (%lu images)\n"
+ "  profileImages: (%lu groups)\n"
+ "%@: %@"
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\tcanCreateSimpleProfiles: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
+ "<no title>"
+ "<none>"
+ "@\"<AKAccountManagerProtocol>\""
+ "@\"AKFeatureManager\""
+ "@\"AKSimpleProfileContext\""
+ "@\"AKURLBag\""
+ "@\"AKURLSession\""
+ "@\"NSString\"24@0:8@\"ACAccount\"16"
+ "@16@?0@\"AKSimpleProfileModel\"8"
+ "@40@0:8@16@?24@?32"
+ "@40@0:8Q16^@24^@32"
+ "@48@0:8@16@24@32q40"
+ "ADULT_AGE_VERIFICATION_REQUIRED"
+ "ADULT_AGE_VERIFICATION_REQUIRED_MINI_BUDDY"
+ "AKAccountPrivacyConsentErrorDomain"
+ "AKAppleIDAuthenticationController fetchUpgradeURLForSponsor calling out to remote service"
+ "AKAppleIDAuthenticationController fetchUpgradeURLForSponsor got result: %@. Error: %{public}@"
+ "AKAppleIDAuthenticationController fetchUpgradeURLForSponsor remoteAuthService returned an error: %{public}@"
+ "AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier - XPC error: %{public}@"
+ "AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier - XPC proxy creation failed: %{public}@"
+ "AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier - XPC success: %ul\nerror: %{public}@"
+ "AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier: %{public}@, sponsorAltDSID: %{mask.hash}@"
+ "AKOSEligibilityManager"
+ "AKPropertySimpleProfileAccounts"
+ "AKSimpleProfileContext"
+ "AKSimpleProfileContextCreate"
+ "AKSimpleProfileContextDelete"
+ "AKSimpleProfileContextEdit"
+ "AKSimpleProfileContextUpgrade"
+ "AKSimpleProfileImageResponseGroup"
+ "AKSimpleProfileImageResponseImageMetadata"
+ "AKSimpleProfileImagesResponse"
+ "AKSimpleProfileImagesResponse {\n"
+ "AKSimpleProfileManager"
+ "AKSimpleProfileManager _sendNotificationForProfilesDidChange"
+ "AKSimpleProfileManager _setProfileAccounts caught exception when setting Simple Profile accounts: %@"
+ "AKSimpleProfileManager _setProfileAccounts no changes"
+ "AKSimpleProfileManager _setProfileAccounts profiles is empty. Removing Simple Profiles"
+ "AKSimpleProfileManager _setProfileAccounts profiles is nil. Removing Simple Profiles"
+ "AKSimpleProfileManager _setProfileAccounts setting new profile accounts"
+ "AKSimpleProfileManager _setProfileAccounts: %lu"
+ "AKSimpleProfileManager isQRCodeEnabledWithCompletion"
+ "AKSimpleProfileManager isQRCodeEnabledWithCompletion %@"
+ "AKSimpleProfileManager isQRCodeEnabledWithCompletion failed to read URLBag: %@"
+ "AKSimpleProfileManager isQRCodeEnabledWithCompletion feature is force enabled"
+ "AKSimpleProfileManager profileImageURLsWithCompletion dataTaskError %@"
+ "AKSimpleProfileManager profileImageURLsWithCompletion failed to get url: %@"
+ "AKSimpleProfileManager profileImagesDataWithCompletion dataTaskError %@"
+ "AKSimpleProfileManager profileImagesDataWithCompletion failed to get url: %@"
+ "AKSimpleProfileManager profileImagesWithCompletion failed to parse JSON for results:\n%@\nwith error:\n%@"
+ "AKSimpleProfileManager profileImagesWithCompletion got data error:\n%@"
+ "AKSimpleProfileManager simpleProfilesForAccount - property has empty or incorrect type - %@"
+ "AKSimpleProfileManager simpleProfilesForAccount caught exception: %@"
+ "AKSimpleProfileManager simpleProfilesForAccount no profiles on account"
+ "AKSimpleProfileModel"
+ "Apple Account consent version update detected, but we didn't have an existing device session ID, creating... %@"
+ "Attaching PVK token from delegate"
+ "B24@0:8Q16"
+ "BEGIN [%lld]: SimpleProfileUpgrade  enableTelemetry=YES "
+ "BEGIN [%lld]: SimpleProfileUpgradeURL  enableTelemetry=YES "
+ "Domain %@ (%llu) answer was forced"
+ "Domain %@ (%llu) eligibility is uncertain (maybe) - treating as not eligible"
+ "Domain %@ (%llu) eligibility not yet available (insufficient inputs)"
+ "Domain %@ (%llu) has additional context available"
+ "Domain %@ (%llu) has input status information available"
+ "Domain %@ (%llu) is eligible"
+ "Domain %@ (%llu) is not eligible"
+ "Domain %@ (%llu) returned invalid eligibility answer: %llu"
+ "END [%lld] %fs:SimpleProfileUpgrade "
+ "END [%lld] %fs:SimpleProfileUpgradeURL "
+ "Empty string is not a valid consent version"
+ "Empty string is not a valid input for consent version"
+ "Exception caught when fetching canCreateSimpleProfiles property: %@"
+ "Exception caught when fetching safety screen seen property: %@"
+ "Exception caught when setting canCreateSimpleProfiles: %@"
+ "Exception caught when setting safety screen seen property: %@"
+ "Failed to get eligibility answer for domain %@ (%llu), error: %{private}d"
+ "Failed to save account after geo change registered with newState: %@"
+ "Failed to save account with consent version"
+ "Failed to set account consent version to %@"
+ "Feature PrivacyVersionSaving enabled - %@ isInternalBuild - %@"
+ "GUARDIAN_AGE_VERIFICATION_REQUIRED"
+ "GUARDIAN_AGE_VERIFICATION_REQUIRED_MINI_BUDDY"
+ "Invalid domain string: %@"
+ "Invalid domain: %@ (%llu)"
+ "No area IDs found for domain %@ (%llu)"
+ "No eligibility answer found for domain: %@ (%llu)"
+ "No eligibility context found for domain: %@ (%llu)"
+ "No strings found in XPC array for %@"
+ "OSEligibility"
+ "OS_ELIGIBILITY_CONTEXT_AREA_ID"
+ "PrivacyVersionSaving"
+ "Regulatory country regions"
+ "Signing request with passwordless token"
+ "Simple Profile Context uses JSON"
+ "SimpleProfileUpgrade"
+ "SimpleProfileUpgradeURL"
+ "SimpleProfiles"
+ "SimpleProfilesUpgradeQRForceEnable"
+ "Successfully set account consent version to %@"
+ "T@\"<AKAccountManagerProtocol>\",&,N,V_accountManager"
+ "T@\"AKFeatureManager\",&,N,V_featureManager"
+ "T@\"AKSimpleProfileContext\",&,N,V_simpleProfileContext"
+ "T@\"AKURLBag\",&,N,V_urlBag"
+ "T@\"AKURLSession\",&,N,V_urlSession"
+ "T@\"NSArray\",&,N,V_imageGroups"
+ "T@\"NSArray\",&,N,V_images"
+ "T@\"NSArray\",C,N,V_simpleProfiles"
+ "T@\"NSNumber\",&,N,V_imageID"
+ "T@\"NSNumber\",C,N,V_DSID"
+ "T@\"NSNumber\",C,N,V_canCreateSimpleProfiles"
+ "T@\"NSNumber\",C,N,V_imageId"
+ "T@\"NSNumber\",C,N,V_safetyScreenSeen"
+ "T@\"NSString\",&,N,V_profileName"
+ "T@\"NSString\",&,N,V_pvkToken"
+ "T@\"NSString\",C,N,V_customShieldDetailText"
+ "T@\"NSString\",C,N,V_customShieldTitle"
+ "T@\"NSString\",C,N,V_followUpItemIdentifier"
+ "T@\"NSString\",C,N,V_groupTitle"
+ "T@\"NSString\",C,N,V_imageDescription"
+ "T@\"NSString\",C,N,V_imageID"
+ "T@\"NSString\",C,N,V_imageURL"
+ "T@\"NSString\",C,N,V_privacyBundleVersion"
+ "T@\"NSString\",C,N,V_profileName"
+ "T@\"NSString\",C,N,V_pvkToken"
+ "T@\"NSString\",C,N,V_sponsorAltDSID"
+ "T@\"NSUUID\",&,N,V_identifier"
+ "TB,N,V_teenRequiredToConnectToFamily"
+ "TB,R,N,GisPrivacyVersionSavingEnabled"
+ "TB,R,N,GisSimpleProfilesEnabled"
+ "TB,R,N,GshouldForceEnableSimpleProfilesUpgradeQR"
+ "TEEN_ATTACHED_TO_FAMILY_REQUIRED"
+ "TQ,N,V_appleAccountPrivacyBundleVersion"
+ "Tq,N,V_ageCategory"
+ "U18_RESTRICTION_REQUIRED"
+ "UNVERIFIED_ADULT_RESTRICTION_REQUIRED"
+ "Vv32@0:8@\"AKSimpleProfileContextUpgrade\"16@?<v@?B@\"NSError\">24"
+ "X-Apple-I-OSE"
+ "X-Apple-I-OSE-Region"
+ "X-Apple-I-PVK-Token"
+ "_AKFakeOSEligibility"
+ "_ageCategory"
+ "_appleAccountPrivacyBundleVersion"
+ "_cachedPrivacyVersionSavingEnabled"
+ "_canCreateSimpleProfiles"
+ "_customShieldDetailText"
+ "_customShieldTitle"
+ "_domainForString:"
+ "_featureManager"
+ "_followUpIdentifier"
+ "_followUpItemIdentifier"
+ "_groupTitle"
+ "_handleSaveResult:version:error:"
+ "_imageDescription"
+ "_imageGroups"
+ "_imageID"
+ "_imageId"
+ "_imageURL"
+ "_images"
+ "_isEligibleForDomain:"
+ "_isEnabledForDomain:"
+ "_minimumConsentVersionForIdentifiableTelemetry"
+ "_privacyBundleVersion"
+ "_profileName"
+ "_pvkToken"
+ "_safetyScreenSeen"
+ "_sendNotificationForProfilesDidChange"
+ "_setConsentVersionProperty:forAccount:error:"
+ "_setProfiles:forAccount:"
+ "_shouldEnableIdentifiableTelemetryForConsentVersion:"
+ "_simpleProfileContext"
+ "_simpleProfiles"
+ "_sponsorAltDSID"
+ "_stringForDomain:"
+ "_stringFromXPCArray:logPrefix:"
+ "_teenRequiredToConnectToFamily"
+ "_urlBag"
+ "_validateConsentVersion:error:"
+ "account:isSponsorForProfile:"
+ "ageCategory"
+ "ak_accountPrivacyConsentErrorWithCode:"
+ "ak_addOSEligibilityHeader"
+ "ak_addOSEligibilityRegionHeader"
+ "ak_addPVKToken:"
+ "appendString:"
+ "appleAccountPrivacyBundleVersion"
+ "authContextWithSponsor:simpleProfileContext:"
+ "authkit/simple-profile-fetch-upgrade-url"
+ "authkit/simple-profile-upgrade-profile"
+ "beginAuthenticationDataTaskWithRequest:serviceErrorHandler:completionHandler:"
+ "canCreateProfile"
+ "canCreateSimpleProfiles"
+ "canCreateSimpleProfiles is missing."
+ "canCreateSimpleProfilesForAccount:"
+ "com.apple.authkit.simple-profile-list-changed"
+ "com.apple.gs.simple.profile.auth"
+ "createProfileAccount"
+ "customShieldDetailText"
+ "customShieldTitle"
+ "decodingClasses"
+ "deleteProfileAccount"
+ "editProfileAccount"
+ "eligibilityAnswerForDomain:"
+ "eligibilityAnswerForDomain:context:status:"
+ "featureManager"
+ "featuresMaskValue"
+ "fetchUpgradeURLForSponsor:forSimpleProfile:completion:"
+ "followUpItemIdentifier"
+ "geoChangeRegistered"
+ "geoChangeRegisteredForAccount:"
+ "groupTitle"
+ "handleAuthenticationResponse:forRequest:forDataTask:withData:error:serviceErrorHandler:completionHandler:"
+ "identifiableTelemetryAllowedForAccount:"
+ "imageDescription"
+ "imageGroups"
+ "imageID"
+ "imageId"
+ "imageURL"
+ "imageUrl"
+ "images"
+ "initWithAccountManager:urlBag:urlSession:featureManager:"
+ "initWithAltDSID:followUpIdentifier:"
+ "initWithProfileName:sponsorAltDSID:imageID:ageCategory:"
+ "isAdultAgeVerificationRequired"
+ "isAdultAgeVerificationRequiredMiniBuddy"
+ "isAdultAgeVerificationRequirementState"
+ "isAdultAgeVerificationRequirementStateMiniBuddy"
+ "isConfiguredForProfileAuthentication"
+ "isEligibleForDomain:"
+ "isEqualToArray:"
+ "isGuardianAgeVerificationRequired"
+ "isGuardianAgeVerificationRequiredMiniBuddy"
+ "isGuardianAgeVerificationRequirementState"
+ "isGuardianAgeVerificationRequirementStateMiniBuddy"
+ "isPrivacyVersionSavingEnabled"
+ "isQRCodeEnabledWithCompletion:"
+ "isSimpleProfilesEnabled"
+ "isTeenAttachedToFamilyRequired"
+ "isTeenAttachedToFamilyRequirementState"
+ "isU18RestrictionRequired"
+ "isU18RestrictionRequirementState"
+ "isUnverifiedAdultRestrictionRequired"
+ "isUnverifiedAdultRestrictionRequirementState"
+ "matchingServiceAccountForAuthKitAccount:service:"
+ "needsNewSimpleProfile"
+ "osEligibilityConfigValueForKey:"
+ "presentSimpleProfileUpgradeWithContext:completionHandler:"
+ "primaryAccountIsSponsorForProfile:"
+ "privacyBundleVersion"
+ "privacyVersionSavingEnabled"
+ "profile"
+ "profileAccountAltDSIDs"
+ "profileAccountName"
+ "profileAccountOwnerAltDSID"
+ "profileImageID"
+ "profileImageURLsWithCompletion:"
+ "profileImageUrl"
+ "profileImages"
+ "profileImagesDataWithCompletion:"
+ "profileImagesWithCompletion:"
+ "profileName"
+ "profileUpgradeCode"
+ "pvkToken"
+ "q24@?0@8@16"
+ "refreshPolicies method is not yet implemented"
+ "refreshPolicies:"
+ "regulatoryCountryRegions"
+ "resourceType: %ld, resourceName: %@, customShieldTitle: %@, customShieldDetailText: %@"
+ "safetyScreenSeenForAccount:"
+ "setAgeCategory:"
+ "setAppleAccountConsentVersion:forAccount:error:"
+ "setAppleAccountPrivacyBundleVersion:"
+ "setCanCreateSimpleProfiles:"
+ "setCanCreateSimpleProfiles:forAccount:"
+ "setCustomShieldDetailText:"
+ "setCustomShieldTitle:"
+ "setFeatureManager:"
+ "setFollowUpItemIdentifier:"
+ "setGeoChangeRegistered:forAccount:"
+ "setGroupTitle:"
+ "setImageDescription:"
+ "setImageGroups:"
+ "setImageID:"
+ "setImageId:"
+ "setImageURL:"
+ "setImages:"
+ "setIsAdultAgeVerificationRequirementState:"
+ "setIsAdultAgeVerificationRequirementStateMiniBuddy:"
+ "setIsGuardianAgeVerificationRequirementState:"
+ "setIsGuardianAgeVerificationRequirementStateMiniBuddy:"
+ "setIsTeenAttachedToFamilyRequirementState:"
+ "setIsU18RestrictionRequirementState:"
+ "setIsUnverifiedAdultRestrictionRequirementState:"
+ "setPrivacyBundleVersion:"
+ "setProfileName:"
+ "setPvkToken:"
+ "setSafetyScreenSeen:"
+ "setSafetyScreenSeen:forAccount:"
+ "setShouldFakeOSEligibility:"
+ "setSimpleProfileContext:"
+ "setSimpleProfiles:"
+ "setSponsorAltDSID:"
+ "setTeenRequiredToConnectToFamily:"
+ "setUrlBag:"
+ "setUrlSession:"
+ "set_identifier:"
+ "shouldFakeOSEligibility"
+ "shouldForceEnableSimpleProfilesUpgradeQR"
+ "simpleProfileAuthTokenForAccount:"
+ "simpleProfileContext"
+ "simpleProfiles"
+ "simpleProfilesEnabled"
+ "simpleProfilesForAccount:"
+ "simpleProfilesForPrimaryAccount"
+ "simpleProfilesUpgradeQRForceEnable"
+ "sortedArrayUsingComparator:"
+ "sortedProfilesFromArray:"
+ "spUpgradeQRCodeEnabled"
+ "sponsorAltDSID"
+ "sponsorDSID"
+ "stringWithString:"
+ "teenRequiredToConnectToFamily"
+ "upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:"
+ "urlBag"
+ "urlSession"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v72@0:8@16@24@32@40@48@?56@?64"
+ "}"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
- "_matchingServiceAccountForAuthKitAccount:service:"
- "accountIdentifiableTelemetryForAccount:"
- "beginAuthenticationDataTaskWithRequest:completionHandler:"
- "resourceType: %ld, resourceName: %@"
- "setConsentVersion:forAccount:"

```
