# 18.0 (22A5297f) .vs 18.0 (22A5307f)

## IPSWs

- `iPhone16,2_18.0_22A5297f_Restore.ipsw`
- `iPhone16,2_18.0_22A5307f_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.0 *(22A5297f)* | 24.0.0 | 11215.0.115.502.1~1 | Sun, 16Jun2024 20:49:29 PDT |
| 18.0 *(22A5307f)* | 24.0.0 | 11215.0.132.502.2~1 | Wed, 03Jul2024 20:40:06 PDT |

### Kexts

#### ⬆️ Updated (44)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.0.41.0.1
-  __TEXT.__cstring: 0x3aba
+1827.0.50.0.0
+  __TEXT.__cstring: 0x3ab6
   __TEXT.__const: 0x864
   __TEXT_EXEC.__text: 0x3d4f4
   __TEXT_EXEC.__auth_stubs: 0x0

```

>  `com.apple.iokit.IOGPUFamily`

```diff

-104.0.5.0.0
+104.0.6.0.0
   __TEXT.__cstring: 0x4faf
   __TEXT.__os_log: 0x387c
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x379c0
+  __TEXT_EXEC.__text: 0x37b28
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4b0
   __DATA.__common: 0x780

```

>  `com.apple.driver.AppleAVE2`

```diff

-802.37.1.0.0
-  __TEXT.__const: 0x28bb0
-  __TEXT.__cstring: 0x33491
-  __TEXT.__os_log: 0x3cb0a
-  __TEXT_EXEC.__text: 0x131e2c
+802.61.1.0.0
+  __TEXT.__const: 0x2e8a0
+  __TEXT.__cstring: 0x34c2c
+  __TEXT.__os_log: 0x3f71f
+  __TEXT_EXEC.__text: 0x13e4b8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x288
-  __DATA.__common: 0x108
-  __DATA.__bss: 0x300
+  __DATA.__data: 0x290
+  __DATA.__common: 0x130
+  __DATA.__bss: 0x560
   __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x30
-  __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x5c60
-  __DATA_CONST.__kalloc_type: 0x1e80
-  __DATA_CONST.__kalloc_var: 0x1310
+  __DATA_CONST.__mod_init_func: 0x38
+  __DATA_CONST.__mod_term_func: 0x38
+  __DATA_CONST.__const: 0x62a8
+  __DATA_CONST.__kalloc_type: 0x1f40
+  __DATA_CONST.__kalloc_var: 0x1090
   Symbols:   0
-  Functions: 2344
+  Functions: 2431
 

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.0.16.0.0
-  __TEXT.__cstring: 0x99f9
+938.0.19.0.0
+  __TEXT.__cstring: 0x9a86
   __TEXT.__const: 0x14b0
   __TEXT.__os_log: 0x233
-  __TEXT_EXEC.__text: 0x25f6c
+  __TEXT_EXEC.__text: 0x25f4c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x412
   __DATA.__common: 0xb0
   __DATA.__bss: 0x79
-  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__auth_got: 0x7b8
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x18

   __DATA_CONST.__kalloc_type: 0xec0
   __DATA_CONST.__kalloc_var: 0x1310
   Symbols:   0
-  Functions: 790
+  Functions: 791
 

```

>  `com.apple.driver.AppleSEPCredentialManager`

```diff

-758.0.14.0.0
-  __TEXT.__cstring: 0x10491
+758.0.16.0.0
+  __TEXT.__cstring: 0x10503
   __TEXT.__const: 0x320
-  __TEXT_EXEC.__text: 0x47fc4
+  __TEXT_EXEC.__text: 0x48090
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2bf1
   __DATA.__common: 0x1d8

   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x1400
   Symbols:   0
-  Functions: 897
+  Functions: 899
 

```

>  `com.apple.driver.AppleSMCWirelessCharger`

```diff

-76.0.0.0.0
+76.0.1.0.0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x28d3
+  __TEXT.__cstring: 0x2915
   __TEXT.__os_log: 0x4b9
-  __TEXT_EXEC.__text: 0xecc8
+  __TEXT_EXEC.__text: 0xef60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68

   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0x1e0
   Symbols:   0
-  Functions: 175
+  Functions: 180
 

```

>  `com.apple.AGXG16P`

```diff

-320.18.0.0.0
+320.23.0.0.0
   __TEXT.__const: 0x4444
-  __TEXT.__cstring: 0xca1b
+  __TEXT.__cstring: 0xca1f
   __TEXT.__os_log: 0x2f7
-  __TEXT_EXEC.__text: 0xae40c
+  __TEXT_EXEC.__text: 0xaea04
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13b8
   __DATA.__common: 0x10

```

>  `com.apple.driver.AppleOLYHAL`

```diff

-336.22.4.1.0
+337.0.0.0.0
   __TEXT.__const: 0x7a8
-  __TEXT.__cstring: 0x4826
-  __TEXT_EXEC.__text: 0x1c998
+  __TEXT.__cstring: 0x473a
+  __TEXT_EXEC.__text: 0x1ca58
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x1338
+  __DATA_CONST.__const: 0x1378
   __DATA_CONST.__kalloc_type: 0x640
   Symbols:   0
-  Functions: 548
+  Functions: 549
 

```

>  `com.apple.driver.AppleProResHW`

```diff

-400.59.1.0.0
-  __TEXT.__const: 0x1b48
-  __TEXT.__os_log: 0x7190
-  __TEXT.__cstring: 0xdb7
-  __TEXT_EXEC.__text: 0x182e8
+400.73.0.0.0
+  __TEXT.__const: 0x1b40
+  __TEXT.__os_log: 0x7318
+  __TEXT.__cstring: 0xdcc
+  __TEXT_EXEC.__text: 0x18950
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x358
   __DATA.__common: 0x70

   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 418
+  Functions: 425
 

```

>  `com.apple.driver.ApplePMGR`

```diff

-1555.0.15.0.0
+1555.0.17.0.0
   __TEXT.__const: 0x248
   __TEXT.__cstring: 0xe858
-  __TEXT_EXEC.__text: 0x527fc
+  __TEXT_EXEC.__text: 0x527f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x100
   __DATA.__common: 0x420

```

>  `com.apple.iokit.IOMIPIFamily`

```diff

-160.0.0.0.0
+160.0.1.0.0
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x1f5
-  __TEXT_EXEC.__text: 0x112c
+  __TEXT_EXEC.__text: 0x1148
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

```

>  `com.apple.security.sandbox`

```diff

-2401.0.37.502.1
-  __TEXT.__const: 0x18bd51
-  __TEXT.__cstring: 0x6e51
+2401.0.48.0.0
+  __TEXT.__const: 0x18cfc1
+  __TEXT.__cstring: 0x6ec0
   __TEXT.__os_log: 0x2029
-  __TEXT_EXEC.__text: 0x30468
+  __TEXT_EXEC.__text: 0x30438
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x144c0
-  __DATA_CONST.__auth_got: 0x828
+  __DATA.__bss: 0x144c8
+  __DATA_CONST.__auth_got: 0x830
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x3620
+  __DATA_CONST.__const: 0x3640
   __DATA_CONST.__kalloc_var: 0x550
   __DATA_CONST.__kalloc_type: 0xa80
   Symbols:   0
-  Functions: 648
+  Functions: 647
 

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-3.25.1.0.0
-  __TEXT.__cstring: 0x190ab
-  __TEXT.__os_log: 0x153bf
+3.28.1.0.0
+  __TEXT.__cstring: 0x190b9
+  __TEXT.__os_log: 0x153cb
   __TEXT.__const: 0xa060
   __TEXT_EXEC.__text: 0x95dfc
   __TEXT_EXEC.__auth_stubs: 0x0

```

>  `com.apple.driver.AppleIDV`

```diff

-7.34.0.0.0
+7.36.1.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x137b
+  __TEXT.__cstring: 0x137d
   __TEXT_EXEC.__text: 0x84b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-148.0.45.0.0
-  __TEXT.__cstring: 0x1661b
-  __TEXT.__const: 0x4f518
-  __TEXT_EXEC.__text: 0xd6390
+148.0.48.0.0
+  __TEXT.__cstring: 0x165cd
+  __TEXT.__const: 0x4ec98
+  __TEXT_EXEC.__text: 0xd6080
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1fe40
   __DATA.__common: 0x20a8

   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__mod_init_func: 0x570
   __DATA_CONST.__mod_term_func: 0x548
-  __DATA_CONST.__const: 0x21100
+  __DATA_CONST.__const: 0x210b8
   __DATA_CONST.__kalloc_type: 0x3c40
   __DATA_CONST.__kalloc_var: 0x500
   Symbols:   0
-  Functions: 6009
+  Functions: 6008
 

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-395.20.1.0.0
-  __TEXT.__cstring: 0x824b
+395.23.1.0.0
+  __TEXT.__cstring: 0x81b4
   __TEXT.__const: 0x800
-  __TEXT_EXEC.__text: 0x2256c
+  __TEXT_EXEC.__text: 0x2257c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2900
   __DATA.__common: 0x1c924

   __DATA_CONST.__const: 0x5e00
   __DATA_CONST.__kalloc_type: 0xac0
   Symbols:   0
-  Functions: 1134
+  Functions: 1133
 

```

>  `com.apple.kec.corecrypto`

```diff

-1736.0.27.0.1
-  __TEXT.__cstring: 0x46c3
-  __TEXT.__const: 0x144b0
+1736.0.36.0.0
+  __TEXT.__cstring: 0x46e7
+  __TEXT.__const: 0x14490
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x54a48
+  __TEXT_EXEC.__text: 0x58bfc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2df0
-  __DATA.__bss: 0x2960
-  __DATA.__common: 0x138
+  __DATA.__bss: 0x2980
+  __DATA.__common: 0x140
   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x2ba8
+  __DATA_CONST.__const: 0x2c90
   Symbols:   0
-  Functions: 1303
+  Functions: 1313
 

```

>  `com.apple.driver.AppleCallbackPowerSource`

```diff

-1730.0.0.0.2
-  __TEXT.__cstring: 0xf76
+1735.0.0.0.0
+  __TEXT.__cstring: 0xf8f
   __TEXT.__os_log: 0x76
-  __TEXT_EXEC.__text: 0x4b50
+  __TEXT_EXEC.__text: 0x4b98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x190
-  __DATA.__bss: 0x1408
+  __DATA.__bss: 0x1438
   __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x10

```

>  `com.apple.driver.AppleHIDTransport`

```diff

-8100.31.0.0.0
+8100.32.0.0.0
   __TEXT.__const: 0x2d4
-  __TEXT.__cstring: 0xab57
+  __TEXT.__cstring: 0xab70
   __TEXT.__os_log: 0x283
-  __TEXT_EXEC.__text: 0x69af4
+  __TEXT_EXEC.__text: 0x69dbc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x420

```

>  `com.apple.driver.AppleT8110DART`

```diff

-452.0.1.0.0
+452.0.2.0.0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x276b
-  __TEXT_EXEC.__text: 0xd390
+  __TEXT.__cstring: 0x27b4
+  __TEXT_EXEC.__text: 0xd458
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__kalloc_type: 0x2c0
   __DATA_CONST.__kalloc_var: 0x410
   Symbols:   0
-  Functions: 148
+  Functions: 149
 

```

>  `com.apple.driver.AppleStockholmControl`

```diff

-350.26.1.0.0
-  __TEXT.__cstring: 0x45c8
+350.28.0.0.0
+  __TEXT.__cstring: 0x46f8
   __TEXT.__const: 0x30
-  __TEXT_EXEC.__text: 0x14bf8
+  __TEXT_EXEC.__text: 0x14f0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x219
   __DATA.__common: 0x1a6

```

>  `com.apple.filesystems.apfs`

```diff

-2309.0.0.502.1
+2310.0.0.0.0
   __TEXT.__const: 0x790
-  __TEXT.__cstring: 0x48053
-  __TEXT_EXEC.__text: 0x13983c
+  __TEXT.__cstring: 0x48034
+  __TEXT_EXEC.__text: 0x1397d8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x690
   __DATA.__bss: 0xc60

   __DATA_CONST.__kalloc_type: 0x4c80
   __DATA_CONST.__kalloc_var: 0x2800
   Symbols:   0
-  Functions: 2261
+  Functions: 2262
 

```

>  `com.apple.driver.ASIOKit`

```diff

-12.26.0.0.0
+12.28.0.0.0
   __TEXT.__cstring: 0x239
-  __TEXT.__const: 0x7c40
-  __TEXT_EXEC.__text: 0x317e8
+  __TEXT.__const: 0x7c30
+  __TEXT_EXEC.__text: 0x30068
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x60

   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x3038
+  __DATA_CONST.__const: 0x2a08
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
   Functions: 88

```

>  `com.apple.driver.AppleBasebandPCI`

```diff

-809.0.0.0.0
-  __TEXT.__cstring: 0xc23c
+810.0.0.0.0
+  __TEXT.__cstring: 0xc286
   __TEXT.__const: 0x5009
-  __TEXT_EXEC.__text: 0x88670
+  __TEXT_EXEC.__text: 0x88dd0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3f8
   __DATA.__common: 0x648

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x1350
   __DATA_CONST.__mod_term_func: 0xf0
-  __DATA_CONST.__const: 0xfe98
+  __DATA_CONST.__const: 0xfeb8
   __DATA_CONST.__kalloc_type: 0x1d80
   __DATA_CONST.__kalloc_var: 0x690
   Symbols:   0
-  Functions: 2397
+  Functions: 2403
 

```

>  `com.apple.driver.AppleSARService`

```diff

-1168.0.0.0.0
+1172.0.0.0.0
   __TEXT.__const: 0x750
   __TEXT.__cstring: 0x9b1f
   __TEXT.__os_log: 0xb8af
   __TEXT.__ustring: 0x8
-  __TEXT_EXEC.__text: 0x53c84
+  __TEXT_EXEC.__text: 0x53e40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x5f0

   __DATA_CONST.__kalloc_type: 0x2940
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 538
+  Functions: 539
 

```

>  `com.apple.driver.AppleHPM`

```diff

-570.0.0.0.0
-  __TEXT.__cstring: 0x1b286
+570.0.1.0.0
+  __TEXT.__cstring: 0x1b2a1
   __TEXT.__const: 0xc0
   __TEXT.__os_log: 0x1e8
-  __TEXT_EXEC.__text: 0x5c3dc
+  __TEXT_EXEC.__text: 0x5c438
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6d0
   __DATA.__common: 0x518
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__auth_got: 0x4a0
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0xf8

```

