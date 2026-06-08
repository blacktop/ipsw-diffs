## AppleIDSSOAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AppleIDSSOAuthenticationPlugin.bundle/AppleIDSSOAuthenticationPlugin`

```diff

-110.0.0.0.0
-  __TEXT.__text: 0x1020
-  __TEXT.__auth_stubs: 0x170
+112.1.0.0.0
+  __TEXT.__text: 0xebc
   __TEXT.__objc_methlist: 0x214
   __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0x189
-  __TEXT.__cstring: 0x71
+  __TEXT.__cstring: 0x73
   __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0x6d6
-  __TEXT.__objc_methtype: 0x427
-  __TEXT.__objc_stubs: 0x520
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x248
-  __AUTH_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x278
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49913A9E-82CF-3202-A743-EF98A6484A6A
-  Functions: 19
-  Symbols:   44
-  CStrings:  130
+  UUID: 226695F3-1E81-3924-978C-10B6F5F65635
+  Functions: 17
+  Symbols:   49
+  CStrings:  15
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"ACAccountCredential\"32@0:8@\"ACAccount\"16@\"ACDClient\"24"
- "@\"ACAccountCredential\"40@0:8@\"ACAccount\"16@\"ACDClient\"24^@32"
- "@\"ACAccountCredential\"48@0:8@\"ACAccount\"16@\"ACDClient\"24@\"ACDAccountStore\"32^@40"
- "@\"AKAppleIDAuthenticationController\""
- "@\"NSArray\"40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32"
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"ACAccount\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32^@40"
- "ACDAccountAuthenticationPlugin"
- "AppleIDSSOAuthenticationPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"ACAccount\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_attemptInteractiveCredentialRenewalForAccount:store:options:completion:"
- "_attemptSilentCredentialRenewalForAccount:store:options:completion:"
- "_authController"
- "_setPassword:"
- "_setProxiedAppBundleID:"
- "_setProxiedAppName:"
- "_setProxyingForApp:"
- "_silentAuthContextForAccount:rawPassword:store:options:"
- "_standardAuthContextForAccount:store:options:"
- "aida_alternateDSID"
- "aida_dsid"
- "aida_iCloudAccountMatchingAppleIDAuthAccount:"
- "authenticateWithContext:completion:"
- "autorelease"
- "boolValue"
- "bundleID"
- "class"
- "client"
- "code"
- "conformsToProtocol:"
- "count"
- "credential"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:error:"
- "credentialItemForKey:"
- "debugDescription"
- "description"
- "dictionaryWithObject:forKey:"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "domain"
- "errorWithDomain:code:userInfo:"
- "hasEntitlement:"
- "hash"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPushSupportedForAccount:"
- "name"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "password"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "renewCredentialsForAccount:accountStore:options:completion:"
- "renewCredentialsForAccount:accountStore:reason:completion:"
- "renewalIDForAccount:"
- "renewalIDsForAccount:accountStore:options:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAltDSID:"
- "setAuthenticationType:"
- "setDSID:"
- "setIsUsernameEditable:"
- "setPassword:"
- "setServiceIdentifiers:"
- "setServiceType:"
- "setShouldUpdatePersistentServiceTokens:"
- "setUsername:"
- "superclass"
- "token"
- "username"
- "v16@0:8"
- "v40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@\"ACAccount\"16@\"ACDClient\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?@\"ACAccount\"@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSString\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "verifyCredentialsForAccount:accountStore:completion:"
- "verifyCredentialsForAccount:accountStore:options:completion:"
- "verifyCredentialsForAccount:client:withHandler:"
- "zone"

```
