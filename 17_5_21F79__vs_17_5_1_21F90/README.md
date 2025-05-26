# 17.5 (21F79) .vs 17.5.1 (21F90)

## IPSWs

- `iPhone16,1_17.5_21F79_Restore.ipsw`
- `iPhone16,1_17.5.1_21F90_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.5 *(21F79)* | 23.5.0 | 10063.122.3~3 | Wed, 01May2024 20:34:22 PDT |
| 17.5.1 *(21F90)* | 23.5.0 | 10063.122.3~3 | Wed, 01May2024 20:34:22 PDT |

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### identityservicesd

>  `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1814.600.72.0.0
-  __TEXT.__text: 0x5fff10
+1814.600.72.2.1
+  __TEXT.__text: 0x5ffcd8
   __TEXT.__auth_stubs: 0x4940
-  __TEXT.__objc_stubs: 0x40260
-  __TEXT.__objc_methlist: 0x20b54
+  __TEXT.__objc_stubs: 0x40240
+  __TEXT.__objc_methlist: 0x20b4c
   __TEXT.__const: 0x3f860
-  __TEXT.__gcc_except_tab: 0x1b408
-  __TEXT.__objc_methname: 0x68c6d
-  __TEXT.__cstring: 0x52539
-  __TEXT.__oslogstring: 0x719f6
+  __TEXT.__gcc_except_tab: 0x1b3ec
+  __TEXT.__objc_methname: 0x68c45
+  __TEXT.__cstring: 0x52499
+  __TEXT.__oslogstring: 0x71955
   __TEXT.__objc_classname: 0x3c87
   __TEXT.__objc_methtype: 0xfddd
   __TEXT.__ustring: 0x52a

   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xd8c8
+  __TEXT.__unwind_info: 0xd8b8
   __TEXT.__eh_frame: 0x1ad0
   __DATA_CONST.__auth_got: 0x24b0
   __DATA_CONST.__got: 0x2110
   __DATA_CONST.__auth_ptr: 0xd8
   __DATA_CONST.__const: 0x19a08
-  __DATA_CONST.__cfstring: 0x31d20
+  __DATA_CONST.__cfstring: 0x31d00
   __DATA_CONST.__objc_classlist: 0xd18
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x5f8

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x40ec0
-  __DATA.__objc_selrefs: 0x13038
+  __DATA.__objc_selrefs: 0x13030
   __DATA.__objc_ivar: 0x2e5c
   __DATA.__objc_data: 0x9b18
   __DATA.__data: 0x6f68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17177
+  Functions: 17175
   Symbols:   2493
-  CStrings:  31665
+  CStrings:  31662
 
CStrings:
+ "20:15:23"
+ "May 15 2024"
+ "We received a last from storage from the server for topic %@"
- "23:09:13"
- "Apr 18 2024"
- "We processed last message from storage from the server for topic %@"
- "We received a last from storage from the server for topic %@, not terminating storage state machine until messages finish processing. Cancelling timeout."
- "processedLastMessageFromStorageForTopic:"

```


</details>

## Firmware

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2b3074
+  __TEXT.__text: 0x2b3084
   __TEXT.__const: 0x7b21c
   __TEXT.__cstring: 0x2d989
   __TEXT.__chain_starts: 0x160

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2b3074
+  __TEXT.__text: 0x2b3084
   __TEXT.__const: 0x7b21c
   __TEXT.__cstring: 0x2d989
   __TEXT.__chain_starts: 0x160

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.5 *(21F79)* | 618.2.12.10.9 |
| 17.5.1 *(21F90)* | 618.2.12.10.9 |

### Dylibs

#### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### AirTrafficDevice

>  `/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice`

```diff

-4023.610.2.0.0
-  __TEXT.__text: 0x112414
+4023.610.6.0.0
+  __TEXT.__text: 0x112454
   __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_methlist: 0x2b24
   __TEXT.__const: 0x15668

```

#### IDSFoundation

>  `/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation`

```diff

-1814.600.72.0.0
-  __TEXT.__text: 0x1acfb8
+1814.600.72.2.1
+  __TEXT.__text: 0x1ad044
   __TEXT.__auth_stubs: 0x24b0
-  __TEXT.__objc_methlist: 0x1497c
+  __TEXT.__objc_methlist: 0x14974
   __TEXT.__const: 0x508
   __TEXT.__oslogstring: 0x204fb
-  __TEXT.__cstring: 0x296e0
+  __TEXT.__cstring: 0x296bf
   __TEXT.__gcc_except_tab: 0x7a04
   __TEXT.__ustring: 0xc
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__unwind_info: 0x5260
   __TEXT.__objc_classname: 0x328c
-  __TEXT.__objc_methname: 0x2e621
+  __TEXT.__objc_methname: 0x2e5b5
   __TEXT.__objc_methtype: 0x6b3e
   __TEXT.__objc_stubs: 0x17600
   __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x5378
+  __DATA_CONST.__const: 0x5370
   __DATA_CONST.__objc_classlist: 0xcf0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x263b8
-  __DATA_CONST.__objc_selrefs: 0x8cb0
+  __DATA_CONST.__objc_const: 0x26388
+  __DATA_CONST.__objc_selrefs: 0x8ca8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_classrefs: 0xa28
   __DATA_CONST.__objc_superrefs: 0x978
   __DATA_CONST.__objc_arraydata: 0x14e0
   __AUTH_CONST.__objc_const: 0x9bd0
   __AUTH_CONST.__const: 0x1780
-  __AUTH_CONST.__cfstring: 0x25880
+  __AUTH_CONST.__cfstring: 0x25860
   __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__objc_intobj: 0xa98
   __AUTH_CONST.__objc_arrayobj: 0x1e78

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x1268
   __AUTH.__objc_data: 0x6cc0
-  __DATA.__objc_ivar: 0x2144
+  __DATA.__objc_ivar: 0x2140
   __DATA.__data: 0x1640
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x6b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8482
-  Symbols:   4209
-  CStrings:  16547
+  Functions: 8481
+  Symbols:   4208
+  CStrings:  16543
 
Symbols:
- _IDSServicePropertyDisablePersistMessagesOnVisionOS
CStrings:
- "DisablePersistMessagesOnVisionOS"
- "TB,R,N,V_disablePersistMessagesOnVisionOS"
- "_disablePersistMessagesOnVisionOS"
- "disablePersistMessagesOnVisionOS"

```

#### IntelligencePlatformCore

>  `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

 75.15.0.0.0
