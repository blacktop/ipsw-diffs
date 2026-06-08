## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-251.120.2.0.0
-  __TEXT.__text: 0x423c4
+300.0.0.0.0
+  __TEXT.__text: 0x40b38
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0x5420
-  __TEXT.__objc_methlist: 0x2b84
-  __TEXT.__cstring: 0x3e80
-  __TEXT.__objc_methname: 0x60da
-  __TEXT.__oslogstring: 0x4703
-  __TEXT.__objc_classname: 0x74c
-  __TEXT.__objc_methtype: 0x1252
-  __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__unwind_info: 0x678
-  __DATA_CONST.__auth_got: 0x240
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0x6580
-  __DATA_CONST.__cfstring: 0x32e0
+  __TEXT.__objc_stubs: 0x5480
+  __TEXT.__objc_methlist: 0x2b9c
+  __TEXT.__cstring: 0x3e3d
+  __TEXT.__objc_methname: 0x610c
+  __TEXT.__oslogstring: 0x466b
+  __TEXT.__objc_classname: 0x61d
+  __TEXT.__objc_methtype: 0x11e8
+  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__unwind_info: 0x670
+  __DATA_CONST.__const: 0x6b38
+  __DATA_CONST.__cfstring: 0x3440
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_arraydata: 0xf8
-  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x180
+  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x448
   __DATA.__objc_const: 0x4848
-  __DATA.__objc_selrefs: 0x1920
+  __DATA.__objc_selrefs: 0x1938
   __DATA.__objc_ivar: 0x254
   __DATA.__objc_data: 0xd70
   __DATA.__data: 0x7a0

   - /System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI
+  - /System/Library/PrivateFrameworks/TipsCore.framework/TipsCore
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7E3096E-BFD3-3BD7-A3B2-4C45C1D8EFE5
-  Functions: 996
-  Symbols:   314
-  CStrings:  2415
+  UUID: D5B92E21-E44E-3E88-9674-8CE3F390D065
+  Functions: 1002
+  Symbols:   316
+  CStrings:  2439
 
