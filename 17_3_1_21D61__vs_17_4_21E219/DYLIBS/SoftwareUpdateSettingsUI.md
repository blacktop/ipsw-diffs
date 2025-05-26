## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-231.80.1.0.0
-  __TEXT.__text: 0x8e3c0
+255.100.5.0.0
+  __TEXT.__text: 0x94514
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x2244
-  __TEXT.__cstring: 0x4fd9
-  __TEXT.__oslogstring: 0xb484
-  __TEXT.__gcc_except_tab: 0xa14
+  __TEXT.__objc_methlist: 0x2234
+  __TEXT.__cstring: 0x512a
+  __TEXT.__oslogstring: 0xb8ab
+  __TEXT.__gcc_except_tab: 0xa9c
   __TEXT.__const: 0x60
   __TEXT.__dlopen_cstrs: 0x1a8
-  __TEXT.__unwind_info: 0x8b4
+  __TEXT.__unwind_info: 0x8d4
   __TEXT.__eh_frame: 0x23c
   __TEXT.__objc_classname: 0x499
-  __TEXT.__objc_methname: 0x90ae
-  __TEXT.__objc_methtype: 0x21a8
+  __TEXT.__objc_methname: 0x90a0
+  __TEXT.__objc_methtype: 0x2197
   __TEXT.__objc_stubs: 0x6e60
   __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x3ef8
+  __DATA_CONST.__const: 0x4438
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4720
   __DATA_CONST.__objc_selrefs: 0x2050
-  __AUTH_CONST.__cfstring: 0x2d00
+  __DATA_CONST.__objc_classrefs: 0x320
+  __DATA_CONST.__objc_superrefs: 0x88
+  __AUTH_CONST.__cfstring: 0x2ea0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_const: 0x6b0
   __AUTH_CONST.__objc_intobj: 0xc0

   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x288
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_classrefs: 0x320
-  __DATA.__objc_superrefs: 0x88
   __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x710
   __DATA.__bss: 0x100

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1072
-  Symbols:   5392
-  CStrings:  2408
+  Functions: 1074
+  Symbols:   5564
+  CStrings:  2423
 
