## libbsm.0.dylib

> `/usr/lib/libbsm.0.dylib`

```diff

   __AUTH_CONST.__auth_got: 0x1e0
   __DATA.__data: 0x180
   __DATA.__bss: 0x8a0
+  __DATA_DIRTY.__bss: 0x4
   - /usr/lib/libSystem.B.dylib
   Functions: 246
   Symbols:   307
-  CStrings:  0
+  CStrings:  178
 
CStrings:
+ "T@\"<ASAuthorizationCredential>\",R,N"
+ "T@\"<CELiftUIPresenterDelegate>\",W,N,V_delegate"
+ "T@\"<CERemoteUIPresenterDelegate>\",W,N,V_delegate"
+ "T@\"<CEUpgradeFlowManagerDelegate>\",W,N,V_delegate"
+ "T@\"ACAccount\",&,N,V_storeAccount"
+ "T@\"AKAuthorization\",R,N"
+ "T@\"AKAuthorization\",R,N,V_appleIDAuthorization"
+ "T@\"AKAuthorizationRequest\",R,N,V_appleIDRequest"
+ "T@\"AKPasswordRequest\",R,N,V_passwordRequest"
+ "T@\"AMSDelegateAuthenticateRequest\",&,N,V_authenticationRequest"
+ "T@\"AMSDelegateAuthenticateResult\",R,N,V_authenticationResult"
+ "T@\"AMSDelegatePurchaseRequest\",&,N,V_delegatePurchaseRequest"
+ "T@\"AMSDelegatePurchaseRequest\",&,N,V_purchaseRequest"
+ "T@\"AMSDelegatePurchaseResult\",R,N,V_purchaseResult"
+ "T@\"ASCPlatformPublicKeyCredentialAssertion\",R,N,V_platformKeyCredentialAssertion"
+ "T@\"ASCPlatformPublicKeyCredentialRegistration\",R,N,V_platformKeyCredentialRegistration"
+ "T@\"ASCPublicKeyCredentialAssertionOptions\",R,N,V_platformKeyCredentialAssertionOptions"
+ "T@\"ASCPublicKeyCredentialCreationOptions\",R,N,V_platformKeyCredentialRegistrationOptions"
+ "T@\"ASWebAuthenticationSessionCallback\",R,N,V_callback"
+ "T@\"CASPasswordCredential\",R,N,V_passwordCredential"
+ "T@\"CHCoreDataController\",&,N,V_coreDataController"
+ "T@\"CPSAuthenticationRequest\",R,N,V_request"
+ "T@\"CPSDedicatedCameraRequest\",&,N,V_dedicatedCameraRequest"
+ "T@\"CPSDevice\",R,N"
+ "T@\"CPSLearnMoreRequest\",&,N,V_learnMoreRequest"
+ "T@\"CPSRestrictedAccessRequest\",&,N,V_restrictedAccessRequest"
+ "T@\"CPSStoreAuthenticationRequest\",&,N,V_storeAuthenticationRequest"
+ "T@\"CPSSystemAuthenticationRequest\",&,N,V_systemAuthenticationRequest"
+ "T@\"CPSTVProviderRequest\",&,N,V_tvProviderRequest"
+ "T@\"CPSWebRequest\",&,N,V_webAuthenticationRequest"
+ "T@\"CPSWebRequest\",R,N,V_webRequest"
+ "T@\"ICQUpgradeFlowManager\",&,N,V_upgradeFlowManager"
+ "T@\"NSArray\",&,N,V_approversAppleAccountAltDSIDs"
+ "T@\"NSArray\",&,N,V_proxiedAppDomains"
+ "T@\"NSArray\",C,N,V_customAuthenticationMethods"
+ "T@\"NSArray\",C,N,V_customSharingMethods"
+ "T@\"NSArray\",R,N,V_embeddingVector"
+ "T@\"NSData\",&,N,V_sharingData"
+ "T@\"NSDate\",R,N,V_trainingDate"
+ "T@\"NSDictionary\",&,N,V_intToUUIDMapping"
+ "T@\"NSDictionary\",&,N,V_paymentContext"
+ "T@\"NSDictionary\",R,N,V_additionalHeaderFields"
+ "T@\"NSString\",&,N,V_appleAccountAltDSID"
+ "T@\"NSString\",&,N,V_providerCode"
+ "T@\"NSString\",C,N,V_customTitleText"
+ "T@\"NSString\",R,N,V_algorithmType"
+ "T@\"NSString\",R,N,V_callbackScheme"
+ "T@\"NSURL\",R,N,V_webCallbackURL"
+ "T@\"UIImage\",&,N,V_providerImage"
+ "T@?,C,N,V_deviceAcceptedNotificationHandler"
+ "T@?,C,N,V_deviceStartedAuthenticationHandler"
+ "T@?,C,N,V_sessionFailedHandler"
+ "T@?,C,N,V_sessionFinishedHandler"
+ "Tq,N,V_restrictionType"
+ "Tq,N,V_service"
+ "_appleAccountAltDSID"
+ "_appleIDAuthorization"
+ "_appleIDRequest"
+ "_approversAppleAccountAltDSIDs"
+ "_authenticationResult"
+ "_coreDataController"
+ "_customAuthenticationMethods"
+ "_customSharingMethods"
+ "_customTitleText"
+ "_dedicatedCameraRequest"
+ "_delegatePurchaseRequest"
+ "_deviceAcceptedNotificationHandler"
+ "_deviceStartedAuthenticationHandler"
+ "_initCurrentDevice"
+ "_intToUUIDMapping"
+ "_isPlatformKeyOnlyRequest"
+ "_learnMoreRequest"
+ "_paymentContext"
+ "_platformKeyCredentialAssertion"
+ "_platformKeyCredentialRegistration"
+ "_platformKeyCredentialRegistrationOptions"
+ "_providerCode"
+ "_proxiedAppDomains"
+ "_restrictedAccessRequest"
+ "_sendEvent:withPayloadBuilder:"
+ "_sessionFailedHandler"
+ "_sessionFinishedHandler"
+ "_sharingData"
+ "_storeAuthenticationRequest"
+ "_systemAuthenticationRequest"
+ "_trainingDate"
+ "_tvProviderRequest"
+ "_webAuthenticationRequest"
+ "_webCallbackURL"
+ "_webRequest"
+ "addPersistentStoreFromDatabase"
+ "aggregatedMotionAndAppLaunchDataFromDate:toDate:completion:"
+ "appleAccountAltDSID"
+ "appleIDAuthorization"
+ "appleIDRequest"
+ "approversAppleAccountAltDSIDs"
+ "authenticationResult"
+ "authenticationSessionDeviceStartedAuthentication:"
+ "authenticationSessionDeviceTappedNotification:"
+ "authenticationSessionDidFailWithError:"
+ "authenticationSessionDidFinishWithResponse:"
+ "autoAssetAvailableForUseForAssetType:assetSpecifier:completion:"
+ "autoAssetEndAllLocksForAssetType:assetSpecifier:completion:"
+ "autoAssetEndLockContentForAssetType:assetSpecifier:endLockReason:completion:"
+ "autoAssetInterestInContentForAssetType:assetSpecifier:completion:"
+ "autoAssetLockContentForAssetType:assetSpecifier:lockReason:completion:"
+ "beginAppleOneUpgradeFlowWithPresenter:url:"
+ "beginLiftUIUpgradeFlowWithPresenter:url:"
+ "beginRemoteUIUpgradeFlowWithPresenter:url:"
+ "buildRecommendationFlowControllerWithAction:"
+ "categoriesForBundleId:completion:"
+ "categoriesForBundleIdSet:completion:"
+ "coreDataController"
+ "customAuthenticationMethods"
+ "customCategoryVersion"
+ "customSharingMethods"
+ "customTitleText"
+ "databaseAssetAvailableStatusWithCompletion:"
+ "dedicatedCameraRequest"
+ "downloadDatabaseAssetIfNeeded"
+ "downloadDatabaseAssetIfNeededWithCompletion:"
+ "embeddingVectorForBundleId:completion:"
+ "extractDataFromCoreDataResult:"
+ "fetchAllWithShouldRefreshBreakout:"
+ "fetchAssetWithTeamID:options:completionHandler:"
+ "fetchCategoriesForBundleId:"
+ "handleEvent:sender:ruleConfig:withReplyBlock:"
+ "handleTapClose"
+ "handleTapContainer"
+ "handleTapStopRecording"
+ "inCallControls"
+ "inCallControlsButtonAvatarOnly"
+ "inCallControlsButtonNoPhotoNoAvatar"
+ "inCallControlsEmergencyCallButton"
+ "inCallControlsKeypadButton"
+ "initWithBundleId:embeddingVector:modelVersion:algorithmType:trainingDate:"
+ "intToUUIDMapping"
+ "learnMoreAboutSensitiveContentWarningURL"
+ "liftUIPresenterDidCancelWithUserInfo:"
+ "liftUIPresenterDidCompleteWithUserInfo:"
+ "liftUIPresenterDidLoadWithSuccess:error:"
+ "loadMappingFromFile"
+ "lockAssetAndReturnAssetPathForFile:withLockReason:"
+ "lockAssetWithLockReason:"
+ "noreClientSectionRank:"
+ "populateSampleAppLaunchEmbeddingWithCompletion:"
+ "purchaseRequest"
+ "refreshEligibleRecommendationsWithShouldSendDisplayedStatus:shouldRefreshBreakout:"
+ "reportWithTeamID:eventType:event:error:"
+ "sendManageStorageDisplayedEvent"
+ "sendRecommendedForYouTapEvent"
+ "sendiCloudSettingsDisplayedEvent"
+ "setContainerPtr:"
+ "setCoreDataController:"
+ "setCustomAuthenticationMethods:"
+ "setIntToUUIDMapping:"
+ "setIsiCloudPlusSubscriber:"
+ "setLastCompletedTimeStamp:"
+ "setMaxRecommendations:"
+ "setMaxRecommendationsToShow:"
+ "setMessageTemplates:"
+ "setRecommendationSpecifierSubtitle:"
+ "setRecommendationSpecifierTitle:"
+ "setServerRecommendationsURL:"
+ "setServerRulesURL:"
+ "setSharingData:"
+ "setSubtitleTemplates:"
+ "setSystemAuthenticationRequest:"
+ "setTitleHint:"
+ "setUpgradeFlowManager:"
+ "setupXpcServiceActivitiesAndReturnError:"
+ "thresholdForKey:"
+ "timestampForLastCanceled:"
+ "timestampForLastCompleted:"
+ "titleHint"
+ "trackActionCanceledForRecommendation:"
+ "trainingDate"
+ "upgradeFlowManager"

```