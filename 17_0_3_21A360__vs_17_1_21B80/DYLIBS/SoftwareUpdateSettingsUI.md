## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-218.2.2.0.0
-  __TEXT.__text: 0x83a08
+231.40.7.0.0
+  __TEXT.__text: 0x8c68c
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x21f4
-  __TEXT.__cstring: 0x4c23
-  __TEXT.__oslogstring: 0xa869
-  __TEXT.__gcc_except_tab: 0x790
-  __TEXT.__const: 0x58
+  __TEXT.__objc_methlist: 0x2244
+  __TEXT.__cstring: 0x4e01
+  __TEXT.__oslogstring: 0xab4b
+  __TEXT.__gcc_except_tab: 0x998
+  __TEXT.__const: 0x60
   __TEXT.__dlopen_cstrs: 0x1a8
-  __TEXT.__unwind_info: 0x878
-  __TEXT.__eh_frame: 0x128
-  __TEXT.__objc_classname: 0x49a
-  __TEXT.__objc_methname: 0x9060
-  __TEXT.__objc_methtype: 0x2122
-  __TEXT.__objc_stubs: 0x6dc0
+  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__eh_frame: 0x23c
+  __TEXT.__objc_classname: 0x499
+  __TEXT.__objc_methname: 0x907c
+  __TEXT.__objc_methtype: 0x21a8
+  __TEXT.__objc_stubs: 0x6e00
   __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x3cc0
+  __DATA_CONST.__const: 0x3d00
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4748
-  __DATA_CONST.__objc_selrefs: 0x2018
-  __AUTH_CONST.__cfstring: 0x2cc0
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__objc_const: 0x668
+  __DATA_CONST.__objc_const: 0x4720
+  __DATA_CONST.__objc_selrefs: 0x2038
+  __AUTH_CONST.__cfstring: 0x2c80
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__objc_const: 0x6b0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x288
   __AUTH.__objc_data: 0x550
   __DATA.__objc_classrefs: 0x320
   __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x1b4
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x710
   __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3687754C-4C4C-36F0-A3CB-DB03EAB9A350
-  Functions: 1060
-  Symbols:   5305
-  CStrings:  2732
+  UUID: CD423552-6F22-3053-A111-A1C054916D8A
+  Functions: 1067
+  Symbols:   5316
+  CStrings:  2742
 
