# 18.0 (22A5282m) .vs 18.0 (22A5297f)

## IPSWs

- `iPhone16,2_18.0_22A5282m_Restore.ipsw`
- `iPhone16,2_18.0_22A5297f_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.0 *(22A5282m)* | 24.0.0 | 11215.0.31.522.1~1 | Thu, 30May2024 22:34:02 +0000 |
| 18.0 *(22A5297f)* | 24.0.0 | 11215.0.115.502.1~1 | Sun, 16Jun2024 20:49:29 +0000 |

### Kexts

#### ⬆️ Updated (90)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.iokit.IOUserEthernet`

```diff

-75.0.0.0.0
+76.0.0.0.0
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0xa40
-  __TEXT_EXEC.__text: 0x5468
+  __TEXT.__cstring: 0xa51
+  __TEXT_EXEC.__text: 0x53f4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb8
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__auth_got: 0x210
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20

```

>  `com.apple.driver.AppleDiskImages2`

```diff

-373.0.0.0.0
-  __TEXT.__cstring: 0x2090
+377.0.0.0.0
+  __TEXT.__cstring: 0x2000
   __TEXT.__os_log: 0x11a2
   __TEXT.__const: 0x10
-  __TEXT_EXEC.__text: 0xd270
+  __TEXT_EXEC.__text: 0xd3e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x498
   __DATA.__common: 0x118

```

>  `com.apple.security.AppleImage4`

```diff

-320.0.9.0.0
-  __TEXT.__const: 0x746f
-  __TEXT.__cstring: 0x5e93
-  __TEXT.__info_plist: 0x4e1
-  __TEXT_EXEC.__text: 0x244e4
+320.0.11.0.0
+  __TEXT.__const: 0x79f4
+  __TEXT.__cstring: 0x5ec4
+  __TEXT.__info_plist: 0x4ea
+  __TEXT_EXEC.__text: 0x24598
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6f8
   __DATA.__bss: 0x236

   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xb5c0
+  __DATA_CONST.__const: 0xb620
   __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__image4_exp: 0x10
   Symbols:   0
-  Functions: 1181
+  Functions: 1184
 

```

>  `com.apple.driver.AppleConvergedPCI`

```diff

-105.0.0.0.0
+106.0.0.0.0
   __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0x6c01
-  __TEXT_EXEC.__text: 0x3e5a8
+  __TEXT.__cstring: 0x6ba1
+  __TEXT_EXEC.__text: 0x3e558
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

```

>  `com.apple.driver.AppleSmartBatteryManagerEmbedded`

```diff

-1725.0.0.0.0
-  __TEXT.__cstring: 0x421c
-  __TEXT.__const: 0x14b0
+1730.0.0.0.2
+  __TEXT.__cstring: 0x4456
+  __TEXT.__const: 0x15c0
   __TEXT.__os_log: 0x25f9
-  __TEXT_EXEC.__text: 0x220dc
+  __TEXT_EXEC.__text: 0x22824
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x208
   __DATA.__common: 0x150
-  __DATA.__bss: 0x2f30
+  __DATA.__bss: 0x3170
   __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__mod_init_func: 0x40

   __DATA_CONST.__const: 0x2dc0
   __DATA_CONST.__kalloc_type: 0x340
   Symbols:   0
-  Functions: 383
+  Functions: 385
 

```

>  `com.apple.driver.AppleDCP`

```diff

-811.0.10.0.1
+811.0.17.0.0
   __TEXT.__cstring: 0x1664
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x5e8c
+  __TEXT_EXEC.__text: 0x5e48
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

```

>  `com.apple.filesystems.tmpfs`

```diff

 79.0.0.0.0
-  __TEXT.__cstring: 0x5da
+  __TEXT.__cstring: 0x4b7
   __TEXT.__const: 0x40
   __TEXT.__os_log: 0x20a
-  __TEXT_EXEC.__text: 0x9770
+  __TEXT_EXEC.__text: 0x95b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x180
   __DATA.__bss: 0x8

   __DATA_CONST.__const: 0x4d0
   __DATA_CONST.__kalloc_type: 0x480
   Symbols:   0
-  Functions: 157
+  Functions: 156
 

```

>  `com.apple.iokit.IOPCIFamily`

```diff

 664.0.2.0.0
   __TEXT.__const: 0x710
   __TEXT.__cstring: 0x52ca
-  __TEXT_EXEC.__text: 0x2e168
+  __TEXT_EXEC.__text: 0x2e23c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x218

```

>  `com.apple.iokit.IOSkywalkFamily`

```diff

-508.0.0.0.0
+508.0.2.0.0
   __TEXT.__cstring: 0x1ade
   __TEXT.__const: 0xd40
-  __TEXT_EXEC.__text: 0x35dfc
+  __TEXT_EXEC.__text: 0x35e10
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe8
   __DATA.__common: 0x6b0
   __DATA.__bss: 0x9c
-  __DATA_CONST.__auth_got: 0xa08
+  __DATA_CONST.__auth_got: 0xa10
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x130

```

>  `com.apple.nke.ppp`

```diff

 1016.0.0.0.0
-  __TEXT.__cstring: 0x1a27
+  __TEXT.__cstring: 0x1968
   __TEXT.__const: 0x230
-  __TEXT_EXEC.__text: 0x7660
+  __TEXT_EXEC.__text: 0x74c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2d0
   __DATA.__bss: 0xa1
   __DATA.__common: 0x24
-  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__kalloc_type: 0x300

```

>  `com.apple.driver.AppleAVD`

```diff

-793.9.0.0.0
-  __TEXT.__const: 0x87bee
-  __TEXT.__cstring: 0x4b62
-  __TEXT.__os_log: 0x10103
-  __TEXT_EXEC.__text: 0x48524
+795.1.0.0.0
+  __TEXT.__const: 0x86e6e
+  __TEXT.__cstring: 0x5135
+  __TEXT.__os_log: 0x116ce
+  __TEXT_EXEC.__text: 0x40f34
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x1c8c
-  __DATA.__common: 0x80
+  __DATA.__data: 0x12dc
+  __DATA.__common: 0x78
   __DATA.__bss: 0x14
-  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x2a70
-  __DATA_CONST.__kalloc_var: 0xcd0
-  __DATA_CONST.__kalloc_type: 0x2480
+  __DATA_CONST.__const: 0x2a88
+  __DATA_CONST.__kalloc_var: 0xb90
+  __DATA_CONST.__kalloc_type: 0x2400
   Symbols:   0
-  Functions: 1397
+  Functions: 1339
 

```

>  `com.apple.driver.AppleInputDeviceSupport`

```diff

 8100.31.0.0.0
-  __TEXT.__cstring: 0x1c3d
+  __TEXT.__cstring: 0x1c3f
   __TEXT.__const: 0x60
   __TEXT.__os_log: 0x63a
   __TEXT_EXEC.__text: 0x16928

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-395.12.2.0.0
-  __TEXT.__cstring: 0x4240
-  __TEXT.__const: 0x2158
-  __TEXT_EXEC.__text: 0x2069c
+395.20.1.0.0
+  __TEXT.__cstring: 0x3ef5
+  __TEXT.__const: 0x2148
+  __TEXT_EXEC.__text: 0x1faa8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe0
-  __DATA.__common: 0x26f8
+  __DATA.__common: 0x26d0
   __DATA.__bss: 0x38
-  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x28
-  __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x1778
-  __DATA_CONST.__kalloc_type: 0x880
+  __DATA_CONST.__mod_init_func: 0x20
+  __DATA_CONST.__mod_term_func: 0x20
+  __DATA_CONST.__const: 0x1628
+  __DATA_CONST.__kalloc_type: 0x7c0
   Symbols:   0
-  Functions: 723
+  Functions: 690
 

```

>  `com.apple.driver.DCPAVFamilyProxy`

```diff

-349.0.0.0.0
+349.0.4.0.0
   __TEXT.__const: 0x278
   __TEXT.__cstring: 0x2399
   __TEXT.__os_log: 0x12b0
-  __TEXT_EXEC.__text: 0x16cbc
+  __TEXT_EXEC.__text: 0x16cd0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x308

```

>  `com.apple.filesystems.apfs`

```diff

-2301.0.0.0.7
-  __TEXT.__const: 0x6c8
-  __TEXT.__cstring: 0x4816f
-  __TEXT_EXEC.__text: 0x138b5c
+2309.0.0.502.1
+  __TEXT.__const: 0x790
+  __TEXT.__cstring: 0x48053
+  __TEXT_EXEC.__text: 0x13983c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x690
   __DATA.__bss: 0xc60
-  __DATA_CONST.__auth_got: 0x1048
+  __DATA_CONST.__auth_got: 0x1050
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x6038
+  __DATA_CONST.__const: 0x6058
   __DATA_CONST.__kalloc_type: 0x4c80
   __DATA_CONST.__kalloc_var: 0x2800
   Symbols:   0
-  Functions: 2256
+  Functions: 2261
 

```

>  `com.apple.driver.ASIOKit`

```diff

-12.22.0.0.0
+12.26.0.0.0
   __TEXT.__cstring: 0x239
   __TEXT.__const: 0x7c40
-  __TEXT_EXEC.__text: 0x33624
+  __TEXT_EXEC.__text: 0x317e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x60

   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x3278
+  __DATA_CONST.__const: 0x3038
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
   Functions: 88

```

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-733.0.0.0.0
+733.0.4.0.1
   __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x86dc
-  __TEXT.__os_log: 0x3dcc
-  __TEXT_EXEC.__text: 0x35de8
+  __TEXT.__cstring: 0x8861
+  __TEXT.__os_log: 0x3e3b
+  __TEXT_EXEC.__text: 0x36500
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
   __DATA.__common: 0x1d8

   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
   Symbols:   0
-  Functions: 520
+  Functions: 522
 

```

>  `com.apple.AUC`

```diff

-542.4.0.0.0
-  __TEXT.__cstring: 0x947
+542.5.0.0.0
+  __TEXT.__cstring: 0x8ca
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x55e0
+  __TEXT_EXEC.__text: 0x5588
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc5
   __DATA.__common: 0xb0

```

>  `com.apple.driver.AppleHapticsSupportLEAP`

```diff

-9.17.0.0.0
-  __TEXT.__const: 0x1f4
-  __TEXT.__cstring: 0x4385
+9.19.0.0.0
+  __TEXT.__const: 0x204
+  __TEXT.__cstring: 0x4405
   __TEXT.__os_log: 0x82e
-  __TEXT_EXEC.__text: 0x32284
+  __TEXT_EXEC.__text: 0x324c0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x800
+  __DATA.__data: 0x810
   __DATA.__common: 0x5f0
   __DATA.__bss: 0x1
   __DATA_CONST.__auth_got: 0x348

```

>  `com.apple.driver.AppleSMC`

```diff

-725.0.0.0.0
+726.0.0.0.0
   __TEXT.__cstring: 0x859f
   __TEXT.__const: 0x1e4
   __TEXT.__os_log: 0xd26
-  __TEXT_EXEC.__text: 0x298e0
+  __TEXT_EXEC.__text: 0x298d4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x4b8

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-8.11.4.0.0
-  __TEXT.__os_log: 0x30d37
-  __TEXT.__cstring: 0xabd8
-  __TEXT.__const: 0x5b0
-  __TEXT_EXEC.__text: 0xa05c8
+8.13.2.0.0
+  __TEXT.__os_log: 0x30df1
+  __TEXT.__cstring: 0xaa49
+  __TEXT.__const: 0x5f0
+  __TEXT_EXEC.__text: 0xa0088
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3058
   __DATA.__common: 0x3c8
   __DATA.__bss: 0x270
-  __DATA_CONST.__auth_got: 0x8b0
+  __DATA_CONST.__auth_got: 0x878
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x98
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x5f38
+  __DATA_CONST.__const: 0x6078
   __DATA_CONST.__kalloc_type: 0x2c80
-  __DATA_CONST.__kalloc_var: 0x2940
+  __DATA_CONST.__kalloc_var: 0x28a0
   Symbols:   0
-  Functions: 1811
+  Functions: 1821
 

```

>  `com.apple.iokit.IOSurface`

```diff

-368.0.0.0.0
-  __TEXT.__cstring: 0x4fbb
+368.0.2.0.0
+  __TEXT.__cstring: 0x4f14
   __TEXT.__const: 0x48
   __TEXT.__os_log: 0x530
-  __TEXT_EXEC.__text: 0x2d538
+  __TEXT_EXEC.__text: 0x2d228
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x178
   __DATA.__common: 0x3e8

```

>  `com.apple.kernel`

```diff

-11215.0.31.522.1
-  __TEXT.__const: 0x33af0
+11215.0.115.502.1
+  __TEXT.__const: 0x33b90
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x6b6db
-  __TEXT.__os_log: 0x26ce8
-  __TEXT.__eh_frame: 0x4c0
+  __TEXT.__cstring: 0x6b9b9
+  __TEXT.__os_log: 0x26bed
+  __TEXT.__eh_frame: 0x5a0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c0
-  __DATA_CONST.__const: 0xa2390
+  __DATA_CONST.__const: 0xa2320
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x13100
+  __DATA_CONST.__kalloc_type: 0x13340
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7fb5d4
+  __TEXT_EXEC.__text: 0x7fa8f4
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x184e1
+  __DATA.__data: 0x184e9
   __DATA.__lock_grp: 0x57a8
   __DATA.__percpu: 0x6e48
-  __DATA.__common: 0x584d8
-  __DATA.__bss: 0x3f800
+  __DATA.__common: 0x584f8
+  __DATA.__bss: 0x3f7b0
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init_entry_set: 0x10758
   __BOOTDATA.__init: 0x5b058

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x4531c
+  __LINKINFO.__symbolsets: 0x45329
+  __LATE_CONST.__late_const: 0xa8
   Symbols:   0
-  Functions: 19810
+  Functions: 19818
 

```

>  `com.apple.iokit.CoreAnalyticsFamily`

```diff

-410.0.0.0.0
+412.0.0.0.0
   __TEXT.__cstring: 0x1cd3
   __TEXT.__os_log: 0x1639
-  __TEXT_EXEC.__text: 0x759c
+  __TEXT_EXEC.__text: 0x7680
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x108

```

>  `com.apple.driver.AudioDMAController-T8130`

```diff

-400.94.0.0.0
+400.97.0.0.0
   __TEXT.__const: 0x1d8
   __TEXT.__cstring: 0x32d3
-  __TEXT_EXEC.__text: 0x15b7c
+  __TEXT_EXEC.__text: 0x15c70
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x178

```

>  `com.apple.iokit.IOUSBHostFamily`

```diff

-1402.0.0.0.0
-  __TEXT.__cstring: 0x9b8c
+1402.0.2.0.0
+  __TEXT.__cstring: 0x9afc
   __TEXT.__os_log: 0x81a1
   __TEXT.__const: 0xa90
-  __TEXT_EXEC.__text: 0x991ec
+  __TEXT_EXEC.__text: 0x99214
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x310
   __DATA.__common: 0x930

   __DATA_CONST.__kalloc_type: 0x1c40
   __DATA_CONST.__kalloc_var: 0x280
   Symbols:   0
-  Functions: 1949
+  Functions: 1948
 

```

>  `com.apple.driver.usb.AppleUSBCommon`

```diff

-1402.0.0.0.0
+1402.0.2.0.0
   __TEXT.__cstring: 0x301
   __TEXT.__os_log: 0xc6
-  __TEXT_EXEC.__text: 0x54b8
+  __TEXT_EXEC.__text: 0x5510
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x110

```

>  `com.apple.driver.AppleCallbackPowerSource`

```diff

-1725.0.0.0.0
-  __TEXT.__cstring: 0xf5f
+1730.0.0.0.2
+  __TEXT.__cstring: 0xf76
   __TEXT.__os_log: 0x76
-  __TEXT_EXEC.__text: 0x4b2c
+  __TEXT_EXEC.__text: 0x4b50
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x190
-  __DATA.__bss: 0x13f0
+  __DATA.__bss: 0x1408
   __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x10

```

>  `com.apple.driver.AppleIDV`

```diff

-7.31.3.0.0
+7.34.0.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x137d
+  __TEXT.__cstring: 0x137b
   __TEXT_EXEC.__text: 0x84b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4

```

>  `com.apple.driver.DiskImages`

```diff

 662.0.0.0.0
-  __TEXT.__cstring: 0xc34
-  __TEXT_EXEC.__text: 0x9b74
+  __TEXT.__cstring: 0xaff
+  __TEXT_EXEC.__text: 0x9a6c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128
-  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30

```

>  `com.apple.driver.ApplePPMCPMS`

```diff

-931.0.0.0.0
-  __TEXT.__const: 0xe50
-  __TEXT.__cstring: 0xd065
+931.0.4.0.0
+  __TEXT.__const: 0xe80
+  __TEXT.__cstring: 0xd087
   __TEXT.__os_log: 0x1fad
-  __TEXT_EXEC.__text: 0x45f2c
+  __TEXT_EXEC.__text: 0x45fe0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x156
   __DATA.__common: 0x4a8

   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__mod_init_func: 0xd0
   __DATA_CONST.__mod_term_func: 0xa0
-  __DATA_CONST.__const: 0x4cc0
+  __DATA_CONST.__const: 0x4cd0
   __DATA_CONST.__kalloc_type: 0x900
   Symbols:   0
   Functions: 1651

```

>  `com.apple.driver.AppleS8000AES`

```diff

 131.0.0.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x1301
-  __TEXT_EXEC.__text: 0x44fc
+  __TEXT_EXEC.__text: 0x453c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x200
   __DATA.__common: 0x60

```

>  `com.apple.driver.AppleBasebandPCI`

```diff

-807.0.0.0.0
-  __TEXT.__cstring: 0xc352
+809.0.0.0.0
+  __TEXT.__cstring: 0xc23c
   __TEXT.__const: 0x5009
-  __TEXT_EXEC.__text: 0x8883c
+  __TEXT_EXEC.__text: 0x88670
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3f8
   __DATA.__common: 0x648

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.0.30.0.1
+1827.0.41.0.1
   __TEXT.__cstring: 0x3aba
   __TEXT.__const: 0x864
-  __TEXT_EXEC.__text: 0x3d4d0
+  __TEXT_EXEC.__text: 0x3d4f4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x39c
   __DATA.__common: 0xe8

```

>  `com.apple.driver.AppleJPEGDriver`

```diff

   __TEXT.__os_log: 0xc16a
   __TEXT.__cstring: 0x324f
   __TEXT.__const: 0x4534
-  __TEXT_EXEC.__text: 0x33b2c
+  __TEXT_EXEC.__text: 0x33b60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x8b08
   __DATA.__common: 0x2b8

```

>  `com.apple.driver.FairPlayIOKit`

```diff

 72.8.0.0.0
   __TEXT.__cstring: 0x1c95
-  __TEXT.__const: 0x499b0
-  __TEXT_EXEC.__text: 0x1ad084
+  __TEXT.__const: 0x49a20
+  __TEXT_EXEC.__text: 0x1ad63c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x12d0
-  __DATA.__common: 0x5fd8
+  __DATA.__data: 0x12e0
+  __DATA.__common: 0x5fd0
   __DATA.__bss: 0x38
   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x138b0
+  __DATA_CONST.__const: 0x139e0
   __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x370
   Symbols:   0
-  Functions: 436
+  Functions: 438
 

