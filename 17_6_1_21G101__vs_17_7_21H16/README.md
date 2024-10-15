# 17.6.1 (21G101) .vs 17.7 (21H16)

## IPSWs

- `iPhone16,2_17.6.1_21G101_Restore.ipsw`
- `iPhone16,2_17.7_21H16_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.6.1 *(21G101)* | 23.6.0 | 10063.142.1~1 | Fri, 05Jul2024 18:04:28 PDT |
| 17.7 *(21H16)* | 23.6.0 | 10063.142.1.700.5~1 | Thu, 01Aug2024 00:13:44 PDT |

### Kexts

#### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.filesystems.apfs`

```diff

 2236.140.6.0.0
   __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x45f11
+  __TEXT.__cstring: 0x45f1a
   __TEXT_EXEC.__text: 0x131130
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x688

   __DATA_CONST.__kalloc_var: 0x2800
   Functions: 1855
   Symbols:   0
-  CStrings:  6118
+  CStrings:  6119
 
CStrings:
+ "00:35:33"
+ "00:35:34"
+ "2024/08/01"
+ "Aug  1 2024"
- "18:23:48"
- "2024/08/16"
- "Aug 16 2024"

```

>  `com.apple.kernel`

```diff

-10063.142.1.0.0
-  __TEXT.__const: 0x340c0
+10063.142.1.700.5
+  __TEXT.__const: 0x340d0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x65487
+  __TEXT.__cstring: 0x654fe
   __TEXT.__os_log: 0x228f2
   __TEXT.__eh_frame: 0x4c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c0
-  __DATA_CONST.__const: 0xa1ef8
+  __DATA_CONST.__const: 0xa1f48
   __DATA_CONST.__hib_const: 0x140
   __DATA_CONST.__kalloc_type: 0x12d00
   __DATA_CONST.__kalloc_var: 0x7620
   __DATA_CONST.__brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xd28
-  __TEXT_EXEC.__text: 0x74eee4
+  __TEXT_EXEC.__text: 0x74ee5c
   __TEXT_BOOT_EXEC.__bootcode: 0x4cf8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__bss: 0x3d220
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5b0e8
-  __BOOTDATA.__init_entry_set: 0x10200
+  __BOOTDATA.__init_entry_set: 0x10218
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __PLK_TEXT_EXEC.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x44bf2
-  Functions: 19237
+  Functions: 19240
   Symbols:   0
-  CStrings:  15920
+  CStrings:  15924
 
CStrings:
+ "%s: pid %d refc: %u != 0 @%s:%d"
+ "com.apple.developer.media-device-discovery-extension"
+ "drop_loopback_count"
+ "fileproc_free"

```

</details>

## MachO

### ⬆️ Updated (15)

<details>
  <summary><i>View Updated</i></summary>

#### fileproviderctl

>  `/usr/bin/fileproviderctl`

```diff

-1835.140.3.0.0
+1835.140.3.701.1
   __TEXT.__text: 0xc038
   __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_stubs: 0x1c00
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__const: 0x68
+  __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x3d8
   __TEXT.__cstring: 0x18e3
   __TEXT.__ustring: 0x74e

```

#### mDNSResponder

>  `/usr/sbin/mDNSResponder`

