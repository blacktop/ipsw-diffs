## SetupAssistantSupport

> `/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport`

```diff

-550.4.6.0.0
-  __TEXT.__text: 0x154b8
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x17e4
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xfeb
-  __TEXT.__oslogstring: 0xa2a
-  __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__dlopen_cstrs: 0x692
-  __TEXT.__unwind_info: 0x500
-  __TEXT.__objc_classname: 0x319
-  __TEXT.__objc_methname: 0x42bb
-  __TEXT.__objc_methtype: 0x77c
-  __TEXT.__objc_stubs: 0x35c0
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x860
-  __DATA_CONST.__objc_classlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x28
+563.0.0.0.0
+  __TEXT.__text: 0x16574
+  __TEXT.__objc_methlist: 0x19a4
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x1135
+  __TEXT.__oslogstring: 0xabe
+  __TEXT.__gcc_except_tab: 0x360
+  __TEXT.__dlopen_cstrs: 0x6f4
+  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1118
-  __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__objc_selrefs: 0x11f8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__got: 0x2c8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1500
-  __AUTH_CONST.__objc_const: 0x2db8
+  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__objc_const: 0x3048
   __AUTH_CONST.__objc_intobj: 0x90
-  __DATA.__objc_ivar: 0x1c4
-  __DATA.__data: 0x1e0
-  __DATA.__bss: 0x160
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x1d4
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x188
+  __DATA_DIRTY.__objc_data: 0x870
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA581520-2C7E-3888-87B9-16AEB1F20F07
-  Functions: 581
-  Symbols:   2301
-  CStrings:  1364
+  UUID: F86BF233-8365-37D6-8AB3-7FDE4B255ACC
+  Functions: 622
+  Symbols:   2453
+  CStrings:  497
 
Symbols:
+ +[SASExpressCloudSettings _glassTintAmount]
+ +[SASExpressCloudSettings _glassTintAmount].cold.1
+ +[SASExpressCloudSettings _glassTintAmount].cold.2
+ +[SASExpressCloudSettings gatherDataForExperienceWithBundleIdentifier:experienceProvider:]
+ +[SASExpressCloudSettings gatherExperiencesData]
+ +[SASExpressSettings buddyExperiencesDataType]
+ -[SASExpressSettings addBuddyExperiencesData:]
+ -[SASExpressSettings buddyExperiencesDataAtIndex:]
+ -[SASExpressSettings buddyExperiencesDatasCount]
+ -[SASExpressSettings buddyExperiencesDatas]
+ -[SASExpressSettings clearBuddyExperiencesDatas]
+ -[SASExpressSettings glassTintAmount]
+ -[SASExpressSettings hasGlassTintAmount]
+ -[SASExpressSettings setBuddyExperiencesDatas:]
+ -[SASExpressSettings setGlassTintAmount:]
+ -[SASExpressSettings setHasGlassTintAmount:]
+ -[SASExpressSettingsBuddyExperienceEntry .cxx_destruct]
+ -[SASExpressSettingsBuddyExperienceEntry copyTo:]
+ -[SASExpressSettingsBuddyExperienceEntry copyWithZone:]
+ -[SASExpressSettingsBuddyExperienceEntry description]
+ -[SASExpressSettingsBuddyExperienceEntry dictionaryRepresentation]
+ -[SASExpressSettingsBuddyExperienceEntry experienceData]
+ -[SASExpressSettingsBuddyExperienceEntry experienceIdentifier]
+ -[SASExpressSettingsBuddyExperienceEntry hasExperienceData]
+ -[SASExpressSettingsBuddyExperienceEntry hash]
+ -[SASExpressSettingsBuddyExperienceEntry isEqual:]
+ -[SASExpressSettingsBuddyExperienceEntry mergeFrom:]
+ -[SASExpressSettingsBuddyExperienceEntry readFrom:]
+ -[SASExpressSettingsBuddyExperienceEntry setExperienceData:]
+ -[SASExpressSettingsBuddyExperienceEntry setExperienceIdentifier:]
+ -[SASExpressSettingsBuddyExperienceEntry writeTo:]
+ -[SASExpressSettingsBuddyExperienceEntry writeTo:].cold.1
+ -[SASServiceProvider serviceForProtocol:]
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table39
+ OBJC_IVAR_$_SASExpressSettings._buddyExperiencesDatas
+ OBJC_IVAR_$_SASExpressSettings._glassTintAmount
+ OBJC_IVAR_$_SASExpressSettingsBuddyExperienceEntry._experienceData
+ OBJC_IVAR_$_SASExpressSettingsBuddyExperienceEntry._experienceIdentifier
+ _OBJC_CLASS_$_SASExpressSettingsBuddyExperienceEntry
+ _OBJC_CLASS_$_SASServiceProvider
+ _OBJC_METACLASS_$_SASExpressSettingsBuddyExperienceEntry
+ _OBJC_METACLASS_$_SASServiceProvider
+ _PBDataWriterWriteFloatField
+ _SASExpressSettingsBuddyExperienceEntryReadFrom
+ _SetupAssistantPaneLibrary
+ _SetupAssistantPaneLibraryCore.frameworkLibrary
+ _UIKitLibrary
+ __OBJC_$_CLASS_METHODS_SASExpressSettings
+ __OBJC_$_INSTANCE_METHODS_SASExpressSettingsBuddyExperienceEntry
+ __OBJC_$_INSTANCE_METHODS_SASServiceProvider
+ __OBJC_$_INSTANCE_VARIABLES_SASExpressSettingsBuddyExperienceEntry
+ __OBJC_$_PROP_LIST_SASExpressSettingsBuddyExperienceEntry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SAPBaseServiceProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SAPFeatureExpressDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAPBaseServiceProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAPFeatureExpressDataSource
+ __OBJC_$_PROTOCOL_REFS_SAPServiceProvider
+ __OBJC_CLASS_PROTOCOLS_$_SASExpressSettingsBuddyExperienceEntry
+ __OBJC_CLASS_PROTOCOLS_$_SASServiceProvider
+ __OBJC_CLASS_RO_$_SASExpressSettingsBuddyExperienceEntry
+ __OBJC_CLASS_RO_$_SASServiceProvider
+ __OBJC_LABEL_PROTOCOL_$_SAPBaseServiceProvider
+ __OBJC_LABEL_PROTOCOL_$_SAPFeatureExpressDataSource
+ __OBJC_LABEL_PROTOCOL_$_SAPServiceProvider
+ __OBJC_METACLASS_RO_$_SASExpressSettingsBuddyExperienceEntry
+ __OBJC_METACLASS_RO_$_SASServiceProvider
+ __OBJC_PROTOCOL_$_SAPBaseServiceProvider
+ __OBJC_PROTOCOL_$_SAPFeatureExpressDataSource
+ __OBJC_PROTOCOL_$_SAPServiceProvider
+ __OBJC_PROTOCOL_REFERENCE_$_SAPFeatureExpressDataSource
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.421
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.421.cold.1
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.422
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.422.cold.1
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.426
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.426.cold.1
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.450
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.451
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.451.cold.1
+ ___NSArray0__struct
+ ___SetupAssistantPaneLibraryCore_block_invoke
+ ___getSAPBundleLoaderClass_block_invoke
+ ___getSAPBundleLoaderClass_block_invoke.cold.1
+ ___getSAPExperienceProviderClass_block_invoke
+ ___getSAPExperienceProviderClass_block_invoke.cold.1
+ ___getUIViewGlassGetLegibilitySettingSymbolLoc_block_invoke
+ ___getUIViewGlassGetTintAmountSymbolLoc_block_invoke
+ _audit_stringSetupAssistantPane
+ _class_conformsToProtocol
+ _getSAPBundleLoaderClass
+ _getSAPBundleLoaderClass.softClass
+ _getSAPExperienceProviderClass.softClass
+ _getUIViewGlassGetLegibilitySettingSymbolLoc.ptr
+ _getUIViewGlassGetTintAmountSymbolLoc.ptr
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_glassTintAmount
+ _objc_msgSend$addBuddyExperiencesData:
+ _objc_msgSend$allAvailableBundleIdentifiersFilteredBy:
+ _objc_msgSend$buddyExperiencesDataAtIndex:
+ _objc_msgSend$buddyExperiencesDatasCount
+ _objc_msgSend$clearBuddyExperiencesDatas
+ _objc_msgSend$expressDataToBackup
+ _objc_msgSend$gatherDataForExperienceWithBundleIdentifier:experienceProvider:
+ _objc_msgSend$gatherExperiencesData
+ _objc_msgSend$initWithBundleLoader:serviceProvider:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$instanceForBundleWithIdentifier:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setExperienceData:
+ _objc_msgSend$setExperienceIdentifier:
+ _objc_msgSend$setGlassTintAmount:
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x9
+ _object_getClass
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.400
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.400.cold.1
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.401
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.401.cold.1
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.405
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.405.cold.1
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.429
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.430
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.430.cold.1
- _objc_autorelease
- _objc_retain_x25
CStrings:
+ "-[SASExpressSettingsBuddyExperienceEntry writeTo:]"
+ "Adding data entry for: %@"
+ "Found entry for: %@"
+ "Gathering bundle data if any are available"
+ "HomeButtonType"
+ "Invalid legibility setting"
+ "No bundle entries are available"
+ "SAPBundleLoader"
+ "SAPExperienceProvider"
+ "SASExpressSettingsBuddyExperienceEntry.m"
+ "UIViewGlassGetLegibilitySetting"
+ "UIViewGlassGetTintAmount"
+ "buddyExperiencesData"
+ "experienceData"
+ "experienceIdentifier"
+ "glassTintAmount"
+ "glasstintamount"
+ "nil != self->_experienceIdentifier"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistantPane.framework/SetupAssistantPane"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SASProximitySessionDelegate>\""
- "@\"ACAccount\""
- "@\"AKAnisetteData\""
- "@\"AKDevice\""
- "@\"CKContainer\""
- "@\"CKDatabase\""
- "@\"CUMessageSession\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"SASCloudKitClient\""
- "@\"SASExpressSettings\""
- "@\"SASExpressSettingsPrivacyBundle\""
- "@\"SASProximityHandshake\""
- "@\"SASProximityInformation\""
- "@\"SASProximitySession\""
- "@\"SASProximitySessionTransport\""
- "@\"_NSAttributedStringGrammarInflection\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@?"
- "@?16@0:8"
- "AKAnisetteServiceProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^{__WiFiNetwork=}16"
- "CKItemErrorForID:"
- "I16@0:8"
- "JwLB44/jEB8aFDpXQ16Tuw"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "SASCloudKitClient"
- "SASExpressCloudSettings"
- "SASExpressSettings"
- "SASExpressSettingsCreator"
- "SASExpressSettingsPrivacyBundle"
- "SASLogging"
- "SASProximityAction"
- "SASProximityAnisetteDataProvider"
- "SASProximityAnisetteRequestAction"
- "SASProximityBackupAction"
- "SASProximityCompanionAuthRequestAction"
- "SASProximityFinishedAction"
- "SASProximityHandshake"
- "SASProximityHandshakeAction"
- "SASProximityInformation"
- "SASProximityInformationAction"
- "SASProximityInformationDictionaryCoder"
- "SASProximityMigrationStartAction"
- "SASProximityMigrationTransferPreparationAction"
- "SASProximityPasscodeValidationAction"
- "SASProximityReadyAction"
- "SASProximitySession"
- "SASProximitySessionSharingTransport"
- "SASProximitySessionTransport"
- "SASSystemInformation"
- "StringAsAppearanceMode:"
- "StringAsDisplayZoomOption:"
- "StringAsIPadMultitaskingMode:"
- "T#,R"
- "T@\"<SASProximitySessionDelegate>\",V_delegate"
- "T@\"ACAccount\",&,V_account"
- "T@\"AKAnisetteData\",&,V_anisetteData"
- "T@\"AKDevice\",&,V_companionDevice"
- "T@\"CKContainer\",&,N,V_container"
- "T@\"CKDatabase\",&,N,V_database"
- "T@\"CUMessageSession\",&"
- "T@\"CUMessageSession\",&,V_actionMessageSession"
- "T@\"CUMessageSession\",&,V_messageSession"
- "T@\"NSArray\",C,V_keyboards"
- "T@\"NSArray\",C,V_networkPasswords"
- "T@\"NSArray\",C,V_networks"
- "T@\"NSData\",&,N,V_walletData"
- "T@\"NSData\",&,N,V_watchMigrationData"
- "T@\"NSData\",&,V_accessibilitySettings"
- "T@\"NSData\",&,V_backupMetadata"
- "T@\"NSData\",&,V_locationServicesData"
- "T@\"NSData\",&,V_sim"
- "T@\"NSData\",&,V_siriVoiceProfileAvailabilityMetadata"
- "T@\"NSDate\",&,V_completionDate"
- "T@\"NSDate\",C,V_dateOfLastBackup"
- "T@\"NSDictionary\",C,V_localePreferences"
- "T@\"NSError\",&,V_error"
- "T@\"NSMutableDictionary\",&,V_dataDictionary"
- "T@\"NSNumber\",&,N,V_allowMoreOn5G"
- "T@\"NSNumber\",&,N,V_hasMegaBackup"
- "T@\"NSNumber\",&,N,V_supportsCellularBackup"
- "T@\"NSNumber\",&,V_appAnalyticsOptIn"
- "T@\"NSNumber\",&,V_connectedToWiFi"
- "T@\"NSNumber\",&,V_deviceAnalyticsOptIn"
- "T@\"NSNumber\",&,V_deviceTermsIdentifier"
- "T@\"NSNumber\",&,V_deviceToDeviceMigrationVersion"
- "T@\"NSNumber\",&,V_findMyDeviceOptIn"
- "T@\"NSNumber\",&,V_hasInexpensiveCellularNetwork"
- "T@\"NSNumber\",&,V_preventSoftwareUpdateDeviceMigration"
- "T@\"NSNumber\",&,V_siriOptIn"
- "T@\"NSNumber\",&,V_storageAvailable"
- "T@\"NSNumber\",&,V_storageCapacity"
- "T@\"NSNumber\",&,V_supportsDeviceToDeviceMigration"
- "T@\"NSNumber\",V_hasTransferrableTelephonyPlan"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callbackQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_actionQueue"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,V_nearbyNetworksSemaphore"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_xpcActivity"
- "T@\"NSSet\",&,V_nearbyNetworks"
- "T@\"NSString\",&,N,V_deviceClass"
- "T@\"NSString\",&,N,V_deviceName"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_productType"
- "T@\"NSString\",&,N,V_productVersion"
- "T@\"NSString\",&,V_dsid"
- "T@\"NSString\",&,V_passcode"
- "T@\"NSString\",&,V_productVersion"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,V_appleID"
- "T@\"NSString\",C,V_backupUUID"
- "T@\"NSString\",C,V_deviceClass"
- "T@\"NSString\",C,V_deviceModel"
- "T@\"NSString\",C,V_deviceName"
- "T@\"NSString\",C,V_firstName"
- "T@\"NSString\",C,V_fullName"
- "T@\"NSString\",C,V_timeZone"
- "T@\"NSString\",R,C"
- "T@\"SASCloudKitClient\",&,N,V_cloudKitClient"
- "T@\"SASExpressSettings\",&,V_expressSettings"
- "T@\"SASExpressSettingsPrivacyBundle\",&,N,V_appAnalyticsPrivacyBundle"
- "T@\"SASExpressSettingsPrivacyBundle\",&,N,V_deviceAnalyticsPrivacyBundle"
- "T@\"SASExpressSettingsPrivacyBundle\",&,N,V_findMyPrivacyBundle"
- "T@\"SASExpressSettingsPrivacyBundle\",&,N,V_locationServicesPrivacyBundle"
- "T@\"SASExpressSettingsPrivacyBundle\",&,N,V_siriPrivacyBundle"
- "T@\"SASProximityHandshake\",&,V_handshake"
- "T@\"SASProximityInformation\",&,V_information"
- "T@\"SASProximitySession\",&,V_session"
- "T@\"SASProximitySessionTransport\",&,V_transport"
- "T@\"_NSAttributedStringGrammarInflection\",&,V_grammarInflection"
- "T@?,C,V_receivedDataBlock"
- "TB,GisConnected,V_connected"
- "TB,GisRestoring,V_restoring"
- "TB,N"
- "TB,N,GisBackupEnabled,V_backupEnabled"
- "TB,N,V_appAnalyticsOptIn"
- "TB,N,V_deviceAnalyticsOptIn"
- "TB,N,V_fileVaultEnabled"
- "TB,N,V_findMyOptIn"
- "TB,N,V_locationServicesOptIn"
- "TB,N,V_screenTimeEnabled"
- "TB,N,V_siriDataSharingOptIn"
- "TB,N,V_siriOptIn"
- "TB,N,V_siriVoiceTriggerEnabled"
- "TB,N,V_softwareUpdateAutoDownloadEnabled"
- "TB,N,V_softwareUpdateAutoUpdateEnabled"
- "TB,N,V_stolenDeviceProtectionEnabled"
- "TB,N,V_stolenDeviceProtectionStrictModeEnabled"
- "TB,N,V_unlockWithWatchEnabled"
- "TB,R"
- "TB,R,N"
- "TB,V_automaticTimeZoneEnabled"
- "TB,V_finishedBackup"
- "TB,V_hasHomeButton"
- "TB,V_hasPasscodeSet"
- "TB,V_locationServicesOptIn"
- "TB,V_passcodeValid"
- "TB,V_shouldProvision"
- "TB,V_shouldStartBackup"
- "TB,V_success"
- "TB,V_usesSameAccountForiTunes"
- "TI,N,V_version"
- "TQ,N,V_contentVersion"
- "TQ,R"
- "TQ,V_timeRemaining"
- "Td,V_percentComplete"
- "Ti,N,V_appearanceMode"
- "Ti,N,V_displayZoomOption"
- "Ti,N,V_iPadMultitaskingMode"
- "Ti,V_simplePasscodeType"
- "Ti,V_unlockType"
- "Tq,V_platformType"
- "Tq,V_request"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessibilitySettings"
- "_account"
- "_actionMessageSession"
- "_actionQueue"
- "_allowMoreOn5G"
- "_anisetteData"
- "_appAnalyticsOptIn"
- "_appAnalyticsPrivacyBundle"
- "_appearanceMode"
- "_appearanceValue"
- "_appleID"
- "_archivedAuthorizationDecisionsWithError:"
- "_automaticTimeZoneEnabled"
- "_backupEnabled"
- "_backupMetadata"
- "_backupUUID"
- "_callbackQueue"
- "_cloudKitClient"
- "_companionDevice"
- "_completionDate"
- "_connected"
- "_connectedToWiFi"
- "_container"
- "_contentVersion"
- "_createSettingsRecordInZoneID:forDeviceID:"
- "_dataDictionary"
- "_database"
- "_dateOfLastBackup"
- "_delegate"
- "_deviceAnalyticsOptIn"
- "_deviceAnalyticsPrivacyBundle"
- "_deviceClass"
- "_deviceModel"
- "_deviceName"
- "_deviceTermsIdentifier"
- "_deviceToDeviceMigrationVersion"
- "_displayZoomOption"
- "_dsid"
- "_error"
- "_expressSettings"
- "_fetchAppropriateSettingsWithCompletion:"
- "_fileVaultEnabled"
- "_findMyDeviceOptIn"
- "_findMyOptIn"
- "_findMyPrivacyBundle"
- "_finishedBackup"
- "_firstName"
- "_fullName"
- "_getFindMyDeviceOptIn"
- "_grammarInflection"
- "_handshake"
- "_has"
- "_hasHomeButton"
- "_hasInexpensiveCellularNetwork"
- "_hasMegaBackup"
- "_hasPasscodeSet"
- "_hasTransferrableTelephonyPlan"
- "_iPadMultitaskingMode"
- "_identifier"
- "_information"
- "_isCloudKitError:"
- "_isFindMyEnabled"
- "_isScreenTimeEnabled"
- "_keyboards"
- "_loadTelephonyInformation"
- "_localePreferences"
- "_locationServicesData"
- "_locationServicesOptIn"
- "_locationServicesPrivacyBundle"
- "_messageSession"
- "_nearbyNetworks"
- "_nearbyNetworksSemaphore"
- "_networkPasswords"
- "_networks"
- "_passcode"
- "_passcodeValid"
- "_percentComplete"
- "_platformType"
- "_predicateForRecordsModifiedInPastMonth"
- "_preventSoftwareUpdateDeviceMigration"
- "_productType"
- "_productVersion"
- "_queryForSettingsForDeviceID:"
- "_queryForSettingsFromPastMonth"
- "_queryForSettingsFromPastMonthForDeviceClass:"
- "_queryForSettingsFromPastMonthForPlatform:"
- "_queue"
- "_receivedDataBlock"
- "_request"
- "_restoring"
- "_scheduleDatabaseOperation:"
- "_screenTimeEnabled"
- "_session"
- "_setError"
- "_setupRecordZoneWithName:completion:"
- "_shouldProvision"
- "_shouldStartBackup"
- "_sim"
- "_simplePasscodeType"
- "_siriDataSharingOptIn"
- "_siriOptIn"
- "_siriPrivacyBundle"
- "_siriVoiceProfileAvailabilityMetadata"
- "_siriVoiceTriggerEnabled"
- "_softwareUpdateAutoDownloadEnabled"
- "_softwareUpdateAutoUpdateEnabled"
- "_stolenDeviceProtectionEnabled"
- "_stolenDeviceProtectionStrictModeEnabled"
- "_storageAvailable"
- "_storageCapacity"
- "_success"
- "_supportsCellularBackup"
- "_supportsDeviceToDeviceMigration"
- "_timeRemaining"
- "_timeZone"
- "_transport"
- "_unlockType"
- "_unlockWithWatchEnabled"
- "_usesSameAccountForiTunes"
- "_version"
- "_walletData"
- "_watchMigrationData"
- "_xpcActivity"
- "_zoneForSettings"
- "aa_altDSID"
- "aa_firstName"
- "aa_fullName"
- "aa_primaryAppleAccount"
- "accountPropertyForKey:"
- "accountTypeWithAccountTypeIdentifier:"
- "accountsWithAccountType:"
- "accountsWithAccountType:options:error:"
- "actionFromData:"
- "actionFromDictionary:"
- "actionID"
- "actionMessageSession"
- "actionQueue"
- "activate"
- "addObject:"
- "addOperation:"
- "addPort:forMode:"
- "allObjects"
- "allocWithZone:"
- "andPredicateWithSubpredicates:"
- "anisetteData"
- "anisetteDataWithCompletion:"
- "appearanceModeAsString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "archivedPreferences"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "assistantIsEnabled"
- "autorelease"
- "backupDeviceUUID"
- "backupMetadata"
- "boolValue"
- "bundleWithIdentifier:"
- "cStringUsingEncoding:"
- "callbackQueue"
- "class"
- "cloudKitClient"
- "code"
- "companionDevice"
- "compareProductVersion:toProductVersion:"
- "componentsSeparatedByString:"
- "configuration"
- "conformsToProtocol:"
- "connected"
- "container"
- "copy"
- "copyTo:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createExpressSettingsUsingDictionary:"
- "createExpressSettingsWithQueue:"
- "credentialForAccount:error:"
- "currentCalendar"
- "currentDevice"
- "currentMode"
- "currentMultitaskingOption"
- "currentRunLoop"
- "d"
- "d16@0:8"
- "dataDictionary"
- "dataUsingEncoding:"
- "database"
- "date"
- "dateByAddingComponents:toDate:options:"
- "dateWithTimeIntervalSinceNow:"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCategory"
- "defaultConfiguration"
- "defaultStore"
- "defaultSubsystem"
- "delegate"
- "description"
- "descriptorWithSubscriptionContext:"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "displayZoomOptionAsString:"
- "domain"
- "doubleValue"
- "dsid"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encryptedValues"
- "eraseAnisetteWithCompletion:"
- "eraseWithCompletion:"
- "error"
- "errorWithDomain:code:userInfo:"
- "expressSettings"
- "facility"
- "fetchAnisetteDataAndProvisionIfNecessary:withCompletion:"
- "fetchAttestationDataForRequestData:completion:"
- "fetchCurrentDeviceIDWithCompletion:"
- "fetchCurrentDeviceIDWithCompletionHandler:"
- "fetchPeerAttestationDataForRequest:completion:"
- "fetchRecordZone:group:completion:"
- "fetchRecords:inZone:group:completion:"
- "fetchSettingsWithCompletion:"
- "fileSystemRepresentation"
- "finishedWithError:"
- "firstObject"
- "floatValue"
- "fmipStateWithCompletion:"
- "getBytes:range:"
- "getCachedVoiceProfileAvailabilityMetaBlob"
- "getCurrentDataSubscriptionContextSync:"
- "handleAction:"
- "hasAppAnalyticsOptIn"
- "hasAppAnalyticsPrivacyBundle"
- "hasAppearanceMode"
- "hasDeviceAnalyticsOptIn"
- "hasDeviceAnalyticsPrivacyBundle"
- "hasDisplayZoomOption"
- "hasError"
- "hasFileVaultEnabled"
- "hasFindMyOptIn"
- "hasFindMyPrivacyBundle"
- "hasIPadMultitaskingMode"
- "hasLocationServicesOptIn"
- "hasLocationServicesPrivacyBundle"
- "hasProductVersion"
- "hasResponse"
- "hasScreenTimeEnabled"
- "hasSiriDataSharingOptIn"
- "hasSiriOptIn"
- "hasSiriPrivacyBundle"
- "hasSiriVoiceTriggerEnabled"
- "hasSoftwareUpdateAutoDownloadEnabled"
- "hasSoftwareUpdateAutoUpdateEnabled"
- "hasStolenDeviceProtectionEnabled"
- "hasStolenDeviceProtectionStrictModeEnabled"
- "hasUnlockWithWatchEnabled"
- "hasWalletData"
- "hasWatchMigrationData"
- "hash"
- "height"
- "i16@0:8"
- "i24@0:8@16"
- "iPadMultitaskingModeAsString:"
- "idmsAccountForiCloud"
- "init"
- "initWithCoder:"
- "initWithContainerID:"
- "initWithContainerIdentifier:"
- "initWithContainerIdentifier:callbackQueue:"
- "initWithContainerIdentifier:environment:"
- "initWithData:"
- "initWithDatabase:inContainer:callbackQueue:"
- "initWithDelegate:"
- "initWithDelegate:eventQueue:"
- "initWithDelegate:queue:clientType:"
- "initWithDictionary:"
- "initWithKey:ascending:"
- "initWithMessageSession:"
- "initWithQuery:"
- "initWithQueue:"
- "initWithRecordType:predicate:"
- "initWithRecordType:zoneID:"
- "initWithRecordZoneIDs:"
- "initWithRecordZonesToSave:recordZoneIDsToDelete:"
- "initWithRecordsToSave:recordIDsToDelete:"
- "initWithTemplate:"
- "initWithZoneID:"
- "initWithZoneName:"
- "initWithZoneName:ownerName:"
- "intValue"
- "integerValue"
- "interface"
- "interfaceCostExpensive:error:"
- "intersectSet:"
- "invalidate"
- "isActive"
- "isAnyPlanTransferableFromThisDeviceForFlow:OrError:"
- "isAutomaticDownloadEnabled"
- "isAutomaticUpdateV2Enabled"
- "isBackupEnabled"
- "isConnected"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isExpensive"
- "isFeatureEnabled"
- "isFeatureStrictModeEnabled"
- "isInitialMegaBackupCompleted:"
- "isKindOfClass:"
- "isManualBackupOnCellularAllowedWithAccount:error:"
- "isMemberOfClass:"
- "isNetworkTransferrable:"
- "isPasscodeSet"
- "isProxy"
- "isRestoring"
- "legacyAnisetteDataForDSID:withCompletion:"
- "length"
- "loadInformation"
- "locationServicesEnabled"
- "lowDataMode:error:"
- "lowercaseString"
- "mainDisplay"
- "mergeFrom:"
- "messageSession"
- "migrationConsentRequestData"
- "modeValue"
- "mutableCopy"
- "name"
- "nearbyNetworks"
- "nearbyNetworksSemaphore"
- "null"
- "numberFromMCUserBoolSetting:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "passcodeValid"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "port"
- "position"
- "predicateWithFormat:"
- "prepareForMigrationToDevice:"
- "privacyBundleForIdentifier:"
- "privacyFlow"
- "privateCloudDatabase"
- "provisionAnisetteWithCompletion:"
- "provisionWithCompletion:"
- "q"
- "q16@0:8"
- "q32@0:8@16@24"
- "queue"
- "readFrom:"
- "ready"
- "receivedAction:response:"
- "receivedBackupAction:"
- "receivedDataBlock"
- "recordID"
- "recordName"
- "registerRequestID:options:handler:"
- "release"
- "removePort:forMode:"
- "requestPayload"
- "resetDeviceIdentityWithCompletion:"
- "respondsToSelector:"
- "responsePayload"
- "restoreState"
- "retain"
- "retainCount"
- "runUntilDate:"
- "saveRecord:group:completion:"
- "saveRecordZone:group:completion:"
- "screenTimeStateWithCompletionHandler:"
- "self"
- "sendAction:"
- "sendData:response:"
- "sendRequestID:options:request:responseHandler:"
- "session"
- "setAccessibilitySettings:"
- "setAccount:"
- "setActionMessageSession:"
- "setActionQueue:"
- "setAllowMoreOn5G:"
- "setAnisetteData:"
- "setAppAnalyticsOptIn:"
- "setAppAnalyticsPrivacyBundle:"
- "setAppearanceMode:"
- "setAppleID:"
- "setAutomaticTimeZoneEnabled:"
- "setBackupEnabled:"
- "setBackupMetadata:"
- "setBackupUUID:"
- "setCallbackQueue:"
- "setCloudKitClient:"
- "setCompanionDevice:"
- "setCompletionDate:"
- "setConnected:"
- "setConnectedToWiFi:"
- "setContainer:"
- "setContentVersion:"
- "setCredential:"
- "setDataDictionary:"
- "setDatabase:"
- "setDateOfLastBackup:"
- "setDelegate:"
- "setDeviceAnalyticsOptIn:"
- "setDeviceAnalyticsPrivacyBundle:"
- "setDeviceClass:"
- "setDeviceModel:"
- "setDeviceName:"
- "setDeviceTermsIdentifier:"
- "setDeviceToDeviceMigrationVersion:"
- "setDisplayZoomOption:"
- "setDsid:"
- "setError:"
- "setExpressSettings:"
- "setFetchRecordZonesCompletionBlock:"
- "setFileVaultEnabled:"
- "setFindMyDeviceOptIn:"
- "setFindMyOptIn:"
- "setFindMyPrivacyBundle:"
- "setFinishedBackup:"
- "setFirstName:"
- "setFullName:"
- "setGender:"
- "setGrammarInflection:"
- "setGrammarInflectionGender:"
- "setGroup:"
- "setHandshake:"
- "setHasAppAnalyticsOptIn:"
- "setHasAppearanceMode:"
- "setHasDeviceAnalyticsOptIn:"
- "setHasDisplayZoomOption:"
- "setHasFileVaultEnabled:"
- "setHasFindMyOptIn:"
- "setHasHomeButton:"
- "setHasIPadMultitaskingMode:"
- "setHasInexpensiveCellularNetwork:"
- "setHasLocationServicesOptIn:"
- "setHasMegaBackup:"
- "setHasPasscodeSet:"
- "setHasScreenTimeEnabled:"
- "setHasSiriDataSharingOptIn:"
- "setHasSiriOptIn:"
- "setHasSiriVoiceTriggerEnabled:"
- "setHasSoftwareUpdateAutoDownloadEnabled:"
- "setHasSoftwareUpdateAutoUpdateEnabled:"
- "setHasStolenDeviceProtectionEnabled:"
- "setHasStolenDeviceProtectionStrictModeEnabled:"
- "setHasTransferrableTelephonyPlan:"
- "setHasUnlockWithWatchEnabled:"
- "setIPadMultitaskingMode:"
- "setIdentifier:"
- "setInformation:"
- "setInvalidationHandler:"
- "setKeyboards:"
- "setLabel:"
- "setLinkType:"
- "setLocalePreferences:"
- "setLocationServicesData:"
- "setLocationServicesOptIn:"
- "setLocationServicesPrivacyBundle:"
- "setMessageSession:"
- "setModifyRecordZonesCompletionBlock:"
- "setModifyRecordsCompletionBlock:"
- "setMonth:"
- "setNearbyNetworks:"
- "setNearbyNetworksSemaphore:"
- "setNetworkPasswords:"
- "setNetworks:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPasscode:"
- "setPasscodeValid:"
- "setPercentComplete:"
- "setPlatformType:"
- "setPosition:"
- "setPreventSoftwareUpdateDeviceMigration:"
- "setProductType:"
- "setProductVersion:"
- "setQualityOfService:"
- "setQueryCompletionBlock:"
- "setQueue:"
- "setReceivedDataBlock:"
- "setRecordMatchedBlock:"
- "setRequest:"
- "setResponseFromData:"
- "setRestoring:"
- "setScreenTimeEnabled:"
- "setSession:"
- "setSharingMessageSession:"
- "setShouldProvision:"
- "setShouldStartBackup:"
- "setSim:"
- "setSimplePasscodeType:"
- "setSiriDataSharingOptIn:"
- "setSiriOptIn:"
- "setSiriPrivacyBundle:"
- "setSiriVoiceProfileAvailabilityMetadata:"
- "setSiriVoiceTriggerEnabled:"
- "setSoftwareUpdateAutoDownloadEnabled:"
- "setSoftwareUpdateAutoUpdateEnabled:"
- "setSortDescriptors:"
- "setStolenDeviceProtectionEnabled:"
- "setStolenDeviceProtectionStrictModeEnabled:"
- "setStorageAvailable:"
- "setStorageCapacity:"
- "setSuccess:"
- "setSupportsCellularBackup:"
- "setSupportsDeviceToDeviceMigration:"
- "setTimeRemaining:"
- "setTimeZone:"
- "setTransport:"
- "setUnlockType:"
- "setUnlockWithWatchEnabled:"
- "setUsesSameAccountForiTunes:"
- "setValue:forKey:"
- "setVersion:"
- "setWalletData:"
- "setWatchMigrationData:"
- "setWiFiPassword:"
- "setWiFiSSID:"
- "setWithArray:"
- "setWithObjects:"
- "setXPCActivity:"
- "setXpcActivity:"
- "setZoneID:"
- "sharedConnection"
- "sharedInstance"
- "sharedMigrator"
- "sharedPreferences"
- "sharingMessageSession"
- "shouldProvision"
- "sim"
- "startMigration"
- "state"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "syncAnisetteWithSIMData:completion:"
- "syncWithSIMData:completion:"
- "systemTimeZone"
- "transport"
- "transportableAuthKitAccount:"
- "type"
- "unarchivedObjectOfClass:fromData:error:"
- "unarchivedObjectOfClasses:fromData:error:"
- "unlockDeviceWithPasscode:outError:"
- "unlockScreenTypeWithOutSimplePasscodeType:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updateSettings:withCompletion:"
- "userBoolValueForSetting:"
- "userInflection"
- "userInterfaceIdiom"
- "username"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16i24"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"AKAnisetteData\"@\"NSError\">20"
- "v32@0:8@\"AKAttestationRequestData\"16@?<v@?@\"AKBAAAttestationData\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"AKAnisetteData\"@\"NSError\">24"
- "v32@0:8@\"NSURLRequest\"16@?<v@?@\"AKAttestationData\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v48@0:8@16@24@32@?40"
- "valueForKey:"
- "versionOfAcceptedAgreement"
- "width"
- "wirelessScanComplete:error:"
- "writeTo:"
- "xpcActivity"
- "zone"
- "zoneID"
- "{?=\"appearanceMode\"b1\"displayZoomOption\"b1\"iPadMultitaskingMode\"b1\"appAnalyticsOptIn\"b1\"deviceAnalyticsOptIn\"b1\"fileVaultEnabled\"b1\"findMyOptIn\"b1\"locationServicesOptIn\"b1\"screenTimeEnabled\"b1\"siriDataSharingOptIn\"b1\"siriOptIn\"b1\"siriVoiceTriggerEnabled\"b1\"softwareUpdateAutoDownloadEnabled\"b1\"softwareUpdateAutoUpdateEnabled\"b1\"stolenDeviceProtectionEnabled\"b1\"stolenDeviceProtectionStrictModeEnabled\"b1\"unlockWithWatchEnabled\"b1}"

```
