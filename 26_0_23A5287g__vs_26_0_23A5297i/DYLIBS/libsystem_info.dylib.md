## libsystem_info.dylib

> `/usr/lib/system/libsystem_info.dylib`

```diff

-597.0.0.0.0
-  __TEXT.__text: 0x24b10
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x1fd0
-  __TEXT.__oslogstring: 0xd15
-  __TEXT.__unwind_info: 0x830
+600.0.0.0.0
+  __TEXT.__text: 0x2501c
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__const: 0x300
+  __TEXT.__cstring: 0x1fd7
+  __TEXT.__oslogstring: 0xe88
+  __TEXT.__unwind_info: 0x838
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x9e0
-  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__const: 0x798
   __AUTH.__data: 0x1d0
   __DATA.__data: 0x21c

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 672A1955-34F8-3DDB-8CAA-1D137D921971
-  Functions: 905
-  Symbols:   1856
-  CStrings:  431
+  UUID: DF5563B1-9689-30A1-A7D8-D3AA041C144F
+  Functions: 910
+  Symbols:   1865
+  CStrings:  437
 
Symbols:
+ _kvbuf_add_key.cold.1
+ _kvbuf_add_val_len.cold.1
+ _kvbuf_append_kvbuf.cold.1
- _strcat
CStrings:
+ "(null)"
+ "kvbuf_add_key: overflow when adding extra (%zu) and kl (%u)"
+ "kvbuf_add_val_len: overflow when adding sizeof(uint32_t) (%zu) and len (%u)"
+ "kvbuf_append_kvbuf: overflow when subtracting sizeof(uint32_t) (%zu) from kv2->datalen (%u)"
+ "kvbuf_grow: overflow when adding kv->datalen (%u), delta (%u), and extra (%u)"
+ "kvbuf_grow: overflow when rounding %u to nearest chunk size (%u)"

```