```diff

-2200.140.11.0.0
-  __TEXT.__text: 0xf93f0
-  __TEXT.__auth_stubs: 0x2d30
+2200.140.11.701.1
+  __TEXT.__text: 0xf93ac
+  __TEXT.__auth_stubs: 0x2d20
   __TEXT.__objc_stubs: 0x1200
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__cstring: 0x195f8
-  __TEXT.__const: 0xdd0
+  __TEXT.__cstring: 0x195e9
+  __TEXT.__const: 0xdd8
   __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__oslogstring: 0x19de7
   __TEXT.__objc_classname: 0x5b1
   __TEXT.__objc_methname: 0x10c9
   __TEXT.__objc_methtype: 0x52d
-  __TEXT.__unwind_info: 0x1638
+  __TEXT.__unwind_info: 0x1634
   __TEXT.__eh_frame: 0x7c
-  __DATA_CONST.__auth_got: 0x16a8
+  __DATA_CONST.__auth_got: 0x16a0
   __DATA_CONST.__got: 0x300
   __DATA_CONST.__auth_ptr: 0x80
   __DATA_CONST.__const: 0x5a40

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1746
-  Symbols:   4128
-  CStrings:  4563
+  Functions: 1745
+  Symbols:   4126
+  CStrings:  4561
 
Symbols:
+ FreeARElemCallback.2844
+ GCC_except_table1050
+ GCC_except_table1242
+ GCC_except_table1436
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6175
+ ___mdns_server_log_block_invoke.4453
+ __block_descriptor_tmp.1.6140
+ __block_descriptor_tmp.10.4660
+ __block_descriptor_tmp.10.6170
+ __block_descriptor_tmp.10.7170
+ __block_descriptor_tmp.11.4452
+ __block_descriptor_tmp.11.5993
+ __block_descriptor_tmp.11.6508
+ __block_descriptor_tmp.12.5995
+ __block_descriptor_tmp.12.6505
+ __block_descriptor_tmp.13.6755
+ __block_descriptor_tmp.14.3470
+ __block_descriptor_tmp.14.4668
+ __block_descriptor_tmp.14.5968
+ __block_descriptor_tmp.144.3799
+ __block_descriptor_tmp.15.5976
+ __block_descriptor_tmp.15.6167
+ __block_descriptor_tmp.15.6756
+ __block_descriptor_tmp.159.4860
+ __block_descriptor_tmp.16.4396
+ __block_descriptor_tmp.16.4436
+ __block_descriptor_tmp.17.3473
+ __block_descriptor_tmp.17.4279
+ __block_descriptor_tmp.17.6498
+ __block_descriptor_tmp.17.6758
+ __block_descriptor_tmp.18.4672
+ __block_descriptor_tmp.18.6512
+ __block_descriptor_tmp.18.6759
+ __block_descriptor_tmp.184.2857
+ __block_descriptor_tmp.19.4399
+ __block_descriptor_tmp.19.5969
+ __block_descriptor_tmp.19.6760
+ __block_descriptor_tmp.2.4341
+ __block_descriptor_tmp.2.6173
+ __block_descriptor_tmp.20.4448
+ __block_descriptor_tmp.20.5973
+ __block_descriptor_tmp.20.6764
+ __block_descriptor_tmp.209.5705
+ __block_descriptor_tmp.21.3475
+ __block_descriptor_tmp.21.5966
+ __block_descriptor_tmp.213.5800
+ __block_descriptor_tmp.22.4666
+ __block_descriptor_tmp.228.5707
+ __block_descriptor_tmp.24.3512
+ __block_descriptor_tmp.25.3431
+ __block_descriptor_tmp.25.5988
+ __block_descriptor_tmp.25.6752
+ __block_descriptor_tmp.27.3432
+ __block_descriptor_tmp.27.4664
+ __block_descriptor_tmp.2858
+ __block_descriptor_tmp.29.5986
+ __block_descriptor_tmp.3.4320
+ __block_descriptor_tmp.3.6002
+ __block_descriptor_tmp.3.6143
+ __block_descriptor_tmp.3.6500
+ __block_descriptor_tmp.3.7290
+ __block_descriptor_tmp.30.5985
+ __block_descriptor_tmp.31.3428
+ __block_descriptor_tmp.31.5984
+ __block_descriptor_tmp.32.5964
+ __block_descriptor_tmp.33.5982
+ __block_descriptor_tmp.3402
+ __block_descriptor_tmp.36.3409
+ __block_descriptor_tmp.3649
+ __block_descriptor_tmp.37.3424
+ __block_descriptor_tmp.37.4677
+ __block_descriptor_tmp.3722
+ __block_descriptor_tmp.39.4674
+ __block_descriptor_tmp.4.4438
+ __block_descriptor_tmp.4.4879
+ __block_descriptor_tmp.4.6003
+ __block_descriptor_tmp.4.6147
+ __block_descriptor_tmp.40.3421
+ __block_descriptor_tmp.41.4659
+ __block_descriptor_tmp.4281
+ __block_descriptor_tmp.4311
+ __block_descriptor_tmp.4338
+ __block_descriptor_tmp.44.4645
+ __block_descriptor_tmp.4434
+ __block_descriptor_tmp.4560
+ __block_descriptor_tmp.46.3478
+ __block_descriptor_tmp.46.4641
+ __block_descriptor_tmp.46.7210
+ __block_descriptor_tmp.47.5403
+ __block_descriptor_tmp.4717
+ __block_descriptor_tmp.49.4880
+ __block_descriptor_tmp.5.4441
+ __block_descriptor_tmp.5.4885
+ __block_descriptor_tmp.5.6004
+ __block_descriptor_tmp.50.4747
+ __block_descriptor_tmp.50.7203
+ __block_descriptor_tmp.51.4746
+ __block_descriptor_tmp.5169
+ __block_descriptor_tmp.52.4654
+ __block_descriptor_tmp.5391
+ __block_descriptor_tmp.5803
+ __block_descriptor_tmp.6.6151
+ __block_descriptor_tmp.6.6178
+ __block_descriptor_tmp.6.7160
+ __block_descriptor_tmp.604.4187
+ __block_descriptor_tmp.6136
+ __block_descriptor_tmp.6161
+ __block_descriptor_tmp.6216
+ __block_descriptor_tmp.6491
+ __block_descriptor_tmp.67.4720
+ __block_descriptor_tmp.6717
+ __block_descriptor_tmp.6770
+ __block_descriptor_tmp.6812
+ __block_descriptor_tmp.69.4721
+ __block_descriptor_tmp.6957
+ __block_descriptor_tmp.7.4309
+ __block_descriptor_tmp.7.4909
+ __block_descriptor_tmp.7.6154
+ __block_descriptor_tmp.70.4757
+ __block_descriptor_tmp.71.4753
+ __block_descriptor_tmp.7154
+ __block_descriptor_tmp.72.4751
+ __block_descriptor_tmp.7286
+ __block_descriptor_tmp.7522
+ __block_descriptor_tmp.7537
+ __block_descriptor_tmp.8.4307
+ __block_descriptor_tmp.8.4445
+ __block_descriptor_tmp.8.6493
+ __block_descriptor_tmp.9.4314
+ __block_descriptor_tmp.9.5992
+ __block_descriptor_tmp.92.4826
+ __block_descriptor_tmp.97.4798
+ __block_literal_global.12.6163
+ __block_literal_global.12.7166
+ __block_literal_global.14.6492
+ __block_literal_global.15.7408
+ __block_literal_global.17.6165
+ __block_literal_global.20.4670
+ __block_literal_global.22.6761
+ __block_literal_global.29.4662
+ __block_literal_global.3207
+ __block_literal_global.3399
+ __block_literal_global.3647
+ __block_literal_global.3763
+ __block_literal_global.39.3420
+ __block_literal_global.4.7401
+ __block_literal_global.43.6438
+ __block_literal_global.4439
+ __block_literal_global.4557
+ __block_literal_global.4883
+ __block_literal_global.5.6495
+ __block_literal_global.5390
+ __block_literal_global.5633
+ __block_literal_global.5971
+ __block_literal_global.599.4186
+ __block_literal_global.6030
+ __block_literal_global.6159
+ __block_literal_global.6212
+ __block_literal_global.6452
+ __block_literal_global.6715
+ __block_literal_global.6754
+ __block_literal_global.6954
+ __block_literal_global.7152
+ __block_literal_global.7284
+ __block_literal_global.7397
+ __block_literal_global.7520
+ __block_literal_global.7534
+ __block_literal_global.8.6176
+ __block_literal_global.8.7158
+ __block_literal_global.9.6037
+ _mdns_server_log.s_log.4443
+ _mdns_server_log.s_once.4442
+ g_session_list.4447
- FreeARElemCallback.2846
- GCC_except_table1051
- GCC_except_table1243
- GCC_except_table1437
- _FatalError
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6177
- ___mdns_server_log_block_invoke.4455
- __block_descriptor_tmp.1.6142
- __block_descriptor_tmp.10.4662
- __block_descriptor_tmp.10.6172
- __block_descriptor_tmp.10.7172
- __block_descriptor_tmp.11.4454
- __block_descriptor_tmp.11.5995
- __block_descriptor_tmp.11.6510
- __block_descriptor_tmp.12.5997
- __block_descriptor_tmp.12.6507
- __block_descriptor_tmp.13.6757
- __block_descriptor_tmp.14.3472
- __block_descriptor_tmp.14.4670
- __block_descriptor_tmp.14.5970
- __block_descriptor_tmp.144.3801
- __block_descriptor_tmp.15.5978
- __block_descriptor_tmp.15.6169
- __block_descriptor_tmp.15.6758
- __block_descriptor_tmp.159.4862
- __block_descriptor_tmp.16.4398
- __block_descriptor_tmp.16.4438
- __block_descriptor_tmp.17.3475
- __block_descriptor_tmp.17.4281
- __block_descriptor_tmp.17.6500
- __block_descriptor_tmp.17.6760
- __block_descriptor_tmp.18.4674
- __block_descriptor_tmp.18.6514
- __block_descriptor_tmp.18.6761
- __block_descriptor_tmp.184.2859
- __block_descriptor_tmp.19.4401
- __block_descriptor_tmp.19.5971
- __block_descriptor_tmp.19.6762
- __block_descriptor_tmp.2.4343
- __block_descriptor_tmp.2.6175
- __block_descriptor_tmp.20.4450
- __block_descriptor_tmp.20.5975
- __block_descriptor_tmp.20.6766
- __block_descriptor_tmp.209.5707
- __block_descriptor_tmp.21.3477
- __block_descriptor_tmp.21.5968
- __block_descriptor_tmp.213.5802
- __block_descriptor_tmp.22.4668
- __block_descriptor_tmp.228.5709
- __block_descriptor_tmp.24.3514
- __block_descriptor_tmp.25.3433
- __block_descriptor_tmp.25.5990
- __block_descriptor_tmp.25.6754
- __block_descriptor_tmp.27.3434
- __block_descriptor_tmp.27.4666
- __block_descriptor_tmp.2860
- __block_descriptor_tmp.29.5988
- __block_descriptor_tmp.3.4322
- __block_descriptor_tmp.3.6004
- __block_descriptor_tmp.3.6145
- __block_descriptor_tmp.3.6502
- __block_descriptor_tmp.3.7292
- __block_descriptor_tmp.30.5987
- __block_descriptor_tmp.31.3430
- __block_descriptor_tmp.31.5986
- __block_descriptor_tmp.32.5966
- __block_descriptor_tmp.33.5984
- __block_descriptor_tmp.3404
- __block_descriptor_tmp.36.3411
- __block_descriptor_tmp.3651
- __block_descriptor_tmp.37.3426
- __block_descriptor_tmp.37.4679
- __block_descriptor_tmp.3724
- __block_descriptor_tmp.39.4676
- __block_descriptor_tmp.4.4440
- __block_descriptor_tmp.4.4881
- __block_descriptor_tmp.4.6005
- __block_descriptor_tmp.4.6149
- __block_descriptor_tmp.40.3423
- __block_descriptor_tmp.41.4661
- __block_descriptor_tmp.4283
- __block_descriptor_tmp.4313
- __block_descriptor_tmp.4340
- __block_descriptor_tmp.44.4647
- __block_descriptor_tmp.4436
- __block_descriptor_tmp.4562
- __block_descriptor_tmp.46.3480
- __block_descriptor_tmp.46.4643
- __block_descriptor_tmp.46.7212
- __block_descriptor_tmp.47.5405
- __block_descriptor_tmp.4719
- __block_descriptor_tmp.49.4882
- __block_descriptor_tmp.5.4443
- __block_descriptor_tmp.5.4887
- __block_descriptor_tmp.5.6006
- __block_descriptor_tmp.50.4749
- __block_descriptor_tmp.50.7205
- __block_descriptor_tmp.51.4748
- __block_descriptor_tmp.5171
- __block_descriptor_tmp.52.4656
- __block_descriptor_tmp.5393
- __block_descriptor_tmp.5805
- __block_descriptor_tmp.6.6153
- __block_descriptor_tmp.6.6180
- __block_descriptor_tmp.6.7162
- __block_descriptor_tmp.604.4189
- __block_descriptor_tmp.6138
- __block_descriptor_tmp.6163
- __block_descriptor_tmp.6218
- __block_descriptor_tmp.6493
- __block_descriptor_tmp.67.4722
- __block_descriptor_tmp.6719
- __block_descriptor_tmp.6772
- __block_descriptor_tmp.6814
- __block_descriptor_tmp.69.4723
- __block_descriptor_tmp.6959
- __block_descriptor_tmp.7.4311
- __block_descriptor_tmp.7.4911
- __block_descriptor_tmp.7.6156
- __block_descriptor_tmp.70.4759
- __block_descriptor_tmp.71.4755
- __block_descriptor_tmp.7156
- __block_descriptor_tmp.72.4753
- __block_descriptor_tmp.7288
- __block_descriptor_tmp.7524
- __block_descriptor_tmp.7539
- __block_descriptor_tmp.8.4309
- __block_descriptor_tmp.8.4447
- __block_descriptor_tmp.8.6495
- __block_descriptor_tmp.9.4316
- __block_descriptor_tmp.9.5994
- __block_descriptor_tmp.92.4828
- __block_descriptor_tmp.97.4800
- __block_literal_global.12.6165
- __block_literal_global.12.7168
- __block_literal_global.14.6494
- __block_literal_global.15.7410
- __block_literal_global.17.6167
- __block_literal_global.20.4672
- __block_literal_global.22.6763
- __block_literal_global.29.4664
- __block_literal_global.3209
- __block_literal_global.3401
- __block_literal_global.3649
- __block_literal_global.3765
- __block_literal_global.39.3422
- __block_literal_global.4.7403
- __block_literal_global.43.6440
- __block_literal_global.4441
- __block_literal_global.4559
- __block_literal_global.4885
- __block_literal_global.5.6497
- __block_literal_global.5392
- __block_literal_global.5635
- __block_literal_global.5973
- __block_literal_global.599.4188
- __block_literal_global.6032
- __block_literal_global.6161
- __block_literal_global.6214
- __block_literal_global.6454
- __block_literal_global.6717
- __block_literal_global.6756
- __block_literal_global.6956
- __block_literal_global.7154
- __block_literal_global.7286
- __block_literal_global.7399
- __block_literal_global.7522
- __block_literal_global.7536
- __block_literal_global.8.6178
- __block_literal_global.8.7160
- __block_literal_global.9.6039
- _abort
- _mdns_server_log.s_log.4445
- _mdns_server_log.s_once.4444
- g_session_list.4449
CStrings:
+ "mDNSResponder-2200.140.11.701.1"
- "%s: %s"
- "ERROR: malloc"
- "mDNSResponder-2200.140.11"

```

