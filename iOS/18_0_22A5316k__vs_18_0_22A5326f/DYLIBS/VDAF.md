## VDAF

> `/System/Library/PrivateFrameworks/VDAF.framework/VDAF`

```diff

 24.0.0.0.0
-  __TEXT.__text: 0x87080
+  __TEXT.__text: 0x86944
   __TEXT.__auth_stubs: 0x1030
   __TEXT.__const: 0x2f20
   __TEXT.__swift5_typeref: 0x1124

   __TEXT.__unwind_info: 0x1950
   __TEXT.__eh_frame: 0x37b8
   __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x818

   __AUTH_CONST.__objc_const: 0x508
   __AUTH.__data: 0x3f8
   __DATA.__data: 0x15e0
-  __DATA.__objc_clsrolist: 0x40
   __DATA.__bss: 0x3c00
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 2375
-  Symbols:   4035
-  CStrings:  0
+  Symbols:   4043
+  CStrings:  111
 
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
+ "_$s20HealthRecordServices30ClinicalAccountSummaryTileTypeO12accountLoginyA2CmFWC"
+ "_$s20HealthRecordServices30ClinicalAccountSummaryTileTypeO14gatewayUpgradeyA2CmFWC"
+ "_$s20HealthRecordServices30ClinicalAccountSummaryTileTypeO19multiGatewayUpgradeyA2CmFWC"
+ "_$s20HealthRecordServices30ClinicalAccountSummaryTileTypeOMn"
+ "_$s20HealthRecordServices30ClinicalAccountSummaryTileTypeOSEAAMc"
+ "_HDHRSClinicalItemPropertyKeyExtractionFailureInfo"
+ "_HDHRSNotificationKeyValueDomainIdentifier"
+ "_HDHRSNotificationKeyValueDomainKey"
+ "_HDHealthRecordsIngestionServiceIdentifier"
+ "_HKClinicalDocumentDownloaderServiceIdentifier"
+ "_HKClinicalGatewayFeatureNameClinicalSharing"
+ "_HKClinicalOnboardingActivityKey"
+ "_HKClinicalOnboardingBatchIDKey"
+ "_HKClinicalOnboardingGatewayIDKey"
+ "_HKClinicalOnboardingOptionsKey"
+ "_HKClinicalOnboardingSourceIDKey"
+ "_HKClinicalSampleAccountGatewayIDPrefix"
+ "_HKClinicalSampleAccountProviderBatchIDPrefix"
+ "_HKClinicalSharingKeyValueDomainDomainName"
+ "_HKClinicalSharingServiceIdentifier"
+ "_HKClinicalSharingSyncObserverServiceIdentifier"
+ "_HKFHIRAttachmentContentMimeType"
+ "_HKHealthRecordsDaemonLaunchNotificationName"
+ "_HKHealthRecordsNotificationSyncClientIdentifier"
+ "_HKMedicalDownloadableAttachmentMetadataOriginalCreationDateKey"
+ "_HKSignedClinicalDataMetadataKeyCountryOfOrigin"
+ "_HKVerifiableHealthRecordsParsingErrorDomain"
+ "_HKVerifiableHealthRecordsParsingServiceIdentifier"
+ "_OBJC_CLASS_$_HDClinicalDataCollectionExtractionResult"
+ "_OBJC_CLASS_$_HDExtractionRequest"
+ "_OBJC_CLASS_$_HDExtractionResult"
+ "_OBJC_CLASS_$_HDFHIRJSONObject"
+ "_OBJC_CLASS_$_HDFHIRResourceObject"
+ "_OBJC_CLASS_$_HDHRSOriginalSignedClinicalDataRecord"
+ "_OBJC_CLASS_$_HDHRSSignedClinicalDataProcessingContextCollection"
+ "_OBJC_CLASS_$_HDHealthRecordsIngestionServiceClient"
+ "_OBJC_CLASS_$_HDHealthRecordsLegacyIngestionServiceClient"
+ "_OBJC_CLASS_$_HDHealthRecordsXPCServiceClient"
+ "_OBJC_CLASS_$_HDOriginalFHIRResourceObject"
+ "_OBJC_CLASS_$_HDReferenceExtractionRequest"
+ "_OBJC_CLASS_$_HDReferenceExtractionResult"
+ "_OBJC_CLASS_$_HKClinicalAccount"
+ "_OBJC_CLASS_$_HKClinicalAccountConnectionInformation"
+ "_OBJC_CLASS_$_HKClinicalAccountEvent"
+ "_OBJC_CLASS_$_HKClinicalAccountStore"
+ "_OBJC_CLASS_$_HKClinicalDocumentSpotlightSearchResult"
+ "_OBJC_CLASS_$_HKClinicalDocumentStore"
+ "_OBJC_CLASS_$_HKClinicalEphemeralAccount"
+ "_OBJC_CLASS_$_HKClinicalGateway"
+ "_OBJC_CLASS_$_HKClinicalIngestionOutcome"
+ "_OBJC_CLASS_$_HKClinicalIngestionStore"
+ "_OBJC_CLASS_$_HKClinicalProviderSearchQueryDescription"
+ "_OBJC_CLASS_$_HKClinicalProviderSearchResultsPage"
+ "_OBJC_CLASS_$_HKClinicalProviderServiceStore"
+ "_OBJC_CLASS_$_HKClinicalSampleAccountProvider"
+ "_OBJC_CLASS_$_HKClinicalSampleAccountProviderGateway"
+ "_OBJC_CLASS_$_HKClinicalSharingClient"
+ "_OBJC_CLASS_$_HKClinicalSharingSyncInfo"
+ "_OBJC_CLASS_$_HKClinicalSharingSyncResult"
+ "_OBJC_CLASS_$_HKFHIRCredential"
+ "_OBJC_CLASS_$_HKHealthRecordsDaemonConnection"
+ "_OBJC_CLASS_$_HKOAuth2Credential"
+ "_OBJC_CLASS_$_HKSignedClinicalDataParsingResult"
+ "_OBJC_CLASS_$_HKSignedClinicalDataRegistryIssuerEntry"
+ "_OBJC_CLASS_$_HKSignedClinicalDataRegistryPublicKeyEntry"
+ "_OBJC_CLASS_$_HKSignedClinicalDataSource"
+ "_OBJC_CLASS_$_HKSignedClinicalDataStore"
+ "_OBJC_CLASS_$_HRSSupportedFHIRConfiguration"
+ "_OBJC_METACLASS_$_HDClinicalDataCollectionExtractionResult"
+ "_OBJC_METACLASS_$_HDExtractionRequest"
+ "_OBJC_METACLASS_$_HDExtractionResult"
+ "_OBJC_METACLASS_$_HDFHIRJSONObject"
+ "_OBJC_METACLASS_$_HDFHIRResourceObject"
+ "_OBJC_METACLASS_$_HDHRSOriginalSignedClinicalDataRecord"
+ "_OBJC_METACLASS_$_HDHRSSignedClinicalDataProcessingContextCollection"
+ "_OBJC_METACLASS_$_HDHealthRecordsIngestionServiceClient"
+ "_OBJC_METACLASS_$_HDHealthRecordsLegacyIngestionServiceClient"
+ "_OBJC_METACLASS_$_HDHealthRecordsXPCServiceClient"
+ "_OBJC_METACLASS_$_HDOriginalFHIRResourceObject"
+ "_OBJC_METACLASS_$_HDReferenceExtractionRequest"
+ "_OBJC_METACLASS_$_HDReferenceExtractionResult"
+ "_OBJC_METACLASS_$_HKClinicalAccount"
+ "_OBJC_METACLASS_$_HKClinicalAccountConnectionInformation"
+ "_OBJC_METACLASS_$_HKClinicalAccountEvent"
+ "_OBJC_METACLASS_$_HKClinicalAccountStore"
+ "_OBJC_METACLASS_$_HKClinicalDocumentSpotlightSearchResult"
+ "_OBJC_METACLASS_$_HKClinicalDocumentStore"
+ "_OBJC_METACLASS_$_HKClinicalEphemeralAccount"
+ "_OBJC_METACLASS_$_HKClinicalGateway"
+ "_OBJC_METACLASS_$_HKClinicalIngestionOutcome"
+ "_OBJC_METACLASS_$_HKClinicalIngestionStore"
+ "_OBJC_METACLASS_$_HKClinicalProviderSearchQueryDescription"
+ "_OBJC_METACLASS_$_HKClinicalProviderSearchResultsPage"
+ "_OBJC_METACLASS_$_HKClinicalProviderServiceStore"
+ "_OBJC_METACLASS_$_HKClinicalSampleAccountProvider"
+ "_OBJC_METACLASS_$_HKClinicalSampleAccountProviderGateway"
+ "_OBJC_METACLASS_$_HKClinicalSharingClient"
+ "_OBJC_METACLASS_$_HKClinicalSharingSyncInfo"
+ "_OBJC_METACLASS_$_HKClinicalSharingSyncResult"
+ "_OBJC_METACLASS_$_HKFHIRCredential"
+ "_OBJC_METACLASS_$_HKHealthRecordsDaemonConnection"
+ "_OBJC_METACLASS_$_HKOAuth2Credential"
+ "_OBJC_METACLASS_$_HKSignedClinicalDataParsingResult"
+ "_OBJC_METACLASS_$_HKSignedClinicalDataRegistryIssuerEntry"
+ "_OBJC_METACLASS_$_HKSignedClinicalDataRegistryPublicKeyEntry"
+ "_OBJC_METACLASS_$_HKSignedClinicalDataSource"
+ "_OBJC_METACLASS_$_HKSignedClinicalDataStore"
+ "_OBJC_METACLASS_$_HRSSupportedFHIRConfiguration"
+ "_kHKHealthRecordsExtractionRulesVersion"
+ "_kHKSignedClinicalDataExtractionRulesVersion"
+ "ices30ClinicalAccountSummaryTileTypeOSeAAMc"

```
