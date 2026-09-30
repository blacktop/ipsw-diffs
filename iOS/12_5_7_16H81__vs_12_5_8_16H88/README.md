# 12.5.7 (16H81) .vs 12.5.8 (16H88)

## IPSWs

- `iPhone_5.5_12.5.7_16H81_Restore.ipsw`
- `iPhone_5.5_12.5.8_16H88_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 12.5.7 *(16H81)* | 18.7.0 | 4903.272.5~1 | Fri, 19Aug2022 23:28:26 PDT |
| 12.5.8 *(16H88)* | 18.7.0 | 4903.272.5~1 | Fri, 19Aug2022 23:28:26 PDT |

## MachO

### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

#### CheckerBoard

>  `/Applications/CheckerBoard.app/CheckerBoard`

```diff

 37.0.0.0.0
-  __TEXT.__text: 0x3f858
+  __TEXT.__text: 0x3f854
   __TEXT.__stubs: 0xac8
   __TEXT.__stub_helper: 0xae0
   __TEXT.__objc_classname: 0x52a

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6BC289EC-8617-3D05-95A2-610F3B42FF00
+  UUID: C61757EF-E435-345B-BC5D-BDBB806AC29D
   Functions: 873
   Symbols:   382
   CStrings:  4104
Functions:
~ sub_10003e348 -> sub_10003e34c : 5380 -> 5376

```

#### eapolclient

>  `/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient`

```diff

 264.250.6.0.0
-  __TEXT.__text: 0x20d64
+  __TEXT.__text: 0x20d60
   __TEXT.__stubs: 0x9fc
   __TEXT.__stub_helper: 0xa14
   __TEXT.__oslogstring: 0x1334

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X
   - /usr/lib/libSystem.B.dylib
-  UUID: 81238434-8ACE-3FC9-9563-D297339788DE
+  UUID: 99D6D88D-CB3D-3E66-832A-55C400DB6CA2
   Functions: 174
   Symbols:   249
   CStrings:  1861
Functions:
~ sub_100021af8 -> sub_100021afc : 5380 -> 5376

```

#### IPConfiguration

>  `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

```diff

 359.250.1.0.0
-  __TEXT.__text: 0x4a1c8
+  __TEXT.__text: 0x4a1c4
   __TEXT.__stubs: 0xc30
   __TEXT.__stub_helper: 0xc48
   __TEXT.__const: 0x39b

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4CCA223-95F6-3835-9BFA-0AD7E771B933
+  UUID: AF92FED1-E6E4-3972-A9A7-8342CB98C9A3
   Functions: 936
   Symbols:   647
   CStrings:  2785
Functions:
~ sub_4a1d0 -> sub_4a1d4 : 5380 -> 5376

```

#### hostapd

>  `/usr/libexec/hostapd`

```diff

 33.1.0.0.0
-  __TEXT.__text: 0x40e5c
+  __TEXT.__text: 0x40e58
   __TEXT.__stubs: 0xb1c
   __TEXT.__stub_helper: 0xb34
   __TEXT.__const: 0x1323

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 011A5E01-12FE-3E17-BC4E-6D241FDACA85
+  UUID: D1415025-2C15-350C-8554-86E1E65E1605
   Functions: 747
   Symbols:   259
   CStrings:  2861
Functions:
~ sub_1000421f0 -> sub_1000421f4 : 5380 -> 5376

```

#### trustd

>  `/usr/libexec/trustd`

