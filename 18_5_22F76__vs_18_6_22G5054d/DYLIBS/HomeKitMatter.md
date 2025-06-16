## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1278.6.31.1.1
-  __TEXT.__text: 0x133d90
+1278.7.19.0.0
+  __TEXT.__text: 0x1346e4
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x9ccc
-  __TEXT.__const: 0x158
+  __TEXT.__objc_methlist: 0x9cf4
+  __TEXT.__const: 0x150
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__gcc_except_tab: 0x2b5c
-  __TEXT.__cstring: 0x6014
-  __TEXT.__oslogstring: 0x25e34
+  __TEXT.__cstring: 0x645c
+  __TEXT.__oslogstring: 0x2602d
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2cc8
+  __TEXT.__unwind_info: 0x2cd0
   __TEXT.__objc_classname: 0x133b
-  __TEXT.__objc_methname: 0x23e0d
+  __TEXT.__objc_methname: 0x23f47
   __TEXT.__objc_methtype: 0x3859
-  __TEXT.__objc_stubs: 0x15820
+  __TEXT.__objc_stubs: 0x158c0
   __DATA_CONST.__got: 0x998
-  __DATA_CONST.__const: 0x4530
+  __DATA_CONST.__const: 0x4560
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67a8
+  __DATA_CONST.__objc_selrefs: 0x67d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x228
   __AUTH_CONST.__auth_got: 0x530
   __AUTH_CONST.__const: 0xec0
-  __AUTH_CONST.__cfstring: 0x6440
+  __AUTH_CONST.__cfstring: 0x67a0
   __AUTH_CONST.__objc_const: 0xe9c0
-  __AUTH_CONST.__objc_intobj: 0x15d8
+  __AUTH_CONST.__objc_intobj: 0x1608
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_doubleobj: 0x20
+  __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1db0
   __DATA.__objc_ivar: 0xa50

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF3E330C-826C-3E5E-824A-95211C3E3FA8
-  Functions: 4085
-  Symbols:   14111
-  CStrings:  9023
+  UUID: 80779D33-5756-3990-83FC-E7B4A67568F6
+  Functions: 4089
+  Symbols:   14124
+  CStrings:  9090
 
