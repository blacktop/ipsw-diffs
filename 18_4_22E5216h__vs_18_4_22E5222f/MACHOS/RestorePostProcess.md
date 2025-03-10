## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2624.100.98.0.0
-  __TEXT.__text: 0x153b8
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x26e0
-  __TEXT.__objc_methlist: 0xd0c
+2624.100.102.0.0
+  __TEXT.__text: 0x15754
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_stubs: 0x2700
+  __TEXT.__objc_methlist: 0xd24
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x3b95
-  __TEXT.__objc_methname: 0x2f27
+  __TEXT.__cstring: 0x3c65
+  __TEXT.__objc_methname: 0x2f72
   __TEXT.__objc_classname: 0x128
   __TEXT.__objc_methtype: 0x61f
-  __TEXT.__oslogstring: 0x2547
-  __TEXT.__gcc_except_tab: 0x2a0
+  __TEXT.__oslogstring: 0x25b7
+  __TEXT.__gcc_except_tab: 0x314
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0xe4
   __TEXT.__swift5_reflstr: 0x8c

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__unwind_info: 0x490
   __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__auth_ptr: 0x128
   __DATA_CONST.__const: 0x820
-  __DATA_CONST.__cfstring: 0xfc0
+  __DATA_CONST.__cfstring: 0x1000
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x1420
-  __DATA.__objc_selrefs: 0xd00
+  __DATA.__objc_selrefs: 0xd18
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x560
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 389
-  Symbols:   310
-  CStrings:  1157
+  Functions: 391
+  Symbols:   318
+  CStrings:  1168
 
Symbols:
+ _container_copy_from_path
+ _container_delete_all_container_content
+ _container_free_object
+ _container_get_error_description
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_terminate
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