Symbols:
+ OBJC_IVAR_$_SUSUIDownloadFailedAlertItem._error
+ _OBJC_CLASS_$_SUSUIAlertModel
+ _OBJC_CLASS_$_SUSUIAvailableAlertItem
+ _OBJC_CLASS_$_SUSUIBaseInstallFailureAlertItem
+ _OBJC_CLASS_$_SUSUIBaseUpdateAlertItem
+ _OBJC_CLASS_$_SUSUIController
+ _OBJC_CLASS_$_SUSUIDefaults
+ _OBJC_CLASS_$_SUSUIDownloadFailedAlertItem
+ _OBJC_CLASS_$_SUSUIInstallAlertItem
+ _OBJC_CLASS_$_SUSUIInstallLaterAlertItem
+ _OBJC_CLASS_$_SUSUIInstallOperationLifeCycleHandler
+ _OBJC_CLASS_$_SUSUIInstallOptions
+ _OBJC_CLASS_$_SUSUIRebootingAlertItem
+ _OBJC_CLASS_$_SUSUIRecommendedAlertItem
+ _OBJC_CLASS_$_SUSUIRollbackFailureAlertItem
+ _OBJC_CLASS_$_SUSUIStatePersistence
+ _OBJC_CLASS_$_SUSUIUnableToInstallAlertItem
+ _OBJC_CLASS_$_SUSUIVerificationFailedAlertItem
+ _OBJC_CLASS_$_SUSUIVerifyingUpdateAlertItem
+ _OBJC_CLASS_$_TPSTipContentConfiguration
+ _OBJC_METACLASS_$_SUSUIAlertModel
+ _OBJC_METACLASS_$_SUSUIAvailableAlertItem
+ _OBJC_METACLASS_$_SUSUIBaseInstallFailureAlertItem
+ _OBJC_METACLASS_$_SUSUIBaseUpdateAlertItem
+ _OBJC_METACLASS_$_SUSUIController
+ _OBJC_METACLASS_$_SUSUIDownloadFailedAlertItem
+ _OBJC_METACLASS_$_SUSUIInstallAlertItem
+ _OBJC_METACLASS_$_SUSUIInstallLaterAlertItem
+ _OBJC_METACLASS_$_SUSUIInstallOperationLifeCycleHandler
+ _OBJC_METACLASS_$_SUSUIInstallOptions
+ _OBJC_METACLASS_$_SUSUIRebootingAlertItem
+ _OBJC_METACLASS_$_SUSUIRecommendedAlertItem
+ _OBJC_METACLASS_$_SUSUIRollbackFailureAlertItem
+ _OBJC_METACLASS_$_SUSUIStatePersistence
+ _OBJC_METACLASS_$_SUSUIUnableToInstallAlertItem
+ _OBJC_METACLASS_$_SUSUIVerificationFailedAlertItem
+ _OBJC_METACLASS_$_SUSUIVerifyingUpdateAlertItem
+ _kSUSUISettingsURL
+ _kSupportFlowURL
- OBJC_IVAR_$_SUSUISoftwareUpdateDownloadFailedAlertItem._error
- _OBJC_CLASS_$_SUSUIBaseSoftwareUpdateAlertItem
- _OBJC_CLASS_$_SUSUIBaseSoftwareUpdateInstallFailureAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateAlertModel
- _OBJC_CLASS_$_SUSUISoftwareUpdateAvailableAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateController
- _OBJC_CLASS_$_SUSUISoftwareUpdateDefaults
- _OBJC_CLASS_$_SUSUISoftwareUpdateDownloadFailedAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateInstallAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateInstallLaterAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateInstallOperationLifeCycleHandler
- _OBJC_CLASS_$_SUSUISoftwareUpdateInstallOptions
- _OBJC_CLASS_$_SUSUISoftwareUpdateRebootingAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateRecommendedAvailableAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateRollbackFailureAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateStatePersistence
- _OBJC_CLASS_$_SUSUISoftwareUpdateUnableToInstallAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateVerificationFailedAlertItem
- _OBJC_CLASS_$_SUSUISoftwareUpdateVerifyingUpdateAlertItem
- _OBJC_METACLASS_$_SUSUIBaseSoftwareUpdateAlertItem
- _OBJC_METACLASS_$_SUSUIBaseSoftwareUpdateInstallFailureAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateAlertModel
- _OBJC_METACLASS_$_SUSUISoftwareUpdateAvailableAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateController
- _OBJC_METACLASS_$_SUSUISoftwareUpdateDownloadFailedAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateInstallAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateInstallLaterAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateInstallOperationLifeCycleHandler
- _OBJC_METACLASS_$_SUSUISoftwareUpdateInstallOptions
- _OBJC_METACLASS_$_SUSUISoftwareUpdateRebootingAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateRecommendedAvailableAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateRollbackFailureAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateStatePersistence
- _OBJC_METACLASS_$_SUSUISoftwareUpdateUnableToInstallAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateVerificationFailedAlertItem
- _OBJC_METACLASS_$_SUSUISoftwareUpdateVerifyingUpdateAlertItem
- _kSUSUISoftwareUpdateSettingsURL
CStrings:
+ "-[SUSUIAlertModel _initialInstallAlertFlowFromDownload]"
+ "-[SUSUIController _needsToWaitForHomescreenToAppear]"
+ "-[SUSUIController _showInstallAlertWithInstallOptions:]"
+ "-[SUSUIController _showInstallAlertWithInstallOptions:]_block_invoke"
+ "-[SUSUIController _showNextInstallAlertWithReasons:orScheduleIfNecessary:withInstallOptions:]"
+ "-[SUSUIController client:downloadDidFinish:withInstallPolicy:]"
+ "-[SUSUIController client:downloadDidFinish:withInstallPolicy:]_block_invoke"
+ "-[SUSUIController client:newOSBuildDetected:]"
+ "-[SUSUIController client:presentingRecommendedUpdate:shouldPresent:]"
+ "-[SUSUIController client:presentingRecommendedUpdate:shouldPresent:]_block_invoke"
+ "-[SUSUIController client:rollbackDidFail:withError:]"
+ "-[SUSUIController client:rollbackDidFinish:]"
+ "-[SUSUIController client:rollbackDidStart:]"
+ "-[SUSUIController client:rollbackReadyToStart:options:completion:]"
+ "-[SUSUIController client:rollbackSuggested:info:]"
+ "-[SUSUIController client:scheduledRollbackReadyForReboot:]"
+ "-[SUSUIController deviceBootedAfterSplatOnlyRollback:rollbackDescriptor:]"
+ "-[SUSUIController deviceBootedAfterSplatOnlyUpdate:]"
+ "-[SUSUIInstallAlertItem _notificationMessage]"
+ "-[SUSUIRollbackFailureAlertItem message]"
+ "220d35fc-bc97-422e-8c96-7ea2785548a1"
+ "55b4b4f0-0ecd-4a85-a72f-3e5e6feeac4d"
+ "5f33eae7-f1e0-4811-9713-07dd879f16d5"
+ "63efd5fa-738b-4560-913f-49a55bc873f4"
+ "71b10ce9-15df-40be-bfca-49113fff8fcc"
+ "@\"<SUSUIAlertModelDelegate>\""
+ "@\"SUSUIAlertModel\""
+ "@\"SUSUIBaseUpdateAlertItem\""
+ "@\"SUSUIController\""
+ "@\"SUSUIDefaults\""
+ "@\"SUSUIInstallOptions\""
+ "@\"SUSUIStatePersistence\""
+ "RSR_INSTALL_FAILURE_DONE_BUTTON"
+ "SOFTWARE_UPDATE_DOWNLOAD_FAILURE_ALERT_SUPPORT_FLOW"
+ "SUSUIAlertFlow"
+ "SUSUIAlertModel"
+ "SUSUIAlertModelDelegate"
+ "SUSUIAlertRepopDate"
+ "SUSUIAlertRepopStrategy"
+ "SUSUIAvailableAlertItem"
+ "SUSUIBaseInstallFailureAlertItem"
+ "SUSUIBaseUpdateAlertItem"
+ "SUSUIController"
+ "SUSUIController_Testing"
+ "SUSUIDownloadFailedAlertItem"
+ "SUSUIDownloadWasQueuedRemotely"
+ "SUSUIInstallAlertItem"
+ "SUSUIInstallAlertStyleAutoDownload"
+ "SUSUIInstallAlertStyleEnforcedCountdown"
+ "SUSUIInstallAlertStyleEnforcedNow"
+ "SUSUIInstallAlertStyleEnforcedReminder"
+ "SUSUIInstallAlertStyleInstallWithCountdown"
+ "SUSUIInstallAlertStyleInstallWithoutCountdown"
+ "SUSUIInstallAlertStyleNone"
+ "SUSUIInstallLaterAlertItem"
+ "SUSUIInstallOperationLifeCycleHandler"
+ "SUSUIInstallOptions"
+ "SUSUIRebootingAlertItem"
+ "SUSUIRecommendedAlertItem"
+ "SUSUIRollbackFailureAlertItem"
+ "SUSUIStateAlertAutoUpdateRetryCount"
+ "SUSUIStateAlertRemindMeLaterCount"
+ "SUSUIStateAlertRemindMeLaterCountSinceRequiringInstallation"
+ "SUSUIStateInstallPolicyKey"
+ "SUSUIStatePersistence"
+ "SUSUIUnableToInstallAlertItem"
+ "SUSUIVerificationFailedAlertItem"
+ "SUSUIVerifyingUpdateAlertItem"
+ "T@\"<SUSUIAlertModelDelegate>\",W,N,V_delegate"
+ "T@\"SUSUIController\",R,N,V_controller"
+ "[SUSUIController] Compute default re-alert date consulting remind me later count (%ld) from policy [%{public}@] (skips allowed: %lu, delaying realert for %ld days) to determine if we need to adjust to one week later than computed time - adjusted time: %{public}@"
+ "[SUSUIController] Duet prediction -4 hours (%{public}@) is before start date (%{public}@) or nil.  Correcting to use hardcoded 8:00 PM on or after the start date."
+ "[SUSUIController] Duet predicts the next last unlock date from %{public}@ is %{public}@"
+ "[SUSUIController] Duet predicts the next last unlock date from now is %{public}@"
+ "[SUSUIController] Final date computed: %{public}@"
+ "[SUSUIController] nextLastPredictedUnlockDateMinus4Hours date computed: %{public}@, adding jitter of %d minutes and %d seconds"
+ "activateSupportFlow"
+ "b9e3c9f6-a252-481e-a9ab-0bd3beeae429"
+ "c1b5ebc2-72ff-44a5-a761-50502d26fc66"
+ "containsAnyCollections:"
+ "demo-external"
+ "demo-internal"
+ "fc098402-04dd-45c5-86f8-50e36d846af1"
+ "sandboxExtensionShortTermLocksKey"
+ "sandboxExtensionShortTermLocksPathKey"
+ "shouldDisplayStepByStepHelpOption"
+ "softwareUpdate"
+ "supportflow://?type=softwareUpdate&referrer=com.apple.SoftwareUpdateServicesUI"
+ "v40@0:8@\"SUSUIAlertModel\"16Q24Q32"
- "-[SUSUISoftwareUpdateAlertModel _initialInstallAlertFlowFromDownload]"
- "-[SUSUISoftwareUpdateController _needsToWaitForHomescreenToAppear]"
- "-[SUSUISoftwareUpdateController _showInstallAlertWithInstallOptions:]"
- "-[SUSUISoftwareUpdateController _showInstallAlertWithInstallOptions:]_block_invoke"
- "-[SUSUISoftwareUpdateController _showNextInstallAlertWithReasons:orScheduleIfNecessary:withInstallOptions:]"
- "-[SUSUISoftwareUpdateController client:downloadDidFinish:withInstallPolicy:]"
- "-[SUSUISoftwareUpdateController client:downloadDidFinish:withInstallPolicy:]_block_invoke"
- "-[SUSUISoftwareUpdateController client:newOSBuildDetected:]"
- "-[SUSUISoftwareUpdateController client:presentingRecommendedUpdate:shouldPresent:]"
- "-[SUSUISoftwareUpdateController client:presentingRecommendedUpdate:shouldPresent:]_block_invoke"
- "-[SUSUISoftwareUpdateController client:rollbackDidFail:withError:]"
- "-[SUSUISoftwareUpdateController client:rollbackDidFinish:]"
- "-[SUSUISoftwareUpdateController client:rollbackDidStart:]"
- "-[SUSUISoftwareUpdateController client:rollbackReadyToStart:options:completion:]"
- "-[SUSUISoftwareUpdateController client:rollbackSuggested:info:]"
- "-[SUSUISoftwareUpdateController client:scheduledRollbackReadyForReboot:]"
- "-[SUSUISoftwareUpdateController deviceBootedAfterSplatOnlyRollback:rollbackDescriptor:]"
- "-[SUSUISoftwareUpdateController deviceBootedAfterSplatOnlyUpdate:]"
- "-[SUSUISoftwareUpdateInstallAlertItem _notificationMessage]"
- "-[SUSUISoftwareUpdateRollbackFailureAlertItem message]"
- "245326d2-3ddb-4c46-a08e-aab8b6060a1b"
- "85ff7a90-361b-42d1-a420-97dee860f018"
- "97d68e5c-95bb-4136-9aa0-f08964fcc0e1"
- "@\"<SUSUISoftwareUpdateAlertModelDelegate>\""
- "@\"SUSUIBaseSoftwareUpdateAlertItem\""
- "@\"SUSUISoftwareUpdateAlertModel\""
- "@\"SUSUISoftwareUpdateController\""
- "@\"SUSUISoftwareUpdateDefaults\""
- "@\"SUSUISoftwareUpdateInstallOptions\""
- "@\"SUSUISoftwareUpdateStatePersistence\""
- "Post-update controller not ready, queuing splat update notification"
- "SUSUIBaseSoftwareUpdateAlertItem"
- "SUSUIBaseSoftwareUpdateInstallFailureAlertItem"
- "SUSUISoftwareUpdateAlertFlow"
- "SUSUISoftwareUpdateAlertModel"
- "SUSUISoftwareUpdateAlertModelDelegate"
- "SUSUISoftwareUpdateAlertRepopDate"
- "SUSUISoftwareUpdateAlertRepopStrategy"
- "SUSUISoftwareUpdateAvailableAlertItem"
- "SUSUISoftwareUpdateController"
- "SUSUISoftwareUpdateController_Testing"
- "SUSUISoftwareUpdateDownloadFailedAlertItem"
- "SUSUISoftwareUpdateDownloadWasQueuedRemotely"
- "SUSUISoftwareUpdateInstallAlertItem"
- "SUSUISoftwareUpdateInstallAlertStyleAutoDownload"
- "SUSUISoftwareUpdateInstallAlertStyleEnforcedCountdown"
- "SUSUISoftwareUpdateInstallAlertStyleEnforcedNow"
- "SUSUISoftwareUpdateInstallAlertStyleEnforcedReminder"
- "SUSUISoftwareUpdateInstallAlertStyleInstallWithCountdown"
- "SUSUISoftwareUpdateInstallAlertStyleInstallWithoutCountdown"
- "SUSUISoftwareUpdateInstallAlertStyleNone"
- "SUSUISoftwareUpdateInstallLaterAlertItem"
- "SUSUISoftwareUpdateInstallOperationLifeCycleHandler"
- "SUSUISoftwareUpdateInstallOptions"
- "SUSUISoftwareUpdateRebootingAlertItem"
- "SUSUISoftwareUpdateRecommendedAvailableAlertItem"
- "SUSUISoftwareUpdateRollbackFailureAlertItem"
- "SUSUISoftwareUpdateStateAlertAutoUpdateRetryCount"
- "SUSUISoftwareUpdateStateAlertRemindMeLaterCount"
- "SUSUISoftwareUpdateStateAlertRemindMeLaterCountSinceRequiringInstallation"
- "SUSUISoftwareUpdateStateInstallPolicyKey"
- "SUSUISoftwareUpdateStatePersistence"
- "SUSUISoftwareUpdateUnableToInstallAlertItem"
- "SUSUISoftwareUpdateVerificationFailedAlertItem"
- "SUSUISoftwareUpdateVerifyingUpdateAlertItem"
- "T@\"<SUSUISoftwareUpdateAlertModelDelegate>\",W,N,V_delegate"
- "T@\"SUSUISoftwareUpdateController\",R,N,V_controller"
- "[SUSUISoftwareUpdateController] Compute default re-alert date consulting remind me later count (%ld) from policy [%{public}@] (skips allowed: %lu, delaying realert for %ld days) to determine if we need to adjust to one week later than computed time - adjusted time: %{public}@"
- "[SUSUISoftwareUpdateController] Duet prediction -4 hours (%{public}@) is before start date (%{public}@) or nil.  Correcting to use hardcoded 8:00 PM on or after the start date."
- "[SUSUISoftwareUpdateController] Duet predicts the next last unlock date from %{public}@ is %{public}@"
- "[SUSUISoftwareUpdateController] Duet predicts the next last unlock date from now is %{public}@"
- "[SUSUISoftwareUpdateController] Final date computed: %{public}@"
- "[SUSUISoftwareUpdateController] nextLastPredictedUnlockDateMinus4Hours date computed: %{public}@, adding jitter of %d minutes and %d seconds"
- "ed5a1c1d-2a39-4993-8bcc-f260c4b42868"
- "fb333b76-b463-401f-8899-96d82fc4c598"
- "v40@0:8@\"SUSUISoftwareUpdateAlertModel\"16Q24Q32"

```
