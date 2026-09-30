## HealthRecordsExtraction

> `/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x149338
-  __TEXT.__auth_stubs: 0x24e0
-  __TEXT.__objc_methlist: 0x17b4
-  __TEXT.__const: 0xcdb8
-  __TEXT.__cstring: 0xd0b5
-  __TEXT.__oslogstring: 0x27db
-  __TEXT.__gcc_except_tab: 0x2684
-  __TEXT.__dlopen_cstrs: 0x56
+6200.5.77.2.6
+  __TEXT.__text: 0x15ac5c
+  __TEXT.__auth_stubs: 0x24b0
+  __TEXT.__objc_methlist: 0x17fc
+  __TEXT.__const: 0xcdc8
+  __TEXT.__gcc_except_tab: 0x255c
+  __TEXT.__cstring: 0xc985
+  __TEXT.__oslogstring: 0x272b
   __TEXT.__ustring: 0x72
-  __TEXT.__swift5_typeref: 0x1a84
-  __TEXT.__constg_swiftt: 0x2134
-  __TEXT.__swift5_reflstr: 0x1ec0
-  __TEXT.__swift5_fieldmd: 0x38ec
+  __TEXT.__dlopen_cstrs: 0x56
+  __TEXT.__constg_swiftt: 0x2124
+  __TEXT.__swift5_typeref: 0x1a90
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_assocty: 0x4b0
-  __TEXT.__swift5_proto: 0xc8c
+  __TEXT.__swift5_reflstr: 0x1eb2
+  __TEXT.__swift5_fieldmd: 0x38f8
+  __TEXT.__swift5_assocty: 0x4e0
+  __TEXT.__swift5_proto: 0xc9c
   __TEXT.__swift5_types: 0x300
-  __TEXT.__swift5_capture: 0x4d4
+  __TEXT.__swift5_capture: 0x4e0
+  __TEXT.__swift_as_entry: 0x180
+  __TEXT.__swift_as_ret: 0x20c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift_as_entry: 0x188
-  __TEXT.__swift_as_ret: 0x214
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x4580
-  __TEXT.__eh_frame: 0x774c
-  __TEXT.__objc_classname: 0x415
-  __TEXT.__objc_methname: 0x7b8d
-  __TEXT.__objc_methtype: 0x583
-  __TEXT.__objc_stubs: 0x44c0
-  __DATA_CONST.__got: 0xb58
+  __TEXT.__unwind_info: 0x4550
+  __TEXT.__eh_frame: 0x766c
+  __TEXT.__objc_classname: 0x6e8
+  __TEXT.__objc_methname: 0x7ce3
+  __TEXT.__objc_methtype: 0x896
+  __TEXT.__objc_stubs: 0x5ca0
+  __DATA_CONST.__got: 0xb60
   __DATA_CONST.__const: 0x5e0
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1948
+  __DATA_CONST.__objc_selrefs: 0x1958
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x1280
-  __AUTH_CONST.__const: 0xf108
+  __AUTH_CONST.__auth_got: 0x1268
+  __AUTH_CONST.__const: 0xe848
   __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x3230
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_const: 0x3168
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xf58
-  __AUTH.__data: 0x1dc0
-  __DATA.__objc_ivar: 0x138
-  __DATA.__data: 0x2a00
-  __DATA.__bss: 0x180d0
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0xf68
+  __AUTH.__data: 0x1d10
+  __DATA.__objc_ivar: 0x140
+  __DATA.__data: 0x2a48
+  __DATA.__bss: 0x182d0
   __DATA.__common: 0x78
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary
-  - /System/Library/PrivateFrameworks/HealthContent.framework/HealthContent
+  - /System/Library/PrivateFrameworks/HealthOntologyKit.framework/HealthOntologyKit
   - /System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 499D8FAB-15B5-3682-B031-1D50FC47DA91
-  Functions: 5685
-  Symbols:   3510
-  CStrings:  2964
+  UUID: 63AFA4DC-9DD8-3407-A564-468A2E2D51B6
+  Functions: 5678
+  Symbols:   3736
+  CStrings:  2955
 
Symbols:
+ -[HDHRSignedClinicalDataHandler .cxx_destruct]
+ -[HDHRSignedClinicalDataHandler createSignedClinicalDataProcessor]
+ -[HDHRSignedClinicalDataHandler initWithHealthStore:]
+ -[HDHRSignedClinicalDataHandler init]
+ _OBJC_IVAR_$_HDHRSignedClinicalDataHandler._healthStore
+ _OBJC_IVAR_$_HDHealthRecordDocumentProcessor._healthStore
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __IVARS_HDHRSignedClinicalDataProcessor
+ __OBJC_$_INSTANCE_VARIABLES_HDHRSignedClinicalDataHandler
+ ___95-[HDHealthRecordConstructClinicalRecordsTask _applyReferenceRulesToClinicalItem:ruleset:error:]_block_invoke.364
+ ___block_literal_global.398
+ ___block_literal_global.598
+ ___block_literal_global.659
+ ___block_literal_global.664
+ ___block_literal_global.675
+ ___block_literal_global.680
+ ___block_literal_global.921
+ ___block_literal_global.927
+ ___block_literal_global.932
+ ___block_literal_global.937
+ ___block_literal_global.942
+ ___swift_project_boxed_opaque_existential_0Tm
+ _associated conformance 23HealthRecordsExtraction19IndexableRecordType33_E1BA825B78A75045722E492A667BDC37LLOSHAASQ
+ _associated conformance 23HealthRecordsExtraction19IndexableRecordType33_E1BA825B78A75045722E492A667BDC37LLOs12CaseIterableAA8AllCasessAEP_Sl
+ _block_copy_helper.17
+ _block_copy_helper.31
+ _block_copy_helper.34
+ _block_copy_helper.53
+ _block_copy_helper.56
+ _block_copy_helper.63
+ _block_copy_helper.69
+ _block_copy_helper.80
+ _block_copy_helper.84
+ _block_descriptor.19
+ _block_descriptor.33
+ _block_descriptor.36
+ _block_descriptor.55
+ _block_descriptor.58
+ _block_descriptor.65
+ _block_descriptor.71
+ _block_descriptor.82
+ _block_descriptor.86
+ _block_destroy_helper.18
+ _block_destroy_helper.32
+ _block_destroy_helper.35
+ _block_destroy_helper.54
+ _block_destroy_helper.57
+ _block_destroy_helper.64
+ _block_destroy_helper.70
+ _block_destroy_helper.81
+ _block_destroy_helper.85
+ _objc_msgSend$CVXSystem
+ _objc_msgSend$FHIRDocumentReferenceClinicalNoteCategorySystem
+ _objc_msgSend$FHIRDocumentReferenceClinicalNoteStatus
+ _objc_msgSend$JWKSData
+ _objc_msgSend$JWKSOutcome
+ _objc_msgSend$LOINCCodeSystem
+ _objc_msgSend$QRRepresentation
+ _objc_msgSend$SNOMEDCodeSystem
+ _objc_msgSend$UUID
+ _objc_msgSend$_creationDate
+ _objc_msgSend$_rowid
+ _objc_msgSend$anchorFromValue:
+ _objc_msgSend$asSignedClinicalDataItem
+ _objc_msgSend$attachmentIdentifiers
+ _objc_msgSend$attachmentObjectIdentifier
+ _objc_msgSend$attachmentSchemaIdentifier
+ _objc_msgSend$attributeSet
+ _objc_msgSend$birthDate
+ _objc_msgSend$cancel
+ _objc_msgSend$cborWithArray:
+ _objc_msgSend$cborWithData:
+ _objc_msgSend$cborWithUTF8String:
+ _objc_msgSend$charactersToBeSkipped
+ _objc_msgSend$clinicalNoteRecordTypeForIdentifier:
+ _objc_msgSend$codingVersion
+ _objc_msgSend$collectionWithCoding:
+ _objc_msgSend$conditionRecordTypeForIdentifier:
+ _objc_msgSend$contentStringFromDOCXData:error:
+ _objc_msgSend$contentStringFromHTMLData:error:
+ _objc_msgSend$contentType
+ _objc_msgSend$contextItems
+ _objc_msgSend$copyWithAlteredData:error:
+ _objc_msgSend$copyWithOriginalRecord:mainRecord:
+ _objc_msgSend$countryCode
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createSignedClinicalDataProcessor
+ _objc_msgSend$credentialTypes
+ _objc_msgSend$dataValue
+ _objc_msgSend$decimalValue
+ _objc_msgSend$defaultManager
+ _objc_msgSend$deleteAllSearchableItemsWithCompletionHandler:
+ _objc_msgSend$deleteSearchableItemsWithDomainIdentifiers:completionHandler:
+ _objc_msgSend$device
+ _objc_msgSend$diagnosticTestReportTypeForIdentifier:
+ _objc_msgSend$diagnosticTestResultTypeForIdentifier:
+ _objc_msgSend$displayName
+ _objc_msgSend$domainIdentifier
+ _objc_msgSend$doubleValue
+ _objc_msgSend$executeQuery:
+ _objc_msgSend$expirationDate
+ _objc_msgSend$extractResource:healthStore:completion:
+ _objc_msgSend$extractionVersion
+ _objc_msgSend$fallbackDisplayString
+ _objc_msgSend$fhirIdentifier
+ _objc_msgSend$file
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileHandle
+ _objc_msgSend$getAttachmentsForObject:completion:
+ _objc_msgSend$getTranscript
+ _objc_msgSend$hrs_safelyLoggableDescription
+ _objc_msgSend$indexSearchableItems:completionHandler:
+ _objc_msgSend$init
+ _objc_msgSend$initWithAttachmentIdentifiers:
+ _objc_msgSend$initWithCategory:domainName:healthStore:
+ _objc_msgSend$initWithCodingSystem:codingVersion:code:displayString:
+ _objc_msgSend$initWithCodings:
+ _objc_msgSend$initWithConceptSelection:resultsHandler:
+ _objc_msgSend$initWithContent:contentType:
+ _objc_msgSend$initWithData:options:
+ _objc_msgSend$initWithDecimal:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithFullName:dateOfBirthComponents:
+ _objc_msgSend$initWithHealthStore:
+ _objc_msgSend$initWithIdentifier:medicalRecordIdentifier:clinicalRecordIdentifier:accountIdentifier:FHIRVersion:type:status:errorStatus:title:webURL:sizeInBytes:contentType:locale:expectedHash:creationDate:retryCount:nextRetryDate:lastUpdatedDate:lastError:fileURL:inlineData:inlineDataChecksum:attachmentIdentifier:metadata:
+ _objc_msgSend$initWithIdentifier:name:OID:type:synonyms:hasDisplayStrings:
+ _objc_msgSend$initWithItemContentType:
+ _objc_msgSend$initWithItems:options:
+ _objc_msgSend$initWithLongLong:
+ _objc_msgSend$initWithName:protectionClass:path:
+ _objc_msgSend$initWithOriginalRecord:mainRecord:verifiableClinicalRecord:medicalRecords:clinicalRecords:
+ _objc_msgSend$initWithOutcome:
+ _objc_msgSend$initWithPath:queryString:context:
+ _objc_msgSend$initWithQueryDescriptors:anchor:limit:resultsHandler:
+ _objc_msgSend$initWithRawContent:sourceType:sourceURL:issuerIdentifier:credentialTypes:syncIdentifier:metadata:receivedDate:receivedDateTimeZone:signatureStatus:
+ _objc_msgSend$initWithRawData:sourceType:sourceURL:issuerIdentifier:signingKeyID:JWKSData:JWKSOutcome:metadata:
+ _objc_msgSend$initWithRawValue:comparatorCoding:unitCoding:
+ _objc_msgSend$initWithReceivedDate:countryCode:options:contextItems:
+ _objc_msgSend$initWithSampleType:predicate:
+ _objc_msgSend$initWithSignedClinicalDataRecordIdentifier:
+ _objc_msgSend$initWithTitle:medicalRecord:attachmentUUID:previewString:previewStringMatchRanges:
+ _objc_msgSend$initWithUniqueIdentifier:domainIdentifier:attributeSet:
+ _objc_msgSend$initWithUnit:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$isAtEnd
+ _objc_msgSend$isCancelled
+ _objc_msgSend$isClinicalNoteRecord
+ _objc_msgSend$issuedDate
+ _objc_msgSend$issuerIdentifier
+ _objc_msgSend$itemWithPrimaryConceptCodingCollection:relevantDate:medicalRecordSampleID:
+ _objc_msgSend$labResultRecordType
+ _objc_msgSend$locale
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedPreferredName
+ _objc_msgSend$longLongValue
+ _objc_msgSend$medicalDateFromComponents:originalTimeZoneString:form:error:
+ _objc_msgSend$medicalRecord
+ _objc_msgSend$medicalRecordCodings
+ _objc_msgSend$metadata
+ _objc_msgSend$modifiedDate
+ _objc_msgSend$note
+ _objc_msgSend$objCType
+ _objc_msgSend$options
+ _objc_msgSend$orderedSegmentsWithError:
+ _objc_msgSend$originIdentifier
+ _objc_msgSend$originIdentifierWithFHIRResourceType:identifier:
+ _objc_msgSend$originalRecord
+ _objc_msgSend$performRequests:error:
+ _objc_msgSend$predicateForObjectsWithUUIDs:
+ _objc_msgSend$preferredName
+ _objc_msgSend$primaryConcept
+ _objc_msgSend$rawContent
+ _objc_msgSend$rawData
+ _objc_msgSend$receivedDateTimeZone
+ _objc_msgSend$referenceCalendar
+ _objc_msgSend$relevantDate
+ _objc_msgSend$results
+ _objc_msgSend$selectionForNodesWithCoding:
+ _objc_msgSend$setAllowsFloats:
+ _objc_msgSend$setAlwaysShowsDecimalSeparator:
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setBundleIDs:
+ _objc_msgSend$setCharactersToBeSkipped:
+ _objc_msgSend$setCity:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setCountry:
+ _objc_msgSend$setCreationDate:
+ _objc_msgSend$setData:forKey:completion:
+ _objc_msgSend$setDecimalSeparator:
+ _objc_msgSend$setDisplayName:
+ _objc_msgSend$setDomainIdentifier:
+ _objc_msgSend$setFetchAttributes:
+ _objc_msgSend$setFoundItemsHandler:
+ _objc_msgSend$setISOCountryCode:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setMaximumFractionDigits:
+ _objc_msgSend$setMaximumIntegerDigits:
+ _objc_msgSend$setMinimumFractionDigits:
+ _objc_msgSend$setMinimumIntegerDigits:
+ _objc_msgSend$setPostalCode:
+ _objc_msgSend$setPrivateIndex:
+ _objc_msgSend$setProtectionClass:
+ _objc_msgSend$setProtectionClasses:
+ _objc_msgSend$setRecognitionLanguages:
+ _objc_msgSend$setRecognitionLevel:
+ _objc_msgSend$setRelatedUniqueIdentifier:
+ _objc_msgSend$setState:
+ _objc_msgSend$setStreet:
+ _objc_msgSend$setString:
+ _objc_msgSend$setStyle:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$setUsesLanguageCorrection:
+ _objc_msgSend$signatureStatus
+ _objc_msgSend$signedClinicalDataRecordIdentifier
+ _objc_msgSend$signedClinicalDataRecordTypeForIdentifier:
+ _objc_msgSend$signedClinicalDataRecordWithType:note:enteredInError:modifiedDate:originIdentifier:locale:extractionVersion:device:metadata:country:state:credentialTypes:issuerIdentifier:issuedDate:relevantDate:expirationDate:signatureStatus:subject:items:dataValue:sourceType:
+ _objc_msgSend$signingKeyID
+ _objc_msgSend$sortDate
+ _objc_msgSend$sourceType
+ _objc_msgSend$start
+ _objc_msgSend$stopQuery:
+ _objc_msgSend$street
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringForObjectValue:
+ _objc_msgSend$stringFromPersonNameComponents:
+ _objc_msgSend$stringFromPostalAddress:style:
+ _objc_msgSend$stringRepresentation
+ _objc_msgSend$subject
+ _objc_msgSend$subjectWithFullName:birthDate:gender:emailAddresses:phoneNumbers:
+ _objc_msgSend$subjectWithFullName:birthDate:gender:emailAddresses:phoneNumbers:identifiers:addresses:maritalStatus:race:ethnicity:birthSex:
+ _objc_msgSend$syncIdentifier
+ _objc_msgSend$synthesizeInMemoryConceptForCodingCollection:
+ _objc_msgSend$title
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$unknownRecordTypeForIdentifier:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$vaccinationRecordTypeForIdentifier:
+ _objc_msgSend$valueWithRange:
+ _objc_msgSend$verifiableClinicalRecordTypeForIdentifier:
+ _objc_msgSend$verifiableClinicalRecordWithType:startDate:endDate:device:metadata:recordTypes:issuedDate:relevantDate:expirationDate:issuerIdentifier:subject:itemNames:dataRepresentation:originIdentifier:sourceType:
+ _objc_msgSend$versionFromVersionString:error:
+ _objc_opt_new
+ _objc_retain_x12
+ _objc_retain_x9
+ _objectdestroy.16Tm
+ _swift_willThrowTypedImpl
+ _symbolic Say_____G 23HealthRecordsExtraction19IndexableRecordType33_E1BA825B78A75045722E492A667BDC37LLO
+ _symbolic _____ 23HealthRecordsExtraction19IndexableRecordType33_E1BA825B78A75045722E492A667BDC37LLO
- __DATA__TtC23HealthRecordsExtraction33HealthRecordSpotlightSearchResult
- __IVARS__TtC23HealthRecordsExtraction33HealthRecordSpotlightSearchResult
- __METACLASS_DATA__TtC23HealthRecordsExtraction33HealthRecordSpotlightSearchResult
- ___95-[HDHealthRecordConstructClinicalRecordsTask _applyReferenceRulesToClinicalItem:ruleset:error:]_block_invoke.325
- ___block_literal_global.359
- ___block_literal_global.559
- ___block_literal_global.620
- ___block_literal_global.625
- ___block_literal_global.636
- ___block_literal_global.641
- ___block_literal_global.882
- ___block_literal_global.888
- ___block_literal_global.893
- ___block_literal_global.898
- ___block_literal_global.903
- ___swift_destroy_boxed_opaque_existential_1Tm
- ___swift_destroy_boxed_opaque_existential_2Tm
- ___swift_mutable_project_boxed_opaque_existential_0
- ___swift_project_boxed_opaque_existential_2Tm
- _block_copy_helper.22
- _block_copy_helper.36
- _block_copy_helper.39
- _block_copy_helper.58
- _block_copy_helper.61
- _block_copy_helper.68
- _block_copy_helper.74
- _block_copy_helper.85
- _block_copy_helper.89
- _block_descriptor.24
- _block_descriptor.38
- _block_descriptor.41
- _block_descriptor.60
- _block_descriptor.63
- _block_descriptor.70
- _block_descriptor.76
- _block_descriptor.87
- _block_descriptor.91
- _block_destroy_helper.23
- _block_destroy_helper.37
- _block_destroy_helper.40
- _block_destroy_helper.59
- _block_destroy_helper.62
- _block_destroy_helper.69
- _block_destroy_helper.75
- _block_destroy_helper.86
- _block_destroy_helper.90
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$extractResource:completion:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objectdestroy.14Tm
- _symbolic SaySny_____GG SS5IndexV
- _symbolic _____ 23HealthRecordsExtraction0A27RecordSpotlightSearchResultC
CStrings:
+ "%s starting to extract Health Records"
+ "@\"HKHealthStore\""
+ "Failed to convert reference "
+ "HealthRecordsExtraction.SignedClinicalDataProcessor"
+ "VCJWT<SignedClinicalDataJWTHeader, SignedClinicalDataJWTPayload<SignedClinicalDataSubject>>"
+ "_healthStore"
+ "createSignedClinicalDataProcessor"
+ "extractResource:healthStore:completion:"
+ "setISOCountryCode:"
+ "v40@0:8@\"HDOriginalFHIRResourceObject\"16@\"HKHealthStore\"24@?<v@?@\"HDExtractionResultItem\"@\"NSError\">32"
- "ModelsDSTU2.ResourceProxy.asClinicalRecord: failed to convert to HKClinicalRecord, skipping. Error: %s"
- "ModelsR4.ResourceProxy.asClinicalRecord: failed to convert to HKClinicalRecord, skipping. Error: %s"
- "_TtC23HealthRecordsExtraction33HealthRecordSpotlightSearchResult"
- "contentHitRanges"
- "effectiveQueryTokens"
- "extractResource:completion:"
- "textContent"
- "titleHitRanges"
- "v32@0:8@\"HDOriginalFHIRResourceObject\"16@?<v@?@\"HDExtractionResultItem\"@\"NSError\">24"

```
