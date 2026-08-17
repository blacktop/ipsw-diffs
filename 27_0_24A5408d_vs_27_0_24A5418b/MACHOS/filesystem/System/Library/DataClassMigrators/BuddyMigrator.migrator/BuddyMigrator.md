## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-5411.0.0.0.0
-  __TEXT.__text: 0x2b034
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_stubs: 0x30e0
-  __TEXT.__objc_methlist: 0x1c30
-  __TEXT.__const: 0xf38
+5411.101.0.0.0
+  __TEXT.__text: 0x2db04
+  __TEXT.__auth_stubs: 0x1230
+  __TEXT.__objc_stubs: 0x3100
+  __TEXT.__objc_methlist: 0x1c48
+  __TEXT.__const: 0xf80
   __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__objc_methname: 0x4cf3
+  __TEXT.__objc_methname: 0x4d93
   __TEXT.__cstring: 0x10a2
-  __TEXT.__oslogstring: 0x2df1
+  __TEXT.__oslogstring: 0x2e89
   __TEXT.__objc_classname: 0xd9a
-  __TEXT.__objc_methtype: 0xd75
+  __TEXT.__objc_methtype: 0xdbd
   __TEXT.__dlopen_cstrs: 0x2ac
   __TEXT.__constg_swiftt: 0xab4
-  __TEXT.__swift5_typeref: 0xb9c
+  __TEXT.__swift5_typeref: 0xbbc
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x4f7
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x84
   __TEXT.__swift5_fieldmd: 0x5e4
-  __TEXT.__swift5_capture: 0x4b4
+  __TEXT.__swift5_capture: 0x4c4
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0xa0
   __TEXT.__swift_as_cont: 0xa8
-  __TEXT.__unwind_info: 0xcc0
-  __TEXT.__eh_frame: 0x1014
-  __DATA_CONST.__const: 0x12a0
+  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__eh_frame: 0x104c
+  __DATA_CONST.__const: 0x12f0
   __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x8d0
+  __DATA_CONST.__auth_got: 0x928
   __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__auth_ptr: 0x1b0
+  __DATA_CONST.__auth_ptr: 0x1b8
   __DATA.__objc_const: 0x3ac0
-  __DATA.__objc_selrefs: 0x1118
+  __DATA.__objc_selrefs: 0x1130
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x1958
   __DATA.__data: 0x1170

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 989
-  Symbols:   421
-  CStrings:  1289
+  Functions: 1010
+  Symbols:   423
+  CStrings:  1297
 
Symbols:
+ _memcmp
+ _swift_release_x3
CStrings:
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "AppState changed (%{private}s): %{public}s"
+ "AppState changed (%{public}s): %{public}s"
+ "B40@0:8@16@24@?32"
+ "Failed to determine bundleID: %{public}s"
+ "appStatesFrom:"
+ "bundleIdentifierForIdentityString:error:"
+ "containsSuspiciousChangesWithOriginalAppStates:currentAppStates:bundleIdentifierResolver:"
```
