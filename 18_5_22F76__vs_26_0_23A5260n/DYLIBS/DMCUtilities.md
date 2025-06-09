## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-20.5.1.2.0
-  __TEXT.__text: 0x31534
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x2a0c
-  __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x734
-  __TEXT.__cstring: 0x335d
-  __TEXT.__oslogstring: 0x4afc
+43.0.0.0.0
+  __TEXT.__text: 0x33848
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x2cac
+  __TEXT.__const: 0x150
+  __TEXT.__gcc_except_tab: 0x77c
+  __TEXT.__cstring: 0x3640
+  __TEXT.__oslogstring: 0x4f44
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0xd48
-  __TEXT.__objc_classname: 0x450
-  __TEXT.__objc_methname: 0x8f61
-  __TEXT.__objc_methtype: 0x12c5
-  __TEXT.__objc_stubs: 0x59e0
-  __DATA_CONST.__got: 0x658
-  __DATA_CONST.__const: 0x1088
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__unwind_info: 0xdc0
+  __TEXT.__objc_classname: 0x48b
+  __TEXT.__objc_methname: 0x974b
+  __TEXT.__objc_methtype: 0x131b
+  __TEXT.__objc_stubs: 0x5fa0
+  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__const: 0x1168
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2270
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x740
-  __AUTH_CONST.__const: 0xcc0
-  __AUTH_CONST.__cfstring: 0x3b80
-  __AUTH_CONST.__objc_const: 0x3d60
-  __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x1d0
+  __DATA_CONST.__objc_selrefs: 0x2478
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__const: 0xd20
+  __AUTH_CONST.__cfstring: 0x3f60
+  __AUTH_CONST.__objc_const: 0x4150
+  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH.__objc_data: 0xe60
+  __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0x2b1
-  __DATA.__bss: 0x950
+  __DATA.__bss: 0x968
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 071E22AE-C231-3688-8813-004ED398124D
-  Functions: 1298
-  Symbols:   4741
-  CStrings:  2998
+  UUID: 2FE97219-3E78-3E4B-B947-86DA1B62B13F
+  Functions: 1360
+  Symbols:   4973
+  CStrings:  3182
 
