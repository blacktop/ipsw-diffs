## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1516.0.0.0.0
-  __TEXT.__text: 0x18030c
-  __TEXT.__objc_methlist: 0xae04
-  __TEXT.__const: 0x2a8
+1520.2.3.0.2
+  __TEXT.__text: 0x1815fc
+  __TEXT.__objc_methlist: 0xaf1c
+  __TEXT.__const: 0x2c8
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x30a8
-  __TEXT.__cstring: 0x7033
-  __TEXT.__oslogstring: 0x502d8
+  __TEXT.__gcc_except_tab: 0x30b0
+  __TEXT.__cstring: 0x704f
+  __TEXT.__oslogstring: 0x50502
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x3ce8
+  __TEXT.__unwind_info: 0x3d28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4960
-  __DATA_CONST.__objc_classlist: 0x458
+  __DATA_CONST.__const: 0x4938
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7160
+  __DATA_CONST.__objc_selrefs: 0x71c8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x310
+  __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x240
-  __DATA_CONST.__got: 0x9f8
-  __AUTH_CONST.__const: 0x1160
-  __AUTH_CONST.__cfstring: 0x6dc0
-  __AUTH_CONST.__objc_const: 0x10330
+  __DATA_CONST.__got: 0xa08
+  __AUTH_CONST.__const: 0x1180
+  __AUTH_CONST.__cfstring: 0x6ee0
+  __AUTH_CONST.__objc_const: 0x10640
   __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1e50
-  __DATA.__objc_ivar: 0xb78
+  __AUTH.__objc_data: 0x1ea0
+  __DATA.__objc_ivar: 0xbac
   __DATA.__data: 0xea0
   __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4508
-  Symbols:   7381
-  CStrings:  5818
+  Functions: 4537
+  Symbols:   7430
+  CStrings:  5832
 