Symbols:
+ -[SUSUISoftwareUpdateClientManager isUpdateReadyForInstallationWithOptions:completion:]
+ -[SUSUISoftwareUpdateManager scanFinishedWithUpdates:options:andError:]
+ GCC_except_table175
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table201
+ GCC_except_table301
+ GCC_except_table303
+ GCC_except_table305
+ GCC_except_table307
+ GCC_except_table312
+ GCC_except_table314
+ GCC_except_table39
+ GCC_except_table81
+ GCC_except_table9
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_ATOMIC_INSTANCE
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_BASE_LOCATION
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_DIRECTORY
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_EXTENSION
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_LATEST
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_SPECIFIC
+ _MA_PALLAS_AUDIENCE_EXTERNAL_PRE_RELEASE
+ _MA_SANDBOX_EXTENSION_PATH_KEY
+ ___42-[SUSUISoftwareUpdateManager refreshState]_block_invoke.383
+ ___45-[SUSUISoftwareUpdateManager setAutoInstall:]_block_invoke.420
+ ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.422
+ ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.423
+ ___56-[SUSUISoftwareUpdateController(UI) willEnterForeground]_block_invoke
+ ___60-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:]_block_invoke.724
+ ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.333
+ ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.340
+ ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.344
+ ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.345
+ ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.346
+ ___64-[SUSUISoftwareUpdateManager unenrollBetaUpdatesWithCompletion:]_block_invoke.726
+ ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.352
+ ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke.735
+ ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke_2.736
+ ___69-[SUSUISoftwareUpdateClientManager initWithDelegate:completionQueue:]_block_invoke.238
+ ___69-[SUSUISoftwareUpdateClientManager initWithDelegate:completionQueue:]_block_invoke.240
+ ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.712
+ ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.713
+ ___71-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:options:andError:]_block_invoke
+ ___71-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:options:andError:]_block_invoke.720
+ ___71-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:options:andError:]_block_invoke_2
+ ___73-[SUSUISoftwareUpdateManager _alertForDownloadConstraintsWithCompletion:]_block_invoke.697
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.414
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.415
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.417
+ ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.709
+ ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.710
+ ___76-[SUSUISoftwareUpdateManager cancelOrPurgeIfNecessaryWithUpdate:completion:]_block_invoke.707
+ ___82-[SUSUISoftwareUpdateManager _setState:preferredUpdateError:alternateUpdateError:]_block_invoke.372
+ ___87-[SUSUISoftwareUpdateClientManager isUpdateReadyForInstallationWithOptions:completion:]_block_invoke
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.403
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.404
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.407
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke_2
+ ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.670
+ ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.673
+ ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"SUScanResults"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e20_v20?0B8"NSError"12ls32l8w56l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e32_v24?0"SUDownload"8"NSError"16ls32l8w64l8s40l8s48l8s56l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs88w_e5_v8?0lw88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.324
+ ___block_literal_global.464
+ ___block_literal_global.651
+ ___os_log_helper_16_2_15_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66
+ ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_4_0
+ ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0
+ ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_64
+ ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_66
+ ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_4_0_4_0
+ ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_4_0_8_64
+ ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_4_0_8_66
+ ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_0
+ ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_64_4_0
+ ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_64_8_64
+ ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_66_4_0
+ ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_66_8_66
+ ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_4_0_8_0_8_64
+ ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_4_0_8_64
+ ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_0_8_66
+ ___os_log_helper_16_2_19_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_4_0_8_66_4_0_8_66
+ ___os_log_helper_16_2_19_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_64_4_0_8_66_4_0
+ ___os_log_helper_16_2_19_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_64_8_0_8_64_8_0
+ ___os_log_helper_16_2_19_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_66_4_0_8_66_4_0
+ ___os_log_helper_16_2_19_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_66_4_0_8_66_8_66
+ ___os_log_helper_16_2_19_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_64
+ ___os_log_helper_16_2_19_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_66
+ ___os_log_helper_16_2_21_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_0_8_66_8_66_4_0_8_66_4_0_8_66_8_66
+ _objc_msgSend$clientName
+ _objc_msgSend$isUpdateReadyForInstallationWithOptions:completion:
+ _objc_msgSend$scanFinishedWithUpdates:options:andError:
- -[SUSUISoftwareUpdateClientManager isUpdateReadyForInstallationWithOpions:completion:]
- -[SUSUISoftwareUpdateController(SoftwareUpdate) downloadAndInstallFinishedWithResult:andError:forInstallType:]
- -[SUSUISoftwareUpdateManager scanFinishedWithUpdates:error:]
- GCC_except_table12
- GCC_except_table172
- GCC_except_table183
- GCC_except_table184
- GCC_except_table195
- GCC_except_table295
- GCC_except_table300
- GCC_except_table302
- GCC_except_table304
- GCC_except_table306
- GCC_except_table311
- GCC_except_table42
- GCC_except_table8
- ___110-[SUSUISoftwareUpdateController(SoftwareUpdate) downloadAndInstallFinishedWithResult:andError:forInstallType:]_block_invoke
- ___42-[SUSUISoftwareUpdateManager refreshState]_block_invoke.359
- ___45-[SUSUISoftwareUpdateManager setAutoInstall:]_block_invoke.389
- ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.391
- ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.392
- ___60-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:]_block_invoke.687
- ___60-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:error:]_block_invoke
- ___60-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:error:]_block_invoke.683
- ___60-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:error:]_block_invoke_2
- ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.309
- ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.316
- ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.320
- ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.321
- ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.322
- ___64-[SUSUISoftwareUpdateManager unenrollBetaUpdatesWithCompletion:]_block_invoke.689
- ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.328
- ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke.698
- ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke_2.699
- ___69-[SUSUISoftwareUpdateClientManager initWithDelegate:completionQueue:]_block_invoke.214
- ___69-[SUSUISoftwareUpdateClientManager initWithDelegate:completionQueue:]_block_invoke.216
- ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.675
- ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.676
- ___73-[SUSUISoftwareUpdateManager _alertForDownloadConstraintsWithCompletion:]_block_invoke.660
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.383
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.384
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.386
- ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.672
- ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.673
- ___76-[SUSUISoftwareUpdateManager cancelOrPurgeIfNecessaryWithUpdate:completion:]_block_invoke.670
- ___82-[SUSUISoftwareUpdateManager _setState:preferredUpdateError:alternateUpdateError:]_block_invoke.348
- ___86-[SUSUISoftwareUpdateClientManager isUpdateReadyForInstallationWithOpions:completion:]_block_invoke
- ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.379
- ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.382
- ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.633
- ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.636
- ___block_descriptor_40_e8_32w_e20_v20?0B8"NSError"12lw32l8
- ___block_descriptor_48_e8_32s40bs_e35_v24?0"SUScanResults"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56w_e20_v20?0B8"NSError"12ls32l8w56l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56bs64w_e32_v24?0"SUDownload"8"NSError"16ls32l8w64l8s40l8s48l8s56l8
- ___block_literal_global.300
- ___block_literal_global.433
- ___block_literal_global.627
- ___os_log_helper_16_2_14_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66
- ___os_log_helper_16_2_15_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_4_0
- ___os_log_helper_16_2_15_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_0
- ___os_log_helper_16_2_15_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_64
- ___os_log_helper_16_2_15_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_66
- ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_4_0_4_0
- ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_4_0_8_64
- ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_4_0_8_66
- ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_0_8_0
- ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_64_4_0
- ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_64_8_64
- ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_66_4_0
- ___os_log_helper_16_2_16_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_66_8_66
- ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_4_0_8_0_8_64
- ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_0_4_0_8_64
- ___os_log_helper_16_2_17_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_0_8_0_8_66
- ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_4_0_8_66_4_0_8_66
- ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_64_4_0_8_66_4_0
- ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_64_8_0_8_64_8_0
- ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_66_4_0_8_66_4_0
- ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_66_4_0_8_66_8_66
- ___os_log_helper_16_2_18_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_66
- ___os_log_helper_16_2_20_8_32_8_66_4_0_8_66_8_0_8_66_8_66_8_0_8_66_8_0_8_0_8_66_8_0_8_66_8_66_4_0_8_66_4_0_8_66_8_66
- _objc_msgSend$downloadAndInstallFinishedWithResult:andError:forInstallType:
- _objc_msgSend$isUpdateReadyForInstallationWithOpions:completion:
- _objc_msgSend$scanFinishedWithUpdates:error:
CStrings:
+ "%s: Attempts to schedule the download for auto-installation"
+ "%s: Called while _anyScanInProgress = NO. Stopping."
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\n"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\n%@ setup auto install error: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nAccepted TOS for update %p: %d, error: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nAssigning new state: %{public}@ (%d) -> %{public}@ (%d). preferredUpdateError: %{public}@, alternateUpdateError: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nAuto-update scheduled: %d, operation: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nBattery level changed: %f -> %f"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nBattery state changed: %d -> %d"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nBypassing TOS because bypassTermsAndConditions=YES"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nChanged network type: %@ (%d) -> %{public}@ (%d)"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nCompleted beta program scan."
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nDownload failed with error: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nEnroll in program: %@, error: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nError: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nFinished to download: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nHandle rollback already applied"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nNew scan results: %p"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nNot scanning for beta programs because this is buddy."
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nRapid Security Response - Skipping SU Terms presentation"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nSU Terms: Agreement status %i"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nScan error: %@; state: %d"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nSkipping setting state due to initial scan. _state: %{public}@ (%d), new state: %{public}@ (%d)"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nSkipping setting state due to same error. _state: %{public}@ (%d), preferredError: %{public}@ alternateError: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nStarting the download and install of '%{public}@'. cellularFeeAcceptance: %d"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nStarting to download: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nUn-enroll from beta program success: %d"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nUpdate: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nUpdate: %@, error: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nUpdating _clearingSpaceForDownload to %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\naccepted: %d, error: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nclearing: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\ndownload fetched the initiated download object - download: %{public}@, downloadError: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\ndownload: %p (owner SUDescriptor: %p), error: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nerror: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\ninstallationType: %@ (%lu), update: %@ (%p)"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nis user-initiated rescan: %d"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisDelaying: %d; pathRestriction: %lu, error: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisKeybagRequired: %d"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisReady: %d; error: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisRollingBack: %@; rollback: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisScanning: %d; error: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\noperationProgress: %@; download done: %d"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\noptions: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\npreferredDownloadable: %d, preferredError: %{public}@, alternateDownloadable: %d, alternateError: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nscanId: %{public}@ (client: %{public}@), error: %{public}@; SUScanResults: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nstartDownloadWithOptions - successfullyStarted: %d; error: %{public}@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nsuccess: %d, passcodeError: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nsuccess; %d, passcodeError: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\ntermsAccepted: %d, termsError: %@"
+ "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p (%{public}@)\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nupdate: %{public}@, error: %{public}@, download: %{public}@, downloadError: %{public}@"
+ "-[SUSUISoftwareUpdateController(UI) willEnterForeground]_block_invoke"
+ "-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke_3"
+ "-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:options:andError:]"
+ "/private/var/MobileAsset/AssetsV2/locks"
+ "0206c249-b301-46e0-9d6a-23ce9c5d875d"
+ "AUTOMATIC_DOWNLOAD_SWITCH_SPECIFIER"
+ "AUTOMATIC_INSTALL_SWITCH_SPECIFIER"
+ "AUTOMATIC_INSTALL_SYSTEM_DATA_FILES_SWITCH_SPECIFIER"
+ "DRIVING_INSTALL_ERROR"
+ "RSR_DRIVING_INSTALL_ERROR"
+ "T@\"NSString\",?,R,C"
+ "Unable to Update"
+ "atomic_instance"
+ "clientName"
+ "isUpdateReadyForInstallationWithOptions:completion:"
+ "latest"
+ "locker"
+ "sandboxExtensionPathKey"
+ "scanFinishedWithUpdates:options:andError:"
+ "shared_locks"
+ "specific"
- "%@ setup auto install error: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\n"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nAccepted TOS for update %p: %d, error: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nAssigning new state: %{public}@ (%d) -> %{public}@ (%d). preferredUpdateError: %{public}@, alternateUpdateError: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nAuto-update scheduled: %d, operation: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nBattery level changed: %f -> %f"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nBattery state changed: %d -> %d"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nBypassing TOS because bypassTermsAndConditions=YES"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nChanged network type: %@ (%d) -> %{public}@ (%d)"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nCompleted beta program scan."
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nDownload failed with error: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nEnroll in program: %@, error: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nError: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nFinished to download: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nHandle rollback already applied"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nNew scan results: %p"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nNot scanning for beta programs because this is buddy."
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nRapid Security Response - Skipping SU Terms presentation"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nSU Terms: Agreement status %i"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nScan error: %@; state: %d"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nSkipping setting state due to initial scan. _state: %{public}@ (%d), new state: %{public}@ (%d)"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nSkipping setting state due to same error. _state: %{public}@ (%d), preferredError: %{public}@ alternateError: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nStarting the download and install of '%{public}@'. cellularFeeAcceptance: %d"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nStarting to download: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nUn-enroll from beta program success: %d"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nUpdate: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nUpdate: %@, error: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nUpdating _clearingSpaceForDownload to %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\naccepted: %d, error: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nclearing: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\ndownload fetched the initiated download object - download: %{public}@, downloadError: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\ndownload: %p (owner SUDescriptor: %p), error: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nerror: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nerror: %@; SUScanResults: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\ninstallationType: %@ (%lu), update: %@ (%p)"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nis user-initiated rescan: %d"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisDelaying: %d; pathRestriction: %lu, error: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisKeybagRequired: %d"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisReady: %d; error: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisRollingBack: %@; rollback: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nisScanning: %d; error: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\noperationProgress: %@; download done: %d"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\noptions: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\npreferredDownloadable: %d, preferredError: %{public}@, alternateDownloadable: %d, alternateError: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nstartDownloadWithOptions - successfullyStarted: %d; error: %{public}@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nsuccess: %d, passcodeError: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nsuccess; %d, passcodeError: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\ntermsAccepted: %d, termsError: %@"
- "%s: Update Manager Checkpoint\n\tstate: %{public}@ (%d)\n\tpreferredUpdate: %{public}@ (%p)\n\tpreferredUpdateError: %{public}@\n\talternateUpdate: %{public}@ (%p)\n\talternateUpdateError: %{public}@\n\tdownload: %p\n\tdelegate: %p (%{public}@)\n\thostController: %p (%{public}@)\n\nupdate: %{public}@, error: %{public}@, download: %{public}@, downloadError: %{public}@"
- "-[SUSUISoftwareUpdateController(SoftwareUpdate) downloadAndInstallFinishedWithResult:andError:forInstallType:]"
- "-[SUSUISoftwareUpdateController(UI) willEnterForeground]"
- "-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:error:]"
- "Unable to Update at This Time"
- "downloadAndInstallFinishedWithResult:andError:forInstallType:"
- "isUpdateReadyForInstallationWithOpions:completion:"
- "scanFinishedWithUpdates:error:"
- "v36@0:8B16@20Q28"

```
