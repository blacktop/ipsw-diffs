## ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/XPCServices/ArchiveService.xpc/Contents/MacOS/ArchiveService`

### Sections with Same Size but Changed Content

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
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1857.0.0.0.0
-  __TEXT.__text: 0x309bc
-  __TEXT.__auth_stubs: 0x1a10
-  __TEXT.__objc_stubs: 0x1d40
-  __TEXT.__objc_methlist: 0x6ac
-  __TEXT.__gcc_except_tab: 0x417c
-  __TEXT.__const: 0x97a
-  __TEXT.__cstring: 0x1af2
-  __TEXT.__oslogstring: 0x1482
-  __TEXT.__objc_methname: 0x2413
+1857.1.4.0.0
+  __TEXT.__text: 0x312a0
+  __TEXT.__auth_stubs: 0x1a30
+  __TEXT.__objc_stubs: 0x1da0
+  __TEXT.__objc_methlist: 0x6c4
+  __TEXT.__gcc_except_tab: 0x42a4
+  __TEXT.__const: 0x98a
+  __TEXT.__cstring: 0x1b22
+  __TEXT.__oslogstring: 0x1597
+  __TEXT.__objc_methname: 0x24a3
   __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methtype: 0xbdf
+  __TEXT.__objc_methtype: 0xc0f
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0xb6
   __TEXT.__swift5_reflstr: 0x95

   __TEXT.__swift5_fieldmd: 0xb8
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x1480
+  __TEXT.__unwind_info: 0x14a0
   __TEXT.__eh_frame: 0xe0
   __DATA_CONST.__const: 0x14f8
   __DATA_CONST.__cfstring: 0x1240

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0xd18
+  __DATA_CONST.__auth_got: 0xd28
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0xf0
   __DATA.__objc_const: 0x7b0
-  __DATA.__objc_selrefs: 0x898
+  __DATA.__objc_selrefs: 0x8b0
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x1d0
   __DATA.__data: 0x2c8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 749
-  Symbols:   737
-  CStrings:  831
+  Functions: 752
+  Symbols:   739
+  CStrings:  841
 
Symbols:
+ __Z31FileProviderInternalErrorDomainv
+ __qtn_file_apply_to_fd
+ __qtn_file_init_with_data
- __ZN23FIProviderDomainFetcherC2Ev
CStrings:
+ "@48@0:8@16B24B28^i32^@40"
+ "Apple Archive extraction failed while closing its streams (extract %d, decode %d)"
+ "B44@?0@\"NSArray\"8@\"NSURL\"16i24@\"NSProgress\"28^@36"
+ "B48@0:8@16@24^@32^@40"
+ "B48@0:8i16@20B28@32^@40"
+ "Failed to apply quarantine to %{public}@: %@"
+ "Failed to open temporary directory %{public}@: %{darwin.errno}d"
+ "Lookup of '%{public}@' needed FP's cache, but nothing is monitoring the provider list"
+ "NSFileProviderInternalErrorDomain"
+ "_applyQuarantineToDirectoryFD:data:useDefaultIfEmpty:url:error:"
+ "_removePlaceholder:andMoveItemIntoPlace:resultingItem:error:"
+ "_temporaryURLAppropriateForURL:calledFromCLI:calledFromLegacyAPI:rootFD:error:"
+ "defaultQuarantineData"
- "@40@0:8@16B24B28^@32"
- "B40@?0@\"NSArray\"8@\"NSURL\"16@\"NSProgress\"24^@32"
- "_temporaryURLAppropriateForURL:calledFromCLI:calledFromLegacyAPI:error:"
```
