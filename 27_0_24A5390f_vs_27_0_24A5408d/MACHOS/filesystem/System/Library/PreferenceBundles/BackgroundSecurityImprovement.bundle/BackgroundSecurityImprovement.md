## BackgroundSecurityImprovement

> `/System/Library/PreferenceBundles/BackgroundSecurityImprovement.bundle/BackgroundSecurityImprovement`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-772.0.10.0.0
-  __TEXT.__text: 0xe0860
+772.0.20.0.0
+  __TEXT.__text: 0xe1a58
   __TEXT.__auth_stubs: 0x18c0
   __TEXT.__objc_stubs: 0xc20
   __TEXT.__objc_methlist: 0x420
+  __TEXT.__const: 0x2b68
   __TEXT.__cstring: 0x1cbc
-  __TEXT.__const: 0x2ac8
   __TEXT.__swift5_typeref: 0x4a42
   __TEXT.__swift5_reflstr: 0xa14
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__constg_swiftt: 0xab0
+  __TEXT.__constg_swiftt: 0xabc
   __TEXT.__swift5_fieldmd: 0x5e4
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0xb4
-  __TEXT.__oslogstring: 0x2bba
-  __TEXT.__swift5_capture: 0x2cf0
+  __TEXT.__oslogstring: 0x2eca
+  __TEXT.__swift5_capture: 0x2d5c
   __TEXT.__objc_classname: 0x1d7
   __TEXT.__objc_methname: 0x1403
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__swift_as_entry: 0x15c
-  __TEXT.__swift_as_ret: 0xd4
-  __TEXT.__swift_as_cont: 0x1c0
+  __TEXT.__swift_as_entry: 0x160
+  __TEXT.__swift_as_ret: 0xd8
+  __TEXT.__swift_as_cont: 0x1cc
   __TEXT.__objc_methtype: 0x8cd
-  __TEXT.__unwind_info: 0x2690
+  __TEXT.__unwind_info: 0x26c8
   __TEXT.__eh_frame: 0x2004
-  __DATA_CONST.__const: 0x7250
+  __DATA_CONST.__const: 0x7340
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3687
-  Symbols:   186
-  CStrings:  612
+  Functions: 3707
+  Symbols:   188
+  CStrings:  613
 
