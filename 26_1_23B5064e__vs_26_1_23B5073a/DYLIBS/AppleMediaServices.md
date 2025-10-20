## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.1.18.0.0
-  __TEXT.__text: 0x74105c
-  __TEXT.__auth_stubs: 0x4a80
-  __TEXT.__objc_methlist: 0x22514
-  __TEXT.__const: 0x5aa20
+9.1.20.2.1
+  __TEXT.__text: 0x7294fc
+  __TEXT.__auth_stubs: 0x49e0
+  __TEXT.__objc_methlist: 0x2203c
+  __TEXT.__const: 0x5adc0
   __TEXT.__dlopen_cstrs: 0x98b
-  __TEXT.__cstring: 0x2c419
-  __TEXT.__swift5_typeref: 0x6469
-  __TEXT.__swift5_reflstr: 0x37f4
-  __TEXT.__swift5_assocty: 0xeb8
-  __TEXT.__constg_swiftt: 0x4fa0
-  __TEXT.__swift5_builtin: 0x30c
-  __TEXT.__swift5_fieldmd: 0x4880
-  __TEXT.__swift5_proto: 0x1018
-  __TEXT.__swift5_types: 0x5c4
-  __TEXT.__swift_as_entry: 0x710
-  __TEXT.__swift_as_ret: 0x878
-  __TEXT.__swift5_capture: 0x30cc
-  __TEXT.__swift5_mpenum: 0x70
-  __TEXT.__swift5_protos: 0xf0
-  __TEXT.__oslogstring: 0x2fbb6
+  __TEXT.__cstring: 0x2b716
+  __TEXT.__swift5_typeref: 0x6201
+  __TEXT.__swift5_reflstr: 0x3404
+  __TEXT.__swift5_assocty: 0xe28
+  __TEXT.__constg_swiftt: 0x4c4c
+  __TEXT.__swift5_builtin: 0x2d0
+  __TEXT.__swift5_fieldmd: 0x4364
+  __TEXT.__swift5_proto: 0xf54
+  __TEXT.__swift5_types: 0x570
+  __TEXT.__swift_as_entry: 0x64c
+  __TEXT.__swift_as_ret: 0x794
+  __TEXT.__swift5_capture: 0x2d44
+  __TEXT.__swift5_mpenum: 0x60
+  __TEXT.__swift5_protos: 0xec
+  __TEXT.__oslogstring: 0x2fda2
   __TEXT.__gcc_except_tab: 0x5ca8
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x113c8
-  __TEXT.__eh_frame: 0x1517c
-  __TEXT.__objc_classname: 0x4040
-  __TEXT.__objc_methname: 0x442aa
+  __TEXT.__unwind_info: 0x103f0
+  __TEXT.__eh_frame: 0x130dc
+  __TEXT.__objc_classname: 0x3f72
+  __TEXT.__objc_methname: 0x44166
   __TEXT.__objc_methtype: 0x786e
-  __TEXT.__objc_stubs: 0x2e500
-  __DATA_CONST.__got: 0x1a00
-  __DATA_CONST.__const: 0xc208
-  __DATA_CONST.__objc_classlist: 0x1478
+  __TEXT.__objc_stubs: 0x2e4a0
+  __DATA_CONST.__got: 0x19d8
+  __DATA_CONST.__const: 0xc230
+  __DATA_CONST.__objc_classlist: 0x1420
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xefe8
+  __DATA_CONST.__objc_selrefs: 0xef28
   __DATA_CONST.__objc_protorefs: 0x210
-  __DATA_CONST.__objc_superrefs: 0xcd0
+  __DATA_CONST.__objc_superrefs: 0xca0
   __DATA_CONST.__objc_arraydata: 0x580
-  __AUTH_CONST.__auth_got: 0x2558
-  __AUTH_CONST.__const: 0x2ce38
-  __AUTH_CONST.__cfstring: 0x223e0
-  __AUTH_CONST.__objc_const: 0x3c2e0
+  __AUTH_CONST.__auth_got: 0x2508
+  __AUTH_CONST.__const: 0x2bae8
+  __AUTH_CONST.__cfstring: 0x22460
+  __AUTH_CONST.__objc_const: 0x3b6a8
   __AUTH_CONST.__objc_intobj: 0xc60
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x91d0
-  __AUTH.__data: 0x2578
-  __DATA.__objc_ivar: 0x18a4
-  __DATA.__data: 0x6f00
-  __DATA.__bss: 0x1a769
-  __DATA.__common: 0xb60
-  __DATA_DIRTY.__objc_ivar: 0x6f0
+  __AUTH.__objc_data: 0x8dd8
+  __AUTH.__data: 0x2228
+  __DATA.__objc_ivar: 0x18ac
+  __DATA.__data: 0x71a0
+  __DATA.__bss: 0x192e9
+  __DATA.__common: 0xb58
+  __DATA_DIRTY.__objc_ivar: 0x6a0
   __DATA_DIRTY.__objc_data: 0x5ac0
