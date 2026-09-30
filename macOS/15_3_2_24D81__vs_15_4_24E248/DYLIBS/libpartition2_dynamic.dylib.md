## libpartition2_dynamic.dylib

> `/usr/lib/libpartition2_dynamic.dylib`

```diff

-3148.80.1.0.2
-  __TEXT.__text: 0xb5f8
+3196.100.165.0.2
+  __TEXT.__text: 0xb520
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_methlist: 0x4e4
   __TEXT.__const: 0x170

   __TEXT.__objc_methname: 0xab0
   __TEXT.__objc_methtype: 0x118
   __TEXT.__objc_stubs: 0xbe0
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5822B6D8-42FB-34C5-A1C1-4170BE56FBA3
-  Functions: 120
-  Symbols:   457
+  UUID: 7833F2A3-3F9F-389E-B532-B3210540177E
+  Functions: 124
+  Symbols:   471
   CStrings:  498
 
Symbols:
+ +[LPAPFSVolume initialize].cold.1
+ +[LPMedia(Private) contentTypeToSubclassMap].cold.1
+ -[LPAPFSVolume _createTemporaryMountPointWithError:].cold.1
+ _LPLogObject.cold.1
+ _OBJC_CLASS_$_LPStaticAPFSContainer
+ _OBJC_CLASS_$_LPStaticAPFSPhysicalStore
+ _OBJC_CLASS_$_LPStaticAPFSVolume
+ _OBJC_CLASS_$_LPStaticMedia
+ _OBJC_CLASS_$_LPStaticPartitionMedia
+ _OBJC_METACLASS_$_LPStaticAPFSContainer
+ _OBJC_METACLASS_$_LPStaticAPFSPhysicalStore
+ _OBJC_METACLASS_$_LPStaticAPFSVolume
+ _OBJC_METACLASS_$_LPStaticMedia
+ _OBJC_METACLASS_$_LPStaticPartitionMedia
Functions:
~ -[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:] : 2472 -> 2448
~ -[LPAPFSContainer volumes] : 632 -> 628
~ +[LPAPFSVolume initialize] : 1076 -> 1060
~ +[LPAPFSVolume _loadMountPointTableForMode:] : 280 -> 276
~ +[LPAPFSVolume defaultVolumeNameGivenRole:] : 92 -> 88
~ -[LPAPFSVolume isEncrypted] : 104 -> 100
~ -[LPAPFSVolume isFilevaultEncrypted] : 104 -> 100
~ -[LPAPFSVolume snapshotMountPoints] : 720 -> 712
~ -[LPAPFSVolume _createTemporaryMountPointWithError:] : 464 -> 448
~ -[LPAPFSVolume mountAtPath:options:error:] : 2448 -> 2360
~ -[LPAPFSVolume unmountWithOptions:error:] : 2476 -> 2468
~ -[LPAPFSVolume snapshotInfoWithError:] : 1676 -> 1672
~ -[LPAPFSVolume createSnapshot:error:] : 900 -> 880
~ -[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:] : 1432 -> 1428
~ -[LPAPFSVolume renameSnapshot:to:error:] : 1060 -> 1056
~ -[LPAPFSVolume revertToSnapshot:options:error:] : 1344 -> 1336
~ __LPLogObject : 84 -> 68
~ __LPLogPack : 308 -> 304
~ +[LPMedia mediaForPath:snapshotName:] : 1748 -> 1740
~ +[LPMedia mediaForBSDNameOrDeviceNode:] : 292 -> 288
~ -[LPMedia setName:withError:] : 740 -> 732
~ -[LPMedia mountPoint] : 228 -> 224
~ -[LPMedia isReadOnly] : 336 -> 320
~ -[LPMedia isJournaled] : 336 -> 324
~ +[LPMedia _copyIOMediaForDiskWithPath:] : 452 -> 448
~ +[LPMedia(Private) contentTypeToSubclassMap] : 84 -> 68
~ +[LPMedia(Private) waitForIOMediaWithDevNode:] : 480 -> 476

```
