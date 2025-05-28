## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5076.0.0.0.0
-  __TEXT.__text: 0x39b0c
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x2d98
+5116.0.0.0.0
+  __TEXT.__text: 0x3b9d4
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_methlist: 0x2f38
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0xa7c
-  __TEXT.__oslogstring: 0x4a8f
-  __TEXT.__cstring: 0x25e7
+  __TEXT.__gcc_except_tab: 0xaec
+  __TEXT.__oslogstring: 0x4eea
+  __TEXT.__cstring: 0x2794
   __TEXT.__dlopen_cstrs: 0x11a1
-  __TEXT.__unwind_info: 0xf38
-  __TEXT.__objc_classname: 0x720
-  __TEXT.__objc_methname: 0x929f
-  __TEXT.__objc_methtype: 0x104d
-  __TEXT.__objc_stubs: 0x6f40
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x15b8
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__unwind_info: 0xfc4
+  __TEXT.__objc_classname: 0x732
+  __TEXT.__objc_methname: 0x9973
+  __TEXT.__objc_methtype: 0x10a6
+  __TEXT.__objc_stubs: 0x7440
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x1588
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x45b8
-  __DATA_CONST.__objc_selrefs: 0x2390
-  __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__objc_const: 0x1748
-  __AUTH_CONST.__cfstring: 0x2a20
-  __AUTH_CONST.__const: 0x9a0
-  __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x608
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x2c0
-  __DATA.__objc_superrefs: 0x110
-  __DATA.__objc_ivar: 0x330
+  __DATA_CONST.__objc_const: 0x47b0
+  __DATA_CONST.__objc_selrefs: 0x2500
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__objc_arraydata: 0x178
+  __AUTH_CONST.__objc_const: 0x1790
+  __AUTH_CONST.__cfstring: 0x2d60
+  __AUTH_CONST.__const: 0x9c0
+  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__auth_got: 0x638
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x344
   __DATA.__data: 0x950
   __DATA.__bss: 0x4a8
   __DATA_DIRTY.__objc_data: 0xe60

   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Seeding.framework/Seeding
   - /System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1511
-  Symbols:   5457
-  CStrings:  2653
+  Functions: 1555
+  Symbols:   5632
+  CStrings:  2762
 
