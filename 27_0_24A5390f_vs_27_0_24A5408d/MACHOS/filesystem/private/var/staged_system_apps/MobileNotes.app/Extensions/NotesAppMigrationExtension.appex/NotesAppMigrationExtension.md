## NotesAppMigrationExtension

> `/private/var/staged_system_apps/MobileNotes.app/Extensions/NotesAppMigrationExtension.appex/NotesAppMigrationExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-2998.0.0.0.0
-  __TEXT.__text: 0x83124
-  __TEXT.__auth_stubs: 0x2260
-  __TEXT.__objc_stubs: 0x2e60
+3001.2.1.0.0
+  __TEXT.__text: 0x84f58
+  __TEXT.__auth_stubs: 0x22e0
+  __TEXT.__objc_stubs: 0x2ec0
   __TEXT.__objc_methlist: 0x104
   __TEXT.__cstring: 0xb64
-  __TEXT.__swift5_typeref: 0x1985
-  __TEXT.__const: 0x58e4
+  __TEXT.__swift5_typeref: 0x19cb
+  __TEXT.__const: 0x5904
   __TEXT.__constg_swiftt: 0xdb0
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x1092
-  __TEXT.__swift5_fieldmd: 0x1ad4
+  __TEXT.__swift5_reflstr: 0x10c2
+  __TEXT.__swift5_fieldmd: 0x1ae0
   __TEXT.__swift5_assocty: 0x360
   __TEXT.__swift5_proto: 0x528
   __TEXT.__swift5_types: 0x164
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_capture: 0x5a4
+  __TEXT.__swift5_capture: 0x5c0
   __TEXT.__objc_methtype: 0x2bb
-  __TEXT.__objc_methname: 0x2086
+  __TEXT.__objc_methname: 0x20d1
   __TEXT.__objc_classname: 0x134
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__oslogstring: 0x1026
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x78
-  __TEXT.__swift_as_ret: 0x6c
-  __TEXT.__swift_as_cont: 0x40
+  __TEXT.__swift_as_ret: 0x70
+  __TEXT.__swift_as_cont: 0x48
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x1ac8
-  __TEXT.__eh_frame: 0x3568
-  __DATA_CONST.__const: 0x3fa0
+  __TEXT.__unwind_info: 0x1b28
+  __TEXT.__eh_frame: 0x36a0
+  __DATA_CONST.__const: 0x3fc8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1138
-  __DATA_CONST.__got: 0x748
-  __DATA_CONST.__auth_ptr: 0x738
-  __DATA.__objc_const: 0x5c0
-  __DATA.__objc_selrefs: 0xbf8
-  __DATA.__objc_data: 0x280
-  __DATA.__data: 0x2390
+  __DATA_CONST.__auth_got: 0x1178
+  __DATA_CONST.__got: 0x750
+  __DATA_CONST.__auth_ptr: 0x748
+  __DATA.__objc_const: 0x5e0
+  __DATA.__objc_selrefs: 0xc10
+  __DATA.__objc_data: 0x288
+  __DATA.__data: 0x23b8
   __DATA.__bss: 0xa110
   __DATA.__common: 0xa2
   - /System/Library/Frameworks/AppMigrationKit.framework/AppMigrationKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2166
+  Functions: 2183
   Symbols:   281
-  CStrings:  619
+  CStrings:  622
 
CStrings:
+ "appMigrationImportedNoteCount"
+ "error importing archive in extension: %@"
+ "extension import finished: %ld/%ld"
+ "ic_save"
+ "importing from resolved root: %s"
+ "isEmpty"
+ "newLocalAccountInContext:"
+ "refreshAllObjects"
+ "workerManagedObjectContext"
- "copyItemAtURL:toURL:error:"
- "destination: %s"
- "error copying archive to group container: %@"
- "fileExistsAtPath:"
- "group container: %s"
- "removing existing import file"
```
