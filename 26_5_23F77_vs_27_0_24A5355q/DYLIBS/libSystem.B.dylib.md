## libSystem.B.dylib

> `/usr/lib/libSystem.B.dylib`

```diff

-1356.0.0.0.0
-  __TEXT.__text: 0x648
-  __TEXT.__auth_stubs: 0x410
+1359.0.0.0.0
+  __TEXT.__text: 0x654
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x6a
   __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0x80
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x208
   __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__auth_got: 0x220
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x8
   - /usr/lib/system/libcache.dylib

   - /usr/lib/system/libsystem_trial.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: ED582B70-F7EF-3222-8F75-30507F4E6E01
+  UUID: 28449900-A70F-3500-945C-1B49B9C05077
   Functions: 23
-  Symbols:   132
+  Symbols:   135
   CStrings:  7
 
Symbols:
+ __sanitizers_atfork_child
+ __sanitizers_atfork_parent
+ __sanitizers_atfork_prepare
Functions:
~ _libSystem_atfork_prepare : 88 -> 92
~ _libSystem_atfork_parent : 100 -> 104
~ _libSystem_atfork_child : 120 -> 124

```