```diff

-58286.270.3.0.2
-  __TEXT.__text: 0x42104
-  __TEXT.__stubs: 0x171c
-  __TEXT.__stub_helper: 0x1734
-  __TEXT.__const: 0x2ff4
-  __TEXT.__gcc_except_tab: 0x580
-  __TEXT.__cstring: 0x4eb9
-  __TEXT.__oslogstring: 0x360d
+58286.270.3.0.3
+  __TEXT.__text: 0x437e0
+  __TEXT.__stubs: 0x1728
+  __TEXT.__stub_helper: 0x1740
+  __TEXT.__const: 0x419c
+  __TEXT.__gcc_except_tab: 0x744
+  __TEXT.__cstring: 0x4f37
+  __TEXT.__oslogstring: 0x379a
   __TEXT.__objc_classname: 0x105
-  __TEXT.__objc_methname: 0x186a
+  __TEXT.__objc_methname: 0x1898
   __TEXT.__objc_methtype: 0x8f4
-  __TEXT.__unwind_info: 0xb24
-  __DATA.__got: 0x4d8
-  __DATA.__la_symbol_ptr: 0xf68
-  __DATA.__const: 0x37a0
-  __DATA.__cfstring: 0x4940
+  __TEXT.__unwind_info: 0xb64
+  __DATA.__got: 0x4e0
+  __DATA.__la_symbol_ptr: 0xf70
+  __DATA.__const: 0x3840
+  __DATA.__cfstring: 0x49e0
   __DATA.__objc_classlist: 0x48
   __DATA.__objc_catlist: 0x8
   __DATA.__objc_protolist: 0x20
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1920
-  __DATA.__objc_selrefs: 0x6f0
-  __DATA.__objc_classrefs: 0x138
+  __DATA.__objc_selrefs: 0x708
+  __DATA.__objc_classrefs: 0x140
   __DATA.__objc_superrefs: 0x30
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x2a0
   __DATA.__common: 0x10
-  __DATA.__bss: 0x380
+  __DATA.__bss: 0x390
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6CE89DD7-80FE-39D0-A889-5650C6CB7B3C
-  Functions: 886
-  Symbols:   2189
-  CStrings:  2126
+  UUID: 8B3633F8-0064-3A3D-8487-6D6BC84C6A82
+  Functions: 908
+  Symbols:   2228
+  CStrings:  2146
 
Symbols:
+ GCC_except_table181
+ GCC_except_table200
+ GCC_except_table208
+ GCC_except_table218
+ GCC_except_table226
+ GCC_except_table283
+ GCC_except_table377
+ GCC_except_table380
+ GCC_except_table436
+ GCC_except_table440
+ GCC_except_table450
+ GCC_except_table452
+ GCC_except_table453
+ GCC_except_table490
+ GCC_except_table506
+ GCC_except_table710
+ GCC_except_table713
+ GCC_except_table763
+ GCC_except_table767
+ GCC_except_table770
+ GCC_except_table772
+ GCC_except_table776
+ SecCertificateIsValidWithAdjustments.onceToken
+ SecCertificateIsValidWithAdjustments.parakeetAnchor
+ _ApplePlatformBackportECCRootG1
+ _ApplePlatformBackportECCRootG1Hash
+ _ApplePlatformBackportRSARootG1
+ _ApplePlatformBackportRSARootG1Hash
+ _ConvertSupplementalAnchorDatasToCerts
+ _GetPeriodicUpdateDelta
+ _InitializeLastAssetCheckIn
+ _OBJC_CLASS_$_NSFileManager
+ _QueryOTATrustAsset
+ _SecCertificateIsValidWithAdjustments
+ _SecOTAPKICopyLastAssetCheckInDate
+ _SecOTAPKICopySupplementalAnchors
+ _SecOTAPKIKillSwitchEnabled
+ _SecPolicyCheckCT
+ _SecPolicyCheckValidLeaf
+ _SecSupplementalSystemAnchorSourceContains
+ _TestApplePlatformBackportECCRootG1
+ _TestApplePlatformBackportECCRootG1Hash
+ _TestApplePlatformBackportRSARootG1
+ _TestApplePlatformBackportRSARootG1Hash
+ _UpdateLocalCheckInDate
+ _UpdateOTARequestDate
+ __Block_byref_object_copy_.1593
+ __Block_byref_object_copy_.536
+ __Block_byref_object_copy_.700
+ __Block_byref_object_copy_.850
+ __Block_byref_object_dispose_.1594
+ __Block_byref_object_dispose_.537
+ __Block_byref_object_dispose_.701
+ __Block_byref_object_dispose_.851
+ __InitializeOTATrustAsset_block_invoke.217
+ __InitializeOTATrustAsset_block_invoke.220
+ __InitializeOTATrustAsset_block_invoke.226
+ __InitializeOTATrustAsset_block_invoke.229
+ __SecOTAPKICopyCurrentOTAPKIRef_block_invoke.85
+ __SecPolicyCheckCT_block_invoke.71
+ __SecPolicyCheckCT_block_invoke.76
+ __TriggerPeriodicOTATrustAssetChecks_block_invoke.331
+ __UpdateOTACheckInDate_block_invoke.324
+ ___GetAssetFileURL_block_invoke
+ ___QueryOTATrustAsset_block_invoke
+ ___SecCertificateIsValidWithAdjustments_block_invoke
+ ___SecOTAPKICopyAppleCertificateAuthorities_block_invoke
+ ___SecOTAPKICopyLastAssetCheckInDate_block_invoke
+ ___SecOTAPKICopySupplementalAnchors_block_invoke
+ ___SecOTAPKICopyTrustedCTLogs_block_invoke
+ ___SecOTAPKIGetSamplingRateForEvent_block_invoke
+ ___SecOTAPKIKillSwitchEnabled_block_invoke
+ ___block_descriptor_40_e8_32r_e9_v16@?0r*8l
+ ___block_descriptor_48_e8_32r_e5_v8@?0l
+ ___block_descriptor_72_e8_32r40r48r56r64r_e5_v8@?0l
+ ___block_descriptor_73_e8_32s40s48s56r64r_e8_v16@?0q8l
+ ___copy_helper_block_e8_32r40r48r56r64r
+ ___copy_helper_block_e8_32s40s48s56r64r
+ ___destroy_helper_block_e8_32r40r48r56r64r
+ ___destroy_helper_block_e8_32s40s48s56r64r
+ __block_descriptor_tmp.1.514
+ __block_descriptor_tmp.1.623
+ __block_descriptor_tmp.10.1107
+ __block_descriptor_tmp.10.1357
+ __block_descriptor_tmp.10.1858
+ __block_descriptor_tmp.100.1132
+ __block_descriptor_tmp.1000
+ __block_descriptor_tmp.110.1119
+ __block_descriptor_tmp.1138
+ __block_descriptor_tmp.12.1780
+ __block_descriptor_tmp.12.490
+ __block_descriptor_tmp.1338
+ __block_descriptor_tmp.145.1124
+ __block_descriptor_tmp.15.1779
+ __block_descriptor_tmp.15.599
+ __block_descriptor_tmp.152.1157
+ __block_descriptor_tmp.16.1240
+ __block_descriptor_tmp.16.1749
+ __block_descriptor_tmp.1811
+ __block_descriptor_tmp.1866
+ __block_descriptor_tmp.19.1747
+ __block_descriptor_tmp.19.577
+ __block_descriptor_tmp.2.630
+ __block_descriptor_tmp.22.1775
+ __block_descriptor_tmp.22.612
+ __block_descriptor_tmp.24.1242
+ __block_descriptor_tmp.24.1892
+ __block_descriptor_tmp.25.1913
+ __block_descriptor_tmp.26.1917
+ __block_descriptor_tmp.26.614
+ __block_descriptor_tmp.27.1262
+ __block_descriptor_tmp.27.1921
+ __block_descriptor_tmp.28.1265
+ __block_descriptor_tmp.28.1769
+ __block_descriptor_tmp.3.1810
+ __block_descriptor_tmp.3.633
+ __block_descriptor_tmp.30.1267
+ __block_descriptor_tmp.30.1762
+ __block_descriptor_tmp.30.616
+ __block_descriptor_tmp.31.1040
+ __block_descriptor_tmp.31.1763
+ __block_descriptor_tmp.32.1759
+ __block_descriptor_tmp.33.610
+ __block_descriptor_tmp.34.1937
+ __block_descriptor_tmp.36.618
+ __block_descriptor_tmp.39.629
+ __block_descriptor_tmp.4.1846
+ __block_descriptor_tmp.4.531
+ __block_descriptor_tmp.40.1873
+ __block_descriptor_tmp.40.626
+ __block_descriptor_tmp.43.1122
+ __block_descriptor_tmp.43.624
+ __block_descriptor_tmp.449
+ __block_descriptor_tmp.46.634
+ __block_descriptor_tmp.49.1220
+ __block_descriptor_tmp.5.1757
+ __block_descriptor_tmp.5.568
+ __block_descriptor_tmp.5.593
+ __block_descriptor_tmp.50.1050
+ __block_descriptor_tmp.50.1247
+ __block_descriptor_tmp.50.1879
+ __block_descriptor_tmp.521
+ __block_descriptor_tmp.55.1941
+ __block_descriptor_tmp.550
+ __block_descriptor_tmp.591
+ __block_descriptor_tmp.61.1227
+ __block_descriptor_tmp.65.1271
+ __block_descriptor_tmp.66.1074
+ __block_descriptor_tmp.66.1270
+ __block_descriptor_tmp.7.571
+ __block_descriptor_tmp.70.1276
+ __block_descriptor_tmp.73.1282
+ __block_descriptor_tmp.74.1249
+ __block_descriptor_tmp.75.1248
+ __block_descriptor_tmp.79
+ __block_descriptor_tmp.8.1855
+ __block_descriptor_tmp.8.572
+ __block_descriptor_tmp.8.596
+ __block_descriptor_tmp.80
+ __block_descriptor_tmp.84
+ __block_descriptor_tmp.9.525
+ __block_literal_global.10.523
+ __block_literal_global.1049
+ __block_literal_global.1264
+ __block_literal_global.1476
+ __block_literal_global.1742
+ __block_literal_global.1863
+ __block_literal_global.216
+ __block_literal_global.218
+ __block_literal_global.221
+ __block_literal_global.227
+ __block_literal_global.230
+ __block_literal_global.298
+ __block_literal_global.332
+ __block_literal_global.367
+ __block_literal_global.374
+ __block_literal_global.448
+ __block_literal_global.513
+ __block_literal_global.592
+ __block_literal_global.62
+ __block_literal_global.683
+ __block_literal_global.81
+ __block_literal_global.86
+ __block_literal_global.892
+ __parakeet_anchor
+ _dispatch_assert_queue$V2
+ _kSecPolicyCheckValidLeaf
+ apply_block_1.1001
+ apply_block_1.1358
+ apply_block_1.1812
+ apply_block_1.1939
+ apply_block_1.516
+ apply_block_1.580
+ apply_block_1.589
+ apply_block_2.1075
+ apply_block_2.1748
+ apply_block_2.578
- GCC_except_table197
- GCC_except_table203
- GCC_except_table211
- GCC_except_table264
- GCC_except_table359
- GCC_except_table362
- GCC_except_table400
- GCC_except_table422
- GCC_except_table432
- GCC_except_table434
- GCC_except_table435
- GCC_except_table472
- GCC_except_table488
- GCC_except_table688
- GCC_except_table691
- GCC_except_table728
- GCC_except_table741
- GCC_except_table745
- GCC_except_table748
- GCC_except_table754
- __Block_byref_object_copy_.1595
- __Block_byref_object_copy_.533
- __Block_byref_object_copy_.690
- __Block_byref_object_copy_.831
- __Block_byref_object_dispose_.1596
- __Block_byref_object_dispose_.534
- __Block_byref_object_dispose_.691
- __Block_byref_object_dispose_.832
- __DownloadOTATrustAsset_block_invoke.300
- __InitializeOTATrustAsset_block_invoke.191
- __InitializeOTATrustAsset_block_invoke.195
- __InitializeOTATrustAsset_block_invoke.201
- __InitializeOTATrustAsset_block_invoke.204
- __SecOTAPKICopyCurrentOTAPKIRef_block_invoke.79
- __SecPolicyCheckCT_block_invoke.65
- __SecPolicyCheckCT_block_invoke.72
- __TriggerPeriodicOTATrustAssetChecks_block_invoke.241
- ___block_descriptor_64_e8_32r40r48r56r_e5_v8@?0l
- ___block_descriptor_73_e8_32s40s48r56r64r_e8_v16@?0q8l
- ___copy_helper_block_e8_32r40r48r56r
- ___copy_helper_block_e8_32s40s48r56r64r
- ___destroy_helper_block_e8_32r40r48r56r
- ___destroy_helper_block_e8_32s40s48r56r64r
- __block_descriptor_tmp.1.508
- __block_descriptor_tmp.1.620
- __block_descriptor_tmp.10.1088
- __block_descriptor_tmp.10.1345
- __block_descriptor_tmp.10.1865
- __block_descriptor_tmp.100.1115
- __block_descriptor_tmp.110.1102
- __block_descriptor_tmp.1121
- __block_descriptor_tmp.12.1787
- __block_descriptor_tmp.12.487
- __block_descriptor_tmp.1326
- __block_descriptor_tmp.145.1107
- __block_descriptor_tmp.15.1786
- __block_descriptor_tmp.15.596
- __block_descriptor_tmp.152.1141
- __block_descriptor_tmp.16.1223
- __block_descriptor_tmp.16.1756
- __block_descriptor_tmp.1818
- __block_descriptor_tmp.1873
- __block_descriptor_tmp.19.1754
- __block_descriptor_tmp.19.574
- __block_descriptor_tmp.2.627
- __block_descriptor_tmp.22.1782
- __block_descriptor_tmp.22.609
- __block_descriptor_tmp.24.1225
- __block_descriptor_tmp.24.1899
- __block_descriptor_tmp.25.1920
- __block_descriptor_tmp.26.1924
- __block_descriptor_tmp.26.611
- __block_descriptor_tmp.27.1244
- __block_descriptor_tmp.27.1928
- __block_descriptor_tmp.28.1249
- __block_descriptor_tmp.28.1776
- __block_descriptor_tmp.3.1817
- __block_descriptor_tmp.3.630
- __block_descriptor_tmp.30.1251
- __block_descriptor_tmp.30.1769
- __block_descriptor_tmp.30.613
- __block_descriptor_tmp.31.1020
- __block_descriptor_tmp.31.1770
- __block_descriptor_tmp.32.1766
- __block_descriptor_tmp.33.607
- __block_descriptor_tmp.34.1944
- __block_descriptor_tmp.36.615
- __block_descriptor_tmp.39.626
- __block_descriptor_tmp.4.1853
- __block_descriptor_tmp.4.528
- __block_descriptor_tmp.40.1880
- __block_descriptor_tmp.40.623
- __block_descriptor_tmp.43.1105
- __block_descriptor_tmp.43.621
- __block_descriptor_tmp.446
- __block_descriptor_tmp.46.631
- __block_descriptor_tmp.49.1206
- __block_descriptor_tmp.5.1764
- __block_descriptor_tmp.5.565
- __block_descriptor_tmp.5.590
- __block_descriptor_tmp.50.1230
- __block_descriptor_tmp.50.1886
- __block_descriptor_tmp.518
- __block_descriptor_tmp.547
- __block_descriptor_tmp.55.1948
- __block_descriptor_tmp.585
- __block_descriptor_tmp.60
- __block_descriptor_tmp.64.1089
- __block_descriptor_tmp.65.1257
- __block_descriptor_tmp.66.1050
- __block_descriptor_tmp.66.1256
- __block_descriptor_tmp.7.568
- __block_descriptor_tmp.71.1264
- __block_descriptor_tmp.73.1270
- __block_descriptor_tmp.74.1231
- __block_descriptor_tmp.77.1255
- __block_descriptor_tmp.78.1254
- __block_descriptor_tmp.8.1862
- __block_descriptor_tmp.8.569
- __block_descriptor_tmp.8.593
- __block_descriptor_tmp.82
- __block_descriptor_tmp.9.522
- __block_descriptor_tmp.981
- __block_literal_global.10.520
- __block_literal_global.1033
- __block_literal_global.1248
- __block_literal_global.1466
- __block_literal_global.1749
- __block_literal_global.1870
- __block_literal_global.189
- __block_literal_global.193
- __block_literal_global.196
- __block_literal_global.202
- __block_literal_global.205
- __block_literal_global.242
- __block_literal_global.319
- __block_literal_global.328.409
- __block_literal_global.369
- __block_literal_global.445
- __block_literal_global.510
- __block_literal_global.589
- __block_literal_global.673
- __block_literal_global.75
- __block_literal_global.80
- __block_literal_global.881
- apply_block_1.1346
- apply_block_1.1819
- apply_block_1.1946
- apply_block_1.513
- apply_block_1.577
- apply_block_1.586
- apply_block_1.982
- apply_block_2.1051
- apply_block_2.1755
- apply_block_2.575
- is_apple_ca.appleISTCA2G1_spkiSHA256
- is_apple_ca.appleISTCA8G1_spkiSHA256
- is_apple_ca.googleIAG3_spkiSHA256
CStrings:
+ "%@-%@"
+ "Anchors.plist"
+ "MobileAssetLastRequest"
+ "OTAContext.plist missing kill switch"
+ "OTATrust: failed to read supplemental anchors list from asset data: %@"
+ "OTATrust: failed to update from asset during periodic re-read: %@"
+ "OTATrust: failed to write last request time: %@"
+ "OTATrust: unable to create SupplementalAnchors from asset file: %@"
+ "Pinning database should not update from version %@ to version %@"
+ "SupplementalsAssets"
+ "Using %lu Supplemental Anchors from asset data"
+ "arrayWithCapacity:"
+ "com.apple.MobileAsset.PKITrustSupplementals.ma.cached-metadata-updated"
+ "com.apple.trustd.asset.downloadAsset"
+ "dateWithTimeIntervalSince1970:"
+ "defaultManager"
+ "fileExistsAtPath:"
+ "fileURLWithPath:isDirectory:"
+ "last MobileAsset request too recent for %@, skipping check."
+ "periodic re-read asset from disk"
- "SupplementalsAssets/"
- "URLByAppendingPathComponent:isDirectory:"
- "augmentResultsWithState:"
- "com.apple.MobileAsset.PKITrustSupplementals.cached-metadata-updated"
- "com.apple.trustd.PKITrustSupplementals.downloadAsset"

```

