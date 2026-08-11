## PlistFile

> `/System/Library/OpenDirectory/Modules/PlistFile.bundle/Contents/MacOS/PlistFile`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 966.100.2.0.0
-  __TEXT.__text: 0x4dfa4
+  __TEXT.__text: 0x4e008
   __TEXT.__auth_stubs: 0x19f0
   __TEXT.__objc_stubs: 0x800
   __TEXT.__const: 0x251

   - /usr/lib/libodaccesstoken.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1442
+  Functions: 1441
   Symbols:   1754
   CStrings:  1605
 
Functions:
~ _OUTLINED_FUNCTION_11 : 16 -> 40
~ _OUTLINED_FUNCTION_12 : 40 -> 12
~ _OUTLINED_FUNCTION_13 : 12 -> 24
~ _OUTLINED_FUNCTION_15 : 24 -> 12
~ _OUTLINED_FUNCTION_16 : 12 -> 28
~ _OUTLINED_FUNCTION_18 : 28 -> 36
~ _OUTLINED_FUNCTION_19 : 36 -> 20
~ _OUTLINED_FUNCTION_21 : 20 -> 28
~ _OUTLINED_FUNCTION_22 : 28 -> 24
- _OUTLINED_FUNCTION_24
~ _serializeParameters : 276 -> 284
~ _DeserializeCredential : 436 -> 432
~ _LibSer_SEPControl_Deserialize : 156 -> 196
~ _LibSer_SEPControlResponse_Deserialize : 64 -> 88
~ _LibSer_ACMDeserializeEnvironmentVariableType : 140 -> 148
~ _LibSer_ACMDeserializeSEPControlCode : 268 -> 308
```
