## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-466.7.15.0.0
-  __TEXT.__text: 0x5fbf8
+466.23.1.1.0
+  __TEXT.__text: 0x5fcf0
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x60d4
-  __TEXT.__const: 0x2d0
+  __TEXT.__objc_methlist: 0x6124
+  __TEXT.__const: 0x2b0
   __TEXT.__gcc_except_tab: 0x884
   __TEXT.__cstring: 0x405a
-  __TEXT.__oslogstring: 0x3a99
+  __TEXT.__oslogstring: 0x3b0e
   __TEXT.__ustring: 0x1c
-  __TEXT.__unwind_info: 0x1a20
-  __TEXT.__objc_classname: 0x12ac
-  __TEXT.__objc_methname: 0x1459a
+  __TEXT.__unwind_info: 0x19fc
+  __TEXT.__objc_classname: 0x12d0
+  __TEXT.__objc_methname: 0x146b8
   __TEXT.__objc_methtype: 0x3d4d
-  __TEXT.__objc_stubs: 0x10140
-  __DATA_CONST.__got: 0x4b0
+  __TEXT.__objc_stubs: 0x10200
+  __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__const: 0x1240
-  __DATA_CONST.__objc_classlist: 0x330
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x14a80
-  __DATA_CONST.__objc_selrefs: 0x4c78
+  __DATA_CONST.__objc_const: 0x14ad8
+  __DATA_CONST.__objc_selrefs: 0x4cb8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x6e8
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__objc_const: 0x2290
+  __AUTH_CONST.__objc_const: 0x22d8
   __AUTH_CONST.__cfstring: 0x3dc0
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH.__objc_data: 0x1cc0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x6e0
-  __DATA.__objc_superrefs: 0x260
+  __AUTH.__objc_data: 0x1d10
   __DATA.__objc_ivar: 0x640
   __DATA.__data: 0x1468
   __DATA.__bss: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 874365AD-EAD7-3909-B3C8-D171B52A770D
-  Functions: 2554
-  Symbols:   9611
-  CStrings:  5328
+  UUID: CFD69CAE-2A55-3F51-BA66-DB6AE94C0715
+  Functions: 2563
+  Symbols:   9637
+  CStrings:  5344
 
Symbols:
+ +[AKAuthorizationAppearance useDifferentIDButtonTextColor]
+ -[AKAuthorizationButton setupButton]
+ -[AKAuthorizationInputPaneViewController _isUnderageUser]
+ -[AKAuthorizationInputPaneViewController _setEditableScopeChoicesForUnderageUser]
+ -[AKAuthorizationSubPaneConfirmButton _checkIfPasscodeFallbackAllowedWithCompletion:]
+ -[AKAuthorizationUseDifferentIDButton initWithCoder:]
+ -[AKAuthorizationUseDifferentIDButton initWithFrame:]
+ -[AKAuthorizationViewController _parentalApprovalRequestViewController]
+ -[AKBasicLoginViewController _keyboardDidShow:]
+ -[AKBringDeviceCloseMicaView arePhonesTogether]
+ -[AKUIMicaPlayer setRootLayer:].cold.1
+ GCC_except_table142
+ GCC_except_table75
+ _OBJC_CLASS_$_AKAuthorizationUseDifferentIDButton
+ _OBJC_METACLASS_$_AKAuthorizationUseDifferentIDButton
+ __OBJC_$_INSTANCE_METHODS_AKAuthorizationUseDifferentIDButton
+ __OBJC_CLASS_RO_$_AKAuthorizationUseDifferentIDButton
+ __OBJC_METACLASS_RO_$_AKAuthorizationUseDifferentIDButton
+ ___85-[AKAuthorizationSubPaneConfirmButton _checkIfPasscodeFallbackAllowedWithCompletion:]_block_invoke
+ ___87-[AKAuthorizationSubPaneConfirmButton _handleBiometricAuthFailureWithError:forContext:]_block_invoke
+ ___block_literal_global.142
+ _objc_msgSend$_checkIfPasscodeFallbackAllowedWithCompletion:
+ _objc_msgSend$_isUnderageUser
+ _objc_msgSend$_setEditableScopeChoicesForUnderageUser
+ _objc_msgSend$arePhonesTogether
+ _objc_msgSend$isTiburonU13Enabled
+ _objc_msgSend$isUnderage
+ _objc_msgSend$setInheritsTiming:
- +[AKAuthorizationSubPaneMetrics scopeDetailLabelTrailingSpacing]
- -[AKAuthorizationContinueButton _commonInit]
- -[AKBasicLoginViewController _keyboardWillShow:]
- -[AKBringDeviceCloseMicaView arePhonesTogather]
- GCC_except_table140
- GCC_except_table26
- GCC_except_table73
- _UIKeyboardFrameBeginUserInfoKey
- __AKIconDefaultSize
- ___block_literal_global.141
- _kActivityIndicatorPadding
- _objc_msgSend$arePhonesTogather
CStrings:
+ "AKAuthorizationUseDifferentIDButton"
+ "Disabling inherits timing on root layer: %@"
+ "Location based device policy preflight passcode validation returned with error %@"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"RUIObjectModel\",?,&,N"
+ "T@\"RUIServerHookResponse\",?,&,N"
+ "T@\"RUIServerHookResponse\",?,&,N,V_serverHookResponse"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "Tq,?,N"
+ "User opted to use another Apple ID."
+ "_checkIfPasscodeFallbackAllowedWithCompletion:"
+ "_isUnderageUser"
+ "_keyboardDidShow:"
+ "_parentalApprovalRequestViewController"
+ "_setEditableScopeChoicesForUnderageUser"
+ "arePhonesTogether"
+ "callerIconPath"
+ "isTiburonU13Enabled"
+ "isUnderage"
+ "setInheritsTiming:"
+ "setupButton"
+ "useDifferentIDButtonTextColor"
- "T@\"RUIObjectModel\",&,N"
- "T@\"RUIServerHookResponse\",&,N"
- "T@\"RUIServerHookResponse\",&,N,V_serverHookResponse"
- "T@\"UITextInputPasswordRules\",C,N"
- "TB,N,GisSecureTextEntry"
- "User declined to use the suggested Apple ID."
- "_keyboardWillShow:"
- "arePhonesTogather"
- "scopeDetailLabelTrailingSpacing"

```