>  `com.apple.driver.AppleHapticsSupportLEAP`

```diff

-9.19.0.0.0
+9.20.0.0.0
   __TEXT.__const: 0x204
-  __TEXT.__cstring: 0x4405
-  __TEXT.__os_log: 0x82e
-  __TEXT_EXEC.__text: 0x324c0
+  __TEXT.__cstring: 0x443a
+  __TEXT.__os_log: 0x88e
+  __TEXT_EXEC.__text: 0x33228
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x810
-  __DATA.__common: 0x5f0
+  __DATA.__common: 0x618
   __DATA.__bss: 0x1
   __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__mod_init_func: 0xb0
-  __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0x4778
-  __DATA_CONST.__kalloc_type: 0xac0
+  __DATA_CONST.__mod_init_func: 0xb8
+  __DATA_CONST.__mod_term_func: 0xc0
+  __DATA_CONST.__const: 0x4900
+  __DATA_CONST.__kalloc_type: 0xc00
   __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 922
+  Functions: 953
 

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-395.20.1.0.0
+395.23.1.0.0
   __TEXT.__cstring: 0x3ef5
   __TEXT.__const: 0x2148
-  __TEXT_EXEC.__text: 0x1faa8
+  __TEXT_EXEC.__text: 0x1fb60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe0
   __DATA.__common: 0x26d0

   __DATA_CONST.__const: 0x1628
   __DATA_CONST.__kalloc_type: 0x7c0
   Symbols:   0
-  Functions: 690
+  Functions: 693
 

```

>  `com.apple.driver.AppleConvergedIPCOLYBTControl`

```diff

-106.0.0.0.0
-  __TEXT.__cstring: 0x7b2d
+107.0.0.0.0
+  __TEXT.__cstring: 0x7ba9
   __TEXT.__const: 0x98
-  __TEXT_EXEC.__text: 0x47870
+  __TEXT_EXEC.__text: 0x479d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x4c58
+  __DATA_CONST.__const: 0x4c70
   __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x500
   Symbols:   0
-  Functions: 969
+  Functions: 971
 

```

>  `com.apple.driver.AppleConvergedPCI`

```diff

-106.0.0.0.0
+107.0.0.0.0
   __TEXT.__const: 0x1b0
   __TEXT.__cstring: 0x6ba1
-  __TEXT_EXEC.__text: 0x3e558
+  __TEXT_EXEC.__text: 0x3e594
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

   __DATA_CONST.__got: 0x108
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x4768
+  __DATA_CONST.__const: 0x4778
   __DATA_CONST.__kalloc_type: 0x1300
   Symbols:   0
-  Functions: 1067
+  Functions: 1069
 

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-8.13.2.0.0
-  __TEXT.__os_log: 0x30df1
-  __TEXT.__cstring: 0xaa49
-  __TEXT.__const: 0x5f0
-  __TEXT_EXEC.__text: 0xa0088
+8.15.1.0.0
+  __TEXT.__os_log: 0x31029
+  __TEXT.__cstring: 0xab3f
+  __TEXT.__const: 0x600
+  __TEXT_EXEC.__text: 0xa0a78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3058
   __DATA.__common: 0x3c8
   __DATA.__bss: 0x270
   __DATA_CONST.__auth_got: 0x878
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x98
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x6078
-  __DATA_CONST.__kalloc_type: 0x2c80
-  __DATA_CONST.__kalloc_var: 0x28a0
+  __DATA_CONST.__const: 0x6098
+  __DATA_CONST.__kalloc_type: 0x2d00
+  __DATA_CONST.__kalloc_var: 0x29e0
   Symbols:   0
-  Functions: 1821
+  Functions: 1824
 

```

>  `com.apple.driver.AppleMobileDispH16P-DCP`

```diff

-395.20.1.0.0
+395.23.1.0.0
   __TEXT.__cstring: 0x5565
   __TEXT.__const: 0x1a78
-  __TEXT_EXEC.__text: 0x20644
+  __TEXT_EXEC.__text: 0x2069c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0xf0

   __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 1105
+  Functions: 1108
 

```

>  `com.apple.driver.AppleProxDriver`

```diff

-41.0.0.0.0
+43.0.0.0.0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x826
+  __TEXT.__cstring: 0x855
   __TEXT.__os_log: 0x607
-  __TEXT_EXEC.__text: 0xa9c4
+  __TEXT_EXEC.__text: 0xa9a4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
+  __DATA.__data: 0xe0
   __DATA.__common: 0xd8
   __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0x78

```

>  `com.apple.driver.AppleT8130TypeCPhy`

```diff

-239.0.0.0.0
+239.0.1.0.0
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x81fb
   __TEXT.__os_log: 0xe07d
-  __TEXT_EXEC.__text: 0x4bf6c
+  __TEXT_EXEC.__text: 0x4bf80
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2c8
   __DATA.__common: 0x58

   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__const: 0x848
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 120
+  Functions: 122
 

```

>  `com.apple.driver.AppleTypeCPhy`

```diff

-239.0.0.0.0
+239.0.1.0.0
   __TEXT.__cstring: 0x1651
   __TEXT.__const: 0x24
   __TEXT.__os_log: 0x114c
-  __TEXT_EXEC.__text: 0x12538
+  __TEXT_EXEC.__text: 0x12570
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

   __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x1240
+  __DATA_CONST.__const: 0x1250
   __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 243
+  Functions: 245
 

```

>  `com.apple.filesystems.hfs.kext`

```diff

-670.0.0.0.0
+672.0.0.0.0
   __TEXT.__const: 0x1a90
   __TEXT.__cstring: 0xa072
-  __TEXT_EXEC.__text: 0x51aac
+  __TEXT_EXEC.__text: 0x51b2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

```

>  `com.apple.driver.AppleDCP`

```diff

-811.0.17.0.0
+811.0.20.0.0
   __TEXT.__cstring: 0x1664
   __TEXT.__const: 0x18
   __TEXT_EXEC.__text: 0x5e48

   __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x1438
+  __DATA_CONST.__const: 0x1430
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
   Functions: 175

```

>  `com.apple.driver.AppleFirmwareKit`

```diff

-531.0.4.0.0
-  __TEXT.__cstring: 0x27af
+531.0.7.0.0
+  __TEXT.__cstring: 0x4064
   __TEXT.__os_log: 0x1129
   __TEXT.__const: 0xa8
-  __TEXT_EXEC.__text: 0x36c24
+  __TEXT_EXEC.__text: 0x3acdc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3f8
   __DATA.__common: 0x700
   __DATA.__bss: 0xc8
-  __DATA_CONST.__auth_got: 0x428
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0xf0
   __DATA_CONST.__mod_term_func: 0xf0
-  __DATA_CONST.__const: 0xd348
+  __DATA_CONST.__const: 0xd318
   __DATA_CONST.__kalloc_type: 0x1880
   __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 1625
+  Functions: 1931
 

```

>  `com.apple.driver.AppleJPEGDriver`

```diff

-7.1.3.0.0
-  __TEXT.__os_log: 0xc16a
-  __TEXT.__cstring: 0x324f
+7.1.4.0.0
+  __TEXT.__os_log: 0xc20c
+  __TEXT.__cstring: 0x3545
   __TEXT.__const: 0x4534
-  __TEXT_EXEC.__text: 0x33b60
+  __TEXT_EXEC.__text: 0x343bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x8b08
   __DATA.__common: 0x2b8
   __DATA.__bss: 0x1
-  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x88
   __DATA_CONST.__mod_term_func: 0x88

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

-6767.0.0.0.0
-  __TEXT.__cstring: 0x32b44
+6769.0.0.0.0
+  __TEXT.__cstring: 0x32b45
   __TEXT.__os_log: 0x2db0c
   __TEXT.__const: 0x7f0
-  __TEXT_EXEC.__text: 0x18d158
+  __TEXT_EXEC.__text: 0x18d2bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
   __DATA.__common: 0x1238

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x3a0
   __DATA_CONST.__mod_term_func: 0x3a0
-  __DATA_CONST.__const: 0x1d988
+  __DATA_CONST.__const: 0x1d998
   __DATA_CONST.__kalloc_type: 0x1d40
   __DATA_CONST.__kalloc_var: 0xaf0
   Symbols:   0
-  Functions: 4756
+  Functions: 4758
 

```

>  `com.apple.kernel`

```diff

-11215.0.115.502.1
-  __TEXT.__const: 0x33b90
+11215.0.132.502.2
+  __TEXT.__const: 0x33ba0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x6b9b9
+  __TEXT.__cstring: 0x6b9cd
   __TEXT.__os_log: 0x26bed
   __TEXT.__eh_frame: 0x5a0
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7fa8f4
+  __TEXT_EXEC.__text: 0x7fb518
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x45329
+  __LINKINFO.__symbolsets: 0x453aa
   __LATE_CONST.__late_const: 0xa8
   Symbols:   0
-  Functions: 19818
+  Functions: 19823
 

```

>  `com.apple.driver.AppleSmartBatteryManagerEmbedded`

```diff

-1730.0.0.0.2
-  __TEXT.__cstring: 0x4456
-  __TEXT.__const: 0x15c0
+1735.0.0.0.0
+  __TEXT.__cstring: 0x447a
+  __TEXT.__const: 0x15f0
   __TEXT.__os_log: 0x25f9
-  __TEXT_EXEC.__text: 0x22824
+  __TEXT_EXEC.__text: 0x228a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x208
   __DATA.__common: 0x150
-  __DATA.__bss: 0x3170
+  __DATA.__bss: 0x31d0
   __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__mod_init_func: 0x40

```

>  `com.apple.driver.FairPlayIOKit`

```diff

 72.8.0.0.0
   __TEXT.__cstring: 0x1c95
-  __TEXT.__const: 0x49a20
-  __TEXT_EXEC.__text: 0x1ad63c
+  __TEXT.__const: 0x49c10
+  __TEXT_EXEC.__text: 0x1b0660
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12e0
-  __DATA.__common: 0x5fd0
+  __DATA.__common: 0x5fd8
   __DATA.__bss: 0x38
   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x139e0
+  __DATA_CONST.__const: 0x13860
   __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x370
   Symbols:   0
-  Functions: 438
+  Functions: 461
 

```

>  `com.apple.iokit.IOSurface`

```diff

-368.0.2.0.0
-  __TEXT.__cstring: 0x4f14
+368.0.4.0.0
+  __TEXT.__cstring: 0x4f28
   __TEXT.__const: 0x48
-  __TEXT.__os_log: 0x530
-  __TEXT_EXEC.__text: 0x2d228
+  __TEXT.__os_log: 0x4ff
+  __TEXT_EXEC.__text: 0x2d340
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x178
   __DATA.__common: 0x3e8
-  __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0x468
+  __DATA.__bss: 0x38
+  __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78

   __DATA_CONST.__kalloc_type: 0xb80
   __DATA_CONST.__kalloc_var: 0x8c0
   Symbols:   0
-  Functions: 1191
+  Functions: 1193
 

```

</details>

## MachO

### 🆕 NEW (4)

- `/Applications/CompanionSetup.app/CompanionSetup`
- `/System/Library/ExtensionKit/Extensions/SettingsSOSAppIntentsExtension.appex/SettingsSOSAppIntentsExtension`
- `/System/Library/PrivateFrameworks/ExchangeSync.framework/PlugIns/SyncDiagnostics.appex/SyncDiagnostics`
- `/System/Library/PrivateFrameworks/ImagePlayground.framework/PlugIns/com.apple.ImagePlayground.DiagnosticExtension.appex/com.apple.ImagePlayground.DiagnosticExtension`

### ❌ Removed (3)

- `/System/Library/PrivateFrameworks/ImageGenerationUI.framework/PlugIns/com.apple.ImageGenerationUI.DiagnosticExtension.appex/com.apple.ImageGenerationUI.DiagnosticExtension`
- `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/XPCServices/ModelCatalogCompilationService.xpc/ModelCatalogCompilationService`
- `/usr/libexec/silhouette`

