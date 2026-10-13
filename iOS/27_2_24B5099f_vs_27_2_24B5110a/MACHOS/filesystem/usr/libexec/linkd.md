## linkd

> `usr/libexec/linkd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__cstring`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-301.1.15.0.0
-  __TEXT.__text: 0xbebc8
+301.1.16.0.0
+  __TEXT.__text: 0xc0024
   __TEXT.__auth_stubs: 0x2a50
-  __TEXT.__objc_stubs: 0x27a0
+  __TEXT.__objc_stubs: 0x27e0
   __TEXT.__objc_methlist: 0xe0c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x5c3c
-  __TEXT.__constg_swiftt: 0x1d60
-  __TEXT.__swift5_typeref: 0x2d9a
-  __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x1325
-  __TEXT.__swift5_fieldmd: 0x16e8
-  __TEXT.__swift5_assocty: 0x2a0
-  __TEXT.__swift5_proto: 0x34c
-  __TEXT.__swift5_types: 0x1cc
-  __TEXT.__objc_classname: 0x90c
-  __TEXT.__objc_methname: 0x3fcd
+  __TEXT.__const: 0x5ddc
+  __TEXT.__constg_swiftt: 0x1d80
+  __TEXT.__swift5_typeref: 0x2e02
+  __TEXT.__swift5_builtin: 0x1cc
+  __TEXT.__swift5_reflstr: 0x1318
+  __TEXT.__swift5_fieldmd: 0x1704
+  __TEXT.__swift5_assocty: 0x2d0
+  __TEXT.__swift5_proto: 0x364
+  __TEXT.__swift5_types: 0x1d0
+  __TEXT.__objc_classname: 0x909
+  __TEXT.__objc_methname: 0x3ffd
   __TEXT.__objc_methtype: 0x188b
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__cstring: 0x1c80
-  __TEXT.__oslogstring: 0x4ef6
   __TEXT.__swift5_capture: 0x2f30
-  __TEXT.__swift5_protos: 0x68
   __TEXT.__swift_as_entry: 0x594
-  __TEXT.__swift_as_ret: 0x560
   __TEXT.__swift_as_cont: 0x758
-  __TEXT.__unwind_info: 0x44c0
-  __TEXT.__eh_frame: 0xa378
-  __DATA_CONST.__const: 0x9b20
+  __TEXT.__oslogstring: 0x4f81
+  __TEXT.__swift5_protos: 0x68
+  __TEXT.__swift_as_ret: 0x560
+  __TEXT.__unwind_info: 0x4500
+  __TEXT.__eh_frame: 0xa3b8
+  __DATA_CONST.__const: 0x9b48
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__auth_got: 0x1530
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__auth_ptr: 0x1420
+  __DATA_CONST.__got: 0xa90
+  __DATA_CONST.__auth_ptr: 0x1468
   __DATA.__objc_const: 0x22a8
-  __DATA.__objc_selrefs: 0xe30
+  __DATA.__objc_selrefs: 0xe40
   __DATA.__objc_data: 0x8e8
-  __DATA.__data: 0x3b90
+  __DATA.__data: 0x3c10
   __DATA.__common: 0x320
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5593
-  Symbols:   1199
-  CStrings:  1235
+  Functions: 5615
+  Symbols:   1202
+  CStrings:  1240
 
Symbols:
+ _NSURLIsExcludedFromBackupKey
+ __kCFURLIsExcludedFromCloudBackupKey
+ __kCFURLIsExcludedFromUnencryptedBackupKey
CStrings:
+ "%{public}@ already excluded from backups"
+ "Excluded %{public}@ from backups"
+ "Setting %{public}s on %{public}@"
+ "resourceValuesForKeys:error:"
+ "setResourceValues:error:"
```
