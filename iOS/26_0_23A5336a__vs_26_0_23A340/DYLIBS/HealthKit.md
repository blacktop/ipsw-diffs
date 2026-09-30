## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

 6106.1.2.11.0
-  __TEXT.__text: 0x333180
-  __TEXT.__auth_stubs: 0x36d0
-  __TEXT.__objc_methlist: 0x2f98c
-  __TEXT.__cstring: 0x34d73
-  __TEXT.__const: 0xabfa2
-  __TEXT.__oslogstring: 0xc263
-  __TEXT.__gcc_except_tab: 0x4070
+  __TEXT.__text: 0x341ff4
+  __TEXT.__auth_stubs: 0x37a0
+  __TEXT.__objc_methlist: 0x2fc14
+  __TEXT.__cstring: 0x35a13
+  __TEXT.__const: 0xac5c2
+  __TEXT.__oslogstring: 0xc623
+  __TEXT.__gcc_except_tab: 0x4138
   __TEXT.__ustring: 0x78
-  __TEXT.__dlopen_cstrs: 0x5da
-  __TEXT.__constg_swiftt: 0x2fa4
-  __TEXT.__swift5_typeref: 0x2cf9
-  __TEXT.__swift5_fieldmd: 0x2ce4
-  __TEXT.__swift5_builtin: 0x398
+  __TEXT.__dlopen_cstrs: 0x644
+  __TEXT.__constg_swiftt: 0x3064
+  __TEXT.__swift5_typeref: 0x2ed9
+  __TEXT.__swift5_builtin: 0x3fc
   __TEXT.__swift5_reflstr: 0x1e92
-  __TEXT.__swift5_assocty: 0xb78
-  __TEXT.__swift5_proto: 0xbdc
-  __TEXT.__swift5_types: 0x400
-  __TEXT.__swift5_capture: 0x78c
-  __TEXT.__swift_as_entry: 0x14c
-  __TEXT.__swift_as_ret: 0x14c
-  __TEXT.__swift5_protos: 0x4c
+  __TEXT.__swift5_fieldmd: 0x2d2c
+  __TEXT.__swift5_assocty: 0xc20
+  __TEXT.__swift5_proto: 0xc2c
+  __TEXT.__swift5_types: 0x414
+  __TEXT.__swift5_capture: 0x940
+  __TEXT.__swift_as_entry: 0x170
+  __TEXT.__swift_as_ret: 0x174
+  __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xf8d8
-  __TEXT.__eh_frame: 0x3fe8
-  __TEXT.__objc_classname: 0x89b5
-  __TEXT.__objc_methname: 0x5d7b3
-  __TEXT.__objc_methtype: 0xbf51
-  __TEXT.__objc_stubs: 0x2b2a0
-  __DATA_CONST.__got: 0x1b10
-  __DATA_CONST.__const: 0xf4a0
-  __DATA_CONST.__objc_classlist: 0x1ab8
+  __TEXT.__unwind_info: 0xfc98
+  __TEXT.__eh_frame: 0x4628
+  __TEXT.__objc_classname: 0x89e6
+  __TEXT.__objc_methname: 0x5ddef
+  __TEXT.__objc_methtype: 0xbfad
+  __TEXT.__objc_stubs: 0x2b4a0
+  __DATA_CONST.__got: 0x1b58
+  __DATA_CONST.__const: 0xf678
+  __DATA_CONST.__objc_classlist: 0x1ad0
   __DATA_CONST.__objc_catlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0x7f0
+  __DATA_CONST.__objc_protolist: 0x808
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11360
-  __DATA_CONST.__objc_protorefs: 0x608
+  __DATA_CONST.__objc_selrefs: 0x114a8
+  __DATA_CONST.__objc_protorefs: 0x618
   __DATA_CONST.__objc_superrefs: 0x1730
