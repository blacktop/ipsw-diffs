## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

-8140.3.0.0.0
-  __TEXT.__text: 0xfda9c
+8140.4.0.0.0
+  __TEXT.__text: 0xfdd3c
   __TEXT.__auth_stubs: 0x1ae0
   __TEXT.__objc_stubs: 0x4c80
   __TEXT.__init_offsets: 0x1f20
-  __TEXT.__objc_methlist: 0x3f88
+  __TEXT.__objc_methlist: 0x3fb0
   __TEXT.__const: 0x3e1e
-  __TEXT.__gcc_except_tab: 0xd774
+  __TEXT.__gcc_except_tab: 0xd7d0
   __TEXT.__cstring: 0x9825
-  __TEXT.__oslogstring: 0x3047
+  __TEXT.__oslogstring: 0x3081
   __TEXT.__objc_methname: 0x566d
   __TEXT.__objc_classname: 0xb07
   __TEXT.__objc_methtype: 0x6fa2
-  __TEXT.__unwind_info: 0x5358
+  __TEXT.__unwind_info: 0x5370
   __DATA_CONST.__auth_got: 0xd80
   __DATA_CONST.__got: 0x290
   __DATA_CONST.__auth_ptr: 0x20

   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_intobj: 0x450
   __DATA_CONST.__objc_floatobj: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7029
-  Symbols:   33072
-  CStrings:  3149
+  Functions: 7032
+  Symbols:   33089
+  CStrings:  3151
 
Symbols:
+ -[HSTPadFirmwareManager _handleVendorEvent:]
+ -[HSTPadFirmwareManager _restoreFirmwareState]
+ -[HSTPadFirmwareManager handleConsume:]
+ __cxx_global_var_init.183
- __cxx_global_var_init.181
CStrings:
+ "8140.4"
+ "Restoring firmware"
+ "iPad handle device ready in state 0x%x"
- "8140.3"

```
