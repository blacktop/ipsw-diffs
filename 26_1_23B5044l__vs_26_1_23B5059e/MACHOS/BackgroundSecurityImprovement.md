## BackgroundSecurityImprovement

> `/System/Library/PreferenceBundles/BackgroundSecurityImprovement.bundle/BackgroundSecurityImprovement`

```diff

-508.40.16.0.0
-  __TEXT.__text: 0x84340
-  __TEXT.__auth_stubs: 0x1500
+508.40.50.0.0
+  __TEXT.__text: 0x94688
+  __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_methlist: 0x394
-  __TEXT.__const: 0x182c
-  __TEXT.__swift5_typeref: 0x31e4
-  __TEXT.__cstring: 0x1ab0
-  __TEXT.__objc_methname: 0xb4d
-  __TEXT.__swift5_capture: 0x166c
-  __TEXT.__swift5_reflstr: 0x7d0
-  __TEXT.__swift5_assocty: 0x150
-  __TEXT.__constg_swiftt: 0x80c
-  __TEXT.__swift5_fieldmd: 0x59c
-  __TEXT.__oslogstring: 0x13e3
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x98
+  __TEXT.__const: 0x186c
+  __TEXT.__swift5_typeref: 0x39bc
+  __TEXT.__cstring: 0x16e0
+  __TEXT.__objc_methname: 0xc7d
+  __TEXT.__swift5_capture: 0x1a10
+  __TEXT.__oslogstring: 0x186c
+  __TEXT.__swift5_reflstr: 0x660
+  __TEXT.__swift5_assocty: 0xd8
+  __TEXT.__constg_swiftt: 0x78c
+  __TEXT.__swift5_fieldmd: 0x400
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x88
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0x50
+  __TEXT.__swift_as_entry: 0xb0
+  __TEXT.__swift_as_ret: 0x5c
   __TEXT.__objc_classname: 0x21
   __TEXT.__objc_methtype: 0x630
-  __TEXT.__unwind_info: 0x15a0
-  __TEXT.__eh_frame: 0x1188
-  __DATA_CONST.__auth_got: 0xa80
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__auth_ptr: 0x3f8
-  __DATA_CONST.__const: 0x3c28
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x1858
+  __TEXT.__eh_frame: 0x14bc
+  __DATA_CONST.__auth_got: 0x9b8
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__auth_ptr: 0x3b8
+  __DATA_CONST.__const: 0x42b0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x6c0
-  __DATA.__objc_selrefs: 0x378
-  __DATA.__objc_data: 0x150
-  __DATA.__data: 0x10c0
-  __DATA.__bss: 0xe90
-  __DATA.__common: 0x20
+  __DATA.__objc_const: 0x5e8
+  __DATA.__objc_selrefs: 0x3e0
+  __DATA.__objc_data: 0x170
+  __DATA.__data: 0x1010
+  __DATA.__bss: 0x970
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 042CBE5D-8F02-3081-B3A3-A9A62577187B
-  Functions: 2115
-  Symbols:   148
-  CStrings:  431
+  UUID: D9C31D37-A81C-304A-902A-458161F2359F
+  Functions: 2254
+  Symbols:   143
+  CStrings:  415
 
Symbols:
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_SUInstallOptions
+ _UIApplicationWillEnterForegroundNotification
- _OBJC_CLASS_$_UIColor
- _objc_retain_x2
- _swift_allocBox
- _swift_getAssociatedConformanceWitness
- _swift_getAssociatedTypeWitness
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
CStrings:
+ " "
+ " This setting is currently managed by your organization. Contact your administrator for more information."
+ "App will enter foreground - refreshing security update status"
+ "Attempted to change state from .removing to %s - only handleRollbackFinished can change from .removing state"
+ "Background Security Improvements provide additional protection to your ProductFamilyName in between software updates. \n\nIn rare instances of compatibility issues, these security improvements may be temporarily removed and then enhanced in a future software update. [Learn More…](https://support.apple.com/102657)"
+ "Background Security Improvements require the latest version of OSName."
+ "Clicked 'Remove' Action in UpdateHistoryView but Rollback not Allowed"
+ "Download finished."
+ "Error fetching install history: %s"
+ "Failed to create UpdateHistoryData from event: %s"
+ "Failed to get documentation data for update type SUOSUpdateTypeSplat: %@"
+ "Install and turn on background security improvements?"
+ "Installed"
+ "No updates (splat or regular) has been found in scan results"
+ "Received rollbackDidFail event for: %s, error: %s"
+ "Received rollbackDidFail event with descriptor: %s,\nbut that's not the displaying descriptor: %s, ignoring this callback"
+ "Received rollbackDidFinish event with descriptor: %s"
+ "Received rollbackDidFinish event with descriptor: %s, \nbut that's not the displaying descriptor: %s, ignoring this callback"
+ "Rollback in progress detected, setting state to removing"
+ "Successfully retrieved documentation data for update type SUOSUpdateTypeSplat"
+ "The security of your DeviceFamilyName and personal data will be reduced if you turn off security improvements."
+ "Turn Off"
+ "Turn On"
+ "Turn off background security improvements?"
+ "_hasNonSplatDescriptor"
+ "_isInitializing"
+ "_presentedSplatDescriptor"
+ "_splatDocumentationData"
+ "alternateDescriptor"
+ "autoInstallSecurityResponseForceOff"
+ "autoInstallSecurityResponseForceOn"
+ "build"
+ "checkmark.seal.fill"
+ "date"
+ "dateFromString:"
+ "defaultCenter"
+ "disableRollback"
+ "fetchInstallHistory:"
+ "getDocumentationDataForInstalledUpdateType:error:"
+ "getInstallHistoryEvents()"
+ "handleScanFinished found (only) a regular updates."
+ "handleScanFinished found a splat update to display: %s"
+ "identifier"
+ "initializationLock"
+ "initializeState already in progress, ignoring duplicate call"
+ "initializeState completed"
+ "installUpdateWithInstallOptions:withResult:"
+ "isRollingBack:"
+ "isSplatOnly"
+ "name"
+ "nil"
+ "onAppear called"
+ "onReceive for willEnterForegroundNotification called"
+ "operationType"
+ "performFailedStateInstallAction()"
+ "performInstallAction()"
+ "performInstallWithPasscodeAndConfirmationFromUser(update:needsPasscode:approvalCallback:failureCallback:)"
+ "productVersionExtra"
+ "readmeSummary"
+ "received scanRequestDidFinishFor, but from other client request. Options might not contains Splat updates search type, so ignoring as this is not a useful result for the BSI pane logic."
+ "rollbackUpdate call has started with result: %{bool}d, rollbackDescriptor: %s, error: %s"
+ "setDateFormat:"
+ "setDownloadOnly:"
+ "setIdentifier:"
+ "settings-navigation://com.apple.Settings.PrivacyAndSecurity/BACKGROUND_SECURITY_IMPROVEMENTS"
+ "update already downloaded."
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "yyyy-MM-dd HH:mm:ss"
- "/CoreAnalytics/"
- "/SUS_History_Tracking.log"
- "/installHistory.db"
- "/private/var/SUS/history"
- "22B124"
- "22B83"
- "Background Security Improvement improves the security of your ProductFamilyName by installing security improvements and system files before they are available in OSName Software Updates. \n\nIn rare instances of compatibility issues, these deliveries may be temporarily removed and then improved in a feature software update.[Learn More…](https://support.apple.com/102657)"
- "Background Security Improvements requires the latest version of OSName."
- "Checking for updates…"
- "DOWNLOAD"
- "DOWNLOAD_ALT"
- "Debug error state"
- "Download failed"
- "ERROR"
- "ERROR_CONTINUITY_CAMERA_IN_USE"
- "ERROR_DOWNLOAD_FAILED"
- "ERROR_STANDARD"
- "INSTALL"
- "INSTALL_COMPLETE"
- "Index out of range"
- "Initialized SUSHistoryTracker with %ld mock events"
- "Installation failed"
- "Last Update"
- "QUIET_OPERATION"
- "Range requires lowerBound <= upperBound"
- "Received rollbackUpdate callback - result: %{bool}d, rollbackDescriptor: %s, error: %s"
- "Recorded history event: %ld for type: %ld"
- "Remove failed"
- "Rescan"
- "Rollback failed for: %s, error: %s"
- "Rollback finished for: %s"
- "SCAN"
- "SCAN_OTA_SLOW_ROLL_FOUND"
- "SPACE"
- "Scan request finished but does not contain Splat updates search type. Ignoring."
- "Security Update 2025-001"
- "Submitted history analytics events"
- "Swift/ArrayShared.swift"
- "Swift/Range.swift"
- "This security update addresses critical vulnerabilities and improves system stability."
- "Unknown Version"
- "Update exists, going to display it soon by the scanRequestDidFinishFor callback"
- "_TtC29BackgroundSecurityImprovement17SUSHistoryTracker"
- "_presentedDescriptor"
- "addType:"
- "basePath"
- "com.apple.sus.history.protection"
- "containsType:"
- "coreAnalyticsPath"
- "exclamationmark.triangle.fill"
- "failedStateButtonView"
- "historyEvents"
- "historyInstallDBPath"
- "historyLogPath"
- "historyType"
- "iOS 18.1.1 (22B83)"
- "id"
- "installUpdate:"
- "invalid Collection: count differed in successive traversals"
- "kSUSHistoryAlternateBuildInfo"
- "kSUSHistoryAlternateVersionInfo"
- "kSUSHistoryAppOffloadEnabled"
- "kSUSHistoryCacheDeleteEnabled"
- "kSUSHistoryDisplayNameInfo"
- "kSUSHistoryErrorCodeInfo"
- "kSUSHistoryErrorMessageInfo"
- "kSUSHistoryIsBackground"
- "kSUSHistoryIsForeground"
- "kSUSHistoryIsSplat"
- "kSUSHistoryIsSplombo"
- "kSUSHistoryPreferredBuildInfo"
- "kSUSHistoryPreferredVersionInfo"
- "kSUSHistoryTargetBuildInfo"
- "kSUSHistoryTargetVersionInfo"
- "kSUSHistoryUserInitiated"
- "operation"
- "performInstallWithPasscodeAndConfirmationFromUser(update:needsPasscode:approvalCallback:)"
- "protectionQueue"
- "scanFinished called with descriptor: %s"
- "settings-navigation://com.apple.Settings.General/BackgroundSecurityImprovement"
- "systemGroupedBackgroundColor"
- "timestamp"
- "updateFoundButtonView"
- "version"

```
