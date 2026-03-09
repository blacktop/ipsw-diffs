## securityd

> `/usr/libexec/securityd`

```diff

-61901.100.286.0.0
-  __TEXT.__text: 0x27d474
-  __TEXT.__auth_stubs: 0x4210
-  __TEXT.__objc_stubs: 0x1cc60
-  __TEXT.__objc_methlist: 0x15670
+61901.102.2.0.0
+  __TEXT.__text: 0x27db40
+  __TEXT.__auth_stubs: 0x4200
+  __TEXT.__objc_stubs: 0x1cd20
+  __TEXT.__objc_methlist: 0x156e0
   __TEXT.__const: 0x919
-  __TEXT.__cstring: 0x214d6
-  __TEXT.__objc_methname: 0x2cd98
-  __TEXT.__oslogstring: 0x2e8ea
+  __TEXT.__cstring: 0x2152c
+  __TEXT.__objc_methname: 0x2ce78
+  __TEXT.__oslogstring: 0x2eb44
   __TEXT.__swift5_typeref: 0x378
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x2555

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb464
+  __TEXT.__gcc_except_tab: 0xb494
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6ea8
+  __TEXT.__unwind_info: 0x6ea0
   __TEXT.__eh_frame: 0xa58
-  __DATA_CONST.__auth_got: 0x2118
+  __DATA_CONST.__auth_got: 0x2110
   __DATA_CONST.__got: 0x1388
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x14548
-  __DATA_CONST.__cfstring: 0x1bb40
+  __DATA_CONST.__const: 0x14528
+  __DATA_CONST.__cfstring: 0x1bbc0
   __DATA_CONST.__objc_classlist: 0x8e0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x808
-  __DATA_CONST.__objc_intobj: 0x1320
+  __DATA_CONST.__objc_intobj: 0x1350
   __DATA_CONST.__objc_arraydata: 0x400
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x23030
-  __DATA.__objc_selrefs: 0x9488
-  __DATA.__objc_ivar: 0x1a50
+  __DATA.__objc_const: 0x230f0
+  __DATA.__objc_selrefs: 0x94b8
+  __DATA.__objc_ivar: 0x1a60
   __DATA.__objc_data: 0x5bb8
   __DATA.__data: 0x3098
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0xe98
+  __DATA.__bss: 0xe88
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3AB49FF8-77B8-3519-B435-FDEB8883440D
-  Functions: 9743
-  Symbols:   1858
-  CStrings:  19892
+  UUID: B471DDE0-2B71-3D6E-AC6F-DEA6F4413666
+  Functions: 9752
+  Symbols:   1857
+  CStrings:  19917
 
Symbols:
- _CFErrorGetTypeID
CStrings:
+ "@\"NSMutableDictionary\"8@?0"
+ "CloudKit tells us of an AuthTokenError, need to recheck CK Account Status"
+ "CloudKit told us of an AuthTokenError, we'll try to re-fetch the current account state"
+ "Failed zone creation due to missing auth token, need to recheck CK Account Status and potentially re-auth"
+ "Failed zone deletion due to missing auth token, need to recheck CK Account Status and potentially re-auth"
+ "Failed zone subscription due to missing auth token, need to recheck CK Account Status and potentially re-auth"
+ "Received notice that we are not authenticated: %@"
+ "Rechecking CK Acct status post-fetch"
+ "TB,V_authTokenError"
+ "TB,V_authTokenFailure"
+ "_authTokenError"
+ "_authTokenFailure"
+ "authTokenError"
+ "authTokenFailure"
+ "isCKServerAuthTokenError"
+ "octagon: after passcode cahnge, failed to clear last escrow repair attempt: %@"
+ "post-fetch-acct-recheck"
+ "recheck-ck-acct-status"
+ "recheck_ck_account_status"
+ "recheck_ck_acct_status"
+ "sendEventLazy:builder:"
+ "setAuthTokenError:"
+ "setAuthTokenFailure:"
- "com.apple.security.SecItemAttrLogger"
- "failed to clear last escrow repair attempt: %@"

```
