## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/Versions/A/PlatformSSOCore`

```diff

-643.0.33.0.0
-  __TEXT.__text: 0x100594
-  __TEXT.__objc_methlist: 0x7158
-  __TEXT.__const: 0x33c8
-  __TEXT.__cstring: 0xf627
-  __TEXT.__oslogstring: 0x5f53
+643.1.1.0.0
+  __TEXT.__text: 0x10186c
+  __TEXT.__objc_methlist: 0x71d0
+  __TEXT.__const: 0x33d8
+  __TEXT.__cstring: 0xf5f7
+  __TEXT.__oslogstring: 0x6293
   __TEXT.__gcc_except_tab: 0x114c
   __TEXT.__dlopen_cstrs: 0x363
   __TEXT.__swift5_typeref: 0x66e

   __TEXT.__swift_as_cont: 0x118
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x3568
-  __TEXT.__eh_frame: 0x2080
+  __TEXT.__unwind_info: 0x3578
+  __TEXT.__eh_frame: 0x2088
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36d8
+  __DATA_CONST.__objc_selrefs: 0x3720
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0xb58
+  __DATA_CONST.__got: 0xb60
   __AUTH_CONST.__const: 0x2df8
-  __AUTH_CONST.__cfstring: 0x8ba0
-  __AUTH_CONST.__objc_const: 0x17898
+  __AUTH_CONST.__cfstring: 0x8b80
+  __AUTH_CONST.__objc_const: 0x17928
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x1088
+  __AUTH_CONST.__auth_got: 0x1078
   __AUTH.__objc_data: 0x3438
   __AUTH.__data: 0x928
-  __DATA.__objc_ivar: 0x6f8
+  __DATA.__objc_ivar: 0x704
   __DATA.__data: 0x14e8
   __DATA.__bss: 0x1760
   __DATA.__common: 0x89

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5687
-  Symbols:   8764
-  CStrings:  2638
+  Functions: 5700
+  Symbols:   8785
+  CStrings:  2646
 
Symbols:
+ +[POAuthenticationProcess authorizationContextScopes]
+ -[POAuthenticationAccessKeyManager scope]
+ -[POAuthenticationAccessKeyManager setScope:]
+ -[POAuthenticationContext includePlatformSSOAuthorizationScopes]
+ -[POAuthenticationContext setIncludePlatformSSOAuthorizationScopes:]
+ -[POAuthenticationProcess _requestScopeForContext:]
+ -[POAuthenticationProcess _scopeByRemovingAuthorizationContextScopes:]
+ -[POLoginConfiguration includePlatformSSOAuthorizationScopes]
+ -[POLoginConfiguration setIncludePlatformSSOAuthorizationScopes:]
+ OBJC_IVAR_$_POAuthenticationAccessKeyManager._scope
+ OBJC_IVAR_$_POAuthenticationContext._includePlatformSSOAuthorizationScopes
+ OBJC_IVAR_$_POLoginConfiguration._includePlatformSSOAuthorizationScopes
+ _OBJC_CLASS_$_TKLoginHelper
+ __OBJC_$_CLASS_METHODS_POAuthenticationProcess
+ _objc_msgSend$_requestScopeForContext:
+ _objc_msgSend$_scopeByRemovingAuthorizationContextScopes:
+ _objc_msgSend$authorizationContextScopes
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$clearSensitiveData
+ _objc_msgSend$includePlatformSSOAuthorizationScopes
+ _objc_msgSend$initWithTokenID:pubKeyHash:wrapPubKeyHash:pin:userPassword:keychainPassword:
+ _objc_msgSend$pairEverything:
+ _objc_msgSend$setIncludePlatformSSOAuthorizationScopes:
- _SecKeychainCopyLogin
- _SecKeychainStoreUnlockKeyWithPubKeyHash
CStrings:
+ "Authentication flow: Attempting IdP authentication for user %{private,mask.hash}s"
+ "Authentication flow: Authentication result = %{public}s"
+ "Authentication flow: IdP authentication failed with result: %{public}s"
+ "Authentication flow: Login result = %{public}s"
+ "Authentication flow: Successfully encoded authentication context for user %{private,mask.hash}s"
+ "Authentication flow: Token inserted for user %{private,mask.hash}s"
+ "Authentication flow: temporary user authentication failed"
+ "Ignoring stale AltSecurityIdentity pairing to temporary session account"
+ "Login Policy: Login Result = %{public}s"
+ "SmartCard keychain/FileVault/keybag pairing succeeded for token %{public}@"
+ "TKLoginHelper pairEverything failed during SmartCard binding."
+ "Using passthrough authenticator: no authenticators active"
+ "authenticateTemporaryOpenIDUser: outcome=failed session=%{public}s user=%{private,mask.hash}s"
+ "authenticateTemporaryOpenIDUser: outcome=success session=%{public}s user=%{private,mask.hash}s"
+ "handleOpenIDAuthentication: result=%{public}s"
+ "passthrough produced builtin-auth blob, handing credential to builtin auth"
+ "userNameEntered: result=%{public}s"
- "A"
- "Authentication flow: Attempting IdP authentication for user %s"
- "Authentication flow: IdP authentication failed with result: %s"
- "Authentication flow: Login result = %s"
- "Authentication flow: OpenID Authorization Request: Result = %s"
- "Authentication flow: Result = %s"
- "Login Policy: Login Result = %s"
- "SecKeychainCopyLogin failed for binding."
- "SecKeychainStoreUnlockKeyWithPubKeyHash failed during binding."
```
