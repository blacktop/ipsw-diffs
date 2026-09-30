## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-571.0.0.0.0
-  __TEXT.__text: 0x1181cc
-  __TEXT.__auth_stubs: 0x2b90
-  __TEXT.__objc_methlist: 0xbb6c
-  __TEXT.__const: 0x2ef4
-  __TEXT.__cstring: 0xdab9
-  __TEXT.__oslogstring: 0x5b93
+580.0.0.0.0
+  __TEXT.__text: 0x119360
+  __TEXT.__auth_stubs: 0x2bb0
+  __TEXT.__objc_methlist: 0xbc34
+  __TEXT.__const: 0x2f04
+  __TEXT.__cstring: 0xdb09
+  __TEXT.__oslogstring: 0x5bd3
   __TEXT.__gcc_except_tab: 0x10d4
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x2e82
+  __TEXT.__swift5_typeref: 0x2ecc
   __TEXT.__constg_swiftt: 0x13b4
-  __TEXT.__swift5_reflstr: 0x9c0
-  __TEXT.__swift5_fieldmd: 0xadc
+  __TEXT.__swift5_reflstr: 0x9d0
+  __TEXT.__swift5_fieldmd: 0xae8
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x2c0
-  __TEXT.__swift5_capture: 0xae4
+  __TEXT.__swift5_capture: 0xb2c
   __TEXT.__swift5_proto: 0xf0
   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0xb8
-  __TEXT.__unwind_info: 0x3978
-  __TEXT.__eh_frame: 0x2328
-  __TEXT.__objc_classname: 0x1ce5
-  __TEXT.__objc_methname: 0x214b0
-  __TEXT.__objc_methtype: 0x3945
-  __TEXT.__objc_stubs: 0x14bc0
-  __DATA_CONST.__got: 0x1358
-  __DATA_CONST.__const: 0x2370
+  __TEXT.__unwind_info: 0x39d0
+  __TEXT.__eh_frame: 0x23c8
+  __TEXT.__objc_classname: 0x1d00
+  __TEXT.__objc_methname: 0x21657
+  __TEXT.__objc_methtype: 0x3975
+  __TEXT.__objc_stubs: 0x14ce0
+  __DATA_CONST.__got: 0x1360
+  __DATA_CONST.__const: 0x2358
   __DATA_CONST.__objc_classlist: 0x738
-  __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x1c0
+  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6978
+  __DATA_CONST.__objc_selrefs: 0x69c0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x5e0
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__auth_got: 0x15d8
-  __AUTH_CONST.__const: 0x2e70
-  __AUTH_CONST.__cfstring: 0xa8c0
-  __AUTH_CONST.__objc_const: 0x23ce8
+  __AUTH_CONST.__auth_got: 0x15e8
+  __AUTH_CONST.__const: 0x2ec0
+  __AUTH_CONST.__cfstring: 0xa900
+  __AUTH_CONST.__objc_const: 0x24208
   __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH.__objc_data: 0x4ba8
   __AUTH.__data: 0x9c0
-  __DATA.__objc_ivar: 0xc5c
-  __DATA.__data: 0x21b0
+  __DATA.__objc_ivar: 0xc68
+  __DATA.__data: 0x2260
   __DATA.__bss: 0x1ea8
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x9b0

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3E0447BF-590D-3993-B0F4-9CD5B69FF074
-  Functions: 5924
-  Symbols:   15813
-  CStrings:  8956
+  UUID: B0C80538-3CAF-3F00-AE03-D2E8990DE5F2
+  Functions: 5946
+  Symbols:   15850
+  CStrings:  8974
 
