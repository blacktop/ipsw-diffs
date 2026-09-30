## SoftwareUpdateUIBridge

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIBridge.framework/SoftwareUpdateUIBridge`

```diff

-772.0.10.0.0
-  __TEXT.__text: 0x16db8
-  __TEXT.__objc_methlist: 0xa8c
-  __TEXT.__cstring: 0x1db7
-  __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__oslogstring: 0x5d0
-  __TEXT.__swift5_typeref: 0x1c9
-  __TEXT.__const: 0x420
-  __TEXT.__swift5_capture: 0x290
+772.0.20.0.0
+  __TEXT.__text: 0x33240
+  __TEXT.__objc_methlist: 0x1634
+  __TEXT.__const: 0x480
+  __TEXT.__gcc_except_tab: 0xd80
+  __TEXT.__cstring: 0x2ab7
+  __TEXT.__oslogstring: 0x196c
+  __TEXT.__swift5_typeref: 0x1ed
+  __TEXT.__swift5_capture: 0x334
   __TEXT.__constg_swiftt: 0xf0
-  __TEXT.__swift5_reflstr: 0xe5
-  __TEXT.__swift5_fieldmd: 0xa8
+  __TEXT.__swift5_reflstr: 0xf5
+  __TEXT.__swift5_fieldmd: 0xb4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x10

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0x4
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x508
+  __TEXT.__unwind_info: 0x890
   __TEXT.__eh_frame: 0x18c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1398
-  __DATA_CONST.__objc_classlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__const: 0x37c0
+  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x528
+  __DATA_CONST.__objc_selrefs: 0xb68
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__got: 0x240
-  __AUTH_CONST.__const: 0x690
-  __AUTH_CONST.__cfstring: 0x1200
-  __AUTH_CONST.__objc_const: 0x2a98
+  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__got: 0x468
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0x1520
+  __AUTH_CONST.__objc_const: 0x50e0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x548
-  __AUTH.__objc_data: 0x828
-  __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x94
-  __DATA.__data: 0x4b0
+  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH.__objc_data: 0xab0
+  __AUTH.__data: 0x60
+  __DATA.__objc_ivar: 0x128
+  __DATA.__data: 0x840
   __DATA.__bss: 0x490
-  __DATA.__common: 0x38
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/Seeding.framework/Seeding
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 473
-  Symbols:   769
-  CStrings:  248
+  Functions: 714
+  Symbols:   1415
+  CStrings:  381
 
