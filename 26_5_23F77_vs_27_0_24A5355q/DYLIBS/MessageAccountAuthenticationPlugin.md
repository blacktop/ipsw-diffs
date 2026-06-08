## MessageAccountAuthenticationPlugin

> `/System/Library/Accounts/Authentication/MessageAccountAuthenticationPlugin.bundle/MessageAccountAuthenticationPlugin`

```diff

-3864.600.51.2.1
-  __TEXT.__text: 0x205c
-  __TEXT.__auth_stubs: 0x2a0
+3891.100.17.2.4
+  __TEXT.__text: 0x1efc
   __TEXT.__objc_methlist: 0x2c4
-  __TEXT.__gcc_except_tab: 0x490
+  __TEXT.__gcc_except_tab: 0x43c
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0xa3
   __TEXT.__cstring: 0x2ce
   __TEXT.__ustring: 0x56
   __TEXT.__unwind_info: 0x180
-  __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0x9a5
-  __TEXT.__objc_methtype: 0x43f
-  __TEXT.__objc_stubs: 0x900
-  __DATA_CONST.__got: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x338
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0x310
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7205D446-83E7-38EF-8E0E-85EB83BE2063
+  UUID: AEAF8678-AA72-3337-A8E7-C0A92E0676DA
   Functions: 27
-  Symbols:   85
-  CStrings:  226
+  Symbols:   86
+  CStrings:  76
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
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
- "B32@0:8@16^@24"
- "I16@0:8"
- "MessageAccountAuthenticationPlugin"
- "MessageAccountCredentialMigration"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^v16@0:8"
- "^{_NSZone=}16@0:8"
- "_bundleIdentifiersAllowedToPromptForAccount:"
- "_clientIsEntitled:"
- "_logWithAccount:level:reason:message:"
- "_passwordPromptMessageWithAccount:"
- "_passwordPromptTitleWithCredential:"
- "_showPasswordPromptWithAccount:completionBlock:"
- "_verifyAccount:error:"
- "accountClassForPersistentAccount:error:"
- "accountDescription"
- "accountIsValid"
- "accountProperties"
- "accountType"
- "accountWithPersistentAccount:error:"
- "addObject:"
- "appendFormat:"
- "appendString:"
- "arrayWithObjects:"
- "autorelease"
- "boolValue"
- "canReceiveNewMailNotifications"
- "class"
- "client"
- "conformsToProtocol:"
- "copy"
- "credential"
- "credentialForAccount:client:"
- "credentialForAccount:client:error:"
- "credentialForAccount:client:store:error:"
- "credentialForAccount:clientID:error:"
- "debugDescription"
- "defaultPortNumber"
- "defaultSecurePortNumber"
- "description"
- "dictionary"
- "discoverPropertiesForAccount:accountStore:options:completion:"
- "displayName"
- "displayedAccountTypeString"
- "error"
- "errorWithDomain:code:userInfo:"
- "fetchTokensIfNecessary:"
- "hasEntitlement:"
- "hash"
- "hostname"
- "identifier"
- "initWithFormat:arguments:"
- "initWithPerformsValidationInBackground:"
- "intValue"
- "invoke"
- "isAuthenticated"
- "isCommonPortNumber:"
- "isEnabledForDataclass:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPushSupportedForAccount:"
- "legacyKeychainProtocol"
- "length"
- "mf_accountClass"
- "mf_hostname"
- "mf_isMissingAccountCredentialError"
- "mf_legacyKeychainProtocol"
- "mf_legacyPasswordFromKeychain"
- "mf_legacyPortNumberForKeychain"
- "mf_migrateCredentialsIfNecessaryWithAccountCredential:"
- "mf_removeLegacyPasswordInKeychain"
- "mf_usesSSL"
- "migrateCredentialsIfNecessaryWithPersistentAccount:credential:"
- "mutableCopy"
- "objectForKeyedSubscript:"
- "password"
- "passwordForHost:username:port:keychainProtocol:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentAccount"
- "release"
- "removePasswordForHost:username:port:keychainProtocol:"
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
- "setCredential:"
- "setCredentialForAccount:"
- "setObject:forKeyedSubscript:"
- "setPassword:"
- "stringWithFormat:"
- "superclass"
- "username"
- "usesSSL"
- "v16@0:8"
- "v32@0:8@16@?24"
- "v40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@\"ACAccount\"16@\"ACDClient\"24@?<v@?@\"ACAccount\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v44@0:8@16C24@28@36"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?@\"ACAccount\"@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSDictionary\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@\"ACAccount\"16@\"ACDAccountStore\"24@\"NSString\"32@?<v@?q@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "validateAccountWithoutFallbacks:"
- "validationInvocation"
- "verifyCredentialsForAccount:accountStore:completion:"
- "verifyCredentialsForAccount:accountStore:options:completion:"
- "verifyCredentialsForAccount:client:withHandler:"
- "zone"

```
