## ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1857.1.4.0.0
-  __TEXT.__text: 0x2d4fc
+1857.1.7.0.0
+  __TEXT.__text: 0x2d7d4
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0x1da0
-  __TEXT.__objc_methlist: 0x6cc
-  __TEXT.__gcc_except_tab: 0x4020
+  __TEXT.__objc_stubs: 0x1de0
+  __TEXT.__objc_methlist: 0x6dc
+  __TEXT.__gcc_except_tab: 0x4064
   __TEXT.__const: 0x8ea
   __TEXT.__cstring: 0x1b42
-  __TEXT.__oslogstring: 0x140d
-  __TEXT.__objc_methname: 0x2417
+  __TEXT.__oslogstring: 0x13d0
+  __TEXT.__objc_methname: 0x2467
   __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methtype: 0xbaf
+  __TEXT.__objc_methtype: 0xbcf
   __TEXT.__swift5_typeref: 0xb6
   __TEXT.__swift5_reflstr: 0x95
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift5_fieldmd: 0xb8
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x1368
+  __TEXT.__unwind_info: 0x1380
   __TEXT.__eh_frame: 0xe0
   __DATA_CONST.__const: 0x13c0
   __DATA_CONST.__cfstring: 0x10c0

   __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0xf0
   __DATA.__objc_const: 0x7b8
-  __DATA.__objc_selrefs: 0x898
+  __DATA.__objc_selrefs: 0x8a8
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x1d0
   __DATA.__data: 0x348

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 691
-  Symbols:   741
-  CStrings:  822
+  Functions: 695
+  Symbols:   743
+  CStrings:  824
 
Symbols:
+ __ZN10TCFURLInfo10InitializeERK12cstring_view
+ __ZN10TCFURLInfo20POSIXErrorToOSStatusEi
+ __ZN12cstring_viewC1ERK7TString
- __ZN10TCFURLInfo10InitializeEPKc
CStrings:
+ "B48@0:8@16@24Q32^@40"
+ "_settleQuarantineForUnarchivedFolder:quarantineData:options:error:"
+ "fileExistsAtPath:"
+ "v40@0:8@\"NSData\"16@\"DSSandboxingURLWrapper\"24@?<v@?@\"NSError\">32"
- "Failed to remove unarchive destination folder %{public}@: %@"
- "v40@0:8@\"NSData\"16@\"DSSandboxingURLWrapper\"24@?<v@?>32"
```
