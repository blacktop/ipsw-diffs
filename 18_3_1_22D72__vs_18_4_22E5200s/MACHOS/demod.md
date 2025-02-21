## demod

> `/usr/libexec/demod`

```diff

-1445.82.1.0.0
-  __TEXT.__text: 0xd76b8
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_stubs: 0x17a80
-  __TEXT.__objc_methlist: 0xaac8
-  __TEXT.__const: 0x21e
-  __TEXT.__gcc_except_tab: 0x4330
-  __TEXT.__cstring: 0xe5fa
-  __TEXT.__objc_methname: 0x1bb24
-  __TEXT.__oslogstring: 0x1758c
-  __TEXT.__objc_classname: 0x156a
-  __TEXT.__objc_methtype: 0x3657
+1445.100.72.0.1
+  __TEXT.__text: 0xde73c
+  __TEXT.__auth_stubs: 0x1b00
+  __TEXT.__objc_stubs: 0x18300
+  __TEXT.__objc_methlist: 0xbc6c
+  __TEXT.__const: 0x226
+  __TEXT.__gcc_except_tab: 0x4608
+  __TEXT.__cstring: 0xe6ca
+  __TEXT.__objc_methname: 0x1c358
+  __TEXT.__oslogstring: 0x17f4c
+  __TEXT.__objc_classname: 0x157a
+  __TEXT.__objc_methtype: 0x369d
   __TEXT.__swift5_typeref: 0x63
   __TEXT.__swift5_capture: 0x38
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2b60
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__unwind_info: 0x31b8
   __TEXT.__eh_frame: 0xf8
-  __DATA_CONST.__auth_got: 0xda8
-  __DATA_CONST.__got: 0xc58
+  __DATA_CONST.__auth_got: 0xd90
+  __DATA_CONST.__got: 0xc78
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2a00
-  __DATA_CONST.__cfstring: 0xcee0
-  __DATA_CONST.__objc_classlist: 0x658
+  __DATA_CONST.__const: 0x2b10
+  __DATA_CONST.__cfstring: 0xd300
+  __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x3a8
+  __DATA_CONST.__objc_superrefs: 0x3b0
   __DATA_CONST.__objc_intobj: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x818
   __DATA_CONST.__objc_arrayobj: 0x3d8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x17f78
-  __DATA.__objc_selrefs: 0x68a8
-  __DATA.__objc_ivar: 0x9d8
-  __DATA.__objc_data: 0x3fd0
+  __DATA.__objc_const: 0x166c0
+  __DATA.__objc_selrefs: 0x6fe0
+  __DATA.__objc_ivar: 0x9f8
+  __DATA.__objc_data: 0x4020
   __DATA.__data: 0x2698
-  __DATA.__bss: 0x500
+  __DATA.__bss: 0x510
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager

   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
+  - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4932
-  Symbols:   867
-  CStrings:  9483
+  Functions: 5165
+  Symbols:   868
+  CStrings:  9647
 
Symbols:
+ _IDSCopyLocalDeviceUniqueID
+ _OBJC_CLASS_$_AFSettingsConnection
+ _OBJC_CLASS_$_BLSAssertion
+ _OBJC_CLASS_$_BLSDisableAlwaysOnAttribute
+ _OBJC_CLASS_$_MAAsset
+ _OBJC_CLASS_$_MAAssetQuery
+ __CFPreferencesFlushCachesForIdentifier
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$sypN
- _swift_arrayDestroy
CStrings:
+ "\tAssetSpecifier: %@\n\tAssetId: %@\n\tSize: %@"
+ "\nAssets already indicated available for updates."
+ "\nDevice is not in demo mode."
+ "\nNo asset types to update."
+ "\x15\x13\x13"
+ "!\x12"
+ "%lu Failed Asset Downloads. %lu Timed-out Asset Downloads."
+ "%s - ChangeSettings has new 'AssetQueryFrequency' set."
+ "%s - Failed to download the asset type %{public}@ catalog"
+ "%s: PlatformType='%{public}@' DeviceClass='%{public}@'"
+ "%{public}@ is missing assets"
+ "-[MSDAssetUpdater runQueryWithAssetType:]"
+ "-[MSDHelperAgent collectDemoLogsToFolder:ofType:]"
+ "/System/Library/UnifiedAssetFramework/AssetSets"
+ "/var/mobile/XcodeBuiltProducts/PressDemoScripts.xctestproducts"
+ "14"
+ "======= Asset type %{public}@ downloaded ========="
+ "======= Asset type %{public}@ failed ========="
+ "======= Asset type %{public}@ timed out ========="
+ "======= Starting to download Asset type: %{public}@ =========="
+ "@\"BLSAssertion\""
+ "@\"MSDAssetUpdater\""
+ "All operations finished"
+ "An error occurred while retrieving contents of %{public}@ - %{public}@"
+ "Asset"
+ "Asset download failed with status %ld"
+ "Asset download failed with status %ld\n%{public}@"
+ "Asset download finished:\n%{public}@"
+ "Asset download timed out"
+ "Asset update."
+ "AssetQueryInterval"
+ "AssetSpecifier"
+ "Assets list returned nil.  Failure occured within checkAssetAvailabilityWithQuery"
+ "AssetsAvailable"
+ "AutoAssetType"
+ "Available assets found in previous assetType query."
+ "B28@0:8B16^@20"
+ "ChangeOSPreferences"
+ "CloudPairedDevices"
+ "Continuing asset query with %lu assets"
+ "Demod Obliterate Device"
+ "Device Preferences Update."
+ "Device already has a Siri language of %{public}@"
+ "DeviceEnclosureColor"
+ "DisableCleanEnergyCharging"
+ "Failed Asset Downloads: %@. Timed-out Asset Downloads: %@"
+ "Failed to query %lu / %lu assets"
+ "Failed to query asset %{public}@"
+ "Failed to read %{public}@ as a dictionary with error - %{public}@"
+ "Failed to set the Siri language to %{public}@, the device Siri language remains set to %{public}@"
+ "Failed to switch to mode %d to update OS Preferences."
+ "Failed to switch to mode %d to update assets."
+ "Found asset type %{public}@"
+ "GreyMatter is not opted in (%d) or feature flag for 'EnableAIModelAutoUpdate' is disabled (%d)."
+ "GreyMatterAssetTypes"
+ "IdentityServicesID"
+ "Including GreyMatter asset types!"
+ "Invalid %{public}@ message received without a valid %{public}@ dictionary"
+ "LogS3BucketUrl"
+ "MSDAssetUpdater"
+ "MSDAssetUpdater init"
+ "MSDNotificationCleanEnergyCharging"
+ "No %{public}@ key in plist at %{public}@"
+ "No asset types to collect! Exiting query..."
+ "No device preferences have been saved in the preferences file under key %{public}@"
+ "No iCloud account. Can't query list of paired devices"
+ "Not starting asset query timer."
+ "OSPreferences"
+ "OutdatedAssets"
+ "PreferencesLanguage"
+ "PreferencesRegion"
+ "PreferencesSiriLanguage"
+ "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual"
+ "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup"
+ "Previous asset query already indicated update available."
+ "Provided S3 URL does not match stored URL pre-fix. Abandoning log upload"
+ "Query failed: result code %lu"
+ "Requested start asset query timer"
+ "Running catalog download for asset type %{public}@"
+ "Running query for asset type %{public}@"
+ "Screen saver idle delay: %{public}@ (minutes)"
+ "Setting Siri language to %{public}@"
+ "Siri language change complete"
+ "SiriLanguage"
+ "StagedOSPreferences"
+ "Starting Asset download op %{public}@"
+ "Starting asset query timer with interval %lu."
+ "Stopping asset query timer."
+ "SupportedDevices"
+ "SystemLanguage"
+ "SystemRegion"
+ "SystemSiriLanguage"
+ "T@\"BLSAssertion\",&,V_alwaysOnDisplayAssertion"
+ "T@\"MSDAssetUpdater\",&,V_assetUpdater"
+ "T@\"MSDPreferencesFile\",&,V_preferences"
+ "T@\"NSMutableArray\",&,V_assetTypes"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_assetUpdaterQueue"
+ "T@\"NSTimer\",&,V_queryTimer"
+ "TQ,V_queryInterval"
+ "The meta data for asset type %{public}@ was downloaded successfully"
+ "Timed out while downloading Assets"
+ "Timed out while waiting %dm for GreyMatter assets to download"
+ "Timed out while waiting for %{public}@ to download"
+ "Timer should not fire. Reasons:%{public}@\nEnd of reasons."
+ "_DownloadSize"
+ "_alwaysOnDisplayAssertion"
+ "_assetTypes"
+ "_assetUpdater"
+ "_assetUpdaterQueue"
+ "_preferences"
+ "_queryInterval"
+ "_queryTimer"
+ "acquireWithObserver:"
+ "addKeyValuePair:with:"
+ "addOperationWithBlock:"
+ "allAssetTypes"
+ "alwaysOnDisplayAssertion"
+ "applyStagedDevicePreferences:"
+ "assetId"
+ "assetToString:"
+ "assetType"
+ "assetTypes"
+ "assetUpdater"
+ "assetUpdaterQueue"
+ "assetsAvailable"
+ "attributes"
+ "checkAssetAvailabilityWithQuery:"
+ "cloudPairedDevices"
+ "collectAllAssetTypes"
+ "collectAllAssetTypesWithGM"
+ "collectDemoLogsToFolder:ofType:"
+ "com.apple.CloudSubscriptionFeatures.optIn"
+ "com.apple.MobileAsset.UAF.Siri"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "continueToUpdateAssets"
+ "continueToUpdateOSPreferences"
+ "demod BlockingUI Active"
+ "demod was never notified that the Siri language change request finished"
+ "disableAlwaysOn"
+ "disableCleanEnergyCharging"
+ "downloadAllAssetsWithCompletion:"
+ "downloadAssets:withError:"
+ "getAllGreyMatterAssetTypes"
+ "getCurrentSiriLanguage"
+ "getDemoPreferencesSiriLanguage"
+ "getIdentityServicesID"
+ "getListOfCloudPairedDevices"
+ "getSavedOSPreferencesRequest"
+ "getSiriLanguage"
+ "getStagedOSPreferencesRequest"
+ "handleGMFeatureFlag"
+ "hasOnlyGMAssetTypes"
+ "identityServicesID"
+ "informTimerFired"
+ "initWithExplanation:attributes:"
+ "initWithType:"
+ "languageCode"
+ "logAsset"
+ "logType"
+ "notifyCleanEnergyChargingToggled"
+ "nsuuid"
+ "preferences"
+ "queryAndDownloadAssetsWithForceGMAssetTypes:withError failed"
+ "queryAndDownloadAssetsWithForceGMAssetTypes:withError:"
+ "queryAndDownloadSiriAssetsWithError:"
+ "queryAssets"
+ "queryInterval"
+ "queryMetaData:"
+ "queryTimer"
+ "results"
+ "runQueryWithAssetType:"
+ "saveCurrentDeviceRegionCode"
+ "saveOSPreferencesRequest:"
+ "saveSiriLanguageToPreferences:"
+ "selectQueryInterval"
+ "setAlwaysOnDisplayAssertion:"
+ "setAssetTypes:"
+ "setAssetUpdater:"
+ "setAssetUpdaterQueue:"
+ "setAssetsAvailable:"
+ "setLanguage:withCompletion:"
+ "setQueryInterval:"
+ "setQueryTimer:"
+ "setSiriLanguage:"
+ "shouldIncludeGMAssetTypes"
+ "signOutFlowController:startSignOutForAccount:completion:"
+ "stageNewOSPreferences:"
+ "startAssetQueryTimer"
+ "startCatalogDownload:then:"
+ "startDownload:"
+ "stopAssetQueryTimer"
+ "string"
+ "supportsiCloudPairing"
+ "timerShouldFire"
+ "toggleAutoUpdate:forAssetTypes:"
+ "uniqueID"
+ "uploadDemoLogsTo:HttpHeaders:andMaxAttempts:ofType:"
+ "v16@?0q8"
+ "v48@0:8@16@24q32Q40"
+ "waitUntilAllOperationsAreFinished"
- "\x15\x13\x12"
- "!\x11"
- "%s: PlatformType '%{public}@'."
- "-[MSDHelperAgent collectDemoLogsToFolder:]"
- "/var/mobile/XcodeBuiltProducts/Tests/PressDemoScripts.xctestproducts"
- "13"
- "Demod obliterate Device"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "MSDDemoPreferencesLanguage"
- "MSDDemoPreferencesRegion"
- "MSDDemoSystemLanguage"
- "MSDDemoSystemRegion"
- "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides"
- "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IF_PlannerOverrides"
- "PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Siri_UnderstandingNLOverrides"
- "Screen saver idle delay: %{public}@ (seconds)"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "c"
- "f"
- "invalid Collection: less than 'count' elements in collection"
- "s"
- "saveCuurentDeviceRegionCode"
- "uploadDemoLogsTo:HttpHeaders:andMaxAttempts:"
- "yyyyMMdd"

```
