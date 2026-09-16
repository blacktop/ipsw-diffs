## ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1857.0.0.0.0
-  __TEXT.__text: 0x2cffc
+1857.1.4.0.0
+  __TEXT.__text: 0x2d4fc
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0x1d80
-  __TEXT.__objc_methlist: 0x6c4
-  __TEXT.__gcc_except_tab: 0x3f68
-  __TEXT.__const: 0x8da
-  __TEXT.__cstring: 0x1b22
-  __TEXT.__oslogstring: 0x1325
-  __TEXT.__objc_methname: 0x23d7
+  __TEXT.__objc_stubs: 0x1da0
+  __TEXT.__objc_methlist: 0x6cc
+  __TEXT.__gcc_except_tab: 0x4020
+  __TEXT.__const: 0x8ea
+  __TEXT.__cstring: 0x1b42
+  __TEXT.__oslogstring: 0x140d
+  __TEXT.__objc_methname: 0x2417
   __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methtype: 0xb8f
+  __TEXT.__objc_methtype: 0xbaf
   __TEXT.__swift5_typeref: 0xb6
   __TEXT.__swift5_reflstr: 0x95
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift5_fieldmd: 0xb8
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x1350
+  __TEXT.__unwind_info: 0x1368
   __TEXT.__eh_frame: 0xe0
   __DATA_CONST.__const: 0x13c0
-  __DATA_CONST.__cfstring: 0x10e0
+  __DATA_CONST.__cfstring: 0x10c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0xf0
   __DATA.__objc_const: 0x7b8
-  __DATA.__objc_selrefs: 0x890
+  __DATA.__objc_selrefs: 0x898
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x1d0
   __DATA.__data: 0x348

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 689
-  Symbols:   742
-  CStrings:  817
+  Functions: 691
+  Symbols:   741
+  CStrings:  822
 
Symbols:
+ __Z31FileProviderInternalErrorDomainv
- __Z19kTStringLiteralDataIJLc104ELc102ELc115EEE
- __ZN23FIProviderDomainFetcherC2Ev
CStrings:
+ "@48@0:8@16B24B28^i32^@40"
+ "Apple Archive extraction failed while closing its streams (extract %d, decode %d)"
+ "B44@?0@\"NSArray\"8@\"NSURL\"16i24@\"NSProgress\"28^@36"
+ "B48@0:8@16@24^@32^@40"
+ "Failed to open temporary directory %{public}@: %{darwin.errno}d"
+ "Lookup of '%{public}@' needed FP's cache, but nothing is monitoring the provider list"
+ "NSFileProviderInternalErrorDomain"
+ "_removePlaceholder:andMoveItemIntoPlace:resultingItem:error:"
+ "_temporaryURLAppropriateForURL:calledFromCLI:calledFromLegacyAPI:rootFD:error:"
- "@40@0:8@16B24B28^@32"
- "B40@?0@\"NSArray\"8@\"NSURL\"16@\"NSProgress\"24^@32"
- "_temporaryURLAppropriateForURL:calledFromCLI:calledFromLegacyAPI:error:"
- "hfs"
```
