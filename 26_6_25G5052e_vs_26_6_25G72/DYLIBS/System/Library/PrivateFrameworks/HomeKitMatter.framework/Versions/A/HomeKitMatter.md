## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1418.7.15.0.0
-  __TEXT.__text: 0x1659b4
+1418.7.18.0.0
+  __TEXT.__text: 0x16579c
   __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_methlist: 0xa62c
+  __TEXT.__objc_methlist: 0xa5e4
   __TEXT.__const: 0x168
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__gcc_except_tab: 0x3310
   __TEXT.__cstring: 0x69d3
-  __TEXT.__oslogstring: 0x26fa9
+  __TEXT.__oslogstring: 0x26fea
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x3470
+  __TEXT.__unwind_info: 0x3458
   __TEXT.__objc_classname: 0x14b0
-  __TEXT.__objc_methname: 0x25a1d
-  __TEXT.__objc_methtype: 0x3e09
+  __TEXT.__objc_methname: 0x259f0
+  __TEXT.__objc_methtype: 0x3de6
   __TEXT.__objc_stubs: 0x15fa0
   __DATA_CONST.__got: 0x950
-  __DATA_CONST.__const: 0xc48
+  __DATA_CONST.__const: 0xc50
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128

   __AUTH_CONST.__auth_got: 0x440
   __AUTH_CONST.__const: 0x5490
   __AUTH_CONST.__cfstring: 0x6c20
-  __AUTH_CONST.__objc_const: 0xf9b8
+  __AUTH_CONST.__objc_const: 0xf928
   __AUTH_CONST.__objc_intobj: 0x16e0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1db0
-  __DATA.__objc_ivar: 0xb00
+  __DATA.__objc_ivar: 0xaf4
   __DATA.__data: 0xde0
   __DATA.__bss: 0x460
   __DATA_DIRTY.__objc_data: 0xc80

   - /System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4367
-  Symbols:   10058
+  Functions: 4361
+  Symbols:   10050
   CStrings:  8520
 
