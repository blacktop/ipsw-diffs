## storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

-814.4.21.0.0
-  __TEXT.__text: 0x2f7ce4
+814.4.23.0.0
+  __TEXT.__text: 0x2f8940
   __TEXT.__auth_stubs: 0x3560
-  __TEXT.__objc_stubs: 0xd0c0
+  __TEXT.__objc_stubs: 0xd040
   __TEXT.__objc_methlist: 0x85c4
-  __TEXT.__const: 0x1ff90
-  __TEXT.__cstring: 0x12ba0
-  __TEXT.__oslogstring: 0xd0fa
-  __TEXT.__objc_classname: 0x11fc
-  __TEXT.__objc_methname: 0x12fe7
+  __TEXT.__const: 0x1ffc0
+  __TEXT.__cstring: 0x12d70
+  __TEXT.__oslogstring: 0xcefa
+  __TEXT.__objc_classname: 0x11fe
+  __TEXT.__objc_methname: 0x12f9f
   __TEXT.__objc_methtype: 0x36b2
-  __TEXT.__gcc_except_tab: 0x249c
+  __TEXT.__gcc_except_tab: 0x2384
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2f64

   __TEXT.__swift5_reflstr: 0x17c5
   __TEXT.__swift5_fieldmd: 0x2b40
   __TEXT.__swift5_builtin: 0x208
-  __TEXT.__swift5_assocty: 0x5e8
-  __TEXT.__swift5_proto: 0x9f8
+  __TEXT.__swift5_assocty: 0x600
+  __TEXT.__swift5_proto: 0x9fc
   __TEXT.__swift5_types: 0x3d8
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_capture: 0x1e2c
-  __TEXT.__swift_as_entry: 0x418
-  __TEXT.__swift_as_ret: 0x564
+  __TEXT.__swift5_capture: 0x1e48
+  __TEXT.__swift_as_entry: 0x42c
+  __TEXT.__swift_as_ret: 0x578
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x8788
-  __TEXT.__eh_frame: 0xfec0
+  __TEXT.__unwind_info: 0x8848
+  __TEXT.__eh_frame: 0x10280
   __DATA_CONST.__auth_got: 0x1ac0
-  __DATA_CONST.__got: 0xcb8
-  __DATA_CONST.__auth_ptr: 0xcc0
-  __DATA_CONST.__const: 0x19580
-  __DATA_CONST.__cfstring: 0x6880
+  __DATA_CONST.__got: 0xca0
+  __DATA_CONST.__auth_ptr: 0xae8
+  __DATA_CONST.__const: 0x19498
+  __DATA_CONST.__cfstring: 0x6860
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x320

   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x1c318
-  __DATA.__objc_selrefs: 0x4b58
+  __DATA.__objc_selrefs: 0x4b38
   __DATA.__objc_ivar: 0x700
   __DATA.__objc_data: 0x4f98
-  __DATA.__data: 0x7b18
-  __DATA.__bss: 0x14718
-  __DATA.__common: 0xdc0
+  __DATA.__data: 0x7b40
+  __DATA.__bss: 0x14798
+  __DATA.__common: 0xdb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12008
-  Symbols:   1499
-  CStrings:  6814
+  Functions: 12037
+  Symbols:   1497
+  CStrings:  6807
 
Symbols:
+ _$ss5ErrorPsSYRzs17FixedWidthInteger8RawValueSYRpzrlE5_codeSivg
- _$s10Foundation15_BridgedNSErrorPAAE7_domainSSvg
- _OBJC_CLASS_$_AMSAuthenticateTask
- _OBJC_CLASS_$_AMSBinaryPromise
CStrings:
+ "01:01:27"
+ "Authenticating with production account for "
+ "Mar  3 2025"
+ "No TestFlight account in beta account store. Attempting silent testflight auth with prod account."
+ "No active account for silent auth"
+ "No prod account for silent testflight auth"
+ "SKAccountService"
+ "Starting authentication"
+ "Testflight account already primed"
+ "[%{public}@] Not caching app transaction for %{public}@ because the account token is empty."
+ "_performWithAccount:originatingStorefront:buyParams:"
+ "primeTestFlightAccountWithClient:logKey:completionHandler:"
+ "storekitd/InAppTransactionTask+Swift.swift"
+ "v40@0:8@\"_TtC9storekitd6Client\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "21:37:20"
- "AccountService"
- "Feb 21 2025"
- "SK Silent Auth"
- "[%{public}@] Attempting to use existing account."
- "[%{public}@] No TestFlight account in beta account store. Attempting silent auth with prod account."
- "[%{public}@] No account after silent auth: %{public}@."
- "[%{public}@] No account for %{public}@: %{public}@"
- "[%{public}@] No info provided."
- "[%{public}@] Sending authentication request for %{public}@"
- "[%{public}@] Silent auth successful."
- "[%{public}@] TF account not detected."
- "[%{public}s] Error authenticating request: %@"
- "[%{public}s] Finished authenticating request for %{private}@"
- "[%{public}s] Starting authentication request for %{private}s"
- "_authenticateWithAccountInfo:error:"
- "_performWithBuyParams:"
- "_silentAuthWithClientInfo:account:logKey:"
- "ams_localiTunesAccountForAccountMediaType:"
- "finishWithSuccess"
- "performAuthentication"

```
