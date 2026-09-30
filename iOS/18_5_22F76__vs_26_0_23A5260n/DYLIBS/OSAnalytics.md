## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

```diff

-758.120.5.0.0
-  __TEXT.__text: 0x40418
-  __TEXT.__auth_stubs: 0x1450
-  __TEXT.__objc_methlist: 0x1aa0
-  __TEXT.__const: 0x5e0
-  __TEXT.__oslogstring: 0x347a
-  __TEXT.__cstring: 0x92d7
-  __TEXT.__gcc_except_tab: 0x1208
-  __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0xa98
-  __TEXT.__eh_frame: 0x40
-  __TEXT.__objc_classname: 0x32a
-  __TEXT.__objc_methname: 0x4e5e
-  __TEXT.__objc_methtype: 0xc92
-  __TEXT.__objc_stubs: 0x4640
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x11b0
-  __DATA_CONST.__objc_classlist: 0xf0
+912.0.0.0.0
+  __TEXT.__text: 0x46708
+  __TEXT.__auth_stubs: 0x1980
+  __TEXT.__objc_methlist: 0x1bd8
+  __TEXT.__const: 0x6e8
+  __TEXT.__oslogstring: 0x392c
+  __TEXT.__cstring: 0x91c6
+  __TEXT.__gcc_except_tab: 0x1260
+  __TEXT.__dlopen_cstrs: 0x21f
+  __TEXT.__constg_swiftt: 0x130
+  __TEXT.__swift5_typeref: 0x7e
+  __TEXT.__swift5_fieldmd: 0x64
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_reflstr: 0x18
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0xc58
+  __TEXT.__eh_frame: 0x170
+  __TEXT.__objc_classname: 0x318
+  __TEXT.__objc_methname: 0x50eb
+  __TEXT.__objc_methtype: 0xc05
+  __TEXT.__objc_stubs: 0x48e0
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x1330
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1550
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0xc60
-  __AUTH_CONST.__auth_got: 0xa38
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0xa4a0
-  __AUTH_CONST.__objc_const: 0x3720
+  __DATA_CONST.__objc_arraydata: 0x978
+  __AUTH_CONST.__auth_got: 0xcd0
+  __AUTH_CONST.__const: 0x4a1
+  __AUTH_CONST.__cfstring: 0xa080
+  __AUTH_CONST.__objc_const: 0x38a8
   __AUTH_CONST.__objc_intobj: 0x4c8
-  __AUTH_CONST.__objc_dictobj: 0x4b0
-  __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x2c8
-  __DATA.__data: 0x168
-  __DATA.__bss: 0x148
-  __DATA_DIRTY.__objc_data: 0x780
-  __DATA_DIRTY.__bss: 0x290
+  __AUTH_CONST.__objc_dictobj: 0x550
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH.__objc_data: 0x340
+  __AUTH.__data: 0x168
+  __DATA.__objc_ivar: 0x2cc
+  __DATA.__data: 0x1d8
+  __DATA.__bss: 0x1b8
+  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
+  - /System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery
   - /System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Symbolication.framework/Symbolication

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 643A1257-0407-34A5-B97D-9CB131AF5471
-  Functions: 976
-  Symbols:   3679
-  CStrings:  4305
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: F0A77940-642C-398C-AF90-759E108046E8
+  Functions: 1140
+  Symbols:   3944
+  CStrings:  4307
 
Symbols:
+ +[OSADiagnosticsReporterSupport initAlertDelegate]
+ +[OSALegacyXform transformURL:template:options:]
+ +[OSALegacyXform transformURL:template:options:].cold.1
+ +[OSALegacyXform transformURL:template:options:].cold.2
+ +[OSALog createForSubmission:metadata:options:error:writing:].cold.4
+ +[OSALog createRetiredDirectoriesForUser:]
+ +[OSALog createRetiredDirectoriesForUser:].cold.1
+ +[OSALog createRetiredDirectoriesForUser:].cold.2
+ +[OSALog createRetiredDirectoriesForUser:].cold.3
+ +[OSALog locallyCreateForSubmission:metadata:options:error:writing:].cold.2
+ +[OSAReport bootProgressRegister]
+ +[OSAReport isDeveloperMode]
+ +[OSAReport isInLDM]
+ +[OSAReport isSecurityResearchDeviceERM]
+ +[OSASystemConfiguration ensureUsablePath:component:options:].cold.1
+ +[OSASystemConfiguration(optIn) boolValForMCSetting:]
+ +[OSASystemConfiguration(optIn) sharedMCProfileConnection]
+ +[OSASystemConfiguration(optIn) sharedMCProfileConnection].cold.1
+ +[OSATasking defaultTasking]
+ +[OSATasking normalizeInstructions:forSamplingKey:]
+ +[OSATasking normalizeInstructions:forSamplingKey:].cold.1
+ +[OSATasking normalizeInstructions:forSamplingKey:].cold.2
+ +[OSATasking randomizedCRKey]
+ +[OSATasking samplingKey]
+ +[OSATasking samplingKey].cold.1
+ +[OSATasking shouldApplyPreference:forSamplingKey:]
+ -[NSMutableArray(OSABinaryImageListExtension) addJITImage:size:]
+ -[NSString(Trimming) stringByReplacingPathBeforeComponent:with:]
+ -[OSABinaryImageSegment initWithSource:size:for:source:]
+ -[OSABinaryImageSegment initWithSymbol:source:]
+ -[OSAOsLogPackParser filterOutSensitiveParts:withFormats:]
+ -[OSAOsLogPackParser formatStringIsSafe]
+ -[OSAOsLogPackParser initWithMaxNumAruments:]
+ -[OSAOsLogPackParser maxNumArguments]
+ -[OSAOsLogPackParser modulePathForMemoryPointer]
+ -[OSAOsLogPackParser pointerPointsToSafeMemory]
+ -[OSAOsLogPackParser setFormatStringIsSafe:]
+ -[OSAOsLogPackParser setModulePathForMemoryPointer:]
+ -[OSAOsLogPackParser setPointerPointsToSafeMemory:]
+ -[OSAParsedOsLogPart argSpecifier]
+ -[OSAParsedOsLogPart initWithArgument:argSpecifier:isSafe:]
+ -[OSAParsedOsLogPart initWithLiteral:isSafe:]
+ -[OSAParsedOsLogPart isSafe]
+ -[OSAProxyConfiguration hwModel]
+ -[OSAProxyConfiguration isInDeviceRecoveryEnvironment]
+ -[OSAProxyConfiguration legacyAutomatedDeviceGroup]
+ -[OSAProxyConfiguration recoveryModeReason]
+ -[OSASystemConfiguration hwModel]
+ -[OSASystemConfiguration isInDeviceRecoveryEnvironment]
+ -[OSASystemConfiguration legacyAutomatedDeviceGroup]
+ -[OSASystemConfiguration overrideMountPath]
+ -[OSASystemConfiguration recoveryModeReason]
+ -[OSASystemConfiguration(optIn) optIn3rdParty].cold.1
+ -[OSASystemConfiguration(optIn) optInApple].cold.1
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table128
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table6
+ OBJC_IVAR_$_OSAProxyConfiguration._hwModel
+ OBJC_IVAR_$_OSAProxyConfiguration._isInDeviceRecoveryEnvironment
+ OBJC_IVAR_$_OSAProxyConfiguration._legacyAutomatedDeviceGroup
+ _DREEntryReason
+ _DREIsRunningInDeviceRecoveryEnvironemnt
+ _IOConnectCallScalarMethod
+ _IOObjectRelease
+ _IOServiceClose
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _IOServiceOpen
+ _LockdownModeLibraryCore
+ _LockdownModeLibraryCore.frameworkLibrary
+ _ManagedConfigurationLibrary
+ _ManagedConfigurationLibraryCore
+ _ManagedConfigurationLibraryCore.frameworkLibrary
+ _MobileGestalt_copy_hwModelDescriptionForAnalytics_obj
+ _MobileGestalt_copy_productTypeDescForAnalytics_obj
+ _MobileGestalt_get_current_device
+ _NSURLVolumeSupportsExclusiveRenamingKey
+ _OBJC_CLASS_$_VMUWiredMemoryInfo
+ _OBJC_CLASS_$__TtC11OSAnalytics11DeviceState
+ _OBJC_CLASS_$__TtC11OSAnalytics24WatchdogExitReasonHelper
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_OSAOsLogPackParser._formatStringIsSafe
+ _OBJC_IVAR_$_OSAOsLogPackParser._maxNumArguments
+ _OBJC_IVAR_$_OSAOsLogPackParser._modulePathForMemoryPointer
+ _OBJC_IVAR_$_OSAOsLogPackParser._pointerPointsToSafeMemory
+ _OBJC_IVAR_$_OSAParsedOsLogPart._argSpecifier
+ _OBJC_IVAR_$_OSAParsedOsLogPart._isSafe
+ _OBJC_IVAR_$_OSAProxyConfiguration._recoveryModeReason
+ _OBJC_IVAR_$_OSASystemConfiguration._recoveryModeReason
+ _OBJC_METACLASS_$__TtC11OSAnalytics11DeviceState
+ _OBJC_METACLASS_$__TtC11OSAnalytics24WatchdogExitReasonHelper
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OSAIsFeedbackPromptingEnabled
+ _OSASandboxConsumeExtensionNoRelease
+ _OSASandboxConsumeExtensionNoRelease.cold.1
+ _OSASandboxConsumeExtensionNoRelease.cold.2
+ _OSASandboxExtensionForPath
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ __CLASS_METHODS__TtC11OSAnalytics11DeviceState
+ __CLASS_METHODS__TtC11OSAnalytics24WatchdogExitReasonHelper
+ __CLASS_PROPERTIES__TtC11OSAnalytics11DeviceState
+ __DATA__TtC11OSAnalytics11DeviceState
+ __DATA__TtC11OSAnalytics24WatchdogExitReasonHelper
+ __DATA__TtC11OSAnalytics9IPSReport
+ __INSTANCE_METHODS__TtC11OSAnalytics11DeviceState
+ __INSTANCE_METHODS__TtC11OSAnalytics24WatchdogExitReasonHelper
+ __IVARS__TtC11OSAnalytics9IPSReport
+ __METACLASS_DATA__TtC11OSAnalytics11DeviceState
+ __METACLASS_DATA__TtC11OSAnalytics24WatchdogExitReasonHelper
+ __METACLASS_DATA__TtC11OSAnalytics9IPSReport
+ __OBJC_$_CLASS_METHODS_OSASystemConfiguration(optIn)
+ ___25+[OSALog cleanupForUser:]_block_invoke.374
+ ___25+[OSALog cleanupForUser:]_block_invoke_2
+ ___25+[OSALog cleanupForUser:]_block_invoke_3
+ ___25+[OSALog cleanupForUser:]_block_invoke_3.cold.1
+ ___32+[OSALog scanLogs:from:options:]_block_invoke.398
+ ___32+[OSALog scanLogs:from:options:]_block_invoke.cold.1
+ ___32+[OSALog scanLogs:from:options:]_block_invoke.cold.2
+ ___33+[OSAReport bootProgressRegister]_block_invoke
+ ___33+[OSAReport bootProgressRegister]_block_invoke.cold.1
+ ___33+[OSAReport bootProgressRegister]_block_invoke.cold.2
+ ___33+[OSAReport bootProgressRegister]_block_invoke.cold.3
+ ___33-[OSASystemConfiguration hwModel]_block_invoke
+ ___35-[OSAExclaveContainer parseKCdata:]_block_invoke.92
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.379
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.379.cold.1
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.379.cold.2
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.379.cold.3
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.379.cold.4
+ ___43+[OSATasking applyTasking:taskId:fromBlob:]_block_invoke.104
+ ___43-[OSASystemConfiguration overrideMountPath]_block_invoke
+ ___43-[OSASystemConfiguration overrideMountPath]_block_invoke.cold.1
+ ___43-[OSASystemConfiguration overrideMountPath]_block_invoke.cold.2
+ ___43-[OSASystemConfiguration overrideMountPath]_block_invoke.cold.3
+ ___43-[OSASystemConfiguration overrideMountPath]_block_invoke_2
+ ___43-[OSASystemConfiguration overrideMountPath]_block_invoke_3
+ ___43-[OSASystemConfiguration(optIn) optInApple]_block_invoke
+ ___43-[OSASystemConfiguration(optIn) optInApple]_block_invoke.cold.1
+ ___44-[OSAReport streamContentAtLevel:withBlock:]_block_invoke.117
+ ___44-[OSAReport streamContentAtLevel:withBlock:]_block_invoke.117.cold.1
+ ___44-[OSAReport streamContentAtLevel:withBlock:]_block_invoke.117.cold.2
+ ___44-[OSASystemConfiguration recoveryModeReason]_block_invoke
+ ___46-[OSASystemConfiguration(optIn) optIn3rdParty]_block_invoke
+ ___46-[OSASystemConfiguration(optIn) optIn3rdParty]_block_invoke.cold.1
+ ___48+[OSALegacyXform transformURL:template:options:]_block_invoke
+ ___52-[OSASystemConfiguration legacyAutomatedDeviceGroup]_block_invoke
+ ___55-[OSASystemConfiguration isInDeviceRecoveryEnvironment]_block_invoke
+ ___58+[OSASystemConfiguration(optIn) sharedMCProfileConnection]_block_invoke
+ ___61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.284
+ ___61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.289
+ ___61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.290
+ ___61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.463
+ ___LockdownModeLibraryCore_block_invoke
+ ___ManagedConfigurationLibraryCore_block_invoke
+ ___block_descriptor_32_e13_v24?0r*8r*16l
+ ___block_descriptor_40_e8_32r_e8_v12?0i8lr32l8
+ ___block_descriptor_40_e8_32s_e13_B24?0r*8r*16ls32l8
+ ___block_descriptor_68_e8_32r_e8_v12?0i8lr32l8
+ ___block_descriptor_72_e8_32r_e8_v12?0i8lr32l8
+ ___block_literal_global.11
+ ___block_literal_global.125
+ ___block_literal_global.157
+ ___block_literal_global.18
+ ___block_literal_global.20
+ ___block_literal_global.204
+ ___block_literal_global.324
+ ___block_literal_global.367
+ ___block_literal_global.376
+ ___block_literal_global.379
+ ___block_literal_global.39
+ ___block_literal_global.400
+ ___block_literal_global.432
+ ___block_literal_global.59
+ ___getLockdownModeManagerClass_block_invoke
+ ___getLockdownModeManagerClass_block_invoke.cold.1
+ ___getMCFeatureAppAnalyticsAllowedSymbolLoc_block_invoke
+ ___getMCFeatureDiagnosticsSubmissionAllowedSymbolLoc_block_invoke
+ ___getMCProfileConnectionClass_block_invoke
+ ___rtc_internal_block_invoke.62
+ ___rtc_internal_block_invoke.62.cold.1
+ ___rtc_internal_block_invoke.62.cold.2
+ ___rtc_internal_block_invoke.62.cold.3
+ ___rtc_internal_block_invoke.64
+ ___rtc_internal_block_invoke.65.cold.1
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_OSAnalytics
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_OSAnalytics
+ __swift_stdlib_malloc_size
+ _audit_stringLockdownMode
+ _audit_stringManagedConfiguration
+ _feof
+ _ferror
+ _getLockdownModeManagerClass.softClass
+ _getMCFeatureAppAnalyticsAllowedSymbolLoc.ptr
+ _getMCFeatureDiagnosticsSubmissionAllowedSymbolLoc.ptr
+ _getMCProfileConnectionClass.softClass
+ _getOSADiagnosticsReporterClass
+ _hwModel.pred
+ _initAlertDelegate.OSADiagnosticsReporterClass
+ _isInDeviceRecoveryEnvironment.pred
+ _kIOMainPortDefault
+ _kOSALogMetadataRecoveryModeReason
+ _kOSALogOptionOptInOverride
+ _kOSALogScanOptionIncludeHidden
+ _legacyAutomatedDeviceGroup.onceToken
+ _malloc_size
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$addJITImage:size:
+ _objc_msgSend$argSpecifier
+ _objc_msgSend$boolValForMCSetting:
+ _objc_msgSend$bootProgressRegister
+ _objc_msgSend$createRetiredDirectoriesForUser:
+ _objc_msgSend$defaultTasking
+ _objc_msgSend$descriptionFromCode:
+ _objc_msgSend$enabled
+ _objc_msgSend$hwModel
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$initAlertDelegate
+ _objc_msgSend$initWithArgument:argSpecifier:isSafe:
+ _objc_msgSend$initWithLiteral:isSafe:
+ _objc_msgSend$initWithSource:size:for:source:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$initWithSymbol:source:
+ _objc_msgSend$isCustomerFused
+ _objc_msgSend$isDeveloperMode
+ _objc_msgSend$isInDeviceRecoveryEnvironment
+ _objc_msgSend$isInLDM
+ _objc_msgSend$isSafe
+ _objc_msgSend$legacyAutomatedDeviceGroup
+ _objc_msgSend$normalizeInstructions:forSamplingKey:
+ _objc_msgSend$randomizedCRKey
+ _objc_msgSend$recoveryModeReason
+ _objc_msgSend$samplingKey
+ _objc_msgSend$scanProxies:
+ _objc_msgSend$shared
+ _objc_msgSend$sharedMCProfileConnection
+ _objc_msgSend$shouldApplyPreference:forSamplingKey:
+ _objc_msgSend$stringByReplacingPathBeforeComponent:with:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$transformURL:template:options:
+ _objc_opt_self
+ _optIn3rdParty._featureAppAnalyticsAllowed
+ _optIn3rdParty.onceToken
+ _optInApple._featureDiagnosticsSubmissionAllowed
+ _optInApple.onceToken
+ _overrideMountPath.onceToken
+ _overrideMountPath.success
+ _recoveryModeReason.pred
+ _removeCurrentAwdTasking
+ _resampleTruncatedStacksWithSymbolicator
+ _sharedMCProfileConnection._sharedConnection
+ _sharedMCProfileConnection.onceToken
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deallocPartialClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic $s11OSAnalytics11SubmittableP
+ _symbolic SDySSypG
+ _symbolic SS
+ _symbolic So8NSObjectC
+ _symbolic _____ 11OSAnalytics11DeviceStateC
+ _symbolic _____ 11OSAnalytics24WatchdogExitReasonHelperC
+ _symbolic _____ 11OSAnalytics9IPSReportC
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______pSg 10Foundation15ContiguousBytesP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____yypG s23_ContiguousArrayStorageC
- +[OSALegacyXform transformURL:options:].cold.1
- +[OSALegacyXform transformURL:options:].cold.2
- +[OSATasking getDefaultTasking]
- +[OSATasking normalizeInstructions:]
- +[OSATasking normalizeInstructions:].cold.1
- +[OSATasking normalizeInstructions:].cold.2
- +[OSATasking normalizeInstructions:].cold.3
- +[OSATasking setCRKeyToRandomValue]
- +[OSATasking shouldApplyPreference:]
- -[OSABinaryImageSegment initWithSymbol:]
- -[OSAExclaveContainer getFramesForThread:usingCatalog:].cold.3
- -[OSAExclaveContainer getFramesForThread:usingCatalog:].cold.4
- -[OSAOsLogPackParser filterOutSensitiveStrings:]
- -[OSAOsLogPackParser formatStringIsImmutable]
- -[OSAOsLogPackParser modulePathForImmutableMemoryPointer]
- -[OSAOsLogPackParser pointerPointsToImmutableMemory]
- -[OSAOsLogPackParser setFormatStringIsImmutable:]
- -[OSAOsLogPackParser setModulePathForImmutableMemoryPointer:]
- -[OSAOsLogPackParser setPointerPointsToImmutableMemory:]
- -[OSAParsedOsLogPart initWithIntegerArgumentStringValue:]
- -[OSAParsedOsLogPart initWithLiteral:isImmutable:]
- -[OSAParsedOsLogPart initWithStringArgument:isImmutable:]
- -[OSAParsedOsLogPart isImmutable]
- -[OSAWiredMemoryInfo dealloc]
- -[OSAWiredMemoryInfo getCounterNameForSite:]
- -[OSAWiredMemoryInfo getTagNameForSite:]
- -[OSAWiredMemoryInfo initWithZoneNames:nameCount:zoneInfo:zoneInfoCount:wiredInfo:wiredInfoCount:]
- -[OSAWiredMemoryInfo vmRegionInfo]
- -[OSAWiredMemoryInfo zoneInfo]
- GCC_except_table27
- GCC_except_table31
- GCC_except_table41
- GCC_except_table45
- GCC_except_table91
- GCC_except_table94
- GCC_except_table95
- _CSSymbolGetName
- _CSSymbolicatorCreateWithMachKernel
- _CSSymbolicatorGetSymbolWithAddressAtTime
- _OBJC_CLASS_$_OSAWiredMemoryInfo
- _OBJC_IVAR_$_OSAOsLogPackParser._formatStringIsImmutable
- _OBJC_IVAR_$_OSAOsLogPackParser._modulePathForImmutableMemoryPointer
- _OBJC_IVAR_$_OSAOsLogPackParser._pointerPointsToImmutableMemory
- _OBJC_IVAR_$_OSAParsedOsLogPart._isImmutable
- _OBJC_IVAR_$_OSAWiredMemoryInfo.wired_info
- _OBJC_IVAR_$_OSAWiredMemoryInfo.wired_info_count
- _OBJC_IVAR_$_OSAWiredMemoryInfo.zone_info
- _OBJC_IVAR_$_OSAWiredMemoryInfo.zone_info_count
- _OBJC_IVAR_$_OSAWiredMemoryInfo.zone_names
- _OBJC_IVAR_$_OSAWiredMemoryInfo.zone_names_count
- _OBJC_METACLASS_$_OSAWiredMemoryInfo
- _OSAIsACDCDevice
- _OSAIsACDCDevice.cold.1
- _OSAIsACDCDevice.isACDCDevice
- _OSAIsACDCDevice.onceToken
- _OSASandboxConsumeExtension.cold.2
- _OSASandboxConsumeExtension.cold.3
- _OSKextCopyLoadedKextInfo
- __OBJC_$_CLASS_METHODS_OSASystemConfiguration
- __OBJC_$_INSTANCE_METHODS_OSAWiredMemoryInfo
- __OBJC_$_INSTANCE_VARIABLES_OSAWiredMemoryInfo
- __OBJC_CLASS_RO_$_OSAWiredMemoryInfo
- __OBJC_METACLASS_RO_$_OSAWiredMemoryInfo
- ___32+[OSALog scanLogs:from:options:]_block_invoke.377
- ___34-[OSAWiredMemoryInfo vmRegionInfo]_block_invoke
- ___35-[OSAExclaveContainer parseKCdata:]_block_invoke.86
- ___37-[OSASystemConfiguration internalKey]_block_invoke.335
- ___37-[OSASystemConfiguration internalKey]_block_invoke.335.cold.1
- ___37-[OSASystemConfiguration internalKey]_block_invoke.335.cold.2
- ___37-[OSASystemConfiguration internalKey]_block_invoke.335.cold.3
- ___37-[OSASystemConfiguration internalKey]_block_invoke.335.cold.4
- ___39+[OSALegacyXform transformURL:options:]_block_invoke
- ___43+[OSATasking applyTasking:taskId:fromBlob:]_block_invoke.101
- ___44-[OSAReport streamContentAtLevel:withBlock:]_block_invoke.116
- ___44-[OSAReport streamContentAtLevel:withBlock:]_block_invoke.116.cold.1
- ___44-[OSAReport streamContentAtLevel:withBlock:]_block_invoke.116.cold.2
- ___61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.268
- ___61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.273
- ___61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.274
- ___61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.419
- ___OSAIsACDCDevice_block_invoke
- ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
- ___block_descriptor_60_e8_32r_e8_v12?0i8lr32l8
- ___block_descriptor_64_e8_32r_e8_v12?0i8lr32l8
- ___block_literal_global.118
- ___block_literal_global.156
- ___block_literal_global.195
- ___block_literal_global.308
- ___block_literal_global.352
- ___block_literal_global.380
- ___block_literal_global.40
- ___block_literal_global.412
- ___block_literal_global.60
- ___block_literal_global.7
- ___rtc_internal_block_invoke.63
- ___rtc_internal_block_invoke.63.cold.1
- ___rtc_internal_block_invoke.63.cold.2
- ___rtc_internal_block_invoke.63.cold.3
- ___rtc_internal_block_invoke.66
- ___rtc_internal_block_invoke.66.cold.1
- __os_feature_enabled_impl
- _checkMCFeature
- _checkMCFeature.dylib_handle
- _checkMCFeature.profileConnectionObj
- _isInternal
- _objc_msgSend$getCounterNameForSite:
- _objc_msgSend$getDefaultTasking
- _objc_msgSend$getTagNameForSite:
- _objc_msgSend$initWithIntegerArgumentStringValue:
- _objc_msgSend$initWithLiteral:isImmutable:
- _objc_msgSend$initWithStringArgument:isImmutable:
- _objc_msgSend$initWithSymbol:
- _objc_msgSend$isImmutable
- _objc_msgSend$normalizeInstructions:
- _objc_msgSend$removeObjectsInArray:
- _objc_msgSend$setCRKeyToRandomValue
- _objc_msgSend$shouldApplyPreference:
- _optIn3rdParty.featureAppAnalyticsAllowed
- _optInApple.featureDiagnosticsSubmissionAllowed
- _samplingKey
- _samplingKeyCString
- _seedFeedbackPromptingEnabled
CStrings:
+ "%@\n%@%@\n%@\n"
+ "%@ could not be safely opened"
+ "%@-seed"
+ "%hhd"
+ "%hhu"
+ "/private/var/containers"
+ "/private/var/mnt"
+ "/private/var/mobile"
+ "0x%llx"
+ "<null>"
+ "@20@0:8i16"
+ "@32@0:8@16r*24"
+ "@44@0:8Q16Q24[16C]32i40"
+ "ApplePMGR"
+ "AppleSoCMisc"
+ "B32@0:8@16r*24"
+ "Carrier"
+ "CarrierSeed"
+ "Cleaning up retired logs (in %@)"
+ "DnUOverride"
+ "Error reading file stream"
+ "Error reading report %{public}s: %s"
+ "Error: bug_type key not found in report header"
+ "Failed override mount path: current root paths did not start with expected prefixes"
+ "Failed override mount path: failed to generate new root paths"
+ "Failed to call getBootProgressRegisterMethod with error: 0x%x"
+ "Failed to convert to header to json"
+ "Failed to get attrs for retired log '%@': %@"
+ "Failed to get the data vault submission path."
+ "Failed to get the home directory submission path for %{private}@."
+ "Failed to get the root submission path."
+ "Failed to open service %@ with error: 0x%x"
+ "Failed to override opt-in for '%@' log: option not supported when moving a log"
+ "Failed to read developer mode status: %{darwin.errno}d"
+ "Failed to remove old log '%@': %@"
+ "Failed to remove retired log '%@': %@"
+ "Failed to retrieve creation date from %@: %@"
+ "Failed to update header as the provided data is not valid JSON"
+ "JIT"
+ "JSON ERROR: %s, payload:\n%s"
+ "LockdownModeManager"
+ "Logfile '%{public}@' not submittable on opted out device"
+ "Logfile '%{public}@' tagged DoNotSubmit"
+ "Mount path can only be overridden in the device recovery environment"
+ "No matching service found"
+ "Removing old log '%@'"
+ "Removing old retired log '%@'"
+ "Report data has unexpected number of elements: %ld"
+ "Seed"
+ "Skipping log limit check on proxy-configured device with disableLogLimits set"
+ "Skipping transfer from proxy-configured device with disablePushOnWrite set"
+ "Successfully overrode mount path. New root path: %@. New container root path: %@"
+ "T@\"NSString\",R,C,V_argSpecifier"
+ "T@\"NSString\",R,V_hwModel"
+ "T@\"NSString\",R,V_legacyAutomatedDeviceGroup"
+ "T@\"NSString\",R,V_recoveryModeReason"
+ "T@?,C,V_modulePathForMemoryPointer"
+ "T@?,C,V_pointerPointsToSafeMemory"
+ "TB,N,R"
+ "TB,R,V_isInDeviceRecoveryEnvironment"
+ "TB,R,V_isSafe"
+ "TB,V_formatStringIsSafe"
+ "TQ,R,N,V_maxNumArguments"
+ "Terminated by Unblock framework for not recovering after hitting thread limit"
+ "Terminated by Unblock framework for unrecoverable deadlock"
+ "Thread:%@; Address space info does exist for asid %@"
+ "Thread:%@; Layout info does not exist for layout id %@"
+ "Unable to convert body stream to data"
+ "Unable to load ManagedConfiguration, falling back to MobileGestalt"
+ "Unable to retrieve file attributes at path %@. Error: %@"
+ "^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}"
+ "^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}28@0:8I16^@20"
+ "_TtC11OSAnalytics11DeviceState"
+ "_TtC11OSAnalytics24WatchdogExitReasonHelper"
+ "_TtC11OSAnalytics9IPSReport"
+ "_argSpecifier"
+ "_formatStringIsSafe"
+ "_hwModel"
+ "_isInDeviceRecoveryEnvironment"
+ "_isSafe"
+ "_legacyAutomatedDeviceGroup"
+ "_maxNumArguments"
+ "_modulePathForMemoryPointer"
+ "_pointerPointsToSafeMemory"
+ "_recoveryModeReason"
+ "addJITImage:size:"
+ "argSpecifier"
+ "body"
+ "boolValForMCSetting:"
+ "bootProgressRegister"
+ "ca1-ohttp"
+ "com.apple.app-sandbox.read-write"
+ "conclave-limit"
+ "containers"
+ "containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist"
+ "createRetiredDirectoriesForUser:"
+ "customerFused"
+ "descriptionFromCode:"
+ "developerMode"
+ "device_in_recovery_mode_with_reason"
+ "disableLogLimits"
+ "disablePushOnWrite"
+ "enabled"
+ "filterOutSensitiveParts:withFormats:"
+ "formatStringIsSafe"
+ "headerJson"
+ "hhd"
+ "hhu"
+ "hwModel"
+ "include-hidden"
+ "indexOfObject:"
+ "initAlertDelegate"
+ "initWithArgument:argSpecifier:isSafe:"
+ "initWithLiteral:isSafe:"
+ "initWithMaxNumAruments:"
+ "initWithSource:size:for:source:"
+ "initWithString:"
+ "initWithSymbol:source:"
+ "isCustomerFused"
+ "isDeveloperMode"
+ "isInDeviceRecoveryEnvironment"
+ "isInLDM"
+ "isSafe"
+ "isSafe: %d, isArgument: %d, stringValue: %@"
+ "isSecurityResearchDeviceERM"
+ "ldm"
+ "legacyAutomatedDeviceGroup"
+ "long-idle-exit"
+ "maxNumArguments"
+ "modulePathForMemoryPointer"
+ "monitoring timed out for service without diags"
+ "normalizeInstructions:forSamplingKey:"
+ "optinOverride"
+ "overrideMountPath"
+ "pointerPointsToSafeMemory"
+ "r*16@0:8"
+ "randomizedCRKey"
+ "recoveryModeReason"
+ "rejected-doNotSubmit"
+ "rejected-optout"
+ "resampledUserFrames might be missing second-to-leaf frame"
+ "restrictedBool"
+ "runawayMitigation"
+ "samplingKey"
+ "scan: including '%@' (explicitly added)"
+ "scan: skipping '%@': failed to find a matching routing"
+ "scan: skipping '%@': hit log limit"
+ "security.mac.amfi.developer_mode_status"
+ "seed"
+ "setFormatStringIsSafe:"
+ "setModulePathForMemoryPointer:"
+ "setPointerPointsToSafeMemory:"
+ "shared"
+ "sharedMCProfileConnection"
+ "shouldApplyPreference:forSamplingKey:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode"
+ "softlink:o:path:/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration"
+ "stringByReplacingPathBeforeComponent:with:"
+ "stringWithCString:encoding:"
+ "submission_from_recovery_mode_with_reason"
+ "transformURL:template:options:"
+ "unknown reason"
+ "v32@0:8Q16Q24"
- "\r"
- "%@%@%@\n%@\n"
- "/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration"
- "@52@0:8^{mach_zone_name=[80c]}16I24^{mach_zone_info_data=QQQQQQQQ}28I36^{mach_memory_info=QQQQQQQQSS[2S][3Q][80c]}40I48"
- "Address space info does exist for asid %@"
- "Cleaning up retired logs (in %{public}@)"
- "Device is an ACDC compute module"
- "Failed to get attrs for retired log '%{public}@': %{public}@"
- "Failed to remove old log '%{public}@': %{public}@"
- "Failed to remove retired log '%{public}@': %{public}@"
- "Failed to retrieve creation date from %{public}@: %{public}@"
- "GM"
- "HWModelStr"
- "Layout info does not exist for layout id %@"
- "OSAWiredMemoryInfo"
- "OSBundleLoadTag"
- "Removing old log '%{public}@'"
- "Removing old retired log '%{public}@'"
- "T@?,C,V_modulePathForImmutableMemoryPointer"
- "T@?,C,V_pointerPointsToImmutableMemory"
- "TB,R,V_isImmutable"
- "TB,V_formatStringIsImmutable"
- "Unable to find class MCProfileConnection"
- "Unable to load ManagedConfiguration dylib ('%s')"
- "Unable to load symbol %s"
- "Unable to retrieve file attributes at path %@. Error: %d %s"
- "VM_KERN_COUNT_%lld"
- "VM_KERN_COUNT_BOOT_STOLEN"
- "VM_KERN_COUNT_LOPAGE"
- "VM_KERN_COUNT_MANAGED"
- "VM_KERN_COUNT_MAP_KALLOC"
- "VM_KERN_COUNT_MAP_KALLOC_LARGE_DATA"
- "VM_KERN_COUNT_MAP_KERNEL"
- "VM_KERN_COUNT_MAP_KERNEL_DATA"
- "VM_KERN_COUNT_MAP_ZONE"
- "VM_KERN_COUNT_RESERVED"
- "VM_KERN_COUNT_STOLEN"
- "VM_KERN_COUNT_WIRED"
- "VM_KERN_COUNT_WIRED_BOOT"
- "VM_KERN_COUNT_WIRED_MANAGED"
- "VM_KERN_COUNT_WIRED_STATIC_KERNELCACHE"
- "VM_KERN_MEMORY_%lld"
- "VM_KERN_MEMORY_34"
- "VM_KERN_MEMORY_ANY"
- "VM_KERN_MEMORY_BSD"
- "VM_KERN_MEMORY_COMPRESSED_DATA"
- "VM_KERN_MEMORY_COMPRESSOR"
- "VM_KERN_MEMORY_COUNT"
- "VM_KERN_MEMORY_CPU"
- "VM_KERN_MEMORY_DIAG"
- "VM_KERN_MEMORY_EXCLAVES"
- "VM_KERN_MEMORY_FILE"
- "VM_KERN_MEMORY_FIRST_DYNAMIC"
- "VM_KERN_MEMORY_HV"
- "VM_KERN_MEMORY_IOKIT"
- "VM_KERN_MEMORY_IPC"
- "VM_KERN_MEMORY_KALLOC"
- "VM_KERN_MEMORY_KALLOC_DATA"
- "VM_KERN_MEMORY_KALLOC_TYPE"
- "VM_KERN_MEMORY_KEXT"
- "VM_KERN_MEMORY_LIBKERN"
- "VM_KERN_MEMORY_LOG"
- "VM_KERN_MEMORY_LTABLE"
- "VM_KERN_MEMORY_MBUF"
- "VM_KERN_MEMORY_MLOCK"
- "VM_KERN_MEMORY_NONE"
- "VM_KERN_MEMORY_OSFMK"
- "VM_KERN_MEMORY_OSKEXT"
- "VM_KERN_MEMORY_PHANTOM_CACHE"
- "VM_KERN_MEMORY_PMAP"
- "VM_KERN_MEMORY_PTE"
- "VM_KERN_MEMORY_REASON"
- "VM_KERN_MEMORY_RECOUNT"
- "VM_KERN_MEMORY_RETIRED"
- "VM_KERN_MEMORY_SECURITY"
- "VM_KERN_MEMORY_SKYWALK"
- "VM_KERN_MEMORY_STACK"
- "VM_KERN_MEMORY_TRIAGE"
- "VM_KERN_MEMORY_UBC"
- "VM_KERN_MEMORY_WAITQ"
- "VM_KERN_MEMORY_ZONE"
- "^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQ}]}"
- "^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQ}]}28@0:8I16^@20"
- "^{mach_memory_info=QQQQQQQQSS[2S][3Q][80c]}"
- "^{mach_zone_info_data=QQQQQQQQ}"
- "^{mach_zone_name=[80c]}"
- "_formatStringIsImmutable"
- "_isImmutable"
- "_modulePathForImmutableMemoryPointer"
- "_pointerPointsToImmutableMemory"
- "alloc_size"
- "collectable"
- "collectable_bytes"
- "com.apple.OSAnalytics.DiagnosticsReporter"
- "com.apple.osanalytics-sandbox.read-write"
- "elem_size"
- "enableDataVault"
- "exhaustible"
- "filterOutSensitiveStrings:"
- "forceSeedFeedbackPrompting"
- "formatStringIsImmutable"
- "getCounterNameForSite:"
- "getDefaultTasking"
- "getTagNameForSite:"
- "initWithIntegerArgumentStringValue:"
- "initWithLiteral:isImmutable:"
- "initWithStringArgument:isImmutable:"
- "initWithSymbol:"
- "isImmutable"
- "isImmutable: %d, isArgument: %d, stringValue: %@"
- "largest"
- "mapped"
- "max_size"
- "modulePathForImmutableMemoryPointer"
- "normalizeInstructions:"
- "peak"
- "pointerPointsToImmutableMemory"
- "removeObjectsInArray:"
- "samplingKey is good"
- "setCRKeyToRandomValue"
- "setFormatStringIsImmutable:"
- "setModulePathForImmutableMemoryPointer:"
- "setPointerPointsToImmutableMemory:"
- "shouldApplyPreference:"
- "site"
- "sum_size"
- "wired_info"
- "wired_info_count"
- "zone_info"
- "zone_info_count"
- "zone_names"
- "zone_names_count"

```
