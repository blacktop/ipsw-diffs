## ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

-2488.4.15.0.0
-  __TEXT.__text: 0x416048
-  __TEXT.__auth_stubs: 0x4290
+2488.3.8.0.0
+  __TEXT.__text: 0x4165cc
+  __TEXT.__auth_stubs: 0x4300
   __TEXT.__objc_stubs: 0xfe0
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1f534
+  __TEXT.__gcc_except_tab: 0x1f540
   __TEXT.__const: 0x2a770
-  __TEXT.__cstring: 0x7769e
+  __TEXT.__cstring: 0x777f1
   __TEXT.__objc_methname: 0x1272
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methtype: 0x5f1
   __TEXT.__oslogstring: 0x1ee
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xecb4
+  __TEXT.__unwind_info: 0xecbc
   __TEXT.__eh_frame: 0x1068
-  __DATA_CONST.__auth_got: 0x2160
+  __DATA_CONST.__auth_got: 0x2198
   __DATA_CONST.__got: 0x640
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x71628
+  __DATA_CONST.__const: 0x71668
   __DATA_CONST.__cfstring: 0xbf40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x3200
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x11728
+  __DATA.__bss: 0x11738
   __DATA.__common: 0x29bc
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 26399B1B-E4D7-3146-9367-59D031B4DC42
-  Functions: 16105
-  Symbols:   10761
-  CStrings:  14092
+  UUID: 31C654ED-EF6C-329E-B888-8DE05FE208EA
+  Functions: 16106
+  Symbols:   10768
+  CStrings:  14100
 
Symbols:
+ _mach_error_string
+ _mach_make_memory_entry_64
+ _mach_memory_entry_ownership
+ _mach_port_deallocate
+ _task_create_identity_token
+ _xpc_dictionary_copy_mach_send
+ _xpc_dictionary_set_mach_send
CStrings:
+ "*** ERROR: OWNERLESS SERVER ALLOCATION: %s, %llu bytes"
+ "*** ERROR: bad makerNote length: %d\n"
+ "*** ERROR: encoded PNG larger than expected (%ld > %ld)\n"
+ "*** ERROR: mach_make_memory_entry_64: %s"
+ "*** ERROR: mach_memory_entry_ownership: %s"
+ "*** ERROR: task_create_identity_token: %s"
+ "iio_xpc_plugin_client_identity"
+ "saveDataToXPCObject_block_invoke"

```
