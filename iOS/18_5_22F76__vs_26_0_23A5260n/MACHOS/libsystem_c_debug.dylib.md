## libsystem_c_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib`

```diff

-1698.100.8.0.0
-  __TEXT.__text: 0xbfc7c
+1724.0.0.0.0
+  __TEXT.__text: 0xbfecc
   __TEXT.__auth_stubs: 0xc00
   __TEXT.__const: 0x27c4
   __TEXT.__cstring: 0x2ed9

   __AUTH_CONST.__auth_got: 0x600
   __AUTH.__data: 0x288
   __AUTH.__constrw: 0x80
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__data: 0x188d
   __DATA.__constrw: 0xc88
   __DATA.__bss: 0xaea8

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  UUID: 82D31768-CC65-3F2A-B4CB-7696B4BB119E
-  Functions: 1706
-  Symbols:   2305
+  UUID: 83013410-86C0-323B-8979-149D3A8E76C1
+  Functions: 1708
+  Symbols:   2307
   CStrings:  828
 
Symbols:
+ ___collate_resolve_legacy_substitutions
+ _ccrng_generate
Functions:
~ ___copy_assignment_8_8_t0w8_pa0_28660_8_pa0_36689_16_pa0_31171_24_pa0_29245_32 : 520 -> 504
~ _arc4random_buf : 72 -> 60
+ _ccrng_generate
~ _basename_r : 492 -> 428
~ _dirname_r : 568 -> 544
~ ___collate_load_tables_legacy : 2672 -> 2680
+ ___collate_resolve_legacy_substitutions

```
