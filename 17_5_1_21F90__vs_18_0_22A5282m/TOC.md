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

#### ❌ Removed (1)

- `com.apple.driver.AppleSamsungSPI`

#### ⬆️ Updated (253)

<details>
  <summary><i>View Updated</i></summary>

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

>  `com.apple.iokit.IOStorageFamily`

```diff

   __DATA_CONST.__kalloc_type: 0x700
   __DATA_CONST.__kalloc_var: 0x320
   Symbols:   0
-  Functions: 0
+  Functions: 578
 

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

>  `com.apple.IOTextEncryptionFamily`

```diff

   __DATA_CONST.__const: 0xe68
   __DATA_CONST.__kalloc_type: 0x100
   Symbols:   0
-  Functions: 0
+  Functions: 88
 

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

>  `com.apple.driver.AppleUSBMassStorageInterfaceNub`

```diff

   __DATA_CONST.__const: 0x600
   __DATA_CONST.__kalloc_type: 0x40
   Symbols:   0
-  Functions: 0
+  Functions: 30
 

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

</details>

### KDKs

- [KDK DIFF](KDK.md)

## MachO

### 🆕 NEW (315)

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

### ❌ Removed (65)

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

### ⬆️ Updated (2624)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AAUIViewService.app/AAUIViewService](MACHOS/AAUIViewService)
- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService)
- [/Applications/AXRemoteViewService.app/AXRemoteViewService](MACHOS/AXRemoteViewService)
- [/Applications/AXUIViewService.app/AXUIViewService](MACHOS/AXUIViewService)
- [/Applications/AccountAuthenticationDialog.app/AccountAuthenticationDialog](MACHOS/AccountAuthenticationDialog)
- [/Applications/ActivityMessagesApp.app/ActivityMessagesApp](MACHOS/ActivityMessagesApp)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI)
- [/Applications/AirPlayReceiver.app/AirPlayReceiver](MACHOS/AirPlayReceiver)
- [/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp](MACHOS/AirPlaySenderUIApp)
- [/Applications/AnimojiStickers.app/AnimojiStickers](MACHOS/AnimojiStickers)
- [/Applications/AnimojiStickers.app/PlugIns/AnimojiStickersExtension.appex/AnimojiStickersExtension](MACHOS/AnimojiStickersExtension)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel)
- [/Applications/AppSSOUIService.app/AppSSOUIService](MACHOS/AppSSOUIService)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension)
- [/Applications/AskPermissionUI.app/AskPermissionUI](MACHOS/AskPermissionUI)
- [/Applications/AskToMessagesHost.app/AskToMessagesHost](MACHOS/AskToMessagesHost)
- [/Applications/AskToMessagesHost.app/Extensions/AskToExtension.appex/AskToExtension](MACHOS/AskToExtension)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension)
- [/Applications/AuthKitUIService.app/AuthKitUIService](MACHOS/AuthKitUIService)
- [/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI](MACHOS/AuthenticationServicesUI)
- [/Applications/AuthenticationServicesUI.app/PlugIns/AccountAuthenticationModificationExtensionHelper.appex/AccountAuthenticationModificationExtensionHelper](MACHOS/AccountAuthenticationModificationExtensionHelper)
- [/Applications/AutoSettings.app/AutoSettings](MACHOS/AutoSettings)
- [/Applications/BacklinkIndicator.app/BacklinkIndicator](MACHOS/BacklinkIndicator)
- [/Applications/BarcodeScanner.app/BarcodeScanner](MACHOS/BarcodeScanner)
- [/Applications/Batteries.app/Batteries](MACHOS/Batteries)
- [/Applications/Batteries.app/PlugIns/BatteriesAvocadoWidgetExtension.appex/BatteriesAvocadoWidgetExtension](MACHOS/BatteriesAvocadoWidgetExtension)
- [/Applications/Batteries.app/PlugIns/BatteriesWidgetExtension.appex/BatteriesWidgetExtension](MACHOS/BatteriesWidgetExtension)
- [/Applications/Batteries.app/PlugIns/BatteriesWidgetIntentsExtension.appex/BatteriesWidgetIntentsExtension](MACHOS/BatteriesWidgetIntentsExtension)
- [/Applications/BusinessChatViewService.app/BusinessChatViewService](MACHOS/BusinessChatViewService)
- [/Applications/BusinessExtensionsWrapper.app/BusinessExtensionsWrapper](MACHOS/BusinessExtensionsWrapper)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business)
- [/Applications/CTCarrierSpaceAuth.app/CTCarrierSpaceAuth](MACHOS/CTCarrierSpaceAuth)
- [/Applications/CTKUIService.app/CTKUIService](MACHOS/CTKUIService)
- [/Applications/CTNotifyUIService.app/CTNotifyUIService](MACHOS/CTNotifyUIService)
- [/Applications/Camera.app/Camera](MACHOS/Camera)
- [/Applications/Camera.app/PlugIns/CameraMessagesApp.appex/CameraMessagesApp](MACHOS/CameraMessagesApp)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings)
- [/Applications/CarPlaySetup.app/CarPlaySetup](MACHOS/CarPlaySetup)
- [/Applications/CarPlaySplashScreen.app/CarPlaySplashScreen](MACHOS/CarPlaySplashScreen)
- [/Applications/CarPlayWallpaper.app/CarPlayWallpaper](MACHOS/CarPlayWallpaper)
- [/Applications/Charge.app/Charge](MACHOS/Charge)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard)
- [/Applications/CheckerBoardRemoteSetup.app/CheckerBoardRemoteSetup](MACHOS/CheckerBoardRemoteSetup)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera)
- [/Applications/ClarityPhotos.app/ClarityPhotos](MACHOS/ClarityPhotos)
- [/Applications/Climate.app/Climate](MACHOS/Climate)
- [/Applications/ClipViewService.app/ClipViewService](MACHOS/ClipViewService)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel)
- [/Applications/Closures.app/Closures](MACHOS/Closures)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService)
- [/Applications/CompassCalibrationViewService.app/CompassCalibrationViewService](MACHOS/CompassCalibrationViewService)
- [/Applications/ContactPhotoCarouselRemoteAlert.app/ContactPhotoCarouselRemoteAlert](MACHOS/ContactPhotoCarouselRemoteAlert)
- [/Applications/ContinuityCaptureShieldUI.app/ContinuityCaptureShieldUI](MACHOS/ContinuityCaptureShieldUI)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI)
- [/Applications/Coverage Details.app/Coverage Details](MACHOS/Coverage_Details)
- [/Applications/CredentialSharingUIViewService.app/CredentialSharingUIViewService](MACHOS/CredentialSharingUIViewService)
- [/Applications/CredentialSharingUIViewService.app/PlugIns/ShareableCredentialsMessagesExtension.appex/ShareableCredentialsMessagesExtension](MACHOS/ShareableCredentialsMessagesExtension)
- [/Applications/DDActionsService.app/DDActionsService](MACHOS/DDActionsService)
- [/Applications/DKPairingUIService.app/DKPairingUIService](MACHOS/DKPairingUIService)
- [/Applications/DemoApp.app/DemoApp](MACHOS/DemoApp)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics)
- [/Applications/Diagnostics.app/PlugIns/com.apple.Diagnostics.diagnosticextension.appex/com.apple.Diagnostics.diagnosticextension](MACHOS/com.apple.Diagnostics.diagnosticextension)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter)
- [/Applications/DiagnosticsService.app/DiagnosticsService](MACHOS/DiagnosticsService)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-0001.appex/Diagnostic-0001](MACHOS/Diagnostic-0001)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3732.appex/Diagnostic-3732](MACHOS/Diagnostic-3732)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3734.appex/Diagnostic-3734](MACHOS/Diagnostic-3734)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3738.appex/Diagnostic-3738](MACHOS/Diagnostic-3738)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3741.appex/Diagnostic-3741](MACHOS/Diagnostic-3741)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3743.appex/Diagnostic-3743](MACHOS/Diagnostic-3743)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3744.appex/Diagnostic-3744](MACHOS/Diagnostic-3744)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3745.appex/Diagnostic-3745](MACHOS/Diagnostic-3745)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3903.appex/Diagnostic-3903](MACHOS/Diagnostic-3903)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3904.appex/Diagnostic-3904](MACHOS/Diagnostic-3904)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3905.appex/Diagnostic-3905](MACHOS/Diagnostic-3905)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3906.appex/Diagnostic-3906](MACHOS/Diagnostic-3906)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3907.appex/Diagnostic-3907](MACHOS/Diagnostic-3907)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3909.appex/Diagnostic-3909](MACHOS/Diagnostic-3909)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939](MACHOS/Diagnostic-3939)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3942.appex/Diagnostic-3942](MACHOS/Diagnostic-3942)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4002.appex/Diagnostic-4002](MACHOS/Diagnostic-4002)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4003.appex/Diagnostic-4003](MACHOS/Diagnostic-4003)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4004.appex/Diagnostic-4004](MACHOS/Diagnostic-4004)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4005.appex/Diagnostic-4005](MACHOS/Diagnostic-4005)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4006.appex/Diagnostic-4006](MACHOS/Diagnostic-4006)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4007.appex/Diagnostic-4007](MACHOS/Diagnostic-4007)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4008.appex/Diagnostic-4008](MACHOS/Diagnostic-4008)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009-iOS-D83-D84.appex/Diagnostic-4009-iOS-D83-D84](MACHOS/Diagnostic-4009-iOS-D83-D84)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153](MACHOS/Diagnostic-4153)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4154.appex/Diagnostic-4154](MACHOS/Diagnostic-4154)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4180.appex/Diagnostic-4180](MACHOS/Diagnostic-4180)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4181.appex/Diagnostic-4181](MACHOS/Diagnostic-4181)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4182.appex/Diagnostic-4182](MACHOS/Diagnostic-4182)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4183.appex/Diagnostic-4183](MACHOS/Diagnostic-4183)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4184.appex/Diagnostic-4184](MACHOS/Diagnostic-4184)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4276.appex/Diagnostic-4276](MACHOS/Diagnostic-4276)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4351.appex/Diagnostic-4351](MACHOS/Diagnostic-4351)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4359.appex/Diagnostic-4359](MACHOS/Diagnostic-4359)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4492-sshb.appex/Diagnostic-4492-sshb](MACHOS/Diagnostic-4492-sshb)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4579.appex/Diagnostic-4579](MACHOS/Diagnostic-4579)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4615.appex/Diagnostic-4615](MACHOS/Diagnostic-4615)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6000.appex/Diagnostic-6000](MACHOS/Diagnostic-6000)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6001.appex/Diagnostic-6001](MACHOS/Diagnostic-6001)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002](MACHOS/Diagnostic-6002)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8035.appex/Diagnostic-8035](MACHOS/Diagnostic-8035)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8068.appex/Diagnostic-8068](MACHOS/Diagnostic-8068)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079](MACHOS/Diagnostic-8079)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8134.appex/Diagnostic-8134](MACHOS/Diagnostic-8134)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187](MACHOS/Diagnostic-8187)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201](MACHOS/Diagnostic-8201)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8209.appex/Diagnostic-8209](MACHOS/Diagnostic-8209)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8217.appex/Diagnostic-8217](MACHOS/Diagnostic-8217)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8238.appex/Diagnostic-8238](MACHOS/Diagnostic-8238)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246](MACHOS/Diagnostic-8246)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253](MACHOS/Diagnostic-8253)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8259.appex/Diagnostic-8259](MACHOS/Diagnostic-8259)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262](MACHOS/Diagnostic-8262)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264](MACHOS/Diagnostic-8264)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276](MACHOS/Diagnostic-8276)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288](MACHOS/Diagnostic-8288)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8290-EFD.appex/Diagnostic-8290-EFD](MACHOS/Diagnostic-8290-EFD)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8357.appex/Diagnostic-8357](MACHOS/Diagnostic-8357)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8374.appex/Diagnostic-8374](MACHOS/Diagnostic-8374)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8381.appex/Diagnostic-8381](MACHOS/Diagnostic-8381)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389](MACHOS/Diagnostic-8389)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Diagnostic-8441](MACHOS/Diagnostic-8441)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Frameworks/DiagnosticsSupport.framework/DiagnosticsSupport](MACHOS/DiagnosticsSupport)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84](MACHOS/SystemReport-iOS-D83-D84)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService)
- [/Applications/ExposureNotificationRemoteViewService.app/ExposureNotificationRemoteViewService](MACHOS/ExposureNotificationRemoteViewService)
- [/Applications/EyeReliefUI.app/EyeReliefUI](MACHOS/EyeReliefUI)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4)
- [/Applications/FaceTimeLinkTrampoline.app/FaceTimeLinkTrampoline](MACHOS/FaceTimeLinkTrampoline)
- [/Applications/Family.app/Family](MACHOS/Family)
- [/Applications/Family.app/PlugIns/FAFollowupExtension.appex/FAFollowupExtension](MACHOS/FAFollowupExtension)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension)
- [/Applications/FamilyControlsAuthenticationUI.app/FamilyControlsAuthenticationUI](MACHOS/FamilyControlsAuthenticationUI)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS)
- [/Applications/FeedbackRemoteView.app/FeedbackRemoteView](MACHOS/FeedbackRemoteView)
- [/Applications/FinanceStub.app/FinanceStub](MACHOS/FinanceStub)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService)
- [/Applications/FindMyExtensionContainer.app/FindMyExtensionContainer](MACHOS/FindMyExtensionContainer)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService)
- [/Applications/FontInstallViewService.app/FontInstallViewService](MACHOS/FontInstallViewService)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService)
- [/Applications/FunCameraEmojiStickers.app/FunCameraEmojiStickers](MACHOS/FunCameraEmojiStickers)
- [/Applications/FunCameraEmojiStickers.app/PlugIns/FunCameraEmojiStickersExtension.appex/FunCameraEmojiStickersExtension](MACHOS/FunCameraEmojiStickersExtension)
- [/Applications/FunCameraShapes.app/FunCameraShapes](MACHOS/FunCameraShapes)
- [/Applications/FunCameraShapes.app/PlugIns/FunCameraShapesExtension.appex/FunCameraShapesExtension](MACHOS/FunCameraShapesExtension)
- [/Applications/FunCameraText.app/FunCameraText](MACHOS/FunCameraText)
- [/Applications/FunCameraText.app/PlugIns/FunCameraTextExtension.appex/FunCameraTextExtension](MACHOS/FunCameraTextExtension)
- [/Applications/GameCenterRemoteAlert.app/GameCenterRemoteAlert](MACHOS/GameCenterRemoteAlert)
- [/Applications/GameCenterUIService.app/GameCenterUIService](MACHOS/GameCenterUIService)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension)
- [/Applications/GameCenterWidgets.app/GameCenterWidgets](MACHOS/GameCenterWidgets)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService)
- [/Applications/HashtagImages.app/HashtagImages](MACHOS/HashtagImages)
- [/Applications/HashtagImages.app/PlugIns/HashtagImagesExtension.appex/HashtagImagesExtension](MACHOS/HashtagImagesExtension)
- [/Applications/HealthENBuddy.app/HealthENBuddy](MACHOS/HealthENBuddy)
- [/Applications/HealthENLauncher.app/HealthENLauncher](MACHOS/HealthENLauncher)
- [/Applications/HealthPrivacyService.app/HealthPrivacyService](MACHOS/HealthPrivacyService)
- [/Applications/HearingApp.app/HearingApp](MACHOS/HearingApp)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService)
- [/Applications/HomeControlService.app/HomeControlService](MACHOS/HomeControlService)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService)
- [/Applications/InCallService.app/PlugIns/FaceTimeShareExtension.appex/FaceTimeShareExtension](MACHOS/FaceTimeShareExtension)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI)
- [/Applications/InCallService.app/PlugIns/RemotePeoplePicker.appex/RemotePeoplePicker](MACHOS/RemotePeoplePicker)
- [/Applications/InputUI.app/InputUI](MACHOS/InputUI)
- [/Applications/Jellyfish.app/Jellyfish](MACHOS/Jellyfish)
- [/Applications/Jellyfish.app/PlugIns/Animoji.appex/Animoji](MACHOS/Animoji)
- [/Applications/MBHelperApp.app/MBHelperApp](MACHOS/MBHelperApp)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController)
- [/Applications/MTLReplayer.app/MTLReplayer](MACHOS/MTLReplayer)
- [/Applications/MailCompositionService.app/MailCompositionService](MACHOS/MailCompositionService)
- [/Applications/Media.app/Media](MACHOS/Media)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI)
- [/Applications/MediaRemoteUIService.app/MediaRemoteUIService](MACHOS/MediaRemoteUIService)
- [/Applications/MessagesViewService.app/MessagesViewService](MACHOS/MessagesViewService)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension)
- [/Applications/MobileReplayer.app/MobileReplayer](MACHOS/MobileReplayer)
- [/Applications/MobileReplayer.app/PlugIns/EAGLReplayControllerSupport.mrplugin/EAGLReplayControllerSupport](MACHOS/EAGLReplayControllerSupport)
- [/Applications/MobileSMS.app/Extensions/MessagesActionExtension.appex/MessagesActionExtension](MACHOS/MessagesActionExtension)
- [/Applications/MobileSMS.app/MobileSMS](MACHOS/MobileSMS)
- [/Applications/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension](MACHOS/MessagesAssistantExtension)
- [/Applications/MobileSMS.app/PlugIns/MessagesAssistantUIExtension.appex/MessagesAssistantUIExtension](MACHOS/MessagesAssistantUIExtension)
- [/Applications/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension](MACHOS/MessagesNotificationExtension)
- [/Applications/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension](MACHOS/MessagesPluginNotificationExtension)
- [/Applications/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension](MACHOS/MessagesTranscriptExtension)
- [/Applications/MobileSMS.app/PlugIns/MobileSMSSpotlightImporter.appex/MobileSMSSpotlightImporter](MACHOS/MobileSMSSpotlightImporter)
- [/Applications/MobileSafari.app/Extensions/SafariLinkExtension.appex/SafariLinkExtension](MACHOS/SafariLinkExtension)
- [/Applications/MobileSafari.app/MobileSafari](MACHOS/MobileSafari)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension)
- [/Applications/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension](MACHOS/com.apple.mobilesafari.SafariDiagnosticExtension)
- [/Applications/MobileSafari.app/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker](MACHOS/com.apple.Safari.SandboxBroker)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow)
- [/Applications/MobileSlideShow.app/PlugIns/PhotoPicker.appex/PhotoPicker](MACHOS/PhotoPicker)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosDestructiveChangeConfirmation.appex/PhotosDestructiveChangeConfirmation](MACHOS/PhotosDestructiveChangeConfirmation)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosFileProvider.appex/PhotosFileProvider](MACHOS/PhotosFileProvider)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMemoriesNotificationUpdates.appex/PhotosMemoriesNotificationUpdates](MACHOS/PhotosMemoriesNotificationUpdates)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMessagesApp.appex/PhotosMessagesApp](MACHOS/PhotosMessagesApp)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates](MACHOS/PhotosNotificationsUpdates)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosPicker.appex/PhotosPicker](MACHOS/PhotosPicker)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosTCCNotificationExtension.appex/PhotosTCCNotificationExtension](MACHOS/PhotosTCCNotificationExtension)
- [/Applications/MobileSlideShow.app/PlugIns/com.apple.social.StreamShareService.appex/com.apple.social.StreamShareService](MACHOS/com.apple.social.StreamShareService)
- [/Applications/MomentsUIService.app/Frameworks/MomentsUIServiceCore.framework/MomentsUIServiceCore](MACHOS/MomentsUIServiceCore)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition)
- [/Applications/MusicUIService.app/MusicUIService](MACHOS/MusicUIService)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService)
- [/Applications/PDUIApp.app/PDUIApp](MACHOS/PDUIApp)
- [/Applications/PassbookSecureUIService.app/PassbookSecureUIService](MACHOS/PassbookSecureUIService)
- [/Applications/PassbookUISceneService.app/PassbookUISceneService](MACHOS/PassbookUISceneService)
- [/Applications/PassbookUIService.app/PassbookUIService](MACHOS/PassbookUIService)
- [/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension](MACHOS/PeerPaymentMessagesExtension)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService)
- [/Applications/PeopleMessageService.app/PeopleMessageService](MACHOS/PeopleMessageService)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension)
- [/Applications/PeopleViewService.app/PlugIns/SelectPerson_iOS.appex/SelectPerson_iOS](MACHOS/SelectPerson_iOS)
- [/Applications/PhotosUIService.app/PhotosUIService](MACHOS/PhotosUIService)
- [/Applications/PosterBoard.app/PlugIns/WallpaperDiagnosticExtension.appex/WallpaperDiagnosticExtension](MACHOS/WallpaperDiagnosticExtension)
- [/Applications/PosterBoard.app/PosterBoard](MACHOS/PosterBoard)
- [/Applications/PreBoard.app/PreBoard](MACHOS/PreBoard)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell)
- [/Applications/Print Center.app/Print Center](MACHOS/Print_Center)
- [/Applications/ProximityReaderSceneUI.app/ProximityReaderSceneUI](MACHOS/ProximityReaderSceneUI)
- [/Applications/ProximityReaderUIService.app/ProximityReaderUIService](MACHOS/ProximityReaderUIService)
- [/Applications/RecoverDeviceUI.app/RecoverDeviceUI](MACHOS/RecoverDeviceUI)
- [/Applications/RemotePaymentPassActionsService.app/PlugIns/RemotePaymentPassActionsMessagesExtension.appex/RemotePaymentPassActionsMessagesExtension](MACHOS/RemotePaymentPassActionsMessagesExtension)
- [/Applications/RemotePaymentPassActionsService.app/RemotePaymentPassActionsService](MACHOS/RemotePaymentPassActionsService)
- [/Applications/RemoteiCloudQuotaUI.app/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI)
- [/Applications/ReplayKitAngel.app/ReplayKitAngel](MACHOS/ReplayKitAngel)
- [/Applications/SIMSetupUIService.app/SIMSetupUIService](MACHOS/SIMSetupUIService)
- [/Applications/SLYahooAuth.app/PlugIns/SLYahooAuthService.appex/SLYahooAuthService](MACHOS/SLYahooAuthService)
- [/Applications/SLYahooAuth.app/SLYahooAuth](MACHOS/SLYahooAuth)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter)
- [/Applications/SMS Filter.app/SMS Filter](MACHOS/SMS_Filter)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy)
- [/Applications/SafariViewService.app/SafariViewService](MACHOS/SafariViewService)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension)
- [/Applications/Screen Time.app/Screen Time](MACHOS/Screen_Time)
- [/Applications/ScreenSharingViewService.app/ScreenSharingViewService](MACHOS/ScreenSharingViewService)
- [/Applications/ScreenTimeUnlock.app/ScreenTimeUnlock](MACHOS/ScreenTimeUnlock)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService)
- [/Applications/Setup.app/Setup](MACHOS/Setup)
- [/Applications/SharedWebCredentialViewService.app/SharedWebCredentialViewService](MACHOS/SharedWebCredentialViewService)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI)
- [/Applications/ShortcutsViewService.app/ShortcutsViewService](MACHOS/ShortcutsViewService)
- [/Applications/Sidecar.app/PlugIns/ContinuityCamera.appex/ContinuityCamera](MACHOS/ContinuityCamera)
- [/Applications/Sidecar.app/PlugIns/ContinuityCapture.appex/ContinuityCapture](MACHOS/ContinuityCapture)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay)
- [/Applications/Sidecar.app/PlugIns/ContinuityMarkup.appex/ContinuityMarkup](MACHOS/ContinuityMarkup)
- [/Applications/Sidecar.app/PlugIns/ContinuitySignature.appex/ContinuitySignature](MACHOS/ContinuitySignature)
- [/Applications/Sidecar.app/PlugIns/ContinuitySketch.appex/ContinuitySketch](MACHOS/ContinuitySketch)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar)
- [/Applications/Siri.app/Siri](MACHOS/Siri)
- [/Applications/SleepLockScreen.app/SleepLockScreen](MACHOS/SleepLockScreen)
- [/Applications/SleepWidgetContainer.app/PlugIns/SleepWidgetExtension.appex/SleepWidgetExtension](MACHOS/SleepWidgetExtension)
- [/Applications/SleepWidgetContainer.app/SleepWidgetContainer](MACHOS/SleepWidgetContainer)
- [/Applications/SoftwareUpdateUIService.app/PlugIns/SUSUIVerifyingAlertCFUserNotificationUIExtension.appex/SUSUIVerifyingAlertCFUserNotificationUIExtension](MACHOS/SUSUIVerifyingAlertCFUserNotificationUIExtension)
- [/Applications/SoftwareUpdateUIService.app/PlugIns/SUSUInstallAlertCFUserNotificationUIExtension.appex/SUSUInstallAlertCFUserNotificationUIExtension](MACHOS/SUSUInstallAlertCFUserNotificationUIExtension)
- [/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService](MACHOS/SoftwareUpdateUIService)
- [/Applications/Spotlight.app/Spotlight](MACHOS/Spotlight)
- [/Applications/SpringBoardEducation.app/SpringBoardEducation](MACHOS/SpringBoardEducation)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension)
- [/Applications/StickersUltra.app/StickersUltra](MACHOS/StickersUltra)
- [/Applications/StoreDemoViewService.app/StoreDemoViewService](MACHOS/StoreDemoViewService)
- [/Applications/StoreKitUIService.app/StoreKitUIService](MACHOS/StoreKitUIService)
- [/Applications/SubcredentialUIService.app/PlugIns/SubcredentialInvitationMessagesExtension.appex/SubcredentialInvitationMessagesExtension](MACHOS/SubcredentialInvitationMessagesExtension)
- [/Applications/SubcredentialUIService.app/SubcredentialUIService](MACHOS/SubcredentialUIService)
- [/Applications/SystemPaperViewService.app/SystemPaperViewService](MACHOS/SystemPaperViewService)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService)
- [/Applications/TVAccessViewService.app/TVAccessViewService](MACHOS/TVAccessViewService)
- [/Applications/TVRemoteUIService.app/PlugIns/TVRemoteIntentExtension.appex/TVRemoteIntentExtension](MACHOS/TVRemoteIntentExtension)
- [/Applications/TVRemoteUIService.app/TVRemoteUIService](MACHOS/TVRemoteUIService)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure)
- [/Applications/Trip.app/Trip](MACHOS/Trip)
- [/Applications/TrustMe.app/TrustMe](MACHOS/TrustMe)
- [/Applications/VideoSubscriberAccountViewService.app/VideoSubscriberAccountViewService](MACHOS/VideoSubscriberAccountViewService)
- [/Applications/Web.app/Web](MACHOS/Web)
- [/Applications/WebContentAnalysisUI.app/WebContentAnalysisUI](MACHOS/WebContentAnalysisUI)
- [/Applications/WebSheet.app/WebSheet](MACHOS/WebSheet)
- [/Applications/WidgetRenderer_CarPlay.app/WidgetRenderer_CarPlay](MACHOS/WidgetRenderer_CarPlay)
- [/Applications/WidgetRenderer_Default.app/WidgetRenderer_Default](MACHOS/WidgetRenderer_Default)
- [/Applications/WorkoutRemoteViewService.app/WorkoutRemoteViewService](MACHOS/WorkoutRemoteViewService)
- [/Applications/iCloud+.app/iCloud+](MACHOS/iCloud+)
- [/Applications/iCloud.app/iCloud](MACHOS/iCloud)
- [/Applications/iMessageAppsViewService.app/iMessageAppsViewService](MACHOS/iMessageAppsViewService)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension)
- [/System/DriverKit/usr/lib/libSystem_debug.dylib](MACHOS/libSystem_debug.dylib)
- [/System/DriverKit/usr/lib/system/libdispatch_debug.dylib](MACHOS/libdispatch_debug.dylib)
- [/System/DriverKit/usr/lib/system/libdispatch_profile.dylib](MACHOS/libdispatch_profile.dylib)
- [/System/DriverKit/usr/lib/system/libsystem_blocks_debug.dylib](MACHOS/libsystem_blocks_debug.dylib)
- [/System/DriverKit/usr/lib/system/libsystem_blocks_profile.dylib](MACHOS/libsystem_blocks_profile.dylib)
- [/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib](MACHOS/libsystem_c_debug.dylib)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib)
- [/System/DriverKit/usr/lib/system/libsystem_platform_debug.dylib](MACHOS/libsystem_platform_debug.dylib)
- [/System/DriverKit/usr/lib/system/libsystem_pthread_debug.dylib](MACHOS/libsystem_pthread_debug.dylib)
- [/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib](MACHOS/libsystem_trace_debug.dylib)
- [/System/Library/AccessibilityBundles/AXAggregateStatisticsServer.axuiservice/AXAggregateStatisticsServer](MACHOS/AXAggregateStatisticsServer)
- [/System/Library/AccessibilityBundles/AXAssetAndDataServer.axuiservice/AXAssetAndDataServer](MACHOS/AXAssetAndDataServer)
- [/System/Library/AccessibilityBundles/AXAuditAXUIService.axuiservice/AXAuditAXUIService](MACHOS/AXAuditAXUIService)
- [/System/Library/AccessibilityBundles/AXBannerUIServer.axuiservice/AXBannerUIServer](MACHOS/AXBannerUIServer)
- [/System/Library/AccessibilityBundles/AXBuddyBundle.bundle/AXBuddyBundle](MACHOS/AXBuddyBundle)
- [/System/Library/AccessibilityBundles/AXContainerManagerServer.axuiservice/AXContainerManagerServer](MACHOS/AXContainerManagerServer)
- [/System/Library/AccessibilityBundles/AXElementInteractionUIServer.axuiservice/AXElementInteractionUIServer](MACHOS/AXElementInteractionUIServer)
- [/System/Library/AccessibilityBundles/AXIDSServer.axuiservice/AXIDSServer](MACHOS/AXIDSServer)
- [/System/Library/AccessibilityBundles/AXLocalizationCaptionServer.axuiservice/AXLocalizationCaptionServer](MACHOS/AXLocalizationCaptionServer)
- [/System/Library/AccessibilityBundles/AXUltronPluginService.axuiservice/AXUltronPluginService](MACHOS/AXUltronPluginService)
- [/System/Library/AccessibilityBundles/AXWatchRemoteScreenUIServer.axuiservice/AXWatchRemoteScreenUIServer](MACHOS/AXWatchRemoteScreenUIServer)
- [/System/Library/AccessibilityBundles/ActivityAchievementsUI.axbundle/ActivityAchievementsUI](MACHOS/ActivityAchievementsUI)
- [/System/Library/AccessibilityBundles/ActivityBridgeSetup.axbundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup)
- [/System/Library/AccessibilityBundles/ActivityRingsUI.axbundle/ActivityRingsUI](MACHOS/ActivityRingsUI)
- [/System/Library/AccessibilityBundles/ActivitySharing.axbundle/ActivitySharing](MACHOS/ActivitySharing)
- [/System/Library/AccessibilityBundles/ActivitySharingUI.axbundle/ActivitySharingUI](MACHOS/ActivitySharingUI)
- [/System/Library/AccessibilityBundles/AssistiveTouch.axuiservice/AssistiveTouch](MACHOS/AssistiveTouch)
- [/System/Library/AccessibilityBundles/BackTapUIServer.axuiservice/BackTapUIServer](MACHOS/BackTapUIServer)
- [/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer](MACHOS/ClarityUIServer)
- [/System/Library/AccessibilityBundles/ClockAngel.axbundle/ClockAngel](MACHOS/ClockAngel)
- [/System/Library/AccessibilityBundles/DisplayFilterUIServer.axuiservice/DisplayFilterUIServer](MACHOS/DisplayFilterUIServer)
- [/System/Library/AccessibilityBundles/FitnessApp.axbundle/FitnessApp](MACHOS/FitnessApp)
- [/System/Library/AccessibilityBundles/FitnessUI.axbundle/FitnessUI](MACHOS/FitnessUI)
- [/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer](MACHOS/GAXBackboardServer)
- [/System/Library/AccessibilityBundles/GAXClient.bundle/GAXClient](MACHOS/GAXClient)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer)
- [/System/Library/AccessibilityBundles/GuidedAccess.axuiservice/GuidedAccess](MACHOS/GuidedAccess)
- [/System/Library/AccessibilityBundles/HoverTextUIServer.axuiservice/HoverTextUIServer](MACHOS/HoverTextUIServer)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService)
- [/System/Library/AccessibilityBundles/NTKCustomization.axbundle/NTKCustomization](MACHOS/NTKCustomization)
- [/System/Library/AccessibilityBundles/NTKUltraCubeFaceBundleCompanion.axbundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion)
- [/System/Library/AccessibilityBundles/NanoMailBridgeSettings.axbundle/NanoMailBridgeSettings](MACHOS/NanoMailBridgeSettings)
- [/System/Library/AccessibilityBundles/NanoMediaBridgeUI.axbundle/NanoMediaBridgeUI](MACHOS/NanoMediaBridgeUI)
- [/System/Library/AccessibilityBundles/NanoPeopleBridgeSettings.axbundle/NanoPeopleBridgeSettings](MACHOS/NanoPeopleBridgeSettings)
- [/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion](MACHOS/NanoTimeKitCompanion)
- [/System/Library/AccessibilityBundles/PingMyWatchControlCenterUI.axbundle/PingMyWatchControlCenterUI](MACHOS/PingMyWatchControlCenterUI)
- [/System/Library/AccessibilityBundles/SchoolTimeSettingsUI.axbundle/SchoolTimeSettingsUI](MACHOS/SchoolTimeSettingsUI)
- [/System/Library/AccessibilityBundles/ScreenSharing.axuiservice/ScreenSharing](MACHOS/ScreenSharing)
- [/System/Library/AccessibilityBundles/SiriSetup.axbundle/SiriSetup](MACHOS/SiriSetup)
- [/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer](MACHOS/SpeakServer)
- [/System/Library/AccessibilityBundles/SpeakThis.axuiservice/SpeakThis](MACHOS/SpeakThis)
- [/System/Library/AccessibilityBundles/StickyKeys.axuiservice/StickyKeys](MACHOS/StickyKeys)
- [/System/Library/AccessibilityBundles/TouchAccommodations.axuiservice/TouchAccommodations](MACHOS/TouchAccommodations)
- [/System/Library/AccessibilityBundles/VisualAlerts.bundle/VisualAlerts](MACHOS/VisualAlerts)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver)
- [/System/Library/AccessibilityBundles/WidgetRenderer.axbundle/WidgetRenderer](MACHOS/WidgetRenderer)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow)
- [/System/Library/AccessibilityBundles/activity-widget.axbundle/activity-widget](MACHOS/activity-widget)
- [/System/Library/AccessibilityBundles/com.apple.NanoTimeKit.CreateWatchFace.axbundle/com.apple.NanoTimeKit.CreateWatchFace](MACHOS/com.apple.NanoTimeKit.CreateWatchFace)
- [/System/Library/Accounts/AppleIDLoginPlugins/FMFAppleIDLoginPlugin.bundle/FMFAppleIDLoginPlugin](MACHOS/FMFAppleIDLoginPlugin)
- [/System/Library/Accounts/AppleIDLoginPlugins/FaceTimeAppleIDLoginPlugin.bundle/FaceTimeAppleIDLoginPlugin](MACHOS/FaceTimeAppleIDLoginPlugin)
- [/System/Library/Accounts/AppleIDLoginPlugins/GameCenterAppleIDLoginPlugin.bundle/GameCenterAppleIDLoginPlugin](MACHOS/GameCenterAppleIDLoginPlugin)
- [/System/Library/Accounts/AppleIDLoginPlugins/ISLoginPlugin.bundle/ISLoginPlugin](MACHOS/ISLoginPlugin)
- [/System/Library/Accounts/AppleIDLoginPlugins/MadridAppleIDLoginPlugin.bundle/MadridAppleIDLoginPlugin](MACHOS/MadridAppleIDLoginPlugin)
- [/System/Library/Accounts/AppleIDLoginPlugins/iCloudAppleIDLoginPlugin.bundle/iCloudAppleIDLoginPlugin](MACHOS/iCloudAppleIDLoginPlugin)
- [/System/Library/Accounts/Authentication/AAGKAuthenticationPlugin.bundle/AAGKAuthenticationPlugin](MACHOS/AAGKAuthenticationPlugin)
- [/System/Library/Accounts/Authentication/AAIDSAuthenticationPlugin.bundle/AAIDSAuthenticationPlugin](MACHOS/AAIDSAuthenticationPlugin)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/AppleAccountAuthenticationDelegate.bundle/AppleAccountAuthenticationDelegate](MACHOS/AppleAccountAuthenticationDelegate)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/GameCenterAppleIDAuthenticationDelegate.bundle/GameCenterAppleIDAuthenticationDelegate](MACHOS/GameCenterAppleIDAuthenticationDelegate)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/IDSAuthenticationDelegatePlugin.bundle/IDSAuthenticationDelegatePlugin](MACHOS/IDSAuthenticationDelegatePlugin)
- [/System/Library/Accounts/DataclassOwners/Bookmarks.bundle/Bookmarks](MACHOS/Bookmarks)
- [/System/Library/Accounts/DataclassOwners/Calendar.bundle/Calendar](MACHOS/Calendar)
- [/System/Library/Accounts/DataclassOwners/CloudDocsDataclassOwnerPlugin.bundle/CloudDocsDataclassOwnerPlugin](MACHOS/CloudDocsDataclassOwnerPlugin)
- [/System/Library/Accounts/DataclassOwners/ContactsDataclassOwner.bundle/ContactsDataclassOwner](MACHOS/ContactsDataclassOwner)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner)
- [/System/Library/Accounts/DataclassOwners/HealthDataclassOwnerPlugin.bundle/HealthDataclassOwnerPlugin](MACHOS/HealthDataclassOwnerPlugin)
- [/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner](MACHOS/JournalDataclassOwner)
- [/System/Library/Accounts/DataclassOwners/KeychainDataclassOwner.bundle/KeychainDataclassOwner](MACHOS/KeychainDataclassOwner)
- [/System/Library/Accounts/DataclassOwners/MessagesDataclassOwner.bundle/MessagesDataclassOwner](MACHOS/MessagesDataclassOwner)
- [/System/Library/Accounts/DataclassOwners/News.bundle/News](MACHOS/News)
- [/System/Library/Accounts/DataclassOwners/Notes.bundle/Notes](MACHOS/Notes)
- [/System/Library/Accounts/DataclassOwners/RemindersDataclassOwnerPlugin.bundle/RemindersDataclassOwnerPlugin](MACHOS/RemindersDataclassOwnerPlugin)
- [/System/Library/Accounts/DataclassOwners/SiriDataclassOwner.bundle/SiriDataclassOwner](MACHOS/SiriDataclassOwner)
- [/System/Library/Accounts/DataclassOwners/StocksDataclassOwner.bundle/StocksDataclassOwner](MACHOS/StocksDataclassOwner)
- [/System/Library/Accounts/Notification/ASDAccountNotificationPlugin.bundle/ASDAccountNotificationPlugin](MACHOS/ASDAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/AccountNotificationPlugin](MACHOS/AccountNotificationPlugin)
- [/System/Library/Accounts/Notification/AccountSuggestionNotificationPlugin.bundle/AccountSuggestionNotificationPlugin](MACHOS/AccountSuggestionNotificationPlugin)
- [/System/Library/Accounts/Notification/CloudBookmarksAccountsNotifier.bundle/CloudBookmarksAccountsNotifier](MACHOS/CloudBookmarksAccountsNotifier)
- [/System/Library/Accounts/Notification/CloudDocsAccountNotificationPlugin.bundle/CloudDocsAccountNotificationPlugin](MACHOS/CloudDocsAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/CoreAccessoriesAccountNotificationPlugin.bundle/CoreAccessoriesAccountNotificationPlugin](MACHOS/CoreAccessoriesAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/DeviceManagementClientAccountNotificationPlugin.bundle/DeviceManagementClientAccountNotificationPlugin](MACHOS/DeviceManagementClientAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/MBPrebuddyAccountNotificationPlugin.bundle/MBPrebuddyAccountNotificationPlugin](MACHOS/MBPrebuddyAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/MCAccountNotificationPlugin.bundle/MCAccountNotificationPlugin](MACHOS/MCAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/NanoMailAccountNotificationPlugin.bundle/NanoMailAccountNotificationPlugin](MACHOS/NanoMailAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/NanoPassbookAccountNotificationPlugin.bundle/NanoPassbookAccountNotificationPlugin](MACHOS/NanoPassbookAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/RemoteManagementAccountNotificationPlugin.bundle/RemoteManagementAccountNotificationPlugin](MACHOS/RemoteManagementAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/SyncedDefaultsAccountNotificationPlugin.bundle/SyncedDefaultsAccountNotificationPlugin](MACHOS/SyncedDefaultsAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/TransparencyAccountNotification.bundle/TransparencyAccountNotification](MACHOS/TransparencyAccountNotification)
- [/System/Library/Accounts/Notification/iTunesAccountsNotificationPlugin.bundle/iTunesAccountsNotificationPlugin](MACHOS/iTunesAccountsNotificationPlugin)
- [/System/Library/Accounts/ServiceOwners/AACloudServiceOwner.bundle/AACloudServiceOwner](MACHOS/AACloudServiceOwner)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner)
- [/System/Library/Accounts/ServiceOwners/GCCloudServiceOwner.bundle/GCCloudServiceOwner](MACHOS/GCCloudServiceOwner)
- [/System/Library/Accounts/ServiceOwners/IDSServiceOwner.bundle/IDSServiceOwner](MACHOS/IDSServiceOwner)
- [/System/Library/AppRemovalServices/com.apple.Bridge.appremoval.xpc/com.apple.Bridge.appremoval](MACHOS/com.apple.Bridge.appremoval)
- [/System/Library/AppRemovalServices/com.apple.Home.appremoval.xpc/com.apple.Home.appremoval](MACHOS/com.apple.Home.appremoval)
- [/System/Library/AppRemovalServices/com.apple.Maps.appremoval.xpc/com.apple.Maps.appremoval](MACHOS/com.apple.Maps.appremoval)
- [/System/Library/AppRemovalServices/com.apple.MobileStore.appremoval.xpc/com.apple.MobileStore.appremoval](MACHOS/com.apple.MobileStore.appremoval)
- [/System/Library/AppRemovalServices/com.apple.Translate.appremoval.xpc/com.apple.Translate.appremoval](MACHOS/com.apple.Translate.appremoval)
- [/System/Library/AppRemovalServices/com.apple.VoiceMemos.appremoval.xpc/com.apple.VoiceMemos.appremoval](MACHOS/com.apple.VoiceMemos.appremoval)
- [/System/Library/AppRemovalServices/com.apple.freeform.appremoval.xpc/com.apple.freeform.appremoval](MACHOS/com.apple.freeform.appremoval)
- [/System/Library/AppRemovalServices/com.apple.iBooks.appremoval.xpc/com.apple.iBooks.appremoval](MACHOS/com.apple.iBooks.appremoval)
- [/System/Library/AppRemovalServices/com.apple.mobilecal.appremoval.xpc/com.apple.mobilecal.appremoval](MACHOS/com.apple.mobilecal.appremoval)
- [/System/Library/AppRemovalServices/com.apple.mobilemail.appremoval.xpc/com.apple.mobilemail.appremoval](MACHOS/com.apple.mobilemail.appremoval)
- [/System/Library/AppRemovalServices/com.apple.mobilenotes.appremoval.xpc/com.apple.mobilenotes.appremoval](MACHOS/com.apple.mobilenotes.appremoval)
- [/System/Library/AppRemovalServices/com.apple.news.appremoval.xpc/com.apple.news](MACHOS/com.apple.news)
- [/System/Library/AppRemovalServices/com.apple.podcasts.appremoval.xpc/com.apple.podcasts.appremoval](MACHOS/com.apple.podcasts.appremoval)
- [/System/Library/AppRemovalServices/com.apple.shortcuts.appremoval.xpc/com.apple.shortcuts.appremoval](MACHOS/com.apple.shortcuts.appremoval)
- [/System/Library/AppRemovalServices/com.apple.tv.appremoval.xpc/com.apple.tv.appremoval](MACHOS/com.apple.tv.appremoval)
- [/System/Library/AppRemovalServices/com.apple.weather.appremoval.xpc/com.apple.weather.appremoval](MACHOS/com.apple.weather.appremoval)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin)
- [/System/Library/AppleMediaServices/WebUI/PlugIns/MusicAMSUIWebPlugin.bundle/MusicAMSUIWebPlugin](MACHOS/MusicAMSUIWebPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/AppLaunchPlugin.bundle/AppLaunchPlugin](MACHOS/AppLaunchPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/CalendarFlowDelegatePlugin.bundle/CalendarFlowDelegatePlugin](MACHOS/CalendarFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/ClockFlowPlugin.bundle/ClockFlowPlugin](MACHOS/ClockFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/ContactsFlowDelegatePlugin.bundle/ContactsFlowDelegatePlugin](MACHOS/ContactsFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/ControlsFlowDelegatePlugin.bundle/ControlsFlowDelegatePlugin](MACHOS/ControlsFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/FindMyFlowPlugin.bundle/FindMyFlowPlugin](MACHOS/FindMyFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeAutomationFlowDelegatePlugin.bundle/HomeAutomationFlowDelegatePlugin](MACHOS/HomeAutomationFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/IdentityFlowPlugin.bundle/IdentityFlowPlugin](MACHOS/IdentityFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/MailFlowDelegatePlugin.bundle/MailFlowDelegatePlugin](MACHOS/MailFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/MessagesFlowDelegatePlugin.bundle/MessagesFlowDelegatePlugin](MACHOS/MessagesFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/NotebookFlowPlugin.bundle/NotebookFlowPlugin](MACHOS/NotebookFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/NotificationsFlowDelegatePlugin.bundle/NotificationsFlowDelegatePlugin](MACHOS/NotificationsFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/PaymentsFlowDelegatePlugin.bundle/PaymentsFlowDelegatePlugin](MACHOS/PaymentsFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/ReaderFlowPlugin.bundle/ReaderFlowPlugin](MACHOS/ReaderFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/SafetySessionFlowPlugin.bundle/SafetySessionFlowPlugin](MACHOS/SafetySessionFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriSuggestionsFlowPlugin.bundle/SiriSuggestionsFlowPlugin](MACHOS/SiriSuggestionsFlowPlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/SystemCommandsFlowDelegatePlugin.bundle/SystemCommandsFlowDelegatePlugin](MACHOS/SystemCommandsFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/TranslationFlowDelegatePlugin.bundle/TranslationFlowDelegatePlugin](MACHOS/TranslationFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/VideoFlowDelegatePlugin.bundle/VideoFlowDelegatePlugin](MACHOS/VideoFlowDelegatePlugin)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin)
- [/System/Library/Assistant/Plugins/Accessibility.assistantBundle/Accessibility](MACHOS/Accessibility)
- [/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications](MACHOS/Applications)
- [/System/Library/Assistant/Plugins/ChatKitAssistant.assistantBundle/ChatKitAssistant](MACHOS/ChatKitAssistant)
- [/System/Library/Assistant/Plugins/DeviceControl.assistantBundle/DeviceControl](MACHOS/DeviceControl)
- [/System/Library/Assistant/Plugins/DoNotDisturbAssistant.assistantBundle/DoNotDisturbAssistant](MACHOS/DoNotDisturbAssistant)
- [/System/Library/Assistant/Plugins/Mail.assistantBundle/Mail](MACHOS/Mail)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps)
- [/System/Library/Assistant/Plugins/MobileTimer.assistantBundle/MobileTimer](MACHOS/MobileTimer)
- [/System/Library/Assistant/Plugins/NanoAppSync.assistantBundle/NanoAppSync](MACHOS/NanoAppSync)
- [/System/Library/Assistant/Plugins/NotificationsSettingsAssistant.assistantBundle/NotificationsSettingsAssistant](MACHOS/NotificationsSettingsAssistant)
- [/System/Library/Assistant/Plugins/ParsecContextSync.assistantBundle/ParsecContextSync](MACHOS/ParsecContextSync)
- [/System/Library/Assistant/Plugins/ParsecSubscriptionServiceSync.assistantBundle/ParsecSubscriptionServiceSync](MACHOS/ParsecSubscriptionServiceSync)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant)
- [/System/Library/Assistant/Plugins/Safari.assistantBundle/Safari](MACHOS/Safari)
- [/System/Library/Assistant/Plugins/SiriFindMyBundle.assistantBundle/SiriFindMyBundle](MACHOS/SiriFindMyBundle)
- [/System/Library/Assistant/Plugins/SiriPrivateLearningAnalytics.assistantBundle/SiriPrivateLearningAnalytics](MACHOS/SiriPrivateLearningAnalytics)
- [/System/Library/Assistant/Plugins/Social.assistantBundle/Social](MACHOS/Social)
- [/System/Library/Assistant/Plugins/Stocks.assistantBundle/Stocks](MACHOS/Stocks)
- [/System/Library/Assistant/Plugins/UILite.assistantBundle/UILite](MACHOS/UILite)
- [/System/Library/Assistant/Plugins/WatchListAssistant.assistantBundle/WatchListAssistant](MACHOS/WatchListAssistant)
- [/System/Library/Assistant/Plugins/WebSearch.assistantBundle/WebSearch](MACHOS/WebSearch)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriReferenceResolutionMetricsPlugin.bundle/SiriReferenceResolutionMetricsPlugin](MACHOS/SiriReferenceResolutionMetricsPlugin)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge)
- [/System/Library/Assistant/Suggestions/SKEBridge/SiriSuggestionsSKEBridge.bundle/SiriSuggestionsSKEBridge](MACHOS/SiriSuggestionsSKEBridge)
- [/System/Library/Assistant/UIPlugins/AcousticId.siriUIBundle/AcousticId](MACHOS/AcousticId)
- [/System/Library/Assistant/UIPlugins/AddressBook.siriUIBundle/AddressBook](MACHOS/AddressBook)
- [/System/Library/Assistant/UIPlugins/Calendar.siriUIBundle/Calendar](MACHOS/Calendar)
- [/System/Library/Assistant/UIPlugins/GeneralKnowledge.siriUIBundle/GeneralKnowledge](MACHOS/GeneralKnowledge)
- [/System/Library/Assistant/UIPlugins/Intents.siriUIBundle/Intents](MACHOS/Intents)
- [/System/Library/Assistant/UIPlugins/Mail.siriUIBundle/Mail](MACHOS/Mail)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps)
- [/System/Library/Assistant/UIPlugins/MobileTimer.siriUIBundle/MobileTimer](MACHOS/MobileTimer)
- [/System/Library/Assistant/UIPlugins/Notes.siriUIBundle/Notes](MACHOS/Notes)
- [/System/Library/Assistant/UIPlugins/Notifications.siriUIBundle/Notifications](MACHOS/Notifications)
- [/System/Library/Assistant/UIPlugins/RemindersSiriUIPlugin.siriUIBundle/RemindersSiriUIPlugin](MACHOS/RemindersSiriUIPlugin)
- [/System/Library/Assistant/UIPlugins/Settings.siriUIBundle/Settings](MACHOS/Settings)
- [/System/Library/Assistant/UIPlugins/Stocks.siriUIBundle/Stocks](MACHOS/Stocks)
- [/System/Library/Assistant/UIPlugins/System.siriUIBundle/System](MACHOS/System)
- [/System/Library/Assistant/UIPlugins/UniversalSearch.siriUIBundle/UniversalSearch](MACHOS/UniversalSearch)
- [/System/Library/Assistant/UIPlugins/WAAnswer.siriUIBundle/WAAnswer](MACHOS/WAAnswer)
- [/System/Library/Audio/MIDI Drivers/AppleIDAMDriver.plugin/AppleIDAMDriver](MACHOS/AppleIDAMDriver)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIBluetoothDriver.plugin/AppleMIDIBluetoothDriver](MACHOS/AppleMIDIBluetoothDriver)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIRTPDriver.plugin/AppleMIDIRTPDriver](MACHOS/AppleMIDIRTPDriver)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver](MACHOS/AppleMIDIUSBDriver)
- [/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver](MACHOS/YamahaUSBMIDIDriver)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen)
- [/System/Library/Audio/Plug-Ins/HAL/AppleAOPAudioPlugin.driver/AppleAOPAudioPlugin](MACHOS/AppleAOPAudioPlugin)
- [/System/Library/Audio/Plug-Ins/HAL/AppleTimeSyncAudioClock.driver/AppleTimeSyncAudioClock](MACHOS/AppleTimeSyncAudioClock)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin)
- [/System/Library/Audio/Plug-Ins/HAL/BasebandVoice.driver/BasebandVoice](MACHOS/BasebandVoice)
- [/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin](MACHOS/BuiltinAudioPlugin)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen)
- [/System/Library/Audio/Plug-Ins/HAL/NetworkUplinkClock.driver/NetworkUplinkClock](MACHOS/NetworkUplinkClock)
- [/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen](MACHOS/OctaviaHalogen)
- [/System/Library/Audio/Plug-Ins/RemoteInput/AudioAppleSiriRemoteInput.bundle/AudioAppleSiriRemoteInput](MACHOS/AudioAppleSiriRemoteInput)
- [/System/Library/Audio/Plug-Ins/RemoteInput/JarvisPlugin.bundle/JarvisPlugin](MACHOS/JarvisPlugin)
- [/System/Library/Audio/Plug-Ins/RemoteInput/RemoteAudioInputPlugin.bundle/RemoteAudioInputPlugin](MACHOS/RemoteAudioInputPlugin)
- [/System/Library/BulletinDistributor/PingSubscribers/NanoCalendarPingSubscriber.bundle/NanoCalendarPingSubscriber](MACHOS/NanoCalendarPingSubscriber)
- [/System/Library/BulletinDistributor/PingSubscribers/NanoHealthPingSubscriber.bundle/NanoHealthPingSubscriber](MACHOS/NanoHealthPingSubscriber)
- [/System/Library/BulletinDistributor/PingSubscribers/SearchPartyNotificationPingSubscriber.bundle/SearchPartyNotificationPingSubscriber](MACHOS/SearchPartyNotificationPingSubscriber)
- [/System/Library/BulletinDistributor/PingSubscribers/ShortcutsPingSubscriber.bundle/ShortcutsPingSubscriber](MACHOS/ShortcutsPingSubscriber)
- [/System/Library/CloudRecommendations/ClientSources/ICQReviewLargeFilesRecommendations.bundle/ICQReviewLargeFilesRecommendations](MACHOS/ICQReviewLargeFilesRecommendations)
- [/System/Library/CloudRecommendations/ClientSources/PhotosCloudRecommendations.bundle/PhotosCloudRecommendations](MACHOS/PhotosCloudRecommendations)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule)
- [/System/Library/ControlCenter/Bundles/ContinuousExposeModule.bundle/ContinuousExposeModule](MACHOS/ContinuousExposeModule)
- [/System/Library/ControlCenter/Bundles/FocusUIModule.bundle/FocusUIModule](MACHOS/FocusUIModule)
- [/System/Library/ControlCenter/Bundles/NFCControlCenterModule.bundle/NFCControlCenterModule](MACHOS/NFCControlCenterModule)
- [/System/Library/ControlCenter/Bundles/PingMyWatchControlCenterUI.bundle/PingMyWatchControlCenterUI](MACHOS/PingMyWatchControlCenterUI)
- [/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule](MACHOS/ReplayKitModule)
- [/System/Library/ControlCenter/Bundles/SilenceCallsCCWidget.bundle/SilenceCallsCCWidget](MACHOS/SilenceCallsCCWidget)
- [/System/Library/ControlCenter/Bundles/SystemQuickNoteModule.bundle/SystemQuickNoteModule](MACHOS/SystemQuickNoteModule)
- [/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule](MACHOS/VideoConferenceControlCenterModule)
- [/System/Library/CoreImage/CIBarcode.cifilter/CIBarcode](MACHOS/CIBarcode)
- [/System/Library/CoreImage/CIPassThrough.cifilter/CIPassThrough](MACHOS/CIPassThrough)
- [/System/Library/CoreImage/PortraitFilters.cifilter/PortraitFilters](MACHOS/PortraitFilters)
- [/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer](MACHOS/AccessibilityUIServer)
- [/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents](MACHOS/AccessibilityAppIntents)
- [/System/Library/CoreServices/AegirProxyApp.app/AegirProxyApp](MACHOS/AegirProxyApp)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService)
- [/System/Library/CoreServices/CacheDeleteAppContainerCaches](MACHOS/CacheDeleteAppContainerCaches)
- [/System/Library/CoreServices/CacheDeleteDaily](MACHOS/CacheDeleteDaily)
- [/System/Library/CoreServices/CarPlay.app/CarPlay](MACHOS/CarPlay)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard)
- [/System/Library/CoreServices/CloudSettingsSyncAgent](MACHOS/CloudSettingsSyncAgent)
- [/System/Library/CoreServices/CommandAndControl.app/CommandAndControl](MACHOS/CommandAndControl)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001](MACHOS/MobileDevices-0001)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002](MACHOS/MobileDevices-0002)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003](MACHOS/MobileDevices-0003)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices.bundle/MobileDevices](MACHOS/MobileDevices)
- [/System/Library/CoreServices/DeviceOMatic.app/DeviceOMatic](MACHOS/DeviceOMatic)
- [/System/Library/CoreServices/EscrowSecurityAlert.app/EscrowSecurityAlert](MACHOS/EscrowSecurityAlert)
- [/System/Library/CoreServices/FullKeyboardAccess.app/FullKeyboardAccess](MACHOS/FullKeyboardAccess)
- [/System/Library/CoreServices/IOUIAngel.app/IOUIAngel](MACHOS/IOUIAngel)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI)
- [/System/Library/CoreServices/MediaMLPluginApp.app/MediaMLPluginApp](MACHOS/MediaMLPluginApp)
- [/System/Library/CoreServices/MediaMLPluginApp.app/PlugIns/MediaMLPlugin.appex/MediaMLPlugin](MACHOS/MediaMLPlugin)
- [/System/Library/CoreServices/OTACrashCopier](MACHOS/OTACrashCopier)
- [/System/Library/CoreServices/OverlayUI.app/OverlayUI](MACHOS/OverlayUI)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent)
- [/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer](MACHOS/ScreenSharingServer)
- [/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension](MACHOS/ShortcutsTopHitsExtension)
- [/System/Library/CoreServices/ShortcutsActions.app/ShortcutsActions](MACHOS/ShortcutsActions)
- [/System/Library/CoreServices/SpringBoard.app/PlugIns/SpringBoardDiagnosticExtension.appex/SpringBoardDiagnosticExtension](MACHOS/SpringBoardDiagnosticExtension)
- [/System/Library/CoreServices/SpringBoard.app/SpringBoard](MACHOS/SpringBoard)
- [/System/Library/CoreServices/VoiceOverTouch.app/scrod](MACHOS/scrod)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot)
- [/System/Library/CoreServices/iconservicesagent](MACHOS/iconservicesagent)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd)
- [/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd](MACHOS/usbsmartcardreaderd)
- [/System/Library/DataClassMigrators/00LaunchServicesMigrator.migrator/00LaunchServicesMigrator](MACHOS/00LaunchServicesMigrator)
- [/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration](MACHOS/AccessibilityDataMigration)
- [/System/Library/DataClassMigrators/Accounts.migrator/Accounts](MACHOS/Accounts)
- [/System/Library/DataClassMigrators/AccountsObsolescence.migrator/AccountsObsolescence](MACHOS/AccountsObsolescence)
- [/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy](MACHOS/AddressBookLegacy)
- [/System/Library/DataClassMigrators/AirTrafficMigrator.migrator/AirTrafficMigrator](MACHOS/AirTrafficMigrator)
- [/System/Library/DataClassMigrators/AnisetteMigrator.migrator/AnisetteMigrator](MACHOS/AnisetteMigrator)
- [/System/Library/DataClassMigrators/AppUserDataMigrator.migrator/AppUserDataMigrator](MACHOS/AppUserDataMigrator)
- [/System/Library/DataClassMigrators/AppleAccountMigrator.migrator/AppleAccountMigrator](MACHOS/AppleAccountMigrator)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator)
- [/System/Library/DataClassMigrators/CallHistoryDataMigrator.migrator/CallHistoryDataMigrator](MACHOS/CallHistoryDataMigrator)
- [/System/Library/DataClassMigrators/CloudRecentsMigrator.migrator/CloudRecentsMigrator](MACHOS/CloudRecentsMigrator)
- [/System/Library/DataClassMigrators/CloudTabsMigrator.migrator/CloudTabsMigrator](MACHOS/CloudTabsMigrator)
- [/System/Library/DataClassMigrators/ContainerMigrator.migrator/ContainerMigrator](MACHOS/ContainerMigrator)
- [/System/Library/DataClassMigrators/CookieDataMigrator.migrator/CookieDataMigrator](MACHOS/CookieDataMigrator)
- [/System/Library/DataClassMigrators/CoreLocationMigrator.migrator/CoreLocationMigrator](MACHOS/CoreLocationMigrator)
- [/System/Library/DataClassMigrators/CoreTimeMigrator.migrator/CoreTimeMigrator](MACHOS/CoreTimeMigrator)
- [/System/Library/DataClassMigrators/FitnessMigrator.migrator/FitnessMigrator](MACHOS/FitnessMigrator)
- [/System/Library/DataClassMigrators/HAENDataMigrator.migrator/HAENDataMigrator](MACHOS/HAENDataMigrator)
- [/System/Library/DataClassMigrators/InternationalSupportMigrator.migrator/InternationalSupportMigrator](MACHOS/InternationalSupportMigrator)
- [/System/Library/DataClassMigrators/KeyboardMigrator.migrator/KeyboardMigrator](MACHOS/KeyboardMigrator)
- [/System/Library/DataClassMigrators/KeyboardUIMigrator.migrator/KeyboardUIMigrator](MACHOS/KeyboardUIMigrator)
- [/System/Library/DataClassMigrators/KeychainMigrator.migrator/KeychainMigrator](MACHOS/KeychainMigrator)
- [/System/Library/DataClassMigrators/LanguageAssetMigrator.migrator/LanguageAssetMigrator](MACHOS/LanguageAssetMigrator)
- [/System/Library/DataClassMigrators/LegacyMessageAccountsMigrator.migrator/LegacyMessageAccountsMigrator](MACHOS/LegacyMessageAccountsMigrator)
- [/System/Library/DataClassMigrators/MCCleanup.migrator/MCCleanup](MACHOS/MCCleanup)
- [/System/Library/DataClassMigrators/MCMDM.migrator/MCMDM](MACHOS/MCMDM)
- [/System/Library/DataClassMigrators/MCProfile.migrator/MCProfile](MACHOS/MCProfile)
- [/System/Library/DataClassMigrators/MKBMigrator.migrator/MKBMigrator](MACHOS/MKBMigrator)
- [/System/Library/DataClassMigrators/MSUDataMigrator.migrator/MSUDataMigrator](MACHOS/MSUDataMigrator)
- [/System/Library/DataClassMigrators/MediaLibrary.migrator/MediaLibrary](MACHOS/MediaLibrary)
- [/System/Library/DataClassMigrators/MergeBuddyProvisioningResponse.migrator/MergeBuddyProvisioningResponse](MACHOS/MergeBuddyProvisioningResponse)
- [/System/Library/DataClassMigrators/MessageAccountsMigrator.migrator/MessageAccountsMigrator](MACHOS/MessageAccountsMigrator)
- [/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator](MACHOS/MobileActivationMigrator)
- [/System/Library/DataClassMigrators/MobileAsset.migrator/MobileAsset](MACHOS/MobileAsset)
- [/System/Library/DataClassMigrators/MobileGestaltMigrator.migrator/MobileGestaltMigrator](MACHOS/MobileGestaltMigrator)
- [/System/Library/DataClassMigrators/MobileMailMigrator.migrator/MobileMailMigrator](MACHOS/MobileMailMigrator)
- [/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari](MACHOS/MobileSafari)
- [/System/Library/DataClassMigrators/MobileSlideShow.migrator/MobileSlideShow](MACHOS/MobileSlideShow)
- [/System/Library/DataClassMigrators/PassbookDataMigrator.migrator/PassbookDataMigrator](MACHOS/PassbookDataMigrator)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator)
- [/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess](MACHOS/RestorePostProcess)
- [/System/Library/DataClassMigrators/Shortcuts.migrator/Shortcuts](MACHOS/Shortcuts)
- [/System/Library/DataClassMigrators/Siri.migrator/Siri](MACHOS/Siri)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard)
- [/System/Library/DataClassMigrators/StocksMigrator.migrator/StocksMigrator](MACHOS/StocksMigrator)
- [/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator](MACHOS/SystemAppMigrator)
- [/System/Library/DataClassMigrators/TVMigrator.migrator/TVMigrator](MACHOS/TVMigrator)
- [/System/Library/DataClassMigrators/Tones.migrator/Tones](MACHOS/Tones)
- [/System/Library/DataClassMigrators/Vibrations.migrator/Vibrations](MACHOS/Vibrations)
- [/System/Library/DataClassMigrators/WebBookmarks.migrator/WebBookmarks](MACHOS/WebBookmarks)
- [/System/Library/DataClassMigrators/WiFiDataMigrator.migrator/WiFiDataMigrator](MACHOS/WiFiDataMigrator)
- [/System/Library/DataClassMigrators/iTunesStore.migrator/iTunesStore](MACHOS/iTunesStore)
- [/System/Library/DigitalSeparation/SharingSources/ActivityDigitalSeparation.bundle/ActivityDigitalSeparation](MACHOS/ActivityDigitalSeparation)
- [/System/Library/DigitalSeparation/SharingSources/CalendarSeparation.bundle/CalendarSeparation](MACHOS/CalendarSeparation)
- [/System/Library/DigitalSeparation/SharingSources/DSNotesPlugin.bundle/DSNotesPlugin](MACHOS/DSNotesPlugin)
- [/System/Library/DigitalSeparation/SharingSources/DigitalSeparationBundle.bundle/DigitalSeparationBundle](MACHOS/DigitalSeparationBundle)
- [/System/Library/DigitalSeparation/SharingSources/FindMy.bundle/FindMy](MACHOS/FindMy)
- [/System/Library/DigitalSeparation/SharingSources/FindMyItemsDigitalSeparation.bundle/FindMyItemsDigitalSeparation](MACHOS/FindMyItemsDigitalSeparation)
- [/System/Library/DigitalSeparation/SharingSources/HealthSharingSeparation.bundle/HealthSharingSeparation](MACHOS/HealthSharingSeparation)
- [/System/Library/DigitalSeparation/SharingSources/MapsDigitalSeparation.bundle/MapsDigitalSeparation](MACHOS/MapsDigitalSeparation)
- [/System/Library/DigitalSeparation/SharingSources/PhotosSeparation.bundle/PhotosSeparation](MACHOS/PhotosSeparation)
- [/System/Library/DigitalSeparation/SharingSources/SafetyMonitorSeparation.bundle/SafetyMonitorSeparation](MACHOS/SafetyMonitorSeparation)
- [/System/Library/DistributedEvaluation/Plugins/AutocorrectionTesterDESPlugin.desPlugin/AutocorrectionTesterDESPlugin](MACHOS/AutocorrectionTesterDESPlugin)
- [/System/Library/DistributedEvaluation/Plugins/DictationPersonalizationFides2Plugin.desPlugin/DictationPersonalizationFides2Plugin](MACHOS/DictationPersonalizationFides2Plugin)
- [/System/Library/DistributedEvaluation/Plugins/GlobalNNLMFidesPlugin.desPlugin/GlobalNNLMFidesPlugin](MACHOS/GlobalNNLMFidesPlugin)
- [/System/Library/DistributedEvaluation/Plugins/InertiaCamDES.desPlugin/InertiaCamDES](MACHOS/InertiaCamDES)
- [/System/Library/DistributedEvaluation/Plugins/PMLDESPlugin.desPlugin/PMLDESPlugin](MACHOS/PMLDESPlugin)
- [/System/Library/DistributedEvaluation/Plugins/PeopleSuggesterDESPlugin.desPlugin/PeopleSuggesterDESPlugin](MACHOS/PeopleSuggesterDESPlugin)
- [/System/Library/DistributedEvaluation/Plugins/QuickTypeDESPlugin.desPlugin/QuickTypeDESPlugin](MACHOS/QuickTypeDESPlugin)
- [/System/Library/DistributedEvaluation/Plugins/RemindersDES.desPlugin/RemindersDES](MACHOS/RemindersDES)
- [/System/Library/DistributedEvaluation/Plugins/TypingDESPlugin.desPlugin/TypingDESPlugin](MACHOS/TypingDESPlugin)
- [/System/Library/DistributedEvaluation/Plugins/siriinference-dodml-plugin.desPlugin/siriinference-dodml-plugin](MACHOS/siriinference-dodml-plugin)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.driving-trigger.bundle/com.apple.donotdisturb.private.driving-trigger](MACHOS/com.apple.donotdisturb.private.driving-trigger)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.intents.preload.bundle/com.apple.donotdisturb.private.intents.preload](MACHOS/com.apple.donotdisturb.private.intents.preload)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.workout-trigger.bundle/com.apple.donotdisturb.private.workout-trigger](MACHOS/com.apple.donotdisturb.private.workout-trigger)
- [/System/Library/DriverExtensions/com.apple.AFKUserHIDDrivers.dext/com.apple.AFKUserHIDDrivers](MACHOS/com.apple.AFKUserHIDDrivers)
- [/System/Library/DriverExtensions/com.apple.AppleUserHIDDrivers.dext/com.apple.AppleUserHIDDrivers](MACHOS/com.apple.AppleUserHIDDrivers)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetE1000.dext/com.apple.DriverKit-AppleEthernetE1000](MACHOS/com.apple.DriverKit-AppleEthernetE1000)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetIXGBE.dext/com.apple.DriverKit-AppleEthernetIXGBE](MACHOS/com.apple.DriverKit-AppleEthernetIXGBE)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetIXL.dext/com.apple.DriverKit-AppleEthernetIXL](MACHOS/com.apple.DriverKit-AppleEthernetIXL)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetMLX5.dext/com.apple.DriverKit-AppleEthernetMLX5](MACHOS/com.apple.DriverKit-AppleEthernetMLX5)
- [/System/Library/DriverExtensions/com.apple.DriverKit.AppleUserECM.dext/com.apple.DriverKit.AppleUserECM](MACHOS/com.apple.DriverKit.AppleUserECM)
- [/System/Library/DuetActivityScheduler/Scheduler/DuetActivitySchedulerDaemon.bundle/DuetActivitySchedulerDaemon](MACHOS/DuetActivitySchedulerDaemon)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension)
- [/System/Library/ExtensionKit/Extensions/AppExtensionManagement.appex/AppExtensionManagement](MACHOS/AppExtensionManagement)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker)
- [/System/Library/ExtensionKit/Extensions/BitacoraWorker.appex/BitacoraWorker](MACHOS/BitacoraWorker)
- [/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension](MACHOS/ComposeReviewExtension)
- [/System/Library/ExtensionKit/Extensions/DeepThoughtWorker.appex/DeepThoughtWorker](MACHOS/DeepThoughtWorker)
- [/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension](MACHOS/DevicePropertiesExtension)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension)
- [/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension](MACHOS/ExperimentationExtension)
- [/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU](MACHOS/com.apple.WebKit.GPU)
- [/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension](MACHOS/MADViewServiceExtension)
- [/System/Library/ExtensionKit/Extensions/MapsTransactionInsightsExtension.appex/MapsTransactionInsightsExtension](MACHOS/MapsTransactionInsightsExtension)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension)
- [/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension](MACHOS/MetricsExtension)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension)
- [/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking](MACHOS/com.apple.WebKit.Networking)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK](MACHOS/PFLHRPeriodPredCK)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush](MACHOS/PFLHRPeriodPredPush)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension)
- [/System/Library/ExtensionKit/Extensions/ProactiveShareSheetLighthouseBackgroundPlugin.appex/ProactiveShareSheetLighthouseBackgroundPlugin](MACHOS/ProactiveShareSheetLighthouseBackgroundPlugin)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker](MACHOS/RepackagingWorker)
- [/System/Library/ExtensionKit/Extensions/SiriCoreMetricsWorker.appex/SiriCoreMetricsWorker](MACHOS/SiriCoreMetricsWorker)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/SiriMASPFLCK](MACHOS/SiriMASPFLCK)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLPlugin.appex/SiriMASPFLPlugin](MACHOS/SiriMASPFLPlugin)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/SiriMASPFLPush](MACHOS/SiriMASPFLPush)
- [/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin](MACHOS/SiriSuggestionsLightHousePlugin)
- [/System/Library/ExtensionKit/Extensions/SiriUserSegmentation.appex/SiriUserSegmentation](MACHOS/SiriUserSegmentation)
- [/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal](MACHOS/com.apple.WebKit.WebContent.CaptivePortal)
- [/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent](MACHOS/com.apple.WebKit.WebContent)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat](MACHOS/com.apple.fskit.exfat)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker](MACHOS/com.apple.mlhost.CloudWorker)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.QuartzWorker.appex/com.apple.mlhost.QuartzWorker](MACHOS/com.apple.mlhost.QuartzWorker)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker)
- [/System/Library/Extensions/ASIOKit.kext/ASIOKit](MACHOS/ASIOKit)
- [/System/Library/Extensions/AppleBiometricSensor.kext/PlugIns/AppleMesaLib.plugin/AppleMesaLib](MACHOS/AppleMesaLib)
- [/System/Library/Extensions/AppleGameControllerPersonality.kext/AppleGameControllerPersonality](MACHOS/AppleGameControllerPersonality)
- [/System/Library/Extensions/AppleHIDALSService.kext/PlugIns/AppleHIDALS.plugin/AppleHIDALS](MACHOS/AppleHIDALS)
- [/System/Library/Extensions/AppleHPM.kext/PlugIns/AppleHPMLib.plugin/AppleHPMLib](MACHOS/AppleHPMLib)
- [/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode](MACHOS/AppleLockdownMode)
- [/System/Library/Extensions/ApplePMUFirmwareDriver.kext/ApplePMUFirmwareDriver](MACHOS/ApplePMUFirmwareDriver)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/FastpathLib.plugin/FastpathLib](MACHOS/FastpathLib)
- [/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib](MACHOS/RoseControllerLib)
- [/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleTopCaseHIDEventDriver.kext/AppleTopCaseHIDEventDriver](MACHOS/AppleTopCaseHIDEventDriver)
- [/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleUSBTopCaseDriver.kext/AppleUSBTopCaseDriver](MACHOS/AppleUSBTopCaseDriver)
- [/System/Library/Extensions/AppleUVDM.kext/PlugIns/AppleUVDMLib.plugin/AppleUVDMLib](MACHOS/AppleUVDMLib)
- [/System/Library/Extensions/EAP-RSA.ppp/EAP-RSA](MACHOS/EAP-RSA)
- [/System/Library/Extensions/IOStreamFamily.kext/PlugIns/IOStreamLib.plugin/IOStreamLib](MACHOS/IOStreamLib)
- [/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBLib.bundle/IOUSBLib](MACHOS/IOUSBLib)
- [/System/Library/Extensions/lifs.kext/lifs](MACHOS/lifs)
- [/System/Library/Filesystems/apfs.fs/apfs.util](MACHOS/apfs.util)
- [/System/Library/Filesystems/apfs.fs/apfs_boot_util](MACHOS/apfs_boot_util)
- [/System/Library/Filesystems/apfs.fs/apfs_checkdigest](MACHOS/apfs_checkdigest)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser)
- [/System/Library/Filesystems/apfs.fs/apfs_iosd](MACHOS/apfs_iosd)
- [/System/Library/Filesystems/apfs.fs/apfs_stats](MACHOS/apfs_stats)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs)
- [/System/Library/Filesystems/apfs.fs/mount_apfs](MACHOS/mount_apfs)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs)
- [/System/Library/Filesystems/apfs.fs/slurpAPFSMeta](MACHOS/slurpAPFSMeta)
- [/System/Library/Filesystems/apfs.fs/sm_stats](MACHOS/sm_stats)
- [/System/Library/Filesystems/apfs_userfs.fs/apfs_userfs.util](MACHOS/apfs_userfs.util)
- [/System/Library/Filesystems/apfs_userfs.fs/fsck_apfs](MACHOS/fsck_apfs)
- [/System/Library/Filesystems/apfs_userfs.fs/newfs_apfs](MACHOS/newfs_apfs)
- [/System/Library/Filesystems/exfat.fs/exfat.util](MACHOS/exfat.util)
- [/System/Library/Filesystems/exfat.fs/fsck_exfat](MACHOS/fsck_exfat)
- [/System/Library/Filesystems/exfat.fs/newfs_exfat](MACHOS/newfs_exfat)
- [/System/Library/Filesystems/hfs.fs/CopyHFSMeta](MACHOS/CopyHFSMeta)
- [/System/Library/Filesystems/hfs.fs/fsck_hfs](MACHOS/fsck_hfs)
- [/System/Library/Filesystems/hfs.fs/hfs.util](MACHOS/hfs.util)
- [/System/Library/Filesystems/hfs.fs/mount_hfs](MACHOS/mount_hfs)
- [/System/Library/Filesystems/hfs.fs/newfs_hfs](MACHOS/newfs_hfs)
- [/System/Library/Filesystems/msdos.fs/fsck_msdos](MACHOS/fsck_msdos)
- [/System/Library/Filesystems/msdos.fs/msdos.util](MACHOS/msdos.util)
- [/System/Library/Filesystems/msdos.fs/newfs_msdos](MACHOS/newfs_msdos)
- [/System/Library/Filesystems/ntfs.fs/BootCampFormatter](MACHOS/BootCampFormatter)
- [/System/Library/Filesystems/ntfs.fs/ntfs.util](MACHOS/ntfs.util)
- [/System/Library/Filesystems/tmpfs.fs/mount_tmpfs](MACHOS/mount_tmpfs)
- [/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService](MACHOS/AVAudioDeviceTestService)
- [/System/Library/Frameworks/AVKit.framework/XPCServices/SharedPreferences.xpc/SharedPreferences](MACHOS/SharedPreferences)
- [/System/Library/Frameworks/Accounts.framework/accountsd](MACHOS/accountsd)
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd)
- [/System/Library/Frameworks/AddressBook.framework/Support/ABDatabaseDoctor](MACHOS/ABDatabaseDoctor)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/XPCServices/EnforcementService.xpc/EnforcementService](MACHOS/EnforcementService)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd)
- [/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterService.xpc/AudioConverterService](MACHOS/AudioConverterService)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension)
- [/System/Library/Frameworks/CFNetwork.framework/AuthBrokerAgent](MACHOS/AuthBrokerAgent)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetworkAgent](MACHOS/CFNetworkAgent)
- [/System/Library/Frameworks/CFNetwork.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance)
- [/System/Library/Frameworks/ClassKit.framework/PlugIns/ClassKitDiagnosticExtension.appex/ClassKitDiagnosticExtension](MACHOS/ClassKitDiagnosticExtension)
- [/System/Library/Frameworks/ClassKit.framework/progressd](MACHOS/progressd)
- [/System/Library/Frameworks/ClockKit.framework/XPCServices/CLKCompanionWatchFaceLibraryService.xpc/CLKCompanionWatchFaceLibraryService](MACHOS/CLKCompanionWatchFaceLibraryService)
- [/System/Library/Frameworks/Contacts.framework/PlugIns/ContactsCoreSpotlightExtension.appex/ContactsCoreSpotlightExtension](MACHOS/ContactsCoreSpotlightExtension)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService](MACHOS/ContactViewViewService)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService](MACHOS/ContactsViewService)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension)
- [/System/Library/Frameworks/CoreGraphics.framework/XPCServices/CGPDFService.xpc/CGPDFService](MACHOS/CGPDFService)
- [/System/Library/Frameworks/CoreImage.framework/coreui_archive_bin.metallib](MACHOS/coreui_archive_bin.metallib)
- [/System/Library/Frameworks/CoreImage.framework/photo_style_archive_bin.metallib](MACHOS/photo_style_archive_bin.metallib)
- [/System/Library/Frameworks/CoreImage.framework/portrait_filters_archive_bin.metallib](MACHOS/portrait_filters_archive_bin.metallib)
- [/System/Library/Frameworks/CoreImage.framework/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationTemporaryPreciseAuthPromptPlugin.appex/CoreLocationTemporaryPreciseAuthPromptPlugin](MACHOS/CoreLocationTemporaryPreciseAuthPromptPlugin)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationVanillaWhenInUseAuthPromptPlugin.appex/CoreLocationVanillaWhenInUseAuthPromptPlugin](MACHOS/CoreLocationVanillaWhenInUseAuthPromptPlugin)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice](MACHOS/maphelperservice)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI)
- [/System/Library/Frameworks/CoreMIDI.framework/MIDIServer](MACHOS/MIDIServer)
- [/System/Library/Frameworks/CoreML.framework/XPCServices/CoreMLModelSecurityService.xpc/CoreMLModelSecurityService](MACHOS/CoreMLModelSecurityService)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension1_iOS.appex/CoreSpotlightImportExtension1_iOS](MACHOS/CoreSpotlightImportExtension1_iOS)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension2_iOS.appex/CoreSpotlightImportExtension2_iOS](MACHOS/CoreSpotlightImportExtension2_iOS)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged)
- [/System/Library/Frameworks/CoreTelephony.framework/PlugIns/CTFollowUpExtension.appex/CTFollowUpExtension](MACHOS/CTFollowUpExtension)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/XPCServices/CTParserService.xpc/CTParserService](MACHOS/CTParserService)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter](MACHOS/CommCenter)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper](MACHOS/CommCenterRootHelper)
- [/System/Library/Frameworks/CryptoTokenKit.framework/PlugIns/pivtoken.appex/pivtoken](MACHOS/pivtoken)
- [/System/Library/Frameworks/CryptoTokenKit.framework/PlugIns/secelemtoken.appex/secelemtoken](MACHOS/secelemtoken)
- [/System/Library/Frameworks/CryptoTokenKit.framework/ctkd](MACHOS/ctkd)
- [/System/Library/Frameworks/EventKit.framework/PlugIns/CalendarDiagnosticExtension.appex/CalendarDiagnosticExtension](MACHOS/CalendarDiagnosticExtension)
- [/System/Library/Frameworks/ExposureNotification.framework/XPCServices/ExposureNotificationService.xpc/ExposureNotificationService](MACHOS/ExposureNotificationService)
- [/System/Library/Frameworks/ExtensionFoundation.framework/XPCServices/extensionkitservice.xpc/extensionkitservice](MACHOS/extensionkitservice)
- [/System/Library/Frameworks/ExternalAccessory.framework/PlugIns/ExternalAccessoryWACUIBits.bundle/ExternalAccessoryWACUIBits](MACHOS/ExternalAccessoryWACUIBits)
- [/System/Library/Frameworks/ExternalAccessory.framework/PlugIns/com.apple.ExternalAccessory.WACUI.appex/com.apple.ExternalAccessory.WACUI](MACHOS/com.apple.ExternalAccessory.WACUI)
- [/System/Library/Frameworks/ExternalAccessory.framework/XPCServices/WACEAService.xpc/WACEAService](MACHOS/WACEAService)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/FamilyControlsOverrideSettingsExtension.appex/FamilyControlsOverrideSettingsExtension](MACHOS/FamilyControlsOverrideSettingsExtension)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/CloudDocsFileProvider.bundle/CloudDocsFileProvider](MACHOS/CloudDocsFileProvider)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/FileProviderOverride.bundle/FileProviderOverride](MACHOS/FileProviderOverride)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/iCloudDriveFileProviderOverride.bundle/iCloudDriveFileProviderOverride](MACHOS/iCloudDriveFileProviderOverride)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider)
- [/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd](MACHOS/fileproviderd)
- [/System/Library/Frameworks/FileProviderUI.framework/PlugIns/ServerAuthUIExtension.appex/ServerAuthUIExtension](MACHOS/ServerAuthUIExtension)
- [/System/Library/Frameworks/FinanceKit.framework/financed](MACHOS/financed)
- [/System/Library/Frameworks/GSS.framework/Helpers/GSSCred](MACHOS/GSSCred)
- [/System/Library/Frameworks/GameController.framework/VirtualGameController.bundle/VirtualGameController](MACHOS/VirtualGameController)
- [/System/Library/Frameworks/GroupActivities.framework/XPCServices/GroupSessionService.xpc/GroupSessionService](MACHOS/GroupSessionService)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthCustomerDiagnosticExtension.appex/com.apple.HealthKit.HealthCustomerDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthCustomerDiagnosticExtension)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthDiagnosticExtension.appex/com.apple.HealthKit.HealthDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthDiagnosticExtension)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.appex/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension)
- [/System/Library/Frameworks/HealthKit.framework/healthd](MACHOS/healthd)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension](MACHOS/HomeKitDiagnosticExtension)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitIntentExtension.appex/HomeKitIntentExtension](MACHOS/HomeKitIntentExtension)
- [/System/Library/Frameworks/IdentityLookup.framework/XPCServices/com.apple.IdentityLookup.MessageFilter.xpc/com.apple.IdentityLookup.MessageFilter](MACHOS/com.apple.IdentityLookup.MessageFilter)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc](MACHOS/icprefd-xpc)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc](MACHOS/mscamerad-xpc)
- [/System/Library/Frameworks/ImageIO.framework/PlugIns/com.apple.imageimporter.appex/com.apple.imageimporter](MACHOS/com.apple.imageimporter)
- [/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService](MACHOS/ImageIOXPCService)
- [/System/Library/Frameworks/Intents.framework/XPCServices/intents_helper.xpc/intents_helper](MACHOS/intents_helper)
- [/System/Library/Frameworks/LinkPresentation.framework/PlugIns/YouTubePlayer.wkbundle/YouTubePlayer](MACHOS/YouTubePlayer)
- [/System/Library/Frameworks/LinkPresentation.framework/XPCServices/com.apple.LinkPresentation.LinkSnapshotGeneratorService.xpc/com.apple.LinkPresentation.LinkSnapshotGeneratorService](MACHOS/com.apple.LinkPresentation.LinkSnapshotGeneratorService)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/MechPasscode](MACHOS/MechPasscode)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl](MACHOS/MechPearl)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPushButton.bundle/MechPushButton](MACHOS/MechPushButton)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId](MACHOS/MechTouchId)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM](MACHOS/ModuleACM)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd](MACHOS/applicensedeliveryd)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent)
- [/System/Library/Frameworks/MapKit.framework/XPCServices/com.apple.MapKit.SnapshotService.xpc/com.apple.MapKit.SnapshotService](MACHOS/com.apple.MapKit.SnapshotService)
- [/System/Library/Frameworks/MediaAccessibility.framework/XPCServices/com.apple.accessibility.mediaaccessibilityd.xpc/com.apple.accessibility.mediaaccessibilityd](MACHOS/com.apple.accessibility.mediaaccessibilityd)
- [/System/Library/Frameworks/MediaPlayer.framework/PlugIns/MediaPlayerDiagnosticExtension.appex/MediaPlayerDiagnosticExtension](MACHOS/MediaPlayerDiagnosticExtension)
- [/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService](MACHOS/RemotePlayerService)
- [/System/Library/Frameworks/MessageUI.framework/PlugIns/MessageUI.wkbundle/MessageUI](MACHOS/MessageUI)
- [/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService](MACHOS/MTLCompilerService)
- [/System/Library/Frameworks/ModelIO.framework/XPCServices/AssetLoader.xpc/AssetLoader](MACHOS/AssetLoader)
- [/System/Library/Frameworks/NetworkExtension.framework/PlugIns/NEIKEv2Provider.appex/NEIKEv2Provider](MACHOS/NEIKEv2Provider)
- [/System/Library/Frameworks/OSLog.framework/XPCServices/OSLogService.xpc/OSLogService](MACHOS/OSLogService)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/PDFImporter.appex/PDFImporter](MACHOS/PDFImporter)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Preview.appex/com.apple.PDFKit.OFD_Preview](MACHOS/com.apple.PDFKit.OFD_Preview)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Thumbnail.appex/com.apple.PDFKit.OFD_Thumbnail](MACHOS/com.apple.PDFKit.OFD_Thumbnail)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.PDFExtensionView.appex/com.apple.PDFKit.PDFExtensionView](MACHOS/com.apple.PDFKit.PDFExtensionView)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/ApplePayDiagnostics.appex/ApplePayDiagnostics](MACHOS/ApplePayDiagnostics)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitEngagementExtension.appex/PassKitEngagementExtension](MACHOS/PassKitEngagementExtension)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitIntentsExtension.appex/PassKitIntentsExtension](MACHOS/PassKitIntentsExtension)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitIntentsUIExtension.appex/PassKitIntentsUIExtension](MACHOS/PassKitIntentsUIExtension)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitSpotlightIndexExtension.appex/PassKitSpotlightIndexExtension](MACHOS/PassKitSpotlightIndexExtension)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitThumbnailExtension.appex/PassKitThumbnailExtension](MACHOS/PassKitThumbnailExtension)
- [/System/Library/Frameworks/QuickLook.framework/PlugIns/QLWebKitBundle.wkbundle/QLWebKitBundle](MACHOS/QLWebKitBundle)
- [/System/Library/Frameworks/QuickLook.framework/PlugIns/com.apple.quicklook.extension.previewUI.appex/com.apple.quicklook.extension.previewUI](MACHOS/com.apple.quicklook.extension.previewUI)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent](MACHOS/com.apple.quicklook.ThumbnailsAgent)
- [/System/Library/Frameworks/ReplayKit.framework/PlugIns/RPBroadcastActivityViewControllerExtension.appex/RPBroadcastActivityViewControllerExtension](MACHOS/RPBroadcastActivityViewControllerExtension)
- [/System/Library/Frameworks/ReplayKit.framework/PlugIns/RPVideoEditorExtension.appex/RPVideoEditorExtension](MACHOS/RPVideoEditorExtension)
- [/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader](MACHOS/com.apple.SafariServices.ContentBlockerLoader)
- [/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper)
- [/System/Library/Frameworks/Security.framework/XPCServices/XPCAcmeService.xpc/XPCAcmeService](MACHOS/XPCAcmeService)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent)
- [/System/Library/Frameworks/SensorKit.framework/PlugIns/SensorKitViewService.appex/SensorKitViewService](MACHOS/SensorKitViewService)
- [/System/Library/Frameworks/SensorKit.framework/Support/srsupporttool](MACHOS/srsupporttool)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitDataExport.xpc/SensorKitDataExport](MACHOS/SensorKitDataExport)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitLongTermStorageHelper.xpc/SensorKitLongTermStorageHelper](MACHOS/SensorKitLongTermStorageHelper)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKit.CHSupportService.xpc/com.apple.SensorKit.CHSupportService](MACHOS/com.apple.SensorKit.CHSupportService)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKitAppHelper.xpc/com.apple.SensorKitAppHelper](MACHOS/com.apple.SensorKitAppHelper)
- [/System/Library/Frameworks/ShazamKit.framework/PlugIns/ShazamNotificationContentExtension.appex/ShazamNotificationContentExtension](MACHOS/ShazamNotificationContentExtension)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition)
- [/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension](MACHOS/SKAskPermissionExtension)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd)
- [/System/Library/Frameworks/System.framework/System_asan](MACHOS/System_asan)
- [/System/Library/Frameworks/SystemConfiguration.framework/SCHelper](MACHOS/SCHelper)
- [/System/Library/Frameworks/Translation.framework/translationd](MACHOS/translationd)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ShareUI.appex/com.apple.UIKit.ShareUI](MACHOS/com.apple.UIKit.ShareUI)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/XPCServices/com.apple.VideoSubscriberAccount.DeveloperService.xpc/com.apple.VideoSubscriberAccount.DeveloperService](MACHOS/com.apple.VideoSubscriberAccount.DeveloperService)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/XPCServices/com.apple.VideoSubscriberAccount.PrivacyService.xpc/com.apple.VideoSubscriberAccount.PrivacyService](MACHOS/com.apple.VideoSubscriberAccount.PrivacyService)
- [/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/videodecodeservice](MACHOS/videodecodeservice)
- [/System/Library/Frameworks/VisionKit.framework/PlugIns/KeyboardCamera.appex/KeyboardCamera](MACHOS/KeyboardCamera)
- [/System/Library/Frameworks/WatchKit.framework/Support/companionappd](MACHOS/companionappd)
- [/System/Library/Frameworks/WeatherKit.framework/XPCServices/com.apple.weatherkit.authservice.xpc/com.apple.weatherkit.authservice](MACHOS/com.apple.weatherkit.authservice)
- [/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond](MACHOS/adattributiond)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService)
- [/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin](MACHOS/ColourSensorFilterPlugin)
- [/System/Library/HIDPlugins/ServiceFilters/AppleDeviceManagementHIDFilter.plugin/AppleDeviceManagementHIDFilter](MACHOS/AppleDeviceManagementHIDFilter)
- [/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter](MACHOS/AppleProxServiceFilter)
- [/System/Library/HIDPlugins/ServiceFilters/AppleWirelessChargingServiceFilter.plugin/AppleWirelessChargingServiceFilter](MACHOS/AppleWirelessChargingServiceFilter)
- [/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter](MACHOS/GamepadHIDServiceFilter)
- [/System/Library/HIDPlugins/ServiceFilters/SafetyServiceFilter.plugin/SafetyServiceFilter](MACHOS/SafetyServiceFilter)
- [/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/DualSenseHIDServicePlugin](MACHOS/DualSenseHIDServicePlugin)
- [/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/DualShock4HIDServicePlugin](MACHOS/DualShock4HIDServicePlugin)
- [/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/GenericGamepadHIDServicePlugin](MACHOS/GenericGamepadHIDServicePlugin)
- [/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService](MACHOS/HSTouchHIDService)
- [/System/Library/HIDPlugins/ServicePlugins/IOHIDEventServicePlugin.plugin/IOHIDEventServicePlugin](MACHOS/IOHIDEventServicePlugin)
- [/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/JoyConHIDServicePlugin](MACHOS/JoyConHIDServicePlugin)
- [/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/LunaHIDServicePlugin](MACHOS/LunaHIDServicePlugin)
- [/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin](MACHOS/XboxOneHIDServicePlugin)
- [/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics](MACHOS/IOAnalytics)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDDisplaySessionFilter.plugin/IOHIDDisplaySessionFilter](MACHOS/IOHIDDisplaySessionFilter)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDMotionEventSessionFilter.plugin/IOHIDMotionEventSessionFilter](MACHOS/IOHIDMotionEventSessionFilter)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDRemoteSensorSessionFilter.plugin/IOHIDRemoteSensorSessionFilter](MACHOS/IOHIDRemoteSensorSessionFilter)
- [/System/Library/Health/Plugins/HealthMedicationsDaemonPluginBundle.bundle/HealthMedicationsDaemonPluginBundle](MACHOS/HealthMedicationsDaemonPluginBundle)
- [/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin](MACHOS/HealthRecordsPlugin)
- [/System/Library/Health/Plugins/HearingDaemonPlugin.bundle/HearingDaemonPlugin](MACHOS/HearingDaemonPlugin)
- [/System/Library/Health/Plugins/MentalHealthDaemonPlugin.bundle/MentalHealthDaemonPlugin](MACHOS/MentalHealthDaemonPlugin)
- [/System/Library/Health/Plugins/MobilityDaemonPlugin.bundle/MobilityDaemonPlugin](MACHOS/MobilityDaemonPlugin)
- [/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin](MACHOS/WorkoutHealthPlugin)
- [/System/Library/KerberosPlugins/GSSAPI/AppSSOReplacePlugin_iOS.bundle/AppSSOReplacePlugin_iOS](MACHOS/AppSSOReplacePlugin_iOS)
- [/System/Library/KerberosPlugins/KerberosFrameworkPlugins/AppSSOConfigPlugin_iOS.bundle/AppSSOConfigPlugin_iOS](MACHOS/AppSSOConfigPlugin_iOS)
- [/System/Library/KerberosPlugins/KerberosFrameworkPlugins/AppSSOLocatePlugin_iOS.bundle/AppSSOLocatePlugin_iOS](MACHOS/AppSSOLocatePlugin_iOS)
- [/System/Library/LocationBundles/CompassCalibration.bundle/CompassCalibration](MACHOS/CompassCalibration)
- [/System/Library/LocationBundles/PLAMonitor.bundle/PLAMonitor](MACHOS/PLAMonitor)
- [/System/Library/MediaStreamPlugins/PhotoSharingPlugin.mediastream/PhotoSharingPlugin](MACHOS/PhotoSharingPlugin)
- [/System/Library/Messages/iMessageApps/AnimojiCameraApp.bundle/AnimojiCameraApp](MACHOS/AnimojiCameraApp)
- [/System/Library/Messages/iMessageApps/AudioMessagesExtension.bundle/AudioMessagesExtension](MACHOS/AudioMessagesExtension)
- [/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/FindMyMessagesApp](MACHOS/FindMyMessagesApp)
- [/System/Library/Messages/iMessageApps/FunCameraFilters.bundle/FunCameraFilters](MACHOS/FunCameraFilters)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider)
- [/System/Library/Messages/iMessageBalloons/HandwritingProvider.bundle/HandwritingProvider](MACHOS/HandwritingProvider)
- [/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin](MACHOS/MSMessageExtensionBalloonPlugin)
- [/System/Library/Messages/iMessageBalloons/RichLinkProvider.bundle/RichLinkProvider](MACHOS/RichLinkProvider)
- [/System/Library/Messages/iMessageEffects/CKConfettiEffect.bundle/CKConfettiEffect](MACHOS/CKConfettiEffect)
- [/System/Library/Messages/iMessageEffects/CKEchoEffect.bundle/CKEchoEffect](MACHOS/CKEchoEffect)
- [/System/Library/Messages/iMessageEffects/CKFireworksEffect.bundle/CKFireworksEffect](MACHOS/CKFireworksEffect)
- [/System/Library/Messages/iMessageEffects/CKHappyBirthdayEffect.bundle/CKHappyBirthdayEffect](MACHOS/CKHappyBirthdayEffect)
- [/System/Library/Messages/iMessageEffects/CKHeartEffect.bundle/CKHeartEffect](MACHOS/CKHeartEffect)
- [/System/Library/Messages/iMessageEffects/CKLasersEffect.bundle/CKLasersEffect](MACHOS/CKLasersEffect)
- [/System/Library/Messages/iMessageEffects/CKShootingStarEffect.bundle/CKShootingStarEffect](MACHOS/CKShootingStarEffect)
- [/System/Library/Messages/iMessageEffects/CKSparklesEffect.bundle/CKSparklesEffect](MACHOS/CKSparklesEffect)
- [/System/Library/Messages/iMessageEffects/CKSpotlightEffect.bundle/CKSpotlightEffect](MACHOS/CKSpotlightEffect)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeAppStoreDaemonSettings.bundle/BridgeAppStoreDaemonSettings](MACHOS/BridgeAppStoreDaemonSettings)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeHealthSettings.bundle/BridgeHealthSettings](MACHOS/BridgeHealthSettings)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeRemoteAccounts.bundle/BridgeRemoteAccounts](MACHOS/BridgeRemoteAccounts)
- [/System/Library/NanoPreferenceBundles/Applications/BrookBridgeSettings.bundle/BrookBridgeSettings](MACHOS/BrookBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/DeepBreathingSettings.bundle/DeepBreathingSettings](MACHOS/DeepBreathingSettings)
- [/System/Library/NanoPreferenceBundles/Applications/DepthCompanionSettings.bundle/DepthCompanionSettings](MACHOS/DepthCompanionSettings)
- [/System/Library/NanoPreferenceBundles/Applications/DoseSettings.bundle/DoseSettings](MACHOS/DoseSettings)
- [/System/Library/NanoPreferenceBundles/Applications/FindMyNotificationsSettings.bundle/FindMyNotificationsSettings](MACHOS/FindMyNotificationsSettings)
- [/System/Library/NanoPreferenceBundles/Applications/HealthAppsSettings.bundle/HealthAppsSettings](MACHOS/HealthAppsSettings)
- [/System/Library/NanoPreferenceBundles/Applications/HeartRateSettings.bundle/HeartRateSettings](MACHOS/HeartRateSettings)
- [/System/Library/NanoPreferenceBundles/Applications/MessagesBridgeSettings.bundle/MessagesBridgeSettings](MACHOS/MessagesBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/MindSettings.bundle/MindSettings](MACHOS/MindSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoBedtimeBridgeSettings.bundle/NanoBedtimeBridgeSettings](MACHOS/NanoBedtimeBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoBooksBridgeSettings.bundle/NanoBooksBridgeSettings](MACHOS/NanoBooksBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoCalendarBridgeSettings.bundle/NanoCalendarBridgeSettings](MACHOS/NanoCalendarBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoClockBridgeSettings.bundle/NanoClockBridgeSettings](MACHOS/NanoClockBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoContactsBridgeSettingsOther.bundle/NanoContactsBridgeSettingsOther](MACHOS/NanoContactsBridgeSettingsOther)
- [/System/Library/NanoPreferenceBundles/Applications/NanoContactsBridgeSettingsPaired.bundle/NanoContactsBridgeSettingsPaired](MACHOS/NanoContactsBridgeSettingsPaired)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMailBridgeSettings.bundle/NanoMailBridgeSettings](MACHOS/NanoMailBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMapsBridgeSettings.bundle/NanoMapsBridgeSettings](MACHOS/NanoMapsBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMenstrualCyclesCompanionSettings.bundle/NanoMenstrualCyclesCompanionSettings](MACHOS/NanoMenstrualCyclesCompanionSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMusicBridgeSettings.bundle/NanoMusicBridgeSettings](MACHOS/NanoMusicBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPhotosBridgeSettings.bundle/NanoPhotosBridgeSettings](MACHOS/NanoPhotosBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/NanoTipsBridgeSettings.bundle/NanoTipsBridgeSettings](MACHOS/NanoTipsBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/OxygenSaturationSettings.bundle/OxygenSaturationSettings](MACHOS/OxygenSaturationSettings)
- [/System/Library/NanoPreferenceBundles/Applications/PhoneBridgeSettings.bundle/PhoneBridgeSettings](MACHOS/PhoneBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/PodcastsBridgeSettings.bundle/PodcastsBridgeSettings](MACHOS/PodcastsBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/SessionTrackerAppSettings.bundle/SessionTrackerAppSettings](MACHOS/SessionTrackerAppSettings)
- [/System/Library/NanoPreferenceBundles/Applications/StocksBridgeSettings.bundle/StocksBridgeSettings](MACHOS/StocksBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Applications/TinCanSettings.bundle/TinCanSettings](MACHOS/TinCanSettings)
- [/System/Library/NanoPreferenceBundles/Applications/WeatherExtensionBridgeSettings.bundle/WeatherExtensionBridgeSettings](MACHOS/WeatherExtensionBridgeSettings)
- [/System/Library/NanoPreferenceBundles/Customization/CarouselAppViewSettings.bundle/CarouselAppViewSettings](MACHOS/CarouselAppViewSettings)
- [/System/Library/NanoPreferenceBundles/Customization/CarouselLayoutSettings.bundle/CarouselLayoutSettings](MACHOS/CarouselLayoutSettings)
- [/System/Library/NanoPreferenceBundles/Customization/NTKCustomization.bundle/NTKCustomization](MACHOS/NTKCustomization)
- [/System/Library/NanoPreferenceBundles/Discover/AppsForYourWatchPlugin.bundle/AppsForYourWatchPlugin](MACHOS/AppsForYourWatchPlugin)
- [/System/Library/NanoPreferenceBundles/Discover/CustomizeYourWatchPlugin.bundle/CustomizeYourWatchPlugin](MACHOS/CustomizeYourWatchPlugin)
- [/System/Library/NanoPreferenceBundles/Discover/GetToKnowCurrentSeriesPlugin.bundle/GetToKnowCurrentSeriesPlugin](MACHOS/GetToKnowCurrentSeriesPlugin)
- [/System/Library/NanoPreferenceBundles/Discover/HealthAndFitnessPlugin.bundle/HealthAndFitnessPlugin](MACHOS/HealthAndFitnessPlugin)
- [/System/Library/NanoPreferenceBundles/Discover/UserGuidePlugin.bundle/UserGuidePlugin](MACHOS/UserGuidePlugin)
- [/System/Library/NanoPreferenceBundles/Discover/WelcomeToAppleWatchPlugin.bundle/WelcomeToAppleWatchPlugin](MACHOS/WelcomeToAppleWatchPlugin)
- [/System/Library/NanoPreferenceBundles/Discover/WhatsNewPlugin.bundle/WhatsNewPlugin](MACHOS/WhatsNewPlugin)
- [/System/Library/NanoPreferenceBundles/General/AssistantBridgeSettings.bundle/AssistantBridgeSettings](MACHOS/AssistantBridgeSettings)
- [/System/Library/NanoPreferenceBundles/General/CellularBridgeSettings.bundle/CellularBridgeSettings](MACHOS/CellularBridgeSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionAppBacklightPrivacySettings.bundle/CompanionAppBacklightPrivacySettings](MACHOS/CompanionAppBacklightPrivacySettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionBARSettings.bundle/CompanionBARSettings](MACHOS/CompanionBARSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionComplicationSettings.bundle/CompanionComplicationSettings](MACHOS/CompanionComplicationSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionDockSettings.bundle/CompanionDockSettings](MACHOS/CompanionDockSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionNotificationSettings.bundle/CompanionNotificationSettings](MACHOS/CompanionNotificationSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionReturnToClockSettings.bundle/CompanionReturnToClockSettings](MACHOS/CompanionReturnToClockSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionStingSettings.bundle/CompanionStingSettings](MACHOS/CompanionStingSettings)
- [/System/Library/NanoPreferenceBundles/General/CompanionWakeSettings.bundle/CompanionWakeSettings](MACHOS/CompanionWakeSettings)
- [/System/Library/NanoPreferenceBundles/General/NTKCTritiumSettings.bundle/NTKCTritiumSettings](MACHOS/NTKCTritiumSettings)
- [/System/Library/NanoPreferenceBundles/General/PairedUnlockSettings.bundle/PairedUnlockSettings](MACHOS/PairedUnlockSettings)
- [/System/Library/NanoPreferenceBundles/General/WGAEltonUsersSettingsPhone.bundle/WGAEltonUsersSettingsPhone](MACHOS/WGAEltonUsersSettingsPhone)
- [/System/Library/NanoPreferenceBundles/PrivacySettings/HealthBridgePrivacySettings.bundle/HealthBridgePrivacySettings](MACHOS/HealthBridgePrivacySettings)
- [/System/Library/NanoPreferenceBundles/SetupBundles/AccessibilityBridgeSetup.bundle/AccessibilityBridgeSetup](MACHOS/AccessibilityBridgeSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/BPSStingSetup.bundle/BPSStingSetup](MACHOS/BPSStingSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/CellularSetupBridgeBuddyUI.bundle/CellularSetupBridgeBuddyUI](MACHOS/CellularSetupBridgeBuddyUI)
- [/System/Library/NanoPreferenceBundles/SetupBundles/CompanionAppViewSetup.bundle/CompanionAppViewSetup](MACHOS/CompanionAppViewSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/DepthCompanionSetup.bundle/DepthCompanionSetup](MACHOS/DepthCompanionSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthBridgeSetupPlugin.bundle/HealthBridgeSetupPlugin](MACHOS/HealthBridgeSetupPlugin)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthFeaturesBridgeSetupPlugin.bundle/HealthFeaturesBridgeSetupPlugin](MACHOS/HealthFeaturesBridgeSetupPlugin)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HeartRateBridgePlugin.bundle/HeartRateBridgePlugin](MACHOS/HeartRateBridgePlugin)
- [/System/Library/NanoPreferenceBundles/SetupBundles/MessagesPairingRegistration.bundle/MessagesPairingRegistration](MACHOS/MessagesPairingRegistration)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoContactsBridgeSetup.bundle/NanoContactsBridgeSetup](MACHOS/NanoContactsBridgeSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoPhotosBridgeSetup.bundle/NanoPhotosBridgeSetup](MACHOS/NanoPhotosBridgeSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/RespiratoryHealthSetupPlugin.bundle/RespiratoryHealthSetupPlugin](MACHOS/RespiratoryHealthSetupPlugin)
- [/System/Library/NanoPreferenceBundles/SetupBundles/SchoolTimeSetup.bundle/SchoolTimeSetup](MACHOS/SchoolTimeSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/SiriWatchPairingSetup.bundle/SiriWatchPairingSetup](MACHOS/SiriWatchPairingSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/TextSettingsBridgeSetup.bundle/TextSettingsBridgeSetup](MACHOS/TextSettingsBridgeSetup)
- [/System/Library/NanoPreferenceBundles/SetupBundles/WGAEltonPhoneBuddyFlowPanel.bundle/WGAEltonPhoneBuddyFlowPanel](MACHOS/WGAEltonPhoneBuddyFlowPanel)
- [/System/Library/NanoTimeKit/ComplicationBundles/ActivityComplicationBundleCompanion.bundle/ActivityComplicationBundleCompanion](MACHOS/ActivityComplicationBundleCompanion)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion)
- [/System/Library/NanoTimeKit/ComplicationBundles/DoseComplicationsCompanion.bundle/DoseComplicationsCompanion](MACHOS/DoseComplicationsCompanion)
- [/System/Library/NanoTimeKit/ComplicationBundles/HearingDevicesComplicationContainerCompanion.bundle/HearingDevicesComplicationContainerCompanion](MACHOS/HearingDevicesComplicationContainerCompanion)
- [/System/Library/NanoTimeKit/ComplicationBundles/MindComplicationBundleCompanion.bundle/MindComplicationBundleCompanion](MACHOS/MindComplicationBundleCompanion)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKCellularConnectivityCompanionComplicationBundle.bundle/NTKCellularConnectivityCompanionComplicationBundle](MACHOS/NTKCellularConnectivityCompanionComplicationBundle)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKTimelyComplications.bundle/NTKTimelyComplications](MACHOS/NTKTimelyComplications)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKTimerComplicationBundle.bundle/NTKTimerComplicationBundle](MACHOS/NTKTimerComplicationBundle)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCalendarComplicationsCompanion.bundle/NanoCalendarComplicationsCompanion](MACHOS/NanoCalendarComplicationsCompanion)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCameraComplication.bundle/NanoCameraComplication](MACHOS/NanoCameraComplication)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoMapsComplications.bundle/NanoMapsComplications](MACHOS/NanoMapsComplications)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoRemindersComplication.bundle/NanoRemindersComplication](MACHOS/NanoRemindersComplication)
- [/System/Library/NanoTimeKit/ComplicationBundles/VoiceMemosComplication.bundle/VoiceMemosComplication](MACHOS/VoiceMemosComplication)
- [/System/Library/NanoTimeKit/ComplicationBundles/WorkoutComplicationBundleCompanion.bundle/WorkoutComplicationBundleCompanion](MACHOS/WorkoutComplicationBundleCompanion)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.finddevices.complications.bundle/com.apple.finddevices.complications](MACHOS/com.apple.finddevices.complications)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.finditems.complications.bundle/com.apple.finditems.complications](MACHOS/com.apple.finditems.complications)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.findpeople.complications.bundle/com.apple.findpeople.complications](MACHOS/com.apple.findpeople.complications)
- [/System/Library/NanoTimeKit/FaceBundles/NTKActivityFaceBundleCompanion.bundle/NTKActivityFaceBundleCompanion](MACHOS/NTKActivityFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAkitaFaceBundleCompanion.bundle/NTKAkitaFaceBundleCompanion](MACHOS/NTKAkitaFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAlaskanFaceBundleCompanion.bundle/NTKAlaskanFaceBundleCompanion](MACHOS/NTKAlaskanFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBigNumeralsAnalogFaceBundleCompanion.bundle/NTKBigNumeralsAnalogFaceBundleCompanion](MACHOS/NTKBigNumeralsAnalogFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBigNumeralsDigitalFaceBundleCompanion.bundle/NTKBigNumeralsDigitalFaceBundleCompanion](MACHOS/NTKBigNumeralsDigitalFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBreatheFaceBundle.bundle/NTKBreatheFaceBundle](MACHOS/NTKBreatheFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCaliforniaFaceBundleCompanion.bundle/NTKCaliforniaFaceBundleCompanion](MACHOS/NTKCaliforniaFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCharacterFaceBundleCompanion.bundle/NTKCharacterFaceBundleCompanion](MACHOS/NTKCharacterFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKChronographFaceBundleCompanion.bundle/NTKChronographFaceBundleCompanion](MACHOS/NTKChronographFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCloudrakerFaceBundleCompanion.bundle/NTKCloudrakerFaceBundleCompanion](MACHOS/NTKCloudrakerFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCollieFaceBundleCompanion.bundle/NTKCollieFaceBundleCompanion](MACHOS/NTKCollieFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColorAnalogFaceBundleCompanion.bundle/NTKColorAnalogFaceBundleCompanion](MACHOS/NTKColorAnalogFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColtanFaceBundleCompanion.bundle/NTKColtanFaceBundleCompanion](MACHOS/NTKColtanFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCrosswindFaceBundleCompanion.bundle/NTKCrosswindFaceBundleCompanion](MACHOS/NTKCrosswindFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKDigitalModularFaceBundleCompanion.bundle/NTKDigitalModularFaceBundleCompanion](MACHOS/NTKDigitalModularFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExplorerFaceBundleCompanion.bundle/NTKExplorerFaceBundleCompanion](MACHOS/NTKExplorerFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExtraLargeFaceBundleCompanion.bundle/NTKExtraLargeFaceBundleCompanion](MACHOS/NTKExtraLargeFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFireWaterFaceBundle.bundle/NTKFireWaterFaceBundle](MACHOS/NTKFireWaterFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGladiusFaceBundleCompanion.bundle/NTKGladiusFaceBundleCompanion](MACHOS/NTKGladiusFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGlobetrotterFaceBundleCompanion.bundle/NTKGlobetrotterFaceBundleCompanion](MACHOS/NTKGlobetrotterFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGreyhoundFaceBundleCompanion.bundle/NTKGreyhoundFaceBundleCompanion](MACHOS/NTKGreyhoundFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographFaceBundle.bundle/NTKInfographFaceBundle](MACHOS/NTKInfographFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographModularFaceBundle.bundle/NTKInfographModularFaceBundle](MACHOS/NTKInfographModularFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKKuiperFaceBundleCompanion.bundle/NTKKuiperFaceBundleCompanion](MACHOS/NTKKuiperFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKLilypadFaceBundleCompanion.bundle/NTKLilypadFaceBundleCompanion](MACHOS/NTKLilypadFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKLiquidMetalFaceBundle.bundle/NTKLiquidMetalFaceBundle](MACHOS/NTKLiquidMetalFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMagmaFaceBundleCompanion.bundle/NTKMagmaFaceBundleCompanion](MACHOS/NTKMagmaFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMargaritaFaceBundleCompanion.bundle/NTKMargaritaFaceBundleCompanion](MACHOS/NTKMargaritaFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMotionFaceBundle.bundle/NTKMotionFaceBundle](MACHOS/NTKMotionFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKNumeralsAnalogFaceBundleCompanion.bundle/NTKNumeralsAnalogFaceBundleCompanion](MACHOS/NTKNumeralsAnalogFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKOlympusFaceBundleCompanion.bundle/NTKOlympusFaceBundleCompanion](MACHOS/NTKOlympusFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParameciumFaceBundleCompanion.bundle/NTKParameciumFaceBundleCompanion](MACHOS/NTKParameciumFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPlumeriaFaceBundleCompanion.bundle/NTKPlumeriaFaceBundleCompanion](MACHOS/NTKPlumeriaFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPrideWeaveFaceBundleCompanion.bundle/NTKPrideWeaveFaceBundleCompanion](MACHOS/NTKPrideWeaveFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKProteusFaceBundleCompanion.bundle/NTKProteusFaceBundleCompanion](MACHOS/NTKProteusFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRenegadeFaceBundleCompanion.bundle/NTKRenegadeFaceBundleCompanion](MACHOS/NTKRenegadeFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSeltzerFaceBundleCompanion.bundle/NTKSeltzerFaceBundleCompanion](MACHOS/NTKSeltzerFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKShibaFaceBundleCompanion.bundle/NTKShibaFaceBundleCompanion](MACHOS/NTKShibaFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSimpleFaceBundleCompanion.bundle/NTKSimpleFaceBundleCompanion](MACHOS/NTKSimpleFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSolarsFaceBundleCompanion.bundle/NTKSolarsFaceBundleCompanion](MACHOS/NTKSolarsFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSpectrumFaceBundleCompanion.bundle/NTKSpectrumFaceBundleCompanion](MACHOS/NTKSpectrumFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKTimelapseFaceBundle.bundle/NTKTimelapseFaceBundle](MACHOS/NTKTimelapseFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKToyStoryFaceBundle.bundle/NTKToyStoryFaceBundle](MACHOS/NTKToyStoryFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUltraCubeFaceBundleCompanion.bundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUtilityFaceBundleCompanion.bundle/NTKUtilityFaceBundleCompanion](MACHOS/NTKUtilityFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVaporFaceBundle.bundle/NTKVaporFaceBundle](MACHOS/NTKVaporFaceBundle)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVictoryAnalogFaceBundleCompanion.bundle/NTKVictoryAnalogFaceBundleCompanion](MACHOS/NTKVictoryAnalogFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVictoryDigitalFaceBundleCompanion.bundle/NTKVictoryDigitalFaceBundleCompanion](MACHOS/NTKVictoryDigitalFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings)
- [/System/Library/PreferenceBundles/AccessoryDeveloperSettings.bundle/AccessoryDeveloperSettings](MACHOS/AccessoryDeveloperSettings)
- [/System/Library/PreferenceBundles/AccountSettings/ActiveSyncSettings.bundle/ActiveSyncSettings](MACHOS/ActiveSyncSettings)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings)
- [/System/Library/PreferenceBundles/AccountSettings/CloudKitSettings.bundle/CloudKitSettings](MACHOS/CloudKitSettings)
- [/System/Library/PreferenceBundles/AccountSettings/DAVSettings.bundle/DAVSettings](MACHOS/DAVSettings)
- [/System/Library/PreferenceBundles/AccountSettings/LDAPSettings.bundle/LDAPSettings](MACHOS/LDAPSettings)
- [/System/Library/PreferenceBundles/AccountSettings/MailAccountSettings.bundle/MailAccountSettings](MACHOS/MailAccountSettings)
- [/System/Library/PreferenceBundles/AccountSettings/RemoteManagementAccountSettings.bundle/RemoteManagementAccountSettings](MACHOS/RemoteManagementAccountSettings)
- [/System/Library/PreferenceBundles/AccountSettings/SubscribedCalendarSettings.bundle/SubscribedCalendarSettings](MACHOS/SubscribedCalendarSettings)
- [/System/Library/PreferenceBundles/AccountSettings/icloudCalendarSettings.bundle/icloudCalendarSettings](MACHOS/icloudCalendarSettings)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings)
- [/System/Library/PreferenceBundles/AccountSettingsUI.bundle/AccountSettingsUI](MACHOS/AccountSettingsUI)
- [/System/Library/PreferenceBundles/ActionButtonSettings.bundle/ActionButtonSettings](MACHOS/ActionButtonSettings)
- [/System/Library/PreferenceBundles/ActivitySettings.bundle/ActivitySettings](MACHOS/ActivitySettings)
- [/System/Library/PreferenceBundles/AmbientSettings.bundle/AmbientSettings](MACHOS/AmbientSettings)
- [/System/Library/PreferenceBundles/AppClipDeveloperSettings.bundle/AppClipDeveloperSettings](MACHOS/AppClipDeveloperSettings)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings)
- [/System/Library/PreferenceBundles/AppleEthernetSettingsPreferences.bundle/AppleEthernetSettingsPreferences](MACHOS/AppleEthernetSettingsPreferences)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI)
- [/System/Library/PreferenceBundles/BlocklistSettings.bundle/BlocklistSettings](MACHOS/BlocklistSettings)
- [/System/Library/PreferenceBundles/CallDirectorySettings.bundle/CallDirectorySettings](MACHOS/CallDirectorySettings)
- [/System/Library/PreferenceBundles/CallForwardingTelephonySettings.bundle/CallForwardingTelephonySettings](MACHOS/CallForwardingTelephonySettings)
- [/System/Library/PreferenceBundles/CallScreeningSettingsBundle.bundle/CallScreeningSettingsBundle](MACHOS/CallScreeningSettingsBundle)
- [/System/Library/PreferenceBundles/CallWaitingTelephonySettings.bundle/CallWaitingTelephonySettings](MACHOS/CallWaitingTelephonySettings)
- [/System/Library/PreferenceBundles/CallingLineIdRestrictionTelephonySettings.bundle/CallingLineIdRestrictionTelephonySettings](MACHOS/CallingLineIdRestrictionTelephonySettings)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings)
- [/System/Library/PreferenceBundles/CellularNetworkTelephonySettings.bundle/CellularNetworkTelephonySettings](MACHOS/CellularNetworkTelephonySettings)
- [/System/Library/PreferenceBundles/ClarityUICameraSettings.bundle/ClarityUICameraSettings](MACHOS/ClarityUICameraSettings)
- [/System/Library/PreferenceBundles/ClarityUIMessagesSettings.bundle/ClarityUIMessagesSettings](MACHOS/ClarityUIMessagesSettings)
- [/System/Library/PreferenceBundles/ClarityUIMusicSettings.bundle/ClarityUIMusicSettings](MACHOS/ClarityUIMusicSettings)
- [/System/Library/PreferenceBundles/ClarityUIPhoneFaceTimeSettings.bundle/ClarityUIPhoneFaceTimeSettings](MACHOS/ClarityUIPhoneFaceTimeSettings)
- [/System/Library/PreferenceBundles/ClarityUIPhotosSettings.bundle/ClarityUIPhotosSettings](MACHOS/ClarityUIPhotosSettings)
- [/System/Library/PreferenceBundles/ClassKitDeveloperSettings.bundle/ClassKitDeveloperSettings](MACHOS/ClassKitDeveloperSettings)
- [/System/Library/PreferenceBundles/ClassKitSettings.bundle/ClassKitSettings](MACHOS/ClassKitSettings)
- [/System/Library/PreferenceBundles/ClassificationAndReportingSettingsBundle.bundle/ClassificationAndReportingSettingsBundle](MACHOS/ClassificationAndReportingSettingsBundle)
- [/System/Library/PreferenceBundles/CommunicationSafetySettings.bundle/CommunicationSafetySettings](MACHOS/CommunicationSafetySettings)
- [/System/Library/PreferenceBundles/CompassSettings.bundle/CompassSettings](MACHOS/CompassSettings)
- [/System/Library/PreferenceBundles/ConferenceExternalSettings.bundle/ConferenceExternalSettings](MACHOS/ConferenceExternalSettings)
- [/System/Library/PreferenceBundles/ConferenceRegistrationSettings.bundle/ConferenceRegistrationSettings](MACHOS/ConferenceRegistrationSettings)
- [/System/Library/PreferenceBundles/ControlCenterSettings.bundle/ControlCenterSettings](MACHOS/ControlCenterSettings)
- [/System/Library/PreferenceBundles/CoreRoutineSettings.bundle/CoreRoutineSettings](MACHOS/CoreRoutineSettings)
- [/System/Library/PreferenceBundles/DeveloperSettings.bundle/DeveloperSettings](MACHOS/DeveloperSettings)
- [/System/Library/PreferenceBundles/DeviceManagementClientDeveloperSettings.bundle/DeviceManagementClientDeveloperSettings](MACHOS/DeviceManagementClientDeveloperSettings)
- [/System/Library/PreferenceBundles/DialAssistTelephonySettings.bundle/DialAssistTelephonySettings](MACHOS/DialAssistTelephonySettings)
- [/System/Library/PreferenceBundles/DictionarySettings.bundle/DictionarySettings](MACHOS/DictionarySettings)
- [/System/Library/PreferenceBundles/DigitalSeparationSettings.bundle/DigitalSeparationSettings](MACHOS/DigitalSeparationSettings)
- [/System/Library/PreferenceBundles/DriverKitSettings.bundle/DriverKitSettings](MACHOS/DriverKitSettings)
- [/System/Library/PreferenceBundles/ENDeveloperSettings.bundle/ENDeveloperSettings](MACHOS/ENDeveloperSettings)
- [/System/Library/PreferenceBundles/EmergencyAlertExtension.bundle/EmergencyAlertExtension](MACHOS/EmergencyAlertExtension)
- [/System/Library/PreferenceBundles/ExposureNotificationSettingsUI.bundle/ExposureNotificationSettingsUI](MACHOS/ExposureNotificationSettingsUI)
- [/System/Library/PreferenceBundles/FitnessSettings.bundle/FitnessSettings](MACHOS/FitnessSettings)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings)
- [/System/Library/PreferenceBundles/FontSettings.bundle/FontSettings](MACHOS/FontSettings)
- [/System/Library/PreferenceBundles/FreeformSettings.bundle/FreeformSettings](MACHOS/FreeformSettings)
- [/System/Library/PreferenceBundles/GameCenterSettings.bundle/GameCenterSettings](MACHOS/GameCenterSettings)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings)
- [/System/Library/PreferenceBundles/HealthRecordsSettings.bundle/HealthRecordsSettings](MACHOS/HealthRecordsSettings)
- [/System/Library/PreferenceBundles/HealthSettings.bundle/HealthSettings](MACHOS/HealthSettings)
- [/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings](MACHOS/HearingSettings)
- [/System/Library/PreferenceBundles/HomeScreenSettings.bundle/HomeScreenSettings](MACHOS/HomeScreenSettings)
- [/System/Library/PreferenceBundles/HomeSettings.bundle/HomeSettings](MACHOS/HomeSettings)
- [/System/Library/PreferenceBundles/ICBSettingsBundle.bundle/ICBSettingsBundle](MACHOS/ICBSettingsBundle)
- [/System/Library/PreferenceBundles/ICSSettingsBundle.bundle/ICSSettingsBundle](MACHOS/ICSSettingsBundle)
- [/System/Library/PreferenceBundles/IDSExternalSettings.bundle/IDSExternalSettings](MACHOS/IDSExternalSettings)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings)
- [/System/Library/PreferenceBundles/MadridExternalSettings.bundle/MadridExternalSettings](MACHOS/MadridExternalSettings)
- [/System/Library/PreferenceBundles/ManagedConfigurationUI.bundle/ManagedConfigurationUI](MACHOS/ManagedConfigurationUI)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings)
- [/System/Library/PreferenceBundles/MeasureSettings.bundle/MeasureSettings](MACHOS/MeasureSettings)
- [/System/Library/PreferenceBundles/MessagesNotificationFiltering.bundle/MessagesNotificationFiltering](MACHOS/MessagesNotificationFiltering)
- [/System/Library/PreferenceBundles/MobileMailSettings.bundle/MobileMailSettings](MACHOS/MobileMailSettings)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings)
- [/System/Library/PreferenceBundles/MobileSlideShowSettings.bundle/MobileSlideShowSettings](MACHOS/MobileSlideShowSettings)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings)
- [/System/Library/PreferenceBundles/MusicSettings.bundle/MusicSettings](MACHOS/MusicSettings)
- [/System/Library/PreferenceBundles/NameAndPhotoSettingsBundle.bundle/NameAndPhotoSettingsBundle](MACHOS/NameAndPhotoSettingsBundle)
- [/System/Library/PreferenceBundles/NewsSettings.bundle/NewsSettings](MACHOS/NewsSettings)
- [/System/Library/PreferenceBundles/NotesSettings.bundle/NotesSettings](MACHOS/NotesSettings)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings)
- [/System/Library/PreferenceBundles/PassbookSettings.bundle/PassbookSettings](MACHOS/PassbookSettings)
- [/System/Library/PreferenceBundles/PhonebookTelephonySettings.bundle/PhonebookTelephonySettings](MACHOS/PhonebookTelephonySettings)
- [/System/Library/PreferenceBundles/PhotosCustomNotifications.bundle/PhotosCustomNotifications](MACHOS/PhotosCustomNotifications)
- [/System/Library/PreferenceBundles/PictureInPictureSettings.bundle/PictureInPictureSettings](MACHOS/PictureInPictureSettings)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin)
- [/System/Library/PreferenceBundles/PrimaryCloudCallingSettingsBundle.bundle/PrimaryCloudCallingSettingsBundle](MACHOS/PrimaryCloudCallingSettingsBundle)
- [/System/Library/PreferenceBundles/Privacy/ClipServicesSettings.bundle/ClipServicesSettings](MACHOS/ClipServicesSettings)
- [/System/Library/PreferenceBundles/Privacy/HealthPrivacySettings.bundle/HealthPrivacySettings](MACHOS/HealthPrivacySettings)
- [/System/Library/PreferenceBundles/Privacy/SensorKitPrivacySettings.bundle/SensorKitPrivacySettings](MACHOS/SensorKitPrivacySettings)
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings)
- [/System/Library/PreferenceBundles/ReplyWithMessageSettings.bundle/ReplyWithMessageSettings](MACHOS/ReplyWithMessageSettings)
- [/System/Library/PreferenceBundles/SIMApplicationsTelephonySettings.bundle/SIMApplicationsTelephonySettings](MACHOS/SIMApplicationsTelephonySettings)
- [/System/Library/PreferenceBundles/SIMPasscodeTelephonySettings.bundle/SIMPasscodeTelephonySettings](MACHOS/SIMPasscodeTelephonySettings)
- [/System/Library/PreferenceBundles/SIMSettings.bundle/SIMSettings](MACHOS/SIMSettings)
- [/System/Library/PreferenceBundles/SMSPreferences.bundle/SMSPreferences](MACHOS/SMSPreferences)
- [/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings](MACHOS/SOSSettings)
- [/System/Library/PreferenceBundles/SecondaryCloudCallingSettingsBundle.bundle/SecondaryCloudCallingSettingsBundle](MACHOS/SecondaryCloudCallingSettingsBundle)
- [/System/Library/PreferenceBundles/SecuritySettings.bundle/SecuritySettings](MACHOS/SecuritySettings)
- [/System/Library/PreferenceBundles/SharePlaySettings.bundle/SharePlaySettings](MACHOS/SharePlaySettings)
- [/System/Library/PreferenceBundles/ShortcutsSettings.bundle/ShortcutsSettings](MACHOS/ShortcutsSettings)
- [/System/Library/PreferenceBundles/SilenceCallsSettingBundle.bundle/SilenceCallsSettingBundle](MACHOS/SilenceCallsSettingBundle)
- [/System/Library/PreferenceBundles/SiriMessagesSettings.bundle/SiriMessagesSettings](MACHOS/SiriMessagesSettings)
- [/System/Library/PreferenceBundles/StocksSettings.bundle/StocksSettings](MACHOS/StocksSettings)
- [/System/Library/PreferenceBundles/StoragePlugins/HealthStoragePlugin.bundle/HealthStoragePlugin](MACHOS/HealthStoragePlugin)
- [/System/Library/PreferenceBundles/StoragePlugins/PhotosStorageManagementSettings.bundle/PhotosStorageManagementSettings](MACHOS/PhotosStorageManagementSettings)
- [/System/Library/PreferenceBundles/StoragePlugins/PodcastsUsagePlugin.bundle/PodcastsUsagePlugin](MACHOS/PodcastsUsagePlugin)
- [/System/Library/PreferenceBundles/StoragePlugins/UsagePlugin.bundle/UsagePlugin](MACHOS/UsagePlugin)
- [/System/Library/PreferenceBundles/StorageSettings.bundle/StorageSettings](MACHOS/StorageSettings)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI)
- [/System/Library/PreferenceBundles/TVSettings.bundle/TVSettings](MACHOS/TVSettings)
- [/System/Library/PreferenceBundles/UsageSettings.bundle/UsageSettings](MACHOS/UsageSettings)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountDeveloperSettings.bundle/VideoSubscriberAccountDeveloperSettings](MACHOS/VideoSubscriberAccountDeveloperSettings)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountSettings.bundle/VideoSubscriberAccountSettings](MACHOS/VideoSubscriberAccountSettings)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountTVAppDeveloperSettings.bundle/VideoSubscriberAccountTVAppDeveloperSettings](MACHOS/VideoSubscriberAccountTVAppDeveloperSettings)
- [/System/Library/PreferenceBundles/VoiceMemosSettings.bundle/VoiceMemosSettings](MACHOS/VoiceMemosSettings)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings)
- [/System/Library/PreferenceBundles/WeatherSettings.bundle/WeatherSettings](MACHOS/WeatherSettings)
- [/System/Library/PreferenceBundles/WiFiCallingTelephonySettings.bundle/WiFiCallingTelephonySettings](MACHOS/WiFiCallingTelephonySettings)
- [/System/Library/PreferenceBundles/WiFiSettings.bundle/WiFiSettings](MACHOS/WiFiSettings)
- [/System/Library/PreferenceBundles/iBooksSettings.bundle/iBooksSettings](MACHOS/iBooksSettings)
- [/System/Library/PreferenceManifestsInternal/PreferencesManifests.bundle/PreferencesManifests](MACHOS/PreferencesManifests)
- [/System/Library/PreferencesSyncBundles/FindMyDevicePreferencesSync.bundle/FindMyDevicePreferencesSync](MACHOS/FindMyDevicePreferencesSync)
- [/System/Library/PreferencesSyncBundles/NanoClockBridgeSettingsPreferencesSyncCompanion.bundle/NanoClockBridgeSettingsPreferencesSyncCompanion](MACHOS/NanoClockBridgeSettingsPreferencesSyncCompanion)
- [/System/Library/PreferencesSyncBundles/NanoPhonePreferencesSyncCompanion.bundle/NanoPhonePreferencesSyncCompanion](MACHOS/NanoPhonePreferencesSyncCompanion)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper)
- [/System/Library/PrivateFrameworks/AGXCompilerConnection-S2A8.framework/XPCServices/AGXCompilerService-S2A8.xpc/AGXCompilerService-S2A8](MACHOS/AGXCompilerService-S2A8)
- [/System/Library/PrivateFrameworks/AGXCompilerCore-S2A8.framework/PlugIns/AGXCompilerCrashLogs-S2A8.appex/AGXCompilerCrashLogs-S2A8](MACHOS/AGXCompilerCrashLogs-S2A8)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService)
- [/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/com.apple.AVConference.Diagnostic](MACHOS/com.apple.AVConference.Diagnostic)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd](MACHOS/axassetsd)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/XPCServices/AXMediaUtilitiesService.xpc/AXMediaUtilitiesService](MACHOS/AXMediaUtilitiesService)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAuditCategories.bundle/AccessibilityAuditCategories](MACHOS/AccessibilityAuditCategories)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/Support/axauditd](MACHOS/axauditd)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/Support/axremoted](MACHOS/axremoted)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd](MACHOS/motiontrackingd)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/AXSettingsShortcuts.appex/AXSettingsShortcuts](MACHOS/AXSettingsShortcuts)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/com.apple.accessibility.Accessibility.HearingAidsTapToRadar.appex/com.apple.accessibility.Accessibility.HearingAidsTapToRadar](MACHOS/com.apple.accessibility.Accessibility.HearingAidsTapToRadar)
- [/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/XPCServices/ACCBluetoothPairingService.xpc/ACCBluetoothPairingService](MACHOS/ACCBluetoothPairingService)
- [/System/Library/PrivateFrameworks/AccountNotification.framework/and](MACHOS/and)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/XPCServices/com.apple.accounts.dom.xpc/com.apple.accounts.dom](MACHOS/com.apple.accounts.dom)
- [/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler](MACHOS/BundledIntentHandler)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/activityawardsd](MACHOS/activityawardsd)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd](MACHOS/activitysharingd)
- [/System/Library/PrivateFrameworks/AdminLite.framework/Resources/AdminLiteTool](MACHOS/AdminLiteTool)
- [/System/Library/PrivateFrameworks/AfibBurden.framework/PlugIns/AfibBurdenDiagnosticExtension.appex/AfibBurdenDiagnosticExtension](MACHOS/AfibBurdenDiagnosticExtension)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/addaily](MACHOS/addaily)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/aggregated](MACHOS/aggregated)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/PlugIns/InfographPoster.appex/InfographPoster](MACHOS/InfographPoster)
- [/System/Library/PrivateFrameworks/AnnounceSiriExtensions.framework/PlugIns/AnnounceIntentExtension.appex/AnnounceIntentExtension](MACHOS/AnnounceIntentExtension)
- [/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd](MACHOS/appconduitd)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/XPCServices/AppPredictionIntentsHelperService.xpc/AppPredictionIntentsHelperService](MACHOS/AppPredictionIntentsHelperService)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon)
- [/System/Library/PrivateFrameworks/AppSSOKerberos.framework/PlugIns/KerberosExtension.appex/KerberosExtension](MACHOS/KerberosExtension)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/ASDAskPermissionExtension](MACHOS/ASDAskPermissionExtension)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDFollowUpExtension.appex/ASDFollowUpExtension](MACHOS/ASDFollowUpExtension)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDUserNotificationExtension.appex/ASDUserNotificationExtension](MACHOS/ASDUserNotificationExtension)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/AppStoreEventServiceExtension.appex/AppStoreEventServiceExtension](MACHOS/AppStoreEventServiceExtension)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/PlugIns/AppStoreOverlaysService.appex/AppStoreOverlaysService](MACHOS/AppStoreOverlaysService)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension](MACHOS/AAUIFollowUpExtension)
- [/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon](MACHOS/AppleCredentialManagerDaemon)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/AMDEngagementExtension.appex/AMDEngagementExtension](MACHOS/AMDEngagementExtension)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLAppEmbedding.appex/ASLAppEmbedding](MACHOS/ASLAppEmbedding)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLArcadeRanking.appex/ASLArcadeRanking](MACHOS/ASLArcadeRanking)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLArcadeRetention.appex/ASLArcadeRetention](MACHOS/ASLArcadeRetention)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLExperimental.appex/ASLExperimental](MACHOS/ASLExperimental)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/AppStoreEvalLighthousePlugin.appex/AppStoreEvalLighthousePlugin](MACHOS/AppStoreEvalLighthousePlugin)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/CSLAppStore.appex/CSLAppStore](MACHOS/CSLAppStore)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/CSLAppStore2.appex/CSLAppStore2](MACHOS/CSLAppStore2)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/PlugIns/AMSFollowUpExtension.appex/AMSFollowUpExtension](MACHOS/AMSFollowUpExtension)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementNotificationsExtension.appex/AMSEngagementNotificationsExtension](MACHOS/AMSEngagementNotificationsExtension)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementViewExtension.appex/AMSEngagementViewExtension](MACHOS/AMSEngagementViewExtension)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSProductPageExtension.appex/AMSProductPageExtension](MACHOS/AMSProductPageExtension)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService](MACHOS/ANECompilerService)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer](MACHOS/ANEStorageMaintainer)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/XPCServices/AssetCacheLocatorService.xpc/AssetCacheLocatorService](MACHOS/AssetCacheLocatorService)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail](MACHOS/ASVAssetThumbnail)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetViewer.appex/ASVAssetViewer](MACHOS/ASVAssetViewer)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/PlugIns/SiriDE.appex/SiriDE](MACHOS/SiriDE)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/DeepSyncVerification.xpc/DeepSyncVerification](MACHOS/DeepSyncVerification)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/OpportuneSpeakingModelService.xpc/OpportuneSpeakingModelService](MACHOS/OpportuneSpeakingModelService)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/com.apple.siri.acousticsignature.xpc/com.apple.siri.acousticsignature](MACHOS/com.apple.siri.acousticsignature)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/com.apple.siri.analyzer.xpc/com.apple.siri.analyzer](MACHOS/com.apple.siri.analyzer)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service](MACHOS/assistant_service)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd)
- [/System/Library/PrivateFrameworks/AuthKit.framework/PlugIns/AKDiagnosticExtension.appex/AKDiagnosticExtension](MACHOS/AKDiagnosticExtension)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension](MACHOS/AKFollowUpExtension)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKLocationSignInAlert.appex/AKLocationSignInAlert](MACHOS/AKLocationSignInAlert)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKSecondFactorAlert.appex/AKSecondFactorAlert](MACHOS/AKSecondFactorAlert)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKSecondFactorEntryAlert.appex/AKSecondFactorEntryAlert](MACHOS/AKSecondFactorEntryAlert)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationModeUI.app/AutomationModeUI](MACHOS/AutomationModeUI)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/automationmode-writer](MACHOS/automationmode-writer)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/Support/avatarsd](MACHOS/avatarsd)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/XPCServices/MemojiImageRenderService.xpc/MemojiImageRenderService](MACHOS/MemojiImageRenderService)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/XPCServices/DisplayArchiveService.xpc/DisplayArchiveService](MACHOS/DisplayArchiveService)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/PlugIns/BacklightDiagnostics.appex/BacklightDiagnostics](MACHOS/BacklightDiagnostics)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/PlugIns/com.apple.BarcodeSupport.BarcodeNotificationExtension.appex/com.apple.BarcodeSupport.BarcodeNotificationExtension](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationExtension)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/PlugIns/com.apple.BarcodeSupport.BarcodeNotificationExtension2.appex/com.apple.BarcodeSupport.BarcodeNotificationExtension2](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationExtension2)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/XPCServices/com.apple.BarcodeSupport.Helper.xpc/com.apple.BarcodeSupport.Helper](MACHOS/com.apple.BarcodeSupport.Helper)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/XPCServices/com.apple.BarcodeSupport.ParsingService.xpc/com.apple.BarcodeSupport.ParsingService](MACHOS/com.apple.BarcodeSupport.ParsingService)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/com.apple.BarcodeSupport.BarcodeNotificationService](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationService)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/XPCServices/BiomeWriteService.xpc/BiomeWriteService](MACHOS/BiomeWriteService)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/PlugIns/BiomeLighthousePlugin.appex/BiomeLighthousePlugin](MACHOS/BiomeLighthousePlugin)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed](MACHOS/biomed)
- [/System/Library/PrivateFrameworks/BiometricKit.framework/PlugIns/BioLogDiagnostic.appex/BioLogDiagnostic](MACHOS/BioLogDiagnostic)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored)
- [/System/Library/PrivateFrameworks/BookLibrary.framework/PlugIns/BooksDiagnosticExtension.appex/BooksDiagnosticExtension](MACHOS/BooksDiagnosticExtension)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/PlugIns/BooksAskPermissionExtension.appex/BooksAskPermissionExtension](MACHOS/BooksAskPermissionExtension)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd](MACHOS/bookassetd)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/XPCServices/BrailleTranslationService.xpc/BrailleTranslationService](MACHOS/BrailleTranslationService)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV)
- [/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension](MACHOS/CMCaptureDiagnosticExtension)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/Support/calaccessd](MACHOS/calaccessd)
- [/System/Library/PrivateFrameworks/CalendarNotification.framework/PlugIns/CalendarNotificationContentExtension.appex/CalendarNotificationContentExtension](MACHOS/CalendarNotificationContentExtension)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/PlugIns/IntentsExtension.appex/IntentsExtension](MACHOS/IntentsExtension)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper)
- [/System/Library/PrivateFrameworks/CameraUI.framework/Support/nebulad](MACHOS/nebulad)
- [/System/Library/PrivateFrameworks/CarKit.framework/PlugIns/CarPlayDiagnostics.appex/CarPlayDiagnostics](MACHOS/CarPlayDiagnostics)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService](MACHOS/SetStoreUpdateService)
- [/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService](MACHOS/CategoriesService)
- [/System/Library/PrivateFrameworks/CertUI.framework/certui_relay](MACHOS/certui_relay)
- [/System/Library/PrivateFrameworks/ChatKit.framework/companionmessagesd](MACHOS/companionmessagesd)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod](MACHOS/chronod)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/PlugIns/PrivacyDisclosure.appex/PrivacyDisclosure](MACHOS/PrivacyDisclosure)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Extensions/EasyMAIDSignInPicker.appex/EasyMAIDSignInPicker](MACHOS/EasyMAIDSignInPicker)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/BooksService.xpc/BooksService](MACHOS/BooksService)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/ScreenshotService.xpc/ScreenshotService](MACHOS/ScreenshotService)
- [/System/Library/PrivateFrameworks/ClipServices.framework/clipserviced](MACHOS/clipserviced)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/PlugIns/ClockPosterExtension.appex/ClockPosterExtension](MACHOS/ClockPosterExtension)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProvider.appex/com.apple.CloudDocs.MobileDocumentsFileProvider](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProvider)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.appex/com.apple.CloudDocs.MobileDocumentsFileProviderManaged](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderManaged)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderUI.appex/com.apple.CloudDocs.MobileDocumentsFileProviderUI](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderUI)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider](MACHOS/com.apple.CloudDocs.iCloudDriveFileProvider)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged](MACHOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic](MACHOS/CloudDocsDiagnostic)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/bird](MACHOS/bird)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.DocumentPicker.appex/com.apple.CloudDocsUI.DocumentPicker](MACHOS/com.apple.CloudDocsUI.DocumentPicker)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose)
- [/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd](MACHOS/com.apple.sbd)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/Versions/A/XPCServices/com.apple.cloudsettings.gamecontroller.xpc/com.apple.cloudsettings.gamecontroller](MACHOS/com.apple.cloudsettings.gamecontroller)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/XPCServices/com.apple.cloudsettings.international.xpc/com.apple.cloudsettings.international](MACHOS/com.apple.cloudsettings.international)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/XPCServices/com.apple.cloudsettings.keyboard.xpc/com.apple.cloudsettings.keyboard](MACHOS/com.apple.cloudsettings.keyboard)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad](MACHOS/companioncamerad)
- [/System/Library/PrivateFrameworks/CompassUI.framework/XPCServices/CompassCalibration.xpc/CompassCalibration](MACHOS/CompassCalibration)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent](MACHOS/contactsdonationagent)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/XPCServices/ContactsBackgroundColorService.xpc/ContactsBackgroundColorService](MACHOS/ContactsBackgroundColorService)
- [/System/Library/PrivateFrameworks/ContextKit.framework/XPCServices/ContextService.xpc/ContextService](MACHOS/ContextService)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd](MACHOS/assistant_cdmd)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCAppLinksIconService.xpc/ACCAppLinksIconService](MACHOS/ACCAppLinksIconService)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCCarPlayService.xpc/ACCCarPlayService](MACHOS/ACCCarPlayService)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService](MACHOS/ACCHWComponentAuthService)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCFeatureAudioProductService.xpc/ACCFeatureAudioProductService](MACHOS/ACCFeatureAudioProductService)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd)
- [/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/PlugIns/BTDevicePickerUI.appex/BTDevicePickerUI](MACHOS/BTDevicePickerUI)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd](MACHOS/cdpd)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension](MACHOS/CDPFollowUpExtension)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored](MACHOS/contextstored)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech](MACHOS/com.apple.siri.embeddedspeech)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/followupd](MACHOS/followupd)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/PlugIns/FollowUpSampleExtension.appex/FollowUpSampleExtension](MACHOS/FollowUpSampleExtension)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/PlugIns/SearchPoirotExtension.appex/SearchPoirotExtension](MACHOS/SearchPoirotExtension)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/XPCServices/AccessoryDataFetch.xpc/AccessoryDataFetch](MACHOS/AccessoryDataFetch)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd](MACHOS/recentsd)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/XPCServices/CoreRepairCoreXPCService.xpc/CoreRepairCoreXPCService](MACHOS/CoreRepairCoreXPCService)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/PlugIns/RTDiagnosticExtension.appex/RTDiagnosticExtension](MACHOS/RTDiagnosticExtension)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/PlugIns/com.apple.CoreSVG.thumbnail.appex/com.apple.CoreSVG.thumbnail](MACHOS/com.apple.CoreSVG.thumbnail)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/MockAVVCPlugin.bundle/MockAVVCPlugin](MACHOS/MockAVVCPlugin)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/PlugIns/CoreSpeechDiagnosticExtension.appex/CoreSpeechDiagnosticExtension](MACHOS/CoreSpeechDiagnosticExtension)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/CoreSpeechXPC.xpc/CoreSpeechXPC](MACHOS/CoreSpeechXPC)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd](MACHOS/speechmodeltrainingd)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool](MACHOS/suggest_tool)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/reversetemplated](MACHOS/reversetemplated)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd](MACHOS/suggestd)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/coresymbolicationd](MACHOS/coresymbolicationd)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/AccessoryTimeSync.bundle/AccessoryTimeSync](MACHOS/AccessoryTimeSync)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/CellularSource.bundle/CellularSource](MACHOS/CellularSource)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/LinkSource.bundle/LinkSource](MACHOS/LinkSource)
- [/System/Library/PrivateFrameworks/DASDaemon.framework/PlugIns/DuetDiagnosticExtension.appex/DuetDiagnosticExtension](MACHOS/DuetDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DASDelegate.framework/XPCServices/DASDelegateService.xpc/DASDelegateService](MACHOS/DASDelegateService)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub](MACHOS/DTServiceHub)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent](MACHOS/LeakAgent)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/PlugIns/DTODRAssetStatus.bundle/DTODRAssetStatus](MACHOS/DTODRAssetStatus)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/PlugIns/IDEDebugGaugeDataProviders.bundle/IDEDebugGaugeDataProviders](MACHOS/IDEDebugGaugeDataProviders)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/RemoteInjectionAgent](MACHOS/RemoteInjectionAgent)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTConditionInducerSupportService.xpc/com.apple.dt.DTConditionInducerSupportService](MACHOS/com.apple.dt.DTConditionInducerSupportService)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTScreenshotService.xpc/com.apple.dt.DTScreenshotService](MACHOS/com.apple.dt.DTScreenshotService)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity](MACHOS/com.apple.dt.instruments.dtsecurity)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/libRemoteInjectionPayload.dylib](MACHOS/libRemoteInjectionPayload.dylib)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/liboainject.dylib](MACHOS/liboainject.dylib)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DADaemonCardDAV.bundle/DADaemonCardDAV](MACHOS/DADaemonCardDAV)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DAIMAPNotes.framework/DADaemonIMAPNotes.bundle/DADaemonIMAPNotes](MACHOS/DADaemonIMAPNotes)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DADaemonLDAP.bundle/DADaemonLDAP](MACHOS/DADaemonLDAP)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DADaemonSubCal.bundle/DADaemonSubCal](MACHOS/DADaemonSubCal)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Support/dataaccessd](MACHOS/dataaccessd)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/XPCServices/DataDetectorsRemoteScanner.xpc/DataDetectorsRemoteScanner](MACHOS/DataDetectorsRemoteScanner)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/PlugIns/com.apple.DataDetectorsUI.ActionsExtension.appex/com.apple.DataDetectorsUI.ActionsExtension](MACHOS/com.apple.DataDetectorsUI.ActionsExtension)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/XPCServices/com.apple.datadetectors.AddToRecentsService.xpc/com.apple.datadetectors.AddToRecentsService](MACHOS/com.apple.datadetectors.AddToRecentsService)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.datamigrator.xpc/com.apple.datamigrator](MACHOS/com.apple.datamigrator)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper](MACHOS/com.apple.migrationpluginwrapper)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/datamigratorhelper.xpc/datamigratorhelper](MACHOS/datamigratorhelper)
- [/System/Library/PrivateFrameworks/DebugHierarchyFoundation.framework/DebugHierarchyFoundation](MACHOS/DebugHierarchyFoundation)
- [/System/Library/PrivateFrameworks/DebugHierarchyKit.framework/DebugHierarchyKit](MACHOS/DebugHierarchyKit)
- [/System/Library/PrivateFrameworks/DeepThought.framework/PlugIns/DeepThoughtPlugin.appex/DeepThoughtPlugin](MACHOS/DeepThoughtPlugin)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/XPCServices/IngestService.xpc/IngestService](MACHOS/IngestService)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd](MACHOS/devicecheckd)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/BTD2DPlugin.bundle/BTD2DPlugin](MACHOS/BTD2DPlugin)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/WiFiAwareD2DPlugin.bundle/WiFiAwareD2DPlugin](MACHOS/WiFiAwareD2DPlugin)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/WiFiD2DPlugin.bundle/WiFiD2DPlugin](MACHOS/WiFiD2DPlugin)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AudioDiagnosticExtension.appex/AudioDiagnosticExtension](MACHOS/AudioDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothHeadset.appex/BluetoothHeadset](MACHOS/BluetoothHeadset)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension](MACHOS/ContinuousRecordingsDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/HomeEnergyDiagnosticExtension.appex/HomeEnergyDiagnosticExtension](MACHOS/HomeEnergyDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IntelligentRoutingDiagnostic.appex/IntelligentRoutingDiagnostic](MACHOS/IntelligentRoutingDiagnostic)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LocationDiagnosticExtension.appex/LocationDiagnosticExtension](MACHOS/LocationDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/NearbydDiagnosticExtension.appex/NearbydDiagnosticExtension](MACHOS/NearbydDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PICSDiagnosticExtension.appex/PICSDiagnosticExtension](MACHOS/PICSDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PedestrianFenceDiagnostic.appex/PedestrianFenceDiagnostic](MACHOS/PedestrianFenceDiagnostic)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PrecisionFindingDiagnostic.appex/PrecisionFindingDiagnostic](MACHOS/PrecisionFindingDiagnostic)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ShortcutsDiagnosticExtension.appex/ShortcutsDiagnosticExtension](MACHOS/ShortcutsDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/TypologyDiagnosticExtension.appex/TypologyDiagnosticExtension](MACHOS/TypologyDiagnosticExtension)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.B389.appex/com.apple.DiagnosticExtensions.B389](MACHOS/com.apple.DiagnosticExtensions.B389)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.BackgroundAppRefresh.appex/com.apple.DiagnosticExtensions.BackgroundAppRefresh](MACHOS/com.apple.DiagnosticExtensions.BackgroundAppRefresh)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.BluetoothABCDE.appex/com.apple.DiagnosticExtensions.BluetoothABCDE](MACHOS/com.apple.DiagnosticExtensions.BluetoothABCDE)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Contacts.appex/com.apple.DiagnosticExtensions.Contacts](MACHOS/com.apple.DiagnosticExtensions.Contacts)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.CrashLogs.appex/com.apple.DiagnosticExtensions.CrashLogs](MACHOS/com.apple.DiagnosticExtensions.CrashLogs)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.DataAccess.appex/com.apple.DiagnosticExtensions.DataAccess](MACHOS/com.apple.DiagnosticExtensions.DataAccess)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.FaceTime.appex/com.apple.DiagnosticExtensions.FaceTime](MACHOS/com.apple.DiagnosticExtensions.FaceTime)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.HangTracer.appex/com.apple.DiagnosticExtensions.HangTracer](MACHOS/com.apple.DiagnosticExtensions.HangTracer)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Keyboard.appex/com.apple.DiagnosticExtensions.Keyboard](MACHOS/com.apple.DiagnosticExtensions.Keyboard)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.LowMemory.appex/com.apple.DiagnosticExtensions.LowMemory](MACHOS/com.apple.DiagnosticExtensions.LowMemory)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Messages.appex/com.apple.DiagnosticExtensions.Messages](MACHOS/com.apple.DiagnosticExtensions.Messages)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Panic.appex/com.apple.DiagnosticExtensions.Panic](MACHOS/com.apple.DiagnosticExtensions.Panic)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Phone.appex/com.apple.DiagnosticExtensions.Phone](MACHOS/com.apple.DiagnosticExtensions.Phone)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Sandbox.appex/com.apple.DiagnosticExtensions.Sandbox](MACHOS/com.apple.DiagnosticExtensions.Sandbox)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.StackShot.appex/com.apple.DiagnosticExtensions.StackShot](MACHOS/com.apple.DiagnosticExtensions.StackShot)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VPN.appex/com.apple.DiagnosticExtensions.VPN](MACHOS/com.apple.DiagnosticExtensions.VPN)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VisualVoiceMail.appex/com.apple.DiagnosticExtensions.VisualVoiceMail](MACHOS/com.apple.DiagnosticExtensions.VisualVoiceMail)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VoiceMemos.appex/com.apple.DiagnosticExtensions.VoiceMemos](MACHOS/com.apple.DiagnosticExtensions.VoiceMemos)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.WiFi.appex/com.apple.DiagnosticExtensions.WiFi](MACHOS/com.apple.DiagnosticExtensions.WiFi)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.tailspin.appex/com.apple.DiagnosticExtensions.tailspin](MACHOS/com.apple.DiagnosticExtensions.tailspin)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/catutil](MACHOS/catutil)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/XPCServices/com.apple.DictionaryServiceHelper.xpc/com.apple.DictionaryServiceHelper](MACHOS/com.apple.DictionaryServiceHelper)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/PlugIns/DKFollowUpExtension.appex/DKFollowUpExtension](MACHOS/DKFollowUpExtension)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/PlugIns/DiskSpaceDiagnosticsExtension.appex/DiskSpaceDiagnosticsExtension](MACHOS/DiskSpaceDiagnosticsExtension)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService](MACHOS/FilesystemMetadataSnapshotService)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/XPCServices/com.apple.siri-distributed-evaluation.xpc/com.apple.siri-distributed-evaluation](MACHOS/com.apple.siri-distributed-evaluation)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/PlugIns/DoNotDisturbIntents.appex/DoNotDisturbIntents](MACHOS/DoNotDisturbIntents)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd](MACHOS/donotdisturbd)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/PlugIns/DockKitExtension.appex/DockKitExtension](MACHOS/DockKitExtension)
- [/System/Library/PrivateFrameworks/DocumentCamera.framework/PlugIns/com.apple.DocumentCamera.ViewService.appex/com.apple.DocumentCamera.ViewService](MACHOS/com.apple.DocumentCamera.ViewService)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Downloads.xpc/com.apple.DocumentManagerCore.Downloads](MACHOS/com.apple.DocumentManagerCore.Downloads)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename](MACHOS/com.apple.DocumentManagerCore.Rename)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/AddTagsActionExtension.appex/AddTagsActionExtension](MACHOS/AddTagsActionExtension)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocadoIntentHandler.appex/RecentsAvocadoIntentHandler](MACHOS/RecentsAvocadoIntentHandler)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/Support/textunderstandingd](MACHOS/textunderstandingd)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/textunderstandingd](MACHOS/textunderstandingd)
- [/System/Library/PrivateFrameworks/DragUI.framework/Support/druid](MACHOS/druid)
- [/System/Library/PrivateFrameworks/EmailCore.framework/PlugIns/EmailCore.wkbundle/EmailCore](MACHOS/EmailCore)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/Support/devicedataresetd](MACHOS/devicedataresetd)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/XPCServices/DeviceDataResetXPCServiceWorker.xpc/DeviceDataResetXPCServiceWorker](MACHOS/DeviceDataResetXPCServiceWorker)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/PlugIns/EmergencyAlertsUIExtension.appex/EmergencyAlertsUIExtension](MACHOS/EmergencyAlertsUIExtension)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/PlugIns/EmojiPosterExtension.appex/EmojiPosterExtension](MACHOS/EmojiPosterExtension)
- [/System/Library/PrivateFrameworks/EventKitTCCUI.framework/PlugIns/EventKitTCCFullAccessNotificationUIExtension.appex/EventKitTCCFullAccessNotificationUIExtension](MACHOS/EventKitTCCFullAccessNotificationUIExtension)
- [/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/PlugIns/EventMetaDataExtractorPlugin.appex/EventMetaDataExtractorPlugin](MACHOS/EventMetaDataExtractorPlugin)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DADaemonEAS.bundle/DADaemonEAS](MACHOS/DADaemonEAS)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Support/exchangesyncd](MACHOS/exchangesyncd)
- [/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/PlugIns/ActiveSyncOAuthService.appex/ActiveSyncOAuthService](MACHOS/ActiveSyncOAuthService)
- [/System/Library/PrivateFrameworks/EyeRelief.framework/Resources/eyereliefd](MACHOS/eyereliefd)
- [/System/Library/PrivateFrameworks/Eyedropper.framework/Support/eyedropperd](MACHOS/eyedropperd)
- [/System/Library/PrivateFrameworks/FMF.framework/XPCServices/FMFMapXPCService.xpc/FMFMapXPCService](MACHOS/FMFMapXPCService)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored](MACHOS/facetimemessagestored)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/PlugIns/FAFollowupExtension.appex/FAFollowupExtension](MACHOS/FAFollowupExtension)
- [/System/Library/PrivateFrameworks/FamilyNotification.framework/familynotificationd](MACHOS/familynotificationd)
- [/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS](MACHOS/DraftingExtension-iOS)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/AppStoreService.xpc/AppStoreService](MACHOS/AppStoreService)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/FPCKService](MACHOS/FPCKService)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealth_client](MACHOS/finhealth_client)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient)
- [/System/Library/PrivateFrameworks/FinHealth.framework/XPCServices/FinHealthXPCServices.xpc/FinHealthXPCServices](MACHOS/FinHealthXPCServices)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceBTDiscoveryXPCService.xpc/FindMyDeviceBTDiscoveryXPCService](MACHOS/FindMyDeviceBTDiscoveryXPCService)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEmergencyCallInfoPublisherXPCService.xpc/FindMyDeviceEmergencyCallInfoPublisherXPCService](MACHOS/FindMyDeviceEmergencyCallInfoPublisherXPCService)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/FindMyDeviceEraseXPCService](MACHOS/FindMyDeviceEraseXPCService)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService](MACHOS/FindMyDeviceHelperXPCService)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/FindMyDeviceIdentityXPCService](MACHOS/FindMyDeviceIdentityXPCService)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceUserNotificationsXPCService.xpc/FindMyDeviceUserNotificationsXPCService](MACHOS/FindMyDeviceUserNotificationsXPCService)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/fitnesscoachingd](MACHOS/fitnesscoachingd)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/PlugIns/UserNotificationExtension.appex/UserNotificationExtension](MACHOS/UserNotificationExtension)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel)
- [/System/Library/PrivateFrameworks/FontServices.framework/Support/fontservicesd](MACHOS/fontservicesd)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/UserFontManager.xpc/UserFontManager](MACHOS/UserFontManager)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/UserFontServices.xpc/UserFontServices](MACHOS/UserFontServices)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/com.apple.FontServices.FontProviderLoader.xpc/com.apple.FontServices.FontProviderLoader](MACHOS/com.apple.FontServices.FontProviderLoader)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture)
- [/System/Library/PrivateFrameworks/GPUToolsDiagnostics.framework/GPUToolsDiagnostics](MACHOS/GPUToolsDiagnostics)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterAuthenticateExtension.appex/GameCenterAuthenticateExtension](MACHOS/GameCenterAuthenticateExtension)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterChallengeIssueExtension.appex/GameCenterChallengeIssueExtension](MACHOS/GameCenterChallengeIssueExtension)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterDashboardExtension.appex/GameCenterDashboardExtension](MACHOS/GameCenterDashboardExtension)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterTurnBasedMatchmakerExtension.appex/GameCenterTurnBasedMatchmakerExtension](MACHOS/GameCenterTurnBasedMatchmakerExtension)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/XPCServices/GameControllerConfigService.xpc/GameControllerConfigService](MACHOS/GameControllerConfigService)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond](MACHOS/revisiond)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd](MACHOS/geoanalyticsd)
- [/System/Library/PrivateFrameworks/GeoServices.framework/MapsOfflineService.bundle/MapsOfflineService](MACHOS/MapsOfflineService)
- [/System/Library/PrivateFrameworks/GeoServices.framework/XPCServices/com.apple.GeoServices.MapsOfflineServices.xpc/com.apple.GeoServices.MapsOfflineServices](MACHOS/com.apple.GeoServices.MapsOfflineServices)
- [/System/Library/PrivateFrameworks/GeoServices.framework/geod](MACHOS/geod)
- [/System/Library/PrivateFrameworks/GradientPoster.framework/PlugIns/GradientPosterExtension.appex/GradientPosterExtension](MACHOS/GradientPosterExtension)
- [/System/Library/PrivateFrameworks/HAENotifications.framework/PlugIns/HAENotificationContentExtension.appex/HAENotificationContentExtension](MACHOS/HAENotificationContentExtension)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/XPCServices/HRTFEnrollmentService.xpc/HRTFEnrollmentService](MACHOS/HRTFEnrollmentService)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/PlugIns/CycleTrackingDiagnosticExtension.appex/CycleTrackingDiagnosticExtension](MACHOS/CycleTrackingDiagnosticExtension)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/DayStreamProcessorService.xpc/DayStreamProcessorService](MACHOS/DayStreamProcessorService)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/HistoricalAnalyzerService.xpc/HistoricalAnalyzerService](MACHOS/HistoricalAnalyzerService)
- [/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex/HealthFollowUpExtension](MACHOS/HealthFollowUpExtension)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/PlugIns/HealthMedicationsNotificationContentExtension.appex/HealthMedicationsNotificationContentExtension](MACHOS/HealthMedicationsNotificationContentExtension)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesUI.framework/PlugIns/HealthMenstrualCyclesNotificationContentExtension.appex/HealthMenstrualCyclesNotificationContentExtension](MACHOS/HealthMenstrualCyclesNotificationContentExtension)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.legacy-ingestion.xpc/com.apple.health.records.legacy-ingestion](MACHOS/com.apple.health.records.legacy-ingestion)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.xpc/com.apple.health.records](MACHOS/com.apple.health.records)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/healthrecordsd](MACHOS/healthrecordsd)
- [/System/Library/PrivateFrameworks/HearingCore.framework/heard](MACHOS/heard)
- [/System/Library/PrivateFrameworks/HearingMLHelper.framework/XPCServices/HearingMLHelperService.xpc/HearingMLHelperService](MACHOS/HearingMLHelperService)
- [/System/Library/PrivateFrameworks/HeartRhythmAlgorithms.framework/PlugIns/IRNDiagnosticExtension.appex/IRNDiagnosticExtension](MACHOS/IRNDiagnosticExtension)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd](MACHOS/homeenergyd)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed](MACHOS/homed)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iapd](MACHOS/iapd)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iaptransportd](MACHOS/iaptransportd)
- [/System/Library/PrivateFrameworks/IAPAuthentication.framework/Support/iapauthd](MACHOS/iapauthd)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSCredentialsAgent.app/IDSCredentialsAgent](MACHOS/IDSCredentialsAgent)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSRemoteURLConnectionAgent.app/IDSRemoteURLConnectionAgent](MACHOS/IDSRemoteURLConnectionAgent)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent](MACHOS/IMDMessageServicesAgent)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMAutomaticHistoryDeletionAgent.app/IMAutomaticHistoryDeletionAgent](MACHOS/IMAutomaticHistoryDeletionAgent)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent](MACHOS/IMDPersistenceAgent)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent](MACHOS/IMTranscoderAgent)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent](MACHOS/IMTransferAgent)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/PlugIns/WetNotification.appex/WetNotification](MACHOS/WetNotification)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/Resources/IOSADiagnose](MACHOS/IOSADiagnose)
- [/System/Library/PrivateFrameworks/InAppMessages.framework/PlugIns/InAppMessagesWebProcessBundle.bundle/InAppMessagesWebProcessBundle](MACHOS/InAppMessagesWebProcessBundle)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordination_proxy](MACHOS/installcoordination_proxy)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/ERMLRuntimePlugin.appex/ERMLRuntimePlugin](MACHOS/ERMLRuntimePlugin)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/Support/localizationswitcherd](MACHOS/localizationswitcherd)
- [/System/Library/PrivateFrameworks/LighthouseAV.framework/PlugIns/LighthouseAVPlugin.appex/LighthouseAVPlugin](MACHOS/LighthouseAVPlugin)
- [/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/PlugIns/LighthouseBitacoraPlugin.appex/LighthouseBitacoraPlugin](MACHOS/LighthouseBitacoraPlugin)
- [/System/Library/PrivateFrameworks/LighthouseDictation.framework/PlugIns/LighthouseDictationPlugin.appex/LighthouseDictationPlugin](MACHOS/LighthouseDictationPlugin)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/XPCServices/MFAANetwork.xpc/MFAANetwork](MACHOS/MFAANetwork)
- [/System/Library/PrivateFrameworks/MLCompilerServices.framework/XPCServices/MLCompilerOSXPC.xpc/MLCompilerOSXPC](MACHOS/MLCompilerOSXPC)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/PlugIns/MacinTalkAUSP.appex/MacinTalkAUSP](MACHOS/MacinTalkAUSP)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension](MACHOS/ManagedSettingsExtension)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd](MACHOS/destinationd)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/geocorrectiond](MACHOS/geocorrectiond)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd](MACHOS/mapspushd)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/nanomapscd](MACHOS/nanomapscd)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd)
- [/System/Library/PrivateFrameworks/MarkupUI.framework/PlugIns/MarkupPrivateExtension.appex/MarkupPrivateExtension](MACHOS/MarkupPrivateExtension)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService](MACHOS/com.apple.photos.ImageConversionService)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService](MACHOS/com.apple.photos.VideoConversionService)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/XPCServices/mediamlxpc.xpc/mediamlxpc](MACHOS/mediamlxpc)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted)
- [/System/Library/PrivateFrameworks/MediaServices.framework/Support/mediaartworkd](MACHOS/mediaartworkd)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService)
- [/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd](MACHOS/mstreamd)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/XPCServices/MetricMeasurementHelper.xpc/MetricMeasurementHelper](MACHOS/MetricMeasurementHelper)
- [/System/Library/PrivateFrameworks/MetricsKit.framework/XPCServices/AMPIDService.xpc/AMPIDService](MACHOS/AMPIDService)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/auearlyboot](MACHOS/auearlyboot)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleEmbeddedAccessoryUpdaterService.xpc/AppleEmbeddedAccessoryUpdaterService](MACHOS/AppleEmbeddedAccessoryUpdaterService)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleSTDP2700BootstrapService.xpc/AppleSTDP2700BootstrapService](MACHOS/AppleSTDP2700BootstrapService)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/DurianUpdaterService.xpc/DurianUpdaterService](MACHOS/DurianUpdaterService)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/GenericKextUpdaterService.xpc/GenericKextUpdaterService](MACHOS/GenericKextUpdaterService)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/StandaloneHIDAudService.xpc/StandaloneHIDAudService](MACHOS/StandaloneHIDAudService)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceAFU.xpc/UARPUpdaterServiceAFU](MACHOS/UARPUpdaterServiceAFU)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/USBCAccessoryUpdaterService.xpc/USBCAccessoryUpdaterService](MACHOS/USBCAccessoryUpdaterService)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBDiagnosticExtension.appex/MBDiagnosticExtension](MACHOS/MBDiagnosticExtension)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBFollowUpExtension.appex/MBFollowUpExtension](MACHOS/MBFollowUpExtension)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension](MACHOS/MBPrebuddyFollowUpExtension)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService](MACHOS/com.apple.MobileInstallationHelperService)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/PlugIns/MailWebProcessBundle.bundle/MailWebProcessBundle](MACHOS/MailWebProcessBundle)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated](MACHOS/softwareupdated)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd](MACHOS/mobiletimerd)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/PlugIns/MobileTimerIntents.appex/MobileTimerIntents](MACHOS/MobileTimerIntents)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/PlugIns/MobileTimerNotificationExtension.appex/MobileTimerNotificationExtension](MACHOS/MobileTimerNotificationExtension)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterPreferenceProvider.xpc/SessionFilterPreferenceProvider](MACHOS/SessionFilterPreferenceProvider)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterRecordingUpdater.xpc/SessionFilterRecordingUpdater](MACHOS/SessionFilterRecordingUpdater)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd](MACHOS/medialibraryd)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/PlugIns/NLPLearnerQuickTypeLighthousePlugin.appex/NLPLearnerQuickTypeLighthousePlugin](MACHOS/NLPLearnerQuickTypeLighthousePlugin)
- [/System/Library/PrivateFrameworks/NPTKit.framework/PlugIns/NPTCellularDiagnosticsExtension.appex/NPTCellularDiagnosticsExtension](MACHOS/NPTCellularDiagnosticsExtension)
- [/System/Library/PrivateFrameworks/NPTKit.framework/PlugIns/NPTWiFiDiagnosticsExtension.appex/NPTWiFiDiagnosticsExtension](MACHOS/NPTWiFiDiagnosticsExtension)
- [/System/Library/PrivateFrameworks/NanoAppRegistry.framework/Support/nanoappregistryd](MACHOS/nanoappregistryd)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/nanobackupd](MACHOS/nanobackupd)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/companionfindlocallyd](MACHOS/companionfindlocallyd)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/findme](MACHOS/findme)
- [/System/Library/PrivateFrameworks/NanoMusicSync.framework/PlugIns/NanoMediaDiagnosticExtension.appex/NanoMediaDiagnosticExtension](MACHOS/NanoMediaDiagnosticExtension)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent](MACHOS/NPKCompanionAgent)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd](MACHOS/nanoprefsyncd)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/NTKDiagnosticExtensionCompanion.appex/NTKDiagnosticExtensionCompanion](MACHOS/NTKDiagnosticExtensionCompanion)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/com.apple.NanoTimeKit.CreateWatchFace.appex/com.apple.NanoTimeKit.CreateWatchFace](MACHOS/com.apple.NanoTimeKit.CreateWatchFace)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/BundleComplicationMigrationService.xpc/BundleComplicationMigrationService](MACHOS/BundleComplicationMigrationService)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/GreenfieldService-Companion.xpc/GreenfieldService-Companion](MACHOS/GreenfieldService-Companion)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/NTKFaceSnapshotService.xpc/NTKFaceSnapshotService](MACHOS/NTKFaceSnapshotService)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond](MACHOS/nanotimekitcompaniond)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRadioPowerSwitch.xpc/NFRadioPowerSwitch](MACHOS/NFRadioPowerSwitch)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRestoreService.xpc/NFRestoreService](MACHOS/NFRestoreService)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService](MACHOS/NFUIService)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService)
- [/System/Library/PrivateFrameworks/NetworkQualityServices.framework/XPCServices/NetworkQualityXPC.xpc/NetworkQualityXPC](MACHOS/NetworkQualityXPC)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/PlugIns/NRDiagnosticExtension.appex/NRDiagnosticExtension](MACHOS/NRDiagnosticExtension)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/XPCServices/ANFDecoder.xpc/ANFDecoder](MACHOS/ANFDecoder)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd)
- [/System/Library/PrivateFrameworks/NewsServices.framework/PlugIns/NewsArticleViewer.appex/NewsArticleViewer](MACHOS/NewsArticleViewer)
- [/System/Library/PrivateFrameworks/NewsServices.framework/nanonewscd](MACHOS/nanonewscd)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/TodayFeedConfigDecoder.xpc/TodayFeedConfigDecoder](MACHOS/TodayFeedConfigDecoder)
- [/System/Library/PrivateFrameworks/NotesShared.framework/XPCServices/com.apple.mobilenotes.datastore.xpc/com.apple.mobilenotes.datastore](MACHOS/com.apple.mobilenotes.datastore)
- [/System/Library/PrivateFrameworks/NotesUI.framework/XPCServices/com.apple.mobilenotes.HTMLConverter.xpc/com.apple.mobilenotes.HTMLConverter](MACHOS/com.apple.mobilenotes.HTMLConverter)
- [/System/Library/PrivateFrameworks/NotesUI.framework/XPCServices/com.apple.mobilenotes.NotesImporter.xpc/com.apple.mobilenotes.NotesImporter](MACHOS/com.apple.mobilenotes.NotesImporter)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/PlugIns/IPSExtension.appex/IPSExtension](MACHOS/IPSExtension)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/PlugIns/OfficeSpotlightImporter.appex/OfficeSpotlightImporter](MACHOS/OfficeSpotlightImporter)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PlugIns/BridgeIntents.appex/BridgeIntents](MACHOS/BridgeIntents)
- [/System/Library/PrivateFrameworks/PairedSync.framework/Support/pairedsyncd](MACHOS/pairedsyncd)
- [/System/Library/PrivateFrameworks/PairedUnlock.framework/pairedunlockd](MACHOS/pairedunlockd)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/XPCServices/com.apple.Bridge.ppNotifierService.xpc/com.apple.Bridge.ppNotifierService](MACHOS/com.apple.Bridge.ppNotifierService)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/XPCServices/SBRendererService.xpc/SBRendererService](MACHOS/SBRendererService)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PlugIns/MarkupPhotoEditingExtension.appex/MarkupPhotoEditingExtension](MACHOS/MarkupPhotoEditingExtension)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/XPCServices/PassKitCoreXPCService.xpc/PassKitCoreXPCService](MACHOS/PassKitCoreXPCService)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd)
- [/System/Library/PrivateFrameworks/PassKitServices.framework/XPCServices/PassKitServicesXPCService.xpc/PassKitServicesXPCService](MACHOS/PassKitServicesXPCService)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Support/pasted](MACHOS/pasted)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/XPCServices/PerfPowerTelemetryReaderService.xpc/PerfPowerTelemetryReaderService](MACHOS/PerfPowerTelemetryReaderService)
- [/System/Library/PrivateFrameworks/PerformanceTrace.framework/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/com.apple.PerformanceTrace.PerformanceTraceService](MACHOS/com.apple.PerformanceTrace.PerformanceTraceService)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PlugIns/PhotoAnalysisLighthousePlugin.appex/PhotoAnalysisLighthousePlugin](MACHOS/PhotoAnalysisLighthousePlugin)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd](MACHOS/photoanalysisd)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosDiagnostics.appex/PhotosDiagnostics](MACHOS/PhotosDiagnostics)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider)
- [/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon](MACHOS/PlugInKitDaemon)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/Support/pointeruid](MACHOS/pointeruid)
- [/System/Library/PrivateFrameworks/PowerLog.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/com.apple.PowerlogCore.diagnosticextension.appex/com.apple.PowerlogCore.diagnosticextension](MACHOS/com.apple.PowerlogCore.diagnosticextension)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PPSFeatureFlagReader.xpc/PPSFeatureFlagReader](MACHOS/PPSFeatureFlagReader)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader](MACHOS/PerfPowerServicesSignpostReader)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/rbdcConverter.xpc/rbdcConverter](MACHOS/rbdcConverter)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool](MACHOS/com.apple.PrintKit.PrinterTool)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/printbandservice.xpc/printbandservice](MACHOS/printbandservice)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd](MACHOS/privacyaccountingd)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin](MACHOS/DPMLRuntimePlugin)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB](MACHOS/DPMLRuntimePluginClassB)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU](MACHOS/DPMLRuntimePluginNonDnU)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/PlugIns/ProactiveShareSheetDataHarvestingLighthousePlugin.appex/ProactiveShareSheetDataHarvestingLighthousePlugin](MACHOS/ProactiveShareSheetDataHarvestingLighthousePlugin)
- [/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/XPCServices/ProfileValidatedAppIdentityService.xpc/ProfileValidatedAppIdentityService](MACHOS/ProfileValidatedAppIdentityService)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PlugIns/SearchResultsExtension.appex/SearchResultsExtension](MACHOS/SearchResultsExtension)
- [/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PlugIns/PromotedContentWebProcessBundle.bundle/PromotedContentWebProcessBundle](MACHOS/PromotedContentWebProcessBundle)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/prototyped](MACHOS/prototyped)
- [/System/Library/PrivateFrameworks/Quagga.framework/XPCServices/com.apple.Quagga.Decode.xpc/com.apple.Quagga.Decode](MACHOS/com.apple.Quagga.Decode)
- [/System/Library/PrivateFrameworks/RTTUI.framework/PlugIns/RTTNotificationContentExtension.appex/RTTNotificationContentExtension](MACHOS/RTTNotificationContentExtension)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/PlugIns/RemindersNotificationContentExtension.appex/RemindersNotificationContentExtension](MACHOS/RemindersNotificationContentExtension)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent](MACHOS/RemoteManagementAgent)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ASConfigurationSubscriber.xpc/ASConfigurationSubscriber](MACHOS/ASConfigurationSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber](MACHOS/AccountSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/InteractiveLegacyProfilesSubscriber.xpc/InteractiveLegacyProfilesSubscriber](MACHOS/InteractiveLegacyProfilesSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/LegacyProfilesSubscriber.xpc/LegacyProfilesSubscriber](MACHOS/LegacyProfilesSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/MDMAppSubscriber.xpc/MDMAppSubscriber](MACHOS/MDMAppSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber](MACHOS/ManagedAppsSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagementTestSubscriber.xpc/ManagementTestSubscriber](MACHOS/ManagementTestSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PasscodeSettingsSubscriber.xpc/PasscodeSettingsSubscriber](MACHOS/PasscodeSettingsSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PowerSubscriber.xpc/PowerSubscriber](MACHOS/PowerSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SecuritySubscriber.xpc/SecuritySubscriber](MACHOS/SecuritySubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber](MACHOS/SoftwareUpdateSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/WatchEnrollmentSubscriber.xpc/WatchEnrollmentSubscriber](MACHOS/WatchEnrollmentSubscriber)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd](MACHOS/remotemanagementd)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/rmdinspect](MACHOS/rmdinspect)
- [/System/Library/PrivateFrameworks/RemoteMediaServices.framework/remotemediaservicesd](MACHOS/remotemediaservicesd)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/CoreGlyphsPrivate.bundle/CoreGlyphsPrivate](MACHOS/CoreGlyphsPrivate)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/PlugIns/com.apple.SMBClientProvider.FileProvider.appex/com.apple.SMBClientProvider.FileProvider](MACHOS/com.apple.SMBClientProvider.FileProvider)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientTool](MACHOS/smbclientTool)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd](MACHOS/smbclientd)
- [/System/Library/PrivateFrameworks/SOS.framework/sosd](MACHOS/sosd)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper](MACHOS/STSXPCHelper)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/AutoFillHelper.xpc/AutoFillHelper](MACHOS/AutoFillHelper)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/CredentialProviderExtensionHelper.xpc/CredentialProviderExtensionHelper](MACHOS/CredentialProviderExtensionHelper)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/com.apple.Safari.SafeBrowsing.Service](MACHOS/com.apple.Safari.SafeBrowsing.Service)
- [/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper](MACHOS/com.apple.Safari.SearchHelper)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/Support/schooltimed](MACHOS/schooltimed)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/PlugIns/ScreenTimeNotificationContentExtension.appex/ScreenTimeNotificationContentExtension](MACHOS/ScreenTimeNotificationContentExtension)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd)
- [/System/Library/PrivateFrameworks/SensorKitHelper.framework/XPCServices/com.apple.SensorKit.SKMediaEventsHelper.xpc/com.apple.SensorKit.SKMediaEventsHelper](MACHOS/com.apple.SensorKit.SKMediaEventsHelper)
- [/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd](MACHOS/liveactivitiesd)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/budd](MACHOS/budd)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourEngagementExtension.appex/SeymourEngagementExtension](MACHOS/SeymourEngagementExtension)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourNotifications.appex/SeymourNotifications](MACHOS/SeymourNotifications)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/diagnosticextension.appex/diagnosticextension](MACHOS/diagnosticextension)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored](MACHOS/fitcored)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcoresessiond](MACHOS/fitcoresessiond)
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/Support/swcutil](MACHOS/swcutil)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropAlertUI.appex/AirDropAlertUI](MACHOS/AirDropAlertUI)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropNotice.appex/AirDropNotice](MACHOS/AirDropNotice)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/ContinuityRemote.appex/ContinuityRemote](MACHOS/ContinuityRemote)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService)
- [/System/Library/PrivateFrameworks/SharingXPCServices.framework/XPCServices/SharingXPCHelper.xpc/SharingXPCHelper](MACHOS/SharingXPCHelper)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/PlugIns/SiriCoreMetricsPlugin.appex/SiriCoreMetricsPlugin](MACHOS/SiriCoreMetricsPlugin)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/PlugIns/SiriGeoIntentExtension.appex/SiriGeoIntentExtension](MACHOS/SiriGeoIntentExtension)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/PlugIns/IdentityIntentExtension.appex/IdentityIntentExtension](MACHOS/IdentityIntentExtension)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced](MACHOS/siriinferenced)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/PlugIns/SiriInferredHelpfulnessPlugin.appex/SiriInferredHelpfulnessPlugin](MACHOS/SiriInferredHelpfulnessPlugin)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/PlugIns/SiriInvocationAnalyticsPlugin.appex/SiriInvocationAnalyticsPlugin](MACHOS/SiriInvocationAnalyticsPlugin)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/PlugIns/THKOnDemandPlugin.appex/THKOnDemandPlugin](MACHOS/THKOnDemandPlugin)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningPlatformPlugin.appex/SiriUserFeedbackLearningPlatformPlugin](MACHOS/SiriUserFeedbackLearningPlatformPlugin)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/PlugIns/SettingsIntentExtension.appex/SettingsIntentExtension](MACHOS/SettingsIntentExtension)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/PlugIns/MusicAppSelectionPFLPlugin.appex/MusicAppSelectionPFLPlugin](MACHOS/MusicAppSelectionPFLPlugin)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/com.apple.SiriTTSService.TrialProxy](MACHOS/com.apple.SiriTTSService.TrialProxy)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTraining](MACHOS/SiriTTSTraining)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent](MACHOS/SiriTTSTrainingAgent)
- [/System/Library/PrivateFrameworks/SiriTasksEvaluation.framework/PlugIns/SiriTasksEvaluationPlugin.appex/SiriTasksEvaluationPlugin](MACHOS/SiriTasksEvaluationPlugin)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/PlugIns/AlarmIntentsExtension.appex/AlarmIntentsExtension](MACHOS/AlarmIntentsExtension)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/PlugIns/TimerIntentsExtension.appex/TimerIntentsExtension](MACHOS/TimerIntentsExtension)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/PlugIns/SiriUserSegmentsPlugin.appex/SiriUserSegmentsPlugin](MACHOS/SiriUserSegmentsPlugin)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension](MACHOS/VideoIntentExtension)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd](MACHOS/sleepd)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/PlugIns/SleepNotificationContentExtension.appex/SleepNotificationContentExtension](MACHOS/SleepNotificationContentExtension)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusMagazineProducer.opplugin/OpusMagazineProducer](MACHOS/OpusMagazineProducer)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusNewClassicProducer.opplugin/OpusNewClassicProducer](MACHOS/OpusNewClassicProducer)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusOrigamiProducer.opplugin/OpusOrigamiProducer](MACHOS/OpusOrigamiProducer)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/PlugIns/SmartRepliesMLRuntimePlugin.appex/SmartRepliesMLRuntimePlugin](MACHOS/SmartRepliesMLRuntimePlugin)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/sociallayerd.app/sociallayerd](MACHOS/sociallayerd)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/Support/subridged](MACHOS/subridged)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUFollowUpRollbackDetectedExtension.appex/SUFollowUpRollbackDetectedExtension](MACHOS/SUFollowUpRollbackDetectedExtension)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUSFollowUpExtension.appex/SUSFollowUpExtension](MACHOS/SUSFollowUpExtension)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd](MACHOS/softwareupdateservicesd)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin)
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics)
- [/System/Library/PrivateFrameworks/SoundDetectionNotificationExtension.appex/SoundDetectionNotificationExtension](MACHOS/SoundDetectionNotificationExtension)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/PlugIns/SoundScapesViewServices.appex/SoundScapesViewServices](MACHOS/SoundScapesViewServices)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd](MACHOS/com.apple.SpeechRecognitionCore.brokerd)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent](MACHOS/StatusKitAgent)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd)
- [/System/Library/PrivateFrameworks/StorageKit.framework/XPCServices/storagekitfsrunner.xpc/storagekitfsrunner](MACHOS/storagekitfsrunner)
- [/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/Support/storebookkeeperd](MACHOS/storebookkeeperd)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.privileged.xpc/STExtractionService.privileged](MACHOS/STExtractionService.privileged)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.xpc/STExtractionService](MACHOS/STExtractionService)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.privileged.xpc/com.apple.StreamingUnzipService.privileged](MACHOS/com.apple.StreamingUnzipService.privileged)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService](MACHOS/com.apple.StreamingUnzipService)
- [/System/Library/PrivateFrameworks/Synapse.framework/Support/contentlinkingd](MACHOS/contentlinkingd)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd](MACHOS/syncdefaultsd)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd](MACHOS/systemstatusd)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd)
- [/System/Library/PrivateFrameworks/TailspinSymbolication.framework/XPCServices/TailspinSymbolicationServer.xpc/TailspinSymbolicationServer](MACHOS/TailspinSymbolicationServer)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FaceTime.FTConversationService.xpc/com.apple.FaceTime.FTConversationService](MACHOS/com.apple.FaceTime.FTConversationService)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/XPCServices/TextInputTestService.xpc/TextInputTestService](MACHOS/TextInputTestService)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/PlugIns/SiriAUSP.appex/SiriAUSP](MACHOS/SiriAUSP)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/PlugIns/KonaSynthesizer.appex/KonaSynthesizer](MACHOS/KonaSynthesizer)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/PlugIns/MauiAUSP.appex/MauiAUSP](MACHOS/MauiAUSP)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/PlugIns/VoiceBankingDiagnostics.appex/VoiceBankingDiagnostics](MACHOS/VoiceBankingDiagnostics)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd)
- [/System/Library/PrivateFrameworks/ToneLibrary.framework/XPCServices/com.apple.tonelibraryd.xpc/com.apple.tonelibraryd](MACHOS/com.apple.tonelibraryd)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/PlugIns/TransparencyFollowUpExtension.appex/TransparencyFollowUpExtension](MACHOS/TransparencyFollowUpExtension)
- [/System/Library/PrivateFrameworks/TrialServer.framework/XPCServices/TrialArchivingService.xpc/TrialArchivingService](MACHOS/TrialArchivingService)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/XPCServices/com.apple.uifoundation-bundle-helper.xpc/com.apple.uifoundation-bundle-helper](MACHOS/com.apple.uifoundation-bundle-helper)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/XPCServices/nsattributedstringagent.xpc/nsattributedstringagent](MACHOS/nsattributedstringagent)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/PlugIns/UIUnderstanding.diagnosticextension.appex/UIUnderstanding.diagnosticextension](MACHOS/UIUnderstanding.diagnosticextension)
- [/System/Library/PrivateFrameworks/USDLib_FormatLoaderProxy.framework/XPCServices/USDLib_FormatLoader.xpc/USDLib_FormatLoader](MACHOS/USDLib_FormatLoader)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService](MACHOS/UVFSService)
- [/System/Library/PrivateFrameworks/UnityPoster.framework/PlugIns/UnityPosterExtension.appex/UnityPosterExtension](MACHOS/UnityPosterExtension)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd)
- [/System/Library/PrivateFrameworks/UserActivity.framework/PlugIns/UASharedPasteboardiOSUI.appex/UASharedPasteboardiOSUI](MACHOS/UASharedPasteboardiOSUI)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/userfs_provider.appex/userfs_provider](MACHOS/userfs_provider)
- [/System/Library/PrivateFrameworks/UserFS.framework/userfs_helper](MACHOS/userfs_helper)
- [/System/Library/PrivateFrameworks/UserFS.framework/userfsd](MACHOS/userfsd)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd](MACHOS/usernotificationsd)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/PlugIns/UserNotificationsUIDefaultExtension.appex/UserNotificationsUIDefaultExtension](MACHOS/UserNotificationsUIDefaultExtension)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/PlugIns/UserNotificationsUIThumbnailProvider.appex/UserNotificationsUIThumbnailProvider](MACHOS/UserNotificationsUIThumbnailProvider)
- [/System/Library/PrivateFrameworks/VectorKit.framework/mapinspectord](MACHOS/mapinspectord)
- [/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit](MACHOS/VisualTestKit)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/Support/voicememod](MACHOS/voicememod)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/PlugIns/VoiceServicesDiagnosticextension.appex/VoiceServicesDiagnosticextension](MACHOS/VoiceServicesDiagnosticextension)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/voiced](MACHOS/voiced)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd](MACHOS/siriactionsd)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/PlugIns/CollectionsPoster.appex/CollectionsPoster](MACHOS/CollectionsPoster)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd](MACHOS/watchlistd)
- [/System/Library/PrivateFrameworks/Weather.framework/Support/nanoweatherprefsd](MACHOS/nanoweatherprefsd)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd](MACHOS/webprivacyd)
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/matd](MACHOS/matd)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/PlugIns/WiFiPickerExtension.appex/WiFiPickerExtension](MACHOS/WiFiPickerExtension)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/ThreeBarsXPCService.xpc/ThreeBarsXPCService](MACHOS/ThreeBarsXPCService)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService](MACHOS/WiFiCloudAssetsXPCService)
- [/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/PlugIns/AWDDiagnosticExtension.appex/AWDDiagnosticExtension](MACHOS/AWDDiagnosticExtension)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents](MACHOS/ShortcutsIntents)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension](MACHOS/AddShortcutExtension)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/CatalystContentExtension.appex/CatalystContentExtension](MACHOS/CatalystContentExtension)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/XPCServices/WorkoutKitXPCService.xpc/WorkoutKitXPCService](MACHOS/WorkoutKitXPCService)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService](MACHOS/ZhuGeService)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/ContainerMetadataExtractor](MACHOS/ContainerMetadataExtractor)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/TelemetryDiskChecker.xpc/TelemetryDiskChecker](MACHOS/TelemetryDiskChecker)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup](MACHOS/ICQFollowup)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/PlugIns/ICQEngagementExtension.appex/ICQEngagementExtension](MACHOS/ICQEngagementExtension)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerCore.framework/PlugIns/PFLPlugin.appex/PFLPlugin](MACHOS/PFLPlugin)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd](MACHOS/icloudsubscriptionoptimizerd)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/PlugIns/LighthousePlugin.appex/LighthousePlugin](MACHOS/LighthousePlugin)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/XPCServices/com.apple.DiagnosticsSessionAvailibility.xpc/com.apple.DiagnosticsSessionAvailibility](MACHOS/com.apple.DiagnosticsSessionAvailibility)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd](MACHOS/iosdiagnosticsd)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/XPCServices/SharedListeningConnectionService.xpc/SharedListeningConnectionService](MACHOS/SharedListeningConnectionService)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/PlugIns/SUAskPermissionExtension.appex/SUAskPermissionExtension](MACHOS/SUAskPermissionExtension)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/iWorkImport](MACHOS/iWorkImport)
- [/System/Library/PrivateFrameworks/iWorkXPC.framework/XPCServices/iWorkFileFormat.xpc/iWorkFileFormat](MACHOS/iWorkFileFormat)
- [/System/Library/Recents/Plugins/GenericAddressHandler.addresshandler/GenericAddressHandler](MACHOS/GenericAddressHandler)
- [/System/Library/Recents/Plugins/MapsRecents.addresshandler/MapsRecents](MACHOS/MapsRecents)
- [/System/Library/RelevanceEngine/NanoDataSources/BreatheRelevanceEngineDataSource.bundle/BreatheRelevanceEngineDataSource](MACHOS/BreatheRelevanceEngineDataSource)
- [/System/Library/RelevanceEngine/NanoDataSources/MindRelevanceEngineDataSource.bundle/MindRelevanceEngineDataSource](MACHOS/MindRelevanceEngineDataSource)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoAlarmCompanionDataSource.bundle/NanoAlarmCompanionDataSource](MACHOS/NanoAlarmCompanionDataSource)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoBedtimeCompanionDataSource.bundle/NanoBedtimeCompanionDataSource](MACHOS/NanoBedtimeCompanionDataSource)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMenstrualCyclesRelevanceEngineDataSource.bundle/NanoMenstrualCyclesRelevanceEngineDataSource](MACHOS/NanoMenstrualCyclesRelevanceEngineDataSource)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineActivityRings.bundle/RelevanceEngineActivityRings](MACHOS/RelevanceEngineActivityRings)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineActivityUpNext.bundle/RelevanceEngineActivityUpNext](MACHOS/RelevanceEngineActivityUpNext)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineAudiobooks.bundle/RelevanceEngineAudiobooks](MACHOS/RelevanceEngineAudiobooks)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineCalendar.bundle/RelevanceEngineCalendar](MACHOS/RelevanceEngineCalendar)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineHeart.bundle/RelevanceEngineHeart](MACHOS/RelevanceEngineHeart)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineMusic.bundle/RelevanceEngineMusic](MACHOS/RelevanceEngineMusic)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineNowPlaying.bundle/RelevanceEngineNowPlaying](MACHOS/RelevanceEngineNowPlaying)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEnginePodcasts.bundle/RelevanceEnginePodcasts](MACHOS/RelevanceEnginePodcasts)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineReminders.bundle/RelevanceEngineReminders](MACHOS/RelevanceEngineReminders)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSiriSnippets.bundle/RelevanceEngineSiriSnippets](MACHOS/RelevanceEngineSiriSnippets)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSports.bundle/RelevanceEngineSports](MACHOS/RelevanceEngineSports)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineStopwatch.bundle/RelevanceEngineStopwatch](MACHOS/RelevanceEngineStopwatch)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineTimer.bundle/RelevanceEngineTimer](MACHOS/RelevanceEngineTimer)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineWallet.bundle/RelevanceEngineWallet](MACHOS/RelevanceEngineWallet)
- [/System/Library/RelevanceEngine/NanoDataSources/ShortcutsRelevanceEngineDataSource.bundle/ShortcutsRelevanceEngineDataSource](MACHOS/ShortcutsRelevanceEngineDataSource)
- [/System/Library/ScreenReader/BrailleDrivers/Alva6Series.brailledriver/Alva6Series](MACHOS/Alva6Series)
- [/System/Library/ScreenReader/BrailleDrivers/Baum.brailledriver/Baum](MACHOS/Baum)
- [/System/Library/ScreenReader/BrailleDrivers/BrailleNoteApex.brailledriver/BrailleNoteApex](MACHOS/BrailleNoteApex)
- [/System/Library/ScreenReader/BrailleDrivers/BrailleSense.brailledriver/BrailleSense](MACHOS/BrailleSense)
- [/System/Library/ScreenReader/BrailleDrivers/Brailliant 2 Driver.brailledriver/Brailliant 2 Driver](MACHOS/Brailliant_2_Driver)
- [/System/Library/ScreenReader/BrailleDrivers/DOT Driver.brailledriver/DOT Driver](MACHOS/DOT_Driver)
- [/System/Library/ScreenReader/BrailleDrivers/EasyLink.brailledriver/EasyLink](MACHOS/EasyLink)
- [/System/Library/ScreenReader/BrailleDrivers/Eurobraille.brailledriver/Eurobraille](MACHOS/Eurobraille)
- [/System/Library/ScreenReader/BrailleDrivers/FreedomScientific.brailledriver/FreedomScientific](MACHOS/FreedomScientific)
- [/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/GenericHID](MACHOS/GenericHID)
- [/System/Library/ScreenReader/BrailleDrivers/HIMS Driver.brailledriver/HIMS Driver](MACHOS/HIMS_Driver)
- [/System/Library/ScreenReader/BrailleDrivers/HandyTech.brailledriver/HandyTech](MACHOS/HandyTech)
- [/System/Library/ScreenReader/BrailleDrivers/KGS Driver.brailledriver/KGS Driver](MACHOS/KGS_Driver)
- [/System/Library/ScreenReader/BrailleDrivers/MDV.brailledriver/MDV](MACHOS/MDV)
- [/System/Library/ScreenReader/BrailleDrivers/Ninepoint Systems Driver.brailledriver/Ninepoint Systems Driver](MACHOS/Ninepoint_Systems_Driver)
- [/System/Library/ScreenReader/BrailleDrivers/Papenmeier.brailledriver/Papenmeier](MACHOS/Papenmeier)
- [/System/Library/ScreenReader/BrailleDrivers/Seika.brailledriver/Seika](MACHOS/Seika)
- [/System/Library/ScreenReader/BrailleTables/AppleBrailleTranslator.brailletable/AppleBrailleTranslator](MACHOS/AppleBrailleTranslator)
- [/System/Library/ScreenReader/BrailleTables/BrailleNBSC.brailletable/BrailleNBSC](MACHOS/BrailleNBSC)
- [/System/Library/ScreenReader/BrailleTables/Duxbury.brailletable/Duxbury](MACHOS/Duxbury)
- [/System/Library/ScreenReader/BrailleTables/LiblouisBrailleTranslator.brailletable/LiblouisBrailleTranslator](MACHOS/LiblouisBrailleTranslator)
- [/System/Library/ScreenReader/BrailleTables/Rhine.brailletable/Rhine](MACHOS/Rhine)
- [/System/Library/SetupAssistantBundles/FaceTimeSetupAssistantBundle.bundle/FaceTimeSetupAssistantBundle](MACHOS/FaceTimeSetupAssistantBundle)
- [/System/Library/SetupAssistantBundles/GameCenterSetupAssistant.bundle/GameCenterSetupAssistant](MACHOS/GameCenterSetupAssistant)
- [/System/Library/SetupAssistantBundles/MadridSetupAssistantBundle.bundle/MadridSetupAssistantBundle](MACHOS/MadridSetupAssistantBundle)
- [/System/Library/SetupAssistantBundles/SBSyncServiceSetupAssistantBundle.bundle/SBSyncServiceSetupAssistantBundle](MACHOS/SBSyncServiceSetupAssistantBundle)
- [/System/Library/SetupAssistantBundles/iTunesStoreSetupAssistant.bundle/iTunesStoreSetupAssistant](MACHOS/iTunesStoreSetupAssistant)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AppLaunchSuggestionsPlugin.bundle/AppLaunchSuggestionsPlugin](MACHOS/AppLaunchSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/CalendarSuggestions.bundle/CalendarSuggestions](MACHOS/CalendarSuggestions)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PhoneSuggestions.bundle/PhoneSuggestions](MACHOS/PhoneSuggestions)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PlaybackControlsSuggestionsPlugin.bundle/PlaybackControlsSuggestionsPlugin](MACHOS/PlaybackControlsSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriGeoSuggestions.bundle/SiriGeoSuggestions](MACHOS/SiriGeoSuggestions)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriInformationSuggestionsPlugin.bundle/SiriInformationSuggestionsPlugin](MACHOS/SiriInformationSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriMessagesSuggestions.bundle/SiriMessagesSuggestions](MACHOS/SiriMessagesSuggestions)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSettingsSuggestionsPlugin.bundle/SiriSettingsSuggestionsPlugin](MACHOS/SiriSettingsSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSocialConversationSuggestionsPlugin.bundle/SiriSocialConversationSuggestionsPlugin](MACHOS/SiriSocialConversationSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriTimeSuggestionsPlugin.bundle/SiriTimeSuggestionsPlugin](MACHOS/SiriTimeSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SystemCommandsSuggestionsPlugin.bundle/SystemCommandsSuggestionsPlugin](MACHOS/SystemCommandsSuggestionsPlugin)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/VideoSuggestionsPlugin.bundle/VideoSuggestionsPlugin](MACHOS/VideoSuggestionsPlugin)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/AudioUIPlugin](MACHOS/AudioUIPlugin)
- [/System/Library/Snippets/UIPlugins/CalendarUIPlugin.bundle/CalendarUIPlugin](MACHOS/CalendarUIPlugin)
- [/System/Library/Snippets/UIPlugins/CarCommandsUIPlugin.bundle/CarCommandsUIPlugin](MACHOS/CarCommandsUIPlugin)
- [/System/Library/Snippets/UIPlugins/FindMyUIPlugin.bundle/FindMyUIPlugin](MACHOS/FindMyUIPlugin)
- [/System/Library/Snippets/UIPlugins/GeoUIPlugin.bundle/GeoUIPlugin](MACHOS/GeoUIPlugin)
- [/System/Library/Snippets/UIPlugins/HomeCommunicationUIPlugin.bundle/HomeCommunicationUIPlugin](MACHOS/HomeCommunicationUIPlugin)
- [/System/Library/Snippets/UIPlugins/MessagesUIPlugin.bundle/MessagesUIPlugin](MACHOS/MessagesUIPlugin)
- [/System/Library/Snippets/UIPlugins/PhoneUIPlugin.bundle/PhoneUIPlugin](MACHOS/PhoneUIPlugin)
- [/System/Library/Snippets/UIPlugins/SettingsCustomPlugin.bundle/SettingsCustomPlugin](MACHOS/SettingsCustomPlugin)
- [/System/Library/Snippets/UIPlugins/ShazamUIPlugin.bundle/ShazamUIPlugin](MACHOS/ShazamUIPlugin)
- [/System/Library/Snippets/UIPlugins/SiriExpanseInternalUIPlugin.bundle/SiriExpanseInternalUIPlugin](MACHOS/SiriExpanseInternalUIPlugin)
- [/System/Library/Snippets/UIPlugins/SiriInferenceFlowsUIPlugin.bundle/SiriInferenceFlowsUIPlugin](MACHOS/SiriInferenceFlowsUIPlugin)
- [/System/Library/Snippets/UIPlugins/SiriLinkUIPlugin.bundle/SiriLinkUIPlugin](MACHOS/SiriLinkUIPlugin)
- [/System/Library/Snippets/UIPlugins/SiriMailUIPlugin.bundle/SiriMailUIPlugin](MACHOS/SiriMailUIPlugin)
- [/System/Library/Snippets/UIPlugins/SiriSocialConversationUIPlugin.bundle/SiriSocialConversationUIPlugin](MACHOS/SiriSocialConversationUIPlugin)
- [/System/Library/Snippets/UIPlugins/SiriSuggestionsUIPlugin.bundle/SiriSuggestionsUIPlugin](MACHOS/SiriSuggestionsUIPlugin)
- [/System/Library/Snippets/UIPlugins/SiriVideoUIPlugin.bundle/SiriVideoUIPlugin](MACHOS/SiriVideoUIPlugin)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin)
- [/System/Library/Snippets/UIPlugins/TimerUIPlugin.bundle/TimerUIPlugin](MACHOS/TimerUIPlugin)
- [/System/Library/Snippets/UIPlugins/WellnessUIPlugin.bundle/WellnessUIPlugin](MACHOS/WellnessUIPlugin)
- [/System/Library/SpringBoardPlugins/FindMyiPhoneLockScreen.lockbundle/FindMyiPhoneLockScreen](MACHOS/FindMyiPhoneLockScreen)
- [/System/Library/SpringBoardPlugins/PassesLockScreenPlugin.lockbundle/PassesLockScreenPlugin](MACHOS/PassesLockScreenPlugin)
- [/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin](MACHOS/StoreDemoPlugin)
- [/System/Library/SpringBoardPlugins/ZoomTouch.bundle/ZoomTouch](MACHOS/ZoomTouch)
- [/System/Library/StreamingExtractorPlugins/STAEAExtractionPlugin.bundle/STAEAExtractionPlugin](MACHOS/STAEAExtractionPlugin)
- [/System/Library/SyncBundles/AirFair.syncBundle/AirFair](MACHOS/AirFair)
- [/System/Library/SyncBundles/AirFair2.syncBundle/AirFair2](MACHOS/AirFair2)
- [/System/Library/SyncBundles/Apps.syncBundle/Apps](MACHOS/Apps)
- [/System/Library/SyncBundles/Books.syncBundle/Books](MACHOS/Books)
- [/System/Library/SyncBundles/LogsPlugin.syncBundle/LogsPlugin](MACHOS/LogsPlugin)
- [/System/Library/SyncBundles/MBATCPlugin.syncBundle/MBATCPlugin](MACHOS/MBATCPlugin)
- [/System/Library/SyncBundles/MobileSlideShow.syncBundle/MobileSlideShow](MACHOS/MobileSlideShow)
- [/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary](MACHOS/MusicLibrary)
- [/System/Library/SyncBundles/Podcasts.syncBundle/Podcasts](MACHOS/Podcasts)
- [/System/Library/SyncBundles/SMS.syncBundle/SMS](MACHOS/SMS)
- [/System/Library/SyncBundles/Tones.syncBundle/Tones](MACHOS/Tones)
- [/System/Library/SyncBundles/UserDataPlugin.syncBundle/UserDataPlugin](MACHOS/UserDataPlugin)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/EAPOLController](MACHOS/EAPOLController)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient](MACHOS/eapolclient)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration)
- [/System/Library/SystemConfiguration/PPPController.bundle/PPPController](MACHOS/PPPController)
- [/System/Library/SystemConfiguration/PPPController.bundle/PlugIns/L2TP.ppp/L2TP](MACHOS/L2TP)
- [/System/Library/SystemConfiguration/PPPController.bundle/PlugIns/PPPDialogs.ppp/PPPDialogs](MACHOS/PPPDialogs)
- [/System/Library/SystemConfiguration/USBDeviceConfiguration.bundle/USBDeviceConfiguration](MACHOS/USBDeviceConfiguration)
- [/System/Library/TextInput/Plugins/MessagesDataKeyboardPlugin.bundle/MessagesDataKeyboardPlugin](MACHOS/MessagesDataKeyboardPlugin)
- [/System/Library/TextInput/kbd](MACHOS/kbd)
- [/System/Library/Trace/Providers/Logging.bundle/Logging](MACHOS/Logging)
- [/System/Library/Trace/Providers/Required.bundle/Required](MACHOS/Required)
- [/System/Library/Trace/Providers/Symbolication.bundle/Symbolication](MACHOS/Symbolication)
- [/System/Library/Trace/Providers/TrialProvider.bundle/TrialProvider](MACHOS/TrialProvider)
- [/System/Library/UsageBundles/CalendarUsage.bundle/CalendarUsage](MACHOS/CalendarUsage)
- [/System/Library/UsageBundles/ContactsUsage.bundle/ContactsUsage](MACHOS/ContactsUsage)
- [/System/Library/UsageBundles/MailUsage.bundle/MailUsage](MACHOS/MailUsage)
- [/System/Library/UsageBundles/MessagesUsagePreferencesPlugin.bundle/MessagesUsagePreferencesPlugin](MACHOS/MessagesUsagePreferencesPlugin)
- [/System/Library/UsageBundles/MusicUsage.bundle/MusicUsage](MACHOS/MusicUsage)
- [/System/Library/UsageBundles/NanoBackupUsage.bundle/NanoBackupUsage](MACHOS/NanoBackupUsage)
- [/System/Library/UsageBundles/PassbookUsageBundle.bundle/PassbookUsageBundle](MACHOS/PassbookUsageBundle)
- [/System/Library/UsageBundles/SafariUsageBundle.bundle/SafariUsageBundle](MACHOS/SafariUsageBundle)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage)
- [/System/Library/UsageBundles/ToneSettingsUsage.bundle/ToneSettingsUsage](MACHOS/ToneSettingsUsage)
- [/System/Library/UsageBundles/VideosUsage.bundle/VideosUsage](MACHOS/VideosUsage)
- [/System/Library/UsageBundles/VisualVoicemailUsage.bundle/VisualVoicemailUsage](MACHOS/VisualVoicemailUsage)
- [/System/Library/UserEventPlugins/ADEventListenerPlugin.plugin/ADEventListenerPlugin](MACHOS/ADEventListenerPlugin)
- [/System/Library/UserEventPlugins/AHTUserEventAgent.plugin/AHTUserEventAgent](MACHOS/AHTUserEventAgent)
- [/System/Library/UserEventPlugins/BonjourEvents.plugin/BonjourEvents](MACHOS/BonjourEvents)
- [/System/Library/UserEventPlugins/GreenTeaUserEventAgent.plugin/GreenTeaUserEventAgent](MACHOS/GreenTeaUserEventAgent)
- [/System/Library/UserEventPlugins/ManagedConfigurationUEA.plugin/ManagedConfigurationUEA](MACHOS/ManagedConfigurationUEA)
- [/System/Library/UserEventPlugins/MemoryMonitor.plugin/MemoryMonitor](MACHOS/MemoryMonitor)
- [/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA](MACHOS/MobileBackupUEA)
- [/System/Library/UserEventPlugins/MobileGestaltEvents.plugin/MobileGestaltEvents](MACHOS/MobileGestaltEvents)
- [/System/Library/UserEventPlugins/MobileKeyBagLockState.plugin/MobileKeyBagLockState](MACHOS/MobileKeyBagLockState)
- [/System/Library/UserEventPlugins/PerfPowerServicesEventListenerPlugin.plugin/PerfPowerServicesEventListenerPlugin](MACHOS/PerfPowerServicesEventListenerPlugin)
- [/System/Library/UserEventPlugins/USBEthernetSharing.plugin/USBEthernetSharing](MACHOS/USBEthernetSharing)
- [/System/Library/UserEventPlugins/com.apple.AppleKeyStoreEvents.plugin/com.apple.AppleKeyStoreEvents](MACHOS/com.apple.AppleKeyStoreEvents)
- [/System/Library/UserEventPlugins/com.apple.BackgroundTaskAgentPlugin.plugin/com.apple.BackgroundTaskAgentPlugin](MACHOS/com.apple.BackgroundTaskAgentPlugin)
- [/System/Library/UserEventPlugins/com.apple.ExternalAccessory.matching.plugin/com.apple.ExternalAccessory.matching](MACHOS/com.apple.ExternalAccessory.matching)
- [/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching](MACHOS/com.apple.accessoryd.matching)
- [/System/Library/UserEventPlugins/com.apple.alarm.plugin/com.apple.alarm](MACHOS/com.apple.alarm)
- [/System/Library/UserEventPlugins/com.apple.bonjour.plugin/com.apple.bonjour](MACHOS/com.apple.bonjour)
- [/System/Library/UserEventPlugins/com.apple.cfnotification.plugin/com.apple.cfnotification](MACHOS/com.apple.cfnotification)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts)
- [/System/Library/UserEventPlugins/com.apple.dispatch.vfs.plugin/com.apple.dispatch.vfs](MACHOS/com.apple.dispatch.vfs)
- [/System/Library/UserEventPlugins/com.apple.fsevents.matching.plugin/com.apple.fsevents.matching](MACHOS/com.apple.fsevents.matching)
- [/System/Library/UserEventPlugins/com.apple.iokit.matching.plugin/com.apple.iokit.matching](MACHOS/com.apple.iokit.matching)
- [/System/Library/UserEventPlugins/com.apple.launchd.helper.plugin/com.apple.launchd.helper](MACHOS/com.apple.launchd.helper)
- [/System/Library/UserEventPlugins/com.apple.netsvcproxy.plugin/com.apple.netsvcproxy](MACHOS/com.apple.netsvcproxy)
- [/System/Library/UserEventPlugins/com.apple.networkextension.plugin/com.apple.networkextension](MACHOS/com.apple.networkextension)
- [/System/Library/UserEventPlugins/com.apple.nsurlsessiond.plugin/com.apple.nsurlsessiond](MACHOS/com.apple.nsurlsessiond)
- [/System/Library/UserEventPlugins/com.apple.rapport.events.plugin/com.apple.rapport.events](MACHOS/com.apple.rapport.events)
- [/System/Library/UserEventPlugins/com.apple.spd.plugin/com.apple.spd](MACHOS/com.apple.spd)
- [/System/Library/UserEventPlugins/com.apple.systemconfiguration.plugin/com.apple.systemconfiguration](MACHOS/com.apple.systemconfiguration)
- [/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin](MACHOS/com.apple.tailspin)
- [/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry](MACHOS/com.apple.telemetry)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events)
- [/System/Library/UserEventPlugins/routined.events.plugin/routined.events](MACHOS/routined.events)
- [/System/Library/UserNotifications/Bundles/com.apple.ARQLNotifications.bundle/com.apple.ARQLNotifications](MACHOS/com.apple.ARQLNotifications)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications)
- [/System/Library/UserNotifications/Bundles/com.apple.donotdisturb.bundle/com.apple.donotdisturb](MACHOS/com.apple.donotdisturb)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1](MACHOS/SemanticStyleV1)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/VideoDeghostingV1](MACHOS/VideoDeghostingV1)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2)
- [/System/Library/VoiceServices/PlugIns/Base.vsplugin/Base](MACHOS/Base)
- [/bin/df](MACHOS/df)
- [/bin/ps](MACHOS/ps)
- [/private/var/staged_system_apps/AppleTV.app/AppleTV](MACHOS/AppleTV)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVCoreSpotlightExtension.appex/TVCoreSpotlightExtension](MACHOS/TVCoreSpotlightExtension)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVIntentsExtension.appex/TVIntentsExtension](MACHOS/TVIntentsExtension)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKAudiobooks.framework/BKAudiobooks](MACHOS/BKAudiobooks)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary](MACHOS/BKLibrary)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksAll.framework/BooksAll](MACHOS/BooksAll)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI)
- [/private/var/staged_system_apps/Books.app/Frameworks/EngagementCollector.framework/EngagementCollector](MACHOS/EngagementCollector)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI)
- [/private/var/staged_system_apps/Books.app/PlugIns/BookEPUBWebProcessPlugin.bundle/BookEPUBWebProcessPlugin](MACHOS/BookEPUBWebProcessPlugin)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksEngagementExtension.appex/BooksEngagementExtension](MACHOS/BooksEngagementExtension)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksIntentHandler.appex/BooksIntentHandler](MACHOS/BooksIntentHandler)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksNotificationContentExtension.appex/BooksNotificationContentExtension](MACHOS/BooksNotificationContentExtension)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension](MACHOS/BooksProductPageExtension)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/BooksSpotlightExtension](MACHOS/BooksSpotlightExtension)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksThumbnail.appex/BooksThumbnail](MACHOS/BooksThumbnail)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension)
- [/private/var/staged_system_apps/Books.app/XPCServices/XPCUbiquityDisableService.xpc/XPCUbiquityDisableService](MACHOS/XPCUbiquityDisableService)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge)
- [/private/var/staged_system_apps/Bridge.app/PlugIns/GreenfieldThumbnailExtension.appex/GreenfieldThumbnailExtension](MACHOS/GreenfieldThumbnailExtension)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator)
- [/private/var/staged_system_apps/Compass.app/Compass](MACHOS/Compass)
- [/private/var/staged_system_apps/Contacts.app/Contacts](MACHOS/Contacts)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsItems.appex/FindMyWidgetIntentsItems](MACHOS/FindMyWidgetIntentsItems)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsPeople.appex/FindMyWidgetIntentsPeople](MACHOS/FindMyWidgetIntentsPeople)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessIntents.appex/FitnessIntents](MACHOS/FitnessIntents)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/MirroredWidgetExtension.appex/MirroredWidgetExtension](MACHOS/MirroredWidgetExtension)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health)
- [/private/var/staged_system_apps/Health.app/PlugIns/HealthMedicationsWidgetExtension.appex/HealthMedicationsWidgetExtension](MACHOS/HealthMedicationsWidgetExtension)
- [/private/var/staged_system_apps/Health.app/PlugIns/HealthMentalHealthWidgetExtension.appex/HealthMentalHealthWidgetExtension](MACHOS/HealthMentalHealthWidgetExtension)
- [/private/var/staged_system_apps/Health.app/PlugIns/ShareExtension.appex/ShareExtension](MACHOS/ShareExtension)
- [/private/var/staged_system_apps/Home.app/Home](MACHOS/Home)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeDiagnosticExtension.appex/HomeDiagnosticExtension](MACHOS/HomeDiagnosticExtension)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification](MACHOS/HomeNotification)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomePersonalRequestNotification.appex/HomePersonalRequestNotification](MACHOS/HomePersonalRequestNotification)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeUtilNotification.appex/HomeUtilNotification](MACHOS/HomeUtilNotification)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen](MACHOS/HomeWidgetLockScreen)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent](MACHOS/HomeWidgetSingleAccessoryIntent)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension)
- [/private/var/staged_system_apps/Magnifier.app/Magnifier](MACHOS/Magnifier)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget)
- [/private/var/staged_system_apps/Maps.app/PlugIns/MapsSpotlightIndexExtension.appex/MapsSpotlightIndexExtension](MACHOS/MapsSpotlightIndexExtension)
- [/private/var/staged_system_apps/Maps.app/PlugIns/SiriTrafficIncidents.appex/SiriTrafficIncidents](MACHOS/SiriTrafficIncidents)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension](MACHOS/CalendarWidgetExtension)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/FacetimeExtension.appex/FacetimeExtension](MACHOS/FacetimeExtension)
- [/private/var/staged_system_apps/MobileMail.app/Extensions/MailShortcutsExtension.appex/MailShortcutsExtension](MACHOS/MailShortcutsExtension)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailIntentsExtension.appex/MailIntentsExtension](MACHOS/MailIntentsExtension)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.EditorExtension.appex/com.apple.mobilenotes.EditorExtension](MACHOS/com.apple.mobilenotes.EditorExtension)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.IntentsExtension.appex/com.apple.mobilenotes.IntentsExtension](MACHOS/com.apple.mobilenotes.IntentsExtension)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.QuickLookExtension.appex/com.apple.mobilenotes.QuickLookExtension](MACHOS/com.apple.mobilenotes.QuickLookExtension)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SpotlightIndexExtension.appex/com.apple.mobilenotes.SpotlightIndexExtension](MACHOS/com.apple.mobilenotes.SpotlightIndexExtension)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension)
- [/private/var/staged_system_apps/MobileStore.app/MobileStore](MACHOS/MobileStore)
- [/private/var/staged_system_apps/MobileStore.app/XPCServices/com.apple.MobileStore.appremoval.xpc/com.apple.MobileStore.appremoval](MACHOS/com.apple.MobileStore.appremoval)
- [/private/var/staged_system_apps/MobileTimer.app/MobileTimer](MACHOS/MobileTimer)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget)
- [/private/var/staged_system_apps/Music.app/Extensions/MusicFocusFilters.appex/MusicFocusFilters](MACHOS/MusicFocusFilters)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music)
- [/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker](MACHOS/MediaPicker)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicCoreSpotlightExtension.appex/MusicCoreSpotlightExtension](MACHOS/MusicCoreSpotlightExtension)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicNotificationContentExtension.appex/MusicNotificationContentExtension](MACHOS/MusicNotificationContentExtension)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets)
- [/private/var/staged_system_apps/Music.app/PlugIns/StoreFlowExtension.appex/StoreFlowExtension](MACHOS/StoreFlowExtension)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News)
- [/private/var/staged_system_apps/News.app/PlugIns/ArticleNotificationExtension.appex/ArticleNotificationExtension](MACHOS/ArticleNotificationExtension)
- [/private/var/staged_system_apps/News.app/PlugIns/MarketingNotificationExtension.appex/MarketingNotificationExtension](MACHOS/MarketingNotificationExtension)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsArticleQuickLook.appex/NewsArticleQuickLook](MACHOS/NewsArticleQuickLook)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsAudioExtension.appex/NewsAudioExtension](MACHOS/NewsAudioExtension)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsDiagnosticExtension.appex/NewsDiagnosticExtension](MACHOS/NewsDiagnosticExtension)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsEngagementExtension.appex/NewsEngagementExtension](MACHOS/NewsEngagementExtension)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents)
- [/private/var/staged_system_apps/News.app/PlugIns/OpenInNews.appex/OpenInNews](MACHOS/OpenInNews)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookQuicklookPreviewExtension.appex/PassbookQuicklookPreviewExtension](MACHOS/PassbookQuicklookPreviewExtension)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookTransactionNotificationContentExtension.appex/PassbookTransactionNotificationContentExtension](MACHOS/PassbookTransactionNotificationContentExtension)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/IMDebug.framework/IMDebug](MACHOS/IMDebug)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/PodcastsClassKitExtension](MACHOS/PodcastsClassKitExtension)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsNotificationExtension.appex/PodcastsNotificationExtension](MACHOS/PodcastsNotificationExtension)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.DiagnosticExtension.appex/com.apple.podcasts.DiagnosticExtension](MACHOS/com.apple.podcasts.DiagnosticExtension)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension](MACHOS/com.apple.podcasts.SpotlightIndexExtension)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSpotlightIndexExtension.appex/RemindersSpotlightIndexExtension](MACHOS/RemindersSpotlightIndexExtension)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/CacheDeleteExtension.appex/CacheDeleteExtension](MACHOS/CacheDeleteExtension)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/AutomationNotificationContent.appex/AutomationNotificationContent](MACHOS/AutomationNotificationContent)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/QuickLookExtension.appex/QuickLookExtension](MACHOS/QuickLookExtension)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsActionExtension.appex/ShortcutsActionExtension](MACHOS/ShortcutsActionExtension)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ThumbnailExtension.appex/ThumbnailExtension](MACHOS/ThumbnailExtension)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDiagnosticExtension.appex/StocksDiagnosticExtension](MACHOS/StocksDiagnosticExtension)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsNotification.appex/TipsNotification](MACHOS/TipsNotification)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsQuicklook.appex/TipsQuicklook](MACHOS/TipsQuicklook)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsSpotlightIndex.appex/TipsSpotlightIndex](MACHOS/TipsSpotlightIndex)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsWidget.appex/TipsWidget](MACHOS/TipsWidget)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension](MACHOS/VoiceMemosIntentsExtension)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension](MACHOS/VoiceMemosShareExtension)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/com.apple.VoiceMemos.SpotlightIndexExtension.appex/com.apple.VoiceMemos.SpotlightIndexExtension](MACHOS/com.apple.VoiceMemos.SpotlightIndexExtension)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherDiagnosticExtension.appex/WeatherDiagnosticExtension](MACHOS/WeatherDiagnosticExtension)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents](MACHOS/WeatherIntents)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather)
- [/sbin/fsck](MACHOS/fsck)
- [/sbin/fsck_apfs](MACHOS/fsck_apfs)
- [/sbin/launchd](MACHOS/launchd)
- [/sbin/mount](MACHOS/mount)
- [/sbin/mount_apfs](MACHOS/mount_apfs)
- [/sbin/mount_lifs](MACHOS/mount_lifs)
- [/sbin/mount_nfs](MACHOS/mount_nfs)
- [/sbin/mount_tmpfs](MACHOS/mount_tmpfs)
- [/sbin/newfs_apfs](MACHOS/newfs_apfs)
- [/sbin/umount](MACHOS/umount)
- [/usr/bin/DumpBasebandCrash](MACHOS/DumpBasebandCrash)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader)
- [/usr/bin/abmlite](MACHOS/abmlite)
- [/usr/bin/afktool](MACHOS/afktool)
- [/usr/bin/brctl](MACHOS/brctl)
- [/usr/bin/codecctl](MACHOS/codecctl)
- [/usr/bin/fileproviderctl](MACHOS/fileproviderctl)
- [/usr/bin/footprint](MACHOS/footprint)
- [/usr/bin/hidutil](MACHOS/hidutil)
- [/usr/bin/hpmdiagnose](MACHOS/hpmdiagnose)
- [/usr/bin/kbdebug](MACHOS/kbdebug)
- [/usr/bin/lsdiagnose](MACHOS/lsdiagnose)
- [/usr/bin/ltop](MACHOS/ltop)
- [/usr/bin/nfsstat](MACHOS/nfsstat)
- [/usr/bin/powerlogHelperd](MACHOS/powerlogHelperd)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect)
- [/usr/bin/sysdiagnose](MACHOS/sysdiagnose)
- [/usr/bin/taskinfo](MACHOS/taskinfo)
- [/usr/bin/umtool](MACHOS/umtool)
- [/usr/bin/vm_stat](MACHOS/vm_stat)
- [/usr/bin/zprint](MACHOS/zprint)
- [/usr/lib/dyld](MACHOS/dyld)
- [/usr/lib/libBacktraceRecording.dylib](MACHOS/libBacktraceRecording.dylib)
- [/usr/lib/libCoreKE.dylib](MACHOS/libCoreKE.dylib)
- [/usr/lib/libCoreLSKD.dylib](MACHOS/libCoreLSKD.dylib)
- [/usr/lib/libMTLCapture.dylib](MACHOS/libMTLCapture.dylib)
- [/usr/lib/libMTLToolsDiagnostics.dylib](MACHOS/libMTLToolsDiagnostics.dylib)
- [/usr/lib/libMainThreadChecker.dylib](MACHOS/libMainThreadChecker.dylib)
- [/usr/lib/libRPAC.dylib](MACHOS/libRPAC.dylib)
- [/usr/lib/libSystem.B_asan.dylib](MACHOS/libSystem.B_asan.dylib)
- [/usr/lib/libSystem_asan.dylib](MACHOS/libSystem_asan.dylib)
- [/usr/lib/libViewDebuggerSupport.dylib](MACHOS/libViewDebuggerSupport.dylib)
- [/usr/lib/swift/libswiftRemoteMirror.dylib](MACHOS/libswiftRemoteMirror.dylib)
- [/usr/lib/system/introspection/libdispatch.dylib](MACHOS/libdispatch.dylib)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2)
- [/usr/libexec/DataDetectorsSourceAccess](MACHOS/DataDetectorsSourceAccess)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic)
- [/usr/libexec/FSTaskScheduler](MACHOS/FSTaskScheduler)
- [/usr/libexec/FinishRestoreFromBackup](MACHOS/FinishRestoreFromBackup)
- [/usr/libexec/IOAccelMemoryInfoCollector](MACHOS/IOAccelMemoryInfoCollector)
- [/usr/libexec/IOMFB_bics_daemon](MACHOS/IOMFB_bics_daemon)
- [/usr/libexec/MSUEarlyBootTask](MACHOS/MSUEarlyBootTask)
- [/usr/libexec/MTLAssetUpgraderD](MACHOS/MTLAssetUpgraderD)
- [/usr/libexec/MobileGestaltHelper](MACHOS/MobileGestaltHelper)
- [/usr/libexec/MobileStorageMounter](MACHOS/MobileStorageMounter)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler)
- [/usr/libexec/OTATaskingAgent](MACHOS/OTATaskingAgent)
- [/usr/libexec/PerfPowerServices](MACHOS/PerfPowerServices)
- [/usr/libexec/PerfPowerServicesExtended](MACHOS/PerfPowerServicesExtended)
- [/usr/libexec/PowerUIAgent](MACHOS/PowerUIAgent)
- [/usr/libexec/PreboardService](MACHOS/PreboardService)
- [/usr/libexec/ProxiedCrashCopier](MACHOS/ProxiedCrashCopier)
- [/usr/libexec/PurpleReverseProxy](MACHOS/PurpleReverseProxy)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException)
- [/usr/libexec/SavageUtil](MACHOS/SavageUtil)
- [/usr/libexec/SensorKitALSHelper](MACHOS/SensorKitALSHelper)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay)
- [/usr/libexec/SyncAgent](MACHOS/SyncAgent)
- [/usr/libexec/UserEventAgent](MACHOS/UserEventAgent)
- [/usr/libexec/ViewHierarchyAgent](MACHOS/ViewHierarchyAgent)
- [/usr/libexec/YonkersUtil](MACHOS/YonkersUtil)
- [/usr/libexec/addressbooksyncd](MACHOS/addressbooksyncd)
- [/usr/libexec/adid](MACHOS/adid)
- [/usr/libexec/adprivacyd](MACHOS/adprivacyd)
- [/usr/libexec/afcd](MACHOS/afcd)
- [/usr/libexec/amfid](MACHOS/amfid)
- [/usr/libexec/aned](MACHOS/aned)
- [/usr/libexec/announced](MACHOS/announced)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad)
- [/usr/libexec/appleidsetupd](MACHOS/appleidsetupd)
- [/usr/libexec/arkitd](MACHOS/arkitd)
- [/usr/libexec/asd](MACHOS/asd)
- [/usr/libexec/asktod](MACHOS/asktod)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent)
- [/usr/libexec/atc](MACHOS/atc)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd)
- [/usr/libexec/audiomxd](MACHOS/audiomxd)
- [/usr/libexec/avconferenced](MACHOS/avconferenced)
- [/usr/libexec/backboardd](MACHOS/backboardd)
- [/usr/libexec/backgroundassets.user](MACHOS/backgroundassets.user)
- [/usr/libexec/batteryalgorithmsd](MACHOS/batteryalgorithmsd)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced)
- [/usr/libexec/betaenrollmentd](MACHOS/betaenrollmentd)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd)
- [/usr/libexec/biometrickitd](MACHOS/biometrickitd)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd)
- [/usr/libexec/bootpd](MACHOS/bootpd)
- [/usr/libexec/brookcompaniond](MACHOS/brookcompaniond)
- [/usr/libexec/bulletindistributord](MACHOS/bulletindistributord)
- [/usr/libexec/captiveagent](MACHOS/captiveagent)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd)
- [/usr/libexec/carkitd](MACHOS/carkitd)
- [/usr/libexec/cc_fips_test](MACHOS/cc_fips_test)
- [/usr/libexec/checkerboardd](MACHOS/checkerboardd)
- [/usr/libexec/checkpointd](MACHOS/checkpointd)
- [/usr/libexec/ciphermld](MACHOS/ciphermld)
- [/usr/libexec/com.apple.Safari.History](MACHOS/com.apple.Safari.History)
- [/usr/libexec/companion_proxy](MACHOS/companion_proxy)
- [/usr/libexec/companiond](MACHOS/companiond)
- [/usr/libexec/configd](MACHOS/configd)
- [/usr/libexec/containermanagerd](MACHOS/containermanagerd)
- [/usr/libexec/containermanagerd_system](MACHOS/containermanagerd_system)
- [/usr/libexec/continuitycaptured](MACHOS/continuitycaptured)
- [/usr/libexec/coordinated](MACHOS/coordinated)
- [/usr/libexec/corebrightnessdiag](MACHOS/corebrightnessdiag)
- [/usr/libexec/corecaptured](MACHOS/corecaptured)
- [/usr/libexec/coredatad](MACHOS/coredatad)
- [/usr/libexec/coreduetd](MACHOS/coreduetd)
- [/usr/libexec/coreidvd](MACHOS/coreidvd)
- [/usr/libexec/corerepaird](MACHOS/corerepaird)
- [/usr/libexec/countryd](MACHOS/countryd)
- [/usr/libexec/crash_mover](MACHOS/crash_mover)
- [/usr/libexec/cryptexd](MACHOS/cryptexd)
- [/usr/libexec/dasd](MACHOS/dasd)
- [/usr/libexec/datastored](MACHOS/datastored)
- [/usr/libexec/debugserver](MACHOS/debugserver)
- [/usr/libexec/deferredmediad](MACHOS/deferredmediad)
- [/usr/libexec/demod](MACHOS/demod)
- [/usr/libexec/demod_helper](MACHOS/demod_helper)
- [/usr/libexec/deviceaccessd](MACHOS/deviceaccessd)
- [/usr/libexec/dhcp6d](MACHOS/dhcp6d)
- [/usr/libexec/diagnosticd](MACHOS/diagnosticd)
- [/usr/libexec/diagnosticextensionsd](MACHOS/diagnosticextensionsd)
- [/usr/libexec/dietapplecamerad](MACHOS/dietapplecamerad)
- [/usr/libexec/dietappleh16camerad](MACHOS/dietappleh16camerad)
- [/usr/libexec/dirs_cleaner](MACHOS/dirs_cleaner)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod)
- [/usr/libexec/dmd](MACHOS/dmd)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd)
- [/usr/libexec/dprivacyd](MACHOS/dprivacyd)
- [/usr/libexec/driverkitd](MACHOS/driverkitd)
- [/usr/libexec/dtfetchsymbolsd](MACHOS/dtfetchsymbolsd)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd)
- [/usr/libexec/eventkitsyncd](MACHOS/eventkitsyncd)
- [/usr/libexec/facemetricsd](MACHOS/facemetricsd)
- [/usr/libexec/fairplaydeviceidentityd](MACHOS/fairplaydeviceidentityd)
- [/usr/libexec/fdrhelper](MACHOS/fdrhelper)
- [/usr/libexec/feedbackd](MACHOS/feedbackd)
- [/usr/libexec/findmybeaconingd](MACHOS/findmybeaconingd)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced)
- [/usr/libexec/findmylocated](MACHOS/findmylocated)
- [/usr/libexec/finish_demo_restore](MACHOS/finish_demo_restore)
- [/usr/libexec/fmfd](MACHOS/fmfd)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord)
- [/usr/libexec/fseventsd](MACHOS/fseventsd)
- [/usr/libexec/ftp-proxy](MACHOS/ftp-proxy)
- [/usr/libexec/fusiond](MACHOS/fusiond)
- [/usr/libexec/gamecontrollerd](MACHOS/gamecontrollerd)
- [/usr/libexec/gamed](MACHOS/gamed)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd)
- [/usr/libexec/gpsd](MACHOS/gpsd)
- [/usr/libexec/gputoolsd](MACHOS/gputoolsd)
- [/usr/libexec/gputoolsserviced](MACHOS/gputoolsserviced)
- [/usr/libexec/griddatad](MACHOS/griddatad)
- [/usr/libexec/handwritingd](MACHOS/handwritingd)
- [/usr/libexec/hangreporter](MACHOS/hangreporter)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd)
- [/usr/libexec/heartbeatd](MACHOS/heartbeatd)
- [/usr/libexec/hidd](MACHOS/hidd)
- [/usr/libexec/hostapd](MACHOS/hostapd)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent)
- [/usr/libexec/idamd](MACHOS/idamd)
- [/usr/libexec/idcredd](MACHOS/idcredd)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd)
- [/usr/libexec/init_data_protection](MACHOS/init_data_protection)
- [/usr/libexec/init_exclavekit](MACHOS/init_exclavekit)
- [/usr/libexec/init_featureflags](MACHOS/init_featureflags)
- [/usr/libexec/installd](MACHOS/installd)
- [/usr/libexec/intelligentroutingd](MACHOS/intelligentroutingd)
- [/usr/libexec/ioupsd](MACHOS/ioupsd)
- [/usr/libexec/keybagd](MACHOS/keybagd)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd)
- [/usr/libexec/languageassetd](MACHOS/languageassetd)
- [/usr/libexec/launchd_cache_loader](MACHOS/launchd_cache_loader)
- [/usr/libexec/linkd](MACHOS/linkd)
- [/usr/libexec/locationd](MACHOS/locationd)
- [/usr/libexec/locationpushd](MACHOS/locationpushd)
- [/usr/libexec/lockdownd](MACHOS/lockdownd)
- [/usr/libexec/logd](MACHOS/logd)
- [/usr/libexec/logd_helper](MACHOS/logd_helper)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter)
- [/usr/libexec/lsd](MACHOS/lsd)
- [/usr/libexec/lskdd](MACHOS/lskdd)
- [/usr/libexec/magicswitchd](MACHOS/magicswitchd)
- [/usr/libexec/mc_mobile_tunnel](MACHOS/mc_mobile_tunnel)
- [/usr/libexec/mdmd](MACHOS/mdmd)
- [/usr/libexec/mdmuserd](MACHOS/mdmuserd)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd)
- [/usr/libexec/mediaplaybackd](MACHOS/mediaplaybackd)
- [/usr/libexec/mediasetupd](MACHOS/mediasetupd)
- [/usr/libexec/metrickitd](MACHOS/metrickitd)
- [/usr/libexec/microstackshot](MACHOS/microstackshot)
- [/usr/libexec/misagent](MACHOS/misagent)
- [/usr/libexec/misd](MACHOS/misd)
- [/usr/libexec/mlhostd](MACHOS/mlhostd)
- [/usr/libexec/mlruntimed](MACHOS/mlruntimed)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced)
- [/usr/libexec/mobile_assertion_agent](MACHOS/mobile_assertion_agent)
- [/usr/libexec/mobile_diagnostics_relay](MACHOS/mobile_diagnostics_relay)
- [/usr/libexec/mobile_house_arrest](MACHOS/mobile_house_arrest)
- [/usr/libexec/mobile_installation_proxy](MACHOS/mobile_installation_proxy)
- [/usr/libexec/mobile_obliterator](MACHOS/mobile_obliterator)
- [/usr/libexec/mobile_storage_proxy](MACHOS/mobile_storage_proxy)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird)
- [/usr/libexec/momentsd](MACHOS/momentsd)
- [/usr/libexec/mtmergeprops](MACHOS/mtmergeprops)
- [/usr/libexec/nanomediaremotelinkagent](MACHOS/nanomediaremotelinkagent)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd)
- [/usr/libexec/nanoregistrylaunchd](MACHOS/nanoregistrylaunchd)
- [/usr/libexec/naturallanguaged](MACHOS/naturallanguaged)
- [/usr/libexec/neagent](MACHOS/neagent)
- [/usr/libexec/nearbyd](MACHOS/nearbyd)
- [/usr/libexec/nehelper](MACHOS/nehelper)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy)
- [/usr/libexec/nexusd](MACHOS/nexusd)
- [/usr/libexec/nfcd](MACHOS/nfcd)
- [/usr/libexec/nlcd](MACHOS/nlcd)
- [/usr/libexec/notification_proxy](MACHOS/notification_proxy)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent)
- [/usr/libexec/ospredictiond](MACHOS/ospredictiond)
- [/usr/libexec/otpaird](MACHOS/otpaird)
- [/usr/libexec/passcodenagd](MACHOS/passcodenagd)
- [/usr/libexec/passwordbreachd](MACHOS/passwordbreachd)
- [/usr/libexec/pcapd](MACHOS/pcapd)
- [/usr/libexec/pcsstatus](MACHOS/pcsstatus)
- [/usr/libexec/peakpowermanagerd](MACHOS/peakpowermanagerd)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled)
- [/usr/libexec/pfd](MACHOS/pfd)
- [/usr/libexec/pipelined](MACHOS/pipelined)
- [/usr/libexec/pkd](MACHOS/pkd)
- [/usr/libexec/pkreporter](MACHOS/pkreporter)
- [/usr/libexec/pmudiagnose/pmudiagnose](MACHOS/pmudiagnose)
- [/usr/libexec/powerdatad](MACHOS/powerdatad)
- [/usr/libexec/prng_seedctl](MACHOS/prng_seedctl)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd)
- [/usr/libexec/profiled](MACHOS/profiled)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad)
- [/usr/libexec/ptpd](MACHOS/ptpd)
- [/usr/libexec/rapportd](MACHOS/rapportd)
- [/usr/libexec/relatived](MACHOS/relatived)
- [/usr/libexec/remindd](MACHOS/remindd)
- [/usr/libexec/remotectl](MACHOS/remotectl)
- [/usr/libexec/remoted](MACHOS/remoted)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced)
- [/usr/libexec/replayd](MACHOS/replayd)
- [/usr/libexec/resourcegrabberd](MACHOS/resourcegrabberd)
- [/usr/libexec/restoreserviced](MACHOS/restoreserviced)
- [/usr/libexec/routined](MACHOS/routined)
- [/usr/libexec/rsync/rsync.samba](MACHOS/rsync.samba)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd)
- [/usr/libexec/runningboardd](MACHOS/runningboardd)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd)
- [/usr/libexec/screenshotsyncd](MACHOS/screenshotsyncd)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose)
- [/usr/libexec/securityd](MACHOS/securityd)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd)
- [/usr/libexec/seld](MACHOS/seld)
- [/usr/libexec/sensorkitd](MACHOS/sensorkitd)
- [/usr/libexec/seputil](MACHOS/seputil)
- [/usr/libexec/seserviced](MACHOS/seserviced)
- [/usr/libexec/sharingd](MACHOS/sharingd)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter)
- [/usr/libexec/silhouette](MACHOS/silhouette)
- [/usr/libexec/siriknowledged](MACHOS/siriknowledged)
- [/usr/libexec/sirireaderd](MACHOS/sirireaderd)
- [/usr/libexec/smcDiagnose](MACHOS/smcDiagnose)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd)
- [/usr/libexec/soundanalysisd](MACHOS/soundanalysisd)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser)
- [/usr/libexec/splashboardd](MACHOS/splashboardd)
- [/usr/libexec/sportsd](MACHOS/sportsd)
- [/usr/libexec/springboardservicesrelay](MACHOS/springboardservicesrelay)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy)
- [/usr/libexec/storagedatad](MACHOS/storagedatad)
- [/usr/libexec/storagekitd](MACHOS/storagekitd)
- [/usr/libexec/streaming_zip_conduit](MACHOS/streaming_zip_conduit)
- [/usr/libexec/swcd](MACHOS/swcd)
- [/usr/libexec/symptomsd](MACHOS/symptomsd)
- [/usr/libexec/symptomsd-diag](MACHOS/symptomsd-diag)
- [/usr/libexec/symptomsd-helper](MACHOS/symptomsd-helper)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed)
- [/usr/libexec/sysmond](MACHOS/sysmond)
- [/usr/libexec/sysstatuscheck](MACHOS/sysstatuscheck)
- [/usr/libexec/tailspind](MACHOS/tailspind)
- [/usr/libexec/terminusd](MACHOS/terminusd)
- [/usr/libexec/teslad](MACHOS/teslad)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord)
- [/usr/libexec/timed](MACHOS/timed)
- [/usr/libexec/tipsd](MACHOS/tipsd)
- [/usr/libexec/transitd](MACHOS/transitd)
- [/usr/libexec/transparency-sysdiagnose](MACHOS/transparency-sysdiagnose)
- [/usr/libexec/transparencyStaticKey](MACHOS/transparencyStaticKey)
- [/usr/libexec/transparencyd](MACHOS/transparencyd)
- [/usr/libexec/triald](MACHOS/triald)
- [/usr/libexec/triald_system](MACHOS/triald_system)
- [/usr/libexec/trustd](MACHOS/trustd)
- [/usr/libexec/tursd](MACHOS/tursd)
- [/usr/libexec/tvremoted](MACHOS/tvremoted)
- [/usr/libexec/tzd](MACHOS/tzd)
- [/usr/libexec/tzinit](MACHOS/tzinit)
- [/usr/libexec/tzlinkd](MACHOS/tzlinkd)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd)
- [/usr/libexec/usermanagerhelper](MACHOS/usermanagerhelper)
- [/usr/libexec/videocodecd](MACHOS/videocodecd)
- [/usr/libexec/videosubscriptionsd](MACHOS/videosubscriptionsd)
- [/usr/libexec/wapic](MACHOS/wapic)
- [/usr/libexec/watchdogd](MACHOS/watchdogd)
- [/usr/libexec/watchpresenced](MACHOS/watchpresenced)
- [/usr/libexec/wcd](MACHOS/wcd)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd)
- [/usr/libexec/webinspectord](MACHOS/webinspectord)
- [/usr/libexec/webpushd](MACHOS/webpushd)
- [/usr/libexec/wifiFirmwareLoader](MACHOS/wifiFirmwareLoader)
- [/usr/libexec/wifianalyticsd](MACHOS/wifianalyticsd)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd)
- [/usr/sbin/BTAvrcp](MACHOS/BTAvrcp)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer)
- [/usr/sbin/BTMap](MACHOS/BTMap)
- [/usr/sbin/BTPbap](MACHOS/BTPbap)
- [/usr/sbin/BlueTool](MACHOS/BlueTool)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd)
- [/usr/sbin/absd](MACHOS/absd)
- [/usr/sbin/addNetworkInterface](MACHOS/addNetworkInterface)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad)
- [/usr/sbin/aslmanager](MACHOS/aslmanager)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd)
- [/usr/sbin/cfprefsd](MACHOS/cfprefsd)
- [/usr/sbin/ckksctl](MACHOS/ckksctl)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad)
- [/usr/sbin/distnoted](MACHOS/distnoted)
- [/usr/sbin/fairplayd.H2](MACHOS/fairplayd.H2)
- [/usr/sbin/filecoordinationd](MACHOS/filecoordinationd)
- [/usr/sbin/hdik](MACHOS/hdik)
- [/usr/sbin/ioreg](MACHOS/ioreg)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder)
- [/usr/sbin/mDNSResponderHelper](MACHOS/mDNSResponderHelper)
- [/usr/sbin/notifyd](MACHOS/notifyd)
- [/usr/sbin/nvram](MACHOS/nvram)
- [/usr/sbin/otctl](MACHOS/otctl)
- [/usr/sbin/pppd](MACHOS/pppd)
- [/usr/sbin/racoon](MACHOS/racoon)
- [/usr/sbin/rtadvd](MACHOS/rtadvd)
- [/usr/sbin/spindump](MACHOS/spindump)
- [/usr/sbin/syslogd](MACHOS/syslogd)
- [/usr/sbin/wifid](MACHOS/wifid)

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

#### ❌ Removed (37)

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

#### ⬆️ Updated (3345)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ARKit.axbundle/ARKit](DYLIBS/ARKit)
- [/System/Library/AccessibilityBundles/ARTraceModule.axbundle/ARTraceModule](DYLIBS/ARTraceModule)
- [/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider](DYLIBS/ASMessagesProvider)
- [/System/Library/AccessibilityBundles/AVFoundation.axbundle/AVFoundation](DYLIBS/AVFoundation)
- [/System/Library/AccessibilityBundles/AVKit.axbundle/AVKit](DYLIBS/AVKit)
- [/System/Library/AccessibilityBundles/AXActionSheetUIServer.axuiservice/AXActionSheetUIServer](DYLIBS/AXActionSheetUIServer)
- [/System/Library/AccessibilityBundles/AccessibilitySettings.axbundle/AccessibilitySettings](DYLIBS/AccessibilitySettings)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader)
- [/System/Library/AccessibilityBundles/AccountsUI.axbundle/AccountsUI](DYLIBS/AccountsUI)
- [/System/Library/AccessibilityBundles/AcousticId-Assistant.axbundle/AcousticId-Assistant](DYLIBS/AcousticId-Assistant)
- [/System/Library/AccessibilityBundles/ActionButtonSelector.axbundle/ActionButtonSelector](DYLIBS/ActionButtonSelector)
- [/System/Library/AccessibilityBundles/ActiveSyncSettings.axbundle/ActiveSyncSettings](DYLIBS/ActiveSyncSettings)
- [/System/Library/AccessibilityBundles/ActivityUIServices.axbundle/ActivityUIServices](DYLIBS/ActivityUIServices)
- [/System/Library/AccessibilityBundles/AddressBook-Assistant.axbundle/AddressBook-Assistant](DYLIBS/AddressBook-Assistant)
- [/System/Library/AccessibilityBundles/AddressBookUIFramework.axbundle/AddressBookUIFramework](DYLIBS/AddressBookUIFramework)
- [/System/Library/AccessibilityBundles/AirDrop.axbundle/AirDrop](DYLIBS/AirDrop)
- [/System/Library/AccessibilityBundles/AirDropUI.axbundle/AirDropUI](DYLIBS/AirDropUI)
- [/System/Library/AccessibilityBundles/AirPlayMirroringModule.axbundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule)
- [/System/Library/AccessibilityBundles/AirPortSettings.axbundle/AirPortSettings](DYLIBS/AirPortSettings)
- [/System/Library/AccessibilityBundles/AirTrafficSettings.axbundle/AirTrafficSettings](DYLIBS/AirTrafficSettings)
- [/System/Library/AccessibilityBundles/AmbientUI.axbundle/AmbientUI](DYLIBS/AmbientUI)
- [/System/Library/AccessibilityBundles/Animoji.axbundle/Animoji](DYLIBS/Animoji)
- [/System/Library/AccessibilityBundles/AnnotationKit.axbundle/AnnotationKit](DYLIBS/AnnotationKit)
- [/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension](DYLIBS/AppInstallExtension)
- [/System/Library/AccessibilityBundles/AppPredictionUI.axbundle/AppPredictionUI](DYLIBS/AppPredictionUI)
- [/System/Library/AccessibilityBundles/AppPredictionUIWidget.axbundle/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget)
- [/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore](DYLIBS/AppStore)
- [/System/Library/AccessibilityBundles/AppearanceModule.axbundle/AppearanceModule](DYLIBS/AppearanceModule)
- [/System/Library/AccessibilityBundles/AppleAccountSettings.axbundle/AppleAccountSettings](DYLIBS/AppleAccountSettings)
- [/System/Library/AccessibilityBundles/AppleAccountUI.axbundle/AppleAccountUI](DYLIBS/AppleAccountUI)
- [/System/Library/AccessibilityBundles/AppleMediaServicesUI.axbundle/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI)
- [/System/Library/AccessibilityBundles/AppleTV.axbundle/AppleTV](DYLIBS/AppleTV)
- [/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade](DYLIBS/Arcade)
- [/System/Library/AccessibilityBundles/AssetExplorer.axbundle/AssetExplorer](DYLIBS/AssetExplorer)
- [/System/Library/AccessibilityBundles/AssetViewer.axbundle/AssetViewer](DYLIBS/AssetViewer)
- [/System/Library/AccessibilityBundles/AssistantServices.axbundle/AssistantServices](DYLIBS/AssistantServices)
- [/System/Library/AccessibilityBundles/AssistantUI.axbundle/AssistantUI](DYLIBS/AssistantUI)
- [/System/Library/AccessibilityBundles/AttributionWeeApp.axbundle/AttributionWeeApp](DYLIBS/AttributionWeeApp)
- [/System/Library/AccessibilityBundles/Audio-QuickLook.axbundle/Audio-QuickLook](DYLIBS/Audio-QuickLook)
- [/System/Library/AccessibilityBundles/AuthKitUI.axbundle/AuthKitUI](DYLIBS/AuthKitUI)
- [/System/Library/AccessibilityBundles/AuthenticationServices.axbundle/AuthenticationServices](DYLIBS/AuthenticationServices)
- [/System/Library/AccessibilityBundles/AvatarKit.axbundle/AvatarKit](DYLIBS/AvatarKit)
- [/System/Library/AccessibilityBundles/AvatarPickerMemojiPicker.axbundle/AvatarPickerMemojiPicker](DYLIBS/AvatarPickerMemojiPicker)
- [/System/Library/AccessibilityBundles/AvatarUI.axbundle/AvatarUI](DYLIBS/AvatarUI)
- [/System/Library/AccessibilityBundles/BPSStingSetup.axbundle/BPSStingSetup](DYLIBS/BPSStingSetup)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard)
- [/System/Library/AccessibilityBundles/BannerKit.axbundle/BannerKit](DYLIBS/BannerKit)
- [/System/Library/AccessibilityBundles/BarcodeScanner.axbundle/BarcodeScanner](DYLIBS/BarcodeScanner)
- [/System/Library/AccessibilityBundles/BaseBoardUI.axbundle/BaseBoardUI](DYLIBS/BaseBoardUI)
- [/System/Library/AccessibilityBundles/BatteryCenterUI.axbundle/BatteryCenterUI](DYLIBS/BatteryCenterUI)
- [/System/Library/AccessibilityBundles/BatteryUsageUI.axbundle/BatteryUsageUI](DYLIBS/BatteryUsageUI)
- [/System/Library/AccessibilityBundles/BatteryWidget.axbundle/BatteryWidget](DYLIBS/BatteryWidget)
- [/System/Library/AccessibilityBundles/BiometricKitUI.axbundle/BiometricKitUI](DYLIBS/BiometricKitUI)
- [/System/Library/AccessibilityBundles/BluetoothSettings.axbundle/BluetoothSettings](DYLIBS/BluetoothSettings)
- [/System/Library/AccessibilityBundles/Bridge.axbundle/Bridge](DYLIBS/Bridge)
- [/System/Library/AccessibilityBundles/BridgePreferences.axbundle/BridgePreferences](DYLIBS/BridgePreferences)
- [/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension](DYLIBS/BridgeStoreExtension)
- [/System/Library/AccessibilityBundles/Business.axbundle/Business](DYLIBS/Business)
- [/System/Library/AccessibilityBundles/BusinessChatFramework.axbundle/BusinessChatFramework](DYLIBS/BusinessChatFramework)
- [/System/Library/AccessibilityBundles/CARDNDUI.axbundle/CARDNDUI](DYLIBS/CARDNDUI)
- [/System/Library/AccessibilityBundles/Calculator.axbundle/Calculator](DYLIBS/Calculator)
- [/System/Library/AccessibilityBundles/Calendar-Assistant.axbundle/Calendar-Assistant](DYLIBS/Calendar-Assistant)
- [/System/Library/AccessibilityBundles/Camera.axbundle/Camera](DYLIBS/Camera)
- [/System/Library/AccessibilityBundles/CameraEditKitFramework.axbundle/CameraEditKitFramework](DYLIBS/CameraEditKitFramework)
- [/System/Library/AccessibilityBundles/CameraEffectsKit.axbundle/CameraEffectsKit](DYLIBS/CameraEffectsKit)
- [/System/Library/AccessibilityBundles/CameraKit.axbundle/CameraKit](DYLIBS/CameraKit)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI)
- [/System/Library/AccessibilityBundles/CarModeModule.axbundle/CarModeModule](DYLIBS/CarModeModule)
- [/System/Library/AccessibilityBundles/CarPlay.axbundle/CarPlay](DYLIBS/CarPlay)
- [/System/Library/AccessibilityBundles/CardKit.axbundle/CardKit](DYLIBS/CardKit)
- [/System/Library/AccessibilityBundles/CarouselAppViewSettings.axbundle/CarouselAppViewSettings](DYLIBS/CarouselAppViewSettings)
- [/System/Library/AccessibilityBundles/CertInfo.axbundle/CertInfo](DYLIBS/CertInfo)
- [/System/Library/AccessibilityBundles/ChargingViewService.axbundle/ChargingViewService](DYLIBS/ChargingViewService)
- [/System/Library/AccessibilityBundles/ChatKitAssistantUI-Assistant.axbundle/ChatKitAssistantUI-Assistant](DYLIBS/ChatKitAssistantUI-Assistant)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework)
- [/System/Library/AccessibilityBundles/CheckerBoard.axbundle/CheckerBoard](DYLIBS/CheckerBoard)
- [/System/Library/AccessibilityBundles/ChronoCore.axbundle/ChronoCore](DYLIBS/ChronoCore)
- [/System/Library/AccessibilityBundles/ClipUIServices.axbundle/ClipUIServices](DYLIBS/ClipUIServices)
- [/System/Library/AccessibilityBundles/ClockPoster.axbundle/ClockPoster](DYLIBS/ClockPoster)
- [/System/Library/AccessibilityBundles/CommunicationsSetupUI.axbundle/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI)
- [/System/Library/AccessibilityBundles/CompanionAppViewSetup.axbundle/CompanionAppViewSetup](DYLIBS/CompanionAppViewSetup)
- [/System/Library/AccessibilityBundles/CompanionStingSettings.axbundle/CompanionStingSettings](DYLIBS/CompanionStingSettings)
- [/System/Library/AccessibilityBundles/Compass.axbundle/Compass](DYLIBS/Compass)
- [/System/Library/AccessibilityBundles/CompassViewCalibrationService.axbundle/CompassViewCalibrationService](DYLIBS/CompassViewCalibrationService)
- [/System/Library/AccessibilityBundles/ConnectivityModule.axbundle/ConnectivityModule](DYLIBS/ConnectivityModule)
- [/System/Library/AccessibilityBundles/ContactsAutocompleteUI.axbundle/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI)
- [/System/Library/AccessibilityBundles/ContactsUI.axbundle/ContactsUI](DYLIBS/ContactsUI)
- [/System/Library/AccessibilityBundles/ContinuityDisplay.axbundle/ContinuityDisplay](DYLIBS/ContinuityDisplay)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI)
- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit)
- [/System/Library/AccessibilityBundles/ConversationKit.axbundle/ConversationKit](DYLIBS/ConversationKit)
- [/System/Library/AccessibilityBundles/CoreAuthUI.axbundle/CoreAuthUI](DYLIBS/CoreAuthUI)
- [/System/Library/AccessibilityBundles/CoreCDPUI.axbundle/CoreCDPUI](DYLIBS/CoreCDPUI)
- [/System/Library/AccessibilityBundles/CoreDynamicUIPlugin.axbundle/CoreDynamicUIPlugin](DYLIBS/CoreDynamicUIPlugin)
- [/System/Library/AccessibilityBundles/CoreIDVRGBLiveness.axbundle/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness)
- [/System/Library/AccessibilityBundles/CoreIDVUI.axbundle/CoreIDVUI](DYLIBS/CoreIDVUI)
- [/System/Library/AccessibilityBundles/CoreRecognition.axbundle/CoreRecognition](DYLIBS/CoreRecognition)
- [/System/Library/AccessibilityBundles/CoreSuggestionsUI.axbundle/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI)
- [/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet](DYLIBS/CoverSheet)
- [/System/Library/AccessibilityBundles/CoverSheetKit.axbundle/CoverSheetKit](DYLIBS/CoverSheetKit)
- [/System/Library/AccessibilityBundles/DDActionsService.axbundle/DDActionsService](DYLIBS/DDActionsService)
- [/System/Library/AccessibilityBundles/DataActivation.axbundle/DataActivation](DYLIBS/DataActivation)
- [/System/Library/AccessibilityBundles/DefaultMediaPlayer-QuickLook.axbundle/DefaultMediaPlayer-QuickLook](DYLIBS/DefaultMediaPlayer-QuickLook)
- [/System/Library/AccessibilityBundles/Diagnostics.axbundle/Diagnostics](DYLIBS/Diagnostics)
- [/System/Library/AccessibilityBundles/DictionarySettings.axbundle/DictionarySettings](DYLIBS/DictionarySettings)
- [/System/Library/AccessibilityBundles/DigitalSeparationSettings.axbundle/DigitalSeparationSettings](DYLIBS/DigitalSeparationSettings)
- [/System/Library/AccessibilityBundles/DigitalTouchBalloonProvider.axbundle/DigitalTouchBalloonProvider](DYLIBS/DigitalTouchBalloonProvider)
- [/System/Library/AccessibilityBundles/DigitalTouchShared.axbundle/DigitalTouchShared](DYLIBS/DigitalTouchShared)
- [/System/Library/AccessibilityBundles/DisplayAndBrightnessSettings.axbundle/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings)
- [/System/Library/AccessibilityBundles/DisplayModule.axbundle/DisplayModule](DYLIBS/DisplayModule)
- [/System/Library/AccessibilityBundles/DoNotDisturbModule.axbundle/DoNotDisturbModule](DYLIBS/DoNotDisturbModule)
- [/System/Library/AccessibilityBundles/DoNotDisturbSettings.axbundle/DoNotDisturbSettings](DYLIBS/DoNotDisturbSettings)
- [/System/Library/AccessibilityBundles/DocumentManager.axbundle/DocumentManager](DYLIBS/DocumentManager)
- [/System/Library/AccessibilityBundles/DocumentManagerExecutables.axbundle/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables)
- [/System/Library/AccessibilityBundles/DocumentManagerUICore.axbundle/DocumentManagerUICore](DYLIBS/DocumentManagerUICore)
- [/System/Library/AccessibilityBundles/DrawingKit.axbundle/DrawingKit](DYLIBS/DrawingKit)
- [/System/Library/AccessibilityBundles/EmojiKit.axbundle/EmojiKit](DYLIBS/EmojiKit)
- [/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/EventKitUIFramework](DYLIBS/EventKitUIFramework)
- [/System/Library/AccessibilityBundles/ExposureNotificationSettingsUI.axbundle/ExposureNotificationSettingsUI](DYLIBS/ExposureNotificationSettingsUI)
- [/System/Library/AccessibilityBundles/FMFindingUI.axbundle/FMFindingUI](DYLIBS/FMFindingUI)
- [/System/Library/AccessibilityBundles/FaceTime.axbundle/FaceTime](DYLIBS/FaceTime)
- [/System/Library/AccessibilityBundles/FacebookSettings.axbundle/FacebookSettings](DYLIBS/FacebookSettings)
- [/System/Library/AccessibilityBundles/Files.axbundle/Files](DYLIBS/Files)
- [/System/Library/AccessibilityBundles/FindMy.axbundle/FindMy](DYLIBS/FindMy)
- [/System/Library/AccessibilityBundles/FlashlightModule.axbundle/FlashlightModule](DYLIBS/FlashlightModule)
- [/System/Library/AccessibilityBundles/FlightUtilities.axbundle/FlightUtilities](DYLIBS/FlightUtilities)
- [/System/Library/AccessibilityBundles/FocusUI.axbundle/FocusUI](DYLIBS/FocusUI)
- [/System/Library/AccessibilityBundles/FocusUIModule.axbundle/FocusUIModule](DYLIBS/FocusUIModule)
- [/System/Library/AccessibilityBundles/FontPicker.axbundle/FontPicker](DYLIBS/FontPicker)
- [/System/Library/AccessibilityBundles/FrontBoard.axbundle/FrontBoard](DYLIBS/FrontBoard)
- [/System/Library/AccessibilityBundles/Game Center.axbundle/Game Center](DYLIBS/Game_Center)
- [/System/Library/AccessibilityBundles/GameCenterDashboardExtension.axbundle/GameCenterDashboardExtension](DYLIBS/GameCenterDashboardExtension)
- [/System/Library/AccessibilityBundles/GameCenterPrivateUIFramework.axbundle/GameCenterPrivateUIFramework](DYLIBS/GameCenterPrivateUIFramework)
- [/System/Library/AccessibilityBundles/GameCenterUIFramework.axbundle/GameCenterUIFramework](DYLIBS/GameCenterUIFramework)
- [/System/Library/AccessibilityBundles/GameCenterUIService.axbundle/GameCenterUIService](DYLIBS/GameCenterUIService)
- [/System/Library/AccessibilityBundles/GameKitFramework.axbundle/GameKitFramework](DYLIBS/GameKitFramework)
- [/System/Library/AccessibilityBundles/GeneralKnowledge-Assistant.axbundle/GeneralKnowledge-Assistant](DYLIBS/GeneralKnowledge-Assistant)
- [/System/Library/AccessibilityBundles/GeneralSettingsUI.axbundle/GeneralSettingsUI](DYLIBS/GeneralSettingsUI)
- [/System/Library/AccessibilityBundles/GeoServices.axbundle/GeoServices](DYLIBS/GeoServices)
- [/System/Library/AccessibilityBundles/Gif-QuickLook.axbundle/Gif-QuickLook](DYLIBS/Gif-QuickLook)
- [/System/Library/AccessibilityBundles/HDSViewService.axbundle/HDSViewService](DYLIBS/HDSViewService)
- [/System/Library/AccessibilityBundles/HandwritingProvider.axbundle/HandwritingProvider](DYLIBS/HandwritingProvider)
- [/System/Library/AccessibilityBundles/HashtagImagesExtension.axbundle/HashtagImagesExtension](DYLIBS/HashtagImagesExtension)
- [/System/Library/AccessibilityBundles/HeadphoneConfigs.axbundle/HeadphoneConfigs](DYLIBS/HeadphoneConfigs)
- [/System/Library/AccessibilityBundles/HealthArticlesUI.axbundle/HealthArticlesUI](DYLIBS/HealthArticlesUI)
- [/System/Library/AccessibilityBundles/HealthExperienceUI.axbundle/HealthExperienceUI](DYLIBS/HealthExperienceUI)
- [/System/Library/AccessibilityBundles/HealthExposureNotificationUI.axbundle/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI)
- [/System/Library/AccessibilityBundles/HealthKit.axbundle/HealthKit](DYLIBS/HealthKit)
- [/System/Library/AccessibilityBundles/HealthKitUI.axbundle/HealthKitUI](DYLIBS/HealthKitUI)
- [/System/Library/AccessibilityBundles/HealthMedicationsUI.axbundle/HealthMedicationsUI](DYLIBS/HealthMedicationsUI)
- [/System/Library/AccessibilityBundles/HealthRecordsUI.axbundle/HealthRecordsUI](DYLIBS/HealthRecordsUI)
- [/System/Library/AccessibilityBundles/HealthSafety.axbundle/HealthSafety](DYLIBS/HealthSafety)
- [/System/Library/AccessibilityBundles/HealthToolbox.axbundle/HealthToolbox](DYLIBS/HealthToolbox)
- [/System/Library/AccessibilityBundles/HealthUI.axbundle/HealthUI](DYLIBS/HealthUI)
- [/System/Library/AccessibilityBundles/HealthVisualization.axbundle/HealthVisualization](DYLIBS/HealthVisualization)
- [/System/Library/AccessibilityBundles/HearingAidUIServer.axuiservice/HearingAidUIServer](DYLIBS/HearingAidUIServer)
- [/System/Library/AccessibilityBundles/HeartRhythmUI.axbundle/HeartRhythmUI](DYLIBS/HeartRhythmUI)
- [/System/Library/AccessibilityBundles/HelpKit.axbundle/HelpKit](DYLIBS/HelpKit)
- [/System/Library/AccessibilityBundles/Home.axbundle/Home](DYLIBS/Home)
- [/System/Library/AccessibilityBundles/HomeControlCenterCompactModule.axbundle/HomeControlCenterCompactModule](DYLIBS/HomeControlCenterCompactModule)
- [/System/Library/AccessibilityBundles/HomeControlCenterModule.axbundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule)
- [/System/Library/AccessibilityBundles/HomeControlService.axbundle/HomeControlService](DYLIBS/HomeControlService)
- [/System/Library/AccessibilityBundles/HomeUI.axbundle/HomeUI](DYLIBS/HomeUI)
- [/System/Library/AccessibilityBundles/HomeUIService.axbundle/HomeUIService](DYLIBS/HomeUIService)
- [/System/Library/AccessibilityBundles/Image-QuickLook.axbundle/Image-QuickLook](DYLIBS/Image-QuickLook)
- [/System/Library/AccessibilityBundles/InCallLockScreen.axbundle/InCallLockScreen](DYLIBS/InCallLockScreen)
- [/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService](DYLIBS/InCallService)
- [/System/Library/AccessibilityBundles/IncomingCall.axbundle/IncomingCall](DYLIBS/IncomingCall)
- [/System/Library/AccessibilityBundles/InputUI.axbundle/InputUI](DYLIBS/InputUI)
- [/System/Library/AccessibilityBundles/IntentsUI.axbundle/IntentsUI](DYLIBS/IntentsUI)
- [/System/Library/AccessibilityBundles/InternationalSettings.axbundle/InternationalSettings](DYLIBS/InternationalSettings)
- [/System/Library/AccessibilityBundles/KeyboardSettings.axbundle/KeyboardSettings](DYLIBS/KeyboardSettings)
- [/System/Library/AccessibilityBundles/LinkPresentation.axbundle/LinkPresentation](DYLIBS/LinkPresentation)
- [/System/Library/AccessibilityBundles/LiveTranscriptionUI.axbundle/LiveTranscriptionUI](DYLIBS/LiveTranscriptionUI)
- [/System/Library/AccessibilityBundles/LocalAuthenticationRGBCapture.axbundle/LocalAuthenticationRGBCapture](DYLIBS/LocalAuthenticationRGBCapture)
- [/System/Library/AccessibilityBundles/LocalAuthenticationUI.axbundle/LocalAuthenticationUI](DYLIBS/LocalAuthenticationUI)
- [/System/Library/AccessibilityBundles/LoginUI.axbundle/LoginUI](DYLIBS/LoginUI)
- [/System/Library/AccessibilityBundles/Mail-Assistant.axbundle/Mail-Assistant](DYLIBS/Mail-Assistant)
- [/System/Library/AccessibilityBundles/MailAttachmentPlugin.axbundle/MailAttachmentPlugin](DYLIBS/MailAttachmentPlugin)
- [/System/Library/AccessibilityBundles/MailVIPWidget.axbundle/MailVIPWidget](DYLIBS/MailVIPWidget)
- [/System/Library/AccessibilityBundles/ManagedConfigurationUI.axbundle/ManagedConfigurationUI](DYLIBS/ManagedConfigurationUI)
- [/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework](DYLIBS/MapKitFramework)
- [/System/Library/AccessibilityBundles/MapKitSwiftUI.axbundle/MapKitSwiftUI](DYLIBS/MapKitSwiftUI)
- [/System/Library/AccessibilityBundles/Maps-Assistant.axbundle/Maps-Assistant](DYLIBS/Maps-Assistant)
- [/System/Library/AccessibilityBundles/Maps.axbundle/Maps](DYLIBS/Maps)
- [/System/Library/AccessibilityBundles/MapsUI.axbundle/MapsUI](DYLIBS/MapsUI)
- [/System/Library/AccessibilityBundles/MarkupUI.axbundle/MarkupUI](DYLIBS/MarkupUI)
- [/System/Library/AccessibilityBundles/Measure.axbundle/Measure](DYLIBS/Measure)
- [/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls](DYLIBS/MediaControls)
- [/System/Library/AccessibilityBundles/MediaPlayerFramework.axbundle/MediaPlayerFramework](DYLIBS/MediaPlayerFramework)
- [/System/Library/AccessibilityBundles/MediaPlayerUIFramework.axbundle/MediaPlayerUIFramework](DYLIBS/MediaPlayerUIFramework)
- [/System/Library/AccessibilityBundles/MedicationsHealthAppPlugin.axbundle/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin)
- [/System/Library/AccessibilityBundles/Memories.axbundle/Memories](DYLIBS/Memories)
- [/System/Library/AccessibilityBundles/MenstrualCyclesAppPlugin.axbundle/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin)
- [/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/MessageUIFramework](DYLIBS/MessageUIFramework)
- [/System/Library/AccessibilityBundles/Messages.axbundle/Messages](DYLIBS/Messages)
- [/System/Library/AccessibilityBundles/MessagesFlowDelegatePlugin.axbundle/MessagesFlowDelegatePlugin](DYLIBS/MessagesFlowDelegatePlugin)
- [/System/Library/AccessibilityBundles/MobileCal.axbundle/MobileCal](DYLIBS/MobileCal)
- [/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail](DYLIBS/MobileMail)
- [/System/Library/AccessibilityBundles/MobileMailSettings.axbundle/MobileMailSettings](DYLIBS/MobileMailSettings)
- [/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone](DYLIBS/MobilePhone)
- [/System/Library/AccessibilityBundles/MobileSMS.axbundle/MobileSMS](DYLIBS/MobileSMS)
- [/System/Library/AccessibilityBundles/MobileSafari.axbundle/MobileSafari](DYLIBS/MobileSafari)
- [/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework](DYLIBS/MobileSafariFramework)
- [/System/Library/AccessibilityBundles/MobileSafariSettings.axbundle/MobileSafariSettings](DYLIBS/MobileSafariSettings)
- [/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI](DYLIBS/MobileSafariUI)
- [/System/Library/AccessibilityBundles/MobileSlideShow.axbundle/MobileSlideShow](DYLIBS/MobileSlideShow)
- [/System/Library/AccessibilityBundles/MobileStore.axbundle/MobileStore](DYLIBS/MobileStore)
- [/System/Library/AccessibilityBundles/MobileStoreUI.axbundle/MobileStoreUI](DYLIBS/MobileStoreUI)
- [/System/Library/AccessibilityBundles/MobileTimer-Assistant.axbundle/MobileTimer-Assistant](DYLIBS/MobileTimer-Assistant)
- [/System/Library/AccessibilityBundles/MobileTimer.axbundle/MobileTimer](DYLIBS/MobileTimer)
- [/System/Library/AccessibilityBundles/MobileTimerFramework.axbundle/MobileTimerFramework](DYLIBS/MobileTimerFramework)
- [/System/Library/AccessibilityBundles/MobileTimerUIFramework.axbundle/MobileTimerUIFramework](DYLIBS/MobileTimerUIFramework)
- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments)
- [/System/Library/AccessibilityBundles/MonogramPosterExtension.axbundle/MonogramPosterExtension](DYLIBS/MonogramPosterExtension)
- [/System/Library/AccessibilityBundles/Movie-QuickLook.axbundle/Movie-QuickLook](DYLIBS/Movie-QuickLook)
- [/System/Library/AccessibilityBundles/Movies-Assistant.axbundle/Movies-Assistant](DYLIBS/Movies-Assistant)
- [/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication](DYLIBS/MusicApplication)
- [/System/Library/AccessibilityBundles/MusicMessagesApp.axbundle/MusicMessagesApp](DYLIBS/MusicMessagesApp)
- [/System/Library/AccessibilityBundles/MusicRecognition.axbundle/MusicRecognition](DYLIBS/MusicRecognition)
- [/System/Library/AccessibilityBundles/MusicSettings.axbundle/MusicSettings](DYLIBS/MusicSettings)
- [/System/Library/AccessibilityBundles/MusicUI.axbundle/MusicUI](DYLIBS/MusicUI)
- [/System/Library/AccessibilityBundles/MusicUsage.axbundle/MusicUsage](DYLIBS/MusicUsage)
- [/System/Library/AccessibilityBundles/MuteModule.axbundle/MuteModule](DYLIBS/MuteModule)
- [/System/Library/AccessibilityBundles/NFCControlCenterModule.axbundle/NFCControlCenterModule](DYLIBS/NFCControlCenterModule)
- [/System/Library/AccessibilityBundles/Nearby.axbundle/Nearby](DYLIBS/Nearby)
- [/System/Library/AccessibilityBundles/NotificationCenter.axbundle/NotificationCenter](DYLIBS/NotificationCenter)
- [/System/Library/AccessibilityBundles/NotificationsSettings.axbundle/NotificationsSettings](DYLIBS/NotificationsSettings)
- [/System/Library/AccessibilityBundles/OnBoardingKit.axbundle/OnBoardingKit](DYLIBS/OnBoardingKit)
- [/System/Library/AccessibilityBundles/OpusKit.axbundle/OpusKit](DYLIBS/OpusKit)
- [/System/Library/AccessibilityBundles/OrientationLockModule.axbundle/OrientationLockModule](DYLIBS/OrientationLockModule)
- [/System/Library/AccessibilityBundles/PDFKit.axbundle/PDFKit](DYLIBS/PDFKit)
- [/System/Library/AccessibilityBundles/PaperKit.axbundle/PaperKit](DYLIBS/PaperKit)
- [/System/Library/AccessibilityBundles/PassKitFramework.axbundle/PassKitFramework](DYLIBS/PassKitFramework)
- [/System/Library/AccessibilityBundles/PassKitUI.axbundle/PassKitUI](DYLIBS/PassKitUI)
- [/System/Library/AccessibilityBundles/PassesLockScreenPlugin.axbundle/PassesLockScreenPlugin](DYLIBS/PassesLockScreenPlugin)
- [/System/Library/AccessibilityBundles/PeerPaymentMessagesExtension.axbundle/PeerPaymentMessagesExtension](DYLIBS/PeerPaymentMessagesExtension)
- [/System/Library/AccessibilityBundles/Pegasus.axbundle/Pegasus](DYLIBS/Pegasus)
- [/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit](DYLIBS/PencilKit)
- [/System/Library/AccessibilityBundles/PerformanceTraceModule.axbundle/PerformanceTraceModule](DYLIBS/PerformanceTraceModule)
- [/System/Library/AccessibilityBundles/PhoneCallFlowDelegatePlugin.axbundle/PhoneCallFlowDelegatePlugin](DYLIBS/PhoneCallFlowDelegatePlugin)
- [/System/Library/AccessibilityBundles/Photo Booth.axbundle/Photo Booth](DYLIBS/Photo_Booth)
- [/System/Library/AccessibilityBundles/PhotoLibraryFramework.axbundle/PhotoLibraryFramework](DYLIBS/PhotoLibraryFramework)
- [/System/Library/AccessibilityBundles/PhotoLibraryServices.axbundle/PhotoLibraryServices](DYLIBS/PhotoLibraryServices)
- [/System/Library/AccessibilityBundles/PhotosEditUI.axbundle/PhotosEditUI](DYLIBS/PhotosEditUI)
- [/System/Library/AccessibilityBundles/PhotosFramework.axbundle/PhotosFramework](DYLIBS/PhotosFramework)
- [/System/Library/AccessibilityBundles/PhotosUICore.axbundle/PhotosUICore](DYLIBS/PhotosUICore)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework)
- [/System/Library/AccessibilityBundles/PlatterKit.axbundle/PlatterKit](DYLIBS/PlatterKit)
- [/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts](DYLIBS/Podcasts)
- [/System/Library/AccessibilityBundles/PodcastsPodcastsTodayExtension.axbundle/PodcastsPodcastsTodayExtension](DYLIBS/PodcastsPodcastsTodayExtension)
- [/System/Library/AccessibilityBundles/PosterBoard.axbundle/PosterBoard](DYLIBS/PosterBoard)
- [/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework](DYLIBS/PosterBoardFramework)
- [/System/Library/AccessibilityBundles/PosterKit.axbundle/PosterKit](DYLIBS/PosterKit)
- [/System/Library/AccessibilityBundles/PreBoard.axbundle/PreBoard](DYLIBS/PreBoard)
- [/System/Library/AccessibilityBundles/Preferences.axbundle/Preferences](DYLIBS/Preferences)
- [/System/Library/AccessibilityBundles/PreferencesFramework.axbundle/PreferencesFramework](DYLIBS/PreferencesFramework)
- [/System/Library/AccessibilityBundles/PreferencesUI.axbundle/PreferencesUI](DYLIBS/PreferencesUI)
- [/System/Library/AccessibilityBundles/PreviewUI.axbundle/PreviewUI](DYLIBS/PreviewUI)
- [/System/Library/AccessibilityBundles/PrintKitUI.axbundle/PrintKitUI](DYLIBS/PrintKitUI)
- [/System/Library/AccessibilityBundles/PrivacySettingsUI.axbundle/PrivacySettingsUI](DYLIBS/PrivacySettingsUI)
- [/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension](DYLIBS/ProductPageExtension)
- [/System/Library/AccessibilityBundles/ProxCardKit.axbundle/ProxCardKit](DYLIBS/ProxCardKit)
- [/System/Library/AccessibilityBundles/QuickLook.axbundle/QuickLook](DYLIBS/QuickLook)
- [/System/Library/AccessibilityBundles/QuickSpeak.bundle/QuickSpeak](DYLIBS/QuickSpeak)
- [/System/Library/AccessibilityBundles/QuickTime Plugin.axbundle/QuickTime Plugin](DYLIBS/QuickTime_Plugin)
- [/System/Library/AccessibilityBundles/RealityFoundation.axbundle/RealityFoundation](DYLIBS/RealityFoundation)
- [/System/Library/AccessibilityBundles/RealityKit.axbundle/RealityKit](DYLIBS/RealityKit)
- [/System/Library/AccessibilityBundles/RecentlyPlayedTodayExtension.axbundle/RecentlyPlayedTodayExtension](DYLIBS/RecentlyPlayedTodayExtension)
- [/System/Library/AccessibilityBundles/RecentsAvocado.axbundle/RecentsAvocado](DYLIBS/RecentsAvocado)
- [/System/Library/AccessibilityBundles/RemoteUIFramework.axbundle/RemoteUIFramework](DYLIBS/RemoteUIFramework)
- [/System/Library/AccessibilityBundles/ReplayKitModule.axbundle/ReplayKitModule](DYLIBS/ReplayKitModule)
- [/System/Library/AccessibilityBundles/Restaurants-Assistant.axbundle/Restaurants-Assistant](DYLIBS/Restaurants-Assistant)
- [/System/Library/AccessibilityBundles/SIMSetupSupport.axbundle/SIMSetupSupport](DYLIBS/SIMSetupSupport)
- [/System/Library/AccessibilityBundles/SIMSetupUIService.axbundle/SIMSetupUIService](DYLIBS/SIMSetupUIService)
- [/System/Library/AccessibilityBundles/SOSSettings.axbundle/SOSSettings](DYLIBS/SOSSettings)
- [/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices](DYLIBS/SafariServices)
- [/System/Library/AccessibilityBundles/SafariSharedUI.axbundle/SafariSharedUI](DYLIBS/SafariSharedUI)
- [/System/Library/AccessibilityBundles/SaveToFiles.axbundle/SaveToFiles](DYLIBS/SaveToFiles)
- [/System/Library/AccessibilityBundles/SceneKit.axbundle/SceneKit](DYLIBS/SceneKit)
- [/System/Library/AccessibilityBundles/ScreenTimeSettingsUI.axbundle/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI)
- [/System/Library/AccessibilityBundles/ScreenTimeUI.axbundle/ScreenTimeUI](DYLIBS/ScreenTimeUI)
- [/System/Library/AccessibilityBundles/ScreenshotServicesFramework.axbundle/ScreenshotServicesFramework](DYLIBS/ScreenshotServicesFramework)
- [/System/Library/AccessibilityBundles/ScreenshotServicesService.axbundle/ScreenshotServicesService](DYLIBS/ScreenshotServicesService)
- [/System/Library/AccessibilityBundles/SearchFoundation.axbundle/SearchFoundation](DYLIBS/SearchFoundation)
- [/System/Library/AccessibilityBundles/SearchSettings.axbundle/SearchSettings](DYLIBS/SearchSettings)
- [/System/Library/AccessibilityBundles/SearchUI.axbundle/SearchUI](DYLIBS/SearchUI)
- [/System/Library/AccessibilityBundles/Settings-Assistant.axbundle/Settings-Assistant](DYLIBS/Settings-Assistant)
- [/System/Library/AccessibilityBundles/Setup.axbundle/Setup](DYLIBS/Setup)
- [/System/Library/AccessibilityBundles/SetupAssistantUI.axbundle/SetupAssistantUI](DYLIBS/SetupAssistantUI)
- [/System/Library/AccessibilityBundles/SeymourUI.axbundle/SeymourUI](DYLIBS/SeymourUI)
- [/System/Library/AccessibilityBundles/ShareSheet.axbundle/ShareSheet](DYLIBS/ShareSheet)
- [/System/Library/AccessibilityBundles/SharedWithYouFramework.axbundle/SharedWithYouFramework](DYLIBS/SharedWithYouFramework)
- [/System/Library/AccessibilityBundles/SharingUI.axbundle/SharingUI](DYLIBS/SharingUI)
- [/System/Library/AccessibilityBundles/SharingViewService.axbundle/SharingViewService](DYLIBS/SharingViewService)
- [/System/Library/AccessibilityBundles/Shortcuts.axbundle/Shortcuts](DYLIBS/Shortcuts)
- [/System/Library/AccessibilityBundles/ShortcutsUI.axbundle/ShortcutsUI](DYLIBS/ShortcutsUI)
- [/System/Library/AccessibilityBundles/Sidecar.axbundle/Sidecar](DYLIBS/Sidecar)
- [/System/Library/AccessibilityBundles/Siri.axbundle/Siri](DYLIBS/Siri)
- [/System/Library/AccessibilityBundles/SiriActivation.axbundle/SiriActivation](DYLIBS/SiriActivation)
- [/System/Library/AccessibilityBundles/SiriKitRuntime.axbundle/SiriKitRuntime](DYLIBS/SiriKitRuntime)
- [/System/Library/AccessibilityBundles/SiriSharedUI.axbundle/SiriSharedUI](DYLIBS/SiriSharedUI)
- [/System/Library/AccessibilityBundles/SiriUI.axbundle/SiriUI](DYLIBS/SiriUI)
- [/System/Library/AccessibilityBundles/SiriUICore.axbundle/SiriUICore](DYLIBS/SiriUICore)
- [/System/Library/AccessibilityBundles/Siriland.axbundle/Siriland](DYLIBS/Siriland)
- [/System/Library/AccessibilityBundles/SleepHealthAppPlugin.axbundle/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin)
- [/System/Library/AccessibilityBundles/SleepHealthUI.axbundle/SleepHealthUI](DYLIBS/SleepHealthUI)
- [/System/Library/AccessibilityBundles/SocialFramework.axbundle/SocialFramework](DYLIBS/SocialFramework)
- [/System/Library/AccessibilityBundles/SocialLayer.axbundle/SocialLayer](DYLIBS/SocialLayer)
- [/System/Library/AccessibilityBundles/SocialWeeApp.axbundle/SocialWeeApp](DYLIBS/SocialWeeApp)
- [/System/Library/AccessibilityBundles/SoftwareUpdateSettingsUI.axbundle/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI)
- [/System/Library/AccessibilityBundles/SoundsAndHapticsSettings.axbundle/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings)
- [/System/Library/AccessibilityBundles/Sports-Assistant.axbundle/Sports-Assistant](DYLIBS/Sports-Assistant)
- [/System/Library/AccessibilityBundles/Spotlight.axbundle/Spotlight](DYLIBS/Spotlight)
- [/System/Library/AccessibilityBundles/SpotlightUIInternalFramework.axbundle/SpotlightUIInternalFramework](DYLIBS/SpotlightUIInternalFramework)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard)
- [/System/Library/AccessibilityBundles/SpringBoardFoundation.axbundle/SpringBoardFoundation](DYLIBS/SpringBoardFoundation)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome)
- [/System/Library/AccessibilityBundles/SpringBoardUI.axbundle/SpringBoardUI](DYLIBS/SpringBoardUI)
- [/System/Library/AccessibilityBundles/SpringBoardUIServices.axbundle/SpringBoardUIServices](DYLIBS/SpringBoardUIServices)
- [/System/Library/AccessibilityBundles/SpriteKit.axbundle/SpriteKit](DYLIBS/SpriteKit)
- [/System/Library/AccessibilityBundles/StickersUI.axbundle/StickersUI](DYLIBS/StickersUI)
- [/System/Library/AccessibilityBundles/Stocks-Assistant.axbundle/Stocks-Assistant](DYLIBS/Stocks-Assistant)
- [/System/Library/AccessibilityBundles/StocksFramework.axbundle/StocksFramework](DYLIBS/StocksFramework)
- [/System/Library/AccessibilityBundles/StocksWidget.axbundle/StocksWidget](DYLIBS/StocksWidget)
- [/System/Library/AccessibilityBundles/StorageSettings.axbundle/StorageSettings](DYLIBS/StorageSettings)
- [/System/Library/AccessibilityBundles/StorageSettingsFramework.axbundle/StorageSettingsFramework](DYLIBS/StorageSettingsFramework)
- [/System/Library/AccessibilityBundles/StoreDynamicUIPlugin.axbundle/StoreDynamicUIPlugin](DYLIBS/StoreDynamicUIPlugin)
- [/System/Library/AccessibilityBundles/StoreKitFramework.axbundle/StoreKitFramework](DYLIBS/StoreKitFramework)
- [/System/Library/AccessibilityBundles/StoreKitUI.axbundle/StoreKitUI](DYLIBS/StoreKitUI)
- [/System/Library/AccessibilityBundles/SwiftUI.axbundle/SwiftUI](DYLIBS/SwiftUI)
- [/System/Library/AccessibilityBundles/System-Assistant.axbundle/System-Assistant](DYLIBS/System-Assistant)
- [/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI](DYLIBS/SystemApertureUI)
- [/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/SystemStatusUI](DYLIBS/SystemStatusUI)
- [/System/Library/AccessibilityBundles/TV.axbundle/TV](DYLIBS/TV)
- [/System/Library/AccessibilityBundles/TVMLKit.axbundle/TVMLKit](DYLIBS/TVMLKit)
- [/System/Library/AccessibilityBundles/TVRemoteModule.axbundle/TVRemoteModule](DYLIBS/TVRemoteModule)
- [/System/Library/AccessibilityBundles/TVRemoteUI.axbundle/TVRemoteUI](DYLIBS/TVRemoteUI)
- [/System/Library/AccessibilityBundles/TVRemoteUIService.axbundle/TVRemoteUIService](DYLIBS/TVRemoteUIService)
- [/System/Library/AccessibilityBundles/TelephonyUIFramework.axbundle/TelephonyUIFramework](DYLIBS/TelephonyUIFramework)
- [/System/Library/AccessibilityBundles/TemplateKit.axbundle/TemplateKit](DYLIBS/TemplateKit)
- [/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI](DYLIBS/TextInputUI)
- [/System/Library/AccessibilityBundles/TimerModule.axbundle/TimerModule](DYLIBS/TimerModule)
- [/System/Library/AccessibilityBundles/TipsApp.axbundle/TipsApp](DYLIBS/TipsApp)
- [/System/Library/AccessibilityBundles/TipsNotificationExtension.axbundle/TipsNotificationExtension](DYLIBS/TipsNotificationExtension)
- [/System/Library/AccessibilityBundles/TipsWidgetExtension.axbundle/TipsWidgetExtension](DYLIBS/TipsWidgetExtension)
- [/System/Library/AccessibilityBundles/ToneKit.axbundle/ToneKit](DYLIBS/ToneKit)
- [/System/Library/AccessibilityBundles/Translate.axbundle/Translate](DYLIBS/Translate)
- [/System/Library/AccessibilityBundles/TwitterFramework.axbundle/TwitterFramework](DYLIBS/TwitterFramework)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit)
- [/System/Library/AccessibilityBundles/UpNext.axbundle/UpNext](DYLIBS/UpNext)
- [/System/Library/AccessibilityBundles/UsageSettings.axbundle/UsageSettings](DYLIBS/UsageSettings)
- [/System/Library/AccessibilityBundles/UserNotificationsUI.axbundle/UserNotificationsUI](DYLIBS/UserNotificationsUI)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit)
- [/System/Library/AccessibilityBundles/VectorKit.axbundle/VectorKit](DYLIBS/VectorKit)
- [/System/Library/AccessibilityBundles/VictoriaSettings.axbundle/VictoriaSettings](DYLIBS/VictoriaSettings)
- [/System/Library/AccessibilityBundles/VideoConferenceControlCenterModule.axbundle/VideoConferenceControlCenterModule](DYLIBS/VideoConferenceControlCenterModule)
- [/System/Library/AccessibilityBundles/Videos.axbundle/Videos](DYLIBS/Videos)
- [/System/Library/AccessibilityBundles/VideosExtrasFramework.axbundle/VideosExtrasFramework](DYLIBS/VideosExtrasFramework)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework)
- [/System/Library/AccessibilityBundles/VisionKitCore.axbundle/VisionKitCore](DYLIBS/VisionKitCore)
- [/System/Library/AccessibilityBundles/VoiceShortcutsUI.axbundle/VoiceShortcutsUI](DYLIBS/VoiceShortcutsUI)
- [/System/Library/AccessibilityBundles/VoiceTriggerUI.axbundle/VoiceTriggerUI](DYLIBS/VoiceTriggerUI)
- [/System/Library/AccessibilityBundles/WAAnswer-Assistant.axbundle/WAAnswer-Assistant](DYLIBS/WAAnswer-Assistant)
- [/System/Library/AccessibilityBundles/Wallpaper.axbundle/Wallpaper](DYLIBS/Wallpaper)
- [/System/Library/AccessibilityBundles/WallpaperSettings.axbundle/WallpaperSettings](DYLIBS/WallpaperSettings)
- [/System/Library/AccessibilityBundles/Weather.axbundle/Weather](DYLIBS/Weather)
- [/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore](DYLIBS/WebCore)
- [/System/Library/AccessibilityBundles/WebKit.axbundle/WebKit](DYLIBS/WebKit)
- [/System/Library/AccessibilityBundles/WebKitLegacy.axbundle/WebKitLegacy](DYLIBS/WebKitLegacy)
- [/System/Library/AccessibilityBundles/WebProcess.axbundle/WebProcess](DYLIBS/WebProcess)
- [/System/Library/AccessibilityBundles/WebProcessLoader.axbundle/WebProcessLoader](DYLIBS/WebProcessLoader)
- [/System/Library/AccessibilityBundles/WebUI.axbundle/WebUI](DYLIBS/WebUI)
- [/System/Library/AccessibilityBundles/WiFiKitUI.axbundle/WiFiKitUI](DYLIBS/WiFiKitUI)
- [/System/Library/AccessibilityBundles/WidgetConfigurationExtension.axbundle/WidgetConfigurationExtension](DYLIBS/WidgetConfigurationExtension)
- [/System/Library/AccessibilityBundles/Widgets.axbundle/Widgets](DYLIBS/Widgets)
- [/System/Library/AccessibilityBundles/WirelessModemSettings.axbundle/WirelessModemSettings](DYLIBS/WirelessModemSettings)
- [/System/Library/AccessibilityBundles/WorkflowUI.axbundle/WorkflowUI](DYLIBS/WorkflowUI)
- [/System/Library/AccessibilityBundles/WorkflowUIServices.axbundle/WorkflowUIServices](DYLIBS/WorkflowUIServices)
- [/System/Library/AccessibilityBundles/com.apple.CloudDocsUI.CloudSharing-AppExtension.axbundle/com.apple.CloudDocsUI.CloudSharing-AppExtension](DYLIBS/com.apple.CloudDocsUI.CloudSharing-AppExtension)
- [/System/Library/AccessibilityBundles/com.apple.DocumentManager.Service-AppExtension.axbundle/com.apple.DocumentManager.Service-AppExtension](DYLIBS/com.apple.DocumentManager.Service-AppExtension)
- [/System/Library/AccessibilityBundles/iAdFramework.axbundle/iAdFramework](DYLIBS/iAdFramework)
- [/System/Library/AccessibilityBundles/iCloudDriveApp.axbundle/iCloudDriveApp](DYLIBS/iCloudDriveApp)
- [/System/Library/AccessibilityBundles/iTunesStoreFramework.axbundle/iTunesStoreFramework](DYLIBS/iTunesStoreFramework)
- [/System/Library/AccessibilityBundles/iTunesStoreUIFramework.axbundle/iTunesStoreUIFramework](DYLIBS/iTunesStoreUIFramework)
- [/System/Library/Accounts/Access/CloudKitAccessPlugin.bundle/CloudKitAccessPlugin](DYLIBS/CloudKitAccessPlugin)
- [/System/Library/Accounts/Access/DefaultAccessPlugin.bundle/DefaultAccessPlugin](DYLIBS/DefaultAccessPlugin)
- [/System/Library/Accounts/Access/YelpAccessPlugin.bundle/YelpAccessPlugin](DYLIBS/YelpAccessPlugin)
- [/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication](DYLIBS/AppleIDAuthentication)
- [/System/Library/Accounts/Authentication/AppleIDSSOAuthenticationPlugin.bundle/AppleIDSSOAuthenticationPlugin](DYLIBS/AppleIDSSOAuthenticationPlugin)
- [/System/Library/Accounts/Authentication/CloudKitAuthenticationPlugin.bundle/CloudKitAuthenticationPlugin](DYLIBS/CloudKitAuthenticationPlugin)
- [/System/Library/Accounts/Authentication/DAAccountAuthenticator.bundle/DAAccountAuthenticator](DYLIBS/DAAccountAuthenticator)
- [/System/Library/Accounts/Authentication/ESAccountAuthenticator.bundle/ESAccountAuthenticator](DYLIBS/ESAccountAuthenticator)
- [/System/Library/Accounts/Authentication/GoogleAuthenticationPlugin.bundle/GoogleAuthenticationPlugin](DYLIBS/GoogleAuthenticationPlugin)
- [/System/Library/Accounts/Authentication/KerberosAuthenticationPlugin.bundle/KerberosAuthenticationPlugin](DYLIBS/KerberosAuthenticationPlugin)
- [/System/Library/Accounts/Authentication/MessageAccountAuthenticationPlugin.bundle/MessageAccountAuthenticationPlugin](DYLIBS/MessageAccountAuthenticationPlugin)
- [/System/Library/Accounts/Authentication/YahooAuthenticationPlugin.bundle/YahooAuthenticationPlugin](DYLIBS/YahooAuthenticationPlugin)
- [/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin](DYLIBS/AAAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin](DYLIBS/AADataclassEnableNotificationPlugin)
- [/System/Library/Accounts/Notification/AAIDMSAccountNotificationPlugin.bundle/AAIDMSAccountNotificationPlugin](DYLIBS/AAIDMSAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/ACDatabaseBackupNotificationPlugin.bundle/ACDatabaseBackupNotificationPlugin](DYLIBS/ACDatabaseBackupNotificationPlugin)
- [/System/Library/Accounts/Notification/ADAccountsNotificationPlugin.bundle/ADAccountsNotificationPlugin](DYLIBS/ADAccountsNotificationPlugin)
- [/System/Library/Accounts/Notification/AISAccountNotificationPlugin.bundle/AISAccountNotificationPlugin](DYLIBS/AISAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/AKAccountNotificationPlugin.bundle/AKAccountNotificationPlugin](DYLIBS/AKAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin](DYLIBS/AMSAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/AMSAccountSyncNotificationPlugin.bundle/AMSAccountSyncNotificationPlugin](DYLIBS/AMSAccountSyncNotificationPlugin)
- [/System/Library/Accounts/Notification/ASDAccountNotficationPlugin.bundle/ASDAccountNotficationPlugin](DYLIBS/ASDAccountNotficationPlugin)
- [/System/Library/Accounts/Notification/AppleIDSSONotificationPlugin.bundle/AppleIDSSONotificationPlugin](DYLIBS/AppleIDSSONotificationPlugin)
- [/System/Library/Accounts/Notification/BTCloudPairingAccountNotificationPlugin.bundle/BTCloudPairingAccountNotificationPlugin](DYLIBS/BTCloudPairingAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/CDPAccountNotificationPlugin_IOS.bundle/CDPAccountNotificationPlugin_IOS](DYLIBS/CDPAccountNotificationPlugin_IOS)
- [/System/Library/Accounts/Notification/ClassKitAccountNotificationPlugin.bundle/ClassKitAccountNotificationPlugin](DYLIBS/ClassKitAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/CloudKitNotificationPlugin.bundle/CloudKitNotificationPlugin](DYLIBS/CloudKitNotificationPlugin)
- [/System/Library/Accounts/Notification/CoreIDVAccountNotificationPlugin.bundle/CoreIDVAccountNotificationPlugin](DYLIBS/CoreIDVAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/CoreLocationAccountNotificationPlugin.bundle/CoreLocationAccountNotificationPlugin](DYLIBS/CoreLocationAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/CoreRecentsAccountNotificationPlugin.bundle/CoreRecentsAccountNotificationPlugin](DYLIBS/CoreRecentsAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/CoreRoutineAccountNotificationPlugin.bundle/CoreRoutineAccountNotificationPlugin](DYLIBS/CoreRoutineAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/DAAccountNotifier.bundle/DAAccountNotifier](DYLIBS/DAAccountNotifier)
- [/System/Library/Accounts/Notification/DMDAccountNotificationPlugin.bundle/DMDAccountNotificationPlugin](DYLIBS/DMDAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/DonationAccountWatcher.bundle/DonationAccountWatcher](DYLIBS/DonationAccountWatcher)
- [/System/Library/Accounts/Notification/ESAccountNotifier.bundle/ESAccountNotifier](DYLIBS/ESAccountNotifier)
- [/System/Library/Accounts/Notification/FMFLocatorAccountNotificationPlugin.bundle/FMFLocatorAccountNotificationPlugin](DYLIBS/FMFLocatorAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin](DYLIBS/FindMyDeviceAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/GameCenterAccountNotificationPlugin.bundle/GameCenterAccountNotificationPlugin](DYLIBS/GameCenterAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/HealthKitAccountNotificationPlugin.bundle/HealthKitAccountNotificationPlugin](DYLIBS/HealthKitAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/HomeKitAccountNotificationPlugin.bundle/HomeKitAccountNotificationPlugin](DYLIBS/HomeKitAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/IDSAccountNotificationPlugin.bundle/IDSAccountNotificationPlugin](DYLIBS/IDSAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/IMAccountNotificationPlugin.bundle/IMAccountNotificationPlugin](DYLIBS/IMAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/INDAccountNotificationPlugin.bundle/INDAccountNotificationPlugin](DYLIBS/INDAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification)
- [/System/Library/Accounts/Notification/LockdownModeAccountNotificationPlugin.bundle/LockdownModeAccountNotificationPlugin](DYLIBS/LockdownModeAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/MessageAccountNotificationPlugin.bundle/MessageAccountNotificationPlugin](DYLIBS/MessageAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/MobileSyncAccountNotificationPlugin.bundle/MobileSyncAccountNotificationPlugin](DYLIBS/MobileSyncAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/NewsNotificationPlugin.bundle/NewsNotificationPlugin](DYLIBS/NewsNotificationPlugin)
- [/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/NotesAccountNotificationPlugin](DYLIBS/NotesAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin](DYLIBS/PCSAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/PassbookAccountNotificationPlugin.bundle/PassbookAccountNotificationPlugin](DYLIBS/PassbookAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/PhotosAccountNotificationPlugin.bundle/PhotosAccountNotificationPlugin](DYLIBS/PhotosAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/RPAccountNotificationPlugin.bundle/RPAccountNotificationPlugin](DYLIBS/RPAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/RemindersAccountNotificationPlugin.bundle/RemindersAccountNotificationPlugin](DYLIBS/RemindersAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/SearchPartyAccountNotificationPlugin.bundle/SearchPartyAccountNotificationPlugin](DYLIBS/SearchPartyAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/SecureBackupNotification.bundle/SecureBackupNotification](DYLIBS/SecureBackupNotification)
- [/System/Library/Accounts/Notification/SharingAccountNotificationPlugin.bundle/SharingAccountNotificationPlugin](DYLIBS/SharingAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/ShortcutsCloudKitAccountNotificationPlugin.bundle/ShortcutsCloudKitAccountNotificationPlugin](DYLIBS/ShortcutsCloudKitAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/SiriCloudKitAccountsNotifier.bundle/SiriCloudKitAccountsNotifier](DYLIBS/SiriCloudKitAccountsNotifier)
- [/System/Library/Accounts/Notification/SocialAccountNotificationPlugin.bundle/SocialAccountNotificationPlugin](DYLIBS/SocialAccountNotificationPlugin)
- [/System/Library/Accounts/Notification/WebBookmarksNotificationPlugin.bundle/WebBookmarksNotificationPlugin](DYLIBS/WebBookmarksNotificationPlugin)
- [/System/Library/Accounts/Notification/com.apple.askpermission.AccountNotificationPlugin.bundle/com.apple.askpermission.AccountNotificationPlugin](DYLIBS/com.apple.askpermission.AccountNotificationPlugin)
- [/System/Library/Assistant/Plugins/AssistantTTSPlugin.assistantBundle/AssistantTTSPlugin](DYLIBS/AssistantTTSPlugin)
- [/System/Library/Assistant/Plugins/Calendar.assistantBundle/Calendar](DYLIBS/Calendar)
- [/System/Library/Assistant/Plugins/Contacts.assistantBundle/Contacts](DYLIBS/Contacts)
- [/System/Library/Assistant/Plugins/CorrectionsProfilesSync.assistantBundle/CorrectionsProfilesSync](DYLIBS/CorrectionsProfilesSync)
- [/System/Library/Assistant/Plugins/GEO.assistantBundle/GEO](DYLIBS/GEO)
- [/System/Library/Assistant/Plugins/HMAssistant.assistantBundle/HMAssistant](DYLIBS/HMAssistant)
- [/System/Library/Assistant/Plugins/LocaleSettings.assistantBundle/LocaleSettings](DYLIBS/LocaleSettings)
- [/System/Library/Assistant/Plugins/Media.assistantBundle/Media](DYLIBS/Media)
- [/System/Library/Assistant/Plugins/Phone.assistantBundle/Phone](DYLIBS/Phone)
- [/System/Library/Assistant/Plugins/Podcasts.assistantBundle/Podcasts](DYLIBS/Podcasts)
- [/System/Library/Assistant/Plugins/Routine.assistantBundle/Routine](DYLIBS/Routine)
- [/System/Library/Assistant/Plugins/SurfStatusSync.assistantBundle/SurfStatusSync](DYLIBS/SurfStatusSync)
- [/System/Library/Assistant/Plugins/SynapseSyncPlugin.assistantBundle/SynapseSyncPlugin](DYLIBS/SynapseSyncPlugin)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI)
- [/System/Library/ControlCenter/Bundles/AccessibilityShorcutsModule.bundle/AccessibilityShorcutsModule](DYLIBS/AccessibilityShorcutsModule)
- [/System/Library/ControlCenter/Bundles/AccessibilitySoundDetectionControlCenterModule.bundle/AccessibilitySoundDetectionControlCenterModule](DYLIBS/AccessibilitySoundDetectionControlCenterModule)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule)
- [/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule)
- [/System/Library/ControlCenter/Bundles/AppearanceModule.bundle/AppearanceModule](DYLIBS/AppearanceModule)
- [/System/Library/ControlCenter/Bundles/CameraModule.bundle/CameraModule](DYLIBS/CameraModule)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule)
- [/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule](DYLIBS/DisplayModule)
- [/System/Library/ControlCenter/Bundles/FeedbackAssistantModule.bundle/FeedbackAssistantModule](DYLIBS/FeedbackAssistantModule)
- [/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule](DYLIBS/FlashlightModule)
- [/System/Library/ControlCenter/Bundles/HearingAidsModule.bundle/HearingAidsModule](DYLIBS/HearingAidsModule)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterCompactModule.bundle/HomeControlCenterCompactModule](DYLIBS/HomeControlCenterCompactModule)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule)
- [/System/Library/ControlCenter/Bundles/KeyboardBrightnessModule.bundle/KeyboardBrightnessModule](DYLIBS/KeyboardBrightnessModule)
- [/System/Library/ControlCenter/Bundles/LowPowerModule.bundle/LowPowerModule](DYLIBS/LowPowerModule)
- [/System/Library/ControlCenter/Bundles/MediaControlsAudioModule.bundle/MediaControlsAudioModule](DYLIBS/MediaControlsAudioModule)
- [/System/Library/ControlCenter/Bundles/MediaControlsModule.bundle/MediaControlsModule](DYLIBS/MediaControlsModule)
- [/System/Library/ControlCenter/Bundles/MuteModule.bundle/MuteModule](DYLIBS/MuteModule)
- [/System/Library/ControlCenter/Bundles/OrientationLockModule.bundle/OrientationLockModule](DYLIBS/OrientationLockModule)
- [/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule](DYLIBS/PerformanceTraceModule)
- [/System/Library/ControlCenter/Bundles/QuickNoteModule.bundle/QuickNoteModule](DYLIBS/QuickNoteModule)
- [/System/Library/ControlCenter/Bundles/ShazamModule.bundle/ShazamModule](DYLIBS/ShazamModule)
- [/System/Library/ControlCenter/Bundles/SpokenNotificationsModule.bundle/SpokenNotificationsModule](DYLIBS/SpokenNotificationsModule)
- [/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule](DYLIBS/TVRemoteModule)
- [/System/Library/ControlCenter/Bundles/TimerModule.bundle/TimerModule](DYLIBS/TimerModule)
- [/System/Library/ControlCenter/Bundles/WalletModule.bundle/WalletModule](DYLIBS/WalletModule)
- [/System/Library/CoreAccessories/PlugIns/Features/AssistiveTouch-iOS.feature/AssistiveTouch-iOS](DYLIBS/AssistiveTouch-iOS)
- [/System/Library/CoreAccessories/PlugIns/Features/BLEPairing-iOS.feature/BLEPairing-iOS](DYLIBS/BLEPairing-iOS)
- [/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS](DYLIBS/Communications-iOS)
- [/System/Library/CoreAccessories/PlugIns/Features/HID.feature/HID](DYLIBS/HID)
- [/System/Library/CoreAccessories/PlugIns/Features/MediaLibrary-iOS.feature/MediaLibrary-iOS](DYLIBS/MediaLibrary-iOS)
- [/System/Library/CoreAccessories/PlugIns/Features/Navigation-iOS.feature/Navigation-iOS](DYLIBS/Navigation-iOS)
- [/System/Library/CoreAccessories/PlugIns/Features/NowPlaying-iOS.feature/NowPlaying-iOS](DYLIBS/NowPlaying-iOS)
- [/System/Library/CoreAccessories/PlugIns/Features/OOBBTPairing-iOS.feature/OOBBTPairing-iOS](DYLIBS/OOBBTPairing-iOS)
- [/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit](DYLIBS/IOKit)
- [/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth](DYLIBS/Platform-Bluetooth)
- [/System/Library/CoreAccessories/PlugIns/Platform/System.platform/System](DYLIBS/System)
- [/System/Library/CoreAccessories/PlugIns/Platform/WiFiSharing.platform/WiFiSharing](DYLIBS/WiFiSharing)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager)
- [/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC](DYLIBS/NFC)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost](DYLIBS/USBHost)
- [/System/Library/CoreServices/RawCamera.bundle/RawCamera](DYLIBS/RawCamera)
- [/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount](DYLIBS/DAAccount)
- [/System/Library/DataClassMigrators/FaceTimeMigrator.migrator/FaceTimeMigrator](DYLIBS/FaceTimeMigrator)
- [/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator](DYLIBS/MessagesDataMigrator)
- [/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation](DYLIBS/PasswordsDigitalSeparation)
- [/System/Library/Extensions/AGXGPURawCounterBundle.bundle/AGXGPURawCounterBundle](DYLIBS/AGXGPURawCounterBundle)
- [/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0](DYLIBS/AGXMetalG16P_A0)
- [/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0](DYLIBS/AGXMetalG16P_B0)
- [/System/Library/Extensions/AppleHDQGasGaugeControl.kext/PlugIns/AppleHDQGasGaugeHID.plugin/AppleHDQGasGaugeHID](DYLIBS/AppleHDQGasGaugeHID)
- [/System/Library/Extensions/AppleMetalGLRenderer.bundle/AppleMetalGLRenderer](DYLIBS/AppleMetalGLRenderer)
- [/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID](DYLIBS/MultitouchHID)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/AppleSPULib.plugin/AppleSPULib](DYLIBS/AppleSPULib)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib](DYLIBS/GNSSPassthroughLib)
- [/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib](DYLIBS/IOHIDLib)
- [/System/Library/Extensions/IOUSBDeviceFamily.kext/PlugIns/IOUSBDeviceLib.plugin/IOUSBDeviceLib](DYLIBS/IOUSBDeviceLib)
- [/System/Library/Fitness/Plugins/ActivitySharingAwardsPlugin.bundle/ActivitySharingAwardsPlugin](DYLIBS/ActivitySharingAwardsPlugin)
- [/System/Library/Fitness/Plugins/SeymourAwardsPlugin.bundle/SeymourAwardsPlugin](DYLIBS/SeymourAwardsPlugin)
- [/System/Library/Frameworks/ARKit.framework/ARKit](DYLIBS/ARKit)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio)
- [/System/Library/Frameworks/AVFoundation.framework/AVFoundation](DYLIBS/AVFoundation)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit)
- [/System/Library/Frameworks/AVRouting.framework/AVRouting](DYLIBS/AVRouting)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/Libraries/libCGInterfaces.dylib](DYLIBS/libCGInterfaces.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLinearAlgebra.dylib](DYLIBS/libLinearAlgebra.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libQuadrature.dylib](DYLIBS/libQuadrature.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib](DYLIBS/libSparse.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib](DYLIBS/libvDSP.dylib)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvMisc.dylib](DYLIBS/libvMisc.dylib)
- [/System/Library/Frameworks/Accessibility.framework/Accessibility](DYLIBS/Accessibility)
- [/System/Library/Frameworks/Accounts.framework/Accounts](DYLIBS/Accounts)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit)
- [/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit](DYLIBS/AdAttributionKit)
- [/System/Library/Frameworks/AdServices.framework/AdServices](DYLIBS/AdServices)
- [/System/Library/Frameworks/AdSupport.framework/AdSupport](DYLIBS/AdSupport)
- [/System/Library/Frameworks/AddressBook.framework/AddressBook](DYLIBS/AddressBook)
- [/System/Library/Frameworks/AddressBookUI.framework/AddressBookUI](DYLIBS/AddressBookUI)
- [/System/Library/Frameworks/AppClip.framework/AppClip](DYLIBS/AppClip)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency](DYLIBS/AppTrackingTransparency)
- [/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary](DYLIBS/AssetsLibrary)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib)
- [/System/Library/Frameworks/AudioToolbox.framework/libValidationCapsule.dylib](DYLIBS/libValidationCapsule.dylib)
- [/System/Library/Frameworks/AudioToolbox.framework/libVibeSynthEngine.dylib](DYLIBS/libVibeSynthEngine.dylib)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/AutomatedDeviceEnrollment](DYLIBS/AutomatedDeviceEnrollment)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration](DYLIBS/AutomaticAssessmentConfiguration)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies](DYLIBS/AACDependencies)
- [/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets](DYLIBS/BackgroundAssets)
- [/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks](DYLIBS/BackgroundTasks)
- [/System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore](DYLIBS/BrowserEngineCore)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit)
- [/System/Library/Frameworks/BusinessChat.framework/BusinessChat](DYLIBS/BusinessChat)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit)
- [/System/Library/Frameworks/CarKey.framework/CarKey](DYLIBS/CarKey)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts)
- [/System/Library/Frameworks/Cinematic.framework/Cinematic](DYLIBS/Cinematic)
- [/System/Library/Frameworks/ClassKit.framework/ClassKit](DYLIBS/ClassKit)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit)
- [/System/Library/Frameworks/ColorSync.framework/ColorSync](DYLIBS/ColorSync)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics)
- [/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics](DYLIBS/CoreHaptics)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation)
- [/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI](DYLIBS/CoreLocationUI)
- [/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI](DYLIBS/CoreMIDI)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion)
- [/System/Library/Frameworks/CoreNFC.framework/CoreNFC](DYLIBS/CoreNFC)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCellularDecoders.dylib](DYLIBS/libCellularDecoders.dylib)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterAWDMetrics.dylib](DYLIBS/libCommCenterAWDMetrics.dylib)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCNTargetData.dylib](DYLIBS/libCommCenterCNTargetData.dylib)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText)
- [/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable](DYLIBS/CoreTransferable)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit)
- [/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit](DYLIBS/CryptoTokenKit)
- [/System/Library/Frameworks/DataDetection.framework/DataDetection](DYLIBS/DataDetection)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity)
- [/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck](DYLIBS/DeviceCheck)
- [/System/Library/Frameworks/DeviceDiscoveryExtension.framework/DeviceDiscoveryExtension](DYLIBS/DeviceDiscoveryExtension)
- [/System/Library/Frameworks/DockKit.framework/DockKit](DYLIBS/DockKit)
- [/System/Library/Frameworks/DriverKit.framework/DriverKit](DYLIBS/DriverKit)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI)
- [/System/Library/Frameworks/ExposureNotification.framework/ExposureNotification](DYLIBS/ExposureNotification)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation)
- [/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit](DYLIBS/ExtensionKit)
- [/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory](DYLIBS/ExternalAccessory)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControls](DYLIBS/FamilyControls)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider)
- [/System/Library/Frameworks/FileProviderUI.framework/FileProviderUI](DYLIBS/FileProviderUI)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation)
- [/System/Library/Frameworks/GLKit.framework/GLKit](DYLIBS/GLKit)
- [/System/Library/Frameworks/GSS.framework/GSS](DYLIBS/GSS)
- [/System/Library/Frameworks/GameController.framework/GameController](DYLIBS/GameController)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit)
- [/System/Library/Frameworks/GameplayKit.framework/GameplayKit](DYLIBS/GameplayKit)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit)
- [/System/Library/Frameworks/HealthKitUI.framework/HealthKitUI](DYLIBS/HealthKitUI)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit)
- [/System/Library/Frameworks/IOSurface.framework/IOSurface](DYLIBS/IOSurface)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup)
- [/System/Library/Frameworks/IdentityLookupUI.framework/IdentityLookupUI](DYLIBS/IdentityLookupUI)
- [/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore](DYLIBS/ImageCaptureCore)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents)
- [/System/Library/Frameworks/IntentsUI.framework/IntentsUI](DYLIBS/IntentsUI)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore)
- [/System/Library/Frameworks/JournalingSuggestions.framework/JournalingSuggestions](DYLIBS/JournalingSuggestions)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils](DYLIBS/DaemonUtils)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils)
- [/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI](DYLIBS/LocalAuthenticationEmbeddedUI)
- [/System/Library/Frameworks/MLCompute.framework/MLCompute](DYLIBS/MLCompute)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings](DYLIBS/ManagedSettings)
- [/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI](DYLIBS/ManagedSettingsUI)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter)
- [/System/Library/Frameworks/MatterSupport.framework/MatterSupport](DYLIBS/MatterSupport)
- [/System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility](DYLIBS/MediaAccessibility)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer)
- [/System/Library/Frameworks/MediaSetup.framework/MediaSetup](DYLIBS/MediaSetup)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox)
- [/System/Library/Frameworks/MediaToolbox.framework/Support/libSTS-N.dylib](DYLIBS/libSTS-N.dylib)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI)
- [/System/Library/Frameworks/Messages.framework/Messages](DYLIBS/Messages)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX)
- [/System/Library/Frameworks/MetalKit.framework/MetalKit](DYLIBS/MetalKit)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop](DYLIBS/MPSBenchmarkLoop)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore](DYLIBS/MPSCore)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSFunctions.framework/MPSFunctions](DYLIBS/MPSFunctions)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/MPSImage](DYLIBS/MPSImage)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSMatrix.framework/MPSMatrix](DYLIBS/MPSMatrix)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray](DYLIBS/MPSNDArray)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork](DYLIBS/MPSNeuralNetwork)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/MPSRayIntersector](DYLIBS/MPSRayIntersector)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders](DYLIBS/MetalPerformanceShaders)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph)
- [/System/Library/Frameworks/MetricKit.framework/MetricKit](DYLIBS/MetricKit)
- [/System/Library/Frameworks/ModelIO.framework/ModelIO](DYLIBS/ModelIO)
- [/System/Library/Frameworks/MultipeerConnectivity.framework/MultipeerConnectivity](DYLIBS/MultipeerConnectivity)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit)
- [/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage](DYLIBS/NaturalLanguage)
- [/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction](DYLIBS/NearbyInteraction)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension)
- [/System/Library/Frameworks/NotificationCenter.framework/NotificationCenter](DYLIBS/NotificationCenter)
- [/System/Library/Frameworks/OSLog.framework/OSLog](DYLIBS/OSLog)
- [/System/Library/Frameworks/OpenAL.framework/OpenAL](DYLIBS/OpenAL)
- [/System/Library/Frameworks/OpenGLES.framework/GLEngine.bundle/GLEngine](DYLIBS/GLEngine)
- [/System/Library/Frameworks/OpenGLES.framework/OpenGLES](DYLIBS/OpenGLES)
- [/System/Library/Frameworks/OpenGLES.framework/libCVMSPluginSupport.dylib](DYLIBS/libCVMSPluginSupport.dylib)
- [/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib](DYLIBS/libCoreFSCache.dylib)
- [/System/Library/Frameworks/OpenGLES.framework/libCoreVMClient.dylib](DYLIBS/libCoreVMClient.dylib)
- [/System/Library/Frameworks/OpenGLES.framework/libGFXShared.dylib](DYLIBS/libGFXShared.dylib)
- [/System/Library/Frameworks/OpenGLES.framework/libGLImage.dylib](DYLIBS/libGLImage.dylib)
- [/System/Library/Frameworks/OpenGLES.framework/libGLProgrammability.dylib](DYLIBS/libGLProgrammability.dylib)
- [/System/Library/Frameworks/OpenGLES.framework/libGLVMPlugin.dylib](DYLIBS/libGLVMPlugin.dylib)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit)
- [/System/Library/Frameworks/PHASE.framework/PHASE](DYLIBS/PHASE)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit)
- [/System/Library/Frameworks/PushToTalk.framework/PushToTalk](DYLIBS/PushToTalk)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit)
- [/System/Library/Frameworks/ReplayKit.framework/ReplayKit](DYLIBS/ReplayKit)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices)
- [/System/Library/Frameworks/SafetyKit.framework/SafetyKit](DYLIBS/SafetyKit)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit)
- [/System/Library/Frameworks/ScreenTime.framework/ScreenTime](DYLIBS/ScreenTime)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security)
- [/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis](DYLIBS/SensitiveContentAnalysis)
- [/System/Library/Frameworks/SensorKit.framework/SensorKit](DYLIBS/SensorKit)
- [/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou](DYLIBS/SharedWithYou)
- [/System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore](DYLIBS/SharedWithYouCore)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit)
- [/System/Library/Frameworks/Social.framework/Social](DYLIBS/Social)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech)
- [/System/Library/Frameworks/SpriteKit.framework/SpriteKit](DYLIBS/SpriteKit)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI)
- [/System/Library/Frameworks/Symbols.framework/Symbols](DYLIBS/Symbols)
- [/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration](DYLIBS/SystemConfiguration)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData)
- [/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork](DYLIBS/ThreadNetwork)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit)
- [/System/Library/Frameworks/TipsNext.framework/TipsNext](DYLIBS/TipsNext)
- [/System/Library/Frameworks/Translation.framework/Translation](DYLIBS/Translation)
- [/System/Library/Frameworks/Twitter.framework/Twitter](DYLIBS/Twitter)
- [/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers](DYLIBS/UniformTypeIdentifiers)
- [/System/Library/Frameworks/UserNotifications.framework/UserNotifications](DYLIBS/UserNotifications)
- [/System/Library/Frameworks/UserNotificationsUI.framework/UserNotificationsUI](DYLIBS/UserNotificationsUI)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision)
- [/System/Library/Frameworks/Vision.framework/libfaceCore.dylib](DYLIBS/libfaceCore.dylib)
- [/System/Library/Frameworks/VisionKit.framework/VisionKit](DYLIBS/VisionKit)
- [/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity](DYLIBS/WatchConnectivity)
- [/System/Library/Frameworks/WatchKit.framework/WatchKit](DYLIBS/WatchKit)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit)
- [/System/Library/Frameworks/_AVKit_SwiftUI.framework/_AVKit_SwiftUI](DYLIBS/_AVKit_SwiftUI)
- [/System/Library/Frameworks/_AdAttributionKit_StoreKit.framework/_AdAttributionKit_StoreKit](DYLIBS/_AdAttributionKit_StoreKit)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI)
- [/System/Library/Frameworks/_CoreData_CloudKit.framework/_CoreData_CloudKit](DYLIBS/_CoreData_CloudKit)
- [/System/Library/Frameworks/_CoreLocationUI_SwiftUI.framework/_CoreLocationUI_SwiftUI](DYLIBS/_CoreLocationUI_SwiftUI)
- [/System/Library/Frameworks/_CoreNFC_UIKit.framework/_CoreNFC_UIKit](DYLIBS/_CoreNFC_UIKit)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit)
- [/System/Library/Frameworks/_HomeKit_SwiftUI.framework/_HomeKit_SwiftUI](DYLIBS/_HomeKit_SwiftUI)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI)
- [/System/Library/Frameworks/_QuickLook_SwiftUI.framework/_QuickLook_SwiftUI](DYLIBS/_QuickLook_SwiftUI)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI)
- [/System/Library/Frameworks/_SceneKit_SwiftUI.framework/_SceneKit_SwiftUI](DYLIBS/_SceneKit_SwiftUI)
- [/System/Library/Frameworks/_SpriteKit_SwiftUI.framework/_SpriteKit_SwiftUI](DYLIBS/_SpriteKit_SwiftUI)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI)
- [/System/Library/Frameworks/_SwiftData_CoreData.framework/_SwiftData_CoreData](DYLIBS/_SwiftData_CoreData)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI)
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI)
- [/System/Library/Frameworks/_WorkoutKit_SwiftUI.framework/_WorkoutKit_SwiftUI](DYLIBS/_WorkoutKit_SwiftUI)
- [/System/Library/Frameworks/iAd.framework/iAd](DYLIBS/iAd)
- [/System/Library/HIDPlugins/AppleSPUAccCompassPlugin.plugin/AppleSPUAccCompassPlugin](DYLIBS/AppleSPUAccCompassPlugin)
- [/System/Library/HIDPlugins/AppleSPUDispCompassPlugin.plugin/AppleSPUDispCompassPlugin](DYLIBS/AppleSPUDispCompassPlugin)
- [/System/Library/HIDPlugins/AppleSPUHIDStatistics.plugin/AppleSPUHIDStatistics](DYLIBS/AppleSPUHIDStatistics)
- [/System/Library/HIDPlugins/AttentionAwarenessFilter.plugin/AttentionAwarenessFilter](DYLIBS/AttentionAwarenessFilter)
- [/System/Library/HIDPlugins/IOHIDEventProcessorFilter.plugin/IOHIDEventProcessorFilter](DYLIBS/IOHIDEventProcessorFilter)
- [/System/Library/HIDPlugins/IOHIDEventSystemStatistics.plugin/IOHIDEventSystemStatistics](DYLIBS/IOHIDEventSystemStatistics)
- [/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter](DYLIBS/IOHIDKeyboardFilter)
- [/System/Library/HIDPlugins/IOHIDPointerScrollFilter.plugin/IOHIDPointerScrollFilter](DYLIBS/IOHIDPointerScrollFilter)
- [/System/Library/HIDPlugins/IOHIDT8027USBSessionFilter.plugin/IOHIDT8027USBSessionFilter](DYLIBS/IOHIDT8027USBSessionFilter)
- [/System/Library/HIDPlugins/PearlEventFilter.plugin/PearlEventFilter](DYLIBS/PearlEventFilter)
- [/System/Library/Health/FeedItemPlugins/AppRecommendations.healthplugin/AppRecommendations](DYLIBS/AppRecommendations)
- [/System/Library/Health/FeedItemPlugins/Categories.healthplugin/Categories](DYLIBS/Categories)
- [/System/Library/Health/FeedItemPlugins/HealthArticles.healthplugin/HealthArticles](DYLIBS/HealthArticles)
- [/System/Library/Health/FeedItemPlugins/HealthRecords.healthplugin/HealthRecords](DYLIBS/HealthRecords)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin)
- [/System/Library/Health/FeedItemPlugins/MobilityAppPlugin.healthplugin/MobilityAppPlugin](DYLIBS/MobilityAppPlugin)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles)
- [/System/Library/Health/FeedItemPlugins/ResearchApp.healthplugin/ResearchApp](DYLIBS/ResearchApp)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin)
- [/System/Library/Health/Plugins/ActivityAchievementsPlugin.bundle/ActivityAchievementsPlugin](DYLIBS/ActivityAchievementsPlugin)
- [/System/Library/Health/Plugins/ActivityAwardsPlugin.bundle/ActivityAwardsPlugin](DYLIBS/ActivityAwardsPlugin)
- [/System/Library/Health/Plugins/ActivitySharingPlugin.bundle/ActivitySharingPlugin](DYLIBS/ActivitySharingPlugin)
- [/System/Library/Health/Plugins/CompanionHealthPlugin.bundle/CompanionHealthPlugin](DYLIBS/CompanionHealthPlugin)
- [/System/Library/Health/Plugins/HealthAppPlugin.bundle/HealthAppPlugin](DYLIBS/HealthAppPlugin)
- [/System/Library/Health/Plugins/HeartDaemonPlugin.bundle/HeartDaemonPlugin](DYLIBS/HeartDaemonPlugin)
- [/System/Library/Health/Plugins/MenstrualCyclesDaemonPlugin.bundle/MenstrualCyclesDaemonPlugin](DYLIBS/MenstrualCyclesDaemonPlugin)
- [/System/Library/Health/Plugins/RespiratoryHealthDaemonPlugin.bundle/RespiratoryHealthDaemonPlugin](DYLIBS/RespiratoryHealthDaemonPlugin)
- [/System/Library/Health/Plugins/SleepHealthDaemonPlugin.bundle/SleepHealthDaemonPlugin](DYLIBS/SleepHealthDaemonPlugin)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture)
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime)
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings)
- [/System/Library/NanoTimeKit/ComplicationBundles/MessagesComplication.bundle/MessagesComplication](DYLIBS/MessagesComplication)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications](DYLIBS/NanoCompassComplications)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoMenstrualCyclesComplication.bundle/NanoMenstrualCyclesComplication](DYLIBS/NanoMenstrualCyclesComplication)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoSleepComplication.bundle/NanoSleepComplication](DYLIBS/NanoSleepComplication)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications)
- [/System/Library/NanoTimeKit/ComplicationBundles/WorldClockComplications.bundle/WorldClockComplications](DYLIBS/WorldClockComplications)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAegirFaceBundleCompanion.bundle/NTKAegirFaceBundleCompanion](DYLIBS/NTKAegirFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExtragalacticFaceBundleCompanion.bundle/NTKExtragalacticFaceBundleCompanion](DYLIBS/NTKExtragalacticFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFoghornFaceBundleCompanion.bundle/NTKFoghornFaceBundleCompanion](DYLIBS/NTKFoghornFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGalleonFaceBundleCompanion.bundle/NTKGalleonFaceBundleCompanion](DYLIBS/NTKGalleonFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSnowglobeFaceBundleCompanion.bundle/NTKSnowglobeFaceBundleCompanion](DYLIBS/NTKSnowglobeFaceBundleCompanion)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVivaldiFaceBundleCompanion.bundle/NTKVivaldiFaceBundleCompanion](DYLIBS/NTKVivaldiFaceBundleCompanion)
- [/System/Library/PreferenceBundles/AirPortSettings.bundle/AirPortSettings](DYLIBS/AirPortSettings)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings)
- [/System/Library/PreferenceBundles/CarrierSettings.bundle/CarrierSettings](DYLIBS/CarrierSettings)
- [/System/Library/PreferenceBundles/EDGESettings.bundle/EDGESettings](DYLIBS/EDGESettings)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings)
- [/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings](DYLIBS/MobilePhoneSettings)
- [/System/Library/PreferenceBundles/ScheduleSettings.bundle/ScheduleSettings](DYLIBS/ScheduleSettings)
- [/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences](DYLIBS/VPNPreferences)
- [/System/Library/PreferenceBundles/WirelessModemSettings.bundle/WirelessModemSettings](DYLIBS/WirelessModemSettings)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift)
- [/System/Library/PrivateFrameworks/AACCore.framework/AACCore](DYLIBS/AACCore)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper)
- [/System/Library/PrivateFrameworks/ACCBaker.framework/ACCBaker](DYLIBS/ACCBaker)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation)
- [/System/Library/PrivateFrameworks/ACTFramework.framework/ACTFramework](DYLIBS/ACTFramework)
- [/System/Library/PrivateFrameworks/AFKUser.framework/AFKUser](DYLIBS/AFKUser)
- [/System/Library/PrivateFrameworks/AGXCompilerConnection-S2A8.framework/AGXCompilerConnection-S2A8](DYLIBS/AGXCompilerConnection-S2A8)
- [/System/Library/PrivateFrameworks/AGXCompilerCore-S2A8.framework/AGXCompilerCore-S2A8](DYLIBS/AGXCompilerCore-S2A8)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore)
- [/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter](DYLIBS/AGXGPURawCounter)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams)
- [/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI](DYLIBS/AMPCoreUI)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/libORTools.dylib](DYLIBS/libORTools.dylib)
- [/System/Library/PrivateFrameworks/ANEServices.framework/ANEServices](DYLIBS/ANEServices)
- [/System/Library/PrivateFrameworks/ANSTKit.framework/ANSTKit](DYLIBS/ANSTKit)
- [/System/Library/PrivateFrameworks/AOPHaptics.framework/AOPHaptics](DYLIBS/AOPHaptics)
- [/System/Library/PrivateFrameworks/AOSKit.framework/AOSKit](DYLIBS/AOSKit)
- [/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem](DYLIBS/APConfigurationSystem)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore)
- [/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon](DYLIBS/ARKitDaemon)
- [/System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation](DYLIBS/ARKitFoundation)
- [/System/Library/PrivateFrameworks/ARKitUI.framework/ARKitUI](DYLIBS/ARKitUI)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/ASOctaneSupport](DYLIBS/ASOctaneSupport)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge)
- [/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation](DYLIBS/ATFoundation)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings)
- [/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings](DYLIBS/AUSettings)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/GKSPerformance.framework/GKSPerformance](DYLIBS/GKSPerformance)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ICE.framework/ICE](DYLIBS/ICE)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/LegacyHandle.framework/LegacyHandle](DYLIBS/LegacyHandle)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/SimpleKeyExchange.framework/SimpleKeyExchange](DYLIBS/SimpleKeyExchange)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/snatmap.framework/snatmap](DYLIBS/snatmap)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore)
- [/System/Library/PrivateFrameworks/AXAggregateStatisticsServices.framework/AXAggregateStatisticsServices](DYLIBS/AXAggregateStatisticsServices)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader](DYLIBS/AXAssetLoader)
- [/System/Library/PrivateFrameworks/AXContainerServices.framework/AXContainerServices](DYLIBS/AXContainerServices)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities)
- [/System/Library/PrivateFrameworks/AXElementInteraction.framework/AXElementInteraction](DYLIBS/AXElementInteraction)
- [/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils](DYLIBS/AXFrontBoardUtils)
- [/System/Library/PrivateFrameworks/AXIDSServices.framework/AXIDSServices](DYLIBS/AXIDSServices)
- [/System/Library/PrivateFrameworks/AXLocalizationCaptionService.framework/AXLocalizationCaptionService](DYLIBS/AXLocalizationCaptionService)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities](DYLIBS/AXMediaUtilities)
- [/System/Library/PrivateFrameworks/AXNTKUtilities.framework/AXNTKUtilities](DYLIBS/AXNTKUtilities)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime)
- [/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection](DYLIBS/AXSoundDetection)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI)
- [/System/Library/PrivateFrameworks/AXSpeakFingerManager.framework/AXSpeakFingerManager](DYLIBS/AXSpeakFingerManager)
- [/System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices](DYLIBS/AXSpeechAssetServices)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance)
- [/System/Library/PrivateFrameworks/AXTapToSpeakTime.framework/AXTapToSpeakTime](DYLIBS/AXTapToSpeakTime)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenServices.framework/AXWatchRemoteScreenServices](DYLIBS/AXWatchRemoteScreenServices)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI](DYLIBS/AXWatchRemoteScreenUI)
- [/System/Library/PrivateFrameworks/AccelerateGPU.framework/AccelerateGPU](DYLIBS/AccelerateGPU)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAudit](DYLIBS/AccessibilityAudit)
- [/System/Library/PrivateFrameworks/AccessibilityFocusEngine.framework/AccessibilityFocusEngine](DYLIBS/AccessibilityFocusEngine)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction)
- [/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation](DYLIBS/AccessibilityPlatformTranslation)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/AccessibilityRemoteServices](DYLIBS/AccessibilityRemoteServices)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteUIServices.framework/AccessibilityRemoteUIServices](DYLIBS/AccessibilityRemoteUIServices)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport)
- [/System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI](DYLIBS/AccessibilityUI)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService)
- [/System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared](DYLIBS/AccessibilityUIShared)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities)
- [/System/Library/PrivateFrameworks/AccessibilityUIViewServices.framework/AccessibilityUIViewServices](DYLIBS/AccessibilityUIViewServices)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities)
- [/System/Library/PrivateFrameworks/AccessoryAssistiveTouch.framework/AccessoryAssistiveTouch](DYLIBS/AccessoryAssistiveTouch)
- [/System/Library/PrivateFrameworks/AccessoryAudio.framework/AccessoryAudio](DYLIBS/AccessoryAudio)
- [/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing](DYLIBS/AccessoryBLEPairing)
- [/System/Library/PrivateFrameworks/AccessoryCommunications.framework/AccessoryCommunications](DYLIBS/AccessoryCommunications)
- [/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth](DYLIBS/AccessoryComponentAuth)
- [/System/Library/PrivateFrameworks/AccessoryHID.framework/AccessoryHID](DYLIBS/AccessoryHID)
- [/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary](DYLIBS/AccessoryMediaLibrary)
- [/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation](DYLIBS/AccessoryNavigation)
- [/System/Library/PrivateFrameworks/AccessoryNowPlaying.framework/AccessoryNowPlaying](DYLIBS/AccessoryNowPlaying)
- [/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/AccessoryOOBBTPairing](DYLIBS/AccessoryOOBBTPairing)
- [/System/Library/PrivateFrameworks/AccessoryVoiceOver.framework/AccessoryVoiceOver](DYLIBS/AccessoryVoiceOver)
- [/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim](DYLIBS/AccessoryiAP2Shim)
- [/System/Library/PrivateFrameworks/AccountNotification.framework/AccountNotification](DYLIBS/AccountNotification)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon)
- [/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI](DYLIBS/AccountsUI)
- [/System/Library/PrivateFrameworks/AcousticMaterials.framework/AcousticMaterials](DYLIBS/AcousticMaterials)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal)
- [/System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements](DYLIBS/ActivityAchievements)
- [/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon](DYLIBS/ActivityAchievementsDaemon)
- [/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI](DYLIBS/ActivityAchievementsUI)
- [/System/Library/PrivateFrameworks/ActivityAwardsClient.framework/ActivityAwardsClient](DYLIBS/ActivityAwardsClient)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices)
- [/System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI](DYLIBS/ActivityRingsUI)
- [/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing](DYLIBS/ActivitySharing)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices)
- [/System/Library/PrivateFrameworks/AdCore.framework/AdCore](DYLIBS/AdCore)
- [/System/Library/PrivateFrameworks/AdID.framework/AdID](DYLIBS/AdID)
- [/System/Library/PrivateFrameworks/AdPlatforms.framework/AdPlatforms](DYLIBS/AdPlatforms)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon)
- [/System/Library/PrivateFrameworks/AdPlatformsCommonUI.framework/AdPlatformsCommonUI](DYLIBS/AdPlatformsCommonUI)
- [/System/Library/PrivateFrameworks/AdPlatformsInternal.framework/AdPlatformsInternal](DYLIBS/AdPlatformsInternal)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy)
- [/System/Library/PrivateFrameworks/AdminLite.framework/AdminLite](DYLIBS/AdminLite)
- [/System/Library/PrivateFrameworks/AfibBurden.framework/AfibBurden](DYLIBS/AfibBurden)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary](DYLIBS/AggregateDictionary)
- [/System/Library/PrivateFrameworks/AggregateDictionaryHistory.framework/AggregateDictionaryHistory](DYLIBS/AggregateDictionaryHistory)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit)
- [/System/Library/PrivateFrameworks/AirPlayRoutePrediction.framework/AirPlayRoutePrediction](DYLIBS/AirPlayRoutePrediction)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender)
- [/System/Library/PrivateFrameworks/AirPlaySenderUI.framework/AirPlaySenderUI](DYLIBS/AirPlaySenderUI)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport)
- [/System/Library/PrivateFrameworks/AirPortAssistant.framework/AirPortAssistant](DYLIBS/AirPortAssistant)
- [/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic](DYLIBS/AirTraffic)
- [/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice](DYLIBS/AirTrafficDevice)
- [/System/Library/PrivateFrameworks/AlgosScoreFramework.framework/AlgosScoreFramework](DYLIBS/AlgosScoreFramework)
- [/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit](DYLIBS/AltruisticBodyPoseKit)
- [/System/Library/PrivateFrameworks/Ambient.framework/Ambient](DYLIBS/Ambient)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI](DYLIBS/AmbientUI)
- [/System/Library/PrivateFrameworks/AmbientUIKit.framework/AmbientUIKit](DYLIBS/AmbientUIKit)
- [/System/Library/PrivateFrameworks/AmbientUIServices.framework/AmbientUIServices](DYLIBS/AmbientUIServices)
- [/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit](DYLIBS/AnnotationKit)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D)
- [/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit](DYLIBS/AppConduit)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics](DYLIBS/AppInstallationMetrics)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation](DYLIBS/AppPredictionFoundation)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal)
- [/System/Library/PrivateFrameworks/AppPredictionUI.framework/AppPredictionUI](DYLIBS/AppPredictionUI)
- [/System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation](DYLIBS/AppPredictionUIFoundation)
- [/System/Library/PrivateFrameworks/AppPredictionUIWidget.framework/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget)
- [/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO](DYLIBS/AppSSO)
- [/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore](DYLIBS/AppSSOCore)
- [/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos](DYLIBS/AppSSOKerberos)
- [/System/Library/PrivateFrameworks/AppSSOUI.framework/AppSSOUI](DYLIBS/AppSSOUI)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon)
- [/System/Library/PrivateFrameworks/AppStoreEvalLighthouseUtils.framework/AppStoreEvalLighthouseUtils](DYLIBS/AppStoreEvalLighthouseUtils)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation](DYLIBS/AppStoreFoundation)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays](DYLIBS/AppStoreOverlays)
- [/System/Library/PrivateFrameworks/AppStoreUI.framework/AppStoreUI](DYLIBS/AppStoreUI)
- [/System/Library/PrivateFrameworks/AppStoreUtilities.framework/AppStoreUtilities](DYLIBS/AppStoreUtilities)
- [/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport](DYLIBS/AppSupport)
- [/System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI](DYLIBS/AppSupportUI)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D)
- [/System/Library/PrivateFrameworks/AppleCV3DMOVKit.framework/AppleCV3DMOVKit](DYLIBS/AppleCV3DMOVKit)
- [/System/Library/PrivateFrameworks/AppleCV3DModels.framework/AppleCV3DModels](DYLIBS/AppleCV3DModels)
- [/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA](DYLIBS/AppleCVA)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport)
- [/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater](DYLIBS/AppleConvergedFirmwareUpdater)
- [/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth](DYLIBS/AppleDepth)
- [/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore](DYLIBS/AppleDepthCore)
- [/System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices](DYLIBS/AppleEmbeddedDisplayServices)
- [/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression](DYLIBS/AppleFSCompression)
- [/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate](DYLIBS/AppleFirmwareUpdate)
- [/System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers](DYLIBS/AppleFlatBuffers)
- [/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback](DYLIBS/AppleHIDFeedback)
- [/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport](DYLIBS/AppleHIDTransportSupport)
- [/System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport](DYLIBS/AppleIDAuthSupport)
- [/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication](DYLIBS/AppleIDSSOAuthentication)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG](DYLIBS/AppleJPEG)
- [/System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL](DYLIBS/AppleJPEGXL)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore)
- [/System/Library/PrivateFrameworks/AppleLDAP.framework/AppleLDAP](DYLIBS/AppleLDAP)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery](DYLIBS/AppleMediaDiscovery)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitSupport.framework/AppleMediaServicesKitSupport](DYLIBS/AppleMediaServicesKitSupport)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets)
- [/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity](DYLIBS/AppleMobileFileIntegrity)
- [/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe](DYLIBS/AppleNVMe)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine](DYLIBS/AppleNeuralEngine)
- [/System/Library/PrivateFrameworks/ApplePDPHelper.framework/ApplePDPHelper](DYLIBS/ApplePDPHelper)
- [/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices](DYLIBS/ApplePhotonDetectorServices)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService)
- [/System/Library/PrivateFrameworks/AppleSARHelper.framework/AppleSARHelper](DYLIBS/AppleSARHelper)
- [/System/Library/PrivateFrameworks/AppleSRP.framework/AppleSRP](DYLIBS/AppleSRP)
- [/System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce](DYLIBS/AppleSauce)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit)
- [/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication](DYLIBS/AppleTracingSupportSymbolication)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission)
- [/System/Library/PrivateFrameworks/AskTo.framework/AskTo](DYLIBS/AskTo)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore)
- [/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices](DYLIBS/AssertionServices)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/AssetCacheServices](DYLIBS/AssetCacheServices)
- [/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/AssetCacheServicesExtensions](DYLIBS/AssetCacheServicesExtensions)
- [/System/Library/PrivateFrameworks/AssetExplorer.framework/AssetExplorer](DYLIBS/AssetExplorer)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer)
- [/System/Library/PrivateFrameworks/AssistantCardServiceSupport.framework/AssistantCardServiceSupport](DYLIBS/AssistantCardServiceSupport)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI)
- [/System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal](DYLIBS/AtomicsInternal)
- [/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness](DYLIBS/AttentionAwareness)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal)
- [/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager](DYLIBS/AudioDSPManager)
- [/System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis](DYLIBS/AudioDataAnalysis)
- [/System/Library/PrivateFrameworks/AudioPasscode.framework/AudioPasscode](DYLIBS/AudioPasscode)
- [/System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication](DYLIBS/AudioServerApplication)
- [/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver](DYLIBS/AudioServerDriver)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP](DYLIBS/AudioServerDriverTransports_IOP)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession)
- [/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib](DYLIBS/libSessionUtility.dylib)
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore)
- [/System/Library/PrivateFrameworks/AudioTransportCommon.framework/AudioTransportCommon](DYLIBS/AudioTransportCommon)
- [/System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion](DYLIBS/AudiogramIngestion)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore)
- [/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore](DYLIBS/AutoFillCore)
- [/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI](DYLIBS/AutoFillUI)
- [/System/Library/PrivateFrameworks/AutoLoop.framework/AutoLoop](DYLIBS/AutoLoop)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationMode](DYLIBS/AutomationMode)
- [/System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit](DYLIBS/AvailabilityKit)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/AvatarPersistence](DYLIBS/AvatarPersistence)
- [/System/Library/PrivateFrameworks/AvatarPoster.framework/AvatarPoster](DYLIBS/AvatarPoster)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI](DYLIBS/AvatarUI)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation](DYLIBS/BackBoardHIDEventFoundation)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors](DYLIBS/BackBoardHIDEventProcessors)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices](DYLIBS/BackBoardServices)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks)
- [/System/Library/PrivateFrameworks/BackgroundTaskAgent.framework/BackgroundTaskAgent](DYLIBS/BackgroundTaskAgent)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost)
- [/System/Library/PrivateFrameworks/BagKit.framework/BagKit](DYLIBS/BagKit)
- [/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit](DYLIBS/BannerKit)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/BarcodeSupport](DYLIBS/BarcodeSupport)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard)
- [/System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI](DYLIBS/BaseBoardUI)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper)
- [/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms](DYLIBS/BatteryAlgorithms)
- [/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter](DYLIBS/BatteryCenter)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI)
- [/System/Library/PrivateFrameworks/BehaviorMiner.framework/BehaviorMiner](DYLIBS/BehaviorMiner)
- [/System/Library/PrivateFrameworks/BiomeDSL.framework/BiomeDSL](DYLIBS/BiomeDSL)
- [/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/BiomeFlexibleStorage](DYLIBS/BiomeFlexibleStorage)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams)
- [/System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync](DYLIBS/BiomeSync)
- [/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit](DYLIBS/BiometricKit)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI](DYLIBS/BiometricKitUI)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/Fluid.framework/Fluid](DYLIBS/Fluid)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline](DYLIBS/MTLSpline)
- [/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport](DYLIBS/BiometricSupport)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor)
- [/System/Library/PrivateFrameworks/BluetoothAudio.framework/BluetoothAudio](DYLIBS/BluetoothAudio)
- [/System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager](DYLIBS/BluetoothManager)
- [/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices](DYLIBS/BluetoothServices)
- [/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI](DYLIBS/BluetoothServicesUI)
- [/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices](DYLIBS/BoardServices)
- [/System/Library/PrivateFrameworks/Bom.framework/Bom](DYLIBS/Bom)
- [/System/Library/PrivateFrameworks/BookCoverUtility.framework/BookCoverUtility](DYLIBS/BookCoverUtility)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation)
- [/System/Library/PrivateFrameworks/BookLibrary.framework/BookLibrary](DYLIBS/BookLibrary)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/BookLibraryCore](DYLIBS/BookLibraryCore)
- [/System/Library/PrivateFrameworks/BookUtility.framework/BookUtility](DYLIBS/BookUtility)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation)
- [/System/Library/PrivateFrameworks/BridgeCommons.framework/BridgeCommons](DYLIBS/BridgeCommons)
- [/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences](DYLIBS/BridgePreferences)
- [/System/Library/PrivateFrameworks/BridgeReporting.framework/BridgeReporting](DYLIBS/BridgeReporting)
- [/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl](DYLIBS/BrightnessControl)
- [/System/Library/PrivateFrameworks/BrookDataCollection.framework/BrookDataCollection](DYLIBS/BrookDataCollection)
- [/System/Library/PrivateFrameworks/BrookServices.framework/BrookServices](DYLIBS/BrookServices)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard)
- [/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion](DYLIBS/BulletinDistributorCompanion)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService)
- [/System/Library/PrivateFrameworks/BusinessFoundation.framework/BusinessFoundation](DYLIBS/BusinessFoundation)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices)
- [/System/Library/PrivateFrameworks/BusinessServicesUI.framework/BusinessServicesUI](DYLIBS/BusinessServicesUI)
- [/System/Library/PrivateFrameworks/ButtonResolver.framework/ButtonResolver](DYLIBS/ButtonResolver)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI)
- [/System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary](DYLIBS/CBORLibrary)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/CDDataAccess](DYLIBS/CDDataAccess)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue](DYLIBS/DACoreDAVGlue)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport)
- [/System/Library/PrivateFrameworks/CDDataAccessExpress.framework/CDDataAccessExpress](DYLIBS/CDDataAccessExpress)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics)
- [/System/Library/PrivateFrameworks/CPMLBestShim.framework/CPMLBestShim](DYLIBS/CPMLBestShim)
- [/System/Library/PrivateFrameworks/CPMS.framework/CPMS](DYLIBS/CPMS)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace)
- [/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP](DYLIBS/CVNLP)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete)
- [/System/Library/PrivateFrameworks/CalDAV.framework/CalDAV](DYLIBS/CalDAV)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon](DYLIBS/CalendarDaemon)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase](DYLIBS/CalendarDatabase)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation](DYLIBS/CalendarFoundation)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink)
- [/System/Library/PrivateFrameworks/CalendarMigration.framework/CalendarMigration](DYLIBS/CalendarMigration)
- [/System/Library/PrivateFrameworks/CalendarNotification.framework/CalendarNotification](DYLIBS/CalendarNotification)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit)
- [/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit](DYLIBS/CameraEffectsKit)
- [/System/Library/PrivateFrameworks/CameraKit.framework/CameraKit](DYLIBS/CameraKit)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI)
- [/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork](DYLIBS/CaptiveNetwork)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework)
- [/System/Library/PrivateFrameworks/CarAssetUtils.framework/CarAssetUtils](DYLIBS/CarAssetUtils)
- [/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework](DYLIBS/CarCommandsUIFramework)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices)
- [/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup](DYLIBS/CarPlaySetup)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices)
- [/System/Library/PrivateFrameworks/CardKit.framework/CardKit](DYLIBS/CardKit)
- [/System/Library/PrivateFrameworks/CardServices.framework/CardServices](DYLIBS/CardServices)
- [/System/Library/PrivateFrameworks/Cards.framework/Cards](DYLIBS/Cards)
- [/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices](DYLIBS/CarouselPreferenceServices)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst)
- [/System/Library/PrivateFrameworks/Categories.framework/Categories](DYLIBS/Categories)
- [/System/Library/PrivateFrameworks/Celestial.framework/Celestial](DYLIBS/Celestial)
- [/System/Library/PrivateFrameworks/CellularBridgeUI.framework/CellularBridgeUI](DYLIBS/CellularBridgeUI)
- [/System/Library/PrivateFrameworks/CellularDataDiagnosticsSuite.framework/CellularDataDiagnosticsSuite](DYLIBS/CellularDataDiagnosticsSuite)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager)
- [/System/Library/PrivateFrameworks/CertInfo.framework/CertInfo](DYLIBS/CertInfo)
- [/System/Library/PrivateFrameworks/CertUI.framework/CertUI](DYLIBS/CertUI)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit)
- [/System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices](DYLIBS/CheckerBoardServices)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsSupport.framework/WidgetPreviewsSupport](DYLIBS/WidgetPreviewsSupport)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices)
- [/System/Library/PrivateFrameworks/ChunkingLibrary.framework/ChunkingLibrary](DYLIBS/ChunkingLibrary)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML)
- [/System/Library/PrivateFrameworks/ClarityBoardFoundation.framework/ClarityBoardFoundation](DYLIBS/ClarityBoardFoundation)
- [/System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation](DYLIBS/ClarityFoundation)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/ClassKitUI](DYLIBS/ClassKitUI)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit](DYLIBS/ClassroomKit)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit)
- [/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices](DYLIBS/ClipServices)
- [/System/Library/PrivateFrameworks/ClipUIServices.framework/ClipUIServices](DYLIBS/ClipUIServices)
- [/System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications](DYLIBS/ClockComplications)
- [/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI](DYLIBS/ClockKitUI)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon](DYLIBS/CloudDocsDaemon)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI)
- [/System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode](DYLIBS/CloudKitCode)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon)
- [/System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync](DYLIBS/CloudKitDistributedSync)
- [/System/Library/PrivateFrameworks/CloudMediaServicesInterfaceKit.framework/CloudMediaServicesInterfaceKit](DYLIBS/CloudMediaServicesInterfaceKit)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary)
- [/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices](DYLIBS/CloudPhotoServices)
- [/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation](DYLIBS/CloudRecommendation)
- [/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices](DYLIBS/CloudServices)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/CloudSettings](DYLIBS/CloudSettings)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing](DYLIBS/CloudSharing)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI](DYLIBS/CloudSharingUI)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry](DYLIBS/CloudTelemetry)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools)
- [/System/Library/PrivateFrameworks/CognitiveHealth.framework/CognitiveHealth](DYLIBS/CognitiveHealth)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence)
- [/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore](DYLIBS/CollectionViewCore)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI)
- [/System/Library/PrivateFrameworks/CommonAuth.framework/CommonAuth](DYLIBS/CommonAuth)
- [/System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities](DYLIBS/CommonUtilities)
- [/System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI](DYLIBS/CommunicationSafetySettingsUI)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter](DYLIBS/CommunicationsFilter)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera](DYLIBS/CompanionCamera)
- [/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon](DYLIBS/CompanionHealthDaemon)
- [/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices](DYLIBS/CompanionServices)
- [/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync](DYLIBS/CompanionSync)
- [/System/Library/PrivateFrameworks/CompassUI.framework/CompassUI](DYLIBS/CompassUI)
- [/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay](DYLIBS/ComplicationDisplay)
- [/System/Library/PrivateFrameworks/ConditionInducer.framework/ConditionInducer](DYLIBS/ConditionInducer)
- [/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel](DYLIBS/ConfigurationEngineModel)
- [/System/Library/PrivateFrameworks/ConstantClasses.framework/ConstantClasses](DYLIBS/ConstantClasses)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI)
- [/System/Library/PrivateFrameworks/ContactsAssistantServices.framework/ContactsAssistantServices](DYLIBS/ContactsAssistantServices)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/ContactsDonation](DYLIBS/ContactsDonation)
- [/System/Library/PrivateFrameworks/ContactsDonationFeedback.framework/ContactsDonationFeedback](DYLIBS/ContactsDonationFeedback)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation)
- [/System/Library/PrivateFrameworks/ContactsMetrics.framework/ContactsMetrics](DYLIBS/ContactsMetrics)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore)
- [/System/Library/PrivateFrameworks/ContactsWidgetUI.framework/ContactsWidgetUI](DYLIBS/ContactsWidgetUI)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon)
- [/System/Library/PrivateFrameworks/ContainerManagerSystem.framework/ContainerManagerSystem](DYLIBS/ContainerManagerSystem)
- [/System/Library/PrivateFrameworks/ContainerManagerUser.framework/ContainerManagerUser](DYLIBS/ContainerManagerUser)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit)
- [/System/Library/PrivateFrameworks/ContextKit.framework/ContextKit](DYLIBS/ContextKit)
- [/System/Library/PrivateFrameworks/ContextKitCore.framework/ContextKitCore](DYLIBS/ContextKitCore)
- [/System/Library/PrivateFrameworks/ContextKitExtraction.framework/ContextKitExtraction](DYLIBS/ContextKitExtraction)
- [/System/Library/PrivateFrameworks/ContextKitPrediction.framework/ContextKitPrediction](DYLIBS/ContextKitPrediction)
- [/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync](DYLIBS/ContextSync)
- [/System/Library/PrivateFrameworks/ContextualActionsClient.framework/ContextualActionsClient](DYLIBS/ContextualActionsClient)
- [/System/Library/PrivateFrameworks/ContextualSuggestionClient.framework/ContextualSuggestionClient](DYLIBS/ContextualSuggestionClient)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/ContextualUnderstanding](DYLIBS/ContextualUnderstanding)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/ContinuousDialogManagerService](DYLIBS/ContinuousDialogManagerService)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit)
- [/System/Library/PrivateFrameworks/Coordination.framework/Coordination](DYLIBS/Coordination)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore)
- [/System/Library/PrivateFrameworks/CoreALD.framework/CoreALD](DYLIBS/CoreALD)
- [/System/Library/PrivateFrameworks/CoreAUC.framework/CoreAUC](DYLIBS/CoreAUC)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories](DYLIBS/CoreAccessories)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/CoreAccessoriesFeatures](DYLIBS/CoreAccessoriesFeatures)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics)
- [/System/Library/PrivateFrameworks/CoreAppleCVA.framework/CoreAppleCVA](DYLIBS/CoreAppleCVA)
- [/System/Library/PrivateFrameworks/CoreAutoLayout.framework/CoreAutoLayout](DYLIBS/CoreAutoLayout)
- [/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI](DYLIBS/CoreBluetoothUI)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI)
- [/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal](DYLIBS/CoreCDPUIInternal)
- [/System/Library/PrivateFrameworks/CoreCapture.framework/CoreCapture](DYLIBS/CoreCapture)
- [/System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl](DYLIBS/CoreCaptureControl)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon)
- [/System/Library/PrivateFrameworks/CoreChartSwift.framework/CoreChartSwift](DYLIBS/CoreChartSwift)
- [/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV](DYLIBS/CoreDAV)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext](DYLIBS/CoreDuetContext)
- [/System/Library/PrivateFrameworks/CoreDuetDaemonProtocol.framework/CoreDuetDaemonProtocol](DYLIBS/CoreDuetDaemonProtocol)
- [/System/Library/PrivateFrameworks/CoreDuetSync.framework/CoreDuetSync](DYLIBS/CoreDuetSync)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition)
- [/System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji](DYLIBS/CoreEmoji)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI](DYLIBS/CoreFollowUpUI)
- [/System/Library/PrivateFrameworks/CoreGPS.framework/CoreGPS](DYLIBS/CoreGPS)
- [/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest](DYLIBS/CoreGPSTest)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting)
- [/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred](DYLIBS/CoreIDCred)
- [/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder](DYLIBS/CoreIDCredBuilder)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI)
- [/System/Library/PrivateFrameworks/CoreIK.framework/CoreIK](DYLIBS/CoreIK)
- [/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor](DYLIBS/CoreIndoor)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge)
- [/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf](DYLIBS/CoreLocationProtobuf)
- [/System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay](DYLIBS/CoreLocationReplay)
- [/System/Library/PrivateFrameworks/CoreMaterial.framework/CoreMaterial](DYLIBS/CoreMaterial)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream)
- [/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms](DYLIBS/CoreMotionAlgorithms)
- [/System/Library/PrivateFrameworks/CoreMotionModels.framework/CoreMotionModels](DYLIBS/CoreMotionModels)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP)
- [/System/Library/PrivateFrameworks/CoreNameParser.framework/CoreNameParser](DYLIBS/CoreNameParser)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC)
- [/System/Library/PrivateFrameworks/CoreOCModules.framework/CoreOCModules](DYLIBS/CoreOCModules)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials)
- [/System/Library/PrivateFrameworks/CoreOptimization.framework/CoreOptimization](DYLIBS/CoreOptimization)
- [/System/Library/PrivateFrameworks/CorePDF.framework/CorePDF](DYLIBS/CorePDF)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec)
- [/System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers](DYLIBS/CorePhoneNumbers)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry)
- [/System/Library/PrivateFrameworks/CorePrediction.framework/CorePrediction](DYLIBS/CorePrediction)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/CorePrescriptionLite](DYLIBS/CorePrescriptionLite)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO](DYLIBS/CoreRealityIO)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents](DYLIBS/CoreRecents)
- [/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition](DYLIBS/CoreRecognition)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit)
- [/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite](DYLIBS/CoreRepairLite)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine](DYLIBS/CoreRoutine)
- [/System/Library/PrivateFrameworks/CoreSDB.framework/CoreSDB](DYLIBS/CoreSDB)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG](DYLIBS/CoreSVG)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding)
- [/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal](DYLIBS/CoreServicesInternal)
- [/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore](DYLIBS/CoreServicesStore)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation)
- [/System/Library/PrivateFrameworks/CoreSpeechGazeTracking.framework/CoreSpeechGazeTracking](DYLIBS/CoreSpeechGazeTracking)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals)
- [/System/Library/PrivateFrameworks/CoreSuggestionsML.framework/CoreSuggestionsML](DYLIBS/CoreSuggestionsML)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication](DYLIBS/CoreSymbolication)
- [/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/CoreThemeDefinition](DYLIBS/CoreThemeDefinition)
- [/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread](DYLIBS/CoreThread)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio](DYLIBS/CoreThreadRadio)
- [/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime](DYLIBS/CoreTime)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils)
- [/System/Library/PrivateFrameworks/CoreUtilsExtras.framework/CoreUtilsExtras](DYLIBS/CoreUtilsExtras)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift)
- [/System/Library/PrivateFrameworks/CoreUtilsUI.framework/CoreUtilsUI](DYLIBS/CoreUtilsUI)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi)
- [/System/Library/PrivateFrameworks/Cornobble.framework/Cornobble](DYLIBS/Cornobble)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit)
- [/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport](DYLIBS/CrashReporterSupport)
- [/System/Library/PrivateFrameworks/CrisisResources.framework/CrisisResources](DYLIBS/CrisisResources)
- [/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging](DYLIBS/CryptoKitCBridging)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate)
- [/System/Library/PrivateFrameworks/DAAPKit.framework/DAAPKit](DYLIBS/DAAPKit)
- [/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework](DYLIBS/DAEASOAuthFramework)
- [/System/Library/PrivateFrameworks/DASDaemon.framework/DASDaemon](DYLIBS/DASDaemon)
- [/System/Library/PrivateFrameworks/DASDelegate.framework/DASDelegate](DYLIBS/DASDelegate)
- [/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary](DYLIBS/DEPClientLibrary)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps)
- [/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary](DYLIBS/DMCEnrollmentLibrary)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities)
- [/System/Library/PrivateFrameworks/DRMFoundation.framework/DRMFoundation](DYLIBS/DRMFoundation)
- [/System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing](DYLIBS/DSRemotePairing)
- [/System/Library/PrivateFrameworks/DTXConnectionServices.framework/DTXConnectionServices](DYLIBS/DTXConnectionServices)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation)
- [/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities](DYLIBS/DVTInstrumentsUtilities)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory](DYLIBS/DarwinDirectory)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard)
- [/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess](DYLIBS/DataAccess)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DACardDAV](DYLIBS/DACardDAV)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue](DYLIBS/DACoreDAVGlue)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DAIMAPNotes.framework/DAIMAPNotes](DYLIBS/DAIMAPNotes)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DALDAP](DYLIBS/DALDAP)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DASubCal](DYLIBS/DASubCal)
- [/System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress](DYLIBS/DataAccessExpress)
- [/System/Library/PrivateFrameworks/DataAccessUI.framework/DataAccessUI](DYLIBS/DataAccessUI)
- [/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices](DYLIBS/DataDeliveryServices)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/PlugIns/PhoneNumbers.plugin/PhoneNumbers](DYLIBS/PhoneNumbers)
- [/System/Library/PrivateFrameworks/DataDetectorsNaturalLanguage.framework/DataDetectorsNaturalLanguage](DYLIBS/DataDetectorsNaturalLanguage)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI)
- [/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration](DYLIBS/DataMigration)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/DendriteIngest](DYLIBS/DendriteIngest)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess)
- [/System/Library/PrivateFrameworks/DeviceActivityConductor.framework/DeviceActivityConductor](DYLIBS/DeviceActivityConductor)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal](DYLIBS/DeviceCheckInternal)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore](DYLIBS/DeviceDiscoveryUICore)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement)
- [/System/Library/PrivateFrameworks/DeviceManagementTools.framework/DeviceManagementTools](DYLIBS/DeviceManagementTools)
- [/System/Library/PrivateFrameworks/DeviceOMatic.framework/DeviceOMatic](DYLIBS/DeviceOMatic)
- [/System/Library/PrivateFrameworks/DevicePresence.framework/DevicePresence](DYLIBS/DevicePresence)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/DeviceToDeviceManager](DYLIBS/DeviceToDeviceManager)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions](DYLIBS/DiagnosticExtensions)
- [/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon](DYLIBS/DiagnosticExtensionsDaemon)
- [/System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/DiagnosticLogCollection](DYLIBS/DiagnosticLogCollection)
- [/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest](DYLIBS/DiagnosticRequest)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService)
- [/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit](DYLIBS/DiagnosticsKit)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices)
- [/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport](DYLIBS/DiagnosticsSupport)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices](DYLIBS/DictionaryServices)
- [/System/Library/PrivateFrameworks/DictionaryUI.framework/DictionaryUI](DYLIBS/DictionaryUI)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI)
- [/System/Library/PrivateFrameworks/DigitalTouchShared.framework/DigitalTouchShared](DYLIBS/DigitalTouchShared)
- [/System/Library/PrivateFrameworks/Disembark.framework/Disembark](DYLIBS/Disembark)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI](DYLIBS/DisembarkUI)
- [/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration](DYLIBS/DiskArbitration)
- [/System/Library/PrivateFrameworks/DiskImages.framework/DiskImages](DYLIBS/DiskImages)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation)
- [/System/Library/PrivateFrameworks/DistributedSensing.framework/DistributedSensing](DYLIBS/DistributedSensing)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb](DYLIBS/DoNotDisturb)
- [/System/Library/PrivateFrameworks/DoNotDisturbKit.framework/DoNotDisturbKit](DYLIBS/DoNotDisturbKit)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore)
- [/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera](DYLIBS/DocumentCamera)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding)
- [/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient](DYLIBS/DocumentUnderstandingClient)
- [/System/Library/PrivateFrameworks/DragUI.framework/DragUI](DYLIBS/DragUI)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard)
- [/System/Library/PrivateFrameworks/DrawingKit.framework/DrawingKit](DYLIBS/DrawingKit)
- [/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement](DYLIBS/DriverManagement)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler)
- [/System/Library/PrivateFrameworks/EAFirmwareUpdater.framework/EAFirmwareUpdater](DYLIBS/EAFirmwareUpdater)
- [/System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X](DYLIBS/EAP8021X)
- [/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity](DYLIBS/EDPSecurity)
- [/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe](DYLIBS/EXDisplayPipe)
- [/System/Library/PrivateFrameworks/EasyConfig.framework/EasyConfig](DYLIBS/EasyConfig)
- [/System/Library/PrivateFrameworks/EditScript.framework/EditScript](DYLIBS/EditScript)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email)
- [/System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing](DYLIBS/EmailAddressing)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset](DYLIBS/EmbeddedDataReset)
- [/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService](DYLIBS/EmbeddingService)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts](DYLIBS/EmergencyAlerts)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation)
- [/System/Library/PrivateFrameworks/EmojiKit.framework/EmojiKit](DYLIBS/EmojiKit)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster)
- [/System/Library/PrivateFrameworks/EncoreXPCService.framework/EncoreXPCService](DYLIBS/EncoreXPCService)
- [/System/Library/PrivateFrameworks/Engram.framework/Engram](DYLIBS/Engram)
- [/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState](DYLIBS/EnhancedLoggingState)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso)
- [/System/Library/PrivateFrameworks/Espresso.framework/Frameworks/LoopKitGeneratedKernels.framework/LoopKitGeneratedKernels](DYLIBS/LoopKitGeneratedKernels)
- [/System/Library/PrivateFrameworks/EventKitTCCUI.framework/EventKitTCCUI](DYLIBS/EventKitTCCUI)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/ExchangeSync](DYLIBS/ExchangeSync)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DAEAS](DYLIBS/DAEAS)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/ESDaemonSupport.framework/ESDaemonSupport](DYLIBS/ESDaemonSupport)
- [/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/ExchangeSyncExpress](DYLIBS/ExchangeSyncExpress)
- [/System/Library/PrivateFrameworks/ExposureNotificationDaemon.framework/ExposureNotificationDaemon](DYLIBS/ExposureNotificationDaemon)
- [/System/Library/PrivateFrameworks/EyeRelief.framework/EyeRelief](DYLIBS/EyeRelief)
- [/System/Library/PrivateFrameworks/Eyedropper.framework/Eyedropper](DYLIBS/Eyedropper)
- [/System/Library/PrivateFrameworks/FMCore.framework/FMCore](DYLIBS/FMCore)
- [/System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite](DYLIBS/FMCoreLite)
- [/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI](DYLIBS/FMCoreUI)
- [/System/Library/PrivateFrameworks/FMF.framework/FMF](DYLIBS/FMF)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore)
- [/System/Library/PrivateFrameworks/FMFUI.framework/FMFUI](DYLIBS/FMFUI)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore)
- [/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking](DYLIBS/FMNetworking)
- [/System/Library/PrivateFrameworks/FRC.framework/FRC](DYLIBS/FRC)
- [/System/Library/PrivateFrameworks/FSEvents.framework/FSEvents](DYLIBS/FSEvents)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit)
- [/System/Library/PrivateFrameworks/FTAWD.framework/FTAWD](DYLIBS/FTAWD)
- [/System/Library/PrivateFrameworks/FTClientServices.framework/FTClientServices](DYLIBS/FTClientServices)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI)
- [/System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC](DYLIBS/FamilyControlsObjC)
- [/System/Library/PrivateFrameworks/FamilyNotification.framework/FamilyNotification](DYLIBS/FamilyNotification)
- [/System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags](DYLIBS/FeatureFlags)
- [/System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport](DYLIBS/FeatureFlagsSupport)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger](DYLIBS/FeedbackLogger)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon)
- [/System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry](DYLIBS/FileProviderTelemetry)
- [/System/Library/PrivateFrameworks/FilesActionsUI.framework/FilesActionsUI](DYLIBS/FilesActionsUI)
- [/System/Library/PrivateFrameworks/FinHealth.framework/FinHealth](DYLIBS/FinHealth)
- [/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore](DYLIBS/FinHealthCore)
- [/System/Library/PrivateFrameworks/FinHealthInsights.framework/FinHealthInsights](DYLIBS/FinHealthInsights)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon)
- [/System/Library/PrivateFrameworks/FindMyCrypto.framework/FindMyCrypto](DYLIBS/FindMyCrypto)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice)
- [/System/Library/PrivateFrameworks/FindMyDeviceUI.framework/FindMyDeviceUI](DYLIBS/FindMyDeviceUI)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate)
- [/System/Library/PrivateFrameworks/FindMyLocateObjCWrapper.framework/FindMyLocateObjCWrapper](DYLIBS/FindMyLocateObjCWrapper)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction](DYLIBS/FindMyServerInteraction)
- [/System/Library/PrivateFrameworks/FindMyStorage.framework/FindMyStorage](DYLIBS/FindMyStorage)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore)
- [/System/Library/PrivateFrameworks/FindMyUnsafeAsyncBridging.framework/FindMyUnsafeAsyncBridging](DYLIBS/FindMyUnsafeAsyncBridging)
- [/System/Library/PrivateFrameworks/Fitness.framework/Fitness](DYLIBS/Fitness)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching)
- [/System/Library/PrivateFrameworks/FitnessCoachingCore.framework/FitnessCoachingCore](DYLIBS/FitnessCoachingCore)
- [/System/Library/PrivateFrameworks/FitnessCoachingHealthServices.framework/FitnessCoachingHealthServices](DYLIBS/FitnessCoachingHealthServices)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI)
- [/System/Library/PrivateFrameworks/FlexMusicKit.framework/FlexMusicKit](DYLIBS/FlexMusicKit)
- [/System/Library/PrivateFrameworks/FlightUtilities.framework/FlightUtilities](DYLIBS/FlightUtilities)
- [/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore](DYLIBS/FlightUtilitiesCore)
- [/System/Library/PrivateFrameworks/FlowFrameKit.framework/FlowFrameKit](DYLIBS/FlowFrameKit)
- [/System/Library/PrivateFrameworks/Fluid.framework/Fluid](DYLIBS/Fluid)
- [/System/Library/PrivateFrameworks/Focus.framework/Focus](DYLIBS/Focus)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI)
- [/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI](DYLIBS/FocusUI)
- [/System/Library/PrivateFrameworks/FontServices.framework/FontServices](DYLIBS/FontServices)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib](DYLIBS/libGSFontCache.dylib)
- [/System/Library/PrivateFrameworks/FontServices.framework/libType1Scaler.dylib](DYLIBS/libType1Scaler.dylib)
- [/System/Library/PrivateFrameworks/FontServices.framework/libhvf.dylib](DYLIBS/libhvf.dylib)
- [/System/Library/PrivateFrameworks/FriendKit.framework/FriendKit](DYLIBS/FriendKit)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices)
- [/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker](DYLIBS/FusionTracker)
- [/System/Library/PrivateFrameworks/Futhark.framework/Futhark](DYLIBS/Futhark)
- [/System/Library/PrivateFrameworks/GLTools.framework/GLTools](DYLIBS/GLTools)
- [/System/Library/PrivateFrameworks/GLToolsCore.framework/GLToolsCore](DYLIBS/GLToolsCore)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libComposeFilters.dylib](DYLIBS/libComposeFilters.dylib)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompiler.dylib](DYLIBS/libGPUCompiler.dylib)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerUtils.dylib](DYLIBS/libGPUCompilerUtils.dylib)
- [/System/Library/PrivateFrameworks/GPURawCounter.framework/GPURawCounter](DYLIBS/GPURawCounter)
- [/System/Library/PrivateFrameworks/GPUSupport.framework/libGPUSupportMercury.dylib](DYLIBS/libGPUSupportMercury.dylib)
- [/System/Library/PrivateFrameworks/GPUTools.framework/GPUTools](DYLIBS/GPUTools)
- [/System/Library/PrivateFrameworks/GPUToolsCore.framework/GPUToolsCore](DYLIBS/GPUToolsCore)
- [/System/Library/PrivateFrameworks/GPUToolsPlayback.framework/GPUToolsPlayback](DYLIBS/GPUToolsPlayback)
- [/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport](DYLIBS/GPUToolsTransport)
- [/System/Library/PrivateFrameworks/GPUToolsiOS.framework/GPUToolsiOS](DYLIBS/GPUToolsiOS)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation](DYLIBS/GameControllerFoundation)
- [/System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings](DYLIBS/GameControllerSettings)
- [/System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices](DYLIBS/GameKitServices)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy)
- [/System/Library/PrivateFrameworks/GamePolicyServices.framework/GamePolicyServices](DYLIBS/GamePolicyServices)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage](DYLIBS/GenerationalStorage)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics](DYLIBS/GeoAnalytics)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices)
- [/System/Library/PrivateFrameworks/GeoServicesCore.framework/GeoServicesCore](DYLIBS/GeoServicesCore)
- [/System/Library/PrivateFrameworks/GeoShifter.framework/GeoShifter](DYLIBS/GeoShifter)
- [/System/Library/PrivateFrameworks/GeoUIFramework.framework/GeoUIFramework](DYLIBS/GeoUIFramework)
- [/System/Library/PrivateFrameworks/Geometry.framework/Geometry](DYLIBS/Geometry)
- [/System/Library/PrivateFrameworks/GradientPoster.framework/GradientPoster](DYLIBS/GradientPoster)
- [/System/Library/PrivateFrameworks/GraphVisualizer.framework/GraphVisualizer](DYLIBS/GraphVisualizer)
- [/System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices](DYLIBS/GraphicsServices)
- [/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices](DYLIBS/GridDataServices)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto)
- [/System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices](DYLIBS/H10ISPServices)
- [/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices](DYLIBS/H16ISPServices)
- [/System/Library/PrivateFrameworks/HAENotifications.framework/HAENotifications](DYLIBS/HAENotifications)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing](DYLIBS/HDRProcessing)
- [/System/Library/PrivateFrameworks/HID.framework/HID](DYLIBS/HID)
- [/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics](DYLIBS/HIDAnalytics)
- [/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay](DYLIBS/HIDDisplay)
- [/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences](DYLIBS/HIDPreferences)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment](DYLIBS/HRTFEnrollment)
- [/System/Library/PrivateFrameworks/HSAAuthentication.framework/HSAAuthentication](DYLIBS/HSAAuthentication)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer)
- [/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient](DYLIBS/HangTracerSettingsClient)
- [/System/Library/PrivateFrameworks/Haptics.framework/Haptics](DYLIBS/Haptics)
- [/System/Library/PrivateFrameworks/HardwareDiagnostics.framework/HardwareDiagnostics](DYLIBS/HardwareDiagnostics)
- [/System/Library/PrivateFrameworks/HardwareSupport.framework/HardwareSupport](DYLIBS/HardwareSupport)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs)
- [/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings](DYLIBS/HeadphoneSettings)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms](DYLIBS/HealthAlgorithms)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon](DYLIBS/HealthAppHealthDaemon)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport](DYLIBS/HealthAppHealthDaemonSupport)
- [/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices](DYLIBS/HealthAppServices)
- [/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration](DYLIBS/HealthArticlesGeneration)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon)
- [/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation](DYLIBS/HealthDaemonFoundation)
- [/System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/HealthDiagnosticExtensionCore](DYLIBS/HealthDiagnosticExtensionCore)
- [/System/Library/PrivateFrameworks/HealthDomainsTools.framework/HealthDomainsTools](DYLIBS/HealthDomainsTools)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI)
- [/System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing](DYLIBS/HealthHearing)
- [/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon](DYLIBS/HealthHearingDaemon)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions)
- [/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications](DYLIBS/HealthMedications)
- [/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin](DYLIBS/HealthMedicationsDaemonPlugin)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI)
- [/System/Library/PrivateFrameworks/HealthMedicationsVision.framework/HealthMedicationsVision](DYLIBS/HealthMedicationsVision)
- [/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI](DYLIBS/HealthMedicationsVisionUI)
- [/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI](DYLIBS/HealthMedicationsWidgetUI)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesUI.framework/HealthMenstrualCyclesUI](DYLIBS/HealthMenstrualCyclesUI)
- [/System/Library/PrivateFrameworks/HealthMobility.framework/HealthMobility](DYLIBS/HealthMobility)
- [/System/Library/PrivateFrameworks/HealthMobilityDaemon.framework/HealthMobilityDaemon](DYLIBS/HealthMobilityDaemon)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices)
- [/System/Library/PrivateFrameworks/HealthRecordsConceptsSupport.framework/HealthRecordsConceptsSupport](DYLIBS/HealthRecordsConceptsSupport)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI)
- [/System/Library/PrivateFrameworks/HealthRecordsWalletSupport.framework/HealthRecordsWalletSupport](DYLIBS/HealthRecordsWalletSupport)
- [/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox](DYLIBS/HealthToolbox)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization)
- [/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore](DYLIBS/HearingCore)
- [/System/Library/PrivateFrameworks/HearingMLHelper.framework/HearingMLHelper](DYLIBS/HearingMLHelper)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities)
- [/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth](DYLIBS/HeartHealth)
- [/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon](DYLIBS/HeartHealthDaemon)
- [/System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI](DYLIBS/HeartRhythmUI)
- [/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal](DYLIBS/Heimdal)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit)
- [/System/Library/PrivateFrameworks/HeroDataClient.framework/HeroDataClient](DYLIBS/HeroDataClient)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home)
- [/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI](DYLIBS/HomeAI)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal)
- [/System/Library/PrivateFrameworks/HomeCommunicationUIFramework.framework/HomeCommunicationUIFramework](DYLIBS/HomeCommunicationUIFramework)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI)
- [/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore](DYLIBS/HomeKitBackingStore)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy)
- [/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter](DYLIBS/HomeKitEventRouter)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents)
- [/System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures](DYLIBS/HomeKitFeatures)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics)
- [/System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils](DYLIBS/HomeMessagingUtils)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings)
- [/System/Library/PrivateFrameworks/HomeRecommendationEngine.framework/HomeRecommendationEngine](DYLIBS/HomeRecommendationEngine)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices)
- [/System/Library/PrivateFrameworks/HomeSharing.framework/HomeSharing](DYLIBS/HomeSharing)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices)
- [/System/Library/PrivateFrameworks/HoverTextServices.framework/HoverTextServices](DYLIBS/HoverTextServices)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation)
- [/System/Library/PrivateFrameworks/IAP.framework/IAP](DYLIBS/IAP)
- [/System/Library/PrivateFrameworks/IAPAuthentication.framework/IAPAuthentication](DYLIBS/IAPAuthentication)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/IDSBlastDoorSupport](DYLIBS/IDSBlastDoorSupport)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation)
- [/System/Library/PrivateFrameworks/IDSHashPersistence.framework/IDSHashPersistence](DYLIBS/IDSHashPersistence)
- [/System/Library/PrivateFrameworks/IDSKVStore.framework/IDSKVStore](DYLIBS/IDSKVStore)
- [/System/Library/PrivateFrameworks/IMAVCore.framework/IMAVCore](DYLIBS/IMAVCore)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore)
- [/System/Library/PrivateFrameworks/IMCorePipeline.framework/IMCorePipeline](DYLIBS/IMCorePipeline)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/IMDMessageServices](DYLIBS/IMDMessageServices)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation](DYLIBS/IMFoundation)
- [/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI](DYLIBS/IMSharedUI)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/IMTranscoding](DYLIBS/IMTranscoding)
- [/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent](DYLIBS/IMTransferAgent)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferServices](DYLIBS/IMTransferServices)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211)
- [/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo](DYLIBS/IOAccelMemoryInfo)
- [/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator](DYLIBS/IOAccelerator)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager](DYLIBS/IOAccessoryManager)
- [/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU](DYLIBS/IOGPU)
- [/System/Library/PrivateFrameworks/IOImageLoader.framework/IOImageLoader](DYLIBS/IOImageLoader)
- [/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten](DYLIBS/IOKitten)
- [/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer](DYLIBS/IOMobileFramebuffer)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator](DYLIBS/IOSurfaceAccelerator)
- [/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost](DYLIBS/IOUSBHost)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib)
- [/System/Library/PrivateFrameworks/ITMLKit.framework/ITMLKit](DYLIBS/ITMLKit)
- [/System/Library/PrivateFrameworks/IXATestAppRelay.framework/IXATestAppRelay](DYLIBS/IXATestAppRelay)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices)
- [/System/Library/PrivateFrameworks/IdleTimerHosting.framework/IdleTimerHosting](DYLIBS/IdleTimerHosting)
- [/System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices](DYLIBS/IdleTimerServices)
- [/System/Library/PrivateFrameworks/ImageHarmonizationKit.framework/ImageHarmonizationKit](DYLIBS/ImageHarmonizationKit)
- [/System/Library/PrivateFrameworks/InAppMessages.framework/InAppMessages](DYLIBS/InAppMessages)
- [/System/Library/PrivateFrameworks/InAppMessagesCore.framework/InAppMessagesCore](DYLIBS/InAppMessagesCore)
- [/System/Library/PrivateFrameworks/IncomingCallFilter.framework/IncomingCallFilter](DYLIBS/IncomingCallFilter)
- [/System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam](DYLIBS/InertiaCam)
- [/System/Library/PrivateFrameworks/InfoQueryPersonalizationFeatures.framework/InfoQueryPersonalizationFeatures](DYLIBS/InfoQueryPersonalizationFeatures)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics)
- [/System/Library/PrivateFrameworks/InputContext.framework/InputContext](DYLIBS/InputContext)
- [/System/Library/PrivateFrameworks/InputTranscoder.framework/InputTranscoder](DYLIBS/InputTranscoder)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination](DYLIBS/InstallCoordination)
- [/System/Library/PrivateFrameworks/InstallProgress.framework/InstallProgress](DYLIBS/InstallProgress)
- [/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary](DYLIBS/InstalledContentLibrary)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/IntelligencePlatformCompute](DYLIBS/IntelligencePlatformCompute)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary)
- [/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting](DYLIBS/IntelligentRouting)
- [/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon](DYLIBS/IntelligentRoutingDaemon)
- [/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore](DYLIBS/IntentsCore)
- [/System/Library/PrivateFrameworks/IntentsFoundation.framework/IntentsFoundation](DYLIBS/IntentsFoundation)
- [/System/Library/PrivateFrameworks/IntentsServices.framework/IntentsServices](DYLIBS/IntentsServices)
- [/System/Library/PrivateFrameworks/IntentsUICardKitProviderSupport.framework/IntentsUICardKitProviderSupport](DYLIBS/IntentsUICardKitProviderSupport)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport)
- [/System/Library/PrivateFrameworks/InternationalTextSearch.framework/InternationalTextSearch](DYLIBS/InternationalTextSearch)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences](DYLIBS/IntlPreferences)
- [/System/Library/PrivateFrameworks/IntlPreferencesUI.framework/IntlPreferencesUI](DYLIBS/IntlPreferencesUI)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient)
- [/System/Library/PrivateFrameworks/JITAppKit.framework/JITAppKit](DYLIBS/JITAppKit)
- [/System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth](DYLIBS/JasperDepth)
- [/System/Library/PrivateFrameworks/Jet.framework/Jet](DYLIBS/Jet)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine)
- [/System/Library/PrivateFrameworks/JetPack.framework/JetPack](DYLIBS/JetPack)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI)
- [/System/Library/PrivateFrameworks/JoinRequests.framework/JoinRequests](DYLIBS/JoinRequests)
- [/System/Library/PrivateFrameworks/KRExperiments.framework/KRExperiments](DYLIBS/KRExperiments)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter)
- [/System/Library/PrivateFrameworks/KeyboardServices.framework/KeyboardServices](DYLIBS/KeyboardServices)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor)
- [/System/Library/PrivateFrameworks/Koa.framework/Koa](DYLIBS/Koa)
- [/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper](DYLIBS/KoaMapper)
- [/System/Library/PrivateFrameworks/LACC.framework/LACC](DYLIBS/LACC)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling)
- [/System/Library/PrivateFrameworks/LatentSemanticMapping.framework/LatentSemanticMapping](DYLIBS/LatentSemanticMapping)
- [/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures](DYLIBS/LearnedFeatures)
- [/System/Library/PrivateFrameworks/LegacyGameKit.framework/LegacyGameKit](DYLIBS/LegacyGameKit)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground)
- [/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework](DYLIBS/LighthouseBitacoraFramework)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore](DYLIBS/LighthouseCoreMLFeatureStore)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLModelAnalysis.framework/LighthouseCoreMLModelAnalysis](DYLIBS/LighthouseCoreMLModelAnalysis)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/LighthouseCoreMLModelStore](DYLIBS/LighthouseCoreMLModelStore)
- [/System/Library/PrivateFrameworks/LighthouseDictation.framework/LighthouseDictation](DYLIBS/LighthouseDictation)
- [/System/Library/PrivateFrameworks/LighthouseModelMonitoring.framework/LighthouseModelMonitoring](DYLIBS/LighthouseModelMonitoring)
- [/System/Library/PrivateFrameworks/LighthouseQuartz.framework/LighthouseQuartz](DYLIBS/LighthouseQuartz)
- [/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking](DYLIBS/LimitAdTracking)
- [/System/Library/PrivateFrameworks/LinguisticData.framework/LinguisticData](DYLIBS/LinguisticData)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsFoundation.framework/LiveExecutionResultsFoundation](DYLIBS/LiveExecutionResultsFoundation)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsRuntime.framework/LiveExecutionResultsRuntime](DYLIBS/LiveExecutionResultsRuntime)
- [/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS](DYLIBS/LiveFS)
- [/System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper](DYLIBS/LiveFSFPHelper)
- [/System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices](DYLIBS/LiveSpeechServices)
- [/System/Library/PrivateFrameworks/LiveSpeechUI.framework/LiveSpeechUI](DYLIBS/LiveSpeechUI)
- [/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription](DYLIBS/LiveTranscription)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI)
- [/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI](DYLIBS/LocalAuthenticationPrivateUI)
- [/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge](DYLIBS/LocalSpeechRecognitionBridge)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit](DYLIBS/LocalStatusKit)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode](DYLIBS/LockdownMode)
- [/System/Library/PrivateFrameworks/LockoutUI.framework/LockoutUI](DYLIBS/LockoutUI)
- [/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport](DYLIBS/LoggingSupport)
- [/System/Library/PrivateFrameworks/LoginKit.framework/LoginKit](DYLIBS/LoginKit)
- [/System/Library/PrivateFrameworks/LoginPerformanceKit.framework/LoginPerformanceKit](DYLIBS/LoginPerformanceKit)
- [/System/Library/PrivateFrameworks/LoginUILogViewer.framework/LoginUILogViewer](DYLIBS/LoginUILogViewer)
- [/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode](DYLIBS/LowPowerMode)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication)
- [/System/Library/PrivateFrameworks/MIL.framework/MIL](DYLIBS/MIL)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME)
- [/System/Library/PrivateFrameworks/MLAssetIO.framework/MLAssetIO](DYLIBS/MLAssetIO)
- [/System/Library/PrivateFrameworks/MLCompilerRuntime.framework/MLCompilerRuntime](DYLIBS/MLCompilerRuntime)
- [/System/Library/PrivateFrameworks/MLCompilerServices.framework/MLCompilerServices](DYLIBS/MLCompilerServices)
- [/System/Library/PrivateFrameworks/MLKit.framework/MLKit](DYLIBS/MLKit)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification)
- [/System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime](DYLIBS/MLRuntime)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS)
- [/System/Library/PrivateFrameworks/MMCSServices.framework/MMCSServices](DYLIBS/MMCSServices)
- [/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO](DYLIBS/MOVStreamIO)
- [/System/Library/PrivateFrameworks/MPUFoundation.framework/MPUFoundation](DYLIBS/MPUFoundation)
- [/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor](DYLIBS/MSUDataAccessor)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/libMTLCompilerHelper.dylib](DYLIBS/libMTLCompilerHelper.dylib)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/MacinTalk](DYLIBS/MacinTalk)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport)
- [/System/Library/PrivateFrameworks/MailKit.framework/MailKit](DYLIBS/MailKit)
- [/System/Library/PrivateFrameworks/MailServices.framework/MailServices](DYLIBS/MailServices)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI)
- [/System/Library/PrivateFrameworks/MailWebProcessSupport.framework/MailWebProcessSupport](DYLIBS/MailWebProcessSupport)
- [/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging](DYLIBS/MallocStackLogging)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration)
- [/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI](DYLIBS/ManagedConfigurationUI)
- [/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC](DYLIBS/ManagedSettingsObjC)
- [/System/Library/PrivateFrameworks/ManagedSettingsSupport.framework/ManagedSettingsSupport](DYLIBS/ManagedSettingsSupport)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI)
- [/System/Library/PrivateFrameworks/Marco.framework/Marco](DYLIBS/Marco)
- [/System/Library/PrivateFrameworks/MarkupUI.framework/MarkupUI](DYLIBS/MarkupUI)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs)
- [/System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit](DYLIBS/MaterialKit)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices)
- [/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl](DYLIBS/MediaControl)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService](DYLIBS/MediaConversionService)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience)
- [/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation](DYLIBS/MediaFoundation)
- [/System/Library/PrivateFrameworks/MediaGroups.framework/MediaGroups](DYLIBS/MediaGroups)
- [/System/Library/PrivateFrameworks/MediaGroupsDaemon.framework/MediaGroupsDaemon](DYLIBS/MediaGroupsDaemon)
- [/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit](DYLIBS/MediaKit)
- [/System/Library/PrivateFrameworks/MediaLibraryCore.framework/MediaLibraryCore](DYLIBS/MediaLibraryCore)
- [/System/Library/PrivateFrameworks/MediaML.framework/MediaML](DYLIBS/MediaML)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/MediaMLServices](DYLIBS/MediaMLServices)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit)
- [/System/Library/PrivateFrameworks/MediaPlatform.framework/MediaPlatform](DYLIBS/MediaPlatform)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore)
- [/System/Library/PrivateFrameworks/MediaPlayerUI.framework/MediaPlayerUI](DYLIBS/MediaPlayerUI)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote)
- [/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet](DYLIBS/MediaSafetyNet)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices)
- [/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream](DYLIBS/MediaStream)
- [/System/Library/PrivateFrameworks/MemoryDiagnostics.framework/MemoryDiagnostics](DYLIBS/MemoryDiagnostics)
- [/System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal](DYLIBS/MenstrualAlgorithmsInternal)
- [/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth](DYLIBS/MentalHealth)
- [/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon](DYLIBS/MentalHealthDaemon)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI)
- [/System/Library/PrivateFrameworks/MentalHealthWidgetUI.framework/MentalHealthWidgetUI](DYLIBS/MentalHealthWidgetUI)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury)
- [/System/Library/PrivateFrameworks/Message.framework/MailServices/IMAP.framework/IMAP](DYLIBS/IMAP)
- [/System/Library/PrivateFrameworks/Message.framework/MailServices/POP.framework/POP](DYLIBS/POP)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message)
- [/System/Library/PrivateFrameworks/MessageLegacy.framework/MailServices/IMAP.framework/IMAP](DYLIBS/IMAP)
- [/System/Library/PrivateFrameworks/MessageLegacy.framework/MessageLegacy](DYLIBS/MessageLegacy)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity)
- [/System/Library/PrivateFrameworks/MessageSupport.framework/MessageSupport](DYLIBS/MessageSupport)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools)
- [/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore](DYLIBS/MetricKitCore)
- [/System/Library/PrivateFrameworks/MetricKitServices.framework/MetricKitServices](DYLIBS/MetricKitServices)
- [/System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource](DYLIBS/MetricKitSource)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement](DYLIBS/MetricMeasurement)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework)
- [/System/Library/PrivateFrameworks/MetricsKit.framework/MetricsKit](DYLIBS/MetricsKit)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit)
- [/System/Library/PrivateFrameworks/MilAneflow.framework/MilAneflow](DYLIBS/MilAneflow)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater](DYLIBS/MobileAccessoryUpdater)
- [/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation](DYLIBS/MobileActivation)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset)
- [/System/Library/PrivateFrameworks/MobileAssetUpdater.framework/MobileAssetUpdater](DYLIBS/MobileAssetUpdater)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup)
- [/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth](DYLIBS/MobileBluetooth)
- [/System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager](DYLIBS/MobileContainerManager)
- [/System/Library/PrivateFrameworks/MobileDeviceLink.framework/MobileDeviceLink](DYLIBS/MobileDeviceLink)
- [/System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons](DYLIBS/MobileIcons)
- [/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI](DYLIBS/MobileIdentityServiceUI)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation](DYLIBS/MobileInstallation)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag)
- [/System/Library/PrivateFrameworks/MobileLookup.framework/MobileLookup](DYLIBS/MobileLookup)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI)
- [/System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration](DYLIBS/MobileObliteration)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/PlugIns/Safari.wkbundle/Safari](DYLIBS/Safari)
- [/System/Library/PrivateFrameworks/MobileSafariSwift.framework/MobileSafariSwift](DYLIBS/MobileSafariSwift)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate](DYLIBS/MobileSoftwareUpdate)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex)
- [/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage](DYLIBS/MobileStorage)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI)
- [/System/Library/PrivateFrameworks/MobileSync.framework/MobileSync](DYLIBS/MobileSync)
- [/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices](DYLIBS/MobileSystemServices)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer](DYLIBS/MobileTimer)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport)
- [/System/Library/PrivateFrameworks/MobileTimerUI.framework/MobileTimerUI](DYLIBS/MobileTimerUI)
- [/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi](DYLIBS/MobileWiFi)
- [/System/Library/PrivateFrameworks/ModalityXObjects.framework/ModalityXObjects](DYLIBS/ModalityXObjects)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings)
- [/System/Library/PrivateFrameworks/MonogramPoster.framework/MonogramPoster](DYLIBS/MonogramPoster)
- [/System/Library/PrivateFrameworks/Montreal.framework/Montreal](DYLIBS/Montreal)
- [/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets](DYLIBS/MorphunAssets)
- [/System/Library/PrivateFrameworks/MorphunSwift.framework/MorphunSwift](DYLIBS/MorphunSwift)
- [/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging](DYLIBS/MotionSensorLogging)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/MultitouchSessionFilterSupport](DYLIBS/MultitouchSessionFilterSupport)
- [/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport](DYLIBS/MultitouchSupport)
- [/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI](DYLIBS/MusicCarDisplayUI)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal)
- [/System/Library/PrivateFrameworks/MusicKitPlaybackSupport.framework/MusicKitPlaybackSupport](DYLIBS/MusicKitPlaybackSupport)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary)
- [/System/Library/PrivateFrameworks/MusicSettingsSupport.framework/MusicSettingsSupport](DYLIBS/MusicSettingsSupport)
- [/System/Library/PrivateFrameworks/MusicStoreUI.framework/MusicStoreUI](DYLIBS/MusicStoreUI)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI)
- [/System/Library/PrivateFrameworks/NCLaunchStats.framework/NCLaunchStats](DYLIBS/NCLaunchStats)
- [/System/Library/PrivateFrameworks/NLP.framework/NLP](DYLIBS/NLP)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/NLPLearner](DYLIBS/NLPLearner)
- [/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit](DYLIBS/NPTKit)
- [/System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry](DYLIBS/NanoAppRegistry)
- [/System/Library/PrivateFrameworks/NanoAudioControl.framework/NanoAudioControl](DYLIBS/NanoAudioControl)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup](DYLIBS/NanoBackup)
- [/System/Library/PrivateFrameworks/NanoComplicationSettings.framework/NanoComplicationSettings](DYLIBS/NanoComplicationSettings)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/NanoLeash](DYLIBS/NanoLeash)
- [/System/Library/PrivateFrameworks/NanoMailCompanionUI.framework/NanoMailCompanionUI](DYLIBS/NanoMailCompanionUI)
- [/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer](DYLIBS/NanoMailKitServer)
- [/System/Library/PrivateFrameworks/NanoMediaAPI.framework/NanoMediaAPI](DYLIBS/NanoMediaAPI)
- [/System/Library/PrivateFrameworks/NanoMediaBridgeUI.framework/NanoMediaBridgeUI](DYLIBS/NanoMediaBridgeUI)
- [/System/Library/PrivateFrameworks/NanoMediaRemote.framework/NanoMediaRemote](DYLIBS/NanoMediaRemote)
- [/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync](DYLIBS/NanoMusicSync)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit)
- [/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore](DYLIBS/NanoPhotosCore)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync](DYLIBS/NanoPreferencesSync)
- [/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry](DYLIBS/NanoRegistry)
- [/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber](DYLIBS/NanoResourceGrabber)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings](DYLIBS/NanoSystemSettings)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NanoUniverse](DYLIBS/NanoUniverse)
- [/System/Library/PrivateFrameworks/NanoWeatherComplicationsCompanion.framework/NanoWeatherComplicationsCompanion](DYLIBS/NanoWeatherComplicationsCompanion)
- [/System/Library/PrivateFrameworks/NanoWeatherKitUICompanion.framework/NanoWeatherKitUICompanion](DYLIBS/NanoWeatherKitUICompanion)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField)
- [/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory](DYLIBS/NearFieldAccessory)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices](DYLIBS/NearFieldPrivateServices)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions](DYLIBS/NearbySessions)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/NeighborhoodActivityConduit](DYLIBS/NeighborhoodActivityConduit)
- [/System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities](DYLIBS/NetAppsUtilities)
- [/System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI](DYLIBS/NetAppsUtilitiesUI)
- [/System/Library/PrivateFrameworks/Netrb.framework/Netrb](DYLIBS/Netrb)
- [/System/Library/PrivateFrameworks/NetworkQualityServices.framework/NetworkQualityServices](DYLIBS/NetworkQualityServices)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay](DYLIBS/NetworkRelay)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy)
- [/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics](DYLIBS/NetworkStatistics)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit](DYLIBS/NeutrinoKit)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics)
- [/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/NewsAnalyticsUpload](DYLIBS/NewsAnalyticsUpload)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement)
- [/System/Library/PrivateFrameworks/NewsEngagementCollector.framework/NewsEngagementCollector](DYLIBS/NewsEngagementCollector)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed)
- [/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation](DYLIBS/NewsFoundation)
- [/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit](DYLIBS/NewsKit)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization)
- [/System/Library/PrivateFrameworks/NewsServices.framework/NewsServices](DYLIBS/NewsServices)
- [/System/Library/PrivateFrameworks/NewsServicesInternal.framework/NewsServicesInternal](DYLIBS/NewsServicesInternal)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday)
- [/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport](DYLIBS/NewsTransport)
- [/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI](DYLIBS/NewsUI)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2)
- [/System/Library/PrivateFrameworks/NewsURLBucket.framework/NewsURLBucket](DYLIBS/NewsURLBucket)
- [/System/Library/PrivateFrameworks/NewsURLResolution.framework/NewsURLResolution](DYLIBS/NewsURLResolution)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining)
- [/System/Library/PrivateFrameworks/NonverbalCues.framework/NonverbalCues](DYLIBS/NonverbalCues)
- [/System/Library/PrivateFrameworks/NotTheStoreKitUIFrameworkYouAreLookingFor.framework/NotTheStoreKitUIFrameworkYouAreLookingFor](DYLIBS/NotTheStoreKitUIFrameworkYouAreLookingFor)
- [/System/Library/PrivateFrameworks/Notes.framework/Notes](DYLIBS/Notes)
- [/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics](DYLIBS/NotesAnalytics)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor)
- [/System/Library/PrivateFrameworks/NotesPreviewKit.framework/NotesPreviewKit](DYLIBS/NotesPreviewKit)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI)
- [/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices](DYLIBS/NotesUIServices)
- [/System/Library/PrivateFrameworks/OAuth.framework/OAuth](DYLIBS/OAuth)
- [/System/Library/PrivateFrameworks/ODCurareAnalysis.framework/ODCurareAnalysis](DYLIBS/ODCurareAnalysis)
- [/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting](DYLIBS/ODCurareEvaluationAndReporting)
- [/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient](DYLIBS/OSAServicesClient)
- [/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient](DYLIBS/OSASubmissionClient)
- [/System/Library/PrivateFrameworks/OSASyncProxyClient.framework/OSASyncProxyClient](DYLIBS/OSASyncProxyClient)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics)
- [/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate](DYLIBS/OSAnalyticsPrivate)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence)
- [/System/Library/PrivateFrameworks/OTSVG.framework/OTSVG](DYLIBS/OTSVG)
- [/System/Library/PrivateFrameworks/ObjectUnderstanding.framework/ObjectUnderstanding](DYLIBS/ObjectUnderstanding)
- [/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust](DYLIBS/OctagonTrust)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport](DYLIBS/OfficeImport)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit)
- [/System/Library/PrivateFrameworks/OpticalFlowFramework.framework/OpticalFlowFramework](DYLIBS/OpticalFlowFramework)
- [/System/Library/PrivateFrameworks/Osprey.framework/Osprey](DYLIBS/Osprey)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport](DYLIBS/PBBridgeSupport)
- [/System/Library/PrivateFrameworks/PDS.framework/PDS](DYLIBS/PDS)
- [/System/Library/PrivateFrameworks/PDSAgent.framework/PDSAgent](DYLIBS/PDSAgent)
- [/System/Library/PrivateFrameworks/PLSnapshot.framework/PLSnapshot](DYLIBS/PLSnapshot)
- [/System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter](DYLIBS/PacketFilter)
- [/System/Library/PrivateFrameworks/PairedSync.framework/PairedSync](DYLIBS/PairedSync)
- [/System/Library/PrivateFrameworks/PairedUnlock.framework/PairedUnlock](DYLIBS/PairedUnlock)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity](DYLIBS/PairingProximity)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit)
- [/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE](DYLIBS/ParavirtualizedANE)
- [/System/Library/PrivateFrameworks/ParsecModel.framework/ParsecModel](DYLIBS/ParsecModel)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore)
- [/System/Library/PrivateFrameworks/PassKitServices.framework/PassKitServices](DYLIBS/PassKitServices)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI)
- [/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation](DYLIBS/PassKitUIFoundation)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard](DYLIBS/Pasteboard)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase](DYLIBS/PaymentUIBase)
- [/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus](DYLIBS/Pegasus)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence)
- [/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI](DYLIBS/PencilPairingUI)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester)
- [/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI](DYLIBS/PeopleUI)
- [/System/Library/PrivateFrameworks/PeopleUIInternal.framework/PeopleUIInternal](DYLIBS/PeopleUIInternal)
- [/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor](DYLIBS/PerfPowerMetricMonitor)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader](DYLIBS/PerfPowerServicesReader)
- [/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit](DYLIBS/PerformanceControlKit)
- [/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace](DYLIBS/PerformanceTrace)
- [/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth](DYLIBS/PeridotDepth)
- [/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection](DYLIBS/PersistentConnection)
- [/System/Library/PrivateFrameworks/PersonaKit.framework/PersonaKit](DYLIBS/PersonaKit)
- [/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI](DYLIBS/PersonaUI)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio)
- [/System/Library/PrivateFrameworks/PersonalIntelligenceCore.framework/PersonalIntelligenceCore](DYLIBS/PersonalIntelligenceCore)
- [/System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait](DYLIBS/PersonalizationPortrait)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals)
- [/System/Library/PrivateFrameworks/Phoenix.framework/Phoenix](DYLIBS/Phoenix)
- [/System/Library/PrivateFrameworks/PhoneNumberResolver.framework/PhoneNumberResolver](DYLIBS/PhoneNumberResolver)
- [/System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers](DYLIBS/PhoneNumbers)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis)
- [/System/Library/PrivateFrameworks/PhotoBoothEffects.framework/PhotoBoothEffects](DYLIBS/PhotoBoothEffects)
- [/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation](DYLIBS/PhotoFoundation)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging)
- [/System/Library/PrivateFrameworks/PhotoLibrary.framework/PhotoLibrary](DYLIBS/PhotoLibrary)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph)
- [/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation](DYLIBS/PhotosImagingFoundation)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence)
- [/System/Library/PrivateFrameworks/PhotosKnowledgeGraph.framework/PhotosKnowledgeGraph](DYLIBS/PhotosKnowledgeGraph)
- [/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer](DYLIBS/PhotosPlayer)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate)
- [/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/PhotosensitivityProcessing](DYLIBS/PhotosensitivityProcessing)
- [/System/Library/PrivateFrameworks/PhysicsKit.framework/PhysicsKit](DYLIBS/PhysicsKit)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO)
- [/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit](DYLIBS/PlatterKit)
- [/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit](DYLIBS/PlugInKit)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/PointerUIServices](DYLIBS/PointerUIServices)
- [/System/Library/PrivateFrameworks/PointerUISystemServices.framework/PointerUISystemServices](DYLIBS/PointerUISystemServices)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks)
- [/System/Library/PrivateFrameworks/PoirotSQLite.framework/PoirotSQLite](DYLIBS/PoirotSQLite)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices)
- [/System/Library/PrivateFrameworks/PosterBoardUI.framework/PosterBoardUI](DYLIBS/PosterBoardUI)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI)
- [/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting](DYLIBS/PowerlogAccounting)
- [/System/Library/PrivateFrameworks/PowerlogControl.framework/PowerlogControl](DYLIBS/PowerlogControl)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore)
- [/System/Library/PrivateFrameworks/PowerlogDatabaseReader.framework/PowerlogDatabaseReader](DYLIBS/PowerlogDatabaseReader)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI)
- [/System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices](DYLIBS/PreviewsServices)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit)
- [/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI](DYLIBS/PrintKitUI)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting](DYLIBS/PrivacyAccounting)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore](DYLIBS/PrivacyDisclosureCore)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureUI.framework/PrivacyDisclosureUI](DYLIBS/PrivacyDisclosureUI)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning)
- [/System/Library/PrivateFrameworks/PrivateSearchClient.framework/PrivateSearchClient](DYLIBS/PrivateSearchClient)
- [/System/Library/PrivateFrameworks/PrivateSearchCore.framework/PrivateSearchCore](DYLIBS/PrivateSearchCore)
- [/System/Library/PrivateFrameworks/PrivateSearchProtocols.framework/PrivateSearchProtocols](DYLIBS/PrivateSearchProtocols)
- [/System/Library/PrivateFrameworks/ProVideo.framework/ProVideo](DYLIBS/ProVideo)
- [/System/Library/PrivateFrameworks/ProactiveBlendingLayer_iOS.framework/ProactiveBlendingLayer_iOS](DYLIBS/ProactiveBlendingLayer_iOS)
- [/System/Library/PrivateFrameworks/ProactiveCDNDownloader.framework/ProactiveCDNDownloader](DYLIBS/ProactiveCDNDownloader)
- [/System/Library/PrivateFrameworks/ProactiveContextClient.framework/ProactiveContextClient](DYLIBS/ProactiveContextClient)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker)
- [/System/Library/PrivateFrameworks/ProactiveExperiments.framework/ProactiveExperiments](DYLIBS/ProactiveExperiments)
- [/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals](DYLIBS/ProactiveExperimentsInternals)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/ProactiveInputPredictions](DYLIBS/ProactiveInputPredictions)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictionsInternals.framework/ProactiveInputPredictionsInternals](DYLIBS/ProactiveInputPredictionsInternals)
- [/System/Library/PrivateFrameworks/ProactiveML.framework/ProactiveML](DYLIBS/ProactiveML)
- [/System/Library/PrivateFrameworks/ProactiveMagicalMoments.framework/ProactiveMagicalMoments](DYLIBS/ProactiveMagicalMoments)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse](DYLIBS/ProactiveShareSheetDataHarvestingLighthouse)
- [/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel](DYLIBS/ProactiveSuggestionClientModel)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport)
- [/System/Library/PrivateFrameworks/ProactiveSupportStubs.framework/ProactiveSupportStubs](DYLIBS/ProactiveSupportStubs)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit)
- [/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity](DYLIBS/ProfileValidatedAppIdentity)
- [/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI](DYLIBS/ProgressUI)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction](DYLIBS/PromotedContentPrediction)
- [/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PromotedContentProxy](DYLIBS/PromotedContentProxy)
- [/System/Library/PrivateFrameworks/PromotedContentSupport.framework/PromotedContentSupport](DYLIBS/PromotedContentSupport)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI)
- [/System/Library/PrivateFrameworks/ProofReader.framework/ProofReader](DYLIBS/ProofReader)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage)
- [/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer](DYLIBS/ProtocolBuffer)
- [/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools](DYLIBS/PrototypeTools)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI](DYLIBS/PrototypeToolsUI)
- [/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit](DYLIBS/ProxCardKit)
- [/System/Library/PrivateFrameworks/Proximity.framework/Proximity](DYLIBS/Proximity)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl)
- [/System/Library/PrivateFrameworks/ProximityUI.framework/ProximityUI](DYLIBS/ProximityUI)
- [/System/Library/PrivateFrameworks/QLCharts.framework/QLCharts](DYLIBS/QLCharts)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit)
- [/System/Library/PrivateFrameworks/Quagga.framework/Quagga](DYLIBS/Quagga)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding)
- [/System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport](DYLIBS/QuickLookSupport)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailGeneration.framework/QuickLookThumbnailGeneration](DYLIBS/QuickLookThumbnailGeneration)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon)
- [/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore](DYLIBS/QuickLookUICore)
- [/System/Library/PrivateFrameworks/RESync.framework/RESync](DYLIBS/RESync)
- [/System/Library/PrivateFrameworks/RTBuddyCrashlogDecoder.framework/RTBuddyCrashlogDecoder](DYLIBS/RTBuddyCrashlogDecoder)
- [/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting](DYLIBS/RTCReporting)
- [/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI](DYLIBS/RTTUI)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities)
- [/System/Library/PrivateFrameworks/Radio.framework/Radio](DYLIBS/Radio)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport)
- [/System/Library/PrivateFrameworks/RapportUI.framework/RapportUI](DYLIBS/RapportUI)
- [/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion](DYLIBS/RealityFusion)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO)
- [/System/Library/PrivateFrameworks/Recap.framework/Recap](DYLIBS/Recap)
- [/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting](DYLIBS/RecapPerformanceTesting)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount)
- [/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal](DYLIBS/ReflectionInternal)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain)
- [/System/Library/PrivateFrameworks/RelativeMotion.framework/RelativeMotion](DYLIBS/RelativeMotion)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine)
- [/System/Library/PrivateFrameworks/RelevanceEngineUI.framework/RelevanceEngineUI](DYLIBS/RelevanceEngineUI)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/ReminderKitUI](DYLIBS/ReminderKitUI)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration](DYLIBS/RemoteConfiguration)
- [/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML](DYLIBS/RemoteCoreML)
- [/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID](DYLIBS/RemoteHID)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement)
- [/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel](DYLIBS/RemoteManagementModel)
- [/System/Library/PrivateFrameworks/RemoteManagementProtocol.framework/RemoteManagementProtocol](DYLIBS/RemoteManagementProtocol)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore](DYLIBS/RemoteManagementStore)
- [/System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI](DYLIBS/RemoteManagementUI)
- [/System/Library/PrivateFrameworks/RemoteMediaServices.framework/RemoteMediaServices](DYLIBS/RemoteMediaServices)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice)
- [/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery](DYLIBS/RemoteServiceDiscovery)
- [/System/Library/PrivateFrameworks/RemoteStateDumpKit.framework/RemoteStateDumpKit](DYLIBS/RemoteStateDumpKit)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges)
- [/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth](DYLIBS/RespiratoryHealth)
- [/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon](DYLIBS/RespiratoryHealthDaemon)
- [/System/Library/PrivateFrameworks/RespiratoryHealthUI.framework/RespiratoryHealthUI](DYLIBS/RespiratoryHealthUI)
- [/System/Library/PrivateFrameworks/ResponseKit.framework/ResponseKit](DYLIBS/ResponseKit)
- [/System/Library/PrivateFrameworks/RevealCore.framework/RevealCore](DYLIBS/RevealCore)
- [/System/Library/PrivateFrameworks/RoomScanCore.framework/RoomScanCore](DYLIBS/RoomScanCore)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal)
- [/System/Library/PrivateFrameworks/SAML.framework/SAML](DYLIBS/SAML)
- [/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects](DYLIBS/SAObjects)
- [/System/Library/PrivateFrameworks/SDAPI.framework/SDAPI](DYLIBS/SDAPI)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols)
- [/System/Library/PrivateFrameworks/SILManager.framework/SILManager](DYLIBS/SILManager)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport)
- [/System/Library/PrivateFrameworks/SIMToolkitUI.framework/SIMToolkitUI](DYLIBS/SIMToolkitUI)
- [/System/Library/PrivateFrameworks/SMBClientEngine.framework/SMBClientEngine](DYLIBS/SMBClientEngine)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/SMBClientProvider](DYLIBS/SMBClientProvider)
- [/System/Library/PrivateFrameworks/SMBSearch.framework/SMBSearch](DYLIBS/SMBSearch)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS)
- [/System/Library/PrivateFrameworks/SOSUI.framework/SOSUI](DYLIBS/SOSUI)
- [/System/Library/PrivateFrameworks/SPFinder.framework/SPFinder](DYLIBS/SPFinder)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient](DYLIBS/STSXPCHelperClient)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing](DYLIBS/SafariSafeBrowsing)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI)
- [/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts](DYLIBS/SafetyAlerts)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis)
- [/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface](DYLIBS/SavageCameraInterface)
- [/System/Library/PrivateFrameworks/Scandium.framework/Scandium](DYLIBS/Scandium)
- [/System/Library/PrivateFrameworks/SceneIntelligence.framework/SceneIntelligence](DYLIBS/SceneIntelligence)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/SchoolTime](DYLIBS/SchoolTime)
- [/System/Library/PrivateFrameworks/SchoolTimeSettingsUI.framework/SchoolTimeSettingsUI](DYLIBS/SchoolTimeSettingsUI)
- [/System/Library/PrivateFrameworks/ScreenReaderBrailleDriver.framework/ScreenReaderBrailleDriver](DYLIBS/ScreenReaderBrailleDriver)
- [/System/Library/PrivateFrameworks/ScreenReaderCore.framework/ScreenReaderCore](DYLIBS/ScreenReaderCore)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore)
- [/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices](DYLIBS/ScreenshotServices)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation)
- [/System/Library/PrivateFrameworks/SearchToShareCore.framework/SearchToShareCore](DYLIBS/SearchToShareCore)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI)
- [/System/Library/PrivateFrameworks/SearchUICardKitProviderSupport.framework/SearchUICardKitProviderSupport](DYLIBS/SearchUICardKitProviderSupport)
- [/System/Library/PrivateFrameworks/SecureChannel.framework/SecureChannel](DYLIBS/SecureChannel)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService](DYLIBS/SecureTransactionService)
- [/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets.framework/SecureVoiceTriggerAssets](DYLIBS/SecureVoiceTriggerAssets)
- [/System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation](DYLIBS/SecurityFoundation)
- [/System/Library/PrivateFrameworks/Seeding.framework/Seeding](DYLIBS/Seeding)
- [/System/Library/PrivateFrameworks/SemanticPerception.framework/SemanticPerception](DYLIBS/SemanticPerception)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI)
- [/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper](DYLIBS/SensorKitHelper)
- [/System/Library/PrivateFrameworks/SensorKitSupport.framework/SensorKitSupport](DYLIBS/SensorKitSupport)
- [/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI](DYLIBS/SensorKitUI)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions)
- [/System/Library/PrivateFrameworks/ServiceExtensionsCore.framework/ServiceExtensionsCore](DYLIBS/ServiceExtensionsCore)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement)
- [/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert](DYLIBS/SessionAlert)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications)
- [/System/Library/PrivateFrameworks/SessionSQL.framework/SessionSQL](DYLIBS/SessionSQL)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings)
- [/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings)
- [/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular](DYLIBS/SettingsCellular)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant)
- [/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport](DYLIBS/SetupAssistantSupport)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI)
- [/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit](DYLIBS/SetupKit)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia)
- [/System/Library/PrivateFrameworks/SeymourServerProtocol.framework/SeymourServerProtocol](DYLIBS/SeymourServerProtocol)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet)
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials](DYLIBS/SharedWebCredentials)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents)
- [/System/Library/PrivateFrameworks/ShazamInsights.framework/ShazamInsights](DYLIBS/ShazamInsights)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI)
- [/System/Library/PrivateFrameworks/ShortcutUIKit.framework/ShortcutUIKit](DYLIBS/ShortcutUIKit)
- [/System/Library/PrivateFrameworks/SidecarCore.framework/SidecarCore](DYLIBS/SidecarCore)
- [/System/Library/PrivateFrameworks/SidecarUI.framework/SidecarUI](DYLIBS/SidecarUI)
- [/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression](DYLIBS/SignalCompression)
- [/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection](DYLIBS/SignpostCollection)
- [/System/Library/PrivateFrameworks/SignpostMetrics.framework/SignpostMetrics](DYLIBS/SignpostMetrics)
- [/System/Library/PrivateFrameworks/SignpostNotification.framework/SignpostNotification](DYLIBS/SignpostNotification)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex)
- [/System/Library/PrivateFrameworks/SilexVideo.framework/SilexVideo](DYLIBS/SilexVideo)
- [/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb](DYLIBS/SilexWeb)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents)
- [/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution](DYLIBS/SiriAppResolution)
- [/System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils](DYLIBS/SiriAudioIntentUtils)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal)
- [/System/Library/PrivateFrameworks/SiriAudioSnippetKit.framework/SiriAudioSnippetKit](DYLIBS/SiriAudioSnippetKit)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam)
- [/System/Library/PrivateFrameworks/SiriCarCommandsIntents.framework/SiriCarCommandsIntents](DYLIBS/SiriCarCommandsIntents)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents)
- [/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore](DYLIBS/SiriCore)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics](DYLIBS/SiriCoreMetrics)
- [/System/Library/PrivateFrameworks/SiriCorrections.framework/SiriCorrections](DYLIBS/SiriCorrections)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback](DYLIBS/SiriCrossDeviceArbitrationFeedback)
- [/System/Library/PrivateFrameworks/SiriDailyBriefingInternal.framework/SiriDailyBriefingInternal](DYLIBS/SiriDailyBriefingInternal)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine](DYLIBS/SiriDialogEngine)
- [/System/Library/PrivateFrameworks/SiriEmergencyIntents.framework/SiriEmergencyIntents](DYLIBS/SiriEmergencyIntents)
- [/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher](DYLIBS/SiriEntityMatcher)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal)
- [/System/Library/PrivateFrameworks/SiriExpanseInternalUI.framework/SiriExpanseInternalUI](DYLIBS/SiriExpanseInternalUI)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo](DYLIBS/SiriGeo)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow)
- [/System/Library/PrivateFrameworks/SiriInferenceIntents.framework/SiriInferenceIntents](DYLIBS/SiriInferenceIntents)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/SiriInferredHelpfulness](DYLIBS/SiriInferredHelpfulness)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch)
- [/System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes](DYLIBS/SiriInformationTypes)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation)
- [/System/Library/PrivateFrameworks/SiriIntentEvents.framework/SiriIntentEvents](DYLIBS/SiriIntentEvents)
- [/System/Library/PrivateFrameworks/SiriInteractive.framework/SiriInteractive](DYLIBS/SiriInteractive)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/SiriInvocationAnalytics](DYLIBS/SiriInvocationAnalytics)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow)
- [/System/Library/PrivateFrameworks/SiriKitInvocation.framework/SiriKitInvocation](DYLIBS/SiriKitInvocation)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime)
- [/System/Library/PrivateFrameworks/SiriLiminal.framework/SiriLiminal](DYLIBS/SiriLiminal)
- [/System/Library/PrivateFrameworks/SiriMASPFLTraining.framework/SiriMASPFLTraining](DYLIBS/SiriMASPFLTraining)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI)
- [/System/Library/PrivateFrameworks/SiriModes.framework/SiriModes](DYLIBS/SiriModes)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents)
- [/System/Library/PrivateFrameworks/SiriObservation.framework/SiriObservation](DYLIBS/SiriObservation)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport)
- [/System/Library/PrivateFrameworks/SiriPowerInstrumentation.framework/SiriPowerInstrumentation](DYLIBS/SiriPowerInstrumentation)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningLogging.framework/SiriPrivateLearningLogging](DYLIBS/SiriPrivateLearningLogging)
- [/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents](DYLIBS/SiriReaderIntents)
- [/System/Library/PrivateFrameworks/SiriReaderServices.framework/SiriReaderServices](DYLIBS/SiriReaderServices)
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution)
- [/System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel](DYLIBS/SiriReferenceResolutionDataModel)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver](DYLIBS/SiriReferenceResolver)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals)
- [/System/Library/PrivateFrameworks/SiriSocialConversation.framework/SiriSocialConversation](DYLIBS/SiriSocialConversation)
- [/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis](DYLIBS/SiriSpeechSynthesis)
- [/System/Library/PrivateFrameworks/SiriStates.framework/SiriStates](DYLIBS/SiriStates)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport)
- [/System/Library/PrivateFrameworks/SiriSystemCommandsIntents.framework/SiriSystemCommandsIntents](DYLIBS/SiriSystemCommandsIntents)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService)
- [/System/Library/PrivateFrameworks/SiriTaskEngagement.framework/SiriTaskEngagement](DYLIBS/SiriTaskEngagement)
- [/System/Library/PrivateFrameworks/SiriTasks.framework/SiriTasks](DYLIBS/SiriTasks)
- [/System/Library/PrivateFrameworks/SiriTasksEvaluation.framework/SiriTasksEvaluation](DYLIBS/SiriTasksEvaluation)
- [/System/Library/PrivateFrameworks/SiriTimeAlarmInternal.framework/SiriTimeAlarmInternal](DYLIBS/SiriTimeAlarmInternal)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/SiriTimeInternal](DYLIBS/SiriTimeInternal)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager)
- [/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI](DYLIBS/SiriUI)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation)
- [/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge](DYLIBS/SiriUIBridge)
- [/System/Library/PrivateFrameworks/SiriUICardKitProviderSupport.framework/SiriUICardKitProviderSupport](DYLIBS/SiriUICardKitProviderSupport)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX](DYLIBS/SiriVOX)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution)
- [/System/Library/PrivateFrameworks/SiriWellnessIntents.framework/SiriWellnessIntents](DYLIBS/SiriWellnessIntents)
- [/System/Library/PrivateFrameworks/Sleep.framework/Sleep](DYLIBS/Sleep)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon](DYLIBS/SleepDaemon)
- [/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth](DYLIBS/SleepHealth)
- [/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon](DYLIBS/SleepHealthDaemon)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusFoundation.framework/OpusFoundation](DYLIBS/OpusFoundation)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusKit.framework/OpusKit](DYLIBS/OpusKit)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/SlideshowKit](DYLIBS/SlideshowKit)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies)
- [/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer](DYLIBS/SmartRepliesServer)
- [/System/Library/PrivateFrameworks/SmartRepliesUI.framework/SmartRepliesUI](DYLIBS/SmartRepliesUI)
- [/System/Library/PrivateFrameworks/SnippetCommands.framework/SnippetCommands](DYLIBS/SnippetCommands)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI)
- [/System/Library/PrivateFrameworks/SnippetUI_Proto.framework/SnippetUI_Proto](DYLIBS/SnippetUI_Proto)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer)
- [/System/Library/PrivateFrameworks/SocialServices.framework/SocialServices](DYLIBS/SocialServices)
- [/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking](DYLIBS/SoftLinking)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge](DYLIBS/SoftwareUpdateBridge)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect](DYLIBS/SoftwareUpdateCoreConnect)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport](DYLIBS/SoftwareUpdateCoreSupport)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI](DYLIBS/SoftwareUpdateServicesUI)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit)
- [/System/Library/PrivateFrameworks/SoundAutoConfig.framework/SoundAutoConfig](DYLIBS/SoundAutoConfig)
- [/System/Library/PrivateFrameworks/SoundBoardServices.framework/SoundBoardServices](DYLIBS/SoundBoardServices)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/SoundScapesUtility](DYLIBS/SoundScapesUtility)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution](DYLIBS/SpaceAttribution)
- [/System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices](DYLIBS/SpeakThisServices)
- [/System/Library/PrivateFrameworks/SpeakTypingServices.framework/SpeakTypingServices](DYLIBS/SpeakTypingServices)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition)
- [/System/Library/PrivateFrameworks/SpeechDetector.framework/SpeechDetector](DYLIBS/SpeechDetector)
- [/System/Library/PrivateFrameworks/SpeechDictionary.framework/SpeechDictionary](DYLIBS/SpeechDictionary)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices](DYLIBS/SpeechRecognitionCommandServices)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore](DYLIBS/SpeechRecognitionCore)
- [/System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport](DYLIBS/SpeechRecognitionSharedSupport)
- [/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard](DYLIBS/SplashBoard)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation](DYLIBS/SpotlightFoundation)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver)
- [/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation](DYLIBS/SpotlightRecommendation)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices)
- [/System/Library/PrivateFrameworks/SpotlightUI.framework/SpotlightUI](DYLIBS/SpotlightUI)
- [/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal](DYLIBS/SpotlightUIInternal)
- [/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared](DYLIBS/SpotlightUIShared)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome)
- [/System/Library/PrivateFrameworks/SpringBoardIntents.framework/SpringBoardIntents](DYLIBS/SpringBoardIntents)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices)
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit](DYLIBS/StatusKit)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI)
- [/System/Library/PrivateFrameworks/Stocks.framework/Stocks](DYLIBS/Stocks)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI)
- [/System/Library/PrivateFrameworks/StorageData.framework/StorageData](DYLIBS/StorageData)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit)
- [/System/Library/PrivateFrameworks/StorageSettings.framework/StorageSettings](DYLIBS/StorageSettings)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI)
- [/System/Library/PrivateFrameworks/StoreBookkeeper.framework/StoreBookkeeper](DYLIBS/StoreBookkeeper)
- [/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/StoreBookkeeperClient](DYLIBS/StoreBookkeeperClient)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor](DYLIBS/StreamingExtractor)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip](DYLIBS/StreamingZip)
- [/System/Library/PrivateFrameworks/StrokeAnimation.framework/StrokeAnimation](DYLIBS/StrokeAnimation)
- [/System/Library/PrivateFrameworks/StudyLog.framework/StudyLog](DYLIBS/StudyLog)
- [/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics](DYLIBS/SuggestionsSpotlightMetrics)
- [/System/Library/PrivateFrameworks/SummariesHealthDaemon.framework/SummariesHealthDaemon](DYLIBS/SummariesHealthDaemon)
- [/System/Library/PrivateFrameworks/SwiftCertificate.framework/SwiftCertificate](DYLIBS/SwiftCertificate)
- [/System/Library/PrivateFrameworks/SwiftNN.framework/SwiftNN](DYLIBS/SwiftNN)
- [/System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite](DYLIBS/SwiftSQLite)
- [/System/Library/PrivateFrameworks/SwiftUIAccessibility.framework/SwiftUIAccessibility](DYLIBS/SwiftUIAccessibility)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication](DYLIBS/Symbolication)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter)
- [/System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter](DYLIBS/SymptomReporter)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent](DYLIBS/ManagedEvent)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics](DYLIBS/SymptomAnalytics)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed](DYLIBS/SymptomPresentationFeed)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationLite.framework/SymptomPresentationLite](DYLIBS/SymptomPresentationLite)
- [/System/Library/PrivateFrameworks/Synapse.framework/Synapse](DYLIBS/Synapse)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults](DYLIBS/SyncedDefaults)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels)
- [/System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture](DYLIBS/SystemAperture)
- [/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI](DYLIBS/SystemApertureUI)
- [/System/Library/PrivateFrameworks/SystemPaperPresentation.framework/SystemPaperPresentation](DYLIBS/SystemPaperPresentation)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI)
- [/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake](DYLIBS/SystemWake)
- [/System/Library/PrivateFrameworks/TCC.framework/TCC](DYLIBS/TCC)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing)
- [/System/Library/PrivateFrameworks/TSReading.framework/TSReading](DYLIBS/TSReading)
- [/System/Library/PrivateFrameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices)
- [/System/Library/PrivateFrameworks/TVLatency.framework/TVLatency](DYLIBS/TVLatency)
- [/System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit](DYLIBS/TVMLKit)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI)
- [/System/Library/PrivateFrameworks/TVUIKit.framework/TVUIKit](DYLIBS/TVUIKit)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi)
- [/System/Library/PrivateFrameworks/TailspinSymbolication.framework/TailspinSymbolication](DYLIBS/TailspinSymbolication)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings)
- [/System/Library/PrivateFrameworks/TeaSnappy.framework/TeaSnappy](DYLIBS/TeaSnappy)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI)
- [/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences](DYLIBS/TelephonyPreferences)
- [/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC](DYLIBS/TelephonyRPC)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities)
- [/System/Library/PrivateFrameworks/TelephonyXPCClient.framework/TelephonyXPCClient](DYLIBS/TelephonyXPCClient)
- [/System/Library/PrivateFrameworks/TelephonyXPCServer.framework/TelephonyXPCServer](DYLIBS/TelephonyXPCServer)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit)
- [/System/Library/PrivateFrameworks/TestFlightCore.framework/TestFlightCore](DYLIBS/TestFlightCore)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput)
- [/System/Library/PrivateFrameworks/TextInputCJK.framework/TextInputCJK](DYLIBS/TextInputCJK)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/TextInputTestingKit](DYLIBS/TextInputTestingKit)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/deu.dylib](DYLIBS/deu.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eci.dylib](DYLIBS/eci.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eng.dylib](DYLIBS/eng.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/enu.dylib](DYLIBS/enu.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esm.dylib](DYLIBS/esm.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esp.dylib](DYLIBS/esp.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fin.dylib](DYLIBS/fin.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fra.dylib](DYLIBS/fra.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/frc.dylib](DYLIBS/frc.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ita.dylib](DYLIBS/ita.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ptb.dylib](DYLIBS/ptb.dylib)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/TextToSpeechKonaSupport](DYLIBS/TextToSpeechKonaSupport)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/TextToSpeechMauiSupport](DYLIBS/TextToSpeechMauiSupport)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared)
- [/System/Library/PrivateFrameworks/TextureIO.framework/TextureIO](DYLIBS/TextureIO)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings)
- [/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](DYLIBS/Tightbeam)
- [/System/Library/PrivateFrameworks/TimeAppServices.framework/TimeAppServices](DYLIBS/TimeAppServices)
- [/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync](DYLIBS/TimeSync)
- [/System/Library/PrivateFrameworks/Timeline.framework/Timeline](DYLIBS/Timeline)
- [/System/Library/PrivateFrameworks/TinCanShared.framework/TinCanShared](DYLIBS/TinCanShared)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore)
- [/System/Library/PrivateFrameworks/TipKitLegacy.framework/TipKitLegacy](DYLIBS/TipKitLegacy)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices](DYLIBS/TipKitServices)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI)
- [/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit](DYLIBS/ToneKit)
- [/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary](DYLIBS/ToneLibrary)
- [/System/Library/PrivateFrameworks/TouchML.framework/TouchML](DYLIBS/TouchML)
- [/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote](DYLIBS/TouchRemote)
- [/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance](DYLIBS/TrackingAvoidance)
- [/System/Library/PrivateFrameworks/TraitsArbiter.framework/TraitsArbiter](DYLIBS/TraitsArbiter)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices](DYLIBS/TranslationUIServices)
- [/System/Library/PrivateFrameworks/Transliteration.framework/Transliteration](DYLIBS/Transliteration)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency)
- [/System/Library/PrivateFrameworks/TransparencyDetailsView.framework/TransparencyDetailsView](DYLIBS/TransparencyDetailsView)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI](DYLIBS/TransparencyUI)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial)
- [/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto](DYLIBS/TrialProto)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer)
- [/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers](DYLIBS/TrustedPeers)
- [/System/Library/PrivateFrameworks/TuriCore.framework/TuriCore](DYLIBS/TuriCore)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework](DYLIBS/TypistFramework)
- [/System/Library/PrivateFrameworks/TypologyAccess.framework/TypologyAccess](DYLIBS/TypologyAccess)
- [/System/Library/PrivateFrameworks/UARPUpdaterService.framework/UARPUpdaterService](DYLIBS/UARPUpdaterService)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices)
- [/System/Library/PrivateFrameworks/UITriggerVC.framework/UITriggerVC](DYLIBS/UITriggerVC)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding)
- [/System/Library/PrivateFrameworks/URLCompression.framework/URLCompression](DYLIBS/URLCompression)
- [/System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting](DYLIBS/URLFormatting)
- [/System/Library/PrivateFrameworks/USDKit.framework/USDKit](DYLIBS/USDKit)
- [/System/Library/PrivateFrameworks/USDLib_FormatLoaderProxy.framework/USDLib_FormatLoaderProxy](DYLIBS/USDLib_FormatLoaderProxy)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework)
- [/System/Library/PrivateFrameworks/UnityPoster.framework/UnityPoster](DYLIBS/UnityPoster)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking)
- [/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity](DYLIBS/UserActivity)
- [/System/Library/PrivateFrameworks/UserAlerts.framework/UserAlerts](DYLIBS/UserAlerts)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/liblivefiles.plugin.dummy.dylib](DYLIBS/liblivefiles.plugin.dummy.dylib)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_cs.dylib](DYLIBS/livefiles_cs.dylib)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib](DYLIBS/livefiles_exfat.dylib)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib](DYLIBS/livefiles_hfs.dylib)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib](DYLIBS/livefiles_msdos.dylib)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_ntfs.dylib](DYLIBS/livefiles_ntfs.dylib)
- [/System/Library/PrivateFrameworks/UserFS.framework/UserFS](DYLIBS/UserFS)
- [/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement](DYLIBS/UserManagement)
- [/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout](DYLIBS/UserManagementLayout)
- [/System/Library/PrivateFrameworks/UserManagementUI.framework/UserManagementUI](DYLIBS/UserManagementUI)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer)
- [/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings](DYLIBS/UserNotificationsSettings)
- [/System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation](DYLIBS/UserNotificationsTranslation)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit)
- [/System/Library/PrivateFrameworks/UserSafety.framework/UserSafety](DYLIBS/UserSafety)
- [/System/Library/PrivateFrameworks/UserSafetyUI.framework/UserSafetyUI](DYLIBS/UserSafetyUI)
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI)
- [/System/Library/PrivateFrameworks/VideoToolboxParavirtualizationSupport.framework/VideoToolboxParavirtualizationSupport](DYLIBS/VideoToolboxParavirtualizationSupport)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage](DYLIBS/VirtualGarage)
- [/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore](DYLIBS/VisionCore)
- [/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices](DYLIBS/VisionHWAccelerationServices)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore](DYLIBS/VisionKitCore)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal)
- [/System/Library/PrivateFrameworks/VisualAlert.framework/VisualAlert](DYLIBS/VisualAlert)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence)
- [/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization](DYLIBS/VisualLocalization)
- [/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger](DYLIBS/VisualLogger)
- [/System/Library/PrivateFrameworks/VisualPairing.framework/VisualPairing](DYLIBS/VisualPairing)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP](DYLIBS/IMAP)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail](DYLIBS/VisualVoicemail)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/libvoiced_tts.dylib](DYLIBS/libvoiced_tts.dylib)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices](DYLIBS/VoiceServices)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts)
- [/System/Library/PrivateFrameworks/VoiceShortcutsUICardKitProviderSupport.framework/VoiceShortcutsUICardKitProviderSupport](DYLIBS/VoiceShortcutsUICardKitProviderSupport)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI)
- [/System/Library/PrivateFrameworks/VoicemailStore.framework/VoicemailStore](DYLIBS/VoicemailStore)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit)
- [/System/Library/PrivateFrameworks/WatchControlAssets.framework/WatchControlAssets](DYLIBS/WatchControlAssets)
- [/System/Library/PrivateFrameworks/WatchControlSettings.framework/WatchControlSettings](DYLIBS/WatchControlSettings)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit)
- [/System/Library/PrivateFrameworks/WatchQuickActionsServices.framework/WatchQuickActionsServices](DYLIBS/WatchQuickActionsServices)
- [/System/Library/PrivateFrameworks/WatchReplies.framework/WatchReplies](DYLIBS/WatchReplies)
- [/System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient](DYLIBS/WatchdogClient)
- [/System/Library/PrivateFrameworks/Weather.framework/Weather](DYLIBS/Weather)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon)
- [/System/Library/PrivateFrameworks/WeatherFoundation.framework/WeatherFoundation](DYLIBS/WeatherFoundation)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI)
- [/System/Library/PrivateFrameworks/WebApp.framework/WebApp](DYLIBS/WebApp)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift)
- [/System/Library/PrivateFrameworks/WebContentAnalysis.framework/WebContentAnalysis](DYLIBS/WebContentAnalysis)
- [/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions](DYLIBS/WebContentRestrictions)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU)
- [/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector](DYLIBS/WebInspector)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/WebPrivacy](DYLIBS/WebPrivacy)
- [/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet](DYLIBS/WebSheet)
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI)
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/WelcomeKit](DYLIBS/WelcomeKit)
- [/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore](DYLIBS/WelcomeKitCore)
- [/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI](DYLIBS/WelcomeKitUI)
- [/System/Library/PrivateFrameworks/WellnessUI.framework/WellnessUI](DYLIBS/WellnessUI)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics)
- [/System/Library/PrivateFrameworks/WiFiCloudSyncEngine.framework/WiFiCloudSyncEngine](DYLIBS/WiFiCloudSyncEngine)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI)
- [/System/Library/PrivateFrameworks/WiFiLogCapture.framework/WiFiLogCapture](DYLIBS/WiFiLogCapture)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy)
- [/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity](DYLIBS/WiFiVelocity)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer)
- [/System/Library/PrivateFrameworks/Widgets.framework/Widgets](DYLIBS/Widgets)
- [/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager](DYLIBS/WirelessCoexManager)
- [/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics](DYLIBS/WirelessDiagnostics)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/WirelessInsights](DYLIBS/WirelessInsights)
- [/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity](DYLIBS/WirelessProximity)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit)
- [/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness](DYLIBS/WorkflowResponsiveness)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore)
- [/System/Library/PrivateFrameworks/WorkoutHealthBridge.framework/WorkoutHealthBridge](DYLIBS/WorkoutHealthBridge)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/WorkoutKitServices](DYLIBS/WorkoutKitServices)
- [/System/Library/PrivateFrameworks/WorkoutKitUI.framework/WorkoutKitUI](DYLIBS/WorkoutKitUI)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI)
- [/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap](DYLIBS/XCTTargetBootstrap)
- [/System/Library/PrivateFrameworks/XGBoostFramework.framework/XGBoostFramework](DYLIBS/XGBoostFramework)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT)
- [/System/Library/PrivateFrameworks/XOJITExecutor.framework/XOJITExecutor](DYLIBS/XOJITExecutor)
- [/System/Library/PrivateFrameworks/XavierCore.framework/XavierCore](DYLIBS/XavierCore)
- [/System/Library/PrivateFrameworks/XavierNews.framework/XavierNews](DYLIBS/XavierNews)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport](DYLIBS/ZhuGeSupport)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib)
- [/System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices](DYLIBS/ZoomServices)
- [/System/Library/PrivateFrameworks/_Coherence_CloudKit_Private.framework/_Coherence_CloudKit_Private](DYLIBS/_Coherence_CloudKit_Private)
- [/System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI](DYLIBS/_IconServices_SwiftUI)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore](DYLIBS/_MusicKitInternal_MediaPlaybackCore)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlayer.framework/_MusicKitInternal_MediaPlayer](DYLIBS/_MusicKitInternal_MediaPlayer)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit)
- [/System/Library/PrivateFrameworks/apfs_boot_mount.framework/apfs_boot_mount](DYLIBS/apfs_boot_mount)
- [/System/Library/PrivateFrameworks/caulk.framework/caulk](DYLIBS/caulk)
- [/System/Library/PrivateFrameworks/iCalendar.framework/iCalendar](DYLIBS/iCalendar)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/iCloudDriveService](DYLIBS/iCloudDriveService)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification](DYLIBS/iCloudNotification)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerClient.framework/iCloudSubscriptionOptimizerClient](DYLIBS/iCloudSubscriptionOptimizerClient)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerCore.framework/iCloudSubscriptionOptimizerCore](DYLIBS/iCloudSubscriptionOptimizerCore)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/iCloudSubscriptionOptimizerDaemon](DYLIBS/iCloudSubscriptionOptimizerDaemon)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/iCloudSubscriptionOptimizerLighthouse](DYLIBS/iCloudSubscriptionOptimizerLighthouse)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerPFLTraining.framework/iCloudSubscriptionOptimizerPFLTraining](DYLIBS/iCloudSubscriptionOptimizerPFLTraining)
- [/System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps](DYLIBS/iMessageApps)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics](DYLIBS/iOSDiagnostics)
- [/System/Library/PrivateFrameworks/iOSScreenSharing.framework/iOSScreenSharing](DYLIBS/iOSScreenSharing)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/iTunesStore](DYLIBS/iTunesStore)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/iTunesStoreUI](DYLIBS/iTunesStoreUI)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/EquationKit.framework/EquationKit](DYLIBS/EquationKit)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/KeynoteQuicklook.framework/KeynoteQuicklook](DYLIBS/KeynoteQuicklook)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/NumbersQuicklook.framework/NumbersQuicklook](DYLIBS/NumbersQuicklook)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/PagesQuicklook.framework/PagesQuicklook](DYLIBS/PagesQuicklook)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TQQuicklook.framework/TQQuicklook](DYLIBS/TQQuicklook)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSApplication.framework/TSApplication](DYLIBS/TSApplication)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCalculationEngine.framework/TSCalculationEngine](DYLIBS/TSCalculationEngine)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCharts.framework/TSCharts](DYLIBS/TSCharts)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSDrawables.framework/TSDrawables](DYLIBS/TSDrawables)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSKit.framework/TSKit](DYLIBS/TSKit)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSPersistence.framework/TSPersistence](DYLIBS/TSPersistence)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSStyles.framework/TSStyles](DYLIBS/TSStyles)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSTables.framework/TSTables](DYLIBS/TSTables)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText](DYLIBS/TSText)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit)
- [/System/Library/PrivateFrameworks/kperf.framework/kperf](DYLIBS/kperf)
- [/System/Library/PrivateFrameworks/kperfdata.framework/kperfdata](DYLIBS/kperfdata)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace)
- [/System/Library/PrivateFrameworks/libEDR.framework/libEDR](DYLIBS/libEDR)
- [/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector](DYLIBS/libmalloc_exclaves_introspector)
- [/System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime](DYLIBS/lighthouse_runtime)
- [/System/Library/PrivateFrameworks/oncrpc.framework/oncrpc](DYLIBS/oncrpc)
- [/System/Library/PrivateFrameworks/perfdata.framework/perfdata](DYLIBS/perfdata)
- [/System/Library/PrivateFrameworks/vCard.framework/vCard](DYLIBS/vCard)
- [/System/Library/ProceduralWallpaper/ProceduralWallpapers.bundle/ProceduralWallpapers](DYLIBS/ProceduralWallpapers)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMapsNavigationCompanionDataSource.bundle/NanoMapsNavigationCompanionDataSource](DYLIBS/NanoMapsNavigationCompanionDataSource)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMapsSampleDataSource.bundle/NanoMapsSampleDataSource](DYLIBS/NanoMapsSampleDataSource)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineHome.bundle/RelevanceEngineHome](DYLIBS/RelevanceEngineHome)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSolar.bundle/RelevanceEngineSolar](DYLIBS/RelevanceEngineSolar)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineWeather.bundle/RelevanceEngineWeather](DYLIBS/RelevanceEngineWeather)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport](DYLIBS/CaptiveNetworkSupport)
- [/System/Library/TextInput/TextInput_bo.bundle/TextInput_bo](DYLIBS/TextInput_bo)
- [/System/Library/TextInput/TextInput_ca.bundle/TextInput_ca](DYLIBS/TextInput_ca)
- [/System/Library/TextInput/TextInput_chr.bundle/TextInput_chr](DYLIBS/TextInput_chr)
- [/System/Library/TextInput/TextInput_cs.bundle/TextInput_cs](DYLIBS/TextInput_cs)
- [/System/Library/TextInput/TextInput_de.bundle/TextInput_de](DYLIBS/TextInput_de)
- [/System/Library/TextInput/TextInput_el.bundle/TextInput_el](DYLIBS/TextInput_el)
- [/System/Library/TextInput/TextInput_emoji.bundle/TextInput_emoji](DYLIBS/TextInput_emoji)
- [/System/Library/TextInput/TextInput_en.bundle/TextInput_en](DYLIBS/TextInput_en)
- [/System/Library/TextInput/TextInput_es.bundle/TextInput_es](DYLIBS/TextInput_es)
- [/System/Library/TextInput/TextInput_fr.bundle/TextInput_fr](DYLIBS/TextInput_fr)
- [/System/Library/TextInput/TextInput_haw.bundle/TextInput_haw](DYLIBS/TextInput_haw)
- [/System/Library/TextInput/TextInput_he.bundle/TextInput_he](DYLIBS/TextInput_he)
- [/System/Library/TextInput/TextInput_hi.bundle/TextInput_hi](DYLIBS/TextInput_hi)
- [/System/Library/TextInput/TextInput_intl.bundle/TextInput_intl](DYLIBS/TextInput_intl)
- [/System/Library/TextInput/TextInput_ja.bundle/TextInput_ja](DYLIBS/TextInput_ja)
- [/System/Library/TextInput/TextInput_ko.bundle/TextInput_ko](DYLIBS/TextInput_ko)
- [/System/Library/TextInput/TextInput_mr.bundle/TextInput_mr](DYLIBS/TextInput_mr)
- [/System/Library/TextInput/TextInput_mul.bundle/TextInput_mul](DYLIBS/TextInput_mul)
- [/System/Library/TextInput/TextInput_my.bundle/TextInput_my](DYLIBS/TextInput_my)
- [/System/Library/TextInput/TextInput_nl.bundle/TextInput_nl](DYLIBS/TextInput_nl)
- [/System/Library/TextInput/TextInput_pa.bundle/TextInput_pa](DYLIBS/TextInput_pa)
- [/System/Library/TextInput/TextInput_pt.bundle/TextInput_pt](DYLIBS/TextInput_pt)
- [/System/Library/TextInput/TextInput_si.bundle/TextInput_si](DYLIBS/TextInput_si)
- [/System/Library/TextInput/TextInput_sk.bundle/TextInput_sk](DYLIBS/TextInput_sk)
- [/System/Library/TextInput/TextInput_ta.bundle/TextInput_ta](DYLIBS/TextInput_ta)
- [/System/Library/TextInput/TextInput_th.bundle/TextInput_th](DYLIBS/TextInput_th)
- [/System/Library/TextInput/TextInput_tr.bundle/TextInput_tr](DYLIBS/TextInput_tr)
- [/System/Library/TextInput/TextInput_ug.bundle/TextInput_ug](DYLIBS/TextInput_ug)
- [/System/Library/TextInput/TextInput_vi.bundle/TextInput_vi](DYLIBS/TextInput_vi)
- [/System/Library/TextInput/TextInput_yue.bundle/TextInput_yue](DYLIBS/TextInput_yue)
- [/System/Library/TextInput/TextInput_zh.bundle/TextInput_zh](DYLIBS/TextInput_zh)
- [/System/Library/UserEventPlugins/AppleHDQGasGauge.plugin/AppleHDQGasGauge](DYLIBS/AppleHDQGasGauge)
- [/System/Library/VideoCodecs/H264SW.videocodec](DYLIBS/H264SW.videocodec)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec)
- [/System/Library/VideoDecoders/AV1SW.videodecoder](DYLIBS/AV1SW.videodecoder)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder)
- [/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder](DYLIBS/AppleProResHWDecoder.videodecoder)
- [/System/Library/VideoDecoders/AppleProResSWDecoder.videodecoder](DYLIBS/AppleProResSWDecoder.videodecoder)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder)
- [/System/Library/VideoDecoders/JPEGH1.videodecoder](DYLIBS/JPEGH1.videodecoder)
- [/System/Library/VideoDecoders/MP4VH8.videodecoder](DYLIBS/MP4VH8.videodecoder)
- [/System/Library/VideoDecoders/VCH263.videodecoder](DYLIBS/VCH263.videodecoder)
- [/System/Library/VideoDecoders/VCPMP4V.videodecoder](DYLIBS/VCPMP4V.videodecoder)
- [/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder](DYLIBS/AppleProResHWEncoder.videoencoder)
- [/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder](DYLIBS/AppleProResSWEncoder.videoencoder)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder)
- [/System/Library/VideoEncoders/JPEGH1.videoencoder](DYLIBS/JPEGH1.videoencoder)
- [/System/Library/VideoEncoders/VCH263.videoencoder](DYLIBS/VCH263.videoencoder)
- [/System/Library/VideoProcessors/BarcodeScanner.videoprocessor](DYLIBS/BarcodeScanner.videoprocessor)
- [/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait](DYLIBS/CCPortrait)
- [/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1](DYLIBS/CalibrationV1)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/DepthProcessorV2](DYLIBS/DepthProcessorV2)
- [/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5](DYLIBS/DisparityV5)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1](DYLIBS/IntelligentDistortionCorrectionV1)
- [/System/Library/VideoProcessors/MattingV2.bundle/MattingV2](DYLIBS/MattingV2)
- [/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter](DYLIBS/MetalFilter)
- [/System/Library/VideoProcessors/NRFV2.bundle/NRFV2](DYLIBS/NRFV2)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4)
- [/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5](DYLIBS/SDOFRenderingV5)
- [/System/Library/VideoProcessors/STF.bundle/STF](DYLIBS/STF)
- [/System/Library/VoiceServices/PlugIns/VoiceDial.vsplugin/VoiceDial](DYLIBS/VoiceDial)
- [/usr/lib/ACIPCBTLib.dylib](DYLIBS/ACIPCBTLib.dylib)
- [/usr/lib/AppleConvergedTransport.dylib](DYLIBS/AppleConvergedTransport.dylib)
- [/usr/lib/CarrierBundleUtilities.dylib](DYLIBS/CarrierBundleUtilities.dylib)
- [/usr/lib/dyld](DYLIBS/dyld)
- [/usr/lib/i18n/libBIG5.dylib](DYLIBS/libBIG5.dylib)
- [/usr/lib/i18n/libDECHanyu.dylib](DYLIBS/libDECHanyu.dylib)
- [/usr/lib/i18n/libDECKanji.dylib](DYLIBS/libDECKanji.dylib)
- [/usr/lib/i18n/libEUC.dylib](DYLIBS/libEUC.dylib)
- [/usr/lib/i18n/libEUCTW.dylib](DYLIBS/libEUCTW.dylib)
- [/usr/lib/i18n/libGBK2K.dylib](DYLIBS/libGBK2K.dylib)
- [/usr/lib/i18n/libHZ.dylib](DYLIBS/libHZ.dylib)
- [/usr/lib/i18n/libISO2022.dylib](DYLIBS/libISO2022.dylib)
- [/usr/lib/i18n/libJOHAB.dylib](DYLIBS/libJOHAB.dylib)
- [/usr/lib/i18n/libMSKanji.dylib](DYLIBS/libMSKanji.dylib)
- [/usr/lib/i18n/libUES.dylib](DYLIBS/libUES.dylib)
- [/usr/lib/i18n/libUTF1632.dylib](DYLIBS/libUTF1632.dylib)
- [/usr/lib/i18n/libUTF7.dylib](DYLIBS/libUTF7.dylib)
- [/usr/lib/i18n/libUTF8.dylib](DYLIBS/libUTF8.dylib)
- [/usr/lib/i18n/libUTF8MAC.dylib](DYLIBS/libUTF8MAC.dylib)
- [/usr/lib/i18n/libVIQR.dylib](DYLIBS/libVIQR.dylib)
- [/usr/lib/i18n/libZW.dylib](DYLIBS/libZW.dylib)
- [/usr/lib/i18n/libiconv_none.dylib](DYLIBS/libiconv_none.dylib)
- [/usr/lib/i18n/libiconv_std.dylib](DYLIBS/libiconv_std.dylib)
- [/usr/lib/i18n/libmapper_646.dylib](DYLIBS/libmapper_646.dylib)
- [/usr/lib/i18n/libmapper_none.dylib](DYLIBS/libmapper_none.dylib)
- [/usr/lib/i18n/libmapper_parallel.dylib](DYLIBS/libmapper_parallel.dylib)
- [/usr/lib/i18n/libmapper_serial.dylib](DYLIBS/libmapper_serial.dylib)
- [/usr/lib/i18n/libmapper_std.dylib](DYLIBS/libmapper_std.dylib)
- [/usr/lib/i18n/libmapper_zone.dylib](DYLIBS/libmapper_zone.dylib)
- [/usr/lib/libAHTRestore.dylib](DYLIBS/libAHTRestore.dylib)
- [/usr/lib/libARI.dylib](DYLIBS/libARI.dylib)
- [/usr/lib/libARIServer.dylib](DYLIBS/libARIServer.dylib)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib)
- [/usr/lib/libAWDProtobufBluetooth.dylib](DYLIBS/libAWDProtobufBluetooth.dylib)
- [/usr/lib/libAWDProtobufFacetime.dylib](DYLIBS/libAWDProtobufFacetime.dylib)
- [/usr/lib/libAWDProtobufGCK.dylib](DYLIBS/libAWDProtobufGCK.dylib)
- [/usr/lib/libAWDProtobufLocation.dylib](DYLIBS/libAWDProtobufLocation.dylib)
- [/usr/lib/libAWDSupport.dylib](DYLIBS/libAWDSupport.dylib)
- [/usr/lib/libAWDSupportFramework.dylib](DYLIBS/libAWDSupportFramework.dylib)
- [/usr/lib/libAXSafeCategoryBundle.dylib](DYLIBS/libAXSafeCategoryBundle.dylib)
- [/usr/lib/libAXSpeechManager.dylib](DYLIBS/libAXSpeechManager.dylib)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib)
- [/usr/lib/libAppPatch.dylib](DYLIBS/libAppPatch.dylib)
- [/usr/lib/libAppleArchive.dylib](DYLIBS/libAppleArchive.dylib)
- [/usr/lib/libAppleEXR.dylib](DYLIBS/libAppleEXR.dylib)
- [/usr/lib/libAppleSSEExt.dylib](DYLIBS/libAppleSSEExt.dylib)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib)
- [/usr/lib/libAudioStatistics.dylib](DYLIBS/libAudioStatistics.dylib)
- [/usr/lib/libAudioToolboxUtility.dylib](DYLIBS/libAudioToolboxUtility.dylib)
- [/usr/lib/libBASupport.dylib](DYLIBS/libBASupport.dylib)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib)
- [/usr/lib/libBBUpdaterDynamic_stubs.dylib](DYLIBS/libBBUpdaterDynamic_stubs.dylib)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib)
- [/usr/lib/libBasebandCommandDrivers.dylib](DYLIBS/libBasebandCommandDrivers.dylib)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib)
- [/usr/lib/libCRFSuite.dylib](DYLIBS/libCRFSuite.dylib)
- [/usr/lib/libCTGreenTeaLogger.dylib](DYLIBS/libCTGreenTeaLogger.dylib)
- [/usr/lib/libChineseTokenizer.dylib](DYLIBS/libChineseTokenizer.dylib)
- [/usr/lib/libCoreEntitlements.dylib](DYLIBS/libCoreEntitlements.dylib)
- [/usr/lib/libDHCPServer.A.dylib](DYLIBS/libDHCPServer.A.dylib)
- [/usr/lib/libETLDIAGLoggingDynamic.dylib](DYLIBS/libETLDIAGLoggingDynamic.dylib)
- [/usr/lib/libETLDLFDynamic.dylib](DYLIBS/libETLDLFDynamic.dylib)
- [/usr/lib/libETLDLOADCoreDumpDynamic.dylib](DYLIBS/libETLDLOADCoreDumpDynamic.dylib)
- [/usr/lib/libETLDLOADDynamic.dylib](DYLIBS/libETLDLOADDynamic.dylib)
- [/usr/lib/libETLDMCDynamic.dylib](DYLIBS/libETLDMCDynamic.dylib)
- [/usr/lib/libETLDynamic.dylib](DYLIBS/libETLDynamic.dylib)
- [/usr/lib/libETLEFSDumpDynamic.dylib](DYLIBS/libETLEFSDumpDynamic.dylib)
- [/usr/lib/libETLSAHDynamic.dylib](DYLIBS/libETLSAHDynamic.dylib)
- [/usr/lib/libFDR.dylib](DYLIBS/libFDR.dylib)
- [/usr/lib/libFDRDecode.dylib](DYLIBS/libFDRDecode.dylib)
- [/usr/lib/libFosl_dynamic.dylib](DYLIBS/libFosl_dynamic.dylib)
- [/usr/lib/libHDLCDynamic.dylib](DYLIBS/libHDLCDynamic.dylib)
- [/usr/lib/libHSFilerDynamic.dylib](DYLIBS/libHSFilerDynamic.dylib)
- [/usr/lib/libICEClient.dylib](DYLIBS/libICEClient.dylib)
- [/usr/lib/libIOABP.dylib](DYLIBS/libIOABP.dylib)
- [/usr/lib/libIOACIPC.dylib](DYLIBS/libIOACIPC.dylib)
- [/usr/lib/libIOACIPCBB.dylib](DYLIBS/libIOACIPCBB.dylib)
- [/usr/lib/libIOAccessoryManager.dylib](DYLIBS/libIOAccessoryManager.dylib)
- [/usr/lib/libIOReport.dylib](DYLIBS/libIOReport.dylib)
- [/usr/lib/libInFieldCollection.dylib](DYLIBS/libInFieldCollection.dylib)
- [/usr/lib/libKTLDynamic.dylib](DYLIBS/libKTLDynamic.dylib)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib)
- [/usr/lib/libMTLHud.dylib](DYLIBS/libMTLHud.dylib)
- [/usr/lib/libMatch.1.dylib](DYLIBS/libMatch.1.dylib)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib)
- [/usr/lib/libMobileCheckpoint.dylib](DYLIBS/libMobileCheckpoint.dylib)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib)
- [/usr/lib/libMobileGestaltExtensions.dylib](DYLIBS/libMobileGestaltExtensions.dylib)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib)
- [/usr/lib/libNFC_HAL.dylib](DYLIBS/libNFC_HAL.dylib)
- [/usr/lib/libPCITransport.dylib](DYLIBS/libPCITransport.dylib)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib)
- [/usr/lib/libPPM.dylib](DYLIBS/libPPM.dylib)
- [/usr/lib/libPPMDataModel.dylib](DYLIBS/libPPMDataModel.dylib)
- [/usr/lib/libParallelCompression.dylib](DYLIBS/libParallelCompression.dylib)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib)
- [/usr/lib/libRemoteTelephonyTransport.dylib](DYLIBS/libRemoteTelephonyTransport.dylib)
- [/usr/lib/libReverseProxyDevice.dylib](DYLIBS/libReverseProxyDevice.dylib)
- [/usr/lib/libRoseBooter.dylib](DYLIBS/libRoseBooter.dylib)
- [/usr/lib/libSCLM.dylib](DYLIBS/libSCLM.dylib)
- [/usr/lib/libSESShared.dylib](DYLIBS/libSESShared.dylib)
- [/usr/lib/libSLAMDynamic.dylib](DYLIBS/libSLAMDynamic.dylib)
- [/usr/lib/libSMC.dylib](DYLIBS/libSMC.dylib)
- [/usr/lib/libSoftwareUpdateSSO.dylib](DYLIBS/libSoftwareUpdateSSO.dylib)
- [/usr/lib/libSystem.B.dylib](DYLIBS/libSystem.B.dylib)
- [/usr/lib/libSystemHealth.dylib](DYLIBS/libSystemHealth.dylib)
- [/usr/lib/libTLE.dylib](DYLIBS/libTLE.dylib)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib)
- [/usr/lib/libTelephonyIOKitDynamic.dylib](DYLIBS/libTelephonyIOKitDynamic.dylib)
- [/usr/lib/libTelephonyUSBDynamic.dylib](DYLIBS/libTelephonyUSBDynamic.dylib)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib)
- [/usr/lib/libThaiTokenizer.dylib](DYLIBS/libThaiTokenizer.dylib)
- [/usr/lib/libWAPI.dylib](DYLIBS/libWAPI.dylib)
- [/usr/lib/libWISSupport.dylib](DYLIBS/libWISSupport.dylib)
- [/usr/lib/libWirelessAudioIPC.dylib](DYLIBS/libWirelessAudioIPC.dylib)
- [/usr/lib/libacmobileshim.dylib](DYLIBS/libacmobileshim.dylib)
- [/usr/lib/libafc.dylib](DYLIBS/libafc.dylib)
- [/usr/lib/libamsupport.dylib](DYLIBS/libamsupport.dylib)
- [/usr/lib/libapp_launch_measurement.dylib](DYLIBS/libapp_launch_measurement.dylib)
- [/usr/lib/libapple_nghttp2.dylib](DYLIBS/libapple_nghttp2.dylib)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib)
- [/usr/lib/libate.dylib](DYLIBS/libate.dylib)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib)
- [/usr/lib/libbsm.0.dylib](DYLIBS/libbsm.0.dylib)
- [/usr/lib/libbz2.1.0.dylib](DYLIBS/libbz2.1.0.dylib)
- [/usr/lib/libc++.1.dylib](DYLIBS/libc++.1.dylib)
- [/usr/lib/libc++abi.dylib](DYLIBS/libc++abi.dylib)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib)
- [/usr/lib/libcharset.1.dylib](DYLIBS/libcharset.1.dylib)
- [/usr/lib/libcmark-gfm.dylib](DYLIBS/libcmark-gfm.dylib)
- [/usr/lib/libcmph.dylib](DYLIBS/libcmph.dylib)
- [/usr/lib/libcompression.dylib](DYLIBS/libcompression.dylib)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib)
- [/usr/lib/libcoretls.dylib](DYLIBS/libcoretls.dylib)
- [/usr/lib/libcoretls_cfhelpers.dylib](DYLIBS/libcoretls_cfhelpers.dylib)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib)
- [/usr/lib/libcupolicy.dylib](DYLIBS/libcupolicy.dylib)
- [/usr/lib/libdns_services.dylib](DYLIBS/libdns_services.dylib)
- [/usr/lib/libdscsym.dylib](DYLIBS/libdscsym.dylib)
- [/usr/lib/libedit.3.dylib](DYLIBS/libedit.3.dylib)
- [/usr/lib/libenergytrace.dylib](DYLIBS/libenergytrace.dylib)
- [/usr/lib/libexpat.1.dylib](DYLIBS/libexpat.1.dylib)
- [/usr/lib/libexslt.0.dylib](DYLIBS/libexslt.0.dylib)
- [/usr/lib/libffi.dylib](DYLIBS/libffi.dylib)
- [/usr/lib/libfire7.dylib](DYLIBS/libfire7.dylib)
- [/usr/lib/libform.5.4.dylib](DYLIBS/libform.5.4.dylib)
- [/usr/lib/libgermantok.dylib](DYLIBS/libgermantok.dylib)
- [/usr/lib/libheimdal-asn1.dylib](DYLIBS/libheimdal-asn1.dylib)
- [/usr/lib/libheimdalasn1.dylib](DYLIBS/libheimdalasn1.dylib)
- [/usr/lib/libiconv.2.dylib](DYLIBS/libiconv.2.dylib)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib)
- [/usr/lib/libipsec.A.dylib](DYLIBS/libipsec.A.dylib)
- [/usr/lib/liblangid.dylib](DYLIBS/liblangid.dylib)
- [/usr/lib/libllvm-flatbuffers.dylib](DYLIBS/libllvm-flatbuffers.dylib)
- [/usr/lib/libllvm-lmdb.dylib](DYLIBS/libllvm-lmdb.dylib)
- [/usr/lib/liblockdown.dylib](DYLIBS/liblockdown.dylib)
- [/usr/lib/liblzma.5.dylib](DYLIBS/liblzma.5.dylib)
- [/usr/lib/libmarisa.dylib](DYLIBS/libmarisa.dylib)
- [/usr/lib/libmav_ipc_router_dynamic.dylib](DYLIBS/libmav_ipc_router_dynamic.dylib)
- [/usr/lib/libmd.dylib](DYLIBS/libmd.dylib)
- [/usr/lib/libmdns.dylib](DYLIBS/libmdns.dylib)
- [/usr/lib/libmecab.dylib](DYLIBS/libmecab.dylib)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib)
- [/usr/lib/libmorphun.dylib](DYLIBS/libmorphun.dylib)
- [/usr/lib/libmrc.dylib](DYLIBS/libmrc.dylib)
- [/usr/lib/libncurses.5.4.dylib](DYLIBS/libncurses.5.4.dylib)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib)
- [/usr/lib/libnfrestore.dylib](DYLIBS/libnfrestore.dylib)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib)
- [/usr/lib/libnfstorage.dylib](DYLIBS/libnfstorage.dylib)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib)
- [/usr/lib/libolaf.dylib](DYLIBS/libolaf.dylib)
- [/usr/lib/libpartition2_dynamic.dylib](DYLIBS/libpartition2_dynamic.dylib)
- [/usr/lib/libpcap.A.dylib](DYLIBS/libpcap.A.dylib)
- [/usr/lib/libperfcheck.dylib](DYLIBS/libperfcheck.dylib)
- [/usr/lib/libpmenergy.dylib](DYLIBS/libpmenergy.dylib)
- [/usr/lib/libpmsample.dylib](DYLIBS/libpmsample.dylib)
- [/usr/lib/libprequelite.dylib](DYLIBS/libprequelite.dylib)
- [/usr/lib/libprotobuf-lite.dylib](DYLIBS/libprotobuf-lite.dylib)
- [/usr/lib/libprotobuf.dylib](DYLIBS/libprotobuf.dylib)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib)
- [/usr/lib/librealtime_safety.dylib](DYLIBS/librealtime_safety.dylib)
- [/usr/lib/libresolv.9.dylib](DYLIBS/libresolv.9.dylib)
- [/usr/lib/libsandbox.1.dylib](DYLIBS/libsandbox.1.dylib)
- [/usr/lib/libsbuf.dylib](DYLIBS/libsbuf.dylib)
- [/usr/lib/libskit.dylib](DYLIBS/libskit.dylib)
- [/usr/lib/libsp.dylib](DYLIBS/libsp.dylib)
- [/usr/lib/libspindump.dylib](DYLIBS/libspindump.dylib)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib)
- [/usr/lib/libsysdiagnose.dylib](DYLIBS/libsysdiagnose.dylib)
- [/usr/lib/libsysmon.dylib](DYLIBS/libsysmon.dylib)
- [/usr/lib/libsystemstats.dylib](DYLIBS/libsystemstats.dylib)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib)
- [/usr/lib/libtidy.A.dylib](DYLIBS/libtidy.A.dylib)
- [/usr/lib/libtzupdate.dylib](DYLIBS/libtzupdate.dylib)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib)
- [/usr/lib/libutil.dylib](DYLIBS/libutil.dylib)
- [/usr/lib/libxml2.2.dylib](DYLIBS/libxml2.2.dylib)
- [/usr/lib/libxo.dylib](DYLIBS/libxo.dylib)
- [/usr/lib/libxpc_datastores.dylib](DYLIBS/libxpc_datastores.dylib)
- [/usr/lib/libxslt.1.dylib](DYLIBS/libxslt.1.dylib)
- [/usr/lib/libz.1.dylib](DYLIBS/libz.1.dylib)
- [/usr/lib/log/liblog_IOHIDFamily.dylib](DYLIBS/liblog_IOHIDFamily.dylib)
- [/usr/lib/log/liblog_SystemConfiguration.dylib](DYLIBS/liblog_SystemConfiguration.dylib)
- [/usr/lib/log/liblog_coreacc.dylib](DYLIBS/liblog_coreacc.dylib)
- [/usr/lib/log/liblog_geo.dylib](DYLIBS/liblog_geo.dylib)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib)
- [/usr/lib/log/liblog_mdns.dylib](DYLIBS/liblog_mdns.dylib)
- [/usr/lib/log/liblog_mdnsresponder.dylib](DYLIBS/liblog_mdnsresponder.dylib)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib)
- [/usr/lib/log/liblog_signpost.description.dylib](DYLIBS/liblog_signpost.description.dylib)
- [/usr/lib/log/liblog_signpost.dylib](DYLIBS/liblog_signpost.dylib)
- [/usr/lib/log/liblog_signpost.telemetry.dylib](DYLIBS/liblog_signpost.telemetry.dylib)
- [/usr/lib/log/liblog_srp.dylib](DYLIBS/liblog_srp.dylib)
- [/usr/lib/swift/libswiftARKit.dylib](DYLIBS/libswiftARKit.dylib)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib)
- [/usr/lib/swift/libswiftAppleArchive.dylib](DYLIBS/libswiftAppleArchive.dylib)
- [/usr/lib/swift/libswiftAssetsLibrary.dylib](DYLIBS/libswiftAssetsLibrary.dylib)
- [/usr/lib/swift/libswiftCallKit.dylib](DYLIBS/libswiftCallKit.dylib)
- [/usr/lib/swift/libswiftCarPlay.dylib](DYLIBS/libswiftCarPlay.dylib)
- [/usr/lib/swift/libswiftCompression.dylib](DYLIBS/libswiftCompression.dylib)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib)
- [/usr/lib/swift/libswiftCoreAudio.dylib](DYLIBS/libswiftCoreAudio.dylib)
- [/usr/lib/swift/libswiftCoreFoundation.dylib](DYLIBS/libswiftCoreFoundation.dylib)
- [/usr/lib/swift/libswiftCoreGraphics.dylib](DYLIBS/libswiftCoreGraphics.dylib)
- [/usr/lib/swift/libswiftCoreImage.dylib](DYLIBS/libswiftCoreImage.dylib)
- [/usr/lib/swift/libswiftCoreLocation.dylib](DYLIBS/libswiftCoreLocation.dylib)
- [/usr/lib/swift/libswiftCoreMIDI.dylib](DYLIBS/libswiftCoreMIDI.dylib)
- [/usr/lib/swift/libswiftCoreML.dylib](DYLIBS/libswiftCoreML.dylib)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib)
- [/usr/lib/swift/libswiftCryptoTokenKit.dylib](DYLIBS/libswiftCryptoTokenKit.dylib)
- [/usr/lib/swift/libswiftDarwin.dylib](DYLIBS/libswiftDarwin.dylib)
- [/usr/lib/swift/libswiftDemangle.dylib](DYLIBS/libswiftDemangle.dylib)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib)
- [/usr/lib/swift/libswiftFileProvider.dylib](DYLIBS/libswiftFileProvider.dylib)
- [/usr/lib/swift/libswiftGLKit.dylib](DYLIBS/libswiftGLKit.dylib)
- [/usr/lib/swift/libswiftGameplayKit.dylib](DYLIBS/libswiftGameplayKit.dylib)
- [/usr/lib/swift/libswiftIntents.dylib](DYLIBS/libswiftIntents.dylib)
- [/usr/lib/swift/libswiftMLCompute.dylib](DYLIBS/libswiftMLCompute.dylib)
- [/usr/lib/swift/libswiftMapKit.dylib](DYLIBS/libswiftMapKit.dylib)
- [/usr/lib/swift/libswiftMetal.dylib](DYLIBS/libswiftMetal.dylib)
- [/usr/lib/swift/libswiftMetalKit.dylib](DYLIBS/libswiftMetalKit.dylib)
- [/usr/lib/swift/libswiftMetricKit.dylib](DYLIBS/libswiftMetricKit.dylib)
- [/usr/lib/swift/libswiftModelIO.dylib](DYLIBS/libswiftModelIO.dylib)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib)
- [/usr/lib/swift/libswiftNearbyInteraction.dylib](DYLIBS/libswiftNearbyInteraction.dylib)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib)
- [/usr/lib/swift/libswiftOSLog.dylib](DYLIBS/libswiftOSLog.dylib)
- [/usr/lib/swift/libswiftObjectiveC.dylib](DYLIBS/libswiftObjectiveC.dylib)
- [/usr/lib/swift/libswiftObservation.dylib](DYLIBS/libswiftObservation.dylib)
- [/usr/lib/swift/libswiftPassKit.dylib](DYLIBS/libswiftPassKit.dylib)
- [/usr/lib/swift/libswiftQuartzCore.dylib](DYLIBS/libswiftQuartzCore.dylib)
- [/usr/lib/swift/libswiftRegexBuilder.dylib](DYLIBS/libswiftRegexBuilder.dylib)
- [/usr/lib/swift/libswiftSceneKit.dylib](DYLIBS/libswiftSceneKit.dylib)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib)
- [/usr/lib/swift/libswiftSpriteKit.dylib](DYLIBS/libswiftSpriteKit.dylib)
- [/usr/lib/swift/libswiftSwiftOnoneSupport.dylib](DYLIBS/libswiftSwiftOnoneSupport.dylib)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib)
- [/usr/lib/swift/libswiftSystem_Foundation.dylib](DYLIBS/libswiftSystem_Foundation.dylib)
- [/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib](DYLIBS/libswiftUniformTypeIdentifiers.dylib)
- [/usr/lib/swift/libswiftVideoToolbox.dylib](DYLIBS/libswiftVideoToolbox.dylib)
- [/usr/lib/swift/libswiftVision.dylib](DYLIBS/libswiftVision.dylib)
- [/usr/lib/swift/libswiftWatchKit.dylib](DYLIBS/libswiftWatchKit.dylib)
- [/usr/lib/swift/libswiftWebKit.dylib](DYLIBS/libswiftWebKit.dylib)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib)
- [/usr/lib/swift/libswift_Differentiation.dylib](DYLIBS/libswift_Differentiation.dylib)
- [/usr/lib/swift/libswift_RegexParser.dylib](DYLIBS/libswift_RegexParser.dylib)
- [/usr/lib/swift/libswift_StringProcessing.dylib](DYLIBS/libswift_StringProcessing.dylib)
- [/usr/lib/swift/libswiftos.dylib](DYLIBS/libswiftos.dylib)
- [/usr/lib/swift/libswiftsimd.dylib](DYLIBS/libswiftsimd.dylib)
- [/usr/lib/swift/~libswiftPencilKit.dylib](DYLIBS/~libswiftPencilKit.dylib)
- [/usr/lib/system/libcache.dylib](DYLIBS/libcache.dylib)
- [/usr/lib/system/libcommonCrypto.dylib](DYLIBS/libcommonCrypto.dylib)
- [/usr/lib/system/libcompiler_rt.dylib](DYLIBS/libcompiler_rt.dylib)
- [/usr/lib/system/libcopyfile.dylib](DYLIBS/libcopyfile.dylib)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib)
- [/usr/lib/system/libdispatch.dylib](DYLIBS/libdispatch.dylib)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib)
- [/usr/lib/system/libmacho.dylib](DYLIBS/libmacho.dylib)
- [/usr/lib/system/libremovefile.dylib](DYLIBS/libremovefile.dylib)
- [/usr/lib/system/libsystem_asl.dylib](DYLIBS/libsystem_asl.dylib)
- [/usr/lib/system/libsystem_blocks.dylib](DYLIBS/libsystem_blocks.dylib)
- [/usr/lib/system/libsystem_c.dylib](DYLIBS/libsystem_c.dylib)
- [/usr/lib/system/libsystem_collections.dylib](DYLIBS/libsystem_collections.dylib)
- [/usr/lib/system/libsystem_configuration.dylib](DYLIBS/libsystem_configuration.dylib)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib)
- [/usr/lib/system/libsystem_coreservices.dylib](DYLIBS/libsystem_coreservices.dylib)
- [/usr/lib/system/libsystem_darwin.dylib](DYLIBS/libsystem_darwin.dylib)
- [/usr/lib/system/libsystem_darwindirectory.dylib](DYLIBS/libsystem_darwindirectory.dylib)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib)
- [/usr/lib/system/libsystem_featureflags.dylib](DYLIBS/libsystem_featureflags.dylib)
- [/usr/lib/system/libsystem_info.dylib](DYLIBS/libsystem_info.dylib)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib)
- [/usr/lib/system/libsystem_m.dylib](DYLIBS/libsystem_m.dylib)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib)
- [/usr/lib/system/libsystem_networkextension.dylib](DYLIBS/libsystem_networkextension.dylib)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib)
- [/usr/lib/system/libsystem_platform.dylib](DYLIBS/libsystem_platform.dylib)
- [/usr/lib/system/libsystem_pthread.dylib](DYLIBS/libsystem_pthread.dylib)
- [/usr/lib/system/libsystem_sandbox.dylib](DYLIBS/libsystem_sandbox.dylib)
- [/usr/lib/system/libsystem_sanitizers.dylib](DYLIBS/libsystem_sanitizers.dylib)
- [/usr/lib/system/libsystem_symptoms.dylib](DYLIBS/libsystem_symptoms.dylib)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib)
- [/usr/lib/system/libunwind.dylib](DYLIBS/libunwind.dylib)
- [/usr/lib/system/libxpc.dylib](DYLIBS/libxpc.dylib)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib)
- [/usr/lib/updaters/libAppleTCONUpdater.dylib](DYLIBS/libAppleTCONUpdater.dylib)
- [/usr/lib/updaters/libAppleTconUARPUpdater.dylib](DYLIBS/libAppleTconUARPUpdater.dylib)
- [/usr/lib/updaters/libRoseUpdater.dylib](DYLIBS/libRoseUpdater.dylib)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib)
- [/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib](DYLIBS/libSavageRestoreInfo_iOS.dylib)
- [/usr/lib/updaters/libSavageUpdater_iOS.dylib](DYLIBS/libSavageUpdater_iOS.dylib)
- [/usr/lib/updaters/libT200Updater.dylib](DYLIBS/libT200Updater.dylib)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib)

</details>

## EOF
