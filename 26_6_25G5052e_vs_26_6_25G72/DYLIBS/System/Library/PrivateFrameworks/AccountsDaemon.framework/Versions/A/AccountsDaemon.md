## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/Versions/A/AccountsDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1037.0.0.0.0
-  __TEXT.__text: 0x89454
+1038.0.0.0.0
+  __TEXT.__text: 0x89b20
   __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0x3c84
+  __TEXT.__objc_methlist: 0x3cac
   __TEXT.__const: 0xc3a
-  __TEXT.__oslogstring: 0x8b2a
-  __TEXT.__cstring: 0x3ba3
-  __TEXT.__gcc_except_tab: 0x2574
+  __TEXT.__oslogstring: 0x8baa
+  __TEXT.__cstring: 0x3bd3
+  __TEXT.__gcc_except_tab: 0x2598
   __TEXT.__swift5_typeref: 0x5e2
   __TEXT.__constg_swiftt: 0x384
   __TEXT.__swift5_reflstr: 0x24b

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1dd8
+  __TEXT.__unwind_info: 0x1e18
   __TEXT.__eh_frame: 0x9b8
   __TEXT.__objc_classname: 0x759
-  __TEXT.__objc_methname: 0xb849
-  __TEXT.__objc_methtype: 0x2669
-  __TEXT.__objc_stubs: 0x9340
-  __DATA_CONST.__got: 0xd20
-  __DATA_CONST.__const: 0x288
+  __TEXT.__objc_methname: 0xb8c9
+  __TEXT.__objc_methtype: 0x25a9
+  __TEXT.__objc_stubs: 0x9360
+  __DATA_CONST.__got: 0xd28
+  __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29c0
+  __DATA_CONST.__objc_selrefs: 0x29d8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0xa80
-  __AUTH_CONST.__const: 0x2140
+  __AUTH_CONST.__const: 0x21c0
   __AUTH_CONST.__cfstring: 0x3460
-  __AUTH_CONST.__objc_const: 0x4b90
+  __AUTH_CONST.__objc_const: 0x4bc0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x3b8
-  __DATA.__objc_ivar: 0x2bc
+  __DATA.__objc_ivar: 0x2c0
   __DATA.__data: 0x7f0
   __DATA.__bss: 0x860
   __DATA_DIRTY.__objc_data: 0xf70

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2400
-  Symbols:   4436
-  CStrings:  3095
+  Functions: 2412
+  Symbols:   4455
+  CStrings:  3104
 
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
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table139
+ GCC_except_table144
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table175
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table190
+ GCC_except_table213
+ GCC_except_table220
+ GCC_except_table234
+ GCC_except_table239
+ GCC_except_table262
+ GCC_except_table264
+ GCC_except_table359
+ OBJC_IVAR_$_ACDKeychainCleanupActivity._volatilityDuration
+ __OBJC_$_PROP_LIST_ACDKeychainCleanupActivity
+ ___37-[ACDAccountStore allCredentialItems]_block_invoke
+ ___54-[ACDKeychainCleanupActivity removeExpiredCredentials]_block_invoke
+ ___56-[ACDAccountStore credentialItemForAccount:serviceName:]_block_invoke
+ ___block_descriptor_32_e27_v24?0"NSURL"8"NSError"16l
+ ___block_descriptor_32_e38_v24?0"ACCredentialItem"8"NSError"16l
+ ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_40_e8_32r_e38_v24?0"ACCredentialItem"8"NSError"16l
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
- GCC_except_table128
- GCC_except_table133
- GCC_except_table136
- GCC_except_table138
- GCC_except_table140
- GCC_except_table150
- GCC_except_table163
- GCC_except_table177
- GCC_except_table179
- GCC_except_table184
- GCC_except_table207
- GCC_except_table214
- GCC_except_table226
- GCC_except_table231
- GCC_except_table254
- GCC_except_table256
- GCC_except_table351
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
