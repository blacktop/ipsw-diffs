## AMSAccountSyncNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountSyncNotificationPlugin.bundle/AMSAccountSyncNotificationPlugin`

```diff

-8.2.30.0.0
-  __TEXT.__text: 0x2788
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x17c
+8.4.21.0.0
+  __TEXT.__text: 0x1d80
+  __TEXT.__auth_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x26f
-  __TEXT.__oslogstring: 0x737
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x88
-  __TEXT.__objc_methname: 0xaf9
-  __TEXT.__objc_methtype: 0x2d5
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__cstring: 0x184
+  __TEXT.__oslogstring: 0x610
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_classname: 0x54
+  __TEXT.__objc_methname: 0x8d5
+  __TEXT.__objc_methtype: 0x296
+  __TEXT.__objc_stubs: 0x6e0
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__objc_selrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__auth_got: 0x158
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x798
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x10
+  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__objc_const: 0x310
+  __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 33
-  Symbols:   102
-  CStrings:  223
+  Functions: 21
+  Symbols:   85
+  CStrings:  173
 
Symbols:
- _AMSError
- _AMSQueryParameterKeyGUID
- _OBJC_CLASS_$_AMSSyncAccountFlagsResult
- _OBJC_CLASS_$_AMSSyncAccountFlagsTask
- _OBJC_CLASS_$_AMSTask
- _OBJC_CLASS_$_AMSURLRequestEncoder
- _OBJC_CLASS_$_AMSURLSession
- _OBJC_CLASS_$_NSDictionary
- _OBJC_METACLASS_$_AMSSyncAccountFlagsResult
- _OBJC_METACLASS_$_AMSSyncAccountFlagsTask
- _OBJC_METACLASS_$_AMSTask
- ___NSDictionary0__struct
- __os_feature_enabled_impl
- _objc_alloc
- _objc_autorelease
- _objc_retainAutorelease
- _objc_retain_x28
CStrings:
- "\x02"
- "%{public}@: [%{public}@] Successfully synced the account flags."
- "%{public}@: [%{public}@] Syncing account flags. account = %{public}@ | flags = %{public}@"
- "%{public}@: [%{public}@] The response was invalid. response = %{public}@"
- "%{public}@: [%{public}@] The server provided updated account flags."
- "@\"<AMSBagProtocol>\""
- "@\"ACAccount\""
- "@\"AMSSyncAccountFlagsResult\"16@?0^@8"
- "@\"NSDictionary\""
- "@32@0:8@16@24"
- "AMSSyncAccountFlagsResult"
- "AMSSyncAccountFlagsTask"
- "AccountFlagsV2Polus"
- "AppleMediaServices"
- "Invalid Parameter"
- "Invalid Response"
- "T@\"<AMSBagProtocol>\",&,N,V_bag"
- "T@\"ACAccount\",&,N,V_account"
- "T@\"NSDictionary\",&,N,V_accountFlags"
- "The request was successful, but the server's response was invalid."
- "URLForKey:"
- "We can't sync flags from the local account."
- "_account"
- "_accountFlags"
- "_bag"
- "account"
- "accountFlags"
- "ams_accountFlags"
- "ams_saveAccount:verifyCredentials:"
- "ams_setAccountFlags:"
- "bag"
- "dataTaskPromiseWithRequest:"
- "defaultSession"
- "deviceGUID"
- "initWithAccount:bag:"
- "initWithAccountFlags:"
- "initWithBag:"
- "isEqualToDictionary:"
- "object"
- "performSync"
- "performTaskWithBlock:"
- "requestWithMethod:bagURL:parameters:"
- "resultWithError:"
- "setAccount:"
- "setAccountFlags:"
- "setBag:"
- "setLogUUID:"
- "setRequestEncoding:"
- "sharedAccountsConfig"

```
