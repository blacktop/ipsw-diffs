## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5359.4.17.100.0
-  __TEXT.__text: 0x40c28
+5369.0.0.0.0
+  __TEXT.__text: 0x456bc
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x3c6c
+  __TEXT.__objc_methlist: 0x411c
   __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0xf30
-  __TEXT.__oslogstring: 0x5829
-  __TEXT.__cstring: 0x2b8e
-  __TEXT.__dlopen_cstrs: 0x1245
-  __TEXT.__unwind_info: 0x1190
-  __TEXT.__objc_classname: 0x7ce
-  __TEXT.__objc_methname: 0xa82f
-  __TEXT.__objc_methtype: 0x113b
-  __TEXT.__objc_stubs: 0x7f20
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0x1618
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __TEXT.__gcc_except_tab: 0x10b8
+  __TEXT.__oslogstring: 0x593a
+  __TEXT.__cstring: 0x3029
+  __TEXT.__dlopen_cstrs: 0x138b
+  __TEXT.__ustring: 0x12
+  __TEXT.__unwind_info: 0x12f8
+  __TEXT.__objc_classname: 0x8ca
+  __TEXT.__objc_methname: 0xb199
+  __TEXT.__objc_methtype: 0x1254
+  __TEXT.__objc_stubs: 0x8900
+  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__const: 0x1730
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2960
+  __DATA_CONST.__objc_selrefs: 0x2bf8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x178
   __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0x2fa0
-  __AUTH_CONST.__objc_const: 0x5c08
-  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__const: 0xaa0
+  __AUTH_CONST.__cfstring: 0x36a0
+  __AUTH_CONST.__objc_const: 0x61a8
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x3a8
-  __DATA.__data: 0x970
-  __DATA.__bss: 0x5c0
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x3c4
+  __DATA.__data: 0xa90
+  __DATA.__bss: 0x608
   __DATA_DIRTY.__objc_data: 0xeb0
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CBE8398-278C-3D08-98FF-21FFC16911A8
-  Functions: 1667
-  Symbols:   6181
-  CStrings:  3401
+  UUID: B1164E00-A368-3CF5-92B4-3D0271DD32C4
+  Functions: 1773
+  Symbols:   6497
+  CStrings:  3643
 
