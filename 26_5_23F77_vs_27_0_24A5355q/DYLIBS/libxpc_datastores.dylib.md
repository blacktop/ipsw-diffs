## libxpc_datastores.dylib

> `/usr/lib/libxpc_datastores.dylib`

```diff

-3102.120.13.0.0
-  __TEXT.__text: 0x188c
-  __TEXT.__auth_stubs: 0x4e0
+3295.0.0.502.1
+  __TEXT.__text: 0x18a0
   __TEXT.__objc_methlist: 0x194
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x19d
-  __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0xc1
-  __TEXT.__objc_methname: 0x1ed
-  __TEXT.__objc_methtype: 0x158
-  __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0x50
+  __TEXT.__cstring: 0x1a1
+  __TEXT.__unwind_info: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0x50
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_const: 0x670
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x180

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0845C4A5-8156-388B-9203-9B7FEF2A6853
+  UUID: B91EEECD-0EB7-3B6C-830C-F74FA0FA3BFD
   Functions: 43
-  Symbols:   131
-  CStrings:  98
+  Symbols:   135
+  CStrings:  21
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
Functions:
~ __xpc_datastores_service_connection : 84 -> 68
~ __xdo_fetch_ds_data_resp_deserialize : 432 -> 444
~ sub_2a4037084 -> sub_2bea6a080 : 116 -> 132
~ __xpc_datastore_publisher_create_suspended : 212 -> 208
~ __xpc_datastore_publisher_resume : 116 -> 112
~ __xdp_set_ds_data_req_serialize : 244 -> 256
~ __xdp_register_ds_resp_deserialize : 380 -> 392
~ sub_2a40375b0 -> sub_2bea6a5cc : 236 -> 220
~ _xpc_datastore_publisher_create : 488 -> 472
~ _xpc_datastore_publisher_invalidate_state : 256 -> 244
~ sub_2a40379f4 -> sub_2bea6a9e4 : 136 -> 152
~ __xds_fetch_ds_info_resp_deserialize : 380 -> 388
~ sub_2a4037da0 -> sub_2bea6ada8 : 236 -> 244
~ __xpc_datastore_subscriber_initial_handshake : 160 -> 152
~ sub_2a403809c -> sub_2bea6b0a4 : 292 -> 288
~ sub_2a40381c0 -> sub_2bea6b1c4 : 372 -> 388
CStrings:
- "#16@0:8"
- "*"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\"16@0:8"
- "@\"OS_xds_local_cache\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8Q16"
- "@24@0:8r*16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@?"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "I"
- "NSObject"
- "OS_xds_local_cache"
- "OS_xpc_datastore_object"
- "OS_xpc_datastore_publisher"
- "OS_xpc_datastore_subscriber"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "XDS_xpc_datastore_object"
- "XDS_xpc_datastore_publisher"
- "XDS_xpc_datastore_subscriber"
- "^v"
- "^{_NSZone=}16@0:8"
- "activated"
- "autorelease"
- "b1"
- "class"
- "conformsToProtocol:"
- "conn"
- "copyCurrentStateWithReqType:"
- "data"
- "dealloc"
- "debugDescription"
- "description"
- "dq"
- "hash"
- "init"
- "initWithName:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "local_data"
- "lock"
- "pending_work_dq"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "publish_data"
- "recvp"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "size"
- "superclass"
- "v16@0:8"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
