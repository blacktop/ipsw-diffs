## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-976.100.0.0.0
-  __TEXT.__text: 0x165b9c
-  __TEXT.__auth_stubs: 0x1230
-  __TEXT.__objc_methlist: 0xe0a4
-  __TEXT.__const: 0x788
-  __TEXT.__dlopen_cstrs: 0x955
-  __TEXT.__cstring: 0x1a375
-  __TEXT.__gcc_except_tab: 0x60cc
-  __TEXT.__oslogstring: 0x15cf8
+976.108.0.0.0
+  __TEXT.__text: 0x166858
+  __TEXT.__auth_stubs: 0x1280
+  __TEXT.__objc_methlist: 0xe3f4
+  __TEXT.__const: 0x798
+  __TEXT.__dlopen_cstrs: 0x891
+  __TEXT.__cstring: 0x1a701
+  __TEXT.__gcc_except_tab: 0x5f7c
+  __TEXT.__oslogstring: 0x15aa3
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x4488
-  __TEXT.__objc_classname: 0xba1
-  __TEXT.__objc_methname: 0x1f400
-  __TEXT.__objc_methtype: 0x3056
-  __TEXT.__objc_stubs: 0x17640
-  __DATA_CONST.__got: 0x6e0
-  __DATA_CONST.__const: 0x43b0
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __TEXT.__unwind_info: 0x44c0
+  __TEXT.__objc_classname: 0xc2a
+  __TEXT.__objc_methname: 0x1ff71
+  __TEXT.__objc_methtype: 0x30e9
+  __TEXT.__objc_stubs: 0x17ca0
+  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__const: 0x4410
+  __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e30
+  __DATA_CONST.__objc_selrefs: 0x7078
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x2a8
-  __DATA_CONST.__objc_arraydata: 0x18d0
-  __AUTH_CONST.__auth_got: 0x928
-  __AUTH_CONST.__const: 0x2420
-  __AUTH_CONST.__cfstring: 0x16280
-  __AUTH_CONST.__objc_const: 0x11f00
-  __AUTH_CONST.__objc_intobj: 0x3630
+  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x18b0
+  __AUTH_CONST.__auth_got: 0x950
+  __AUTH_CONST.__const: 0x2440
+  __AUTH_CONST.__cfstring: 0x168c0
+  __AUTH_CONST.__objc_const: 0x12878
+  __AUTH_CONST.__objc_intobj: 0x3660
   __AUTH_CONST.__objc_arrayobj: 0x3c0
-  __AUTH_CONST.__objc_dictobj: 0x208
-  __AUTH.__objc_data: 0x910
+  __AUTH_CONST.__objc_dictobj: 0x1e0
+  __AUTH.__objc_data: 0xa50
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xf40
-  __DATA.__data: 0xb18
-  __DATA.__bss: 0x178
+  __DATA.__objc_ivar: 0xfe0
+  __DATA.__data: 0xb78
+  __DATA.__bss: 0x150
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0x54
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 429A9A79-8E5E-3C60-86C8-3D604694824D
-  Functions: 5925
-  Symbols:   931
-  CStrings:  12976
+  UUID: 0FDC01E8-7196-3B2F-BD84-4A74AB3725AC
+  Functions: 5979
+  Symbols:   946
+  CStrings:  13224
 