Symbols:
+ +[BYExpressCloudSettings _iPadMultitaskingMode]
+ +[BYSUManagerClient createWithQueue:clientType:]
+ +[BYSUManagerClientTestingSurrogate enabled]
+ +[BYTestingSurrogateBehavior updateWithDictionary:]
+ +[BYTestingSurrogateBehaviorManager sharedInstance]
+ +[BuddyOverrideUtilities _defaultValueFor:]
+ +[BuddyOverrideUtilities buildSupportsOverrides]
+ +[BuddyOverrideUtilities dictionaryByMerging:with:]
+ +[BuddyOverrideUtilities keyForOverrideEntry:]
+ +[BuddyOverrideUtilities keyForSourceDeviceOverrideEntry:]
+ +[BuddyOverrideUtilities mergeIntoOverridesDictionary:]
+ +[BuddyOverrideUtilities overridePreferences]
+ +[BuddyOverrideUtilities setOverrideEntryFor:shouldOverride:]
+ +[BuddyOverrideUtilities setSourceDeviceValueEntryFor:value:]
+ +[BuddyOverrideUtilities sourceDeviceValueFor:]
+ +[BuddyOverrideUtilities useOverridesFor:]
+ -[BFFSettingsManager _restoreIPadMultitaskingMode]
+ -[BFFSettingsManager setIPadMultitaskingMode:]
+ -[BYBuddyDaemonGeneralClient lockScreenMode]
+ -[BYBuddyDaemonGeneralClient setLockScreenMode:]
+ -[BYChronicle setProductVersion:forFeature:]
+ -[BYSUManagerClient .cxx_destruct]
+ -[BYSUManagerClient cancelDownload:]
+ -[BYSUManagerClient enableAutomaticDownload:]
+ -[BYSUManagerClient enableAutomaticUpdateV2:]
+ -[BYSUManagerClient getMandatorySoftwareUpdateDictionary:]
+ -[BYSUManagerClient initWithQueue:clientType:]
+ -[BYSUManagerClient isAutomaticDownloadEnabled]
+ -[BYSUManagerClient isAutomaticUpdateV2Enabled]
+ -[BYSUManagerClient scanForUpdates:withScanResults:]
+ -[BYSUManagerClient setMandatorySoftwareUpdateDictionary:]
+ -[BYSUManagerClient setUnderlyingManagerClient:]
+ -[BYSUManagerClient underlyingManagerClient]
+ -[BYSUManagerClientTestingSurrogate .cxx_destruct]
+ -[BYSUManagerClientTestingSurrogate behaviorManager]
+ -[BYSUManagerClientTestingSurrogate cancelDownload:]
+ -[BYSUManagerClientTestingSurrogate enableAutomaticDownload:]
+ -[BYSUManagerClientTestingSurrogate enableAutomaticUpdateV2:]
+ -[BYSUManagerClientTestingSurrogate getMandatorySoftwareUpdateDictionary:]
+ -[BYSUManagerClientTestingSurrogate initWithQueue:clientType:]
+ -[BYSUManagerClientTestingSurrogate isAutomaticDownloadEnabled]
+ -[BYSUManagerClientTestingSurrogate isAutomaticUpdateV2Enabled]
+ -[BYSUManagerClientTestingSurrogate queue]
+ -[BYSUManagerClientTestingSurrogate scanForUpdates:withScanResults:]
+ -[BYSUManagerClientTestingSurrogate setBehaviorManager:]
+ -[BYSUManagerClientTestingSurrogate setMandatorySoftwareUpdateDictionary:]
+ -[BYSUManagerClientTestingSurrogate setQueue:]
+ -[BYTestingSurrogateBehavior .cxx_destruct]
+ -[BYTestingSurrogateBehavior alternateUpdate]
+ -[BYTestingSurrogateBehavior duration]
+ -[BYTestingSurrogateBehavior error]
+ -[BYTestingSurrogateBehavior preferredUpdate]
+ -[BYTestingSurrogateBehavior resultsAsBasicBoolean]
+ -[BYTestingSurrogateBehavior results]
+ -[BYTestingSurrogateBehavior scanResults]
+ -[BYTestingSurrogateBehavior setDuration:]
+ -[BYTestingSurrogateBehavior setError:]
+ -[BYTestingSurrogateBehavior setResults:]
+ -[BYTestingSurrogateBehavior setResultsAsBasicBoolean:]
+ -[BYTestingSurrogateBehaviorManager _addBehaviorsFromConfigurationFilesIfNecessary]
+ -[BYTestingSurrogateBehaviorManager _allDomains]
+ -[BYTestingSurrogateBehaviorManager _behaviorDictionaryFromBehavior:count:]
+ -[BYTestingSurrogateBehaviorManager _behaviorFromBehaviorDictionary:returningCount:]
+ -[BYTestingSurrogateBehaviorManager _behaviorFromBehaviorsArray:returningCount:]
+ -[BYTestingSurrogateBehaviorManager _behaviorsForDomain:behaviorName:]
+ -[BYTestingSurrogateBehaviorManager _enabledForDomain:]
+ -[BYTestingSurrogateBehaviorManager _hasEnabledValueForDomain:]
+ -[BYTestingSurrogateBehaviorManager _preferenceKeyForDomain:behaviorName:]
+ -[BYTestingSurrogateBehaviorManager _preferenceKeyForEnablementOfDomain:]
+ -[BYTestingSurrogateBehaviorManager _setBehaviors:forDomain:behaviorName:]
+ -[BYTestingSurrogateBehaviorManager _setEnabled:forDomain:]
+ -[BYTestingSurrogateBehaviorManager _setNamedBehaviorsFromDictionary:forDomain:]
+ -[BYTestingSurrogateBehaviorManager acquireNextBehaviorWithName:domain:]
+ -[BYTestingSurrogateBehaviorManager acquireNextBehaviorWithName:domain:].cold.1
+ -[BYTestingSurrogateBehaviorManager addBehavior:withName:domain:count:replacingAllOthers:]
+ -[BYTestingSurrogateBehaviorManager domainSoftwareUpdate]
+ -[BYTestingSurrogateBehaviorManager enabledForDomain:]
+ -[BYTestingSurrogateBehaviorManager init]
+ -[BuddyFeatureFlags isSolariumEnabled]
+ GCC_except_table108
+ GCC_except_table18
+ GCC_except_table26
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table46
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table60
+ GCC_except_table67
+ GCC_except_table71
+ _BYBuddyRunMDMMigrationAfterSoftwareUpdateMiniBuddy
+ _BYSetupAssistantLockScreenMode
+ _OBJC_CLASS_$_BYSUManagerClient
+ _OBJC_CLASS_$_BYSUManagerClientTestingSurrogate
+ _OBJC_CLASS_$_BYTestingSurrogateBehavior
+ _OBJC_CLASS_$_BYTestingSurrogateBehaviorManager
+ _OBJC_CLASS_$_BuddyOverrideUtilities
+ _OBJC_IVAR_$_BFFSettingsManager._stashedIPadMultitaskingMode
+ _OBJC_IVAR_$_BYSUManagerClient._underlyingManagerClient
+ _OBJC_IVAR_$_BYSUManagerClientTestingSurrogate._behaviorManager
+ _OBJC_IVAR_$_BYSUManagerClientTestingSurrogate._queue
+ _OBJC_IVAR_$_BYTestingSurrogateBehavior._duration
+ _OBJC_IVAR_$_BYTestingSurrogateBehavior._error
+ _OBJC_IVAR_$_BYTestingSurrogateBehavior._results
+ _OBJC_METACLASS_$_BYSUManagerClient
+ _OBJC_METACLASS_$_BYSUManagerClientTestingSurrogate
+ _OBJC_METACLASS_$_BYTestingSurrogateBehavior
+ _OBJC_METACLASS_$_BYTestingSurrogateBehaviorManager
+ _OBJC_METACLASS_$_BuddyOverrideUtilities
+ _SASProximityDeviceToDeviceCurrentVersion
+ _SoftwareUpdateServicesLibrary
+ _ThreatNotificationUILibraryCore.frameworkLibrary
+ _UIKitLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_BYSUManagerClient
+ __OBJC_$_CLASS_METHODS_BYSUManagerClientTestingSurrogate
+ __OBJC_$_CLASS_METHODS_BYTestingSurrogateBehavior
+ __OBJC_$_CLASS_METHODS_BYTestingSurrogateBehaviorManager
+ __OBJC_$_CLASS_METHODS_BuddyOverrideUtilities
+ __OBJC_$_INSTANCE_METHODS_BYSUManagerClient
+ __OBJC_$_INSTANCE_METHODS_BYSUManagerClientTestingSurrogate
+ __OBJC_$_INSTANCE_METHODS_BYTestingSurrogateBehavior
+ __OBJC_$_INSTANCE_METHODS_BYTestingSurrogateBehaviorManager
+ __OBJC_$_INSTANCE_VARIABLES_BYSUManagerClient
+ __OBJC_$_INSTANCE_VARIABLES_BYSUManagerClientTestingSurrogate
+ __OBJC_$_INSTANCE_VARIABLES_BYTestingSurrogateBehavior
+ __OBJC_$_PROP_LIST_BYSUManagerClient
+ __OBJC_$_PROP_LIST_BYSUManagerClientTestingSurrogate
+ __OBJC_$_PROP_LIST_BYTestingSurrogateBehavior
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BYDaemonProximityBaseTargetProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BYDaemonProximityTargetClientConnectionProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BYDaemonProximityTargetClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BYSUManagerClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BYDaemonProximityBaseTargetProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BYDaemonProximityTargetClientConnectionProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BYDaemonProximityTargetClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BYSUManagerClientProtocol
+ __OBJC_$_PROTOCOL_REFS_BYDaemonProximityBaseTargetProtocol
+ __OBJC_$_PROTOCOL_REFS_BYDaemonProximityTargetClientConnectionProtocol
+ __OBJC_$_PROTOCOL_REFS_BYDaemonProximityTargetClientProtocol
+ __OBJC_$_PROTOCOL_REFS_BYSUManagerClientProtocol
+ __OBJC_CLASS_PROTOCOLS_$_BYSUManagerClient
+ __OBJC_CLASS_PROTOCOLS_$_BYSUManagerClientTestingSurrogate
+ __OBJC_CLASS_RO_$_BYSUManagerClient
+ __OBJC_CLASS_RO_$_BYSUManagerClientTestingSurrogate
+ __OBJC_CLASS_RO_$_BYTestingSurrogateBehavior
+ __OBJC_CLASS_RO_$_BYTestingSurrogateBehaviorManager
+ __OBJC_CLASS_RO_$_BuddyOverrideUtilities
+ __OBJC_LABEL_PROTOCOL_$_BYDaemonProximityBaseTargetProtocol
+ __OBJC_LABEL_PROTOCOL_$_BYDaemonProximityTargetClientConnectionProtocol
+ __OBJC_LABEL_PROTOCOL_$_BYDaemonProximityTargetClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_BYSUManagerClientProtocol
+ __OBJC_METACLASS_RO_$_BYSUManagerClient
+ __OBJC_METACLASS_RO_$_BYSUManagerClientTestingSurrogate
+ __OBJC_METACLASS_RO_$_BYTestingSurrogateBehavior
+ __OBJC_METACLASS_RO_$_BYTestingSurrogateBehaviorManager
+ __OBJC_METACLASS_RO_$_BuddyOverrideUtilities
+ __OBJC_PROTOCOL_$_BYDaemonProximityBaseTargetProtocol
+ __OBJC_PROTOCOL_$_BYDaemonProximityTargetClientConnectionProtocol
+ __OBJC_PROTOCOL_$_BYDaemonProximityTargetClientProtocol
+ __OBJC_PROTOCOL_$_BYSUManagerClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_BYDaemonProximityTargetClientConnectionProtocol
+ ___120-[BYAppleIDAccountsManager repeatedlyAttemptPostRestoreRenewForAccount:loginContext:numberOfAttemptsAllowed:completion:]_block_invoke.48
+ ___123-[BYAppleIDAccountsManager loginDelegateAccountsWithUsername:password:rawPassword:skipiTunes:onlyAppleIDPlugin:completion:]_block_invoke.36
+ ___123-[BYAppleIDAccountsManager loginDelegateAccountsWithUsername:password:rawPassword:skipiTunes:onlyAppleIDPlugin:completion:]_block_invoke.43
+ ___44-[BYBuddyDaemonGeneralClient backupMetadata]_block_invoke.43
+ ___44-[BYBuddyDaemonGeneralClient lockScreenMode]_block_invoke
+ ___44-[BYBuddyDaemonGeneralClient lockScreenMode]_block_invoke.26
+ ___47-[BYBuddyDaemonGeneralClient _daemonConnection]_block_invoke.167
+ ___48-[BYBuddyDaemonGeneralClient setLockScreenMode:]_block_invoke
+ ___51+[BuddyOverrideUtilities dictionaryByMerging:with:]_block_invoke
+ ___51-[BYBuddyDaemonGeneralClient deferDataMigratorExit]_block_invoke.57
+ ___52-[BYSUManagerClientTestingSurrogate cancelDownload:]_block_invoke
+ ___53-[BYBuddyDaemonProximityTargetClient connectToDaemon]_block_invoke.94
+ ___54-[BYBuddyDaemonGeneralClient ensureSilentLoginUpgrade]_block_invoke.32
+ ___54-[BYBuddyDaemonGeneralClient performSilentICDPUpgrade]_block_invoke.52
+ ___56-[BYBuddyDaemonGeneralClient observeFinishSetupTriggers]_block_invoke.47
+ ___58-[BYBuddyDaemonGeneralClient ensureShortLivedTokenUpgrade]_block_invoke.38
+ ___60-[BYBuddyDaemonGeneralClient cancelDataMigratorDeferredExit]_block_invoke.62
+ ___65-[BYBuddyDaemonProximityTargetClient fileTransferSessionTemplate]_block_invoke.110
+ ___67-[BYBuddyDaemonGeneralClient fetchAuthenticationContextForApplePay]_block_invoke.77
+ ___68-[BYBuddyDaemonGeneralClient fetchAuthenticationContextForBiometric]_block_invoke.86
+ ___68-[BYBuddyDaemonGeneralClient storeAuthenticationContextforApplyPay:]_block_invoke.72
+ ___68-[BYSUManagerClientTestingSurrogate scanForUpdates:withScanResults:]_block_invoke
+ ___69-[BYBuddyDaemonGeneralClient storeAuthenticationContextforBiometric:]_block_invoke.81
+ ___74-[BYSUManagerClientTestingSurrogate getMandatorySoftwareUpdateDictionary:]_block_invoke
+ ___83-[BYBuddyDaemonGeneralClient enrollInSeedProgramNamed:withAssetAudience:programID:]_block_invoke.67
+ ___BYDaemonCreateMetadataArchive_block_invoke.319
+ ___BYSetLaunchSentinel_block_invoke
+ ___BYSetupAssistantCreateAuthContext_block_invoke.185
+ ___Daemon_BYSetupAssistantNeedsToRun_block_invoke.150
+ ___ThreatNotificationUILibraryCore_block_invoke
+ ___UIKitLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e8_v16?0Q8lr32l8
+ ___block_descriptor_56_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_literal_global.101
+ ___block_literal_global.107
+ ___block_literal_global.147
+ ___block_literal_global.157
+ ___block_literal_global.175
+ ___block_literal_global.188
+ ___block_literal_global.198
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.37
+ ___block_literal_global.42
+ ___block_literal_global.46
+ ___block_literal_global.49
+ ___block_literal_global.51
+ ___block_literal_global.54
+ ___block_literal_global.56
+ ___block_literal_global.59
+ ___block_literal_global.61
+ ___block_literal_global.69
+ ___block_literal_global.71
+ ___block_literal_global.76
+ ___block_literal_global.80
+ ___block_literal_global.83
+ ___block_literal_global.85
+ ___block_literal_global.88
+ ___block_literal_global.90
+ ___block_literal_global.96
+ ___getSBSBuddyMultitaskingFlowClass_block_invoke
+ ___getSBSBuddyMultitaskingFlowClass_block_invoke.cold.1
+ ___getSUDescriptorClass_block_invoke
+ ___getSUDescriptorClass_block_invoke.cold.1
+ ___getSUScanResultsClass_block_invoke
+ ___getSUScanResultsClass_block_invoke.cold.1
+ ___getTNUIOnBoardingFlowClass_block_invoke
+ ___getTNUIOnBoardingFlowClass_block_invoke.cold.1
+ ___getUIDeviceClass_block_invoke
+ ___getUIDeviceClass_block_invoke.cold.1
+ _audit_stringThreatNotificationUI
+ _audit_stringUIKit
+ _getSBSBuddyMultitaskingFlowClass.softClass
+ _getSUDescriptorClass.softClass
+ _getSUScanResultsClass.softClass
+ _getTNUIOnBoardingFlowClass
+ _getTNUIOnBoardingFlowClass.softClass
+ _getUIDeviceClass
+ _getUIDeviceClass.softClass
+ _objc_msgSend$_addBehaviorsFromConfigurationFilesIfNecessary
+ _objc_msgSend$_allDomains
+ _objc_msgSend$_behaviorDictionaryFromBehavior:count:
+ _objc_msgSend$_behaviorFromBehaviorDictionary:returningCount:
+ _objc_msgSend$_behaviorFromBehaviorsArray:returningCount:
+ _objc_msgSend$_behaviorsForDomain:behaviorName:
+ _objc_msgSend$_defaultValueFor:
+ _objc_msgSend$_enabledForDomain:
+ _objc_msgSend$_hasEnabledValueForDomain:
+ _objc_msgSend$_iPadMultitaskingMode
+ _objc_msgSend$_preferenceKeyForDomain:behaviorName:
+ _objc_msgSend$_preferenceKeyForEnablementOfDomain:
+ _objc_msgSend$_restoreIPadMultitaskingMode
+ _objc_msgSend$_setBehaviors:forDomain:behaviorName:
+ _objc_msgSend$_setEnabled:forDomain:
+ _objc_msgSend$_setError
+ _objc_msgSend$_setNamedBehaviorsFromDictionary:forDomain:
+ _objc_msgSend$acquireNextBehaviorWithName:domain:
+ _objc_msgSend$addBehavior:withName:domain:count:replacingAllOthers:
+ _objc_msgSend$alternateUpdate
+ _objc_msgSend$behaviorManager
+ _objc_msgSend$buildSupportsOverrides
+ _objc_msgSend$cancelDownload:
+ _objc_msgSend$createWithQueue:clientType:
+ _objc_msgSend$currentDevice
+ _objc_msgSend$currentMultitaskingOption
+ _objc_msgSend$dictionaryByMerging:with:
+ _objc_msgSend$domainSoftwareUpdate
+ _objc_msgSend$duration
+ _objc_msgSend$enabled
+ _objc_msgSend$enabledForDomain:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getMandatorySoftwareUpdateDictionary:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithPreferredDescriptor:alternateDescriptor:
+ _objc_msgSend$initWithQueue:clientType:
+ _objc_msgSend$isLDMEnabledOnBoardingViewControllerRequired
+ _objc_msgSend$keyForOverrideEntry:
+ _objc_msgSend$keyForSourceDeviceOverrideEntry:
+ _objc_msgSend$lockScreenMode
+ _objc_msgSend$lockScreenMode:
+ _objc_msgSend$mergeIntoOverridesDictionary:
+ _objc_msgSend$overridePreferences
+ _objc_msgSend$position
+ _objc_msgSend$preferredUpdate
+ _objc_msgSend$results
+ _objc_msgSend$resultsAsBasicBoolean
+ _objc_msgSend$scanForUpdates:withScanResults:
+ _objc_msgSend$scanResults
+ _objc_msgSend$setBehaviorManager:
+ _objc_msgSend$setCurrentMultitaskingOption:
+ _objc_msgSend$setDownloadSize:
+ _objc_msgSend$setDownloadable:
+ _objc_msgSend$setDownloadableOverCellular:
+ _objc_msgSend$setDuration:
+ _objc_msgSend$setHumanReadableUpdateName:
+ _objc_msgSend$setIPadMultitaskingMode:
+ _objc_msgSend$setLockScreenMode:
+ _objc_msgSend$setMandatorySoftwareUpdateDictionary:
+ _objc_msgSend$setMandatoryUpdateEligible:
+ _objc_msgSend$setMandatoryUpdateOptional:
+ _objc_msgSend$setMandatoryUpdateRestrictedToOutOfTheBox:
+ _objc_msgSend$setMandatoryUpdateVersionMax:
+ _objc_msgSend$setMandatoryUpdateVersionMin:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setProductBuildVersion:
+ _objc_msgSend$setProductSystemName:
+ _objc_msgSend$setProductVersionExtra:
+ _objc_msgSend$setPublisher:
+ _objc_msgSend$setResults:
+ _objc_msgSend$setResultsAsBasicBoolean:
+ _objc_msgSend$setUnderlyingManagerClient:
+ _objc_msgSend$setUpdateType:
+ _objc_msgSend$underlyingManagerClient
+ _objc_msgSend$updateWithDictionary:
+ _objc_msgSend$useOverridesFor:
+ _objc_msgSend$userInterfaceIdiom
- GCC_except_table103
- GCC_except_table35
- GCC_except_table39
- GCC_except_table48
- GCC_except_table51
- GCC_except_table54
- GCC_except_table58
- GCC_except_table61
- GCC_except_table63
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _BYPrivacySubscriptionBundleIdentifier
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BYDaemonProximityTargetProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_BYDaemonProximityTargetProtocol
- __OBJC_$_PROTOCOL_REFS_BYDaemonProximityTargetProtocol
- __OBJC_LABEL_PROTOCOL_$_BYDaemonProximityTargetProtocol
- __OBJC_PROTOCOL_$_BYDaemonProximityTargetProtocol
- __OBJC_PROTOCOL_REFERENCE_$_BYDaemonProximityTargetProtocol
- ___120-[BYAppleIDAccountsManager repeatedlyAttemptPostRestoreRenewForAccount:loginContext:numberOfAttemptsAllowed:completion:]_block_invoke.45
- ___123-[BYAppleIDAccountsManager loginDelegateAccountsWithUsername:password:rawPassword:skipiTunes:onlyAppleIDPlugin:completion:]_block_invoke.33
- ___123-[BYAppleIDAccountsManager loginDelegateAccountsWithUsername:password:rawPassword:skipiTunes:onlyAppleIDPlugin:completion:]_block_invoke.40
- ___44-[BYBuddyDaemonGeneralClient backupMetadata]_block_invoke.37
- ___47-[BYBuddyDaemonGeneralClient _daemonConnection]_block_invoke.157
- ___51-[BYBuddyDaemonGeneralClient deferDataMigratorExit]_block_invoke.51
- ___53-[BYBuddyDaemonProximityTargetClient connectToDaemon]_block_invoke.93
- ___54-[BYBuddyDaemonGeneralClient ensureSilentLoginUpgrade]_block_invoke.26
- ___54-[BYBuddyDaemonGeneralClient performSilentICDPUpgrade]_block_invoke.46
- ___56-[BYBuddyDaemonGeneralClient observeFinishSetupTriggers]_block_invoke.41
- ___58-[BYBuddyDaemonGeneralClient ensureShortLivedTokenUpgrade]_block_invoke.32
- ___60-[BYBuddyDaemonGeneralClient cancelDataMigratorDeferredExit]_block_invoke.56
- ___65-[BYBuddyDaemonProximityTargetClient fileTransferSessionTemplate]_block_invoke.109
- ___67-[BYBuddyDaemonGeneralClient fetchAuthenticationContextForApplePay]_block_invoke.71
- ___68-[BYBuddyDaemonGeneralClient fetchAuthenticationContextForBiometric]_block_invoke.80
- ___68-[BYBuddyDaemonGeneralClient storeAuthenticationContextforApplyPay:]_block_invoke.66
- ___69-[BYBuddyDaemonGeneralClient storeAuthenticationContextforBiometric:]_block_invoke.75
- ___83-[BYBuddyDaemonGeneralClient enrollInSeedProgramNamed:withAssetAudience:programID:]_block_invoke.61
- ___BYDaemonCreateMetadataArchive_block_invoke.313
- ___BYSetupAssistantCreateAuthContext_block_invoke.178
- ___Daemon_BYSetupAssistantNeedsToRun_block_invoke.147
- ___block_literal_global.100
- ___block_literal_global.106
- ___block_literal_global.108
- ___block_literal_global.144
- ___block_literal_global.170
- ___block_literal_global.181
- ___block_literal_global.191
- ___block_literal_global.199
- ___block_literal_global.201
- ___block_literal_global.34
- ___block_literal_global.36
- ___block_literal_global.43
- ___block_literal_global.45
- ___block_literal_global.48
- ___block_literal_global.50
- ___block_literal_global.53
- ___block_literal_global.55
- ___block_literal_global.58
- ___block_literal_global.60
- ___block_literal_global.63
- ___block_literal_global.65
- ___block_literal_global.77
- ___block_literal_global.79
- ___block_literal_global.82
- ___block_literal_global.84
- ___block_literal_global.95
- _objc_msgSend$initWithDelegate:clientType:
CStrings:
+ "/AppleInternal/System/Library/"
+ "@\"BYTestingSurrogateBehaviorManager\""
+ "@\"RPFileTransferSession\"16@0:8"
+ "@\"SUManagerClient\""
+ "@28@0:8@16i24"
+ "@32@0:8@16^Q24"
+ "BYDaemonProximityBaseTargetProtocol"
+ "BYDaemonProximityTargetClientConnectionProtocol"
+ "BYDaemonProximityTargetClientProtocol"
+ "BYSUManagerClient"
+ "BYSUManagerClientProtocol"
+ "BYSUManagerClientTestingSurrogate"
+ "BYSetupAssistantNeedsToRun is YES because ThreatNotificationUI says so"
+ "BYTestingSurrogateBehavior"
+ "BYTestingSurrogateBehavior.%@.%@"
+ "BYTestingSurrogateBehaviorManager"
+ "BYTestingSurrogateEnabled.%@"
+ "BuddyOverrideUtilities"
+ "Enabling testing surrogate functionality for domain %@ with %@ behavior names"
+ "NaturalUI"
+ "No behavior specified or incorrectly specified (behavior `%@` domain '%@')"
+ "No iPad Multitasking mode"
+ "OnBoardingKit"
+ "P+\x0f\xfe "
+ "PurpleBuddy-%@.plist"
+ "SBSBuddyMultitaskingFlow"
+ "SUDescriptor"
+ "SUScanResults"
+ "Setting iPad multitasking mode %ld"
+ "ShouldRunMDMMigrationAfterSoftwareUpdateMiniBuddy"
+ "Solarium"
+ "SwiftUI"
+ "T@\"BYTestingSurrogateBehaviorManager\",&,V_behaviorManager"
+ "T@\"NSDictionary\",&,V_results"
+ "T@\"NSError\",&,V_error"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"SUManagerClient\",&,N,V_underlyingManagerClient"
+ "TNUIOnBoardingFlow"
+ "Td,V_duration"
+ "Throwing %@"
+ "UIDevice"
+ "Unspecified or malformed testing behavior"
+ "_addBehaviorsFromConfigurationFilesIfNecessary"
+ "_allDomains"
+ "_behaviorDictionaryFromBehavior:count:"
+ "_behaviorFromBehaviorDictionary:returningCount:"
+ "_behaviorFromBehaviorsArray:returningCount:"
+ "_behaviorManager"
+ "_behaviorsForDomain:behaviorName:"
+ "_defaultValueFor:"
+ "_duration"
+ "_enabledForDomain:"
+ "_hasEnabledValueForDomain:"
+ "_iPadMultitaskingMode"
+ "_preferenceKeyForDomain:behaviorName:"
+ "_preferenceKeyForEnablementOfDomain:"
+ "_restoreIPadMultitaskingMode"
+ "_results"
+ "_setBehaviors:forDomain:behaviorName:"
+ "_setEnabled:forDomain:"
+ "_setError"
+ "_setNamedBehaviorsFromDictionary:forDomain:"
+ "_stashedIPadMultitaskingMode"
+ "_underlyingManagerClient"
+ "acquireNextBehaviorWithName:domain:"
+ "addBehavior:withName:domain:count:replacingAllOthers:"
+ "alternateUpdate"
+ "apple-id"
+ "automaticDownloadEnabled"
+ "automaticUpdateV2Enabled"
+ "ax-data"
+ "behaviorManager"
+ "boolean"
+ "buildSupportsOverrides"
+ "cancelDownload"
+ "cancelDownload:"
+ "createWithQueue:clientType:"
+ "currentMultitaskingOption"
+ "d2d-version"
+ "device-class"
+ "device-name"
+ "dictionaryByMerging:with:"
+ "disable-default-values"
+ "domainSoftwareUpdate"
+ "downloadSize"
+ "downloadable"
+ "downloadableOverCellular"
+ "duration"
+ "enable-quick-start-overrides"
+ "enable-setup-overrides"
+ "enabledForDomain:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "getBytes:range:"
+ "getMandatorySoftwareUpdateDictionary:"
+ "has-passcode"
+ "hasError"
+ "humanReadableUpdateName"
+ "initWithContentsOfURL:error:"
+ "initWithPreferredDescriptor:alternateDescriptor:"
+ "initWithQueue:clientType:"
+ "isLDMEnabledOnBoardingViewControllerRequired"
+ "isSolariumEnabled"
+ "keyForOverrideEntry:"
+ "keyForSourceDeviceOverrideEntry:"
+ "languages"
+ "locale"
+ "lockScreenMode"
+ "lockScreenMode:"
+ "lockScreenMode: budd returned an error: %{public}@"
+ "mandatorySoftwareUpdateInfo"
+ "mandatoryUpdateEligible"
+ "mandatoryUpdateOptional"
+ "mandatoryUpdateRestrictedToOutOfTheBox"
+ "mandatoryUpdateVersionMax"
+ "mandatoryUpdateVersionMin"
+ "mergeIntoOverridesDictionary:"
+ "model"
+ "multitaskingModeKey"
+ "overridePreferences"
+ "overrides"
+ "passcode-type"
+ "position"
+ "preferredUpdate"
+ "product-version"
+ "productBuildVersion"
+ "productSystemName"
+ "productVersionExtra"
+ "publisher"
+ "results"
+ "resultsAsBasicBoolean"
+ "scanForUpdates"
+ "scanForUpdates:withScanResults:"
+ "scanResults"
+ "setBehaviorManager:"
+ "setCurrentMultitaskingOption:"
+ "setDownloadSize:"
+ "setDownloadable:"
+ "setDownloadableOverCellular:"
+ "setDuration:"
+ "setHumanReadableUpdateName:"
+ "setIPadMultitaskingMode:"
+ "setLockScreenMode:"
+ "setMandatorySoftwareUpdateDictionary:"
+ "setMandatoryUpdateEligible:"
+ "setMandatoryUpdateOptional:"
+ "setMandatoryUpdateRestrictedToOutOfTheBox:"
+ "setMandatoryUpdateVersionMax:"
+ "setMandatoryUpdateVersionMin:"
+ "setObject:atIndexedSubscript:"
+ "setOverrideEntryFor:shouldOverride:"
+ "setPosition:"
+ "setProductBuildVersion:"
+ "setProductSystemName:"
+ "setProductVersion:forFeature:"
+ "setProductVersionExtra:"
+ "setPublisher:"
+ "setResults:"
+ "setResultsAsBasicBoolean:"
+ "setSourceDeviceValueEntryFor:value:"
+ "setUnderlyingManagerClient:"
+ "setUpdateType:"
+ "simple-passcode-type"
+ "softlink:r:path:/System/Library/Frameworks/UIKit.framework/UIKit"
+ "softlink:r:path:/System/Library/PrivateFrameworks/ThreatNotificationUI.framework/ThreatNotificationUI"
+ "softwareUpdate"
+ "source-device-%@"
+ "sourceDevice"
+ "sourceDeviceValueFor:"
+ "supports-migration"
+ "underlyingManagerClient"
+ "updateType"
+ "updateWithDictionary:"
+ "useOverridesFor:"
+ "userInterfaceIdiom"
+ "v16@?0Q8"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v28@0:8Q16B24"
+ "v32@0:8@\"SUScanOptions\"16@?<v@?@\"SUScanResults\"@\"NSError\">24"
+ "v32@?0@8@16^B24"
+ "v52@0:8@16@24@32Q40B48"
- "BYDaemonProximityTargetProtocol"
- "com.apple.onboarding.subscriptionbundle"
- "initWithDelegate:clientType:"

```
