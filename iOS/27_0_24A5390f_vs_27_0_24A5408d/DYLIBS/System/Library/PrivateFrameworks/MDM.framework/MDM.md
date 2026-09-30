## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-113.0.2.0.0
-  __TEXT.__text: 0x585d0
-  __TEXT.__objc_methlist: 0x43a4
+113.2.5.0.0
+  __TEXT.__text: 0x5559c
+  __TEXT.__objc_methlist: 0x42d4
   __TEXT.__const: 0x1c2
   __TEXT.__gcc_except_tab: 0xf08
-  __TEXT.__cstring: 0x58c0
-  __TEXT.__oslogstring: 0x76e4
+  __TEXT.__cstring: 0x532d
+  __TEXT.__oslogstring: 0x70d4
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x1310
+  __TEXT.__unwind_info: 0x12c0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f68
+  __DATA_CONST.__const: 0x1eb8
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35c0
+  __DATA_CONST.__objc_selrefs: 0x3478
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x408
-  __DATA_CONST.__got: 0x1270
+  __DATA_CONST.__got: 0x1230
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x52c0
-  __AUTH_CONST.__objc_const: 0x6c08
+  __AUTH_CONST.__cfstring: 0x4bc0
+  __AUTH_CONST.__objc_const: 0x6c58
   __AUTH_CONST.__objc_arrayobj: 0x8d0
   __AUTH_CONST.__objc_intobj: 0x660
-  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH_CONST.__auth_got: 0x7e0
   __AUTH.__objc_data: 0x638
-  __DATA.__objc_ivar: 0x2a4
+  __DATA.__objc_ivar: 0x2ac
   __DATA.__data: 0x7f0
   __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0xa28

   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
-  - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1711
-  Symbols:   4970
-  CStrings:  1370
+  Functions: 1687
+  Symbols:   4897
+  CStrings:  1272
 
