## ScreenTimeUICore

> `/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore`

```diff

-605.2.3.0.0
-  __TEXT.__text: 0xa4be8
-  __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_methlist: 0x1f0
-  __TEXT.__const: 0x5214
-  __TEXT.__cstring: 0x24c5
-  __TEXT.__constg_swiftt: 0x1ef4
-  __TEXT.__swift5_typeref: 0x9dce
+605.2.5.0.0
+  __TEXT.__text: 0xa6a44
+  __TEXT.__auth_stubs: 0x25e0
+  __TEXT.__objc_methlist: 0x410
+  __TEXT.__const: 0x52d4
+  __TEXT.__cstring: 0x25f5
+  __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__oslogstring: 0x994
+  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__constg_swiftt: 0x1f30
+  __TEXT.__swift5_typeref: 0x9e2a
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x133f
   __TEXT.__swift5_assocty: 0x690
-  __TEXT.__swift5_fieldmd: 0x1814
-  __TEXT.__swift5_capture: 0x5f8
+  __TEXT.__swift5_fieldmd: 0x1824
+  __TEXT.__swift5_capture: 0x638
   __TEXT.__swift5_proto: 0x190
-  __TEXT.__swift5_types: 0x1f8
-  __TEXT.__oslogstring: 0x6e4
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x30
+  __TEXT.__swift5_types: 0x1fc
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x1d50
-  __TEXT.__eh_frame: 0x1890
-  __TEXT.__objc_classname: 0xaa
-  __TEXT.__objc_methname: 0x8b3
-  __TEXT.__objc_methtype: 0x82
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x6e0
-  __DATA_CONST.__const: 0x220
-  __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__unwind_info: 0x1e48
+  __TEXT.__eh_frame: 0x1a48
+  __TEXT.__objc_classname: 0x128
+  __TEXT.__objc_methname: 0xd53
+  __TEXT.__objc_methtype: 0x262
+  __TEXT.__objc_stubs: 0x3e0
+  __DATA_CONST.__got: 0x720
+  __DATA_CONST.__const: 0x2f8
+  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a0
+  __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1220
-  __AUTH_CONST.__const: 0x2460
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x1300
+  __AUTH_CONST.__const: 0x2500
   __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0xc78
-  __AUTH.__objc_data: 0x538
-  __AUTH.__data: 0x2c10
-  __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x22b0
-  __DATA.__bss: 0x32d8
+  __AUTH_CONST.__objc_const: 0x1028
+  __AUTH.__objc_data: 0x690
+  __AUTH.__data: 0x2c38
+  __DATA.__objc_ivar: 0x1c
+  __DATA.__data: 0x23a0
+  __DATA.__bss: 0x32e8
   __DATA.__common: 0x70
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard
   - /System/Library/PrivateFrameworks/Categories.framework/Categories
+  - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift
   - /System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 12716101-B1F5-3DC7-9F14-F5C6210FCB1C
-  Functions: 2446
-  Symbols:   1436
-  CStrings:  399
+  UUID: F795977C-376E-3E71-8E4D-6E8A58C56DDE
+  Functions: 2500
+  Symbols:   1583
+  CStrings:  496
 
Symbols:
+ -[STParentAuthenticationPrompt .cxx_destruct]
+ -[STParentAuthenticationPrompt coordinator]
+ -[STParentAuthenticationPrompt presentFromViewController:completion:]
+ -[STParentAuthenticationPrompt setCoordinator:]
+ -[STParentAuthenticationPromptCoordinator .cxx_destruct]
+ -[STParentAuthenticationPromptCoordinator appleIDSetupPresenter]
+ -[STParentAuthenticationPromptCoordinator completion]
+ -[STParentAuthenticationPromptCoordinator initWithPresentingViewController:completion:]
+ -[STParentAuthenticationPromptCoordinator parentGuardianLoginPresenter:didCompleteWithResponse:]
+ -[STParentAuthenticationPromptCoordinator parentGuardianLoginPresenter:didFailWithError:]
+ -[STParentAuthenticationPromptCoordinator parentGuardianLoginPresenter:didFailWithError:].cold.1
+ -[STParentAuthenticationPromptCoordinator present]
+ -[STParentAuthenticationPromptCoordinator setAppleIDSetupPresenter:]
+ -[STParentAuthenticationPromptCoordinator setCompletion:]
+ -[STParentAuthenticationPromptCoordinator setStPresentingViewController:]
+ -[STParentAuthenticationPromptCoordinator stPresentingViewController]
+ GCC_except_table0
+ GCC_except_table6
+ _AKAuthenticationAlternateDSIDKey
+ _AppleIDSetupUILibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_FAFetchFamilyCircleRequest
+ _OBJC_CLASS_$_STLog
+ _OBJC_CLASS_$_STParentAuthenticationPrompt
+ _OBJC_CLASS_$_STParentAuthenticationPromptCoordinator
+ _OBJC_CLASS_$__TtC16ScreenTimeUICore45STParentAuthenticationPromptResponseValidator
+ _OBJC_IVAR_$_STParentAuthenticationPrompt._coordinator
+ _OBJC_IVAR_$_STParentAuthenticationPromptCoordinator._appleIDSetupPresenter
+ _OBJC_IVAR_$_STParentAuthenticationPromptCoordinator._completion
+ _OBJC_IVAR_$_STParentAuthenticationPromptCoordinator._stPresentingViewController
+ _OBJC_METACLASS_$_STParentAuthenticationPrompt
+ _OBJC_METACLASS_$_STParentAuthenticationPromptCoordinator
+ _OBJC_METACLASS_$__TtC16ScreenTimeUICore45STParentAuthenticationPromptResponseValidator
+ __Block_object_dispose
+ __CLASS_METHODS__TtC16ScreenTimeUICore45STParentAuthenticationPromptResponseValidator
+ __DATA__TtC16ScreenTimeUICore45STParentAuthenticationPromptResponseValidator
+ __INSTANCE_METHODS__TtC16ScreenTimeUICore45STParentAuthenticationPromptResponseValidator
+ __METACLASS_DATA__TtC16ScreenTimeUICore45STParentAuthenticationPromptResponseValidator
+ __OBJC_$_INSTANCE_METHODS_STParentAuthenticationPrompt
+ __OBJC_$_INSTANCE_METHODS_STParentAuthenticationPromptCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_STParentAuthenticationPrompt
+ __OBJC_$_INSTANCE_VARIABLES_STParentAuthenticationPromptCoordinator
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_STParentAuthenticationPrompt
+ __OBJC_$_PROP_LIST_STParentAuthenticationPromptCoordinator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AISParentGuardianLoginPresenterDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AISParentGuardianLoginPresenterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_AISParentGuardianLoginPresenterDelegate
+ __OBJC_CLASS_PROTOCOLS_$_STParentAuthenticationPromptCoordinator
+ __OBJC_CLASS_RO_$_STParentAuthenticationPrompt
+ __OBJC_CLASS_RO_$_STParentAuthenticationPromptCoordinator
+ __OBJC_LABEL_PROTOCOL_$_AISParentGuardianLoginPresenterDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_STParentAuthenticationPrompt
+ __OBJC_METACLASS_RO_$_STParentAuthenticationPromptCoordinator
+ __OBJC_PROTOCOL_$_AISParentGuardianLoginPresenterDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ __Unwind_Resume
+ ___69-[STParentAuthenticationPrompt presentFromViewController:completion:]_block_invoke
+ ___69-[STParentAuthenticationPrompt presentFromViewController:completion:]_block_invoke_2
+ ___96-[STParentAuthenticationPromptCoordinator parentGuardianLoginPresenter:didCompleteWithResponse:]_block_invoke
+ ___AppleIDSetupUILibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32bs40w_e8_v12?0B8lw40l8s32l8
+ ___getAISParentGuardianLoginPresenterClass_block_invoke
+ ___getAISParentGuardianLoginPresenterClass_block_invoke.cold.1
+ ___objc_personality_v0
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_0
+ __dispatch_main_q
+ __os_log_error_impl
+ __sl_dlopen
+ __swift_stdlib_bridgeErrorToNSError
+ _abort_report_np
+ _audit_stringAppleIDSetupUI
+ _dispatch_async
+ _getAISParentGuardianLoginPresenterClass.softClass
+ _objc_alloc_init
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_getClass
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$appleIDSetupPresenter
+ _objc_msgSend$completion
+ _objc_msgSend$coordinator
+ _objc_msgSend$initWithPresentingViewController:completion:
+ _objc_msgSend$present
+ _objc_msgSend$regulatoryRestrictions
+ _objc_msgSend$setCoordinator:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$stPresentingViewController
+ _objc_msgSend$startParentGuardianLoginWithViewControllerPresentationHandler:
+ _objc_msgSend$validateResponse:withCompletion:
+ _objc_retainAutorelease
+ _objc_retain_x19
+ _objc_retain_x3
+ _objc_setProperty_nonatomic_copy
+ _objc_storeWeak
+ _objectdestroy.7Tm
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _symbolic SbIeyBy_
+ _symbolic SccySo14FAFamilyCircleC______pG s5ErrorP
+ _symbolic So12NSDictionaryC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 16ScreenTimeUICore45STParentAuthenticationPromptResponseValidatorC
+ _symbolic _____XMo 16ScreenTimeUICore45STParentAuthenticationPromptResponseValidatorC
- _objectdestroy.55Tm
CStrings:
+ "#16@0:8"
+ "%s"
+ "@\"AISParentGuardianLoginPresenter\""
+ "@\"NSString\"16@0:8"
+ "@\"STParentAuthenticationPromptCoordinator\""
+ "@\"UIViewController<STParentAuthenticationPromptPresenting>\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@16@?24"
+ "@40@0:8:16@24@32"
+ "@?"
+ "@?16@0:8"
+ "AISParentGuardianLoginPresenter"
+ "AISParentGuardianLoginPresenterDelegate"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "NSObject"
+ "Parent authentication prompt failed with error: %{public}@"
+ "Q16@0:8"
+ "STParentAuthenticationPrompt"
+ "STParentAuthenticationPromptCoordinator"
+ "STParentAuthenticationPromptResponseValidator found altDSID in response: %{private}s"
+ "STParentAuthenticationPromptResponseValidator found no altDSID in response"
+ "STParentAuthenticationPromptResponseValidator unable to determine if altDSID matches guardian: %{public}@; assuming not guardian"
+ "STParentAuthenticationPromptResponseValidator: response does not match any family member"
+ "STParentAuthenticationPromptResponseValidator: response matches guardian"
+ "STParentAuthenticationPromptResponseValidator: response matches non-guardian family member"
+ "Showing parent authentication prompt"
+ "T#,R"
+ "T@\"AISParentGuardianLoginPresenter\",&,N,V_appleIDSetupPresenter"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"STParentAuthenticationPromptCoordinator\",&,N,V_coordinator"
+ "T@\"UIViewController<STParentAuthenticationPromptPresenting>\",W,N,V_stPresentingViewController"
+ "T@?,C,N,V_completion"
+ "TQ,R"
+ "Unable to find class %s"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_TtC16ScreenTimeUICore45STParentAuthenticationPromptResponseValidator"
+ "_appleIDSetupPresenter"
+ "_completion"
+ "_coordinator"
+ "_stPresentingViewController"
+ "appleIDSetupPresenter"
+ "autorelease"
+ "class"
+ "com.apple.screentime.core"
+ "completion"
+ "conformsToProtocol:"
+ "coordinator"
+ "debugDescription"
+ "description"
+ "hash"
+ "initWithPresentingViewController:completion:"
+ "isEqual:"
+ "isGuardian"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "memberForAltDSID:"
+ "parentGuardianLoginPresenter:didCompleteWithResponse:"
+ "parentGuardianLoginPresenter:didFailWithError:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "present"
+ "presentFromViewController:completion:"
+ "regulatoryRestrictions"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "setAppleIDSetupPresenter:"
+ "setCompletion:"
+ "setCoordinator:"
+ "setDelegate:"
+ "setStPresentingViewController:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI"
+ "stPresentingViewController"
+ "startParentGuardianLoginWithViewControllerPresentationHandler:"
+ "startRequestWithCompletionHandler:"
+ "superclass"
+ "v12@?0B8"
+ "v24@0:8@16"
+ "v24@?0@\"FAFamilyCircle\"8@\"NSError\"16"
+ "v32@0:8@\"AISParentGuardianLoginPresenter\"16@\"NSDictionary\"24"
+ "v32@0:8@\"AISParentGuardianLoginPresenter\"16@\"NSError\"24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B>24"
+ "v32@0:8@16@24"
+ "validateResponse:withCompletion:"
+ "zone"

```