Symbols:
+ +[HMMTRAsyncMutex logCategory]
+ -[HMMTRAccessoryServerBrowser _makeAccessoryServerFactory]
+ -[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]
+ -[HMMTRAccessoryServerBrowser discoveredAccessoryServersAsyncMutex]
+ -[HMMTRAccessoryServerBrowser updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]
+ -[HMMTRAccessoryServerBrowser workQueueFactory]
+ -[HMMTRAccessoryServerFactory workQueueFactory]
+ -[HMMTRAsyncMutex .cxx_destruct]
+ -[HMMTRAsyncMutex initWithQueue:]
+ -[HMMTRAsyncMutex lockWithCompletion:]
+ -[HMMTRAsyncMutex locked]
+ -[HMMTRAsyncMutex pendingCompletions]
+ -[HMMTRAsyncMutex queue]
+ -[HMMTRAsyncMutex setLocked:]
+ -[HMMTRAsyncMutex unlock]
+ -[HMMTRControllerFactory workQueueFactory]
+ -[HMMTRControllerFactoryStorage initWithWorkQueueFactory:]
+ -[HMMTRControllerFactoryStorage workQueueFactory]
+ -[HMMTRDescriptorClusterManager workQueueFactory]
+ -[HMMTRExclusiveServerActionQueue workQueueFactory]
+ -[HMMTRFirmwareUpdateStatus workQueueFactory]
+ -[HMMTRSystemCommissionerControllerParams workQueueFactory]
+ -[HMMTRThreadRadioManager workQueueFactory]
+ GCC_except_table1056
+ GCC_except_table1060
+ GCC_except_table1062
+ GCC_except_table1184
+ GCC_except_table1244
+ GCC_except_table1290
+ GCC_except_table1298
+ GCC_except_table1349
+ GCC_except_table1357
+ GCC_except_table1394
+ GCC_except_table1432
+ GCC_except_table1459
+ GCC_except_table1656
+ GCC_except_table1697
+ GCC_except_table1849
+ GCC_except_table1850
+ GCC_except_table1851
+ GCC_except_table1854
+ GCC_except_table1874
+ GCC_except_table1875
+ GCC_except_table1876
+ GCC_except_table1877
+ GCC_except_table1878
+ GCC_except_table1881
+ GCC_except_table1884
+ GCC_except_table1885
+ GCC_except_table1886
+ GCC_except_table1887
+ GCC_except_table1888
+ GCC_except_table1889
+ GCC_except_table1890
+ GCC_except_table1949
+ GCC_except_table1955
+ GCC_except_table1993
+ GCC_except_table2076
+ GCC_except_table2192
+ GCC_except_table2194
+ GCC_except_table2225
+ GCC_except_table2234
+ GCC_except_table2236
+ GCC_except_table2285
+ GCC_except_table2322
+ GCC_except_table2346
+ GCC_except_table2412
+ GCC_except_table2691
+ GCC_except_table2693
+ GCC_except_table2695
+ GCC_except_table2699
+ GCC_except_table2760
+ GCC_except_table2801
+ GCC_except_table2848
+ GCC_except_table2850
+ GCC_except_table2905
+ GCC_except_table2906
+ GCC_except_table2907
+ GCC_except_table2908
+ GCC_except_table2909
+ GCC_except_table2911
+ GCC_except_table2912
+ GCC_except_table2922
+ GCC_except_table2924
+ GCC_except_table2936
+ GCC_except_table2955
+ GCC_except_table2977
+ GCC_except_table2990
+ GCC_except_table2997
+ GCC_except_table3012
+ GCC_except_table3015
+ GCC_except_table3019
+ GCC_except_table3021
+ GCC_except_table3051
+ GCC_except_table3060
+ GCC_except_table3065
+ GCC_except_table3077
+ GCC_except_table3129
+ GCC_except_table3130
+ GCC_except_table3520
+ GCC_except_table3545
+ GCC_except_table3547
+ GCC_except_table3551
+ GCC_except_table3556
+ GCC_except_table3559
+ GCC_except_table3575
+ GCC_except_table3590
+ GCC_except_table3659
+ GCC_except_table3667
+ GCC_except_table3669
+ GCC_except_table3676
+ GCC_except_table3677
+ GCC_except_table3710
+ GCC_except_table3719
+ GCC_except_table3723
+ GCC_except_table3757
+ GCC_except_table3760
+ GCC_except_table3768
+ GCC_except_table3790
+ GCC_except_table3794
+ GCC_except_table3833
+ GCC_except_table3835
+ GCC_except_table3837
+ GCC_except_table3854
+ GCC_except_table3856
+ GCC_except_table3874
+ GCC_except_table3951
+ GCC_except_table3998
+ GCC_except_table4016
+ GCC_except_table4039
+ GCC_except_table4043
+ GCC_except_table4058
+ GCC_except_table4059
+ GCC_except_table4060
+ GCC_except_table4066
+ GCC_except_table4073
+ GCC_except_table4078
+ GCC_except_table4133
+ GCC_except_table4155
+ GCC_except_table4197
+ GCC_except_table4202
+ GCC_except_table4205
+ GCC_except_table4289
+ GCC_except_table4290
+ GCC_except_table4346
+ GCC_except_table4349
+ GCC_except_table4411
+ GCC_except_table4473
+ GCC_except_table4477
+ GCC_except_table4481
+ GCC_except_table4484
+ GCC_except_table4517
+ GCC_except_table572
+ GCC_except_table576
+ GCC_except_table578
+ GCC_except_table580
+ GCC_except_table753
+ GCC_except_table754
+ GCC_except_table811
+ GCC_except_table812
+ GCC_except_table813
+ GCC_except_table886
+ GCC_except_table928
+ GCC_except_table978
+ GCC_except_table982
+ GCC_except_table984
+ GCC_except_table986
+ GCC_except_table988
+ GCC_except_table992
+ _HAPWorkQueueFactoryOrDefault
+ _HMErrorDomain
+ _HMMTRIsSecondPartyProduct
+ _OBJC_CLASS_$_HMMTRAsyncMutex
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._discoveredAccessoryServersAsyncMutex
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._workQueueFactory
+ _OBJC_IVAR_$_HMMTRAccessoryServerFactory._workQueueFactory
+ _OBJC_IVAR_$_HMMTRAsyncMutex._locked
+ _OBJC_IVAR_$_HMMTRAsyncMutex._pendingCompletions
+ _OBJC_IVAR_$_HMMTRAsyncMutex._queue
+ _OBJC_IVAR_$_HMMTRControllerFactory._workQueueFactory
+ _OBJC_IVAR_$_HMMTRControllerFactoryStorage._workQueueFactory
+ _OBJC_IVAR_$_HMMTRDescriptorClusterManager._workQueueFactory
+ _OBJC_IVAR_$_HMMTRExclusiveServerActionQueue._workQueueFactory
+ _OBJC_IVAR_$_HMMTRFirmwareUpdateStatus._workQueueFactory
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._workQueueFactory
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._workQueueFactory
+ _OBJC_METACLASS_$_HMMTRAsyncMutex
+ __OBJC_$_CLASS_METHODS_HMMTRAsyncMutex
+ __OBJC_$_INSTANCE_METHODS_HMMTRAsyncMutex
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAsyncMutex
+ __OBJC_$_PROP_LIST_HMMTRAsyncMutex
+ __OBJC_CLASS_RO_$_HMMTRAsyncMutex
+ __OBJC_METACLASS_RO_$_HMMTRAsyncMutex
+ ___177-[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:accessoryServerNodeIDs:forTargetFabricUUID:]_block_invoke_2
+ ___25-[HMMTRAsyncMutex unlock]_block_invoke
+ ___30+[HMMTRAsyncMutex logCategory]_block_invoke
+ ___38-[HMMTRAsyncMutex lockWithCompletion:]_block_invoke
+ ___95-[HMMTRAccessoryServerBrowser updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]_block_invoke
+ ___96-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]_block_invoke
+ ___96-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]_block_invoke_2
+ _secondPartyProducts
- -[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]
- GCC_except_table1041
- GCC_except_table1045
- GCC_except_table1047
- GCC_except_table1169
- GCC_except_table1229
- GCC_except_table1275
- GCC_except_table1283
- GCC_except_table1332
- GCC_except_table1340
- GCC_except_table1377
- GCC_except_table1414
- GCC_except_table1441
- GCC_except_table1637
- GCC_except_table1678
- GCC_except_table1830
- GCC_except_table1831
- GCC_except_table1832
- GCC_except_table1835
- GCC_except_table1855
- GCC_except_table1856
- GCC_except_table1857
- GCC_except_table1858
- GCC_except_table1859
- GCC_except_table1862
- GCC_except_table1865
- GCC_except_table1866
- GCC_except_table1867
- GCC_except_table1868
- GCC_except_table1869
- GCC_except_table1870
- GCC_except_table1871
- GCC_except_table1930
- GCC_except_table1936
- GCC_except_table1974
- GCC_except_table2057
- GCC_except_table2173
- GCC_except_table2175
- GCC_except_table2205
- GCC_except_table2213
- GCC_except_table2215
- GCC_except_table2264
- GCC_except_table2301
- GCC_except_table2325
- GCC_except_table2390
- GCC_except_table2667
- GCC_except_table2669
- GCC_except_table2671
- GCC_except_table2675
- GCC_except_table2736
- GCC_except_table2777
- GCC_except_table2823
- GCC_except_table2825
- GCC_except_table2856
- GCC_except_table2857
- GCC_except_table2858
- GCC_except_table2880
- GCC_except_table2884
- GCC_except_table2885
- GCC_except_table2886
- GCC_except_table2887
- GCC_except_table2897
- GCC_except_table2899
- GCC_except_table2929
- GCC_except_table2945
- GCC_except_table2951
- GCC_except_table2964
- GCC_except_table2967
- GCC_except_table2986
- GCC_except_table2989
- GCC_except_table2995
- GCC_except_table3023
- GCC_except_table3032
- GCC_except_table3037
- GCC_except_table3049
- GCC_except_table3100
- GCC_except_table3101
- GCC_except_table3491
- GCC_except_table3516
- GCC_except_table3517
- GCC_except_table3518
- GCC_except_table3522
- GCC_except_table3527
- GCC_except_table3530
- GCC_except_table3561
- GCC_except_table3630
- GCC_except_table3638
- GCC_except_table3640
- GCC_except_table3647
- GCC_except_table3648
- GCC_except_table3681
- GCC_except_table3690
- GCC_except_table3694
- GCC_except_table3728
- GCC_except_table3731
- GCC_except_table3739
- GCC_except_table3761
- GCC_except_table3765
- GCC_except_table3804
- GCC_except_table3806
- GCC_except_table3808
- GCC_except_table3825
- GCC_except_table3827
- GCC_except_table3845
- GCC_except_table3922
- GCC_except_table3969
- GCC_except_table3987
- GCC_except_table4010
- GCC_except_table4014
- GCC_except_table4029
- GCC_except_table4030
- GCC_except_table4031
- GCC_except_table4037
- GCC_except_table4044
- GCC_except_table4049
- GCC_except_table4104
- GCC_except_table4126
- GCC_except_table4168
- GCC_except_table4173
- GCC_except_table4176
- GCC_except_table4260
- GCC_except_table4261
- GCC_except_table4317
- GCC_except_table4320
- GCC_except_table4382
- GCC_except_table4444
- GCC_except_table4448
- GCC_except_table4452
- GCC_except_table4455
- GCC_except_table4488
- GCC_except_table571
- GCC_except_table575
- GCC_except_table577
- GCC_except_table579
- GCC_except_table739
- GCC_except_table740
- GCC_except_table797
- GCC_except_table798
- GCC_except_table799
- GCC_except_table872
- GCC_except_table914
- GCC_except_table963
- GCC_except_table967
- GCC_except_table969
- GCC_except_table971
- GCC_except_table973
- GCC_except_table977
- ___84-[HMMTRAccessoryServerBrowser updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke
- ___85-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke
- ___85-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8ls32l8s40l8s48l8
- _dispatch_queue_create_with_target$V2
CStrings:
+ "Firmware update connection attempt for an accessory with nodeID %@, error = %@"
+ "Lock acquired"
+ "Lock handed to next waiter (pending=%lu)"
+ "Lock is held; queued waiter (pending=%lu)"
+ "Lock released"
+ "ProxPairing"
+ "Refusing to commission vendor %@ product %@: pairing this accessory is not supported"
+ "Unlock called while not locked; ignoring"
+ "[%{public}@] Firmware update connection attempt for an accessory with nodeID %@, error = %@"
+ "[%{public}@] Lock acquired"
+ "[%{public}@] Lock handed to next waiter (pending=%lu)"
+ "[%{public}@] Lock is held; queued waiter (pending=%lu)"
+ "[%{public}@] Lock released"
+ "[%{public}@] Refusing to commission vendor %@ product %@: pairing this accessory is not supported"
+ "[%{public}@] Unlock called while not locked; ignoring"
+ "hmmtr.asyncmutex"
- "Firmware update connection attempt for a accessory with nodeID %@, error = %@"
- "[%{public}@] Firmware update connection attempt for a accessory with nodeID %@, error = %@"
```