-  __DATA_CONST.__objc_arraydata: 0x6910
-  __AUTH_CONST.__auth_got: 0x1b80
-  __AUTH_CONST.__const: 0xc050
-  __AUTH_CONST.__cfstring: 0x321a0
-  __AUTH_CONST.__objc_const: 0x4fe08
-  __AUTH_CONST.__objc_intobj: 0x45c0
+  __DATA_CONST.__objc_arraydata: 0x6958
+  __AUTH_CONST.__auth_got: 0x1be8
+  __AUTH_CONST.__const: 0xc6a0
+  __AUTH_CONST.__cfstring: 0x326a0
+  __AUTH_CONST.__objc_const: 0x50260
+  __AUTH_CONST.__objc_intobj: 0x4608
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
-  __AUTH_CONST.__objc_arrayobj: 0x6f0
-  __AUTH.__objc_data: 0xeaf0
-  __AUTH.__data: 0x1938
-  __DATA.__objc_ivar: 0x2dd0
-  __DATA.__data: 0xce58
-  __DATA.__bss: 0x182b0
-  __DATA.__common: 0x9a0
+  __AUTH_CONST.__objc_arrayobj: 0x720
+  __AUTH.__objc_data: 0xec40
+  __AUTH.__data: 0x19a8
+  __DATA.__objc_ivar: 0x2dec
+  __DATA.__data: 0xd0c8
+  __DATA.__bss: 0x18c60
+  __DATA.__common: 0x9c0
   __DATA_DIRTY.__objc_data: 0x2480
   __DATA_DIRTY.__data: 0x130
   __DATA_DIRTY.__bss: 0xca8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: EE090EAE-EC92-3DDF-9959-25CD8636248A
-  Functions: 23908
-  Symbols:   60702
-  CStrings:  29770
+  UUID: 45984941-72CA-30C0-8EC5-20DC2936C6AE
+  Functions: 24208
+  Symbols:   60976
+  CStrings:  29980
 
