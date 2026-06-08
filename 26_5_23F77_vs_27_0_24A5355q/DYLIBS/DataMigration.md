## DataMigration

> `/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration`

```diff

-2842.4.0.0.0
-  __TEXT.__text: 0x76ac
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x920
-  __TEXT.__cstring: 0x161a
+2851.0.0.0.0
+  __TEXT.__text: 0x75f8
+  __TEXT.__objc_methlist: 0x960
+  __TEXT.__cstring: 0x1769
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__unwind_info: 0x2f0
-  __TEXT.__objc_classname: 0x164
-  __TEXT.__objc_methname: 0x1898
-  __TEXT.__objc_methtype: 0x255
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0x168
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x458
+  __DATA_CONST.__got: 0x168
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xee0
+  __AUTH_CONST.__cfstring: 0x1060
   __AUTH_CONST.__objc_const: 0xdc8
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x78
   __DATA.__bss: 0x58

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88A07678-21C6-3D20-8D04-1C658BA03B4A
-  Functions: 236
-  Symbols:   934
-  CStrings:  595
+  UUID: 0DB9FD3F-4071-38C3-A718-98A48A3D85A5
+  Functions: 244
+  Symbols:   955
+  CStrings:  302
 
Symbols:
+ -[DMClientAPIController requiredPreboardMode]
+ -[DMEnvironment isDarkBoot]
+ -[DMEnvironment isFullTracingEnabled]
+ -[DMEnvironment isTracingEnabledForAllPlugins]
+ -[DMEnvironment isTracingEnabledForPluginIdentifier:]
+ -[DMEnvironment traceDuration]
+ _CFPreferencesGetAppIntegerValue
+ _DMGetRequiredPreboardMode
+ _DMPreboardModeDescription
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$requiredPreboardMode
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
+ _sysctlbyname
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x28
CStrings:
+ "%s: Connection failed"
+ "%s: Got mode: %@"
+ "%s: XPC error: %s"
+ "%s: failed to query kern.darkboot sysctl: %d"
+ "%s: kern.darkboot = %d"
+ "-[DMClientAPIController requiredPreboardMode]"
+ "-[DMEnvironment isDarkBoot]"
+ "DMEnableFullTracing"
+ "DMPluginsToTrace"
+ "DMTraceAllPlugins"
+ "DMTraceDurationSeconds"
+ "kern.darkboot"
+ "monitor"
+ "none"
+ "preboardMode"
+ "unlock"
- ".cxx_destruct"
- "@\"DMEnvironment\""
- "@\"DMXPCConnection\""
- "@\"NSBundle\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "@28@0:8B16@20"
- "@28@0:8^*16i24"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "@40@0:8Q16Q24@?32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B40@0:8@16B24@28B36"
- "DMBuildVersion"
- "DMClientAPIController"
- "DMConnection"
- "DMContext"
- "DMContextManager"
- "DMEnvironment"
- "DMInducedPluginFailureManager"
- "DMMigrationDeferredExitManager"
- "DMMigrationPluginWrapperConnection"
- "DMPluginFileSystemRep"
- "DMPluginParameters"
- "DMTimer"
- "DMUserDataDispositionManager"
- "DMXPCConnection"
- "DataClassMigrator"
- "I"
- "I16@0:8"
- "I20@0:8I16"
- "I24@0:8@16"
- "Q"
- "Q16@0:8"
- "T@\"DMEnvironment\",&,N,V_environment"
- "T@\"NSDictionary\",&,N,V_context"
- "T@\"NSDictionary\",&,N,V_dispositionSupersetOfContext"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_connection"
- "T@\"NSString\",&,N,V_restoredBackupBuildVersion"
- "T@\"NSString\",&,N,V_restoredBackupDeviceName"
- "T@\"NSString\",&,N,V_restoredBackupProductType"
- "T@\"NSString\",C,N,V_backupDeviceUUID"
- "T@\"NSString\",C,N,V_dmBundleIdentifier"
- "T@\"NSString\",R,N,V_bundleIdentifier"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_path"
- "T@?,C,N,V_fireBlock"
- "T@?,C,V_interruptionHandler"
- "T@?,C,V_invalidationHandler"
- "T@?,C,V_messageHandler"
- "TB,N,V_didUpgrade"
- "TB,N,V_testMigrationInfrastructureOnly"
- "TB,R,N"
- "TI,N,V_userDataDisposition"
- "TQ,N,V_connectionMigrationMaximumAttempts"
- "TQ,N,V_secondsBeforeFirstFire"
- "TQ,N,V_secondsOfLeeway"
- "Td,N,V_connectionMigrationTimeIntervalToLastRetryDate"
- "UTF8String"
- "UUID"
- "UUIDString"
- "_backupDeviceUUID"
- "_bundle"
- "_bundleIdentifier"
- "_connection"
- "_connectionMigrationMaximumAttempts"
- "_connectionMigrationTimeIntervalToLastRetryDate"
- "_context"
- "_crash"
- "_deferralDuration"
- "_didReceivePid"
- "_didUpgrade"
- "_dispositionSupersetOfContext"
- "_dmBundleIdentifier"
- "_entriesHavingBoolValue"
- "_entriesHavingStringValue"
- "_environment"
- "_exitClean"
- "_fireBlock"
- "_handleMessage:"
- "_hang"
- "_interruptionHandler"
- "_invalidationHandler"
- "_isDeferringExit"
- "_isInternalBuild"
- "_messageHandler"
- "_migrateWithConnection:checkNecessity:lastRelevantPlugin:testMigrationInfrastructureOnly:"
- "_name"
- "_path"
- "_pathsContainingPossiblePluginDirectory"
- "_pid"
- "_queue"
- "_replyQueue"
- "_resetGlobalState"
- "_restoredBackupBuildVersion"
- "_restoredBackupDeviceName"
- "_restoredBackupProductType"
- "_secondsBeforeFirstFire"
- "_secondsOfLeeway"
- "_serialQueue"
- "_testMigrationInfrastructureOnly"
- "_timer"
- "_userDataDisposition"
- "addContext:toXPCDictionary:"
- "addInducedFailure:forPluginIdentifier:"
- "addObject:"
- "allInducedFailures"
- "allReps"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "backupDeviceUUIDFromDispositionSupersetOfContext:"
- "backupSourceDispositionFlagsFromDispositionFlags:"
- "basicDispositionFlagsFromDispositionFlags:"
- "blockUntilPreferencesFlush"
- "boolValue"
- "bundleIdentifier"
- "bundleWithPath:"
- "cancel"
- "cancelDeferredExit"
- "cancelDeferredExitWithConnection:"
- "cancelSynchronously"
- "changeVisibility:completion:"
- "clearContext"
- "compare:"
- "compare:options:"
- "connection"
- "connectionMigrationMaximumAttempts"
- "connectionMigrationTimeIntervalToLastRetryDate"
- "containsObject:"
- "contentsOfDirectoryAtPath:error:"
- "context"
- "contextFromArguments:withCount:"
- "contextFromXPCDictionary:"
- "contextPath"
- "continuousIntegrationMarkerPref"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "dataClassMigratorForBundleAtPath:"
- "dataWithBytes:length:"
- "date"
- "dateByAddingTimeInterval:"
- "dealloc"
- "defaultManager"
- "deferExit"
- "deferExitWithConnection:"
- "descriptionFromDispositionFlags:"
- "deviceModeIsSharediPad"
- "dictionaryWithObjects:forKeys:count:"
- "didMigrateBackupFromDifferentDevice"
- "didReceivePid"
- "didRestoreFromBackup"
- "didRestoreFromCloudBackup"
- "didUpgrade"
- "dispositionFlagsFromDispositionDict:"
- "dispositionSupersetOfContext"
- "dmBundleIdentifier"
- "dm_migrationRebootCountPrefWithRebootCount:buildVersion:"
- "dm_migrationRebootCountPref_buildVersion"
- "dm_migrationRebootCountPref_buildVersionKey"
- "dm_migrationRebootCountPref_rebootCount"
- "dm_migrationRebootCountPref_rebootCountKey"
- "dmlmr_buildVersion"
- "dmlmr_buildVersionKey"
- "dmlmr_lastMigrationResultsWithSuccess:buildVersion:"
- "dmlmr_success"
- "dmlmr_successKey"
- "environment"
- "errorWithDomain:code:userInfo:"
- "fireBlock"
- "forceMigrationOnNextRebootWithUserDataDisposition:context:"
- "handleMessage:"
- "hasEntitlement:"
- "i16@0:8"
- "implementMigrationPluginResults"
- "inducedPluginFailures"
- "init"
- "initWithConnection:"
- "initWithDispositionSupersetOfContext:backupDeviceUUID:"
- "initWithEnvironment:"
- "initWithName:atEnclosingPath:"
- "initWithSecondsBeforeFirstFire:secondsOfLeeway:fireBlock:"
- "initWithServiceName:"
- "interruptionHandler"
- "invalidate"
- "invalidationHandler"
- "isBuildVersion:equalToBuildVersion:"
- "isBundleValid"
- "isDeviceUsingEphemeralStorage"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToString:"
- "isMainThread"
- "isMemberOfClass:"
- "isSubclassOfClass:"
- "lastBuildVersionPref"
- "lastMigrationResultsPref"
- "length"
- "loadAndReturnError:"
- "messageHandler"
- "migrateCheckingNecessity:lastRelevantPlugin:testMigrationInfrastructureOnly:"
- "migrationPhaseDescription"
- "migrationPluginResults:"
- "migrationPluginResultsPref"
- "migrationRebootCount"
- "migrationRebootCountPref"
- "mutableCopy"
- "name"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "orderedPluginIdentifiers"
- "path"
- "performMigration"
- "pidForWatchdog"
- "principalClass"
- "progressHostIsReady"
- "q32@0:8B16@20B28"
- "removeObjectAtIndex:"
- "reportMigrationFailure"
- "restoredBackupBuildVersion"
- "restoredBackupDeviceName"
- "restoredBackupProductType"
- "resume"
- "runPluginAtPath:withIdentifier:parameters:completion:"
- "secondsBeforeFirstFire"
- "secondsOfLeeway"
- "sendMessage:replyHandler:"
- "sendMessageSync:"
- "setBackupDeviceUUID:"
- "setConnectionMigrationMaximumAttempts:"
- "setConnectionMigrationTimeIntervalToLastRetryDate:"
- "setContext:"
- "setDidUpgrade:"
- "setDispositionSupersetOfContext:"
- "setDmBundleIdentifier:"
- "setEnvironment:"
- "setFireBlock:"
- "setInducedPluginFailures:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLastBuildVersionPref:"
- "setLastMigrationResultsPref:"
- "setMessageHandler:"
- "setMigrationPluginResultsPref:"
- "setMigrationRebootCount:"
- "setMigrationRebootCountPref:"
- "setObject:forKeyedSubscript:"
- "setRestoredBackupBuildVersion:"
- "setRestoredBackupDeviceName:"
- "setRestoredBackupProductType:"
- "setSecondsBeforeFirstFire:"
- "setSecondsOfLeeway:"
- "setTestMigrationInfrastructureOnly:"
- "setTimer:"
- "setUserDataDisposition:"
- "setUserDataDispositionPref:"
- "setWithArray:"
- "sharedInstance"
- "shouldImposePluginArtificialHang"
- "shouldInduceFailureForPluginIdentifier:"
- "shouldPreserveSettingsAfterRestore"
- "shouldWatchdogPluginsAfterTimeout"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "suppressMigrationPluginWrapperExitMarkerPref"
- "targetForegroundUserSessionIfNecessary"
- "testMigrationUIWithProgress:forceInvert:"
- "timer"
- "unarchivedDictionaryWithKeysOfClasses:objectsOfClasses:fromData:error:"
- "unarchivedObjectOfClass:fromData:error:"
- "unsignedIntegerValue"
- "userDataDispositionAuxiliaryData"
- "userDataDispositionPref"
- "userSessionIsLoginWindow"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v28@0:8B16@?20"
- "v28@0:8I16@20"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@24"
- "v48@0:8@16@24@32@?40"
- "waitForExecutePluginsSignalMarkerPref"
- "wasPasscodeSetInBackup"

```
