## libSystem.B_asan.dylib

> `/usr/lib/libSystem.B_asan.dylib`

```diff

-1356.0.0.0.0
-  __TEXT.__text: 0x6e4
-  __TEXT.__auth_stubs: 0x450
+1359.0.0.0.0
+  __TEXT.__text: 0x6f0
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x172
   __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x228
-  __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x10
   __DATA.__data: 0x8
   __DATA.__common: 0x408
   - /usr/lib/system/libcache.dylib

   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
   - @rpath/libclang_rt.asan_ios_dynamic.dylib
-  UUID: A71284E1-3798-33DC-AC72-74AF6A125B08
+  UUID: C790F534-D085-330B-9101-CC286D38DD2E
   Functions: 24
-  Symbols:   115
+  Symbols:   118
   CStrings:  11
 
Symbols:
+ __sanitizers_atfork_child
+ __sanitizers_atfork_parent
+ __sanitizers_atfork_prepare
Functions:
~ _libSystem_atfork_prepare : 88 -> 92
~ _libSystem_atfork_parent : 100 -> 104
~ _libSystem_atfork_child : 120 -> 124

```
