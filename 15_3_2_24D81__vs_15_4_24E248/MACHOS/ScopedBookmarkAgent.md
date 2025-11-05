## ScopedBookmarkAgent

> `/System/Library/CoreServices/ScopedBookmarkAgent`

```diff

-548.3.0.0.0
-  __TEXT.__text: 0x8184
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_stubs: 0x5c0
+554.5.0.0.0
+  __TEXT.__text: 0x91c0
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_stubs: 0xa60
+  __TEXT.__objc_methlist: 0x164
   __TEXT.__const: 0xdc
-  __TEXT.__cstring: 0xd38
-  __TEXT.__gcc_except_tab: 0x400
-  __TEXT.__oslogstring: 0x138d
-  __TEXT.__objc_methname: 0x378
-  __TEXT.__unwind_info: 0x1a0
-  __DATA_CONST.__auth_got: 0x520
-  __DATA_CONST.__got: 0x1e0
+  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__cstring: 0xf59
+  __TEXT.__objc_methname: 0x7eb
+  __TEXT.__oslogstring: 0x1428
+  __TEXT.__objc_classname: 0xb
+  __TEXT.__objc_methtype: 0xef
+  __TEXT.__unwind_info: 0x220
+  __DATA_CONST.__auth_got: 0x528
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x160
-  __DATA_CONST.__cfstring: 0x6a0
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__cfstring: 0x760
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_selrefs: 0x170
+  __DATA.__objc_const: 0x250
+  __DATA.__objc_selrefs: 0x2a8
+  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_data: 0x50
   __DATA.__data: 0x28
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34929584-C571-3DF8-B70A-2BEFA70720D5
-  Functions: 134
-  Symbols:   1030
-  CStrings:  335
+  UUID: ECA5D9C6-C0C0-3525-9C5B-F6D2737BCFEA
+  Functions: 169
+  Symbols:   1286
+  CStrings:  427
 
Symbols:
+ +[KeyManager shared]
+ +[KeyManager shared].cold.1
+ -[KeyManager _fetchAgentKey]
+ -[KeyManager _fetchAgentKey].cold.1
+ -[KeyManager _fetchAgentKey].cold.2
+ -[KeyManager _fetchDataProtectionAgentKey]
+ -[KeyManager _fetchDataProtectionAgentKey].cold.1
+ -[KeyManager _fetchLegacyAgentKey]
+ -[KeyManager _fetchLegacyAgentKey].cold.1
+ -[KeyManager _fetchLegacyAgentKey].cold.2
+ -[KeyManager _insertDataProtectionAgentKey:]
+ -[KeyManager _insertDataProtectionAgentKey:].cold.1
+ -[KeyManager _insertLegacyAgentKey:]
+ -[KeyManager _insertLegacyAgentKey:].cold.1
+ -[KeyManager _insertLegacyAgentKey:].cold.2
+ -[KeyManager _migrateAgentKey]
+ -[KeyManager _migrateAgentKey].cold.1
+ -[KeyManager agentKey]
+ -[KeyManager dataProcessedWithKEK:encrypt:]
+ -[KeyManager dataProcessedWithKEK:encrypt:].cold.1
+ -[KeyManager dataProtectionAgentKey]
+ -[KeyManager dealloc]
+ -[KeyManager encryptedLabel]
+ -[KeyManager getSigningIdentifier:bundleIdentifier:forAuditToken:]
+ -[KeyManager initWithSuffix:]
+ -[KeyManager kekFileName]
+ -[KeyManager keyEncryptionKeyURL]
+ -[KeyManager keyEncryptionKeyURL].cold.1
+ -[KeyManager keyEncryptionKeyURL].cold.2
+ -[KeyManager keyEncryptionKey]
+ -[KeyManager label]
+ -[KeyManager legacyAgentKey]
+ -[KeyManager newKey]
+ -[KeyManager readKeyEncryptionKey]
+ -[KeyManager readKeyEncryptionKey].cold.1
+ -[KeyManager saveBackupAgentKey:]
+ -[KeyManager saveBackupAgentKey:].cold.1
+ -[KeyManager scopeKeyForAuditToken:revocable:]
+ -[KeyManager scopeKeyForAuditToken:revocable:].cold.1
+ -[KeyManager scopeKeyForAuditToken:revocable:].cold.2
+ -[KeyManager scopeKeyForCollection:create:]
+ -[KeyManager scopeKeyForCollection:create:].cold.1
+ -[KeyManager scopeKeyForCollection:create:].cold.2
+ -[KeyManager scopeKeyForCollection:create:].cold.3
+ -[KeyManager scopeKeyForCollection:create:].cold.4
+ -[KeyManager scopeKeyForCollection:create:].cold.5
+ -[KeyManager scopeKeyForSigningIdentifier:]
+ -[KeyManager scopeKeyForSigningIdentifier:].cold.1
+ -[KeyManager scopeKeyForSigningIdentifier:].cold.2
+ -[KeyManager setDataProtectionAgentKey:]
+ -[KeyManager setLegacyAgentKey:]
+ -[KeyManager writeKeyEncryptionKey:]
+ -[KeyManager writeKeyEncryptionKey:].cold.1
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/Objects-normal/arm64e/KeyManager.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/Objects-normal/arm64e/Logging.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/Objects-normal/arm64e/Revocable.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/Objects-normal/arm64e/ScopedBookmarkAgent_vers.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/Objects-normal/arm64e/ScopedBookmarksAgent.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesInternalScopedBookmarksAgent/Source/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesInternalScopedBookmarksAgent/Source/Bookmarks/ScopedBookmarksAgent/
+ GCC_except_table11
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table23
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table3
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table68
+ GCC_except_table7
+ GCC_except_table8
+ KeyManager.mm
+ OBJC_IVAR_$_KeyManager._agentKey
+ OBJC_IVAR_$_KeyManager._agentKeyLock
+ OBJC_IVAR_$_KeyManager._cachedScopeKeysForPid
+ OBJC_IVAR_$_KeyManager._cachedScopedKeysLock
+ OBJC_IVAR_$_KeyManager._dataProtectionAgentKey
+ OBJC_IVAR_$_KeyManager._dataProtectionAgentKeyLock
+ OBJC_IVAR_$_KeyManager._encryptedLabel
+ OBJC_IVAR_$_KeyManager._kekFileName
+ OBJC_IVAR_$_KeyManager._keyEncryptionKey
+ OBJC_IVAR_$_KeyManager._keyEncryptionKeyLock
+ OBJC_IVAR_$_KeyManager._label
+ OBJC_IVAR_$_KeyManager._legacyAgentKey
+ OBJC_IVAR_$_KeyManager._legacyAgentKeyLock
+ Revocable.mm
+ _CCCrypt
+ _CFRetain
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_KeyManager
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_KeyManager
+ _OBJC_METACLASS_$_NSObject
+ _Z27GetRevocableClientsSnapshotv.cold.1
+ _Z30CreateRevocableClientFromToken13audit_token_t.cold.1
+ _Z38RevocableClientsRevokeBundleIdentifierP8NSString.cold.1
+ _Z38RevocableClientsSetStatusForIdentifierP8NSStringb.cold.1
+ _Z42GetRevocableClientSnapshotForAppIdentifierP8NSString.cold.1
+ _ZL21_SaveRevocableClientsv.cold.1
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.1
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.10
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.11
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.12
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.13
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.2
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.3
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.4
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.5
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.6
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.7
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.8
+ _ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_.cold.9
+ _ZL22handle_upgrade_requestPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t.cold.1
+ _ZL22handle_upgrade_requestPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t.cold.2
+ _ZL23handle_revocable_revokePU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t.cold.1
+ _ZL29handle_revocable_copy_clientsPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t.cold.1
+ _ZL41handle_revocable_set_client_active_statusPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t.cold.1
+ __OBJC_$_CLASS_METHODS_KeyManager
+ __OBJC_$_INSTANCE_METHODS_KeyManager
+ __OBJC_$_INSTANCE_VARIABLES_KeyManager
+ __OBJC_$_PROP_LIST_KeyManager
+ __OBJC_CLASS_RO_$_KeyManager
+ __OBJC_METACLASS_RO_$_KeyManager
+ __Z27GetRevocableClientsSnapshotv
+ __Z30CreateRevocableClientFromToken13audit_token_t
+ __Z38RevocableClientsRevokeBundleIdentifierP8NSString
+ __Z38RevocableClientsSetStatusForIdentifierP8NSStringb
+ __Z42GetRevocableClientSnapshotForAppIdentifierP8NSString
+ __ZL22handle_copy_id_requestPU24objcproto13OS_xpc_object8NSObjectS1_
+ __ZL22handle_upgrade_requestPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t
+ __ZL23handle_revocable_revokePU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t
+ __ZL29handle_revocable_copy_clientsPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t
+ __ZL40handle_revocable_copy_bundle_identifiersPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t
+ __ZL41handle_revocable_set_client_active_statusPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
+ __ZNSt3__116__pad_and_outputB8nn190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn190102Ev
+ __ZNSt3__124__put_character_sequenceB8nn190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__1lsB8nn190102INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_RKNS_8__iom_t4IcEE
+ __ZZ20+[KeyManager shared]E6shared
+ __ZZ20+[KeyManager shared]E9onceToken
+ ___20+[KeyManager shared]_block_invoke
+ __objc_empty_cache
+ _kSecAttrService
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$_fetchAgentKey
+ _objc_msgSend$_fetchDataProtectionAgentKey
+ _objc_msgSend$_fetchLegacyAgentKey
+ _objc_msgSend$_insertDataProtectionAgentKey:
+ _objc_msgSend$_insertLegacyAgentKey:
+ _objc_msgSend$_migrateAgentKey
+ _objc_msgSend$agentKey
+ _objc_msgSend$code
+ _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dataProcessedWithKEK:encrypt:
+ _objc_msgSend$dataProtectionAgentKey
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$domain
+ _objc_msgSend$encryptedLabel
+ _objc_msgSend$fileURLWithPath:isDirectory:relativeToURL:
+ _objc_msgSend$getSigningIdentifier:bundleIdentifier:forAuditToken:
+ _objc_msgSend$initWithSuffix:
+ _objc_msgSend$kekFileName
+ _objc_msgSend$keyEncryptionKey
+ _objc_msgSend$keyEncryptionKeyURL
+ _objc_msgSend$label
+ _objc_msgSend$legacyAgentKey
+ _objc_msgSend$newKey
+ _objc_msgSend$readKeyEncryptionKey
+ _objc_msgSend$saveBackupAgentKey:
+ _objc_msgSend$scopeKeyForAuditToken:revocable:
+ _objc_msgSend$scopeKeyForCollection:create:
+ _objc_msgSend$scopeKeyForSigningIdentifier:
+ _objc_msgSend$setDataProtectionAgentKey:
+ _objc_msgSend$setLegacyAgentKey:
+ _objc_msgSend$shared
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$writeKeyEncryptionKey:
+ _objc_msgSend$writeToURL:options:error:
+ _objc_msgSendSuper2
- /AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/Objects-normal/arm64e/Logging.o
- /AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/Objects-normal/arm64e/ScopedBookmarkAgent_vers.o
- /AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Binaries/CoreServicesInternalScopedBookmarksAgent/install/TempContent/Objects/CoreServicesInternal.build/ScopedBookmarkAgent.build/Objects-normal/arm64e/ScopedBookmarksAgent.o
- /AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesInternalScopedBookmarksAgent/Source/
- /AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesInternalScopedBookmarksAgent/Source/Bookmarks/ScopedBookmarksAgent/
- GCC_except_table20
- GCC_except_table21
- GCC_except_table32
- GCC_except_table33
- GCC_except_table4
- GCC_except_table66
- GCC_except_table70
- GCC_except_table71
- GCC_except_table72
- GCC_except_table73
- GCC_except_table74
- GCC_except_table81
- GCC_except_table82
- GCC_except_table83
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _ZL21copy_legacy_agent_keyv.cold.1
- _ZL21copy_legacy_agent_keyv.cold.2
- _ZL28get_scope_key_for_collectionib.cold.1
- _ZL28get_scope_key_for_collectionib.cold.2
- _ZL28get_scope_key_for_collectionib.cold.3
- _ZL34scope_key_for_app_with_audit_token13audit_token_tb.cold.1
- _ZL34scope_key_for_app_with_audit_token13audit_token_tb.cold.2
- _ZL41scope_key_for_app_with_signing_identifierP8NSString.cold.1
- _ZL41scope_key_for_app_with_signing_identifierP8NSString.cold.2
- __ZL21copy_legacy_agent_keyv
- __ZL27GetRevocableClientsSnapshotv
- __ZL28get_scope_key_for_collectionib
- __ZL30CreateRevocableClientFromToken13audit_token_t
- __ZL34scope_key_for_app_with_audit_token13audit_token_tb
- __ZL36get_app_identifiers_with_audit_token13audit_token_tPP8NSStringS2_
- __ZL41scope_key_for_app_with_signing_identifierP8NSString
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn180100Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn180100ILi0EEEPKc
- __ZNSt3__116__pad_and_outputB8nn180100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn180100Ev
- __ZNSt3__124__put_character_sequenceB8nn180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__1lsB8nn180100INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_RKNS_8__iom_t4IcEE
- __ZSt9terminatev
- __ZZL13get_agent_keyvE13cachedKeyData
- __ZZL13get_agent_keyvE9onceToken
- __ZZL34scope_key_for_app_with_audit_token13audit_token_tbE22sCachedScopeKeysForPid
- __ZZL34scope_key_for_app_with_audit_token13audit_token_tbE4lock
- __ZZL34scope_key_for_app_with_audit_token13audit_token_tbE5sOnce
- ___ZL13get_agent_keyv_block_invoke.cold.1
- ___ZL13get_agent_keyv_block_invoke.cold.10
- ___ZL13get_agent_keyv_block_invoke.cold.2
- ___ZL13get_agent_keyv_block_invoke.cold.3
- ___ZL13get_agent_keyv_block_invoke.cold.4
- ___ZL13get_agent_keyv_block_invoke.cold.5
- ___ZL13get_agent_keyv_block_invoke.cold.6
- ___ZL13get_agent_keyv_block_invoke.cold.7
- ___ZL13get_agent_keyv_block_invoke.cold.8
- ___ZL13get_agent_keyv_block_invoke.cold.9
- ____ZL13get_agent_keyv_block_invoke
- ____ZL34scope_key_for_app_with_audit_token13audit_token_tb_block_invoke
- ___clang_call_terminate
- ___cxa_begin_catch
- __block_literal_global.118
- __block_literal_global.128
- __block_literal_global.138
- __main_block_invoke.9.cold.35
- __main_block_invoke.9.cold.36
- __main_block_invoke.9.cold.37
- __main_block_invoke.9.cold.38
- __main_block_invoke.9.cold.39
- __main_block_invoke.9.cold.40
- __main_block_invoke.9.cold.41
- __main_block_invoke.9.cold.42
- __main_block_invoke.9.cold.43
- __main_block_invoke.9.cold.44
- __main_block_invoke.9.cold.45
- __main_block_invoke.9.cold.46
- __main_block_invoke.9.cold.47
- __main_block_invoke.9.cold.48
- __main_block_invoke.9.cold.49
- __main_block_invoke.9.cold.50
- __main_block_invoke.9.cold.51
- __main_block_invoke.9.cold.52
- _objc_msgSend$debugDescription
CStrings:
+ ""
+ "%s: cryptor result: %d"
+ "%s: error creating subdirectories: %@"
+ "%s: error inserting login key: %d"
+ "%s: error reading KEK: %{public}@"
+ "%s: error writing KEK: %{public}@"
+ "%s: failed to decrypt the bookmark"
+ "%s: failed to encrypt the bookmark"
+ "-[KeyManager _fetchAgentKey]"
+ "-[KeyManager _fetchDataProtectionAgentKey]"
+ "-[KeyManager _fetchLegacyAgentKey]"
+ "-[KeyManager _insertDataProtectionAgentKey:]"
+ "-[KeyManager _insertLegacyAgentKey:]"
+ "-[KeyManager _migrateAgentKey]"
+ "-[KeyManager dataProcessedWithKEK:encrypt:]"
+ "-[KeyManager getSigningIdentifier:bundleIdentifier:forAuditToken:]"
+ "-[KeyManager keyEncryptionKeyURL]"
+ "-[KeyManager readKeyEncryptionKey]"
+ "-[KeyManager saveBackupAgentKey:]"
+ "-[KeyManager scopeKeyForAuditToken:revocable:]"
+ "-[KeyManager scopeKeyForCollection:create:]"
+ "-[KeyManager writeKeyEncryptionKey:]"
+ "21:44:11"
+ "@\"NSData\""
+ "@\"NSMutableDictionary\""
+ "@\"NSString\""
+ "@16@0:8"
+ "@24@0:8@16"
+ "@24@0:8i16B20"
+ "@28@0:8@16B24"
+ "@52@0:8{?=[8I]}16B48"
+ "B64@0:8^@16^@24{?=[8I]}32"
+ "KeyManager"
+ "KeyManager.keyEncryptionKeyURL: no container URL."
+ "Library/Application Support/com.apple.scopedbookmarkagent/"
+ "Mar  7 2025"
+ "T@\"NSData\",R"
+ "URLByAppendingPathComponent:"
+ "^{__CFString=}"
+ "^{__CFString=}16@0:8"
+ "_agentKey"
+ "_agentKeyLock"
+ "_cachedScopeKeysForPid"
+ "_cachedScopedKeysLock"
+ "_dataProtectionAgentKey"
+ "_dataProtectionAgentKeyLock"
+ "_encryptedLabel"
+ "_fetchAgentKey"
+ "_fetchDataProtectionAgentKey"
+ "_fetchLegacyAgentKey"
+ "_insertDataProtectionAgentKey:"
+ "_insertLegacyAgentKey:"
+ "_kekFileName"
+ "_keyEncryptionKey"
+ "_keyEncryptionKeyLock"
+ "_label"
+ "_legacyAgentKey"
+ "_legacyAgentKeyLock"
+ "_migrateAgentKey"
+ "agentKey"
+ "code"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dataProcessedWithKEK:encrypt:"
+ "dataProtectionAgentKey"
+ "dataWithContentsOfURL:options:error:"
+ "dataWithLength:"
+ "dealloc"
+ "defaultManager"
+ "domain"
+ "encrypted"
+ "encryptedLabel"
+ "fileURLWithPath:isDirectory:relativeToURL:"
+ "getSigningIdentifier:bundleIdentifier:forAuditToken:"
+ "group.com.apple.scopedbookmarkagent"
+ "init"
+ "initWithSuffix:"
+ "kek.%@.data"
+ "kek.data"
+ "kekFileName"
+ "keyEncryptionKey"
+ "keyEncryptionKeyURL"
+ "label"
+ "legacyAgentKey"
+ "newKey"
+ "readKeyEncryptionKey"
+ "saveBackupAgentKey:"
+ "scopeKeyForAuditToken:revocable:"
+ "scopeKeyForCollection:create:"
+ "scopeKeyForSigningIdentifier:"
+ "setDataProtectionAgentKey:"
+ "setLegacyAgentKey:"
+ "shared"
+ "stringByAppendingPathExtension:"
+ "v16@0:8"
+ "v24@0:8@16"
+ "writeKeyEncryptionKey:"
+ "writeToURL:options:error:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "%s: error %d inserting new agent key for uid=%d"
- "%s: no legacy agent key found"
- "23:31:28"
- "Dec 18 2024"
- "backup_agent_key"
- "copy_data_protection_agent_key"
- "copy_legacy_agent_key"
- "copy_migrated_agent_key"
- "debugDescription"
- "get_agent_key_block_invoke"
- "get_app_identifiers_with_audit_token"
- "scope_key_for_app_with_audit_token"

```