#### wapic

>  `/usr/libexec/wapic`

```diff

 34.1.0.0.0
-  __TEXT.__text: 0x2d900
+  __TEXT.__text: 0x2d8fc
   __TEXT.__stubs: 0x9c0
   __TEXT.__stub_helper: 0x9d8
   __TEXT.__cstring: 0x817b

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 968CDF96-3D87-3D16-855B-3C9F7F5C24A4
+  UUID: 2331EE7A-EAF2-3032-AB88-4BBE6B859D07
   Functions: 379
   Symbols:   232
   CStrings:  2132
Functions:
~ sub_10002d048 -> sub_10002d04c : 5380 -> 5376

```

#### wifivelocityd

>  `/usr/libexec/wifivelocityd`

```diff

 170.11.0.0.0
-  __TEXT.__text: 0x96954
+  __TEXT.__text: 0x96950
   __TEXT.__stubs: 0xe70
   __TEXT.__stub_helper: 0xe88
   __TEXT.__const: 0x630

   - /System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B4EF9C5-08DD-34B0-95D0-DE6EBD72260A
+  UUID: D3D85FE7-89E7-3C4D-B82B-054CDEFB9D2A
   Functions: 2129
   Symbols:   465
   CStrings:  6839
Functions:
~ sub_100091f88 -> sub_100091f8c : 5380 -> 5376

```

