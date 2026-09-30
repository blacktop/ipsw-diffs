## nehelper

> `/usr/libexec/nehelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2340.0.0.0.4
-  __TEXT.__text: 0x25328
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_stubs: 0x2a60
+2365.40.1.0.0
+  __TEXT.__text: 0x255b8
+  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__objc_stubs: 0x2a80
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0x7f8
-  __TEXT.__objc_methname: 0x1f9c
-  __TEXT.__cstring: 0x5f44
-  __TEXT.__oslogstring: 0x4a97
+  __TEXT.__objc_methname: 0x1fc7
+  __TEXT.__cstring: 0x5ff2
+  __TEXT.__oslogstring: 0x4ac1
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x26e
-  __TEXT.__unwind_info: 0x4b0
-  __DATA_CONST.__const: 0xd10
-  __DATA_CONST.__cfstring: 0x51a0
+  __TEXT.__unwind_info: 0x4b8
+  __DATA_CONST.__const: 0xcf0
+  __DATA_CONST.__cfstring: 0x51c0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x1350
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__auth_got: 0x870
+  __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x1788
-  __DATA.__objc_selrefs: 0xb38
+  __DATA.__objc_selrefs: 0xb40
   __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xc8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 247
-  Symbols:   382
-  CStrings:  1700
+  Functions: 248
+  Symbols:   384
+  CStrings:  1707
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _xpc_copy
CStrings:
+ "Error deserializing trusted user info: %@"
+ "LaunchServices"
+ "PreserveExistingConnections"
+ "com.apple.distnoted.matching.trusted"
+ "com.apple.networkextension.preserve-existing-connections"
+ "propertyListWithData:options:format:error:"
+ "restricted_distributed_notifications"
```