#### ImageIOXPCService

>  `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

-2488.6.2.0.0
-  __TEXT.__text: 0x41dfec
-  __TEXT.__auth_stubs: 0x4250
+2488.7.2.0.0
+  __TEXT.__text: 0x41df2c
+  __TEXT.__auth_stubs: 0x4240
   __TEXT.__objc_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x310
   __TEXT.__gcc_except_tab: 0x1f710

   __TEXT.__objc_methtype: 0x5f1
   __TEXT.__oslogstring: 0x1ee
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xebc8
+  __TEXT.__unwind_info: 0xebc4
   __TEXT.__eh_frame: 0x1018
-  __DATA_CONST.__auth_got: 0x2140
+  __DATA_CONST.__auth_got: 0x2138
   __DATA_CONST.__got: 0x630
   __DATA_CONST.__auth_ptr: 0x90
   __DATA_CONST.__const: 0x706c8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 16132
-  Symbols:   10804
+  Symbols:   10803
   CStrings:  12658
 
Symbols:
- _CGColorSpaceCreateFromCICP

```

#### appleaccountd

>  `/usr/libexec/appleaccountd`

```diff

-981.23.1.0.0
-  __TEXT.__text: 0x275078
+981.23.2.0.0
+  __TEXT.__text: 0x275900
   __TEXT.__auth_stubs: 0x2300
   __TEXT.__objc_methlist: 0x620
   __TEXT.__objc_methname: 0x3d8a
   __TEXT.__objc_classname: 0x1e0
   __TEXT.__objc_methtype: 0x1261
-  __TEXT.__cstring: 0x1c484
+  __TEXT.__cstring: 0x1c4b4
   __TEXT.__swift5_typeref: 0x5a17
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0xb6c0

   __TEXT.__swift5_protos: 0x1b8
   __TEXT.__swift5_capture: 0x4c98
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5ab8
+  __TEXT.__unwind_info: 0x5ab4
   __TEXT.__eh_frame: 0x5688
   __DATA_CONST.__auth_got: 0x1180
   __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x430
-  __DATA_CONST.__const: 0x13568
+  __DATA_CONST.__const: 0x13560
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8227
+  Functions: 8231
   Symbols:   1080
-  CStrings:  3039
+  CStrings:  3040
 
CStrings:
+ "Invalid container ID received %s"

```