Symbols:
+ -[HMMTRAccessoryServer readSpecificationVersionWithCompletionHandler:]
+ -[HMMTRDescriptorClusterManager _populateMeasuredValueAttributeForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:]
+ -[HMMTRProtocolMap getBaseClusterName:]
+ GCC_except_table2104
+ GCC_except_table2166
+ GCC_except_table2406
+ GCC_except_table2410
+ GCC_except_table2459
+ GCC_except_table2467
+ GCC_except_table2508
+ GCC_except_table2546
+ GCC_except_table2548
+ GCC_except_table2574
+ GCC_except_table2599
+ GCC_except_table2611
+ GCC_except_table2613
+ GCC_except_table2632
+ GCC_except_table2648
+ GCC_except_table2654
+ GCC_except_table2665
+ GCC_except_table2668
+ GCC_except_table2672
+ GCC_except_table2684
+ GCC_except_table2688
+ GCC_except_table2690
+ GCC_except_table2709
+ GCC_except_table2715
+ GCC_except_table2722
+ GCC_except_table2735
+ GCC_except_table2787
+ GCC_except_table3151
+ GCC_except_table3154
+ GCC_except_table3159
+ GCC_except_table3162
+ GCC_except_table3176
+ GCC_except_table3192
+ GCC_except_table3253
+ GCC_except_table3268
+ GCC_except_table3270
+ GCC_except_table3278
+ GCC_except_table3304
+ GCC_except_table3336
+ GCC_except_table3339
+ GCC_except_table3347
+ GCC_except_table3366
+ GCC_except_table3369
+ GCC_except_table3405
+ GCC_except_table3409
+ GCC_except_table3425
+ GCC_except_table3427
+ GCC_except_table3445
+ GCC_except_table3506
+ GCC_except_table3550
+ GCC_except_table3567
+ GCC_except_table3592
+ GCC_except_table3596
+ GCC_except_table3611
+ GCC_except_table3612
+ GCC_except_table3617
+ GCC_except_table3624
+ GCC_except_table3682
+ GCC_except_table3702
+ GCC_except_table3755
+ GCC_except_table3763
+ GCC_except_table3840
+ GCC_except_table3841
+ GCC_except_table3896
+ GCC_except_table3899
+ GCC_except_table4020
+ GCC_except_table4023
+ GCC_except_table4046
+ GCC_except_table4069
+ ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.413
+ ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.338
+ ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.339
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.349
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.352
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.350
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.313
+ ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.292
+ ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.294
+ ___70-[HMMTRAccessoryServer readSpecificationVersionWithCompletionHandler:]_block_invoke
+ ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.273
+ ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.416
+ ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.387
+ ___96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.389
+ ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.417
+ ___Block_byref_object_copy_.10484
+ ___Block_byref_object_copy_.11142
+ ___Block_byref_object_copy_.11823
+ ___Block_byref_object_copy_.12020
+ ___Block_byref_object_copy_.6895
+ ___Block_byref_object_copy_.7256
+ ___Block_byref_object_copy_.7679
+ ___Block_byref_object_copy_.8765
+ ___Block_byref_object_copy_.9713
+ ___Block_byref_object_dispose_.10485
+ ___Block_byref_object_dispose_.11143
+ ___Block_byref_object_dispose_.11824
+ ___Block_byref_object_dispose_.12021
+ ___Block_byref_object_dispose_.6896
+ ___Block_byref_object_dispose_.7257
+ ___Block_byref_object_dispose_.7680
+ ___Block_byref_object_dispose_.8766
+ ___Block_byref_object_dispose_.9714
+ ___block_literal_global.10180
+ ___block_literal_global.10741
+ ___block_literal_global.10964
+ ___block_literal_global.11179
+ ___block_literal_global.11323
+ ___block_literal_global.11438
+ ___block_literal_global.11871
+ ___block_literal_global.201
+ ___block_literal_global.275
+ ___block_literal_global.333
+ ___block_literal_global.361.8951
+ ___block_literal_global.396
+ ___block_literal_global.46.9514
+ ___block_literal_global.531
+ ___block_literal_global.6176
+ ___block_literal_global.6270
+ ___block_literal_global.6364
+ ___block_literal_global.6469
+ ___block_literal_global.6563
+ ___block_literal_global.6657
+ ___block_literal_global.6798
+ ___block_literal_global.6937
+ ___block_literal_global.7046
+ ___block_literal_global.7125
+ ___block_literal_global.7462
+ ___block_literal_global.75.9515
+ ___block_literal_global.7690
+ ___block_literal_global.8021
+ ___block_literal_global.8144
+ ___block_literal_global.8796
+ ___block_literal_global.9193
+ ___block_literal_global.9513
+ ___block_literal_global.9590
+ _logCategory._hmf_once_t103
+ _logCategory._hmf_once_t14
+ _logCategory._hmf_once_t14.6175
+ _logCategory._hmf_once_t14.6269
+ _logCategory._hmf_once_t14.6468
+ _logCategory._hmf_once_t14.6562
+ _logCategory._hmf_once_t14.6656
+ _logCategory._hmf_once_t2.6797
+ _logCategory._hmf_once_t2.9589
+ _logCategory._hmf_once_t20.11322
+ _logCategory._hmf_once_t201
+ _logCategory._hmf_once_t26.6363
+ _logCategory._hmf_once_t31.11437
+ _logCategory._hmf_once_t364
+ _logCategory._hmf_once_t4.7045
+ _logCategory._hmf_once_t653
+ _logCategory._hmf_once_t8.10963
+ _logCategory._hmf_once_v104
+ _logCategory._hmf_once_v15
+ _logCategory._hmf_once_v15.6177
+ _logCategory._hmf_once_v15.6271
+ _logCategory._hmf_once_v15.6470
+ _logCategory._hmf_once_v15.6564
+ _logCategory._hmf_once_v15.6658
+ _logCategory._hmf_once_v202
+ _logCategory._hmf_once_v21.11324
+ _logCategory._hmf_once_v27.6365
+ _logCategory._hmf_once_v3.6799
+ _logCategory._hmf_once_v3.9591
+ _logCategory._hmf_once_v32.11439
+ _logCategory._hmf_once_v365
+ _logCategory._hmf_once_v5.7047
+ _logCategory._hmf_once_v654
+ _logCategory._hmf_once_v9.10965
+ _objc_msgSend$_populateMeasuredValueAttributeForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:
+ _objc_msgSend$getBaseClusterName:
+ _objc_msgSend$readAttributeMaxMeasuredValueWithParams:
+ _objc_msgSend$readAttributeMinMeasuredValueWithParams:
+ _objc_msgSend$readAttributeSpecificationVersionWithParams:
- GCC_except_table2103
- GCC_except_table2165
- GCC_except_table2405
- GCC_except_table2409
- GCC_except_table2458
- GCC_except_table2466
- GCC_except_table2507
- GCC_except_table2545
- GCC_except_table2547
- GCC_except_table2571
- GCC_except_table2591
- GCC_except_table2610
- GCC_except_table2612
- GCC_except_table2631
- GCC_except_table2647
- GCC_except_table2653
- GCC_except_table2664
- GCC_except_table2667
- GCC_except_table2671
- GCC_except_table2683
- GCC_except_table2687
- GCC_except_table2689
- GCC_except_table2708
- GCC_except_table2714
- GCC_except_table2721
- GCC_except_table2734
- GCC_except_table2785
- GCC_except_table3148
- GCC_except_table3153
- GCC_except_table3158
- GCC_except_table3161
- GCC_except_table3175
- GCC_except_table3191
- GCC_except_table3252
- GCC_except_table3267
- GCC_except_table3269
- GCC_except_table3276
- GCC_except_table3302
- GCC_except_table3335
- GCC_except_table3338
- GCC_except_table3346
- GCC_except_table3365
- GCC_except_table3368
- GCC_except_table3404
- GCC_except_table3408
- GCC_except_table3424
- GCC_except_table3426
- GCC_except_table3444
- GCC_except_table3503
- GCC_except_table3547
- GCC_except_table3564
- GCC_except_table3589
- GCC_except_table3593
- GCC_except_table3608
- GCC_except_table3609
- GCC_except_table3614
- GCC_except_table3621
- GCC_except_table3679
- GCC_except_table3699
- GCC_except_table3752
- GCC_except_table3757
- GCC_except_table3836
- GCC_except_table3837
- GCC_except_table3892
- GCC_except_table3895
- GCC_except_table4008
- GCC_except_table4019
- GCC_except_table4042
- GCC_except_table4065
- ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.408
- ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.285
- ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.286
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.296
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.299
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.297
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.260
- ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.239
- ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.287
- ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.266
- ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.411
- ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.334
- ___96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.336
- ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.412
- ___Block_byref_object_copy_.10442
- ___Block_byref_object_copy_.11120
- ___Block_byref_object_copy_.11801
- ___Block_byref_object_copy_.11998
- ___Block_byref_object_copy_.6917
- ___Block_byref_object_copy_.7268
- ___Block_byref_object_copy_.7688
- ___Block_byref_object_copy_.8772
- ___Block_byref_object_copy_.9722
- ___Block_byref_object_dispose_.10443
- ___Block_byref_object_dispose_.11121
- ___Block_byref_object_dispose_.11802
- ___Block_byref_object_dispose_.11999
- ___Block_byref_object_dispose_.6918
- ___Block_byref_object_dispose_.7269
- ___Block_byref_object_dispose_.7689
- ___Block_byref_object_dispose_.8773
- ___Block_byref_object_dispose_.9723
- ___block_literal_global.10181
- ___block_literal_global.10719
- ___block_literal_global.10942
- ___block_literal_global.11157
- ___block_literal_global.11301
- ___block_literal_global.11416
- ___block_literal_global.11849
- ___block_literal_global.197
- ___block_literal_global.268
- ___block_literal_global.280
- ___block_literal_global.343
- ___block_literal_global.361.8959
- ___block_literal_global.46.9523
- ___block_literal_global.482
- ___block_literal_global.6179
- ___block_literal_global.6276
- ___block_literal_global.6372
- ___block_literal_global.6482
- ___block_literal_global.6579
- ___block_literal_global.6676
- ___block_literal_global.6820
- ___block_literal_global.6959
- ___block_literal_global.7068
- ___block_literal_global.7147
- ___block_literal_global.7472
- ___block_literal_global.75.9524
- ___block_literal_global.7699
- ___block_literal_global.8030
- ___block_literal_global.8153
- ___block_literal_global.8803
- ___block_literal_global.9202
- ___block_literal_global.9522
- ___block_literal_global.9599
- _logCategory._hmf_once_t195
- _logCategory._hmf_once_t2.6819
- _logCategory._hmf_once_t2.9598
- _logCategory._hmf_once_t20.11300
- _logCategory._hmf_once_t23
- _logCategory._hmf_once_t23.6178
- _logCategory._hmf_once_t23.6275
- _logCategory._hmf_once_t23.6481
- _logCategory._hmf_once_t23.6578
- _logCategory._hmf_once_t23.6675
- _logCategory._hmf_once_t31.11415
- _logCategory._hmf_once_t363
- _logCategory._hmf_once_t4.7067
- _logCategory._hmf_once_t44
- _logCategory._hmf_once_t651
- _logCategory._hmf_once_t8.10941
- _logCategory._hmf_once_t87
- _logCategory._hmf_once_v196
- _logCategory._hmf_once_v21.11302
- _logCategory._hmf_once_v24
- _logCategory._hmf_once_v24.6180
- _logCategory._hmf_once_v24.6277
- _logCategory._hmf_once_v24.6483
- _logCategory._hmf_once_v24.6580
- _logCategory._hmf_once_v24.6677
- _logCategory._hmf_once_v3.6821
- _logCategory._hmf_once_v3.9600
- _logCategory._hmf_once_v32.11417
- _logCategory._hmf_once_v364
- _logCategory._hmf_once_v45
- _logCategory._hmf_once_v5.7069
- _logCategory._hmf_once_v652
- _logCategory._hmf_once_v88
- _logCategory._hmf_once_v9.10943
CStrings:
+ "%{public}@Error: nil read for MeasurementUnit attribute for cluster %@, using min/max defaults"
+ "%{public}@Fetched specification number version data: %@"
+ "%{public}@Is in system commissioner mode and target fabric is nil, not setting storage"
+ "%{public}@MaxMeasuredValue %@ for %@ cluster"
+ "%{public}@MaxMeasuredValue attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@MeasurementUnit attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@MeasurementUnit type %@ for cluster %@ is not supported"
+ "%{public}@MinMeasuredValue %@ for %@ cluster"
+ "%{public}@MinMeasuredValue attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@No Matter device available to read specification version"
+ "%{public}@No attributes found for cluster %@ on endpoint %@. Use default MeasuredValue Min/Max %@, %@"
+ "%{public}@Updating software version number from %@ to %@"
+ "00000090-0000-1000-8000-0026BB765291"
+ "00000091-0000-1000-8000-0026BB765291"
+ "00000093-0000-1000-8000-0026BB765291"
+ "00000094-0000-1000-8000-0026BB765291"
+ "000000C3-0000-1000-8000-0026BB765291"
+ "000000C4-0000-1000-8000-0026BB765291"
+ "000000C6-0000-1000-8000-0026BB765291"
+ "000000C7-0000-1000-8000-0026BB765291"
+ "000000C8-0000-1000-8000-0026BB765291"
+ "HMMTRCluster"
+ "MTRClusterCarbonDioxideConcentrationMeasurement"
+ "MTRClusterCarbonMonoxideConcentrationMeasurement"
+ "MTRClusterNitrogenDioxideConcentrationMeasurement"
+ "MTRClusterOzoneConcentrationMeasurement"
+ "MTRClusterPM10ConcentrationMeasurement"
+ "MTRClusterPM25ConcentrationMeasurement"
+ "MTRClusterTotalVolatileOrganicCompoundsConcentrationMeasurement"
+ "MaxMeasuredValue"
+ "MeasurementUnit"
+ "MinMeasuredValue"
+ "_populateMeasuredValueAttributeForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:"
+ "getBaseClusterName:"
+ "readAttributeMaxMeasuredValueWithParams:"
+ "readAttributeMinMeasuredValueWithParams:"
+ "readAttributeSpecificationVersionWithParams:"
+ "readSpecificationVersionWithCompletionHandler:"
- "%{public}@An error occurred while trying to read Measured Value attribute"
- "%{public}@An error occurred while trying to read Measurement Unit attribute"
- "%{public}@An error occurred while trying to read Measurement Unit attribute. Cannot handle Measured Value attribute."
- "%{public}@An error occurred while trying to read Peak Measured Value attribute"
- "%{public}@Updating software version number from from %@ to %@"

```
