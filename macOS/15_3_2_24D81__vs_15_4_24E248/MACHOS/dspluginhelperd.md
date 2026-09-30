## dspluginhelperd

> `/usr/libexec/dspluginhelperd`

```diff

 686.0.0.0.0
-  __TEXT.__text: 0x3f73c
+  __TEXT.__text: 0x3edb8
   __TEXT.__auth_stubs: 0x1250
   __TEXT.__init_offsets: 0xc
-  __TEXT.__const: 0x6c0
-  __TEXT.__gcc_except_tab: 0x43a8
+  __TEXT.__const: 0x6b0
+  __TEXT.__gcc_except_tab: 0x435c
   __TEXT.__cstring: 0x907f
   __TEXT.__oslogstring: 0x128
   __TEXT.__dof_dslocksta: 0x3d5
   __TEXT.__unwind_info: 0x1080
   __DATA_CONST.__auth_got: 0x930
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0x1780
   __DATA_CONST.__cfstring: 0x23e0
   __DATA.__data: 0x140

   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libsasl2.2.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C0140A6E-3A3E-3B80-BF8E-BAFD49735FBE
-  Functions: 869
-  Symbols:   1659
+  UUID: 6A277CD4-653B-3FDE-96DD-36A881A89EC4
+  Functions: 863
+  Symbols:   1715
   CStrings:  1336
 
Symbols:
+ _ODNodeInitWithName.cold.1
+ _ZL11_QueryStartPv.cold.1
+ _ZL11_QueryStartPv.cold.2
+ _ZL11_QueryStartPv.cold.3
+ _ZL11_add_od_refPKvi.cold.1
+ _ZL18_remove_identifierPKvi.cold.1
+ _ZL20_delete_refs_for_pidi.cold.1
+ _ZL22_get_and_retain_od_refPKviPjj.cold.1
+ _ZL23_od_passthru_send_replyjyPKvjb.cold.1
+ _ZL26_QueryCreateWithNode_asyncPKvPK9__CFArrayjyi.cold.1
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ ___ZN9CRefTable15CreateReferenceEPj8eRefTypeP13CServerPluginjijP8sockaddriPKc_block_invoke.15.cold.1
+ ___read_schema_block_invoke.cold.10
+ ___read_schema_block_invoke.cold.11
+ ___read_schema_block_invoke.cold.12
+ ___read_schema_block_invoke.cold.13
+ ___read_schema_block_invoke.cold.7
+ ___read_schema_block_invoke.cold.8
+ ___read_schema_block_invoke.cold.9
+ __od_passthru_log_message_block_invoke.cold.1
+ __receive_session_close_block_invoke.cold.1
+ __receive_session_close_block_invoke.cold.2
+ __receive_session_create_block_invoke.cold.1
+ __receive_session_create_block_invoke.cold.2
+ __receive_session_create_block_invoke.cold.3
+ _schema_construct.cold.1
+ _schema_deconstruct.cold.1
+ _schema_validate_type.cold.2
+ od_passthru_get_uid.cold.1
+ od_passthru_log_message.cold.1
+ od_passthru_log_message.cold.2
+ od_passthru_register_node.cold.1
+ od_passthru_set_plugin_enabled.cold.1
+ od_passthru_unregister_node.cold.1
+ odschema_get_legacy_matchtype.cold.1
+ receive_extmodule_new_connection.cold.1
+ receive_extmodule_new_connection.cold.2
+ receive_extmodule_new_connection.cold.3
+ receive_extmodule_new_connection.cold.4
+ receive_extmodule_process_request.cold.1
+ receive_extmodule_process_request.cold.2
+ receive_extmodule_process_request.cold.3
+ receive_extmodule_process_request.cold.4
+ receive_legacy_launch.cold.1
+ receive_legacy_launch.cold.2
+ receive_session_close.cold.1
+ receive_session_create.cold.1
+ receive_session_create.cold.2
+ receive_session_create.cold.3
+ receive_session_create.cold.4
+ receive_session_create.cold.5
+ receive_session_process_request.cold.1
+ receive_session_process_request.cold.2
+ receive_session_process_request.cold.3
+ receive_session_process_request.cold.4
+ receive_session_process_request.cold.5
+ receive_session_process_request.cold.6
+ schema_set_callback.cold.1
- __ZN10CMessaging11GetEmptyObjEP8sComData10eValueTypePP7sObject
- __ZN14CSrvrMessaging11GetEmptyObjEP8sComData10eValueTypePP7sObject
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/APIFramework/CDSRefMap.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/APIFramework/CDSRefTable.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/APIFramework/CMessaging.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/APIFramework/DirServices.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/CoreFramework/Private/CFile.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/CHandlers.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/CNodeList.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/CNodeList.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/CPlugInList.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/DirServiceMain.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/ServerControl.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/od_passthru.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/APIFramework/CDSRefMap.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/APIFramework/CDSRefTable.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/APIFramework/CMessaging.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/APIFramework/DirServices.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/CoreFramework/Private/CFile.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/CHandlers.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/CNodeList.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/CNodeList.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/CPlugInList.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/DirServiceMain.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/ServerControl.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/dspluginhelperd/Server/od_passthru.cpp"

```
