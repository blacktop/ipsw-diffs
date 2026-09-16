## HealthRecordsPlugin

> `/System/Library/PrivateFrameworks/HealthRecordsPlugin.framework/HealthRecordsPlugin`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0xb27ec
-  __TEXT.__objc_methlist: 0x780c
-  __TEXT.__const: 0xa30
-  __TEXT.__cstring: 0x978f
-  __TEXT.__oslogstring: 0xfdb7
-  __TEXT.__gcc_except_tab: 0x1968
+7027.1.36.2.7
+  __TEXT.__text: 0xc42f8
+  __TEXT.__objc_methlist: 0x79b4
+  __TEXT.__const: 0xe80
+  __TEXT.__cstring: 0x9aaf
+  __TEXT.__oslogstring: 0x10747
+  __TEXT.__gcc_except_tab: 0x198c
   __TEXT.__ustring: 0x7e
-  __TEXT.__swift5_typeref: 0x463
-  __TEXT.__swift5_capture: 0x328
-  __TEXT.__constg_swiftt: 0x370
-  __TEXT.__swift5_reflstr: 0x183
-  __TEXT.__swift5_fieldmd: 0x248
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_typeref: 0x6cf
+  __TEXT.__swift5_capture: 0x4f0
+  __TEXT.__constg_swiftt: 0x47c
+  __TEXT.__swift5_reflstr: 0x223
+  __TEXT.__swift5_fieldmd: 0x304
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_proto: 0x5c
+  __TEXT.__swift5_types: 0x44
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift_as_cont: 0xac
-  __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x34a8
-  __TEXT.__eh_frame: 0xba0
+  __TEXT.__unwind_info: 0x3810
+  __TEXT.__eh_frame: 0x1020
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2f48
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__const: 0x2fc8
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x120
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5228
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_selrefs: 0x5358
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0x150
-  __DATA_CONST.__got: 0x11a8
-  __AUTH_CONST.__const: 0x1180
-  __AUTH_CONST.__cfstring: 0x6740
-  __AUTH_CONST.__objc_const: 0xb820
+  __DATA_CONST.__got: 0x12a8
+  __AUTH_CONST.__const: 0x1838
+  __AUTH_CONST.__cfstring: 0x68a0
+  __AUTH_CONST.__objc_const: 0xbb00
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xae0
-  __AUTH.__objc_data: 0x1690
-  __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0xdb0
-  __DATA_DIRTY.__objc_data: 0x13f8
-  __DATA_DIRTY.__data: 0x538
+  __AUTH_CONST.__auth_got: 0xeb0
+  __AUTH.__objc_data: 0x1860
+  __AUTH.__data: 0x1a8
+  __DATA.__objc_ivar: 0x5e8
+  __DATA.__data: 0xf40
+  __DATA_DIRTY.__objc_data: 0x1420
+  __DATA_DIRTY.__data: 0x578
   __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3549
-  Symbols:   7806
-  CStrings:  1779
+  Functions: 3809
+  Symbols:   7956
+  CStrings:  1822
 