#### assessmentagent

>  `/usr/libexec/assessmentagent`

```diff

   __TEXT.__swift5_capture: 0xbb4
   __TEXT.__swift5_protos: 0x94
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3398
+  __TEXT.__unwind_info: 0x339c
   __TEXT.__eh_frame: 0x2f20
   __DATA_CONST.__auth_got: 0xe90
   __DATA_CONST.__got: 0x518

```

#### countryd

>  `/usr/libexec/countryd`

```diff

 47.0.3.0.0
-  __TEXT.__text: 0xa75c
-  __TEXT.__auth_stubs: 0x910
+  __TEXT.__text: 0xa8a4
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x27c
-  __TEXT.__const: 0xd8
-  __TEXT.__swift5_typeref: 0x152
+  __TEXT.__const: 0xb8
+  __TEXT.__swift5_typeref: 0x1a2
   __TEXT.__objc_methname: 0x97a
   __TEXT.__cstring: 0x70c
   __TEXT.__constg_swiftt: 0xb0

   __TEXT.__objc_methtype: 0x2a5
   __TEXT.__unwind_info: 0x334
   __TEXT.__eh_frame: 0x5b0
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__const: 0x378
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30

   __DATA.__objc_selrefs: 0x2c0
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x408
+  __DATA.__data: 0x420
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

```

