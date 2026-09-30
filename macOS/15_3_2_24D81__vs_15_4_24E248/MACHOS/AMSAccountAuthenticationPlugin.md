## AMSAccountAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/Contents/MacOS/AMSAccountAuthenticationPlugin`

```diff

-8.2.30.0.0
-  __TEXT.__text: 0x9b14
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0x3c4
-  __TEXT.__const: 0x114
-  __TEXT.__cstring: 0xa15
-  __TEXT.__objc_classname: 0xcf
-  __TEXT.__objc_methname: 0x1e42
-  __TEXT.__objc_methtype: 0x886
-  __TEXT.__oslogstring: 0x163e
+8.4.25.1.2
+  __TEXT.__text: 0x8ec8
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_stubs: 0x1ca0
+  __TEXT.__objc_methlist: 0x5ac
+  __TEXT.__const: 0xc2
+  __TEXT.__cstring: 0x8f2
+  __TEXT.__objc_classname: 0x9b
+  __TEXT.__objc_methname: 0x1dd7
+  __TEXT.__objc_methtype: 0x884
+  __TEXT.__oslogstring: 0x1518
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__constg_swiftt: 0x48
-  __TEXT.__swift5_typeref: 0x3a
-  __TEXT.__swift5_reflstr: 0x13
-  __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1b8
-  __DATA_CONST.__auth_got: 0x198
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x528
-  __DATA_CONST.__cfstring: 0x9a0
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x4a8
+  __DATA_CONST.__cfstring: 0x920
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0xec0
-  __DATA.__objc_selrefs: 0x7b8
-  __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0x200
-  __DATA.__data: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x808
+  __DATA.__objc_selrefs: 0x8e8
+  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x180
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 77B63D31-12AA-3881-96C7-72D709E84A52
-  Functions: 120
-  Symbols:   145
-  CStrings:  640
+  UUID: 9AAD83DA-7ECC-35D9-8F99-39A2E7110C2F
+  Functions: 102
+  Symbols:   131
+  CStrings:  612
 
Symbols:
+ _OBJC_CLASS_$_AMSCertificateManager
+ _OBJC_CLASS_$_AMSPromiseSerialQueue
- _AMSQueryParameterKeyGUID
- _OBJC_CLASS_$_AMSSyncAccountFlagsResult
- _OBJC_CLASS_$_AMSSyncAccountFlagsTask
- _OBJC_METACLASS_$_AMSSyncAccountFlagsResult
- _OBJC_METACLASS_$_AMSSyncAccountFlagsTask
- __Block_copy
- __Block_release
- ___NSDictionary0__struct
- __os_feature_enabled_impl
- _objc_autorelease
- _objc_opt_self
- _objc_retainAutorelease
- _swift_allocObject
- _swift_deallocObject
- _swift_release
- _swift_retain
CStrings:
+ "%{public}@: [%@] Provisioning biometrics."
+ "@\"AMSPromiseSerialQueue\""
+ "@\"NSObject<OS_nw_activity>\""
+ "T@\"AMSPromiseSerialQueue\",R,V_authenticationQueue"
+ "T@\"NSObject<OS_nw_activity>\",&,V_activity"
+ "_activity"
+ "_expectedBiometricActionConstraint"
+ "accessControlForAccount:forSignaturePurpose:"
+ "activity"
+ "completeMetricsActivityWithPromise:"
+ "dataTaskPromiseWithRequestPromise:activity:"
+ "prepareMetricsActivity"
+ "purpose"
+ "runPromiseBlock:"
+ "setActivity:"
+ "shouldUseAccountSpecificCertificatesForAccount:"
- "%{public}@: [%@] Provisoning biometrics."
- "%{public}@: [%{public}@] Successfully synced the account flags."
- "%{public}@: [%{public}@] Syncing account flags. account = %{public}@ | flags = %{public}@"
- "%{public}@: [%{public}@] The response was invalid. response = %{public}@"
- "%{public}@: [%{public}@] The server provided updated account flags."
- "@\"AMSAccountAuthenticationPluginQueue\""
- "@\"AMSSyncAccountFlagsResult\"16@?0^@8"
- "@\"NSDictionary\""
- "@24@0:8@?16"
- "AMSAccountAuthenticationPluginQueue"
- "AMSSyncAccountFlagsResult"
- "AMSSyncAccountFlagsTask"
- "AccountFlagsV2Polus"
- "AppleMediaServices"
- "Invalid Parameter"
- "Invalid Response"
- "T@\"<AMSBagProtocol>\",&,V_bag"
- "T@\"ACAccount\",&,V_account"
- "T@\"AMSAccountAuthenticationPluginQueue\",R,V_authenticationQueue"
- "T@\"NSDictionary\",&,N,V_accountFlags"
- "The request was successful, but the server's response was invalid."
- "URLForKey:"
- "We can't sync flags from the local account."
- "_accountFlags"
- "ams_saveAccount:verifyCredentials:"
- "ams_setAccountFlags:"
- "ams_sharedAccountStore"
- "dataTaskPromiseWithRequest:"
- "dataTaskPromiseWithRequestPromise:"
- "dealloc"
- "enqueuePromiseBlock:"
- "initWithAccountFlags:"
- "isEqualToDictionary:"
- "performSync"
- "performTaskWithBlock:"
- "promiseSerialQueue"
- "setAccountFlags:"
- "setBag:"
- "sharedAccountsConfig"
- "v24@?0@8@\"NSError\"16"

```
