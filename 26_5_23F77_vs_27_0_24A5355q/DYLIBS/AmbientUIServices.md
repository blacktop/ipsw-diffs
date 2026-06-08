## AmbientUIServices

> `/System/Library/PrivateFrameworks/AmbientUIServices.framework/AmbientUIServices`

```diff

-81.4.1.0.0
-  __TEXT.__text: 0x914
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_methlist: 0x2ac
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0xb6
-  __TEXT.__unwind_info: 0xa0
-  __TEXT.__objc_classname: 0x124
-  __TEXT.__objc_methname: 0x480
-  __TEXT.__objc_methtype: 0xfb
-  __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x50
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+101.0.100.0.0
+  __TEXT.__text: 0x6a08
+  __TEXT.__objc_methlist: 0x618
+  __TEXT.__const: 0x2a8
+  __TEXT.__cstring: 0x1b8
+  __TEXT.__swift5_typeref: 0x262
+  __TEXT.__swift5_capture: 0x144
+  __TEXT.__constg_swiftt: 0x1c4
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_cont: 0x8
+  __TEXT.__swift5_reflstr: 0x3a
+  __TEXT.__swift5_fieldmd: 0xa0
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__eh_frame: 0x1b8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a0
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0x388
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb0
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x638
+  __DATA_CONST.__got: 0x108
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__objc_const: 0x1518
+  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH.__objc_data: 0x4d0
+  __AUTH.__data: 0xd0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x180
+  __DATA.__data: 0x340
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E67816BC-CC76-37B9-9D84-F84054203BBC
-  Functions: 27
-  Symbols:   179
-  CStrings:  114
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 95CA0CB6-8884-367B-B14E-7A15A0B9FC01
+  Functions: 234
+  Symbols:   551
+  CStrings:  30
 
Symbols:
+ +[AMUIAmbientInteractionEventAction actionWithEventType:userInfo:]
+ +[AMUIAmbientInteractionEventAction longPressActionWithLocation:phase:]
+ +[AMUIAmbientInteractionEventAction swipeActionWithLocation:phase:]
+ +[AMUIAmbientPosterSceneUnlockRequestAction actionWithReason:unlockDestination:]
+ -[AMUIAmbientInteractionEventAction description]
+ -[AMUIAmbientInteractionEventAction eventType]
+ -[AMUIAmbientInteractionEventAction userInfo]
+ -[AMUIAmbientPosterSceneUnlockRequestAction reason]
+ -[AMUIAmbientPosterSceneUnlockRequestAction unlockDestination]
+ _AMUIAmbientInteractionEventLocationKey
+ _AMUIAmbientInteractionEventPhaseKey
+ _NSStringFromAMUIAmbientInteractionEventType
+ _OBJC_CLASS_$_AMUIAmbientInteractionEventAction
+ _OBJC_CLASS_$_AMUIAmbientPosterSceneUnlockRequestAction
+ _OBJC_CLASS_$_BSAction
+ _OBJC_CLASS_$_BSActionResponder
+ _OBJC_CLASS_$_BSActionResponse
+ _OBJC_CLASS_$_BSDescriptionBuilder
+ _OBJC_CLASS_$_BSMutableSettings
+ _OBJC_CLASS_$_FBScene
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$__TtC17AmbientUIServices27AmbientPosterSceneExtension
+ _OBJC_CLASS_$__TtC17AmbientUIServices31AmbientPosterSceneHostComponent
+ _OBJC_CLASS_$__TtC17AmbientUIServices33AmbientPosterSceneClientComponent
+ _OBJC_CLASS_$__TtC17AmbientUIServices39AmbientPosterSceneHostSettingsExtension
+ _OBJC_CLASS_$__TtC17AmbientUIServices41AmbientPosterSceneClientSettingsExtension
+ _OBJC_METACLASS_$_AMUIAmbientInteractionEventAction
+ _OBJC_METACLASS_$_AMUIAmbientPosterSceneUnlockRequestAction
+ _OBJC_METACLASS_$_BSAction
+ _OBJC_METACLASS_$__TtC17AmbientUIServices27AmbientPosterSceneExtension
+ _OBJC_METACLASS_$__TtC17AmbientUIServices31AmbientPosterSceneHostComponent
+ _OBJC_METACLASS_$__TtC17AmbientUIServices33AmbientPosterSceneClientComponent
+ _OBJC_METACLASS_$__TtC17AmbientUIServices39AmbientPosterSceneHostSettingsExtension
+ _OBJC_METACLASS_$__TtC17AmbientUIServices41AmbientPosterSceneClientSettingsExtension
+ _SUIDisplayStyleFromAMUIAmbientDisplayStyle
+ __Block_copy
+ __Block_release
+ __CATEGORY_FBScene_$_AmbientUIServices
+ __CATEGORY_INSTANCE_METHODS_FBScene_$_AmbientUIServices
+ __CLASS_METHODS__TtC17AmbientUIServices27AmbientPosterSceneExtension
+ __CLASS_METHODS__TtC17AmbientUIServices39AmbientPosterSceneHostSettingsExtension
+ __CLASS_METHODS__TtC17AmbientUIServices41AmbientPosterSceneClientSettingsExtension
+ __DATA__TtC17AmbientUIServices27AmbientPosterSceneExtension
+ __DATA__TtC17AmbientUIServices31AmbientPosterSceneHostComponent
+ __DATA__TtC17AmbientUIServices33AmbientPosterSceneClientComponent
+ __DATA__TtC17AmbientUIServices39AmbientPosterSceneHostSettingsExtension
+ __DATA__TtC17AmbientUIServices41AmbientPosterSceneClientSettingsExtension
+ __INSTANCE_METHODS__TtC17AmbientUIServices27AmbientPosterSceneExtension
+ __INSTANCE_METHODS__TtC17AmbientUIServices39AmbientPosterSceneHostSettingsExtension
+ __INSTANCE_METHODS__TtC17AmbientUIServices41AmbientPosterSceneClientSettingsExtension
+ __IVARS__TtC17AmbientUIServices31AmbientPosterSceneHostComponent
+ __IVARS__TtC17AmbientUIServices33AmbientPosterSceneClientComponent
+ __METACLASS_DATA__TtC17AmbientUIServices27AmbientPosterSceneExtension
+ __METACLASS_DATA__TtC17AmbientUIServices31AmbientPosterSceneHostComponent
+ __METACLASS_DATA__TtC17AmbientUIServices33AmbientPosterSceneClientComponent
+ __METACLASS_DATA__TtC17AmbientUIServices39AmbientPosterSceneHostSettingsExtension
+ __METACLASS_DATA__TtC17AmbientUIServices41AmbientPosterSceneClientSettingsExtension
+ __OBJC_$_CLASS_METHODS_AMUIAmbientInteractionEventAction
+ __OBJC_$_CLASS_METHODS_AMUIAmbientPosterSceneUnlockRequestAction
+ __OBJC_$_INSTANCE_METHODS_AMUIAmbientInteractionEventAction
+ __OBJC_$_INSTANCE_METHODS_AMUIAmbientPosterSceneUnlockRequestAction
+ __OBJC_$_INSTANCE_METHODS__TtC17AmbientUIServices31AmbientPosterSceneHostComponent(AmbientUIServices)
+ __OBJC_$_INSTANCE_METHODS__TtC17AmbientUIServices33AmbientPosterSceneClientComponent(AmbientUIServices)
+ __OBJC_$_PROP_LIST_AMUIAmbientInteractionEventAction
+ __OBJC_$_PROP_LIST_AMUIAmbientPosterSceneUnlockRequestAction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMUIAmbientPosterSceneDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSSceneObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AMUIAmbientPosterSceneDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSSceneObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneObserver
+ __OBJC_$_PROTOCOL_REFS_AMUIAmbientPosterSceneDelegate
+ __OBJC_$_PROTOCOL_REFS_FBSSceneObserver
+ __OBJC_$_PROTOCOL_REFS_FBSceneObserver
+ __OBJC_CLASS_PROTOCOLS_$__TtC17AmbientUIServices31AmbientPosterSceneHostComponent(AmbientUIServices)
+ __OBJC_CLASS_PROTOCOLS_$__TtC17AmbientUIServices33AmbientPosterSceneClientComponent(AmbientUIServices)
+ __OBJC_CLASS_RO_$_AMUIAmbientInteractionEventAction
+ __OBJC_CLASS_RO_$_AMUIAmbientPosterSceneUnlockRequestAction
+ __OBJC_LABEL_PROTOCOL_$_AMUIAmbientPosterSceneDelegate
+ __OBJC_LABEL_PROTOCOL_$_FBSSceneObserver
+ __OBJC_LABEL_PROTOCOL_$_FBSceneObserver
+ __OBJC_METACLASS_RO_$_AMUIAmbientInteractionEventAction
+ __OBJC_METACLASS_RO_$_AMUIAmbientPosterSceneUnlockRequestAction
+ __OBJC_PROTOCOL_$_AMUIAmbientPosterSceneDelegate
+ __OBJC_PROTOCOL_$_FBSSceneObserver
+ __OBJC_PROTOCOL_$_FBSceneObserver
+ __PROTOCOL_INSTANCE_METHODS__TtP17AmbientUIServices26AmbientPosterSceneSettings_
+ __PROTOCOL_INSTANCE_METHODS__TtP17AmbientUIServices32AmbientPosterSceneClientSettings_
+ __PROTOCOL_METHOD_TYPES__TtP17AmbientUIServices26AmbientPosterSceneSettings_
+ __PROTOCOL_METHOD_TYPES__TtP17AmbientUIServices32AmbientPosterSceneClientSettings_
+ __PROTOCOL_PROPERTIES__TtP17AmbientUIServices26AmbientPosterSceneSettings_
+ __PROTOCOL_PROPERTIES__TtP17AmbientUIServices32AmbientPosterSceneClientSettings_
+ __PROTOCOL__TtP17AmbientUIServices26AmbientPosterSceneSettings_
+ __PROTOCOL__TtP17AmbientUIServices32AmbientPosterSceneClientSettings_
+ ___chkstk_darwin
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.19
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.22
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.3
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.7
+ ___swift_closure_destructor.8
+ ___swift_closure_destructorTm
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_reflection_version
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_AmbientUIServices
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_AmbientUIServices
+ _block_copy_helper
+ _block_copy_helper.10
+ _block_copy_helper.7
+ _block_descriptor
+ _block_descriptor.12
+ _block_descriptor.9
+ _block_destroy_helper
+ _block_destroy_helper.11
+ _block_destroy_helper.8
+ _bzero
+ _flat unique So30AMUIAmbientPosterSceneDelegate_p
+ _free
+ _memmove
+ _objc_alloc
+ _objc_allocWithZone
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$actionWithEventType:userInfo:
+ _objc_msgSend$ambientPosterSceneDidBeginConfiguring
+ _objc_msgSend$ambientPosterSceneDidEndConfiguring
+ _objc_msgSend$ambientPosterSceneDidRequestUnlock:completion:
+ _objc_msgSend$appendObject:withName:
+ _objc_msgSend$build
+ _objc_msgSend$builderWithObject:
+ _objc_msgSend$clientScene
+ _objc_msgSend$clientSettings
+ _objc_msgSend$componentForExtension:ofClass:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$eventType
+ _objc_msgSend$flagForSetting:
+ _objc_msgSend$hostScene
+ _objc_msgSend$info
+ _objc_msgSend$init
+ _objc_msgSend$initWithInfo:responder:
+ _objc_msgSend$isAuthenticated
+ _objc_msgSend$isConfiguring
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectForSetting:
+ _objc_msgSend$responderWithHandler:
+ _objc_msgSend$responseWithInfo:
+ _objc_msgSend$sendPrivateActions:
+ _objc_msgSend$sendResponse:
+ _objc_msgSend$setFlag:forSetting:
+ _objc_msgSend$setIsAuthenticated:
+ _objc_msgSend$setIsConfiguring:
+ _objc_msgSend$setObject:forSetting:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$updateClientSettings:
+ _objc_msgSend$updateSettingsWithBlock:
+ _objc_msgSend$userInfo
+ _objc_msgSend$valueWithCGPoint:
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_coroFrameAlloc
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastClass
+ _swift_dynamicCastObjCClass
+ _swift_dynamicCastObjCProtocolConditional
+ _swift_endAccess
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isEscapingClosureAtFileLocation
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_release
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x1
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x23
+ _swift_setDeallocating
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic $s17AmbientUIServices0A19PosterSceneSettingsP
+ _symbolic $s17AmbientUIServices0A25PosterSceneClientSettingsP
+ _symbolic Sb
+ _symbolic SbIeghy_
+ _symbolic SbIegy_
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic So17FBSSceneComponentC
+ _symbolic So17FBSSceneExtensionC
+ _symbolic So20FBSSettingsExtensionC
+ _symbolic So23FBSMutableSceneSettingsCIgg_
+ _symbolic So29FBSMutableSceneClientSettingsCSo25FBSSceneTransitionContextCIggg_
+ _symbolic So41AMUIAmbientPosterSceneUnlockRequestActionC
+ _symbolic _____ 17AmbientUIServices0A20PosterSceneExtensionC
+ _symbolic _____ 17AmbientUIServices0A24PosterSceneHostComponentC
+ _symbolic _____ 17AmbientUIServices0A26PosterSceneClientComponentC
+ _symbolic _____ 17AmbientUIServices0A32PosterSceneHostSettingsExtensionC
+ _symbolic _____ 17AmbientUIServices0A34PosterSceneClientSettingsExtensionC
+ _symbolic _____ So31AMUIAmbientInteractionEventTypeV
+ _symbolic _____3key_yp5valuet s11AnyHashableV
+ _symbolic _____SDySSypGSgIegyg_ So31AMUIAmbientInteractionEventTypeV
+ _symbolic _____SDySSypGSgytIegnnr_ So31AMUIAmbientInteractionEventTypeV
+ _symbolic ______pSgXw So30AMUIAmbientPosterSceneDelegateP
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySo8BSActionCG s11_SetStorageC
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic _____yyXlXpG s23_ContiguousArrayStorageC
+ _symbolic yXlXp
+ _symbolic y______SDySSypGSgtcSg So31AMUIAmbientInteractionEventTypeV
+ _symbolic ytIeAgHr_
CStrings:
+ "AMUIAmbientInteractionEventLocationKey"
+ "AMUIAmbientInteractionEventPhaseKey"
+ "AmbientUIServices/AmbientPosterSceneHostComponent.swift"
+ "AmbientUIServices/FBScene+AmbientPosterSceneExtension.swift"
+ "longPress"
+ "none"
+ "swipe"
+ "type"
+ "userInfo"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AMUIAmbientDisplayStyleTrait"
- "AMUIAmbientPresentationSceneClientComponent"
- "AMUIAmbientPresentationSceneExtension"
- "AMUIAmbientPresentationSettings"
- "AMUIAmbientPresentationSettingsExtension"
- "AMUIAmbientPresentationStateTrait"
- "AmbientPresentation"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,N"
- "T@\"NSString\",R,C"
- "TB,?,R,N"
- "TB,N,GisAmbientPresented"
- "TB,N,GisAmbientPresented,V_ambientPresented"
- "TB,R,N,GisAmbientPresented"
- "TQ,R"
- "Tq,N"
- "Tq,N,V_ambientDisplayStyle"
- "Tq,R,N"
- "UINSIntegerTraitDefinition"
- "UITraitDefinition"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_ambientDisplayStyle"
- "_ambientDisplayStyleForScene:"
- "_ambientPresented"
- "_isAmbientPresentedForScene:"
- "_sceneWillConnect:"
- "_updateAmbientTraitsForWindowScene:"
- "addObserver:selector:name:object:"
- "affectsColorAppearance"
- "ambientDisplayStyle"
- "ambientPresented"
- "arrayWithObjects:count:"
- "autorelease"
- "class"
- "clientComponents"
- "conformsToProtocol:"
- "connectedScenes"
- "containsProperty:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultValue"
- "description"
- "enumerateObjectsUsingBlock:"
- "hash"
- "identifier"
- "isAmbientPresented"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "name"
- "object"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "protocol"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "release"
- "removeObserver:name:object:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scene:didUpdateSettings:"
- "self"
- "setAmbientDisplayStyle:"
- "setAmbientPresented:"
- "setNSIntegerValue:forTrait:"
- "setScene:"
- "settings"
- "settingsDiff"
- "settingsExtensions"
- "sharedApplication"
- "superclass"
- "traitOverrides"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "valueForNSIntegerTrait:"
- "zone"

```
