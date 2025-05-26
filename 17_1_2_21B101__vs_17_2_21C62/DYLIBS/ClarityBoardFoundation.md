## ClarityBoardFoundation

> `/System/Library/PrivateFrameworks/ClarityBoardFoundation.framework/ClarityBoardFoundation`

```diff

-67.0.4.0.0
-  __TEXT.__text: 0x521c
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0xc8
-  __TEXT.__const: 0x302
-  __TEXT.__cstring: 0x37f
-  __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__swift5_typeref: 0xf4
-  __TEXT.__swift5_reflstr: 0xbe
+67.0.9.0.0
+  __TEXT.__text: 0xa254
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0xf8
+  __TEXT.__const: 0x432
+  __TEXT.__cstring: 0x7da
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__oslogstring: 0x42
+  __TEXT.__swift5_typeref: 0x1a2
+  __TEXT.__swift5_fieldmd: 0x124
+  __TEXT.__constg_swiftt: 0x2c0
+  __TEXT.__swift5_reflstr: 0x15a
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__constg_swiftt: 0x19c
-  __TEXT.__swift5_fieldmd: 0x68
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x244
-  __TEXT.__objc_classname: 0x2e
-  __TEXT.__objc_methname: 0x2c5
-  __TEXT.__objc_methtype: 0xb8
-  __TEXT.__objc_stubs: 0x1c0
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x364
+  __TEXT.__eh_frame: 0x78
+  __TEXT.__objc_classname: 0x2d
+  __TEXT.__objc_methname: 0x3cf
+  __TEXT.__objc_methtype: 0xfa
+  __TEXT.__objc_stubs: 0x260
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0x2c0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3f8
-  __DATA_CONST.__objc_selrefs: 0xe8
-  __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__const: 0x148
+  __DATA_CONST.__objc_const: 0x548
+  __DATA_CONST.__objc_selrefs: 0x140
+  __AUTH_CONST.__cfstring: 0x540
+  __AUTH_CONST.__const: 0x2b0
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__auth_got: 0x568
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x260
+  __AUTH.__data: 0x3c0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x38
+  __DATA.__objc_classrefs: 0x58
   __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x140
-  __DATA.__bss: 0x1d0
-  __DATA.__common: 0x18
+  __DATA.__objc_ivar: 0x18
+  __DATA.__data: 0x1d0
+  __DATA.__bss: 0x2d0
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 147
-  Symbols:   305
-  CStrings:  86
+  Functions: 260
+  Symbols:   396
+  CStrings:  140
 
Symbols:
+ -[CLBMobileKeybagManager _lockStateFromDictionary:]
+ -[CLBMobileKeybagManager hasUnlockedSinceBoot]
+ -[CLBMobileKeybagManager unregisterFirstUnlockBlockWithIdentifier:]
+ -[CLBMobileKeybagManager unregisterLockStateChangedBlockWithIdentifier:]
+ GCC_except_table10
+ GCC_except_table14
+ GCC_except_table27
+ GCC_except_table29
+ _CLBAccessibilityUIServerBundleIdentifier
+ _CLBAssistantServiceJobLabel
+ _CLBAssistiveTouchBundleIdentifier
+ _CLBCallServicesJobLabel
+ _CLBClarityBoardBundleIdentifier
+ _CLBCoreAuthDaemonBundleIdentifier
+ _CLBCoreAuthUIBundleIdentifier
+ _CLBDruidBundleIdentifier
+ _CLBFaceTimeBundleIdentifier
+ _CLBInCallServiceBundleIdentifier
+ _CLBInstrumentsBundleIdentifier
+ _CLBInstrumentsFoundationBundleIdentifier
+ _CLBMailCompositionServiceBundleIdentifier
+ _CLBMessagesCompositionServiceBundleIdentifier
+ _CLBMobilePhoneBundleIdentifier
+ _CLBSOSBundleIdentifier
+ _CLBSafariViewServiceBundleIdentifier
+ _CLBTestManagerBundleIdentifier
+ _CLBVoiceControlBundleIdentifier
+ _CLBXcodeBundleIdentifier
+ _MKBDeviceUnlockedSinceBoot
+ _MKBEventsRegister
+ _MKBEventsUnregister
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_RBSProcessIdentity
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_IVAR_$_CLBMobileKeybagManager._mkbEvent
+ __DATA__TtC22ClarityBoardFoundation23OpenApplicationVerifier
+ __IVARS__TtC22ClarityBoardFoundation23OpenApplicationVerifier
+ __METACLASS_DATA__TtC22ClarityBoardFoundation23OpenApplicationVerifier
+ __OBJC_$_CLASS_PROP_LIST_CLBMobileKeybagManager
+ ___67-[CLBMobileKeybagManager unregisterFirstUnlockBlockWithIdentifier:]_block_invoke
+ ___72-[CLBMobileKeybagManager unregisterLockStateChangedBlockWithIdentifier:]_block_invoke
+ ___block_descriptor_40_e8_32w_e28_v20?0i8^{__CFDictionary=}12lw32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy1_1
+ ___swift_memcpy24_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ __os_log_impl
+ __swiftEmptySetSingleton
+ __swift_stdlib_malloc_size
+ _associated conformance 22ClarityBoardFoundation29OpenApplicationVerifierResultV9ErrorCodeOSHAASQ
+ _block_copy_helper.10
+ _block_copy_helper.7
+ _block_descriptor.12
+ _block_descriptor.9
+ _block_destroy_helper.11
+ _block_destroy_helper.8
+ _malloc_size
+ _memcpy
+ _objc_msgSend$UUID
+ _objc_msgSend$_lockStateFromDictionary:
+ _objc_msgSend$allValues
+ _objc_msgSend$commonLog
+ _objc_msgSend$dictionary
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$stringWithFormat:
+ _objc_release_x23
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retainBlock
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x25
+ _os_log_type_enabled
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_dynamicCast
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_initStackObject
+ _swift_initStructMetadata
+ _swift_setDeallocating
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _symbolic $s22ClarityBoardFoundation30OpenApplicationVerifierRequestP
+ _symbolic ShySSG
+ _symbolic So19MobileKeybagManager_p
+ _symbolic _____ 22ClarityBoardFoundation23OpenApplicationVerifierC
+ _symbolic _____ 22ClarityBoardFoundation29OpenApplicationVerifierResultV
+ _symbolic _____ 22ClarityBoardFoundation29OpenApplicationVerifierResultV5ErrorV
+ _symbolic _____ 22ClarityBoardFoundation29OpenApplicationVerifierResultV9ErrorCodeO
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____Sg 22ClarityBoardFoundation29OpenApplicationVerifierResultV5ErrorV
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySo18RBSProcessIdentityCG s11_SetStorageC
- GCC_except_table13
- GCC_except_table15
- GCC_except_table23
- GCC_except_table25
- GCC_except_table8
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_IVAR_$_CLBMobileKeybagManager._firstUnlockToken
- _OBJC_IVAR_$_CLBMobileKeybagManager._keybagStatusChangedToken
- ___30-[CLBMobileKeybagManager init]_block_invoke_3
- ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- _block_copy_helper.5
- _block_copy_helper.8
- _block_descriptor.10
- _block_descriptor.7
- _block_destroy_helper.6
- _block_destroy_helper.9
- _notify_cancel
- _notify_register_dispatch
- _objc_alloc
- _objc_msgSend$addObject:
- _objc_msgSend$initWithCapacity:
- _swift_unknownObjectRelease_n
- _symbolic So19MobileKeybagManager_pSg
CStrings:
+ "\x05"
+ "@\"NSMutableDictionary\""
+ "@\"NSUUID\"24@0:8@?<v@?>16"
+ "@24@0:8@?16"
+ "Disabled"
+ "Handle first unlock"
+ "Handle keybag status changed"
+ "In Assert Delay"
+ "In Bio Unlock"
+ "In Grace Period"
+ "Locked"
+ "Locked state: %@"
+ "Locking"
+ "No installed application found for "
+ "Not allowing open application request from unallowed client process."
+ "System app URL requests only supported for PPT."
+ "T@\"CLBMobileKeybagManager\",R,N"
+ "TB,R,N"
+ "The application cannot be opened in Assistive Access."
+ "UUID"
+ "Unknown: %ld"
+ "Unlock In Progress"
+ "Unlocked"
+ "Untrusted open application requests are not allowed in Assistive Access."
+ "^{_MKBEvent=}"
+ "_TtC22ClarityBoardFoundation23OpenApplicationVerifier"
+ "_lockStateFromDictionary:"
+ "_mkbEvent"
+ "_shouldHandleTestURL:"
+ "allValues"
+ "com.apple.AccessibilityUIServer"
+ "com.apple.ClarityBoard"
+ "com.apple.CoreAuthUI"
+ "com.apple.CoreDevice.dtappserviced"
+ "com.apple.DTServiceHub"
+ "com.apple.DragUI.druid"
+ "com.apple.InCallService"
+ "com.apple.MailCompositionService"
+ "com.apple.SOS"
+ "com.apple.SafariViewService"
+ "com.apple.assistant_service"
+ "com.apple.assistivetouchd"
+ "com.apple.commandandcontrol"
+ "com.apple.coreauthd"
+ "com.apple.dt.instruments.DVTInstrumentsFoundation"
+ "com.apple.facetime"
+ "com.apple.mobilephone"
+ "com.apple.mobilesms.compose"
+ "com.apple.telephonyutilities.callservicesd"
+ "com.apple.testmanagerd"
+ "description"
+ "dictionary"
+ "hasUnlockedSinceBoot"
+ "identityForDaemonJobLabel:"
+ "lockStateChangedBlockIdentifier"
+ "q24@0:8@16"
+ "setObject:forKeyedSubscript:"
+ "sharedApplication"
+ "stringWithFormat:"
+ "unregisterFirstUnlockBlockWithIdentifier:"
+ "unregisterLockStateChangedBlockWithIdentifier:"
+ "userSelectedApplicationBundleIdentifiers"
+ "v20@?0i8^{__CFDictionary=}12"
+ "v24@0:8@\"NSUUID\"16"
+ "v24@0:8@16"
+ "with neither bundle id or process id"
- "\x03\x12"
- "@\"NSMutableArray\""
- "_firstUnlockToken"
- "_keybagStatusChangedToken"
- "addObject:"
- "com.apple.mobile.keybagd.first_unlock"
- "com.apple.mobile.keybagd.lock_status"
- "i"
- "initWithCapacity:"
- "v12@?0i8"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"

```
