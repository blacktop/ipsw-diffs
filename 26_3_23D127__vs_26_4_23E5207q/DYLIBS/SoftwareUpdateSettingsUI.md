## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-508.80.83.0.0
-  __TEXT.__text: 0x108648
+508.100.172.0.0
+  __TEXT.__text: 0x10d820
   __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x4b08
-  __TEXT.__cstring: 0x9f39
-  __TEXT.__oslogstring: 0x15904
-  __TEXT.__gcc_except_tab: 0x4bb4
+  __TEXT.__objc_methlist: 0x4b48
+  __TEXT.__gcc_except_tab: 0x4f84
+  __TEXT.__cstring: 0x9f9e
+  __TEXT.__oslogstring: 0x16864
   __TEXT.__dlopen_cstrs: 0x658
   __TEXT.__const: 0xa2
   __TEXT.__swift5_typeref: 0xc3
   __TEXT.__swift5_capture: 0xd4
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x17a0
+  __TEXT.__unwind_info: 0x17c0
   __TEXT.__eh_frame: 0xf0
-  __TEXT.__objc_classname: 0x6cc
-  __TEXT.__objc_methname: 0xe4e0
-  __TEXT.__objc_methtype: 0x2453
-  __TEXT.__objc_stubs: 0x9720
-  __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__const: 0x9b00
+  __TEXT.__objc_classname: 0x6ce
+  __TEXT.__objc_methname: 0xe5c7
+  __TEXT.__objc_methtype: 0x247c
+  __TEXT.__objc_stubs: 0x97e0
+  __DATA_CONST.__got: 0x6e8
+  __DATA_CONST.__const: 0x9ed0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3138
+  __DATA_CONST.__objc_selrefs: 0x3168
   __DATA_CONST.__objc_superrefs: 0x100
   __AUTH_CONST.__auth_got: 0x4e0
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x4380
-  __AUTH_CONST.__objc_const: 0x8b80
+  __AUTH_CONST.__cfstring: 0x4400
+  __AUTH_CONST.__objc_const: 0x8bd8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xaf0
   __DATA.__objc_ivar: 0x45c
   __DATA.__data: 0x958
-  __DATA.__bss: 0x241
+  __DATA.__bss: 0x248
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
+  - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 18426940-A7FA-38A6-961D-4C17115B4545
-  Functions: 2105
-  Symbols:   10940
-  CStrings:  4239
+  UUID: 60B5050B-E045-31CA-9C1F-C1B4BDBB63F8
+  Functions: 2118
+  Symbols:   11091
+  CStrings:  4260
 