### ⬆️ Updated (894)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AAUIViewService.app/AAUIViewService](MACHOS/AAUIViewService.md)
- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService.md)
- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService](MACHOS/AppleIDSetupUIService.md)
- [/Applications/AskPermissionUI.app/AskPermissionUI](MACHOS/AskPermissionUI.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AutoSettings.app/AutoSettings](MACHOS/AutoSettings.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/CarPlayWallpaper.app/CarPlayWallpaper](MACHOS/CarPlayWallpaper.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/DDActionsService.app/DDActionsService](MACHOS/DDActionsService.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsService.app/DiagnosticsService](MACHOS/DiagnosticsService.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-0001.appex/Diagnostic-0001](MACHOS/Diagnostic-0001.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3909.appex/Diagnostic-3909](MACHOS/Diagnostic-3909.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939](MACHOS/Diagnostic-3939.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4579.appex/Diagnostic-4579](MACHOS/Diagnostic-4579.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6000.appex/Diagnostic-6000](MACHOS/Diagnostic-6000.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6006.appex/Diagnostic-6006](MACHOS/Diagnostic-6006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079](MACHOS/Diagnostic-8079.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201](MACHOS/Diagnostic-8201.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253](MACHOS/Diagnostic-8253.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262](MACHOS/Diagnostic-8262.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288](MACHOS/Diagnostic-8288.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8290-EFD.appex/Diagnostic-8290-EFD](MACHOS/Diagnostic-8290-EFD.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389](MACHOS/Diagnostic-8389.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FeedbackRemoteView.app/FeedbackRemoteView](MACHOS/FeedbackRemoteView.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HealthENLauncher.app/HealthENLauncher](MACHOS/HealthENLauncher.md)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/InputUI.app/InputUI](MACHOS/InputUI.md)
- [/Applications/LimitedAccessPromptView.app/LimitedAccessPromptView](MACHOS/LimitedAccessPromptView.md)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MediaRemoteUIService.app/MediaRemoteUIService](MACHOS/MediaRemoteUIService.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MobileSMS.app/MobileSMS](MACHOS/MobileSMS.md)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosFileProvider.appex/PhotosFileProvider](MACHOS/PhotosFileProvider.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates](MACHOS/PhotosNotificationsUpdates.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension](MACHOS/PeerPaymentMessagesExtension.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/PosterBoard.app/PosterBoard](MACHOS/PosterBoard.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/ProximityReaderUIService.app/ProximityReaderUIService](MACHOS/ProximityReaderUIService.md)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter.md)
- [/Applications/SMS Filter.app/SMS Filter](MACHOS/SMS_Filter.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/Screen Time.app/Screen Time](MACHOS/Screen_Time.md)
- [/Applications/ScreenContinuityShell.app/ScreenContinuityShell](MACHOS/ScreenContinuityShell.md)
- [/Applications/ScreenTimeUnlock.app/ScreenTimeUnlock](MACHOS/ScreenTimeUnlock.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/Spotlight.app/Spotlight](MACHOS/Spotlight.md)
- [/Applications/StickerPickerService.app/StickerPickerService](MACHOS/StickerPickerService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StoreDemoViewService.app/StoreDemoViewService](MACHOS/StoreDemoViewService.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVRemoteUIService.app/PlugIns/TVRemoteIntentExtension.appex/TVRemoteIntentExtension](MACHOS/TVRemoteIntentExtension.md)
- [/Applications/TVRemoteUIService.app/PlugIns/TVRemoteWidgetExtension.appex/TVRemoteWidgetExtension](MACHOS/TVRemoteWidgetExtension.md)
- [/Applications/TVRemoteUIService.app/TVRemoteUIService](MACHOS/TVRemoteUIService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer](MACHOS/AXHapticMusicServer.md)
- [/System/Library/AccessibilityBundles/AXIDSServer.axuiservice/AXIDSServer](MACHOS/AXIDSServer.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/AXUltronPluginService.axuiservice/AXUltronPluginService](MACHOS/AXUltronPluginService.md)
- [/System/Library/AccessibilityBundles/AXWatchRemoteScreenUIServer.axuiservice/AXWatchRemoteScreenUIServer](MACHOS/AXWatchRemoteScreenUIServer.md)
- [/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer](MACHOS/ClarityUIServer.md)
- [/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer](MACHOS/GAXBackboardServer.md)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer.md)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/NTKCustomization.axbundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion](MACHOS/NanoTimeKitCompanion.md)
- [/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer](MACHOS/SpeakServer.md)
- [/System/Library/AccessibilityBundles/SpeakThis.axuiservice/SpeakThis](MACHOS/SpeakThis.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/AccessibilityBundles/WidgetRenderer.axbundle/WidgetRenderer](MACHOS/WidgetRenderer.md)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow.md)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner](MACHOS/JournalDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/PassbookDataclassOwnerPlugin.bundle/PassbookDataclassOwnerPlugin](MACHOS/PassbookDataclassOwnerPlugin.md)
- [/System/Library/Accounts/Notification/ASDAccountNotificationPlugin.bundle/ASDAccountNotificationPlugin](MACHOS/ASDAccountNotificationPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge.md)
- [/System/Library/Assistant/UIPlugins/AddressBook.siriUIBundle/AddressBook](MACHOS/AddressBook.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/NetworkUplinkClock.driver/NetworkUplinkClock](MACHOS/NetworkUplinkClock.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule](MACHOS/ReplayKitModule.md)
- [/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule](MACHOS/VideoConferenceControlCenterModule.md)
- [/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting](MACHOS/CIInpainting.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_archive_bin.metallib](MACHOS/portrait_filters_archive_bin.metallib.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer](MACHOS/AccessibilityUIServer.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents](MACHOS/AccessibilityAppIntents.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/scrod](MACHOS/scrod.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/appplaceholdersyncd](MACHOS/appplaceholdersyncd.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration](MACHOS/AccessibilityDataMigration.md)
- [/System/Library/DataClassMigrators/CookieDataMigrator.migrator/CookieDataMigrator](MACHOS/CookieDataMigrator.md)
- [/System/Library/DataClassMigrators/KeyboardMigrator.migrator/KeyboardMigrator](MACHOS/KeyboardMigrator.md)
- [/System/Library/DataClassMigrators/MCProfile.migrator/MCProfile](MACHOS/MCProfile.md)
- [/System/Library/DataClassMigrators/iTunesStore.migrator/iTunesStore](MACHOS/iTunesStore.md)
- [/System/Library/DistributedEvaluation/Plugins/AutocorrectionTesterDESPlugin.desPlugin/AutocorrectionTesterDESPlugin](MACHOS/AutocorrectionTesterDESPlugin.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AudiovisualThumbnailExtension.appex/AudiovisualThumbnailExtension](MACHOS/AudiovisualThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/CalendarThumbnailExtension.appex/CalendarThumbnailExtension](MACHOS/CalendarThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension](MACHOS/CameraSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ClassKitAppIntents.appex/ClassKitAppIntents](MACHOS/ClassKitAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents](MACHOS/DeveloperSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension](MACHOS/DevicePropertiesExtension.md)
- [/System/Library/ExtensionKit/Extensions/DoNotDisturbAppIntents.appex/DoNotDisturbAppIntents](MACHOS/DoNotDisturbAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension](MACHOS/ExperimentationExtension.md)
- [/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension](MACHOS/GPUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents](MACHOS/GeneralSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/IFTelemetrySELFIngestor.appex/IFTelemetrySELFIngestor](MACHOS/IFTelemetrySELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/IntelligenceIntentsExtension.appex/IntelligenceIntentsExtension](MACHOS/IntelligenceIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/InternationalSettingsExtension.appex/InternationalSettingsExtension](MACHOS/InternationalSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/MKRemoteUI](MACHOS/MKRemoteUI.md)
- [/System/Library/ExtensionKit/Extensions/MailSettingsIntentsExtension.appex/MailSettingsIntentsExtension](MACHOS/MailSettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension](MACHOS/MetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/OfficeThumbnailExtension.appex/OfficeThumbnailExtension](MACHOS/OfficeThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/PersonalHotspotControlExtension.appex/PersonalHotspotControlExtension](MACHOS/PersonalHotspotControlExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivacyAppIntents.appex/PrivacyAppIntents](MACHOS/PrivacyAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService](MACHOS/PrivateMLClientInferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/QuickLookUIExtension.appex/QuickLookUIExtension](MACHOS/QuickLookUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/SearchAnalyticsWorker.appex/SearchAnalyticsWorker](MACHOS/SearchAnalyticsWorker.md)
- [/System/Library/ExtensionKit/Extensions/SettingsCellularAppIntentsExtension.appex/SettingsCellularAppIntentsExtension](MACHOS/SettingsCellularAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsIntents.appex/SoftwareUpdateSettingsIntents](MACHOS/SoftwareUpdateSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension](MACHOS/WiFiSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension](MACHOS/ZeoliteExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.hfs.appex/com.apple.fskit.hfs](MACHOS/com.apple.fskit.hfs.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Extensions/ASIOKit.kext/ASIOKit](MACHOS/ASIOKit.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/slurpAPFSMeta](MACHOS/slurpAPFSMeta.md)
- [/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService](MACHOS/AVAudioDeviceTestService.md)
- [/System/Library/Frameworks/Accounts.framework/accountsd](MACHOS/accountsd.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/CFNetwork.framework/AuthBrokerAgent](MACHOS/AuthBrokerAgent.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetworkAgent](MACHOS/CFNetworkAgent.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/ClassKit.framework/progressd](MACHOS/progressd.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService](MACHOS/LimitedLibraryPickerViewService.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService](MACHOS/ContactsButtonXPCService.md)
- [/System/Library/Frameworks/CoreImage.framework/coreui_archive_bin.metallib](MACHOS/coreui_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/photo_style_archive_bin.metallib](MACHOS/photo_style_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin](MACHOS/CoreLocationNumberedMapCalloutPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/GNSSLocationService.xpc/GNSSLocationService](MACHOS/GNSSLocationService.md)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice](MACHOS/eedmediaservice.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/ctkd](MACHOS/ctkd.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd](MACHOS/fileproviderd.md)
- [/System/Library/Frameworks/IdentityLookup.framework/XPCServices/com.apple.IdentityLookup.MessageFilter.xpc/com.apple.IdentityLookup.MessageFilter](MACHOS/com.apple.IdentityLookup.MessageFilter.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc](MACHOS/icprefd-xpc.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc](MACHOS/mscamerad-xpc.md)
- [/System/Library/Frameworks/ImageIO.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM](MACHOS/ModuleACM.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd](MACHOS/applicensedeliveryd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/MessageUI.framework/PlugIns/MessageUI.wkbundle/MessageUI](MACHOS/MessageUI.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/ApplePayDiagnostics.appex/ApplePayDiagnostics](MACHOS/ApplePayDiagnostics.md)
- [/System/Library/Frameworks/QuickLook.framework/PlugIns/com.apple.quicklook.extension.previewUI.appex/com.apple.quicklook.extension.previewUI](MACHOS/com.apple.quicklook.extension.previewUI.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/SensorKit.framework/PlugIns/SensorKitViewService.appex/SensorKitViewService](MACHOS/SensorKitViewService.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitDataExport.xpc/SensorKitDataExport](MACHOS/SensorKitDataExport.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/Translation.framework/translationd](MACHOS/translationd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter](MACHOS/AppleProxServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter](MACHOS/GamepadHIDServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/SafetyServiceFilter.plugin/SafetyServiceFilter](MACHOS/SafetyServiceFilter.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/DualSenseHIDServicePlugin](MACHOS/DualSenseHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/DualShock4HIDServicePlugin](MACHOS/DualShock4HIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/GenericGamepadHIDServicePlugin](MACHOS/GenericGamepadHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService](MACHOS/HSTouchHIDService.md)
- [/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/JoyConHIDServicePlugin](MACHOS/JoyConHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/LunaHIDServicePlugin](MACHOS/LunaHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxGamepadHIDServicePlugin.plugin/XboxGamepadHIDServicePlugin](MACHOS/XboxGamepadHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin](MACHOS/XboxOneHIDServicePlugin.md)
- [/System/Library/Health/Plugins/HealthActivityCache.bundle/HealthActivityCache](MACHOS/HealthActivityCache.md)
- [/System/Library/Health/Plugins/HealthBluetoothPeripheral.bundle/HealthBluetoothPeripheral](MACHOS/HealthBluetoothPeripheral.md)
- [/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin](MACHOS/HealthRecordsPlugin.md)
- [/System/Library/LocationBundles/AltimeterHarvest.bundle/AltimeterHarvest](MACHOS/AltimeterHarvest.md)
- [/System/Library/LocationBundles/AppGenius.bundle/AppGenius](MACHOS/AppGenius.md)
- [/System/Library/LocationBundles/CompassCalibration.bundle/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/LocationBundles/IonosphereHarvest.bundle/IonosphereHarvest](MACHOS/IonosphereHarvest.md)
- [/System/Library/LocationBundles/LocationFenceSync.bundle/LocationFenceSync](MACHOS/LocationFenceSync.md)
- [/System/Library/LocationBundles/LocationPromptUI.bundle/LocationPromptUI](MACHOS/LocationPromptUI.md)
- [/System/Library/LocationBundles/MotionCalibration.bundle/MotionCalibration](MACHOS/MotionCalibration.md)
- [/System/Library/LocationBundles/PLAMonitor.bundle/PLAMonitor](MACHOS/PLAMonitor.md)
- [/System/Library/LocationBundles/TimeZone.bundle/TimeZone](MACHOS/TimeZone.md)
- [/System/Library/LocationBundles/Traffic.bundle/Traffic](MACHOS/Traffic.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/SMS](MACHOS/SMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/FindMyMessagesApp](MACHOS/FindMyMessagesApp.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/RichLinkProvider.bundle/RichLinkProvider](MACHOS/RichLinkProvider.md)
- [/System/Library/NanoPreferenceBundles/Applications/DoseSettings.bundle/DoseSettings](MACHOS/DoseSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/HeartRateSettings.bundle/HeartRateSettings](MACHOS/HeartRateSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/MindSettings.bundle/MindSettings](MACHOS/MindSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoBedtimeBridgeSettings.bundle/NanoBedtimeBridgeSettings](MACHOS/NanoBedtimeBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoHealthBalanceBridgeSettings.bundle/NanoHealthBalanceBridgeSettings](MACHOS/NanoHealthBalanceBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPhotosBridgeSettings.bundle/NanoPhotosBridgeSettings](MACHOS/NanoPhotosBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/SessionTrackerAppSettings.bundle/SessionTrackerAppSettings](MACHOS/SessionTrackerAppSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings](MACHOS/CSLCompanionLiveActivitiesSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CellularBridgeSettings.bundle/CellularBridgeSettings](MACHOS/CellularBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoPhotosBridgeSetup.bundle/NanoPhotosBridgeSetup](MACHOS/NanoPhotosBridgeSetup.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColtanFaceBundleCompanion.bundle/NTKColtanFaceBundleCompanion](MACHOS/NTKColtanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUltraCubeFaceBundleCompanion.bundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUtilityFaceBundleCompanion.bundle/NTKUtilityFaceBundleCompanion](MACHOS/NTKUtilityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings](MACHOS/AirPlayAndHandoffSettings.md)
- [/System/Library/PreferenceBundles/AppClipDeveloperSettings.bundle/AppClipDeveloperSettings](MACHOS/AppClipDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings](MACHOS/ContactsSettings.md)
- [/System/Library/PreferenceBundles/ControlCenterSettings.bundle/ControlCenterSettings](MACHOS/ControlCenterSettings.md)
- [/System/Library/PreferenceBundles/CoreRoutineSettings.bundle/CoreRoutineSettings](MACHOS/CoreRoutineSettings.md)
- [/System/Library/PreferenceBundles/DigitalSeparationSettings.bundle/DigitalSeparationSettings](MACHOS/DigitalSeparationSettings.md)
- [/System/Library/PreferenceBundles/FitnessSettings.bundle/FitnessSettings](MACHOS/FitnessSettings.md)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings.md)
- [/System/Library/PreferenceBundles/FontSettings.bundle/FontSettings](MACHOS/FontSettings.md)
- [/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings](MACHOS/HearingSettings.md)
- [/System/Library/PreferenceBundles/HomeScreenSettings.bundle/HomeScreenSettings](MACHOS/HomeScreenSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MobileCalSettings.bundle/MobileCalSettings](MACHOS/MobileCalSettings.md)
- [/System/Library/PreferenceBundles/MobileMailSettings.bundle/MobileMailSettings](MACHOS/MobileMailSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/NewsSettings.bundle/NewsSettings](MACHOS/NewsSettings.md)
- [/System/Library/PreferenceBundles/NotesSettings.bundle/NotesSettings](MACHOS/NotesSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PassbookSettings.bundle/PassbookSettings](MACHOS/PassbookSettings.md)
- [/System/Library/PreferenceBundles/PhonebookTelephonySettings.bundle/PhonebookTelephonySettings](MACHOS/PhonebookTelephonySettings.md)
- [/System/Library/PreferenceBundles/Privacy/ClipServicesSettings.bundle/ClipServicesSettings](MACHOS/ClipServicesSettings.md)
- [/System/Library/PreferenceBundles/Privacy/HealthPrivacySettings.bundle/HealthPrivacySettings](MACHOS/HealthPrivacySettings.md)
- [/System/Library/PreferenceBundles/Privacy/SensorKitPrivacySettings.bundle/SensorKitPrivacySettings](MACHOS/SensorKitPrivacySettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings.md)
- [/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings](MACHOS/SOSSettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PodcastsUsagePlugin.bundle/PodcastsUsagePlugin](MACHOS/PodcastsUsagePlugin.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/TVSettings.bundle/TVSettings](MACHOS/TVSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountSettings.bundle/VideoSubscriberAccountSettings](MACHOS/VideoSubscriberAccountSettings.md)
- [/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings](MACHOS/VoiceControlSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceBundles/WeatherSettings.bundle/WeatherSettings](MACHOS/WeatherSettings.md)
- [/System/Library/PreferenceBundles/WiFiSettings.bundle/WiFiSettings](MACHOS/WiFiSettings.md)
- [/System/Library/PreferenceManifests/ScreenTimeSettingsSearch.bundle/ScreenTimeSettingsSearch](MACHOS/ScreenTimeSettingsSearch.md)
- [/System/Library/PreferencesSyncBundles/CoreLocationSync.bundle/CoreLocationSync](MACHOS/CoreLocationSync.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd](MACHOS/motiontrackingd.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/AfibBurden.framework/PlugIns/AfibBurdenDiagnosticExtension.appex/AfibBurdenDiagnosticExtension](MACHOS/AfibBurdenDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension](MACHOS/AAUIFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService](MACHOS/AppleDeviceQueryService.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService](MACHOS/ANECompilerService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer](MACHOS/ANEStorageMaintainer.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail](MACHOS/ASVAssetThumbnail.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension](MACHOS/AKFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed](MACHOS/biomed.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd](MACHOS/bookassetd.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/ShutterLiquid.metallib](MACHOS/ShutterLiquid.metallib.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/Support/nebulad](MACHOS/nebulad.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/companionmessagesd](MACHOS/companionmessagesd.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd](MACHOS/com.apple.sbd.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent](MACHOS/contactsdonationagent.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech](MACHOS/com.apple.siri.embeddedspeech.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/PlugIns/FollowUpSampleExtension.appex/FollowUpSampleExtension](MACHOS/FollowUpSampleExtension.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/XPCServices/TilesService.xpc/TilesService](MACHOS/TilesService.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/PlugIns/SearchPoirotExtension.appex/SearchPoirotExtension](MACHOS/SearchPoirotExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd](MACHOS/speechmodeltrainingd.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool](MACHOS/suggest_tool.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub](MACHOS/DTServiceHub.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent](MACHOS/LeakAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/RemoteInjectionAgent](MACHOS/RemoteInjectionAgent.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension](MACHOS/AirPlayDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/NearbydDiagnosticExtension.appex/NearbydDiagnosticExtension](MACHOS/NearbydDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.B389.appex/com.apple.DiagnosticExtensions.B389](MACHOS/com.apple.DiagnosticExtensions.B389.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/DragUI.framework/Support/druid](MACHOS/druid.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/Support/devicedataresetd](MACHOS/devicedataresetd.md)
- [/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/PlugIns/EventMetaDataExtractorPlugin.appex/EventMetaDataExtractorPlugin](MACHOS/EventMetaDataExtractorPlugin.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS](MACHOS/DraftingExtension-iOS.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/XPCServices/FinHealthXPCServices.xpc/FinHealthXPCServices](MACHOS/FinHealthXPCServices.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond](MACHOS/revisiond.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/PlugIns/GenerativeModelsDiagnostics.appex/GenerativeModelsDiagnostics](MACHOS/GenerativeModelsDiagnostics.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd](MACHOS/generativeexperiencesd.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/MapsOfflineService.bundle/MapsOfflineService](MACHOS/MapsOfflineService.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed](MACHOS/homed.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent](MACHOS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd](MACHOS/intelligencecontextd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd](MACHOS/intelligenceflowd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/ERMLRuntimePlugin.appex/ERMLRuntimePlugin](MACHOS/ERMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension](MACHOS/ManagedSettingsExtension.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd](MACHOS/mapspushd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/nanomapscd](MACHOS/nanomapscd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/Support/mediaartworkd](MACHOS/mediaartworkd.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/XPCServices/MetricMeasurementHelper.xpc/MetricMeasurementHelper](MACHOS/MetricMeasurementHelper.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleEmbeddedAccessoryUpdaterService.xpc/AppleEmbeddedAccessoryUpdaterService](MACHOS/AppleEmbeddedAccessoryUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU](MACHOS/UARPUpdaterServiceDFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBFollowUpExtension.appex/MBFollowUpExtension](MACHOS/MBFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension](MACHOS/MBPrebuddyFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterRecordingUpdater.xpc/SessionFilterRecordingUpdater](MACHOS/SessionFilterRecordingUpdater.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond](MACHOS/nanotimekitcompaniond.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService](MACHOS/NFUIService.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool](MACHOS/com.apple.PrintKit.PrinterTool.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd](MACHOS/privacyaccountingd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Reconstruction_Gpu_Archive.metallib](MACHOS/Reconstruction_Gpu_Archive.metallib.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent](MACHOS/RemoteManagementAgent.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/InteractiveLegacyProfilesSubscriber.xpc/InteractiveLegacyProfilesSubscriber](MACHOS/InteractiveLegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/LegacyProfilesSubscriber.xpc/LegacyProfilesSubscriber](MACHOS/LegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber](MACHOS/ManagedAppsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PasscodeSettingsSubscriber.xpc/PasscodeSettingsSubscriber](MACHOS/PasscodeSettingsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SecuritySubscriber.xpc/SecuritySubscriber](MACHOS/SecuritySubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd](MACHOS/remotemanagementd.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientTool](MACHOS/smbclientTool.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd](MACHOS/smbclientd.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper](MACHOS/STSXPCHelper.md)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/Support/schooltimed](MACHOS/schooltimed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd](MACHOS/liveactivitiesd.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/budd](MACHOS/budd.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourEngagementExtension.appex/SeymourEngagementExtension](MACHOS/SeymourEngagementExtension.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced](MACHOS/siriinferenced.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent](MACHOS/SiriTTSTrainingAgent.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd](MACHOS/softwareupdateservicesd.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent](MACHOS/StatusKitAgent.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/Support/storebookkeeperd](MACHOS/storebookkeeperd.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd](MACHOS/syncdefaultsd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/PlugIns/SiriAUSP.appex/SiriAUSP](MACHOS/SiriAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/PlugIns/MauiAUSP.appex/MauiAUSP](MACHOS/MauiAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/PlugIns/VoiceBankingDiagnostics.appex/VoiceBankingDiagnostics](MACHOS/VoiceBankingDiagnostics.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd](MACHOS/usernotificationsd.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/Plugins.bundle/Plugins](MACHOS/Plugins.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/voiced](MACHOS/voiced.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd](MACHOS/siriactionsd.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd](MACHOS/webprivacyd.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService](MACHOS/ZhuGeService.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd](MACHOS/icloudsubscriptionoptimizerd.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/PlugIns/LighthousePlugin.appex/LighthousePlugin](MACHOS/LighthousePlugin.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PhoneSuggestions.bundle/PhoneSuggestions](MACHOS/PhoneSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/AudioUIPlugin](MACHOS/AudioUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ContactsFlowUIPlugin.bundle/ContactsFlowUIPlugin](MACHOS/ContactsFlowUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/FindMyUIPlugin.bundle/FindMyUIPlugin](MACHOS/FindMyUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriInferenceFlowsUIPlugin.bundle/SiriInferenceFlowsUIPlugin](MACHOS/SiriInferenceFlowsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/SiriKitUIPlugin](MACHOS/SiriKitUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriLinkUIPlugin.bundle/SiriLinkUIPlugin](MACHOS/SiriLinkUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriPaymentsUIPlugin.bundle/SiriPaymentsUIPlugin](MACHOS/SiriPaymentsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSuggestionsUIPlugin.bundle/SiriSuggestionsUIPlugin](MACHOS/SiriSuggestionsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriVideoUIPlugin.bundle/SiriVideoUIPlugin](MACHOS/SiriVideoUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin](MACHOS/StoreDemoPlugin.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient](MACHOS/eapolclient.md)
- [/System/Library/Trace/Providers/Required.bundle/Required](MACHOS/Required.md)
- [/System/Library/UsageBundles/MusicUsage.bundle/MusicUsage](MACHOS/MusicUsage.md)
- [/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA](MACHOS/MobileBackupUEA.md)
- [/System/Library/UserEventPlugins/com.apple.nsurlsessiond.plugin/com.apple.nsurlsessiond](MACHOS/com.apple.nsurlsessiond.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeEnabledNotifications.bundle/com.apple.ScreenTimeEnabledNotifications](MACHOS/com.apple.ScreenTimeEnabledNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/CCPortrait.bundle/ccportrait_archive_bin.metallib](MACHOS/ccportrait_archive_bin.metallib.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/AppleTV.app/AppleTV](MACHOS/AppleTV.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary](MACHOS/BKLibrary.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BookEPUBWebProcessPlugin.bundle/BookEPUBWebProcessPlugin](MACHOS/BookEPUBWebProcessPlugin.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension](MACHOS/BooksProductPageExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Bridge.app/PlugIns/BridgeWidgetExtension.appex/BridgeWidgetExtension](MACHOS/BridgeWidgetExtension.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension](MACHOS/FreeformWidgetKitExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/Home](MACHOS/Home.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents](MACHOS/GenerativePlaygroundAppIntents.md)
- [/private/var/staged_system_apps/Image Playground.app/Image Playground](MACHOS/Image_Playground.md)
- [/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension](MACHOS/GenerativePlaygroundMessagesAppExtension.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Magnifier.app/Magnifier](MACHOS/Magnifier.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.IntentsExtension.appex/com.apple.mobilenotes.IntentsExtension](MACHOS/com.apple.mobilenotes.IntentsExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SpotlightIndexExtension.appex/com.apple.mobilenotes.SpotlightIndexExtension](MACHOS/com.apple.mobilenotes.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/MobileTimer](MACHOS/MobileTimer.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passwords.app/Passwords](MACHOS/Passwords.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/IMDebug.framework/IMDebug](MACHOS/IMDebug.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsNotification.appex/TipsNotification](MACHOS/TipsNotification.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount](MACHOS/mount.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/brctl](MACHOS/brctl.md)
- [/usr/bin/fileproviderctl](MACHOS/fileproviderctl.md)
- [/usr/bin/footprint](MACHOS/footprint.md)
- [/usr/bin/modelmanagerdump](MACHOS/modelmanagerdump.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/bin/sysdiagnose](MACHOS/sysdiagnose.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libCoreLSKD.dylib](MACHOS/libCoreLSKD.dylib.md)
- [/usr/lib/libLogRedirect.dylib](MACHOS/libLogRedirect.dylib.md)
- [/usr/lib/libMainThreadChecker.dylib](MACHOS/libMainThreadChecker.dylib.md)
- [/usr/lib/libViewDebuggerSupport.dylib](MACHOS/libViewDebuggerSupport.dylib.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/lib/swift/libswiftRemoteMirror.dylib](MACHOS/libswiftRemoteMirror.dylib.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/DataDetectorsSourceAccess](MACHOS/DataDetectorsSourceAccess.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/FinishRestoreFromBackup](MACHOS/FinishRestoreFromBackup.md)
- [/usr/libexec/MTLAssetUpgraderD](MACHOS/MTLAssetUpgraderD.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/PreboardService](MACHOS/PreboardService.md)
- [/usr/libexec/SavageUtil](MACHOS/SavageUtil.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/ViewHierarchyAgent](MACHOS/ViewHierarchyAgent.md)
- [/usr/libexec/YonkersUtil](MACHOS/YonkersUtil.md)
- [/usr/libexec/adprivacyd](MACHOS/adprivacyd.md)
- [/usr/libexec/airplayd](MACHOS/airplayd.md)
- [/usr/libexec/amfid](MACHOS/amfid.md)
- [/usr/libexec/aned](MACHOS/aned.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/aonsensed](MACHOS/aonsensed.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/appprotectiond](MACHOS/appprotectiond.md)
- [/usr/libexec/asd](MACHOS/asd.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced.md)
- [/usr/libexec/batterytrapd](MACHOS/batterytrapd.md)
- [/usr/libexec/betaenrollmentd](MACHOS/betaenrollmentd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/brookcompaniond](MACHOS/brookcompaniond.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/ciphermld](MACHOS/ciphermld.md)
- [/usr/libexec/coordinated](MACHOS/coordinated.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/demod_helper](MACHOS/demod_helper.md)
- [/usr/libexec/diagnosticextensionsd](MACHOS/diagnosticextensionsd.md)
- [/usr/libexec/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/facemetricsd](MACHOS/facemetricsd.md)
- [/usr/libexec/fairplaydeviceidentityd](MACHOS/fairplaydeviceidentityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmybeaconingd](MACHOS/findmybeaconingd.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/fskitd](MACHOS/fskitd.md)
- [/usr/libexec/gamecontrollerd](MACHOS/gamecontrollerd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/griddatad](MACHOS/griddatad.md)
- [/usr/libexec/handwritingd](MACHOS/handwritingd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/inputanalyticsd](MACHOS/inputanalyticsd.md)
- [/usr/libexec/installd](MACHOS/installd.md)
- [/usr/libexec/keybagd](MACHOS/keybagd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/locationpushd](MACHOS/locationpushd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/lskdd](MACHOS/lskdd.md)
- [/usr/libexec/mediasetupd](MACHOS/mediasetupd.md)
- [/usr/libexec/metrickitd](MACHOS/metrickitd.md)
- [/usr/libexec/microstackshot](MACHOS/microstackshot.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mlruntimed](MACHOS/mlruntimed.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobile_installation_proxy](MACHOS/mobile_installation_proxy.md)
- [/usr/libexec/mobile_obliterator](MACHOS/mobile_obliterator.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nexusd](MACHOS/nexusd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/ospredictiond](MACHOS/ospredictiond.md)
- [/usr/libexec/passcodenagd](MACHOS/passcodenagd.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/pipelined](MACHOS/pipelined.md)
- [/usr/libexec/pkd](MACHOS/pkd.md)
- [/usr/libexec/powerexperienced](MACHOS/powerexperienced.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/relatived](MACHOS/relatived.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remoted](MACHOS/remoted.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/restoreserviced](MACHOS/restoreserviced.md)
- [/usr/libexec/rsync/rsync.openrsync](MACHOS/rsync.openrsync.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seld](MACHOS/seld.md)
- [/usr/libexec/sensorkitd](MACHOS/sensorkitd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/siriknowledged](MACHOS/siriknowledged.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/storagedatad](MACHOS/storagedatad.md)
- [/usr/libexec/storagekitd](MACHOS/storagekitd.md)
- [/usr/libexec/swcd](MACHOS/swcd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/symptomsd](MACHOS/symptomsd.md)
- [/usr/libexec/symptomsd-helper](MACHOS/symptomsd-helper.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/sysstatuscheck](MACHOS/sysstatuscheck.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/teslad](MACHOS/teslad.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/timed](MACHOS/timed.md)
- [/usr/libexec/transitd](MACHOS/transitd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tvremoted](MACHOS/tvremoted.md)
- [/usr/libexec/uarppersonalizationd](MACHOS/uarppersonalizationd.md)
- [/usr/libexec/videosubscriptionsd](MACHOS/videosubscriptionsd.md)
- [/usr/libexec/wifiFirmwareLoader](MACHOS/wifiFirmwareLoader.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/otctl](MACHOS/otctl.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (15)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H16.im4p

>  `AppleAVE2FW_H16.im4p`

```diff

 
-  __TEXT.__text: 0xc8410
-  __TEXT.__cstring: 0x124a3
-  __TEXT.__const: 0x1e9c0
+  __TEXT.__text: 0xc9560
+  __TEXT.__cstring: 0x12657
+  __TEXT.__const: 0x1f660
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x320
   __TEXT.__constructor: 0x0
-  __DATA.__const: 0x2190
-  __DATA.__data: 0x12e8
+  __DATA.__const: 0x2890
+  __DATA.__data: 0x1238
   __DATA._rtk_patchbay: 0x1e8
   __DATA._rtk_init_stack: 0x10000
   __DATA._rtk_irq_stack: 0x1000

   __DATA._rtk_threads: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xc68b8
-  Symbols:   1443
+  Symbols:   1453
   Functions: 0
 

```

#### SmartIOFirmware_ASCv6.im4p

>  `SmartIOFirmware_ASCv6.im4p`

```diff

 
-  __TEXT.__text: 0x1a9b8
+  __TEXT.__text: 0x1a9c8
   __TEXT.__cstring: 0x1087
   __TEXT.__const: 0x318
   __TEXT._rtk_mtab: 0x290

```

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

 
-  __TEXT.__text: 0x970cec
+  __TEXT.__text: 0x984550
   __TEXT.__data_copy: 0x100000
-  __TEXT.__const: 0x7f9470
-  __TEXT.__cstring: 0x1262ef
+  __TEXT.__const: 0x7fa830
+  __TEXT.__cstring: 0x12746d
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x507ac
   __TEXT.__eh_frame: 0x308
-  __DATA.__const: 0x51f30
+  __DATA.__const: 0x52ee8
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xdf108
+  __DATA.__data: 0xdf0b8
   __DATA._rtk_power: 0x3a8
   __DATA._rtk_patchbay: 0x218
   __DATA._rtk_init_stack: 0x2000

```

#### agx_a000.bin

>  `agx_a000.bin`

```diff

 
-  __TEXT.__text: 0x5a9d0
-  __TEXT.__gxf_code: 0x106c
+  __TEXT.__text: 0x5b298
+  __TEXT.__gxf_shr_code: 0x554
+  __TEXT.__gxf_code: 0x1024
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x1e20
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__gxf_shr_code: 0x554
   __TEXT.__cstring: 0x1e51
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x390
   __DATA.__gxf_data: 0x41f0
   __DATA.__data: 0xdf8
-  __DATA.__const: 0x530
+  __DATA.__const: 0x548
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__xnu_shared: 0x3c000
-  __DATA.__zerofill: 0x670d8
+  __DATA.__zerofill: 0x670f8
   Symbols:   208
   Functions: 0
 

```

#### agx_b000.bin

>  `agx_b000.bin`

```diff

 
-  __TEXT.__text: 0x5a6d4
-  __TEXT.__gxf_code: 0x106c
+  __TEXT.__text: 0x5af9c
+  __TEXT.__gxf_shr_code: 0x554
+  __TEXT.__gxf_code: 0x1024
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x1e60
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__gxf_shr_code: 0x554
   __TEXT.__cstring: 0x1e51
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x390
   __DATA.__gxf_data: 0x41f0
   __DATA.__data: 0xdf8
-  __DATA.__const: 0x530
+  __DATA.__const: 0x548
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__xnu_shared: 0x3c000
-  __DATA.__zerofill: 0x66f58
+  __DATA.__zerofill: 0x66f78
   Symbols:   208
   Functions: 0
 

```

#### agx_b100.bin

>  `agx_b100.bin`

```diff

 
-  __TEXT.__text: 0x5a6d4
-  __TEXT.__gxf_code: 0x106c
+  __TEXT.__text: 0x5af9c
+  __TEXT.__gxf_shr_code: 0x554
+  __TEXT.__gxf_code: 0x1024
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x1e60
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__gxf_shr_code: 0x554
   __TEXT.__cstring: 0x1e51
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x390
   __DATA.__gxf_data: 0x41f0
   __DATA.__data: 0xdf8
-  __DATA.__const: 0x530
+  __DATA.__const: 0x548
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__xnu_shared: 0x3c000
-  __DATA.__zerofill: 0x66f58
+  __DATA.__zerofill: 0x66f78
   Symbols:   208
   Functions: 0
 

```

#### ansf.t8130.release.im4p

>  `ansf.t8130.release.im4p`

```diff

 
-  __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x171c7c
+  __TEXT.text_first: 0x4488
+  __TEXT.__text: 0x172564
   __TEXT.shared: 0xb6e4
   __TEXT.read: 0x5a78
-  __TEXT.__const: 0x8e68
+  __TEXT.__const: 0x9088
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e59a
+  __TEXT.__cstring: 0x1e5ce
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
-  __DATA.core_globals: 0x138
-  __DATA.__zerofill: 0x19b788
+  __DATA.core_globals: 0x139
+  __DATA.__zerofill: 0x19bd38
   Symbols:   0
   Functions: 0
 

```

#### aopfw-iphone16aop.RELEASE.im4p

>  `aopfw-iphone16aop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0x12fde8
-  __TEXT.__const: 0x11db8
-  __TEXT.__cstring: 0x81e1
+  __TEXT.__text: 0x12ff1c
+  __TEXT.__const: 0x11da8
+  __TEXT.__cstring: 0x81e0
   __TEXT.__chain_starts: 0x50
   __TEXT.__eh_frame: 0x40
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xd0b70
-  __ETEXT.__StaticInit: 0x764c
+  __DATA.__zerofill: 0xd0c90
+  __ETEXT.__StaticInit: 0x7688
   __ETEXT.__text: 0x396c8
   __ETEXT.__const: 0xdce
   __EDATA.__data: 0x60
-  __OS_LOG.__string: 0x276f6
+  __OS_LOG.__string: 0x27724
   __MISC.__apf_list: 0xb0
   __CMA.__cma_log_string: 0x3df8
   Symbols:   0

```

#### h16x_ane_fw_iaso_d8x.im4p

>  `h16x_ane_fw_iaso_d8x.im4p`

```diff

 
-  __TEXT.__text: 0xaeb14
+  __TEXT.__text: 0xaeb24
   __TEXT.__data_copy: 0x8000
   __TEXT.__const: 0xc380
-  __TEXT.__cstring: 0x1ae76
+  __TEXT.__cstring: 0x1ae7d
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x28
-  __DATA.__const: 0x4bb8
+  __DATA.__const: 0x4bc8
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xf58
   __DATA._rtk_power: 0x368

```

#### rans.t8130.release.im4p

>  `rans.t8130.release.im4p`

```diff

 
-  __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x171c7c
+  __TEXT.text_first: 0x4488
+  __TEXT.__text: 0x172564
   __TEXT.shared: 0xb6e4
   __TEXT.read: 0x5a78
-  __TEXT.__const: 0x8e68
+  __TEXT.__const: 0x9088
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e59a
+  __TEXT.__cstring: 0x1e5ce
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
-  __DATA.core_globals: 0x138
-  __DATA.__zerofill: 0x19b788
+  __DATA.core_globals: 0x139
+  __DATA.__zerofill: 0x19bd38
   Symbols:   0
   Functions: 0
 

```

#### sptm.t8122.release.im4p

>  `sptm.t8122.release.im4p`

```diff

-392.0.26.0.0
-  __TEXT.__cstring: 0xc184
+392.0.31.0.1
+  __TEXT.__cstring: 0xc1c4
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x6c
   __TEXT.__const: 0x9d0
   __DATA_CONST.__const: 0x5990
   __LATE_CONST.__late_const: 0x5d5e0
-  __TEXT_EXEC.__text: 0x47228
+  __TEXT_EXEC.__text: 0x4742c
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6
   __DATA.__common: 0x73d0
-  __DATA.__bss: 0x5bf0
+  __DATA.__bss: 0x5c00
   __BOOTDATA.__data: 0x14000
   Symbols:   1
   Functions: 0

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2e24d8
-  __TEXT.__const: 0x7cebc
-  __TEXT.__cstring: 0x30d44
+  __TEXT.__text: 0x2ddbf4
+  __TEXT.__const: 0x7ceb4
+  __TEXT.__cstring: 0x30d64
   __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x4a400
+  __DATA.__const: 0x4a3f8
   __DATA._rtk_patchbay: 0x710
   __DATA._rtk_data_uuid: 0x40
-  __DATA.__data: 0x2b53c
+  __DATA.__data: 0x2b524
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA.__mod_init_func: 0x88
   __DATA._afk_sys_objt: 0xbb0
   __DATA._rtk_mtab: 0x5c8
-  __DATA.__zerofill: 0x9f210
-  __OS_LOG.__string: 0x20f69
+  __DATA.__zerofill: 0x9b210
+  __OS_LOG.__string: 0x20f90
   Symbols:   0
   Functions: 0
 

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2e24d8
-  __TEXT.__const: 0x7cebc
-  __TEXT.__cstring: 0x30d44
+  __TEXT.__text: 0x2ddbf4
+  __TEXT.__const: 0x7ceb4
+  __TEXT.__cstring: 0x30d64
   __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x4a400
+  __DATA.__const: 0x4a3f8
   __DATA._rtk_patchbay: 0x710
   __DATA._rtk_data_uuid: 0x40
-  __DATA.__data: 0x2b53c
+  __DATA.__data: 0x2b524
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA.__mod_init_func: 0x88
   __DATA._afk_sys_objt: 0xbb0
   __DATA._rtk_mtab: 0x5c8
-  __DATA.__zerofill: 0x9f210
-  __OS_LOG.__string: 0x20f69
+  __DATA.__zerofill: 0x9b210
+  __OS_LOG.__string: 0x20f90
   Symbols:   0
   Functions: 0
 

```

#### t8130pmp.im4p

>  `t8130pmp.im4p`

```diff

 
-  __TEXT.__text: 0x370d0
+  __TEXT.__text: 0x370d4
   __TEXT.__const: 0x2310
   __TEXT.__cstring: 0x1634
   __TEXT.__chain_starts: 0x0

```

#### txm.iphoneos.release.im4p

>  `txm.iphoneos.release.im4p`

```diff

-135.0.5.0.1
+135.0.6.0.1
   __TEXT.__cstring: 0x5781
   __TEXT.__const: 0x4210
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x20
-  __TEXT.__info_plist: 0x500
+  __TEXT.__info_plist: 0x508
   __DATA_CONST.__auth_ptr: 0x50
   __DATA_CONST.__const: 0x7c98
-  __TEXT_EXEC.__text: 0x3f1dc
+  __TEXT_EXEC.__text: 0x3f28c
   __TEXT_BOOT_EXEC.__text: 0x4058
   __TEXT_BOOT_EXEC.__bootcode: 0x2c
   __DATA.__data: 0x278

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.0 *(22A5297f)* | 619.1.18.10.1 |
| 18.0 *(22A5307f)* | 619.1.20.10.1 |

### Dylibs

#### 🆕 NEW (11)

- `/System/Library/AccessibilityBundles/HeadphoneProxService.axbundle/HeadphoneProxService`
- `/System/Library/Frameworks/_SwiftUICore.framework/_SwiftUICore`
- `/System/Library/PrivateFrameworks/CallHistoryToolKit.framework/CallHistoryToolKit`
- `/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils`
- `/System/Library/PrivateFrameworks/DSContinuityPairing.framework/DSContinuityPairing`
- `/System/Library/PrivateFrameworks/ImagePlayground.framework/ImagePlayground`
- `/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus`
- `/System/Library/PrivateFrameworks/TestHook.framework/TestHook`
- `/System/Library/PrivateFrameworks/TestHookService.framework/TestHookService`
- `/System/Library/PrivateFrameworks/TestHookShared.framework/TestHookShared`
- `/System/Library/PrivateFrameworks/VisualIntelligenceStream.framework/VisualIntelligenceStream`

#### ❌ Removed (3)

- `/System/Library/PrivateFrameworks/CoreChartSwift.framework/CoreChartSwift`
- `/System/Library/PrivateFrameworks/CoreSpeechGazeTracking.framework/CoreSpeechGazeTracking`
- `/System/Library/PrivateFrameworks/ImageGenerationUI.framework/ImageGenerationUI`

#### ⬆️ Updated (1596)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider](DYLIBS/ASMessagesProvider.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/Library/AccessibilityBundles/AcousticId-Assistant.axbundle/AcousticId-Assistant](DYLIBS/AcousticId-Assistant.md)
- [/System/Library/AccessibilityBundles/AirPlayMirroringModule.axbundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule.md)
- [/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension](DYLIBS/AppInstallExtension.md)
- [/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore](DYLIBS/AppStore.md)
- [/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade](DYLIBS/Arcade.md)
- [/System/Library/AccessibilityBundles/AvatarUI.axbundle/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/BarcodeScanner.axbundle/BarcodeScanner](DYLIBS/BarcodeScanner.md)
- [/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension](DYLIBS/BridgeStoreExtension.md)
- [/System/Library/AccessibilityBundles/CameraEditKitFramework.axbundle/CameraEditKitFramework](DYLIBS/CameraEditKitFramework.md)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/ConnectivityModule.axbundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/AccessibilityBundles/ContactsUI.axbundle/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/AccessibilityBundles/ConversationKit.axbundle/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/AccessibilityBundles/DisplayAndBrightnessSettings.axbundle/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/EventKitUIFramework](DYLIBS/EventKitUIFramework.md)
- [/System/Library/AccessibilityBundles/FlightUtilities.axbundle/FlightUtilities](DYLIBS/FlightUtilities.md)
- [/System/Library/AccessibilityBundles/FocusUIModule.axbundle/FocusUIModule](DYLIBS/FocusUIModule.md)
- [/System/Library/AccessibilityBundles/HeadphoneConfigs.axbundle/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/AccessibilityBundles/HealthExperienceUI.axbundle/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/AccessibilityBundles/HealthMedicationsUI.axbundle/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/AccessibilityBundles/HomeUI.axbundle/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/AccessibilityBundles/HomeUIService.axbundle/HomeUIService](DYLIBS/HomeUIService.md)
- [/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework](DYLIBS/MapKitFramework.md)
- [/System/Library/AccessibilityBundles/Maps.axbundle/Maps](DYLIBS/Maps.md)
- [/System/Library/AccessibilityBundles/Measure.axbundle/Measure](DYLIBS/Measure.md)
- [/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/AccessibilityBundles/MenstrualCyclesAppPlugin.axbundle/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/MessageUIFramework](DYLIBS/MessageUIFramework.md)
- [/System/Library/AccessibilityBundles/MobileCal.axbundle/MobileCal](DYLIBS/MobileCal.md)
- [/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail](DYLIBS/MobileMail.md)
- [/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone](DYLIBS/MobilePhone.md)
- [/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/AccessibilityBundles/Movies-Assistant.axbundle/Movies-Assistant](DYLIBS/Movies-Assistant.md)
- [/System/Library/AccessibilityBundles/Music.axbundle/Music](DYLIBS/Music.md)
- [/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication](DYLIBS/MusicApplication.md)
- [/System/Library/AccessibilityBundles/NFCControlCenterModule.axbundle/NFCControlCenterModule](DYLIBS/NFCControlCenterModule.md)
- [/System/Library/AccessibilityBundles/NotificationsSettings.axbundle/NotificationsSettings](DYLIBS/NotificationsSettings.md)
- [/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/AccessibilityBundles/PosterKit.axbundle/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/AccessibilityBundles/PreferencesFramework.axbundle/PreferencesFramework](DYLIBS/PreferencesFramework.md)
- [/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension](DYLIBS/ProductPageExtension.md)
- [/System/Library/AccessibilityBundles/QuickSpeak.bundle/QuickSpeak](DYLIBS/QuickSpeak.md)
- [/System/Library/AccessibilityBundles/ScreenshotServicesService.axbundle/ScreenshotServicesService](DYLIBS/ScreenshotServicesService.md)
- [/System/Library/AccessibilityBundles/SearchUI.axbundle/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/AccessibilityBundles/SleepHealthAppPlugin.axbundle/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardFoundation.axbundle/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/TVMLKit.axbundle/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/AccessibilityBundles/TelephonyUIFramework.axbundle/TelephonyUIFramework](DYLIBS/TelephonyUIFramework.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/AccessibilityBundles/VectorKit.axbundle/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore](DYLIBS/WebCore.md)
- [/System/Library/AccessibilityBundles/iCloudSettings.axbundle/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication](DYLIBS/AppleIDAuthentication.md)
- [/System/Library/Accounts/Authentication/GoogleAuthenticationPlugin.bundle/GoogleAuthenticationPlugin](DYLIBS/GoogleAuthenticationPlugin.md)
- [/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/NotesAccountNotificationPlugin](DYLIBS/NotesAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PassbookAccountNotificationPlugin.bundle/PassbookAccountNotificationPlugin](DYLIBS/PassbookAccountNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityHeadphoneLevelsControlCenterModule.bundle/AccessibilityHeadphoneLevelsControlCenterModule](DYLIBS/AccessibilityHeadphoneLevelsControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityLiveListenControlCenterModule.bundle/AccessibilityLiveListenControlCenterModule](DYLIBS/AccessibilityLiveListenControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityMotionCuesControlCenterModule.bundle/AccessibilityMotionCuesControlCenterModule](DYLIBS/AccessibilityMotionCuesControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityShorcutsModule.bundle/AccessibilityShorcutsModule](DYLIBS/AccessibilityShorcutsModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule.md)
- [/System/Library/ControlCenter/Bundles/BackgroundSoundsCCModule.bundle/BackgroundSoundsCCModule](DYLIBS/BackgroundSoundsCCModule.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule](DYLIBS/DisplayModule.md)
- [/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule](DYLIBS/FlashlightModule.md)
- [/System/Library/ControlCenter/Bundles/HeadphoneAccommodationsCCModule.bundle/HeadphoneAccommodationsCCModule](DYLIBS/HeadphoneAccommodationsCCModule.md)
- [/System/Library/ControlCenter/Bundles/HearingAidsModule.bundle/HearingAidsModule](DYLIBS/HearingAidsModule.md)
- [/System/Library/ControlCenter/Bundles/HearingDevicesCCModule.bundle/HearingDevicesCCModule](DYLIBS/HearingDevicesCCModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterSingleTileModule.bundle/HomeControlCenterSingleTileModule](DYLIBS/HomeControlCenterSingleTileModule.md)
- [/System/Library/ControlCenter/Bundles/MediaControlsAudioModule.bundle/MediaControlsAudioModule](DYLIBS/MediaControlsAudioModule.md)
- [/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule](DYLIBS/TVRemoteModule.md)
- [/System/Library/ControlCenter/Bundles/TimerModule.bundle/TimerModule](DYLIBS/TimerModule.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/CoreServices/RawCamera.bundle/RawCamera](DYLIBS/RawCamera.md)
- [/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator](DYLIBS/MessagesDataMigrator.md)
- [/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0](DYLIBS/AGXMetalG16P_A0.md)
- [/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0](DYLIBS/AGXMetalG16P_B0.md)
- [/System/Library/Fitness/Plugins/SeymourAwardsPlugin.bundle/SeymourAwardsPlugin](DYLIBS/SeymourAwardsPlugin.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib.md)
- [/System/Library/Frameworks/Accounts.framework/Accounts](DYLIBS/Accounts.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit](DYLIBS/AdAttributionKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency](DYLIBS/AppTrackingTransparency.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies](DYLIBS/AACDependencies.md)
- [/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets](DYLIBS/BackgroundAssets.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Cinematic.framework/Cinematic](DYLIBS/Cinematic.md)
- [/System/Library/Frameworks/ClassKit.framework/ClassKit](DYLIBS/ClassKit.md)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/ColorSync.framework/ColorSync](DYLIBS/ColorSync.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactProvider.framework/ContactProvider](DYLIBS/ContactProvider.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI](DYLIBS/CoreLocationUI.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable](DYLIBS/CoreTransferable.md)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit](DYLIBS/CryptoTokenKit.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/DeviceDiscoveryExtension.framework/DeviceDiscoveryExtension](DYLIBS/DeviceDiscoveryExtension.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit](DYLIBS/ExtensionKit.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameController.framework/GameController](DYLIBS/GameController.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore](DYLIBS/ImageCaptureCore.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/JournalingSuggestions.framework/JournalingSuggestions](DYLIBS/JournalingSuggestions.md)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI](DYLIBS/LocalAuthenticationEmbeddedUI.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MatterSupport.framework/MatterSupport](DYLIBS/MatterSupport.md)
- [/System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility](DYLIBS/MediaAccessibility.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX.md)
- [/System/Library/Frameworks/MetalKit.framework/MetalKit](DYLIBS/MetalKit.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/MPSImage](DYLIBS/MPSImage.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/MPSRayIntersector](DYLIBS/MPSRayIntersector.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage](DYLIBS/NaturalLanguage.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/Frameworks/PHASE.framework/PHASE](DYLIBS/PHASE.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/Social.framework/Social](DYLIBS/Social.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/Symbols.framework/Symbols](DYLIBS/Symbols.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/Translation.framework/Translation](DYLIBS/Translation.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/Vision.framework/libfaceCore.dylib](DYLIBS/libfaceCore.dylib.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib](DYLIBS/libWebKitSwift.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AVKit_SwiftUI.framework/_AVKit_SwiftUI](DYLIBS/_AVKit_SwiftUI.md)
- [/System/Library/Frameworks/_AdAttributionKit_StoreKit.framework/_AdAttributionKit_StoreKit](DYLIBS/_AdAttributionKit_StoreKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_CoreNFC_UIKit.framework/_CoreNFC_UIKit](DYLIBS/_CoreNFC_UIKit.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_QuickLook_SwiftUI.framework/_QuickLook_SwiftUI](DYLIBS/_QuickLook_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/AppRecommendations.healthplugin/AppRecommendations](DYLIBS/AppRecommendations.md)
- [/System/Library/Health/FeedItemPlugins/Categories.healthplugin/Categories](DYLIBS/Categories.md)
- [/System/Library/Health/FeedItemPlugins/HealthRecords.healthplugin/HealthRecords](DYLIBS/HealthRecords.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MobilityAppPlugin.healthplugin/MobilityAppPlugin](DYLIBS/MobilityAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WorldClockComplications.bundle/WorldClockComplications](DYLIBS/WorldClockComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFoghornFaceBundleCompanion.bundle/NTKFoghornFaceBundleCompanion](DYLIBS/NTKFoghornFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVivaldiFaceBundleCompanion.bundle/NTKVivaldiFaceBundleCompanion](DYLIBS/NTKVivaldiFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings](DYLIBS/MobilePhoneSettings.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/ALDataTypes.framework/ALDataTypes.dylib](DYLIBS/ALDataTypes.dylib.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/ANEServices.framework/ANEServices](DYLIBS/ANEServices.md)
- [/System/Library/PrivateFrameworks/AONSense.framework/AONSense.dylib](DYLIBS/AONSense.dylib.md)
- [/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem](DYLIBS/APConfigurationSystem.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation](DYLIBS/ATFoundation.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings](DYLIBS/AUSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXIDSServices.framework/AXIDSServices](DYLIBS/AXIDSServices.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities](DYLIBS/AXMediaUtilities.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenServices.framework/AXWatchRemoteScreenServices](DYLIBS/AXWatchRemoteScreenServices.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI](DYLIBS/AXWatchRemoteScreenUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI](DYLIBS/AccountsUI.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements](DYLIBS/ActivityAchievements.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon](DYLIBS/ActivityAchievementsDaemon.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI](DYLIBS/ActivityAchievementsUI.md)
- [/System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI](DYLIBS/ActivityRingsUI.md)
- [/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing](DYLIBS/ActivitySharing.md)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient.md)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdID.framework/AdID](DYLIBS/AdID.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AirPlayAndHandoffSettingsSupport.framework/AirPlayAndHandoffSettingsSupport](DYLIBS/AirPlayAndHandoffSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics](DYLIBS/AppInstallationMetrics.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation](DYLIBS/AppPredictionFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIWidget.framework/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI](DYLIBS/AppProtectionUI.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport](DYLIBS/AppSupport.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA](DYLIBS/AppleCVA.md)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth](DYLIBS/AppleDepth.md)
- [/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore](DYLIBS/AppleDepthCore.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport](DYLIBS/AppleDeviceQuerySupport.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libAppleDeviceQueryArmory.dylib](DYLIBS/libAppleDeviceQueryArmory.dylib.md)
- [/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication](DYLIBS/AppleIDSSOAuthentication.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG](DYLIBS/AppleJPEG.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity](DYLIBS/AppleMobileFileIntegrity.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine](DYLIBS/AppleNeuralEngine.md)
- [/System/Library/PrivateFrameworks/ApplePDPHelper.framework/ApplePDPHelper](DYLIBS/ApplePDPHelper.md)
- [/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices](DYLIBS/ApplePhotonDetectorServices.md)
- [/System/Library/PrivateFrameworks/ArchetypeEngine.framework/ArchetypeEngine](DYLIBS/ArchetypeEngine.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI](DYLIBS/AssistiveTouchUI.md)
- [/System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal](DYLIBS/AtomicsInternal.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore](DYLIBS/AutoFillCore.md)
- [/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI](DYLIBS/AutoFillUI.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices](DYLIBS/BackBoardServices.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/BarcodeSupport](DYLIBS/BarcodeSupport.md)
- [/System/Library/PrivateFrameworks/BarcodeSupportUI.framework/BarcodeSupportUI](DYLIBS/BarcodeSupportUI.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI](DYLIBS/BaseBoardUI.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BlockMonitoring.framework/BlockMonitoring](DYLIBS/BlockMonitoring.md)
- [/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices](DYLIBS/BluetoothServices.md)
- [/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices](DYLIBS/BoardServices.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/BusinessServicesUI.framework/BusinessServicesUI](DYLIBS/BusinessServicesUI.md)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary](DYLIBS/CBORLibrary.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP](DYLIBS/CVNLP.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase](DYLIBS/CalendarDatabase.md)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation](DYLIBS/CalendarFoundation.md)
- [/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/CalendarIntegrationSupport](DYLIBS/CalendarIntegrationSupport.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/CalendarUIKitInternal](DYLIBS/CalendarUIKitInternal.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices.md)
- [/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices](DYLIBS/CarouselPreferenceServices.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClarityBoardFoundation.framework/ClarityBoardFoundation](DYLIBS/ClarityBoardFoundation.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices](DYLIBS/ClipServices.md)
- [/System/Library/PrivateFrameworks/ClipUIServices.framework/ClipUIServices](DYLIBS/ClipUIServices.md)
- [/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI](DYLIBS/ClockKitUI.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets](DYLIBS/CloudAssets.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon](DYLIBS/CloudDocsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode](DYLIBS/CloudKitCode.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation](DYLIBS/CloudRecommendation.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI](DYLIBS/CloudSharingUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon](DYLIBS/CompanionHealthDaemon.md)
- [/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices](DYLIBS/CompanionServices.md)
- [/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards](DYLIBS/ComputeSafeguards.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync](DYLIBS/ContextSync.md)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices](DYLIBS/ControlCenterUIServices.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/Coordination.framework/Coordination](DYLIBS/Coordination.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI](DYLIBS/CoreFollowUpUI.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreIK.framework/CoreIK](DYLIBS/CoreIK.md)
- [/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor](DYLIBS/CoreIndoor.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay](DYLIBS/CoreLocationReplay.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles](DYLIBS/CoreLocationTiles.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreOCModules.framework/CoreOCModules](DYLIBS/CoreOCModules.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/CorePrescriptionLite](DYLIBS/CorePrescriptionLite.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO](DYLIBS/CoreRealityIO.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine](DYLIBS/CoreRoutine.md)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG](DYLIBS/CoreSVG.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore](DYLIBS/CoreServicesStore.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication](DYLIBS/CoreSymbolication.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreUtilsUI.framework/CoreUtilsUI](DYLIBS/CoreUtilsUI.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities](DYLIBS/DVTInstrumentsUtilities.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal](DYLIBS/DarwinDirectoryInternal.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryQuery.framework/DarwinDirectoryQuery](DYLIBS/DarwinDirectoryQuery.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport.md)
- [/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices](DYLIBS/DataDeliveryServices.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/DendriteIngest](DYLIBS/DendriteIngest.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing](DYLIBS/DeviceSharing.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices](DYLIBS/DictionaryServices.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DirectResource.framework/DirectResource](DYLIBS/DirectResource.md)
- [/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration](DYLIBS/DiskArbitration.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb](DYLIBS/DoNotDisturb.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts](DYLIBS/EmergencyAlerts.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/EnergyKitFoundation.framework/EnergyKitFoundation](DYLIBS/EnergyKitFoundation.md)
- [/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState](DYLIBS/EnhancedLoggingState.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FRC.framework/FRC](DYLIBS/FRC.md)
- [/System/Library/PrivateFrameworks/FSEvents.framework/FSEvents](DYLIBS/FSEvents.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeFeatureControl.framework/FaceTimeFeatureControl](DYLIBS/FaceTimeFeatureControl.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/FedStats.framework/FedStats](DYLIBS/FedStats.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger](DYLIBS/FeedbackLogger.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore](DYLIBS/FinHealthCore.md)
- [/System/Library/PrivateFrameworks/FinHealthInsights.framework/FinHealthInsights](DYLIBS/FinHealthInsights.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyLocateObjCWrapper.framework/FindMyLocateObjCWrapper](DYLIBS/FindMyLocateObjCWrapper.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction](DYLIBS/FindMyServerInteraction.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/Fitness.framework/Fitness](DYLIBS/Fitness.md)
- [/System/Library/PrivateFrameworks/FitnessActions.framework/FitnessActions](DYLIBS/FitnessActions.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards](DYLIBS/FitnessAwards.md)
- [/System/Library/PrivateFrameworks/FitnessBrowsing.framework/FitnessBrowsing](DYLIBS/FitnessBrowsing.md)
- [/System/Library/PrivateFrameworks/FitnessCanvas.framework/FitnessCanvas](DYLIBS/FitnessCanvas.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI](DYLIBS/FitnessCoreUI.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessForYou.framework/FitnessForYou](DYLIBS/FitnessForYou.md)
- [/System/Library/PrivateFrameworks/FitnessLibrary.framework/FitnessLibrary](DYLIBS/FitnessLibrary.md)
- [/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing](DYLIBS/FitnessMarketing.md)
- [/System/Library/PrivateFrameworks/FitnessOnboarding.framework/FitnessOnboarding](DYLIBS/FitnessOnboarding.md)
- [/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail](DYLIBS/FitnessProductDetail.md)
- [/System/Library/PrivateFrameworks/FitnessRemoteBrowsing.framework/FitnessRemoteBrowsing](DYLIBS/FitnessRemoteBrowsing.md)
- [/System/Library/PrivateFrameworks/FitnessSearch.framework/FitnessSearch](DYLIBS/FitnessSearch.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities](DYLIBS/FitnessUtilities.md)
- [/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan](DYLIBS/FitnessWorkoutPlan.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib](DYLIBS/libGSFontCache.dylib.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libComposeFilters.dylib](DYLIBS/libComposeFilters.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompiler.dylib](DYLIBS/libGPUCompiler.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport](DYLIBS/GPUToolsTransport.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GameServicesProtocols.framework/GameServicesProtocols](DYLIBS/GameServicesProtocols.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage](DYLIBS/GenerationalStorage.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctions.framework/GenerativeFunctions](DYLIBS/GenerativeFunctions.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativePlaygroundUI.framework/GenerativePlaygroundUI](DYLIBS/GenerativePlaygroundUI.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics](DYLIBS/GeoAnalytics.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/GeoUIFramework.framework/GeoUIFramework](DYLIBS/GeoUIFramework.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices](DYLIBS/H16ISPServices.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient](DYLIBS/HangTracerSettingsClient.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings](DYLIBS/HeadphoneSettings.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms](DYLIBS/HealthAlgorithms.md)
- [/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration](DYLIBS/HealthArticlesGeneration.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceAppPlugin.framework/HealthBalanceAppPlugin](DYLIBS/HealthBalanceAppPlugin.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications](DYLIBS/HealthMedications.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin](DYLIBS/HealthMedicationsDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI](DYLIBS/HealthMedicationsWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesWidgetUI.framework/HealthMenstrualCyclesWidgetUI](DYLIBS/HealthMenstrualCyclesWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration](DYLIBS/HealthOrchestration.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordsConceptsSupport.framework/HealthRecordsConceptsSupport](DYLIBS/HealthRecordsConceptsSupport.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService](DYLIBS/HearingModeService.md)
- [/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private](DYLIBS/HearingModeService_Private.md)
- [/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI](DYLIBS/HearingModeSettingsUI.md)
- [/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI](DYLIBS/HearingModeUI.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon](DYLIBS/HeartHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI](DYLIBS/HeartRhythmUI.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeCommunicationUIFramework.framework/HomeCommunicationUIFramework](DYLIBS/HomeCommunicationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils](DYLIBS/HomeMessagingUtils.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents](DYLIBS/HomeWidgetIntents.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation](DYLIBS/IMFoundation.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent](DYLIBS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferServices](DYLIBS/IMTransferServices.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/InputToolKitUI.framework/InputToolKitUI](DYLIBS/InputToolKitUI.md)
- [/System/Library/PrivateFrameworks/InputTranscoder.framework/InputTranscoder](DYLIBS/InputTranscoder.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination](DYLIBS/InstallCoordination.md)
- [/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary](DYLIBS/InstalledContentLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared](DYLIBS/IntelligenceFlowShared.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon](DYLIBS/IntelligentRoutingDaemon.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore](DYLIBS/IntentsCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences](DYLIBS/IntlPreferences.md)
- [/System/Library/PrivateFrameworks/JITAppKit.framework/JITAppKit](DYLIBS/JITAppKit.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/Koa.framework/Koa](DYLIBS/Koa.md)
- [/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache](DYLIBS/LLMCache.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkPresentationStyleSheetParsing.framework/LinkPresentationStyleSheetParsing](DYLIBS/LinkPresentationStyleSheetParsing.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices](DYLIBS/LiveSpeechServices.md)
- [/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription](DYLIBS/LiveTranscription.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit](DYLIBS/LocalStatusKit.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization](DYLIBS/MCCKitCategorization.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MIL.framework/MIL](DYLIBS/MIL.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO](DYLIBS/MOVStreamIO.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32023/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MailWebProcessSupport.framework/MailWebProcessSupport](DYLIBS/MailWebProcessSupport.md)
- [/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging](DYLIBS/MallocStackLogging.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI](DYLIBS/ManagedConfigurationUI.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MathTypesetting.framework/MathTypesetting](DYLIBS/MathTypesetting.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl](DYLIBS/MediaControl.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation](DYLIBS/MediaFoundation.md)
- [/System/Library/PrivateFrameworks/MediaML.framework/MediaML](DYLIBS/MediaML.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal](DYLIBS/MenstrualAlgorithmsInternal.md)
- [/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth](DYLIBS/MentalHealth.md)
- [/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon](DYLIBS/MentalHealthDaemon.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement](DYLIBS/MetricMeasurement.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth](DYLIBS/MobileBluetooth.md)
- [/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI](DYLIBS/MobileIdentityServiceUI.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation](DYLIBS/MobileInstallation.md)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariSwift.framework/MobileSafariSwift](DYLIBS/MobileSafariSwift.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi](DYLIBS/MobileWiFi.md)
- [/System/Library/PrivateFrameworks/ModalityXObjects.framework/ModalityXObjects](DYLIBS/ModalityXObjects.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/ModelMonitoringLighthouse.framework/ModelMonitoringLighthouse](DYLIBS/ModelMonitoringLighthouse.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/MonogramPoster.framework/MonogramPoster](DYLIBS/MonogramPoster.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/MultitouchSessionFilterSupport](DYLIBS/MultitouchSessionFilterSupport.md)
- [/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI](DYLIBS/MusicCarDisplayUI.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NanoAudioControl.framework/NanoAudioControl](DYLIBS/NanoAudioControl.md)
- [/System/Library/PrivateFrameworks/NanoHomeIntents.framework/NanoHomeIntents](DYLIBS/NanoHomeIntents.md)
- [/System/Library/PrivateFrameworks/NanoMediaAPI.framework/NanoMediaAPI](DYLIBS/NanoMediaAPI.md)
- [/System/Library/PrivateFrameworks/NanoMediaBridgeUI.framework/NanoMediaBridgeUI](DYLIBS/NanoMediaBridgeUI.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore](DYLIBS/NanoPhotosCore.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions](DYLIBS/NearbySessions.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/NeighborhoodActivityConduit](DYLIBS/NeighborhoodActivityConduit.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit](DYLIBS/NeutrinoKit.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/NewsAnalyticsUpload](DYLIBS/NewsAnalyticsUpload.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation](DYLIBS/NewsFoundation.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI](DYLIBS/NewsUI.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSiriUI.framework/NotesSiriUI](DYLIBS/NotesSiriUI.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices](DYLIBS/NotesUIServices.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport](DYLIBS/OfficeImport.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OmniSearchTypes.framework/OmniSearchTypes](DYLIBS/OmniSearchTypes.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase](DYLIBS/PaymentUIBase.md)
- [/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI](DYLIBS/PencilPairingUI.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterMetrics.framework/PeopleSuggesterMetrics](DYLIBS/PeopleSuggesterMetrics.md)
- [/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI](DYLIBS/PeopleUI.md)
- [/System/Library/PrivateFrameworks/PeopleUIInternal.framework/PeopleUIInternal](DYLIBS/PeopleUIInternal.md)
- [/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor](DYLIBS/PerfPowerMetricMonitor.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth](DYLIBS/PeridotDepth.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosFaceCore.framework/PhotosFaceCore](DYLIBS/PhotosFaceCore.md)
- [/System/Library/PrivateFrameworks/PhotosFaceLayout.framework/PhotosFaceLayout](DYLIBS/PhotosFaceLayout.md)
- [/System/Library/PrivateFrameworks/PhotosFaceLayoutCore.framework/PhotosFaceLayoutCore](DYLIBS/PhotosFaceLayoutCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligenceCore.framework/PhotosIntelligenceCore](DYLIBS/PhotosIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PhotosSearchClient.framework/PhotosSearchClient](DYLIBS/PhotosSearchClient.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/Planks.framework/Planks](DYLIBS/Planks.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore](DYLIBS/PlatformSSOCore.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation](DYLIBS/PosterFoundation.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation](DYLIBS/PosterUIFoundation.md)
- [/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience](DYLIBS/PowerExperience.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit.md)
- [/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI](DYLIBS/PrintKitUI.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/PrivateMLClientInferenceProvider](DYLIBS/PrivateMLClientInferenceProvider.md)
- [/System/Library/PrivateFrameworks/ProVideo.framework/ProVideo](DYLIBS/ProVideo.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel](DYLIBS/ProactiveSuggestionClientModel.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction](DYLIBS/PromotedContentPrediction.md)
- [/System/Library/PrivateFrameworks/PromotedContentSupport.framework/PromotedContentSupport](DYLIBS/PromotedContentSupport.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/PromptKit.framework/PromptKit](DYLIBS/PromptKit.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI](DYLIBS/RTTUI.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion](DYLIBS/RealityFusion.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/ReminderKitUI](DYLIBS/ReminderKitUI.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration](DYLIBS/RemoteConfiguration.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore](DYLIBS/RemoteManagementStore.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery](DYLIBS/RemoteServiceDiscovery.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RoomScanCore.framework/RoomScanCore](DYLIBS/RoomScanCore.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SAML.framework/SAML](DYLIBS/SAML.md)
- [/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects](DYLIBS/SAObjects.md)
- [/System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders](DYLIBS/SCSharingReminders.md)
- [/System/Library/PrivateFrameworks/SDAPI.framework/SDAPI](DYLIBS/SDAPI.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/SMBClientProvider](DYLIBS/SMBClientProvider.md)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS.md)
- [/System/Library/PrivateFrameworks/SOSUI.framework/SOSUI](DYLIBS/SOSUI.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/Scandium.framework/Scandium](DYLIBS/Scandium.md)
- [/System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices](DYLIBS/ScreenContinuityServices.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingAccessibilityService.framework/ScreenSharingAccessibilityService](DYLIBS/ScreenSharingAccessibilityService.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SearchUICardKitProviderSupport.framework/SearchUICardKitProviderSupport](DYLIBS/SearchUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit](DYLIBS/SecureCaptureKit.md)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService](DYLIBS/SecureTransactionService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI](DYLIBS/SensorKitUI.md)
- [/System/Library/PrivateFrameworks/SentencePieceInternal.framework/SentencePieceInternal](DYLIBS/SentencePieceInternal.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement.md)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit](DYLIBS/SetupKit.md)
- [/System/Library/PrivateFrameworks/SetupKitUI.framework/SetupKitUI](DYLIBS/SetupKitUI.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices](DYLIBS/SeymourClientServices.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework](DYLIBS/SiriAppLaunchUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI](DYLIBS/SiriAutoCompleteAPI.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsCommon.framework/SiriContactsCommon](DYLIBS/SiriContactsCommon.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics](DYLIBS/SiriCoreMetrics.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback](DYLIBS/SiriCrossDeviceArbitrationFeedback.md)
- [/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher](DYLIBS/SiriEntityMatcher.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternalUI.framework/SiriExpanseInternalUI](DYLIBS/SiriExpanseInternalUI.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo](DYLIBS/SiriGeo.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/SiriInferredHelpfulness](DYLIBS/SiriInferredHelpfulness.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes](DYLIBS/SiriInformationTypes.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriInteractive.framework/SiriInteractive](DYLIBS/SiriInteractive.md)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/SiriInvocationAnalytics](DYLIBS/SiriInvocationAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriLiminal.framework/SiriLiminal](DYLIBS/SiriLiminal.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMailUIModel.framework/SiriMailUIModel](DYLIBS/SiriMailUIModel.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver](DYLIBS/SiriReferenceResolver.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriStates.framework/SiriStates](DYLIBS/SiriStates.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/SiriSuggestionsBaseModel](DYLIBS/SiriSuggestionsBaseModel.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriSystemCommandsIntents.framework/SiriSystemCommandsIntents](DYLIBS/SiriSystemCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUICardKitProviderSupport.framework/SiriUICardKitProviderSupport](DYLIBS/SiriUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX](DYLIBS/SiriVOX.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution.md)
- [/System/Library/PrivateFrameworks/SiriWellnessIntents.framework/SiriWellnessIntents](DYLIBS/SiriWellnessIntents.md)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon](DYLIBS/SleepDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusKit.framework/OpusKit](DYLIBS/OpusKit.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialServices.framework/SocialServices](DYLIBS/SocialServices.md)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution](DYLIBS/SpaceAttribution.md)
- [/System/Library/PrivateFrameworks/SpatialInspectorFoundation.framework/SpatialInspectorFoundation](DYLIBS/SpatialInspectorFoundation.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognitionKit.framework/SpeakerRecognitionKit](DYLIBS/SpeakerRecognitionKit.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport](DYLIBS/SpeechRecognitionSharedSupport.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport](DYLIBS/SpotlightSettingsSupport.md)
- [/System/Library/PrivateFrameworks/SpotlightUI.framework/SpotlightUI](DYLIBS/SpotlightUI.md)
- [/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal](DYLIBS/SpotlightUIInternal.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardDisplayServices.framework/SpringBoardDisplayServices](DYLIBS/SpringBoardDisplayServices.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SwiftASN1.framework/SwiftASN1](DYLIBS/SwiftASN1.md)
- [/System/Library/PrivateFrameworks/SwiftNN.framework/SwiftNN](DYLIBS/SwiftNN.md)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication](DYLIBS/Symbolication.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults](DYLIBS/SyncedDefaults.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemPaperPresentation.framework/SystemPaperPresentation](DYLIBS/SystemPaperPresentation.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TSReading.framework/TSReading](DYLIBS/TSReading.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVLatency.framework/TVLatency](DYLIBS/TVLatency.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSnappy.framework/TeaSnappy](DYLIBS/TeaSnappy.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences](DYLIBS/TelephonyPreferences.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TemporaryFramework.framework/TemporaryFramework](DYLIBS/TemporaryFramework.md)
- [/System/Library/PrivateFrameworks/TestFlightCore.framework/TestFlightCore](DYLIBS/TestFlightCore.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextGenerationInference.framework/TextGenerationInference](DYLIBS/TextGenerationInference.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/TextInputTestingKit](DYLIBS/TextInputTestingKit.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/TextToSpeechMauiSupport](DYLIBS/TextToSpeechMauiSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices](DYLIBS/TipKitServices.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TouchML.framework/TouchML](DYLIBS/TouchML.md)
- [/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote](DYLIBS/TouchRemote.md)
- [/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance](DYLIBS/TrackingAvoidance.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI](DYLIBS/TransparencyUI.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto](DYLIBS/TrialProto.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/Tungsten.framework/Tungsten](DYLIBS/Tungsten.md)
- [/System/Library/PrivateFrameworks/TuriCore.framework/TuriCore](DYLIBS/TuriCore.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UINavigationKit.framework/UINavigationKit](DYLIBS/UINavigationKit.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UniversalHIDKit.framework/UniversalHIDKit](DYLIBS/UniversalHIDKit.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity](DYLIBS/UserActivity.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib](DYLIBS/livefiles_hfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices](DYLIBS/UserNotificationsServices.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage](DYLIBS/VirtualGarage.md)
- [/System/Library/PrivateFrameworks/Visage.framework/Visage](DYLIBS/Visage.md)
- [/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore](DYLIBS/VisionCore.md)
- [/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices](DYLIBS/VisionHWAccelerationServices.md)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger](DYLIBS/VisualLogger.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherAppSupport.framework/WeatherAppSupport](DYLIBS/WeatherAppSupport.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector](DYLIBS/WebInspector.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet](DYLIBS/WebSheet.md)
- [/System/Library/PrivateFrameworks/WellnessUI.framework/WellnessUI](DYLIBS/WellnessUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity](DYLIBS/WiFiVelocity.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/Widgets.framework/Widgets](DYLIBS/Widgets.md)
- [/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager](DYLIBS/WirelessCoexManager.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness](DYLIBS/WorkflowResponsiveness.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/ZeoliteFramework.framework/ZeoliteFramework](DYLIBS/ZeoliteFramework.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib.md)
- [/System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices](DYLIBS/ZoomServices.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/caulk.framework/caulk](DYLIBS/caulk.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudMailUnifiedSettings.framework/iCloudMailUnifiedSettings](DYLIBS/iCloudMailUnifiedSettings.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/iCloudSubscriptionOptimizerDaemon](DYLIBS/iCloudSubscriptionOptimizerDaemon.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/iCloudSubscriptionOptimizerLighthouse](DYLIBS/iCloudSubscriptionOptimizerLighthouse.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText](DYLIBS/TSText.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/TextInput/TextInput_ko.bundle/TextInput_ko](DYLIBS/TextInput_ko.md)
- [/System/Library/TextInput/TextInput_pa.bundle/TextInput_pa](DYLIBS/TextInput_pa.md)
- [/System/Library/TextInput/TextInput_th.bundle/TextInput_th](DYLIBS/TextInput_th.md)
- [/System/Library/TextInput/TextInput_zh.bundle/TextInput_zh](DYLIBS/TextInput_zh.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder](DYLIBS/AppleProResHWDecoder.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoDecoders/MP4VH8.videodecoder](DYLIBS/MP4VH8.videodecoder.md)
- [/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder](DYLIBS/AppleProResHWEncoder.videoencoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAppleEXR.dylib](DYLIBS/libAppleEXR.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libFosl_dynamic.dylib](DYLIBS/libFosl_dynamic.dylib.md)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libNFC_HAL.dylib](DYLIBS/libNFC_HAL.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libParallelCompression.dylib](DYLIBS/libParallelCompression.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libfire7.dylib](DYLIBS/libfire7.dylib.md)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libllvm-flatbuffers.dylib](DYLIBS/libllvm-flatbuffers.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libmorphun.dylib](DYLIBS/libmorphun.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/libskit.dylib](DYLIBS/libskit.dylib.md)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libtidy.A.dylib](DYLIBS/libtidy.A.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftCarPlay.dylib](DYLIBS/libswiftCarPlay.dylib.md)
- [/usr/lib/swift/libswiftCompression.dylib](DYLIBS/libswiftCompression.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftDarwin.dylib](DYLIBS/libswiftDarwin.dylib.md)
- [/usr/lib/swift/libswiftDemangle.dylib](DYLIBS/libswiftDemangle.dylib.md)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib.md)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib.md)
- [/usr/lib/swift/libswiftGLKit.dylib](DYLIBS/libswiftGLKit.dylib.md)
- [/usr/lib/swift/libswiftGameplayKit.dylib](DYLIBS/libswiftGameplayKit.dylib.md)
- [/usr/lib/swift/libswiftMapKit.dylib](DYLIBS/libswiftMapKit.dylib.md)
- [/usr/lib/swift/libswiftMetalKit.dylib](DYLIBS/libswiftMetalKit.dylib.md)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)
- [/usr/lib/swift/libswiftObservation.dylib](DYLIBS/libswiftObservation.dylib.md)
- [/usr/lib/swift/libswiftRegexBuilder.dylib](DYLIBS/libswiftRegexBuilder.dylib.md)
- [/usr/lib/swift/libswiftSceneKit.dylib](DYLIBS/libswiftSceneKit.dylib.md)
- [/usr/lib/swift/libswiftSpriteKit.dylib](DYLIBS/libswiftSpriteKit.dylib.md)
- [/usr/lib/swift/libswiftSwiftOnoneSupport.dylib](DYLIBS/libswiftSwiftOnoneSupport.dylib.md)
- [/usr/lib/swift/libswiftSynchronization.dylib](DYLIBS/libswiftSynchronization.dylib.md)
- [/usr/lib/swift/libswiftWatchKit.dylib](DYLIBS/libswiftWatchKit.dylib.md)
- [/usr/lib/swift/libswiftWebKit.dylib](DYLIBS/libswiftWebKit.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_Builtin_float.dylib](DYLIBS/libswift_Builtin_float.dylib.md)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib.md)
- [/usr/lib/swift/libswift_Differentiation.dylib](DYLIBS/libswift_Differentiation.dylib.md)
- [/usr/lib/swift/libswift_RegexParser.dylib](DYLIBS/libswift_RegexParser.dylib.md)
- [/usr/lib/swift/libswift_StringProcessing.dylib](DYLIBS/libswift_StringProcessing.dylib.md)
- [/usr/lib/swift/~libswiftPencilKit.dylib](DYLIBS/~libswiftPencilKit.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_coreservices.dylib](DYLIBS/libsystem_coreservices.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_m.dylib](DYLIBS/libsystem_m.dylib.md)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib.md)
- [/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib](DYLIBS/libSavageRestoreInfo_iOS.dylib.md)
- [/usr/lib/updaters/libSavageUpdater_iOS.dylib](DYLIBS/libSavageUpdater_iOS.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

### Feature Flags

#### 🆕 NEW (2)

- `Domain/DriverKit.plist`
- `Domain/Intercom.plist`

#### ❌ Removed (4)

- `Domain/Announce.plist`
- `Domain/BlockMonitoring.plist`
- `Domain/CoreChartSwift.plist`
- `Domain/ModelCatalog.plist`

#### ⬆️ Updated (26)

<details>
  <summary><i>View Updated</i></summary>

- [Domain/AppStore.plist](FEATURES/AppStore.plist.md)
- [Domain/ControlCenter.plist](FEATURES/ControlCenter.plist.md)
- [Domain/Freeform.plist](FEATURES/Freeform.plist.md)
- [Domain/Home.plist](FEATURES/Home.plist.md)
- [Domain/HomeDeviceSetup.plist](FEATURES/HomeDeviceSetup.plist.md)
- [Domain/IDS.plist](FEATURES/IDS.plist.md)
- [Domain/IconServices.plist](FEATURES/IconServices.plist.md)
- [Domain/MediaAnalysis.plist](FEATURES/MediaAnalysis.plist.md)
- [Domain/MediaRemote.plist](FEATURES/MediaRemote.plist.md)
- [Domain/NetworkServiceProxy.plist](FEATURES/NetworkServiceProxy.plist.md)
- [Domain/PerfPowerServices.plist](FEATURES/PerfPowerServices.plist.md)
- [Domain/ProactiveHarvesting.plist](FEATURES/ProactiveHarvesting.plist.md)
- [Domain/RealityKit.plist](FEATURES/RealityKit.plist.md)
- [Domain/Siri.plist](FEATURES/Siri.plist.md)
- [Domain/SiriAnalytics.plist](FEATURES/SiriAnalytics.plist.md)
- [Domain/SiriHomeAutomation.plist](FEATURES/SiriHomeAutomation.plist.md)
- [Domain/SiriMetrics.plist](FEATURES/SiriMetrics.plist.md)
- [Domain/SoundAnalysis.plist](FEATURES/SoundAnalysis.plist.md)
- [Domain/Spotlight.plist](FEATURES/Spotlight.plist.md)
- [Domain/TVApp.plist](FEATURES/TVApp.plist.md)
- [Domain/TVRemoteCore.plist](FEATURES/TVRemoteCore.plist.md)
- [Domain/TelephonyUtilities.plist](FEATURES/TelephonyUtilities.plist.md)
- [Domain/TrialXP.plist](FEATURES/TrialXP.plist.md)
- [Domain/UIKit.plist](FEATURES/UIKit.plist.md)
- [Domain/UserNotifications.plist](FEATURES/UserNotifications.plist.md)
- [Domain/WritingTools.plist](FEATURES/WritingTools.plist.md)

</details>

## EOF
