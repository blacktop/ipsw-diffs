## SyncedDefaults

> `/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults`

```diff

-2150.11.0.0.0
-  __TEXT.__text: 0xb9dc
+2150.12.0.0.0
+  __TEXT.__text: 0xba50
   __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0x81c
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xc78
+  __TEXT.__cstring: 0xce8
   __TEXT.__oslogstring: 0x1a58
-  __TEXT.__gcc_except_tab: 0x734
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__gcc_except_tab: 0x744
+  __TEXT.__unwind_info: 0x454
   __TEXT.__objc_classname: 0xcc
-  __TEXT.__objc_methname: 0x1a1d
+  __TEXT.__objc_methname: 0x1a39
   __TEXT.__objc_methtype: 0x677
-  __TEXT.__objc_stubs: 0x14a0
+  __TEXT.__objc_stubs: 0x14c0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x480
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x770
-  __DATA_CONST.__objc_selrefs: 0x698
+  __DATA_CONST.__objc_selrefs: 0x6a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x960
+  __AUTH_CONST.__cfstring: 0x980
   __AUTH_CONST.__objc_const: 0x288
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 346
-  Symbols:   1193
-  CStrings:  557
+  Symbols:   1194
+  CStrings:  559
 
Symbols:
+ ___44-[SYDClientToDaemonConnection xpcConnection]_block_invoke.279
+ ___47+[SYDClientToDaemonConnection newXPCConnection]_block_invoke.189
+ ___47+[SYDClientToDaemonConnection newXPCConnection]_block_invoke.189.cold.1
+ ___49-[SYDClientToDaemonConnection synchronizeForced:]_block_invoke.163
+ ___50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.137
+ ___50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke_2.141
+ ___54+[SYDClientToDaemonConnection daemonProtocolInterface]_block_invoke.270
+ ___54-[SYDClientToDaemonConnection setObject:forKey:error:]_block_invoke.133
+ ___61-[SYDClientToDaemonConnection applicationWillEnterForeground]_block_invoke.205
+ ___61-[SYDClientToDaemonConnection applicationWillEnterForeground]_block_invoke.205.cold.1
+ ___62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.195
+ ___62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.195.cold.1
+ ___62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.195.cold.2
+ ___68-[SYDClientToDaemonConnection synchronizationWithCompletionHandler:]_block_invoke.170
+ ___74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.219
+ ___74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.219.cold.1
+ ___74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.219.cold.2
+ ___79+[SYDClientToDaemonConnection isCloudSyncUserDefaultEnabledForStoreIdentifier:]_block_invoke.179
+ ___87+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:completionHandler:]_block_invoke.174
+ ___87+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:completionHandler:]_block_invoke.174.cold.1
+ ___87+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:completionHandler:]_block_invoke.175
+ ___87+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:completionHandler:]_block_invoke.176
+ ___block_literal_global.178
+ ___block_literal_global.182
+ ___block_literal_global.197
+ ___block_literal_global.212
+ ___block_literal_global.214
+ ___block_literal_global.216
+ ___block_literal_global.221
+ ___block_literal_global.273
+ ___block_literal_global.278
+ _objc_msgSend$lengthOfBytesUsingEncoding:
- ___44-[SYDClientToDaemonConnection xpcConnection]_block_invoke.276
- ___47+[SYDClientToDaemonConnection newXPCConnection]_block_invoke.186
- ___47+[SYDClientToDaemonConnection newXPCConnection]_block_invoke.186.cold.1
- ___49-[SYDClientToDaemonConnection synchronizeForced:]_block_invoke.160
- ___50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.134
- ___50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke_2.138
- ___54+[SYDClientToDaemonConnection daemonProtocolInterface]_block_invoke.267
- ___54-[SYDClientToDaemonConnection setObject:forKey:error:]_block_invoke.130
- ___61-[SYDClientToDaemonConnection applicationWillEnterForeground]_block_invoke.202
- ___61-[SYDClientToDaemonConnection applicationWillEnterForeground]_block_invoke.202.cold.1
- ___62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.192
- ___62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.192.cold.1
- ___62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.192.cold.2
- ___68-[SYDClientToDaemonConnection synchronizationWithCompletionHandler:]_block_invoke.167
- ___74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.216
- ___74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.216.cold.1
- ___74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.216.cold.2
- ___79+[SYDClientToDaemonConnection isCloudSyncUserDefaultEnabledForStoreIdentifier:]_block_invoke.176
- ___87+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:completionHandler:]_block_invoke.171
- ___87+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:completionHandler:]_block_invoke.171.cold.1
- ___87+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:completionHandler:]_block_invoke.172
- ___87+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:completionHandler:]_block_invoke.173
- ___block_literal_global.175
- ___block_literal_global.179
- ___block_literal_global.185
- ___block_literal_global.209
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.270
- ___block_literal_global.275
CStrings:
+ "NSUbiquitousKeyValueStore key '%@' is larger than the maximum allowed UTF-8 code units of (%ld)"
+ "NSUbiquitousKeyValueStore key '%@' is longer than the maximum allowed UTF-16 code units of (%ld)"
+ "lengthOfBytesUsingEncoding:"
- "NSUbiquitousKeyValueStore key '%@' is longer than the maximum allowed size (%ld)"

```
