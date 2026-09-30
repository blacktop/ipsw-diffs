## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4025.300.10.0.0
-  __TEXT.__text: 0x14b148
+4025.300.12.0.0
+  __TEXT.__text: 0x14b430
   __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_stubs: 0x15880
-  __TEXT.__objc_methlist: 0xb79c
+  __TEXT.__objc_stubs: 0x158c0
+  __TEXT.__objc_methlist: 0xb7b4
   __TEXT.__dlopen_cstrs: 0x705
   __TEXT.__const: 0x4f0
   __TEXT.__oslogstring: 0x2a510
-  __TEXT.__cstring: 0x10e19
-  __TEXT.__objc_methname: 0x221f9
+  __TEXT.__cstring: 0x10ffa
+  __TEXT.__objc_methname: 0x222ef
   __TEXT.__constg_swiftt: 0x98
   __TEXT.__swift5_typeref: 0x9c
   __TEXT.__swift5_reflstr: 0x27

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__gcc_except_tab: 0x5a08
+  __TEXT.__gcc_except_tab: 0x5a14
   __TEXT.__objc_classname: 0x26f0
-  __TEXT.__objc_methtype: 0x4703
-  __TEXT.__unwind_info: 0x3c08
+  __TEXT.__objc_methtype: 0x475b
+  __TEXT.__unwind_info: 0x3c18
   __TEXT.__eh_frame: 0x3e0
   __DATA_CONST.__auth_got: 0xae8
   __DATA_CONST.__got: 0x1050
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x60a8
+  __DATA_CONST.__const: 0x6120
   __DATA_CONST.__cfstring: 0xc420
   __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x600
   __DATA_CONST.__objc_intobj: 0xf48
-  __DATA_CONST.__objc_arraydata: 0x2e0
-  __DATA_CONST.__objc_arrayobj: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x288
+  __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x16460
-  __DATA.__objc_selrefs: 0x6698
+  __DATA.__objc_const: 0x16468
+  __DATA.__objc_selrefs: 0x66b0
   __DATA.__objc_ivar: 0xe48
   __DATA.__objc_data: 0x5438
   __DATA.__data: 0x1228

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DAAPKit.framework/DAAPKit
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1390CE76-CEB3-3CF0-A400-7290C59162C5
-  Functions: 5172
-  Symbols:   924
-  CStrings:  10974
+  UUID: 153358AD-9C1D-3D0A-BA25-32E3452B6890
+  Functions: 5173
+  Symbols:   929
+  CStrings:  10979
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
CStrings:
+ "SELECT DISTINCT (fetchable_artwork_token), best_artwork_token.entity_pid FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token LEFT OUTER JOIN entity_revision ON (entity_revision.entity_pid = best_artwork_token.entity_pid) WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? AND entity_revision.revision > ? GROUP BY fetchable_artwork_token"
+ "SELECT DISTINCT (fetchable_artwork_token), store_cloud_id FROM best_artwork_token LEFT OUTER JOIN artwork ON (fetchable_artwork_token = artwork_token) JOIN container ON (container_pid = best_artwork_token.entity_pid) LEFT OUTER JOIN entity_revision ON (entity_revision.entity_pid = best_artwork_token.entity_pid) WHERE artwork_token IS NULL AND best_artwork_token.entity_type = ? AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? AND entity_revision.revision > ? GROUP BY fetchable_artwork_token"
+ "SELECT DISTINCT (fetchable_artwork_token), store_saga_id, media_type FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token JOIN item_store ON best_artwork_token.entity_pid = item_store.item_pid JOIN item USING (item_pid) LEFT OUTER JOIN entity_revision ON (entity_revision.entity_pid = item_store.item_pid) WHERE artwork_token IS NULL AND best_artwork_token.entity_type = ? AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? AND entity_revision.revision > ? GROUP BY fetchable_artwork_token"
+ "_importOriginalContainerArtworkForEntitiesChangedSinceRevision:withClientIdentity:"
+ "_importOriginalItemArtworkForEntitiesChangedSinceRevision:withClientIdentity:"
+ "artwork_operation(%llu, %ld, %ld, %ld)"
+ "importAllItemArtworkForEntitiesChangedSinceRevision:withClientIdentity:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
- "SELECT DISTINCT (fetchable_artwork_token), entity_pid FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? GROUP BY fetchable_artwork_token"
- "SELECT DISTINCT (fetchable_artwork_token), store_cloud_id FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token JOIN container ON entity_pid = container_pid AND entity_type = ? WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? GROUP BY fetchable_artwork_token"
- "SELECT DISTINCT (fetchable_artwork_token), store_saga_id, media_type FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token JOIN item_store ON entity_pid = item_store.item_pid AND entity_type = ? JOIN item USING (item_pid) WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? GROUP BY fetchable_artwork_token"
- "_importOriginalContainerArtworkWithClientIdentity:"
- "artwork_operation(%llu, %ld, %ld)"

```
