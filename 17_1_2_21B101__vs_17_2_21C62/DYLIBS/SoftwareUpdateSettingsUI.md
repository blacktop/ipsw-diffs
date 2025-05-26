## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-231.40.7.0.0
-  __TEXT.__text: 0x8c68c
+231.60.16.0.0
+  __TEXT.__text: 0x8e3c0
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0x2244
-  __TEXT.__cstring: 0x4e01
-  __TEXT.__oslogstring: 0xab4b
-  __TEXT.__gcc_except_tab: 0x998
+  __TEXT.__cstring: 0x4fd9
+  __TEXT.__oslogstring: 0xb484
+  __TEXT.__gcc_except_tab: 0xa14
   __TEXT.__const: 0x60
   __TEXT.__dlopen_cstrs: 0x1a8
-  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__unwind_info: 0x8b4
   __TEXT.__eh_frame: 0x23c
   __TEXT.__objc_classname: 0x499
-  __TEXT.__objc_methname: 0x907c
+  __TEXT.__objc_methname: 0x90ae
   __TEXT.__objc_methtype: 0x21a8
-  __TEXT.__objc_stubs: 0x6e00
+  __TEXT.__objc_stubs: 0x6e60
   __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x3d00
+  __DATA_CONST.__const: 0x3ef8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4720
-  __DATA_CONST.__objc_selrefs: 0x2038
-  __AUTH_CONST.__cfstring: 0x2c80
+  __DATA_CONST.__objc_selrefs: 0x2050
+  __AUTH_CONST.__cfstring: 0x2d00
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_const: 0x6b0
   __AUTH_CONST.__objc_intobj: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1067
-  Symbols:   5316
-  CStrings:  2386
+  Functions: 1072
+  Symbols:   5392
+  CStrings:  2408
 
Symbols:
+ -[SUSUISoftwareUpdateController(BetaUpdates) betaUpdatesHasInstallationRestriction]
+ -[SUSUISoftwareUpdateController(UI) isBusy]
+ -[SUSUISoftwareUpdateController(UI) setBusyWithActivityStyle:]
+ GCC_except_table18
+ GCC_except_table195
+ GCC_except_table198
+ GCC_except_table24
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table300
+ GCC_except_table302
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table311
+ _MA_PALLAS_AUDIENCE_CUSTOMER_VISIONOS
+ _MA_PALLAS_AUDIENCE_CUSTOMER_VISIONOS_ALT
+ _MA_PALLAS_AUDIENCE_CUSTOMER_VISIONOS_GENERIC
+ _SUBetaUpdatesRestrictionToString
+ ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.328
+ ___block_literal_global.627
+ ___os_log_helper_16_2_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_32
+ ___os_log_helper_16_2_3_8_32_4_0_4_0
+ ___os_log_helper_16_2_3_8_32_8_64_4_0
+ ___os_log_helper_16_2_3_8_32_8_64_8_0
+ _objc_msgSend$activityIndicatorDisplayStyle
+ _objc_msgSend$betaUpdatesHasInstallationRestriction
+ _objc_msgSend$isBusy
+ _objc_msgSend$isLockdownModeEnabled
+ _objc_msgSend$setBusyWithActivityStyle:
+ _objc_msgSend$setSpecifiers:
- -[SUSUISoftwareUpdateController(BetaUpdates) betaUpdatesHasDeviceManagementRestriction]
- -[SUSUISoftwareUpdateController(UI) currentlyPerformsUpdateRefresh]
- -[SUSUISoftwareUpdateController(UI) setTermsLoading:]
- GCC_except_table17
- GCC_except_table194
- GCC_except_table197
- GCC_except_table23
- GCC_except_table294
- GCC_except_table297
- GCC_except_table299
- GCC_except_table301
- GCC_except_table303
- GCC_except_table305
- GCC_except_table308
- GCC_except_table310
- ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.325
- ___block_literal_global.630
- _objc_msgSend$betaUpdatesHasDeviceManagementRestriction
- _objc_msgSend$currentlyPerformsUpdateRefresh
- _objc_msgSend$setTermsLoading:
CStrings:
+ "%s: Beta program restriction type: %@ (%ld)"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nCurrent top view controller: %@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nNavigation controller attached? %s"
+ "%s: No navigation controller available. Skipping on popping out."
+ "%s: Popping the Slow roll view controller"
+ "%s: Skipping on popping up the Slow Roll view controller because it was already popped out. Current top view controller: %@, isMovingFromParentViewController? %d"
+ "%s: Un-mapped restriction %ld"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nis user-initiated rescan: %d"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\noptions: %{public}@"
+ "%s: _runningInitialScan: %d, _userInitiatedRescan: %d"
+ "-[SUSUISoftwareUpdateBetaUpdatesController setupProgramListSpecifiers]"
+ "-[SUSUISoftwareUpdateManager manager:scanRequestDidFinishForOptions:results:error:]"
+ "-[SUSUISoftwareUpdateManager rescanForUpdatesInBackgroundWithOptions:andCompletionHandler:]"
+ "-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke"
+ "BETA_UPDATES_LOCKDOWN_RESTRICTED"
+ "Hiding Apple ID row - device has installation restriction (%ld)."
+ "Lockdown"
+ "MDM"
+ "N/A (restriction: %ld)"
+ "NSString *const SUBetaUpdatesRestrictionToString(SUBetaUpdatesRestriction)"
+ "None"
+ "activityIndicatorDisplayStyle"
+ "betaUpdatesHasInstallationRestriction"
+ "isBusy"
+ "isLockdownModeEnabled"
+ "setBusyWithActivityStyle:"
+ "setSpecifiers:"
- "Hiding Apple ID row - device has management restriction."
- "OS_NAME"
- "betaUpdatesHasDeviceManagementRestriction"
- "currentlyPerformsUpdateRefresh"
- "setTermsLoading:"

```
