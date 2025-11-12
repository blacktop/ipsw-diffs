## DeviceRecoveryBrainSupport

> `/System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport`

```diff

 103.60.1.0.5
-  __TEXT.__text: 0x1d860
+  __TEXT.__text: 0x1df74
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_methlist: 0xd1c
   __TEXT.__const: 0x150
   __TEXT.__oslogstring: 0x2bf1
   __TEXT.__cstring: 0x3d6d
-  __TEXT.__gcc_except_tab: 0x5bc
+  __TEXT.__gcc_except_tab: 0x5c0
   __TEXT.__unwind_info: 0x560
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x16b

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4E0F977-898F-370D-9A27-18BA6D2E1886
+  UUID: 98473DBC-ED55-3FAD-8CBD-73E53FB86130
   Functions: 529
   Symbols:   1328
   CStrings:  1470
Functions:
~ +[LPStaticAPFSContainer _containerWithPhysticalStoreRole:] : 540 -> 560
~ -[LPStaticAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:] : 2620 -> 2820
~ -[LPStaticAPFSContainer physicalStores] : 684 -> 704
~ -[LPStaticAPFSPhysicalStore role] : 296 -> 316
~ -[LPStaticAPFSPhysicalStore parent] : 684 -> 704
~ -[LPStaticAPFSVolume role] : 620 -> 640
~ -[LPStaticAPFSVolume snapshotMountPoints] : 712 -> 732
~ -[LPStaticAPFSVolume eraseVolumeWithError:] : 380 -> 400
~ -[LPStaticAPFSVolume mountAtPath:options:error:] : 2440 -> 2600
~ -[LPStaticAPFSVolume unmountWithOptions:error:] : 2716 -> 2896
~ -[LPStaticAPFSVolume deleteVolumeWithError:] : 868 -> 948
~ -[LPStaticAPFSVolume snapshotInfoWithError:] : 1656 -> 1756
~ -[LPStaticAPFSVolume createSnapshot:error:] : 880 -> 960
~ -[LPStaticAPFSVolume deleteSnapshots:waitForDeletionFor:error:] : 1428 -> 1528
~ -[LPStaticAPFSVolume renameSnapshot:to:error:] : 1056 -> 1156
~ -[LPStaticAPFSVolume revertToSnapshot:options:error:] : 1336 -> 1476
~ -[LPStaticAPFSVolume rootToSnapshot:error:] : 960 -> 1060
~ +[LPStaticMedia allMedia] : 452 -> 472
~ +[LPStaticMedia snapshotNameForMediaForPath:] : 1588 -> 1700
~ +[LPStaticMedia liveMediaForSnapshotAtPath:] : 792 -> 872
~ -[LPStaticMedia wholeMediaForMedia] : 528 -> 548
~ -[LPStaticMedia setName:withError:] : 732 -> 772
~ -[LPStaticMedia isReadOnly] : 320 -> 340
~ -[LPStaticMedia isJournaled] : 324 -> 344
~ +[LPStaticMedia _copyIOMediaForDiskWithPath:] : 448 -> 468
~ +[LPStaticMedia _copyLiveFilesystemIOMediaForRootedSnapshot] : 556 -> 576
~ +[LPStaticMedia(Private) waitForIOMediaWithDevNode:] : 476 -> 516
~ +[LPStaticMedia(Private) waitForBlockStorage] : 368 -> 388
~ -[LPStaticPartitionMedia children] : 532 -> 552

```