Symbols:
+ +[DMCAppIdentifier newAppIdentifierWithIdentifier:]
+ +[DMCFeatureFlags isRRTSEnabled]
+ +[DMCFeatureFlags isRRTSMDMTimeoutEnabled]
+ +[DMCFeatureFlags isRRTSUEATimeoutEnabled]
+ +[DMCFeatureOverrides _allOverrides]
+ +[DMCFeatureOverrides awaitSystemDeletableAppsTimeoutWithDefaultValue:]
+ +[DMCFeatureOverrides bootstrapTokenOverride]
+ +[DMCFeatureOverrides depPushTokenPeriodicSyncIntervalWithDefaultValue:]
+ +[DMCFeatureOverrides shouldPreserveUserDefaultsForReturnToService]
+ +[DMCFeatureOverrides shouldSimulateRapidReturnToService]
+ +[DMCFeatureOverrides shouldSuppressRRTSOnIdleTimeout]
+ +[DMCFeatureOverrides simulatedWiFiProfile]
+ -[DMCAppIdentifier .cxx_destruct]
+ -[DMCAppIdentifier bundleID]
+ -[DMCAppIdentifier identifier]
+ -[DMCAppIdentifier initWithBundleID:personaID:]
+ -[DMCAppIdentifier personaID]
+ -[DMCAppIdentifier setBundleID:]
+ -[DMCAppIdentifier setPersonaID:]
+ -[DMCObliterationShelter _createFailToWriteFileErrorWithFilePath:]
+ -[DMCObliterationShelter _generateShelteredDetailsForLogging]
+ -[DMCObliterationShelter additionalDetails]
+ -[DMCObliterationShelter isRapidReturnToService]
+ -[DMCObliterationShelter isSharediPad]
+ -[DMCObliterationShelter setAdditionalDetails:]
+ -[DMCObliterationShelter setIsRapidReturnToService:]
+ -[DMCObliterationShelter setIsSharediPad:]
+ -[DMCObliterationShelter setUserDefaults:]
+ -[DMCObliterationShelter userDefaults]
+ -[DMCSnapshotUtilities _executeSnapshotActionAtPath:action:]
+ -[DMCSnapshotUtilities captureSnapshotAtPath:name:]
+ -[DMCSnapshotUtilities captureSystemVolumeSnapshotWithName:]
+ -[DMCSnapshotUtilities deleteSnapshotAtPath:name:]
+ -[DMCSnapshotUtilities deleteSystemVolumeSnapshotWithName:]
+ -[DMCWiFiUtilities .cxx_destruct]
+ -[DMCWiFiUtilities _noRecoveryNetworkError]
+ -[DMCWiFiUtilities _timeoutError]
+ -[DMCWiFiUtilities cancelTimeoutBlock]
+ -[DMCWiFiUtilities cleanup]
+ -[DMCWiFiUtilities config]
+ -[DMCWiFiUtilities dealloc]
+ -[DMCWiFiUtilities enableAutoJoinIfNeededWithTimeout:completionHandler:]
+ -[DMCWiFiUtilities haveNetwork]
+ -[DMCWiFiUtilities init]
+ -[DMCWiFiUtilities interface]
+ -[DMCWiFiUtilities powerOn]
+ -[DMCWiFiUtilities setConfig:]
+ -[DMCWiFiUtilities setInterface:]
+ -[DMCWiFiUtilities setPower:error:]
+ -[DMCWiFiUtilities setTimeoutBlock:]
+ -[DMCWiFiUtilities timeoutBlock]
+ -[DMCWiFiUtilities timeoutQueue]
+ _CWFEventAutoJoinStatusKey
+ _DMCDatabaseDirectory
+ _DMCDefaultsKeyAwaitSystemDeletableAppsTimeout
+ _DMCDefaultsKeyBootstrapTokenOverride
+ _DMCDefaultsKeyDEPPushTokenSyncInterval
+ _DMCDefaultsKeyPreserveUserDefaultsForRTS
+ _DMCDefaultsKeySimulateRapidReturnToService
+ _DMCDefaultsKeySimulatedWiFiProfile
+ _DMCDefaultsKeySuppressRRTSOnIdleTimeout
+ _DMCEventsTopicRTS
+ _DMCMigrationErrorDomain
+ _DMCNagDeadlineNotification
+ _DMCNagItemKey
+ _DMCNagItemsDirectory
+ _DMCNagItemsDirectory.cold.1
+ _DMCNagItemsDirectory.once
+ _DMCNagItemsDirectory.str
+ _DMCSendNagDeadlineNotification
+ _MDMBootstrapTokenErrorDomain
+ _MDMDatabaseReturnToServiceStorageDirectory
+ _MDMDatabaseReturnToServiceStorageDirectory.cold.1
+ _MDMDatabaseReturnToServiceStorageDirectory.once
+ _MDMDatabaseReturnToServiceStorageDirectory.str
+ _MDMMigrationConfigFilePath
+ _MDMMigrationConfigFilePath.cold.1
+ _MDMMigrationConfigFilePath.once
+ _MDMMigrationConfigFilePath.str
+ _OBJC_CLASS_$_CWFAutoJoinParameters
+ _OBJC_CLASS_$_CWFInterface
+ _OBJC_CLASS_$_DMCAppIdentifier
+ _OBJC_CLASS_$_DMCSnapshotUtilities
+ _OBJC_CLASS_$_DMCWiFiUtilities
+ _OBJC_IVAR_$_DMCAppIdentifier._bundleID
+ _OBJC_IVAR_$_DMCAppIdentifier._personaID
+ _OBJC_IVAR_$_DMCObliterationShelter._additionalDetails
+ _OBJC_IVAR_$_DMCObliterationShelter._isRapidReturnToService
+ _OBJC_IVAR_$_DMCObliterationShelter._isSharediPad
+ _OBJC_IVAR_$_DMCObliterationShelter._userDefaults
+ _OBJC_IVAR_$_DMCWiFiUtilities._config
+ _OBJC_IVAR_$_DMCWiFiUtilities._interface
+ _OBJC_IVAR_$_DMCWiFiUtilities._timeoutBlock
+ _OBJC_IVAR_$_DMCWiFiUtilities._timeoutQueue
+ _OBJC_METACLASS_$_DMCAppIdentifier
+ _OBJC_METACLASS_$_DMCSnapshotUtilities
+ _OBJC_METACLASS_$_DMCWiFiUtilities
+ __OBJC_$_CLASS_METHODS_DMCAppIdentifier
+ __OBJC_$_INSTANCE_METHODS_DMCAppIdentifier
+ __OBJC_$_INSTANCE_METHODS_DMCSnapshotUtilities
+ __OBJC_$_INSTANCE_METHODS_DMCWiFiUtilities
+ __OBJC_$_INSTANCE_VARIABLES_DMCAppIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_DMCWiFiUtilities
+ __OBJC_$_PROP_LIST_DMCAppIdentifier
+ __OBJC_$_PROP_LIST_DMCWiFiUtilities
+ __OBJC_CLASS_RO_$_DMCAppIdentifier
+ __OBJC_CLASS_RO_$_DMCSnapshotUtilities
+ __OBJC_CLASS_RO_$_DMCWiFiUtilities
+ __OBJC_METACLASS_RO_$_DMCAppIdentifier
+ __OBJC_METACLASS_RO_$_DMCSnapshotUtilities
+ __OBJC_METACLASS_RO_$_DMCWiFiUtilities
+ ___50-[DMCSnapshotUtilities deleteSnapshotAtPath:name:]_block_invoke
+ ___51-[DMCSnapshotUtilities captureSnapshotAtPath:name:]_block_invoke
+ ___72-[DMCWiFiUtilities enableAutoJoinIfNeededWithTimeout:completionHandler:]_block_invoke
+ ___72-[DMCWiFiUtilities enableAutoJoinIfNeededWithTimeout:completionHandler:]_block_invoke.5
+ ___72-[DMCWiFiUtilities enableAutoJoinIfNeededWithTimeout:completionHandler:]_block_invoke.7
+ ___DMCNagItemsDirectory_block_invoke
+ ___DMCNagItemsDirectory_block_invoke.cold.1
+ ___MDMDatabaseReturnToServiceStorageDirectory_block_invoke
+ ___MDMMigrationConfigFilePath_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e8_B12?0i8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e18_v16?0"CWFEvent"8lw40l8s32l8
+ ___block_literal_global.104
+ ___block_literal_global.109
+ ___block_literal_global.11
+ ___block_literal_global.114
+ ___block_literal_global.119
+ ___block_literal_global.124
+ ___block_literal_global.129
+ ___block_literal_global.13
+ ___block_literal_global.134
+ ___block_literal_global.139
+ ___block_literal_global.144
+ ___block_literal_global.149
+ ___block_literal_global.159
+ ___block_literal_global.169
+ ___block_literal_global.18
+ ___block_literal_global.187
+ ___block_literal_global.192
+ ___block_literal_global.197
+ ___block_literal_global.202
+ ___block_literal_global.207
+ ___block_literal_global.212
+ ___block_literal_global.217
+ ___block_literal_global.222
+ ___block_literal_global.227
+ ___block_literal_global.229
+ ___block_literal_global.23
+ ___block_literal_global.240
+ ___block_literal_global.246
+ ___block_literal_global.251
+ ___block_literal_global.253
+ ___block_literal_global.28
+ ___block_literal_global.38
+ ___block_literal_global.43
+ ___block_literal_global.48
+ ___block_literal_global.58
+ ___block_literal_global.63
+ ___block_literal_global.68
+ ___block_literal_global.78
+ ___block_literal_global.83
+ ___block_literal_global.85
+ ___block_literal_global.9
+ ___block_literal_global.92
+ ___block_literal_global.97
+ ___block_literal_global.99
+ _close
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _fs_snapshot_create
+ _fs_snapshot_delete
+ _kDMCProfileInstallationSourceMDMMigration
+ _kDMCRapidReturntoServiceSnapshotName
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$IPv4Addresses
+ _objc_msgSend$IPv4AssignedAt
+ _objc_msgSend$IPv4RouterAddress
+ _objc_msgSend$IPv6Addresses
+ _objc_msgSend$IPv6AssignedAt
+ _objc_msgSend$IPv6RouterAddress
+ _objc_msgSend$_createFailToWriteFileErrorWithFilePath:
+ _objc_msgSend$_executeSnapshotActionAtPath:action:
+ _objc_msgSend$_generateShelteredDetailsForLogging
+ _objc_msgSend$_noRecoveryNetworkError
+ _objc_msgSend$_timeoutError
+ _objc_msgSend$activate
+ _objc_msgSend$additionalDetails
+ _objc_msgSend$cancelTimeoutBlock
+ _objc_msgSend$captureSnapshotAtPath:name:
+ _objc_msgSend$cleanup
+ _objc_msgSend$debugDescription
+ _objc_msgSend$deleteSnapshotAtPath:name:
+ _objc_msgSend$generateExclusionPaths
+ _objc_msgSend$haveNetwork
+ _objc_msgSend$info
+ _objc_msgSend$invalidate
+ _objc_msgSend$isRapidReturnToService
+ _objc_msgSend$joinAttempts
+ _objc_msgSend$knownNetworkProfilesWithProperties:
+ _objc_msgSend$logRegularEventForTopic:reason:details:
+ _objc_msgSend$networkName
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$performAutoJoinWithParameters:reply:
+ _objc_msgSend$personaID
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$powerOn
+ _objc_msgSend$result
+ _objc_msgSend$setAdditionalDetails:
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setEventHandler:
+ _objc_msgSend$setIsRapidReturnToService:
+ _objc_msgSend$setIsSharediPad:
+ _objc_msgSend$setMode:
+ _objc_msgSend$setPersonaID:
+ _objc_msgSend$setPower:error:
+ _objc_msgSend$setTrigger:
+ _objc_msgSend$setUserDefaults:
+ _objc_msgSend$startMonitoringEventType:error:
+ _objc_msgSend$stopMonitoringEventType:
+ _objc_msgSend$userDefaults
+ _open
- _MDMUserReturnToServiceStorageDirectory
- _MDMUserReturnToServiceStorageDirectory.cold.1
- _MDMUserReturnToServiceStorageDirectory.once
- _MDMUserReturnToServiceStorageDirectory.str
- ___MDMUserReturnToServiceStorageDirectory_block_invoke
- ___block_literal_global.10
- ___block_literal_global.111
- ___block_literal_global.116
- ___block_literal_global.121
- ___block_literal_global.131
- ___block_literal_global.136
- ___block_literal_global.141
- ___block_literal_global.146
- ___block_literal_global.15
- ___block_literal_global.161
- ___block_literal_global.184
- ___block_literal_global.189
- ___block_literal_global.194
- ___block_literal_global.199
- ___block_literal_global.20
- ___block_literal_global.204
- ___block_literal_global.209
- ___block_literal_global.214
- ___block_literal_global.216
- ___block_literal_global.224
- ___block_literal_global.230
- ___block_literal_global.235
- ___block_literal_global.237
- ___block_literal_global.25
- ___block_literal_global.30
- ___block_literal_global.35
- ___block_literal_global.40
- ___block_literal_global.45
- ___block_literal_global.55
- ___block_literal_global.60
- ___block_literal_global.65
- ___block_literal_global.70
- ___block_literal_global.75
- ___block_literal_global.77
- ___block_literal_global.8
- ___block_literal_global.82
- ___block_literal_global.84
- ___block_literal_global.89
- ___block_literal_global.91
- ___getLARatchetMaxEnablementGracePeriodSymbolLoc_block_invoke
- _dlerror
- _dlsym
- _getLARatchetMaxEnablementGracePeriod
- _getLARatchetMaxEnablementGracePeriod.cold.1
- _getLARatchetMaxEnablementGracePeriodSymbolLoc.ptr
CStrings:
+ " %@"
+ "/MDM_ReturnToService"
+ "/private/var/db/com.apple.devicemanagementclient"
+ "@\"CWFAutoJoinParameters\""
+ "@\"CWFInterface\""
+ "AdditionalDetails"
+ "B12@?0i8"
+ "B28@0:8B16^@20"
+ "B32@0:8@16@?24"
+ "DMCAppIdentifier"
+ "DMCAppIdentifier (%{public}@): Failed to create json from data with error: %{public}@"
+ "DMCAppIdentifier (%{public}@): Failed to find bundleID"
+ "DMCAppIdentifier: Failed to create data from json object with error: %{public}@"
+ "DMCAwaitSystemDeletableAppsTimeout"
+ "DMCBootstrapTokenOverride"
+ "DMCDEPPushTokenSyncInterval"
+ "DMCMigrationErrorDomain"
+ "DMCObliterationShelter: Cleaning up existing Return to Service files."
+ "DMCObliterationShelter: Device was in Shared iPad mode. Nothing to migrate."
+ "DMCObliterationShelter: Failed to delete existing file in the retrieve directory. Error: %{public}@"
+ "DMCObliterationShelter: Failed to store cloud config profile"
+ "DMCObliterationShelter: config file exists in the stash directory instead. This might be before data migration"
+ "DMCObliterationShelter: sheltered files migrated."
+ "DMCPreserveUserDefaultsForRTS"
+ "DMCSnapshotUtilities"
+ "DMCSuppressRRTSOnIdleTimeout"
+ "DMCWiFiUtilities"
+ "Dictionary could not be written to %{public}@, could not write data: %{public}@. Write Options: %lu"
+ "Error monitoring CWFEvent: %{public}@"
+ "Error performing auto join with parameters: %{public}@"
+ "Error turning WiFi power on: %{public}@"
+ "ExclusionPaths"
+ "Failed to copy frame information from 0x%lx, result: %d"
+ "Failed to store file to path %@"
+ "IPv4Addresses"
+ "IPv4AssignedAt"
+ "IPv4RouterAddress"
+ "IPv6Addresses"
+ "IPv6AssignedAt"
+ "IPv6RouterAddress"
+ "IsRapidReturnToService"
+ "IsSharediPad"
+ "MDMBootstrapTokenErrorDomain"
+ "MDMMigrationConfig.plist"
+ "MDMProfileData"
+ "NagItem"
+ "NagItems"
+ "No recovery network has found"
+ "RRTS"
+ "RRTSEnabled"
+ "RRTSMDMTimeout"
+ "RRTSMDMTimeoutEnabled"
+ "RRTSUEATimeout"
+ "RRTSUEATimeoutEnabled"
+ "RTS File Migrated"
+ "RapidReturnToServiceSnapshot"
+ "Return to Service"
+ "Sending nag deadline notification for item: %{public}@"
+ "SimulateRapidReturnToService"
+ "SimulatedWiFiProfile"
+ "T@\"CWFAutoJoinParameters\",&,N,V_config"
+ "T@\"CWFInterface\",&,N,V_interface"
+ "T@\"NSDictionary\",&,N,V_additionalDetails"
+ "T@\"NSDictionary\",&,N,V_userDefaults"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_timeoutQueue"
+ "T@\"NSString\",&,N,V_bundleID"
+ "T@\"NSString\",&,N,V_personaID"
+ "T@\"NSString\",R,N"
+ "T@?,C,N,V_timeoutBlock"
+ "TB,N,V_isRapidReturnToService"
+ "TB,N,V_isSharediPad"
+ "TB,R,N,GisRRTSEnabled"
+ "TB,R,N,GisRRTSMDMTimeoutEnabled"
+ "TB,R,N,GisRRTSUEATimeoutEnabled"
+ "There is no network in class C and class D, stop WiFi auto join process"
+ "UserDefaults"
+ "WiFi Auto Join timed out"
+ "WiFi Connection Queue"
+ "WiFi auto join succeeded"
+ "WiFiProfileData"
+ "^([0-9a-zA-Z\\-\\.]+)(\\s(.*))?"
+ "_additionalDetails"
+ "_allOverrides"
+ "_config"
+ "_createFailToWriteFileErrorWithFilePath:"
+ "_executeSnapshotActionAtPath:action:"
+ "_generateShelteredDetailsForLogging"
+ "_interface"
+ "_isRapidReturnToService"
+ "_isSharediPad"
+ "_noRecoveryNetworkError"
+ "_personaID"
+ "_timeoutBlock"
+ "_timeoutError"
+ "_timeoutQueue"
+ "_userDefaults"
+ "activate"
+ "additionalDetails"
+ "autojoin state : %@"
+ "awaitSystemDeletableAppsTimeoutWithDefaultValue:"
+ "bootstrapTokenOverride"
+ "cancelTimeoutBlock"
+ "captureSnapshotAtPath:name:"
+ "captureSystemVolumeSnapshotWithName:"
+ "cleanup"
+ "com.apple.devicemanagementclient.nagDeadline"
+ "config"
+ "deleteSnapshotAtPath:name:"
+ "deleteSystemVolumeSnapshotWithName:"
+ "depPushTokenPeriodicSyncIntervalWithDefaultValue:"
+ "enableAutoJoinIfNeededWithTimeout:completionHandler:"
+ "fs_snapshot_create() failed with error: %{public}@ (%d)"
+ "fs_snapshot_create() succeeded."
+ "fs_snapshot_delete() failed with error: %{public}@ (%d)"
+ "fs_snapshot_delete() succeeded."
+ "haveNetwork"
+ "info"
+ "initWithBundleID:personaID:"
+ "invalidate"
+ "isRRTSEnabled"
+ "isRRTSMDMTimeoutEnabled"
+ "isRRTSUEATimeoutEnabled"
+ "isRapidReturnToService"
+ "joinAttempts"
+ "knownNetworkProfilesWithProperties:"
+ "networkName"
+ "newAppIdentifierWithIdentifier:"
+ "numberOfRanges"
+ "open() failed with error: %{public}@ (%d)"
+ "performAutoJoinWithParameters:reply:"
+ "personaID"
+ "postNotificationName:object:userInfo:"
+ "powerOn"
+ "result"
+ "setAdditionalDetails:"
+ "setBundleID:"
+ "setConfig:"
+ "setEventHandler:"
+ "setInterface:"
+ "setIsRapidReturnToService:"
+ "setIsSharediPad:"
+ "setMode:"
+ "setPersonaID:"
+ "setPower:error:"
+ "setTimeoutBlock:"
+ "setTrigger:"
+ "setUserDefaults:"
+ "shouldPreserveUserDefaultsForReturnToService"
+ "shouldSimulateRapidReturnToService"
+ "shouldSuppressRRTSOnIdleTimeout"
+ "simulatedWiFiProfile"
+ "startMonitoringEventType:error:"
+ "stopMonitoringEventType:"
+ "timeoutBlock"
+ "timeoutQueue"
+ "userDefaults"
+ "v16@?0@\"CWFEvent\"8"
+ "v32@0:8d16@?24"
- "DMCObliterationShelter: Failed to store cloud config profile with error: %{public}@"
- "DMCRatchet failed to softlink LARatchetMaxEnablementGracePeriod"
- "Dictionary could not be written to %{public}@, could not write data: %{public}@"
- "Failed to copy frame information from 0x%lx"
- "LARatchetMaxEnablementGracePeriod"
- "Library/MDM_ReturnToService"

```
