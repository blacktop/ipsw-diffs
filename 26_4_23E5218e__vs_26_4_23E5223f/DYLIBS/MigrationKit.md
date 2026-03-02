## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-1224.100.83.0.0
-  __TEXT.__text: 0x6f6ec0
-  __TEXT.__auth_stubs: 0x5db0
-  __TEXT.__objc_methlist: 0x6c14
-  __TEXT.__const: 0x2ec20
-  __TEXT.__oslogstring: 0xeadc
-  __TEXT.__gcc_except_tab: 0x1494
-  __TEXT.__cstring: 0x1af81
-  __TEXT.__constg_swiftt: 0xd8fc
-  __TEXT.__swift5_typeref: 0xab53
+1224.100.94.0.0
+  __TEXT.__text: 0x6e617c
+  __TEXT.__auth_stubs: 0x5e00
+  __TEXT.__objc_methlist: 0x6d04
+  __TEXT.__const: 0x355d0
+  __TEXT.__oslogstring: 0xeb5c
+  __TEXT.__cstring: 0x15281
+  __TEXT.__gcc_except_tab: 0x1590
+  __TEXT.__constg_swiftt: 0xdaa4
+  __TEXT.__swift5_typeref: 0xaa6b
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0xb162
-  __TEXT.__swift5_fieldmd: 0xc530
+  __TEXT.__swift5_reflstr: 0xb202
+  __TEXT.__swift5_fieldmd: 0xc594
   __TEXT.__swift5_assocty: 0x1f10
   __TEXT.__swift5_proto: 0x20ac
-  __TEXT.__swift5_types: 0xbb0
-  __TEXT.__swift_as_entry: 0x1020
-  __TEXT.__swift_as_ret: 0x1348
-  __TEXT.__swift5_capture: 0x28f0
+  __TEXT.__swift5_types: 0xbb4
+  __TEXT.__swift_as_entry: 0x1038
+  __TEXT.__swift_as_ret: 0x1364
+  __TEXT.__swift5_capture: 0x29cc
   __TEXT.__swift5_protos: 0x13c
   __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__unwind_info: 0x14590
-  __TEXT.__eh_frame: 0x38990
-  __TEXT.__objc_classname: 0x3cf1
-  __TEXT.__objc_methname: 0x13316
-  __TEXT.__objc_methtype: 0x441e
-  __TEXT.__objc_stubs: 0xf5c0
-  __DATA_CONST.__got: 0x1a68
-  __DATA_CONST.__const: 0xa10
-  __DATA_CONST.__objc_classlist: 0xb50
+  __TEXT.__unwind_info: 0x144b0
+  __TEXT.__eh_frame: 0x38eb8
+  __TEXT.__objc_classname: 0x3d71
+  __TEXT.__objc_methname: 0x13656
+  __TEXT.__objc_methtype: 0x448e
+  __TEXT.__objc_stubs: 0xf700
+  __DATA_CONST.__got: 0x2190
+  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__objc_classlist: 0xb60
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a18
+  __DATA_CONST.__objc_selrefs: 0x4a90
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x310
+  __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x488
-  __AUTH_CONST.__auth_got: 0x2ef0
-  __AUTH_CONST.__const: 0x14cf8
-  __AUTH_CONST.__cfstring: 0x5960
-  __AUTH_CONST.__objc_const: 0x19a88
+  __AUTH_CONST.__auth_got: 0x2f18
+  __AUTH_CONST.__const: 0x14e80
+  __AUTH_CONST.__cfstring: 0x5ac0
+  __AUTH_CONST.__objc_const: 0x19f58
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH.__objc_data: 0x74b8
-  __AUTH.__data: 0x14bf8
-  __DATA.__objc_ivar: 0x794
-  __DATA.__data: 0xc798
-  __DATA.__bss: 0x397c0
+  __AUTH.__objc_data: 0x7570
+  __AUTH.__data: 0x14e48
+  __DATA.__objc_ivar: 0x7ac
+  __DATA.__data: 0xc738
+  __DATA.__bss: 0x39760
   __DATA.__common: 0x14a8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F43FF893-2BD2-385D-ACBF-379C53B86761
-  Functions: 21445
-  Symbols:   15010
-  CStrings:  9771
+  UUID: AB61EA30-3327-3150-9C27-E0B00C5525C6
+  Functions: 21498
+  Symbols:   15338
+  CStrings:  9005
 