```

>  `com.apple.filesystems.hfs.kext`

```diff

-667.0.0.0.1
-  __TEXT.__const: 0x1a98
-  __TEXT.__cstring: 0xa17d
-  __TEXT_EXEC.__text: 0x51dac
+670.0.0.0.0
+  __TEXT.__const: 0x1a90
+  __TEXT.__cstring: 0xa072
+  __TEXT_EXEC.__text: 0x51aac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

```

>  `com.apple.driver.AppleOLYHAL`

```diff

-336.19.0.0.0
-  __TEXT.__const: 0x798
-  __TEXT.__cstring: 0x4801
-  __TEXT_EXEC.__text: 0x1c7c4
+336.22.4.1.0
+  __TEXT.__const: 0x7a8
+  __TEXT.__cstring: 0x4826
+  __TEXT_EXEC.__text: 0x1c998
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

```

>  `com.apple.driver.AppleSPURose`

```diff

-1013.0.0.0.1
+1014.0.1.0.0
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x1f7c
   __TEXT.__os_log: 0x1431
-  __TEXT_EXEC.__text: 0x179cc
+  __TEXT_EXEC.__text: 0x179e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x268

```

>  `com.apple.filesystems.lifs`

```diff

-411.0.0.0.4
+432.0.0.0.2
   __TEXT.__os_log: 0x1278
-  __TEXT.__cstring: 0x22bb
+  __TEXT.__cstring: 0x21bd
   __TEXT.__const: 0x2d0
-  __TEXT_EXEC.__text: 0x1ac80
+  __TEXT_EXEC.__text: 0x1a8b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138

   __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__kalloc_type: 0xb40
   Symbols:   0
-  Functions: 399
+  Functions: 400
 

```

>  `com.apple.iokit.IOAccessoryPortUSB`

```diff

-1000.0.0.0.0
-  __TEXT.__cstring: 0x6a0
-  __TEXT_EXEC.__text: 0x27f4
+1003.0.0.0.0
+  __TEXT.__cstring: 0x6a7
+  __TEXT_EXEC.__text: 0x2808
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x20a
   __DATA.__common: 0x48

```

>  `com.apple.iokit.IOMikeyBusFamily`

```diff

 103.0.0.0.0
-  __TEXT.__cstring: 0x109d
+  __TEXT.__cstring: 0x100a
   __TEXT.__os_log: 0x3de
   __TEXT.__const: 0x208
-  __TEXT_EXEC.__text: 0x1e9e4
+  __TEXT_EXEC.__text: 0x1e874
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x488

```

>  `com.apple.driver.IODARTFamily`

```diff

-349.0.0.0.0
-  __TEXT.__cstring: 0x1ffa
+350.0.2.0.0
+  __TEXT.__cstring: 0x1f67
   __TEXT.__const: 0x14
-  __TEXT_EXEC.__text: 0x13630
+  __TEXT_EXEC.__text: 0x135a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x410
   Symbols:   0
-  Functions: 376
+  Functions: 374
 

```

>  `com.apple.driver.AppleEmbeddedPCIE`

```diff

-824.0.1.0.1
+824.0.7.0.0
   __TEXT.__cstring: 0x57b3
   __TEXT.__const: 0x198
-  __TEXT_EXEC.__text: 0x13d6c
+  __TEXT_EXEC.__text: 0x13da0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x188

```

>  `com.apple.driver.AppleSmartIO2`

```diff

 140.0.0.0.0
   __TEXT.__cstring: 0x451b
   __TEXT.__const: 0x60
-  __TEXT_EXEC.__text: 0xc4b0
+  __TEXT_EXEC.__text: 0xc54c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7f8
   __DATA.__common: 0x1a0

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-148.0.41.0.0
-  __TEXT.__cstring: 0x16484
-  __TEXT.__const: 0x4f738
-  __TEXT_EXEC.__text: 0xd5e6c
+148.0.45.0.0
+  __TEXT.__cstring: 0x1661b
+  __TEXT.__const: 0x4f518
+  __TEXT_EXEC.__text: 0xd6390
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1fe40
   __DATA.__common: 0x20a8

   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__mod_init_func: 0x570
   __DATA_CONST.__mod_term_func: 0x548
-  __DATA_CONST.__const: 0x210f8
-  __DATA_CONST.__kalloc_type: 0x3bc0
+  __DATA_CONST.__const: 0x21100
+  __DATA_CONST.__kalloc_type: 0x3c40
   __DATA_CONST.__kalloc_var: 0x500
   Symbols:   0
-  Functions: 6001
+  Functions: 6009
 

```

>  `com.apple.driver.AppleM68Buttons`

```diff

-125.0.0.0.0
-  __TEXT.__cstring: 0x48ee
+126.0.0.0.0
+  __TEXT.__cstring: 0x4907
   __TEXT.__const: 0x140
   __TEXT.__os_log: 0x606
-  __TEXT_EXEC.__text: 0x1bf78
+  __TEXT_EXEC.__text: 0x1c368
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xca
   __DATA.__common: 0x90
-  __DATA.__bss: 0x91
+  __DATA.__bss: 0x99
   __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x1400
   Symbols:   0
-  Functions: 314
+  Functions: 315
 

```

>  `com.apple.security.sandbox`

```diff

-2401.0.31.0.1
-  __TEXT.__const: 0x18ba79
-  __TEXT.__cstring: 0x6f41
+2401.0.37.502.1
+  __TEXT.__const: 0x18bd51
+  __TEXT.__cstring: 0x6e51
   __TEXT.__os_log: 0x2029
-  __TEXT_EXEC.__text: 0x3062c
+  __TEXT_EXEC.__text: 0x30468
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x144c0

```

>  `com.apple.driver.AppleARMPlatform`

```diff

   __TEXT.__const: 0x16f8
   __TEXT.__os_log: 0x13fe
   __TEXT.__cstring: 0xcadd
-  __TEXT_EXEC.__text: 0x52944
+  __TEXT_EXEC.__text: 0x52a4c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6c8
   __DATA.__common: 0xca0

```

>  `com.apple.driver.AppleAOPAudio`

```diff

 400.7.0.0.0
-  __TEXT.__cstring: 0xc5b3
+  __TEXT.__cstring: 0xc5bc
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
   __TEXT_EXEC.__text: 0x32968

```

>  `com.apple.driver.AppleSEPManager`

```diff

-834.0.0.0.1
-  __TEXT.__cstring: 0xf955
-  __TEXT.__const: 0x6b0f
-  __TEXT_EXEC.__text: 0x4640c
+840.0.0.0.0
+  __TEXT.__cstring: 0xfaf3
+  __TEXT.__const: 0x7094
+  __TEXT_EXEC.__text: 0x4692c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x168
   __DATA.__common: 0xc48

   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0x9650
+  __DATA_CONST.__const: 0x9708
   __DATA_CONST.__kalloc_type: 0xdc0
   __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 2305
+  Functions: 2319
 

```

>  `com.apple.iokit.IOStorageFamily`

```diff

-315.0.0.0.0
+317.0.0.0.0
   __TEXT.__cstring: 0x1620
   __TEXT.__const: 0x2e0
-  __TEXT_EXEC.__text: 0x1d5ec
+  __TEXT_EXEC.__text: 0x1d658
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x170
   __DATA.__common: 0x218

```

>  `com.apple.driver.ApplePMGR`

```diff

-1555.0.2.0.2
+1555.0.15.0.0
   __TEXT.__const: 0x248
-  __TEXT.__cstring: 0xe6eb
-  __TEXT_EXEC.__text: 0x52650
+  __TEXT.__cstring: 0xe858
+  __TEXT_EXEC.__text: 0x527fc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x100
   __DATA.__common: 0x420
   __DATA.__bss: 0x40
   __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x7788
   __DATA_CONST.__kalloc_type: 0x680
-  __DATA_CONST.__kalloc_var: 0xdc0
+  __DATA_CONST.__kalloc_var: 0xe10
   Symbols:   0
-  Functions: 2159
+  Functions: 2163
 

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-395.12.2.0.0
-  __TEXT.__cstring: 0x8221
+395.20.1.0.0
+  __TEXT.__cstring: 0x824b
   __TEXT.__const: 0x800
-  __TEXT_EXEC.__text: 0x22670
+  __TEXT_EXEC.__text: 0x2256c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2900
-  __DATA.__common: 0x1c9a4
+  __DATA.__common: 0x1c924
   __DATA.__bss: 0x18
   __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x5dd0
+  __DATA_CONST.__const: 0x5e00
   __DATA_CONST.__kalloc_type: 0xac0
   Symbols:   0
-  Functions: 1131
+  Functions: 1134
 

```

>  `com.apple.driver.AppleInterruptControllerV3`

```diff

 91.0.0.0.0
   __TEXT.__cstring: 0x9b8
-  __TEXT_EXEC.__text: 0x4190
+  __TEXT_EXEC.__text: 0x4204
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

```

>  `com.apple.iokit.IONetworkingFamily`

```diff

 185.0.0.0.0
-  __TEXT.__cstring: 0x127d
+  __TEXT.__cstring: 0x1113
   __TEXT.__const: 0x44
-  __TEXT_EXEC.__text: 0x1d19c
+  __TEXT_EXEC.__text: 0x1d008
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x3b8

   __DATA_CONST.__kalloc_type: 0xa80
   __DATA_CONST.__kalloc_var: 0x230
   Symbols:   0
-  Functions: 870
+  Functions: 861
 

```

>  `com.apple.kec.corecrypto`

```diff

-1736.0.22.0.0
+1736.0.27.0.1
   __TEXT.__cstring: 0x46c3
   __TEXT.__const: 0x144b0
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x54ac8
+  __TEXT_EXEC.__text: 0x54a48
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2df0
   __DATA.__bss: 0x2960

```

>  `com.apple.iokit.IOSCSIArchitectureModelFamily`

```diff

 498.0.0.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x1441
-  __TEXT_EXEC.__text: 0x185b4
+  __TEXT_EXEC.__text: 0x188c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x418
   __DATA.__common: 0x1c8

```

>  `com.apple.driver.AppleBasebandPCIMAVControl`

```diff

-807.0.0.0.0
+809.0.0.0.0
   __TEXT.__const: 0x262a
-  __TEXT.__cstring: 0x6820
-  __TEXT_EXEC.__text: 0x510e0
+  __TEXT.__cstring: 0x67ee
+  __TEXT_EXEC.__text: 0x511fc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x140
   __DATA.__common: 0x100

```

>  `com.apple.driver.AppleConvergedIPCOLYBTControl`

```diff

-105.0.0.0.0
-  __TEXT.__cstring: 0x7a9f
+106.0.0.0.0
+  __TEXT.__cstring: 0x7b2d
   __TEXT.__const: 0x98
-  __TEXT_EXEC.__text: 0x4716c
+  __TEXT_EXEC.__text: 0x47870
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x4c50
+  __DATA_CONST.__const: 0x4c58
   __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x500
   Symbols:   0
-  Functions: 968
+  Functions: 969
 

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-3.19.5.0.0
-  __TEXT.__cstring: 0x194aa
-  __TEXT.__os_log: 0x1526d
-  __TEXT.__const: 0xa050
-  __TEXT_EXEC.__text: 0x986d0
+3.25.1.0.0
+  __TEXT.__cstring: 0x190ab
+  __TEXT.__os_log: 0x153bf
+  __TEXT.__const: 0xa060
+  __TEXT_EXEC.__text: 0x95dfc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a0
   __DATA.__common: 0x4a0

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0xa220
+  __DATA_CONST.__const: 0xacb8
   __DATA_CONST.__kalloc_type: 0x1300
   __DATA_CONST.__kalloc_var: 0xd70
   Symbols:   0
-  Functions: 1924
+  Functions: 1860
 

```

>  `com.apple.kec.pthread`

```diff

 535.0.0.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x850
-  __TEXT_EXEC.__text: 0x5dec
+  __TEXT.__cstring: 0x72d
+  __TEXT_EXEC.__text: 0x5c28
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12c
   __DATA.__common: 0x30

```

>  `com.apple.driver.AppleSARService`

```diff

-1163.1.0.0.0
+1168.0.0.0.0
   __TEXT.__const: 0x750
-  __TEXT.__cstring: 0x9ae2
-  __TEXT.__os_log: 0xb872
+  __TEXT.__cstring: 0x9b1f
+  __TEXT.__os_log: 0xb8af
   __TEXT.__ustring: 0x8
-  __TEXT_EXEC.__text: 0x53b0c
+  __TEXT_EXEC.__text: 0x53c84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x5f0

```

>  `com.apple.driver.AppleBasebandPCIMAVPDP`

```diff

-807.0.0.0.0
+809.0.0.0.0
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x4c64
-  __TEXT_EXEC.__text: 0x245dc
+  __TEXT.__cstring: 0x4bd1
+  __TEXT_EXEC.__text: 0x2456c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

```

>  `com.apple.driver.AppleIISController`

```diff

 400.1.0.0.0
   __TEXT.__cstring: 0x93f
-  __TEXT_EXEC.__text: 0x6fd8
+  __TEXT_EXEC.__text: 0x7064
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x100

```

>  `com.apple.driver.AppleFirmwareUpdateKext`

```diff

-1139.0.0.502.1
-  __TEXT.__cstring: 0x8f8
-  __TEXT_EXEC.__text: 0x25cc
+1155.0.0.0.0
+  __TEXT.__cstring: 0x95a
+  __TEXT_EXEC.__text: 0x2738
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
   Symbols:   0
-  Functions: 67
+  Functions: 72
 

```

>  `com.apple.driver.AppleT8110DART`

```diff

-447.0.0.0.1
+452.0.1.0.0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2757
-  __TEXT_EXEC.__text: 0xd25c
+  __TEXT.__cstring: 0x276b
+  __TEXT_EXEC.__text: 0xd390
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

```

>  `com.apple.driver.corecapture`

```diff

-1180.59.0.0.0
+1180.60.0.0.0
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x1ec9
   __TEXT.__os_log: 0x4094
-  __TEXT_EXEC.__text: 0x26e20
+  __TEXT_EXEC.__text: 0x26f08
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x2e0
-  __DATA.__bss: 0x27c
+  __DATA.__bss: 0x284
   __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__mod_init_func: 0x80
+  __DATA_CONST.__mod_init_func: 0x88
   __DATA_CONST.__mod_term_func: 0x80
   __DATA_CONST.__const: 0x6e88
   __DATA_CONST.__kalloc_type: 0x1000
   __DATA_CONST.__kalloc_var: 0xa0
   Symbols:   0
-  Functions: 848
+  Functions: 849
 

```

>  `com.apple.driver.AppleT8130CLPC`

```diff

-1173.0.0.0.1
-  __TEXT.__cstring: 0x2baf
-  __TEXT.__const: 0xb5c
-  __TEXT_EXEC.__text: 0x4a758
+1175.0.17.0.0
+  __TEXT.__cstring: 0x2c2f
+  __TEXT.__const: 0xb34
+  __TEXT_EXEC.__text: 0x4c260
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x9cd0
-  __DATA.__common: 0x7a91
-  __DATA.__bss: 0x268
+  __DATA.__data: 0xa2b8
+  __DATA.__common: 0x7b19
+  __DATA.__bss: 0x278
   __DATA_CONST.__auth_got: 0x4a0
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__mod_init_func: 0x110
+  __DATA_CONST.__mod_init_func: 0x118
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x4da0
+  __DATA_CONST.__const: 0x4fb0
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
   Symbols:   0
-  Functions: 1226
+  Functions: 1262
 

```

>  `com.apple.driver.usb.cdc.ncm`

```diff

-352.0.0.0.0
+353.0.0.0.0
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xc5d
-  __TEXT_EXEC.__text: 0x86dc
+  __TEXT.__cstring: 0xc2c
+  __TEXT_EXEC.__text: 0x8620
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10

```

>  `com.apple.driver.AppleMobileDispH16P-DCP`

```diff

-395.12.2.0.0
-  __TEXT.__cstring: 0x5358
+395.20.1.0.0
+  __TEXT.__cstring: 0x5565
   __TEXT.__const: 0x1a78
-  __TEXT_EXEC.__text: 0x1ffd8
+  __TEXT_EXEC.__text: 0x20644
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2b0
+  __DATA.__data: 0x2b8
   __DATA.__common: 0xf0
   __DATA.__bss: 0x170
   __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x3dd8
-  __DATA_CONST.__kalloc_type: 0x580
+  __DATA_CONST.__const: 0x3e18
+  __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 1092
+  Functions: 1105
 

```

>  `com.apple.AGXG16P`

```diff

-320.13.8.0.0
-  __TEXT.__const: 0x443c
-  __TEXT.__cstring: 0xcadf
+320.18.0.0.0
+  __TEXT.__const: 0x4444
+  __TEXT.__cstring: 0xca1b
   __TEXT.__os_log: 0x2f7
-  __TEXT_EXEC.__text: 0xae2ec
+  __TEXT_EXEC.__text: 0xae40c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13b8
   __DATA.__common: 0x10

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x320
   __DATA_CONST.__mod_term_func: 0x280
-  __DATA_CONST.__const: 0x10b78
+  __DATA_CONST.__const: 0x10bb0
   __DATA_CONST.__kalloc_type: 0x2140
   __DATA_CONST.__kalloc_var: 0x3160
   Symbols:   0
-  Functions: 3067
+  Functions: 3069
 

```

>  `com.apple.kext.CoreTrust`

```diff

 148.0.0.0.0
   __TEXT.__const: 0xfe8
-  __TEXT.__cstring: 0x52
-  __TEXT_EXEC.__text: 0x8660
+  __TEXT_EXEC.__text: 0x8620
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x10
-  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14e0

```

>  `com.apple.driver.AppleUSBXDCI`

```diff

-816.0.0.0.0
+818.0.0.0.0
   __TEXT.__cstring: 0x5780
   __TEXT.__os_log: 0x27fd
   __TEXT.__const: 0x28
-  __TEXT_EXEC.__text: 0x210d0
+  __TEXT_EXEC.__text: 0x210dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100

```

>  `com.apple.driver.AppleALSColorSensor`

```diff

-1835.0.2.0.1
+1835.0.23.0.0
   __TEXT.__const: 0x104
-  __TEXT.__cstring: 0x3653
+  __TEXT.__cstring: 0x36b6
   __TEXT.__os_log: 0x96
-  __TEXT_EXEC.__text: 0x15634
+  __TEXT_EXEC.__text: 0x15648
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x1f8

```

>  `com.apple.iokit.IOGPUFamily`

```diff

-104.0.4.0.0
-  __TEXT.__cstring: 0x502a
+104.0.5.0.0
+  __TEXT.__cstring: 0x4faf
   __TEXT.__os_log: 0x387c
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x37ce4
+  __TEXT_EXEC.__text: 0x379c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4b0
   __DATA.__common: 0x780

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

-6760.0.0.0.0
-  __TEXT.__cstring: 0x3240d
-  __TEXT.__os_log: 0x2d8f5
+6767.0.0.0.0
+  __TEXT.__cstring: 0x32b44
+  __TEXT.__os_log: 0x2db0c
   __TEXT.__const: 0x7f0
-  __TEXT_EXEC.__text: 0x18b590
+  __TEXT_EXEC.__text: 0x18d158
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
   __DATA.__common: 0x1238

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x3a0
   __DATA_CONST.__mod_term_func: 0x3a0
