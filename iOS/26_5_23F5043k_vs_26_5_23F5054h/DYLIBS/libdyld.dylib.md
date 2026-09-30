## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-1377.1.0.0.0
+1377.2.1.0.0
   __TEXT.__text: 0x2bfe8
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__const: 0x600
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__const: 0x610
   __TEXT.__cstring: 0x4a06
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x1708
   __DATA_CONST.__helper: 0x8
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x1718
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0x1720
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1048
   __DATA.__common: 0x11

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 96793664-2303-3B77-95F1-21A0B7ADF6B0
-  Functions: 1100
-  Symbols:   3059
+  UUID: F32DDC43-7D67-3BEA-8E46-66CCE0A41E07
+  Functions: 1101
+  Symbols:   3062
   CStrings:  548
 
Symbols:
+ __ZNK5dyld416LibSystemHelpers32os_unfair_recursive_lock_trylockEP26os_unfair_recursive_lock_s
+ _os_unfair_recursive_lock_trylock
Functions:
~ __ZNK5dyld416LibSystemHelpers17setUpThreadLocalsEPK15DyldSharedCachePKN6mach_o12UnsafeHeaderE : 20 -> 12
+ __ZNK5dyld416LibSystemHelpers32os_unfair_recursive_lock_trylockEP26os_unfair_recursive_lock_s

```
