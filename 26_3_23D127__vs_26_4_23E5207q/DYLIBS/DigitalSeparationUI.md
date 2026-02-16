## DigitalSeparationUI

> `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`

```diff

-595.0.2.0.0
-  __TEXT.__text: 0x53d0c
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x50d8
-  __TEXT.__cstring: 0x44b1
-  __TEXT.__const: 0x864
-  __TEXT.__gcc_except_tab: 0x734
-  __TEXT.__oslogstring: 0x264e
+618.0.0.0.0
+  __TEXT.__text: 0x5c91c
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x5118
+  __TEXT.__cstring: 0x43c6
+  __TEXT.__const: 0x984
+  __TEXT.__gcc_except_tab: 0x6f0
+  __TEXT.__oslogstring: 0x282c
   __TEXT.__dlopen_cstrs: 0x332
-  __TEXT.__constg_swiftt: 0x2b0
-  __TEXT.__swift5_typeref: 0x518
-  __TEXT.__swift5_reflstr: 0x193
-  __TEXT.__swift5_fieldmd: 0x160
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_capture: 0x300
-  __TEXT.__swift5_proto: 0x1c
-  __TEXT.__swift_as_entry: 0x68
-  __TEXT.__swift_as_ret: 0x88
+  __TEXT.__constg_swiftt: 0x3f8
+  __TEXT.__swift5_typeref: 0x6b8
+  __TEXT.__swift5_reflstr: 0x222
+  __TEXT.__swift5_fieldmd: 0x1b8
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_capture: 0x318
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift_as_entry: 0x7c
+  __TEXT.__swift_as_ret: 0x9c
   __TEXT.__swift5_assocty: 0x50
-  __TEXT.__unwind_info: 0x1600
-  __TEXT.__eh_frame: 0xb20
-  __TEXT.__objc_classname: 0x968
-  __TEXT.__objc_methname: 0xd8ab
-  __TEXT.__objc_methtype: 0x28ec
-  __TEXT.__objc_stubs: 0x9c20
-  __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0x1090
-  __DATA_CONST.__objc_classlist: 0x1e0
-  __DATA_CONST.__objc_catlist: 0x38
+  __TEXT.__unwind_info: 0x1bd0
+  __TEXT.__eh_frame: 0xe10
+  __TEXT.__objc_classname: 0xa93
+  __TEXT.__objc_methname: 0xda6d
+  __TEXT.__objc_methtype: 0x2a8b
+  __TEXT.__objc_stubs: 0x9d00
+  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__const: 0x1140
+  __DATA_CONST.__objc_classlist: 0x1e8
+  __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33a0
+  __DATA_CONST.__objc_selrefs: 0x33b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x7e8
-  __AUTH_CONST.__const: 0x1008
-  __AUTH_CONST.__cfstring: 0x4600
-  __AUTH_CONST.__objc_const: 0x10540
+  __AUTH_CONST.__auth_got: 0x888
+  __AUTH_CONST.__const: 0x1080
+  __AUTH_CONST.__cfstring: 0x4640
+  __AUTH_CONST.__objc_const: 0x10600
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH.__objc_data: 0x12b8
-  __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x434
-  __DATA.__data: 0xd18
-  __DATA.__bss: 0x588
+  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH.__objc_data: 0x12b0
+  __AUTH.__data: 0x230
+  __DATA.__objc_ivar: 0x430
+  __DATA.__data: 0xd48
+  __DATA.__bss: 0x650
   __DATA.__common: 0x1f8
-  __DATA_DIRTY.__objc_data: 0x188
-  __DATA_DIRTY.__data: 0x30
+  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FC3A3608-EF09-315C-AAE8-C48A7AA6E360
-  Functions: 2197
-  Symbols:   6800
-  CStrings:  3892
+  UUID: 0E12FF08-7603-306A-B2EB-704C5163D30B
+  Functions: 2286
+  Symbols:   6969
+  CStrings:  3928
 
Symbols:
+ +[DSAppPermissionsDescriptor(DigitalSeparationUI) iconForPermission:tableFormat:viewController:]
+ +[DSBiometricManager deviceWithType:]
+ +[DSBiometricManager deviceWithType:].cold.1
+ +[DSBiometricManager identitiesWithType:device:]
+ +[DSBiometricManager identitiesWithType:device:].cold.1
+ +[DSIconFactory detailIconForContact:viewController:]
+ +[DSIconFactory iconWithSize:contact:viewController:]
+ +[DSIconFactory tableIconForContact:viewController:]
+ +[DSPlatterTableView defaultHeaderHorizontalPadding]
+ +[DSUIUtilities appIconForAppID:format:viewController:]
+ -[DSBiometricManager configurePeriocularEnabled:device:]
+ -[DSPublicSharingType(DigitalSeparationUI) iconForDetailInViewController:]
+ -[DSPublicSharingType(DigitalSeparationUI) iconForTableInViewController:]
+ -[DSRemoteUILoader loadRemoteUIFromURL:]
+ -[DSSafetyCheckWhenBlocking isSharingWith:completion:].cold.1
+ -[DSSafetyCheckWhenBlocking isSharingWithContacts:completion:].cold.1
+ -[DSSafetyCheckWhenBlocking safetyCheckControllerWithPreview:forFetchResult:completion:]
+ -[DSSharingPerson(DigitalSeparationUI) iconForDetailInViewController:]
+ -[DSSharingPerson(DigitalSeparationUI) iconForTableInViewController:]
+ -[DSSharingType(DigitalSeparationUI) iconForDetailInViewController:]
+ -[DSSharingType(DigitalSeparationUI) iconForTableInViewController:]
+ -[DSSourceDescriptor(DigitalSeparationUI) iconForDetailInViewController:]
+ -[DSSourceDescriptor(DigitalSeparationUI) iconForTableInViewController:]
+ -[DSTableWelcomeController addIcon:withBorder:]
+ -[DSXPCSharingPerson(DigitalSeparationUI) iconForDetailInViewController:]
+ -[DSXPCSharingPerson(DigitalSeparationUI) iconForTableInViewController:]
+ -[UIViewController(DigitalSeparationUI) ds_scale]
+ _AKURLBagKeyPrivacyRepair
+ _OBJC_CLASS_$__HKEmergencyContact
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __DATA__TtC19DigitalSeparationUI23EmergencyContactManager
+ __IVARS__TtC19DigitalSeparationUI23EmergencyContactManager
+ __METACLASS_DATA__TtC19DigitalSeparationUI23EmergencyContactManager
+ __MergedGlobals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIViewController_$_DigitalSeparationUI
+ __OBJC_$_CATEGORY_UIViewController_$_DigitalSeparationUI
+ __OBJC_$_PROP_LIST_UIViewController_$_DigitalSeparationUI
+ __PROPERTIES_DSBlockingFetchResult
+ ___32-[DSRemoteUILoader loadRemoteUI]_block_invoke
+ ___32-[DSRemoteUILoader loadRemoteUI]_block_invoke.cold.1
+ ___40-[DSRemoteUILoader loadRemoteUIFromURL:]_block_invoke
+ ___40-[DSRemoteUILoader loadRemoteUIFromURL:]_block_invoke.cold.1
+ ___70-[DSSafetyCheckWhenBlocking startManageSharingWithContact:completion:]_block_invoke
+ ___70-[DSSafetyCheckWhenBlocking startManageSharingWithContact:completion:]_block_invoke.314
+ ___70-[DSSafetyCheckWhenBlocking startManageSharingWithContact:completion:]_block_invoke.314.cold.1
+ ___70-[DSSafetyCheckWhenBlocking startManageSharingWithContact:completion:]_block_invoke.317
+ ___70-[DSSafetyCheckWhenBlocking startManageSharingWithContact:completion:]_block_invoke.cold.1
+ ___88-[DSSafetyCheckWhenBlocking safetyCheckControllerWithPreview:forFetchResult:completion:]_block_invoke
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e27_v24?0"NSURL"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32bs40w_e31_v16?0"DSBlockingFetchResult"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_literal_global.344
+ ___block_literal_global.348
+ ___block_literal_global.352
+ ___block_literal_global.376
+ ___isOSVersionAtLeast
+ ___isOSVersionAtLeast.cold.1
+ ___isPlatformVersionAtLeast
+ ___isPlatformVersionAtLeast.cold.1
+ ___isPlatformVersionAtLeast.cold.2
+ ___swift_memcpy136_8
+ __availability_version_check
+ __initializeAvailabilityCheck
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_DigitalSeparationUI
+ __swift_dead_method_stub
+ _block_copy_helper.105
+ _block_copy_helper.119
+ _block_copy_helper.14
+ _block_copy_helper.17
+ _block_copy_helper.20
+ _block_copy_helper.37
+ _block_copy_helper.56
+ _block_copy_helper.59
+ _block_copy_helper.62
+ _block_copy_helper.79
+ _block_descriptor.107
+ _block_descriptor.121
+ _block_descriptor.16
+ _block_descriptor.19
+ _block_descriptor.22
+ _block_descriptor.39
+ _block_descriptor.58
+ _block_descriptor.61
+ _block_descriptor.64
+ _block_descriptor.81
+ _block_destroy_helper.106
+ _block_destroy_helper.120
+ _block_destroy_helper.15
+ _block_destroy_helper.18
+ _block_destroy_helper.21
+ _block_destroy_helper.38
+ _block_destroy_helper.57
+ _block_destroy_helper.60
+ _block_destroy_helper.63
+ _block_destroy_helper.80
+ _compatibilityInitializeAvailabilityCheck
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOQr.48
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC.49
+ _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyx017DigitalSeparationB027SafetyCheckBlockingModifierVGAaBHPxAaBHD1__AgA0cK0HPyHCHC.54
+ _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAcAE5sheet11isPresented0D7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOyAcAE18confirmationDialog_AN15titleVisibility7actions7messageQrqd___AsA0V0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQOyAA01_C16Modifier_ContentVy017DigitalSeparationB0019SafetyCheckBlockingY0VG_SSAcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQOyAA6ButtonVyAA4TextVG_Qo_A11_Qo__AA08ModifiedZ0VyA1_011SafetyCheckC0VAA30_SafeAreaRegionsIgnoringLayoutVGSgQo__Qo__SbQo_HO.53
+ _initializeAvailabilityCheck
+ _kFaceIDRatchetIdentifier
+ _kPasscodeRatchetIdentifier
+ _kTouchIDRatchetIdentifier
+ _memcpy
+ _objc_autorelease
+ _objc_msgSend$addIcon:withBorder:
+ _objc_msgSend$appIconForAppID:format:viewController:
+ _objc_msgSend$cleanup
+ _objc_msgSend$configurePeriocularEnabled:device:
+ _objc_msgSend$detailIconForContact:viewController:
+ _objc_msgSend$deviceWithType:
+ _objc_msgSend$displayScale
+ _objc_msgSend$ds_scale
+ _objc_msgSend$fetchError
+ _objc_msgSend$iconForDetailInViewController:
+ _objc_msgSend$iconForPermission:tableFormat:viewController:
+ _objc_msgSend$iconForTableInViewController:
+ _objc_msgSend$iconWithSize:contact:viewController:
+ _objc_msgSend$identitiesWithType:device:
+ _objc_msgSend$initWithEmail:
+ _objc_msgSend$initWithPeople:error:
+ _objc_msgSend$initWithPhone:
+ _objc_msgSend$isSharingWithContacts:completion:
+ _objc_msgSend$loadRemoteUIFromURL:
+ _objc_msgSend$loadRequest:completion:
+ _objc_msgSend$nameContactIdentifier
+ _objc_msgSend$removeIdentity:error:
+ _objc_msgSend$safetyCheckControllerWithPreview:forFetchResult:completion:
+ _objc_msgSend$setDisplayName:
+ _objc_msgSend$setMasksToBounds:
+ _objc_msgSend$sharingPeople
+ _objc_msgSend$sharingPeopleForContacts:completion:
+ _objc_msgSend$sharingPeopleForIdentities:completion:
+ _objc_msgSend$tableIconForContact:viewController:
+ _objc_msgSend$urlForKey:completion:
+ _objectdestroy.40Tm
+ _objectdestroy.44Tm
+ _rewind
+ _sscanf
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_isUniquelyReferenced_nonNull_native
+ _symbolic SaySo18DSXPCSharingPersonCG
+ _symbolic SaySo19_HKEmergencyContactCG
+ _symbolic SccySaySo19_HKEmergencyContactCG______pG s5ErrorP
+ _symbolic SccySb______pG s5ErrorP
+ _symbolic So13HKHealthStoreC
+ _symbolic So16HKMedicalIDStoreC
+ _symbolic So7NSErrorCSg
+ _symbolic _____ 19DigitalSeparationUI23EmergencyContactManagerC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV 017DigitalSeparationB015SafetyCheckViewV AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y__________GSg 7SwiftUI15ModifiedContentV 017DigitalSeparationB015SafetyCheckViewV AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y_____y_____y_____G_SS_____y_____y_____G_Qo_AEQo_______y__________GSgQo_ 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAE18confirmationDialog_AE15titleVisibility7actions7messageQrqd___AjA0N0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA01_C16Modifier_ContentV 017DigitalSeparationB0019SafetyCheckBlockingQ0V AcAE16keyboardShortcutyQrAA08KeyboardY0VFQO AA6ButtonV AA4TextV AA08ModifiedR0V AT0uvC0V AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y_____y_____y_____y_____G_SS_____y_____y_____G_Qo_AEQo_______y__________GSgQo__Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AcAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAE18confirmationDialog_AK15titleVisibility7actions7messageQrqd___ApA0S0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA01_C16Modifier_ContentV 017DigitalSeparationB0019SafetyCheckBlockingV0V AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA6ButtonV AA4TextV AA08ModifiedW0V AZ0z5CheckC0V AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y_____y_____y_____y_____G_SS_____y_____y_____G_Qo_AFQo__AAy__________GSgQo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaDRd__lFQO AeAE18confirmationDialog_AG15titleVisibility7actions7messageQrqd___AlA0P0Oqd_0_yXEqd_1_yXEtSyRd__AaDRd_0_AaDRd_1_r1_lFQO AA01_e9Modifier_D0V 017DigitalSeparationB0019SafetyCheckBlockingS0V AeAE16keyboardShortcutyQrAA08KeyboardZ0VFQO AA6ButtonV AA4TextV AV0vwE0V AA30_SafeAreaRegionsIgnoringLayoutV AA14_TaskModifier2V
+ _symbolic _____y_____y_____y_____y_____y_____G_SS_____y_____y_____G_Qo_AEQo_______y__________GSgQo__Qo__SbQo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AcAE5sheet11isPresented0D7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAE18confirmationDialog_AN15titleVisibility7actions7messageQrqd___AsA0V0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA01_C16Modifier_ContentV 017DigitalSeparationB0019SafetyCheckBlockingY0V AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA6ButtonV AA4TextV AA08ModifiedZ0V A1_011SafetyCheckC0V AA30_SafeAreaRegionsIgnoringLayoutV
- +[DSAppPermissionsDescriptor(DigitalSeparationUI) iconForPermission:tableFormat:]
- +[DSBiometricManager pearlIdentities].cold.1
- +[DSIconFactory detailIconForContact:]
- +[DSIconFactory iconWithSize:contact:]
- +[DSIconFactory tableIconForContact:]
- +[DSUIUtilities appIconForAppID:format:]
- -[DSBiometricManager configurePeriocularEnabled:]
- -[DSPublicSharingType(DigitalSeparationUI) iconForDetail]
- -[DSPublicSharingType(DigitalSeparationUI) iconForTable]
- -[DSSafetyCheckWhenBlocking prefetchError]
- -[DSSafetyCheckWhenBlocking safetyCheckControllerWithPreview:forContacts:completion:]
- -[DSSafetyCheckWhenBlocking safetyCheckControllerWithPreview:forHandles:completion:]
- -[DSSafetyCheckWhenBlocking safetyCheckControllerWithPreview:forPeople:completion:]
- -[DSSafetyCheckWhenBlocking setPrefetchError:]
- -[DSSharingPerson(DigitalSeparationUI) iconForDetail]
- -[DSSharingPerson(DigitalSeparationUI) iconForTable]
- -[DSSharingType(DigitalSeparationUI) iconForDetail]
- -[DSSharingType(DigitalSeparationUI) iconForTable]
- -[DSSourceDescriptor(DigitalSeparationUI) iconForDetail]
- -[DSSourceDescriptor(DigitalSeparationUI) iconForTable]
- -[DSXPCSharingPerson(DigitalSeparationUI) iconForDetail]
- -[DSXPCSharingPerson(DigitalSeparationUI) iconForTable]
- _OBJC_CLASS_$_PKBiometrics
- _OBJC_CLASS_$_UIScreen
- _OBJC_IVAR_$_DSSafetyCheckWhenBlocking._prefetchError
- __OBJC_$_PROP_LIST_DSPublicSharingType_$_DigitalSeparationUI
- __OBJC_$_PROP_LIST_DSSharingPerson_$_DigitalSeparationUI
- __OBJC_$_PROP_LIST_DSSharingType_$_DigitalSeparationUI
- __OBJC_$_PROP_LIST_DSSourceDescriptor_$_DigitalSeparationUI
- __OBJC_$_PROP_LIST_DSXPCSharingPerson_$_DigitalSeparationUI
- ___83-[DSSafetyCheckWhenBlocking safetyCheckControllerWithPreview:forPeople:completion:]_block_invoke
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_literal_global.345
- ___block_literal_global.349
- ___block_literal_global.353
- ___swift_memcpy128_8
- __os_log_debug_impl
- _block_copy_helper.101
- _block_copy_helper.118
- _block_copy_helper.13
- _block_copy_helper.16
- _block_copy_helper.19
- _block_copy_helper.35
- _block_copy_helper.46
- _block_copy_helper.49
- _block_copy_helper.52
- _block_copy_helper.60
- _block_copy_helper.63
- _block_copy_helper.80
- _block_descriptor.103
- _block_descriptor.120
- _block_descriptor.15
- _block_descriptor.18
- _block_descriptor.21
- _block_descriptor.37
- _block_descriptor.48
- _block_descriptor.51
- _block_descriptor.54
- _block_descriptor.62
- _block_descriptor.65
- _block_descriptor.82
- _block_destroy_helper.102
- _block_destroy_helper.119
- _block_destroy_helper.14
- _block_destroy_helper.17
- _block_destroy_helper.20
- _block_destroy_helper.36
- _block_destroy_helper.47
- _block_destroy_helper.50
- _block_destroy_helper.53
- _block_destroy_helper.61
- _block_destroy_helper.64
- _block_destroy_helper.81
- _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyx017DigitalSeparationB027SafetyCheckBlockingModifierVGAaBHPxAaBHD1__AgA0cK0HPyHCHC.57
- _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAcAE5sheet11isPresented0D7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOyAcAE18confirmationDialog_AJ15titleVisibility7actions7messageQrqd___AoA0S0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQOyAA01_c9Modifier_I0Vy017DigitalSeparationB0019SafetyCheckBlockingV0VG_SSAcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQOyAA6ButtonVyAA4TextVG_Qo_A7_Qo__AY0yzC0VSgQo_AA017_AppearanceActionV0VG_SbQo_HO.56
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$appIconForAppID:format:
- _objc_msgSend$configurePeriocularEnabled:
- _objc_msgSend$detailIconForContact:
- _objc_msgSend$deviceForType:
- _objc_msgSend$iconForDetail
- _objc_msgSend$iconForPermission:tableFormat:
- _objc_msgSend$iconForTable
- _objc_msgSend$iconWithSize:contact:
- _objc_msgSend$identitiesForIdentityType:
- _objc_msgSend$initWithPeople:
- _objc_msgSend$loadRequest:
- _objc_msgSend$mainScreen
- _objc_msgSend$makeSharingPeople
- _objc_msgSend$prefetchError
- _objc_msgSend$privacyRepairURL
- _objc_msgSend$safetyCheckControllerWithPreview:forContacts:completion:
- _objc_msgSend$safetyCheckControllerWithPreview:forHandles:completion:
- _objc_msgSend$safetyCheckControllerWithPreview:forPeople:completion:
- _objc_msgSend$scale
- _objc_msgSend$setPrefetchError:
- _objc_msgSend$sharingPeopleForContacts:
- _objc_msgSend$sharingPeopleForIdentities:
- _objc_msgSend$tableIconForContact:
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
- _objectdestroy.39Tm
- _objectdestroy.43Tm
- _swift_unknownObjectRelease_n
- _symbolic SaySSG
- _symbolic _____Sg 19DigitalSeparationUI15SafetyCheckViewV
- _symbolic _____y_____y_____y_____y_____G_SS_____y_____y_____G_Qo_AFQo_______SgQo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaDRd__lFQO AeAE18confirmationDialog_AG15titleVisibility7actions7messageQrqd___AlA0P0Oqd_0_yXEqd_1_yXEtSyRd__AaDRd_0_AaDRd_1_r1_lFQO AA01_e9Modifier_D0V 017DigitalSeparationB0019SafetyCheckBlockingS0V AeAE16keyboardShortcutyQrAA08KeyboardZ0VFQO AA6ButtonV AA4TextV AV0vwE0V AA017_AppearanceActionS0V
- _symbolic _____y_____y_____y_____y_____y_____G_SS_____y_____y_____G_Qo_AFQo_______SgQo______G_SbQo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA15ModifiedContentV AcAE5sheet11isPresented0D7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAE18confirmationDialog_AJ15titleVisibility7actions7messageQrqd___AoA0S0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA01_c9Modifier_I0V 017DigitalSeparationB0019SafetyCheckBlockingV0V AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA6ButtonV AA4TextV AY0yzC0V AA017_AppearanceActionV0V
CStrings:
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "?"
+ "@36@0:8@16B24@28"
+ "@36@0:8@16i24@28"
+ "@36@0:8f16@20@28"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "Completed emergency contact fetch"
+ "Error getting device with type %ld: %@"
+ "Error removing identity %@ from device: %@"
+ "Error retrieving identities with type %ld from device: %@"
+ "Failed to fetch Remote UI URL %@, error: %@"
+ "Failed to fetch emergency contacts: %@"
+ "Failed to remove emergency contact %@ from list. Error: %@"
+ "Failure removing emergency contact: %@"
+ "Fetching emergency contacts"
+ "ProductVersion"
+ "Ran getSharingStatus but fetchResult is nil, this should never happen!"
+ "Removed emergency contact"
+ "Removing contact: %s from emergency contacts"
+ "Removing emergency contact %@ from emergency contact list"
+ "Retrying fetch emergency contacts due to error: %@"
+ "T@\"NSArray\",N,R"
+ "T@\"NSError\",N,R,VfetchError"
+ "Td,R,N"
+ "View.task @ DigitalSeparationUI/DSBlockingConfirmationView.swift:"
+ "_TtC19DigitalSeparationUI23EmergencyContactManager"
+ "addIcon:withBorder:"
+ "appIconForAppID:format:viewController:"
+ "com.apple.DigitalSeparation.faceID"
+ "com.apple.DigitalSeparation.touchID"
+ "configurePeriocularEnabled:device:"
+ "defaultHeaderHorizontalPadding"
+ "detailIconForContact:viewController:"
+ "deviceWithType:"
+ "displayScale"
+ "ds_scale"
+ "emergencyContactManager"
+ "hasRetriedFetch"
+ "iconForDetailInViewController:"
+ "iconForPermission:tableFormat:viewController:"
+ "iconForTableInViewController:"
+ "iconWithSize:contact:viewController:"
+ "identitiesWithType:device:"
+ "initWithPeople:error:"
+ "isSharingWith: feature disabled or unavailable"
+ "isSharingWithContacts: Permissions fetch completed with error: %{public}@"
+ "isSharingWithContacts: feature disabled or unavailable"
+ "isSharingWithIdentities: Permissions fetch completed with error: %{public}@"
+ "kCFAllocatorNull"
+ "loadRemoteUIFromURL:"
+ "loadRequest completed with success: %d error: %@"
+ "loadRequest:completion:"
+ "nameContactIdentifier"
+ "r"
+ "removeIdentity:error:"
+ "safetyCheckControllerWithPreview:forFetchResult:completion:"
+ "setMasksToBounds:"
+ "sharingPeople"
+ "sharingPeopleForContacts:completion:"
+ "sharingPeopleForIdentities:completion:"
+ "tableIconForContact:viewController:"
+ "urlForKey:completion:"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v28@0:8B16@20"
- "@28@0:8@16B24"
- "@28@0:8@16i24"
- "@28@0:8f16@20"
- "DS Face ID: Failed to fetch BKDevice: %@"
- "SafetyCheckBlockingModifier has neither contacts nor handles"
- "T@\"NSError\",&,N,V_prefetchError"
- "T@\"UIImage\",R,N"
- "Warning: Stale sharing permissions model, refreshing. Please add a prefetch call"
- "_prefetchError"
- "appIconForAppID:format:"
- "configurePeriocularEnabled:"
- "detailIconForContact:"
- "deviceForType:"
- "displayGivenNames"
- "displayNames"
- "iconForDetail"
- "iconForPermission:tableFormat:"
- "iconForTable"
- "iconWithSize:contact:"
- "identitiesForIdentityType:"
- "initWithPeople:"
- "isSharing"
- "isSharingWith: finding sharing with identities"
- "isSharingWithContacts: finding sharing with contacts"
- "loadRequest:"
- "mainScreen"
- "makeSharingPeople"
- "prefetchError"
- "privacyRepairURL"
- "safetyCheckControllerWithPreview:forContacts: feature disabled or unavailable"
- "safetyCheckControllerWithPreview:forContacts: found (%ld) people"
- "safetyCheckControllerWithPreview:forContacts:completion:"
- "safetyCheckControllerWithPreview:forHandles: feature disabled or unavailable"
- "safetyCheckControllerWithPreview:forHandles:completion:"
- "safetyCheckControllerWithPreview:forPeople:completion:"
- "scale"
- "setPrefetchError:"
- "sharingPeopleForContacts:"
- "sharingPeopleForIdentities:"
- "tableIconForContact:"

```
