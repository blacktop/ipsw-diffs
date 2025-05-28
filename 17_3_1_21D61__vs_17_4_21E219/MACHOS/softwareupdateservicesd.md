## softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

-746.80.1.0.0
-  __TEXT.__text: 0x5415c
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0xc6e0
-  __TEXT.__objc_methlist: 0x3ed8
-  __TEXT.__objc_methname: 0xd3e1
-  __TEXT.__cstring: 0xcd0c
-  __TEXT.__objc_classname: 0x57b
-  __TEXT.__objc_methtype: 0x204f
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x534
+781.100.15.0.0
+  __TEXT.__text: 0x5b3bc
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0xc700
+  __TEXT.__objc_methlist: 0x3e80
+  __TEXT.__objc_methname: 0xd27f
+  __TEXT.__cstring: 0xd041
+  __TEXT.__objc_classname: 0x53a
+  __TEXT.__objc_methtype: 0x203c
+  __TEXT.__const: 0xd8
+  __TEXT.__gcc_except_tab: 0x4ac
   __TEXT.__oslogstring: 0x86d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x17d8
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x1da0
-  __DATA_CONST.__cfstring: 0x7920
-  __DATA_CONST.__objc_classlist: 0x168
+  __TEXT.__unwind_info: 0x1754
+  __DATA_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__got: 0x558
+  __DATA_CONST.__const: 0x18d8
+  __DATA_CONST.__cfstring: 0x7a20
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x4d0
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x99f0
-  __DATA.__objc_selrefs: 0x3738
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x4d8
-  __DATA.__objc_superrefs: 0x118
-  __DATA.__objc_ivar: 0x34c
-  __DATA.__objc_data: 0xe10
-  __DATA.__data: 0x878
+  __DATA.__objc_const: 0x96d8
+  __DATA.__objc_selrefs: 0x3700
+  __DATA.__objc_ivar: 0x330
+  __DATA.__objc_data: 0xd20
+  __DATA.__data: 0x758
   __DATA.__bss: 0xd8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2036
-  Symbols:   437
-  CStrings:  3747
+  Functions: 2023
+  Symbols:   455
+  CStrings:  3728
 
