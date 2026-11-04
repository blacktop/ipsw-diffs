## HealthRecordsPlugin

> `/System/Library/PrivateFrameworks/HealthRecordsPlugin.framework/HealthRecordsPlugin`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0xc4b98
-  __TEXT.__objc_methlist: 0x7994
-  __TEXT.__const: 0xeb0
-  __TEXT.__cstring: 0x9b1f
-  __TEXT.__oslogstring: 0x10617
+7027.2.13.0.0
+  __TEXT.__text: 0xcc820
+  __TEXT.__objc_methlist: 0x7a44
+  __TEXT.__const: 0xfc0
+  __TEXT.__cstring: 0x9c7f
+  __TEXT.__oslogstring: 0x10b07
   __TEXT.__gcc_except_tab: 0x1978
   __TEXT.__ustring: 0x7e
-  __TEXT.__swift5_typeref: 0x6f9
-  __TEXT.__swift5_capture: 0x4f0
-  __TEXT.__constg_swiftt: 0x4ac
-  __TEXT.__swift5_reflstr: 0x233
-  __TEXT.__swift5_fieldmd: 0x32c
+  __TEXT.__swift5_typeref: 0x781
+  __TEXT.__swift5_capture: 0x574
+  __TEXT.__constg_swiftt: 0x4d4
+  __TEXT.__swift5_reflstr: 0x2b3
+  __TEXT.__swift5_fieldmd: 0x36c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x48
-  __TEXT.__swift_as_entry: 0x70
-  __TEXT.__swift_as_ret: 0x54
-  __TEXT.__swift_as_cont: 0xac
+  __TEXT.__swift5_proto: 0x68
+  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift_as_entry: 0x7c
+  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__swift_as_cont: 0xc4
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x3818
-  __TEXT.__eh_frame: 0x1020
+  __TEXT.__unwind_info: 0x39a8
+  __TEXT.__eh_frame: 0x1428
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2fa0
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5368
+  __DATA_CONST.__objc_selrefs: 0x5440
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x150
-  __DATA_CONST.__got: 0x12c0
-  __AUTH_CONST.__const: 0x1838
-  __AUTH_CONST.__cfstring: 0x68a0
-  __AUTH_CONST.__objc_const: 0xba20
-  __AUTH_CONST.__objc_intobj: 0x4e0
+  __DATA_CONST.__got: 0x1428
+  __AUTH_CONST.__const: 0x1a58
+  __AUTH_CONST.__cfstring: 0x6960
+  __AUTH_CONST.__objc_const: 0xbad0
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xec0
-  __AUTH.__objc_data: 0x1880
-  __AUTH.__data: 0x250
-  __DATA.__objc_ivar: 0x5e0
-  __DATA.__data: 0xf38
+  __AUTH_CONST.__auth_got: 0xf90
+  __AUTH.__objc_data: 0x18f0
+  __AUTH.__data: 0x278
+  __DATA.__objc_ivar: 0x5e4
+  __DATA.__data: 0x1008
   __DATA_DIRTY.__objc_data: 0x1420
   __DATA_DIRTY.__data: 0x578
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3817
-  Symbols:   5612
-  CStrings:  1822
+  Functions: 3909
+  Symbols:   5667
+  CStrings:  1844
 
