## libsystem_sanitizers.dylib

> `/usr/lib/system/libsystem_sanitizers.dylib`

```diff

-18.2.0.0.0
-  __TEXT.__text: 0x3f74
+19.0.0.0.0
+  __TEXT.__text: 0x40fc
   __TEXT.__auth_stubs: 0x190
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0xa42
+  __TEXT.__cstring: 0xa36
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x90
   __AUTH_CONST.__auth_got: 0xc8

   - /usr/lib/system/libsystem_pthread.dylib
   Functions: 186
   Symbols:   248
-  CStrings:  129
+  CStrings:  130
 
Symbols:
+ _ZN5trace6Lookup6createERA24_h.cold.1
+ __ZN5trace12lookupTracesEmR24sanitizers_stack_trace_tS1_
- __asan_get_alloc_stack.cold.1
- __asan_get_free_stack.cold.1
CStrings:
+ "create"
+ "isInitialized()"
+ "trace.cpp"
- "__asan_get_alloc_stack"
- "__asan_get_free_stack"

```
