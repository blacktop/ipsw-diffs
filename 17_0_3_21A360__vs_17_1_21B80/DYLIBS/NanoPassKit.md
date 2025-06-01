## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1149.0.0.0.0
-  __TEXT.__text: 0x211540
-  __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__objc_methlist: 0x203ec
+1160.0.0.0.0
+  __TEXT.__text: 0x2119e4
+  __TEXT.__auth_stubs: 0x17f0
+  __TEXT.__objc_methlist: 0x20404
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x1663a
-  __TEXT.__oslogstring: 0x284fe
-  __TEXT.__gcc_except_tab: 0x3c5c
+  __TEXT.__cstring: 0x1665c
+  __TEXT.__oslogstring: 0x28570
+  __TEXT.__gcc_except_tab: 0x3c80
   __TEXT.__dlopen_cstrs: 0x2eb
   __TEXT.__ustring: 0x160
-  __TEXT.__unwind_info: 0x7e94
+  __TEXT.__unwind_info: 0x7eac
   __TEXT.__objc_classname: 0x646d
-  __TEXT.__objc_methname: 0x3b73a
-  __TEXT.__objc_methtype: 0x95a1
-  __TEXT.__objc_stubs: 0x200a0
-  __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__const: 0x63c8
+  __TEXT.__objc_methname: 0x3b834
+  __TEXT.__objc_methtype: 0x95e6
+  __TEXT.__objc_stubs: 0x20120
+  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__const: 0x63f0
   __DATA_CONST.__objc_classlist: 0x10a0
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x392f0
-  __DATA_CONST.__objc_selrefs: 0xb5a8
+  __DATA_CONST.__objc_const: 0x39330
+  __DATA_CONST.__objc_selrefs: 0xb5c8
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__cfstring: 0xe1e0
   __AUTH_CONST.__objc_const: 0xc320

   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH_CONST.__auth_got: 0xc08
   __AUTH.__objc_data: 0xa5f0
   __DATA.__objc_protorefs: 0x90
   __DATA.__objc_classrefs: 0x1460

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AC28E469-1919-3582-ACAD-A513E3D2A2E0
-  Functions: 13009
-  Symbols:   39003
-  CStrings:  16083
+  UUID: 6402E488-9DC5-3E1F-BAA2-4619ECE20E29
+  Functions: 13012
+  Symbols:   39019
+  CStrings:  16092
 
