## NanoTimeKit

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit`

```diff

-2398.53.19.0.0
-  __TEXT.__text: 0x2a3b38
-  __TEXT.__auth_stubs: 0x2ce0
-  __TEXT.__objc_methlist: 0x29cd4
-  __TEXT.__const: 0x27e4
-  __TEXT.__cstring: 0x1adbb
-  __TEXT.__gcc_except_tab: 0x51e0
-  __TEXT.__oslogstring: 0x135f8
+2398.92.0.0.0
+  __TEXT.__text: 0x2a4e94
+  __TEXT.__auth_stubs: 0x2cd0
+  __TEXT.__objc_methlist: 0x29ecc
+  __TEXT.__const: 0x2804
+  __TEXT.__cstring: 0x1affb
+  __TEXT.__gcc_except_tab: 0x51f4
+  __TEXT.__oslogstring: 0x13619
   __TEXT.__dlopen_cstrs: 0x26b
   __TEXT.__ustring: 0x464
   __TEXT.__constg_swiftt: 0x7c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0xbc54
+  __TEXT.__unwind_info: 0xbce0
   __TEXT.__eh_frame: 0x208
-  __TEXT.__objc_classname: 0x7de3
-  __TEXT.__objc_methname: 0x5bc27
-  __TEXT.__objc_methtype: 0xc014
-  __TEXT.__objc_stubs: 0x3dae0
+  __TEXT.__objc_classname: 0x7e8b
+  __TEXT.__objc_methname: 0x5bd29
+  __TEXT.__objc_methtype: 0xc041
+  __TEXT.__objc_stubs: 0x3db60
   __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0xb0b8
-  __DATA_CONST.__objc_classlist: 0x1a08
+  __DATA_CONST.__const: 0xb0b0
+  __DATA_CONST.__objc_classlist: 0x1a30
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x598
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6b6c0
-  __DATA_CONST.__objc_selrefs: 0x13598
+  __DATA_CONST.__objc_const: 0x6b840
+  __DATA_CONST.__objc_selrefs: 0x135b8
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_classrefs: 0x23d8
+  __DATA_CONST.__objc_superrefs: 0x14a0
   __DATA_CONST.__objc_arraydata: 0x29a0
-  __AUTH_CONST.__objc_intobj: 0x4d70
+  __AUTH_CONST.__objc_intobj: 0x4db8
   __AUTH_CONST.__objc_doubleobj: 0x30a0
-  __AUTH_CONST.__cfstring: 0x1f480
-  __AUTH_CONST.__objc_const: 0x16a58
-  __AUTH_CONST.__const: 0x39b8
+  __AUTH_CONST.__cfstring: 0x1f680
+  __AUTH_CONST.__objc_const: 0x16ce0
+  __AUTH_CONST.__const: 0x39d8
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x2148
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1688
-  __AUTH.__objc_data: 0xe260
+  __AUTH_CONST.__auth_got: 0x1680
+  __AUTH.__objc_data: 0xe3a0
   __AUTH.__data: 0xc0
-  __DATA.__objc_protorefs: 0xb0
-  __DATA.__objc_classrefs: 0x23b8
-  __DATA.__objc_superrefs: 0x1490
-  __DATA.__objc_ivar: 0x3710
+  __DATA.__objc_ivar: 0x3728
   __DATA.__data: 0x45c8
-  __DATA.__bss: 0x4b78
+  __DATA.__bss: 0x4ba8
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x21c0
+  __DATA_DIRTY.__objc_data: 0x2210
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x780
   __FONT_DATA.__VictoryFont1: 0x13d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EDDBDF97-B57C-3C73-AD1C-AFD3DD16EEDA
-  Functions: 17455
-  Symbols:   60733
-  CStrings:  26882
+  UUID: 711ECB5D-46D1-334E-96D4-18A698014555
+  Functions: 17499
+  Symbols:   60872
+  CStrings:  26942
 
