## mobileactivationd

> `/usr/libexec/mobileactivationd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1145.40.5.0.0
-  __TEXT.__text: 0x34acd0
-  __TEXT.__auth_stubs: 0x1240
+1145.40.5.502.1
+  __TEXT.__text: 0x34b39c
+  __TEXT.__auth_stubs: 0x12f0
   __TEXT.__objc_stubs: 0x3240
   __TEXT.__objc_methlist: 0x112c
   __TEXT.__const: 0x60b63
-  __TEXT.__cstring: 0xeec2
+  __TEXT.__cstring: 0xf13f
   __TEXT.__objc_methname: 0x4044
   __TEXT.__oslogstring: 0xf47
   __TEXT.__objc_classname: 0x1a4
   __TEXT.__objc_methtype: 0x1061
-  __TEXT.__gcc_except_tab: 0x1b88
+  __TEXT.__gcc_except_tab: 0x1bcc
   __TEXT.__dlopen_cstrs: 0x294
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x17a0
+  __TEXT.__unwind_info: 0x17b8
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__const: 0x1c4f8
-  __DATA_CONST.__cfstring: 0xd500
+  __DATA_CONST.__const: 0x1c528
+  __DATA_CONST.__cfstring: 0xd620
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_intobj: 0x330
   __DATA_CONST.__objc_arraydata: 0x608
   __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA_CONST.__auth_got: 0x930
-  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__auth_got: 0x988
+  __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x80
   __DATA.__objc_const: 0x1900
   __DATA.__objc_selrefs: 0x10c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1660
-  Symbols:   4048
-  CStrings:  3068
+  Functions: 1664
+  Symbols:   4063
+  CStrings:  3081
 
Symbols:
+ _DRE_SYSTEM_DATA_MOUNT_PATH
+ _IOPSSetBatteryDateOfFirstUseWithPackDetails
+ _NSPOSIXErrorDomain
+ ___block_descriptor_48_e8_32r40r_e63_B24?0r^{container_object_s=}8r^{container_error_extended_s=}16l
+ ___copy_activation_records_directory_path_for_mount_path_block_invoke
+ _container_error_get_message
+ _container_error_get_path
+ _container_error_get_posix_errno
+ _container_get_identifier
+ _container_get_path
+ _container_paths_context_create
+ _container_paths_context_free
+ _container_paths_context_set_class
+ _container_paths_copy_container_root_path_for_context
+ _container_paths_enumerate_containers_at
+ _copy_activation_records_directory_path_for_mount_path
- _IOPSSetBatteryDateOfFirstUse
CStrings:
+ "/private/var/mnt"
+ "1145.40.5.502.1"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1145.40.5.502.1 built on Sep 28 2026 at 21:08:25)"
+ "B24@?0r^{container_object_s=}8r^{container_error_extended_s=}16"
+ "Failed to create a container paths context."
+ "Failed to determine the container root path under %@."
+ "Failed to enumerate the container at %s: %s"
+ "Failed to locate the activation records directory under %@."
+ "Failed to open the container root %s."
+ "Failed to read an activation record under %@."
+ "Missing or invalid system data volume mount path."
+ "No %@ container found under %@."
+ "com.apple.mobileactivationd.containerEnumeration"
+ "copy_activation_records_directory_path_for_mount_path"
+ "copy_activation_records_directory_path_for_mount_path_block_invoke"
+ "iOS Device Activator (MobileActivation-1145.40.5.502.1)"
- "1145.40.5"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1145.40.5 built on Sep 13 2026 at 20:09:15)"
- "iOS Device Activator (MobileActivation-1145.40.5)"
```