#### wifid

>  `/usr/sbin/wifid`

```diff

 634.21.0.0.0
-  __TEXT.__text: 0x17c928
+  __TEXT.__text: 0x17c994
   __TEXT.__stubs: 0x1968
   __TEXT.__stub_helper: 0x1980
   __TEXT.__gcc_except_tab: 0x17e8
   __TEXT.__const: 0xb22
   __TEXT.__objc_methname: 0x94c9
-  __TEXT.__cstring: 0xc267c
+  __TEXT.__cstring: 0xc26a4
   __TEXT.__objc_classname: 0x26c
   __TEXT.__objc_methtype: 0x15bb
   __TEXT.__oslogstring: 0x397

   __DATA.__objc_catlist: 0x8
   __DATA.__objc_protolist: 0x30
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x8ad0
+  __DATA.__objc_const: 0x8b30
   __DATA.__objc_selrefs: 0x2e80
   __DATA.__objc_classrefs: 0x518
   __DATA.__objc_superrefs: 0x98

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 854F0B1A-BEC7-3BCB-BD9A-33D6E611C5D4
-  Functions: 3002
+  UUID: B9C031CE-E7FD-3950-8FA7-8E249106592C
+  Functions: 3006
   Symbols:   865
-  CStrings:  31093
+  CStrings:  31094
 
CStrings:
+ "WiFiManager-634.21 Aug 19 2025 14:47:17"
+ "WiFiManager-634.21 Aug 19 2025 14:47:18"
- "WiFiManager-634.21 Aug 20 2022 00:54:41"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 12.5.7 *(16H81)* | 7607.3.18.0.0 |
| 12.5.8 *(16H88)* | 7607.3.18.0.0 |

### Dylibs

#### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### libCommCenterMCommandDrivers.dylib

>  `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib`

```diff

