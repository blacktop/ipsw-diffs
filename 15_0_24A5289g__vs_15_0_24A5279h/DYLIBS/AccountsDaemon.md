## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/Versions/A/AccountsDaemon`

```diff

-985.0.0.0.0
-  __TEXT.__text: 0x7d430
+984.0.0.0.0
+  __TEXT.__text: 0x7d18c
   __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x3274
+  __TEXT.__objc_methlist: 0x3264
   __TEXT.__const: 0x726
-  __TEXT.__oslogstring: 0x824f
-  __TEXT.__cstring: 0x3d83
+  __TEXT.__oslogstring: 0x821f
+  __TEXT.__cstring: 0x3da3
   __TEXT.__gcc_except_tab: 0x2564
   __TEXT.__swift5_typeref: 0x2a4
   __TEXT.__swift5_capture: 0x88

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x19d8
+  __TEXT.__unwind_info: 0x19c0
   __TEXT.__eh_frame: 0x248
   __TEXT.__objc_classname: 0x61c
-  __TEXT.__objc_methname: 0xb0c4
-  __TEXT.__objc_methtype: 0x244a
+  __TEXT.__objc_methname: 0xb0cd
+  __TEXT.__objc_methtype: 0x246b
   __TEXT.__objc_stubs: 0x8f80
-  __DATA_CONST.__got: 0xc98
+  __DATA_CONST.__got: 0xca0
   __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2758
+  __DATA_CONST.__objc_selrefs: 0x2750
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x930
   __AUTH_CONST.__auth_ptr: 0x208
-  __AUTH_CONST.__const: 0x1c18
-  __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x5690
+  __AUTH_CONST.__const: 0x1b88
+  __AUTH_CONST.__cfstring: 0x33c0
+  __AUTH_CONST.__objc_const: 0x56b0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x2e0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2107
-  Symbols:   4871
-  CStrings:  566
+  Functions: 2102
+  Symbols:   4863
+  CStrings:  567
 
Symbols:
+ -[ACDAccountCache cacheAccount:].cold.1
+ -[ACDAccountStore _updateExistenceCacheOfAccountWithTypeIdentifier:withHandler:]
+ -[ACDAccountStore updateExistenceCacheOfAccountWithTypeIdentifier:withHandler:]
+ -[ACDAccountStoreFilter updateExistenceCacheOfAccountWithTypeIdentifier:withHandler:]
+ GCC_except_table102
+ GCC_except_table108
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table133
+ GCC_except_table143
+ GCC_except_table160
+ GCC_except_table166
+ GCC_except_table174
+ GCC_except_table181
+ GCC_except_table206
+ GCC_except_table224
+ GCC_except_table229
+ GCC_except_table250
+ GCC_except_table257
+ GCC_except_table341
+ GCC_except_table47
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table93
+ GCC_except_table99
+ _OBJC_CLASS_$_ACSystemConfigManager
+ __52-[ACDAccountCache cacheAccounts:forType:justActive:]_block_invoke.18
+ __52-[ACDAccountCache cacheAccounts:forType:justActive:]_block_invoke_3.cold.1
+ __61-[ACDAccountStore dataclassActionsForAccountSave:completion:]_block_invoke.246
+ __65-[ACDAccountStore renewCredentialsForAccount:options:completion:]_block_invoke.228
+ __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.213
+ __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.217
+ __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.217.cold.1
+ __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.217.cold.2
+ __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.221
+ __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.221.cold.1
+ __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.221.cold.2
+ ___51-[ACDAccountCache cachedAccountsOfType:justActive:]_block_invoke
+ ___52-[ACDAccountCache cacheAccounts:forType:justActive:]_block_invoke_2
+ ___52-[ACDAccountCache cacheAccounts:forType:justActive:]_block_invoke_3
+ ___79-[ACDAccountStore updateExistenceCacheOfAccountWithTypeIdentifier:withHandler:]_block_invoke
+ ___ACDChangeDictionaryForAccount_block_invoke.637
+ ___block_descriptor_49_e8_32s40s_e14_"NSArray"8?0l
+ __block_literal_global.208
+ __block_literal_global.223
+ __block_literal_global.255
+ _objc_msgSend$_updateExistenceCacheOfAccountWithTypeIdentifier:withHandler:
+ _objc_msgSend$cachedAccountsOfType:justActive:
+ _objc_msgSend$setAccountsWithAccountTypeIdentifier:exist:
+ _objc_msgSend$setCountOfAccounts:withAccountTypeIdentifier:
+ _objc_msgSend$updateExistenceCacheOfAccountWithTypeIdentifier:withHandler:
- -[ACDAccountCache _caches_lock_cacheAccounts:forType:justActive:]
- -[ACDAccountCache _lock_cacheAccount:]
- -[ACDAccountCache _lock_cacheAccount:].cold.1
- -[ACDAccountCache cachedAccountsOfType:justActive:fetchBlock:]
- -[ACDAccountStore _block_accountWithIdentifier:]
- -[ACDAccountStore _block_accountsWithAccountTypeIdentifiers:preloadedProperties:]
- -[ACDAccountStore _saveWithError:].cold.6
- GCC_except_table100
- GCC_except_table103
- GCC_except_table109
- GCC_except_table116
- GCC_except_table120
- GCC_except_table122
- GCC_except_table127
- GCC_except_table132
- GCC_except_table141
- GCC_except_table159
- GCC_except_table162
- GCC_except_table168
- GCC_except_table178
- GCC_except_table183
- GCC_except_table205
- GCC_except_table223
- GCC_except_table228
- GCC_except_table252
- GCC_except_table259
- GCC_except_table344
- GCC_except_table35
- GCC_except_table37
- GCC_except_table44
- GCC_except_table46
- GCC_except_table75
- GCC_except_table77
- GCC_except_table79
- GCC_except_table81
- GCC_except_table84
- GCC_except_table94
- __61-[ACDAccountStore dataclassActionsForAccountSave:completion:]_block_invoke.245
- __65-[ACDAccountCache _caches_lock_cacheAccounts:forType:justActive:]_block_invoke_3.cold.1
- __65-[ACDAccountStore renewCredentialsForAccount:options:completion:]_block_invoke.231
- __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.216
- __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.220
- __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.220.cold.1
- __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.220.cold.2
- __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.224
- __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.224.cold.1
- __66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.224.cold.2
- __85-[ACDAccountStore accountsWithAccountTypeIdentifiers:preloadedProperties:completion:]_block_invoke.271
- ___58-[ACDAccountStore _accountsWithAccountType:options:error:]_block_invoke_2
- ___62-[ACDAccountCache cachedAccountsOfType:justActive:fetchBlock:]_block_invoke
- ___65-[ACDAccountCache _caches_lock_cacheAccounts:forType:justActive:]_block_invoke
- ___65-[ACDAccountCache _caches_lock_cacheAccounts:forType:justActive:]_block_invoke_2
- ___65-[ACDAccountCache _caches_lock_cacheAccounts:forType:justActive:]_block_invoke_3
- ___85-[ACDAccountStore accountsWithAccountTypeIdentifiers:preloadedProperties:completion:]_block_invoke_2
- ___ACDChangeDictionaryForAccount_block_invoke.638
- ___block_descriptor_56_e8_32s40s48s_e14_"NSArray"8?0l
- ___block_descriptor_57_e8_32s40s48bs_e14_"NSArray"8?0l
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48r_e14_"NSArray"8?0l
- __block_literal_global.211
- __block_literal_global.226
- __block_literal_global.254
- _objc_msgSend$_block_accountWithIdentifier:
- _objc_msgSend$_block_accountsWithAccountTypeIdentifiers:preloadedProperties:
- _objc_msgSend$_caches_lock_cacheAccounts:forType:justActive:
- _objc_msgSend$_lock_cacheAccount:
- _objc_msgSend$cachedAccountsOfType:justActive:fetchBlock:
CStrings:
+ "accountType.identifier=%!@(MISSING)"

```
