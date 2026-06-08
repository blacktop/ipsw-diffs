## SetupAssistantSoftwareUpdateUI

> `/System/Library/PrivateFrameworks/SetupAssistantSoftwareUpdateUI.framework/SetupAssistantSoftwareUpdateUI`

```diff

-508.122.1.0.0
-  __TEXT.__text: 0x67df0
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x6b0
-  __TEXT.__cstring: 0xf3b
-  __TEXT.__swift5_typeref: 0xefb
-  __TEXT.__const: 0xe18
-  __TEXT.__swift5_capture: 0x17cc
-  __TEXT.__oslogstring: 0x16ad
-  __TEXT.__constg_swiftt: 0x884
-  __TEXT.__swift5_reflstr: 0x41d
-  __TEXT.__swift5_fieldmd: 0x2d8
+772.0.0.0.0
+  __TEXT.__text: 0x72c70
+  __TEXT.__objc_methlist: 0x758
+  __TEXT.__cstring: 0xf5b
+  __TEXT.__swift5_typeref: 0xfeb
+  __TEXT.__const: 0xec8
+  __TEXT.__swift5_capture: 0x1dd8
+  __TEXT.__oslogstring: 0x1b5d
+  __TEXT.__constg_swiftt: 0x8c8
+  __TEXT.__swift5_reflstr: 0x43d
+  __TEXT.__swift5_fieldmd: 0x2e4
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_proto: 0x48
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x40
-  __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift_as_ret: 0x50
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x78
+  __TEXT.__swift_as_cont: 0xd4
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12c8
-  __TEXT.__eh_frame: 0xd28
-  __TEXT.__objc_classname: 0x253
-  __TEXT.__objc_methname: 0x19c1
-  __TEXT.__objc_methtype: 0x632
-  __TEXT.__objc_stubs: 0xf00
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x188
+  __TEXT.__unwind_info: 0x16b0
+  __TEXT.__eh_frame: 0xff8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x610
+  __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_protorefs: 0x58
-  __AUTH_CONST.__auth_got: 0x820
-  __AUTH_CONST.__const: 0x3d68
-  __AUTH_CONST.__objc_const: 0x2f98
-  __AUTH.__objc_data: 0x1378
-  __AUTH.__data: 0x180
-  __DATA.__data: 0x930
-  __DATA.__bss: 0x840
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x4c40
+  __AUTH_CONST.__objc_const: 0x3708
+  __AUTH_CONST.__auth_got: 0x870
+  __AUTH.__objc_data: 0x14c0
+  __AUTH.__data: 0x170
+  __DATA.__data: 0x998
+  __DATA.__bss: 0x750
   __DATA.__common: 0x60
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
+  - /System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI
   - /System/Library/PrivateFrameworks/Seeding.framework/Seeding
   - /System/Library/PrivateFrameworks/Settings.framework/Settings
-  - /System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E32B8A4-41F3-357E-B012-4361C9FB6834
-  Functions: 1733
-  Symbols:   678
-  CStrings:  494
+  UUID: 1CA59E43-6695-3E32-A836-79DA0CB85CCC
+  Functions: 2009
+  Symbols:   1642
+  CStrings:  187
 
Symbols:
+ -[SUUISetupAssistantMandatoryUpdateController(InitRedirect) init]
+ -[SUUISetupAssistantMigrationController(InitRedirect) init]
+ -[SUUISetupAssistantRestoreController(InitRedirect) init]
+ _OBJC_CLASS_$_UIViewController
+ __OBJC_$_INSTANCE_METHODS_SUUISetupAssistantMandatoryUpdateController(InitRedirect)
+ __OBJC_$_INSTANCE_METHODS_SUUISetupAssistantMigrationController(InitRedirect)
+ __OBJC_$_INSTANCE_METHODS_SUUISetupAssistantRestoreController(InitRedirect)
+ __PROTOCOLS_SUUISetupAssistantMandatoryUpdateController.197
+ __PROTOCOL_INSTANCE_METHODS_OPT_SUUISetupAssistantMandatoryUpdateControllerDelegate
+ ___swift__destructor
+ ___swift__destructor.137
+ ___swift__destructor.827
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.1002
+ ___swift_closure_destructor.1006
+ ___swift_closure_destructor.101
+ ___swift_closure_destructor.1010
+ ___swift_closure_destructor.1013
+ ___swift_closure_destructor.1016
+ ___swift_closure_destructor.102
+ ___swift_closure_destructor.1020
+ ___swift_closure_destructor.1024
+ ___swift_closure_destructor.1028
+ ___swift_closure_destructor.103
+ ___swift_closure_destructor.1032
+ ___swift_closure_destructor.1036
+ ___swift_closure_destructor.1040
+ ___swift_closure_destructor.1043
+ ___swift_closure_destructor.1047
+ ___swift_closure_destructor.105
+ ___swift_closure_destructor.1050
+ ___swift_closure_destructor.1054
+ ___swift_closure_destructor.1058
+ ___swift_closure_destructor.106
+ ___swift_closure_destructor.1062
+ ___swift_closure_destructor.1065
+ ___swift_closure_destructor.1069
+ ___swift_closure_destructor.107
+ ___swift_closure_destructor.1072
+ ___swift_closure_destructor.1075
+ ___swift_closure_destructor.1078
+ ___swift_closure_destructor.1082
+ ___swift_closure_destructor.1086
+ ___swift_closure_destructor.109
+ ___swift_closure_destructor.1090
+ ___swift_closure_destructor.1094
+ ___swift_closure_destructor.1098
+ ___swift_closure_destructor.1102
+ ___swift_closure_destructor.1106
+ ___swift_closure_destructor.1109
+ ___swift_closure_destructor.111
+ ___swift_closure_destructor.1113
+ ___swift_closure_destructor.1119
+ ___swift_closure_destructor.1123
+ ___swift_closure_destructor.113
+ ___swift_closure_destructor.114
+ ___swift_closure_destructor.115
+ ___swift_closure_destructor.116
+ ___swift_closure_destructor.117
+ ___swift_closure_destructor.119
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.120
+ ___swift_closure_destructor.121
+ ___swift_closure_destructor.124
+ ___swift_closure_destructor.125
+ ___swift_closure_destructor.127
+ ___swift_closure_destructor.128
+ ___swift_closure_destructor.129
+ ___swift_closure_destructor.130
+ ___swift_closure_destructor.132
+ ___swift_closure_destructor.133
+ ___swift_closure_destructor.136
+ ___swift_closure_destructor.137
+ ___swift_closure_destructor.139
+ ___swift_closure_destructor.140
+ ___swift_closure_destructor.141
+ ___swift_closure_destructor.143
+ ___swift_closure_destructor.145
+ ___swift_closure_destructor.146
+ ___swift_closure_destructor.147
+ ___swift_closure_destructor.149
+ ___swift_closure_destructor.15
+ ___swift_closure_destructor.151
+ ___swift_closure_destructor.153
+ ___swift_closure_destructor.155
+ ___swift_closure_destructor.157
+ ___swift_closure_destructor.158
+ ___swift_closure_destructor.160
+ ___swift_closure_destructor.161
+ ___swift_closure_destructor.162
+ ___swift_closure_destructor.163
+ ___swift_closure_destructor.166
+ ___swift_closure_destructor.169
+ ___swift_closure_destructor.170
+ ___swift_closure_destructor.173
+ ___swift_closure_destructor.174
+ ___swift_closure_destructor.177
+ ___swift_closure_destructor.178
+ ___swift_closure_destructor.18
+ ___swift_closure_destructor.180
+ ___swift_closure_destructor.181
+ ___swift_closure_destructor.182
+ ___swift_closure_destructor.183
+ ___swift_closure_destructor.186
+ ___swift_closure_destructor.187
+ ___swift_closure_destructor.191
+ ___swift_closure_destructor.194
+ ___swift_closure_destructor.195
+ ___swift_closure_destructor.197
+ ___swift_closure_destructor.199
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.201
+ ___swift_closure_destructor.203
+ ___swift_closure_destructor.205
+ ___swift_closure_destructor.207
+ ___swift_closure_destructor.209
+ ___swift_closure_destructor.21
+ ___swift_closure_destructor.210
+ ___swift_closure_destructor.213
+ ___swift_closure_destructor.216
+ ___swift_closure_destructor.219
+ ___swift_closure_destructor.22
+ ___swift_closure_destructor.222
+ ___swift_closure_destructor.223
+ ___swift_closure_destructor.227
+ ___swift_closure_destructor.230
+ ___swift_closure_destructor.231
+ ___swift_closure_destructor.234
+ ___swift_closure_destructor.235
+ ___swift_closure_destructor.238
+ ___swift_closure_destructor.239
+ ___swift_closure_destructor.24
+ ___swift_closure_destructor.242
+ ___swift_closure_destructor.244
+ ___swift_closure_destructor.246
+ ___swift_closure_destructor.247
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.250
+ ___swift_closure_destructor.251
+ ___swift_closure_destructor.254
+ ___swift_closure_destructor.258
+ ___swift_closure_destructor.26
+ ___swift_closure_destructor.262
+ ___swift_closure_destructor.266
+ ___swift_closure_destructor.27
+ ___swift_closure_destructor.270
+ ___swift_closure_destructor.274
+ ___swift_closure_destructor.275
+ ___swift_closure_destructor.277
+ ___swift_closure_destructor.280
+ ___swift_closure_destructor.282
+ ___swift_closure_destructor.285
+ ___swift_closure_destructor.287
+ ___swift_closure_destructor.288
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.291
+ ___swift_closure_destructor.292
+ ___swift_closure_destructor.295
+ ___swift_closure_destructor.296
+ ___swift_closure_destructor.30
+ ___swift_closure_destructor.300
+ ___swift_closure_destructor.303
+ ___swift_closure_destructor.304
+ ___swift_closure_destructor.307
+ ___swift_closure_destructor.31
+ ___swift_closure_destructor.311
+ ___swift_closure_destructor.314
+ ___swift_closure_destructor.318
+ ___swift_closure_destructor.32
+ ___swift_closure_destructor.322
+ ___swift_closure_destructor.323
+ ___swift_closure_destructor.325
+ ___swift_closure_destructor.326
+ ___swift_closure_destructor.328
+ ___swift_closure_destructor.329
+ ___swift_closure_destructor.331
+ ___swift_closure_destructor.332
+ ___swift_closure_destructor.335
+ ___swift_closure_destructor.336
+ ___swift_closure_destructor.339
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.340
+ ___swift_closure_destructor.343
+ ___swift_closure_destructor.344
+ ___swift_closure_destructor.347
+ ___swift_closure_destructor.348
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.351
+ ___swift_closure_destructor.352
+ ___swift_closure_destructor.355
+ ___swift_closure_destructor.356
+ ___swift_closure_destructor.359
+ ___swift_closure_destructor.360
+ ___swift_closure_destructor.363
+ ___swift_closure_destructor.364
+ ___swift_closure_destructor.368
+ ___swift_closure_destructor.37
+ ___swift_closure_destructor.370
+ ___swift_closure_destructor.372
+ ___swift_closure_destructor.373
+ ___swift_closure_destructor.376
+ ___swift_closure_destructor.377
+ ___swift_closure_destructor.38
+ ___swift_closure_destructor.380
+ ___swift_closure_destructor.381
+ ___swift_closure_destructor.383
+ ___swift_closure_destructor.385
+ ___swift_closure_destructor.386
+ ___swift_closure_destructor.389
+ ___swift_closure_destructor.39
+ ___swift_closure_destructor.393
+ ___swift_closure_destructor.394
+ ___swift_closure_destructor.397
+ ___swift_closure_destructor.401
+ ___swift_closure_destructor.405
+ ___swift_closure_destructor.409
+ ___swift_closure_destructor.413
+ ___swift_closure_destructor.416
+ ___swift_closure_destructor.417
+ ___swift_closure_destructor.419
+ ___swift_closure_destructor.42
+ ___swift_closure_destructor.421
+ ___swift_closure_destructor.423
+ ___swift_closure_destructor.425
+ ___swift_closure_destructor.427
+ ___swift_closure_destructor.429
+ ___swift_closure_destructor.43
+ ___swift_closure_destructor.431
+ ___swift_closure_destructor.433
+ ___swift_closure_destructor.435
+ ___swift_closure_destructor.437
+ ___swift_closure_destructor.440
+ ___swift_closure_destructor.443
+ ___swift_closure_destructor.446
+ ___swift_closure_destructor.447
+ ___swift_closure_destructor.450
+ ___swift_closure_destructor.451
+ ___swift_closure_destructor.454
+ ___swift_closure_destructor.455
+ ___swift_closure_destructor.458
+ ___swift_closure_destructor.459
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.462
+ ___swift_closure_destructor.463
+ ___swift_closure_destructor.466
+ ___swift_closure_destructor.467
+ ___swift_closure_destructor.47
+ ___swift_closure_destructor.470
+ ___swift_closure_destructor.474
+ ___swift_closure_destructor.477
+ ___swift_closure_destructor.478
+ ___swift_closure_destructor.48
+ ___swift_closure_destructor.481
+ ___swift_closure_destructor.482
+ ___swift_closure_destructor.485
+ ___swift_closure_destructor.489
+ ___swift_closure_destructor.493
+ ___swift_closure_destructor.497
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.50
+ ___swift_closure_destructor.501
+ ___swift_closure_destructor.508
+ ___swift_closure_destructor.51
+ ___swift_closure_destructor.511
+ ___swift_closure_destructor.514
+ ___swift_closure_destructor.517
+ ___swift_closure_destructor.521
+ ___swift_closure_destructor.525
+ ___swift_closure_destructor.529
+ ___swift_closure_destructor.533
+ ___swift_closure_destructor.537
+ ___swift_closure_destructor.54
+ ___swift_closure_destructor.541
+ ___swift_closure_destructor.545
+ ___swift_closure_destructor.55
+ ___swift_closure_destructor.552
+ ___swift_closure_destructor.555
+ ___swift_closure_destructor.559
+ ___swift_closure_destructor.563
+ ___swift_closure_destructor.567
+ ___swift_closure_destructor.57
+ ___swift_closure_destructor.571
+ ___swift_closure_destructor.577
+ ___swift_closure_destructor.58
+ ___swift_closure_destructor.580
+ ___swift_closure_destructor.582
+ ___swift_closure_destructor.586
+ ___swift_closure_destructor.589
+ ___swift_closure_destructor.59
+ ___swift_closure_destructor.593
+ ___swift_closure_destructor.597
+ ___swift_closure_destructor.60
+ ___swift_closure_destructor.600
+ ___swift_closure_destructor.604
+ ___swift_closure_destructor.607
+ ___swift_closure_destructor.611
+ ___swift_closure_destructor.614
+ ___swift_closure_destructor.618
+ ___swift_closure_destructor.62
+ ___swift_closure_destructor.622
+ ___swift_closure_destructor.63
+ ___swift_closure_destructor.65
+ ___swift_closure_destructor.650
+ ___swift_closure_destructor.653
+ ___swift_closure_destructor.657
+ ___swift_closure_destructor.661
+ ___swift_closure_destructor.665
+ ___swift_closure_destructor.669
+ ___swift_closure_destructor.67
+ ___swift_closure_destructor.674
+ ___swift_closure_destructor.677
+ ___swift_closure_destructor.68
+ ___swift_closure_destructor.681
+ ___swift_closure_destructor.685
+ ___swift_closure_destructor.689
+ ___swift_closure_destructor.693
+ ___swift_closure_destructor.698
+ ___swift_closure_destructor.701
+ ___swift_closure_destructor.705
+ ___swift_closure_destructor.709
+ ___swift_closure_destructor.71
+ ___swift_closure_destructor.713
+ ___swift_closure_destructor.717
+ ___swift_closure_destructor.722
+ ___swift_closure_destructor.725
+ ___swift_closure_destructor.729
+ ___swift_closure_destructor.733
+ ___swift_closure_destructor.737
+ ___swift_closure_destructor.741
+ ___swift_closure_destructor.744
+ ___swift_closure_destructor.747
+ ___swift_closure_destructor.75
+ ___swift_closure_destructor.751
+ ___swift_closure_destructor.755
+ ___swift_closure_destructor.759
+ ___swift_closure_destructor.763
+ ___swift_closure_destructor.767
+ ___swift_closure_destructor.771
+ ___swift_closure_destructor.775
+ ___swift_closure_destructor.779
+ ___swift_closure_destructor.78
+ ___swift_closure_destructor.784
+ ___swift_closure_destructor.788
+ ___swift_closure_destructor.79
+ ___swift_closure_destructor.792
+ ___swift_closure_destructor.796
+ ___swift_closure_destructor.8
+ ___swift_closure_destructor.800
+ ___swift_closure_destructor.804
+ ___swift_closure_destructor.807
+ ___swift_closure_destructor.811
+ ___swift_closure_destructor.815
+ ___swift_closure_destructor.819
+ ___swift_closure_destructor.82
+ ___swift_closure_destructor.823
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.831
+ ___swift_closure_destructor.834
+ ___swift_closure_destructor.837
+ ___swift_closure_destructor.841
+ ___swift_closure_destructor.845
+ ___swift_closure_destructor.849
+ ___swift_closure_destructor.853
+ ___swift_closure_destructor.857
+ ___swift_closure_destructor.86
+ ___swift_closure_destructor.861
+ ___swift_closure_destructor.865
+ ___swift_closure_destructor.869
+ ___swift_closure_destructor.87
+ ___swift_closure_destructor.873
+ ___swift_closure_destructor.877
+ ___swift_closure_destructor.880
+ ___swift_closure_destructor.883
+ ___swift_closure_destructor.886
+ ___swift_closure_destructor.890
+ ___swift_closure_destructor.894
+ ___swift_closure_destructor.898
+ ___swift_closure_destructor.9
+ ___swift_closure_destructor.90
+ ___swift_closure_destructor.902
+ ___swift_closure_destructor.906
+ ___swift_closure_destructor.91
+ ___swift_closure_destructor.910
+ ___swift_closure_destructor.914
+ ___swift_closure_destructor.918
+ ___swift_closure_destructor.922
+ ___swift_closure_destructor.926
+ ___swift_closure_destructor.93
+ ___swift_closure_destructor.930
+ ___swift_closure_destructor.934
+ ___swift_closure_destructor.937
+ ___swift_closure_destructor.94
+ ___swift_closure_destructor.940
+ ___swift_closure_destructor.943
+ ___swift_closure_destructor.947
+ ___swift_closure_destructor.951
+ ___swift_closure_destructor.955
+ ___swift_closure_destructor.959
+ ___swift_closure_destructor.96
+ ___swift_closure_destructor.963
+ ___swift_closure_destructor.967
+ ___swift_closure_destructor.97
+ ___swift_closure_destructor.971
+ ___swift_closure_destructor.975
+ ___swift_closure_destructor.979
+ ___swift_closure_destructor.98
+ ___swift_closure_destructor.983
+ ___swift_closure_destructor.987
+ ___swift_closure_destructor.99
+ ___swift_closure_destructor.991
+ ___swift_closure_destructor.994
+ ___swift_closure_destructor.998
+ _block_copy_helper.213
+ _block_copy_helper.216
+ _block_descriptor.215
+ _block_descriptor.218
+ _block_destroy_helper.214
+ _block_destroy_helper.217
+ _keypath_get_selector_downloadSize
+ _keypath_get_selector_isSplatUpdate
+ _objc_msgSend$downloadSize
+ _objc_msgSend$initForSetupAssistant:
+ _objc_msgSend$isSplatUpdate
+ _objc_msgSend$parentViewController
+ _objc_msgSend$setupAssistantMandatoryUpdateControllerAutoInstallCountdownDuration:
+ _objc_msgSend$setupAssistantMandatoryUpdateControllerShouldShowAutoInstallAlert:
+ _objc_storeStrong
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_deallocPartialClassInstance
+ _swift_release_x8
+ _symbolic Sbz_Xx
+ _symbolic ScCy__________G So19SUUIStatefulUIStateV s5NeverO
+ _symbolic Sd
+ _symbolic SdIegd_
+ _symbolic So16UIViewControllerCSdIegyd_
+ _symbolic So16UIViewControllerC_____Iegyd_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____ s6UInt64V
+ _symbolic _____Iegr_ So19SUUIStatefulUIStateV
+ _symbolic _____Sg 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV
+ _symbolic _____Sg 26SoftwareUpdateUIFoundation36SUUIExperienceReconfigurationContextV
+ _symbolic _____Sg 30SetupAssistantSoftwareUpdateUI09SUUISetupB10ControllerC
+ _symbolic _____y______ySS_____GGSg 7Combine10PublishersO9MergeManyV AA12AnyPublisherV s5NeverO
+ _symbolic _____y______y__________GG 7Combine10PublishersO6FilterV AA18PassthroughSubjectC So19SUUIStatefulUIStateV s5NeverO
+ _symbolic _____y______y______y__________GGG 7Combine10PublishersO5FirstV AC6FilterV AA18PassthroughSubjectC So19SUUIStatefulUIStateV s5NeverO
+ _symbolic ypXmTIegd_
- __INSTANCE_METHODS_SUUISetupAssistantMandatoryUpdateController
- __INSTANCE_METHODS_SUUISetupAssistantMigrationController
- __INSTANCE_METHODS_SUUISetupAssistantRestoreController
- __PROTOCOLS_SUUISetupAssistantMandatoryUpdateController.124
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SetupAssistantSoftwareUpdateUI
- _block_copy_helper.141
- _block_copy_helper.144
- _block_descriptor.143
- _block_descriptor.146
- _block_destroy_helper.142
- _block_destroy_helper.145
- _objc_msgSend$isEmptyScanResults
- _objc_msgSend$percentComplete
- _objc_msgSend$setFormattingContext:
- _objc_msgSend$setIncludesApproximationPhrase:
- _objc_msgSend$setIncludesTimeRemainingPhrase:
- _objc_msgSend$setMaximumUnitCount:
- _objc_msgSend$timeRemaining
- _objc_release_x20
- _objc_retain_x8
CStrings:
+ "%s: environment is nil when instantiating progress view"
+ "%s: reactivePlatformEnvironment is nil in handlePreUpdateError"
+ "%{public}s have been asked to shwo the auto-install alert. Showing alert with countdown duration: %{public}f seconds."
+ "%{public}s: Cannot wait for scan completion - reactive manager is nil"
+ "%{public}s: Manager is idle, triggering scan for available updates"
+ "%{public}s: No presented descriptor available after scan completion"
+ "%{public}s: Popping back after scan failure alert"
+ "%{public}s: Scan completed with state %{public}s"
+ "%{public}s: Scan failure alert cancel button tapped"
+ "%{public}s: State is %{public}s, waiting for scan completion"
+ "%{public}s: Will show scan failure alert"
+ "%{public}s: statefulUIEnvironment is nil in viewDidAppear, initializing environment now"
+ "Double value cannot be converted to Int because it is either infinite or NaN"
+ "Double value cannot be converted to Int because the result would be greater than Int.max"
+ "Double value cannot be converted to Int because the result would be less than Int.min"
+ "Failed to instantitate progress view"
+ "Initializing platform environment..."
+ "Not enough bits to represent the passed value"
+ "Performing extended initialization for SUUISetupAssistantMandatoryUpdateController"
+ "Platform environment initialized."
+ "SUUISetupAssistantController.initializeEnvironment: Already initialized, skipping"
+ "SUUISetupAssistantController.initializeEnvironment: Creating platform environment..."
+ "SUUISetupAssistantController.initializeEnvironment: Platform environment ready"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "waitForScanCompletion()"
- "#16@0:8"
- ".cxx_destruct"
- "?"
- "@\"<SUUIDescriptor>\"16@0:8"
- "@\"<SUUIDocumentation>\"16@0:8"
- "@\"<SUUIDownloadPolicy>\"16@0:8"
- "@\"<SUUIDownloadProgress>\"16@0:8"
- "@\"NSDate\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"UIViewController\"16"
- "@\"NSString\"32@0:8@\"UIViewController\"16@\"SUScanOptions\"24"
- "@\"SUScanOptions\""
- "@\"SUScanOptions\"32@0:8@\"<SUUIScanOperation>\"16@\"NSString\"24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8B16B20"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24@32q40"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIViewController\"16"
- "B24@0:8@16"
- "Installing…"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Paused"
- "Popping back from mandatory update after scan failure for required update alert"
- "Preparing Update…"
- "Q16@0:8"
- "SUUIDescriptor"
- "SUUIDownload"
- "SUUIDownloadProgress"
- "SUUIMobileScanOptionsProvider"
- "SUUISetupAssistantController"
- "SUUISetupAssistantControllerDelegate"
- "SUUISetupAssistantMandatoryUpdateController"
- "SUUISetupAssistantMandatoryUpdateControllerDelegate"
- "SUUISetupAssistantMigrationController"
- "SUUISetupAssistantNetworkProvider"
- "SUUISetupAssistantProgressController"
- "SUUISetupAssistantRestoreController"
- "Scan failure for required update alert cancel button tapped"
- "SetupAssistantSoftwareUpdateUI/SUUISetupAssistantProgressController.swift"
- "SetupAssistantSoftwareUpdateUI/SUUISetupAssistantReactiveStateManaging.swift"
- "SetupAssistantSoftwareUpdateUI/SUUISetupAssistantRestoreController.swift"
- "T#,R"
- "T@\"<SUUIDescriptor>\",R"
- "T@\"<SUUIDocumentation>\",R"
- "T@\"<SUUIDownloadPolicy>\",R"
- "T@\"<SUUIDownloadProgress>\",R"
- "T@\"NSDate\",R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",N,C"
- "T@\"NSString\",R,C"
- "T@\"SUScanOptions\",N,&,VmdmUpdateOptions"
- "T@\"SUUIStatefulUIManager\",N,R"
- "TB,R"
- "TB,R,GisAutoDownload"
- "TB,R,GisDone"
- "TB,R,GisDownloadable"
- "TB,R,GisSplatUpdate"
- "TB,R,GisSplomboUpdate"
- "TB,R,GisStalled"
- "TB,R,GisUninitialized"
- "TQ,R"
- "Td,R"
- "Tf,R"
- "Tq,R"
- "Unable to download"
- "Unable to install"
- "Unknown descriptor state"
- "Update Requested…"
- "Vv16@0:8"
- "Will show alert for scan failure for required update"
- "^{_NSZone=}16@0:8"
- "_TtCE30SetupAssistantSoftwareUpdateUICSo8NSBundleP33_23AEB59017C19753AB8020CF5548E9C011LookupClass"
- "_applicationIconImageForBundleIdentifier:format:"
- "actionWithTitle:style:handler:"
- "activateConstraints:"
- "addAction:"
- "addButton:"
- "addChildViewController:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "alertControllerWithTitle:message:preferredStyle:"
- "allowUserToInstallTonight"
- "allowUserToSkip"
- "applicableUpdate"
- "audienceType"
- "autoDownload"
- "autoInstallTimeRemaining"
- "autoInstallTimer"
- "autorelease"
- "availableContentViewHeight"
- "backupName"
- "boldButton"
- "bottomAnchor"
- "bundleForClass:"
- "buttonTray"
- "class"
- "code"
- "conformsToProtocol:"
- "constant"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "constraintLessThanOrEqualToAnchor:constant:"
- "contentView"
- "copyWithZone:"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "descriptor"
- "descriptorStateChangedCancellable"
- "deviceModel"
- "deviceName"
- "didMoveToParentViewController:"
- "dismissViewControllerAnimated:completion:"
- "documentation"
- "done"
- "downloadErrorPreventingUpdate"
- "downloadFailedCancellable"
- "downloadFinishedCancellable"
- "downloadProgressDidChangedCancellable"
- "downloadSize"
- "downloadable"
- "encodeWithCoder:"
- "errorLabel"
- "f16@0:8"
- "fullUpdateName"
- "hash"
- "headerView"
- "heightAnchor"
- "heightConstraint"
- "hostingController"
- "iconSource"
- "init"
- "initWithCoder:"
- "initWithTitle:detailText:icon:"
- "initWithTitle:detailText:icon:contentLayout:"
- "initWithTitle:detailText:symbolName:"
- "initWithTitle:detailText:symbolName:contentLayout:"
- "initiatingUpdate"
- "installFailedCancellable"
- "installStartedCancellable"
- "installationSize"
- "invalidate"
- "isAutoDownload"
- "isDone"
- "isDownloadable"
- "isEmptyScanResults"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isScheduled"
- "isSplatUpdate"
- "isSplomboUpdate"
- "isStalled"
- "isSuccess"
- "isUninitialized"
- "isViewLoaded"
- "layoutIfNeeded"
- "leadingAnchor"
- "linkButton"
- "loadView"
- "makeWithAllowUserToInstallTonight:allowUserToSkip:"
- "mandatoryUpdateBodyString"
- "mandatoryUpdateEligible"
- "mandatoryUpdateOptional"
- "mandatoryUpdateRestrictedToOutOfTheBox"
- "mandatoryUpdateVersionMax"
- "mandatoryUpdateVersionMin"
- "mdmUpdateOptions"
- "navigationController"
- "navigationItem"
- "networkUnavailable"
- "normalizedPercentComplete"
- "percentComplete"
- "performExtendedInitializationWithCompletion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phase"
- "policy"
- "popViewControllerAnimated:"
- "preferredFontForTextStyle:"
- "preparationSize"
- "presentViewController:animated:completion:"
- "productBuildVersion"
- "productSystemName"
- "productVersion"
- "productVersionExtra"
- "progress"
- "promoteAlternateUpdate"
- "publisher"
- "pushViewController:animated:"
- "q16@0:8"
- "q40@0:8@\"UIViewController\"16@\"NSString\"24@\"NSString\"32"
- "q40@0:8@16@24@32"
- "reactivePlatformEnvironment"
- "release"
- "releaseDate"
- "removeButton:"
- "removeConstraint:"
- "requestedBuild"
- "requestedPMV"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scanOptionsForScanOperation:clientIdentifier:"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "self"
- "setAllowedUnits:"
- "setBackupName:"
- "setDelegate:"
- "setDetailText:"
- "setDeviceModel:"
- "setDeviceName:"
- "setEnabled:"
- "setFont:"
- "setFormattingContext:"
- "setHidden:"
- "setHidesBackButton:"
- "setIncludesApproximationPhrase:"
- "setIncludesTimeRemainingPhrase:"
- "setLineBreakMode:"
- "setMaximumUnitCount:"
- "setMdmUpdateOptions:"
- "setMessage:"
- "setNumberOfLines:"
- "setPasscodePrompt:"
- "setPasscodeSubPrompt:"
- "setProgress:"
- "setProgressText:"
- "setScanOptionsProvider:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTitle:"
- "setTitle:forState:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUnitsStyle:"
- "setupAssistantMandatoryUpdateController:compareProductVersion:toProductVersion:"
- "setupAssistantMandatoryUpdateController:humanReadableOSVersionFromScanOptions:"
- "setupAssistantMandatoryUpdateControllerCurrentProductVersion:"
- "setupAssistantMandatoryUpdateControllerDeviceIsFromFactory:"
- "setupAssistantMandatoryUpdateControllerDidFail:"
- "setupAssistantMandatoryUpdateControllerHasBuddyCloudConfiguration:"
- "setupAssistantMandatoryUpdateControllerHumanReadableCurrentOSVersion:"
- "setupAssistantMandatoryUpdateControllerIsDEP:"
- "setupAssistantMandatoryUpdateControllerIsSuggestedUpdateRequired:"
- "setupAssistantNetworkProviderIsConnectedOverWiFi:"
- "setupAssistantNetworkProviderIsNetworkReachable:"
- "setupAssistantNetworkProviderPresentWiFiPane:"
- "setupAssistantViewController:didFailToInstallUpdate:error:"
- "setupAssistantViewController:didStartInstallUpdate:"
- "setupAssistantViewController:prepareToInstallUpdate:replyHandler:"
- "setupAssistantViewController:toggleLoadingUI:"
- "setupAssistantViewController:updateAttempt:ofType:failedDueToError:"
- "setupAssistantViewControllerDidAppear:animated:"
- "setupAssistantViewControllerDidDisappear:animated:"
- "setupAssistantViewControllerDidLoad:"
- "setupAssistantViewControllerDone:"
- "setupAssistantViewControllerLoadView:"
- "setupAssistantViewControllerWillAppear:animated:"
- "setupAssistantViewControllerWillDisappear:animated:"
- "splatUpdate"
- "splomboUpdate"
- "stalled"
- "stateRefreshedCancellable"
- "statefulUIEnvironment"
- "statefulUIManager"
- "stringFromTimeInterval:"
- "superclass"
- "supportsSecureCoding"
- "systemRedColor"
- "timeRemaining"
- "topAnchor"
- "topViewController"
- "totalRequiredFreeSpace"
- "trailingAnchor"
- "traits"
- "underlyingDescriptor"
- "uninitialized"
- "updateAction"
- "updateLaterButton"
- "updateLaterTapped"
- "updateName"
- "updateNowButton"
- "updateNowTapped"
- "updateTonightButton"
- "updateTonightTapped"
- "updateType"
- "upgradeVersionType"
- "v16@0:8"
- "v16@?0@\"NSTimer\"8"
- "v16@?0@\"UIAlertAction\"8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"UIViewController\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8@\"UIViewController\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"UIViewController\"16@\"SUUIStatefulDescriptor\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"UIViewController\"16@\"SUUIStatefulDescriptor\"24@\"SUUIStatefulError\"32"
- "v40@0:8@\"UIViewController\"16@\"SUUIStatefulDescriptor\"24@?<v@?>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"UIViewController\"16@\"SUUIStatefulDescriptor\"24q32@\"SUUIStatefulError\"40"
- "v48@0:8@16@24q32@40"
- "v8@?0"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewWillAppear:"
- "viewWillDisappear:"
- "zone"

```