Symbols:
+ _CWFEventDriverAvailabilityMessageKey
+ _NSFileCreationDate
+ _NSSearchPathForDirectoriesInDomains
+ _OBJC_CLASS_$_CWFAssetCreatorFromRoot
+ _OBJC_CLASS_$_CWFAssetRootMonitor
+ _OBJC_CLASS_$_CWFDriverAvailabilityMessage
+ _OBJC_CLASS_$_CWFMLOLink
+ _OBJC_CLASS_$_CWFPowerTableElectionTelemetry
+ _OBJC_METACLASS_$_CWFAssetCreatorFromRoot
+ _OBJC_METACLASS_$_CWFAssetRootMonitor
+ _OBJC_METACLASS_$_CWFDriverAvailabilityMessage
+ _OBJC_METACLASS_$_CWFMLOLink
+ _OBJC_METACLASS_$_CWFPowerTableElectionTelemetry
+ __os_signpost_emit_with_name_impl
+ _objc_storeWeak
+ _os_signpost_enabled
+ _os_signpost_id_make_with_pointer
- _OBJC_CLASS_$_CWFAssetManager
- _OBJC_METACLASS_$_CWFAssetManager
CStrings:
+ "%@.01.0001,0"
+ "%{public}s::%d:%s:  addedPaths ---\n %@\n deletedPaths ---\n %@\n updatedPaths ---\n %@"
+ "%{public}s::%d:%s: Attempting to send telemetry"
+ "%{public}s::%d:%s: Clearing pathsExisting"
+ "%{public}s::%d:%s: Clearing pathsFileAttributes"
+ "%{public}s::%d:%s: Clearing pathsUpdated"
+ "%{public}s::%d:%s: Done"
+ "%{public}s::%d:%s: Error accessing attributesOfItemAtPath %@ : %@"
+ "%{public}s::%d:%s: Failed to init"
+ "%{public}s::%d:%s: Found Info.plist with data: %@"
+ "%{public}s::%d:%s: Monitoring Directory %@ at interval %ld seconds"
+ "%{public}s::%d:%s: NO ELECTOR"
+ "%{public}s::%d:%s: Root Removed, freeing rootAsset"
+ "%{public}s::%d:%s: Sent telemetry metricDict: %@"
+ "%{public}s::%d:%s: Setting assetRootToProcess FALSE"
+ "%{public}s::%d:%s: Setting assetRootToProcess TRUE"
+ "%{public}s::%d:%s: checkForChanges NSUserDefaults found with key %@ value %@"
+ "%{public}s::%d:%s: checkForChanges NSUserDefaults found with key %@ value %ld"
+ "%{public}s::%d:%s: key %@\n\tdictOne %@\n\tdictTwo %@"
+ "%{public}s::%d:CWFPowerTableElectionTelemetry super init failed"
+ "%{public}s::%d:Files Added %@"
+ "%{public}s::%d:Files Deleted \n%@"
+ "%{public}s::%d:Files Modified: \n%@"
+ "%{public}s::%d:Monitoring Directory %@ at interval %ld seconds"
+ "%{public}s::%d:handleUpdatedPaths ERROR processing pathsUpdated path %@ attr %@ prevAttr %@"
+ "%{public}s::%d:stopMonitoringStream"
+ "-[CWFAssetCreatorFromRoot initWithPaths:]"
+ "-[CWFAssetCreatorFromRoot loadTopLevelInfoPlistFromPaths:]"
+ "-[CWFAssetLocal initWithAssetType:assetSpecifier:assetVersion:attributes:rootCatalogInfo:localURL:]"
+ "-[CWFAssetPowerTable init]"
+ "-[CWFAssetRootMonitor checkForChanges]"
+ "-[CWFAssetRootMonitor handleUpdatedPaths]"
+ "-[CWFAssetRootMonitor initMonitorWithPath:]"
+ "-[CWFAssetRootMonitor printDictionaryDifferences:dictTwo:]"
+ "-[CWFAssetRootMonitor startMonitoringPath:]"
+ "-[CWFAssetRootMonitor stopMonitoringStream]"
+ "-[CWFAssetSetManager lockAndHandOffCanBlock:forcedFetch:]"
+ "-[CWFAssetSetManager lockAutoAssetWithReason:isBlocking:forcedFetch:]"
+ "-[CWFAssetSetManager rootMonitorDetectedAdd:deleted:updated:]"
+ "-[CWFAssetSetManager rootMonitorDetectedAdd:deleted:updated:]_block_invoke"
+ "-[CWFPowerTableElectionTelemetry init]"
+ "-[CWFPowerTableElectionTelemetry sendTelemetryAndClear]"
+ "-[CWFPowerTableElectionTelemetry sendTelemetryAndClear]_block_invoke"
+ "10MHz"
+ "160MHz"
+ "2.4GHz"
+ "20MHz"
+ "40MHz"
+ "80+80MHz"
+ "80MHz"
+ "@\"<CWFAssetRootMonitorDelegate>\""
+ "@\"CWFAssetCreatorFromRoot\""
+ "@\"CWFAssetRootMonitor\""
+ "@64@0:8@16@24@32@40@48@56"
+ "@72@0:8@16@24B32Q36Q44B52B56B60^@64"
+ "ACK TIMEOUT"
+ "AssetData"
+ "AssetSpecifier"
+ "AssetVersion"
+ "CFBundleIdentifier"
+ "CFBundleName"
+ "CFBundleVersion"
+ "COALESCED+CACHED EVENT FOR SUSPENDED PROCESS"
+ "CWFAssetCreatorFromRoot"
+ "CWFAssetRootMonitor"
+ "CWFAssetRootMonitorDelegate"
+ "CWFDriverAvailabilityMessage"
+ "CWFEventID eventIDWithType"
+ "CWFMLOLink"
+ "CWFPowerTableElectionTelemetry"
+ "CoreWiFiAssetRootDropoff"
+ "DRIVER AVAILABILITY EVENT"
+ "DRIVER AVAILABLE"
+ "DROPPING EVENT FOR SUSPENDED PROCESS"
+ "DriverAvailabilityMessage"
+ "MobileAssetProperties"
+ "No Reply DROPPING EVENT FOR SUSPENDED PROCESS"
+ "No Reply OALESCED+CACHED EVENT FOR SUSPENDED PROCESS"
+ "No reply"
+ "PHBBHNotificationPresentationTimestamps"
+ "PHBBHNotificationResponseTimestamps"
+ "RECV ACK"
+ "RootAssetID"
+ "RootMonitorCheckInterval_s"
+ "RootMonitorCheckPath"
+ "Root_%@_%@"
+ "SENT EVENT"
+ "T@\"<CWFAssetRootMonitorDelegate>\",W,N,V_delegate"
+ "T@\"CWFAssetCreatorFromRoot\",&,N,V_assetFromRoot"
+ "T@\"CWFAssetRootMonitor\",&,N,V_assetRootMonitor"
+ "T@\"NSData\",C,N,V_rawEventData"
+ "T@\"NSDate\",&,N,V_creationDate"
+ "T@\"NSDateFormatter\",&,N,V_formatter"
+ "T@\"NSDictionary\",&,N,V_infoPlist"
+ "T@\"NSDictionary\",&,N,V_rootCatalogInfo"
+ "T@\"NSString\",&,N,V_AssetSpecifier"
+ "T@\"NSString\",&,N,V_AssetVersion"
+ "T@\"NSString\",C,N,V_reasonString"
+ "T@\"NSURL\",&,N,V_localContentURL"
+ "TB,N,V_assetRootToProcess"
+ "TB,N,V_available"
+ "TB,N,V_availableForUse"
+ "TB,N,V_isPrimaryLink"
+ "TC,N,V_channel"
+ "Ti,N,V_band"
+ "Ti,N,V_subchannel"
+ "Ti,N,V_width"
+ "Tq,N,V_event_id"
+ "Tq,N,V_flags"
+ "Tq,N,V_minor_reason"
+ "Tq,N,V_reason"
+ "Tq,N,V_sub_reason"
+ "Tq,N,V_trapInfoSequenceNum"
+ "UTC"
+ "XPCGetRequestWithType"
+ "[OTA] %s: assetSpecifier:%@ is nil or malformed, or doesn't match required %@"
+ "[OTA] %s: createTopLevelDir %@ not found, calling createDirectoryAtPath"
+ "[OTA_SET] %s: No Server Side auto-asset-entries matching set requirements exist, exiting"
+ "[OTA_SET] %s: invalid localContentURL %@"
+ "[corewifi] [bbh] PH BBH notification is %{public}sallowed (network=%{public}@)"
+ "[corewifi] [bbh] Reset PH BBH notification timestamps (network=%{public}@), "
+ "[corewifi] [bbh] Updated PH BBH notification presentation timestamp (%{public}@) for network (%{public}@)"
+ "[corewifi] [bbh] Updated PH BBH notification response timestamp (%{public}@) for network (%{public}@)"
+ "_AssetSpecifier"
+ "_AssetVersion"
+ "__performScanWithChannelList:SSIDList:passive:dwellTime:maxCacheAge:cacheOnly:isPreAssociationScan:checkForKnownNetworks:error:"
+ "_assetFromRoot"
+ "_assetRootMonitor"
+ "_assetRootToProcess"
+ "_available"
+ "_availableForUse"
+ "_btInitiatedPTUpdate"
+ "_creationDate"
+ "_electionStartNotificationDate"
+ "_event_id"
+ "_finalAssetVersionInfoDate"
+ "_finalAssetVersionInfoVersion"
+ "_finalResultString"
+ "_formatter"
+ "_handoffAvailableDate"
+ "_handoffBTAssetVersionInfo"
+ "_handoffWiFiAssetVersionInfo"
+ "_infoPlist"
+ "_initialAssetFilename"
+ "_initialAssetVersionInfoDate"
+ "_initialAssetVersionInfoVersion"
+ "_isPrimaryLink"
+ "_localContentURL"
+ "_minor_reason"
+ "_rawEventData"
+ "_readinessReply"
+ "_readinessReplyDeliveredDate"
+ "_rootCatalogInfo"
+ "_sub_reason"
+ "_subchannel"
+ "_trapInfoSequenceNum"
+ "_voteDeliveredDate"
+ "_voteResult"
+ "_width"
+ "_wifiInitiatedPTUpdate"
+ "assetFromRoot"
+ "assetRootMonitor"
+ "assetRootToProcess"
+ "assetVersionFilename"
+ "attributesOfItemAtPath:error:"
+ "availabilityFlagFwLoaded"
+ "availabilityFlagHasJoinTimeoutInfo"
+ "availabilityFlagHasTrapCrashTracerMiniDump"
+ "availabilityFlagHasTrapInfo"
+ "availabilityFlagIsNonFatal"
+ "availabilityFlagIsRetry"
+ "available"
+ "availableForUse"
+ "band=%@, channel=%ld, width=%@, subchannel=%d"
+ "checkForChanges"
+ "checkForDeletedPath:"
+ "com.apple.wifi.CWFAssetRootMonitor"
+ "com.apple.wifi.otapowertable.load"
+ "creationDate"
+ "currentAssetVersionInfoVersion"
+ "dataWithData:"
+ "dictionaryWithContentsOfFile:"
+ "en_US_POSIX"
+ "enumeratorAtPath:"
+ "event_id"
+ "finalAssetVersionInfoVersion"
+ "finalResult"
+ "formatter"
+ "handleUpdatedPaths"
+ "handoffAssetVersionBT"
+ "handoffAssetVersionWiFI"
+ "infoPlist"
+ "initMonitorWithPath:"
+ "initWithAssetType:assetSpecifier:assetVersion:attributes:rootCatalogInfo:localURL:"
+ "initWithDriverAvailabiltyData:"
+ "initWithPaths:"
+ "isEqualToDictionary:"
+ "isEqualToDriverAvailabiltyMessage:"
+ "isEqualToMLOLink:"
+ "isPrimaryLink"
+ "loadTopLevelInfoPlistFromPaths:"
+ "localContentURL"
+ "localeWithLocaleIdentifier:"
+ "lockAndHandOffCanBlock:forcedFetch:"
+ "lockAutoAssetWithReason:isBlocking:forcedFetch:"
+ "lockdownd.internal"
+ "lockdownd.watch"
+ "lockdownd.watch.internal"
+ "mLOLinks"
+ "max"
+ "minor_reason"
+ "monitoredParentPath"
+ "monitoredPath"
+ "newerVersionAttributes"
+ "nextObject"
+ "pathPollingInterval"
+ "pathsExisting"
+ "pathsExistingAtLastCheck"
+ "pathsFileAttributes"
+ "pathsFileAttributesAtLastCheck"
+ "pathsUpdated"
+ "printDictionaryDifferences:dictTwo:"
+ "rawEventData"
+ "receivedAcknowledgedXPCEvent"
+ "receivedXPCEvent"
+ "rootCatalogInfo"
+ "rootMonitorDetectedAdd:deleted:updated:"
+ "scheduleTimer"
+ "sendXPCEvent"
+ "setAssetFromRoot:"
+ "setAssetRootMonitor:"
+ "setAssetRootToProcess:"
+ "setAssetVersion:"
+ "setAvailable:"
+ "setAvailableForUse:"
+ "setCandidatePowerTableVersionBluetooth:"
+ "setCandidatePowerTableVersionWiFi:"
+ "setCreationDate:"
+ "setCurrentPowerTableVersionAtReadiness:fileName:"
+ "setEvent_id:"
+ "setFinalPowerTableVersion:"
+ "setFinalResultAndSendTelemetry:"
+ "setFormatter:"
+ "setInfoPlist:"
+ "setIsPrimaryLink:"
+ "setLocalContentURL:"
+ "setMinor_reason:"
+ "setPowerTableReadiness:"
+ "setPowerTableVote:"
+ "setRawEventData:"
+ "setRootCatalogInfo:"
+ "setSub_reason:"
+ "setSubchannel:"
+ "setTrapInfoSequenceNum:"
+ "setValue:forKey:"
+ "setWidth:"
+ "setWithSet:"
+ "startMonitoring"
+ "startMonitoringPath:"
+ "stopMonitoringStream"
+ "stringByAppendingPathComponent:"
+ "stringByDeletingLastPathComponent"
+ "stringForKey:"
+ "sub_reason"
+ "subchannel"
+ "timer"
+ "timerQueue"
+ "timestamp=%@ available %s reasonString %@ reason=0x%lX sub_reason=0x%lX minor_reason=0x%lX event_id=0x%lX"
+ "trapInfoSequenceNum"
+ "v24@0:8B16B20"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32"
+ "wifiChipReloadsAfterSession"
+ "wifiChipReloadsDuringEvaluation"
+ "wifiInitiatedLoad"
+ "wifiReadiness"
+ "wifiVote"
+ "yyyy-MM-dd'T'HH:mm:ss'Z'"
+ "\xa1"
- "+[CWFAssetManager endAllPreviousLocksForSpecifier:]"
- "-[CWFAssetLocal initWithAssetType:assetSpecifier:assetVersion:attributes:localURL:]"
- "-[CWFAssetManager __periodicCheck]"
- "-[CWFAssetManager __startAssetTracking]_block_invoke"
- "-[CWFAssetManager __startAssetTracking]_block_invoke_2"
- "-[CWFAssetManager __stopPeriodicCheckA11]"
- "-[CWFAssetManager _registerForAssetChangedNotification:]"
- "-[CWFAssetManager _registerForAssetChangedNotification:]_block_invoke"
- "-[CWFAssetManager activate]"
- "-[CWFAssetManager enablePeriodicCheck]"
- "-[CWFAssetManager init]"
- "-[CWFAssetManager lockAndHandOffCanBlock:]"
- "-[CWFAssetManager lockAutoAssetWithReason:isBlocking:]"
- "-[CWFAssetManager makeAutoAssetWithSelector:]"
- "-[CWFAssetManager processQueryResults:withError:]"
- "-[CWFAssetManager processQueryResults:withError:]_block_invoke"
- "-[CWFAssetManager unlockAssetWithReason:]"
- "-[CWFAssetSetManager lockAndHandOffCanBlock:]"
- "-[CWFAssetSetManager lockAutoAssetWithReason:isBlocking:]"
- "@56@0:8@16@24@32@40@48"
- "@68@0:8@16@24B32Q36Q44B52B56^@60"
- "ASSET_VERSION_DOWNLOADED"
- "CWFAssetManager"
- "MAAutoAssetNotifications"
- "PHBBHDismissNotificationTimestamps"
- "TB,N,V_interestSet"
- "[OTA] %s:  --- Received asset download notificaiton --- "
- "[OTA] %s:  Begin: notify_register_dispatch's completion handler"
- "[OTA] %s:  Could not create _assetPowerTable"
- "[OTA] %s:  End: notify_register_dispatch's completion handler"
- "[OTA] %s:  Entered"
- "[OTA] %s:  Exiting"
- "[OTA] %s:  Failed to unlock for reason:%@ with error: %@"
- "[OTA] %s:  Interest registration failed for %@ with error: %@"
- "[OTA] %s:  Interest registration succeeded for %@"
- "[OTA] %s:  Not locking asset as interest is not yet set"
- "[OTA] %s:  Skipping the end asset lock operation as it was never locked."
- "[OTA] %s:  Unable to initialize autoAsset with requested assetSelector: %@, error: %@"
- "[OTA] %s:  Unable to lock any version of auto-asset content, lockedAssetSelector: %@ error: %@"
- "[OTA] %s:  Unlocked Assets"
- "[OTA] %s:  localAsset did not populate"
- "[OTA] %s:  notify_register_dispatch() returned token %d"
- "[OTA] %s: About to start tracking Assets"
- "[OTA] %s: Asset is already locked! Unlocking first."
- "[OTA] %s: Cannot create auto asset instance with selector: %@, error: %@"
- "[OTA] %s: Completed for assetSelector: %@ with error: %@"
- "[OTA] %s: Download only platform or firmware. Disabling future a11 checks and proceeding with download-only path. error = %@"
- "[OTA] %s: Empty or nil wifichipset data"
- "[OTA] %s: Entering"
- "[OTA] %s: Error: %@"
- "[OTA] %s: Existing self.apiMajorVersion=%@, queryResults=%@, disabling future checks."
- "[OTA] %s: Fetch status for locked auto asset: %@ completed with error: %@"
- "[OTA] %s: Found new version of asset with assetSelector: %@ and attributes: %@"
- "[OTA] %s: Initialized successfully"
- "[OTA] %s: Locked Asset: %@, Attributes: %@, localContentURL: %@"
- "[OTA] %s: No availableForUseAttributes for status: %@"
- "[OTA] %s: Not processing queryResults=%@, existing apiMajorversion=%@"
- "[OTA] %s: Running on internal build"
- "[OTA] %s: Same Version of asset is already downloaded. Error: %@"
- "[OTA] %s: Setting up dispatch source for periodic check"
- "[OTA] %s: Stopping periodic check for a11 interface"
- "[OTA] %s: Successfully locked the asset. currentLockedAutoAsset = %@"
- "[OTA] %s: Successfully locked the asset. lockedAssetSelector = %@"
- "[OTA] %s: Supported platform or firmware, transient error = %@"
- "[OTA] %s: Unable to init"
- "[OTA] %s: Unsupported platform or disabled FF"
- "[OTA] %s: Unsupported platform or firmware, disabling future a11 checks. error = %@, "
- "[OTA] %s: _periodicCheckA11Timer is nil"
- "[OTA] %s: _periodicCheckEnabled from defaults: %@"
- "[OTA] %s: _periodicityInSecs from defaults: %lld"
- "[OTA] %s: assetSpecifier:%@ is nil or malformed"
- "[OTA] %s: invalid apiMajorVersion=%@, processing queryResults=%@"
- "[OTA] OTA update of PT is disabled"
- "[corewifi] [bbh] PH BBH notification is %{public}sallowed (network=%{public}@, interval=%lu)"
- "[corewifi] [bbh] Reset PH BBH notification timestamp (network=%{public}@), "
- "[corewifi] [bbh] Updated PH BBH notification timestamp (%{public}@) for network (%{public}@)"
- "__performScanWithChannelList:SSIDList:passive:dwellTime:maxCacheAge:cacheOnly:isPreAssociationScan:error:"
- "_interestSet"
- "checkForNewerSync:withUsagePolicy:withTimeout:discoveredAttributes:error:"
- "endAllPreviousLocksForSpecifier:"
- "endAllPreviousLocksOfSelectorSync:forClientName:"
- "initWithAssetType:assetSpecifier:assetVersion:attributes:localURL:"
- "interestInContent:withInterestPolicy:completion:"
- "interestSet"
- "lockAndHandOffCanBlock:"
- "lockAutoAssetWithReason:isBlocking:"
- "notifyRegistrationName:forAssetType:forAssetSpecifier:"
- "setInterestSet:"
- "v24@?0@\"MAAutoAssetSelector\"8@\"NSError\"16"

```
