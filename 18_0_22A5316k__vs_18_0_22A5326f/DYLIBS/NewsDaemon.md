## NewsDaemon

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon`

```diff

-5564.0.0.0.0
+5575.0.0.0.0
   __TEXT.__text: 0xaa2c
   __TEXT.__auth_stubs: 0x9b0
   __TEXT.__objc_methlist: 0x62c

   __TEXT.__objc_methtype: 0x5f5
   __TEXT.__objc_stubs: 0xf40
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x358
+  __DATA_CONST.__const: 0x398
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __AUTH_CONST.__const: 0x348
   __AUTH_CONST.__cfstring: 0x4a0
   __AUTH_CONST.__objc_const: 0x15c0
-  __AUTH.__objc_data: 0x250
+  __AUTH.__objc_data: 0x1b0
   __AUTH.__data: 0xd0
   __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x5c0
+  __DATA.__data: 0x588
   __DATA.__bss: 0x6c0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 350
-  Symbols:   392
-  CStrings:  315
+  Symbols:   400
+  CStrings:  445
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ ",R,N,V_maxLength"
+ "Count"
+ "TQ,R,N,V_receivedEvents"
+ "TQ,R,N,V_referralSource"
+ "TQ,R,N,V_relationshipType"
+ "TQ,R,N,V_relayServerPasswordLength"
+ "TQ,R,N,V_reportType"
+ "TQ,R,N,V_requiredDeviceMetadataFields"
+ "TQ,R,N,V_requiredPersonalizationFields"
+ "TQ,R,N,V_riskLevel"
+ "TQ,R,N,V_selectedPaymentMethodType"
+ "TQ,R,N,V_setupAssistant"
+ "TQ,R,N,V_severity"
+ "TQ,R,N,V_sharingGroup"
+ "TQ,R,N,V_sharingStatus"
+ "TQ,R,N,V_shipmentQuoteMaximum"
+ "TQ,R,N,V_shipmentQuoteMinimum"
+ "TQ,R,N,V_subtype"
+ "TQ,R,N,V_supportedRepaymentTypes"
+ "TQ,R,N,V_technology"
+ "TQ,R,N,V_textColor"
+ "TQ,R,N,V_tier"
+ "TQ,R,N,V_topicType"
+ "TQ,R,N,V_transferType"
+ "TQ,R,N,V_unavailableActionBehavior"
+ "TQ,R,N,V_unitCount"
+ "TQ,R,N,V_updateReason"
+ "TQ,R,N,V_updateReasons"
+ "TQ,R,N,V_usage"
+ "TQ,R,N,V_verificationType"
+ "TQ,R,V_expressUpgradeHideDisableAction"
+ "T^B,N,V_isFeatureNotSupportedError"
+ "T^v,N,V_billingAddress"
+ "T^v,N,V_shippingAddress"
+ "T^{CGColorSpace=},R,N,V_colorSpace"
+ "T^{CGImage=},N"
+ "T^{CGImage=},N,V_digitalCardImage"
+ "T^{CGImage=},N,V_logoImage"
+ "T^{CGImage=},N,V_plasticCardImage"
+ "T^{CGImage=},R,N,V_art"
+ "T^{CGImage=},R,N,V_backgroundImage"
+ "T^{CGImage=},R,N,V_icon"
+ "T^{CGImage=},R,N,V_image"
+ "T^{CGImage=},R,N,V_imageRef"
+ "T^{CGPDFPage=},R,N,V_pageRef"
+ "T^{CGPath=},R,V_CGPath"
+ "T^{__SecAccessControl=},N,V_accesssControlRef"
+ "Td,N,V_accountFetchAfterTransactionWaitPeriod"
+ "Td,N,V_accountFetchAfterTransactionWaitTolerance"
+ "Td,N,V_accountFetchPeriod"
+ "Td,N,V_amount"
+ "Td,N,V_availableFromRelative"
+ "Td,N,V_availableUntilRelative"
+ "Td,N,V_canvasScale"
+ "Td,N,V_clientCallbackTimeout"
+ "Td,N,V_connectionTimeout"
+ "Td,N,V_createdAt"
+ "Td,N,V_dateCreated"
+ "Td,N,V_deferredDate"
+ "Td,N,V_deviceScoreTimeout"
+ "Td,N,V_endDate"
+ "Td,N,V_endStationLatitude"
+ "Td,N,V_endStationLongitude"
+ "Td,N,V_extendedAccountFetchPeriod"
+ "Td,N,V_financingPlansFetchPeriod"
+ "Td,N,V_freeCancellationDate"
+ "Td,N,V_fundingSourcesFetchPeriod"
+ "Td,N,V_ingestedDate"
+ "Td,N,V_locationAltitude"
+ "Td,N,V_locationHorizontalAccuracy"
+ "Td,N,V_locationLatitude"
+ "Td,N,V_locationLongitude"
+ "Td,N,V_longMinRefreshPeriod"
+ "Td,N,V_maxDistance"
+ "Td,N,V_minRefreshPeriod"
+ "Td,N,V_outputBorderTrim"
+ "Td,N,V_outputCornerRadius"
+ "Td,N,V_outputScale"
+ "Td,N,V_passActivationTimeout"
+ "Td,N,V_preferredImageScale"
+ "Td,N,V_proactiveAssociatedAccountFetchPeriod"
+ "Td,N,V_proactiveFetchPeriod"
+ "Td,N,V_promotionsFetchPeriod"
+ "Td,N,V_recoveryPaymentPlansFetchPeriod"
+ "Td,N,V_recurringPaymentStartDate"
+ "Td,N,V_repeatInterval"
+ "Td,N,V_sharedCloudStoreModelFetchPeriod"
+ "Td,N,V_shortMinRefreshPeriod"
+ "Td,N,V_startDate"
+ "Td,N,V_startStationLatitude"
+ "Td,N,V_startStationLongitude"
+ "Td,N,V_timeInterval"
+ "Td,N,V_timeVisibleAfterCompleted"
+ "Td,N,V_timeoutOverride"
+ "Td,N,V_updatePaymentDeviceTimeout"
+ "Td,N,V_usersFetchPeriod"
+ "Td,R,N,V_availableFromOffsetFromUTC"
+ "Td,R,N,V_createdAt"
+ "Td,R,N,V_maximumMatchingDistance"
+ "Td,R,V_expressUpgradePromoteDuration"
+ "Technologies"
+ "Tf,R,N,V_enablementThreshold"
+ "Ti,N,V_confirmationStyle"
+ "Ti,N,V_endpointID"
+ "Ti,N,V_isCompact"
+ "Ti,N,V_isNegative"
+ "Ti,N,V_length"
+ "Ti,N,V_merchantCategoryCode"
+ "Ti,N,V_nearby"
+ "Ti,N,V_requestor"
+ "Ti,N,V_requestorDeviceType"
+ "Ti,R,N,V_remoteProcessIdentifier"
+ "Tq,N,V_APIType"
+ "Tq,N,V_accessType"
+ "Tq,N,V_accountEventType"
+ "Tq,N,V_accountType"
+ "Tq,N,V_adamIdentifier"
+ "Tq,N,V_adjustmentType"
+ "Tq,N,V_adjustmentTypeReason"
+ "Tq,N,V_ageCategory"
+ "Tq,N,V_altHeaderSubtitleTimeInterval"
+ "Tq,N,V_amount"
+ "Tq,N,V_amountComparison"
+ "Tq,N,V_appleIdentifierType"
+ "Tq,N,V_applePayLaterAvailability"
+ "Tq,N,V_applicationType"
+ "Tq,N,V_associatedIntent"
+ "Tq,N,V_authRequirement"
+ "Tq,N,V_carKeyBrandCode"
+ "Tq,N,V_cardNetwork"
+ "Tq,N,V_cardholderNameInputMethod"
+ "Tq,N,V_cellStyle"
+ "Tq,N,V_certificatesVersion"
+ "Tq,N,V_channel"
+ "Tq,N,V_cleanConfidence"
+ "Tq,N,V_cleanConfidenceLevel"
+ "Tq,N,V_codeOnError"
+ "Tq,N,V_comparison"
+ "Tq,N,V_compoundingPeriods"
+ "Tq,N,V_configurationDataType"
+ "Tq,N,V_confirmationBlobVersion"
+ "Tq,N,V_contactID"
+ "Tq,N,V_contactlessPriority"
+ "Tq,N,V_countryCode"
+ "Tq,N,V_creationVersion"
+ "Tq,N,V_credentialType"
+ "Tq,N,V_cryptogramType"
+ "Tq,N,V_currencyCode"
+ "Tq,N,V_cyclesPastDue"
+ "Tq,N,V_dateOrder"
+ "Tq,N,V_dateStyle"
+ "Tq,N,V_daysPastDue"
+ "Tq,N,V_daysPriorToRelativeInstallmentNumber"
+ "Tq,N,V_daysSinceTransactionStart"
+ "Tq,N,V_decimalPrecision"
+ "Tq,N,V_demoMerchant"
+ "Tq,N,V_demoPerson"
+ "Tq,N,V_encryptionSource"
+ "Tq,N,V_endProcessingHour"
+ "Tq,N,V_error"
+ "Tq,N,V_errorCode"
+ "Tq,N,V_expirationInputMethod"
+ "Tq,N,V_fallbackCategory"
+ "Tq,N,V_fallbackcategory"
+ "Tq,N,V_fetchReason"
+ "Tq,N,V_financingPlanFetchLimit"
+ "Tq,N,V_foregroundContentMode"
+ "Tq,R,N,V_consistencyCheckBackoffLevel"
+ "Tq,R,N,V_countryCode"
+ "Tq,R,N,V_credentialType"
+ "Tq,R,N,V_cryptogramType"
+ "Tq,R,N,V_currencyCode"
+ "Tq,R,N,V_displayType"
+ "Tq,R,N,V_eligibilitySource"
+ "Tq,R,N,V_eligibilityStatus"
+ "Tq,R,N,V_feesInterval"
+ "Tq,R,N,V_foregroundContentMode"
+ "Tq,R,N,V_glyphState"
+ "Tq,R,N,V_groupNumber"
+ "Tq,R,N,V_initialBarcodeFetchCount"
+ "Tq,R,N,V_installmentCount"
+ "Tq,R,N,V_installmentInterval"
+ "Tq,R,N,V_largeCardTemplateType"
+ "Tq,R,N,V_minLength"
+ "Tq,R,N,V_miniCardTemplateType"
+ "Tq,R,N,V_minimumAge"
+ "Tq,R,N,V_numberOfActiveStatementedInstallments"
+ "Tq,R,N,V_numberOfKeys"
+ "Tq,R,N,V_operation"
+ "Tq,R,N,V_orientation"
+ "Tq,R,N,V_outstandingCheckInAction"
+ "Tq,R,N,V_payLaterSuppressionMode"
+ "Tq,R,N,V_paymentApplicationState"
+ "Tq,R,N,V_paymentMode"
+ "Tq,R,N,V_productType"
+ "Tq,R,N,V_proxCardType"
+ "Tq,R,N,V_registrationType"
+ "Tq,R,N,V_scatterInterval"
+ "Tq,R,N,V_shippingTimeUnit"
+ "Tq,R,N,V_standaloneTransactionType"
+ "Tq,R,N,V_stateMachineCancelReason"
+ "Tq,R,N,V_supersededBy"
+ "Tq,R,N,V_supportedProtocols"
+ "Tq,R,N,V_terminalType"
+ "Tq,R,N,V_tintColor"
+ "Tq,R,N,V_transactionType"
+ "Tq,R,N,V_trustLevel"
+ "Tq,R,N,V_valueAddedServiceMode"
+ "Tq,R,N,V_variant"
+ "Tq,R,V_classification"
+ "Tq,V_concurrentRequests"
+ "Tq,V_consistencyCheckBackoffLevel"
+ "Tq,V_registrationType"
+ "Tq,V_version"
+ "Transaction"
+ "Ts,N,V_merchantCategoryCode"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_cobrandLogoRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_logoRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_stripRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_thumbnailRect"
+ "T{PKEdgeInsets=dddd},R,N"
+ "T{_NSRange=QQ},N,V_footerLinkRange"
+ "URLBase64EncodedString"
+ "URLForImageNamed:inBundle:scale:"
+ "URLForImageNamed:inBundle:scale:preferredScreenScale:suffix:"
+ "URLForImageWithScale:"
+ "VE7BAlWGDSKrO5xc:hostChallenge:challengeResponse:seid:nonce:HY6FXG20397zwmVg:"
+ "_ABKeyFromCNKey:"
+ "_AMPCardEnrollment"
+ "_AMPEnrollmentAvailable"
+ "_AMPMetrics"
+ "_APIType"
+ "_CNKeyFromABKey:"
+ "_FPANSuffix"
+ "_HTTPBodyWithDictionary:"
+ "_JSONObject"
+ "_PKBankAccountInformation"
+ "_SEPCertificates"
+ "_SPID"
+ "_TCIs"
+ "_UID"
+ "__setState:param:"
+ "_aaAlternateDSID"
+ "_abbreviationCode"
+ "_acceptableDocuments"
+ "_acceptedApplications"
+ "_acceptedBankAccountsForAcceptedFundingSources:"
+ "_acceptedFundingSources"
+ "_accessDelegatesWithHandler:"
+ "_accessObserversWithHandler:"
+ "_accessTerminalSubtype"
+ "_accessType"
+ "_accessibility"
+ "_accessibilityURL"
+ "_accessoryAttached"
+ "_accessoryConnectionInfo"
+ "_accessoryConnectionUUID"
+ "_accesssControlRef"
+ "_accountAttestationAnonymizationSalt"
+ "_accountChangedNotificationSuspensionCount"
+ "_accountCredential"
+ "_accountEventType"
+ "_accountEvents"
+ "_accountFetchAfterTransactionWaitPeriod"
+ "_accountFetchAfterTransactionWaitTolerance"
+ "_accountFetchPeriod"
+ "_accountHash"
+ "_accountKeyIdentifier"
+ "_accountManagedStateChanged"
+ "_accountNumberSuffix"
+ "_accountOrderChanged"
+ "_accountPaymentFundingSource"
+ "_accountPaymentSupportsPeerPayment"
+ "_accountPaymentUsePeerPaymentBalance"
+ "_accountServicePushTopic"
+ "_accountServiceURL"
+ "_accountServicesURL"
+ "_accountStateDirty"
+ "_accountStorefrontChanged"
+ "_accountSuffix"
+ "_accountUser"
+ "_accountUserAccessLevel"
+ "_accountUserActivity"
+ "_accountUserAltDSID"
+ "_accountUserCollection"
+ "_accountUserFirstName"
+ "_accountUserLastName"
+ "_accountUserPreferences"
+ "_accountUsers"
+ "_accountUsersByAltDSID"
+ "_accountsForFeatureIdentifier:"
+ "_achPaymentWithAmount:bankInformation:"
+ "_acquireSuppressionAssertionIfNeededWithCompletion:"
+ "_acquireSuppressionAssertionWithCompletion:"
+ "_acquiredAssertions"
+ "_actionAssertionCount"
+ "_actionContent"
+ "_actionDictionaries"
+ "_actionGroupDescription"
+ "_actionGroups"
+ "_actionIdentifier"
+ "_actionIdentifiers"
+ "_actionIdentifiersRequiringAuthentication"
+ "_actionInfo"
+ "_actionLocalizations"
+ "_actionLock"
+ "_actionOnDismiss"
+ "_actionState"
+ "_actionURL"
+ "_actionsForStrings:"
+ "_activatePaymentApplications:forPaymentPass:forceReactivation:"
+ "_activatedHostCards"
+ "_activatedPaymentApplications"
+ "_activatedPaymentPass"
+ "_activatedValueAddedServicePasses"
+ "_activationCodeConfigurations"
+ "_activationCodeHash"
+ "_activationOptions"
+ "_activationStateForApplicationState:"
+ "_activationTimer"
+ "_activeCapabilityRole"
+ "_activeFinancingPlans"
+ "_activeInstallments"
+ "_activeManageability"
+ "_activeODIAssessment"
+ "_activePasscodeUpgradeFlowAssertion"
+ "_activePasscodeUpgradeFlowAssertionActive"
+ "_activePassesOnly"
+ "_activeRegistrationTasks"
+ "_activeShareability"
+ "_activeVisibility"
+ "_activityContext"
+ "_activityCriteria"
+ "_activityRegistrations"
+ "_addAccountPaymentSourcesToPaymentSourcesIfNecessary:supportedRepaymentTypes:eligibleBankSources:"
+ "_addAssociatedCredential:"
+ "_addCashbackTransactions:currentMonthOnly:completion:"
+ "_addCleanupActionsToResultsSummary"
+ "_addContactToKeychain:forPreference:"
+ "_addDismissActionToArticleLayouts:"
+ "_addEnrouteTransitType:"
+ "_addExistingTitle"
+ "_addField:result:destination:requiresSecureSubmission:"
+ "_addFinancingOptionRequest:"
+ "_addInsightsToSummary:completion:"
+ "_addInstantWidthdrawalTransactionsWithCompletion:"
+ "_addInterestToSummaryIfNecessary:withLastPeriodChange:completion:"
+ "_addNewBankAccountIfNecessary:"
+ "_addNewTitle"
+ "_addPaymentOffersControllerRequest:"
+ "_addPaymentPassRequestConfiguration"
+ "_addPaymentPassToLibrary"
+ "_addRequest:"
+ "_addRequestConfiguration"
+ "_addSuggestedAmount:force:"
+ "_addSupportedFeaturesToEncryptedCloudRecord:"
+ "_addToAMPState"
+ "_addedCredential"
+ "_additionalBalanceForProcessingDate:"
+ "_additionalDeviceSerialNumbers"
+ "_additionalEligiblePaymentPassesForPaymentRequest:"
+ "_additionalInfoFields"
+ "_additionalPayLaterServiceProviderData"
+ "_additionalProvisioningDictionary"
+ "_additionalPushTopics"
+ "_additionalRelevantAnalyticsDictionary"
+ "_addressFieldsToContactFields:"
+ "_addressFormatConfiguration"
+ "_addressableHandles"
+ "_adjustBalanceForAuthorizedTransferQuote:"
+ "_adjustedBalance"
+ "_adjustmentTypeReason"
+ "_adjustments"
+ "_advanceToNextState"
+ "_advanceToNextStateFromResolveError:"
+ "_advertiserQueue"
+ "_advertisingDeviceNearby"
+ "_advertisingDeviceUUID"
+ "_ageCategory"
+ "_aggregateDictionary"
+ "_aidaAlternateDSID"
+ "_aidaToken"
+ "_aisle"
+ "_alingment"
+ "_aliroGroupResolvingKeys"
+ "_allAcceptedRemotePaymentInstruments"
+ "_allAisles"
+ "_allChannels"
+ "_allEntryNodes"
+ "_allFeatureApplications"
+ "_allInstallments"
+ "_allLevels"
+ "_allMandatoryValuesAreSameAmount"
+ "_allPartialErrors"
+ "_allPasses"
+ "_allPossibleCapabilityForAccumulateBlock:"
+ "_allPossibleCapabilitySetsForView:"
+ "_allRemoteDevices"
+ "_allRows"
+ "_allSeats"
+ "_allSectionColors"
+ "_allSections"
+ "_allSemantics"
+ "_allSupportedRadioTechnologies"
+ "_allUnavailableRemotePaymentInstruments"
+ "_allocation"
+ "_allowDeepLink"
+ "_allowInternalSymbols"
+ "_allowManagedAppleID"
+ "_allowOnManagedAccount"
+ "_allowPartialAssessment"
+ "_allowSynchronousFetch"
+ "_allowUserEdit"
+ "_allowedCardTypes"
+ "_allowedCharacters"
+ "_allowedFeatureIdentifiers"
+ "_allowedPassType"
+ "_allowedPassUniqueIDs"
+ "_allowedPaymentNetworks"
+ "_allowedProductIdentifiers"
+ "_allowedRelayServerHosts"
+ "_allowedSharingChannels"
+ "_allowsCachedCardRequirements"
+ "_allowsFormalPaymentRequests"
+ "_alphaInfoTransform"
+ "_altContentSubtitle"
+ "_altDSIDToContactCache"
+ "_altFooterContent"
+ "_altHeaderSubtitle"
+ "_altHeaderSubtitleTimeInterval"
+ "_altImage"
+ "_altPrimaryActionIdentifier"
+ "_altPrimaryActionTitle"
+ "_altSubtitle"
+ "_altSubtitleTimeInterval"
+ "_alternativeAcceptedValues"
+ "_alternativeAction"
+ "_alternativeActionOverride"
+ "_ambientMaterialPropertyImage"
+ "_ambientOcclusionMaterialPropertyImage"
+ "_amountAddedToAuth"
+ "_amountApplied"
+ "cancelReason"
+ "es"
+ "nnectionStatus"
- ":"
- "AKUIMicaPlayerDidChangePlaybackTime:"
- "AKUIMicaPlayerDidStopPlaying:"
- "IDPHandler:didStartLoadingPageInWebView:"
- "T@\"<AKAppleIDAuthenticationInAppContextDelegate>\",W,N,V_delegate"
- "T@\"<RUIServerHookDelegate>\",W,N"
- "T@\"NSURL\",R,C,N,V_initiatingURL"
- "T@\"UIButton\",&,N,V_createButton"
- "T@\"UIButton\",&,N,V_signInButton"
- "addParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:withReply:"
- "addParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:withReply:"
- "addParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:withReply:"
- "addToCloudKitSharing:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:withReply:"
- "addToShareFromSharingURL:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:withReply:"
- "callForAddParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:reply:"
- "callForAddParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:reply:"
- "callForAddParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:reply:"
- "callForCloudKitAddToShare:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:reply:"
- "callForCurrentUserSharingStatus:reply:"
- "callForExistingShareForFile:reply:"
- "callForFileSharing:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:reply:"
- "callForFileURLRemoveShare:reply:"
- "callForForciblyShareFolder:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:reply:"
- "callForMailContent:share:fileURL:appName:appIconData:reply:"
- "callForMetadataFromShareURL:containerSetupInfo:reply:"
- "callForRemoveShare:containerSetupInfo:reply:"
- "callForSharingStatus:reply:"
- "callForSharingURLAddToShare:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:reply:"
- "callForSharingURLRemoveShare:containerSetupInfo:reply:"
- "callForUpdateShare:containerSetupInfo:reply:"
- "callForUserNameAndEmail:containerSetupInfo:reply:"
- "ctsBrowser"
- "currentUserSharingStatusFor:withReply:"
- "effectBrowserViewController:willChangeDockHeight:"
- "effectTypeWithIdentifier:"
- "effectsAreAvailable"
- "effectsAreEnabled"
- "effectsButton"
- "effectsButtonIsVisible"
- "effectsState"
- "embedEffectsBrowserViewController:"
- "encodeProcessedVideoFrame:"
- "endGreenTea3PCallButtonTappedWithButton:"
- "endRemoteControlSessionTappedWithButton:"
- "endedRecordingVideoMessage"
- "eportFlow:"
- "ermissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:"
- "existingShareForFile:withReply:"
- "expandedAppViewControllerSizeFor:"
- "expandedAppViewControllerSizeForEffectBrowserViewController:"
- "faceTimeDateString"
- "forceBumpPriority"
- "forciblyShareFolder:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:withReply:"
- "frameForRestoreAnimation"
- "frontBoardInterfaceOrientation"
- "fullScreenFocusedParticipantOrientation"
- "getMetadataFromShareFromSharingURL:containerSetupInfo:withReply:"
- "getSharedContentSourceAvatarWithImageHandler:"
- "handedOffCall"
- "handleAppLaunchWantsHUDDismissal:"
- "handleAudioUplinkChange:"
- "handleBluetoothAudioFormatChanged:"
- "handleCallConnected:"
- "handleCallRecordingStateChanged:"
- "handleCallStartedConnecting:"
- "handleCallStatusDidChange:"
- "handleCameraBlurTapped"
- "handleCameraCinematicFramingAvailabilityChanged:"
- "handleCameraCinematicFramingEnabledChanged:"
- "handleCameraFlipTapped"
- "handleCameraListDidChange:"
- "handleCameraReactionEffectsEnabledChanged:"
- "handleCameraStudioLightEnabledChanged:"
- "handleCameraZoomBecameAvailable:"
- "handleCameraZoomBecameUnavailable:"
- "handleCinematicFramingTapped"
- "handleCollapseButtonTapped"
- "handleContentSizeCategoryDidChange:"
- "handleDidChangeIsWaitingOnFirstRemoteFrame:"
- "handleEffectsTapped"
- "handleHoldMusicDidChange:"
- "handleIDSStatusChanged"
- "handleIDSStatusChangedWithNotification:"
- "handleIdsStatusChanged"
- "handleIsScreeningChanged:"
- "handleLegacyCallStatusDidChangeNotification:"
- "handleLocalPreviewChanged:"
- "handleLocalVideoAttributesChanged:"
- "handleLocalVideoPreviewFirstFrameArrived:"
- "handleLockScreenStatusChanged"
- "handleLookupManagerDidChangeNotification:"
- "handlePTTCallStatusDidChange:"
- "handlePersonalNicknameChanged:"
- "handlePinchWithSender:"
- "handleReactionEffectGestureTapped"
- "handleRecognizer:"
- "handleRotateButtonTapped"
- "handleSceneStateChangeNotification:"
- "handleScreenConnectionDidUpdate:"
- "handleScreenSharingAttributesChanged:"
- "handleScreenSharingDidChange:"
- "handleSendingVideoChanged:"
- "handleSharedProfileUpdateForController:contact:"
- "handleShutterButtonTapped"
- "handleStudioLightTapped"
- "handleSystemApertureTapGesture"
- "handleSystemPreferredCameraChanged:"
- "handleTappedEducationScreenCancel"
- "handleTappedEducationScreenContinue"
- "handleVideoMessageButtonTapped"
- "handleWindowDidFinishResize:"
- "handlelocalCameraUIDDidChange:"
- "hasAssociatedCall"
- "hasParticipantVideo"
- "hasPresentedFullScreenCallUI"
- "hasReceivedFirstFrame"
- "hideEffectsBrowser"
- "hudActivityManagerEnabled"
- "iOSDelegate"
- "inCallControlsDismissTimer"
- "inCallControlsState"
- "inCallControlsVisible"
- "inCallSceneSessionIdentifier"
- "initWithCaptureMode:devicePosition:flashMode:aspectRatioCrop:"
- "initWithContainingViewController:"
- "initWithConversationMember:"
- "initWithDelegate:contentPresenter:"
- "initWithDelegate:streamToken:"
- "initWithHostViewController:controlsManager:deferredPresentationManager:"
- "initWithItemProvider:faceTimeConversation:completion:"
- "initWithLeadingAccessoryView:"
- "initWithPixelBuffer:time:imageData:"
- "initWithTitle:subtitle:image:primaryActionTitle:secondaryActionTitle:type:"
- "initializeCountdownWithInitialValue:fullValue:"
- "invalidatePersistentSystemApertureAlertWithReason:"
- "isAlertAvailable"
- "isAnalysisEnabled"
- "isAppProtectionEnabled"
- "isAudioAllowedFor:"
- "isBroadcastingScreenSharing"
- "isCaptioningEnabled"
- "isConfirmLeavePTTChannelAlertPresented"
- "isPresentingFullScreenCallUI"
- "isReadyToShowCallDetails"
- "isScreenSharingFullScreen"
- "isScreeningLiveActivityEnabled"
- "isShowingHUD"
- "isShowingReactions"
- "isShownAboveCoverSheet"
- "isSpringBoardLocked"
- "isTransformForRemoteVideoOrientationEnabled"
- "isVideoAllowedFor:"
- "isVideoSuspended"
- "isWebCapableFor:"
- "joinButtonTappedWithButton:"
- "kickMemberButton"
- "labelDescriptorWithStringsForCall:callCount:alertAvailable:allowsDuration:"
- "labelDescriptorWithStringsForCall:callCount:callCenter:alertAvailable:allowsDuration:"
- "lagunaHandoffButtonTapped"
- "lagunaPullButtonTapped"
- "latestRemoteControlDate"
- "leaveButtonTappedWithButton:"
- "lmiApproveButton"
- "localAudioToggledWithIsMuted:"
- "localAudioTogglingDelegate"
- "localParticipantState"
- "localParticipantView"
- "localizedSenderIdentity"
- "mailContentFromSharingURL:share:fileURL:appName:appIconData:withReply:"
- "makeAnimator"
- "makeBannerController"
- "makeContentViewController"
- "makeDestinationQueryController"
- "makeLabel"
- "makeLabelWithString:"
- "makeScreenSharingStateMonitorWithCall:"
- "ntroller:animated:completion:"
- "removeFromShare:containerSetupInfo:withReply:"
- "removeFromShareFileURL:completionHandler:"
- "removeFromShareForFileURL:withReply:"
- "removeFromShareFromSharingURL:containerSetupInfo:withReply:"
- "setConversationDetailsView:"
- "setConversationSubtitleLabel:"
- "setConversationTitleLabel:"
- "setCustomCornerRadius:"
- "setEffectsAreAvailable:"
- "setEffectsAreEnabled:"
- "setEffectsButtonIsVisible:"
- "setEffectsPickerHidden:animated:"
- "setFrontBoardInterfaceOrientation:"
- "setHandedOffCall:"
- "setHasParticipantVideo:"
- "setInCallControlsDismissTimer:"
- "setInCallControlsState:"
- "setIsAmbient:"
- "setIsCaptioningEnabled:"
- "setIsDisplayedInBanner:"
- "setIsInRoster:"
- "setIsMomentsAvailable:"
- "setIsPipStashed:"
- "setIsPipped:"
- "setIsScreenSharing:"
- "setIsScreenSharingFullScreen:"
- "setKickMemberButton:"
- "setLatestRemoteControlDate:"
- "setLmiApproveButton:"
- "setLmiRejectButton:"
- "setLocalAudioTogglingDelegate:"
- "setLocalParticipantState:"
- "setLocalizedSenderIdentity:"
- "setMediaPipFrameInWindowScene:"
- "setOracleUsingController:contact:"
- "setOrganizationNameProvider:"
- "setPercentage:"
- "setRequesterIdentifier:"
- "setRingButton:"
- "setShouldHideViewsFromScreenSharing:"
- "setShouldOverrideShadowHidden:"
- "setShouldShowLeaveButton:"
- "setShowsViewfinder:"
- "setTransformForRemoteVideoOrientationEnabled:"
- "setUsesInternalCaptureSession:"
- "setVideoButtonIsEnabled:"
- "setVideoIsEnabled:"
- "setVideoLayerHost:forMode:"
- "set_deviceOrientation:"
- "setupRootView"
- "shareFileOrFolderShareURL:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:"
- "shareFileOrFolderURL:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:"
- "shareNameAndPhotoTappedWithButton:"
- "shareNameTappedWithButton:"
- "shareOrUpdateShareURL:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:completionHandler:"
- "sharedContentSourceName"
- "sharingStatusFor:withReply:"
- "shouldAlwaysPresentExpandedAppsFor:"
- "shouldAlwaysPresentExpandedAppsForEffectBrowserViewController:"
- "shouldDisconnectOnDismissal"
- "shouldHideViewsFromScreenSharing"
- "shouldOverrideShadowHidden"
- "shouldShowCallDetailsWhenReady"
- "shouldShowEndActivity"
- "shouldShowLeaveButton"
- "showAccessoryButtonEventsNoticeIfNeeded"
- "showCallDetailsButtonTapped"
- "showDefaultSystemHUD"
- "showGreenTea3PHUD"
- "showHandoffHUD"
- "showInCallHUD"
- "showLagunaPullConversationHUD"
- "showPTTHUD"
- "showRemoteParticipantNoticeIfNeeded"
- "showSidebar"
- "showTTRBannerWithFullLogArchive:"
- "slotForMode:"
- "startCountdown"
- "startFileSharing:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:withReply:"
- "startWithReason:"
- "statusViewTapped"
- "studioLightButton"
- "subtitleLabelContainer"
- "subviewForEffectsBrowserViewController"
- "supportedDeviceOrientations"
- "swapButtonTappedWithButton:"
- "tView"
- "tapContainer"
- "tapDoneButton"
- "tapStopRecording"
- "testing_didFinishLocalPreviewRotationAnimation"
- "titleLabelContainer"
- "toggleCinematicFraming"
- "toggleLocalOrientation"
- "toggleMicButtonTapped"
- "toggleMicButtonTappedWithButton:"
- "toggleReactionsView"
- "toggleStudioLight"
- "toggleVideoButtonTapped"
- "toggleVideoButtonTappedWithButton:"
- "toggleVideoMuteWithShouldPauseIfStopped:"
- "unansweredCallUIDismissed"
- "updateAudioRouteButtonFor:"
- "updateBackgroundStartPipAuthorizationState"
- "updateCallParticipantLabelsViewForViewController:"
- "updateConstraintsWith:controlsViewController:localParticipantView:effectsView:effectsBrowserViewController:"
- "updateControlsVisibilityForExpandedState:"
- "updateCountdownWith:"
- "updateFor:deviceOrientation:"
- "updatePillViewWithIsMuted:"
- "updateShare:containerSetupInfo:withReply:"
- "updateToRepresentLegacyCall:"
- "updateVideoState"
- "userNameAndEmail:containerSetupInfo:withReply:"
- "utteranceComplete"
- "videoButtonIsEnabled"
- "videoButtonTapped"
- "videoIsEnabled"
- "videoMessageButton"
- "videoPauseButton"
- "viewController:fullScreenFocusedParticipantAspectRatioChanged:participantGridIsFullScreen:"
- "viewController:fullScreenFocusedParticipantOrientationChanged:"
- "viewController:localParticipantAspectRatioChanged:"
- "viewController:mediaPipSafeAreaFrameChanged:"
- "viewController:pipSourceProviderNeedsUpdate:"
- "viewController:rubberBandConstrained:inRange:"
- "viewController:setStatusBarHidden:"
- "viewControllerDidRequestAddParticipants:"
- "viewControllerDidRequestTemporaryPreventSuspension:"
- "viewControllerForCall:"
- "viewControllerForPiP"
- "viewControllerMinimizedLocalPreview:"
- "wantsApplicationDismissalStyle"
- "wantsBannerWithoutScene"
- "wantsDismissal"
- "wantsStandardControls"
- "willDismissViewAnimated:"
- "willEnterForegroundNotification:"

```
