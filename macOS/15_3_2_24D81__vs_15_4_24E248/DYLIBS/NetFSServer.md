## NetFSServer

> `/System/Library/PrivateFrameworks/NetFSServer.framework/Versions/A/NetFSServer`

```diff

 61.0.0.0.0
-  __TEXT.__text: 0x3fa4
+  __TEXT.__text: 0x4390
   __TEXT.__auth_stubs: 0x5a0
   __TEXT.__cstring: 0x580
   __TEXT.__const: 0x60
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__unwind_info: 0x178
   __TEXT.__objc_classname: 0xc
-  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/Frameworks/ServiceManagement.framework/Versions/A/ServiceManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B937361-36AE-32F4-8773-75C9399C3C59
-  Functions: 109
-  Symbols:   238
+  UUID: 1C84DA92-BDAE-33A3-B0C5-1F89198A0888
+  Functions: 107
+  Symbols:   236
   CStrings:  61
 
Symbols:
- _nsc_ops
- _nsc_service
Functions:
~ _nsc_server_isenabled : 48 -> 108
- _nsc_service
- _nsc_ops
~ _send_request_get_reply : 224 -> 232
~ _connect_to_server : 176 -> 188
~ _nsc_supported : 32 -> 100
~ _nsc_server_enable : 64 -> 136
~ _nsc_server_disable : 64 -> 136
~ _nsc_server_status : 96 -> 156
~ _nsc_server_isrunning : 60 -> 120
~ _nsc_server_shutdown : 184 -> 284
~ _nsc_server_shutdown_delay : 136 -> 236
~ _nsc_server_shutdown_cancel : 84 -> 144
~ _nsc_server_update : 64 -> 136
~ _nsc_shares_get : 96 -> 156
~ _nsc_sessions_get : 148 -> 248
~ _nsc_sessions_disconnect : 144 -> 200
~ _nsc_sessions_count : 136 -> 236
~ _nsc_server_guest_access : 92 -> 164
~ _get_pid : 244 -> 248
~ _get_sorted_active_user_list : 372 -> 384
~ _free_nfs_export_list : 120 -> 104
~ _alloc_and_copy : 96 -> 112
~ _send_request_noreply : 188 -> 204
~ __SCRPIGetServerAttribute : 464 -> 468
~ __SCRPISetServerAttribute : 420 -> 424
~ __SCRPISendServerCommand : 484 -> 488
~ __SCRPICreateObjectIter : 372 -> 376
~ __SCRPIGetIterAttribute : 476 -> 480
~ __SCRPIAdvanceIterator : 320 -> 324
~ __SCRPIDestroyIterator : 320 -> 324
~ __SCRPIRegisterNotiferPort : 448 -> 452

```
