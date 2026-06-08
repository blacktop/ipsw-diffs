## CloudKitAuthenticationPlugin

> `/System/Library/Accounts/Authentication/CloudKitAuthenticationPlugin.bundle/CloudKitAuthenticationPlugin`

```diff

-2360.120.2.0.0
-  __TEXT.__text: 0x680
-  __TEXT.__auth_stubs: 0x130
+2710.108.20.0.0
+  __TEXT.__text: 0x644
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0x58
   __TEXT.__oslogstring: 0x183
   __TEXT.__cstring: 0x33
   __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methname: 0x4c3
-  __TEXT.__objc_methtype: 0x3f4
-  __TEXT.__objc_stubs: 0x1c0
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x178
-  __AUTH_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18C1ACBB-E270-325A-9A96-5EACDFB60F29
+  UUID: A73B0CA0-50D4-3DC9-B27F-2C50978345B6
   Functions: 5
-  Symbols:   36
-  CStrings:  97
+  Symbols:   34
+  CStrings:  10
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
- "#16@0:8"
- "@\"ACAccountCredential\"32@0:8@\"ACAccount\"16@\"ACDClient\"24"
- "@\"ACAccountCredential\"40@0:8@\"ACAccount\"16@\"ACDClient\"24^@32"
- "@\"ACAccountCredential\"48@0:8@\"ACAccount\"16@\"ACDClient\"24@\"ACDAccountStore\"32^@40"
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
- "@48@0:8@16@24@32^@40"
- "ACDAccountAuthenticationPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"ACAccount\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "CloudKitAuthenticationPlugin"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accountAccessIsAllowedForAccount:client:"
- "aa_isSuspended"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:error:"
- "debugDescription"
- "description"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "errorWithDomain:code:userInfo:"
- "hasEntitlement:"
- "hash"
- "identifier"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPushSupportedForAccount:"
- "parentAccount"
- "passwordForServiceName:username:accessGroup:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "removePasswordForService:username:accessGroup:"
- "renewCredentialsForAccount:accountStore:options:completion:"
- "renewCredentialsForAccount:accountStore:reason:completion:"
- "renewalIDForAccount:"
- "renewalIDsForAccount:accountStore:options:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setCredential:"
- "setCredentialForAccount:error:"
- "setToken:"
- "superclass"
- "supportsAccountType:"
- "username"
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