Symbols:
+ +[STRootViewModelCoordinator currentAccountIsProtoForAKAccountManager:]
+ +[STRootViewModelCoordinator shouldShowConnectToFamilyForSignInForAKAccountManager:]
+ -[STCommunicationSafetyViewModelCoordinator currentAccountIsProto]
+ -[STCommunicationSafetyViewModelCoordinator initWithPersistenceController:userDSID:currentAccountIsProto:]
+ -[STCommunicationSafetyViewModelCoordinator initWithPersistenceController:userDSID:currentAccountIsProto:modelUpdatedHandler:]
+ -[STCommunicationSafetyViewModelCoordinator isCommunicationSafetySendingEditable]
+ -[STContentPrivacyViewModelCoordinator areRestrictionsEditable]
+ -[STContentPrivacyViewModelCoordinator currentAccountIsProto]
+ -[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]
+ -[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:]
+ -[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]
+ -[STEyeReliefViewModelCoordinator currentAccountIsProto]
+ -[STEyeReliefViewModelCoordinator initWithPersistenceController:userDSID:currentAccountIsProto:]
+ -[STEyeReliefViewModelCoordinator isScreenDistanceEditable]
+ -[STRootViewModelCoordinator _akAccountManager]
+ -[STRootViewModelCoordinator _currentAccountIsProto]
+ -[STRootViewModelCoordinator shouldShowConnectToFamilyForSignIn]
+ -[STSignInToiCloudGroupSpecifierProvider _updateSpecifiersForConnectToFamily]
+ GCC_except_table100
+ GCC_except_table187
+ GCC_except_table196
+ _OBJC_IVAR_$_STCommunicationSafetyViewModelCoordinator._currentAccountIsProto
+ _OBJC_IVAR_$_STContentPrivacyViewModelCoordinator._currentAccountIsProto
+ _OBJC_IVAR_$_STEyeReliefViewModelCoordinator._currentAccountIsProto
+ _STPrefsURLComponentFragmentLastWeek
+ _STPrefsURLComponentFragmentToday
+ _STRegionRatingsLeastRestrictiveValue
+ __OBJC_$_CATEGORY_AKAccountManager_$_STAKAccountManagerProtocol
+ __OBJC_$_PROP_LIST_AKAccountManager_$_STAKAccountManagerProtocol
+ __OBJC_$_PROP_LIST_STAKAccountManagerProtocol
+ __OBJC_$_PROP_LIST_STCommunicationSafetyViewModelCoordinator.174
+ __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.980
+ __OBJC_$_PROP_LIST_STEyeReliefViewModelCoordinator.158
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STAKAccountManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STAKAccountManagerProtocol
+ __OBJC_$_PROTOCOL_REFS_STAKAccountManagerProtocol
+ __OBJC_CATEGORY_PROTOCOLS_$_AKAccountManager_$_STAKAccountManagerProtocol
+ __OBJC_LABEL_PROTOCOL_$_STAKAccountManagerProtocol
+ __OBJC_PROTOCOL_$_STAKAccountManagerProtocol
+ ___110-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:]_block_invoke
+ ___110-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:]_block_invoke.cold.1
+ ___171-[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]_block_invoke
+ ___53-[STIntroPasscodeViewController userEnteredPasscode:]_block_invoke.79
+ ___53-[STIntroPasscodeViewController userEnteredPasscode:]_block_invoke_2.84
+ ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.312
+ ___96-[STEyeReliefViewModelCoordinator initWithPersistenceController:userDSID:currentAccountIsProto:]_block_invoke
+ ___block_literal_global.702
+ ___block_literal_global.983
+ _block_copy_helper.25
+ _block_copy_helper.33
+ _block_copy_helper.68
+ _block_copy_helper.71
+ _block_copy_helper.77
+ _block_copy_helper.85
+ _block_descriptor.27
+ _block_descriptor.35
+ _block_descriptor.70
+ _block_descriptor.73
+ _block_descriptor.79
+ _block_descriptor.87
+ _block_destroy_helper.26
+ _block_destroy_helper.34
+ _block_destroy_helper.69
+ _block_destroy_helper.72
+ _block_destroy_helper.78
+ _block_destroy_helper.86
+ _get_witness_table 7SwiftUI6HStackVyAA9TupleViewVyAA6ButtonVyAA5ImageVG_AiA4TextVAA6SpacerVALtGGAA0E0HPyHC.42
+ _objc_msgSend$_akAccountManager
+ _objc_msgSend$_currentAccountIsProto
+ _objc_msgSend$_updateSpecifiersForConnectToFamily
+ _objc_msgSend$addBulletedListItemWithTitle:description:symbolName:
+ _objc_msgSend$areRestrictionsEditable
+ _objc_msgSend$currentAccountIsProto
+ _objc_msgSend$currentAccountIsProtoForAKAccountManager:
+ _objc_msgSend$initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:loadCompletionHandler:
+ _objc_msgSend$initWithPersistenceController:userDSID:currentAccountIsProto:
+ _objc_msgSend$initWithPersistenceController:userDSID:currentAccountIsProto:modelUpdatedHandler:
+ _objc_msgSend$initWithPersistenceController:userDSID:userName:currentAccountIsProto:
+ _objc_msgSend$initWithPersistenceController:userDSID:userName:currentAccountIsProto:loadCompletionHandler:
+ _objc_msgSend$initWithTitle:detailText:symbolName:
+ _objc_msgSend$isCommunicationSafetySendingEditable
+ _objc_msgSend$isScreenDistanceEditable
+ _objc_msgSend$shouldShowConnectToFamilyForSignIn
+ _objc_msgSend$shouldShowConnectToFamilyForSignInForAKAccountManager:
+ _objectdestroy.23Tm
+ _swift_initStackObject
+ _symbolic SDy_____SSG s6UInt64V
+ _symbolic _____3key_yp5valuet s11AnyHashableV
+ _symbolic _____Iegn_ 20ScreenTimeSettingsUI12ExceptionAppV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So18NSNotificationNamea
+ _symbolic _____y_____G_AB__________ADt 7SwiftUI6ButtonV AA5ImageV AA4TextV AA6SpacerV
+ _symbolic _____y_____SSG s18_DictionaryStorageC s6UInt64V
+ _symbolic _____y___________y_____y_____G_AE__________AGtGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA05TupleD0V AA6ButtonV AA5ImageV AA4TextV AA6SpacerV
+ _symbolic _____y_____y_____y_____G_AD__________AFtGG 7SwiftUI6HStackV AA9TupleViewV AA6ButtonV AA5ImageV AA4TextV AA6SpacerV
- -[STCommunicationSafetyViewModelCoordinator initWithPersistenceController:userDSID:]
- -[STCommunicationSafetyViewModelCoordinator initWithPersistenceController:userDSID:modelUpdatedHandler:]
- -[STContentPrivacyListController setItemSpecifierValue:specifier:].cold.1
- -[STContentPrivacyMediaRestrictionsDetailController setItemSpecifierValue:specifier:].cold.1
- -[STContentPrivacyStoreDetailController tableView:didSelectRowAtIndexPath:].cold.1
- -[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:loadCompletionHandler:]
- -[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:]
- -[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:loadCompletionHandler:]
- -[STEyeReliefViewModelCoordinator initWithPersistenceController:userDSID:]
- GCC_except_table182
- GCC_except_table191
- _STPrefsURLComponentFragmentDay
- _STPrefsURLComponentFragmentWeek
- __OBJC_$_PROP_LIST_STCommunicationSafetyViewModelCoordinator.167
- __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.974
- __OBJC_$_PROP_LIST_STEyeReliefViewModelCoordinator.151
- ___149-[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:loadCompletionHandler:]_block_invoke
- ___53-[STIntroPasscodeViewController userEnteredPasscode:]_block_invoke.81
- ___53-[STIntroPasscodeViewController userEnteredPasscode:]_block_invoke_2.86
- ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.315
- ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.cold.2
- ___74-[STEyeReliefViewModelCoordinator initWithPersistenceController:userDSID:]_block_invoke
- ___88-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:]_block_invoke
- ___88-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:]_block_invoke.cold.1
- ___block_literal_global.696
- ___block_literal_global.977
- ___swift_memcpy32_8
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ScreenTimeSettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ScreenTimeSettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ScreenTimeSettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ScreenTimeSettingsUI
- _block_copy_helper.22
- _block_copy_helper.27
- _block_copy_helper.78
- _block_descriptor.24
- _block_descriptor.29
- _block_descriptor.80
- _block_destroy_helper.23
- _block_destroy_helper.28
- _block_destroy_helper.79
- _get_witness_table 7SwiftUI6HStackVyAA9TupleViewVyAA6ButtonVyAA5ImageVG_AiA4TextVAA6SpacerVtGGAA0E0HPyHC.42
- _objc_msgSend$_systemImageNamed:withConfiguration:
- _objc_msgSend$configurationPreferringMonochrome
- _objc_msgSend$configurationWithHierarchicalColor:
- _objc_msgSend$initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:loadCompletionHandler:
- _objc_msgSend$initWithPersistenceController:userDSID:modelUpdatedHandler:
- _objc_msgSend$initWithPersistenceController:userDSID:userName:
- _objc_msgSend$initWithPersistenceController:userDSID:userName:loadCompletionHandler:
- _objc_msgSend$initWithTitle:detailText:icon:
- _symbolic _____Iegg_ 20ScreenTimeSettingsUI12ExceptionAppV
- _symbolic _____y_____G_AB__________t 7SwiftUI6ButtonV AA5ImageV AA4TextV AA6SpacerV
- _symbolic _____y___________y_____y_____G_AE__________tGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA05TupleD0V AA6ButtonV AA5ImageV AA4TextV AA6SpacerV
- _symbolic _____y_____y_____y_____G_AD__________tGG 7SwiftUI6HStackV AA9TupleViewV AA6ButtonV AA5ImageV AA4TextV AA6SpacerV
CStrings:
+ "@44@0:8@16@24B32@?36"
+ "@60@0:8@16@24@32@40B48@?52"
+ "Did not enter PIN successfully for app ratings and exceptions"
+ "Failed to cast ratings titleDictionary to expected type. %s"
+ "Failed to lookup rating title for app exception: %@"
+ "Remove app exception alert body format string?"
+ "Remove button title for remove app exception UI alert"
+ "Remove this app?"
+ "RemoveAppExceptionAlertBodyFormat"
+ "RemoveButtonText"
+ "STAKAccountManagerProtocol"
+ "SignInToiCloudButtonNameConnectToFamily"
+ "SignInToiCloudFooterTextConnectToFamily"
+ "TB,R,N,V_currentAccountIsProto"
+ "_akAccountManager"
+ "_currentAccountIsProto"
+ "_updateSpecifiersForConnectToFamily"
+ "addBulletedListItemWithTitle:description:symbolName:"
+ "areRestrictionsEditable"
+ "currentAccountIsProto"
+ "currentAccountIsProtoForAKAccountManager:"
+ "initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:loadCompletionHandler:"
+ "initWithPersistenceController:userDSID:currentAccountIsProto:"
+ "initWithPersistenceController:userDSID:currentAccountIsProto:modelUpdatedHandler:"
+ "initWithPersistenceController:userDSID:userName:currentAccountIsProto:"
+ "initWithPersistenceController:userDSID:userName:currentAccountIsProto:loadCompletionHandler:"
+ "initWithTitle:detailText:symbolName:"
+ "isCommunicationSafetySendingEditable"
+ "isScreenDistanceEditable"
+ "ratingValue"
+ "shouldShowConnectToFamilyForSignIn"
+ "shouldShowConnectToFamilyForSignInForAKAccountManager:"
- "@56@0:8@16@24@32@40@?48"
- "Content for remove app exception UI alert"
- "Continue button title for remove app exception UI alert"
- "ContinueButtonText"
- "Failed to save ContentPrivacyListController settings: %{public}@"
- "Failed to save ContentPrivacyMediaRestriction settings: %{public}@"
- "RemoveAppExceptionAlertBody"
- "Title for remove app exception UI warning alert"
- "_systemImageNamed:withConfiguration:"
- "configurationPreferringMonochrome"
- "configurationWithHierarchicalColor:"
- "imageNamed:inBundle:withConfiguration:"
- "initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:loadCompletionHandler:"
- "initWithPersistenceController:userDSID:modelUpdatedHandler:"
- "initWithPersistenceController:userDSID:userName:"
- "initWithPersistenceController:userDSID:userName:loadCompletionHandler:"
- "initWithTitle:detailText:icon:"

```
