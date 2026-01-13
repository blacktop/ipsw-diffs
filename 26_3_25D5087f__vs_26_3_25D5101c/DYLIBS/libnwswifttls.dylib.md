## libnwswifttls.dylib

> `/usr/lib/libnwswifttls.dylib`

```diff

-108.80.1.0.0
-  __TEXT.__text: 0xd68fc
-  __TEXT.__auth_stubs: 0x1f60
+108.80.2.0.0
+  __TEXT.__text: 0xd6a1c
+  __TEXT.__auth_stubs: 0x1fa0
   __TEXT.__objc_methlist: 0x5ac
   __TEXT.__const: 0x70c4
   __TEXT.__cstring: 0x19c6

   __TEXT.__swift5_protos: 0x14
   __TEXT.__unwind_info: 0x2628
   __TEXT.__eh_frame: 0x41dc
-  __TEXT.__objc_classname: 0xf1
-  __TEXT.__objc_methname: 0x101d
-  __TEXT.__objc_methtype: 0x3de
+  __TEXT.__objc_classname: 0xf2
+  __TEXT.__objc_methname: 0x101c
+  __TEXT.__objc_methtype: 0x312
   __TEXT.__objc_stubs: 0x780
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f8
+  __DATA_CONST.__objc_selrefs: 0x300
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xfc0
+  __AUTH_CONST.__auth_got: 0xfe0
   __AUTH_CONST.__const: 0x3328
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x2070

   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x16a8
   __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x2a8
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E5BBFCAC-80EB-331C-86A8-6BF9AF6672CB
+  UUID: 4DA725C4-6A8A-38B7-8BBE-F76E12D5E3B2
   Functions: 3384
-  Symbols:   7939
-  CStrings:  755
+  Symbols:   7943
+  CStrings:  754
 
Symbols:
+ -[NWConcrete_nwswifttls destroy]
+ OBJC_IVAR_$_NWConcrete_nwswifttls.internal_reference
+ ___32-[NWConcrete_nwswifttls destroy]_block_invoke
+ _nw_protocol_disconnect_is_valid
+ _nw_protocol_disconnected
+ _nw_protocol_get_parameters_is_valid
+ _nw_protocol_get_remote_endpoint
+ _nw_protocol_remove_input_handler
+ _nw_protocol_remove_input_handler_is_valid
- -[NWConcrete_nwswifttls dealloc]
- OBJC_IVAR_$_NWConcrete_nwswifttls.protocol
- ___32-[NWConcrete_nwswifttls dealloc]_block_invoke
- _nw_protocol_register
- _uuid_copy
Functions:
~ -[NWConcrete_nwswifttls dealloc] -> -[NWConcrete_nwswifttls destroy] : 88 -> 24
~ _nwswifttls_disconnect : 108 -> 124
~ ___nwswifttls_identifier_block_invoke : 304 -> 352
~ _nwswifttls_add_input_handler : 272 -> 348
~ _nwswifttls_remove_input_handler : 380 -> 440
~ _nwswifttls_input_available : 332 -> 344
~ _nwswifttls_copy_info : 188 -> 208
~ _nwswifttls_create : 148 -> 168
~ _nwswifttls_complete_handshake : 132 -> 160
~ _nwswifttls_send_error : 160 -> 184
~ _nwswifttls_add_message : 380 -> 412
~ _nwswifttls_send_messages : 160 -> 152
~ _nwswifttls_send_alert : 128 -> 152
~ _nwswifttls_configure_server_name : 524 -> 520
~ _nwswifttlsrecord_configure_server_name : 524 -> 520
~ _nwswifttls_configure_with_sec_protocol_options : 208 -> 216
CStrings:
+ "destroy"
- "protocol"
- "{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}"

```
