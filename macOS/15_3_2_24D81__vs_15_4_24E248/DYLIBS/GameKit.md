## GameKit

> `/System/iOSSupport/System/Library/Frameworks/GameKit.framework/Versions/A/GameKit`

```diff

-819.3.6.0.0
-  __TEXT.__text: 0x68
-  __TEXT.__auth_stubs: 0x30
-  __TEXT.__const: 0x3e
-  __TEXT.__unwind_info: 0x58
-  __TEXT.__objc_methname: 0x1a
-  __DATA_CONST.__const: 0x118
+819.4.46.0.0
+  __TEXT.__text: 0x361b4
+  __TEXT.__auth_stubs: 0x15b0
+  __TEXT.__objc_methlist: 0x69c
+  __TEXT.__const: 0x594
+  __TEXT.__cstring: 0xf66
+  __TEXT.__swift5_typeref: 0x8ab
+  __TEXT.__swift5_capture: 0x378
+  __TEXT.__oslogstring: 0x2ec
+  __TEXT.__constg_swiftt: 0x1ec
+  __TEXT.__swift5_fieldmd: 0x11c
+  __TEXT.__swift5_reflstr: 0xd6
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift_as_entry: 0xd8
+  __TEXT.__swift_as_ret: 0x10c
+  __TEXT.__unwind_info: 0xe00
+  __TEXT.__eh_frame: 0x271c
+  __TEXT.__objc_classname: 0x69
+  __TEXT.__objc_methname: 0x10a4
+  __TEXT.__objc_methtype: 0x93
+  __TEXT.__objc_stubs: 0x3a0
+  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x18
+  __DATA_CONST.__objc_selrefs: 0x4d0
+  __AUTH_CONST.__auth_got: 0xae0
+  __AUTH_CONST.__const: 0xb28
+  __AUTH_CONST.__cfstring: 0x60
+  __AUTH_CONST.__objc_const: 0xe78
+  __AUTH.__objc_data: 0x580
+  __AUTH.__data: 0xf0
+  __DATA.__data: 0x858
+  __DATA.__bss: 0xa68
+  __DATA.__common: 0x80
+  - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
+  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/ModelIO.framework/Versions/A/ModelIO
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices
   - /System/Library/PrivateFrameworks/GameCenterFoundation.framework/Versions/A/GameCenterFoundation
   - /System/Library/PrivateFrameworks/GameCenterUICore.framework/Versions/A/GameCenterUICore
+  - /System/Library/PrivateFrameworks/GameServices.framework/Versions/A/GameServices
+  - /System/Library/PrivateFrameworks/GameServicesCore.framework/Versions/A/GameServicesCore
   - /System/iOSSupport/System/Library/Frameworks/GameController.framework/Versions/A/GameController
   - /System/iOSSupport/System/Library/Frameworks/GameplayKit.framework/Versions/A/GameplayKit
   - /System/iOSSupport/System/Library/Frameworks/ReplayKit.framework/Versions/A/ReplayKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7F133067-CBA7-3F4E-BF98-12EB8B175E5F
-  Functions: 1
-  Symbols:   76
-  CStrings:  2
+  UUID: E5D19ABC-6AF1-37A4-AC0D-CD73B58D0302
+  Functions: 881
+  Symbols:   565
+  CStrings:  337
 
Symbols:
+ +[GKAchievementSPI filledWithIdentifier:player:percentComplete:lastReportedDate:]
+ +[GKAchievementSPI loadAchievementWithId:forGame:playerIDs:withCompletionHandler:]
+ +[GKChallengeDefinition(State) loadChallengeDefinitionsWithCompletionHandler:]
+ +[GKDaemonInvoker invokeWithData:completionHandler:]
+ +[GKGameActivityDefinition(State) loadGameActivityDefinitionsWithCompletionHandler:]
+ +[GKGameActivityDefinition(State) loadGameActivityDefinitionsWithIDs:completionHandler:]
+ +[GKGameSPI currentGame]
+ +[GKImageLoader getImageURLForURLTemplate:size:]
+ +[GKImageLoader getImageURLForURLTemplate:size:scale:]
+ +[GKImageLoader loadImageForURL:queue:withCompletionHandler:]
+ +[GKLocalPlayerSPI playerID]
+ +[GKPlayerSPI loadPlayersForIdentifiersPrivate:withCompletionHandler:]
+ +[GKPlayerSPI playerFromPlayerID:]
+ -[GKChallengeDefinition(State) hasActiveChallengesWithCompletionHandler:]
+ -[GKLocalPlayer(GameActivity) gameHasProcessedGameActivity:]
+ -[GKLocalPlayer(GameActivity) playerWantsToPlayGameActivity:completion:]
+ _GKErrorDomain
+ _OBJC_CLASS_$_AMSMediaArtwork
+ _OBJC_CLASS_$_GKAchievement
+ _OBJC_CLASS_$_GKAchievementDescription
+ _OBJC_CLASS_$_GKAchievementSPI
+ _OBJC_CLASS_$_GKChallengeDefinition
+ _OBJC_CLASS_$_GKDaemonInvoker
+ _OBJC_CLASS_$_GKDaemonProxy
+ _OBJC_CLASS_$_GKGame
+ _OBJC_CLASS_$_GKGameActivity
+ _OBJC_CLASS_$_GKGameActivityDefinition
+ _OBJC_CLASS_$_GKGameSPI
+ _OBJC_CLASS_$_GKImageLoader
+ _OBJC_CLASS_$_GKLeaderboard
+ _OBJC_CLASS_$_GKLeaderboardScore
+ _OBJC_CLASS_$_GKLocalPlayer
+ _OBJC_CLASS_$_GKLocalPlayerSPI
+ _OBJC_CLASS_$_GKMatch
+ _OBJC_CLASS_$_GKMatchRequest
+ _OBJC_CLASS_$_GKMatchmaker
+ _OBJC_CLASS_$_GKPlayer
+ _OBJC_CLASS_$_GKPlayerSPI
+ _OBJC_CLASS_$_GKScreenConfigurationController
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$__TtC7GameKit21GSGameActivitySupport
+ _OBJC_CLASS_$__TtC7GameKit28GKChallengeDefinitionSupport
+ _OBJC_CLASS_$__TtC7GameKit31GKGameActivityDefinitionSupport
+ _OBJC_METACLASS_$_GKAchievementSPI
+ _OBJC_METACLASS_$_GKChallengeDefinition
+ _OBJC_METACLASS_$_GKDaemonInvoker
+ _OBJC_METACLASS_$_GKGameActivity
+ _OBJC_METACLASS_$_GKGameActivityDefinition
+ _OBJC_METACLASS_$_GKGameSPI
+ _OBJC_METACLASS_$_GKImageLoader
+ _OBJC_METACLASS_$_GKLocalPlayerSPI
+ _OBJC_METACLASS_$_GKPlayerSPI
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$__TtC7GameKit21GSGameActivitySupport
+ _OBJC_METACLASS_$__TtC7GameKit28GKChallengeDefinitionSupport
+ _OBJC_METACLASS_$__TtC7GameKit31GKGameActivityDefinitionSupport
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_GKGameActivity
+ __CLASS_METHODS__TtC7GameKit21GSGameActivitySupport
+ __CLASS_METHODS__TtC7GameKit28GKChallengeDefinitionSupport
+ __CLASS_METHODS__TtC7GameKit31GKGameActivityDefinitionSupport
+ __CLASS_PROPERTIES__TtC7GameKit21GSGameActivitySupport
+ __CLASS_PROPERTIES__TtC7GameKit28GKChallengeDefinitionSupport
+ __CLASS_PROPERTIES__TtC7GameKit31GKGameActivityDefinitionSupport
+ __DATA_GKChallengeDefinition
+ __DATA_GKGameActivity
+ __DATA_GKGameActivityDefinition
+ __DATA__TtC7GameKit21GSGameActivitySupport
+ __DATA__TtC7GameKit28GKChallengeDefinitionSupport
+ __DATA__TtC7GameKit31GKGameActivityDefinitionSupport
+ __INSTANCE_METHODS_GKGameActivity
+ __INSTANCE_METHODS_GKGameActivityDefinition
+ __INSTANCE_METHODS__TtC7GameKit21GSGameActivitySupport
+ __INSTANCE_METHODS__TtC7GameKit28GKChallengeDefinitionSupport
+ __INSTANCE_METHODS__TtC7GameKit31GKGameActivityDefinitionSupport
+ __IVARS_GKChallengeDefinition
+ __IVARS_GKGameActivity
+ __IVARS_GKGameActivityDefinition
+ __IVARS__TtC7GameKit21GSGameActivitySupport
+ __IVARS__TtC7GameKit28GKChallengeDefinitionSupport
+ __IVARS__TtC7GameKit31GKGameActivityDefinitionSupport
+ __METACLASS_DATA_GKChallengeDefinition
+ __METACLASS_DATA_GKGameActivity
+ __METACLASS_DATA_GKGameActivityDefinition
+ __METACLASS_DATA__TtC7GameKit21GSGameActivitySupport
+ __METACLASS_DATA__TtC7GameKit28GKChallengeDefinitionSupport
+ __METACLASS_DATA__TtC7GameKit31GKGameActivityDefinitionSupport
+ __NSConcreteStackBlock
+ __OBJC_$_CATEGORY_GKLocalPlayer_$_GameActivity
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GKLocalPlayer_$_GameActivity
+ __OBJC_$_CLASS_METHODS_GKAchievementSPI
+ __OBJC_$_CLASS_METHODS_GKChallengeDefinition(State)
+ __OBJC_$_CLASS_METHODS_GKDaemonInvoker
+ __OBJC_$_CLASS_METHODS_GKGameActivityDefinition(State)
+ __OBJC_$_CLASS_METHODS_GKGameSPI
+ __OBJC_$_CLASS_METHODS_GKImageLoader
+ __OBJC_$_CLASS_METHODS_GKLocalPlayerSPI
+ __OBJC_$_CLASS_METHODS_GKPlayerSPI
+ __OBJC_$_CLASS_PROP_LIST_GKLocalPlayerSPI
+ __OBJC_$_INSTANCE_METHODS_GKChallengeDefinition(State)
+ __OBJC_CLASS_RO_$_GKAchievementSPI
+ __OBJC_CLASS_RO_$_GKDaemonInvoker
+ __OBJC_CLASS_RO_$_GKGameSPI
+ __OBJC_CLASS_RO_$_GKImageLoader
+ __OBJC_CLASS_RO_$_GKLocalPlayerSPI
+ __OBJC_CLASS_RO_$_GKPlayerSPI
+ __OBJC_METACLASS_RO_$_GKAchievementSPI
+ __OBJC_METACLASS_RO_$_GKDaemonInvoker
+ __OBJC_METACLASS_RO_$_GKGameSPI
+ __OBJC_METACLASS_RO_$_GKImageLoader
+ __OBJC_METACLASS_RO_$_GKLocalPlayerSPI
+ __OBJC_METACLASS_RO_$_GKPlayerSPI
+ __PROPERTIES_GKChallengeDefinition
+ __PROPERTIES_GKGameActivity
+ __PROPERTIES_GKGameActivityDefinition
+ ___72-[GKLocalPlayer(GameActivity) playerWantsToPlayGameActivity:completion:]_block_invoke
+ ___72-[GKLocalPlayer(GameActivity) playerWantsToPlayGameActivity:completion:]_block_invoke_2
+ ___82+[GKAchievementSPI loadAchievementWithId:forGame:playerIDs:withCompletionHandler:]_block_invoke
+ ___CFConstantStringClassReference
+ ___block_descriptor_40_e8_32b_e36_v24?0"GKGameActivity"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32o40b_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o40o48b_e29_v24?0"NSArray"8"NSError"16ls48l8s32l8s40l8
+ ___chkstk_darwin
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_allocate_value_buffer
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy9_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_boxed_opaque_existential_1Tm
+ ___swift_project_value_buffer
+ __dispatch_main_q
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_GameKit
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_GameKit
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance SC11GKErrorCodeLeV10Foundation13CustomNSErrorSCs5Error
+ _associated conformance SC11GKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC11GKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_AC06_ErrorB8Protocol
+ _associated conformance SC11GKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_SY
+ _associated conformance SC11GKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomF0
+ _associated conformance SC11GKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC26_ObjectiveCBridgeableError
+ _associated conformance SC11GKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC11GKErrorCodeLeV10Foundation26_ObjectiveCBridgeableErrorSCs0F0
+ _associated conformance SC11GKErrorCodeLeVSHSCSQ
+ _associated conformance So11GKErrorCodeV10Foundation06_ErrorB8ProtocolSC01_D4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So11GKErrorCodeV10Foundation06_ErrorB8ProtocolSCSQ
+ _associated conformance So21GKChallengeDefinitionC7GameKitE12AttemptLimitOSHACSQ
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _bzero
+ _dispatch_async
+ _free
+ _malloc
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_alloc
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_gkImageURLForSize:scale:
+ _objc_msgSend$_gkloadRemoteImageForURL:queue:withCompletionHandler:
+ _objc_msgSend$baseProxy
+ _objc_msgSend$createFromGameActivityInstance:completionHandler:
+ _objc_msgSend$currentGame
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$gameServicesRemoteCall:completionHandler:
+ _objc_msgSend$getImageURLForURLTemplate:size:scale:
+ _objc_msgSend$greatestScreenScale
+ _objc_msgSend$hasActiveChallengesWithDefinitionID:completionHandler:
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithIdentifier:player:percentComplete:lastReportedDate:
+ _objc_msgSend$internal
+ _objc_msgSend$loadAchievementWithID:forGame:players:complete:
+ _objc_msgSend$loadChallengeDefinitionsWithCompletionHandler:
+ _objc_msgSend$loadGameActivityDefinitionsWith:completionHandler:
+ _objc_msgSend$loadGameActivityDefinitionsWithCompletionHandler:
+ _objc_msgSend$loadPlayersForIdentifiers:withCompletionHandler:
+ _objc_msgSend$loadPlayersForIdentifiersPrivate:withCompletionHandler:
+ _objc_msgSend$local
+ _objc_msgSend$markAsProcessed
+ _objc_msgSend$playerFormPlayerID:
+ _objc_msgSend$playerID
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$proxyForLocalPlayer
+ _objc_msgSend$shared
+ _objc_msgSend$sharedController
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_release
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x10
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x8
+ _objc_retain_x9
+ _objectdestroyTm
+ _os_log_type_enabled
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unexpectedError
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_willThrow
+ _symbolic $s10Foundation18_ErrorCodeProtocolP
+ _symbolic $s10Foundation21_BridgedStoredNSErrorP
+ _symbolic $sSY
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic SNySiG
+ _symbolic SS_ypt
+ _symbolic SSyYbc
+ _symbolic SX_p
+ _symbolic SX_pSg
+ _symbolic SaySo13GKAchievementCG
+ _symbolic SaySo13GKLeaderboardCG
+ _symbolic SaySo18GKLeaderboardScoreCG
+ _symbolic SaySo24GKAchievementDescriptionCG
+ _symbolic SaySo24GKAchievementDescriptionCGSg______pSgIeggg_ s5ErrorP
+ _symbolic SaySo8GKPlayerCG
+ _symbolic Say_____G 12GameServices0A24ActivityDefinitionFilterO
+ _symbolic Say_____G 12GameServices25ChallengeDefinitionFilterO
+ _symbolic SayypG
+ _symbolic SbIeyBy_
+ _symbolic SbSo7NSErrorCSgIeyByy_
+ _symbolic ScA_pSg
+ _symbolic ScCySaySo13GKAchievementCG______pG s5ErrorP
+ _symbolic ScCySaySo13GKLeaderboardCG______pG s5ErrorP
+ _symbolic ScCySaySo24GKAchievementDescriptionCG______pG s5ErrorP
+ _symbolic ScCySaySo8GKPlayerCG______pG s5ErrorP
+ _symbolic ScCySo7GKMatchC______pG s5ErrorP
+ _symbolic ScCy___________pG 10Foundation4DataV s5ErrorP
+ _symbolic ScCyyt______pG s5ErrorP
+ _symbolic ScPSg
+ _symbolic Si
+ _symbolic Si5count_t
+ _symbolic So13GKLeaderboardCSgSSYaYbKc
+ _symbolic So14GKGameActivityC
+ _symbolic So14GKGameActivityCSgSo7NSErrorCSgIeyByy_
+ _symbolic So14GKGameActivityCSgXw
+ _symbolic So14GKGameActivityCXMo
+ _symbolic So21GKChallengeDefinitionC
+ _symbolic So24GKGameActivityDefinitionC
+ _symbolic So7GKMatchCSgSo7NSErrorCSgIeyByy_
+ _symbolic So7NSArrayC
+ _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
+ _symbolic So7NSErrorC
+ _symbolic So7UIImageCSgSo7NSErrorCSgIeyByy_
+ _symbolic So7UIImageCSg______pSgIeggg_ s5ErrorP
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic So8NSStringC
+ _symbolic _____ 12GameServices0A21ActivityUpdateContextO
+ _symbolic _____ 7GameKit0aB13ServiceClientO
+ _symbolic _____ 7GameKit10AsyncUtilsO
+ _symbolic _____ 7GameKit10ErrorUtilsO
+ _symbolic _____ 7GameKit18GKGameActivitySPIsO
+ _symbolic _____ 7GameKit21GSGameActivitySupportC
+ _symbolic _____ 7GameKit28GKChallengeDefinitionSupportC
+ _symbolic _____ 7GameKit28GKGameActivityDefinitionSPIsO
+ _symbolic _____ 7GameKit31GKGameActivityDefinitionSupportC
+ _symbolic _____ SC11GKErrorCodeLeV
+ _symbolic _____ So11GKErrorCodeV
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ So21GKChallengeDefinitionC7GameKitE12AttemptLimitO
+ _symbolic _____ s6UInt32V
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 10Foundation8CalendarV
+ _symbolic _____Sg 10Foundation8TimeZoneV
+ _symbolic _____Sg 12GameServices0A16ActivityInstanceV
+ _symbolic _____Sg 12GameServices0A18ActivityDefinitionV
+ _symbolic _____Sg 12GameServices0A18ActivityStaticStatO
+ _symbolic _____Sg 12GameServices0A24ActivityConsumptionStateO
+ _symbolic _____Sg 12GameServices0A24ActivityParticipantStateO
+ _symbolic _____Sg 12GameServices19ChallengeDefinitionV
+ _symbolic _____Sg 12GameServices6CursorV
+ _symbolic _____Sg 12GameServices7ArtworkV
+ _symbolic _____SgSg 12GameServices0A18ActivityDefinitionV
+ _symbolic ______p 12GameServices0A18KitServiceProtocolP
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSg s5ErrorP
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____yShySo13GKAchievementCG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____yShySo18GKLeaderboardScoreCG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____ySiG s16PartialRangeFromV
+ _symbolic _____ySiG s23_ContiguousArrayStorageC
+ _symbolic _____ySo13GKAchievementCG s11_SetStorageC
+ _symbolic _____ySo18GKLeaderboardScoreCG s11_SetStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation14DateComponentsV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12GameServices0D14ActivityFilterO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12GameServices0D16ActivityInstanceV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12GameServices0D18ActivityDefinitionV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12GameServices0D19ActivityRuntimeStatO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12GameServices0D24ActivityDefinitionFilterO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12GameServices15ChallengeFilterO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12GameServices19ChallengeDefinitionV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12GameServices25ChallengeDefinitionFilterO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So21GKChallengeDefinitionC7GameKitE12AttemptLimitO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 12GameServices0C16ActivityInstanceV So16os_unfair_lock_sV
+ _symbolic _____y______pG 12GameServices3RefV AA0A0P
+ _symbolic _____y______pG 12GameServices3RefV AA0A14ActivityEntityP
+ _symbolic _____y______pG 12GameServices3RefV AA0A24ActivityDefinitionEntityP
+ _symbolic _____y______pG 12GameServices3RefV AA11AchievementP
+ _symbolic _____y______pG 12GameServices3RefV AA11ImageEntityP
+ _symbolic _____y______pG 12GameServices3RefV AA11LeaderboardP
+ _symbolic _____y______pG 12GameServices3RefV AA25ChallengeDefinitionEntityP
+ _symbolic _____y______pG 12GameServices3RefV AA28AchievementDescriptionEntityP
+ _symbolic _____y______pG 12GameServices3RefV AA6PlayerP
+ _symbolic _____y______pG3key______5valuet 12GameServices3RefV AA6PlayerP AA0A24ActivityParticipantStateO
+ _symbolic _____y______pGSg 12GameServices3RefV AA6PlayerP
+ _symbolic _____y______pG______t 12GameServices3RefV AA6PlayerP AA0A24ActivityParticipantStateO
+ _symbolic _____y______yyt_____GSo17OS_dispatch_queueCG 7Combine10PublishersO8ThrottleV AA18PassthroughSubjectC s5NeverO
+ _symbolic _____y_____y______pGG 12GameServices17PaginatedSequenceV AA3RefV AA0A14ActivityEntityP
+ _symbolic _____y_____y______pGG 12GameServices17PaginatedSequenceV AA3RefV AA0A24ActivityDefinitionEntityP
+ _symbolic _____y_____y______pGG 12GameServices17PaginatedSequenceV AA3RefV AA25ChallengeDefinitionEntityP
+ _symbolic _____y_____y______pGG 12GameServices4PageV AA3RefV AA9ChallengeP
+ _symbolic _____y_____y______pGG s11_SetStorageC 12GameServices3RefV AC6PlayerP
+ _symbolic _____y_____y______pGG s23_ContiguousArrayStorageC 12GameServices3RefV AC0D24ActivityDefinitionEntityP
+ _symbolic _____y_____y______pGG s23_ContiguousArrayStorageC 12GameServices3RefV AC6PlayerP
+ _symbolic _____y_____y______pG_____G s18_DictionaryStorageC 12GameServices3RefV AC6PlayerP AC0C24ActivityParticipantStateO
+ _symbolic _____y_____y______pG______tG s23_ContiguousArrayStorageC 12GameServices3RefV AC6PlayerP AC0D24ActivityParticipantStateO
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _symbolic _____yyt_____G 7Combine18PassthroughSubjectC s5NeverO
+ _symbolic yXl
+ _symbolic ytIeAgHr_
+ block_copy_helper.1
+ block_copy_helper.104
+ block_copy_helper.15
+ block_copy_helper.161
+ block_copy_helper.165
+ block_copy_helper.184
+ block_copy_helper.19
+ block_copy_helper.22
+ block_copy_helper.63
+ block_copy_helper.73
+ block_copy_helper.85
+ block_descriptor.106
+ block_descriptor.163
+ block_descriptor.167
+ block_descriptor.17
+ block_descriptor.186
+ block_descriptor.21
+ block_descriptor.24
+ block_descriptor.3
+ block_descriptor.65
+ block_descriptor.75
+ block_descriptor.87
+ block_destroy_helper.105
+ block_destroy_helper.16
+ block_destroy_helper.162
+ block_destroy_helper.166
+ block_destroy_helper.185
+ block_destroy_helper.2
+ block_destroy_helper.20
+ block_destroy_helper.23
+ block_destroy_helper.64
+ block_destroy_helper.74
+ block_destroy_helper.86
+ objectdestroy.116Tm
+ objectdestroy.18Tm
+ objectdestroy.27Tm
+ objectdestroy.51Tm
+ objectdestroy.55Tm
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_GameKit
CStrings:
+ " failed when resolving services: "
+ ".cxx_destruct"
+ "@116@0:8@16@24@32@40B48@52@60@68@76@84q92@100@108"
+ "@16@0:8"
+ "@188@0:8@16@24@32Q40@48@56@64@72@80d88@96@104@112B120@124@132@140@148@156@164@172^@180"
+ "@24@0:8@16"
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "@32@0:8@16q24"
+ "@40@0:8@16@24^@32"
+ "@40@0:8@16q24d32"
+ "@48@0:8@16@24d32@40"
+ "@76@0:8@16@24@32B40@44@52@60^@68"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "B16@0:8"
+ "B24@0:8@16"
+ "Cannot cast loaded activities to [GKGameActivity]."
+ "Duplicate values for key: '"
+ "Failed to end game activity: last resume date is nil."
+ "Failed to initialize GKGameActivity: "
+ "Failed to initialize GKGameActivity: %@"
+ "Failed to pause game activity: last resume date is nil."
+ "Failed to refresh challenge definitions: %@"
+ "Failed to report achievements on activity end, due to error: %s"
+ "Failed to report score on activity end for leaderboard %s, due to error: %s"
+ "Fatal error"
+ "GKAchievementSPI"
+ "GKChallengeDefinition"
+ "GKDaemonInvoker"
+ "GKGameActivity"
+ "GKGameActivityDefinition"
+ "GKGameActivityDelivered"
+ "GKGameSPI"
+ "GKImageLoader"
+ "GKLocalPlayerSPI"
+ "GKPlayerSPI"
+ "GameActivity"
+ "GameKit.GKChallengeDefinitionSupport"
+ "GameKit.GKGameActivityDefinitionSupport"
+ "GameKit.GSGameActivitySupport"
+ "GameKit/GKGameActivity.swift"
+ "GameKit/GameServices+GameKit.swift"
+ "GameKit_Private.GKChallengeDefinition"
+ "GameKit_Private.GKGameActivity"
+ "GameKit_Private.GKGameActivityDefinition"
+ "Invalid game activity definition."
+ "Invalid party code provided."
+ "Invalid progress complete value provided."
+ "Invalid referral found for game activity."
+ "Main bundle has a nil identifier"
+ "Party code is not supported for this activity."
+ "Q16@0:8"
+ "State"
+ "Swift/Dictionary.swift"
+ "Swift/NativeDictionary.swift"
+ "T@\"<OS_dispatch_source_timer>\",N,&,VgsTimer"
+ "T@\"GKAchievementDescription\",N,R,VreferralAchievement"
+ "T@\"GKGameActivityDefinition\",N,R,VactivityDefinition"
+ "T@\"GKLeaderboard\",N,R,Vleaderboard"
+ "T@\"GKLeaderboard\",N,R,VreferralLeaderboard"
+ "T@\"GKPlayer\",N,R,Vcreator"
+ "T@\"NSArray\",N,C"
+ "T@\"NSArray\",N,R"
+ "T@\"NSDate\",N,&,VlastUpdateTime"
+ "T@\"NSDate\",N,R"
+ "T@\"NSDictionary\",N,C"
+ "T@\"NSDictionary\",N,R"
+ "T@\"NSNumber\",N,&,V__maxPlayers"
+ "T@\"NSNumber\",N,&,V__minPlayers"
+ "T@\"NSSet\",N,R"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R,C"
+ "T@\"NSURL\",N,R"
+ "T@\"NSURL\",N,R,V_fallbackURL"
+ "T@\"NSURL\",N,R,VimageURL"
+ "T@\"NSURL\",N,R,VimageUrl"
+ "T@\"_TtC7GameKit21GSGameActivitySupport\",N,R"
+ "T@\"_TtC7GameKit21GSGameActivitySupport\",N,R,Vsupport"
+ "T@\"_TtC7GameKit28GKChallengeDefinitionSupport\",N,R"
+ "T@\"_TtC7GameKit31GKGameActivityDefinitionSupport\",N,R"
+ "TB,N,R"
+ "TB,N,R,VinitiatedByApple"
+ "TB,N,R,VsupportsPartyCode"
+ "TQ,N,R"
+ "Td,N,R"
+ "Throwing converted error: %@ as: %@"
+ "Tq,N,R,VplayStyle"
+ "URLWithString:"
+ "Unknown referral found for game activity."
+ "_TtC7GameKit21GSGameActivitySupport"
+ "_TtC7GameKit28GKChallengeDefinitionSupport"
+ "_TtC7GameKit31GKGameActivityDefinitionSupport"
+ "__attemptLimitOptions"
+ "__maxPlayers"
+ "__minPlayers"
+ "_achievements"
+ "_createCheckedThrowingContinuation(_:)"
+ "_fallbackURL"
+ "_gkImageURLForSize:scale:"
+ "_gkloadRemoteImageForURL:queue:withCompletionHandler:"
+ "_instanceSnapshot"
+ "_leaderboardScores"
+ "_removeScoresFromLeaderboard:"
+ "_setScoreOnLeaderboard:to:with:for:"
+ "achievements"
+ "activity"
+ "activityDefinition"
+ "associatedAchievementDescriptionIDs"
+ "associatedLeaderboardIDs"
+ "attemptLimitOptions"
+ "baseLeaderboardID"
+ "baseProxy"
+ "bundleIdentifier"
+ "checkPendingGameActivityExistenceWithCompletionHandler:"
+ "com.apple.GameKit"
+ "consumptionState"
+ "context"
+ "createFromGameActivityInstance:completionHandler:"
+ "creationDate"
+ "creator"
+ "currentGame"
+ "d16@0:8"
+ "dealloc"
+ "defaultCenter"
+ "defaultProperties"
+ "details"
+ "dictionaryWithObjects:forKeys:count:"
+ "distantPast"
+ "duration"
+ "durationOptions"
+ "end"
+ "endDate"
+ "fallbackURL"
+ "filledWithIdentifier:player:percentComplete:lastReportedDate:"
+ "findMatchForRequest:withCompletionHandler:"
+ "findMatchWithCompletionHandler:"
+ "findPlayersForHostedMatchWithCompletionHandler:"
+ "findPlayersForHostedRequest:withCompletionHandler:"
+ "gameHasProcessedGameActivity:"
+ "gameServicesRemoteCall:completionHandler:"
+ "getImageURLForURLTemplate:size:"
+ "getImageURLForURLTemplate:size:scale:"
+ "getProgressOnAchievement:"
+ "getScoreOnLeaderboard:"
+ "greatestScreenScale"
+ "groupIdentifier"
+ "gsTimer"
+ "hasActiveChallengesWithCompletionHandler:"
+ "hasActiveChallengesWithDefinitionID:completionHandler:"
+ "identifier"
+ "imageURL"
+ "imageUrl"
+ "init"
+ "init()"
+ "initWithActivityDefinition:partyCode:creator:initiatedByApple:referralLeaderboard:referralAchievement:support:error:"
+ "initWithDefinition:"
+ "initWithIdentifier:activityDefinition:properties:state:partyCode:creationDate:startDate:lastResumeDate:endDate:duration:achievements:leaderboardScores:creator:initiatedByApple:referralLeaderboard:referralAchievement:participants:participantStates:shortGroupID:consumptionState:support:error:"
+ "initWithIdentifier:groupIdentifier:title:details:attemptLimitOptions:durationOptions:leaderboard:imageUrl:"
+ "initWithIdentifier:groupIdentifier:title:details:supportPartyCode:fallbackURL:maxPlayers:minPlayers:defaultProperties:imageURL:playStyle:associatedLeaderboardIDs:associatedAchievementDescriptionIDs:"
+ "initWithIdentifier:player:percentComplete:lastReportedDate:"
+ "initWithInteger:"
+ "initiatedByApple"
+ "integerValue"
+ "internal"
+ "internalPlayerID"
+ "invokeWithData:completionHandler:"
+ "isCompleted"
+ "isValidPartyCode:"
+ "lastReportedDate"
+ "lastResumeDate"
+ "lastUpdateTime"
+ "leaderboard"
+ "leaderboardID"
+ "leaderboardLoader"
+ "leaderboardScores"
+ "loadAchievementDescriptionsWithCompletionHandler:"
+ "loadAchievementWithID:forGame:players:complete:"
+ "loadAchievementWithId:forGame:playerIDs:withCompletionHandler:"
+ "loadAllForCurrentGameWithCompletionHandler:"
+ "loadChallengeDefinitionsWithCompletionHandler:"
+ "loadGameActivityDefinitionsWith:completionHandler:"
+ "loadGameActivityDefinitionsWithCompletionHandler:"
+ "loadGameActivityDefinitionsWithIDs:completionHandler:"
+ "loadImageForURL:queue:withCompletionHandler:"
+ "loadImageWithCompletionHandler:"
+ "loadLeaderboardsWithCompletionHandler:"
+ "loadLeaderboardsWithIDs:completionHandler:"
+ "loadPlayersForIdentifiers:withCompletionHandler:"
+ "loadPlayersForIdentifiersPrivate:withCompletionHandler:"
+ "local"
+ "localPlayer"
+ "localPlayerIDProvider"
+ "mainBundle"
+ "markAsProcessed"
+ "maxPlayers"
+ "minPlayers"
+ "participantStates"
+ "participants"
+ "partyCode"
+ "partyURL"
+ "pause"
+ "percentComplete"
+ "playStyle"
+ "player"
+ "playerFormPlayerID:"
+ "playerFromPlayerID:"
+ "playerID"
+ "playerWantsToPlayGameActivity:completion:"
+ "postNotificationName:object:userInfo:"
+ "properties"
+ "proxyForLocalPlayer"
+ "q16@0:8"
+ "referralAchievement"
+ "referralLeaderboard"
+ "removeAchievements:"
+ "removeScoresFromLeaderboards:"
+ "reportAchievements:withCompletionHandler:"
+ "resume"
+ "resumedGameActivityFromSnapshot:withCompletionHandler:"
+ "service"
+ "setAchievementCompleted:"
+ "setContext:"
+ "setGsTimer:"
+ "setLastUpdateTime:"
+ "setLeaderboardID:"
+ "setMaxPlayers:"
+ "setMinPlayers:"
+ "setPercentComplete:"
+ "setPlayer:"
+ "setPlayerGroup:"
+ "setProgressOnAchievement:toPercentComplete:"
+ "setProperties:"
+ "setScoreOnLeaderboard:toScore:"
+ "setScoreOnLeaderboard:toScore:context:"
+ "setShowsCompletionBanner:"
+ "setValidPartyCodeAlphabets:"
+ "setValue:"
+ "setupMatchRequestAndReturnError:"
+ "setupUpdateSubscription"
+ "shared"
+ "sharedController"
+ "sharedMatchmaker"
+ "shortGroupID"
+ "snapshotWithCompletionHandler:"
+ "start"
+ "startDate"
+ "startWithDefinition:error:"
+ "startWithDefinition:partyCode:error:"
+ "state"
+ "submitScore:context:player:leaderboardIDs:completionHandler:"
+ "subscriptions"
+ "support"
+ "supportsPartyCode"
+ "supportsUnlimitedPlayers"
+ "template"
+ "timeIntervalSinceDate:"
+ "title"
+ "updateTrigger"
+ "v16@0:8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"UIImage\"8"
+ "v24@0:8@16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"GKMatch\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?B>16"
+ "v24@?0@\"GKGameActivity\"8@\"NSError\"16"
+ "v24@?0@\"GKMatch\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v32@0:8@16@?<v@?@\"GKGameActivity\"@\"NSError\">24"
+ "v32@0:8@16d24"
+ "v32@0:8@16q24"
+ "v40@0:8@16@24@?32"
+ "v40@0:8@16q24q32"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16q24q32@40"
+ "v8@?0"
+ "validPartyCodeAlphabets"
+ "value"

```