Symbols:
+ -[HMMTRAccessoryServer startBusyImageResponseTimer:timeInterval:requestParams:queue:]
+ -[HMMTRAccessoryServer startOtaProviderSchedulerTimer:queue:]
+ -[HMMTRAnnounceOtaSchedulerTimer init:server:queue:]
+ -[HMMTROTAAnnounceTimer initWithServer:nodeId:queue:]
+ -[HMMTRQueryImageResponseBusyTimer initWithServer:softwareUpdateProvider:timeInterval:requestParams:queue:]
+ GCC_except_table1034
+ GCC_except_table1040
+ GCC_except_table1164
+ GCC_except_table1232
+ GCC_except_table1278
+ GCC_except_table1286
+ GCC_except_table1337
+ GCC_except_table1345
+ GCC_except_table1382
+ GCC_except_table1419
+ GCC_except_table1446
+ GCC_except_table1642
+ GCC_except_table1685
+ GCC_except_table1839
+ GCC_except_table1840
+ GCC_except_table1841
+ GCC_except_table1844
+ GCC_except_table1864
+ GCC_except_table1865
+ GCC_except_table1866
+ GCC_except_table1867
+ GCC_except_table1868
+ GCC_except_table1875
+ GCC_except_table1876
+ GCC_except_table1878
+ GCC_except_table1879
+ GCC_except_table1939
+ GCC_except_table1947
+ GCC_except_table2024
+ GCC_except_table2138
+ GCC_except_table2140
+ GCC_except_table2170
+ GCC_except_table2180
+ GCC_except_table2182
+ GCC_except_table2238
+ GCC_except_table2284
+ GCC_except_table2308
+ GCC_except_table2379
+ GCC_except_table2642
+ GCC_except_table2646
+ GCC_except_table2702
+ GCC_except_table2735
+ GCC_except_table2776
+ GCC_except_table2778
+ GCC_except_table2803
+ GCC_except_table2804
+ GCC_except_table2805
+ GCC_except_table2827
+ GCC_except_table2828
+ GCC_except_table2829
+ GCC_except_table2830
+ GCC_except_table2831
+ GCC_except_table2832
+ GCC_except_table2846
+ GCC_except_table2848
+ GCC_except_table2873
+ GCC_except_table2888
+ GCC_except_table2907
+ GCC_except_table2910
+ GCC_except_table2914
+ GCC_except_table2929
+ GCC_except_table2932
+ GCC_except_table2936
+ GCC_except_table2957
+ GCC_except_table2964
+ GCC_except_table2969
+ GCC_except_table2981
+ GCC_except_table3034
+ GCC_except_table3035
+ GCC_except_table3412
+ GCC_except_table3413
+ GCC_except_table3414
+ GCC_except_table3427
+ GCC_except_table3443
+ GCC_except_table3458
+ GCC_except_table3526
+ GCC_except_table3527
+ GCC_except_table3556
+ GCC_except_table3587
+ GCC_except_table3591
+ GCC_except_table3599
+ GCC_except_table3618
+ GCC_except_table3621
+ GCC_except_table3663
+ GCC_except_table3667
+ GCC_except_table3685
+ GCC_except_table3687
+ GCC_except_table3708
+ GCC_except_table3785
+ GCC_except_table3832
+ GCC_except_table3852
+ GCC_except_table3876
+ GCC_except_table3880
+ GCC_except_table3895
+ GCC_except_table3896
+ GCC_except_table3897
+ GCC_except_table3910
+ GCC_except_table3950
+ GCC_except_table3970
+ GCC_except_table4012
+ GCC_except_table4021
+ GCC_except_table4106
+ GCC_except_table4107
+ GCC_except_table4164
+ GCC_except_table4167
+ GCC_except_table4231
+ GCC_except_table4291
+ GCC_except_table4307
+ GCC_except_table4341
+ GCC_except_table839
+ GCC_except_table882
+ GCC_except_table947
+ GCC_except_table953
+ GCC_except_table963
+ GCC_except_table967
+ GCC_except_table972
+ _kDefaultOtaProviderEndpoint
+ _objc_msgSend$init:server:queue:
+ _objc_msgSend$initWithServer:softwareUpdateProvider:timeInterval:requestParams:queue:
+ _objc_msgSend$startOtaProviderSchedulerTimer:queue:
- -[HMMTRAccessoryServer startBusyImageResponseTimer:timeInterval:endpoint:requestParams:queue:]
- -[HMMTRAccessoryServer startOtaProviderSchedulerTimer:endpoint:queue:]
- -[HMMTRAnnounceOtaSchedulerTimer endpoint]
- -[HMMTRAnnounceOtaSchedulerTimer init:server:endpoint:queue:]
- -[HMMTRAnnounceOtaSchedulerTimer setEndpoint:]
- -[HMMTROTAAnnounceTimer endpoint]
- -[HMMTROTAAnnounceTimer initWithServer:nodeId:endpoint:queue:]
- -[HMMTROTAAnnounceTimer setEndpoint:]
- -[HMMTRQueryImageResponseBusyTimer endpoint]
- -[HMMTRQueryImageResponseBusyTimer initWithServer:softwareUpdateProvider:timeInterval:endpoint:requestParams:queue:]
- -[HMMTRQueryImageResponseBusyTimer setEndpoint:]
- GCC_except_table1036
- GCC_except_table1044
- GCC_except_table1168
- GCC_except_table1236
- GCC_except_table1282
- GCC_except_table1290
- GCC_except_table1341
- GCC_except_table1349
- GCC_except_table1386
- GCC_except_table1423
- GCC_except_table1452
- GCC_except_table1648
- GCC_except_table1691
- GCC_except_table1845
- GCC_except_table1846
- GCC_except_table1847
- GCC_except_table1850
- GCC_except_table1870
- GCC_except_table1872
- GCC_except_table1873
- GCC_except_table1881
- GCC_except_table1882
- GCC_except_table1883
- GCC_except_table1884
- GCC_except_table1885
- GCC_except_table1886
- GCC_except_table1945
- GCC_except_table1953
- GCC_except_table2030
- GCC_except_table2144
- GCC_except_table2146
- GCC_except_table2176
- GCC_except_table2186
- GCC_except_table2188
- GCC_except_table2244
- GCC_except_table2290
- GCC_except_table2314
- GCC_except_table2385
- GCC_except_table2648
- GCC_except_table2652
- GCC_except_table2708
- GCC_except_table2741
- GCC_except_table2782
- GCC_except_table2784
- GCC_except_table2809
- GCC_except_table2810
- GCC_except_table2811
- GCC_except_table2835
- GCC_except_table2836
- GCC_except_table2837
- GCC_except_table2838
- GCC_except_table2839
- GCC_except_table2840
- GCC_except_table2852
- GCC_except_table2854
- GCC_except_table2879
- GCC_except_table2900
- GCC_except_table2913
- GCC_except_table2916
- GCC_except_table2920
- GCC_except_table2935
- GCC_except_table2942
- GCC_except_table2944
- GCC_except_table2963
- GCC_except_table2970
- GCC_except_table2975
- GCC_except_table2987
- GCC_except_table3040
- GCC_except_table3041
- GCC_except_table3419
- GCC_except_table3420
- GCC_except_table3430
- GCC_except_table3433
- GCC_except_table3449
- GCC_except_table3464
- GCC_except_table3532
- GCC_except_table3533
- GCC_except_table3562
- GCC_except_table3593
- GCC_except_table3597
- GCC_except_table3605
- GCC_except_table3624
- GCC_except_table3627
- GCC_except_table3669
- GCC_except_table3673
- GCC_except_table3691
- GCC_except_table3693
- GCC_except_table3714
- GCC_except_table3791
- GCC_except_table3838
- GCC_except_table3858
- GCC_except_table3882
- GCC_except_table3886
- GCC_except_table3901
- GCC_except_table3902
- GCC_except_table3909
- GCC_except_table3916
- GCC_except_table3956
- GCC_except_table3976
- GCC_except_table4024
- GCC_except_table4027
- GCC_except_table4112
- GCC_except_table4113
- GCC_except_table4170
- GCC_except_table4173
- GCC_except_table4237
- GCC_except_table4309
- GCC_except_table4313
- GCC_except_table4347
- GCC_except_table841
- GCC_except_table884
- GCC_except_table949
- GCC_except_table961
- GCC_except_table965
- GCC_except_table969
- GCC_except_table974
- OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._endpoint
- OBJC_IVAR_$_HMMTROTAAnnounceTimer._endpoint
- OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._endpoint
- _objc_msgSend$init:server:endpoint:queue:
- _objc_msgSend$initWithServer:softwareUpdateProvider:timeInterval:endpoint:requestParams:queue:
- _objc_msgSend$startOtaProviderSchedulerTimer:endpoint:queue:
CStrings:
+ "%{public}@Timer already deallocated, skipping completion handler"
+ "@40@0:8d16@24@32"
+ "init:server:queue:"
+ "initWithServer:nodeId:queue:"
+ "initWithServer:softwareUpdateProvider:timeInterval:requestParams:queue:"
+ "startBusyImageResponseTimer:timeInterval:requestParams:queue:"
+ "startOtaProviderSchedulerTimer:queue:"
+ "v32@0:8d16@24"
+ "v48@0:8@16d24@32@40"
- "@48@0:8d16@24@32@40"
- "@64@0:8@16@24d32@40@48@56"
- "init:server:endpoint:queue:"
- "initWithServer:nodeId:endpoint:queue:"
- "initWithServer:softwareUpdateProvider:timeInterval:endpoint:requestParams:queue:"
- "startBusyImageResponseTimer:timeInterval:endpoint:requestParams:queue:"
- "startOtaProviderSchedulerTimer:endpoint:queue:"
- "v40@0:8d16@24@32"
- "v56@0:8@16d24@32@40@48"
```