Symbols:
+ _OBJC_CLASS_$_SBSSoftwareUpdateService
+ _OBJC_CLASS_$_SUAlertPresentationManager
+ _OBJC_CLASS_$_SUAutoInstallFailureAlertItem
+ _OBJC_CLASS_$_SUSpace
+ _OBJC_CLASS_$_SUSpacePurgeOptions
+ _SUHasEnoughBatteryForAutoDownloadForDescriptor
+ _SUStringFromNetworkType
+ ___NSDictionary0__struct
+ __dispatch_source_type_signal
+ _dispatch_resume
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _exit
+ _kSUAssetAllowAutoDownloadOnBatteryKey
+ _kSUAssetAutoDownloadOnBatteryDelayKey
+ _kSUAssetAutoDownloadOnBatteryMinBatteryKey
+ _kSUAssetGranularlyRampedKey
+ _kSUAutomaticInstallationKey
+ _kSUCoreControllerClientNameKey
+ _kSUCoreControllerDownloadOverCellularKey
+ _kSUCoreControllerEventOTAStartedDownloading
+ _kSUCoreControllerNetworkTypeKey
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_retain_x5
+ _signal
+ _specificTimeOnDate
+ _xpc_dictionary_create_empty
- _OBJC_CLASS_$_SUAppPurgingNotification
- _OBJC_CLASS_$_SUAutoInstallFailureNotification
- _OBJC_CLASS_$_SUCoreSpace
- __Block_object_assign
- _dispatch_release
- _kSUAdditionalError
- _kSUAdditionalSpaceRequired
- _objc_loadWeak
- _statfs
- _xpc_retain
CStrings:
+ "\x01\x17"
+ "\x02"
+ "\x02\x11"
+ "\x03"
+ "\a"
+ "\n[>>>\n         paramType: PurgeOptions:\n            %@\n            error: %@\n<<<]"
+ "\x13\x16\""
+ "\x15\x12"
+ "%s is called"
+ "%s is called with options = %@"
+ "%s: Failed to set %@ activity state to XPC_ACTIVITY_STATE_DONE"
+ "%s: Scheduled simulated auto install activity"
+ "%s: Scheduling a new auto download in one hour in case this one fails"
+ "%s: Simulated auto install activity called"
+ "%s: Simulated auto install activity deferred"
+ "%s: outError = %@"
+ "%s: ramping control flags changed (%d, %d) -> (%d, %d)"
+ "%s: set passcode policy to required"
+ "%s: trigger date = %@"
+ ")"
+ "-[SUCoreDescriptor(SUS) isEqualToDescriptor:]"
+ "-[SUInstaller installUpdateWithInstallOptions:withResult:]_block_invoke"
+ "-[SUInstaller isUpdateReadyForInstallation:]"
+ "-[SUInstaller isUpdateReadyForInstallationWithOptions:replyHandler:]"
+ "-[SUManagerServer autoScanAndDownloadNow:ifAvailable:]_block_invoke"
+ "-[SUScheduler _queue_handleAutoInstallGetKeybag:info:]_block_invoke"
+ "-[SUScheduler scheduleAutoInstallGetKeybagTaskForDescriptor:]"
+ "-[SUScheduler scheduleSimulatedAutoInstallTask]"
+ "-[SUScheduler scheduleSimulatedAutoInstallTask]_block_invoke"
+ "@28@0:8B16@20"
+ "A"
+ "Auto-download power policy not satisfied. Skipping auto download attempt"
+ "AutoInstallOperation wants to begin"
+ "B36@0:8B16B20B24^@28"
+ "Current download is successfully canceled."
+ "Device passcode changed"
+ "DownloadDone: %@ ProgressPhase: %@"
+ "Got SIGTERM, exiting"
+ "Ignoring update located by scan due to existing prepared update (disablePurgeOnNewerUpdateFound is set)"
+ "Is ready for installation?  YES"
+ "No installOptions provided, using the default value"
+ "Ready to install!"
+ "SUFakeInstallFailure is set; faking an installation failure of SUErrorCodeInstallNotAllowable..."
+ "Scan found an update and no previously prepared update is present"
+ "Scheduling an auto download for %@; requirePower=%d, minimumPowerRequirement=%d"
+ "Starting SU Installation with install options: %@; policy: %@"
+ "Succeeded to remove fully un-ramped date for %@"
+ "Succeeded to set fully un-ramped date %@ for %@"
+ "T@\"<SUAutoInstallManagerDelegate>\",W,N,V_delegate"
+ "T@\"NSString\",?,R,C"
+ "T@\"SUManagerEngineParam\",&,N,V_pendingPurgeParams"
+ "TB,R,N,V_skipDocAssetsPurge"
+ "The ramping portion is set to %@ by default"
+ "Unable to remove fully un-ramped date for %@ because we don't have it"
+ "Unable to remove fully un-ramped date for nil descriptor build version"
+ "Unable to set fully un-ramped date because it's already been set for %@"
+ "Unable to set fully un-ramped date for descriptor with nil date"
+ "Unable to set fully un-ramped date for nil descriptor build version"
+ "[Auto scan] %@ has granularlyRamped set, auto download now"
+ "[Auto scan] %@ has rampEnabled set, do not auto download"
+ "[Auto scan] Automatic scan failed with error: %@"
+ "[Auto scan] Automatic scan failed with error: No suitable update to auto download"
+ "[Auto scan] Automatic scan fouond an update: %@"
+ "[Auto scan] Less than %f days have passed since last auto-download, do not auto download"
+ "[Auto scan] downloadNow is set, auto download now"
+ "[SUAutoInstallManager] A previous auto installation failed due to error %@, retrying..."
+ "[SUAutoInstallManager] A previous manual installation failed due to error %@, nothing to do here"
+ "[scanCompleted] %@ is fully unramped!"
+ "[scanCompleted] %@ is fully unramped."
+ "[scanCompleted] %@ is not fully unramped."
+ "_autoInstallActivityCriteriaWithInstallDate:descriptor:"
+ "_currentInstallOptions"
+ "_descriptionPurge"
+ "_fullyUnrampedDateManager"
+ "_next7OClockFrom:"
+ "_pendingPurgeParams"
+ "_queue_handleAutoInstallGetKeybag:info:"
+ "_skipDocAssetsPurge"
+ "allowAutoDownloadOnBattery"
+ "autoDownloadOnBatteryDelay"
+ "autoDownloadOnBatteryMinBattery"
+ "autoScanAndDownloadNow:ifAvailable:"
+ "cancelAutoInstallGetKeybagTask"
+ "cancelDownload:userRequested:keepDocAssets:error:"
+ "cellular"
+ "com.apple.softwareupdate.autoinstall.simulated.startInstall"
+ "com.apple.softwareupdateservicesd.activity.autoInstallGetKeybag"
+ "deleteAUKeepAliveFile"
+ "dismissAlertsOfClass:animated:"
+ "fakeInstallFailure"
+ "fullyUnrampedDateForBuildVersion:"
+ "granularlyRamped"
+ "initWithError:buildNumber:"
+ "initWithPurgeOptions:withError:"
+ "isEqualToDescriptor:"
+ "isInstallerReadyForInstallationWithOptions? NO due to %@"
+ "isInstallerReadyForInstallationWithOptions? YES"
+ "keybagInterfacePasscodeDidChange:"
+ "killDownload:userRequested:keepDocAssets:error:"
+ "lastPreferred: %@ lastAlternate: %@ results: %@"
+ "otaSimulatedAutoTriggered"
+ "overrideGranularRamping"
+ "overrideRamping"
+ "overrideScanSessionIDRampingPortion"
+ "pendingPurgeParams"
+ "presentAlert:animated:"
+ "purge doc assets"
+ "removeDiscoveryDateForBuildVersion:"
+ "removeFullyUnrampedDateForBuildVersion:"
+ "removeUpdateKeepingDocAssets:"
+ "reportOTAStartedDownloadingEvent"
+ "reportSimulatedOTAAutoTriggeredEvent"
+ "safeObjectForKey:ofClass:"
+ "scanResultsChangedSinceLastScan: Alternate update has changed"
+ "scanResultsChangedSinceLastScan: Alternate update is newly discovered"
+ "scanResultsChangedSinceLastScan: Alternate update is newly null"
+ "scanResultsChangedSinceLastScan: Alternate update was previously the preferred update"
+ "scanResultsChangedSinceLastScan: Preferred update has changed"
+ "scanResultsChangedSinceLastScan: Preferred update is newly discovered"
+ "scanResultsChangedSinceLastScan: Preferred update is newly null"
+ "scanResultsChangedSinceLastScan: Preferred update was previously the alternate update"
+ "scanResultsChangedSinceLastScan: pc=%d, ac=%d, pwa=%d, awp=%d, pnd=%d, and=%d"
+ "scheduleAutoInstallGetKeybagTaskForDescriptor:"
+ "scheduleSimulatedAutoInstallTask"
+ "setAllowAutoDownloadOnBattery:"
+ "setAutoDownloadOnBatteryDelay:"
+ "setAutoDownloadOnBatteryMinBattery:"
+ "setDocumentationAssetType:"
+ "setFullyUnrampedDate:forBuildVersion:"
+ "setGranularlyRamped:"
+ "setPendingPurgeParams:"
+ "setUpdateFullyUnrampedDates:"
+ "skip doc assets"
+ "skipDocAssetsPurge"
+ "updateError:withAdditionalUserInfo:"
+ "updateFullyUnrampedDates"
+ "v24@0:8@\"SUKeybagInterface\"16"
+ "v28@0:8B16@?<v@?@\"SUScanResults\"@\"NSError\">20"
+ "writeAUKeepAliveFile"
- "\x12\x16\""
- "%s: Attempting app offload"
- "%s: Attempting cache delete"
- "%s: Cache Delete was not enabled"
- "%s: Current free space without purging: %llu"
- "%s: Needed bytes: %llu"
- "%s: Only attempting app offload"
- "%s: Post CacheDelete neededBytes: %llu; amountPurgeable: %llu"
- "%s: Scheduling a new auto download in case this one fails"
- "%s: [DEFAULTS] space purge failed"
- "%s: [DEFAULTS] space purge succeeded"
- "%s: [DEFAULTS] spacePurgeTime set, sleeping %d secs"
- "%s: haveEnoughSpace: %@"
- "+[SUSpace hasSufficientSpaceWithOptions:withCompletion:]"
- "+[SUSpace hasSufficientSpaceWithOptions:withCompletion:]_block_invoke_5"
- "+[SUSpace makeRoomForUpdate:completion:]"
- "+[SUSpace makeRoomForUpdate:completion:]_block_invoke_7"
- "-[SUManagerServer autoScanAndDownloadIfAvailable:]_block_invoke"
- "/"
- "1"
- "@\"SUAutoInstallFailureNotification\""
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16^@24"
- "Alternate update is has changed"
- "Alternate update is newly discovered"
- "Alternate update is newly null"
- "Alternate update was previously preferred update"
- "App offload declined by user"
- "AppStoreDaemon was unable to offload requested space: %@"
- "B32@0:8B16B20^@24"
- "CacheDelete Purge and "
- "CacheDelete purged %llu bytes. Originally requested %llu bytes"
- "Device has insufficient free space after CacheDelete purged %llu bytes"
- "Device has sufficient free space"
- "Device has sufficient free space after AppStoreDaemon offloaded %llu bytes worth of apps"
- "Device has sufficient free space after CacheDelete purged %llu bytes"
- "Device has sufficient free space. No cleanup needed"
- "Device needs to offload apps to make suffience space for download"
- "Download cancel requested."
- "DownloadDone : %@ ProgressPhase: %@"
- "Ignoring update located by scan due to existing prepared update"
- "Insufficient free space: %@"
- "Insufficient space with %@app offload purge: %@"
- "Insufficient space with CacheDelete purge: %@"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Preferred update is newly null"
- "PreferredLastScanCoreDescriptor: %@ alternateLastScannedCoreDescriptor:%@ results: %@"
- "Primary update has changed"
- "Primary update is newly discovered"
- "Primary update was previously the alternate update"
- "Requesting AppStoreDaemon offload %llu bytes worth of apps"
- "Requesting CacheDelete purge %llu bytes"
- "SUSpace"
- "SUSpaceCheckResults"
- "SUSpacePurgeOptions"
- "Scan found an update and no previously prepared update present"
- "Spoofing %s with %@, the space purge will directly end and no further actions"
- "Spoofing %s with result: %@"
- "Starting SU Installation with install options: %@"
- "T@\"<SUAutoInstallManagerDelegate>\",N,V_delegate"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_completionQueue"
- "T@\"SUAutoInstallFailureNotification\",&,N,V_autoSUFailureNotification"
- "TB,N,V_enableAppOffload"
- "TB,N,V_enableCacheDelete"
- "TB,N,V_hasSufficientFreeSpace"
- "TB,N,V_needsAppOffload"
- "TB,N,V_needsCacheDelete"
- "TB,R"
- "TQ,N,V_additionalBytesRequired"
- "TQ,N,V_neededBytes"
- "Ti,N,V_cacheDeleteUrgency"
- "Tq,N,V_appOffloadUrgency"
- "Unable to make sufficient room for download"
- "[Auto scan] Automatic scan for failed with error: %@"
- "[Auto scan] Less than %f days have passed since discovering %@, do not auto download"
- "[Auto scan] No suitable update to auto download"
- "[Auto scan] downloadNow is set, auto downloading now"
- "_additionalBytesRequired"
- "_appOffloadUrgency"
- "_autoSUFailureNotification"
- "_cacheDeleteUrgency"
- "_completionQueue"
- "_enableAppOffload"
- "_enableCacheDelete"
- "_hasSufficientFreeSpace"
- "_neededBytes"
- "_needsAppOffload"
- "_needsCacheDelete"
- "appOffloadUrgency"
- "autoSUFailureNotification"
- "cacheDeletePurge:cacheDeleteUrgency:withCompletionQueue:completion:"
- "cancelDownload:userRequested:error:"
- "checkPurgeableSpaceCacheDelete:cacheDeleteUrgency:withCompletionQueue:completion:"
- "checkPurgeableSpaceOffloadApps:cacheDeleteUrgency:withCompletionQueue:completion:"
- "completionQueue"
- "components:fromDate:"
- "copyWithZone:"
- "currentFreeSpaceForVolume:"
- "dateFromComponents:"
- "decodeBoolForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "dismissNotification"
- "enableAppOffload"
- "enableCachDelete"
- "enableCacheDelete"
- "encodeBool:forKey:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeWithCoder:"
- "fileSystemRepresentation"
- "hasSufficientSpaceWithOptions:error:"
- "haveEnoughSpace"
- "initWithCoder:"
- "isPowerRequired"
- "killDownload:userRequested:error:"
- "makeRoomForUpdate:error:"
- "minimumPowerRequirement"
- "neededBytes"
- "needsAppOffload"
- "needsCacheDelete"
- "offloadAppsPurge:cacheDeleteUrgency:withCompletionQueue:completion:"
- "postAppPurgingNotificationWithCompletion:"
- "postNotificationForError:withUpdateBuildNumber:"
- "removeUpdate"
- "scanWeeklyInternally"
- "selectCompletionQueue:"
- "setAdditionalBytesRequired:"
- "setAutoSUFailureNotification:"
- "setHasSufficientFreeSpace:"
- "setHour:"
- "setMinute:"
- "setNeedsAppOffload:"
- "setNeedsCacheDelete:"
- "setSecond:"
- "spacePurgeSuccessful"
- "spacePurgeTime"
- "supportsSecureCoding"
- "unmetConstraints"
- "v12@?0B8"
- "v24@0:8@\"NSCoder\"16"
- "v28@?0B8Q12@\"NSError\"20"
- "v36@?0B8@\"NSError\"12@\"NSObject<OS_dispatch_queue>\"20@?<v@?B@\"NSError\">28"
- "v40@?0@\"SUSpaceCheckResults\"8@\"NSError\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?@\"SUSpaceCheckResults\"@\"NSError\">32"
- "v40@?0Q8i16B20@\"NSObject<OS_dispatch_queue>\"24@?<v@?B@\"NSError\">32"
- "v40@?0Q8q16@\"NSObject<OS_dispatch_queue>\"24@?<v@?B@\"NSError\">32"
- "v60@?0B8Q12q20@\"SUSpaceCheckResults\"28@\"NSError\"36@\"NSObject<OS_dispatch_queue>\"44@?<v@?@\"SUSpaceCheckResults\"@\"NSError\">52"
- "{hasSufficientFreeSpace:%d,needsCacheDelete:%d,needsAppOffload:%d,additionalBytesRequired:%llu}"

```