-  __DATA_CONST.__const: 0x1d920
+  __DATA_CONST.__const: 0x1d988
   __DATA_CONST.__kalloc_type: 0x1d40
   __DATA_CONST.__kalloc_var: 0xaf0
   Symbols:   0
-  Functions: 4753
+  Functions: 4756
 

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-768.0.0.0.0
-  __TEXT.__const: 0x6b8
-  __TEXT.__cstring: 0xf7bd
-  __TEXT_EXEC.__text: 0x58bec
+769.0.1.0.0
+  __TEXT.__const: 0x6f8
+  __TEXT.__cstring: 0xf7d5
+  __TEXT_EXEC.__text: 0x59824
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4e4
   __DATA.__common: 0x528
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__auth_got: 0x670
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100

   __DATA_CONST.__kalloc_type: 0x7c0
   __DATA_CONST.__kalloc_var: 0x550
   Symbols:   0
-  Functions: 1706
+  Functions: 1709
 

```

>  `com.apple.iokit.IOAVFamily`

```diff

-482.0.0.0.0
+483.0.0.0.0
   __TEXT.__cstring: 0xa8dc
   __TEXT.__os_log: 0x9ca0
   __TEXT.__const: 0xe7d4
-  __TEXT_EXEC.__text: 0x84e0c
+  __TEXT_EXEC.__text: 0x84ef0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x988

```

>  `com.apple.iokit.IOUSBMassStorageDriver`

```diff

 250.0.0.0.0
   __TEXT.__cstring: 0x2658
   __TEXT.__const: 0x268
-  __TEXT_EXEC.__text: 0x1f2dc
+  __TEXT_EXEC.__text: 0x1f500
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x120
   __DATA.__common: 0x190

```

>  `com.apple.driver.AppleOnboardSerial`

```diff

 201.0.0.0.0
-  __TEXT.__cstring: 0x192e
+  __TEXT.__cstring: 0x1906
   __TEXT.__const: 0x68
-  __TEXT_EXEC.__text: 0x11fc0
+  __TEXT_EXEC.__text: 0x120c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
   __DATA.__common: 0x2a8

   __DATA_CONST.__const: 0x3280
   __DATA_CONST.__kalloc_type: 0x380
   Symbols:   0
-  Functions: 460
+  Functions: 459
 

```

>  `com.apple.driver.AppleStockholmControl`

```diff

-350.23.1.0.0
-  __TEXT.__cstring: 0x4961
+350.26.1.0.0
+  __TEXT.__cstring: 0x45c8
   __TEXT.__const: 0x30
-  __TEXT_EXEC.__text: 0x15d30
+  __TEXT_EXEC.__text: 0x14bf8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x219
   __DATA.__common: 0x1a6

   __DATA_CONST.__const: 0x2260
   __DATA_CONST.__kalloc_type: 0x1c0
   Symbols:   0
-  Functions: 248
+  Functions: 249
 

```

>  `com.apple.iokit.IOAccessoryManager`

```diff

-1000.0.0.0.0
+1003.0.0.0.0
   __TEXT.__const: 0x2f8
-  __TEXT.__cstring: 0x1069c
-  __TEXT.__os_log: 0x10191
-  __TEXT_EXEC.__text: 0xe8540
+  __TEXT.__cstring: 0x10627
+  __TEXT.__os_log: 0x10365
+  __TEXT_EXEC.__text: 0xe8ba8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
   __DATA.__common: 0x15b8

   __DATA_CONST.__const: 0x28668
   __DATA_CONST.__kalloc_type: 0x2380
   Symbols:   0
-  Functions: 4351
+  Functions: 4352
 

```

>  `com.apple.driver.AppleFirmwareKit`

```diff

-529.0.0.0.0
-  __TEXT.__cstring: 0x2781
-  __TEXT.__os_log: 0x1098
-  __TEXT.__const: 0xc0
-  __TEXT_EXEC.__text: 0x36614
+531.0.4.0.0
+  __TEXT.__cstring: 0x27af
+  __TEXT.__os_log: 0x1129
+  __TEXT.__const: 0xa8
+  __TEXT_EXEC.__text: 0x36c24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3f8
   __DATA.__common: 0x700
   __DATA.__bss: 0xc8
-  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0xf0
   __DATA_CONST.__mod_term_func: 0xf0
   __DATA_CONST.__const: 0xd348
-  __DATA_CONST.__kalloc_type: 0x17c0
+  __DATA_CONST.__kalloc_type: 0x1880
   __DATA_CONST.__kalloc_var: 0x50
   Symbols:   0
-  Functions: 1624
+  Functions: 1625
 

```

>  `com.apple.driver.RTBuddy`

```diff

-617.0.0.0.0
-  __TEXT.__cstring: 0x93e8
+618.0.2.0.0
+  __TEXT.__cstring: 0x947e
   __TEXT.__const: 0x278
-  __TEXT_EXEC.__text: 0x3f8e0
+  __TEXT_EXEC.__text: 0x3f918
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
   __DATA.__common: 0xb20

   __DATA_CONST.__kalloc_type: 0x12c0
   __DATA_CONST.__kalloc_var: 0xf0
   Symbols:   0
-  Functions: 2208
+  Functions: 2210
 

```

>  `com.apple.driver.AppleSMCWirelessCharger`

```diff

-72.0.0.0.0
+76.0.0.0.0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x28c2
+  __TEXT.__cstring: 0x28d3
   __TEXT.__os_log: 0x4b9
-  __TEXT_EXEC.__text: 0xecb4
+  __TEXT_EXEC.__text: 0xecc8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68
-  __DATA.__bss: 0x64
+  __DATA.__bss: 0x68
   __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x8

```

>  `com.apple.driver.AppleSPU`

```diff

-1013.0.0.0.1
+1014.0.1.0.0
   __TEXT.__cstring: 0x5aae
   __TEXT.__os_log: 0x85b
   __TEXT.__const: 0x358
-  __TEXT_EXEC.__text: 0x49660
+  __TEXT_EXEC.__text: 0x49668
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7b8
   __DATA.__common: 0x970

```

>  `com.apple.nke.l2tp`

```diff

 1016.0.0.0.0
-  __TEXT.__cstring: 0xb0c
+  __TEXT.__cstring: 0xa63
   __TEXT.__const: 0x58
-  __TEXT_EXEC.__text: 0x4050
+  __TEXT_EXEC.__text: 0x3ed4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x130
   __DATA.__common: 0x150
   __DATA.__bss: 0x1058
-  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__kalloc_var: 0xa0

```

>  `com.apple.iokit.IOCryptoAcceleratorFamily`

```diff

 135.0.0.0.0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x52f
-  __TEXT_EXEC.__text: 0x3868
+  __TEXT_EXEC.__text: 0x38b8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x140
   __DATA.__common: 0xc0

```

>  `com.apple.iokit.IOHIDFamily`

```diff

-2094.0.0.0.0
+2102.0.0.0.0
   __TEXT.__cstring: 0x24b3
   __TEXT.__const: 0x6c8
   __TEXT.__os_log: 0x2a2f
-  __TEXT_EXEC.__text: 0x6288c
+  __TEXT_EXEC.__text: 0x629a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xbcc
   __DATA.__common: 0x748

```

</details>

### KDKs

- [KDK DIFF](KDK.md)

## MachO

### 🆕 NEW (22)

- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`
- `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`
- `/Applications/MomentsUIService.app/PlugIns/MomentsDiagnosticsExtensionFeedbackAssistant.appex/MomentsDiagnosticsExtensionFeedbackAssistant`
- `/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_archive_bin.metallib`
- `/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib`
- `/System/Library/ExtensionKit/Extensions/DictionarySettingsExtension.appex/DictionarySettingsExtension`
- `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`
- `/System/Library/ExtensionKit/Extensions/NotificationsSettingsExtension.appex/NotificationsSettingsExtension`
- `/System/Library/ExtensionKit/Extensions/PodcastsSettingsAppIntentsExtension.appex/PodcastsSettingsAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`
- `/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationMapLNPromptPlugin.appex/CoreLocationMapLNPromptPlugin`
- `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension`
- `/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PlugIns/PhotosStoryDiagnostics.appex/PhotosStoryDiagnostics`
- `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsInternalXPCServices.xpc/SiriSuggestionsInternalXPCServices`
- `/System/Library/VideoProcessors/CCPortrait.bundle/ccportrait_archive_bin.metallib`
- `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`
- `/private/var/staged_system_apps/Image Playground.app/Image Playground`
- `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`
- `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension`
- `/usr/lib/libLogRedirect.dylib`
- `/usr/lib/libffi-trampolines.dylib`
- `/usr/libexec/NRDUpdated`

### ❌ Removed (16)

- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009-iOS-D83-D84.appex/Diagnostic-4009-iOS-D83-D84`
- `/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84`
- `/Applications/MobileSMS.app/PlugIns/MobileSMSSpotlightImporter.appex/MobileSMSSpotlightImporter`
- `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor`
- `/System/Library/ExtensionKit/Extensions/IFResponseGenerationSELFIngestor.appex/IFResponseGenerationSELFIngestor`
- `/System/Library/ExtensionKit/Extensions/IFTranscriptSELFIngestor.appex/IFTranscriptSELFIngestor`
- `/System/Library/Frameworks/CoreImage.framework/portrait_filters_archive_bin.metallib`
- `/System/Library/Frameworks/CoreImage.framework/portrait_filters_fullsize_archive_bin.metallib`
- `/System/Library/Frameworks/NetworkExtension.framework/PlugIns/NEUserNotificationUIExtension.appex/NEUserNotificationUIExtension`
- `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/XPCServices/AMSUIPaymentViewService_macCatalyst.xpc/AMSUIPaymentViewService_macCatalyst`
- `/System/Library/PrivateFrameworks/ClassroomKit.framework/Extensions/EasyMAIDSignInPicker.appex/EasyMAIDSignInPicker`
- `/private/var/staged_system_apps/GenerativePlayground.app/Extensions/GPUIExtension.appex/GPUIExtension`
- `/private/var/staged_system_apps/GenerativePlayground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`
- `/private/var/staged_system_apps/GenerativePlayground.app/GenerativePlayground`
- `/private/var/staged_system_apps/GenerativePlayground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`
- `/private/var/staged_system_apps/MobileMail.app/Extensions/MailSettingsIntentsExtension.appex/MailSettingsIntentsExtension`

### ⬆️ Updated (1125)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService.md)
- [/Applications/AXUIViewService.app/AXUIViewService](MACHOS/AXUIViewService.md)
- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AirPlayReceiver.app/AirPlayReceiver](MACHOS/AirPlayReceiver.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppSSOUIService.app/AppSSOUIService](MACHOS/AppSSOUIService.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService](MACHOS/AppleIDSetupUIService.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI](MACHOS/AuthenticationServicesUI.md)
- [/Applications/AutoSettings.app/AutoSettings](MACHOS/AutoSettings.md)
- [/Applications/BarcodeScanner.app/PlugIns/BarcodeScannerWidgetExtension.appex/BarcodeScannerWidgetExtension](MACHOS/BarcodeScannerWidgetExtension.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CTKUIService.app/CTKUIService](MACHOS/CTKUIService.md)
- [/Applications/Camera.app/Camera](MACHOS/Camera.md)
- [/Applications/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera](MACHOS/LockScreenCamera.md)
- [/Applications/Camera.app/PlugIns/LauncherControlExtension.appex/LauncherControlExtension](MACHOS/LauncherControlExtension.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/CarPlayWallpaper.app/CarPlayWallpaper](MACHOS/CarPlayWallpaper.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/ClarityPhotos.app/ClarityPhotos](MACHOS/ClarityPhotos.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/ContactPhotoCarouselRemoteAlert.app/ContactPhotoCarouselRemoteAlert](MACHOS/ContactPhotoCarouselRemoteAlert.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsService.app/DiagnosticsService](MACHOS/DiagnosticsService.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4615.appex/Diagnostic-4615](MACHOS/Diagnostic-4615.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002](MACHOS/Diagnostic-6002.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6006.appex/Diagnostic-6006](MACHOS/Diagnostic-6006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201](MACHOS/Diagnostic-8201.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253](MACHOS/Diagnostic-8253.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264](MACHOS/Diagnostic-8264.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276](MACHOS/Diagnostic-8276.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288](MACHOS/Diagnostic-8288.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340](MACHOS/Diagnostic-8340.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389](MACHOS/Diagnostic-8389.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008](MACHOS/Diagnostic-9008.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/EyeReliefUI.app/EyeReliefUI](MACHOS/EyeReliefUI.md)
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
- [/Applications/HearingApp.app/HearingApp](MACHOS/HearingApp.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/LimitedAccessPromptView.app/LimitedAccessPromptView](MACHOS/LimitedAccessPromptView.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MediaRemoteUIService.app/MediaRemoteUIService](MACHOS/MediaRemoteUIService.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/SpotlightIndexExtension.appex/SpotlightIndexExtension](MACHOS/SpotlightIndexExtension.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MobileSMS.app/MobileSMS](MACHOS/MobileSMS.md)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension](MACHOS/com.apple.mobilesafari.SafariDiagnosticExtension.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMessagesApp.appex/PhotosMessagesApp](MACHOS/PhotosMessagesApp.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MomentsUIService.app/Frameworks/MomentsUIServiceCore.framework/MomentsUIServiceCore](MACHOS/MomentsUIServiceCore.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/MusicRecognition.app/PlugIns/MusicRecognitionControls.appex/MusicRecognitionControls](MACHOS/MusicRecognitionControls.md)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension](MACHOS/PeerPaymentMessagesExtension.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/PreBoard.app/PreBoard](MACHOS/PreBoard.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/Print Center.app/PlugIns/PrintLiveActivity.iOS.appex/PrintLiveActivity.iOS](MACHOS/PrintLiveActivity.iOS.md)
- [/Applications/Print Center.app/Print Center](MACHOS/Print_Center.md)
- [/Applications/ProximityReaderSceneUI.app/ProximityReaderSceneUI](MACHOS/ProximityReaderSceneUI.md)
- [/Applications/RecoverDeviceUI.app/RecoverDeviceUI](MACHOS/RecoverDeviceUI.md)
- [/Applications/ReplayKitAngel.app/ReplayKitAngel](MACHOS/ReplayKitAngel.md)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/ScreenContinuityShell.app/ScreenContinuityShell](MACHOS/ScreenContinuityShell.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityCamera.appex/ContinuityCamera](MACHOS/ContinuityCamera.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/StickerPickerService.app/StickerPickerService](MACHOS/StickerPickerService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVRemoteUIService.app/PlugIns/TVRemoteIntentExtension.appex/TVRemoteIntentExtension](MACHOS/TVRemoteIntentExtension.md)
- [/Applications/TVRemoteUIService.app/TVRemoteUIService](MACHOS/TVRemoteUIService.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Applications/iCloud.app/iCloud](MACHOS/iCloud.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/usr/lib/system/libdispatch_debug.dylib](MACHOS/libdispatch_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libdispatch_profile.dylib](MACHOS/libdispatch_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_blocks_debug.dylib](MACHOS/libsystem_blocks_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_blocks_profile.dylib](MACHOS/libsystem_blocks_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib](MACHOS/libsystem_trace_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXAssetAndDataServer.axuiservice/AXAssetAndDataServer](MACHOS/AXAssetAndDataServer.md)
- [/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer](MACHOS/AXHapticMusicServer.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/AXUltronPluginService.axuiservice/AXUltronPluginService](MACHOS/AXUltronPluginService.md)
- [/System/Library/AccessibilityBundles/AXWatchRemoteScreenUIServer.axuiservice/AXWatchRemoteScreenUIServer](MACHOS/AXWatchRemoteScreenUIServer.md)
- [/System/Library/AccessibilityBundles/AssistiveTouch.axuiservice/AssistiveTouch](MACHOS/AssistiveTouch.md)
- [/System/Library/AccessibilityBundles/FitnessApp.axbundle/FitnessApp](MACHOS/FitnessApp.md)
- [/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer](MACHOS/GAXBackboardServer.md)
- [/System/Library/AccessibilityBundles/GAXClient.bundle/GAXClient](MACHOS/GAXClient.md)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer.md)
- [/System/Library/AccessibilityBundles/GuidedAccess.axuiservice/GuidedAccess](MACHOS/GuidedAccess.md)
- [/System/Library/AccessibilityBundles/HoverTextUIServer.axuiservice/HoverTextUIServer](MACHOS/HoverTextUIServer.md)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion](MACHOS/NanoTimeKitCompanion.md)
- [/System/Library/AccessibilityBundles/ScreenSharingAccessibilityServer.axuiservice/ScreenSharingAccessibilityServer](MACHOS/ScreenSharingAccessibilityServer.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow.md)
- [/System/Library/Accounts/DataclassOwners/Calendar.bundle/Calendar](MACHOS/Calendar.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner](MACHOS/JournalDataclassOwner.md)
- [/System/Library/AppRemovalServices/com.apple.podcasts.appremoval.xpc/com.apple.podcasts.appremoval](MACHOS/com.apple.podcasts.appremoval.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/NotificationsFlowDelegatePlugin.bundle/NotificationsFlowDelegatePlugin](MACHOS/NotificationsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PaymentsFlowDelegatePlugin.bundle/PaymentsFlowDelegatePlugin](MACHOS/PaymentsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriSuggestionsFlowPlugin.bundle/SiriSuggestionsFlowPlugin](MACHOS/SiriSuggestionsFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SystemCommandsFlowDelegatePlugin.bundle/SystemCommandsFlowDelegatePlugin](MACHOS/SystemCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications](MACHOS/Applications.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge.md)
- [/System/Library/Assistant/UIPlugins/Mail.siriUIBundle/Mail](MACHOS/Mail.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/UIPlugins/RemindersSiriUIPlugin.siriUIBundle/RemindersSiriUIPlugin](MACHOS/RemindersSiriUIPlugin.md)
- [/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen](MACHOS/AVCHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/ContinuousExposeModule.bundle/ContinuousExposeModule](MACHOS/ContinuousExposeModule.md)
- [/System/Library/ControlCenter/Bundles/FocusUIModule.bundle/FocusUIModule](MACHOS/FocusUIModule.md)
- [/System/Library/ControlCenter/Bundles/NFCControlCenterModule.bundle/NFCControlCenterModule](MACHOS/NFCControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule](MACHOS/ReplayKitModule.md)
- [/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule](MACHOS/VideoConferenceControlCenterModule.md)
- [/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting](MACHOS/CIInpainting.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/PortraitFilters](MACHOS/PortraitFilters.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents](MACHOS/AccessibilityAppIntents.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/CarPlay.app/CarPlay](MACHOS/CarPlay.md)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices.bundle/MobileDevices](MACHOS/MobileDevices.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/OTACrashCopier](MACHOS/OTACrashCopier.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/scrod](MACHOS/scrod.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/appplaceholdersyncd](MACHOS/appplaceholdersyncd.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration](MACHOS/AccessibilityDataMigration.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/KeyboardMigrator.migrator/KeyboardMigrator](MACHOS/KeyboardMigrator.md)
- [/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator](MACHOS/MobileActivationMigrator.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DigitalSeparation/SharingSources/ActivityDigitalSeparation.bundle/ActivityDigitalSeparation](MACHOS/ActivityDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/MapsDigitalSeparation.bundle/MapsDigitalSeparation](MACHOS/MapsDigitalSeparation.md)
- [/System/Library/DistributedEvaluation/Plugins/QuickTypeDESPlugin.desPlugin/QuickTypeDESPlugin](MACHOS/QuickTypeDESPlugin.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.intents.user-interactive.preload.bundle/com.apple.donotdisturb.private.intents.user-interactive.preload](MACHOS/com.apple.donotdisturb.private.intents.user-interactive.preload.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.schedule.bundle/com.apple.donotdisturb.private.schedule](MACHOS/com.apple.donotdisturb.private.schedule.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.sleeping-trigger.bundle/com.apple.donotdisturb.private.sleeping-trigger](MACHOS/com.apple.donotdisturb.private.sleeping-trigger.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AirDropSettingsIntents.appex/AirDropSettingsIntents](MACHOS/AirDropSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension](MACHOS/CameraSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension](MACHOS/ComposeReviewExtension.md)
- [/System/Library/ExtensionKit/Extensions/ControlCenterControlsExtension.appex/ControlCenterControlsExtension](MACHOS/ControlCenterControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents](MACHOS/DeveloperSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/DisplayAndBrightnessSettingsExtension](MACHOS/DisplayAndBrightnessSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DoNotDisturbAppIntents.appex/DoNotDisturbAppIntents](MACHOS/DoNotDisturbAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/FontIntents.appex/FontIntents](MACHOS/FontIntents.md)
- [/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents](MACHOS/GeneralSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/HealthStandaloneIntents.appex/HealthStandaloneIntents](MACHOS/HealthStandaloneIntents.md)
- [/System/Library/ExtensionKit/Extensions/InferenceProviderService.appex/InferenceProviderService](MACHOS/InferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/InstalledAppsSettingsAppIntents.appex/InstalledAppsSettingsAppIntents](MACHOS/InstalledAppsSettingsAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/IntelligenceIntentsExtension.appex/IntelligenceIntentsExtension](MACHOS/IntelligenceIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/InternationalSettingsExtension.appex/InternationalSettingsExtension](MACHOS/InternationalSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/KeyboardSettingsExtension.appex/KeyboardSettingsExtension](MACHOS/KeyboardSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension](MACHOS/MADViewServiceExtension.md)
- [/System/Library/ExtensionKit/Extensions/MailSettingsIntentsExtension.appex/MailSettingsIntentsExtension](MACHOS/MailSettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MapsTransactionInsightsExtension.appex/MapsTransactionInsightsExtension](MACHOS/MapsTransactionInsightsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MeasureSettingsAppIntentsExtension.appex/MeasureSettingsAppIntentsExtension](MACHOS/MeasureSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MessagesSettingsWidgetKitExtension.appex/MessagesSettingsWidgetKitExtension](MACHOS/MessagesSettingsWidgetKitExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK](MACHOS/PFLHRPeriodPredCK.md)
- [/System/Library/ExtensionKit/Extensions/PersonalHotspotControlExtension.appex/PersonalHotspotControlExtension](MACHOS/PersonalHotspotControlExtension.md)
- [/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin](MACHOS/PhotosPFLPlugin.md)
- [/System/Library/ExtensionKit/Extensions/PhotosSearchClientLighthouse.appex/PhotosSearchClientLighthouse](MACHOS/PhotosSearchClientLighthouse.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivacyAppIntents.appex/PrivacyAppIntents](MACHOS/PrivacyAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService](MACHOS/PrivateMLClientInferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/QuickLookUIExtension.appex/QuickLookUIExtension](MACHOS/QuickLookUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension](MACHOS/SearchToolExtension.md)
- [/System/Library/ExtensionKit/Extensions/SettingsCellularAppIntentsExtension.appex/SettingsCellularAppIntentsExtension](MACHOS/SettingsCellularAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/SiriMASPFLCK](MACHOS/SiriMASPFLCK.md)
- [/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin](MACHOS/SiriSuggestionsLightHousePlugin.md)
- [/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsIntents.appex/SoftwareUpdateSettingsIntents](MACHOS/SoftwareUpdateSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/SummarizationTool.appex/SummarizationTool](MACHOS/SummarizationTool.md)
- [/System/Library/ExtensionKit/Extensions/ToggleAirplaneModeExtension.appex/ToggleAirplaneModeExtension](MACHOS/ToggleAirplaneModeExtension.md)
- [/System/Library/ExtensionKit/Extensions/ToggleCellularDataModeExtension.appex/ToggleCellularDataModeExtension](MACHOS/ToggleCellularDataModeExtension.md)
- [/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension](MACHOS/TranslationAPISupportExtension.md)
- [/System/Library/ExtensionKit/Extensions/VPNAppIntentWidgetExtension.appex/VPNAppIntentWidgetExtension](MACHOS/VPNAppIntentWidgetExtension.md)
- [/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/WebThumbnailExtension](MACHOS/WebThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension](MACHOS/WiFiSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/WirelessModemSettingsControlsExtension.appex/WirelessModemSettingsControlsExtension](MACHOS/WirelessModemSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension](MACHOS/ZeoliteExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Extensions/ASIOKit.kext/ASIOKit](MACHOS/ASIOKit.md)
- [/System/Library/Extensions/lifs.kext/lifs](MACHOS/lifs.md)
- [/System/Library/Filesystems/apfs.fs/apfs_boot_util](MACHOS/apfs_boot_util.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_iosd](MACHOS/apfs_iosd.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/slurpAPFSMeta](MACHOS/slurpAPFSMeta.md)
- [/System/Library/Filesystems/apfs.fs/sm_stats](MACHOS/sm_stats.md)
- [/System/Library/Filesystems/apfs_userfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs_userfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/hfs.fs/CopyHFSMeta](MACHOS/CopyHFSMeta.md)
- [/System/Library/Filesystems/hfs.fs/hfs.util](MACHOS/hfs.util.md)
- [/System/Library/Filesystems/hfs.fs/mount_hfs](MACHOS/mount_hfs.md)
- [/System/Library/Filesystems/hfs.fs/newfs_hfs](MACHOS/newfs_hfs.md)
- [/System/Library/Filesystems/msdos.fs/fsck_msdos](MACHOS/fsck_msdos.md)
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
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService](MACHOS/ContactsButtonXPCService.md)
- [/System/Library/Frameworks/CoreImage.framework/photo_style_archive_bin.metallib](MACHOS/photo_style_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin](MACHOS/CoreLocationNumberedMapCalloutPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice](MACHOS/eedmediaservice.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension1_iOS.appex/CoreSpotlightImportExtension1_iOS](MACHOS/CoreSpotlightImportExtension1_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension2_iOS.appex/CoreSpotlightImportExtension2_iOS](MACHOS/CoreSpotlightImportExtension2_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter](MACHOS/CommCenter.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/ctkd](MACHOS/ctkd.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd](MACHOS/fileproviderd.md)
- [/System/Library/Frameworks/FinanceKit.framework/financed](MACHOS/financed.md)
- [/System/Library/Frameworks/GSS.framework/Helpers/GSSCred](MACHOS/GSSCred.md)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension](MACHOS/HomeKitDiagnosticExtension.md)
- [/System/Library/Frameworks/IdentityLookup.framework/XPCServices/com.apple.IdentityLookup.MessageFilter.xpc/com.apple.IdentityLookup.MessageFilter](MACHOS/com.apple.IdentityLookup.MessageFilter.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc](MACHOS/mscamerad-xpc.md)
- [/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService](MACHOS/ImageIOXPCService.md)
- [/System/Library/Frameworks/ImageIO.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl](MACHOS/MechPearl.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd](MACHOS/applicensedeliveryd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/QuickLook.framework/PlugIns/com.apple.quicklook.extension.previewUI.appex/com.apple.quicklook.extension.previewUI](MACHOS/com.apple.quicklook.extension.previewUI.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent](MACHOS/com.apple.quicklook.ThumbnailsAgent.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitDataExport.xpc/SensorKitDataExport](MACHOS/SensorKitDataExport.md)
- [/System/Library/Frameworks/ShazamKit.framework/PlugIns/ShazamNotificationContentExtension.appex/ShazamNotificationContentExtension](MACHOS/ShazamNotificationContentExtension.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/Translation.framework/translationd](MACHOS/translationd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter](MACHOS/AppleProxServiceFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/FTRemoteEventHIDSessionFilter.plugin/FTRemoteEventHIDSessionFilter](MACHOS/FTRemoteEventHIDSessionFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics](MACHOS/IOAnalytics.md)
- [/System/Library/Health/DiagnosticExtensionPlugins/HealthMedicationsDiagnosticExtensionPlugin.bundle/HealthMedicationsDiagnosticExtensionPlugin](MACHOS/HealthMedicationsDiagnosticExtensionPlugin.md)
- [/System/Library/Health/Plugins/HealthActivityCache.bundle/HealthActivityCache](MACHOS/HealthActivityCache.md)
- [/System/Library/Health/Plugins/HealthBluetoothPeripheral.bundle/HealthBluetoothPeripheral](MACHOS/HealthBluetoothPeripheral.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/SMS](MACHOS/SMS.md)
- [/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS](MACHOS/SatelliteSMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/PlugIns/iMessageLite.imservice/iMessageLite](MACHOS/iMessageLite.md)
- [/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/FindMyMessagesApp](MACHOS/FindMyMessagesApp.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin](MACHOS/MSMessageExtensionBalloonPlugin.md)
- [/System/Library/Messages/iMessageBalloons/SendLaterProvider.bundle/SendLaterProvider](MACHOS/SendLaterProvider.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeRemoteAccounts.bundle/BridgeRemoteAccounts](MACHOS/BridgeRemoteAccounts.md)
- [/System/Library/NanoPreferenceBundles/Applications/DepthCompanionSettings.bundle/DepthCompanionSettings](MACHOS/DepthCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/HeartRateSettings.bundle/HeartRateSettings](MACHOS/HeartRateSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoBedtimeBridgeSettings.bundle/NanoBedtimeBridgeSettings](MACHOS/NanoBedtimeBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMapsBridgeSettings.bundle/NanoMapsBridgeSettings](MACHOS/NanoMapsBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/PodcastsBridgeSettings.bundle/PodcastsBridgeSettings](MACHOS/PodcastsBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/SessionTrackerAppSettings.bundle/SessionTrackerAppSettings](MACHOS/SessionTrackerAppSettings.md)
- [/System/Library/NanoPreferenceBundles/Customization/NTKCustomization.bundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings](MACHOS/CSLCompanionLiveActivitiesSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoPreferenceBundles/PrivacySettings/HealthBridgePrivacySettings.bundle/HealthBridgePrivacySettings](MACHOS/HealthBridgePrivacySettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/BPSStingSetup.bundle/BPSStingSetup](MACHOS/BPSStingSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthBridgeSetupPlugin.bundle/HealthBridgeSetupPlugin](MACHOS/HealthBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/TextSettingsBridgeSetup.bundle/TextSettingsBridgeSetup](MACHOS/TextSettingsBridgeSetup.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCalendarComplicationsCompanion.bundle/NanoCalendarComplicationsCompanion](MACHOS/NanoCalendarComplicationsCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoMapsComplications.bundle/NanoMapsComplications](MACHOS/NanoMapsComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKActivityFaceBundleCompanion.bundle/NTKActivityFaceBundleCompanion](MACHOS/NTKActivityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAlaskanFaceBundleCompanion.bundle/NTKAlaskanFaceBundleCompanion](MACHOS/NTKAlaskanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBigNumeralsAnalogFaceBundleCompanion.bundle/NTKBigNumeralsAnalogFaceBundleCompanion](MACHOS/NTKBigNumeralsAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCaliforniaFaceBundleCompanion.bundle/NTKCaliforniaFaceBundleCompanion](MACHOS/NTKCaliforniaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCollieFaceBundleCompanion.bundle/NTKCollieFaceBundleCompanion](MACHOS/NTKCollieFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCrosswindFaceBundleCompanion.bundle/NTKCrosswindFaceBundleCompanion](MACHOS/NTKCrosswindFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExtraLargeFaceBundleCompanion.bundle/NTKExtraLargeFaceBundleCompanion](MACHOS/NTKExtraLargeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGladiusFaceBundleCompanion.bundle/NTKGladiusFaceBundleCompanion](MACHOS/NTKGladiusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGlobetrotterFaceBundleCompanion.bundle/NTKGlobetrotterFaceBundleCompanion](MACHOS/NTKGlobetrotterFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGreyhoundFaceBundleCompanion.bundle/NTKGreyhoundFaceBundleCompanion](MACHOS/NTKGreyhoundFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMargaritaFaceBundleCompanion.bundle/NTKMargaritaFaceBundleCompanion](MACHOS/NTKMargaritaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPlumeriaFaceBundleCompanion.bundle/NTKPlumeriaFaceBundleCompanion](MACHOS/NTKPlumeriaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPrideWeaveFaceBundleCompanion.bundle/NTKPrideWeaveFaceBundleCompanion](MACHOS/NTKPrideWeaveFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSolarsFaceBundleCompanion.bundle/NTKSolarsFaceBundleCompanion](MACHOS/NTKSolarsFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUltraCubeFaceBundleCompanion.bundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUtilityFaceBundleCompanion.bundle/NTKUtilityFaceBundleCompanion](MACHOS/NTKUtilityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVictoryAnalogFaceBundleCompanion.bundle/NTKVictoryAnalogFaceBundleCompanion](MACHOS/NTKVictoryAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/MailAccountSettings.bundle/MailAccountSettings](MACHOS/MailAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AccountSettingsUI.bundle/AccountSettingsUI](MACHOS/AccountSettingsUI.md)
- [/System/Library/PreferenceBundles/ActionButtonSettings.bundle/ActionButtonSettings](MACHOS/ActionButtonSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings](MACHOS/AirPlayAndHandoffSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/CallDirectorySettings.bundle/CallDirectorySettings](MACHOS/CallDirectorySettings.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIMusicSettings.bundle/ClarityUIMusicSettings](MACHOS/ClarityUIMusicSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIPhotosSettings.bundle/ClarityUIPhotosSettings](MACHOS/ClarityUIPhotosSettings.md)
- [/System/Library/PreferenceBundles/DeveloperSettings.bundle/DeveloperSettings](MACHOS/DeveloperSettings.md)
- [/System/Library/PreferenceBundles/DictionarySettings.bundle/DictionarySettings](MACHOS/DictionarySettings.md)
- [/System/Library/PreferenceBundles/DigitalSeparationSettings.bundle/DigitalSeparationSettings](MACHOS/DigitalSeparationSettings.md)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings.md)
- [/System/Library/PreferenceBundles/FontSettings.bundle/FontSettings](MACHOS/FontSettings.md)
- [/System/Library/PreferenceBundles/FreeformSettings.bundle/FreeformSettings](MACHOS/FreeformSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/HealthSettings.bundle/HealthSettings](MACHOS/HealthSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MobileCalSettings.bundle/MobileCalSettings](MACHOS/MobileCalSettings.md)
- [/System/Library/PreferenceBundles/MobileMailSettings.bundle/MobileMailSettings](MACHOS/MobileMailSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MobileSlideShowSettings.bundle/MobileSlideShowSettings](MACHOS/MobileSlideShowSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/NewsSettings.bundle/NewsSettings](MACHOS/NewsSettings.md)
- [/System/Library/PreferenceBundles/NotesSettings.bundle/NotesSettings](MACHOS/NotesSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PassbookSettings.bundle/PassbookSettings](MACHOS/PassbookSettings.md)
- [/System/Library/PreferenceBundles/PasswordsSettings.bundle/PasswordsSettings](MACHOS/PasswordsSettings.md)
- [/System/Library/PreferenceBundles/PictureInPictureSettings.bundle/PictureInPictureSettings](MACHOS/PictureInPictureSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/PrimaryCloudCallingSettingsBundle.bundle/PrimaryCloudCallingSettingsBundle](MACHOS/PrimaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/Privacy/HealthPrivacySettings.bundle/HealthPrivacySettings](MACHOS/HealthPrivacySettings.md)
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings.md)
- [/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings](MACHOS/SOSSettings.md)
- [/System/Library/PreferenceBundles/SiriMessagesSettings.bundle/SiriMessagesSettings](MACHOS/SiriMessagesSettings.md)
- [/System/Library/PreferenceBundles/StocksSettings.bundle/StocksSettings](MACHOS/StocksSettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/TVSettings.bundle/TVSettings](MACHOS/TVSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountDeveloperSettings.bundle/VideoSubscriberAccountDeveloperSettings](MACHOS/VideoSubscriberAccountDeveloperSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountSettings.bundle/VideoSubscriberAccountSettings](MACHOS/VideoSubscriberAccountSettings.md)
- [/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings](MACHOS/VoiceControlSettings.md)
- [/System/Library/PreferenceBundles/VoiceMemosSettings.bundle/VoiceMemosSettings](MACHOS/VoiceMemosSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceBundles/WeatherSettings.bundle/WeatherSettings](MACHOS/WeatherSettings.md)
- [/System/Library/PreferenceBundles/iBooksSettings.bundle/iBooksSettings](MACHOS/iBooksSettings.md)
- [/System/Library/PreferencesSyncBundles/DoNotDisturbSettingsSync.bundle/DoNotDisturbSettingsSync](MACHOS/DoNotDisturbSettingsSync.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd](MACHOS/axassetsd.md)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/Support/axremoted](MACHOS/axremoted.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd](MACHOS/motiontrackingd.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/AXTeachableMomentsNotificationsExtension.appex/AXTeachableMomentsNotificationsExtension](MACHOS/AXTeachableMomentsNotificationsExtension.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/activityawardsd](MACHOS/activityawardsd.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd](MACHOS/activitysharingd.md)
- [/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/XPCServices/AirPlaySenderService.xpc/AirPlaySenderService](MACHOS/AirPlaySenderService.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon](MACHOS/AppleCredentialManagerDaemon.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService](MACHOS/AppleDeviceQueryService.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementViewExtension.appex/AMSEngagementViewExtension](MACHOS/AMSEngagementViewExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService](MACHOS/ANECompilerService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer](MACHOS/ANEStorageMaintainer.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail](MACHOS/ASVAssetThumbnail.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/Support/avatarsd](MACHOS/avatarsd.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/com.apple.BarcodeSupport.BarcodeNotificationService](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationService.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed](MACHOS/biomed.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd](MACHOS/bookassetd.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/PlugIns/LazuliDiagnosticExtension.appex/LazuliDiagnosticExtension](MACHOS/LazuliDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/Support/calaccessd](MACHOS/calaccessd.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/PlugIns/IntentsExtension.appex/IntentsExtension](MACHOS/IntentsExtension.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/Support/nebulad](MACHOS/nebulad.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/clipserviced](MACHOS/clipserviced.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider](MACHOS/com.apple.CloudDocs.iCloudDriveFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged](MACHOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/bird](MACHOS/bird.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd](MACHOS/com.apple.sbd.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent](MACHOS/contactsdonationagent.md)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd](MACHOS/assistant_cdmd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService](MACHOS/ACCHWComponentAuthService.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd](MACHOS/cdpd.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored](MACHOS/contextstored.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech](MACHOS/com.apple.siri.embeddedspeech.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/followupd](MACHOS/followupd.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/PlugIns/SearchPoirotExtension.appex/SearchPoirotExtension](MACHOS/SearchPoirotExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd](MACHOS/speechmodeltrainingd.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool](MACHOS/suggest_tool.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/reversetemplated](MACHOS/reversetemplated.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd](MACHOS/suggestd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub](MACHOS/DTServiceHub.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent](MACHOS/LeakAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/RemoteInjectionAgent](MACHOS/RemoteInjectionAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Support/dataaccessd](MACHOS/dataaccessd.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.datamigrator.xpc/com.apple.datamigrator](MACHOS/com.apple.datamigrator.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothHeadset.appex/BluetoothHeadset](MACHOS/BluetoothHeadset.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.tailspin.appex/com.apple.DiagnosticExtensions.tailspin](MACHOS/com.apple.DiagnosticExtensions.tailspin.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/XPCServices/DiagnosticsSessionAvailabilityService.xpc/DiagnosticsSessionAvailabilityService](MACHOS/DiagnosticsSessionAvailabilityService.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService](MACHOS/FilesystemMetadataSnapshotService.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd](MACHOS/donotdisturbd.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/DragUI.framework/Support/druid](MACHOS/druid.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/Support/devicedataresetd](MACHOS/devicedataresetd.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Support/exchangesyncd](MACHOS/exchangesyncd.md)
- [/System/Library/PrivateFrameworks/Eyedropper.framework/Support/eyedropperd](MACHOS/eyedropperd.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored](MACHOS/facetimemessagestored.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/FPCKService](MACHOS/FPCKService.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/XPCServices/FinHealthXPCServices.xpc/FinHealthXPCServices](MACHOS/FinHealthXPCServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/fitnesscoachingd](MACHOS/fitnesscoachingd.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Support/fontservicesd](MACHOS/fontservicesd.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterAuthenticateExtension.appex/GameCenterAuthenticateExtension](MACHOS/GameCenterAuthenticateExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond](MACHOS/revisiond.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd](MACHOS/generativeexperiencesd.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd](MACHOS/geoanalyticsd.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/MapsOfflineService.bundle/MapsOfflineService](MACHOS/MapsOfflineService.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/geod](MACHOS/geod.md)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/XPCServices/HRTFEnrollmentService.xpc/HRTFEnrollmentService](MACHOS/HRTFEnrollmentService.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/PlugIns/HealthMedicationsNotificationContentExtension.appex/HealthMedicationsNotificationContentExtension](MACHOS/HealthMedicationsNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd](MACHOS/homeenergyd.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iapd](MACHOS/iapd.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iaptransportd](MACHOS/iaptransportd.md)
- [/System/Library/PrivateFrameworks/IAPAuthentication.framework/Support/iapauthd](MACHOS/iapauthd.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd](MACHOS/intelligencecontextd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd](MACHOS/intelligenceflowd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/ERMLRuntimePlugin.appex/ERMLRuntimePlugin](MACHOS/ERMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension](MACHOS/ManagedSettingsExtension.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd](MACHOS/destinationd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/geocorrectiond](MACHOS/geocorrectiond.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd](MACHOS/mapspushd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/nanomapscd](MACHOS/nanomapscd.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService](MACHOS/MediaAnalysisBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService](MACHOS/com.apple.photos.ImageConversionService.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/Support/mediaartworkd](MACHOS/mediaartworkd.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd](MACHOS/mstreamd.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleEmbeddedAccessoryUpdaterService.xpc/AppleEmbeddedAccessoryUpdaterService](MACHOS/AppleEmbeddedAccessoryUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU](MACHOS/UARPUpdaterServiceDFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated](MACHOS/softwareupdated.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd](MACHOS/mobiletimerd.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd](MACHOS/medialibraryd.md)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/nanobackupd](MACHOS/nanobackupd.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/companionfindlocallyd](MACHOS/companionfindlocallyd.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent](MACHOS/NPKCompanionAgent.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/NTKDiagnosticExtensionCompanion.appex/NTKDiagnosticExtensionCompanion](MACHOS/NTKDiagnosticExtensionCompanion.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/com.apple.NanoTimeKit.CreateWatchFace.appex/com.apple.NanoTimeKit.CreateWatchFace](MACHOS/com.apple.NanoTimeKit.CreateWatchFace.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond](MACHOS/nanotimekitcompaniond.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/PlugIns/NewsArticleViewer.appex/NewsArticleViewer](MACHOS/NewsArticleViewer.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/nanonewscd](MACHOS/nanonewscd.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PlugIns/PeopleSuggesterLighthousePlugin.appex/PeopleSuggesterLighthousePlugin](MACHOS/PeopleSuggesterLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/XPCServices/PerfPowerTelemetryReaderService.xpc/PerfPowerTelemetryReaderService](MACHOS/PerfPowerTelemetryReaderService.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd](MACHOS/photoanalysisd.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider.md)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/Support/pointeruid](MACHOS/pointeruid.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/com.apple.PowerlogCore.diagnosticextension.appex/com.apple.PowerlogCore.diagnosticextension](MACHOS/com.apple.PowerlogCore.diagnosticextension.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PPSFeatureFlagReader.xpc/PPSFeatureFlagReader](MACHOS/PPSFeatureFlagReader.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader](MACHOS/PerfPowerServicesSignpostReader.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool](MACHOS/com.apple.PrintKit.PrinterTool.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd](MACHOS/privacyaccountingd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Reconstruction_Gpu_Archive.metallib](MACHOS/Reconstruction_Gpu_Archive.metallib.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent](MACHOS/RemoteManagementAgent.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd](MACHOS/remotemanagementd.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/rmdinspect](MACHOS/rmdinspect.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/Support/replicatord](MACHOS/replicatord.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd](MACHOS/smbclientd.md)
- [/System/Library/PrivateFrameworks/SOS.framework/sosd](MACHOS/sosd.md)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/Support/schooltimed](MACHOS/schooltimed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/PlugIns/ScreenTimeDeviceActivityMonitorExtension.appex/ScreenTimeDeviceActivityMonitorExtension](MACHOS/ScreenTimeDeviceActivityMonitorExtension.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd](MACHOS/liveactivitiesd.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/budd](MACHOS/budd.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/diagnosticextension.appex/diagnosticextension](MACHOS/diagnosticextension.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored](MACHOS/fitcored.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcoresessiond](MACHOS/fitcoresessiond.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced](MACHOS/siriinferenced.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTraining](MACHOS/SiriTTSTraining.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent](MACHOS/SiriTTSTrainingAgent.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/PlugIns/SleepNotificationContentExtension.appex/SleepNotificationContentExtension](MACHOS/SleepNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/Support/subridged](MACHOS/subridged.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd](MACHOS/softwareupdateservicesd.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/PlugIns/SoundScapesViewServices.appex/SoundScapesViewServices](MACHOS/SoundScapesViewServices.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpatialAudioServices.framework/XPCServices/SpatialAudioXPCService.xpc/SpatialAudioXPCService](MACHOS/SpatialAudioXPCService.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent](MACHOS/StatusKitAgent.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/Support/storebookkeeperd](MACHOS/storebookkeeperd.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Support/contentlinkingd](MACHOS/contentlinkingd.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd](MACHOS/syncdefaultsd.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd](MACHOS/systemstatusd.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/PlugIns/SWTFollowUpExtension.appex/SWTFollowUpExtension](MACHOS/SWTFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService](MACHOS/UVFSService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd](MACHOS/usernotificationsd.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/Plugins.bundle/Plugins](MACHOS/Plugins.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/voiced](MACHOS/voiced.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd](MACHOS/siriactionsd.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd](MACHOS/watchlistd.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd](MACHOS/webprivacyd.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService](MACHOS/ZhuGeService.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/ContainerMetadataExtractor](MACHOS/ContainerMetadataExtractor.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd](MACHOS/icloudsubscriptionoptimizerd.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/XPCServices/com.apple.DiagnosticsSessionAvailibility.xpc/com.apple.DiagnosticsSessionAvailibility](MACHOS/com.apple.DiagnosticsSessionAvailibility.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd](MACHOS/iosdiagnosticsd.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMenstrualCyclesRelevanceEngineDataSource.bundle/NanoMenstrualCyclesRelevanceEngineDataSource](MACHOS/NanoMenstrualCyclesRelevanceEngineDataSource.md)
- [/System/Library/ScreenReader/BrailleDrivers/DOT Driver.brailledriver/DOT Driver](MACHOS/DOT_Driver.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AppLaunchSuggestionsPlugin.bundle/AppLaunchSuggestionsPlugin](MACHOS/AppLaunchSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/CalendarSuggestions.bundle/CalendarSuggestions](MACHOS/CalendarSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriMessagesSuggestions.bundle/SiriMessagesSuggestions](MACHOS/SiriMessagesSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSocialConversationSuggestionsPlugin.bundle/SiriSocialConversationSuggestionsPlugin](MACHOS/SiriSocialConversationSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SystemCommandsSuggestionsPlugin.bundle/SystemCommandsSuggestionsPlugin](MACHOS/SystemCommandsSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/AudioUIPlugin](MACHOS/AudioUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ContactsFlowUIPlugin.bundle/ContactsFlowUIPlugin](MACHOS/ContactsFlowUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SettingsCustomPlugin.bundle/SettingsCustomPlugin](MACHOS/SettingsCustomPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriInferenceFlowsUIPlugin.bundle/SiriInferenceFlowsUIPlugin](MACHOS/SiriInferenceFlowsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriLinkUIPlugin.bundle/SiriLinkUIPlugin](MACHOS/SiriLinkUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriPaymentsUIPlugin.bundle/SiriPaymentsUIPlugin](MACHOS/SiriPaymentsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSocialConversationUIPlugin.bundle/SiriSocialConversationUIPlugin](MACHOS/SiriSocialConversationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriTranslationUIPlugin.bundle/SiriTranslationUIPlugin](MACHOS/SiriTranslationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriVideoUIPlugin.bundle/SiriVideoUIPlugin](MACHOS/SiriVideoUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/Snippets/UIPlugins/TimerUIPlugin.bundle/TimerUIPlugin](MACHOS/TimerUIPlugin.md)
- [/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin](MACHOS/StoreDemoPlugin.md)
- [/System/Library/SyncBundles/AirFair2.syncBundle/AirFair2](MACHOS/AirFair2.md)
- [/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary](MACHOS/MusicLibrary.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin](MACHOS/com.apple.tailspin.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1](MACHOS/ColourConstancyV1.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKAudiobooks.framework/BKAudiobooks](MACHOS/BKAudiobooks.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary](MACHOS/BKLibrary.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/EngagementCollector.framework/EngagementCollector](MACHOS/EngagementCollector.md)
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
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsItems.appex/FindMyWidgetIntentsItems](MACHOS/FindMyWidgetIntentsItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsPeople.appex/FindMyWidgetIntentsPeople](MACHOS/FindMyWidgetIntentsPeople.md)
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
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen](MACHOS/HomeWidgetLockScreen.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Magnifier.app/Extensions/MagnifierExtension.appex/MagnifierExtension](MACHOS/MagnifierExtension.md)
- [/private/var/staged_system_apps/Magnifier.app/Magnifier](MACHOS/Magnifier.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension](MACHOS/CalendarWidgetExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/Extensions/MailShortcutsExtension.appex/MailShortcutsExtension](MACHOS/MailShortcutsExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.IntentsExtension.appex/com.apple.mobilenotes.IntentsExtension](MACHOS/com.apple.mobilenotes.IntentsExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
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
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Passwords.app/Passwords](MACHOS/Passwords.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/CacheDeleteExtension.appex/CacheDeleteExtension](MACHOS/CacheDeleteExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsQuicklook.appex/TipsQuicklook](MACHOS/TipsQuicklook.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsWidget.appex/TipsWidget](MACHOS/TipsWidget.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/RecordWidgetExtension.appex/RecordWidgetExtension](MACHOS/RecordWidgetExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosSettingsWidgetExtension.appex/VoiceMemosSettingsWidgetExtension](MACHOS/VoiceMemosSettingsWidgetExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherDiagnosticExtension.appex/WeatherDiagnosticExtension](MACHOS/WeatherDiagnosticExtension.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents](MACHOS/WeatherIntents.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/fsck_apfs](MACHOS/fsck_apfs.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount](MACHOS/mount.md)
- [/sbin/newfs_apfs](MACHOS/newfs_apfs.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/brctl](MACHOS/brctl.md)
- [/usr/bin/fileproviderctl](MACHOS/fileproviderctl.md)
- [/usr/bin/footprint](MACHOS/footprint.md)
- [/usr/bin/modelmanagerdump](MACHOS/modelmanagerdump.md)
- [/usr/bin/powerlogHelperd](MACHOS/powerlogHelperd.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/bin/sysdiagnose](MACHOS/sysdiagnose.md)
- [/usr/bin/taskinfo](MACHOS/taskinfo.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libCoreFP.dylib](MACHOS/libCoreFP.dylib.md)
- [/usr/lib/libCoreLSKD.dylib](MACHOS/libCoreLSKD.dylib.md)
- [/usr/lib/libRPAC.dylib](MACHOS/libRPAC.dylib.md)
- [/usr/lib/libViewDebuggerSupport.dylib](MACHOS/libViewDebuggerSupport.dylib.md)
- [/usr/lib/swift/libswiftRemoteMirror.dylib](MACHOS/libswiftRemoteMirror.dylib.md)
- [/usr/lib/system/introspection/libdispatch.dylib](MACHOS/libdispatch.dylib.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent.md)
- [/usr/libexec/ContinuityCaptureAgent](MACHOS/ContinuityCaptureAgent.md)
- [/usr/libexec/DataDetectorsSourceAccess](MACHOS/DataDetectorsSourceAccess.md)
- [/usr/libexec/MTLAssetUpgraderD](MACHOS/MTLAssetUpgraderD.md)
- [/usr/libexec/MobileGestaltHelper](MACHOS/MobileGestaltHelper.md)
- [/usr/libexec/MobileStorageMounter](MACHOS/MobileStorageMounter.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/PerfPowerServices](MACHOS/PerfPowerServices.md)
- [/usr/libexec/PerfPowerServicesExtended](MACHOS/PerfPowerServicesExtended.md)
- [/usr/libexec/PowerUIAgent](MACHOS/PowerUIAgent.md)
- [/usr/libexec/PreboardService](MACHOS/PreboardService.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/SensorKitALSHelper](MACHOS/SensorKitALSHelper.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/UserEventAgent](MACHOS/UserEventAgent.md)
- [/usr/libexec/ViewHierarchyAgent](MACHOS/ViewHierarchyAgent.md)
- [/usr/libexec/adprivacyd](MACHOS/adprivacyd.md)
- [/usr/libexec/amfid](MACHOS/amfid.md)
- [/usr/libexec/aned](MACHOS/aned.md)
- [/usr/libexec/announced](MACHOS/announced.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/aonsensed](MACHOS/aonsensed.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/appleidsetupd](MACHOS/appleidsetupd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/appprotectiond](MACHOS/appprotectiond.md)
- [/usr/libexec/arkitd](MACHOS/arkitd.md)
- [/usr/libexec/asd](MACHOS/asd.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/atc](MACHOS/atc.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd.md)
- [/usr/libexec/avconferenced](MACHOS/avconferenced.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/backgroundassets.user](MACHOS/backgroundassets.user.md)
- [/usr/libexec/batteryalgorithmsd](MACHOS/batteryalgorithmsd.md)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced.md)
- [/usr/libexec/batterytrapd](MACHOS/batterytrapd.md)
- [/usr/libexec/betaenrollmentd](MACHOS/betaenrollmentd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/brookcompaniond](MACHOS/brookcompaniond.md)
- [/usr/libexec/bulletindistributord](MACHOS/bulletindistributord.md)
- [/usr/libexec/cameracaptured](MACHOS/cameracaptured.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/checkerboardd](MACHOS/checkerboardd.md)
- [/usr/libexec/ciphermld](MACHOS/ciphermld.md)
- [/usr/libexec/com.apple.Safari.History](MACHOS/com.apple.Safari.History.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/configd](MACHOS/configd.md)
- [/usr/libexec/continuitycaptured](MACHOS/continuitycaptured.md)
- [/usr/libexec/coordinated](MACHOS/coordinated.md)
- [/usr/libexec/coreduetd](MACHOS/coreduetd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/deferredmediad](MACHOS/deferredmediad.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/demod_helper](MACHOS/demod_helper.md)
- [/usr/libexec/deviceaccessd](MACHOS/deviceaccessd.md)
- [/usr/libexec/diagnosticextensionsd](MACHOS/diagnosticextensionsd.md)
- [/usr/libexec/diagnosticspushd](MACHOS/diagnosticspushd.md)
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
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/fmfd](MACHOS/fmfd.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/fskitd](MACHOS/fskitd.md)
- [/usr/libexec/gamecontrollerd](MACHOS/gamecontrollerd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/gputoolsserviced](MACHOS/gputoolsserviced.md)
- [/usr/libexec/griddatad](MACHOS/griddatad.md)
- [/usr/libexec/handwritingd](MACHOS/handwritingd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtelemetryd](MACHOS/hangtelemetryd.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/init_data_protection](MACHOS/init_data_protection.md)
- [/usr/libexec/inputanalyticsd](MACHOS/inputanalyticsd.md)
- [/usr/libexec/installd](MACHOS/installd.md)
- [/usr/libexec/keybagd](MACHOS/keybagd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd](MACHOS/logd.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/lskdd](MACHOS/lskdd.md)
- [/usr/libexec/mdmd](MACHOS/mdmd.md)
- [/usr/libexec/mdmuserd](MACHOS/mdmuserd.md)
- [/usr/libexec/mediasetupd](MACHOS/mediasetupd.md)
- [/usr/libexec/merchantd](MACHOS/merchantd.md)
- [/usr/libexec/metrickitd](MACHOS/metrickitd.md)
- [/usr/libexec/microstackshot](MACHOS/microstackshot.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mlruntimed](MACHOS/mlruntimed.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobile_installation_proxy](MACHOS/mobile_installation_proxy.md)
- [/usr/libexec/mobile_storage_proxy](MACHOS/mobile_storage_proxy.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanomediaremotelinkagent](MACHOS/nanomediaremotelinkagent.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/naturallanguaged](MACHOS/naturallanguaged.md)
- [/usr/libexec/neagent](MACHOS/neagent.md)
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
- [/usr/libexec/otpaird](MACHOS/otpaird.md)
- [/usr/libexec/passcodenagd](MACHOS/passcodenagd.md)
- [/usr/libexec/passwordbreachd](MACHOS/passwordbreachd.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/pipelined](MACHOS/pipelined.md)
- [/usr/libexec/pkd](MACHOS/pkd.md)
- [/usr/libexec/powerdatad](MACHOS/powerdatad.md)
- [/usr/libexec/powerexperienced](MACHOS/powerexperienced.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad.md)
- [/usr/libexec/ptpd](MACHOS/ptpd.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/relatived](MACHOS/relatived.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remoted](MACHOS/remoted.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/resourcegrabberd](MACHOS/resourcegrabberd.md)
- [/usr/libexec/restoreserviced](MACHOS/restoreserviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/runningboardd](MACHOS/runningboardd.md)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
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
- [/usr/libexec/siriknowledged](MACHOS/siriknowledged.md)
- [/usr/libexec/sirireaderd](MACHOS/sirireaderd.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/soundanalysisd](MACHOS/soundanalysisd.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/storagedatad](MACHOS/storagedatad.md)
- [/usr/libexec/storagekitd](MACHOS/storagekitd.md)
- [/usr/libexec/swcd](MACHOS/swcd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/symptomsd](MACHOS/symptomsd.md)
- [/usr/libexec/symptomsd-diag](MACHOS/symptomsd-diag.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/teslad](MACHOS/teslad.md)
- [/usr/libexec/textcontextd](MACHOS/textcontextd.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/timed](MACHOS/timed.md)
- [/usr/libexec/tipsd](MACHOS/tipsd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/triald](MACHOS/triald.md)
- [/usr/libexec/triald_system](MACHOS/triald_system.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tursd](MACHOS/tursd.md)
- [/usr/libexec/tvremoted](MACHOS/tvremoted.md)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd.md)
- [/usr/libexec/videosubscriptionsd](MACHOS/videosubscriptionsd.md)
- [/usr/libexec/watchdogd](MACHOS/watchdogd.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/webinspectord](MACHOS/webinspectord.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTAvrcp](MACHOS/BTAvrcp.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/distnoted](MACHOS/distnoted.md)
- [/usr/sbin/fairplayd.H2](MACHOS/fairplayd.H2.md)
- [/usr/sbin/filecoordinationd](MACHOS/filecoordinationd.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/mDNSResponderHelper](MACHOS/mDNSResponderHelper.md)
- [/usr/sbin/notifyd](MACHOS/notifyd.md)
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

 
-  __TEXT.__text: 0xc8418
+  __TEXT.__text: 0xc8410
   __TEXT.__cstring: 0x124a3
-  __TEXT.__const: 0x1e9b8
+  __TEXT.__const: 0x1e9c0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x320
   __TEXT.__constructor: 0x0

```

