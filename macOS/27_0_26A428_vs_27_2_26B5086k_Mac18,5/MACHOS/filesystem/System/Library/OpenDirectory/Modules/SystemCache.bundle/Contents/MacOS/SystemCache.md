## SystemCache

> `/System/Library/OpenDirectory/Modules/SystemCache.bundle/Contents/MacOS/SystemCache`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-1003.0.1.0.0
-  __TEXT.__text: 0x2ddb8
+1003.40.4.0.0
+  __TEXT.__text: 0x2de4c
   __TEXT.__auth_stubs: 0x1330
   __TEXT.__const: 0x208
   __TEXT.__cstring: 0x7e7c
-  __TEXT.__oslogstring: 0x39e4
+  __TEXT.__oslogstring: 0x3a16
   __TEXT.__unwind_info: 0xd08
   __DATA_CONST.__const: 0x4cd0
   __DATA_CONST.__cfstring: 0x49c0

   - /usr/lib/libbsm.0.dylib
   Functions: 883
   Symbols:   1780
-  CStrings:  1219
+  CStrings:  1220
 
Functions:
~ _mbr_lookup_idtype : 3668 -> 3688
~ ___process_getpwnam_initext_block_invoke : 104 -> 140
~ _libinfoDSmig_do_GetProcedureNumber : 244 -> 332
~ __generate_xpc_obj : 688 -> 692
CStrings:
+ "Received a request with a malformed function name"
```