-6851.1.0.0.0
-  __TEXT.__text: 0x20bdac
+6851.2.0.0.0
+  __TEXT.__text: 0x20c334
   __TEXT.__stubs: 0x1b9c
   __TEXT.__stub_helper: 0x1b9c
-  __TEXT.__gcc_except_tab: 0x234fc
-  __TEXT.__const: 0x12a54
-  __TEXT.__cstring: 0x299d1
-  __TEXT.__oslogstring: 0x115ad
-  __TEXT.__unwind_info: 0x12190
+  __TEXT.__gcc_except_tab: 0x2355c
+  __TEXT.__const: 0x12a94
+  __TEXT.__cstring: 0x29a58
+  __TEXT.__oslogstring: 0x1163a
+  __TEXT.__unwind_info: 0x121b8
   __TEXT.__eh_frame: 0x34
   __DATA.__got_weak: 0x290
   __DATA.__la_weak_ptr: 0x10

   __DATA_CONST.__got: 0x518
   __DATA_CONST.__la_symbol_ptr: 0x1258
   __DATA_CONST.__mod_init_func: 0xd0
-  __DATA_CONST.__const: 0x20ef0
+  __DATA_CONST.__const: 0x20f70
   __DATA_CONST.__cfstring: 0xbc0
   __DATA_DIRTY.__const: 0x22
   __DATA_DIRTY.__data: 0x370

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 2241EC67-0282-32F4-8FFF-07859A22E3F4
-  Functions: 12984
-  Symbols:   33706
-  CStrings:  4880
+  UUID: 7F18D0B4-A314-323A-BE86-0713FA60ABE0
+  Functions: 12995
+  Symbols:   33734
+  CStrings:  4884
 
