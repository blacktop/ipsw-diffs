## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1696.3.2.0.0
-  __TEXT.__text: 0x8f66e4
-  __TEXT.__objc_methlist: 0x72bf8
-  __TEXT.__const: 0x2d780
+1696.3.5.4.0
+  __TEXT.__text: 0x8fa138
+  __TEXT.__objc_methlist: 0x72d90
+  __TEXT.__const: 0x2d750
   __TEXT.__swift5_typeref: 0x8da0
-  __TEXT.__cstring: 0x7441c
+  __TEXT.__cstring: 0x7492f
   __TEXT.__constg_swiftt: 0x7588
   __TEXT.__swift5_reflstr: 0x664d
   __TEXT.__swift5_fieldmd: 0x7de0

   __TEXT.__swift5_proto: 0x13f0
   __TEXT.__swift5_types: 0x7f8
   __TEXT.__swift5_capture: 0x5454
-  __TEXT.__oslogstring: 0x3cc7a
+  __TEXT.__oslogstring: 0x3cd2f
   __TEXT.__swift_as_entry: 0x198
   __TEXT.__swift_as_ret: 0x1bc
   __TEXT.__swift_as_cont: 0x3ac
   __TEXT.__swift5_mpenum: 0x140
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x6bbc
+  __TEXT.__gcc_except_tab: 0x6bd0
   __TEXT.__ustring: 0x1e76
-  __TEXT.__unwind_info: 0x27360
+  __TEXT.__unwind_info: 0x27440
   __TEXT.__eh_frame: 0x8978
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x239e8
+  __DATA_CONST.__const: 0x23aa0
   __DATA_CONST.__objc_classlist: 0x3e48
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x254f8
+  __DATA_CONST.__objc_selrefs: 0x255b8
   __DATA_CONST.__objc_protorefs: 0x260
-  __DATA_CONST.__objc_superrefs: 0x3158
-  __DATA_CONST.__objc_arraydata: 0x2870
-  __DATA_CONST.__got: 0x53a0
-  __AUTH_CONST.__const: 0x27258
-  __AUTH_CONST.__cfstring: 0x7a740
-  __AUTH_CONST.__objc_const: 0xd08c0
-  __AUTH_CONST.__objc_arrayobj: 0xd20
-  __AUTH_CONST.__objc_intobj: 0x11d0
+  __DATA_CONST.__objc_superrefs: 0x3160
+  __DATA_CONST.__objc_arraydata: 0x2a78
+  __DATA_CONST.__got: 0x53a8
+  __AUTH_CONST.__const: 0x27298
+  __AUTH_CONST.__cfstring: 0x7b000
+  __AUTH_CONST.__objc_const: 0xd0a98
+  __AUTH_CONST.__objc_arrayobj: 0xd38
+  __AUTH_CONST.__objc_intobj: 0x11e8
   __AUTH_CONST.__objc_dictobj: 0x1608
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__auth_got: 0x3018

   __AUTH.__data: 0x59a8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x735c
+  __DATA.__objc_ivar: 0x7388
   __DATA.__data: 0xa2b0
   __DATA.__common: 0xc39
   __DATA_DIRTY.__objc_ivar: 0x1f58
   __DATA_DIRTY.__objc_data: 0x7940
   __DATA_DIRTY.__data: 0x188
-  __DATA_DIRTY.__bss: 0x1348
+  __DATA_DIRTY.__bss: 0x1390
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 55997
-  Symbols:   79277
-  CStrings:  21835
+  Functions: 56061
+  Symbols:   79368
+  CStrings:  21911
 
