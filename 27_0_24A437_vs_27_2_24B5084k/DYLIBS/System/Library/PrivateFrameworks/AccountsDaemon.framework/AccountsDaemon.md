## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`

```diff

-1123.0.0.0.0
-  __TEXT.__text: 0x80934
+1125.0.0.0.0
+  __TEXT.__text: 0x8122c
   __TEXT.__objc_methlist: 0x3c8c
   __TEXT.__const: 0xd0a
-  __TEXT.__oslogstring: 0x90ca
-  __TEXT.__cstring: 0x3dc3
+  __TEXT.__oslogstring: 0x916a
+  __TEXT.__cstring: 0x3e03
   __TEXT.__gcc_except_tab: 0x2504
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__swift5_typeref: 0x6d2

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2860
+  __TEXT.__unwind_info: 0x2870
   __TEXT.__eh_frame: 0x1120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1750
+  __DATA_CONST.__const: 0x1778
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__got: 0xd80
   __AUTH_CONST.__const: 0x1080
-  __AUTH_CONST.__cfstring: 0x3300
+  __AUTH_CONST.__cfstring: 0x3320
   __AUTH_CONST.__objc_const: 0x4bb8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2423
-  Symbols:   4392
-  CStrings:  1187
+  Functions: 2428
+  Symbols:   4395
+  CStrings:  1190
 
Symbols:
+ ___76-[ACDAccountStoreFilter enabledDataclassesForAccountWithIdentifier:handler:]_block_invoke
+ ___80-[ACDAccountStoreFilter provisionedDataclassesForAccountWithIdentifier:handler:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e31_v24?0"ACAccount"8"NSError"16ls32l8s40l8s48l8
CStrings:
+ "\"Client %@ is not allowed to access enabled dataclasses for account %@.\""
+ "\"Client %@ is not allowed to access provisioned dataclasses for account %@.\""
+ "\"Posting ACDAccountStoreDidChangeNotification: %{public}@ %{public}@ account: %{private}@ [%{private}@], notifying:%{bool}d\""
+ "You are not allowed to read the authorization model."
- "Posting ACDAccountStoreDidChangeNotification: %{public}@ %{public}@ account: %{private}@ [%{private}@], notifying:%{bool}d"
```
