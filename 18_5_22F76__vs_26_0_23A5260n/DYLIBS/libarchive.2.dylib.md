## libarchive.2.dylib

> `/usr/lib/libarchive.2.dylib`

```diff

-149.0.0.0.0
-  __TEXT.__text: 0xe1a64
-  __TEXT.__auth_stubs: 0x10c0
+156.0.0.0.0
+  __TEXT.__text: 0xe1d54
+  __TEXT.__auth_stubs: 0x1100
   __TEXT.__const: 0x932c
-  __TEXT.__cstring: 0x9cb0
-  __TEXT.__unwind_info: 0xba8
+  __TEXT.__cstring: 0x9d44
+  __TEXT.__unwind_info: 0xb58
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x1a10
-  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_got: 0x880
   __AUTH_CONST.__const: 0xd48
   __DATA.__data: 0xc
-  __DATA.__bss: 0x1438
+  __DATA.__bss: 0x1440
   __DATA_DIRTY.__bss: 0xb4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B7C5C2A6-36E1-3490-86A9-E150FEDC168A
-  Functions: 2237
-  Symbols:   4482
-  CStrings:  1814
+  UUID: 74B60CDB-CDA9-3DFE-BAAA-7BA48CCF9B9E
+  Functions: 2241
+  Symbols:   4495
+  CStrings:  1818
 
Symbols:
+ _FILE_close
+ _FILE_read
+ _FILE_seek
+ _FILE_skip
+ ___archive_get_tempdir
+ ___call_test_hook
+ _create_filesystem_object_at
+ _dlhandle
+ _dlopen
+ _dlsym
+ _ftello
+ _mkdirat
+ _mkfifoat
+ _mknodat
+ _os_variant_has_internal_content
+ _symlinkat
+ _unlinkat
- _chdir
- _mkfifo
- _mknod
- _pthread_chdir_np
- _symlink
CStrings:
+ "Error seeking in FILE* pointer"
+ "__test_hook_after_check_symlinks_fsobj"
+ "__test_hook_edit_deep_directories_after_create_dir"
+ "com.apple.libarchive.tests"

```
