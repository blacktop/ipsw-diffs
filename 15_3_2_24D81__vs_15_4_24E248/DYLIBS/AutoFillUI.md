## AutoFillUI

> `/System/Library/PrivateFrameworks/AutoFillUI.framework/Versions/A/AutoFillUI`

```diff

-71.203.0.0.0
-  __TEXT.__text: 0x201b0
+71.301.0.0.0
+  __TEXT.__text: 0x2014c
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x1998
+  __TEXT.__objc_methlist: 0x1d30
   __TEXT.__const: 0x120
   __TEXT.__cstring: 0xc81
   __TEXT.__gcc_except_tab: 0x5b0
   __TEXT.__dlopen_cstrs: 0x107
   __TEXT.__ustring: 0xdc
   __TEXT.__oslogstring: 0x10c
-  __TEXT.__unwind_info: 0x6c0
+  __TEXT.__unwind_info: 0x6c8
   __TEXT.__objc_classname: 0x3c1
   __TEXT.__objc_methname: 0x5bf3
   __TEXT.__objc_methtype: 0xb06

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17a0
+  __DATA_CONST.__objc_selrefs: 0x1890
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x790
   __AUTH_CONST.__cfstring: 0x1420
-  __AUTH_CONST.__objc_const: 0x4880
+  __AUTH_CONST.__objc_const: 0x41f8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x780

   - /System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AD9755D3-CF9F-3D3D-844C-09398ADC760F
-  Functions: 684
-  Symbols:   2153
+  UUID: AACDB527-09CE-37C0-81E8-FF6666FDCE9B
+  Functions: 698
+  Symbols:   2183
   CStrings:  1490
 
Symbols:
+ +[AFUIAdapter runtimeClass].cold.1
+ -[AFUIContactsController _meContactInfosForTextContentType:meContact:].cold.1
+ -[AFUITargetDetectionController _detectionDisabledForResponder:].cold.1
+ -[AFUITargetDetectionController _detectionEnabledForResponder:].cold.1
+ -[AFUITargetDetectionController accessibilityLoginKeywordList].cold.1
+ -[AFUITargetDetectionController accessibilitySignupKeywordList].cold.1
+ -[AFUITargetDetectionController loginKeywordList].cold.1
+ -[AFUITargetDetectionController signupKeywordList].cold.1
+ -[AFUITargetDetectionController textContentTypeForResponder:traits:contentTypesFound:].cold.1
+ AFUIAutoFillPopoverControllerOSLogFacility.cold.1
+ AFUIIsAppleApp.cold.1
+ AFUIPanelOSLogFacility.cold.1
+ AFUIResponderIsExemptFromDetectionHints.cold.1
+ AFUIServiceDelegateOSLogFacility.cold.1
+ _AFUIApplicationClass.cold.1
+ _AFUIButtonClass.cold.1
+ _AFUICacheRuntimeObjects.cold.1
+ _AFUIColorClass.cold.1
+ _AFUIFontClass.cold.1
+ _AFUINavigationControllerClass.cold.1
+ _AFUIResponderClass.cold.1
+ _AFUISecureTextFieldClass.cold.1
+ _AFUITextFieldClass.cold.1
+ _AFUITextInputProtocol.cold.1
+ _AFUITextViewClass.cold.1
+ _AFUITraitsClass.cold.1
+ _AFUITraitsProtocol.cold.1
+ _AFUIViewClass.cold.1
+ _AFUIViewControllerClass.cold.1
+ __86-[AFUITargetDetectionController textContentTypeForResponder:traits:contentTypesFound:]_block_invoke_2.cold.1

```
