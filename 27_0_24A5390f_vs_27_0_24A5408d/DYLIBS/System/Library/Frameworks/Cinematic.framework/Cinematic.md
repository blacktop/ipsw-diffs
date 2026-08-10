## Cinematic

> `/System/Library/Frameworks/Cinematic.framework/Cinematic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-558.0.0.0.0
-  __TEXT.__text: 0x14238
+560.22.1.0.0
+  __TEXT.__text: 0x142f4
   __TEXT.__objc_methlist: 0xeb4
   __TEXT.__cstring: 0x369
   __TEXT.__const: 0x9d8
-  __TEXT.__oslogstring: 0x927
-  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__oslogstring: 0x98f
+  __TEXT.__gcc_except_tab: 0x2c0
   __TEXT.__constg_swiftt: 0x5b0
   __TEXT.__swift5_typeref: 0x332
   __TEXT.__swift5_reflstr: 0x22d

   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x4d8
+  __AUTH_CONST.__auth_got: 0x4e0
   __AUTH.__objc_data: 0x5f0
   __AUTH.__data: 0x840
   __DATA.__objc_ivar: 0x98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 753
-  Symbols:   1292
-  CStrings:  83
+  Functions: 755
+  Symbols:   1293
+  CStrings:  84
 
Symbols:
+ _objc_retain_x28
Functions:
~ ____CNLoadMetadataTrackForVideoTrack_block_invoke : 1136 -> 1276
~ _OUTLINED_FUNCTION_1 : 16 -> 20
+ _OUTLINED_FUNCTION_2
~ ___65+[CNAssetInfo _loadFromAsset:requireDisparity:completionHandler:]_block_invoke.20.cold.1 : 60 -> 52
~ +[CNAssetInfo loadFromCinematicVideoTracks:requireDisparity:error:].cold.2 : 60 -> 52
~ +[CNAssetInfo loadFromCinematicVideoTracks:requireDisparity:error:].cold.3 : 64 -> 56
~ ____CNLoadMetadataTrackForVideoTrack_block_invoke.cold.1 : 68 -> 52
+ ____CNLoadMetadataTrackForVideoTrack_block_invoke.cold.2
CStrings:
+ "Warning: Cannot find associated metadata track. Using last found instance with correct tract identifier"
```