#### AccessibilityAppIntents

>  `/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents`

```diff

-3093.32.11.0.0
-  __TEXT.__text: 0x4264
+3093.32.12.0.0
+  __TEXT.__text: 0x4514
   __TEXT.__auth_stubs: 0x470
   __TEXT.__const: 0x5e2
   __TEXT.__swift5_typeref: 0x2dc

   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1e4
+  __TEXT.__unwind_info: 0x1e8
   __TEXT.__eh_frame: 0x140
   __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x4c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x8

```

#### fileproviderd

>  `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

-1835.140.3.0.0
+1835.140.3.701.1
   __TEXT.__text: 0x850
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_stubs: 0x200
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x66
+  __TEXT.__const: 0x6e
   __TEXT.__cstring: 0xe1
   __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methname: 0x2aa

```

#### accessoryupdaterd

>  `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

   __TEXT.__auth_stubs: 0x1170
   __TEXT.__objc_stubs: 0x7540
   __TEXT.__objc_methlist: 0x3188
-  __TEXT.__cstring: 0xb84a
+  __TEXT.__cstring: 0xb858
   __TEXT.__objc_methname: 0x8a00
   __TEXT.__oslogstring: 0x4496
   __TEXT.__objc_classname: 0x685
CStrings:
+ "DawnSecurityCrystal"
- "DawnG"

```

