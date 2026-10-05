## HealthRecordsPlugin

> `/System/Library/PrivateFrameworks/HealthRecordsPlugin.framework/HealthRecordsPlugin`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0xc42f8
-  __TEXT.__objc_methlist: 0x79b4
-  __TEXT.__const: 0xe80
-  __TEXT.__cstring: 0x9aaf
-  __TEXT.__oslogstring: 0x10747
-  __TEXT.__gcc_except_tab: 0x198c
+7027.1.54.2.3
+  __TEXT.__text: 0xc4b98
+  __TEXT.__objc_methlist: 0x7994
+  __TEXT.__const: 0xeb0
+  __TEXT.__cstring: 0x9b1f
+  __TEXT.__oslogstring: 0x10617
+  __TEXT.__gcc_except_tab: 0x1978
   __TEXT.__ustring: 0x7e
-  __TEXT.__swift5_typeref: 0x6cf
+  __TEXT.__swift5_typeref: 0x6f9
   __TEXT.__swift5_capture: 0x4f0
-  __TEXT.__constg_swiftt: 0x47c
-  __TEXT.__swift5_reflstr: 0x223
-  __TEXT.__swift5_fieldmd: 0x304
+  __TEXT.__constg_swiftt: 0x4ac
+  __TEXT.__swift5_reflstr: 0x233
+  __TEXT.__swift5_fieldmd: 0x32c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_types: 0x48
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift_as_cont: 0xac
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x3810
+  __TEXT.__unwind_info: 0x3818
   __TEXT.__eh_frame: 0x1020
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2fc8
+  __DATA_CONST.__const: 0x2fa0
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x120
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5358
+  __DATA_CONST.__objc_selrefs: 0x5368
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x2e0
+  __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x150
-  __DATA_CONST.__got: 0x12a8
+  __DATA_CONST.__got: 0x12c0
   __AUTH_CONST.__const: 0x1838
   __AUTH_CONST.__cfstring: 0x68a0
-  __AUTH_CONST.__objc_const: 0xbb00
+  __AUTH_CONST.__objc_const: 0xba20
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xeb0
-  __AUTH.__objc_data: 0x1860
-  __AUTH.__data: 0x1a8
-  __DATA.__objc_ivar: 0x5e8
-  __DATA.__data: 0xf40
+  __AUTH_CONST.__auth_got: 0xec0
+  __AUTH.__objc_data: 0x1880
+  __AUTH.__data: 0x250
+  __DATA.__objc_ivar: 0x5e0
+  __DATA.__data: 0xf38
   __DATA_DIRTY.__objc_data: 0x1420
   __DATA_DIRTY.__data: 0x578
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3809
-  Symbols:   5620
+  Functions: 3817
+  Symbols:   5612
   CStrings:  1822
 
