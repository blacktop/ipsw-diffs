## AssistantSettingsSupport

> `/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport`

```diff

-3510.7.1.1.2
-  __TEXT.__text: 0x52064
+3510.7.2.11.5
+  __TEXT.__text: 0x5291c
   __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x2a3c
+  __TEXT.__objc_methlist: 0x2a8c
   __TEXT.__const: 0x1264
-  __TEXT.__gcc_except_tab: 0x808
-  __TEXT.__cstring: 0x6bdd
-  __TEXT.__oslogstring: 0x1941
+  __TEXT.__gcc_except_tab: 0x820
+  __TEXT.__cstring: 0x6d2d
+  __TEXT.__oslogstring: 0x1991
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x3dc
   __TEXT.__constg_swiftt: 0x9b4

   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift_as_entry: 0x90
   __TEXT.__swift_as_ret: 0x9c
-  __TEXT.__unwind_info: 0x1528
+  __TEXT.__unwind_info: 0x1548
   __TEXT.__eh_frame: 0x11a4
-  __TEXT.__objc_classname: 0x68d
-  __TEXT.__objc_methname: 0x86a4
-  __TEXT.__objc_methtype: 0xcc5
-  __TEXT.__objc_stubs: 0x6820
-  __DATA_CONST.__got: 0x9f0
-  __DATA_CONST.__const: 0xd30
+  __TEXT.__objc_classname: 0x6ad
+  __TEXT.__objc_methname: 0x87c8
+  __TEXT.__objc_methtype: 0xcdf
+  __TEXT.__objc_stubs: 0x68e0
+  __DATA_CONST.__got: 0xa00
+  __DATA_CONST.__const: 0xd58
   __DATA_CONST.__objc_classlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21b8
+  __DATA_CONST.__objc_selrefs: 0x21f0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0xe08
-  __AUTH_CONST.__const: 0x1070
-  __AUTH_CONST.__cfstring: 0x3f60
-  __AUTH_CONST.__objc_const: 0x44a0
+  __AUTH_CONST.__const: 0x1090
+  __AUTH_CONST.__cfstring: 0x4000
+  __AUTH_CONST.__objc_const: 0x4578
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1418
   __AUTH.__data: 0x2a0
-  __DATA.__objc_ivar: 0x2d4
-  __DATA.__data: 0xb58
+  __DATA.__objc_ivar: 0x2e0
+  __DATA.__data: 0xbb8
   __DATA.__bss: 0xed8
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x658

   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition
+  - /System/Library/PrivateFrameworks/SystemVoiceAssistantServices.framework/SystemVoiceAssistantServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F42E0047-B9FF-38CF-886D-3CA54B9AEB0A
-  Functions: 1701
-  Symbols:   4254
-  CStrings:  2968
+  UUID: D84E3599-F8F1-3FBC-9B34-A3B7F6D70A73
+  Functions: 1709
+  Symbols:   4290
+  CStrings:  2994
 
Symbols:
+ -[AssistantActivationController _addHyperlinkStyleToText:inString:action:forGroup:]
+ -[AssistantActivationController _refreshTalkToSiriFooter]
+ -[AssistantActivationController _updateSideButtonSpecifierState]
+ -[AssistantActivationController eligibilityDidChange]
+ -[AssistantActivationController navigateToSideButtonSettings]
+ -[AssistantActivationController navigateToSideButtonSettings].cold.1
+ GCC_except_table23
+ _OBJC_CLASS_$_SVASSettingsConnection
+ _OBJC_IVAR_$_AssistantActivationController._shouldDisableSideButtonSpecifier
+ _OBJC_IVAR_$_AssistantActivationController._sideButtonAppName
+ _OBJC_IVAR_$_AssistantActivationController._svasSettingsConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SVASSettingsConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SVASSettingsConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_SVASSettingsConnectionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AssistantActivationController
+ __OBJC_LABEL_PROTOCOL_$_SVASSettingsConnectionDelegate
+ __OBJC_PROTOCOL_$_SVASSettingsConnectionDelegate
+ ___64-[AssistantActivationController _updateSideButtonSpecifierState]_block_invoke
+ ___64-[AssistantActivationController _updateSideButtonSpecifierState]_block_invoke.194
+ ___block_descriptor_40_e8_32w_e45_v24?0"SVASApplicationIdentity"8"NSError"16lw32l8
+ _kSVASSideButtonSettingDidChange
+ _objc_msgSend$_refreshTalkToSiriFooter
+ _objc_msgSend$_updateSideButtonSpecifierState
+ _objc_msgSend$activateWithInvalidationHandler:
+ _objc_msgSend$initWithDispatchQueue:
+ _objc_msgSend$nameForApplicationWithBundleID:
+ _objc_msgSend$selectedAssistantApplicationIdentityWithCompletion:
CStrings:
+ "%s Side Button Settings link clicked"
+ "%s svas-settings connection invalidated"
+ "-[AssistantActivationController _updateSideButtonSpecifierState]_block_invoke"
+ "-[AssistantActivationController navigateToSideButtonSettings]"
+ "@\"SVASSettingsConnection\""
+ "AssistantActivationExtra"
+ "SIDEBUTTON_FOOTER"
+ "SIDEBUTTON_LINK_MISSING_APP_NAME"
+ "SIDEBUTTON_LINK_TEXT"
+ "SVASSettingsConnectionDelegate"
+ "_refreshTalkToSiriFooter"
+ "_shouldDisableSideButtonSpecifier"
+ "_sideButtonAppName"
+ "_svasSettingsConnection"
+ "_updateSideButtonSpecifierState"
+ "activateWithInvalidationHandler:"
+ "eligibilityDidChange"
+ "initWithDispatchQueue:"
+ "navigateToSideButtonSettings"
+ "selectedAssistantApplicationIdentityWithCompletion:"
+ "settings-navigation://com.apple.Settings.SideButton"
+ "v24@?0@\"SVASApplicationIdentity\"8@\"NSError\"16"
+ "\xe1"
- "\xb1"

```