-  __DATA_DIRTY.__data: 0x20d8
+  __DATA_DIRTY.__data: 0x1b08
   __DATA_DIRTY.__bss: 0x40e0
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BAB76256-8EB9-3583-BB02-83FFDE9642B5
-  Functions: 25885
-  Symbols:   51977
-  CStrings:  25424
+  UUID: E88DF4CD-B96A-3986-8EA4-D50742232001
+  Functions: 24933
+  Symbols:   51088
+  CStrings:  25326
 
Symbols:
+ +[AMSHardwareOffersMigrator migrateHardwareOffersWithOptions:]
+ -[AMSFollowUp _clearGroupedFollowUpWithBackingIdentifier:config:]
+ -[AMSFollowUp _getHardwareFollowUpGroupingEnabledWithBag:]
+ -[AMSFollowUp _getHardwareFollowUpSheetURLWithBag:]
+ -[AMSFollowUp _getHardwareOffersFeatureConfigFromBag]
+ -[AMSFollowUp _getHardwareOffersSheetURL]
+ -[AMSFollowUp _makeGroupedHardwareFollowUpItemFromItems:DSID:config:]
+ -[AMSFollowUp _postGroupedFollowUpItem:config:]
+ -[AMSFollowUp _updateGroupedHardwareFollowUpItemWithItems:DSID:config:error:]
+ -[AMSHardwareOffersConfig .cxx_destruct]
+ -[AMSHardwareOffersConfig initWithIsGroupingEnabled:sheetURL:]
+ -[AMSHardwareOffersConfig isGroupingEnabled]
+ -[AMSHardwareOffersConfig setIsGroupingEnabled:]
+ -[AMSHardwareOffersConfig setSheetURL:]
+ -[AMSHardwareOffersConfig sheetURL]
+ _AMSBagKeyFollowUpHardwareFollowUpSheetURL
+ _OBJC_CLASS_$_AMSHardwareOffersConfig
+ _OBJC_CLASS_$_AMSHardwareOffersMigrator
+ _OBJC_IVAR_$_AMSHardwareOffersConfig._isGroupingEnabled
+ _OBJC_IVAR_$_AMSHardwareOffersConfig._sheetURL
+ _OBJC_METACLASS_$_AMSHardwareOffersConfig
+ _OBJC_METACLASS_$_AMSHardwareOffersMigrator
+ _OUTLINED_FUNCTION_184
+ _OUTLINED_FUNCTION_185
+ _OUTLINED_FUNCTION_186
+ __OBJC_$_CLASS_METHODS_AMSHardwareOffersMigrator
+ __OBJC_$_INSTANCE_METHODS_AMSHardwareOffersConfig
+ __OBJC_$_INSTANCE_VARIABLES_AMSHardwareOffersConfig
+ __OBJC_$_PROP_LIST_AMSHardwareOffersConfig
+ __OBJC_CLASS_RO_$_AMSHardwareOffersConfig
+ __OBJC_CLASS_RO_$_AMSHardwareOffersMigrator
+ __OBJC_METACLASS_RO_$_AMSHardwareOffersConfig
+ __OBJC_METACLASS_RO_$_AMSHardwareOffersMigrator
+ ___45-[AMSFollowUp _clearGroupedHardwareFollowUps]_block_invoke.115
+ ___47-[AMSFollowUp _postGroupedFollowUpItem:config:]_block_invoke
+ ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke.19
+ ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke.23
+ ___50-[AMSFollowUp clearFollowUpWithBackingIdentifier:]_block_invoke.14
+ ___51-[AMSFollowUp _getHardwareFollowUpSheetURLWithBag:]_block_invoke
+ ___53-[AMSFollowUp _getHardwareOffersFeatureConfigFromBag]_block_invoke
+ ___58-[AMSFollowUp _getHardwareFollowUpGroupingEnabledWithBag:]_block_invoke
+ ___58-[AMSFollowUp _getHardwareFollowUpGroupingEnabledWithBag:]_block_invoke.84
+ ___65-[AMSFollowUp _clearGroupedFollowUpWithBackingIdentifier:config:]_block_invoke
+ ___block_descriptor_40_e8_32s_e51_"AMSBinaryPromise"16?0"AMSHardwareOffersConfig"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e45_"AMSPromise"16?0"AMSHardwareOffersConfig"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e51_"AMSBinaryPromise"16?0"AMSHardwareOffersConfig"8ls32l8s40l8
+ ___block_literal_global.117
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _kFollowUpActionUserInfoKeyRequiresFollowUpUI
+ _objc_msgSend$_clearGroupedFollowUpWithBackingIdentifier:config:
+ _objc_msgSend$_getHardwareFollowUpGroupingEnabledWithBag:
+ _objc_msgSend$_getHardwareFollowUpSheetURLWithBag:
+ _objc_msgSend$_getHardwareOffersFeatureConfigFromBag
+ _objc_msgSend$_makeGroupedHardwareFollowUpItemFromItems:DSID:config:
+ _objc_msgSend$_postGroupedFollowUpItem:config:
+ _objc_msgSend$_updateGroupedHardwareFollowUpItemWithItems:DSID:config:error:
+ _objc_msgSend$initWithIsGroupingEnabled:sheetURL:
+ _objc_msgSend$isGroupingEnabled
+ _objc_msgSend$migrateHardwareOffersWithOptions:
+ _objc_msgSend$sheetURL
- -[AMSFollowUp _clearGroupedFollowUpWithBackingIdentifier:]
- -[AMSFollowUp _isHardwareOfferFollowUpGroupingEnabled]
- -[AMSFollowUp _makeGroupedHardwareFollowUpItemFromItems:DSID:]
- -[AMSFollowUp _postGroupedFollowUpItem:]
- -[AMSFollowUp _updateGroupedHardwareFollowUpItemWithItems:DSID:error:]
- -[AMSMediaRestrictionsDisableTask .cxx_destruct]
- -[AMSMediaRestrictionsDisableTask account]
- -[AMSMediaRestrictionsDisableTask bag]
- -[AMSMediaRestrictionsDisableTask editToken]
- -[AMSMediaRestrictionsDisableTask initWithAccount:editToken:bag:]
- -[AMSMediaRestrictionsDisableTask perform]
- -[AMSMediaRestrictionsDisableTask setEditToken:]
- -[AMSMediaRestrictionsEditProfileLockTask .cxx_destruct]
- -[AMSMediaRestrictionsEditProfileLockTask account]
- -[AMSMediaRestrictionsEditProfileLockTask bag]
- -[AMSMediaRestrictionsEditProfileLockTask editToken]
- -[AMSMediaRestrictionsEditProfileLockTask initWithAccount:editToken:bag:]
- -[AMSMediaRestrictionsEditProfileLockTask performWithPasscode:]
- -[AMSMediaRestrictionsEditProfileLockTask setEditToken:]
- -[AMSMediaRestrictionsEditTask .cxx_destruct]
- -[AMSMediaRestrictionsEditTask account]
- -[AMSMediaRestrictionsEditTask bag]
- -[AMSMediaRestrictionsEditTask editToken]
- -[AMSMediaRestrictionsEditTask initWithAccount:editToken:bag:]
- -[AMSMediaRestrictionsEditTask performWithRestrictions:]
- -[AMSMediaRestrictionsEditTask setEditToken:]
- -[AMSMediaRestrictionsRemoveProfileLockTask .cxx_destruct]
- -[AMSMediaRestrictionsRemoveProfileLockTask account]
- -[AMSMediaRestrictionsRemoveProfileLockTask bag]
- -[AMSMediaRestrictionsRemoveProfileLockTask editToken]
- -[AMSMediaRestrictionsRemoveProfileLockTask initWithAccount:bag:]
- -[AMSMediaRestrictionsRemoveProfileLockTask performWithPasscode:]
- -[AMSMediaRestrictionsRemoveProfileLockTask setEditToken:]
- -[AMSMediaRestrictionsSetupProfileLockTask .cxx_destruct]
- -[AMSMediaRestrictionsSetupProfileLockTask account]
- -[AMSMediaRestrictionsSetupProfileLockTask bag]
- -[AMSMediaRestrictionsSetupProfileLockTask editToken]
- -[AMSMediaRestrictionsSetupProfileLockTask initWithAccount:editToken:bag:]
- -[AMSMediaRestrictionsSetupProfileLockTask performWithPasscode:]
- -[AMSMediaRestrictionsSetupProfileLockTask setEditToken:]
- -[AMSMediaRestrictionsSetupTask .cxx_destruct]
- -[AMSMediaRestrictionsSetupTask account]
- -[AMSMediaRestrictionsSetupTask bag]
- -[AMSMediaRestrictionsSetupTask editToken]
- -[AMSMediaRestrictionsSetupTask initWithAccount:editToken:bag:]
- -[AMSMediaRestrictionsSetupTask performWithRestrictions:]
- -[AMSMediaRestrictionsSetupTask setEditToken:]
- -[AMSMediaRestrictionsVerifyProfileLockTask .cxx_destruct]
- -[AMSMediaRestrictionsVerifyProfileLockTask account]
- -[AMSMediaRestrictionsVerifyProfileLockTask bag]
- -[AMSMediaRestrictionsVerifyProfileLockTask initWithAccount:bag:]
- -[AMSMediaRestrictionsVerifyProfileLockTask performWithPasscode:]
- _OBJC_CLASS_$_AMSMediaRestrictionsDisableTask
- _OBJC_CLASS_$_AMSMediaRestrictionsEditProfileLockTask
- _OBJC_CLASS_$_AMSMediaRestrictionsEditTask
- _OBJC_CLASS_$_AMSMediaRestrictionsPerformer
- _OBJC_CLASS_$_AMSMediaRestrictionsRatingItem
- _OBJC_CLASS_$_AMSMediaRestrictionsRemoveProfileLockTask
- _OBJC_CLASS_$_AMSMediaRestrictionsResult
- _OBJC_CLASS_$_AMSMediaRestrictionsSetupProfileLockTask
- _OBJC_CLASS_$_AMSMediaRestrictionsSetupTask
- _OBJC_CLASS_$_AMSMediaRestrictionsValue
- _OBJC_CLASS_$_AMSMediaRestrictionsVerifyProfileLockTask
- _OBJC_METACLASS_$_AMSMediaRestrictionsDisableTask
- _OBJC_METACLASS_$_AMSMediaRestrictionsEditProfileLockTask
- _OBJC_METACLASS_$_AMSMediaRestrictionsEditTask
- _OBJC_METACLASS_$_AMSMediaRestrictionsPerformer
- _OBJC_METACLASS_$_AMSMediaRestrictionsRatingItem
- _OBJC_METACLASS_$_AMSMediaRestrictionsRemoveProfileLockTask
- _OBJC_METACLASS_$_AMSMediaRestrictionsResult
- _OBJC_METACLASS_$_AMSMediaRestrictionsSetupProfileLockTask
- _OBJC_METACLASS_$_AMSMediaRestrictionsSetupTask
- _OBJC_METACLASS_$_AMSMediaRestrictionsValue
- _OBJC_METACLASS_$_AMSMediaRestrictionsVerifyProfileLockTask
- __CLASS_METHODS_AMSMediaRestrictionsRatingItem
- __CLASS_METHODS_AMSMediaRestrictionsValue
- __CLASS_PROPERTIES_AMSMediaRestrictionsRatingItem
- __DATA_AMSMediaRestrictionsPerformer
- __DATA_AMSMediaRestrictionsRatingItem
- __DATA_AMSMediaRestrictionsResult
- __DATA_AMSMediaRestrictionsValue
- __DATA__TtC18AppleMediaServices27MediaRestrictionsQRAuthTask
- __DATA__TtCC18AppleMediaServices26MediaRestrictionsPerformerP33_36668741CA9525741226C3D3F7E765C314PromiseHandler
- __INSTANCE_METHODS_AMSMediaRestrictionsPerformer
- __INSTANCE_METHODS_AMSMediaRestrictionsRatingItem
- __INSTANCE_METHODS_AMSMediaRestrictionsResult
- __INSTANCE_METHODS_AMSMediaRestrictionsValue
- __IVARS_AMSMediaRestrictionsPerformer
- __IVARS_AMSMediaRestrictionsRatingItem
- __IVARS_AMSMediaRestrictionsResult
- __IVARS_AMSMediaRestrictionsValue
- __IVARS__TtC18AppleMediaServices27MediaRestrictionsQRAuthTask
- __IVARS__TtCC18AppleMediaServices26MediaRestrictionsPerformerP33_36668741CA9525741226C3D3F7E765C314PromiseHandler
- __METACLASS_DATA_AMSMediaRestrictionsPerformer
- __METACLASS_DATA_AMSMediaRestrictionsRatingItem
- __METACLASS_DATA_AMSMediaRestrictionsResult
- __METACLASS_DATA_AMSMediaRestrictionsValue
- __METACLASS_DATA__TtC18AppleMediaServices27MediaRestrictionsQRAuthTask
- __METACLASS_DATA__TtCC18AppleMediaServices26MediaRestrictionsPerformerP33_36668741CA9525741226C3D3F7E765C314PromiseHandler
- __OBJC_$_INSTANCE_METHODS_AMSMediaRestrictionsDisableTask
- __OBJC_$_INSTANCE_METHODS_AMSMediaRestrictionsEditProfileLockTask
- __OBJC_$_INSTANCE_METHODS_AMSMediaRestrictionsEditTask
- __OBJC_$_INSTANCE_METHODS_AMSMediaRestrictionsRemoveProfileLockTask
- __OBJC_$_INSTANCE_METHODS_AMSMediaRestrictionsSetupProfileLockTask
- __OBJC_$_INSTANCE_METHODS_AMSMediaRestrictionsSetupTask
- __OBJC_$_INSTANCE_METHODS_AMSMediaRestrictionsVerifyProfileLockTask
- __OBJC_$_INSTANCE_VARIABLES_AMSMediaRestrictionsDisableTask
- __OBJC_$_INSTANCE_VARIABLES_AMSMediaRestrictionsEditProfileLockTask
- __OBJC_$_INSTANCE_VARIABLES_AMSMediaRestrictionsEditTask
- __OBJC_$_INSTANCE_VARIABLES_AMSMediaRestrictionsRemoveProfileLockTask
- __OBJC_$_INSTANCE_VARIABLES_AMSMediaRestrictionsSetupProfileLockTask
- __OBJC_$_INSTANCE_VARIABLES_AMSMediaRestrictionsSetupTask
- __OBJC_$_INSTANCE_VARIABLES_AMSMediaRestrictionsVerifyProfileLockTask
- __OBJC_$_PROP_LIST_AMSMediaRestrictionsDisableTask
- __OBJC_$_PROP_LIST_AMSMediaRestrictionsEditProfileLockTask
- __OBJC_$_PROP_LIST_AMSMediaRestrictionsEditTask
- __OBJC_$_PROP_LIST_AMSMediaRestrictionsRemoveProfileLockTask
- __OBJC_$_PROP_LIST_AMSMediaRestrictionsSetupProfileLockTask
- __OBJC_$_PROP_LIST_AMSMediaRestrictionsSetupTask
- __OBJC_$_PROP_LIST_AMSMediaRestrictionsVerifyProfileLockTask
- __OBJC_CLASS_RO_$_AMSMediaRestrictionsDisableTask
- __OBJC_CLASS_RO_$_AMSMediaRestrictionsEditProfileLockTask
- __OBJC_CLASS_RO_$_AMSMediaRestrictionsEditTask
- __OBJC_CLASS_RO_$_AMSMediaRestrictionsRemoveProfileLockTask
- __OBJC_CLASS_RO_$_AMSMediaRestrictionsSetupProfileLockTask
- __OBJC_CLASS_RO_$_AMSMediaRestrictionsSetupTask
- __OBJC_CLASS_RO_$_AMSMediaRestrictionsVerifyProfileLockTask
- __OBJC_METACLASS_RO_$_AMSMediaRestrictionsDisableTask
- __OBJC_METACLASS_RO_$_AMSMediaRestrictionsEditProfileLockTask
- __OBJC_METACLASS_RO_$_AMSMediaRestrictionsEditTask
- __OBJC_METACLASS_RO_$_AMSMediaRestrictionsRemoveProfileLockTask
- __OBJC_METACLASS_RO_$_AMSMediaRestrictionsSetupProfileLockTask
- __OBJC_METACLASS_RO_$_AMSMediaRestrictionsSetupTask
- __OBJC_METACLASS_RO_$_AMSMediaRestrictionsVerifyProfileLockTask
- __PROPERTIES_AMSMediaRestrictionsRatingItem
- __PROPERTIES_AMSMediaRestrictionsResult
- __PROPERTIES_AMSMediaRestrictionsValue
- __PROTOCOLS_AMSMediaRestrictionsRatingItem
- __PROTOCOLS_AMSMediaRestrictionsRatingItem.2
- ___40-[AMSFollowUp _postGroupedFollowUpItem:]_block_invoke
- ___42-[AMSMediaRestrictionsDisableTask perform]_block_invoke
- ___45-[AMSFollowUp _clearGroupedHardwareFollowUps]_block_invoke.110
- ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke.14
- ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke.18
- ___54-[AMSFollowUp _isHardwareOfferFollowUpGroupingEnabled]_block_invoke
- ___56-[AMSMediaRestrictionsEditTask performWithRestrictions:]_block_invoke
- ___57-[AMSMediaRestrictionsSetupTask performWithRestrictions:]_block_invoke
- ___58-[AMSFollowUp _clearGroupedFollowUpWithBackingIdentifier:]_block_invoke
- ___60-[AMSFollowUp _isGroupedHardwareOfferWithBackingIdentifier:]_block_invoke_2
- ___63-[AMSMediaRestrictionsEditProfileLockTask performWithPasscode:]_block_invoke
- ___64-[AMSMediaRestrictionsSetupProfileLockTask performWithPasscode:]_block_invoke
- ___65-[AMSMediaRestrictionsRemoveProfileLockTask performWithPasscode:]_block_invoke
- ___65-[AMSMediaRestrictionsVerifyProfileLockTask performWithPasscode:]_block_invoke
- ___block_descriptor_40_e8_32s_e38_"AMSBinaryPromise"16?0"AMSBoolean"8ls32l8
- ___block_descriptor_48_e8_32s40s_e32_"AMSPromise"16?0"AMSBoolean"8ls32l8s40l8
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
- ___swift_memcpy128_8
- ___swift_memcpy80_8
- _associated conformance 18AppleMediaServices0B12RestrictionsV19ValidationValueType33_DF65CEE45A27989D454821BA2DD8A103LLOSHAASQ
- _associated conformance 18AppleMediaServices0B20RestrictionsBagModelV10CodingKeysOSHAASQ
- _associated conformance 18AppleMediaServices0B20RestrictionsBagModelV10CodingKeysOs0G3KeyAAs23CustomStringConvertible
- _associated conformance 18AppleMediaServices0B20RestrictionsBagModelV10CodingKeysOs0G3KeyAAs28CustomDebugStringConvertible
- _associated conformance 18AppleMediaServices0B20RestrictionsBagModelV10CodingKeysOs12CaseIterableAA8AllCasessAFP_Sl
- _associated conformance 18AppleMediaServices0B20RestrictionsBagModelVSHAASQ
- _associated conformance 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelV10CodingKeysOSHAASQ
- _associated conformance 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelV10CodingKeysOs0I3KeyAAs23CustomStringConvertible
- _associated conformance 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelV10CodingKeysOs0I3KeyAAs28CustomDebugStringConvertible
- _associated conformance 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelV10CodingKeysOs12CaseIterableAA8AllCasessAFP_Sl
- _associated conformance 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelVSHAASQ
- _associated conformance 18AppleMediaServices0B31RestrictionsQRAuthPollingStatusOSHAASQ
- _associated conformance So30AMSMediaRestrictionsRatingItemC18AppleMediaServicesE10CodingKeys33_2DC91A10759E7D25F95C2A0598D9B8EBLLOSHACSQ
- _associated conformance So30AMSMediaRestrictionsRatingItemC18AppleMediaServicesE10CodingKeys33_2DC91A10759E7D25F95C2A0598D9B8EBLLOs0H3KeyACs23CustomStringConvertible
- _associated conformance So30AMSMediaRestrictionsRatingItemC18AppleMediaServicesE10CodingKeys33_2DC91A10759E7D25F95C2A0598D9B8EBLLOs0H3KeyACs28CustomDebugStringConvertible
- _get_enum_tag_for_layout_string 18AppleMediaServices18QRCodeHandlerErrorO
- _get_enum_tag_for_layout_string 18AppleMediaServices20RestrictionValueTypeO
- _objc_msgSend$_clearGroupedFollowUpWithBackingIdentifier:
- _objc_msgSend$_isHardwareOfferFollowUpGroupingEnabled
- _objc_msgSend$_makeGroupedHardwareFollowUpItemFromItems:DSID:
- _objc_msgSend$_postGroupedFollowUpItem:
- _objc_msgSend$_updateGroupedHardwareFollowUpItemWithItems:DSID:error:
- _objc_msgSend$disableRestrictions
- _objc_msgSend$editProfileLockWithPasscode:
- _objc_msgSend$editToken
- _objc_msgSend$editWithRestricitons:
- _objc_msgSend$initWithAccount:editToken:bag:
- _objc_msgSend$performSetupWithRestrictions:
- _objc_msgSend$removeProfileLockWithPasscode:
- _objc_msgSend$setupProfileLockWithPasscode:
- _objc_msgSend$verifyProfileLockWithPasscode:
- _objectdestroy.81Tm
- _pow
- _symbolic $s18AppleMediaServices0B30RestrictionsQRAuthTaskDelegateP
- _symbolic SDySS_____G 18AppleMediaServices20RestrictionValueTypeO
- _symbolic Say_____G 18AppleMediaServices0B20RestrictionsBagModelV10CodingKeysO
- _symbolic Say_____G 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelV10CodingKeysO
- _symbolic So17AMSMutablePromiseCySo26AMSMediaRestrictionsResultCG
- _symbolic So30AMSMediaRestrictionsRatingItemC
- _symbolic _____ 18AppleMediaServices0B12RestrictionsV
- _symbolic _____ 18AppleMediaServices0B12RestrictionsV19ValidationValueType33_DF65CEE45A27989D454821BA2DD8A103LLO
- _symbolic _____ 18AppleMediaServices0B17RestrictionsErrorO
- _symbolic _____ 18AppleMediaServices0B20RestrictionsBagModelV
- _symbolic _____ 18AppleMediaServices0B20RestrictionsBagModelV10CodingKeysO
- _symbolic _____ 18AppleMediaServices0B21RestrictionsPerformerC
- _symbolic _____ 18AppleMediaServices0B21RestrictionsPerformerC14PromiseHandler031_36668741CA9525741226C3D3F7E765I0LLC
- _symbolic _____ 18AppleMediaServices0B22RestrictionsQRAuthTaskC
- _symbolic _____ 18AppleMediaServices0B24RestrictionsQRAuthResultV
- _symbolic _____ 18AppleMediaServices0B25RestrictionsConfigurationV
- _symbolic _____ 18AppleMediaServices0B29RestrictionsQRAuthSetupResultV
- _symbolic _____ 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelV
- _symbolic _____ 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelV10CodingKeysO
- _symbolic _____ 18AppleMediaServices0B31RestrictionsQRAuthPollingResultV
- _symbolic _____ 18AppleMediaServices0B31RestrictionsQRAuthPollingStatusO
- _symbolic _____ 18AppleMediaServices0B31RestrictionsQRAuthTaskBagValuesV
- _symbolic _____ 18AppleMediaServices13QRCodeContextV
- _symbolic _____ 18AppleMediaServices18QRCodeHandlerErrorO
- _symbolic _____ 18AppleMediaServices20RestrictionValueTypeO
- _symbolic _____ So29AMSMediaRestrictionsValueTypeV
- _symbolic _____ So30AMSMediaRestrictionsRatingItemC18AppleMediaServicesE10CodingKeys33_2DC91A10759E7D25F95C2A0598D9B8EBLLO
- _symbolic _____Sg 18AppleMediaServices0B20RestrictionsBagModelV
- _symbolic _____Sg 18AppleMediaServices0B24RestrictionsQRAuthResultV
- _symbolic _____Sg 18AppleMediaServices0B29RestrictionsQRAuthSetupResultV
- _symbolic _____Sg 18AppleMediaServices13QRCodeHandlerC
- _symbolic ______p 18AppleMediaServices12QRCodeResultP
- _symbolic ______p 18AppleMediaServices19QRCodeSetupResponseP
- _symbolic ______p 18AppleMediaServices21QRCodePollingResponseP
- _symbolic ______pSg 18AppleMediaServices12QRCodeResultP
- _symbolic ______pSg 18AppleMediaServices19QRCodeSetupResponseP
- _symbolic ______pSgXw 18AppleMediaServices0B30RestrictionsQRAuthTaskDelegateP
- _symbolic _____ySS_____G s18_DictionaryStorageC 18AppleMediaServices20RestrictionValueTypeO
- _symbolic _____y_____G s22KeyedDecodingContainerV 18AppleMediaServices0E20RestrictionsBagModelV10CodingKeysO
- _symbolic _____y_____G s22KeyedDecodingContainerV 18AppleMediaServices0E30RestrictionsQRAuthTaskBagModelV10CodingKeysO
- _symbolic _____y_____G s22KeyedDecodingContainerV So30AMSMediaRestrictionsRatingItemC18AppleMediaServicesE10CodingKeys33_2DC91A10759E7D25F95C2A0598D9B8EBLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 18AppleMediaServices0E20RestrictionsBagModelV10CodingKeysO
- _symbolic _____y_____G s22KeyedEncodingContainerV 18AppleMediaServices0E30RestrictionsQRAuthTaskBagModelV10CodingKeysO
- _symbolic _____y_____G s22KeyedEncodingContainerV So30AMSMediaRestrictionsRatingItemC18AppleMediaServicesE10CodingKeys33_2DC91A10759E7D25F95C2A0598D9B8EBLLO
- _type_layout_string 18AppleMediaServices0B12RestrictionsV
- _type_layout_string 18AppleMediaServices0B17RestrictionsErrorO
- _type_layout_string 18AppleMediaServices0B20RestrictionsBagModelV
- _type_layout_string 18AppleMediaServices0B24RestrictionsQRAuthResultV
- _type_layout_string 18AppleMediaServices0B25RestrictionsConfigurationV
- _type_layout_string 18AppleMediaServices0B30RestrictionsQRAuthTaskBagModelV
- _type_layout_string 18AppleMediaServices0B31RestrictionsQRAuthPollingResultV
- _type_layout_string 18AppleMediaServices0B31RestrictionsQRAuthTaskBagValuesV
- _type_layout_string 18AppleMediaServices18QRCodeHandlerErrorO
- _type_layout_string 18AppleMediaServices20RestrictionValueTypeO
CStrings:
+ "%{public}@: Failed to load hardware offers sheet URL from bag with key \"%@\". Using fallback URL: \"%@\" Error: %@"
+ "%{public}@: Hardware offer configuration: isGroupingEnabled: %@, sheet URL: %@"
+ "%{public}@: Hardware offer grouping bag feature flag is enabled: %@"
+ "%{public}@: Hardware offer grouping bag feature flag is enabled: NO (bag key not found)"
+ "%{public}@: Hardware offer grouping disabled with OS feature flag"
+ "%{public}@: [%{public}@] %{public}@ migration enqueued."
+ "%{public}@: [%{public}@] %{public}@ skipping. No account DSID found during upgrade."
+ "@\"AMSBinaryPromise\"16@?0@\"AMSHardwareOffersConfig\"8"
+ "@\"AMSPromise\"16@?0@\"AMSHardwareOffersConfig\"8"
+ "AMSHardwareOffersConfig"
+ "AMSHardwareOffersMigrator"
+ "FollowUpCommand"
+ "T@\"NSString\",C,N,V_sheetURL"
+ "TB,N,V_isGroupingEnabled"
+ "_clearGroupedFollowUpWithBackingIdentifier:config:"
+ "_getHardwareFollowUpGroupingEnabledWithBag:"
+ "_getHardwareFollowUpSheetURLWithBag:"
+ "_getHardwareOffersFeatureConfigFromBag"
+ "_getHardwareOffersSheetURL"
+ "_isGroupingEnabled"
+ "_makeGroupedHardwareFollowUpItemFromItems:DSID:config:"
+ "_postGroupedFollowUpItem:config:"
+ "_sheetURL"
+ "_updateGroupedHardwareFollowUpItemWithItems:DSID:config:error:"
+ "command"
+ "follow-up-hardware-follow-up-sheet-url"
+ "https://amsui.apple.com/dynamic/marketing#route=hardwareOffers"
+ "initWithIsGroupingEnabled:sheetURL:"
+ "isGroupingEnabled"
+ "migrate"
+ "migrateHardwareOffersWithOptions:"
+ "setIsGroupingEnabled:"
+ "setSheetURL:"
+ "sheetURL"
- "  allowPurchases: "
- "  isProfileLockSet: "
- "  movieRestriction: "
- "  tvRestriction: "
- " seconds. Attempts until "
- "%{public}@: Hardware offer grouping enabled: OS: %@, bag: %@"
- "; ratingSystem = "
- "; ratingValue = "
- "@\"AMSPromise\"16@?0@\"AMSBoolean\"8"
- "AMSMediaRestrictionsDisableTask"
- "AMSMediaRestrictionsEditProfileLockTask"
- "AMSMediaRestrictionsEditTask"
- "AMSMediaRestrictionsPerformer"
- "AMSMediaRestrictionsRemoveProfileLockTask"
- "AMSMediaRestrictionsResult"
- "AMSMediaRestrictionsSetupProfileLockTask"
- "AMSMediaRestrictionsSetupTask"
- "AMSMediaRestrictionsValue"
- "AMSMediaRestrictionsVerifyProfileLockTask"
- "AUTH_WITH_RESTRICTION"
- "AppleMediaServices.MediaRestrictionsPerformer"
- "AppleMediaServices.MediaRestrictionsRatingItem"
- "AppleMediaServices.MediaRestrictionsResult"
- "AppleMediaServices.MediaRestrictionsValue"
- "AppleMediaServices/MediaRestrictionsValue.swift"
- "Calling didFailWithError"
- "Cancelling QR code handler"
- "Configuration is not valid"
- "Fetching QR code data"
- "Handler configured a QR Code. result = "
- "Handler reported a failure. error = "
- "Handler returned a result. result = "
- "Handler updated its status. status = "
- "Invalid ratingItem value"
- "Invalid type for "
- "MediaRestrictionsResult("
- "Missing Polling URL"
- "Missing Setup URL"
- "Missing necessary values to build the polling url"
- "Pausing polling will check again in "
- "Performing QR Code fetch"
- "Performing Status Check"
- "Polling QR code status"
- "Polling continues..."
- "Polling failed (consecutive failures: "
- "QR code fetch failed. error = "
- "Server requested polling stop"
- "Status result was not 'MediaRestrictionsQRAuthResult'"
- "T@\"AMSMediaRestrictionsRatingItem\",N,R"
- "T@\"AMSURLResult\",N,R,VrawResult"
- "T@\"NSDictionary\",N,R"
- "T@\"NSNumber\",N,R,VratingValue"
- "T@\"NSString\",C,N,V_editToken"
- "T@,N,R"
- "The provided bag did not contain a value for the profileLockDelete key"
- "The provided bag did not contain a value for the profileLockEdit key"
- "The provided bag did not contain a value for the profileLockSetup key"
- "The provided bag did not contain a value for the profileLockVerify key"
- "The provided bag did not contain a value for the restrictionsDisable key"
- "The provided bag did not contain a value for the restrictionsEdit key"
- "The provided bag did not contain a value for the restrictionsGet key"
- "The provided bag did not contain a value for the restrictionsQRAuthPolling key"
- "The provided bag did not contain a value for the restrictionsQRAuthSetup key"
- "The provided bag did not contain a value for the restrictionsSetup key"
- "Tq,N,R,VvalueType"
- "Unexpected parameter: "
- "Unknown restriction key: "
- "Updated polling interval to "
- "_TtC18AppleMediaServices27MediaRestrictionsQRAuthTask"
- "_TtCC18AppleMediaServices26MediaRestrictionsPerformerP33_36668741CA9525741226C3D3F7E765C314PromiseHandler"
- "_clearGroupedFollowUpWithBackingIdentifier:"
- "_editToken"
- "_isHardwareOfferFollowUpGroupingEnabled"
- "_makeGroupedHardwareFollowUpItemFromItems:DSID:"
- "_postGroupedFollowUpItem:"
- "_updateGroupedHardwareFollowUpItemWithItems:DSID:error:"
- "allowPurchasesValue"
- "ams-ui://amsui.apple.com/dynamic/marketing#route=hardwareOffers"
- "bagValues"
- "dictionaryValue"
- "disableRestrictions"
- "editProfileLockWithPasscode:"
- "editToken"
- "editWithRestricitons:"
- "expirationDateInMillis"
- "hasRestrictionKeys"
- "initWithAccount:editToken:bag:"
- "initWithBoolValue:"
- "initWithIntValue:"
- "initWithRatingItem:"
- "initWithRatingSystem:intValue:"
- "initWithRatingSystem:numberValue:"
- "isProfileLockSet"
- "isProfileLockSetValue"
- "isSuccess"
- "movieRestriction"
- "only one of passcode or restrictions is permitted"
- "performSetupWithRestrictions:"
- "performWithPasscode:"
- "performWithRestrictions:"
- "ratingItem"
- "ratingSystem"
- "removeProfileLockWithPasscode:"
- "restrictionsQRAuthPolling"
- "restrictionsQRAuthSetup"
- "setDateStyle:"
- "setEditToken:"
- "setTimeStyle:"
- "setupProfileLockWithPasscode:"
- "tvRestriction"
- "verifyProfileLockWithPasscode:"
- "withBool:"
- "withInt:"
- "withRatingItem:"
- "withString:"
- "x-apple-user-agent"

```
