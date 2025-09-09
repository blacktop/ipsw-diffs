## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

 1323.3.0.0.0
-  __TEXT.__text: 0x28e84
-  __TEXT.__auth_stubs: 0x650
+  __TEXT.__text: 0x28fd0
+  __TEXT.__auth_stubs: 0x660
   __TEXT.__const: 0x610
-  __TEXT.__cstring: 0x4871
+  __TEXT.__cstring: 0x488b
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x15a0
+  __DATA_CONST.__const: 0x15c0
   __DATA_CONST.__helper: 0x8
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x1730
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0x1750
   __AUTH.__data: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__data: 0x120
   __DATA.__common: 0x11
-  __DATA.__bss: 0x1048
+  __DATA.__bss: 0x1058
   __DATA_DIRTY.__common: 0x28
   __DATA_DIRTY.__bss: 0x50
   __TPRO_CONST.__dyld_apis: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 148C2AB6-7AC4-3878-BF47-3CD421204BA0
-  Functions: 1057
-  Symbols:   2779
-  CStrings:  545
+  UUID: AD2F2ABC-3423-3C78-849D-6B16A361906B
+  Functions: 1061
+  Symbols:   2794
+  CStrings:  546
 
Symbols:
+ __ZZ17deviceSupportsMTEE6result
+ __ZZ17deviceSupportsMTEE9onceToken
+ ___deviceSupportsMTE_block_invoke
+ _deviceSupportsMTE
+ _deviceSupportsMTE.cold.1
+ _sysctlbyname
+ _vm_read_safe.cold.1
+ _vm_read_safe.cold.2
CStrings:
+ "hw.optional.arm.FEAT_MTE4"

```
