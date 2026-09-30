## MediaPlayer

> `/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__gcc_except_tab`
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
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-4026.100.76.0.0
-  __TEXT.__text: 0x38cbb4
-  __TEXT.__objc_methlist: 0x28b04
+4026.100.79.0.0
+  __TEXT.__text: 0x38cebc
+  __TEXT.__objc_methlist: 0x28b1c
   __TEXT.__dlopen_cstrs: 0x4bd
   __TEXT.__const: 0x14fc0
   __TEXT.__swift5_typeref: 0x18a

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__cstring: 0x319fa
+  __TEXT.__cstring: 0x31a3f
   __TEXT.__swift5_proto: 0x14
   __TEXT.__gcc_except_tab: 0x1c41c
-  __TEXT.__oslogstring: 0x1a1d5
+  __TEXT.__oslogstring: 0x1a251
   __TEXT.__ustring: 0x1ca
-  __TEXT.__unwind_info: 0xd1d8
+  __TEXT.__unwind_info: 0xd1e0
   __TEXT.__eh_frame: 0x3c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x428
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x13988
+  __DATA_CONST.__objc_selrefs: 0x139b8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xdb0
   __DATA_CONST.__objc_arraydata: 0x8d8

   __AUTH.__data: 0x100
   __DATA.__objc_ivar: 0x2d6c
   __DATA.__data: 0x3af8
-  __DATA.__bss: 0xe90
+  __DATA.__bss: 0xe88
   __DATA.__common: 0xab8
   __DATA_DIRTY.__objc_data: 0xf78
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17156
-  Symbols:   38940
+  Functions: 17158
+  Symbols:   38948
   CStrings:  7417
 
Symbols:
+ -[MPRouteButton _accessoryImageForRoute:]
+ -[MPRouteButton largeContentTitle]
+ GCC_except_table16657
+ GCC_except_table16737
+ GCC_except_table16743
+ GCC_except_table16841
+ _objc_msgSend$_accessoryImageForRoute:
+ _objc_msgSend$accessoryImageView
+ _objc_msgSend$isExplicit
+ _objc_msgSend$setLargeContentImage:
+ _objc_msgSend$setScalesLargeContentImage:
+ _objc_msgSend$setShowsLargeContentViewer:
- GCC_except_table16655
- GCC_except_table16735
- GCC_except_table16741
- GCC_except_table16839
Functions:
~ ___91-[MPMediaLibraryDataProviderML3 setValue:forProperty:ofItemWithIdentifier:completionBlock:]_block_invoke : 1776 -> 1924
~ ___110-[MPMediaLibraryDataProviderML3 setValue:forProperty:ofCollectionWithIdentifier:groupingType:completionBlock:]_block_invoke.195 : 2316 -> 2656
~ ___126-[MPMediaLibraryDataProviderML3 setValuesForProperties:trackList:andEntryProperties:ofPlaylistWithIdentifier:completionBlock:]_block_invoke.205 : 2280 -> 2364
~ ___129-[MPModelStorePlatformMetadataGenericObjectBuilder genericObjectForStorePlatformMetadata:radioStationContainsVideo:userIdentity:]_block_invoke_4 : 3648 -> 3644
~ -[MPRouteButton initWithFrame:] : 440 -> 464
+ -[MPRouteButton largeContentTitle]
~ -[MPRouteButton _updateAccessoryIcon] : 572 -> 144
+ -[MPRouteButton _accessoryImageForRoute:]
CStrings:
+ " SELECT child.rowid, child.explicit, r.suborder FROM object_relationships r INNER JOIN objects parent   ON parent.identifier = r.parent_identifier AND parent.person_id = r.person_id INNER JOIN objects child   ON child.identifier = r.child_identifier AND child.person_id = r.person_id WHERE parent.rowid = @id   AND r.child_key = @childKey   AND r.parent_version_hash = COALESCE(@parentVersionHash, r.parent_version_hash) ORDER BY r.suborder"
+ "%{public}@ imageForRoute image: %{public}@ | routes: %{public}@"
+ "Not propagating favorite state change for album (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as cloudLibrary is not enabled and it's missing store identifiers"
+ "Not propagating favorite state change for album (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as it's missing store identifiers"
+ "Not propagating favorite state change for album (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as the request is not valid"
+ "Not propagating favorite state change for album artist (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as cloudLibrary is not enabled and it's missing store identifiers"
+ "Not propagating favorite state change for album artist (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as it's missing store identifiers"
+ "Not propagating favorite state change for album artist (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as the request is not valid"
+ "Not propagating favorite state change for playlist (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as it's missing store identifiers"
+ "Not propagating favorite state change for playlist (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as the request is not valid"
+ "Not propagating favorite state change for track (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as cloudLibrary is not enabled and it's missing store identifiers"
+ "Not propagating favorite state change for track (likedState=%{public}@, timeStamp=%{public}@) with persistentID=%lld as it's missing store identifiers"
+ "Not propagating favorite state change for trackPID=%lld as the request is not valid (likedState=%{public}@, timeStamp=%{public}@"
+ "Not propagating liked state=%{public}@ for album=%{public}@"
- " SELECT child.rowid, child.explicit, r.suborder FROM object_relationships r INNER JOIN objects parent   ON parent.identifier = r.parent_identifier INNER JOIN objects child   ON child.identifier = r.child_identifier WHERE parent.rowid = @id   AND r.child_key = @childKey   AND r.parent_version_hash = COALESCE(@parentVersionHash, r.parent_version_hash) ORDER BY r.suborder"
- "%{public}@ imageForRoute routes: %{public}@"
- "Not propagating favorite state change for album (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as cloudLibrary is not enabled and it's missing store identifiers"
- "Not propagating favorite state change for album (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as it's missing store identifiers"
- "Not propagating favorite state change for album (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as the request is not valid"
- "Not propagating favorite state change for album artist (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as cloudLibrary is not enabled and it's missing store identifiers"
- "Not propagating favorite state change for album artist (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as it's missing store identifiers"
- "Not propagating favorite state change for album artist (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as the request is not valid"
- "Not propagating favorite state change for playlist (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as it's missing store identifiers"
- "Not propagating favorite state change for playlist (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as the request is not valid"
- "Not propagating favorite state change for track (likedState=%d, timeStamp=%p) with persistentID=%lld as it's missing store identifiers"
- "Not propagating favorite state change for track (likedState=%d, timeStamp=%{public}@) with persistentID=%lld as cloudLibrary is not enabled and it's missing store identifiers"
- "Not propagating favorite state change for trackPID=%lld as the request is not valid (likedState=%d, timeStamp=%{public}@"
- "Not propagating liked state=%d for album=%{public}@"
```
