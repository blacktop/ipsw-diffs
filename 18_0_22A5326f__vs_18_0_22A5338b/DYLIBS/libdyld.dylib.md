## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-1231.1.0.0.0
-  __TEXT.__text: 0x2520c
-  __TEXT.__auth_stubs: 0x640
+1231.3.0.0.0
+  __TEXT.__text: 0x23f0c
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__const: 0x5f0
-  __TEXT.__cstring: 0x3fb4
+  __TEXT.__cstring: 0x3d9c
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x14f8
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x14d8
+  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x14d8
   __AUTH.__data: 0x8
   __DATA.__data: 0xf8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1030
+  __DATA.__bss: 0x1068
   __DATA.__common: 0x1
   __DATA_DIRTY.__common: 0x20
   __TPRO_CONST.__dyld4: 0x48

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 997
-  Symbols:   1288
+  Functions: 957
+  Symbols:   1244
   CStrings:  0
 
Symbols:
+ _malloc_type_aligned_alloc
- _mach_vm_map
- _os_unfair_lock_assert_not_owner
- _os_unfair_lock_assert_owner
- _vm_page_mask

```