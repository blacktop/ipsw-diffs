## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-792.0.0.0.0
-  __TEXT.__text: 0x36948
+792.0.2.0.0
+  __TEXT.__text: 0x36b84
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__const: 0x4ea
-  __TEXT.__cstring: 0x97b7
+  __TEXT.__const: 0x4fa
+  __TEXT.__cstring: 0x98bf
   __TEXT.__dof_magmalloc: 0x912
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__unwind_info: 0x880
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x808

   __DATA.__data: 0xb9
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x216d
-  __DATA.__common: 0x60
+  __DATA.__common: 0x78
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__common: 0x1f0
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: C2946FD1-2C54-3129-B168-202D41FFF12E
-  Functions: 837
-  Symbols:   2181
-  CStrings:  853
+  UUID: E2E18937-2D8E-327A-B30E-077C36F6DE78
+  Functions: 838
+  Symbols:   2184
+  CStrings:  857
 
Symbols:
+ _malloc_guarded_range_config
+ _mvm_guarded_range_init
Functions:
~ _mvm_allocate_plat : 244 -> 300
~ ___malloc_init : 5476 -> 5568
~ _malloc_zone_register_while_locked : 484 -> 608
+ _mvm_guarded_range_init
CStrings:
+ "Failed to create carveout at 0x%lx in malloc guarded range 0x%lx: %d\n"
+ "Failed to map guarded range: %d\n"
+ "Guarded Range Config (base/size/carveout): 0x%lx / 0x%lx / 0x%lx\n"
+ "Unsupported guarded metadata allocation at address 0x%lx of size 0x%lx with flags %d and label %d\n"
+ "malloc_zone_register allocation failed\n"
- "malloc_zone_register allocation failed: %d\n"

```
