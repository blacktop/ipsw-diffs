## HealthRecordsPlugin

> `/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin`

```diff

-5132.0.0.0.0
-  __TEXT.__text: 0xb195c
+5138.0.1.1.0
+  __TEXT.__text: 0xb1ef4
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_stubs: 0x13000
-  __TEXT.__objc_methlist: 0x7b74
-  __TEXT.__objc_methname: 0x1cf28
-  __TEXT.__objc_classname: 0x1bed
-  __TEXT.__objc_methtype: 0x3563
+  __TEXT.__objc_stubs: 0x130a0
+  __TEXT.__objc_methlist: 0x7bbc
+  __TEXT.__objc_methname: 0x1d11a
+  __TEXT.__objc_classname: 0x1bee
+  __TEXT.__objc_methtype: 0x3571
   __TEXT.__const: 0x1f4
-  __TEXT.__gcc_except_tab: 0x22ac
-  __TEXT.__cstring: 0xa0c5
-  __TEXT.__oslogstring: 0xeaa4
+  __TEXT.__gcc_except_tab: 0x22c0
+  __TEXT.__cstring: 0xa0b8
+  __TEXT.__oslogstring: 0xebc9
   __TEXT.__ustring: 0x7e
-  __TEXT.__unwind_info: 0x2808
+  __TEXT.__unwind_info: 0x2818
   __DATA_CONST.__auth_got: 0x6e0
   __DATA_CONST.__got: 0xef0
   __DATA_CONST.__const: 0x3828
-  __DATA_CONST.__cfstring: 0x77a0
+  __DATA_CONST.__cfstring: 0x7780
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x3a8
-  __DATA_CONST.__objc_intobj: 0x6a8
+  __DATA_CONST.__objc_intobj: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x1d8
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xea98
-  __DATA.__objc_selrefs: 0x55b8
-  __DATA.__objc_ivar: 0x714
+  __DATA.__objc_const: 0xeb20
+  __DATA.__objc_selrefs: 0x55e0
+  __DATA.__objc_ivar: 0x71c
   __DATA.__objc_data: 0x25d0
   __DATA.__data: 0x1028
   __DATA.__bss: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3380
+  Functions: 3385
   Symbols:   1088
-  CStrings:  5952
+  CStrings:  5966
 
CStrings:
+ "\x13\x12\x12"
+ "%!{(MISSING)public}@ Account %!{(MISSING)public}@: Detected a resource schema with MCAV %!{(MISSING)public}ld, which is greater than our version, skipping this schema"
+ "%!{(MISSING)public}@ Account %!{(MISSING)public}@: context may not make requests, will not run %!l(MISSING)u feature operations"
+ "%!{(MISSING)public}@ Account %!{(MISSING)public}@: context may not make requests, will not run %!l(MISSING)u schema operations"
+ "%!{(MISSING)public}@ Account %!{(MISSING)public}@: unable to run resource fetch operation for URL %!{(MISSING)public}@"
+ "@24@0:8B16B20"
+ "T@\"NSNumber\",R,C,N,V_overrideFailedAttemptsCount"
+ "T@\"NSNumber\",R,N"
+ "TB,R,N,V_accountMustLimitRequests"
+ "TB,R,N,V_mayMakeRequests"
+ "_accountMustLimitRequests"
+ "_mayMakeRequests"
+ "_overrideFailedAttemptsCount"
+ "_updateLastFailedFetchDate:overrideFailedAttemptsCount:profile:transaction:error:"
+ "_withLock_evaluateNewErrors:"
+ "accountMustLimitRequests"
+ "failedToCompleteFetchForAccount:mustLimitFutureRequests:"
+ "hrs_hasResourceFetchErrorsIndicatingRateLimitation"
+ "initWithLastFailedFetchDate:overrideFailedAttemptsCount:accountIdentifier:"
+ "initWithOneFetchSucceeded:accountMustLimitRequests:"
+ "mayMakeRequests"
+ "numFailedAttemptsToReachMaxBlockTime"
+ "overrideFailedAttemptsCount"
+ "updateAccountLastFailedFetchDate:overrideFailedAttemptsCount:identifier:profile:healthDatabase:error:"
- "\x16\x12"
- "%!{(MISSING)public}@ Account %!{(MISSING)public}@: Detected a resource schema with MCAV: %!{(MISSING)public}ld greater than our version, skipping this schema"
- "SaveQueue-%!@(MISSING)"
- "_saveQueue"
- "_updateLastFailedFetchDate:profile:transaction:error:"
- "failedToCompleteFetchForAccount:"
- "initWithLastFailedFetchDate:accountIdentifier:"
- "initWithOneFetchSucceeded:"
- "isiPad"
- "updateAccountLastFailedFetchDate:identifier:profile:healthDatabase:error:"

```
