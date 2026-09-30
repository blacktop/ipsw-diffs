## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/Versions/A/AppleAccountUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-583.0.0.0.0
-  __TEXT.__text: 0x601c4
-  __TEXT.__objc_methlist: 0xa74
-  __TEXT.__const: 0x55b4
-  __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__oslogstring: 0x129d
-  __TEXT.__cstring: 0x2150
-  __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__swift5_typeref: 0x688c
-  __TEXT.__swift5_reflstr: 0x1100
-  __TEXT.__swift5_assocty: 0x608
-  __TEXT.__constg_swiftt: 0x21c8
-  __TEXT.__swift5_fieldmd: 0x11c4
-  __TEXT.__swift5_proto: 0x1f8
-  __TEXT.__swift5_types: 0x178
+584.0.0.0.0
+  __TEXT.__text: 0x6aad4
+  __TEXT.__objc_methlist: 0xad4
+  __TEXT.__const: 0x5c94
+  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__oslogstring: 0x136d
+  __TEXT.__cstring: 0x24c0
+  __TEXT.__dlopen_cstrs: 0xa2
+  __TEXT.__swift5_typeref: 0x70aa
+  __TEXT.__swift5_reflstr: 0x12f0
+  __TEXT.__swift5_assocty: 0x638
+  __TEXT.__constg_swiftt: 0x251c
+  __TEXT.__swift5_fieldmd: 0x1304
+  __TEXT.__swift5_proto: 0x20c
+  __TEXT.__swift5_types: 0x184
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_capture: 0x634
-  __TEXT.__swift_as_entry: 0x90
-  __TEXT.__swift_as_ret: 0x7c
-  __TEXT.__swift_as_cont: 0xe4
+  __TEXT.__swift5_capture: 0x73c
+  __TEXT.__swift_as_entry: 0xb8
+  __TEXT.__swift_as_ret: 0xa0
+  __TEXT.__swift_as_cont: 0x110
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x1de8
-  __TEXT.__eh_frame: 0x1550
+  __TEXT.__unwind_info: 0x2160
+  __TEXT.__eh_frame: 0x1ab0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3f8
-  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc28
+  __DATA_CONST.__objc_selrefs: 0xcd0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x640
-  __AUTH_CONST.__const: 0x3030
+  __DATA_CONST.__got: 0x670
+  __AUTH_CONST.__const: 0x3540
   __AUTH_CONST.__cfstring: 0x10e0
-  __AUTH_CONST.__objc_const: 0x2a00
+  __AUTH_CONST.__objc_const: 0x2d88
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x1250
-  __AUTH.__objc_data: 0xe18
-  __AUTH.__data: 0x1bf0
-  __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x1690
-  __DATA.__bss: 0x4838
+  __AUTH_CONST.__auth_got: 0x12c0
+  __AUTH.__objc_data: 0xeb8
+  __AUTH.__data: 0x1fd0
+  __DATA.__objc_ivar: 0x44
+  __DATA.__data: 0x1848
+  __DATA.__bss: 0x4ad8
   __DATA.__common: 0x4a8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/ContactsUICore.framework/Versions/A/ContactsUICore
   - /System/Library/PrivateFrameworks/CoreCDP.framework/Versions/A/CoreCDP
   - /System/Library/PrivateFrameworks/CoreCDPUI.framework/Versions/A/CoreCDPUI
+  - /System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/Versions/A/IMSharedUtilities

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2880
-  Symbols:   1787
-  CStrings:  368
+  Functions: 3144
+  Symbols:   1894
+  CStrings:  394
 
