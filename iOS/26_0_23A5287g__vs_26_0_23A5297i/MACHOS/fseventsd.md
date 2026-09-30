## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1405.0.0.0.0
-  __TEXT.__text: 0x1804c
+1406.0.0.0.0
+  __TEXT.__text: 0x18240
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__cstring: 0xd74
+  __TEXT.__cstring: 0xde4
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x313a
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__oslogstring: 0x3124
+  __TEXT.__unwind_info: 0x370
   __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2d8
+  __DATA_CONST.__const: 0x318
   __DATA_CONST.__cfstring: 0x4e0
   __DATA.__data: 0x232
   __DATA.__bss: 0x468

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 08BAAD3C-2388-31BC-BBD1-D10336F89ADD
-  Functions: 377
+  UUID: D7EEC28B-1A79-3A35-AD82-4B3E14AC7C98
+  Functions: 379
   Symbols:   241
-  CStrings:  490
+  CStrings:  494
 
CStrings:
+ "    purge_events: deleting: %s bytes(%lld)"
+ " com.apple.massStorage.FUNInfo.fsevents_purges_1"
+ "archive_size"
+ "purge_count"
+ "purge_source"
+ "seconds_since_last_purge"
- "    purge_events: deleting: %s"
- "%s:    purge_events: deleting: %s"

```