Symbols:
+ +[HDMedicalRecordEntity(HealthRecordsPlugin) processMedicalRecordsInExtractionResult:accountIdentifier:tally:profile:error:]
+ +[HDMedicalRecordEntity(HealthRecordsPlugin) processMedicalRecordsInExtractionResultItem:accountIdentifier:tally:database:profile:error:]
+ -[HDClinicalAccountEntity(HealthRecordsPlugin) _mergeCodableAccountFromSync:syncIdentifier:profile:transaction:error:]
+ -[HDClinicalAccountEntity(HealthRecordsPlugin) _updateAccountFromSyncWithCodable:syncIdentifier:profile:transaction:error:]
+ -[HDClinicalIngestionExtractionOperation medicalRecordsTally]
+ -[HDClinicalIngestionExtractionOperation setMedicalRecordsTally:]
+ -[HDClinicalIngestionTask accumulateMedicalRecordsTally:forAccountIdentifier:]
+ -[HDClinicalIngestionTask medicalRecordsTallyForAccountIdentifier:]
+ -[HDHealthRecordsProfileExtension notifyNewMedicalRecordsObserversForAccountWithIdentifier:tally:]
+ GCC_except_table19
+ GCC_except_table190
+ _OBJC_CLASS_$_HDClinicalIngestionNotifyNewMedicalRecordsOperation
+ _OBJC_CLASS_$_HDMutableNewMedicalRecordsTally
+ _OBJC_CLASS_$_HDNewMedicalRecordsCounts
+ _OBJC_CLASS_$_HDNewMedicalRecordsTally
+ _OBJC_IVAR_$_HDClinicalIngestionExtractionOperation._medicalRecordsTally
+ _OBJC_IVAR_$_HDClinicalIngestionTask._medicalRecordsTalliesForAccountIdentifier
+ _OBJC_METACLASS_$_HDClinicalIngestionNotifyNewMedicalRecordsOperation
+ __DATA_HDClinicalIngestionNotifyNewMedicalRecordsOperation
+ __INSTANCE_METHODS_HDClinicalIngestionNotifyNewMedicalRecordsOperation
+ __IVARS_HDClinicalIngestionNotifyNewMedicalRecordsOperation
+ __METACLASS_DATA_HDClinicalIngestionNotifyNewMedicalRecordsOperation
+ ___123-[HDClinicalAccountEntity(HealthRecordsPlugin) _updateAccountFromSyncWithCodable:syncIdentifier:profile:transaction:error:]_block_invoke
+ ___123-[HDClinicalAccountEntity(HealthRecordsPlugin) _updateAccountFromSyncWithCodable:syncIdentifier:profile:transaction:error:]_block_invoke_2
+ ___124+[HDMedicalRecordEntity(HealthRecordsPlugin) processMedicalRecordsInExtractionResult:accountIdentifier:tally:profile:error:]_block_invoke
+ ___137+[HDMedicalRecordEntity(HealthRecordsPlugin) processMedicalRecordsInExtractionResultItem:accountIdentifier:tally:database:profile:error:]_block_invoke
+ ___98-[HDHealthRecordsProfileExtension notifyNewMedicalRecordsObserversForAccountWithIdentifier:tally:]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56s64r_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8s56l8r64l8
+ _symbolic So24HDNewMedicalRecordsTallyC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 19HealthRecordsPlugin010NewMedicalB12AccountTally33_A607BC9B74B93B3162EE719C7C1CE808LLV
- +[HDMedicalRecordEntity(HealthRecordsPlugin) countOfMedicalRecordsForAccountRowID:profile:error:]
- +[HDMedicalRecordEntity(HealthRecordsPlugin) processMedicalRecordsInExtractionResult:accountIdentifier:profile:error:]
- +[HDMedicalRecordEntity(HealthRecordsPlugin) processMedicalRecordsInExtractionResultItem:accountIdentifier:database:profile:error:]
- -[HDClinicalAccountEntity(HealthRecordsPlugin) _updateAccountFromSyncWithCodable:profile:transaction:error:]
- -[HDHealthRecordsProfileExtension notifyNewMedicalRecordsObserversForAccountIdentifier:healthLinkIdentifier:]
- -[HDSignedClinicalDataManager _newMedicalRecordCountForAccountRowID:medicalRecordCountBeforeExtraction:]
- -[_HDConceptIndexAwaiter .cxx_destruct]
- -[_HDConceptIndexAwaiter _complete]
- -[_HDConceptIndexAwaiter conceptIndexManagerDidBecomeQuiescent:samplesProcessedCount:]
- -[_HDConceptIndexAwaiter conceptIndexManagerDidChangeExecutionState:]
- -[_HDConceptIndexAwaiter initWithProfile:completion:]
- -[_HDConceptIndexAwaiter wait]
- GCC_except_table189
- _OBJC_CLASS_$__HDConceptIndexAwaiter
- _OBJC_IVAR_$__HDConceptIndexAwaiter._completion
- _OBJC_IVAR_$__HDConceptIndexAwaiter._didComplete
- _OBJC_IVAR_$__HDConceptIndexAwaiter._lock
- _OBJC_IVAR_$__HDConceptIndexAwaiter._profile
- _OBJC_METACLASS_$__HDConceptIndexAwaiter
- __OBJC_$_INSTANCE_METHODS__HDConceptIndexAwaiter
- __OBJC_$_INSTANCE_VARIABLES__HDConceptIndexAwaiter
- __OBJC_$_PROP_LIST__HDConceptIndexAwaiter
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDConceptIndexManagerObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDConceptIndexManagerObserver
- __OBJC_$_PROTOCOL_REFS_HDConceptIndexManagerObserver
- __OBJC_CLASS_PROTOCOLS_$__HDConceptIndexAwaiter
- __OBJC_CLASS_RO_$__HDConceptIndexAwaiter
- __OBJC_LABEL_PROTOCOL_$_HDConceptIndexManagerObserver
- __OBJC_METACLASS_RO_$__HDConceptIndexAwaiter
- __OBJC_PROTOCOL_$_HDConceptIndexManagerObserver
- ___108-[HDClinicalAccountEntity(HealthRecordsPlugin) _updateAccountFromSyncWithCodable:profile:transaction:error:]_block_invoke
- ___108-[HDClinicalAccountEntity(HealthRecordsPlugin) _updateAccountFromSyncWithCodable:profile:transaction:error:]_block_invoke_2
- ___109-[HDHealthRecordsProfileExtension notifyNewMedicalRecordsObserversForAccountIdentifier:healthLinkIdentifier:]_block_invoke
- ___118+[HDMedicalRecordEntity(HealthRecordsPlugin) processMedicalRecordsInExtractionResult:accountIdentifier:profile:error:]_block_invoke
- ___131+[HDMedicalRecordEntity(HealthRecordsPlugin) processMedicalRecordsInExtractionResultItem:accountIdentifier:database:profile:error:]_block_invoke
- ___30-[_HDConceptIndexAwaiter wait]_block_invoke
- ___97+[HDMedicalRecordEntity(HealthRecordsPlugin) countOfMedicalRecordsForAccountRowID:profile:error:]_block_invoke
- ___block_descriptor_56_e8_32r_e35_B24?0"HDDatabaseTransaction"8^16lr32l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8
CStrings:
+ "%s no account for clinical health link %s, not inserting it"
+ "%{public}@ dropping journaled clinical account event for missing account: %{public}@"
+ "%{public}@ extraction produced %@ medical record samples that were saved, of which %@ were new and %@ replaced an existing record"
+ "%{public}@: Received newer codable clinical account %{public}@, merging it into existing account %{public}@"
+ "%{public}s notifying new medical records observers for account %{public}s with %ld new and %ld updated record(s) across %ld medical record type(s)"
+ "HealthRecordsPlugin.HDClinicalIngestionNotifyNewMedicalRecordsOperation"
+ "init(task:nextOperation:)"
- "%{public}@ extraction produced %@ medical record samples that were saved"
- "%{public}@: storeSignedClinicalData accountIdentifier nil for accountIdentifierForSMARTHealthLinkParsingResult"
- "%{public}@: storeSignedClinicalData failed to count medical records after extraction: %{public}@"
- "%{public}@: storeSignedClinicalData finished awaiting concept indexing, notifying new medical records observers for account %{public}@"
- "%{public}@: storeSignedClinicalData found %lu new medical record(s) after extracting SMARTHealthLinks, awaiting concept indexing before notifying new medical records observers for accountRowID %{public}@"
- "%{public}@: storeSignedClinicalData found no new medical records after extraction (before: %{public}@, after: %{public}@)"
- "%{public}@: storeSignedClinicalData missing accountRowID, cannot determine whether new medical records were created"
```
