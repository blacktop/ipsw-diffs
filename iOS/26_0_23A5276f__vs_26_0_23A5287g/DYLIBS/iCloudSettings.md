## iCloudSettings

> `/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings`

```diff

-301.23.0.17.0
-  __TEXT.__text: 0x17f4fc
-  __TEXT.__auth_stubs: 0x3840
-  __TEXT.__objc_methlist: 0x4404
-  __TEXT.__const: 0xe0f4
-  __TEXT.__oslogstring: 0x8e01
-  __TEXT.__cstring: 0x914e
-  __TEXT.__gcc_except_tab: 0x50c
+301.23.0.19.0
+  __TEXT.__text: 0x186cc4
+  __TEXT.__auth_stubs: 0x38a0
+  __TEXT.__objc_methlist: 0x44b4
+  __TEXT.__const: 0xeb34
+  __TEXT.__oslogstring: 0x9211
+  __TEXT.__cstring: 0x94fe
+  __TEXT.__gcc_except_tab: 0x560
   __TEXT.__dlopen_cstrs: 0x22d
   __TEXT.__ustring: 0x10
-  __TEXT.__constg_swiftt: 0x439c
-  __TEXT.__swift5_typeref: 0x111ca
-  __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0x376a
-  __TEXT.__swift5_fieldmd: 0x3824
-  __TEXT.__swift5_assocty: 0xd30
-  __TEXT.__swift5_capture: 0x21e4
-  __TEXT.__swift5_proto: 0x7b8
-  __TEXT.__swift5_types: 0x394
-  __TEXT.__swift_as_entry: 0x450
-  __TEXT.__swift_as_ret: 0x384
-  __TEXT.__swift5_protos: 0x40
+  __TEXT.__constg_swiftt: 0x45e4
+  __TEXT.__swift5_typeref: 0x114c4
+  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_reflstr: 0x38da
+  __TEXT.__swift5_fieldmd: 0x3a58
+  __TEXT.__swift5_assocty: 0xdd8
+  __TEXT.__swift5_capture: 0x2214
+  __TEXT.__swift5_proto: 0x834
+  __TEXT.__swift5_types: 0x3c0
+  __TEXT.__swift_as_entry: 0x470
+  __TEXT.__swift_as_ret: 0x3a4
+  __TEXT.__swift5_protos: 0x44
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x6110
-  __TEXT.__eh_frame: 0x97bc
+  __TEXT.__unwind_info: 0x6370
+  __TEXT.__eh_frame: 0x9bf0
   __TEXT.__objc_classname: 0x8a8
-  __TEXT.__objc_methname: 0xac37
+  __TEXT.__objc_methname: 0xacc0
   __TEXT.__objc_methtype: 0x265a
-  __TEXT.__objc_stubs: 0x7040
-  __DATA_CONST.__got: 0x1738
+  __TEXT.__objc_stubs: 0x7020
+  __DATA_CONST.__got: 0x1758
   __DATA_CONST.__const: 0x1230
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3000
+  __DATA_CONST.__objc_selrefs: 0x3028
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1c30
-  __AUTH_CONST.__const: 0x9350
-  __AUTH_CONST.__cfstring: 0x25a0
-  __AUTH_CONST.__objc_const: 0x16380
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x1c60
+  __AUTH_CONST.__const: 0x9808
+  __AUTH_CONST.__cfstring: 0x2540
+  __AUTH_CONST.__objc_const: 0x16520
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x3c50
-  __AUTH.__data: 0x3970
+  __AUTH.__objc_data: 0x3ee8
+  __AUTH.__data: 0x3a90
   __DATA.__objc_ivar: 0x364
-  __DATA.__data: 0x4f38
-  __DATA.__bss: 0xf670
-  __DATA.__common: 0x288
+  __DATA.__data: 0x50a8
+  __DATA.__bss: 0x10500
+  __DATA.__common: 0x2a0
   __DATA_DIRTY.__objc_data: 0xb80
-  __DATA_DIRTY.__data: 0x418
+  __DATA_DIRTY.__data: 0x428
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/LiftUI.framework/LiftUI
   - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
+  - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 234A6D4C-8AB0-3815-8CD8-85721E64BC18
-  Functions: 7914
-  Symbols:   7682
-  CStrings:  4388
+  UUID: 44AD85C7-5110-3869-8E8D-8F3239143077
+  Functions: 8120
+  Symbols:   7748
+  CStrings:  4435
 
Symbols:
+ +[ISImageDescriptor(Apperance) ics_appearanceVariantForTraitCollection:]
+ +[ISImageDescriptor(Apperance) ics_imageApperanceForColorForTraitCollection:]
+ +[ISImageDescriptor(Apperance) ics_imageApperanceForTraitCollection:]
+ +[ISImageDescriptor(Apperance) ics_tintColorForTraitCollection:]
+ -[ICSBackupViewController isRapidReturnToService]
+ -[ICSDataclassDetailSpecifierProvider _iconForDataclass:].cold.1
+ GCC_except_table109
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table79
+ _OBJC_CLASS_$_MDMConfiguration
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$__TtC14iCloudSettings23SettingsPlacardCellKeys
+ _OBJC_CLASS_$__TtC14iCloudSettings25BackupSettingsPlacardCell
+ _OBJC_CLASS_$__TtC14iCloudSettings28PasswordsSettingsPlacardCell
+ _OBJC_METACLASS_$__TtC14iCloudSettings23SettingsPlacardCellKeys
+ _OBJC_METACLASS_$__TtC14iCloudSettings25BackupSettingsPlacardCell
+ _OBJC_METACLASS_$__TtC14iCloudSettings28PasswordsSettingsPlacardCell
+ __CLASS_METHODS__TtC14iCloudSettings23SettingsPlacardCellKeys
+ __CLASS_PROPERTIES__TtC14iCloudSettings23SettingsPlacardCellKeys
+ __DATA__TtC14iCloudSettings23SettingsPlacardCellKeys
+ __DATA__TtC14iCloudSettings25BackupSettingsPlacardCell
+ __DATA__TtC14iCloudSettings28PasswordsSettingsPlacardCell
+ __DATA__TtC14iCloudSettings37ManageStorageDrilldownAnalyticsAction
+ __INSTANCE_METHODS__TtC14iCloudSettings23SettingsPlacardCellKeys
+ __INSTANCE_METHODS__TtC14iCloudSettings25BackupSettingsPlacardCell
+ __INSTANCE_METHODS__TtC14iCloudSettings28PasswordsSettingsPlacardCell
+ __IVARS__TtC14iCloudSettings37ManageStorageDrilldownAnalyticsAction
+ __METACLASS_DATA__TtC14iCloudSettings23SettingsPlacardCellKeys
+ __METACLASS_DATA__TtC14iCloudSettings25BackupSettingsPlacardCell
+ __METACLASS_DATA__TtC14iCloudSettings28PasswordsSettingsPlacardCell
+ __METACLASS_DATA__TtC14iCloudSettings37ManageStorageDrilldownAnalyticsAction
+ __PROTOCOLS_ICSManageStorageDrilldownController.51
+ ___38-[ICSBackupViewController startBackup]_block_invoke.606
+ ___38-[ICSBackupViewController startBackup]_block_invoke.608
+ ___41-[ICSBackupViewController cancelRestore:]_block_invoke.603
+ ___42-[ICSBackupViewController updateBusyState]_block_invoke.590
+ ___47-[ICSBackupViewController _fetchiCloudHomeData]_block_invoke.635
+ ___54-[ICSBackupViewController _setBackupEnabled:passcode:]_block_invoke.444
+ ___54-[ICSBackupViewController _setBackupEnabled:passcode:]_block_invoke.445
+ ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.453
+ ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.453.cold.1
+ ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.455
+ ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.455.cold.1
+ ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.481
+ ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.482
+ ___block_literal_global.611
+ ___swift_memcpy104_8
+ _associated conformance 14iCloudSettings33ManageStorageDrilldownActionEventV0F0OSHAASQ
+ _associated conformance 14iCloudSettings34ManageStorageAppAnimationImageViewV06SymbolH10CodingKeys33_09731684779CF4B95EC43794C80EA962LLOSHAASQ
+ _associated conformance 14iCloudSettings34ManageStorageAppAnimationImageViewV06SymbolH10CodingKeys33_09731684779CF4B95EC43794C80EA962LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 14iCloudSettings34ManageStorageAppAnimationImageViewV06SymbolH10CodingKeys33_09731684779CF4B95EC43794C80EA962LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 14iCloudSettings34ManageStorageAppAnimationImageViewV6LiftUI010ModifiableH0AA1VAdEP_05SwiftJ00H0
+ _associated conformance 14iCloudSettings34ManageStorageAppAnimationImageViewV6LiftUI03AnyH7ContentAASe
+ _associated conformance 14iCloudSettings34ManageStorageAppAnimationImageViewV6LiftUI03AnyH7ContentAaD16StringIdentified
+ _associated conformance 14iCloudSettings34ManageStorageAppAnimationImageViewV7SwiftUI0H0AA4BodyAdEP_AdE
+ _associated conformance 14iCloudSettings37ManageStorageDrilldownAnalyticsActionC10CodingKeys33_83B533DEC73D4D6934FC7B38042835E2LLOSHAASQ
+ _associated conformance 14iCloudSettings37ManageStorageDrilldownAnalyticsActionC10CodingKeys33_83B533DEC73D4D6934FC7B38042835E2LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 14iCloudSettings37ManageStorageDrilldownAnalyticsActionC10CodingKeys33_83B533DEC73D4D6934FC7B38042835E2LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 14iCloudSettings37ManageStorageDrilldownAnalyticsActionC6LiftUI06RemoteG0AaD15ContentModifier
+ _associated conformance 14iCloudSettings37ManageStorageDrilldownAnalyticsActionC6LiftUI15ContentModifierAASe
+ _associated conformance So38UIApplicationOpenExternalURLOptionsKeyaSHSCSQ
+ _associated conformance So38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper.221
+ _block_copy_helper.228
+ _block_copy_helper.251
+ _block_copy_helper.255
+ _block_copy_helper.259
+ _block_copy_helper.289
+ _block_copy_helper.303
+ _block_copy_helper.307
+ _block_copy_helper.323
+ _block_copy_helper.338
+ _block_copy_helper.355
+ _block_copy_helper.365
+ _block_copy_helper.382
+ _block_copy_helper.385
+ _block_copy_helper.388
+ _block_copy_helper.59
+ _block_descriptor.223
+ _block_descriptor.230
+ _block_descriptor.253
+ _block_descriptor.257
+ _block_descriptor.261
+ _block_descriptor.291
+ _block_descriptor.305
+ _block_descriptor.309
+ _block_descriptor.325
+ _block_descriptor.340
+ _block_descriptor.357
+ _block_descriptor.367
+ _block_descriptor.384
+ _block_descriptor.387
+ _block_descriptor.390
+ _block_descriptor.61
+ _block_destroy_helper.222
+ _block_destroy_helper.229
+ _block_destroy_helper.252
+ _block_destroy_helper.256
+ _block_destroy_helper.260
+ _block_destroy_helper.290
+ _block_destroy_helper.304
+ _block_destroy_helper.308
+ _block_destroy_helper.324
+ _block_destroy_helper.339
+ _block_destroy_helper.356
+ _block_destroy_helper.366
+ _block_destroy_helper.383
+ _block_destroy_helper.386
+ _block_destroy_helper.389
+ _block_destroy_helper.60
+ _get_enum_tag_for_layout_string 7SwiftUI11EnvironmentV7ContentOy14iCloudSettings25ManageStorageAppViewModelCSg_G
+ _get_witness_table 7SwiftUI5ImageVSgAA4ViewHpAcaEHPyHC_HC.6
+ _get_witness_table 7SwiftUI7SectionVyAA9EmptyViewVAA0E0PAAE8staticIf_4then4elseQrqd___qd_0_xXEqd_1_xXEtAA0E14InputPredicateRd__AaFRd_0_AaFRd_1_r1_lFQOyAgAE11buttonStyleyQrqd__AA015PrimitiveButtonM0Rd__lFQOyAA6VStackVyAA05TupleE0VyAA15ModifiedContentVyASyAA0O0VyAA012_ConditionalS0VyAOyAQyAA6HStackVyAQyASyASyAA6CircleVAA12_FrameLayoutVGAA011_ForegroundM8ModifierVyAA5ColorVGG_ASyAA4TextVAA023AccessibilityAttachmentZ0VGAA6SpacerVtGG_AYyAQyA13__A15_ASyASyASyAA5ImageVAA022_EnvironmentKeyWritingZ0VyA19_5ScaleOGGA21_yAA4FontVSgGGA21_yA6_SgGGtGGtGGAYyAQyA8__A13_A15_A13_A33_tGGGGA12_GAA08_PaddingX0VG_ASyA13_A44_GSg14iCloudSettings11SixPackGridVyA48_24iCloudDataclassCardModelCGtGG_AA010BorderlessoM0VQo__AA8SolariumVASyA58_A44_GA61_Qo_ASy019CloudRecommendationB020TurnOnMoreAppsFooterVA12_GSgGAaFHPAeaFHPyHC_qd0__AaFHD5_A62_HOA67_AaFHpA66_AaFHPA65_AaFHPyHC_A12_AA0eZ0HPyHCHC_HCHC.31
+ _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE15navigationTitleyQrqd__SyRd__lFQOyAA4ListVys5NeverOAA05TupleC0VyAA7SectionVyAA05EmptyC0VAA15ModifiedContentVyAA6ToggleVyAA5LabelVyAA6HStackVyAJyAA4TextV_AA6SpacerVtGG014_IconServices_aB005AsyncR5ImageVyAA0U0VGGGAA32_EnvironmentKeyTransformModifierVySbGGAXG_ALyAnRyA0_GAXGtGG_SSQo_HO.18
+ _keypath_set.82Tm
+ _objc_msgSend$acui_applicationBundleIdentifierForDataclass:
+ _objc_msgSend$acui_typedIconIdentifierForDataclass:
+ _objc_msgSend$graphicIconWithIdentifier:size:
+ _objc_msgSend$graphicIconWithType:size:
+ _objc_msgSend$iconWithBundleId:size:
+ _objc_msgSend$ics_imageApperanceForColorForTraitCollection:
+ _objc_msgSend$isRapidReturnToService
+ _objc_msgSend$policyPreventsBackups
+ _objc_msgSend$tableIconWithType:
+ _objc_release_x11
+ _objectdestroy.55Tm
+ _objectdestroy.57Tm
+ _symbolic $s14iCloudSettings18TelemetryProvidingP
+ _symbolic SbSS_SDySSSo8NSObjectCGSgyctc
+ _symbolic So11PSTableCellC
+ _symbolic _____ 14iCloudSettings06BackupB11PlacardCellC
+ _symbolic _____ 14iCloudSettings09PasswordsB11PlacardCellC
+ _symbolic _____ 14iCloudSettings0B15PlacardCellKeysC
+ _symbolic _____ 14iCloudSettings17TelemetryProviderV
+ _symbolic _____ 14iCloudSettings33ManageStorageDrilldownActionEventV
+ _symbolic _____ 14iCloudSettings33ManageStorageDrilldownActionEventV0F0O
+ _symbolic _____ 14iCloudSettings34ManageStorageAppAnimationImageViewV
+ _symbolic _____ 14iCloudSettings34ManageStorageAppAnimationImageViewV06SymbolH10CodingKeys33_09731684779CF4B95EC43794C80EA962LLO
+ _symbolic _____ 14iCloudSettings37ManageStorageDrilldownAnalyticsActionC
+ _symbolic _____ 14iCloudSettings37ManageStorageDrilldownAnalyticsActionC10CodingKeys33_83B533DEC73D4D6934FC7B38042835E2LLO
+ _symbolic _____ So38UIApplicationOpenExternalURLOptionsKeya
+ _symbolic ______p 14iCloudSettings18TelemetryProvidingP
+ _symbolic ______ypt So38UIApplicationOpenExternalURLOptionsKeya
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14iCloudSettings34ManageStorageAppAnimationImageViewV06SymbolK10CodingKeys33_09731684779CF4B95EC43794C80EA962LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14iCloudSettings37ManageStorageDrilldownAnalyticsActionC10CodingKeys33_83B533DEC73D4D6934FC7B38042835E2LLO
+ _symbolic _____y______Qo_ 6LiftUI14AnyViewContentPAA05SwiftB00D0RzrlE4bodyQrvpQO 14iCloudSettings030ManageStorageAppAnimationImageD0V
+ _symbolic _____y__________y_____y__________y_____y_____y_____yACy___________tGG_____y_____GGG_____ySbGGAJG_ADyAeGyAMGAJGtGG 7SwiftUI4ListV s5NeverO AA9TupleViewV AA7SectionV AA05EmptyF0V AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA4TextV AA6SpacerV 014_IconServices_aB005AsyncP5ImageV AA0S0V AA32_EnvironmentKeyTransformModifierV
+ _symbolic _____y__________y_____y_____y_____y_____yAEy_____y_____yACyADy_____yADyAEyAEy__________G_____y_____GG_AEy__________G_____tGG_AHyADyAR_AsEyAEyAEy__________y_____GGAWy_____SgGGAWyAMSgGGtGGtGGAHyADyAO_ArsRA5_tGGGGAQG_____G_AEyARA15_GSg_____y_____GtGG______Qo_______AEyA25_A15_GA27_Qo_AEy_____AQGSgG 7SwiftUI7SectionV AA9EmptyViewV AA0E0PAAE8staticIf_4then4elseQrqd___qd_0_xXEqd_1_xXEtAA0E14InputPredicateRd__AaFRd_0_AaFRd_1_r1_lFQO AgAE11buttonStyleyQrqd__AA015PrimitiveButtonM0Rd__lFQO AA6VStackV AA05TupleE0V AA15ModifiedContentV AA0O0V AA012_ConditionalS0V AA6HStackV AA6CircleV AA12_FrameLayoutV AA011_ForegroundM8ModifierV AA5ColorV AA4TextV AA023AccessibilityAttachmentZ0V AA6SpacerV AA5ImageV AA022_EnvironmentKeyWritingZ0V A13_5ScaleO AA4FontV AA08_PaddingX0V 14iCloudSettings11SixPackGridV A22_24iCloudDataclassCardModelC AA010BorderlessoM0V AA8SolariumV 019CloudRecommendationB020TurnOnMoreAppsFooterV
+ _symbolic _____y__________y_____y_____y_____y_____y___________tGG_____y_____GGG_____ySbGGAHG 7SwiftUI7SectionV AA9EmptyViewV AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA05TupleE0V AA4TextV AA6SpacerV 014_IconServices_aB005AsyncN5ImageV AA0Q0V AA32_EnvironmentKeyTransformModifierV
+ _symbolic _____y__________y_____y_____y_____y_____y___________tGG_____y_____GGG_____ySbGGAHG_AAyAbDyAKGAHGt 7SwiftUI7SectionV AA9EmptyViewV AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA05TupleE0V AA4TextV AA6SpacerV 014_IconServices_aB005AsyncN5ImageV AA0Q0V AA32_EnvironmentKeyTransformModifierV
+ _symbolic _____y_____y_____GG 8Settings0A11PlacardViewV 21_IconServices_SwiftUI05AsyncD5ImageV 0fG00I0V
+ _symbolic _____y_____y__________y_____y__________y_____y_____y_____yACy___________tGG_____y_____GGG_____ySbGGAJG_ADyAeGyAMGAJGtGG_SSQo_ 7SwiftUI4ViewPAAE15navigationTitleyQrqd__SyRd__lFQO AA4ListV s5NeverO AA05TupleC0V AA7SectionV AA05EmptyC0V AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA4TextV AA6SpacerV 014_IconServices_aB005AsyncR5ImageV AA0U0V AA32_EnvironmentKeyTransformModifierV
+ _symbolic _____y_____y__________y_____y_____y_____yAAy___________tGG_____y_____GGG_____ySbGGAHG_AByAcEyAKGAHGtG 7SwiftUI9TupleViewV AA7SectionV AA05EmptyD0V AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA4TextV AA6SpacerV 014_IconServices_aB005AsyncN5ImageV AA0Q0V AA32_EnvironmentKeyTransformModifierV
+ _symbolic _____y_____y_____y_____GG_____G 7SwiftUI22UIHostingConfigurationV 8Settings0E11PlacardViewV 014_IconServices_aB005AsyncH5ImageV AA0K0V AA05EmptyG0V
+ _symbolic _____y_____y_____y___________tGG_____y_____GG 7SwiftUI5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV 014_IconServices_aB005AsyncI5ImageV AA0L0V
+ _symbolic _____y_____y_____y_____yAAyAAy_____y_____yAByACy_____yACyAAyAAy__________G_____y_____GG_AAy__________G_____tGG_AFyACyAP_AqAyAAyAAy__________y_____GGAUy_____SgGGAUyAKSgGGtGGtGGAFyACyAM_ApqPA3_tGGGGAOG_____G_AAyAPA13_GSg_____y_____GtGG______Qo_A13_G 7SwiftUI15ModifiedContentV AA4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonG0Rd__lFQO AA6VStackV AA05TupleE0V AA0I0V AA012_ConditionalD0V AA6HStackV AA6CircleV AA12_FrameLayoutV AA011_ForegroundG8ModifierV AA5ColorV AA4TextV AA023AccessibilityAttachmentR0V AA6SpacerV AA5ImageV AA022_EnvironmentKeyWritingR0V A5_5ScaleO AA4FontV AA08_PaddingP0V 14iCloudSettings11SixPackGridV A14_24iCloudDataclassCardModelC AA010BorderlessiG0V
+ _symbolic _____y_____y_____y_____yACy_____y_____yAAyABy_____yAByACyACy__________G_____y_____GG_ACy__________G_____tGG_AFyAByAP_AqCyACyACy__________y_____GGAUy_____SgGGAUyAKSgGGtGGtGGAFyAByAM_ApqPA3_tGGGGAOG_____G_ACyAPA13_GSg_____y_____GtGG______Qo_ 7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonE0Rd__lFQO AA6VStackV AA05TupleC0V AA15ModifiedContentV AA0G0V AA012_ConditionalK0V AA6HStackV AA6CircleV AA12_FrameLayoutV AA011_ForegroundE8ModifierV AA5ColorV AA4TextV AA023AccessibilityAttachmentR0V AA6SpacerV AA5ImageV AA022_EnvironmentKeyWritingR0V A5_5ScaleO AA4FontV AA08_PaddingP0V 14iCloudSettings11SixPackGridV A14_24iCloudDataclassCardModelC AA010BorderlessgE0V
+ _symbolic _____y_____y_____y_____y___________tGG_____y_____GGG 7SwiftUI6ToggleV AA5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV 014_IconServices_aB005AsyncJ5ImageV AA0M0V
+ _symbolic _____y_____y_____y_____y_____yACy_____y_____yAAyABy_____yAByACyACy__________G_____y_____GG_ACy__________G_____tGG_AFyAByAP_AqCyACyACy__________y_____GGAUy_____SgGGAUyAKSgGGtGGtGGAFyAByAM_ApqPA3_tGGGGAOG_____G_ACyAPA13_GSg_____y_____GtGG______Qo_______ACyA23_A13_GA25_Qo_ 7SwiftUI4ViewPAAE8staticIf_4then4elseQrqd___qd_0_xXEqd_1_xXEtAA0C14InputPredicateRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE11buttonStyleyQrqd__AA015PrimitiveButtonK0Rd__lFQO AA6VStackV AA05TupleC0V AA15ModifiedContentV AA0M0V AA012_ConditionalQ0V AA6HStackV AA6CircleV AA12_FrameLayoutV AA011_ForegroundK8ModifierV AA5ColorV AA4TextV AA023AccessibilityAttachmentX0V AA6SpacerV AA5ImageV AA022_EnvironmentKeyWritingX0V A9_5ScaleO AA4FontV AA08_PaddingV0V 14iCloudSettings11SixPackGridV A18_24iCloudDataclassCardModelC AA010BorderlessmK0V AA8SolariumV
+ _symbolic _____y_____y_____y_____y_____y___________tGG_____y_____GGG_____ySbGG 7SwiftUI15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV 014_IconServices_aB005AsyncL5ImageV AA0O0V AA32_EnvironmentKeyTransformModifierV
+ _symbolic _____y_____ypG s18_DictionaryStorageC So38UIApplicationOpenExternalURLOptionsKeya
+ _type_layout_string 14iCloudSettings17TelemetryProviderV
+ _type_layout_string 14iCloudSettings33ManageStorageDrilldownActionEventV
+ _type_layout_string 14iCloudSettings34ManageStorageAppAnimationImageViewV
- +[ISImageDescriptor(Apperance) ics_appearanceVariant]
- +[ISImageDescriptor(Apperance) ics_imageApperanceForColor]
- +[ISImageDescriptor(Apperance) ics_imageApperance]
- +[ISImageDescriptor(Apperance) ics_tintColor]
- GCC_except_table108
- GCC_except_table40
- GCC_except_table44
- GCC_except_table78
- _OBJC_CLASS_$_AAUIDataclassSpecifierCell
- __PROTOCOLS_ICSManageStorageDrilldownController.50
- ___38-[ICSBackupViewController startBackup]_block_invoke.613
- ___38-[ICSBackupViewController startBackup]_block_invoke.615
- ___41-[ICSBackupViewController cancelRestore:]_block_invoke.610
- ___42-[ICSBackupViewController updateBusyState]_block_invoke.597
- ___47-[ICSBackupViewController _fetchiCloudHomeData]_block_invoke.642
- ___54-[ICSBackupViewController _setBackupEnabled:passcode:]_block_invoke.455
- ___54-[ICSBackupViewController _setBackupEnabled:passcode:]_block_invoke.456
- ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.465
- ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.465.cold.1
- ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.491
- ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke.492
- ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke_2
- ___66-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke_2.cold.1
- ___block_literal_global.618
- _block_copy_helper.209
- _block_copy_helper.216
- _block_copy_helper.22
- _block_copy_helper.235
- _block_copy_helper.239
- _block_copy_helper.243
- _block_copy_helper.277
- _block_copy_helper.291
- _block_copy_helper.295
- _block_copy_helper.311
- _block_copy_helper.326
- _block_copy_helper.343
- _block_copy_helper.353
- _block_copy_helper.370
- _block_copy_helper.373
- _block_copy_helper.376
- _block_copy_helper.45
- _block_copy_helper.55
- _block_descriptor.211
- _block_descriptor.218
- _block_descriptor.237
- _block_descriptor.24
- _block_descriptor.241
- _block_descriptor.245
- _block_descriptor.279
- _block_descriptor.293
- _block_descriptor.297
- _block_descriptor.313
- _block_descriptor.328
- _block_descriptor.345
- _block_descriptor.355
- _block_descriptor.372
- _block_descriptor.375
- _block_descriptor.378
- _block_descriptor.47
- _block_descriptor.57
- _block_destroy_helper.210
- _block_destroy_helper.217
- _block_destroy_helper.23
- _block_destroy_helper.236
- _block_destroy_helper.240
- _block_destroy_helper.244
- _block_destroy_helper.278
- _block_destroy_helper.292
- _block_destroy_helper.296
- _block_destroy_helper.312
- _block_destroy_helper.327
- _block_destroy_helper.344
- _block_destroy_helper.354
- _block_destroy_helper.371
- _block_destroy_helper.374
- _block_destroy_helper.377
- _block_destroy_helper.46
- _block_destroy_helper.56
- _get_witness_table 7SwiftUI7SectionVyAA9EmptyViewVAA0E0PAAE8staticIf_4then4elseQrqd___qd_0_xXEqd_1_xXEtAA0E14InputPredicateRd__AaFRd_0_AaFRd_1_r1_lFQOyAA6VStackVyAA05TupleE0VyAA15ModifiedContentVyAQyAA6ButtonVyAA012_ConditionalO0VyAMyAOyAA6HStackVyAOyAQyAQyAA6CircleVAA12_FrameLayoutVGAA24_ForegroundStyleModifierVyAA5ColorVGG_AQyAA4TextVAA023AccessibilityAttachmentX0VGAA6SpacerVtGG_AWyAOyA11__A13_AQyAQyAQyAA5ImageVAA022_EnvironmentKeyWritingX0VyA17_5ScaleOGGA19_yAA4FontVSgGGA19_yA4_SgGGtGGtGGAWyAOyA6__A11_A13_A11_A31_tGGGGA10_GAA08_PaddingU0VG_AQyA11_A42_GSg14iCloudSettings11SixPackGridVyA46_24iCloudDataclassCardModelCGtGG_AA8SolariumVAQyA53_A42_GA56_Qo_AQy019CloudRecommendationB020TurnOnMoreAppsFooterVA10_GSgGAaFHPAeaFHPyHC_qd0__AaFHD5_A57_HOA62_AaFHpA61_AaFHPA60_AaFHPyHC_A10_AA0eX0HPyHCHC_HCHC.30
- _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE15navigationTitleyQrqd__SyRd__lFQOyAA4ListVys5NeverOAA05TupleC0VyAA7SectionVyAA05EmptyC0VAA15ModifiedContentVyAA6ToggleVyAA5LabelVyAA6HStackVyAJyAA4TextV_AA6SpacerVtGGAA5ImageVGGAA32_EnvironmentKeyTransformModifierVySbGGAXG_ALyAnRyA0_GAXGtGG_SSQo_HO.18
- _keypath_set.86Tm
- _objc_msgSend$acui_iconForDataclass:
- _objc_msgSend$currentTraitCollection
- _objc_msgSend$graphicIconWithType:size:scale:
- _objc_msgSend$iconWithType:size:drawBorder:
- _objc_msgSend$ics_imageApperanceForColor
- _objc_msgSend$imageForDataclassWithBundleID:
- _objc_msgSend$imageForDataclassWithType:
- _objc_msgSend$mainScreen
- _objc_msgSend$scale
- _objc_msgSend$tableIconWithType:drawBorder:
- _objectdestroy.56Tm
- _objectdestroy.59Tm
- _objectdestroy.92Tm
- _symbolic _____y__________y_____y__________y_____y_____y_____yACy___________tGG_____GG_____ySbGGAJG_ADyAeGyAMGAJGtGG 7SwiftUI4ListV s5NeverO AA9TupleViewV AA7SectionV AA05EmptyF0V AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA4TextV AA6SpacerV AA5ImageV AA32_EnvironmentKeyTransformModifierV
- _symbolic _____y__________y_____y_____y_____yAEy_____y_____yACyADy_____yADyAEyAEy__________G_____y_____GG_AEy__________G_____tGG_AHyADyAR_AsEyAEyAEy__________y_____GGAWy_____SgGGAWyAMSgGGtGGtGGAHyADyAO_ArsRA5_tGGGGAQG_____G_AEyARA15_GSg_____y_____GtGG______AEyA23_A15_GA25_Qo_AEy_____AQGSgG 7SwiftUI7SectionV AA9EmptyViewV AA0E0PAAE8staticIf_4then4elseQrqd___qd_0_xXEqd_1_xXEtAA0E14InputPredicateRd__AaFRd_0_AaFRd_1_r1_lFQO AA6VStackV AA05TupleE0V AA15ModifiedContentV AA6ButtonV AA012_ConditionalO0V AA6HStackV AA6CircleV AA12_FrameLayoutV AA24_ForegroundStyleModifierV AA5ColorV AA4TextV AA023AccessibilityAttachmentX0V AA6SpacerV AA5ImageV AA022_EnvironmentKeyWritingX0V A11_5ScaleO AA4FontV AA08_PaddingU0V 14iCloudSettings11SixPackGridV A20_24iCloudDataclassCardModelC AA8SolariumV 019CloudRecommendationB020TurnOnMoreAppsFooterV
- _symbolic _____y__________y_____y_____y_____y_____y___________tGG_____GG_____ySbGGAHG 7SwiftUI7SectionV AA9EmptyViewV AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA05TupleE0V AA4TextV AA6SpacerV AA5ImageV AA32_EnvironmentKeyTransformModifierV
- _symbolic _____y__________y_____y_____y_____y_____y___________tGG_____GG_____ySbGGAHG_AAyAbDyAKGAHGt 7SwiftUI7SectionV AA9EmptyViewV AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA05TupleE0V AA4TextV AA6SpacerV AA5ImageV AA32_EnvironmentKeyTransformModifierV
- _symbolic _____y_____y__________y_____y__________y_____y_____y_____yACy___________tGG_____GG_____ySbGGAJG_ADyAeGyAMGAJGtGG_SSQo_ 7SwiftUI4ViewPAAE15navigationTitleyQrqd__SyRd__lFQO AA4ListV s5NeverO AA05TupleC0V AA7SectionV AA05EmptyC0V AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA4TextV AA6SpacerV AA5ImageV AA32_EnvironmentKeyTransformModifierV
- _symbolic _____y_____y__________y_____y_____y_____yAAy___________tGG_____GG_____ySbGGAHG_AByAcEyAKGAHGtG 7SwiftUI9TupleViewV AA7SectionV AA05EmptyD0V AA15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA4TextV AA6SpacerV AA5ImageV AA32_EnvironmentKeyTransformModifierV
- _symbolic _____y_____y_____yAAyAAy_____y_____yAByACy_____yACyAAyAAy__________G_____y_____GG_AAy__________G_____tGG_AFyACyAP_AqAyAAyAAy__________y_____GGAUy_____SgGGAUyAKSgGGtGGtGGAFyACyAM_ApqPA3_tGGGGAOG_____G_AAyAPA13_GSg_____y_____GtGGA13_G 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA6ButtonV AA012_ConditionalD0V AA6HStackV AA6CircleV AA12_FrameLayoutV AA24_ForegroundStyleModifierV AA5ColorV AA4TextV AA023AccessibilityAttachmentP0V AA6SpacerV AA5ImageV AA022_EnvironmentKeyWritingP0V A1_5ScaleO AA4FontV AA08_PaddingM0V 14iCloudSettings11SixPackGridV A10_24iCloudDataclassCardModelC
- _symbolic _____y_____y_____y___________tGG_____G 7SwiftUI5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA5ImageV
- _symbolic _____y_____y_____y_____yACy_____y_____yAAyABy_____yAByACyACy__________G_____y_____GG_ACy__________G_____tGG_AFyAByAP_AqCyACyACy__________y_____GGAUy_____SgGGAUyAKSgGGtGGtGGAFyAByAM_ApqPA3_tGGGGAOG_____G_ACyAPA13_GSg_____y_____GtGG______ACyA21_A13_GA23_Qo_ 7SwiftUI4ViewPAAE8staticIf_4then4elseQrqd___qd_0_xXEqd_1_xXEtAA0C14InputPredicateRd__AaBRd_0_AaBRd_1_r1_lFQO AA6VStackV AA05TupleC0V AA15ModifiedContentV AA6ButtonV AA012_ConditionalM0V AA6HStackV AA6CircleV AA12_FrameLayoutV AA24_ForegroundStyleModifierV AA5ColorV AA4TextV AA023AccessibilityAttachmentV0V AA6SpacerV AA5ImageV AA022_EnvironmentKeyWritingV0V A7_5ScaleO AA4FontV AA08_PaddingS0V 14iCloudSettings11SixPackGridV A16_24iCloudDataclassCardModelC AA8SolariumV
- _symbolic _____y_____y_____y_____y___________tGG_____GG 7SwiftUI6ToggleV AA5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA5ImageV
- _symbolic _____y_____y_____y_____y_____y___________tGG_____GG_____ySbGG 7SwiftUI15ModifiedContentV AA6ToggleV AA5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA5ImageV AA32_EnvironmentKeyTransformModifierV
CStrings:
+ "%s  Failed to fetch graphic icon for identifier %s"
+ "%s Completed with success!"
+ "%s Entering backup dispatch queue"
+ "%s Entering main queue, hiding progressHUD, enabling interaction"
+ "%s Expected bundleId %s but it was not found"
+ "%s Failed to fetch graphic icon for bundleId %s"
+ "%s Failed to fetch graphic icon for type %s"
+ "%s IconServices may do I/O on main thread"
+ "%s account save complete"
+ "%s disabling user interaction"
+ "%s persist state complete, updating UI"
+ "%s reloading specifiers..."
+ "%s setBackupEnabled complete"
+ "%s setupBackupWithPasscode returned without error"
+ "%s showing progress HUD"
+ "%s starting account save"
+ "%s: %@"
+ "-[ICSBackupViewController _persistBackupEnablementState:passcode:]_block_invoke"
+ "-[ICSBackupViewController fetchIsBackupEnabled]"
+ "-[ICSBackupViewController setLastBackupDateString:]"
+ "@24@0:8q16"
+ "@40@0:8@16{CGSize=dd}24"
+ "@40@0:8q16{CGSize=dd}24"
+ "Backup is not allowed!"
+ "Error setting up backup with passcode: %@"
+ "ManageStorageApp.fetchLocalAnimationImage bundleId: %s"
+ "ManageStorageApp.fetchLocalAnimationImage graphicIcon: %s"
+ "ManageStorageApp.fetchLocalAnimationImage: no local image found"
+ "ManageStorageApp.fetchLocalTableImage graphicIcon: %s"
+ "ManageStorageApp.fetchLocalTableImage: local image, bundleId: %s"
+ "ManageStorageApp.fetchLocalTableImage: no local image found"
+ "ManageStorageApp.fetchRemoteAnimationImage using url: %s"
+ "ManageStorageApp.fetchRemoteTableImage: remote image, url: %s"
+ "ManageStorageAppAnimationImage"
+ "ManageStorageDrilldownAnalyticsAction performing action"
+ "Missing icon for dataclass %@"
+ "Omitting backup subtitle since policy doesn't allow backup"
+ "Rapid Return to Service: %d"
+ "Resolved values action: %s bundleId: %s"
+ "T@\"NSArray\",N,C"
+ "_TtC14iCloudSettings23SettingsPlacardCellKeys"
+ "_TtC14iCloudSettings25BackupSettingsPlacardCell"
+ "_TtC14iCloudSettings28PasswordsSettingsPlacardCell"
+ "_TtC14iCloudSettings37ManageStorageDrilldownAnalyticsAction"
+ "acui_applicationBundleIdentifierForDataclass:"
+ "acui_typedIconIdentifierForDataclass:"
+ "canOpenURL:"
+ "com.apple.iCloudSettings.manageStorage.drilldownAction"
+ "fetchRemoteAnimationImage(fallbackURL:)"
+ "graphicIcon(identifier:size:)"
+ "graphicIconWithIdentifier:size:"
+ "graphicIconWithType:size:"
+ "icon(bundleId:size:)"
+ "icon(type:size:)"
+ "iconWithBundleId:size:"
+ "ics_appearanceVariantForTraitCollection:"
+ "ics_imageApperanceForColorForTraitCollection:"
+ "ics_imageApperanceForTraitCollection:"
+ "ics_prepareImage(for:)"
+ "ics_tintColorForTraitCollection:"
+ "isMainThread"
+ "isRapidReturnToService"
+ "layoutMargins"
+ "msDrilldownAnalyticsAction"
+ "policyPreventsBackups"
+ "reviewRecentlyDeletedFiles"
+ "setBundleIds:"
+ "setSeparatorInset:"
+ "tableIcon(type:)"
+ "tableIconWithType:"
+ "telemetryProvider"
+ "viewiPhoneStorage"
- "@28@0:8q16B24"
- "@44@0:8q16{CGSize=dd}24B40"
- "@48@0:8@16{CGSize=dd}24d40"
- "@48@0:8q16{CGSize=dd}24d40"
- "Backup is allowed, setting backup info text"
- "Error setting up backup: %@"
- "Failed to fetch graphic icon for identifier %s"
- "Failed to recreate image using IconServices"
- "ManageStorageApp.loadAnimationImage: local image, bundleId: %s"
- "ManageStorageApp.loadAnimationImage: remote image, url: %s"
- "ManageStorageApp.loadImage: local image, bundleId: %s"
- "ManageStorageApp.loadImage: remote image, url: %s"
- "acui_iconForDataclass:"
- "appIconWithImage:drawBorder:"
- "graphicIconWithIdentifier:size:scale:"
- "graphicIconWithType:size:scale:"
- "iconWithType:size:drawBorder:"
- "ics_appearanceVariant"
- "ics_imageApperance"
- "ics_imageApperanceForColor"
- "ics_tintColor"
- "imageForDataclassWithBundleID:"
- "imageForDataclassWithType:"
- "loadAnimationImage(fallbackURL:)"
- "tableIconWithType:drawBorder:"

```
