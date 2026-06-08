## HangTracerSettingsClient

> `/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient`

```diff

-398.2.0.0.0
-  __TEXT.__text: 0x167bc
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0xbbc
-  __TEXT.__const: 0x20b2
+412.0.0.0.0
+  __TEXT.__text: 0x1685c
+  __TEXT.__objc_methlist: 0xbec
+  __TEXT.__const: 0x20c2
+  __TEXT.__cstring: 0x310b
   __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__cstring: 0x2f59
-  __TEXT.__oslogstring: 0x375
+  __TEXT.__oslogstring: 0x54c
   __TEXT.__dlopen_cstrs: 0xaf
   __TEXT.__ustring: 0x822
   __TEXT.__swift5_typeref: 0x4c3

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x194
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__unwind_info: 0x658
-  __TEXT.__objc_classname: 0x173
-  __TEXT.__objc_methname: 0x2707
-  __TEXT.__objc_methtype: 0x3c8
-  __TEXT.__objc_stubs: 0x1d40
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0xd08
+  __TEXT.__unwind_info: 0x650
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xd58
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_selrefs: 0xaf8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x158
-  __AUTH_CONST.__auth_got: 0x468
+  __DATA_CONST.__got: 0x360
   __AUTH_CONST.__const: 0x608
   __AUTH_CONST.__cfstring: 0x38c0
-  __AUTH_CONST.__objc_const: 0x1550
+  __AUTH_CONST.__objc_const: 0x1570
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x4b0
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x6f8
-  __DATA.__bss: 0x3630
+  __DATA.__bss: 0x36a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/HangTracer.framework/HangTracer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BC3E1AFB-83F4-31A9-95AA-D1F14F91DFF7
-  Functions: 761
-  Symbols:   1654
-  CStrings:  1535
+  UUID: DD6716B0-F7BB-3C57-9D72-06375848495B
+  Functions: 784
+  Symbols:   1730
+  CStrings:  1020
 
Symbols:
+ -[HTInternalSettings hudOpacity]
+ -[HTInternalSettings isHUDClientsEnabled]
+ -[HTInternalSettings setHUDClientsEnabled:]
+ -[HTInternalSettings setHUDOpacity:]
+ _AnalyticsSendEventLazy
+ _CAEventHTPrefsTypeMismatch
+ _CAKeyHTPrefsTypeMismatch
+ _CAKeyHTPrefsTypeMismatchClassName
+ _CAKeyHTPrefsTypeMismatchExpectedSelector
+ _CAKeyHTPrefsTypeMismatchKeyName
+ _CAKeyHTPrefsTypeMismatchValue
+ _HTUIInternalDisplaySectionFooter
+ _HTUIInternalDisplaySectionFooter.str
+ _HTUIInternalDisplaySectionTitle
+ _HTUIInternalDisplaySectionTitle.str
+ _HTUIInternalEnableHUDOverlaysToggleTitle
+ _HTUIInternalEnableHUDOverlaysToggleTitle.str
+ _HTUIInternalHUDOptionsSectionTitle
+ _HTUIInternalHUDOptionsSectionTitle.str
+ _HTUIInternalHUDOverlaysTitle
+ _HTUIInternalHUDOverlaysTitle.str
+ _HTUIInternalHangTracerHUDTitle
+ _HTUIInternalHangTracerHUDTitle.str
+ _HTUIInternalKillHUDProcessFooter
+ _HTUIInternalKillHUDProcessFooter.str
+ _HTUIInternalLocalizedString.cold.1
+ _HTUIInternalLocalizedString.cold.2
+ _HTUIInternalOpacityTitle
+ _HTUIInternalOpacityTitle.str
+ _HTUIInternalPerformanceDashboardTitle
+ _HTUIInternalPerformanceDashboardTitle.str
+ _HTUIInternalPerformanceIssuesSectionTitle
+ _HTUIInternalPerformanceIssuesSectionTitle.str
+ _HTUIInternalProcessTerminationsHUDTitle
+ _HTUIInternalProcessTerminationsHUDTitle.str
+ _HTUIInternalViewAllDetectedIssues
+ _HTUIInternalViewAllDetectedIssues.str
+ _NSStringFromSelector
+ ___32-[HTInternalSettings hudOpacity]_block_invoke
+ ___32-[HTInternalSettings hudOpacity]_block_invoke_2
+ ___34-[HTInternalSettings hudThreshold]_block_invoke
+ ___34-[HTInternalSettings hudThreshold]_block_invoke_2
+ ___HTInternalSettingsBundle_block_invoke.cold.1
+ ___HTInternalSettingsBundle_block_invoke.cold.2
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.125
+ ___kCFBooleanTrue
+ _hudOpacity.onceToken
+ _hudThreshold.onceToken
+ _kHTPrefsHUDClientsEnabled
+ _kHTPrefsHUDOpacity
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$description
+ _objc_msgSend$isHUDClientsEnabled
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x6
+ _object_getClassName
+ _swift_release_x19
- _OUTLINED_FUNCTION_3
- ___block_literal_global.126
- _objc_autorelease
- _swift_release
CStrings:
+ "Failed to find localization string for key %{private}@, falling back to %{private}@"
+ "Failed to load NSBundle at path: %{private}@ because the path does not exist"
+ "Failed to load NSBundle at path: %{private}@ despite the path existing"
+ "Found localization string '%{private}@' for key %{private}@"
+ "HTUIInternalDisplaySectionFooter"
+ "HTUIInternalDisplaySectionTitle"
+ "HTUIInternalEnableHUDOverlaysToggleTitle"
+ "HTUIInternalHUDOptionsSectionTitle"
+ "HTUIInternalHUDOverlaysTitle"
+ "HTUIInternalHangTracerHUDTitle"
+ "HTUIInternalKillHUDProcessFooter"
+ "HTUIInternalOpacityTitle"
+ "HTUIInternalPerformanceDashboardTitle"
+ "HTUIInternalPerformanceIssuesSectionTitle"
+ "HTUIInternalProcessTerminationsHUDTitle"
+ "HTUIInternalViewAllDetectedIssues"
+ "Localization string for key %{private}@ is nil despite specifying fallback value: %{private}@"
+ "OS does not have internal content, not attempting to load bundle at path %{private}@"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HTDeveloperAppsFinderDelegate>\""
- "@\"HTDeveloperSettings\""
- "@\"HTHangReporterService\""
- "@\"LSApplicationRecord\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSMeasurementFormatter\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSPredicate\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUserDefaults\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@?16@?24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8B16B20@24Q32@40"
- "@56@0:8@16@24@32@40@48"
- "@72@0:8@16@24@32d40@48@56@64"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B28@0:8Q16B24"
- "B32@0:8Q16Q24"
- "HTDeveloperApp"
- "HTDeveloperAppsFinder"
- "HTDeveloperSettings"
- "HTHang"
- "HTHangExtendedAttributes"
- "HTHangReporterService"
- "HTHangSymbolicator"
- "HTHangsAnalytics"
- "HTHangsDataEntry"
- "HTHangsDataFinder"
- "HTInternalSettings"
- "HTProcessExitFilteringConfiguration"
- "HTProcessTerminationSettings"
- "JSONObjectWithData:options:error:"
- "LSApplicationWorkspaceObserverProtocol"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "Q24@0:8Q16"
- "T#,R"
- "T@\"<HTDeveloperAppsFinderDelegate>\",W,N,V_delegate"
- "T@\"HTHangSymbolicator\",R"
- "T@\"HTProcessTerminationSettings\",R,N"
- "T@\"LSApplicationRecord\",R,C,N,V_processRecord"
- "T@\"NSArray\",&,N,V_allowedProcessNames"
- "T@\"NSArray\",C,N"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,N"
- "T@\"NSDate\",R,C,N,V_creationDate"
- "T@\"NSDate\",R,N,V_createdAt"
- "T@\"NSDate\",R,N,V_creationDate"
- "T@\"NSDictionary\",&,N,V_allowedSubReasons"
- "T@\"NSMutableArray\",&,N,V_folderWatchDispatchSrcs"
- "T@\"NSMutableDictionary\",&,N,V_logCountByPath"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_folderWatchTaskQueue"
- "T@\"NSPredicate\",&,N,V_hangLogPredicate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_bundleID"
- "T@\"NSString\",R,C,N,V_bundleId"
- "T@\"NSString\",R,C,N,V_creationDate"
- "T@\"NSString\",R,C,N,V_duration"
- "T@\"NSString\",R,C,N,V_hangID"
- "T@\"NSString\",R,C,N,V_hangId"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_path"
- "T@\"NSString\",R,C,N,V_processBundleID"
- "T@\"NSString\",R,C,N,V_processPath"
- "T@\"NSString\",R,N,V_bundleDisplayName"
- "T@\"NSString\",R,N,V_bundleExecutable"
- "T@\"NSString\",R,N,V_bundleID"
- "T@\"NSString\",R,N,V_bundleName"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_processPath"
- "T@?,C,N,V_logUpdateCallback"
- "T@?,C,N,V_tailspinSavedCallback"
- "TB,N"
- "TB,N,GisEnabled"
- "TB,N,GisForceQuitDetectionEnabled,SsetForceQuitDetectionEnabled:"
- "TB,N,GisHUDEnabled,SsetHUDEnabled:"
- "TB,N,V_allowListingOnDemandVPNs"
- "TB,N,V_allowsAllProcesses"
- "TB,N,V_allowsCriticalProcesses"
- "TB,N,V_doNotFilter"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisInternalBuild"
- "TB,R,N,V_isBeingProcessed"
- "TB,R,N,V_isLogFile"
- "TQ,N"
- "TQ,N,V_allowedReasons"
- "TQ,R"
- "TQ,R,N"
- "Td,R,N,V_duration"
- "Tq,N"
- "Tq,N,SsetHUDThreshold:"
- "Tq,R,N"
- "URLByAppendingPathComponent:"
- "URLByDeletingLastPathComponent"
- "URLByDeletingPathExtension"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_addTrackedReason:propagatingSubReasons:"
- "_allowListingOnDemandVPNs"
- "_allowedProcessNames"
- "_allowedReasons"
- "_allowedSubReasons"
- "_allowsAllProcesses"
- "_allowsCriticalProcesses"
- "_bundleDisplayName"
- "_bundleExecutable"
- "_bundleID"
- "_bundleId"
- "_bundleName"
- "_createdAt"
- "_creationDate"
- "_defaults"
- "_delegate"
- "_doNotFilter"
- "_duration"
- "_folderWatchDispatchSrcs"
- "_folderWatchTaskQueue"
- "_hangID"
- "_hangId"
- "_hangLogPredicate"
- "_hangReporterConnection"
- "_hangReporterService"
- "_identifier"
- "_isBeingProcessed"
- "_isLogFile"
- "_logCountByPath"
- "_logUpdateCallback"
- "_longDurationFormatter"
- "_name"
- "_path"
- "_processBundleID"
- "_processPath"
- "_processRecord"
- "_queue"
- "_removeTrackedReason:"
- "_removeTrackedReason:propagatingSubReasons:"
- "_removeTrackedSubReason:forReason:"
- "_savedSettingsDefaults"
- "_setTrackedReasons:propagatingSubReasons:"
- "_setTrackedSubReasons:forReason:"
- "_setTracksAllProcesses:"
- "_setTracksCriticalProcesses:"
- "_settings"
- "_shortDurationFormatter"
- "_tailspinSavedCallback"
- "_trackAllDefaultReasons"
- "_trackAllReasons"
- "_trackAllSubReasonsForReason:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addTrackedProcessNamed:"
- "addTrackedReason:"
- "addTrackedSubReason:forReason:"
- "allHeaderFields"
- "allKeys"
- "allReasonsValue"
- "allSubReasonsValueForReason:"
- "allowListingOnDemandVPNs"
- "appRecordWithBundleId:cachedAppRecords:"
- "appendData:"
- "applicationIconDidChange:"
- "applicationInstallsArePrioritized:arePaused:"
- "applicationInstallsDidCancel:"
- "applicationInstallsDidChange:"
- "applicationInstallsDidPause:"
- "applicationInstallsDidPrioritize:"
- "applicationInstallsDidResume:"
- "applicationInstallsDidStart:"
- "applicationInstallsDidUpdateIcon:"
- "applicationStateDidChange:"
- "applicationsDidChangePersonas:"
- "applicationsDidFailToInstall:"
- "applicationsDidFailToUninstall:"
- "applicationsDidInstall:"
- "applicationsDidUninstall:"
- "applicationsDidUpdateMetadata:"
- "applicationsWillInstall:"
- "applicationsWillUninstall:"
- "applySettings"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attributesOfItemAtPath:error:"
- "autorelease"
- "availableReasons"
- "availableSubReasonsForReason:"
- "availableThresholdsLongNames"
- "availableThresholdsShortNames"
- "availableThresholdsValues"
- "boolForKey:"
- "boolValue"
- "bundleDisplayName"
- "bundleExecutable"
- "bundleForClass:"
- "bundleID"
- "bundleId"
- "bundleIdentifier"
- "bundleName"
- "bundleWithPath:"
- "bytes"
- "canSymbolicateLogFile:"
- "capitalizedString"
- "checkProxiesForDeveloperAppAndNotifyDelegate:"
- "checkResourceIsReachableAndReturnError:"
- "class"
- "code"
- "compare:"
- "componentsSeparatedByString:"
- "configurationAllowingAllProcesses:criticalProcesses:processNames:reasons:subReasons:"
- "configurationFromPrefs:"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "controlCharacterSet"
- "copy"
- "correspondingApplicationRecord"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createdAt"
- "creationDate"
- "criticalProcessNames"
- "d"
- "d16@0:8"
- "data"
- "dataUsingEncoding:"
- "dataWithContentsOfURL:options:error:"
- "dataWithLength:"
- "databaseWasRebuilt"
- "dateFromString:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
- "decodeObjectOfClass:forKey:"
- "defaultCenter"
- "defaultManager"
- "defaultWorkspace"
- "delegate"
- "description"
- "developerAppsDidChangeForFinder:"
- "deviceManagementPolicyDidChange:"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "displayName"
- "displayTerminationsInHUD"
- "doNotFilter"
- "domain"
- "doubleValue"
- "duration"
- "durationLevel"
- "enabled"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "enumeratorWithOptions:"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:isDirectory:"
- "fileSize"
- "fileSystemRepresentation"
- "fileURLWithPath:isDirectory:"
- "filterUsingPredicate:"
- "filteredArrayUsingPredicate:"
- "findApps:"
- "findEventsFilteringDeveloperApps:completionHandler:"
- "findProcessingEventsFilteringDeveloperApps:completionHandler:"
- "firstObject"
- "folderWatchDispatchSrcs"
- "folderWatchTaskQueue"
- "forceQuitDetectionEnabled"
- "forceQuitDetectionThreshold"
- "formUnionWithCharacterSet:"
- "getExtendedAttributeNamed:forFileAtPath:"
- "getFilteredLogURLsForPath:error:"
- "getProcessingHangsWithCompletion:"
- "getResourceValue:forKey:error:"
- "groupEntriesByHangID:"
- "hangID"
- "hangId"
- "hangLogPredicate"
- "hangReporterDidSaveTailspin:"
- "hangTracerThreshold"
- "hangsDataEntryAtPath:error:"
- "hangsDataEntryWithFullPath:extendedAttributes:cachedAppRecords:"
- "hasPrefix:"
- "hasSuffix:"
- "hash"
- "helperPlaceholdersInstalled:"
- "helperPlaceholdersUninstalled:"
- "hudEnabled"
- "hudThreshold"
- "identifier"
- "indexOfObject:"
- "indexesOfObjectsPassingTest:"
- "infoDictionary"
- "init"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithCoder:"
- "initWithData:encoding:"
- "initWithDefaults:"
- "initWithDefaults:savedSettingsDefaults:"
- "initWithDoubleValue:unit:"
- "initWithFilePath:"
- "initWithLogUpdateCallback:tailspinSavedCallback:"
- "initWithName:bundleID:"
- "initWithName:bundleID:bundleExecutable:bundleName:bundleDisplayName:"
- "initWithPath:hangID:creationDate:duration:processBundleID:processPath:processRecord:"
- "initWithSuiteName:"
- "initWithXPCDictionary:"
- "intValue"
- "integerForKey:"
- "integerValue"
- "internalBuild"
- "isBeingProcessed"
- "isDeveloperApp"
- "isEqual:"
- "isEqualToString:"
- "isForceQuitDetectionEnabled"
- "isHUDEnabled"
- "isInternal"
- "isInternalBuild"
- "isKindOfClass:"
- "isLogFile"
- "isLogFileSymbolicated:"
- "isMemberOfClass:"
- "isOnDemandEnabled"
- "isProfileValidated"
- "isProxy"
- "isSystemConditionsHUDEnabled"
- "lastObject"
- "lastPathComponent"
- "length"
- "loadAllFromPreferencesWithCompletionHandler:"
- "localizedName"
- "localizedStandardRangeOfString:"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "logCountByPath"
- "logUpdateCallback"
- "milliseconds"
- "moveItemAtURL:toURL:error:"
- "mutableBytes"
- "mutableCopy"
- "name"
- "networkUsageChanged:"
- "nextObject"
- "numberFormatter"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKey:ofClass:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "observeLaunchProhibitedApps"
- "orderedSetWithArray:"
- "path"
- "pathExtension"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginsDidInstall:"
- "pluginsDidUninstall:"
- "pluginsWillUninstall:"
- "predicateWithBlock:"
- "predicateWithFormat:"
- "processBundleID"
- "processPath"
- "processRecord"
- "q16@0:8"
- "release"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeTrackedProcessNamed:"
- "removeTrackedReason:"
- "removeTrackedSubReason:forReason:"
- "requestWithURL:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "runloopHangTimeoutDurationMSec"
- "seconds"
- "self"
- "sendActivationEvent:developerAppCount:"
- "sendHangThresholdChangedEvent:"
- "sendLogSharedEvent"
- "setAllowListingOnDemandVPNs:"
- "setAllowedProcessNames:"
- "setAllowedReasons:"
- "setAllowedSubReasons:"
- "setAllowsAllProcesses:"
- "setAllowsCriticalProcesses:"
- "setBool:forKey:"
- "setDelegate:"
- "setDisplayTerminationsInHUD:"
- "setDoNotFilter:"
- "setEnabled:"
- "setErrorHandler:"
- "setFilter:"
- "setFloat:forKey:"
- "setFolderWatchDispatchSrcs:"
- "setFolderWatchTaskQueue:"
- "setForceQuitDetectionEnabled:"
- "setForceQuitDetectionThreshold:"
- "setHTTPMethod:"
- "setHUDEnabled:"
- "setHUDThreshold:"
- "setHangLogPredicate:"
- "setHangTracerThreshold:"
- "setInteger:forKey:"
- "setLogCountByPath:"
- "setLogUpdateCallback:"
- "setMaximumFractionDigits:"
- "setNumberFormatter:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setSystemConditionsHUDEnabled:"
- "setTailspinSavedCallback:"
- "setTrackedProcessNames:"
- "setTrackedReasons:"
- "setTrackedSubReasons:forReason:"
- "setTracksAllProcesses:"
- "setTracksCriticalProcesses:"
- "setUnitOptions:"
- "setUnitStyle:"
- "setValue:forHTTPHeaderField:"
- "sharedPrefs"
- "sharedSession"
- "sharedSettings"
- "sharedSymbolicator"
- "sortUsingSelector:"
- "sortedArrayUsingComparator:"
- "sortedEntriesByFileType:"
- "sortedHangIDsByCreationDate:"
- "status"
- "statusCode"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByDeletingPathExtension"
- "stringByTrimmingCharactersInSet:"
- "stringFromMeasurement:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "superclass"
- "supportsSecureCoding"
- "symbolicateLogFile:completion:"
- "symbolicateLogFiles:completion:"
- "symbolicatedLogURLForFile:"
- "tailspinSavedCallback"
- "temporaryDirectory"
- "trackAllReasons"
- "trackAllSubReasonsForReason:"
- "trackedProcessNames"
- "trackedReasons"
- "trackedSubReasonsForReason:"
- "tracksAllProcesses"
- "tracksCriticalProcesses"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "uploadTaskWithRequest:fromData:completionHandler:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8B16@?20"
- "v28@0:8B16Q20"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16Q24"
- "whitespaceCharacterSet"
- "writeToURL:options:error:"
- "zone"

```