#### EAUpdaterService

>  `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService`

```diff

   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__objc_stubs: 0x31e0
   __TEXT.__objc_methlist: 0xbe0
-  __TEXT.__cstring: 0x6b03
+  __TEXT.__cstring: 0x6b11
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__objc_methname: 0x3853
CStrings:
+ "DawnSecurityCrystal"
- "DawnG"

```

#### BackgroundShortcutRunner

>  `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

-2610.0.0.0.0
+2610.1.0.0.0
   __TEXT.__text: 0x148b0
   __TEXT.__auth_stubs: 0x980
   __TEXT.__objc_stubs: 0x4160

   __TEXT.__objc_classname: 0x274
   __TEXT.__objc_methtype: 0x162a
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__oslogstring: 0x16f6
+  __TEXT.__oslogstring: 0x16f8
   __TEXT.__ustring: 0x6a
   __TEXT.__unwind_info: 0x470
   __DATA_CONST.__auth_got: 0x4d0
CStrings:
+ "Shortcut %@ failed with error %{private}@."
+ "Shortcut %@ has finished running with output: %{private}@."
- "Shortcut %@ failed with error %{public}@."
- "Shortcut %@ has finished running with output: %{public}@."

```

#### assistantd

>  `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

   __TEXT.__objc_methlist: 0x1c59c
   __TEXT.__const: 0x10520
   __TEXT.__gcc_except_tab: 0x2ce4
-  __TEXT.__cstring: 0x4e320
+  __TEXT.__cstring: 0x4e321
   __TEXT.__objc_classname: 0x5049
   __TEXT.__objc_methname: 0x59aca
   __TEXT.__objc_methtype: 0xe8d3
CStrings:
+ "284"
- "18"

```

