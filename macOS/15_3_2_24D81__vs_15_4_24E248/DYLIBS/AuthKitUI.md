## AuthKitUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/AuthKitUI`

```diff

-493.230.1.0.0
-  __TEXT.__text: 0x376e4
+493.462.0.0.0
+  __TEXT.__text: 0x36e60
   __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x4164
+  __TEXT.__objc_methlist: 0x4e38
   __TEXT.__const: 0x298
-  __TEXT.__oslogstring: 0x11c9
-  __TEXT.__cstring: 0x20aa
+  __TEXT.__oslogstring: 0x1257
+  __TEXT.__cstring: 0x216e
   __TEXT.__ustring: 0x1c
-  __TEXT.__gcc_except_tab: 0x3b0
-  __TEXT.__unwind_info: 0xfe0
+  __TEXT.__gcc_except_tab: 0x3a8
+  __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_classname: 0xcc8
-  __TEXT.__objc_methname: 0xddca
-  __TEXT.__objc_methtype: 0x29ff
-  __TEXT.__objc_stubs: 0xaa80
-  __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x958
+  __TEXT.__objc_methname: 0xdf8b
+  __TEXT.__objc_methtype: 0x2aa3
+  __TEXT.__objc_stubs: 0xaac0
+  __DATA_CONST.__got: 0x7b0
+  __DATA_CONST.__const: 0x960
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3458
+  __DATA_CONST.__objc_selrefs: 0x3940
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x538
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x21a0
-  __AUTH_CONST.__objc_const: 0xd560
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__objc_const: 0xc008
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x15e0
-  __DATA.__objc_ivar: 0x3d8
+  __DATA.__objc_ivar: 0x3e4
   __DATA.__data: 0xc60
   __DATA.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D2504ED-C9F7-3F59-B456-660C2A4A166B
-  Functions: 1536
-  Symbols:   4484
-  CStrings:  3356
+  UUID: 4068DCAD-6DFF-3D83-BB8E-6670A1435BDA
+  Functions: 1549
+  Symbols:   4508
+  CStrings:  3367
 
Symbols:
+ -[AKAppleIDProximityAuthenticationContext .cxx_destruct]
+ -[AKAppleIDProximityAuthenticationContext proxDelegate]
+ -[AKAppleIDProximityAuthenticationContext proximityAIDAHandler]
+ -[AKAppleIDProximityAuthenticationContext secondaryButtonTitle]
+ -[AKAppleIDProximityAuthenticationContext setProxDelegate:]
+ -[AKAppleIDProximityAuthenticationContext setProximityAIDAHandler:]
+ -[AKAppleIDProximityAuthenticationContext setSecondaryButtonTitle:]
+ -[AKInlineSignInViewController _presentShieldUIIfNeededWithViewController:]
+ -[AKInlineSignInViewController _presentShieldUIIfNeededWithViewController:].cold.1
+ -[AKInlineSignInViewController _presentShieldUIIfNeededWithViewController:].cold.2
+ -[AKInlineSignInViewController _presentShieldUIWithViewController:]
+ -[AKInlineSignInViewController _presentShieldUIWithViewController:].cold.1
+ -[AKInlineSignInViewController viewDidAppear:]
+ -[AKTextField cachedImageUsingBlock:].cold.1
+ AKCreateAppleIDButtonImageWithCornerRadius.cold.1
+ OBJC_IVAR_$_AKAppleIDProximityAuthenticationContext._proxDelegate
+ OBJC_IVAR_$_AKAppleIDProximityAuthenticationContext._proximityAIDAHandler
+ OBJC_IVAR_$_AKAppleIDProximityAuthenticationContext._secondaryButtonTitle
+ _AKUIMainBundle.cold.1
+ _ColorSpaceStandardRGB.cold.1
+ _CreateAttributedStringWithFontSize.cold.1
+ __OBJC_$_INSTANCE_VARIABLES_AKAppleIDProximityAuthenticationContext
+ __OBJC_$_PROP_LIST_AKAppleIDProximityAuthenticationContext
+ __block_literal_global.142
+ __block_literal_global.71
+ _objc_msgSend$_presentShieldUIIfNeededWithViewController:
+ _objc_msgSend$_presentShieldUIWithViewController:
+ _objc_msgSend$shieldSignInOrCreateFlows
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __block_literal_global.149
- __block_literal_global.78
- _objc_msgSend$isAABrandingEnabled
CStrings:
+ "%@: Not presenting shield UI, not needed"
+ "%@: Shielding sign in / create flows by presenting shield UI with view controller: %@"
+ "%s (%d) called"
+ "-[AKInlineSignInViewController _presentShieldUIIfNeededWithViewController:]"
+ "-[AKInlineSignInViewController _presentShieldUIWithViewController:]"
+ "/System/AppleInternal/Library/Frameworks/CoreFollowUp.framework/CoreFollowUp"
+ "@\"<AKAppleIDProximityAuthenticationContextDelegate>\""
+ "@\"UIConversationContext\"16@0:8"
+ "APPLE_ID_ALERT_PLACEHOLDER_REBRAND"
+ "APPLE_ID_PASSWORD_HEADER_REBRAND"
+ "APPLE_ID_REBRAND"
+ "APPLE_ID_SIGN_IN_HEADER_REBRAND"
+ "AUTHORIZATION_VIEWCONTROLLER_TITLE_REBRAND"
+ "AUTHORIZE_APPLE_ID_1ST_PARTY_LOGIN_KEY_ACCESS_REBRAND"
+ "AUTHORIZE_APPLE_ID_1ST_PARTY_LOGIN_REBRAND"
+ "AUTHORIZE_FIRST_TIME_MANAGED_ACCOUNT_MESSAGE_1_REBRAND"
+ "AUTHORIZE_FIRST_TIME_MESSAGE_1_REBRAND"
+ "AUTHORIZE_FOR_ACCOUNT_WITH_PASSWORD_REBRAND"
+ "AUTHORIZE_UPGRADE_MESSAGE_1_NOBIO_REBRAND"
+ "CREATE_APPLE_ID_BUTTON_TITLE_REBRAND"
+ "CREATE_APPLE_ID_REBRAND"
+ "FORGOT_APPLE_ID_REBRAND"
+ "FORGOT_DESCRIPTION_REBRAND"
+ "T@\"<AKAppleIDProximityAuthenticationContextDelegate>\",W,N,V_proxDelegate"
+ "T@\"NSString\",C,N,V_secondaryButtonTitle"
+ "T@\"UIConversationContext\",?,&,N"
+ "T@?,N,V_proximityAIDAHandler"
+ "USE_APPLE_ID_REBRAND"
+ "USE_DIFFERENT_APPLE_ID_REBRAND"
+ "VERIFICATION_HEADER_REBRAND"
+ "_presentShieldUIIfNeededWithViewController:"
+ "_presentShieldUIWithViewController:"
+ "_proxDelegate"
+ "_proximityAIDAHandler"
+ "conversationContext"
+ "proxDelegate"
+ "proximityAIDAHandler"
+ "setConversationContext:"
+ "setProxDelegate:"
+ "setProximityAIDAHandler:"
+ "shieldSignInOrCreateFlows"
+ "textField:insertInputSuggestion:"
+ "v24@0:8@\"UIConversationContext\"16"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
- "APPLE_ID"
- "APPLE_ID_ALERT_PLACEHOLDER"
- "APPLE_ID_PASSWORD_HEADER"
- "APPLE_ID_SIGN_IN_HEADER"
- "AUTHORIZATION_VIEWCONTROLLER_TITLE"
- "AUTHORIZE_APPLEID_CREATE"
- "AUTHORIZE_APPLE_ID_1ST_PARTY_LOGIN"
- "AUTHORIZE_APPLE_ID_1ST_PARTY_LOGIN_KEY_ACCESS"
- "AUTHORIZE_APPLE_ID_UPGRADE_LOGIN"
- "AUTHORIZE_APPLE_ID_WELCOME"
- "AUTHORIZE_FIRST_TIME_MANAGED_ACCOUNT_MESSAGE_1"
- "AUTHORIZE_FIRST_TIME_MESSAGE_1"
- "AUTHORIZE_FOR_ACCOUNT_WITH_PASSWORD"
- "AUTHORIZE_MANAGED_APPLEID_CREATE"
- "AUTHORIZE_MANAGED_APPLEID_WELCOME"
- "AUTHORIZE_UPGRADE_MESSAGE_1_NOBIO"
- "CREATE_APPLE_ID"
- "CREATE_APPLE_ID_BUTTON_TITLE"
- "FORGOT_APPLE_ID"
- "FORGOT_DESCRIPTION"
- "REBRAND"
- "USE_APPLE_ID"
- "USE_DIFFERENT_APPLE_ID"
- "VERIFICATION_HEADER"
- "_REBRAND"
- "isAABrandingEnabled"

```