Symbols:
+ -[AAUIContactsProvider .cxx_destruct]
+ -[AAUIContactsProvider _fetchImageDataForLocalContact:ofSize:withCompletion:]
+ -[AAUIContactsProvider _fetchImagesForContacts:ofSize:completion:]
+ -[AAUIContactsProvider _fetchServerImageDataFor:WithCompletion:]
+ -[AAUIContactsProvider fetchSuggestedBeneficiariesWithImagesOfSize:andCompletion:]
+ -[AAUIContactsProvider fetchSuggestedCustodiansWithImagesOfSize:andCompletion:]
+ -[AAUIContactsProvider init]
+ FamilyCircleUILibraryCore.frameworkLibrary
+ GCC_except_table12
+ OBJC_IVAR_$_AAUIContactsProvider._contactsManager
+ _OBJC_CLASS_$_AAContactsManager
+ _OBJC_CLASS_$_AACustodianRecoveryRequestContext
+ _OBJC_CLASS_$_AAUIContactsProvider
+ _OBJC_CLASS_$_AIDAAccountManager
+ _OBJC_CLASS_$_FAFetchFamilyPhotoRequest
+ _OBJC_METACLASS_$_AAContactsProvider
+ _OBJC_METACLASS_$_AAUIContactsProvider
+ __66-[AAUIContactsProvider _fetchImagesForContacts:ofSize:completion:]_block_invoke
+ __DATA__TtC14AppleAccountUI38CustodianOwnerListViewServiceViewModel
+ __IVARS__TtC14AppleAccountUI38CustodianOwnerListViewServiceViewModel
+ __METACLASS_DATA__TtC14AppleAccountUI38CustodianOwnerListViewServiceViewModel
+ __OBJC_$_INSTANCE_METHODS_AAUIContactsProvider
+ __OBJC_$_INSTANCE_VARIABLES_AAUIContactsProvider
+ __OBJC_CLASS_RO_$_AAUIContactsProvider
+ __OBJC_METACLASS_RO_$_AAUIContactsProvider
+ ___64-[AAUIContactsProvider _fetchServerImageDataFor:WithCompletion:]_block_invoke
+ ___66-[AAUIContactsProvider _fetchImagesForContacts:ofSize:completion:]_block_invoke
+ ___77-[AAUIContactsProvider _fetchImageDataForLocalContact:ofSize:withCompletion:]_block_invoke
+ ___79-[AAUIContactsProvider fetchSuggestedCustodiansWithImagesOfSize:andCompletion:]_block_invoke
+ ___82-[AAUIContactsProvider fetchSuggestedBeneficiariesWithImagesOfSize:andCompletion:]_block_invoke
+ ___FamilyCircleUILibraryCore_block_invoke
+ ___block_descriptor_40_e8_32bs_e31_v32?0"NSData"8Q16"NSError"24l
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e16_v16?0"NSData"8l
+ ___block_descriptor_56_e8_32s40bs_e16_v16?0"NSData"8l
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSArray"8l
+ ___getFAProfilePictureStoreClass_block_invoke
+ __getFAProfilePictureStoreClass_block_invoke
+ __swift_closure_destructor.17Tm
+ _associated conformance 14AppleAccountUI029CustodianOwnerListViewServiceG0V05SwiftC00G0AA4BodyAdEP_AdE
+ _associated conformance 14AppleAccountUI029CustodianOwnerListViewServiceG5ModelCAA017OnboardingContentG0AA06CustomG0AaDP_05SwiftC00G0
+ _audit_stringFamilyCircleUI
+ _dispatch_get_global_queue
+ _objc_getClass
+ _objc_msgSend$_fetchImageDataForLocalContact:ofSize:withCompletion:
+ _objc_msgSend$_fetchImagesForContacts:ofSize:completion:
+ _objc_msgSend$_fetchServerImageDataFor:WithCompletion:
+ _objc_msgSend$contactForHandle:
+ _objc_msgSend$familyDSID
+ _objc_msgSend$firstNameOrHandleForDisplay
+ _objc_msgSend$generateCustodianRecoveryCodeWithContext:completion:
+ _objc_msgSend$initWithAccountStore:
+ _objc_msgSend$initWithFamilyMemberDSID:size:localFallback:
+ _objc_msgSend$profilePictureForContact:serverImageData:firstName:lastName:diameter:
+ _objc_msgSend$setCustodianUUID:
+ _objc_msgSend$setTelemetryFlowID:
+ _objc_msgSend$setTopImageTintColor:
+ _objc_msgSend$setUseMonogramAsLastResort:
+ _objc_msgSend$startRequestWithCompletionHandler:
+ _objc_msgSend$systemBlueColor
+ _objc_msgSend$thumbnailImageData
+ _objc_opt_new
+ _swift_allocError
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _symbolic IeyB_
+ _symbolic SccySS______pG s5ErrorP
+ _symbolic So18AALocalContactInfoCIegHg_
+ _symbolic So18AALocalContactInfoCSg
+ _symbolic So7NSColorC
+ _symbolic _____ 14AppleAccountUI029CustodianOwnerListViewServiceG0V
+ _symbolic _____ 14AppleAccountUI029CustodianOwnerListViewServiceG5ModelC
+ _symbolic _____Sg 14AppleAccountUI30CustodianOwnerRecoveryCodeViewV
+ _symbolic _____So18AALocalContactInfoCcSg 7SwiftUI7AnyViewV
+ _symbolic ___________y_____y_____ACG______Qo_AAt 7SwiftUI6SpacerV AA4ViewPAAE08progressD5StyleyQrqd__AA08ProgressdF0Rd__lFQO AA0gD0V AA05EmptyD0V AA08CirculargdF0V
+ _symbolic ______p s5ErrorP
+ _symbolic _____yAAyAAy_____y___________y_____y_____AEG______Qo_ACQPG_____GAAyA2EGG_____y_____GG 7SwiftUI19_ConditionalContentV AA05TupleD0V AA6SpacerV AA4ViewPAAE08progressG5StyleyQrqd__AA08ProgressgI0Rd__lFQO AA0jG0V AA05EmptyG0V AA08CircularjgI0V AA4TextV 012AppleAccountB0018TrustedContactListG0V AT014CustodianOwnerrg7ServiceG5ModelC
+ _symbolic _____yAAy_____y___________y_____y_____AEG______Qo_ACQPG_____GAAyA2EGG 7SwiftUI19_ConditionalContentV AA05TupleD0V AA6SpacerV AA4ViewPAAE08progressG5StyleyQrqd__AA08ProgressgI0Rd__lFQO AA0jG0V AA05EmptyG0V AA08CircularjgI0V AA4TextV
+ _symbolic _____y_____ABG 7SwiftUI12ProgressViewV AA05EmptyD0V
+ _symbolic _____y_____ABG 7SwiftUI19_ConditionalContentV AA9EmptyViewV
+ _symbolic _____y_____G 14AppleAccountUI14OnboardingViewV AA018CustodianOwnerListe7ServiceE5ModelC
+ _symbolic _____y_____G 14AppleAccountUI22TrustedContactListViewV AA014CustodianOwnerfg7ServiceG5ModelC
+ _symbolic _____y_____G 7SwiftUI19NSHostingControllerC 012AppleAccountB0029CustodianOwnerListViewServiceJ0V
+ _symbolic _____y___________y_____y_____ADG______Qo_ABQPG 7SwiftUI12TupleContentV AA6SpacerV AA4ViewPAAE08progressF5StyleyQrqd__AA08ProgressfH0Rd__lFQO AA0iF0V AA05EmptyF0V AA08CircularifH0V
+ _symbolic _____y__________y_____SgGG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV
+ _symbolic _____y__________y_____y_____y_____y_____y_____y_____G_____G______yytADy_____yADy__________y_____SgGGG_____GGSgQo_SiG_So18AALocalContactInfoC_____SgQo__SS_____yAKy_____G_Qo_A2_Qo_G 7SwiftUI15NavigationStackV AA0C4PathV AA4ViewPAAE5alert_11isPresented7actions7messageQrqd___AA7BindingVySbGqd_0_yXEqd_1_yXEtSyRd__AaFRd_0_AaFRd_1_r1_lFQO AgAE21navigationDestination4item11destinationQrAMyqd__SgG_qd_0_qd__ctSHRd__AaFRd_0_r0_lFQO AA6IDViewV AgAE7toolbar7contentQrqd__yXE_tAA14ToolbarContentRd__lFQO AA08ModifiedU0V 012AppleAccountB0010OnboardingF0V A_018CustodianOwnerListf7ServiceF5ModelC AA30_SafeAreaRegionsIgnoringLayoutV AA0T4ItemV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA31AccessibilityAttachmentModifierV A_0z17OwnerRecoveryCodeF0V AgAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA4TextV
+ _symbolic _____y_____yAAy__________y_____SgGGG_____G 7SwiftUI15ModifiedContentV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA023AccessibilityAttachmentJ0V
+ _symbolic _____y_____yABy_____y___________y_____y_____AFG______Qo_ADQPG_____GAByA2FGG_____y_____G_G 7SwiftUI19_ConditionalContentV7StorageO AC AA05TupleD0V AA6SpacerV AA4ViewPAAE08progressH5StyleyQrqd__AA08ProgresshJ0Rd__lFQO AA0kH0V AA05EmptyH0V AA08CircularkhJ0V AA4TextV 012AppleAccountB0018TrustedContactListH0V AV014CustodianOwnersh7ServiceH5ModelC
+ _symbolic _____y_____y_____ABG______Qo_ 7SwiftUI4ViewPAAE08progressC5StyleyQrqd__AA08ProgresscE0Rd__lFQO AA0fC0V AA05EmptyC0V AA08CircularfcE0V
+ _symbolic _____y_____y_____G_Qo_ 7SwiftUI4ViewPAAE16keyboardShortcutyQrAA08KeyboardE0VFQO AA6ButtonV AA4TextV
+ _symbolic _____y_____y_____G_____G 7SwiftUI15ModifiedContentV 012AppleAccountB014OnboardingViewV AD018CustodianOwnerListh7ServiceH5ModelC AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y_____y___________y_____y_____AEG______Qo_ACQPG_____G 7SwiftUI19_ConditionalContentV AA05TupleD0V AA6SpacerV AA4ViewPAAE08progressG5StyleyQrqd__AA08ProgressgI0Rd__lFQO AA0jG0V AA05EmptyG0V AA08CircularjgI0V AA4TextV
+ _symbolic _____y_____y___________y_____y_____AEG______Qo_ACQPG______G 7SwiftUI19_ConditionalContentV7StorageO AA05TupleD0V AA6SpacerV AA4ViewPAAE08progressH5StyleyQrqd__AA08ProgresshJ0Rd__lFQO AA0kH0V AA05EmptyH0V AA08CircularkhJ0V AA4TextV
+ _symbolic _____y_____y__________y_____SgGGG 7SwiftUI6ButtonV AA15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV
+ _symbolic _____y_____y__________y_____y_____y_____yAAy_____y_____G_____G______yytAAy_____yAAy__________y_____SgGGG_____GGSgQo_SiG_So18AALocalContactInfoC_____SgQo__SS_____yAKy_____G_Qo_A2_Qo_G_____G 7SwiftUI15ModifiedContentV AA15NavigationStackV AA0E4PathV AA4ViewPAAE5alert_11isPresented7actions7messageQrqd___AA7BindingVySbGqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQO AiAE21navigationDestination4item11destinationQrAOyqd__SgG_qd_0_qd__ctSHRd__AaHRd_0_r0_lFQO AA6IDViewV AiAE7toolbar7contentQrqd__yXE_tAA07ToolbarD0Rd__lFQO 012AppleAccountB0010OnboardingH0V A_018CustodianOwnerListh7ServiceH5ModelC AA30_SafeAreaRegionsIgnoringLayoutV AA0V4ItemV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA31AccessibilityAttachmentModifierV A_0z17OwnerRecoveryCodeH0V AiAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA4TextV AA14_TaskModifier2V
+ _symbolic _____y_____y__________y_____y_____y_____y_____y_____y_____G_____G______yytADy_____yADy__________y_____SgGGG_____GGSgQo_SiG_So18AALocalContactInfoC_____SgQo__SS_____yAKy_____G_Qo_A2_Qo_G_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15NavigationStackV AA0I4PathV AcAE5alert_11isPresented7actions7messageQrqd___AA7BindingVySbGqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE21navigationDestination4item11destinationQrASyqd__SgG_qd_0_qd__ctSHRd__AaBRd_0_r0_lFQO AA6IDViewV AcAE7toolbar7contentQrqd__yXE_tAA14ToolbarContentRd__lFQO AA08ModifiedZ0V 012AppleAccountB0010OnboardingC0V A5_018CustodianOwnerListc7ServiceC5ModelC AA30_SafeAreaRegionsIgnoringLayoutV AA0Y4ItemV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA31AccessibilityAttachmentModifierV A5_026CustodianOwnerRecoveryCodeC0V AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA4TextV
+ _symbolic _____y_____y_____y___________y_____y_____AFG______Qo_ADQPG_____GAByA2FG_G 7SwiftUI19_ConditionalContentV7StorageO AC AA05TupleD0V AA6SpacerV AA4ViewPAAE08progressH5StyleyQrqd__AA08ProgresshJ0Rd__lFQO AA0kH0V AA05EmptyH0V AA08CircularkhJ0V AA4TextV
+ _symbolic _____y_____y_____y_____y_____G_____G______yytABy_____yABy__________y_____SgGGG_____GGSgQo_SiG 7SwiftUI6IDViewV AA4ViewPAAE7toolbar7contentQrqd__yXE_tAA14ToolbarContentRd__lFQO AA08ModifiedH0V 012AppleAccountB0010OnboardingD0V AK018CustodianOwnerListd7ServiceD5ModelC AA30_SafeAreaRegionsIgnoringLayoutV AA0G4ItemV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA31AccessibilityAttachmentModifierV
+ _symbolic _____y_____y_____y_____y_____y_____G_____G______yytABy_____yABy__________y_____SgGGG_____GGSgQo_SiG_So18AALocalContactInfoC_____SgQo_ 7SwiftUI4ViewPAAE21navigationDestination4item11destinationQrAA7BindingVyqd__SgG_qd_0_qd__ctSHRd__AaBRd_0_r0_lFQO AA6IDViewV AcAE7toolbar7contentQrqd__yXE_tAA14ToolbarContentRd__lFQO AA08ModifiedM0V 012AppleAccountB0010OnboardingC0V AR018CustodianOwnerListc7ServiceC5ModelC AA30_SafeAreaRegionsIgnoringLayoutV AA0L4ItemV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA31AccessibilityAttachmentModifierV AR0rs12RecoveryCodeC0V
+ _symbolic _____y_____y_____y_____y_____y_____y_____G_____G______yytABy_____yABy__________y_____SgGGG_____GGSgQo_SiG_So18AALocalContactInfoC_____SgQo__SS_____yAIy_____G_Qo_A0_Qo_ 7SwiftUI4ViewPAAE5alert_11isPresented7actions7messageQrqd___AA7BindingVySbGqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE21navigationDestination4item11destinationQrAIyqd__SgG_qd_0_qd__ctSHRd__AaBRd_0_r0_lFQO AA6IDViewV AcAE7toolbar7contentQrqd__yXE_tAA14ToolbarContentRd__lFQO AA08ModifiedR0V 012AppleAccountB0010OnboardingC0V AW018CustodianOwnerListc7ServiceC5ModelC AA30_SafeAreaRegionsIgnoringLayoutV AA0Q4ItemV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA31AccessibilityAttachmentModifierV AW0wx12RecoveryCodeC0V AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA4TextV
+ _symbolic _____yyt_____y_____yABy__________y_____SgGGG_____GG 7SwiftUI11ToolbarItemV AA15ModifiedContentV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA023AccessibilityAttachmentL0V
+ _symbolic _____yyt_____y_____yABy__________y_____SgGGG_____GGSg 7SwiftUI11ToolbarItemV AA15ModifiedContentV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA023AccessibilityAttachmentL0V
+ _symbolic ySo18AALocalContactInfoCYacSg
+ _type_layout_string 14AppleAccountUI029CustodianOwnerListViewServiceG0V
+ getFAProfilePictureStoreClass.softClass
+ get_witness_table 7SwiftUI19_ConditionalContentVyACyACyAA05TupleD0VyAA6SpacerV_AA4ViewPAAE08progressG5StyleyQrqd__AA08ProgressgI0Rd__lFQOyAA0jG0VyAA05EmptyG0VAOG_AA08CircularjgI0VQo_AGQPGAA4TextVGACyA2OGG012AppleAccountB0018TrustedContactListG0VyAZ014CustodianOwnerrg7ServiceG5ModelCGGAaHHPAyaHHPAwaHHPAtaHHPAgaHHPyHC_qd0__AaHHD3_ASHOAgaHHPyHCHX_HC_AvaHHPyHCHC_AxaHHPAoaHHPyHC_AoaHHPyHCHCHC_A3_AaHHPyHCHC
+ get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15NavigationStackVyAA0I4PathVAcAE5alert_11isPresented7actions7messageQrqd___AA7BindingVySbGqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQOyAcAE21navigationDestination4item11destinationQrASyqd__SgG_qd_0_qd__ctSHRd__AaBRd_0_r0_lFQOyAA6IDViewVyAcAE7toolbar7contentQrqd__yXE_tAA14ToolbarContentRd__lFQOyAA08ModifiedZ0Vy012AppleAccountB0010OnboardingC0VyA5_018CustodianOwnerListc7ServiceC5ModelCGAA30_SafeAreaRegionsIgnoringLayoutVG_AA0Y4ItemVyytA4_yAA6ButtonVyA4_yAA5ImageVAA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGGGAA31AccessibilityAttachmentModifierVGGSgQo_SiG_So18AALocalContactInfoCA5_026CustodianOwnerRecoveryCodeC0VSgQo__SSAcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQOyA17_yAA4TextVG_Qo_A45_Qo_G_Qo_HO
CStrings:
+ "/System/Library/PrivateFrameworks/FamilyCircleUI.framework/Contents/MacOS/FamilyCircleUI"
+ "Error fetching the list of people you are a recovery contact for."
+ "Error generating recovery code: %@"
+ "FAProfilePictureStore"
+ "Generated recovery code for contact: %s"
+ "RECOVERY_CODE_NOT_AVAILABLE_MESSAGE"
+ "RECOVERY_CODE_NOT_AVAILABLE_MESSAGE_FALLBACK_NAME"
+ "RECOVERY_CODE_NOT_AVAILABLE_TITLE"
+ "RECOVERY_CONTACT_EMPTY_STATE_DESCRIPTION"
+ "RECOVERY_CONTACT_EMPTY_STATE_TITLE"
+ "RECOVERY_CONTACT_HELP_NAME"
+ "RECOVERY_CONTACT_LEARN_MORE"
+ "RECOVERY_CONTACT_LIST_DESCRIPTION"
+ "RECOVERY_CONTACT_LIST_TITLE"
+ "RECOVERY_CONTACT_SINGLE_DESCRIPTION"
+ "RECOVERY_CONTACT_SINGLE_TITLE"
+ "Unable to find class %s"
+ "View.task @ AppleAccountUI/CustodianOwnerListViewServiceView.swift:"
+ "handleContactTap ignored - already generating code"
+ "https://support.apple.com/102608"
+ "softlink:r:path:/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"NSData\"8"
+ "v32@?0@\"NSData\"8Q16@\"NSError\"24"
+ "✓ Fetched %ld custodianship owners"
+ "✓ fetchContacts END - isLoading: %{bool}d, isEmpty: %{bool}d"
+ "🔍 fetchContacts START - isLoading: %{bool}d"
- "TrustedContactListViewService macOS: returning placeholder NSViewController (stub — see rdar://177985331)"
```
