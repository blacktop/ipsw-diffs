## MusicLibrary

> `/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary`

```diff

-4024.600.7.0.0
-  __TEXT.__text: 0x6c6b4
+4025.100.95.0.0
+  __TEXT.__text: 0x743b8
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_stubs: 0x4b80
-  __TEXT.__objc_methlist: 0x117c
+  __TEXT.__objc_stubs: 0x4c60
+  __TEXT.__objc_methlist: 0x119c
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__const: 0xf658
-  __TEXT.__gcc_except_tab: 0xe6c
-  __TEXT.__objc_methname: 0x5cee
+  __TEXT.__const: 0xf6d4
+  __TEXT.__gcc_except_tab: 0xe80
+  __TEXT.__objc_methname: 0x5e79
   __TEXT.__objc_classname: 0x224
-  __TEXT.__objc_methtype: 0xbe1
-  __TEXT.__cstring: 0x244d
-  __TEXT.__oslogstring: 0x45c1
-  __TEXT.__unwind_info: 0x930
-  __TEXT.__eh_frame: 0xda0
+  __TEXT.__objc_methtype: 0xbec
+  __TEXT.__cstring: 0x2633
+  __TEXT.__oslogstring: 0x4661
+  __TEXT.__unwind_info: 0x810
+  __TEXT.__eh_frame: 0x80
   __DATA_CONST.__auth_got: 0x448
-  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__got: 0x608
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x6550
-  __DATA_CONST.__cfstring: 0x18a0
+  __DATA_CONST.__const: 0x68d8
+  __DATA_CONST.__cfstring: 0x19a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_intobj: 0x378
+  __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_arraydata: 0x248
   __DATA_CONST.__objc_arrayobj: 0x2e8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1378
-  __DATA.__objc_selrefs: 0x1810
+  __DATA.__objc_const: 0x1380
+  __DATA.__objc_selrefs: 0x1850
   __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x11b8
-  __DATA.__bss: 0x1f8
-  __DATA.__common: 0x48
-  __DATA_DIRTY.__bss: 0x8
+  __DATA.__data: 0x7d0
+  __DATA.__bss: 0x200
+  __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 1DF42D42-4401-30E1-8D6B-502CEB096D42
-  Functions: 584
-  Symbols:   355
-  CStrings:  1743
+  UUID: F4F6B374-D5E0-3F03-BC61-0EB64F9E190D
+  Functions: 587
+  Symbols:   356
+  CStrings:  1771
 
Symbols:
+ _OBJC_CLASS_$_ML3LibraryPin
CStrings:
+ "MLSyncParamCanProcessLibraryPins"
+ "MLSyncParamMLSagaMaxAllowedLibraryPinCount"
+ "MusicKit"
+ "SELECT COUNT() from library_pins"
+ "SELECT cloud_library_id FROM album WHERE album_pid=?"
+ "SELECT cloud_universal_library_id FROM album_artist WHERE album_artist_pid=?"
+ "SELECT entity_pid, entity_type, default_action, position, position_uuid FROM library_pins ORDER BY position ASC"
+ "SELECT store_cloud_id FROM container WHERE container_pid=?"
+ "SELECT store_saga_id FROM item_store WHERE item_pid=?"
+ "_DMAPEntityKindFromMLEntityKind:"
+ "clearSagaMaxLibraryPinCount"
+ "enumerateLibraryPinsPersistentIDsAfterRevision:revisionTrackingCode:usingBlock:"
+ "exportLibraryPinWithCloudItemID:cloudLibraryID:defaultAtion:type:position:positionUUID:"
+ "failed to export pinned entity pid%lld, type=%ld, position=%d, sagaID=%lld, cloudLibraryID=%{public}@ err=%{public}@"
+ "i24@0:8q16"
+ "library_pins"
+ "runKeepLocalEvaluationAndDownloadAssetsForPinningChangeWithCompletionBlock:"
+ "sagaMaximumLibraryPinCount"
+ "setSagaMaximumLibraryPinCount:"
+ "stringValueForFirstRowAndColumn"
+ "updating cloud account id from paired device: %lld --> %lld, addEntityToLibraryWhenFavoritingBehavior=%{public}@, clientFeatures=%{public}@, maxPinCount=%d"
- "updating cloud account id from paired device: %lld --> %lld, addEntityToLibraryWhenFavoritingBehavior=%{public}@"

```
