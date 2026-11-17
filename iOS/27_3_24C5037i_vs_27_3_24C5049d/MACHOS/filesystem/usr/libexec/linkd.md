## linkd

> `/usr/libexec/linkd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__objc_classname`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-301.2.7.2.0
-  __TEXT.__text: 0xc1574
-  __TEXT.__auth_stubs: 0x2a70
+301.2.12.2.0
+  __TEXT.__text: 0xc2694
+  __TEXT.__auth_stubs: 0x2a80
   __TEXT.__objc_stubs: 0x27e0
   __TEXT.__objc_methlist: 0xdfc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x5e2c
+  __TEXT.__const: 0x5e3a
+  __TEXT.__objc_classname: 0x909
+  __TEXT.__objc_methname: 0x3ffd
+  __TEXT.__objc_methtype: 0x189b
   __TEXT.__constg_swiftt: 0x1d78
-  __TEXT.__swift5_typeref: 0x2e12
+  __TEXT.__swift5_typeref: 0x2e42
+  __TEXT.__swift5_reflstr: 0x1308
+  __TEXT.__swift5_fieldmd: 0x1710
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_reflstr: 0x1318
-  __TEXT.__swift5_fieldmd: 0x1704
+  __TEXT.__swift5_capture: 0x2f18
   __TEXT.__swift5_assocty: 0x2d0
   __TEXT.__swift5_proto: 0x364
   __TEXT.__swift5_types: 0x1d0
-  __TEXT.__objc_classname: 0x909
-  __TEXT.__objc_methname: 0x3fbd
-  __TEXT.__objc_methtype: 0x188b
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__cstring: 0x1d40
-  __TEXT.__swift5_capture: 0x2ee4
   __TEXT.__swift_as_entry: 0x598
   __TEXT.__swift_as_ret: 0x570
   __TEXT.__swift_as_cont: 0x788
-  __TEXT.__oslogstring: 0x50a1
+  __TEXT.__swift5_mpenum: 0x18
+  __TEXT.__cstring: 0x1d91
+  __TEXT.__oslogstring: 0x5136
   __TEXT.__swift5_protos: 0x68
-  __TEXT.__unwind_info: 0x4558
-  __TEXT.__eh_frame: 0xa4c8
-  __DATA_CONST.__const: 0x9a80
+  __TEXT.__unwind_info: 0x4568
+  __TEXT.__eh_frame: 0xa500
+  __DATA_CONST.__const: 0x9b20
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__auth_got: 0x1540
+  __DATA_CONST.__auth_got: 0x1548
   __DATA_CONST.__got: 0xa98
-  __DATA_CONST.__auth_ptr: 0x1480
+  __DATA_CONST.__auth_ptr: 0x1430
   __DATA.__objc_const: 0x22a0
   __DATA.__objc_selrefs: 0xe38
   __DATA.__objc_data: 0x8e8
-  __DATA.__data: 0x3c30
+  __DATA.__data: 0x3c40
   __DATA.__common: 0x320
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5612
-  Symbols:   1205
-  CStrings:  1246
+  Functions: 5624
+  Symbols:   1206
+  CStrings:  1250
 
Symbols:
+ _$s8Dispatch0A3QoSV10backgroundACvgZ
CStrings:
+ "%{public}s is not in the index and no audit is needed, unblocking"
+ "Failed to exclude %{public}s from backups: %{public}@"
+ "com.apple.frontboard.launchapplications"
+ "com.apple.linkd.backup-exclusion"
```
