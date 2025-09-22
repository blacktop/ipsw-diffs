## ManagedConfigurationUI

> `/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`

```diff

-52.0.0.0.0
-  __TEXT.__text: 0x24d70
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x3960
+54.0.0.0.0
+  __TEXT.__text: 0x24a68
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x3908
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x61c
-  __TEXT.__cstring: 0x3062
+  __TEXT.__gcc_except_tab: 0x614
+  __TEXT.__cstring: 0x310c
   __TEXT.__ustring: 0x46
-  __TEXT.__unwind_info: 0xca0
+  __TEXT.__unwind_info: 0xc90
   __TEXT.__objc_classname: 0x9c6
-  __TEXT.__objc_methname: 0xac67
-  __TEXT.__objc_methtype: 0x1f63
-  __TEXT.__objc_stubs: 0x7860
+  __TEXT.__objc_methname: 0xab21
+  __TEXT.__objc_methtype: 0x1f55
+  __TEXT.__objc_stubs: 0x7740
   __DATA_CONST.__got: 0x740
-  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__const: 0xa88
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2870
+  __DATA_CONST.__objc_selrefs: 0x2818
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x25e0
-  __AUTH_CONST.__objc_const: 0x5660
+  __AUTH_CONST.__cfstring: 0x2640
+  __AUTH_CONST.__objc_const: 0x55a8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x2dc
+  __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0xb40
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
+  - /System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5A5491F1-8EC4-31BA-8D5E-4FB2A4F0108E
-  Functions: 1114
-  Symbols:   4422
-  CStrings:  2619
+  UUID: A1670E33-36BA-3E0E-AD15-6842E23D7126
+  Functions: 1108
+  Symbols:   4399
+  CStrings:  2611
 
Symbols:
+ _LAPasscodeServiceErrorDomain
+ _NSStringFromClass
+ _OBJC_CLASS_$_LAPasscodeVerificationService
+ _OBJC_CLASS_$_LAPasscodeVerificationServiceOptions
+ __OBJC_$_PROP_LIST_MCInstallProfileViewController
+ ___63-[MCInstallProfileViewController(PIN) pinExtensionShowPINSheet]_block_invoke
+ ___63-[MCInstallProfileViewController(PIN) pinExtensionShowPINSheet]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40w_e31_v24?0"LAContext"8"NSError"16lw40l8s32l8
+ _objc_msgSend$contentConfiguration
+ _objc_msgSend$credentialOfType:reply:
+ _objc_msgSend$didAcceptEnteredPIN:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$setPasscodeSubPrompt:
+ _objc_msgSend$startInParentVC:completion:
- -[MCInstallationWarningCell .cxx_destruct]
- -[MCInstallationWarningCell _setupConstraints]
- -[MCInstallationWarningCell _setup]
- -[MCInstallationWarningCell constraints]
- -[MCInstallationWarningCell setConstraints:]
- -[MCInstallationWarningCell setWarningLabel:]
- -[MCInstallationWarningCell warningLabel]
- _BPSApplyStyleToNavBar
- _BPSDetailTextColor
- _OBJC_CLASS_$_UITextView
- _OBJC_IVAR_$_MCInstallationWarningCell._constraints
- _OBJC_IVAR_$_MCInstallationWarningCell._warningLabel
- _UIEdgeInsetsZero
- _UIFontTextStyleBody
- __OBJC_$_INSTANCE_VARIABLES_MCInstallationWarningCell
- __OBJC_$_PROP_LIST_MCInstallationWarningCell
- ___75-[MCInstallProfileViewController(PIN) _didFinishEnteringPINWithCompletion:]_block_invoke_2
- _objc_msgSend$_setupConstraints
- _objc_msgSend$constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:
- _objc_msgSend$constraints
- _objc_msgSend$preferredFontForTextStyle:
- _objc_msgSend$removeConstraints:
- _objc_msgSend$setConstraints:
- _objc_msgSend$setDataDetectorTypes:
- _objc_msgSend$setEditable:
- _objc_msgSend$setLineFragmentPadding:
- _objc_msgSend$setModalTransitionStyle:
- _objc_msgSend$setScrollEnabled:
- _objc_msgSend$setSelectable:
- _objc_msgSend$setTextContainerInset:
- _objc_msgSend$textContainer
- _objc_msgSend$warningLabel
CStrings:
+ "Failed to get credential from context: %@"
+ "Got password"
+ "LAPasscodeVerificationService canceled"
+ "LAPasscodeVerificationService failed: %@"
+ "contentConfiguration"
+ "credentialOfType:reply:"
+ "initWithData:encoding:"
+ "setPasscodeSubPrompt:"
+ "startInParentVC:completion:"
+ "v24@?0@\"LAContext\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
- "@\"UITextView\""
- "T@\"NSArray\",&,N,V_constraints"
- "T@\"UITextView\",&,N,V_warningLabel"
- "_constraints"
- "_setupConstraints"
- "_warningLabel"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "constraints"
- "preferredFontForTextStyle:"
- "removeConstraints:"
- "setConstraints:"
- "setDataDetectorTypes:"
- "setEditable:"
- "setLineFragmentPadding:"
- "setModalTransitionStyle:"
- "setScrollEnabled:"
- "setSelectable:"
- "setTextContainerInset:"
- "setWarningLabel:"
- "textContainer"
- "warningLabel"

```
