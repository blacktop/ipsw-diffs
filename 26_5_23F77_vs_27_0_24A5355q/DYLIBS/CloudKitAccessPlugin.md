## CloudKitAccessPlugin

> `/System/Library/Accounts/Access/CloudKitAccessPlugin.bundle/CloudKitAccessPlugin`

```diff

-2360.120.2.0.0
-  __TEXT.__text: 0x1658
-  __TEXT.__auth_stubs: 0x230
+2710.108.20.0.0
+  __TEXT.__text: 0x1558
   __TEXT.__objc_methlist: 0x1d4
   __TEXT.__const: 0x68
   __TEXT.__oslogstring: 0x354
+  __TEXT.__cstring: 0x2
   __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x5c9
-  __TEXT.__objc_methtype: 0x22d
-  __TEXT.__objc_stubs: 0x460
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7723D681-2D86-35A0-BFD1-9AD139DD5DC8
+  UUID: 3007AA6B-D354-3C49-A62D-47B4C8428755
   Functions: 9
-  Symbols:   52
-  CStrings:  109
+  Symbols:   53
+  CStrings:  14
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x26
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"ACAccountStore\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACDAccountAccessPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "CloudKitAccessPlugin"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"CKXPCConnection\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_ckAccountInStore:"
- "_haveAccountsOfType:withStore:"
- "_store"
- "aa_primaryAppleAccount"
- "accountsDidGrantAccessToBundleID:containerIdentifiers:"
- "accountsDidRevokeAccessToBundleID:containerIdentifiers:"
- "accountsWithAccountTypeIdentifier:"
- "addObject:"
- "allAuthorizationsForAccountType:"
- "allObjects"
- "arrayWithObjects:count:"
- "authorizationForClient:accountType:"
- "authorizationManager"
- "authorizeAccessToAccountsOfType:forClient:store:completion:"
- "autorelease"
- "bundleID"
- "ck_cloudKitAccount"
- "class"
- "client"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "description"
- "errorWithDomain:code:userInfo:"
- "grantedPermissions"
- "handleAccessRequestToAccountsOfType:forClient:withOptions:store:allowUserInteraction:completion:"
- "hasEntitlement:"
- "hash"
- "identifier"
- "initForClient:"
- "isEqual:"
- "isEqualToString:"
- "isGranted"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "mutableCopy"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processScopedDaemonProxy"
- "release"
- "removeAuthorizationForClient:accountType:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "revokeAccessToAccountsOfType:forClient:store:completion:"
- "revokeAllAccessToAccountsOfType:store:withCompletion:"
- "self"
- "setAuthorization:forClient:onAccountType:"
- "setGrantedPermissions:"
- "setIsGranted:"
- "sharedXPCConnection"
- "superclass"
- "supportsAccountTypeWithIdentifier:"
- "v16@0:8"
- "v40@0:8@\"ACAccountType\"16@\"ACDAccountStore\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"ACAccountType\"16@\"ACDClient\"24@\"ACDAccountStore\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v60@0:8@\"ACAccountType\"16@\"ACDClient\"24@\"NSDictionary\"32@\"ACDAccountStore\"40B48@?<v@?B@\"NSError\">52"
- "v60@0:8@16@24@32@40B48@?52"
- "zone"

```
