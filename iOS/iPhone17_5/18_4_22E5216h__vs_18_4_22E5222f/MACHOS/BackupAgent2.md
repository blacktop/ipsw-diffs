## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2624.100.98.0.0
-  __TEXT.__text: 0xa6930
-  __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_stubs: 0xe300
-  __TEXT.__objc_methlist: 0x7440
+2624.100.102.0.0
+  __TEXT.__text: 0xa6cd4
+  __TEXT.__auth_stubs: 0x1a40
+  __TEXT.__objc_stubs: 0xe320
+  __TEXT.__objc_methlist: 0x7468
   __TEXT.__const: 0x4b0
-  __TEXT.__cstring: 0x1e20e
-  __TEXT.__oslogstring: 0xe800
-  __TEXT.__objc_methname: 0x10d09
+  __TEXT.__cstring: 0x1e2d4
+  __TEXT.__oslogstring: 0xe870
+  __TEXT.__objc_methname: 0x10d54
   __TEXT.__objc_classname: 0xb4e
   __TEXT.__objc_methtype: 0x2385
-  __TEXT.__gcc_except_tab: 0x28e8
-  __TEXT.__unwind_info: 0x1da0
-  __DATA_CONST.__auth_got: 0xd10
+  __TEXT.__gcc_except_tab: 0x295c
+  __TEXT.__unwind_info: 0x1db0
+  __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x560
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x16f8
-  __DATA_CONST.__cfstring: 0xb760
+  __DATA_CONST.__cfstring: 0xb7a0
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0xb248
-  __DATA.__objc_selrefs: 0x4760
+  __DATA.__objc_const: 0xb258
+  __DATA.__objc_selrefs: 0x4778
   __DATA.__objc_ivar: 0x68c
   __DATA.__objc_data: 0x2710
   __DATA.__data: 0x8d8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2941
-  Symbols:   603
-  CStrings:  8016
+  Functions: 2944
+  Symbols:   607
+  CStrings:  8027
 
Symbols:
+ _container_copy_from_path
+ _container_delete_all_container_content
+ _container_free_object
+ _container_get_error_description
CStrings:
+ "Failed to reset container at %@: %s"
+ "No container found to reset at path %@"
+ "Reset container %s with root path %@"
+ "containerIDForPath:error:"
+ "container_copy_from_path failed: %s"
+ "container_delete_all_container_content failed: %s"
+ "resetContainerWithRoot:error:"
+ "stringWithCString:"

```