Symbols:
+ +[HKObjectType appleSleepScoreType]
+ +[HKObjectType hypertensionEventType]
+ +[HKObjectType hypertensiveMeasurementType]
+ +[NSURL(_HKURLSupport) _hk_urlForHypertensionEventType]
+ -[HKHealthServicesManager _fetchHealthKitDataWriteStatusWithIdentifier:completion:]
+ -[HKHealthServicesManager _getAudioAccessoryWriteStatusForIdentifier:completion:]
+ -[HKHealthServicesManager _getAudioHRMDevicesWithCompletion:]
+ -[HKHealthServicesManager _setAudioAccessoryWriteStatusEnabled:identifier:completion:]
+ -[HKHealthServicesManager _setHealthKitDataWriteEnabled:identifier:completion:]
+ -[_HKFeatureFlags chutney]
+ -[_HKFeatureFlags hermit]
+ -[_HKFeatureFlags setChutney:]
+ -[_HKFeatureFlags setHermit:]
+ -[_HKFeatureFlags setSleepDetails:]
+ -[_HKFeatureFlags sleepDetails]
+ GCC_except_table124
+ GCC_except_table156
+ GCC_except_table65
+ GCC_except_table74
+ _AudioAccessoryServicesLibrary
+ _AudioAccessoryServicesLibrary.cold.1
+ _AudioAccessoryServicesLibraryCore.frameworkLibrary
+ _HKBloodPressureClassificationCategoryAHAElevated
+ _HKBloodPressureClassificationCategoryAHAHypertensionStage1
+ _HKBloodPressureClassificationCategoryAHAHypertensionStage2
+ _HKBloodPressureClassificationCategoryAHAHypertensiveCrisis
+ _HKBloodPressureClassificationCategoryAHANormal
+ _HKBloodPressureClassificationCategoryESCElevated
+ _HKBloodPressureClassificationCategoryESCHypertension
+ _HKBloodPressureClassificationCategoryESCHypertensiveEmergency
+ _HKBloodPressureClassificationCategoryESCNonElevated
+ _HKBloodPressureClassificationCategoryFIGOMildlyElevated
+ _HKBloodPressureClassificationCategoryFIGONormal
+ _HKBloodPressureClassificationCategoryFIGOSeverelyElevated
+ _HKBloodPressureClassificationCategoryForGuidelines
+ _HKBloodPressureClassificationCategoryUnavailable
+ _HKBloodPressureClassificationGuidelinesIdentifierForGuidelines
+ _HKCategoryTypeIdentifierHypertensionEvent
+ _HKFeatureIdentifierBloodPressureJournal
+ _HKFeatureIdentifierHearingProtectionPPE
+ _HKFeatureIdentifierHypertensionNotifications
+ _HKIsAgeGatedUserDefaultsBloodPressureClassificationKey
+ _HKLogBloodPressureJournal
+ _HKLogBloodPressureJournal.category
+ _HKLogBloodPressureJournal.cold.1
+ _HKLogBloodPressureJournal.onceToken
+ _HKQuantityTypeIdentifierHypertensivePatternMeasurement
+ _OBJC_CLASS_$_HKBloodPressureClassificationCategoryData
+ _OBJC_CLASS_$_HKBloodPressureClassificationEvaluator
+ _OBJC_CLASS_$_HKBloodPressureClassificationManager
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_IVAR_$_HKHealthServicesManager._audioDeviceManager
+ _OBJC_IVAR_$_HKHealthServicesManager._audioDeviceManagerActivated
+ _OBJC_IVAR_$_HKHealthServicesManager._audioStateMonitor
+ _OBJC_IVAR_$_HKHealthServicesManager._audioStateMonitorActivated
+ _OBJC_IVAR_$__HKFeatureFlags._chutney
+ _OBJC_IVAR_$__HKFeatureFlags._hermit
+ _OBJC_IVAR_$__HKFeatureFlags._sleepDetails
+ _OBJC_METACLASS_$_HKBloodPressureClassificationCategoryData
+ _OBJC_METACLASS_$_HKBloodPressureClassificationEvaluator
+ _OBJC_METACLASS_$_HKBloodPressureClassificationManager
+ __CLASS_METHODS_HKBloodPressureClassificationEvaluator
+ __DATA_HKBloodPressureClassificationCategoryData
+ __DATA_HKBloodPressureClassificationEvaluator
+ __DATA_HKBloodPressureClassificationManager
+ __HKDataTypeIdentifierAppleSleepScore
+ __INSTANCE_METHODS_HKBloodPressureClassificationEvaluator
+ __IVARS_HKBloodPressureClassificationCategoryData
+ __IVARS_HKBloodPressureClassificationManager
+ __METACLASS_DATA_HKBloodPressureClassificationCategoryData
+ __METACLASS_DATA_HKBloodPressureClassificationEvaluator
+ __METACLASS_DATA_HKBloodPressureClassificationManager
+ __OBJC_$_INSTANCE_METHODS_HKBloodPressureClassificationCategoryData(HealthKit)
+ __OBJC_$_INSTANCE_METHODS_HKBloodPressureClassificationManager(HealthKit)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKBloodPressureClassificationManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKBloodPressureClassificationManagerObserver
+ __OBJC_CLASS_PROTOCOLS_$_HKBloodPressureClassificationManager(HealthKit)
+ __OBJC_LABEL_PROTOCOL_$_HKBloodPressureClassificationManagerObserver
+ __OBJC_PROTOCOL_$_HKBloodPressureClassificationManagerObserver
+ ___102-[HKHealthServicesManager clientRemote_deliverSessionHealthServiceStatus:toClient:finished:withError:]_block_invoke.103
+ ___102-[HKHealthServicesManager clientRemote_deliverSessionHealthServiceStatus:toClient:finished:withError:]_block_invoke.103.cold.1
+ ___25-[_HKFeatureFlags hermit]_block_invoke
+ ___26-[_HKFeatureFlags chutney]_block_invoke
+ ___31-[_HKFeatureFlags sleepDetails]_block_invoke
+ ___61-[HKHealthServicesManager _getAudioHRMDevicesWithCompletion:]_block_invoke
+ ___63-[HKHealthServicesManager healthAudioHRMDevicesWithCompletion:]_block_invoke
+ ___72-[HKHealthServicesManager getEnabledStatusForPeripheral:withCompletion:]_block_invoke
+ ___72-[HKHealthServicesManager getEnabledStatusForPeripheral:withCompletion:]_block_invoke_2
+ ___73-[HKHealthServicesManager setEnabledStatus:forPeripheral:withCompletion:]_block_invoke
+ ___73-[HKHealthServicesManager setEnabledStatus:forPeripheral:withCompletion:]_block_invoke_2
+ ___79-[HKHealthServicesManager _setHealthKitDataWriteEnabled:identifier:completion:]_block_invoke
+ ___81-[HKHealthServicesManager _getAudioAccessoryWriteStatusForIdentifier:completion:]_block_invoke
+ ___86-[HKHealthServicesManager _setAudioAccessoryWriteStatusEnabled:identifier:completion:]_block_invoke
+ ___98-[HKHealthServicesManager clientRemote_deliverDiscoveryHealthService:toClient:finished:withError:]_block_invoke.102
+ ___98-[HKHealthServicesManager clientRemote_deliverDiscoveryHealthService:toClient:finished:withError:]_block_invoke.102.cold.1
+ ___AudioAccessoryServicesLibraryCore_block_invoke
+ ___HKLogBloodPressureJournal_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSNumber"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40bs48w_e20_v20?0B8"NSError"12ls40l8w48l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_tmp.187
+ ___block_literal_global.102
+ ___block_literal_global.108
+ ___block_literal_global.111
+ ___block_literal_global.114
+ ___block_literal_global.120
+ ___block_literal_global.123
+ ___block_literal_global.132
+ ___block_literal_global.135
+ ___block_literal_global.138
+ ___block_literal_global.156
+ ___block_literal_global.189
+ ___block_literal_global.90
+ ___block_literal_global.96
+ ___block_literal_global.99
+ ___getAADeviceConfigClass_block_invoke
+ ___getAADeviceConfigClass_block_invoke.cold.1
+ ___getAADeviceManagerClass_block_invoke
+ ___getAADeviceManagerClass_block_invoke.cold.1
+ ___getAASystemStateMonitorClass_block_invoke
+ ___getAASystemStateMonitorClass_block_invoke.cold.1
+ ___swift_project_boxed_opaque_existential_1Tm
+ _associated conformance So13HKCountryCodeaSHSCSQ
+ _associated conformance So13HKCountryCodeas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So13HKCountryCodeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So37HKBloodPressureClassificationCategoryaSHSCSQ
+ _associated conformance So37HKBloodPressureClassificationCategoryas12CaseIterable9HealthKit8AllCasessACP_Sl
+ _associated conformance So37HKBloodPressureClassificationCategoryas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So37HKBloodPressureClassificationCategoryas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So39HKBloodPressureClassificationGuidelinesVSHSCSQ
+ _associated conformance So39HKBloodPressureClassificationGuidelinesVs12CaseIterable9HealthKit8AllCasessACP_Sl
+ _audit_stringAudioAccessoryServices
+ _block_copy_helper.102
+ _block_copy_helper.116
+ _block_copy_helper.20
+ _block_copy_helper.38
+ _block_copy_helper.69
+ _block_copy_helper.90
+ _block_copy_helper.95
+ _block_descriptor.104
+ _block_descriptor.118
+ _block_descriptor.22
+ _block_descriptor.40
+ _block_descriptor.71
+ _block_descriptor.92
+ _block_descriptor.97
+ _block_destroy_helper.103
+ _block_destroy_helper.117
+ _block_destroy_helper.21
+ _block_destroy_helper.39
+ _block_destroy_helper.70
+ _block_destroy_helper.91
+ _block_destroy_helper.96
+ _getAADeviceConfigClass.softClass
+ _getAADeviceManagerClass.softClass
+ _getAASystemStateMonitorClass.softClass
+ _kHKAgeGatingKeyEnableBloodPressureClassification
+ _kHKBloodPressureClassificationAgeGatingAge
+ _kHKBloodPressureClassificationDefaultsDomain
+ _kHKBloodPressureClassificationUserPreferredClassificationGuidelinesKey
+ _kHKHypertensionNotificationsAgeGatingAge
+ _objc_msgSend$_fetchHealthKitDataWriteStatusWithIdentifier:completion:
+ _objc_msgSend$_forAAFeatureCapability:
+ _objc_msgSend$_getAudioAccessoryWriteStatusForIdentifier:completion:
+ _objc_msgSend$_getAudioHRMDevicesWithCompletion:
+ _objc_msgSend$_setAudioAccessoryWriteStatusEnabled:identifier:completion:
+ _objc_msgSend$_setHealthKitDataWriteEnabled:identifier:completion:
+ _objc_msgSend$chutney
+ _objc_msgSend$fetchHealthKitDataWriteAllowedForDevice:
+ _objc_msgSend$fetchPairedHRMDevices:
+ _objc_msgSend$heartRateMonitorCapability
+ _objc_msgSend$hermit
+ _objc_msgSend$hypertensionEventType
+ _objc_msgSend$initWithAudioAccessoryDevice:
+ _objc_msgSend$sendDeviceConfig:identifier:completion:
+ _objc_msgSend$setAllowHealthKitDataWrite:
+ _objc_msgSend$sleepDetails
+ _objectdestroy.17Tm
+ _objectdestroy.24Tm
+ _objectdestroy.32Tm
+ _swift_isEscapingClosureAtFileLocation
+ _swift_task_create
+ _symbolic $s9HealthKit52HKBloodPressureClassificationPregnancyModelProvidingP
+ _symbolic Ig_
+ _symbolic Say_____G So37HKBloodPressureClassificationCategorya
+ _symbolic Say_____G So39HKBloodPressureClassificationGuidelinesV
+ _symbolic Sb______pSgIeghyg_Sg s5ErrorP
+ _symbolic ScA_pSg
+ _symbolic ScCySo18HKMCPregnancyModelC______pG s5ErrorP
+ _symbolic So13HKHealthStoreCSgXwz_Xx
+ _symbolic So36HKBloodPressureClassificationManagerC
+ _symbolic So36HKBloodPressureClassificationManagerCSgXw
+ _symbolic So36HKBloodPressureClassificationManagerCXDXMT
+ _symbolic _____ So13HKCountryCodea
+ _symbolic _____ So18HKMCPregnancyStateV
+ _symbolic _____ So37HKBloodPressureClassificationCategorya
+ _symbolic _____ So39HKBloodPressureClassificationGuidelinesV
+ _symbolic _____ So54HKBloodPressureClassificationCategoryRangeRelationshipV
+ _symbolic _____Ieghy_ So39HKBloodPressureClassificationGuidelinesV
+ _symbolic _____IeyBhy_ So39HKBloodPressureClassificationGuidelinesV
+ _symbolic _____So7NSErrorCSgIeyBhyy_ 10ObjectiveC8ObjCBoolV
+ _symbolic ytIeAgHr_
- ___102-[HKHealthServicesManager clientRemote_deliverSessionHealthServiceStatus:toClient:finished:withError:]_block_invoke.95
- ___102-[HKHealthServicesManager clientRemote_deliverSessionHealthServiceStatus:toClient:finished:withError:]_block_invoke.95.cold.1
- ___98-[HKHealthServicesManager clientRemote_deliverDiscoveryHealthService:toClient:finished:withError:]_block_invoke.94
- ___98-[HKHealthServicesManager clientRemote_deliverDiscoveryHealthService:toClient:finished:withError:]_block_invoke.94.cold.1
- ___block_literal_global.104
- ___block_literal_global.107
- ___block_literal_global.110
- ___block_literal_global.116
- ___block_literal_global.119
- ___block_literal_global.131
- ___block_literal_global.140
- ___block_literal_global.151
- ___block_literal_global.74
- ___block_literal_global.92
- ___block_literal_global.95
CStrings:
+ "@\"AADeviceManager\""
+ "@\"AASystemStateMonitor\""
+ "@56@0:8q16@24@32@40q48"
+ "AADeviceConfig"
+ "AADeviceManager"
+ "AASystemStateMonitor"
+ "AHA"
+ "AHA.Elevated"
+ "AHA.HypertensionStage1"
+ "AHA.HypertensionStage2"
+ "AHA.HypertensiveCrisis"
+ "AHA.Normal"
+ "APPLE_SLEEP_SCORE"
+ "AirPods3,4"
+ "American Heart Association (AHA)"
+ "Audio accessory state unknown."
+ "Audio device manager inactive. Abort set healthkit data."
+ "Audio state monitor inactive. Abort fetch healthkit data write info."
+ "B48@0:8q16@24@32@40"
+ "Blood Pressure Journal Notifications"
+ "Blood Pressure classification is unavailable for age <"
+ "Blood Pressure onboarding record country code unavailable with error: %s"
+ "BloodPressureClassificationGuidelines"
+ "BloodPressureJournal"
+ "Chutney"
+ "Class getAADeviceConfigClass(void)_block_invoke"
+ "Class getAADeviceManagerClass(void)_block_invoke"
+ "Class getAASystemStateMonitorClass(void)_block_invoke"
+ "Classification unavailable for the provided values"
+ "Device1,22034"
+ "Device1,8232"
+ "Device1,8233"
+ "Device1,8239"
+ "Diastolic quantity must be compatible with mmHg unit"
+ "ESC"
+ "ESC.Elevated"
+ "ESC.Hypertension"
+ "ESC.HypertensiveEmergency"
+ "ESC.NonElevated"
+ "EnableBloodPressureClassificationAgeGating"
+ "EnableChutneyLiveOn"
+ "EnableHermitLiveOn"
+ "European Society of Cardiology (ESC)"
+ "FIGO"
+ "FIGO.MildlyElevated"
+ "FIGO.Normal"
+ "FIGO.SeverelyElevated"
+ "Get audio accessory write status not found or failed for identifier %@ error: %@"
+ "HKBloodPressureClassificationCategoryData"
+ "HKBloodPressureClassificationEvaluator"
+ "HKBloodPressureClassificationManager"
+ "HKBloodPressureClassificationManagerObserver"
+ "HKCategoryTypeIdentifierHypertensionEvent"
+ "HKDataTypeAppleSleepScore"
+ "HKLogBloodPressureJournal"
+ "HKObjectType_SleepAnalysisLegacyCategoryRoom"
+ "HKQuantityTypeIdentifierHypertensivePatternMeasurement"
+ "HYPERTENSION_EVENT"
+ "HYPERTENSIVE_PATTERN_MEASUREMENT"
+ "HealthKit/HKBloodPressureClassificationCategoryData.swift"
+ "HealthKit_Private.HKBloodPressureClassificationCategoryData"
+ "HealthKit_Private.HKBloodPressureClassificationManager"
+ "Hearing Protection PPE"
+ "HearingProtectionPPE"
+ "Hermit"
+ "Hypertension Notifications"
+ "HypertensionNotifications"
+ "International Federation of Gynecology and Obstetrics (FIGO)"
+ "Localizable-Hermit"
+ "Localizable-SleepDetails"
+ "Set audio accessory write status failed for identifier %@ error: %@"
+ "Systolic quantity must be compatible with mmHg unit"
+ "T@\"NSString\",N,R,Videntifier"
+ "Td,N,R,VdiastolicLowerBound"
+ "Td,N,R,VdiastolicUpperBound"
+ "Td,N,R,VsystolicLowerBound"
+ "Td,N,R,VsystolicUpperBound"
+ "Tq,N,R,VclassificationGuidelines"
+ "Tq,N,R,VrangeRelationship"
+ "Unable to determine blood pressure classification with error: %s"
+ "Unavailable"
+ "Unsupported Blood Pressure classification category"
+ "Unsupported Blood Pressure classification guidelines"
+ "Unsupported range relationship"
+ "[%s] database is inaccessible; unable to determine user age"
+ "[%s] database is inaccessible; unable to determine user preferred blood pressure classification guidelines"
+ "[%s] unexpected classification guidelines provided for hypertensive escalation"
+ "[%s]: Guidelines are %s on %s"
+ "[%s]: deleting preferred blood pressure guidelines"
+ "[%s]: received error from pregnancy state query, using preferred classification guidelines. error: %s"
+ "[%s]: setting preferred blood pressure guidelines: %s"
+ "[%s]: user preferred blood pressure classification guidelines not available, using default classification guidelines"
+ "_audioDeviceManager"
+ "_audioDeviceManagerActivated"
+ "_audioStateMonitor"
+ "_audioStateMonitorActivated"
+ "_chutney"
+ "_createCheckedContinuation(_:)"
+ "_fetchHealthKitDataWriteStatusWithIdentifier:completion:"
+ "_getAudioAccessoryWriteStatusForIdentifier:completion:"
+ "_getAudioHRMDevicesWithCompletion:"
+ "_hermit"
+ "_hk_urlForHypertensionEventType"
+ "_setAudioAccessoryWriteStatusEnabled:identifier:completion:"
+ "_setHealthKitDataWriteEnabled:identifier:completion:"
+ "_sleepDetails"
+ "appleSleepScoreType"
+ "bloodPressureDefaultsDomain"
+ "blood_pressure_classification"
+ "blood_pressure_classification_manager"
+ "categoriesForClassificationGuidelines:error:"
+ "categoryDataForCategory:error:"
+ "categoryForClassificationGuidelines:systolic:diastolic:"
+ "categoryForClassificationGuidelines:systolic:diastolic:age:"
+ "chutney"
+ "classificationGuidelines"
+ "classificationGuidelinesOnDate:completionHandler:"
+ "com.apple.private.health.blood-pressure-classification"
+ "currentClassificationGuidelinesWithCompletionHandler:"
+ "defaultClassificationGuidelinesForCountryCode:"
+ "diastolicLowerBound"
+ "diastolicRange"
+ "diastolicUpperBound"
+ "didUpdatePreferredClassificationGuidelines:"
+ "fetchHealthKitDataWriteAllowedForDevice:"
+ "fetchPairedHRMDevices:"
+ "hearing-protection-ppe"
+ "hermit"
+ "hypertensionEventType"
+ "hypertensiveEscalationForClassificationGuidelines:systolic:diastolic:age:"
+ "hypertensiveMeasurementType"
+ "initWithClassificationGuidelines:identifier:systolicRange:diastolicRange:rangeRelationship:"
+ "isClassificationAgeGated"
+ "observerQueue"
+ "preferredClassificationGuidelinesWithCompletionHandler:"
+ "pregnancyModel()"
+ "pregnancyModelProvider"
+ "rangeRelationship"
+ "removePreferredClassificationGuidelinesWithCompletionHandler:"
+ "sendDeviceConfig:identifier:completion:"
+ "setAllowHealthKitDataWrite:"
+ "setChutney:"
+ "setHermit:"
+ "setSleepDetails:"
+ "sleepDetails"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices"
+ "startObserving:"
+ "stopObserving:"
+ "systolicLowerBound"
+ "systolicRange"
+ "systolicUpperBound"
+ "updatePreferredClassificationGuidelines:completionHandler:"
+ "v16@?0@\"<HKBloodPressureClassificationManagerObserver>\"8"
+ "v24@0:8@\"HKBloodPressureClassificationManager\"16"
+ "void *AudioAccessoryServicesLibrary(void)"
+ "yodel-protection-ppe"
- "Audio Accessory is not supported on this platform"
- "Reserved16"
- "Reserved9"

```