Symbols:
+ +[HDCPSUpdateGatewaysOperation updateGatewaysOperationsForAccounts:manager:profile:]
+ +[HDClinicalHealthLinkSyncEntityObjcBridge syncEntityDependenciesForSyncProtocolVersion:]
+ +[HDMedicalRecordEntity(HealthRecordsPlugin) countOfMedicalRecordsForAccountRowID:profile:error:]
+ -[HDCPSOperation runIfNeededAndWait]
+ -[HDClinicalAccountManager accountEntityForSMARTHealthLinkHost:error:]
+ -[HDClinicalIngestionSignedClinicalDataOperation _fetchCurrentAccessCredentialsWithError:]
+ -[HDClinicalIngestionSignedClinicalDataOperation _refreshAccessCredentialsWithCurrentCredentials:error:]
+ -[HDClinicalProviderServiceStoreServer remote_fetchRemoteGatewaysWithBatchID:completion:]
+ -[HDHealthRecordsDaemonExtension medicalHistoryFeatureEvaluator]
+ -[HDHealthRecordsDaemonExtension setMedicalHistoryFeatureEvaluator:]
+ -[HDHealthRecordsProfileExtension addNewMedicalRecordsObserver:]
+ -[HDHealthRecordsProfileExtension notifyNewMedicalRecordsObserversForAccountIdentifier:healthLinkIdentifier:]
+ -[HDHealthRecordsProfileExtension removeNewMedicalRecordsObserver:]
+ -[HDOntologyMedicalHistoryFeatureEvaluator canRequireShardWithError:]
+ -[HDOntologyMedicalHistoryFeatureEvaluator featureIdentifier]
+ -[HDOntologyMedicalHistoryFeatureEvaluator registerRequiredObserversForProfile:queue:]
+ -[HDOntologyMedicalHistoryFeatureEvaluator requiresFeatureShardForProfile:]
+ -[HDSignedClinicalDataManager _newMedicalRecordCountForAccountRowID:medicalRecordCountBeforeExtraction:]
+ -[_HDConceptIndexAwaiter .cxx_destruct]
+ -[_HDConceptIndexAwaiter _complete]
+ -[_HDConceptIndexAwaiter conceptIndexManagerDidBecomeQuiescent:samplesProcessedCount:]
+ -[_HDConceptIndexAwaiter conceptIndexManagerDidChangeExecutionState:]
+ -[_HDConceptIndexAwaiter initWithProfile:completion:]
+ -[_HDConceptIndexAwaiter wait]
+ GCC_except_table101
+ _HKOntologyShardIdentifierMedicalHistory
+ _OBJC_CLASS_$_HDClinicalHealthLinkSyncEntity
+ _OBJC_CLASS_$_HDClinicalHealthLinkSyncEntityObjcBridge
+ _OBJC_CLASS_$_HDCodableClinicalHealthLink
+ _OBJC_CLASS_$_HDInsertClinicalHealthLinkOperation
+ _OBJC_CLASS_$_HDOntologyMedicalHistoryFeatureEvaluator
+ _OBJC_CLASS_$_HDSMARTHealthLinkManager
+ _OBJC_CLASS_$_HKSMARTHealthLinkParsingResult
+ _OBJC_CLASS_$__HDConceptIndexAwaiter
+ _OBJC_IVAR_$_HDHealthRecordsDaemonExtension._medicalHistoryFeatureEvaluator
+ _OBJC_IVAR_$_HDHealthRecordsProfileExtension._newMedicalRecordsObservers
+ _OBJC_IVAR_$__HDConceptIndexAwaiter._completion
+ _OBJC_IVAR_$__HDConceptIndexAwaiter._didComplete
+ _OBJC_IVAR_$__HDConceptIndexAwaiter._lock
+ _OBJC_IVAR_$__HDConceptIndexAwaiter._profile
+ _OBJC_METACLASS_$_HDClinicalHealthLinkSyncEntity
+ _OBJC_METACLASS_$_HDClinicalHealthLinkSyncEntityObjcBridge
+ _OBJC_METACLASS_$_HDInsertClinicalHealthLinkOperation
+ _OBJC_METACLASS_$_HDOntologyMedicalHistoryFeatureEvaluator
+ _OBJC_METACLASS_$_HDSMARTHealthLinkManager
+ _OBJC_METACLASS_$__HDConceptIndexAwaiter
+ __CLASS_METHODS_HDClinicalHealthLinkSyncEntity
+ __CLASS_METHODS_HDHealthRecordsDataEntityHelper
+ __CLASS_METHODS_HDInsertClinicalHealthLinkOperation
+ __CLASS_PROPERTIES_HDClinicalHealthLinkSyncEntity
+ __CLASS_PROPERTIES_HDInsertClinicalHealthLinkOperation
+ __DATA_HDClinicalHealthLinkSyncEntity
+ __DATA_HDInsertClinicalHealthLinkOperation
+ __DATA_HDSMARTHealthLinkManager
+ __INSTANCE_METHODS_HDClinicalHealthLinkSyncEntity
+ __INSTANCE_METHODS_HDInsertClinicalHealthLinkOperation
+ __INSTANCE_METHODS_HDSMARTHealthLinkManager
+ __IVARS_HDInsertClinicalHealthLinkOperation
+ __IVARS_HDSMARTHealthLinkManager
+ __METACLASS_DATA_HDClinicalHealthLinkSyncEntity
+ __METACLASS_DATA_HDInsertClinicalHealthLinkOperation
+ __METACLASS_DATA_HDSMARTHealthLinkManager
+ __OBJC_$_CLASS_METHODS_HDCPSUpdateGatewaysOperation
+ __OBJC_$_CLASS_METHODS_HDClinicalHealthLinkSyncEntityObjcBridge
+ __OBJC_$_CLASS_PROP_LIST_HDOntologyMedicalHistoryFeatureEvaluator
+ __OBJC_$_INSTANCE_METHODS_HDOntologyMedicalHistoryFeatureEvaluator
+ __OBJC_$_INSTANCE_METHODS__HDConceptIndexAwaiter
+ __OBJC_$_INSTANCE_VARIABLES__HDConceptIndexAwaiter
+ __OBJC_$_PROP_LIST_HDOntologyMedicalHistoryFeatureEvaluator
+ __OBJC_$_PROP_LIST__HDConceptIndexAwaiter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDConceptIndexManagerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSyncCodable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDConceptIndexManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDSyncCodable
+ __OBJC_$_PROTOCOL_REFS_HDConceptIndexManagerObserver
+ __OBJC_$_PROTOCOL_REFS_HDSyncCodable
+ __OBJC_CLASS_PROTOCOLS_$_HDOntologyMedicalHistoryFeatureEvaluator
+ __OBJC_CLASS_PROTOCOLS_$__HDConceptIndexAwaiter
+ __OBJC_CLASS_RO_$_HDClinicalHealthLinkSyncEntityObjcBridge
+ __OBJC_CLASS_RO_$_HDOntologyMedicalHistoryFeatureEvaluator
+ __OBJC_CLASS_RO_$__HDConceptIndexAwaiter
+ __OBJC_LABEL_PROTOCOL_$_HDConceptIndexManagerObserver
+ __OBJC_LABEL_PROTOCOL_$_HDSyncCodable
+ __OBJC_METACLASS_RO_$_HDClinicalHealthLinkSyncEntityObjcBridge
+ __OBJC_METACLASS_RO_$_HDOntologyMedicalHistoryFeatureEvaluator
+ __OBJC_METACLASS_RO_$__HDConceptIndexAwaiter
+ __OBJC_PROTOCOL_$_HDConceptIndexManagerObserver
+ __OBJC_PROTOCOL_$_HDSyncCodable
+ __PROPERTIES_HDSMARTHealthLinkManager
+ __PROTOCOLS_HDClinicalHealthLinkSyncEntity
+ ___104-[HDClinicalIngestionSignedClinicalDataOperation _refreshAccessCredentialsWithCurrentCredentials:error:]_block_invoke
+ ___104-[HDClinicalIngestionSignedClinicalDataOperation _refreshAccessCredentialsWithCurrentCredentials:error:]_block_invoke_2
+ ___109-[HDHealthRecordsProfileExtension notifyNewMedicalRecordsObserversForAccountIdentifier:healthLinkIdentifier:]_block_invoke
+ ___30-[_HDConceptIndexAwaiter wait]_block_invoke
+ ___97+[HDMedicalRecordEntity(HealthRecordsPlugin) countOfMedicalRecordsForAccountRowID:profile:error:]_block_invoke
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_48_e8_32s40bs_e58_v24?0"HKSignedClinicalDataParsingResultMux"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32r_e35_B24?0"HDDatabaseTransaction"8^16lr32l8
+ ___block_descriptor_56_e8_32s40s48s_e52_v16?0"<HDHealthRecordsNewMedicalRecordsObserver>"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_HealthRecordsPlugin
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_HealthRecordsPlugin
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_HealthRecordsPlugin
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_HealthRecordsPlugin
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_HealthRecordsPlugin
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_HealthRecordsPlugin
+ _associated conformance 12HealthDaemon010HDClinicalA10LinkEntityC0A13RecordsPluginE20InsertOrUpdateResultV7OutcomeOSHADSQ
+ _associated conformance SC11HKErrorCodeLeV10Foundation13CustomNSErrorSCs5Error
+ _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_AC06_ErrorB8Protocol
+ _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_SY
+ _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomF0
+ _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC26_ObjectiveCBridgeableError
+ _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC11HKErrorCodeLeV10Foundation26_ObjectiveCBridgeableErrorSCs0F0
+ _associated conformance SC11HKErrorCodeLeVSHSCSQ
+ _associated conformance So11HKErrorCodeV10Foundation06_ErrorB8ProtocolSC01_D4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So11HKErrorCodeV10Foundation06_ErrorB8ProtocolSCSQ
+ _associated conformance So24HDSMARTHealthLinkManagerC19HealthRecordsPluginE011SMARTHealthbC5ErrorOSHACSQ
+ _objc_msgSend$_complete
+ _objc_msgSend$_fetchCurrentAccessCredentialsWithError:
+ _objc_msgSend$_newMedicalRecordCountForAccountRowID:medicalRecordCountBeforeExtraction:
+ _objc_msgSend$_refreshAccessCredentialsWithCurrentCredentials:error:
+ _objc_msgSend$accountEntityForSMARTHealthLinkHost:error:
+ _objc_msgSend$accountIdentifierForSMARTHealthLinkParsingResult:
+ _objc_msgSend$accountRowIDForSMARTHealthLinkParsingResult:error:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$clinicalHealthLink
+ _objc_msgSend$clinicalHealthLinkEntityForLinkWithIdentifier:database:error:
+ _objc_msgSend$clinicalHealthLinkSyncIdentifierForHealthLinkWithPersistentID:database:error:
+ _objc_msgSend$conceptIndexManager
+ _objc_msgSend$countOfMedicalRecordsForAccountRowID:profile:error:
+ _objc_msgSend$dateAdded
+ _objc_msgSend$dateAddedTimezone
+ _objc_msgSend$hasAccountSyncIdentifier
+ _objc_msgSend$hasDateAdded
+ _objc_msgSend$hasLinkKey
+ _objc_msgSend$hasLinkURL
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$healthLinkIdentifierForSMARTHealthLinkParsingResult:
+ _objc_msgSend$initWithHost:clinicalHealthLink:label:FHIRResources:
+ _objc_msgSend$initWithLongLong:
+ _objc_msgSend$initWithProfile:completion:
+ _objc_msgSend$isEqualToIgnoringCase:
+ _objc_msgSend$isExecuting
+ _objc_msgSend$label
+ _objc_msgSend$linkFlags
+ _objc_msgSend$linkKey
+ _objc_msgSend$linkLabel
+ _objc_msgSend$linkPasscode
+ _objc_msgSend$linkURL
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$manifestData
+ _objc_msgSend$manifestResolutionBlockedUntil
+ _objc_msgSend$manifestResolved
+ _objc_msgSend$medicalHistoryFeatureEvaluator
+ _objc_msgSend$mulberry
+ _objc_msgSend$newTokenRefresh
+ _objc_msgSend$notifyNewMedicalRecordsObserversForAccountIdentifier:healthLinkIdentifier:
+ _objc_msgSend$predicateWithProperty:comparisonType:subqueryDescriptor:subqueryProperties:
+ _objc_msgSend$profileExtension:didCreateNewMedicalRecordsForAccountIdentifier:healthLinkIdentifier:
+ _objc_msgSend$readDataToEndOfFileAndReturnError:
+ _objc_msgSend$runIfNeededAndWait
+ _objc_msgSend$setDateAdded:
+ _objc_msgSend$setDateAddedTimezone:
+ _objc_msgSend$setLinkFlags:
+ _objc_msgSend$setLinkKey:
+ _objc_msgSend$setLinkLabel:
+ _objc_msgSend$setLinkPasscode:
+ _objc_msgSend$setLinkURL:
+ _objc_msgSend$setManifestData:
+ _objc_msgSend$setManifestResolutionBlockedUntil:
+ _objc_msgSend$setManifestResolved:
+ _objc_msgSend$setMedicalHistoryFeatureEvaluator:
+ _objc_msgSend$smartHealthLink
+ _objc_msgSend$storeSMARTHealthLink:accountManager:error:
+ _objc_msgSend$updateGatewaysOperationsForAccounts:manager:profile:
+ _objc_msgSend$wait
+ _swift_allocError
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_getExistentialMetatypeMetadata
+ _swift_initStackObject
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_x1
+ _swift_release_x24
+ _swift_release_x27
+ _swift_release_x28
+ _swift_setDeallocating
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic $s10Foundation18_ErrorCodeProtocolP
+ _symbolic $s10Foundation21_BridgedStoredNSErrorP
+ _symbolic $sSY
+ _symbolic SaySSG_____Iggy_ s13OpaquePointerV
+ _symbolic SaySo27HDCodableClinicalHealthLinkCG
+ _symbolic Si
+ _symbolic So16HDSQLiteDatabaseC
+ _symbolic So21HDDatabaseTransactionC
+ _symbolic So22HDConcreteSyncIdentityC
+ _symbolic So22HDJournalableOperationC
+ _symbolic So24HDSMARTHealthLinkManagerC
+ _symbolic So27HDCodableClinicalHealthLinkC
+ _symbolic So7NSErrorC
+ _symbolic _____ 12HealthDaemon010HDClinicalA10LinkEntityC
+ _symbolic _____ 12HealthDaemon010HDClinicalA10LinkEntityC0A13RecordsPluginE20InsertOrUpdateResultV
+ _symbolic _____ 12HealthDaemon010HDClinicalA10LinkEntityC0A13RecordsPluginE20InsertOrUpdateResultV7OutcomeO
+ _symbolic _____ 19HealthRecordsPlugin016HDInsertClinicalA13LinkOperationC
+ _symbolic _____ 20HealthRecordServices08ClinicalA4LinkV
+ _symbolic _____ 20HealthRecordServices08ClinicalA4LinkV0E0V
+ _symbolic _____ 20HealthRecordServices08ClinicalA4LinkV8IdentityV
+ _symbolic _____ SC11HKErrorCodeLeV
+ _symbolic _____ So11HKErrorCodeV
+ _symbolic _____ So24HDSMARTHealthLinkManagerC19HealthRecordsPluginE011SMARTHealthbC5ErrorO
+ _symbolic _____Igy_ s13OpaquePointerV
+ _symbolic _____SAySo7NSErrorCSgGSgSbIgyyd_ s13OpaquePointerV
+ _symbolic _____Sg 20HealthRecordServices08ClinicalA4LinkV
+ _symbolic _____Sg 20HealthRecordServices08ClinicalA4LinkV8ManifestV
+ _symbolic _____XMT 12HealthDaemon010HDClinicalA10LinkEntityC
+ _symbolic ypSaySSG__________SiSpy_____GSAySo7NSErrorCSgGSgSbIgngyyyyyd_ s13OpaquePointerV s5Int64V 10ObjectiveC8ObjCBoolV
+ _type_layout_string SC11HKErrorCodeLeV
- -[HDClinicalIngestionNotifyHealthRecordsDaemonOperation main]
- -[HDClinicalProviderServiceManager addOperationUnlessAlreadyEnqueued:]
- -[HDClinicalProviderServiceManager createUpdateGatewaysOperationsForAccounts:]
- -[HDClinicalProviderServiceManager operationQueue]
- -[HDClinicalSharingManager .cxx_destruct]
- -[HDClinicalSharingManager _observedDataTypes]
- -[HDClinicalSharingManager _registerDataObservation]
- -[HDClinicalSharingManager _unregisterDataObservation]
- -[HDClinicalSharingManager database:protectedDataDidBecomeAvailable:]
- -[HDClinicalSharingManager dealloc]
- -[HDClinicalSharingManager didAddSamplesOfTypes:anchor:]
- -[HDClinicalSharingManager didUpdateKeyValueDomain:]
- -[HDClinicalSharingManager initWithProfileExtension:]
- -[HDClinicalSharingManager profileDidBecomeReady:]
- -[HDClinicalSharingManager samplesAdded:anchor:]
- -[HDClinicalSharingManager scheduleSharing]
- -[HDHealthRecordsProfileExtension clinicalSharingManager]
- -[HDHealthRecordsProfileExtension createClinicalSharingClient]
- -[HDHealthRecordsProfileExtension createClinicalSharingManager]
- GCC_except_table100
- _HKCategoryTypeIdentifierHighHeartRateEvent
- _HKCategoryTypeIdentifierIrregularHeartRhythmEvent
- _HKCategoryTypeIdentifierLowHeartRateEvent
- _HKQuantityTypeIdentifierBloodPressureDiastolic
- _HKQuantityTypeIdentifierBloodPressureSystolic
- _HKQuantityTypeIdentifierBodyMass
- _HKQuantityTypeIdentifierNumberOfTimesFallen
- _OBJC_CLASS_$_HDClinicalIngestionNotifyHealthRecordsDaemonOperation
- _OBJC_CLASS_$_HDClinicalSharingManager
- _OBJC_CLASS_$_HKClinicalSharingClient
- _OBJC_IVAR_$_HDClinicalProviderServiceManager._addOperationLock
- _OBJC_IVAR_$_HDClinicalProviderServiceManager._operationQueue
- _OBJC_IVAR_$_HDClinicalSharingManager._keyValueDomain
- _OBJC_IVAR_$_HDClinicalSharingManager._profileExtension
- _OBJC_IVAR_$_HDHealthRecordsProfileExtension._clinicalSharingManager
- _OBJC_METACLASS_$_HDClinicalIngestionNotifyHealthRecordsDaemonOperation
- _OBJC_METACLASS_$_HDClinicalSharingManager
- __OBJC_$_INSTANCE_METHODS_HDClinicalIngestionNotifyHealthRecordsDaemonOperation
- __OBJC_$_INSTANCE_METHODS_HDClinicalSharingManager
- __OBJC_$_INSTANCE_VARIABLES_HDClinicalSharingManager
- __OBJC_$_PROP_LIST_HDClinicalSharingManager
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDDataObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDKeyValueDomainObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDDataObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDDataObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDKeyValueDomainObserver
- __OBJC_$_PROTOCOL_REFS_HDDataObserver
- __OBJC_CLASS_PROTOCOLS_$_HDClinicalSharingManager
- __OBJC_CLASS_RO_$_HDClinicalIngestionNotifyHealthRecordsDaemonOperation
- __OBJC_CLASS_RO_$_HDClinicalSharingManager
- __OBJC_LABEL_PROTOCOL_$_HDDataObserver
- __OBJC_LABEL_PROTOCOL_$_HDKeyValueDomainObserver
- __OBJC_METACLASS_RO_$_HDClinicalIngestionNotifyHealthRecordsDaemonOperation
- __OBJC_METACLASS_RO_$_HDClinicalSharingManager
- __OBJC_PROTOCOL_$_HDDataObserver
- __OBJC_PROTOCOL_$_HDKeyValueDomainObserver
- ___43-[HDClinicalSharingManager scheduleSharing]_block_invoke
- ___82-[HDClinicalDailyAnalyticsManager reportDailyAnalyticsWithCoordinator:completion:]_block_invoke
- ___84-[HDClinicalIngestionSignedClinicalDataOperation _askForAccessCredentialsWithError:]_block_invoke
- ___84-[HDClinicalIngestionSignedClinicalDataOperation _askForAccessCredentialsWithError:]_block_invoke_2
- ___block_descriptor_104_e8_32s40s48s56s64s72s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_40_e8_32bs_e58_v24?0"HKSignedClinicalDataParsingResultMux"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
- _objc_msgSend$_observedDataTypes
- _objc_msgSend$_registerDataObservation
- _objc_msgSend$_unregisterDataObservation
- _objc_msgSend$addObserver:forDataType:
- _objc_msgSend$addOperationUnlessAlreadyEnqueued:
- _objc_msgSend$categoryTypeForIdentifier:
- _objc_msgSend$clinicalSharingManager
- _objc_msgSend$createClinicalSharingClient
- _objc_msgSend$createClinicalSharingManager
- _objc_msgSend$createUpdateGatewaysOperationsForAccounts:
- _objc_msgSend$electrocardiogramType
- _objc_msgSend$operationQueue
- _objc_msgSend$operations
- _objc_msgSend$quantityTypeForIdentifier:
- _objc_msgSend$readDataToEndOfFile
- _objc_msgSend$removeObserver:forDataType:
- _objc_msgSend$scheduleSharing
- _objc_msgSend$scheduleSharingHealthDataWithReason:completion:
- _objc_msgSend$submitDailyAnalyticsWithCompletion:
CStrings:
+ "$."
+ "%s %@ generated %ld sync objects"
+ "%s could not get sync identifier for account. not inserting clinical health link: %s"
+ "%s validation failed, not inserting clinical health link: %s: %@"
+ "%{public}@ attempting to register a new medical records observer on an unsupported profile: %{public}@"
+ "%{public}@ failed to convert health link sync identifier data %{public}@ for incoming resource %{public}@/%{public}@ to a UUID, ignoring but won't be able to associate FHIR resource to the link"
+ "%{public}@ failed to deserialize JSON: %{public}@"
+ "%{public}@ failed to find health link with link ID %{public}@, won't be able to associate FHIR resource with link. Error: %{public}@"
+ "%{public}@ failed to pull dictionary from JSON: %{public}@"
+ "%{public}@ failed to read data from file: %{public}@"
+ "%{public}@ failed to retrieve health link for incoming resource %{public}@/%{public}@, continuing but unable to associate to link. Error: %{public}@"
+ "%{public}@ failed to retrieve sync ID for health link at row %{public}@. Skipping resource at anchor %lld: %{public}@"
+ "%{public}@ fetching current access credentials"
+ "%{public}@ refreshing access credentials"
+ "%{public}@: Failed to get account row ID from SHL result: %{public}@"
+ "%{public}@: Found %{public}ld attachments for %{public}ld medical records"
+ "%{public}@: storeSignedClinicalData accountIdentifier nil for accountIdentifierForSMARTHealthLinkParsingResult"
+ "%{public}@: storeSignedClinicalData failed to count medical records after extraction: %{public}@"
+ "%{public}@: storeSignedClinicalData finished awaiting concept indexing, notifying new medical records observers for account %{public}@"
+ "%{public}@: storeSignedClinicalData finished extracting SMARTHealthLinks"
+ "%{public}@: storeSignedClinicalData found %lu new medical record(s) after extracting SMARTHealthLinks, awaiting concept indexing before notifying new medical records observers for accountRowID %{public}@"
+ "%{public}@: storeSignedClinicalData found no new medical records after extraction (before: %{public}@, after: %{public}@)"
+ "%{public}@: storeSignedClinicalData missing accountRowID, cannot determine whether new medical records were created"
+ "%{public}@: storeSignedClinicalData received SMARTHealthLink extraction error %{public}@"
+ "%{public}@: storeSignedClinicalData received SMARTHealthLink, storing data"
+ ") than what we support ("
+ ".health.apple.com"
+ ".questdiagnostics.com"
+ "00000000-0000-0000-0000-000000000000"
+ "Apple Sandbox"
+ "Batch gateway fetch is not supported by the legacy provider service."
+ "Clinical health link already stored; reusing existing %s"
+ "ContentType %@ has no preferred filename extension"
+ "ContentType not recognized: %@"
+ "HDClinicalHealthLinkSyncEntity expects HDCodableClinicalHealthLink"
+ "HealthRecordsPlugin.HDInsertClinicalHealthLinkOperation"
+ "HealthRecordsPlugin.HDSMARTHealthLinkManager"
+ "Inserting clinical health link %s"
+ "NOT EXISTS (SELECT 1 FROM %@ AS mr JOIN %@ AS scds ON scds.%@ = mr.%@ WHERE mr.%@ = %@.%@)"
+ "Only SMART Health Link values are supported"
+ "Quest (Staging)"
+ "Quest Diagnostics"
+ "Stored new clinical health link %s"
+ "Unable to insert journaled clinical health link %s because of a constraint violation, likely because the link already exists. Ignoring error: %@"
+ "api-stage-experience.questdiagnostics.com"
+ "codable clinical health link is invalid: "
+ "compatibility version is higher ("
+ "health-records-profile-extension-new-medical-records"
+ "no message version"
+ "stored SMARTHealthLinks"
+ "v16@?0@\"<HDHealthRecordsNewMedicalRecordsObserver>\"8"
- "#/"
- "%{public}@ attempting to run on profile %{public}@ which does not have a sharing manager"
- "%{public}@ failed to schedule clinical sharing: %{public}@"
- "%{public}@ scheduling clinical sharing for added samples"
- "%{public}@: failed to submit clinical sharing daily analytics, error: %@"
- "ContentType not supported: %@"
- "HDClinicalProviderServiceManager.m"
- "Now running %@"
```
