## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/Versions/A/AccountsDaemon`

```diff

-1123.0.0.0.0
-  __TEXT.__text: 0x89bbc
+1125.0.0.0.0
+  __TEXT.__text: 0x8a5a8
   __TEXT.__objc_methlist: 0x3cc4
   __TEXT.__const: 0xd1a
-  __TEXT.__oslogstring: 0x91ea
-  __TEXT.__cstring: 0x3e23
+  __TEXT.__oslogstring: 0x928a
+  __TEXT.__cstring: 0x3e63
   __TEXT.__gcc_except_tab: 0x24ac
   __TEXT.__swift5_typeref: 0x6d2
   __TEXT.__constg_swiftt: 0x3d4

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2940
+  __TEXT.__unwind_info: 0x2958
   __TEXT.__eh_frame: 0x1120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0xd48
-  __AUTH_CONST.__const: 0x2630
-  __AUTH_CONST.__cfstring: 0x34a0
+  __AUTH_CONST.__const: 0x2660
+  __AUTH_CONST.__cfstring: 0x34c0
   __AUTH_CONST.__objc_const: 0x4c50
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2499
-  Symbols:   4461
-  CStrings:  1200
+  Functions: 2504
+  Symbols:   4466
+  CStrings:  1203
 
Symbols:
+ __76-[ACDAccountStoreFilter enabledDataclassesForAccountWithIdentifier:handler:]_block_invoke
+ __80-[ACDAccountStoreFilter provisionedDataclassesForAccountWithIdentifier:handler:]_block_invoke
+ ___76-[ACDAccountStoreFilter enabledDataclassesForAccountWithIdentifier:handler:]_block_invoke
+ ___80-[ACDAccountStoreFilter provisionedDataclassesForAccountWithIdentifier:handler:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e31_v24?0"ACAccount"8"NSError"16l
CStrings:
+ "\"Client %@ is not allowed to access enabled dataclasses for account %@.\""
+ "\"Client %@ is not allowed to access provisioned dataclasses for account %@.\""
+ "\"Posting ACDAccountStoreDidChangeNotification: %{public}@ %{public}@ account: %{private}@ [%{private}@], notifying:%{bool}d\""
+ "You are not allowed to read the authorization model."
- "Posting ACDAccountStoreDidChangeNotification: %{public}@ %{public}@ account: %{private}@ [%{private}@], notifying:%{bool}d"
```