Symbols:
+ +[NTKLuxViewerComplicationDataSource acceptsComplicationFamily:forDevice:]
+ +[NTKLuxViewerComplicationDataSource acceptsComplicationType:forDevice:]
+ +[NTKLuxViewerComplicationEntryModel modelWithLux:]
+ +[NTKLuxViewerComplicationEntryModel tritiumModel]
+ +[NTKNitsViewerComplicationDataSource acceptsComplicationFamily:forDevice:]
+ +[NTKNitsViewerComplicationDataSource acceptsComplicationType:forDevice:]
+ +[NTKNitsViewerComplicationEntryModel modelWithNits:]
+ +[NTKNitsViewerComplicationEntryModel tritiumModel]
+ -[NTKBundleComplicationMigrationServiceClient _queue_resetConnection:]
+ -[NTKComplicationProvider initWithDevice:]
+ -[NTKGroupedBezelProperties .cxx_destruct]
+ -[NTKGroupedBezelProperties bezelTextColor]
+ -[NTKGroupedBezelProperties bezelTextRadius]
+ -[NTKGroupedBezelProperties setBezelTextColor:]
+ -[NTKGroupedBezelProperties setBezelTextRadius:]
+ -[NTKLuxViewerComplicationDataSource .cxx_destruct]
+ -[NTKLuxViewerComplicationDataSource _currentTimelineEntry]
+ -[NTKLuxViewerComplicationDataSource alwaysOnTemplate]
+ -[NTKLuxViewerComplicationDataSource currentSwitcherTemplate]
+ -[NTKLuxViewerComplicationDataSource dealloc]
+ -[NTKLuxViewerComplicationDataSource getCurrentTimelineEntryWithHandler:]
+ -[NTKLuxViewerComplicationDataSource initWithComplication:family:forDevice:]
+ -[NTKLuxViewerComplicationDataSource pause]
+ -[NTKLuxViewerComplicationDataSource resume]
+ -[NTKLuxViewerComplicationEntryModel entryForComplicationFamily:]
+ -[NTKNitsViewerComplicationDataSource .cxx_destruct]
+ -[NTKNitsViewerComplicationDataSource _currentTimelineEntry]
+ -[NTKNitsViewerComplicationDataSource alwaysOnTemplate]
+ -[NTKNitsViewerComplicationDataSource currentSwitcherTemplate]
+ -[NTKNitsViewerComplicationDataSource dealloc]
+ -[NTKNitsViewerComplicationDataSource getCurrentTimelineEntryWithHandler:]
+ -[NTKNitsViewerComplicationDataSource initWithComplication:family:forDevice:]
+ -[NTKNitsViewerComplicationDataSource pause]
+ -[NTKNitsViewerComplicationDataSource resume]
+ -[NTKNitsViewerComplicationEntryModel entryForComplicationFamily:]
+ GCC_except_table127
+ GCC_except_table137
+ _NTKHasRegionalGeoRestrictions
+ _NTKHasRegionalGeoRestrictions.geoRestricted
+ _NTKHasRegionalGeoRestrictions.onceToken
+ _OBJC_CLASS_$_NTKGroupedBezelProperties
+ _OBJC_CLASS_$_NTKLuxViewerComplicationDataSource
+ _OBJC_CLASS_$_NTKLuxViewerComplicationEntryModel
+ _OBJC_CLASS_$_NTKNitsViewerComplicationDataSource
+ _OBJC_CLASS_$_NTKNitsViewerComplicationEntryModel
+ _OBJC_IVAR_$_NTKGroupedBezelProperties._bezelTextColor
+ _OBJC_IVAR_$_NTKGroupedBezelProperties._bezelTextRadius
+ _OBJC_IVAR_$_NTKLuxViewerComplicationDataSource._updateTimer
+ _OBJC_IVAR_$_NTKLuxViewerComplicationEntryModel._luxValue
+ _OBJC_IVAR_$_NTKNitsViewerComplicationDataSource._updateTimer
+ _OBJC_IVAR_$_NTKNitsViewerComplicationEntryModel._nitsValue
+ _OBJC_METACLASS_$_NTKGroupedBezelProperties
+ _OBJC_METACLASS_$_NTKLuxViewerComplicationDataSource
+ _OBJC_METACLASS_$_NTKLuxViewerComplicationEntryModel
+ _OBJC_METACLASS_$_NTKNitsViewerComplicationDataSource
+ _OBJC_METACLASS_$_NTKNitsViewerComplicationEntryModel
+ __OBJC_$_CLASS_METHODS_NTKLuxViewerComplicationDataSource
+ __OBJC_$_CLASS_METHODS_NTKLuxViewerComplicationEntryModel
+ __OBJC_$_CLASS_METHODS_NTKNitsViewerComplicationDataSource
+ __OBJC_$_CLASS_METHODS_NTKNitsViewerComplicationEntryModel
+ __OBJC_$_INSTANCE_METHODS_NTKGroupedBezelProperties
+ __OBJC_$_INSTANCE_METHODS_NTKLuxViewerComplicationDataSource
+ __OBJC_$_INSTANCE_METHODS_NTKLuxViewerComplicationEntryModel
+ __OBJC_$_INSTANCE_METHODS_NTKNitsViewerComplicationDataSource
+ __OBJC_$_INSTANCE_METHODS_NTKNitsViewerComplicationEntryModel
+ __OBJC_$_INSTANCE_VARIABLES_NTKGroupedBezelProperties
+ __OBJC_$_INSTANCE_VARIABLES_NTKLuxViewerComplicationDataSource
+ __OBJC_$_INSTANCE_VARIABLES_NTKLuxViewerComplicationEntryModel
+ __OBJC_$_INSTANCE_VARIABLES_NTKNitsViewerComplicationDataSource
+ __OBJC_$_INSTANCE_VARIABLES_NTKNitsViewerComplicationEntryModel
+ __OBJC_$_PROP_LIST_NTKBlackcombColorPalette.121
+ __OBJC_$_PROP_LIST_NTKCaliforniaColorPalette.132
+ __OBJC_$_PROP_LIST_NTKFaceColorPalette.260
+ __OBJC_$_PROP_LIST_NTKGossamerColorPalette.254
+ __OBJC_$_PROP_LIST_NTKGroupedBezelProperties
+ __OBJC_$_PROP_LIST_NTKOlympusColorPalette.158
+ __OBJC_$_PROP_LIST_NTKRichComplicationBezelView.137
+ __OBJC_$_PROP_LIST_NTKUtilityComplicationView.425
+ __OBJC_$_PROP_LIST_NTKUtilityFlatComplicationView.512
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NTKRichComplicationBezelView
+ __OBJC_CLASS_RO_$_NTKGroupedBezelProperties
+ __OBJC_CLASS_RO_$_NTKLuxViewerComplicationDataSource
+ __OBJC_CLASS_RO_$_NTKLuxViewerComplicationEntryModel
+ __OBJC_CLASS_RO_$_NTKNitsViewerComplicationDataSource
+ __OBJC_CLASS_RO_$_NTKNitsViewerComplicationEntryModel
+ __OBJC_METACLASS_RO_$_NTKGroupedBezelProperties
+ __OBJC_METACLASS_RO_$_NTKLuxViewerComplicationDataSource
+ __OBJC_METACLASS_RO_$_NTKLuxViewerComplicationEntryModel
+ __OBJC_METACLASS_RO_$_NTKNitsViewerComplicationDataSource
+ __OBJC_METACLASS_RO_$_NTKNitsViewerComplicationEntryModel
+ ___119-[NTKPersistentFaceCollection loadFullCollectionWithOrderedUUIDs:selectedUUID:facesDescriptorsByUUID:seqId:completion:]_block_invoke.94
+ ___119-[NTKPersistentFaceCollection loadFullCollectionWithOrderedUUIDs:selectedUUID:facesDescriptorsByUUID:seqId:completion:]_block_invoke.98
+ ___121-[NTKDArgonService _push_sendNotificationForContent:requestIdentifier:toNotificationCenter:identifier:bundle:completion:]_block_invoke.272
+ ___121-[NTKDArgonService _push_sendNotificationForContent:requestIdentifier:toNotificationCenter:identifier:bundle:completion:]_block_invoke.272.cold.1
+ ___25-[NTKDArgonService _init]_block_invoke.155
+ ___25-[NTKDArgonService _init]_block_invoke.161
+ ___25-[NTKDArgonService _init]_block_invoke.161.cold.1
+ ___25-[NTKDArgonService _init]_block_invoke.164
+ ___25-[NTKDArgonService _init]_block_invoke.167
+ ___25-[NTKDArgonService _init]_block_invoke.167.cold.1
+ ___25-[NTKDArgonService start]_block_invoke.172
+ ___33-[NTKCGalleryCell setCollection:]_block_invoke.88
+ ___33-[NTKCGalleryCell setCollection:]_block_invoke_2.90
+ ___44-[NTKSystemAppStateCache prewarmGizmoDaemon]_block_invoke.266
+ ___45+[NTKComplicationProvider providerForDevice:]_block_invoke
+ ___47-[NTKGreenfieldAddWatchFaceManager _decodeUrl:]_block_invoke.270
+ ___57-[NTKDArgonService connection:didReceiveIncomingMessage:]_block_invoke.215
+ ___57-[NTKDArgonService connection:didReceiveIncomingMessage:]_block_invoke.215.cold.1
+ ___57-[NTKFace _applyConfiguration:allowFailure:forMigration:]_block_invoke.233
+ ___58-[NTKCPhotoFaceCollectionGalleryCollection initForDevice:]_block_invoke.171
+ ___61-[NTKCWhistlerSubdialsFacesGalleryCollection facesForDevice:]_block_invoke.126
+ ___62-[NTKDArgonService ingestKeyDescriptor:withMethod:completion:]_block_invoke.186
+ ___62-[NTKDArgonService ingestKeyDescriptor:withMethod:completion:]_block_invoke.186.cold.1
+ ___62-[NTKPhotosFaceView _updateDateAttributesAnimated:completion:]_block_invoke_3
+ ___71-[NTKBundleComplicationMigrationServiceClient _setupConnectionIfNeeded]_block_invoke_2
+ ___71-[NTKBundleComplicationMigrationServiceClient _setupConnectionIfNeeded]_block_invoke_2.13
+ ___76-[NTKDArgonService _queue_push_userNotification_processWaitingNotifications]_block_invoke.227
+ ___76-[NTKDArgonService _queue_push_userNotification_processWaitingNotifications]_block_invoke.227.cold.1
+ ___76-[NTKDArgonService _queue_push_userNotification_processWaitingNotifications]_block_invoke.237.cold.1
+ ___76-[NTKDArgonService _queue_push_userNotification_processWaitingNotifications]_block_invoke.238
+ ___77-[NTKBundleComplicationMigrationServiceClient _queue_updateInvalidationTimer]_block_invoke.30
+ ___80+[NTKSampleComplicationDataSource acceptsComplicationType:withFamily:forDevice:]_block_invoke.330
+ ___81-[NTKBundleComplicationMigrationServiceClient _queue_serviceRequest:retryBudget:]_block_invoke.23.cold.1
+ ___81-[NTKBundleComplicationMigrationServiceClient _queue_serviceRequest:retryBudget:]_block_invoke.24
+ ___81-[NTKTimelineRemoteDataSourceProvider getCurrentEntryForComplication:completion:]_block_invoke.69
+ ___84-[NTKGreenfieldAddWatchFaceManager _refreshInstalledComplicationsWithContinueBlock:]_block_invoke.341
+ ___84-[NTKGreenfieldAddWatchFaceManager _refreshInstalledComplicationsWithContinueBlock:]_block_invoke.343
+ ___84-[NTKGreenfieldAddWatchFaceManager _refreshInstalledComplicationsWithContinueBlock:]_block_invoke.344
+ ___92-[NTKTimelineRemoteDataSourceProvider getEntriesForComplication:afterDate:limit:completion:]_block_invoke.73
+ ___NTKAskFaceSupportServerForCurrentEnvironment_block_invoke.116
+ ___NTKAskFaceSupportServerForKnownKeyDescriptors_block_invoke.113
+ ___NTKAskFaceSupportServerToAddKeyDescriptor_block_invoke.106.cold.1
+ ___NTKAskFaceSupportServerToAddKeyDescriptor_block_invoke.107
+ ___NTKAskFaceSupportServerToChangeCurrentEnvironment_block_invoke.118
+ ___NTKAskFaceSupportServerToDisplayUserNotificationForKeyDescriptor_block_invoke.115
+ ___NTKAskFaceSupportServerToResetOnNextLaunch_block_invoke.112
+ ___NTKCanAddWatchFace_block_invoke.509
+ ___NTKHasRegionalGeoRestrictions_block_invoke
+ ___NTKHighPriorityApply_block_invoke.379
+ ___NTKPhotosConfirmMemoryWasViewed_block_invoke.332
+ ___NTKQueryFaceSupportServerForNewFaces_block_invoke.95
+ ___NTKQueryFaceSupportServerForNewFaces_block_invoke.95.cold.1
+ ___NTKQueryFaceSupportServerForNewFaces_block_invoke.99
+ ___block_descriptor_48_e8_32bs40w_e53_v24?0"CLKWidgetComplicationDescriptor"8"NSError"16lw40l8s32l8
+ ___block_descriptor_64_e8_32s40r48w_e17_v16?0"NSError"8lw48l8r40l8s32l8
+ ___block_literal_global.1116
+ ___block_literal_global.1288
+ ___block_literal_global.1317
+ ___block_literal_global.1366
+ ___block_literal_global.1399
+ ___block_literal_global.1405
+ ___block_literal_global.151
+ ___block_literal_global.1529
+ ___block_literal_global.1531
+ ___block_literal_global.1575
+ ___block_literal_global.158
+ ___block_literal_global.1624
+ ___block_literal_global.1626
+ ___block_literal_global.1629
+ ___block_literal_global.1631
+ ___block_literal_global.1641
+ ___block_literal_global.1645
+ ___block_literal_global.1656
+ ___block_literal_global.1660
+ ___block_literal_global.1664
+ ___block_literal_global.1669
+ ___block_literal_global.1674
+ ___block_literal_global.1681
+ ___block_literal_global.1683
+ ___block_literal_global.1690
+ ___block_literal_global.1694
+ ___block_literal_global.1704
+ ___block_literal_global.1707
+ ___block_literal_global.1709
+ ___block_literal_global.1711
+ ___block_literal_global.1728
+ ___block_literal_global.174
+ ___block_literal_global.1745
+ ___block_literal_global.1751
+ ___block_literal_global.177
+ ___block_literal_global.1873
+ ___block_literal_global.1916
+ ___block_literal_global.212
+ ___block_literal_global.269
+ ___block_literal_global.280
+ ___block_literal_global.285
+ ___block_literal_global.287
+ ___block_literal_global.292
+ ___block_literal_global.294
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.306
+ ___block_literal_global.332
+ ___block_literal_global.337
+ ___block_literal_global.340
+ ___block_literal_global.354
+ ___block_literal_global.358
+ ___block_literal_global.363
+ ___block_literal_global.377
+ ___block_literal_global.383
+ ___block_literal_global.394
+ ___block_literal_global.408
+ ___block_literal_global.416
+ ___block_literal_global.418
+ ___block_literal_global.434
+ ___block_literal_global.474
+ ___block_literal_global.482
+ ___block_literal_global.493
+ ___block_literal_global.498
+ ___block_literal_global.545
+ ___block_literal_global.552
+ ___block_literal_global.599
+ ___block_literal_global.621
+ ___block_literal_global.624
+ ___block_literal_global.70
+ ___block_literal_global.709
+ ___block_literal_global.752
+ ___block_literal_global.769
+ ___block_literal_global.772
+ ___block_literal_global.774
+ ___block_literal_global.776
+ ___block_literal_global.779
+ ___block_literal_global.782
+ ___block_literal_global.785
+ ___block_literal_global.788
+ ___block_literal_global.79
+ ___block_literal_global.791
+ ___block_literal_global.794
+ ___block_literal_global.81
+ ___block_literal_global.898
+ ___block_literal_global.932
+ ___block_literal_global.960
+ ___block_literal_global.98
+ __imageScaleForTemplate:.__cachedDevice.352
+ __imageScaleForTemplate:.__lock.351
+ __imageScaleForTemplate:.__previousCLKDeviceVersion.353
+ __imageScaleForTemplate:._scale.350
+ __orderedValuesForDevice:.__cachedDevice.1231
+ __orderedValuesForDevice:.__cachedDevice.1260
+ __orderedValuesForDevice:.__cachedDevice.1298
+ __orderedValuesForDevice:.__cachedDevice.1329
+ __orderedValuesForDevice:.__cachedDevice.1415
+ __orderedValuesForDevice:.__cachedDevice.1444
+ __orderedValuesForDevice:.__cachedDevice.1581
+ __orderedValuesForDevice:.__cachedDevice.1657
+ __orderedValuesForDevice:.__cachedDevice.1666
+ __orderedValuesForDevice:.__cachedDevice.1708
+ __orderedValuesForDevice:.__cachedDevice.1738
+ __orderedValuesForDevice:.__cachedDevice.1758
+ __orderedValuesForDevice:.__cachedDevice.1857
+ __orderedValuesForDevice:.__cachedDevice.824
+ __orderedValuesForDevice:.__cachedDevice.833
+ __orderedValuesForDevice:.__cachedDevice.842
+ __orderedValuesForDevice:.__cachedDevice.867
+ __orderedValuesForDevice:.__cachedDevice.907
+ __orderedValuesForDevice:.__cachedDevice.941
+ __orderedValuesForDevice:.__cachedDevice.970
+ __orderedValuesForDevice:.__colors.1229
+ __orderedValuesForDevice:.__colors.1442
+ __orderedValuesForDevice:.__colors.1655
+ __orderedValuesForDevice:.__colors.1756
+ __orderedValuesForDevice:.__colors.1855
+ __orderedValuesForDevice:.__colors.822
+ __orderedValuesForDevice:.__colors.831
+ __orderedValuesForDevice:.__colors.840
+ __orderedValuesForDevice:.__colors.968
+ __orderedValuesForDevice:.__lock.1230
+ __orderedValuesForDevice:.__lock.1259
+ __orderedValuesForDevice:.__lock.1297
+ __orderedValuesForDevice:.__lock.1328
+ __orderedValuesForDevice:.__lock.1414
+ __orderedValuesForDevice:.__lock.1443
+ __orderedValuesForDevice:.__lock.1580
+ __orderedValuesForDevice:.__lock.1656
+ __orderedValuesForDevice:.__lock.1665
+ __orderedValuesForDevice:.__lock.1707
+ __orderedValuesForDevice:.__lock.1737
+ __orderedValuesForDevice:.__lock.1757
+ __orderedValuesForDevice:.__lock.1856
+ __orderedValuesForDevice:.__lock.823
+ __orderedValuesForDevice:.__lock.832
+ __orderedValuesForDevice:.__lock.841
+ __orderedValuesForDevice:.__lock.866
+ __orderedValuesForDevice:.__lock.906
+ __orderedValuesForDevice:.__lock.940
+ __orderedValuesForDevice:.__lock.969
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1232
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1261
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1299
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1330
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1416
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1445
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1582
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1658
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1667
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1709
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1739
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1759
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.1858
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.825
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.834
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.843
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.868
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.908
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.942
+ __orderedValuesForDevice:.__previousCLKDeviceVersion.971
+ __orderedValuesForDevice:.__styles.1258
+ __orderedValuesForDevice:.__styles.1296
+ __orderedValuesForDevice:.__styles.1327
+ __orderedValuesForDevice:.__styles.1413
+ __orderedValuesForDevice:.__styles.1664
+ __orderedValuesForDevice:.__styles.1736
+ __orderedValuesRestrictedByDevice:.__cachedDevice.1703
+ __orderedValuesRestrictedByDevice:.__cachedDevice.1771
+ __orderedValuesRestrictedByDevice:.__lock.1702
+ __orderedValuesRestrictedByDevice:.__lock.1770
+ __orderedValuesRestrictedByDevice:.__previousCLKDeviceVersion.1704
+ __orderedValuesRestrictedByDevice:.__previousCLKDeviceVersion.1772
+ __orderedValuesRestrictedByDevice:.hardwareSpecificValues.1701
+ __orderedValuesRestrictedByDevice:.hardwareSpecificValues.1769
+ __unnamed_array_storage.1000
+ __unnamed_array_storage.1003
+ __unnamed_array_storage.1006
+ __unnamed_array_storage.1009
+ __unnamed_array_storage.102
+ __unnamed_array_storage.115
+ __unnamed_array_storage.118
+ __unnamed_array_storage.121
+ __unnamed_array_storage.1234
+ __unnamed_array_storage.125
+ __unnamed_array_storage.1265
+ __unnamed_array_storage.1334
+ __unnamed_array_storage.1376
+ __unnamed_array_storage.1382
+ __unnamed_array_storage.1385
+ __unnamed_array_storage.1388
+ __unnamed_array_storage.1391
+ __unnamed_array_storage.1418
+ __unnamed_array_storage.1586
+ __unnamed_array_storage.1589
+ __unnamed_array_storage.1637
+ __unnamed_array_storage.1642
+ __unnamed_array_storage.1647
+ __unnamed_array_storage.1666
+ __unnamed_array_storage.1671
+ __unnamed_array_storage.1678
+ __unnamed_array_storage.1687
+ __unnamed_array_storage.1711
+ __unnamed_array_storage.1751
+ __unnamed_array_storage.1764
+ __unnamed_array_storage.1767
+ __unnamed_array_storage.1862
+ __unnamed_array_storage.225
+ __unnamed_array_storage.280
+ __unnamed_array_storage.302
+ __unnamed_array_storage.322
+ __unnamed_array_storage.336
+ __unnamed_array_storage.342
+ __unnamed_array_storage.361
+ __unnamed_array_storage.436
+ __unnamed_array_storage.476
+ __unnamed_array_storage.558
+ __unnamed_array_storage.82
+ __unnamed_array_storage.83
+ __unnamed_array_storage.845
+ __unnamed_array_storage.973
+ __unnamed_array_storage.982
+ __unnamed_array_storage.985
+ __unnamed_array_storage.991
+ __unnamed_array_storage.997
+ __valueToFaceBundleStringDict.onceToken.1114
+ __valueToFaceBundleStringDict.onceToken.1239
+ __valueToFaceBundleStringDict.onceToken.1286
+ __valueToFaceBundleStringDict.onceToken.1315
+ __valueToFaceBundleStringDict.onceToken.1364
+ __valueToFaceBundleStringDict.onceToken.1403
+ __valueToFaceBundleStringDict.onceToken.1436
+ __valueToFaceBundleStringDict.onceToken.1552
+ __valueToFaceBundleStringDict.onceToken.1622
+ __valueToFaceBundleStringDict.onceToken.1692
+ __valueToFaceBundleStringDict.onceToken.1726
+ __valueToFaceBundleStringDict.onceToken.1749
+ __valueToFaceBundleStringDict.onceToken.1814
+ __valueToFaceBundleStringDict.onceToken.1871
+ __valueToFaceBundleStringDict.onceToken.896
+ __valueToFaceBundleStringDict.onceToken.930
+ __valueToFaceBundleStringDict.onceToken.958
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1113
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1285
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1314
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1363
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1402
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1435
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1551
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1621
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1691
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1725
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1748
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1813
+ __valueToFaceBundleStringDict.valueToFaceBundleString.1870
+ __valueToFaceBundleStringDict.valueToFaceBundleString.895
+ __valueToFaceBundleStringDict.valueToFaceBundleString.929
+ __valueToFaceBundleStringDict.valueToFaceBundleString.957
+ _acceptsComplicationType:withFamily:forDevice:.onceToken.329
+ _kInvalidLuxValue
+ _kInvalidNitsValue
+ _ntk_seasons_spring2024
+ _ntk_seasons_spring2024_lightBlue
+ _ntk_seasons_spring2024_oceanBlue
+ _ntk_seasons_spring2024_pink
+ _ntk_seasons_spring2024_raspberry
+ _ntk_seasons_spring2024_softMint
+ _ntk_seasons_spring2024_sunshine
+ _ntk_zeus_spring2024
+ _objc_msgSend$_queue_resetConnection:
+ _objc_msgSend$modelWithLux:
+ _objc_msgSend$modelWithNits:
+ _objc_msgSend$tritiumModel
+ _providerForDevice:.__cachedDevice
+ _providerForDevice:.__lock
+ _providerForDevice:.__previousCLKDeviceVersion
+ _providerForDevice:.__provider
+ _providerForDevice:.lock
- -[NTKComplicationProvider init]
- GCC_except_table125
- GCC_except_table73
- __OBJC_$_PROP_LIST_NTKBlackcombColorPalette.120
- __OBJC_$_PROP_LIST_NTKCaliforniaColorPalette.131
- __OBJC_$_PROP_LIST_NTKFaceColorPalette.259
- __OBJC_$_PROP_LIST_NTKGossamerColorPalette.253
- __OBJC_$_PROP_LIST_NTKOlympusColorPalette.157
- __OBJC_$_PROP_LIST_NTKRichComplicationBezelView.127
- __OBJC_$_PROP_LIST_NTKUtilityComplicationView.423
- __OBJC_$_PROP_LIST_NTKUtilityFlatComplicationView.510
- ___119-[NTKPersistentFaceCollection loadFullCollectionWithOrderedUUIDs:selectedUUID:facesDescriptorsByUUID:seqId:completion:]_block_invoke.93
- ___119-[NTKPersistentFaceCollection loadFullCollectionWithOrderedUUIDs:selectedUUID:facesDescriptorsByUUID:seqId:completion:]_block_invoke.97
- ___121-[NTKDArgonService _push_sendNotificationForContent:requestIdentifier:toNotificationCenter:identifier:bundle:completion:]_block_invoke.270
- ___121-[NTKDArgonService _push_sendNotificationForContent:requestIdentifier:toNotificationCenter:identifier:bundle:completion:]_block_invoke.270.cold.1
- ___25-[NTKDArgonService _init]_block_invoke.153
- ___25-[NTKDArgonService _init]_block_invoke.160
- ___25-[NTKDArgonService _init]_block_invoke.160.cold.1
- ___25-[NTKDArgonService _init]_block_invoke.163
- ___25-[NTKDArgonService _init]_block_invoke.166
- ___25-[NTKDArgonService _init]_block_invoke.166.cold.1
- ___25-[NTKDArgonService start]_block_invoke.171
- ___33-[NTKCGalleryCell setCollection:]_block_invoke.87
- ___33-[NTKCGalleryCell setCollection:]_block_invoke_2.89
- ___44-[NTKSystemAppStateCache prewarmGizmoDaemon]_block_invoke.242
- ___47-[NTKGreenfieldAddWatchFaceManager _decodeUrl:]_block_invoke.246
- ___57-[NTKDArgonService connection:didReceiveIncomingMessage:]_block_invoke.212
- ___57-[NTKDArgonService connection:didReceiveIncomingMessage:]_block_invoke.212.cold.1
- ___57-[NTKFace _applyConfiguration:allowFailure:forMigration:]_block_invoke.232
- ___58-[NTKCPhotoFaceCollectionGalleryCollection initForDevice:]_block_invoke.170
- ___61-[NTKCWhistlerSubdialsFacesGalleryCollection facesForDevice:]_block_invoke.124
- ___62-[NTKDArgonService ingestKeyDescriptor:withMethod:completion:]_block_invoke.185
- ___62-[NTKDArgonService ingestKeyDescriptor:withMethod:completion:]_block_invoke.185.cold.1
- ___76-[NTKDArgonService _queue_push_userNotification_processWaitingNotifications]_block_invoke.226
- ___76-[NTKDArgonService _queue_push_userNotification_processWaitingNotifications]_block_invoke.226.cold.1
- ___76-[NTKDArgonService _queue_push_userNotification_processWaitingNotifications]_block_invoke.235
- ___76-[NTKDArgonService _queue_push_userNotification_processWaitingNotifications]_block_invoke.235.cold.1
- ___77-[NTKBundleComplicationMigrationServiceClient _queue_updateInvalidationTimer]_block_invoke.29
- ___80+[NTKSampleComplicationDataSource acceptsComplicationType:withFamily:forDevice:]_block_invoke.305
- ___81-[NTKBundleComplicationMigrationServiceClient _queue_serviceRequest:retryBudget:]_block_invoke.22
- ___81-[NTKBundleComplicationMigrationServiceClient _queue_serviceRequest:retryBudget:]_block_invoke.22.cold.1
- ___81-[NTKTimelineRemoteDataSourceProvider getCurrentEntryForComplication:completion:]_block_invoke.68
- ___84-[NTKGreenfieldAddWatchFaceManager _refreshInstalledComplicationsWithContinueBlock:]_block_invoke.317
- ___84-[NTKGreenfieldAddWatchFaceManager _refreshInstalledComplicationsWithContinueBlock:]_block_invoke.319
- ___84-[NTKGreenfieldAddWatchFaceManager _refreshInstalledComplicationsWithContinueBlock:]_block_invoke.320
- ___92-[NTKTimelineRemoteDataSourceProvider getEntriesForComplication:afterDate:limit:completion:]_block_invoke.72
- ___NTKAskFaceSupportServerForCurrentEnvironment_block_invoke.115
- ___NTKAskFaceSupportServerForKnownKeyDescriptors_block_invoke.112
- ___NTKAskFaceSupportServerToAddKeyDescriptor_block_invoke.102
- ___NTKAskFaceSupportServerToAddKeyDescriptor_block_invoke.103.cold.1
- ___NTKAskFaceSupportServerToChangeCurrentEnvironment_block_invoke.117
- ___NTKAskFaceSupportServerToDisplayUserNotificationForKeyDescriptor_block_invoke.114
- ___NTKAskFaceSupportServerToResetOnNextLaunch_block_invoke.111
- ___NTKCanAddWatchFace_block_invoke.480
- ___NTKHighPriorityApply_block_invoke.350
- ___NTKPhotosConfirmMemoryWasViewed_block_invoke.331
- ___NTKQueryFaceSupportServerForNewFaces_block_invoke.94
- ___NTKQueryFaceSupportServerForNewFaces_block_invoke.94.cold.1
- ___NTKQueryFaceSupportServerForNewFaces_block_invoke.98
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e53_v24?0"CLKWidgetComplicationDescriptor"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
- ___block_literal_global.1115
- ___block_literal_global.1287
- ___block_literal_global.1316
- ___block_literal_global.1365
- ___block_literal_global.1393
- ___block_literal_global.1404
- ___block_literal_global.1509
- ___block_literal_global.1511
- ___block_literal_global.1565
- ___block_literal_global.157
- ___block_literal_global.1620
- ___block_literal_global.1623
- ___block_literal_global.1625
- ___block_literal_global.1634
- ___block_literal_global.1639
- ___block_literal_global.1644
- ___block_literal_global.1646
- ___block_literal_global.1648
- ___block_literal_global.1663
- ___block_literal_global.1668
- ___block_literal_global.1675
- ___block_literal_global.1677
- ___block_literal_global.1684
- ___block_literal_global.1686
- ___block_literal_global.1689
- ___block_literal_global.1693
- ___block_literal_global.1703
- ___block_literal_global.1705
- ___block_literal_global.1727
- ___block_literal_global.173
- ___block_literal_global.1739
- ___block_literal_global.1750
- ___block_literal_global.176
- ___block_literal_global.1872
- ___block_literal_global.1915
- ___block_literal_global.211
- ___block_literal_global.245
- ___block_literal_global.256
- ___block_literal_global.261
- ___block_literal_global.263
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.275
- ___block_literal_global.282
- ___block_literal_global.307
- ___block_literal_global.325
- ___block_literal_global.329
- ___block_literal_global.334
- ___block_literal_global.336
- ___block_literal_global.348
- ___block_literal_global.353
- ___block_literal_global.365
- ___block_literal_global.381
- ___block_literal_global.407
- ___block_literal_global.415
- ___block_literal_global.417
- ___block_literal_global.432
- ___block_literal_global.445
- ___block_literal_global.453
- ___block_literal_global.464
- ___block_literal_global.469
- ___block_literal_global.516
- ___block_literal_global.523
- ___block_literal_global.56
- ___block_literal_global.570
- ___block_literal_global.572
- ___block_literal_global.592
- ___block_literal_global.595
- ___block_literal_global.64
- ___block_literal_global.68
- ___block_literal_global.684
- ___block_literal_global.751
- ___block_literal_global.768
- ___block_literal_global.771
- ___block_literal_global.773
- ___block_literal_global.775
- ___block_literal_global.778
- ___block_literal_global.781
- ___block_literal_global.784
- ___block_literal_global.787
- ___block_literal_global.790
- ___block_literal_global.793
- ___block_literal_global.83
- ___block_literal_global.86
- ___block_literal_global.897
- ___block_literal_global.91
- ___block_literal_global.931
- ___block_literal_global.959
- __imageScaleForTemplate:.__cachedDevice.350
- __imageScaleForTemplate:.__lock.349
- __imageScaleForTemplate:.__previousCLKDeviceVersion.351
- __imageScaleForTemplate:._scale.348
- __orderedValuesForDevice:.__cachedDevice.1230
- __orderedValuesForDevice:.__cachedDevice.1259
- __orderedValuesForDevice:.__cachedDevice.1297
- __orderedValuesForDevice:.__cachedDevice.1328
- __orderedValuesForDevice:.__cachedDevice.1414
- __orderedValuesForDevice:.__cachedDevice.1443
- __orderedValuesForDevice:.__cachedDevice.1580
- __orderedValuesForDevice:.__cachedDevice.1656
- __orderedValuesForDevice:.__cachedDevice.1665
- __orderedValuesForDevice:.__cachedDevice.1707
- __orderedValuesForDevice:.__cachedDevice.1737
- __orderedValuesForDevice:.__cachedDevice.1757
- __orderedValuesForDevice:.__cachedDevice.1856
- __orderedValuesForDevice:.__cachedDevice.823
- __orderedValuesForDevice:.__cachedDevice.832
- __orderedValuesForDevice:.__cachedDevice.841
- __orderedValuesForDevice:.__cachedDevice.866
- __orderedValuesForDevice:.__cachedDevice.906
- __orderedValuesForDevice:.__cachedDevice.940
- __orderedValuesForDevice:.__cachedDevice.969
- __orderedValuesForDevice:.__colors.1228
- __orderedValuesForDevice:.__colors.1441
- __orderedValuesForDevice:.__colors.1654
- __orderedValuesForDevice:.__colors.1755
- __orderedValuesForDevice:.__colors.1854
- __orderedValuesForDevice:.__colors.821
- __orderedValuesForDevice:.__colors.830
- __orderedValuesForDevice:.__colors.839
- __orderedValuesForDevice:.__colors.967
- __orderedValuesForDevice:.__lock.1229
- __orderedValuesForDevice:.__lock.1258
- __orderedValuesForDevice:.__lock.1296
- __orderedValuesForDevice:.__lock.1327
- __orderedValuesForDevice:.__lock.1413
- __orderedValuesForDevice:.__lock.1442
- __orderedValuesForDevice:.__lock.1579
- __orderedValuesForDevice:.__lock.1655
- __orderedValuesForDevice:.__lock.1664
- __orderedValuesForDevice:.__lock.1706
- __orderedValuesForDevice:.__lock.1736
- __orderedValuesForDevice:.__lock.1756
- __orderedValuesForDevice:.__lock.1855
- __orderedValuesForDevice:.__lock.822
- __orderedValuesForDevice:.__lock.831
- __orderedValuesForDevice:.__lock.840
- __orderedValuesForDevice:.__lock.865
- __orderedValuesForDevice:.__lock.905
- __orderedValuesForDevice:.__lock.939
- __orderedValuesForDevice:.__lock.968
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1231
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1260
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1298
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1329
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1415
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1444
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1581
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1657
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1666
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1708
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1738
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1758
- __orderedValuesForDevice:.__previousCLKDeviceVersion.1857
- __orderedValuesForDevice:.__previousCLKDeviceVersion.824
- __orderedValuesForDevice:.__previousCLKDeviceVersion.833
- __orderedValuesForDevice:.__previousCLKDeviceVersion.842
- __orderedValuesForDevice:.__previousCLKDeviceVersion.867
- __orderedValuesForDevice:.__previousCLKDeviceVersion.907
- __orderedValuesForDevice:.__previousCLKDeviceVersion.941
- __orderedValuesForDevice:.__previousCLKDeviceVersion.970
- __orderedValuesForDevice:.__styles.1257
- __orderedValuesForDevice:.__styles.1295
- __orderedValuesForDevice:.__styles.1326
- __orderedValuesForDevice:.__styles.1412
- __orderedValuesForDevice:.__styles.1663
- __orderedValuesForDevice:.__styles.1735
- __orderedValuesRestrictedByDevice:.__cachedDevice.1702
- __orderedValuesRestrictedByDevice:.__cachedDevice.1770
- __orderedValuesRestrictedByDevice:.__lock.1701
- __orderedValuesRestrictedByDevice:.__lock.1769
- __orderedValuesRestrictedByDevice:.__previousCLKDeviceVersion.1703
- __orderedValuesRestrictedByDevice:.__previousCLKDeviceVersion.1771
- __orderedValuesRestrictedByDevice:.hardwareSpecificValues.1700
- __orderedValuesRestrictedByDevice:.hardwareSpecificValues.1768
- __unnamed_array_storage.100
- __unnamed_array_storage.1002
- __unnamed_array_storage.1005
- __unnamed_array_storage.1008
- __unnamed_array_storage.105
- __unnamed_array_storage.116
- __unnamed_array_storage.119
- __unnamed_array_storage.122
- __unnamed_array_storage.1233
- __unnamed_array_storage.1264
- __unnamed_array_storage.1333
- __unnamed_array_storage.1375
- __unnamed_array_storage.1381
- __unnamed_array_storage.1384
- __unnamed_array_storage.1387
- __unnamed_array_storage.1390
- __unnamed_array_storage.1417
- __unnamed_array_storage.1585
- __unnamed_array_storage.1588
- __unnamed_array_storage.1631
- __unnamed_array_storage.1636
- __unnamed_array_storage.1641
- __unnamed_array_storage.1660
- __unnamed_array_storage.1665
- __unnamed_array_storage.1670
- __unnamed_array_storage.1672
- __unnamed_array_storage.1681
- __unnamed_array_storage.1710
- __unnamed_array_storage.1745
- __unnamed_array_storage.1763
- __unnamed_array_storage.1766
- __unnamed_array_storage.1861
- __unnamed_array_storage.223
- __unnamed_array_storage.232
- __unnamed_array_storage.243
- __unnamed_array_storage.279
- __unnamed_array_storage.301
- __unnamed_array_storage.311
- __unnamed_array_storage.341
- __unnamed_array_storage.447
- __unnamed_array_storage.529
- __unnamed_array_storage.844
- __unnamed_array_storage.97
- __unnamed_array_storage.972
- __unnamed_array_storage.978
- __unnamed_array_storage.981
- __unnamed_array_storage.984
- __unnamed_array_storage.987
- __unnamed_array_storage.990
- __unnamed_array_storage.993
- __unnamed_array_storage.996
- __unnamed_array_storage.999
- __valueToFaceBundleStringDict.onceToken.1113
- __valueToFaceBundleStringDict.onceToken.1238
- __valueToFaceBundleStringDict.onceToken.1285
- __valueToFaceBundleStringDict.onceToken.1314
- __valueToFaceBundleStringDict.onceToken.1363
- __valueToFaceBundleStringDict.onceToken.1402
- __valueToFaceBundleStringDict.onceToken.1435
- __valueToFaceBundleStringDict.onceToken.1551
- __valueToFaceBundleStringDict.onceToken.1621
- __valueToFaceBundleStringDict.onceToken.1691
- __valueToFaceBundleStringDict.onceToken.1725
- __valueToFaceBundleStringDict.onceToken.1748
- __valueToFaceBundleStringDict.onceToken.1813
- __valueToFaceBundleStringDict.onceToken.1870
- __valueToFaceBundleStringDict.onceToken.895
- __valueToFaceBundleStringDict.onceToken.929
- __valueToFaceBundleStringDict.onceToken.957
- __valueToFaceBundleStringDict.valueToFaceBundleString.1112
- __valueToFaceBundleStringDict.valueToFaceBundleString.1284
- __valueToFaceBundleStringDict.valueToFaceBundleString.1313
- __valueToFaceBundleStringDict.valueToFaceBundleString.1362
- __valueToFaceBundleStringDict.valueToFaceBundleString.1401
- __valueToFaceBundleStringDict.valueToFaceBundleString.1434
- __valueToFaceBundleStringDict.valueToFaceBundleString.1550
- __valueToFaceBundleStringDict.valueToFaceBundleString.1620
- __valueToFaceBundleStringDict.valueToFaceBundleString.1690
- __valueToFaceBundleStringDict.valueToFaceBundleString.1724
- __valueToFaceBundleStringDict.valueToFaceBundleString.1747
- __valueToFaceBundleStringDict.valueToFaceBundleString.1812
- __valueToFaceBundleStringDict.valueToFaceBundleString.1869
- __valueToFaceBundleStringDict.valueToFaceBundleString.894
- __valueToFaceBundleStringDict.valueToFaceBundleString.928
- __valueToFaceBundleStringDict.valueToFaceBundleString.956
- _acceptsComplicationType:withFamily:forDevice:.onceToken.304
- _swift_bridgeObjectRetain
- _swift_unknownObjectRetain
CStrings:
+ "%.0f"
+ "%s - fastFaceSwitchingEnabled:%@"
+ "-[NTKFastFaceSwitchingSettings _readValue]"
+ "Fatal error"
+ "Internal: Lux Viewer"
+ "Internal: Nits Viewer"
+ "LUX"
+ "NITS"
+ "NTKGroupedBezelProperties"
+ "NTKLuxViewerComplicationDataSource"
+ "NTKLuxViewerComplicationEntryModel"
+ "NTKNitsViewerComplicationDataSource"
+ "NTKNitsViewerComplicationEntryModel"
+ "PhotosColorRamps-SS2024"
+ "Swift/UnsafePointer.swift"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIColor\",?,R,D,N"
+ "T@\"UIColor\",?,R,N"
+ "T@\"UIFontDescriptor\",?,C,N"
+ "TB,?,N"
+ "TB,?,N,GisHighlighted"
+ "Td,?,N"
+ "Td,N,V_bezelTextRadius"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "_CN"
+ "_bezelTextRadius"
+ "_luxValue"
+ "_nitsValue"
+ "_queue_resetConnection:"
+ "_updateTimer"
+ "description=NanoTimeKitCompanion-2398.92"
+ "lux viewer"
+ "modelWithLux:"
+ "modelWithNits:"
+ "nits viewer"
+ "seasons.spring2024"
+ "seasons.spring2024.lightBlue"
+ "seasons.spring2024.oceanBlue"
+ "seasons.spring2024.pink"
+ "seasons.spring2024.raspberry"
+ "seasons.spring2024.softMint"
+ "seasons.spring2024.sunshine"
+ "tritiumModel"
+ "updatePropertiesAsGroupWithHandler:"
+ "v24@0:8@?<v@?@\"NTKGroupedBezelProperties\">16"
+ "zeus.spring2024"
- "PhotosColorRamps-F2023"
- "T@\"UIFontDescriptor\",C,N"
- "TB,N,GisHighlighted"
- "description=NanoTimeKitCompanion-2398.53.19"

```
