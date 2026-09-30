## libsystem_c_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib`

```diff

-1752.100.10.0.0
-  __TEXT.__text: 0xc0884
+1752.120.2.0.0
+  __TEXT.__text: 0xc0d30
   __TEXT.__auth_stubs: 0xc00
   __TEXT.__const: 0x27e4
   __TEXT.__cstring: 0x2ed2
-  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__unwind_info: 0x9c8
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x13c0
   __AUTH_CONST.__auth_got: 0x600

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  UUID: 2D1171F6-AED9-3CDF-8298-DC359C83F65F
+  UUID: C304EA9C-400A-3532-9644-07A37A3CFE48
   Functions: 1721
   Symbols:   2256
   CStrings:  828
Symbols:
+ _tre_stack_num_items
- _tre_stack_num_objects
Functions:
~ _regncomp_l : 756 -> 784
~ _regcomp_l : 232 -> 260
~ _regwncomp_l : 140 -> 180
~ _regwcomp_l : 160 -> 224
~ _regwcomp : 84 -> 200
~ _tre_match : 832 -> 824
~ _tre_compile : 3768 -> 3764
~ _tre_add_tags : 11472 -> 11492
~ _tre_expand_ast : 2200 -> 2208
~ _tre_tnfa_run_backtrack : 7932 -> 8028
~ _tre_tnfa_run_parallel : 7040 -> 7876
~ _tre_parse : 10020 -> 10016
~ _tre_stack_new : 220 -> 204
~ _tre_stack_pop_int : 56 -> 48

```
