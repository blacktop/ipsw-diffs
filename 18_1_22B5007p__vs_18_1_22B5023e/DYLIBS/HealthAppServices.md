## HealthAppServices

> `/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices`

```diff

-5132.0.0.0.0
-  __TEXT.__text: 0x1df84
+5200.1.3.0.0
+  __TEXT.__text: 0x1db88
   __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_methlist: 0x58c
   __TEXT.__const: 0xde2

   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x768
+  __TEXT.__unwind_info: 0x770
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x1df
   __TEXT.__objc_methname: 0x18f9
   __TEXT.__objc_methtype: 0x2e9
   __TEXT.__objc_stubs: 0xd60
   __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48

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
   Functions: 781
-  Symbols:   348
-  CStrings:  394
+  Symbols:   356
+  CStrings:  403
 
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
+ "PrimaryAccountNumber:expirationDate:"
+ "cheduleNotifications:"
+ "fier:webMerchantName:merchantName:adamIdentifier:isMerchantTokenRequest:isMultiTokenRequest:channel:channelType:supportedNetworks:suppressionMode:"
+ "initWithTransactionAmount:currencyCode:merchantCountryCode:merchantIdentifier:originURL:webMerchantIdentifier:webMerchantName:merchantName:adamIdentifier:supportedNetworks:merchantCapabilities:payLaterSuppressionMode:options:"
+ "initWithTransactionAmount:optionIdentifierToCancel:authenticationState:stateMachineError:stateMachineCancelReason:completion:"
+ "initWithTransactionIdentifier:amount:foreignAmount:foreignCurrencyExchangeRate:transactionDate:transactionStatusChangedDate:type:status:transactionDescription:originalTransactionDescription:localizedTypeDescription:creditDebitIndicator:actions:isBankConnectTransaction:merchantCategoryCode:hasNotificationServiceData:paymentHash:altDSID:insights:"
+ "initWithTransactionIdentifier:orderTypeIdentifier:orderIdentifier:webServiceBaseURL:authenticationToken:"
+ "initWithTransactionServiceIdentifier:recordName:recordType:zoneName:altDSID:"
+ "initWithTransactionSource:"
+ "initWithTransactionSourceCollection:account:"
+ "initWithTransactionSourceCollection:account:accountUser:"
+ "initWithTransactionSourceCollection:paymentDataProvider:"
+ "initWithTransactionSourceIdentifier:accountIdentifier:accountType:accountEventIdentifier:altDSID:zoneName:"
+ "initWithTransactionSourceIdentifier:accountIdentifier:accountType:serviceIdentifier:altDSID:zoneName:"
+ "initWithTransactionSourceIdentifier:type:"
+ "initWithTransactionSources:"
+ "initWithTransactionType:transactionSourceCollection:paymentDataProvider:"
+ "initWithTransitAppletBalance:balanceField:"
+ "initWithTransitAppletState:paymentApplication:fieldCollection:"
+ "initWithTransitCommutePlan:"
+ "initWithTransportIdentifier:invitation:share:"
+ "initWithType:archived:cloudStoreZone:"
+ "initWithType:completion:"
+ "initWithType:dictionary:"
+ "initWithType:identifier:subIdentifier:"
+ "initWithType:monetaryValue:value:"
+ "initWithType:pendingProvisioning:"
+ "initWithType:recordType:recordUniqueID:timestamp:"
+ "initWithType:selectedOfferIdentifier:paymentPass:criteriaIdentifier:sessionIdentifier:serviceProviderData:"
+ "initWithType:state:underlyingCredentialState:address:"
+ "initWithURL:expectedPairedReaderIdentifier:expectedProvisioningCredentialHash:"
+ "initWithUnavailableFundingSourceTopicForAccount:"
+ "initWithUniqueIdentifier:status:"
+ "initWithUnknownCount:foodAndDrinksCount:shoppingCount:travelCount:servicesCount:funCount:healthCount:transportCount:"
+ "initWithUpdateReason:"
+ "initWithUpdatedAt:fallbackCategory:merchant:brand:"
+ "initWithVPANPaymentCredentialResponse:privateKey:error:"
+ "initWithValue:currencyCode:"
+ "initWithValueAddedServiceTransaction:"
+ "initWithVersion:ephemeralPublicKey:publicKeyHash:encryptedRequest:"
+ "initWithVersion:rules:discoveryItems:engagementMessagesMetadata:"
+ "initWithVertical:type:genericSharingDict:appleSharingDict:"
+ "initWithWebService:"
+ "initWithWebService:addPaymentPassToLibrary:"
+ "initWithWebService:connection:"
+ "initWithWebService:localPaymentService:"
+ "initWithWebService:paymentSetupRequest:"
+ "initWithWebService:registrationMetadata:configurationType:"
+ "initWithWebServiceDictionary:"
+ "initWithWithXPCObject:hash:"
+ "initWithWithXPCObject:length:isSharedMemory:offset:hash:"
+ "initWithZoneID:databaseIdentifier:"
+ "initWithZoneName:creationDate:originDeviceIdentifier:originDeviceName:"
+ "initalizeCloudStoreIfNecessaryWithHandler:"
+ "initialAmount"
+ "initialBarcodeFetchCount"
+ "initialRemotePaymentInstrument"
+ "initialSuggestedAmount"
+ "initialTransactionAmount"
+ "initializeAccountAttestationIfNecessaryWithCompletion:"
+ "initializedViaInitWithCoder"
+ "initiative"
+ "initiativeContext"
+ "inlineDescription"
+ "inlineDescriptionKey"
+ "insertAfterSection"
+ "insertAndUpdateAccountWithAdditionalFinancingPlans:completion:"
+ "insertAndUpdateAccountWithNewPlanType:installmentCount:principalAmount:apr:daysSinceTransactionStart:merchant:completion:"
+ "insertDailyCashNotificationForAccountIdentifier:completion:"
+ "insertDiscoveryEngagementMessages:completion:"
+ "insertDiscoveryItems:discoveryArticleLayouts:completion:"
+ "insertEvents:withAccountidentifier:completion:"
+ "insertOrUpdateAccountEnhancedMerchants:accountIdentifier:completion:"
+ "insertOrUpdateAccountPromotions:accountIdentifier:completion:"
+ "insertOrUpdateArchiveLocationWithCloudStoreZone:isArchived:insertionMode:"
+ "insertOrUpdateDeviceOriginatedNearbyPeerPaymentTransactionWithIdentifier:memo:counterpartAppearanceData:completion:"
+ "insertOrUpdateInStoreTopUpToken:accountIdentifier:completion:"
+ "insertOrUpdateLocalAccount:completion:"
+ "insertOrUpdateNearbyPeerPaymentSetupNotificationWithTransactionIdentifier:amount:currency:senderName:completion:"
+ "insertOrUpdatePaymentRewardsRedemption:withPassUniqueIdentifier:completion:"
+ "insertOrUpdatePeerPaymentPendingRequests:shouldScheduleNotifications:completion:"
+ "insertOrUpdatePendingApplePayOrder:"
+ "insertOrUpdateRecurringPayments:completion:"
+ "insertOrUpdateValueAddedServiceTransaction:forPassUniqueIdentifier:paymentTransaction:handler:"
+ "insertPassField:"
+ "insertPaymentApplication:"
+ "insertRule:completion:"
+ "insertSummaryNotificationForAccountIdentifier:summaryType:completion:"
+ "insertTransactionAndEventsWithConfiguration:completion:"
+ "insetsSeparatorByTextOffset"
+ "insights"
+ "installment"
+ "installmentAgreementIdentifier"
+ "installmentAmount"
+ "installmentAmountMultiple"
+ "installmentAmounts"
+ "installmentAssessment"
+ "installmentAuthorizationAmount"
+ "installmentAuthorizationToken"
+ "installmentBalance"
+ "isEqualToSavingsAccountFeatureDescriptor:"
+ "isEqualToSeat:"
+ "isEqualToServiceProviderPurchase:"
+ "isEqualToServiceProviderPurchaseAction:"
+ "isEqualToShareableCredential:"
+ "isEqualToSharedAccountCloudStore:"
+ "isEqualToSharedAccountCloudStoreZone:"
+ "isEqualToShippingMethod:"
+ "isEqualToShippingMethods:"
+ "isEqualToTransactionAuthenticationContext:"
+ "isEqualToTransactionAuthenticationResult:"
+ "isEqualToTransactionReceipt:"
+ "isEqualToTransactionReceiptHeaderField:"
+ "isEqualToTransactionReceiptSummaryItem:"
+ "isEqualToTransitAppletHistoryRecord:"
+ "isEqualToUnresolvedAccessory:"
+ "isEqualToUnresolvedImage:"
+ "isEqualToUnresolvedMetadata:"
+ "isEqualToUnresolvedState:"
+ "isEqualToUnresolvedValue:"
+ "isEqualToWorldRegion:"
+ "isEquivalentToCatalog:"
+ "isExpectedFailureReason:"
+ "isExpiredBasedOnSigningDate"
+ "isExpiredForDate:"
+ "isExpiredInCalendar:"
+ "isExposed"
+ "isExpress"
+ "isExpressModeEnabledForRemotePassUniqueIdentifier:handler:"
+ "isExpressModeSetupOptional"
+ "isExpressModeSupportedForPass:"
+ "isExternalOfferCredential"
+ "isFamilyName:validFormatForCountryCode:"
+ "isFeatureNotSupportedError"
+ "isFieldTypeFooter"
+ "isFieldTypeLabel"
+ "isFieldTypePicker"
+ "isFirstInQueue"
+ "isFollowupAction"
+ "isFollowupProvisioning"
+ "isFollowupSetupAssistant"
+ "isForLocalDevice"
+ "isForWatch"
+ "isFreshForNow:"
+ "isFromBackgroundProvisioning"
+ "isFullBleed"
+ "isFuzzyMatched"
+ "isGivenName:validFormatForCountryCode:"
+ "isGraduation"
+ "isGreenCarTicketUsed"
+ "isGroupTile"
+ "isGroupType"
+ "isGroupType:"
+ "isHideMyEmail"
+ "isHideMyEmailLoading"
+ "isHomeAccessRestrictedForPassSerialNumber:withCompletion:"
+ "isHomeKeyCredential"
+ "isHomeKeyPass"
+ "isHomeShare"
+ "isHybridIdentityPass"
+ "isIdentityCredential"
+ "isIdentityPass"
+ "isIgnorable"
+ "isImageSetLoaded:"
+ "isImageSetType:equalToImageSetTypeFromObject:"
+ "isInDisasterRecovery"
+ "isInGoodStanding"
+ "isInMonthOfMerge"
+ "isInShinkansenStation"
+ "isInStation"
+ "isInStorePurchase"
+ "isInTerminalState"
+ "isIncludedInRegions:"
+ "isIncompatible"
+ "isInformalRequestToken"
+ "isInitializationTimeOutError"
+ "isInlineSummaryItemsEligible"
+ "isIntegrationTypeSupported:"
+ "isIssuerAppProvisioningSupported"
+ "isIssuerInstallmentTransaction"
+ "isIssuerProvisioningExtensionCredential"
+ "isKeychainSyncingInProgress"
+ "isLastUpdatedOutOfDate:fetchPeriod:"
+ "isLocalAppletSubcredentialPassCredential"
+ "isLocalPassCredential"
+ "isLocalShare"
+ "isLowBalanceGateNotificationEnabled"
+ "isManagingEntitlementConfiguration"
+ "isManagingTimeConfiguration"
+ "isManateeEnabled"
+ "isManateeNotAvailableError"
+ "isMeCardCachingEnabled"
+ "isMerchantTokenRequest"
+ "isMerchantTokenTransaction"
+ "isMiniCardsAllowed"
+ "isMock"
+ "isMultiTokenRequest"
+ "isMultiTokensRequest"
+ "isNFCExpressEnabled"
+ "isNetworkUnavailable"
+ "isNewRecurringPayment"
+ "isNewerThan:"
+ "isNewerThanCatalog:"
+ "isNextInstallmentPastDue"
+ "isNumeric"
+ "isNumericFractional"
+ "isOctopusPass"
+ "isOnHoldForAccount:"
+ "isOnlineImmobilizerToken"
+ "isOrderManagementDisabled"
+ "isOrderManagementNotificationsDisabled"
+ "isOutOfDate"
+ "isOwnerSharing"
+ "isPCSError"
+ "isPariticipantAccountEmbargoRecovery"
+ "isPariticipantAccountSecurityDowngraded"
+ "isParsedTransitApplication"
+ "isPartialError"
+ "isPartialErrorWithUnkownItems"
+ "isParticipantAccountLockedByOwner"
+ "isParticipantMayNeedVerificationError"
+ "isPass"
+ "isPassCatalog"
+ "isPassbookVisibleWithHandler:"
+ "isPasscodeUpgradeRequired"
+ "isPayLaterPass"
+ "isPayLaterPaymentRequest"
+ "isPayLaterSupportedInCurrentRegion"
+ "isPaymentAccount"
+ "isPaymentHandoffDisabled"
+ "isPaymentOffersError"
+ "isPaymentOptionSelectable"
+ "isPaymentPassActivationAvailableWithHandler:"
+ "isPaymentPassRelevant:"
+ "isPaymentSummaryPinned"
+ "isPeerPaymentCredential"
+ "isPeerPaymentPass"
+ "isPeerPaymentRequest"
+ "isPersonalizable"
+ "isPhoneticFamilyName:validFormatForCountryCode:"
+ "isPhoneticGivenName:validFormatForCountryCode:"
+ "isPlanDisplayable"
+ "isPortraitElement:"
+ "isPostalAddressFieldEntry:validForPostalFieldKey:forCountryCode:"
+ "isPrecursorCredential"
+ "isPrecursorPass:"
+ "isPrepaidPass"
+ "isPrivateLabel"
+ "isProvisioningForAltAccount"
+ "isPurchasedProductCredential"
+ "isQuantitative"
+ "isRecurring"
+ "isRecurringPayment"
+ "isRedeemable"
+ "isRefunded"
+ "isRelatedToState:"
+ "isRemoteAsset"
+ "isRemoteCredential"
+ "isRemotePass"
+ "isRestrictedGuestInAllowedPeriod"
+ "isRevokable"
+ "isSRD"
+ "isSafariCredential"
+ "isSameInvitationAsInvitation:"
+ "isSameUnderlyingShareAs:"
+ "isSecureText"
+ "isSecureVisibleText"
+ "isServerDriven"
+ "isServerGenerated"
+ "isSetupAssistantProvisioningSupported"
+ "isShareableCredential"
+ "isSharedCredential"
+ "isSharingChannelBlockedForChannel:isRecipientKnownContact:"
+ "isShellPass"
+ "isShieldRequiredWithCompletionHandler:"
+ "isShinkansenTicketActive"
+ "isShippingEditable"
+ "isSleeve"
+ "isSpinnerEnabled"
+ "isStateFinal:"
+ "isStatefulTransferCredential"
+ "isStatic"
+ "isStoredValuePass"
+ "isSubsetOfMeCard"
+ "isSuicaPass"
+ "isSupportedByDevice:"
+ "isSupportedDictionaryKeyType:"
+ "isSupportedOnDevice:"
+ "isSuppressing"
+ "isTaggedForAllowInAppPaymentFailureRetry"
+ "isTaggedForFactor:"
+ "isTaggedForLineItemsInMainPaymentSheet"
+ "isTall"
+ "isTerminalStatus"
+ "isThirdPartyCrossPlatformInvitation"
+ "isTransactionSourceIdentifierRelevant:"
+ "isTransitPass"
+ "isTrustedRelyingParty"
+ "isUWBExpressEnabled"
+ "isUnknownItemError"
+ "isUnknownNearbyPeerPayment"
+ "isUnrecoverableDecryptionError"
+ "isUpgradeEligible"
+ "isUserChoice"
+ "isVPANAutoFillSupported:"
+ "isValidCharacterSet"
+ "isValidFromKeychain"
+ "isValidStartingState:"
+ "isValidStateTransitionFrom:to:"
+ "isValidWithAPIType:withError:"
+ "isValidWithError:errorStatus:"
+ "isValidWithUnableReason:"
+ "isValueAccepted:"
+ "isVirtualCardEnrollmentRequest"
+ "isVirtualCardRefreshRequest"
+ "isVirtualCardRequest"
+ "isVoided"
+ "isWaitingOnConfirmationForHandoff"
+ "isWaitingOnUserAction"
+ "isWalletForeground"
+ "isWatchIssuerAppProvisioningSupportedWithHandler:"
+ "isWatchSupportedForProduct:"
+ "isWebPaymentRequest"
+ "isYesterday"
+ "isZeroTransaction"
+ "isZipFile"
+ "isZoneNotFoundError"
+ "iso18013BlobsForSecureElementIdentifiers:"
+ "iso18013BlobsMetdataForSecureElementIdentifiers:"
+ "isoCredentialIdentifier"
+ "isoDeviceEncryptionAttestation"
+ "isoDeviceEncryptionAuthorization"
+ "isoFormat"
+ "isoIdentifier"
+ "isoProperties"
+ "issueReportIdentifier"
+ "issueType"
+ "issuedOnTheWeb"
+ "issuerAdministrativeAreaCode"
+ "issuerBindingInformation"
+ "issuerCountryCode"
+ "issuerIdentifier"
+ "issuerInstallmentManagementURL"
+ "issuerName"
+ "issuerProvisioningExtensionCredential"
+ "issuingAuthorityElement"
+ "itemForType:"
+ "itemIdentifierForAccountUser:"
+ "itemIdentifierForPass:"
+ "itemOfItemType:recordName:completion:"
+ "itemOfItemType:recordName:qualityOfService:completion:"
+ "itemOfItemTypeFromAllZones:recordName:qualityOfService:completion:"
+ "itemTypeFromRecord:"
+ "itemWithLocalURL:passURL:dictionary:error:"
+ "itemWithProtobuf:"
+ "itemWithRelativePath:"
+ "itemsMissingFromDevice"
+ "joinedDate"
+ "jsblCounter"
+ "jsonArrayRepresentation"
+ "jsonArrayRepresentationWithCertificatesResponse:"
+ "jsonArrayValue"
+ "jsonDataOptional"
+ "jsonDictionaryRepresentationWithCertificatesResponse:"
+ "jsonNonZeroUnsignedLongLongNSNumberArrayValue"
+ "jsonNonZeroUnsignedLongLongNSNumberSetValue"
+ "jsonRepresentationForAccountUserAccessLevel:"
+ "jsonStringSetValue"
+ "k0p7Rchr49btq6wB:HY6FXG20397zwmVg:"
+ "k4eQYhyzyebbQqys:"
+ "keepPaddingCharactersForSubmission"
+ "kextBlacklistVersion"
+ "key:oldValue:newValue:message:forHunkAtIndex:"
+ "keyAttestation"
+ "keyAttestationAuthority"
+ "keyCreationMetadata"
+ "keyForProductType:optionIdentifier:"
+ "keyInformation"
+ "keyMaterialHashForDeviceCredentialType"
+ "keyPairingSession:didFinishPairingWithKey:trackingRequest:error:"
+ "keyReferenceIdentifier"
+ "keyRequestWithSubjectIdentifier:discretionaryData:localValidations:counterLimit:"
+ "keyboardAccessories"
+ "keychainCardCredentials"
+ "keychainDataWithError:"
+ "keychainItemData"
+ "keychainVirtualCard"
+ "knownManifestHashes"
+ "knownManifestHashesAtIndex:"
+ "knownManifestHashesCount"
+ "knownManifestHashesType"
+ "labelFieldObject"
+ "labelImage"
+ "languageDisclosureLocation"
+ "largeCardTemplateType"
+ "lastAddedDate"
+ "lastAutoFilledBySafari"
+ "lastDeviceCheckInBuildVersion"
+ "lastDeviceUpgradeTaskBuildVersion"
+ "lastDismissedDate"
+ "lastErrorIsSetupAssistantNotComplete"
+ "tAddress:quoteDestinationType:"
+ "ualToTransactionReceiptLineItem:"
- "T@\"NSNumber\",R,N,V_hasStyleFormatting"
- "T@\"NSNumber\",R,N,V_hasTable"
- "T@\"NSNumber\",R,N,V_hasTags"
- "T@\"NSNumber\",R,N,V_hasUpdates"
- "T@\"NSNumber\",R,N,V_importItemCount"
- "T@\"NSNumber\",R,N,V_isAllTagsSelected"
- "T@\"NSNumber\",R,N,V_isAutoConversionEnabled"
- "T@\"NSNumber\",R,N,V_isExistingMention"
- "T@\"NSNumber\",R,N,V_isExistingTag"
- "T@\"NSNumber\",R,N,V_isGlobalSession"
- "T@\"NSNumber\",R,N,V_isLocked"
- "T@\"NSNumber\",R,N,V_isNoteFoundByAttachment"
- "T@\"NSNumber\",R,N,V_isPasswordProtected"
- "T@\"NSNumber\",R,N,V_isResultSelected"
- "T@\"NSNumber\",R,N,V_isSaltRegenerated"
- "T@\"NSNumber\",R,N,V_isTimelineView"
- "T@\"NSNumber\",R,N,V_isTokenizedLink"
- "T@\"NSNumber\",R,N,V_isTopHit"
- "T@\"NSNumber\",R,N,V_isUserMentioned"
- "T@\"NSNumber\",R,N,V_lastTimeOfAttemptedSchedule"
- "T@\"NSNumber\",R,N,V_leftBound"
- "T@\"NSNumber\",R,N,V_localNotesEnabled"
- "T@\"NSNumber\",R,N,V_mathHandwritingEnabled"
- "T@\"NSNumber\",R,N,V_mathTextEnabled"
- "T@\"NSNumber\",R,N,V_maxMessageSizeInBytes"
- "T@\"NSNumber\",R,N,V_maxNumCharTyped"
- "T@\"NSNumber\",R,N,V_minimizedViewDuration"
- "T@\"NSNumber\",R,N,V_nonTopHitCount"
- "T@\"NSNumber\",R,N,V_nonTopHitRawCount"
- "T@\"NSNumber\",R,N,V_noteCount"
- "T@\"NSNumber\",R,N,V_notesCount"
- "T@\"NSNumber\",R,N,V_rightBound"
- "T@\"NSNumber\",R,N,V_searchStringLength"
- "T@\"NSNumber\",R,N,V_sectionAffordanceExposures"
- "T@\"NSNumber\",R,N,V_sectionAffordanceUsages"
- "T@\"NSNumber\",R,N,V_sessionDuration"
- "T@\"NSNumber\",R,N,V_sideBarViewDuration"
- "T@\"NSNumber\",R,N,V_startAcceptedCount"
- "T@\"NSNumber\",R,N,V_startFingerStrokeCount"
- "T@\"NSNumber\",R,N,V_startInvitedCount"
- "T@\"NSNumber\",R,N,V_startPageCount"
- "T@\"NSNumber\",R,N,V_startPencilStrokeCount"
- "T@\"NSNumber\",R,N,V_startTimestamp"
- "T@\"NSNumber\",R,N,V_startingColumnCount"
- "T@\"NSNumber\",R,N,V_startingRowCount"
- "T@\"NSNumber\",R,N,V_subFolderLevel"
- "T@\"NSNumber\",R,N,V_tableColumnCount"
- "T@\"NSNumber\",R,N,V_tableRowCount"
- "T@\"NSNumber\",R,N,V_topHitCount"
- "T@\"NSNumber\",R,N,V_topHitCountForLongestSearchString"
- "T@\"NSNumber\",R,N,V_totalChecklistCount"
- "T@\"NSNumber\",R,N,V_totalCountOfAudioAttachments"
- "T@\"NSNumber\",R,N,V_totalCountOfAudioAttachmentsRecordedInNotes"
- "T@\"NSNumber\",R,N,V_totalCountOfAudioAttachmentsWithAppendedAudio"
- "T@\"NSNumber\",R,N,V_totalCountOfCollaboratedScrapPapers"
- "T@\"NSNumber\",R,N,V_totalCountOfLockedNotes"
- "T@\"NSNumber\",R,N,V_totalCountOfLockedNotesWithDivergedMode"
- "T@\"NSNumber\",R,N,V_totalCountOfLockedNotesWithDivergedPassword"
- "T@\"NSNumber\",R,N,V_totalCountOfLockedScrapPapers"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesIsPinnedAndIsLocked"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentAudio"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentAudioSummary"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentAudioTranscript"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentDeepLink"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentDocScan"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentFullscreenDrawing"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentInlineDrawingV1"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentInlineDrawingV2"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentMapLink"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentOther"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentPaperKit"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentRichUrl"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithAttachmentTables"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithChecklistAndIsPinned"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollabAndChecklist"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollabAndDocScan"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollabAndFullscreenDrawing"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollabAndInlineDrawingV1"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollabAndInlineDrawingV2"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollabAndIsPinned"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollabAndOtherAttachments"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollabAndTables"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithCollapsedSections"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithDocScanAndChecklist"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithDocScanAndFullscreenDrawing"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithDocScanAndInlineDrawingV1"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithDocScanAndInlineDrawingV2"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithDocScanAndIsLocked"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithDocScanAndIsPinned"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithDocScanAndOtherAttachments"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithDocScanAndTables"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithFolderLinks"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithFullscreenDrawingAndChecklist"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithFullscreenDrawingAndIsLocked"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithFullscreenDrawingAndIsPinned"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithFullscreenDrawingAndOtherAttachments"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV1AndChecklist"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV1AndFullscreenDrawing"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV1AndInlineDrawingV2"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV1AndIsLocked"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV1AndIsPinned"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV1AndOtherAttachments"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV1AndTables"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV2AndChecklist"
- "T@\"NSNumber\",R,N,V_totalCountOfNotesWithInlineDrawingV2AndFullscreenDrawing"
- "TQ,N,V_countOfSmartFoldersWithPinnedNotesFilter"
- "TQ,N,V_countOfSmartFoldersWithQuickNotesFilter"
- "TQ,N,V_countOfSmartFoldersWithSharedFilter"
- "TQ,N,V_countOfSmartFoldersWithTagsFilter"
- "TQ,N,V_countOfSmartFoldersWithUnknownFilter"
- "TQ,N,V_countOfTags"
- "TQ,N,V_countOfV1LockedNotes"
- "TQ,N,V_countOfV2LockedNotes"
- "TQ,N,V_endFingerStrokeCount"
- "TQ,N,V_endPencilStrokeCount"
- "TQ,N,V_nonTopHitResultCount"
- "TQ,N,V_scrapPaperCount"
- "TQ,N,V_startFingerStrokeCount"
- "TQ,N,V_startMonth"
- "TQ,N,V_startYear"
- "TQ,N,V_topHitResultCount"
- "TQ,N,V_totalNoteCountIncludingSubFolders"
- "Tc,V_serverEnvironmentType"
- "Td,N,V_previousArea"
- "Td,N,V_valuePrecision"
- "Tq,N,V_lastUsedTool"
- "Tq,N,V_sessionTypeEnum"
- "Tq,R,N,V_accountPurpose"
- "Tq,R,N,V_actionMenuContextType"
- "Tq,R,N,V_actionMenuUsageType"
- "Tq,R,N,V_bioAuthType"
- "Tq,R,N,V_cellularRadioAccessTechnology"
- "Tq,R,N,V_checklistAction"
- "Tq,R,N,V_clickContext"
- "Tq,R,N,V_collabActivityContextPath"
- "Tq,R,N,V_collabNotificationAction"
- "Tq,R,N,V_collaborationAccessReason"
- "Tq,R,N,V_collaborationAccessType"
- "Tq,R,N,V_collaborationActionType"
- "Tq,R,N,V_collaborationInviteStep"
- "Tq,R,N,V_collaborationItemType"
- "Tq,R,N,V_collaborationStatus"
- "Tq,R,N,V_collaborationType"
- "Tq,R,N,V_contextPath"
- "Tq,R,N,V_conversionMethod"
- "Tq,R,N,V_docScanActionType"
- "Tq,R,N,V_docScanStage"
- "Tq,R,N,V_drawingActionType"
- "Tq,R,N,V_drawingTool"
- "Tq,R,N,V_endMode"
- "Tq,R,N,V_endReason"
- "Tq,R,N,V_endState"
- "Tq,R,N,V_errorStatus"
- "Tq,R,N,V_filterCondition"
- "Tq,R,N,V_folderLabelType"
- "Tq,R,N,V_folderType"
- "Tq,R,N,V_gmRankingStrategyType"
- "Tq,R,N,V_importFileType"
- "Tq,R,N,V_linkAddApproach"
- "Tq,R,N,V_linkContentType"
- "Tq,R,N,V_mentionAddApproach"
- "Tq,R,N,V_moveCheckedItemsToBottomSwitchSetting"
- "Tq,R,N,V_noteCreateApproach"
- "Tq,R,N,V_noteEditContext"
- "Tq,R,N,V_noteEditorCallOutBarButtonType"
- "Tq,R,N,V_noteType"
- "Tq,R,N,V_notesToPagesContextPath"
- "Tq,R,N,V_onboardingScreenType"
- "Tq,R,N,V_onboardingUserAction"
- "Tq,R,N,V_osInstallVariant"
- "Tq,R,N,V_paletteEngagementType"
- "Tq,R,N,V_palettePosition"
- "Tq,R,N,V_passwordType"
- "Tq,R,N,V_pdfState"
- "Tq,R,N,V_pwdModeChangeContextPath"
- "Tq,R,N,V_rankingStrategyType"
- "Tq,R,N,V_searchSuggestionType"
- "Tq,R,N,V_selectedResultAccountType"
- "Tq,R,N,V_selectedResultType"
- "Tq,R,N,V_sessionDetailType"
- "Tq,R,N,V_shareFlowType"
- "Tq,R,N,V_startMode"
- "Tq,R,N,V_startState"
- "Tq,R,N,V_switchSelectionType"
- "Tq,R,N,V_tagAddApproach"
- "Tq,R,N,V_tagDeleteApproach"
- "Tq,R,N,V_tagRenameApproach"
- "Tq,V_contextHolderCount"
- "Tq,V_deviceOrientationEnum"
- "_aaEndPointTypeName"
- "_aaTracker"
- "_aaTrackerName"
- "_accountData"
- "_accountHistogramManager"
- "_accountNotesTwoFactorSummary"
- "_accountSnapshotSummary"
- "_accountTypeSummary"
- "_actionMenuContextType"
- "_actionMenuSelection"
- "_actionMenuUsageType"
- "_appBuild"
- "_appDelegate"
- "_appSessionManager"
- "_attachmentCountPerNoteHistogram"
- "_attachmentHitCount"
- "_attachmentHitCountForLongestSearchString"
- "_attachmentSectionCount"
- "_attachmentSnapshotSummary"
- "_attachmentSummary"
- "_attachmentTypeUTI"
- "_attachmentUTISummary"
- "_attachmentsCount"
- "_audioSummaryEnabled"
- "_audioTranscriptEnabled"
- "_automaticAppUpdatesAllowed"
- "_avgMessageSizeInBytes"
- "_bioAuthType"
- "_bucketLeftBounds"
- "_charLength"
- "_charLengthOfQueryString"
- "_checklistAction"
- "_clickContext"
- "_collabActivityContextPath"
- "_collabFoldersSummary"
- "_collabNotesSummary"
- "_collabNotificationAction"
- "_collabOwnedRootFolderAcceptanceCountHistogram"
- "_collabOwnedRootFolderAcceptanceRatioHistogram"
- "_collabOwnedRootFolderInviteeCountHistogram"
- "_collabOwnedRootFolderNoReplyCountHistogram"
- "_collabOwnedSingleNoteAcceptanceCountHistogram"
- "_collabOwnedSingleNoteAcceptanceRatioHistogram"
- "_collabOwnedSingleNoteInviteeCountHistogram"
- "_collabOwnedSingleNoteNoReplyCountHistogram"
- "_collabRootFolderTotalNoteCountHistogram"
- "_collaborationAccessReason"
- "_collaborationAccessType"
- "_collaborationActionType"
- "_collaborationInviteStep"
- "_collaborationItemType"
- "_collaborationMethod"
- "_collaborationStatus"
- "_contextHolderCount"
- "_conversionMethod"
- "_countOfAcceptances"
- "_countOfAccounts"
- "_countOfAccountsByType"
- "_countOfAttachmentByUTI"
- "_countOfAttachmentOther"
- "_countOfAttachments"
- "_countOfCalculateGraphExpressions"
- "_countOfCalculateResults"
- "_countOfCheckedItems"
- "_countOfChecklists"
- "_countOfCollaboratorAdded"
- "_countOfCollaboratorRemoved"
- "_countOfCustomSmartFolders"
- "_countOfDistinctFolderLinks"
- "_countOfDistinctMentions"
- "_countOfDistinctNoteLinks"
- "_countOfDistinctTags"
- "_countOfFingerStrokes"
- "_countOfFolderLinks"
- "_countOfFullscreenDrawing"
- "_countOfFullscreenDrawingStrokes"
- "_countOfIgnoredMessages"
- "_countOfInlineDrawingV1"
- "_countOfInlineDrawingV1FingerStrokes"
- "_countOfInlineDrawingV1PencilStrokes"
- "_countOfInlineDrawingV2"
- "_countOfInlineDrawingV2FingerStrokes"
- "_countOfInlineDrawingV2PencilStrokes"
- "_countOfInvitees"
- "_countOfLockedNotes"
- "_countOfLockedNotesWithDivergedMode"
- "_countOfLockedNotesWithDivergedPassword"
- "_countOfLockedScrapPapers"
- "_countOfMentions"
- "_countOfMessagesReceived"
- "_countOfMessagesSent"
- "_countOfModernNotes"
- "_countOfModernNotesWithDrawing"
- "_countOfModernNotesWithImage"
- "_countOfModernNotesWithLinks"
- "_countOfModernNotesWithTable"
- "_countOfModernNotesWithWebHighlights"
- "_countOfNoteLinks"
- "_countOfNotes"
- "_countOfNotesByType"
- "_countOfNotesWithChecklists"
- "_countOfNotesWithCollapsedSections"
- "_countOfNotesWithDeepLink"
- "_countOfNotesWithDocScan"
- "_countOfNotesWithFolderLink"
- "_countOfNotesWithFullscreenDrawing"
- "_countOfNotesWithInlineDrawingV1"
- "_countOfNotesWithInlineDrawingV2"
- "_countOfNotesWithMapLink"
- "_countOfNotesWithMathUsage"
- "_countOfNotesWithMentions"
- "_countOfNotesWithNoteLink"
- "_countOfNotesWithOtherAttachments"
- "_countOfNotesWithPDF"
- "_countOfNotesWithPaperDocument"
- "_countOfNotesWithPaperKit"
- "_countOfNotesWithRichURL"
- "_countOfNotesWithTable"
- "_countOfNotesWithTags"
- "_countOfPencilStrokes"
- "_countOfPinnedNotes"
- "_countOfPinnedScrapPapers"
- "_countOfRecognizedHandwrittenCharacters"
- "_countOfRecognizedLines"
- "_countOfScrapPapers"
- "_countOfScrapPapersWithDocScan"
- "_countOfScrapPapersWithDrawing"
- "_countOfScrapPapersWithFullscreenDrawing"
- "_countOfScrapPapersWithImage"
- "_countOfScrapPapersWithInlineDrawingV1"
- "_countOfScrapPapersWithInlineDrawingV2"
- "_countOfScrapPapersWithLinks"
- "_countOfScrapPapersWithMapLink"
- "_countOfScrapPapersWithOtherAttachments"
- "_countOfScrapPapersWithRichUrl"
- "_countOfScrapPapersWithTables"
- "_countOfScrapPapersWithTags"
- "_countOfScrapPapersWithWebHighlights"
- "_countOfSelectedTags"
- "_countOfSmartFoldersWithAttachmentsFilter"
- "_countOfSmartFoldersWithChecklistsFilter"
- "_countOfSmartFoldersWithDateCreatedFilter"
- "_countOfSmartFoldersWithDateModifiedFilter"
- "_countOfSmartFoldersWithFoldersFilter"
- "_countOfSmartFoldersWithLockedNotesFilter"
- "_countOfSmartFoldersWithMentionsFilter"
- "_countOfSmartFoldersWithPinnedNotesFilter"
- "_countOfSmartFoldersWithQuickNotesFilter"
- "_countOfSmartFoldersWithSharedFilter"
- "_countOfSmartFoldersWithTagsFilter"
- "_countOfSmartFoldersWithUnknownFilter"
- "_countOfTables"
- "_countOfTags"
- "_countOfTotalItems"
- "_countOfUniqueAccounts"
- "_countOfUniqueDevices"
- "_countOfV1LockedNotes"
- "_countOfV2LockedNotes"
- "_countofNotes"
- "_countsForEachBucket"
- "_currentlyViewedNoteIdentifier"
- "_deletedNoteCount"
- "_deviceOrientationEnum"
- "_deviceSnapshotSummary"
- "_directNoteCount"
- "_distinctMentionCountPerNoteHistogram"
- "_docScanActionType"
- "_docScanID"
- "_docScanLength"
- "_docScanPageCountHistogram"
- "_docScanSnapshotSummary"
- "_docScanStage"
- "_drawingActionType"
- "_drawingCountPerNoteHistogram"
- "_drawingID"
- "_drawingRecognitionData"
- "_drawingSnapshotSummary"
- "_drawingTool"
- "_enabledFiltersArray"
- "_encryptedKVStore"
- "_endAcceptedCount"
- "_endFingerStrokeCount"
- "_endInvitedCount"
- "_endMode"
- "_endPageCount"
- "_endPencilStrokeCount"
- "_endSessionBackgroundTaskIdentifier"
- "_endSessionBackgroundTaskIdentifiersByWindowSceneIdentifier"
- "_endingColumnCount"
- "_exposureDataThreadUnsafe"
- "_fastSyncSessionId"
- "_filterCondition"
- "_findSessionData"
- "_flushManager"
- "_folderCollaborationMatrix"
- "_folderCreationApproach"
- "_folderLabelType"
- "_folderSnapshotSummary"
- "_fullErrorCode"
- "_fullHeightViewDuration"
- "asSmallStateUsage"
- "gCountPerNoteHistogram"
- "ithMentionsFilter"
- "llscreenDrawingAndTables"
- "tartPencilStrokeCount"

```