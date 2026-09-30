## libxpc_datastores.dylib

> `/usr/lib/libxpc_datastores.dylib`

```diff

-3089.82.3.0.0
-  __TEXT.__text: 0x1934
-  __TEXT.__auth_stubs: 0x530
+3102.100.97.502.1
+  __TEXT.__text: 0x188c
+  __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x194
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x19d
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__unwind_info: 0xd0
   __TEXT.__objc_classname: 0xc1
   __TEXT.__objc_methname: 0x1ed
   __TEXT.__objc_methtype: 0x158

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_const: 0x670
   __AUTH.__objc_data: 0x140

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3CABBC6C-C519-3AFD-93B9-F9C596944B47
+  UUID: 7276BC1B-D4FF-3E0A-B225-D275EB6FC93C
   Functions: 43
-  Symbols:   136
+  Symbols:   131
   CStrings:  98
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_release_x9
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x8
Functions:
~ __xpc_datastores_service_connection : 68 -> 84
~ __xdo_fetch_ds_data_resp_deserialize : 444 -> 432
~ sub_29e0ea080 -> sub_2a59bb084 : 132 -> 116
~ sub_29e0ea104 -> sub_2a59bb0f8 : 104 -> 80
~ __xpc_datastore_publisher_create_suspended : 224 -> 212
~ __xpc_datastore_publisher_resume : 152 -> 116
~ __xdp_set_ds_data_req_serialize : 256 -> 244
~ __xdp_register_ds_resp_deserialize : 392 -> 380
~ sub_29e0ea61c -> sub_2a59bb5b0 : 220 -> 236
~ _xpc_datastore_publisher_invalidate_state : 244 -> 256
~ sub_29e0ea9d4 -> sub_2a59bb984 : 120 -> 112
~ sub_29e0eaa4c -> sub_2a59bb9f4 : 152 -> 136
~ __xpc_datastore_subscriber_refresh : 260 -> 248
~ __xds_fetch_ds_info_resp_deserialize : 388 -> 380
~ sub_29e0eae1c -> sub_2a59bbda0 : 244 -> 236
~ __xpc_datastore_subscriber_initial_handshake : 152 -> 160
~ __xpc_datastore_subscriber_invalidated : 132 -> 124
~ _xpc_datastore_subscriber_create : 148 -> 140
~ sub_29e0eb128 -> sub_2a59bc09c : 296 -> 292
~ sub_29e0eb250 -> sub_2a59bc1c0 : 396 -> 372

```