Symbols:
+ +[BYPaneFeatureAnalyticsManager _featuresForPane:]
+ +[BYSiriUtilities isVoiceTriggerEnabled]
+ -[BFFSettingsManager hasAssistantVoiceTriggerEnabledValue]
+ -[BYAnalyticsManager _sendCombinedAnalyticsRepromptCompletedEventIfNecessary]
+ -[BYAnalyticsManager _sendCombinedAnalyticsRepromptNecessaryEventWithRTCReporting:]
+ -[BYAnalyticsManager combinedAnalyticsRepromptChoiceNumber]
+ -[BYAnalyticsManager prepareForCombinedAnalyticsRepromptWithCompletion:]
+ -[BYAnalyticsManager rtcReporting]
+ -[BYAnalyticsManager setCombinedAnalyticsRepromptChoice:]
+ -[BYAnalyticsManager setCombinedAnalyticsRepromptChoiceNumber:]
+ -[BYAnalyticsManager setRtcReporting:]
+ -[BYBuddyDaemonGeneralClient migrateWithStoredMigratorVersion:userDataDisposition:]
+ -[BYBuddyDaemonProximityTargetClient beginSIMSetupExternalAuthentication]
+ -[BYBuddyDaemonProximityTargetClient endSIMSetupExternalAuthentication]
+ -[BYCapabilities eligibilitySetDeviceLocale:]
+ -[BYCapabilities eligibilitySetDeviceLocale:].cold.1
+ -[BYCapabilities eligibleForChlorine]
+ -[BYCapabilities eligibleForChlorine].cold.1
+ -[BYCapabilities isAppAnalyticsRestricted]
+ -[BYGreenController .cxx_destruct]
+ -[BYGreenController _effectivePlaceForLocaleRegionCode:]
+ -[BYGreenController _extractGreenValuesForEffectivePlace:desiredPlistState:]
+ -[BYGreenController _greenBinaryFilePath]
+ -[BYGreenController _greenPlistFilePath]
+ -[BYGreenController _readPlistState]
+ -[BYGreenController _shouldWriteInformedDefaultPlist]
+ -[BYGreenController _shouldWriteInitialPlist]
+ -[BYGreenController _skuRegionCodeIsAmbiguous]
+ -[BYGreenController _skuRegionCode]
+ -[BYGreenController _skuRegionCode].cold.1
+ -[BYGreenController _writeFilesWithPlist:desiredPlistState:]
+ -[BYGreenController _writePlistForLocaleRegionCode:desiredPlistState:]
+ -[BYGreenController init]
+ -[BYGreenController plistStateCache]
+ -[BYGreenController setPlistStateCache:]
+ -[BYGreenController writeInformedDefaultPlistIfNecessaryForLocaleRegionCode:]
+ -[BYGreenController writeInitialPlistIfNecessary]
+ -[BYSetupUserDisposition buildVersion]
+ -[BYSetupUserDisposition initWithProductVersion:buildVersion:date:]
+ -[BYSetupUserDisposition initWithProductVersion:buildVersion:date:newUser:child:]
+ -[BYSetupUserDisposition setBuildVersion:]
+ GCC_except_table22
+ GCC_except_table36
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table59
+ _BYAssistantScreenShouldRunForVTConfirmation
+ _BYBuddyRunCombinedDiagnosticsMismatchMiniBuddy
+ _BYBuddyRunStolenDeviceProtectionMiniBuddy
+ _MGCopyAnswerWithError
+ _OBJC_CLASS_$_BYGreenController
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_RTCReporting
+ _OBJC_IVAR_$_BYAnalyticsManager._combinedAnalyticsRepromptChoiceNumber
+ _OBJC_IVAR_$_BYAnalyticsManager._rtcReporting
+ _OBJC_IVAR_$_BYGreenController._plistStateCache
+ _OBJC_IVAR_$_BYGreenController._relevantGreenKeys
+ _OBJC_IVAR_$_BYSetupUserDisposition._buildVersion
+ _OBJC_METACLASS_$_BYGreenController
+ __OBJC_$_INSTANCE_METHODS_BYGreenController
+ __OBJC_$_INSTANCE_VARIABLES_BYGreenController
+ __OBJC_$_PROP_LIST_BYDeviceConfiguration.64
+ __OBJC_$_PROP_LIST_BYGreenController
+ __OBJC_CLASS_RO_$_BYGreenController
+ __OBJC_METACLASS_RO_$_BYGreenController
+ ___41-[BYBuddyDaemonCloudSyncClient startSync]_block_invoke.53
+ ___42-[BYBuddyDaemonCloudSyncClient cancelSync]_block_invoke.57
+ ___43-[BYSettingsManagerClient _connectToDaemon]_block_invoke.56
+ ___43-[BYSettingsManagerClient _connectToDaemon]_block_invoke.56.cold.1
+ ___47-[BYBuddyDaemonCloudSyncClient connectToDaemon]_block_invoke.80
+ ___47-[BYBuddyDaemonGeneralClient _daemonConnection]_block_invoke.145
+ ___53-[BYBuddyDaemonProximitySourceClient connectToDaemon]_block_invoke.66
+ ___53-[BYBuddyDaemonProximityTargetClient connectToDaemon]_block_invoke.81
+ ___54-[BYBuddyDaemonMigrationSourceClient _connectToDaemon]_block_invoke.60
+ ___54-[BYBuddyDaemonMigrationSourceClient _connectToDaemon]_block_invoke.60.cold.1
+ ___65-[BYBuddyDaemonProximityTargetClient fileTransferSessionTemplate]_block_invoke.97
+ ___72-[BYAnalyticsManager prepareForCombinedAnalyticsRepromptWithCompletion:]_block_invoke
+ ___80-[BYBuddyDaemonCloudSyncClient cloudSyncProgressUpdate:completedClients:errors:]_block_invoke.61
+ ___83-[BYBuddyDaemonGeneralClient migrateWithStoredMigratorVersion:userDataDisposition:]_block_invoke
+ ___87-[BYBuddyDaemonProximityAutomatedDeviceEnrollmentTargetClient connectionToMachService:]_block_invoke.65
+ ___BYDaemonCreateMetadataArchive_block_invoke.262
+ ___BYSetupAssistantCreateAuthContext_block_invoke.174
+ ___Daemon_BYSetupAssistantNeedsToRun_block_invoke.143
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_literal_global.140
+ ___block_literal_global.166
+ ___block_literal_global.187
+ ___block_literal_global.195
+ ___block_literal_global.197
+ ___block_literal_global.60
+ ___block_literal_global.63
+ ___block_literal_global.72
+ ___block_literal_global.83
+ ___block_literal_global.88
+ ___block_literal_global.94
+ ___block_literal_global.96
+ ___kCFBooleanFalse
+ __unnamed_array_storage.27
+ __unnamed_array_storage.28
+ __unnamed_array_storage.33
+ __unnamed_array_storage.34
+ __unnamed_array_storage.40
+ __unnamed_array_storage.41
+ __unnamed_array_storage.47
+ __unnamed_array_storage.48
+ __unnamed_array_storage.51
+ __unnamed_array_storage.52
+ _arc4random
+ _kRTCReportingSessionInfoBatchEvent
+ _kRTCReportingSessionInfoClientBundleID
+ _kRTCReportingSessionInfoClientType
+ _kRTCReportingSessionInfoClientVersion
+ _kRTCReportingSessionInfoContainsRealtimeEvents
+ _kRTCReportingSessionInfoSessionID
+ _kRTCReportingUserInfoClientName
+ _kRTCReportingUserInfoServiceName
+ _objc_msgSend$_effectivePlaceForLocaleRegionCode:
+ _objc_msgSend$_extractGreenValuesForEffectivePlace:desiredPlistState:
+ _objc_msgSend$_featuresForPane:
+ _objc_msgSend$_greenBinaryFilePath
+ _objc_msgSend$_greenPlistFilePath
+ _objc_msgSend$_readPlistState
+ _objc_msgSend$_sendCombinedAnalyticsRepromptCompletedEventIfNecessary
+ _objc_msgSend$_sendCombinedAnalyticsRepromptNecessaryEventWithRTCReporting:
+ _objc_msgSend$_shouldWriteInformedDefaultPlist
+ _objc_msgSend$_shouldWriteInitialPlist
+ _objc_msgSend$_skuRegionCode
+ _objc_msgSend$_skuRegionCodeIsAmbiguous
+ _objc_msgSend$_writeFilesWithPlist:desiredPlistState:
+ _objc_msgSend$_writePlistForLocaleRegionCode:desiredPlistState:
+ _objc_msgSend$autoupdatingCurrentLocale
+ _objc_msgSend$beginSIMSetupExternalAuthentication
+ _objc_msgSend$buildVersion
+ _objc_msgSend$combinedAnalyticsRepromptChoiceNumber
+ _objc_msgSend$countryCode
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$endSIMSetupExternalAuthentication
+ _objc_msgSend$initWithProductVersion:buildVersion:date:
+ _objc_msgSend$initWithProductVersion:buildVersion:date:newUser:child:
+ _objc_msgSend$initWithSessionInfo:userInfo:frameworksToCheck:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$isVoiceTriggerEnabled
+ _objc_msgSend$isVoiceTriggerRepromptRequired
+ _objc_msgSend$localizedStringForRegion:context:short:
+ _objc_msgSend$migrateWithStoredMigratorVersion:userDataDisposition:
+ _objc_msgSend$plistStateCache
+ _objc_msgSend$rtcReporting
+ _objc_msgSend$sendMessageWithCategory:type:payload:error:
+ _objc_msgSend$setBuildVersion:
+ _objc_msgSend$setCombinedAnalyticsRepromptChoiceNumber:
+ _objc_msgSend$setPlistStateCache:
+ _objc_msgSend$setRtcReporting:
+ _objc_msgSend$setSiriVoiceTriggerEnabled:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$startConfigurationWithCompletionHandler:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$voiceTriggerRepromptFinished
+ _objc_msgSend$writeToFile:atomically:
+ _objc_msgSend$writeToFile:options:error:
+ _objc_opt_self
+ _os_eligibility_get_domain_answer
+ _os_eligibility_set_input
+ _xpc_string_create
- +[BYPaneFeatureAnalyticsManager _featureForPane:]
- -[BYSetupUserDisposition initWithProductVersion:date:]
- -[BYSetupUserDisposition initWithProductVersion:date:newUser:child:]
- GCC_except_table46
- GCC_except_table50
- GCC_except_table53
- GCC_except_table56
- GCC_except_table58
- __OBJC_$_PROP_LIST_BYDeviceConfiguration.63
- ___41-[BYBuddyDaemonCloudSyncClient startSync]_block_invoke.52
- ___42-[BYBuddyDaemonCloudSyncClient cancelSync]_block_invoke.56
- ___43-[BYSettingsManagerClient _connectToDaemon]_block_invoke.55
- ___43-[BYSettingsManagerClient _connectToDaemon]_block_invoke.55.cold.1
- ___47-[BYBuddyDaemonCloudSyncClient connectToDaemon]_block_invoke.79
- ___47-[BYBuddyDaemonGeneralClient _daemonConnection]_block_invoke.140
- ___53-[BYBuddyDaemonProximitySourceClient connectToDaemon]_block_invoke.65
- ___53-[BYBuddyDaemonProximityTargetClient connectToDaemon]_block_invoke.78
- ___54-[BYBuddyDaemonMigrationSourceClient _connectToDaemon]_block_invoke.59
- ___54-[BYBuddyDaemonMigrationSourceClient _connectToDaemon]_block_invoke.59.cold.1
- ___65-[BYBuddyDaemonProximityTargetClient fileTransferSessionTemplate]_block_invoke.94
- ___80-[BYBuddyDaemonCloudSyncClient cloudSyncProgressUpdate:completedClients:errors:]_block_invoke.60
- ___87-[BYBuddyDaemonProximityAutomatedDeviceEnrollmentTargetClient connectionToMachService:]_block_invoke.64
- ___BYDaemonCreateMetadataArchive_block_invoke.238
- ___BYSetupAssistantCreateAuthContext_block_invoke.156
- ___Daemon_BYSetupAssistantNeedsToRun_block_invoke.125
- ___block_literal_global.122
- ___block_literal_global.148
- ___block_literal_global.159
- ___block_literal_global.169
- ___block_literal_global.179
- ___block_literal_global.54
- ___block_literal_global.57
- ___block_literal_global.59
- ___block_literal_global.61
- ___block_literal_global.80
- ___block_literal_global.85
- ___block_literal_global.91
- ___block_literal_global.93
- _objc_msgSend$_featureForPane:
- _objc_msgSend$initWithProductVersion:date:
- _objc_msgSend$initWithProductVersion:date:newUser:child:
- _objc_msgSend$localizedStringForCountryCode:
CStrings:
+ "\x05"
+ "\t"
+ "(forced)"
+ "/var/mobile/Library/Application Support/com.apple.palette.green.bin"
+ "/var/mobile/Library/Application Support/com.apple.palette.green.plist"
+ "@\"RTCReporting\""
+ "@28@0:8Q16i24"
+ "@40@0:8@16@24@32"
+ "@48@0:8@16@24@32B40B44"
+ "Analytics did send combined analytics reprompt completed event (choice %@) with success %d error %@"
+ "Analytics did send combined analytics reprompt necessary event with success %d error %@"
+ "Analytics reporting configuration already started"
+ "Analytics reporting configuration forcing success"
+ "Analytics reporting configuration started with success %d"
+ "B28@0:8@16i24"
+ "BYGreenController"
+ "BYSetupAssistantNeedsToRun is YES to show combined diagnostics mismatch buddy"
+ "BYSetupAssistantNeedsToRun is YES to show stolen device protection buddy"
+ "CH"
+ "CN"
+ "Failed to get eligibility for chlorine with error %d"
+ "Failed to migrate with stored migration version: %{public}@"
+ "Failed to set eligibility device locale with error %d"
+ "ForceRTCStartConfigurationSuccess"
+ "HK"
+ "MO"
+ "Not showing VT Confirmation because voicetrigger is turned off"
+ "Q24@0:8@16"
+ "RegionCode"
+ "ShouldRunCombinedDiagnosticsMismatchMiniBuddy"
+ "ShouldRunStolenDeviceProtectionMiniBuddy"
+ "Showing VT Confirmation %@"
+ "T@\"NSNumber\",&,N,V_combinedAnalyticsRepromptChoiceNumber"
+ "T@\"NSSet\",&,N,V_expressSetupFeatures"
+ "T@\"NSString\",&,N,V_buildVersion"
+ "T@\"NSString\",?,R,C"
+ "T@\"RTCReporting\",&,N,V_rtcReporting"
+ "TA"
+ "TW"
+ "Ti,N,V_plistStateCache"
+ "ZA"
+ "ZP"
+ "_combinedAnalyticsRepromptChoiceNumber"
+ "_effectivePlaceForLocaleRegionCode:"
+ "_extractGreenValuesForEffectivePlace:desiredPlistState:"
+ "_featuresForPane:"
+ "_greenBinaryFilePath"
+ "_greenPlistFilePath"
+ "_plistStateCache"
+ "_readPlistState"
+ "_relevantGreenKeys"
+ "_rtcReporting"
+ "_sendCombinedAnalyticsRepromptCompletedEventIfNecessary"
+ "_sendCombinedAnalyticsRepromptNecessaryEventWithRTCReporting:"
+ "_shouldWriteInformedDefaultPlist"
+ "_shouldWriteInitialPlist"
+ "_skuRegionCode"
+ "_skuRegionCodeIsAmbiguous"
+ "_writeFilesWithPlist:desiredPlistState:"
+ "_writePlistForLocaleRegionCode:desiredPlistState:"
+ "autoupdatingCurrentLocale"
+ "beginSIMSetupExternalAuthentication"
+ "com.apple.VoiceTriggerUI.vtconf"
+ "combinedAnalyticsRepromptChoiceNumber"
+ "countryCode"
+ "dataWithBytes:length:"
+ "dataWithPropertyList:format:options:error:"
+ "dict1"
+ "dict2"
+ "dict3"
+ "dict4"
+ "eligibilitySetDeviceLocale:"
+ "eligibleForChlorine"
+ "enabled"
+ "endSIMSetupExternalAuthentication"
+ "forceNeedsConfirmation"
+ "green file already exists with state %d"
+ "green file already exists with state key"
+ "green file already exists without state key"
+ "green file does not exist"
+ "green file initial did write with success %d"
+ "green region code MG returned NULL; %d"
+ "green write informed defaults completed for %@ with success %d"
+ "green write informed defaults unnecessary. already in state %d"
+ "hasAssistantVoiceTriggerEnabledValue"
+ "initWithProductVersion:buildVersion:date:"
+ "initWithProductVersion:buildVersion:date:newUser:child:"
+ "initWithSessionInfo:userInfo:frameworksToCheck:"
+ "intersectsSet:"
+ "isAppAnalyticsRestricted"
+ "isVoiceTriggerEnabled"
+ "isVoiceTriggerRepromptRequired"
+ "key1"
+ "key2"
+ "key3"
+ "localizedStringForRegion:context:short:"
+ "migrateWithStoredMigratorVersion:userDataDisposition:"
+ "plistStateCache"
+ "prepareForCombinedAnalyticsRepromptWithCompletion:"
+ "rtcReporting"
+ "sendMessageWithCategory:type:payload:error:"
+ "setCombinedAnalyticsRepromptChoice:"
+ "setCombinedAnalyticsRepromptChoiceNumber:"
+ "setPlistStateCache:"
+ "setRtcReporting:"
+ "setSiriVoiceTriggerEnabled:"
+ "setWithObject:"
+ "startConfigurationWithCompletionHandler:"
+ "stringWithString:"
+ "v16@?0@\"NSArray\"8"
+ "v24@0:8I16I20"
+ "voiceTriggerRepromptFinished"
+ "writeInformedDefaultPlistIfNecessaryForLocaleRegionCode:"
+ "writeInitialPlistIfNecessary"
+ "writeToFile:atomically:"
+ "writeToFile:options:error:"
- "\x04"
- "\a"
- "@40@0:8@16@24B32B36"
- "T@\"NSArray\",&,N,V_expressSetupFeatures"
- "_featureForPane:"
- "initWithProductVersion:date:"
- "initWithProductVersion:date:newUser:child:"
- "localizedStringForCountryCode:"

```
