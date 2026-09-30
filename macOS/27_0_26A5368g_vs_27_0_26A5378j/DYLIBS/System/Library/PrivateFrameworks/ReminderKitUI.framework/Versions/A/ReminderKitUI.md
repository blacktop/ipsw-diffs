## ReminderKitUI

> `/System/Library/PrivateFrameworks/ReminderKitUI.framework/Versions/A/ReminderKitUI`

```diff

-  __TEXT.__text: 0x52fc
-  __TEXT.__objc_methlist: 0x690
-  __TEXT.__const: 0x252
-  __TEXT.__cstring: 0x1c4
-  __TEXT.__oslogstring: 0x174
-  __TEXT.__swift5_typeref: 0xca
-  __TEXT.__constg_swiftt: 0x1ec
-  __TEXT.__swift5_reflstr: 0x72
-  __TEXT.__swift5_fieldmd: 0xc0
-  __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_types: 0xc
+  __TEXT.__text: 0xcdbc
+  __TEXT.__objc_methlist: 0x7c0
+  __TEXT.__const: 0x8ec
+  __TEXT.__cstring: 0x342
+  __TEXT.__oslogstring: 0x207
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__swift5_typeref: 0x38d
+  __TEXT.__constg_swiftt: 0x400
+  __TEXT.__swift5_reflstr: 0x332
+  __TEXT.__swift5_fieldmd: 0x354
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_proto: 0x5c
+  __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x230
+  __TEXT.__swift5_capture: 0x54
+  __TEXT.__swift5_assocty: 0x68
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__eh_frame: 0x148
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x78
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b8
-  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0x530
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0xe0
-  __AUTH_CONST.__const: 0x2d8
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x898
-  __AUTH_CONST.__auth_got: 0x1a0
-  __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x408
-  __DATA.__bss: 0x100
+  __DATA_CONST.__got: 0x1a0
+  __AUTH_CONST.__const: 0x8d1
+  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__objc_const: 0xc30
+  __AUTH_CONST.__auth_got: 0x4a8
+  __AUTH.__objc_data: 0x110
+  __AUTH.__data: 0x138
+  __DATA.__objc_ivar: 0x50
+  __DATA.__data: 0x5b8
+  __DATA.__bss: 0xa10
+  __DATA_DIRTY.__objc_data: 0x238
+  __DATA_DIRTY.__data: 0x1b8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
   - /System/Library/Frameworks/_LocationEssentials.framework/Versions/A/_LocationEssentials
   - /System/Library/PrivateFrameworks/ReminderKit.framework/Versions/A/ReminderKit
   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 246
-  Symbols:   441
-  CStrings:  40
+  Functions: 493
+  Symbols:   635
+  CStrings:  52
 
Sections:
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
Symbols:
+ +[REMRemindersShareSheetServiceLookup embedShareSheetInHostViewController:publicViewController:reminderStorages:changedKeys:destinationPreference:specificListID:configurationData:completion:]
+ -[REMReminderCreationRemoteViewController setShareSheetPublicViewController:]
+ -[REMReminderCreationRemoteViewController shareSheetPublicViewController]
+ -[REMReminderCreationRemoteViewController shareSheetViewServiceViewController]
+ -[REMReminderCreationRemoteViewController viewServiceDidCommitWithReminderIDs:]
+ GCC_except_table0
+ OBJC_IVAR_$_REMReminderCreationRemoteViewController._shareSheetPublicViewController
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_REMList
+ _OBJC_CLASS_$_REMReminderChangeItem
+ _OBJC_CLASS_$_REMRemindersShareSheetServiceLookup
+ _OBJC_CLASS_$_REMSaveRequest
+ _OBJC_CLASS_$__TtC13ReminderKitUI36REMRemindersShareSheetViewController
+ _OBJC_CLASS_$__TtCV13ReminderKitUI19RemindersShareSheet11Coordinator
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$_REMRemindersShareSheetServiceLookup
+ _OBJC_METACLASS_$__TtC13ReminderKitUI36REMRemindersShareSheetViewController
+ _OBJC_METACLASS_$__TtCV13ReminderKitUI19RemindersShareSheet11Coordinator
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __191+[REMRemindersShareSheetServiceLookup embedShareSheetInHostViewController:publicViewController:reminderStorages:changedKeys:destinationPreference:specificListID:configurationData:completion:]_block_invoke
+ __Block_copy
+ __Block_object_assign
+ __Block_release
+ __DATA__TtC13ReminderKitUI36REMRemindersShareSheetViewController
+ __DATA__TtC13ReminderKitUIP33_3CC6A07B062BDB4E67ED93B4E9DD37C630_REMRemindersShareSheetSession
+ __DATA__TtCV13ReminderKitUI19RemindersShareSheet11Coordinator
+ __INSTANCE_METHODS__TtCV13ReminderKitUI19RemindersShareSheet11Coordinator
+ __IVARS__TtC13ReminderKitUI36REMRemindersShareSheetViewController
+ __IVARS__TtC13ReminderKitUIP33_3CC6A07B062BDB4E67ED93B4E9DD37C630_REMRemindersShareSheetSession
+ __IVARS__TtCV13ReminderKitUI19RemindersShareSheet11Coordinator
+ __METACLASS_DATA__TtC13ReminderKitUI36REMRemindersShareSheetViewController
+ __METACLASS_DATA__TtC13ReminderKitUIP33_3CC6A07B062BDB4E67ED93B4E9DD37C630_REMRemindersShareSheetSession
+ __METACLASS_DATA__TtCV13ReminderKitUI19RemindersShareSheet11Coordinator
+ __OBJC_$_CLASS_METHODS_REMRemindersShareSheetServiceLookup
+ __OBJC_$_INSTANCE_METHODS__TtC13ReminderKitUI36REMRemindersShareSheetViewController(ReminderKitUI)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_REMRemindersShareSheetPublicViewController
+ __OBJC_$_PROTOCOL_METHOD_TYPES_REMRemindersShareSheetPublicViewController
+ __OBJC_CLASS_PROTOCOLS_$__TtC13ReminderKitUI36REMRemindersShareSheetViewController(ReminderKitUI)
+ __OBJC_CLASS_RO_$_REMRemindersShareSheetServiceLookup
+ __OBJC_LABEL_PROTOCOL_$_REMRemindersShareSheetPublicViewController
+ __OBJC_METACLASS_RO_$_REMRemindersShareSheetServiceLookup
+ __OBJC_PROTOCOL_$_REMRemindersShareSheetPublicViewController
+ __Unwind_Resume
+ ___191+[REMRemindersShareSheetServiceLookup embedShareSheetInHostViewController:publicViewController:reminderStorages:changedKeys:destinationPreference:specificListID:configurationData:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e30_v32?0"NSError"8{CGSize=dd}16l
+ ___block_descriptor_96_e8_32s40s48s56s64bs72w80w_e44_v24?0"NSRemoteViewController"8"NSError"16l
+ ___chkstk_darwin
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32s40s48s56s64b72w80w
+ ___destroy_helper_block_e8_32s40s48s56s64s72w80w
+ ___objc_personality_v0
+ ___swift__destructor
+ ___swift_closure_destructor
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_memcpy16_8
+ ___swift_memcpy48_8
+ ___swift_memcpy8_8
+ ___swift_memcpy9_8
+ ___swift_project_boxed_opaque_existential_1
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_ReminderKitUI
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_ReminderKitUI
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_ReminderKitUI
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_ReminderKitUI
+ __swift_closure_destructor
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 13ReminderKitUI19RemindersShareSheetV05SwiftC029NSViewControllerRepresentableAaD4View
+ _associated conformance 13ReminderKitUI19RemindersShareSheetV05SwiftC04ViewAA4BodyAdEP_AdE
+ _associated conformance 13ReminderKitUI27REMRemindersShareSheetErrorOSHAASQ
+ _associated conformance 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV0I11LayoutStyleOSHAASQ
+ _associated conformance 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV10CodingKeysOSHAASQ
+ _associated conformance 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV10CodingKeysOs0U3KeyAAs23CustomStringConvertible
+ _associated conformance 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV10CodingKeysOs0U3KeyAAs28CustomDebugStringConvertible
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _bzero
+ _keypath_get_selector_preferredContentSize
+ _memmove
+ _objc_allocWithZone
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$addReminderWithTitle:toListChangeItem:
+ _objc_msgSend$changedKeys
+ _objc_msgSend$dismissViewController:
+ _objc_msgSend$displayShareSheetWithReminderStorages:changedKeys:destinationPreference:specificListID:configurationData:completion:
+ _objc_msgSend$embedShareSheetInHostViewController:publicViewController:reminderStorages:changedKeys:destinationPreference:specificListID:configurationData:completion:
+ _objc_msgSend$fetchDefaultListWithError:
+ _objc_msgSend$init
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithNibName:bundle:
+ _objc_msgSend$initWithStore:
+ _objc_msgSend$objectID
+ _objc_msgSend$preferredContentSize
+ _objc_msgSend$presentingViewController
+ _objc_msgSend$rem_combinedViewServicesRemoteViewControllerInterface
+ _objc_msgSend$rem_combinedViewServicesServiceViewControllerInterface
+ _objc_msgSend$setShareSheetPublicViewController:
+ _objc_msgSend$shareSheetPublicViewController
+ _objc_msgSend$shareSheetViewServiceViewController
+ _objc_msgSend$storage
+ _objc_msgSend$updateList:
+ _objc_msgSend$viewServiceDidCommitWithReminderIDs:
+ _swift_allocError
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getForeignTypeMetadata
+ _swift_getKeyPath
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic $s7SwiftUI29NSViewControllerRepresentableP
+ _symbolic $s7SwiftUI4ViewP
+ _symbolic $sSY
+ _symbolic SDySo11REMObjectIDCShySSGG
+ _symbolic SS
+ _symbolic SaySo11REMObjectIDCG11reminderIDs_t
+ _symbolic SaySo18REMReminderStorageCG
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say______pG 13ReminderKitUI25REMReminderShareSheetItemP
+ _symbolic Say______pG______pScMYcc 13ReminderKitUI25REMReminderShareSheetItemP AA0deF7SessionP
+ _symbolic Sb
+ _symbolic ShySSG
+ _symbolic Si
+ _symbolic So11REMObjectIDCSg
+ _symbolic So14REMSaveRequestC
+ _symbolic So16NSViewControllerC
+ _symbolic So17REMListChangeItemC
+ _symbolic So8NSObjectC
+ _symbolic So8REMStoreC
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 12CoreGraphics7CGFloatV
+ _symbolic _____ 13ReminderKitUI19RemindersShareSheetV
+ _symbolic _____ 13ReminderKitUI19RemindersShareSheetV11CoordinatorC
+ _symbolic _____ 13ReminderKitUI27REMRemindersShareSheetErrorO
+ _symbolic _____ 13ReminderKitUI30_REMRemindersShareSheetSession33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLC
+ _symbolic _____ 13ReminderKitUI36REMRemindersShareSheetViewControllerC
+ _symbolic _____ 13ReminderKitUI36REMRemindersShareSheetViewControllerC11WirePayload33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV
+ _symbolic _____ 13ReminderKitUI36REMRemindersShareSheetViewControllerC15PopulateOutcome33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLO
+ _symbolic _____ 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV
+ _symbolic _____ 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV0I11LayoutStyleO
+ _symbolic _____ 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV10CodingKeysO
+ _symbolic _____ 13ReminderKitUI36REMRemindersShareSheetViewControllerC6ResultO
+ _symbolic _____ So43REMRemindersShareSheetDestinationPreferenceV
+ _symbolic _____ So6CGSizeV
+ _symbolic _____ s5NeverO
+ _symbolic _____Sg 10Foundation21NSKeyValueObservationC
+ _symbolic _____Sg 13ReminderKitUI36REMRemindersShareSheetViewControllerC11WirePayload33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV
+ _symbolic _____Sg So6CGSizeV
+ _symbolic _____SgXw 13ReminderKitUI19RemindersShareSheetV11CoordinatorC
+ _symbolic _____SgXw 13ReminderKitUI36REMRemindersShareSheetViewControllerC
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSg s5ErrorP
+ _symbolic _____ySo11REMObjectIDCShySSGG s18_DictionaryStorageC
+ _symbolic _____y_____G 7SwiftUI36NSViewControllerRepresentableContextV 011ReminderKitB019RemindersShareSheetV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13ReminderKitUI36REMRemindersShareSheetViewControllerC17WireConfiguration33_3CC6A07B062BDB4E67ED93B4E9DD37C6LLV10CodingKeysO
+ _symbolic _____y_____SgG 7SwiftUI9LazyStateV So6CGSizeV
+ _symbolic _____y_____Sg_G 7SwiftUI9LazyStateV7StorageO So6CGSizeV
+ _symbolic _____y_____Sg_G_yXlSgt 7SwiftUI9LazyStateV7StorageO So6CGSizeV
+ _symbolic y_____ScMYcc 13ReminderKitUI36REMRemindersShareSheetViewControllerC6ResultO
+ _symbolic y_____cSg So6CGSizeV
+ block_copy_helper
+ block_descriptor
+ block_destroy_helper
- _objc_msgSend$rem_reminderCreationRemoteViewControllerExportedInterface
CStrings:
+ "Fatal error"
+ "NSRemoteViewController returned wrong-class instance"
+ "REMRemindersShareSheetServiceLookup: failed to obtain remote VC: %{public}@"
+ "REMRemindersShareSheetServiceLookup: requesting NSRemoteViewController"
+ "REMRemindersShareSheetViewController does not support NSCoding"
+ "ReminderKitUI.REMRemindersShareSheetViewController"
+ "ReminderKitUI/REMRemindersShareSheetViewController.swift"
+ "com.apple.remindersKitUI.remindersShareSheet"
+ "editingAndSelection"
+ "init(nibName:bundle:)"
+ "selectionOnly"

```
