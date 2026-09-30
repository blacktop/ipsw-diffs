## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-2964.0.107.502.1
-  __TEXT.__text: 0x5200d4
+2964.0.137.0.0
+  __TEXT.__text: 0x519060
   __TEXT.__auth_stubs: 0x2d80
-  __TEXT.__objc_methlist: 0x30324
-  __TEXT.__const: 0x1ed8
+  __TEXT.__objc_methlist: 0x3022c
+  __TEXT.__const: 0x1ef8
   __TEXT.__swift5_typeref: 0x4ce
   __TEXT.__constg_swiftt: 0x364
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x51c
-  __TEXT.__cstring: 0x846f3
+  __TEXT.__cstring: 0x849d1
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x34
-  __TEXT.__oslogstring: 0x121d2
+  __TEXT.__oslogstring: 0x12599
   __TEXT.__swift5_capture: 0x4f4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__gcc_except_tab: 0x2d24
+  __TEXT.__gcc_except_tab: 0x2d50
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x81d8
+  __TEXT.__unwind_info: 0x8178
   __TEXT.__eh_frame: 0x10f0
-  __TEXT.__objc_classname: 0x2846
-  __TEXT.__objc_methname: 0x671a9
-  __TEXT.__objc_methtype: 0x8304
-  __TEXT.__objc_stubs: 0x35980
+  __TEXT.__objc_classname: 0x2837
+  __TEXT.__objc_methname: 0x66f42
+  __TEXT.__objc_methtype: 0x832b
+  __TEXT.__objc_stubs: 0x35780
   __DATA_CONST.__got: 0x1af0
-  __DATA_CONST.__const: 0xa6a8
-  __DATA_CONST.__objc_classlist: 0xa68
-  __DATA_CONST.__objc_nlclslist: 0x260
+  __DATA_CONST.__const: 0xa708
+  __DATA_CONST.__objc_classlist: 0xa60
+  __DATA_CONST.__objc_nlclslist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14fb0
+  __DATA_CONST.__objc_selrefs: 0x14f68
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb58
-  __DATA_CONST.__objc_arraydata: 0x15fd0
+  __DATA_CONST.__objc_superrefs: 0xb50
+  __DATA_CONST.__objc_arraydata: 0x15f60
   __AUTH_CONST.__auth_got: 0x16d8
-  __AUTH_CONST.__const: 0x24d8
-  __AUTH_CONST.__cfstring: 0x75120
-  __AUTH_CONST.__objc_const: 0x3a8f0
+  __AUTH_CONST.__const: 0x2418
+  __AUTH_CONST.__cfstring: 0x745c0
+  __AUTH_CONST.__objc_const: 0x3a7f0
   __AUTH_CONST.__objc_intobj: 0x7530
   __AUTH_CONST.__objc_arrayobj: 0x2d18
-  __AUTH_CONST.__objc_dictobj: 0x4ee8
-  __AUTH_CONST.__objc_doubleobj: 0x1470
-  __AUTH.__objc_data: 0x2cf8
+  __AUTH_CONST.__objc_dictobj: 0x4e70
+  __AUTH_CONST.__objc_doubleobj: 0x1430
+  __AUTH.__objc_data: 0x2c08
   __AUTH.__data: 0x760
-  __DATA.__objc_ivar: 0x1f18
+  __DATA.__objc_ivar: 0x1f14
   __DATA.__data: 0xef0
-  __DATA.__bss: 0x1ff8
-  __DATA.__common: 0x228
-  __DATA_DIRTY.__objc_ivar: 0x1724
-  __DATA_DIRTY.__objc_data: 0x3c98
+  __DATA.__common: 0x220
+  __DATA.__bss: 0x1ff0
+  __DATA_DIRTY.__objc_ivar: 0x1720
+  __DATA_DIRTY.__objc_data: 0x3d38
   __DATA_DIRTY.__data: 0x2a0
-  __DATA_DIRTY.__bss: 0x56c0
-  __DATA_DIRTY.__common: 0x90
+  __DATA_DIRTY.__bss: 0x56f8
+  __DATA_DIRTY.__common: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3077AE29-F736-3722-BCCF-20EE647D8F32
-  Functions: 20394
-  Symbols:   55077
-  CStrings:  52889
+  UUID: 4B3F1225-301E-3F31-B2D5-E8AF3498109B
+  Functions: 20381
+  Symbols:   55008
+  CStrings:  52716
 
