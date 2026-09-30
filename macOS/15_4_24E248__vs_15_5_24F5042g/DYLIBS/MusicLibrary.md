## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Versions/A/MusicLibrary`

```diff

-4024.500.35.0.0
-  __TEXT.__text: 0x1f92c8
+4024.600.4.0.0
+  __TEXT.__text: 0x1f96e0
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0xdccc
+  __TEXT.__objc_methlist: 0xdcfc
   __TEXT.__const: 0x6342
   __TEXT.__dlopen_cstrs: 0xec
-  __TEXT.__gcc_except_tab: 0x132d0
-  __TEXT.__cstring: 0x65a58
-  __TEXT.__oslogstring: 0x18c79
+  __TEXT.__gcc_except_tab: 0x132d4
+  __TEXT.__cstring: 0x65a4b
+  __TEXT.__oslogstring: 0x18db3
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x6888
+  __TEXT.__unwind_info: 0x6898
   __TEXT.__objc_classname: 0x1929
-  __TEXT.__objc_methname: 0x1da78
-  __TEXT.__objc_methtype: 0x5248
-  __TEXT.__objc_stubs: 0x13b80
+  __TEXT.__objc_methname: 0x1db9b
+  __TEXT.__objc_methtype: 0x525c
+  __TEXT.__objc_stubs: 0x13bc0
   __DATA_CONST.__got: 0xa28
   __DATA_CONST.__const: 0x5670
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68a0
+  __DATA_CONST.__objc_selrefs: 0x68c0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0x10b8

   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xba90
   __AUTH_CONST.__cfstring: 0x21e60
-  __AUTH_CONST.__objc_const: 0x14e28
+  __AUTH_CONST.__objc_const: 0x14e68
   __AUTH_CONST.__objc_arrayobj: 0x20b8
   __AUTH_CONST.__objc_intobj: 0x1b30
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x44c0
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xe78
+  __DATA.__objc_ivar: 0xe80
   __DATA.__data: 0xac0
   __DATA.__bss: 0xda0
   __DATA.__common: 0x38

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7748
-  Symbols:   16613
-  CStrings:  11864
+  Functions: 7753
+  Symbols:   16622
+  CStrings:  11874
 
Symbols:
+ -[ML3DatabaseConnectionPool _closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:]
+ -[ML3SpotlightBatchDonationObject albumPersistentIDsToUpdate]
+ -[ML3SpotlightBatchDonationObject artistPersistentIDsToUpdate]
+ -[ML3SpotlightBatchDonationObject initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistPersistentIDsToUpdate:albumPersistentIDsToUpdate:artistPersistentIDsToUpdate:entityStringsToDelete:]
+ -[ML3SpotlightBatchDonationObject playlistPersistentIDsToUpdate]
+ -[_ML3DatabaseConnectionSubPool closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:]
+ -[_ML3DatabaseConnectionSubPool description]
+ GCC_except_table6634
+ GCC_except_table6639
+ GCC_except_table6657
+ GCC_except_table6673
+ GCC_except_table6674
+ GCC_except_table6680
+ GCC_except_table6686
+ GCC_except_table6687
+ GCC_except_table6723
+ GCC_except_table6724
+ GCC_except_table6730
+ GCC_except_table6731
+ GCC_except_table6738
+ GCC_except_table6739
+ GCC_except_table6749
+ GCC_except_table6750
+ GCC_except_table6757
+ GCC_except_table6758
+ GCC_except_table6777
+ GCC_except_table6778
+ GCC_except_table6783
+ GCC_except_table6784
+ GCC_except_table6792
+ GCC_except_table6795
+ GCC_except_table6799
+ GCC_except_table6802
+ GCC_except_table6823
+ GCC_except_table6845
+ GCC_except_table6867
+ GCC_except_table6876
+ GCC_except_table6883
+ GCC_except_table6907
+ GCC_except_table6931
+ GCC_except_table6932
+ GCC_except_table6996
+ GCC_except_table7024
+ GCC_except_table7146
+ GCC_except_table7232
+ GCC_except_table7302
+ GCC_except_table7308
+ GCC_except_table7314
+ GCC_except_table7315
+ GCC_except_table7316
+ GCC_except_table7331
+ GCC_except_table7335
+ GCC_except_table7381
+ GCC_except_table7387
+ GCC_except_table7391
+ GCC_except_table7694
+ GCC_except_table7695
+ GCC_except_table7696
+ GCC_except_table7702
+ GCC_except_table7704
+ GCC_except_table7705
+ GCC_except_table7708
+ MSVFastHexStringFromBytes.hexCharacters.25552
+ OBJC_IVAR_$_ML3SpotlightBatchDonationObject._albumPersistentIDsToUpdate
+ OBJC_IVAR_$_ML3SpotlightBatchDonationObject._artistPersistentIDsToUpdate
+ OBJC_IVAR_$_ML3SpotlightBatchDonationObject._playlistPersistentIDsToUpdate
+ _MSV_XXH_XXH32_update.25544
+ _MSV_XXH_XXH64_digest.25549
+ _MSV_XXH_XXH64_update.25545
+ __47-[ML3MusicLibrary _tearDownNotificationManager]_block_invoke.1075
+ __49-[_ML3DatabaseConnectionSubPool closeConnection:]_block_invoke.245
+ __58-[ML3MusicLibrary _closeAndLockCurrentDatabaseConnections]_block_invoke.1069
+ __95-[_ML3DatabaseConnectionSubPool closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:]_block_invoke.247
+ __Block_byref_object_copy_.10781
+ __Block_byref_object_copy_.10890
+ __Block_byref_object_copy_.11747
+ __Block_byref_object_copy_.11909
+ __Block_byref_object_copy_.12731
+ __Block_byref_object_copy_.13740
+ __Block_byref_object_copy_.16183
+ __Block_byref_object_copy_.16516
+ __Block_byref_object_copy_.17032
+ __Block_byref_object_copy_.17861
+ __Block_byref_object_copy_.18258
+ __Block_byref_object_copy_.18514
+ __Block_byref_object_copy_.19391
+ __Block_byref_object_copy_.19748
+ __Block_byref_object_copy_.20839
+ __Block_byref_object_copy_.21604
+ __Block_byref_object_copy_.23403
+ __Block_byref_object_copy_.23486
+ __Block_byref_object_copy_.23593
+ __Block_byref_object_copy_.23876
+ __Block_byref_object_copy_.24254
+ __Block_byref_object_copy_.2459
+ __Block_byref_object_copy_.25682
+ __Block_byref_object_copy_.26513
+ __Block_byref_object_copy_.3733
+ __Block_byref_object_copy_.4612
+ __Block_byref_object_copy_.4805
+ __Block_byref_object_copy_.5926
+ __Block_byref_object_copy_.7142
+ __Block_byref_object_copy_.7232
+ __Block_byref_object_copy_.7820
+ __Block_byref_object_copy_.8410
+ __Block_byref_object_copy_.8891
+ __Block_byref_object_copy_.9000
+ __Block_byref_object_copy_.9084
+ __Block_byref_object_copy_.9956
+ __Block_byref_object_dispose_.10782
+ __Block_byref_object_dispose_.10891
+ __Block_byref_object_dispose_.11748
+ __Block_byref_object_dispose_.11910
+ __Block_byref_object_dispose_.12732
+ __Block_byref_object_dispose_.13741
+ __Block_byref_object_dispose_.16184
+ __Block_byref_object_dispose_.16517
+ __Block_byref_object_dispose_.17033
+ __Block_byref_object_dispose_.17862
+ __Block_byref_object_dispose_.18259
+ __Block_byref_object_dispose_.18515
+ __Block_byref_object_dispose_.19392
+ __Block_byref_object_dispose_.19749
+ __Block_byref_object_dispose_.20840
+ __Block_byref_object_dispose_.21605
+ __Block_byref_object_dispose_.23404
+ __Block_byref_object_dispose_.23487
+ __Block_byref_object_dispose_.23594
+ __Block_byref_object_dispose_.23877
+ __Block_byref_object_dispose_.24255
+ __Block_byref_object_dispose_.2460
+ __Block_byref_object_dispose_.25683
+ __Block_byref_object_dispose_.26514
+ __Block_byref_object_dispose_.3734
+ __Block_byref_object_dispose_.4613
+ __Block_byref_object_dispose_.4806
+ __Block_byref_object_dispose_.5927
+ __Block_byref_object_dispose_.7143
+ __Block_byref_object_dispose_.7233
+ __Block_byref_object_dispose_.7821
+ __Block_byref_object_dispose_.8411
+ __Block_byref_object_dispose_.8892
+ __Block_byref_object_dispose_.9001
+ __Block_byref_object_dispose_.9085
+ __Block_byref_object_dispose_.9957
+ ___95-[_ML3DatabaseConnectionSubPool closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:]_block_invoke
+ ___block_descriptor_66_e8_32s40s48s56r_e5_v8?0l
+ __block_literal_global.10028
+ __block_literal_global.1071
+ __block_literal_global.10803
+ __block_literal_global.11231
+ __block_literal_global.12690
+ __block_literal_global.12878
+ __block_literal_global.13637
+ __block_literal_global.14502
+ __block_literal_global.15312
+ __block_literal_global.15632
+ __block_literal_global.16242
+ __block_literal_global.17325
+ __block_literal_global.18257
+ __block_literal_global.18533
+ __block_literal_global.18700
+ __block_literal_global.18824
+ __block_literal_global.18968
+ __block_literal_global.19508
+ __block_literal_global.20223
+ __block_literal_global.20328
+ __block_literal_global.20678
+ __block_literal_global.21373
+ __block_literal_global.23511
+ __block_literal_global.23646
+ __block_literal_global.24265
+ __block_literal_global.24585
+ __block_literal_global.2981
+ __block_literal_global.3906
+ __block_literal_global.4069
+ __block_literal_global.4611
+ __block_literal_global.4786
+ __block_literal_global.5399
+ __block_literal_global.5536
+ __block_literal_global.5909
+ __block_literal_global.6387
+ __block_literal_global.7119
+ __block_literal_global.8074
+ __block_literal_global.83.5596
+ __block_literal_global.8401
+ __block_literal_global.8647
+ __block_literal_global.8869
+ __block_literal_global.8988
+ __block_literal_global.9488
+ __block_literal_global.9975
+ __getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc_block_invoke.16825
+ __getICStoreArtworkInfoImageFormatJPEGSymbolLoc_block_invoke.16811
+ __getICStorePlatformMetadataKindPlaylistSymbolLoc_block_invoke.16837
+ __iTunesCloudLibraryCore_block_invoke.16820
+ _objc_msgSend$_closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:
+ _objc_msgSend$closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:
+ audit_stringiTunesCloud.16823
+ getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc.ptr.16824
+ getICStoreArtworkInfoImageFormatJPEGSymbolLoc.ptr.16810
+ getICStorePlatformMetadataKindPlaylistSymbolLoc.ptr.16836
+ iTunesCloudLibrary.16812
+ iTunesCloudLibraryCore.frameworkLibrary.16819
+ propertiesForGroupingKey.onceToken.5398
+ propertiesForGroupingKey.onceToken.7118
+ propertiesForGroupingKey.onceToken.8868
+ propertiesForGroupingKey.onceToken.8987
+ propertiesForGroupingKey.propertiesForGroupingKey.5400
+ propertiesForGroupingKey.propertiesForGroupingKey.7120
+ propertiesForGroupingKey.propertiesForGroupingKey.8870
+ propertiesForGroupingKey.propertiesForGroupingKey.8989
- -[ML3SpotlightBatchDonationObject initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistsPersistentIDsToUpdate:entityStringsToDelete:]
- -[ML3SpotlightBatchDonationObject playlistsPersistentIDsToUpdate]
- -[_ML3DatabaseConnectionSubPool debugDescription]
- GCC_except_table6632
- GCC_except_table6637
- GCC_except_table6653
- GCC_except_table6670
- GCC_except_table6671
- GCC_except_table6678
- GCC_except_table6683
- GCC_except_table6684
- GCC_except_table6721
- GCC_except_table6722
- GCC_except_table6728
- GCC_except_table6729
- GCC_except_table6732
- GCC_except_table6733
- GCC_except_table6743
- GCC_except_table6744
- GCC_except_table6754
- GCC_except_table6755
- GCC_except_table6767
- GCC_except_table6768
- GCC_except_table6781
- GCC_except_table6782
- GCC_except_table6788
- GCC_except_table6789
- GCC_except_table6797
- GCC_except_table6798
- GCC_except_table6821
- GCC_except_table6843
- GCC_except_table6865
- GCC_except_table6874
- GCC_except_table6881
- GCC_except_table6905
- GCC_except_table6928
- GCC_except_table6929
- GCC_except_table6993
- GCC_except_table7021
- GCC_except_table7141
- GCC_except_table7227
- GCC_except_table7297
- GCC_except_table7303
- GCC_except_table7309
- GCC_except_table7310
- GCC_except_table7311
- GCC_except_table7326
- GCC_except_table7330
- GCC_except_table7376
- GCC_except_table7382
- GCC_except_table7386
- GCC_except_table7689
- GCC_except_table7690
- GCC_except_table7691
- GCC_except_table7697
- GCC_except_table7699
- GCC_except_table7700
- GCC_except_table7703
- MSVFastHexStringFromBytes.hexCharacters.25562
- OBJC_IVAR_$_ML3SpotlightBatchDonationObject._playlistsPersistentIDsToUpdate
- _MSV_XXH_XXH32_update.25554
- _MSV_XXH_XXH64_digest.25559
- _MSV_XXH_XXH64_update.25555
- __47-[ML3MusicLibrary _tearDownNotificationManager]_block_invoke.1074
- __49-[_ML3DatabaseConnectionSubPool closeConnection:]_block_invoke.240
- __Block_byref_object_copy_.10805
- __Block_byref_object_copy_.10914
- __Block_byref_object_copy_.11771
- __Block_byref_object_copy_.11933
- __Block_byref_object_copy_.12755
- __Block_byref_object_copy_.13764
- __Block_byref_object_copy_.16207
- __Block_byref_object_copy_.16540
- __Block_byref_object_copy_.17056
- __Block_byref_object_copy_.17885
- __Block_byref_object_copy_.18282
- __Block_byref_object_copy_.18538
- __Block_byref_object_copy_.19415
- __Block_byref_object_copy_.19772
- __Block_byref_object_copy_.20863
- __Block_byref_object_copy_.21628
- __Block_byref_object_copy_.23423
- __Block_byref_object_copy_.23506
- __Block_byref_object_copy_.23613
- __Block_byref_object_copy_.23894
- __Block_byref_object_copy_.24260
- __Block_byref_object_copy_.2458
- __Block_byref_object_copy_.25692
- __Block_byref_object_copy_.26531
- __Block_byref_object_copy_.3757
- __Block_byref_object_copy_.4636
- __Block_byref_object_copy_.4829
- __Block_byref_object_copy_.5950
- __Block_byref_object_copy_.7166
- __Block_byref_object_copy_.7256
- __Block_byref_object_copy_.7844
- __Block_byref_object_copy_.8434
- __Block_byref_object_copy_.8915
- __Block_byref_object_copy_.9024
- __Block_byref_object_copy_.9108
- __Block_byref_object_copy_.9980
- __Block_byref_object_dispose_.10806
- __Block_byref_object_dispose_.10915
- __Block_byref_object_dispose_.11772
- __Block_byref_object_dispose_.11934
- __Block_byref_object_dispose_.12756
- __Block_byref_object_dispose_.13765
- __Block_byref_object_dispose_.16208
- __Block_byref_object_dispose_.16541
- __Block_byref_object_dispose_.17057
- __Block_byref_object_dispose_.17886
- __Block_byref_object_dispose_.18283
- __Block_byref_object_dispose_.18539
- __Block_byref_object_dispose_.19416
- __Block_byref_object_dispose_.19773
- __Block_byref_object_dispose_.20864
- __Block_byref_object_dispose_.21629
- __Block_byref_object_dispose_.23424
- __Block_byref_object_dispose_.23507
- __Block_byref_object_dispose_.23614
- __Block_byref_object_dispose_.23895
- __Block_byref_object_dispose_.24261
- __Block_byref_object_dispose_.2459
- __Block_byref_object_dispose_.25693
- __Block_byref_object_dispose_.26532
- __Block_byref_object_dispose_.3758
- __Block_byref_object_dispose_.4637
- __Block_byref_object_dispose_.4830
- __Block_byref_object_dispose_.5951
- __Block_byref_object_dispose_.7167
- __Block_byref_object_dispose_.7257
- __Block_byref_object_dispose_.7845
- __Block_byref_object_dispose_.8435
- __Block_byref_object_dispose_.8916
- __Block_byref_object_dispose_.9025
- __Block_byref_object_dispose_.9109
- __Block_byref_object_dispose_.9981
- ___58-[ML3MusicLibrary _closeAndLockCurrentDatabaseConnections]_block_invoke_2
- ___75-[_ML3DatabaseConnectionSubPool closeConnectionsAndWaitForBusyConnections:]_block_invoke
- ___block_descriptor_57_e8_32s40s48r_e5_v8?0l
- __block_literal_global.10052
- __block_literal_global.1070
- __block_literal_global.10827
- __block_literal_global.11255
- __block_literal_global.12714
- __block_literal_global.12902
- __block_literal_global.13661
- __block_literal_global.14526
- __block_literal_global.15336
- __block_literal_global.15656
- __block_literal_global.16266
- __block_literal_global.17349
- __block_literal_global.18281
- __block_literal_global.18557
- __block_literal_global.18724
- __block_literal_global.18848
- __block_literal_global.18992
- __block_literal_global.19532
- __block_literal_global.20247
- __block_literal_global.20352
- __block_literal_global.20702
- __block_literal_global.21397
- __block_literal_global.23531
- __block_literal_global.23666
- __block_literal_global.24271
- __block_literal_global.24595
- __block_literal_global.3006
- __block_literal_global.3930
- __block_literal_global.4093
- __block_literal_global.4635
- __block_literal_global.4810
- __block_literal_global.5423
- __block_literal_global.5560
- __block_literal_global.5933
- __block_literal_global.6411
- __block_literal_global.7143
- __block_literal_global.8098
- __block_literal_global.83.5620
- __block_literal_global.8425
- __block_literal_global.8671
- __block_literal_global.8893
- __block_literal_global.9012
- __block_literal_global.9512
- __block_literal_global.9999
- __getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc_block_invoke.16849
- __getICStoreArtworkInfoImageFormatJPEGSymbolLoc_block_invoke.16835
- __getICStorePlatformMetadataKindPlaylistSymbolLoc_block_invoke.16861
- __iTunesCloudLibraryCore_block_invoke.16844
- audit_stringiTunesCloud.16847
- getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc.ptr.16848
- getICStoreArtworkInfoImageFormatJPEGSymbolLoc.ptr.16834
- getICStorePlatformMetadataKindPlaylistSymbolLoc.ptr.16860
- iTunesCloudLibrary.16836
- iTunesCloudLibraryCore.frameworkLibrary.16843
- propertiesForGroupingKey.onceToken.5422
- propertiesForGroupingKey.onceToken.7142
- propertiesForGroupingKey.onceToken.8892
- propertiesForGroupingKey.onceToken.9011
- propertiesForGroupingKey.propertiesForGroupingKey.5424
- propertiesForGroupingKey.propertiesForGroupingKey.7144
- propertiesForGroupingKey.propertiesForGroupingKey.8894
- propertiesForGroupingKey.propertiesForGroupingKey.9013
CStrings:
+ "%p dealloc"
+ "%{public}@ - Creating new connection pool=%{public}@ with path: %{public}@"
+ "%{public}@ - _closeAndLockCurrentDatabaseConnections, _connectionPoolsPendingClose.count=%d, connectionPool=%{public}@ "
+ "%{public}@ - not removing connection pool=%{public}@ as it has active connections"
+ "%{public}@ - removing connection pool=%{public}@"
+ "%{public}@ Closing all connections and wait for busy connection=%{BOOL}u, owningPoolClosed=%{BOOL}u"
+ "%{public}@ checking in available connection=%{public}@"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/MusicLibrary/MusicLibrary/Sorting/iPhoneSortKey/iPhoneSortKey.c"
+ "@72@0:8q16q24@32@40@48@56@64"
+ "AvailableConnectionCount"
+ "AvailableConnectionDesc"
+ "BusyConnectionDesc"
+ "DatabaseConnectionPoolDesc"
+ "ML3DatabaseConnectionPool=%p, maxReaders=%d, maxWriters=%d, journalingMode=%d, closed=%d, useDistantWriterConnections=%d, closed=%d"
+ "ML3DatabaseConnectionSubPool=%p closeConnectionsAndWaitForBusyConnections owningPoolClosed=%{BOOL}u, waitForBusyConnections=%{BOOL}u,_availableConnections(count)=%{public}@, _busyConnections=%{public}@"
+ "ML3DatabaseConnectionSubPool=%p, maxConcurrentConnections=%lu, useReadOnlyConnections=%d, useDistantConnections=%d, busyConnections=%p, availableConnections=%p"
+ "_albumPersistentIDsToUpdate"
+ "_artistPersistentIDsToUpdate"
+ "_closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:"
+ "_playlistPersistentIDsToUpdate"
+ "albumPersistentIDsToUpdate"
+ "artistPersistentIDsToUpdate"
+ "closeConnectionsForOwningPoolClosed:andWaitForBusyConnections:"
+ "initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistPersistentIDsToUpdate:albumPersistentIDsToUpdate:artistPersistentIDsToUpdate:entityStringsToDelete:"
+ "playlistPersistentIDsToUpdate"
+ "v24@0:8B16B20"
- "%{public}@ - Creating connection pool with path: %{public}@"
- "%{public}@ - _closeAndLockCurrentDatabaseConnections"
- "%{public}@ - connection pool %{public}@ has pending or active connections"
- "%{public}@ Closing all connections and wait for busy connection=%{BOOL}u."
- "%{public}@ closeConnectionsAndWaitForBusyConnections _availableConnections (count) = %d, _busyConnections (count) = %d"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MusicLibrary/MusicLibrary/Sorting/iPhoneSortKey/iPhoneSortKey.c"
- "@56@0:8q16q24@32@40@48"
- "Attempted to return connection %@ not owned by connection pool %@. (Connections in this pool: %@)"
- "DatabaseConnectionPool"
- "ML3DatabaseConnectionPool=%p, maxReaders=%d, maxWriters=%d, journalingMode=%d, useDistantWriterConnections=%d, closed=%d"
- "ML3DatabaseConnectionSubPool=%p, maxConcurrentConnections=%lu, useReadOnlyConnections=%d, useDistantConnections=%d"
- "_playlistsPersistentIDsToUpdate"
- "availableConnections=%@"
- "busyConnections=%@"
- "initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistsPersistentIDsToUpdate:entityStringsToDelete:"
- "playlistsPersistentIDsToUpdate"

```
