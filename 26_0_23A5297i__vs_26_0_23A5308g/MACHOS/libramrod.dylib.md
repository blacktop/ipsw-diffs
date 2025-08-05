## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3476.0.38.0.0
-  __TEXT.__text: 0xd9110
-  __TEXT.__auth_stubs: 0x2820
+3476.0.46.0.0
+  __TEXT.__text: 0xd9350
+  __TEXT.__auth_stubs: 0x2830
   __TEXT.__objc_methlist: 0x1164
-  __TEXT.__cstring: 0x285de
+  __TEXT.__cstring: 0x286e1
   __TEXT.__const: 0x94960
   __TEXT.__gcc_except_tab: 0xbb4
   __TEXT.__oslogstring: 0x9e5
-  __TEXT.__unwind_info: 0x1c78
+  __TEXT.__unwind_info: 0x1c90
   __TEXT.__eh_frame: 0x3c0
   __TEXT.__objc_classname: 0x195
-  __TEXT.__objc_methname: 0x28ee
+  __TEXT.__objc_methname: 0x2901
   __TEXT.__objc_methtype: 0xb70
-  __TEXT.__objc_stubs: 0x2820
+  __TEXT.__objc_stubs: 0x2840
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__const: 0x1f80
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc88
-  __AUTH_CONST.__auth_got: 0x1428
+  __DATA_CONST.__objc_selrefs: 0xc90
+  __AUTH_CONST.__auth_got: 0x1430
   __AUTH_CONST.__const: 0x1fd0
-  __AUTH_CONST.__cfstring: 0xb4e0
+  __AUTH_CONST.__cfstring: 0xb500
   __AUTH_CONST.__objc_const: 0x1aa0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x5a0

   - /usr/lib/libpartition2_dynamic.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 675FA07C-35AC-3C27-97D7-7D681A310975
-  Functions: 2589
-  Symbols:   1789
-  CStrings:  7330
+  UUID: 9D661A11-236A-3749-840A-072F23AAB5F6
+  Functions: 2593
+  Symbols:   1794
+  CStrings:  7336
 
Symbols:
+ _APFSContainerWaitForReaper
+ _ramrod_socket_get_error
+ _ramrod_socket_recv
+ _ramrod_socket_send
+ _ramrod_stash_info_to_file
CStrings:
+ "%s: Attempting to read the current file so we can modify it\n"
+ "%s: Creating directory(%@) to save current state\n"
+ "%s: Directory(%@) doesn't exist but a file exists with the same name at that location. Cannot proceed.\n"
+ "%s: Failed to allocate path string to save persisted state\n"
+ "%s: Failed to allocate string for the stashed file path\n"
+ "%s: Failed to create directory. Error: %@\n"
+ "%s: Failed to delete persisted file at %@. Error: %@"
+ "%s: Failed to set permissions on stashed file..Deleting it\n"
+ "%s: No existing file\n"
+ "%s: Saving data to %@\n"
+ "%s: Stashing info to mount:%s dir:%s file:%s\n"
+ "APFSContainerWaitForReaper(%s) completed\n"
+ "APFSContainerWaitForReaper(%s) failed: %d (%s)\n"
+ "APFSContainerWaitForReaper(%s) running...\n"
+ "ramrod_stash_info_to_file"
+ "sock %3d: recv(%lu) failed: %s"
+ "sock %3d: recv(%lu) failed: connection closed"
+ "sock %3d: send(%lu) failed: %s"
+ "stringWithCString:"
- "%@/%s"
- "%s: Creating directory(%@) to save current OS state"
- "%s: Failed to allocate path string to save Booted OS state\n"
- "%s: Failed to allocate string to save the path for the state file\n"
- "%s: Failed to create directory : %@"
- "%s: Failed to delete BootedOsState file at %@. Error: %@"
- "%s: Failed to set permissions on BootedOSState file..Deleting it"
- "%s: No exiting file\n"
- "%s: Read the current file so we can modify it\n"
- "%s: Saving env data to %@"
- "ramrod_write_os_info_for_nerd"
- "sock %3d: recv(%d, %lu) failed: %s"
- "sock %3d: recv(%d, %lu) failed: connection closed"
- "sock %3d: send(%d, %lu) failed: %s"

```
