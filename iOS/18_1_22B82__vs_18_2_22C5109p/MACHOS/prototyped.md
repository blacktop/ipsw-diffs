## prototyped

> `/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/prototyped`

```diff

-155.1.1.0.0
-  __TEXT.__text: 0x5908
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x594
+155.2.3.0.0
+  __TEXT.__text: 0xa73c
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_stubs: 0x12e0
+  __TEXT.__objc_methlist: 0x570
   __TEXT.__ustring: 0x272
-  __TEXT.__cstring: 0x47a
-  __TEXT.__objc_methname: 0x32a3
-  __TEXT.__objc_classname: 0x223
-  __TEXT.__objc_methtype: 0x14f8
-  __TEXT.__const: 0x38
-  __TEXT.__oslogstring: 0x338
-  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__cstring: 0x996
+  __TEXT.__objc_methname: 0x318a
+  __TEXT.__objc_classname: 0x201
+  __TEXT.__objc_methtype: 0x159c
+  __TEXT.__const: 0x28a
+  __TEXT.__oslogstring: 0x2be
+  __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x290
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x4a0
-  __DATA_CONST.__cfstring: 0x500
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__swift5_entry: 0x8
+  __TEXT.__constg_swiftt: 0x214
+  __TEXT.__swift5_typeref: 0x21d
+  __TEXT.__swift5_fieldmd: 0x190
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_reflstr: 0x193
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_capture: 0x70
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x18
+  __TEXT.__unwind_info: 0x400
+  __TEXT.__eh_frame: 0x230
+  __DATA_CONST.__auth_got: 0x520
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__auth_ptr: 0xd0
+  __DATA_CONST.__const: 0x7a8
+  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2a38
-  __DATA.__objc_selrefs: 0x7e8
-  __DATA.__objc_ivar: 0x94
-  __DATA.__objc_data: 0x320
-  __DATA.__data: 0x540
-  __DATA.__bss: 0x38
+  __DATA.__objc_const: 0x2f20
+  __DATA.__objc_selrefs: 0x778
+  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_data: 0x6e8
+  __DATA.__data: 0x7d0
+  __DATA.__bss: 0x340
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 158
-  Symbols:   156
-  CStrings:  725
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftFileProvider.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 272
+  Symbols:   296
+  CStrings:  741
 
Symbols:
+ _$s12CoreGraphics7CGFloatVMn
+ _$s15_ObjectiveCTypes01_A11CBridgeablePTl
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$s5UIKit31UISceneSessionActivationRequestV4role12userActivity7optionsACSo0bC4Rolea_So06NSUserH0CSgSo0bdE7OptionsCSgtcfC
+ _$s5UIKit31UISceneSessionActivationRequestVMa
+ _$s8RawValueSYTl
+ _$sBOWV
+ _$sBi64_WV
+ _$sSD10FoundationE36_unconditionallyBridgeFromObjectiveCySDyxq_GSo12NSDictionaryCSgFZ
+ _$sSD11descriptionSSvg
+ _$sSH13_rawHashValue4seedS2i_tFTq
+ _$sSH4hash4intoys6HasherVz_tFTq
+ _$sSH9hashValueSivgTq
+ _$sSHMp
+ _$sSHSQTb
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE26_forceBridgeFromObjectiveC_6resultySo8NSStringC_SSSgztFZ
+ _$sSS10FoundationE34_conditionallyBridgeFromObjectiveC_6resultSbSo8NSStringC_SSSgztFZ
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS4hash4intoys6HasherVz_tF
+ _$sSS6appendyySSF
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSS9hashValueSivg
+ _$sSSSHsWP
+ _$sSY8rawValue03RawB0QzvgTq
+ _$sSY8rawValuexSg03RawB0Qz_tcfCTq
+ _$sSYMp
+ _$sScA15unownedExecutorScevgTj
+ _$sScM6sharedScMvgZ
+ _$sScMMa
+ _$sScMScAsWP
+ _$sScP8rawValues5UInt8Vvg
+ _$sScPMa
+ _$sSh10FoundationE36_unconditionallyBridgeFromObjectiveCyShyxGSo5NSSetCSgFZ
+ _$sSh8IteratorV6_cocoaAByx_Gs10__CocoaSetVAACn_tcfC
+ _$sSiN
+ _$sSis23CustomStringConvertiblesWP
+ _$sSo13UIApplicationC5UIKitE20activateSceneSession3for12errorHandleryAC07UISceneE17ActivationRequestV_ys5Error_pcSgtF
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
+ _$sSo8NSObjectCSH10ObjectiveCMc
+ _$sSw10copyMemory4fromySW_tF
+ _$sSwys5UInt8VSicis
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss10__CocoaSetV12makeIteratorAB0D0CyF
+ _$ss10__CocoaSetV5countSivg
+ _$ss10__CocoaSetV8IteratorC4nextyXlSgyF
+ _$ss11CommandLineO10unsafeArgvSpySpys4Int8VGSgGvgZ
+ _$ss11CommandLineO4argcs5Int32VvgZ
+ _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsVN
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss20_SwiftNewtypeWrapperMp
+ _$ss20_SwiftNewtypeWrapperPSYTb
+ _$ss20_SwiftNewtypeWrapperPs35_HasCustomAnyHashableRepresentationTb
+ _$ss20_SwiftNewtypeWrapperPsSHRzSH8RawValueSYRpzrlE20_toCustomAnyHashables0hI0VSgyF
+ _$ss21_ObjectiveCBridgeableMp
+ _$ss21_ObjectiveCBridgeableP016_forceBridgeFromA1C_6resulty01_A5CTypeQz_xSgztFZTq
+ _$ss21_ObjectiveCBridgeableP024_conditionallyBridgeFromA1C_6resultSb01_A5CTypeQz_xSgztFZTq
+ _$ss21_ObjectiveCBridgeableP026_unconditionallyBridgeFromA1Cyx01_A5CTypeQzSgFZTq
+ _$ss21_ObjectiveCBridgeableP09_bridgeToA1C01_A5CTypeQzyFTq
+ _$ss23CustomStringConvertibleP11descriptionSSvgTj
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss27_stringCompareWithSmolCheck__9expectingSbs11_StringGutsV_ADs01_G16ComparisonResultOtF
+ _$ss35_HasCustomAnyHashableRepresentationMp
+ _$ss35_HasCustomAnyHashableRepresentationP03_tobcD0s0cD0VSgyFTq
+ _$ss5UInt8VMn
+ _$ss6HasherV5_seedABSi_tcfC
+ _$ss6HasherV9_finalizeSiyF
+ _$syXlN
+ _$sypN
+ _$sytN
+ _CGAffineTransformMakeScale
+ _CGRectApplyAffineTransform
+ _NSStringFromClass
+ _OBJC_CLASS_$_UIPanGestureRecognizer
+ _OBJC_CLASS_$_UIPinchGestureRecognizer
+ _OBJC_CLASS_$_UIScene
+ _OBJC_CLASS_$_UISceneSessionActivationRequest
+ _OBJC_CLASS_$_UIWindowScene
+ _UIWindowSceneSessionRoleApplication
+ __Block_copy
+ __Block_release
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_enumerationMutation
+ _objc_opt_self
+ _objc_retain_x24
+ _objc_retain_x26
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastClassUnconditional
+ _swift_dynamicCastObjCClass
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
- _CGRectOffset
- _OBJC_CLASS_$_FBSOrientationObserver
- _OBJC_CLASS_$_UIMutableApplicationSceneClientSettings
- _OBJC_CLASS_$_UISApplicationSupportDisplayEdgeInfo
- _OBJC_CLASS_$_UIScreen
- _OBJC_CLASS_$_UIView
- _OBJC_EHTYPE_$_NSException
- _PTUINumericKeypadSetNeededWithWindow
- _UIEdgeInsetsFromApplicationSupportDisplayEdgeInsetsWrapper
- _UIEdgeInsetsZero
- _dispatch_sync
- _exit
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_begin_catch
- _objc_end_catch
- _objc_unsafeClaimAutoreleasedReturnValue
- _os_variant_has_internal_diagnostics
CStrings:
+ "$__lazy_storage_$_editingServer"
+ "$__lazy_storage_$_originalBounds"
+ "$__lazy_storage_$_originalOrigin"
+ "$__lazy_storage_$_panGesture"
+ "$__lazy_storage_$_pinchGesture"
+ "$__lazy_storage_$_rootModuleController"
+ "$__lazy_storage_$_settingsViewController"
+ "@\"<PTUIClient>\""
+ "@\"NSUserActivity\"24@0:8@\"UIScene\"16"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Modified Settings"
+ "Multi Window Enabled"
+ "PTUIClient"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<PTUIClient>\",W,N,V_delegate"
+ "UISceneDelegate"
+ "UIWindowSceneDelegate"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_TtC10prototyped11AppDelegate"
+ "_TtC10prototyped11Application"
+ "_TtC10prototyped13SceneDelegate"
+ "_TtC10prototyped6Window"
+ "_TtC10prototypedP33_7D6121B4D28911B7760A4E8ABB7760C28Listener"
+ "_TtC10prototypedP33_7D6121B4D28911B7760A4E8ABB7760C28UIServer"
+ "activateSceneSessionForRequest:errorHandler:"
+ "addGestureRecognizer:"
+ "application didFinishLaunchingWithOptions: %!s(MISSING)"
+ "center"
+ "connectedScenes"
+ "connection"
+ "countByEnumeratingWithState:objects:count:"
+ "dealloc"
+ "didDrag:"
+ "didPinch:"
+ "didSelectDone"
+ "endEditing:"
+ "frame"
+ "handle prototyping event: %!s(MISSING)"
+ "hardwareRingerButton"
+ "hardwareRingerSwitch"
+ "hardwareVolumeDown"
+ "hardwareVolumeUp"
+ "initWithContentRect:"
+ "initWithRootModule:"
+ "initWithTarget:action:"
+ "initWithWindowScene:"
+ "invalid Collection: less than 'count' elements in collection"
+ "listener"
+ "listener shouldAcceptNewConnection: %!@(MISSING)"
+ "makeKeyAndVisible"
+ "multiWindowEnabled"
+ "navigationBar"
+ "prototyped/AppDelegate.swift"
+ "prototyped/Application.swift"
+ "prototyped/SceneDelegate.swift"
+ "removeFromSuperview"
+ "request"
+ "requestSceneSessionDestruction:options:errorHandler:"
+ "rootViewController"
+ "scene:continueUserActivity:"
+ "scene:didFailToContinueUserActivityWithType:error:"
+ "scene:didUpdateUserActivity:"
+ "scene:openURLContexts:"
+ "scene:restoreInteractionStateWithUserActivity:"
+ "scene:willConnectToSession:options:"
+ "scene:willContinueUserActivityWithType:"
+ "sceneDidBecomeActive:"
+ "sceneDidDisconnect:"
+ "sceneDidEnterBackground:"
+ "sceneWillEnterForeground:"
+ "sceneWillResignActive:"
+ "session"
+ "setBounds:"
+ "setCenter:"
+ "setMultiWindowEnabled:"
+ "setTranslation:inView:"
+ "sharedApplication"
+ "showModifiedSettings"
+ "state"
+ "stateRestorationActivityForScene:"
+ "translationInView:"
+ "uiServer"
+ "v24@0:8@\"UIScene\"16"
+ "v32@0:8@\"UIScene\"16@\"NSSet\"24"
+ "v32@0:8@\"UIScene\"16@\"NSString\"24"
+ "v32@0:8@\"UIScene\"16@\"NSUserActivity\"24"
+ "v32@0:8@\"UIWindowScene\"16@\"CKShareMetadata\"24"
+ "v40@0:8@\"UIScene\"16@\"NSString\"24@\"NSError\"32"
+ "v40@0:8@\"UIScene\"16@\"UISceneSession\"24@\"UISceneConnectionOptions\"32"
+ "v40@0:8@\"UIWindowScene\"16@\"UIApplicationShortcutItem\"24@?<v@?B>32"
+ "v48@0:8@\"UIWindowScene\"16@\"<UICoordinateSpace>\"24q32@\"UITraitCollection\"40"
+ "v48@0:8@16@24q32@40"
+ "windowScene"
+ "windowScene:didUpdateCoordinateSpace:interfaceOrientation:traitCollection:"
+ "windowScene:performActionForShortcutItem:completionHandler:"
+ "windowScene:userDidAcceptCloudKitShareWithMetadata:"
- "\x05\x15!"
- "@\"<PTDRootModuleDelegate>\""
- "@\"FBSOrientationObserver\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"PTDRemotePrototypingServer\""
- "@\"PTDRootModuleController\""
- "@\"PTDWindow\""
- "@\"PTUISettingsController\""
- "Modified Settomgs"
- "PTDApplication"
- "PTDRootModuleDelegate"
- "PTDServer"
- "PTDServer active test recipe"
- "PTDServer delay exit after showing UI"
- "PTDServer showing UI"
- "PTDWindow"
- "PTSettingsKeyObserver"
- "PTUIServer expects to only talk to a single client, and it already has one. Refusing additional connection."
- "Prototype daemon did finish launching"
- "T@\"<PTDRootModuleDelegate>\",W,N,V_delegate"
- "_animateUsingDefaultTimingWithOptions:animations:completion:"
- "_client"
- "_currentOrientation"
- "_delayExitAfterShowingUI"
- "_delayExitAfterUITimer"
- "_delayingExitAfterUI"
- "_endDelayingExitAfterShowingUI"
- "_frameForHidingSettingsWindow"
- "_frameForShowingSettingsWindow"
- "_hasActiveTestRecipe"
- "_hidePrototypingUI"
- "_initWithRootModule:"
- "_interfaceOrientationObserver"
- "_isSystemUIService"
- "_listener"
- "_normalizedSafeAreaInsets"
- "_noteActivePrototypingEnabled:"
- "_noteHasActiveTestRecipe:"
- "_notePrototypeSettingsEnabled:"
- "_noteRemotePrototypingEnabled:"
- "_observeDefaults"
- "_postPrototypingIsActiveNotification"
- "_reloadWithRootModule:"
- "_remotePrototypingServer"
- "_rootModuleController"
- "_setAllWindowsKeepContextInBackground:"
- "_setRotatableViewOrientation:duration:"
- "_setUpOrientationObserver"
- "_settingsController"
- "_shouldDelayExitAfterUI"
- "_showOrHidePrototypingUI"
- "_showPrototypingUI"
- "_showingUI"
- "_systemUIServiceClientSettings"
- "_systemUIServiceIdentifier"
- "_updateCurrentOrientation:"
- "_updatePreventingLockover"
- "_window"
- "activeInterfaceOrientationWithCompletion:"
- "activePrototypingEnabled"
- "addKeyObserver:"
- "com.apple.internal.prototyped"
- "com.apple.prototyped"
- "defaultDisplayEdgeInfo"
- "handle prototyping event: %!@(MISSING)"
- "hiding prototyping UI"
- "isHidden"
- "mainScreen"
- "observeDefault:onQueue:withBlock:"
- "observeTestRecipeDefaultsOnQueue:withBlock:"
- "orientation"
- "persistChanges"
- "prototypeSettingsEnabled"
- "q"
- "remotePrototypingEnabled"
- "safeAreaInsetsPortrait"
- "setAutoresizingMask:"
- "setContentScaleFactor:"
- "setHandler:"
- "setHidden:"
- "setPreferredLevel:"
- "settings"
- "settings:changedValueForKey:"
- "showModifiedSettomgs"
- "showing prototyping UI"
- "stringWithUTF8String:"
- "testRecipeIsActive"
- "uh oh, our workaround for rdar://problem/45299814 has stopped working!"
- "v12@?0B8"
- "v16@?0@\"FBSOrientationUpdate\"8"
- "v32@0:8@\"PTSettings\"16@\"NSString\"24"
- "valueForKey:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{UIEdgeInsets=dddd}16@0:8"

```
