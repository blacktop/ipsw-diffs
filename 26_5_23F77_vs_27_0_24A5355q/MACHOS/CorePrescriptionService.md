## CorePrescriptionService

> `/System/Library/PrivateFrameworks/CorePrescription.framework/XPCServices/CorePrescriptionService.xpc/CorePrescriptionService`

```diff

-207.100.10.0.0
-  __TEXT.__text: 0x87088
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x16a4
-  __TEXT.__const: 0xb3f8
-  __TEXT.__objc_methname: 0x373f
-  __TEXT.__objc_classname: 0xa92
-  __TEXT.__objc_methtype: 0x11ba
-  __TEXT.__cstring: 0x2a74
-  __TEXT.__oslogstring: 0x1008
+230.0.0.0.0
+  __TEXT.__text: 0xd019c
+  __TEXT.__auth_stubs: 0x1f40
+  __TEXT.__objc_stubs: 0x1600
+  __TEXT.__objc_methlist: 0x2070
+  __TEXT.__const: 0xd09c
+  __TEXT.__objc_methname: 0x4ed7
+  __TEXT.__objc_classname: 0xea2
+  __TEXT.__cstring: 0x409c
+  __TEXT.__objc_methtype: 0x175d
+  __TEXT.__oslogstring: 0xd12
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1f1c
-  __TEXT.__swift5_typeref: 0x12a8
-  __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_reflstr: 0x19a3
-  __TEXT.__swift5_fieldmd: 0x18ec
-  __TEXT.__swift5_assocty: 0x360
-  __TEXT.__swift5_proto: 0x37c
-  __TEXT.__swift5_types: 0x19c
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0xac4
-  __TEXT.__swift_as_entry: 0x1e4
-  __TEXT.__swift_as_ret: 0x250
-  __TEXT.__unwind_info: 0x2730
-  __TEXT.__eh_frame: 0x5ec8
-  __DATA_CONST.__auth_got: 0xe00
-  __DATA_CONST.__got: 0x528
-  __DATA_CONST.__auth_ptr: 0x658
-  __DATA_CONST.__const: 0x2f78
-  __DATA_CONST.__cfstring: 0x2c0
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __TEXT.__constg_swiftt: 0x2c7c
+  __TEXT.__swift5_typeref: 0x160c
+  __TEXT.__swift5_builtin: 0x230
+  __TEXT.__swift5_reflstr: 0x2283
+  __TEXT.__swift5_fieldmd: 0x1fcc
+  __TEXT.__swift5_assocty: 0x438
+  __TEXT.__swift5_proto: 0x424
+  __TEXT.__swift5_types: 0x21c
+  __TEXT.__swift5_protos: 0x14
+  __TEXT.__swift5_capture: 0x17e8
+  __TEXT.__swift_as_entry: 0x3cc
+  __TEXT.__swift_as_ret: 0x45c
+  __TEXT.__swift_as_cont: 0x9e4
+  __TEXT.__swift5_mpenum: 0x20
+  __TEXT.__unwind_info: 0x4490
+  __TEXT.__eh_frame: 0xa4e0
+  __DATA_CONST.__const: 0x5210
+  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA.__objc_const: 0x52c0
-  __DATA.__objc_selrefs: 0xaf8
-  __DATA.__objc_ivar: 0x80
-  __DATA.__objc_data: 0x1ab0
-  __DATA.__data: 0x3410
-  __DATA.__bss: 0x6da0
-  __DATA.__common: 0x20c
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__auth_got: 0xfa8
+  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__auth_ptr: 0x938
+  __DATA.__objc_const: 0x6bc0
+  __DATA.__objc_selrefs: 0xeb0
+  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_data: 0x26e8
+  __DATA.__data: 0x43e0
+  __DATA.__bss: 0x8210
+  __DATA.__common: 0x238
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CloudKitCodeProtobuf.framework/CloudKitCodeProtobuf
   - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ManagedAssets.framework/ManagedAssets

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 426E2380-D39D-3D25-A4D4-2BC763AC7E1D
-  Functions: 2880
-  Symbols:   460
-  CStrings:  1276
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 6435BA9C-D80C-381A-9EEE-EEFB36F28056
+  Functions: 4227
+  Symbols:   513
+  CStrings:  1600
 
Symbols:
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _HKMetadataKeyGlassesPrescriptionDescription
+ _HKMetadataKeySyncIdentifier
+ _HKMetadataKeySyncVersion
+ _HKQuantityRangeInclusive
+ _NSClassFromString
+ _OBJC_CLASS_$_CRXCAppClipCodeScannerErrorConstants
+ _OBJC_CLASS_$_CRXCAppClipCodeTranscoderErrorConstants
+ _OBJC_CLASS_$_CRXCCompositorData
+ _OBJC_CLASS_$_CRXCContextSessionDonStatus
+ _OBJC_CLASS_$_CRXCCorePrescriptionServiceErrorConstants
+ _OBJC_CLASS_$_CRXCDataManagerErrorConstants
+ _OBJC_CLASS_$_CRXCDataStoreErrorConstants
+ _OBJC_CLASS_$_CRXCHealthRecord
+ _OBJC_CLASS_$_CRXCOption
+ _OBJC_CLASS_$_CRXCOptionValue
+ _OBJC_CLASS_$_HKDevice
+ _OBJC_CLASS_$_HKGlassesLensSpecification
+ _OBJC_CLASS_$_HKObject
+ _OBJC_CLASS_$_HKQuantity
+ _OBJC_CLASS_$_HKUnit
+ _OBJC_CLASS_$_HKVisionPrism
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_METACLASS_$_CRXCAppClipCodeScannerErrorConstants
+ _OBJC_METACLASS_$_CRXCAppClipCodeTranscoderErrorConstants
+ _OBJC_METACLASS_$_CRXCCompositorData
+ _OBJC_METACLASS_$_CRXCContextSessionDonStatus
+ _OBJC_METACLASS_$_CRXCCorePrescriptionServiceErrorConstants
+ _OBJC_METACLASS_$_CRXCDataManagerErrorConstants
+ _OBJC_METACLASS_$_CRXCDataStoreErrorConstants
+ _OBJC_METACLASS_$_CRXCHealthRecord
+ _OBJC_METACLASS_$_CRXCOption
+ _OBJC_METACLASS_$_CRXCOptionValue
+ _VRX_CURRENT_FORMAT_VERSION
+ _VRX_FALSE
+ _VRX_FIRST_FORMAT_VERSION
+ _VRX_TRUE
+ __HKPrivateMetadataKeyVisionColorCode
+ __HKPrivateMetadataKeyVisionDeviceSpecificLensType
+ __HKPrivateMetadataKeyVisionReaderStrengthRangeHigh
+ __HKPrivateMetadataKeyVisionReaderStrengthRangeLow
+ __HKPrivateMetadataKeyVisionSerialNumber
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_stdlib_strtod_clocale
+ _atoi
+ _dlopen
+ _isVM
+ _memset
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x3
+ _setGlobalPreferences
+ _strcasecmp
+ _strncmp
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_makeBoxUnique
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x10
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_retain_x9
+ _swift_task_addCancellationHandler
+ _swift_task_removeCancellationHandler
+ _vrx_find_matching_lenses
+ _vrx_get_metadata_key
+ _vrx_lens_matching_options_set_defaults
+ _vrx_lens_tray_file_extension
+ _vrx_print_prism_rx
+ _vrx_prism_rx_equal
- _CRXUIsVM
- _CRXULoggingCategory
- _CRXULoggingSubsystem
- _CRXUObjectsEqual
- _OBJC_CLASS_$_CRXUDispatchGroup
- _OBJC_CLASS_$_CRXUDispatchQueue
- _OBJC_CLASS_$_CRXUDispatchSemaphore
- _OBJC_CLASS_$_CRXUFormatters
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_METACLASS_$_CRXUDispatchGroup
- _OBJC_METACLASS_$_CRXUDispatchQueue
- _OBJC_METACLASS_$_CRXUDispatchSemaphore
- _OBJC_METACLASS_$_CRXUFormatters
- __dispatch_main_q
- __dispatch_queue_attr_concurrent
- _dispatch_after
- _dispatch_assert_queue$V2
- _dispatch_barrier_async
- _dispatch_barrier_sync
- _dispatch_group_async
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_notify
- _dispatch_group_wait
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_attr_make_with_qos_class
- _dispatch_queue_get_label
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_sync
- _dispatch_time
- _objc_alloc_init
- _objc_retain_x9
- _swift_allocBox
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_stdlib_isStackAllocationSafe
- _swift_unexpectedError
CStrings:
+ " sessionDidStart: "
+ "%s (%c) - sn: %*s, seq#: %*s, "
+ ", activeComfortAdjustment: "
+ ", activeEnrollmentGroup: "
+ ", activePrismCorrection: "
+ ", comfortAdjustments: "
+ ", diopterRange: "
+ ", hasUserStatus: "
+ ", inputRecoveryReason: "
+ ", lastSelectedEnrollmentUUID: "
+ ", lastSyncedUser: "
+ ", lensIntrinsics: "
+ ", prescriptionState: "
+ ", prismCorrection: "
+ ", selectedEnrollment: "
+ ", serialNumber: "
+ ", userStatusIcon: "
+ ", userStatusMessage: "
+ ", userStatusTitle: "
+ "/System/Library/Frameworks/CloudKit.framework/CloudKit"
+ "/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain"
+ "@\"CRXCEnrollmentRecord\""
+ "@\"CRXCOptionValue\""
+ "@\"CRXCPrescriptionState\""
+ "@\"CRXCPrismCorrection\""
+ "@\"CRXCSystemStatus\""
+ "@128@0:8@16@24@32@40@48@56@64@72@80@88@96q104@112@120"
+ "@24@0:8q16"
+ "@40@0:8f16f20Q24f32f36"
+ "@56@0:8q16q24q32q40@48"
+ "@60@0:8B16Q20B28@32@40@48B56"
+ "@76@0:8Q16q24@32@40Q48Q56@64I72"
+ "A179"
+ "ARKit Callback Error"
+ "BD"
+ "BI"
+ "BO"
+ "BU"
+ "CRXCAppClipCodeScannerErrorConstants"
+ "CRXCAppClipCodeTranscoderErrorConstants"
+ "CRXCCompositorData"
+ "CRXCContextSessionDonStatus"
+ "CRXCContextSessionDonStatus(hasInputRecovery: "
+ "CRXCCorePrescriptionServiceErrorConstants"
+ "CRXCDataManagerErrorConstants"
+ "CRXCDataStoreErrorConstants"
+ "CRXCHealthRecord"
+ "CRXCOption"
+ "CRXCOptionValue"
+ "CompositorData(systemStatus: "
+ "CorePrescriptionService.AppClipCodeScannerError"
+ "CorePrescriptionService.AppClipCodeTranscoderError"
+ "CorePrescriptionService.CRXCCompositorData"
+ "CorePrescriptionService.CRXCContextSessionDonStatus"
+ "CorePrescriptionService.CRXCHealthRecord"
+ "CorePrescriptionService.CRXCOption"
+ "CorePrescriptionService.CRXCOptionValue"
+ "CorePrescriptionService.DataManagerError"
+ "CorePrescriptionService.DataStoreError"
+ "CorePrescriptionService.InternalDataStoreProfileChangeObserver"
+ "CorePrescriptionService.InternalDataStoreTableChangeObserver"
+ "Discarding prescription with duplicate ACC"
+ "DistributedNotificationCallbackQueue"
+ "Download error: %@"
+ "Enrollment already exists"
+ "Entering %s"
+ "ExecutionManager"
+ "Fetching Rx records for device model %s"
+ "HKGlassesPrescription"
+ "Health record to return: %@"
+ "HealthKit not available, HealthDataProvider will be inert"
+ "HealthRecord(leftRx: "
+ "Incompatible lens model"
+ "Initialization Error"
+ "Invalid ACC payload"
+ "Invalid JSON data"
+ "Invalid enrollment name"
+ "Invalid null value in record"
+ "Invalid option name"
+ "Invalid property name"
+ "Invalid value(s)"
+ "JSONObjectWithData:options:error:"
+ "Killing queued up lens pose algorthms"
+ "Lens pose estimation failed"
+ "Mismatched lens types"
+ "Multiple ACCs scanned"
+ "N50"
+ "No enrollment selected"
+ "Non-complementary ACCs scanned"
+ "OD Prism: "
+ "OS Prism: "
+ "Prescription to add has source bundle ID %s"
+ "RealityDevice14,1"
+ "RealityDevice14,3"
+ "RealityDevice17,1"
+ "RealityDevice99,3"
+ "RegulatoryDomain not available, returning nil country code"
+ "Returning country code: %s"
+ "Returning override country code: %s"
+ "Scanning already in progress"
+ "Skipping record for incompatible lens model %s"
+ "T@\"CRXCDiopterRange\",N,R,VreaderRange"
+ "T@\"CRXCEnrollmentRecord\",N,R,VselectedEnrollment"
+ "T@\"CRXCEyePrescription\",N,R,VleftRx"
+ "T@\"CRXCEyePrescription\",N,R,VrightRx"
+ "T@\"CRXCEyePrismCorrection\",N,R,VleftPrism"
+ "T@\"CRXCEyePrismCorrection\",N,R,VrightPrism"
+ "T@\"CRXCOptionValue\",N,R,VdefaultValue"
+ "T@\"CRXCOptionValue\",N,R,Vvalue"
+ "T@\"CRXCPrescriptionState\",N,R,VprescriptionState"
+ "T@\"CRXCPrismCorrection\",N,R,VactivePrismCorrection"
+ "T@\"CRXCPrismCorrection\",N,R,VprismCorrection"
+ "T@\"CRXCSystemStatus\",N,R,VsystemStatus"
+ "T@\"NSDictionary\",N,R"
+ "T@\"NSString\",N,C"
+ "TB,N,VhasInputRecovery"
+ "TB,N,VhasUserStatus"
+ "TB,N,VsessionDidStart"
+ "TQ,N,VinputRecoveryReason"
+ "TQ,N,VlensModel"
+ "Td,N,R"
+ "Tf,N,Vadd"
+ "Tq,N,R"
+ "Tq,N,R,VactiveEnrollmentGroup"
+ "Tq,N,R,VcolorCode"
+ "Trying to reprocess current gaze"
+ "Unsupported version"
+ "User profile switched to: %s"
+ "VRAdd clamped successfully!"
+ "X1078"
+ "_TtC23CorePrescriptionService10DebugTrace"
+ "_TtC23CorePrescriptionService12ContextState"
+ "_TtC23CorePrescriptionService17LensCompatibility"
+ "_TtC23CorePrescriptionService19ExecutionManagerXPC"
+ "_TtC23CorePrescriptionService25PrescriptionRecordFetcher"
+ "_TtC23CorePrescriptionService28VisionPrescriptionURLDecoder"
+ "_TtC23CorePrescriptionService29DistributedNotificationCenter"
+ "_TtC23CorePrescriptionServiceP33_721C45E69E13589B716B3DB30077E60936InternalDataStoreTableChangeObserver"
+ "_TtC23CorePrescriptionServiceP33_721C45E69E13589B716B3DB30077E60938InternalDataStoreProfileChangeObserver"
+ "_TtC23CorePrescriptionServiceP33_DF965F07F57F1EA5E47EC4BCCA95554B8Settings"
+ "_TtCC23CorePrescriptionService16ExecutionManagerP33_D980D2326E09A9A9FB863F29FCC1CBD212AnyExecution"
+ "_TtCC23CorePrescriptionService16ExecutionManagerP33_D980D2326E09A9A9FB863F29FCC1CBD215AnyContinuation"
+ "_TtCC23CorePrescriptionService19ExecutionManagerXPCP33_B083E35B69D7DD86D662644D1AEC016912AnyExecution"
+ "_TtCC23CorePrescriptionService19ExecutionManagerXPCP33_B083E35B69D7DD86D662644D1AEC016915AnyContinuation"
+ "__unit_test_property_3__"
+ "_deviceLocked"
+ "_doubleValue"
+ "_lensPoseFailedOnUserPresence"
+ "_lensSelectionUpdateAction"
+ "_lensSelectionUpdateRXUUID"
+ "_prescriptionPresenceRequired"
+ "_previousEnrollmentGroup"
+ "_requireLensPoseOnUserPresence"
+ "_requireLensPoseProcessing"
+ "_requirePreUnlockProcessing"
+ "_requireProcessingOnUserPresence"
+ "_setSourceBundleIdentifier:"
+ "_sourceBundleIdentifier"
+ "_stringValue"
+ "_userPresenceDetected"
+ "activateGuestPrism()"
+ "activateGuestPrismWithCompletionHandler:"
+ "activeComfortAdjustment"
+ "activeEnrollmentGroup"
+ "activePrismCorrection"
+ "add"
+ "addKVStoreEventObserver:storeNames:sharingGroup:profile:events:error:"
+ "addPower"
+ "addProfileChangeEventObserver:events:error:"
+ "allowLensFinder"
+ "allowLensPoseBeforeUnlock"
+ "allowReenrollmentNotifications"
+ "allowUnsupportedRX"
+ "arkitRXStateUpdateTimeout"
+ "arkitStartTimeout"
+ "boolForKey:"
+ "boolValue"
+ "bootTime"
+ "calibrationDataServerType"
+ "cancelEnrollmentScan()"
+ "cancelEnrollmentScanWithCompletionHandler:"
+ "checkLensPresence(updatePrescriptionState:)"
+ "checkLensPresenceWithUpdatePrescriptionState:completionHandler:"
+ "checkPrismActivationStatus()"
+ "checkPrismActivationStatusWithCompletionHandler:"
+ "checkWorldTrackingStatus(withTimeout:)"
+ "checkWorldTrackingStatusWithTimeout:completionHandler:"
+ "checksumHealthURL(url:)"
+ "checksumHealthURLWithUrl:completionHandler:"
+ "clipOnLensPresenceTimeout"
+ "clipOnLensUpdateTimeout"
+ "cloud sync status updated: %@"
+ "com.apple.Health"
+ "comfortAdjustments"
+ "commitFactoryCalibrationData(forEnrollmentWithUUID:)"
+ "commitFactoryCalibrationDataForEnrollmentWithUUID:completionHandler:"
+ "containsQuantity:"
+ "context"
+ "contextClearPrescriptionCache()"
+ "contextClearPrescriptionCacheWithCompletionHandler:"
+ "contextDeviceLock()"
+ "contextDeviceLockWithCompletionHandler:"
+ "contextDeviceUnlock()"
+ "contextDeviceUnlockWithCompletionHandler:"
+ "contextFetchPrescriptionPresenceState()"
+ "contextFetchPrescriptionPresenceStateWithCompletionHandler:"
+ "contextHandleChangeToEnrollments()"
+ "contextHandleChangeToEnrollmentsWithCompletionHandler:"
+ "contextHandlePresenceRequest()"
+ "contextHandlePresenceRequestWithCompletionHandler:"
+ "contextHandleProfileChanged()"
+ "contextHandleProfileChangedWithCompletionHandler:"
+ "contextResetWithCompletionHandler:"
+ "contextTable"
+ "contextUserPresenceDetected()"
+ "contextUserPresenceDetectedWithCompletionHandler:"
+ "contextUserPresenceLost()"
+ "contextUserPresenceLostWithCompletionHandler:"
+ "currentUser"
+ "deactivateGuestPrism()"
+ "deactivateGuestPrismWithCompletionHandler:"
+ "defaultUserNotificationTimeout"
+ "defaultUserStatusNotificationTimeout"
+ "defaultValue"
+ "degreeAngleUnit"
+ "deleteAllHealthRecords()"
+ "deleteAllHealthRecordsWithCompletionHandler:"
+ "deleteCloudSyncDataStore"
+ "deleteEnrollments(withOwner:)"
+ "deleteEnrollmentsWithOwner:completionHandler:"
+ "deleteHealthRecord(forACC:)"
+ "deleteHealthRecordForACC:completionHandler:"
+ "deleteObjects:withCompletion:"
+ "deviceSharingValidationThrottle"
+ "deviceType"
+ "diopterUnit"
+ "disableDemoLensAutoDeletion"
+ "displayOpticalInsertDetectionOverrideUI"
+ "doubleForKey:"
+ "doubleValue"
+ "doubleValueForUnit:"
+ "enableFactoryCalibrationFetch"
+ "enableRecoveryFlow"
+ "encodeAppClipCodePayload(_:age:)"
+ "encodeAppClipCodePayload:age:completionHandler:"
+ "fetchActivePrismCorrection()"
+ "fetchActivePrismCorrectionWithCompletionHandler:"
+ "fetchBoolProperty(name:)"
+ "fetchBoolPropertyWithName:completionHandler:"
+ "fetchComfortAdjustmentData(forUUID:inGroup:)"
+ "fetchComfortAdjustmentDataForUUID:inGroup:completionHandler:"
+ "fetchCompositorData()"
+ "fetchCompositorDataWithCompletionHandler:"
+ "fetchHealthRecords()"
+ "fetchHealthRecordsWithCompletionHandler:"
+ "fetchLensIntrinsics(forEnrollmentWithUUID:inGroup:nominal:)"
+ "fetchLensIntrinsicsForEnrollmentWithUUID:inGroup:nominal:completionHandler:"
+ "fetchOption(name:)"
+ "fetchOptionWithName:completionHandler:"
+ "fetchOptionsWithCompletionHandler:"
+ "fetchPrescriptionRecords(withTimeout:targetDeviceModel:)"
+ "fetchPrescriptionRecordsWithTimeout:targetDeviceModel:completionHandler:"
+ "fetchProperties()"
+ "fetchPropertiesWithCompletionHandler:"
+ "fetchSelectedEnrollment()"
+ "fetchSelectedEnrollmentWithCompletionHandler:"
+ "fetchSystemStatus(options:)"
+ "fetchSystemStatusWithOptions:completionHandler:"
+ "file_format_version"
+ "gazeEnrollmentCheckTimeout"
+ "generateAppClipCodePayload(version:lensType:odRX:osRX:age:colorCode:lensModel:secret:)"
+ "generateAppClipCodePayloadWithVersion:lensType:odRX:osRX:age:colorCode:lensModel:secret:completionHandler:"
+ "getCachedSystemPresenceState()"
+ "getCachedSystemPresenceStateWithCompletionHandler:"
+ "getCurrentCountryCode"
+ "getPrescriptionDetectionMode()"
+ "getPrescriptionDetectionModeWithCompletionHandler:"
+ "getPrescriptionDetectionStatus()"
+ "getPrescriptionDetectionStatusWithCompletionHandler:"
+ "hasInputRecovery"
+ "hasUserStatus"
+ "horizontal: %+6.2f (%s), vertical: %+6.2f (%s)"
+ "horizontalBase"
+ "initWithBool:"
+ "initWithDouble:"
+ "initWithHasInputRecovery:inputRecoveryReason:hasUserStatus:userStatusTitle:userStatusMessage:userStatusIcon:sessionDidStart:"
+ "initWithInt:"
+ "initWithInteger:"
+ "initWithLeftRx:rightRx:leftPrism:rightPrism:readerRange:acc:name:serialNumber:deviceType:source:revision:colorCode:issueDate:metadata:"
+ "initWithLensDetectionStatus:lensCalibrationStatus:lensPoseStatus:updateClipOnInfoStatus:rxUUID:"
+ "initWithSphere:cylinder:axis:add:vrAdd:"
+ "initWithSphere:cylinder:axis:addPower:vertexDistance:prism:farPupillaryDistance:nearPupillaryDistance:"
+ "initWithTimeInterval:"
+ "initWithUnsignedInt:"
+ "initWithVersion:lensType:left:right:lensColorCode:lensModel:secret:randomBits:"
+ "initWithVerticalAmount:verticalBase:horizontalAmount:horizontalBase:eye:"
+ "inputRecoveryReason"
+ "insertHealthRecord(withURL:fromHealthApp:deviceModel:description:)"
+ "insertHealthRecordWithURL:fromHealthApp:deviceModel:description:completionHandler:"
+ "intValue"
+ "integerForKey:"
+ "integerValue"
+ "internalNotificationsDisabled"
+ "isCompatibleLensModel(lensModel:)"
+ "isCompatibleLensModelWithLensModel:completionHandler:"
+ "isDefaulted"
+ "key != ((void*)0)"
+ "keyDetail"
+ "keyField"
+ "keyName"
+ "keyUUID"
+ "keyUnderlyingError"
+ "killLensAlgorithms()"
+ "killLensAlgorithmsWithCompletionHandler:"
+ "lastPullTime"
+ "lastPushTime"
+ "lastSelectedEnrollmentUUID"
+ "lastSyncedUser"
+ "left eye sphere: %@"
+ "leftEye: %@, rightEye: %@"
+ "leftPrism"
+ "leftRx"
+ "lensFinderMaxSize"
+ "lensFinderOnFailOnly"
+ "lensIntrinsics"
+ "lensModel"
+ "lensPoseAlgorithmDisabled"
+ "lensPoseCompletionTimeout"
+ "lensPoseRetryCount"
+ "lensPoseRetryDelay"
+ "lensPoseTimeout"
+ "lensPresenceMinSuccessesRequired"
+ "lensPresenceRetryDelay"
+ "lensPresenceRetryMax"
+ "lens_model"
+ "lenstray"
+ "loadDataStore(fromFileHandle:table:options:)"
+ "loadDataStoreFromFileHandle:table:options:completionHandler:"
+ "localDevice"
+ "objectForKey:"
+ "options->age >= 0"
+ "persistGuestModeStateOverride"
+ "prefs sync failed"
+ "prescriptionRecordFetcher"
+ "prescriptionState"
+ "prescriptionWithRightEyeSpecification:leftEyeSpecification:dateIssued:expirationDate:device:metadata:"
+ "presenceDetectionMode"
+ "printExecutionTime"
+ "prism"
+ "prismActivationOverrideLocation"
+ "prismCorrection"
+ "prismDiopterUnit"
+ "prism_rx != ((void*)0)"
+ "profileChangeObservers"
+ "quantityWithUnit:doubleValue:"
+ "reEnrollmentCanStartTimeout"
+ "reEnrollmentCliponPoseCompletionTimeout"
+ "reEnrollmentCliponWithSerializedTimeout"
+ "reEnrollmentReenrollTimeout"
+ "reEnrollmentSerializedImageTimeout"
+ "readDataToEndOfFile"
+ "readerRange"
+ "removeObjectForKey:"
+ "reprocessCurrentGaze()"
+ "reprocessCurrentGazeWithCompletionHandler:"
+ "resetAllOptions()"
+ "resetAllOptionsWithCompletionHandler:"
+ "resetOptions(names:)"
+ "resetOptionsWithNames:completionHandler:"
+ "resetUserCalibration()"
+ "resetUserCalibrationWithCompletionHandler:"
+ "revision"
+ "right eye sphere: %@"
+ "rightPrism"
+ "rightRx"
+ "runPrescriptionPose(inGroup:withMultiRX:doUpdate:)"
+ "runPrescriptionPoseInGroup:withMultiRX:doUpdate:completionHandler:"
+ "runPrescriptionPoseWithIntrinsics(_:rxuuid:)"
+ "runPrescriptionPoseWithIntrinsics:rxuuid:completionHandler:"
+ "saveObject:withCompletion:"
+ "scanEnrollment(timeout:replayURL:)"
+ "scanEnrollmentWithTimeout:replayURL:completionHandler:"
+ "selectedEnrollment"
+ "sessionDidStart"
+ "setAdd:"
+ "setBool:forKey:"
+ "setCachedSystemPresenceState(newState:)"
+ "setCachedSystemPresenceStateWithNewState:completionHandler:"
+ "setDouble:forKey:"
+ "setHasInputRecovery:"
+ "setHasUserStatus:"
+ "setInputRecoveryReason:"
+ "setInteger:forKey:"
+ "setLensModel:"
+ "setObject:forKey:"
+ "setOption(name:toValue:)"
+ "setOptionWithName:toValue:completionHandler:"
+ "setPrescriptionDetectionMode(to:)"
+ "setPrescriptionDetectionModeTo:completionHandler:"
+ "setPrescriptionDetectionStatus(to:)"
+ "setPrescriptionDetectionStatusTo:completionHandler:"
+ "setProperty(name:value:)"
+ "setPropertyWithName:value:completionHandler:"
+ "setSessionDidStart:"
+ "setSourceBundleIdentifier:"
+ "setTimeZone:"
+ "setUserStatusIcon:"
+ "setUserStatusMessage:"
+ "setUserStatusTitle:"
+ "skipLensPresenceCheck"
+ "source bundle ID of prescription to save: %s"
+ "sourceRevision"
+ "sourceRevision.source.bundleIdentifier: %s"
+ "standardUserDefaults"
+ "stringForKey:"
+ "stringFromDate:"
+ "stringValue"
+ "systemStatus"
+ "tableChangeObservers"
+ "timeIntervalValue"
+ "updateActivePrismCorrection(_:)"
+ "updateActivePrismCorrection:completionHandler:"
+ "updatePrescriptionPoseWithIntrinsics(_:rxuuid:)"
+ "updatePrescriptionPoseWithIntrinsics:rxuuid:completionHandler:"
+ "updatePrescriptionState(_:)"
+ "updatePrescriptionState:completionHandler:"
+ "userNotificationsDisabled"
+ "userSignOutSyncEnabled"
+ "userStatusIcon"
+ "userStatusMessage"
+ "userStatusTitle"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?<v@?@\"CRXCCompositorData\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CRXCContextSessionDonStatus\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CRXCEnrollmentRecord\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CRXCPrismCorrection\"@\"NSError\">16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?q@\"NSError\">20"
+ "v32@0:8@\"CRXCPrescriptionState\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CRXCPrismCorrection\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"CRXCOption\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?S@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"CRXCSystemStatus\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?B@\"NSError\">24"
+ "v32@0:8d16@?<v@?B@\"NSError\">24"
+ "v40@0:8@\"CRXCAppClipCodePayload\"16Q24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"CRXCOptionValue\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v40@0:8d16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8d16@\"NSURL\"24@?<v@?@\"CRXCEnrollmentData\"@\"NSError\">32"
+ "v40@0:8d16@24@?32"
+ "v40@0:8q16B24B28@?32"
+ "v40@0:8q16B24B28@?<v@?@\"NSError\">32"
+ "v44@0:8@\"NSString\"16q24B32@?<v@?@\"NSString\"@\"NSError\">36"
+ "v44@0:8@16q24B32@?36"
+ "v52@0:8@\"NSURL\"16B24@\"NSString\"28@\"NSString\"36@?<v@?@\"NSError\">44"
+ "v52@0:8@16B24@28@36@?44"
+ "v88@0:8Q16q24@\"CRXCEyePrescription\"32@\"CRXCEyePrescription\"40Q48Q56Q64@\"NSData\"72@?<v@?@\"NSData\"@\"NSError\">80"
+ "v88@0:8Q16q24@32@40Q48Q56Q64@72@?80"
+ "verticalBase"
+ "visionExecutionManager"
+ "vrx_find_matching_lenses"
+ "vrx_get_metadata_key"
+ "vrx_print_prism_rx"
+ "vrx_prism_rx_equal"
+ "xpcContext"
+ "xpcLensPose"
+ "xpcLensPresence"
+ "xpcLensReprocessing"
+ "yyyy-MM-dd HH:mm:ss.SSS zzz"
- "%02lu"
- "%02lu:"
- "%@<%p>"
- "%@<%p> %@"
- "%lu"
- "%lu:"
- "%s - sn: %*s, seq#: %*s, "
- "%s @%d: <%{public}@> async enter"
- "%s @%d: <%{public}@> async leave"
- "%s @%d: <%{public}@> sync enter"
- "%s @%d: <%{public}@> sync leave"
- "-"
- "-[CRXUDispatchQueue afterDelay:dispatchAsync:]_block_invoke"
- "-[CRXUDispatchQueue dispatchAsync:]_block_invoke"
- "-[CRXUDispatchQueue dispatchSync:]_block_invoke"
- ".%03lu"
- "<main>"
- "@\"CRXUDispatchQueue\""
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@24@0:8Q16"
- "@28@0:8@16I24"
- "@32@0:8@16@24"
- "@36@0:8f16f20Q24f32"
- "@68@0:8Q16q24@32@40Q48@56I64"
- "AddVR clamped successfully!"
- "B24@0:8d16"
- "CRXUDispatchGroup"
- "CRXUDispatchQueue"
- "CRXUDispatchSemaphore"
- "CRXUFormatters"
- "CXRCExecutionManager"
- "CorePrescription.CorePrescriptionServiceError"
- "CorePrescription.DataManagerError"
- "CorePrescription.DataStoreError"
- "CorePrescriptionService.InternalDataStoreObserver"
- "NO"
- "Swift/Dictionary.swift"
- "T@\"CRXUDispatchQueue\",R,N"
- "T@\"NSObject<OS_dispatch_group>\",R,N,V_group"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "TB,N,V_tracingEnabled"
- "YES"
- "_TtC23CorePrescriptionService8Settings"
- "_TtC23CorePrescriptionServiceP33_721C45E69E13589B716B3DB30077E60925InternalDataStoreObserver"
- "_TtCC23CorePrescriptionService20CXRCExecutionManagerP33_D980D2326E09A9A9FB863F29FCC1CBD212AnyExecution"
- "_TtCC23CorePrescriptionService20CXRCExecutionManagerP33_D980D2326E09A9A9FB863F29FCC1CBD215AnyContinuation"
- "_group"
- "_sem"
- "_tracingEnabled"
- "activatePrism()"
- "afterDelay:dispatchAsync:"
- "appendFormat:"
- "appendString:"
- "assert"
- "boolAsString:"
- "checkLensPresence()"
- "checkLensPresenceWithCompletionHandler:"
- "com.apple.CorePrescription.CommonUtils"
- "completion"
- "concurrentQueueWithName:"
- "concurrentQueueWithName:qos:"
- "dispatchAsync:"
- "dispatchBarrierAsync:"
- "dispatchBarrierSync:"
- "dispatchQueueWithQueue:"
- "dispatchSync:"
- "encodeAppClipCodePayload(_:)"
- "encodeAppClipCodePayload:completionHandler:"
- "enter"
- "fetchPrescriptionRecords(withTimeout:)"
- "fetchPrescriptionRecordsWithTimeout:completionHandler:"
- "fetchSystemStatus()"
- "fetchSystemStatusWithCompletionHandler:"
- "fetchUserInfo()"
- "generateAppClipCodePayload(version:lensType:odRX:osRX:colorCode:secret:)"
- "generateAppClipCodePayloadWithVersion:lensType:odRX:osRX:colorCode:secret:completionHandler:"
- "getPrismActivationStatus()"
- "getPrismActivationStatusWithCompletionHandler:"
- "group"
- "initWithName:"
- "initWithQueue:name:"
- "initWithSphere:cylinder:axis:vrAdd:"
- "initWithValue:"
- "initWithVersion:lensType:left:right:lensColorCode:secret:randomBits:"
- "leave"
- "main"
- "notifyOnQueue:withBlock:"
- "onQueue:dispatchAsync:"
- "serialQueueWithName:"
- "serialQueueWithName:qos:"
- "setTracingEnabled:"
- "signal"
- "stringWithCString:encoding:"
- "stringWithString:"
- "timeIntervalAsString:"
- "tracingEnabled"
- "v24@0:8@?<v@?@\"CRXCSystemStatus\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSString\"@\"NSError\">16"
- "v32@0:8@\"CRXCAppClipCodePayload\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8d16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v72@0:8Q16q24@\"CRXCEyePrescription\"32@\"CRXCEyePrescription\"40Q48@\"NSData\"56@?<v@?@\"NSData\"@\"NSError\">64"
- "v72@0:8Q16q24@32@40Q48@56@?64"
- "vrx_find_lenses_ex"
- "wait"
- "waitFor:"

```