-  __TEXT.__text: 0xad540c
+  __TEXT.__text: 0xad53c4
   __TEXT.__auth_stubs: 0x9170
   __TEXT.__objc_methlist: 0x154c
   __TEXT.__const: 0x5a1b9
   __TEXT.__cstring: 0x54dea
   __TEXT.__swift5_typeref: 0x19ab0
   __TEXT.__constg_swiftt: 0x1e8d0
-  __TEXT.__swift5_reflstr: 0x23f8c
+  __TEXT.__swift5_reflstr: 0x23f6c
   __TEXT.__swift5_fieldmd: 0x1eac8
   __TEXT.__swift5_builtin: 0x438
   __TEXT.__swift5_mpenum: 0xf8

   __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__oslogstring: 0x385
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__unwind_info: 0x29060
+  __TEXT.__unwind_info: 0x29064
   __TEXT.__eh_frame: 0x55fb4
   __TEXT.__objc_classname: 0x488
   __TEXT.__objc_methname: 0x8baf

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 71464
+  Functions: 71505
   Symbols:   771
   CStrings:  8750
 

```

#### PencilPairingUI

>  `/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`

```diff

-136.15.0.0.0
-  __TEXT.__text: 0x1fcf0
+136.16.0.0.0
+  __TEXT.__text: 0x1fe98
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x2bac
+  __TEXT.__objc_methlist: 0x2bb4
   __TEXT.__const: 0x2b8
   __TEXT.__cstring: 0xe75
-  __TEXT.__oslogstring: 0x4f3
-  __TEXT.__gcc_except_tab: 0x1d8
+  __TEXT.__oslogstring: 0x5c3
+  __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0xad4
+  __TEXT.__unwind_info: 0xad0
   __TEXT.__objc_classname: 0x854
-  __TEXT.__objc_methname: 0x8447
+  __TEXT.__objc_methname: 0x847f
   __TEXT.__objc_methtype: 0x1a93
-  __TEXT.__objc_stubs: 0x6e60
+  __TEXT.__objc_stubs: 0x6ea0
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x748
   __DATA_CONST.__objc_classlist: 0x188

   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x8f80
-  __DATA_CONST.__objc_selrefs: 0x1fe8
+  __DATA_CONST.__objc_selrefs: 0x1ff8
   __DATA_CONST.__objc_classrefs: 0x368
   __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arraydata: 0x118
   __AUTH_CONST.__objc_const: 0x13e8
   __AUTH_CONST.__cfstring: 0x17c0
   __AUTH_CONST.__const: 0x280

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1026
-  Symbols:   4183
-  CStrings:  2013
+  Functions: 1027
+  Symbols:   4187
+  CStrings:  2020
 
Symbols:
+ -[PNPSqueezeThresholdController initializeToDefaultThresholdIfUninitialized]
+ __unnamed_array_storage.48
+ __unnamed_array_storage.51
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$initializeToDefaultThresholdIfUninitialized
- __unnamed_array_storage.31
- __unnamed_array_storage.50
CStrings:
+ "PNPWizardController exit"
+ "Setting PPUIHasSeenScribbleEducationPanelsKey: %d"
+ "Setting PPUIHasShownEducationUIKey"
+ "Setting PPUILastSeenWhatsNewVersionKey: %d"
+ "Squeeze threshold already set in backboard: %@"
+ "boolForKey:"
+ "initializeToDefaultThresholdIfUninitialized"
- "Synchronizing squeeze threshold: %@"

```

#### PhotoLibraryServices

>  `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices`

```diff

-652.0.100.0.0
-  __TEXT.__text: 0x5b6410
+652.0.110.0.0
+  __TEXT.__text: 0x5b63d4
   __TEXT.__auth_stubs: 0x3f10
   __TEXT.__objc_methlist: 0x33774
   __TEXT.__const: 0x5638

   __DATA_CONST.__objc_const: 0x4d080
   __DATA_CONST.__objc_selrefs: 0x1ef98
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_classrefs: 0x2350
+  __DATA_CONST.__objc_classrefs: 0x2348
   __DATA_CONST.__objc_superrefs: 0x1250
   __DATA_CONST.__objc_arraydata: 0x1468
   __AUTH_CONST.__const: 0x4bb8
