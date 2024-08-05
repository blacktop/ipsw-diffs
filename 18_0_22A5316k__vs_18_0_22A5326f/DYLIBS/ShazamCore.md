## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore`

```diff

-295.0.0.0.0
-  __TEXT.__text: 0xb224
-  __TEXT.__auth_stubs: 0x7b0
+301.0.0.0.0
+  __TEXT.__text: 0xaf7c
+  __TEXT.__auth_stubs: 0x7a0
   __TEXT.__objc_methlist: 0xd78
   __TEXT.__const: 0x7a
   __TEXT.__cstring: 0xc7c
   __TEXT.__oslogstring: 0x49f
   __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__swift5_typeref: 0x60
+  __TEXT.__swift5_typeref: 0x5e
   __TEXT.__swift5_capture: 0x4c
-  __TEXT.__unwind_info: 0x428
+  __TEXT.__unwind_info: 0x420
   __TEXT.__eh_frame: 0x258
   __TEXT.__objc_classname: 0x1e7
   __TEXT.__objc_methname: 0x282d
   __TEXT.__objc_methtype: 0x53c
   __TEXT.__objc_stubs: 0x1c60
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x4b8
+  __DATA_CONST.__const: 0x4f8
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9c8
   __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3e0
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0xec0
   __AUTH_CONST.__objc_const: 0x20b0
-  __AUTH.__objc_data: 0x840
-  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0xd4
   __DATA.__data: 0x188
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x840
+  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MusicKit.framework/MusicKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 341
-  Symbols:   526
-  CStrings:  0
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 339
+  Symbols:   533
+  CStrings:  260
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_retain
CStrings:
+ "MobileDocumentReaderResponseV0c8IdentityD8ElementsV7AddressVMa"
+ "_$s7CoreIDV18MobileDocumentTypeV14driversLicenseACvgZ"
+ "_$s7CoreIDV18MobileDocumentTypeV14nationalIDCardyAC10Foundation6LocaleV6RegionVFZ"
+ "_$s7CoreIDV18MobileDocumentTypeV31isSupportedNationalIDCardRegionySb10Foundation6LocaleV0J0VFZ"
+ "_$s7CoreIDV18MobileDocumentTypeVMa"
+ "_$s7CoreIDV20MobileDocumentIssuerV16jurisdictionCodeSSvg"
+ "_$s7CoreIDV20MobileDocumentIssuerVMa"
+ "_$s7CoreIDV20MobileDocumentIssuerVMn"
+ "_$s7CoreIDV21ISO18013KnownDocTypesO16iso18013_5_1_mDLyA2CmFWC"
+ "_$s7CoreIDV21ISO18013KnownDocTypesO19japanNationalIDCardyA2CmFWC"
+ "_$s7CoreIDV21ISO18013KnownDocTypesOMa"
+ "_$s7CoreIDV21ISO18013KnownDocTypesOMn"
+ "_$s7CoreIDV21MobileDocumentElementV10familyNameACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV11dateOfBirthACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV16issuingAuthorityACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV17drivingPrivilegesACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV27documentDHSComplianceStatusACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV3ageACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV3sexACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV7addressACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV8portraitACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementV9givenNameACvgZ"
+ "_$s7CoreIDV21MobileDocumentElementVMn"
+ "_$s7CoreIDV23IdentityDocumentElementV10identifierSSvg"
+ "_$s7CoreIDV23IdentityDocumentElementV15RetentionIntentO11displayOnlyyA2EmFWC"
+ "_$s7CoreIDV23IdentityDocumentElementV15RetentionIntentO11doNotRetainyA2EmFWC"
+ "_$s7CoreIDV23IdentityDocumentElementV15RetentionIntentO6retainyAESi_tcAEmFWC"
+ "_$s7CoreIDV23IdentityDocumentElementV15RetentionIntentOMa"
+ "_$s7CoreIDV23IdentityDocumentElementV15retentionIntentAC09RetentionG0Ovg"
+ "_$s7CoreIDV23IdentityDocumentElementV9namespace10identifier15retentionIntentACSS_SSAC09RetentionI0OtcfC"
+ "_$s7CoreIDV23IdentityDocumentElementV9namespaceSSvg"
+ "_$s7CoreIDV23IdentityDocumentElementVMa"
+ "_$s7CoreIDV23IdentityDocumentElementVMn"
+ "_$s7CoreIDV27MobileDocumentReaderRequestV0D0V17ValidationOptionsV34useSystemTrustedIssuerCertificates010additionallM0AGSb_SaySo17SecCertificateRefaGtcfC"
+ "_$s7CoreIDV27MobileDocumentReaderRequestV0D0V17ValidationOptionsVMa"
+ "_$s7CoreIDV27MobileDocumentReaderRequestV0D0V4type16retainedElements011nonRetainedI0AeA0cD4TypeV_SayAA0cD7ElementVGAMtcfC"
+ "_$s7CoreIDV27MobileDocumentReaderRequestV0D0V4type19displayOnlyElementsAeA0cD4TypeV_SayAA0cD7ElementVGtcfC"
+ "_$s7CoreIDV27MobileDocumentReaderRequestV0D0VMa"
+ "_$s7CoreIDV27MobileDocumentReaderRequestV17sessionIdentifier8documentACSS_AC0D0VtcfC"
+ "_$s7CoreIDV27MobileDocumentReaderRequestVMa"
+ "_$s7CoreIDV27MobileDocumentReaderRequestVMn"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC010canRequestD0yyAA0cdeH0VYaKFTjTu"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC16readerIdentifierSSyYaKFTjTu"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO022documentReadConnectionG0yA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO07networkG0yA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO11nfcDisabledyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO11notEntitledyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO12hsa2DisabledyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO12invalidTokenyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO12notSupportedyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO14invalidRequestyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO14osNotSupportedyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO14passcodeNotSetyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO14sessionExpiredyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO15invalidResponseyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO17bluetoothDisabledyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO18serviceUnavailableyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO20documentReadTimedOutyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO22iCloudAccountSignedOutyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO27nfcNegotiatedHandoverFailedyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO28nfcOverheatProtectionEnabledyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO29documentReadAlreadyInProgressyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO36termsAndConditionsAcceptanceRequiredyAGSS_tcAGmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO7unknownyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO9cancelledyA2GmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5ErrorVsAdAMc"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5StateO10connectingyA2EmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5StateO16awaitingApprovalyA2EmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5StateO5readyyA2EmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5StateO8finishedyAeA0cdE8ResponseVcAEmFWC"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC5StateOMn"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC7prepare4withAA0cdE21ConfigurationResponseVAA0cdeI0V_tYaKFTjTu"
+ "_$s7CoreIDV27MobileDocumentReaderSessionC8merchant3forAA0cdE8MerchantVSgSS_tYaKFTjTu"
+ "_$s7CoreIDV27MobileDocumentReaderSessionCMn"
+ "_$s7CoreIDV28IdentityDocumentRelyingPartyVMn"
+ "_$s7CoreIDV28MobileDocumentReaderMerchantV10identifierSSSgvg"
+ "_$s7CoreIDV28MobileDocumentReaderMerchantV4nameSSvg"
+ "_$s7CoreIDV28MobileDocumentReaderMerchantV8logoData10Foundation0H0VSgvg"
+ "_$s7CoreIDV28MobileDocumentReaderMerchantVMa"
+ "_$s7CoreIDV28MobileDocumentReaderMerchantVMn"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV16DrivingPrivilegeV4CodeVMa"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV16IssuingAuthorityV12jurisdictionSSSgvg"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV16IssuingAuthorityV14isoCountryCodeSSSgvg"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV16IssuingAuthorityVMa"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV16IssuingAuthorityVMn"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV19DHSComplianceStatusO12noncompliantyA2GmFWC"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV19DHSComplianceStatusO9compliantyA2GmFWC"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV19DHSComplianceStatusOMa"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV19DHSComplianceStatusOMn"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV21AAMVADrivingPrivilegeV12VehicleClassV4codeSSvg"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV21AAMVADrivingPrivilegeV12VehicleClassVMn"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV21AAMVADrivingPrivilegeV18VehicleEndorsementVMa"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV21AAMVADrivingPrivilegeV18VehicleRestrictionV11descriptionSSvg"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV21AAMVADrivingPrivilegeV18VehicleRestrictionV4codeSSSgvg"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV21AAMVADrivingPrivilegeV18VehicleRestrictionVMa"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV3SexO12notSpecifiedyA2GmFWC"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV3SexO13notApplicableyA2GmFWC"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV3SexO4maleyA2GmFWC"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV3SexO6femaleyA2GmFWC"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV3SexO7unknownyA2GmFWC"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV3SexOMa"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV3SexOMn"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsV7AddressVMn"
+ "_$s7CoreIDV28MobileDocumentReaderResponseV0c8IdentityD8ElementsVMn"
+ "_$s7CoreIDV28MobileDocumentReaderResponseVMn"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO10ageAtLeastyAESi_tcAEmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO10postalCodeyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO11dateOfBirthyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO13veteranStatusyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO14documentNumberyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO14expirationDateyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO16individualNumberyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO16issuingAuthorityyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO17documentIssueDateyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO17drivingPrivilegesyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO27documentDHSComplianceStatusyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO3ageyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO3sexyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO4cityyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO4nameyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO5stateyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO6heightyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO6weightyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO7addressyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO7countryyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO8eyeColoryA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO8portraityA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO9birthYearyA2EmFWC"
+ "_$s7CoreIDV31IdentityDocumentElementCategoryV011PresentmentE5GroupO9hairColoryA2EmFWC"
+ "_$s7CoreIDV33IdentityDocumentPresentmentSourceO2eeoiySbAC_ACtFZ"
+ "_$s7CoreIDV33IdentityDocumentPresentmentSourceO3appyA2CmFWC"
+ "_$s7CoreIDV33IdentityDocumentPresentmentSourceO6readeryA2CmFWC"
+ "_$s7CoreIDV33IdentityDocumentPresentmentSourceOMa"
+ "_$s7CoreIDV33IdentityDocumentPresentmentSourceOMn"
+ "_$s7CoreIDV33MobileDocumentReaderConfigurationV25merchantServerAccessToken30userAcceptedTermsAndConditionsACSSSg_SbtcfC"
+ "_$s7CoreIDV33MobileDocumentReaderConfigurationVMa"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsV12documentType0H8ElementsACSgSS_SayAA0cdE0VGtcfC"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsV12documentTypeAA21ISO18013KnownDocTypesOvg"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsV17retainingElementsSayAA0cdeF0VGvg"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsV18recognizedElementsSayAA0cdE0VGvg"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsV19displayOnlyElementsSayAA0cdeF0VGvg"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsV20notRetainingElementsSayAA0cdeF0VGvg"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsV22maximumRetentionPeriodSiSgvg"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsVMa"
+ "_$s7CoreIDV37IdentityDocumentElementCategoryGroupsVMn"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV06ClientE4InfoO12appleBrandedyAESSSg_tcAEmFWC"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV06ClientE4InfoO6customyAESS_So10CGImageRefaSgtcAEmFWC"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV06ClientE4InfoOMa"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV06ClientE4InfoOMn"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV06clientE4NameSSSgvg"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV17PresentationStyleO12consentSheetyA2EmFWC"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV17PresentationStyleO25transactionElementDetailsyA2EmFWC"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV17PresentationStyleOMn"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV32PersistedElementsStorageLifetimeO12indefinitelyyA2EmFWC"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV32PersistedElementsStorageLifetimeO5limityAESi_tcAEmFWC"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV32PersistedElementsStorageLifetimeOMa"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationV32PersistedElementsStorageLifetimeOMn"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationVMa"
+ "_$s7CoreIDV38DigitalPresentmentDisplayConfigurationVMn"
+ "_$s7CoreIDV40MobileDocumentReaderDeviceEngagementTypeO2eeoiySbAC_ACtFZ"
+ "_$s7CoreIDV40MobileDocumentReaderDeviceEngagementTypeO2qryAC10Foundation4DataV_tcACmFWC"
+ "_$s7CoreIDV40MobileDocumentReaderDeviceEngagementTypeO3nfcyA2CmFWC"
+ "_$s7CoreIDV40MobileDocumentReaderDeviceEngagementTypeOMa"
+ "_$s7CoreIDV40MobileDocumentReaderDeviceEngagementTypeOMn"
+ "_DIIdentityErrorDomain"
+ "_DIVerificationErrorDomain"
+ "_OBJC_CLASS_$_DIAttribute"
+ "_OBJC_CLASS_$_DIAttributeCamera"
+ "_OBJC_CLASS_$_DIAttributeCustom"
+ "_OBJC_CLASS_$_DIAttributeDate"
+ "_OBJC_CLASS_$_DIAttributeDocument"
+ "_OBJC_CLASS_$_DIAttributeDocumentScanRequirements"
+ "_OBJC_CLASS_$_DIAttributeFooter"
+ "_OBJC_CLASS_$_DIAttributeImage"
+ "_OBJC_CLASS_$_DIAttributeImageCaptureRequirements"
+ "_OBJC_CLASS_$_DIAttributeLabel"
+ "_OBJC_CLASS_$_DIAttributePicker"
+ "_OBJC_CLASS_$_DIAttributePickerItem"
+ "_OBJC_CLASS_$_DIAttributeSMSOTP"
+ "_OBJC_CLASS_$_DIAttributeText"
+ "_OBJC_CLASS_$_DIDocUploadSession"
+ "_OBJC_CLASS_$_DIDocUploadSettings"
+ "_OBJC_CLASS_$_DIExecutionFeedback"
+ "_OBJC_CLASS_$_DIFileUploadAsset"
+ "_OBJC_CLASS_$_DIIdentityAuthorizationController"
+ "_OBJC_CLASS_$_DIIdentityDocument"
+ "_OBJC_CLASS_$_DIIdentityDriversLicenseDescriptor"
+ "_OBJC_CLASS_$_DIIdentityElement"
+ "_OBJC_CLASS_$_DIIdentityIntentToStore"
+ "_OBJC_CLASS_$_DIIdentityNationalIDCardDescriptor"
+ "_OBJC_CLASS_$_DIIdentityProofingSession"
+ "_OBJC_CLASS_$_DIIdentityProvisioningAttestations"
+ "_OBJC_CLASS_$_DIIdentityProvisioningSession"
+ "_OBJC_CLASS_$_DIIdentityProvisioningTransactionKey"
+ "_OBJC_CLASS_$_DIIdentityRequest"
+ "_OBJC_CLASS_$_DIUploadAsset"
+ "_OBJC_CLASS_$_DIVerificationSession"
+ "_OBJC_CLASS_$_DIVerificationSessionContext"
+ "_OBJC_CLASS_$_TRAccountsManager"
+ "_OBJC_CLASS_$_TRCompletionOperationHandler"
+ "_OBJC_CLASS_$_TRDeviceSetupBrowser"
+ "_OBJC_CLASS_$_TRHeartbeatRequest"
+ "_OBJC_CLASS_$_TRMessageDecoder"
+ "_OBJC_CLASS_$_TRMessageEncoder"
+ "_OBJC_CLASS_$_TRResponseMessage"
+ "_OBJC_CLASS_$_TRTransferBrowser"
+ "_OBJC_METACLASS_$_DIAttribute"
+ "_OBJC_METACLASS_$_DIAttributeCamera"
+ "_OBJC_METACLASS_$_DIAttributeCustom"
+ "_OBJC_METACLASS_$_DIAttributeDate"
+ "_OBJC_METACLASS_$_DIAttributeDocument"
+ "_OBJC_METACLASS_$_DIAttributeDocumentScanRequirements"
+ "_OBJC_METACLASS_$_DIAttributeFooter"
+ "_OBJC_METACLASS_$_DIAttributeImage"
+ "_OBJC_METACLASS_$_DIAttributeImageCaptureRequirements"
+ "_OBJC_METACLASS_$_DIAttributeLabel"
+ "_OBJC_METACLASS_$_DIAttributePicker"
+ "_OBJC_METACLASS_$_DIAttributePickerItem"
+ "_OBJC_METACLASS_$_DIAttributeSMSOTP"
+ "_OBJC_METACLASS_$_DIAttributeText"
+ "_OBJC_METACLASS_$_DIDocUploadSession"
+ "_OBJC_METACLASS_$_DIDocUploadSettings"
+ "_OBJC_METACLASS_$_DIExecutionFeedback"
+ "_OBJC_METACLASS_$_DIFileUploadAsset"
+ "_OBJC_METACLASS_$_DIIdentityAuthorizationController"
+ "_OBJC_METACLASS_$_DIIdentityDocument"
+ "_OBJC_METACLASS_$_DIIdentityDriversLicenseDescriptor"
+ "_OBJC_METACLASS_$_DIIdentityElement"
+ "_OBJC_METACLASS_$_DIIdentityIntentToStore"
+ "_OBJC_METACLASS_$_DIIdentityNationalIDCardDescriptor"
+ "_OBJC_METACLASS_$_DIIdentityProofingSession"
+ "_OBJC_METACLASS_$_DIIdentityProvisioningAttestations"
+ "_OBJC_METACLASS_$_DIIdentityProvisioningSession"
+ "_OBJC_METACLASS_$_DIIdentityProvisioningTransactionKey"
+ "_OBJC_METACLASS_$_DIIdentityRequest"
+ "_OBJC_METACLASS_$_DIPage"
+ "_OBJC_METACLASS_$_DIUploadAsset"
+ "_OBJC_METACLASS_$_DIVerificationSession"
+ "_OBJC_METACLASS_$_DIVerificationSessionContext"
+ "_OBJC_METACLASS_$_TRAccountsManager"
+ "_OBJC_METACLASS_$_TRCompletionOperationHandler"
+ "_OBJC_METACLASS_$_TRDeviceSetupBrowser"
+ "_OBJC_METACLASS_$_TRHeartbeatRequest"
+ "_OBJC_METACLASS_$_TRMessageDecoder"
+ "_OBJC_METACLASS_$_TRMessageEncoder"
+ "_OBJC_METACLASS_$_TRResponseMessage"
+ "_OBJC_METACLASS_$_TRTransferBrowser"
+ "_kDIHttpHeaderAppleWebServiceSession"
+ "_kDIHttpHeaderAuthorization"
+ "_kDISharingOptionHttpHeader"
+ "_qpod_conn_create"
+ "_qpod_conn_decode_datagram"
+ "_qpod_conn_encode_datagram"
+ "_qpod_conn_free"
+ "_quic_fillout_definition_callbacks"
+ "_quic_shorthand_describe_entry"
+ "ge"
+ "ionV17PresentationStyleOMa"
+ "reIDV27MobileDocumentReaderRequestV0D0V4type16retainedElements011nonRetainedI017validationOptionsAeA0cD4TypeV_SayAA0cD7ElementVGAnE010ValidationM0VtcfC"
+ "yDocumentElementCategoryVG_A2qA016IdentityDocumentdM0OAC012PresentationO0OAC09PersistedjpQ0OSgAC06ClienteT0OSgSSSgA0_A0_AA21ISO18013KnownDocTypesOtcfC"

```