Symbols:
+ +[HKSignedClinicalDataIssuer(HealthRecordsPlugin) subtitleForIdentifier:]
+ -[HDClinicalIngestionTask _performSMARTHealthLinkFetchWithAccount:]
+ -[HDHealthRecordsProfileExtension _enqueueMedicalHistoryClinicalRecordDerivationWithManager:]
+ -[HDHealthRecordsProfileExtension scheduleMedicalHistoryClinicalRecordDerivationAfterCommitOfTransaction:]
+ _HKClinicalTypeIdentifierAllergyRecord
+ _HKClinicalTypeIdentifierConditionRecord
+ _HKClinicalTypeIdentifierImmunizationRecord
+ _HKClinicalTypeIdentifierLabResultRecord
+ _HKClinicalTypeIdentifierProcedureRecord
+ _HKMetadataKeyWasUserEntered
+ _OBJC_CLASS_$_HDMHRecordEntity
+ _OBJC_CLASS_$_HDMedicalHistoryDerivationManager
+ _OBJC_CLASS_$_HDMetadataManager
+ _OBJC_CLASS_$_HDNotificationManager
+ _OBJC_CLASS_$_HKClinicalHealthLinkBridge
+ _OBJC_CLASS_$_HKMedicalHistoryAllergyRecord
+ _OBJC_CLASS_$_HKMedicalHistoryAllergyRecordType
+ _OBJC_CLASS_$_HKMedicalHistoryFHIRSynthesisRequest
+ _OBJC_CLASS_$_HKMedicalHistoryFHIRSynthesisResult
+ _OBJC_CLASS_$_HKMedicalHistoryHealthConcernRecord
+ _OBJC_CLASS_$_HKMedicalHistoryHealthConcernRecordType
+ _OBJC_CLASS_$_HKMedicalHistoryImmunizationRecord
+ _OBJC_CLASS_$_HKMedicalHistoryImmunizationRecordType
+ _OBJC_CLASS_$_HKMedicalHistoryProcedureRecord
+ _OBJC_CLASS_$_HKMedicalHistoryProcedureRecordType
+ _OBJC_CLASS_$_HKMedicalHistoryQuantitativeLabResultRecord
+ _OBJC_CLASS_$_HKMedicalHistoryQuantitativeLabResultRecordType
+ _OBJC_CLASS_$_HKMedicalHistoryRecord
+ _OBJC_CLASS_$_HKMedicalHistoryRecordType
+ _OBJC_CLASS_$_HKObject
+ _OBJC_IVAR_$_HDHealthRecordsProfileExtension._medicalHistoryDerivationScheduled
+ _OBJC_METACLASS_$_HDMedicalHistoryDerivationManager
+ __DATA_HDMedicalHistoryDerivationManager
+ __HKPrivateMetadataKeyOriginalMHRecordUUID
+ __INSTANCE_METHODS_HDMedicalHistoryDerivationManager
+ __IVARS_HDMedicalHistoryDerivationManager
+ __METACLASS_DATA_HDMedicalHistoryDerivationManager
+ __PROPERTIES_HDMedicalHistoryDerivationManager
+ ___106-[HDHealthRecordsProfileExtension scheduleMedicalHistoryClinicalRecordDerivationAfterCommitOfTransaction:]_block_invoke
+ ___93-[HDHealthRecordsProfileExtension _enqueueMedicalHistoryClinicalRecordDerivationWithManager:]_block_invoke
+ ___93-[HDHealthRecordsProfileExtension _enqueueMedicalHistoryClinicalRecordDerivationWithManager:]_block_invoke_2
+ ___swift_closure_destructor.34Tm
+ ___swift_closure_destructor.4Tm
+ __swiftEmptySetSingleton
+ _associated conformance So33HDMedicalHistoryDerivationManagerC19HealthRecordsPluginE07MedicalbC5ErrorOSHACSQ
+ _kHKNotificationsDomainKey
+ _kHKNotificationsURLKey
+ _objc_retain_x10
+ _swift_bridgeObjectRelease_n
+ _swift_getErrorValue
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _symbolic SaySo22HKMedicalHistoryRecordCG
+ _symbolic Sb
+ _symbolic So33HDMedicalHistoryDerivationManagerC
+ _symbolic So8HKObjectC_____SAySo7NSErrorCSgGSgSbIggyyd_ s5Int64V
+ _symbolic _____ So33HDMedicalHistoryDerivationManagerC19HealthRecordsPluginE07MedicalbC5ErrorO
- GCC_except_table37
CStrings:
+ "%@ derived %ld of %ld clinical record(s)"
+ "%@ enumerated an unexpected sample type while looking for self-entered lab results"
+ "%@ failed to derive a clinical record: %s. Continue with the remaining records."
+ "%@ found no self-entered lab results to derive from"
+ "%{public}@ Account %{public}@: failed to look up SMART Health Links: %{public}@"
+ "%{public}@ Account %{public}@: failed to refresh SMART Health Link: %{public}@"
+ "%{public}@ Account %{public}@: fetch disabled, not refreshing SMART Health Links"
+ "%{public}@ Account %{public}@: not gateway backed and has no refreshable SMART Health Links, not attempting to ingest"
+ "%{public}@ Account %{public}@: not yet fetchable, not refreshing SMART Health Links"
+ "%{public}@ Account %{public}@: refreshing %lu SMART Health Link(s)"
+ "%{public}@: Completed derivation of clinical records for medical history records"
+ "%{public}@: Failed to derive clinical records for medical history records: %{private}@"
+ "%{public}@: No maintenance work coordinator, cannot derive clinical records for medical history records"
+ "%{public}@: No medical history derivation manager, not deriving clinical records for medical history records"
+ "%{public}@: Scheduling derivation of clinical records for medical history records"
+ "HealthRecordsPlugin.HDMedicalHistoryDerivationManager"
+ "SIGNED_CLINICAL_DATA_ISSUER_SUBTITLE_VIA_APPLE_HEALTH"
+ "SMART Health Link refresh failed without an error"
+ "Stopping scheduled refresh of clinical health link %s: %{public}s"
+ "api-experience.questdiagnostics.com"
+ "com.apple.private.health.healthrecords.new-records"
+ "com.apple.private.health.healthrecords.pinned-labs"
+ "derive clinical records for medical history records"
- "%{public}@ Account %{public}@: not gateway backed, not attempting to ingest"
```