Symbols:
+ +[SUSUISoftwareUpdateManager timeRemainingForProgress:isValid:]
+ -[SUSUISoftwareUpdateClientManager client:clearingSpaceForDownload:clearingSpace:]
+ -[SUSUISoftwareUpdateClientManager client:handleUIForDDMDeclaration:]
+ -[SUSUISoftwareUpdateController(SoftwareUpdate) manager:handleDDMDeclaration:]
+ -[SUSUISoftwareUpdateManager actionStringForBuddy]
+ -[SUSUISoftwareUpdateManager manager:handleDDMDeclaration:]
+ -[SUSUISoftwareUpdateManager statusStringForBuddy]
+ -[SUSUISoftwareUpdateManager timeRemainingStringForProgress:]
+ -[SUSUISoftwareUpdateSlowRollController startDownloadAndInstallOnMainPaneWithCompletionHandler:]
+ GCC_except_table114
+ GCC_except_table119
+ GCC_except_table172
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table194
+ GCC_except_table197
+ GCC_except_table297
+ GCC_except_table299
+ GCC_except_table30
+ GCC_except_table301
+ GCC_except_table308
+ GCC_except_table31
+ GCC_except_table310
+ GCC_except_table42
+ GCC_except_table72
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table79
+ __OBJC_$_CLASS_METHODS_SUSUISoftwareUpdateManager
+ ___42-[SUSUISoftwareUpdateManager refreshState]_block_invoke.359
+ ___45-[SUSUISoftwareUpdateManager setAutoInstall:]_block_invoke.389
+ ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.391
+ ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.392
+ ___60-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:]_block_invoke.687
+ ___60-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:error:]_block_invoke.683
+ ___64-[SUSUISoftwareUpdateManager unenrollBetaUpdatesWithCompletion:]_block_invoke.689
+ ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke.698
+ ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke_2.699
+ ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.675
+ ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.676
+ ___73-[SUSUISoftwareUpdateManager _alertForDownloadConstraintsWithCompletion:]_block_invoke.660
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.383
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.384
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.386
+ ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.672
+ ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.673
+ ___76-[SUSUISoftwareUpdateManager cancelOrPurgeIfNecessaryWithUpdate:completion:]_block_invoke.670
+ ___82-[SUSUISoftwareUpdateManager _setState:preferredUpdateError:alternateUpdateError:]_block_invoke.348
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.379
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.382
+ ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.633
+ ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.636
+ ___96-[SUSUISoftwareUpdateSlowRollController startDownloadAndInstallOnMainPaneWithCompletionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_literal_global.300
+ ___block_literal_global.433
+ ___block_literal_global.630
+ ___os_log_helper_16_2_25_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34
+ ___os_log_helper_16_2_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_0
+ ___os_log_helper_16_2_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64
+ ___os_log_helper_16_2_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_66
+ ___os_log_helper_16_2_27_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_0_8_0
+ ___os_log_helper_16_2_27_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_4_0
+ ___os_log_helper_16_2_27_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_8_0
+ ___os_log_helper_16_2_27_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_8_64
+ ___os_log_helper_16_2_29_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_4_0_8_64_8_64_8_0
+ ___os_log_helper_16_2_2_8_34_4_0
+ ___os_log_helper_16_2_30_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_4_0_8_64_8_64_8_0_8_64
+ ___os_log_helper_16_2_31_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_4_0_8_64_4_0_8_64_4_0
+ ___os_log_helper_16_3_27_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_0_8_65
+ ___os_log_helper_16_3_27_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_8_65
+ _objc_msgSend$actionStringForBuddy
+ _objc_msgSend$detailsURL
+ _objc_msgSend$manager:clearingSpaceForDownload:clearingSpace:
+ _objc_msgSend$manager:handleDDMDeclaration:
+ _objc_msgSend$startDownloadAndInstallOnMainPaneWithCompletionHandler:
+ _objc_msgSend$statusStringForBuddy
- -[SUSUISoftwareUpdateController timeRemainingForProgress:isValid:]
- -[SUSUISoftwareUpdateController(Specifiers) _deferredUpdateCellSpecifierForState:]
- -[SUSUISoftwareUpdateController(Specifiers) _deferredUpdateGroupSpecifierForState:]
- GCC_except_table116
- GCC_except_table123
- GCC_except_table168
- GCC_except_table179
- GCC_except_table180
- GCC_except_table190
- GCC_except_table193
- GCC_except_table29
- GCC_except_table290
- GCC_except_table292
- GCC_except_table296
- GCC_except_table298
- GCC_except_table300
- GCC_except_table32
- GCC_except_table41
- GCC_except_table68
- GCC_except_table70
- GCC_except_table73
- _OBJC_IVAR_$_SUSUISoftwareUpdateController._deferredUpdateCell
- _SUSUISpecifierDeferredUpdateCell
- _SUSUISpecifierDeferredUpdateGroup
- ___42-[SUSUISoftwareUpdateManager refreshState]_block_invoke.312
- ___45-[SUSUISoftwareUpdateManager setAutoInstall:]_block_invoke.350
- ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.352
- ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.353
- ___59-[SUSUISoftwareUpdateController(UI) updatedSpecifiersArray]_block_invoke_21
- ___59-[SUSUISoftwareUpdateController(UI) updatedSpecifiersArray]_block_invoke_22
- ___60-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:]_block_invoke.649
- ___60-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:error:]_block_invoke.645
- ___64-[SUSUISoftwareUpdateManager unenrollBetaUpdatesWithCompletion:]_block_invoke.651
- ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke.660
- ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke_2.661
- ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.637
- ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.638
- ___73-[SUSUISoftwareUpdateManager _alertForDownloadConstraintsWithCompletion:]_block_invoke.622
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.344
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.345
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.347
- ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.634
- ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.635
- ___74-[SUSUISoftwareUpdateSlowRollController startDownloadAndInstallOnMainPane]_block_invoke
- ___76-[SUSUISoftwareUpdateManager cancelOrPurgeIfNecessaryWithUpdate:completion:]_block_invoke.632
- ___82-[SUSUISoftwareUpdateManager _setState:preferredUpdateError:alternateUpdateError:]_block_invoke.301
- ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.340
- ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.343
- ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.595
- ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.598
- ___block_descriptor_48_e8_32w_e20_v20?0B8"NSError"12lw32l8
- ___block_literal_global.306
- ___block_literal_global.394
- ___block_literal_global.636
- ___os_log_helper_16_2_24_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34
- ___os_log_helper_16_2_25_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_0
- ___os_log_helper_16_2_25_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64
- ___os_log_helper_16_2_25_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_66
- ___os_log_helper_16_2_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_0_8_0
- ___os_log_helper_16_2_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_4_0
- ___os_log_helper_16_2_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_8_0
- ___os_log_helper_16_2_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_8_64
- ___os_log_helper_16_2_28_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_4_0_8_64_8_64_8_0
- ___os_log_helper_16_2_29_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_4_0_8_64_8_64_8_0_8_64
- ___os_log_helper_16_2_30_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_4_0_8_64_4_0_8_64_4_0
- ___os_log_helper_16_3_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_0_8_65
- ___os_log_helper_16_3_26_8_32_8_66_8_0_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_34_8_34_8_0_8_0_8_66_4_0_8_66_8_0_8_66_8_0_8_66_8_34_8_34_8_64_8_65
- _objc_msgSend$_deferredUpdateCellSpecifierForState:
- _objc_msgSend$_deferredUpdateGroupSpecifierForState:
- _objc_msgSend$shouldShowDeferredUpdateGroupForState:
- _objc_msgSend$systemBlueColor
CStrings:
+ "\x05\x1f\x13"
+ "%s: %@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\n"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nAttempting to show the update pane with the Default Audience asset"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nCan't open the Automatic Updates pane as automatic updates are managed."
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nDismissing tip: %@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nNew size: [%f, %f]"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nNo deviceLAContextCompletion, going legacy"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nReceive Beta programs (length: %lu): %{private}@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nSelected specifier ID: %@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nSelected specifier is nil, return"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nShowing PIN sheet using specifier: %@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nSoftwareUpdatePane invoked via URL but no supported option passed in. Nothing to do here. Available options: ShowDefaultAudiencePane, PerformAction"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nSoftwareUpdatePane invoked via URL. Will attempt URL specific loading. dictionary is %{public}@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nState transition: %@ (%d) -> %@ (%d) (controller masked state: %@ (%d))"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTip button tapped"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@, animated: %d"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@, animated? %d"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@, context: %{private}@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@, customizationID: %lu"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nUnknown deep link update action %ld"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ndeviceLAContextCompletion:YES"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ndevicePasscodeCompletion:NO"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ndevicePasscodeCompletion:YES"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ndownload: %@, error: %@"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nfailed to create LAContext with passcode"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ninstallType: %@ (%lu)"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nsuccessfullyStarted: %d, error: %@, installType: %@ (%lu)"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p (%{public}@)\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nsuccessfullyStarted: %d, error: %@, update: %@, download: %p, downloadError: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nNot scanning for beta programs because this is buddy."
+ "%s: strongSelf is nil"
+ "%{public}s, clearing = %d"
+ "-[SUSUISoftwareUpdateClientManager client:clearingSpaceForDownload:clearingSpace:]"
+ "-[SUSUISoftwareUpdateClientManager client:handleUIForDDMDeclaration:]"
+ "-[SUSUISoftwareUpdateManager actionString]"
+ "-[SUSUISoftwareUpdateManager progressString]"
+ "-[SUSUISoftwareUpdateManager scanForBetaPrograms]"
+ "-[SUSUISoftwareUpdateSlowRollController startDownloadAndInstallOnMainPaneWithCompletionHandler:]"
+ "-[SUSUISoftwareUpdateSlowRollController startDownloadAndInstallOnMainPaneWithCompletionHandler:]_block_invoke"
+ "MANAGED_DEVICE_ENFORCED_UPDATE_BODY_WITH_DATE"
+ "MANAGED_DEVICE_ENFORCED_UPDATE_BODY_WITH_URL"
+ "OS_NAME"
+ "actionStringForBuddy"
+ "detailsURL"
+ "manager:handleDDMDeclaration:"
+ "startDownloadAndInstallOnMainPaneWithCompletionHandler:"
+ "statusStringForBuddy"
+ "v32@0:8@\"SUSUISoftwareUpdateClientManager\"16@\"SUCoreDDMDeclaration\"24"
+ "v32@0:8@\"SUSUISoftwareUpdateManager\"16@\"SUCoreDDMDeclaration\"24"
- "\x05\x1f\x01\x13"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\n"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nAttempting to show the update pane with the Default Audience asset"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nCan't open the Automatic Updates pane as automatic updates are managed."
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nDismissing tip: %@"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nNew size: [%f, %f]"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nNo deviceLAContextCompletion, going legacy"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nReceive Beta programs (length: %lu): %{private}@"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nSelected specifier ID: %@"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nSelected specifier is nil, return"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nShowing PIN sheet using specifier: %@"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nSoftwareUpdatePane invoked via URL but no supported option passed in. Nothing to do here. Available options: ShowDefaultAudiencePane, PerformAction"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nSoftwareUpdatePane invoked via URL. Will attempt URL specific loading. dictionary is %{public}@"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nState transition: %@ (%d) -> %@ (%d) (controller masked state: %@ (%d))"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTip button tapped"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@, animated: %d"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@, animated? %d"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@, context: %{private}@"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nTipKit content: %@, customizationID: %lu"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nUnknown deep link update action %ld"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ndeviceLAContextCompletion:YES"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ndevicePasscodeCompletion:NO"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ndevicePasscodeCompletion:YES"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ndownload: %@, error: %@"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nfailed to create LAContext with passcode"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\ninstallType: %@ (%lu)"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nsuccessfullyStarted: %d, error: %@, installType: %@ (%lu)"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager state: %{public}@ (%d)\n\tmanager preferredUpdate: %{public}@ (%p)\n\tmanager preferredUpdateError: %{public}@\n\tmanager alternateUpdate: %{public}@ (%p)\n\tmanager alternateUpdateError: %{public}@\n\tmanager isDelayingUpdates: %{public}s\n\tmanager automaticUpdateScheduled: %{public}s\n\tmanager delegate: %p\n\tmanager host: %p\n\tcontroller currentState: %{public}@ (%d)\n\tcontroller updateDescriptor: %{public}@ (%p)\n\tcontroller alternateUpdateDescriptor: %{public}@ (%p)\n\tcontroller suError: %{public}@\n\tcontroller hasAlternateUpdate: %{public}s\n\tcontroller downloadDescriptorPane: %{public}s\n\nsuccessfullyStarted: %d, error: %@, update: %@, download: %p, downloadError: %@"
- "MANAGED_DEVICE_DELAY_TITLE"
- "MANAGED_DEVICE_ENFORCED_UPDATE_TITLE"
- "SUDeferredUpdateCell"
- "SUDeferredUpdateGroup"
- "_deferredUpdateCell"
- "_deferredUpdateCellSpecifierForState:"
- "_deferredUpdateGroupSpecifierForState:"
- "info.circle"
- "systemBlueColor"

```
