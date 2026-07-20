## MediaPlayer

> `/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
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
-  __TEXT.__text: 0x21a5d4
+4026.100.79.0.0
+  __TEXT.__text: 0x21a5d0
   __TEXT.__objc_methlist: 0x1cfbc
   __TEXT.__dlopen_cstrs: 0x1da
   __TEXT.__const: 0x4e00

   __TEXT.__swift5_reflstr: 0xae
   __TEXT.__swift5_fieldmd: 0x194
   __TEXT.__oslogstring: 0xdd4d
-  __TEXT.__cstring: 0x27350
+  __TEXT.__cstring: 0x27395
   __TEXT.__swift5_capture: 0x1f40
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x48

   __DATA_CONST.__objc_protolist: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xdbf8
+  __DATA_CONST.__objc_selrefs: 0xdc00
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xa10
   __DATA_CONST.__objc_arraydata: 0x800

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 12851
-  Symbols:   27218
+  Symbols:   27219
   CStrings:  5516
 
Symbols:
+ _objc_msgSend$isExplicit
Functions:
~ __129-[MPModelStorePlatformMetadataGenericObjectBuilder genericObjectForStorePlatformMetadata:radioStationContainsVideo:userIdentity:]_block_invoke.7 : 3832 -> 3828
CStrings:
+ " SELECT child.rowid, child.explicit, r.suborder FROM object_relationships r INNER JOIN objects parent   ON parent.identifier = r.parent_identifier AND parent.person_id = r.person_id INNER JOIN objects child   ON child.identifier = r.child_identifier AND child.person_id = r.person_id WHERE parent.rowid = @id   AND r.child_key = @childKey   AND r.parent_version_hash = COALESCE(@parentVersionHash, r.parent_version_hash) ORDER BY r.suborder"
- " SELECT child.rowid, child.explicit, r.suborder FROM object_relationships r INNER JOIN objects parent   ON parent.identifier = r.parent_identifier INNER JOIN objects child   ON child.identifier = r.child_identifier WHERE parent.rowid = @id   AND r.child_key = @childKey   AND r.parent_version_hash = COALESCE(@parentVersionHash, r.parent_version_hash) ORDER BY r.suborder"
```
