## ESAccountAuthenticator

> `/System/Library/Accounts/Authentication/ESAccountAuthenticator.bundle/ESAccountAuthenticator`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-2076.0.0.0.0
-  __TEXT.__text: 0x6a68
+2078.0.0.0.0
+  __TEXT.__text: 0x85c4
   __TEXT.__objc_methlist: 0x31c
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x110
-  __TEXT.__cstring: 0x57c
-  __TEXT.__oslogstring: 0xd40
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__const: 0xa0
+  __TEXT.__gcc_except_tab: 0x138
+  __TEXT.__cstring: 0x712
+  __TEXT.__oslogstring: 0x117c
+  __TEXT.__unwind_info: 0x160
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__const: 0x370
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x598
+  __DATA_CONST.__objc_selrefs: 0x5e8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0x2c0
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x2e0
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x120
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 64
-  Symbols:   156
-  CStrings:  107
+  Functions: 79
+  Symbols:   170
+  CStrings:  146
 
Symbols:
+ _OAuthRefresh4XXIsTerminal
+ _OAuthRefreshErrorNameIsUserActionRequired
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSSet
+ __NSConcreteGlobalBlock
+ _kESExchangeOAuthRefresh5XXResetCount
+ _kESExchangeOAuthRefreshFailureCount
+ _kESExchangeOAuthRefreshFirstFailureDate
+ _objc_enumerationMutation
+ _objc_release_x1
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ " "
+ "%lu"
+ "OAuthRefreshGrace: 200-recovery save failed for account %@; stale grace state may persist. err=%@"
+ "OAuthRefreshGrace: 5XX reset status=%ld 5xxResetCount=%lu"
+ "OAuthRefreshGrace: entering grace status=%ld errorName=%{public}@ error_codes=%{public}@ count=1 elapsed=0"
+ "OAuthRefreshGrace: in-grace 4XX status=%ld errorName=%{public}@ error_codes=%{public}@ count=%lu elapsed=%.0f"
+ "OAuthRefreshGrace: in-grace 5XX/429 status=%ld error_codes=%{public}@ count=%lu elapsed=%.0f"
+ "OAuthRefreshGrace: recovered status=200 elapsed=%.0f count=%lu 5xxResetCount=%lu"
+ "OAuthRefreshGrace: short-circuit (backoff) count=%lu elapsed=%.0f"
+ "OAuthRefreshGrace: short-circuit (in-flight) inFlightCount=%lu"
+ "OAuthRefreshGrace: terminal (4XX) status=%ld errorName=%{public}@ error_codes=%{public}@"
+ "OAuthRefreshGrace: terminal (5XX-cap) status=%ld error_codes=%{public}@ elapsed=%.0f 5xxResetCount=%lu"
+ "OAuthRefreshGrace: terminal (final 4XX) status=%ld errorName=%{public}@ error_codes=%{public}@ elapsed=%.0f count=%lu 5xxResetCount=%lu"
+ "Received an error. errorName=%{public}@"
+ "Received an invalid_grant error. errorName=%{public}@"
+ "Refreshing OAuth Token failed (bypass arm). status=%ld errorName=%{public}@ errorDomain=%{public}@ errorCode=%ld"
+ "access_denied"
+ "account_unusable"
+ "authorization_pending"
+ "bad_token"
+ "consent_required"
+ "error_codes"
+ "expired_token"
+ "i"
+ "insufficient_claims"
+ "interaction_required"
+ "invalid_client"
+ "invalid_request"
+ "invalid_resource"
+ "invalid_scope"
+ "invalid_token"
+ "login_required"
+ "malformed"
+ "none"
+ "other"
+ "server_error"
+ "slow_down"
+ "temporarily_unavailable"
+ "unauthorized_client"
+ "unsupported_grant_type"
+ "unsupported_response_type"
+ "unsupported_token_type"
- "Received an Error: refreshing OAuth Token failed with Error %@"
- "Received an error. %@ %@"
- "Received an invalid_grant error. %@ %@"
```