Symbols:
+ GCC_except_table427
+ GCC_except_table474
+ GCC_except_table478
+ GCC_except_table526
+ GCC_except_table631
+ GCC_except_table655
+ GCC_except_table656
+ GCC_except_table660
+ GCC_except_table661
+ GCC_except_table666
+ GCC_except_table684
+ GCC_except_table726
+ __ZN3qmi18MutableMessageBase10TlvWrapperIN3nas3tlv8AvoidRatEED0Ev
+ __ZN3qmi18MutableMessageBase10TlvWrapperIN3nas3tlv8AvoidRatEED1Ev
+ __ZN3qmi18MutableMessageBase6getTLVIN3nas3tlv8AvoidRatEEERT_t
+ __ZN3qmi18MutableMessageBase9createTLVIN3nas3tlv8AvoidRatEEERT_t
+ __ZN3tlv4sizeIN3nas3tlv8AvoidRatEEEmRKT_
+ __ZN3tlv6writeVIN3nas3tlv8AvoidRatEEEvRPhRKT_
+ __ZNK3qmi18MutableMessageBase10TlvWrapperIN3nas3tlv8AvoidRatEE5cloneEv
+ __ZNK3qmi18MutableMessageBase10TlvWrapperIN3nas3tlv8AvoidRatEE5writeERPh
+ __ZNK3qmi18MutableMessageBase10TlvWrapperIN3nas3tlv8AvoidRatEE7getSizeEv
+ __ZNSt3__110unique_ptrIZN28QMINetworkRegistrationDriver8shutdownEN8dispatch13group_sessionEE3$_9NS_14default_deleteIS4_EEED1Ev
+ __ZNSt3__110unique_ptrIZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENS_10shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEE3$_7NS_14default_deleteIS7_EEED1Ev
+ __ZTIN3qmi18MutableMessageBase10TlvWrapperIN3nas3tlv8AvoidRatEEE
+ __ZTSN3qmi18MutableMessageBase10TlvWrapperIN3nas3tlv8AvoidRatEEE
+ __ZTVN3qmi18MutableMessageBase10TlvWrapperIN3nas3tlv8AvoidRatEEE
+ __ZZN28QMINetworkRegistrationDriver14enterE911StateERKNSt3__16vectorI18EmergencySetupTypeNS0_9allocatorIS2_EEEEbENK3$_5clEv
+ __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI25NetworkRegistrationDriverE15execute_wrappedIZN28QMINetworkRegistrationDriver5startEvE3$_8EEvOT_EUlvE_EEvP16dispatch_queue_sNSt3__110unique_ptrIS8_NSD_14default_deleteIS8_EEEEENUlPvE_8__invokeESI_
+ __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI25NetworkRegistrationDriverE15execute_wrappedIZN28QMINetworkRegistrationDriver8shutdownENS_13group_sessionEE3$_9EEvOT_EUlvE_EEvP16dispatch_queue_sNSt3__110unique_ptrIS9_NSE_14default_deleteIS9_EEEEENUlPvE_8__invokeESJ_
+ __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI25NetworkRegistrationDriverE15execute_wrappedIZN28QMINetworkRegistrationDriver9bootstrapENS_13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEE3$_7EEvOT_EUlvE_EEvP16dispatch_queue_sNS8_10unique_ptrISD_NS8_14default_deleteISD_EEEEENUlPvE_8__invokeESM_
+ ____ZN28QMINetworkRegistrationDriver14enterE911StateERKNSt3__16vectorI18EmergencySetupTypeNS0_9allocatorIS2_EEEEb_block_invoke
+ ____ZN28QMINetworkRegistrationDriver15updateIMSStatusEN10subscriber7SimSlotE21RadioAccessTechnology8DataModey_block_invoke.241
+ ____ZN28QMINetworkRegistrationDriver34triggerClosedSubscriberGroupSearchEN10subscriber7SimSlotENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiN5boost8optionalI9MCCAndMNCEEON3ctu4rest19command_responder_tI17CSGSearchResponseEE_block_invoke.250
+ ____ZN28QMINetworkRegistrationDriver34triggerClosedSubscriberGroupSearchEN10subscriber7SimSlotENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiN5boost8optionalI9MCCAndMNCEEON3ctu4rest19command_responder_tI17CSGSearchResponseEE_block_invoke.252
+ ____ZZN28QMINetworkRegistrationDriver14enterE911StateERKNSt3__16vectorI18EmergencySetupTypeNS0_9allocatorIS2_EEEEbENK3$_5clEv_block_invoke
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.301
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.304
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.307
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.310
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.313
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.316
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.319
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.321
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.325
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke.329
+ ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_7clEv_block_invoke_2
+ ___block_descriptor_tmp.324
- GCC_except_table461
- GCC_except_table506
- GCC_except_table595
- GCC_except_table598
- GCC_except_table628
- GCC_except_table672
- GCC_except_table714
- __ZNSt3__110unique_ptrIZN28QMINetworkRegistrationDriver8shutdownEN8dispatch13group_sessionEE3$_7NS_14default_deleteIS4_EEED1Ev
- __ZNSt3__110unique_ptrIZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENS_10shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEE3$_5NS_14default_deleteIS7_EEED1Ev
- __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI25NetworkRegistrationDriverE15execute_wrappedIZN28QMINetworkRegistrationDriver5startEvE3$_6EEvOT_EUlvE_EEvP16dispatch_queue_sNSt3__110unique_ptrIS8_NSD_14default_deleteIS8_EEEEENUlPvE_8__invokeESI_
- __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI25NetworkRegistrationDriverE15execute_wrappedIZN28QMINetworkRegistrationDriver8shutdownENS_13group_sessionEE3$_7EEvOT_EUlvE_EEvP16dispatch_queue_sNSt3__110unique_ptrIS9_NSE_14default_deleteIS9_EEEEENUlPvE_8__invokeESJ_
- __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI25NetworkRegistrationDriverE15execute_wrappedIZN28QMINetworkRegistrationDriver9bootstrapENS_13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEE3$_5EEvOT_EUlvE_EEvP16dispatch_queue_sNS8_10unique_ptrISD_NS8_14default_deleteISD_EEEEENUlPvE_8__invokeESM_
- ____ZN28QMINetworkRegistrationDriver14enterE911StateERKNSt3__16vectorI18EmergencySetupTypeNS0_9allocatorIS2_EEEEb_block_invoke_2
- ____ZN28QMINetworkRegistrationDriver15updateIMSStatusEN10subscriber7SimSlotE21RadioAccessTechnology8DataModey_block_invoke.245
- ____ZN28QMINetworkRegistrationDriver34triggerClosedSubscriberGroupSearchEN10subscriber7SimSlotENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiN5boost8optionalI9MCCAndMNCEEON3ctu4rest19command_responder_tI17CSGSearchResponseEE_block_invoke.254
- ____ZN28QMINetworkRegistrationDriver34triggerClosedSubscriberGroupSearchEN10subscriber7SimSlotENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiN5boost8optionalI9MCCAndMNCEEON3ctu4rest19command_responder_tI17CSGSearchResponseEE_block_invoke.256
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.300
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.303
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.306
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.309
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.312
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.315
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.318
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.320
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.324
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke.328
- ____ZZN28QMINetworkRegistrationDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI46NetworkRegistrationDriverEventHandlerInterfaceEEENK3$_5clEv_block_invoke_2
- ___block_descriptor_tmp.219
- ___block_descriptor_tmp.322
CStrings:
+ "#I Entering E911 state"
+ "#I Sending cell avoidance request with RAT mask set to 0x%08llx"
+ "#N Sending cell avoidance request failed: Error in response with code %d (%s)"
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.2/CSI/Modules/vinyl/VinylQMICommandDriver.cpp"
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.2/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/Mav16QMIDataContextIP.cpp"
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.2/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextDriver.cpp"
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.2/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIPAggregator.cpp"
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.2/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIPBase.cpp"
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.2/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIQOSClientIP.cpp"
+ "Entering E911 state"
+ "Sending cell avoidance request failed: Error in response with code %d (%s)"
+ "Sending cell avoidance request with RAT mask set to 0x%08llx"
- "#I Entering E911 State."
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.1/CSI/Modules/vinyl/VinylQMICommandDriver.cpp"
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.1/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/Mav16QMIDataContextIP.cpp"
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.1/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextDriver.cpp"
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.1/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIPAggregator.cpp"
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.1/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIPBase.cpp"
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CoreTelephony-6851.1/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIQOSClientIP.cpp"
- "Entering E911 State."

```

#### Security

>  `/System/Library/Frameworks/Security.framework/Security`

```diff

-58286.270.3.0.2
-  __TEXT.__text: 0xdfc74
+58286.270.3.0.3
+  __TEXT.__text: 0xdfd80
   __TEXT.__stubs: 0x24f0
   __TEXT.__stub_helper: 0x24d8
-  __TEXT.__const: 0x51d0
-  __TEXT.__cstring: 0x11bb0
+  __TEXT.__const: 0x5250
+  __TEXT.__cstring: 0x11bba
   __TEXT.__oslogstring: 0x3c22
   __TEXT.__gcc_except_tab: 0x4210
   __TEXT.__objc_methname: 0x32b0

   __DATA_DIRTY.__bss: 0x388
   __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__la_symbol_ptr: 0x1880