Symbols:
+ +[MKUSBRoleSwap startMonitoringUSBStateWithCallback:]
+ +[MKUSBRoleSwap stopMonitoringUSBState]
+ -[MKUSBMonitoringState .cxx_destruct]
+ -[MKUSBMonitoringState callbackQueue]
+ -[MKUSBMonitoringState callback]
+ -[MKUSBMonitoringState checkAndInvokeCallbackForService:]
+ -[MKUSBMonitoringState dealloc]
+ -[MKUSBMonitoringState handleServiceMatched:]
+ -[MKUSBMonitoringState init]
+ -[MKUSBMonitoringState interestNotifier]
+ -[MKUSBMonitoringState notificationPort]
+ -[MKUSBMonitoringState service]
+ -[MKUSBMonitoringState setCallback:]
+ -[MKUSBMonitoringState setCallbackQueue:]
+ -[MKUSBMonitoringState setInterestNotifier:]
+ -[MKUSBMonitoringState setNotificationPort:]
+ -[MKUSBMonitoringState setService:]
+ -[MKUSBMonitoringState setStateNotifier:]
+ -[MKUSBMonitoringState stateNotifier]
+ GCC_except_table29
+ GCC_except_table30
+ _CFRunLoopGetMain
+ _CFRunLoopRemoveSource
+ _CNLabelContactRelationAssistant
+ _CNLabelContactRelationAunt
+ _CNLabelContactRelationAuntFathersBrothersWife
+ _CNLabelContactRelationAuntFathersElderBrothersWife
+ _CNLabelContactRelationAuntFathersElderSister
+ _CNLabelContactRelationAuntFathersSister
+ _CNLabelContactRelationAuntFathersYoungerBrothersWife
+ _CNLabelContactRelationAuntFathersYoungerSister
+ _CNLabelContactRelationAuntMothersBrothersWife
+ _CNLabelContactRelationAuntMothersElderSister
+ _CNLabelContactRelationAuntMothersSister
+ _CNLabelContactRelationAuntMothersYoungerSister
+ _CNLabelContactRelationAuntParentsElderSister
+ _CNLabelContactRelationAuntParentsSister
+ _CNLabelContactRelationAuntParentsYoungerSister
+ _CNLabelContactRelationBoyfriend
+ _CNLabelContactRelationBrother
+ _CNLabelContactRelationBrotherInLaw
+ _CNLabelContactRelationBrotherInLawElderSistersHusband
+ _CNLabelContactRelationBrotherInLawHusbandsBrother
+ _CNLabelContactRelationBrotherInLawHusbandsSistersHusband
+ _CNLabelContactRelationBrotherInLawSistersHusband
+ _CNLabelContactRelationBrotherInLawSpousesBrother
+ _CNLabelContactRelationBrotherInLawWifesBrother
+ _CNLabelContactRelationBrotherInLawWifesSistersHusband
+ _CNLabelContactRelationBrotherInLawYoungerSistersHusband
+ _CNLabelContactRelationChild
+ _CNLabelContactRelationChildInLaw
+ _CNLabelContactRelationCoBrotherInLaw
+ _CNLabelContactRelationCoFatherInLaw
+ _CNLabelContactRelationCoMotherInLaw
+ _CNLabelContactRelationCoParentInLaw
+ _CNLabelContactRelationCoSiblingInLaw
+ _CNLabelContactRelationCoSisterInLaw
+ _CNLabelContactRelationColleague
+ _CNLabelContactRelationCousin
+ _CNLabelContactRelationCousinFathersBrothersDaughter
+ _CNLabelContactRelationCousinFathersBrothersSon
+ _CNLabelContactRelationCousinFathersSistersDaughter
+ _CNLabelContactRelationCousinFathersSistersSon
+ _CNLabelContactRelationCousinGrandparentsSiblingsChild
+ _CNLabelContactRelationCousinGrandparentsSiblingsDaughter
+ _CNLabelContactRelationCousinGrandparentsSiblingsSon
+ _CNLabelContactRelationCousinMothersBrothersDaughter
+ _CNLabelContactRelationCousinMothersBrothersSon
+ _CNLabelContactRelationCousinMothersSistersDaughter
+ _CNLabelContactRelationCousinMothersSistersSon
+ _CNLabelContactRelationCousinOrSiblingsChild
+ _CNLabelContactRelationCousinParentsSiblingsChild
+ _CNLabelContactRelationCousinParentsSiblingsDaughter
+ _CNLabelContactRelationCousinParentsSiblingsSon
+ _CNLabelContactRelationDaughter
+ _CNLabelContactRelationDaughterInLaw
+ _CNLabelContactRelationDaughterInLawOrSisterInLaw
+ _CNLabelContactRelationDaughterInLawOrStepdaughter
+ _CNLabelContactRelationElderBrother
+ _CNLabelContactRelationElderBrotherInLaw
+ _CNLabelContactRelationElderCousin
+ _CNLabelContactRelationElderCousinFathersBrothersDaughter
+ _CNLabelContactRelationElderCousinFathersBrothersSon
+ _CNLabelContactRelationElderCousinFathersSistersDaughter
+ _CNLabelContactRelationElderCousinFathersSistersSon
+ _CNLabelContactRelationElderCousinMothersBrothersDaughter
+ _CNLabelContactRelationElderCousinMothersBrothersSon
+ _CNLabelContactRelationElderCousinMothersSiblingsDaughterOrFathersSistersDaughter
+ _CNLabelContactRelationElderCousinMothersSiblingsSonOrFathersSistersSon
+ _CNLabelContactRelationElderCousinMothersSistersDaughter
+ _CNLabelContactRelationElderCousinMothersSistersSon
+ _CNLabelContactRelationElderCousinParentsSiblingsDaughter
+ _CNLabelContactRelationElderCousinParentsSiblingsSon
+ _CNLabelContactRelationElderSibling
+ _CNLabelContactRelationElderSiblingInLaw
+ _CNLabelContactRelationElderSister
+ _CNLabelContactRelationElderSisterInLaw
+ _CNLabelContactRelationEldestBrother
+ _CNLabelContactRelationEldestSister
+ _CNLabelContactRelationFather
+ _CNLabelContactRelationFatherInLaw
+ _CNLabelContactRelationFatherInLawHusbandsFather
+ _CNLabelContactRelationFatherInLawOrStepfather
+ _CNLabelContactRelationFatherInLawWifesFather
+ _CNLabelContactRelationFemaleCousin
+ _CNLabelContactRelationFemaleFriend
+ _CNLabelContactRelationFemalePartner
+ _CNLabelContactRelationFriend
+ _CNLabelContactRelationGirlfriend
+ _CNLabelContactRelationGirlfriendOrBoyfriend
+ _CNLabelContactRelationGrandaunt
+ _CNLabelContactRelationGrandchild
+ _CNLabelContactRelationGrandchildOrSiblingsChild
+ _CNLabelContactRelationGranddaughter
+ _CNLabelContactRelationGranddaughterDaughtersDaughter
+ _CNLabelContactRelationGranddaughterOrNiece
+ _CNLabelContactRelationGranddaughterSonsDaughter
+ _CNLabelContactRelationGrandfather
+ _CNLabelContactRelationGrandfatherFathersFather
+ _CNLabelContactRelationGrandfatherMothersFather
+ _CNLabelContactRelationGrandmother
+ _CNLabelContactRelationGrandmotherFathersMother
+ _CNLabelContactRelationGrandmotherMothersMother
+ _CNLabelContactRelationGrandnephew
+ _CNLabelContactRelationGrandnephewBrothersGrandson
+ _CNLabelContactRelationGrandnephewSistersGrandson
+ _CNLabelContactRelationGrandniece
+ _CNLabelContactRelationGrandnieceBrothersGranddaughter
+ _CNLabelContactRelationGrandnieceSistersGranddaughter
+ _CNLabelContactRelationGrandparent
+ _CNLabelContactRelationGrandson
+ _CNLabelContactRelationGrandsonDaughtersSon
+ _CNLabelContactRelationGrandsonOrNephew
+ _CNLabelContactRelationGrandsonSonsSon
+ _CNLabelContactRelationGranduncle
+ _CNLabelContactRelationGreatGrandchild
+ _CNLabelContactRelationGreatGrandchildOrSiblingsGrandchild
+ _CNLabelContactRelationGreatGranddaughter
+ _CNLabelContactRelationGreatGrandfather
+ _CNLabelContactRelationGreatGrandmother
+ _CNLabelContactRelationGreatGrandparent
+ _CNLabelContactRelationGreatGrandson
+ _CNLabelContactRelationHusband
+ _CNLabelContactRelationMaleCousin
+ _CNLabelContactRelationMaleFriend
+ _CNLabelContactRelationMalePartner
+ _CNLabelContactRelationManager
+ _CNLabelContactRelationMother
+ _CNLabelContactRelationMotherInLaw
+ _CNLabelContactRelationMotherInLawHusbandsMother
+ _CNLabelContactRelationMotherInLawOrStepmother
+ _CNLabelContactRelationMotherInLawWifesMother
+ _CNLabelContactRelationNephew
+ _CNLabelContactRelationNephewBrothersSon
+ _CNLabelContactRelationNephewBrothersSonOrHusbandsSiblingsSon
+ _CNLabelContactRelationNephewOrCousin
+ _CNLabelContactRelationNephewSistersSon
+ _CNLabelContactRelationNephewSistersSonOrWifesSiblingsSon
+ _CNLabelContactRelationNiece
+ _CNLabelContactRelationNieceBrothersDaughter
+ _CNLabelContactRelationNieceBrothersDaughterOrHusbandsSiblingsDaughter
+ _CNLabelContactRelationNieceOrCousin
+ _CNLabelContactRelationNieceSistersDaughter
+ _CNLabelContactRelationNieceSistersDaughterOrWifesSiblingsDaughter
+ _CNLabelContactRelationParent
+ _CNLabelContactRelationParentInLaw
+ _CNLabelContactRelationParentsElderSibling
+ _CNLabelContactRelationParentsSibling
+ _CNLabelContactRelationParentsSiblingFathersElderSibling
+ _CNLabelContactRelationParentsSiblingFathersSibling
+ _CNLabelContactRelationParentsSiblingFathersYoungerSibling
+ _CNLabelContactRelationParentsSiblingMothersElderSibling
+ _CNLabelContactRelationParentsSiblingMothersSibling
+ _CNLabelContactRelationParentsSiblingMothersYoungerSibling
+ _CNLabelContactRelationParentsYoungerSibling
+ _CNLabelContactRelationPartner
+ _CNLabelContactRelationSibling
+ _CNLabelContactRelationSiblingInLaw
+ _CNLabelContactRelationSiblingsChild
+ _CNLabelContactRelationSister
+ _CNLabelContactRelationSisterInLaw
+ _CNLabelContactRelationSisterInLawBrothersWife
+ _CNLabelContactRelationSisterInLawElderBrothersWife
+ _CNLabelContactRelationSisterInLawHusbandsBrothersWife
+ _CNLabelContactRelationSisterInLawHusbandsSister
+ _CNLabelContactRelationSisterInLawSpousesSister
+ _CNLabelContactRelationSisterInLawWifesBrothersWife
+ _CNLabelContactRelationSisterInLawWifesSister
+ _CNLabelContactRelationSisterInLawYoungerBrothersWife
+ _CNLabelContactRelationSon
+ _CNLabelContactRelationSonInLaw
+ _CNLabelContactRelationSonInLawOrBrotherInLaw
+ _CNLabelContactRelationSonInLawOrStepson
+ _CNLabelContactRelationSpouse
+ _CNLabelContactRelationStepbrother
+ _CNLabelContactRelationStepchild
+ _CNLabelContactRelationStepdaughter
+ _CNLabelContactRelationStepfather
+ _CNLabelContactRelationStepmother
+ _CNLabelContactRelationStepparent
+ _CNLabelContactRelationStepsister
+ _CNLabelContactRelationStepson
+ _CNLabelContactRelationTeacher
+ _CNLabelContactRelationUncle
+ _CNLabelContactRelationUncleFathersBrother
+ _CNLabelContactRelationUncleFathersElderBrother
+ _CNLabelContactRelationUncleFathersElderSistersHusband
+ _CNLabelContactRelationUncleFathersSistersHusband
+ _CNLabelContactRelationUncleFathersYoungerBrother
+ _CNLabelContactRelationUncleFathersYoungerSistersHusband
+ _CNLabelContactRelationUncleMothersBrother
+ _CNLabelContactRelationUncleMothersElderBrother
+ _CNLabelContactRelationUncleMothersSistersHusband
+ _CNLabelContactRelationUncleMothersYoungerBrother
+ _CNLabelContactRelationUncleParentsBrother
+ _CNLabelContactRelationUncleParentsElderBrother
+ _CNLabelContactRelationUncleParentsYoungerBrother
+ _CNLabelContactRelationWife
+ _CNLabelContactRelationYoungerBrother
+ _CNLabelContactRelationYoungerBrotherInLaw
+ _CNLabelContactRelationYoungerCousin
+ _CNLabelContactRelationYoungerCousinFathersBrothersDaughter
+ _CNLabelContactRelationYoungerCousinFathersBrothersSon
+ _CNLabelContactRelationYoungerCousinFathersSistersDaughter
+ _CNLabelContactRelationYoungerCousinFathersSistersSon
+ _CNLabelContactRelationYoungerCousinMothersBrothersDaughter
+ _CNLabelContactRelationYoungerCousinMothersBrothersSon
+ _CNLabelContactRelationYoungerCousinMothersSiblingsDaughterOrFathersSistersDaughter
+ _CNLabelContactRelationYoungerCousinMothersSiblingsSonOrFathersSistersSon
+ _CNLabelContactRelationYoungerCousinMothersSistersDaughter
+ _CNLabelContactRelationYoungerCousinMothersSistersSon
+ _CNLabelContactRelationYoungerCousinParentsSiblingsDaughter
+ _CNLabelContactRelationYoungerCousinParentsSiblingsSon
+ _CNLabelContactRelationYoungerSibling
+ _CNLabelContactRelationYoungerSiblingInLaw
+ _CNLabelContactRelationYoungerSister
+ _CNLabelContactRelationYoungerSisterInLaw
+ _CNLabelContactRelationYoungestBrother
+ _CNLabelContactRelationYoungestSister
+ _CNLabelDateAnniversary
+ _CNLabelEmailiCloud
+ _CNLabelOther
+ _CNLabelPhoneNumberAssistant
+ _CNLabelPhoneNumberCallback
+ _CNLabelPhoneNumberCar
+ _CNLabelPhoneNumberCompanyMain
+ _CNLabelPhoneNumberHomeFax
+ _CNLabelPhoneNumberISDN
+ _CNLabelPhoneNumberMain
+ _CNLabelPhoneNumberMobile
+ _CNLabelPhoneNumberOtherFax
+ _CNLabelPhoneNumberPager
+ _CNLabelPhoneNumberRadio
+ _CNLabelPhoneNumberTTY
+ _CNLabelPhoneNumberTelex
+ _CNLabelPhoneNumberWorkFax
+ _CNLabelPhoneNumberiPhone
+ _CNLabelSchool
+ _IOObjectRetain
+ _IOServiceAddInterestNotification
+ _OBJC_CLASS_$_MKUSBMonitoringState
+ _OBJC_IVAR_$_MKUSBMonitoringState._callback
+ _OBJC_IVAR_$_MKUSBMonitoringState._callbackQueue
+ _OBJC_IVAR_$_MKUSBMonitoringState._interestNotifier
+ _OBJC_IVAR_$_MKUSBMonitoringState._notificationPort
+ _OBJC_IVAR_$_MKUSBMonitoringState._service
+ _OBJC_IVAR_$_MKUSBMonitoringState._stateNotifier
+ _OBJC_METACLASS_$_MKUSBMonitoringState
+ __DATA__TtCV12MigrationKit18OSMigrationMessageP33_F2D56D5E7DEA747D877788BB4B1FFC5113_StorageClass
+ __IVARS__TtCV12MigrationKit18OSMigrationMessageP33_F2D56D5E7DEA747D877788BB4B1FFC5113_StorageClass
+ __METACLASS_DATA__TtCV12MigrationKit18OSMigrationMessageP33_F2D56D5E7DEA747D877788BB4B1FFC5113_StorageClass
+ __OBJC_$_INSTANCE_METHODS_MKUSBMonitoringState
+ __OBJC_$_INSTANCE_VARIABLES_MKUSBMonitoringState
+ __OBJC_$_PROP_LIST_MKUSBMonitoringState
+ __OBJC_CLASS_RO_$_MKUSBMonitoringState
+ __OBJC_METACLASS_RO_$_MKUSBMonitoringState
+ __ZL16_monitoringState
+ __ZL21usb_interest_callbackPvjjS_
+ __ZL26usb_state_changed_callbackPvj
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB9nqe210106ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqe210106EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9nqe210106ERKS6_S9_
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
+ __ZNSt3__113unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigNS_4hashIS6_EENS_8equal_toIS6_EENS4_INS_4pairIKS6_S7_EEEEED1B9nqe210106Ev
+ __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12migrationkit9signature14get_identifierEPKhmE3$_0EEEEEvPv
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9nqe210106EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9nqe210106EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9nqe210106EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE3sigEEPvEEEEEclB9nqe210106EPSC_
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ___57-[MKUSBMonitoringState checkAndInvokeCallbackForService:]_block_invoke
+ ___block_descriptor_41_ea8_32bs_e5_v8?0ls32l8
+ ___swift_get_extra_inhabitant_index.119Tm
+ ___swift_store_extra_inhabitant_index.120Tm
+ _dispatch_sync
+ _objc_msgSend$checkAndInvokeCallbackForService:
+ _objc_msgSend$handleServiceMatched:
+ _objc_msgSend$notificationPort
+ _objc_msgSend$previewLayer
+ _objc_msgSend$setCallback:
+ _objc_msgSend$setCallbackQueue:
+ _objc_msgSend$setNotificationPort:
+ _objc_msgSend$setStateNotifier:
+ _objc_msgSend$startMonitoringUSBStateWithCallback:
+ _objc_msgSend$stateNotifier
+ _objc_msgSend$stopMonitoringUSBState
+ _objc_retainBlock
+ _objectdestroy.15Tm
+ _objectdestroy.29Tm
+ _symbolic Ig_
+ _symbolic SayScCySb_____GG s5NeverO
+ _symbolic SbIeAgHr_
+ _symbolic ScGySbG
+ _symbolic So19AVCaptureConnectionC
+ _symbolic _____ 12MigrationKit18OSMigrationMessageV13_StorageClass33_F2D56D5E7DEA747D877788BB4B1FFC51LLC
+ _symbolic _____SgXwz_Xx 12MigrationKit10NCMNetworkC
+ _symbolic _____yScCySb_____GG s23_ContiguousArrayStorageC s5NeverO
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB9foe210106ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9foe210106EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9foe210106ERKS6_S9_
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106ILi0EEEPKc
- __ZNSt3__113unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigNS_4hashIS6_EENS_8equal_toIS6_EENS4_INS_4pairIKS6_S7_EEEEED1B9foe210106Ev
- __ZNSt3__117__call_once_proxyB9foe210106INS_5tupleIJOZN12migrationkit9signature14get_identifierEPKhmE3$_0EEEEEvPv
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9foe210106EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9foe210106EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9foe210106EPKcm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE3sigEEPvEEEEEclB9foe210106EPSC_
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ___swift_get_extra_inhabitant_index.72Tm
- ___swift_store_extra_inhabitant_index.73Tm
- _objc_msgSend$isUSBConnected
- _objectdestroy.16Tm
- _symbolic Si______t 21InternalSwiftProtobuf8_NameMapV0D11DescriptionO
- _symbolic So26AVCaptureVideoPreviewLayerCSgXw
- _symbolic So26AVCaptureVideoPreviewLayerCSgXwz_Xx
- _symbolic _____ySi______tG s23_ContiguousArrayStorageC 21InternalSwiftProtobuf8_NameMapV0G11DescriptionO
- _symbolic _____y_AAy______y______GSSGSbG 10Foundation20PredicateExpressionsO7KeyPathV AC8VariableV 12MigrationKit29MessagePersistenceParticipantC
- _symbolic _____y_SbG 10Foundation20PredicateExpressionsO5ValueV
- _symbolic _____y______y_ABy______y______GSSGSbG_____y_SbGG 10Foundation20PredicateExpressionsO5EqualV AC7KeyPathV AC8VariableV 12MigrationKit29MessagePersistenceParticipantC AC5ValueV
- _symbolic _____y______y______GSbG 10Foundation20PredicateExpressionsO7KeyPathV AC8VariableV 12MigrationKit29MessagePersistenceParticipantC
- _symbolic _____y______y______y______GSbG_____y_SbGG 10Foundation20PredicateExpressionsO5EqualV AC7KeyPathV AC8VariableV 12MigrationKit29MessagePersistenceParticipantC AC5ValueV
- _symbolic _____y______y______y______y______GSbG_____y_SbGGABy_ACy_ACy_AFSSGSbGAIGG 10Foundation20PredicateExpressionsO11ConjunctionV AC5EqualV AC7KeyPathV AC8VariableV 12MigrationKit29MessagePersistenceParticipantC AC5ValueV
CStrings:
+ "@?"
+ "@?16@0:8"
+ "App %{public}s has distributorType: %{public}s"
+ "Attempting NCM fallback"
+ "B24@0:8@?16"
+ "Failed to get default account for service %{public}s"
+ "Failed to start USB state monitoring"
+ "Home Screen Layout"
+ "I"
+ "I16@0:8"
+ "IOGeneralInterest"
+ "IOServiceMatched"
+ "MKUSBMonitoringState"
+ "NCM activated successfully"
+ "NCM activation failed - continuing without NCM"
+ "NCM activation wait timed out - continuing without NCM"
+ "No ASC data returned for bundle IDs: %{public}s"
+ "Passwords and Passkeys"
+ "Photos and Videos"
+ "Starting NCM monitoring"
+ "Starting USB state monitoring..."
+ "Stopped USB state monitoring"
+ "Successfully started USB state monitoring"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callbackQueue"
+ "T@?,C,N,V_callback"
+ "TI,N,V_interestNotifier"
+ "TI,N,V_service"
+ "TI,N,V_stateNotifier"
+ "T^{IONotificationPort=},N,V_notificationPort"
+ "USB already configured"
+ "USB connected - attempting NCM activation"
+ "USB connected - configuring device mode and NCM"
+ "USB disconnected"
+ "Waiting up to %lld seconds for USB configuration"
+ "[MKUSBMonitoringState] Failed to register interest notification: 0x%x"
+ "[MKUSBMonitoringState] Successfully registered interest notification"
+ "[MKUSBMonitoringState] USB service matched - setting up interest notification"
+ "[MKUSBMonitoringState] USB state check: DataRole=%d (%s), Connected=%s"
+ "[MKUSBRoleSwap] Callback cannot be nil"
+ "[MKUSBRoleSwap] Failed to create matching dictionary"
+ "[MKUSBRoleSwap] Failed to create notification port"
+ "[MKUSBRoleSwap] IOServiceAddMatchingNotification failed: 0x%x"
+ "[MKUSBRoleSwap] Stopped USB state monitoring"
+ "[MKUSBRoleSwap] Successfully started USB state monitoring"
+ "[MKUSBRoleSwap] USB monitoring is already active"
+ "^{IONotificationPort=}"
+ "^{IONotificationPort=}16@0:8"
+ "_TtCV12MigrationKit18OSMigrationMessageP33_F2D56D5E7DEA747D877788BB4B1FFC5113_StorageClass"
+ "_callback"
+ "_callbackQueue"
+ "_direction"
+ "_interestNotifier"
+ "_nonStandardContentType"
+ "_notificationPort"
+ "_outgoingStatus"
+ "_protocolType"
+ "_stateNotifier"
+ "_timestampMillis"
+ "callback"
+ "callbackQueue"
+ "checkAndInvokeCallbackForService:"
+ "com.apple.MigrationKit.NCMNetwork.waiters"
+ "com.apple.MigrationKit.USBStateMonitor"
+ "handleServiceMatched:"
+ "init(conversation:participants:message:)"
+ "interestNotifier"
+ "isMonitoring"
+ "notificationPort"
+ "previewLayer"
+ "serviceName"
+ "setCallback:"
+ "setCallbackQueue:"
+ "setInterestNotifier:"
+ "setNotificationPort:"
+ "setStateNotifier:"
+ "startMonitoringUSBStateWithCallback:"
+ "stateNotifier"
+ "stopMonitoringUSBState"
+ "usbConfigurationWaiters"
+ "usbConfigured"
+ "v20@0:8I16"
+ "v24@0:8^{IONotificationPort=}16"
+ "waitForNCMActivation(timeout:)"
+ "waiterQueue"
+ "will create a participant. address=%s, sequence_id=%lld, service=%s"
- "ALARM_REPEATED_DAY_FRIDAY"
- "ALARM_REPEATED_DAY_MONDAY"
- "ALARM_REPEATED_DAY_NEVER"
- "ALARM_REPEATED_DAY_SATURDAY"
- "ALARM_REPEATED_DAY_SUNDAY"
- "ALARM_REPEATED_DAY_THURSDAY"
- "ALARM_REPEATED_DAY_TUESDAY"
- "ALARM_REPEATED_DAY_UNSPECIFIED"
- "ALARM_REPEATED_DAY_WEDNESDAY"
- "ALARM_STATE_DISABLED"
- "ALARM_STATE_ENABLED"
- "ALARM_STATE_UNSPECIFIED"
- "ALARM_VIBRATION_TYPE_DISABLED"
- "ALARM_VIBRATION_TYPE_ENABLED"
- "ALARM_VIBRATION_TYPE_UNSPECIFIED"
- "APP_DISTRIBUTION_TYPE_ALT_MARKETPLACE"
- "APP_DISTRIBUTION_TYPE_APP_STORE"
- "APP_DISTRIBUTION_TYPE_TEST_FLIGHT"
- "APP_DISTRIBUTION_TYPE_UNKNOWN"
- "APP_DISTRIBUTION_TYPE_WEB_DISTRIBUTED"
- "ASSET_SUBTYPE_ADJUSTED"
- "ASSET_SUBTYPE_ANIMATED"
- "ASSET_SUBTYPE_ORIGINAL"
- "ASSET_SUBTYPE_SCREENSHOT"
- "ASSET_SUBTYPE_UNSPECIFIED"
- "ASSET_TYPE_PHOTO"
- "ASSET_TYPE_UNSPECIFIED"
- "ASSET_TYPE_VIDEO"
- "ATTESTATION_STATUS_ERROR_HASH_TOO_SHORT"
- "ATTESTATION_STATUS_ERROR_NOT_AVAILABLE"
- "ATTESTATION_STATUS_SUCCESS"
- "ATTESTATION_STATUS_UNKNOWN"
- "CALENDAR_DAY_FRIDAY"
- "CALENDAR_DAY_MONDAY"
- "CALENDAR_DAY_NOTSET"
- "CALENDAR_DAY_SATURDAY"
- "CALENDAR_DAY_SUNDAY"
- "CALENDAR_DAY_THURSDAY"
- "CALENDAR_DAY_TUESDAY"
- "CALENDAR_DAY_UNKNOWN"
- "CALENDAR_DAY_WEDNESDAY"
- "CALENDAR_EVENT_AVAILABILITY_BUSY"
- "CALENDAR_EVENT_AVAILABILITY_FREE"
- "CALENDAR_EVENT_AVAILABILITY_NOT_SUPPORTED"
- "CALENDAR_EVENT_AVAILABILITY_TENTATIVE"
- "CALENDAR_EVENT_AVAILABILITY_UNAVAILABLE"
- "CALENDAR_EVENT_AVAILABILITY_UNKNOWN"
- "CALENDAR_EVENT_STATUS_CANCELED"
- "CALENDAR_EVENT_STATUS_CONFIRMED"
- "CALENDAR_EVENT_STATUS_NONE"
- "CALENDAR_EVENT_STATUS_TENTATIVE"
- "CALENDAR_EVENT_STATUS_UNKNOWN"
- "CALENDAR_PARTICIPANT_ROLE_CHAIR"
- "CALENDAR_PARTICIPANT_ROLE_NONPARTICIPANT"
- "CALENDAR_PARTICIPANT_ROLE_OPTIONAL"
- "CALENDAR_PARTICIPANT_ROLE_REQUIRED"
- "CALENDAR_PARTICIPANT_ROLE_UNKNOWN"
- "CALENDAR_PARTICIPANT_STATUS_ACCEPTED"
- "CALENDAR_PARTICIPANT_STATUS_COMPLETED"
- "CALENDAR_PARTICIPANT_STATUS_DECLINED"
- "CALENDAR_PARTICIPANT_STATUS_DELEGATED"
- "CALENDAR_PARTICIPANT_STATUS_IN_PROCESS"
- "CALENDAR_PARTICIPANT_STATUS_PENDING"
- "CALENDAR_PARTICIPANT_STATUS_TENTATIVE"
- "CALENDAR_PARTICIPANT_STATUS_UNKNOWN"
- "CALENDAR_PARTICIPANT_TYPE_GROUP"
- "CALENDAR_PARTICIPANT_TYPE_PERSON"
- "CALENDAR_PARTICIPANT_TYPE_RESOURCE"
- "CALENDAR_PARTICIPANT_TYPE_ROOM"
- "CALENDAR_PARTICIPANT_TYPE_UNKNOWN"
- "CALENDAR_RECURRENCE_FREQUENCY_DAILY"
- "CALENDAR_RECURRENCE_FREQUENCY_MONTHLY"
- "CALENDAR_RECURRENCE_FREQUENCY_UNKNOWN"
- "CALENDAR_RECURRENCE_FREQUENCY_WEEKLY"
- "CALENDAR_RECURRENCE_FREQUENCY_YEARLY"
- "CALENDAR_TYPE_BIRTHDAY"
- "CALENDAR_TYPE_CAL_DAV"
- "CALENDAR_TYPE_EXCHANGE"
- "CALENDAR_TYPE_LOCAL"
- "CALENDAR_TYPE_SUBSCRIPTION"
- "CALENDAR_TYPE_UNKNOWN"
- "CALL_MEDIA_TYPE_AUDIO"
- "CALL_MEDIA_TYPE_UNSPECIFIED"
- "CALL_MEDIA_TYPE_VIDEO"
- "CALL_TTY_TYPE_DIRECT"
- "CALL_TTY_TYPE_NONE"
- "CALL_TTY_TYPE_RELAY"
- "CALL_TTY_TYPE_UNSPECIFIED"
- "CALL_TYPE_ANSWERED_ELSEWHERE"
- "CALL_TYPE_BLOCKED"
- "CALL_TYPE_CANCELLED"
- "CALL_TYPE_INCOMING"
- "CALL_TYPE_MISSED"
- "CALL_TYPE_OUTGOING"
- "CALL_TYPE_UNSPECIFIED"
- "CAPTION_STYLE_COLOR_BLACK"
- "CAPTION_STYLE_COLOR_BLUE"
- "CAPTION_STYLE_COLOR_CYAN"
- "CAPTION_STYLE_COLOR_GREEN"
- "CAPTION_STYLE_COLOR_MAGENTA"
- "CAPTION_STYLE_COLOR_RED"
- "CAPTION_STYLE_COLOR_UNKNOWN"
- "CAPTION_STYLE_COLOR_WHITE"
- "CAPTION_STYLE_COLOR_YELLOW"
- "CAPTION_STYLE_SIZE_EXTRA_LARGE"
- "CAPTION_STYLE_SIZE_LARGE"
- "CAPTION_STYLE_SIZE_MEDIUM"
- "CAPTION_STYLE_SIZE_SMALL"
- "CAPTION_STYLE_SIZE_UNKNOWN"
- "CAPTION_STYLE_TEXT_EDGE_STYLE_DEPRESSED"
- "CAPTION_STYLE_TEXT_EDGE_STYLE_DROP_SHADOW"
- "CAPTION_STYLE_TEXT_EDGE_STYLE_NONE"
- "CAPTION_STYLE_TEXT_EDGE_STYLE_RAISED"
- "CAPTION_STYLE_TEXT_EDGE_STYLE_UNIFORM"
- "CONTACT_CALENDAR_TYPE_GREGORIAN"
- "CONTACT_CALENDAR_TYPE_LUNISOLAR"
- "CONTACT_CALENDAR_TYPE_UNSPECIFIED"
- "CONTENT_TRANSFER_TYPE_FCI_ONLY"
- "CONTENT_TRANSFER_TYPE_FCI_ONLY_OR_INLINE_ONLY"
- "CONTENT_TRANSFER_TYPE_INLINE_ONLY"
- "CONTENT_TRANSFER_TYPE_MIXED"
- "CONTENT_TRANSFER_TYPE_UNSPECIFIED"
- "Client initialization: USB connection check: %s"
- "DATA_CLASS_ACCESSIBILITY_SETTINGS"
- "DATA_CLASS_ACCOUNTS"
- "DATA_CLASS_ALARMS"
- "DATA_CLASS_APPS"
- "DATA_CLASS_APP_DATA"
- "DATA_CLASS_BROWSER_DATA"
- "DATA_CLASS_CALENDAR"
- "DATA_CLASS_CALL_LOGS"
- "DATA_CLASS_CONTACTS"
- "DATA_CLASS_FILES_AND_FOLDERS"
- "DATA_CLASS_HOMESCREEN_LAYOUT"
- "DATA_CLASS_MESSAGES"
- "DATA_CLASS_MUSIC"
- "DATA_CLASS_NOTES"
- "DATA_CLASS_PASSWORDS_AND_PASSKEYS"
- "DATA_CLASS_PHOTOS_AND_VIDEOS"
- "DATA_CLASS_RECORDINGS"
- "DATA_CLASS_UNSPECIFIED"
- "DATA_CLASS_WALLET"
- "DATA_CLASS_WALLPAPERS"
- "DATA_CLASS_WIFI_CREDENTIALS"
- "DCT_ERROR_CAPABILITY_MISMATCH"
- "DCT_ERROR_CONTROL_MESSAGE_EXCHANGE"
- "DCT_ERROR_HIGH_SPEED_MEDIUM_UNAVAILABLE"
- "DCT_ERROR_MDNS_DISCOVERY_TIMEOUT"
- "DCT_ERROR_MDNS_REGISTER_SERVICE"
- "DCT_ERROR_REQUEST_FAILED"
- "DCT_ERROR_RESPONSE_FAILED"
- "DCT_ERROR_SERVICE_CANCELLED"
- "DCT_ERROR_SUBSEQUENT_TLS_SPAKE"
- "DCT_ERROR_UNVERIFIED_INTEGRITY"
- "DCT_ERROR_UPGRADE_HIGH_SPEED_MEDIUM_FAILED"
- "DCT_ERROR_USER_CANCELLED"
- "DCT_ERROR_WIFI_CREDENTIAL_TRANSFER"
- "DCT_ERROR_WIFI_DISABLED"
- "DCT_ERROR_WIFI_DISCONNECTED"
- "DCT_ERROR_WIFI_INTERNET_CONNECTION"
- "EXPORT_FAILURE_STATE_EXPORT_FAILED"
- "EXPORT_FAILURE_STATE_UNSPECIFIED"
- "EXPORT_FAILURE_STATE_UNTRANSFERRABLE"
- "Failed to get default account for service %{public}s; using '%s' as fallback"
- "Forcing USB device mode and configuring NCM"
- "Home screen Layout"
- "INSTALLATION_STATE_IS_ARCHIVED"
- "INSTALLATION_STATE_IS_INSTALLED"
- "INSTALLATION_STATE_IS_PENDING_INSTALL"
- "INSTALLATION_STATE_IS_UNSPECIFIED"
- "IOS_ACCOUNT_TYPE_AOL"
- "IOS_ACCOUNT_TYPE_APPLE"
- "IOS_ACCOUNT_TYPE_CAL_DAV"
- "IOS_ACCOUNT_TYPE_CARD_DAV"
- "IOS_ACCOUNT_TYPE_EXCHANGE"
- "IOS_ACCOUNT_TYPE_GOOGLE"
- "IOS_ACCOUNT_TYPE_HOTMAIL"
- "IOS_ACCOUNT_TYPE_IMAP"
- "IOS_ACCOUNT_TYPE_LDAP"
- "IOS_ACCOUNT_TYPE_NET_EASE126"
- "IOS_ACCOUNT_TYPE_NET_EASE163"
- "IOS_ACCOUNT_TYPE_POP"
- "IOS_ACCOUNT_TYPE_QQ"
- "IOS_ACCOUNT_TYPE_UNSPECIFIED"
- "IOS_ACCOUNT_TYPE_YAHOO"
- "NCM activated successfully as fallback"
- "NCM activation failed or no USB connection - continuing without NCM"
- "NCM is supported; USB connection check: %s"
- "No USB connection detected - skipping NCM setup"
- "PLATFORM_ANDROID"
- "PLATFORM_IOS"
- "PLATFORM_RFU1"
- "PLATFORM_RFU2"
- "PLATFORM_UNKNOWN"
- "PRESET_ANNIVERSARY"
- "PRESET_ASSISTANT"
- "PRESET_AUNT"
- "PRESET_AUNTPARENTS_ELDER_SISTER"
- "PRESET_AUNT_FATHERS_BROTHERS_WIFE"
- "PRESET_AUNT_FATHERS_OLDER_BROTHERS_WIFE"
- "PRESET_AUNT_FATHERS_OLDER_SISTER"
- "PRESET_AUNT_FATHERS_YOUNGER_BROTHERS_WIFE"
- "PRESET_AUNT_FATHERS_YOUNGER_SISTER"
- "PRESET_AUNT_FATHER_SISTER"
- "PRESET_AUNT_MOTHERS_BROTHERS_WIFE"
- "PRESET_AUNT_MOTHERS_OLDER_SISTER"
- "PRESET_AUNT_MOTHERS_SISTER"
- "PRESET_AUNT_MOTHERS_YOUNGER_SISTER"
- "PRESET_AUNT_PARENTS_YOUNGER_SISTER"
- "PRESET_AUNT_PARENT_SISTER"
- "PRESET_BLOG"
- "PRESET_BOYFRIEND"
- "PRESET_BROTHER"
- "PRESET_BROTHERINLAW"
- "PRESET_BROTHERINLAWS_ELDER_BROTHERS_HUSBAND"
- "PRESET_BROTHERINLAWS_HUSBANDS_BROTHER"
- "PRESET_BROTHERINLAWS_HUSBANDS_SISTERS_HUSBAND"
- "PRESET_BROTHERINLAWS_SISTERS_HUSBAND"
- "PRESET_BROTHERINLAWS_SPOUSES_BROTHER"
- "PRESET_BROTHERINLAWS_WIFES_BROTHER"
- "PRESET_BROTHERINLAWS_WIFES_SISTERS_HUSBAND"
- "PRESET_BROTHERINLAWS_YOUNGERS_SISTERS_HUSBAND"
- "PRESET_CALLBACK"
- "PRESET_CAR"
- "PRESET_CHILD"
- "PRESET_CHILDINLAW"
- "PRESET_COBROTHERINLAW"
- "PRESET_COFATHERINLAW"
- "PRESET_COLLEAGUE"
- "PRESET_COMOTHERINLAW"
- "PRESET_COMPANY_MAIN"
- "PRESET_COPARENTINLAW"
- "PRESET_COSIBLINGINLAW"
- "PRESET_COSISTERINLAW"
- "PRESET_COUSIN"
- "PRESET_COUSINFATHERS_BROTHERS_DAUGHTER"
- "PRESET_COUSINFATHERS_BROTHERS_SON"
- "PRESET_COUSINFATHERS_DAUGHTER"
- "PRESET_COUSINFATHERS_SON"
- "PRESET_COUSINGRANDPARENTS_SIBLINGCHILD"
- "PRESET_COUSINGRANDPARENTS_SIBLINGDAUGHTER"
- "PRESET_COUSINGRANDPARENTS_SIBLINGSON"
- "PRESET_COUSINMOTHERS_MOTHERS_DAUGHTER"
- "PRESET_COUSINPARENTS_SIBLINGCHILD"
- "PRESET_COUSINPARENTS_SIBLINGDAUGHTER"
- "PRESET_COUSINPARENTS_SIBLINGTON"
- "PRESET_COUSIN_OR_SIBLINGS_CHILD"
- "PRESET_DAUGHTER"
- "PRESET_DAUGHTERINLAW"
- "PRESET_DAUGHTERINLAW_OR_SISTERINLAW"
- "PRESET_DAUGHTERINLAW_OR_STEP_DAUGHTER"
- "PRESET_DOMESTIC_PARTNER"
- "PRESET_ELDERS_SIBLING"
- "PRESET_ELDERS_SISTER"
- "PRESET_ELDER_BROTHER"
- "PRESET_ELDER_BROTHERINLAW"
- "PRESET_ELDER_COUSIN"
- "PRESET_ELDER_COUSINFATHERS_BROTHERS_DAUGHTER"
- "PRESET_ELDER_COUSINFATHERS_BROTHERS_SON"
- "PRESET_ELDER_COUSINFATHERS_DAUGHTER"
- "PRESET_ELDER_COUSINFATHERS_SON"
- "PRESET_ELDER_COUSINMOTHERS_MOTHERS_DAUGHTER"
- "PRESET_ELDER_COUSINMOTHERS_SIBLINGDAUGHTER_OR_FATHERS_SISTERS_DAUGHTER"
- "PRESET_ELDER_COUSINMOTHERS_SIBLINGTON_OR_FATHERS_SISTERS_SON"
- "PRESET_ELDER_COUSINPARENTS_SIBLINGDAUGHTER"
- "PRESET_ELDER_COUSIN_PARENTS_SIBLINGTON"
- "PRESET_ELDER_SIBLINGINLAW"
- "PRESET_ELDER_SISTERINLAW"
- "PRESET_ELDEST_BROTHER"
- "PRESET_ELDEST_SISTER"
- "PRESET_EMAIL_ICLOUD"
- "PRESET_FATHER"
- "PRESET_FATHERINLAW"
- "PRESET_FATHERINLAW_HUSBANDS_FATHER"
- "PRESET_FATHERINLAW_OR_STEP_FATHER"
- "PRESET_FATHERINLAW_WIFES_FATHER"
- "PRESET_FEMALE_COUSIN"
- "PRESET_FEMALE_FRIEND"
- "PRESET_FEMALE_PARTNER"
- "PRESET_FRIEND"
- "PRESET_FTP"
- "PRESET_GIRLFRIEND"
- "PRESET_GIRLFRIEND_OR_BOYFRIEND"
- "PRESET_GRANDAUNT"
- "PRESET_GRANDCHILD"
- "PRESET_GRANDCHILD_OR_SIBLINGS_CHILD"
- "PRESET_GRANDDAUGHTER"
- "PRESET_GRANDDAUGHTERS_DAUGHTERS_DAUGHTER"
- "PRESET_GRANDDAUGHTER_OR_NIECE"
- "PRESET_GRANDDAUGHTER_SONS_DAUGHTER"
- "PRESET_GRANDFATHER"
- "PRESET_GRANDFATHERS_FATHERS_FATHER"
- "PRESET_GRANDFATHERS_MOTHERS_FATHER"
- "PRESET_GRANDMOTHER"
- "PRESET_GRANDMOTHERS_FATHERS_MOTHER"
- "PRESET_GRANDMOTHERS_MOTHERS_MOTHER"
- "PRESET_GRANDNEPHEW"
- "PRESET_GRANDNEPHEW_BROTHERS_GRANDSON"
- "PRESET_GRANDNEPHEW_SISTERS_GRANDSON"
- "PRESET_GRANDNIECE"
- "PRESET_GRANDNIECE_BROTHERS_GRANDDAUGHTER"
- "PRESET_GRANDNIECE_SISTERS_GRANDDAUGHTER"
- "PRESET_GRANDPARENT"
- "PRESET_GRANDSON"
- "PRESET_GRANDSONS_DAUGHTERS_SON"
- "PRESET_GRANDSONS_SONS_SON"
- "PRESET_GRANDSON_OR_NEPHEW"
- "PRESET_GRANDUNCLE"
- "PRESET_GREATGRANDCHILD"
- "PRESET_GREATGRANDCHILD_OR_SIBLINGS_GRANDCHILD"
- "PRESET_GREATGRANDDAUGHTER"
- "PRESET_GREATGRANDFATHER"
- "PRESET_GREATGRANDMOTHER"
- "PRESET_GREATGRANDPARENT"
- "PRESET_GREATGRANDSON"
- "PRESET_HOME"
- "PRESET_HOMEPAGE"
- "PRESET_HOME_FAX"
- "PRESET_HUSBAND"
- "PRESET_IPHONE"
- "PRESET_ISDN"
- "PRESET_MAIN"
- "PRESET_MALE_COUSIN"
- "PRESET_MALE_FRIEND"
- "PRESET_MALE_PARTNER"
- "PRESET_MANAGER"
- "PRESET_MMS"
- "PRESET_MOBILE"
- "PRESET_MOTHER"
- "PRESET_MOTHERINLAW"
- "PRESET_MOTHERINLAW_HUSBANDS_MOTHER"
- "PRESET_MOTHERINLAW_OR_STEP_MOTHER"
- "PRESET_MOTHERINLAW_WIFES_MOTHER"
- "PRESET_NEPHEW"
- "PRESET_NEPHEW_BROTHERS_SON"
- "PRESET_NEPHEW_BROTHERS_SON_OR_HUSBANDS_SIBLINGS"
- "PRESET_NEPHEW_OR_COUSIN"
- "PRESET_NEPHEW_SISTERS_SON"
- "PRESET_NEPHEW_SISTERS_SON_OR_WIFES_SIBLINGS"
- "PRESET_NIECE"
- "PRESET_NIECE_BROTHERS_DAUGHTER"
- "PRESET_NIECE_BROTHERS_DAUGHTER_OR_HUSBANDS_SIBLINGS_DAUGHTER"
- "PRESET_NIECE_OR_COUSIN"
- "PRESET_NIECE_SISTERS_DAUGHTER"
- "PRESET_NIECE_SISTERS_DAUGHTER_OR_WIFES_SIBLINGS_DAUGHTER"
- "PRESET_OTHER"
- "PRESET_OTHER_FAX"
- "PRESET_PAGER"
- "PRESET_PARENT"
- "PRESET_PARENTINLAW"
- "PRESET_PARENTS_OLDERS_SIBLING"
- "PRESET_PARENTS_SIBLING"
- "PRESET_PARENTS_SIBLING_FATHERS_OLDER_SIBLING"
- "PRESET_PARENTS_SIBLING_FATHERS_SIBLING"
- "PRESET_PARENTS_SIBLING_FATHERS_YOUNGER_SIBLING"
- "PRESET_PARENTS_SIBLING_MOTHERS_OLDER_SIBLING"
- "PRESET_PARENTS_SIBLING_MOTHERS_SIBLING"
- "PRESET_PARENTS_SIBLING_MOTHERS_YOUNGER_SIBLING"
- "PRESET_PARENTS_YOUNGER_SIBLING"
- "PRESET_PARTNER"
- "PRESET_PROFILE"
- "PRESET_RADIO"
- "PRESET_REFERRED_BY"
- "PRESET_RELATIVE"
- "PRESET_SCHOOL"
- "PRESET_SIBLING"
- "PRESET_SIBLINGINLAW"
- "PRESET_SIBLINGSCHILD"
- "PRESET_SISTER"
- "PRESET_SISTERINLAW"
- "PRESET_SISTERINLAWS_HUSBANDS_BROTHERS_WIFE"
- "PRESET_SISTERINLAWS_WIFES_BROTHERS_WIFE"
- "PRESET_SISTERINLAW_BROTHERS_WIFE"
- "PRESET_SISTERINLAW_ELDER_BROTHERS_WIFE"
- "PRESET_SISTERINLAW_HUSBANDS_SISTER"
- "PRESET_SISTERINLAW_SPOUSES_SISTER"
- "PRESET_SISTERINLAW_WIFES_SISTER"
- "PRESET_SISTERINLAW_YOUNGER_BROTHERS_WIFE"
- "PRESET_SON"
- "PRESET_SONINLAW"
- "PRESET_SONINLAW_OR_BROTHERINLAW"
- "PRESET_SONINLAW_OR_STEP_SON"
- "PRESET_SPOUSE"
- "PRESET_STEP_BROTHER"
- "PRESET_STEP_CHILD"
- "PRESET_STEP_DAUGHTER"
- "PRESET_STEP_FATHER"
- "PRESET_STEP_MOTHER"
- "PRESET_STEP_PARENT"
- "PRESET_STEP_SISTER"
- "PRESET_STEP_SON"
- "PRESET_TEACHER"
- "PRESET_TELEX"
- "PRESET_TTY_TDD"
- "PRESET_UNCLE"
- "PRESET_UNCLE_FATHERS_BROTHER"
- "PRESET_UNCLE_FATHERS_OLDERS_SISTERS_HUSBAND"
- "PRESET_UNCLE_FATHERS_OLDER_BROTHER"
- "PRESET_UNCLE_FATHERS_SISTERS_HUSBAND"
- "PRESET_UNCLE_FATHERS_YOUNGER_BROTHER"
- "PRESET_UNCLE_FATHERS_YOUNGER_SISTERS_HUSBAND"
- "PRESET_UNCLE_MOTHERS_BROTHER"
- "PRESET_UNCLE_MOTHERS_OLDER_BROTHER"
- "PRESET_UNCLE_MOTHERS_SISTERS_HUSBAND"
- "PRESET_UNCLE_MOTHERS_YOUNGER_BROTHER"
- "PRESET_UNCLE_PARENTS_BROTHER"
- "PRESET_UNCLE_PARENTS_OLDER_BROTHER"
- "PRESET_UNCLE_PARENTS_YOUNGER_BROTHER"
- "PRESET_UNSPECIFIED"
- "PRESET_WIFE"
- "PRESET_WORK"
- "PRESET_WORK_FAX"
- "PRESET_WORK_MOBILE"
- "PRESET_WORK_PAGER"
- "PRESET_YOUNGERCOUSINMOTHERS_SIBLINGTON_OR_FATHERS_SISTERS_SON"
- "PRESET_YOUNGER_BROTHER"
- "PRESET_YOUNGER_BROTHERINLAW"
- "PRESET_YOUNGER_COUSIN"
- "PRESET_YOUNGER_COUSINFATHERS_BROTHERS_DAUGHTER"
- "PRESET_YOUNGER_COUSINFATHERS_BROTHERS_SON"
- "PRESET_YOUNGER_COUSINFATHERS_DAUGHTER"
- "PRESET_YOUNGER_COUSINFATHERS_SON"
- "PRESET_YOUNGER_COUSINMOTHERS_MOTHERS_DAUGHTER"
- "PRESET_YOUNGER_COUSINMOTHERS_SIBLINGDAUGHTER_OR_FATHERS_SISTERS_DAUGHTER"
- "PRESET_YOUNGER_COUSINPARENTS_SIBLINGDAUGHTER"
- "PRESET_YOUNGER_COUSINPARENTS_SIBLINGTON"
- "PRESET_YOUNGER_SIBLING"
- "PRESET_YOUNGER_SIBLINGINLAW"
- "PRESET_YOUNGER_SISTER"
- "PRESET_YOUNGER_SISTERINLAW"
- "PRESET_YOUNGEST_BROTHER"
- "PRESET_YOUNGEST_SISTER"
- "Passwords & Passkeys"
- "RESOURCE_TYPE_ACCESSIBILITY_SETTINGS"
- "RESOURCE_TYPE_ACCOUNTS"
- "RESOURCE_TYPE_ALARMS"
- "RESOURCE_TYPE_APPS"
- "RESOURCE_TYPE_BROWSER_DATA"
- "RESOURCE_TYPE_CALENDARS"
- "RESOURCE_TYPE_CALENDARS_ATTACHMENTS"
- "RESOURCE_TYPE_CALENDARS_EVENTS"
- "RESOURCE_TYPE_CALL_LOGS"
- "RESOURCE_TYPE_CONTACTS"
- "RESOURCE_TYPE_CONTACTS_PHOTOS"
- "RESOURCE_TYPE_FILES_AND_FOLDERS"
- "RESOURCE_TYPE_FILE_CONTENTS"
- "RESOURCE_TYPE_HOMESCREEN_LAYOUT"
- "RESOURCE_TYPE_MESSAGES"
- "RESOURCE_TYPE_MESSAGES_ATTACHMENTS"
- "RESOURCE_TYPE_MESSAGES_CONVERSATIONS"
- "RESOURCE_TYPE_MESSAGES_PARTICIPANTS"
- "RESOURCE_TYPE_MUSIC_PLAYLISTS"
- "RESOURCE_TYPE_MUSIC_TRACKS"
- "RESOURCE_TYPE_NOTES"
- "RESOURCE_TYPE_PASSWORDS_AND_PASSKEYS"
- "RESOURCE_TYPE_PHOTOS_AND_VIDEOS"
- "RESOURCE_TYPE_RECORDINGS"
- "RESOURCE_TYPE_UNSPECIFIED"
- "RESOURCE_TYPE_WALLET_CARDS"
- "RESOURCE_TYPE_WALLPAPERS"
- "RESOURCE_TYPE_WIFI_CREDENTIALS"
- "RESULT_FAILURE"
- "RESULT_PARTIAL"
- "RESULT_SUCCESS"
- "RESULT_UNSPECIFIED"
- "SESSION_SUCCESS"
- "SNOOZE_CAPABILITY_ALLOWED"
- "SNOOZE_CAPABILITY_DISALLOWED"
- "SNOOZE_CAPABILITY_UNSPECIFIED"
- "Server initialization: USB connection check: %s"
- "Starting NCM bringUp in parallel with device info exchange"
- "TRANSFER_STATE_CANCELLED_CRITICAL_BATTERY"
- "TRANSFER_STATE_CANCELLED_DEVICE_REBOOT"
- "TRANSFER_STATE_CANCELLED_NOT_ENOUGH_SPACE"
- "TRANSFER_STATE_COMPLETED_DATA_TRANSFER"
- "TRANSFER_STATE_CONFIGURING_DATA_TRANSFER"
- "TRANSFER_STATE_FAILURE"
- "TRANSFER_STATE_TRANSFERRING"
- "TRANSFER_STATE_TRANSFER_SUMMARY"
- "TRANSFER_STATE_UNSPECIFIED"
- "UNKNOWN_DISCONNECTION_REASON"
- "WALLET_CARD_TYPE_ACCESS_KEY"
- "WALLET_CARD_TYPE_BOARDING_PASS"
- "WALLET_CARD_TYPE_COUPON"
- "WALLET_CARD_TYPE_EVENT_TICKET"
- "WALLET_CARD_TYPE_GENERIC"
- "WALLET_CARD_TYPE_GENERIC_TICKET"
- "WALLET_CARD_TYPE_GIFT"
- "WALLET_CARD_TYPE_IDENTITY_DOCUMENT"
- "WALLET_CARD_TYPE_PAYMENT"
- "WALLET_CARD_TYPE_TRANSIT"
- "WALLET_CARD_TYPE_UNSPECIFIED"
- "WIFI_PRIVATE_MAC_ADDRESS_TYPE_SYSTEM_SELECTED_FIXED"
- "WIFI_PRIVATE_MAC_ADDRESS_TYPE_SYSTEM_SELECTED_OFF"
- "WIFI_PRIVATE_MAC_ADDRESS_TYPE_SYSTEM_SELECTED_ROTATING"
- "WIFI_PRIVATE_MAC_ADDRESS_TYPE_UNSPECIFIED"
- "WIFI_PRIVATE_MAC_ADDRESS_TYPE_USER_SELECTED_FIXED"
- "WIFI_PRIVATE_MAC_ADDRESS_TYPE_USER_SELECTED_OFF"
- "WIFI_PRIVATE_MAC_ADDRESS_TYPE_USER_SELECTED_ROTATING"
- "WIFI_SECURITY_TYPE_OPEN"
- "WIFI_SECURITY_TYPE_OWE"
- "WIFI_SECURITY_TYPE_PSK"
- "WIFI_SECURITY_TYPE_SAE"
- "WIFI_SECURITY_TYPE_UNSPECIFIED"
- "WIFI_SECURITY_TYPE_WAPI_PSK"
- "WIFI_SECURITY_TYPE_WEP"
- "Wireless failed - attempting NCM as fallback"
- "_isSelf"
- "absolute_epoch_millis"
- "account_name"
- "account_number_suffix"
- "account_type"
- "address1"
- "address2"
- "address3"
- "addresses"
- "agreement"
- "alarm_id"
- "alarm_state"
- "album_artists"
- "albums"
- "all_day"
- "android_app"
- "ap_frequency"
- "app"
- "app_content_export_options"
- "app_content_exports"
- "app_data_results"
- "app_datas"
- "app_id"
- "app_identifier"
- "app_list"
- "apple_integrity"
- "assertion"
- "audio_balance"
- "audio_description_enabled"
- "auto_rotate_screen_enabled"
- "background_color"
- "background_color_video_override"
- "background_opacity"
- "background_opacity_video_override"
- "billing_address"
- "birthday_date"
- "bitrate"
- "bold_text"
- "bottom_bar_items"
- "bssid"
- "bundle_id"
- "burst_id"
- "calendarType"
- "calendar_data"
- "calendar_id"
- "call_account_id"
- "calls"
- "caption_style_name"
- "caption_styles"
- "cardholder_name"
- "challenge"
- "client_id"
- "color_video_override"
- "column_index"
- "company"
- "company_name"
- "component_version"
- "composer"
- "contact_id"
- "contact_type"
- "content_identifier"
- "content_transfer_type"
- "content_version"
- "copyright"
- "creation_epoch_millis"
- "creation_time_epoch_millis"
- "credential_in_secure_element"
- "current_progress"
- "custom_type"
- "data_class"
- "data_class_results"
- "data_set"
- "date_created_millis"
- "date_epoch_millis"
- "date_modified_millis"
- "day_of_the_week"
- "days_of_the_month"
- "days_of_the_week"
- "days_of_the_year"
- "default_browser_app_id"
- "department"
- "deuteranomaly_filter"
- "developer_identity"
- "device_brand"
- "device_info"
- "device_info_request"
- "device_info_response"
- "device_information"
- "device_os_version"
- "device_platform"
- "disc_count"
- "disc_number"
- "disconnect_reason"
- "disconnection_request"
- "disconnection_response"
- "distributor_type"
- "dr_swap_support"
- "duration_millis"
- "email"
- "emails"
- "end_epoch_millis"
- "estimated_item_count"
- "estimated_size"
- "estimated_size_in_bytes"
- "event_availability"
- "event_data"
- "event_id"
- "events"
- "eviction_time_epoch_millis"
- "export_failure"
- "export_failure_summary"
- "failed to fetch self"
- "failed_items_count"
- "failure_message"
- "failure_messages"
- "failure_state"
- "file_name"
- "file_path"
- "file_size"
- "first_day_of_the_week"
- "first_name"
- "flash_for_alerts_enabled"
- "folder_name"
- "font_name"
- "font_size"
- "free_storage_bytes"
- "genre"
- "grayscale_filter"
- "host_app"
- "immutable"
- "infra_sta"
- "init(conversation:participants:message:defaultAccount:)"
- "install_state"
- "installer"
- "integrity_attestation"
- "integrity_attestation_ack"
- "integrity_start_request"
- "integrity_start_response"
- "integrity_token"
- "ios_app"
- "is_compilation"
- "is_deleted"
- "is_directory"
- "is_edited"
- "is_explicit"
- "is_favorite"
- "is_hidden"
- "is_homescreen"
- "is_local"
- "is_lockscreen"
- "is_tdls_supported"
- "job_title"
- "key_attestation"
- "last_modified_epoch_millis"
- "last_name"
- "latitude"
- "layout_items"
- "live_caption_enabled"
- "live_transcribe_enabled"
- "localized_name"
- "lohs"
- "lohs_sta"
- "longitude"
- "maiden_name"
- "manufacturer"
- "media_type"
- "medium_closure_request"
- "medium_closure_response"
- "middle_name"
- "modified_epoch_millis"
- "modified_time_epoch_millis"
- "mono_audio_enabled"
- "months_of_the_year"
- "multi_layer"
- "multi_layer_mix"
- "music_album"
- "music_track_ids"
- "name_prefix"
- "name_suffix"
- "ncm_device_support"
- "ncm_host_support"
- "networks"
- "new_state"
- "num_items_failed"
- "num_items_transferred"
- "num_items_untransferable"
- "num_of_columns"
- "num_of_rows"
- "occurrence_count"
- "occurrence_epoch_millis"
- "organization"
- "other_date"
- "other_dates"
- "package_name"
- "package_version"
- "participant_role"
- "participant_status"
- "participant_type"
- "payload_json_cxf"
- "payment_details"
- "phone_number"
- "phonetic_first_name"
- "phonetic_last_name"
- "phonetic_middle_name"
- "phonetic_name"
- "pkpass_path"
- "play_integrity"
- "postal_code"
- "power_button_ends_call_enabled"
- "pre_detected_untransferable_item_count"
- "prefer_captions_sdh"
- "preset_type"
- "private_mac_address_type"
- "profile"
- "protanomaly_filter"
- "recorded_on_watch"
- "recurrence_end"
- "recurrence_frequency"
- "recurrence_rule"
- "recurrence_rule_id"
- "related_contacts"
- "relative_file_path"
- "relative_offset"
- "relative_path"
- "release_date_epoch_millis"
- "repeated_days"
- "requires_r4_security_features"
- "resource_results"
- "resources"
- "result"
- "row_index"
- "screen_reader_enabled"
- "screen_timeout"
- "security_type"
- "serialized_data"
- "session_id"
- "set_positions"
- "short_bundle_version"
- "short_localized_name"
- "size_transferred_bytes"
- "snooze_capability"
- "social_medias"
- "source_app"
- "source_developer_identity"
- "source_device_export_capabilities"
- "source_device_info"
- "source_id"
- "source_state_change"
- "speak_selection"
- "start_epoch_millis"
- "store_id"
- "subscribed"
- "subtype"
- "supported_destinations"
- "supported_frequency"
- "supported_options"
- "target_device_import_capabilities"
- "target_device_info"
- "target_platform_identifiers"
- "target_state_change"
- "telephone_numbers"
- "text_color"
- "text_edge_style"
- "text_edge_style_video_override"
- "text_highlight_color"
- "text_highlight_opacity"
- "text_highlight_video_override"
- "text_opacity"
- "text_opacity_video_override"
- "text_scale"
- "time_remaining_seconds"
- "time_zone"
- "track_artists"
- "track_count"
- "track_number"
- "transfer_progress"
- "transfer_summary"
- "tritanomaly_filter"
- "tty_type"
- "untransferrable_items_count"
- "urls"
- "usb"
- "user_selected_data_classes"
- "user_selected_default_apps"
- "user_selection_summary"
- "v1"
- "vibration_type"
- "visible_bitmap_croppings"
- "voice_control_enabled"
- "was_supervised_kids_account"
- "week_number"
- "weeks_number"
- "widget"
- "widget_identifier"
- "widget_kind"
- "wifi_aware"
- "wifi_aware_publisher"
- "wifi_aware_subscriber"
- "wifi_credential_request"
- "wifi_credential_response"
- "wifi_direct"
- "wifi_direct_client"
- "wifi_direct_group_owner"
- "wifi_direct_legacy"
- "wifi_direct_r2"
- "will create a participant. address=%s, is_self=%{bool}d, sequence_id=%lld, service=%s"
- "wireless_medium_negotiation_request"
- "wireless_medium_negotiation_response"
- "wireless_medium_negotiation_reverse_direction_support"
- "wpa3_supported"

```