#### SmartIOFirmware_ASCv6.im4p

>  `SmartIOFirmware_ASCv6.im4p`

```diff

 
-  __TEXT.__text: 0x1a9c0
+  __TEXT.__text: 0x1a9b8
   __TEXT.__cstring: 0x1087
-  __TEXT.__const: 0x310
+  __TEXT.__const: 0x318
   __TEXT._rtk_mtab: 0x290
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0

```

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

 
-  __TEXT.__text: 0x963cd0
+  __TEXT.__text: 0x970cec
   __TEXT.__data_copy: 0x100000
-  __TEXT.__const: 0x7f61c0
-  __TEXT.__cstring: 0x125450
+  __TEXT.__const: 0x7f9470
+  __TEXT.__cstring: 0x1262ef
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x507ac
   __TEXT.__eh_frame: 0x308
-  __DATA.__const: 0x51a10
+  __DATA.__const: 0x51f30
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xdf108
   __DATA._rtk_power: 0x3a8

```

#### agx_a000.bin

>  `agx_a000.bin`

```diff

 
-  __TEXT.__text: 0x5a99c
+  __TEXT.__text: 0x5a9d0
   __TEXT.__gxf_code: 0x106c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1e10
+  __TEXT.__const: 0x1e20
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x554

```

#### agx_b000.bin

>  `agx_b000.bin`

```diff

 
-  __TEXT.__text: 0x5a6a0
+  __TEXT.__text: 0x5a6d4
   __TEXT.__gxf_code: 0x106c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1e50
