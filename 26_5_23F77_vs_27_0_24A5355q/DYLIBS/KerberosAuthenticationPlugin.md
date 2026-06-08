## KerberosAuthenticationPlugin

> `/System/Library/Accounts/Authentication/KerberosAuthenticationPlugin.bundle/KerberosAuthenticationPlugin`

```diff

-1036.0.0.0.0
-  __TEXT.__text: 0x1854
-  __TEXT.__auth_stubs: 0x270
+1116.0.0.0.0
+  __TEXT.__text: 0x16f0
   __TEXT.__objc_methlist: 0x1fc
   __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0x2fb
   __TEXT.__cstring: 0x22f
-  __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methname: 0x6c4
-  __TEXT.__objc_methtype: 0x422
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
-  __AUTH_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 965C56DD-1B47-3197-A24C-4DFB94E9C4C2
-  Functions: 29
-  Symbols:   67
-  CStrings:  167
+  UUID: 1BD28CB7-AF51-36B9-9D9D-4B414BABEA99
+  Functions: 27
+  Symbols:   71
+  CStrings:  57
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
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
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_authenticateAccount:password:certificate:client:completion:"
- "_presentAuthenticationDialogForAccount:completion:"
- "_promptForPasswordAndAuthenticateAccount:authAttemptsRemaining:client:completion:"
- "_useCertificate:toAuthenticateAccount:client:withCompletion:"
- "accountPropertyForKey:"
- "accountStore"
- "accountType"
- "accountTypeDescription"
- "allKeys"
- "appPermissionsForAccountType:"
- "array"
- "arrayByAddingObject:"
- "auditToken"
- "autorelease"
- "boolValue"
- "bundleForClass:"
- "bundleID"
- "class"
- "client"
- "conformsToProtocol:"
- "connection"
- "countByEnumeratingWithState:objects:count:"
- "credential"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:error:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "debugDescription"
- "description"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "errorWithDomain:code:userInfo:"
- "hash"
- "identifier"
- "isAuthenticated"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPushSupportedForAccount:"
- "localizedStringForKey:value:table:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pid"
- "release"
- "renewCredentialsForAccount:accountStore:options:completion:"
- "renewCredentialsForAccount:accountStore:reason:completion:"
- "renewalIDForAccount:"
- "renewalIDsForAccount:accountStore:options:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "saveAccount:withHandler:"
- "self"
- "setAuthenticated:"
- "setToken:"
- "stringWithFormat:"
- "superclass"
- "username"
- "v32@0:8@16@?24"
- "v40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@\"ACAccount\"16@\"ACDClient\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v44@0:8@16I24@28@?36"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?@\"ACAccount\"@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSString\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@?48"
- "verifyCredentialsForAccount:accountStore:completion:"
- "verifyCredentialsForAccount:accountStore:options:completion:"
- "verifyCredentialsForAccount:client:withHandler:"
- "zone"

```