Symbols:
+ +[PKAnalyticsReporter(Attribution) reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:newToWalletUser:newToProductUser:]
+ +[PKAnalyticsReporter(Attribution) reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:newToWalletUser:newToProductUser:sessionIdentifier:]
+ +[PKAnalyticsReporter(Attribution) reportCashCampaignIdentifier:eventType:]
+ -[PKIssuerMessagingFlag expirationDate]
+ -[PKIssuerMessagingFlag setExpirationDate:]
+ -[PKPassLibrary addPendingCampaignAttribution:forPassUniqueIdentifier:]
+ -[PKPassLibrary campaignAttributionNewToStatusesWithCompletion:]
+ -[PKPaymentCredential(PKPaymentCredentialSubclassAdditions) compare:withBackedUpDefaultPaymentPassSerialNumber:demoteNonStandardFlowCredentials:]
+ -[PKPaymentService deleteUserNotificationReceiptForNotificationIdentifier:]
+ -[PKPaymentService insertUserNotificationReceiptForAccountIdentifier:deliveredDate:]
+ -[PKProvisioningAnalyticsSession _fetchCampaignAttributionNewToStatusesIfNeeded]
+ -[PKProvisioningAnalyticsSession _resolveCampaignAttributionNewToWalletUser]
+ -[PKProvisioningAnalyticsSession _setCampaignAttributionProvisionedPassUniqueIdentifier:onLocalDevice:]
+ -[PKProvisioningAnalyticsSession reportNCCCheck]
+ -[PKProvisioningAnalyticsSession setProvisionedPass:onLocalDevice:]
+ -[PKProvisioningAnalyticsSessionCampaignAttributionSubjectHandle reportNCCCheckWithState:]
+ -[PKProvisioningAnalyticsSessionStepReporter setProvisionedPass:onLocalDevice:]
+ -[PKProvisioningAnalyticsState campaignAttributionNewToProductUser]
+ -[PKProvisioningAnalyticsState campaignAttributionNewToWalletUser]
+ -[PKProvisioningAnalyticsState campaignAttributionReferralSource]
+ -[PKProvisioningAnalyticsState setCampaignAttributionNewToProductUser:]
+ -[PKProvisioningAnalyticsState setCampaignAttributionNewToWalletUser:]
+ -[PKSpotlightBaseDocumentProcessor fieldMapForFieldBuckets:duplicateKeys:]
+ -[PKSpotlightBaseDocumentProcessor isDonatableValue:]
+ -[PKSpotlightBoardingPassDocumentProcessor barcodeLegFromLegs:departureAirportCode:arrivalAirportCode:]
+ -[PKSpotlightBoardingPassDocumentProcessor carrierCodeForPassFlightNumber:barcodeAttributes:]
+ -[PKSpotlightBoardingPassDocumentProcessor departureDateForPass:]
+ -[PKSpotlightBoardingPassDocumentProcessor extractAttributesFromBarcodeOfPass:departureAirportCode:arrivalAirportCode:]
+ -[PKSpotlightBoardingPassDocumentProcessor isWellFormedBarcodeLeg:]
+ -[PKSpotlightBoardingPassDocumentProcessor passengerNameFromBarcodeName:]
+ -[PKSpotlightBoardingPassDocumentProcessor processDocument:]
+ -[PKSpotlightBoardingPassDocumentProcessor seatDesignationFromBarcodeSeat:]
+ -[PKUserNotificationReceipt initWithNotificationIdentifier:notificationType:accountIdentifier:accountBaseURL:requiresReporting:]
+ -[PKUserNotificationReceipt notificationType]
+ -[PKUserNotificationReceipt requiresReporting]
+ -[PKUserNotificationReceipt setNotificationType:]
+ -[PKUserNotificationReceipt setRequiresReporting:]
+ GCC_except_table113
+ GCC_except_table127
+ GCC_except_table133
+ GCC_except_table163
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table206
+ GCC_except_table262
+ GCC_except_table288
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table306
+ GCC_except_table308
+ GCC_except_table310
+ GCC_except_table323
+ GCC_except_table334
+ GCC_except_table337
+ GCC_except_table349
+ GCC_except_table373
+ GCC_except_table382
+ GCC_except_table386
+ GCC_except_table404
+ GCC_except_table425
+ GCC_except_table482
+ GCC_except_table495
+ GCC_except_table542
+ GCC_except_table546
+ GCC_except_table555
+ GCC_except_table565
+ GCC_except_table580
+ GCC_except_table583
+ GCC_except_table586
+ GCC_except_table589
+ GCC_except_table607
+ GCC_except_table775
+ GCC_except_table895
+ _MDItemEventFlightDepartureDateTime
+ _OBJC_IVAR_$_PKIssuerMessagingFlag._expirationDate
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._campaignAttributionNewToStatuses
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._campaignAttributionNewToStatusesGeneration
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._campaignAttributionQueue
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._didReportNCCCheck
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._didRequestCampaignAttributionNewToStatuses
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._didResolveCampaignAttributionNewToWalletUser
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._pendingCardReadyToUsePassUniqueIdentifier
+ _OBJC_IVAR_$_PKProvisioningAnalyticsState._campaignAttributionNewToProductUser
+ _OBJC_IVAR_$_PKProvisioningAnalyticsState._campaignAttributionNewToWalletUser
+ _OBJC_IVAR_$_PKUserNotificationReceipt._notificationType
+ _OBJC_IVAR_$_PKUserNotificationReceipt._requiresReporting
+ _PKAddPendingCampaignAttributionForPassUniqueIdentifier
+ _PKAnalyticsReportNewToCreditUserKey
+ _PKAnalyticsReportNewToDebitUserKey
+ _PKAnalyticsReportNewToTransitUserKey
+ _PKAnalyticsReportNewToWalletUserKey
+ _PKAnalyticsReporterAttributionAddLocalPendingCardReadyToUse
+ _PKAnalyticsReporterAttributionFetchNewToStatuses
+ _PKAnalyticsReporterAttributionSetLocalNewToStatusProvider
+ _PKAnalyticsReporterAttributionSetLocalPendingCardReadyToUseAddedHandler
+ _PKAnalyticsReporterAttributionSetPendingCardReadyToUse
+ _PKIssuerMessagingFlagExpirationDateFromRecord
+ _PKPassUniqueIdentifiersWithPendingCampaignAttribution
+ _PKPendingCampaignAttributionCampaignIdentifierKey
+ _PKPendingCampaignAttributionForPassUniqueIdentifier
+ _PKPendingCampaignAttributionNewToProductUserKey
+ _PKPendingCampaignAttributionNewToWalletUserKey
+ _PKPendingCampaignAttributionProductTypeKey
+ _PKPendingCampaignAttributionQueue
+ _PKPendingCampaignAttributionReferralSourceKey
+ _PKPendingCampaignAttributionSessionIDKey
+ _PKPendingCampaignAttributions
+ _PKRemoveExpiredPendingCampaignAttributions
+ _PKRemovePendingCampaignAttributionForPassUniqueIdentifier
+ _PKSetPendingCampaignAttributions
+ _PKURLActionRoutePeerPaymentSendOrRequest
+ ___145-[PKPaymentCredential(PKPaymentCredentialSubclassAdditions) compare:withBackedUpDefaultPaymentPassSerialNumber:demoteNonStandardFlowCredentials:]_block_invoke
+ ___38-[PKProvisioningAnalyticsSession stop]_block_invoke
+ ___42-[PKProvisioningAnalyticsSession setPass:]_block_invoke
+ ___48-[PKProvisioningAnalyticsSession reportNCCCheck]_block_invoke
+ ___57-[PKProvisioningAnalyticsSession resetForNewProductSetup]_block_invoke
+ ___64-[PKPassLibrary campaignAttributionNewToStatusesWithCompletion:]_block_invoke
+ ___67-[PKProvisioningAnalyticsSession setProvisionedPass:onLocalDevice:]_block_invoke
+ ___71-[PKPassLibrary addPendingCampaignAttribution:forPassUniqueIdentifier:]_block_invoke
+ ___75-[PKProvisioningAnalyticsSession setCampaignAttributionReferrerIdentifier:]_block_invoke
+ ___80-[PKProvisioningAnalyticsSession _fetchCampaignAttributionNewToStatusesIfNeeded]_block_invoke
+ ___80-[PKProvisioningAnalyticsSession reportProvisioningCompleteForReporter:success:]_block_invoke
+ ___91-[PKProvisioningAnalyticsSession initWithEnvironment:intent:referralSource:archivedParent:]_block_invoke
+ ___95-[PKProvisioningAnalyticsSession reportProvisioningStepForReporter:step:success:error:context:]_block_invoke
+ ___PKAnalyticsReporterAttributionAddLocalPendingCardReadyToUse_block_invoke
+ ___PKAnalyticsReporterAttributionFetchNewToStatuses_block_invoke
+ ___PKAnalyticsReporterAttributionFetchNewToStatuses_block_invoke_2
+ ___PKAnalyticsReporterAttributionFetchNewToStatuses_block_invoke_3
+ ___PKAnalyticsReporterAttributionSendEvent_block_invoke
+ ___PKAnalyticsReporterAttributionSendEvent_block_invoke_2
+ ___PKAnalyticsReporterAttributionSendEvent_block_invoke_3
+ ___PKPendingCampaignAttributionQueue_block_invoke
+ ___PKRemoveExpiredPendingCampaignAttributions_block_invoke
+ ___block_descriptor_48_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_48_e8_32w_e22_v16?0"NSDictionary"8lw32l8
+ ___swift_closure_destructor.42Tm
- +[PKAnalyticsReporter(Attribution) reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:]
- +[PKPaymentHeroImageController cardArtSizeForWatchViewSize:]
- +[PKTransitCommutePlan(Utilities) displayDateStringForCommutePlan:pass:balanceModel:style:allowsActivationPrompt:]
- -[PKPaymentHeroImageController cardArtSizeForSize:]
- -[PKPaymentHeroImageController setWatchSize:]
- -[PKPaymentHeroImageController watchSize]
- -[PKProvisioningAnalyticsSessionStepReporter setProvisionedPass:]
- -[PKUserNotificationReceipt initWithNotificationIdentifier:accountIdentifier:accountBaseURL:]
- GCC_except_table103
- GCC_except_table122
- GCC_except_table128
- GCC_except_table164
- GCC_except_table170
- GCC_except_table201
- GCC_except_table257
- GCC_except_table294
- GCC_except_table301
- GCC_except_table303
- GCC_except_table305
- GCC_except_table318
- GCC_except_table327
- GCC_except_table329
- GCC_except_table339
- GCC_except_table368
- GCC_except_table377
- GCC_except_table399
- GCC_except_table415
- GCC_except_table477
- GCC_except_table485
- GCC_except_table487
- GCC_except_table538
- GCC_except_table544
- GCC_except_table548
- GCC_except_table558
- GCC_except_table560
- GCC_except_table575
- GCC_except_table578
- GCC_except_table581
- GCC_except_table584
- GCC_except_table602
- GCC_except_table773
- GCC_except_table893
- GCC_except_table99
- _MDItemEventFlightBoardingDateTime
- _OBJC_IVAR_$_PKPaymentHeroImageController._watchSize
- ___112-[PKPaymentCredential(PKPaymentCredentialSubclassAdditions) compare:withBackedUpDefaultPaymentPassSerialNumber:]_block_invoke
CStrings:
+ "-[PKPassLibrary %@]: no extended interface; cardReadyToUse won't be reported for %@"
+ "Failed to write pending campaign attributions"
+ "PKPendingCampaignAttributions"
+ "Pending campaign attribution already exists for %@"
+ "^([A-Z]{2,3}|[A-Z][0-9]|[0-9][A-Z]) ?[0-9]{1,4}[A-Z]?$"
+ "^0*([1-9][0-9]{0,2}[A-Z])$"
+ "^[0-9]{1,4}$"
+ "^[A-Z0-9]{2,3}$"
+ "^[A-Z]{3}$"
+ "addMoneySuccess"
+ "appleAccount"
+ "arrival terminal"
+ "arrival_gate"
+ "arrival_terminal"
+ "arrivalterminal"
+ "boarding gate"
+ "boarding-gate"
+ "boarding_gate"
+ "boardinggate"
+ "booking"
+ "booking_reference"
+ "bookingreference"
+ "campaignAttributionNewToProductUser"
+ "campaignAttributionNewToWalletUser"
+ "cardReadyToUse"
+ "com.apple.passkit.attribution.teardown"
+ "com.apple.passkit.pendingcampaignattribution"
+ "com.apple.passkit.provisioninganalytics.attribution"
+ "conf #"
+ "conf#"
+ "confirmation number"
+ "confirmationcode"
+ "confirmationnumber"
+ "confnum"
+ "customer name"
+ "departingterminal"
+ "departure terminal"
+ "departure_gate"
+ "departure_terminal"
+ "departureterminal"
+ "destination gate"
+ "destination terminal"
+ "destinationgate"
+ "destinationterminal"
+ "flight #"
+ "flight no"
+ "flight no."
+ "flight_number"
+ "flightnb"
+ "flightno"
+ "gate number"
+ "gate_number"
+ "name of passenger"
+ "nccCheck"
+ "newToCreditUser"
+ "newToDebitUser"
+ "newToProductUser"
+ "newToTransitUser"
+ "newToWalletUser"
+ "passenger-name"
+ "passenger_name"
+ "record locator"
+ "record_locator"
+ "recordlocator"
+ "requestMoneySuccess"
+ "requiresReporting"
+ "requiresReporting: %@; "
+ "reservation"
+ "reservation number"
+ "seat no"
+ "seat no."
+ "seat_number"
+ "seatno"
+ "sendMoneySuccess"
+ "startAddMoney"
+ "startRequestMoney"
+ "startSendMoney"
+ "startSendOrRequestMoney"
+ "traveler"
+ "traveler name"
+ "travelername"
- " - "
- "boarding"
- "boarding time"
- "boardingtime"
- "boards"
```
