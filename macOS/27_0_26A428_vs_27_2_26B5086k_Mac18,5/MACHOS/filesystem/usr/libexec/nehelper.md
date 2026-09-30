## nehelper

> `/usr/libexec/nehelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2340.1.2.0.0
-  __TEXT.__text: 0x2235c
-  __TEXT.__auth_stubs: 0xe10
+2365.40.1.0.0
+  __TEXT.__text: 0x22610
+  __TEXT.__auth_stubs: 0xe20
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_stubs: 0x2340
+  __TEXT.__objc_stubs: 0x2360
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x12c
   __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__objc_methname: 0x1c16
-  __TEXT.__cstring: 0x3146
-  __TEXT.__oslogstring: 0x4059
+  __TEXT.__objc_methname: 0x1c41
+  __TEXT.__cstring: 0x31f4
+  __TEXT.__oslogstring: 0x4083
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x280
   __TEXT.__unwind_info: 0x498
-  __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__cfstring: 0x2300
+  __DATA_CONST.__const: 0xcd0
+  __DATA_CONST.__cfstring: 0x2320
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x610
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x718
-  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__auth_got: 0x720
+  __DATA_CONST.__got: 0x2a8
   __DATA.__objc_const: 0x17c8
-  __DATA.__objc_selrefs: 0x970
+  __DATA.__objc_selrefs: 0x978
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xcc

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 240
-  Symbols:   305
-  CStrings:  1235
+  Functions: 241
+  Symbols:   307
+  CStrings:  1242
 
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
