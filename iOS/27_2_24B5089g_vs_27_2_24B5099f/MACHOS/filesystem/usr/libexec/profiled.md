## profiled

> `/usr/libexec/profiled`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2483.40.14.0.0
-  __TEXT.__text: 0xc64e4
+2483.40.19.0.0
+  __TEXT.__text: 0xc68b8
   __TEXT.__auth_stubs: 0x2a00
-  __TEXT.__objc_stubs: 0x13400
-  __TEXT.__objc_methlist: 0x620c
+  __TEXT.__objc_stubs: 0x13480
+  __TEXT.__objc_methlist: 0x6214
   __TEXT.__const: 0x138e
   __TEXT.__gcc_except_tab: 0x1210
-  __TEXT.__oslogstring: 0xfed0
-  __TEXT.__cstring: 0xa9ea
-  __TEXT.__objc_methname: 0x16b77
+  __TEXT.__oslogstring: 0x100b0
+  __TEXT.__cstring: 0xaa0a
+  __TEXT.__objc_methname: 0x16c17
   __TEXT.__objc_classname: 0xbfe
   __TEXT.__objc_methtype: 0x23b2
   __TEXT.__constg_swiftt: 0xe94

   __TEXT.__unwind_info: 0x26c0
   __TEXT.__eh_frame: 0x190
   __DATA_CONST.__const: 0x3048
-  __DATA_CONST.__cfstring: 0x86e0
+  __DATA_CONST.__cfstring: 0x8700
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__got: 0x2148
   __DATA_CONST.__auth_ptr: 0x300
   __DATA.__objc_const: 0x7090
-  __DATA.__objc_selrefs: 0x54b8
+  __DATA.__objc_selrefs: 0x54d8
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x1ea8
   __DATA.__data: 0x900

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2737
+  Functions: 2738
   Symbols:   1816
-  CStrings:  5766
+  CStrings:  5779
 
CStrings:
+ "Finished updating user auto lock time if necessary"
+ "MCInstaller could not parse installed profile %{public}@: %{public}@"
+ "MCInstaller could not read installed profile %{public}@: %{public}@"
+ "MCInstaller could not read one or more installed profiles. Skipping MDM clean up."
+ "MCInstaller found no stub on disk for installed profile %{public}@"
+ "MCMigrator.MigratePostDataMigrator"
+ "No default value found for auto lock time"
+ "Updating user auto lock time if necessary..."
+ "Updating user auto lock time to %{public}@"
+ "_updateUserAutoLockTimeIfNecessary"
+ "defaultValueForSetting:"
+ "identifiersOfProfilesWithFilterFlags:error:"
+ "installedProfileDataWithIdentifier:error:"
+ "isAuthorizedForOperation:policy:completion:"
- "isAuthorizedForOperation:completion:"
```
