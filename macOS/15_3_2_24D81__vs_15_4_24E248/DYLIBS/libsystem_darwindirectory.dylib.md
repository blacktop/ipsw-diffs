## libsystem_darwindirectory.dylib

> `/usr/lib/system/libsystem_darwindirectory.dylib`

```diff

 122.0.0.0.0
-  __TEXT.__text: 0x2338
+  __TEXT.__text: 0x2504
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__const: 0x70
-  __TEXT.__oslogstring: 0x4b7
+  __TEXT.__oslogstring: 0x4b3
   __TEXT.__cstring: 0x597
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x140
   __AUTH_CONST.__auth_got: 0x178

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: E3036CCB-95CF-3BD6-AA4F-58543B923EA5
-  Functions: 60
-  Symbols:   156
+  UUID: 9987E5C5-ADAF-38B3-A6DB-C773331AA54D
+  Functions: 69
+  Symbols:   167
   CStrings:  71
 
Symbols:
+ DarwinDirectoryGetGeneration.cold.1
+ DarwinDirectoryRecordStoreApply.cold.1
+ DarwinDirectoryRecordStoreApplyWithFilter.cold.1
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ ___ddrsReaderApplyToStoreRecords_block_invoke.cold.15
+ ___ddrsReaderFindStoreRecordIndex_block_invoke.cold.3
+ __getStore_block_invoke.cold.2
+ _ddrsReaderLoadAndValidateRecordStoreAtPath.cold.2
+ _ddrsReaderLoadAndValidateRecordStoreAtPath.cold.3
+ _ddrsReaderLoadAndValidateRecordStoreAtPath.cold.4
CStrings:
+ "assertion failure: \"aeData != ((void*)0)\" -> %llu"
+ "assertion failure: \"bootUUIDFound\" -> %llu"
+ "assertion failure: \"data != ((void*)0)\" -> %llu"
+ "assertion failure: \"foundMap\" -> %llu"
+ "assertion failure: \"munmapResult == 0\" -> %llu"
+ "assertion failure: \"seData->length == sizeof(uuid_t)\" -> %llu"
+ "assertion failure: \"seData->type == (&_xpc_type_uuid)\" -> %llu"
+ "assertion failure: \"store->notifyToken == -1\" -> %llu"
+ "assertion failure: \"store->recordStore != ((void*)0)\" -> %llu"
+ "assertion failure: \"store->recordStore == ((void*)0)\" -> %llu"
+ "assertion failure: \"store->recordStoreLen != 0\" -> %llu"
+ "assertion failure: \"store->recordStoreLen == 0\" -> %llu"
+ "assertion failure: \"xpc_get_type(memberValue) == (&_xpc_type_string)\" -> %llu"
+ "assertion failure: \"xpc_get_type(object) == (&_xpc_type_dictionary)\" -> %llu"
+ "assertion failure: \"xpc_get_type(value) == (&_xpc_type_array)\" -> %llu"
+ "assertion failure: \"xpc_get_type(value) == (&_xpc_type_bool)\" -> %llu"
+ "assertion failure: \"xpc_get_type(value) == (&_xpc_type_string)\" -> %llu"
+ "assertion failure: \"xpc_get_type(value) == (&_xpc_type_uint64)\" -> %llu"
+ "assertion failure: \"xpc_get_type(value) == (&_xpc_type_uuid)\" -> %llu"
- "assertion failure: \"aeData != ((void *)0)\" -> %lld"
- "assertion failure: \"bootUUIDFound\" -> %lld"
- "assertion failure: \"data != ((void *)0)\" -> %lld"
- "assertion failure: \"foundMap\" -> %lld"
- "assertion failure: \"munmapResult == 0\" -> %lld"
- "assertion failure: \"seData->length == sizeof(uuid_t)\" -> %lld"
- "assertion failure: \"seData->type == (&_xpc_type_uuid)\" -> %lld"
- "assertion failure: \"store->notifyToken == -1\" -> %lld"
- "assertion failure: \"store->recordStore != ((void *)0)\" -> %lld"
- "assertion failure: \"store->recordStore == ((void *)0)\" -> %lld"
- "assertion failure: \"store->recordStoreLen != 0\" -> %lld"
- "assertion failure: \"store->recordStoreLen == 0\" -> %lld"
- "assertion failure: \"xpc_get_type(memberValue) == (&_xpc_type_string)\" -> %lld"
- "assertion failure: \"xpc_get_type(object) == (&_xpc_type_dictionary)\" -> %lld"
- "assertion failure: \"xpc_get_type(value) == (&_xpc_type_array)\" -> %lld"
- "assertion failure: \"xpc_get_type(value) == (&_xpc_type_bool)\" -> %lld"
- "assertion failure: \"xpc_get_type(value) == (&_xpc_type_string)\" -> %lld"
- "assertion failure: \"xpc_get_type(value) == (&_xpc_type_uint64)\" -> %lld"
- "assertion failure: \"xpc_get_type(value) == (&_xpc_type_uuid)\" -> %lld"

```