Symbols:
+ -[SUSettingsSUPreferencesManager enableRapidReturnToService]
+ -[SUSettingsSUPreferencesManager queue_setEnableRapidReturnToService:]
+ -[SUSettingsSUPreferencesManager setEnableRapidReturnToService:]
+ -[SUSettingsStatefulUIManager isRapidReturnToServiceMode]
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table183
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table199
+ GCC_except_table213
+ GCC_except_table304
+ GCC_except_table95
+ _INTERNAL_PALLAS_SERVER_URL_V2_AUTH
+ _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
+ _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_MDMConfiguration
+ __OBJC_$_CLASS_METHODS_SUSUISoftwareUpdateController(Analytics|AutomaticUpdates|BetaUpdates|SoftwareUpdate|Specifiers|StatefulUI|UI|SUSUISoftwareUpdateController)
+ __OBJC_$_INSTANCE_METHODS_SUSUISoftwareUpdateController(Analytics|AutomaticUpdates|BetaUpdates|SoftwareUpdate|Specifiers|StatefulUI|UI|SUSUISoftwareUpdateController)
+ __OBJC_CLASS_PROTOCOLS_$_SUSUISoftwareUpdateController(Analytics|AutomaticUpdates|BetaUpdates|SoftwareUpdate|Specifiers|StatefulUI|UI|SUSUISoftwareUpdateController)
+ ___103-[SUSUISoftwareUpdateController(UI) waitForScanCompletionWithTimeout:currentAttempt:completionHandler:]_block_invoke.446
+ ___103-[SUSUISoftwareUpdateController(UI) waitForScanCompletionWithTimeout:currentAttempt:completionHandler:]_block_invoke.449
+ ___103-[SUSUISoftwareUpdateController(UI) waitForScanCompletionWithTimeout:currentAttempt:completionHandler:]_block_invoke.450
+ ___103-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.392
+ ___103-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.394
+ ___103-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.393
+ ___103-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.397
+ ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.368
+ ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.370
+ ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.372
+ ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.369
+ ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.371
+ ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.375
+ ___104-[SUSettingsStatefulUIManager scheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.400
+ ___104-[SUSettingsStatefulUIManager scheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.401
+ ___104-[SUSettingsStatefulUIManager scheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.402
+ ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.379
+ ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.381
+ ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.383
+ ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.380
+ ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.382
+ ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.384
+ ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.385
+ ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.387
+ ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.389
+ ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.386
+ ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.388
+ ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.390
+ ___42-[SUSUISoftwareUpdateManager refreshState]_block_invoke.443
+ ___45-[SUSUISoftwareUpdateManager setAutoInstall:]_block_invoke.480
+ ___47-[SUSettingsStatefulUIManager performFullScan:]_block_invoke.454
+ ___50-[SUSettingsStatefulUIManager refreshBetaUpdates:]_block_invoke.426
+ ___53-[SUSettingsStatefulUIManager handleFullScanResults:]_block_invoke.458
+ ___53-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke.333
+ ___53-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke.334
+ ___53-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke.335
+ ___53-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke.336
+ ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.482
+ ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.483
+ ___55-[SUSettingsUpdateOperation action_AquireKeybag:error:]_block_invoke.339
+ ___55-[SUSettingsUpdateOperation action_AquireKeybag:error:]_block_invoke.340
+ ___57-[SUSettingsScanOperation action_QueryUpdatesInfo:error:]_block_invoke.340
+ ___57-[SUSettingsUpdateOperation action_ScheduleUpdate:error:]_block_invoke.359
+ ___58-[SUSettingsScanOperation action_ReportScanOutcome:error:]_block_invoke.349
+ ___60-[SUSettingsSUPreferencesManager enableRapidReturnToService]_block_invoke
+ ___61-[SUSettingsScanOperation action_QueryCurrentDownload:error:]_block_invoke.330
+ ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.391
+ ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.392
+ ___64-[SUSUISoftwareUpdateManager unenrollBetaUpdatesWithCompletion:]_block_invoke.792
+ ___64-[SUSettingsSUPreferencesManager setEnableRapidReturnToService:]_block_invoke
+ ___64-[SUSettingsScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.407
+ ___65-[SUSettingsStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.467
+ ___65-[SUSettingsUpdateOperation action_InitiateUpdateDownload:error:]_block_invoke.355
+ ___65-[SUSettingsUpdateOperation action_PresentTermsConditions:error:]_block_invoke.345
+ ___65-[SUSettingsUpdateOperation action_PresentTermsConditions:error:]_block_invoke.346
+ ___65-[SUSettingsUpdateOperation action_PresentTermsConditions:error:]_block_invoke.347
+ ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.422
+ ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.423
+ ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke.801
+ ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke_2.802
+ ___68-[SUSettingsScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.390
+ ___69-[SUSUISoftwareUpdateClientManager initWithDelegate:completionQueue:]_block_invoke.298
+ ___69-[SUSUISoftwareUpdateClientManager initWithDelegate:completionQueue:]_block_invoke.300
+ ___69-[SUSettingsStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.419
+ ___69-[SUSettingsUpdateOperation action_PresentDownloadConstraints:error:]_block_invoke.352
+ ___69-[SUSettingsUpdateOperation action_PresentDownloadConstraints:error:]_block_invoke.353
+ ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.778
+ ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.779
+ ___71-[SUSUISoftwareUpdateBetaUpdatesController presentAuthenticationDialog]_block_invoke.409
+ ___71-[SUSUISoftwareUpdateBetaUpdatesController presentAuthenticationDialog]_block_invoke.410
+ ___71-[SUSUISoftwareUpdateBetaUpdatesController presentAuthenticationDialog]_block_invoke.416
+ ___71-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:completion:]_block_invoke.790
+ ___71-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:options:andError:]_block_invoke.786
+ ___71-[SUSettingsScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.411
+ ___71-[SUSettingsScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.409
+ ___71-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke.363
+ ___71-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke.364
+ ___71-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke.365
+ ___71-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke.366
+ ___73-[SUSUISoftwareUpdateManager _alertForDownloadConstraintsWithCompletion:]_block_invoke.763
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.474
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.475
+ ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.477
+ ___73-[SUSettingsStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus]_block_invoke.406
+ ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.775
+ ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.776
+ ___74-[SUSettingsScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.388
+ ___75-[SUSettingsStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.456
+ ___76-[SUSUISoftwareUpdateAutomaticUpdateController(NeRD) displayNeRDAlertToUser]_block_invoke.313
+ ___76-[SUSUISoftwareUpdateManager cancelOrPurgeIfNecessaryWithUpdate:completion:]_block_invoke.773
+ ___76-[SUSettingsScanOperation refreshBetaProgramsWithOptions:completionHandler:]_block_invoke.382
+ ___78-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]_block_invoke.379
+ ___78-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]_block_invoke.382
+ ___78-[SUSettingsScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.400
+ ___78-[SUSettingsStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.463
+ ___82-[SUSUISoftwareUpdateManager _setState:preferredUpdateError:alternateUpdateError:]_block_invoke.432
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.463
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.464
+ ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.467
+ ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.736
+ ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.739
+ ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke.412
+ ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke.413
+ ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke.416
+ ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke_2.415
+ ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke_2.417
+ ___block_literal_global.383
+ ___block_literal_global.524
+ ___block_literal_global.721
+ _objc_msgSend$enableRapidReturnToService
+ _objc_msgSend$isRapidReturnToService
+ _objc_msgSend$isRapidReturnToServiceMode
+ _objc_msgSend$queue_setEnableRapidReturnToService:
+ _objc_msgSend$setEnableRapidReturnToService:
+ _objc_msgSend$setShouldShowComingSoonTip:
+ _swift_errorRelease
- GCC_except_table118
- GCC_except_table121
- GCC_except_table158
- GCC_except_table161
- GCC_except_table178
- GCC_except_table190
- GCC_except_table192
- GCC_except_table193
- GCC_except_table194
- GCC_except_table208
- GCC_except_table299
- GCC_except_table31
- __OBJC_$_CLASS_METHODS_SUSUISoftwareUpdateController(BetaUpdates|AutomaticUpdates|Analytics|StatefulUI|Specifiers|UI|SoftwareUpdate|SUSUISoftwareUpdateController)
- __OBJC_$_INSTANCE_METHODS_SUSUISoftwareUpdateController(BetaUpdates|AutomaticUpdates|Analytics|StatefulUI|Specifiers|UI|SoftwareUpdate|SUSUISoftwareUpdateController)
- __OBJC_CLASS_PROTOCOLS_$_SUSUISoftwareUpdateController(BetaUpdates|AutomaticUpdates|Analytics|StatefulUI|Specifiers|UI|SoftwareUpdate|SUSUISoftwareUpdateController)
- ___103-[SUSUISoftwareUpdateController(UI) waitForScanCompletionWithTimeout:currentAttempt:completionHandler:]_block_invoke.437
- ___103-[SUSUISoftwareUpdateController(UI) waitForScanCompletionWithTimeout:currentAttempt:completionHandler:]_block_invoke.440
- ___103-[SUSUISoftwareUpdateController(UI) waitForScanCompletionWithTimeout:currentAttempt:completionHandler:]_block_invoke.441
- ___103-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.368
- ___103-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.369
- ___103-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.372
- ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.346
- ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.348
- ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.350
- ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.349
- ___104-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.353
- ___104-[SUSettingsStatefulUIManager scheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.375
- ___104-[SUSettingsStatefulUIManager scheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.376
- ___104-[SUSettingsStatefulUIManager scheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.377
- ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.357
- ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.358
- ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.360
- ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.359
- ___108-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.361
- ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.362
- ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.363
- ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke.365
- ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.364
- ___115-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke_2.366
- ___42-[SUSUISoftwareUpdateManager refreshState]_block_invoke.434
- ___45-[SUSUISoftwareUpdateManager setAutoInstall:]_block_invoke.471
- ___47-[SUSettingsStatefulUIManager performFullScan:]_block_invoke.429
- ___50-[SUSettingsStatefulUIManager refreshBetaUpdates:]_block_invoke.401
- ___53-[SUSettingsStatefulUIManager handleFullScanResults:]_block_invoke.433
- ___53-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke.324
- ___53-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke.325
- ___53-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke.326
- ___53-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke.327
- ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.473
- ___54-[SUSUISoftwareUpdateManager startInstallWithHandler:]_block_invoke.474
- ___55-[SUSettingsUpdateOperation action_AquireKeybag:error:]_block_invoke.330
- ___55-[SUSettingsUpdateOperation action_AquireKeybag:error:]_block_invoke.331
- ___57-[SUSettingsScanOperation action_QueryUpdatesInfo:error:]_block_invoke.331
- ___57-[SUSettingsUpdateOperation action_ScheduleUpdate:error:]_block_invoke.350
- ___58-[SUSettingsScanOperation action_ReportScanOutcome:error:]_block_invoke.340
- ___61-[SUSettingsScanOperation action_QueryCurrentDownload:error:]_block_invoke.321
- ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.382
- ___62-[SUSUISoftwareUpdateController(UI) handleURL:withCompletion:]_block_invoke.383
- ___64-[SUSUISoftwareUpdateManager unenrollBetaUpdatesWithCompletion:]_block_invoke.783
- ___64-[SUSettingsScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.398
- ___65-[SUSettingsStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.442
- ___65-[SUSettingsUpdateOperation action_InitiateUpdateDownload:error:]_block_invoke.346
- ___65-[SUSettingsUpdateOperation action_PresentTermsConditions:error:]_block_invoke.336
- ___65-[SUSettingsUpdateOperation action_PresentTermsConditions:error:]_block_invoke.337
- ___65-[SUSettingsUpdateOperation action_PresentTermsConditions:error:]_block_invoke.338
- ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.413
- ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.414
- ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke.792
- ___68-[SUSUISoftwareUpdateManager _scanForBetaProgramsWithSeedingDevice:]_block_invoke_2.793
- ___68-[SUSettingsScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.381
- ___69-[SUSUISoftwareUpdateClientManager initWithDelegate:completionQueue:]_block_invoke.289
- ___69-[SUSUISoftwareUpdateClientManager initWithDelegate:completionQueue:]_block_invoke.291
- ___69-[SUSettingsStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.394
- ___69-[SUSettingsUpdateOperation action_PresentDownloadConstraints:error:]_block_invoke.343
- ___69-[SUSettingsUpdateOperation action_PresentDownloadConstraints:error:]_block_invoke.344
- ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.769
- ___70-[SUSUISoftwareUpdateManager scanForUpdatesWithOptions:andCompletion:]_block_invoke.770
- ___71-[SUSUISoftwareUpdateBetaUpdatesController presentAuthenticationDialog]_block_invoke.400
- ___71-[SUSUISoftwareUpdateBetaUpdatesController presentAuthenticationDialog]_block_invoke.401
- ___71-[SUSUISoftwareUpdateBetaUpdatesController presentAuthenticationDialog]_block_invoke.407
- ___71-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:completion:]_block_invoke.781
- ___71-[SUSUISoftwareUpdateManager scanFinishedWithUpdates:options:andError:]_block_invoke.777
- ___71-[SUSettingsScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.402
- ___71-[SUSettingsScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.400
- ___71-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke.354
- ___71-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke.355
- ___71-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke.356
- ___71-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke.357
- ___73-[SUSUISoftwareUpdateManager _alertForDownloadConstraintsWithCompletion:]_block_invoke.754
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.465
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.466
- ___73-[SUSUISoftwareUpdateManager startDownloadAndInstall:update:withHandler:]_block_invoke.468
- ___73-[SUSettingsStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus]_block_invoke.381
- ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.766
- ___74-[SUSUISoftwareUpdateManager presentTermsIfNecessaryForUpdate:completion:]_block_invoke.767
- ___74-[SUSettingsScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.379
- ___75-[SUSettingsStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.431
- ___76-[SUSUISoftwareUpdateAutomaticUpdateController(NeRD) displayNeRDAlertToUser]_block_invoke.304
- ___76-[SUSUISoftwareUpdateManager cancelOrPurgeIfNecessaryWithUpdate:completion:]_block_invoke.764
- ___76-[SUSettingsScanOperation refreshBetaProgramsWithOptions:completionHandler:]_block_invoke.373
- ___78-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]_block_invoke.370
- ___78-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]_block_invoke.373
- ___78-[SUSettingsScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.391
- ___78-[SUSettingsStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.438
- ___82-[SUSUISoftwareUpdateManager _setState:preferredUpdateError:alternateUpdateError:]_block_invoke.423
- ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.454
- ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.455
- ___96-[SUSUISoftwareUpdateManager _reallyDownloadAndInstall:update:AcceptingCellularFees:completion:]_block_invoke.458
- ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.727
- ___96-[SUSUISoftwareUpdateManager promptForDevicePasscodeForDescriptor:unattendedInstall:completion:]_block_invoke.730
- ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke.387
- ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke.388
- ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke.391
- ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke_2.390
- ___98-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke_2.392
- ___block_literal_global.374
- ___block_literal_global.515
- ___block_literal_global.712
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_SoftwareUpdateSettingsUI
CStrings:
+ "%s: RRTS mode forced via SUPreferences: RapidReturnToServiceMode = YES"
+ "%s: Stateful UI Manager Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}s\n\tscheduledForAutoInstall: %{public}s\n\thiddenUpdatesPostSelection: preferred[%{public}s, %{public}@]; alternate[%{public}s, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDevice is in RRTS mode, blocking download and install operation"
+ "%s: Stateful UI Manager Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}s\n\tscheduledForAutoInstall: %{public}s\n\thiddenUpdatesPostSelection: preferred[%{public}s, %{public}@]; alternate[%{public}s, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDevice is in RRTS mode, blocking download and schedule operation"
+ "%s: Stateful UI Manager Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}s\n\tscheduledForAutoInstall: %{public}s\n\thiddenUpdatesPostSelection: preferred[%{public}s, %{public}@]; alternate[%{public}s, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDevice is in RRTS mode, blocking download operation"
+ "%s: Stateful UI Manager Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}s\n\tscheduledForAutoInstall: %{public}s\n\thiddenUpdatesPostSelection: preferred[%{public}s, %{public}@]; alternate[%{public}s, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDevice is in RRTS mode, blocking full scan operation"
+ "%s: Stateful UI Manager Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}s\n\tscheduledForAutoInstall: %{public}s\n\thiddenUpdatesPostSelection: preferred[%{public}s, %{public}@]; alternate[%{public}s, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDevice is in RRTS mode, blocking install operation"
+ "%s: Stateful UI Manager Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}s\n\tscheduledForAutoInstall: %{public}s\n\thiddenUpdatesPostSelection: preferred[%{public}s, %{public}@]; alternate[%{public}s, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDevice is in Rapid Return To Service Mode. Skipping refresh."
+ "%s: Stateful UI Manager Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}s\n\tscheduledForAutoInstall: %{public}s\n\thiddenUpdatesPostSelection: preferred[%{public}s, %{public}@]; alternate[%{public}s, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDevice is in Rapid Return to Service Mode. Skipping refresh beta update."
+ "%s: Using MDMConfiguration for RRTS: %d"
+ "-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]"
+ "-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]"
+ "-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]"
+ "-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]"
+ "-[SUSettingsStatefulUIManager isRapidReturnToServiceMode]"
+ "UPDATE_NOT_ALLOWED_IN_RRTS_MODE"
+ "cd060049-2465-43e3-bbb5-d769a66da2d7"
+ "client:newOSBuildDetected:"
+ "enableRapidReturnToService"
+ "ffc25f86-b83c-4139-b8ad-91131d0e5429"
+ "https://gdmf-auth-stg.apple.com/v2/assets"
+ "isRapidReturnToService"
+ "isRapidReturnToServiceMode"
+ "queue_setEnableRapidReturnToService:"
+ "setEnableRapidReturnToService:"
+ "v32@0:8@\"SUManagerClient\"16@\"NSString\"24"
- "-[SUSettingsStatefulUIManager downloadAndInstall:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke"
- "-[SUSettingsStatefulUIManager downloadAndScheduleUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke"
- "-[SUSettingsStatefulUIManager downloadUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke"
- "-[SUSettingsStatefulUIManager installUpdate:completionHandler:operationDelegate:delegateCallbackQueue:]_block_invoke"

```
