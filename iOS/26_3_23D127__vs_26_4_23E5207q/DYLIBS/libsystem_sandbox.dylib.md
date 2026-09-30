## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2680.80.20.0.0
-  __TEXT.__text: 0x3698
+2680.100.163.0.0
+  __TEXT.__text: 0x36d0
   __TEXT.__auth_stubs: 0x360
   __TEXT.__const: 0x178
   __TEXT.__cstring: 0x747

   __DATA.__data: 0x13
   __DATA.__bss: 0x10
   __DATA_DIRTY.__bss: 0x8
-  - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 5A35D64F-153D-3159-BF81-4354E6CBC478
+  UUID: 20A2B277-5DDA-357D-A7D0-04B01C415281
   Functions: 131
   Symbols:   251
   CStrings:  67
Functions:
~ _sandbox_check_common : 560 -> 568
~ sub_29e5a5b60 -> sub_2a5e47b20 : 76 -> 80
~ _rootless_trusted_by_self_token : 140 -> 160
~ _sandbox_init_with_parameters : 836 -> 860

```
