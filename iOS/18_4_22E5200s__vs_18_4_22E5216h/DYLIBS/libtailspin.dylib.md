## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

-218.0.0.0.0
-  __TEXT.__text: 0x1e06c
-  __TEXT.__auth_stubs: 0xfd0
+218.1.0.0.0
+  __TEXT.__text: 0x1eb34
+  __TEXT.__auth_stubs: 0x1060
   __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__const: 0x171
-  __TEXT.__cstring: 0x1a6d
-  __TEXT.__oslogstring: 0x223a
-  __TEXT.__gcc_except_tab: 0x111c
+  __TEXT.__const: 0x189
+  __TEXT.__cstring: 0x1ae6
+  __TEXT.__oslogstring: 0x2433
+  __TEXT.__gcc_except_tab: 0x1274
   __TEXT.__ustring: 0x6
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__unwind_info: 0x720
+  __TEXT.__unwind_info: 0x790
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methname: 0x108d
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__const: 0x958
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4c8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__auth_got: 0x848
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__cfstring: 0x1a40
   __AUTH_CONST.__objc_const: 0x2a0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x10

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 492
-  Symbols:   506
-  CStrings:  661
+  Functions: 504
+  Symbols:   519
+  CStrings:  676
 
Symbols:
+ _TSPMetadata_SharedCacheInfo
+ _TSPMetadata_SharedCacheResidentSize
+ _TSPMetadata_SharedCacheVirtualSize
+ _dyld_process_create_for_current_task
+ _dyld_process_dispose
+ _dyld_process_snapshot_create_for_process
+ _dyld_process_snapshot_dispose
+ _dyld_process_snapshot_get_shared_cache
+ _dyld_shared_cache_for_each_file
+ _mach_error_string
+ _mincore
+ _mmap
+ _munmap
+ _vm_page_size
- _objc_retain_x28
CStrings:
+ "MAX_CHUNK_SIZE 0x%x isn't a page multiple 0x%lx"
+ "SharedCacheInfo"
+ "SharedCacheSizeResident"
+ "SharedCacheSizeVirtual"
+ "failed to create dyld process:%d (%s)"
+ "failed to create snapshot of the process:%d (%s)"
+ "failed to fstat shared cache file %s: %{errno}d"
+ "failed to get shared cache"
+ "failed to open shared cache file %s: %{errno}d"
+ "mincore of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "mmap of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "munmap of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "native shared cache has %llu/%llu pages resident"
+ "shared cache file %s has %llu/%llu pages resident"
+ "v16@?0r*8"

```