+  __TEXT.__const: 0x1e60
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x554

```

#### agx_b100.bin

>  `agx_b100.bin`

```diff

 
-  __TEXT.__text: 0x5a6a0
+  __TEXT.__text: 0x5a6d4
   __TEXT.__gxf_code: 0x106c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1e50
+  __TEXT.__const: 0x1e60
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x554

```

#### ansf.t8130.release.im4p

>  `ansf.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x171c60
+  __TEXT.__text: 0x171c7c
   __TEXT.shared: 0xb6e4
   __TEXT.read: 0x5a78
-  __TEXT.__const: 0x8e58
+  __TEXT.__const: 0x8e68
   __TEXT.idle_hooks: 0x10
   __TEXT.__cstring: 0x1e59a
   __TEXT.__chain_starts: 0x0

```

#### aopfw-iphone16aop.RELEASE.im4p

>  `aopfw-iphone16aop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0x12f570
-  __TEXT.__const: 0x11dc0
-  __TEXT.__cstring: 0x7a4f
+  __TEXT.__text: 0x12fde8
+  __TEXT.__const: 0x11db8
+  __TEXT.__cstring: 0x81e1
   __TEXT.__chain_starts: 0x50
   __TEXT.__eh_frame: 0x40
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_heap: 0x3b340
   __DATA.__const: 0x132b8
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x7310
+  __DATA.__data: 0x7308
   __DATA._rtk_patchbay: 0x319
   __DATA._rtk_power: 0x3b8
   __DATA._spu_service: 0xa20

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xd0b70
-  __ETEXT.__StaticInit: 0x7648
-  __ETEXT.__text: 0x39b10
+  __ETEXT.__StaticInit: 0x764c
+  __ETEXT.__text: 0x396c8
   __ETEXT.__const: 0xdce
   __EDATA.__data: 0x60
-  __OS_LOG.__string: 0x2789e
+  __OS_LOG.__string: 0x276f6
   __MISC.__apf_list: 0xb0
-  __CMA.__cma_log_string: 0x3e24
+  __CMA.__cma_log_string: 0x3df8
   Symbols:   0
   Functions: 0
 

```

#### h16x_ane_fw_iaso_d8x.im4p

>  `h16x_ane_fw_iaso_d8x.im4p`

```diff

 
-  __TEXT.__text: 0xadb24
+  __TEXT.__text: 0xaeb14
   __TEXT.__data_copy: 0x8000
-  __TEXT.__const: 0xc388
-  __TEXT.__cstring: 0x1ae59
+  __TEXT.__const: 0xc380
+  __TEXT.__cstring: 0x1ae76
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

```

#### rans.t8130.release.im4p

>  `rans.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x171c60
+  __TEXT.__text: 0x171c7c
   __TEXT.shared: 0xb6e4
   __TEXT.read: 0x5a78
-  __TEXT.__const: 0x8e58
+  __TEXT.__const: 0x8e68
   __TEXT.idle_hooks: 0x10
   __TEXT.__cstring: 0x1e59a
   __TEXT.__chain_starts: 0x0

```

#### sptm.t8122.release.im4p

>  `sptm.t8122.release.im4p`

```diff

-392.0.6.0.0
-  __TEXT.__cstring: 0xb986
+392.0.26.0.0
+  __TEXT.__cstring: 0xc184
   __TEXT.__binname: 0x40
-  __TEXT.__chain_starts: 0x74
+  __TEXT.__chain_starts: 0x6c
   __TEXT.__const: 0x9d0
-  __DATA_CONST.__const: 0x63188
-  __TEXT_EXEC.__text: 0x3ff24
+  __DATA_CONST.__const: 0x5990
+  __LATE_CONST.__late_const: 0x5d5e0
+  __TEXT_EXEC.__text: 0x47228
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6
-  __DATA.__common: 0x71d0
-  __DATA.__bss: 0x56b0
+  __DATA.__common: 0x73d0
+  __DATA.__bss: 0x5bf0
   __BOOTDATA.__data: 0x14000
   Symbols:   1
   Functions: 0

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2dd3cc
-  __TEXT.__const: 0x7ce90
-  __TEXT.__cstring: 0x30d18
+  __TEXT.__text: 0x2e24d8
+  __TEXT.__const: 0x7cebc
+  __TEXT.__cstring: 0x30d44
   __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x4a338
+  __DATA.__const: 0x4a400
   __DATA._rtk_patchbay: 0x710
   __DATA._rtk_data_uuid: 0x40
-  __DATA.__data: 0x2b4e4
+  __DATA.__data: 0x2b53c
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA._afk_sys_drv: 0xac0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__mod_init_func: 0x90
+  __DATA.__mod_init_func: 0x88
   __DATA._afk_sys_objt: 0xbb0
   __DATA._rtk_mtab: 0x5c8
-  __DATA.__zerofill: 0x9b6c0
-  __OS_LOG.__string: 0x20e8a
+  __DATA.__zerofill: 0x9f210
+  __OS_LOG.__string: 0x20f69
   Symbols:   0
   Functions: 0
 

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2dd3cc
-  __TEXT.__const: 0x7ce90
-  __TEXT.__cstring: 0x30d18
+  __TEXT.__text: 0x2e24d8
+  __TEXT.__const: 0x7cebc
+  __TEXT.__cstring: 0x30d44
   __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x4a338
+  __DATA.__const: 0x4a400
   __DATA._rtk_patchbay: 0x710
   __DATA._rtk_data_uuid: 0x40
-  __DATA.__data: 0x2b4e4
+  __DATA.__data: 0x2b53c
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA._afk_sys_drv: 0xac0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__mod_init_func: 0x90
+  __DATA.__mod_init_func: 0x88
   __DATA._afk_sys_objt: 0xbb0
   __DATA._rtk_mtab: 0x5c8
-  __DATA.__zerofill: 0x9b6c0
-  __OS_LOG.__string: 0x20e8a
+  __DATA.__zerofill: 0x9f210
+  __OS_LOG.__string: 0x20f69
   Symbols:   0
   Functions: 0
 

```

#### t8130pmp.im4p

>  `t8130pmp.im4p`

```diff

 
-  __TEXT.__text: 0x36b5c
-  __TEXT.__const: 0x2300
+  __TEXT.__text: 0x370d0
+  __TEXT.__const: 0x2310
   __TEXT.__cstring: 0x1634
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__mod_init_func: 0x10
-  __DATA.__zerofill: 0x4d3f0
+  __DATA.__zerofill: 0x4d410
   Symbols:   0
   Functions: 0
 

```

#### txm.iphoneos.release.im4p

>  `txm.iphoneos.release.im4p`

```diff

-135.0.3.0.0
-  __TEXT.__cstring: 0x574c
+135.0.5.0.1
+  __TEXT.__cstring: 0x5781
   __TEXT.__const: 0x4210
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x20
-  __TEXT.__info_plist: 0x4ff
+  __TEXT.__info_plist: 0x500
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x7d40
-  __TEXT_EXEC.__text: 0x3f10c
+  __DATA_CONST.__const: 0x7c98
+  __TEXT_EXEC.__text: 0x3f1dc
   __TEXT_BOOT_EXEC.__text: 0x4058
   __TEXT_BOOT_EXEC.__bootcode: 0x2c
   __DATA.__data: 0x278
   __DATA.__common: 0xa70
   __DATA.__bss: 0x490
+  __LATE_CONST.__late_const: 0xa8
   Symbols:   1
   Functions: 0
 

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.0 *(22A5282m)* | 619.1.15.10.1 |
| 18.0 *(22A5297f)* | 619.1.18.10.1 |

### Dylibs

#### 🆕 NEW (5)

- `/System/Library/AccessibilityBundles/PlasterBoardUI.axbundle/PlasterBoardUI`
- `/System/Library/PrivateFrameworks/FitnessSync.framework/FitnessSync`
- `/System/Library/PrivateFrameworks/FitnessTrainerTips.framework/FitnessTrainerTips`
- `/System/Library/PrivateFrameworks/SetupKitUI.framework/SetupKitUI`
- `/System/Library/PrivateFrameworks/SiriMailOntology.framework/SiriMailOntology`

#### ❌ Removed (3)

- `/System/Library/Frameworks/TipsNext.framework/TipsNext`
- `/System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth`
- `/System/Library/PrivateFrameworks/OpticalFlowFramework.framework/OpticalFlowFramework`