-  __DATA_CONST.__const: 0x114f8
-  __DATA_CONST.__cfstring: 0xffa0
+  __DATA_CONST.__const: 0x11508
+  __DATA_CONST.__cfstring: 0xffc0
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AD91A9ED-07A6-3949-909B-D8CA972B1B7F
-  Functions: 4494
-  Symbols:   12198
-  CStrings:  6553
+  UUID: B9A5970C-B7E0-39FF-9450-AAA644B1430E
+  Functions: 4495
+  Symbols:   12204
+  CStrings:  6555
 
Symbols:
+ GCC_except_table3224
+ GCC_except_table3231
+ GCC_except_table3245
+ GCC_except_table3249
+ GCC_except_table3256
+ GCC_except_table3262
+ GCC_except_table3264
+ GCC_except_table3270
+ GCC_except_table3274
+ GCC_except_table3280
+ GCC_except_table3292
+ GCC_except_table3319
+ GCC_except_table3323
+ GCC_except_table3336
+ GCC_except_table3340
+ GCC_except_table3342
+ GCC_except_table3347
+ GCC_except_table3354
+ GCC_except_table3370
+ GCC_except_table3378
+ GCC_except_table3380
+ GCC_except_table3383
+ GCC_except_table3385
+ GCC_except_table3394
+ GCC_except_table3396
+ GCC_except_table3403
+ GCC_except_table3406
+ GCC_except_table3432
+ GCC_except_table3436
+ GCC_except_table3440
+ GCC_except_table3445
+ GCC_except_table3448
+ GCC_except_table3453
+ GCC_except_table3459
+ GCC_except_table3464
+ GCC_except_table3467
+ GCC_except_table3469
+ GCC_except_table3471
+ GCC_except_table3474
+ GCC_except_table3479
+ GCC_except_table3487
+ GCC_except_table3493
+ GCC_except_table3497
+ GCC_except_table3500
+ GCC_except_table3502
+ GCC_except_table3508
+ GCC_except_table3511
+ GCC_except_table3514
+ GCC_except_table3516
+ GCC_except_table3523
+ GCC_except_table3535
+ GCC_except_table3545
+ GCC_except_table3548
+ GCC_except_table3555
+ GCC_except_table3563
+ GCC_except_table3566
+ GCC_except_table3568
+ GCC_except_table3571
+ GCC_except_table3578
+ GCC_except_table3600
+ GCC_except_table3605
+ GCC_except_table3607
+ GCC_except_table3612
+ GCC_except_table3625
+ GCC_except_table3628
+ GCC_except_table3631
+ GCC_except_table3641
+ GCC_except_table3651
+ GCC_except_table3666
+ GCC_except_table3671
+ GCC_except_table3682
+ GCC_except_table3687
+ GCC_except_table3691
+ GCC_except_table3699
+ GCC_except_table3703
+ GCC_except_table3707
+ GCC_except_table3709
+ GCC_except_table3712
+ GCC_except_table3714
+ GCC_except_table3717
+ GCC_except_table3723
+ GCC_except_table3730
+ GCC_except_table3736
+ GCC_except_table3744
+ GCC_except_table3746
+ GCC_except_table3750
+ GCC_except_table3752
+ GCC_except_table3755
+ GCC_except_table3763
+ GCC_except_table3768
+ GCC_except_table3771
+ GCC_except_table3775
+ GCC_except_table3777
+ GCC_except_table3780
+ GCC_except_table3783
+ GCC_except_table3786
+ GCC_except_table3789
+ GCC_except_table3798
+ GCC_except_table3805
+ GCC_except_table3808
+ GCC_except_table3812
+ GCC_except_table3817
+ GCC_except_table3819
+ GCC_except_table3824
+ GCC_except_table3826
+ GCC_except_table3831
+ GCC_except_table3840
+ GCC_except_table3850
+ GCC_except_table3854
+ GCC_except_table3858
+ GCC_except_table3860
+ GCC_except_table3862
+ GCC_except_table3866
+ GCC_except_table3870
+ GCC_except_table3873
+ GCC_except_table3878
+ GCC_except_table3884
+ GCC_except_table3900
+ GCC_except_table3905
+ _ApplePlatformBackportECCRootG1Hash
+ _ApplePlatformBackportRSARootG1Hash
+ _SecPolicyCheckCertValidLeaf
+ _TestApplePlatformBackportECCRootG1Hash
+ _TestApplePlatformBackportRSARootG1Hash
+ ___CFAbsoluteTimeForGregorianZuluDay_block_invoke.5964
+ ___block_descriptor_tmp.571
+ ___block_descriptor_tmp.5930
+ _kSecPolicyCheckValidLeaf
- GCC_except_table3223
- GCC_except_table3230
- GCC_except_table3241
- GCC_except_table3247
- GCC_except_table3253
- GCC_except_table3261
- GCC_except_table3263
- GCC_except_table3266
- GCC_except_table3272
- GCC_except_table3277
- GCC_except_table3291
- GCC_except_table3315
- GCC_except_table3320
- GCC_except_table3334
- GCC_except_table3339
- GCC_except_table3341
- GCC_except_table3344
- GCC_except_table3348
- GCC_except_table3369
- GCC_except_table3376
- GCC_except_table3379
- GCC_except_table3382
- GCC_except_table3384
- GCC_except_table3390
- GCC_except_table3395
- GCC_except_table3401
- GCC_except_table3405
- GCC_except_table3431
- GCC_except_table3435
- GCC_except_table3438
- GCC_except_table3444
- GCC_except_table3446
- GCC_except_table3452
- GCC_except_table3457
- GCC_except_table3460
- GCC_except_table3465
- GCC_except_table3468
- GCC_except_table3470
- GCC_except_table3473
- GCC_except_table3478
- GCC_except_table3486
- GCC_except_table3490
- GCC_except_table3495
- GCC_except_table3498
- GCC_except_table3501
- GCC_except_table3507
- GCC_except_table3509
- GCC_except_table3513
- GCC_except_table3515
- GCC_except_table3522
- GCC_except_table3532
- GCC_except_table3540
- GCC_except_table3547
- GCC_except_table3553
- GCC_except_table3560
- GCC_except_table3565
- GCC_except_table3567
- GCC_except_table3569
- GCC_except_table3577
- GCC_except_table3594
- GCC_except_table3601
- GCC_except_table3606
- GCC_except_table3608
- GCC_except_table3613
- GCC_except_table3626
- GCC_except_table3629
- GCC_except_table3640
- GCC_except_table3650
- GCC_except_table3664
- GCC_except_table3667
- GCC_except_table3672
- GCC_except_table3684
- GCC_except_table3689
- GCC_except_table3697
- GCC_except_table3702
- GCC_except_table3704
- GCC_except_table3708
- GCC_except_table3711
- GCC_except_table3713
- GCC_except_table3715
- GCC_except_table3718
- GCC_except_table3728
- GCC_except_table3735
- GCC_except_table3740
- GCC_except_table3745
- GCC_except_table3749
- GCC_except_table3751
- GCC_except_table3753
- GCC_except_table3762
- GCC_except_table3767
- GCC_except_table3769
- GCC_except_table3772
- GCC_except_table3776
- GCC_except_table3778
- GCC_except_table3782
- GCC_except_table3784
- GCC_except_table3788
- GCC_except_table3795
- GCC_except_table3804
- GCC_except_table3807
- GCC_except_table3811
- GCC_except_table3816
- GCC_except_table3818
- GCC_except_table3820
- GCC_except_table3825
- GCC_except_table3830
- GCC_except_table3838
- GCC_except_table3842
- GCC_except_table3851
- GCC_except_table3855
- GCC_except_table3859
- GCC_except_table3861
- GCC_except_table3865
- GCC_except_table3867
- GCC_except_table3872
- GCC_except_table3875
- GCC_except_table3882
- GCC_except_table3898
- GCC_except_table3904
- ___CFAbsoluteTimeForGregorianZuluDay_block_invoke.5965
- ___block_descriptor_tmp.569
- ___block_descriptor_tmp.5928
Functions:
~ _SecPolicyCreateAppleBasicAttestationSystem : 220 -> 248
~ _SecPolicyCreateAppleBasicAttestationUser : 220 -> 248
+ _SecPolicyCheckCertValidLeaf
~ _SecLeafPVCValidateKey : 260 -> 280
~ ___SecTrustCopyErrorStrings_block_invoke.241 : 980 -> 996
~ _SecTrustEvaluateLeafOnly : 1356 -> 1380
~ ___getAnchors_block_invoke : 180 -> 260
CStrings:
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/Security/Security-58286.270.3.0.3/Analytics/SFAnalyticsActivityTracker.m"
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/Security/Security-58286.270.3.0.3/Analytics/SQLite/SFSQLite.m"
+ "/BuildRoot/Library/Caches/com.apple.xbs/Sources/Security/Security-58286.270.3.0.3/Analytics/SQLite/SFSQLiteStatement.m"
+ "ValidLeaf"
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/Security/Security-58286.270.3.0.2/Analytics/SFAnalyticsActivityTracker.m"
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/Security/Security-58286.270.3.0.2/Analytics/SQLite/SFSQLite.m"
- "/BuildRoot/Library/Caches/com.apple.xbs/Sources/Security/Security-58286.270.3.0.2/Analytics/SQLite/SFSQLiteStatement.m"

