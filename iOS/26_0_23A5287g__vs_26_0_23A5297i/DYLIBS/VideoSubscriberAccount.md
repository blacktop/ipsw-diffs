## VideoSubscriberAccount

> `/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount`

```diff

-590.0.0.0.1
-  __TEXT.__text: 0xd8a20
-  __TEXT.__auth_stubs: 0x1470
-  __TEXT.__objc_methlist: 0x88b4
+592.0.0.0.0
+  __TEXT.__text: 0xd9248
+  __TEXT.__auth_stubs: 0x1480
+  __TEXT.__objc_methlist: 0x88cc
   __TEXT.__const: 0x10fa0
-  __TEXT.__cstring: 0x9e76
+  __TEXT.__cstring: 0x9e96
   __TEXT.__oslogstring: 0x5caa
-  __TEXT.__gcc_except_tab: 0x1634
+  __TEXT.__gcc_except_tab: 0x1650
   __TEXT.__ustring: 0x178
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__swift5_typeref: 0x466
+  __TEXT.__swift5_typeref: 0x480
   __TEXT.__swift5_reflstr: 0x4dd
   __TEXT.__swift5_assocty: 0x1f8
   __TEXT.__constg_swiftt: 0x444

   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x7c
   __TEXT.__swift_as_entry: 0xb0
-  __TEXT.__swift_as_ret: 0xb0
+  __TEXT.__swift_as_ret: 0xb4
   __TEXT.__swift5_capture: 0x1a4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2b30
-  __TEXT.__eh_frame: 0xe40
+  __TEXT.__unwind_info: 0x2b70
+  __TEXT.__eh_frame: 0xe70
   __TEXT.__objc_classname: 0x1364
-  __TEXT.__objc_methname: 0x122ad
+  __TEXT.__objc_methname: 0x122f9
   __TEXT.__objc_methtype: 0x1eb9
-  __TEXT.__objc_stubs: 0xbc60
+  __TEXT.__objc_stubs: 0xbc80
   __DATA_CONST.__got: 0x9e8
-  __DATA_CONST.__const: 0x2628
+  __DATA_CONST.__const: 0x26f0
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4020
+  __DATA_CONST.__objc_selrefs: 0x4030
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0xa48
-  __AUTH_CONST.__const: 0x7ce8
+  __AUTH_CONST.__auth_got: 0xa50
+  __AUTH_CONST.__const: 0x7d38
   __AUTH_CONST.__cfstring: 0x82a0
   __AUTH_CONST.__objc_const: 0x165e8
   __AUTH_CONST.__objc_intobj: 0x210

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E7F3791B-CAAA-3064-A732-0EC88F17AB1E
-  Functions: 4388
-  Symbols:   12147
-  CStrings:  6361
+  UUID: F5CE22AB-97FB-3CF3-89B6-0B5B6E62EF09
+  Functions: 4401
+  Symbols:   12178
+  CStrings:  6364
 
Symbols:
+ -[VSAccountStore _updateCachedFirstAccountWithCompletion:]
+ -[VSAccountStore firstAccountWithCompletionHandler:]
+ GCC_except_table37
+ GCC_except_table54
+ GCC_except_table59
+ ___30-[VSAccountStore firstAccount]_block_invoke_2
+ ___52-[VSAccountStore firstAccountWithCompletionHandler:]_block_invoke
+ ___52-[VSAccountStore firstAccountWithCompletionHandler:]_block_invoke_2
+ ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke.195
+ ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke.199
+ ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke_2.196
+ ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke_2.196.cold.1
+ ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke_2.200
+ ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke_3.204
+ ___53-[VSAccountStore saveAccounts:withCompletionHandler:]_block_invoke.211
+ ___53-[VSAccountStore saveAccounts:withCompletionHandler:]_block_invoke.212
+ ___53-[VSAccountStore saveAccounts:withCompletionHandler:]_block_invoke.214
+ ___55-[VSAccountStore removeAccounts:withCompletionHandler:]_block_invoke.221
+ ___55-[VSAccountStore removeAccounts:withCompletionHandler:]_block_invoke.222
+ ___55-[VSAccountStore removeAccounts:withCompletionHandler:]_block_invoke.224
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke.179
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke.185
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke.187
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_2
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_2.180
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_2.186
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_2.186.cold.1
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_3
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_3.181
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_3.cold.1
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_4
+ ___58-[VSAccountStore _updateCachedFirstAccountWithCompletion:]_block_invoke_4.cold.1
+ ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e29_v24?0"NSArray"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40bs48r56r64w_e5_v8?0lw64l8r48l8s32l8r56l8s40l8
+ ___block_literal_global.177
+ ___block_literal_global.190
+ ___block_literal_global.198
+ _objc_msgSend$_updateCachedFirstAccountWithCompletion:
+ _swift_continuation_resume
+ _symbolic SccySo9VSAccountCSg_____G s5NeverO
- GCC_except_table46
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.175
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.180
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.180.cold.1
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke.182
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_2.177
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_2.177.cold.1
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_3
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_4
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_5
- ___43-[VSAccountStore _updateCachedFirstAccount]_block_invoke_5.cold.1
- ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke.189
- ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke.193
- ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke_2.190
- ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke_2.190.cold.1
- ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke_2.194
- ___53-[VSAccountStore fetchAccountsWithCompletionHandler:]_block_invoke_3.198
- ___53-[VSAccountStore saveAccounts:withCompletionHandler:]_block_invoke.205
- ___53-[VSAccountStore saveAccounts:withCompletionHandler:]_block_invoke.206
- ___53-[VSAccountStore saveAccounts:withCompletionHandler:]_block_invoke.208
- ___55-[VSAccountStore removeAccounts:withCompletionHandler:]_block_invoke.215
- ___55-[VSAccountStore removeAccounts:withCompletionHandler:]_block_invoke.216
- ___55-[VSAccountStore removeAccounts:withCompletionHandler:]_block_invoke.218
- ___block_descriptor_56_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16ls32l8r48l8s40l8
- ___block_literal_global.179
- ___block_literal_global.192
CStrings:
+ "_updateCachedFirstAccountWithCompletion:"
+ "firstAccountWithCompletionHandler:"
+ "v16@?0@\"VSAccount\"8"

```
