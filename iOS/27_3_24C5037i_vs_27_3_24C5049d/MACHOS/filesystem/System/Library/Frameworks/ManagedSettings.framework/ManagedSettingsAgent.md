## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-322.0.0.0.0
-  __TEXT.__text: 0x71f4c
-  __TEXT.__auth_stubs: 0x2090
+322.60.4.0.0
+  __TEXT.__text: 0x73ea4
+  __TEXT.__auth_stubs: 0x20a0
   __TEXT.__objc_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x680
+  __TEXT.__objc_methlist: 0x6a0
   __TEXT.__const: 0x1c8c
   __TEXT.__objc_classname: 0x76c
-  __TEXT.__objc_methtype: 0xb92
-  __TEXT.__objc_methname: 0x19d5
-  __TEXT.__cstring: 0x825
+  __TEXT.__objc_methtype: 0xbd2
+  __TEXT.__objc_methname: 0x1a19
+  __TEXT.__cstring: 0x865
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1090
+  __TEXT.__constg_swiftt: 0x10b0
   __TEXT.__swift5_typeref: 0x102f
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0xb55

   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x90
-  __TEXT.__oslogstring: 0x2fc2
+  __TEXT.__oslogstring: 0x3122
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_capture: 0x430
-  __TEXT.__unwind_info: 0x10b0
-  __TEXT.__eh_frame: 0x1e40
+  __TEXT.__unwind_info: 0x10c8
+  __TEXT.__eh_frame: 0x1eb0
   __DATA_CONST.__const: 0x1eb0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__auth_got: 0x1050
+  __DATA_CONST.__auth_got: 0x1058
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0x400
-  __DATA.__objc_const: 0x1e68
-  __DATA.__objc_selrefs: 0x428
+  __DATA.__objc_const: 0x1e70
+  __DATA.__objc_selrefs: 0x430
   __DATA.__objc_data: 0x2b8
-  __DATA.__data: 0x1f78
+  __DATA.__data: 0x1f98
   __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1123
-  Symbols:   770
-  CStrings:  557
+  Functions: 1128
+  Symbols:   771
+  CStrings:  566
 
Symbols:
+ _$s2os6LoggerV15ManagedSettingsE16appDataMigrationACvgZ
CStrings:
+ "Migrated record %{public}s from %{public}s to %{public}s"
+ "Migrating app data from %{public}s to %{public}s"
+ "No data to migrate for %{public}s"
+ "Not migrating data from unauthorized %{public}s"
+ "Not migrating data to %{public}s, which already has its own data"
+ "Not migrating data to unauthorized %{public}s"
+ "com.apple.private.managed-settings.app-data-migration"
+ "migrateAppDataFromBundleIdentifier:toBundleIdentifier:replyHandler:"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
```
