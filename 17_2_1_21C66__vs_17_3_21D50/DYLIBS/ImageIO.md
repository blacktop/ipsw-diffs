## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2488.4.15.0.0
-  __TEXT.__text: 0x3b6be4
-  __TEXT.__auth_stubs: 0x3bd0
+2488.3.8.0.0
+  __TEXT.__text: 0x3b70b8
+  __TEXT.__auth_stubs: 0x3c40
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1bbd0
+  __TEXT.__gcc_except_tab: 0x1bbdc
   __TEXT.__const: 0x28978
-  __TEXT.__cstring: 0x6cbdc
+  __TEXT.__cstring: 0x6ccf8
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xce84
+  __TEXT.__unwind_info: 0xce90
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x3c
   __TEXT.__objc_methname: 0x1260
   __TEXT.__objc_methtype: 0x5f1
   __TEXT.__objc_stubs: 0xfc0
   __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x10c68
+  __DATA_CONST.__const: 0x10c88
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0x478
   __AUTH_CONST.__cfstring: 0xbc60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__const: 0x3d328
+  __AUTH_CONST.__const: 0x3d348
   __AUTH_CONST.__objc_const: 0x120
-  __AUTH_CONST.__auth_got: 0x1e00
+  __AUTH_CONST.__auth_got: 0x1e38
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x1d0
   __DATA.__objc_classrefs: 0x80
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x33b0
-  __DATA.__bss: 0x1030
+  __DATA.__bss: 0x1040
   __DATA.__common: 0x1a5c
   __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__crash_info: 0x40

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 804378B1-31EB-3938-85C1-EECD09038AA0
-  Functions: 12991
-  Symbols:   32598
-  CStrings:  12723
+  UUID: 77170A5B-C819-3417-84AA-BEBB608905F1
+  Functions: 12992
+  Symbols:   32611
+  CStrings:  12730
 
Symbols:
+ __ZZN13IIOReadPlugin19saveDataToXPCObjectEPvE3tok
+ __ZZN13IIOReadPlugin19saveDataToXPCObjectEPvE9onceToken
+ ____ZN13IIOReadPlugin19saveDataToXPCObjectEPv_block_invoke
+ ___block_descriptor_tmp.167
+ ___block_descriptor_tmp.77
+ ___block_literal_global.79
+ _mach_error_string
+ _mach_make_memory_entry_64
+ _mach_memory_entry_ownership
+ _mach_port_deallocate
+ _task_create_identity_token
+ _xpc_dictionary_copy_mach_send
+ _xpc_dictionary_set_mach_send
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.157
- ___block_descriptor_tmp.165
- ___block_descriptor_tmp.169
- ___block_literal_global.167
CStrings:
+ "*** ERROR: bad makerNote length: %d\n"
+ "*** ERROR: encoded PNG larger than expected (%ld > %ld)\n"
+ "*** ERROR: mach_make_memory_entry_64: %s"
+ "*** ERROR: mach_memory_entry_ownership: %s"
+ "*** ERROR: task_create_identity_token: %s"
+ "iio_xpc_plugin_client_identity"
+ "saveDataToXPCObject_block_invoke"

```