Symbols:
+ +[SUUIBridgeDescriptor supportsSecureCoding]
+ +[SUUIBridgeDocumentation supportsSecureCoding]
+ +[SUUIBridgeDownload supportsSecureCoding]
+ +[SUUIBridgeDownloadProgress supportsSecureCoding]
+ -[SUUIBridgeDescriptor .cxx_destruct]
+ -[SUUIBridgeDescriptor audienceType]
+ -[SUUIBridgeDescriptor copyWithZone:]
+ -[SUUIBridgeDescriptor description]
+ -[SUUIBridgeDescriptor documentation]
+ -[SUUIBridgeDescriptor downloadSize]
+ -[SUUIBridgeDescriptor encodeWithCoder:]
+ -[SUUIBridgeDescriptor fullUpdateName]
+ -[SUUIBridgeDescriptor hash]
+ -[SUUIBridgeDescriptor initWithCoder:]
+ -[SUUIBridgeDescriptor initWithDescriptor:]
+ -[SUUIBridgeDescriptor init]
+ -[SUUIBridgeDescriptor installationSize]
+ -[SUUIBridgeDescriptor isDownloadable]
+ -[SUUIBridgeDescriptor isEqual:]
+ -[SUUIBridgeDescriptor isSplatUpdate]
+ -[SUUIBridgeDescriptor isSplomboUpdate]
+ -[SUUIBridgeDescriptor mandatoryUpdateEligible]
+ -[SUUIBridgeDescriptor mandatoryUpdateOptional]
+ -[SUUIBridgeDescriptor mandatoryUpdateRestrictedToOutOfTheBox]
+ -[SUUIBridgeDescriptor mandatoryUpdateVersionMax]
+ -[SUUIBridgeDescriptor mandatoryUpdateVersionMin]
+ -[SUUIBridgeDescriptor preparationSize]
+ -[SUUIBridgeDescriptor productBuildVersion]
+ -[SUUIBridgeDescriptor productSystemName]
+ -[SUUIBridgeDescriptor productVersionExtra]
+ -[SUUIBridgeDescriptor productVersion]
+ -[SUUIBridgeDescriptor promoteAlternateUpdate]
+ -[SUUIBridgeDescriptor publisher]
+ -[SUUIBridgeDescriptor releaseDate]
+ -[SUUIBridgeDescriptor totalRequiredFreeSpace]
+ -[SUUIBridgeDescriptor underlyingDescriptor]
+ -[SUUIBridgeDescriptor updateName]
+ -[SUUIBridgeDescriptor updateType]
+ -[SUUIBridgeDescriptor upgradeVersionType]
+ -[SUUIBridgeDocumentation .cxx_destruct]
+ -[SUUIBridgeDocumentation copyWithZone:]
+ -[SUUIBridgeDocumentation encodeWithCoder:]
+ -[SUUIBridgeDocumentation hash]
+ -[SUUIBridgeDocumentation initWithCoder:]
+ -[SUUIBridgeDocumentation initWithDocumentation:]
+ -[SUUIBridgeDocumentation init]
+ -[SUUIBridgeDocumentation isEqual:]
+ -[SUUIBridgeDocumentation licenseAgreement]
+ -[SUUIBridgeDocumentation mandatoryUpdateBodyString]
+ -[SUUIBridgeDocumentation releaseNotesSummary]
+ -[SUUIBridgeDocumentation releaseNotes]
+ -[SUUIBridgeDocumentation setUnderlyingDocumentation:]
+ -[SUUIBridgeDocumentation underlyingDocumentation]
+ -[SUUIBridgeDocumentation updateIcon]
+ -[SUUIBridgeDownload .cxx_destruct]
+ -[SUUIBridgeDownload copyWithZone:]
+ -[SUUIBridgeDownload description]
+ -[SUUIBridgeDownload descriptor]
+ -[SUUIBridgeDownload encodeWithCoder:]
+ -[SUUIBridgeDownload hash]
+ -[SUUIBridgeDownload initWithCoder:]
+ -[SUUIBridgeDownload initWithDownload:]
+ -[SUUIBridgeDownload init]
+ -[SUUIBridgeDownload isAutoDownload]
+ -[SUUIBridgeDownload isEqual:]
+ -[SUUIBridgeDownload isUninitialized]
+ -[SUUIBridgeDownload policy]
+ -[SUUIBridgeDownload progress]
+ -[SUUIBridgeDownload underlyingDownload]
+ -[SUUIBridgeDownloadProgress .cxx_destruct]
+ -[SUUIBridgeDownloadProgress copyWithZone:]
+ -[SUUIBridgeDownloadProgress encodeWithCoder:]
+ -[SUUIBridgeDownloadProgress hash]
+ -[SUUIBridgeDownloadProgress initWithCoder:]
+ -[SUUIBridgeDownloadProgress initWithProgress:]
+ -[SUUIBridgeDownloadProgress init]
+ -[SUUIBridgeDownloadProgress isDone]
+ -[SUUIBridgeDownloadProgress isEqual:]
+ -[SUUIBridgeDownloadProgress isStalled]
+ -[SUUIBridgeDownloadProgress isValidTimeRemaining:]
+ -[SUUIBridgeDownloadProgress normalizedPercentComplete]
+ -[SUUIBridgeDownloadProgress percentComplete]
+ -[SUUIBridgeDownloadProgress phase]
+ -[SUUIBridgeDownloadProgress timeRemaining]
+ -[SUUIBridgeDownloadProgress underlyingProgress]
+ -[SUUIBridgeManagerClient .cxx_destruct]
+ -[SUUIBridgeManagerClient _broadcastWithBlock:]
+ -[SUUIBridgeManagerClient _removeObserverForToken:]
+ -[SUUIBridgeManagerClient addObserver:queue:]
+ -[SUUIBridgeManagerClient currentDownloadForDescriptor:completion:]
+ -[SUUIBridgeManagerClient dealloc]
+ -[SUUIBridgeManagerClient deviceType]
+ -[SUUIBridgeManagerClient initWithDeviceType:]
+ -[SUUIBridgeManagerClient installUpdate:completion:]
+ -[SUUIBridgeManagerClient manager:didChangeProgressOnDownload:]
+ -[SUUIBridgeManagerClient manager:didFailDownload:withError:]
+ -[SUUIBridgeManagerClient manager:didFailInstallation:withError:]
+ -[SUUIBridgeManagerClient manager:didFinishInstallation:]
+ -[SUUIBridgeManagerClient manager:installationAwaitingUserInteraction:]
+ -[SUUIBridgeManagerClient manager:installationOfUpdate:willProceed:waitingForAdmissionControl:]
+ -[SUUIBridgeManagerClient manager:scanRequestDidLocateUpdate:error:]
+ -[SUUIBridgeManagerClient manager:userInstallRequestTypeDidChange:]
+ -[SUUIBridgeManagerClient managerState:]
+ -[SUUIBridgeManagerClient managerUserDidAcceptTermsAndConditionsForUpdate:]
+ -[SUUIBridgeManagerClient manager]
+ -[SUUIBridgeManagerClient purgeUpdate:completion:]
+ -[SUUIBridgeManagerClient scanForUpdatesWithCompletion:]
+ -[SUUIBridgeManagerClient setUserInstallRequestType:forUpdate:completion:]
+ -[SUUIBridgeManagerClient startDownload:completion:]
+ -[SUUIBridgeManagerClient userDidAcceptTermsAndConditionsForUpdate:completion:]
+ -[SUUIBridgeManagerClientObservationToken .cxx_destruct]
+ -[SUUIBridgeManagerClientObservationToken _initWithClient:]
+ -[SUUIBridgeManagerClientObservationToken dealloc]
+ -[SUUIBridgeManagerClientObservationToken description]
+ -[SUUIBridgeManagerClientObservationToken invalidate]
+ -[SUUIBridgeManagerClientObservationToken isInvalidated]
+ -[SUUIBridgeManagerClientObserverEntry .cxx_destruct]
+ -[SUUIBridgeManagerClientObserverEntry callbackQueue]
+ -[SUUIBridgeManagerClientObserverEntry observer]
+ -[SUUIBridgeManagerClientObserverEntry setCallbackQueue:]
+ -[SUUIBridgeManagerClientObserverEntry setObserver:]
+ -[SUUIBridgeManagerClientObserverEntry setToken:]
+ -[SUUIBridgeManagerClientObserverEntry token]
+ -[SUUIBridgeScanOperation _classifyScanError:withDescriptor:intoParam:]
+ -[SUUIBridgeScanOperation _companionConnectivityTimeoutError]
+ -[SUUIBridgeScanOperation _isScanPhaseConnectivityError:]
+ -[SUUIBridgeScanOperation _shouldSkipManagerStateQuery:]
+ -[SUUIBridgeScanOperation action_CheckForAvailableUpdate:error:]
+ -[SUUIBridgeScanOperation action_ObserveConcurrentQueries:error:]
+ -[SUUIBridgeScanOperation action_QueryCurrentDownload:error:]
+ -[SUUIBridgeScanOperation action_QueryFullScanMetadata:error:]
+ -[SUUIBridgeScanOperation action_QueryManagerState:error:]
+ -[SUUIBridgeScanOperation action_ReportScanCanceled:error:]
+ -[SUUIBridgeScanOperation action_ReportScanOutcome:error:]
+ -[SUUIBridgeScanOperation bridgeClient]
+ -[SUUIBridgeScanOperation checkForBetaPrograms:withReplyHandler:]
+ -[SUUIBridgeScanOperation initWithIdentifier:environment:usingBridgeClient:andBetaManager:withCompletionQueue:]
+ -[SUUIBridgeScanOperation scheduleConcurrentActionWithSelector:eventInfo:]
+ -[SUUIBridgeScanOperation seedingBetaManager]
+ -[SUUIBridgeScanOperation selfRetain]
+ -[SUUIBridgeScanOperation setSelfRetain:]
+ -[SUUIBridgeScanOperation shouldSupportBetaUpdatesManagement]
+ -[SUUIBridgeScanOperationFullScanResults initFromScanParam:withIdentifier:]
+ -[SUUIBridgeScanOperationParam .cxx_destruct]
+ -[SUUIBridgeScanOperationParam betaPrograms]
+ -[SUUIBridgeScanOperationParam currentDownload]
+ -[SUUIBridgeScanOperationParam emptyScanResults]
+ -[SUUIBridgeScanOperationParam enrolledBetaProgram]
+ -[SUUIBridgeScanOperationParam initWithError:]
+ -[SUUIBridgeScanOperationParam initWithFullScanContext:]
+ -[SUUIBridgeScanOperationParam initWithPreferredDescriptor:andRefreshContext:]
+ -[SUUIBridgeScanOperationParam isAutoUpdateScheduled]
+ -[SUUIBridgeScanOperationParam isUpdateReadyForInstallation]
+ -[SUUIBridgeScanOperationParam managerState]
+ -[SUUIBridgeScanOperationParam operationError]
+ -[SUUIBridgeScanOperationParam preferredDescriptor]
+ -[SUUIBridgeScanOperationParam preferredUpdateDownloadError]
+ -[SUUIBridgeScanOperationParam preferredUpdateDownloadable]
+ -[SUUIBridgeScanOperationParam scanError]
+ -[SUUIBridgeScanOperationParam setAutoUpdateScheduled:]
+ -[SUUIBridgeScanOperationParam setBetaPrograms:]
+ -[SUUIBridgeScanOperationParam setCurrentDownload:]
+ -[SUUIBridgeScanOperationParam setEmptyScanResults:]
+ -[SUUIBridgeScanOperationParam setEnrolledBetaProgram:]
+ -[SUUIBridgeScanOperationParam setIsUpdateReadyForInstallation:]
+ -[SUUIBridgeScanOperationParam setManagerState:]
+ -[SUUIBridgeScanOperationParam setOperationError:]
+ -[SUUIBridgeScanOperationParam setPreferredDescriptor:]
+ -[SUUIBridgeScanOperationParam setPreferredUpdateDownloadError:]
+ -[SUUIBridgeScanOperationParam setPreferredUpdateDownloadable:]
+ -[SUUIBridgeScanOperationParam setScanError:]
+ -[SUUIBridgeScanOperationResults initFromScanParam:withIdentifier:]
+ -[SUUIBridgeStatefulError bodyForAdmissionControlDenial:]
+ -[SUUIBridgeStatefulError companionUnreachable]
+ -[SUUIBridgeStatefulError headingForAdmissionControlDenial:]
+ -[SUUIBridgeStatefulUIManager bridgeClient]
+ -[SUUIBridgeStatefulUIManager initWithEnvironment:forPairedDevice:bridgeClient:identifier:]
+ -[SUUIBridgeStatefulUIManager pairedDevice]
+ GCC_except_table1
+ GCC_except_table11
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table15
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table55
+ GCC_except_table6
+ GCC_except_table61
+ GCC_except_table7
+ GCC_except_table8
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_SEED_STAGING_EXT_PRERELEASE
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_SDDevice
+ _OBJC_CLASS_$_SUBDescriptor
+ _OBJC_CLASS_$_SUBDocumentation
+ _OBJC_CLASS_$_SUBDownload
+ _OBJC_CLASS_$_SUBManager
+ _OBJC_CLASS_$_SUBProgress
+ _OBJC_CLASS_$_SUUIBridgeDescriptor
+ _OBJC_CLASS_$_SUUIBridgeDocumentation
+ _OBJC_CLASS_$_SUUIBridgeDownload
+ _OBJC_CLASS_$_SUUIBridgeDownloadProgress
+ _OBJC_CLASS_$_SUUIBridgeManagerClient
+ _OBJC_CLASS_$_SUUIBridgeManagerClientObservationToken
+ _OBJC_CLASS_$_SUUIBridgeManagerClientObserverEntry
+ _OBJC_CLASS_$_SUUIBridgeScanOperationParam
+ _OBJC_CLASS_$_SUUIObjectDescriptionFormatter
+ _OBJC_CLASS_$_SUUIRetryConfiguration
+ _OBJC_IVAR_$_SUUIBridgeDescriptor._bridgeDocumentation
+ _OBJC_IVAR_$_SUUIBridgeDescriptor._underlyingDescriptor
+ _OBJC_IVAR_$_SUUIBridgeDocumentation._underlyingDocumentation
+ _OBJC_IVAR_$_SUUIBridgeDownload._bridgeDescriptor
+ _OBJC_IVAR_$_SUUIBridgeDownload._bridgeDownloadProgress
+ _OBJC_IVAR_$_SUUIBridgeDownload._underlyingDownload
+ _OBJC_IVAR_$_SUUIBridgeDownloadProgress._underlyingProgress
+ _OBJC_IVAR_$_SUUIBridgeManagerClient._deviceType
+ _OBJC_IVAR_$_SUUIBridgeManagerClient._downloadsByDescriptor
+ _OBJC_IVAR_$_SUUIBridgeManagerClient._lock
+ _OBJC_IVAR_$_SUUIBridgeManagerClient._manager
+ _OBJC_IVAR_$_SUUIBridgeManagerClient._observers
+ _OBJC_IVAR_$_SUUIBridgeManagerClient._pendingDownloadCompletions
+ _OBJC_IVAR_$_SUUIBridgeManagerClient._pendingInstallCompletions
+ _OBJC_IVAR_$_SUUIBridgeManagerClient._pendingScanCompletions
+ _OBJC_IVAR_$_SUUIBridgeManagerClientObservationToken._client
+ _OBJC_IVAR_$_SUUIBridgeManagerClientObservationToken._invalidated
+ _OBJC_IVAR_$_SUUIBridgeManagerClientObserverEntry._callbackQueue
+ _OBJC_IVAR_$_SUUIBridgeManagerClientObserverEntry._observer
+ _OBJC_IVAR_$_SUUIBridgeManagerClientObserverEntry._token
+ _OBJC_IVAR_$_SUUIBridgeScanOperation._bridgeClient
+ _OBJC_IVAR_$_SUUIBridgeScanOperation._seedingBetaManager
+ _OBJC_IVAR_$_SUUIBridgeScanOperation._selfRetain
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._autoUpdateScheduled
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._betaPrograms
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._currentDownload
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._emptyScanResults
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._enrolledBetaProgram
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._isUpdateReadyForInstallation
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._managerState
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._operationError
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._preferredDescriptor
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._preferredUpdateDownloadError
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._preferredUpdateDownloadable
+ _OBJC_IVAR_$_SUUIBridgeScanOperationParam._scanError
+ _OBJC_IVAR_$_SUUIBridgeStatefulUIManager._bridgeClient
+ _OBJC_IVAR_$_SUUIBridgeStatefulUIManager._pairedDevice
+ _OBJC_METACLASS_$_SUUIBridgeDescriptor
+ _OBJC_METACLASS_$_SUUIBridgeDocumentation
+ _OBJC_METACLASS_$_SUUIBridgeDownload
+ _OBJC_METACLASS_$_SUUIBridgeDownloadProgress
+ _OBJC_METACLASS_$_SUUIBridgeManagerClient
+ _OBJC_METACLASS_$_SUUIBridgeManagerClientObservationToken
+ _OBJC_METACLASS_$_SUUIBridgeManagerClientObserverEntry
+ _OBJC_METACLASS_$_SUUIBridgeScanOperationParam
+ _PDRDevicePropertyKeyIsInternalInstall
+ _PDRDevicePropertyKeyMarketingProductName
+ _PDRDevicePropertyKeyName
+ _PDRDevicePropertyKeySystemVersion
+ _SUBErrorDomain
+ _SUBErrorUserInfoChargerConnected
+ _SUBErrorUserInfoDenialReasons
+ _SUBErrorUserInfoMinNeededBatteryLevelWithChargerForApply
+ _SUBManagerStateIsUpdateReadyForInstallation
+ _SUBMessageRequiredDiskSpaceKey
+ _SUBPhaseDownloading
+ _SUBPhasePreparingUpdate
+ _SUBPhaseStalled
+ _SUUIBridgeManagerClientDeviceTypeToString
+ _SoftwareUpdateUIBridgeVersionNumber
+ _SoftwareUpdateUIBridgeVersionString
+ __Block_object_dispose
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_SUUIBridgeDescriptor
+ __OBJC_$_CLASS_METHODS_SUUIBridgeDocumentation
+ __OBJC_$_CLASS_METHODS_SUUIBridgeDownload
+ __OBJC_$_CLASS_METHODS_SUUIBridgeDownloadProgress
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_SUUIBridgeDescriptor
+ __OBJC_$_CLASS_PROP_LIST_SUUIBridgeDocumentation
+ __OBJC_$_CLASS_PROP_LIST_SUUIBridgeDownload
+ __OBJC_$_CLASS_PROP_LIST_SUUIBridgeDownloadProgress
+ __OBJC_$_INSTANCE_METHODS_SUUIBridgeDescriptor
+ __OBJC_$_INSTANCE_METHODS_SUUIBridgeDocumentation
+ __OBJC_$_INSTANCE_METHODS_SUUIBridgeDownload
+ __OBJC_$_INSTANCE_METHODS_SUUIBridgeDownloadProgress
+ __OBJC_$_INSTANCE_METHODS_SUUIBridgeManagerClient
+ __OBJC_$_INSTANCE_METHODS_SUUIBridgeManagerClientObservationToken
+ __OBJC_$_INSTANCE_METHODS_SUUIBridgeManagerClientObserverEntry
+ __OBJC_$_INSTANCE_METHODS_SUUIBridgeScanOperationParam
+ __OBJC_$_INSTANCE_VARIABLES_SUUIBridgeDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_SUUIBridgeDocumentation
+ __OBJC_$_INSTANCE_VARIABLES_SUUIBridgeDownload
+ __OBJC_$_INSTANCE_VARIABLES_SUUIBridgeDownloadProgress
+ __OBJC_$_INSTANCE_VARIABLES_SUUIBridgeManagerClient
+ __OBJC_$_INSTANCE_VARIABLES_SUUIBridgeManagerClientObservationToken
+ __OBJC_$_INSTANCE_VARIABLES_SUUIBridgeManagerClientObserverEntry
+ __OBJC_$_INSTANCE_VARIABLES_SUUIBridgeScanOperationParam
+ __OBJC_$_PROP_LIST_SUUIBridgeDescriptor
+ __OBJC_$_PROP_LIST_SUUIBridgeDocumentation
+ __OBJC_$_PROP_LIST_SUUIBridgeDownload
+ __OBJC_$_PROP_LIST_SUUIBridgeDownloadProgress
+ __OBJC_$_PROP_LIST_SUUIBridgeManagerClient
+ __OBJC_$_PROP_LIST_SUUIBridgeManagerClientObservationToken
+ __OBJC_$_PROP_LIST_SUUIBridgeManagerClientObserverEntry
+ __OBJC_$_PROP_LIST_SUUIBridgeScanOperationParam
+ __OBJC_$_PROP_LIST_SUUIDescriptor
+ __OBJC_$_PROP_LIST_SUUIDocumentation
+ __OBJC_$_PROP_LIST_SUUIDownload
+ __OBJC_$_PROP_LIST_SUUIDownloadProgress
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SUBManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUUIDescriptor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUUIDocumentation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUUIDownload
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUUIDownloadProgress
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUBManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUUIDescriptor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUUIDocumentation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUUIDownload
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUUIDownloadProgress
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_SUBManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_SUUIDescriptor
+ __OBJC_$_PROTOCOL_REFS_SUUIDocumentation
+ __OBJC_$_PROTOCOL_REFS_SUUIDownload
+ __OBJC_$_PROTOCOL_REFS_SUUIDownloadProgress
+ __OBJC_CLASS_PROTOCOLS_$_SUUIBridgeDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_SUUIBridgeDocumentation
+ __OBJC_CLASS_PROTOCOLS_$_SUUIBridgeDownload
+ __OBJC_CLASS_PROTOCOLS_$_SUUIBridgeDownloadProgress
+ __OBJC_CLASS_PROTOCOLS_$_SUUIBridgeManagerClient
+ __OBJC_CLASS_RO_$_SUUIBridgeDescriptor
+ __OBJC_CLASS_RO_$_SUUIBridgeDocumentation
+ __OBJC_CLASS_RO_$_SUUIBridgeDownload
+ __OBJC_CLASS_RO_$_SUUIBridgeDownloadProgress
+ __OBJC_CLASS_RO_$_SUUIBridgeManagerClient
+ __OBJC_CLASS_RO_$_SUUIBridgeManagerClientObservationToken
+ __OBJC_CLASS_RO_$_SUUIBridgeManagerClientObserverEntry
+ __OBJC_CLASS_RO_$_SUUIBridgeScanOperationParam
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_SUBManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SUUIDescriptor
+ __OBJC_LABEL_PROTOCOL_$_SUUIDocumentation
+ __OBJC_LABEL_PROTOCOL_$_SUUIDownload
+ __OBJC_LABEL_PROTOCOL_$_SUUIDownloadProgress
+ __OBJC_METACLASS_RO_$_SUUIBridgeDescriptor
+ __OBJC_METACLASS_RO_$_SUUIBridgeDocumentation
+ __OBJC_METACLASS_RO_$_SUUIBridgeDownload
+ __OBJC_METACLASS_RO_$_SUUIBridgeDownloadProgress
+ __OBJC_METACLASS_RO_$_SUUIBridgeManagerClient
+ __OBJC_METACLASS_RO_$_SUUIBridgeManagerClientObservationToken
+ __OBJC_METACLASS_RO_$_SUUIBridgeManagerClientObserverEntry
+ __OBJC_METACLASS_RO_$_SUUIBridgeScanOperationParam
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_SUBManagerDelegate
+ __OBJC_PROTOCOL_$_SUUIDescriptor
+ __OBJC_PROTOCOL_$_SUUIDocumentation
+ __OBJC_PROTOCOL_$_SUUIDownload
+ __OBJC_PROTOCOL_$_SUUIDownloadProgress
+ __SUUIActivityCleanup
+ ___44-[SUUIBridgeScanOperation invalidateMachine]_block_invoke
+ ___46-[SUUIBridgeManagerClient initWithDeviceType:]_block_invoke
+ ___47-[SUUIBridgeManagerClient _broadcastWithBlock:]_block_invoke
+ ___57-[SUUIBridgeManagerClient manager:didFinishInstallation:]_block_invoke
+ ___58-[SUUIBridgeScanOperation action_QueryManagerState:error:]_block_invoke
+ ___58-[SUUIBridgeScanOperation action_ReportScanOutcome:error:]_block_invoke
+ ___59-[SUUIBridgeScanOperation action_ReportScanCanceled:error:]_block_invoke
+ ___61-[SUUIBridgeManagerClient manager:didFailDownload:withError:]_block_invoke
+ ___61-[SUUIBridgeScanOperation action_QueryCurrentDownload:error:]_block_invoke
+ ___63-[SUUIBridgeManagerClient manager:didChangeProgressOnDownload:]_block_invoke
+ ___64-[SUUIBridgeScanOperation action_CheckForAvailableUpdate:error:]_block_invoke
+ ___65-[SUUIBridgeManagerClient manager:didFailInstallation:withError:]_block_invoke
+ ___65-[SUUIBridgeScanOperation action_ObserveConcurrentQueries:error:]_block_invoke
+ ___65-[SUUIBridgeScanOperation checkForBetaPrograms:withReplyHandler:]_block_invoke
+ ___67-[SUUIBridgeManagerClient manager:userInstallRequestTypeDidChange:]_block_invoke
+ ___68-[SUUIBridgeManagerClient manager:scanRequestDidLocateUpdate:error:]_block_invoke
+ ___71-[SUUIBridgeManagerClient manager:installationAwaitingUserInteraction:]_block_invoke
+ ___74-[SUUIBridgeManagerClient setUserInstallRequestType:forUpdate:completion:]_block_invoke
+ ___74-[SUUIBridgeScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke
+ ___75-[SUUIBridgeManagerClient managerUserDidAcceptTermsAndConditionsForUpdate:]_block_invoke
+ ___95-[SUUIBridgeManagerClient manager:installationOfUpdate:willProceed:waitingForAdmissionControl:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e38_v32?0q8"SUBDescriptor"16"NSError"24l
+ ___block_descriptor_40_e8_32bs_e20_v24?0"NSError"8q16ls32l8
+ ___block_descriptor_40_e8_32s_e30_v16?0"<SUBManagerDelegate>"8ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e30_v16?0"<SUBManagerDelegate>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e30_v16?0"<SUBManagerDelegate>"8ls32l8
+ ___block_descriptor_50_e8_32s40s_e30_v16?0"<SUBManagerDelegate>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e30_v16?0"<SUBManagerDelegate>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e23_v16?0"SDBetaProgram"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40r48w_e21_v16?0"SUBDownload"8lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40s48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40bs48w_e17_v16?0"NSArray"8lw48l8s40l8s32l8
+ ___block_descriptor_72_e8_32s40bs48w_e20_v24?0"NSArray"8q16lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40r48r56w_e35_v24?0"SUBDescriptor"8"NSError"16lw56l8r40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40r48r56w_e38_v32?0q8"SUBDescriptor"16"NSError"24lw56l8r40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40r48r56w_e5_v8?0lw56l8r40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_literal_global
+ ___os_log_helper_16_2_2_8_32_8_0
+ ___os_log_helper_16_2_2_8_66_8_66
+ ___os_log_helper_16_2_3_8_32_8_0_8_66
+ ___os_log_helper_16_2_3_8_32_8_66_8_66
+ ___os_log_helper_16_2_4_8_32_8_66_4_0_4_0
+ ___os_log_helper_16_2_4_8_32_8_66_8_66_8_0
+ ___os_log_helper_16_2_4_8_32_8_66_8_66_8_66
+ ___os_log_helper_16_2_5_8_32_8_66_8_66_8_0_8_66
+ ___os_log_helper_16_2_5_8_32_8_66_8_66_8_34_8_66
+ ___os_log_helper_16_2_5_8_32_8_66_8_66_8_66_8_66
+ ___os_log_helper_16_2_6_8_32_8_66_8_66_8_0_8_66_8_66
+ __os_feature_enabled_impl
+ __os_log_debug_impl
+ __suui_precondition_failure_with_format
+ _dispatch_after
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _dispatch_time
+ _kDenialReasonLowBattery
+ _kSUCoreActionKey
+ _kSUUIStatefulErrorTokenRequiredBatteryLevel
+ _kSUUIStatefulErrorTokenRequiredFreeDiskSpace
+ _kSU_A_CheckForAvailableUpdate
+ _kSU_A_ObserveConcurrentQueries
+ _kSU_A_QueryCurrentDownload
+ _kSU_A_QueryFullScanMetadata
+ _kSU_A_QueryManagerState
+ _kSU_A_ReportScanOutcome
+ _kSU_E_AllConcurrentActionsFinished
+ _kSU_E_CancelScan
+ _kSU_E_CheckForAvailableUpdate
+ _kSU_E_CheckingForUpdatesFailed
+ _kSU_E_ConcurrentActionFailed
+ _kSU_E_NoUpdateAvailable
+ _kSU_E_PerformFullScan
+ _kSU_E_QueryCurrentDownloadFailed
+ _kSU_E_QueryCurrentDownloadSuccess
+ _kSU_E_QueryManagerStateFailed
+ _kSU_E_QueryManagerStateSuccess
+ _kSU_E_RefreshScanResults
+ _kSU_E_UpdatesAvailable
+ _kSU_S_CheckingForAvailableUpdate
+ _kSU_S_ObservingConcurrentQueries
+ _kSU_S_QueryingCurrentDownload
+ _kSU_S_QueryingManagerState
+ _memset
+ _objc_enumerationMutation
+ _objc_msgSend$_broadcastWithBlock:
+ _objc_msgSend$_classifyScanError:withDescriptor:intoParam:
+ _objc_msgSend$_companionConnectivityTimeoutError
+ _objc_msgSend$_initWithClient:
+ _objc_msgSend$_isScanPhaseConnectivityError:
+ _objc_msgSend$_removeObserverForToken:
+ _objc_msgSend$_shouldSkipManagerStateQuery:
+ _objc_msgSend$action_CheckForAvailableUpdate:error:
+ _objc_msgSend$action_ObserveConcurrentQueries:error:
+ _objc_msgSend$action_QueryCurrentDownload:error:
+ _objc_msgSend$action_QueryFullScanMetadata:error:
+ _objc_msgSend$action_QueryManagerState:error:
+ _objc_msgSend$action_ReportScanCanceled:error:
+ _objc_msgSend$action_ReportScanOutcome:error:
+ _objc_msgSend$addObject:
+ _objc_msgSend$allObjects
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$betaPrograms
+ _objc_msgSend$bodyForAdmissionControlDenial:
+ _objc_msgSend$bodyTokenWithType:parameters:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bridgeClient
+ _objc_msgSend$bridgeLogger
+ _objc_msgSend$callbackQueue
+ _objc_msgSend$concurrentQueue
+ _objc_msgSend$containsObject:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$currentDownload
+ _objc_msgSend$currentDownloadForDescriptor:completion:
+ _objc_msgSend$currentState
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$descriptionForObject:properties:
+ _objc_msgSend$deviceType
+ _objc_msgSend$documentation
+ _objc_msgSend$downloadSize
+ _objc_msgSend$emptyScanResults
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$enrolledBetaProgram
+ _objc_msgSend$enrolledBetaProgramForDevice:completion:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$estimatedTimeRemaining
+ _objc_msgSend$firstObject
+ _objc_msgSend$floatValue
+ _objc_msgSend$followupEvent:withInfo:
+ _objc_msgSend$fullUpdateName
+ _objc_msgSend$getDevicesMatchingPlatforms:completion:
+ _objc_msgSend$hash
+ _objc_msgSend$hashTableWithOptions:
+ _objc_msgSend$headingForAdmissionControlDenial:
+ _objc_msgSend$headingTokenWithType:parameters:
+ _objc_msgSend$humanReadableUpdateName
+ _objc_msgSend$initFromScanParam:withIdentifier:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithDescriptor:
+ _objc_msgSend$initWithDeviceType:
+ _objc_msgSend$initWithDocumentation:
+ _objc_msgSend$initWithDownload:
+ _objc_msgSend$initWithEnvironment:forPairedDevice:bridgeClient:identifier:
+ _objc_msgSend$initWithFullScanContext:
+ _objc_msgSend$initWithIdentifier:environment:usingBridgeClient:andBetaManager:withCompletionQueue:
+ _objc_msgSend$initWithPreferredDescriptor:andRefreshContext:
+ _objc_msgSend$initWithProgress:
+ _objc_msgSend$installUpdate:
+ _objc_msgSend$installationSize
+ _objc_msgSend$invalidate
+ _objc_msgSend$invocationWithMethodSignature:
+ _objc_msgSend$invoke
+ _objc_msgSend$isAutoUpdateScheduled
+ _objc_msgSend$isDone
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isInvalidated
+ _objc_msgSend$isNonBlockingErrorForStatefulDescriptor:download:
+ _objc_msgSend$isUpdateReadyForInstallation
+ _objc_msgSend$licenseAgreement
+ _objc_msgSend$localizedStringFromNumber:numberStyle:
+ _objc_msgSend$longLongValue
+ _objc_msgSend$manager:didChangeProgressOnDownload:
+ _objc_msgSend$manager:didFailDownload:withError:
+ _objc_msgSend$manager:didFailInstallation:withError:
+ _objc_msgSend$manager:didFinishInstallation:
+ _objc_msgSend$manager:installationAwaitingUserInteraction:
+ _objc_msgSend$manager:installationOfUpdate:willProceed:waitingForAdmissionControl:
+ _objc_msgSend$manager:scanRequestDidLocateUpdate:error:
+ _objc_msgSend$manager:userInstallRequestTypeDidChange:
+ _objc_msgSend$managerState:
+ _objc_msgSend$managerUserDidAcceptTermsAndConditionsForUpdate:
+ _objc_msgSend$methodSignatureForSelector:
+ _objc_msgSend$null
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$observer
+ _objc_msgSend$operationError
+ _objc_msgSend$options
+ _objc_msgSend$percentComplete
+ _objc_msgSend$phase
+ _objc_msgSend$portionComplete
+ _objc_msgSend$postEvent:withInfo:
+ _objc_msgSend$postEvent:withInfo:endingActivity:
+ _objc_msgSend$preferencesIcon
+ _objc_msgSend$preferredDescriptor
+ _objc_msgSend$preferredUpdateDownloadError
+ _objc_msgSend$preferredUpdateDownloadable
+ _objc_msgSend$preparationSize
+ _objc_msgSend$productBuildVersion
+ _objc_msgSend$productSystemName
+ _objc_msgSend$productVersion
+ _objc_msgSend$programID
+ _objc_msgSend$progress
+ _objc_msgSend$publisher
+ _objc_msgSend$purgeUpdate:completion:
+ _objc_msgSend$queryProgramsForSystemAccountsWithPlatforms:retryConfiguration:identifier:completion:
+ _objc_msgSend$quickConfiguration
+ _objc_msgSend$raise:format:
+ _objc_msgSend$releaseNotes
+ _objc_msgSend$releaseNotesSummary
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$scanError
+ _objc_msgSend$scanForUpdates
+ _objc_msgSend$scanForUpdatesWithCompletion:
+ _objc_msgSend$scanGroup
+ _objc_msgSend$scheduleConcurrentActionWithSelector:eventInfo:
+ _objc_msgSend$seedingBetaManager
+ _objc_msgSend$selfRetain
+ _objc_msgSend$setArgument:atIndex:
+ _objc_msgSend$setBetaPrograms:
+ _objc_msgSend$setCallbackQueue:
+ _objc_msgSend$setCurrentDownload:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setEmptyScanResults:
+ _objc_msgSend$setEnrolledBetaProgram:
+ _objc_msgSend$setIsUpdateReadyForInstallation:
+ _objc_msgSend$setManagerState:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObserver:
+ _objc_msgSend$setOperationError:
+ _objc_msgSend$setPreferredDescriptor:
+ _objc_msgSend$setPreferredUpdateDownloadError:
+ _objc_msgSend$setPreferredUpdateDownloadable:
+ _objc_msgSend$setScanError:
+ _objc_msgSend$setSelector:
+ _objc_msgSend$setSelfRetain:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$setToken:
+ _objc_msgSend$setUserInstallRequestTypeForUpdate:userInstallRequestType:completion:
+ _objc_msgSend$startDownload:
+ _objc_msgSend$statefulUILogger
+ _objc_msgSend$stringFromByteCount:countStyle:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$strongToStrongObjectsMapTable
+ _objc_msgSend$systemBuildVersion
+ _objc_msgSend$token
+ _objc_msgSend$totalRequiredFreeSpace
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _objc_msgSend$underlyingDescriptor
+ _objc_msgSend$underlyingDocumentation
+ _objc_msgSend$underlyingDownload
+ _objc_msgSend$underlyingProgress
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$userDidAcceptTermsAndConditionsForUpdate:completion:
+ _objc_msgSend$userInfo
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$valueForProperty:
+ _objc_opt_isKindOfClass
+ _objc_opt_respondsToSelector
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _os_unfair_lock_lock_with_options
+ _symbolic So9PDRDeviceCSg
+ _symbolic _____Sg 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierV
+ _symbolic _____XDXMT 22SoftwareUpdateUIBridge29SUUIBridgePlatformEnvironmentC
- -[SUUIBridgeScanOperation initWithIdentifier:environment:withCompletionQueue:]
- -[SUUIBridgeScanOperationFullScanResults initWithIdentifier:]
- -[SUUIBridgeScanOperationResults initWithIdentifier:]
- -[SUUIBridgeStatefulUIManager initWithEnvironment:identifier:]
- GCC_except_table10
- _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
- _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
- ___107-[SUUIBridgeScanOperation refreshScanResultsWithPreferredUpdate:alternateUpdate:context:completionHandler:]_block_invoke
- ___34-[SUUIBridgeScanOperation cancel:]_block_invoke
- ___81-[SUUIBridgeScanOperation checkForAvailableUpdatesWithContext:completionHandler:]_block_invoke
- ___os_log_helper_16_2_4_8_32_8_66_8_66_8_64
- _objc_msgSend$initWithEnvironment:identifier:
- _objc_msgSend$initWithIdentifier:environment:withCompletionQueue:
CStrings:
+ ""
+ " "
+ " ("
+ "%@ (%@)"
+ "%s [%{public}@|%{public}@]: Beta Updates Management is not supported. Skipping."
+ "%s [%{public}@|%{public}@]: Cancel has been requested. Skipping on %{public}@"
+ "%s [%{public}@|%{public}@]: Classified as download-phase error: %{public}@"
+ "%s [%{public}@|%{public}@]: Classified as scan-phase error (device locked): %{public}@"
+ "%s [%{public}@|%{public}@]: Classified as scan-phase error: %{public}@"
+ "%s [%{public}@|%{public}@]: Concurrent queue is nil, cannot dispatch action %{public}@"
+ "%s [%{public}@|%{public}@]: Could not determine SDPlatform for device type %ld. Skipping beta query."
+ "%s [%{public}@|%{public}@]: Could not fetch beta programs: %ld"
+ "%s [%{public}@|%{public}@]: Current download for descriptor: %{public}@"
+ "%s [%{public}@|%{public}@]: Got beta programs (count: %ld): %{public}@"
+ "%s [%{public}@|%{public}@]: Ignoring managerState completion; the connectivity timeout already reported."
+ "%s [%{public}@|%{public}@]: Ignoring request to call dispatch_group_leave for the action %{public}@, as the running actions set has no entry for this action anymore."
+ "%s [%{public}@|%{public}@]: Ignoring scan completion; the connectivity timeout already reported."
+ "%s [%{public}@|%{public}@]: Manager state: %ld, update: %{public}@, error: %{public}@"
+ "%s [%{public}@|%{public}@]: No SDDevice found for platform %lu. Skipping enrolled beta program query."
+ "%s [%{public}@|%{public}@]: Not scheduling action %{public}@ because a previous action has already failed or timed out"
+ "%s [%{public}@|%{public}@]: Querying beta programs for platform: %lu"
+ "%s [%{public}@|%{public}@]: Refreshed current beta program: %{public}@ (program ID: %{public}@)"
+ "%s [%{public}@|%{public}@]: Reporting a %{public}s scan of type: %{public}@"
+ "%s [%{public}@|%{public}@]: Scan completed. descriptor: %{public}@, error: %{public}@"
+ "%s [%{public}@|%{public}@]: Skipping managerState query (device locked): %{public}@"
+ "%s [%{public}@|%{public}@]: The scan was canceled. Calling the cancelation handler."
+ "%s [%{public}@|%{public}@]: The seeding beta manager was not configured for this scan operation. Skipping."
+ "%s [%{public}@|%{public}@]: The task has already been canceled. Stopping."
+ "%s [%{public}@|%{public}@]: Timed out waiting for the companion manager-state response after %ld seconds."
+ "%s [%{public}@|%{public}@]: Timed out waiting for the companion scan response after %ld seconds."
+ "%s [%{public}@|%{public}@]: Up to date (SUBErrorUpToDate) — not an error"
+ "%s: ...client registered (initial state: %ld)"
+ "%s: ...installUpdate awaiting user interaction (descriptor: %{public}@)"
+ "%s: ...installUpdate failed (descriptor: %{public}@): %{public}@"
+ "%s: ...installUpdate finished (descriptor: %{public}@)"
+ "%s: ...installUpdate will proceed (descriptor: %{public}@, willProceed: %d, waiting: %d)"
+ "%s: ...scanForUpdates failed: %{public}@"
+ "%s: ...scanForUpdates finished (descriptor: %{public}@)"
+ "%s: ...setUserInstallRequestTypeForUpdate finished (type: %ld)"
+ "%s: ...startDownload failed (%{public}@): %{public}@"
+ "%s: ...startDownload progress changed (%{public}@)"
+ "%s: ...userDidAcceptTermsAndConditionsForUpdate finished"
+ "%s: Calling installUpdate...(%{public}@)"
+ "%s: Calling managerState..."
+ "%s: Calling purgeUpdate...(%{public}@)"
+ "%s: Calling scanForUpdates..."
+ "%s: Calling setUserInstallRequestTypeForUpdate...(type: %ld, %{public}@)"
+ "%s: Calling startDownload...(%{public}@)"
+ "%s: Calling userDidAcceptTermsAndConditionsForUpdate...(%{public}@)"
+ "%s: Registering client with SUBManager..."
+ "%s: Returning cached download for descriptor %{public}@: %{public}@"
+ "(null)"
+ ")"
+ "-[SUUIBridgeManagerClient currentDownloadForDescriptor:completion:]"
+ "-[SUUIBridgeManagerClient initWithDeviceType:]"
+ "-[SUUIBridgeManagerClient initWithDeviceType:]_block_invoke"
+ "-[SUUIBridgeManagerClient installUpdate:completion:]"
+ "-[SUUIBridgeManagerClient manager:didChangeProgressOnDownload:]"
+ "-[SUUIBridgeManagerClient manager:didFailDownload:withError:]"
+ "-[SUUIBridgeManagerClient manager:didFailInstallation:withError:]"
+ "-[SUUIBridgeManagerClient manager:didFinishInstallation:]"
+ "-[SUUIBridgeManagerClient manager:installationAwaitingUserInteraction:]"
+ "-[SUUIBridgeManagerClient manager:installationOfUpdate:willProceed:waitingForAdmissionControl:]"
+ "-[SUUIBridgeManagerClient manager:scanRequestDidLocateUpdate:error:]"
+ "-[SUUIBridgeManagerClient manager:userInstallRequestTypeDidChange:]"
+ "-[SUUIBridgeManagerClient managerState:]"
+ "-[SUUIBridgeManagerClient managerUserDidAcceptTermsAndConditionsForUpdate:]"
+ "-[SUUIBridgeManagerClient purgeUpdate:completion:]"
+ "-[SUUIBridgeManagerClient scanForUpdatesWithCompletion:]"
+ "-[SUUIBridgeManagerClient setUserInstallRequestType:forUpdate:completion:]"
+ "-[SUUIBridgeManagerClient startDownload:completion:]"
+ "-[SUUIBridgeManagerClient userDidAcceptTermsAndConditionsForUpdate:completion:]"
+ "-[SUUIBridgeScanOperation _classifyScanError:withDescriptor:intoParam:]"
+ "-[SUUIBridgeScanOperation action_CheckForAvailableUpdate:error:]_block_invoke"
+ "-[SUUIBridgeScanOperation action_ObserveConcurrentQueries:error:]_block_invoke"
+ "-[SUUIBridgeScanOperation action_QueryCurrentDownload:error:]_block_invoke"
+ "-[SUUIBridgeScanOperation action_QueryManagerState:error:]"
+ "-[SUUIBridgeScanOperation action_QueryManagerState:error:]_block_invoke"
+ "-[SUUIBridgeScanOperation action_ReportScanCanceled:error:]"
+ "-[SUUIBridgeScanOperation action_ReportScanCanceled:error:]_block_invoke"
+ "-[SUUIBridgeScanOperation action_ReportScanOutcome:error:]"
+ "-[SUUIBridgeScanOperation action_ReportScanOutcome:error:]_block_invoke"
+ "-[SUUIBridgeScanOperation checkForBetaPrograms:withReplyHandler:]"
+ "-[SUUIBridgeScanOperation checkForBetaPrograms:withReplyHandler:]_block_invoke"
+ "-[SUUIBridgeScanOperation initWithIdentifier:environment:usingBridgeClient:andBetaManager:withCompletionQueue:]"
+ "-[SUUIBridgeScanOperation scheduleConcurrentActionWithSelector:eventInfo:]"
+ "-[SUUIBridgeScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke"
+ "11"
+ "165413ff-a1b0-4e64-b0a0-25ca4fa99e4a"
+ "<%@: %p; invalidated=%{BOOL}d>"
+ "Bridge Platform Environment initialized successfully\nHost Device: %{public}s\nTarget Device: %{public}s\nPaired Device: %{public}s\nPaired Device Name: %{private}s\nEffective Policy: %{public}s\nStatefulUI Environment: %{public}s 0x%{public}s (%{public}s)"
+ "Concurrent operations timed out."
+ "Could not create a copy of %@: archiving the underlying descriptor failed."
+ "Could not create a copy of %@: archiving the underlying documentation failed."
+ "Could not create a copy of %@: archiving the underlying download failed."
+ "Could not create a copy of %@: archiving the underlying progress failed."
+ "Could not create a copy of %@: unarchiving the underlying descriptor failed."
+ "Could not create a copy of %@: unarchiving the underlying documentation failed."
+ "Could not create a copy of %@: unarchiving the underlying download failed."
+ "Could not create a copy of %@: unarchiving the underlying progress failed."
+ "Could not invoke a completion handler for a 'None' operation type."
+ "Couldn't map the error into a localizable body for %{public}@: %{public}@"
+ "Couldn't map the error into a localizable title for %{public}@: %{public}@"
+ "EnrollmentInSettings"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.CheckForUpdates"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ObserveConcurrentQueries"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryCurrentDownload"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryManagerState"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForBetaPrograms:withReplyHandler:"
+ "Received an unexpected non-SUB error for descriptor %{public}@. Not ignoring. Error: %{public}@"
+ "SU - Timeout waiting for update"
+ "SUBManager is nil: SoftwareUpdateBridge is unavailable on this image."
+ "SUUIBridgeManagerClientDeviceTypeWatch"
+ "Seeding"
+ "The given eventInfo parameter must not be nil."
+ "The machine is currently in a middle of a scan."
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.CheckForUpdates"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ObserveConcurrentQueries"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryCurrentDownload"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryManagerState"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForBetaPrograms:withReplyHandler:"
+ "descriptor"
+ "documentation"
+ "download"
+ "failed"
+ "hash"
+ "none"
+ "programID"
+ "progress"
+ "queryHostRootsInstalledCapability: rooted from darwinup snapshot %{public}s"
+ "queryHostRootsInstalledCapability: statfs(\"/\") failed with errno: %{public}d"
+ "successful"
+ "unknown"
+ "updateName"
+ "v16@?0@\"<SUBManagerDelegate>\"8"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"SDBetaProgram\"8"
+ "v16@?0@\"SUBDownload\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"NSArray\"8q16"
+ "v24@?0@\"NSError\"8q16"
+ "v24@?0@\"SUBDescriptor\"8@\"NSError\"16"
+ "v32@?0q8@\"SUBDescriptor\"16@\"NSError\"24"
- "$*"
- "%s [%{public}@|%{public}@]: Cancel has been requested. Skipping on %@"
- "-[SUUIBridgeScanOperation cancel:]_block_invoke"
- "-[SUUIBridgeScanOperation checkForAvailableUpdatesWithContext:completionHandler:]_block_invoke"
- "-[SUUIBridgeScanOperation initWithIdentifier:environment:withCompletionQueue:]"
- "-[SUUIBridgeScanOperation refreshScanResultsWithPreferredUpdate:alternateUpdate:context:completionHandler:]_block_invoke"
- "Bridge Platform Environment initialized successfully\nHost Device: %s\nTarget Device: %s\nEffective Policy: %s\nStatefulUI Environment: %s 0x%s (%s)"
- "cd060049-2465-43e3-bbb5-d769a66da2d7"
- "ffc25f86-b83c-4139-b8ad-91131d0e5429"
- "q"
- "queryRootsInstalledCapability: rooted from darwinup snapshot %s"
- "queryRootsInstalledCapability: statfs(\"/\") failed with errno: %d"
```