Symbols:
+ _DataMigrationLibrary.73001
+ _DataMigrationLibraryCore.frameworkLibrary.73010
+ _MobileBackupLibraryCore.frameworkLibrary.73062
+ _NeutrinoCoreLibraryCore.frameworkLibrary.61020
+ _PSIRowIDCompare.102822
+ _PSIRowIDCompare.96004
+ _PhotoImagingLibrary.60850
+ _PhotoImagingLibraryCore.frameworkLibrary.60860
+ _PhotoImagingLibraryCore.frameworkLibrary.71938
+ ___100-[PLModelMigrationAction_LibraryScopeTrashedStateFixup performActionWithManagedObjectContext:error:]_block_invoke.283
+ ___101-[PLModelMigrationAction_PushAssetsWithPetSyncableFaces performActionWithManagedObjectContext:error:]_block_invoke.228
+ ___103-[PLModelMigrationAction_PopulatePersonCloudDetectionType performActionWithManagedObjectContext:error:]_block_invoke.295
+ ___106-[PLModelMigrationAction_MergeDetectedFacesAndDetectedTorsos performActionWithManagedObjectContext:error:]_block_invoke.251
+ ___109-[PLModelMigrationAction_CopyStickerConfidenceScoreToAssetTable performActionWithManagedObjectContext:error:]_block_invoke.268
+ ___193-[PLModelMigrationAction_DeletePetPersonsAndDetectedFaces deleteManagedObjectsWithManagedObjectContext:entity:predicate:pendingParentUnitCount:deletedIdentifiers:entityIdentifierKeyPath:error:]_block_invoke.162
+ ___Block_byref_object_copy_.100169
+ ___Block_byref_object_copy_.100972
+ ___Block_byref_object_copy_.102803
+ ___Block_byref_object_copy_.46556
+ ___Block_byref_object_copy_.46798
+ ___Block_byref_object_copy_.47387
+ ___Block_byref_object_copy_.47971
+ ___Block_byref_object_copy_.48727
+ ___Block_byref_object_copy_.49858
+ ___Block_byref_object_copy_.51787
+ ___Block_byref_object_copy_.51968
+ ___Block_byref_object_copy_.52752
+ ___Block_byref_object_copy_.52954
+ ___Block_byref_object_copy_.53245
+ ___Block_byref_object_copy_.53780
+ ___Block_byref_object_copy_.55770
+ ___Block_byref_object_copy_.56731
+ ___Block_byref_object_copy_.57052
+ ___Block_byref_object_copy_.57460
+ ___Block_byref_object_copy_.58150
+ ___Block_byref_object_copy_.59210
+ ___Block_byref_object_copy_.59652
+ ___Block_byref_object_copy_.60205
+ ___Block_byref_object_copy_.62975
+ ___Block_byref_object_copy_.63366
+ ___Block_byref_object_copy_.63799
+ ___Block_byref_object_copy_.64335
+ ___Block_byref_object_copy_.64687
+ ___Block_byref_object_copy_.65480
+ ___Block_byref_object_copy_.65723
+ ___Block_byref_object_copy_.66664
+ ___Block_byref_object_copy_.66877
+ ___Block_byref_object_copy_.67489
+ ___Block_byref_object_copy_.67662
+ ___Block_byref_object_copy_.67886
+ ___Block_byref_object_copy_.68535
+ ___Block_byref_object_copy_.69672
+ ___Block_byref_object_copy_.71056
+ ___Block_byref_object_copy_.71801
+ ___Block_byref_object_copy_.72604
+ ___Block_byref_object_copy_.72995
+ ___Block_byref_object_copy_.73326
+ ___Block_byref_object_copy_.74868
+ ___Block_byref_object_copy_.76019
+ ___Block_byref_object_copy_.76857
+ ___Block_byref_object_copy_.77589
+ ___Block_byref_object_copy_.78751
+ ___Block_byref_object_copy_.79221
+ ___Block_byref_object_copy_.79401
+ ___Block_byref_object_copy_.79533
+ ___Block_byref_object_copy_.81906
+ ___Block_byref_object_copy_.82456
+ ___Block_byref_object_copy_.82756
+ ___Block_byref_object_copy_.82916
+ ___Block_byref_object_copy_.86433
+ ___Block_byref_object_copy_.86739
+ ___Block_byref_object_copy_.87014
+ ___Block_byref_object_copy_.87526
+ ___Block_byref_object_copy_.87794
+ ___Block_byref_object_copy_.88467
+ ___Block_byref_object_copy_.90307
+ ___Block_byref_object_copy_.92467
+ ___Block_byref_object_copy_.93190
+ ___Block_byref_object_copy_.94203
+ ___Block_byref_object_copy_.94846
+ ___Block_byref_object_copy_.95871
+ ___Block_byref_object_copy_.96379
+ ___Block_byref_object_copy_.96628
+ ___Block_byref_object_copy_.97160
+ ___Block_byref_object_copy_.97231
+ ___Block_byref_object_copy_.97761
+ ___Block_byref_object_copy_.98150
+ ___Block_byref_object_copy_.98351
+ ___Block_byref_object_copy_.98502
+ ___Block_byref_object_copy_.98569
+ ___Block_byref_object_copy_.99561
+ ___Block_byref_object_dispose_.100170
+ ___Block_byref_object_dispose_.100973
+ ___Block_byref_object_dispose_.102804
+ ___Block_byref_object_dispose_.46557
+ ___Block_byref_object_dispose_.46799
+ ___Block_byref_object_dispose_.47388
+ ___Block_byref_object_dispose_.47972
+ ___Block_byref_object_dispose_.48728
+ ___Block_byref_object_dispose_.49859
+ ___Block_byref_object_dispose_.51788
+ ___Block_byref_object_dispose_.51969
+ ___Block_byref_object_dispose_.52753
+ ___Block_byref_object_dispose_.52955
+ ___Block_byref_object_dispose_.53246
+ ___Block_byref_object_dispose_.53781
+ ___Block_byref_object_dispose_.55771
+ ___Block_byref_object_dispose_.56732
+ ___Block_byref_object_dispose_.57053
+ ___Block_byref_object_dispose_.57461
+ ___Block_byref_object_dispose_.58151
+ ___Block_byref_object_dispose_.59211
+ ___Block_byref_object_dispose_.59653
+ ___Block_byref_object_dispose_.60206
+ ___Block_byref_object_dispose_.62976
+ ___Block_byref_object_dispose_.63367
+ ___Block_byref_object_dispose_.63800
+ ___Block_byref_object_dispose_.64336
+ ___Block_byref_object_dispose_.64688
+ ___Block_byref_object_dispose_.65481
+ ___Block_byref_object_dispose_.65724
+ ___Block_byref_object_dispose_.66665
+ ___Block_byref_object_dispose_.66878
+ ___Block_byref_object_dispose_.67490
+ ___Block_byref_object_dispose_.67663
+ ___Block_byref_object_dispose_.67887
+ ___Block_byref_object_dispose_.68536
+ ___Block_byref_object_dispose_.69673
+ ___Block_byref_object_dispose_.71057
+ ___Block_byref_object_dispose_.71802
+ ___Block_byref_object_dispose_.72605
+ ___Block_byref_object_dispose_.72996
+ ___Block_byref_object_dispose_.73327
+ ___Block_byref_object_dispose_.74869
+ ___Block_byref_object_dispose_.76020
+ ___Block_byref_object_dispose_.76858
+ ___Block_byref_object_dispose_.77590
+ ___Block_byref_object_dispose_.78752
+ ___Block_byref_object_dispose_.79222
+ ___Block_byref_object_dispose_.79402
+ ___Block_byref_object_dispose_.79534
+ ___Block_byref_object_dispose_.81907
+ ___Block_byref_object_dispose_.82457
+ ___Block_byref_object_dispose_.82757
+ ___Block_byref_object_dispose_.82917
+ ___Block_byref_object_dispose_.86434
+ ___Block_byref_object_dispose_.86740
+ ___Block_byref_object_dispose_.87015
+ ___Block_byref_object_dispose_.87527
+ ___Block_byref_object_dispose_.87795
+ ___Block_byref_object_dispose_.88468
+ ___Block_byref_object_dispose_.90308
+ ___Block_byref_object_dispose_.92468
+ ___Block_byref_object_dispose_.93191
+ ___Block_byref_object_dispose_.94204
+ ___Block_byref_object_dispose_.94847
+ ___Block_byref_object_dispose_.95872
+ ___Block_byref_object_dispose_.96380
+ ___Block_byref_object_dispose_.96629
+ ___Block_byref_object_dispose_.97161
+ ___Block_byref_object_dispose_.97232
+ ___Block_byref_object_dispose_.97762
+ ___Block_byref_object_dispose_.98151
+ ___Block_byref_object_dispose_.98352
+ ___Block_byref_object_dispose_.98503
+ ___Block_byref_object_dispose_.98570
+ ___Block_byref_object_dispose_.99562
+ ___DataMigrationLibraryCore_block_invoke.73011
+ ___MobileBackupLibraryCore_block_invoke.73063
+ ___NeutrinoCoreLibraryCore_block_invoke.61021
+ ___PhotoImagingLibraryCore_block_invoke.60861
+ ___PhotoImagingLibraryCore_block_invoke.71939
+ ____PLGetPlaceNamesSortedByCategory_block_invoke.96095
+ ___block_literal_global.10.97051
+ ___block_literal_global.100122
+ ___block_literal_global.100662
+ ___block_literal_global.100821
+ ___block_literal_global.101229
+ ___block_literal_global.101693
+ ___block_literal_global.102195
+ ___block_literal_global.102400
+ ___block_literal_global.104.77701
+ ___block_literal_global.11.98531
+ ___block_literal_global.110.99348
+ ___block_literal_global.112.79223
+ ___block_literal_global.114.79200
+ ___block_literal_global.118.60459
+ ___block_literal_global.118.64996
+ ___block_literal_global.12.97045
+ ___block_literal_global.122.53572
+ ___block_literal_global.122.64998
+ ___block_literal_global.123.90096
+ ___block_literal_global.148.47135
+ ___block_literal_global.158.54656
+ ___block_literal_global.158.99314
+ ___block_literal_global.161.99309
+ ___block_literal_global.162.87033
+ ___block_literal_global.163.54664
+ ___block_literal_global.168.54672
+ ___block_literal_global.178.54686
+ ___block_literal_global.183.99294
+ ___block_literal_global.190.90809
+ ___block_literal_global.23.81242
+ ___block_literal_global.25.65440
+ ___block_literal_global.27.82157
+ ___block_literal_global.3.83796
+ ___block_literal_global.33.94169
+ ___block_literal_global.340.63157
+ ___block_literal_global.36.81155
+ ___block_literal_global.36.99409
+ ___block_literal_global.363.96560
+ ___block_literal_global.37.56375
+ ___block_literal_global.37.81231
+ ___block_literal_global.38.54312
+ ___block_literal_global.39.102393
+ ___block_literal_global.39.78445
+ ___block_literal_global.404.63141
+ ___block_literal_global.46601
+ ___block_literal_global.47002
+ ___block_literal_global.47797
+ ___block_literal_global.49211
+ ___block_literal_global.49387
+ ___block_literal_global.49504
+ ___block_literal_global.49672
+ ___block_literal_global.51.55854
+ ___block_literal_global.51685
+ ___block_literal_global.52636
+ ___block_literal_global.53056
+ ___block_literal_global.53714
+ ___block_literal_global.53887
+ ___block_literal_global.54050
+ ___block_literal_global.54328
+ ___block_literal_global.54648
+ ___block_literal_global.55018
+ ___block_literal_global.55152
+ ___block_literal_global.55851
+ ___block_literal_global.56115
+ ___block_literal_global.56373
+ ___block_literal_global.56733
+ ___block_literal_global.57030
+ ___block_literal_global.57213
+ ___block_literal_global.57278
+ ___block_literal_global.57900
+ ___block_literal_global.58111
+ ___block_literal_global.58601
+ ___block_literal_global.60467
+ ___block_literal_global.61581
+ ___block_literal_global.62.54309
+ ___block_literal_global.62010
+ ___block_literal_global.62559
+ ___block_literal_global.63070
+ ___block_literal_global.63483
+ ___block_literal_global.64.49594
+ ___block_literal_global.64.58112
+ ___block_literal_global.64088
+ ___block_literal_global.64147
+ ___block_literal_global.64167
+ ___block_literal_global.65029
+ ___block_literal_global.65441
+ ___block_literal_global.65986
+ ___block_literal_global.66182
+ ___block_literal_global.66904
+ ___block_literal_global.66977
+ ___block_literal_global.67111
+ ___block_literal_global.67469
+ ___block_literal_global.68662
+ ___block_literal_global.69.49358
+ ___block_literal_global.69643
+ ___block_literal_global.72.65024
+ ___block_literal_global.72028
+ ___block_literal_global.72595
+ ___block_literal_global.73077
+ ___block_literal_global.73241
+ ___block_literal_global.73396
+ ___block_literal_global.74717
+ ___block_literal_global.74904
+ ___block_literal_global.75174
+ ___block_literal_global.75732
+ ___block_literal_global.76.49361
+ ___block_literal_global.76396
+ ___block_literal_global.76554
+ ___block_literal_global.77292
+ ___block_literal_global.77568
+ ___block_literal_global.77780
+ ___block_literal_global.78484
+ ___block_literal_global.79.100615
+ ___block_literal_global.79.74861
+ ___block_literal_global.79235
+ ___block_literal_global.79309
+ ___block_literal_global.79331
+ ___block_literal_global.80.77276
+ ___block_literal_global.81.49658
+ ___block_literal_global.81158
+ ___block_literal_global.81248
+ ___block_literal_global.81946
+ ___block_literal_global.82.98165
+ ___block_literal_global.82011
+ ___block_literal_global.82160
+ ___block_literal_global.82739
+ ___block_literal_global.83392
+ ___block_literal_global.83804
+ ___block_literal_global.83931
+ ___block_literal_global.84156
+ ___block_literal_global.85.49364
+ ___block_literal_global.85791
+ ___block_literal_global.87047
+ ___block_literal_global.87510
+ ___block_literal_global.88.49367
+ ___block_literal_global.88419
+ ___block_literal_global.89.53957
+ ___block_literal_global.89.77767
+ ___block_literal_global.89453
+ ___block_literal_global.90098
+ ___block_literal_global.90210
+ ___block_literal_global.90811
+ ___block_literal_global.91.53958
+ ___block_literal_global.91.77762
+ ___block_literal_global.91043
+ ___block_literal_global.91769
+ ___block_literal_global.92239
+ ___block_literal_global.92333
+ ___block_literal_global.92621
+ ___block_literal_global.93.89454
+ ___block_literal_global.93750
+ ___block_literal_global.94065
+ ___block_literal_global.94168
+ ___block_literal_global.95447
+ ___block_literal_global.95789
+ ___block_literal_global.95853
+ ___block_literal_global.95996
+ ___block_literal_global.96155
+ ___block_literal_global.96831
+ ___block_literal_global.97.53034
+ ___block_literal_global.97.89388
+ ___block_literal_global.97056
+ ___block_literal_global.98164
+ ___block_literal_global.98529
+ ___block_literal_global.99429
+ ___block_literal_global.99681
+ ___block_literal_global.99751
+ ___getDMIsMigrationNeededSymbolLoc_block_invoke.73023
+ ___getMBManagerClass_block_invoke.73055
+ ___getPIPhotoEditHelperClass_block_invoke.60913
+ ___getPIPhotoEditHelperClass_block_invoke.71937
+ __downloadOriginalsChanged.53908
+ __unnamed_array_storage.100789
+ __unnamed_array_storage.101205
+ __unnamed_array_storage.102438
+ __unnamed_array_storage.102716
+ __unnamed_array_storage.150.97812
+ __unnamed_array_storage.159.102439
+ __unnamed_array_storage.182
+ __unnamed_array_storage.222
+ __unnamed_array_storage.44.99886
+ __unnamed_array_storage.46524
+ __unnamed_array_storage.52344
+ __unnamed_array_storage.52782
+ __unnamed_array_storage.53302
+ __unnamed_array_storage.54031
+ __unnamed_array_storage.54332
+ __unnamed_array_storage.55913
+ __unnamed_array_storage.57177
+ __unnamed_array_storage.60.84422
+ __unnamed_array_storage.60973
+ __unnamed_array_storage.61672
+ __unnamed_array_storage.62.95469
+ __unnamed_array_storage.63161
+ __unnamed_array_storage.65.95468
+ __unnamed_array_storage.65508
+ __unnamed_array_storage.68508
+ __unnamed_array_storage.69039
+ __unnamed_array_storage.69387
+ __unnamed_array_storage.71023
+ __unnamed_array_storage.75159
+ __unnamed_array_storage.81939
+ __unnamed_array_storage.84449
+ __unnamed_array_storage.84561
+ __unnamed_array_storage.85795
+ __unnamed_array_storage.86147
+ __unnamed_array_storage.86589
+ __unnamed_array_storage.87520
+ __unnamed_array_storage.87806
+ __unnamed_array_storage.88410
+ __unnamed_array_storage.89070
+ __unnamed_array_storage.89373
+ __unnamed_array_storage.92151
+ __unnamed_array_storage.95460
+ __unnamed_array_storage.96892
+ __unnamed_array_storage.97818
+ __unnamed_array_storage.99288
+ __unnamed_array_storage.99666
+ __unnamed_array_storage.99885
+ _audit_stringDataMigration.73013
+ _audit_stringMobileBackup.73071
+ _audit_stringNeutrinoCore.61024
+ _audit_stringPhotoImaging.60867
+ _audit_stringPhotoImaging.71950
+ _baseSearchIndexPredicate.onceToken.96154
+ _baseSearchIndexPredicate.predicate.96156
+ _getDMIsMigrationNeededSymbolLoc.ptr.73022
+ _getMBManagerClass.softClass.73054
+ _getPIPhotoEditHelperClass.60911
+ _getPIPhotoEditHelperClass.71935
+ _getPIPhotoEditHelperClass.softClass.60912
+ _getPIPhotoEditHelperClass.softClass.71936
+ _indexArrayCopyDescription.57907
+ _isEligibleForSearchIndexingPredicate.onceToken.66181
+ _isEligibleForSearchIndexingPredicate.onceToken.90209
+ _isEligibleForSearchIndexingPredicate.predicate.66183
+ _isEligibleForSearchIndexingPredicate.predicate.90211
+ _isSyncableChange.didSetupSyncedProperties.87372
+ _isSyncableChange.syncedProperties.87373
+ _listOfSyncedProperties.didSetupSyncedProperties.68523
+ _listOfSyncedProperties.didSetupSyncedProperties.73452
+ _listOfSyncedProperties.didSetupSyncedProperties.74606
+ _listOfSyncedProperties.didSetupSyncedProperties.75091
+ _listOfSyncedProperties.result.68524
+ _listOfSyncedProperties.result.73453
+ _listOfSyncedProperties.result.74607
+ _listOfSyncedProperties.result.75092
+ _listOfSyncedProperties.result.96231
+ _modelProperties.modelProperties.50893
+ _modelProperties.modelProperties.54741
+ _modelProperties.modelProperties.61257
+ _modelProperties.modelProperties.68206
+ _modelProperties.modelProperties.70377
+ _modelProperties.modelProperties.81450
+ _modelProperties.modelProperties.83833
+ _modelProperties.modelProperties.84491
+ _modelProperties.modelProperties.86601
+ _modelProperties.modelProperties.87108
+ _modelProperties.onceToken.50892
+ _modelProperties.onceToken.54740
+ _modelProperties.onceToken.61256
+ _modelProperties.onceToken.68205
+ _modelProperties.onceToken.70376
+ _modelProperties.onceToken.81449
+ _modelProperties.onceToken.83832
+ _modelProperties.onceToken.84490
+ _modelProperties.onceToken.86600
+ _modelProperties.onceToken.87107
+ _persistedPropertyNamesForEntityNames.onceToken.50890
+ _persistedPropertyNamesForEntityNames.onceToken.54738
+ _persistedPropertyNamesForEntityNames.onceToken.61254
+ _persistedPropertyNamesForEntityNames.onceToken.68203
+ _persistedPropertyNamesForEntityNames.onceToken.70374
+ _persistedPropertyNamesForEntityNames.onceToken.81447
+ _persistedPropertyNamesForEntityNames.onceToken.83830
+ _persistedPropertyNamesForEntityNames.onceToken.84488
+ _persistedPropertyNamesForEntityNames.onceToken.86598
+ _persistedPropertyNamesForEntityNames.onceToken.87105
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.50891
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.54739
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.61255
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.68204
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.70375
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.81448
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.83831
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.84489
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.86599
+ _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.87106
+ _s_lock.51358
+ _sharedManager.onceToken.72027
+ _sharedManager.onceToken.96397
- _DataMigrationLibrary.72990
- _DataMigrationLibraryCore.frameworkLibrary.72999
- _MobileBackupLibraryCore.frameworkLibrary.73051
- _NeutrinoCoreLibraryCore.frameworkLibrary.61009
- _PSIRowIDCompare.102812
- _PSIRowIDCompare.95994
- _PhotoImagingLibrary.60839
- _PhotoImagingLibraryCore.frameworkLibrary.60849
- _PhotoImagingLibraryCore.frameworkLibrary.71927
- ___100-[PLModelMigrationAction_LibraryScopeTrashedStateFixup performActionWithManagedObjectContext:error:]_block_invoke.284
- ___101-[PLModelMigrationAction_PushAssetsWithPetSyncableFaces performActionWithManagedObjectContext:error:]_block_invoke.229
- ___103-[PLModelMigrationAction_PopulatePersonCloudDetectionType performActionWithManagedObjectContext:error:]_block_invoke.296
- ___106-[PLModelMigrationAction_MergeDetectedFacesAndDetectedTorsos performActionWithManagedObjectContext:error:]_block_invoke.252
- ___109-[PLModelMigrationAction_CopyStickerConfidenceScoreToAssetTable performActionWithManagedObjectContext:error:]_block_invoke.269
- ___193-[PLModelMigrationAction_DeletePetPersonsAndDetectedFaces deleteManagedObjectsWithManagedObjectContext:entity:predicate:pendingParentUnitCount:deletedIdentifiers:entityIdentifierKeyPath:error:]_block_invoke.163
- ___Block_byref_object_copy_.100160
- ___Block_byref_object_copy_.100963
- ___Block_byref_object_copy_.102793
- ___Block_byref_object_copy_.46553
- ___Block_byref_object_copy_.46788
- ___Block_byref_object_copy_.47378
- ___Block_byref_object_copy_.47962
- ___Block_byref_object_copy_.48717
- ___Block_byref_object_copy_.49846
- ___Block_byref_object_copy_.51775
- ___Block_byref_object_copy_.51956
- ___Block_byref_object_copy_.52739
- ___Block_byref_object_copy_.52941
- ___Block_byref_object_copy_.53232
- ___Block_byref_object_copy_.53766
- ___Block_byref_object_copy_.55757
- ___Block_byref_object_copy_.56718
- ___Block_byref_object_copy_.57039
- ___Block_byref_object_copy_.57447
- ___Block_byref_object_copy_.58137
- ___Block_byref_object_copy_.59198
- ___Block_byref_object_copy_.59640
- ___Block_byref_object_copy_.60194
- ___Block_byref_object_copy_.62964
- ___Block_byref_object_copy_.63355
- ___Block_byref_object_copy_.63788
- ___Block_byref_object_copy_.64324
- ___Block_byref_object_copy_.64676
- ___Block_byref_object_copy_.65469
- ___Block_byref_object_copy_.65712
- ___Block_byref_object_copy_.66653
- ___Block_byref_object_copy_.66866
- ___Block_byref_object_copy_.67478
- ___Block_byref_object_copy_.67651
- ___Block_byref_object_copy_.67875
- ___Block_byref_object_copy_.68524
- ___Block_byref_object_copy_.69661
- ___Block_byref_object_copy_.71045
- ___Block_byref_object_copy_.71790
- ___Block_byref_object_copy_.72593
- ___Block_byref_object_copy_.72984
- ___Block_byref_object_copy_.73315
- ___Block_byref_object_copy_.74857
- ___Block_byref_object_copy_.76008
- ___Block_byref_object_copy_.76846
- ___Block_byref_object_copy_.77578
- ___Block_byref_object_copy_.78740
- ___Block_byref_object_copy_.79210
- ___Block_byref_object_copy_.79390
- ___Block_byref_object_copy_.79522
- ___Block_byref_object_copy_.81895
- ___Block_byref_object_copy_.82445
- ___Block_byref_object_copy_.82745
- ___Block_byref_object_copy_.82905
- ___Block_byref_object_copy_.86422
- ___Block_byref_object_copy_.86728
- ___Block_byref_object_copy_.87003
- ___Block_byref_object_copy_.87517
- ___Block_byref_object_copy_.87785
- ___Block_byref_object_copy_.88458
- ___Block_byref_object_copy_.90298
- ___Block_byref_object_copy_.92458
- ___Block_byref_object_copy_.93181
- ___Block_byref_object_copy_.94194
- ___Block_byref_object_copy_.94837
- ___Block_byref_object_copy_.95861
- ___Block_byref_object_copy_.96369
- ___Block_byref_object_copy_.96618
- ___Block_byref_object_copy_.97149
- ___Block_byref_object_copy_.97220
- ___Block_byref_object_copy_.97750
- ___Block_byref_object_copy_.98139
- ___Block_byref_object_copy_.98340
- ___Block_byref_object_copy_.98491
- ___Block_byref_object_copy_.98558
- ___Block_byref_object_copy_.99553
- ___Block_byref_object_dispose_.100161
- ___Block_byref_object_dispose_.100964
- ___Block_byref_object_dispose_.102794
- ___Block_byref_object_dispose_.46554
- ___Block_byref_object_dispose_.46789
- ___Block_byref_object_dispose_.47379
- ___Block_byref_object_dispose_.47963
- ___Block_byref_object_dispose_.48718
- ___Block_byref_object_dispose_.49847
- ___Block_byref_object_dispose_.51776
- ___Block_byref_object_dispose_.51957
- ___Block_byref_object_dispose_.52740
- ___Block_byref_object_dispose_.52942
- ___Block_byref_object_dispose_.53233
- ___Block_byref_object_dispose_.53767
- ___Block_byref_object_dispose_.55758
- ___Block_byref_object_dispose_.56719
- ___Block_byref_object_dispose_.57040
- ___Block_byref_object_dispose_.57448
- ___Block_byref_object_dispose_.58138
- ___Block_byref_object_dispose_.59199
- ___Block_byref_object_dispose_.59641
- ___Block_byref_object_dispose_.60195
- ___Block_byref_object_dispose_.62965
- ___Block_byref_object_dispose_.63356
- ___Block_byref_object_dispose_.63789
- ___Block_byref_object_dispose_.64325
- ___Block_byref_object_dispose_.64677
- ___Block_byref_object_dispose_.65470
- ___Block_byref_object_dispose_.65713
- ___Block_byref_object_dispose_.66654
- ___Block_byref_object_dispose_.66867
- ___Block_byref_object_dispose_.67479
- ___Block_byref_object_dispose_.67652
- ___Block_byref_object_dispose_.67876
- ___Block_byref_object_dispose_.68525
- ___Block_byref_object_dispose_.69662
- ___Block_byref_object_dispose_.71046
- ___Block_byref_object_dispose_.71791
- ___Block_byref_object_dispose_.72594
- ___Block_byref_object_dispose_.72985
- ___Block_byref_object_dispose_.73316
- ___Block_byref_object_dispose_.74858
- ___Block_byref_object_dispose_.76009
- ___Block_byref_object_dispose_.76847
- ___Block_byref_object_dispose_.77579
- ___Block_byref_object_dispose_.78741
- ___Block_byref_object_dispose_.79211
- ___Block_byref_object_dispose_.79391
- ___Block_byref_object_dispose_.79523
- ___Block_byref_object_dispose_.81896
- ___Block_byref_object_dispose_.82446
- ___Block_byref_object_dispose_.82746
- ___Block_byref_object_dispose_.82906
- ___Block_byref_object_dispose_.86423
- ___Block_byref_object_dispose_.86729
- ___Block_byref_object_dispose_.87004
- ___Block_byref_object_dispose_.87518
- ___Block_byref_object_dispose_.87786
- ___Block_byref_object_dispose_.88459
- ___Block_byref_object_dispose_.90299
- ___Block_byref_object_dispose_.92459
- ___Block_byref_object_dispose_.93182
- ___Block_byref_object_dispose_.94195
- ___Block_byref_object_dispose_.94838
- ___Block_byref_object_dispose_.95862
- ___Block_byref_object_dispose_.96370
- ___Block_byref_object_dispose_.96619
- ___Block_byref_object_dispose_.97150
- ___Block_byref_object_dispose_.97221
- ___Block_byref_object_dispose_.97751
- ___Block_byref_object_dispose_.98140
- ___Block_byref_object_dispose_.98341
- ___Block_byref_object_dispose_.98492
- ___Block_byref_object_dispose_.98559
- ___Block_byref_object_dispose_.99554
- ___DataMigrationLibraryCore_block_invoke.73000
- ___MobileBackupLibraryCore_block_invoke.73052
- ___NeutrinoCoreLibraryCore_block_invoke.61010
- ___PhotoImagingLibraryCore_block_invoke.60850
- ___PhotoImagingLibraryCore_block_invoke.71928
- ____PLGetPlaceNamesSortedByCategory_block_invoke.96085
- ___block_literal_global.10.97040
- ___block_literal_global.100113
- ___block_literal_global.100653
- ___block_literal_global.100812
- ___block_literal_global.101220
- ___block_literal_global.101684
- ___block_literal_global.102186
- ___block_literal_global.102391
- ___block_literal_global.104.77690
- ___block_literal_global.11.98520
- ___block_literal_global.110.99340
- ___block_literal_global.112.79212
- ___block_literal_global.114.79189
- ___block_literal_global.118.60448
- ___block_literal_global.118.64985
- ___block_literal_global.12.97034
- ___block_literal_global.122.53559
- ___block_literal_global.122.64987
- ___block_literal_global.123.90087
- ___block_literal_global.148.47126
- ___block_literal_global.158.54643
- ___block_literal_global.158.99306
- ___block_literal_global.161.99301
- ___block_literal_global.162.87024
- ___block_literal_global.163.54651
- ___block_literal_global.168.54659
- ___block_literal_global.178.54673
- ___block_literal_global.183.99286
- ___block_literal_global.190.90800
- ___block_literal_global.23.81231
- ___block_literal_global.25.65429
- ___block_literal_global.27.82146
- ___block_literal_global.3.83785
- ___block_literal_global.33.94160
- ___block_literal_global.340.63146
- ___block_literal_global.36.81144
- ___block_literal_global.36.99401
- ___block_literal_global.363.96550
- ___block_literal_global.37.56362
- ___block_literal_global.37.81220
- ___block_literal_global.38.54299
- ___block_literal_global.39.102384
- ___block_literal_global.39.78434
- ___block_literal_global.404.63130
- ___block_literal_global.46599
- ___block_literal_global.46992
- ___block_literal_global.47788
- ___block_literal_global.49201
- ___block_literal_global.49375
- ___block_literal_global.49492
- ___block_literal_global.49660
- ___block_literal_global.51.55841
- ___block_literal_global.51673
- ___block_literal_global.52623
- ___block_literal_global.53043
- ___block_literal_global.53701
- ___block_literal_global.53873
- ___block_literal_global.54036
- ___block_literal_global.54315
- ___block_literal_global.54635
- ___block_literal_global.55005
- ___block_literal_global.55139
- ___block_literal_global.55838
- ___block_literal_global.56102
- ___block_literal_global.56360
- ___block_literal_global.56720
- ___block_literal_global.57017
- ___block_literal_global.57200
- ___block_literal_global.57265
- ___block_literal_global.57887
- ___block_literal_global.58098
- ___block_literal_global.58588
- ___block_literal_global.60456
- ___block_literal_global.61570
- ___block_literal_global.61999
- ___block_literal_global.62.54296
- ___block_literal_global.62548
- ___block_literal_global.63059
- ___block_literal_global.63472
- ___block_literal_global.64.49582
- ___block_literal_global.64.58099
- ___block_literal_global.64077
- ___block_literal_global.64136
- ___block_literal_global.64156
- ___block_literal_global.65018
- ___block_literal_global.65430
- ___block_literal_global.65975
- ___block_literal_global.66171
- ___block_literal_global.66893
- ___block_literal_global.66966
- ___block_literal_global.67100
- ___block_literal_global.67458
- ___block_literal_global.68651
- ___block_literal_global.69.49346
- ___block_literal_global.69632
- ___block_literal_global.72.65013
- ___block_literal_global.72017
- ___block_literal_global.72584
- ___block_literal_global.73066
- ___block_literal_global.73230
- ___block_literal_global.73385
- ___block_literal_global.74706
- ___block_literal_global.74893
- ___block_literal_global.75163
- ___block_literal_global.75721
- ___block_literal_global.76.49349
- ___block_literal_global.76385
- ___block_literal_global.76543
- ___block_literal_global.77281
- ___block_literal_global.77557
- ___block_literal_global.77769
- ___block_literal_global.78473
- ___block_literal_global.79.100606
- ___block_literal_global.79.74850
- ___block_literal_global.79224
- ___block_literal_global.79298
- ___block_literal_global.79320
- ___block_literal_global.80.77265
- ___block_literal_global.81.49646
- ___block_literal_global.81147
- ___block_literal_global.81237
- ___block_literal_global.81935
- ___block_literal_global.82.98154
- ___block_literal_global.82000
- ___block_literal_global.82149
- ___block_literal_global.82728
- ___block_literal_global.83381
- ___block_literal_global.83793
- ___block_literal_global.83920
- ___block_literal_global.84145
- ___block_literal_global.85.49352
- ___block_literal_global.85780
- ___block_literal_global.87038
- ___block_literal_global.87501
- ___block_literal_global.88.49355
- ___block_literal_global.88410
- ___block_literal_global.89.53943
- ___block_literal_global.89.77756
- ___block_literal_global.89444
- ___block_literal_global.90089
- ___block_literal_global.90201
- ___block_literal_global.90802
- ___block_literal_global.91.53944
- ___block_literal_global.91.77751
- ___block_literal_global.91034
- ___block_literal_global.91760
- ___block_literal_global.92230
- ___block_literal_global.92324
- ___block_literal_global.92612
- ___block_literal_global.93.89445
- ___block_literal_global.93741
- ___block_literal_global.94056
- ___block_literal_global.94159
- ___block_literal_global.95437
- ___block_literal_global.95779
- ___block_literal_global.95843
- ___block_literal_global.95986
- ___block_literal_global.96145
- ___block_literal_global.96821
- ___block_literal_global.97.53021
- ___block_literal_global.97.89379
- ___block_literal_global.97045
- ___block_literal_global.98153
- ___block_literal_global.98518
- ___block_literal_global.99421
- ___block_literal_global.99673
- ___block_literal_global.99743
- ___getDMIsMigrationNeededSymbolLoc_block_invoke.73012
- ___getMBManagerClass_block_invoke.73044
- ___getPIPhotoEditHelperClass_block_invoke.60902
- ___getPIPhotoEditHelperClass_block_invoke.71926
- __downloadOriginalsChanged.53894
- __unnamed_array_storage.100780
- __unnamed_array_storage.101196
- __unnamed_array_storage.102428
- __unnamed_array_storage.102706
- __unnamed_array_storage.150.97801
- __unnamed_array_storage.159.102429
- __unnamed_array_storage.183
- __unnamed_array_storage.223
- __unnamed_array_storage.44.99878
- __unnamed_array_storage.46525
- __unnamed_array_storage.52332
- __unnamed_array_storage.52769
- __unnamed_array_storage.53289
- __unnamed_array_storage.54017
- __unnamed_array_storage.54319
- __unnamed_array_storage.55900
- __unnamed_array_storage.57164
- __unnamed_array_storage.60.84411
- __unnamed_array_storage.60962
- __unnamed_array_storage.61661
- __unnamed_array_storage.62.95459
- __unnamed_array_storage.63150
- __unnamed_array_storage.65.95458
- __unnamed_array_storage.65497
- __unnamed_array_storage.68497
- __unnamed_array_storage.69028
- __unnamed_array_storage.69376
- __unnamed_array_storage.71012
- __unnamed_array_storage.75148
- __unnamed_array_storage.81928
- __unnamed_array_storage.84438
- __unnamed_array_storage.84550
- __unnamed_array_storage.85784
- __unnamed_array_storage.86136
- __unnamed_array_storage.86578
- __unnamed_array_storage.87511
- __unnamed_array_storage.87797
- __unnamed_array_storage.88401
- __unnamed_array_storage.89061
- __unnamed_array_storage.89364
- __unnamed_array_storage.92142
- __unnamed_array_storage.95450
- __unnamed_array_storage.96881
- __unnamed_array_storage.97807
- __unnamed_array_storage.99280
- __unnamed_array_storage.99658
- __unnamed_array_storage.99877
- _audit_stringDataMigration.73002
- _audit_stringMobileBackup.73060
- _audit_stringNeutrinoCore.61013
- _audit_stringPhotoImaging.60856
- _audit_stringPhotoImaging.71939
- _baseSearchIndexPredicate.onceToken.96144
- _baseSearchIndexPredicate.predicate.96146
- _getDMIsMigrationNeededSymbolLoc.ptr.73011
- _getMBManagerClass.softClass.73043
- _getPIPhotoEditHelperClass.60900
- _getPIPhotoEditHelperClass.71924
- _getPIPhotoEditHelperClass.softClass.60901
- _getPIPhotoEditHelperClass.softClass.71925
- _indexArrayCopyDescription.57894
- _isEligibleForSearchIndexingPredicate.onceToken.66170
- _isEligibleForSearchIndexingPredicate.onceToken.90200
- _isEligibleForSearchIndexingPredicate.predicate.66172
- _isEligibleForSearchIndexingPredicate.predicate.90202
- _isSyncableChange.didSetupSyncedProperties.87363
- _isSyncableChange.syncedProperties.87364
- _listOfSyncedProperties.didSetupSyncedProperties.68512
- _listOfSyncedProperties.didSetupSyncedProperties.73441
- _listOfSyncedProperties.didSetupSyncedProperties.74595
- _listOfSyncedProperties.didSetupSyncedProperties.75080
- _listOfSyncedProperties.result.68513
- _listOfSyncedProperties.result.73442
- _listOfSyncedProperties.result.74596
- _listOfSyncedProperties.result.75081
- _listOfSyncedProperties.result.96221
- _modelProperties.modelProperties.50881
- _modelProperties.modelProperties.54728
- _modelProperties.modelProperties.61246
- _modelProperties.modelProperties.68195
- _modelProperties.modelProperties.70366
- _modelProperties.modelProperties.81439
- _modelProperties.modelProperties.83822
- _modelProperties.modelProperties.84480
- _modelProperties.modelProperties.86590
- _modelProperties.modelProperties.87099
- _modelProperties.onceToken.50880
- _modelProperties.onceToken.54727
- _modelProperties.onceToken.61245
- _modelProperties.onceToken.68194
- _modelProperties.onceToken.70365
- _modelProperties.onceToken.81438
- _modelProperties.onceToken.83821
- _modelProperties.onceToken.84479
- _modelProperties.onceToken.86589
- _modelProperties.onceToken.87098
- _persistedPropertyNamesForEntityNames.onceToken.50878
- _persistedPropertyNamesForEntityNames.onceToken.54725
- _persistedPropertyNamesForEntityNames.onceToken.61243
- _persistedPropertyNamesForEntityNames.onceToken.68192
- _persistedPropertyNamesForEntityNames.onceToken.70363
- _persistedPropertyNamesForEntityNames.onceToken.81436
- _persistedPropertyNamesForEntityNames.onceToken.83819
- _persistedPropertyNamesForEntityNames.onceToken.84477
- _persistedPropertyNamesForEntityNames.onceToken.86587
- _persistedPropertyNamesForEntityNames.onceToken.87096
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.50879
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.54726
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.61244
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.68193
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.70364
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.81437
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.83820
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.84478
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.86588
- _persistedPropertyNamesForEntityNames.persistedPropertyNamesForEntityNames.87097
- _s_lock.51346
- _sharedManager.onceToken.72016
- _sharedManager.onceToken.96387

```


</details>

## EOF