#### ⬆️ Updated (1790)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider](DYLIBS/ASMessagesProvider.md)
- [/System/Library/AccessibilityBundles/AVFoundation.axbundle/AVFoundation](DYLIBS/AVFoundation.md)
- [/System/Library/AccessibilityBundles/AVKit.axbundle/AVKit](DYLIBS/AVKit.md)
- [/System/Library/AccessibilityBundles/AXActionSheetUIServer.axuiservice/AXActionSheetUIServer](DYLIBS/AXActionSheetUIServer.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/Library/AccessibilityBundles/AcousticId-Assistant.axbundle/AcousticId-Assistant](DYLIBS/AcousticId-Assistant.md)
- [/System/Library/AccessibilityBundles/AnnotationKit.axbundle/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension](DYLIBS/AppInstallExtension.md)
- [/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore](DYLIBS/AppStore.md)
- [/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade](DYLIBS/Arcade.md)
- [/System/Library/AccessibilityBundles/AuthKitUI.axbundle/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/AccessibilityBundles/AvatarUI.axbundle/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/BiometricKitUI.axbundle/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension](DYLIBS/BridgeStoreExtension.md)
- [/System/Library/AccessibilityBundles/CameraEffectsKit.axbundle/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/AccessibilityBundles/CarPlay.axbundle/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/ContactsAutocompleteUI.axbundle/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/AccessibilityBundles/ContactsUI.axbundle/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/AccessibilityBundles/ConversationKit.axbundle/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/AccessibilityBundles/DocumentManagerExecutables.axbundle/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/EventKitUIFramework](DYLIBS/EventKitUIFramework.md)
- [/System/Library/AccessibilityBundles/FaceTime.axbundle/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/AccessibilityBundles/GameCenterPrivateUIFramework.axbundle/GameCenterPrivateUIFramework](DYLIBS/GameCenterPrivateUIFramework.md)
- [/System/Library/AccessibilityBundles/GameCenterUIFramework.axbundle/GameCenterUIFramework](DYLIBS/GameCenterUIFramework.md)
- [/System/Library/AccessibilityBundles/HealthExperienceUI.axbundle/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/AccessibilityBundles/HealthMedicationsUI.axbundle/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/AccessibilityBundles/HealthUI.axbundle/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/AccessibilityBundles/HomeUI.axbundle/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/AccessibilityBundles/HomeUIService.axbundle/HomeUIService](DYLIBS/HomeUIService.md)
- [/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService](DYLIBS/InCallService.md)
- [/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework](DYLIBS/MapKitFramework.md)
- [/System/Library/AccessibilityBundles/Maps.axbundle/Maps](DYLIBS/Maps.md)
- [/System/Library/AccessibilityBundles/MapsUI.axbundle/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/AccessibilityBundles/MedicationsHealthAppPlugin.axbundle/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/MessageUIFramework](DYLIBS/MessageUIFramework.md)
- [/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail](DYLIBS/MobileMail.md)
- [/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone](DYLIBS/MobilePhone.md)
- [/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework](DYLIBS/MobileSafariFramework.md)
- [/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/AccessibilityBundles/MobileStoreUI.axbundle/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/AccessibilityBundles/MobileTimer-Assistant.axbundle/MobileTimer-Assistant](DYLIBS/MobileTimer-Assistant.md)
- [/System/Library/AccessibilityBundles/Movies-Assistant.axbundle/Movies-Assistant](DYLIBS/Movies-Assistant.md)
- [/System/Library/AccessibilityBundles/Music.axbundle/Music](DYLIBS/Music.md)
- [/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication](DYLIBS/MusicApplication.md)
- [/System/Library/AccessibilityBundles/OnBoardingKit.axbundle/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/AccessibilityBundles/PDFKit.axbundle/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/AccessibilityBundles/PassKitUI.axbundle/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/AccessibilityBundles/Pegasus.axbundle/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/AccessibilityBundles/PhotoLibraryFramework.axbundle/PhotoLibraryFramework](DYLIBS/PhotoLibraryFramework.md)
- [/System/Library/AccessibilityBundles/PhotosUICore.axbundle/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/AccessibilityBundles/PreBoard.axbundle/PreBoard](DYLIBS/PreBoard.md)
- [/System/Library/AccessibilityBundles/PreferencesFramework.axbundle/PreferencesFramework](DYLIBS/PreferencesFramework.md)
- [/System/Library/AccessibilityBundles/PrivacySettingsUI.axbundle/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension](DYLIBS/ProductPageExtension.md)
- [/System/Library/AccessibilityBundles/SIMSetupUIService.axbundle/SIMSetupUIService](DYLIBS/SIMSetupUIService.md)
- [/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/AccessibilityBundles/ScreenshotServicesFramework.axbundle/ScreenshotServicesFramework](DYLIBS/ScreenshotServicesFramework.md)
- [/System/Library/AccessibilityBundles/SearchUI.axbundle/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/AccessibilityBundles/Setup.axbundle/Setup](DYLIBS/Setup.md)
- [/System/Library/AccessibilityBundles/SetupAssistantUI.axbundle/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/AccessibilityBundles/SocialFramework.axbundle/SocialFramework](DYLIBS/SocialFramework.md)
- [/System/Library/AccessibilityBundles/SocialWeeApp.axbundle/SocialWeeApp](DYLIBS/SocialWeeApp.md)
- [/System/Library/AccessibilityBundles/Spotlight.axbundle/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/AccessibilityBundles/SpotlightUIInternalFramework.axbundle/SpotlightUIInternalFramework](DYLIBS/SpotlightUIInternalFramework.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardFoundation.axbundle/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/SpringBoardUIServices.axbundle/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/AccessibilityBundles/StocksWidget.axbundle/StocksWidget](DYLIBS/StocksWidget.md)
- [/System/Library/AccessibilityBundles/StoreKitUI.axbundle/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/AccessibilityBundles/SwiftUI.axbundle/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/AccessibilityBundles/TipsApp.axbundle/TipsApp](DYLIBS/TipsApp.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/VectorKit.axbundle/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore](DYLIBS/WebCore.md)
- [/System/Library/AccessibilityBundles/WebProcess.axbundle/WebProcess](DYLIBS/WebProcess.md)
- [/System/Library/AccessibilityBundles/WorkflowUI.axbundle/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/AccessibilityBundles/iCloudDriveApp.axbundle/iCloudDriveApp](DYLIBS/iCloudDriveApp.md)
- [/System/Library/AccessibilityBundles/iTunesStoreUIFramework.axbundle/iTunesStoreUIFramework](DYLIBS/iTunesStoreUIFramework.md)
- [/System/Library/Accounts/Notification/DMDAccountNotificationPlugin.bundle/DMDAccountNotificationPlugin](DYLIBS/DMDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityHeadphoneLevelsControlCenterModule.bundle/AccessibilityHeadphoneLevelsControlCenterModule](DYLIBS/AccessibilityHeadphoneLevelsControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityLiveListenControlCenterModule.bundle/AccessibilityLiveListenControlCenterModule](DYLIBS/AccessibilityLiveListenControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityMotionCuesControlCenterModule.bundle/AccessibilityMotionCuesControlCenterModule](DYLIBS/AccessibilityMotionCuesControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityShorcutsModule.bundle/AccessibilityShorcutsModule](DYLIBS/AccessibilityShorcutsModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilitySoundDetectionControlCenterModule.bundle/AccessibilitySoundDetectionControlCenterModule](DYLIBS/AccessibilitySoundDetectionControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule.md)
- [/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule.md)
- [/System/Library/ControlCenter/Bundles/BackgroundSoundsCCModule.bundle/BackgroundSoundsCCModule](DYLIBS/BackgroundSoundsCCModule.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule](DYLIBS/DisplayModule.md)
- [/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule](DYLIBS/FlashlightModule.md)
- [/System/Library/ControlCenter/Bundles/HeadphoneAccommodationsCCModule.bundle/HeadphoneAccommodationsCCModule](DYLIBS/HeadphoneAccommodationsCCModule.md)
- [/System/Library/ControlCenter/Bundles/HearingAidsModule.bundle/HearingAidsModule](DYLIBS/HearingAidsModule.md)
- [/System/Library/ControlCenter/Bundles/HearingDevicesCCModule.bundle/HearingDevicesCCModule](DYLIBS/HearingDevicesCCModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterCompactModule.bundle/HomeControlCenterCompactModule](DYLIBS/HomeControlCenterCompactModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterSingleTileModule.bundle/HomeControlCenterSingleTileModule](DYLIBS/HomeControlCenterSingleTileModule.md)
- [/System/Library/ControlCenter/Bundles/KeyboardBrightnessModule.bundle/KeyboardBrightnessModule](DYLIBS/KeyboardBrightnessModule.md)
- [/System/Library/ControlCenter/Bundles/LowPowerModule.bundle/LowPowerModule](DYLIBS/LowPowerModule.md)
- [/System/Library/ControlCenter/Bundles/MediaControlsAudioModule.bundle/MediaControlsAudioModule](DYLIBS/MediaControlsAudioModule.md)
- [/System/Library/ControlCenter/Bundles/MediaControlsModule.bundle/MediaControlsModule](DYLIBS/MediaControlsModule.md)
- [/System/Library/ControlCenter/Bundles/MuteModule.bundle/MuteModule](DYLIBS/MuteModule.md)
- [/System/Library/ControlCenter/Bundles/OrientationLockModule.bundle/OrientationLockModule](DYLIBS/OrientationLockModule.md)
- [/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule](DYLIBS/PerformanceTraceModule.md)
- [/System/Library/ControlCenter/Bundles/ShazamModule.bundle/ShazamModule](DYLIBS/ShazamModule.md)
- [/System/Library/ControlCenter/Bundles/SpokenNotificationsModule.bundle/SpokenNotificationsModule](DYLIBS/SpokenNotificationsModule.md)
- [/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule](DYLIBS/TVRemoteModule.md)
- [/System/Library/ControlCenter/Bundles/WalletModule.bundle/WalletModule](DYLIBS/WalletModule.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0](DYLIBS/AGXMetalG16P_A0.md)
- [/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0](DYLIBS/AGXMetalG16P_B0.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVFoundation.framework/AVFoundation](DYLIBS/AVFoundation.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib.md)
- [/System/Library/Frameworks/Accessibility.framework/Accessibility](DYLIBS/Accessibility.md)
- [/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit](DYLIBS/AccessorySetupKit.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit](DYLIBS/AdAttributionKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/AutomatedDeviceEnrollment](DYLIBS/AutomatedDeviceEnrollment.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies](DYLIBS/AACDependencies.md)
- [/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets](DYLIBS/BackgroundAssets.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit.md)
- [/System/Library/Frameworks/CarKey.framework/CarKey](DYLIBS/CarKey.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Cinematic.framework/Cinematic](DYLIBS/Cinematic.md)
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
- [/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI](DYLIBS/CoreMIDI.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
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
- [/System/Library/Frameworks/DockKit.framework/DockKit](DYLIBS/DockKit.md)
- [/System/Library/Frameworks/DriverKit.framework/DriverKit](DYLIBS/DriverKit.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit](DYLIBS/ExtensionKit.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControls](DYLIBS/FamilyControls.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GSS.framework/GSS](DYLIBS/GSS.md)
- [/System/Library/Frameworks/GameController.framework/GameController](DYLIBS/GameController.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HealthKitUI.framework/HealthKitUI](DYLIBS/HealthKitUI.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/IOSurface.framework/IOSurface](DYLIBS/IOSurface.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/JournalingSuggestions.framework/JournalingSuggestions](DYLIBS/JournalingSuggestions.md)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils](DYLIBS/DaemonUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings](DYLIBS/ManagedSettings.md)
- [/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI](DYLIBS/ManagedSettingsUI.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Messages.framework/Messages](DYLIBS/Messages.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX.md)
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
- [/System/Library/Frameworks/ReplayKit.framework/ReplayKit](DYLIBS/ReplayKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou](DYLIBS/SharedWithYou.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration](DYLIBS/SystemConfiguration.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork](DYLIBS/ThreadNetwork.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/Translation.framework/Translation](DYLIBS/Translation.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/VisionKit.framework/VisionKit](DYLIBS/VisionKit.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib](DYLIBS/libWebKitSwift.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_CoreLocationUI_SwiftUI.framework/_CoreLocationUI_SwiftUI](DYLIBS/_CoreLocationUI_SwiftUI.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI.md)
- [/System/Library/Frameworks/_WorkoutKit_SwiftUI.framework/_WorkoutKit_SwiftUI](DYLIBS/_WorkoutKit_SwiftUI.md)
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
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/ResearchApp.healthplugin/ResearchApp](DYLIBS/ResearchApp.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications](DYLIBS/NanoCompassComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAegirFaceBundleCompanion.bundle/NTKAegirFaceBundleCompanion](DYLIBS/NTKAegirFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFoghornFaceBundleCompanion.bundle/NTKFoghornFaceBundleCompanion](DYLIBS/NTKFoghornFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGalleonFaceBundleCompanion.bundle/NTKGalleonFaceBundleCompanion](DYLIBS/NTKGalleonFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVivaldiFaceBundleCompanion.bundle/NTKVivaldiFaceBundleCompanion](DYLIBS/NTKVivaldiFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings](DYLIBS/MobilePhoneSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/AACCore](DYLIBS/AACCore.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/ALDataTypes.framework/ALDataTypes.dylib](DYLIBS/ALDataTypes.dylib.md)
- [/System/Library/PrivateFrameworks/ANEClientSignals.framework/ANEClientSignals](DYLIBS/ANEClientSignals.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/libORTools.dylib](DYLIBS/libORTools.dylib.md)
- [/System/Library/PrivateFrameworks/ANEServices.framework/ANEServices](DYLIBS/ANEServices.md)
- [/System/Library/PrivateFrameworks/AONSense.framework/AONSense.dylib](DYLIBS/AONSense.dylib.md)
- [/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem](DYLIBS/APConfigurationSystem.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore.md)
- [/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon](DYLIBS/ARKitDaemon.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings](DYLIBS/AUSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader](DYLIBS/AXAssetLoader.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils](DYLIBS/AXFrontBoardUtils.md)
- [/System/Library/PrivateFrameworks/AXMotionCuesServices.framework/AXMotionCuesServices](DYLIBS/AXMotionCuesServices.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection](DYLIBS/AXSoundDetection.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AXTapToSpeakTime.framework/AXTapToSpeakTime](DYLIBS/AXTapToSpeakTime.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenServices.framework/AXWatchRemoteScreenServices](DYLIBS/AXWatchRemoteScreenServices.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI](DYLIBS/AXWatchRemoteScreenUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction.md)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteUIServices.framework/AccessibilityRemoteUIServices](DYLIBS/AccessibilityRemoteUIServices.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth](DYLIBS/AccessoryComponentAuth.md)
- [/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI](DYLIBS/AccountsUI.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient.md)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdID.framework/AdID](DYLIBS/AdID.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AeroML.framework/AeroML](DYLIBS/AeroML.md)
- [/System/Library/PrivateFrameworks/AirPlayAndHandoffSettingsSupport.framework/AirPlayAndHandoffSettingsSupport](DYLIBS/AirPlayAndHandoffSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/AirPlaySenderKit](DYLIBS/AirPlaySenderKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice](DYLIBS/AirTrafficDevice.md)
- [/System/Library/PrivateFrameworks/AlarmUIFramework.framework/AlarmUIFramework](DYLIBS/AlarmUIFramework.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D.md)
- [/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit](DYLIBS/AppConduit.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIWidget.framework/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI](DYLIBS/AppProtectionUI.md)
- [/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore](DYLIBS/AppSSOCore.md)
- [/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos](DYLIBS/AppSSOKerberos.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation](DYLIBS/AppStoreFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport](DYLIBS/AppSupport.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA](DYLIBS/AppleCVA.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater](DYLIBS/AppleConvergedFirmwareUpdater.md)
- [/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore](DYLIBS/AppleDepthCore.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport](DYLIBS/AppleDeviceQuerySupport.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libAppleDeviceQueryArmory.dylib](DYLIBS/libAppleDeviceQueryArmory.dylib.md)
- [/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate](DYLIBS/AppleFirmwareUpdate.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG](DYLIBS/AppleJPEG.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitSupport.framework/AppleMediaServicesKitSupport](DYLIBS/AppleMediaServicesKitSupport.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine](DYLIBS/AppleNeuralEngine.md)
- [/System/Library/PrivateFrameworks/ApplePDPHelper.framework/ApplePDPHelper](DYLIBS/ApplePDPHelper.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication](DYLIBS/AppleTracingSupportSymbolication.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices](DYLIBS/AssertionServices.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI](DYLIBS/AssistiveTouchUI.md)
- [/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness](DYLIBS/AttentionAwareness.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager](DYLIBS/AudioDSPManager.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion](DYLIBS/AudiogramIngestion.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI](DYLIBS/AutoFillUI.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/AvatarPoster.framework/AvatarPoster](DYLIBS/AvatarPoster.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices](DYLIBS/BackBoardServices.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/BarcodeSupport](DYLIBS/BarcodeSupport.md)
- [/System/Library/PrivateFrameworks/BarcodeSupportUI.framework/BarcodeSupportUI](DYLIBS/BarcodeSupportUI.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms](DYLIBS/BatteryAlgorithms.md)
- [/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter](DYLIBS/BatteryCenter.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync](DYLIBS/BiomeSync.md)
- [/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport](DYLIBS/BiometricSupport.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BlockMonitoring.framework/BlockMonitoring](DYLIBS/BlockMonitoring.md)
- [/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices](DYLIBS/BluetoothServices.md)
- [/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices](DYLIBS/BoardServices.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BookLibrary.framework/BookLibrary](DYLIBS/BookLibrary.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/BookLibraryCore](DYLIBS/BookLibraryCore.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation.md)
- [/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl](DYLIBS/BrightnessControl.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/BusinessFoundation.framework/BusinessFoundation](DYLIBS/BusinessFoundation.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/BusinessServicesUI.framework/BusinessServicesUI](DYLIBS/BusinessServicesUI.md)
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
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP](DYLIBS/CVNLP.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase](DYLIBS/CalendarDatabase.md)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation](DYLIBS/CalendarFoundation.md)
- [/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/CalendarIntegrationSupport](DYLIBS/CalendarIntegrationSupport.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarMigration.framework/CalendarMigration](DYLIBS/CalendarMigration.md)
- [/System/Library/PrivateFrameworks/CalendarNotification.framework/CalendarNotification](DYLIBS/CalendarNotification.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/CalendarUIKitInternal](DYLIBS/CalendarUIKitInternal.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork](DYLIBS/CaptiveNetwork.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework](DYLIBS/CarCommandsUIFramework.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup](DYLIBS/CarPlaySetup.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices.md)
- [/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices](DYLIBS/CarouselPreferenceServices.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/Categories.framework/Categories](DYLIBS/Categories.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsSupport.framework/WidgetPreviewsSupport](DYLIBS/WidgetPreviewsSupport.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation](DYLIBS/ClarityFoundation.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit](DYLIBS/ClassroomKit.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
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
- [/System/Library/PrivateFrameworks/CloudMediaServicesInterfaceKit.framework/CloudMediaServicesInterfaceKit](DYLIBS/CloudMediaServicesInterfaceKit.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices](DYLIBS/CloudServices.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing](DYLIBS/CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI](DYLIBS/CloudSharingUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry](DYLIBS/CloudTelemetry.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI](DYLIBS/CommunicationSafetySettingsUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera](DYLIBS/CompanionCamera.md)
- [/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon](DYLIBS/CompanionHealthDaemon.md)
- [/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay](DYLIBS/ComplicationDisplay.md)
- [/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards](DYLIBS/ComputeSafeguards.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync](DYLIBS/ContextSync.md)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/ContextualUnderstanding](DYLIBS/ContextualUnderstanding.md)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices](DYLIBS/ControlCenterUIServices.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreAUC.framework/CoreAUC](DYLIBS/CoreAUC.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreChartSwift.framework/CoreChartSwift](DYLIBS/CoreChartSwift.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib](DYLIBS/CoreGEM.dylib.md)
- [/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest](DYLIBS/CoreGPSTest.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred](DYLIBS/CoreIDCred.md)
- [/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder](DYLIBS/CoreIDCredBuilder.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreIK.framework/CoreIK](DYLIBS/CoreIK.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf](DYLIBS/CoreLocationProtobuf.md)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream.md)
- [/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms](DYLIBS/CoreMotionAlgorithms.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO](DYLIBS/CoreRealityIO.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite](DYLIBS/CoreRepairLite.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine](DYLIBS/CoreRoutine.md)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG](DYLIBS/CoreSVG.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal](DYLIBS/CoreServicesInternal.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/CoreThemeDefinition](DYLIBS/CoreThemeDefinition.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary](DYLIBS/DEPClientLibrary.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary](DYLIBS/DMCEnrollmentLibrary.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing](DYLIBS/DSRemotePairing.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal](DYLIBS/DarwinDirectoryInternal.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryQuery.framework/DarwinDirectoryQuery](DYLIBS/DarwinDirectoryQuery.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess](DYLIBS/DataAccess.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport.md)
- [/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices](DYLIBS/DataDeliveryServices.md)
- [/System/Library/PrivateFrameworks/DataDetectorsNaturalLanguage.framework/DataDetectorsNaturalLanguage](DYLIBS/DataDetectorsNaturalLanguage.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing](DYLIBS/DeviceSharing.md)
- [/System/Library/PrivateFrameworks/DeviceSharingServices.framework/DeviceSharingServices](DYLIBS/DeviceSharingServices.md)
- [/System/Library/PrivateFrameworks/DeviceSharingUI.framework/DeviceSharingUI](DYLIBS/DeviceSharingUI.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest](DYLIBS/DiagnosticRequest.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit](DYLIBS/DiagnosticsKit.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/DiagnosticsSessionAvailability](DYLIBS/DiagnosticsSessionAvailability.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DirectResource.framework/DirectResource](DYLIBS/DirectResource.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb](DYLIBS/DoNotDisturb.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbKit.framework/DoNotDisturbKit](DYLIBS/DoNotDisturbKit.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement](DYLIBS/DriverManagement.md)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity](DYLIBS/EDPSecurity.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/EnergyKitFoundation.framework/EnergyKitFoundation](DYLIBS/EnergyKitFoundation.md)
- [/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState](DYLIBS/EnhancedLoggingState.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/EventKitTCCUI.framework/EventKitTCCUI](DYLIBS/EventKitTCCUI.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FRC.framework/FRC](DYLIBS/FRC.md)
- [/System/Library/PrivateFrameworks/FSEvents.framework/FSEvents](DYLIBS/FSEvents.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/FedStats.framework/FedStats](DYLIBS/FedStats.md)
- [/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore](DYLIBS/FedStatsPluginCore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger](DYLIBS/FeedbackLogger.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore](DYLIBS/FinHealthCore.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
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
- [/System/Library/PrivateFrameworks/FitnessSharePlaySession.framework/FitnessSharePlaySession](DYLIBS/FitnessSharePlaySession.md)
- [/System/Library/PrivateFrameworks/FitnessSiriSession.framework/FitnessSiriSession](DYLIBS/FitnessSiriSession.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities](DYLIBS/FitnessUtilities.md)
- [/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan](DYLIBS/FitnessWorkoutPlan.md)
- [/System/Library/PrivateFrameworks/Fluid.framework/Fluid](DYLIBS/Fluid.md)
- [/System/Library/PrivateFrameworks/FocusEngine.framework/FocusEngine](DYLIBS/FocusEngine.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/FontServices](DYLIBS/FontServices.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib](DYLIBS/libGSFontCache.dylib.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/GESS.framework/GESS](DYLIBS/GESS.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation](DYLIBS/GameControllerFoundation.md)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy.md)
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
- [/System/Library/PrivateFrameworks/Geometry.framework/Geometry](DYLIBS/Geometry.md)
- [/System/Library/PrivateFrameworks/GraphComputeRT.framework/GraphComputeRT](DYLIBS/GraphComputeRT.md)
- [/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices](DYLIBS/GridDataServices.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing](DYLIBS/HDRProcessing.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment](DYLIBS/HRTFEnrollment.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient](DYLIBS/HangTracerSettingsClient.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService](DYLIBS/HeadphoneProxFeatureService.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon](DYLIBS/HealthAppHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices](DYLIBS/HealthAppServices.md)
- [/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration](DYLIBS/HealthArticlesGeneration.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceAppPlugin.framework/HealthBalanceAppPlugin](DYLIBS/HealthBalanceAppPlugin.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation](DYLIBS/HealthDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/HealthDiagnosticExtensionCore](DYLIBS/HealthDiagnosticExtensionCore.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon](DYLIBS/HealthHearingDaemon.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications](DYLIBS/HealthMedications.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin](DYLIBS/HealthMedicationsDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI](DYLIBS/HealthMedicationsWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesUI.framework/HealthMenstrualCyclesUI](DYLIBS/HealthMenstrualCyclesUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesWidgetUI.framework/HealthMenstrualCyclesWidgetUI](DYLIBS/HealthMenstrualCyclesWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration](DYLIBS/HealthOrchestration.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService](DYLIBS/HearingModeService.md)
- [/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI](DYLIBS/HearingModeSettingsUI.md)
- [/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI](DYLIBS/HearingModeUI.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth](DYLIBS/HeartHealth.md)
- [/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon](DYLIBS/HeartHealthDaemon.md)
- [/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal](DYLIBS/Heimdal.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI](DYLIBS/HomeAI.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
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
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents](DYLIBS/HomeWidgetIntents.md)
- [/System/Library/PrivateFrameworks/HoverTextServices.framework/HoverTextServices](DYLIBS/HoverTextServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMAVCore.framework/IMAVCore](DYLIBS/IMAVCore.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMCorePipeline.framework/IMCorePipeline](DYLIBS/IMCorePipeline.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMRCSTransfer.framework/IMRCSTransfer](DYLIBS/IMRCSTransfer.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/IMTranscoding](DYLIBS/IMTranscoding.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU](DYLIBS/IOGPU.md)
- [/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer](DYLIBS/IOMobileFramebuffer.md)
- [/System/Library/PrivateFrameworks/IPConfiguration.framework/IPConfiguration](DYLIBS/IPConfiguration.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/ImageGenerationUI.framework/ImageGenerationUI](DYLIBS/ImageGenerationUI.md)
- [/System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam](DYLIBS/InertiaCam.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/InputToolKitUI.framework/InputToolKitUI](DYLIBS/InputToolKitUI.md)
- [/System/Library/PrivateFrameworks/InputTranscoder.framework/InputTranscoder](DYLIBS/InputTranscoder.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowFeedbackDataCollector.framework/IntelligenceFlowFeedbackDataCollector](DYLIBS/IntelligenceFlowFeedbackDataCollector.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared](DYLIBS/IntelligenceFlowShared.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting](DYLIBS/IntelligentRouting.md)
- [/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon](DYLIBS/IntelligentRoutingDaemon.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/JournalShared.framework/JournalShared](DYLIBS/JournalShared.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/Koa.framework/Koa](DYLIBS/Koa.md)
- [/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper](DYLIBS/KoaMapper.md)
- [/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache](DYLIBS/LLMCache.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinguisticData.framework/LinguisticData](DYLIBS/LinguisticData.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS](DYLIBS/LiveFS.md)
- [/System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices](DYLIBS/LiveSpeechServices.md)
- [/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription](DYLIBS/LiveTranscription.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationPreboard.framework/LocalAuthenticationPreboard](DYLIBS/LocalAuthenticationPreboard.md)
- [/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge](DYLIBS/LocalSpeechRecognitionBridge.md)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit](DYLIBS/LocalStatusKit.md)
- [/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport](DYLIBS/LoggingSupport.md)
- [/System/Library/PrivateFrameworks/LoginKit.framework/LoginKit](DYLIBS/LoginKit.md)
- [/System/Library/PrivateFrameworks/LoginUILogViewer.framework/LoginUILogViewer](DYLIBS/LoginUILogViewer.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MIL.framework/MIL](DYLIBS/MIL.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32023/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailServices.framework/MailServices](DYLIBS/MailServices.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC](DYLIBS/ManagedSettingsObjC.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MathTypesetting.framework/MathTypesetting](DYLIBS/MathTypesetting.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/MediaAnalysisBlastDoorSupport](DYLIBS/MediaAnalysisBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl](DYLIBS/MediaControl.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService](DYLIBS/MediaConversionService.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation](DYLIBS/MediaFoundation.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth](DYLIBS/MentalHealth.md)
- [/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon](DYLIBS/MentalHealthDaemon.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthWidgetUI.framework/MentalHealthWidgetUI](DYLIBS/MentalHealthWidgetUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation](DYLIBS/MicroLocation.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation](DYLIBS/MobileActivation.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager](DYLIBS/MobileContainerManager.md)
- [/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI](DYLIBS/MobileIdentityServiceUI.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation](DYLIBS/MobileInstallation.md)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariSwift.framework/MobileSafariSwift](DYLIBS/MobileSafariSwift.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate](DYLIBS/MobileSoftwareUpdate.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage](DYLIBS/MobileStorage.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
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
- [/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets](DYLIBS/MorphunAssets.md)
- [/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging](DYLIBS/MotionSensorLogging.md)
- [/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI](DYLIBS/MusicCarDisplayUI.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/NLPLearner](DYLIBS/NLPLearner.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit](DYLIBS/NPTKit.md)
- [/System/Library/PrivateFrameworks/NanoHomeScreenUIServices.framework/NanoHomeScreenUIServices](DYLIBS/NanoHomeScreenUIServices.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/NanoLeash](DYLIBS/NanoLeash.md)
- [/System/Library/PrivateFrameworks/NanoMediaBridgeUI.framework/NanoMediaBridgeUI](DYLIBS/NanoMediaBridgeUI.md)
- [/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync](DYLIBS/NanoMusicSync.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore](DYLIBS/NanoPhotosCore.md)
- [/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry](DYLIBS/NanoRegistry.md)
- [/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber](DYLIBS/NanoResourceGrabber.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings](DYLIBS/NanoSystemSettings.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions](DYLIBS/NearbySessions.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/NeighborhoodActivityConduit](DYLIBS/NeighborhoodActivityConduit.md)
- [/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics](DYLIBS/NetworkStatistics.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/NewsAnalyticsUpload](DYLIBS/NewsAnalyticsUpload.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation](DYLIBS/NewsFoundation.md)
- [/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit](DYLIBS/NewsKit.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/NewsServices](DYLIBS/NewsServices.md)
- [/System/Library/PrivateFrameworks/NewsServicesInternal.framework/NewsServicesInternal](DYLIBS/NewsServicesInternal.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI](DYLIBS/NewsUI.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NewsURLResolution.framework/NewsURLResolution](DYLIBS/NewsURLResolution.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics](DYLIBS/NotesAnalytics.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSiriUI.framework/NotesSiriUI](DYLIBS/NotesSiriUI.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices](DYLIBS/NotesUIServices.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate](DYLIBS/OSAnalyticsPrivate.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OmniSearchTypes.framework/OmniSearchTypes](DYLIBS/OmniSearchTypes.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PLSnapshot.framework/PLSnapshot](DYLIBS/PLSnapshot.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PairedSync.framework/PairedSync](DYLIBS/PairedSync.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE](DYLIBS/ParavirtualizedANE.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard](DYLIBS/Pasteboard.md)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase](DYLIBS/PaymentUIBase.md)
- [/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI](DYLIBS/PencilPairingUI.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterMetrics.framework/PeopleSuggesterMetrics](DYLIBS/PeopleSuggesterMetrics.md)
- [/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor](DYLIBS/PerfPowerMetricMonitor.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader](DYLIBS/PerfPowerServicesReader.md)
- [/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit](DYLIBS/PerformanceControlKit.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalIntelligenceCore.framework/PersonalIntelligenceCore](DYLIBS/PersonalIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/Phoenix.framework/Phoenix](DYLIBS/Phoenix.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibrary.framework/PhotoLibrary](DYLIBS/PhotoLibrary.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosFaceLayoutCore.framework/PhotosFaceLayoutCore](DYLIBS/PhotosFaceLayoutCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligenceCore.framework/PhotosIntelligenceCore](DYLIBS/PhotosIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PhotosKnowledgeGraph.framework/PhotosKnowledgeGraph](DYLIBS/PhotosKnowledgeGraph.md)
- [/System/Library/PrivateFrameworks/PhotosMediaFoundation.framework/PhotosMediaFoundation](DYLIBS/PhotosMediaFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer](DYLIBS/PhotosPlayer.md)
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
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSQLite.framework/PoirotSQLite](DYLIBS/PoirotSQLite.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation](DYLIBS/PosterFoundation.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport](DYLIBS/PosterPlatformSupport.md)
- [/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation](DYLIBS/PosterUIFoundation.md)
- [/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience](DYLIBS/PowerExperience.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting](DYLIBS/PowerlogAccounting.md)
- [/System/Library/PrivateFrameworks/PowerlogControl.framework/PowerlogControl](DYLIBS/PowerlogControl.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting](DYLIBS/PrivacyAccounting.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/PrivateMLClientInferenceProvider](DYLIBS/PrivateMLClientInferenceProvider.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse](DYLIBS/ProactiveShareSheetDataHarvestingLighthouse.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/PromptKit.framework/PromptKit](DYLIBS/PromptKit.md)
- [/System/Library/PrivateFrameworks/ProofReader.framework/ProofReader](DYLIBS/ProofReader.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/RESync.framework/RESync](DYLIBS/RESync.md)
- [/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting](DYLIBS/RTCReporting.md)
- [/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI](DYLIBS/RTTUI.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion](DYLIBS/RealityFusion.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/RealityKitInspection.framework/RealityKitInspection](DYLIBS/RealityKitInspection.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal](DYLIBS/ReflectionInternal.md)
- [/System/Library/PrivateFrameworks/RelativeMotion.framework/RelativeMotion](DYLIBS/RelativeMotion.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore](DYLIBS/RemoteManagementStore.md)
- [/System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI](DYLIBS/RemoteManagementUI.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth](DYLIBS/RespiratoryHealth.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon](DYLIBS/RespiratoryHealthDaemon.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders](DYLIBS/SCSharingReminders.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SILManager.framework/SILManager](DYLIBS/SILManager.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SMBClientEngine.framework/SMBClientEngine](DYLIBS/SMBClientEngine.md)
- [/System/Library/PrivateFrameworks/SOSUI.framework/SOSUI](DYLIBS/SOSUI.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing](DYLIBS/SafariSafeBrowsing.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/Frameworks/SAHelper.framework/SAHelper](DYLIBS/SAHelper.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/Scandium.framework/Scandium](DYLIBS/Scandium.md)
- [/System/Library/PrivateFrameworks/SceneIntelligence.framework/SceneIntelligence](DYLIBS/SceneIntelligence.md)
- [/System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices](DYLIBS/ScreenContinuityServices.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingAccessibilityService.framework/ScreenSharingAccessibilityService](DYLIBS/ScreenSharingAccessibilityService.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices](DYLIBS/ScreenshotServices.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit](DYLIBS/SecureCaptureKit.md)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService](DYLIBS/SecureTransactionService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit](DYLIBS/SetupKit.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices](DYLIBS/SeymourClientServices.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServerProtocol.framework/SeymourServerProtocol](DYLIBS/SeymourServerProtocol.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamInsights.framework/ShazamInsights](DYLIBS/ShazamInsights.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SilexVideo.framework/SilexVideo](DYLIBS/SilexVideo.md)
- [/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb](DYLIBS/SilexWeb.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution](DYLIBS/SiriAppResolution.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
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
- [/System/Library/PrivateFrameworks/SiriCorrections.framework/SiriCorrections](DYLIBS/SiriCorrections.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback](DYLIBS/SiriCrossDeviceArbitrationFeedback.md)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine](DYLIBS/SiriDialogEngine.md)
- [/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher](DYLIBS/SiriEntityMatcher.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo](DYLIBS/SiriGeo.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/SiriInferredHelpfulness](DYLIBS/SiriInferredHelpfulness.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes](DYLIBS/SiriInformationTypes.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriIntentEvents.framework/SiriIntentEvents](DYLIBS/SiriIntentEvents.md)
- [/System/Library/PrivateFrameworks/SiriInteractive.framework/SiriInteractive](DYLIBS/SiriInteractive.md)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/SiriInvocationAnalytics](DYLIBS/SiriInvocationAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriOrchestration.framework/SiriOrchestration](DYLIBS/SiriOrchestration.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningLogging.framework/SiriPrivateLearningLogging](DYLIBS/SiriPrivateLearningLogging.md)
- [/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents](DYLIBS/SiriReaderIntents.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel](DYLIBS/SiriReferenceResolutionDataModel.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSettingsUI.framework/SiriSettingsUI](DYLIBS/SiriSettingsUI.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSocialConversation.framework/SiriSocialConversation](DYLIBS/SiriSocialConversation.md)
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
- [/System/Library/PrivateFrameworks/SiriTranslationUI.framework/SiriTranslationUI](DYLIBS/SiriTranslationUI.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge](DYLIBS/SiriUIBridge.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX](DYLIBS/SiriVOX.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework](DYLIBS/SiriVideoUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution.md)
- [/System/Library/PrivateFrameworks/Sleep.framework/Sleep](DYLIBS/Sleep.md)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon](DYLIBS/SleepDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon](DYLIBS/SleepHealthDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport](DYLIBS/SoftwareUpdateCoreSupport.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution](DYLIBS/SpaceAttribution.md)
- [/System/Library/PrivateFrameworks/SpatialAudioServices.framework/SpatialAudioServices](DYLIBS/SpatialAudioServices.md)
- [/System/Library/PrivateFrameworks/SpatialInspectorFoundation.framework/SpatialInspectorFoundation](DYLIBS/SpatialInspectorFoundation.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport](DYLIBS/SpeechRecognitionSharedSupport.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding](DYLIBS/SpotlightEmbedding.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport](DYLIBS/SpotlightSettingsSupport.md)
- [/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal](DYLIBS/SpotlightUIInternal.md)
- [/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared](DYLIBS/SpotlightUIShared.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit.md)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/StrokeAnimation.framework/StrokeAnimation](DYLIBS/StrokeAnimation.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SwiftNN.framework/SwiftNN](DYLIBS/SwiftNN.md)
- [/System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite](DYLIBS/SwiftSQLite.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics](DYLIBS/SymptomAnalytics.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationLite.framework/SymptomPresentationLite](DYLIBS/SymptomPresentationLite.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC](DYLIBS/TelephonyRPC.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCJK.framework/TextInputCJK](DYLIBS/TextInputCJK.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/chs.dylib](DYLIBS/chs.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/cht.dylib](DYLIBS/cht.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/deu.dylib](DYLIBS/deu.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eng.dylib](DYLIBS/eng.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/enu.dylib](DYLIBS/enu.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esm.dylib](DYLIBS/esm.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esp.dylib](DYLIBS/esp.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fin.dylib](DYLIBS/fin.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fra.dylib](DYLIBS/fra.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/frc.dylib](DYLIBS/frc.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ita.dylib](DYLIBS/ita.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/jpn.dylib](DYLIBS/jpn.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/kor.dylib](DYLIBS/kor.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ptb.dylib](DYLIBS/ptb.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/TextureIO.framework/TextureIO](DYLIBS/TextureIO.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](DYLIBS/Tightbeam.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitLegacy.framework/TipKitLegacy](DYLIBS/TipKitLegacy.md)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices](DYLIBS/TipKitServices.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote](DYLIBS/TouchRemote.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/Transliteration.framework/Transliteration](DYLIBS/Transliteration.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI](DYLIBS/TransparencyUI.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers](DYLIBS/TrustedPeers.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UniversalHIDKit.framework/UniversalHIDKit](DYLIBS/UniversalHIDKit.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_cs.dylib](DYLIBS/livefiles_cs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib](DYLIBS/livefiles_exfat.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib](DYLIBS/livefiles_msdos.dylib.md)
- [/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement](DYLIBS/UserManagement.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices](DYLIBS/UserNotificationsServices.md)
- [/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings](DYLIBS/UserNotificationsSettings.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage](DYLIBS/VirtualGarage.md)
- [/System/Library/PrivateFrameworks/Visage.framework/Visage](DYLIBS/Visage.md)
- [/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore](DYLIBS/VisionCore.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/libvoiced_tts.dylib](DYLIBS/libvoiced_tts.dylib.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices](DYLIBS/VoiceServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
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
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI.md)
- [/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI](DYLIBS/WelcomeKitUI.md)
- [/System/Library/PrivateFrameworks/WellnessUI.framework/WellnessUI](DYLIBS/WellnessUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity](DYLIBS/WiFiVelocity.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity](DYLIBS/WirelessProximity.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness](DYLIBS/WorkflowResponsiveness.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/XOJITExecutor.framework/XOJITExecutor](DYLIBS/XOJITExecutor.md)
- [/System/Library/PrivateFrameworks/XavierNews.framework/XavierNews](DYLIBS/XavierNews.md)
- [/System/Library/PrivateFrameworks/ZeoliteFramework.framework/ZeoliteFramework](DYLIBS/ZeoliteFramework.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib.md)
- [/System/Library/PrivateFrameworks/_AppIntentsServices_AppIntents.framework/_AppIntentsServices_AppIntents](DYLIBS/_AppIntentsServices_AppIntents.md)
- [/System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI](DYLIBS/_IconServices_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore](DYLIBS/_MusicKitInternal_MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlayer.framework/_MusicKitInternal_MediaPlayer](DYLIBS/_MusicKitInternal_MediaPlayer.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/caulk.framework/caulk](DYLIBS/caulk.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps](DYLIBS/iMessageApps.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime](DYLIBS/lighthouse_runtime.md)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport](DYLIBS/CaptiveNetworkSupport.md)
- [/System/Library/TextInput/TextInput_ja.bundle/TextInput_ja](DYLIBS/TextInput_ja.md)
- [/System/Library/TextInput/TextInput_ko.bundle/TextInput_ko](DYLIBS/TextInput_ko.md)
- [/System/Library/TextInput/TextInput_ta.bundle/TextInput_ta](DYLIBS/TextInput_ta.md)
- [/System/Library/TextInput/TextInput_vi.bundle/TextInput_vi](DYLIBS/TextInput_vi.md)
- [/System/Library/TextInput/TextInput_zh.bundle/TextInput_zh](DYLIBS/TextInput_zh.md)
- [/System/Library/VideoCodecs/H264SW.videocodec](DYLIBS/H264SW.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder](DYLIBS/AppleProResHWEncoder.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoProcessors/NRFV2.bundle/NRFV2](DYLIBS/NRFV2.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/i18n/libiconv_std.dylib](DYLIBS/libiconv_std.dylib.md)
- [/usr/lib/libARI.dylib](DYLIBS/libARI.dylib.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAppleEXR.dylib](DYLIBS/libAppleEXR.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib.md)
- [/usr/lib/libBasebandCommandDrivers.dylib](DYLIBS/libBasebandCommandDrivers.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversMIPC.dylib](DYLIBS/libBasebandCommandDriversMIPC.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerDAL.dylib](DYLIBS/libBasebandManagerDAL.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libFDR.dylib](DYLIBS/libFDR.dylib.md)
- [/usr/lib/libInFieldCollection.dylib](DYLIBS/libInFieldCollection.dylib.md)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libMobileGestaltExtensions.dylib](DYLIBS/libMobileGestaltExtensions.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libNFC_HAL.dylib](DYLIBS/libNFC_HAL.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libSESShared.dylib](DYLIBS/libSESShared.dylib.md)
- [/usr/lib/libSMC.dylib](DYLIBS/libSMC.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libVinylNonUpdater.dylib](DYLIBS/libVinylNonUpdater.dylib.md)
- [/usr/lib/libamsupport.dylib](DYLIBS/libamsupport.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libdns_services.dylib](DYLIBS/libdns_services.dylib.md)
- [/usr/lib/libfire7.dylib](DYLIBS/libfire7.dylib.md)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libktrace.dylib](DYLIBS/libktrace.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmorphun.dylib](DYLIBS/libmorphun.dylib.md)
- [/usr/lib/libmrc.dylib](DYLIBS/libmrc.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnfrestore.dylib](DYLIBS/libnfrestore.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libpcap.A.dylib](DYLIBS/libpcap.A.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftCallKit.dylib](DYLIBS/libswiftCallKit.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftDemangle.dylib](DYLIBS/libswiftDemangle.dylib.md)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib.md)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)
- [/usr/lib/swift/libswiftObservation.dylib](DYLIBS/libswiftObservation.dylib.md)
- [/usr/lib/swift/libswiftSynchronization.dylib](DYLIBS/libswiftSynchronization.dylib.md)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib.md)
- [/usr/lib/swift/libswift_Differentiation.dylib](DYLIBS/libswift_Differentiation.dylib.md)
- [/usr/lib/swift/libswift_RegexParser.dylib](DYLIBS/libswift_RegexParser.dylib.md)
- [/usr/lib/swift/libswift_StringProcessing.dylib](DYLIBS/libswift_StringProcessing.dylib.md)
- [/usr/lib/swift/libswiftsimd.dylib](DYLIBS/libswiftsimd.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libdispatch.dylib](DYLIBS/libdispatch.dylib.md)
- [/usr/lib/system/libsystem_blocks.dylib](DYLIBS/libsystem_blocks.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_coreservices.dylib](DYLIBS/libsystem_coreservices.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_m.dylib](DYLIBS/libsystem_m.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib.md)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib.md)
- [/usr/lib/system/libxpc.dylib](DYLIBS/libxpc.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib.md)
- [/usr/lib/updaters/libSavageUpdater_iOS.dylib](DYLIBS/libSavageUpdater_iOS.dylib.md)
- [/usr/lib/updaters/libT200Updater.dylib](DYLIBS/libT200Updater.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

## EOF