Symbols:
+ -[MDMDEPPushTokenManager cachedLastPushTokenHash]
+ -[MDMDEPPushTokenManager cachedLastSyncedEligibility]
+ -[MDMDEPPushTokenManager setCachedLastPushTokenHash:]
+ -[MDMDEPPushTokenManager setCachedLastSyncedEligibility:]
+ GCC_except_table110
+ GCC_except_table147
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table216
+ GCC_except_table227
+ GCC_except_table232
+ GCC_except_table253
+ GCC_except_table287
+ GCC_except_table294
+ GCC_except_table305
+ GCC_except_table318
+ GCC_except_table329
+ GCC_except_table333
+ GCC_except_table344
+ GCC_except_table348
+ GCC_except_table364
+ _OBJC_CLASS_$_DMCProcessAssertion
+ _OBJC_IVAR_$_MDMDEPPushTokenManager._cachedLastPushTokenHash
+ _OBJC_IVAR_$_MDMDEPPushTokenManager._cachedLastSyncedEligibility
+ _objc_msgSend$cachedLastPushTokenHash
+ _objc_msgSend$cachedLastSyncedEligibility
+ _objc_msgSend$setCachedLastPushTokenHash:
+ _objc_msgSend$setCachedLastSyncedEligibility:
- +[MDMParser _dmfAction:fromMDMActionString:]
- +[MDMParser _errorFromDMFSoftwareUpdateError:]
- +[MDMParser _errorWithDomain:code:descriptionKey:underlyingError:type:]
- +[MDMParser _resolvedInstallActionStringForAction:]
- +[MDMParser _shouldUseDelayWithRequest:]
- +[MDMParser _statusFromError:action:]
- +[MDMParser _updateDictionaryFromUpdate:]
- +[MDMParser _useDelayFlagAllowed]
- -[MDMParser _availableOSUpdates:assertion:completionBlock:]
- -[MDMParser _dmfScheduleOSUpdate:assertion:completionBlock:]
- -[MDMParser _mdmScheduleOSUpdate:assertion:completionBlock:]
- -[MDMParser _performSetUpdatePath:]
- -[MDMParser _platformSupportsOSUpdateManagement]
- -[MDMParser _rejectSoftwareUpdateBecauseOfMalformedRequestCompletionBlock:]
- -[MDMParser _rejectSoftwareUpdateBecauseUserLoggedInCompletionBlock:]
- -[MDMParser _responseForMalformedUpdateRequest]
- -[MDMParser _scheduleOSUpdate:assertion:completionBlock:]
- -[MDMParser _scheduleOSUpdateScan:assertion:completionBlock:]
- -[MDMParser _softwareUpdatesNotPermittedWithLoggedInUserError]
- -[MDMParser _statusOfOSUpdates:assertion:completionBlock:]
- -[MDMServerCore softwareUpdatePathFromDisk]
- GCC_except_table111
- GCC_except_table150
- GCC_except_table190
- GCC_except_table193
- GCC_except_table196
- GCC_except_table209
- GCC_except_table212
- GCC_except_table220
- GCC_except_table228
- GCC_except_table233
- GCC_except_table254
- GCC_except_table288
- GCC_except_table295
- GCC_except_table306
- GCC_except_table319
- GCC_except_table330
- GCC_except_table334
- GCC_except_table345
- GCC_except_table349
- GCC_except_table365
- _DMCErrorTypeNeedsRetry
- _DMCInternalErrorDomain
- _DMCSendSettingsChangedNotification
- _OBJC_CLASS_$_MDFFetchAvailableOSUpdatesRequest
- _OBJC_CLASS_$_MDFFetchOSUpdateStatusRequest
- _OBJC_CLASS_$_MDFScheduleOSUpdateRequest
- _OBJC_CLASS_$_SUUtility
- ___35-[MDMParser _performSetUpdatePath:]_block_invoke
- ___57-[MDMParser _scheduleOSUpdate:assertion:completionBlock:]_block_invoke
- ___58-[MDMParser _statusOfOSUpdates:assertion:completionBlock:]_block_invoke
- ___59-[MDMParser _availableOSUpdates:assertion:completionBlock:]_block_invoke
- ___NSArray0__struct
- _kMDMPQuerySoftwareUpdate
- _kMDMPQuerySoftwareUpdateDeviceID
- _kMDMPRequestTypeAvailableOSUpdates
- _kMDMPRequestTypeOSUpdateStatus
- _kMDMPRequestTypeScheduleOSUpdate
- _kMDMPRequestTypeScheduleOSUpdateScan
- _kMDMPSettingsSettingsSoftwareUpdate
- _kSettingsSettingsSoftwareUpdatePathKey
- _objc_msgSend$_availableOSUpdates:assertion:completionBlock:
- _objc_msgSend$_dmfAction:fromMDMActionString:
- _objc_msgSend$_dmfScheduleOSUpdate:assertion:completionBlock:
- _objc_msgSend$_errorFromDMFSoftwareUpdateError:
- _objc_msgSend$_errorWithDomain:code:descriptionKey:underlyingError:type:
- _objc_msgSend$_performSetUpdatePath:
- _objc_msgSend$_platformSupportsOSUpdateManagement
- _objc_msgSend$_rejectSoftwareUpdateBecauseOfMalformedRequestCompletionBlock:
- _objc_msgSend$_rejectSoftwareUpdateBecauseUserLoggedInCompletionBlock:
- _objc_msgSend$_resolvedInstallActionStringForAction:
- _objc_msgSend$_scheduleOSUpdate:assertion:completionBlock:
- _objc_msgSend$_scheduleOSUpdateScan:assertion:completionBlock:
- _objc_msgSend$_shouldUseDelayWithRequest:
- _objc_msgSend$_softwareUpdatesNotPermittedWithLoggedInUserError
- _objc_msgSend$_statusFromError:action:
- _objc_msgSend$_statusOfOSUpdates:assertion:completionBlock:
- _objc_msgSend$_updateDictionaryFromUpdate:
- _objc_msgSend$_useDelayFlagAllowed
- _objc_msgSend$action
- _objc_msgSend$allowsInstallLater
- _objc_msgSend$alternateDSID
- _objc_msgSend$boolForKey:
- _objc_msgSend$build
- _objc_msgSend$currentProductType
- _objc_msgSend$downloadPercentComplete
- _objc_msgSend$downloadSize
- _objc_msgSend$humanReadableName
- _objc_msgSend$installSize
- _objc_msgSend$isCritical
- _objc_msgSend$isSplat
- _objc_msgSend$lowercaseString
- _objc_msgSend$productKey
- _objc_msgSend$productName
- _objc_msgSend$restartRequired
- _objc_msgSend$setAction:
- _objc_msgSend$setProductKey:
- _objc_msgSend$setProductVersion:
- _objc_msgSend$setUseDelay:
- _objc_msgSend$softwareUpdateDeviceIDWithDefaultValue:
- _objc_msgSend$softwareUpdatePathFromDisk
- _objc_msgSend$supplementalBuild
- _objc_msgSend$supplementalVersionExtra
- _objc_msgSend$update
CStrings:
+ "DEP push token sync in flight"
+ "Failed to persist lastPushTokenHash (cache is authoritative) with error: %{public}@"
+ "Failed to persist lastSyncedEligibility (cache is authoritative) with error: %{public}@"
+ "Ignoring deadlineToSync of unexpected class: %{public}@"
+ "Ignoring lastPushTokenHash of unexpected class: %{public}@"
+ "Ignoring lastSyncedEligibility of unexpected class: %{public}@"
+ "Ignoring lastestPushTokenHashToSync of unexpected class: %{public}@"
- "-[MDMParser _availableOSUpdates:assertion:completionBlock:]"
- "-[MDMParser _statusOfOSUpdates:assertion:completionBlock:]"
- "AllowsInstallLater"
- "Available OS update end."
- "Available OS update start."
- "AvailableOSUpdates"
- "Build"
- "Can't fetch OS update status due to user logged in."
- "Can't fetch available updates due to user logged in."
- "Could not check for available iOS updates - %{public}@"
- "Could not check for iOS update status - %{public}@"
- "Could not schedule an update - %{public}@"
- "DMF Schedule OS update end."
- "DMF Schedule OS update start."
- "Did not write to plist!"
- "DownloadFailed"
- "DownloadInsufficientNetwork"
- "DownloadInsufficientPower"
- "DownloadInsufficientSpace"
- "DownloadOnly"
- "DownloadPercentComplete"
- "DownloadRequiresComputer"
- "DownloadSize"
- "Downloading"
- "Failed to get lastPushTokenHash with error: %{public}@"
- "Failed to get lastSyncedEligibility with error: %{public}@"
- "Failed to set lastPushTokenHash with error: %{public}@"
- "Failed to set lastSyncedEligibility with error: %{public}@"
- "HumanReadableName"
- "InstallASAP"
- "InstallAction"
- "InstallFailed"
- "InstallInsufficientPower"
- "InstallInsufficientSpace"
- "InstallSize"
- "IsCritical"
- "IsDownloaded"
- "IsSecurityResponse"
- "MCUseSoftwareUpdateDelayFlagAllowed"
- "MDM Schedule OS update end."
- "MDM Schedule OS update start."
- "MDMParser.m"
- "MDM_ERROR_SU_DEVICE_PASSCODE_MUST_BE_CLEARED"
- "MDM_ERROR_SU_DOWNLOAD_COMPLETE"
- "MDM_ERROR_SU_DOWNLOAD_FAILED"
- "MDM_ERROR_SU_DOWNLOAD_INSUFFICIENT_NETWORK"
- "MDM_ERROR_SU_DOWNLOAD_INSUFFICIENT_POWER"
- "MDM_ERROR_SU_DOWNLOAD_INSUFFICIENT_SPACE"
- "MDM_ERROR_SU_DOWNLOAD_IN_PROGRESS"
- "MDM_ERROR_SU_DOWNLOAD_REQUIRES_COMPUTER"
- "MDM_ERROR_SU_INSTALL_FAILED"
- "MDM_ERROR_SU_INSTALL_INSUFFICIENT_POWER"
- "MDM_ERROR_SU_INSTALL_INSUFFICIENT_SPACE"
- "MDM_ERROR_SU_INSTALL_IN_PROGRESS"
- "MDM_ERROR_SU_INSTALL_REQUIRES_DOWNLOAD"
- "MDM_ERROR_SU_NOT_PERMITTED_WITH_LOGGED_IN_USER"
- "MDM_ERROR_SU_NO_UPDATE_AVAILABLE"
- "MDM_ERROR_SU_SCAN_FAILED"
- "NO"
- "No update available."
- "No updates available."
- "OSUpdateStatus"
- "OSUpdateStatus DMF raw data: %{public}@"
- "OSUpdateStatus response: %{public}@"
- "ProductKey"
- "ProductName"
- "ProductVersion"
- "RecommendationCadence"
- "Rejected software update due to \"use delay\" bad request."
- "Rejected software update due to install action being non-default, non-download only nor immediate install actions."
- "Rejected software update due to malformed OS update action."
- "Rejected software update due to malformed install action."
- "Rejected software update due to malformed product key."
- "Rejected software update due to malformed product version."
- "Rejected software update due to malformed update array."
- "Rejected software update due to malformed update object."
- "Rejected software update due to missing or malformed OS update object."
- "Rejected software update due to missing or malformed update array."
- "Rejected software update due to multiple OS update objects."
- "Rejected software update due to user logged in."
- "Requesting an update with a specific PMV - %{public}@"
- "Requesting an update with any PMV"
- "RestartRequired"
- "Returning updates array: %{public}@"
- "Schedule OS update end."
- "Schedule OS update scan end."
- "Schedule OS update scan start."
- "Schedule OS update start"
- "ScheduleOSUpdate"
- "ScheduleOSUpdateScan"
- "SoftwareUpdateSettings"
- "Status of OS update end."
- "Status of OS update start."
- "SupplementalBuildVersion"
- "SupplementalOSVersionExtra"
- "Unknown software update error"
- "UpdateResults"
- "Updates"
- "UseDelay"
- "Writing Software Update setting to disk."
- "YES"
- "availableOSUpdates useDelay = %{public}@"
- "dmfError != nil"
- "scheduleOSUpdate useDelay = %{public}@"
- "useDelayFlagAllowed = %{public}@"
```