Symbols:
+ -[PLBatteryAgent getIconChargeState:]
+ -[PLEnergyIssuesService currentUrsaCloudKitTask]
+ -[PLEnergyIssuesService executeUrsaClientCallWithBlock:]
+ -[PLEnergyIssuesService extractActionfromEntry:]
+ -[PLEnergyIssuesService extractProcessNameFromEntry:]
+ -[PLEnergyIssuesService handlePeriodicTableUpdateCallback:withRequestUUID:withPayload:forEntry:]
+ -[PLEnergyIssuesService isValidUrsaEntry:]
+ -[PLEnergyIssuesService processExistingEntriesSequentially]
+ -[PLEnergyIssuesService queryExistingUrsaEntries:]
+ -[PLEnergyIssuesService requestUrsaNotificationAndLog:]
+ -[PLEnergyIssuesService setCurrentUrsaCloudKitTask:]
+ -[PLEnergyIssuesService setUrsaClientQueue:]
+ -[PLEnergyIssuesService shouldUpdateTableFrom:newPayload:]
+ -[PLEnergyIssuesService updateExistingTableEntry:withResponsePayload:]
+ -[PLEnergyIssuesService ursaClientQueue]
+ -[PLPerformanceAgent logEventPointSystemMemory:]
+ -[PLRenderingAgent logEventForwardScrollPocket]
+ -[PLRenderingAgent scrollPocketListener]
+ -[PLRenderingAgent setScrollPocketListener:]
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table275
+ GCC_except_table282
+ GCC_except_table286
+ GCC_except_table32
+ GCC_except_table328
+ GCC_except_table33
+ GCC_except_table330
+ GCC_except_table334
+ GCC_except_table426
+ GCC_except_table440
+ _OBJC_CLASS_$_NSBlockOperation
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5102
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5111
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5120
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5147
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5168
+ ___27-[PLBBAgent modelGPSPower:]_block_invoke.5722
+ ___27-[PLBBAgent modelGPSPower:]_block_invoke.5728
+ ___27-[PLBBAgent modelGPSPower:]_block_invoke.5734
+ ___27-[PLBBAgent modelGPSPower:]_block_invoke.5740
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4831
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4837
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4846
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4858
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4864
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4867
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4873
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4876
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4879
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4885
+ ___27-[PLBBAgent modelMavPower:]_block_invoke.4894
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.4933
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.4939
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.4945
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5038
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5074
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5080
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5146
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5170
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5182
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5188
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5194
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5203
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5209
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5215
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5338
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5344
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5350
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5356
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5362
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5395
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5401
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5413
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5443
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5506
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5512
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5518
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5524
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5530
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5536
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5539
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5551
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5557
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5563
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5566
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5569
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5572
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5575
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5578
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5581
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5584
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5587
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5590
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5593
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5596
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5599
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5605
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5611
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5617
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5623
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5629
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5635
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5644
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5650
+ ___30-[PLBBAgent modelSinopePower:]_block_invoke.5656
+ ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4789
+ ___33-[PLBBAgent logTelephonyActivity]_block_invoke.5818
+ ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5181
+ ___34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke.603
+ ___37-[PLXPCAgent logEventForwardGMSOptIn]_block_invoke.2950
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1850
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1858
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1866
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1874
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1882
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1890
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1898
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1906
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1908
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1916
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1927
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1938
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1949
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1960
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1971
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1976
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1990
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1998
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2003
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2017
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2025
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2035
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2040
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2047
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2052
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2062
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2070
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2078
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2083
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2099
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2107
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2115
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2123
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2131
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2143
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2151
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2161
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2169
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2185
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2193
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2201
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2213
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2221
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2229
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2234
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2239
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2257
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2264
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2274
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2282
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2300
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2308
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2315
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2325
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2333
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2343
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2352
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2361
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2371
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2379
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2387
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2397
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2405
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2413
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2423
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2431
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2441
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2451
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2461
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2471
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2479
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2487
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2492
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2497
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2502
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2507
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2514
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2519
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2524
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2538
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2545
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2555
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2563
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2579
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2587
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2592
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2602
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2620
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2628
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2636
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2643
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2651
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2661
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2671
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2681
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2688
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2698
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2706
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2714
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2722
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2729
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2734
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2741
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2746
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2754
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2759
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2766
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2776
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2784
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2797
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2805
+ ___40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1609
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4177
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4184
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4180
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4187
+ ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.172
+ ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.178
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5332
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5340
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5334
+ ___42-[PLEnergyIssuesService addUrsaResponders]_block_invoke.265
+ ___42-[PLEnergyIssuesService addUrsaResponders]_block_invoke_5
+ ___42-[PLEnergyIssuesService addUrsaResponders]_block_invoke_6
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1723
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1728
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1735
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1740
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1750
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1760
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1765
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1772
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1777
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1784
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1794
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1801
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1808
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1818
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1826
+ ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.2016
+ ___43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.162
+ ___44-[PLRenderingAgent initOperatorDependancies]_block_invoke.57
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5369
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5370
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5371
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5372
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5373
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5374
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5415
+ ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.2064
+ ___46-[PLEnergyIssuesService handlePowerException:]_block_invoke_2
+ ___46-[PLEnergyIssuesService runPeriodic:withFlag:]_block_invoke_2
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5357
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5358
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5362
+ ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.2073
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5045
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5049
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5054
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5058
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5050
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5055
+ ___56-[PLEnergyIssuesService executeUrsaClientCallWithBlock:]_block_invoke
+ ___58-[PLEnergyIssuesService handlePowerExceptionNotification:]_block_invoke_2
+ ___59-[PLEnergyIssuesService processExistingEntriesSequentially]_block_invoke
+ ___59-[PLEnergyIssuesService processExistingEntriesSequentially]_block_invoke_2
+ ___60-[PLBBAgent telephonyActivityNotificationCB_Agent:withName:]_block_invoke.5800
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1732
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1739
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1744
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1750
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1761
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1762
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1763
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1773
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1777
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1782
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1786
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1811
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1812
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1745
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1757
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1778
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1805
+ ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4440
+ ___96-[PLEnergyIssuesService handlePeriodicTableUpdateCallback:withRequestUUID:withPayload:forEntry:]_block_invoke
+ ___BasebandResetCallback_block_invoke.6502
+ ___PowerChangedCallback_block_invoke.438
+ ___PowerChangedCallback_block_invoke.444
+ ___PowerChangedCallback_block_invoke.448
+ ___PowerChangedCallback_block_invoke.454
+ ___PowerChangedCallback_block_invoke.460
+ ___TelephonyActivityNotificationCB_block_invoke.6529
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e47_v32?0"NSError"8"NSString"16"NSDictionary"24ls32l8s40l8
+ ___block_descriptor_60_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r48r56r_e47_v32?0"NSError"8"NSString"16"NSDictionary"24lr40l8r48l8r56l8s32l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56r64r72r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8r72l8
+ ___block_literal_global.179
+ ___block_literal_global.1841
+ ___block_literal_global.1843
+ ___block_literal_global.1845
+ ___block_literal_global.1847
+ ___block_literal_global.1849
+ ___block_literal_global.1851
+ ___block_literal_global.1853
+ ___block_literal_global.1855
+ ___block_literal_global.1861
+ ___block_literal_global.189
+ ___block_literal_global.1911
+ ___block_literal_global.1913
+ ___block_literal_global.192
+ ___block_literal_global.1954
+ ___block_literal_global.2284
+ ___block_literal_global.2786
+ ___block_literal_global.299
+ ___block_literal_global.4492
+ ___block_literal_global.460
+ ___block_literal_global.4745
+ ___block_literal_global.4757
+ ___block_literal_global.4807
+ ___block_literal_global.523
+ ___block_literal_global.5306
+ ___block_literal_global.5367
+ ___block_literal_global.560
+ ___block_literal_global.562
+ ___block_literal_global.564
+ ___block_literal_global.566
+ ___block_literal_global.576
+ ___block_literal_global.579
+ ___block_literal_global.599
+ ___block_literal_global.840
+ ___fakeSleep_block_invoke.395
+ ___fakeSleep_block_invoke.407
+ ___fakeSleep_block_invoke.411
+ ___fakeSleep_block_invoke.417
+ _objc_msgSend$addOperation:
+ _objc_msgSend$blockOperationWithBlock:
+ _objc_msgSend$cancelAllOperations
+ _objc_msgSend$currentUrsaCloudKitTask
+ _objc_msgSend$executeUrsaClientCallWithBlock:
+ _objc_msgSend$extractActionfromEntry:
+ _objc_msgSend$extractProcessNameFromEntry:
+ _objc_msgSend$getIconChargeState:
+ _objc_msgSend$handlePeriodicTableUpdateCallback:withRequestUUID:withPayload:forEntry:
+ _objc_msgSend$hasLPW
+ _objc_msgSend$isValidUrsaEntry:
+ _objc_msgSend$logEventForwardScrollPocket
+ _objc_msgSend$logEventPointSystemMemory:
+ _objc_msgSend$processExistingEntriesSequentially
+ _objc_msgSend$queryExistingUrsaEntries:
+ _objc_msgSend$requestUrsaNotificationAndLog:
+ _objc_msgSend$scrollPocketListener
+ _objc_msgSend$setCurrentUrsaCloudKitTask:
+ _objc_msgSend$setMaxConcurrentOperationCount:
+ _objc_msgSend$setName:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setUrsaClientQueue:
+ _objc_msgSend$shouldUpdateTableFrom:newPayload:
+ _objc_msgSend$updateExistingTableEntry:withResponsePayload:
+ _objc_msgSend$ursaClientQueue
- +[PLIPSecAgent entryEventPointDefinitionIPSecWake]
- +[PLIPSecAgent entryEventPointDefinitions]
- +[PLIPSecAgent load]
- +[PLSMCAgent entryEventBackwardDefinitionAccumulatedKeys]
- +[PLSMCAgent entryEventBackwardDefinitionDisplayPowerKeys]
- +[PLSMCAgent entryEventBackwardDefinitionPowerAccumulatedKeys]
- +[PLSMCAgent entryEventPointDefinitionThermalInstantKeys]
- +[PLSMCAgent entryEventPointDefinitionThermalKeys]
- +[PLSMCAgent shouldModelDisplayPowerFromSMC]
- +[PLXPCAgent entryEventBackwardDefinitionCKKSSyncing]
- +[PLXPCAgent entryEventBackwardDefinitionUbiquityAccountStatistics]
- +[PLXPCAgent entryEventPointDefinitionCKKSSyncingRateLimit]
- +[PLXPCAgent entryEventPointDefinitionDeepScanReasons]
- +[PLXPCAgent entryEventPointDefinitionOctagonTrust]
- -[PLEnergyIssuesService requestUrsaNotification:]
- -[PLIPSecAgent initIPSecKEvent]
- -[PLIPSecAgent initOperatorDependancies]
- -[PLIPSecAgent ipsecSocket]
- -[PLIPSecAgent logEventPointIPSecWake]
- -[PLIPSecAgent setIpsecSocket:]
- -[PLPerformanceAgent logEventPointSystemMemory]
- -[PLSMCAgent accumulatedKeys]
- -[PLSMCAgent displayAccumulatedKeys]
- -[PLSMCAgent logDisplayPower]
- -[PLSMCAgent logEventPointThermalKeys]
- -[PLSMCAgent thermalInstantKeys]
- -[PLSMCAgent thermalKeys]
- -[PLXPCAgent CKKSSyncingEventXPCListener]
- -[PLXPCAgent DeepScanReasonsXPCListener]
- -[PLXPCAgent OctagonTrustEventXPCListener]
- -[PLXPCAgent UbiquityAccountStatisticsXPCListener]
- -[PLXPCAgent handleCKKSSyncingEvent:]
- -[PLXPCAgent logEventBackwardUbiquityAccountStatistics:]
- -[PLXPCAgent logEventPointDeepScanReasons:]
- -[PLXPCAgent logEventPointOctagonTrustEvent:]
- -[PLXPCAgent setCKKSSyncingEventXPCListener:]
- -[PLXPCAgent setDeepScanReasonsXPCListener:]
- -[PLXPCAgent setOctagonTrustEventXPCListener:]
- -[PLXPCAgent setUbiquityAccountStatisticsXPCListener:]
- GCC_except_table266
- GCC_except_table268
- GCC_except_table273
- GCC_except_table285
- GCC_except_table30
- GCC_except_table327
- GCC_except_table329
- GCC_except_table333
- GCC_except_table439
- GCC_except_table47
- GCC_except_table53
- _OBJC_CLASS_$_PLIPSecAgent
- _OBJC_IVAR_$_PLIPSecAgent._ipsecSocket
- _OBJC_METACLASS_$_PLIPSecAgent
- _PLLogIPSec
- __OBJC_$_CLASS_METHODS_PLIPSecAgent
- __OBJC_$_INSTANCE_METHODS_PLIPSecAgent
- __OBJC_$_INSTANCE_VARIABLES_PLIPSecAgent
- __OBJC_$_PROP_LIST_PLIPSecAgent
- __OBJC_CLASS_RO_$_PLIPSecAgent
- __OBJC_METACLASS_RO_$_PLIPSecAgent
- ___24-[PLBatteryAgent xFlags]_block_invoke.5096
- ___24-[PLBatteryAgent xFlags]_block_invoke.5105
- ___24-[PLBatteryAgent xFlags]_block_invoke.5114
- ___24-[PLBatteryAgent xFlags]_block_invoke.5123
- ___24-[PLBatteryAgent xFlags]_block_invoke.5150
- ___25-[PLSMCAgent thermalKeys]_block_invoke
- ___27-[PLBBAgent modelGPSPower:]_block_invoke.5620
- ___27-[PLBBAgent modelGPSPower:]_block_invoke.5626
- ___27-[PLBBAgent modelGPSPower:]_block_invoke.5632
- ___27-[PLBBAgent modelGPSPower:]_block_invoke.5638
- ___27-[PLBBAgent modelMavPower:]_block_invoke.4795
- ___27-[PLBBAgent modelMavPower:]_block_invoke.4801
- ___27-[PLBBAgent modelMavPower:]_block_invoke.4807
- ___27-[PLBBAgent modelMavPower:]_block_invoke.4813
- ___27-[PLBBAgent modelMavPower:]_block_invoke.4855
- ___27-[PLBBAgent modelMavPower:]_block_invoke.4861
- ___27-[PLBBAgent modelMavPower:]_block_invoke.4870
- ___29-[PLSMCAgent accumulatedKeys]_block_invoke
- ___29-[PLSMCAgent logDisplayPower]_block_invoke
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.4909
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.4915
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.4921
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.4936
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.4942
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.4954
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.4972
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5068
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5104
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5110
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5173
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5179
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5185
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5200
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5206
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5212
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5218
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5224
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5335
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5341
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5347
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5353
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5359
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5392
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5404
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5410
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5416
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5422
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5428
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5434
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5452
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5464
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5470
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5476
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5482
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5488
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5497
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5503
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5515
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5542
- ___30-[PLBBAgent modelSinopePower:]_block_invoke.5548
- ___31-[PLIPSecAgent initIPSecKEvent]_block_invoke
- ___31-[PLIPSecAgent initIPSecKEvent]_block_invoke.29
- ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4783
- ___32-[PLSMCAgent thermalInstantKeys]_block_invoke
- ___33-[PLBBAgent logTelephonyActivity]_block_invoke.5716
- ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5175
- ___34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke.920
- ___36-[PLSMCAgent displayAccumulatedKeys]_block_invoke
- ___37-[PLXPCAgent logEventForwardGMSOptIn]_block_invoke.3020
- ___38-[PLSMCAgent initOperatorDependancies]_block_invoke
- ___38-[PLSMCAgent initOperatorDependancies]_block_invoke_2
- ___38-[PLSMCAgent initOperatorDependancies]_block_invoke_3
- ___38-[PLSMCAgent initOperatorDependancies]_block_invoke_4
- ___38-[PLSMCAgent initOperatorDependancies]_block_invoke_5
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1889
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1897
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1905
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1913
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1921
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1929
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1937
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1945
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1947
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1955
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1966
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1977
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1988
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1999
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2015
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2029
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2037
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2042
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2049
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2056
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2064
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2074
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2079
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2086
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2101
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2109
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2117
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2122
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2130
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2146
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2154
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2162
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2170
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2182
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2190
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2200
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2216
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2224
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2232
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2240
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2252
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2260
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2268
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2273
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2278
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2286
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2296
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2303
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2313
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2321
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2339
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2347
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2354
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2364
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2374
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2382
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2392
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2401
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2410
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2420
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2428
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2436
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2446
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2454
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2462
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2472
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2480
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2490
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2500
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2510
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2518
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2528
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2536
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2544
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2549
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2554
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2559
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2564
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2576
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2581
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2586
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2591
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2605
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2622
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2630
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2638
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2646
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2654
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2659
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2669
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2679
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2687
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2695
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2703
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2710
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2718
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2728
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2738
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2748
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2755
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2765
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2773
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2781
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2789
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2801
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2808
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2813
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2821
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2826
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2833
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2843
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2851
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2863
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2864
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2872
- ___40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1612
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4183
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4190
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4186
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4193
- ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.721
- ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.727
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5326
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5334
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5328
- ___42-[PLEnergyIssuesService addUrsaResponders]_block_invoke.261
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1762
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1767
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1774
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1779
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1799
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1804
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1811
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1816
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1823
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1828
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1840
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1847
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1857
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1865
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1872
- ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.2019
- ___43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.711
- ___44+[PLSMCAgent shouldModelDisplayPowerFromSMC]_block_invoke
- ___45-[PLBBSleepWakeMsg logEventPointSleepWakeABM]_block_invoke.195
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5362
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5363
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5364
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5365
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5366
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5367
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5409
- ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.2067
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5351
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5352
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5356
- ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.2076
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5039
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5043
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5048
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5052
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5044
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5049
- ___60-[PLBBAgent telephonyActivityNotificationCB_Agent:withName:]_block_invoke.5698
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1735
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1742
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1747
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1753
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1767
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1768
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1769
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1776
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1780
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1785
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1789
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1814
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1815
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1748
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1760
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1781
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1808
- ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4446
- ___BasebandResetCallback_block_invoke.6400
- ___PLLogIPSec_block_invoke
- ___PowerChangedCallback_block_invoke.437
- ___PowerChangedCallback_block_invoke.443
- ___PowerChangedCallback_block_invoke.447
- ___PowerChangedCallback_block_invoke.453
- ___PowerChangedCallback_block_invoke.459
- ___TelephonyActivityNotificationCB_block_invoke.6427
- ___block_descriptor_56_e8_32r40r48r_e47_v32?0"NSError"8"NSString"16"NSDictionary"24lr32l8r40l8r48l8
- ___block_literal_global.176
- ___block_literal_global.1844
- ___block_literal_global.1846
- ___block_literal_global.1848
- ___block_literal_global.1850
- ___block_literal_global.1852
- ___block_literal_global.1854
- ___block_literal_global.1856
- ___block_literal_global.1858
- ___block_literal_global.1864
- ___block_literal_global.1914
- ___block_literal_global.1916
- ___block_literal_global.1957
- ___block_literal_global.2323
- ___block_literal_global.2853
- ___block_literal_global.436
- ___block_literal_global.4495
- ___block_literal_global.4739
- ___block_literal_global.4751
- ___block_literal_global.4801
- ___block_literal_global.499
- ___block_literal_global.5300
- ___block_literal_global.5361
- ___block_literal_global.741
- ___block_literal_global.852
- ___block_literal_global.854
- ___block_literal_global.855
- ___block_literal_global.856
- ___block_literal_global.858
- ___block_literal_global.860
- ___block_literal_global.862
- ___block_literal_global.883
- ___block_literal_global.885
- ___block_literal_global.887
- ___block_literal_global.889
- ___block_literal_global.891
- ___block_literal_global.894
- ___block_literal_global.896
- ___block_literal_global.916
- ___fakeSleep_block_invoke.394
- ___fakeSleep_block_invoke.406
- ___fakeSleep_block_invoke.410
- ___fakeSleep_block_invoke.416
- _initIPSecKEvent.ipsecSrc
- _kIPDst
- _kIPDstPort
- _kIPProtocol
- _kIPSrc
- _kIPSrcPort
- _kIPVersion
- _kPLSMCAgentEventBackwardAccumulatedKeys
- _kPLSMCAgentEventBackwardDisplayPowerKeys
- _kPLSMCAgentEventBackwardPowerAccumulatedKeys
- _kPLSMCAgentEventPointThermalInstantKeys
- _kPLSMCAgentEventPointThermalKeys
- _kPLXPCAgentEventBackwardNameCKKSSyncing
- _kPLXPCAgentEventBackwardNameUbiquityAccountStatistics
- _kPLXPCAgentEventPointNameCKKSSyncingRateLimit
- _kPLXPCAgentEventPointNameDeepScanReasons
- _kPLXPCAgentEventPointNameOctagonTrust
- _kProcessId
- _kProcessName
- _objc_msgSend$bbWakeDataBin
- _objc_msgSend$displayAccumulatedKeys
- _objc_msgSend$entryEventBackwardDefinitionAccumulatedKeys
- _objc_msgSend$entryEventBackwardDefinitionCKKSSyncing
- _objc_msgSend$entryEventBackwardDefinitionDisplayPowerKeys
- _objc_msgSend$entryEventBackwardDefinitionPowerAccumulatedKeys
- _objc_msgSend$entryEventBackwardDefinitionUbiquityAccountStatistics
- _objc_msgSend$entryEventPointDefinitionCKKSSyncingRateLimit
- _objc_msgSend$entryEventPointDefinitionDeepScanReasons
- _objc_msgSend$entryEventPointDefinitionIPSecWake
- _objc_msgSend$entryEventPointDefinitionOctagonTrust
- _objc_msgSend$entryEventPointDefinitionThermalInstantKeys
- _objc_msgSend$entryEventPointDefinitionThermalKeys
- _objc_msgSend$getAccumEntryFromSample:lastSample:withEntryKey:withDate:
- _objc_msgSend$getPowerEntryFromSample:lastSample:withEntryKey:
- _objc_msgSend$handleCKKSSyncingEvent:
- _objc_msgSend$handleIPSecEvent:
- _objc_msgSend$handleStateChangeForSMCStats
- _objc_msgSend$initIPSecKEvent
- _objc_msgSend$ipsecSocket
- _objc_msgSend$lastPowerAccumlatedSample
- _objc_msgSend$lastThermalInstantEntry
- _objc_msgSend$logEventBackwardUbiquityAccountStatistics:
- _objc_msgSend$logEventPointDeepScanReasons:
- _objc_msgSend$logEventPointIPSecWake
- _objc_msgSend$logEventPointOctagonTrustEvent:
- _objc_msgSend$logEventPointSystemMemory
- _objc_msgSend$logThermalAggregationKeysToCA
- _objc_msgSend$parseThermalThresholds:thermalPressure:virtualTemp:thermalLevel:
- _objc_msgSend$requestUrsaNotification:
- _objc_msgSend$setCKKSSyncingEventXPCListener:
- _objc_msgSend$setDeepScanReasonsXPCListener:
- _objc_msgSend$setLastPowerAccumlatedSample:
- _objc_msgSend$setOctagonTrustEventXPCListener:
- _objc_msgSend$setThermalAggregationTimer:
- _objc_msgSend$setThermalMonitorTimer:
- _objc_msgSend$setUbiquityAccountStatisticsXPCListener:
- _objc_msgSend$thermalAggregationTimer
- _objc_msgSend$thermalInstantKeys
- _objc_msgSend$thermalKeys
- _objc_msgSend$thermalMonitorTimer
CStrings:
+ "%@ >= %@ AND INSTR(%@, ':') > 0"
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@24@0:8^{IOReportGroupChecks=BBBBBB}16"
+ "@SIM 1: RX TX duration over flows the total window of %f: %f + %f + %f + %f"
+ "ASPFTLParseBufferToCxt: nandReadsByMode(1463): (#6) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: nandReadsByMode(1463): Cannot add 6 elements to context"
+ "ASPFTLParseBufferToCxt: nandWritesByMode(1462): (#6) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: nandWritesByMode(1462): Cannot add 6 elements to context"
+ "Adjusted DLTBSz[primary][%d]=%f"
+ "Adjusted DLTBSz[secondary][%d]=%f"
+ "Adjusted activatedCASCC[PRIMARY_SIM][%d]=%d"
+ "Adjusted activatedCASCC[SECONDARY_SIM][%d]=%d"
+ "Adjusted configuredCASCC[PRIMARY_SIM][%d]=%d"
+ "Adjusted configuredCASCC[SECONDARY_SIM][%d]=%d"
+ "Adjusted nrsub6DLTBSz[primary][%d]=%f"
+ "Adjusted nrsub6DLTBSz[secondary][%d]=%f"
+ "Adjusted nrsub6RxTxActivity2[%d]: %f"
+ "Adjusted nrsub6RxTxActivity[%d]: %f"
+ "BackdropGroup"
+ "Callback for %@ - error:%@ payload:%@"
+ "Charging Completed Limited"
+ "Dynamic"
+ "Entry failed with error: %@"
+ "Entry is nil"
+ "Found %lu existing entries for update"
+ "GPU Stats,GPU Power Controller States"
+ "Hard"
+ "In full-mode. Configuring TG Stats"
+ "Invalid PLEntry. Skipping update for %@"
+ "Other"
+ "Running periodic with table update since %.2f %@"
+ "SELECT * FROM %@ p1 WHERE %@ AND %@ = (%@) ORDER BY %@ DESC;"
+ "SELECT MAX(%@) FROM %@ p2 WHERE %@ "
+ "SIM 0: RX TX duration over flows the total window of %f: %f + %f + %f + %f"
+ "SIM 2: RX TX duration over flows the total window of %f: %f + %f + %f + %f"
+ "SINOPE_HW_HIST_LTE_DL_TBS: lteTbsDuration=%f"
+ "SINOPE_HW_HIST_NR_SUB6_DL_TBS: nrTbsDuration=%f"
+ "SUBSTR(p1.%@, INSTR(p1.%@, ':') + 1) = SUBSTR(p2.%@, INSTR(p2.%@, ':') + 1)"
+ "Scroll Pocket payload: %@"
+ "Scroll Pocket stats Unavailable"
+ "Scroll Pocket stats notification received"
+ "Scroll Pocket stats: %llu"
+ "ScrollPocket"
+ "Sim 0: Total of CAActive bins %f or CAConfig bins %f greater than expected duration %f"
+ "Sim 0: Total of LTE TBS bins %f greater than expected duration %f"
+ "Sim 0: Total of NR TBS bins %f greater than expected duration %f"
+ "Sim 1: Total of CAActive bins %f or CAConfig bins %f greater than expected duration %f"
+ "Sim 1: Total of LTE TBS bins %f greater than expected duration %f"
+ "Sim 1: Total of NR TBS bins %f greater than expected duration %f"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,V_currentUrsaCloudKitTask"
+ "T@\"NSOperationQueue\",&,V_ursaClientQueue"
+ "T@\"PLCFNotificationOperatorComposition\",&,V_scrollPocketListener"
+ "Total"
+ "Updated table entry for %@ with new entry %@"
+ "_currentUrsaCloudKitTask"
+ "_scrollPocketListener"
+ "_ursaClientQueue"
+ "addOperation:"
+ "blockOperationWithBlock:"
+ "boot_rd_sdl_overflow"
+ "boot_wr_sdl_overflow"
+ "cancelAllOperations"
+ "coge_cache_hit_program"
+ "coge_cache_hit_read"
+ "coge_cache_miss_program"
+ "coge_cache_miss_read"
+ "coge_lru_num_of_replacement"
+ "coge_lru_num_of_searches"
+ "com.apple.UIKit.ScrollPocketStatistics"
+ "com.apple.powerlog.ursaClient"
+ "current state is : %u"
+ "currentUrsaCloudKitTask"
+ "driMessage empty or missing ':'"
+ "driMessage format invalid, expected 'action:process' got '%@'"
+ "driMessage missing or not a string"
+ "dspExceptionParameter152"
+ "dspExceptionParameter153"
+ "dspExceptionParameter154"
+ "dspExceptionParameter155"
+ "dspExceptionParameter156"
+ "dspExceptionParameter157"
+ "dspExceptionParameter169"
+ "executeUrsaClientCallWithBlock:"
+ "extractActionfromEntry:"
+ "extractProcessNameFromEntry:"
+ "fixedInBuild present but not NSString"
+ "getIconChargeState:"
+ "handlePeriodicTableUpdateCallback:withRequestUUID:withPayload:forEntry:"
+ "handling callback for %@"
+ "hasLPW"
+ "hitInBuild is empty string"
+ "hitInBuild missing or not a string"
+ "impact present but not NSNumber"
+ "isValidUrsaEntry:"
+ "logEventForwardScrollPocket"
+ "logEventPointSystemMemory:"
+ "msp_number_hw_sram_flips"
+ "nandReadsByMode_"
+ "nandStageOfLife105"
+ "nandStageOfLife106"
+ "nandStageOfLife111"
+ "nandStageOfLife112"
+ "nandStageOfLife113"
+ "nandStageOfLife114"
+ "nandStageOfLife115"
+ "nandStageOfLife116"
+ "nandStageOfLife117"
+ "nandStageOfLife118"
+ "nandStageOfLife119"
+ "nandWritesByMode_"
+ "periodic_rd_sdl_overflow"
+ "periodic_rd_training_failure"
+ "periodic_wr_sdl_overflow"
+ "periodic_wr_training_failure"
+ "pge_rd_sdl_overflow"
+ "pge_rd_training_failure"
+ "pge_wr_sdl_overflow"
+ "pge_wr_training_failure"
+ "processExistingEntriesSequentially"
+ "queryExistingUrsaEntries:"
+ "radar present but not NSNumber"
+ "readStage111"
+ "requestUrsaNotificationAndLog:"
+ "scrollPocketListener"
+ "setCurrentUrsaCloudKitTask:"
+ "setMaxConcurrentOperationCount:"
+ "setName:"
+ "setQualityOfService:"
+ "setScrollPocketListener:"
+ "setUrsaClientQueue:"
+ "shouldUpdateTableFrom:newPayload:"
+ "softwareUpdate"
+ "throttlingSecPerTTPerMW"
+ "timestampEnd missing"
+ "timestampEnd not NSDate or NSNumber"
+ "too_frequent_temp_change_rd"
+ "too_frequent_temp_change_wr"
+ "updateExistingTableEntry:withResponsePayload:"
+ "ursaClientQueue"
+ "{IOReportGroupChecks=BBBBBB}16@0:8"
- " pidAndProcessName=%@"
- "@24@0:8^{IOReportGroupChecks=BBBB}16"
- "AccumulatedKeys"
- "Adjusted SINOPE_HW_HIST_LTE_DL_TBS: DLTBSz[primary][%d]=%f"
- "Adjusted SINOPE_HW_HIST_LTE_DL_TBS: DLTBSz[secondary][%d]=%f"
- "AppLibraryID"
- "CKKSSyncing"
- "CKKSSyncing Callback: %@"
- "CKKSSyncingEventXPCListener"
- "CKKSSyncingRateLimit"
- "CKRQ"
- "Deep Scan Reasons callback: %@"
- "DeepScanReasons"
- "DeepScanReasonsXPCListener"
- "Dictionary for IPSec : %@"
- "DisplayPowerKeys"
- "DisplayStateExtended"
- "EnableLegacySMC"
- "EnergyAccounting"
- "EnergyMetrics"
- "F0Ac"
- "F0Tg"
- "F1Ac"
- "F1Tg"
- "FPDc"
- "Failed to log, invalid SMC connection"
- "ICMP"
- "IPSec"
- "IPSecWake"
- "IpDst"
- "IpDstPort"
- "IpProto"
- "IpSrc"
- "IpSrcPort"
- "IpVer"
- "Logging Thermal Instant entry: %@"
- "MSAc"
- "MSAg"
- "MSAi"
- "OctagonTrust"
- "OctagonTrust callback: %@"
- "OctagonTrustEventXPCListener"
- "PAPC"
- "PBLR"
- "PC0R"
- "PCAC"
- "PCIC"
- "PCPC"
- "PCPG"
- "PCPT"
- "PCTC"
- "PG0C"
- "PG0R"
- "PH0C"
- "PH0R"
- "PH1C"
- "PH1R"
- "PLDC"
- "PLIPSecAgent"
- "PM0C"
- "PM1C"
- "PMCC"
- "PO3R"
- "PO5R"
- "POLR"
- "PORR"
- "PPBR"
- "PS1C"
- "PSLC"
- "PW3C"
- "PowerAccumulatedKeys"
- "Running periodic since %.2f %@"
- "SDTL"
- "SDTO_"
- "SDTh"
- "SDTo"
- "SINOPE_HW_HIST_LTE_DL_TBS: tbsDuration=%f"
- "T@\"PLXPCListenerOperatorComposition\",&,V_CKKSSyncingEventXPCListener"
- "T@\"PLXPCListenerOperatorComposition\",&,V_DeepScanReasonsXPCListener"
- "T@\"PLXPCListenerOperatorComposition\",&,V_OctagonTrustEventXPCListener"
- "T@\"PLXPCListenerOperatorComposition\",&,V_UbiquityAccountStatisticsXPCListener"
- "TA0V"
- "TB1T"
- "TB2T"
- "TBXT"
- "TC0F"
- "TC0P"
- "TCMc"
- "TCXC"
- "TG0D"
- "TG0F"
- "TG0P"
- "TG1D"
- "TG1F"
- "TH0B"
- "TH0C"
- "TH0F"
- "TH0J"
- "TH0x"
- "TKBV"
- "TM0P"
- "TM0S"
- "TM0V"
- "TPMV"
- "Ta0P"
- "Th0N"
- "Th1H"
- "Th2H"
- "ThermalInstantKeys"
- "ThermalKeys"
- "Ti,N,V_ipsecSocket"
- "Ts0S"
- "Ts1S"
- "Ubiquity Account Statistics callback: %@"
- "UbiquityAccountStatistics"
- "UbiquityAccountStatisticsXPCListener"
- "_CKKSSyncingEventXPCListener"
- "_DeepScanReasonsXPCListener"
- "_OctagonTrustEventXPCListener"
- "_UbiquityAccountStatisticsXPCListener"
- "_ipsecSocket"
- "accessgroup"
- "accountStatistic"
- "accumulatedKeys"
- "boot_rd_sdl_overflow_"
- "boot_wr_sdl_overflow_"
- "cmSM"
- "coge_cache_hit_program_"
- "coge_cache_hit_read_"
- "coge_cache_miss_program_"
- "coge_cache_miss_read_"
- "coge_lru_num_of_replacement_"
- "coge_lru_num_of_searches_"
- "decodedPacket is empty"
- "deepScanReasons"
- "displayAccumulatedKeys"
- "dspExceptionParameter152_"
- "dspExceptionParameter153_"
- "dspExceptionParameter154_"
- "dspExceptionParameter155_"
- "dspExceptionParameter156_"
- "dspExceptionParameter157_"
- "dspExceptionParameter169_"
- "entryEventBackwardDefinitionAccumulatedKeys"
- "entryEventBackwardDefinitionCKKSSyncing"
- "entryEventBackwardDefinitionDisplayPowerKeys"
- "entryEventBackwardDefinitionPowerAccumulatedKeys"
- "entryEventBackwardDefinitionUbiquityAccountStatistics"
- "entryEventPointDefinitionCKKSSyncingRateLimit"
- "entryEventPointDefinitionDeepScanReasons"
- "entryEventPointDefinitionIPSecWake"
- "entryEventPointDefinitionOctagonTrust"
- "entryEventPointDefinitionThermalInstantKeys"
- "entryEventPointDefinitionThermalKeys"
- "got ipsec event!!!!"
- "handleCKKSSyncingEvent:"
- "handleIPSecEvent:"
- "headerInfo"
- "headerInfo not present"
- "initIPSecKEvent"
- "ipsec cancel event!!!!"
- "ipsec socket number %d"
- "ipsecSocket"
- "ipsecsrc is invalid"
- "items"
- "kKeyIPProtocol"
- "kKeyIPVersion"
- "logEventBackwardUbiquityAccountStatistics:"
- "logEventPointDeepScanReasons:"
- "logEventPointIPSecWake"
- "logEventPointOctagonTrustEvent:"
- "logEventPointSystemMemory"
- "logEventPointThermalKeys"
- "mTLL"
- "mlCC"
- "mlNN"
- "msp_number_hw_sram_flips_"
- "nandStageOfLife105_"
- "nandStageOfLife106_"
- "nandStageOfLife111_"
- "nandStageOfLife112_"
- "nandStageOfLife113_"
- "nandStageOfLife114_"
- "nandStageOfLife115_"
- "nandStageOfLife116_"
- "nandStageOfLife117_"
- "nandStageOfLife118_"
- "nandStageOfLife119_"
- "packet dictionary %@"
- "periodic_rd_sdl_overflow_"
- "periodic_rd_training_failure_"
- "periodic_wr_sdl_overflow_"
- "periodic_wr_training_failure_"
- "pge_rd_sdl_overflow_"
- "pge_rd_training_failure_"
- "pge_wr_sdl_overflow_"
- "pge_wr_training_failure_"
- "ratelimit"
- "readStage111_"
- "requestUrsaNotification:"
- "setCKKSSyncingEventXPCListener:"
- "setDeepScanReasonsXPCListener:"
- "setIpsecSocket:"
- "setOctagonTrustEventXPCListener:"
- "setUbiquityAccountStatisticsXPCListener:"
- "thermalInstantKeys"
- "thermalKeys"
- "too_frequent_temp_change_rd_"
- "too_frequent_temp_change_wr_"
- "totalNumberOfDirectories"
- "totalNumberOfDocuments"
- "totalNumberOfFaults"
- "totalNumberOfItems"
- "voBB"
- "voC0"
- "voR1"
- "voR2"
- "voS0"
- "voT0"
- "xPAr"
- "xPDs"
- "xPNf"
- "xPPT"
- "xPSp"
- "xPWi"
- "xPb1"
- "xPb2"
- "{IOReportGroupChecks=BBBB}16@0:8"

```
