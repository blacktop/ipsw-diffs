## MediaPlayer

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-4026.100.76.0.0
-  __TEXT.__text: 0x21a308
-  __TEXT.__objc_methlist: 0x2171c
+4026.100.79.0.0
+  __TEXT.__text: 0x21a3d4
+  __TEXT.__objc_methlist: 0x21734
   __TEXT.__const: 0x4d60
-  __TEXT.__cstring: 0x299b5
-  __TEXT.__oslogstring: 0xfd60
+  __TEXT.__cstring: 0x299f5
+  __TEXT.__oslogstring: 0xfd70
   __TEXT.__gcc_except_tab: 0xa3e0
   __TEXT.__dlopen_cstrs: 0x25c
   __TEXT.__ustring: 0x1dc

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x9e88
+  __TEXT.__unwind_info: 0x9e90
   __TEXT.__eh_frame: 0x4a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x102b8
+  __DATA_CONST.__objc_selrefs: 0x102e8
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0xbb0
   __DATA_CONST.__objc_arraydata: 0x818

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13681
-  Symbols:   29931
+  Functions: 13683
+  Symbols:   29939
   CStrings:  5930
 
Symbols:
+ -[MPRouteButton _accessoryImageForRoute:]
+ -[MPRouteButton largeContentTitle]
+ _objc_msgSend$_accessoryImageForRoute:
+ _objc_msgSend$accessoryImageView
+ _objc_msgSend$isExplicit
+ _objc_msgSend$setLargeContentImage:
+ _objc_msgSend$setScalesLargeContentImage:
+ _objc_msgSend$setShowsLargeContentViewer:
Functions:
~ ___129-[MPModelStorePlatformMetadataGenericObjectBuilder genericObjectForStorePlatformMetadata:radioStationContainsVideo:userIdentity:]_block_invoke_4 : 3672 -> 3668
~ -[MPRouteButton initWithFrame:] : 444 -> 468
+ -[MPRouteButton largeContentTitle]
~ -[MPRouteButton _updateAccessoryIcon] : 560 -> 144
+ -[MPRouteButton _accessoryImageForRoute:]
CStrings:
+ " SELECT child.rowid, child.explicit, r.suborder FROM object_relationships r INNER JOIN objects parent   ON parent.identifier = r.parent_identifier AND parent.person_id = r.person_id INNER JOIN objects child   ON child.identifier = r.child_identifier AND child.person_id = r.person_id WHERE parent.rowid = @id   AND r.child_key = @childKey   AND r.parent_version_hash = COALESCE(@parentVersionHash, r.parent_version_hash) ORDER BY r.suborder"
+ "%{public}@ imageForRoute image: %{public}@ | routes: %{public}@"
- " SELECT child.rowid, child.explicit, r.suborder FROM object_relationships r INNER JOIN objects parent   ON parent.identifier = r.parent_identifier INNER JOIN objects child   ON child.identifier = r.child_identifier WHERE parent.rowid = @id   AND r.child_key = @childKey   AND r.parent_version_hash = COALESCE(@parentVersionHash, r.parent_version_hash) ORDER BY r.suborder"
- "%{public}@ imageForRoute routes: %{public}@"
```
