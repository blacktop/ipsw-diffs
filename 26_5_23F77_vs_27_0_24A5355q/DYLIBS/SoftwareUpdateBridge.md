## SoftwareUpdateBridge

> `/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge`

```diff

-367.120.2.0.0
-  __TEXT.__text: 0x7ba8
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x858
+393.0.0.0.0
+  __TEXT.__text: 0x82c0
+  __TEXT.__objc_methlist: 0x888
   __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__cstring: 0x1168
-  __TEXT.__oslogstring: 0xbe5
-  __TEXT.__unwind_info: 0x2c0
-  __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x1dff
-  __TEXT.__objc_methtype: 0x20f
-  __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x380
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__cstring: 0x1485
+  __TEXT.__oslogstring: 0x12b8
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e0
+  __DATA_CONST.__objc_selrefs: 0x748
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xec0
+  __AUTH_CONST.__cfstring: 0x1260
   __AUTH_CONST.__objc_const: 0xf98
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x2a0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73339BE5-290E-3861-A865-84FE11CD8A33
-  Functions: 215
-  Symbols:   926
-  CStrings:  733
+  UUID: 449299E6-01C0-3B96-BFDA-323F0767C65B
+  Functions: 219
+  Symbols:   957
+  CStrings:  444
 
Symbols:
+ -[SUBDescriptor _denialReasonsMessageForExpiredWindow:]
+ -[SUBDescriptor getDenialReasonsMessage]
+ -[SUBDescriptor getExpiredDenialReasonsMessage]
+ -[SUBDescriptor internalMessageFromDenialInfo:]
+ _OBJC_CLASS_$_NSBundle
+ _SUBErrorUserInfoConstraintDenialMessage
+ _SUBErrorUserInfoDeviceBusyReasons
+ _SUBErrorUserInfoDeviceIsBusyReasonCall
+ _SUBErrorUserInfoDeviceIsBusyReasonNavigationActive
+ _SUBErrorUserInfoDeviceIsBusyReasonWorkout
+ ___31-[SUBManager _serverConnection]_block_invoke.359
+ ___block_literal_global.356
+ ___block_literal_global.366
+ ___block_literal_global.374
+ ___block_literal_global.385
+ ___kCFBooleanFalse
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_denialReasonsMessageForExpiredWindow:
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$code
+ _objc_msgSend$denialReasons
+ _objc_msgSend$intValue
+ _objc_msgSend$internalMessageFromDenialInfo:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$localizedUserNotificationStringForKey:arguments:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$userInfo
+ _objc_msgSend$valueForKey:
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x8
- ___31-[SUBManager _serverConnection]_block_invoke.338
- ___block_literal_global.335
- ___block_literal_global.345
- ___block_literal_global.353
- ___block_literal_global.364
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
+ "%@"
+ "%@\n[Internal Only : %@]"
+ "-[SUBDescriptor internalMessageFromDenialInfo:]"
+ "/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework"
+ ": CallOngoing :"
+ ": ChargerRequired :"
+ ": LowBatt(Min/Current) (%@ / %@) :"
+ ": NavigationActive :"
+ ": WorkoutInProgress :"
+ "CallInProgress"
+ "ConstraintDenialMessage"
+ "DeviceBusyReasons"
+ "INSTALLATION_PAUSED_BATTERY"
+ "INSTALLATION_PAUSED_CHARGER"
+ "INSTALLATION_PAUSED_CHARGER_OPTIONAL"
+ "INSTALLATION_PAUSED_NAVIGATION"
+ "INSTALLATION_PAUSED_PHONE_CALL"
+ "INSTALLATION_PAUSED_WORKOUT"
+ "INSTALL_EXPIRED_BATTERY"
+ "INSTALL_EXPIRED_CHARGER"
+ "INSTALL_EXPIRED_CHARGER_OPTIONAL"
+ "INSTALL_EXPIRED_NAVIGATION"
+ "INSTALL_EXPIRED_PHONE_CALL"
+ "INSTALL_EXPIRED_WORKOUT"
+ "Install Pause Reason: "
+ "Invalid denialInfo passed to %s"
+ "Invalid value passed for battery level"
+ "Invalid value passed for chargerConnected"
+ "Invalid value passed for minBatteryLevelForApplyOffCharger"
+ "Invalid value passed for minBatteryLevelForApplyOnCharger"
+ "LBJfwOEzExRxzlAnSuI7eg"
+ "NavigationActive"
+ "SoftwareUpdateBridge"
+ "Unable to parse error info"
+ "Unexpected value passed for chargerRequiredForUpdate. Assuming required"
+ "WorkoutInProgress"
+ "[DenialReasons]: Charger is not required for update. Showing new combined battery/charger message in notification"
+ "[DenialReasons]: Charger is required for update and is connected. Showing low battery message in notification"
+ "[DenialReasons]: Charger is required for update and not connected. Showing charger required message in notification"
+ "[DenialReasons]: DenialReasons passed in using legacy format"
+ "[DenialReasons]: DenialReasons passed in using new format : %@"
+ "[DenialReasons]: DeviceBusyReason : %{public}@"
+ "[DenialReasons]: Got invalid value for CurrentBatteryLevel, assuming low battery"
+ "[DenialReasons]: Invalid denialInfo passed to showDuetConditions. Showing default alert"
+ "[DenialReasons]: No denial reasons set in descriptor. Returning nil message"
+ "[DenialReasons]: Showing combined battery/charger message in notification due to inability to determine more specific reason"
+ "[DenialReasons]: Showing installation paused due to call"
+ "[DenialReasons]: Showing installation paused due to ongoing navigation"
+ "[DenialReasons]: Showing installation paused due to workout"
+ "[DenialReasons]: Unexpected value passed for chargerConnected. Assuming not connected"
+ "[DenialReasons]: Unexpected value passed for chargerRequiredForUpdate. Assuming required"
+ "[DenialReasons]: Unexpected value passed for requiredBatteryLevelWithCharger. Assuming default(%@)"
+ "[DenialReasons]: Unexpected value passed for requiredBatteryLevelWithoutCharger. Assuming default(%@)"
- ".cxx_destruct"
- "@\"<SUBManagerDelegate>\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"SUBDescriptor\""
- "@\"SUBDocumentation\""
- "@\"SUBProgress\""
- "@\"SUCoreDescriptor\""
- "@\"SUCoreDocumentation\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "AB"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "NSCoding"
- "NSSecureCoding"
- "Q16@0:8"
- "SUBDescriptor"
- "SUBDocumentation"
- "SUBDownload"
- "SUBManager"
- "SUBProgress"
- "T@\"<SUBManagerDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",R,&,N"
- "T@\"NSData\",&,N,V_licenseAgreement"
- "T@\"NSData\",&,N,V_manifest"
- "T@\"NSData\",&,N,V_preferencesIcon"
- "T@\"NSData\",&,N,V_releaseNotes"
- "T@\"NSData\",&,N,V_releaseNotesSummary"
- "T@\"NSDate\",&,N,V_autoSUEndTime"
- "T@\"NSDate\",&,N,V_autoSUStartTime"
- "T@\"NSDate\",&,N,V_dateOfLastScheduleOfAutoUpdate"
- "T@\"NSDate\",&,N,V_dateOfLastScheduleOfAutoUpdateNotification"
- "T@\"NSDate\",&,N,V_dateOfLastSentInstallNotification"
- "T@\"NSDictionary\",&,N,V_updatePowerPolicy"
- "T@\"NSError\",&,N,V_denialReasons"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_serverConnection"
- "T@\"NSString\",&,N,V_documentationID"
- "T@\"NSString\",&,N,V_humanReadableUpdateName"
- "T@\"NSString\",&,N,V_marketingVersion"
- "T@\"NSString\",&,N,V_osName"
- "T@\"NSString\",&,N,V_phase"
- "T@\"NSString\",&,N,V_phoneLanguage"
- "T@\"NSString\",&,N,V_productBuildVersion"
- "T@\"NSString\",&,N,V_productSystemName"
- "T@\"NSString\",&,N,V_productVersion"
- "T@\"NSString\",&,N,V_publisher"
- "T@\"NSString\",&,N,V_taskID"
- "T@\"NSString\",R,&,N"
- "T@\"NSURL\",&,N,V_documentationBundleURL"
- "T@\"SUBDescriptor\",&,N,V_descriptor"
- "T@\"SUBDocumentation\",&,N,V_documentation"
- "T@\"SUBProgress\",&,N,V_progress"
- "T@\"SUCoreDescriptor\",&,N,V_coreDescriptor"
- "T@\"SUCoreDocumentation\",&,N,V_suCoreParsedDocumentation"
- "TB,N,V_backgroundDownloadDisabledByServer"
- "TB,N,V_displayTermsRequested"
- "TB,N,V_installTonightScheduled"
- "TB,N,V_isAwaitingAdmissionControlForInstallation"
- "TB,N,V_isDone"
- "TB,N,V_isStalled"
- "TB,N,V_userDidAcceptTermsAndConditions"
- "TB,N,V_userDidManuallyTriggerInstall"
- "TB,N,V_willProceedWithInstallation"
- "TB,R"
- "Td,N,V_estimatedTimeRemaining"
- "Tf,N,V_portionComplete"
- "Tq,N,V_downloadSize"
- "Tq,N,V_installationSize"
- "Tq,N,V_msuPrepareSize"
- "Tq,N,V_totalRequiredFreeSpace"
- "Tq,N,V_unarchivedSize"
- "Tq,N,V_userInstallRequestType"
- "Tq,R,N"
- "UTF8String"
- "_autoSUEndTime"
- "_autoSUStartTime"
- "_backgroundDownloadDisabledByServer"
- "_coreDescriptor"
- "_dateOfLastScheduleOfAutoUpdate"
- "_dateOfLastScheduleOfAutoUpdateNotification"
- "_dateOfLastSentInstallNotification"
- "_delegate"
- "_denialReasons"
- "_descriptor"
- "_displayTermsRequested"
- "_documentation"
- "_documentationBundleURL"
- "_documentationID"
- "_downloadSize"
- "_estimatedTimeRemaining"
- "_forwardDownloadProgress:"
- "_forwardInstallResult:"
- "_forwardInstallationAwaitingUserInteraction:"
- "_forwardInstallationCanProceed:"
- "_forwardInstallationWillProceed:"
- "_forwardScanResult:"
- "_forwardUserDidAcceptTermsAndConditionsChanged:"
- "_forwardUserInstallRequestTypeChanged:"
- "_hasQueriedStateOnceFlag"
- "_humanReadableUpdateName"
- "_installTonightScheduled"
- "_installationSize"
- "_isAwaitingAdmissionControlForInstallation"
- "_isDone"
- "_isStalled"
- "_licenseAgreement"
- "_loadBundleResources"
- "_manifest"
- "_marketingVersion"
- "_msuPrepareSize"
- "_osName"
- "_phase"
- "_phoneLanguage"
- "_portionComplete"
- "_preferencesIcon"
- "_productBuildVersion"
- "_productSystemName"
- "_productVersion"
- "_progress"
- "_publisher"
- "_queue"
- "_releaseNotes"
- "_releaseNotesSummary"
- "_resourceFromBundle:forKey:"
- "_serverConnection"
- "_suCoreParsedDocumentation"
- "_taskID"
- "_totalRequiredFreeSpace"
- "_unarchivedSize"
- "_updatePowerPolicy"
- "_userDidAcceptTermsAndConditions"
- "_userDidManuallyTriggerInstall"
- "_userInstallRequestType"
- "_willProceedWithInstallation"
- "absoluteString"
- "adoptSimulationFileOfName:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "autoSUEndTime"
- "autoSUStartTime"
- "backgroundDownloadDisabledByServer"
- "boolValue"
- "bytes"
- "compare:"
- "compare:options:"
- "copy"
- "coreDescriptor"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentPhoneLanguage"
- "d"
- "d16@0:8"
- "dataWithBytes:length:"
- "dataWithContentsOfURL:"
- "dateOfLastScheduleOfAutoUpdate"
- "dateOfLastScheduleOfAutoUpdateNotification"
- "dateOfLastSentInstallNotification"
- "dealloc"
- "decodeBoolForKey:"
- "decodeFloatForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeTopLevelObjectOfClasses:forKey:error:"
- "defaultManager"
- "delegate"
- "description"
- "dictionary"
- "downloadWithDescriptor:andProgress:"
- "encodeBool:forKey:"
- "encodeFloat:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodedData"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "f"
- "f16@0:8"
- "fileExistsAtPath:"
- "finishDecoding"
- "finishEncoding"
- "getActivePairedDevice"
- "getAllDevices"
- "getCloudDescriptors:"
- "getLocalUrl"
- "hash"
- "humanReadableUpdateName"
- "init"
- "initForReadingFromData:error:"
- "initRequiringSecureCoding:"
- "initWithCoder:"
- "initWithContentsOfFile:options:error:"
- "initWithDelegate:"
- "initWithDocumentationAsset:"
- "initWithDocumentationBundleURL:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithMAAsset:"
- "initWithUUIDString:"
- "initialize"
- "installUpdate:"
- "installUpdate:passcode:"
- "integerValue"
- "isEqual:"
- "isEqualToString:"
- "isStalled"
- "length"
- "manager:didChangeProgressOnDownload:"
- "manager:didFailDownload:withError:"
- "manager:didFailInstallation:withError:"
- "manager:didFinishDownload:willProceedWithInstallation:waitingForAdmissionControl:"
- "manager:didFinishInstallation:"
- "manager:installationAwaitingUserInteraction:"
- "manager:installationOfUpdate:canProceed:"
- "manager:installationOfUpdate:willProceed:waitingForAdmissionControl:"
- "manager:scanRequestDidLocateUpdate:error:"
- "manager:userInstallRequestTypeDidChange:"
- "manager:willProceedWithInstallation:"
- "managerState:"
- "managerUserDidAcceptTermsAndConditionsForUpdate:"
- "marketingVersion"
- "mutableCopy"
- "numberWithInteger:"
- "numberWithLongLong:"
- "objectAtIndex:"
- "osName"
- "performMigration"
- "phoneLanguage"
- "preferencesIcon"
- "preferredLanguages"
- "preferredPhoneLanguages"
- "preparationSize"
- "purgeUpdate:completion:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "queue"
- "removeCloudDescriptor:"
- "scanForUpdates"
- "sendTermsRequest:"
- "serverConnection"
- "setAutoSUEndTime:"
- "setAutoSUStartTime:"
- "setBackgroundDownloadDisabledByServer:"
- "setCoreDescriptor:"
- "setDateOfLastScheduleOfAutoUpdate:"
- "setDateOfLastScheduleOfAutoUpdateNotification:"
- "setDateOfLastSentInstallNotification:"
- "setDelegate:"
- "setDenialReasons:"
- "setDescriptor:"
- "setDisplayTermsRequested:"
- "setDocumentation:"
- "setDocumentationBundleURL:"
- "setDocumentationID:"
- "setDownloadSize:"
- "setEstimatedTimeRemaining:"
- "setHumanReadableUpdateName:"
- "setInstallTonightScheduled:"
- "setInstallationSize:"
- "setIsAwaitingAdmissionControlForInstallation:"
- "setIsDone:"
- "setIsStalled:"
- "setLicenseAgreement:"
- "setManifest:"
- "setMarketingVersion:"
- "setMsuPrepareSize:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOsName:"
- "setPhase:"
- "setPhoneLanguage:"
- "setPortionComplete:"
- "setPreferencesIcon:"
- "setProductBuildVersion:"
- "setProductSystemName:"
- "setProductVersion:"
- "setProgress:"
- "setPublisher:"
- "setQueue:"
- "setReleaseNotes:"
- "setReleaseNotesSummary:"
- "setServerConnection:"
- "setSuCoreParsedDocumentation:"
- "setTaskID:"
- "setTotalRequiredFreeSpace:"
- "setUnarchivedSize:"
- "setUpdatePowerPolicy:"
- "setUserDidAcceptTermsAndConditions:"
- "setUserDidManuallyTriggerInstall:"
- "setUserInstallRequestType:"
- "setUserInstallRequestTypeForUpdate:userInstallRequestType:completion:"
- "setWillProceedWithInstallation:"
- "setWithArray:"
- "setWithObjects:"
- "sharedInstance"
- "softwareUpdateIconImagePath"
- "startDownload:"
- "startDownload:passcode:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "stringsMatch:second:"
- "suCoreParsedDocumentation"
- "summary"
- "supportsCapability:"
- "supportsInstallTonightWithCompletion:"
- "supportsSecureCoding"
- "totalRequiredFreeSpace"
- "unarchivedObjectOfClass:fromData:error:"
- "unsignedIntegerValue"
- "userDidAcceptTermsAndConditionsForUpdate:"
- "userDidAcceptTermsAndConditionsForUpdate:completion:"
- "userDidManuallyTriggerInstall"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@16q24@?32"
- "valueForProperty:"

```
