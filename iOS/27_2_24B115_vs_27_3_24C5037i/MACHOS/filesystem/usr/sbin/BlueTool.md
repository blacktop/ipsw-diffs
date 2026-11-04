## BlueTool

> `/usr/sbin/BlueTool`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2701.4.0.0.0
-  __TEXT.__text: 0x4c5a0
-  __TEXT.__auth_stubs: 0xc10
+2702.1.0.0.0
+  __TEXT.__text: 0x4c77c
+  __TEXT.__auth_stubs: 0xc40
   __TEXT.__objc_stubs: 0x2e0
   __TEXT.__init_offsets: 0x59c
   __TEXT.__const: 0x47c600
-  __TEXT.__cstring: 0xecc3
-  __TEXT.__oslogstring: 0x4844
+  __TEXT.__cstring: 0xecdf
+  __TEXT.__oslogstring: 0x488b
   __TEXT.__objc_methname: 0x1c0
-  __TEXT.__unwind_info: 0x2798
-  __DATA_CONST.__const: 0x6ca8
+  __TEXT.__unwind_info: 0x27b0
+  __DATA_CONST.__const: 0x6ce8
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x610
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_got: 0x628
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_selrefs: 0xb8
   __DATA.__data: 0x990

   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2614
-  Symbols:   226
-  CStrings:  1941
+  Functions: 2618
+  Symbols:   230
+  CStrings:  1943
 
Symbols:
+ __xpc_type_bool
+ _xpc_bool_get_value
+ _xpc_connection_copy_entitlement_value
+ _xpc_connection_get_pid
CStrings:
+ "Rejecting XPC message from pid %d: missing com.apple.bluetooth.control"
+ "com.apple.bluetooth.control"
```
