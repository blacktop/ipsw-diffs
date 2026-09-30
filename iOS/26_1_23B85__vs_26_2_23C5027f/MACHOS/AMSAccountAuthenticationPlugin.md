## AMSAccountAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin`

```diff

-9.1.20.2.1
-  __TEXT.__text: 0x8004
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_stubs: 0x1de0
-  __TEXT.__objc_methlist: 0x5bc
+9.2.16.0.0
+  __TEXT.__text: 0x9508
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0x1f80
+  __TEXT.__objc_methlist: 0x5d4
   __TEXT.__const: 0xca
-  __TEXT.__cstring: 0x942
+  __TEXT.__cstring: 0x9d2
   __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0x1f90
+  __TEXT.__objc_methname: 0x20da
   __TEXT.__objc_methtype: 0x884
-  __TEXT.__oslogstring: 0x14b1
-  __TEXT.__gcc_except_tab: 0x3c
+  __TEXT.__oslogstring: 0x17b8
+  __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x198
-  __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x478
-  __DATA_CONST.__cfstring: 0x920
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x4d0
+  __DATA_CONST.__cfstring: 0x9e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x808
-  __DATA.__objc_selrefs: 0x940
+  __DATA.__objc_selrefs: 0x9a0
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1CD355DB-B4E1-3BAE-AB6B-D25D338FD12D
-  Functions: 95
-  Symbols:   151
-  CStrings:  627
+  UUID: 90524663-7310-31EF-A5D7-FE138148152E
+  Functions: 100
+  Symbols:   155
+  CStrings:  662
 
Symbols:
+ _AMSAccountGrandSlamTokenIdentifierSimpleProfileAuth
+ _AMSBagKeyAuthenticateSimpleProfileURL
+ _AMSHTTPHeaderAgeAreaComplianceID
+ _OBJC_CLASS_$_AMSEligibility
+ _OBJC_CLASS_$_NSJSONSerialization
- _objc_retain_x4
CStrings:
+ ""
+ "%{public}@: [%{public}@] Processing Profile Account"
+ "%{public}@: [%{public}@] Updating the simple-profile's storefront. oldStorefront = %{public}@ | newStorefront = %{public}@"
+ "%{public}@Failed to serialize sponsor cookies to JSON. error = %{public}@"
+ "%{public}@Finished refreshing Simple Profile. account = %{publics}@ error = %{public}@"
+ "%{public}@No age area compliance ID; setting header %{public}@ to empty string"
+ "%{public}@Refreshing Simple Profile cookies for %ld accounts"
+ "%{public}@Refreshing Simple Profile. account = %{publics}@"
+ "%{public}@Set %{public}@ as value for header %{public}@"
+ "%{public}@Set sponsor cookies as JSON request body. cookieCount = %lu"
+ "%{public}@Starting an account credential verification. account = %{public}@ | simple-profile = %{public}@ | options = %{public}@"
+ "%{public}@The authentication completed with result = %{publics}@ error = %{public}@"
+ "@\"AMSPromise\"24@?0@8@\"NSError\"16"
+ "Content-Type"
+ "URL"
+ "_createUpdatedSimpleProfileAccountWithAuthenticationResult:"
+ "_refreshSimpleProfilesOnAccount:"
+ "ams_isSimpleProfile"
+ "ams_simpleProfileAccountsForiTunesAccount:"
+ "application/json"
+ "authenticateSimpleProfile"
+ "dataTaskPromiseWithRequestPromise:"
+ "dataWithJSONObject:options:error:"
+ "false"
+ "getAgeAreaComplianceId"
+ "parentAccount"
+ "setGsTokenIdentifier:"
+ "setHTTPBody:"
+ "sharedAccountsOversizeConfig"
+ "sponsorCookies"
+ "v24@?0@\"AMSURLResult\"8@\"NSError\"16"
- "%{public}@Starting an account credential verification. account = %{public}@ | options = %{public}@"

```
