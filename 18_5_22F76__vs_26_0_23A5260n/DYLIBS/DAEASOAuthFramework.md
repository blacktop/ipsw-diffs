## DAEASOAuthFramework

> `/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework`

```diff

-2067.40.1.0.0
-  __TEXT.__text: 0xcc84
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0xc30
+2072.0.0.0.0
+  __TEXT.__text: 0xce88
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0xc40
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__cstring: 0xe05
+  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__cstring: 0xe36
   __TEXT.__oslogstring: 0x167d
   __TEXT.__unwind_info: 0x290
   __TEXT.__objc_classname: 0x249
-  __TEXT.__objc_methname: 0x2994
+  __TEXT.__objc_methname: 0x2a47
   __TEXT.__objc_methtype: 0x4bc
-  __TEXT.__objc_stubs: 0x2180
-  __DATA_CONST.__got: 0x2e0
+  __TEXT.__objc_stubs: 0x2240
+  __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__const: 0x4c0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb00
+  __DATA_CONST.__objc_selrefs: 0xb30
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x278
-  __AUTH_CONST.__cfstring: 0x15c0
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__cfstring: 0x1620
   __AUTH_CONST.__objc_const: 0x1ed0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 259BBA29-0065-34F6-A79D-6E718E2FE330
-  Functions: 242
-  Symbols:   1180
-  CStrings:  1001
+  UUID: B0B30A21-EC4A-3020-929D-63862A7F2C3C
+  Functions: 243
+  Symbols:   1192
+  CStrings:  1015
 
Symbols:
+ +[DAEASOAuthClient clientRedirectURLSchemeForOAuthType:]
+ +[DAOAuthSafariViewController authenticationSessionWithURL:callbackURLScheme:handler:]
+ _ACUIDescriptionFromEmailAddress
+ _OBJC_CLASS_$_ASWebAuthenticationSessionCallback
+ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke.24
+ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke.58
+ ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke_2.25
+ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.121
+ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.123
+ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.76
+ __os_feature_enabled_impl
+ _kConsumerEASEndPoint
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$callbackWithCustomScheme:
+ _objc_msgSend$clientRedirectForOAuthType:
+ _objc_msgSend$initWithURL:callback:completionHandler:
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$queryItemWithName:value:
- +[DAOAuthSafariViewController authenticationSessionWithURL:handler:]
- ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke.41
- ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke.9
- ___123-[DAEASOAuthWebViewController _commonInitializationWithAccount:accountStore:username:accountDescription:presentationBlock:]_block_invoke_2.10
- ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.104
- ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.106
- ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke.59
CStrings:
+ "AccountsUI"
+ "ModernAddFlow"
+ "arrayWithArray:"
+ "authenticationSessionWithURL:callbackURLScheme:handler:"
+ "callbackWithCustomScheme:"
+ "clientRedirectURLSchemeForOAuthType:"
+ "code_challenge"
+ "code_challenge_method"
+ "display"
+ "initWithURL:callback:completionHandler:"
+ "localeIdentifier"
+ "login_hint"
+ "queryItemWithName:value:"
+ "ui_locales"
- "authenticationSessionWithURL:handler:"
- "code_challenge=%@"
- "code_challenge_method=%@"

```
