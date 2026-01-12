## libnwswifttls.dylib

> `/usr/lib/libnwswifttls.dylib`

```diff

-108.80.1.0.0
-  __TEXT.__text: 0xd1090
-  __TEXT.__auth_stubs: 0x2100
+108.80.2.0.0
+  __TEXT.__text: 0xd1188
+  __TEXT.__auth_stubs: 0x2140
   __TEXT.__objc_methlist: 0x5ac
   __TEXT.__const: 0x70d4
   __TEXT.__cstring: 0x19c6

   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_mpenum: 0x60
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2668
+  __TEXT.__unwind_info: 0x2660
   __TEXT.__eh_frame: 0x40bc
-  __TEXT.__objc_classname: 0xf1
-  __TEXT.__objc_methname: 0x101d
-  __TEXT.__objc_methtype: 0x3de
+  __TEXT.__objc_classname: 0xf2
+  __TEXT.__objc_methname: 0x101c
+  __TEXT.__objc_methtype: 0x312
   __TEXT.__objc_stubs: 0x780
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x460
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f8
+  __DATA_CONST.__objc_selrefs: 0x300
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1090
+  __AUTH_CONST.__auth_got: 0x10b0
   __AUTH_CONST.__const: 0x3028
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x2070

   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x16d0
   __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x2a8
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 623B5D97-086B-3CA2-9108-3D78D73B7FB3
+  UUID: 6541E53E-3513-3896-8729-6670D0CFFE5A
   Functions: 3350
-  Symbols:   12172
-  CStrings:  755
+  Symbols:   12176
+  CStrings:  754
 
Symbols:
+ -[NWConcrete_nwswifttls destroy]
+ _OBJC_IVAR_$_NWConcrete_nwswifttls.internal_reference
+ ___32-[NWConcrete_nwswifttls destroy]_block_invoke
+ _nw_protocol_disconnect_is_valid
+ _nw_protocol_disconnected
+ _nw_protocol_get_parameters_is_valid
+ _nw_protocol_get_remote_endpoint
+ _nw_protocol_remove_input_handler
+ _nw_protocol_remove_input_handler_is_valid
- -[NWConcrete_nwswifttls dealloc]
- _OBJC_IVAR_$_NWConcrete_nwswifttls.protocol
- ___32-[NWConcrete_nwswifttls dealloc]_block_invoke
- _nw_protocol_register
- _uuid_copy
Functions:
~ _nwswifttls_create : 140 -> 152
~ _nwswifttls_add_input_handler : 248 -> 320
~ _nwswifttls_connected : 1484 -> 1480
~ _nwswifttls_configure_with_sec_protocol_options : 200 -> 204
~ _nwswifttls_configure_server_name : 468 -> 464
~ _nwswifttls_input_available : 324 -> 332
~ _nwswifttls_disconnect : 120 -> 128
~ _nwswifttls_add_message : 368 -> 400
~ _nwswifttls_send_messages : 156 -> 148
~ _nwswifttls_copy_info : 184 -> 200
~ _nwswifttls_complete_handshake : 152 -> 176
~ ___nwswifttls_identifier_block_invoke : 304 -> 352
~ -[NWConcrete_nwswifttls dealloc] -> -[NWConcrete_nwswifttls destroy] : 88 -> 24
~ _nwswifttls_remove_input_handler : 376 -> 428
~ _nwswifttls_send_error : 164 -> 192
~ _nwswifttls_send_alert : 132 -> 160
~ _nwswifttlsrecord_configure_server_name : 468 -> 464
CStrings:
+ "destroy"
- "protocol"
- "{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}"

```
