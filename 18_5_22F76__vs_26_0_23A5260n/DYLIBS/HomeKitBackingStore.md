## HomeKitBackingStore

> `/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore`

```diff

-1278.6.31.1.1
-  __TEXT.__text: 0x88c40
+1323.0.6.0.1
+  __TEXT.__text: 0x88c90
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_methlist: 0x54f4
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x5280
-  __TEXT.__cstring: 0x7382
-  __TEXT.__oslogstring: 0xd1da
+  __TEXT.__cstring: 0x735e
+  __TEXT.__oslogstring: 0xd20c
   __TEXT.__unwind_info: 0x1e38
   __TEXT.__objc_classname: 0xeed
-  __TEXT.__objc_methname: 0xd0a2
+  __TEXT.__objc_methname: 0xd0da
   __TEXT.__objc_methtype: 0x197d
-  __TEXT.__objc_stubs: 0x9aa0
+  __TEXT.__objc_stubs: 0x9ac0
   __DATA_CONST.__got: 0x590
   __DATA_CONST.__const: 0x29b8
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2cf8
+  __DATA_CONST.__objc_selrefs: 0x2d00
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0xd0
+  __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x46a0
+  __AUTH_CONST.__cfstring: 0x4600
   __AUTH_CONST.__objc_const: 0xadd0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 80C95BD3-6F24-32ED-A380-1423C04223BA
+  UUID: 0618CF99-F894-3CDA-B61F-0E9E72981DA0
   Functions: 2146
-  Symbols:   7927
-  CStrings:  4696
+  Symbols:   7928
+  CStrings:  4687
 
Symbols:
+ -[HMBCloudDatabase initWithLocalDatabase:configuration:error:]
+ -[HMBLocalDatabase initWithDatastorePath:configuration:error:]
+ ___44-[HMBCloudZone _startUpWithPublicLocalZone:]_block_invoke.63
+ ___44-[HMBCloudZone _startUpWithPublicLocalZone:]_block_invoke.64
+ ___45-[HMBCloudZone _startUpWithPrivateLocalZone:]_block_invoke.55
+ ___45-[HMBCloudZone _startUpWithPrivateLocalZone:]_block_invoke.56
+ ___45-[HMBCloudZone _startUpWithPrivateLocalZone:]_block_invoke.57
+ ___Block_byref_object_copy_.1738
+ ___Block_byref_object_copy_.1811
+ ___Block_byref_object_copy_.1955
+ ___Block_byref_object_copy_.2209
+ ___Block_byref_object_copy_.2585
+ ___Block_byref_object_copy_.3414
+ ___Block_byref_object_copy_.3984
+ ___Block_byref_object_copy_.4545
+ ___Block_byref_object_copy_.5196
+ ___Block_byref_object_copy_.5411
+ ___Block_byref_object_copy_.5636
+ ___Block_byref_object_copy_.5757
+ ___Block_byref_object_copy_.6304
+ ___Block_byref_object_copy_.6423
+ ___Block_byref_object_copy_.6503
+ ___Block_byref_object_copy_.6713
+ ___Block_byref_object_copy_.7343
+ ___Block_byref_object_copy_.7523
+ ___Block_byref_object_copy_.7740
+ ___Block_byref_object_dispose_.1739
+ ___Block_byref_object_dispose_.1812
+ ___Block_byref_object_dispose_.1956
+ ___Block_byref_object_dispose_.2210
+ ___Block_byref_object_dispose_.2586
+ ___Block_byref_object_dispose_.3415
+ ___Block_byref_object_dispose_.3985
+ ___Block_byref_object_dispose_.4546
+ ___Block_byref_object_dispose_.5197
+ ___Block_byref_object_dispose_.5412
+ ___Block_byref_object_dispose_.5637
+ ___Block_byref_object_dispose_.5758
+ ___Block_byref_object_dispose_.6305
+ ___Block_byref_object_dispose_.6424
+ ___Block_byref_object_dispose_.6504
+ ___Block_byref_object_dispose_.6714
+ ___Block_byref_object_dispose_.7344
+ ___Block_byref_object_dispose_.7524
+ ___Block_byref_object_dispose_.7741
+ _____fetchNextBatch_block_invoke.5199
+ _____fetchNextBatch_block_invoke_2.5202
+ ___block_descriptor_32_e21_"HMFTimer"20?0d8I16l
+ ___block_literal_global.12.2976
+ ___block_literal_global.12.6243
+ ___block_literal_global.1287
+ ___block_literal_global.1527
+ ___block_literal_global.2040
+ ___block_literal_global.2112
+ ___block_literal_global.2203
+ ___block_literal_global.2330
+ ___block_literal_global.2682
+ ___block_literal_global.2856
+ ___block_literal_global.2983
+ ___block_literal_global.3063
+ ___block_literal_global.3257
+ ___block_literal_global.33.5142
+ ___block_literal_global.3432
+ ___block_literal_global.3759
+ ___block_literal_global.3873
+ ___block_literal_global.4093
+ ___block_literal_global.4172
+ ___block_literal_global.5108
+ ___block_literal_global.5867
+ ___block_literal_global.6005
+ ___block_literal_global.6251
+ ___block_literal_global.6333
+ ___block_literal_global.6425
+ ___block_literal_global.6635
+ ___block_literal_global.6717
+ ___block_literal_global.6927
+ ___block_literal_global.7263
+ ___block_literal_global.7346
+ ___block_literal_global.7541
+ ___block_literal_global.8147
+ ___block_literal_global.8288
+ ___block_literal_global.974
+ _hmbProperties._properties.2984
+ _hmbProperties._properties.3258
+ _hmbProperties._properties.6334
+ _hmbProperties._properties.7756
+ _hmbProperties.onceToken.2982
+ _hmbProperties.onceToken.3256
+ _hmbProperties.onceToken.6332
+ _hmbProperties.onceToken.7755
+ _logCategory._hmf_once_t0.4092
+ _logCategory._hmf_once_t101
+ _logCategory._hmf_once_t20.3449
+ _logCategory._hmf_once_t7.6634
+ _logCategory._hmf_once_v1.4094
+ _logCategory._hmf_once_v102
+ _logCategory._hmf_once_v21.3450
+ _logCategory._hmf_once_v8.6636
+ _objc_msgSend$hmf_enumerateWithAutoreleasePoolUsingBlock:
- -[HMBCloudDatabase initWithLocalDatabase:configuration:]
- -[HMBLocalDatabase initWithDatastorePath:configuration:]
- ___44-[HMBCloudZone _startUpWithPublicLocalZone:]_block_invoke.78
- ___44-[HMBCloudZone _startUpWithPublicLocalZone:]_block_invoke.79
- ___45-[HMBCloudZone _startUpWithPrivateLocalZone:]_block_invoke.70
- ___45-[HMBCloudZone _startUpWithPrivateLocalZone:]_block_invoke.71
- ___45-[HMBCloudZone _startUpWithPrivateLocalZone:]_block_invoke.72
- ___Block_byref_object_copy_.1717
- ___Block_byref_object_copy_.1789
- ___Block_byref_object_copy_.1923
- ___Block_byref_object_copy_.2185
- ___Block_byref_object_copy_.2566
- ___Block_byref_object_copy_.3389
- ___Block_byref_object_copy_.3987
- ___Block_byref_object_copy_.4555
- ___Block_byref_object_copy_.5208
- ___Block_byref_object_copy_.5423
- ___Block_byref_object_copy_.5648
- ___Block_byref_object_copy_.5771
- ___Block_byref_object_copy_.6315
- ___Block_byref_object_copy_.6434
- ___Block_byref_object_copy_.6518
- ___Block_byref_object_copy_.6728
- ___Block_byref_object_copy_.7362
- ___Block_byref_object_copy_.7547
- ___Block_byref_object_copy_.7767
- ___Block_byref_object_dispose_.1718
- ___Block_byref_object_dispose_.1790
- ___Block_byref_object_dispose_.1924
- ___Block_byref_object_dispose_.2186
- ___Block_byref_object_dispose_.2567
- ___Block_byref_object_dispose_.3390
- ___Block_byref_object_dispose_.3988
- ___Block_byref_object_dispose_.4556
- ___Block_byref_object_dispose_.5209
- ___Block_byref_object_dispose_.5424
- ___Block_byref_object_dispose_.5649
- ___Block_byref_object_dispose_.5772
- ___Block_byref_object_dispose_.6316
- ___Block_byref_object_dispose_.6435
- ___Block_byref_object_dispose_.6519
- ___Block_byref_object_dispose_.6729
- ___Block_byref_object_dispose_.7363
- ___Block_byref_object_dispose_.7548
- ___Block_byref_object_dispose_.7768
- _____fetchNextBatch_block_invoke.5211
- _____fetchNextBatch_block_invoke_2.5214
- ___block_descriptor_32_e21_"HMFTimer"24?0d8Q16l
- ___block_literal_global.12.2950
- ___block_literal_global.12.6255
- ___block_literal_global.1263
- ___block_literal_global.1508
- ___block_literal_global.2009
- ___block_literal_global.2088
- ___block_literal_global.2179
- ___block_literal_global.2306
- ___block_literal_global.2663
- ___block_literal_global.2830
- ___block_literal_global.2957
- ___block_literal_global.3037
- ___block_literal_global.3231
- ___block_literal_global.33.5154
- ___block_literal_global.3407
- ___block_literal_global.3763
- ___block_literal_global.3875
- ___block_literal_global.4097
- ___block_literal_global.4176
- ___block_literal_global.5119
- ___block_literal_global.5880
- ___block_literal_global.6017
- ___block_literal_global.6263
- ___block_literal_global.6344
- ___block_literal_global.6436
- ___block_literal_global.6650
- ___block_literal_global.6732
- ___block_literal_global.6944
- ___block_literal_global.7282
- ___block_literal_global.7365
- ___block_literal_global.7568
- ___block_literal_global.8174
- ___block_literal_global.8315
- ___block_literal_global.961
- _hmbProperties._properties.2958
- _hmbProperties._properties.3232
- _hmbProperties._properties.6345
- _hmbProperties._properties.7783
- _hmbProperties.onceToken.2956
- _hmbProperties.onceToken.3230
- _hmbProperties.onceToken.6343
- _hmbProperties.onceToken.7782
- _logCategory._hmf_once_t0.4096
- _logCategory._hmf_once_t100
- _logCategory._hmf_once_t19
- _logCategory._hmf_once_t7.6649
- _logCategory._hmf_once_v1.4098
- _logCategory._hmf_once_v101
- _logCategory._hmf_once_v20
- _logCategory._hmf_once_v8.6651
CStrings:
+ "%{public}@Failed to create state zone for HMBCloudDatabase initialization: %@"
+ "%{public}@Failed to open SQL context for HMBLocalDatabase initialization: %@"
+ "@\"HMFTimer\"20@?0d8I16"
+ "hmf_enumerateWithAutoreleasePoolUsingBlock:"
+ "initWithDatastorePath:configuration:error:"
+ "initWithLocalDatabase:configuration:error:"
- "%{public}@Failed to create state zone for database: %@"
- "%{public}@Unable to create our local storage: %@."
- "@\"HMFTimer\"24@?0d8Q16"
- "ebl00"
- "ebl01"
- "initWithDatastorePath:configuration:"
- "initWithLocalDatabase:configuration:"
- "parent_record"
- "sa00"
- "sa01"

```