Symbols:
+ _BackgroundSecurityImprovementVersionNumber
+ _BackgroundSecurityImprovementVersionString
CStrings:
+ "(loadInstalledSplatUpdate) Installed update found:\n%{public}s"
+ "Battery level changed: %{public}f -> %{public}f"
+ "Battery monitoring initialized: level=%{public}f, connected=%{bool,public}d"
+ "Battery state changed: %{bool,public}d -> %{bool,public}d"
+ "Clearing space for download: %{bool,public}d, update: %{public}s"
+ "Device cellular capability check: dataService=%{bool,public}d, radioTech=%{bool,public}d"
+ "Download failed for update: %{public}s, error: %{public}s"
+ "Download finished for update: %{public}s"
+ "Download initiated for update: %{public}s success: %{bool,public}d, error: %{public}s"
+ "Download progress changed for update: %{public}s, progress: %{public}@"
+ "Download started for update: %{public}s"
+ "Error fetching install history: %{public}s"
+ "Error while calling isRollingBack: %{public}s for descriptor: %{public}s"
+ "Failed to get DDM declaration: %{public}@"
+ "Failed to get documentation data for update type SUOSUpdateTypeSplat: %{public}@"
+ "Found active SPLAT download with descriptor: %{public}s"
+ "Found installFinishedBootUUID: %{public}s, current: %{public}s"
+ "Found rollbackFinishedBootUUID: %{public}s, current: %{public}s"
+ "Handling DDM declaration: %{public}s"
+ "Installation failed for update: %{public}s, error: %{public}s"
+ "Installation finished for update: %{public}s"
+ "Installation started for update: %{public}s"
+ "Manager state changing from %{public}s to %{public}s"
+ "Manager state unchanged: %{public}s"
+ "Network monitoring initialized: connected=%{bool,public}d, type=%{public}u"
+ "Network status changed:\nFrom: %{public}s (%{public}u)\nTo: %{public}s (%{public}u)"
+ "Passcode challenge failed with error '%{public}s'"
+ "Persisting installFinished: %{bool,public}d"
+ "Persisting rollbackFinished: %{bool,public}d"
+ "Processing DDM declaration with declarationKey: %{public}s"
+ "Received installUpdate callback - success: %{bool,public}d, error: %{public}s"
+ "Received rollbackDidFail event for: %{public}s, error: %{public}s"
+ "Received rollbackDidFinish event with descriptor: %{public}s"
+ "Received scan callback - results: %{public}s, error: %{public}s"
+ "Restored installFinished flag from persistence: %{bool,public}d"
+ "Restored rollbackFinished flag from persistence: %{bool,public}d"
+ "Rollback started for: %{public}s"
+ "Scan request finished - results: %{public}s, error: %{public}s"
+ "Scan request started with options: %{public}s"
+ "Updated build number visibility on appear to match isInternalBuild: %{bool,public}d"
+ "Updated build number visibility to match isInternalBuild: %{bool,public}d"
+ "downloadAndInstall called with update: %{public}s"
+ "getInstallHistoryEvents returning %{public}ld history events"
+ "handleDownloadFinished called for update: %{public}s, success: %{bool,public}d"
+ "handleInstallFinished called for update: %{public}s, success: %{bool,public}d"
+ "handleInstallFinished result : isSuccessfullyInstalled is %{bool,public}d"
+ "handleRollbackFinished called, success: %{bool,public}d"
+ "handleScanFinished found a splat update to display: %{public}s"
+ "hasSemiSplatActive: %{bool,public}d"
+ "initializeAutoInstallForceOffStatus: autoInstallSecurityForceOff returned %{bool,public}d"
+ "initializeAutoInstallForceOnStatus: autoInstallSecurityForceOn returned %{bool,public}d"
+ "initializeAutomaticSecurityUpdatesDisabledStatus: shouldDisableAutoInstallRSRToggle returned %{bool,public}d"
+ "initializeInternalBuildStatus: MobileGestalt.current.internalBuild returned %{bool,public}d"
+ "initializeState - after initializationLock.withLock, shouldProceed: %{bool,public}d"
+ "installStarted called for update: %{public}s"
+ "installUpdate called with update: %{public}s"
+ "isSplatOnlyUpdateRollbackAllowed threw an error (%{public}@), rollback is not allowed"
+ "isSplatOnlyUpdateRollbackAllowedBySUS is %{bool,public}d, that will determine if we can allow rollback action"
+ "kern.bootsessionuuid UUID: %{public}s"
+ "kern.bootsessionuuid call returned error, result is: %{public}d"
+ "performActualInstallation: install could not start - success: %{bool,public}d, error: %{public}s"
+ "performActualInstallation: scan in progress during install attempt for %{public}s, retrying after scan completes."
+ "rollbackUpdate call has started with result: %{bool,public}d, rollbackDescriptor: %{public}s, error: %{public}s"
+ "rollbackUpdate: SUS failed to start rollback, result: %{bool,public}d, error: %{public}s"
+ "shouldDisplayRebootButtonInHistoryView: returned %{bool,public}d"
+ "waitUntilClientIsNotScanning: error querying isScanning: %{public}@, proceeding"
- "(loadInstalledSplatUpdate) Installed update found:\n%s"
- "Battery level changed: %f -> %f"
- "Battery monitoring initialized: level=%f, connected=%{bool}d"
- "Battery state changed: %{bool}d -> %{bool}d"
- "Clearing space for download: %{bool}d, update: %s"
- "Device cellular capability check: dataService=%{bool}d, radioTech=%{bool}d"
- "Download failed for update: %s, error: %s"
- "Download finished for update: %s"
- "Download initiated for update: %s success: %{bool}d, error: %s"
- "Download progress changed for update: %s, progress: %@"
- "Download started for update: %s"
- "Error fetching install history: %s"
- "Error while calling isRollingBack: %s for descriptor: %s"
- "Failed to get DDM declaration: %@"
- "Failed to get documentation data for update type SUOSUpdateTypeSplat: %@"
- "Found active SPLAT download with descriptor: %s"
- "Found installFinishedBootUUID: %s, current: %s"
- "Found rollbackFinishedBootUUID: %s, current: %s"
- "Handling DDM declaration: %s"
- "Installation failed for update: %s, error: %s"
- "Installation finished for update: %s"
- "Installation started for update: %s"
- "Manager state changing from %s to %s"
- "Manager state unchanged: %s"
- "Network monitoring initialized: connected=%{bool}d, type=%u"
- "Network status changed:\nFrom: %s (%u)\nTo: %s (%u)"
- "Passcode challenge failed with error '%s'"
- "Persisting installFinished: %{bool}d"
- "Persisting rollbackFinished: %{bool}d"
- "Processing DDM declaration with declarationKey: %s"
- "Received installUpdate callback - success: %{bool}d, error: %s"
- "Received rollbackDidFail event for: %s, error: %s"
- "Received rollbackDidFinish event with descriptor: %s"
- "Received scan callback - results: %s, error: %s"
- "Restored installFinished flag from persistence: %{bool}d"
- "Restored rollbackFinished flag from persistence: %{bool}d"
- "Rollback started for: %s"
- "Scan request finished - results: %s, error: %s"
- "Scan request started with options: %s"
- "Updated build number visibility on appear to match isInternalBuild: %{bool}d"
- "Updated build number visibility to match isInternalBuild: %{bool}d"
- "downloadAndInstall called with update: %s"
- "getInstallHistoryEvents returning %ld history events"
- "handleDownloadFinished called for update: %s, success: %{bool}d"
- "handleInstallFinished called for update: %s, success: %{bool}d"
- "handleInstallFinished result : isSuccessfullyInstalled is %{bool}d"
- "handleRollbackFinished called, success: %{bool}d"
- "handleScanFinished found a splat update to display: %s"
- "hasSemiSplatActive: %{bool}d"
- "initializeAutoInstallForceOffStatus: autoInstallSecurityForceOff returned %{bool}d"
- "initializeAutoInstallForceOnStatus: autoInstallSecurityForceOn returned %{bool}d"
- "initializeAutomaticSecurityUpdatesDisabledStatus: shouldDisableAutoInstallRSRToggle returned %{bool}d"
- "initializeInternalBuildStatus: MobileGestalt.current.internalBuild returned %{bool}d"
- "initializeState - after initializationLock.withLock, shouldProceed: %{bool}d"
- "installStarted called for update: %s"
- "installUpdate called with update: %s"
- "isSplatOnlyUpdateRollbackAllowed threw an error (%@), rollback is not allowed"
- "isSplatOnlyUpdateRollbackAllowedBySUS is %{bool}d, that will determine if we can allow rollback action"
- "kern.bootsessionuuid UUID: %s"
- "kern.bootsessionuuid call returned error, result is: %d"
- "performActualInstallation: install could not start - success: %{bool}d, error: %s"
- "rollbackUpdate call has started with result: %{bool}d, rollbackDescriptor: %s, error: %s"
- "rollbackUpdate: SUS failed to start rollback, result: %{bool}d, error: %s"
- "shouldDisplayRebootButtonInHistoryView: returned %{bool}d"
- "waitUntilClientIsNotScanning: error querying isScanning: %@, proceeding"
```
