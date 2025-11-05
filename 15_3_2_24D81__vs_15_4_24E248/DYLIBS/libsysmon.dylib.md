## libsysmon.dylib

> `/usr/lib/libsysmon.dylib`

```diff

-130.0.0.0.0
-  __TEXT.__text: 0x184c
+131.0.0.0.0
+  __TEXT.__text: 0x1850
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x4c
+  __TEXT.__objc_methlist: 0x154
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x150
   __TEXT.__oslogstring: 0xb2

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__objc_const: 0x6f8
+  __AUTH_CONST.__objc_const: 0x508
   __AUTH.__objc_data: 0x140
   __DATA.__data: 0x218
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B59584A4-2F5F-340E-AD85-4C41FC6FDAE2
+  UUID: 9F054DBB-5A54-3CEA-9AD5-8ECE424F3419
   Functions: 51
   Symbols:   184
   CStrings:  64
Functions:
~ _sysmon_request_set_interval : 88 -> 80
~ ___sysmon_request_execute_block_invoke : 612 -> 616
~ __sysmon_request_invoke_client_handler : 236 -> 240
~ _sysmon_table_apply : 96 -> 100
~ ____bitarray_index_of_bit_block_invoke : 92 -> 96
~ ____sysmon_attr_index_block_invoke : 92 -> 88

```