```

#### ICE

>  `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ICE.framework/ICE`

```diff

 1475.1.8.0.0
-  __TEXT.__text: 0x348bc
+  __TEXT.__text: 0x348b8
   __TEXT.__stubs: 0x60c
   __TEXT.__stub_helper: 0x624
   __TEXT.__cstring: 0x3dc0

   - /System/Library/PrivateFrameworks/AVConference.framework/Frameworks/snatmap.framework/snatmap
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
-  UUID: 4F8BCC53-9191-3492-A6AC-516A24964971
+  UUID: 0381D910-336A-390A-9FB0-ECDFB4FDA795
   Functions: 222
   Symbols:   542
   CStrings:  1669
Functions:
~ _Apple80211ParseWPS_IE : 5380 -> 5376

```

#### KeychainCircle

>  `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-58286.270.3.0.2
-  __TEXT.__text: 0xd620
+58286.270.3.0.3
+  __TEXT.__text: 0xd650
   __TEXT.__stubs: 0x744
   __TEXT.__stub_helper: 0x75c
   __TEXT.__const: 0x68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 121E4A40-7EF6-3485-86F5-FC58A9427276
-  Functions: 362
-  Symbols:   1008
+  UUID: 8086AD07-F69C-3C11-A97B-228563C7D83C
+  Functions: 363
+  Symbols:   1009
   CStrings:  784
 
Symbols:
+ _WithPathInSystemKeychainDirectory
Functions:
+ _SetCustomHomeURL

```

#### MobileWiFi

>  `/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`

```diff

 634.21.0.0.0
-  __TEXT.__text: 0x335fc
+  __TEXT.__text: 0x335f8
   __TEXT.__stubs: 0xa68
   __TEXT.__stub_helper: 0xa80
   __TEXT.__cstring: 0x6ec5

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA49B5A2-2578-38A0-AE5E-5DDBB37D68EA
+  UUID: 0461850E-9D17-3209-9890-8539BEDBD54D
   Functions: 697
   Symbols:   1385
   CStrings:  2397
Functions:
~ _Apple80211ParseWPS_IE : 5380 -> 5376

```


</details>

## Files

### 🆕 New

#### IPSW (2)

- `Firmware/Mav10-13.00.00.Release.bbfw`
- `Firmware/Mav10-13.00.00.Release.plist`

#### filesystem (2)

- `/.fseventsd/0000000000d63766`
- `/.fseventsd/0000000000d63767`

### ❌ Removed

#### IPSW (2)

- `Firmware/Mav10-7.80.04.Release.bbfw`
- `Firmware/Mav10-7.80.04.Release.plist`

#### filesystem (2)

- `/.fseventsd/000000000103af2e`
- `/.fseventsd/000000000103af2f`

## EOF
