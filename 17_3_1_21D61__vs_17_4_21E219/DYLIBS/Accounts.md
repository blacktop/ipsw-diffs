## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-956.0.0.0.0
-  __TEXT.__text: 0x590f4
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x3904
+962.2.0.0.0
+  __TEXT.__text: 0x58ab8
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x391c
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x35e4
-  __TEXT.__cstring: 0x389c
-  __TEXT.__oslogstring: 0x5638
-  __TEXT.__unwind_info: 0x1864
-  __TEXT.__objc_classname: 0x57e
-  __TEXT.__objc_methname: 0x803d
-  __TEXT.__objc_methtype: 0x1572
-  __TEXT.__objc_stubs: 0x5be0
+  __TEXT.__gcc_except_tab: 0x351c
+  __TEXT.__cstring: 0x38a5
+  __TEXT.__oslogstring: 0x543d
+  __TEXT.__unwind_info: 0x183c
+  __TEXT.__objc_classname: 0x580
+  __TEXT.__objc_methname: 0x80bb
+  __TEXT.__objc_methtype: 0x15c2
+  __TEXT.__objc_stubs: 0x5c20
   __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x23b0
+  __DATA_CONST.__const: 0x2428
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5188
-  __DATA_CONST.__objc_selrefs: 0x1f88
+  __DATA_CONST.__objc_const: 0x51e8
+  __DATA_CONST.__objc_selrefs: 0x1f98
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__cfstring: 0x4560
   __AUTH_CONST.__objc_const: 0x1388

   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x620
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x230
-  __DATA.__objc_superrefs: 0x120
-  __DATA.__objc_ivar: 0x378
+  __AUTH_CONST.__auth_got: 0x630
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x384
   __DATA.__data: 0x610
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0x5f0
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1875
-  Symbols:   6258
+  Functions: 1862
+  Symbols:   6241
   CStrings:  2741
 
Symbols:
+ -[ACMonitoredAccountStore _registerNotifyReaders]
+ -[ACNotifyReader dealloc]
+ -[ACNotifyReader initWithKey:updateQueue:updateBlock:]
+ -[ACNotifyReader initWithKey:updateQueue:updateBlock:].cold.1
+ -[ACNotifyWriter dealloc]
+ _OBJC_IVAR_$_ACMonitoredAccountStore._disconnected
+ _OBJC_IVAR_$_ACMonitoredAccountStore._monitoringReaders
+ _OBJC_IVAR_$_ACNotifyReader._dispatchToken
+ ___42-[ACRemoteAccountStoreSession _connection]_block_invoke.55
+ ___49-[ACMonitoredAccountStore _registerNotifyReaders]_block_invoke
+ ___54-[ACNotifyReader initWithKey:updateQueue:updateBlock:]_block_invoke
+ ___71-[ACRemoteAccountStoreSession _locked_connection:setEffectiveBundleID:]_block_invoke.68
+ ___71-[ACRemoteAccountStoreSession _locked_connection:setEffectiveBundleID:]_block_invoke.68.cold.1
+ ___71-[ACRemoteAccountStoreSession _locked_connection:setEffectiveBundleID:]_block_invoke.68.cold.2
+ ___block_descriptor_40_e8_32bs_e8_v12?0i8ls32l8
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_72_e8_32s40bs48w_e29_v24?0"NSArray"8"NSError"16lw48l8s32l8s40l8
+ ___block_literal_global.60
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_msgSend$_registerNotifyReaders
+ _objc_msgSend$initWithKey:updateQueue:updateBlock:
- -[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:].cold.2
- -[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:error:].cold.2
- -[ACAccountStore accountsWithAccountType:completion:].cold.2
- -[ACAccountStore accountsWithAccountType:options:completion:].cold.1
- -[ACAccountStore accountsWithAccountType:options:error:].cold.1
- -[ACNotifyReader currentValue].cold.3
- -[ACNotifyReader initWithKey:]
- -[ACNotifyReader initWithKey:].cold.1
- GCC_except_table1
- GCC_except_table274
- GCC_except_table28
- GCC_except_table33
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- ___38-[ACNotifyAccountCache cachedAccounts]_block_invoke.cold.1
- ___38-[ACNotifyAccountCache cachedAccounts]_block_invoke.cold.2
- ___38-[ACNotifyAccountCache cachedAccounts]_block_invoke.cold.3
- ___38-[ACNotifyAccountCache cachedAccounts]_block_invoke.cold.4
- ___42-[ACRemoteAccountStoreSession _connection]_block_invoke.54
- ___43-[ACMonitoredAccountStore connectionClosed]_block_invoke
- ___44-[ACAccountStoreCache cachedAllAccountTypes]_block_invoke.cold.1
- ___71-[ACRemoteAccountStoreSession _locked_connection:setEffectiveBundleID:]_block_invoke.67
- ___71-[ACRemoteAccountStoreSession _locked_connection:setEffectiveBundleID:]_block_invoke.67.cold.1
- ___71-[ACRemoteAccountStoreSession _locked_connection:setEffectiveBundleID:]_block_invoke.67.cold.2
- ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
- ___block_literal_global.59
CStrings:
+ "\a"
+ "@40@0:8@\"NSString\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?>32"
+ "@40@0:8@16@24@?32"
+ "T@\"NSString\",?,R,C"
+ "_disconnected"
+ "_dispatchToken"
+ "_monitoringReaders"
+ "_registerNotifyReaders"
+ "initWithKey:updateQueue:updateBlock:"
+ "v12@?0i8"
- "\"Failed to get %@ number: notify state is 0\""
- "\"New %@ number: %llu\""
- "\"No cached accounts for key %@, fetching from remote\""
- "\"notify cache hit: cached accounts %@ matches generation for %@\""
- "\"notify cache hit: empty array cache for key %@\""
- "\"notify cache miss: cached account generation changed for %@, clearing!\""
- "\"notify cache miss: current generation is 0 fetching again for key: %@\""
- "@\"all accountTypes already cached\""
- "BEGIN [%lld]: ChildAccountForAccounts %@ : %@"
- "accounts/child-accounts-for-account-with-type"

```
