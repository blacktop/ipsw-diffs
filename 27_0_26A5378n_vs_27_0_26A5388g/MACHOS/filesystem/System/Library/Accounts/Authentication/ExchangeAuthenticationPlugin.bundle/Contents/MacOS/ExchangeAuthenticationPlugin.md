## ExchangeAuthenticationPlugin

> `/System/Library/Accounts/Authentication/ExchangeAuthenticationPlugin.bundle/Contents/MacOS/ExchangeAuthenticationPlugin`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-842.0.0.0.0
-  __TEXT.__text: 0x7d34
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_stubs: 0x1300
-  __TEXT.__objc_methlist: 0x44c
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x44c
-  __TEXT.__oslogstring: 0xece
-  __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0x1376
-  __TEXT.__objc_methtype: 0x63b
-  __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__unwind_info: 0x1b0
-  __DATA_CONST.__const: 0x360
-  __DATA_CONST.__cfstring: 0x240
-  __DATA_CONST.__objc_classlist: 0x18
+844.0.0.0.0
+  __TEXT.__text: 0x8284
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x1400
+  __TEXT.__objc_methlist: 0x48c
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x4b5
+  __TEXT.__oslogstring: 0x1006
+  __TEXT.__objc_classname: 0xd8
+  __TEXT.__objc_methname: 0x14c2
+  __TEXT.__objc_methtype: 0x673
+  __TEXT.__gcc_except_tab: 0xec
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__const: 0x390
+  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0x298
-  __DATA.__objc_const: 0xc80
-  __DATA.__objc_selrefs: 0x5e0
+  __DATA.__objc_const: 0xd10
+  __DATA.__objc_selrefs: 0x620
   __DATA.__objc_ivar: 0x30
-  __DATA.__objc_data: 0xf0
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x180
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 168
-  Symbols:   135
-  CStrings:  360
+  Functions: 176
+  Symbols:   138
+  CStrings:  380
 
Symbols:
+ _OBJC_CLASS_$_ExchangeCredentialRenewalPolicy
+ _OBJC_METACLASS_$_ExchangeCredentialRenewalPolicy
+ _dispatch_time
CStrings:
+ "B24@0:8B16B20"
+ "B24@0:8q16"
+ "B28@0:8@16B24"
+ "B28@0:8B16B20B24"
+ "Couldn't renew credential (deferrable failure); not invalidating. Renewal result %{public}@"
+ "ExchangeCredentialRenewalPolicy"
+ "OAuth account has no refresh token (confirmed via store re-read); requesting reauthentication (shouldAvoidUI=%hhd)."
+ "OAuth renewal: no refresh token on the passed snapshot, but the fresh store read %{public}@ — deferring instead of invalidating."
+ "OpenID rediscovery timed out; proceeding without token endpoint."
+ "Token request URI missing for OAuth account; rediscovering via OpenID metadata before refresh."
+ "freshCredentialConfirmsNoRefreshToken:hasRefreshToken:"
+ "interaction_required"
+ "invalid_token"
+ "isOAuthAccountWithRefreshTokenPresent:oauthSupported:oauthVersionV2:"
+ "isServerCredentialRejection:"
+ "isServerTransientStatus:"
+ "isTransientNetworkError:"
+ "masterCredentialForAccountIdentifier:"
+ "setTimeoutIntervalForRequest:"
+ "setTimeoutIntervalForResource:"
+ "shouldInvalidateForFailedRenewalResponse:shouldAvoidUI:"
+ "still has a refresh token (stale snapshot)"
+ "was nil (keychain locked?)"
- "Couldn't renew credential with networking error, calling completion with renewal result %{public}@"
- "Couldn't renew credential without UI, calling completion with renewal result %{public}@"
- "_isTransientNetworkError:"
```
