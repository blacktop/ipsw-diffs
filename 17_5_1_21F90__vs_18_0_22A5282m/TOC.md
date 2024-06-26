# 17.5.1 (21F90) .vs 18.0 (22A5282m)

## IPSWs

- `iPhone16,2_17.5.1_21F90_Restore.ipsw`
- `iPhone16,2_18.0_22A5282m_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.5.1 *(21F90)* | 23.5.0 | 10063.122.3~3 | Wed, 01May2024 20:34:22 PDT |
| 18.0 *(22A5282m)* | 24.0.0 | 11215.0.31.522.1~1 | Thu, 30May2024 22:34:02 PDT |

### Kexts

#### 🆕 NEW (2)

- `com.apple.iokit.IOGameControllerFamily`
- `com.apple.kec.AppleEncryptedArchive`

#### ❌ Removed (1)

- `com.apple.driver.AppleSamsungSPI`

#### ⬆️ Updated (253)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.ExclavesAudioKext`

```diff

-146.11.0.0.0
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2b35
-  __TEXT.__os_log: 0x438
-  __TEXT_EXEC.__text: 0x5f1c
+200.49.1.0.0
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x31cd
+  __TEXT.__os_log: 0x55a
+  __TEXT_EXEC.__text: 0x8d24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__mod_init_func: 0x10
-  __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x6d8
-  __DATA_CONST.__kalloc_type: 0x80
+  __DATA.__common: 0xd8
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__mod_init_func: 0x28
+  __DATA_CONST.__mod_term_func: 0x28
+  __DATA_CONST.__const: 0xb08
+  __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 320
 

```

>  `com.apple.iokit.IOReportFamily`

```diff

 106.0.0.0.0
   __TEXT.__cstring: 0x215
   __TEXT.__os_log: 0x329
-  __TEXT_EXEC.__text: 0x2e18
+  __TEXT_EXEC.__text: 0x2c58
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xd00
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 64
 

```

>  `com.apple.driver.AppleHIDALSService`

```diff

-1672.120.23.0.0
+1835.0.2.0.1
   __TEXT.__cstring: 0xbf
   __TEXT.__os_log: 0xc0
-  __TEXT_EXEC.__text: 0x904
+  __TEXT_EXEC.__text: 0x90c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x40

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 27
 

```

>  `com.apple.driver.ApplePPMCPMS`

```diff

-879.120.6.0.0
-  __TEXT.__const: 0xe90
-  __TEXT.__cstring: 0xdb50
-  __TEXT.__os_log: 0x1f84
-  __TEXT_EXEC.__text: 0x46884
+931.0.0.0.0
+  __TEXT.__const: 0xe50
+  __TEXT.__cstring: 0xd065
+  __TEXT.__os_log: 0x1fad
+  __TEXT_EXEC.__text: 0x45f2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x156
-  __DATA.__common: 0x4d0
-  __DATA.__bss: 0x1c8
-  __DATA_CONST.__auth_got: 0x360
+  __DATA.__common: 0x4a8
+  __DATA.__bss: 0x1b8
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__mod_init_func: 0xd8
-  __DATA_CONST.__mod_term_func: 0xa8
-  __DATA_CONST.__const: 0x4f28
-  __DATA_CONST.__kalloc_type: 0x940
+  __DATA_CONST.__mod_init_func: 0xd0
+  __DATA_CONST.__mod_term_func: 0xa0
+  __DATA_CONST.__const: 0x4cc0
+  __DATA_CONST.__kalloc_type: 0x900
   Symbols:   0
-  Functions: 0
+  Functions: 1651
 

```

>  `com.apple.driver.AppleUSBEthernetHost`

```diff

-159.0.0.0.0
-  __TEXT.__const: 0x8
+161.0.0.0.0
   __TEXT.__cstring: 0xbc4
-  __TEXT_EXEC.__text: 0x4048
+  __TEXT_EXEC.__text: 0x404c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x88

   __DATA_CONST.__const: 0x1258
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 109
 

```

>  `com.apple.kext.CoreTrust`

```diff

-140.120.3.0.0
-  __TEXT.__const: 0xfc9
+148.0.0.0.0
+  __TEXT.__const: 0xfe8
   __TEXT.__cstring: 0x52
-  __TEXT_EXEC.__text: 0x83f4
+  __TEXT_EXEC.__text: 0x8660
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x10
   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x14a0
+  __DATA_CONST.__const: 0x14e0
   Symbols:   0
-  Functions: 0
+  Functions: 128
 

```

>  `com.apple.driver.AppleARMPMU`

```diff

-1026.120.7.0.0
+1066.0.0.0.0
   __TEXT.__const: 0x64
   __TEXT.__cstring: 0x2d45
-  __TEXT_EXEC.__text: 0x16170
+  __TEXT_EXEC.__text: 0x160f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e8
   __DATA.__common: 0x148

   __DATA_CONST.__const: 0x1e50
   __DATA_CONST.__kalloc_type: 0x300
   Symbols:   0
-  Functions: 0
+  Functions: 271
 

```

>  `com.apple.driver.AppleBasebandPCIMAVControl`

```diff

-760.0.0.0.0
+807.0.0.0.0
   __TEXT.__const: 0x262a
-  __TEXT.__cstring: 0x1225
-  __TEXT_EXEC.__text: 0x2841c
+  __TEXT.__cstring: 0x6820
+  __TEXT_EXEC.__text: 0x510e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x140
-  __DATA.__common: 0xd8
+  __DATA.__common: 0x100
   __DATA.__bss: 0x1760
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__mod_init_func: 0xaf0
-  __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x7c38
-  __DATA_CONST.__kalloc_type: 0xc00
-  __DATA_CONST.__kalloc_var: 0x550
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__mod_init_func: 0xaf8
+  __DATA_CONST.__mod_term_func: 0x38
+  __DATA_CONST.__const: 0x7dc0
+  __DATA_CONST.__kalloc_type: 0xc80
+  __DATA_CONST.__kalloc_var: 0x5a0
   Symbols:   0
-  Functions: 0
+  Functions: 1079
 

```

>  `com.apple.driver.AppleT8030SOCTuner`

```diff

-1374.120.11.0.0
+1555.0.2.0.2
   __TEXT.__cstring: 0x41e
   __TEXT.__const: 0x30
-  __TEXT_EXEC.__text: 0x1654
+  __TEXT_EXEC.__text: 0x163c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xc50
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 89
 

```

>  `com.apple.driver.DiskImages.UDIFDiskImage`

```diff

-654.120.2.0.0
+662.0.0.0.0
   __TEXT.__const: 0x30b8
   __TEXT.__cstring: 0x2ac
-  __TEXT_EXEC.__text: 0xab18
+  __TEXT_EXEC.__text: 0xaa2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0xd8

   __DATA_CONST.__kalloc_type: 0x140
   __DATA_CONST.__kalloc_var: 0x190
   Symbols:   0
-  Functions: 0
+  Functions: 197
 

```

>  `com.apple.filesystems.lifs`

```diff

-208.120.7.0.3
-  __TEXT.__os_log: 0x11c5
-  __TEXT.__cstring: 0x1d28
-  __TEXT.__const: 0x290
-  __TEXT_EXEC.__text: 0x19f88
+411.0.0.0.4
+  __TEXT.__os_log: 0x1278
+  __TEXT.__cstring: 0x22bb
+  __TEXT.__const: 0x2d0
+  __TEXT_EXEC.__text: 0x1ac80
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x50
-  __DATA_CONST.__auth_got: 0x790
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1688
+  __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__kalloc_type: 0xb40
   Symbols:   0
-  Functions: 0
+  Functions: 399
 

```

>  `com.apple.driver.AppleCallbackPowerSource`

```diff

-1630.120.8.0.0
-  __TEXT.__cstring: 0xf3b
+1725.0.0.0.0
+  __TEXT.__cstring: 0xf5f
   __TEXT.__os_log: 0x76
-  __TEXT_EXEC.__text: 0x4ac4
+  __TEXT_EXEC.__text: 0x4b2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x190
-  __DATA.__bss: 0x13c0
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0x58
+  __DATA.__bss: 0x13f0
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc00
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 63
 

```

>  `com.apple.driver.AppleNANDConfigAccess`

```diff

-7.0.0.0.0
+8.0.0.0.0
   __TEXT.__cstring: 0x43
   __TEXT_EXEC.__text: 0x3cc
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x610
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 26
 

```

>  `com.apple.driver.AppleStockholmControl`

```diff

-345.7.0.0.0
-  __TEXT.__cstring: 0x4736
+350.23.1.0.0
+  __TEXT.__cstring: 0x4961
   __TEXT.__const: 0x30
-  __TEXT_EXEC.__text: 0x15624
+  __TEXT_EXEC.__text: 0x15d30
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x219
   __DATA.__common: 0x1a6
-  __DATA_CONST.__auth_got: 0x288
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x21c8
+  __DATA_CONST.__const: 0x2260
   __DATA_CONST.__kalloc_type: 0x1c0
   Symbols:   0
-  Functions: 0
+  Functions: 248
 

```

>  `com.apple.driver.AppleIISController`

```diff

-340.1.0.0.0
+400.1.0.0.0
   __TEXT.__cstring: 0x93f
-  __TEXT_EXEC.__text: 0x6fe8
+  __TEXT_EXEC.__text: 0x6fd8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x100

   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 200
 

```

>  `com.apple.driver.AppleMultiFunctionManager`

```diff

-60.0.0.0.0
-  __TEXT.__const: 0x29
+70.0.0.0.0
+  __TEXT.__const: 0x19
   __TEXT.__cstring: 0x2502
-  __TEXT_EXEC.__text: 0xb444
+  __TEXT_EXEC.__text: 0xb518
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1d8
   __DATA.__common: 0x108

   __DATA_CONST.__const: 0xed8
   __DATA_CONST.__kalloc_type: 0x300
   Symbols:   0
-  Functions: 0
+  Functions: 262
 

```

>  `com.apple.driver.DiskImages`

```diff

-654.120.2.0.0
-  __TEXT.__cstring: 0xc3a
-  __TEXT_EXEC.__text: 0x9b7c
+662.0.0.0.0
+  __TEXT.__cstring: 0xc34
+  __TEXT_EXEC.__text: 0x9b74
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

   __DATA_CONST.__kalloc_type: 0x2c0
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 265
 

```

>  `com.apple.driver.AppleSPURose`

```diff

-957.120.3.0.1
+1013.0.0.0.1
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x1f82
+  __TEXT.__cstring: 0x1f7c
   __TEXT.__os_log: 0x1431
-  __TEXT_EXEC.__text: 0x17b50
+  __TEXT_EXEC.__text: 0x179cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x268
+  __DATA.__bss: 0x2
   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x78

   __DATA_CONST.__const: 0x32c8
   __DATA_CONST.__kalloc_type: 0x3c0
   Symbols:   0
-  Functions: 0
+  Functions: 620
 

```

>  `com.apple.driver.usb.AppleUSBHostiOSDevice`

```diff

-1337.120.6.0.0
-  __TEXT.__cstring: 0x145
-  __TEXT.__os_log: 0x1e
-  __TEXT_EXEC.__text: 0x1094
+1402.0.0.0.0
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x3ef
+  __TEXT.__os_log: 0x2e0
+  __TEXT_EXEC.__text: 0x1964
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0x78
-  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x5f0
+  __DATA_CONST.__const: 0x620
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 29
 

```

>  `com.apple.driver.AppleDCPDPTXProxy`

```diff

-224.120.9.0.0
-  __TEXT.__cstring: 0x1524
-  __TEXT.__const: 0x58
-  __TEXT.__os_log: 0xd02
-  __TEXT_EXEC.__text: 0x99d0
+311.0.9.0.0
+  __TEXT.__cstring: 0x1027
+  __TEXT.__const: 0x48
+  __TEXT.__os_log: 0xa0c
+  __TEXT_EXEC.__text: 0x859c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x2c40
+  __DATA_CONST.__const: 0x2b18
   __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 282
 

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-859.120.5.0.0
-  __TEXT.__cstring: 0x9247
+938.0.8.0.1
+  __TEXT.__cstring: 0x99f9
   __TEXT.__const: 0x14b0
   __TEXT.__os_log: 0x233
-  __TEXT_EXEC.__text: 0x24b3c
+  __TEXT_EXEC.__text: 0x25f6c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3ba
+  __DATA.__data: 0x412
   __DATA.__common: 0xb0
   __DATA.__bss: 0x79
-  __DATA_CONST.__auth_got: 0x790
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x3718
+  __DATA_CONST.__const: 0x3750
   __DATA_CONST.__kalloc_type: 0xec0
   __DATA_CONST.__kalloc_var: 0x1310
   Symbols:   0
-  Functions: 0
+  Functions: 790
 

```

>  `com.apple.driver.AppleSARService`

```diff

-1053.0.0.0.0
-  __TEXT.__const: 0x720
-  __TEXT.__cstring: 0x2975
-  __TEXT.__os_log: 0x74d6
+1163.1.0.0.0
+  __TEXT.__const: 0x750
+  __TEXT.__cstring: 0x9ae2
+  __TEXT.__os_log: 0xb872
   __TEXT.__ustring: 0x8
-  __TEXT_EXEC.__text: 0x3207c
+  __TEXT_EXEC.__text: 0x53b0c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xd0
-  __DATA.__common: 0x5e8
-  __DATA.__bss: 0xc40
-  __DATA_CONST.__auth_got: 0x240
-  __DATA_CONST.__got: 0x90
+  __DATA.__data: 0xd8
+  __DATA.__common: 0x5f0
+  __DATA.__bss: 0x1458
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x60
-  __DATA_CONST.__const: 0x4620
-  __DATA_CONST.__kalloc_type: 0x1940
+  __DATA_CONST.__const: 0x4d28
+  __DATA_CONST.__kalloc_type: 0x2940
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 538
 

```

>  `com.apple.driver.AppleHapticsSupportLEAP`

```diff

-8.11.0.0.0
+9.17.0.0.0
   __TEXT.__const: 0x1f4
-  __TEXT.__cstring: 0x3eaa
-  __TEXT.__os_log: 0x781
-  __TEXT_EXEC.__text: 0x306c4
+  __TEXT.__cstring: 0x4385
+  __TEXT.__os_log: 0x82e
+  __TEXT_EXEC.__text: 0x32284
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__got_weak: 0x60
-  __DATA.__data: 0x7f0
-  __DATA.__common: 0x5a0
+  __DATA.__data: 0x800
+  __DATA.__common: 0x5f0
   __DATA.__bss: 0x1
-  __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__mod_init_func: 0xa0
-  __DATA_CONST.__mod_term_func: 0xa8
-  __DATA_CONST.__const: 0x3a30
-  __DATA_CONST.__kalloc_type: 0x940
+  __DATA_CONST.__auth_got: 0x348
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__mod_init_func: 0xb0
+  __DATA_CONST.__mod_term_func: 0xb8
+  __DATA_CONST.__const: 0x4778
+  __DATA_CONST.__kalloc_type: 0xac0
   __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 0
+  Functions: 922
 

```

>  `com.apple.kec.corecrypto`

```diff

-1638.100.62.0.0
-  __TEXT.__cstring: 0x4693
-  __TEXT.__const: 0x14150
+1736.0.22.0.0
+  __TEXT.__cstring: 0x46c3
+  __TEXT.__const: 0x144b0
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x511bc
+  __TEXT_EXEC.__text: 0x54ac8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2df0
   __DATA.__bss: 0x2960
   __DATA.__common: 0x138
   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x28f8
+  __DATA_CONST.__auth_ptr: 0x128
+  __DATA_CONST.__const: 0x2ba8
   Symbols:   0
-  Functions: 0
+  Functions: 1303
 

```

>  `com.apple.iokit.IOPortFamily`

```diff

-50.0.0.0.0
+54.0.0.0.0
   __TEXT_EXEC.__text: 0x84
   __DATA.__data: 0xc8
   __DATA.__common: 0x10
   Symbols:   0
-  Functions: 0
+  Functions: 5
 

```

>  `com.apple.driver.AppleEmbeddedTempSensor`

```diff

-181.0.0.0.0
+182.0.0.0.0
   __TEXT.__cstring: 0x2ca7
   __TEXT.__const: 0x90
-  __TEXT_EXEC.__text: 0x17dcc
+  __TEXT_EXEC.__text: 0x17ddc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3f0
   __DATA.__common: 0x308

   __DATA_CONST.__const: 0x77e0
   __DATA_CONST.__kalloc_type: 0x4c0
   Symbols:   0
-  Functions: 0
+  Functions: 542
 

```

>  `com.apple.driver.ApplePMP`

```diff

-967.120.6.0.0
-  __TEXT.__const: 0x48
+1173.0.9.0.1
+  __TEXT.__const: 0x3c
   __TEXT.__cstring: 0x14f0
-  __TEXT_EXEC.__text: 0xd804
+  __TEXT_EXEC.__text: 0xd7e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x3348
+  __DATA_CONST.__const: 0x3330
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 394
 

```

>  `com.apple.iokit.IONetworkFamily`

```diff

-464.120.2.0.0
+508.0.0.0.0
   __TEXT.__cstring: 0x63
   __TEXT_EXEC.__text: 0x394
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 22
 

```

>  `com.apple.driver.AppleEffaceableBlockDevice`

```diff

-86.0.0.0.0
+88.0.0.0.0
   __TEXT.__cstring: 0x166
   __TEXT_EXEC.__text: 0x105c
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x5f8
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 55
 

```

>  `com.apple.driver.AppleLockdownMode`

```diff

-65.100.3.0.0
+71.0.0.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x44bb
-  __TEXT_EXEC.__text: 0x13bd8
+  __TEXT.__cstring: 0x4320
+  __TEXT_EXEC.__text: 0x13b14
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
   __DATA.__common: 0x40

   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x1400
   Symbols:   0
-  Functions: 0
+  Functions: 204
 

```

>  `com.apple.driver.IOHIDPowerSource`

```diff

-2031.120.4.0.0
+2094.0.0.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x7e4
   __TEXT.__os_log: 0x433
-  __TEXT_EXEC.__text: 0x9670
+  __TEXT_EXEC.__text: 0x95b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x138

   __DATA_CONST.__const: 0x1a78
   __DATA_CONST.__kalloc_type: 0x340
   Symbols:   0
-  Functions: 0
+  Functions: 209
 

```

>  `com.apple.driver.DCPAVFamilyProxy`

```diff

-283.120.9.0.1
-  __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x23fd
-  __TEXT.__os_log: 0x1252
-  __TEXT_EXEC.__text: 0x16df0
+349.0.0.0.0
+  __TEXT.__const: 0x278
+  __TEXT.__cstring: 0x2399
+  __TEXT.__os_log: 0x12b0
+  __TEXT_EXEC.__text: 0x16cbc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x308

   __DATA_CONST.__got: 0x118
   __DATA_CONST.__mod_init_func: 0x98
   __DATA_CONST.__mod_term_func: 0x98
-  __DATA_CONST.__const: 0x85b8
+  __DATA_CONST.__const: 0x85d0
   __DATA_CONST.__kalloc_type: 0x4c0
   __DATA_CONST.__kalloc_var: 0x3c0
   Symbols:   0
-  Functions: 0
+  Functions: 809
 

```

>  `com.apple.kec.Compression`

```diff

-171.0.0.0.0
+181.0.0.0.0
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x37dc
+  __TEXT_EXEC.__text: 0x37f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xdc
   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x48
   Symbols:   0
-  Functions: 0
+  Functions: 43
 

```

>  `com.apple.driver.AppleAOPVoiceTrigger`

```diff

-346.6.0.0.0
+400.37.0.0.0
   __TEXT.__cstring: 0x18a0
   __TEXT.__os_log: 0x1d6d
   __TEXT_EXEC.__text: 0x64ac

   __DATA_CONST.__const: 0xd70
   __DATA_CONST.__kalloc_type: 0x180
   Symbols:   0
-  Functions: 0
+  Functions: 144
 

```

>  `com.apple.driver.AppleEmbeddedUSBHost`

```diff

-615.120.5.0.0
+644.0.0.0.0
   __TEXT.__cstring: 0x5a2
   __TEXT.__const: 0x40
-  __TEXT_EXEC.__text: 0x2590
+  __TEXT_EXEC.__text: 0x2584
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x138

   __DATA_CONST.__got: 0x90
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x2b70
+  __DATA_CONST.__const: 0x2b80
   __DATA_CONST.__kalloc_type: 0x180
   Symbols:   0
-  Functions: 0
+  Functions: 119
 

```

>  `com.apple.driver.AppleTypeCPhy`

```diff

-177.120.2.0.0
-  __TEXT.__cstring: 0x134f
-  __TEXT.__const: 0x20
-  __TEXT.__os_log: 0xead
-  __TEXT_EXEC.__text: 0x132d0
+235.0.0.0.2
+  __TEXT.__cstring: 0x1651
+  __TEXT.__const: 0x24
+  __TEXT.__os_log: 0x114c
+  __TEXT_EXEC.__text: 0x12538
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x1218
+  __DATA_CONST.__const: 0x1240
   __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 243
 

```

>  `com.apple.driver.AppleAOPAD5860`

```diff

-740.41.0.0.0
+800.81.0.0.0
   __TEXT.__const: 0x488
   __TEXT.__cstring: 0x89c
-  __TEXT.__os_log: 0x97c
-  __TEXT_EXEC.__text: 0x4f08
+  __TEXT.__os_log: 0xa47
+  __TEXT_EXEC.__text: 0x48bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xcf0
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 76
 

```

>  `com.apple.driver.AppleMobileDispH16P-DCP`

```diff

-337.7.12.5.0
-  __TEXT.__cstring: 0x54c2
-  __TEXT.__const: 0x1a90
-  __TEXT_EXEC.__text: 0x1fc00
+395.12.2.0.0
+  __TEXT.__cstring: 0x5358
+  __TEXT.__const: 0x1a78
+  __TEXT_EXEC.__text: 0x1ffd8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b0
-  __DATA.__common: 0xf8
-  __DATA.__bss: 0x1
-  __DATA_CONST.__auth_got: 0x700
+  __DATA.__common: 0xf0
+  __DATA.__bss: 0x170
+  __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x3c28
+  __DATA_CONST.__const: 0x3dd8
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 0
+  Functions: 1092
 

```

>  `com.apple.driver.ASIOKit`

```diff

-11.77.0.0.0
-  __TEXT.__cstring: 0x1e3
+12.22.0.0.0
+  __TEXT.__cstring: 0x239
   __TEXT.__const: 0x7c40
-  __TEXT_EXEC.__text: 0x33220
+  __TEXT_EXEC.__text: 0x33624
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xd0
+  __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x31d8
+  __DATA_CONST.__const: 0x3278
+  __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 88
 

```

>  `com.apple.driver.AppleSMCWirelessCharger`

```diff

-50.120.2.0.0
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x2793
-  __TEXT.__os_log: 0x4c9
-  __TEXT_EXEC.__text: 0xf718
+72.0.0.0.0
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x28c2
+  __TEXT.__os_log: 0x4b9
+  __TEXT_EXEC.__text: 0xecb4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0xb8
+  __DATA.__common: 0x68
   __DATA.__bss: 0x64
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x1130
-  __DATA_CONST.__kalloc_type: 0x100
+  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0x1e0
   Symbols:   0
-  Functions: 0
+  Functions: 175
 

```

>  `com.apple.driver.AppleSPMIPMU`

```diff

-1345.120.2.0.0
+1350.0.0.0.0
   __TEXT.__cstring: 0x24d1
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xbd54
+  __TEXT_EXEC.__text: 0xbd60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0

   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 154
 

```

>  `com.apple.nke.l2tp`

```diff

 1016.0.0.0.0
   __TEXT.__cstring: 0xb0c
   __TEXT.__const: 0x58
-  __TEXT_EXEC.__text: 0x4080
+  __TEXT_EXEC.__text: 0x4050
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x130
   __DATA.__common: 0x150

   __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 64
 

```

>  `com.apple.driver.AppleCSEmbeddedAudio`

```diff

-740.41.0.0.0
+800.81.0.0.0
   __TEXT.__cstring: 0x594
   __TEXT.__os_log: 0x1ea
   __TEXT.__const: 0x40
-  __TEXT_EXEC.__text: 0xa61c
+  __TEXT_EXEC.__text: 0xa5b8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x198

   __DATA_CONST.__const: 0x3a98
   __DATA_CONST.__kalloc_type: 0x1c0
   Symbols:   0
-  Functions: 0
+  Functions: 244
 

```

>  `com.apple.driver.usb.AppleUSBXHCI`

```diff

-1337.120.6.0.0
-  __TEXT.__const: 0xc4
-  __TEXT.__cstring: 0x5da9
-  __TEXT.__os_log: 0x5d61
-  __TEXT_EXEC.__text: 0x64f14
+1402.0.0.0.0
+  __TEXT.__const: 0xb4
+  __TEXT.__cstring: 0x5dda
+  __TEXT.__os_log: 0x5da8
+  __TEXT_EXEC.__text: 0x57848
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x428
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x90
-  __DATA_CONST.__const: 0x5d78
+  __DATA_CONST.__const: 0x5e10
   __DATA_CONST.__kalloc_type: 0x8c0
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 900
 

```

>  `com.apple.kext.AppleMatch`

```diff

 47.0.0.0.0
   __TEXT.__cstring: 0x5f
-  __TEXT_EXEC.__text: 0x23ac
+  __TEXT_EXEC.__text: 0x23b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xdc
   __DATA_CONST.__auth_got: 0x60

   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 0
+  Functions: 40
 

```

>  `com.apple.driver.AOPTouchKext`

```diff

-312.0.0.0.0
+313.0.0.0.0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x173
   __TEXT.__os_log: 0x12d

   __DATA_CONST.__const: 0xb30
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 81
 

```

>  `com.apple.driver.AppleS5L8960XNCO`

```diff

-194.0.0.0.0
+195.0.0.0.0
   __TEXT.__cstring: 0xb0
-  __TEXT_EXEC.__text: 0x1004
+  __TEXT_EXEC.__text: 0xff0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 0
+  Functions: 45
 

```

>  `com.apple.filesystems.hfs.kext`

```diff

-650.120.1.0.0
-  __TEXT.__const: 0x1a80
+667.0.0.0.1
+  __TEXT.__const: 0x1a98
   __TEXT.__cstring: 0xa17d
-  __TEXT_EXEC.__text: 0x51a04
+  __TEXT_EXEC.__text: 0x51dac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10
   __DATA.__bss: 0x1a4
-  __DATA_CONST.__auth_got: 0xc50
+  __DATA_CONST.__auth_got: 0xc60
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x8

   __DATA_CONST.__kalloc_type: 0x3340
   __DATA_CONST.__kalloc_var: 0x690
   Symbols:   0
-  Functions: 0
+  Functions: 550
 

```

>  `com.apple.driver.AppleEmbeddedMikeyBus`

```diff

-217.0.0.0.0
-  __TEXT.__cstring: 0x1ede
-  __TEXT.__const: 0x78
-  __TEXT_EXEC.__text: 0x187e4
+218.0.0.0.0
+  __TEXT.__cstring: 0x1ee3
+  __TEXT.__const: 0xa8
+  __TEXT_EXEC.__text: 0x187a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x298
   __DATA.__common: 0x240

   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x1e0
   Symbols:   0
-  Functions: 0
+  Functions: 493
 

```

>  `com.apple.driver.ApplePMGR`

```diff

-1374.120.11.0.0
-  __TEXT.__const: 0x250
-  __TEXT.__cstring: 0xdc05
-  __TEXT_EXEC.__text: 0x5028c
+1555.0.2.0.2
+  __TEXT.__const: 0x248
+  __TEXT.__cstring: 0xe6eb
+  __TEXT_EXEC.__text: 0x52650
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x100
-  __DATA.__common: 0x3d0
+  __DATA.__common: 0x420
   __DATA.__bss: 0x40
-  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x63e0
-  __DATA_CONST.__kalloc_type: 0x600
+  __DATA_CONST.__const: 0x7788
+  __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0xdc0
   Symbols:   0
-  Functions: 0
+  Functions: 2159
 

```

>  `com.apple.driver.AppleSEPCredentialManager`

```diff

-660.120.3.0.1
-  __TEXT.__cstring: 0x102b4
-  __TEXT.__const: 0x318
-  __TEXT_EXEC.__text: 0x47ba8
+758.0.14.0.0
+  __TEXT.__cstring: 0x10491
+  __TEXT.__const: 0x320
+  __TEXT_EXEC.__text: 0x47fc4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2191
+  __DATA.__data: 0x2bf1
   __DATA.__common: 0x1d8
-  __DATA.__bss: 0x24d9
+  __DATA.__bss: 0x24f1
   __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x1400
   Symbols:   0
-  Functions: 0
+  Functions: 897
 

```

>  `com.apple.driver.AppleSynopsysMIPIDSI`

```diff

-94.0.0.0.0
+96.0.0.0.0
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x26ea
-  __TEXT_EXEC.__text: 0x8de0
+  __TEXT_EXEC.__text: 0x8e00
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__kalloc_type: 0x100
   __DATA_CONST.__kalloc_var: 0x550
   Symbols:   0
-  Functions: 0
+  Functions: 236
 

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-732.120.3.0.0
-  __TEXT.__cstring: 0xf4df
-  __TEXT.__const: 0x688
-  __TEXT_EXEC.__text: 0x580c0
+768.0.0.0.0
+  __TEXT.__const: 0x6b8
+  __TEXT.__cstring: 0xf7bd
+  __TEXT_EXEC.__text: 0x58bec
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x534
-  __DATA.__common: 0x500
+  __DATA.__data: 0x4e4
+  __DATA.__common: 0x528
   __DATA.__bss: 0x10
   __DATA_CONST.__auth_got: 0x668
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__mod_init_func: 0xf8
-  __DATA_CONST.__mod_term_func: 0xf8
-  __DATA_CONST.__const: 0xc138
-  __DATA_CONST.__kalloc_type: 0x780
-  __DATA_CONST.__kalloc_var: 0x5f0
+  __DATA_CONST.__mod_init_func: 0x100
+  __DATA_CONST.__mod_term_func: 0x100
+  __DATA_CONST.__const: 0xcc18
+  __DATA_CONST.__kalloc_type: 0x7c0
+  __DATA_CONST.__kalloc_var: 0x550
   Symbols:   0
-  Functions: 0
+  Functions: 1706
 

```

>  `com.apple.iokit.IOPCIFamily`

```diff

-617.100.7.0.0
+664.0.2.0.0
   __TEXT.__const: 0x710
-  __TEXT.__cstring: 0x4fad
-  __TEXT_EXEC.__text: 0x2c670
+  __TEXT.__cstring: 0x52ca
+  __TEXT_EXEC.__text: 0x2e168
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x218
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_got: 0x450
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x3c98
+  __DATA_CONST.__const: 0x3d00
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x190
   Symbols:   0
-  Functions: 0
+  Functions: 684
 

```

>  `com.apple.driver.AppleAOPHaptics`

```diff

-740.41.0.0.0
+800.81.0.0.0
   __TEXT.__cstring: 0x60d
   __TEXT.__const: 0x1e8
   __TEXT.__os_log: 0x331
-  __TEXT_EXEC.__text: 0x2e50
+  __TEXT_EXEC.__text: 0x2d40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__const: 0x2238
   __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 135
 

```

>  `com.apple.driver.AppleBluetoothModule`

```diff

-65.0.0.0.0
-  __TEXT.__const: 0x68
+65.1.0.0.0
+  __TEXT.__const: 0x60
   __TEXT.__cstring: 0x25a0
-  __TEXT_EXEC.__text: 0x7bfc
+  __TEXT_EXEC.__text: 0x7c18
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xdc0
   __DATA_CONST.__kalloc_type: 0x180
   Symbols:   0
-  Functions: 0
+  Functions: 141
 

```

>  `com.apple.driver.ApplePhotonDetector`

```diff

-8.600.0.0.0
+9.3.0.0.0
   __TEXT.__cstring: 0x1d7
   __TEXT.__os_log: 0x56e
-  __TEXT_EXEC.__text: 0x2790
+  __TEXT_EXEC.__text: 0x27c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xe48
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 97
 

```

>  `com.apple.iokit.IOGPUFamily`

```diff

-93.40.3.0.0
-  __TEXT.__cstring: 0x3fc1
-  __TEXT.__os_log: 0x30ec
-  __TEXT.__const: 0x84
-  __TEXT_EXEC.__text: 0x30674
+104.0.4.0.0
+  __TEXT.__cstring: 0x502a
+  __TEXT.__os_log: 0x387c
+  __TEXT.__const: 0x7c
+  __TEXT_EXEC.__text: 0x37ce4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x410
-  __DATA.__common: 0x728
+  __DATA.__data: 0x4b0
+  __DATA.__common: 0x780
   __DATA.__bss: 0x9
-  __DATA_CONST.__auth_got: 0x618
+  __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0xe0
-  __DATA_CONST.__mod_term_func: 0xe0
-  __DATA_CONST.__const: 0x5d50
-  __DATA_CONST.__kalloc_type: 0xe80
-  __DATA_CONST.__kalloc_var: 0xa00
+  __DATA_CONST.__mod_init_func: 0xf0
+  __DATA_CONST.__mod_term_func: 0xf0
+  __DATA_CONST.__const: 0x6230
+  __DATA_CONST.__kalloc_type: 0x1000
+  __DATA_CONST.__kalloc_var: 0xf00
   Symbols:   0
-  Functions: 0
+  Functions: 1741
 

```

>  `com.apple.iokit.IOHDCPFamily`

```diff

   __TEXT.__const: 0x38
   __TEXT.__cstring: 0x4369
   __TEXT.__os_log: 0x162e
-  __TEXT_EXEC.__text: 0xeec0
+  __TEXT_EXEC.__text: 0xee1c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__const: 0x1c10
   __DATA_CONST.__kalloc_type: 0x340
   Symbols:   0
-  Functions: 0
+  Functions: 353
 

```

>  `com.apple.driver.AppleIDV`

```diff

-6.504.0.0.0
+7.31.3.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x137c
-  __TEXT_EXEC.__text: 0x80e0
+  __TEXT.__cstring: 0x137d
+  __TEXT_EXEC.__text: 0x84b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__got: 0x50
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xde8
+  __DATA_CONST.__const: 0xe00
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 115
 

```

>  `com.apple.driver.AppleInterruptControllerV3`

```diff

-88.0.0.0.0
-  __TEXT.__cstring: 0x9a9
-  __TEXT_EXEC.__text: 0x40d0
+91.0.0.0.0
+  __TEXT.__cstring: 0x9b8
+  __TEXT_EXEC.__text: 0x4190
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__kalloc_type: 0xc0
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 113
 

```

>  `com.apple.driver.AppleMobileApNonce`

```diff

-31.0.0.0.0
-  __TEXT.__cstring: 0xaee
-  __TEXT.__const: 0x10
-  __TEXT_EXEC.__text: 0x2bb0
+42.0.0.0.0
+  __TEXT.__cstring: 0x10bc
+  __TEXT.__const: 0x12
+  __TEXT_EXEC.__text: 0x372c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 102
 

```

>  `com.apple.iokit.IOUSBMassStorageDriver`

```diff

-245.0.0.0.0
-  __TEXT.__cstring: 0x260e
-  __TEXT.__const: 0x258
-  __TEXT_EXEC.__text: 0x1ec18
+250.0.0.0.0
+  __TEXT.__cstring: 0x2658
+  __TEXT.__const: 0x268
+  __TEXT_EXEC.__text: 0x1f2dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x120
   __DATA.__common: 0x190
   __DATA.__bss: 0x50
-  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x2a70
+  __DATA_CONST.__const: 0x2aa0
   __DATA_CONST.__kalloc_type: 0x3c0
   Symbols:   0
-  Functions: 0
+  Functions: 502
 

```

>  `com.apple.AGXFirmwareKextG16PRTBuddy`

```diff

-282.14.0.0.0
-  __TEXT.__const: 0x127
-  __TEXT.__cstring: 0x5ce
-  __TEXT_EXEC.__text: 0x282c
+320.13.8.0.0
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x673
+  __TEXT_EXEC.__text: 0x27d4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x38
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0xd40
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 71
 

```

>  `com.apple.driver.AppleBasebandPCI`

```diff

-760.0.0.0.0
-  __TEXT.__cstring: 0x392b
-  __TEXT.__const: 0x4f69
-  __TEXT_EXEC.__text: 0x48db8
+807.0.0.0.0
+  __TEXT.__cstring: 0xc352
+  __TEXT.__const: 0x5009
+  __TEXT_EXEC.__text: 0x8883c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x33c
-  __DATA.__common: 0x5c8
-  __DATA.__bss: 0x2e48
-  __DATA_CONST.__auth_got: 0x558
-  __DATA_CONST.__got: 0x178
+  __DATA.__data: 0x3f8
+  __DATA.__common: 0x648
+  __DATA.__bss: 0x3048
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x12f8
-  __DATA_CONST.__mod_term_func: 0xd8
-  __DATA_CONST.__const: 0xf2b0
-  __DATA_CONST.__kalloc_type: 0x1a40
-  __DATA_CONST.__kalloc_var: 0x550
+  __DATA_CONST.__mod_init_func: 0x1350
+  __DATA_CONST.__mod_term_func: 0xf0
+  __DATA_CONST.__const: 0xfe98
+  __DATA_CONST.__kalloc_type: 0x1d80
+  __DATA_CONST.__kalloc_var: 0x690
   Symbols:   0
-  Functions: 0
+  Functions: 2397
 

```

>  `com.apple.driver.AppleS5L8920XPWM`

```diff

-367.0.0.0.0
+368.0.0.0.0
   __TEXT.__cstring: 0x23d
   __TEXT.__os_log: 0xe7
-  __TEXT_EXEC.__text: 0x2858
+  __TEXT_EXEC.__text: 0x289c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xcf0
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 78
 

```

>  `com.apple.driver.AppleUSBHostMergeProperties`

```diff

-1337.120.6.0.0
+1402.0.0.0.0
   __TEXT.__cstring: 0x89
   __TEXT_EXEC.__text: 0xac4
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x600
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 25
 

```

>  `com.apple.driver.AppleUSBLightningAdapter`

```diff

-50.0.0.0.0
+54.0.0.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x1185
   __TEXT.__os_log: 0xa8b
-  __TEXT_EXEC.__text: 0x60a8
+  __TEXT_EXEC.__text: 0x5be0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xe38
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 84
 

```

>  `com.apple.driver.AppleEmbeddedTouchEEPROM`

```diff

-46.0.0.0.0
-  __TEXT.__cstring: 0x96d
-  __TEXT_EXEC.__text: 0x18c0
+49.0.0.0.0
+  __TEXT.__cstring: 0x9f1
+  __TEXT_EXEC.__text: 0x18b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x84

   __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 51
 

```

>  `com.apple.driver.AppleHIDTransportFIFO`

```diff

-7141.1.0.0.0
-  __TEXT.__cstring: 0x2c86
+8100.31.0.0.0
+  __TEXT.__cstring: 0x2de1
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x16848
+  __TEXT_EXEC.__text: 0x16610
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
   __DATA.__bss: 0x1
-  __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x2038
+  __DATA_CONST.__const: 0x2088
   __DATA_CONST.__kalloc_type: 0x400
   Symbols:   0
-  Functions: 0
+  Functions: 280
 

```

>  `com.apple.driver.AppleUSBDeviceNCM`

```diff

-341.120.1.0.1
-  __TEXT.__const: 0x57
-  __TEXT.__cstring: 0xaa5
-  __TEXT_EXEC.__text: 0x779c
+352.0.0.0.0
+  __TEXT.__const: 0x67
+  __TEXT.__cstring: 0xa8a
+  __TEXT_EXEC.__text: 0x75c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
-  __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1698
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 129
 

```

>  `com.apple.driver.AppleAuthCP`

```diff

-144.120.2.0.0
+156.0.0.0.1
   __TEXT.__const: 0x4c
-  __TEXT.__cstring: 0x26c1
-  __TEXT.__os_log: 0x1025
-  __TEXT_EXEC.__text: 0x17bc4
+  __TEXT.__cstring: 0x280a
+  __TEXT.__os_log: 0x12c7
+  __TEXT_EXEC.__text: 0x186e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
-  __DATA.__common: 0x1f0
+  __DATA.__common: 0x218
   __DATA.__bss: 0x2
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__mod_init_func: 0x40
-  __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0x50a0
-  __DATA_CONST.__kalloc_type: 0x680
+  __DATA_CONST.__mod_init_func: 0x48
+  __DATA_CONST.__mod_term_func: 0x48
+  __DATA_CONST.__const: 0x5840
+  __DATA_CONST.__kalloc_type: 0x6c0
   Symbols:   0
-  Functions: 0
+  Functions: 470
 

```

>  `com.apple.iokit.IOAVFamily`

```diff

-446.120.2.0.0
-  __TEXT.__cstring: 0xa99f
-  __TEXT.__os_log: 0x9c42
-  __TEXT.__const: 0xe7c4
-  __TEXT_EXEC.__text: 0x872f8
+482.0.0.0.0
+  __TEXT.__cstring: 0xa8dc
+  __TEXT.__os_log: 0x9ca0
+  __TEXT.__const: 0xe7d4
+  __TEXT_EXEC.__text: 0x84e0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
-  __DATA.__common: 0x9d0
+  __DATA.__common: 0x988
   __DATA.__bss: 0x48
-  __DATA_CONST.__auth_got: 0x4f8
+  __DATA_CONST.__auth_got: 0x4f0
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__mod_init_func: 0x1d0
-  __DATA_CONST.__mod_term_func: 0x1d0
-  __DATA_CONST.__const: 0x14e58
-  __DATA_CONST.__kalloc_type: 0xf00
+  __DATA_CONST.__mod_init_func: 0x1c0
+  __DATA_CONST.__mod_term_func: 0x1c0
+  __DATA_CONST.__const: 0x14170
+  __DATA_CONST.__kalloc_type: 0xe80
   __DATA_CONST.__kalloc_var: 0x1e0
   Symbols:   0
-  Functions: 0
+  Functions: 2950
 

```

>  `com.apple.driver.AppleSEPHDCPManager`

```diff

-82.0.0.0.0
+84.0.0.0.0
   __TEXT.__cstring: 0x82e
   __TEXT.__os_log: 0x58b
-  __TEXT_EXEC.__text: 0x4af8
+  __TEXT_EXEC.__text: 0x4ae0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__const: 0x15d8
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 154
 

```

>  `com.apple.driver.AudioDMAController-T8130`

```diff

-350.2.0.0.0
+400.94.0.0.0
+  __TEXT.__const: 0x1d8
   __TEXT.__cstring: 0x32d3
-  __TEXT.__const: 0x1e0
-  __TEXT_EXEC.__text: 0x15c28
+  __TEXT_EXEC.__text: 0x15b7c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x178

   __DATA_CONST.__const: 0x1988
   __DATA_CONST.__kalloc_type: 0x340
   Symbols:   0
-  Functions: 0
+  Functions: 346
 

```

>  `com.apple.driver.usb.cdc`

```diff

-341.120.1.0.1
-  __TEXT.__cstring: 0x20d
-  __TEXT_EXEC.__text: 0x22f0
+352.0.0.0.0
+  __TEXT.__cstring: 0x210
+  __TEXT_EXEC.__text: 0x22cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xc20
+  __DATA_CONST.__const: 0xc18
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 58
 

```

>  `com.apple.driver.IODARTFamily`

```diff

-341.100.5.0.0
-  __TEXT.__cstring: 0x1ff9
+349.0.0.0.0
+  __TEXT.__cstring: 0x1ffa
   __TEXT.__const: 0x14
-  __TEXT_EXEC.__text: 0x138c8
+  __TEXT_EXEC.__text: 0x13630
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x410
   Symbols:   0
-  Functions: 0
+  Functions: 376
 

```

>  `com.apple.driver.mDNSOffloadUserClient-Embedded`

```diff

-119.120.1.0.0
+122.0.0.0.0
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0xd61
-  __TEXT_EXEC.__text: 0x37f8
+  __TEXT.__cstring: 0x119f
+  __TEXT_EXEC.__text: 0x38c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8

   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 0
+  Functions: 73
 

```

>  `com.apple.iokit.IOSlowAdaptiveClockingFamily`

```diff

-29.0.0.0.0
-  __TEXT.__const: 0x10
+30.0.0.0.0
   __TEXT.__cstring: 0x37d
   __TEXT.__os_log: 0x2c8
-  __TEXT_EXEC.__text: 0x2ee4
+  __TEXT_EXEC.__text: 0x2e98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0x7f8
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 76
 

```

>  `com.apple.driver.AppleDiskImages2`

```diff

-276.120.5.0.2
-  __TEXT.__cstring: 0x2040
+373.0.0.0.0
+  __TEXT.__cstring: 0x2090
   __TEXT.__os_log: 0x11a2
   __TEXT.__const: 0x10
-  __TEXT_EXEC.__text: 0xd32c
+  __TEXT_EXEC.__text: 0xd270
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x498
   __DATA.__common: 0x118

   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 293
 

```

>  `com.apple.driver.AppleHIDTransportSPI`

```diff

-7141.1.0.0.0
-  __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x79b7
-  __TEXT_EXEC.__text: 0x3d310
+8100.31.0.0.0
+  __TEXT.__const: 0x348
+  __TEXT.__cstring: 0x7a73
+  __TEXT_EXEC.__text: 0x3d4b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x31e0
+  __DATA_CONST.__const: 0x3210
   __DATA_CONST.__kalloc_type: 0xa80
   __DATA_CONST.__kalloc_var: 0x320
   Symbols:   0
-  Functions: 0
+  Functions: 655
 

```

>  `com.apple.driver.AppleUSBMike`

```diff

-73.0.0.0.0
-  __TEXT.__const: 0x10
+75.0.0.0.0
+  __TEXT.__const: 0x28
   __TEXT.__cstring: 0xcda
   __TEXT.__os_log: 0x8de
-  __TEXT_EXEC.__text: 0x72f4
+  __TEXT_EXEC.__text: 0x6a0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xec
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0x800
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 72
 

```

>  `com.apple.iokit.IOUSBDeviceFamily`

```diff

-785.120.4.0.0
-  __TEXT.__cstring: 0x284e
-  __TEXT.__const: 0x88
-  __TEXT.__os_log: 0x18bd
-  __TEXT_EXEC.__text: 0x2b2b4
+816.0.0.0.0
+  __TEXT.__cstring: 0x29ba
+  __TEXT.__const: 0x90
+  __TEXT.__os_log: 0x199c
+  __TEXT_EXEC.__text: 0x29494
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x3668
+  __DATA_CONST.__const: 0x3688
   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0x190
   Symbols:   0
-  Functions: 0
+  Functions: 683
 

```

>  `com.apple.driver.AppleParrot`

```diff

-2.0.0.0.0
+3.0.0.0.0
   __TEXT.__cstring: 0x1b3
   __TEXT_EXEC.__text: 0x10a0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x628
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 33
 

```

>  `com.apple.driver.AppleT8130CLPC`

```diff

-994.120.9.0.0
-  __TEXT.__cstring: 0x2b20
-  __TEXT.__const: 0xaf0
-  __TEXT_EXEC.__text: 0x46c54
+1173.0.0.0.1
+  __TEXT.__cstring: 0x2baf
+  __TEXT.__const: 0xb5c
+  __TEXT_EXEC.__text: 0x4a758
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x9428
-  __DATA.__common: 0x7291
+  __DATA.__data: 0x9cd0
+  __DATA.__common: 0x7a91
   __DATA.__bss: 0x268
-  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__auth_got: 0x4a0
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x4a08
+  __DATA_CONST.__const: 0x4da0
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
   Symbols:   0
-  Functions: 0
+  Functions: 1226
 

```

>  `com.apple.driver.AppleUSBXDCI`

```diff

-785.120.4.0.0
-  __TEXT.__cstring: 0x5949
-  __TEXT.__os_log: 0x28b5
-  __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x26c60
+816.0.0.0.0
+  __TEXT.__cstring: 0x5780
+  __TEXT.__os_log: 0x27fd
+  __TEXT.__const: 0x28
+  __TEXT_EXEC.__text: 0x210d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100
-  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x1080
+  __DATA_CONST.__const: 0x10b0
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 283
 

```

>  `com.apple.driver.AppleM68Buttons`

```diff

-124.0.0.0.0
-  __TEXT.__cstring: 0x4a89
+125.0.0.0.0
+  __TEXT.__cstring: 0x48ee
   __TEXT.__const: 0x140
   __TEXT.__os_log: 0x606
-  __TEXT_EXEC.__text: 0x1c2bc
+  __TEXT_EXEC.__text: 0x1bf78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xca
   __DATA.__common: 0x90

   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x1400
   Symbols:   0
-  Functions: 0
+  Functions: 314
 

```

>  `com.apple.driver.AppleOnboardSerial`

```diff

-200.0.0.0.0
+201.0.0.0.0
   __TEXT.__cstring: 0x192e
   __TEXT.__const: 0x68
-  __TEXT_EXEC.__text: 0x11ff0
+  __TEXT_EXEC.__text: 0x11fc0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
   __DATA.__common: 0x2a8

   __DATA_CONST.__const: 0x3280
   __DATA_CONST.__kalloc_type: 0x380
   Symbols:   0
-  Functions: 0
+  Functions: 460
 

```

>  `com.apple.driver.AppleSEPManager`

```diff

-774.120.7.0.0
-  __TEXT.__cstring: 0xf132
-  __TEXT.__const: 0x63e0
-  __TEXT_EXEC.__text: 0x4432c
+834.0.0.0.1
+  __TEXT.__cstring: 0xf955
+  __TEXT.__const: 0x6b0f
+  __TEXT_EXEC.__text: 0x4640c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x168
   __DATA.__common: 0xc48
   __DATA.__bss: 0x4e
-  __DATA_CONST.__auth_got: 0x540
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__auth_got: 0x558
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0x9478
+  __DATA_CONST.__const: 0x9650
   __DATA_CONST.__kalloc_type: 0xdc0
   __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 0
+  Functions: 2305
 

```

>  `com.apple.driver.AppleT8130TypeCPhy`

```diff

-177.120.2.0.0
+235.0.0.0.2
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x81a9
-  __TEXT.__os_log: 0xdfd5
-  __TEXT_EXEC.__text: 0x5ef00
+  __TEXT.__cstring: 0x81fb
+  __TEXT.__os_log: 0xe07d
+  __TEXT_EXEC.__text: 0x4bf6c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2b8
+  __DATA.__data: 0x2c8
   __DATA.__common: 0x58
-  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x818
+  __DATA_CONST.__const: 0x838
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 120
 

```

>  `com.apple.iokit.IOAccessoryPortUSB`

```diff

-971.120.5.0.0
+1000.0.0.0.0
   __TEXT.__cstring: 0x6a0
   __TEXT_EXEC.__text: 0x27f4
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x640
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 43
 

```

>  `com.apple.driver.AppleAVE2`

```diff

-760.30.1.0.0
-  __TEXT.__const: 0x22d10
-  __TEXT.__cstring: 0x29aaa
-  __TEXT.__os_log: 0x303b9
-  __TEXT_EXEC.__text: 0x102684
+802.37.0.0.0
+  __TEXT.__const: 0x28bb0
+  __TEXT.__cstring: 0x33491
+  __TEXT.__os_log: 0x3cb0a
+  __TEXT_EXEC.__text: 0x131e2c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2b0
-  __DATA.__common: 0xb4
-  __DATA.__bss: 0x260
-  __DATA_CONST.__auth_got: 0x398
-  __DATA_CONST.__got: 0xb8
+  __DATA.__data: 0x288
+  __DATA.__common: 0x108
+  __DATA.__bss: 0x300
+  __DATA_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x20
-  __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x46e0
-  __DATA_CONST.__kalloc_type: 0x1540
-  __DATA_CONST.__kalloc_var: 0x8c0
+  __DATA_CONST.__mod_init_func: 0x30
+  __DATA_CONST.__mod_term_func: 0x30
+  __DATA_CONST.__const: 0x5c60
+  __DATA_CONST.__kalloc_type: 0x1e80
+  __DATA_CONST.__kalloc_var: 0x1310
   Symbols:   0
-  Functions: 0
+  Functions: 2344
 

```

>  `com.apple.driver.AppleAstrisGpioProbe`

```diff

 30.0.0.0.0
-  __TEXT.__const: 0xa2
+  __TEXT.__const: 0x8a
   __TEXT.__cstring: 0x6df
-  __TEXT_EXEC.__text: 0x46a4
+  __TEXT_EXEC.__text: 0x4584
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__got_weak: 0x8
   __DATA.__data: 0xcc
   __DATA.__common: 0x64
   __DATA.__bss: 0x1fc
-  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0xef0
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 134
 

```

>  `com.apple.driver.AppleDAPF`

```diff

-11.0.0.0.0
+12.0.0.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x300
-  __TEXT_EXEC.__text: 0xdc8
+  __TEXT_EXEC.__text: 0xdcc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 35
 

```

>  `com.apple.iokit.IOSCSIBlockCommandsDevice`

```diff

-495.0.0.0.0
-  __TEXT.__cstring: 0x658
-  __TEXT_EXEC.__text: 0xcca4
+498.0.0.0.0
+  __TEXT.__cstring: 0x69e
+  __TEXT_EXEC.__text: 0xce58
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a8
   __DATA.__common: 0x98
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x18a0
   __DATA_CONST.__kalloc_type: 0x3c0
   Symbols:   0
-  Functions: 0
+  Functions: 191
 

```

>  `com.apple.kec.Libm`

```diff

-3252.100.9.0.0
-  __TEXT.__const: 0x64a8
-  __TEXT_EXEC.__text: 0x3944
+3287.0.0.0.0
+  __TEXT.__const: 0x6968
+  __TEXT_EXEC.__text: 0x398c
   __DATA.__data: 0xdc
   Symbols:   0
-  Functions: 0
+  Functions: 55
 

```

>  `com.apple.driver.AppleSPMI`

```diff

-87.120.2.0.0
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x214a
-  __TEXT_EXEC.__text: 0x90dc
+100.0.0.0.0
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x21cb
+  __TEXT_EXEC.__text: 0x9bd8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
-  __DATA.__common: 0xd8
+  __DATA.__common: 0x100
   __DATA.__bss: 0x8
   __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__mod_init_func: 0x28
-  __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x31f8
-  __DATA_CONST.__kalloc_type: 0x140
+  __DATA_CONST.__mod_init_func: 0x30
+  __DATA_CONST.__mod_term_func: 0x30
+  __DATA_CONST.__const: 0x3d90
+  __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__kalloc_var: 0x230
   Symbols:   0
-  Functions: 0
+  Functions: 192
 

```

>  `com.apple.driver.AppleT8130`

```diff

-44.0.0.0.0
-  __TEXT.__cstring: 0x5243
+47.0.0.0.0
+  __TEXT.__cstring: 0x54b1
   __TEXT.__const: 0x50
-  __TEXT.__os_log: 0xff3
-  __TEXT_EXEC.__text: 0xb84c
+  __TEXT.__os_log: 0x11ae
+  __TEXT_EXEC.__text: 0xbe2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4e58
   __DATA.__common: 0x108

   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 314
 

```

>  `com.apple.driver.usb.AppleUSBHostBillboardDevice`

```diff

-1337.120.6.0.0
+1402.0.0.0.0
   __TEXT.__cstring: 0x29b
   __TEXT.__os_log: 0x15d
-  __TEXT_EXEC.__text: 0x1ae0
+  __TEXT_EXEC.__text: 0x1770
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 23
 

```

>  `com.apple.filesystems.apfs`

```diff

-2236.122.2.0.0
-  __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x45e95
-  __TEXT_EXEC.__text: 0x130f80
+2301.0.0.0.7
+  __TEXT.__const: 0x6c8
+  __TEXT.__cstring: 0x4816f
+  __TEXT_EXEC.__text: 0x138b5c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x688
+  __DATA.__data: 0x690
   __DATA.__bss: 0xc60
-  __DATA_CONST.__auth_got: 0x1018
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_got: 0x1048
+  __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x5d80
-  __DATA_CONST.__kalloc_type: 0x4dc0
+  __DATA_CONST.__const: 0x6038
+  __DATA_CONST.__kalloc_type: 0x4c80
   __DATA_CONST.__kalloc_var: 0x2800
   Symbols:   0
-  Functions: 0
+  Functions: 2256
 

```

>  `com.apple.driver.AppleBasebandM20`

```diff

-859.1.0.0.0
+927.0.0.0.0
   __TEXT.__const: 0x39d
-  __TEXT.__cstring: 0x26e9
-  __TEXT.__os_log: 0x61ee
-  __TEXT_EXEC.__text: 0x34b28
+  __TEXT.__cstring: 0x6fed
+  __TEXT.__os_log: 0x6645
+  __TEXT_EXEC.__text: 0x39598
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x188
+  __DATA.__data: 0x190
   __DATA.__common: 0x200
-  __DATA.__bss: 0x149
+  __DATA.__bss: 0x181
   __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x60
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x5318
+  __DATA_CONST.__const: 0x5398
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x320
   Symbols:   0
-  Functions: 0
+  Functions: 643
 

```

>  `com.apple.driver.AppleC26Charger`

```diff

-50.120.2.0.0
-  __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x2121
+72.0.0.0.0
+  __TEXT.__const: 0x177
+  __TEXT.__cstring: 0x1ce9
   __TEXT.__os_log: 0x51
-  __TEXT_EXEC.__text: 0x15124
+  __TEXT_EXEC.__text: 0x12660
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x370
-  __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0xf8
+  __DATA.__common: 0x348
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x20
-  __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x5f18
-  __DATA_CONST.__kalloc_type: 0x540
+  __DATA_CONST.__mod_init_func: 0x18
+  __DATA_CONST.__mod_term_func: 0x18
+  __DATA_CONST.__const: 0x58b8
+  __DATA_CONST.__kalloc_type: 0x500
   Symbols:   0
-  Functions: 0
+  Functions: 542
 

```

>  `com.apple.driver.AppleMultitouchDriver`

```diff

-7150.1.0.0.0
-  __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x2133
-  __TEXT.__os_log: 0x2f65
-  __TEXT_EXEC.__text: 0x1ce04
+8100.31.1.0.0
+  __TEXT.__const: 0x1a8
+  __TEXT.__cstring: 0x21f5
+  __TEXT.__os_log: 0x2f71
+  __TEXT_EXEC.__text: 0x1d070
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xca
   __DATA.__common: 0x270

   __DATA_CONST.__got: 0x128
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x4308
+  __DATA_CONST.__const: 0x4310
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__kalloc_type: 0x780
   Symbols:   0
-  Functions: 0
+  Functions: 526
 

```

>  `com.apple.driver.AppleH16PhotonDetector`

```diff

-2.602.0.0.0
-  __TEXT.__cstring: 0x1ea
-  __TEXT.__os_log: 0x5af
-  __TEXT_EXEC.__text: 0x2790
+3.19.5.0.0
+  __TEXT.__cstring: 0x1fd
+  __TEXT.__os_log: 0x606
+  __TEXT_EXEC.__text: 0x2c90
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
+  __DATA.__data: 0xd8
   __DATA.__common: 0x60
   __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe48
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 98
 

```

>  `com.apple.driver.AppleHIDTransport`

```diff

-7141.1.0.0.0
-  __TEXT.__const: 0x28d
-  __TEXT.__cstring: 0x9922
+8100.31.0.0.0
+  __TEXT.__const: 0x2d4
+  __TEXT.__cstring: 0xab57
   __TEXT.__os_log: 0x283
-  __TEXT_EXEC.__text: 0x5f75c
+  __TEXT_EXEC.__text: 0x69af4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x420
-  __DATA_CONST.__auth_got: 0x410
+  __DATA.__bss: 0x98
+  __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__mod_init_func: 0xb8
   __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0x88b8
-  __DATA_CONST.__kalloc_type: 0x940
+  __DATA_CONST.__const: 0x8a88
+  __DATA_CONST.__kalloc_type: 0x9c0
   Symbols:   0
-  Functions: 0
+  Functions: 1189
 

```

>  `com.apple.driver.AppleTopCaseHIDEventDriver`

```diff

-7150.1.0.0.0
-  __TEXT.__cstring: 0xaad
-  __TEXT.__os_log: 0x1086
+8100.20.1.0.0
+  __TEXT.__cstring: 0xbcb
+  __TEXT.__os_log: 0x11a4
   __TEXT.__const: 0x7b
-  __TEXT_EXEC.__text: 0x9dc4
+  __TEXT_EXEC.__text: 0xa8dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x20d0
+  __DATA_CONST.__const: 0x20e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 175
 

```

>  `com.apple.iokit.CoreAnalyticsFamily`

```diff

-381.120.2.0.0
+410.0.0.0.0
   __TEXT.__cstring: 0x1cd3
   __TEXT.__os_log: 0x1639
-  __TEXT_EXEC.__text: 0x79ac
+  __TEXT_EXEC.__text: 0x759c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x108

   __DATA_CONST.__const: 0x1b78
   __DATA_CONST.__kalloc_type: 0x2c0
   Symbols:   0
-  Functions: 0
+  Functions: 136
 

```

>  `com.apple.iokit.IODisplayPortFamily`

```diff

-678.120.2.0.0
-  __TEXT.__const: 0x300
-  __TEXT.__cstring: 0x73f2
-  __TEXT.__os_log: 0x8fd7
-  __TEXT_EXEC.__text: 0x5544c
+729.0.0.0.0
+  __TEXT.__cstring: 0x7c3b
+  __TEXT.__os_log: 0x9571
+  __TEXT.__const: 0x310
+  __TEXT_EXEC.__text: 0x5cfe4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x488
+  __DATA.__common: 0x550
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__mod_init_func: 0xe8
-  __DATA_CONST.__mod_term_func: 0xe0
-  __DATA_CONST.__const: 0xd5a8
-  __DATA_CONST.__kalloc_type: 0x700
+  __DATA_CONST.__auth_got: 0x530
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__mod_init_func: 0x110
+  __DATA_CONST.__mod_term_func: 0x108
+  __DATA_CONST.__const: 0xf880
+  __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0x280
   Symbols:   0
-  Functions: 0
+  Functions: 1961
 

```

>  `com.apple.driver.AppleEmbeddedAudioLibs`

```diff

-340.8.0.0.0
-  __TEXT.__cstring: 0x1bdc
+400.9.0.0.0
+  __TEXT.__cstring: 0x1c16
   __TEXT.__os_log: 0x2c55
-  __TEXT_EXEC.__text: 0xddb4
+  __TEXT_EXEC.__text: 0xcc28
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1a0
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0xf90
   __DATA_CONST.__kalloc_type: 0x200
   Symbols:   0
-  Functions: 0
+  Functions: 204
 

```

>  `com.apple.driver.AppleEmbeddedUSB`

```diff

-615.120.5.0.0
+644.0.0.0.0
   __TEXT.__cstring: 0x10bb
   __TEXT.__const: 0x1c
-  __TEXT_EXEC.__text: 0x89a8
+  __TEXT_EXEC.__text: 0x89c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x270
   __DATA.__common: 0x140

   __DATA_CONST.__const: 0x1808
   __DATA_CONST.__kalloc_type: 0x200
   Symbols:   0
-  Functions: 0
+  Functions: 211
 

```

>  `com.apple.driver.AppleFirmwareUpdateKext`

```diff

-975.120.15.0.0
+1139.0.0.502.1
   __TEXT.__cstring: 0x8f8
-  __TEXT_EXEC.__text: 0x25f4
+  __TEXT_EXEC.__text: 0x25cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 67
 

```

>  `com.apple.kec.pthread`

```diff

-519.120.4.0.0
+535.0.0.0.0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x850
-  __TEXT_EXEC.__text: 0x5e04
+  __TEXT_EXEC.__text: 0x5dec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12c
   __DATA.__common: 0x30

   __DATA_CONST.__const: 0x3f8
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 63
 

```

>  `com.apple.driver.AppleEmbeddedLightSensor`

```diff

-1672.120.23.0.0
-  __TEXT.__const: 0x15e8
-  __TEXT.__cstring: 0x4331
+1835.0.2.0.1
+  __TEXT.__const: 0x15d8
+  __TEXT.__cstring: 0x3f22
   __TEXT.__os_log: 0x2c
-  __TEXT_EXEC.__text: 0x19128
+  __TEXT_EXEC.__text: 0x16328
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x670
-  __DATA.__common: 0x180
-  __DATA_CONST.__auth_got: 0x200
+  __DATA.__data: 0x488
+  __DATA.__common: 0x158
+  __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__mod_init_func: 0x48
-  __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x4a98
-  __DATA_CONST.__kalloc_type: 0x240
+  __DATA_CONST.__mod_init_func: 0x40
+  __DATA_CONST.__mod_term_func: 0x40
+  __DATA_CONST.__const: 0x4280
+  __DATA_CONST.__kalloc_type: 0x200
   Symbols:   0
-  Functions: 0
+  Functions: 339
 

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-147.0.26.0.0
-  __TEXT.__const: 0x25158
-  __TEXT.__cstring: 0x10523
-  __TEXT_EXEC.__text: 0x8d0a8
+148.0.41.0.0
+  __TEXT.__cstring: 0x16484
+  __TEXT.__const: 0x4f738
+  __TEXT_EXEC.__text: 0xd5e6c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x150e4
-  __DATA.__common: 0x1970
-  __DATA.__bss: 0xd20
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__mod_init_func: 0x450
-  __DATA_CONST.__mod_term_func: 0x428
-  __DATA_CONST.__const: 0x1ac00
-  __DATA_CONST.__kalloc_type: 0x2c00
+  __DATA.__data: 0x1fe40
+  __DATA.__common: 0x20a8
+  __DATA.__bss: 0x1068
+  __DATA_CONST.__auth_got: 0x538
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_ptr: 0x88
+  __DATA_CONST.__mod_init_func: 0x570
+  __DATA_CONST.__mod_term_func: 0x548
+  __DATA_CONST.__const: 0x210f8
+  __DATA_CONST.__kalloc_type: 0x3bc0
+  __DATA_CONST.__kalloc_var: 0x500
   Symbols:   0
-  Functions: 0
+  Functions: 6001
 

```

>  `com.apple.driver.RTBuddy`

```diff

-550.120.14.0.0
-  __TEXT.__cstring: 0x9b77
-  __TEXT.__const: 0x280
-  __TEXT_EXEC.__text: 0x41b60
+617.0.0.0.0
+  __TEXT.__cstring: 0x93e8
+  __TEXT.__const: 0x278
+  __TEXT_EXEC.__text: 0x3f8e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
-  __DATA.__common: 0xb48
+  __DATA.__common: 0xb20
   __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__mod_init_func: 0x148
-  __DATA_CONST.__mod_term_func: 0x148
-  __DATA_CONST.__const: 0xa958
-  __DATA_CONST.__kalloc_type: 0x1300
+  __DATA_CONST.__mod_init_func: 0x140
+  __DATA_CONST.__mod_term_func: 0x140
+  __DATA_CONST.__const: 0xa778
+  __DATA_CONST.__kalloc_type: 0x12c0
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 0
+  Functions: 2208
 

```

>  `com.apple.driver.AppleConvergedIPCOLYBTControl`

```diff

-101.2.0.0.0
-  __TEXT.__cstring: 0x7833
+105.0.0.0.0
+  __TEXT.__cstring: 0x7a9f
   __TEXT.__const: 0x98
-  __TEXT_EXEC.__text: 0x46760
+  __TEXT_EXEC.__text: 0x4716c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x4c38
+  __DATA_CONST.__const: 0x4c50
   __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x500
   Symbols:   0
-  Functions: 0
+  Functions: 968
 

```

>  `com.apple.driver.AppleEmbeddedAudio`

```diff

-740.41.0.0.0
-  __TEXT.__cstring: 0x40d8
+800.81.0.0.0
+  __TEXT.__cstring: 0x4144
   __TEXT.__const: 0xd0
-  __TEXT.__os_log: 0x310c
-  __TEXT_EXEC.__text: 0x3a894
+  __TEXT.__os_log: 0x3132
+  __TEXT_EXEC.__text: 0x37754
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x308
   __DATA.__common: 0x458

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78
-  __DATA_CONST.__const: 0xcee8
+  __DATA_CONST.__const: 0xcf60
   __DATA_CONST.__kalloc_type: 0x740
   __DATA_CONST.__kalloc_var: 0xa50
   Symbols:   0
-  Functions: 0
+  Functions: 1011
 

```

>  `com.apple.driver.AppleJPEGDriver`

```diff

-6.6.2.0.0
-  __TEXT.__os_log: 0x972d
-  __TEXT.__cstring: 0x2efe
-  __TEXT.__const: 0x2464
-  __TEXT_EXEC.__text: 0x2a930
+7.1.3.0.0
+  __TEXT.__os_log: 0xc16a
+  __TEXT.__cstring: 0x324f
+  __TEXT.__const: 0x4534
+  __TEXT_EXEC.__text: 0x33b2c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x6f88
-  __DATA.__common: 0x1f0
+  __DATA.__data: 0x8b08
+  __DATA.__common: 0x2b8
   __DATA.__bss: 0x1
   __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__mod_init_func: 0x60
-  __DATA_CONST.__mod_term_func: 0x60
-  __DATA_CONST.__const: 0x1e38
-  __DATA_CONST.__kalloc_type: 0x880
+  __DATA_CONST.__mod_init_func: 0x88
+  __DATA_CONST.__mod_term_func: 0x88
+  __DATA_CONST.__const: 0x2610
+  __DATA_CONST.__kalloc_type: 0xa40
   Symbols:   0
-  Functions: 0
+  Functions: 1165
 

```

>  `com.apple.driver.AppleMikeyBusAudio`

```diff

-340.1.0.0.0
+400.2.1.0.0
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x1934
-  __TEXT.__os_log: 0x221e
-  __TEXT_EXEC.__text: 0x1ace0
+  __TEXT.__cstring: 0x197f
+  __TEXT.__os_log: 0x2269
+  __TEXT_EXEC.__text: 0x188a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x290
   __DATA.__common: 0xd8

   __DATA_CONST.__const: 0x1ff0
   __DATA_CONST.__kalloc_type: 0x240
   Symbols:   0
-  Functions: 0
+  Functions: 291
 

```

>  `com.apple.driver.AppleSPU`

```diff

-957.120.3.0.1
-  __TEXT.__cstring: 0x5957
-  __TEXT.__os_log: 0x725
-  __TEXT.__const: 0x368
-  __TEXT_EXEC.__text: 0x48a58
+1013.0.0.0.1
+  __TEXT.__cstring: 0x5aae
+  __TEXT.__os_log: 0x85b
+  __TEXT.__const: 0x358
+  __TEXT_EXEC.__text: 0x49660
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7b8
-  __DATA.__common: 0x948
-  __DATA.__bss: 0x5b8
-  __DATA_CONST.__auth_got: 0x5d0
+  __DATA.__common: 0x970
+  __DATA.__bss: 0x590
+  __DATA_CONST.__auth_got: 0x5e0
   __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__mod_init_func: 0x178
-  __DATA_CONST.__mod_term_func: 0x178
-  __DATA_CONST.__const: 0x157f0
-  __DATA_CONST.__kalloc_type: 0xe80
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__mod_init_func: 0x180
+  __DATA_CONST.__mod_term_func: 0x180
+  __DATA_CONST.__const: 0x16440
+  __DATA_CONST.__kalloc_type: 0xec0
   __DATA_CONST.__kalloc_var: 0x320
   Symbols:   0
-  Functions: 0
+  Functions: 2065
 

```

>  `com.apple.AGXFirmwareKextRTBuddy64`

```diff

-282.14.0.0.0
+320.13.8.0.0
   __TEXT_EXEC.__text: 0x48
   __DATA.__data: 0xc4
   __DATA.__common: 0x10
   Symbols:   0
-  Functions: 0
+  Functions: 2
 

```

>  `com.apple.driver.AppleARMWatchdogTimer`

```diff

-254.120.4.0.0
-  __TEXT.__cstring: 0x113f
-  __TEXT_EXEC.__text: 0x4d4c
+274.0.0.0.0
+  __TEXT.__cstring: 0x1206
+  __TEXT_EXEC.__text: 0x5018
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x118
   __DATA.__common: 0xc0

   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1380
+  __DATA_CONST.__const: 0x1390
   __DATA_CONST.__kalloc_type: 0xc0
   __DATA_CONST.__kalloc_var: 0x190
   Symbols:   0
-  Functions: 0
+  Functions: 161
 

```

>  `com.apple.driver.AppleBasebandPCIMAVPDP`

```diff

-760.0.0.0.0
+807.0.0.0.0
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0xd87
-  __TEXT_EXEC.__text: 0xc03c
+  __TEXT.__cstring: 0x4c64
+  __TEXT_EXEC.__text: 0x245dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128
   __DATA.__bss: 0xb0
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x70
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x3810
+  __DATA_CONST.__const: 0x3818
   __DATA_CONST.__kalloc_type: 0x400
   Symbols:   0
-  Functions: 0
+  Functions: 363
 

```

>  `com.apple.iokit.IOStreamFamily`

```diff

-119.0.0.0.0
+120.0.0.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x134
-  __TEXT_EXEC.__text: 0x397c
+  __TEXT_EXEC.__text: 0x3990
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__const: 0x16d8
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 161
 

```

>  `com.apple.driver.AppleFAN53740`

```diff

-7.0.0.0.0
+8.0.0.0.0
   __TEXT.__cstring: 0x186
-  __TEXT_EXEC.__text: 0x166c
+  __TEXT_EXEC.__text: 0x1674
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0x728
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 54
 

```

>  `com.apple.security.sandbox`

```diff

-2190.120.12.0.0
-  __TEXT.__const: 0x171dd9
-  __TEXT.__cstring: 0x6549
-  __TEXT.__os_log: 0x1cbb
-  __TEXT_EXEC.__text: 0x2e4b0
+2401.0.31.0.1
+  __TEXT.__const: 0x18ba79
+  __TEXT.__cstring: 0x6f41
+  __TEXT.__os_log: 0x2029
+  __TEXT_EXEC.__text: 0x3062c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x144d0
-  __DATA_CONST.__auth_got: 0x7d8
+  __DATA.__bss: 0x144c0
+  __DATA_CONST.__auth_got: 0x828
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x3450
+  __DATA_CONST.__const: 0x3620
   __DATA_CONST.__kalloc_var: 0x550
-  __DATA_CONST.__kalloc_type: 0xb40
+  __DATA_CONST.__kalloc_type: 0xa80
   Symbols:   0
-  Functions: 0
+  Functions: 648
 

```

>  `com.apple.driver.DCPDPFamilyProxy`

```diff

-143.120.3.0.0
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x356
-  __TEXT.__os_log: 0x1dc
-  __TEXT_EXEC.__text: 0x41c8
+200.0.6.0.0
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x3ac
+  __TEXT.__os_log: 0x232
+  __TEXT_EXEC.__text: 0x4488
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100

   __DATA_CONST.__got: 0x68
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x28b0
+  __DATA_CONST.__const: 0x28c0
   __DATA_CONST.__kalloc_type: 0x180
   Symbols:   0
-  Functions: 0
+  Functions: 192
 

```

>  `com.apple.driver.corecapture`

```diff

-1085.3.0.0.0
+1180.59.0.0.0
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x1e76
-  __TEXT.__os_log: 0x3eb0
-  __TEXT_EXEC.__text: 0x284fc
+  __TEXT.__cstring: 0x1ec9
+  __TEXT.__os_log: 0x4094
+  __TEXT_EXEC.__text: 0x26e20
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x2e0
-  __DATA.__bss: 0x278
+  __DATA.__bss: 0x27c
   __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__mod_init_func: 0x80

   __DATA_CONST.__kalloc_type: 0x1000
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 848
 

```

>  `com.apple.driver.AppleHPM`

```diff

-540.120.2.0.0
-  __TEXT.__cstring: 0x18257
+570.0.0.0.0
+  __TEXT.__cstring: 0x1b286
+  __TEXT.__const: 0xc0
   __TEXT.__os_log: 0x1e8
-  __TEXT.__const: 0x60
-  __TEXT_EXEC.__text: 0x4d114
+  __TEXT_EXEC.__text: 0x5c3dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6d0
   __DATA.__common: 0x518
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x488
+  __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xf8
-  __DATA_CONST.__const: 0x11150
+  __DATA_CONST.__const: 0x111b0
   __DATA_CONST.__kalloc_type: 0xb00
   Symbols:   0
-  Functions: 0
+  Functions: 1394
 

```

>  `com.apple.driver.AppleTriStar`

```diff

-209.0.0.0.0
+212.0.0.0.0
   __TEXT.__const: 0x8f4
-  __TEXT.__cstring: 0x2ff4
+  __TEXT.__cstring: 0x301a
   __TEXT.__os_log: 0x25d
-  __TEXT_EXEC.__text: 0x1da4c
+  __TEXT_EXEC.__text: 0x1da70
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x270

   __DATA_CONST.__const: 0x5cd0
   __DATA_CONST.__kalloc_type: 0x340
   Symbols:   0
-  Functions: 0
+  Functions: 509
 

```

>  `com.apple.driver.AppleUVDM`

```diff

-21.0.0.0.0
+22.0.0.0.0
   __TEXT.__cstring: 0x452
   __TEXT_EXEC.__text: 0x1f40
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0xdc8
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 59
 

```

>  `com.apple.driver.AppleMultitouchSPI`

```diff

-7150.1.0.0.0
+8100.31.1.0.0
   __TEXT.__const: 0x168
   __TEXT.__cstring: 0x3f4b
   __TEXT.__os_log: 0x629
-  __TEXT_EXEC.__text: 0x20a30
+  __TEXT_EXEC.__text: 0x20a7c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x190
   __DATA.__common: 0x178

   __DATA_CONST.__kalloc_type: 0x3c0
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 465
 

```

>  `com.apple.driver.AppleUSBXDCIARM`

```diff

-785.120.4.0.0
+816.0.0.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x3348
-  __TEXT.__os_log: 0x4424
-  __TEXT_EXEC.__text: 0x30870
+  __TEXT.__cstring: 0x33a1
+  __TEXT.__os_log: 0x4ad7
+  __TEXT_EXEC.__text: 0x2bc1c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1a0
-  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x5390
+  __DATA_CONST.__const: 0x5540
   __DATA_CONST.__kalloc_type: 0x240
   Symbols:   0
-  Functions: 0
+  Functions: 277
 

```

>  `com.apple.driver.usb.AppleUSBHub`

```diff

-1337.120.6.0.0
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x227f
-  __TEXT.__os_log: 0x2466
-  __TEXT_EXEC.__text: 0x28594
+1402.0.0.0.0
+  __TEXT.__const: 0x38
+  __TEXT.__cstring: 0x227e
+  __TEXT.__os_log: 0x2465
+  __TEXT_EXEC.__text: 0x224dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1a0

   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x4848
+  __DATA_CONST.__const: 0x4860
   __DATA_CONST.__kalloc_type: 0x280
   Symbols:   0
-  Functions: 0
+  Functions: 310
 

```

>  `com.apple.driver.AppleDCP`

```diff

-590.122.1.0.0
-  __TEXT.__cstring: 0x12a3
+811.0.10.0.1
+  __TEXT.__cstring: 0x1664
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x504c
+  __TEXT_EXEC.__text: 0x5e8c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x1400
+  __DATA_CONST.__const: 0x1438
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 175
 

```

>  `com.apple.driver.AppleGPIOCanary`

```diff

 53.0.0.0.0
   __TEXT.__cstring: 0xee
-  __TEXT_EXEC.__text: 0x820
+  __TEXT_EXEC.__text: 0x830
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 25
 

```

>  `com.apple.driver.AppleSerialShim`

```diff

-10.0.0.0.0
-  __TEXT.__cstring: 0x1d7
-  __TEXT_EXEC.__text: 0xd48
+14.0.0.0.0
+  __TEXT.__cstring: 0x1f2
+  __TEXT_EXEC.__text: 0xc30
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
+  __DATA.__data: 0xc4
   __DATA.__common: 0x38
   __DATA_CONST.__auth_got: 0x70
   __DATA_CONST.__got: 0x18

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 25
 

```

>  `com.apple.iokit.IOCryptoAcceleratorFamily`

```diff

-133.0.0.0.0
+135.0.0.0.0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x52f
-  __TEXT_EXEC.__text: 0x383c
+  __TEXT_EXEC.__text: 0x3868
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x140
   __DATA.__common: 0xc0

   __DATA_CONST.__const: 0x1408
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 107
 

```

>  `com.apple.AGXG16P`

```diff

-282.14.0.0.0
-  __TEXT.__const: 0x4414
-  __TEXT.__cstring: 0xc5d9
-  __TEXT.__os_log: 0x2d8
-  __TEXT_EXEC.__text: 0xa89a8
+320.13.8.0.0
+  __TEXT.__const: 0x443c
+  __TEXT.__cstring: 0xcadf
+  __TEXT.__os_log: 0x2f7
+  __TEXT_EXEC.__text: 0xae2ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13b8
   __DATA.__common: 0x10
-  __DATA.__bss: 0x2598
-  __DATA_CONST.__auth_got: 0xbb0
-  __DATA_CONST.__got: 0x228
+  __DATA.__bss: 0x2950
+  __DATA_CONST.__auth_got: 0xbe8
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x308
-  __DATA_CONST.__mod_term_func: 0x270
-  __DATA_CONST.__const: 0x10418
-  __DATA_CONST.__kalloc_type: 0x2100
+  __DATA_CONST.__mod_init_func: 0x320
+  __DATA_CONST.__mod_term_func: 0x280
+  __DATA_CONST.__const: 0x10b78
+  __DATA_CONST.__kalloc_type: 0x2140
   __DATA_CONST.__kalloc_var: 0x3160
   Symbols:   0
-  Functions: 0
+  Functions: 3067
 

```

>  `com.apple.driver.AppleAVD`

```diff

-742.5.0.0.0
-  __TEXT.__os_log: 0x1ccb0
-  __TEXT.__cstring: 0x10bfe
-  __TEXT.__const: 0x8a1c8
-  __TEXT_EXEC.__text: 0xf087c
+793.9.0.0.0
+  __TEXT.__const: 0x87bee
+  __TEXT.__cstring: 0x4b62
+  __TEXT.__os_log: 0x10103
+  __TEXT_EXEC.__text: 0x48524
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2ac
-  __DATA.__common: 0x90
+  __DATA.__data: 0x1c8c
+  __DATA.__common: 0x80
   __DATA.__bss: 0x14
-  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x5678
-  __DATA_CONST.__kalloc_type: 0x3a80
-  __DATA_CONST.__kalloc_var: 0x1b30
+  __DATA_CONST.__const: 0x2a70
+  __DATA_CONST.__kalloc_var: 0xcd0
+  __DATA_CONST.__kalloc_type: 0x2480
   Symbols:   0
-  Functions: 0
+  Functions: 1397
 

```

>  `com.apple.driver.AppleActuatorDriver`

```diff

-7150.1.0.0.0
+8100.31.1.0.0
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x1283
   __TEXT.__os_log: 0x2f1
-  __TEXT_EXEC.__text: 0xa8f0
+  __TEXT_EXEC.__text: 0xa8d4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xf0

   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x190
   Symbols:   0
-  Functions: 0
+  Functions: 213
 

```

>  `com.apple.driver.usb.ethernet.asix`

```diff

-341.120.1.0.1
+352.0.0.0.0
   __TEXT.__cstring: 0xe36
   __TEXT.__const: 0x270
-  __TEXT_EXEC.__text: 0x12574
+  __TEXT_EXEC.__text: 0x1253c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e8
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x2538
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 229
 

```

>  `com.apple.driver.AppleDialogPMU`

```diff

-1345.120.2.0.0
+1350.0.0.0.0
   __TEXT.__cstring: 0x59e
-  __TEXT_EXEC.__text: 0x2e84
+  __TEXT_EXEC.__text: 0x2e70
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x78

   __DATA_CONST.__const: 0xda8
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 90
 

```

>  `com.apple.driver.AppleUSBDeviceAudioController`

```diff

-640.12.0.0.0
-  __TEXT.__const: 0x70
+701.49.0.0.0
+  __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x2ec
-  __TEXT_EXEC.__text: 0x2ed8
+  __TEXT_EXEC.__text: 0x34f4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
+  __DATA.__data: 0xc4
   __DATA.__common: 0x60
   __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x60

   __DATA_CONST.__const: 0xc28
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 79
 

```

>  `com.apple.driver.IOSlaveProcessor`

```diff

-24.120.1.0.0
+26.0.0.0.0
   __TEXT.__cstring: 0x12e
   __TEXT_EXEC.__text: 0x1924
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x16c8
   __DATA_CONST.__kalloc_type: 0x180
   Symbols:   0
-  Functions: 0
+  Functions: 110
 

```

>  `com.apple.driver.AppleEmbeddedAudioResourceManager`

```diff

-740.41.0.0.0
-  __TEXT.__const: 0x1400
+800.81.0.0.0
+  __TEXT.__const: 0x1e8c
   __TEXT.__cstring: 0x3a3
-  __TEXT.__os_log: 0x3dd
-  __TEXT_EXEC.__text: 0x2ec0
+  __TEXT.__os_log: 0x469
+  __TEXT_EXEC.__text: 0x2b78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x6a0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 45
 

```

>  `com.apple.driver.AppleT8130PMGR`

```diff

-1374.120.11.0.0
-  __TEXT.__const: 0x1250
-  __TEXT.__cstring: 0x1616
-  __TEXT_EXEC.__text: 0xf26c
+1555.0.2.0.2
+  __TEXT.__const: 0x1238
+  __TEXT.__cstring: 0x165a
+  __TEXT_EXEC.__text: 0xf8c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xda8
-  __DATA.__const_weak: 0x3f80
   __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__const: 0x5718
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 588
 

```

>  `com.apple.driver.DiskImages.FileBackingStore`

```diff

-654.120.2.0.0
+662.0.0.0.0
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x237
-  __TEXT_EXEC.__text: 0x1384
+  __TEXT_EXEC.__text: 0x1380
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x678
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 32
 

```

>  `com.apple.driver.AppleEffaceableStorage`

```diff

-86.0.0.0.0
+88.0.0.0.0
   __TEXT.__cstring: 0x148b
   __TEXT.__const: 0x44
-  __TEXT_EXEC.__text: 0x4f88
+  __TEXT_EXEC.__text: 0x4f90
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xc78
   __DATA_CONST.__kalloc_type: 0x300
   Symbols:   0
-  Functions: 0
+  Functions: 142
 

```

>  `com.apple.driver.AppleS8000DWI`

```diff

-129.0.0.0.0
+131.0.0.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x20f
   __TEXT_EXEC.__text: 0x189c

   __DATA_CONST.__const: 0x860
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 65
 

```

>  `com.apple.iokit.IOAudio2Family`

```diff

-340.5.0.0.0
+400.2.0.0.0
   __TEXT.__cstring: 0x3af
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x6070
+  __TEXT_EXEC.__text: 0x6078
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0x1058
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 256
 

```

>  `com.apple.driver.AppleCS35L27Amp`

```diff

-740.41.0.0.0
-  __TEXT.__const: 0x23e0
+800.81.0.0.0
+  __TEXT.__const: 0x23f0
   __TEXT.__cstring: 0x48c5
   __TEXT.__os_log: 0x4bff
-  __TEXT_EXEC.__text: 0x178f8
+  __TEXT_EXEC.__text: 0x14510
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__kalloc_type: 0x40
   __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 0
+  Functions: 161
 

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-2.602.0.0.0
-  __TEXT.__const: 0x9fb0
-  __TEXT.__cstring: 0x18d42
-  __TEXT.__os_log: 0x14f6a
-  __TEXT_EXEC.__text: 0x85a18
+3.19.5.0.0
+  __TEXT.__cstring: 0x194aa
+  __TEXT.__os_log: 0x1526d
+  __TEXT.__const: 0xa050
+  __TEXT_EXEC.__text: 0x986d0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x248
-  __DATA.__common: 0x470
-  __DATA.__bss: 0x1f8
-  __DATA_CONST.__auth_got: 0x888
+  __DATA.__data: 0x2a0
+  __DATA.__common: 0x4a0
+  __DATA.__bss: 0x200
+  __DATA_CONST.__auth_got: 0x890
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x88
-  __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x8848
-  __DATA_CONST.__kalloc_type: 0x1280
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__mod_init_func: 0x90
+  __DATA_CONST.__mod_term_func: 0x50
+  __DATA_CONST.__const: 0xa220
+  __DATA_CONST.__kalloc_type: 0x1300
   __DATA_CONST.__kalloc_var: 0xd70
   Symbols:   0
-  Functions: 0
+  Functions: 1924
 

```

>  `com.apple.driver.ApplePhoneBTM`

```diff

-134.120.2.0.0
+148.0.0.0.0
   __TEXT.__cstring: 0x4207
-  __TEXT.__const: 0x4b0
+  __TEXT.__const: 0x4a0
   __TEXT.__os_log: 0x11d
-  __TEXT_EXEC.__text: 0x16468
+  __TEXT_EXEC.__text: 0x163f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x177
   __DATA.__common: 0x3f8

   __DATA_CONST.__const: 0x33b8
   __DATA_CONST.__kalloc_type: 0x680
   Symbols:   0
-  Functions: 0
+  Functions: 914
 

```

>  `com.apple.driver.usb.networking`

```diff

-341.120.1.0.1
+352.0.0.0.0
   __TEXT.__cstring: 0x24a
-  __TEXT_EXEC.__text: 0x215c
+  __TEXT_EXEC.__text: 0x3110
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x438
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 99
 

```

>  `com.apple.AppleFSCompression.AppleFSCompressionTypeZlib`

```diff

-163.0.0.0.0
+166.0.0.0.0
   __TEXT.__const: 0x3a40
   __TEXT.__cstring: 0x775
-  __TEXT_EXEC.__text: 0xae0c
+  __TEXT_EXEC.__text: 0xabf8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__bss: 0x29

   __DATA_CONST.__kalloc_type: 0x40
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 86
 

```

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-673.120.3.0.0
-  __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x83ca
-  __TEXT.__os_log: 0x3cd9
-  __TEXT_EXEC.__text: 0x35788
+733.0.0.0.0
+  __TEXT.__const: 0x298
+  __TEXT.__cstring: 0x86dc
+  __TEXT.__os_log: 0x3dcc
+  __TEXT_EXEC.__text: 0x35de8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
   __DATA.__common: 0x1d8
-  __DATA.__bss: 0x82
-  __DATA_CONST.__auth_got: 0x588
+  __DATA.__bss: 0x85
+  __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1fc0
-  __DATA_CONST.__kalloc_type: 0x540
+  __DATA_CONST.__const: 0x1ff0
+  __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
   Symbols:   0
-  Functions: 0
+  Functions: 520
 

```

>  `com.apple.driver.AppleS5L8940XI2C`

```diff

-201.40.3.0.0
-  __TEXT.__cstring: 0x783
+206.0.0.0.0
+  __TEXT.__cstring: 0x7b9
+  __TEXT.__const: 0x18
   __TEXT.__os_log: 0x96
-  __TEXT_EXEC.__text: 0x2f38
+  __TEXT_EXEC.__text: 0x2f10
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x650
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 51
 

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

-6728.100.5.0.0
-  __TEXT.__cstring: 0x3022c
-  __TEXT.__const: 0x7e0
-  __TEXT_EXEC.__text: 0x13bf04
+6760.0.0.0.0
+  __TEXT.__cstring: 0x3240d
+  __TEXT.__os_log: 0x2d8f5
+  __TEXT.__const: 0x7f0
+  __TEXT_EXEC.__text: 0x18b590
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
-  __DATA.__common: 0x1210
+  __DATA.__common: 0x1238
   __DATA.__bss: 0x9
-  __DATA_CONST.__auth_got: 0x4b8
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__mod_init_func: 0x398
-  __DATA_CONST.__mod_term_func: 0x398
-  __DATA_CONST.__const: 0x1cf40
-  __DATA_CONST.__kalloc_type: 0x1d00
-  __DATA_CONST.__kalloc_var: 0x910
+  __DATA_CONST.__auth_got: 0x4c0
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__mod_init_func: 0x3a0
+  __DATA_CONST.__mod_term_func: 0x3a0
+  __DATA_CONST.__const: 0x1d920
+  __DATA_CONST.__kalloc_type: 0x1d40
+  __DATA_CONST.__kalloc_var: 0xaf0
   Symbols:   0
-  Functions: 0
+  Functions: 4753
 

```

>  `com.apple.driver.ApplePMPFirmware`

```diff

-967.120.6.0.0
-  __TEXT.__cstring: 0x3c3
-  __TEXT_EXEC.__text: 0x1468
+1173.0.9.0.1
+  __TEXT.__cstring: 0x3d9
+  __TEXT_EXEC.__text: 0x14f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x618
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 33
 

```

>  `com.apple.driver.AppleUSBAudio`

```diff

-640.12.0.0.0
-  __TEXT.__cstring: 0x2d91
-  __TEXT.__const: 0x5b8
-  __TEXT_EXEC.__text: 0x773a4
+701.49.0.0.0
+  __TEXT.__cstring: 0x2dad
+  __TEXT.__const: 0x5b0
+  __TEXT_EXEC.__text: 0x7682c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
+  __DATA.__data: 0xc4
   __DATA.__common: 0x628
   __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x80
   __DATA_CONST.__mod_term_func: 0x80
-  __DATA_CONST.__const: 0x9638
+  __DATA_CONST.__const: 0x9630
   __DATA_CONST.__kalloc_type: 0x9c0
   __DATA_CONST.__kalloc_var: 0x960
   Symbols:   0
-  Functions: 0
+  Functions: 1554
 

```

>  `com.apple.driver.usb.AppleSynopsysUSBXHCI`

```diff

-615.120.5.0.0
-  __TEXT.__cstring: 0x3bd4
-  __TEXT.__os_log: 0x2e57
+644.0.0.0.0
+  __TEXT.__cstring: 0x3d1f
+  __TEXT.__os_log: 0x2fc9
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x293e4
+  __TEXT_EXEC.__text: 0x254f4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x268
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78
-  __DATA_CONST.__const: 0x6ad8
+  __DATA_CONST.__const: 0x6d20
   __DATA_CONST.__kalloc_type: 0x440
   Symbols:   0
-  Functions: 0
+  Functions: 485
 

```

>  `com.apple.iokit.IOCECFamily`

```diff

-60.100.2.0.0
+62.0.0.0.0
   __TEXT.__cstring: 0x403
-  __TEXT_EXEC.__text: 0x2484
+  __TEXT_EXEC.__text: 0x246c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__const: 0x1388
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 103
 

```

>  `com.apple.iokit.IOMikeyBusFamily`

```diff

-102.0.0.0.0
-  __TEXT.__cstring: 0x1052
+103.0.0.0.0
+  __TEXT.__cstring: 0x109d
   __TEXT.__os_log: 0x3de
   __TEXT.__const: 0x208
-  __TEXT_EXEC.__text: 0x1e87c
+  __TEXT_EXEC.__text: 0x1e9e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x488
-  __DATA_CONST.__auth_got: 0x270
+  __DATA.__bss: 0x28
+  __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x68
+  __DATA_CONST.__mod_init_func: 0x70
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x4fc8
-  __DATA_CONST.__kalloc_type: 0x4c0
+  __DATA_CONST.__const: 0x50f0
+  __DATA_CONST.__kalloc_type: 0x540
   __DATA_CONST.__kalloc_var: 0x2d0
   Symbols:   0
-  Functions: 0
+  Functions: 666
 

```

>  `com.apple.driver.AppleEmbeddedPCIE`

```diff

-749.120.3.0.0
-  __TEXT.__cstring: 0x5550
-  __TEXT.__const: 0x178
-  __TEXT_EXEC.__text: 0x1e0e8
+824.0.1.0.1
+  __TEXT.__cstring: 0x57b3
+  __TEXT.__const: 0x198
+  __TEXT_EXEC.__text: 0x13d6c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3d8
+  __DATA.__data: 0xc8
   __DATA.__common: 0x188
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0x2af0
+  __DATA_CONST.__const: 0x2e20
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 491
 

```

>  `com.apple.driver.ApplePTD`

```diff

-19.0.0.0.0
+21.0.0.0.0
   __TEXT.__cstring: 0x1a2e
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x907c
+  __TEXT_EXEC.__text: 0x9074
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0xf0

   __DATA_CONST.__kalloc_type: 0x100
   __DATA_CONST.__kalloc_var: 0x190
   Symbols:   0
-  Functions: 0
+  Functions: 225
 

```

>  `com.apple.driver.AppleSPUSphere`

```diff

-957.120.3.0.1
+1013.0.0.0.1
   __TEXT.__cstring: 0x220
   __TEXT_EXEC.__text: 0x190c
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x748
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 55
 

```

>  `com.apple.driver.AppleSART`

```diff

-19.0.0.0.0
-  __TEXT.__cstring: 0xc3c
-  __TEXT_EXEC.__text: 0x292c
+21.0.0.0.0
+  __TEXT.__cstring: 0xc94
+  __TEXT_EXEC.__text: 0x29e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
-  __DATA_CONST.__auth_got: 0xb8
+  __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1238
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 114
 

```

>  `com.apple.iokit.IOStorageFamily`

```diff

   __DATA_CONST.__kalloc_type: 0x700
   __DATA_CONST.__kalloc_var: 0x320
   Symbols:   0
-  Functions: 0
+  Functions: 578
 

```

>  `com.apple.iokit.IOTimeSyncFamily`

```diff

-1250.2.0.0.0
-  __TEXT.__cstring: 0x31ac
-  __TEXT.__os_log: 0x6fa2
+1300.48.0.0.0
+  __TEXT.__cstring: 0x3298
+  __TEXT.__os_log: 0x749a
   __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x2fd44
+  __TEXT_EXEC.__text: 0x2f3bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
-  __DATA.__common: 0x630
+  __DATA.__common: 0x638
   __DATA.__bss: 0x39
-  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xf8
-  __DATA_CONST.__const: 0xbe08
+  __DATA_CONST.__const: 0xbda0
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0x280
   Symbols:   0
-  Functions: 0
+  Functions: 1202
 

```

>  `com.apple.driver.DiskImages.ReadWriteDiskImage`

```diff

-654.120.2.0.0
+662.0.0.0.0
   __TEXT.__cstring: 0x48
-  __TEXT_EXEC.__text: 0x57c
+  __TEXT_EXEC.__text: 0x578
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x678
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 24
 

```

>  `com.apple.driver.AppleBluetoothDebug`

```diff

-39.0.0.0.0
-  __TEXT.__const: 0x80
+42.0.0.0.0
+  __TEXT.__const: 0x70
   __TEXT.__cstring: 0x17e3
-  __TEXT_EXEC.__text: 0xb3b0
+  __TEXT_EXEC.__text: 0xb428
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf8
   __DATA.__common: 0x90

   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0x190
   Symbols:   0
-  Functions: 0
+  Functions: 165
 

```

>  `com.apple.driver.AppleCS42L77Audio`

```diff

-740.41.0.0.0
-  __TEXT.__cstring: 0x93e4
-  __TEXT.__const: 0xce0
+800.81.0.0.0
+  __TEXT.__cstring: 0x93e5
+  __TEXT.__const: 0xd10
   __TEXT.__os_log: 0xa00a
-  __TEXT_EXEC.__text: 0x47f08
+  __TEXT_EXEC.__text: 0x4091c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x318

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x6f30
+  __DATA_CONST.__const: 0x6f48
   __DATA_CONST.__kalloc_type: 0x400
   Symbols:   0
-  Functions: 0
+  Functions: 857
 

```

>  `com.apple.driver.AppleSPIMC`

```diff

-17.100.4.0.0
-  __TEXT.__const: 0x20
+28.0.0.0.0
+  __TEXT.__const: 0x10
   __TEXT.__cstring: 0x1163
-  __TEXT_EXEC.__text: 0x60f8
+  __TEXT_EXEC.__text: 0x60e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x68

   __DATA_CONST.__const: 0x838
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 79
 

```

>  `com.apple.iokit.IOSCSIArchitectureModelFamily`

```diff

-495.0.0.0.0
+498.0.0.0.0
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x1432
-  __TEXT_EXEC.__text: 0x184f4
+  __TEXT.__cstring: 0x1441
+  __TEXT_EXEC.__text: 0x185b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x418
   __DATA.__common: 0x1c8
   __DATA.__bss: 0x68
-  __DATA_CONST.__auth_got: 0x300
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x60
   __DATA_CONST.__mod_term_func: 0x60

   __DATA_CONST.__kalloc_var: 0x5a0
   __DATA_CONST.__kalloc_type: 0xa80
   Symbols:   0
-  Functions: 0
+  Functions: 657
 

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-7.500.0.0.0
-  __TEXT.__os_log: 0x24c6a
-  __TEXT.__cstring: 0x9d40
-  __TEXT.__const: 0x4e0
-  __TEXT_EXEC.__text: 0x83158
+8.11.4.0.0
+  __TEXT.__os_log: 0x30d37
+  __TEXT.__cstring: 0xabd8
+  __TEXT.__const: 0x5b0
+  __TEXT_EXEC.__text: 0xa05c8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2f90
-  __DATA.__common: 0x370
-  __DATA.__bss: 0x210
-  __DATA_CONST.__auth_got: 0x7e8
-  __DATA_CONST.__got: 0x110
+  __DATA.__data: 0x3058
+  __DATA.__common: 0x3c8
+  __DATA.__bss: 0x270
+  __DATA_CONST.__auth_got: 0x8b0
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x80
+  __DATA_CONST.__mod_init_func: 0x98
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x5870
-  __DATA_CONST.__kalloc_type: 0x2680
-  __DATA_CONST.__kalloc_var: 0x1ef0
+  __DATA_CONST.__const: 0x5f38
+  __DATA_CONST.__kalloc_type: 0x2c80
+  __DATA_CONST.__kalloc_var: 0x2940
   Symbols:   0
-  Functions: 0
+  Functions: 1811
 

```

>  `com.apple.driver.DiskImages.KernelBacked`

```diff

-654.120.2.0.0
+662.0.0.0.0
   __TEXT.__cstring: 0x382
-  __TEXT_EXEC.__text: 0x4818
+  __TEXT_EXEC.__text: 0x46b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x128

   __DATA_CONST.__const: 0x2d28
   __DATA_CONST.__kalloc_type: 0x1c0
   Symbols:   0
-  Functions: 0
+  Functions: 212
 

```

>  `com.apple.iokit.IONetworkingFamily`

```diff

-177.0.0.0.0
-  __TEXT.__const: 0x64
-  __TEXT.__cstring: 0x1b70
-  __TEXT_EXEC.__text: 0x1f33c
+185.0.0.0.0
+  __TEXT.__cstring: 0x127d
+  __TEXT.__const: 0x44
+  __TEXT_EXEC.__text: 0x1d19c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x3b8
   __DATA.__bss: 0x88
-  __DATA_CONST.__auth_got: 0x688
+  __DATA_CONST.__auth_got: 0x690
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__mod_init_func: 0x60
   __DATA_CONST.__mod_term_func: 0x60

   __DATA_CONST.__kalloc_type: 0xa80
   __DATA_CONST.__kalloc_var: 0x230
   Symbols:   0
-  Functions: 0
+  Functions: 870
 

```

>  `com.apple.driver.AppleGPIOICController`

```diff

 53.0.0.0.0
   __TEXT.__cstring: 0xd79
   __TEXT.__const: 0x130
-  __TEXT_EXEC.__text: 0xaac0
+  __TEXT_EXEC.__text: 0xa9b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

   __DATA_CONST.__kalloc_type: 0x1c0
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 0
+  Functions: 263
 

```

>  `com.apple.driver.AppleOLYHAL`

```diff

-210.6.0.0.0
-  __TEXT.__const: 0x728
-  __TEXT.__cstring: 0x4322
-  __TEXT_EXEC.__text: 0x194e8
+336.19.0.0.0
+  __TEXT.__const: 0x798
+  __TEXT.__cstring: 0x4801
+  __TEXT_EXEC.__text: 0x1c7c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170
   __DATA.__bss: 0xc
-  __DATA_CONST.__auth_got: 0x2e8
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x1328
-  __DATA_CONST.__kalloc_type: 0x580
+  __DATA_CONST.__const: 0x1338
+  __DATA_CONST.__kalloc_type: 0x640
   Symbols:   0
-  Functions: 0
+  Functions: 548
 

```

>  `com.apple.driver.usb.cdc.ncm`

```diff

-341.120.1.0.1
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0xcba
-  __TEXT_EXEC.__text: 0x8a2c
+352.0.0.0.0
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0xc5d
+  __TEXT_EXEC.__text: 0x86dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf48
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 144
 

```

>  `com.apple.security.AppleImage4`

```diff

-257.120.3.0.0
-  __TEXT.__const: 0x6ad8
-  __TEXT.__cstring: 0x528b
-  __TEXT.__info_plist: 0x4ed
-  __TEXT_EXEC.__text: 0x20464
+320.0.9.0.0
+  __TEXT.__const: 0x746f
+  __TEXT.__cstring: 0x5e93
+  __TEXT.__info_plist: 0x4e1
+  __TEXT_EXEC.__text: 0x244e4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x640
-  __DATA.__bss: 0x215
+  __DATA.__data: 0x6f8
+  __DATA.__bss: 0x236
   __DATA.__common: 0x88
   __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xa968
-  __DATA_CONST.__kalloc_type: 0x180
+  __DATA_CONST.__const: 0xb5c0
+  __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__image4_exp: 0x10
   Symbols:   0
-  Functions: 0
+  Functions: 1181
 

```

>  `com.apple.driver.AppleInputDeviceSupport`

```diff

-7141.1.0.0.0
-  __TEXT.__cstring: 0x1540
-  __TEXT.__const: 0x48
+8100.31.0.0.0
+  __TEXT.__cstring: 0x1c3d
+  __TEXT.__const: 0x60
   __TEXT.__os_log: 0x63a
-  __TEXT_EXEC.__text: 0x13238
+  __TEXT_EXEC.__text: 0x16928
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x2e0
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__mod_init_func: 0x78
-  __DATA_CONST.__mod_term_func: 0x78
-  __DATA_CONST.__const: 0x30f8
-  __DATA_CONST.__kalloc_type: 0x580
+  __DATA.__common: 0x358
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__mod_init_func: 0x80
+  __DATA_CONST.__mod_term_func: 0x80
+  __DATA_CONST.__const: 0x3540
+  __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0x2d0
   Symbols:   0
-  Functions: 0
+  Functions: 553
 

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-337.7.12.5.0
-  __TEXT.__cstring: 0x87b4
-  __TEXT.__const: 0x938
-  __TEXT_EXEC.__text: 0x420e8
+395.12.2.0.0
+  __TEXT.__cstring: 0x8221
+  __TEXT.__const: 0x800
+  __TEXT_EXEC.__text: 0x22670
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2908
+  __DATA.__data: 0x2900
   __DATA.__common: 0x1c9a4
   __DATA.__bss: 0x18
-  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x5160
+  __DATA_CONST.__const: 0x5dd0
   __DATA_CONST.__kalloc_type: 0xac0
   Symbols:   0
-  Functions: 0
+  Functions: 1131
 

```

>  `com.apple.kernel`

```diff

-10063.122.3.0.0
-  __TEXT.__const: 0x340c0
+11215.0.31.522.1
+  __TEXT.__const: 0x33af0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x65664
-  __TEXT.__os_log: 0x228f2
+  __TEXT.__cstring: 0x6b6db
+  __TEXT.__os_log: 0x26ce8
   __TEXT.__eh_frame: 0x4c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c0
-  __DATA_CONST.__const: 0xa1f98
-  __DATA_CONST.__hib_const: 0x140
-  __DATA_CONST.__kalloc_type: 0x12d00
-  __DATA_CONST.__kalloc_var: 0x7800
-  __DATA_CONST.__brk_desc: 0x60
+  __DATA_CONST.__const: 0xa2390
+  __DATA_CONST.__hib_const: 0x120
+  __DATA_CONST.__kalloc_type: 0x13100
+  __DATA_CONST.__kalloc_var: 0x78f0
+  __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__hib_text: 0xd28
-  __TEXT_EXEC.__text: 0x74cba4
-  __TEXT_BOOT_EXEC.__bootcode: 0x4cf8
+  __TEXT_EXEC.__hib_text: 0xc68
+  __TEXT_EXEC.__text: 0x7fb5d4
+  __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x2050
+  __KLDDATA.__const: 0x23e8
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x17aa9
-  __DATA.__lock_grp: 0x5800
-  __DATA.__percpu: 0x4e50
-  __DATA.__common: 0x577d0
-  __DATA.__bss: 0x3d220
+  __DATA.__data: 0x184e1
+  __DATA.__lock_grp: 0x57a8
+  __DATA.__percpu: 0x6e48
+  __DATA.__common: 0x584d8
+  __DATA.__bss: 0x3f800
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init: 0x5b0e8
-  __BOOTDATA.__init_entry_set: 0x10230
+  __BOOTDATA.__init_entry_set: 0x10758
+  __BOOTDATA.__init: 0x5b058
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __PLK_TEXT_EXEC.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x44bf2
+  __LINKINFO.__symbolsets: 0x4531c
   Symbols:   0
-  Functions: 19223
+  Functions: 19810
 

```

>  `com.apple.driver.AppleConvergedPCI`

```diff

-101.2.0.0.0
-  __TEXT.__const: 0x1e0
+105.0.0.0.0
+  __TEXT.__const: 0x1b0
   __TEXT.__cstring: 0x6c01
-  __TEXT_EXEC.__text: 0x3e4d0
+  __TEXT_EXEC.__text: 0x3e5a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

   __DATA_CONST.__got: 0x108
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x4740
+  __DATA_CONST.__const: 0x4768
   __DATA_CONST.__kalloc_type: 0x1300
   Symbols:   0
-  Functions: 0
+  Functions: 1067
 

```

>  `com.apple.driver.AppleIDAMInterface`

```diff

 24.0.0.0.0
+  __TEXT.__const: 0x8
   __TEXT.__cstring: 0x159
   __TEXT.__os_log: 0x4b7
   __TEXT_EXEC.__text: 0xce8

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 31
 

```

>  `com.apple.iokit.AppleSEPGenericTransfer`

```diff

 28.0.0.0.0
   __TEXT.__cstring: 0x875
   __TEXT.__os_log: 0x3e7
-  __TEXT_EXEC.__text: 0x4914
+  __TEXT_EXEC.__text: 0x490c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__const: 0x378
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 105
 

```

>  `com.apple.plugin.IOgPTPPlugin`

```diff

-1250.2.0.0.0
-  __TEXT.__cstring: 0x6101
-  __TEXT.__os_log: 0x1a273
-  __TEXT.__const: 0x290
-  __TEXT_EXEC.__text: 0x75b98
+1300.48.0.0.0
+  __TEXT.__cstring: 0x6179
+  __TEXT.__os_log: 0x1a456
+  __TEXT.__const: 0x278
+  __TEXT_EXEC.__text: 0x709f4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xcc
+  __DATA.__data: 0xc8
   __DATA.__common: 0x5d8
   __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x110
-  __DATA_CONST.__const: 0xeab8
+  __DATA_CONST.__const: 0xeb08
   __DATA_CONST.__kalloc_type: 0x940
   __DATA_CONST.__kalloc_var: 0x280
   Symbols:   0
-  Functions: 0
+  Functions: 1416
 

```

>  `com.apple.driver.AppleIPAppender`

```diff

-84.0.0.0.0
+106.0.0.0.0
   __TEXT.__cstring: 0x63c
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x568c
+  __TEXT_EXEC.__text: 0x5690
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc9
   __DATA.__common: 0x120

   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 0
+  Functions: 168
 

```

>  `com.apple.driver.AppleMCA2-T8130`

```diff

-840.3.0.0.0
+900.4.0.0.0
   __TEXT.__cstring: 0x6f6f
-  __TEXT.__const: 0x634
+  __TEXT.__const: 0x644
   __TEXT.__os_log: 0x3a
-  __TEXT_EXEC.__text: 0x309cc
+  __TEXT_EXEC.__text: 0x30934
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3c8
   __DATA.__common: 0x678

   __DATA_CONST.__kalloc_type: 0xd40
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 1302
 

```

>  `com.apple.driver.AppleUSBMassStorageInterfaceNub`

```diff

   __DATA_CONST.__const: 0x600
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 30
 

```

>  `com.apple.driver.DiskImages.RAMBackingStore`

```diff

-654.120.2.0.0
+662.0.0.0.0
   __TEXT.__cstring: 0xc8
   __TEXT_EXEC.__text: 0xb54
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x678
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 29
 

```

>  `com.apple.iokit.IOAccessoryManager`

```diff

-971.120.5.0.0
-  __TEXT.__const: 0x330
-  __TEXT.__cstring: 0x10212
-  __TEXT.__os_log: 0xfd4c
-  __TEXT_EXEC.__text: 0x1064f0
+1000.0.0.0.0
+  __TEXT.__const: 0x2f8
+  __TEXT.__cstring: 0x1069c
+  __TEXT.__os_log: 0x10191
+  __TEXT_EXEC.__text: 0xe8540
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
-  __DATA.__common: 0x1590
-  __DATA.__bss: 0x15a
-  __DATA_CONST.__auth_got: 0x5b0
+  __DATA.__common: 0x15b8
+  __DATA.__bss: 0x132
+  __DATA_CONST.__auth_got: 0x5b8
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__mod_init_func: 0x328
+  __DATA_CONST.__mod_init_func: 0x320
   __DATA_CONST.__mod_term_func: 0x318
-  __DATA_CONST.__const: 0x28190
-  __DATA_CONST.__kalloc_type: 0x23c0
+  __DATA_CONST.__const: 0x28668
+  __DATA_CONST.__kalloc_type: 0x2380
   Symbols:   0
-  Functions: 0
+  Functions: 4351
 

```

>  `com.apple.driver.AppleDisplayCrossbar`

```diff

-314.120.5.0.0
-  __TEXT.__cstring: 0x41bd
-  __TEXT.__os_log: 0x5bf1
+354.0.0.0.1
+  __TEXT.__cstring: 0x4413
   __TEXT.__const: 0x160
-  __TEXT_EXEC.__text: 0x320e0
+  __TEXT.__os_log: 0x5d14
+  __TEXT_EXEC.__text: 0x32084
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
-  __DATA.__common: 0x3a8
-  __DATA_CONST.__auth_got: 0x1f0
+  __DATA.__common: 0x3d0
+  __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__mod_init_func: 0xb8
-  __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0xc7e0
-  __DATA_CONST.__kalloc_type: 0x5c0
+  __DATA_CONST.__mod_init_func: 0xc0
+  __DATA_CONST.__mod_term_func: 0xc0
+  __DATA_CONST.__const: 0xd1e0
+  __DATA_CONST.__kalloc_type: 0x600
   Symbols:   0
-  Functions: 0
+  Functions: 1475
 

```

>  `com.apple.driver.AppleProResHW`

```diff

-350.47.0.0.0
-  __TEXT.__const: 0xa250
-  __TEXT.__os_log: 0x337c
-  __TEXT.__cstring: 0x9fe
-  __TEXT_EXEC.__text: 0xe180
+400.59.0.0.0
+  __TEXT.__const: 0x1b48
+  __TEXT.__os_log: 0x7190
+  __TEXT.__cstring: 0xdb7
+  __TEXT_EXEC.__text: 0x182e8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x330
-  __DATA.__common: 0x60
-  __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x228
+  __DATA.__data: 0x358
+  __DATA.__common: 0x70
+  __DATA.__bss: 0xea0
+  __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xc70
-  __DATA_CONST.__kalloc_type: 0x2c0
+  __DATA_CONST.__const: 0x5ac8
+  __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 418
 

```

>  `com.apple.driver.AppleUSBDeviceMux`

```diff

 540.0.0.0.0
   __TEXT.__const: 0x34
   __TEXT.__cstring: 0x1313
-  __TEXT_EXEC.__text: 0x5934
+  __TEXT_EXEC.__text: 0x5924
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68

   __DATA_CONST.__const: 0x780
   __DATA_CONST.__kalloc_type: 0x440
   Symbols:   0
-  Functions: 0
+  Functions: 97
 

```

>  `com.apple.driver.AppleUSBCardReader`

```diff

 556.0.0.0.0
   __TEXT.__cstring: 0xfa1
-  __TEXT.__const: 0x3e0
-  __TEXT_EXEC.__text: 0xafd0
+  __TEXT.__const: 0x3e8
+  __TEXT_EXEC.__text: 0xafc4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x548
   __DATA.__common: 0xe0

   __DATA_CONST.__const: 0x2308
   __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 191
 

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-337.7.12.5.0
-  __TEXT.__cstring: 0x4511
-  __TEXT.__const: 0x23a1
-  __TEXT_EXEC.__text: 0x419cc
+395.12.2.0.0
+  __TEXT.__cstring: 0x4240
+  __TEXT.__const: 0x2158
+  __TEXT_EXEC.__text: 0x2069c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xf8
+  __DATA.__data: 0xe0
   __DATA.__common: 0x26f8
-  __DATA.__bss: 0x4e
-  __DATA_CONST.__auth_got: 0x6d0
+  __DATA.__bss: 0x38
+  __DATA_CONST.__auth_got: 0x6c8
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x1740
+  __DATA_CONST.__const: 0x1778
   __DATA_CONST.__kalloc_type: 0x880
   Symbols:   0
-  Functions: 0
+  Functions: 723
 

```

>  `com.apple.driver.AppleDockChannel`

```diff

-18.0.0.0.0
+19.0.0.0.0
   __TEXT.__cstring: 0x15c3
   __TEXT_EXEC.__text: 0x2d20
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x12e8
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 89
 

```

>  `com.apple.driver.AppleEmbeddedGPS`

```diff

-25.0.0.0.0
+26.0.0.0.0
   __TEXT.__cstring: 0x411
   __TEXT_EXEC.__text: 0x37c0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x1960
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 133
 

```

>  `com.apple.driver.AppleEverestErrorHandler`

```diff

-51.0.0.0.0
+52.0.0.0.0
   __TEXT.__cstring: 0xebf
-  __TEXT_EXEC.__text: 0xf5c
+  __TEXT_EXEC.__text: 0xf60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x39

   __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 39
 

```

>  `com.apple.driver.AppleALSColorSensor`

```diff

-1672.120.23.0.0
+1835.0.2.0.1
   __TEXT.__const: 0x104
-  __TEXT.__cstring: 0x3470
+  __TEXT.__cstring: 0x3653
   __TEXT.__os_log: 0x96
-  __TEXT_EXEC.__text: 0x141d0
+  __TEXT_EXEC.__text: 0x15634
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
-  __DATA.__common: 0x1d0
+  __DATA.__common: 0x1f8
   __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__mod_init_func: 0x58
-  __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x5a38
-  __DATA_CONST.__kalloc_type: 0x340
+  __DATA_CONST.__mod_init_func: 0x60
+  __DATA_CONST.__mod_term_func: 0x60
+  __DATA_CONST.__const: 0x6270
+  __DATA_CONST.__kalloc_type: 0x400
   Symbols:   0
-  Functions: 0
+  Functions: 361
 

```

>  `com.apple.driver.IOAudioCodecs`

```diff

-205.5.2.0.0
-  __TEXT.__cstring: 0x489
-  __TEXT.__const: 0x2710
-  __TEXT_EXEC.__text: 0x48190
+208.1.0.0.0
+  __TEXT.__cstring: 0x487
+  __TEXT.__const: 0x2400
+  __TEXT_EXEC.__text: 0xcb2c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x60a0
-  __DATA.__common: 0x88
-  __DATA_CONST.__auth_got: 0x160
+  __DATA.__data: 0xc8
+  __DATA.__common: 0x60
+  __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x2318
+  __DATA_CONST.__const: 0x21e8
   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0x4b0
   Symbols:   0
-  Functions: 0
+  Functions: 408
 

```

>  `com.apple.driver.usb.AppleUSBCommon`

```diff

-1337.120.6.0.0
-  __TEXT.__cstring: 0x2b6
+1402.0.0.0.0
+  __TEXT.__cstring: 0x301
   __TEXT.__os_log: 0xc6
-  __TEXT_EXEC.__text: 0x4c54
+  __TEXT_EXEC.__text: 0x54b8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0xe8
+  __DATA.__common: 0x110
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__mod_init_func: 0x20
-  __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x818
-  __DATA_CONST.__kalloc_type: 0x240
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__mod_init_func: 0x28
+  __DATA_CONST.__mod_term_func: 0x28
+  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__kalloc_type: 0x280
+  __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 204
 

```

>  `com.apple.iokit.IOUserEthernet`

```diff

-74.0.0.0.0
+75.0.0.0.0
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x9f0
-  __TEXT_EXEC.__text: 0x5438
+  __TEXT.__cstring: 0xa40
+  __TEXT_EXEC.__text: 0x5468
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb8

   __DATA_CONST.__const: 0x1d30
   __DATA_CONST.__kalloc_type: 0x180
   Symbols:   0
-  Functions: 0
+  Functions: 164
 

```

>  `com.apple.nke.ppp`

```diff

 1016.0.0.0.0
   __TEXT.__cstring: 0x1a27
   __TEXT.__const: 0x230
-  __TEXT_EXEC.__text: 0x7630
+  __TEXT_EXEC.__text: 0x7660
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2d0
   __DATA.__bss: 0xa1

   __DATA_CONST.__const: 0x40
   __DATA_CONST.__kalloc_type: 0x300
   Symbols:   0
-  Functions: 0
+  Functions: 113
 

```

>  `com.apple.driver.AppleA7IOP`

```diff

-225.120.5.0.0
-  __TEXT.__cstring: 0xe1e
-  __TEXT_EXEC.__text: 0x5ec0
+257.0.0.0.0
+  __TEXT.__cstring: 0xe4f
+  __TEXT_EXEC.__text: 0x5ff4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__const: 0x1bb8
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 238
 

```

>  `com.apple.driver.AppleSamsungSerial`

```diff

-145.0.0.0.0
+146.0.0.0.0
   __TEXT.__cstring: 0x1bb
   __TEXT_EXEC.__text: 0x1e30
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x6c8
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 56
 

```

>  `com.apple.driver.AppleSmartBatteryManagerEmbedded`

```diff

-1630.120.8.0.0
-  __TEXT.__cstring: 0x4120
-  __TEXT.__const: 0xc70
-  __TEXT.__os_log: 0x268f
-  __TEXT_EXEC.__text: 0x22238
+1725.0.0.0.0
+  __TEXT.__cstring: 0x421c
+  __TEXT.__const: 0x14b0
+  __TEXT.__os_log: 0x25f9
+  __TEXT_EXEC.__text: 0x220dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x208
   __DATA.__common: 0x150
-  __DATA.__bss: 0x2e78
-  __DATA_CONST.__auth_got: 0x398
+  __DATA.__bss: 0x2f30
+  __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
   __DATA_CONST.__const: 0x2dc0
   __DATA_CONST.__kalloc_type: 0x340
   Symbols:   0
-  Functions: 0
+  Functions: 383
 

```

>  `com.apple.AUC`

```diff

-516.2.0.0.0
+542.4.0.0.0
   __TEXT.__cstring: 0x947
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x56e4
+  __TEXT_EXEC.__text: 0x55e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc5
   __DATA.__common: 0xb0

   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0xfc8
+  __DATA_CONST.__const: 0xfb0
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 221
 

```

>  `com.apple.driver.AppleUSBTopCaseDriver`

```diff

-7150.1.0.0.0
+8100.20.1.0.0
   __TEXT.__cstring: 0x75
   __TEXT.__os_log: 0x135
   __TEXT_EXEC.__text: 0x618

   __DATA_CONST.__const: 0x790
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 23
 

```

>  `com.apple.filesystems.tmpfs`

```diff

-75.0.0.0.0
-  __TEXT.__cstring: 0x5ed
+79.0.0.0.0
+  __TEXT.__cstring: 0x5da
   __TEXT.__const: 0x40
   __TEXT.__os_log: 0x20a
-  __TEXT_EXEC.__text: 0x9efc
+  __TEXT_EXEC.__text: 0x9770
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x180
   __DATA.__bss: 0x8

   __DATA_CONST.__const: 0x4d0
   __DATA_CONST.__kalloc_type: 0x480
   Symbols:   0
-  Functions: 0
+  Functions: 157
 

```

>  `com.apple.driver.AppleA7IOP-ASCWrap-v6`

```diff

-225.120.5.0.0
-  __TEXT.__cstring: 0x40d
-  __TEXT_EXEC.__text: 0x1920
+257.0.0.0.0
+  __TEXT.__cstring: 0x472
+  __TEXT_EXEC.__text: 0x1ea4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xd8
+  __DATA.__common: 0x88
+  __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__mod_init_func: 0x10
-  __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xf20
-  __DATA_CONST.__kalloc_type: 0x80
+  __DATA_CONST.__mod_init_func: 0x18
+  __DATA_CONST.__mod_term_func: 0x18
+  __DATA_CONST.__const: 0x16b0
+  __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 115
 

```

>  `com.apple.driver.AppleFirmwareKit`

```diff

-454.120.7.0.1
-  __TEXT.__os_log: 0x1d3f
-  __TEXT.__cstring: 0x2b5d
-  __TEXT.__const: 0x2e0
-  __TEXT_EXEC.__text: 0x45bc8
+529.0.0.0.0
+  __TEXT.__cstring: 0x2781
+  __TEXT.__os_log: 0x1098
+  __TEXT.__const: 0xc0
+  __TEXT_EXEC.__text: 0x36614
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x578
-  __DATA.__common: 0x790
-  __DATA.__bss: 0x20
-  __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x158
+  __DATA.__data: 0x3f8
+  __DATA.__common: 0x700
+  __DATA.__bss: 0xc8
+  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__mod_init_func: 0x100
-  __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0xd7b8
-  __DATA_CONST.__kalloc_type: 0x1780
-  __DATA_CONST.__kalloc_var: 0xa0
+  __DATA_CONST.__mod_init_func: 0xf0
+  __DATA_CONST.__mod_term_func: 0xf0
+  __DATA_CONST.__const: 0xd348
+  __DATA_CONST.__kalloc_type: 0x17c0
+  __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 0
+  Functions: 1624
 

```

>  `com.apple.driver.AppleHapticsSupportNVM`

```diff

-8.11.0.0.0
+9.17.0.0.0
   __TEXT.__const: 0x59
   __TEXT.__cstring: 0x343
-  __TEXT_EXEC.__text: 0x97c
+  __TEXT_EXEC.__text: 0x964
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 27
 

```

>  `com.apple.driver.FairPlayIOKit`

```diff

-71.10.0.0.0
+72.8.0.0.0
   __TEXT.__cstring: 0x1c95
-  __TEXT.__const: 0x44480
-  __TEXT_EXEC.__text: 0x1709c4
+  __TEXT.__const: 0x499b0
+  __TEXT_EXEC.__text: 0x1ad084
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x1220
-  __DATA.__common: 0x5fe0
+  __DATA.__data: 0x12d0
+  __DATA.__common: 0x5fd8
   __DATA.__bss: 0x38
   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x123c0
-  __DATA_CONST.__kalloc_type: 0x1a00
+  __DATA_CONST.__const: 0x138b0
+  __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x370
   Symbols:   0
-  Functions: 0
+  Functions: 436
 

```

>  `com.apple.driver.usb.AppleUSBHostCompositeDevice`

```diff

-1337.120.6.0.0
-  __TEXT.__cstring: 0x4de
-  __TEXT.__os_log: 0x358
-  __TEXT_EXEC.__text: 0x4294
+1402.0.0.0.0
+  __TEXT.__cstring: 0x41b
+  __TEXT.__os_log: 0x206
+  __TEXT_EXEC.__text: 0x3570
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x920
+  __DATA_CONST.__const: 0x918
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 67
 

```

>  `com.apple.driver.AppleAOPAudio`

```diff

-340.4.0.0.0
-  __TEXT.__cstring: 0xc598
+400.7.0.0.0
+  __TEXT.__cstring: 0xc5b3
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
-  __TEXT_EXEC.__text: 0x329a0
+  __TEXT_EXEC.__text: 0x32968
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2f0
   __DATA.__common: 0x660
   __DATA.__bss: 0x49
-  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0xe8

   __DATA_CONST.__const: 0xb7c8
   __DATA_CONST.__kalloc_type: 0xa00
   Symbols:   0
-  Functions: 0
+  Functions: 1277
 

```

>  `com.apple.driver.AppleGenericMultitouch`

```diff

   __TEXT.__cstring: 0x6115
   __TEXT.__const: 0x21e
   __TEXT.__os_log: 0x6c4
-  __TEXT_EXEC.__text: 0x6d08
+  __TEXT_EXEC.__text: 0x6cf0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd4
   __DATA.__common: 0x80

   __DATA_CONST.__const: 0x1640
   __DATA_CONST.__kalloc_type: 0x1c0
   Symbols:   0
-  Functions: 0
+  Functions: 168
 

```

>  `com.apple.driver.AppleHIDKeyboard`

```diff

-7140.2.0.0.0
-  __TEXT.__cstring: 0x7dc
-  __TEXT.__os_log: 0x84f
+8100.5.0.0.0
+  __TEXT.__cstring: 0x806
+  __TEXT.__os_log: 0x907
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x697c
+  __TEXT_EXEC.__text: 0x69e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
-  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1898
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 114
 

```

>  `com.apple.driver.AppleT8110DART`

```diff

-417.120.2.0.0
+447.0.0.0.1
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2758
-  __TEXT_EXEC.__text: 0xcf18
+  __TEXT.__cstring: 0x2757
+  __TEXT_EXEC.__text: 0xd25c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x758
   __DATA_CONST.__kalloc_type: 0x2c0
-  __DATA_CONST.__kalloc_var: 0x370
+  __DATA_CONST.__kalloc_var: 0x410
   Symbols:   0
-  Functions: 0
+  Functions: 148
 

```

>  `com.apple.iokit.IOBiometricFamily`

```diff

-471.100.9.0.0
+504.0.0.0.0
   __TEXT.__os_log: 0x1301
   __TEXT.__cstring: 0x1a9b
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x10e30
+  __TEXT_EXEC.__text: 0x10ae8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x3c0

   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 492
 

```

>  `com.apple.IOTextEncryptionFamily`

```diff

   __DATA_CONST.__const: 0xe68
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 88
 

```

>  `com.apple.driver.usb.AppleUSBHostPacketFilter`

```diff

-1337.120.6.0.0
+1402.0.0.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xa5a
   __TEXT.__os_log: 0xaf
-  __TEXT_EXEC.__text: 0x1da8
+  __TEXT_EXEC.__text: 0x1d94
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x48

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 38
 

```

>  `com.apple.iokit.AppleARMIISAudio`

```diff

-346.4.0.0.0
+400.20.0.0.0
   __TEXT.__os_log: 0x2778
-  __TEXT.__cstring: 0x2dc8
-  __TEXT.__const: 0xc8
-  __TEXT_EXEC.__text: 0x19130
+  __TEXT.__cstring: 0x2dc9
+  __TEXT.__const: 0xa8
+  __TEXT_EXEC.__text: 0x15688
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x1138
+  __DATA_CONST.__const: 0x1150
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0x1e0
   Symbols:   0
-  Functions: 0
+  Functions: 217
 

```

>  `com.apple.iokit.IOHIDFamily`

```diff

-2031.120.4.0.0
+2094.0.0.0.0
   __TEXT.__cstring: 0x24b3
-  __TEXT.__const: 0x6b8
-  __TEXT.__os_log: 0x29a0
-  __TEXT_EXEC.__text: 0x65474
+  __TEXT.__const: 0x6c8
+  __TEXT.__os_log: 0x2a2f
+  __TEXT_EXEC.__text: 0x6288c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xbcc
   __DATA.__common: 0x748

   __DATA_CONST.__const: 0x9ff0
   __DATA_CONST.__kalloc_type: 0x1480
   Symbols:   0
-  Functions: 0
+  Functions: 1859
 

```

>  `com.apple.driver.AppleBluetoothDebugService`

```diff

-39.0.0.0.0
+42.0.0.0.0
   __TEXT.__cstring: 0x35
   __TEXT_EXEC.__text: 0x304
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x610
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 26
 

```

>  `com.apple.driver.AppleH10PearlCameraInterface`

```diff

-20.500.1.0.0
+21.0.0.0.0
   __TEXT.__cstring: 0x67b
   __TEXT.__os_log: 0x130
-  __TEXT_EXEC.__text: 0x79e8
+  __TEXT_EXEC.__text: 0x79e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x2e0

   __DATA_CONST.__const: 0x1b48
   __DATA_CONST.__kalloc_type: 0x480
   Symbols:   0
-  Functions: 0
+  Functions: 391
 

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1655.120.10.0.0
-  __TEXT.__cstring: 0x3974
-  __TEXT.__const: 0x814
-  __TEXT_EXEC.__text: 0x3b698
+1827.0.30.0.1
+  __TEXT.__cstring: 0x3aba
+  __TEXT.__const: 0x864
+  __TEXT_EXEC.__text: 0x3d4d0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x378
+  __DATA.__data: 0x39c
   __DATA.__common: 0xe8
-  __DATA.__bss: 0x265
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x90
+  __DATA.__bss: 0x2f4
+  __DATA_CONST.__auth_got: 0x488
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x39b0
+  __DATA_CONST.__const: 0x3a68
   __DATA_CONST.__kalloc_type: 0xd40
-  __DATA_CONST.__kalloc_var: 0x140
+  __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 671
 

```

>  `com.apple.driver.AppleUSBEthernetDevice`

```diff

-159.0.0.0.0
+161.0.0.0.0
+  __TEXT.__const: 0x16
   __TEXT.__cstring: 0xbc4
-  __TEXT.__const: 0x6
-  __TEXT_EXEC.__text: 0x3e28
+  __TEXT_EXEC.__text: 0x3e30
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__kalloc_type: 0xc0
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 99
 

```

>  `com.apple.driver.usb.IOUSBHostHIDDevice`

```diff

-1337.120.6.0.0
+1402.0.0.0.0
   __TEXT.__cstring: 0xac4
   __TEXT.__os_log: 0x9af
-  __TEXT_EXEC.__text: 0x8aac
+  __TEXT_EXEC.__text: 0x7f5c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xf20
   __DATA_CONST.__kalloc_type: 0x200
   Symbols:   0
-  Functions: 0
+  Functions: 86
 

```

>  `com.apple.iokit.IOUSBHostFamily`

```diff

-1337.120.6.0.0
-  __TEXT.__cstring: 0x9912
-  __TEXT.__os_log: 0x814a
-  __TEXT.__const: 0xa30
-  __TEXT_EXEC.__text: 0xaad70
+1402.0.0.0.0
+  __TEXT.__cstring: 0x9b8c
+  __TEXT.__os_log: 0x81a1
+  __TEXT.__const: 0xa90
+  __TEXT_EXEC.__text: 0x991ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x310
-  __DATA.__common: 0x928
+  __DATA.__common: 0x930
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x590
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__auth_got: 0x5a8
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__mod_init_func: 0xe8
   __DATA_CONST.__mod_term_func: 0xe0
-  __DATA_CONST.__const: 0xcb50
-  __DATA_CONST.__kalloc_type: 0x1cc0
+  __DATA_CONST.__const: 0xcca8
+  __DATA_CONST.__kalloc_type: 0x1c40
   __DATA_CONST.__kalloc_var: 0x280
   Symbols:   0
-  Functions: 0
+  Functions: 1949
 

```

>  `com.apple.driver.AppleGameControllerPersonality`

```diff

-11.5.1.0.0
+12.0.31.0.0
   __TEXT.__cstring: 0xd4
   __TEXT.__os_log: 0x53
   __TEXT_EXEC.__text: 0x7b8

   __DATA_CONST.__const: 0x788
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 26
 

```

>  `com.apple.driver.AppleSSE`

```diff

-282.100.5.0.0
-  __TEXT.__cstring: 0x163e
+294.0.0.0.0
+  __TEXT.__cstring: 0x16ba
   __TEXT.__const: 0xc8
-  __TEXT_EXEC.__text: 0x7ad8
+  __TEXT_EXEC.__text: 0x7db8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
+  __DATA.__bss: 0x4
   __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__mod_init_func: 0x18

   __DATA_CONST.__const: 0x12f8
   __DATA_CONST.__kalloc_type: 0xc0
   Symbols:   0
-  Functions: 0
+  Functions: 115
 

```

>  `com.apple.driver.AppleTemperatureSensor`

```diff

 56.0.0.0.0
   __TEXT.__cstring: 0xdd6
-  __TEXT.__const: 0x134
+  __TEXT.__const: 0x11c
   __TEXT.__os_log: 0x50
-  __TEXT_EXEC.__text: 0xa754
+  __TEXT_EXEC.__text: 0xa66c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x308
   __DATA.__common: 0x1a8

   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 0
+  Functions: 355
 

```

>  `com.apple.driver.AppleS8000AES`

```diff

-129.0.0.0.0
+131.0.0.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x1301
-  __TEXT_EXEC.__text: 0x4578
+  __TEXT_EXEC.__text: 0x44fc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x1e8
+  __DATA.__data: 0x200
   __DATA.__common: 0x60
   __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x40

   __DATA_CONST.__const: 0x790
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 108
 

```

>  `com.apple.driver.AppleSmartIO2`

```diff

-135.0.0.0.0
-  __TEXT.__cstring: 0x4506
+140.0.0.0.0
+  __TEXT.__cstring: 0x451b
   __TEXT.__const: 0x60
-  __TEXT_EXEC.__text: 0xc488
+  __TEXT_EXEC.__text: 0xc4b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7f8
   __DATA.__common: 0x1a0

   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 471
 

```

>  `com.apple.driver.IISAudioIsolatedStreamECProxy`

```diff

-346.4.0.0.0
-  __TEXT.__cstring: 0x1db
-  __TEXT.__os_log: 0xd9
-  __TEXT_EXEC.__text: 0xc68
+400.20.0.0.0
+  __TEXT.__cstring: 0x2d2
+  __TEXT.__os_log: 0x1b2
+  __TEXT_EXEC.__text: 0x1118
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x68
+  __DATA_CONST.__auth_got: 0x98
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f8
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 34
 

```

>  `com.apple.driver.AppleAudioClockLibs`

```diff

-340.8.0.0.0
+400.9.0.0.0
   __TEXT.__os_log: 0x103
   __TEXT.__cstring: 0x200
-  __TEXT_EXEC.__text: 0x83c
+  __TEXT_EXEC.__text: 0x81c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x10

   __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__got: 0x10
   Symbols:   0
-  Functions: 0
+  Functions: 13
 

```

>  `com.apple.driver.AppleDiagnosticDataAccessReadOnly`

```diff

-46.0.0.0.0
+50.0.0.0.0
   __TEXT.__cstring: 0x184
-  __TEXT_EXEC.__text: 0xd80
+  __TEXT.__const: 0x8
+  __TEXT_EXEC.__text: 0xdf4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38
   __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0xb8
+  __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f8
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 35
 

```

>  `com.apple.driver.AppleEventLogHandler`

```diff

-1374.120.11.0.0
+1555.0.2.0.2
   __TEXT.__cstring: 0x4cf
-  __TEXT_EXEC.__text: 0x13e0
+  __TEXT_EXEC.__text: 0x13e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__kalloc_type: 0x40
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 0
+  Functions: 48
 

```

>  `com.apple.driver.AppleT8130PCIe`

```diff

-749.120.3.0.0
-  __TEXT.__cstring: 0x1785
+824.0.1.0.1
+  __TEXT.__cstring: 0x1748
   __TEXT.__const: 0xb6
-  __TEXT_EXEC.__text: 0x92f0
+  __TEXT_EXEC.__text: 0x6e04
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x240
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__const: 0x11b8
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 183
 

```

>  `com.apple.driver.AppleUVDMDriver`

```diff

-21.0.0.0.0
+22.0.0.0.0
   __TEXT.__cstring: 0x13a6
-  __TEXT_EXEC.__text: 0x70f0
+  __TEXT.__const: 0x20
+  __TEXT_EXEC.__text: 0x7184
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0xb0

   __DATA_CONST.__const: 0x1098
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 132
 

```

>  `com.apple.driver.usb.cdc.ecm`

```diff

-341.120.1.0.1
-  __TEXT.__const: 0x38
+352.0.0.0.0
   __TEXT.__cstring: 0x32c
-  __TEXT_EXEC.__text: 0x40dc
+  __TEXT.__const: 0x28
+  __TEXT_EXEC.__text: 0x408c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e8
   __DATA.__common: 0x88

   __DATA_CONST.__const: 0x17b8
   __DATA_CONST.__kalloc_type: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 127
 

```

>  `com.apple.iokit.IOSurface`

```diff

-352.50.1.0.0
-  __TEXT.__cstring: 0x4fc8
+368.0.0.0.0
+  __TEXT.__cstring: 0x4fbb
   __TEXT.__const: 0x48
   __TEXT.__os_log: 0x530
-  __TEXT_EXEC.__text: 0x2c990
+  __TEXT_EXEC.__text: 0x2d538
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x178
   __DATA.__common: 0x3e8
   __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0x458
+  __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78
-  __DATA_CONST.__const: 0x3ed0
-  __DATA_CONST.__kalloc_type: 0xb40
+  __DATA_CONST.__const: 0x3fc0
+  __DATA_CONST.__kalloc_type: 0xb80
   __DATA_CONST.__kalloc_var: 0x8c0
   Symbols:   0
-  Functions: 0
+  Functions: 1191
 

```

>  `com.apple.driver.AppleBSDKextStarter`

```diff

-17.0.0.0.0
+18.0.0.0.0
   __TEXT.__cstring: 0xb2
   __TEXT_EXEC.__text: 0x5c8
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 25
 

```

>  `com.apple.driver.AppleProxDriver`

```diff

-31.7.0.0.0
-  __TEXT.__cstring: 0x819
-  __TEXT.__os_log: 0x5d9
-  __TEXT.__const: 0x28
-  __TEXT_EXEC.__text: 0xa92c
+40.0.0.0.0
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x826
+  __TEXT.__os_log: 0x607
+  __TEXT_EXEC.__text: 0xa9c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x160
+  __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x2118
   __DATA_CONST.__kalloc_type: 0x200
   Symbols:   0
-  Functions: 0
+  Functions: 158
 

```

>  `com.apple.driver.AppleSMC`

```diff

-689.120.3.0.0
-  __TEXT.__cstring: 0x75bd
-  __TEXT.__const: 0x1a4
-  __TEXT.__os_log: 0x20f
-  __TEXT_EXEC.__text: 0x23ff0
+725.0.0.0.0
+  __TEXT.__cstring: 0x859f
+  __TEXT.__const: 0x1e4
+  __TEXT.__os_log: 0xd26
+  __TEXT_EXEC.__text: 0x298e0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4
-  __DATA.__common: 0x3f8
-  __DATA.__bss: 0x88
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x198
+  __DATA.__data: 0xcc
+  __DATA.__common: 0x4b8
+  __DATA.__bss: 0x110
+  __DATA_CONST.__auth_got: 0x538
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x90
-  __DATA_CONST.__mod_term_func: 0x88
-  __DATA_CONST.__const: 0x7618
-  __DATA_CONST.__kalloc_type: 0x680
+  __DATA_CONST.__mod_init_func: 0xc0
+  __DATA_CONST.__mod_term_func: 0xa8
+  __DATA_CONST.__const: 0x8c98
+  __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 0
+  Functions: 929
 

```

>  `com.apple.iokit.IOSkywalkFamily`

```diff

-464.120.2.0.0
-  __TEXT.__cstring: 0x1aff
+508.0.0.0.0
+  __TEXT.__cstring: 0x1ade
   __TEXT.__const: 0xd40
-  __TEXT_EXEC.__text: 0x3722c
+  __TEXT_EXEC.__text: 0x35dfc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe8
   __DATA.__common: 0x6b0
   __DATA.__bss: 0x9c
-  __DATA_CONST.__auth_got: 0xa30
+  __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x130
   __DATA_CONST.__mod_term_func: 0x130
-  __DATA_CONST.__const: 0x8d00
+  __DATA_CONST.__const: 0x8cd0
   __DATA_CONST.__kalloc_type: 0x1640
-  __DATA_CONST.__kalloc_var: 0x6e0
+  __DATA_CONST.__kalloc_var: 0x640
   Symbols:   0
-  Functions: 0
+  Functions: 1853
 

```

>  `com.apple.driver.AppleARMPlatform`

```diff

-1026.120.7.0.0
-  __TEXT.__const: 0x16f0
+1066.0.0.0.0
+  __TEXT.__const: 0x16f8
   __TEXT.__os_log: 0x13fe
-  __TEXT.__cstring: 0xcac1
-  __TEXT_EXEC.__text: 0x52c40
+  __TEXT.__cstring: 0xcadd
+  __TEXT_EXEC.__text: 0x52944
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6c8
-  __DATA.__common: 0xcc8
+  __DATA.__common: 0xca0
   __DATA.__bss: 0x69
-  __DATA_CONST.__auth_got: 0x668
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__auth_got: 0x658
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x128
   __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0x16588
+  __DATA_CONST.__const: 0x16388
   __DATA_CONST.__kalloc_var: 0x140
-  __DATA_CONST.__kalloc_type: 0x1580
+  __DATA_CONST.__kalloc_type: 0x1540
   Symbols:   0
-  Functions: 0
+  Functions: 2114
 

```

>  `com.apple.iokit.IOMIPIFamily`

```diff

-142.100.2.0.0
+160.0.0.0.0
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x1f5
-  __TEXT_EXEC.__text: 0x111c
+  __TEXT_EXEC.__text: 0x112c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 0
+  Functions: 58
 

```

>  `com.apple.iokit.IOSerialFamily`

```diff

-115.0.0.0.0
+117.0.0.0.0
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x3df
-  __TEXT_EXEC.__text: 0x7d3c
+  __TEXT_EXEC.__text: 0x7d40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x258
   __DATA.__common: 0x130

   __DATA_CONST.__kalloc_type: 0x140
   __DATA_CONST.__kalloc_var: 0x140
   Symbols:   0
-  Functions: 0
+  Functions: 159
 

```

</details>

### KDKs

- [KDK DIFF](KDK.md)

## MachO

### 🆕 NEW (315)

<details>
  <summary><i>View NEW</i></summary>

- `/Applications/AccessorySetupUI.app/AccessorySetupUI`
- `/Applications/ActivityProgressUI.app/ActivityProgressUI`
- `/Applications/AppProtectionUIHost.app/AppProtectionUIHost`
- `/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService`
- `/Applications/BarcodeScanner.app/Extensions/BarcodeScannerCaptureExtension.appex/BarcodeScannerCaptureExtension`
- `/Applications/BarcodeScanner.app/PlugIns/BarcodeScannerWidgetExtension.appex/BarcodeScannerWidgetExtension`
- `/Applications/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`
- `/Applications/Camera.app/PlugIns/LauncherControlExtension.appex/LauncherControlExtension`
- `/Applications/CompanionViewService.app/CompanionViewService`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6006.appex/Diagnostic-6006`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010`
- `/Applications/GAXApp.app/GAXApp`
- `/Applications/GAXApp.app/PlugIns/GAXAppWidgetExtension.appex/GAXAppWidgetExtension`
- `/Applications/GameOverlayUI.app/GameOverlayUI`
- `/Applications/HeadphoneProxService.app/HeadphoneProxService`
- `/Applications/LimitedAccessPromptView.app/LimitedAccessPromptView`
- `/Applications/MagnifierAngel.app/MagnifierAngel`
- `/Applications/MobilePhone.app/PlugIns/SpotlightIndexExtension.appex/SpotlightIndexExtension`
- `/Applications/MobileSlideShow.app/PlugIns/PhotosEngagementExtension.appex/PhotosEngagementExtension`
- `/Applications/MusicRecognition.app/PlugIns/MusicRecognitionControls.appex/MusicRecognitionControls`
- `/Applications/Print Center.app/PlugIns/PrintLiveActivity.iOS.appex/PrintLiveActivity.iOS`
- `/Applications/ProductKitViewer.app/ProductKitViewer`
- `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`
- `/Applications/StickerPickerService.app/StickerPickerService`
- `/Applications/SubcredentialUIService.app/Extensions/PassbookSettingsIntentExtension.appex/PassbookSettingsIntentExtension`
- `/Applications/SystemActions.app/SystemActions`
- `/Applications/TVRemoteUIService.app/PlugIns/TVRemoteWidgetExtension.appex/TVRemoteWidgetExtension`
- `/Applications/WritingToolsUIService.app/WritingToolsUIService`
- `/System/Library/AccessibilityBundles/AXAVSPluginService.axuiservice/AXAVSPluginService`
- `/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer`
- `/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer`
- `/System/Library/AccessibilityBundles/ScreenSharingAccessibilityServer.axuiservice/ScreenSharingAccessibilityServer`
- `/System/Library/Accounts/DataclassOwners/PassbookDataclassOwnerPlugin.bundle/PassbookDataclassOwnerPlugin`
- `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`
- `/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod`
- `/System/Library/ControlCenter/Bundles/PrintCenterModule.bundle/PrintCenterModule`
- `/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting`
- `/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`
- `/System/Library/CoreServices/HangHUD.app/HangHUD`
- `/System/Library/CoreServices/IntelligentLight.app/IntelligentLight`
- `/System/Library/CoreServices/ReportSystemMemory`
- `/System/Library/CoreServices/appplaceholdersyncd`
- `/System/Library/DataClassMigrators/AMFIMigrator.migrator/AMFIMigrator`
- `/System/Library/DriverExtensions/XboxGamepad.dext/XboxGamepad`
- `/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`
- `/System/Library/ExtensionKit/Extensions/AccountsUISettingsAppIntents.appex/AccountsUISettingsAppIntents`
- `/System/Library/ExtensionKit/Extensions/AirDropSettingsIntents.appex/AirDropSettingsIntents`
- `/System/Library/ExtensionKit/Extensions/AmbientSettingsAppIntentsExtension.appex/AmbientSettingsAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/AppleAccountIntents.appex/AppleAccountIntents`
- `/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension`
- `/System/Library/ExtensionKit/Extensions/AudiovisualThumbnailExtension.appex/AudiovisualThumbnailExtension`
- `/System/Library/ExtensionKit/Extensions/AutocompleteAppIntentsExtension.appex/AutocompleteAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/BiomeLibraryEventUploader.appex/BiomeLibraryEventUploader`
- `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor`
- `/System/Library/ExtensionKit/Extensions/CalendarThumbnailExtension.appex/CalendarThumbnailExtension`
- `/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/ClassKitAppIntents.appex/ClassKitAppIntents`
- `/System/Library/ExtensionKit/Extensions/ContactThumbnailExtension.appex/ContactThumbnailExtension`
- `/System/Library/ExtensionKit/Extensions/ContactsAppIntentsExtension.appex/ContactsAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/ContactsSettingsIntentsExtension.appex/ContactsSettingsIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/ControlCenterAppIntentsExtension.appex/ControlCenterAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/ControlCenterControlsExtension.appex/ControlCenterControlsExtension`
- `/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents`
- `/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/DisplayAndBrightnessSettingsExtension`
- `/System/Library/ExtensionKit/Extensions/DoNotDisturbAppIntents.appex/DoNotDisturbAppIntents`
- `/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents`
- `/System/Library/ExtensionKit/Extensions/DocumentAppShortcuts.appex/DocumentAppShortcuts`
- `/System/Library/ExtensionKit/Extensions/FaceTimeMessageStoreIntentsExtension.appex/FaceTimeMessageStoreIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents`
- `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`
- `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA`
- `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB`
- `/System/Library/ExtensionKit/Extensions/FinanceImageProcessingExtension.appex/FinanceImageProcessingExtension`
- `/System/Library/ExtensionKit/Extensions/FindMySettingsAppIntentsExtension.appex/FindMySettingsAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/FontIntents.appex/FontIntents`
- `/System/Library/ExtensionKit/Extensions/FontThumbnailExtension.appex/FontThumbnailExtension`
- `/System/Library/ExtensionKit/Extensions/GameCenterSettingsDeviceExpertExtension.appex/GameCenterSettingsDeviceExpertExtension`
- `/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents`
- `/System/Library/ExtensionKit/Extensions/HealthStandaloneIntents.appex/HealthStandaloneIntents`
- `/System/Library/ExtensionKit/Extensions/HomeWidgetIntentsExtension.appex/HomeWidgetIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/IEMetricsWorker`
- `/System/Library/ExtensionKit/Extensions/IFResponseGenerationSELFIngestor.appex/IFResponseGenerationSELFIngestor`
- `/System/Library/ExtensionKit/Extensions/IFTelemetrySELFIngestor.appex/IFTelemetrySELFIngestor`
- `/System/Library/ExtensionKit/Extensions/IFTranscriptSELFIngestor.appex/IFTranscriptSELFIngestor`
- `/System/Library/ExtensionKit/Extensions/ImageThumbnailExtension.appex/ImageThumbnailExtension`
- `/System/Library/ExtensionKit/Extensions/InferenceProviderService.appex/InferenceProviderService`
- `/System/Library/ExtensionKit/Extensions/InstalledAppsSettingsAppIntents.appex/InstalledAppsSettingsAppIntents`
- `/System/Library/ExtensionKit/Extensions/IntelligenceIntentsExtension.appex/IntelligenceIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/InternationalSettingsExtension.appex/InternationalSettingsExtension`
- `/System/Library/ExtensionKit/Extensions/KeyboardSettingsExtension.appex/KeyboardSettingsExtension`
- `/System/Library/ExtensionKit/Extensions/LegacyPoster.appex/LegacyPoster`
- `/System/Library/ExtensionKit/Extensions/LegalAndRegulatoryAppIntents.appex/LegalAndRegulatoryAppIntents`
- `/System/Library/ExtensionKit/Extensions/MCUIAppIntents.appex/MCUIAppIntents`
- `/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/MKRemoteUI`
- `/System/Library/ExtensionKit/Extensions/MailSettingsIntentsExtension.appex/MailSettingsIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/MeasureSettingsAppIntentsExtension.appex/MeasureSettingsAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/MessagesSettingsWidgetKitExtension.appex/MessagesSettingsWidgetKitExtension`
- `/System/Library/ExtensionKit/Extensions/ModelMonitoringLighthousePlugin.appex/ModelMonitoringLighthousePlugin`
- `/System/Library/ExtensionKit/Extensions/MusicUIEngagementExtension.appex/MusicUIEngagementExtension`
- `/System/Library/ExtensionKit/Extensions/NewDeviceOutreachIntents_iOS.appex/NewDeviceOutreachIntents_iOS`
- `/System/Library/ExtensionKit/Extensions/OfficeThumbnailExtension.appex/OfficeThumbnailExtension`
- `/System/Library/ExtensionKit/Extensions/PFLASLAppEmbedding.appex/PFLASLAppEmbedding`
- `/System/Library/ExtensionKit/Extensions/PFLASLArcadeRanking.appex/PFLASLArcadeRanking`
- `/System/Library/ExtensionKit/Extensions/PFLASLArcadeRetention.appex/PFLASLArcadeRetention`
- `/System/Library/ExtensionKit/Extensions/PFLASLExperimental.appex/PFLASLExperimental`
- `/System/Library/ExtensionKit/Extensions/PFLCSLAppStore.appex/PFLCSLAppStore`
- `/System/Library/ExtensionKit/Extensions/PFLCSLAppStore2.appex/PFLCSLAppStore2`
- `/System/Library/ExtensionKit/Extensions/PFLNightingaleD.appex/PFLNightingaleD`
- `/System/Library/ExtensionKit/Extensions/PassbookSettingsIntentExtension.appex/PassbookSettingsIntentExtension`
- `/System/Library/ExtensionKit/Extensions/PeopleSuggesterLighthouseBackgroundPlugin.appex/PeopleSuggesterLighthouseBackgroundPlugin`
- `/System/Library/ExtensionKit/Extensions/PeopleSuggesterMetricsLighthouse.appex/PeopleSuggesterMetricsLighthouse`
- `/System/Library/ExtensionKit/Extensions/PersonalHotspotControlExtension.appex/PersonalHotspotControlExtension`
- `/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin`
- `/System/Library/ExtensionKit/Extensions/PhotosSearchClientLighthouse.appex/PhotosSearchClientLighthouse`
- `/System/Library/ExtensionKit/Extensions/PnROnDeviceWorker.appex/PnROnDeviceWorker`
- `/System/Library/ExtensionKit/Extensions/PrivacyAppIntents.appex/PrivacyAppIntents`
- `/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService`
- `/System/Library/ExtensionKit/Extensions/QuickLookUIExtension.appex/QuickLookUIExtension`
- `/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker`
- `/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/SearchAnalyticsWorker.appex/SearchAnalyticsWorker`
- `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`
- `/System/Library/ExtensionKit/Extensions/SettingsCellularAppIntentsExtension.appex/SettingsCellularAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsIntents.appex/SoftwareUpdateSettingsIntents`
- `/System/Library/ExtensionKit/Extensions/StorageSettingsIntentsExtension.appex/StorageSettingsIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/SummarizationTool.appex/SummarizationTool`
- `/System/Library/ExtensionKit/Extensions/SystemAssistantSettingsAppIntents.appex/SystemAssistantSettingsAppIntents`
- `/System/Library/ExtensionKit/Extensions/TextThumbnailExtension.appex/TextThumbnailExtension`
- `/System/Library/ExtensionKit/Extensions/ToggleAirplaneModeExtension.appex/ToggleAirplaneModeExtension`
- `/System/Library/ExtensionKit/Extensions/ToggleCellularDataModeExtension.appex/ToggleCellularDataModeExtension`
- `/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension`
- `/System/Library/ExtensionKit/Extensions/TransparencySettingsIntents.appex/TransparencySettingsIntents`
- `/System/Library/ExtensionKit/Extensions/VPNAppIntentWidgetExtension.appex/VPNAppIntentWidgetExtension`
- `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`
- `/System/Library/ExtensionKit/Extensions/WallpaperSettingsIntents.appex/WallpaperSettingsIntents`
- `/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/WebThumbnailExtension`
- `/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension`
- `/System/Library/ExtensionKit/Extensions/WirelessModemSettingsControlsExtension.appex/WirelessModemSettingsControlsExtension`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension`
- `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`
- `/System/Library/ExtensionKit/Extensions/com.apple.fskit.hfs.appex/com.apple.fskit.hfs`
- `/System/Library/ExtensionKit/Extensions/iWorkThumbnailExtension.appex/iWorkThumbnailExtension`
- `/System/Library/Extensions/AppleH15MCD.kext/AppleH15MCD`
- `/System/Library/Extensions/AppleT6030.kext/AppleT6030`
- `/System/Library/Extensions/AppleT8122.kext/AppleT8122`
- `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`
- `/System/Library/Frameworks/Accounts.framework/Support/acdiagnose`
- `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AUHostingServiceXPC_arrow.xpc/AUHostingServiceXPC_arrow`
- `/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService`
- `/System/Library/Frameworks/ContactsUI.framework/PlugIns/OnboardingPromptExtension.appex/OnboardingPromptExtension`
- `/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService`
- `/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin`
- `/System/Library/Frameworks/CoreLocation.framework/XPCServices/GNSSLocationService.xpc/GNSSLocationService`
- `/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice`
- `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthRegulatoryCustomerDiagnosticExtension.appex/com.apple.HealthKit.HealthRegulatoryCustomerDiagnosticExtension`
- `/System/Library/Frameworks/ImageIO.framework/archive.metallib`
- `/System/Library/Frameworks/NetworkExtension.framework/PlugIns/NEUserNotificationUIExtension.appex/NEUserNotificationUIExtension`
- `/System/Library/Frameworks/PDFKit.framework/PlugIns/Illustrator_Preview.appex/Illustrator_Preview`
- `/System/Library/HIDPlugins/ServicePlugins/XboxGamepadHIDServicePlugin.plugin/XboxGamepadHIDServicePlugin`
- `/System/Library/HIDPlugins/SessionFilters/FTRemoteEventHIDSessionFilter.plugin/FTRemoteEventHIDSessionFilter`
- `/System/Library/Health/DiagnosticExtensionPlugins/HealthMedicationsDiagnosticExtensionPlugin.bundle/HealthMedicationsDiagnosticExtensionPlugin`
- `/System/Library/Health/FeedItemPlugins/HealthBalanceAppPluginBundle.healthplugin/HealthBalanceAppPluginBundle`
- `/System/Library/Health/Plugins/HealthActivityCache.bundle/HealthActivityCache`
- `/System/Library/Health/Plugins/HealthBalanceDaemonPlugin.bundle/HealthBalanceDaemonPlugin`
- `/System/Library/Health/Plugins/HealthBluetoothPeripheral.bundle/HealthBluetoothPeripheral`
- `/System/Library/Health/Plugins/HealthDaemonFeaturesPlugin.bundle/HealthDaemonFeaturesPlugin`
- `/System/Library/Messages/PlugIns/RCS.imservice/RCS`
- `/System/Library/Messages/PlugIns/SMS.imservice/SMS`
- `/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS`
- `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`
- `/System/Library/Messages/PlugIns/iMessageLite.imservice/iMessageLite`
- `/System/Library/Messages/iMessageBalloons/SendLaterProvider.bundle/SendLaterProvider`
- `/System/Library/NanoPreferenceBundles/Applications/NanoHealthBalanceBridgeSettings.bundle/NanoHealthBalanceBridgeSettings`
- `/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings`
- `/System/Library/NanoPreferenceBundles/SetupBundles/NanoSleepBridgeSetup.bundle/NanoSleepBridgeSetup`
- `/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings`
- `/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings`
- `/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings`
- `/System/Library/PreferenceBundles/LegalAndRegulatorySettings.bundle/LegalAndRegulatorySettings`
- `/System/Library/PreferenceBundles/MobileCalSettings.bundle/MobileCalSettings`
- `/System/Library/PreferenceBundles/PasswordsSettings.bundle/PasswordsSettings`
- `/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings`
- `/System/Library/PreferenceBundles/SpotlightSetting.bundle/SpotlightSetting`
- `/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings`
- `/System/Library/PreferencesSyncBundles/NHSPreferencesSync.bundle/NHSPreferencesSync`
- `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/AXTeachableMomentsNotificationsExtension.appex/AXTeachableMomentsNotificationsExtension`
- `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/XPCServices/AirPlaySenderService.xpc/AirPlaySenderService`
- `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`
- `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/XPCServices/AMSUIPaymentViewService_macCatalyst.xpc/AMSUIPaymentViewService_macCatalyst`
- `/System/Library/PrivateFrameworks/BlastDoor.framework/Resources/BlastDoorPosterArchiveBridging.bundle/BlastDoorPosterArchiveBridging`
- `/System/Library/PrivateFrameworks/CTLazuliSupport.framework/PlugIns/LazuliDiagnosticExtension.appex/LazuliDiagnosticExtension`
- `/System/Library/PrivateFrameworks/CameraUI.framework/ShutterLiquid.metallib`
- `/System/Library/PrivateFrameworks/CoreLocationTiles.framework/XPCServices/TilesService.xpc/TilesService`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothDiagnosticExtension.appex/BluetoothDiagnosticExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/MiLoDiagnostic.appex/MiLoDiagnostic`
- `/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/XPCServices/DiagnosticsSessionAvailabilityService.xpc/DiagnosticsSessionAvailabilityService`
- `/System/Library/PrivateFrameworks/DoubleAgent.framework/doubleagentd`
- `/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/FedStatsMLRPlugin`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/FedStatsMLRPluginClassB`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/FedStatsMLRPluginNonDnU`
- `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/PlugIns/GenerativeModelsDiagnostics.appex/GenerativeModelsDiagnostics`
- `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`
- `/System/Library/PrivateFrameworks/HeadGestures.framework/PlugIns/HeadGesturesDiagnosticExtension.appex/HeadGesturesDiagnosticExtension`
- `/System/Library/PrivateFrameworks/HealthBalance.framework/PlugIns/HealthBalanceDiagnosticExtension.appex/HealthBalanceDiagnosticExtension`
- `/System/Library/PrivateFrameworks/HealthPluginHost.framework/XPCServices/healthappworkd.xpc/healthappworkd`
- `/System/Library/PrivateFrameworks/IPConfiguration.framework/XPCServices/IPConfigurationHelper.xpc/IPConfigurationHelper`
- `/System/Library/PrivateFrameworks/IVRConversationAssistant.framework/XPCServices/IVRConversationAssistantXPC.xpc/IVRConversationAssistantXPC`
- `/System/Library/PrivateFrameworks/ImageGenerationUI.framework/PlugIns/com.apple.ImageGenerationUI.DiagnosticExtension.appex/com.apple.ImageGenerationUI.DiagnosticExtension`
- `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`
- `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics`
- `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`
- `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService`
- `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`
- `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU`
- `/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService`
- `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/XPCServices/ModelCatalogCompilationService.xpc/ModelCatalogCompilationService`
- `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`
- `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFStorageServer.xpc/NFStorageServer`
- `/System/Library/PrivateFrameworks/NumberAdder.framework/XPCServices/NumberAdderService.xpc/NumberAdderService`
- `/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PlugIns/PeopleSuggesterLighthousePlugin.appex/PeopleSuggesterLighthousePlugin`
- `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`
- `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`
- `/System/Library/PrivateFrameworks/Recon3D.framework/Reconstruction_Gpu_Archive.metallib`
- `/System/Library/PrivateFrameworks/RenderBox.framework/archive.metallib`
- `/System/Library/PrivateFrameworks/ReplicatorCore.framework/Support/replicatord`
- `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/SafariConfigurationSubscriber.xpc/SafariConfigurationSubscriber`
- `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/screentimediagnose`
- `/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/PlugIns/ScreenTimeDeviceActivityMonitorExtension.appex/ScreenTimeDeviceActivityMonitorExtension`
- `/System/Library/PrivateFrameworks/SensingPredictServices.framework/XPCServices/SensingPredictXPCService.xpc/SensingPredictXPCService`
- `/System/Library/PrivateFrameworks/SiriAnalytics.framework/XPCServices/SAExtensionOrchestrator.xpc/SAExtensionOrchestrator`
- `/System/Library/PrivateFrameworks/SiriUICore.framework/archive.metallib`
- `/System/Library/PrivateFrameworks/SpatialAudioServices.framework/XPCServices/SpatialAudioXPCService.xpc/SpatialAudioXPCService`
- `/System/Library/PrivateFrameworks/StocksKit.framework/XPCServices/StocksKitService.xpc/StocksKitService`
- `/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/XPCServices/TelephonyBlastDoorService.xpc/TelephonyBlastDoorService`
- `/System/Library/PrivateFrameworks/TransparencyUI.framework/PlugIns/SWTFollowUpExtension.appex/SWTFollowUpExtension`
- `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/PlugIns/UserNotificationsThumbnailProvider.appex/UserNotificationsThumbnailProvider`
- `/System/Library/PrivateFrameworks/VisualUnderstanding.framework/Plugins.bundle/Plugins`
- `/System/Library/PrivateFrameworks/WiFiVelocity.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension`
- `/System/Library/Settings/InstalledApps.settings/InstalledApps`
- `/System/Library/Siri/DM/SiriSuggestions/Owners/WritingToolsSuggestionsPlugin.bundle/WritingToolsSuggestionsPlugin`
- `/System/Library/Snippets/UIPlugins/AlarmUIPlugin.bundle/AlarmUIPlugin`
- `/System/Library/Snippets/UIPlugins/ClockUIPlugin.bundle/ClockUIPlugin`
- `/System/Library/Snippets/UIPlugins/ContactsFlowUIPlugin.bundle/ContactsFlowUIPlugin`
- `/System/Library/Snippets/UIPlugins/DeviceExpertUIPlugin.bundle/DeviceExpertUIPlugin`
- `/System/Library/Snippets/UIPlugins/HomeAutomationUIPlugin.bundle/HomeAutomationUIPlugin`
- `/System/Library/Snippets/UIPlugins/NotebookUIPlugin.bundle/NotebookUIPlugin`
- `/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin`
- `/System/Library/Snippets/UIPlugins/SiriAppLaunchUIPlugin.bundle/SiriAppLaunchUIPlugin`
- `/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/SiriKitUIPlugin`
- `/System/Library/Snippets/UIPlugins/SiriPaymentsUIPlugin.bundle/SiriPaymentsUIPlugin`
- `/System/Library/Snippets/UIPlugins/SiriSettingsUIPlugin.bundle/SiriSettingsUIPlugin`
- `/System/Library/Snippets/UIPlugins/SiriTranslationUIPlugin.bundle/SiriTranslationUIPlugin`
- `/System/Library/SystemStatus/Bundles/BackgroundActivities/ActivityProgressBackgroundUI.bundle/ActivityProgressBackgroundUI`
- `/System/Library/UserNotifications/Bundles/com.apple.safetyalerts_tones.bundle.bundle/com.apple.safetyalerts_tones.bundle`
- `/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1`
- `/private/var/staged_system_apps/Bridge.app/PlugIns/BridgeWidgetExtension.appex/BridgeWidgetExtension`
- `/private/var/staged_system_apps/Calculator.app/PlugIns/CalculatorWidget.appex/CalculatorWidget`
- `/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore`
- `/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension`
- `/private/var/staged_system_apps/GenerativePlayground.app/Extensions/GPUIExtension.appex/GPUIExtension`
- `/private/var/staged_system_apps/GenerativePlayground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`
- `/private/var/staged_system_apps/GenerativePlayground.app/GenerativePlayground`
- `/private/var/staged_system_apps/GenerativePlayground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`
- `/private/var/staged_system_apps/Health.app/PlugIns/HealthBalanceWidgetExtension.appex/HealthBalanceWidgetExtension`
- `/private/var/staged_system_apps/Health.app/PlugIns/HealthCycleTrackingWidgetExtension.appex/HealthCycleTrackingWidgetExtension`
- `/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets`
- `/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure`
- `/private/var/staged_system_apps/Magnifier.app/Extensions/MagnifierExtension.appex/MagnifierExtension`
- `/private/var/staged_system_apps/Magnifier.app/PlugIns/MagnifierWidgetExtension.appex/MagnifierWidgetExtension`
- `/private/var/staged_system_apps/MobileCal.app/Extensions/CalendarIntentsExtension.appex/CalendarIntentsExtension`
- `/private/var/staged_system_apps/MobileMail.app/Extensions/MailSettingsIntentsExtension.appex/MailSettingsIntentsExtension`
- `/private/var/staged_system_apps/Passwords.app/Passwords`
- `/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit`
- `/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews`
- `/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension`
- `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/RecordWidgetExtension.appex/RecordWidgetExtension`
- `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosSettingsWidgetExtension.appex/VoiceMemosSettingsWidgetExtension`
- `/private/var/staged_system_apps/Weather.app/Extensions/WeatherAppIntents.appex/WeatherAppIntents`
- `/usr/bin/appprotectiondiagnose`
- `/usr/bin/modelmanagerdump`
- `/usr/bin/truncate`
- `/usr/lib/libCoreFP.dylib`
- `/usr/libexec/ContinuityCaptureAgent`
- `/usr/libexec/airplayd`
- `/usr/libexec/aonsensed`
- `/usr/libexec/applekeystored`
- `/usr/libexec/appprotectiond`
- `/usr/libexec/batterytrapd`
- `/usr/libexec/cameracaptured`
- `/usr/libexec/diagnosticspushd`
- `/usr/libexec/fskit_helper`
- `/usr/libexec/fskitd`
- `/usr/libexec/hangtelemetryd`
- `/usr/libexec/inputanalyticsd`
- `/usr/libexec/jetsam_priority`
- `/usr/libexec/memoryanalyticsd`
- `/usr/libexec/merchantd`
- `/usr/libexec/milod`
- `/usr/libexec/modelmanagerd`
- `/usr/libexec/photosfaced`
- `/usr/libexec/powerexperienced`
- `/usr/libexec/rsync/rsync.openrsync`
- `/usr/libexec/safetycheckd`
- `/usr/libexec/swtransparency-sysdiagnose`
- `/usr/libexec/swtransparencyd`
- `/usr/libexec/textcontextd`
- `/usr/libexec/uarppersonalizationd`
- `/usr/libexec/visionhwserverd`

</details>

### ❌ Removed (65)

<details>
  <summary><i>View Removed</i></summary>

- `/Applications/CompanionServicesViewService.app/CompanionServicesViewService`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3985.appex/Diagnostic-3985`
- `/Applications/FieldTest.app/FieldTest`
- `/Applications/MTLReplayer.app/Frameworks/libGTLLVMShaderProfilerHelper.dylib`
- `/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidgetIntents.appex/PhotosReliveWidgetIntents`
- `/Applications/PaperBoard.app/PaperBoard`
- `/Applications/PaperBoard.app/PlugIns/LegacyPoster.appex/LegacyPoster`
- `/System/Library/Accounts/Notification/GroupKitAccountNotification.bundle/GroupKitAccountNotification`
- `/System/Library/Accounts/Notification/NDOAccountNotificationPlugin.bundle/NDOAccountNotificationPlugin`
- `/System/Library/Audio/Plug-Ins/HAL/AppleUSBAudio.driver/AppleUSBAudio`
- `/System/Library/BulletinDistributor/PingSubscribers/NanoBedtimePingSubscriber.bundle/NanoBedtimePingSubscriber`
- `/System/Library/DataClassMigrators/HealthMigrator.migrator/HealthMigrator`
- `/System/Library/DistributedEvaluation/Plugins/APODMLDESPlugin.desPlugin/APODMLDESPlugin`
- `/System/Library/DistributedEvaluation/Plugins/FidesPHSPlugin.desPlugin/FidesPHSPlugin`
- `/System/Library/DistributedEvaluation/Plugins/PhotosDESPlugin.desPlugin/PhotosDESPlugin`
- `/System/Library/ExtensionKit/Extensions/LighthouseNightingaleExtension.appex/LighthouseNightingaleExtension`
- `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredMLH.appex/PFLHRPeriodPredMLH`
- `/System/Library/Extensions/EXBrightKext.kext/EXBrightKext`
- `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/CAReportingService.xpc/CAReportingService`
- `/System/Library/Frameworks/CoreImage.framework/ccportrait_builtins_archive_bin.metallib`
- `/System/Library/Frameworks/CoreTelephony.framework/Support/DMHelper`
- `/System/Library/Frameworks/FileProvider.framework/PlugIns/FPSpotlightIndexer.appex/FPSpotlightIndexer`
- `/System/Library/Frameworks/ProximityReader.framework/merchantd`
- `/System/Library/Frameworks/QuickLookThumbnailing.framework/PlugIns/ThumbnailExtension.appex/ThumbnailExtension`
- `/System/Library/Frameworks/QuickLookThumbnailing.framework/PlugIns/ThumbnailExtensionSecure.appex/ThumbnailExtensionSecure`
- `/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.FontPicker.appex/com.apple.UIKit.FontPicker`
- `/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.TextFormatting.appex/com.apple.UIKit.TextFormatting`
- `/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib`
- `/System/Library/LocationBundles/MicroLocation.bundle/MicroLocation`
- `/System/Library/PreferenceBundles/ApplicationSettingsWrapper.bundle/ApplicationSettingsWrapper`
- `/System/Library/PreferenceBundles/ContactlessAndCredentialSettings.bundle/ContactlessAndCredentialSettings`
- `/System/Library/PrivateFrameworks/BehaviorMiner.framework/Support/mlmodelingd`
- `/System/Library/PrivateFrameworks/CipherML.framework/XPCServices/CipherMLService.xpc/CipherMLService`
- `/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/FidesPHSXPC.xpc/FidesPHSXPC`
- `/System/Library/PrivateFrameworks/FSKit.framework/fskit_helper`
- `/System/Library/PrivateFrameworks/FSKit.framework/fskitd`
- `/System/Library/PrivateFrameworks/GroupKit.framework/groupkitd`
- `/System/Library/PrivateFrameworks/HomeAI.framework/PlugIns/HomeAIDESExtension.appex/HomeAIDESExtension`
- `/System/Library/PrivateFrameworks/IAP.framework/Support/iap2d`
- `/System/Library/PrivateFrameworks/LighthouseNightingale.framework/PlugIns/LighthouseNightingalePluginBattery.appex/LighthouseNightingalePluginBattery`
- `/System/Library/PrivateFrameworks/LighthouseNightingale.framework/PlugIns/LighthouseNightingalePluginCharger.appex/LighthouseNightingalePluginCharger`
- `/System/Library/PrivateFrameworks/MarkupUI.framework/PlugIns/MarkupPhotoExtension.appex/MarkupPhotoExtension`
- `/System/Library/PrivateFrameworks/NotesUI.framework/XPCServices/com.apple.mobilenotes.LPPreviewGenerator.xpc/com.apple.mobilenotes.LPPreviewGenerator`
- `/System/Library/PrivateFrameworks/Quagga.framework/QuaggaNeuralNetworks.bundle/QuaggaNeuralNetworks`
- `/System/Library/PrivateFrameworks/RelevanceEngine.framework/relevanced`
- `/System/Library/SyncBundles/ProofingPlugin.syncBundle/ProofingPlugin`
- `/System/Library/VideoProcessors/CCPortrait.bundle/ccportrait_archive_bin.metallib`
- `/private/var/staged_system_apps/Health.app/Frameworks/HealthAppSupport.framework/HealthAppSupport`
- `/private/var/staged_system_apps/Health.app/Frameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex/HealthFollowUpExtension`
- `/private/var/staged_system_apps/Home.app/PlugIns/HomeIntentExtension.appex/HomeIntentExtension`
- `/private/var/staged_system_apps/MobileCal.app/Extensions/CalendarFocusConfigurationExtension.appex/CalendarFocusConfigurationExtension`
- `/private/var/staged_system_apps/MobileMail.app/PlugIns/MailSpotlightIndexExtension.appex/MailSpotlightIndexExtension`
- `/private/var/staged_system_apps/Podcasts.app/Frameworks/AppStoreKit.framework/AppStoreKit`
- `/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsStoreUI.framework/PodcastsStoreUI`
- `/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.PodcastsProductPageExtension.appex/com.apple.podcasts.PodcastsProductPageExtension`
- `/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDetailIntents.appex/StocksDetailIntents`
- `/usr/lib/libLogRedirect.dylib`
- `/usr/lib/libffi-trampolines.dylib`
- `/usr/lib/libglInterpose.dylib`
- `/usr/lib/libobjc-trampolines.dylib`
- `/usr/lib/libstdc++.6.0.9.dylib`
- `/usr/lib/libstdc++.6.dylib`
- `/usr/lib/libstdc++.dylib`
- `/usr/lib/xpc/support.bundle/support`
- `/usr/sbin/mediaserverd`

</details>

### ⬆️ Updated (2624)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AAUIViewService.app/AAUIViewService](MACHOS/AAUIViewService.md)
- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService.md)
- [/Applications/AXRemoteViewService.app/AXRemoteViewService](MACHOS/AXRemoteViewService.md)
- [/Applications/AXUIViewService.app/AXUIViewService](MACHOS/AXUIViewService.md)
- [/Applications/AccountAuthenticationDialog.app/AccountAuthenticationDialog](MACHOS/AccountAuthenticationDialog.md)
- [/Applications/ActivityMessagesApp.app/ActivityMessagesApp](MACHOS/ActivityMessagesApp.md)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AirPlayReceiver.app/AirPlayReceiver](MACHOS/AirPlayReceiver.md)
- [/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp](MACHOS/AirPlaySenderUIApp.md)
- [/Applications/AnimojiStickers.app/AnimojiStickers](MACHOS/AnimojiStickers.md)
- [/Applications/AnimojiStickers.app/PlugIns/AnimojiStickersExtension.appex/AnimojiStickersExtension](MACHOS/AnimojiStickersExtension.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppSSOUIService.app/AppSSOUIService](MACHOS/AppSSOUIService.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AskPermissionUI.app/AskPermissionUI](MACHOS/AskPermissionUI.md)
- [/Applications/AskToMessagesHost.app/AskToMessagesHost](MACHOS/AskToMessagesHost.md)
- [/Applications/AskToMessagesHost.app/Extensions/AskToExtension.appex/AskToExtension](MACHOS/AskToExtension.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AuthKitUIService.app/AuthKitUIService](MACHOS/AuthKitUIService.md)
- [/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI](MACHOS/AuthenticationServicesUI.md)
- [/Applications/AuthenticationServicesUI.app/PlugIns/AccountAuthenticationModificationExtensionHelper.appex/AccountAuthenticationModificationExtensionHelper](MACHOS/AccountAuthenticationModificationExtensionHelper.md)
- [/Applications/AutoSettings.app/AutoSettings](MACHOS/AutoSettings.md)
- [/Applications/BacklinkIndicator.app/BacklinkIndicator](MACHOS/BacklinkIndicator.md)
- [/Applications/BarcodeScanner.app/BarcodeScanner](MACHOS/BarcodeScanner.md)
- [/Applications/Batteries.app/Batteries](MACHOS/Batteries.md)
- [/Applications/Batteries.app/PlugIns/BatteriesAvocadoWidgetExtension.appex/BatteriesAvocadoWidgetExtension](MACHOS/BatteriesAvocadoWidgetExtension.md)
- [/Applications/Batteries.app/PlugIns/BatteriesWidgetExtension.appex/BatteriesWidgetExtension](MACHOS/BatteriesWidgetExtension.md)
- [/Applications/Batteries.app/PlugIns/BatteriesWidgetIntentsExtension.appex/BatteriesWidgetIntentsExtension](MACHOS/BatteriesWidgetIntentsExtension.md)
- [/Applications/BusinessChatViewService.app/BusinessChatViewService](MACHOS/BusinessChatViewService.md)
- [/Applications/BusinessExtensionsWrapper.app/BusinessExtensionsWrapper](MACHOS/BusinessExtensionsWrapper.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CTCarrierSpaceAuth.app/CTCarrierSpaceAuth](MACHOS/CTCarrierSpaceAuth.md)
- [/Applications/CTKUIService.app/CTKUIService](MACHOS/CTKUIService.md)
- [/Applications/CTNotifyUIService.app/CTNotifyUIService](MACHOS/CTNotifyUIService.md)
- [/Applications/Camera.app/Camera](MACHOS/Camera.md)
- [/Applications/Camera.app/PlugIns/CameraMessagesApp.appex/CameraMessagesApp](MACHOS/CameraMessagesApp.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/CarPlaySetup.app/CarPlaySetup](MACHOS/CarPlaySetup.md)
- [/Applications/CarPlaySplashScreen.app/CarPlaySplashScreen](MACHOS/CarPlaySplashScreen.md)
- [/Applications/CarPlayWallpaper.app/CarPlayWallpaper](MACHOS/CarPlayWallpaper.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/CheckerBoardRemoteSetup.app/CheckerBoardRemoteSetup](MACHOS/CheckerBoardRemoteSetup.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/ClarityPhotos.app/ClarityPhotos](MACHOS/ClarityPhotos.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClipViewService.app/ClipViewService](MACHOS/ClipViewService.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CompassCalibrationViewService.app/CompassCalibrationViewService](MACHOS/CompassCalibrationViewService.md)
- [/Applications/ContactPhotoCarouselRemoteAlert.app/ContactPhotoCarouselRemoteAlert](MACHOS/ContactPhotoCarouselRemoteAlert.md)
- [/Applications/ContinuityCaptureShieldUI.app/ContinuityCaptureShieldUI](MACHOS/ContinuityCaptureShieldUI.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Coverage Details.app/Coverage Details](MACHOS/Coverage_Details.md)
- [/Applications/CredentialSharingUIViewService.app/CredentialSharingUIViewService](MACHOS/CredentialSharingUIViewService.md)
- [/Applications/CredentialSharingUIViewService.app/PlugIns/ShareableCredentialsMessagesExtension.appex/ShareableCredentialsMessagesExtension](MACHOS/ShareableCredentialsMessagesExtension.md)
- [/Applications/DDActionsService.app/DDActionsService](MACHOS/DDActionsService.md)
- [/Applications/DKPairingUIService.app/DKPairingUIService](MACHOS/DKPairingUIService.md)
- [/Applications/DemoApp.app/DemoApp](MACHOS/DemoApp.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/Diagnostics.app/PlugIns/com.apple.Diagnostics.diagnosticextension.appex/com.apple.Diagnostics.diagnosticextension](MACHOS/com.apple.Diagnostics.diagnosticextension.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/DiagnosticsService](MACHOS/DiagnosticsService.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-0001.appex/Diagnostic-0001](MACHOS/Diagnostic-0001.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3732.appex/Diagnostic-3732](MACHOS/Diagnostic-3732.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3734.appex/Diagnostic-3734](MACHOS/Diagnostic-3734.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3738.appex/Diagnostic-3738](MACHOS/Diagnostic-3738.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3741.appex/Diagnostic-3741](MACHOS/Diagnostic-3741.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3743.appex/Diagnostic-3743](MACHOS/Diagnostic-3743.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3744.appex/Diagnostic-3744](MACHOS/Diagnostic-3744.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3745.appex/Diagnostic-3745](MACHOS/Diagnostic-3745.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3903.appex/Diagnostic-3903](MACHOS/Diagnostic-3903.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3904.appex/Diagnostic-3904](MACHOS/Diagnostic-3904.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3905.appex/Diagnostic-3905](MACHOS/Diagnostic-3905.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3906.appex/Diagnostic-3906](MACHOS/Diagnostic-3906.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3907.appex/Diagnostic-3907](MACHOS/Diagnostic-3907.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3909.appex/Diagnostic-3909](MACHOS/Diagnostic-3909.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939](MACHOS/Diagnostic-3939.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3942.appex/Diagnostic-3942](MACHOS/Diagnostic-3942.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4002.appex/Diagnostic-4002](MACHOS/Diagnostic-4002.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4003.appex/Diagnostic-4003](MACHOS/Diagnostic-4003.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4004.appex/Diagnostic-4004](MACHOS/Diagnostic-4004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4005.appex/Diagnostic-4005](MACHOS/Diagnostic-4005.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4006.appex/Diagnostic-4006](MACHOS/Diagnostic-4006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4007.appex/Diagnostic-4007](MACHOS/Diagnostic-4007.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4008.appex/Diagnostic-4008](MACHOS/Diagnostic-4008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009-iOS-D83-D84.appex/Diagnostic-4009-iOS-D83-D84](MACHOS/Diagnostic-4009-iOS-D83-D84.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153](MACHOS/Diagnostic-4153.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4154.appex/Diagnostic-4154](MACHOS/Diagnostic-4154.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4180.appex/Diagnostic-4180](MACHOS/Diagnostic-4180.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4181.appex/Diagnostic-4181](MACHOS/Diagnostic-4181.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4182.appex/Diagnostic-4182](MACHOS/Diagnostic-4182.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4183.appex/Diagnostic-4183](MACHOS/Diagnostic-4183.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4184.appex/Diagnostic-4184](MACHOS/Diagnostic-4184.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4276.appex/Diagnostic-4276](MACHOS/Diagnostic-4276.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4351.appex/Diagnostic-4351](MACHOS/Diagnostic-4351.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4359.appex/Diagnostic-4359](MACHOS/Diagnostic-4359.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4492-sshb.appex/Diagnostic-4492-sshb](MACHOS/Diagnostic-4492-sshb.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4579.appex/Diagnostic-4579](MACHOS/Diagnostic-4579.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4615.appex/Diagnostic-4615](MACHOS/Diagnostic-4615.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6000.appex/Diagnostic-6000](MACHOS/Diagnostic-6000.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6001.appex/Diagnostic-6001](MACHOS/Diagnostic-6001.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002](MACHOS/Diagnostic-6002.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8035.appex/Diagnostic-8035](MACHOS/Diagnostic-8035.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8068.appex/Diagnostic-8068](MACHOS/Diagnostic-8068.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079](MACHOS/Diagnostic-8079.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8134.appex/Diagnostic-8134](MACHOS/Diagnostic-8134.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187](MACHOS/Diagnostic-8187.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201](MACHOS/Diagnostic-8201.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8209.appex/Diagnostic-8209](MACHOS/Diagnostic-8209.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8217.appex/Diagnostic-8217](MACHOS/Diagnostic-8217.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8238.appex/Diagnostic-8238](MACHOS/Diagnostic-8238.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246](MACHOS/Diagnostic-8246.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253](MACHOS/Diagnostic-8253.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8259.appex/Diagnostic-8259](MACHOS/Diagnostic-8259.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262](MACHOS/Diagnostic-8262.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264](MACHOS/Diagnostic-8264.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276](MACHOS/Diagnostic-8276.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288](MACHOS/Diagnostic-8288.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8290-EFD.appex/Diagnostic-8290-EFD](MACHOS/Diagnostic-8290-EFD.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8357.appex/Diagnostic-8357](MACHOS/Diagnostic-8357.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8374.appex/Diagnostic-8374](MACHOS/Diagnostic-8374.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8381.appex/Diagnostic-8381](MACHOS/Diagnostic-8381.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389](MACHOS/Diagnostic-8389.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Diagnostic-8441](MACHOS/Diagnostic-8441.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Frameworks/DiagnosticsSupport.framework/DiagnosticsSupport](MACHOS/DiagnosticsSupport.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84](MACHOS/SystemReport-iOS-D83-D84.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/ExposureNotificationRemoteViewService.app/ExposureNotificationRemoteViewService](MACHOS/ExposureNotificationRemoteViewService.md)
- [/Applications/EyeReliefUI.app/EyeReliefUI](MACHOS/EyeReliefUI.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/FaceTimeLinkTrampoline.app/FaceTimeLinkTrampoline](MACHOS/FaceTimeLinkTrampoline.md)
- [/Applications/Family.app/Family](MACHOS/Family.md)
- [/Applications/Family.app/PlugIns/FAFollowupExtension.appex/FAFollowupExtension](MACHOS/FAFollowupExtension.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FamilyControlsAuthenticationUI.app/FamilyControlsAuthenticationUI](MACHOS/FamilyControlsAuthenticationUI.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FeedbackRemoteView.app/FeedbackRemoteView](MACHOS/FeedbackRemoteView.md)
- [/Applications/FinanceStub.app/FinanceStub](MACHOS/FinanceStub.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyExtensionContainer.app/FindMyExtensionContainer](MACHOS/FindMyExtensionContainer.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontInstallViewService.app/FontInstallViewService](MACHOS/FontInstallViewService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/FunCameraEmojiStickers.app/FunCameraEmojiStickers](MACHOS/FunCameraEmojiStickers.md)
- [/Applications/FunCameraEmojiStickers.app/PlugIns/FunCameraEmojiStickersExtension.appex/FunCameraEmojiStickersExtension](MACHOS/FunCameraEmojiStickersExtension.md)
- [/Applications/FunCameraShapes.app/FunCameraShapes](MACHOS/FunCameraShapes.md)
- [/Applications/FunCameraShapes.app/PlugIns/FunCameraShapesExtension.appex/FunCameraShapesExtension](MACHOS/FunCameraShapesExtension.md)
- [/Applications/FunCameraText.app/FunCameraText](MACHOS/FunCameraText.md)
- [/Applications/FunCameraText.app/PlugIns/FunCameraTextExtension.appex/FunCameraTextExtension](MACHOS/FunCameraTextExtension.md)
- [/Applications/GameCenterRemoteAlert.app/GameCenterRemoteAlert](MACHOS/GameCenterRemoteAlert.md)
- [/Applications/GameCenterUIService.app/GameCenterUIService](MACHOS/GameCenterUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/GameCenterWidgets](MACHOS/GameCenterWidgets.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HashtagImages.app/HashtagImages](MACHOS/HashtagImages.md)
- [/Applications/HashtagImages.app/PlugIns/HashtagImagesExtension.appex/HashtagImagesExtension](MACHOS/HashtagImagesExtension.md)
- [/Applications/HealthENBuddy.app/HealthENBuddy](MACHOS/HealthENBuddy.md)
- [/Applications/HealthENLauncher.app/HealthENLauncher](MACHOS/HealthENLauncher.md)
- [/Applications/HealthPrivacyService.app/HealthPrivacyService](MACHOS/HealthPrivacyService.md)
- [/Applications/HearingApp.app/HearingApp](MACHOS/HearingApp.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/HomeControlService.app/HomeControlService](MACHOS/HomeControlService.md)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/FaceTimeShareExtension.appex/FaceTimeShareExtension](MACHOS/FaceTimeShareExtension.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/InCallService.app/PlugIns/RemotePeoplePicker.appex/RemotePeoplePicker](MACHOS/RemotePeoplePicker.md)
- [/Applications/InputUI.app/InputUI](MACHOS/InputUI.md)
- [/Applications/Jellyfish.app/Jellyfish](MACHOS/Jellyfish.md)
- [/Applications/Jellyfish.app/PlugIns/Animoji.appex/Animoji](MACHOS/Animoji.md)
- [/Applications/MBHelperApp.app/MBHelperApp](MACHOS/MBHelperApp.md)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController.md)
- [/Applications/MTLReplayer.app/MTLReplayer](MACHOS/MTLReplayer.md)
- [/Applications/MailCompositionService.app/MailCompositionService](MACHOS/MailCompositionService.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MediaRemoteUIService.app/MediaRemoteUIService](MACHOS/MediaRemoteUIService.md)
- [/Applications/MessagesViewService.app/MessagesViewService](MACHOS/MessagesViewService.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MobileReplayer.app/MobileReplayer](MACHOS/MobileReplayer.md)
- [/Applications/MobileReplayer.app/PlugIns/EAGLReplayControllerSupport.mrplugin/EAGLReplayControllerSupport](MACHOS/EAGLReplayControllerSupport.md)
- [/Applications/MobileSMS.app/Extensions/MessagesActionExtension.appex/MessagesActionExtension](MACHOS/MessagesActionExtension.md)
- [/Applications/MobileSMS.app/MobileSMS](MACHOS/MobileSMS.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension](MACHOS/MessagesAssistantExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesAssistantUIExtension.appex/MessagesAssistantUIExtension](MACHOS/MessagesAssistantUIExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension](MACHOS/MessagesNotificationExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension](MACHOS/MessagesPluginNotificationExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension](MACHOS/MessagesTranscriptExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MobileSMSSpotlightImporter.appex/MobileSMSSpotlightImporter](MACHOS/MobileSMSSpotlightImporter.md)
- [/Applications/MobileSafari.app/Extensions/SafariLinkExtension.appex/SafariLinkExtension](MACHOS/SafariLinkExtension.md)
- [/Applications/MobileSafari.app/MobileSafari](MACHOS/MobileSafari.md)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension](MACHOS/com.apple.mobilesafari.SafariDiagnosticExtension.md)
- [/Applications/MobileSafari.app/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker](MACHOS/com.apple.Safari.SandboxBroker.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotoPicker.appex/PhotoPicker](MACHOS/PhotoPicker.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosDestructiveChangeConfirmation.appex/PhotosDestructiveChangeConfirmation](MACHOS/PhotosDestructiveChangeConfirmation.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosFileProvider.appex/PhotosFileProvider](MACHOS/PhotosFileProvider.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMemoriesNotificationUpdates.appex/PhotosMemoriesNotificationUpdates](MACHOS/PhotosMemoriesNotificationUpdates.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMessagesApp.appex/PhotosMessagesApp](MACHOS/PhotosMessagesApp.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates](MACHOS/PhotosNotificationsUpdates.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosPicker.appex/PhotosPicker](MACHOS/PhotosPicker.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosTCCNotificationExtension.appex/PhotosTCCNotificationExtension](MACHOS/PhotosTCCNotificationExtension.md)
- [/Applications/MobileSlideShow.app/PlugIns/com.apple.social.StreamShareService.appex/com.apple.social.StreamShareService](MACHOS/com.apple.social.StreamShareService.md)
- [/Applications/MomentsUIService.app/Frameworks/MomentsUIServiceCore.framework/MomentsUIServiceCore](MACHOS/MomentsUIServiceCore.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/MusicUIService.app/MusicUIService](MACHOS/MusicUIService.md)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService.md)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PDUIApp.app/PDUIApp](MACHOS/PDUIApp.md)
- [/Applications/PassbookSecureUIService.app/PassbookSecureUIService](MACHOS/PassbookSecureUIService.md)
- [/Applications/PassbookUISceneService.app/PassbookUISceneService](MACHOS/PassbookUISceneService.md)
- [/Applications/PassbookUIService.app/PassbookUIService](MACHOS/PassbookUIService.md)
- [/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension](MACHOS/PeerPaymentMessagesExtension.md)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService.md)
- [/Applications/PeopleMessageService.app/PeopleMessageService](MACHOS/PeopleMessageService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/PeopleViewService.app/PlugIns/SelectPerson_iOS.appex/SelectPerson_iOS](MACHOS/SelectPerson_iOS.md)
- [/Applications/PhotosUIService.app/PhotosUIService](MACHOS/PhotosUIService.md)
- [/Applications/PosterBoard.app/PlugIns/WallpaperDiagnosticExtension.appex/WallpaperDiagnosticExtension](MACHOS/WallpaperDiagnosticExtension.md)
- [/Applications/PosterBoard.app/PosterBoard](MACHOS/PosterBoard.md)
- [/Applications/PreBoard.app/PreBoard](MACHOS/PreBoard.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/Print Center.app/Print Center](MACHOS/Print_Center.md)
- [/Applications/ProximityReaderSceneUI.app/ProximityReaderSceneUI](MACHOS/ProximityReaderSceneUI.md)
- [/Applications/ProximityReaderUIService.app/ProximityReaderUIService](MACHOS/ProximityReaderUIService.md)
- [/Applications/RecoverDeviceUI.app/RecoverDeviceUI](MACHOS/RecoverDeviceUI.md)
- [/Applications/RemotePaymentPassActionsService.app/PlugIns/RemotePaymentPassActionsMessagesExtension.appex/RemotePaymentPassActionsMessagesExtension](MACHOS/RemotePaymentPassActionsMessagesExtension.md)
- [/Applications/RemotePaymentPassActionsService.app/RemotePaymentPassActionsService](MACHOS/RemotePaymentPassActionsService.md)
- [/Applications/RemoteiCloudQuotaUI.app/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI.md)
- [/Applications/ReplayKitAngel.app/ReplayKitAngel](MACHOS/ReplayKitAngel.md)
- [/Applications/SIMSetupUIService.app/SIMSetupUIService](MACHOS/SIMSetupUIService.md)
- [/Applications/SLYahooAuth.app/PlugIns/SLYahooAuthService.appex/SLYahooAuthService](MACHOS/SLYahooAuthService.md)
- [/Applications/SLYahooAuth.app/SLYahooAuth](MACHOS/SLYahooAuth.md)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter.md)
- [/Applications/SMS Filter.app/SMS Filter](MACHOS/SMS_Filter.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/SafariViewService.app/SafariViewService](MACHOS/SafariViewService.md)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/Screen Time.app/Screen Time](MACHOS/Screen_Time.md)
- [/Applications/ScreenSharingViewService.app/ScreenSharingViewService](MACHOS/ScreenSharingViewService.md)
- [/Applications/ScreenTimeUnlock.app/ScreenTimeUnlock](MACHOS/ScreenTimeUnlock.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharedWebCredentialViewService.app/SharedWebCredentialViewService](MACHOS/SharedWebCredentialViewService.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI.md)
- [/Applications/ShortcutsViewService.app/ShortcutsViewService](MACHOS/ShortcutsViewService.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityCamera.appex/ContinuityCamera](MACHOS/ContinuityCamera.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityCapture.appex/ContinuityCapture](MACHOS/ContinuityCapture.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityMarkup.appex/ContinuityMarkup](MACHOS/ContinuityMarkup.md)
- [/Applications/Sidecar.app/PlugIns/ContinuitySignature.appex/ContinuitySignature](MACHOS/ContinuitySignature.md)
- [/Applications/Sidecar.app/PlugIns/ContinuitySketch.appex/ContinuitySketch](MACHOS/ContinuitySketch.md)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SleepLockScreen.app/SleepLockScreen](MACHOS/SleepLockScreen.md)
- [/Applications/SleepWidgetContainer.app/PlugIns/SleepWidgetExtension.appex/SleepWidgetExtension](MACHOS/SleepWidgetExtension.md)
- [/Applications/SleepWidgetContainer.app/SleepWidgetContainer](MACHOS/SleepWidgetContainer.md)
- [/Applications/SoftwareUpdateUIService.app/PlugIns/SUSUIVerifyingAlertCFUserNotificationUIExtension.appex/SUSUIVerifyingAlertCFUserNotificationUIExtension](MACHOS/SUSUIVerifyingAlertCFUserNotificationUIExtension.md)
- [/Applications/SoftwareUpdateUIService.app/PlugIns/SUSUInstallAlertCFUserNotificationUIExtension.appex/SUSUInstallAlertCFUserNotificationUIExtension](MACHOS/SUSUInstallAlertCFUserNotificationUIExtension.md)
- [/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService](MACHOS/SoftwareUpdateUIService.md)
- [/Applications/Spotlight.app/Spotlight](MACHOS/Spotlight.md)
- [/Applications/SpringBoardEducation.app/SpringBoardEducation](MACHOS/SpringBoardEducation.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StickersUltra.app/StickersUltra](MACHOS/StickersUltra.md)
- [/Applications/StoreDemoViewService.app/StoreDemoViewService](MACHOS/StoreDemoViewService.md)
- [/Applications/StoreKitUIService.app/StoreKitUIService](MACHOS/StoreKitUIService.md)
- [/Applications/SubcredentialUIService.app/PlugIns/SubcredentialInvitationMessagesExtension.appex/SubcredentialInvitationMessagesExtension](MACHOS/SubcredentialInvitationMessagesExtension.md)
- [/Applications/SubcredentialUIService.app/SubcredentialUIService](MACHOS/SubcredentialUIService.md)
- [/Applications/SystemPaperViewService.app/SystemPaperViewService](MACHOS/SystemPaperViewService.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVAccessViewService.app/TVAccessViewService](MACHOS/TVAccessViewService.md)
- [/Applications/TVRemoteUIService.app/PlugIns/TVRemoteIntentExtension.appex/TVRemoteIntentExtension](MACHOS/TVRemoteIntentExtension.md)
- [/Applications/TVRemoteUIService.app/TVRemoteUIService](MACHOS/TVRemoteUIService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/TrustMe.app/TrustMe](MACHOS/TrustMe.md)
- [/Applications/VideoSubscriberAccountViewService.app/VideoSubscriberAccountViewService](MACHOS/VideoSubscriberAccountViewService.md)
- [/Applications/Web.app/Web](MACHOS/Web.md)
- [/Applications/WebContentAnalysisUI.app/WebContentAnalysisUI](MACHOS/WebContentAnalysisUI.md)
- [/Applications/WebSheet.app/WebSheet](MACHOS/WebSheet.md)
- [/Applications/WidgetRenderer_CarPlay.app/WidgetRenderer_CarPlay](MACHOS/WidgetRenderer_CarPlay.md)
- [/Applications/WidgetRenderer_Default.app/WidgetRenderer_Default](MACHOS/WidgetRenderer_Default.md)
- [/Applications/WorkoutRemoteViewService.app/WorkoutRemoteViewService](MACHOS/WorkoutRemoteViewService.md)
- [/Applications/iCloud+.app/iCloud+](MACHOS/iCloud+.md)
- [/Applications/iCloud.app/iCloud](MACHOS/iCloud.md)
- [/Applications/iMessageAppsViewService.app/iMessageAppsViewService](MACHOS/iMessageAppsViewService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/usr/lib/libSystem_debug.dylib](MACHOS/libSystem_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libdispatch_debug.dylib](MACHOS/libdispatch_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libdispatch_profile.dylib](MACHOS/libdispatch_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_blocks_debug.dylib](MACHOS/libsystem_blocks_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_blocks_profile.dylib](MACHOS/libsystem_blocks_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib](MACHOS/libsystem_c_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_platform_debug.dylib](MACHOS/libsystem_platform_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_pthread_debug.dylib](MACHOS/libsystem_pthread_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib](MACHOS/libsystem_trace_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXAggregateStatisticsServer.axuiservice/AXAggregateStatisticsServer](MACHOS/AXAggregateStatisticsServer.md)
- [/System/Library/AccessibilityBundles/AXAssetAndDataServer.axuiservice/AXAssetAndDataServer](MACHOS/AXAssetAndDataServer.md)
- [/System/Library/AccessibilityBundles/AXAuditAXUIService.axuiservice/AXAuditAXUIService](MACHOS/AXAuditAXUIService.md)
- [/System/Library/AccessibilityBundles/AXBannerUIServer.axuiservice/AXBannerUIServer](MACHOS/AXBannerUIServer.md)
- [/System/Library/AccessibilityBundles/AXBuddyBundle.bundle/AXBuddyBundle](MACHOS/AXBuddyBundle.md)
- [/System/Library/AccessibilityBundles/AXContainerManagerServer.axuiservice/AXContainerManagerServer](MACHOS/AXContainerManagerServer.md)
- [/System/Library/AccessibilityBundles/AXElementInteractionUIServer.axuiservice/AXElementInteractionUIServer](MACHOS/AXElementInteractionUIServer.md)
- [/System/Library/AccessibilityBundles/AXIDSServer.axuiservice/AXIDSServer](MACHOS/AXIDSServer.md)
- [/System/Library/AccessibilityBundles/AXLocalizationCaptionServer.axuiservice/AXLocalizationCaptionServer](MACHOS/AXLocalizationCaptionServer.md)
- [/System/Library/AccessibilityBundles/AXUltronPluginService.axuiservice/AXUltronPluginService](MACHOS/AXUltronPluginService.md)
- [/System/Library/AccessibilityBundles/AXWatchRemoteScreenUIServer.axuiservice/AXWatchRemoteScreenUIServer](MACHOS/AXWatchRemoteScreenUIServer.md)
- [/System/Library/AccessibilityBundles/ActivityAchievementsUI.axbundle/ActivityAchievementsUI](MACHOS/ActivityAchievementsUI.md)
- [/System/Library/AccessibilityBundles/ActivityBridgeSetup.axbundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/AccessibilityBundles/ActivityRingsUI.axbundle/ActivityRingsUI](MACHOS/ActivityRingsUI.md)
- [/System/Library/AccessibilityBundles/ActivitySharing.axbundle/ActivitySharing](MACHOS/ActivitySharing.md)
- [/System/Library/AccessibilityBundles/ActivitySharingUI.axbundle/ActivitySharingUI](MACHOS/ActivitySharingUI.md)
- [/System/Library/AccessibilityBundles/AssistiveTouch.axuiservice/AssistiveTouch](MACHOS/AssistiveTouch.md)
- [/System/Library/AccessibilityBundles/BackTapUIServer.axuiservice/BackTapUIServer](MACHOS/BackTapUIServer.md)
- [/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer](MACHOS/ClarityUIServer.md)
- [/System/Library/AccessibilityBundles/ClockAngel.axbundle/ClockAngel](MACHOS/ClockAngel.md)
- [/System/Library/AccessibilityBundles/DisplayFilterUIServer.axuiservice/DisplayFilterUIServer](MACHOS/DisplayFilterUIServer.md)
- [/System/Library/AccessibilityBundles/FitnessApp.axbundle/FitnessApp](MACHOS/FitnessApp.md)
- [/System/Library/AccessibilityBundles/FitnessUI.axbundle/FitnessUI](MACHOS/FitnessUI.md)
- [/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer](MACHOS/GAXBackboardServer.md)
- [/System/Library/AccessibilityBundles/GAXClient.bundle/GAXClient](MACHOS/GAXClient.md)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer.md)
- [/System/Library/AccessibilityBundles/GuidedAccess.axuiservice/GuidedAccess](MACHOS/GuidedAccess.md)
- [/System/Library/AccessibilityBundles/HoverTextUIServer.axuiservice/HoverTextUIServer](MACHOS/HoverTextUIServer.md)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/NTKCustomization.axbundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/AccessibilityBundles/NTKUltraCubeFaceBundleCompanion.axbundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/AccessibilityBundles/NanoMailBridgeSettings.axbundle/NanoMailBridgeSettings](MACHOS/NanoMailBridgeSettings.md)
- [/System/Library/AccessibilityBundles/NanoMediaBridgeUI.axbundle/NanoMediaBridgeUI](MACHOS/NanoMediaBridgeUI.md)
- [/System/Library/AccessibilityBundles/NanoPeopleBridgeSettings.axbundle/NanoPeopleBridgeSettings](MACHOS/NanoPeopleBridgeSettings.md)
- [/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion](MACHOS/NanoTimeKitCompanion.md)
- [/System/Library/AccessibilityBundles/PingMyWatchControlCenterUI.axbundle/PingMyWatchControlCenterUI](MACHOS/PingMyWatchControlCenterUI.md)
- [/System/Library/AccessibilityBundles/SchoolTimeSettingsUI.axbundle/SchoolTimeSettingsUI](MACHOS/SchoolTimeSettingsUI.md)
- [/System/Library/AccessibilityBundles/ScreenSharing.axuiservice/ScreenSharing](MACHOS/ScreenSharing.md)
- [/System/Library/AccessibilityBundles/SiriSetup.axbundle/SiriSetup](MACHOS/SiriSetup.md)
- [/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer](MACHOS/SpeakServer.md)
- [/System/Library/AccessibilityBundles/SpeakThis.axuiservice/SpeakThis](MACHOS/SpeakThis.md)
- [/System/Library/AccessibilityBundles/StickyKeys.axuiservice/StickyKeys](MACHOS/StickyKeys.md)
- [/System/Library/AccessibilityBundles/TouchAccommodations.axuiservice/TouchAccommodations](MACHOS/TouchAccommodations.md)
- [/System/Library/AccessibilityBundles/VisualAlerts.bundle/VisualAlerts](MACHOS/VisualAlerts.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/AccessibilityBundles/WidgetRenderer.axbundle/WidgetRenderer](MACHOS/WidgetRenderer.md)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow.md)
- [/System/Library/AccessibilityBundles/activity-widget.axbundle/activity-widget](MACHOS/activity-widget.md)
- [/System/Library/AccessibilityBundles/com.apple.NanoTimeKit.CreateWatchFace.axbundle/com.apple.NanoTimeKit.CreateWatchFace](MACHOS/com.apple.NanoTimeKit.CreateWatchFace.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/FMFAppleIDLoginPlugin.bundle/FMFAppleIDLoginPlugin](MACHOS/FMFAppleIDLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/FaceTimeAppleIDLoginPlugin.bundle/FaceTimeAppleIDLoginPlugin](MACHOS/FaceTimeAppleIDLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/GameCenterAppleIDLoginPlugin.bundle/GameCenterAppleIDLoginPlugin](MACHOS/GameCenterAppleIDLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/ISLoginPlugin.bundle/ISLoginPlugin](MACHOS/ISLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/MadridAppleIDLoginPlugin.bundle/MadridAppleIDLoginPlugin](MACHOS/MadridAppleIDLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/iCloudAppleIDLoginPlugin.bundle/iCloudAppleIDLoginPlugin](MACHOS/iCloudAppleIDLoginPlugin.md)
- [/System/Library/Accounts/Authentication/AAGKAuthenticationPlugin.bundle/AAGKAuthenticationPlugin](MACHOS/AAGKAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/AAIDSAuthenticationPlugin.bundle/AAIDSAuthenticationPlugin](MACHOS/AAIDSAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/AppleAccountAuthenticationDelegate.bundle/AppleAccountAuthenticationDelegate](MACHOS/AppleAccountAuthenticationDelegate.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/GameCenterAppleIDAuthenticationDelegate.bundle/GameCenterAppleIDAuthenticationDelegate](MACHOS/GameCenterAppleIDAuthenticationDelegate.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/IDSAuthenticationDelegatePlugin.bundle/IDSAuthenticationDelegatePlugin](MACHOS/IDSAuthenticationDelegatePlugin.md)
- [/System/Library/Accounts/DataclassOwners/Bookmarks.bundle/Bookmarks](MACHOS/Bookmarks.md)
- [/System/Library/Accounts/DataclassOwners/Calendar.bundle/Calendar](MACHOS/Calendar.md)
- [/System/Library/Accounts/DataclassOwners/CloudDocsDataclassOwnerPlugin.bundle/CloudDocsDataclassOwnerPlugin](MACHOS/CloudDocsDataclassOwnerPlugin.md)
- [/System/Library/Accounts/DataclassOwners/ContactsDataclassOwner.bundle/ContactsDataclassOwner](MACHOS/ContactsDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/HealthDataclassOwnerPlugin.bundle/HealthDataclassOwnerPlugin](MACHOS/HealthDataclassOwnerPlugin.md)
- [/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner](MACHOS/JournalDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/KeychainDataclassOwner.bundle/KeychainDataclassOwner](MACHOS/KeychainDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/MessagesDataclassOwner.bundle/MessagesDataclassOwner](MACHOS/MessagesDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/News.bundle/News](MACHOS/News.md)
- [/System/Library/Accounts/DataclassOwners/Notes.bundle/Notes](MACHOS/Notes.md)
- [/System/Library/Accounts/DataclassOwners/RemindersDataclassOwnerPlugin.bundle/RemindersDataclassOwnerPlugin](MACHOS/RemindersDataclassOwnerPlugin.md)
- [/System/Library/Accounts/DataclassOwners/SiriDataclassOwner.bundle/SiriDataclassOwner](MACHOS/SiriDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/StocksDataclassOwner.bundle/StocksDataclassOwner](MACHOS/StocksDataclassOwner.md)
- [/System/Library/Accounts/Notification/ASDAccountNotificationPlugin.bundle/ASDAccountNotificationPlugin](MACHOS/ASDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/AccountNotificationPlugin](MACHOS/AccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AccountSuggestionNotificationPlugin.bundle/AccountSuggestionNotificationPlugin](MACHOS/AccountSuggestionNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CloudBookmarksAccountsNotifier.bundle/CloudBookmarksAccountsNotifier](MACHOS/CloudBookmarksAccountsNotifier.md)
- [/System/Library/Accounts/Notification/CloudDocsAccountNotificationPlugin.bundle/CloudDocsAccountNotificationPlugin](MACHOS/CloudDocsAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreAccessoriesAccountNotificationPlugin.bundle/CoreAccessoriesAccountNotificationPlugin](MACHOS/CoreAccessoriesAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/DeviceManagementClientAccountNotificationPlugin.bundle/DeviceManagementClientAccountNotificationPlugin](MACHOS/DeviceManagementClientAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/MBPrebuddyAccountNotificationPlugin.bundle/MBPrebuddyAccountNotificationPlugin](MACHOS/MBPrebuddyAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/MCAccountNotificationPlugin.bundle/MCAccountNotificationPlugin](MACHOS/MCAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NanoMailAccountNotificationPlugin.bundle/NanoMailAccountNotificationPlugin](MACHOS/NanoMailAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NanoPassbookAccountNotificationPlugin.bundle/NanoPassbookAccountNotificationPlugin](MACHOS/NanoPassbookAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/RemoteManagementAccountNotificationPlugin.bundle/RemoteManagementAccountNotificationPlugin](MACHOS/RemoteManagementAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SyncedDefaultsAccountNotificationPlugin.bundle/SyncedDefaultsAccountNotificationPlugin](MACHOS/SyncedDefaultsAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/TransparencyAccountNotification.bundle/TransparencyAccountNotification](MACHOS/TransparencyAccountNotification.md)
- [/System/Library/Accounts/Notification/iTunesAccountsNotificationPlugin.bundle/iTunesAccountsNotificationPlugin](MACHOS/iTunesAccountsNotificationPlugin.md)
- [/System/Library/Accounts/ServiceOwners/AACloudServiceOwner.bundle/AACloudServiceOwner](MACHOS/AACloudServiceOwner.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/Accounts/ServiceOwners/GCCloudServiceOwner.bundle/GCCloudServiceOwner](MACHOS/GCCloudServiceOwner.md)
- [/System/Library/Accounts/ServiceOwners/IDSServiceOwner.bundle/IDSServiceOwner](MACHOS/IDSServiceOwner.md)
- [/System/Library/AppRemovalServices/com.apple.Bridge.appremoval.xpc/com.apple.Bridge.appremoval](MACHOS/com.apple.Bridge.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.Home.appremoval.xpc/com.apple.Home.appremoval](MACHOS/com.apple.Home.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.Maps.appremoval.xpc/com.apple.Maps.appremoval](MACHOS/com.apple.Maps.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.MobileStore.appremoval.xpc/com.apple.MobileStore.appremoval](MACHOS/com.apple.MobileStore.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.Translate.appremoval.xpc/com.apple.Translate.appremoval](MACHOS/com.apple.Translate.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.VoiceMemos.appremoval.xpc/com.apple.VoiceMemos.appremoval](MACHOS/com.apple.VoiceMemos.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.freeform.appremoval.xpc/com.apple.freeform.appremoval](MACHOS/com.apple.freeform.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.iBooks.appremoval.xpc/com.apple.iBooks.appremoval](MACHOS/com.apple.iBooks.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.mobilecal.appremoval.xpc/com.apple.mobilecal.appremoval](MACHOS/com.apple.mobilecal.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.mobilemail.appremoval.xpc/com.apple.mobilemail.appremoval](MACHOS/com.apple.mobilemail.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.mobilenotes.appremoval.xpc/com.apple.mobilenotes.appremoval](MACHOS/com.apple.mobilenotes.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.news.appremoval.xpc/com.apple.news](MACHOS/com.apple.news.md)
- [/System/Library/AppRemovalServices/com.apple.podcasts.appremoval.xpc/com.apple.podcasts.appremoval](MACHOS/com.apple.podcasts.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.shortcuts.appremoval.xpc/com.apple.shortcuts.appremoval](MACHOS/com.apple.shortcuts.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.tv.appremoval.xpc/com.apple.tv.appremoval](MACHOS/com.apple.tv.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.weather.appremoval.xpc/com.apple.weather.appremoval](MACHOS/com.apple.weather.appremoval.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/WebUI/PlugIns/MusicAMSUIWebPlugin.bundle/MusicAMSUIWebPlugin](MACHOS/MusicAMSUIWebPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AppLaunchPlugin.bundle/AppLaunchPlugin](MACHOS/AppLaunchPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CalendarFlowDelegatePlugin.bundle/CalendarFlowDelegatePlugin](MACHOS/CalendarFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ClockFlowPlugin.bundle/ClockFlowPlugin](MACHOS/ClockFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ContactsFlowDelegatePlugin.bundle/ContactsFlowDelegatePlugin](MACHOS/ContactsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ControlsFlowDelegatePlugin.bundle/ControlsFlowDelegatePlugin](MACHOS/ControlsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/FindMyFlowPlugin.bundle/FindMyFlowPlugin](MACHOS/FindMyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeAutomationFlowDelegatePlugin.bundle/HomeAutomationFlowDelegatePlugin](MACHOS/HomeAutomationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IdentityFlowPlugin.bundle/IdentityFlowPlugin](MACHOS/IdentityFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/MailFlowDelegatePlugin.bundle/MailFlowDelegatePlugin](MACHOS/MailFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/MessagesFlowDelegatePlugin.bundle/MessagesFlowDelegatePlugin](MACHOS/MessagesFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/NotebookFlowPlugin.bundle/NotebookFlowPlugin](MACHOS/NotebookFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/NotificationsFlowDelegatePlugin.bundle/NotificationsFlowDelegatePlugin](MACHOS/NotificationsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PaymentsFlowDelegatePlugin.bundle/PaymentsFlowDelegatePlugin](MACHOS/PaymentsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ReaderFlowPlugin.bundle/ReaderFlowPlugin](MACHOS/ReaderFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SafetySessionFlowPlugin.bundle/SafetySessionFlowPlugin](MACHOS/SafetySessionFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriSuggestionsFlowPlugin.bundle/SiriSuggestionsFlowPlugin](MACHOS/SiriSuggestionsFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SystemCommandsFlowDelegatePlugin.bundle/SystemCommandsFlowDelegatePlugin](MACHOS/SystemCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TranslationFlowDelegatePlugin.bundle/TranslationFlowDelegatePlugin](MACHOS/TranslationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/VideoFlowDelegatePlugin.bundle/VideoFlowDelegatePlugin](MACHOS/VideoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Accessibility.assistantBundle/Accessibility](MACHOS/Accessibility.md)
- [/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications](MACHOS/Applications.md)
- [/System/Library/Assistant/Plugins/ChatKitAssistant.assistantBundle/ChatKitAssistant](MACHOS/ChatKitAssistant.md)
- [/System/Library/Assistant/Plugins/DeviceControl.assistantBundle/DeviceControl](MACHOS/DeviceControl.md)
- [/System/Library/Assistant/Plugins/DoNotDisturbAssistant.assistantBundle/DoNotDisturbAssistant](MACHOS/DoNotDisturbAssistant.md)
- [/System/Library/Assistant/Plugins/Mail.assistantBundle/Mail](MACHOS/Mail.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/Plugins/MobileTimer.assistantBundle/MobileTimer](MACHOS/MobileTimer.md)
- [/System/Library/Assistant/Plugins/NanoAppSync.assistantBundle/NanoAppSync](MACHOS/NanoAppSync.md)
- [/System/Library/Assistant/Plugins/NotificationsSettingsAssistant.assistantBundle/NotificationsSettingsAssistant](MACHOS/NotificationsSettingsAssistant.md)
- [/System/Library/Assistant/Plugins/ParsecContextSync.assistantBundle/ParsecContextSync](MACHOS/ParsecContextSync.md)
- [/System/Library/Assistant/Plugins/ParsecSubscriptionServiceSync.assistantBundle/ParsecSubscriptionServiceSync](MACHOS/ParsecSubscriptionServiceSync.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/Plugins/Safari.assistantBundle/Safari](MACHOS/Safari.md)
- [/System/Library/Assistant/Plugins/SiriFindMyBundle.assistantBundle/SiriFindMyBundle](MACHOS/SiriFindMyBundle.md)
- [/System/Library/Assistant/Plugins/SiriPrivateLearningAnalytics.assistantBundle/SiriPrivateLearningAnalytics](MACHOS/SiriPrivateLearningAnalytics.md)
- [/System/Library/Assistant/Plugins/Social.assistantBundle/Social](MACHOS/Social.md)
- [/System/Library/Assistant/Plugins/Stocks.assistantBundle/Stocks](MACHOS/Stocks.md)
- [/System/Library/Assistant/Plugins/UILite.assistantBundle/UILite](MACHOS/UILite.md)
- [/System/Library/Assistant/Plugins/WatchListAssistant.assistantBundle/WatchListAssistant](MACHOS/WatchListAssistant.md)
- [/System/Library/Assistant/Plugins/WebSearch.assistantBundle/WebSearch](MACHOS/WebSearch.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriReferenceResolutionMetricsPlugin.bundle/SiriReferenceResolutionMetricsPlugin](MACHOS/SiriReferenceResolutionMetricsPlugin.md)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge.md)
- [/System/Library/Assistant/Suggestions/SKEBridge/SiriSuggestionsSKEBridge.bundle/SiriSuggestionsSKEBridge](MACHOS/SiriSuggestionsSKEBridge.md)
- [/System/Library/Assistant/UIPlugins/AcousticId.siriUIBundle/AcousticId](MACHOS/AcousticId.md)
- [/System/Library/Assistant/UIPlugins/AddressBook.siriUIBundle/AddressBook](MACHOS/AddressBook.md)
- [/System/Library/Assistant/UIPlugins/Calendar.siriUIBundle/Calendar](MACHOS/Calendar.md)
- [/System/Library/Assistant/UIPlugins/GeneralKnowledge.siriUIBundle/GeneralKnowledge](MACHOS/GeneralKnowledge.md)
- [/System/Library/Assistant/UIPlugins/Intents.siriUIBundle/Intents](MACHOS/Intents.md)
- [/System/Library/Assistant/UIPlugins/Mail.siriUIBundle/Mail](MACHOS/Mail.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/UIPlugins/MobileTimer.siriUIBundle/MobileTimer](MACHOS/MobileTimer.md)
- [/System/Library/Assistant/UIPlugins/Notes.siriUIBundle/Notes](MACHOS/Notes.md)
- [/System/Library/Assistant/UIPlugins/Notifications.siriUIBundle/Notifications](MACHOS/Notifications.md)
- [/System/Library/Assistant/UIPlugins/RemindersSiriUIPlugin.siriUIBundle/RemindersSiriUIPlugin](MACHOS/RemindersSiriUIPlugin.md)
- [/System/Library/Assistant/UIPlugins/Settings.siriUIBundle/Settings](MACHOS/Settings.md)
- [/System/Library/Assistant/UIPlugins/Stocks.siriUIBundle/Stocks](MACHOS/Stocks.md)
- [/System/Library/Assistant/UIPlugins/System.siriUIBundle/System](MACHOS/System.md)
- [/System/Library/Assistant/UIPlugins/UniversalSearch.siriUIBundle/UniversalSearch](MACHOS/UniversalSearch.md)
- [/System/Library/Assistant/UIPlugins/WAAnswer.siriUIBundle/WAAnswer](MACHOS/WAAnswer.md)
- [/System/Library/Audio/MIDI Drivers/AppleIDAMDriver.plugin/AppleIDAMDriver](MACHOS/AppleIDAMDriver.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIBluetoothDriver.plugin/AppleMIDIBluetoothDriver](MACHOS/AppleMIDIBluetoothDriver.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIRTPDriver.plugin/AppleMIDIRTPDriver](MACHOS/AppleMIDIRTPDriver.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver](MACHOS/AppleMIDIUSBDriver.md)
- [/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver](MACHOS/YamahaUSBMIDIDriver.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/AppleAOPAudioPlugin.driver/AppleAOPAudioPlugin](MACHOS/AppleAOPAudioPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/AppleTimeSyncAudioClock.driver/AppleTimeSyncAudioClock](MACHOS/AppleTimeSyncAudioClock.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/BasebandVoice.driver/BasebandVoice](MACHOS/BasebandVoice.md)
- [/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin](MACHOS/BuiltinAudioPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/NetworkUplinkClock.driver/NetworkUplinkClock](MACHOS/NetworkUplinkClock.md)
- [/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen](MACHOS/OctaviaHalogen.md)
- [/System/Library/Audio/Plug-Ins/RemoteInput/AudioAppleSiriRemoteInput.bundle/AudioAppleSiriRemoteInput](MACHOS/AudioAppleSiriRemoteInput.md)
- [/System/Library/Audio/Plug-Ins/RemoteInput/JarvisPlugin.bundle/JarvisPlugin](MACHOS/JarvisPlugin.md)
- [/System/Library/Audio/Plug-Ins/RemoteInput/RemoteAudioInputPlugin.bundle/RemoteAudioInputPlugin](MACHOS/RemoteAudioInputPlugin.md)
- [/System/Library/BulletinDistributor/PingSubscribers/NanoCalendarPingSubscriber.bundle/NanoCalendarPingSubscriber](MACHOS/NanoCalendarPingSubscriber.md)
- [/System/Library/BulletinDistributor/PingSubscribers/NanoHealthPingSubscriber.bundle/NanoHealthPingSubscriber](MACHOS/NanoHealthPingSubscriber.md)
- [/System/Library/BulletinDistributor/PingSubscribers/SearchPartyNotificationPingSubscriber.bundle/SearchPartyNotificationPingSubscriber](MACHOS/SearchPartyNotificationPingSubscriber.md)
- [/System/Library/BulletinDistributor/PingSubscribers/ShortcutsPingSubscriber.bundle/ShortcutsPingSubscriber](MACHOS/ShortcutsPingSubscriber.md)
- [/System/Library/CloudRecommendations/ClientSources/ICQReviewLargeFilesRecommendations.bundle/ICQReviewLargeFilesRecommendations](MACHOS/ICQReviewLargeFilesRecommendations.md)
- [/System/Library/CloudRecommendations/ClientSources/PhotosCloudRecommendations.bundle/PhotosCloudRecommendations](MACHOS/PhotosCloudRecommendations.md)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/ContinuousExposeModule.bundle/ContinuousExposeModule](MACHOS/ContinuousExposeModule.md)
- [/System/Library/ControlCenter/Bundles/FocusUIModule.bundle/FocusUIModule](MACHOS/FocusUIModule.md)
- [/System/Library/ControlCenter/Bundles/NFCControlCenterModule.bundle/NFCControlCenterModule](MACHOS/NFCControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/PingMyWatchControlCenterUI.bundle/PingMyWatchControlCenterUI](MACHOS/PingMyWatchControlCenterUI.md)
- [/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule](MACHOS/ReplayKitModule.md)
- [/System/Library/ControlCenter/Bundles/SilenceCallsCCWidget.bundle/SilenceCallsCCWidget](MACHOS/SilenceCallsCCWidget.md)
- [/System/Library/ControlCenter/Bundles/SystemQuickNoteModule.bundle/SystemQuickNoteModule](MACHOS/SystemQuickNoteModule.md)
- [/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule](MACHOS/VideoConferenceControlCenterModule.md)
- [/System/Library/CoreImage/CIBarcode.cifilter/CIBarcode](MACHOS/CIBarcode.md)
- [/System/Library/CoreImage/CIPassThrough.cifilter/CIPassThrough](MACHOS/CIPassThrough.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/PortraitFilters](MACHOS/PortraitFilters.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer](MACHOS/AccessibilityUIServer.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents](MACHOS/AccessibilityAppIntents.md)
- [/System/Library/CoreServices/AegirProxyApp.app/AegirProxyApp](MACHOS/AegirProxyApp.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/CacheDeleteAppContainerCaches](MACHOS/CacheDeleteAppContainerCaches.md)
- [/System/Library/CoreServices/CacheDeleteDaily](MACHOS/CacheDeleteDaily.md)
- [/System/Library/CoreServices/CarPlay.app/CarPlay](MACHOS/CarPlay.md)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/CloudSettingsSyncAgent](MACHOS/CloudSettingsSyncAgent.md)
- [/System/Library/CoreServices/CommandAndControl.app/CommandAndControl](MACHOS/CommandAndControl.md)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001](MACHOS/MobileDevices-0001.md)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002](MACHOS/MobileDevices-0002.md)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003](MACHOS/MobileDevices-0003.md)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices.bundle/MobileDevices](MACHOS/MobileDevices.md)
- [/System/Library/CoreServices/DeviceOMatic.app/DeviceOMatic](MACHOS/DeviceOMatic.md)
- [/System/Library/CoreServices/EscrowSecurityAlert.app/EscrowSecurityAlert](MACHOS/EscrowSecurityAlert.md)
- [/System/Library/CoreServices/FullKeyboardAccess.app/FullKeyboardAccess](MACHOS/FullKeyboardAccess.md)
- [/System/Library/CoreServices/IOUIAngel.app/IOUIAngel](MACHOS/IOUIAngel.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/MediaMLPluginApp.app/MediaMLPluginApp](MACHOS/MediaMLPluginApp.md)
- [/System/Library/CoreServices/MediaMLPluginApp.app/PlugIns/MediaMLPlugin.appex/MediaMLPlugin](MACHOS/MediaMLPlugin.md)
- [/System/Library/CoreServices/OTACrashCopier](MACHOS/OTACrashCopier.md)
- [/System/Library/CoreServices/OverlayUI.app/OverlayUI](MACHOS/OverlayUI.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer](MACHOS/ScreenSharingServer.md)
- [/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension](MACHOS/ShortcutsTopHitsExtension.md)
- [/System/Library/CoreServices/ShortcutsActions.app/ShortcutsActions](MACHOS/ShortcutsActions.md)
- [/System/Library/CoreServices/SpringBoard.app/PlugIns/SpringBoardDiagnosticExtension.appex/SpringBoardDiagnosticExtension](MACHOS/SpringBoardDiagnosticExtension.md)
- [/System/Library/CoreServices/SpringBoard.app/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/scrod](MACHOS/scrod.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/iconservicesagent](MACHOS/iconservicesagent.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd](MACHOS/usbsmartcardreaderd.md)
- [/System/Library/DataClassMigrators/00LaunchServicesMigrator.migrator/00LaunchServicesMigrator](MACHOS/00LaunchServicesMigrator.md)
- [/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration](MACHOS/AccessibilityDataMigration.md)
- [/System/Library/DataClassMigrators/Accounts.migrator/Accounts](MACHOS/Accounts.md)
- [/System/Library/DataClassMigrators/AccountsObsolescence.migrator/AccountsObsolescence](MACHOS/AccountsObsolescence.md)
- [/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy](MACHOS/AddressBookLegacy.md)
- [/System/Library/DataClassMigrators/AirTrafficMigrator.migrator/AirTrafficMigrator](MACHOS/AirTrafficMigrator.md)
- [/System/Library/DataClassMigrators/AnisetteMigrator.migrator/AnisetteMigrator](MACHOS/AnisetteMigrator.md)
- [/System/Library/DataClassMigrators/AppUserDataMigrator.migrator/AppUserDataMigrator](MACHOS/AppUserDataMigrator.md)
- [/System/Library/DataClassMigrators/AppleAccountMigrator.migrator/AppleAccountMigrator](MACHOS/AppleAccountMigrator.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/CallHistoryDataMigrator.migrator/CallHistoryDataMigrator](MACHOS/CallHistoryDataMigrator.md)
- [/System/Library/DataClassMigrators/CloudRecentsMigrator.migrator/CloudRecentsMigrator](MACHOS/CloudRecentsMigrator.md)
- [/System/Library/DataClassMigrators/CloudTabsMigrator.migrator/CloudTabsMigrator](MACHOS/CloudTabsMigrator.md)
- [/System/Library/DataClassMigrators/ContainerMigrator.migrator/ContainerMigrator](MACHOS/ContainerMigrator.md)
- [/System/Library/DataClassMigrators/CookieDataMigrator.migrator/CookieDataMigrator](MACHOS/CookieDataMigrator.md)
- [/System/Library/DataClassMigrators/CoreLocationMigrator.migrator/CoreLocationMigrator](MACHOS/CoreLocationMigrator.md)
- [/System/Library/DataClassMigrators/CoreTimeMigrator.migrator/CoreTimeMigrator](MACHOS/CoreTimeMigrator.md)
- [/System/Library/DataClassMigrators/FitnessMigrator.migrator/FitnessMigrator](MACHOS/FitnessMigrator.md)
- [/System/Library/DataClassMigrators/HAENDataMigrator.migrator/HAENDataMigrator](MACHOS/HAENDataMigrator.md)
- [/System/Library/DataClassMigrators/InternationalSupportMigrator.migrator/InternationalSupportMigrator](MACHOS/InternationalSupportMigrator.md)
- [/System/Library/DataClassMigrators/KeyboardMigrator.migrator/KeyboardMigrator](MACHOS/KeyboardMigrator.md)
- [/System/Library/DataClassMigrators/KeyboardUIMigrator.migrator/KeyboardUIMigrator](MACHOS/KeyboardUIMigrator.md)
- [/System/Library/DataClassMigrators/KeychainMigrator.migrator/KeychainMigrator](MACHOS/KeychainMigrator.md)
- [/System/Library/DataClassMigrators/LanguageAssetMigrator.migrator/LanguageAssetMigrator](MACHOS/LanguageAssetMigrator.md)
- [/System/Library/DataClassMigrators/LegacyMessageAccountsMigrator.migrator/LegacyMessageAccountsMigrator](MACHOS/LegacyMessageAccountsMigrator.md)
- [/System/Library/DataClassMigrators/MCCleanup.migrator/MCCleanup](MACHOS/MCCleanup.md)
- [/System/Library/DataClassMigrators/MCMDM.migrator/MCMDM](MACHOS/MCMDM.md)
- [/System/Library/DataClassMigrators/MCProfile.migrator/MCProfile](MACHOS/MCProfile.md)
- [/System/Library/DataClassMigrators/MKBMigrator.migrator/MKBMigrator](MACHOS/MKBMigrator.md)
- [/System/Library/DataClassMigrators/MSUDataMigrator.migrator/MSUDataMigrator](MACHOS/MSUDataMigrator.md)
- [/System/Library/DataClassMigrators/MediaLibrary.migrator/MediaLibrary](MACHOS/MediaLibrary.md)
- [/System/Library/DataClassMigrators/MergeBuddyProvisioningResponse.migrator/MergeBuddyProvisioningResponse](MACHOS/MergeBuddyProvisioningResponse.md)
- [/System/Library/DataClassMigrators/MessageAccountsMigrator.migrator/MessageAccountsMigrator](MACHOS/MessageAccountsMigrator.md)
- [/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator](MACHOS/MobileActivationMigrator.md)
- [/System/Library/DataClassMigrators/MobileAsset.migrator/MobileAsset](MACHOS/MobileAsset.md)
- [/System/Library/DataClassMigrators/MobileGestaltMigrator.migrator/MobileGestaltMigrator](MACHOS/MobileGestaltMigrator.md)
- [/System/Library/DataClassMigrators/MobileMailMigrator.migrator/MobileMailMigrator](MACHOS/MobileMailMigrator.md)
- [/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari](MACHOS/MobileSafari.md)
- [/System/Library/DataClassMigrators/MobileSlideShow.migrator/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/System/Library/DataClassMigrators/PassbookDataMigrator.migrator/PassbookDataMigrator](MACHOS/PassbookDataMigrator.md)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator.md)
- [/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess](MACHOS/RestorePostProcess.md)
- [/System/Library/DataClassMigrators/Shortcuts.migrator/Shortcuts](MACHOS/Shortcuts.md)
- [/System/Library/DataClassMigrators/Siri.migrator/Siri](MACHOS/Siri.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DataClassMigrators/StocksMigrator.migrator/StocksMigrator](MACHOS/StocksMigrator.md)
- [/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator](MACHOS/SystemAppMigrator.md)
- [/System/Library/DataClassMigrators/TVMigrator.migrator/TVMigrator](MACHOS/TVMigrator.md)
- [/System/Library/DataClassMigrators/Tones.migrator/Tones](MACHOS/Tones.md)
- [/System/Library/DataClassMigrators/Vibrations.migrator/Vibrations](MACHOS/Vibrations.md)
- [/System/Library/DataClassMigrators/WebBookmarks.migrator/WebBookmarks](MACHOS/WebBookmarks.md)
- [/System/Library/DataClassMigrators/WiFiDataMigrator.migrator/WiFiDataMigrator](MACHOS/WiFiDataMigrator.md)
- [/System/Library/DataClassMigrators/iTunesStore.migrator/iTunesStore](MACHOS/iTunesStore.md)
- [/System/Library/DigitalSeparation/SharingSources/ActivityDigitalSeparation.bundle/ActivityDigitalSeparation](MACHOS/ActivityDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/CalendarSeparation.bundle/CalendarSeparation](MACHOS/CalendarSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/DSNotesPlugin.bundle/DSNotesPlugin](MACHOS/DSNotesPlugin.md)
- [/System/Library/DigitalSeparation/SharingSources/DigitalSeparationBundle.bundle/DigitalSeparationBundle](MACHOS/DigitalSeparationBundle.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMy.bundle/FindMy](MACHOS/FindMy.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyItemsDigitalSeparation.bundle/FindMyItemsDigitalSeparation](MACHOS/FindMyItemsDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/HealthSharingSeparation.bundle/HealthSharingSeparation](MACHOS/HealthSharingSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/MapsDigitalSeparation.bundle/MapsDigitalSeparation](MACHOS/MapsDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/PhotosSeparation.bundle/PhotosSeparation](MACHOS/PhotosSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/SafetyMonitorSeparation.bundle/SafetyMonitorSeparation](MACHOS/SafetyMonitorSeparation.md)
- [/System/Library/DistributedEvaluation/Plugins/AutocorrectionTesterDESPlugin.desPlugin/AutocorrectionTesterDESPlugin](MACHOS/AutocorrectionTesterDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/DictationPersonalizationFides2Plugin.desPlugin/DictationPersonalizationFides2Plugin](MACHOS/DictationPersonalizationFides2Plugin.md)
- [/System/Library/DistributedEvaluation/Plugins/GlobalNNLMFidesPlugin.desPlugin/GlobalNNLMFidesPlugin](MACHOS/GlobalNNLMFidesPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/InertiaCamDES.desPlugin/InertiaCamDES](MACHOS/InertiaCamDES.md)
- [/System/Library/DistributedEvaluation/Plugins/PMLDESPlugin.desPlugin/PMLDESPlugin](MACHOS/PMLDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/PeopleSuggesterDESPlugin.desPlugin/PeopleSuggesterDESPlugin](MACHOS/PeopleSuggesterDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/QuickTypeDESPlugin.desPlugin/QuickTypeDESPlugin](MACHOS/QuickTypeDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/RemindersDES.desPlugin/RemindersDES](MACHOS/RemindersDES.md)
- [/System/Library/DistributedEvaluation/Plugins/TypingDESPlugin.desPlugin/TypingDESPlugin](MACHOS/TypingDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/siriinference-dodml-plugin.desPlugin/siriinference-dodml-plugin](MACHOS/siriinference-dodml-plugin.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.driving-trigger.bundle/com.apple.donotdisturb.private.driving-trigger](MACHOS/com.apple.donotdisturb.private.driving-trigger.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.intents.preload.bundle/com.apple.donotdisturb.private.intents.preload](MACHOS/com.apple.donotdisturb.private.intents.preload.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.workout-trigger.bundle/com.apple.donotdisturb.private.workout-trigger](MACHOS/com.apple.donotdisturb.private.workout-trigger.md)
- [/System/Library/DriverExtensions/com.apple.AFKUserHIDDrivers.dext/com.apple.AFKUserHIDDrivers](MACHOS/com.apple.AFKUserHIDDrivers.md)
- [/System/Library/DriverExtensions/com.apple.AppleUserHIDDrivers.dext/com.apple.AppleUserHIDDrivers](MACHOS/com.apple.AppleUserHIDDrivers.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetE1000.dext/com.apple.DriverKit-AppleEthernetE1000](MACHOS/com.apple.DriverKit-AppleEthernetE1000.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetIXGBE.dext/com.apple.DriverKit-AppleEthernetIXGBE](MACHOS/com.apple.DriverKit-AppleEthernetIXGBE.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetIXL.dext/com.apple.DriverKit-AppleEthernetIXL](MACHOS/com.apple.DriverKit-AppleEthernetIXL.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetMLX5.dext/com.apple.DriverKit-AppleEthernetMLX5](MACHOS/com.apple.DriverKit-AppleEthernetMLX5.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit.AppleUserECM.dext/com.apple.DriverKit.AppleUserECM](MACHOS/com.apple.DriverKit.AppleUserECM.md)
- [/System/Library/DuetActivityScheduler/Scheduler/DuetActivitySchedulerDaemon.bundle/DuetActivitySchedulerDaemon](MACHOS/DuetActivitySchedulerDaemon.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppExtensionManagement.appex/AppExtensionManagement](MACHOS/AppExtensionManagement.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/BitacoraWorker.appex/BitacoraWorker](MACHOS/BitacoraWorker.md)
- [/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension](MACHOS/ComposeReviewExtension.md)
- [/System/Library/ExtensionKit/Extensions/DeepThoughtWorker.appex/DeepThoughtWorker](MACHOS/DeepThoughtWorker.md)
- [/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension](MACHOS/DevicePropertiesExtension.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension](MACHOS/ExperimentationExtension.md)
- [/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU](MACHOS/com.apple.WebKit.GPU.md)
- [/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension](MACHOS/MADViewServiceExtension.md)
- [/System/Library/ExtensionKit/Extensions/MapsTransactionInsightsExtension.appex/MapsTransactionInsightsExtension](MACHOS/MapsTransactionInsightsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension](MACHOS/MetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking](MACHOS/com.apple.WebKit.Networking.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK](MACHOS/PFLHRPeriodPredCK.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush](MACHOS/PFLHRPeriodPredPush.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/ProactiveShareSheetLighthouseBackgroundPlugin.appex/ProactiveShareSheetLighthouseBackgroundPlugin](MACHOS/ProactiveShareSheetLighthouseBackgroundPlugin.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriCoreMetricsWorker.appex/SiriCoreMetricsWorker](MACHOS/SiriCoreMetricsWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/SiriMASPFLCK](MACHOS/SiriMASPFLCK.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLPlugin.appex/SiriMASPFLPlugin](MACHOS/SiriMASPFLPlugin.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/SiriMASPFLPush](MACHOS/SiriMASPFLPush.md)
- [/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin](MACHOS/SiriSuggestionsLightHousePlugin.md)
- [/System/Library/ExtensionKit/Extensions/SiriUserSegmentation.appex/SiriUserSegmentation](MACHOS/SiriUserSegmentation.md)
- [/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal](MACHOS/com.apple.WebKit.WebContent.CaptivePortal.md)
- [/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent](MACHOS/com.apple.WebKit.WebContent.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat](MACHOS/com.apple.fskit.exfat.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker](MACHOS/com.apple.mlhost.CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.QuartzWorker.appex/com.apple.mlhost.QuartzWorker](MACHOS/com.apple.mlhost.QuartzWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Extensions/ASIOKit.kext/ASIOKit](MACHOS/ASIOKit.md)
- [/System/Library/Extensions/AppleBiometricSensor.kext/PlugIns/AppleMesaLib.plugin/AppleMesaLib](MACHOS/AppleMesaLib.md)
- [/System/Library/Extensions/AppleGameControllerPersonality.kext/AppleGameControllerPersonality](MACHOS/AppleGameControllerPersonality.md)
- [/System/Library/Extensions/AppleHIDALSService.kext/PlugIns/AppleHIDALS.plugin/AppleHIDALS](MACHOS/AppleHIDALS.md)
- [/System/Library/Extensions/AppleHPM.kext/PlugIns/AppleHPMLib.plugin/AppleHPMLib](MACHOS/AppleHPMLib.md)
- [/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode](MACHOS/AppleLockdownMode.md)
- [/System/Library/Extensions/ApplePMUFirmwareDriver.kext/ApplePMUFirmwareDriver](MACHOS/ApplePMUFirmwareDriver.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/FastpathLib.plugin/FastpathLib](MACHOS/FastpathLib.md)
- [/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib](MACHOS/RoseControllerLib.md)
- [/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleTopCaseHIDEventDriver.kext/AppleTopCaseHIDEventDriver](MACHOS/AppleTopCaseHIDEventDriver.md)
- [/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleUSBTopCaseDriver.kext/AppleUSBTopCaseDriver](MACHOS/AppleUSBTopCaseDriver.md)
- [/System/Library/Extensions/AppleUVDM.kext/PlugIns/AppleUVDMLib.plugin/AppleUVDMLib](MACHOS/AppleUVDMLib.md)
- [/System/Library/Extensions/EAP-RSA.ppp/EAP-RSA](MACHOS/EAP-RSA.md)
- [/System/Library/Extensions/IOStreamFamily.kext/PlugIns/IOStreamLib.plugin/IOStreamLib](MACHOS/IOStreamLib.md)
- [/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBLib.bundle/IOUSBLib](MACHOS/IOUSBLib.md)
- [/System/Library/Extensions/lifs.kext/lifs](MACHOS/lifs.md)
- [/System/Library/Filesystems/apfs.fs/apfs.util](MACHOS/apfs.util.md)
- [/System/Library/Filesystems/apfs.fs/apfs_boot_util](MACHOS/apfs_boot_util.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkdigest](MACHOS/apfs_checkdigest.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_iosd](MACHOS/apfs_iosd.md)
- [/System/Library/Filesystems/apfs.fs/apfs_stats](MACHOS/apfs_stats.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/mount_apfs](MACHOS/mount_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/slurpAPFSMeta](MACHOS/slurpAPFSMeta.md)
- [/System/Library/Filesystems/apfs.fs/sm_stats](MACHOS/sm_stats.md)
- [/System/Library/Filesystems/apfs_userfs.fs/apfs_userfs.util](MACHOS/apfs_userfs.util.md)
- [/System/Library/Filesystems/apfs_userfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs_userfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/exfat.fs/exfat.util](MACHOS/exfat.util.md)
- [/System/Library/Filesystems/exfat.fs/fsck_exfat](MACHOS/fsck_exfat.md)
- [/System/Library/Filesystems/exfat.fs/newfs_exfat](MACHOS/newfs_exfat.md)
- [/System/Library/Filesystems/hfs.fs/CopyHFSMeta](MACHOS/CopyHFSMeta.md)
- [/System/Library/Filesystems/hfs.fs/fsck_hfs](MACHOS/fsck_hfs.md)
- [/System/Library/Filesystems/hfs.fs/hfs.util](MACHOS/hfs.util.md)
- [/System/Library/Filesystems/hfs.fs/mount_hfs](MACHOS/mount_hfs.md)
- [/System/Library/Filesystems/hfs.fs/newfs_hfs](MACHOS/newfs_hfs.md)
- [/System/Library/Filesystems/msdos.fs/fsck_msdos](MACHOS/fsck_msdos.md)
- [/System/Library/Filesystems/msdos.fs/msdos.util](MACHOS/msdos.util.md)
- [/System/Library/Filesystems/msdos.fs/newfs_msdos](MACHOS/newfs_msdos.md)
- [/System/Library/Filesystems/ntfs.fs/BootCampFormatter](MACHOS/BootCampFormatter.md)
- [/System/Library/Filesystems/ntfs.fs/ntfs.util](MACHOS/ntfs.util.md)
- [/System/Library/Filesystems/tmpfs.fs/mount_tmpfs](MACHOS/mount_tmpfs.md)
- [/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService](MACHOS/AVAudioDeviceTestService.md)
- [/System/Library/Frameworks/AVKit.framework/XPCServices/SharedPreferences.xpc/SharedPreferences](MACHOS/SharedPreferences.md)
- [/System/Library/Frameworks/Accounts.framework/accountsd](MACHOS/accountsd.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd.md)
- [/System/Library/Frameworks/AddressBook.framework/Support/ABDatabaseDoctor](MACHOS/ABDatabaseDoctor.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/XPCServices/EnforcementService.xpc/EnforcementService](MACHOS/EnforcementService.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterService.xpc/AudioConverterService](MACHOS/AudioConverterService.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/CFNetwork.framework/AuthBrokerAgent](MACHOS/AuthBrokerAgent.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetworkAgent](MACHOS/CFNetworkAgent.md)
- [/System/Library/Frameworks/CFNetwork.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/ClassKit.framework/PlugIns/ClassKitDiagnosticExtension.appex/ClassKitDiagnosticExtension](MACHOS/ClassKitDiagnosticExtension.md)
- [/System/Library/Frameworks/ClassKit.framework/progressd](MACHOS/progressd.md)
- [/System/Library/Frameworks/ClockKit.framework/XPCServices/CLKCompanionWatchFaceLibraryService.xpc/CLKCompanionWatchFaceLibraryService](MACHOS/CLKCompanionWatchFaceLibraryService.md)
- [/System/Library/Frameworks/Contacts.framework/PlugIns/ContactsCoreSpotlightExtension.appex/ContactsCoreSpotlightExtension](MACHOS/ContactsCoreSpotlightExtension.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService](MACHOS/ContactViewViewService.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService](MACHOS/ContactsViewService.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/CoreGraphics.framework/XPCServices/CGPDFService.xpc/CGPDFService](MACHOS/CGPDFService.md)
- [/System/Library/Frameworks/CoreImage.framework/coreui_archive_bin.metallib](MACHOS/coreui_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/photo_style_archive_bin.metallib](MACHOS/photo_style_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/portrait_filters_archive_bin.metallib](MACHOS/portrait_filters_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationTemporaryPreciseAuthPromptPlugin.appex/CoreLocationTemporaryPreciseAuthPromptPlugin](MACHOS/CoreLocationTemporaryPreciseAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationVanillaWhenInUseAuthPromptPlugin.appex/CoreLocationVanillaWhenInUseAuthPromptPlugin](MACHOS/CoreLocationVanillaWhenInUseAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice](MACHOS/maphelperservice.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreMIDI.framework/MIDIServer](MACHOS/MIDIServer.md)
- [/System/Library/Frameworks/CoreML.framework/XPCServices/CoreMLModelSecurityService.xpc/CoreMLModelSecurityService](MACHOS/CoreMLModelSecurityService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension1_iOS.appex/CoreSpotlightImportExtension1_iOS](MACHOS/CoreSpotlightImportExtension1_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension2_iOS.appex/CoreSpotlightImportExtension2_iOS](MACHOS/CoreSpotlightImportExtension2_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/PlugIns/CTFollowUpExtension.appex/CTFollowUpExtension](MACHOS/CTFollowUpExtension.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/XPCServices/CTParserService.xpc/CTParserService](MACHOS/CTParserService.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter](MACHOS/CommCenter.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper](MACHOS/CommCenterRootHelper.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/PlugIns/pivtoken.appex/pivtoken](MACHOS/pivtoken.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/PlugIns/secelemtoken.appex/secelemtoken](MACHOS/secelemtoken.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/ctkd](MACHOS/ctkd.md)
- [/System/Library/Frameworks/EventKit.framework/PlugIns/CalendarDiagnosticExtension.appex/CalendarDiagnosticExtension](MACHOS/CalendarDiagnosticExtension.md)
- [/System/Library/Frameworks/ExposureNotification.framework/XPCServices/ExposureNotificationService.xpc/ExposureNotificationService](MACHOS/ExposureNotificationService.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/XPCServices/extensionkitservice.xpc/extensionkitservice](MACHOS/extensionkitservice.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/PlugIns/ExternalAccessoryWACUIBits.bundle/ExternalAccessoryWACUIBits](MACHOS/ExternalAccessoryWACUIBits.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/PlugIns/com.apple.ExternalAccessory.WACUI.appex/com.apple.ExternalAccessory.WACUI](MACHOS/com.apple.ExternalAccessory.WACUI.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/XPCServices/WACEAService.xpc/WACEAService](MACHOS/WACEAService.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/FamilyControlsOverrideSettingsExtension.appex/FamilyControlsOverrideSettingsExtension](MACHOS/FamilyControlsOverrideSettingsExtension.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/CloudDocsFileProvider.bundle/CloudDocsFileProvider](MACHOS/CloudDocsFileProvider.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/FileProviderOverride.bundle/FileProviderOverride](MACHOS/FileProviderOverride.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/iCloudDriveFileProviderOverride.bundle/iCloudDriveFileProviderOverride](MACHOS/iCloudDriveFileProviderOverride.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd](MACHOS/fileproviderd.md)
- [/System/Library/Frameworks/FileProviderUI.framework/PlugIns/ServerAuthUIExtension.appex/ServerAuthUIExtension](MACHOS/ServerAuthUIExtension.md)
- [/System/Library/Frameworks/FinanceKit.framework/financed](MACHOS/financed.md)
- [/System/Library/Frameworks/GSS.framework/Helpers/GSSCred](MACHOS/GSSCred.md)
- [/System/Library/Frameworks/GameController.framework/VirtualGameController.bundle/VirtualGameController](MACHOS/VirtualGameController.md)
- [/System/Library/Frameworks/GroupActivities.framework/XPCServices/GroupSessionService.xpc/GroupSessionService](MACHOS/GroupSessionService.md)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthCustomerDiagnosticExtension.appex/com.apple.HealthKit.HealthCustomerDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthCustomerDiagnosticExtension.md)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthDiagnosticExtension.appex/com.apple.HealthKit.HealthDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthDiagnosticExtension.md)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.appex/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.md)
- [/System/Library/Frameworks/HealthKit.framework/healthd](MACHOS/healthd.md)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension](MACHOS/HomeKitDiagnosticExtension.md)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitIntentExtension.appex/HomeKitIntentExtension](MACHOS/HomeKitIntentExtension.md)
- [/System/Library/Frameworks/IdentityLookup.framework/XPCServices/com.apple.IdentityLookup.MessageFilter.xpc/com.apple.IdentityLookup.MessageFilter](MACHOS/com.apple.IdentityLookup.MessageFilter.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc](MACHOS/icprefd-xpc.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc](MACHOS/mscamerad-xpc.md)
- [/System/Library/Frameworks/ImageIO.framework/PlugIns/com.apple.imageimporter.appex/com.apple.imageimporter](MACHOS/com.apple.imageimporter.md)
- [/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService](MACHOS/ImageIOXPCService.md)
- [/System/Library/Frameworks/Intents.framework/XPCServices/intents_helper.xpc/intents_helper](MACHOS/intents_helper.md)
- [/System/Library/Frameworks/LinkPresentation.framework/PlugIns/YouTubePlayer.wkbundle/YouTubePlayer](MACHOS/YouTubePlayer.md)
- [/System/Library/Frameworks/LinkPresentation.framework/XPCServices/com.apple.LinkPresentation.LinkSnapshotGeneratorService.xpc/com.apple.LinkPresentation.LinkSnapshotGeneratorService](MACHOS/com.apple.LinkPresentation.LinkSnapshotGeneratorService.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/MechPasscode](MACHOS/MechPasscode.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl](MACHOS/MechPearl.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPushButton.bundle/MechPushButton](MACHOS/MechPushButton.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId](MACHOS/MechTouchId.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM](MACHOS/ModuleACM.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd](MACHOS/applicensedeliveryd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/MapKit.framework/XPCServices/com.apple.MapKit.SnapshotService.xpc/com.apple.MapKit.SnapshotService](MACHOS/com.apple.MapKit.SnapshotService.md)
- [/System/Library/Frameworks/MediaAccessibility.framework/XPCServices/com.apple.accessibility.mediaaccessibilityd.xpc/com.apple.accessibility.mediaaccessibilityd](MACHOS/com.apple.accessibility.mediaaccessibilityd.md)
- [/System/Library/Frameworks/MediaPlayer.framework/PlugIns/MediaPlayerDiagnosticExtension.appex/MediaPlayerDiagnosticExtension](MACHOS/MediaPlayerDiagnosticExtension.md)
- [/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService](MACHOS/RemotePlayerService.md)
- [/System/Library/Frameworks/MessageUI.framework/PlugIns/MessageUI.wkbundle/MessageUI](MACHOS/MessageUI.md)
- [/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService](MACHOS/MTLCompilerService.md)
- [/System/Library/Frameworks/ModelIO.framework/XPCServices/AssetLoader.xpc/AssetLoader](MACHOS/AssetLoader.md)
- [/System/Library/Frameworks/NetworkExtension.framework/PlugIns/NEIKEv2Provider.appex/NEIKEv2Provider](MACHOS/NEIKEv2Provider.md)
- [/System/Library/Frameworks/OSLog.framework/XPCServices/OSLogService.xpc/OSLogService](MACHOS/OSLogService.md)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/PDFImporter.appex/PDFImporter](MACHOS/PDFImporter.md)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Preview.appex/com.apple.PDFKit.OFD_Preview](MACHOS/com.apple.PDFKit.OFD_Preview.md)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Thumbnail.appex/com.apple.PDFKit.OFD_Thumbnail](MACHOS/com.apple.PDFKit.OFD_Thumbnail.md)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.PDFExtensionView.appex/com.apple.PDFKit.PDFExtensionView](MACHOS/com.apple.PDFKit.PDFExtensionView.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/ApplePayDiagnostics.appex/ApplePayDiagnostics](MACHOS/ApplePayDiagnostics.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitEngagementExtension.appex/PassKitEngagementExtension](MACHOS/PassKitEngagementExtension.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitIntentsExtension.appex/PassKitIntentsExtension](MACHOS/PassKitIntentsExtension.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitIntentsUIExtension.appex/PassKitIntentsUIExtension](MACHOS/PassKitIntentsUIExtension.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitSpotlightIndexExtension.appex/PassKitSpotlightIndexExtension](MACHOS/PassKitSpotlightIndexExtension.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitThumbnailExtension.appex/PassKitThumbnailExtension](MACHOS/PassKitThumbnailExtension.md)
- [/System/Library/Frameworks/QuickLook.framework/PlugIns/QLWebKitBundle.wkbundle/QLWebKitBundle](MACHOS/QLWebKitBundle.md)
- [/System/Library/Frameworks/QuickLook.framework/PlugIns/com.apple.quicklook.extension.previewUI.appex/com.apple.quicklook.extension.previewUI](MACHOS/com.apple.quicklook.extension.previewUI.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent](MACHOS/com.apple.quicklook.ThumbnailsAgent.md)
- [/System/Library/Frameworks/ReplayKit.framework/PlugIns/RPBroadcastActivityViewControllerExtension.appex/RPBroadcastActivityViewControllerExtension](MACHOS/RPBroadcastActivityViewControllerExtension.md)
- [/System/Library/Frameworks/ReplayKit.framework/PlugIns/RPVideoEditorExtension.appex/RPVideoEditorExtension](MACHOS/RPVideoEditorExtension.md)
- [/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader](MACHOS/com.apple.SafariServices.ContentBlockerLoader.md)
- [/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/XPCAcmeService.xpc/XPCAcmeService](MACHOS/XPCAcmeService.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/Frameworks/SensorKit.framework/PlugIns/SensorKitViewService.appex/SensorKitViewService](MACHOS/SensorKitViewService.md)
- [/System/Library/Frameworks/SensorKit.framework/Support/srsupporttool](MACHOS/srsupporttool.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitDataExport.xpc/SensorKitDataExport](MACHOS/SensorKitDataExport.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitLongTermStorageHelper.xpc/SensorKitLongTermStorageHelper](MACHOS/SensorKitLongTermStorageHelper.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKit.CHSupportService.xpc/com.apple.SensorKit.CHSupportService](MACHOS/com.apple.SensorKit.CHSupportService.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKitAppHelper.xpc/com.apple.SensorKitAppHelper](MACHOS/com.apple.SensorKitAppHelper.md)
- [/System/Library/Frameworks/ShazamKit.framework/PlugIns/ShazamNotificationContentExtension.appex/ShazamNotificationContentExtension](MACHOS/ShazamNotificationContentExtension.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension](MACHOS/SKAskPermissionExtension.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/System.framework/System_asan](MACHOS/System_asan.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SCHelper](MACHOS/SCHelper.md)
- [/System/Library/Frameworks/Translation.framework/translationd](MACHOS/translationd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ShareUI.appex/com.apple.UIKit.ShareUI](MACHOS/com.apple.UIKit.ShareUI.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/XPCServices/com.apple.VideoSubscriberAccount.DeveloperService.xpc/com.apple.VideoSubscriberAccount.DeveloperService](MACHOS/com.apple.VideoSubscriberAccount.DeveloperService.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/XPCServices/com.apple.VideoSubscriberAccount.PrivacyService.xpc/com.apple.VideoSubscriberAccount.PrivacyService](MACHOS/com.apple.VideoSubscriberAccount.PrivacyService.md)
- [/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/videodecodeservice](MACHOS/videodecodeservice.md)
- [/System/Library/Frameworks/VisionKit.framework/PlugIns/KeyboardCamera.appex/KeyboardCamera](MACHOS/KeyboardCamera.md)
- [/System/Library/Frameworks/WatchKit.framework/Support/companionappd](MACHOS/companionappd.md)
- [/System/Library/Frameworks/WeatherKit.framework/XPCServices/com.apple.weatherkit.authservice.xpc/com.apple.weatherkit.authservice](MACHOS/com.apple.weatherkit.authservice.md)
- [/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond](MACHOS/adattributiond.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin](MACHOS/ColourSensorFilterPlugin.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleDeviceManagementHIDFilter.plugin/AppleDeviceManagementHIDFilter](MACHOS/AppleDeviceManagementHIDFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter](MACHOS/AppleProxServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleWirelessChargingServiceFilter.plugin/AppleWirelessChargingServiceFilter](MACHOS/AppleWirelessChargingServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter](MACHOS/GamepadHIDServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/SafetyServiceFilter.plugin/SafetyServiceFilter](MACHOS/SafetyServiceFilter.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/DualSenseHIDServicePlugin](MACHOS/DualSenseHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/DualShock4HIDServicePlugin](MACHOS/DualShock4HIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/GenericGamepadHIDServicePlugin](MACHOS/GenericGamepadHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService](MACHOS/HSTouchHIDService.md)
- [/System/Library/HIDPlugins/ServicePlugins/IOHIDEventServicePlugin.plugin/IOHIDEventServicePlugin](MACHOS/IOHIDEventServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/JoyConHIDServicePlugin](MACHOS/JoyConHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/LunaHIDServicePlugin](MACHOS/LunaHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin](MACHOS/XboxOneHIDServicePlugin.md)
- [/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics](MACHOS/IOAnalytics.md)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDDisplaySessionFilter.plugin/IOHIDDisplaySessionFilter](MACHOS/IOHIDDisplaySessionFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDMotionEventSessionFilter.plugin/IOHIDMotionEventSessionFilter](MACHOS/IOHIDMotionEventSessionFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDRemoteSensorSessionFilter.plugin/IOHIDRemoteSensorSessionFilter](MACHOS/IOHIDRemoteSensorSessionFilter.md)
- [/System/Library/Health/Plugins/HealthMedicationsDaemonPluginBundle.bundle/HealthMedicationsDaemonPluginBundle](MACHOS/HealthMedicationsDaemonPluginBundle.md)
- [/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin](MACHOS/HealthRecordsPlugin.md)
- [/System/Library/Health/Plugins/HearingDaemonPlugin.bundle/HearingDaemonPlugin](MACHOS/HearingDaemonPlugin.md)
- [/System/Library/Health/Plugins/MentalHealthDaemonPlugin.bundle/MentalHealthDaemonPlugin](MACHOS/MentalHealthDaemonPlugin.md)
- [/System/Library/Health/Plugins/MobilityDaemonPlugin.bundle/MobilityDaemonPlugin](MACHOS/MobilityDaemonPlugin.md)
- [/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin](MACHOS/WorkoutHealthPlugin.md)
- [/System/Library/KerberosPlugins/GSSAPI/AppSSOReplacePlugin_iOS.bundle/AppSSOReplacePlugin_iOS](MACHOS/AppSSOReplacePlugin_iOS.md)
- [/System/Library/KerberosPlugins/KerberosFrameworkPlugins/AppSSOConfigPlugin_iOS.bundle/AppSSOConfigPlugin_iOS](MACHOS/AppSSOConfigPlugin_iOS.md)
- [/System/Library/KerberosPlugins/KerberosFrameworkPlugins/AppSSOLocatePlugin_iOS.bundle/AppSSOLocatePlugin_iOS](MACHOS/AppSSOLocatePlugin_iOS.md)
- [/System/Library/LocationBundles/CompassCalibration.bundle/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/LocationBundles/PLAMonitor.bundle/PLAMonitor](MACHOS/PLAMonitor.md)
- [/System/Library/MediaStreamPlugins/PhotoSharingPlugin.mediastream/PhotoSharingPlugin](MACHOS/PhotoSharingPlugin.md)
- [/System/Library/Messages/iMessageApps/AnimojiCameraApp.bundle/AnimojiCameraApp](MACHOS/AnimojiCameraApp.md)
- [/System/Library/Messages/iMessageApps/AudioMessagesExtension.bundle/AudioMessagesExtension](MACHOS/AudioMessagesExtension.md)
- [/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/FindMyMessagesApp](MACHOS/FindMyMessagesApp.md)
- [/System/Library/Messages/iMessageApps/FunCameraFilters.bundle/FunCameraFilters](MACHOS/FunCameraFilters.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/Messages/iMessageBalloons/HandwritingProvider.bundle/HandwritingProvider](MACHOS/HandwritingProvider.md)
- [/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin](MACHOS/MSMessageExtensionBalloonPlugin.md)
- [/System/Library/Messages/iMessageBalloons/RichLinkProvider.bundle/RichLinkProvider](MACHOS/RichLinkProvider.md)
- [/System/Library/Messages/iMessageEffects/CKConfettiEffect.bundle/CKConfettiEffect](MACHOS/CKConfettiEffect.md)
- [/System/Library/Messages/iMessageEffects/CKEchoEffect.bundle/CKEchoEffect](MACHOS/CKEchoEffect.md)
- [/System/Library/Messages/iMessageEffects/CKFireworksEffect.bundle/CKFireworksEffect](MACHOS/CKFireworksEffect.md)
- [/System/Library/Messages/iMessageEffects/CKHappyBirthdayEffect.bundle/CKHappyBirthdayEffect](MACHOS/CKHappyBirthdayEffect.md)
- [/System/Library/Messages/iMessageEffects/CKHeartEffect.bundle/CKHeartEffect](MACHOS/CKHeartEffect.md)
- [/System/Library/Messages/iMessageEffects/CKLasersEffect.bundle/CKLasersEffect](MACHOS/CKLasersEffect.md)
- [/System/Library/Messages/iMessageEffects/CKShootingStarEffect.bundle/CKShootingStarEffect](MACHOS/CKShootingStarEffect.md)
- [/System/Library/Messages/iMessageEffects/CKSparklesEffect.bundle/CKSparklesEffect](MACHOS/CKSparklesEffect.md)
- [/System/Library/Messages/iMessageEffects/CKSpotlightEffect.bundle/CKSpotlightEffect](MACHOS/CKSpotlightEffect.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeAppStoreDaemonSettings.bundle/BridgeAppStoreDaemonSettings](MACHOS/BridgeAppStoreDaemonSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeHealthSettings.bundle/BridgeHealthSettings](MACHOS/BridgeHealthSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeRemoteAccounts.bundle/BridgeRemoteAccounts](MACHOS/BridgeRemoteAccounts.md)
- [/System/Library/NanoPreferenceBundles/Applications/BrookBridgeSettings.bundle/BrookBridgeSettings](MACHOS/BrookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/DeepBreathingSettings.bundle/DeepBreathingSettings](MACHOS/DeepBreathingSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/DepthCompanionSettings.bundle/DepthCompanionSettings](MACHOS/DepthCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/DoseSettings.bundle/DoseSettings](MACHOS/DoseSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/FindMyNotificationsSettings.bundle/FindMyNotificationsSettings](MACHOS/FindMyNotificationsSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/HealthAppsSettings.bundle/HealthAppsSettings](MACHOS/HealthAppsSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/HeartRateSettings.bundle/HeartRateSettings](MACHOS/HeartRateSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/MessagesBridgeSettings.bundle/MessagesBridgeSettings](MACHOS/MessagesBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/MindSettings.bundle/MindSettings](MACHOS/MindSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoBedtimeBridgeSettings.bundle/NanoBedtimeBridgeSettings](MACHOS/NanoBedtimeBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoBooksBridgeSettings.bundle/NanoBooksBridgeSettings](MACHOS/NanoBooksBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoCalendarBridgeSettings.bundle/NanoCalendarBridgeSettings](MACHOS/NanoCalendarBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoClockBridgeSettings.bundle/NanoClockBridgeSettings](MACHOS/NanoClockBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoContactsBridgeSettingsOther.bundle/NanoContactsBridgeSettingsOther](MACHOS/NanoContactsBridgeSettingsOther.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoContactsBridgeSettingsPaired.bundle/NanoContactsBridgeSettingsPaired](MACHOS/NanoContactsBridgeSettingsPaired.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMailBridgeSettings.bundle/NanoMailBridgeSettings](MACHOS/NanoMailBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMapsBridgeSettings.bundle/NanoMapsBridgeSettings](MACHOS/NanoMapsBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMenstrualCyclesCompanionSettings.bundle/NanoMenstrualCyclesCompanionSettings](MACHOS/NanoMenstrualCyclesCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMusicBridgeSettings.bundle/NanoMusicBridgeSettings](MACHOS/NanoMusicBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPhotosBridgeSettings.bundle/NanoPhotosBridgeSettings](MACHOS/NanoPhotosBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoTipsBridgeSettings.bundle/NanoTipsBridgeSettings](MACHOS/NanoTipsBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/OxygenSaturationSettings.bundle/OxygenSaturationSettings](MACHOS/OxygenSaturationSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/PhoneBridgeSettings.bundle/PhoneBridgeSettings](MACHOS/PhoneBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/PodcastsBridgeSettings.bundle/PodcastsBridgeSettings](MACHOS/PodcastsBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/SessionTrackerAppSettings.bundle/SessionTrackerAppSettings](MACHOS/SessionTrackerAppSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/StocksBridgeSettings.bundle/StocksBridgeSettings](MACHOS/StocksBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/TinCanSettings.bundle/TinCanSettings](MACHOS/TinCanSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/WeatherExtensionBridgeSettings.bundle/WeatherExtensionBridgeSettings](MACHOS/WeatherExtensionBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Customization/CarouselAppViewSettings.bundle/CarouselAppViewSettings](MACHOS/CarouselAppViewSettings.md)
- [/System/Library/NanoPreferenceBundles/Customization/CarouselLayoutSettings.bundle/CarouselLayoutSettings](MACHOS/CarouselLayoutSettings.md)
- [/System/Library/NanoPreferenceBundles/Customization/NTKCustomization.bundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/NanoPreferenceBundles/Discover/AppsForYourWatchPlugin.bundle/AppsForYourWatchPlugin](MACHOS/AppsForYourWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/CustomizeYourWatchPlugin.bundle/CustomizeYourWatchPlugin](MACHOS/CustomizeYourWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/GetToKnowCurrentSeriesPlugin.bundle/GetToKnowCurrentSeriesPlugin](MACHOS/GetToKnowCurrentSeriesPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/HealthAndFitnessPlugin.bundle/HealthAndFitnessPlugin](MACHOS/HealthAndFitnessPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/UserGuidePlugin.bundle/UserGuidePlugin](MACHOS/UserGuidePlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/WelcomeToAppleWatchPlugin.bundle/WelcomeToAppleWatchPlugin](MACHOS/WelcomeToAppleWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/WhatsNewPlugin.bundle/WhatsNewPlugin](MACHOS/WhatsNewPlugin.md)
- [/System/Library/NanoPreferenceBundles/General/AssistantBridgeSettings.bundle/AssistantBridgeSettings](MACHOS/AssistantBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CellularBridgeSettings.bundle/CellularBridgeSettings](MACHOS/CellularBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAppBacklightPrivacySettings.bundle/CompanionAppBacklightPrivacySettings](MACHOS/CompanionAppBacklightPrivacySettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionBARSettings.bundle/CompanionBARSettings](MACHOS/CompanionBARSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionComplicationSettings.bundle/CompanionComplicationSettings](MACHOS/CompanionComplicationSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionDockSettings.bundle/CompanionDockSettings](MACHOS/CompanionDockSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionNotificationSettings.bundle/CompanionNotificationSettings](MACHOS/CompanionNotificationSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionReturnToClockSettings.bundle/CompanionReturnToClockSettings](MACHOS/CompanionReturnToClockSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionStingSettings.bundle/CompanionStingSettings](MACHOS/CompanionStingSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionWakeSettings.bundle/CompanionWakeSettings](MACHOS/CompanionWakeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/NTKCTritiumSettings.bundle/NTKCTritiumSettings](MACHOS/NTKCTritiumSettings.md)
- [/System/Library/NanoPreferenceBundles/General/PairedUnlockSettings.bundle/PairedUnlockSettings](MACHOS/PairedUnlockSettings.md)
- [/System/Library/NanoPreferenceBundles/General/WGAEltonUsersSettingsPhone.bundle/WGAEltonUsersSettingsPhone](MACHOS/WGAEltonUsersSettingsPhone.md)
- [/System/Library/NanoPreferenceBundles/PrivacySettings/HealthBridgePrivacySettings.bundle/HealthBridgePrivacySettings](MACHOS/HealthBridgePrivacySettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/AccessibilityBridgeSetup.bundle/AccessibilityBridgeSetup](MACHOS/AccessibilityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/BPSStingSetup.bundle/BPSStingSetup](MACHOS/BPSStingSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/CellularSetupBridgeBuddyUI.bundle/CellularSetupBridgeBuddyUI](MACHOS/CellularSetupBridgeBuddyUI.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/CompanionAppViewSetup.bundle/CompanionAppViewSetup](MACHOS/CompanionAppViewSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/DepthCompanionSetup.bundle/DepthCompanionSetup](MACHOS/DepthCompanionSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthBridgeSetupPlugin.bundle/HealthBridgeSetupPlugin](MACHOS/HealthBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthFeaturesBridgeSetupPlugin.bundle/HealthFeaturesBridgeSetupPlugin](MACHOS/HealthFeaturesBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HeartRateBridgePlugin.bundle/HeartRateBridgePlugin](MACHOS/HeartRateBridgePlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/MessagesPairingRegistration.bundle/MessagesPairingRegistration](MACHOS/MessagesPairingRegistration.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoContactsBridgeSetup.bundle/NanoContactsBridgeSetup](MACHOS/NanoContactsBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoPhotosBridgeSetup.bundle/NanoPhotosBridgeSetup](MACHOS/NanoPhotosBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/RespiratoryHealthSetupPlugin.bundle/RespiratoryHealthSetupPlugin](MACHOS/RespiratoryHealthSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/SchoolTimeSetup.bundle/SchoolTimeSetup](MACHOS/SchoolTimeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/SiriWatchPairingSetup.bundle/SiriWatchPairingSetup](MACHOS/SiriWatchPairingSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/TextSettingsBridgeSetup.bundle/TextSettingsBridgeSetup](MACHOS/TextSettingsBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/WGAEltonPhoneBuddyFlowPanel.bundle/WGAEltonPhoneBuddyFlowPanel](MACHOS/WGAEltonPhoneBuddyFlowPanel.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/ActivityComplicationBundleCompanion.bundle/ActivityComplicationBundleCompanion](MACHOS/ActivityComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DoseComplicationsCompanion.bundle/DoseComplicationsCompanion](MACHOS/DoseComplicationsCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/HearingDevicesComplicationContainerCompanion.bundle/HearingDevicesComplicationContainerCompanion](MACHOS/HearingDevicesComplicationContainerCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/MindComplicationBundleCompanion.bundle/MindComplicationBundleCompanion](MACHOS/MindComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKCellularConnectivityCompanionComplicationBundle.bundle/NTKCellularConnectivityCompanionComplicationBundle](MACHOS/NTKCellularConnectivityCompanionComplicationBundle.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKTimelyComplications.bundle/NTKTimelyComplications](MACHOS/NTKTimelyComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKTimerComplicationBundle.bundle/NTKTimerComplicationBundle](MACHOS/NTKTimerComplicationBundle.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCalendarComplicationsCompanion.bundle/NanoCalendarComplicationsCompanion](MACHOS/NanoCalendarComplicationsCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCameraComplication.bundle/NanoCameraComplication](MACHOS/NanoCameraComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoMapsComplications.bundle/NanoMapsComplications](MACHOS/NanoMapsComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoRemindersComplication.bundle/NanoRemindersComplication](MACHOS/NanoRemindersComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/VoiceMemosComplication.bundle/VoiceMemosComplication](MACHOS/VoiceMemosComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WorkoutComplicationBundleCompanion.bundle/WorkoutComplicationBundleCompanion](MACHOS/WorkoutComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.finddevices.complications.bundle/com.apple.finddevices.complications](MACHOS/com.apple.finddevices.complications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.finditems.complications.bundle/com.apple.finditems.complications](MACHOS/com.apple.finditems.complications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.findpeople.complications.bundle/com.apple.findpeople.complications](MACHOS/com.apple.findpeople.complications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKActivityFaceBundleCompanion.bundle/NTKActivityFaceBundleCompanion](MACHOS/NTKActivityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAkitaFaceBundleCompanion.bundle/NTKAkitaFaceBundleCompanion](MACHOS/NTKAkitaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAlaskanFaceBundleCompanion.bundle/NTKAlaskanFaceBundleCompanion](MACHOS/NTKAlaskanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBigNumeralsAnalogFaceBundleCompanion.bundle/NTKBigNumeralsAnalogFaceBundleCompanion](MACHOS/NTKBigNumeralsAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBigNumeralsDigitalFaceBundleCompanion.bundle/NTKBigNumeralsDigitalFaceBundleCompanion](MACHOS/NTKBigNumeralsDigitalFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBreatheFaceBundle.bundle/NTKBreatheFaceBundle](MACHOS/NTKBreatheFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCaliforniaFaceBundleCompanion.bundle/NTKCaliforniaFaceBundleCompanion](MACHOS/NTKCaliforniaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCharacterFaceBundleCompanion.bundle/NTKCharacterFaceBundleCompanion](MACHOS/NTKCharacterFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKChronographFaceBundleCompanion.bundle/NTKChronographFaceBundleCompanion](MACHOS/NTKChronographFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCloudrakerFaceBundleCompanion.bundle/NTKCloudrakerFaceBundleCompanion](MACHOS/NTKCloudrakerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCollieFaceBundleCompanion.bundle/NTKCollieFaceBundleCompanion](MACHOS/NTKCollieFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColorAnalogFaceBundleCompanion.bundle/NTKColorAnalogFaceBundleCompanion](MACHOS/NTKColorAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColtanFaceBundleCompanion.bundle/NTKColtanFaceBundleCompanion](MACHOS/NTKColtanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCrosswindFaceBundleCompanion.bundle/NTKCrosswindFaceBundleCompanion](MACHOS/NTKCrosswindFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKDigitalModularFaceBundleCompanion.bundle/NTKDigitalModularFaceBundleCompanion](MACHOS/NTKDigitalModularFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExplorerFaceBundleCompanion.bundle/NTKExplorerFaceBundleCompanion](MACHOS/NTKExplorerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExtraLargeFaceBundleCompanion.bundle/NTKExtraLargeFaceBundleCompanion](MACHOS/NTKExtraLargeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFireWaterFaceBundle.bundle/NTKFireWaterFaceBundle](MACHOS/NTKFireWaterFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGladiusFaceBundleCompanion.bundle/NTKGladiusFaceBundleCompanion](MACHOS/NTKGladiusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGlobetrotterFaceBundleCompanion.bundle/NTKGlobetrotterFaceBundleCompanion](MACHOS/NTKGlobetrotterFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGreyhoundFaceBundleCompanion.bundle/NTKGreyhoundFaceBundleCompanion](MACHOS/NTKGreyhoundFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographFaceBundle.bundle/NTKInfographFaceBundle](MACHOS/NTKInfographFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographModularFaceBundle.bundle/NTKInfographModularFaceBundle](MACHOS/NTKInfographModularFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKKuiperFaceBundleCompanion.bundle/NTKKuiperFaceBundleCompanion](MACHOS/NTKKuiperFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKLilypadFaceBundleCompanion.bundle/NTKLilypadFaceBundleCompanion](MACHOS/NTKLilypadFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKLiquidMetalFaceBundle.bundle/NTKLiquidMetalFaceBundle](MACHOS/NTKLiquidMetalFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMagmaFaceBundleCompanion.bundle/NTKMagmaFaceBundleCompanion](MACHOS/NTKMagmaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMargaritaFaceBundleCompanion.bundle/NTKMargaritaFaceBundleCompanion](MACHOS/NTKMargaritaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMotionFaceBundle.bundle/NTKMotionFaceBundle](MACHOS/NTKMotionFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKNumeralsAnalogFaceBundleCompanion.bundle/NTKNumeralsAnalogFaceBundleCompanion](MACHOS/NTKNumeralsAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKOlympusFaceBundleCompanion.bundle/NTKOlympusFaceBundleCompanion](MACHOS/NTKOlympusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParameciumFaceBundleCompanion.bundle/NTKParameciumFaceBundleCompanion](MACHOS/NTKParameciumFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPlumeriaFaceBundleCompanion.bundle/NTKPlumeriaFaceBundleCompanion](MACHOS/NTKPlumeriaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPrideWeaveFaceBundleCompanion.bundle/NTKPrideWeaveFaceBundleCompanion](MACHOS/NTKPrideWeaveFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKProteusFaceBundleCompanion.bundle/NTKProteusFaceBundleCompanion](MACHOS/NTKProteusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRenegadeFaceBundleCompanion.bundle/NTKRenegadeFaceBundleCompanion](MACHOS/NTKRenegadeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSeltzerFaceBundleCompanion.bundle/NTKSeltzerFaceBundleCompanion](MACHOS/NTKSeltzerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKShibaFaceBundleCompanion.bundle/NTKShibaFaceBundleCompanion](MACHOS/NTKShibaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSimpleFaceBundleCompanion.bundle/NTKSimpleFaceBundleCompanion](MACHOS/NTKSimpleFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSolarsFaceBundleCompanion.bundle/NTKSolarsFaceBundleCompanion](MACHOS/NTKSolarsFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSpectrumFaceBundleCompanion.bundle/NTKSpectrumFaceBundleCompanion](MACHOS/NTKSpectrumFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKTimelapseFaceBundle.bundle/NTKTimelapseFaceBundle](MACHOS/NTKTimelapseFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKToyStoryFaceBundle.bundle/NTKToyStoryFaceBundle](MACHOS/NTKToyStoryFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUltraCubeFaceBundleCompanion.bundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUtilityFaceBundleCompanion.bundle/NTKUtilityFaceBundleCompanion](MACHOS/NTKUtilityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVaporFaceBundle.bundle/NTKVaporFaceBundle](MACHOS/NTKVaporFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVictoryAnalogFaceBundleCompanion.bundle/NTKVictoryAnalogFaceBundleCompanion](MACHOS/NTKVictoryAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVictoryDigitalFaceBundleCompanion.bundle/NTKVictoryDigitalFaceBundleCompanion](MACHOS/NTKVictoryDigitalFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccessoryDeveloperSettings.bundle/AccessoryDeveloperSettings](MACHOS/AccessoryDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/ActiveSyncSettings.bundle/ActiveSyncSettings](MACHOS/ActiveSyncSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/CloudKitSettings.bundle/CloudKitSettings](MACHOS/CloudKitSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/DAVSettings.bundle/DAVSettings](MACHOS/DAVSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/LDAPSettings.bundle/LDAPSettings](MACHOS/LDAPSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/MailAccountSettings.bundle/MailAccountSettings](MACHOS/MailAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/RemoteManagementAccountSettings.bundle/RemoteManagementAccountSettings](MACHOS/RemoteManagementAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/SubscribedCalendarSettings.bundle/SubscribedCalendarSettings](MACHOS/SubscribedCalendarSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudCalendarSettings.bundle/icloudCalendarSettings](MACHOS/icloudCalendarSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AccountSettingsUI.bundle/AccountSettingsUI](MACHOS/AccountSettingsUI.md)
- [/System/Library/PreferenceBundles/ActionButtonSettings.bundle/ActionButtonSettings](MACHOS/ActionButtonSettings.md)
- [/System/Library/PreferenceBundles/ActivitySettings.bundle/ActivitySettings](MACHOS/ActivitySettings.md)
- [/System/Library/PreferenceBundles/AmbientSettings.bundle/AmbientSettings](MACHOS/AmbientSettings.md)
- [/System/Library/PreferenceBundles/AppClipDeveloperSettings.bundle/AppClipDeveloperSettings](MACHOS/AppClipDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/AppleEthernetSettingsPreferences.bundle/AppleEthernetSettingsPreferences](MACHOS/AppleEthernetSettingsPreferences.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/BlocklistSettings.bundle/BlocklistSettings](MACHOS/BlocklistSettings.md)
- [/System/Library/PreferenceBundles/CallDirectorySettings.bundle/CallDirectorySettings](MACHOS/CallDirectorySettings.md)
- [/System/Library/PreferenceBundles/CallForwardingTelephonySettings.bundle/CallForwardingTelephonySettings](MACHOS/CallForwardingTelephonySettings.md)
- [/System/Library/PreferenceBundles/CallScreeningSettingsBundle.bundle/CallScreeningSettingsBundle](MACHOS/CallScreeningSettingsBundle.md)
- [/System/Library/PreferenceBundles/CallWaitingTelephonySettings.bundle/CallWaitingTelephonySettings](MACHOS/CallWaitingTelephonySettings.md)
- [/System/Library/PreferenceBundles/CallingLineIdRestrictionTelephonySettings.bundle/CallingLineIdRestrictionTelephonySettings](MACHOS/CallingLineIdRestrictionTelephonySettings.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/CellularNetworkTelephonySettings.bundle/CellularNetworkTelephonySettings](MACHOS/CellularNetworkTelephonySettings.md)
- [/System/Library/PreferenceBundles/ClarityUICameraSettings.bundle/ClarityUICameraSettings](MACHOS/ClarityUICameraSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIMessagesSettings.bundle/ClarityUIMessagesSettings](MACHOS/ClarityUIMessagesSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIMusicSettings.bundle/ClarityUIMusicSettings](MACHOS/ClarityUIMusicSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIPhoneFaceTimeSettings.bundle/ClarityUIPhoneFaceTimeSettings](MACHOS/ClarityUIPhoneFaceTimeSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIPhotosSettings.bundle/ClarityUIPhotosSettings](MACHOS/ClarityUIPhotosSettings.md)
- [/System/Library/PreferenceBundles/ClassKitDeveloperSettings.bundle/ClassKitDeveloperSettings](MACHOS/ClassKitDeveloperSettings.md)
- [/System/Library/PreferenceBundles/ClassKitSettings.bundle/ClassKitSettings](MACHOS/ClassKitSettings.md)
- [/System/Library/PreferenceBundles/ClassificationAndReportingSettingsBundle.bundle/ClassificationAndReportingSettingsBundle](MACHOS/ClassificationAndReportingSettingsBundle.md)
- [/System/Library/PreferenceBundles/CommunicationSafetySettings.bundle/CommunicationSafetySettings](MACHOS/CommunicationSafetySettings.md)
- [/System/Library/PreferenceBundles/CompassSettings.bundle/CompassSettings](MACHOS/CompassSettings.md)
- [/System/Library/PreferenceBundles/ConferenceExternalSettings.bundle/ConferenceExternalSettings](MACHOS/ConferenceExternalSettings.md)
- [/System/Library/PreferenceBundles/ConferenceRegistrationSettings.bundle/ConferenceRegistrationSettings](MACHOS/ConferenceRegistrationSettings.md)
- [/System/Library/PreferenceBundles/ControlCenterSettings.bundle/ControlCenterSettings](MACHOS/ControlCenterSettings.md)
- [/System/Library/PreferenceBundles/CoreRoutineSettings.bundle/CoreRoutineSettings](MACHOS/CoreRoutineSettings.md)
- [/System/Library/PreferenceBundles/DeveloperSettings.bundle/DeveloperSettings](MACHOS/DeveloperSettings.md)
- [/System/Library/PreferenceBundles/DeviceManagementClientDeveloperSettings.bundle/DeviceManagementClientDeveloperSettings](MACHOS/DeviceManagementClientDeveloperSettings.md)
- [/System/Library/PreferenceBundles/DialAssistTelephonySettings.bundle/DialAssistTelephonySettings](MACHOS/DialAssistTelephonySettings.md)
- [/System/Library/PreferenceBundles/DictionarySettings.bundle/DictionarySettings](MACHOS/DictionarySettings.md)
- [/System/Library/PreferenceBundles/DigitalSeparationSettings.bundle/DigitalSeparationSettings](MACHOS/DigitalSeparationSettings.md)
- [/System/Library/PreferenceBundles/DriverKitSettings.bundle/DriverKitSettings](MACHOS/DriverKitSettings.md)
- [/System/Library/PreferenceBundles/ENDeveloperSettings.bundle/ENDeveloperSettings](MACHOS/ENDeveloperSettings.md)
- [/System/Library/PreferenceBundles/EmergencyAlertExtension.bundle/EmergencyAlertExtension](MACHOS/EmergencyAlertExtension.md)
- [/System/Library/PreferenceBundles/ExposureNotificationSettingsUI.bundle/ExposureNotificationSettingsUI](MACHOS/ExposureNotificationSettingsUI.md)
- [/System/Library/PreferenceBundles/FitnessSettings.bundle/FitnessSettings](MACHOS/FitnessSettings.md)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings.md)
- [/System/Library/PreferenceBundles/FontSettings.bundle/FontSettings](MACHOS/FontSettings.md)
- [/System/Library/PreferenceBundles/FreeformSettings.bundle/FreeformSettings](MACHOS/FreeformSettings.md)
- [/System/Library/PreferenceBundles/GameCenterSettings.bundle/GameCenterSettings](MACHOS/GameCenterSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/HealthRecordsSettings.bundle/HealthRecordsSettings](MACHOS/HealthRecordsSettings.md)
- [/System/Library/PreferenceBundles/HealthSettings.bundle/HealthSettings](MACHOS/HealthSettings.md)
- [/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings](MACHOS/HearingSettings.md)
- [/System/Library/PreferenceBundles/HomeScreenSettings.bundle/HomeScreenSettings](MACHOS/HomeScreenSettings.md)
- [/System/Library/PreferenceBundles/HomeSettings.bundle/HomeSettings](MACHOS/HomeSettings.md)
- [/System/Library/PreferenceBundles/ICBSettingsBundle.bundle/ICBSettingsBundle](MACHOS/ICBSettingsBundle.md)
- [/System/Library/PreferenceBundles/ICSSettingsBundle.bundle/ICSSettingsBundle](MACHOS/ICSSettingsBundle.md)
- [/System/Library/PreferenceBundles/IDSExternalSettings.bundle/IDSExternalSettings](MACHOS/IDSExternalSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MadridExternalSettings.bundle/MadridExternalSettings](MACHOS/MadridExternalSettings.md)
- [/System/Library/PreferenceBundles/ManagedConfigurationUI.bundle/ManagedConfigurationUI](MACHOS/ManagedConfigurationUI.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MeasureSettings.bundle/MeasureSettings](MACHOS/MeasureSettings.md)
- [/System/Library/PreferenceBundles/MessagesNotificationFiltering.bundle/MessagesNotificationFiltering](MACHOS/MessagesNotificationFiltering.md)
- [/System/Library/PreferenceBundles/MobileMailSettings.bundle/MobileMailSettings](MACHOS/MobileMailSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MobileSlideShowSettings.bundle/MobileSlideShowSettings](MACHOS/MobileSlideShowSettings.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/MusicSettings.bundle/MusicSettings](MACHOS/MusicSettings.md)
- [/System/Library/PreferenceBundles/NameAndPhotoSettingsBundle.bundle/NameAndPhotoSettingsBundle](MACHOS/NameAndPhotoSettingsBundle.md)
- [/System/Library/PreferenceBundles/NewsSettings.bundle/NewsSettings](MACHOS/NewsSettings.md)
- [/System/Library/PreferenceBundles/NotesSettings.bundle/NotesSettings](MACHOS/NotesSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PassbookSettings.bundle/PassbookSettings](MACHOS/PassbookSettings.md)
- [/System/Library/PreferenceBundles/PhonebookTelephonySettings.bundle/PhonebookTelephonySettings](MACHOS/PhonebookTelephonySettings.md)
- [/System/Library/PreferenceBundles/PhotosCustomNotifications.bundle/PhotosCustomNotifications](MACHOS/PhotosCustomNotifications.md)
- [/System/Library/PreferenceBundles/PictureInPictureSettings.bundle/PictureInPictureSettings](MACHOS/PictureInPictureSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/PrimaryCloudCallingSettingsBundle.bundle/PrimaryCloudCallingSettingsBundle](MACHOS/PrimaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/Privacy/ClipServicesSettings.bundle/ClipServicesSettings](MACHOS/ClipServicesSettings.md)
- [/System/Library/PreferenceBundles/Privacy/HealthPrivacySettings.bundle/HealthPrivacySettings](MACHOS/HealthPrivacySettings.md)
- [/System/Library/PreferenceBundles/Privacy/SensorKitPrivacySettings.bundle/SensorKitPrivacySettings](MACHOS/SensorKitPrivacySettings.md)
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings.md)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings.md)
- [/System/Library/PreferenceBundles/ReplyWithMessageSettings.bundle/ReplyWithMessageSettings](MACHOS/ReplyWithMessageSettings.md)
- [/System/Library/PreferenceBundles/SIMApplicationsTelephonySettings.bundle/SIMApplicationsTelephonySettings](MACHOS/SIMApplicationsTelephonySettings.md)
- [/System/Library/PreferenceBundles/SIMPasscodeTelephonySettings.bundle/SIMPasscodeTelephonySettings](MACHOS/SIMPasscodeTelephonySettings.md)
- [/System/Library/PreferenceBundles/SIMSettings.bundle/SIMSettings](MACHOS/SIMSettings.md)
- [/System/Library/PreferenceBundles/SMSPreferences.bundle/SMSPreferences](MACHOS/SMSPreferences.md)
- [/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings](MACHOS/SOSSettings.md)
- [/System/Library/PreferenceBundles/SecondaryCloudCallingSettingsBundle.bundle/SecondaryCloudCallingSettingsBundle](MACHOS/SecondaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/SecuritySettings.bundle/SecuritySettings](MACHOS/SecuritySettings.md)
- [/System/Library/PreferenceBundles/SharePlaySettings.bundle/SharePlaySettings](MACHOS/SharePlaySettings.md)
- [/System/Library/PreferenceBundles/ShortcutsSettings.bundle/ShortcutsSettings](MACHOS/ShortcutsSettings.md)
- [/System/Library/PreferenceBundles/SilenceCallsSettingBundle.bundle/SilenceCallsSettingBundle](MACHOS/SilenceCallsSettingBundle.md)
- [/System/Library/PreferenceBundles/SiriMessagesSettings.bundle/SiriMessagesSettings](MACHOS/SiriMessagesSettings.md)
- [/System/Library/PreferenceBundles/StocksSettings.bundle/StocksSettings](MACHOS/StocksSettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/HealthStoragePlugin.bundle/HealthStoragePlugin](MACHOS/HealthStoragePlugin.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PhotosStorageManagementSettings.bundle/PhotosStorageManagementSettings](MACHOS/PhotosStorageManagementSettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PodcastsUsagePlugin.bundle/PodcastsUsagePlugin](MACHOS/PodcastsUsagePlugin.md)
- [/System/Library/PreferenceBundles/StoragePlugins/UsagePlugin.bundle/UsagePlugin](MACHOS/UsagePlugin.md)
- [/System/Library/PreferenceBundles/StorageSettings.bundle/StorageSettings](MACHOS/StorageSettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/TVSettings.bundle/TVSettings](MACHOS/TVSettings.md)
- [/System/Library/PreferenceBundles/UsageSettings.bundle/UsageSettings](MACHOS/UsageSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountDeveloperSettings.bundle/VideoSubscriberAccountDeveloperSettings](MACHOS/VideoSubscriberAccountDeveloperSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountSettings.bundle/VideoSubscriberAccountSettings](MACHOS/VideoSubscriberAccountSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountTVAppDeveloperSettings.bundle/VideoSubscriberAccountTVAppDeveloperSettings](MACHOS/VideoSubscriberAccountTVAppDeveloperSettings.md)
- [/System/Library/PreferenceBundles/VoiceMemosSettings.bundle/VoiceMemosSettings](MACHOS/VoiceMemosSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceBundles/WeatherSettings.bundle/WeatherSettings](MACHOS/WeatherSettings.md)
- [/System/Library/PreferenceBundles/WiFiCallingTelephonySettings.bundle/WiFiCallingTelephonySettings](MACHOS/WiFiCallingTelephonySettings.md)
- [/System/Library/PreferenceBundles/WiFiSettings.bundle/WiFiSettings](MACHOS/WiFiSettings.md)
- [/System/Library/PreferenceBundles/iBooksSettings.bundle/iBooksSettings](MACHOS/iBooksSettings.md)
- [/System/Library/PreferenceManifestsInternal/PreferencesManifests.bundle/PreferencesManifests](MACHOS/PreferencesManifests.md)
- [/System/Library/PreferencesSyncBundles/FindMyDevicePreferencesSync.bundle/FindMyDevicePreferencesSync](MACHOS/FindMyDevicePreferencesSync.md)
- [/System/Library/PreferencesSyncBundles/NanoClockBridgeSettingsPreferencesSyncCompanion.bundle/NanoClockBridgeSettingsPreferencesSyncCompanion](MACHOS/NanoClockBridgeSettingsPreferencesSyncCompanion.md)
- [/System/Library/PreferencesSyncBundles/NanoPhonePreferencesSyncCompanion.bundle/NanoPhonePreferencesSyncCompanion](MACHOS/NanoPhonePreferencesSyncCompanion.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/AGXCompilerConnection-S2A8.framework/XPCServices/AGXCompilerService-S2A8.xpc/AGXCompilerService-S2A8](MACHOS/AGXCompilerService-S2A8.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore-S2A8.framework/PlugIns/AGXCompilerCrashLogs-S2A8.appex/AGXCompilerCrashLogs-S2A8](MACHOS/AGXCompilerCrashLogs-S2A8.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/com.apple.AVConference.Diagnostic](MACHOS/com.apple.AVConference.Diagnostic.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd](MACHOS/axassetsd.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/XPCServices/AXMediaUtilitiesService.xpc/AXMediaUtilitiesService](MACHOS/AXMediaUtilitiesService.md)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAuditCategories.bundle/AccessibilityAuditCategories](MACHOS/AccessibilityAuditCategories.md)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/Support/axauditd](MACHOS/axauditd.md)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/Support/axremoted](MACHOS/axremoted.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd](MACHOS/motiontrackingd.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/AXSettingsShortcuts.appex/AXSettingsShortcuts](MACHOS/AXSettingsShortcuts.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/com.apple.accessibility.Accessibility.HearingAidsTapToRadar.appex/com.apple.accessibility.Accessibility.HearingAidsTapToRadar](MACHOS/com.apple.accessibility.Accessibility.HearingAidsTapToRadar.md)
- [/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/XPCServices/ACCBluetoothPairingService.xpc/ACCBluetoothPairingService](MACHOS/ACCBluetoothPairingService.md)
- [/System/Library/PrivateFrameworks/AccountNotification.framework/and](MACHOS/and.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/XPCServices/com.apple.accounts.dom.xpc/com.apple.accounts.dom](MACHOS/com.apple.accounts.dom.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler](MACHOS/BundledIntentHandler.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/activityawardsd](MACHOS/activityawardsd.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd](MACHOS/activitysharingd.md)
- [/System/Library/PrivateFrameworks/AdminLite.framework/Resources/AdminLiteTool](MACHOS/AdminLiteTool.md)
- [/System/Library/PrivateFrameworks/AfibBurden.framework/PlugIns/AfibBurdenDiagnosticExtension.appex/AfibBurdenDiagnosticExtension](MACHOS/AfibBurdenDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/addaily](MACHOS/addaily.md)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/aggregated](MACHOS/aggregated.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/PlugIns/InfographPoster.appex/InfographPoster](MACHOS/InfographPoster.md)
- [/System/Library/PrivateFrameworks/AnnounceSiriExtensions.framework/PlugIns/AnnounceIntentExtension.appex/AnnounceIntentExtension](MACHOS/AnnounceIntentExtension.md)
- [/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd](MACHOS/appconduitd.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/XPCServices/AppPredictionIntentsHelperService.xpc/AppPredictionIntentsHelperService](MACHOS/AppPredictionIntentsHelperService.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon.md)
- [/System/Library/PrivateFrameworks/AppSSOKerberos.framework/PlugIns/KerberosExtension.appex/KerberosExtension](MACHOS/KerberosExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/ASDAskPermissionExtension](MACHOS/ASDAskPermissionExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDFollowUpExtension.appex/ASDFollowUpExtension](MACHOS/ASDFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDUserNotificationExtension.appex/ASDUserNotificationExtension](MACHOS/ASDUserNotificationExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/AppStoreEventServiceExtension.appex/AppStoreEventServiceExtension](MACHOS/AppStoreEventServiceExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/PlugIns/AppStoreOverlaysService.appex/AppStoreOverlaysService](MACHOS/AppStoreOverlaysService.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension](MACHOS/AAUIFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon](MACHOS/AppleCredentialManagerDaemon.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/AMDEngagementExtension.appex/AMDEngagementExtension](MACHOS/AMDEngagementExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLAppEmbedding.appex/ASLAppEmbedding](MACHOS/ASLAppEmbedding.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLArcadeRanking.appex/ASLArcadeRanking](MACHOS/ASLArcadeRanking.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLArcadeRetention.appex/ASLArcadeRetention](MACHOS/ASLArcadeRetention.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLExperimental.appex/ASLExperimental](MACHOS/ASLExperimental.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/AppStoreEvalLighthousePlugin.appex/AppStoreEvalLighthousePlugin](MACHOS/AppStoreEvalLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/CSLAppStore.appex/CSLAppStore](MACHOS/CSLAppStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/CSLAppStore2.appex/CSLAppStore2](MACHOS/CSLAppStore2.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/PlugIns/AMSFollowUpExtension.appex/AMSFollowUpExtension](MACHOS/AMSFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementNotificationsExtension.appex/AMSEngagementNotificationsExtension](MACHOS/AMSEngagementNotificationsExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementViewExtension.appex/AMSEngagementViewExtension](MACHOS/AMSEngagementViewExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSProductPageExtension.appex/AMSProductPageExtension](MACHOS/AMSProductPageExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService](MACHOS/ANECompilerService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer](MACHOS/ANEStorageMaintainer.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/XPCServices/AssetCacheLocatorService.xpc/AssetCacheLocatorService](MACHOS/AssetCacheLocatorService.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail](MACHOS/ASVAssetThumbnail.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetViewer.appex/ASVAssetViewer](MACHOS/ASVAssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/PlugIns/SiriDE.appex/SiriDE](MACHOS/SiriDE.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/DeepSyncVerification.xpc/DeepSyncVerification](MACHOS/DeepSyncVerification.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/OpportuneSpeakingModelService.xpc/OpportuneSpeakingModelService](MACHOS/OpportuneSpeakingModelService.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/com.apple.siri.acousticsignature.xpc/com.apple.siri.acousticsignature](MACHOS/com.apple.siri.acousticsignature.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/com.apple.siri.analyzer.xpc/com.apple.siri.analyzer](MACHOS/com.apple.siri.analyzer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service](MACHOS/assistant_service.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/PlugIns/AKDiagnosticExtension.appex/AKDiagnosticExtension](MACHOS/AKDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension](MACHOS/AKFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKLocationSignInAlert.appex/AKLocationSignInAlert](MACHOS/AKLocationSignInAlert.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKSecondFactorAlert.appex/AKSecondFactorAlert](MACHOS/AKSecondFactorAlert.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKSecondFactorEntryAlert.appex/AKSecondFactorEntryAlert](MACHOS/AKSecondFactorEntryAlert.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationModeUI.app/AutomationModeUI](MACHOS/AutomationModeUI.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/automationmode-writer](MACHOS/automationmode-writer.md)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/Support/avatarsd](MACHOS/avatarsd.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/XPCServices/MemojiImageRenderService.xpc/MemojiImageRenderService](MACHOS/MemojiImageRenderService.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/XPCServices/DisplayArchiveService.xpc/DisplayArchiveService](MACHOS/DisplayArchiveService.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/PlugIns/BacklightDiagnostics.appex/BacklightDiagnostics](MACHOS/BacklightDiagnostics.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/PlugIns/com.apple.BarcodeSupport.BarcodeNotificationExtension.appex/com.apple.BarcodeSupport.BarcodeNotificationExtension](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationExtension.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/PlugIns/com.apple.BarcodeSupport.BarcodeNotificationExtension2.appex/com.apple.BarcodeSupport.BarcodeNotificationExtension2](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationExtension2.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/XPCServices/com.apple.BarcodeSupport.Helper.xpc/com.apple.BarcodeSupport.Helper](MACHOS/com.apple.BarcodeSupport.Helper.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/XPCServices/com.apple.BarcodeSupport.ParsingService.xpc/com.apple.BarcodeSupport.ParsingService](MACHOS/com.apple.BarcodeSupport.ParsingService.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/com.apple.BarcodeSupport.BarcodeNotificationService](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationService.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/XPCServices/BiomeWriteService.xpc/BiomeWriteService](MACHOS/BiomeWriteService.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/PlugIns/BiomeLighthousePlugin.appex/BiomeLighthousePlugin](MACHOS/BiomeLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed](MACHOS/biomed.md)
- [/System/Library/PrivateFrameworks/BiometricKit.framework/PlugIns/BioLogDiagnostic.appex/BioLogDiagnostic](MACHOS/BioLogDiagnostic.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BookLibrary.framework/PlugIns/BooksDiagnosticExtension.appex/BooksDiagnosticExtension](MACHOS/BooksDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/PlugIns/BooksAskPermissionExtension.appex/BooksAskPermissionExtension](MACHOS/BooksAskPermissionExtension.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd](MACHOS/bookassetd.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/XPCServices/BrailleTranslationService.xpc/BrailleTranslationService](MACHOS/BrailleTranslationService.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension](MACHOS/CMCaptureDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/Support/calaccessd](MACHOS/calaccessd.md)
- [/System/Library/PrivateFrameworks/CalendarNotification.framework/PlugIns/CalendarNotificationContentExtension.appex/CalendarNotificationContentExtension](MACHOS/CalendarNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/PlugIns/IntentsExtension.appex/IntentsExtension](MACHOS/IntentsExtension.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/Support/nebulad](MACHOS/nebulad.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/PlugIns/CarPlayDiagnostics.appex/CarPlayDiagnostics](MACHOS/CarPlayDiagnostics.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService](MACHOS/SetStoreUpdateService.md)
- [/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService](MACHOS/CategoriesService.md)
- [/System/Library/PrivateFrameworks/CertUI.framework/certui_relay](MACHOS/certui_relay.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/companionmessagesd](MACHOS/companionmessagesd.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod](MACHOS/chronod.md)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/PlugIns/PrivacyDisclosure.appex/PrivacyDisclosure](MACHOS/PrivacyDisclosure.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Extensions/EasyMAIDSignInPicker.appex/EasyMAIDSignInPicker](MACHOS/EasyMAIDSignInPicker.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/BooksService.xpc/BooksService](MACHOS/BooksService.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/ScreenshotService.xpc/ScreenshotService](MACHOS/ScreenshotService.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/clipserviced](MACHOS/clipserviced.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/PlugIns/ClockPosterExtension.appex/ClockPosterExtension](MACHOS/ClockPosterExtension.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProvider.appex/com.apple.CloudDocs.MobileDocumentsFileProvider](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.appex/com.apple.CloudDocs.MobileDocumentsFileProviderManaged](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderUI.appex/com.apple.CloudDocs.MobileDocumentsFileProviderUI](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderUI.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider](MACHOS/com.apple.CloudDocs.iCloudDriveFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged](MACHOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic](MACHOS/CloudDocsDiagnostic.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/bird](MACHOS/bird.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.DocumentPicker.appex/com.apple.CloudDocsUI.DocumentPicker](MACHOS/com.apple.CloudDocsUI.DocumentPicker.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd](MACHOS/com.apple.sbd.md)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/Versions/A/XPCServices/com.apple.cloudsettings.gamecontroller.xpc/com.apple.cloudsettings.gamecontroller](MACHOS/com.apple.cloudsettings.gamecontroller.md)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/XPCServices/com.apple.cloudsettings.international.xpc/com.apple.cloudsettings.international](MACHOS/com.apple.cloudsettings.international.md)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/XPCServices/com.apple.cloudsettings.keyboard.xpc/com.apple.cloudsettings.keyboard](MACHOS/com.apple.cloudsettings.keyboard.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad](MACHOS/companioncamerad.md)
- [/System/Library/PrivateFrameworks/CompassUI.framework/XPCServices/CompassCalibration.xpc/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent](MACHOS/contactsdonationagent.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/XPCServices/ContactsBackgroundColorService.xpc/ContactsBackgroundColorService](MACHOS/ContactsBackgroundColorService.md)
- [/System/Library/PrivateFrameworks/ContextKit.framework/XPCServices/ContextService.xpc/ContextService](MACHOS/ContextService.md)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd](MACHOS/assistant_cdmd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCAppLinksIconService.xpc/ACCAppLinksIconService](MACHOS/ACCAppLinksIconService.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCCarPlayService.xpc/ACCCarPlayService](MACHOS/ACCCarPlayService.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService](MACHOS/ACCHWComponentAuthService.md)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCFeatureAudioProductService.xpc/ACCFeatureAudioProductService](MACHOS/ACCFeatureAudioProductService.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/PlugIns/BTDevicePickerUI.appex/BTDevicePickerUI](MACHOS/BTDevicePickerUI.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd](MACHOS/cdpd.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension](MACHOS/CDPFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored](MACHOS/contextstored.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech](MACHOS/com.apple.siri.embeddedspeech.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/followupd](MACHOS/followupd.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/PlugIns/FollowUpSampleExtension.appex/FollowUpSampleExtension](MACHOS/FollowUpSampleExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/PlugIns/SearchPoirotExtension.appex/SearchPoirotExtension](MACHOS/SearchPoirotExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/XPCServices/AccessoryDataFetch.xpc/AccessoryDataFetch](MACHOS/AccessoryDataFetch.md)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd](MACHOS/recentsd.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/XPCServices/CoreRepairCoreXPCService.xpc/CoreRepairCoreXPCService](MACHOS/CoreRepairCoreXPCService.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/PlugIns/RTDiagnosticExtension.appex/RTDiagnosticExtension](MACHOS/RTDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/PlugIns/com.apple.CoreSVG.thumbnail.appex/com.apple.CoreSVG.thumbnail](MACHOS/com.apple.CoreSVG.thumbnail.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/MockAVVCPlugin.bundle/MockAVVCPlugin](MACHOS/MockAVVCPlugin.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/PlugIns/CoreSpeechDiagnosticExtension.appex/CoreSpeechDiagnosticExtension](MACHOS/CoreSpeechDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/CoreSpeechXPC.xpc/CoreSpeechXPC](MACHOS/CoreSpeechXPC.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd](MACHOS/speechmodeltrainingd.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool](MACHOS/suggest_tool.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/reversetemplated](MACHOS/reversetemplated.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd](MACHOS/suggestd.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/coresymbolicationd](MACHOS/coresymbolicationd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/AccessoryTimeSync.bundle/AccessoryTimeSync](MACHOS/AccessoryTimeSync.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/CellularSource.bundle/CellularSource](MACHOS/CellularSource.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/LinkSource.bundle/LinkSource](MACHOS/LinkSource.md)
- [/System/Library/PrivateFrameworks/DASDaemon.framework/PlugIns/DuetDiagnosticExtension.appex/DuetDiagnosticExtension](MACHOS/DuetDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DASDelegate.framework/XPCServices/DASDelegateService.xpc/DASDelegateService](MACHOS/DASDelegateService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub](MACHOS/DTServiceHub.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent](MACHOS/LeakAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/PlugIns/DTODRAssetStatus.bundle/DTODRAssetStatus](MACHOS/DTODRAssetStatus.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/PlugIns/IDEDebugGaugeDataProviders.bundle/IDEDebugGaugeDataProviders](MACHOS/IDEDebugGaugeDataProviders.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/RemoteInjectionAgent](MACHOS/RemoteInjectionAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTConditionInducerSupportService.xpc/com.apple.dt.DTConditionInducerSupportService](MACHOS/com.apple.dt.DTConditionInducerSupportService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTScreenshotService.xpc/com.apple.dt.DTScreenshotService](MACHOS/com.apple.dt.DTScreenshotService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity](MACHOS/com.apple.dt.instruments.dtsecurity.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/libRemoteInjectionPayload.dylib](MACHOS/libRemoteInjectionPayload.dylib.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/liboainject.dylib](MACHOS/liboainject.dylib.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DADaemonCardDAV.bundle/DADaemonCardDAV](MACHOS/DADaemonCardDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DAIMAPNotes.framework/DADaemonIMAPNotes.bundle/DADaemonIMAPNotes](MACHOS/DADaemonIMAPNotes.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DADaemonLDAP.bundle/DADaemonLDAP](MACHOS/DADaemonLDAP.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DADaemonSubCal.bundle/DADaemonSubCal](MACHOS/DADaemonSubCal.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Support/dataaccessd](MACHOS/dataaccessd.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/XPCServices/DataDetectorsRemoteScanner.xpc/DataDetectorsRemoteScanner](MACHOS/DataDetectorsRemoteScanner.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/PlugIns/com.apple.DataDetectorsUI.ActionsExtension.appex/com.apple.DataDetectorsUI.ActionsExtension](MACHOS/com.apple.DataDetectorsUI.ActionsExtension.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/XPCServices/com.apple.datadetectors.AddToRecentsService.xpc/com.apple.datadetectors.AddToRecentsService](MACHOS/com.apple.datadetectors.AddToRecentsService.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.datamigrator.xpc/com.apple.datamigrator](MACHOS/com.apple.datamigrator.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper](MACHOS/com.apple.migrationpluginwrapper.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/datamigratorhelper.xpc/datamigratorhelper](MACHOS/datamigratorhelper.md)
- [/System/Library/PrivateFrameworks/DebugHierarchyFoundation.framework/DebugHierarchyFoundation](MACHOS/DebugHierarchyFoundation.md)
- [/System/Library/PrivateFrameworks/DebugHierarchyKit.framework/DebugHierarchyKit](MACHOS/DebugHierarchyKit.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/PlugIns/DeepThoughtPlugin.appex/DeepThoughtPlugin](MACHOS/DeepThoughtPlugin.md)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/XPCServices/IngestService.xpc/IngestService](MACHOS/IngestService.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd](MACHOS/devicecheckd.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/BTD2DPlugin.bundle/BTD2DPlugin](MACHOS/BTD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/WiFiAwareD2DPlugin.bundle/WiFiAwareD2DPlugin](MACHOS/WiFiAwareD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/WiFiD2DPlugin.bundle/WiFiD2DPlugin](MACHOS/WiFiD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AudioDiagnosticExtension.appex/AudioDiagnosticExtension](MACHOS/AudioDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothHeadset.appex/BluetoothHeadset](MACHOS/BluetoothHeadset.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension](MACHOS/ContinuousRecordingsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/HomeEnergyDiagnosticExtension.appex/HomeEnergyDiagnosticExtension](MACHOS/HomeEnergyDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IntelligentRoutingDiagnostic.appex/IntelligentRoutingDiagnostic](MACHOS/IntelligentRoutingDiagnostic.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LocationDiagnosticExtension.appex/LocationDiagnosticExtension](MACHOS/LocationDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/NearbydDiagnosticExtension.appex/NearbydDiagnosticExtension](MACHOS/NearbydDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PICSDiagnosticExtension.appex/PICSDiagnosticExtension](MACHOS/PICSDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PedestrianFenceDiagnostic.appex/PedestrianFenceDiagnostic](MACHOS/PedestrianFenceDiagnostic.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PrecisionFindingDiagnostic.appex/PrecisionFindingDiagnostic](MACHOS/PrecisionFindingDiagnostic.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ShortcutsDiagnosticExtension.appex/ShortcutsDiagnosticExtension](MACHOS/ShortcutsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/TypologyDiagnosticExtension.appex/TypologyDiagnosticExtension](MACHOS/TypologyDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.B389.appex/com.apple.DiagnosticExtensions.B389](MACHOS/com.apple.DiagnosticExtensions.B389.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.BackgroundAppRefresh.appex/com.apple.DiagnosticExtensions.BackgroundAppRefresh](MACHOS/com.apple.DiagnosticExtensions.BackgroundAppRefresh.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.BluetoothABCDE.appex/com.apple.DiagnosticExtensions.BluetoothABCDE](MACHOS/com.apple.DiagnosticExtensions.BluetoothABCDE.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Contacts.appex/com.apple.DiagnosticExtensions.Contacts](MACHOS/com.apple.DiagnosticExtensions.Contacts.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.CrashLogs.appex/com.apple.DiagnosticExtensions.CrashLogs](MACHOS/com.apple.DiagnosticExtensions.CrashLogs.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.DataAccess.appex/com.apple.DiagnosticExtensions.DataAccess](MACHOS/com.apple.DiagnosticExtensions.DataAccess.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.FaceTime.appex/com.apple.DiagnosticExtensions.FaceTime](MACHOS/com.apple.DiagnosticExtensions.FaceTime.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.HangTracer.appex/com.apple.DiagnosticExtensions.HangTracer](MACHOS/com.apple.DiagnosticExtensions.HangTracer.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Keyboard.appex/com.apple.DiagnosticExtensions.Keyboard](MACHOS/com.apple.DiagnosticExtensions.Keyboard.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.LowMemory.appex/com.apple.DiagnosticExtensions.LowMemory](MACHOS/com.apple.DiagnosticExtensions.LowMemory.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Messages.appex/com.apple.DiagnosticExtensions.Messages](MACHOS/com.apple.DiagnosticExtensions.Messages.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Panic.appex/com.apple.DiagnosticExtensions.Panic](MACHOS/com.apple.DiagnosticExtensions.Panic.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Phone.appex/com.apple.DiagnosticExtensions.Phone](MACHOS/com.apple.DiagnosticExtensions.Phone.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Sandbox.appex/com.apple.DiagnosticExtensions.Sandbox](MACHOS/com.apple.DiagnosticExtensions.Sandbox.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.StackShot.appex/com.apple.DiagnosticExtensions.StackShot](MACHOS/com.apple.DiagnosticExtensions.StackShot.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VPN.appex/com.apple.DiagnosticExtensions.VPN](MACHOS/com.apple.DiagnosticExtensions.VPN.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VisualVoiceMail.appex/com.apple.DiagnosticExtensions.VisualVoiceMail](MACHOS/com.apple.DiagnosticExtensions.VisualVoiceMail.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VoiceMemos.appex/com.apple.DiagnosticExtensions.VoiceMemos](MACHOS/com.apple.DiagnosticExtensions.VoiceMemos.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.WiFi.appex/com.apple.DiagnosticExtensions.WiFi](MACHOS/com.apple.DiagnosticExtensions.WiFi.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.tailspin.appex/com.apple.DiagnosticExtensions.tailspin](MACHOS/com.apple.DiagnosticExtensions.tailspin.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/catutil](MACHOS/catutil.md)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/XPCServices/com.apple.DictionaryServiceHelper.xpc/com.apple.DictionaryServiceHelper](MACHOS/com.apple.DictionaryServiceHelper.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/PlugIns/DKFollowUpExtension.appex/DKFollowUpExtension](MACHOS/DKFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/PlugIns/DiskSpaceDiagnosticsExtension.appex/DiskSpaceDiagnosticsExtension](MACHOS/DiskSpaceDiagnosticsExtension.md)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService](MACHOS/FilesystemMetadataSnapshotService.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/XPCServices/com.apple.siri-distributed-evaluation.xpc/com.apple.siri-distributed-evaluation](MACHOS/com.apple.siri-distributed-evaluation.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/PlugIns/DoNotDisturbIntents.appex/DoNotDisturbIntents](MACHOS/DoNotDisturbIntents.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd](MACHOS/donotdisturbd.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/PlugIns/DockKitExtension.appex/DockKitExtension](MACHOS/DockKitExtension.md)
- [/System/Library/PrivateFrameworks/DocumentCamera.framework/PlugIns/com.apple.DocumentCamera.ViewService.appex/com.apple.DocumentCamera.ViewService](MACHOS/com.apple.DocumentCamera.ViewService.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Downloads.xpc/com.apple.DocumentManagerCore.Downloads](MACHOS/com.apple.DocumentManagerCore.Downloads.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename](MACHOS/com.apple.DocumentManagerCore.Rename.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/AddTagsActionExtension.appex/AddTagsActionExtension](MACHOS/AddTagsActionExtension.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocadoIntentHandler.appex/RecentsAvocadoIntentHandler](MACHOS/RecentsAvocadoIntentHandler.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/Support/textunderstandingd](MACHOS/textunderstandingd.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/textunderstandingd](MACHOS/textunderstandingd.md)
- [/System/Library/PrivateFrameworks/DragUI.framework/Support/druid](MACHOS/druid.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/PlugIns/EmailCore.wkbundle/EmailCore](MACHOS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/Support/devicedataresetd](MACHOS/devicedataresetd.md)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/XPCServices/DeviceDataResetXPCServiceWorker.xpc/DeviceDataResetXPCServiceWorker](MACHOS/DeviceDataResetXPCServiceWorker.md)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/PlugIns/EmergencyAlertsUIExtension.appex/EmergencyAlertsUIExtension](MACHOS/EmergencyAlertsUIExtension.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/PlugIns/EmojiPosterExtension.appex/EmojiPosterExtension](MACHOS/EmojiPosterExtension.md)
- [/System/Library/PrivateFrameworks/EventKitTCCUI.framework/PlugIns/EventKitTCCFullAccessNotificationUIExtension.appex/EventKitTCCFullAccessNotificationUIExtension](MACHOS/EventKitTCCFullAccessNotificationUIExtension.md)
- [/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/PlugIns/EventMetaDataExtractorPlugin.appex/EventMetaDataExtractorPlugin](MACHOS/EventMetaDataExtractorPlugin.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DADaemonEAS.bundle/DADaemonEAS](MACHOS/DADaemonEAS.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Support/exchangesyncd](MACHOS/exchangesyncd.md)
- [/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/PlugIns/ActiveSyncOAuthService.appex/ActiveSyncOAuthService](MACHOS/ActiveSyncOAuthService.md)
- [/System/Library/PrivateFrameworks/EyeRelief.framework/Resources/eyereliefd](MACHOS/eyereliefd.md)
- [/System/Library/PrivateFrameworks/Eyedropper.framework/Support/eyedropperd](MACHOS/eyedropperd.md)
- [/System/Library/PrivateFrameworks/FMF.framework/XPCServices/FMFMapXPCService.xpc/FMFMapXPCService](MACHOS/FMFMapXPCService.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored](MACHOS/facetimemessagestored.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/PlugIns/FAFollowupExtension.appex/FAFollowupExtension](MACHOS/FAFollowupExtension.md)
- [/System/Library/PrivateFrameworks/FamilyNotification.framework/familynotificationd](MACHOS/familynotificationd.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS](MACHOS/DraftingExtension-iOS.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/AppStoreService.xpc/AppStoreService](MACHOS/AppStoreService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/FPCKService](MACHOS/FPCKService.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealth_client](MACHOS/finhealth_client.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/XPCServices/FinHealthXPCServices.xpc/FinHealthXPCServices](MACHOS/FinHealthXPCServices.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceBTDiscoveryXPCService.xpc/FindMyDeviceBTDiscoveryXPCService](MACHOS/FindMyDeviceBTDiscoveryXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEmergencyCallInfoPublisherXPCService.xpc/FindMyDeviceEmergencyCallInfoPublisherXPCService](MACHOS/FindMyDeviceEmergencyCallInfoPublisherXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/FindMyDeviceEraseXPCService](MACHOS/FindMyDeviceEraseXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService](MACHOS/FindMyDeviceHelperXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/FindMyDeviceIdentityXPCService](MACHOS/FindMyDeviceIdentityXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceUserNotificationsXPCService.xpc/FindMyDeviceUserNotificationsXPCService](MACHOS/FindMyDeviceUserNotificationsXPCService.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/fitnesscoachingd](MACHOS/fitnesscoachingd.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/PlugIns/UserNotificationExtension.appex/UserNotificationExtension](MACHOS/UserNotificationExtension.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Support/fontservicesd](MACHOS/fontservicesd.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/UserFontManager.xpc/UserFontManager](MACHOS/UserFontManager.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/UserFontServices.xpc/UserFontServices](MACHOS/UserFontServices.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/com.apple.FontServices.FontProviderLoader.xpc/com.apple.FontServices.FontProviderLoader](MACHOS/com.apple.FontServices.FontProviderLoader.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GPUToolsDiagnostics.framework/GPUToolsDiagnostics](MACHOS/GPUToolsDiagnostics.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterAuthenticateExtension.appex/GameCenterAuthenticateExtension](MACHOS/GameCenterAuthenticateExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterChallengeIssueExtension.appex/GameCenterChallengeIssueExtension](MACHOS/GameCenterChallengeIssueExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterDashboardExtension.appex/GameCenterDashboardExtension](MACHOS/GameCenterDashboardExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterTurnBasedMatchmakerExtension.appex/GameCenterTurnBasedMatchmakerExtension](MACHOS/GameCenterTurnBasedMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/XPCServices/GameControllerConfigService.xpc/GameControllerConfigService](MACHOS/GameControllerConfigService.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond](MACHOS/revisiond.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd](MACHOS/geoanalyticsd.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/MapsOfflineService.bundle/MapsOfflineService](MACHOS/MapsOfflineService.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/XPCServices/com.apple.GeoServices.MapsOfflineServices.xpc/com.apple.GeoServices.MapsOfflineServices](MACHOS/com.apple.GeoServices.MapsOfflineServices.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/geod](MACHOS/geod.md)
- [/System/Library/PrivateFrameworks/GradientPoster.framework/PlugIns/GradientPosterExtension.appex/GradientPosterExtension](MACHOS/GradientPosterExtension.md)
- [/System/Library/PrivateFrameworks/HAENotifications.framework/PlugIns/HAENotificationContentExtension.appex/HAENotificationContentExtension](MACHOS/HAENotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/XPCServices/HRTFEnrollmentService.xpc/HRTFEnrollmentService](MACHOS/HRTFEnrollmentService.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/PlugIns/CycleTrackingDiagnosticExtension.appex/CycleTrackingDiagnosticExtension](MACHOS/CycleTrackingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/DayStreamProcessorService.xpc/DayStreamProcessorService](MACHOS/DayStreamProcessorService.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/HistoricalAnalyzerService.xpc/HistoricalAnalyzerService](MACHOS/HistoricalAnalyzerService.md)
- [/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex/HealthFollowUpExtension](MACHOS/HealthFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/PlugIns/HealthMedicationsNotificationContentExtension.appex/HealthMedicationsNotificationContentExtension](MACHOS/HealthMedicationsNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesUI.framework/PlugIns/HealthMenstrualCyclesNotificationContentExtension.appex/HealthMenstrualCyclesNotificationContentExtension](MACHOS/HealthMenstrualCyclesNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.legacy-ingestion.xpc/com.apple.health.records.legacy-ingestion](MACHOS/com.apple.health.records.legacy-ingestion.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.xpc/com.apple.health.records](MACHOS/com.apple.health.records.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/healthrecordsd](MACHOS/healthrecordsd.md)
- [/System/Library/PrivateFrameworks/HearingCore.framework/heard](MACHOS/heard.md)
- [/System/Library/PrivateFrameworks/HearingMLHelper.framework/XPCServices/HearingMLHelperService.xpc/HearingMLHelperService](MACHOS/HearingMLHelperService.md)
- [/System/Library/PrivateFrameworks/HeartRhythmAlgorithms.framework/PlugIns/IRNDiagnosticExtension.appex/IRNDiagnosticExtension](MACHOS/IRNDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd](MACHOS/homeenergyd.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed](MACHOS/homed.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iapd](MACHOS/iapd.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iaptransportd](MACHOS/iaptransportd.md)
- [/System/Library/PrivateFrameworks/IAPAuthentication.framework/Support/iapauthd](MACHOS/iapauthd.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSCredentialsAgent.app/IDSCredentialsAgent](MACHOS/IDSCredentialsAgent.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSRemoteURLConnectionAgent.app/IDSRemoteURLConnectionAgent](MACHOS/IDSRemoteURLConnectionAgent.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent](MACHOS/IMDMessageServicesAgent.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMAutomaticHistoryDeletionAgent.app/IMAutomaticHistoryDeletionAgent](MACHOS/IMAutomaticHistoryDeletionAgent.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent](MACHOS/IMDPersistenceAgent.md)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent](MACHOS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent](MACHOS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/PlugIns/WetNotification.appex/WetNotification](MACHOS/WetNotification.md)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/Resources/IOSADiagnose](MACHOS/IOSADiagnose.md)
- [/System/Library/PrivateFrameworks/InAppMessages.framework/PlugIns/InAppMessagesWebProcessBundle.bundle/InAppMessagesWebProcessBundle](MACHOS/InAppMessagesWebProcessBundle.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordination_proxy](MACHOS/installcoordination_proxy.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/ERMLRuntimePlugin.appex/ERMLRuntimePlugin](MACHOS/ERMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/Support/localizationswitcherd](MACHOS/localizationswitcherd.md)
- [/System/Library/PrivateFrameworks/LighthouseAV.framework/PlugIns/LighthouseAVPlugin.appex/LighthouseAVPlugin](MACHOS/LighthouseAVPlugin.md)
- [/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/PlugIns/LighthouseBitacoraPlugin.appex/LighthouseBitacoraPlugin](MACHOS/LighthouseBitacoraPlugin.md)
- [/System/Library/PrivateFrameworks/LighthouseDictation.framework/PlugIns/LighthouseDictationPlugin.appex/LighthouseDictationPlugin](MACHOS/LighthouseDictationPlugin.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/XPCServices/MFAANetwork.xpc/MFAANetwork](MACHOS/MFAANetwork.md)
- [/System/Library/PrivateFrameworks/MLCompilerServices.framework/XPCServices/MLCompilerOSXPC.xpc/MLCompilerOSXPC](MACHOS/MLCompilerOSXPC.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/PlugIns/MacinTalkAUSP.appex/MacinTalkAUSP](MACHOS/MacinTalkAUSP.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension](MACHOS/ManagedSettingsExtension.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd](MACHOS/destinationd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/geocorrectiond](MACHOS/geocorrectiond.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd](MACHOS/mapspushd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/nanomapscd](MACHOS/nanomapscd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MarkupUI.framework/PlugIns/MarkupPrivateExtension.appex/MarkupPrivateExtension](MACHOS/MarkupPrivateExtension.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService](MACHOS/com.apple.photos.ImageConversionService.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService](MACHOS/com.apple.photos.VideoConversionService.md)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/XPCServices/mediamlxpc.xpc/mediamlxpc](MACHOS/mediamlxpc.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/Support/mediaartworkd](MACHOS/mediaartworkd.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd](MACHOS/mstreamd.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/XPCServices/MetricMeasurementHelper.xpc/MetricMeasurementHelper](MACHOS/MetricMeasurementHelper.md)
- [/System/Library/PrivateFrameworks/MetricsKit.framework/XPCServices/AMPIDService.xpc/AMPIDService](MACHOS/AMPIDService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/auearlyboot](MACHOS/auearlyboot.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleEmbeddedAccessoryUpdaterService.xpc/AppleEmbeddedAccessoryUpdaterService](MACHOS/AppleEmbeddedAccessoryUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleSTDP2700BootstrapService.xpc/AppleSTDP2700BootstrapService](MACHOS/AppleSTDP2700BootstrapService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/DurianUpdaterService.xpc/DurianUpdaterService](MACHOS/DurianUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/GenericKextUpdaterService.xpc/GenericKextUpdaterService](MACHOS/GenericKextUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/StandaloneHIDAudService.xpc/StandaloneHIDAudService](MACHOS/StandaloneHIDAudService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceAFU.xpc/UARPUpdaterServiceAFU](MACHOS/UARPUpdaterServiceAFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/USBCAccessoryUpdaterService.xpc/USBCAccessoryUpdaterService](MACHOS/USBCAccessoryUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBDiagnosticExtension.appex/MBDiagnosticExtension](MACHOS/MBDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBFollowUpExtension.appex/MBFollowUpExtension](MACHOS/MBFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension](MACHOS/MBPrebuddyFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService](MACHOS/com.apple.MobileInstallationHelperService.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/PlugIns/MailWebProcessBundle.bundle/MailWebProcessBundle](MACHOS/MailWebProcessBundle.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated](MACHOS/softwareupdated.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd](MACHOS/mobiletimerd.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/PlugIns/MobileTimerIntents.appex/MobileTimerIntents](MACHOS/MobileTimerIntents.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/PlugIns/MobileTimerNotificationExtension.appex/MobileTimerNotificationExtension](MACHOS/MobileTimerNotificationExtension.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterPreferenceProvider.xpc/SessionFilterPreferenceProvider](MACHOS/SessionFilterPreferenceProvider.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterRecordingUpdater.xpc/SessionFilterRecordingUpdater](MACHOS/SessionFilterRecordingUpdater.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd](MACHOS/medialibraryd.md)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/PlugIns/NLPLearnerQuickTypeLighthousePlugin.appex/NLPLearnerQuickTypeLighthousePlugin](MACHOS/NLPLearnerQuickTypeLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/PlugIns/NPTCellularDiagnosticsExtension.appex/NPTCellularDiagnosticsExtension](MACHOS/NPTCellularDiagnosticsExtension.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/PlugIns/NPTWiFiDiagnosticsExtension.appex/NPTWiFiDiagnosticsExtension](MACHOS/NPTWiFiDiagnosticsExtension.md)
- [/System/Library/PrivateFrameworks/NanoAppRegistry.framework/Support/nanoappregistryd](MACHOS/nanoappregistryd.md)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/nanobackupd](MACHOS/nanobackupd.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/companionfindlocallyd](MACHOS/companionfindlocallyd.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/findme](MACHOS/findme.md)
- [/System/Library/PrivateFrameworks/NanoMusicSync.framework/PlugIns/NanoMediaDiagnosticExtension.appex/NanoMediaDiagnosticExtension](MACHOS/NanoMediaDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent](MACHOS/NPKCompanionAgent.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd](MACHOS/nanoprefsyncd.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/NTKDiagnosticExtensionCompanion.appex/NTKDiagnosticExtensionCompanion](MACHOS/NTKDiagnosticExtensionCompanion.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/com.apple.NanoTimeKit.CreateWatchFace.appex/com.apple.NanoTimeKit.CreateWatchFace](MACHOS/com.apple.NanoTimeKit.CreateWatchFace.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/BundleComplicationMigrationService.xpc/BundleComplicationMigrationService](MACHOS/BundleComplicationMigrationService.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/GreenfieldService-Companion.xpc/GreenfieldService-Companion](MACHOS/GreenfieldService-Companion.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/NTKFaceSnapshotService.xpc/NTKFaceSnapshotService](MACHOS/NTKFaceSnapshotService.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond](MACHOS/nanotimekitcompaniond.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRadioPowerSwitch.xpc/NFRadioPowerSwitch](MACHOS/NFRadioPowerSwitch.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRestoreService.xpc/NFRestoreService](MACHOS/NFRestoreService.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService](MACHOS/NFUIService.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NetworkQualityServices.framework/XPCServices/NetworkQualityXPC.xpc/NetworkQualityXPC](MACHOS/NetworkQualityXPC.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/PlugIns/NRDiagnosticExtension.appex/NRDiagnosticExtension](MACHOS/NRDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/XPCServices/ANFDecoder.xpc/ANFDecoder](MACHOS/ANFDecoder.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/PlugIns/NewsArticleViewer.appex/NewsArticleViewer](MACHOS/NewsArticleViewer.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/nanonewscd](MACHOS/nanonewscd.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/TodayFeedConfigDecoder.xpc/TodayFeedConfigDecoder](MACHOS/TodayFeedConfigDecoder.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/XPCServices/com.apple.mobilenotes.datastore.xpc/com.apple.mobilenotes.datastore](MACHOS/com.apple.mobilenotes.datastore.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/XPCServices/com.apple.mobilenotes.HTMLConverter.xpc/com.apple.mobilenotes.HTMLConverter](MACHOS/com.apple.mobilenotes.HTMLConverter.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/XPCServices/com.apple.mobilenotes.NotesImporter.xpc/com.apple.mobilenotes.NotesImporter](MACHOS/com.apple.mobilenotes.NotesImporter.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/PlugIns/IPSExtension.appex/IPSExtension](MACHOS/IPSExtension.md)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/PlugIns/OfficeSpotlightImporter.appex/OfficeSpotlightImporter](MACHOS/OfficeSpotlightImporter.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PlugIns/BridgeIntents.appex/BridgeIntents](MACHOS/BridgeIntents.md)
- [/System/Library/PrivateFrameworks/PairedSync.framework/Support/pairedsyncd](MACHOS/pairedsyncd.md)
- [/System/Library/PrivateFrameworks/PairedUnlock.framework/pairedunlockd](MACHOS/pairedunlockd.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/XPCServices/com.apple.Bridge.ppNotifierService.xpc/com.apple.Bridge.ppNotifierService](MACHOS/com.apple.Bridge.ppNotifierService.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/XPCServices/SBRendererService.xpc/SBRendererService](MACHOS/SBRendererService.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PlugIns/MarkupPhotoEditingExtension.appex/MarkupPhotoEditingExtension](MACHOS/MarkupPhotoEditingExtension.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/XPCServices/PassKitCoreXPCService.xpc/PassKitCoreXPCService](MACHOS/PassKitCoreXPCService.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/PassKitServices.framework/XPCServices/PassKitServicesXPCService.xpc/PassKitServicesXPCService](MACHOS/PassKitServicesXPCService.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Support/pasted](MACHOS/pasted.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/XPCServices/PerfPowerTelemetryReaderService.xpc/PerfPowerTelemetryReaderService](MACHOS/PerfPowerTelemetryReaderService.md)
- [/System/Library/PrivateFrameworks/PerformanceTrace.framework/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/com.apple.PerformanceTrace.PerformanceTraceService](MACHOS/com.apple.PerformanceTrace.PerformanceTraceService.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PlugIns/PhotoAnalysisLighthousePlugin.appex/PhotoAnalysisLighthousePlugin](MACHOS/PhotoAnalysisLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd](MACHOS/photoanalysisd.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosDiagnostics.appex/PhotosDiagnostics](MACHOS/PhotosDiagnostics.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider.md)
- [/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon](MACHOS/PlugInKitDaemon.md)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/Support/pointeruid](MACHOS/pointeruid.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/com.apple.PowerlogCore.diagnosticextension.appex/com.apple.PowerlogCore.diagnosticextension](MACHOS/com.apple.PowerlogCore.diagnosticextension.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PPSFeatureFlagReader.xpc/PPSFeatureFlagReader](MACHOS/PPSFeatureFlagReader.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader](MACHOS/PerfPowerServicesSignpostReader.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/rbdcConverter.xpc/rbdcConverter](MACHOS/rbdcConverter.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool](MACHOS/com.apple.PrintKit.PrinterTool.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/printbandservice.xpc/printbandservice](MACHOS/printbandservice.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd](MACHOS/privacyaccountingd.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin](MACHOS/DPMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB](MACHOS/DPMLRuntimePluginClassB.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU](MACHOS/DPMLRuntimePluginNonDnU.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/PlugIns/ProactiveShareSheetDataHarvestingLighthousePlugin.appex/ProactiveShareSheetDataHarvestingLighthousePlugin](MACHOS/ProactiveShareSheetDataHarvestingLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/XPCServices/ProfileValidatedAppIdentityService.xpc/ProfileValidatedAppIdentityService](MACHOS/ProfileValidatedAppIdentityService.md)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PlugIns/SearchResultsExtension.appex/SearchResultsExtension](MACHOS/SearchResultsExtension.md)
- [/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PlugIns/PromotedContentWebProcessBundle.bundle/PromotedContentWebProcessBundle](MACHOS/PromotedContentWebProcessBundle.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/prototyped](MACHOS/prototyped.md)
- [/System/Library/PrivateFrameworks/Quagga.framework/XPCServices/com.apple.Quagga.Decode.xpc/com.apple.Quagga.Decode](MACHOS/com.apple.Quagga.Decode.md)
- [/System/Library/PrivateFrameworks/RTTUI.framework/PlugIns/RTTNotificationContentExtension.appex/RTTNotificationContentExtension](MACHOS/RTTNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/PlugIns/RemindersNotificationContentExtension.appex/RemindersNotificationContentExtension](MACHOS/RemindersNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent](MACHOS/RemoteManagementAgent.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ASConfigurationSubscriber.xpc/ASConfigurationSubscriber](MACHOS/ASConfigurationSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber](MACHOS/AccountSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/InteractiveLegacyProfilesSubscriber.xpc/InteractiveLegacyProfilesSubscriber](MACHOS/InteractiveLegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/LegacyProfilesSubscriber.xpc/LegacyProfilesSubscriber](MACHOS/LegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/MDMAppSubscriber.xpc/MDMAppSubscriber](MACHOS/MDMAppSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber](MACHOS/ManagedAppsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagementTestSubscriber.xpc/ManagementTestSubscriber](MACHOS/ManagementTestSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PasscodeSettingsSubscriber.xpc/PasscodeSettingsSubscriber](MACHOS/PasscodeSettingsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PowerSubscriber.xpc/PowerSubscriber](MACHOS/PowerSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SecuritySubscriber.xpc/SecuritySubscriber](MACHOS/SecuritySubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber](MACHOS/SoftwareUpdateSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/WatchEnrollmentSubscriber.xpc/WatchEnrollmentSubscriber](MACHOS/WatchEnrollmentSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd](MACHOS/remotemanagementd.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/rmdinspect](MACHOS/rmdinspect.md)
- [/System/Library/PrivateFrameworks/RemoteMediaServices.framework/remotemediaservicesd](MACHOS/remotemediaservicesd.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/CoreGlyphsPrivate.bundle/CoreGlyphsPrivate](MACHOS/CoreGlyphsPrivate.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/PlugIns/com.apple.SMBClientProvider.FileProvider.appex/com.apple.SMBClientProvider.FileProvider](MACHOS/com.apple.SMBClientProvider.FileProvider.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientTool](MACHOS/smbclientTool.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd](MACHOS/smbclientd.md)
- [/System/Library/PrivateFrameworks/SOS.framework/sosd](MACHOS/sosd.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper](MACHOS/STSXPCHelper.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/AutoFillHelper.xpc/AutoFillHelper](MACHOS/AutoFillHelper.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/CredentialProviderExtensionHelper.xpc/CredentialProviderExtensionHelper](MACHOS/CredentialProviderExtensionHelper.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/com.apple.Safari.SafeBrowsing.Service](MACHOS/com.apple.Safari.SafeBrowsing.Service.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper](MACHOS/com.apple.Safari.SearchHelper.md)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/Support/schooltimed](MACHOS/schooltimed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/PlugIns/ScreenTimeNotificationContentExtension.appex/ScreenTimeNotificationContentExtension](MACHOS/ScreenTimeNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SensorKitHelper.framework/XPCServices/com.apple.SensorKit.SKMediaEventsHelper.xpc/com.apple.SensorKit.SKMediaEventsHelper](MACHOS/com.apple.SensorKit.SKMediaEventsHelper.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd](MACHOS/liveactivitiesd.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/budd](MACHOS/budd.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourEngagementExtension.appex/SeymourEngagementExtension](MACHOS/SeymourEngagementExtension.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourNotifications.appex/SeymourNotifications](MACHOS/SeymourNotifications.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/diagnosticextension.appex/diagnosticextension](MACHOS/diagnosticextension.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored](MACHOS/fitcored.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcoresessiond](MACHOS/fitcoresessiond.md)
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/Support/swcutil](MACHOS/swcutil.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropAlertUI.appex/AirDropAlertUI](MACHOS/AirDropAlertUI.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropNotice.appex/AirDropNotice](MACHOS/AirDropNotice.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/ContinuityRemote.appex/ContinuityRemote](MACHOS/ContinuityRemote.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService.md)
- [/System/Library/PrivateFrameworks/SharingXPCServices.framework/XPCServices/SharingXPCHelper.xpc/SharingXPCHelper](MACHOS/SharingXPCHelper.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/PlugIns/SiriCoreMetricsPlugin.appex/SiriCoreMetricsPlugin](MACHOS/SiriCoreMetricsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/PlugIns/SiriGeoIntentExtension.appex/SiriGeoIntentExtension](MACHOS/SiriGeoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/PlugIns/IdentityIntentExtension.appex/IdentityIntentExtension](MACHOS/IdentityIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced](MACHOS/siriinferenced.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/PlugIns/SiriInferredHelpfulnessPlugin.appex/SiriInferredHelpfulnessPlugin](MACHOS/SiriInferredHelpfulnessPlugin.md)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/PlugIns/SiriInvocationAnalyticsPlugin.appex/SiriInvocationAnalyticsPlugin](MACHOS/SiriInvocationAnalyticsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/PlugIns/THKOnDemandPlugin.appex/THKOnDemandPlugin](MACHOS/THKOnDemandPlugin.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningPlatformPlugin.appex/SiriUserFeedbackLearningPlatformPlugin](MACHOS/SiriUserFeedbackLearningPlatformPlugin.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/PlugIns/SettingsIntentExtension.appex/SettingsIntentExtension](MACHOS/SettingsIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/PlugIns/MusicAppSelectionPFLPlugin.appex/MusicAppSelectionPFLPlugin](MACHOS/MusicAppSelectionPFLPlugin.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/com.apple.SiriTTSService.TrialProxy](MACHOS/com.apple.SiriTTSService.TrialProxy.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTraining](MACHOS/SiriTTSTraining.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent](MACHOS/SiriTTSTrainingAgent.md)
- [/System/Library/PrivateFrameworks/SiriTasksEvaluation.framework/PlugIns/SiriTasksEvaluationPlugin.appex/SiriTasksEvaluationPlugin](MACHOS/SiriTasksEvaluationPlugin.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/PlugIns/AlarmIntentsExtension.appex/AlarmIntentsExtension](MACHOS/AlarmIntentsExtension.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/PlugIns/TimerIntentsExtension.appex/TimerIntentsExtension](MACHOS/TimerIntentsExtension.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/PlugIns/SiriUserSegmentsPlugin.appex/SiriUserSegmentsPlugin](MACHOS/SiriUserSegmentsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension](MACHOS/VideoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd](MACHOS/sleepd.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/PlugIns/SleepNotificationContentExtension.appex/SleepNotificationContentExtension](MACHOS/SleepNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusMagazineProducer.opplugin/OpusMagazineProducer](MACHOS/OpusMagazineProducer.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusNewClassicProducer.opplugin/OpusNewClassicProducer](MACHOS/OpusNewClassicProducer.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusOrigamiProducer.opplugin/OpusOrigamiProducer](MACHOS/OpusOrigamiProducer.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/PlugIns/SmartRepliesMLRuntimePlugin.appex/SmartRepliesMLRuntimePlugin](MACHOS/SmartRepliesMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/sociallayerd.app/sociallayerd](MACHOS/sociallayerd.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/Support/subridged](MACHOS/subridged.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUFollowUpRollbackDetectedExtension.appex/SUFollowUpRollbackDetectedExtension](MACHOS/SUFollowUpRollbackDetectedExtension.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUSFollowUpExtension.appex/SUSFollowUpExtension](MACHOS/SUSFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd](MACHOS/softwareupdateservicesd.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics.md)
- [/System/Library/PrivateFrameworks/SoundDetectionNotificationExtension.appex/SoundDetectionNotificationExtension](MACHOS/SoundDetectionNotificationExtension.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/PlugIns/SoundScapesViewServices.appex/SoundScapesViewServices](MACHOS/SoundScapesViewServices.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd](MACHOS/com.apple.SpeechRecognitionCore.brokerd.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent](MACHOS/StatusKitAgent.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/XPCServices/storagekitfsrunner.xpc/storagekitfsrunner](MACHOS/storagekitfsrunner.md)
- [/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/Support/storebookkeeperd](MACHOS/storebookkeeperd.md)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.privileged.xpc/STExtractionService.privileged](MACHOS/STExtractionService.privileged.md)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.xpc/STExtractionService](MACHOS/STExtractionService.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.privileged.xpc/com.apple.StreamingUnzipService.privileged](MACHOS/com.apple.StreamingUnzipService.privileged.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService](MACHOS/com.apple.StreamingUnzipService.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Support/contentlinkingd](MACHOS/contentlinkingd.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd](MACHOS/syncdefaultsd.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd](MACHOS/systemstatusd.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TailspinSymbolication.framework/XPCServices/TailspinSymbolicationServer.xpc/TailspinSymbolicationServer](MACHOS/TailspinSymbolicationServer.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FaceTime.FTConversationService.xpc/com.apple.FaceTime.FTConversationService](MACHOS/com.apple.FaceTime.FTConversationService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/XPCServices/TextInputTestService.xpc/TextInputTestService](MACHOS/TextInputTestService.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/PlugIns/SiriAUSP.appex/SiriAUSP](MACHOS/SiriAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/PlugIns/KonaSynthesizer.appex/KonaSynthesizer](MACHOS/KonaSynthesizer.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/PlugIns/MauiAUSP.appex/MauiAUSP](MACHOS/MauiAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/PlugIns/VoiceBankingDiagnostics.appex/VoiceBankingDiagnostics](MACHOS/VoiceBankingDiagnostics.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd.md)
- [/System/Library/PrivateFrameworks/ToneLibrary.framework/XPCServices/com.apple.tonelibraryd.xpc/com.apple.tonelibraryd](MACHOS/com.apple.tonelibraryd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/PlugIns/TransparencyFollowUpExtension.appex/TransparencyFollowUpExtension](MACHOS/TransparencyFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/XPCServices/TrialArchivingService.xpc/TrialArchivingService](MACHOS/TrialArchivingService.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/XPCServices/com.apple.uifoundation-bundle-helper.xpc/com.apple.uifoundation-bundle-helper](MACHOS/com.apple.uifoundation-bundle-helper.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/XPCServices/nsattributedstringagent.xpc/nsattributedstringagent](MACHOS/nsattributedstringagent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/PlugIns/UIUnderstanding.diagnosticextension.appex/UIUnderstanding.diagnosticextension](MACHOS/UIUnderstanding.diagnosticextension.md)
- [/System/Library/PrivateFrameworks/USDLib_FormatLoaderProxy.framework/XPCServices/USDLib_FormatLoader.xpc/USDLib_FormatLoader](MACHOS/USDLib_FormatLoader.md)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService](MACHOS/UVFSService.md)
- [/System/Library/PrivateFrameworks/UnityPoster.framework/PlugIns/UnityPosterExtension.appex/UnityPosterExtension](MACHOS/UnityPosterExtension.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/PlugIns/UASharedPasteboardiOSUI.appex/UASharedPasteboardiOSUI](MACHOS/UASharedPasteboardiOSUI.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/userfs_provider.appex/userfs_provider](MACHOS/userfs_provider.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/userfs_helper](MACHOS/userfs_helper.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/userfsd](MACHOS/userfsd.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd](MACHOS/usernotificationsd.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/PlugIns/UserNotificationsUIDefaultExtension.appex/UserNotificationsUIDefaultExtension](MACHOS/UserNotificationsUIDefaultExtension.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/PlugIns/UserNotificationsUIThumbnailProvider.appex/UserNotificationsUIThumbnailProvider](MACHOS/UserNotificationsUIThumbnailProvider.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/mapinspectord](MACHOS/mapinspectord.md)
- [/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit](MACHOS/VisualTestKit.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/Support/voicememod](MACHOS/voicememod.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/PlugIns/VoiceServicesDiagnosticextension.appex/VoiceServicesDiagnosticextension](MACHOS/VoiceServicesDiagnosticextension.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/voiced](MACHOS/voiced.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd](MACHOS/siriactionsd.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/PlugIns/CollectionsPoster.appex/CollectionsPoster](MACHOS/CollectionsPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd](MACHOS/watchlistd.md)
- [/System/Library/PrivateFrameworks/Weather.framework/Support/nanoweatherprefsd](MACHOS/nanoweatherprefsd.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd](MACHOS/webprivacyd.md)
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/matd](MACHOS/matd.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/PlugIns/WiFiPickerExtension.appex/WiFiPickerExtension](MACHOS/WiFiPickerExtension.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/ThreeBarsXPCService.xpc/ThreeBarsXPCService](MACHOS/ThreeBarsXPCService.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService](MACHOS/WiFiCloudAssetsXPCService.md)
- [/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/PlugIns/AWDDiagnosticExtension.appex/AWDDiagnosticExtension](MACHOS/AWDDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents](MACHOS/ShortcutsIntents.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension](MACHOS/AddShortcutExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/CatalystContentExtension.appex/CatalystContentExtension](MACHOS/CatalystContentExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/XPCServices/WorkoutKitXPCService.xpc/WorkoutKitXPCService](MACHOS/WorkoutKitXPCService.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService](MACHOS/ZhuGeService.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/ContainerMetadataExtractor](MACHOS/ContainerMetadataExtractor.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/TelemetryDiskChecker.xpc/TelemetryDiskChecker](MACHOS/TelemetryDiskChecker.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup](MACHOS/ICQFollowup.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/PlugIns/ICQEngagementExtension.appex/ICQEngagementExtension](MACHOS/ICQEngagementExtension.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerCore.framework/PlugIns/PFLPlugin.appex/PFLPlugin](MACHOS/PFLPlugin.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd](MACHOS/icloudsubscriptionoptimizerd.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/PlugIns/LighthousePlugin.appex/LighthousePlugin](MACHOS/LighthousePlugin.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/XPCServices/com.apple.DiagnosticsSessionAvailibility.xpc/com.apple.DiagnosticsSessionAvailibility](MACHOS/com.apple.DiagnosticsSessionAvailibility.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd](MACHOS/iosdiagnosticsd.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/XPCServices/SharedListeningConnectionService.xpc/SharedListeningConnectionService](MACHOS/SharedListeningConnectionService.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/PlugIns/SUAskPermissionExtension.appex/SUAskPermissionExtension](MACHOS/SUAskPermissionExtension.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/iWorkImport](MACHOS/iWorkImport.md)
- [/System/Library/PrivateFrameworks/iWorkXPC.framework/XPCServices/iWorkFileFormat.xpc/iWorkFileFormat](MACHOS/iWorkFileFormat.md)
- [/System/Library/Recents/Plugins/GenericAddressHandler.addresshandler/GenericAddressHandler](MACHOS/GenericAddressHandler.md)
- [/System/Library/Recents/Plugins/MapsRecents.addresshandler/MapsRecents](MACHOS/MapsRecents.md)
- [/System/Library/RelevanceEngine/NanoDataSources/BreatheRelevanceEngineDataSource.bundle/BreatheRelevanceEngineDataSource](MACHOS/BreatheRelevanceEngineDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/MindRelevanceEngineDataSource.bundle/MindRelevanceEngineDataSource](MACHOS/MindRelevanceEngineDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoAlarmCompanionDataSource.bundle/NanoAlarmCompanionDataSource](MACHOS/NanoAlarmCompanionDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoBedtimeCompanionDataSource.bundle/NanoBedtimeCompanionDataSource](MACHOS/NanoBedtimeCompanionDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMenstrualCyclesRelevanceEngineDataSource.bundle/NanoMenstrualCyclesRelevanceEngineDataSource](MACHOS/NanoMenstrualCyclesRelevanceEngineDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineActivityRings.bundle/RelevanceEngineActivityRings](MACHOS/RelevanceEngineActivityRings.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineActivityUpNext.bundle/RelevanceEngineActivityUpNext](MACHOS/RelevanceEngineActivityUpNext.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineAudiobooks.bundle/RelevanceEngineAudiobooks](MACHOS/RelevanceEngineAudiobooks.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineCalendar.bundle/RelevanceEngineCalendar](MACHOS/RelevanceEngineCalendar.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineHeart.bundle/RelevanceEngineHeart](MACHOS/RelevanceEngineHeart.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineMusic.bundle/RelevanceEngineMusic](MACHOS/RelevanceEngineMusic.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineNowPlaying.bundle/RelevanceEngineNowPlaying](MACHOS/RelevanceEngineNowPlaying.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEnginePodcasts.bundle/RelevanceEnginePodcasts](MACHOS/RelevanceEnginePodcasts.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineReminders.bundle/RelevanceEngineReminders](MACHOS/RelevanceEngineReminders.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSiriSnippets.bundle/RelevanceEngineSiriSnippets](MACHOS/RelevanceEngineSiriSnippets.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSports.bundle/RelevanceEngineSports](MACHOS/RelevanceEngineSports.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineStopwatch.bundle/RelevanceEngineStopwatch](MACHOS/RelevanceEngineStopwatch.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineTimer.bundle/RelevanceEngineTimer](MACHOS/RelevanceEngineTimer.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineWallet.bundle/RelevanceEngineWallet](MACHOS/RelevanceEngineWallet.md)
- [/System/Library/RelevanceEngine/NanoDataSources/ShortcutsRelevanceEngineDataSource.bundle/ShortcutsRelevanceEngineDataSource](MACHOS/ShortcutsRelevanceEngineDataSource.md)
- [/System/Library/ScreenReader/BrailleDrivers/Alva6Series.brailledriver/Alva6Series](MACHOS/Alva6Series.md)
- [/System/Library/ScreenReader/BrailleDrivers/Baum.brailledriver/Baum](MACHOS/Baum.md)
- [/System/Library/ScreenReader/BrailleDrivers/BrailleNoteApex.brailledriver/BrailleNoteApex](MACHOS/BrailleNoteApex.md)
- [/System/Library/ScreenReader/BrailleDrivers/BrailleSense.brailledriver/BrailleSense](MACHOS/BrailleSense.md)
- [/System/Library/ScreenReader/BrailleDrivers/Brailliant 2 Driver.brailledriver/Brailliant 2 Driver](MACHOS/Brailliant_2_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/DOT Driver.brailledriver/DOT Driver](MACHOS/DOT_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/EasyLink.brailledriver/EasyLink](MACHOS/EasyLink.md)
- [/System/Library/ScreenReader/BrailleDrivers/Eurobraille.brailledriver/Eurobraille](MACHOS/Eurobraille.md)
- [/System/Library/ScreenReader/BrailleDrivers/FreedomScientific.brailledriver/FreedomScientific](MACHOS/FreedomScientific.md)
- [/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/GenericHID](MACHOS/GenericHID.md)
- [/System/Library/ScreenReader/BrailleDrivers/HIMS Driver.brailledriver/HIMS Driver](MACHOS/HIMS_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/HandyTech.brailledriver/HandyTech](MACHOS/HandyTech.md)
- [/System/Library/ScreenReader/BrailleDrivers/KGS Driver.brailledriver/KGS Driver](MACHOS/KGS_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/MDV.brailledriver/MDV](MACHOS/MDV.md)
- [/System/Library/ScreenReader/BrailleDrivers/Ninepoint Systems Driver.brailledriver/Ninepoint Systems Driver](MACHOS/Ninepoint_Systems_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/Papenmeier.brailledriver/Papenmeier](MACHOS/Papenmeier.md)
- [/System/Library/ScreenReader/BrailleDrivers/Seika.brailledriver/Seika](MACHOS/Seika.md)
- [/System/Library/ScreenReader/BrailleTables/AppleBrailleTranslator.brailletable/AppleBrailleTranslator](MACHOS/AppleBrailleTranslator.md)
- [/System/Library/ScreenReader/BrailleTables/BrailleNBSC.brailletable/BrailleNBSC](MACHOS/BrailleNBSC.md)
- [/System/Library/ScreenReader/BrailleTables/Duxbury.brailletable/Duxbury](MACHOS/Duxbury.md)
- [/System/Library/ScreenReader/BrailleTables/LiblouisBrailleTranslator.brailletable/LiblouisBrailleTranslator](MACHOS/LiblouisBrailleTranslator.md)
- [/System/Library/ScreenReader/BrailleTables/Rhine.brailletable/Rhine](MACHOS/Rhine.md)
- [/System/Library/SetupAssistantBundles/FaceTimeSetupAssistantBundle.bundle/FaceTimeSetupAssistantBundle](MACHOS/FaceTimeSetupAssistantBundle.md)
- [/System/Library/SetupAssistantBundles/GameCenterSetupAssistant.bundle/GameCenterSetupAssistant](MACHOS/GameCenterSetupAssistant.md)
- [/System/Library/SetupAssistantBundles/MadridSetupAssistantBundle.bundle/MadridSetupAssistantBundle](MACHOS/MadridSetupAssistantBundle.md)
- [/System/Library/SetupAssistantBundles/SBSyncServiceSetupAssistantBundle.bundle/SBSyncServiceSetupAssistantBundle](MACHOS/SBSyncServiceSetupAssistantBundle.md)
- [/System/Library/SetupAssistantBundles/iTunesStoreSetupAssistant.bundle/iTunesStoreSetupAssistant](MACHOS/iTunesStoreSetupAssistant.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AppLaunchSuggestionsPlugin.bundle/AppLaunchSuggestionsPlugin](MACHOS/AppLaunchSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/CalendarSuggestions.bundle/CalendarSuggestions](MACHOS/CalendarSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PhoneSuggestions.bundle/PhoneSuggestions](MACHOS/PhoneSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PlaybackControlsSuggestionsPlugin.bundle/PlaybackControlsSuggestionsPlugin](MACHOS/PlaybackControlsSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriGeoSuggestions.bundle/SiriGeoSuggestions](MACHOS/SiriGeoSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriInformationSuggestionsPlugin.bundle/SiriInformationSuggestionsPlugin](MACHOS/SiriInformationSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriMessagesSuggestions.bundle/SiriMessagesSuggestions](MACHOS/SiriMessagesSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSettingsSuggestionsPlugin.bundle/SiriSettingsSuggestionsPlugin](MACHOS/SiriSettingsSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSocialConversationSuggestionsPlugin.bundle/SiriSocialConversationSuggestionsPlugin](MACHOS/SiriSocialConversationSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriTimeSuggestionsPlugin.bundle/SiriTimeSuggestionsPlugin](MACHOS/SiriTimeSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SystemCommandsSuggestionsPlugin.bundle/SystemCommandsSuggestionsPlugin](MACHOS/SystemCommandsSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/VideoSuggestionsPlugin.bundle/VideoSuggestionsPlugin](MACHOS/VideoSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/AudioUIPlugin](MACHOS/AudioUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/CalendarUIPlugin.bundle/CalendarUIPlugin](MACHOS/CalendarUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/CarCommandsUIPlugin.bundle/CarCommandsUIPlugin](MACHOS/CarCommandsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/FindMyUIPlugin.bundle/FindMyUIPlugin](MACHOS/FindMyUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/GeoUIPlugin.bundle/GeoUIPlugin](MACHOS/GeoUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/HomeCommunicationUIPlugin.bundle/HomeCommunicationUIPlugin](MACHOS/HomeCommunicationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/MessagesUIPlugin.bundle/MessagesUIPlugin](MACHOS/MessagesUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/PhoneUIPlugin.bundle/PhoneUIPlugin](MACHOS/PhoneUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SettingsCustomPlugin.bundle/SettingsCustomPlugin](MACHOS/SettingsCustomPlugin.md)
- [/System/Library/Snippets/UIPlugins/ShazamUIPlugin.bundle/ShazamUIPlugin](MACHOS/ShazamUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriExpanseInternalUIPlugin.bundle/SiriExpanseInternalUIPlugin](MACHOS/SiriExpanseInternalUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriInferenceFlowsUIPlugin.bundle/SiriInferenceFlowsUIPlugin](MACHOS/SiriInferenceFlowsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriLinkUIPlugin.bundle/SiriLinkUIPlugin](MACHOS/SiriLinkUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriMailUIPlugin.bundle/SiriMailUIPlugin](MACHOS/SiriMailUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSocialConversationUIPlugin.bundle/SiriSocialConversationUIPlugin](MACHOS/SiriSocialConversationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSuggestionsUIPlugin.bundle/SiriSuggestionsUIPlugin](MACHOS/SiriSuggestionsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriVideoUIPlugin.bundle/SiriVideoUIPlugin](MACHOS/SiriVideoUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/Snippets/UIPlugins/TimerUIPlugin.bundle/TimerUIPlugin](MACHOS/TimerUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/WellnessUIPlugin.bundle/WellnessUIPlugin](MACHOS/WellnessUIPlugin.md)
- [/System/Library/SpringBoardPlugins/FindMyiPhoneLockScreen.lockbundle/FindMyiPhoneLockScreen](MACHOS/FindMyiPhoneLockScreen.md)
- [/System/Library/SpringBoardPlugins/PassesLockScreenPlugin.lockbundle/PassesLockScreenPlugin](MACHOS/PassesLockScreenPlugin.md)
- [/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin](MACHOS/StoreDemoPlugin.md)
- [/System/Library/SpringBoardPlugins/ZoomTouch.bundle/ZoomTouch](MACHOS/ZoomTouch.md)
- [/System/Library/StreamingExtractorPlugins/STAEAExtractionPlugin.bundle/STAEAExtractionPlugin](MACHOS/STAEAExtractionPlugin.md)
- [/System/Library/SyncBundles/AirFair.syncBundle/AirFair](MACHOS/AirFair.md)
- [/System/Library/SyncBundles/AirFair2.syncBundle/AirFair2](MACHOS/AirFair2.md)
- [/System/Library/SyncBundles/Apps.syncBundle/Apps](MACHOS/Apps.md)
- [/System/Library/SyncBundles/Books.syncBundle/Books](MACHOS/Books.md)
- [/System/Library/SyncBundles/LogsPlugin.syncBundle/LogsPlugin](MACHOS/LogsPlugin.md)
- [/System/Library/SyncBundles/MBATCPlugin.syncBundle/MBATCPlugin](MACHOS/MBATCPlugin.md)
- [/System/Library/SyncBundles/MobileSlideShow.syncBundle/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary](MACHOS/MusicLibrary.md)
- [/System/Library/SyncBundles/Podcasts.syncBundle/Podcasts](MACHOS/Podcasts.md)
- [/System/Library/SyncBundles/SMS.syncBundle/SMS](MACHOS/SMS.md)
- [/System/Library/SyncBundles/Tones.syncBundle/Tones](MACHOS/Tones.md)
- [/System/Library/SyncBundles/UserDataPlugin.syncBundle/UserDataPlugin](MACHOS/UserDataPlugin.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/EAPOLController](MACHOS/EAPOLController.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient](MACHOS/eapolclient.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/SystemConfiguration/PPPController.bundle/PPPController](MACHOS/PPPController.md)
- [/System/Library/SystemConfiguration/PPPController.bundle/PlugIns/L2TP.ppp/L2TP](MACHOS/L2TP.md)
- [/System/Library/SystemConfiguration/PPPController.bundle/PlugIns/PPPDialogs.ppp/PPPDialogs](MACHOS/PPPDialogs.md)
- [/System/Library/SystemConfiguration/USBDeviceConfiguration.bundle/USBDeviceConfiguration](MACHOS/USBDeviceConfiguration.md)
- [/System/Library/TextInput/Plugins/MessagesDataKeyboardPlugin.bundle/MessagesDataKeyboardPlugin](MACHOS/MessagesDataKeyboardPlugin.md)
- [/System/Library/TextInput/kbd](MACHOS/kbd.md)
- [/System/Library/Trace/Providers/Logging.bundle/Logging](MACHOS/Logging.md)
- [/System/Library/Trace/Providers/Required.bundle/Required](MACHOS/Required.md)
- [/System/Library/Trace/Providers/Symbolication.bundle/Symbolication](MACHOS/Symbolication.md)
- [/System/Library/Trace/Providers/TrialProvider.bundle/TrialProvider](MACHOS/TrialProvider.md)
- [/System/Library/UsageBundles/CalendarUsage.bundle/CalendarUsage](MACHOS/CalendarUsage.md)
- [/System/Library/UsageBundles/ContactsUsage.bundle/ContactsUsage](MACHOS/ContactsUsage.md)
- [/System/Library/UsageBundles/MailUsage.bundle/MailUsage](MACHOS/MailUsage.md)
- [/System/Library/UsageBundles/MessagesUsagePreferencesPlugin.bundle/MessagesUsagePreferencesPlugin](MACHOS/MessagesUsagePreferencesPlugin.md)
- [/System/Library/UsageBundles/MusicUsage.bundle/MusicUsage](MACHOS/MusicUsage.md)
- [/System/Library/UsageBundles/NanoBackupUsage.bundle/NanoBackupUsage](MACHOS/NanoBackupUsage.md)
- [/System/Library/UsageBundles/PassbookUsageBundle.bundle/PassbookUsageBundle](MACHOS/PassbookUsageBundle.md)
- [/System/Library/UsageBundles/SafariUsageBundle.bundle/SafariUsageBundle](MACHOS/SafariUsageBundle.md)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage.md)
- [/System/Library/UsageBundles/ToneSettingsUsage.bundle/ToneSettingsUsage](MACHOS/ToneSettingsUsage.md)
- [/System/Library/UsageBundles/VideosUsage.bundle/VideosUsage](MACHOS/VideosUsage.md)
- [/System/Library/UsageBundles/VisualVoicemailUsage.bundle/VisualVoicemailUsage](MACHOS/VisualVoicemailUsage.md)
- [/System/Library/UserEventPlugins/ADEventListenerPlugin.plugin/ADEventListenerPlugin](MACHOS/ADEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/AHTUserEventAgent.plugin/AHTUserEventAgent](MACHOS/AHTUserEventAgent.md)
- [/System/Library/UserEventPlugins/BonjourEvents.plugin/BonjourEvents](MACHOS/BonjourEvents.md)
- [/System/Library/UserEventPlugins/GreenTeaUserEventAgent.plugin/GreenTeaUserEventAgent](MACHOS/GreenTeaUserEventAgent.md)
- [/System/Library/UserEventPlugins/ManagedConfigurationUEA.plugin/ManagedConfigurationUEA](MACHOS/ManagedConfigurationUEA.md)
- [/System/Library/UserEventPlugins/MemoryMonitor.plugin/MemoryMonitor](MACHOS/MemoryMonitor.md)
- [/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA](MACHOS/MobileBackupUEA.md)
- [/System/Library/UserEventPlugins/MobileGestaltEvents.plugin/MobileGestaltEvents](MACHOS/MobileGestaltEvents.md)
- [/System/Library/UserEventPlugins/MobileKeyBagLockState.plugin/MobileKeyBagLockState](MACHOS/MobileKeyBagLockState.md)
- [/System/Library/UserEventPlugins/PerfPowerServicesEventListenerPlugin.plugin/PerfPowerServicesEventListenerPlugin](MACHOS/PerfPowerServicesEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/USBEthernetSharing.plugin/USBEthernetSharing](MACHOS/USBEthernetSharing.md)
- [/System/Library/UserEventPlugins/com.apple.AppleKeyStoreEvents.plugin/com.apple.AppleKeyStoreEvents](MACHOS/com.apple.AppleKeyStoreEvents.md)
- [/System/Library/UserEventPlugins/com.apple.BackgroundTaskAgentPlugin.plugin/com.apple.BackgroundTaskAgentPlugin](MACHOS/com.apple.BackgroundTaskAgentPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.ExternalAccessory.matching.plugin/com.apple.ExternalAccessory.matching](MACHOS/com.apple.ExternalAccessory.matching.md)
- [/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching](MACHOS/com.apple.accessoryd.matching.md)
- [/System/Library/UserEventPlugins/com.apple.alarm.plugin/com.apple.alarm](MACHOS/com.apple.alarm.md)
- [/System/Library/UserEventPlugins/com.apple.bonjour.plugin/com.apple.bonjour](MACHOS/com.apple.bonjour.md)
- [/System/Library/UserEventPlugins/com.apple.cfnotification.plugin/com.apple.cfnotification](MACHOS/com.apple.cfnotification.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/UserEventPlugins/com.apple.dispatch.vfs.plugin/com.apple.dispatch.vfs](MACHOS/com.apple.dispatch.vfs.md)
- [/System/Library/UserEventPlugins/com.apple.fsevents.matching.plugin/com.apple.fsevents.matching](MACHOS/com.apple.fsevents.matching.md)
- [/System/Library/UserEventPlugins/com.apple.iokit.matching.plugin/com.apple.iokit.matching](MACHOS/com.apple.iokit.matching.md)
- [/System/Library/UserEventPlugins/com.apple.launchd.helper.plugin/com.apple.launchd.helper](MACHOS/com.apple.launchd.helper.md)
- [/System/Library/UserEventPlugins/com.apple.netsvcproxy.plugin/com.apple.netsvcproxy](MACHOS/com.apple.netsvcproxy.md)
- [/System/Library/UserEventPlugins/com.apple.networkextension.plugin/com.apple.networkextension](MACHOS/com.apple.networkextension.md)
- [/System/Library/UserEventPlugins/com.apple.nsurlsessiond.plugin/com.apple.nsurlsessiond](MACHOS/com.apple.nsurlsessiond.md)
- [/System/Library/UserEventPlugins/com.apple.rapport.events.plugin/com.apple.rapport.events](MACHOS/com.apple.rapport.events.md)
- [/System/Library/UserEventPlugins/com.apple.spd.plugin/com.apple.spd](MACHOS/com.apple.spd.md)
- [/System/Library/UserEventPlugins/com.apple.systemconfiguration.plugin/com.apple.systemconfiguration](MACHOS/com.apple.systemconfiguration.md)
- [/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin](MACHOS/com.apple.tailspin.md)
- [/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry](MACHOS/com.apple.telemetry.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/UserEventPlugins/routined.events.plugin/routined.events](MACHOS/routined.events.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ARQLNotifications.bundle/com.apple.ARQLNotifications](MACHOS/com.apple.ARQLNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.donotdisturb.bundle/com.apple.donotdisturb](MACHOS/com.apple.donotdisturb.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1](MACHOS/SemanticStyleV1.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/VideoDeghostingV1](MACHOS/VideoDeghostingV1.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/System/Library/VoiceServices/PlugIns/Base.vsplugin/Base](MACHOS/Base.md)
- [/bin/df](MACHOS/df.md)
- [/bin/ps](MACHOS/ps.md)
- [/private/var/staged_system_apps/AppleTV.app/AppleTV](MACHOS/AppleTV.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVCoreSpotlightExtension.appex/TVCoreSpotlightExtension](MACHOS/TVCoreSpotlightExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVIntentsExtension.appex/TVIntentsExtension](MACHOS/TVIntentsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKAudiobooks.framework/BKAudiobooks](MACHOS/BKAudiobooks.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary](MACHOS/BKLibrary.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksAll.framework/BooksAll](MACHOS/BooksAll.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/EngagementCollector.framework/EngagementCollector](MACHOS/EngagementCollector.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BookEPUBWebProcessPlugin.bundle/BookEPUBWebProcessPlugin](MACHOS/BookEPUBWebProcessPlugin.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksEngagementExtension.appex/BooksEngagementExtension](MACHOS/BooksEngagementExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksIntentHandler.appex/BooksIntentHandler](MACHOS/BooksIntentHandler.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksNotificationContentExtension.appex/BooksNotificationContentExtension](MACHOS/BooksNotificationContentExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension](MACHOS/BooksProductPageExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/BooksSpotlightExtension](MACHOS/BooksSpotlightExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksThumbnail.appex/BooksThumbnail](MACHOS/BooksThumbnail.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/XPCServices/XPCUbiquityDisableService.xpc/XPCUbiquityDisableService](MACHOS/XPCUbiquityDisableService.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Bridge.app/PlugIns/GreenfieldThumbnailExtension.appex/GreenfieldThumbnailExtension](MACHOS/GreenfieldThumbnailExtension.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Compass.app/Compass](MACHOS/Compass.md)
- [/private/var/staged_system_apps/Contacts.app/Contacts](MACHOS/Contacts.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsItems.appex/FindMyWidgetIntentsItems](MACHOS/FindMyWidgetIntentsItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsPeople.appex/FindMyWidgetIntentsPeople](MACHOS/FindMyWidgetIntentsPeople.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessIntents.appex/FitnessIntents](MACHOS/FitnessIntents.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/MirroredWidgetExtension.appex/MirroredWidgetExtension](MACHOS/MirroredWidgetExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Health.app/PlugIns/HealthMedicationsWidgetExtension.appex/HealthMedicationsWidgetExtension](MACHOS/HealthMedicationsWidgetExtension.md)
- [/private/var/staged_system_apps/Health.app/PlugIns/HealthMentalHealthWidgetExtension.appex/HealthMentalHealthWidgetExtension](MACHOS/HealthMentalHealthWidgetExtension.md)
- [/private/var/staged_system_apps/Health.app/PlugIns/ShareExtension.appex/ShareExtension](MACHOS/ShareExtension.md)
- [/private/var/staged_system_apps/Home.app/Home](MACHOS/Home.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeDiagnosticExtension.appex/HomeDiagnosticExtension](MACHOS/HomeDiagnosticExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification](MACHOS/HomeNotification.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomePersonalRequestNotification.appex/HomePersonalRequestNotification](MACHOS/HomePersonalRequestNotification.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeUtilNotification.appex/HomeUtilNotification](MACHOS/HomeUtilNotification.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen](MACHOS/HomeWidgetLockScreen.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent](MACHOS/HomeWidgetSingleAccessoryIntent.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Magnifier.app/Magnifier](MACHOS/Magnifier.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/MapsSpotlightIndexExtension.appex/MapsSpotlightIndexExtension](MACHOS/MapsSpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/SiriTrafficIncidents.appex/SiriTrafficIncidents](MACHOS/SiriTrafficIncidents.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension](MACHOS/CalendarWidgetExtension.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/FacetimeExtension.appex/FacetimeExtension](MACHOS/FacetimeExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/Extensions/MailShortcutsExtension.appex/MailShortcutsExtension](MACHOS/MailShortcutsExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailIntentsExtension.appex/MailIntentsExtension](MACHOS/MailIntentsExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.EditorExtension.appex/com.apple.mobilenotes.EditorExtension](MACHOS/com.apple.mobilenotes.EditorExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.IntentsExtension.appex/com.apple.mobilenotes.IntentsExtension](MACHOS/com.apple.mobilenotes.IntentsExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.QuickLookExtension.appex/com.apple.mobilenotes.QuickLookExtension](MACHOS/com.apple.mobilenotes.QuickLookExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SpotlightIndexExtension.appex/com.apple.mobilenotes.SpotlightIndexExtension](MACHOS/com.apple.mobilenotes.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileStore.app/MobileStore](MACHOS/MobileStore.md)
- [/private/var/staged_system_apps/MobileStore.app/XPCServices/com.apple.MobileStore.appremoval.xpc/com.apple.MobileStore.appremoval](MACHOS/com.apple.MobileStore.appremoval.md)
- [/private/var/staged_system_apps/MobileTimer.app/MobileTimer](MACHOS/MobileTimer.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Extensions/MusicFocusFilters.appex/MusicFocusFilters](MACHOS/MusicFocusFilters.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker](MACHOS/MediaPicker.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicCoreSpotlightExtension.appex/MusicCoreSpotlightExtension](MACHOS/MusicCoreSpotlightExtension.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicNotificationContentExtension.appex/MusicNotificationContentExtension](MACHOS/MusicNotificationContentExtension.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/StoreFlowExtension.appex/StoreFlowExtension](MACHOS/StoreFlowExtension.md)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News.md)
- [/private/var/staged_system_apps/News.app/PlugIns/ArticleNotificationExtension.appex/ArticleNotificationExtension](MACHOS/ArticleNotificationExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/MarketingNotificationExtension.appex/MarketingNotificationExtension](MACHOS/MarketingNotificationExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsArticleQuickLook.appex/NewsArticleQuickLook](MACHOS/NewsArticleQuickLook.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsAudioExtension.appex/NewsAudioExtension](MACHOS/NewsAudioExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsDiagnosticExtension.appex/NewsDiagnosticExtension](MACHOS/NewsDiagnosticExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsEngagementExtension.appex/NewsEngagementExtension](MACHOS/NewsEngagementExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/News.app/PlugIns/OpenInNews.appex/OpenInNews](MACHOS/OpenInNews.md)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookQuicklookPreviewExtension.appex/PassbookQuicklookPreviewExtension](MACHOS/PassbookQuicklookPreviewExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookTransactionNotificationContentExtension.appex/PassbookTransactionNotificationContentExtension](MACHOS/PassbookTransactionNotificationContentExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/IMDebug.framework/IMDebug](MACHOS/IMDebug.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/PodcastsClassKitExtension](MACHOS/PodcastsClassKitExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsNotificationExtension.appex/PodcastsNotificationExtension](MACHOS/PodcastsNotificationExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.DiagnosticExtension.appex/com.apple.podcasts.DiagnosticExtension](MACHOS/com.apple.podcasts.DiagnosticExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension](MACHOS/com.apple.podcasts.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSpotlightIndexExtension.appex/RemindersSpotlightIndexExtension](MACHOS/RemindersSpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/CacheDeleteExtension.appex/CacheDeleteExtension](MACHOS/CacheDeleteExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/AutomationNotificationContent.appex/AutomationNotificationContent](MACHOS/AutomationNotificationContent.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/QuickLookExtension.appex/QuickLookExtension](MACHOS/QuickLookExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsActionExtension.appex/ShortcutsActionExtension](MACHOS/ShortcutsActionExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ThumbnailExtension.appex/ThumbnailExtension](MACHOS/ThumbnailExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDiagnosticExtension.appex/StocksDiagnosticExtension](MACHOS/StocksDiagnosticExtension.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsNotification.appex/TipsNotification](MACHOS/TipsNotification.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsQuicklook.appex/TipsQuicklook](MACHOS/TipsQuicklook.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsSpotlightIndex.appex/TipsSpotlightIndex](MACHOS/TipsSpotlightIndex.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsWidget.appex/TipsWidget](MACHOS/TipsWidget.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension](MACHOS/VoiceMemosIntentsExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension](MACHOS/VoiceMemosShareExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/com.apple.VoiceMemos.SpotlightIndexExtension.appex/com.apple.VoiceMemos.SpotlightIndexExtension](MACHOS/com.apple.VoiceMemos.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherDiagnosticExtension.appex/WeatherDiagnosticExtension](MACHOS/WeatherDiagnosticExtension.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents](MACHOS/WeatherIntents.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/fsck](MACHOS/fsck.md)
- [/sbin/fsck_apfs](MACHOS/fsck_apfs.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount](MACHOS/mount.md)
- [/sbin/mount_apfs](MACHOS/mount_apfs.md)
- [/sbin/mount_lifs](MACHOS/mount_lifs.md)
- [/sbin/mount_nfs](MACHOS/mount_nfs.md)
- [/sbin/mount_tmpfs](MACHOS/mount_tmpfs.md)
- [/sbin/newfs_apfs](MACHOS/newfs_apfs.md)
- [/sbin/umount](MACHOS/umount.md)
- [/usr/bin/DumpBasebandCrash](MACHOS/DumpBasebandCrash.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/afktool](MACHOS/afktool.md)
- [/usr/bin/brctl](MACHOS/brctl.md)
- [/usr/bin/codecctl](MACHOS/codecctl.md)
- [/usr/bin/fileproviderctl](MACHOS/fileproviderctl.md)
- [/usr/bin/footprint](MACHOS/footprint.md)
- [/usr/bin/hidutil](MACHOS/hidutil.md)
- [/usr/bin/hpmdiagnose](MACHOS/hpmdiagnose.md)
- [/usr/bin/kbdebug](MACHOS/kbdebug.md)
- [/usr/bin/lsdiagnose](MACHOS/lsdiagnose.md)
- [/usr/bin/ltop](MACHOS/ltop.md)
- [/usr/bin/nfsstat](MACHOS/nfsstat.md)
- [/usr/bin/powerlogHelperd](MACHOS/powerlogHelperd.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/bin/sysdiagnose](MACHOS/sysdiagnose.md)
- [/usr/bin/taskinfo](MACHOS/taskinfo.md)
- [/usr/bin/umtool](MACHOS/umtool.md)
- [/usr/bin/vm_stat](MACHOS/vm_stat.md)
- [/usr/bin/zprint](MACHOS/zprint.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libBacktraceRecording.dylib](MACHOS/libBacktraceRecording.dylib.md)
- [/usr/lib/libCoreKE.dylib](MACHOS/libCoreKE.dylib.md)
- [/usr/lib/libCoreLSKD.dylib](MACHOS/libCoreLSKD.dylib.md)
- [/usr/lib/libMTLCapture.dylib](MACHOS/libMTLCapture.dylib.md)
- [/usr/lib/libMTLToolsDiagnostics.dylib](MACHOS/libMTLToolsDiagnostics.dylib.md)
- [/usr/lib/libMainThreadChecker.dylib](MACHOS/libMainThreadChecker.dylib.md)
- [/usr/lib/libRPAC.dylib](MACHOS/libRPAC.dylib.md)
- [/usr/lib/libSystem.B_asan.dylib](MACHOS/libSystem.B_asan.dylib.md)
- [/usr/lib/libSystem_asan.dylib](MACHOS/libSystem_asan.dylib.md)
- [/usr/lib/libViewDebuggerSupport.dylib](MACHOS/libViewDebuggerSupport.dylib.md)
- [/usr/lib/swift/libswiftRemoteMirror.dylib](MACHOS/libswiftRemoteMirror.dylib.md)
- [/usr/lib/system/introspection/libdispatch.dylib](MACHOS/libdispatch.dylib.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/DataDetectorsSourceAccess](MACHOS/DataDetectorsSourceAccess.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/FSTaskScheduler](MACHOS/FSTaskScheduler.md)
- [/usr/libexec/FinishRestoreFromBackup](MACHOS/FinishRestoreFromBackup.md)
- [/usr/libexec/IOAccelMemoryInfoCollector](MACHOS/IOAccelMemoryInfoCollector.md)
- [/usr/libexec/IOMFB_bics_daemon](MACHOS/IOMFB_bics_daemon.md)
- [/usr/libexec/MSUEarlyBootTask](MACHOS/MSUEarlyBootTask.md)
- [/usr/libexec/MTLAssetUpgraderD](MACHOS/MTLAssetUpgraderD.md)
- [/usr/libexec/MobileGestaltHelper](MACHOS/MobileGestaltHelper.md)
- [/usr/libexec/MobileStorageMounter](MACHOS/MobileStorageMounter.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/OTATaskingAgent](MACHOS/OTATaskingAgent.md)
- [/usr/libexec/PerfPowerServices](MACHOS/PerfPowerServices.md)
- [/usr/libexec/PerfPowerServicesExtended](MACHOS/PerfPowerServicesExtended.md)
- [/usr/libexec/PowerUIAgent](MACHOS/PowerUIAgent.md)
- [/usr/libexec/PreboardService](MACHOS/PreboardService.md)
- [/usr/libexec/ProxiedCrashCopier](MACHOS/ProxiedCrashCopier.md)
- [/usr/libexec/PurpleReverseProxy](MACHOS/PurpleReverseProxy.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/SavageUtil](MACHOS/SavageUtil.md)
- [/usr/libexec/SensorKitALSHelper](MACHOS/SensorKitALSHelper.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/SyncAgent](MACHOS/SyncAgent.md)
- [/usr/libexec/UserEventAgent](MACHOS/UserEventAgent.md)
- [/usr/libexec/ViewHierarchyAgent](MACHOS/ViewHierarchyAgent.md)
- [/usr/libexec/YonkersUtil](MACHOS/YonkersUtil.md)
- [/usr/libexec/addressbooksyncd](MACHOS/addressbooksyncd.md)
- [/usr/libexec/adid](MACHOS/adid.md)
- [/usr/libexec/adprivacyd](MACHOS/adprivacyd.md)
- [/usr/libexec/afcd](MACHOS/afcd.md)
- [/usr/libexec/amfid](MACHOS/amfid.md)
- [/usr/libexec/aned](MACHOS/aned.md)
- [/usr/libexec/announced](MACHOS/announced.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/appleidsetupd](MACHOS/appleidsetupd.md)
- [/usr/libexec/arkitd](MACHOS/arkitd.md)
- [/usr/libexec/asd](MACHOS/asd.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/atc](MACHOS/atc.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd.md)
- [/usr/libexec/audiomxd](MACHOS/audiomxd.md)
- [/usr/libexec/avconferenced](MACHOS/avconferenced.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/backgroundassets.user](MACHOS/backgroundassets.user.md)
- [/usr/libexec/batteryalgorithmsd](MACHOS/batteryalgorithmsd.md)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced.md)
- [/usr/libexec/betaenrollmentd](MACHOS/betaenrollmentd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/biometrickitd](MACHOS/biometrickitd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/bootpd](MACHOS/bootpd.md)
- [/usr/libexec/brookcompaniond](MACHOS/brookcompaniond.md)
- [/usr/libexec/bulletindistributord](MACHOS/bulletindistributord.md)
- [/usr/libexec/captiveagent](MACHOS/captiveagent.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/cc_fips_test](MACHOS/cc_fips_test.md)
- [/usr/libexec/checkerboardd](MACHOS/checkerboardd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/ciphermld](MACHOS/ciphermld.md)
- [/usr/libexec/com.apple.Safari.History](MACHOS/com.apple.Safari.History.md)
- [/usr/libexec/companion_proxy](MACHOS/companion_proxy.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/configd](MACHOS/configd.md)
- [/usr/libexec/containermanagerd](MACHOS/containermanagerd.md)
- [/usr/libexec/containermanagerd_system](MACHOS/containermanagerd_system.md)
- [/usr/libexec/continuitycaptured](MACHOS/continuitycaptured.md)
- [/usr/libexec/coordinated](MACHOS/coordinated.md)
- [/usr/libexec/corebrightnessdiag](MACHOS/corebrightnessdiag.md)
- [/usr/libexec/corecaptured](MACHOS/corecaptured.md)
- [/usr/libexec/coredatad](MACHOS/coredatad.md)
- [/usr/libexec/coreduetd](MACHOS/coreduetd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/crash_mover](MACHOS/crash_mover.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/datastored](MACHOS/datastored.md)
- [/usr/libexec/debugserver](MACHOS/debugserver.md)
- [/usr/libexec/deferredmediad](MACHOS/deferredmediad.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/demod_helper](MACHOS/demod_helper.md)
- [/usr/libexec/deviceaccessd](MACHOS/deviceaccessd.md)
- [/usr/libexec/dhcp6d](MACHOS/dhcp6d.md)
- [/usr/libexec/diagnosticd](MACHOS/diagnosticd.md)
- [/usr/libexec/diagnosticextensionsd](MACHOS/diagnosticextensionsd.md)
- [/usr/libexec/dietapplecamerad](MACHOS/dietapplecamerad.md)
- [/usr/libexec/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/libexec/dirs_cleaner](MACHOS/dirs_cleaner.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/dprivacyd](MACHOS/dprivacyd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/dtfetchsymbolsd](MACHOS/dtfetchsymbolsd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/eventkitsyncd](MACHOS/eventkitsyncd.md)
- [/usr/libexec/facemetricsd](MACHOS/facemetricsd.md)
- [/usr/libexec/fairplaydeviceidentityd](MACHOS/fairplaydeviceidentityd.md)
- [/usr/libexec/fdrhelper](MACHOS/fdrhelper.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmybeaconingd](MACHOS/findmybeaconingd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/finish_demo_restore](MACHOS/finish_demo_restore.md)
- [/usr/libexec/fmfd](MACHOS/fmfd.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/fseventsd](MACHOS/fseventsd.md)
- [/usr/libexec/ftp-proxy](MACHOS/ftp-proxy.md)
- [/usr/libexec/fusiond](MACHOS/fusiond.md)
- [/usr/libexec/gamecontrollerd](MACHOS/gamecontrollerd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/gputoolsd](MACHOS/gputoolsd.md)
- [/usr/libexec/gputoolsserviced](MACHOS/gputoolsserviced.md)
- [/usr/libexec/griddatad](MACHOS/griddatad.md)
- [/usr/libexec/handwritingd](MACHOS/handwritingd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/heartbeatd](MACHOS/heartbeatd.md)
- [/usr/libexec/hidd](MACHOS/hidd.md)
- [/usr/libexec/hostapd](MACHOS/hostapd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idamd](MACHOS/idamd.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/init_data_protection](MACHOS/init_data_protection.md)
- [/usr/libexec/init_exclavekit](MACHOS/init_exclavekit.md)
- [/usr/libexec/init_featureflags](MACHOS/init_featureflags.md)
- [/usr/libexec/installd](MACHOS/installd.md)
- [/usr/libexec/intelligentroutingd](MACHOS/intelligentroutingd.md)
- [/usr/libexec/ioupsd](MACHOS/ioupsd.md)
- [/usr/libexec/keybagd](MACHOS/keybagd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/languageassetd](MACHOS/languageassetd.md)
- [/usr/libexec/launchd_cache_loader](MACHOS/launchd_cache_loader.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/locationpushd](MACHOS/locationpushd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd](MACHOS/logd.md)
- [/usr/libexec/logd_helper](MACHOS/logd_helper.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/lsd](MACHOS/lsd.md)
- [/usr/libexec/lskdd](MACHOS/lskdd.md)
- [/usr/libexec/magicswitchd](MACHOS/magicswitchd.md)
- [/usr/libexec/mc_mobile_tunnel](MACHOS/mc_mobile_tunnel.md)
- [/usr/libexec/mdmd](MACHOS/mdmd.md)
- [/usr/libexec/mdmuserd](MACHOS/mdmuserd.md)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd.md)
- [/usr/libexec/mediaplaybackd](MACHOS/mediaplaybackd.md)
- [/usr/libexec/mediasetupd](MACHOS/mediasetupd.md)
- [/usr/libexec/metrickitd](MACHOS/metrickitd.md)
- [/usr/libexec/microstackshot](MACHOS/microstackshot.md)
- [/usr/libexec/misagent](MACHOS/misagent.md)
- [/usr/libexec/misd](MACHOS/misd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mlruntimed](MACHOS/mlruntimed.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobile_assertion_agent](MACHOS/mobile_assertion_agent.md)
- [/usr/libexec/mobile_diagnostics_relay](MACHOS/mobile_diagnostics_relay.md)
- [/usr/libexec/mobile_house_arrest](MACHOS/mobile_house_arrest.md)
- [/usr/libexec/mobile_installation_proxy](MACHOS/mobile_installation_proxy.md)
- [/usr/libexec/mobile_obliterator](MACHOS/mobile_obliterator.md)
- [/usr/libexec/mobile_storage_proxy](MACHOS/mobile_storage_proxy.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/mtmergeprops](MACHOS/mtmergeprops.md)
- [/usr/libexec/nanomediaremotelinkagent](MACHOS/nanomediaremotelinkagent.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nanoregistrylaunchd](MACHOS/nanoregistrylaunchd.md)
- [/usr/libexec/naturallanguaged](MACHOS/naturallanguaged.md)
- [/usr/libexec/neagent](MACHOS/neagent.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nexusd](MACHOS/nexusd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nlcd](MACHOS/nlcd.md)
- [/usr/libexec/notification_proxy](MACHOS/notification_proxy.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/ospredictiond](MACHOS/ospredictiond.md)
- [/usr/libexec/otpaird](MACHOS/otpaird.md)
- [/usr/libexec/passcodenagd](MACHOS/passcodenagd.md)
- [/usr/libexec/passwordbreachd](MACHOS/passwordbreachd.md)
- [/usr/libexec/pcapd](MACHOS/pcapd.md)
- [/usr/libexec/pcsstatus](MACHOS/pcsstatus.md)
- [/usr/libexec/peakpowermanagerd](MACHOS/peakpowermanagerd.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/pfd](MACHOS/pfd.md)
- [/usr/libexec/pipelined](MACHOS/pipelined.md)
- [/usr/libexec/pkd](MACHOS/pkd.md)
- [/usr/libexec/pkreporter](MACHOS/pkreporter.md)
- [/usr/libexec/pmudiagnose/pmudiagnose](MACHOS/pmudiagnose.md)
- [/usr/libexec/powerdatad](MACHOS/powerdatad.md)
- [/usr/libexec/prng_seedctl](MACHOS/prng_seedctl.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad.md)
- [/usr/libexec/ptpd](MACHOS/ptpd.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/relatived](MACHOS/relatived.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotectl](MACHOS/remotectl.md)
- [/usr/libexec/remoted](MACHOS/remoted.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/resourcegrabberd](MACHOS/resourcegrabberd.md)
- [/usr/libexec/restoreserviced](MACHOS/restoreserviced.md)
- [/usr/libexec/routined](MACHOS/routined.md)
- [/usr/libexec/rsync/rsync.samba](MACHOS/rsync.samba.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/runningboardd](MACHOS/runningboardd.md)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
- [/usr/libexec/screenshotsyncd](MACHOS/screenshotsyncd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seld](MACHOS/seld.md)
- [/usr/libexec/sensorkitd](MACHOS/sensorkitd.md)
- [/usr/libexec/seputil](MACHOS/seputil.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/silhouette](MACHOS/silhouette.md)
- [/usr/libexec/siriknowledged](MACHOS/siriknowledged.md)
- [/usr/libexec/sirireaderd](MACHOS/sirireaderd.md)
- [/usr/libexec/smcDiagnose](MACHOS/smcDiagnose.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/soundanalysisd](MACHOS/soundanalysisd.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/splashboardd](MACHOS/splashboardd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/springboardservicesrelay](MACHOS/springboardservicesrelay.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/storagedatad](MACHOS/storagedatad.md)
- [/usr/libexec/storagekitd](MACHOS/storagekitd.md)
- [/usr/libexec/streaming_zip_conduit](MACHOS/streaming_zip_conduit.md)
- [/usr/libexec/swcd](MACHOS/swcd.md)
- [/usr/libexec/symptomsd](MACHOS/symptomsd.md)
- [/usr/libexec/symptomsd-diag](MACHOS/symptomsd-diag.md)
- [/usr/libexec/symptomsd-helper](MACHOS/symptomsd-helper.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/sysmond](MACHOS/sysmond.md)
- [/usr/libexec/sysstatuscheck](MACHOS/sysstatuscheck.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/teslad](MACHOS/teslad.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/timed](MACHOS/timed.md)
- [/usr/libexec/tipsd](MACHOS/tipsd.md)
- [/usr/libexec/transitd](MACHOS/transitd.md)
- [/usr/libexec/transparency-sysdiagnose](MACHOS/transparency-sysdiagnose.md)
- [/usr/libexec/transparencyStaticKey](MACHOS/transparencyStaticKey.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/triald](MACHOS/triald.md)
- [/usr/libexec/triald_system](MACHOS/triald_system.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tursd](MACHOS/tursd.md)
- [/usr/libexec/tvremoted](MACHOS/tvremoted.md)
- [/usr/libexec/tzd](MACHOS/tzd.md)
- [/usr/libexec/tzinit](MACHOS/tzinit.md)
- [/usr/libexec/tzlinkd](MACHOS/tzlinkd.md)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd.md)
- [/usr/libexec/usermanagerhelper](MACHOS/usermanagerhelper.md)
- [/usr/libexec/videocodecd](MACHOS/videocodecd.md)
- [/usr/libexec/videosubscriptionsd](MACHOS/videosubscriptionsd.md)
- [/usr/libexec/wapic](MACHOS/wapic.md)
- [/usr/libexec/watchdogd](MACHOS/watchdogd.md)
- [/usr/libexec/watchpresenced](MACHOS/watchpresenced.md)
- [/usr/libexec/wcd](MACHOS/wcd.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/webinspectord](MACHOS/webinspectord.md)
- [/usr/libexec/webpushd](MACHOS/webpushd.md)
- [/usr/libexec/wifiFirmwareLoader](MACHOS/wifiFirmwareLoader.md)
- [/usr/libexec/wifianalyticsd](MACHOS/wifianalyticsd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTAvrcp](MACHOS/BTAvrcp.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/BTMap](MACHOS/BTMap.md)
- [/usr/sbin/BTPbap](MACHOS/BTPbap.md)
- [/usr/sbin/BlueTool](MACHOS/BlueTool.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/absd](MACHOS/absd.md)
- [/usr/sbin/addNetworkInterface](MACHOS/addNetworkInterface.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/aslmanager](MACHOS/aslmanager.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/cfprefsd](MACHOS/cfprefsd.md)
- [/usr/sbin/ckksctl](MACHOS/ckksctl.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/distnoted](MACHOS/distnoted.md)
- [/usr/sbin/fairplayd.H2](MACHOS/fairplayd.H2.md)
- [/usr/sbin/filecoordinationd](MACHOS/filecoordinationd.md)
- [/usr/sbin/hdik](MACHOS/hdik.md)
- [/usr/sbin/ioreg](MACHOS/ioreg.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/mDNSResponderHelper](MACHOS/mDNSResponderHelper.md)
- [/usr/sbin/notifyd](MACHOS/notifyd.md)
- [/usr/sbin/nvram](MACHOS/nvram.md)
- [/usr/sbin/otctl](MACHOS/otctl.md)
- [/usr/sbin/pppd](MACHOS/pppd.md)
- [/usr/sbin/racoon](MACHOS/racoon.md)
- [/usr/sbin/rtadvd](MACHOS/rtadvd.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/syslogd](MACHOS/syslogd.md)
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

 
-  __TEXT.__text: 0xb8980
-  __TEXT.__cstring: 0x11f2c
-  __TEXT.__const: 0x1ca70
+  __TEXT.__text: 0xc8418
+  __TEXT.__cstring: 0x124a3
+  __TEXT.__const: 0x1e9b8
   __TEXT.__chain_starts: 0x0
-  __TEXT._rtk_mtab: 0x308
+  __TEXT._rtk_mtab: 0x320
   __TEXT.__constructor: 0x0
-  __DATA.__const: 0x27a0
-  __DATA.__data: 0x1288
+  __DATA.__const: 0x2190
+  __DATA.__data: 0x12e8
   __DATA._rtk_patchbay: 0x1e8
   __DATA._rtk_init_stack: 0x10000
   __DATA._rtk_irq_stack: 0x1000

   __DATA._rtk_boot: 0x8000
   __DATA._rtk_page_tables: 0x40000
   __DATA._rtk_power: 0x368
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_tunables: 0x5b0
   __DATA.__mod_init_func: 0x0
   __DATA.__noinit: 0x0
   __DATA._rtk_threads: 0x0
   __DATA._rtk_heap: 0x0
-  __DATA.__zerofill: 0xc6880
-  Symbols:   1436
+  __DATA.__zerofill: 0xc68b8
+  Symbols:   1443
   Functions: 0
 

```

#### SmartIOFirmware_ASCv6.im4p

>  `SmartIOFirmware_ASCv6.im4p`

```diff

 
-  __TEXT.__text: 0x1a454
-  __TEXT.__cstring: 0x102c
-  __TEXT.__const: 0x338
-  __TEXT._rtk_mtab: 0x278
+  __TEXT.__text: 0x1a9c0
+  __TEXT.__cstring: 0x1087
+  __TEXT.__const: 0x310
+  __TEXT._rtk_mtab: 0x290
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_vtt_KIC: 0x0
   __DATA.__mod_init_func: 0x20
-  __DATA.__const: 0x548
-  __DATA.__data: 0x15a0
+  __DATA.__const: 0x528
+  __DATA.__data: 0x1618
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_patchbay: 0x1e8
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_power: 0x358
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__autobkp: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xcec78
-  Symbols:   171
+  Symbols:   160
   Functions: 0
 

```

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

 
-  __TEXT.__text: 0x7aff00
+  __TEXT.__text: 0x963cd0
   __TEXT.__data_copy: 0x100000
-  __TEXT.__const: 0x803ff0
-  __TEXT.__cstring: 0x9c1ab
-  __TEXT._rtk_mtab: 0x288
+  __TEXT.__const: 0x7f61c0
+  __TEXT.__cstring: 0x125450
+  __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x507ac
-  __TEXT.__ustring: 0xe
-  __TEXT.__eh_frame: 0x200
-  __DATA.__const: 0x54958
+  __TEXT.__eh_frame: 0x308
+  __DATA.__const: 0x51a10
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xe0210
+  __DATA.__data: 0xdf108
   __DATA._rtk_power: 0x3a8
   __DATA._rtk_patchbay: 0x218
   __DATA._rtk_init_stack: 0x2000

   __DATA._rtk_smp_main: 0x8
   __DATA._rtk_boot_l1: 0x80
   __DATA.__mod_init_func: 0x20
-  __DATA.__zerofill: 0x221e58
+  __DATA.__zerofill: 0x20ded0
   Symbols:   0
   Functions: 0
 

```

#### agx_a000.bin

>  `agx_a000.bin`

```diff

 
-  __TEXT.__text: 0x58940
-  __TEXT.__gxf_code: 0x108c
+  __TEXT.__text: 0x5a99c
+  __TEXT.__gxf_code: 0x106c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1540
+  __TEXT.__const: 0x1e10
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bce
+  __TEXT.__gxf_shr_code: 0x554
+  __TEXT.__cstring: 0x1e51
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
-  __TEXT._rtk_mtab: 0x378
+  __TEXT._rtk_mtab: 0x390
   __DATA.__gxf_data: 0x41f0
-  __DATA.__data: 0xd78
-  __DATA.__const: 0x4c0
+  __DATA.__data: 0xdf8
+  __DATA.__const: 0x530
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
-  __DATA.__zerofill: 0x6b518
-  Symbols:   199
+  __DATA.__xnu_shared: 0x3c000
+  __DATA.__zerofill: 0x670d8
+  Symbols:   208
   Functions: 0
 

```

#### agx_b000.bin

>  `agx_b000.bin`

```diff

 
-  __TEXT.__text: 0x5862c
-  __TEXT.__gxf_code: 0x108c
+  __TEXT.__text: 0x5a6a0
+  __TEXT.__gxf_code: 0x106c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1580
+  __TEXT.__const: 0x1e50
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bce
+  __TEXT.__gxf_shr_code: 0x554
+  __TEXT.__cstring: 0x1e51
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
-  __TEXT._rtk_mtab: 0x378
+  __TEXT._rtk_mtab: 0x390
   __DATA.__gxf_data: 0x41f0
-  __DATA.__data: 0xd78
-  __DATA.__const: 0x4c0
+  __DATA.__data: 0xdf8
+  __DATA.__const: 0x530
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
-  __DATA.__zerofill: 0x6b398
-  Symbols:   199
+  __DATA.__xnu_shared: 0x3c000
+  __DATA.__zerofill: 0x66f58
+  Symbols:   208
   Functions: 0
 

```

#### agx_b100.bin

>  `agx_b100.bin`

```diff

 
-  __TEXT.__text: 0x5862c
-  __TEXT.__gxf_code: 0x108c
+  __TEXT.__text: 0x5a6a0
+  __TEXT.__gxf_code: 0x106c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1580
+  __TEXT.__const: 0x1e50
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bce
+  __TEXT.__gxf_shr_code: 0x554
+  __TEXT.__cstring: 0x1e51
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
-  __TEXT._rtk_mtab: 0x378
+  __TEXT._rtk_mtab: 0x390
   __DATA.__gxf_data: 0x41f0
-  __DATA.__data: 0xd78
-  __DATA.__const: 0x4c0
+  __DATA.__data: 0xdf8
+  __DATA.__const: 0x530
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
-  __DATA.__zerofill: 0x6b398
-  Symbols:   199
+  __DATA.__xnu_shared: 0x3c000
+  __DATA.__zerofill: 0x66f58
+  Symbols:   208
   Functions: 0
 

```

#### ansf.t8130.release.im4p

>  `ansf.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x1727cc
-  __TEXT.shared: 0xb7b0
-  __TEXT.read: 0x59d0
-  __TEXT.__const: 0x8d68
+  __TEXT.__text: 0x171c60
+  __TEXT.shared: 0xb6e4
+  __TEXT.read: 0x5a78
+  __TEXT.__const: 0x8e58
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e5b9
+  __TEXT.__cstring: 0x1e59a
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
   __DATA._rtk_boot: 0x8000
   __DATA._rtk_power: 0x160
-  __DATA._rtk_patchbay: 0x3bf
+  __DATA._rtk_patchbay: 0x38f
   __DATA._rtk_tunables: 0x5b0
-  __DATA.__const: 0x1588
+  __DATA.__const: 0x15c8
   __DATA.__data: 0x5fd0
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_page_tables: 0x40000
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
   __DATA.core_globals: 0x138
-  __DATA.__zerofill: 0x19b818
+  __DATA.__zerofill: 0x19b788
   Symbols:   0
   Functions: 0
 

```

#### aopfw-iphone16aop.RELEASE.im4p

>  `aopfw-iphone16aop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0x145edc
-  __TEXT.__const: 0x11f28
-  __TEXT.__cstring: 0x93fc
-  __TEXT.__chain_starts: 0x9c
-  __TEXT.__eh_frame: 0x778
+  __TEXT.__text: 0x12f570
+  __TEXT.__const: 0x11dc0
+  __TEXT.__cstring: 0x7a4f
+  __TEXT.__chain_starts: 0x50
+  __TEXT.__eh_frame: 0x40
   __DATA._rtk_boot: 0x3000
   __DATA.__mod_init_func: 0x258
   __DATA._rtk_page_tables: 0x6000
-  __DATA._spu_stack: 0x3000
-  __DATA._rtk_heap: 0x3b340
+  __DATA._spu_stack: 0x5000
   __DATA._rtk_init_stack: 0x2000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
-  __DATA.__const: 0x13dd8
+  __DATA._rtk_heap: 0x3b340
+  __DATA.__const: 0x132b8
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x64a0
-  __DATA._rtk_patchbay: 0x325
+  __DATA.__data: 0x7310
+  __DATA._rtk_patchbay: 0x319
   __DATA._rtk_power: 0x3b8
-  __DATA._spu_service: 0xb10
+  __DATA._spu_service: 0xa20
   __DATA._spu_endpoint: 0xd8
-  __DATA.__cmevent: 0x600
-  __DATA._rtk_mtab: 0x788
+  __DATA.__cmevent: 0x5d0
+  __DATA._rtk_mtab: 0x798
   __DATA._rtk_tunables: 0x5b0
   __DATA.__version: 0x8
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xdc590
-  __ETEXT.__StaticInit: 0x8490
-  __ETEXT.__text: 0x1d5dc
-  __ETEXT.__const: 0xd9e
-  __OS_LOG.__string: 0x26799
+  __DATA.__zerofill: 0xd0b70
+  __ETEXT.__StaticInit: 0x7648
+  __ETEXT.__text: 0x39b10
+  __ETEXT.__const: 0xdce
+  __EDATA.__data: 0x60
+  __OS_LOG.__string: 0x2789e
   __MISC.__apf_list: 0xb0
-  __CMA.__cma_log_string: 0x40da
+  __CMA.__cma_log_string: 0x3e24
   Symbols:   0
   Functions: 0
 

```

#### h16x_ane_fw_iaso_d8x.im4p

>  `h16x_ane_fw_iaso_d8x.im4p`

```diff

 
-  __TEXT.__text: 0xa53f8
+  __TEXT.__text: 0xadb24
   __TEXT.__data_copy: 0x8000
-  __TEXT.__const: 0x8388
-  __TEXT.__cstring: 0x19533
-  __TEXT._rtk_mtab: 0x288
+  __TEXT.__const: 0xc388
+  __TEXT.__cstring: 0x1ae59
+  __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x28
-  __DATA.__const: 0x4a90
+  __DATA.__const: 0x4bb8
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xf58
-  __DATA._rtk_patchbay: 0x1e8
+  __DATA._rtk_power: 0x368
+  __DATA._rtk_patchbay: 0x218
   __DATA._rtk_init_stack: 0x10000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
-  __DATA._rtk_power: 0x368
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_boot: 0x8000
-  __DATA._rtk_page_tables: 0x3c0000
+  __DATA._rtk_page_tables: 0x80000
   __DATA._rtk_threads: 0x0
   __DATA._fwinfo: 0x100
+  __DATA.__sysvars: 0x4
   __DATA._rtk_boot_l1: 0x80
   __DATA.__mod_init_func: 0x0
-  __DATA.__noinit: 0x0
-  __DATA.__zerofill: 0x53f28
+  __DATA.__zerofill: 0x53eb0
   Symbols:   0
   Functions: 0
 

```

#### rans.t8130.release.im4p

>  `rans.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x1727cc
-  __TEXT.shared: 0xb7b0
-  __TEXT.read: 0x59d0
-  __TEXT.__const: 0x8d68
+  __TEXT.__text: 0x171c60
+  __TEXT.shared: 0xb6e4
+  __TEXT.read: 0x5a78
+  __TEXT.__const: 0x8e58
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e5b9
+  __TEXT.__cstring: 0x1e59a
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
   __DATA._rtk_boot: 0x8000
   __DATA._rtk_power: 0x160
-  __DATA._rtk_patchbay: 0x3bf
+  __DATA._rtk_patchbay: 0x38f
   __DATA._rtk_tunables: 0x5b0
-  __DATA.__const: 0x1588
+  __DATA.__const: 0x15c8
   __DATA.__data: 0x5fd0
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_page_tables: 0x40000
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
   __DATA.core_globals: 0x138
-  __DATA.__zerofill: 0x19b818
+  __DATA.__zerofill: 0x19b788
   Symbols:   0
   Functions: 0
 

```

#### sptm.t8122.release.im4p

>  `sptm.t8122.release.im4p`

```diff

-194.122.2.0.0
-  __TEXT.__cstring: 0xa28d
+392.0.6.0.0
+  __TEXT.__cstring: 0xb986
   __TEXT.__binname: 0x40
-  __TEXT.__chain_starts: 0x1c
-  __TEXT.__const: 0x4b8
-  __DATA_CONST.__const: 0x4c638
-  __TEXT_EXEC.__text: 0x31c40
+  __TEXT.__chain_starts: 0x74
+  __TEXT.__const: 0x9d0
+  __DATA_CONST.__const: 0x63188
+  __TEXT_EXEC.__text: 0x3ff24
   __LAST.__pinst: 0x8
-  __DATA.__data: 0x16
-  __DATA.__common: 0x7150
-  __DATA.__bss: 0x4e70
+  __DATA.__auth_ptr: 0x18
+  __DATA.__data: 0x6
+  __DATA.__common: 0x71d0
+  __DATA.__bss: 0x56b0
   __BOOTDATA.__data: 0x14000
   Symbols:   1
   Functions: 0

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2b3084
-  __TEXT.__const: 0x7b21c
-  __TEXT.__cstring: 0x2d989
-  __TEXT.__chain_starts: 0x160
+  __TEXT.__text: 0x2dd3cc
+  __TEXT.__const: 0x7ce90
+  __TEXT.__cstring: 0x30d18
+  __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x47b08
+  __DATA.__const: 0x4a338
   __DATA._rtk_patchbay: 0x710
-  __DATA.__data: 0x2bac0
+  __DATA._rtk_data_uuid: 0x40
+  __DATA.__data: 0x2b4e4
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA._rtk_exc_stack: 0x1000
   __DATA.__afk_obj_num: 0x1f0
   __DATA._rtk_tunables: 0x5b0
-  __DATA._afk_sys_drv: 0xaa0
+  __DATA._afk_sys_drv: 0xac0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x90
-  __DATA._afk_sys_objt: 0xb60
-  __DATA._rtk_mtab: 0x5b0
-  __DATA.__zerofill: 0x9c868
-  __OS_LOG.__string: 0x1ed47
+  __DATA._afk_sys_objt: 0xbb0
+  __DATA._rtk_mtab: 0x5c8
+  __DATA.__zerofill: 0x9b6c0
+  __OS_LOG.__string: 0x20e8a
   Symbols:   0
   Functions: 0
 

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2b3084
-  __TEXT.__const: 0x7b21c
-  __TEXT.__cstring: 0x2d989
-  __TEXT.__chain_starts: 0x160
+  __TEXT.__text: 0x2dd3cc
+  __TEXT.__const: 0x7ce90
+  __TEXT.__cstring: 0x30d18
+  __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x47b08
+  __DATA.__const: 0x4a338
   __DATA._rtk_patchbay: 0x710
-  __DATA.__data: 0x2bac0
+  __DATA._rtk_data_uuid: 0x40
+  __DATA.__data: 0x2b4e4
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA._rtk_exc_stack: 0x1000
   __DATA.__afk_obj_num: 0x1f0
   __DATA._rtk_tunables: 0x5b0
-  __DATA._afk_sys_drv: 0xaa0
+  __DATA._afk_sys_drv: 0xac0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x90
-  __DATA._afk_sys_objt: 0xb60
-  __DATA._rtk_mtab: 0x5b0
-  __DATA.__zerofill: 0x9c868
-  __OS_LOG.__string: 0x1ed47
+  __DATA._afk_sys_objt: 0xbb0
+  __DATA._rtk_mtab: 0x5c8
+  __DATA.__zerofill: 0x9b6c0
+  __OS_LOG.__string: 0x20e8a
   Symbols:   0
   Functions: 0
 

```

#### t8130pmp.im4p

>  `t8130pmp.im4p`

```diff

 
-  __TEXT.__text: 0x34b40
-  __TEXT.__const: 0x1e90
-  __TEXT.__cstring: 0x15c4
+  __TEXT.__text: 0x36b5c
+  __TEXT.__const: 0x2300
+  __TEXT.__cstring: 0x1634
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
-  __TEXT._rtk_mtab: 0x5d0
-  __DATA.__const: 0x1e90
-  __DATA.__data: 0x6c78
+  __TEXT._rtk_mtab: 0x5e8
+  __DATA.__const: 0x1f10
+  __DATA.__data: 0x70a0
   __DATA._rtk_page_tables: 0x8000
   __DATA._rtk_boot: 0x1000
   __DATA._rtk_init_stack: 0x1800
   __DATA._rtk_irq_stack: 0x800
   __DATA._rtk_exc_stack: 0x800
-  __DATA._rtk_patchbay: 0x29c
+  __DATA._rtk_patchbay: 0x2a8
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_power: 0x358
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__mod_init_func: 0x10
-  __DATA.__zerofill: 0x4d0f0
+  __DATA.__zerofill: 0x4d3f0
   Symbols:   0
   Functions: 0
 

```

#### txm.iphoneos.release.im4p

>  `txm.iphoneos.release.im4p`

```diff

-89.120.2.0.0
-  __TEXT.__cstring: 0x46a2
-  __TEXT.__const: 0x33d0
+135.0.3.0.0
+  __TEXT.__cstring: 0x574c
+  __TEXT.__const: 0x4210
   __TEXT.__binname: 0x40
-  __TEXT.__chain_starts: 0x44
-  __TEXT.__info_plist: 0x4f3
-  __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x6c58
-  __TEXT_EXEC.__text: 0x3aafc
+  __TEXT.__chain_starts: 0x20
+  __TEXT.__info_plist: 0x4ff
+  __DATA_CONST.__auth_ptr: 0x50
+  __DATA_CONST.__const: 0x7d40
+  __TEXT_EXEC.__text: 0x3f10c
   __TEXT_BOOT_EXEC.__text: 0x4058
-  __TEXT_BOOT_EXEC.__bootcode: 0x20
-  __DATA.__data: 0x238
-  __DATA.__common: 0xa60
-  __DATA.__bss: 0x488
+  __TEXT_BOOT_EXEC.__bootcode: 0x2c
+  __DATA.__data: 0x278
+  __DATA.__common: 0xa70
+  __DATA.__bss: 0x490
   Symbols:   1
   Functions: 0
 

```


</details>

### Launchd

```diff

 			<key>Program</key>
 			<string>/usr/libexec/darwinos-boot-task</string>
 		</dict>
+		<key>select-boot-mode</key>
+		<dict>
+			<key>Block</key>
+			<string>select-boot-mode</string>
+			<key>PerformAfterUserspaceReboot</key>
+			<true/>
+		</dict>
 		<key>commit-boot-mode</key>
 		<dict>
 			<key>Block</key>

 			<key>PerformAlways</key>
 			<true/>
 		</dict>
+		<key>rem-enable-fuse</key>
+		<dict>
+			<key>Block</key>
+			<string>rem-enable-fuse</string>
+			<key>PerformAlways</key>
+			<true/>
+		</dict>
 		<key>detect-installed-roots</key>
 		<dict>
 			<key>Block</key>

```
## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.5.1 *(21F90)* | 618.2.12.10.9 |
| 18.0 *(22A5282m)* | 619.1.15.10.1 |

### Dylibs

#### 🆕 NEW (345)

<details>
  <summary><i>View NEW</i></summary>

- `/System/Library/AccessibilityBundles/ActionButtonConfigurationUI.axbundle/ActionButtonConfigurationUI`
- `/System/Library/AccessibilityBundles/DashBoard.axbundle/DashBoard`
- `/System/Library/AccessibilityBundles/MailAccountSettings.axbundle/MailAccountSettings`
- `/System/Library/AccessibilityBundles/MailUI.axbundle/MailUI`
- `/System/Library/AccessibilityBundles/MedicalIDUI.axbundle/MedicalIDUI`
- `/System/Library/AccessibilityBundles/Music.axbundle/Music`
- `/System/Library/AccessibilityBundles/PosterUIFoundation.axbundle/PosterUIFoundation`
- `/System/Library/AccessibilityBundles/StickerKit.axbundle/StickerKit`
- `/System/Library/AccessibilityBundles/iCloudSettings.axbundle/iCloudSettings`
- `/System/Library/ControlCenter/Bundles/AccessibilityHeadphoneLevelsControlCenterModule.bundle/AccessibilityHeadphoneLevelsControlCenterModule`
- `/System/Library/ControlCenter/Bundles/AccessibilityLiveListenControlCenterModule.bundle/AccessibilityLiveListenControlCenterModule`
- `/System/Library/ControlCenter/Bundles/AccessibilityMotionCuesControlCenterModule.bundle/AccessibilityMotionCuesControlCenterModule`
- `/System/Library/ControlCenter/Bundles/BackgroundSoundsCCModule.bundle/BackgroundSoundsCCModule`
- `/System/Library/ControlCenter/Bundles/HeadphoneAccommodationsCCModule.bundle/HeadphoneAccommodationsCCModule`
- `/System/Library/ControlCenter/Bundles/HearingDevicesCCModule.bundle/HearingDevicesCCModule`
- `/System/Library/ControlCenter/Bundles/HomeControlCenterSingleTileModule.bundle/HomeControlCenterSingleTileModule`
- `/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`
- `/System/Library/Frameworks/ContactProvider.framework/ContactProvider`
- `/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture`
- `/System/Library/Frameworks/StickerFoundation.framework/StickerFoundation`
- `/System/Library/Frameworks/StickerKit.framework/StickerKit`
- `/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore`
- `/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib`
- `/System/Library/Frameworks/_GameController_SwiftUI.framework/_GameController_SwiftUI`
- `/System/Library/Frameworks/_Intents_TipKit.framework/_Intents_TipKit`
- `/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion`
- `/System/Library/PrivateFrameworks/ALDataTypes.framework/ALDataTypes.dylib`
- `/System/Library/PrivateFrameworks/ANEClientSignals.framework/ANEClientSignals`
- `/System/Library/PrivateFrameworks/AONSense.framework/AONSense.dylib`
- `/System/Library/PrivateFrameworks/AXMotionCuesServices.framework/AXMotionCuesServices`
- `/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI`
- `/System/Library/PrivateFrameworks/AccountSuggestions.framework/AccountSuggestions`
- `/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings`
- `/System/Library/PrivateFrameworks/ActivityProgressKit.framework/ActivityProgressKit`
- `/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts`
- `/System/Library/PrivateFrameworks/AeroML.framework/AeroML`
- `/System/Library/PrivateFrameworks/AirDropSettingsSupport.framework/AirDropSettingsSupport`
- `/System/Library/PrivateFrameworks/AirPlayAndHandoffSettingsSupport.framework/AirPlayAndHandoffSettingsSupport`
- `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/AirPlaySenderKit`
- `/System/Library/PrivateFrameworks/AlarmUIFramework.framework/AlarmUIFramework`
- `/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices`
- `/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync`
- `/System/Library/PrivateFrameworks/AppPredictionToolsInternal.framework/AppPredictionToolsInternal`
- `/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`
- `/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI`
- `/System/Library/PrivateFrameworks/AppleBasebandLink.framework/AppleBasebandLink`
- `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport`
- `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libAppleDeviceQueryArmory.dylib`
- `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libAppleDeviceQueryRoster.dylib`
- `/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon`
- `/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter`
- `/System/Library/PrivateFrameworks/Archetype.framework/Archetype`
- `/System/Library/PrivateFrameworks/ArchetypeEngine.framework/ArchetypeEngine`
- `/System/Library/PrivateFrameworks/AssistantSettingsFoundation.framework/AssistantSettingsFoundation`
- `/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI`
- `/System/Library/PrivateFrameworks/AudioDSPGraph.framework/AudioDSPGraph`
- `/System/Library/PrivateFrameworks/BarcodeSupportUI.framework/BarcodeSupportUI`
- `/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard`
- `/System/Library/PrivateFrameworks/BlockMonitoring.framework/BlockMonitoring`
- `/System/Library/PrivateFrameworks/BridgeLiveActivity.framework/BridgeLiveActivity`
- `/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport`
- `/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport`
- `/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI`
- `/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/CalendarIntegrationSupport`
- `/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/CalendarUIKitInternal`
- `/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer`
- `/System/Library/PrivateFrameworks/ClockUIFramework.framework/ClockUIFramework`
- `/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets`
- `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`
- `/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI`
- `/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI`
- `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`
- `/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices`
- `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics`
- `/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib`
- `/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID`
- `/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles`
- `/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal`
- `/System/Library/PrivateFrameworks/DarwinDirectoryQuery.framework/DarwinDirectoryQuery`
- `/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents`
- `/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI`
- `/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing`
- `/System/Library/PrivateFrameworks/DeviceSharingServices.framework/DeviceSharingServices`
- `/System/Library/PrivateFrameworks/DeviceSharingUI.framework/DeviceSharingUI`
- `/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/DiagnosticsSessionAvailability`
- `/System/Library/PrivateFrameworks/DirectResource.framework/DirectResource`
- `/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers`
- `/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon`
- `/System/Library/PrivateFrameworks/DoubleAgent.framework/DoubleAgent`
- `/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI`
- `/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics`
- `/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit`
- `/System/Library/PrivateFrameworks/EnergyKitFoundation.framework/EnergyKitFoundation`
- `/System/Library/PrivateFrameworks/ExclaveFDRDecode.framework/ExclaveFDRDecode`
- `/System/Library/PrivateFrameworks/FPFS.framework/FPFS`
- `/System/Library/PrivateFrameworks/FaceTimeFeatureControl.framework/FaceTimeFeatureControl`
- `/System/Library/PrivateFrameworks/FedStats.framework/FedStats`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`
- `/System/Library/PrivateFrameworks/FitnessActions.framework/FitnessActions`
- `/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot`
- `/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset`
- `/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards`
- `/System/Library/PrivateFrameworks/FitnessBrowsing.framework/FitnessBrowsing`
- `/System/Library/PrivateFrameworks/FitnessCanvas.framework/FitnessCanvas`
- `/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI`
- `/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI`
- `/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering`
- `/System/Library/PrivateFrameworks/FitnessForYou.framework/FitnessForYou`
- `/System/Library/PrivateFrameworks/FitnessLibrary.framework/FitnessLibrary`
- `/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing`
- `/System/Library/PrivateFrameworks/FitnessOnboarding.framework/FitnessOnboarding`
- `/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail`
- `/System/Library/PrivateFrameworks/FitnessRemoteBrowsing.framework/FitnessRemoteBrowsing`
- `/System/Library/PrivateFrameworks/FitnessSearch.framework/FitnessSearch`
- `/System/Library/PrivateFrameworks/FitnessSharePlaySession.framework/FitnessSharePlaySession`
- `/System/Library/PrivateFrameworks/FitnessSiriSession.framework/FitnessSiriSession`
- `/System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities`
- `/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan`
- `/System/Library/PrivateFrameworks/FocusEngine.framework/FocusEngine`
- `/System/Library/PrivateFrameworks/FramePacing.framework/FramePacing`
- `/System/Library/PrivateFrameworks/GCoreFramework.framework/GCoreFramework`
- `/System/Library/PrivateFrameworks/GESS.framework/GESS`
- `/System/Library/PrivateFrameworks/GameServicesProtocols.framework/GameServicesProtocols`
- `/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences`
- `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime`
- `/System/Library/PrivateFrameworks/GenerativeFunctions.framework/GenerativeFunctions`
- `/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation`
- `/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation`
- `/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels`
- `/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation`
- `/System/Library/PrivateFrameworks/GenerativePlaygroundUI.framework/GenerativePlaygroundUI`
- `/System/Library/PrivateFrameworks/GeometryCompression.framework/GeometryCompression`
- `/System/Library/PrivateFrameworks/GraphComputeRT.framework/GraphComputeRT`
- `/System/Library/PrivateFrameworks/Hands.framework/Hands`
- `/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures`
- `/System/Library/PrivateFrameworks/HeadphoneDeviceTest.framework/HeadphoneDeviceTest`
- `/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager`
- `/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService`
- `/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance`
- `/System/Library/PrivateFrameworks/HealthBalanceAppPlugin.framework/HealthBalanceAppPlugin`
- `/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon`
- `/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI`
- `/System/Library/PrivateFrameworks/HealthDaemonFeatures.framework/HealthDaemonFeatures`
- `/System/Library/PrivateFrameworks/HealthFeatures.framework/HealthFeatures`
- `/System/Library/PrivateFrameworks/HealthMenstrualCyclesWidgetUI.framework/HealthMenstrualCyclesWidgetUI`
- `/System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration`
- `/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService`
- `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`
- `/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI`
- `/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI`
- `/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework`
- `/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2`
- `/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents`
- `/System/Library/PrivateFrameworks/IMRCSTransfer.framework/IMRCSTransfer`
- `/System/Library/PrivateFrameworks/IMTransferAgentClient.framework/IMTransferAgentClient`
- `/System/Library/PrivateFrameworks/IPConfiguration.framework/IPConfiguration`
- `/System/Library/PrivateFrameworks/IVRConversationAssistant.framework/IVRConversationAssistant`
- `/System/Library/PrivateFrameworks/ImageGenerationUI.framework/ImageGenerationUI`
- `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`
- `/System/Library/PrivateFrameworks/InputToolKit.framework/InputToolKit`
- `/System/Library/PrivateFrameworks/InputToolKitUI.framework/InputToolKitUI`
- `/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow`
- `/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext`
- `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime`
- `/System/Library/PrivateFrameworks/IntelligenceFlowFeedbackDataCollector.framework/IntelligenceFlowFeedbackDataCollector`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport`
- `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime`
- `/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared`
- `/System/Library/PrivateFrameworks/IntelligentRoutingMediaBundles.framework/IntelligentRoutingMediaBundles`
- `/System/Library/PrivateFrameworks/IntelligentRoutingServices.framework/IntelligentRoutingServices`
- `/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore`
- `/System/Library/PrivateFrameworks/JournalShared.framework/JournalShared`
- `/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings`
- `/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache`
- `/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport`
- `/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor`
- `/System/Library/PrivateFrameworks/LinkPresentationStyleSheetParsing.framework/LinkPresentationStyleSheetParsing`
- `/System/Library/PrivateFrameworks/LocalAuthenticationPreboard.framework/LocalAuthenticationPreboard`
- `/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices`
- `/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization`
- `/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32023/MTLCompiler`
- `/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler`
- `/System/Library/PrivateFrameworks/MagnifierServices.framework/MagnifierServices`
- `/System/Library/PrivateFrameworks/MathTypesetting.framework/MathTypesetting`
- `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/MediaAnalysisBlastDoorSupport`
- `/System/Library/PrivateFrameworks/MediaAnalysisPhotosServices.framework/MediaAnalysisPhotosServices`
- `/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI`
- `/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation`
- `/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`
- `/System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities`
- `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`
- `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime`
- `/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices`
- `/System/Library/PrivateFrameworks/ModelMonitoringLighthouse.framework/ModelMonitoringLighthouse`
- `/System/Library/PrivateFrameworks/NanoHomeIntents.framework/NanoHomeIntents`
- `/System/Library/PrivateFrameworks/NanoHomeScreenServices.framework/NanoHomeScreenServices`
- `/System/Library/PrivateFrameworks/NanoHomeScreenUIServices.framework/NanoHomeScreenUIServices`
- `/System/Library/PrivateFrameworks/NanoNetAppsUI.framework/NanoNetAppsUI`
- `/System/Library/PrivateFrameworks/NotesSiriUI.framework/NotesSiriUI`
- `/System/Library/PrivateFrameworks/NumberAdder.framework/NumberAdder`
- `/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch`
- `/System/Library/PrivateFrameworks/OmniSearchTypes.framework/OmniSearchTypes`
- `/System/Library/PrivateFrameworks/PacketParser.framework/PacketParser`
- `/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry`
- `/System/Library/PrivateFrameworks/ParsingInternal.framework/ParsingInternal`
- `/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse`
- `/System/Library/PrivateFrameworks/PeopleSuggesterMetrics.framework/PeopleSuggesterMetrics`
- `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing`
- `/System/Library/PrivateFrameworks/PhotoEditing.framework/PhotoEditing`
- `/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace`
- `/System/Library/PrivateFrameworks/PhotosFaceCore.framework/PhotosFaceCore`
- `/System/Library/PrivateFrameworks/PhotosFaceLayout.framework/PhotosFaceLayout`
- `/System/Library/PrivateFrameworks/PhotosFaceLayoutCore.framework/PhotosFaceLayoutCore`
- `/System/Library/PrivateFrameworks/PhotosIntelligenceCore.framework/PhotosIntelligenceCore`
- `/System/Library/PrivateFrameworks/PhotosMediaFoundation.framework/PhotosMediaFoundation`
- `/System/Library/PrivateFrameworks/PhotosSearchClient.framework/PhotosSearchClient`
- `/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore`
- `/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation`
- `/System/Library/PrivateFrameworks/Planks.framework/Planks`
- `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`
- `/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework`
- `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`
- `/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport`
- `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`
- `/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience`
- `/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended`
- `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute`
- `/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient`
- `/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/PrivateMLClientInferenceProvider`
- `/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport`
- `/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization`
- `/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient`
- `/System/Library/PrivateFrameworks/PromptKit.framework/PromptKit`
- `/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon`
- `/System/Library/PrivateFrameworks/RealityKitInspection.framework/RealityKitInspection`
- `/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents`
- `/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore`
- `/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine`
- `/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices`
- `/System/Library/PrivateFrameworks/ResponseUI.framework/ResponseUI`
- `/System/Library/PrivateFrameworks/SADSupport.framework/SADSupport`
- `/System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders`
- `/System/Library/PrivateFrameworks/Sage.framework/Sage`
- `/System/Library/PrivateFrameworks/SampleAnalysis.framework/Frameworks/SAHelper.framework/SAHelper`
- `/System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices`
- `/System/Library/PrivateFrameworks/ScreenSharingAccessibilityService.framework/ScreenSharingAccessibilityService`
- `/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit`
- `/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets`
- `/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics`
- `/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit`
- `/System/Library/PrivateFrameworks/SensingPredictServices.framework/SensingPredictServices`
- `/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting`
- `/System/Library/PrivateFrameworks/SentencePieceInternal.framework/SentencePieceInternal`
- `/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices`
- `/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph`
- `/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit`
- `/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices`
- `/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework`
- `/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete`
- `/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI`
- `/System/Library/PrivateFrameworks/SiriContactsCommon.framework/SiriContactsCommon`
- `/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI`
- `/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge`
- `/System/Library/PrivateFrameworks/SiriMailUIModel.framework/SiriMailUIModel`
- `/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI`
- `/System/Library/PrivateFrameworks/SiriOrchestration.framework/SiriOrchestration`
- `/System/Library/PrivateFrameworks/SiriOrchestrationServices.framework/SiriOrchestrationServices`
- `/System/Library/PrivateFrameworks/SiriSettingsUI.framework/SiriSettingsUI`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/SiriSuggestionsBaseModel`
- `/System/Library/PrivateFrameworks/SiriTranslationUI.framework/SiriTranslationUI`
- `/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework`
- `/System/Library/PrivateFrameworks/SpatialAudioServices.framework/SpatialAudioServices`
- `/System/Library/PrivateFrameworks/SpatialInspectorFoundation.framework/SpatialInspectorFoundation`
- `/System/Library/PrivateFrameworks/SpeakerRecognitionKit.framework/SpeakerRecognitionKit`
- `/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding`
- `/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge`
- `/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport`
- `/System/Library/PrivateFrameworks/SpringBoardDisplay.framework/SpringBoardDisplay`
- `/System/Library/PrivateFrameworks/SpringBoardDisplayServices.framework/SpringBoardDisplayServices`
- `/System/Library/PrivateFrameworks/StickerFoundationInternal.framework/StickerFoundationInternal`
- `/System/Library/PrivateFrameworks/StickerKitInternal.framework/StickerKitInternal`
- `/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization`
- `/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit`
- `/System/Library/PrivateFrameworks/SwiftASN1.framework/SwiftASN1`
- `/System/Library/PrivateFrameworks/SymptomLinkAdvisory.framework/SymptomLinkAdvisory`
- `/System/Library/PrivateFrameworks/SymptomShared.framework/SymptomShared`
- `/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit`
- `/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport`
- `/System/Library/PrivateFrameworks/TemporaryFramework.framework/TemporaryFramework`
- `/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI`
- `/System/Library/PrivateFrameworks/TextGeneration.framework/TextGeneration`
- `/System/Library/PrivateFrameworks/TextGenerationInference.framework/TextGenerationInference`
- `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/chs.dylib`
- `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/chsrom.dylib`
- `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/cht.dylib`
- `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/chtrom.dylib`
- `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/jpn.dylib`
- `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/jpnrom.dylib`
- `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/kor.dylib`
- `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/korrom.dylib`
- `/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration`
- `/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore`
- `/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference`
- `/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit`
- `/System/Library/PrivateFrameworks/TranslationAPISupport.framework/TranslationAPISupport`
- `/System/Library/PrivateFrameworks/TranslationPersistence.framework/TranslationPersistence`
- `/System/Library/PrivateFrameworks/Tungsten.framework/Tungsten`
- `/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents`
- `/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport`
- `/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent`
- `/System/Library/PrivateFrameworks/UINavigationKit.framework/UINavigationKit`
- `/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag`
- `/System/Library/PrivateFrameworks/UniversalHIDKit.framework/UniversalHIDKit`
- `/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices`
- `/System/Library/PrivateFrameworks/VFXAssets.framework/VFXAssets`
- `/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch`
- `/System/Library/PrivateFrameworks/Visage.framework/Visage`
- `/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration`
- `/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI`
- `/System/Library/PrivateFrameworks/VoiceProcessor.framework/VoiceProcessor`
- `/System/Library/PrivateFrameworks/WatchdogServiceManagement.framework/WatchdogServiceManagement`
- `/System/Library/PrivateFrameworks/WeatherAppSupport.framework/WeatherAppSupport`
- `/System/Library/PrivateFrameworks/WeatherData.framework/WeatherData`
- `/System/Library/PrivateFrameworks/WritingTools.framework/WritingTools`
- `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`
- `/System/Library/PrivateFrameworks/ZeoliteFramework.framework/ZeoliteFramework`
- `/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeRoster.dylib`
- `/System/Library/PrivateFrameworks/_AppIntentsServices_AppIntents.framework/_AppIntentsServices_AppIntents`
- `/System/Library/PrivateFrameworks/_SonicKit_MusicKit_Packages.framework/_SonicKit_MusicKit_Packages`
- `/System/Library/PrivateFrameworks/iCloudMailUnifiedSettings.framework/iCloudMailUnifiedSettings`
- `/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings`
- `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCollaborationKit.framework/TSCollaborationKit`
- `/System/Library/TextInput/TextInput_bn.bundle/TextInput_bn`
- `/System/Library/TextInput/TextInput_sl.bundle/TextInput_sl`
- `/usr/lib/libBasebandCommandDriversMIPC.dylib`
- `/usr/lib/libBasebandDiagnostics.dylib`
- `/usr/lib/libBasebandManagerDAL.dylib`
- `/usr/lib/libBasebandSharedServices.dylib`
- `/usr/lib/libMIPCSdk.dylib`
- `/usr/lib/libVinylNonUpdater.dylib`
- `/usr/lib/libswiftPrespecialized.dylib`
- `/usr/lib/swift/libswiftSynchronization.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`

</details>

#### ❌ Removed (37)

<details>
  <summary><i>View Removed</i></summary>

- `/System/Library/AccessibilityBundles/AXSpeechImplementation.bundle/AXSpeechImplementation`
- `/System/Library/ControlCenter/Bundles/AccessibilityGuidedAccessControlCenterModule.bundle/AccessibilityGuidedAccessControlCenterModule`
- `/System/Library/Messages/PlugIns/SMS.imservice/SMS`
- `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`
- `/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings`
- `/System/Library/PreferenceBundles/MobileCalSettings.bundle/MobileCalSettings`
- `/System/Library/PrivateFrameworks/AppleCV3DHA.framework/AppleCV3DHA`
- `/System/Library/PrivateFrameworks/BiomeSequence.framework/BiomeSequence`
- `/System/Library/PrivateFrameworks/CameraImagingFramework.framework/CameraImagingFramework`
- `/System/Library/PrivateFrameworks/ContactProvider.framework/ContactProvider`
- `/System/Library/PrivateFrameworks/ExpansionBoard.framework/ExpansionBoard`
- `/System/Library/PrivateFrameworks/GroupKit.framework/GroupKit`
- `/System/Library/PrivateFrameworks/GroupKitCore.framework/GroupKitCore`
- `/System/Library/PrivateFrameworks/HealthAppSupport.framework/HealthAppSupport`
- `/System/Library/PrivateFrameworks/HomeEnergy.framework/HomeEnergy`
- `/System/Library/PrivateFrameworks/LighthouseNightingale.framework/LighthouseNightingale`
- `/System/Library/PrivateFrameworks/MTLCompiler.framework/MTLCompiler`
- `/System/Library/PrivateFrameworks/PassKitCore_SoftLinking.framework/PassKitCore_SoftLinking`
- `/System/Library/PrivateFrameworks/PlacesKit.framework/PlacesKit`
- `/System/Library/PrivateFrameworks/RealityCamera.framework/AirPlayPlugin.rcplugin`
- `/System/Library/PrivateFrameworks/Settings/LegalAndRegulatorySettingsPrivate.framework/LegalAndRegulatorySettingsPrivate`
- `/System/Library/PrivateFrameworks/SiriAudioSnippetUI.framework/SiriAudioSnippetUI`
- `/System/Library/PrivateFrameworks/SnippetKit_Proto.framework/SnippetKit_Proto`
- `/System/Library/PrivateFrameworks/StateReplicator.framework/StateReplicator`
- `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomNetworkUsage.framework/SymptomNetworkUsage`
- `/System/Library/PrivateFrameworks/TipsNextServices.framework/TipsNextServices`
- `/System/Library/PrivateFrameworks/VFX.framework/Frameworks/libVFXCore.dylib`
- `/System/Library/PrivateFrameworks/VisageHRTF.framework/VisageHRTF`
- `/usr/lib/libBasebandDiagnostic.dylib`
- `/usr/lib/libThreadExternalCommissioner.dylib`
- `/usr/lib/libgraphcompute-rt.dylib`
- `/usr/lib/libipconfig.dylib`
- `/usr/lib/libmobileassetd.dylib`
- `/usr/lib/libomadm.dylib`
- `/usr/lib/swift/libswiftHomeKit.dylib`
- `/usr/lib/swift/libswiftIdentityLookup.dylib`
- `/usr/lib/swift/libswiftShazamKit.dylib`

</details>

#### ⬆️ Updated (3345)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ARKit.axbundle/ARKit](DYLIBS/ARKit.md)
- [/System/Library/AccessibilityBundles/ARTraceModule.axbundle/ARTraceModule](DYLIBS/ARTraceModule.md)
- [/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider](DYLIBS/ASMessagesProvider.md)
- [/System/Library/AccessibilityBundles/AVFoundation.axbundle/AVFoundation](DYLIBS/AVFoundation.md)
- [/System/Library/AccessibilityBundles/AVKit.axbundle/AVKit](DYLIBS/AVKit.md)
- [/System/Library/AccessibilityBundles/AXActionSheetUIServer.axuiservice/AXActionSheetUIServer](DYLIBS/AXActionSheetUIServer.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettings.axbundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/Library/AccessibilityBundles/AccountsUI.axbundle/AccountsUI](DYLIBS/AccountsUI.md)
- [/System/Library/AccessibilityBundles/AcousticId-Assistant.axbundle/AcousticId-Assistant](DYLIBS/AcousticId-Assistant.md)
- [/System/Library/AccessibilityBundles/ActionButtonSelector.axbundle/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/AccessibilityBundles/ActiveSyncSettings.axbundle/ActiveSyncSettings](DYLIBS/ActiveSyncSettings.md)
- [/System/Library/AccessibilityBundles/ActivityUIServices.axbundle/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/AccessibilityBundles/AddressBook-Assistant.axbundle/AddressBook-Assistant](DYLIBS/AddressBook-Assistant.md)
- [/System/Library/AccessibilityBundles/AddressBookUIFramework.axbundle/AddressBookUIFramework](DYLIBS/AddressBookUIFramework.md)
- [/System/Library/AccessibilityBundles/AirDrop.axbundle/AirDrop](DYLIBS/AirDrop.md)
- [/System/Library/AccessibilityBundles/AirDropUI.axbundle/AirDropUI](DYLIBS/AirDropUI.md)
- [/System/Library/AccessibilityBundles/AirPlayMirroringModule.axbundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule.md)
- [/System/Library/AccessibilityBundles/AirPortSettings.axbundle/AirPortSettings](DYLIBS/AirPortSettings.md)
- [/System/Library/AccessibilityBundles/AirTrafficSettings.axbundle/AirTrafficSettings](DYLIBS/AirTrafficSettings.md)
- [/System/Library/AccessibilityBundles/AmbientUI.axbundle/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/AccessibilityBundles/Animoji.axbundle/Animoji](DYLIBS/Animoji.md)
- [/System/Library/AccessibilityBundles/AnnotationKit.axbundle/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension](DYLIBS/AppInstallExtension.md)
- [/System/Library/AccessibilityBundles/AppPredictionUI.axbundle/AppPredictionUI](DYLIBS/AppPredictionUI.md)
- [/System/Library/AccessibilityBundles/AppPredictionUIWidget.axbundle/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget.md)
- [/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore](DYLIBS/AppStore.md)
- [/System/Library/AccessibilityBundles/AppearanceModule.axbundle/AppearanceModule](DYLIBS/AppearanceModule.md)
- [/System/Library/AccessibilityBundles/AppleAccountSettings.axbundle/AppleAccountSettings](DYLIBS/AppleAccountSettings.md)
- [/System/Library/AccessibilityBundles/AppleAccountUI.axbundle/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/AccessibilityBundles/AppleMediaServicesUI.axbundle/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/AccessibilityBundles/AppleTV.axbundle/AppleTV](DYLIBS/AppleTV.md)
- [/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade](DYLIBS/Arcade.md)
- [/System/Library/AccessibilityBundles/AssetExplorer.axbundle/AssetExplorer](DYLIBS/AssetExplorer.md)
- [/System/Library/AccessibilityBundles/AssetViewer.axbundle/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/AccessibilityBundles/AssistantServices.axbundle/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/AccessibilityBundles/AssistantUI.axbundle/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/AccessibilityBundles/AttributionWeeApp.axbundle/AttributionWeeApp](DYLIBS/AttributionWeeApp.md)
- [/System/Library/AccessibilityBundles/Audio-QuickLook.axbundle/Audio-QuickLook](DYLIBS/Audio-QuickLook.md)
- [/System/Library/AccessibilityBundles/AuthKitUI.axbundle/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/AccessibilityBundles/AuthenticationServices.axbundle/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/AccessibilityBundles/AvatarKit.axbundle/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/AccessibilityBundles/AvatarPickerMemojiPicker.axbundle/AvatarPickerMemojiPicker](DYLIBS/AvatarPickerMemojiPicker.md)
- [/System/Library/AccessibilityBundles/AvatarUI.axbundle/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/AccessibilityBundles/BPSStingSetup.axbundle/BPSStingSetup](DYLIBS/BPSStingSetup.md)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/BannerKit.axbundle/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/AccessibilityBundles/BarcodeScanner.axbundle/BarcodeScanner](DYLIBS/BarcodeScanner.md)
- [/System/Library/AccessibilityBundles/BaseBoardUI.axbundle/BaseBoardUI](DYLIBS/BaseBoardUI.md)
- [/System/Library/AccessibilityBundles/BatteryCenterUI.axbundle/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/AccessibilityBundles/BatteryUsageUI.axbundle/BatteryUsageUI](DYLIBS/BatteryUsageUI.md)
- [/System/Library/AccessibilityBundles/BatteryWidget.axbundle/BatteryWidget](DYLIBS/BatteryWidget.md)
- [/System/Library/AccessibilityBundles/BiometricKitUI.axbundle/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/AccessibilityBundles/BluetoothSettings.axbundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/AccessibilityBundles/Bridge.axbundle/Bridge](DYLIBS/Bridge.md)
- [/System/Library/AccessibilityBundles/BridgePreferences.axbundle/BridgePreferences](DYLIBS/BridgePreferences.md)
- [/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension](DYLIBS/BridgeStoreExtension.md)
- [/System/Library/AccessibilityBundles/Business.axbundle/Business](DYLIBS/Business.md)
- [/System/Library/AccessibilityBundles/BusinessChatFramework.axbundle/BusinessChatFramework](DYLIBS/BusinessChatFramework.md)
- [/System/Library/AccessibilityBundles/CARDNDUI.axbundle/CARDNDUI](DYLIBS/CARDNDUI.md)
- [/System/Library/AccessibilityBundles/Calculator.axbundle/Calculator](DYLIBS/Calculator.md)
- [/System/Library/AccessibilityBundles/Calendar-Assistant.axbundle/Calendar-Assistant](DYLIBS/Calendar-Assistant.md)
- [/System/Library/AccessibilityBundles/Camera.axbundle/Camera](DYLIBS/Camera.md)
- [/System/Library/AccessibilityBundles/CameraEditKitFramework.axbundle/CameraEditKitFramework](DYLIBS/CameraEditKitFramework.md)
- [/System/Library/AccessibilityBundles/CameraEffectsKit.axbundle/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/AccessibilityBundles/CameraKit.axbundle/CameraKit](DYLIBS/CameraKit.md)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/AccessibilityBundles/CarModeModule.axbundle/CarModeModule](DYLIBS/CarModeModule.md)
- [/System/Library/AccessibilityBundles/CarPlay.axbundle/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/AccessibilityBundles/CardKit.axbundle/CardKit](DYLIBS/CardKit.md)
- [/System/Library/AccessibilityBundles/CarouselAppViewSettings.axbundle/CarouselAppViewSettings](DYLIBS/CarouselAppViewSettings.md)
- [/System/Library/AccessibilityBundles/CertInfo.axbundle/CertInfo](DYLIBS/CertInfo.md)
- [/System/Library/AccessibilityBundles/ChargingViewService.axbundle/ChargingViewService](DYLIBS/ChargingViewService.md)
- [/System/Library/AccessibilityBundles/ChatKitAssistantUI-Assistant.axbundle/ChatKitAssistantUI-Assistant](DYLIBS/ChatKitAssistantUI-Assistant.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/CheckerBoard.axbundle/CheckerBoard](DYLIBS/CheckerBoard.md)
- [/System/Library/AccessibilityBundles/ChronoCore.axbundle/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/AccessibilityBundles/ClipUIServices.axbundle/ClipUIServices](DYLIBS/ClipUIServices.md)
- [/System/Library/AccessibilityBundles/ClockPoster.axbundle/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/AccessibilityBundles/CommunicationsSetupUI.axbundle/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/AccessibilityBundles/CompanionAppViewSetup.axbundle/CompanionAppViewSetup](DYLIBS/CompanionAppViewSetup.md)
- [/System/Library/AccessibilityBundles/CompanionStingSettings.axbundle/CompanionStingSettings](DYLIBS/CompanionStingSettings.md)
- [/System/Library/AccessibilityBundles/Compass.axbundle/Compass](DYLIBS/Compass.md)
- [/System/Library/AccessibilityBundles/CompassViewCalibrationService.axbundle/CompassViewCalibrationService](DYLIBS/CompassViewCalibrationService.md)
- [/System/Library/AccessibilityBundles/ConnectivityModule.axbundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/AccessibilityBundles/ContactsAutocompleteUI.axbundle/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/AccessibilityBundles/ContactsUI.axbundle/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/AccessibilityBundles/ContinuityDisplay.axbundle/ContinuityDisplay](DYLIBS/ContinuityDisplay.md)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/AccessibilityBundles/ConversationKit.axbundle/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/AccessibilityBundles/CoreAuthUI.axbundle/CoreAuthUI](DYLIBS/CoreAuthUI.md)
- [/System/Library/AccessibilityBundles/CoreCDPUI.axbundle/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/AccessibilityBundles/CoreDynamicUIPlugin.axbundle/CoreDynamicUIPlugin](DYLIBS/CoreDynamicUIPlugin.md)
- [/System/Library/AccessibilityBundles/CoreIDVRGBLiveness.axbundle/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/AccessibilityBundles/CoreIDVUI.axbundle/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/AccessibilityBundles/CoreRecognition.axbundle/CoreRecognition](DYLIBS/CoreRecognition.md)
- [/System/Library/AccessibilityBundles/CoreSuggestionsUI.axbundle/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/AccessibilityBundles/CoverSheetKit.axbundle/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/AccessibilityBundles/DDActionsService.axbundle/DDActionsService](DYLIBS/DDActionsService.md)
- [/System/Library/AccessibilityBundles/DataActivation.axbundle/DataActivation](DYLIBS/DataActivation.md)
- [/System/Library/AccessibilityBundles/DefaultMediaPlayer-QuickLook.axbundle/DefaultMediaPlayer-QuickLook](DYLIBS/DefaultMediaPlayer-QuickLook.md)
- [/System/Library/AccessibilityBundles/Diagnostics.axbundle/Diagnostics](DYLIBS/Diagnostics.md)
- [/System/Library/AccessibilityBundles/DictionarySettings.axbundle/DictionarySettings](DYLIBS/DictionarySettings.md)
- [/System/Library/AccessibilityBundles/DigitalSeparationSettings.axbundle/DigitalSeparationSettings](DYLIBS/DigitalSeparationSettings.md)
- [/System/Library/AccessibilityBundles/DigitalTouchBalloonProvider.axbundle/DigitalTouchBalloonProvider](DYLIBS/DigitalTouchBalloonProvider.md)
- [/System/Library/AccessibilityBundles/DigitalTouchShared.axbundle/DigitalTouchShared](DYLIBS/DigitalTouchShared.md)
- [/System/Library/AccessibilityBundles/DisplayAndBrightnessSettings.axbundle/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/AccessibilityBundles/DisplayModule.axbundle/DisplayModule](DYLIBS/DisplayModule.md)
- [/System/Library/AccessibilityBundles/DoNotDisturbModule.axbundle/DoNotDisturbModule](DYLIBS/DoNotDisturbModule.md)
- [/System/Library/AccessibilityBundles/DoNotDisturbSettings.axbundle/DoNotDisturbSettings](DYLIBS/DoNotDisturbSettings.md)
- [/System/Library/AccessibilityBundles/DocumentManager.axbundle/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/AccessibilityBundles/DocumentManagerExecutables.axbundle/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/AccessibilityBundles/DocumentManagerUICore.axbundle/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/AccessibilityBundles/DrawingKit.axbundle/DrawingKit](DYLIBS/DrawingKit.md)
- [/System/Library/AccessibilityBundles/EmojiKit.axbundle/EmojiKit](DYLIBS/EmojiKit.md)
- [/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/EventKitUIFramework](DYLIBS/EventKitUIFramework.md)
- [/System/Library/AccessibilityBundles/ExposureNotificationSettingsUI.axbundle/ExposureNotificationSettingsUI](DYLIBS/ExposureNotificationSettingsUI.md)
- [/System/Library/AccessibilityBundles/FMFindingUI.axbundle/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/AccessibilityBundles/FaceTime.axbundle/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/AccessibilityBundles/FacebookSettings.axbundle/FacebookSettings](DYLIBS/FacebookSettings.md)
- [/System/Library/AccessibilityBundles/Files.axbundle/Files](DYLIBS/Files.md)
- [/System/Library/AccessibilityBundles/FindMy.axbundle/FindMy](DYLIBS/FindMy.md)
- [/System/Library/AccessibilityBundles/FlashlightModule.axbundle/FlashlightModule](DYLIBS/FlashlightModule.md)
- [/System/Library/AccessibilityBundles/FlightUtilities.axbundle/FlightUtilities](DYLIBS/FlightUtilities.md)
- [/System/Library/AccessibilityBundles/FocusUI.axbundle/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/AccessibilityBundles/FocusUIModule.axbundle/FocusUIModule](DYLIBS/FocusUIModule.md)
- [/System/Library/AccessibilityBundles/FontPicker.axbundle/FontPicker](DYLIBS/FontPicker.md)
- [/System/Library/AccessibilityBundles/FrontBoard.axbundle/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/AccessibilityBundles/Game Center.axbundle/Game Center](DYLIBS/Game_Center.md)
- [/System/Library/AccessibilityBundles/GameCenterDashboardExtension.axbundle/GameCenterDashboardExtension](DYLIBS/GameCenterDashboardExtension.md)
- [/System/Library/AccessibilityBundles/GameCenterPrivateUIFramework.axbundle/GameCenterPrivateUIFramework](DYLIBS/GameCenterPrivateUIFramework.md)
- [/System/Library/AccessibilityBundles/GameCenterUIFramework.axbundle/GameCenterUIFramework](DYLIBS/GameCenterUIFramework.md)
- [/System/Library/AccessibilityBundles/GameCenterUIService.axbundle/GameCenterUIService](DYLIBS/GameCenterUIService.md)
- [/System/Library/AccessibilityBundles/GameKitFramework.axbundle/GameKitFramework](DYLIBS/GameKitFramework.md)
- [/System/Library/AccessibilityBundles/GeneralKnowledge-Assistant.axbundle/GeneralKnowledge-Assistant](DYLIBS/GeneralKnowledge-Assistant.md)
- [/System/Library/AccessibilityBundles/GeneralSettingsUI.axbundle/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/AccessibilityBundles/GeoServices.axbundle/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/AccessibilityBundles/Gif-QuickLook.axbundle/Gif-QuickLook](DYLIBS/Gif-QuickLook.md)
- [/System/Library/AccessibilityBundles/HDSViewService.axbundle/HDSViewService](DYLIBS/HDSViewService.md)
- [/System/Library/AccessibilityBundles/HandwritingProvider.axbundle/HandwritingProvider](DYLIBS/HandwritingProvider.md)
- [/System/Library/AccessibilityBundles/HashtagImagesExtension.axbundle/HashtagImagesExtension](DYLIBS/HashtagImagesExtension.md)
- [/System/Library/AccessibilityBundles/HeadphoneConfigs.axbundle/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/AccessibilityBundles/HealthArticlesUI.axbundle/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/AccessibilityBundles/HealthExperienceUI.axbundle/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/AccessibilityBundles/HealthExposureNotificationUI.axbundle/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/AccessibilityBundles/HealthKit.axbundle/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/AccessibilityBundles/HealthKitUI.axbundle/HealthKitUI](DYLIBS/HealthKitUI.md)
- [/System/Library/AccessibilityBundles/HealthMedicationsUI.axbundle/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/AccessibilityBundles/HealthRecordsUI.axbundle/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/AccessibilityBundles/HealthSafety.axbundle/HealthSafety](DYLIBS/HealthSafety.md)
- [/System/Library/AccessibilityBundles/HealthToolbox.axbundle/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/AccessibilityBundles/HealthUI.axbundle/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/AccessibilityBundles/HealthVisualization.axbundle/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/AccessibilityBundles/HearingAidUIServer.axuiservice/HearingAidUIServer](DYLIBS/HearingAidUIServer.md)
- [/System/Library/AccessibilityBundles/HeartRhythmUI.axbundle/HeartRhythmUI](DYLIBS/HeartRhythmUI.md)
- [/System/Library/AccessibilityBundles/HelpKit.axbundle/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/AccessibilityBundles/Home.axbundle/Home](DYLIBS/Home.md)
- [/System/Library/AccessibilityBundles/HomeControlCenterCompactModule.axbundle/HomeControlCenterCompactModule](DYLIBS/HomeControlCenterCompactModule.md)
- [/System/Library/AccessibilityBundles/HomeControlCenterModule.axbundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/AccessibilityBundles/HomeControlService.axbundle/HomeControlService](DYLIBS/HomeControlService.md)
- [/System/Library/AccessibilityBundles/HomeUI.axbundle/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/AccessibilityBundles/HomeUIService.axbundle/HomeUIService](DYLIBS/HomeUIService.md)
- [/System/Library/AccessibilityBundles/Image-QuickLook.axbundle/Image-QuickLook](DYLIBS/Image-QuickLook.md)
- [/System/Library/AccessibilityBundles/InCallLockScreen.axbundle/InCallLockScreen](DYLIBS/InCallLockScreen.md)
- [/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService](DYLIBS/InCallService.md)
- [/System/Library/AccessibilityBundles/IncomingCall.axbundle/IncomingCall](DYLIBS/IncomingCall.md)
- [/System/Library/AccessibilityBundles/InputUI.axbundle/InputUI](DYLIBS/InputUI.md)
- [/System/Library/AccessibilityBundles/IntentsUI.axbundle/IntentsUI](DYLIBS/IntentsUI.md)
- [/System/Library/AccessibilityBundles/InternationalSettings.axbundle/InternationalSettings](DYLIBS/InternationalSettings.md)
- [/System/Library/AccessibilityBundles/KeyboardSettings.axbundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/AccessibilityBundles/LinkPresentation.axbundle/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/AccessibilityBundles/LiveTranscriptionUI.axbundle/LiveTranscriptionUI](DYLIBS/LiveTranscriptionUI.md)
- [/System/Library/AccessibilityBundles/LocalAuthenticationRGBCapture.axbundle/LocalAuthenticationRGBCapture](DYLIBS/LocalAuthenticationRGBCapture.md)
- [/System/Library/AccessibilityBundles/LocalAuthenticationUI.axbundle/LocalAuthenticationUI](DYLIBS/LocalAuthenticationUI.md)
- [/System/Library/AccessibilityBundles/LoginUI.axbundle/LoginUI](DYLIBS/LoginUI.md)
- [/System/Library/AccessibilityBundles/Mail-Assistant.axbundle/Mail-Assistant](DYLIBS/Mail-Assistant.md)
- [/System/Library/AccessibilityBundles/MailAttachmentPlugin.axbundle/MailAttachmentPlugin](DYLIBS/MailAttachmentPlugin.md)
- [/System/Library/AccessibilityBundles/MailVIPWidget.axbundle/MailVIPWidget](DYLIBS/MailVIPWidget.md)
- [/System/Library/AccessibilityBundles/ManagedConfigurationUI.axbundle/ManagedConfigurationUI](DYLIBS/ManagedConfigurationUI.md)
- [/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework](DYLIBS/MapKitFramework.md)
- [/System/Library/AccessibilityBundles/MapKitSwiftUI.axbundle/MapKitSwiftUI](DYLIBS/MapKitSwiftUI.md)
- [/System/Library/AccessibilityBundles/Maps-Assistant.axbundle/Maps-Assistant](DYLIBS/Maps-Assistant.md)
- [/System/Library/AccessibilityBundles/Maps.axbundle/Maps](DYLIBS/Maps.md)
- [/System/Library/AccessibilityBundles/MapsUI.axbundle/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/AccessibilityBundles/MarkupUI.axbundle/MarkupUI](DYLIBS/MarkupUI.md)
- [/System/Library/AccessibilityBundles/Measure.axbundle/Measure](DYLIBS/Measure.md)
- [/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/AccessibilityBundles/MediaPlayerFramework.axbundle/MediaPlayerFramework](DYLIBS/MediaPlayerFramework.md)
- [/System/Library/AccessibilityBundles/MediaPlayerUIFramework.axbundle/MediaPlayerUIFramework](DYLIBS/MediaPlayerUIFramework.md)
- [/System/Library/AccessibilityBundles/MedicationsHealthAppPlugin.axbundle/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/AccessibilityBundles/Memories.axbundle/Memories](DYLIBS/Memories.md)
- [/System/Library/AccessibilityBundles/MenstrualCyclesAppPlugin.axbundle/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/MessageUIFramework](DYLIBS/MessageUIFramework.md)
- [/System/Library/AccessibilityBundles/Messages.axbundle/Messages](DYLIBS/Messages.md)
- [/System/Library/AccessibilityBundles/MessagesFlowDelegatePlugin.axbundle/MessagesFlowDelegatePlugin](DYLIBS/MessagesFlowDelegatePlugin.md)
- [/System/Library/AccessibilityBundles/MobileCal.axbundle/MobileCal](DYLIBS/MobileCal.md)
- [/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail](DYLIBS/MobileMail.md)
- [/System/Library/AccessibilityBundles/MobileMailSettings.axbundle/MobileMailSettings](DYLIBS/MobileMailSettings.md)
- [/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone](DYLIBS/MobilePhone.md)
- [/System/Library/AccessibilityBundles/MobileSMS.axbundle/MobileSMS](DYLIBS/MobileSMS.md)
- [/System/Library/AccessibilityBundles/MobileSafari.axbundle/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework](DYLIBS/MobileSafariFramework.md)
- [/System/Library/AccessibilityBundles/MobileSafariSettings.axbundle/MobileSafariSettings](DYLIBS/MobileSafariSettings.md)
- [/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/AccessibilityBundles/MobileSlideShow.axbundle/MobileSlideShow](DYLIBS/MobileSlideShow.md)
- [/System/Library/AccessibilityBundles/MobileStore.axbundle/MobileStore](DYLIBS/MobileStore.md)
- [/System/Library/AccessibilityBundles/MobileStoreUI.axbundle/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/AccessibilityBundles/MobileTimer-Assistant.axbundle/MobileTimer-Assistant](DYLIBS/MobileTimer-Assistant.md)
- [/System/Library/AccessibilityBundles/MobileTimer.axbundle/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/AccessibilityBundles/MobileTimerFramework.axbundle/MobileTimerFramework](DYLIBS/MobileTimerFramework.md)
- [/System/Library/AccessibilityBundles/MobileTimerUIFramework.axbundle/MobileTimerUIFramework](DYLIBS/MobileTimerUIFramework.md)
- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/AccessibilityBundles/MonogramPosterExtension.axbundle/MonogramPosterExtension](DYLIBS/MonogramPosterExtension.md)
- [/System/Library/AccessibilityBundles/Movie-QuickLook.axbundle/Movie-QuickLook](DYLIBS/Movie-QuickLook.md)
- [/System/Library/AccessibilityBundles/Movies-Assistant.axbundle/Movies-Assistant](DYLIBS/Movies-Assistant.md)
- [/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication](DYLIBS/MusicApplication.md)
- [/System/Library/AccessibilityBundles/MusicMessagesApp.axbundle/MusicMessagesApp](DYLIBS/MusicMessagesApp.md)
- [/System/Library/AccessibilityBundles/MusicRecognition.axbundle/MusicRecognition](DYLIBS/MusicRecognition.md)
- [/System/Library/AccessibilityBundles/MusicSettings.axbundle/MusicSettings](DYLIBS/MusicSettings.md)
- [/System/Library/AccessibilityBundles/MusicUI.axbundle/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/AccessibilityBundles/MusicUsage.axbundle/MusicUsage](DYLIBS/MusicUsage.md)
- [/System/Library/AccessibilityBundles/MuteModule.axbundle/MuteModule](DYLIBS/MuteModule.md)
- [/System/Library/AccessibilityBundles/NFCControlCenterModule.axbundle/NFCControlCenterModule](DYLIBS/NFCControlCenterModule.md)
- [/System/Library/AccessibilityBundles/Nearby.axbundle/Nearby](DYLIBS/Nearby.md)
- [/System/Library/AccessibilityBundles/NotificationCenter.axbundle/NotificationCenter](DYLIBS/NotificationCenter.md)
- [/System/Library/AccessibilityBundles/NotificationsSettings.axbundle/NotificationsSettings](DYLIBS/NotificationsSettings.md)
- [/System/Library/AccessibilityBundles/OnBoardingKit.axbundle/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/AccessibilityBundles/OpusKit.axbundle/OpusKit](DYLIBS/OpusKit.md)
- [/System/Library/AccessibilityBundles/OrientationLockModule.axbundle/OrientationLockModule](DYLIBS/OrientationLockModule.md)
- [/System/Library/AccessibilityBundles/PDFKit.axbundle/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/AccessibilityBundles/PaperKit.axbundle/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/AccessibilityBundles/PassKitFramework.axbundle/PassKitFramework](DYLIBS/PassKitFramework.md)
- [/System/Library/AccessibilityBundles/PassKitUI.axbundle/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/AccessibilityBundles/PassesLockScreenPlugin.axbundle/PassesLockScreenPlugin](DYLIBS/PassesLockScreenPlugin.md)
- [/System/Library/AccessibilityBundles/PeerPaymentMessagesExtension.axbundle/PeerPaymentMessagesExtension](DYLIBS/PeerPaymentMessagesExtension.md)
- [/System/Library/AccessibilityBundles/Pegasus.axbundle/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/AccessibilityBundles/PerformanceTraceModule.axbundle/PerformanceTraceModule](DYLIBS/PerformanceTraceModule.md)
- [/System/Library/AccessibilityBundles/PhoneCallFlowDelegatePlugin.axbundle/PhoneCallFlowDelegatePlugin](DYLIBS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/AccessibilityBundles/Photo Booth.axbundle/Photo Booth](DYLIBS/Photo_Booth.md)
- [/System/Library/AccessibilityBundles/PhotoLibraryFramework.axbundle/PhotoLibraryFramework](DYLIBS/PhotoLibraryFramework.md)
- [/System/Library/AccessibilityBundles/PhotoLibraryServices.axbundle/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/AccessibilityBundles/PhotosEditUI.axbundle/PhotosEditUI](DYLIBS/PhotosEditUI.md)
- [/System/Library/AccessibilityBundles/PhotosFramework.axbundle/PhotosFramework](DYLIBS/PhotosFramework.md)
- [/System/Library/AccessibilityBundles/PhotosUICore.axbundle/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/Library/AccessibilityBundles/PlatterKit.axbundle/PlatterKit](DYLIBS/PlatterKit.md)
- [/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/AccessibilityBundles/PodcastsPodcastsTodayExtension.axbundle/PodcastsPodcastsTodayExtension](DYLIBS/PodcastsPodcastsTodayExtension.md)
- [/System/Library/AccessibilityBundles/PosterBoard.axbundle/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework](DYLIBS/PosterBoardFramework.md)
- [/System/Library/AccessibilityBundles/PosterKit.axbundle/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/AccessibilityBundles/PreBoard.axbundle/PreBoard](DYLIBS/PreBoard.md)
- [/System/Library/AccessibilityBundles/Preferences.axbundle/Preferences](DYLIBS/Preferences.md)
- [/System/Library/AccessibilityBundles/PreferencesFramework.axbundle/PreferencesFramework](DYLIBS/PreferencesFramework.md)
- [/System/Library/AccessibilityBundles/PreferencesUI.axbundle/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/AccessibilityBundles/PreviewUI.axbundle/PreviewUI](DYLIBS/PreviewUI.md)
- [/System/Library/AccessibilityBundles/PrintKitUI.axbundle/PrintKitUI](DYLIBS/PrintKitUI.md)
- [/System/Library/AccessibilityBundles/PrivacySettingsUI.axbundle/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension](DYLIBS/ProductPageExtension.md)
- [/System/Library/AccessibilityBundles/ProxCardKit.axbundle/ProxCardKit](DYLIBS/ProxCardKit.md)
- [/System/Library/AccessibilityBundles/QuickLook.axbundle/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/AccessibilityBundles/QuickSpeak.bundle/QuickSpeak](DYLIBS/QuickSpeak.md)
- [/System/Library/AccessibilityBundles/QuickTime Plugin.axbundle/QuickTime Plugin](DYLIBS/QuickTime_Plugin.md)
- [/System/Library/AccessibilityBundles/RealityFoundation.axbundle/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/AccessibilityBundles/RealityKit.axbundle/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/AccessibilityBundles/RecentlyPlayedTodayExtension.axbundle/RecentlyPlayedTodayExtension](DYLIBS/RecentlyPlayedTodayExtension.md)
- [/System/Library/AccessibilityBundles/RecentsAvocado.axbundle/RecentsAvocado](DYLIBS/RecentsAvocado.md)
- [/System/Library/AccessibilityBundles/RemoteUIFramework.axbundle/RemoteUIFramework](DYLIBS/RemoteUIFramework.md)
- [/System/Library/AccessibilityBundles/ReplayKitModule.axbundle/ReplayKitModule](DYLIBS/ReplayKitModule.md)
- [/System/Library/AccessibilityBundles/Restaurants-Assistant.axbundle/Restaurants-Assistant](DYLIBS/Restaurants-Assistant.md)
- [/System/Library/AccessibilityBundles/SIMSetupSupport.axbundle/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/AccessibilityBundles/SIMSetupUIService.axbundle/SIMSetupUIService](DYLIBS/SIMSetupUIService.md)
- [/System/Library/AccessibilityBundles/SOSSettings.axbundle/SOSSettings](DYLIBS/SOSSettings.md)
- [/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/AccessibilityBundles/SafariSharedUI.axbundle/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/AccessibilityBundles/SaveToFiles.axbundle/SaveToFiles](DYLIBS/SaveToFiles.md)
- [/System/Library/AccessibilityBundles/SceneKit.axbundle/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/AccessibilityBundles/ScreenTimeSettingsUI.axbundle/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/AccessibilityBundles/ScreenTimeUI.axbundle/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/AccessibilityBundles/ScreenshotServicesFramework.axbundle/ScreenshotServicesFramework](DYLIBS/ScreenshotServicesFramework.md)
- [/System/Library/AccessibilityBundles/ScreenshotServicesService.axbundle/ScreenshotServicesService](DYLIBS/ScreenshotServicesService.md)
- [/System/Library/AccessibilityBundles/SearchFoundation.axbundle/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/AccessibilityBundles/SearchSettings.axbundle/SearchSettings](DYLIBS/SearchSettings.md)
- [/System/Library/AccessibilityBundles/SearchUI.axbundle/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/AccessibilityBundles/Settings-Assistant.axbundle/Settings-Assistant](DYLIBS/Settings-Assistant.md)
- [/System/Library/AccessibilityBundles/Setup.axbundle/Setup](DYLIBS/Setup.md)
- [/System/Library/AccessibilityBundles/SetupAssistantUI.axbundle/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/AccessibilityBundles/SeymourUI.axbundle/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/AccessibilityBundles/ShareSheet.axbundle/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/AccessibilityBundles/SharedWithYouFramework.axbundle/SharedWithYouFramework](DYLIBS/SharedWithYouFramework.md)
- [/System/Library/AccessibilityBundles/SharingUI.axbundle/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/AccessibilityBundles/SharingViewService.axbundle/SharingViewService](DYLIBS/SharingViewService.md)
- [/System/Library/AccessibilityBundles/Shortcuts.axbundle/Shortcuts](DYLIBS/Shortcuts.md)
- [/System/Library/AccessibilityBundles/ShortcutsUI.axbundle/ShortcutsUI](DYLIBS/ShortcutsUI.md)
- [/System/Library/AccessibilityBundles/Sidecar.axbundle/Sidecar](DYLIBS/Sidecar.md)
- [/System/Library/AccessibilityBundles/Siri.axbundle/Siri](DYLIBS/Siri.md)
- [/System/Library/AccessibilityBundles/SiriActivation.axbundle/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/AccessibilityBundles/SiriKitRuntime.axbundle/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/AccessibilityBundles/SiriSharedUI.axbundle/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/AccessibilityBundles/SiriUI.axbundle/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/AccessibilityBundles/SiriUICore.axbundle/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/AccessibilityBundles/Siriland.axbundle/Siriland](DYLIBS/Siriland.md)
- [/System/Library/AccessibilityBundles/SleepHealthAppPlugin.axbundle/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/AccessibilityBundles/SleepHealthUI.axbundle/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/AccessibilityBundles/SocialFramework.axbundle/SocialFramework](DYLIBS/SocialFramework.md)
- [/System/Library/AccessibilityBundles/SocialLayer.axbundle/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/AccessibilityBundles/SocialWeeApp.axbundle/SocialWeeApp](DYLIBS/SocialWeeApp.md)
- [/System/Library/AccessibilityBundles/SoftwareUpdateSettingsUI.axbundle/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/AccessibilityBundles/SoundsAndHapticsSettings.axbundle/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/AccessibilityBundles/Sports-Assistant.axbundle/Sports-Assistant](DYLIBS/Sports-Assistant.md)
- [/System/Library/AccessibilityBundles/Spotlight.axbundle/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/AccessibilityBundles/SpotlightUIInternalFramework.axbundle/SpotlightUIInternalFramework](DYLIBS/SpotlightUIInternalFramework.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardFoundation.axbundle/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/SpringBoardUI.axbundle/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/AccessibilityBundles/SpringBoardUIServices.axbundle/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/AccessibilityBundles/SpriteKit.axbundle/SpriteKit](DYLIBS/SpriteKit.md)
- [/System/Library/AccessibilityBundles/StickersUI.axbundle/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/AccessibilityBundles/Stocks-Assistant.axbundle/Stocks-Assistant](DYLIBS/Stocks-Assistant.md)
- [/System/Library/AccessibilityBundles/StocksFramework.axbundle/StocksFramework](DYLIBS/StocksFramework.md)
- [/System/Library/AccessibilityBundles/StocksWidget.axbundle/StocksWidget](DYLIBS/StocksWidget.md)
- [/System/Library/AccessibilityBundles/StorageSettings.axbundle/StorageSettings](DYLIBS/StorageSettings.md)
- [/System/Library/AccessibilityBundles/StorageSettingsFramework.axbundle/StorageSettingsFramework](DYLIBS/StorageSettingsFramework.md)
- [/System/Library/AccessibilityBundles/StoreDynamicUIPlugin.axbundle/StoreDynamicUIPlugin](DYLIBS/StoreDynamicUIPlugin.md)
- [/System/Library/AccessibilityBundles/StoreKitFramework.axbundle/StoreKitFramework](DYLIBS/StoreKitFramework.md)
- [/System/Library/AccessibilityBundles/StoreKitUI.axbundle/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/AccessibilityBundles/SwiftUI.axbundle/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/AccessibilityBundles/System-Assistant.axbundle/System-Assistant](DYLIBS/System-Assistant.md)
- [/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/AccessibilityBundles/TV.axbundle/TV](DYLIBS/TV.md)
- [/System/Library/AccessibilityBundles/TVMLKit.axbundle/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/AccessibilityBundles/TVRemoteModule.axbundle/TVRemoteModule](DYLIBS/TVRemoteModule.md)
- [/System/Library/AccessibilityBundles/TVRemoteUI.axbundle/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/AccessibilityBundles/TVRemoteUIService.axbundle/TVRemoteUIService](DYLIBS/TVRemoteUIService.md)
- [/System/Library/AccessibilityBundles/TelephonyUIFramework.axbundle/TelephonyUIFramework](DYLIBS/TelephonyUIFramework.md)
- [/System/Library/AccessibilityBundles/TemplateKit.axbundle/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/AccessibilityBundles/TimerModule.axbundle/TimerModule](DYLIBS/TimerModule.md)
- [/System/Library/AccessibilityBundles/TipsApp.axbundle/TipsApp](DYLIBS/TipsApp.md)
- [/System/Library/AccessibilityBundles/TipsNotificationExtension.axbundle/TipsNotificationExtension](DYLIBS/TipsNotificationExtension.md)
- [/System/Library/AccessibilityBundles/TipsWidgetExtension.axbundle/TipsWidgetExtension](DYLIBS/TipsWidgetExtension.md)
- [/System/Library/AccessibilityBundles/ToneKit.axbundle/ToneKit](DYLIBS/ToneKit.md)
- [/System/Library/AccessibilityBundles/Translate.axbundle/Translate](DYLIBS/Translate.md)
- [/System/Library/AccessibilityBundles/TwitterFramework.axbundle/TwitterFramework](DYLIBS/TwitterFramework.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UpNext.axbundle/UpNext](DYLIBS/UpNext.md)
- [/System/Library/AccessibilityBundles/UsageSettings.axbundle/UsageSettings](DYLIBS/UsageSettings.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUI.axbundle/UserNotificationsUI](DYLIBS/UserNotificationsUI.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/AccessibilityBundles/VectorKit.axbundle/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/AccessibilityBundles/VictoriaSettings.axbundle/VictoriaSettings](DYLIBS/VictoriaSettings.md)
- [/System/Library/AccessibilityBundles/VideoConferenceControlCenterModule.axbundle/VideoConferenceControlCenterModule](DYLIBS/VideoConferenceControlCenterModule.md)
- [/System/Library/AccessibilityBundles/Videos.axbundle/Videos](DYLIBS/Videos.md)
- [/System/Library/AccessibilityBundles/VideosExtrasFramework.axbundle/VideosExtrasFramework](DYLIBS/VideosExtrasFramework.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/AccessibilityBundles/VisionKitCore.axbundle/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/AccessibilityBundles/VoiceShortcutsUI.axbundle/VoiceShortcutsUI](DYLIBS/VoiceShortcutsUI.md)
- [/System/Library/AccessibilityBundles/VoiceTriggerUI.axbundle/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/AccessibilityBundles/WAAnswer-Assistant.axbundle/WAAnswer-Assistant](DYLIBS/WAAnswer-Assistant.md)
- [/System/Library/AccessibilityBundles/Wallpaper.axbundle/Wallpaper](DYLIBS/Wallpaper.md)
- [/System/Library/AccessibilityBundles/WallpaperSettings.axbundle/WallpaperSettings](DYLIBS/WallpaperSettings.md)
- [/System/Library/AccessibilityBundles/Weather.axbundle/Weather](DYLIBS/Weather.md)
- [/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore](DYLIBS/WebCore.md)
- [/System/Library/AccessibilityBundles/WebKit.axbundle/WebKit](DYLIBS/WebKit.md)
- [/System/Library/AccessibilityBundles/WebKitLegacy.axbundle/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/AccessibilityBundles/WebProcess.axbundle/WebProcess](DYLIBS/WebProcess.md)
- [/System/Library/AccessibilityBundles/WebProcessLoader.axbundle/WebProcessLoader](DYLIBS/WebProcessLoader.md)
- [/System/Library/AccessibilityBundles/WebUI.axbundle/WebUI](DYLIBS/WebUI.md)
- [/System/Library/AccessibilityBundles/WiFiKitUI.axbundle/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/AccessibilityBundles/WidgetConfigurationExtension.axbundle/WidgetConfigurationExtension](DYLIBS/WidgetConfigurationExtension.md)
- [/System/Library/AccessibilityBundles/Widgets.axbundle/Widgets](DYLIBS/Widgets.md)
- [/System/Library/AccessibilityBundles/WirelessModemSettings.axbundle/WirelessModemSettings](DYLIBS/WirelessModemSettings.md)
- [/System/Library/AccessibilityBundles/WorkflowUI.axbundle/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/AccessibilityBundles/WorkflowUIServices.axbundle/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/AccessibilityBundles/com.apple.CloudDocsUI.CloudSharing-AppExtension.axbundle/com.apple.CloudDocsUI.CloudSharing-AppExtension](DYLIBS/com.apple.CloudDocsUI.CloudSharing-AppExtension.md)
- [/System/Library/AccessibilityBundles/com.apple.DocumentManager.Service-AppExtension.axbundle/com.apple.DocumentManager.Service-AppExtension](DYLIBS/com.apple.DocumentManager.Service-AppExtension.md)
- [/System/Library/AccessibilityBundles/iAdFramework.axbundle/iAdFramework](DYLIBS/iAdFramework.md)
- [/System/Library/AccessibilityBundles/iCloudDriveApp.axbundle/iCloudDriveApp](DYLIBS/iCloudDriveApp.md)
- [/System/Library/AccessibilityBundles/iTunesStoreFramework.axbundle/iTunesStoreFramework](DYLIBS/iTunesStoreFramework.md)
- [/System/Library/AccessibilityBundles/iTunesStoreUIFramework.axbundle/iTunesStoreUIFramework](DYLIBS/iTunesStoreUIFramework.md)
- [/System/Library/Accounts/Access/CloudKitAccessPlugin.bundle/CloudKitAccessPlugin](DYLIBS/CloudKitAccessPlugin.md)
- [/System/Library/Accounts/Access/DefaultAccessPlugin.bundle/DefaultAccessPlugin](DYLIBS/DefaultAccessPlugin.md)
- [/System/Library/Accounts/Access/YelpAccessPlugin.bundle/YelpAccessPlugin](DYLIBS/YelpAccessPlugin.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication](DYLIBS/AppleIDAuthentication.md)
- [/System/Library/Accounts/Authentication/AppleIDSSOAuthenticationPlugin.bundle/AppleIDSSOAuthenticationPlugin](DYLIBS/AppleIDSSOAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/CloudKitAuthenticationPlugin.bundle/CloudKitAuthenticationPlugin](DYLIBS/CloudKitAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/DAAccountAuthenticator.bundle/DAAccountAuthenticator](DYLIBS/DAAccountAuthenticator.md)
- [/System/Library/Accounts/Authentication/ESAccountAuthenticator.bundle/ESAccountAuthenticator](DYLIBS/ESAccountAuthenticator.md)
- [/System/Library/Accounts/Authentication/GoogleAuthenticationPlugin.bundle/GoogleAuthenticationPlugin](DYLIBS/GoogleAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/KerberosAuthenticationPlugin.bundle/KerberosAuthenticationPlugin](DYLIBS/KerberosAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/MessageAccountAuthenticationPlugin.bundle/MessageAccountAuthenticationPlugin](DYLIBS/MessageAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/YahooAuthenticationPlugin.bundle/YahooAuthenticationPlugin](DYLIBS/YahooAuthenticationPlugin.md)
- [/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin](DYLIBS/AAAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin](DYLIBS/AADataclassEnableNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AAIDMSAccountNotificationPlugin.bundle/AAIDMSAccountNotificationPlugin](DYLIBS/AAIDMSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/ACDatabaseBackupNotificationPlugin.bundle/ACDatabaseBackupNotificationPlugin](DYLIBS/ACDatabaseBackupNotificationPlugin.md)
- [/System/Library/Accounts/Notification/ADAccountsNotificationPlugin.bundle/ADAccountsNotificationPlugin](DYLIBS/ADAccountsNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AISAccountNotificationPlugin.bundle/AISAccountNotificationPlugin](DYLIBS/AISAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AKAccountNotificationPlugin.bundle/AKAccountNotificationPlugin](DYLIBS/AKAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin](DYLIBS/AMSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AMSAccountSyncNotificationPlugin.bundle/AMSAccountSyncNotificationPlugin](DYLIBS/AMSAccountSyncNotificationPlugin.md)
- [/System/Library/Accounts/Notification/ASDAccountNotficationPlugin.bundle/ASDAccountNotficationPlugin](DYLIBS/ASDAccountNotficationPlugin.md)
- [/System/Library/Accounts/Notification/AppleIDSSONotificationPlugin.bundle/AppleIDSSONotificationPlugin](DYLIBS/AppleIDSSONotificationPlugin.md)
- [/System/Library/Accounts/Notification/BTCloudPairingAccountNotificationPlugin.bundle/BTCloudPairingAccountNotificationPlugin](DYLIBS/BTCloudPairingAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CDPAccountNotificationPlugin_IOS.bundle/CDPAccountNotificationPlugin_IOS](DYLIBS/CDPAccountNotificationPlugin_IOS.md)
- [/System/Library/Accounts/Notification/ClassKitAccountNotificationPlugin.bundle/ClassKitAccountNotificationPlugin](DYLIBS/ClassKitAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CloudKitNotificationPlugin.bundle/CloudKitNotificationPlugin](DYLIBS/CloudKitNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreIDVAccountNotificationPlugin.bundle/CoreIDVAccountNotificationPlugin](DYLIBS/CoreIDVAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreLocationAccountNotificationPlugin.bundle/CoreLocationAccountNotificationPlugin](DYLIBS/CoreLocationAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreRecentsAccountNotificationPlugin.bundle/CoreRecentsAccountNotificationPlugin](DYLIBS/CoreRecentsAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreRoutineAccountNotificationPlugin.bundle/CoreRoutineAccountNotificationPlugin](DYLIBS/CoreRoutineAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/DAAccountNotifier.bundle/DAAccountNotifier](DYLIBS/DAAccountNotifier.md)
- [/System/Library/Accounts/Notification/DMDAccountNotificationPlugin.bundle/DMDAccountNotificationPlugin](DYLIBS/DMDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/DonationAccountWatcher.bundle/DonationAccountWatcher](DYLIBS/DonationAccountWatcher.md)
- [/System/Library/Accounts/Notification/ESAccountNotifier.bundle/ESAccountNotifier](DYLIBS/ESAccountNotifier.md)
- [/System/Library/Accounts/Notification/FMFLocatorAccountNotificationPlugin.bundle/FMFLocatorAccountNotificationPlugin](DYLIBS/FMFLocatorAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin](DYLIBS/FindMyDeviceAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/GameCenterAccountNotificationPlugin.bundle/GameCenterAccountNotificationPlugin](DYLIBS/GameCenterAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/HealthKitAccountNotificationPlugin.bundle/HealthKitAccountNotificationPlugin](DYLIBS/HealthKitAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/HomeKitAccountNotificationPlugin.bundle/HomeKitAccountNotificationPlugin](DYLIBS/HomeKitAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/IDSAccountNotificationPlugin.bundle/IDSAccountNotificationPlugin](DYLIBS/IDSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/IMAccountNotificationPlugin.bundle/IMAccountNotificationPlugin](DYLIBS/IMAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/INDAccountNotificationPlugin.bundle/INDAccountNotificationPlugin](DYLIBS/INDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Accounts/Notification/LockdownModeAccountNotificationPlugin.bundle/LockdownModeAccountNotificationPlugin](DYLIBS/LockdownModeAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/MessageAccountNotificationPlugin.bundle/MessageAccountNotificationPlugin](DYLIBS/MessageAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/MobileSyncAccountNotificationPlugin.bundle/MobileSyncAccountNotificationPlugin](DYLIBS/MobileSyncAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NewsNotificationPlugin.bundle/NewsNotificationPlugin](DYLIBS/NewsNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/NotesAccountNotificationPlugin](DYLIBS/NotesAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin](DYLIBS/PCSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PassbookAccountNotificationPlugin.bundle/PassbookAccountNotificationPlugin](DYLIBS/PassbookAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PhotosAccountNotificationPlugin.bundle/PhotosAccountNotificationPlugin](DYLIBS/PhotosAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/RPAccountNotificationPlugin.bundle/RPAccountNotificationPlugin](DYLIBS/RPAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/RemindersAccountNotificationPlugin.bundle/RemindersAccountNotificationPlugin](DYLIBS/RemindersAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SearchPartyAccountNotificationPlugin.bundle/SearchPartyAccountNotificationPlugin](DYLIBS/SearchPartyAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SecureBackupNotification.bundle/SecureBackupNotification](DYLIBS/SecureBackupNotification.md)
- [/System/Library/Accounts/Notification/SharingAccountNotificationPlugin.bundle/SharingAccountNotificationPlugin](DYLIBS/SharingAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/ShortcutsCloudKitAccountNotificationPlugin.bundle/ShortcutsCloudKitAccountNotificationPlugin](DYLIBS/ShortcutsCloudKitAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SiriCloudKitAccountsNotifier.bundle/SiriCloudKitAccountsNotifier](DYLIBS/SiriCloudKitAccountsNotifier.md)
- [/System/Library/Accounts/Notification/SocialAccountNotificationPlugin.bundle/SocialAccountNotificationPlugin](DYLIBS/SocialAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/WebBookmarksNotificationPlugin.bundle/WebBookmarksNotificationPlugin](DYLIBS/WebBookmarksNotificationPlugin.md)
- [/System/Library/Accounts/Notification/com.apple.askpermission.AccountNotificationPlugin.bundle/com.apple.askpermission.AccountNotificationPlugin](DYLIBS/com.apple.askpermission.AccountNotificationPlugin.md)
- [/System/Library/Assistant/Plugins/AssistantTTSPlugin.assistantBundle/AssistantTTSPlugin](DYLIBS/AssistantTTSPlugin.md)
- [/System/Library/Assistant/Plugins/Calendar.assistantBundle/Calendar](DYLIBS/Calendar.md)
- [/System/Library/Assistant/Plugins/Contacts.assistantBundle/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Assistant/Plugins/CorrectionsProfilesSync.assistantBundle/CorrectionsProfilesSync](DYLIBS/CorrectionsProfilesSync.md)
- [/System/Library/Assistant/Plugins/GEO.assistantBundle/GEO](DYLIBS/GEO.md)
- [/System/Library/Assistant/Plugins/HMAssistant.assistantBundle/HMAssistant](DYLIBS/HMAssistant.md)
- [/System/Library/Assistant/Plugins/LocaleSettings.assistantBundle/LocaleSettings](DYLIBS/LocaleSettings.md)
- [/System/Library/Assistant/Plugins/Media.assistantBundle/Media](DYLIBS/Media.md)
- [/System/Library/Assistant/Plugins/Phone.assistantBundle/Phone](DYLIBS/Phone.md)
- [/System/Library/Assistant/Plugins/Podcasts.assistantBundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/Assistant/Plugins/Routine.assistantBundle/Routine](DYLIBS/Routine.md)
- [/System/Library/Assistant/Plugins/SurfStatusSync.assistantBundle/SurfStatusSync](DYLIBS/SurfStatusSync.md)
- [/System/Library/Assistant/Plugins/SynapseSyncPlugin.assistantBundle/SynapseSyncPlugin](DYLIBS/SynapseSyncPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityShorcutsModule.bundle/AccessibilityShorcutsModule](DYLIBS/AccessibilityShorcutsModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilitySoundDetectionControlCenterModule.bundle/AccessibilitySoundDetectionControlCenterModule](DYLIBS/AccessibilitySoundDetectionControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule.md)
- [/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule.md)
- [/System/Library/ControlCenter/Bundles/AppearanceModule.bundle/AppearanceModule](DYLIBS/AppearanceModule.md)
- [/System/Library/ControlCenter/Bundles/CameraModule.bundle/CameraModule](DYLIBS/CameraModule.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule](DYLIBS/DisplayModule.md)
- [/System/Library/ControlCenter/Bundles/FeedbackAssistantModule.bundle/FeedbackAssistantModule](DYLIBS/FeedbackAssistantModule.md)
- [/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule](DYLIBS/FlashlightModule.md)
- [/System/Library/ControlCenter/Bundles/HearingAidsModule.bundle/HearingAidsModule](DYLIBS/HearingAidsModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterCompactModule.bundle/HomeControlCenterCompactModule](DYLIBS/HomeControlCenterCompactModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/KeyboardBrightnessModule.bundle/KeyboardBrightnessModule](DYLIBS/KeyboardBrightnessModule.md)
- [/System/Library/ControlCenter/Bundles/LowPowerModule.bundle/LowPowerModule](DYLIBS/LowPowerModule.md)
- [/System/Library/ControlCenter/Bundles/MediaControlsAudioModule.bundle/MediaControlsAudioModule](DYLIBS/MediaControlsAudioModule.md)
- [/System/Library/ControlCenter/Bundles/MediaControlsModule.bundle/MediaControlsModule](DYLIBS/MediaControlsModule.md)
- [/System/Library/ControlCenter/Bundles/MuteModule.bundle/MuteModule](DYLIBS/MuteModule.md)
- [/System/Library/ControlCenter/Bundles/OrientationLockModule.bundle/OrientationLockModule](DYLIBS/OrientationLockModule.md)
- [/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule](DYLIBS/PerformanceTraceModule.md)
- [/System/Library/ControlCenter/Bundles/QuickNoteModule.bundle/QuickNoteModule](DYLIBS/QuickNoteModule.md)
- [/System/Library/ControlCenter/Bundles/ShazamModule.bundle/ShazamModule](DYLIBS/ShazamModule.md)
- [/System/Library/ControlCenter/Bundles/SpokenNotificationsModule.bundle/SpokenNotificationsModule](DYLIBS/SpokenNotificationsModule.md)
- [/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule](DYLIBS/TVRemoteModule.md)
- [/System/Library/ControlCenter/Bundles/TimerModule.bundle/TimerModule](DYLIBS/TimerModule.md)
- [/System/Library/ControlCenter/Bundles/WalletModule.bundle/WalletModule](DYLIBS/WalletModule.md)
- [/System/Library/CoreAccessories/PlugIns/Features/AssistiveTouch-iOS.feature/AssistiveTouch-iOS](DYLIBS/AssistiveTouch-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/BLEPairing-iOS.feature/BLEPairing-iOS](DYLIBS/BLEPairing-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS](DYLIBS/Communications-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/HID.feature/HID](DYLIBS/HID.md)
- [/System/Library/CoreAccessories/PlugIns/Features/MediaLibrary-iOS.feature/MediaLibrary-iOS](DYLIBS/MediaLibrary-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/Navigation-iOS.feature/Navigation-iOS](DYLIBS/Navigation-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/NowPlaying-iOS.feature/NowPlaying-iOS](DYLIBS/NowPlaying-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/OOBBTPairing-iOS.feature/OOBBTPairing-iOS](DYLIBS/OOBBTPairing-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit](DYLIBS/IOKit.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth](DYLIBS/Platform-Bluetooth.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/System.platform/System](DYLIBS/System.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/WiFiSharing.platform/WiFiSharing](DYLIBS/WiFiSharing.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC](DYLIBS/NFC.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost](DYLIBS/USBHost.md)
- [/System/Library/CoreServices/RawCamera.bundle/RawCamera](DYLIBS/RawCamera.md)
- [/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount](DYLIBS/DAAccount.md)
- [/System/Library/DataClassMigrators/FaceTimeMigrator.migrator/FaceTimeMigrator](DYLIBS/FaceTimeMigrator.md)
- [/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator](DYLIBS/MessagesDataMigrator.md)
- [/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation](DYLIBS/PasswordsDigitalSeparation.md)
- [/System/Library/Extensions/AGXGPURawCounterBundle.bundle/AGXGPURawCounterBundle](DYLIBS/AGXGPURawCounterBundle.md)
- [/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0](DYLIBS/AGXMetalG16P_A0.md)
- [/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0](DYLIBS/AGXMetalG16P_B0.md)
- [/System/Library/Extensions/AppleHDQGasGaugeControl.kext/PlugIns/AppleHDQGasGaugeHID.plugin/AppleHDQGasGaugeHID](DYLIBS/AppleHDQGasGaugeHID.md)
- [/System/Library/Extensions/AppleMetalGLRenderer.bundle/AppleMetalGLRenderer](DYLIBS/AppleMetalGLRenderer.md)
- [/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID](DYLIBS/MultitouchHID.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/AppleSPULib.plugin/AppleSPULib](DYLIBS/AppleSPULib.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib](DYLIBS/GNSSPassthroughLib.md)
- [/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib](DYLIBS/IOHIDLib.md)
- [/System/Library/Extensions/IOUSBDeviceFamily.kext/PlugIns/IOUSBDeviceLib.plugin/IOUSBDeviceLib](DYLIBS/IOUSBDeviceLib.md)
- [/System/Library/Fitness/Plugins/ActivitySharingAwardsPlugin.bundle/ActivitySharingAwardsPlugin](DYLIBS/ActivitySharingAwardsPlugin.md)
- [/System/Library/Fitness/Plugins/SeymourAwardsPlugin.bundle/SeymourAwardsPlugin](DYLIBS/SeymourAwardsPlugin.md)
- [/System/Library/Frameworks/ARKit.framework/ARKit](DYLIBS/ARKit.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVFoundation.framework/AVFoundation](DYLIBS/AVFoundation.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/AVRouting.framework/AVRouting](DYLIBS/AVRouting.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/Libraries/libCGInterfaces.dylib](DYLIBS/libCGInterfaces.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLinearAlgebra.dylib](DYLIBS/libLinearAlgebra.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libQuadrature.dylib](DYLIBS/libQuadrature.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib](DYLIBS/libSparse.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib](DYLIBS/libvDSP.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvMisc.dylib](DYLIBS/libvMisc.dylib.md)
- [/System/Library/Frameworks/Accessibility.framework/Accessibility](DYLIBS/Accessibility.md)
- [/System/Library/Frameworks/Accounts.framework/Accounts](DYLIBS/Accounts.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit](DYLIBS/AdAttributionKit.md)
- [/System/Library/Frameworks/AdServices.framework/AdServices](DYLIBS/AdServices.md)
- [/System/Library/Frameworks/AdSupport.framework/AdSupport](DYLIBS/AdSupport.md)
- [/System/Library/Frameworks/AddressBook.framework/AddressBook](DYLIBS/AddressBook.md)
- [/System/Library/Frameworks/AddressBookUI.framework/AddressBookUI](DYLIBS/AddressBookUI.md)
- [/System/Library/Frameworks/AppClip.framework/AppClip](DYLIBS/AppClip.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency](DYLIBS/AppTrackingTransparency.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary](DYLIBS/AssetsLibrary.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libValidationCapsule.dylib](DYLIBS/libValidationCapsule.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libVibeSynthEngine.dylib](DYLIBS/libVibeSynthEngine.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/AutomatedDeviceEnrollment](DYLIBS/AutomatedDeviceEnrollment.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration](DYLIBS/AutomaticAssessmentConfiguration.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies](DYLIBS/AACDependencies.md)
- [/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets](DYLIBS/BackgroundAssets.md)
- [/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks](DYLIBS/BackgroundTasks.md)
- [/System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore](DYLIBS/BrowserEngineCore.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/BusinessChat.framework/BusinessChat](DYLIBS/BusinessChat.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit.md)
- [/System/Library/Frameworks/CarKey.framework/CarKey](DYLIBS/CarKey.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Cinematic.framework/Cinematic](DYLIBS/Cinematic.md)
- [/System/Library/Frameworks/ClassKit.framework/ClassKit](DYLIBS/ClassKit.md)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/ColorSync.framework/ColorSync](DYLIBS/ColorSync.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics](DYLIBS/CoreHaptics.md)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI](DYLIBS/CoreLocationUI.md)
- [/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI](DYLIBS/CoreMIDI.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreNFC.framework/CoreNFC](DYLIBS/CoreNFC.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCellularDecoders.dylib](DYLIBS/libCellularDecoders.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterAWDMetrics.dylib](DYLIBS/libCommCenterAWDMetrics.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCNTargetData.dylib](DYLIBS/libCommCenterCNTargetData.dylib.md)
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
- [/System/Library/Frameworks/DataDetection.framework/DataDetection](DYLIBS/DataDetection.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck](DYLIBS/DeviceCheck.md)
- [/System/Library/Frameworks/DeviceDiscoveryExtension.framework/DeviceDiscoveryExtension](DYLIBS/DeviceDiscoveryExtension.md)
- [/System/Library/Frameworks/DockKit.framework/DockKit](DYLIBS/DockKit.md)
- [/System/Library/Frameworks/DriverKit.framework/DriverKit](DYLIBS/DriverKit.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExposureNotification.framework/ExposureNotification](DYLIBS/ExposureNotification.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit](DYLIBS/ExtensionKit.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory](DYLIBS/ExternalAccessory.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControls](DYLIBS/FamilyControls.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FileProviderUI.framework/FileProviderUI](DYLIBS/FileProviderUI.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GLKit.framework/GLKit](DYLIBS/GLKit.md)
- [/System/Library/Frameworks/GSS.framework/GSS](DYLIBS/GSS.md)
- [/System/Library/Frameworks/GameController.framework/GameController](DYLIBS/GameController.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/GameplayKit.framework/GameplayKit](DYLIBS/GameplayKit.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HealthKitUI.framework/HealthKitUI](DYLIBS/HealthKitUI.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/IOSurface.framework/IOSurface](DYLIBS/IOSurface.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/IdentityLookupUI.framework/IdentityLookupUI](DYLIBS/IdentityLookupUI.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore](DYLIBS/ImageCaptureCore.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/IntentsUI.framework/IntentsUI](DYLIBS/IntentsUI.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/JournalingSuggestions.framework/JournalingSuggestions](DYLIBS/JournalingSuggestions.md)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils](DYLIBS/DaemonUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI](DYLIBS/LocalAuthenticationEmbeddedUI.md)
- [/System/Library/Frameworks/MLCompute.framework/MLCompute](DYLIBS/MLCompute.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings](DYLIBS/ManagedSettings.md)
- [/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI](DYLIBS/ManagedSettingsUI.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MatterSupport.framework/MatterSupport](DYLIBS/MatterSupport.md)
- [/System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility](DYLIBS/MediaAccessibility.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaSetup.framework/MediaSetup](DYLIBS/MediaSetup.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MediaToolbox.framework/Support/libSTS-N.dylib](DYLIBS/libSTS-N.dylib.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Messages.framework/Messages](DYLIBS/Messages.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX.md)
- [/System/Library/Frameworks/MetalKit.framework/MetalKit](DYLIBS/MetalKit.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop](DYLIBS/MPSBenchmarkLoop.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore](DYLIBS/MPSCore.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSFunctions.framework/MPSFunctions](DYLIBS/MPSFunctions.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/MPSImage](DYLIBS/MPSImage.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSMatrix.framework/MPSMatrix](DYLIBS/MPSMatrix.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork](DYLIBS/MPSNeuralNetwork.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/MPSRayIntersector](DYLIBS/MPSRayIntersector.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders](DYLIBS/MetalPerformanceShaders.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/MetricKit.framework/MetricKit](DYLIBS/MetricKit.md)
- [/System/Library/Frameworks/ModelIO.framework/ModelIO](DYLIBS/ModelIO.md)
- [/System/Library/Frameworks/MultipeerConnectivity.framework/MultipeerConnectivity](DYLIBS/MultipeerConnectivity.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage](DYLIBS/NaturalLanguage.md)
- [/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction](DYLIBS/NearbyInteraction.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/NotificationCenter.framework/NotificationCenter](DYLIBS/NotificationCenter.md)
- [/System/Library/Frameworks/OSLog.framework/OSLog](DYLIBS/OSLog.md)
- [/System/Library/Frameworks/OpenAL.framework/OpenAL](DYLIBS/OpenAL.md)
- [/System/Library/Frameworks/OpenGLES.framework/GLEngine.bundle/GLEngine](DYLIBS/GLEngine.md)
- [/System/Library/Frameworks/OpenGLES.framework/OpenGLES](DYLIBS/OpenGLES.md)
- [/System/Library/Frameworks/OpenGLES.framework/libCVMSPluginSupport.dylib](DYLIBS/libCVMSPluginSupport.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib](DYLIBS/libCoreFSCache.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libCoreVMClient.dylib](DYLIBS/libCoreVMClient.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGFXShared.dylib](DYLIBS/libGFXShared.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLImage.dylib](DYLIBS/libGLImage.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLProgrammability.dylib](DYLIBS/libGLProgrammability.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLVMPlugin.dylib](DYLIBS/libGLVMPlugin.dylib.md)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/Frameworks/PHASE.framework/PHASE](DYLIBS/PHASE.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/PushToTalk.framework/PushToTalk](DYLIBS/PushToTalk.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/ReplayKit.framework/ReplayKit](DYLIBS/ReplayKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SafetyKit.framework/SafetyKit](DYLIBS/SafetyKit.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/ScreenTime.framework/ScreenTime](DYLIBS/ScreenTime.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis](DYLIBS/SensitiveContentAnalysis.md)
- [/System/Library/Frameworks/SensorKit.framework/SensorKit](DYLIBS/SensorKit.md)
- [/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou](DYLIBS/SharedWithYou.md)
- [/System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore](DYLIBS/SharedWithYouCore.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/Social.framework/Social](DYLIBS/Social.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/SpriteKit.framework/SpriteKit](DYLIBS/SpriteKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/Symbols.framework/Symbols](DYLIBS/Symbols.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration](DYLIBS/SystemConfiguration.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork](DYLIBS/ThreadNetwork.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/TipsNext.framework/TipsNext](DYLIBS/TipsNext.md)
- [/System/Library/Frameworks/Translation.framework/Translation](DYLIBS/Translation.md)
- [/System/Library/Frameworks/Twitter.framework/Twitter](DYLIBS/Twitter.md)
- [/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers](DYLIBS/UniformTypeIdentifiers.md)
- [/System/Library/Frameworks/UserNotifications.framework/UserNotifications](DYLIBS/UserNotifications.md)
- [/System/Library/Frameworks/UserNotificationsUI.framework/UserNotificationsUI](DYLIBS/UserNotificationsUI.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/Vision.framework/libfaceCore.dylib](DYLIBS/libfaceCore.dylib.md)
- [/System/Library/Frameworks/VisionKit.framework/VisionKit](DYLIBS/VisionKit.md)
- [/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity](DYLIBS/WatchConnectivity.md)
- [/System/Library/Frameworks/WatchKit.framework/WatchKit](DYLIBS/WatchKit.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AVKit_SwiftUI.framework/_AVKit_SwiftUI](DYLIBS/_AVKit_SwiftUI.md)
- [/System/Library/Frameworks/_AdAttributionKit_StoreKit.framework/_AdAttributionKit_StoreKit](DYLIBS/_AdAttributionKit_StoreKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_CoreData_CloudKit.framework/_CoreData_CloudKit](DYLIBS/_CoreData_CloudKit.md)
- [/System/Library/Frameworks/_CoreLocationUI_SwiftUI.framework/_CoreLocationUI_SwiftUI](DYLIBS/_CoreLocationUI_SwiftUI.md)
- [/System/Library/Frameworks/_CoreNFC_UIKit.framework/_CoreNFC_UIKit](DYLIBS/_CoreNFC_UIKit.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_HomeKit_SwiftUI.framework/_HomeKit_SwiftUI](DYLIBS/_HomeKit_SwiftUI.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/Library/Frameworks/_QuickLook_SwiftUI.framework/_QuickLook_SwiftUI](DYLIBS/_QuickLook_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_SceneKit_SwiftUI.framework/_SceneKit_SwiftUI](DYLIBS/_SceneKit_SwiftUI.md)
- [/System/Library/Frameworks/_SpriteKit_SwiftUI.framework/_SpriteKit_SwiftUI](DYLIBS/_SpriteKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_CoreData.framework/_SwiftData_CoreData](DYLIBS/_SwiftData_CoreData.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI.md)
- [/System/Library/Frameworks/_WorkoutKit_SwiftUI.framework/_WorkoutKit_SwiftUI](DYLIBS/_WorkoutKit_SwiftUI.md)
- [/System/Library/Frameworks/iAd.framework/iAd](DYLIBS/iAd.md)
- [/System/Library/HIDPlugins/AppleSPUAccCompassPlugin.plugin/AppleSPUAccCompassPlugin](DYLIBS/AppleSPUAccCompassPlugin.md)
- [/System/Library/HIDPlugins/AppleSPUDispCompassPlugin.plugin/AppleSPUDispCompassPlugin](DYLIBS/AppleSPUDispCompassPlugin.md)
- [/System/Library/HIDPlugins/AppleSPUHIDStatistics.plugin/AppleSPUHIDStatistics](DYLIBS/AppleSPUHIDStatistics.md)
- [/System/Library/HIDPlugins/AttentionAwarenessFilter.plugin/AttentionAwarenessFilter](DYLIBS/AttentionAwarenessFilter.md)
- [/System/Library/HIDPlugins/IOHIDEventProcessorFilter.plugin/IOHIDEventProcessorFilter](DYLIBS/IOHIDEventProcessorFilter.md)
- [/System/Library/HIDPlugins/IOHIDEventSystemStatistics.plugin/IOHIDEventSystemStatistics](DYLIBS/IOHIDEventSystemStatistics.md)
- [/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter](DYLIBS/IOHIDKeyboardFilter.md)
- [/System/Library/HIDPlugins/IOHIDPointerScrollFilter.plugin/IOHIDPointerScrollFilter](DYLIBS/IOHIDPointerScrollFilter.md)
- [/System/Library/HIDPlugins/IOHIDT8027USBSessionFilter.plugin/IOHIDT8027USBSessionFilter](DYLIBS/IOHIDT8027USBSessionFilter.md)
- [/System/Library/HIDPlugins/PearlEventFilter.plugin/PearlEventFilter](DYLIBS/PearlEventFilter.md)
- [/System/Library/Health/FeedItemPlugins/AppRecommendations.healthplugin/AppRecommendations](DYLIBS/AppRecommendations.md)
- [/System/Library/Health/FeedItemPlugins/Categories.healthplugin/Categories](DYLIBS/Categories.md)
- [/System/Library/Health/FeedItemPlugins/HealthArticles.healthplugin/HealthArticles](DYLIBS/HealthArticles.md)
- [/System/Library/Health/FeedItemPlugins/HealthRecords.healthplugin/HealthRecords](DYLIBS/HealthRecords.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MobilityAppPlugin.healthplugin/MobilityAppPlugin](DYLIBS/MobilityAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/ResearchApp.healthplugin/ResearchApp](DYLIBS/ResearchApp.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/Health/Plugins/ActivityAchievementsPlugin.bundle/ActivityAchievementsPlugin](DYLIBS/ActivityAchievementsPlugin.md)
- [/System/Library/Health/Plugins/ActivityAwardsPlugin.bundle/ActivityAwardsPlugin](DYLIBS/ActivityAwardsPlugin.md)
- [/System/Library/Health/Plugins/ActivitySharingPlugin.bundle/ActivitySharingPlugin](DYLIBS/ActivitySharingPlugin.md)
- [/System/Library/Health/Plugins/CompanionHealthPlugin.bundle/CompanionHealthPlugin](DYLIBS/CompanionHealthPlugin.md)
- [/System/Library/Health/Plugins/HealthAppPlugin.bundle/HealthAppPlugin](DYLIBS/HealthAppPlugin.md)
- [/System/Library/Health/Plugins/HeartDaemonPlugin.bundle/HeartDaemonPlugin](DYLIBS/HeartDaemonPlugin.md)
- [/System/Library/Health/Plugins/MenstrualCyclesDaemonPlugin.bundle/MenstrualCyclesDaemonPlugin](DYLIBS/MenstrualCyclesDaemonPlugin.md)
- [/System/Library/Health/Plugins/RespiratoryHealthDaemonPlugin.bundle/RespiratoryHealthDaemonPlugin](DYLIBS/RespiratoryHealthDaemonPlugin.md)
- [/System/Library/Health/Plugins/SleepHealthDaemonPlugin.bundle/SleepHealthDaemonPlugin](DYLIBS/SleepHealthDaemonPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/MessagesComplication.bundle/MessagesComplication](DYLIBS/MessagesComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications](DYLIBS/NanoCompassComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoMenstrualCyclesComplication.bundle/NanoMenstrualCyclesComplication](DYLIBS/NanoMenstrualCyclesComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoSleepComplication.bundle/NanoSleepComplication](DYLIBS/NanoSleepComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WorldClockComplications.bundle/WorldClockComplications](DYLIBS/WorldClockComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAegirFaceBundleCompanion.bundle/NTKAegirFaceBundleCompanion](DYLIBS/NTKAegirFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExtragalacticFaceBundleCompanion.bundle/NTKExtragalacticFaceBundleCompanion](DYLIBS/NTKExtragalacticFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFoghornFaceBundleCompanion.bundle/NTKFoghornFaceBundleCompanion](DYLIBS/NTKFoghornFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGalleonFaceBundleCompanion.bundle/NTKGalleonFaceBundleCompanion](DYLIBS/NTKGalleonFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSnowglobeFaceBundleCompanion.bundle/NTKSnowglobeFaceBundleCompanion](DYLIBS/NTKSnowglobeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVivaldiFaceBundleCompanion.bundle/NTKVivaldiFaceBundleCompanion](DYLIBS/NTKVivaldiFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AirPortSettings.bundle/AirPortSettings](DYLIBS/AirPortSettings.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PreferenceBundles/CarrierSettings.bundle/CarrierSettings](DYLIBS/CarrierSettings.md)
- [/System/Library/PreferenceBundles/EDGESettings.bundle/EDGESettings](DYLIBS/EDGESettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings](DYLIBS/MobilePhoneSettings.md)
- [/System/Library/PreferenceBundles/ScheduleSettings.bundle/ScheduleSettings](DYLIBS/ScheduleSettings.md)
- [/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences](DYLIBS/VPNPreferences.md)
- [/System/Library/PreferenceBundles/WirelessModemSettings.bundle/WirelessModemSettings](DYLIBS/WirelessModemSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/AACCore](DYLIBS/AACCore.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/ACCBaker.framework/ACCBaker](DYLIBS/ACCBaker.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/ACTFramework.framework/ACTFramework](DYLIBS/ACTFramework.md)
- [/System/Library/PrivateFrameworks/AFKUser.framework/AFKUser](DYLIBS/AFKUser.md)
- [/System/Library/PrivateFrameworks/AGXCompilerConnection-S2A8.framework/AGXCompilerConnection-S2A8](DYLIBS/AGXCompilerConnection-S2A8.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore-S2A8.framework/AGXCompilerCore-S2A8](DYLIBS/AGXCompilerCore-S2A8.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter](DYLIBS/AGXGPURawCounter.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI](DYLIBS/AMPCoreUI.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/libORTools.dylib](DYLIBS/libORTools.dylib.md)
- [/System/Library/PrivateFrameworks/ANEServices.framework/ANEServices](DYLIBS/ANEServices.md)
- [/System/Library/PrivateFrameworks/ANSTKit.framework/ANSTKit](DYLIBS/ANSTKit.md)
- [/System/Library/PrivateFrameworks/AOPHaptics.framework/AOPHaptics](DYLIBS/AOPHaptics.md)
- [/System/Library/PrivateFrameworks/AOSKit.framework/AOSKit](DYLIBS/AOSKit.md)
- [/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem](DYLIBS/APConfigurationSystem.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore.md)
- [/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon](DYLIBS/ARKitDaemon.md)
- [/System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation](DYLIBS/ARKitFoundation.md)
- [/System/Library/PrivateFrameworks/ARKitUI.framework/ARKitUI](DYLIBS/ARKitUI.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/ASOctaneSupport](DYLIBS/ASOctaneSupport.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation](DYLIBS/ATFoundation.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings](DYLIBS/AUSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/GKSPerformance.framework/GKSPerformance](DYLIBS/GKSPerformance.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ICE.framework/ICE](DYLIBS/ICE.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/LegacyHandle.framework/LegacyHandle](DYLIBS/LegacyHandle.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/SimpleKeyExchange.framework/SimpleKeyExchange](DYLIBS/SimpleKeyExchange.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/snatmap.framework/snatmap](DYLIBS/snatmap.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXAggregateStatisticsServices.framework/AXAggregateStatisticsServices](DYLIBS/AXAggregateStatisticsServices.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader](DYLIBS/AXAssetLoader.md)
- [/System/Library/PrivateFrameworks/AXContainerServices.framework/AXContainerServices](DYLIBS/AXContainerServices.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXElementInteraction.framework/AXElementInteraction](DYLIBS/AXElementInteraction.md)
- [/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils](DYLIBS/AXFrontBoardUtils.md)
- [/System/Library/PrivateFrameworks/AXIDSServices.framework/AXIDSServices](DYLIBS/AXIDSServices.md)
- [/System/Library/PrivateFrameworks/AXLocalizationCaptionService.framework/AXLocalizationCaptionService](DYLIBS/AXLocalizationCaptionService.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities](DYLIBS/AXMediaUtilities.md)
- [/System/Library/PrivateFrameworks/AXNTKUtilities.framework/AXNTKUtilities](DYLIBS/AXNTKUtilities.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection](DYLIBS/AXSoundDetection.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AXSpeakFingerManager.framework/AXSpeakFingerManager](DYLIBS/AXSpeakFingerManager.md)
- [/System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices](DYLIBS/AXSpeechAssetServices.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AXTapToSpeakTime.framework/AXTapToSpeakTime](DYLIBS/AXTapToSpeakTime.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenServices.framework/AXWatchRemoteScreenServices](DYLIBS/AXWatchRemoteScreenServices.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI](DYLIBS/AXWatchRemoteScreenUI.md)
- [/System/Library/PrivateFrameworks/AccelerateGPU.framework/AccelerateGPU](DYLIBS/AccelerateGPU.md)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAudit](DYLIBS/AccessibilityAudit.md)
- [/System/Library/PrivateFrameworks/AccessibilityFocusEngine.framework/AccessibilityFocusEngine](DYLIBS/AccessibilityFocusEngine.md)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction.md)
- [/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation](DYLIBS/AccessibilityPlatformTranslation.md)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/AccessibilityRemoteServices](DYLIBS/AccessibilityRemoteServices.md)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteUIServices.framework/AccessibilityRemoteUIServices](DYLIBS/AccessibilityRemoteUIServices.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI](DYLIBS/AccessibilityUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared](DYLIBS/AccessibilityUIShared.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIViewServices.framework/AccessibilityUIViewServices](DYLIBS/AccessibilityUIViewServices.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccessoryAssistiveTouch.framework/AccessoryAssistiveTouch](DYLIBS/AccessoryAssistiveTouch.md)
- [/System/Library/PrivateFrameworks/AccessoryAudio.framework/AccessoryAudio](DYLIBS/AccessoryAudio.md)
- [/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing](DYLIBS/AccessoryBLEPairing.md)
- [/System/Library/PrivateFrameworks/AccessoryCommunications.framework/AccessoryCommunications](DYLIBS/AccessoryCommunications.md)
- [/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth](DYLIBS/AccessoryComponentAuth.md)
- [/System/Library/PrivateFrameworks/AccessoryHID.framework/AccessoryHID](DYLIBS/AccessoryHID.md)
- [/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary](DYLIBS/AccessoryMediaLibrary.md)
- [/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation](DYLIBS/AccessoryNavigation.md)
- [/System/Library/PrivateFrameworks/AccessoryNowPlaying.framework/AccessoryNowPlaying](DYLIBS/AccessoryNowPlaying.md)
- [/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/AccessoryOOBBTPairing](DYLIBS/AccessoryOOBBTPairing.md)
- [/System/Library/PrivateFrameworks/AccessoryVoiceOver.framework/AccessoryVoiceOver](DYLIBS/AccessoryVoiceOver.md)
- [/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim](DYLIBS/AccessoryiAP2Shim.md)
- [/System/Library/PrivateFrameworks/AccountNotification.framework/AccountNotification](DYLIBS/AccountNotification.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI](DYLIBS/AccountsUI.md)
- [/System/Library/PrivateFrameworks/AcousticMaterials.framework/AcousticMaterials](DYLIBS/AcousticMaterials.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements](DYLIBS/ActivityAchievements.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon](DYLIBS/ActivityAchievementsDaemon.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI](DYLIBS/ActivityAchievementsUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsClient.framework/ActivityAwardsClient](DYLIBS/ActivityAwardsClient.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI](DYLIBS/ActivityRingsUI.md)
- [/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing](DYLIBS/ActivitySharing.md)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient.md)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI.md)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdCore.framework/AdCore](DYLIBS/AdCore.md)
- [/System/Library/PrivateFrameworks/AdID.framework/AdID](DYLIBS/AdID.md)
- [/System/Library/PrivateFrameworks/AdPlatforms.framework/AdPlatforms](DYLIBS/AdPlatforms.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommonUI.framework/AdPlatformsCommonUI](DYLIBS/AdPlatformsCommonUI.md)
- [/System/Library/PrivateFrameworks/AdPlatformsInternal.framework/AdPlatformsInternal](DYLIBS/AdPlatformsInternal.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AdminLite.framework/AdminLite](DYLIBS/AdminLite.md)
- [/System/Library/PrivateFrameworks/AfibBurden.framework/AfibBurden](DYLIBS/AfibBurden.md)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary](DYLIBS/AggregateDictionary.md)
- [/System/Library/PrivateFrameworks/AggregateDictionaryHistory.framework/AggregateDictionaryHistory](DYLIBS/AggregateDictionaryHistory.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlayRoutePrediction.framework/AirPlayRoutePrediction](DYLIBS/AirPlayRoutePrediction.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySenderUI.framework/AirPlaySenderUI](DYLIBS/AirPlaySenderUI.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AirPortAssistant.framework/AirPortAssistant](DYLIBS/AirPortAssistant.md)
- [/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic](DYLIBS/AirTraffic.md)
- [/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice](DYLIBS/AirTrafficDevice.md)
- [/System/Library/PrivateFrameworks/AlgosScoreFramework.framework/AlgosScoreFramework](DYLIBS/AlgosScoreFramework.md)
- [/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit](DYLIBS/AltruisticBodyPoseKit.md)
- [/System/Library/PrivateFrameworks/Ambient.framework/Ambient](DYLIBS/Ambient.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/PrivateFrameworks/AmbientUIKit.framework/AmbientUIKit](DYLIBS/AmbientUIKit.md)
- [/System/Library/PrivateFrameworks/AmbientUIServices.framework/AmbientUIServices](DYLIBS/AmbientUIServices.md)
- [/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D.md)
- [/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit](DYLIBS/AppConduit.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics](DYLIBS/AppInstallationMetrics.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation](DYLIBS/AppPredictionFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUI.framework/AppPredictionUI](DYLIBS/AppPredictionUI.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation](DYLIBS/AppPredictionUIFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIWidget.framework/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO](DYLIBS/AppSSO.md)
- [/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore](DYLIBS/AppSSOCore.md)
- [/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos](DYLIBS/AppSSOKerberos.md)
- [/System/Library/PrivateFrameworks/AppSSOUI.framework/AppSSOUI](DYLIBS/AppSSOUI.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreEvalLighthouseUtils.framework/AppStoreEvalLighthouseUtils](DYLIBS/AppStoreEvalLighthouseUtils.md)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation](DYLIBS/AppStoreFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays](DYLIBS/AppStoreOverlays.md)
- [/System/Library/PrivateFrameworks/AppStoreUI.framework/AppStoreUI](DYLIBS/AppStoreUI.md)
- [/System/Library/PrivateFrameworks/AppStoreUtilities.framework/AppStoreUtilities](DYLIBS/AppStoreUtilities.md)
- [/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport](DYLIBS/AppSupport.md)
- [/System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI](DYLIBS/AppSupportUI.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCV3DMOVKit.framework/AppleCV3DMOVKit](DYLIBS/AppleCV3DMOVKit.md)
- [/System/Library/PrivateFrameworks/AppleCV3DModels.framework/AppleCV3DModels](DYLIBS/AppleCV3DModels.md)
- [/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA](DYLIBS/AppleCVA.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater](DYLIBS/AppleConvergedFirmwareUpdater.md)
- [/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth](DYLIBS/AppleDepth.md)
- [/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore](DYLIBS/AppleDepthCore.md)
- [/System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices](DYLIBS/AppleEmbeddedDisplayServices.md)
- [/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression](DYLIBS/AppleFSCompression.md)
- [/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate](DYLIBS/AppleFirmwareUpdate.md)
- [/System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers](DYLIBS/AppleFlatBuffers.md)
- [/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback](DYLIBS/AppleHIDFeedback.md)
- [/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport](DYLIBS/AppleHIDTransportSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport](DYLIBS/AppleIDAuthSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication](DYLIBS/AppleIDSSOAuthentication.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG](DYLIBS/AppleJPEG.md)
- [/System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL](DYLIBS/AppleJPEGXL.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleLDAP.framework/AppleLDAP](DYLIBS/AppleLDAP.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery](DYLIBS/AppleMediaDiscovery.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitSupport.framework/AppleMediaServicesKitSupport](DYLIBS/AppleMediaServicesKitSupport.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity](DYLIBS/AppleMobileFileIntegrity.md)
- [/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe](DYLIBS/AppleNVMe.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine](DYLIBS/AppleNeuralEngine.md)
- [/System/Library/PrivateFrameworks/ApplePDPHelper.framework/ApplePDPHelper](DYLIBS/ApplePDPHelper.md)
- [/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices](DYLIBS/ApplePhotonDetectorServices.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService.md)
- [/System/Library/PrivateFrameworks/AppleSARHelper.framework/AppleSARHelper](DYLIBS/AppleSARHelper.md)
- [/System/Library/PrivateFrameworks/AppleSRP.framework/AppleSRP](DYLIBS/AppleSRP.md)
- [/System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce](DYLIBS/AppleSauce.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication](DYLIBS/AppleTracingSupportSymbolication.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AskTo.framework/AskTo](DYLIBS/AskTo.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices](DYLIBS/AssertionServices.md)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/AssetCacheServices](DYLIBS/AssetCacheServices.md)
- [/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/AssetCacheServicesExtensions](DYLIBS/AssetCacheServicesExtensions.md)
- [/System/Library/PrivateFrameworks/AssetExplorer.framework/AssetExplorer](DYLIBS/AssetExplorer.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantCardServiceSupport.framework/AssistantCardServiceSupport](DYLIBS/AssistantCardServiceSupport.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal](DYLIBS/AtomicsInternal.md)
- [/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness](DYLIBS/AttentionAwareness.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager](DYLIBS/AudioDSPManager.md)
- [/System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis](DYLIBS/AudioDataAnalysis.md)
- [/System/Library/PrivateFrameworks/AudioPasscode.framework/AudioPasscode](DYLIBS/AudioPasscode.md)
- [/System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication](DYLIBS/AudioServerApplication.md)
- [/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver](DYLIBS/AudioServerDriver.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP](DYLIBS/AudioServerDriverTransports_IOP.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib](DYLIBS/libSessionUtility.dylib.md)
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AudioTransportCommon.framework/AudioTransportCommon](DYLIBS/AudioTransportCommon.md)
- [/System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion](DYLIBS/AudiogramIngestion.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore](DYLIBS/AutoFillCore.md)
- [/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI](DYLIBS/AutoFillUI.md)
- [/System/Library/PrivateFrameworks/AutoLoop.framework/AutoLoop](DYLIBS/AutoLoop.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationMode](DYLIBS/AutomationMode.md)
- [/System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit](DYLIBS/AvailabilityKit.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/AvatarPersistence](DYLIBS/AvatarPersistence.md)
- [/System/Library/PrivateFrameworks/AvatarPoster.framework/AvatarPoster](DYLIBS/AvatarPoster.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation](DYLIBS/BackBoardHIDEventFoundation.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors](DYLIBS/BackBoardHIDEventProcessors.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices](DYLIBS/BackBoardServices.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BackgroundTaskAgent.framework/BackgroundTaskAgent](DYLIBS/BackgroundTaskAgent.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BagKit.framework/BagKit](DYLIBS/BagKit.md)
- [/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/BarcodeSupport](DYLIBS/BarcodeSupport.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI](DYLIBS/BaseBoardUI.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms](DYLIBS/BatteryAlgorithms.md)
- [/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter](DYLIBS/BatteryCenter.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BehaviorMiner.framework/BehaviorMiner](DYLIBS/BehaviorMiner.md)
- [/System/Library/PrivateFrameworks/BiomeDSL.framework/BiomeDSL](DYLIBS/BiomeDSL.md)
- [/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/BiomeFlexibleStorage](DYLIBS/BiomeFlexibleStorage.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync](DYLIBS/BiomeSync.md)
- [/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit](DYLIBS/BiometricKit.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/Fluid.framework/Fluid](DYLIBS/Fluid.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline](DYLIBS/MTLSpline.md)
- [/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport](DYLIBS/BiometricSupport.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BluetoothAudio.framework/BluetoothAudio](DYLIBS/BluetoothAudio.md)
- [/System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager](DYLIBS/BluetoothManager.md)
- [/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices](DYLIBS/BluetoothServices.md)
- [/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI](DYLIBS/BluetoothServicesUI.md)
- [/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices](DYLIBS/BoardServices.md)
- [/System/Library/PrivateFrameworks/Bom.framework/Bom](DYLIBS/Bom.md)
- [/System/Library/PrivateFrameworks/BookCoverUtility.framework/BookCoverUtility](DYLIBS/BookCoverUtility.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BookLibrary.framework/BookLibrary](DYLIBS/BookLibrary.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/BookLibraryCore](DYLIBS/BookLibraryCore.md)
- [/System/Library/PrivateFrameworks/BookUtility.framework/BookUtility](DYLIBS/BookUtility.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation.md)
- [/System/Library/PrivateFrameworks/BridgeCommons.framework/BridgeCommons](DYLIBS/BridgeCommons.md)
- [/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences](DYLIBS/BridgePreferences.md)
- [/System/Library/PrivateFrameworks/BridgeReporting.framework/BridgeReporting](DYLIBS/BridgeReporting.md)
- [/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl](DYLIBS/BrightnessControl.md)
- [/System/Library/PrivateFrameworks/BrookDataCollection.framework/BrookDataCollection](DYLIBS/BrookDataCollection.md)
- [/System/Library/PrivateFrameworks/BrookServices.framework/BrookServices](DYLIBS/BrookServices.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion](DYLIBS/BulletinDistributorCompanion.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService.md)
- [/System/Library/PrivateFrameworks/BusinessFoundation.framework/BusinessFoundation](DYLIBS/BusinessFoundation.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/BusinessServicesUI.framework/BusinessServicesUI](DYLIBS/BusinessServicesUI.md)
- [/System/Library/PrivateFrameworks/ButtonResolver.framework/ButtonResolver](DYLIBS/ButtonResolver.md)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary](DYLIBS/CBORLibrary.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/CDDataAccess](DYLIBS/CDDataAccess.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue](DYLIBS/DACoreDAVGlue.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport.md)
- [/System/Library/PrivateFrameworks/CDDataAccessExpress.framework/CDDataAccessExpress](DYLIBS/CDDataAccessExpress.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CPMLBestShim.framework/CPMLBestShim](DYLIBS/CPMLBestShim.md)
- [/System/Library/PrivateFrameworks/CPMS.framework/CPMS](DYLIBS/CPMS.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP](DYLIBS/CVNLP.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete.md)
- [/System/Library/PrivateFrameworks/CalDAV.framework/CalDAV](DYLIBS/CalDAV.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase](DYLIBS/CalendarDatabase.md)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation](DYLIBS/CalendarFoundation.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarMigration.framework/CalendarMigration](DYLIBS/CalendarMigration.md)
- [/System/Library/PrivateFrameworks/CalendarNotification.framework/CalendarNotification](DYLIBS/CalendarNotification.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/PrivateFrameworks/CameraKit.framework/CameraKit](DYLIBS/CameraKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork](DYLIBS/CaptiveNetwork.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarAssetUtils.framework/CarAssetUtils](DYLIBS/CarAssetUtils.md)
- [/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework](DYLIBS/CarCommandsUIFramework.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices.md)
- [/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup](DYLIBS/CarPlaySetup.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices.md)
- [/System/Library/PrivateFrameworks/CardKit.framework/CardKit](DYLIBS/CardKit.md)
- [/System/Library/PrivateFrameworks/CardServices.framework/CardServices](DYLIBS/CardServices.md)
- [/System/Library/PrivateFrameworks/Cards.framework/Cards](DYLIBS/Cards.md)
- [/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices](DYLIBS/CarouselPreferenceServices.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/Categories.framework/Categories](DYLIBS/Categories.md)
- [/System/Library/PrivateFrameworks/Celestial.framework/Celestial](DYLIBS/Celestial.md)
- [/System/Library/PrivateFrameworks/CellularBridgeUI.framework/CellularBridgeUI](DYLIBS/CellularBridgeUI.md)
- [/System/Library/PrivateFrameworks/CellularDataDiagnosticsSuite.framework/CellularDataDiagnosticsSuite](DYLIBS/CellularDataDiagnosticsSuite.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/CertInfo.framework/CertInfo](DYLIBS/CertInfo.md)
- [/System/Library/PrivateFrameworks/CertUI.framework/CertUI](DYLIBS/CertUI.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices](DYLIBS/CheckerBoardServices.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsSupport.framework/WidgetPreviewsSupport](DYLIBS/WidgetPreviewsSupport.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/ChunkingLibrary.framework/ChunkingLibrary](DYLIBS/ChunkingLibrary.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClarityBoardFoundation.framework/ClarityBoardFoundation](DYLIBS/ClarityBoardFoundation.md)
- [/System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation](DYLIBS/ClarityFoundation.md)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/ClassKitUI](DYLIBS/ClassKitUI.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit](DYLIBS/ClassroomKit.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices](DYLIBS/ClipServices.md)
- [/System/Library/PrivateFrameworks/ClipUIServices.framework/ClipUIServices](DYLIBS/ClipUIServices.md)
- [/System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications](DYLIBS/ClockComplications.md)
- [/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI](DYLIBS/ClockKitUI.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon](DYLIBS/CloudDocsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode](DYLIBS/CloudKitCode.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync](DYLIBS/CloudKitDistributedSync.md)
- [/System/Library/PrivateFrameworks/CloudMediaServicesInterfaceKit.framework/CloudMediaServicesInterfaceKit](DYLIBS/CloudMediaServicesInterfaceKit.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices](DYLIBS/CloudPhotoServices.md)
- [/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation](DYLIBS/CloudRecommendation.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices](DYLIBS/CloudServices.md)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/CloudSettings](DYLIBS/CloudSettings.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing](DYLIBS/CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI](DYLIBS/CloudSharingUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry](DYLIBS/CloudTelemetry.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/CognitiveHealth.framework/CognitiveHealth](DYLIBS/CognitiveHealth.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore](DYLIBS/CollectionViewCore.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommonAuth.framework/CommonAuth](DYLIBS/CommonAuth.md)
- [/System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities](DYLIBS/CommonUtilities.md)
- [/System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI](DYLIBS/CommunicationSafetySettingsUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter](DYLIBS/CommunicationsFilter.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera](DYLIBS/CompanionCamera.md)
- [/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon](DYLIBS/CompanionHealthDaemon.md)
- [/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices](DYLIBS/CompanionServices.md)
- [/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync](DYLIBS/CompanionSync.md)
- [/System/Library/PrivateFrameworks/CompassUI.framework/CompassUI](DYLIBS/CompassUI.md)
- [/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay](DYLIBS/ComplicationDisplay.md)
- [/System/Library/PrivateFrameworks/ConditionInducer.framework/ConditionInducer](DYLIBS/ConditionInducer.md)
- [/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel](DYLIBS/ConfigurationEngineModel.md)
- [/System/Library/PrivateFrameworks/ConstantClasses.framework/ConstantClasses](DYLIBS/ConstantClasses.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAssistantServices.framework/ContactsAssistantServices](DYLIBS/ContactsAssistantServices.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/ContactsDonation](DYLIBS/ContactsDonation.md)
- [/System/Library/PrivateFrameworks/ContactsDonationFeedback.framework/ContactsDonationFeedback](DYLIBS/ContactsDonationFeedback.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsMetrics.framework/ContactsMetrics](DYLIBS/ContactsMetrics.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContactsWidgetUI.framework/ContactsWidgetUI](DYLIBS/ContactsWidgetUI.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContainerManagerSystem.framework/ContainerManagerSystem](DYLIBS/ContainerManagerSystem.md)
- [/System/Library/PrivateFrameworks/ContainerManagerUser.framework/ContainerManagerUser](DYLIBS/ContainerManagerUser.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextKit.framework/ContextKit](DYLIBS/ContextKit.md)
- [/System/Library/PrivateFrameworks/ContextKitCore.framework/ContextKitCore](DYLIBS/ContextKitCore.md)
- [/System/Library/PrivateFrameworks/ContextKitExtraction.framework/ContextKitExtraction](DYLIBS/ContextKitExtraction.md)
- [/System/Library/PrivateFrameworks/ContextKitPrediction.framework/ContextKitPrediction](DYLIBS/ContextKitPrediction.md)
- [/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync](DYLIBS/ContextSync.md)
- [/System/Library/PrivateFrameworks/ContextualActionsClient.framework/ContextualActionsClient](DYLIBS/ContextualActionsClient.md)
- [/System/Library/PrivateFrameworks/ContextualSuggestionClient.framework/ContextualSuggestionClient](DYLIBS/ContextualSuggestionClient.md)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/ContextualUnderstanding](DYLIBS/ContextualUnderstanding.md)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/ContinuousDialogManagerService](DYLIBS/ContinuousDialogManagerService.md)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/Coordination.framework/Coordination](DYLIBS/Coordination.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreALD.framework/CoreALD](DYLIBS/CoreALD.md)
- [/System/Library/PrivateFrameworks/CoreAUC.framework/CoreAUC](DYLIBS/CoreAUC.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories](DYLIBS/CoreAccessories.md)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/CoreAccessoriesFeatures](DYLIBS/CoreAccessoriesFeatures.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreAppleCVA.framework/CoreAppleCVA](DYLIBS/CoreAppleCVA.md)
- [/System/Library/PrivateFrameworks/CoreAutoLayout.framework/CoreAutoLayout](DYLIBS/CoreAutoLayout.md)
- [/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI](DYLIBS/CoreBluetoothUI.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal](DYLIBS/CoreCDPUIInternal.md)
- [/System/Library/PrivateFrameworks/CoreCapture.framework/CoreCapture](DYLIBS/CoreCapture.md)
- [/System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl](DYLIBS/CoreCaptureControl.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreChartSwift.framework/CoreChartSwift](DYLIBS/CoreChartSwift.md)
- [/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV](DYLIBS/CoreDAV.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext](DYLIBS/CoreDuetContext.md)
- [/System/Library/PrivateFrameworks/CoreDuetDaemonProtocol.framework/CoreDuetDaemonProtocol](DYLIBS/CoreDuetDaemonProtocol.md)
- [/System/Library/PrivateFrameworks/CoreDuetSync.framework/CoreDuetSync](DYLIBS/CoreDuetSync.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji](DYLIBS/CoreEmoji.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI](DYLIBS/CoreFollowUpUI.md)
- [/System/Library/PrivateFrameworks/CoreGPS.framework/CoreGPS](DYLIBS/CoreGPS.md)
- [/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest](DYLIBS/CoreGPSTest.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred](DYLIBS/CoreIDCred.md)
- [/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder](DYLIBS/CoreIDCredBuilder.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreIK.framework/CoreIK](DYLIBS/CoreIK.md)
- [/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor](DYLIBS/CoreIndoor.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf](DYLIBS/CoreLocationProtobuf.md)
- [/System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay](DYLIBS/CoreLocationReplay.md)
- [/System/Library/PrivateFrameworks/CoreMaterial.framework/CoreMaterial](DYLIBS/CoreMaterial.md)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream.md)
- [/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms](DYLIBS/CoreMotionAlgorithms.md)
- [/System/Library/PrivateFrameworks/CoreMotionModels.framework/CoreMotionModels](DYLIBS/CoreMotionModels.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreNameParser.framework/CoreNameParser](DYLIBS/CoreNameParser.md)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreOCModules.framework/CoreOCModules](DYLIBS/CoreOCModules.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreOptimization.framework/CoreOptimization](DYLIBS/CoreOptimization.md)
- [/System/Library/PrivateFrameworks/CorePDF.framework/CorePDF](DYLIBS/CorePDF.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers](DYLIBS/CorePhoneNumbers.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CorePrediction.framework/CorePrediction](DYLIBS/CorePrediction.md)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/CorePrescriptionLite](DYLIBS/CorePrescriptionLite.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO](DYLIBS/CoreRealityIO.md)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents](DYLIBS/CoreRecents.md)
- [/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition](DYLIBS/CoreRecognition.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite](DYLIBS/CoreRepairLite.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine](DYLIBS/CoreRoutine.md)
- [/System/Library/PrivateFrameworks/CoreSDB.framework/CoreSDB](DYLIBS/CoreSDB.md)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG](DYLIBS/CoreSVG.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal](DYLIBS/CoreServicesInternal.md)
- [/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore](DYLIBS/CoreServicesStore.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSpeechGazeTracking.framework/CoreSpeechGazeTracking](DYLIBS/CoreSpeechGazeTracking.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsML.framework/CoreSuggestionsML](DYLIBS/CoreSuggestionsML.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication](DYLIBS/CoreSymbolication.md)
- [/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/CoreThemeDefinition](DYLIBS/CoreThemeDefinition.md)
- [/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread](DYLIBS/CoreThread.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio](DYLIBS/CoreThreadRadio.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime](DYLIBS/CoreTime.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsExtras.framework/CoreUtilsExtras](DYLIBS/CoreUtilsExtras.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreUtilsUI.framework/CoreUtilsUI](DYLIBS/CoreUtilsUI.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cornobble.framework/Cornobble](DYLIBS/Cornobble.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport](DYLIBS/CrashReporterSupport.md)
- [/System/Library/PrivateFrameworks/CrisisResources.framework/CrisisResources](DYLIBS/CrisisResources.md)
- [/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging](DYLIBS/CryptoKitCBridging.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DAAPKit.framework/DAAPKit](DYLIBS/DAAPKit.md)
- [/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework](DYLIBS/DAEASOAuthFramework.md)
- [/System/Library/PrivateFrameworks/DASDaemon.framework/DASDaemon](DYLIBS/DASDaemon.md)
- [/System/Library/PrivateFrameworks/DASDelegate.framework/DASDelegate](DYLIBS/DASDelegate.md)
- [/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary](DYLIBS/DEPClientLibrary.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary](DYLIBS/DMCEnrollmentLibrary.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DRMFoundation.framework/DRMFoundation](DYLIBS/DRMFoundation.md)
- [/System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing](DYLIBS/DSRemotePairing.md)
- [/System/Library/PrivateFrameworks/DTXConnectionServices.framework/DTXConnectionServices](DYLIBS/DTXConnectionServices.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities](DYLIBS/DVTInstrumentsUtilities.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess](DYLIBS/DataAccess.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DACardDAV](DYLIBS/DACardDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue](DYLIBS/DACoreDAVGlue.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DAIMAPNotes.framework/DAIMAPNotes](DYLIBS/DAIMAPNotes.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DALDAP](DYLIBS/DALDAP.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DASubCal](DYLIBS/DASubCal.md)
- [/System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress](DYLIBS/DataAccessExpress.md)
- [/System/Library/PrivateFrameworks/DataAccessUI.framework/DataAccessUI](DYLIBS/DataAccessUI.md)
- [/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices](DYLIBS/DataDeliveryServices.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/PlugIns/PhoneNumbers.plugin/PhoneNumbers](DYLIBS/PhoneNumbers.md)
- [/System/Library/PrivateFrameworks/DataDetectorsNaturalLanguage.framework/DataDetectorsNaturalLanguage](DYLIBS/DataDetectorsNaturalLanguage.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration](DYLIBS/DataMigration.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/DendriteIngest](DYLIBS/DendriteIngest.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DeviceActivityConductor.framework/DeviceActivityConductor](DYLIBS/DeviceActivityConductor.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal](DYLIBS/DeviceCheckInternal.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore](DYLIBS/DeviceDiscoveryUICore.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DeviceManagementTools.framework/DeviceManagementTools](DYLIBS/DeviceManagementTools.md)
- [/System/Library/PrivateFrameworks/DeviceOMatic.framework/DeviceOMatic](DYLIBS/DeviceOMatic.md)
- [/System/Library/PrivateFrameworks/DevicePresence.framework/DevicePresence](DYLIBS/DevicePresence.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/DeviceToDeviceManager](DYLIBS/DeviceToDeviceManager.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions](DYLIBS/DiagnosticExtensions.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon](DYLIBS/DiagnosticExtensionsDaemon.md)
- [/System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/DiagnosticLogCollection](DYLIBS/DiagnosticLogCollection.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest](DYLIBS/DiagnosticRequest.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit](DYLIBS/DiagnosticsKit.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport](DYLIBS/DiagnosticsSupport.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices](DYLIBS/DictionaryServices.md)
- [/System/Library/PrivateFrameworks/DictionaryUI.framework/DictionaryUI](DYLIBS/DictionaryUI.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DigitalTouchShared.framework/DigitalTouchShared](DYLIBS/DigitalTouchShared.md)
- [/System/Library/PrivateFrameworks/Disembark.framework/Disembark](DYLIBS/Disembark.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI](DYLIBS/DisembarkUI.md)
- [/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration](DYLIBS/DiskArbitration.md)
- [/System/Library/PrivateFrameworks/DiskImages.framework/DiskImages](DYLIBS/DiskImages.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedSensing.framework/DistributedSensing](DYLIBS/DistributedSensing.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb](DYLIBS/DoNotDisturb.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbKit.framework/DoNotDisturbKit](DYLIBS/DoNotDisturbKit.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera](DYLIBS/DocumentCamera.md)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient](DYLIBS/DocumentUnderstandingClient.md)
- [/System/Library/PrivateFrameworks/DragUI.framework/DragUI](DYLIBS/DragUI.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DrawingKit.framework/DrawingKit](DYLIBS/DrawingKit.md)
- [/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement](DYLIBS/DriverManagement.md)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/EAFirmwareUpdater.framework/EAFirmwareUpdater](DYLIBS/EAFirmwareUpdater.md)
- [/System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X](DYLIBS/EAP8021X.md)
- [/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity](DYLIBS/EDPSecurity.md)
- [/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe](DYLIBS/EXDisplayPipe.md)
- [/System/Library/PrivateFrameworks/EasyConfig.framework/EasyConfig](DYLIBS/EasyConfig.md)
- [/System/Library/PrivateFrameworks/EditScript.framework/EditScript](DYLIBS/EditScript.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing](DYLIBS/EmailAddressing.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset](DYLIBS/EmbeddedDataReset.md)
- [/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService](DYLIBS/EmbeddingService.md)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts](DYLIBS/EmergencyAlerts.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiKit.framework/EmojiKit](DYLIBS/EmojiKit.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/EncoreXPCService.framework/EncoreXPCService](DYLIBS/EncoreXPCService.md)
- [/System/Library/PrivateFrameworks/Engram.framework/Engram](DYLIBS/Engram.md)
- [/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState](DYLIBS/EnhancedLoggingState.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Frameworks/LoopKitGeneratedKernels.framework/LoopKitGeneratedKernels](DYLIBS/LoopKitGeneratedKernels.md)
- [/System/Library/PrivateFrameworks/EventKitTCCUI.framework/EventKitTCCUI](DYLIBS/EventKitTCCUI.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/ExchangeSync](DYLIBS/ExchangeSync.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DAEAS](DYLIBS/DAEAS.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/ESDaemonSupport.framework/ESDaemonSupport](DYLIBS/ESDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/ExchangeSyncExpress](DYLIBS/ExchangeSyncExpress.md)
- [/System/Library/PrivateFrameworks/ExposureNotificationDaemon.framework/ExposureNotificationDaemon](DYLIBS/ExposureNotificationDaemon.md)
- [/System/Library/PrivateFrameworks/EyeRelief.framework/EyeRelief](DYLIBS/EyeRelief.md)
- [/System/Library/PrivateFrameworks/Eyedropper.framework/Eyedropper](DYLIBS/Eyedropper.md)
- [/System/Library/PrivateFrameworks/FMCore.framework/FMCore](DYLIBS/FMCore.md)
- [/System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite](DYLIBS/FMCoreLite.md)
- [/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI](DYLIBS/FMCoreUI.md)
- [/System/Library/PrivateFrameworks/FMF.framework/FMF](DYLIBS/FMF.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFUI.framework/FMFUI](DYLIBS/FMFUI.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking](DYLIBS/FMNetworking.md)
- [/System/Library/PrivateFrameworks/FRC.framework/FRC](DYLIBS/FRC.md)
- [/System/Library/PrivateFrameworks/FSEvents.framework/FSEvents](DYLIBS/FSEvents.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FTAWD.framework/FTAWD](DYLIBS/FTAWD.md)
- [/System/Library/PrivateFrameworks/FTClientServices.framework/FTClientServices](DYLIBS/FTClientServices.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC](DYLIBS/FamilyControlsObjC.md)
- [/System/Library/PrivateFrameworks/FamilyNotification.framework/FamilyNotification](DYLIBS/FamilyNotification.md)
- [/System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags](DYLIBS/FeatureFlags.md)
- [/System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport](DYLIBS/FeatureFlagsSupport.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger](DYLIBS/FeedbackLogger.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry](DYLIBS/FileProviderTelemetry.md)
- [/System/Library/PrivateFrameworks/FilesActionsUI.framework/FilesActionsUI](DYLIBS/FilesActionsUI.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/FinHealth](DYLIBS/FinHealth.md)
- [/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore](DYLIBS/FinHealthCore.md)
- [/System/Library/PrivateFrameworks/FinHealthInsights.framework/FinHealthInsights](DYLIBS/FinHealthInsights.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyCrypto.framework/FindMyCrypto](DYLIBS/FindMyCrypto.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyDeviceUI.framework/FindMyDeviceUI](DYLIBS/FindMyDeviceUI.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyLocateObjCWrapper.framework/FindMyLocateObjCWrapper](DYLIBS/FindMyLocateObjCWrapper.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction](DYLIBS/FindMyServerInteraction.md)
- [/System/Library/PrivateFrameworks/FindMyStorage.framework/FindMyStorage](DYLIBS/FindMyStorage.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FindMyUnsafeAsyncBridging.framework/FindMyUnsafeAsyncBridging](DYLIBS/FindMyUnsafeAsyncBridging.md)
- [/System/Library/PrivateFrameworks/Fitness.framework/Fitness](DYLIBS/Fitness.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingCore.framework/FitnessCoachingCore](DYLIBS/FitnessCoachingCore.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingHealthServices.framework/FitnessCoachingHealthServices](DYLIBS/FitnessCoachingHealthServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FlexMusicKit.framework/FlexMusicKit](DYLIBS/FlexMusicKit.md)
- [/System/Library/PrivateFrameworks/FlightUtilities.framework/FlightUtilities](DYLIBS/FlightUtilities.md)
- [/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore](DYLIBS/FlightUtilitiesCore.md)
- [/System/Library/PrivateFrameworks/FlowFrameKit.framework/FlowFrameKit](DYLIBS/FlowFrameKit.md)
- [/System/Library/PrivateFrameworks/Fluid.framework/Fluid](DYLIBS/Fluid.md)
- [/System/Library/PrivateFrameworks/Focus.framework/Focus](DYLIBS/Focus.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/FontServices](DYLIBS/FontServices.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib](DYLIBS/libGSFontCache.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libType1Scaler.dylib](DYLIBS/libType1Scaler.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libhvf.dylib](DYLIBS/libhvf.dylib.md)
- [/System/Library/PrivateFrameworks/FriendKit.framework/FriendKit](DYLIBS/FriendKit.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker](DYLIBS/FusionTracker.md)
- [/System/Library/PrivateFrameworks/Futhark.framework/Futhark](DYLIBS/Futhark.md)
- [/System/Library/PrivateFrameworks/GLTools.framework/GLTools](DYLIBS/GLTools.md)
- [/System/Library/PrivateFrameworks/GLToolsCore.framework/GLToolsCore](DYLIBS/GLToolsCore.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libComposeFilters.dylib](DYLIBS/libComposeFilters.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompiler.dylib](DYLIBS/libGPUCompiler.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerUtils.dylib](DYLIBS/libGPUCompilerUtils.dylib.md)
- [/System/Library/PrivateFrameworks/GPURawCounter.framework/GPURawCounter](DYLIBS/GPURawCounter.md)
- [/System/Library/PrivateFrameworks/GPUSupport.framework/libGPUSupportMercury.dylib](DYLIBS/libGPUSupportMercury.dylib.md)
- [/System/Library/PrivateFrameworks/GPUTools.framework/GPUTools](DYLIBS/GPUTools.md)
- [/System/Library/PrivateFrameworks/GPUToolsCore.framework/GPUToolsCore](DYLIBS/GPUToolsCore.md)
- [/System/Library/PrivateFrameworks/GPUToolsPlayback.framework/GPUToolsPlayback](DYLIBS/GPUToolsPlayback.md)
- [/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport](DYLIBS/GPUToolsTransport.md)
- [/System/Library/PrivateFrameworks/GPUToolsiOS.framework/GPUToolsiOS](DYLIBS/GPUToolsiOS.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation](DYLIBS/GameControllerFoundation.md)
- [/System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings](DYLIBS/GameControllerSettings.md)
- [/System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices](DYLIBS/GameKitServices.md)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy.md)
- [/System/Library/PrivateFrameworks/GamePolicyServices.framework/GamePolicyServices](DYLIBS/GamePolicyServices.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage](DYLIBS/GenerationalStorage.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics](DYLIBS/GeoAnalytics.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/GeoServicesCore.framework/GeoServicesCore](DYLIBS/GeoServicesCore.md)
- [/System/Library/PrivateFrameworks/GeoShifter.framework/GeoShifter](DYLIBS/GeoShifter.md)
- [/System/Library/PrivateFrameworks/GeoUIFramework.framework/GeoUIFramework](DYLIBS/GeoUIFramework.md)
- [/System/Library/PrivateFrameworks/Geometry.framework/Geometry](DYLIBS/Geometry.md)
- [/System/Library/PrivateFrameworks/GradientPoster.framework/GradientPoster](DYLIBS/GradientPoster.md)
- [/System/Library/PrivateFrameworks/GraphVisualizer.framework/GraphVisualizer](DYLIBS/GraphVisualizer.md)
- [/System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices](DYLIBS/GraphicsServices.md)
- [/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices](DYLIBS/GridDataServices.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices](DYLIBS/H10ISPServices.md)
- [/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices](DYLIBS/H16ISPServices.md)
- [/System/Library/PrivateFrameworks/HAENotifications.framework/HAENotifications](DYLIBS/HAENotifications.md)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing](DYLIBS/HDRProcessing.md)
- [/System/Library/PrivateFrameworks/HID.framework/HID](DYLIBS/HID.md)
- [/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics](DYLIBS/HIDAnalytics.md)
- [/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay](DYLIBS/HIDDisplay.md)
- [/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences](DYLIBS/HIDPreferences.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment](DYLIBS/HRTFEnrollment.md)
- [/System/Library/PrivateFrameworks/HSAAuthentication.framework/HSAAuthentication](DYLIBS/HSAAuthentication.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient](DYLIBS/HangTracerSettingsClient.md)
- [/System/Library/PrivateFrameworks/Haptics.framework/Haptics](DYLIBS/Haptics.md)
- [/System/Library/PrivateFrameworks/HardwareDiagnostics.framework/HardwareDiagnostics](DYLIBS/HardwareDiagnostics.md)
- [/System/Library/PrivateFrameworks/HardwareSupport.framework/HardwareSupport](DYLIBS/HardwareSupport.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings](DYLIBS/HeadphoneSettings.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms](DYLIBS/HealthAlgorithms.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon](DYLIBS/HealthAppHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport](DYLIBS/HealthAppHealthDaemonSupport.md)
- [/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices](DYLIBS/HealthAppServices.md)
- [/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration](DYLIBS/HealthArticlesGeneration.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation](DYLIBS/HealthDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/HealthDiagnosticExtensionCore](DYLIBS/HealthDiagnosticExtensionCore.md)
- [/System/Library/PrivateFrameworks/HealthDomainsTools.framework/HealthDomainsTools](DYLIBS/HealthDomainsTools.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing](DYLIBS/HealthHearing.md)
- [/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon](DYLIBS/HealthHearingDaemon.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications](DYLIBS/HealthMedications.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin](DYLIBS/HealthMedicationsDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVision.framework/HealthMedicationsVision](DYLIBS/HealthMedicationsVision.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI](DYLIBS/HealthMedicationsVisionUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI](DYLIBS/HealthMedicationsWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesUI.framework/HealthMenstrualCyclesUI](DYLIBS/HealthMenstrualCyclesUI.md)
- [/System/Library/PrivateFrameworks/HealthMobility.framework/HealthMobility](DYLIBS/HealthMobility.md)
- [/System/Library/PrivateFrameworks/HealthMobilityDaemon.framework/HealthMobilityDaemon](DYLIBS/HealthMobilityDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsConceptsSupport.framework/HealthRecordsConceptsSupport](DYLIBS/HealthRecordsConceptsSupport.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthRecordsWalletSupport.framework/HealthRecordsWalletSupport](DYLIBS/HealthRecordsWalletSupport.md)
- [/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore](DYLIBS/HearingCore.md)
- [/System/Library/PrivateFrameworks/HearingMLHelper.framework/HearingMLHelper](DYLIBS/HearingMLHelper.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth](DYLIBS/HeartHealth.md)
- [/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon](DYLIBS/HeartHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI](DYLIBS/HeartRhythmUI.md)
- [/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal](DYLIBS/Heimdal.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/HeroDataClient.framework/HeroDataClient](DYLIBS/HeroDataClient.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI](DYLIBS/HomeAI.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeCommunicationUIFramework.framework/HomeCommunicationUIFramework](DYLIBS/HomeCommunicationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore](DYLIBS/HomeKitBackingStore.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter](DYLIBS/HomeKitEventRouter.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures](DYLIBS/HomeKitFeatures.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils](DYLIBS/HomeMessagingUtils.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeRecommendationEngine.framework/HomeRecommendationEngine](DYLIBS/HomeRecommendationEngine.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeSharing.framework/HomeSharing](DYLIBS/HomeSharing.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextServices.framework/HoverTextServices](DYLIBS/HoverTextServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IAP.framework/IAP](DYLIBS/IAP.md)
- [/System/Library/PrivateFrameworks/IAPAuthentication.framework/IAPAuthentication](DYLIBS/IAPAuthentication.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/IDSBlastDoorSupport](DYLIBS/IDSBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IDSHashPersistence.framework/IDSHashPersistence](DYLIBS/IDSHashPersistence.md)
- [/System/Library/PrivateFrameworks/IDSKVStore.framework/IDSKVStore](DYLIBS/IDSKVStore.md)
- [/System/Library/PrivateFrameworks/IMAVCore.framework/IMAVCore](DYLIBS/IMAVCore.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMCorePipeline.framework/IMCorePipeline](DYLIBS/IMCorePipeline.md)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/IMDMessageServices](DYLIBS/IMDMessageServices.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation](DYLIBS/IMFoundation.md)
- [/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI](DYLIBS/IMSharedUI.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/IMTranscoding](DYLIBS/IMTranscoding.md)
- [/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent](DYLIBS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferServices](DYLIBS/IMTransferServices.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo](DYLIBS/IOAccelMemoryInfo.md)
- [/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator](DYLIBS/IOAccelerator.md)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU](DYLIBS/IOGPU.md)
- [/System/Library/PrivateFrameworks/IOImageLoader.framework/IOImageLoader](DYLIBS/IOImageLoader.md)
- [/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten](DYLIBS/IOKitten.md)
- [/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer](DYLIBS/IOMobileFramebuffer.md)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator](DYLIBS/IOSurfaceAccelerator.md)
- [/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost](DYLIBS/IOUSBHost.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/ITMLKit.framework/ITMLKit](DYLIBS/ITMLKit.md)
- [/System/Library/PrivateFrameworks/IXATestAppRelay.framework/IXATestAppRelay](DYLIBS/IXATestAppRelay.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/IdleTimerHosting.framework/IdleTimerHosting](DYLIBS/IdleTimerHosting.md)
- [/System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices](DYLIBS/IdleTimerServices.md)
- [/System/Library/PrivateFrameworks/ImageHarmonizationKit.framework/ImageHarmonizationKit](DYLIBS/ImageHarmonizationKit.md)
- [/System/Library/PrivateFrameworks/InAppMessages.framework/InAppMessages](DYLIBS/InAppMessages.md)
- [/System/Library/PrivateFrameworks/InAppMessagesCore.framework/InAppMessagesCore](DYLIBS/InAppMessagesCore.md)
- [/System/Library/PrivateFrameworks/IncomingCallFilter.framework/IncomingCallFilter](DYLIBS/IncomingCallFilter.md)
- [/System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam](DYLIBS/InertiaCam.md)
- [/System/Library/PrivateFrameworks/InfoQueryPersonalizationFeatures.framework/InfoQueryPersonalizationFeatures](DYLIBS/InfoQueryPersonalizationFeatures.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputContext.framework/InputContext](DYLIBS/InputContext.md)
- [/System/Library/PrivateFrameworks/InputTranscoder.framework/InputTranscoder](DYLIBS/InputTranscoder.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination](DYLIBS/InstallCoordination.md)
- [/System/Library/PrivateFrameworks/InstallProgress.framework/InstallProgress](DYLIBS/InstallProgress.md)
- [/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary](DYLIBS/InstalledContentLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/IntelligencePlatformCompute](DYLIBS/IntelligencePlatformCompute.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting](DYLIBS/IntelligentRouting.md)
- [/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon](DYLIBS/IntelligentRoutingDaemon.md)
- [/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore](DYLIBS/IntentsCore.md)
- [/System/Library/PrivateFrameworks/IntentsFoundation.framework/IntentsFoundation](DYLIBS/IntentsFoundation.md)
- [/System/Library/PrivateFrameworks/IntentsServices.framework/IntentsServices](DYLIBS/IntentsServices.md)
- [/System/Library/PrivateFrameworks/IntentsUICardKitProviderSupport.framework/IntentsUICardKitProviderSupport](DYLIBS/IntentsUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/InternationalTextSearch.framework/InternationalTextSearch](DYLIBS/InternationalTextSearch.md)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences](DYLIBS/IntlPreferences.md)
- [/System/Library/PrivateFrameworks/IntlPreferencesUI.framework/IntlPreferencesUI](DYLIBS/IntlPreferencesUI.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/JITAppKit.framework/JITAppKit](DYLIBS/JITAppKit.md)
- [/System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth](DYLIBS/JasperDepth.md)
- [/System/Library/PrivateFrameworks/Jet.framework/Jet](DYLIBS/Jet.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetPack.framework/JetPack](DYLIBS/JetPack.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/JoinRequests.framework/JoinRequests](DYLIBS/JoinRequests.md)
- [/System/Library/PrivateFrameworks/KRExperiments.framework/KRExperiments](DYLIBS/KRExperiments.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/KeyboardServices.framework/KeyboardServices](DYLIBS/KeyboardServices.md)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/Koa.framework/Koa](DYLIBS/Koa.md)
- [/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper](DYLIBS/KoaMapper.md)
- [/System/Library/PrivateFrameworks/LACC.framework/LACC](DYLIBS/LACC.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/LatentSemanticMapping.framework/LatentSemanticMapping](DYLIBS/LatentSemanticMapping.md)
- [/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures](DYLIBS/LearnedFeatures.md)
- [/System/Library/PrivateFrameworks/LegacyGameKit.framework/LegacyGameKit](DYLIBS/LegacyGameKit.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework](DYLIBS/LighthouseBitacoraFramework.md)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore](DYLIBS/LighthouseCoreMLFeatureStore.md)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLModelAnalysis.framework/LighthouseCoreMLModelAnalysis](DYLIBS/LighthouseCoreMLModelAnalysis.md)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/LighthouseCoreMLModelStore](DYLIBS/LighthouseCoreMLModelStore.md)
- [/System/Library/PrivateFrameworks/LighthouseDictation.framework/LighthouseDictation](DYLIBS/LighthouseDictation.md)
- [/System/Library/PrivateFrameworks/LighthouseModelMonitoring.framework/LighthouseModelMonitoring](DYLIBS/LighthouseModelMonitoring.md)
- [/System/Library/PrivateFrameworks/LighthouseQuartz.framework/LighthouseQuartz](DYLIBS/LighthouseQuartz.md)
- [/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking](DYLIBS/LimitAdTracking.md)
- [/System/Library/PrivateFrameworks/LinguisticData.framework/LinguisticData](DYLIBS/LinguisticData.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsFoundation.framework/LiveExecutionResultsFoundation](DYLIBS/LiveExecutionResultsFoundation.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsRuntime.framework/LiveExecutionResultsRuntime](DYLIBS/LiveExecutionResultsRuntime.md)
- [/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS](DYLIBS/LiveFS.md)
- [/System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper](DYLIBS/LiveFSFPHelper.md)
- [/System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices](DYLIBS/LiveSpeechServices.md)
- [/System/Library/PrivateFrameworks/LiveSpeechUI.framework/LiveSpeechUI](DYLIBS/LiveSpeechUI.md)
- [/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription](DYLIBS/LiveTranscription.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI](DYLIBS/LocalAuthenticationPrivateUI.md)
- [/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge](DYLIBS/LocalSpeechRecognitionBridge.md)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit](DYLIBS/LocalStatusKit.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode](DYLIBS/LockdownMode.md)
- [/System/Library/PrivateFrameworks/LockoutUI.framework/LockoutUI](DYLIBS/LockoutUI.md)
- [/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport](DYLIBS/LoggingSupport.md)
- [/System/Library/PrivateFrameworks/LoginKit.framework/LoginKit](DYLIBS/LoginKit.md)
- [/System/Library/PrivateFrameworks/LoginPerformanceKit.framework/LoginPerformanceKit](DYLIBS/LoginPerformanceKit.md)
- [/System/Library/PrivateFrameworks/LoginUILogViewer.framework/LoginUILogViewer](DYLIBS/LoginUILogViewer.md)
- [/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode](DYLIBS/LowPowerMode.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MIL.framework/MIL](DYLIBS/MIL.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MLAssetIO.framework/MLAssetIO](DYLIBS/MLAssetIO.md)
- [/System/Library/PrivateFrameworks/MLCompilerRuntime.framework/MLCompilerRuntime](DYLIBS/MLCompilerRuntime.md)
- [/System/Library/PrivateFrameworks/MLCompilerServices.framework/MLCompilerServices](DYLIBS/MLCompilerServices.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/MLKit](DYLIBS/MLKit.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime](DYLIBS/MLRuntime.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MMCSServices.framework/MMCSServices](DYLIBS/MMCSServices.md)
- [/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO](DYLIBS/MOVStreamIO.md)
- [/System/Library/PrivateFrameworks/MPUFoundation.framework/MPUFoundation](DYLIBS/MPUFoundation.md)
- [/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor](DYLIBS/MSUDataAccessor.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/libMTLCompilerHelper.dylib](DYLIBS/libMTLCompilerHelper.dylib.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/MacinTalk](DYLIBS/MacinTalk.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailKit.framework/MailKit](DYLIBS/MailKit.md)
- [/System/Library/PrivateFrameworks/MailServices.framework/MailServices](DYLIBS/MailServices.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MailWebProcessSupport.framework/MailWebProcessSupport](DYLIBS/MailWebProcessSupport.md)
- [/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging](DYLIBS/MallocStackLogging.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI](DYLIBS/ManagedConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC](DYLIBS/ManagedSettingsObjC.md)
- [/System/Library/PrivateFrameworks/ManagedSettingsSupport.framework/ManagedSettingsSupport](DYLIBS/ManagedSettingsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marco.framework/Marco](DYLIBS/Marco.md)
- [/System/Library/PrivateFrameworks/MarkupUI.framework/MarkupUI](DYLIBS/MarkupUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit](DYLIBS/MaterialKit.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl](DYLIBS/MediaControl.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService](DYLIBS/MediaConversionService.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation](DYLIBS/MediaFoundation.md)
- [/System/Library/PrivateFrameworks/MediaGroups.framework/MediaGroups](DYLIBS/MediaGroups.md)
- [/System/Library/PrivateFrameworks/MediaGroupsDaemon.framework/MediaGroupsDaemon](DYLIBS/MediaGroupsDaemon.md)
- [/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit](DYLIBS/MediaKit.md)
- [/System/Library/PrivateFrameworks/MediaLibraryCore.framework/MediaLibraryCore](DYLIBS/MediaLibraryCore.md)
- [/System/Library/PrivateFrameworks/MediaML.framework/MediaML](DYLIBS/MediaML.md)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/MediaMLServices](DYLIBS/MediaMLServices.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlatform.framework/MediaPlatform](DYLIBS/MediaPlatform.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaPlayerUI.framework/MediaPlayerUI](DYLIBS/MediaPlayerUI.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet](DYLIBS/MediaSafetyNet.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream](DYLIBS/MediaStream.md)
- [/System/Library/PrivateFrameworks/MemoryDiagnostics.framework/MemoryDiagnostics](DYLIBS/MemoryDiagnostics.md)
- [/System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal](DYLIBS/MenstrualAlgorithmsInternal.md)
- [/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth](DYLIBS/MentalHealth.md)
- [/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon](DYLIBS/MentalHealthDaemon.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthWidgetUI.framework/MentalHealthWidgetUI](DYLIBS/MentalHealthWidgetUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/MailServices/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/Message.framework/MailServices/POP.framework/POP](DYLIBS/POP.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageLegacy.framework/MailServices/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/MessageLegacy.framework/MessageLegacy](DYLIBS/MessageLegacy.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessageSupport.framework/MessageSupport](DYLIBS/MessageSupport.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore](DYLIBS/MetricKitCore.md)
- [/System/Library/PrivateFrameworks/MetricKitServices.framework/MetricKitServices](DYLIBS/MetricKitServices.md)
- [/System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource](DYLIBS/MetricKitSource.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement](DYLIBS/MetricMeasurement.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MetricsKit.framework/MetricsKit](DYLIBS/MetricsKit.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MilAneflow.framework/MilAneflow](DYLIBS/MilAneflow.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater](DYLIBS/MobileAccessoryUpdater.md)
- [/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation](DYLIBS/MobileActivation.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileAssetUpdater.framework/MobileAssetUpdater](DYLIBS/MobileAssetUpdater.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth](DYLIBS/MobileBluetooth.md)
- [/System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager](DYLIBS/MobileContainerManager.md)
- [/System/Library/PrivateFrameworks/MobileDeviceLink.framework/MobileDeviceLink](DYLIBS/MobileDeviceLink.md)
- [/System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons](DYLIBS/MobileIcons.md)
- [/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI](DYLIBS/MobileIdentityServiceUI.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation](DYLIBS/MobileInstallation.md)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag.md)
- [/System/Library/PrivateFrameworks/MobileLookup.framework/MobileLookup](DYLIBS/MobileLookup.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration](DYLIBS/MobileObliteration.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/PlugIns/Safari.wkbundle/Safari](DYLIBS/Safari.md)
- [/System/Library/PrivateFrameworks/MobileSafariSwift.framework/MobileSafariSwift](DYLIBS/MobileSafariSwift.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate](DYLIBS/MobileSoftwareUpdate.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage](DYLIBS/MobileStorage.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileSync.framework/MobileSync](DYLIBS/MobileSync.md)
- [/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices](DYLIBS/MobileSystemServices.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/MobileTimerUI.framework/MobileTimerUI](DYLIBS/MobileTimerUI.md)
- [/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi](DYLIBS/MobileWiFi.md)
- [/System/Library/PrivateFrameworks/ModalityXObjects.framework/ModalityXObjects](DYLIBS/ModalityXObjects.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/MonogramPoster.framework/MonogramPoster](DYLIBS/MonogramPoster.md)
- [/System/Library/PrivateFrameworks/Montreal.framework/Montreal](DYLIBS/Montreal.md)
- [/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets](DYLIBS/MorphunAssets.md)
- [/System/Library/PrivateFrameworks/MorphunSwift.framework/MorphunSwift](DYLIBS/MorphunSwift.md)
- [/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging](DYLIBS/MotionSensorLogging.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/MultitouchSessionFilterSupport](DYLIBS/MultitouchSessionFilterSupport.md)
- [/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport](DYLIBS/MultitouchSupport.md)
- [/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI](DYLIBS/MusicCarDisplayUI.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicKitPlaybackSupport.framework/MusicKitPlaybackSupport](DYLIBS/MusicKitPlaybackSupport.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicSettingsSupport.framework/MusicSettingsSupport](DYLIBS/MusicSettingsSupport.md)
- [/System/Library/PrivateFrameworks/MusicStoreUI.framework/MusicStoreUI](DYLIBS/MusicStoreUI.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NCLaunchStats.framework/NCLaunchStats](DYLIBS/NCLaunchStats.md)
- [/System/Library/PrivateFrameworks/NLP.framework/NLP](DYLIBS/NLP.md)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/NLPLearner](DYLIBS/NLPLearner.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit](DYLIBS/NPTKit.md)
- [/System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry](DYLIBS/NanoAppRegistry.md)
- [/System/Library/PrivateFrameworks/NanoAudioControl.framework/NanoAudioControl](DYLIBS/NanoAudioControl.md)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup](DYLIBS/NanoBackup.md)
- [/System/Library/PrivateFrameworks/NanoComplicationSettings.framework/NanoComplicationSettings](DYLIBS/NanoComplicationSettings.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/NanoLeash](DYLIBS/NanoLeash.md)
- [/System/Library/PrivateFrameworks/NanoMailCompanionUI.framework/NanoMailCompanionUI](DYLIBS/NanoMailCompanionUI.md)
- [/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer](DYLIBS/NanoMailKitServer.md)
- [/System/Library/PrivateFrameworks/NanoMediaAPI.framework/NanoMediaAPI](DYLIBS/NanoMediaAPI.md)
- [/System/Library/PrivateFrameworks/NanoMediaBridgeUI.framework/NanoMediaBridgeUI](DYLIBS/NanoMediaBridgeUI.md)
- [/System/Library/PrivateFrameworks/NanoMediaRemote.framework/NanoMediaRemote](DYLIBS/NanoMediaRemote.md)
- [/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync](DYLIBS/NanoMusicSync.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore](DYLIBS/NanoPhotosCore.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync](DYLIBS/NanoPreferencesSync.md)
- [/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry](DYLIBS/NanoRegistry.md)
- [/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber](DYLIBS/NanoResourceGrabber.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings](DYLIBS/NanoSystemSettings.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NanoUniverse](DYLIBS/NanoUniverse.md)
- [/System/Library/PrivateFrameworks/NanoWeatherComplicationsCompanion.framework/NanoWeatherComplicationsCompanion](DYLIBS/NanoWeatherComplicationsCompanion.md)
- [/System/Library/PrivateFrameworks/NanoWeatherKitUICompanion.framework/NanoWeatherKitUICompanion](DYLIBS/NanoWeatherKitUICompanion.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory](DYLIBS/NearFieldAccessory.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices](DYLIBS/NearFieldPrivateServices.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions](DYLIBS/NearbySessions.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/NeighborhoodActivityConduit](DYLIBS/NeighborhoodActivityConduit.md)
- [/System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities](DYLIBS/NetAppsUtilities.md)
- [/System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI](DYLIBS/NetAppsUtilitiesUI.md)
- [/System/Library/PrivateFrameworks/Netrb.framework/Netrb](DYLIBS/Netrb.md)
- [/System/Library/PrivateFrameworks/NetworkQualityServices.framework/NetworkQualityServices](DYLIBS/NetworkQualityServices.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay](DYLIBS/NetworkRelay.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics](DYLIBS/NetworkStatistics.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit](DYLIBS/NeutrinoKit.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/NewsAnalyticsUpload](DYLIBS/NewsAnalyticsUpload.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/Library/PrivateFrameworks/NewsEngagementCollector.framework/NewsEngagementCollector](DYLIBS/NewsEngagementCollector.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation](DYLIBS/NewsFoundation.md)
- [/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit](DYLIBS/NewsKit.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/NewsServices](DYLIBS/NewsServices.md)
- [/System/Library/PrivateFrameworks/NewsServicesInternal.framework/NewsServicesInternal](DYLIBS/NewsServicesInternal.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport](DYLIBS/NewsTransport.md)
- [/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI](DYLIBS/NewsUI.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NewsURLBucket.framework/NewsURLBucket](DYLIBS/NewsURLBucket.md)
- [/System/Library/PrivateFrameworks/NewsURLResolution.framework/NewsURLResolution](DYLIBS/NewsURLResolution.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NonverbalCues.framework/NonverbalCues](DYLIBS/NonverbalCues.md)
- [/System/Library/PrivateFrameworks/NotTheStoreKitUIFrameworkYouAreLookingFor.framework/NotTheStoreKitUIFrameworkYouAreLookingFor](DYLIBS/NotTheStoreKitUIFrameworkYouAreLookingFor.md)
- [/System/Library/PrivateFrameworks/Notes.framework/Notes](DYLIBS/Notes.md)
- [/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics](DYLIBS/NotesAnalytics.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesPreviewKit.framework/NotesPreviewKit](DYLIBS/NotesPreviewKit.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices](DYLIBS/NotesUIServices.md)
- [/System/Library/PrivateFrameworks/OAuth.framework/OAuth](DYLIBS/OAuth.md)
- [/System/Library/PrivateFrameworks/ODCurareAnalysis.framework/ODCurareAnalysis](DYLIBS/ODCurareAnalysis.md)
- [/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting](DYLIBS/ODCurareEvaluationAndReporting.md)
- [/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient](DYLIBS/OSAServicesClient.md)
- [/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient](DYLIBS/OSASubmissionClient.md)
- [/System/Library/PrivateFrameworks/OSASyncProxyClient.framework/OSASyncProxyClient](DYLIBS/OSASyncProxyClient.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate](DYLIBS/OSAnalyticsPrivate.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/OTSVG.framework/OTSVG](DYLIBS/OTSVG.md)
- [/System/Library/PrivateFrameworks/ObjectUnderstanding.framework/ObjectUnderstanding](DYLIBS/ObjectUnderstanding.md)
- [/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust](DYLIBS/OctagonTrust.md)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport](DYLIBS/OfficeImport.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/OpticalFlowFramework.framework/OpticalFlowFramework](DYLIBS/OpticalFlowFramework.md)
- [/System/Library/PrivateFrameworks/Osprey.framework/Osprey](DYLIBS/Osprey.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport](DYLIBS/PBBridgeSupport.md)
- [/System/Library/PrivateFrameworks/PDS.framework/PDS](DYLIBS/PDS.md)
- [/System/Library/PrivateFrameworks/PDSAgent.framework/PDSAgent](DYLIBS/PDSAgent.md)
- [/System/Library/PrivateFrameworks/PLSnapshot.framework/PLSnapshot](DYLIBS/PLSnapshot.md)
- [/System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter](DYLIBS/PacketFilter.md)
- [/System/Library/PrivateFrameworks/PairedSync.framework/PairedSync](DYLIBS/PairedSync.md)
- [/System/Library/PrivateFrameworks/PairedUnlock.framework/PairedUnlock](DYLIBS/PairedUnlock.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity](DYLIBS/PairingProximity.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE](DYLIBS/ParavirtualizedANE.md)
- [/System/Library/PrivateFrameworks/ParsecModel.framework/ParsecModel](DYLIBS/ParsecModel.md)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitServices.framework/PassKitServices](DYLIBS/PassKitServices.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation](DYLIBS/PassKitUIFoundation.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard](DYLIBS/Pasteboard.md)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase](DYLIBS/PaymentUIBase.md)
- [/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI](DYLIBS/PencilPairingUI.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI](DYLIBS/PeopleUI.md)
- [/System/Library/PrivateFrameworks/PeopleUIInternal.framework/PeopleUIInternal](DYLIBS/PeopleUIInternal.md)
- [/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor](DYLIBS/PerfPowerMetricMonitor.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader](DYLIBS/PerfPowerServicesReader.md)
- [/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit](DYLIBS/PerformanceControlKit.md)
- [/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace](DYLIBS/PerformanceTrace.md)
- [/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth](DYLIBS/PeridotDepth.md)
- [/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection](DYLIBS/PersistentConnection.md)
- [/System/Library/PrivateFrameworks/PersonaKit.framework/PersonaKit](DYLIBS/PersonaKit.md)
- [/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI](DYLIBS/PersonaUI.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalIntelligenceCore.framework/PersonalIntelligenceCore](DYLIBS/PersonalIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait](DYLIBS/PersonalizationPortrait.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/Phoenix.framework/Phoenix](DYLIBS/Phoenix.md)
- [/System/Library/PrivateFrameworks/PhoneNumberResolver.framework/PhoneNumberResolver](DYLIBS/PhoneNumberResolver.md)
- [/System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers](DYLIBS/PhoneNumbers.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoBoothEffects.framework/PhotoBoothEffects](DYLIBS/PhotoBoothEffects.md)
- [/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation](DYLIBS/PhotoFoundation.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibrary.framework/PhotoLibrary](DYLIBS/PhotoLibrary.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation](DYLIBS/PhotosImagingFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosKnowledgeGraph.framework/PhotosKnowledgeGraph](DYLIBS/PhotosKnowledgeGraph.md)
- [/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer](DYLIBS/PhotosPlayer.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/PhotosensitivityProcessing](DYLIBS/PhotosensitivityProcessing.md)
- [/System/Library/PrivateFrameworks/PhysicsKit.framework/PhysicsKit](DYLIBS/PhysicsKit.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit](DYLIBS/PlatterKit.md)
- [/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit](DYLIBS/PlugInKit.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/PointerUIServices](DYLIBS/PointerUIServices.md)
- [/System/Library/PrivateFrameworks/PointerUISystemServices.framework/PointerUISystemServices](DYLIBS/PointerUISystemServices.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSQLite.framework/PoirotSQLite](DYLIBS/PoirotSQLite.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterBoardUI.framework/PosterBoardUI](DYLIBS/PosterBoardUI.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting](DYLIBS/PowerlogAccounting.md)
- [/System/Library/PrivateFrameworks/PowerlogControl.framework/PowerlogControl](DYLIBS/PowerlogControl.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogDatabaseReader.framework/PowerlogDatabaseReader](DYLIBS/PowerlogDatabaseReader.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices](DYLIBS/PreviewsServices.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit.md)
- [/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI](DYLIBS/PrintKitUI.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting](DYLIBS/PrivacyAccounting.md)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore](DYLIBS/PrivacyDisclosureCore.md)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureUI.framework/PrivacyDisclosureUI](DYLIBS/PrivacyDisclosureUI.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateSearchClient.framework/PrivateSearchClient](DYLIBS/PrivateSearchClient.md)
- [/System/Library/PrivateFrameworks/PrivateSearchCore.framework/PrivateSearchCore](DYLIBS/PrivateSearchCore.md)
- [/System/Library/PrivateFrameworks/PrivateSearchProtocols.framework/PrivateSearchProtocols](DYLIBS/PrivateSearchProtocols.md)
- [/System/Library/PrivateFrameworks/ProVideo.framework/ProVideo](DYLIBS/ProVideo.md)
- [/System/Library/PrivateFrameworks/ProactiveBlendingLayer_iOS.framework/ProactiveBlendingLayer_iOS](DYLIBS/ProactiveBlendingLayer_iOS.md)
- [/System/Library/PrivateFrameworks/ProactiveCDNDownloader.framework/ProactiveCDNDownloader](DYLIBS/ProactiveCDNDownloader.md)
- [/System/Library/PrivateFrameworks/ProactiveContextClient.framework/ProactiveContextClient](DYLIBS/ProactiveContextClient.md)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker.md)
- [/System/Library/PrivateFrameworks/ProactiveExperiments.framework/ProactiveExperiments](DYLIBS/ProactiveExperiments.md)
- [/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals](DYLIBS/ProactiveExperimentsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/ProactiveInputPredictions](DYLIBS/ProactiveInputPredictions.md)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictionsInternals.framework/ProactiveInputPredictionsInternals](DYLIBS/ProactiveInputPredictionsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveML.framework/ProactiveML](DYLIBS/ProactiveML.md)
- [/System/Library/PrivateFrameworks/ProactiveMagicalMoments.framework/ProactiveMagicalMoments](DYLIBS/ProactiveMagicalMoments.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse](DYLIBS/ProactiveShareSheetDataHarvestingLighthouse.md)
- [/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel](DYLIBS/ProactiveSuggestionClientModel.md)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveSupportStubs.framework/ProactiveSupportStubs](DYLIBS/ProactiveSupportStubs.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity](DYLIBS/ProfileValidatedAppIdentity.md)
- [/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI](DYLIBS/ProgressUI.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction](DYLIBS/PromotedContentPrediction.md)
- [/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PromotedContentProxy](DYLIBS/PromotedContentProxy.md)
- [/System/Library/PrivateFrameworks/PromotedContentSupport.framework/PromotedContentSupport](DYLIBS/PromotedContentSupport.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProofReader.framework/ProofReader](DYLIBS/ProofReader.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer](DYLIBS/ProtocolBuffer.md)
- [/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools](DYLIBS/PrototypeTools.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI](DYLIBS/PrototypeToolsUI.md)
- [/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit](DYLIBS/ProxCardKit.md)
- [/System/Library/PrivateFrameworks/Proximity.framework/Proximity](DYLIBS/Proximity.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl.md)
- [/System/Library/PrivateFrameworks/ProximityUI.framework/ProximityUI](DYLIBS/ProximityUI.md)
- [/System/Library/PrivateFrameworks/QLCharts.framework/QLCharts](DYLIBS/QLCharts.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/Quagga.framework/Quagga](DYLIBS/Quagga.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport](DYLIBS/QuickLookSupport.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailGeneration.framework/QuickLookThumbnailGeneration](DYLIBS/QuickLookThumbnailGeneration.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore](DYLIBS/QuickLookUICore.md)
- [/System/Library/PrivateFrameworks/RESync.framework/RESync](DYLIBS/RESync.md)
- [/System/Library/PrivateFrameworks/RTBuddyCrashlogDecoder.framework/RTBuddyCrashlogDecoder](DYLIBS/RTBuddyCrashlogDecoder.md)
- [/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting](DYLIBS/RTCReporting.md)
- [/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI](DYLIBS/RTTUI.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/Radio.framework/Radio](DYLIBS/Radio.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RapportUI.framework/RapportUI](DYLIBS/RapportUI.md)
- [/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion](DYLIBS/RealityFusion.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/Recap.framework/Recap](DYLIBS/Recap.md)
- [/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting](DYLIBS/RecapPerformanceTesting.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal](DYLIBS/ReflectionInternal.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/RelativeMotion.framework/RelativeMotion](DYLIBS/RelativeMotion.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/RelevanceEngineUI.framework/RelevanceEngineUI](DYLIBS/RelevanceEngineUI.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/ReminderKitUI](DYLIBS/ReminderKitUI.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration](DYLIBS/RemoteConfiguration.md)
- [/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML](DYLIBS/RemoteCoreML.md)
- [/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID](DYLIBS/RemoteHID.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel](DYLIBS/RemoteManagementModel.md)
- [/System/Library/PrivateFrameworks/RemoteManagementProtocol.framework/RemoteManagementProtocol](DYLIBS/RemoteManagementProtocol.md)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore](DYLIBS/RemoteManagementStore.md)
- [/System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI](DYLIBS/RemoteManagementUI.md)
- [/System/Library/PrivateFrameworks/RemoteMediaServices.framework/RemoteMediaServices](DYLIBS/RemoteMediaServices.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery](DYLIBS/RemoteServiceDiscovery.md)
- [/System/Library/PrivateFrameworks/RemoteStateDumpKit.framework/RemoteStateDumpKit](DYLIBS/RemoteStateDumpKit.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth](DYLIBS/RespiratoryHealth.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon](DYLIBS/RespiratoryHealthDaemon.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealthUI.framework/RespiratoryHealthUI](DYLIBS/RespiratoryHealthUI.md)
- [/System/Library/PrivateFrameworks/ResponseKit.framework/ResponseKit](DYLIBS/ResponseKit.md)
- [/System/Library/PrivateFrameworks/RevealCore.framework/RevealCore](DYLIBS/RevealCore.md)
- [/System/Library/PrivateFrameworks/RoomScanCore.framework/RoomScanCore](DYLIBS/RoomScanCore.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SAML.framework/SAML](DYLIBS/SAML.md)
- [/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects](DYLIBS/SAObjects.md)
- [/System/Library/PrivateFrameworks/SDAPI.framework/SDAPI](DYLIBS/SDAPI.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SILManager.framework/SILManager](DYLIBS/SILManager.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SIMToolkitUI.framework/SIMToolkitUI](DYLIBS/SIMToolkitUI.md)
- [/System/Library/PrivateFrameworks/SMBClientEngine.framework/SMBClientEngine](DYLIBS/SMBClientEngine.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/SMBClientProvider](DYLIBS/SMBClientProvider.md)
- [/System/Library/PrivateFrameworks/SMBSearch.framework/SMBSearch](DYLIBS/SMBSearch.md)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS.md)
- [/System/Library/PrivateFrameworks/SOSUI.framework/SOSUI](DYLIBS/SOSUI.md)
- [/System/Library/PrivateFrameworks/SPFinder.framework/SPFinder](DYLIBS/SPFinder.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient](DYLIBS/STSXPCHelperClient.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing](DYLIBS/SafariSafeBrowsing.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts](DYLIBS/SafetyAlerts.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface](DYLIBS/SavageCameraInterface.md)
- [/System/Library/PrivateFrameworks/Scandium.framework/Scandium](DYLIBS/Scandium.md)
- [/System/Library/PrivateFrameworks/SceneIntelligence.framework/SceneIntelligence](DYLIBS/SceneIntelligence.md)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/SchoolTime](DYLIBS/SchoolTime.md)
- [/System/Library/PrivateFrameworks/SchoolTimeSettingsUI.framework/SchoolTimeSettingsUI](DYLIBS/SchoolTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenReaderBrailleDriver.framework/ScreenReaderBrailleDriver](DYLIBS/ScreenReaderBrailleDriver.md)
- [/System/Library/PrivateFrameworks/ScreenReaderCore.framework/ScreenReaderCore](DYLIBS/ScreenReaderCore.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices](DYLIBS/ScreenshotServices.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchToShareCore.framework/SearchToShareCore](DYLIBS/SearchToShareCore.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SearchUICardKitProviderSupport.framework/SearchUICardKitProviderSupport](DYLIBS/SearchUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/SecureChannel.framework/SecureChannel](DYLIBS/SecureChannel.md)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService](DYLIBS/SecureTransactionService.md)
- [/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets.framework/SecureVoiceTriggerAssets](DYLIBS/SecureVoiceTriggerAssets.md)
- [/System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation](DYLIBS/SecurityFoundation.md)
- [/System/Library/PrivateFrameworks/Seeding.framework/Seeding](DYLIBS/Seeding.md)
- [/System/Library/PrivateFrameworks/SemanticPerception.framework/SemanticPerception](DYLIBS/SemanticPerception.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper](DYLIBS/SensorKitHelper.md)
- [/System/Library/PrivateFrameworks/SensorKitSupport.framework/SensorKitSupport](DYLIBS/SensorKitSupport.md)
- [/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI](DYLIBS/SensorKitUI.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/ServiceExtensionsCore.framework/ServiceExtensionsCore](DYLIBS/ServiceExtensionsCore.md)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement.md)
- [/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert](DYLIBS/SessionAlert.md)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications.md)
- [/System/Library/PrivateFrameworks/SessionSQL.framework/SessionSQL](DYLIBS/SessionSQL.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular](DYLIBS/SettingsCellular.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport](DYLIBS/SetupAssistantSupport.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit](DYLIBS/SetupKit.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServerProtocol.framework/SeymourServerProtocol](DYLIBS/SeymourServerProtocol.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials](DYLIBS/SharedWebCredentials.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamInsights.framework/ShazamInsights](DYLIBS/ShazamInsights.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShortcutUIKit.framework/ShortcutUIKit](DYLIBS/ShortcutUIKit.md)
- [/System/Library/PrivateFrameworks/SidecarCore.framework/SidecarCore](DYLIBS/SidecarCore.md)
- [/System/Library/PrivateFrameworks/SidecarUI.framework/SidecarUI](DYLIBS/SidecarUI.md)
- [/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression](DYLIBS/SignalCompression.md)
- [/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection](DYLIBS/SignpostCollection.md)
- [/System/Library/PrivateFrameworks/SignpostMetrics.framework/SignpostMetrics](DYLIBS/SignpostMetrics.md)
- [/System/Library/PrivateFrameworks/SignpostNotification.framework/SignpostNotification](DYLIBS/SignpostNotification.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SilexVideo.framework/SilexVideo](DYLIBS/SilexVideo.md)
- [/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb](DYLIBS/SilexWeb.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution](DYLIBS/SiriAppResolution.md)
- [/System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils](DYLIBS/SiriAudioIntentUtils.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSnippetKit.framework/SiriAudioSnippetKit](DYLIBS/SiriAudioSnippetKit.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriCarCommandsIntents.framework/SiriCarCommandsIntents](DYLIBS/SiriCarCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore](DYLIBS/SiriCore.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics](DYLIBS/SiriCoreMetrics.md)
- [/System/Library/PrivateFrameworks/SiriCorrections.framework/SiriCorrections](DYLIBS/SiriCorrections.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback](DYLIBS/SiriCrossDeviceArbitrationFeedback.md)
- [/System/Library/PrivateFrameworks/SiriDailyBriefingInternal.framework/SiriDailyBriefingInternal](DYLIBS/SiriDailyBriefingInternal.md)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine](DYLIBS/SiriDialogEngine.md)
- [/System/Library/PrivateFrameworks/SiriEmergencyIntents.framework/SiriEmergencyIntents](DYLIBS/SiriEmergencyIntents.md)
- [/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher](DYLIBS/SiriEntityMatcher.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternalUI.framework/SiriExpanseInternalUI](DYLIBS/SiriExpanseInternalUI.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo](DYLIBS/SiriGeo.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInferenceIntents.framework/SiriInferenceIntents](DYLIBS/SiriInferenceIntents.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/SiriInferredHelpfulness](DYLIBS/SiriInferredHelpfulness.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes](DYLIBS/SiriInformationTypes.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriIntentEvents.framework/SiriIntentEvents](DYLIBS/SiriIntentEvents.md)
- [/System/Library/PrivateFrameworks/SiriInteractive.framework/SiriInteractive](DYLIBS/SiriInteractive.md)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/SiriInvocationAnalytics](DYLIBS/SiriInvocationAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitInvocation.framework/SiriKitInvocation](DYLIBS/SiriKitInvocation.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriLiminal.framework/SiriLiminal](DYLIBS/SiriLiminal.md)
- [/System/Library/PrivateFrameworks/SiriMASPFLTraining.framework/SiriMASPFLTraining](DYLIBS/SiriMASPFLTraining.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriModes.framework/SiriModes](DYLIBS/SiriModes.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriObservation.framework/SiriObservation](DYLIBS/SiriObservation.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPowerInstrumentation.framework/SiriPowerInstrumentation](DYLIBS/SiriPowerInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningLogging.framework/SiriPrivateLearningLogging](DYLIBS/SiriPrivateLearningLogging.md)
- [/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents](DYLIBS/SiriReaderIntents.md)
- [/System/Library/PrivateFrameworks/SiriReaderServices.framework/SiriReaderServices](DYLIBS/SiriReaderServices.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel](DYLIBS/SiriReferenceResolutionDataModel.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver](DYLIBS/SiriReferenceResolver.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSocialConversation.framework/SiriSocialConversation](DYLIBS/SiriSocialConversation.md)
- [/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis](DYLIBS/SiriSpeechSynthesis.md)
- [/System/Library/PrivateFrameworks/SiriStates.framework/SiriStates](DYLIBS/SiriStates.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriSystemCommandsIntents.framework/SiriSystemCommandsIntents](DYLIBS/SiriSystemCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTaskEngagement.framework/SiriTaskEngagement](DYLIBS/SiriTaskEngagement.md)
- [/System/Library/PrivateFrameworks/SiriTasks.framework/SiriTasks](DYLIBS/SiriTasks.md)
- [/System/Library/PrivateFrameworks/SiriTasksEvaluation.framework/SiriTasksEvaluation](DYLIBS/SiriTasksEvaluation.md)
- [/System/Library/PrivateFrameworks/SiriTimeAlarmInternal.framework/SiriTimeAlarmInternal](DYLIBS/SiriTimeAlarmInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/SiriTimeInternal](DYLIBS/SiriTimeInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge](DYLIBS/SiriUIBridge.md)
- [/System/Library/PrivateFrameworks/SiriUICardKitProviderSupport.framework/SiriUICardKitProviderSupport](DYLIBS/SiriUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX](DYLIBS/SiriVOX.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution.md)
- [/System/Library/PrivateFrameworks/SiriWellnessIntents.framework/SiriWellnessIntents](DYLIBS/SiriWellnessIntents.md)
- [/System/Library/PrivateFrameworks/Sleep.framework/Sleep](DYLIBS/Sleep.md)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon](DYLIBS/SleepDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth](DYLIBS/SleepHealth.md)
- [/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon](DYLIBS/SleepHealthDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusFoundation.framework/OpusFoundation](DYLIBS/OpusFoundation.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusKit.framework/OpusKit](DYLIBS/OpusKit.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/SlideshowKit](DYLIBS/SlideshowKit.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer](DYLIBS/SmartRepliesServer.md)
- [/System/Library/PrivateFrameworks/SmartRepliesUI.framework/SmartRepliesUI](DYLIBS/SmartRepliesUI.md)
- [/System/Library/PrivateFrameworks/SnippetCommands.framework/SnippetCommands](DYLIBS/SnippetCommands.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SnippetUI_Proto.framework/SnippetUI_Proto](DYLIBS/SnippetUI_Proto.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SocialServices.framework/SocialServices](DYLIBS/SocialServices.md)
- [/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking](DYLIBS/SoftLinking.md)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge](DYLIBS/SoftwareUpdateBridge.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect](DYLIBS/SoftwareUpdateCoreConnect.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport](DYLIBS/SoftwareUpdateCoreSupport.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI](DYLIBS/SoftwareUpdateServicesUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SoundAutoConfig.framework/SoundAutoConfig](DYLIBS/SoundAutoConfig.md)
- [/System/Library/PrivateFrameworks/SoundBoardServices.framework/SoundBoardServices](DYLIBS/SoundBoardServices.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/SoundScapesUtility](DYLIBS/SoundScapesUtility.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution](DYLIBS/SpaceAttribution.md)
- [/System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices](DYLIBS/SpeakThisServices.md)
- [/System/Library/PrivateFrameworks/SpeakTypingServices.framework/SpeakTypingServices](DYLIBS/SpeakTypingServices.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeechDetector.framework/SpeechDetector](DYLIBS/SpeechDetector.md)
- [/System/Library/PrivateFrameworks/SpeechDictionary.framework/SpeechDictionary](DYLIBS/SpeechDictionary.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices](DYLIBS/SpeechRecognitionCommandServices.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore](DYLIBS/SpeechRecognitionCore.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport](DYLIBS/SpeechRecognitionSharedSupport.md)
- [/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard](DYLIBS/SplashBoard.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation](DYLIBS/SpotlightFoundation.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation](DYLIBS/SpotlightRecommendation.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpotlightUI.framework/SpotlightUI](DYLIBS/SpotlightUI.md)
- [/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal](DYLIBS/SpotlightUIInternal.md)
- [/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared](DYLIBS/SpotlightUIShared.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardIntents.framework/SpringBoardIntents](DYLIBS/SpringBoardIntents.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit](DYLIBS/StatusKit.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/Stocks.framework/Stocks](DYLIBS/Stocks.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageData.framework/StorageData](DYLIBS/StorageData.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit.md)
- [/System/Library/PrivateFrameworks/StorageSettings.framework/StorageSettings](DYLIBS/StorageSettings.md)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI.md)
- [/System/Library/PrivateFrameworks/StoreBookkeeper.framework/StoreBookkeeper](DYLIBS/StoreBookkeeper.md)
- [/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/StoreBookkeeperClient](DYLIBS/StoreBookkeeperClient.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor](DYLIBS/StreamingExtractor.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip](DYLIBS/StreamingZip.md)
- [/System/Library/PrivateFrameworks/StrokeAnimation.framework/StrokeAnimation](DYLIBS/StrokeAnimation.md)
- [/System/Library/PrivateFrameworks/StudyLog.framework/StudyLog](DYLIBS/StudyLog.md)
- [/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics](DYLIBS/SuggestionsSpotlightMetrics.md)
- [/System/Library/PrivateFrameworks/SummariesHealthDaemon.framework/SummariesHealthDaemon](DYLIBS/SummariesHealthDaemon.md)
- [/System/Library/PrivateFrameworks/SwiftCertificate.framework/SwiftCertificate](DYLIBS/SwiftCertificate.md)
- [/System/Library/PrivateFrameworks/SwiftNN.framework/SwiftNN](DYLIBS/SwiftNN.md)
- [/System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite](DYLIBS/SwiftSQLite.md)
- [/System/Library/PrivateFrameworks/SwiftUIAccessibility.framework/SwiftUIAccessibility](DYLIBS/SwiftUIAccessibility.md)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication](DYLIBS/Symbolication.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter](DYLIBS/SymptomReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent](DYLIBS/ManagedEvent.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics](DYLIBS/SymptomAnalytics.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed](DYLIBS/SymptomPresentationFeed.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationLite.framework/SymptomPresentationLite](DYLIBS/SymptomPresentationLite.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Synapse](DYLIBS/Synapse.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults](DYLIBS/SyncedDefaults.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture](DYLIBS/SystemAperture.md)
- [/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/PrivateFrameworks/SystemPaperPresentation.framework/SystemPaperPresentation](DYLIBS/SystemPaperPresentation.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake](DYLIBS/SystemWake.md)
- [/System/Library/PrivateFrameworks/TCC.framework/TCC](DYLIBS/TCC.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TSReading.framework/TSReading](DYLIBS/TSReading.md)
- [/System/Library/PrivateFrameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVLatency.framework/TVLatency](DYLIBS/TVLatency.md)
- [/System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TVUIKit.framework/TVUIKit](DYLIBS/TVUIKit.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TailspinSymbolication.framework/TailspinSymbolication](DYLIBS/TailspinSymbolication.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TeaSnappy.framework/TeaSnappy](DYLIBS/TeaSnappy.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences](DYLIBS/TelephonyPreferences.md)
- [/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC](DYLIBS/TelephonyRPC.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TelephonyXPCClient.framework/TelephonyXPCClient](DYLIBS/TelephonyXPCClient.md)
- [/System/Library/PrivateFrameworks/TelephonyXPCServer.framework/TelephonyXPCServer](DYLIBS/TelephonyXPCServer.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TestFlightCore.framework/TestFlightCore](DYLIBS/TestFlightCore.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCJK.framework/TextInputCJK](DYLIBS/TextInputCJK.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/TextInputTestingKit](DYLIBS/TextInputTestingKit.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/deu.dylib](DYLIBS/deu.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eci.dylib](DYLIBS/eci.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eng.dylib](DYLIBS/eng.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/enu.dylib](DYLIBS/enu.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esm.dylib](DYLIBS/esm.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esp.dylib](DYLIBS/esp.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fin.dylib](DYLIBS/fin.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fra.dylib](DYLIBS/fra.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/frc.dylib](DYLIBS/frc.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ita.dylib](DYLIBS/ita.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ptb.dylib](DYLIBS/ptb.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/TextToSpeechKonaSupport](DYLIBS/TextToSpeechKonaSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/TextToSpeechMauiSupport](DYLIBS/TextToSpeechMauiSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/TextureIO.framework/TextureIO](DYLIBS/TextureIO.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](DYLIBS/Tightbeam.md)
- [/System/Library/PrivateFrameworks/TimeAppServices.framework/TimeAppServices](DYLIBS/TimeAppServices.md)
- [/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync](DYLIBS/TimeSync.md)
- [/System/Library/PrivateFrameworks/Timeline.framework/Timeline](DYLIBS/Timeline.md)
- [/System/Library/PrivateFrameworks/TinCanShared.framework/TinCanShared](DYLIBS/TinCanShared.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitLegacy.framework/TipKitLegacy](DYLIBS/TipKitLegacy.md)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices](DYLIBS/TipKitServices.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit](DYLIBS/ToneKit.md)
- [/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary](DYLIBS/ToneLibrary.md)
- [/System/Library/PrivateFrameworks/TouchML.framework/TouchML](DYLIBS/TouchML.md)
- [/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote](DYLIBS/TouchRemote.md)
- [/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance](DYLIBS/TrackingAvoidance.md)
- [/System/Library/PrivateFrameworks/TraitsArbiter.framework/TraitsArbiter](DYLIBS/TraitsArbiter.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices](DYLIBS/TranslationUIServices.md)
- [/System/Library/PrivateFrameworks/Transliteration.framework/Transliteration](DYLIBS/Transliteration.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/TransparencyDetailsView.framework/TransparencyDetailsView](DYLIBS/TransparencyDetailsView.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI](DYLIBS/TransparencyUI.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto](DYLIBS/TrialProto.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers](DYLIBS/TrustedPeers.md)
- [/System/Library/PrivateFrameworks/TuriCore.framework/TuriCore](DYLIBS/TuriCore.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/TypologyAccess.framework/TypologyAccess](DYLIBS/TypologyAccess.md)
- [/System/Library/PrivateFrameworks/UARPUpdaterService.framework/UARPUpdaterService](DYLIBS/UARPUpdaterService.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UITriggerVC.framework/UITriggerVC](DYLIBS/UITriggerVC.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/URLCompression.framework/URLCompression](DYLIBS/URLCompression.md)
- [/System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting](DYLIBS/URLFormatting.md)
- [/System/Library/PrivateFrameworks/USDKit.framework/USDKit](DYLIBS/USDKit.md)
- [/System/Library/PrivateFrameworks/USDLib_FormatLoaderProxy.framework/USDLib_FormatLoaderProxy](DYLIBS/USDLib_FormatLoaderProxy.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UnityPoster.framework/UnityPoster](DYLIBS/UnityPoster.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity](DYLIBS/UserActivity.md)
- [/System/Library/PrivateFrameworks/UserAlerts.framework/UserAlerts](DYLIBS/UserAlerts.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/liblivefiles.plugin.dummy.dylib](DYLIBS/liblivefiles.plugin.dummy.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_cs.dylib](DYLIBS/livefiles_cs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib](DYLIBS/livefiles_exfat.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib](DYLIBS/livefiles_hfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib](DYLIBS/livefiles_msdos.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_ntfs.dylib](DYLIBS/livefiles_ntfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/UserFS](DYLIBS/UserFS.md)
- [/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement](DYLIBS/UserManagement.md)
- [/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout](DYLIBS/UserManagementLayout.md)
- [/System/Library/PrivateFrameworks/UserManagementUI.framework/UserManagementUI](DYLIBS/UserManagementUI.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings](DYLIBS/UserNotificationsSettings.md)
- [/System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation](DYLIBS/UserNotificationsTranslation.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/UserSafety.framework/UserSafety](DYLIBS/UserSafety.md)
- [/System/Library/PrivateFrameworks/UserSafetyUI.framework/UserSafetyUI](DYLIBS/UserSafetyUI.md)
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI.md)
- [/System/Library/PrivateFrameworks/VideoToolboxParavirtualizationSupport.framework/VideoToolboxParavirtualizationSupport](DYLIBS/VideoToolboxParavirtualizationSupport.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage](DYLIBS/VirtualGarage.md)
- [/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore](DYLIBS/VisionCore.md)
- [/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices](DYLIBS/VisionHWAccelerationServices.md)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualAlert.framework/VisualAlert](DYLIBS/VisualAlert.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization](DYLIBS/VisualLocalization.md)
- [/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger](DYLIBS/VisualLogger.md)
- [/System/Library/PrivateFrameworks/VisualPairing.framework/VisualPairing](DYLIBS/VisualPairing.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail](DYLIBS/VisualVoicemail.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/libvoiced_tts.dylib](DYLIBS/libvoiced_tts.dylib.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices](DYLIBS/VoiceServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutsUICardKitProviderSupport.framework/VoiceShortcutsUICardKitProviderSupport](DYLIBS/VoiceShortcutsUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/VoicemailStore.framework/VoicemailStore](DYLIBS/VoicemailStore.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchControlAssets.framework/WatchControlAssets](DYLIBS/WatchControlAssets.md)
- [/System/Library/PrivateFrameworks/WatchControlSettings.framework/WatchControlSettings](DYLIBS/WatchControlSettings.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WatchQuickActionsServices.framework/WatchQuickActionsServices](DYLIBS/WatchQuickActionsServices.md)
- [/System/Library/PrivateFrameworks/WatchReplies.framework/WatchReplies](DYLIBS/WatchReplies.md)
- [/System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient](DYLIBS/WatchdogClient.md)
- [/System/Library/PrivateFrameworks/Weather.framework/Weather](DYLIBS/Weather.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherFoundation.framework/WeatherFoundation](DYLIBS/WeatherFoundation.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebApp.framework/WebApp](DYLIBS/WebApp.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebContentAnalysis.framework/WebContentAnalysis](DYLIBS/WebContentAnalysis.md)
- [/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions](DYLIBS/WebContentRestrictions.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector](DYLIBS/WebInspector.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/WebPrivacy](DYLIBS/WebPrivacy.md)
- [/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet](DYLIBS/WebSheet.md)
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI.md)
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/WelcomeKit](DYLIBS/WelcomeKit.md)
- [/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore](DYLIBS/WelcomeKitCore.md)
- [/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI](DYLIBS/WelcomeKitUI.md)
- [/System/Library/PrivateFrameworks/WellnessUI.framework/WellnessUI](DYLIBS/WellnessUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiCloudSyncEngine.framework/WiFiCloudSyncEngine](DYLIBS/WiFiCloudSyncEngine.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiLogCapture.framework/WiFiLogCapture](DYLIBS/WiFiLogCapture.md)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity](DYLIBS/WiFiVelocity.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/Widgets.framework/Widgets](DYLIBS/Widgets.md)
- [/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager](DYLIBS/WirelessCoexManager.md)
- [/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics](DYLIBS/WirelessDiagnostics.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/WirelessInsights](DYLIBS/WirelessInsights.md)
- [/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity](DYLIBS/WirelessProximity.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness](DYLIBS/WorkflowResponsiveness.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutHealthBridge.framework/WorkoutHealthBridge](DYLIBS/WorkoutHealthBridge.md)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/WorkoutKitServices](DYLIBS/WorkoutKitServices.md)
- [/System/Library/PrivateFrameworks/WorkoutKitUI.framework/WorkoutKitUI](DYLIBS/WorkoutKitUI.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap](DYLIBS/XCTTargetBootstrap.md)
- [/System/Library/PrivateFrameworks/XGBoostFramework.framework/XGBoostFramework](DYLIBS/XGBoostFramework.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/XOJITExecutor.framework/XOJITExecutor](DYLIBS/XOJITExecutor.md)
- [/System/Library/PrivateFrameworks/XavierCore.framework/XavierCore](DYLIBS/XavierCore.md)
- [/System/Library/PrivateFrameworks/XavierNews.framework/XavierNews](DYLIBS/XavierNews.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib.md)
- [/System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices](DYLIBS/ZoomServices.md)
- [/System/Library/PrivateFrameworks/_Coherence_CloudKit_Private.framework/_Coherence_CloudKit_Private](DYLIBS/_Coherence_CloudKit_Private.md)
- [/System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI](DYLIBS/_IconServices_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore](DYLIBS/_MusicKitInternal_MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlayer.framework/_MusicKitInternal_MediaPlayer](DYLIBS/_MusicKitInternal_MediaPlayer.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/apfs_boot_mount.framework/apfs_boot_mount](DYLIBS/apfs_boot_mount.md)
- [/System/Library/PrivateFrameworks/caulk.framework/caulk](DYLIBS/caulk.md)
- [/System/Library/PrivateFrameworks/iCalendar.framework/iCalendar](DYLIBS/iCalendar.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/iCloudDriveService](DYLIBS/iCloudDriveService.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification](DYLIBS/iCloudNotification.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerClient.framework/iCloudSubscriptionOptimizerClient](DYLIBS/iCloudSubscriptionOptimizerClient.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerCore.framework/iCloudSubscriptionOptimizerCore](DYLIBS/iCloudSubscriptionOptimizerCore.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/iCloudSubscriptionOptimizerDaemon](DYLIBS/iCloudSubscriptionOptimizerDaemon.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/iCloudSubscriptionOptimizerLighthouse](DYLIBS/iCloudSubscriptionOptimizerLighthouse.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerPFLTraining.framework/iCloudSubscriptionOptimizerPFLTraining](DYLIBS/iCloudSubscriptionOptimizerPFLTraining.md)
- [/System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps](DYLIBS/iMessageApps.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics](DYLIBS/iOSDiagnostics.md)
- [/System/Library/PrivateFrameworks/iOSScreenSharing.framework/iOSScreenSharing](DYLIBS/iOSScreenSharing.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/iTunesStore](DYLIBS/iTunesStore.md)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/iTunesStoreUI](DYLIBS/iTunesStoreUI.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/EquationKit.framework/EquationKit](DYLIBS/EquationKit.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/KeynoteQuicklook.framework/KeynoteQuicklook](DYLIBS/KeynoteQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/NumbersQuicklook.framework/NumbersQuicklook](DYLIBS/NumbersQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/PagesQuicklook.framework/PagesQuicklook](DYLIBS/PagesQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TQQuicklook.framework/TQQuicklook](DYLIBS/TQQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSApplication.framework/TSApplication](DYLIBS/TSApplication.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCalculationEngine.framework/TSCalculationEngine](DYLIBS/TSCalculationEngine.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCharts.framework/TSCharts](DYLIBS/TSCharts.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSDrawables.framework/TSDrawables](DYLIBS/TSDrawables.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSKit.framework/TSKit](DYLIBS/TSKit.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSPersistence.framework/TSPersistence](DYLIBS/TSPersistence.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSStyles.framework/TSStyles](DYLIBS/TSStyles.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSTables.framework/TSTables](DYLIBS/TSTables.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText](DYLIBS/TSText.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/PrivateFrameworks/kperf.framework/kperf](DYLIBS/kperf.md)
- [/System/Library/PrivateFrameworks/kperfdata.framework/kperfdata](DYLIBS/kperfdata.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/libEDR.framework/libEDR](DYLIBS/libEDR.md)
- [/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector](DYLIBS/libmalloc_exclaves_introspector.md)
- [/System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime](DYLIBS/lighthouse_runtime.md)
- [/System/Library/PrivateFrameworks/oncrpc.framework/oncrpc](DYLIBS/oncrpc.md)
- [/System/Library/PrivateFrameworks/perfdata.framework/perfdata](DYLIBS/perfdata.md)
- [/System/Library/PrivateFrameworks/vCard.framework/vCard](DYLIBS/vCard.md)
- [/System/Library/ProceduralWallpaper/ProceduralWallpapers.bundle/ProceduralWallpapers](DYLIBS/ProceduralWallpapers.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMapsNavigationCompanionDataSource.bundle/NanoMapsNavigationCompanionDataSource](DYLIBS/NanoMapsNavigationCompanionDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMapsSampleDataSource.bundle/NanoMapsSampleDataSource](DYLIBS/NanoMapsSampleDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineHome.bundle/RelevanceEngineHome](DYLIBS/RelevanceEngineHome.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSolar.bundle/RelevanceEngineSolar](DYLIBS/RelevanceEngineSolar.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineWeather.bundle/RelevanceEngineWeather](DYLIBS/RelevanceEngineWeather.md)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport](DYLIBS/CaptiveNetworkSupport.md)
- [/System/Library/TextInput/TextInput_bo.bundle/TextInput_bo](DYLIBS/TextInput_bo.md)
- [/System/Library/TextInput/TextInput_ca.bundle/TextInput_ca](DYLIBS/TextInput_ca.md)
- [/System/Library/TextInput/TextInput_chr.bundle/TextInput_chr](DYLIBS/TextInput_chr.md)
- [/System/Library/TextInput/TextInput_cs.bundle/TextInput_cs](DYLIBS/TextInput_cs.md)
- [/System/Library/TextInput/TextInput_de.bundle/TextInput_de](DYLIBS/TextInput_de.md)
- [/System/Library/TextInput/TextInput_el.bundle/TextInput_el](DYLIBS/TextInput_el.md)
- [/System/Library/TextInput/TextInput_emoji.bundle/TextInput_emoji](DYLIBS/TextInput_emoji.md)
- [/System/Library/TextInput/TextInput_en.bundle/TextInput_en](DYLIBS/TextInput_en.md)
- [/System/Library/TextInput/TextInput_es.bundle/TextInput_es](DYLIBS/TextInput_es.md)
- [/System/Library/TextInput/TextInput_fr.bundle/TextInput_fr](DYLIBS/TextInput_fr.md)
- [/System/Library/TextInput/TextInput_haw.bundle/TextInput_haw](DYLIBS/TextInput_haw.md)
- [/System/Library/TextInput/TextInput_he.bundle/TextInput_he](DYLIBS/TextInput_he.md)
- [/System/Library/TextInput/TextInput_hi.bundle/TextInput_hi](DYLIBS/TextInput_hi.md)
- [/System/Library/TextInput/TextInput_intl.bundle/TextInput_intl](DYLIBS/TextInput_intl.md)
- [/System/Library/TextInput/TextInput_ja.bundle/TextInput_ja](DYLIBS/TextInput_ja.md)
- [/System/Library/TextInput/TextInput_ko.bundle/TextInput_ko](DYLIBS/TextInput_ko.md)
- [/System/Library/TextInput/TextInput_mr.bundle/TextInput_mr](DYLIBS/TextInput_mr.md)
- [/System/Library/TextInput/TextInput_mul.bundle/TextInput_mul](DYLIBS/TextInput_mul.md)
- [/System/Library/TextInput/TextInput_my.bundle/TextInput_my](DYLIBS/TextInput_my.md)
- [/System/Library/TextInput/TextInput_nl.bundle/TextInput_nl](DYLIBS/TextInput_nl.md)
- [/System/Library/TextInput/TextInput_pa.bundle/TextInput_pa](DYLIBS/TextInput_pa.md)
- [/System/Library/TextInput/TextInput_pt.bundle/TextInput_pt](DYLIBS/TextInput_pt.md)
- [/System/Library/TextInput/TextInput_si.bundle/TextInput_si](DYLIBS/TextInput_si.md)
- [/System/Library/TextInput/TextInput_sk.bundle/TextInput_sk](DYLIBS/TextInput_sk.md)
- [/System/Library/TextInput/TextInput_ta.bundle/TextInput_ta](DYLIBS/TextInput_ta.md)
- [/System/Library/TextInput/TextInput_th.bundle/TextInput_th](DYLIBS/TextInput_th.md)
- [/System/Library/TextInput/TextInput_tr.bundle/TextInput_tr](DYLIBS/TextInput_tr.md)
- [/System/Library/TextInput/TextInput_ug.bundle/TextInput_ug](DYLIBS/TextInput_ug.md)
- [/System/Library/TextInput/TextInput_vi.bundle/TextInput_vi](DYLIBS/TextInput_vi.md)
- [/System/Library/TextInput/TextInput_yue.bundle/TextInput_yue](DYLIBS/TextInput_yue.md)
- [/System/Library/TextInput/TextInput_zh.bundle/TextInput_zh](DYLIBS/TextInput_zh.md)
- [/System/Library/UserEventPlugins/AppleHDQGasGauge.plugin/AppleHDQGasGauge](DYLIBS/AppleHDQGasGauge.md)
- [/System/Library/VideoCodecs/H264SW.videocodec](DYLIBS/H264SW.videocodec.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AV1SW.videodecoder](DYLIBS/AV1SW.videodecoder.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder](DYLIBS/AppleProResHWDecoder.videodecoder.md)
- [/System/Library/VideoDecoders/AppleProResSWDecoder.videodecoder](DYLIBS/AppleProResSWDecoder.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoDecoders/JPEGH1.videodecoder](DYLIBS/JPEGH1.videodecoder.md)
- [/System/Library/VideoDecoders/MP4VH8.videodecoder](DYLIBS/MP4VH8.videodecoder.md)
- [/System/Library/VideoDecoders/VCH263.videodecoder](DYLIBS/VCH263.videodecoder.md)
- [/System/Library/VideoDecoders/VCPMP4V.videodecoder](DYLIBS/VCPMP4V.videodecoder.md)
- [/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder](DYLIBS/AppleProResHWEncoder.videoencoder.md)
- [/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder](DYLIBS/AppleProResSWEncoder.videoencoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoEncoders/JPEGH1.videoencoder](DYLIBS/JPEGH1.videoencoder.md)
- [/System/Library/VideoEncoders/VCH263.videoencoder](DYLIBS/VCH263.videoencoder.md)
- [/System/Library/VideoProcessors/BarcodeScanner.videoprocessor](DYLIBS/BarcodeScanner.videoprocessor.md)
- [/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait](DYLIBS/CCPortrait.md)
- [/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1](DYLIBS/CalibrationV1.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/DepthProcessorV2](DYLIBS/DepthProcessorV2.md)
- [/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5](DYLIBS/DisparityV5.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1](DYLIBS/IntelligentDistortionCorrectionV1.md)
- [/System/Library/VideoProcessors/MattingV2.bundle/MattingV2](DYLIBS/MattingV2.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter](DYLIBS/MetalFilter.md)
- [/System/Library/VideoProcessors/NRFV2.bundle/NRFV2](DYLIBS/NRFV2.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5](DYLIBS/SDOFRenderingV5.md)
- [/System/Library/VideoProcessors/STF.bundle/STF](DYLIBS/STF.md)
- [/System/Library/VoiceServices/PlugIns/VoiceDial.vsplugin/VoiceDial](DYLIBS/VoiceDial.md)
- [/usr/lib/ACIPCBTLib.dylib](DYLIBS/ACIPCBTLib.dylib.md)
- [/usr/lib/AppleConvergedTransport.dylib](DYLIBS/AppleConvergedTransport.dylib.md)
- [/usr/lib/CarrierBundleUtilities.dylib](DYLIBS/CarrierBundleUtilities.dylib.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/i18n/libBIG5.dylib](DYLIBS/libBIG5.dylib.md)
- [/usr/lib/i18n/libDECHanyu.dylib](DYLIBS/libDECHanyu.dylib.md)
- [/usr/lib/i18n/libDECKanji.dylib](DYLIBS/libDECKanji.dylib.md)
- [/usr/lib/i18n/libEUC.dylib](DYLIBS/libEUC.dylib.md)
- [/usr/lib/i18n/libEUCTW.dylib](DYLIBS/libEUCTW.dylib.md)
- [/usr/lib/i18n/libGBK2K.dylib](DYLIBS/libGBK2K.dylib.md)
- [/usr/lib/i18n/libHZ.dylib](DYLIBS/libHZ.dylib.md)
- [/usr/lib/i18n/libISO2022.dylib](DYLIBS/libISO2022.dylib.md)
- [/usr/lib/i18n/libJOHAB.dylib](DYLIBS/libJOHAB.dylib.md)
- [/usr/lib/i18n/libMSKanji.dylib](DYLIBS/libMSKanji.dylib.md)
- [/usr/lib/i18n/libUES.dylib](DYLIBS/libUES.dylib.md)
- [/usr/lib/i18n/libUTF1632.dylib](DYLIBS/libUTF1632.dylib.md)
- [/usr/lib/i18n/libUTF7.dylib](DYLIBS/libUTF7.dylib.md)
- [/usr/lib/i18n/libUTF8.dylib](DYLIBS/libUTF8.dylib.md)
- [/usr/lib/i18n/libUTF8MAC.dylib](DYLIBS/libUTF8MAC.dylib.md)
- [/usr/lib/i18n/libVIQR.dylib](DYLIBS/libVIQR.dylib.md)
- [/usr/lib/i18n/libZW.dylib](DYLIBS/libZW.dylib.md)
- [/usr/lib/i18n/libiconv_none.dylib](DYLIBS/libiconv_none.dylib.md)
- [/usr/lib/i18n/libiconv_std.dylib](DYLIBS/libiconv_std.dylib.md)
- [/usr/lib/i18n/libmapper_646.dylib](DYLIBS/libmapper_646.dylib.md)
- [/usr/lib/i18n/libmapper_none.dylib](DYLIBS/libmapper_none.dylib.md)
- [/usr/lib/i18n/libmapper_parallel.dylib](DYLIBS/libmapper_parallel.dylib.md)
- [/usr/lib/i18n/libmapper_serial.dylib](DYLIBS/libmapper_serial.dylib.md)
- [/usr/lib/i18n/libmapper_std.dylib](DYLIBS/libmapper_std.dylib.md)
- [/usr/lib/i18n/libmapper_zone.dylib](DYLIBS/libmapper_zone.dylib.md)
- [/usr/lib/libAHTRestore.dylib](DYLIBS/libAHTRestore.dylib.md)
- [/usr/lib/libARI.dylib](DYLIBS/libARI.dylib.md)
- [/usr/lib/libARIServer.dylib](DYLIBS/libARIServer.dylib.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAWDProtobufBluetooth.dylib](DYLIBS/libAWDProtobufBluetooth.dylib.md)
- [/usr/lib/libAWDProtobufFacetime.dylib](DYLIBS/libAWDProtobufFacetime.dylib.md)
- [/usr/lib/libAWDProtobufGCK.dylib](DYLIBS/libAWDProtobufGCK.dylib.md)
- [/usr/lib/libAWDProtobufLocation.dylib](DYLIBS/libAWDProtobufLocation.dylib.md)
- [/usr/lib/libAWDSupport.dylib](DYLIBS/libAWDSupport.dylib.md)
- [/usr/lib/libAWDSupportFramework.dylib](DYLIBS/libAWDSupportFramework.dylib.md)
- [/usr/lib/libAXSafeCategoryBundle.dylib](DYLIBS/libAXSafeCategoryBundle.dylib.md)
- [/usr/lib/libAXSpeechManager.dylib](DYLIBS/libAXSpeechManager.dylib.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAppPatch.dylib](DYLIBS/libAppPatch.dylib.md)
- [/usr/lib/libAppleArchive.dylib](DYLIBS/libAppleArchive.dylib.md)
- [/usr/lib/libAppleEXR.dylib](DYLIBS/libAppleEXR.dylib.md)
- [/usr/lib/libAppleSSEExt.dylib](DYLIBS/libAppleSSEExt.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libAudioStatistics.dylib](DYLIBS/libAudioStatistics.dylib.md)
- [/usr/lib/libAudioToolboxUtility.dylib](DYLIBS/libAudioToolboxUtility.dylib.md)
- [/usr/lib/libBASupport.dylib](DYLIBS/libBASupport.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libBBUpdaterDynamic_stubs.dylib](DYLIBS/libBBUpdaterDynamic_stubs.dylib.md)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib.md)
- [/usr/lib/libBasebandCommandDrivers.dylib](DYLIBS/libBasebandCommandDrivers.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libCRFSuite.dylib](DYLIBS/libCRFSuite.dylib.md)
- [/usr/lib/libCTGreenTeaLogger.dylib](DYLIBS/libCTGreenTeaLogger.dylib.md)
- [/usr/lib/libChineseTokenizer.dylib](DYLIBS/libChineseTokenizer.dylib.md)
- [/usr/lib/libCoreEntitlements.dylib](DYLIBS/libCoreEntitlements.dylib.md)
- [/usr/lib/libDHCPServer.A.dylib](DYLIBS/libDHCPServer.A.dylib.md)
- [/usr/lib/libETLDIAGLoggingDynamic.dylib](DYLIBS/libETLDIAGLoggingDynamic.dylib.md)
- [/usr/lib/libETLDLFDynamic.dylib](DYLIBS/libETLDLFDynamic.dylib.md)
- [/usr/lib/libETLDLOADCoreDumpDynamic.dylib](DYLIBS/libETLDLOADCoreDumpDynamic.dylib.md)
- [/usr/lib/libETLDLOADDynamic.dylib](DYLIBS/libETLDLOADDynamic.dylib.md)
- [/usr/lib/libETLDMCDynamic.dylib](DYLIBS/libETLDMCDynamic.dylib.md)
- [/usr/lib/libETLDynamic.dylib](DYLIBS/libETLDynamic.dylib.md)
- [/usr/lib/libETLEFSDumpDynamic.dylib](DYLIBS/libETLEFSDumpDynamic.dylib.md)
- [/usr/lib/libETLSAHDynamic.dylib](DYLIBS/libETLSAHDynamic.dylib.md)
- [/usr/lib/libFDR.dylib](DYLIBS/libFDR.dylib.md)
- [/usr/lib/libFDRDecode.dylib](DYLIBS/libFDRDecode.dylib.md)
- [/usr/lib/libFosl_dynamic.dylib](DYLIBS/libFosl_dynamic.dylib.md)
- [/usr/lib/libHDLCDynamic.dylib](DYLIBS/libHDLCDynamic.dylib.md)
- [/usr/lib/libHSFilerDynamic.dylib](DYLIBS/libHSFilerDynamic.dylib.md)
- [/usr/lib/libICEClient.dylib](DYLIBS/libICEClient.dylib.md)
- [/usr/lib/libIOABP.dylib](DYLIBS/libIOABP.dylib.md)
- [/usr/lib/libIOACIPC.dylib](DYLIBS/libIOACIPC.dylib.md)
- [/usr/lib/libIOACIPCBB.dylib](DYLIBS/libIOACIPCBB.dylib.md)
- [/usr/lib/libIOAccessoryManager.dylib](DYLIBS/libIOAccessoryManager.dylib.md)
- [/usr/lib/libIOReport.dylib](DYLIBS/libIOReport.dylib.md)
- [/usr/lib/libInFieldCollection.dylib](DYLIBS/libInFieldCollection.dylib.md)
- [/usr/lib/libKTLDynamic.dylib](DYLIBS/libKTLDynamic.dylib.md)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/usr/lib/libMTLHud.dylib](DYLIBS/libMTLHud.dylib.md)
- [/usr/lib/libMatch.1.dylib](DYLIBS/libMatch.1.dylib.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileCheckpoint.dylib](DYLIBS/libMobileCheckpoint.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libMobileGestaltExtensions.dylib](DYLIBS/libMobileGestaltExtensions.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libNFC_HAL.dylib](DYLIBS/libNFC_HAL.dylib.md)
- [/usr/lib/libPCITransport.dylib](DYLIBS/libPCITransport.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libPPM.dylib](DYLIBS/libPPM.dylib.md)
- [/usr/lib/libPPMDataModel.dylib](DYLIBS/libPPMDataModel.dylib.md)
- [/usr/lib/libParallelCompression.dylib](DYLIBS/libParallelCompression.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libRemoteTelephonyTransport.dylib](DYLIBS/libRemoteTelephonyTransport.dylib.md)
- [/usr/lib/libReverseProxyDevice.dylib](DYLIBS/libReverseProxyDevice.dylib.md)
- [/usr/lib/libRoseBooter.dylib](DYLIBS/libRoseBooter.dylib.md)
- [/usr/lib/libSCLM.dylib](DYLIBS/libSCLM.dylib.md)
- [/usr/lib/libSESShared.dylib](DYLIBS/libSESShared.dylib.md)
- [/usr/lib/libSLAMDynamic.dylib](DYLIBS/libSLAMDynamic.dylib.md)
- [/usr/lib/libSMC.dylib](DYLIBS/libSMC.dylib.md)
- [/usr/lib/libSoftwareUpdateSSO.dylib](DYLIBS/libSoftwareUpdateSSO.dylib.md)
- [/usr/lib/libSystem.B.dylib](DYLIBS/libSystem.B.dylib.md)
- [/usr/lib/libSystemHealth.dylib](DYLIBS/libSystemHealth.dylib.md)
- [/usr/lib/libTLE.dylib](DYLIBS/libTLE.dylib.md)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib.md)
- [/usr/lib/libTelephonyIOKitDynamic.dylib](DYLIBS/libTelephonyIOKitDynamic.dylib.md)
- [/usr/lib/libTelephonyUSBDynamic.dylib](DYLIBS/libTelephonyUSBDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libThaiTokenizer.dylib](DYLIBS/libThaiTokenizer.dylib.md)
- [/usr/lib/libWAPI.dylib](DYLIBS/libWAPI.dylib.md)
- [/usr/lib/libWISSupport.dylib](DYLIBS/libWISSupport.dylib.md)
- [/usr/lib/libWirelessAudioIPC.dylib](DYLIBS/libWirelessAudioIPC.dylib.md)
- [/usr/lib/libacmobileshim.dylib](DYLIBS/libacmobileshim.dylib.md)
- [/usr/lib/libafc.dylib](DYLIBS/libafc.dylib.md)
- [/usr/lib/libamsupport.dylib](DYLIBS/libamsupport.dylib.md)
- [/usr/lib/libapp_launch_measurement.dylib](DYLIBS/libapp_launch_measurement.dylib.md)
- [/usr/lib/libapple_nghttp2.dylib](DYLIBS/libapple_nghttp2.dylib.md)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib.md)
- [/usr/lib/libate.dylib](DYLIBS/libate.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libbsm.0.dylib](DYLIBS/libbsm.0.dylib.md)
- [/usr/lib/libbz2.1.0.dylib](DYLIBS/libbz2.1.0.dylib.md)
- [/usr/lib/libc++.1.dylib](DYLIBS/libc++.1.dylib.md)
- [/usr/lib/libc++abi.dylib](DYLIBS/libc++abi.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libcharset.1.dylib](DYLIBS/libcharset.1.dylib.md)
- [/usr/lib/libcmark-gfm.dylib](DYLIBS/libcmark-gfm.dylib.md)
- [/usr/lib/libcmph.dylib](DYLIBS/libcmph.dylib.md)
- [/usr/lib/libcompression.dylib](DYLIBS/libcompression.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcoretls.dylib](DYLIBS/libcoretls.dylib.md)
- [/usr/lib/libcoretls_cfhelpers.dylib](DYLIBS/libcoretls_cfhelpers.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libcupolicy.dylib](DYLIBS/libcupolicy.dylib.md)
- [/usr/lib/libdns_services.dylib](DYLIBS/libdns_services.dylib.md)
- [/usr/lib/libdscsym.dylib](DYLIBS/libdscsym.dylib.md)
- [/usr/lib/libedit.3.dylib](DYLIBS/libedit.3.dylib.md)
- [/usr/lib/libenergytrace.dylib](DYLIBS/libenergytrace.dylib.md)
- [/usr/lib/libexpat.1.dylib](DYLIBS/libexpat.1.dylib.md)
- [/usr/lib/libexslt.0.dylib](DYLIBS/libexslt.0.dylib.md)
- [/usr/lib/libffi.dylib](DYLIBS/libffi.dylib.md)
- [/usr/lib/libfire7.dylib](DYLIBS/libfire7.dylib.md)
- [/usr/lib/libform.5.4.dylib](DYLIBS/libform.5.4.dylib.md)
- [/usr/lib/libgermantok.dylib](DYLIBS/libgermantok.dylib.md)
- [/usr/lib/libheimdal-asn1.dylib](DYLIBS/libheimdal-asn1.dylib.md)
- [/usr/lib/libheimdalasn1.dylib](DYLIBS/libheimdalasn1.dylib.md)
- [/usr/lib/libiconv.2.dylib](DYLIBS/libiconv.2.dylib.md)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libipsec.A.dylib](DYLIBS/libipsec.A.dylib.md)
- [/usr/lib/liblangid.dylib](DYLIBS/liblangid.dylib.md)
- [/usr/lib/libllvm-flatbuffers.dylib](DYLIBS/libllvm-flatbuffers.dylib.md)
- [/usr/lib/libllvm-lmdb.dylib](DYLIBS/libllvm-lmdb.dylib.md)
- [/usr/lib/liblockdown.dylib](DYLIBS/liblockdown.dylib.md)
- [/usr/lib/liblzma.5.dylib](DYLIBS/liblzma.5.dylib.md)
- [/usr/lib/libmarisa.dylib](DYLIBS/libmarisa.dylib.md)
- [/usr/lib/libmav_ipc_router_dynamic.dylib](DYLIBS/libmav_ipc_router_dynamic.dylib.md)
- [/usr/lib/libmd.dylib](DYLIBS/libmd.dylib.md)
- [/usr/lib/libmdns.dylib](DYLIBS/libmdns.dylib.md)
- [/usr/lib/libmecab.dylib](DYLIBS/libmecab.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libmorphun.dylib](DYLIBS/libmorphun.dylib.md)
- [/usr/lib/libmrc.dylib](DYLIBS/libmrc.dylib.md)
- [/usr/lib/libncurses.5.4.dylib](DYLIBS/libncurses.5.4.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib.md)
- [/usr/lib/libnfrestore.dylib](DYLIBS/libnfrestore.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libnfstorage.dylib](DYLIBS/libnfstorage.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libolaf.dylib](DYLIBS/libolaf.dylib.md)
- [/usr/lib/libpartition2_dynamic.dylib](DYLIBS/libpartition2_dynamic.dylib.md)
- [/usr/lib/libpcap.A.dylib](DYLIBS/libpcap.A.dylib.md)
- [/usr/lib/libperfcheck.dylib](DYLIBS/libperfcheck.dylib.md)
- [/usr/lib/libpmenergy.dylib](DYLIBS/libpmenergy.dylib.md)
- [/usr/lib/libpmsample.dylib](DYLIBS/libpmsample.dylib.md)
- [/usr/lib/libprequelite.dylib](DYLIBS/libprequelite.dylib.md)
- [/usr/lib/libprotobuf-lite.dylib](DYLIBS/libprotobuf-lite.dylib.md)
- [/usr/lib/libprotobuf.dylib](DYLIBS/libprotobuf.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/librealtime_safety.dylib](DYLIBS/librealtime_safety.dylib.md)
- [/usr/lib/libresolv.9.dylib](DYLIBS/libresolv.9.dylib.md)
- [/usr/lib/libsandbox.1.dylib](DYLIBS/libsandbox.1.dylib.md)
- [/usr/lib/libsbuf.dylib](DYLIBS/libsbuf.dylib.md)
- [/usr/lib/libskit.dylib](DYLIBS/libskit.dylib.md)
- [/usr/lib/libsp.dylib](DYLIBS/libsp.dylib.md)
- [/usr/lib/libspindump.dylib](DYLIBS/libspindump.dylib.md)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib.md)
- [/usr/lib/libsysdiagnose.dylib](DYLIBS/libsysdiagnose.dylib.md)
- [/usr/lib/libsysmon.dylib](DYLIBS/libsysmon.dylib.md)
- [/usr/lib/libsystemstats.dylib](DYLIBS/libsystemstats.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libtidy.A.dylib](DYLIBS/libtidy.A.dylib.md)
- [/usr/lib/libtzupdate.dylib](DYLIBS/libtzupdate.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/libutil.dylib](DYLIBS/libutil.dylib.md)
- [/usr/lib/libxml2.2.dylib](DYLIBS/libxml2.2.dylib.md)
- [/usr/lib/libxo.dylib](DYLIBS/libxo.dylib.md)
- [/usr/lib/libxpc_datastores.dylib](DYLIBS/libxpc_datastores.dylib.md)
- [/usr/lib/libxslt.1.dylib](DYLIBS/libxslt.1.dylib.md)
- [/usr/lib/libz.1.dylib](DYLIBS/libz.1.dylib.md)
- [/usr/lib/log/liblog_IOHIDFamily.dylib](DYLIBS/liblog_IOHIDFamily.dylib.md)
- [/usr/lib/log/liblog_SystemConfiguration.dylib](DYLIBS/liblog_SystemConfiguration.dylib.md)
- [/usr/lib/log/liblog_coreacc.dylib](DYLIBS/liblog_coreacc.dylib.md)
- [/usr/lib/log/liblog_geo.dylib](DYLIBS/liblog_geo.dylib.md)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib.md)
- [/usr/lib/log/liblog_mdns.dylib](DYLIBS/liblog_mdns.dylib.md)
- [/usr/lib/log/liblog_mdnsresponder.dylib](DYLIBS/liblog_mdnsresponder.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/log/liblog_signpost.description.dylib](DYLIBS/liblog_signpost.description.dylib.md)
- [/usr/lib/log/liblog_signpost.dylib](DYLIBS/liblog_signpost.dylib.md)
- [/usr/lib/log/liblog_signpost.telemetry.dylib](DYLIBS/liblog_signpost.telemetry.dylib.md)
- [/usr/lib/log/liblog_srp.dylib](DYLIBS/liblog_srp.dylib.md)
- [/usr/lib/swift/libswiftARKit.dylib](DYLIBS/libswiftARKit.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftAppleArchive.dylib](DYLIBS/libswiftAppleArchive.dylib.md)
- [/usr/lib/swift/libswiftAssetsLibrary.dylib](DYLIBS/libswiftAssetsLibrary.dylib.md)
- [/usr/lib/swift/libswiftCallKit.dylib](DYLIBS/libswiftCallKit.dylib.md)
- [/usr/lib/swift/libswiftCarPlay.dylib](DYLIBS/libswiftCarPlay.dylib.md)
- [/usr/lib/swift/libswiftCompression.dylib](DYLIBS/libswiftCompression.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreAudio.dylib](DYLIBS/libswiftCoreAudio.dylib.md)
- [/usr/lib/swift/libswiftCoreFoundation.dylib](DYLIBS/libswiftCoreFoundation.dylib.md)
- [/usr/lib/swift/libswiftCoreGraphics.dylib](DYLIBS/libswiftCoreGraphics.dylib.md)
- [/usr/lib/swift/libswiftCoreImage.dylib](DYLIBS/libswiftCoreImage.dylib.md)
- [/usr/lib/swift/libswiftCoreLocation.dylib](DYLIBS/libswiftCoreLocation.dylib.md)
- [/usr/lib/swift/libswiftCoreMIDI.dylib](DYLIBS/libswiftCoreMIDI.dylib.md)
- [/usr/lib/swift/libswiftCoreML.dylib](DYLIBS/libswiftCoreML.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftCryptoTokenKit.dylib](DYLIBS/libswiftCryptoTokenKit.dylib.md)
- [/usr/lib/swift/libswiftDarwin.dylib](DYLIBS/libswiftDarwin.dylib.md)
- [/usr/lib/swift/libswiftDemangle.dylib](DYLIBS/libswiftDemangle.dylib.md)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib.md)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib.md)
- [/usr/lib/swift/libswiftFileProvider.dylib](DYLIBS/libswiftFileProvider.dylib.md)
- [/usr/lib/swift/libswiftGLKit.dylib](DYLIBS/libswiftGLKit.dylib.md)
- [/usr/lib/swift/libswiftGameplayKit.dylib](DYLIBS/libswiftGameplayKit.dylib.md)
- [/usr/lib/swift/libswiftIntents.dylib](DYLIBS/libswiftIntents.dylib.md)
- [/usr/lib/swift/libswiftMLCompute.dylib](DYLIBS/libswiftMLCompute.dylib.md)
- [/usr/lib/swift/libswiftMapKit.dylib](DYLIBS/libswiftMapKit.dylib.md)
- [/usr/lib/swift/libswiftMetal.dylib](DYLIBS/libswiftMetal.dylib.md)
- [/usr/lib/swift/libswiftMetalKit.dylib](DYLIBS/libswiftMetalKit.dylib.md)
- [/usr/lib/swift/libswiftMetricKit.dylib](DYLIBS/libswiftMetricKit.dylib.md)
- [/usr/lib/swift/libswiftModelIO.dylib](DYLIBS/libswiftModelIO.dylib.md)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib.md)
- [/usr/lib/swift/libswiftNearbyInteraction.dylib](DYLIBS/libswiftNearbyInteraction.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)
- [/usr/lib/swift/libswiftOSLog.dylib](DYLIBS/libswiftOSLog.dylib.md)
- [/usr/lib/swift/libswiftObjectiveC.dylib](DYLIBS/libswiftObjectiveC.dylib.md)
- [/usr/lib/swift/libswiftObservation.dylib](DYLIBS/libswiftObservation.dylib.md)
- [/usr/lib/swift/libswiftPassKit.dylib](DYLIBS/libswiftPassKit.dylib.md)
- [/usr/lib/swift/libswiftQuartzCore.dylib](DYLIBS/libswiftQuartzCore.dylib.md)
- [/usr/lib/swift/libswiftRegexBuilder.dylib](DYLIBS/libswiftRegexBuilder.dylib.md)
- [/usr/lib/swift/libswiftSceneKit.dylib](DYLIBS/libswiftSceneKit.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftSpriteKit.dylib](DYLIBS/libswiftSpriteKit.dylib.md)
- [/usr/lib/swift/libswiftSwiftOnoneSupport.dylib](DYLIBS/libswiftSwiftOnoneSupport.dylib.md)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib.md)
- [/usr/lib/swift/libswiftSystem_Foundation.dylib](DYLIBS/libswiftSystem_Foundation.dylib.md)
- [/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib](DYLIBS/libswiftUniformTypeIdentifiers.dylib.md)
- [/usr/lib/swift/libswiftVideoToolbox.dylib](DYLIBS/libswiftVideoToolbox.dylib.md)
- [/usr/lib/swift/libswiftVision.dylib](DYLIBS/libswiftVision.dylib.md)
- [/usr/lib/swift/libswiftWatchKit.dylib](DYLIBS/libswiftWatchKit.dylib.md)
- [/usr/lib/swift/libswiftWebKit.dylib](DYLIBS/libswiftWebKit.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib.md)
- [/usr/lib/swift/libswift_Differentiation.dylib](DYLIBS/libswift_Differentiation.dylib.md)
- [/usr/lib/swift/libswift_RegexParser.dylib](DYLIBS/libswift_RegexParser.dylib.md)
- [/usr/lib/swift/libswift_StringProcessing.dylib](DYLIBS/libswift_StringProcessing.dylib.md)
- [/usr/lib/swift/libswiftos.dylib](DYLIBS/libswiftos.dylib.md)
- [/usr/lib/swift/libswiftsimd.dylib](DYLIBS/libswiftsimd.dylib.md)
- [/usr/lib/swift/~libswiftPencilKit.dylib](DYLIBS/~libswiftPencilKit.dylib.md)
- [/usr/lib/system/libcache.dylib](DYLIBS/libcache.dylib.md)
- [/usr/lib/system/libcommonCrypto.dylib](DYLIBS/libcommonCrypto.dylib.md)
- [/usr/lib/system/libcompiler_rt.dylib](DYLIBS/libcompiler_rt.dylib.md)
- [/usr/lib/system/libcopyfile.dylib](DYLIBS/libcopyfile.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libdispatch.dylib](DYLIBS/libdispatch.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libmacho.dylib](DYLIBS/libmacho.dylib.md)
- [/usr/lib/system/libremovefile.dylib](DYLIBS/libremovefile.dylib.md)
- [/usr/lib/system/libsystem_asl.dylib](DYLIBS/libsystem_asl.dylib.md)
- [/usr/lib/system/libsystem_blocks.dylib](DYLIBS/libsystem_blocks.dylib.md)
- [/usr/lib/system/libsystem_c.dylib](DYLIBS/libsystem_c.dylib.md)
- [/usr/lib/system/libsystem_collections.dylib](DYLIBS/libsystem_collections.dylib.md)
- [/usr/lib/system/libsystem_configuration.dylib](DYLIBS/libsystem_configuration.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_coreservices.dylib](DYLIBS/libsystem_coreservices.dylib.md)
- [/usr/lib/system/libsystem_darwin.dylib](DYLIBS/libsystem_darwin.dylib.md)
- [/usr/lib/system/libsystem_darwindirectory.dylib](DYLIBS/libsystem_darwindirectory.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_featureflags.dylib](DYLIBS/libsystem_featureflags.dylib.md)
- [/usr/lib/system/libsystem_info.dylib](DYLIBS/libsystem_info.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)
- [/usr/lib/system/libsystem_m.dylib](DYLIBS/libsystem_m.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_networkextension.dylib](DYLIBS/libsystem_networkextension.dylib.md)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib.md)
- [/usr/lib/system/libsystem_platform.dylib](DYLIBS/libsystem_platform.dylib.md)
- [/usr/lib/system/libsystem_pthread.dylib](DYLIBS/libsystem_pthread.dylib.md)
- [/usr/lib/system/libsystem_sandbox.dylib](DYLIBS/libsystem_sandbox.dylib.md)
- [/usr/lib/system/libsystem_sanitizers.dylib](DYLIBS/libsystem_sanitizers.dylib.md)
- [/usr/lib/system/libsystem_symptoms.dylib](DYLIBS/libsystem_symptoms.dylib.md)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib.md)
- [/usr/lib/system/libunwind.dylib](DYLIBS/libunwind.dylib.md)
- [/usr/lib/system/libxpc.dylib](DYLIBS/libxpc.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libAppleTCONUpdater.dylib](DYLIBS/libAppleTCONUpdater.dylib.md)
- [/usr/lib/updaters/libAppleTconUARPUpdater.dylib](DYLIBS/libAppleTconUARPUpdater.dylib.md)
- [/usr/lib/updaters/libRoseUpdater.dylib](DYLIBS/libRoseUpdater.dylib.md)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib.md)
- [/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib](DYLIBS/libSavageRestoreInfo_iOS.dylib.md)
- [/usr/lib/updaters/libSavageUpdater_iOS.dylib](DYLIBS/libSavageUpdater_iOS.dylib.md)
- [/usr/lib/updaters/libT200Updater.dylib](DYLIBS/libT200Updater.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

## EOF
