## libpartition2_dynamic.dylib

> `/usr/lib/libpartition2_dynamic.dylib`

```diff

-3476.60.7.0.1
-  __TEXT.__text: 0xaf10
+3476.60.7.0.4
+  __TEXT.__text: 0xb624
   __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x584
   __TEXT.__const: 0xc8
   __TEXT.__oslogstring: 0x115f
   __TEXT.__cstring: 0xc86
-  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__gcc_except_tab: 0x90
   __TEXT.__unwind_info: 0x258
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0xc41

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C9A44577-2C7D-3806-9C16-6F1F88B46A83
+  UUID: 1470BCAC-ADF1-3378-ADF9-DBD4B0CB0F2D
   Functions: 143
   Symbols:   647
   CStrings:  537
Functions:
~ +[LPAPFSContainer _containerWithPhysticalStoreRole:] : 540 -> 560
~ -[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:] : 2436 -> 2636
~ -[LPAPFSContainer physicalStores] : 684 -> 704
~ -[LPAPFSPhysicalStore role] : 296 -> 316
~ -[LPAPFSPhysicalStore parent] : 684 -> 704
~ -[LPAPFSVolume role] : 620 -> 640
~ -[LPAPFSVolume snapshotMountPoints] : 712 -> 732
~ -[LPAPFSVolume eraseVolumeWithError:] : 380 -> 400
~ -[LPAPFSVolume mountAtPath:options:error:] : 2360 -> 2520
~ -[LPAPFSVolume unmountWithOptions:error:] : 2716 -> 2896
~ -[LPAPFSVolume deleteVolumeWithError:] : 868 -> 948
~ -[LPAPFSVolume snapshotInfoWithError:] : 1672 -> 1772
~ -[LPAPFSVolume createSnapshot:error:] : 880 -> 960
~ -[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:] : 1428 -> 1528
~ -[LPAPFSVolume renameSnapshot:to:error:] : 1056 -> 1156
~ -[LPAPFSVolume revertToSnapshot:options:error:] : 1336 -> 1476
~ -[LPAPFSVolume rootToSnapshot:error:] : 960 -> 1060
~ +[LPMedia allMedia] : 444 -> 464
~ +[LPMedia snapshotNameForMediaForPath:] : 1588 -> 1700
~ +[LPMedia liveMediaForSnapshotAtPath:] : 792 -> 872
~ -[LPMedia wholeMediaForMedia] : 528 -> 548
~ -[LPMedia setName:withError:] : 732 -> 772
~ -[LPMedia isReadOnly] : 320 -> 340
~ -[LPMedia isJournaled] : 324 -> 344
~ +[LPMedia _copyIOMediaForDiskWithPath:] : 448 -> 468
~ +[LPMedia _copyLiveFilesystemIOMediaForRootedSnapshot] : 556 -> 576
~ +[LPMedia(Private) waitForIOMediaWithDevNode:] : 476 -> 516
~ +[LPMedia(Private) waitForBlockStorage] : 368 -> 388
~ -[LPPartitionMedia children] : 520 -> 540

```