#### UARPUpdaterServiceLegacyAudio

>  `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio`

```diff

   __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_stubs: 0x4360
   __TEXT.__objc_methlist: 0x132c
-  __TEXT.__cstring: 0x817d
+  __TEXT.__cstring: 0x818b
   __TEXT.__const: 0x2c0
   __TEXT.__objc_methname: 0x4e82
   __TEXT.__objc_classname: 0x24e
CStrings:
+ "DawnSecurityCrystal"
- "DawnG"

```

#### gamed

>  `/usr/libexec/gamed`

```diff

-818.6.8.0.0
-  __TEXT.__text: 0x1f38dc
+818.6.8.2.1
+  __TEXT.__text: 0x1f3954
   __TEXT.__auth_stubs: 0x27b0
   __TEXT.__objc_stubs: 0x1a180
   __TEXT.__objc_methlist: 0xba7c

   __TEXT.__oslogstring: 0x12810
   __TEXT.__const: 0x10c30
   __TEXT.__gcc_except_tab: 0x29e4
-  __TEXT.__cstring: 0x1ad24
+  __TEXT.__cstring: 0x1ad34
   __TEXT.__objc_methname: 0x21a21
   __TEXT.__objc_methtype: 0x6626
   __TEXT.__swift5_typeref: 0xd0e

   __DATA_CONST.__got: 0xfd8
   __DATA_CONST.__auth_ptr: 0xb0
   __DATA_CONST.__const: 0x10fc8
-  __DATA_CONST.__cfstring: 0xcb80
+  __DATA_CONST.__cfstring: 0xcbc0
   __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0x200

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 8546
   Symbols:   1562
-  CStrings:  10313
+  CStrings:  10315
 
CStrings:
+ "http"
+ "https"

```

#### mobileassetd

>  `/usr/libexec/mobileassetd`

```diff

   __TEXT.__objc_stubs: 0xae0
   __TEXT.__objc_methlist: 0x1f8
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1698
+  __TEXT.__cstring: 0x16a6
   __TEXT.__gcc_except_tab: 0x1b4
   __TEXT.__objc_methname: 0x721
   __TEXT.__objc_classname: 0x29
CStrings:
+ "DawnSecurityCrystal"
+ "Starting mobileassetd built Jul 23 2024 14:54:38"
- "DawnG"
- "Starting mobileassetd built Jul 16 2024 21:21:39"

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.6.1 *(21G101)* | 618.3.11.10.5 |
| 17.7 *(21H16)* | 618.4.1.10.4 |

### Dylibs

#### ⬆️ Updated (59)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/VisionKit.framework/VisionKit](DYLIBS/VisionKit.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/Bom.framework/Bom](DYLIBS/Bom.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/CoreIK.framework/CoreIK](DYLIBS/CoreIK.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore](DYLIBS/IntentsCore.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SwiftNN.framework/SwiftNN](DYLIBS/SwiftNN.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoProcessors/STF.bundle/STF](DYLIBS/STF.md)
- [/usr/lib/libAppleArchive.dylib](DYLIBS/libAppleArchive.dylib.md)
- [/usr/lib/libParallelCompression.dylib](DYLIBS/libParallelCompression.dylib.md)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libmobileassetd.dylib](DYLIBS/libmobileassetd.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)

</details>

## EOF
