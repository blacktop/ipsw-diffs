## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`

```diff

-  __TEXT.__text: 0x80018
+  __TEXT.__text: 0x806a8
   __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_methlist: 0x3c4c
+  __TEXT.__objc_methlist: 0x3c74
   __TEXT.__const: 0xc2a
-  __TEXT.__oslogstring: 0x89ea
-  __TEXT.__cstring: 0x3b43
-  __TEXT.__gcc_except_tab: 0x25b4
+  __TEXT.__oslogstring: 0x8a5a
+  __TEXT.__cstring: 0x3b73
+  __TEXT.__gcc_except_tab: 0x25d8
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__swift5_typeref: 0x5e2
   __TEXT.__constg_swiftt: 0x384

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1db8
+  __TEXT.__unwind_info: 0x1df8
   __TEXT.__eh_frame: 0x9b8
   __TEXT.__objc_classname: 0x739
-  __TEXT.__objc_methname: 0xb6e9
-  __TEXT.__objc_methtype: 0x2649
-  __TEXT.__objc_stubs: 0x9380
-  __DATA_CONST.__got: 0xd68
-  __DATA_CONST.__const: 0x16b8
+  __TEXT.__objc_methname: 0xb759
+  __TEXT.__objc_methtype: 0x2589
+  __TEXT.__objc_stubs: 0x93a0
+  __DATA_CONST.__got: 0xd70
+  __DATA_CONST.__const: 0x1728
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29c8
+  __DATA_CONST.__objc_selrefs: 0x29e0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH_CONST.__const: 0xc50
+  __AUTH_CONST.__const: 0xc70
   __AUTH_CONST.__cfstring: 0x32c0
-  __AUTH_CONST.__objc_const: 0x4af8
+  __AUTH_CONST.__objc_const: 0x4b28
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x368
-  __DATA.__objc_ivar: 0x2bc
+  __DATA.__objc_ivar: 0x2c0
   __DATA.__data: 0x7f0
   __DATA.__bss: 0x880
   __DATA_DIRTY.__objc_data: 0xf70

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2320
-  Symbols:   7326
-  CStrings:  3516
+  Functions: 2332
+  Symbols:   7368
+  CStrings:  3525
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[ACDAccountStore allCredentialItems]
+ -[ACDAccountStore credentialItemForAccount:serviceName:]
+ -[ACDAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]
+ -[ACDAccountStore triggerCredentialItemCleanupWithCompletion:]
+ -[ACDAccountStoreFilter setCredentialItemCleanupVolatilityDuration:withCompletion:]
+ -[ACDAccountStoreFilter triggerCredentialItemCleanupWithCompletion:]
+ -[ACDKeychainCleanupActivity accountStore]
+ -[ACDKeychainCleanupActivity removeExpiredCredentials]
+ -[ACDKeychainCleanupActivity setAccountStore:]
+ -[ACDKeychainCleanupActivity setVolatilityDuration:]
+ -[ACDKeychainCleanupActivity volatilityDuration]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table108
+ GCC_except_table113
+ GCC_except_table120
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table161
+ GCC_except_table191
+ GCC_except_table205
+ GCC_except_table210
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table328
+ _OBJC_IVAR_$_ACDKeychainCleanupActivity._volatilityDuration
+ __OBJC_$_PROP_LIST_ACDKeychainCleanupActivity
+ ___37-[ACDAccountStore allCredentialItems]_block_invoke
+ ___54-[ACDKeychainCleanupActivity removeExpiredCredentials]_block_invoke
+ ___56-[ACDAccountStore credentialItemForAccount:serviceName:]_block_invoke
+ ___block_descriptor_32_e27_v24?0"NSURL"8"NSError"16l
+ ___block_descriptor_32_e38_v24?0"ACCredentialItem"8"NSError"16l
+ ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
+ ___block_descriptor_40_e8_32r_e38_v24?0"ACCredentialItem"8"NSError"16lr32l8
+ _kACDAccountsTestingEntitlement
+ _objc_msgSend$removeExpiredCredentials
+ _objc_msgSend$setCredentialItemCleanupVolatilityDuration:withCompletion:
+ _objc_msgSend$setVolatilityDuration:
+ _objc_msgSend$triggerCredentialItemCleanupWithCompletion:
- -[ACDAccountStoreFilter credentialItemForAccount:serviceName:completion:]
- -[ACDAccountStoreFilter credentialItemsWithCompletion:]
- -[ACDAccountStoreFilter insertCredentialItem:completion:]
- -[ACDAccountStoreFilter removeCredentialItem:completion:]
- -[ACDAccountStoreFilter saveCredentialItem:completion:]
- GCC_except_table104
- GCC_except_table109
- GCC_except_table112
- GCC_except_table114
- GCC_except_table124
- GCC_except_table139
- GCC_except_table144
- GCC_except_table150
- GCC_except_table152
- GCC_except_table157
- GCC_except_table179
- GCC_except_table199
- GCC_except_table204
- GCC_except_table227
- GCC_except_table229
- GCC_except_table322
- ___block_descriptor_32_e20_v20?0B8"NSError"12l
- _objc_msgSend$insertCredentialItem:withCompletionHandler:
- _objc_msgSend$removeCredentialItem:withCompletionHandler:
- _objc_msgSend$saveCredentialItem:withCompletionHandler:
CStrings:
+ "\"Client is not entitled to set cleanup volatility duration.\""
+ "\"Client is not entitled to trigger credential item cleanup.\""
+ "T@\"ACDAccountStore\",&,N,V_accountStore"
+ "Td,N,V_volatilityDuration"
+ "_volatilityDuration"
+ "accountStore"
+ "d"
+ "removeExpiredCredentials"
+ "setCredentialItemCleanupVolatilityDuration:withCompletion:"
+ "setVolatilityDuration:"
+ "triggerCredentialItemCleanupWithCompletion:"
+ "v24@0:8d16"
+ "v24@?0@\"ACCredentialItem\"8@\"NSError\"16"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?B@\"NSError\">24"
+ "volatilityDuration"
- "insertCredentialItem:withCompletionHandler:"
- "removeCredentialItem:withCompletionHandler:"
- "saveCredentialItem:withCompletionHandler:"
- "v32@0:8@\"ACCredentialItem\"16@?<v@?@\"ACCredentialItem\"@\"NSError\">24"
- "v32@0:8@\"ACCredentialItem\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@0:8@\"ACCredentialItem\"16@?<v@?B@\"NSError\">24"
- "v40@0:8@\"ACAccount\"16@\"NSString\"24@?<v@?@\"ACCredentialItem\"@\"NSError\">32"

```
