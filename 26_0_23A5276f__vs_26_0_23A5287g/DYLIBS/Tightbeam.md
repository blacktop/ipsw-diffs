## Tightbeam

> `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`

```diff

-483.0.12.0.0
-  __TEXT.__text: 0x27c10
-  __TEXT.__auth_stubs: 0x1120
+483.0.17.0.1
+  __TEXT.__text: 0x28018
+  __TEXT.__auth_stubs: 0x1130
   __TEXT.__const: 0x1bca
   __TEXT.__cstring: 0x31b0
   __TEXT.__constg_swiftt: 0x13b8

   __TEXT.__oslogstring: 0x16e
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_types2: 0x18
-  __TEXT.__unwind_info: 0xb48
+  __TEXT.__unwind_info: 0xb40
   __TEXT.__eh_frame: 0x8a0
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x1ff

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__auth_got: 0x8a0
   __AUTH_CONST.__const: 0x28f8
   __AUTH_CONST.__objc_const: 0x1058
   __DATA.__data: 0x4d0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6306C24D-CAF4-362C-9C93-8A61EDE91A7A
+  UUID: 46E8B203-2548-3F78-B8EC-7B75F46D5CFB
   Functions: 1381
   Symbols:   1554
   CStrings:  289
Symbols:
+ ___strlcpy_chk
- _strncpy
Functions:
~ __tb_delegated_c_service_transport_create : 80 -> 100
~ _tb_delegated_c_request_handler : 336 -> 352
~ _tb_null_transport_create_inplace_with_endpoint : 56 -> 72
~ _tb_null_transport_create : 104 -> 124
~ __tb_null_transport_send_message : 536 -> 576
~ __tb_delegated_c_client_transport_create : 88 -> 112
~ __tb_delegated_c_client_transport_send_message : 236 -> 256
~ _tb_message_initialize : 40 -> 60
~ _tb_message_construct : 76 -> 116
~ _tb_message_reset : 36 -> 68
~ _tb_message_get_capability : 36 -> 44
~ _tb_message_encode_capability : 48 -> 72
~ _tb_message_decode_capability : 136 -> 144
~ _tb_message_encode_bool : 124 -> 136
~ _tb_message_raw_encode_bool : 64 -> 76
~ _tb_message_encode_u8 : 124 -> 136
~ _tb_message_raw_encode_u8 : 64 -> 76
~ _tb_message_encode_u16 : 128 -> 140
~ _tb_message_raw_encode_u16 : 68 -> 80
~ _tb_message_encode_u32 : 128 -> 140
~ _tb_message_raw_encode_u32 : 68 -> 80
~ _tb_message_encode_u64 : 128 -> 140
~ _tb_message_raw_encode_u64 : 68 -> 80
~ _tb_message_encode_s8 : 124 -> 136
~ _tb_message_raw_encode_s8 : 64 -> 76
~ _tb_message_encode_s16 : 128 -> 140
~ _tb_message_raw_encode_s16 : 68 -> 80
~ _tb_message_encode_s32 : 128 -> 140
~ _tb_message_raw_encode_s32 : 68 -> 80
~ _tb_message_encode_s64 : 128 -> 140
~ _tb_message_raw_encode_s64 : 68 -> 80
~ _tb_message_encode_f32_v2 : 164 -> 176
~ _tb_message_raw_encode_f32_v2 : 104 -> 116
~ _tb_message_encode_f64_v2 : 164 -> 176
~ _tb_message_raw_encode_f64_v2 : 104 -> 116
~ _tb_message_encode_buffer : 128 -> 152
~ _tb_message_decode_bool : 128 -> 124
~ _tb_message_raw_decode_bool : 64 -> 60
~ _tb_message_decode_buffer : 136 -> 156
~ __tb_connection_create : 88 -> 104
~ _tb_service_connection_create : 160 -> 172
~ ___tb_service_connection_create_block_invoke : 480 -> 536
~ _tb_client_connection_create_with_endpoint_static : 88 -> 104
~ _tb_mach_service_transport_create : 284 -> 308
~ _tb_mach_client_transport_create : 244 -> 268
~ ____tb_mach_transport_create_block_invoke : 596 -> 628
~ __tb_unpack_dispatch_mach_msg_to_tb_message : 228 -> 248
~ __tb_mach_transport_send_message : 364 -> 388
~ __tb_darwin_transport_construct_message_buffer : 124 -> 140
~ _tb_message_accumulator_accumulate : 552 -> 604
~ _tb_message_splitter_send : 796 -> 788
~ _tb_reply_splitter_add_reply : 540 -> 552
~ _tb_reply_splitter_next_message : 316 -> 332
~ _tb_transport_initialize_message_buffer : 44 -> 72
~ _tb_transport_message_buffer_deep_copy : 116 -> 144
~ __tb_forwarding_connection_create : 260 -> 272
~ __tb_forwarding_connection_message_forward : 556 -> 572
~ __iterate_list : 116 -> 132
~ _tb_list_create : 80 -> 96
~ _tb_list_add : 148 -> 172
~ sub_275819210 -> sub_275d82620 : 248 -> 240

```