Symbols:
+ -[NPKPassAssociatedInfoModel _commutePlanFieldsWithBalancesByID:dynamicPlansByID:]
+ -[NPKPaymentWebServiceCompanionTargetDevice _addCompanionDevicePhoneNumberDataIfNeededWithFields:toDeviceMetadata:]
+ -[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForSecureElementPass:encrypted:completion:]
+ GCC_except_table290
+ GCC_except_table295
+ GCC_except_table300
+ GCC_except_table306
+ GCC_except_table311
+ GCC_except_table318
+ GCC_except_table325
+ GCC_except_table330
+ GCC_except_table335
+ GCC_except_table340
+ GCC_except_table345
+ GCC_except_table359
+ GCC_except_table364
+ GCC_except_table375
+ GCC_except_table382
+ GCC_except_table400
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table416
+ GCC_except_table421
+ GCC_except_table432
+ GCC_except_table435
+ GCC_except_table444
+ GCC_except_table449
+ GCC_except_table451
+ GCC_except_table457
+ GCC_except_table465
+ GCC_except_table470
+ GCC_except_table479
+ GCC_except_table481
+ GCC_except_table487
+ GCC_except_table492
+ GCC_except_table497
+ GCC_except_table503
+ GCC_except_table509
+ GCC_except_table514
+ GCC_except_table521
+ GCC_except_table524
+ GCC_except_table526
+ GCC_except_table537
+ GCC_except_table539
+ GCC_except_table549
+ GCC_except_table557
+ GCC_except_table563
+ GCC_except_table572
+ GCC_except_table577
+ GCC_except_table582
+ GCC_except_table587
+ GCC_except_table592
+ GCC_except_table597
+ GCC_except_table602
+ GCC_except_table607
+ GCC_except_table612
+ GCC_except_table619
+ GCC_except_table625
+ GCC_except_table630
+ GCC_except_table635
+ GCC_except_table640
+ GCC_except_table648
+ GCC_except_table656
+ GCC_except_table662
+ GCC_except_table667
+ GCC_except_table672
+ GCC_except_table678
+ GCC_except_table684
+ GCC_except_table691
+ GCC_except_table696
+ GCC_except_table702
+ GCC_except_table704
+ GCC_except_table713
+ GCC_except_table719
+ GCC_except_table726
+ GCC_except_table731
+ GCC_except_table736
+ GCC_except_table742
+ GCC_except_table747
+ GCC_except_table758
+ GCC_except_table782
+ _PKCurrencyStorageIntegerToCurrencyDecimal
+ _PKDevicePhoneNumberSignature
+ _PKEnableDynamicSEAllocationIsWatch
+ _PKTransitAppletDataFormatNavigo
+ ___100-[NPKPaymentWebServiceCompanionTargetDevice prepareProvisioningTarget:checkFamilyCircle:completion:]_block_invoke.835
+ ___101-[NPKPaymentWebServiceCompanionTargetDevice performDeviceRegistrationForReason:brokerURL:completion:]_block_invoke.725
+ ___101-[NPKPaymentWebServiceCompanionTargetDevice performDeviceRegistrationForReason:brokerURL:completion:]_block_invoke_2.730
+ ___105-[NPKPaymentWebServiceCompanionTargetDevice revokeShareForPassIdentifier:share:shouldCascade:completion:]_block_invoke.806
+ ___105-[NPKPaymentWebServiceCompanionTargetDevice updateShareForPassIdentifier:share:authorization:completion:]_block_invoke.840
+ ___106-[NPKPaymentWebServiceCompanionTargetDevice generateSEEncryptionCertificateForSubCredentialId:completion:]_block_invoke.789
+ ___106-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForSecureElementPass:encrypted:completion:]_block_invoke
+ ___107-[NPKPaymentWebServiceCompanionTargetDevice createShareForPartialShareInvitation:authorization:completion:]_block_invoke.823
+ ___107-[NPKPaymentWebServiceCompanionTargetDevice generateISOEncryptionCertificateForSubCredentialId:completion:]_block_invoke.779
+ ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:passOwnershipTokenWithIdentifier:completion:]_block_invoke.714
+ ___108-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:passSharesForCredentialIdentifier:completion:]_block_invoke.809
+ ___113-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForPassWithUniqueIdentifier:encrypted:completion:]_block_invoke.860
+ ___113-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForPassWithUniqueIdentifier:encrypted:completion:]_block_invoke.862
+ ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:canAddSecureElementPassWithConfiguration:completion:]_block_invoke.650
+ ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:generateTransactionKeyWithParameters:withCompletion:]_block_invoke.786
+ ___117-[NPKPaymentWebServiceCompanionTargetDevice longTermPrivacyKeyForCredentialGroupIdentifier:reuseExisting:completion:]_block_invoke.799
+ ___118-[NPKPaymentWebServiceCompanionTargetDevice cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.847
+ ___122-[NPKPaymentWebServiceCompanionTargetDevice _trackOutstandingRequestWithMessageIdentifier:completionHandler:errorHandler:]_block_invoke.893
+ ___127-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:completion:]_block_invoke.701
+ ___127-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:completion:]_block_invoke.705
+ ___128-[NPKPaymentWebServiceCompanionTargetDevice checkFidoKeyPresenceForRelyingParty:relyingPartyAccountHash:fidoKeyHash:completion:]_block_invoke.773
+ ___136-[NPKPaymentWebServiceCompanionTargetDevice createFidoKeyForRelyingParty:relyingPartyAccountHash:challenge:externalizedAuth:completion:]_block_invoke.761
+ ___137-[NPKPaymentWebServiceCompanionTargetDevice requestPasscodeUpgradeForPasscodeUpgradeFlowController:withVisibleViewController:completion:]_block_invoke.638
+ ___137-[NPKPaymentWebServiceCompanionTargetDevice requestPasscodeUpgradeForPasscodeUpgradeFlowController:withVisibleViewController:completion:]_block_invoke_2.640
+ ___148-[NPKPaymentWebServiceCompanionTargetDevice _singleExpressTransitPassPaymentWebService:handlePotentialExpressPassInformation:withCompletionHandler:]_block_invoke.585
+ ___148-[NPKPaymentWebServiceCompanionTargetDevice _singleExpressTransitPassPaymentWebService:handlePotentialExpressPassInformation:withCompletionHandler:]_block_invoke.588
+ ___170-[NPKPaymentWebServiceCompanionTargetDevice _multipleExpressTransitPassPaymentWebService:handlePotentialExpressPassInformation:upgradeRequest:pass:withCompletionHandler:]_block_invoke.579
+ ___170-[NPKPaymentWebServiceCompanionTargetDevice _multipleExpressTransitPassPaymentWebService:handlePotentialExpressPassInformation:upgradeRequest:pass:withCompletionHandler:]_block_invoke.582
+ ___170-[NPKPaymentWebServiceCompanionTargetDevice signWithFidoKeyForRelyingParty:relyingPartyAccountHash:fidoKeyHash:challenge:publicKeyIdentifier:externalizedAuth:completion:]_block_invoke.776
+ ___76-[NPKPaymentWebServiceCompanionTargetDevice productsWithRequest:completion:]_block_invoke.560
+ ___78-[NPKPaymentWebServiceCompanionTargetDevice accountWithIdentifier:completion:]_block_invoke.553
+ ___82-[NPKPassAssociatedInfoModel _commutePlanFieldsWithBalancesByID:dynamicPlansByID:]_block_invoke
+ ___82-[NPKPaymentWebServiceCompanionTargetDevice addISO18013Blobs:cardType:completion:]_block_invoke.793
+ ___86-[NPKPaymentWebServiceCompanionTargetDevice statusForShareableCredentials:completion:]_block_invoke.830
+ ___88-[NPKPaymentWebServiceCompanionTargetDevice photosForFamilyMembersWithDSIDs:completion:]_block_invoke.734
+ ___91-[NPKPaymentWebServiceCompanionTargetDevice hasActiveExternallySharedPassesWithCompletion:]_block_invoke.890
+ ___91-[NPKPaymentWebServiceCompanionTargetDevice requestAndStoreExternalizedAuthWithCompletion:]_block_invoke.782
+ ___92-[NPKPaymentWebServiceCompanionTargetDevice _displayableSharesForPassIdentifier:completion:]_block_invoke.813
+ ___92-[NPKPaymentWebServiceCompanionTargetDevice prewarmCreateShareForPassIdentifier:completion:]_block_invoke.820
+ ___93-[NPKPaymentWebServiceCompanionTargetDevice paymentSetupFeaturesForConfiguration:completion:]_block_invoke.873
+ ___95-[NPKPaymentWebServiceCompanionTargetDevice checkInvitationStatusForMailboxAddress:completion:]_block_invoke.827
+ ___96-[NPKPaymentWebServiceCompanionTargetDevice featureApplicationsForAccountIdentifier:completion:]_block_invoke.745
+ ___97-[NPKPaymentWebServiceCompanionTargetDevice retrieveShareInvitationForMailboxAddress:completion:]_block_invoke.802
+ ___98-[NPKPaymentWebServiceCompanionTargetDevice _canAddSecureElementPassWithConfiguration:completion:]_block_invoke.655
+ ___98-[NPKPaymentWebServiceCompanionTargetDevice _displayableEntitlementsForPassIdentifier:completion:]_block_invoke.816
+ ___99-[NPKPaymentWebServiceCompanionTargetDevice acceptCarKeyShareForMessage:activationCode:completion:]_block_invoke.843
+ ___99-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:deviceMetadataWithFields:completion:]_block_invoke_3
+ ___block_descriptor_56_e8_32bs40w_e33_v16?0"PKPaymentDeviceMetadata"8lw40l8s32l8
+ ___block_literal_global.598
+ ___block_literal_global.604
+ ___block_literal_global.613
+ ___block_literal_global.621
+ ___block_literal_global.867
+ _kCarrierPhoneNumberSignature
+ _kCarrierPhoneNumberSignatureVersion
+ _objc_msgSend$_addCompanionDevicePhoneNumberDataIfNeededWithFields:toDeviceMetadata:
+ _objc_msgSend$_commutePlanFieldsWithBalancesByID:dynamicPlansByID:
+ _objc_msgSend$remoteContentConfiguration
+ _objc_msgSend$serviceProviderDataForSecureElementPass:encrypted:completion:
+ _objc_msgSend$setSignedPhoneNumber:
+ _objc_msgSend$setSignedPhoneNumberVersion:
- -[NPKPassAssociatedInfoModel _commutePlanFieldsWithBalancesByID:commutePlansByID:]
- GCC_except_table294
- GCC_except_table299
- GCC_except_table305
- GCC_except_table310
- GCC_except_table317
- GCC_except_table324
- GCC_except_table329
- GCC_except_table334
- GCC_except_table339
- GCC_except_table344
- GCC_except_table358
- GCC_except_table363
- GCC_except_table374
- GCC_except_table381
- GCC_except_table399
- GCC_except_table408
- GCC_except_table410
- GCC_except_table415
- GCC_except_table420
- GCC_except_table431
- GCC_except_table434
- GCC_except_table443
- GCC_except_table448
- GCC_except_table450
- GCC_except_table456
- GCC_except_table464
- GCC_except_table469
- GCC_except_table478
- GCC_except_table480
- GCC_except_table486
- GCC_except_table491
- GCC_except_table496
- GCC_except_table502
- GCC_except_table508
- GCC_except_table513
- GCC_except_table520
- GCC_except_table523
- GCC_except_table525
- GCC_except_table536
- GCC_except_table538
- GCC_except_table548
- GCC_except_table556
- GCC_except_table562
- GCC_except_table571
- GCC_except_table576
- GCC_except_table581
- GCC_except_table586
- GCC_except_table591
- GCC_except_table596
- GCC_except_table601
- GCC_except_table606
- GCC_except_table611
- GCC_except_table618
- GCC_except_table624
- GCC_except_table629
- GCC_except_table634
- GCC_except_table639
- GCC_except_table647
- GCC_except_table655
- GCC_except_table661
- GCC_except_table666
- GCC_except_table671
- GCC_except_table677
- GCC_except_table683
- GCC_except_table690
- GCC_except_table695
- GCC_except_table701
- GCC_except_table703
- GCC_except_table711
- GCC_except_table717
- GCC_except_table724
- GCC_except_table729
- GCC_except_table734
- GCC_except_table740
- GCC_except_table745
- GCC_except_table755
- GCC_except_table779
- _PKCurrencyStorageIntegerToDecimal
- _PKEnableDynamicSEAllocation
- ___100-[NPKPaymentWebServiceCompanionTargetDevice prepareProvisioningTarget:checkFamilyCircle:completion:]_block_invoke.834
- ___101-[NPKPaymentWebServiceCompanionTargetDevice performDeviceRegistrationForReason:brokerURL:completion:]_block_invoke.723
- ___101-[NPKPaymentWebServiceCompanionTargetDevice performDeviceRegistrationForReason:brokerURL:completion:]_block_invoke_2.729
- ___105-[NPKPaymentWebServiceCompanionTargetDevice encryptedServiceProviderDataForSecureElementPass:completion:]_block_invoke
- ___105-[NPKPaymentWebServiceCompanionTargetDevice revokeShareForPassIdentifier:share:shouldCascade:completion:]_block_invoke.805
- ___105-[NPKPaymentWebServiceCompanionTargetDevice updateShareForPassIdentifier:share:authorization:completion:]_block_invoke.839
- ___106-[NPKPaymentWebServiceCompanionTargetDevice generateSEEncryptionCertificateForSubCredentialId:completion:]_block_invoke.788
- ___107-[NPKPaymentWebServiceCompanionTargetDevice createShareForPartialShareInvitation:authorization:completion:]_block_invoke.822
- ___107-[NPKPaymentWebServiceCompanionTargetDevice generateISOEncryptionCertificateForSubCredentialId:completion:]_block_invoke.778
- ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:passOwnershipTokenWithIdentifier:completion:]_block_invoke.713
- ___108-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:passSharesForCredentialIdentifier:completion:]_block_invoke.808
- ___113-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForPassWithUniqueIdentifier:encrypted:completion:]_block_invoke.856
- ___113-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForPassWithUniqueIdentifier:encrypted:completion:]_block_invoke.858
- ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:canAddSecureElementPassWithConfiguration:completion:]_block_invoke.649
- ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:generateTransactionKeyWithParameters:withCompletion:]_block_invoke.785
- ___117-[NPKPaymentWebServiceCompanionTargetDevice longTermPrivacyKeyForCredentialGroupIdentifier:reuseExisting:completion:]_block_invoke.798
- ___118-[NPKPaymentWebServiceCompanionTargetDevice cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.846
- ___122-[NPKPaymentWebServiceCompanionTargetDevice _trackOutstandingRequestWithMessageIdentifier:completionHandler:errorHandler:]_block_invoke.889
- ___127-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:completion:]_block_invoke.700
- ___127-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:completion:]_block_invoke.702
- ___128-[NPKPaymentWebServiceCompanionTargetDevice checkFidoKeyPresenceForRelyingParty:relyingPartyAccountHash:fidoKeyHash:completion:]_block_invoke.772
- ___136-[NPKPaymentWebServiceCompanionTargetDevice createFidoKeyForRelyingParty:relyingPartyAccountHash:challenge:externalizedAuth:completion:]_block_invoke.760
- ___137-[NPKPaymentWebServiceCompanionTargetDevice requestPasscodeUpgradeForPasscodeUpgradeFlowController:withVisibleViewController:completion:]_block_invoke.637
- ___137-[NPKPaymentWebServiceCompanionTargetDevice requestPasscodeUpgradeForPasscodeUpgradeFlowController:withVisibleViewController:completion:]_block_invoke_2.639
- ___148-[NPKPaymentWebServiceCompanionTargetDevice _singleExpressTransitPassPaymentWebService:handlePotentialExpressPassInformation:withCompletionHandler:]_block_invoke.584
- ___148-[NPKPaymentWebServiceCompanionTargetDevice _singleExpressTransitPassPaymentWebService:handlePotentialExpressPassInformation:withCompletionHandler:]_block_invoke.587
- ___170-[NPKPaymentWebServiceCompanionTargetDevice _multipleExpressTransitPassPaymentWebService:handlePotentialExpressPassInformation:upgradeRequest:pass:withCompletionHandler:]_block_invoke.577
- ___170-[NPKPaymentWebServiceCompanionTargetDevice _multipleExpressTransitPassPaymentWebService:handlePotentialExpressPassInformation:upgradeRequest:pass:withCompletionHandler:]_block_invoke.581
- ___170-[NPKPaymentWebServiceCompanionTargetDevice signWithFidoKeyForRelyingParty:relyingPartyAccountHash:fidoKeyHash:challenge:publicKeyIdentifier:externalizedAuth:completion:]_block_invoke.775
- ___76-[NPKPaymentWebServiceCompanionTargetDevice productsWithRequest:completion:]_block_invoke.559
- ___78-[NPKPaymentWebServiceCompanionTargetDevice accountWithIdentifier:completion:]_block_invoke.552
- ___82-[NPKPassAssociatedInfoModel _commutePlanFieldsWithBalancesByID:commutePlansByID:]_block_invoke
- ___82-[NPKPaymentWebServiceCompanionTargetDevice addISO18013Blobs:cardType:completion:]_block_invoke.792
- ___86-[NPKPaymentWebServiceCompanionTargetDevice statusForShareableCredentials:completion:]_block_invoke.829
- ___88-[NPKPaymentWebServiceCompanionTargetDevice photosForFamilyMembersWithDSIDs:completion:]_block_invoke.733
- ___91-[NPKPaymentWebServiceCompanionTargetDevice hasActiveExternallySharedPassesWithCompletion:]_block_invoke.886
- ___91-[NPKPaymentWebServiceCompanionTargetDevice requestAndStoreExternalizedAuthWithCompletion:]_block_invoke.781
- ___92-[NPKPaymentWebServiceCompanionTargetDevice _displayableSharesForPassIdentifier:completion:]_block_invoke.812
- ___92-[NPKPaymentWebServiceCompanionTargetDevice prewarmCreateShareForPassIdentifier:completion:]_block_invoke.819
- ___93-[NPKPaymentWebServiceCompanionTargetDevice paymentSetupFeaturesForConfiguration:completion:]_block_invoke.869
- ___95-[NPKPaymentWebServiceCompanionTargetDevice checkInvitationStatusForMailboxAddress:completion:]_block_invoke.826
- ___96-[NPKPaymentWebServiceCompanionTargetDevice featureApplicationsForAccountIdentifier:completion:]_block_invoke.744
- ___97-[NPKPaymentWebServiceCompanionTargetDevice retrieveShareInvitationForMailboxAddress:completion:]_block_invoke.801
- ___98-[NPKPaymentWebServiceCompanionTargetDevice _canAddSecureElementPassWithConfiguration:completion:]_block_invoke.654
- ___98-[NPKPaymentWebServiceCompanionTargetDevice _displayableEntitlementsForPassIdentifier:completion:]_block_invoke.815
- ___99-[NPKPaymentWebServiceCompanionTargetDevice acceptCarKeyShareForMessage:activationCode:completion:]_block_invoke.842
- ___block_literal_global.597
- ___block_literal_global.603
- ___block_literal_global.612
- ___block_literal_global.620
- ___block_literal_global.863
- _objc_msgSend$_commutePlanFieldsWithBalancesByID:commutePlansByID:
- _objc_msgSend$hasRemoteContent
CStrings:
+ "Notice: Device Metadata: Phone number %@ to be added"
+ "Notice: Device Metadata: Phone number data not applicable for family device"
+ "Notice: Device Metadata: Phone number signature (%lu characters long) and version %@ to be added"
+ "Notice: Device Metadata: Verifying whether phone number data needs to be added for fields: %lu"
+ "_addCompanionDevicePhoneNumberDataIfNeededWithFields:toDeviceMetadata:"
+ "_commutePlanFieldsWithBalancesByID:dynamicPlansByID:"
+ "creditRecoveryPaymentPlansChangedForAccountIdentifier:"
+ "remoteContentConfiguration"
+ "serviceProviderDataForSecureElementPass:encrypted:completion:"
+ "setSignedPhoneNumber:"
+ "setSignedPhoneNumberVersion:"
+ "v16@?0@\"PKPaymentDeviceMetadata\"8"
+ "v36@0:8@\"PKSecureElementPass\"16B24@?<v@?@\"NSDictionary\"@\"NSError\">28"
- "Notice: NPKPassAssociatedInfoModel: Adding commute plan %@ with identifier %@ to plansByIdentifier dictionary"
- "Notice: NPKPassAssociatedInfoModel: Missing commute plan in commutePlansByIDs with identifier:%@"
- "_commutePlanFieldsWithBalancesByID:commutePlansByID:"
- "hasRemoteContent"

```
