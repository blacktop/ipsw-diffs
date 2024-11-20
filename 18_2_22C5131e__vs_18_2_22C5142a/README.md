# 18.2 (22C5131e) .vs 18.2 (22C5142a)

## IPSWs

- `iPhone17,1_18.2_22C5131e_Restore.ipsw`
- `iPhone17,1_18.2_22C5142a_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.2 *(22C5131e)* | 24.2.0 | 11215.60.405~55 | Sun, 03Nov2024 22:57:30 PST |
| 18.2 *(22C5142a)* | 24.2.0 | 11215.62.3~2 | Thu, 14Nov2024 22:18:12 PST |

### Kexts

#### ⬆️ Updated (16)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleAVD`

```diff

-807.0.0.0.0
+808.0.0.0.0
   __TEXT.__const: 0x9a8c9
   __TEXT.__cstring: 0x5277
   __TEXT.__os_log: 0x12f18
-  __TEXT_EXEC.__text: 0x45574
+  __TEXT_EXEC.__text: 0x45658
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x2d08
+  __DATA_CONST.__const: 0x2d60
   __DATA_CONST.__kalloc_var: 0xbe0
   __DATA_CONST.__kalloc_type: 0x2600
-  Functions: 1415
+  Functions: 1426
   Symbols:   0
   CStrings:  1459
 

```

>  `com.apple.driver.AppleOLYHAL`

```diff

-405.15.0.0.0
+405.16.0.0.0
   __TEXT.__const: 0x7a8
-  __TEXT.__cstring: 0x471a
-  __TEXT_EXEC.__text: 0x1cba0
+  __TEXT.__cstring: 0x4607
+  __TEXT_EXEC.__text: 0x1ca2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
   __DATA_CONST.__const: 0x13b8
-  __DATA_CONST.__kalloc_type: 0x640
-  Functions: 551
+  __DATA_CONST.__kalloc_type: 0x600
+  Functions: 549
   Symbols:   0
-  CStrings:  497
+  CStrings:  496
 
CStrings:
+ "\"%s:%u:\" \"!failed\" @%s:%d"
+ "\"%s:%u:\" \"task\" @%s:%d"
+ "\"%s:%u:\" \"threadCall\" @%s:%d"
- "\"%s:%u:\" \"triggerAsyncResetWork(kAppleOLYHALPortInterfaceActionPowerOn) == kIOReturnSuccess\" @%s:%d"
- "\"%s:%u:\" \"triggerAsyncResetWork(kAppleOLYHALPortInterfaceActionPrepareOutsideFunctionReset) == kIOReturnSuccess\" @%s:%d"
- "\"%s:%u:\" \"triggerAsyncResetWork(kAppleOLYHALPortInterfaceActionReset) == kIOReturnSuccess\" @%s:%d"
- "%s::%s: thread_call_enter1 failed\n"

```

>  `com.apple.driver.AppleT8140CLPC`

```diff

-1175.60.50.0.1
-  __TEXT.__cstring: 0x2ba3
+1175.60.51.0.0
+  __TEXT.__cstring: 0x2b9f
   __TEXT.__const: 0xc8c
   __TEXT_EXEC.__text: 0x4fee4
   __TEXT_EXEC.__auth_stubs: 0x0
CStrings:
+ "2024-11-14T22:53:15-08:00"
+ "AppleCLPC-1175.60.51"
- "2024-11-03T22:35:02-08:00"
- "AppleCLPC-1175.60.50.0.1"

```

>  `com.apple.kext.CoreTrust`

```diff

-148.0.2.0.0
-  __TEXT.__const: 0xfe8
-  __TEXT_EXEC.__text: 0x8620
+148.60.1.0.0
+  __TEXT.__const: 0x10d2
+  __TEXT_EXEC.__text: 0x87e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x10
   __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x14e0
-  Functions: 128
+  __DATA_CONST.__const: 0x1558
+  Functions: 130
   Symbols:   0
   CStrings:  0
 

```

>  `com.apple.security.AppleImage4`

```diff

 320.60.4.0.0
   __TEXT.__const: 0x79f4
-  __TEXT.__cstring: 0x5ec0
+  __TEXT.__cstring: 0x5ec2
   __TEXT_EXEC.__text: 0x245a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6f8
CStrings:
+ "@(#)VERSION:Darwin Image4 Extension Version 7.0.0: Thu Nov 14 22:06:40 PST 2024; root:AppleImage4-320.60.4~227/AppleImage4/RELEASE_ARM64E"
+ "Darwin Image4 Extension Version 7.0.0: Thu Nov 14 22:06:40 PST 2024; root:AppleImage4-320.60.4~227/AppleImage4/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Image4 Extension Version 7.0.0: Sun Nov  3 22:26:48 PST 2024; root:AppleImage4-320.60.4~25/AppleImage4/RELEASE_ARM64E"
- "Darwin Image4 Extension Version 7.0.0: Sun Nov  3 22:26:48 PST 2024; root:AppleImage4-320.60.4~25/AppleImage4/RELEASE_ARM64E"

```

>  `com.apple.security.sandbox`

```diff

-2401.60.112.0.0
+2401.60.113.0.0
   __TEXT.__const: 0x18e4e9
   __TEXT.__cstring: 0x70d3
   __TEXT.__os_log: 0x20a1
-  __TEXT_EXEC.__text: 0x317e4
+  __TEXT_EXEC.__text: 0x3174c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x15420

   __DATA_CONST.__const: 0x3640
   __DATA_CONST.__kalloc_var: 0x4b0
   __DATA_CONST.__kalloc_type: 0xb40
-  Functions: 658
+  Functions: 657
   Symbols:   0
   CStrings:  1315
 

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-8.203.0.0.0
-  __TEXT.__os_log: 0x3300f
+8.203.4.0.0
+  __TEXT.__os_log: 0x3303b
   __TEXT.__cstring: 0xa5cd
   __TEXT.__const: 0x690
-  __TEXT_EXEC.__text: 0xa3990
+  __TEXT_EXEC.__text: 0xa3bb0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3948
   __DATA.__common: 0x3c8

   __DATA_CONST.__kalloc_var: 0x2e40
   Functions: 1816
   Symbols:   0
-  CStrings:  3552
+  CStrings:  3553
 
CStrings:
+ "ANE%d: %s: WARN: client context is invalid\n"

```

>  `com.apple.driver.AppleSPU`

```diff

-1014.60.5.0.0
+1014.60.5.0.1
   __TEXT.__cstring: 0x5aae
-  __TEXT.__os_log: 0x955
+  __TEXT.__os_log: 0x944
   __TEXT.__const: 0x358
-  __TEXT_EXEC.__text: 0x498dc
+  __TEXT_EXEC.__text: 0x498d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x878
   __DATA.__common: 0x970
CStrings:
+ "Dropped gnss data report due to missing data queue (%zu)"
+ "Dropped gnss data report for queue (%zu)"
+ "Dropped gnss event due to missing data queue (%zu)"
+ "Dropped gnss event due to oversized packet (%zu)"
+ "Dropped gnss event for queue (%zu)"
- "Dropped gnss data report due to missing data queue %zu"
- "Dropped gnss data report for queue error: %#x (%zu)"
- "Dropped gnss event due to missing data queue %zu"
- "Dropped gnss event due to oversized packet: %zu"
- "Dropped gnss event for queue error: %#x (%zu)"

```

>  `com.apple.iokit.IOSkywalkFamily`

```diff

-508.60.1.0.0
+508.60.2.0.0
   __TEXT.__cstring: 0x1ade
   __TEXT.__const: 0xd40
-  __TEXT_EXEC.__text: 0x35e38
+  __TEXT_EXEC.__text: 0x35d54
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe8
   __DATA.__common: 0x6b0
   __DATA.__bss: 0x9c
-  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x130

   __DATA_CONST.__const: 0x8cd0
   __DATA_CONST.__kalloc_type: 0x1640
   __DATA_CONST.__kalloc_var: 0x640
-  Functions: 1853
+  Functions: 1852
   Symbols:   0
   CStrings:  281
 

```

>  `com.apple.iokit.IOTimeSyncFamily`

```diff

-1320.7.0.0.0
+1320.8.0.0.0
   __TEXT.__cstring: 0x3298
   __TEXT.__os_log: 0x74e4
   __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x2f3e4
+  __TEXT_EXEC.__text: 0x2f424
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x638

```

>  `com.apple.driver.AppleConvergedPCI`

```diff

-109.0.0.0.0
+110.0.0.0.0
   __TEXT.__const: 0x1e0
   __TEXT.__cstring: 0x6c2f
-  __TEXT_EXEC.__text: 0x3eb64
+  __TEXT_EXEC.__text: 0x3eb84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

```

>  `com.apple.driver.AppleMobileDispH17P-DCP`

```diff

-397.14.4.0.0
-  __TEXT.__cstring: 0x5c91
+397.17.0.0.0
+  __TEXT.__cstring: 0x5dae
   __TEXT.__const: 0x1a40
-  __TEXT_EXEC.__text: 0x21754
+  __TEXT_EXEC.__text: 0x21928
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2c0
   __DATA.__common: 0xf0
   __DATA.__bss: 0x8179
-  __DATA_CONST.__auth_got: 0x700
+  __DATA_CONST.__auth_got: 0x728
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x3fa8
-  __DATA_CONST.__kalloc_type: 0x5c0
+  __DATA_CONST.__const: 0x3fc0
+  __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0xf0
-  Functions: 1138
+  Functions: 1139
   Symbols:   0
-  CStrings:  543
+  CStrings:  551
 
CStrings:
+ "\"%s: Failed to allocate _upload_trace_lock\" @%s:%d"
+ "%s: Should not be entering here - async_swap = %d, swapID = %d!!\n"
+ "%s: log_write called but trace not enabled\n"
+ "1"
+ "1211111212221212121212222222222221111111111111211111111111111122221111112222222222222221122221122211222222222221111122122212222221222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212212212212212212212212212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111111111111111111111111112222222222222122122122122122122122122121111111111112111222111112222112112222222222222222222222222222221111111111121211111212211111221112222222222222222222222222222222222222222222222222222222222222222222222222222222221"
+ "121111121222121212121222222222222111111111111121111111111111112222111111222222222222222112222112221122222222222111112212221222222122222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221221221221221221221221221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212212212212212212212212212111111111111211122211111222211211222222222222222222222222222222111111111112121111121221111122111222222222222222222222222222222222222222222222222222222222222222222222222222222222111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111122222222221"
+ "12121211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212"
+ "FrameInfoBuffer"
+ "IOMFBFrameInfoBuffer.cpp"
+ "site.Lock"
+ "void IOMFB::FrameInfoBuffer::log_write(const FrameInfoData *)"
- "121111121222121212121222222222222111111111111121111111111111222211111122222222222222211222211222112222222222211111221222122222212222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111111111111111111111111112222222222222122122122122122122122122122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221221221221221221221221221211111111111121112221111122221121122222222222222222222222222222211111111111212111112122111122112222222222222222222222222222222222222222222222222222222222222222222222222222222221"
- "12111112122212121212122222222222211111111111112111111111111122221111112222222222222221122221122211222222222221111122122212222221222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212212212212212212212212212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111111111111111111111111112222222222222122122122122122122122122121111111111112111222111112222112112222222222222222222222222222221111111111121211111212211112211222222222222222222222222222222222222222222222222222222222222222222222222222222222111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111122222222221"
- "1212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212"

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-397.14.4.0.0
-  __TEXT.__cstring: 0x3f31
+397.17.0.0.0
+  __TEXT.__cstring: 0x4022
   __TEXT.__const: 0x2f88
-  __TEXT_EXEC.__text: 0x1ffc4
+  __TEXT_EXEC.__text: 0x201d8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe0
   __DATA.__common: 0x26d0

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x1640
-  __DATA_CONST.__kalloc_type: 0x7c0
-  Functions: 693
+  __DATA_CONST.__const: 0x1648
+  __DATA_CONST.__kalloc_type: 0x800
+  Functions: 696
   Symbols:   0
-  CStrings:  365
+  CStrings:  370
 
CStrings:
+ "\"IOMFB: Failed to allocate _service_count_lock\" @%s:%d"
+ "%s: Can't send need swap notification since notify queue empty!\n"
+ "%s: Dropped need_swap_notify notification!\n"
+ "121111121222121212121222222222222111111111111121111111111111112222111111222222222222222112222112221122222222222111112212221222222122222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221221221221221221221221221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212212212212212212212212212111111111111211122211111222211211222222222222222222222222222222111"
+ "12121211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212"
+ "D590_callback__"
+ "async_swap_hw forced to false -> YUV layer with surface\n"
+ "need_swap_notify"
- "1211111212221212121212222222222221111111111111211111111111112222111111222222222222222112222112221122222222222111112212221222222122222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221221221221221221221221221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212212212212212212212212212111111111111211122211111222211211222222222222222222222222222222111"
- "1212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212211212121212121212121212121212121212121212121212121212121212121212"
- "D588_callback__"

```

>  `com.apple.kernel`

```diff

-11215.60.405.0.0
+11215.62.3.0.0
   __TEXT.__const: 0x34270
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x72df0
+  __TEXT.__cstring: 0x72dd0
   __TEXT.__os_log: 0x276f6
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7f35f4
+  __TEXT_EXEC.__text: 0x7f3350
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x45b4f
-  Functions: 20496
+  Functions: 20495
   Symbols:   0
-  CStrings:  17259
+  CStrings:  17257
 
CStrings:
- "mbuf invalid: %p @%s:%d"
- "mptcp.c"

```

>  `com.apple.driver.AppleBluetoothModule`

```diff

-65.1.0.0.0
+66.0.0.0.0
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x25a0
-  __TEXT_EXEC.__text: 0x7c18
+  __TEXT_EXEC.__text: 0x7c58
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-397.14.4.0.0
-  __TEXT.__cstring: 0x823d
+397.17.0.0.0
+  __TEXT.__cstring: 0x8255
   __TEXT.__const: 0x9f4
-  __TEXT_EXEC.__text: 0x20f50
+  __TEXT_EXEC.__text: 0x20f58
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2900
   __DATA.__common: 0x1c92c

   __DATA_CONST.__got: 0x120
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x65c0
+  __DATA_CONST.__const: 0x65c8
   __DATA_CONST.__kalloc_type: 0xac0
-  Functions: 1133
+  Functions: 1134
   Symbols:   0
   CStrings:  957
 
CStrings:
+ "121111121222121211111111111121222211111111111122122221121111111111112212222112111111111111221222211211111111111122122221121111111111112212222112111111111111221222211211111111111122122221122"
+ "121111121222121212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111111111111111111111111112222222222222122122122122122122122122122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221221221221221221221221221211111111111111111112211111111111111122222222222222222222222222222222222222222221211112111111111111121122222"
- "12111112122212121111111111112122221111111111112212222112111111111111221222211211111111111122122221121111111111112212222112111111111111221222211211111111111122122221122"
- "1211111212221212121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221221221221221221221221221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212212212212212212212212212111111111111111112211111111111111122222222222222222222222222222222222222222221211112111111111111121122222"

```

</details>

## MachO

### 🆕 NEW (10)

- `/System/Library/ExtensionKit/Extensions/PhotosAppIntentsExtension.appex/PhotosAppIntentsExtension`
- `/System/Library/PreferenceBundles/PaymentContactlessUIPlugin.bundle/PaymentContactlessUIPlugin`
- `/private/var/staged_system_apps/MobileSafari.app/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker`
- `/usr/lib/libLogRedirect.dylib`
- `/usr/lib/libffi-trampolines.dylib`
- `/usr/lib/libglInterpose.dylib`
- `/usr/lib/libmobileassetd.dylib`
- `/usr/lib/libobjc-trampolines.dylib`
- `/usr/lib/libstdc++.6.0.9.dylib`
- `/usr/libexec/BatteryAlgorithms.framework/BatteryAlgorithms`

### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/CustodianInviteMessageExtension.appex/CustodianInviteMessageExtension`
- `/System/Library/PrivateFrameworks/MobileSafari.framework/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker`

### ⬆️ Updated (326)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AXUIViewService.app/AXUIViewService](MACHOS/AXUIViewService.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AppDeletionUIHost.app/AppDeletionUIHost](MACHOS/AppDeletionUIHost.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI](MACHOS/AuthenticationServicesUI.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/Jellyfish.app/PlugIns/Animoji.appex/Animoji](MACHOS/Animoji.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI.md)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/Spotlight.app/Spotlight](MACHOS/Spotlight.md)
- [/Applications/StickerPickerService.app/StickerPickerService](MACHOS/StickerPickerService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StoreKitUIService.app/StoreKitUIService](MACHOS/StoreKitUIService.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Applications/iCloud+.app/iCloud+](MACHOS/iCloud+.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation](MACHOS/Foundation.md)
- [/System/ExclaveKit/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](MACHOS/SoundAnalysis.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8140_IR_ISP_EK_Component.framework/T8140_IR_ISP_EK_Component](MACHOS/T8140_IR_ISP_EK_Component.md)
- [/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision](MACHOS/Vision.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8140_ExclaveISPSharedLib_exclavekit.framework/T8140_ExclaveISPSharedLib_exclavekit](MACHOS/T8140_ExclaveISPSharedLib_exclavekit.md)
- [/System/Library/AccessibilityBundles/AXAggregateStatisticsServer.axuiservice/AXAggregateStatisticsServer](MACHOS/AXAggregateStatisticsServer.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/EscrowSecurityAlert.app/EscrowSecurityAlert](MACHOS/EscrowSecurityAlert.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration](MACHOS/AccessibilityDataMigration.md)
- [/System/Library/DataClassMigrators/AppleAccountMigrator.migrator/AppleAccountMigrator](MACHOS/AppleAccountMigrator.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari](MACHOS/MobileSafari.md)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AirDropSettingsIntents.appex/AirDropSettingsIntents](MACHOS/AirDropSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension](MACHOS/CameraSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DefaultAppsSettingsIntents.appex/DefaultAppsSettingsIntents](MACHOS/DefaultAppsSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents](MACHOS/GeneralSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/InstalledAppsSettingsAppIntents.appex/InstalledAppsSettingsAppIntents](MACHOS/InstalledAppsSettingsAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/KeyboardSettingsExtension.appex/KeyboardSettingsExtension](MACHOS/KeyboardSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PasscodeSettingsExtension.appex/PasscodeSettingsExtension](MACHOS/PasscodeSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension](MACHOS/WiFiSettingsControlsExtension.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService](MACHOS/ContactsButtonXPCService.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin](MACHOS/CoreLocationNumberedMapCalloutPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTestImporter.appex/CoreSpotlightTestImporter](MACHOS/CoreSpotlightTestImporter.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTextImporter.appex/CoreSpotlightTextImporter](MACHOS/CoreSpotlightTextImporter.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/MechPasscode](MACHOS/MechPasscode.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId](MACHOS/MechTouchId.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader](MACHOS/com.apple.SafariServices.ContentBlockerLoader.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension](MACHOS/SKAskPermissionExtension.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
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
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/PlugIns/iMessageLite.imservice/iMessageLite](MACHOS/iMessageLite.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeAppStoreDaemonSettings.bundle/BridgeAppStoreDaemonSettings](MACHOS/BridgeAppStoreDaemonSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPhotosBridgeSettings.bundle/NanoPhotosBridgeSettings](MACHOS/NanoPhotosBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings](MACHOS/CSLCompanionLiveActivitiesSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/DefaultAppsSettingsUIPlugin.bundle/DefaultAppsSettingsUIPlugin](MACHOS/DefaultAppsSettingsUIPlugin.md)
- [/System/Library/PreferenceBundles/MeasureSettings.bundle/MeasureSettings](MACHOS/MeasureSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings](MACHOS/SOSSettings.md)
- [/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings](MACHOS/VoiceControlSettings.md)
- [/System/Library/PreferencesSyncBundles/CoreLocationSync.bundle/CoreLocationSync](MACHOS/CoreLocationSync.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDUserNotificationExtension.appex/ASDUserNotificationExtension](MACHOS/ASDUserNotificationExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension](MACHOS/AAUIFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/Support/avatarsd](MACHOS/avatarsd.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/XPCServices/MemojiImageRenderService.xpc/MemojiImageRenderService](MACHOS/MemojiImageRenderService.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/BooksService.xpc/BooksService](MACHOS/BooksService.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/PlugIns/CSFFollowUpExtension.appex/CSFFollowUpExtension](MACHOS/CSFFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/PlugIns/EventMetaDataExtractorPlugin.appex/EventMetaDataExtractorPlugin](MACHOS/EventMetaDataExtractorPlugin.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd](MACHOS/intelligenceflowd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService](MACHOS/NFUIService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ASConfigurationSubscriber.xpc/ASConfigurationSubscriber](MACHOS/ASConfigurationSubscriber.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/ScreenReader/BrailleDrivers/KGS Driver.brailledriver/KGS Driver](MACHOS/KGS_Driver.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileSMS.app/Extensions/MessagesActionExtension.appex/MessagesActionExtension](MACHOS/MessagesActionExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Photos.app/Photos](MACHOS/Photos.md)
- [/private/var/staged_system_apps/Photos.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates](MACHOS/PhotosNotificationsUpdates.md)
- [/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/aned](MACHOS/aned.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audiomxd](MACHOS/audiomxd.md)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/eventkitsyncd](MACHOS/eventkitsyncd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/pcsstatus](MACHOS/pcsstatus.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tvremoted](MACHOS/tvremoted.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/sbin/filecoordinationd](MACHOS/filecoordinationd.md)
- [/usr/sbin/otctl](MACHOS/otctl.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### agx_a000.bin

>  `agx_a000.bin`

```diff

   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1238
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x18a9
+  __TEXT.__const: 0x18aa
   __TEXT._rtk_patchbay: 0x208
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Nov 14 2024 22:51:17"
- "Nov  4 2024 00:51:55"

```

#### agx_a010.bin

>  `agx_a010.bin`

```diff

   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1238
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x18a9
+  __TEXT.__const: 0x18aa
   __TEXT._rtk_patchbay: 0x208
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Nov 14 2024 22:58:17"
- "Nov  4 2024 00:59:12"

```

#### agx_b000.bin

>  `agx_b000.bin`

```diff

   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1238
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x18a9
+  __TEXT.__const: 0x18aa
   __TEXT._rtk_patchbay: 0x208
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Nov 14 2024 22:55:33"
- "Nov  4 2024 00:56:25"

```

#### agx_b010.bin

>  `agx_b010.bin`

```diff

   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1238
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x18a9
+  __TEXT.__const: 0x18aa
   __TEXT._rtk_patchbay: 0x208
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Nov 14 2024 22:59:37"
- "Nov  4 2024 01:00:38"

```

#### agx_b100.bin

>  `agx_b100.bin`

```diff

   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1238
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x18a9
+  __TEXT.__const: 0x18aa
   __TEXT._rtk_patchbay: 0x208
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Nov 14 2024 22:56:57"
- "Nov  4 2024 00:57:49"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

-460.60.253.502.1
-  __TEXT.__text: 0x4c2284
+460.62.1.0.0
+  __TEXT.__text: 0x4c2324
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__cstring: 0x3090f
+  __TEXT.__cstring: 0x308ff
   __TEXT.__const: 0xe2768
   __TEXT.__swift5_typeref: 0xdee5
   __TEXT.__swift5_reflstr: 0x9235

   __TEXT.__term_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x3c
-  __TEXT.__eh_frame: 0x23ae4
+  __TEXT.__eh_frame: 0x23abc
   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x280
   __DATA.__mod_init_func: 0x38
CStrings:
+ "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "Invalid Log Data. "
- "/AppleInternal/Library/BuildRoots/38565290-993f-11ef-b290-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/38565290-993f-11ef-b290-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "OSLogServerComponent/RedactedLogServer.swift"

```

#### h17_ane_fw_theia_d9x.im4p

>  `h17_ane_fw_theia_d9x.im4p`

```diff

 
-  __TEXT.__text: 0xb8840
-  __TEXT.__const: 0x421c
-  __TEXT.__cstring: 0x1ad40
+  __TEXT.__text: 0x96388
+  __TEXT.__const: 0x4218
+  __TEXT.__cstring: 0x12c93
   __TEXT.ce_env: 0x4000
   __TEXT.__constructor: 0x0
   __TEXT.text_env: 0x20
-  __DATA.__const: 0x9be0
+  __DATA.__const: 0x9ba0
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xf70
+  __DATA.__data: 0xd70
   __DATA._rtk_power: 0x3b8
   __DATA._rtk_patchbay: 0x258
   __DATA._rtk_init_stack: 0x10000

   __DATA._rtk_mtab: 0x2a0
   __DATA.__gxf_data: 0x10
   __DATA.__mod_init_func: 0x0
-  __DATA.__zerofill: 0x55998
-  Functions: 1466
+  __DATA.__zerofill: 0x55948
+  Functions: 1351
   Symbols:   0
-  CStrings:  3288
+  CStrings:  2148
 
CStrings:
+ "%s .Sanity check failure!\n"
+ "00:29:07"
+ "Couldn't find ShareMemInfoItem to free !!!\n"
+ "IPC Endpoint cmd failed %d"
+ "IPC Endpoint cmd failure"
+ "Nov 11 2024"
+ "Procedure %d exceeded maximum for program %d"
+ "Run out of CSharedMemory !!!\n"
+ "pProc != __null"
+ "pProg != __null"
+ "unremap WriteMessage failed\n"
- "\tFW Latency Signposts 0x%x id 0x%x ts %lld"
- "\x1b[31m\"    Found Matched Priority Q[%d]S[%d] during Termination\"\x1b[39m"
- "\x1b[31m\"ABORT queue %d slot %d (nid %d) with multi segment\"\x1b[39m"
- "\x1b[31m\"Fail\"\x1b[39m"
- "\x1b[31m\"[ABORT] Suspend other TQs for TQ[%d]S[%d] at %lld\"\x1b[39m"
- "\x1b[31m\"[ABORT] TQ abort Q[%d] -> 1 slot at %lld\"\x1b[39m"
- "\x1b[31m\"[ABORT] TQ abort Q[%d] -> both slots, first slot is %d at %lld\"\x1b[39m"
- "\x1b[31m\"[StopTqInt] nid %d\"\x1b[39m"
- "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] bufferIndex %d is NOT matched with any buffer!"
- "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] bufferIndex %d is matched with buffers more than one!"
- "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] index %d should <= %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Generic ANE[%d] nbrOfNe %d exceeds H11 max NE %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Generic section (%lu) is smaller than actual (%lu)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Generic section buffer[%d] is not valid!"
- "\x1b[31m[VERIFICATION]\x1b[39m Generic section buffer[%d] is wrong type %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m KernelProp[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
- "\x1b[31m[VERIFICATION]\x1b[39m KernelProp[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation BAR setup number %d is exceed MAX_BAR_SLOTS %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation number %d exceeds MAX Operation number (%d)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation section (%lu) is smaller than actual (%lu)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] BAR setup is wrong!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] bar[%d] index %d exceeds H11 bar slots %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] nbrOfLocalbarSetup %d exceeds EAnsProgramBarMaxIndex %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] nbrOfNe %d exceeds H11 max NE %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] wrong opType %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Procedure[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
- "\x1b[31m[VERIFICATION]\x1b[39m Procedure[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
- "\x1b[31m[VERIFICATION]\x1b[39m SegmentProp section (%lu) is smaller than actual (%lu)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] Addr %p EON %d last TID %d with Liveouts 0x%x"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] Addr %p TID %d with 0 size"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] len %lld is smaller than ane_Network_Seg_Hdr_t (BranchEn %d)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] number of TD (%d) does not match value in prop (%d)"
- "\x1b[31m[VERIFICATION]\x1b[39m TD[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
- "\x1b[31m[VERIFICATION]\x1b[39m maxAneUsed %d :: H11 maxAneUsed should be %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d] is not valid!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] SHOULD not match with Kernel!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] SHOULD not match with segment!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] is matched more than one!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] is not matched with any of buffers!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d](%lld)=>Generic:buffer[%d](%lld). But wrong size!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d]=>Generic:buffer[%d]. But not valid!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall nbfOfbuffers %d (range 1 <= # <= 64)!"
- "\x1b[31m[VERIFICATION]\x1b[39m totalBufferNbr %d :: range should 0 < # < ECSneProgramMaxBuf (%d)!"
- "\x1b[32m\"Success\"\x1b[39m"
- "\x1b[33m\"Saving KMem from 0x%zx with 0x%zx\"\x1b[39m"
- "\x1b[33m\"Saving L2 from 0x%zx with 0x%zx\"\x1b[39m"
- "\x1b[33m\"Saving ane registers from 0x%zx with 0x%zx\"\x1b[39m"
- "\x1b[33m\"Start saving out after running into TD#%d from (%d-%d-%d)\"\x1b[39m"
- "\x1b[33m* PROGRAM :\x1b[39m"
- "\x1b[33m* TD :\x1b[39m"
- "\x1b[33m***** ANE RUN INFO ***** : program (0x%x)\x1b[39m"
- "\x1b[33m***** ANE TD INFO ***** : program (0x%x)\x1b[39m"
- "\x1b[33m************************\x1b[39m"
- "\x1b[34m* OPTIONS *\x1b[39m"
- "\x1b[34m***** ANE STATS *****\x1b[39m"
- "\x1b[34m***** PROCEDURE INFO *****\x1b[39m"
- "\x1b[34m***** PROCESS INFO *****\x1b[39m"
- "\x1b[34m***** PROGRAM INFO *****\x1b[39m"
- "\x1b[34m*********************\x1b[39m"
- "\x1b[34m************************\x1b[39m"
- "\x1b[34m**************************\x1b[39m"
- " "
- "          Bar[%d] : barIndex %d bufIndex %d"
- "     [%d] : Offset %lld length %lld"
- "     [%d] : Type %d nbrNe %d nbrOfLocalbarSetup %d"
- "     [%d] : Type %d startAddr 0x%x endAddr 0x%x Size %x nbrNe %d nbrOfLocalbarSetup %d"
- "     [%d] : format %d isCompressed 0x%x len 0x%llx offset %llx"
- "     aneMapping[%d] : %d"
- "     nBuf %d inputEvent %d priority %d uuid 0x%llx"
- "   %6u : [P:%d, %s] -- [T:%d, %s] -> ERROR: %s\n"
- "   %6u : [P:%d, %s] -- [T:%d, %s] -> [S:%d, %s]\n"
- "   %6u : [P:%d, %s] -- [T:%d] -> ERROR: WRONG EVENT\n"
- "  %s : There no state transitions\n"
- "  %s [%p]: Last %zu transitions [total = %zu]:\n"
- " %d : handle 0x%x offset 0x%lx len 0x%lx with Remap count %d\n"
- " %d : handle 0x%x offset 0x%lx len 0x%lx with map count %d\n"
- " %d [%#x]"
- " %p"
- " %s: event (%d, %s)"
- " %s: event (%d, %s), rc = %d [%#x]"
- " %s: event=%d [%s] cb %s"
- " Acquired %p"
- " Acquiring %p"
- " Released %p"
- " To release %p"
- "!(pageWiringOn && forceWiring)"
- "!bSubNetworkCustomExecuteOrder"
- "!commandBufPhysAddr"
- "!endPointCb[pCmd->endPointId].shareMem.item[i].used"
- "!pEntry->child"
- "!reader"
- "%-30s %-16.4f %-16lld %-16lld %-8lld\n"
- "%-30s %-16s %-16s %-16s %-8s\n"
- "%-30s %-6s %-8.4f %-8.4f\n"
- "%-30s %-6s %-8.4f %-8s %-10.4f %-16lld %-16lld %-8lld\n"
- "%-30s %-6s %-8s %-8.4f %-10.4f %-16lld %-16lld %-8lld\n"
- "%-30s %-6s %-8s %-8s %-10.4f %-16lld %-16lld %-8lld\n"
- "%-30s %-6s %-8s %-8s %-10s %-16s %-16s %-8s\n"
- "%d : buf %p size 0x%lx index 0x%x\n"
- "%lld delay trigger, %lld ignored due to exceeded execTimestamp"
- "%s : *** ACK: Endpoint command %d with ticket %u seq %u\n"
- "%s : *** endPoint %d cmd %d ack 0x%x ack_rc 0x%x ticket %u seq %u\n"
- "%s : Configure pCmd endPointId = %d\n"
- "%s : Free Shared Memory endPointId = %d at %p\n"
- "%s : Get EndPoint Status %d\n"
- "%s : Get Outstanding Ticket Cnt %d\n"
- "%s : Malloc Shared Memory endPointId = %d\n"
- "%s : SAP Register endPointId = %d sapId = 0x%x\n"
- "%s : SAP UnRegister endPointId = %d sapId = 0x%x\n"
- "%s : Send Buf endPointId %d sapId 0x%x %d\n"
- "%s : Unset pCmd endPointId = %d\n"
- "%s : valid %d bufIndex %d type %d addr 0x%llx memType %d size %lld tag %llx"
- "%s: (%d, %s): [%d, %s]->[%d, %s]"
- "%s: CH = %zu START"
- "%s: CH = %zu STOP"
- "%s: GOING TO STOP"
- "%s: SETUP"
- "%s: START"
- "%s: STOP"
- "%s: TEARDOWN"
- "(%s) %s\n"
- "(((size_t)(blockArray[dBlock])) % alignment[dBlock]) == 0"
- "((size_t)pointer) < ((size_t)(h->pMsg)) + h->queueDepth * sizeof(struct ffwInterProcMsg)"
- "((size_t)pointer) >= ((size_t)(h->pMsg))"
- "((uintptr_t)entry->stack & (RTK_CRT_STACK_ALIGNMENT - 1)) == 0"
- "(*parent == logDepth) || (*parent == index)"
- "(*parent == logDepth) || (*parent == pEntry->parent)"
- "(FFWMUTEX)0 != lock"
- "(IOP_RINGBUFFER_VERSION == (pBuf->_header._version>>16)) || (IOP_RINGBUFFER_VERSION_V2 == (pBuf->_header._version>>16))"
- "(SEMA)0 != cmd.syncCmdSema"
- "(callback == NULL) || (user_signal == 0)"
- "(ffwQueueCount (queue) == 0) || (((size_t) ffwQueueCount (queue)) == buffers)"
- "(idx >= 0) && (idx < (mNumEntriesPerPool * mMaxPoolNum))"
- "(idx >= 0) && (idx < hash_entries_num)"
- "(inputs > 0) || (outputs > 0)"
- "(mCurrPoolNum + pool_num) <= mMaxPoolNum"
- "(new_end & HEAP_OFFSET) == 0"
- "(operation == LOG_OPERATION_WIRED) || (operation == LOG_OPERATION_UNWIRED)"
- "(pCmd->pBufIndex[i] & ~maskRemapIndex) < sizeof(endPointCb[pCmd->endPointId].shareMem.remap)/sizeof(endPointCb[pCmd->endPointId].shareMem.remap[0])"
- "(pCmd->pBufIndex[i]) < sizeof(endPointCb[pCmd->endPointId].shareMem.item)/sizeof(endPointCb[pCmd->endPointId].shareMem.item[0])"
- "(size_t) ffwQueueCount (queue) == available"
- "(size_t)source < INTERRUPT_SRC_TOTAL"
- "(stacksize & (RTK_CRT_STACK_ALIGNMENT - 1)) == 0"
- "*extra_heap_size >= extra_heap_size_min"
- "*idx < CTASKPOOL_MAXTASK_HIST_ENTRIES"
- "*indexOut == logDepth"
- "*outsize <= maxOutsize"
- "*outsize >= sizeof(struct sCSneCmdPrintEnable)"
- "*print_buffer_base != 0"
- "*sm_base != 0"
- "*sm_size != 0"
- "-----------interval------------\n"
- "./ffw64_rtxc/ffw/CBuffer.cpp"
- "./ffw64_rtxc/ffw/CBufferPool.cpp"
- "./ffw64_rtxc/ffw/CBufferPoolStatic.cpp"
- "./ffw64_rtxc/ffw/CChannelManager.cpp"
- "./ffw64_rtxc/ffw/CController.cpp"
- "./ffw64_rtxc/ffw/CExpandablePool.cpp"
- "./ffw64_rtxc/ffw/CFifo.cpp"
- "./ffw64_rtxc/ffw/CFilter.cpp"
- "./ffw64_rtxc/ffw/CGPIOManager.cpp"
- "./ffw64_rtxc/ffw/CHashTable.cpp"
- "./ffw64_rtxc/ffw/CIPSynchro.cpp"
- "./ffw64_rtxc/ffw/CInterruptBuffer.cpp"
- "./ffw64_rtxc/ffw/CLatencyProfiler.cpp"
- "./ffw64_rtxc/ffw/CList.cpp"
- "./ffw64_rtxc/ffw/CLoggerInterProcessor.cpp"
- "./ffw64_rtxc/ffw/CLoggerSharedBuffer.cpp"
- "./ffw64_rtxc/ffw/CMMU.cpp"
- "./ffw64_rtxc/ffw/CMMULoggerPA.cpp"
- "./ffw64_rtxc/ffw/CMMULoggerVA.cpp"
- "./ffw64_rtxc/ffw/CMultiFilter.cpp"
- "./ffw64_rtxc/ffw/CObject.cpp"
- "./ffw64_rtxc/ffw/CObjectTree.cpp"
- "./ffw64_rtxc/ffw/CPipe.cpp"
- "./ffw64_rtxc/ffw/CPool.cpp"
- "./ffw64_rtxc/ffw/CRoot.cpp"
- "./ffw64_rtxc/ffw/CSharedMemory.cpp"
- "./ffw64_rtxc/ffw/CSignalPool.cpp"
- "./ffw64_rtxc/ffw/CTerminalOut.cpp"
- "./ffw64_rtxc/ffw/CTimeProfiler.cpp"
- "./ffw64_rtxc/ffw/ffwCRC.cpp"
- "./ffw64_rtxc/ffw/rtkit/CDebugAgent.cpp"
- "./ffw64_rtxc/ffw/rtkit/CEnvironment.cpp"
- "./ffw64_rtxc/ffw/rtkit/CISRManager.cpp"
- "./ffw64_rtxc/ffw/rtkit/CMailboxPool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CQueuePool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CRTOSObjectPool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CResourcePool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CScopedLock.cpp"
- "./ffw64_rtxc/ffw/rtkit/CSemaphorePool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CSharedMemoryHeap.cpp"
- "./ffw64_rtxc/ffw/rtkit/CSharedMemoryHost.cpp"
- "./ffw64_rtxc/ffw/rtkit/CTaskPool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CTimerManager.cpp"
- "./ffw64_rtxc/ffw/rtkit/CTimerPool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CTraceEventBuffer.cpp"
- "./ffw64_rtxc/ffw/rtkit/ffwSharedMemory.cpp"
- "./ffw64_rtxc/platform/common/CFakeChannel.cpp"
- "./ffw64_rtxc/platform/common/CIPSynchroFake.cpp"
- "./ffw64_rtxc/platform/common/ChannelTable.cpp"
- "./ffw64_rtxc/platform/common/FakeChannelTable.cpp"
- "./ffw64_rtxc/platform/theia/rtkit/CPlatformEnvironment.cpp"
- "./ffw64_rtxc/platform/theia/rtkit/CPlatformGPIOManager.cpp"
- "./ffw64_rtxc/platform/theia/rtkit/CPlatformISRManager.cpp"
- "./ffw64_rtxc/platform/theia/rtkit/RealChannelTableTarget.cpp"
- "./sne/drivers/CDeviceDriver.cpp"
- "./sne/drivers/FE/CConfigDrvH11.cpp"
- "./sne/ssi/src/rtxc/sema.cpp"
- "0 < mpGroupBufCnt[group]"
- "0 == ((size_t)virtualAddr & wiringPageMask)"
- "0 == (physicalAddr & wiringPageMask)"
- "0 == matched || 1 == matched"
- "0 == mpGroupBufCnt[group]"
- "0 == ret"
- "0/1"
- "1"
- "17:12:43"
- "<=== CMMU_LOGGER_FFW_ASSERT from %s\n"
- "===> CMMU_LOGGER_FFW_ASSERT from %s\n"
- ">>>>>>> Frame ID mismatch, expect: %lld, get: %lld"
- "ACK \"%s\""
- "ACTION"
- "AFPP load is not allowed after program setup done\n"
- "ALIGN_DOWN(pointer, CMMU::CacheLineSize()) == pointer"
- "ALL_CPU(%)"
- "ANE in secure mode, request dropped for cacheHandler 0x%llx"
- "ANE latency profiler already exists"
- "ANE latency profiler created"
- "ANE requestCallProc %zu"
- "ANE_PROPERTY_PRC Channel related logs are disabled"
- "ANE_PROPERTY_PRC Channel related logs are enabled"
- "ANE_PROPERTY_PRC wrong valid"
- "Aborted network finished execution before dummy finish event created"
- "AddScheduleInfo"
- "AneVersionGet"
- "AvailableScheduleInfo"
- "BAR[%d] barIndex %d : bufferIndex %d"
- "Buf MSG: sapId 0x%x bufNbr %d subPacketSize %d\n"
- "Buf[%d] sz %lld type %d"
- "BufferProcessor"
- "CAneDebugEventsManager"
- "CAneServer"
- "CBufferPool::alignment != 0"
- "CBufferPool::blockArray != 0"
- "CBufferPool::size != 0"
- "CBufferPool::stride != 0"
- "CDMEDIABUSMANAGER_ENDPOINT_CMD_PING == pCmd->hdr.cmd"
- "CDMEDIABUSMANAGER_ENDPOINT_CMD_REMAP == pCmd->hdr.cmd"
- "CDMEDIABUSMANAGER_ENDPOINT_CMD_SEND_BUF_MSG == pCmd->hdr.cmd"
- "CDMEDIABUSMANAGER_ENDPOINT_CMD_UNMAP == pCmd->hdr.cmd"
- "CDMediaBusManager"
- "CExpandablePool allocEntryIdx enter"
- "CExpandablePool allocEntryIdx exit idx %zu"
- "CExpandablePool expandPool enter expand pool num %d, mCurrPoolNum %d "
- "CExpandablePool expandPool exit mCurrPoolNum %d"
- "CExpandablePool freeEntryIdx enter idx %zu RefCount %d"
- "CExpandablePool freeEntryIdx exit idx %zu RefCount %d"
- "CExpandablePool freeEntryIdx free poolIdx %d, mCurrPoolNum %d"
- "CExpandablePool maximum pool num (%d) allowed already allocated"
- "CExpandablePool retain enter idx %zu RefCount %d"
- "CExpandablePool retain exit idx %zu RefCount %d"
- "CFakeChannel::chDescr"
- "CGPIOManager::Instance() != NULL"
- "CMMULoggerPA::hisEntry != 0"
- "CMMULoggerPA::logEntry != 0"
- "CMMULoggerVA::hisEntry != 0"
- "CMMULoggerVA::logEntry != 0"
- "CMMU_LOGGER_FFW_ASSERT:%d [%zu] PA = 0x%lx, length = 0x%zx\n"
- "CMMU_LOGGER_FFW_ASSERT:%d [%zu] vir = %p, length = 0x%zx\n"
- "CMailboxPool::Instance() != 0"
- "CPU num: %d\n"
- "CPU_0(%)"
- "CPU_1(%)"
- "CPU_ID"
- "CQueuePool::Instance() != 0"
- "CRPCClient is down"
- "CScopedLock"
- "CSemaphorePool::Instance() != 0"
- "CSharedMemory::Instance () != 0"
- "CTaskPool::Instance() != 0"
- "CTraceEventBuffer.cpp"
- "CWorkTaskCore"
- "CacheHandler (0x%llx) already removed from the list in the trigger ISR"
- "CallProcedure"
- "CallProcedure nbrOfCustomBars %d"
- "CallProcedure progId %d procId %d numIoBuffers %d"
- "CallProcedure progId %d procId %d numIoBuffers %d\n"
- "CallProcedure2"
- "ChannelCmd"
- "ChannelStarted"
- "ChannelStopped"
- "Cleanup complete. mpDataChainingStat at %p deallocated"
- "CmdAFPPLoad"
- "CmdAFPPUnload"
- "CmdAcknowledge"
- "CmdCpuLoadNotification"
- "CmdDataChainingEvent"
- "CmdDbgEvent"
- "CmdDsidEvent"
- "CmdErrorNotification"
- "CmdGetEndPointStatus"
- "CmdGetOutstandingTicketCnt"
- "CmdIpcEndpointSet"
- "CmdIpcEndpointUnset"
- "CmdIpcSharedMemoryFree"
- "CmdIpcSharedMemoryMalloc"
- "CmdPowerControl"
- "CmdProcessor"
- "CmdProgramEvent"
- "CmdProgramSetup"
- "CmdProgramUnsetup"
- "CmdPropertyAccess"
- "CmdRegSAP"
- "CmdResetNotification"
- "CmdSendBufMsg"
- "CmdUnRegSAP"
- "CpuLoadNotification"
- "Create"
- "Create,%lu,%s"
- "Data Chaining Latency for cacheReqIdx %d"
- "DataChainingProgramEvent"
- "DataProcessor"
- "DbgEvent"
- "Delete"
- "Delete,%lu,%s"
- "DeleteProgram"
- "DepriorDsid"
- "DirectPost"
- "DriverCmdSanityCheck : off"
- "DriverCmdSanityCheck : on"
- "DriverCmdSanityCheck TD/overflow : off"
- "DriverCmdSanityCheck TD/overflow : on"
- "Dummy network NID %d TD Complete event %lld"
- "Dummy network for NID %d TQ abort finished at %lld"
- "DumpAFPP"
- "EL"
- "END"
- "ENT: CFSM.cpp, "
- "ENT: CScopedLock.cpp, "
- "ENTER"
- "EVENT_DISP options:"
- "EXIT"
- "EXT: CFSM.cpp, "
- "EXT: CScopedLock.cpp, "
- "Enable TQs after Dummy network finish in TQ[%d]"
- "Enable TQs after letting TQ[%d] finish"
- "EndPoint %d sends the Ping Message\n"
- "EndPointUnset remap not by peer %d\n"
- "EndpointCmdPing"
- "EndpointCmdRemap"
- "EndpointCmdSendBufMsg"
- "EndpointCmdUnmap"
- "Event %d nbrUsrD %d 22"
- "EventProcess"
- "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgBuffRef)"
- "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgCmd)"
- "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgData)"
- "FFW_INTERPROC_BUFF_ACK_FLAG_CHECK(extra) != 0"
- "FFW_INTERPROC_BUFF_EXCHANGE_FLAG_CHECK(param2)"
- "FFW_OK == ffwrc"
- "FSMSwitchNonSecure"
- "FSMSwitchSecure"
- "FSM_EVENT_EXELOOP_IN_SECURE"
- "FSM_EVENT_EXELOOP_START"
- "FSM_EVENT_EXELOOP_STOP"
- "FSM_EVENT_EXELOOP_SWITCH_FROM_SECURE"
- "FSM_EVENT_EXELOOP_SWITCH_TO_SECURE"
- "FSM_STATE_EXELOOP_IDLE"
- "FSM_STATE_EXELOOP_PAUSE"
- "FSM_STATE_EXELOOP_RUN"
- "FSM_STATE_EXELOOP_RUN_2_PAUSE"
- "Failed to map command buffer"
- "FileInfo %s failed"
- "Filewrite %p %zu bytes"
- "Filewrite %s %s"
- "Force Disable already set"
- "Generic : [%d] bufferIndex %d"
- "GetCacheReqEvent"
- "GetCmdBuf"
- "GetDirectProcCallEvent"
- "GetLastCommittedTDInfo"
- "GetPowerStatus"
- "GetProcInfo"
- "GetProgInfo"
- "GetTraceBuffer"
- "H11ISPInterruptMapping[(size_t)aispSource]->platformIntSrc != PLATFORM_INT_INVALID"
- "H17TunableManager"
- "HandleEventInt"
- "HandleMcwInt"
- "HandleStopTqInt"
- "Help"
- "IDLE"
- "IDLE_DEFAULT"
- "ID_GET_SOURCE(id) < INTERRUPT_SRC_TOTAL"
- "INVALID"
- "IOP nothing to read"
- "IOP read done: rtPtr %d wtPtr %d readCount %d"
- "IOP read init: rtPtr %d wtPtr %d msgLen %zu"
- "IOP wait for Read"
- "IOP write done: rtPtr %d wtPtr %d writeCount %d"
- "IOP write init: rtPtr %d wtPtr %d msgLen %zu (with header)"
- "IOP write: Message length too big"
- "IOP write: buffer overflow"
- "IOP write: buffer wrapup"
- "IOP write: pBuffer not initialized yet"
- "IOP write: register 0x%zx 0x%x"
- "ISR_ID_GET_BANK(id) < lines"
- "ISR_ID_GET_INDEX(id) < ISR_CALLBACK_MAX"
- "ISR_ID_GET_LINE(id) < ISR_REG_ENTRY"
- "In SendSecureModeRequest()\n"
- "Info"
- "InitCacheRequest"
- "InitProcedureCallCmds"
- "InitProcedureCallCustomBarsCmds"
- "Initialization"
- "InqTaskArg"
- "Invalid log operation"
- "IpcEndpointSet"
- "IpcEndpointUnset"
- "ItqIrqEnable"
- "Kernel : bufferIndex %d"
- "KickStartCe"
- "Load %s failed"
- "LoadProgramsInAFPP"
- "LogEnterVerbose"
- "MapTextSection"
- "Master asking to release the remap while it is still being used by local user\n"
- "NO trace buffer to post!"
- "NULL != clockToMicroSecondConvertFunc"
- "NULL != encode_handler[encodeScheme]"
- "NULL != entry"
- "NULL != instance"
- "NULL != nbytes"
- "NULL != pCmd"
- "NULL != pIpcRingBufferIn[pCmd->endPointId]"
- "NULL != pIpcRingBufferOut[pCmd->endPointId]"
- "NULL != pMsg"
- "NULL != pResourceIndex[endPoint]"
- "NULL != pResourceIndex[pCmd->endPointId]"
- "NULL != pTaskHistoryHead"
- "NULL != physical_addr"
- "NULL != ppReadBufferAddr"
- "NULL != ppWriteBufferAddr"
- "NULL != semalist"
- "NULL != semaphore"
- "NULL != timeCodeGetFunc"
- "NULL != timestampFrequencyFunc"
- "NULL != virtualAddr"
- "NULL == instance"
- "NULL == mpGroups[group][j].buf && STATE_RELEASED == mpGroups[group][j].state"
- "NULL == pHandler"
- "NULL == pIpcRingBufferIn[pCmd->endPointId]"
- "NULL == pIpcRingBufferOut[pCmd->endPointId]"
- "Need dummy for TQ[%d]S[%d], b_queue_dummy_network %d"
- "No output buffers are ready for cache request with cacheHandler 0x%llx"
- "Notify score %u\n"
- "Nov  2 2024"
- "Overflow detected in dram event log: programId %d processId %d procedureId %d"
- "POST CONDITION: "
- "POWEROFF"
- "POWERON"
- "PRE CONDITION: "
- "PROCESSING"
- "ParseTD"
- "PerfMode : off"
- "PerfMode : on"
- "Performance"
- "Phase %d: %dus (avg %9.6fus, std sq %9.6fus statsCount %d)"
- "PiningThreadsTotal: "
- "PostCallback"
- "PostCmd"
- "PowerControl"
- "PowerDown"
- "PowerUp"
- "PowerUpByState"
- "PreMapProcessStatsBuf"
- "PrintBufDesc"
- "PrintDescriptorProp"
- "PrintGeneric"
- "PrintKernelProp"
- "PrintOperation"
- "PrintProcedure"
- "ProcessEndpointCmd"
- "ProcessSubPacket"
- "ProgramEvent"
- "PropertyWrite"
- "Queue dummy network using NID %d Q[%d]S[%d] at %lld"
- "RESET"
- "ROUND_DOWN(paddr, CMMU::CacheLineSize()) == paddr"
- "RPC Id is 0x%x\n"
- "RPC read file size as %zu"
- "RTK_ST_IS_SUCCESS(rc)"
- "RTK_queue_count(queue) == tot"
- "RTK_vm_unmap failed\n"
- "Read %s done %zu bytes"
- "ReadMessage"
- "Received Signal %p\n"
- "Received an program whose has 0 operation : %d"
- "Received an program whose procedure has invalid operation Index : %d vs %d"
- "RegisterClient"
- "ReloadTunables"
- "Remap :  handle 0x%x : base %p : len 0x%lx\n"
- "RemoveScheduleInfo"
- "Report Debug Event : Debug Event %d count %d (tid:%d)"
- "Reset"
- "ReturnCacheReqEvent"
- "ReturnDirectProcCallEvent"
- "RunProc"
- "RunProc2"
- "RunProcCacheRequest"
- "RunProcInternal"
- "START"
- "STOP"
- "STREAM"
- "STREAM_CMD_APPLY"
- "STREAM_CMD_APPLY_NOW"
- "STREAM_IDLE"
- "STREAM_IDLE_DEFAULT"
- "STREAM_INSTANDBY"
- "STREAM_OFF"
- "STREAM_PROCESSING"
- "STREAM_RESET"
- "STREAM_SETUP"
- "STREAM_STANDBY"
- "STREAM_START"
- "STREAM_STOP"
- "STREAM_TEARDOWN"
- "SUCC"
- "SVC"
- "SaveProcedureCall"
- "SaveRunToTdStop"
- "SaveStatsBuffer"
- "SaveToFile"
- "Segment : bufferIndex %d"
- "SendBufMsg"
- "SendCall"
- "SendHWRequest"
- "SendMsg : endPointId %d sapId 0x%x subPacket %p subPacketSize %d\n"
- "SendSecureModeRequest"
- "SetPMUBaseAddress"
- "SetProgram"
- "SetTQState"
- "Setting high watermark to %u\n"
- "Setting low watermark to %u\n"
- "Setting poll interval to %u seconds\n"
- "Setting threshold to %u ticks\n"
- "Setup complete. mpDataChainingStat at %p allocated"
- "SetupEngineRequest"
- "SetupExecute"
- "Started"
- "StatsBuf sz %lld type %d"
- "Stopped"
- "Suspend TQs for Dummy Network"
- "SwitchExclaveMode"
- "TD : bufferIndex %d"
- "TQ[%d] reqRunningStatus 0x%x"
- "Task"
- "TaskArg not found"
- "TearDownExecute"
- "TerminateCacheRequest"
- "TerminateProcess"
- "Thread time"
- "Total Abort : Raise Priority %d TQ Abort %d"
- "Total Process create/terminate : %d/%d"
- "Total Program add/delete       : %d/%d"
- "Total Scheduled Run : %d (failed %d)"
- "Total finished  Run : %d"
- "TracePost2Host"
- "TransitionProcess"
- "Trigger input dropped: src 0x%x Surface Id 0x%x Offset 0x%llx"
- "Trigger input fifo overflow. Dropped: src 0x%x Surface Id 0x%x Offset 0x%llx"
- "UnMapTextSection"
- "UnRemap :  handle 0x%x : base : %p len : 0x%lx\n"
- "UnsetMem : %p 0x%lx 0x%x\n"
- "UnsetRemap : %p 0x%lx 0x%x\n"
- "WriteMessage"
- "Writer regAddr 0x%lx regValue 0x%x\n"
- "[%d]: intermediate spill bar id %d, dsid 0x%llx"
- "[%d]: prefetch bar id %d, dsid 0x%llx"
- "[%s]  CMD = %#04x [%s] at %lld : type = 0x%x addr = %p, size = %d \n"
- "[%s] CMD = %#04x [%s] at %lld : enable=%d\n"
- "[%s] CMD = %#04x [%s] at %lld [0x%x]\n"
- "[0]: show options"
- "[1]: TD events sorted by TID"
- "[2]: TD events sorted by timestamp"
- "[3]: TD performance profiling"
- "[4]: show task switch event"
- "[5]: network performance profiling"
- "[ANE Exclave] Enter"
- "[ANE Exclave] Exit"
- "[ANE Power] down"
- "[ANE Power] up"
- "[AneCmd] Allocated processId %d for programId %d at %lld"
- "[AneCmd] Allocated programId = %d at %lld"
- "[AneCmd] Terminated processId %d for programId %d at %lld"
- "[AneCmd] Unloaded programId = %d at %lld"
- "[Desciptor prop Section] Total %d"
- "[Descriptor prop Section] X"
- "[Generic Section] X"
- "[Generic Section] maxAneUsed %d maxNe %d total Buf %d"
- "[Kernel Prop Section] Total %d"
- "[Kernel Prop Section] X"
- "[MessageBack] cmdId %d counter 0x%x - %dus (cache command # : %zu)"
- "[No] Generic Section"
- "[No] Operation Section"
- "[No] Procedure Section"
- "[No] Segment Prop Section"
- "[No] Segment Section"
- "[OPERATION Section] Total %d"
- "[OPERATION Section] X"
- "[POST] cmdId %d counter 0x%x"
- "[POST] cmdId %d counter 0x%x => Trace # %d"
- "[PROCEDURE Section] Total %d"
- "[PROCEDURE Section] X"
- "[TestCond] ASSERTION is set"
- "[TestCond] Cmd_Timeout is set"
- "[WRN] Exeloop cmd %d latency %dus"
- "[X] kernelPropSection is valid but no buffer!"
- "[X] kernelSection is valid but no buffer!"
- "[X] verifyBAR"
- "[X] verifyDescriptorPropSection"
- "[X] verifyDescriptors"
- "[X] verifyGenericSection"
- "[X] verifyKernelPropSection"
- "[X] verifyOperationSection"
- "[X] verifyProcedureSection"
- "[ipc] Send %llu"
- "[ipc] callProc Cb %llu"
- "[ipc] pCb %llu"
- "_AneCallBack"
- "_maskUnmaskMutex != (FFWMUTEX)0"
- "actionbuf.bin"
- "addDbgEvent"
- "addEntry"
- "addr != NULL"
- "alignment != 0"
- "allocDbgEventIdx"
- "allocEntryIdx"
- "allocL2SpillBufferIdx"
- "allocatedPoolAddr[i] != NULL"
- "array != 0"
- "arrayEmptyBuffer != 0"
- "array[index].ch != 0"
- "array[index].ch == 0"
- "array[index].inuse == false"
- "available == tot"
- "bGroupInUse[%d] %d"
- "b_found == false"
- "blockArray != 0"
- "blocks <= CBuffer::idTot"
- "bootArgs != 0"
- "buf %d: addr 0x%llx size %lld"
- "bufMsg->hdr.len <= sizeof(msg)"
- "bufNbr <= maxAneIpcBufMsg"
- "buffPointer"
- "buffPool != 0"
- "bufferLen == 0"
- "bufferLen > sizeof(sIOPRingBuffer_t)"
- "buffers != 0"
- "buffers <= FFW_INTERPROC_BUFF_TOT"
- "bundledBlocks <= CBuffer::idTot"
- "bundledBlocksIn <= CBuffer::idTot"
- "calcTriggerUsDelay"
- "ch != 0"
- "chMan != 0"
- "chManH2T != 0"
- "chTot <= ISP_CAMERA_CHANNEL_TOT"
- "channel < inchannels"
- "channelBufferSize != 0"
- "channelPhys != 0"
- "channelTotal != 0"
- "channel_mem != NULL"
- "checkBarEachAneOp"
- "checkpointId < mMaxCheckpoints"
- "cmdBuffer_mem != 0"
- "cmdDataCheck"
- "cmdInternalSema != (SEMA)0"
- "cmdMbox != (MBOX)0"
- "cmdMboxSema != (SEMA)0"
- "cmdSema != (SEMA)0"
- "cmdSynchronizationSema != (SEMA)0"
- "context != NULL"
- "count"
- "create writeRingBufferLen %d with writeRingBufferAddr at 0x%lx %d\n"
- "createCacheRequest"
- "curEntry"
- "dPrio != 0"
- "dPrio % 2 == 0"
- "dPrio <= 124"
- "dPrio <= RTK_THREAD_PRIORITY_MAX"
- "dPrio >= RTK_THREAD_PRIORITY_MIN"
- "dataBufSize == pBuf->_header._size"
- "dataChainingRecycleOutput"
- "dataChainingTrigger"
- "dataChainingTriggerIsr"
- "decPendingExeLoopCmdCnt"
- "deferredCmdAck == false"
- "delay trigger[%lld]: execTimestamp %lld cmdHandleTimestamp %lld"
- "deleteCacheRequest"
- "depriorDsid"
- "descr.indexList != 0"
- "descr.list != 0"
- "descr.lock != (FFWMUTEX)0"
- "dieRequest != (SEMA)0"
- "dieRequest != 0"
- "dieSema != (SEMA)0"
- "dispDataChainingLatency"
- "duty : %u %\n"
- "enableEventLogInNetworkDesc"
- "endPoint < maxEndpoint"
- "endPointCb[endPoint].shareMem.nbrOfRemapItem < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
- "endPointCb[i].curState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
- "endPointCb[pCmd->endPointId].curState != ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_IDLE"
- "endPointCb[pCmd->endPointId].curState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfItem"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfItem < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfItem == 0"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem == 0"
- "endPointCb[pCmd->endPointId].shareMem.remap[i].refCount==0"
- "endPointId < maxEndpoint"
- "entries != 0"
- "entries > 0"
- "entries_per_pool > 0"
- "entry != 0"
- "entry != NULL"
- "entry->callback || entry->callback_with_source"
- "entry->stack != 0"
- "entry->used == true"
- "entryList != 0"
- "entry_size > 0"
- "exe_interval(%)"
- "execution(us)"
- "expandPool"
- "extra_heap_virt != NULL"
- "ffwQueueCount (queue) == 0"
- "ffwrc == FFW_OK"
- "fileDescs[i].pData != nullptr"
- "fileDescs[i].size == fileDescs[i].sizeRef"
- "fileLen"
- "fileWrite"
- "filter == (class CObject *)0"
- "fiq(us)"
- "found"
- "freeEntryIdx"
- "freeL2SpillBuffIdx"
- "freeUnusedL2SpillBufferPool"
- "freeUnusedPool"
- "func != 0"
- "getActionProperty"
- "getCacheReqPendingCmdCnt"
- "getCacheReqState"
- "getCacheRequestInfo"
- "getCacheRequestIoBuffers"
- "getCacheRequestIoBuffersNbr"
- "getCacheRequestSignalEvents"
- "getDataChainingInputInfo"
- "getDirectAneRequestNetworkDesc"
- "getFileSize"
- "getL2SpillBufferAddr"
- "getNbrOfTd"
- "getProcedureCallType"
- "getRequestId"
- "gpTimerArray != 0"
- "gpTimerArray[0] != 0"
- "group < MAX_ASYNCBUFFERS_GROUPS"
- "h"
- "h != 0"
- "h->ch != 0"
- "h->chH2T != 0"
- "h->chT2H != 0"
- "h->managed == 0"
- "h->signature == CFSM_SIGNATURE"
- "h2tchIOMan != 0"
- "handle != 0"
- "handle != NULL"
- "handleAbortCacheRequest"
- "handleAbort_abortRaisePriority"
- "handleCallProcedureWithBar"
- "handleCmdChannel"
- "handleDelayedTriggerCmd"
- "handleInvalidSingleUseCacheRequest"
- "handleIpcEndpointCmd"
- "handlePendingCmd"
- "handler == memHandler"
- "handshake_info != NULL"
- "hashNodeIdxMutex != (FFWMUTEX)0"
- "hash_table_size > 0"
- "head == 0"
- "heap->addToPool(heapAddress, size) == RTK_ST_OK"
- "heapSize != 0"
- "heapVirt != NULL"
- "heap_resource != (FFWMUTEX)0"
- "heap_resource != 0"
- "i <= 1000"
- "id < max"
- "id >= 0 && id < CDMEDIABUSMANAGER_CMD_COMMON_TOT"
- "idx != 0"
- "inUseList == 0"
- "incPendingExeLoopCmdCnt"
- "index < entries"
- "index < tot"
- "index == pEntry->parent"
- "index >= 0"
- "indexOfGroup < MAX_ASYNCBUFFERS_IN_GROUP"
- "initDbgEventMem"
- "initSharedEvents"
- "inputPipe != 0"
- "inputPipeEnable != nullptr"
- "insize != CCONTROLLER_INVALID_SHARED_INSIZE"
- "insize == sizeof(struct sCSneCmdPrintEnable)"
- "instance != 0"
- "instance != NULL"
- "instance == 0"
- "instance == NULL"
- "instance == nullptr"
- "instance->ch != 0"
- "instance->chT2H != 0"
- "internalCmdListMutex_ != (FFWMUTEX)0"
- "interrupt(us)"
- "interruptTimerSignal != 0"
- "iobuf0.bin"
- "iobuf1.bin"
- "iobuf2.bin"
- "irqLine != 0"
- "isAneIdle"
- "isCacheReqInUse"
- "isCacheReqValid"
- "isHWReady"
- "isrHandle"
- "isrhandle != 0"
- "it"
- "list == 0"
- "loadMonitorTask != RTK_THREAD_NONE"
- "lock != (FFWMUTEX) 0"
- "lock != nullptr"
- "log != 0"
- "logCmdData"
- "logDepth > 0"
- "logEntry"
- "logRecvCmdAck"
- "logTot <= logDepth"
- "mLatencyStat.maxEntryNum > 0"
- "mLatencyStat.pCheckpoint"
- "mLatencyStat.pLatency"
- "mLatencyStat.pLatency[i]"
- "mMaxCheckpoints > 0"
- "mMutex != (RESOURCE)0"
- "mask cmd : address = 0x%x, actual address = 0x%x\n"
- "mask cmd : reg addr = 0x%x, data = 0x%x"
- "mask cmd : size = 0x%x\n"
- "maskCount[aispSource] > 0"
- "maxBuff != 0"
- "max_hash_entries > 0"
- "max_pool_num > 0 && max_pool_num <= MAX_EXPANDABLE_POOL_NUM"
- "maxchannels != 0"
- "maxmbox > 0"
- "maxqueue > 1"
- "maxres > 0"
- "maxsema > 0"
- "maxsig > 0"
- "maxtask > 1"
- "maxtimers > 0"
- "mboxPool != 0"
- "mboxPool == 0"
- "memory != 0"
- "message != NULL"
- "messages > 0"
- "mmu"
- "mmuLoggerOn == true"
- "mpEntryIdxRefCount"
- "mpEntryIdxRefCount[idx] == 0"
- "mpEntryIdxRefCount[idx] > 0"
- "mpGroupBufCnt[%d] %d"
- "mpGroupsOwnerName[%d] %s"
- "mpPoolInfo"
- "mpPoolInfo[mFirstUnusedPoolIdx].pIndexPool != NULL"
- "mpPoolInfo[mFirstUnusedPoolIdx].pPoolBaseAddr == NULL"
- "mpPoolInfo[poolIdx].pIndexPool != NULL"
- "mpPoolInfo[poolIdx].valid != 0"
- "msgHandler"
- "msgLen > 0"
- "msgPhys != 0"
- "mutex != (FFWMUTEX) NULL"
- "mutex != (RESOURCE) 0"
- "myDbg"
- "myProcCb"
- "nBytes != NULL"
- "name != 0"
- "napCount == 0"
- "nbrOfRemapLeft == endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem"
- "newState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
- "newTask != RTK_THREAD_NONE"
- "new_end > new_start"
- "newrdptr <= pBuf->_header._size"
- "object != 0"
- "object != NULL"
- "ok == true"
- "operationbuf.bin"
- "outputAddr && outputSize"
- "outputPipe != 0"
- "outsize != 0"
- "outstanding"
- "outstanding <= entries"
- "outstanding == 0"
- "owner != 0"
- "pAddr != NULL"
- "pAneLatencyProfiler != __null"
- "pBuf->_header._rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < pBuf->_header._wrptr"
- "pBuf->_header._rdptr + sizeof(sIOPRingBufferMsgHeader_t) < pBuf->_header._wrptr"
- "pBufAddr && pBufSize && pBufIndex"
- "pBufAddr[i] && pBufSize[i]"
- "pBuffMsg->buffers <= FFW_INTERPROC_BUFF_TOT"
- "pCmd != NULL"
- "pCmd->bufNbr <= maxAneIpcBufMsg"
- "pCmd->pSubPacket"
- "pCmd->sharedMemIndex < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
- "pData"
- "pEntry->parent != index"
- "pEntry->parent < logDepth"
- "pEntry->parent == index"
- "pEntry->physicalAddr"
- "pEntry->refCount"
- "pEntry->virtualAddr"
- "pExchange->buffers > 0"
- "pInternalCmdArray_"
- "pInternalCmdFreeList_"
- "pInternalCmdList_"
- "pItem->bufferRefCount"
- "pItem->pBase == pCmd->sharedMemPtr"
- "pItem->used"
- "pMMULogger != NULL"
- "pMMULogger == NULL"
- "pMsg"
- "pMsg != 0"
- "pMyMsg->id == FFW_INTERPROC_MSG_EXCHANGE"
- "pNodeData != NULL"
- "pPoolAddrToFree[i] != NULL"
- "pRingBuffer != 0"
- "pSize != 0"
- "pStride != 0"
- "pSubPacket != NULL"
- "pTemp"
- "pTemp + pCmd->pBufSize[i] <= (size_t)pItem->pBase + pItem->memSize"
- "pTemp >= (size_t)pItem->pBase && pTemp <= (size_t)pItem->pBase + pItem->memSize"
- "pUserStr != 0"
- "param1 >= sizeof(struct ffwInterProcMsg)"
- "parent < logDepth"
- "parent == logDepth"
- "parent == pEntry->parent"
- "parentEntry->child"
- "parentEntry->physicalAddr"
- "parentEntry->virtualAddr"
- "parseOperation"
- "parseProc"
- "physicalAddr"
- "physicalAddr != (uintptr_t) -1"
- "pin < buffPools"
- "pin < inputs"
- "pin < outputs"
- "pin < portInputs"
- "pointer"
- "pointer != 0"
- "pointer != NULL"
- "pointer == VP(messagePhys)"
- "pool != (void *)0"
- "pool != 0"
- "pool == ALIGN_DOWN(pool, CMMU::CacheLineSize())"
- "poolArray != 0"
- "poolArray[container->attach.id] == 0"
- "poolArray[id] != 0"
- "poolBufferReceived != 0"
- "poolBufferReturned != 0"
- "poolIdx < mMaxPoolNum"
- "poolIdx >= 0 && poolIdx < mMaxPoolNum"
- "poolsizeIn >= CBufferPoolStatic::PoolSizeGet(buffers, newbundledBlocks, newsize, newalignment)"
- "port < inports"
- "powerUpAne"
- "powerUpAneStage1"
- "powerUpAneStage2"
- "print"
- "printCommandInfo"
- "printInfo"
- "printStats"
- "priority != 0"
- "priority <= RTK_THREAD_PRIORITY_MAX"
- "priority >= RTK_THREAD_PRIORITY_MIN"
- "processCmdOnly == true"
- "processedCmdCounter == 0"
- "processorEnter"
- "processorExit"
- "prog.tdProp.buf %p procValid %d"
- "programId 0x%x processId 0x%x nbrAneMapping %d"
- "programId 0x%x processId 0x%x procedureId 0x%x"
- "propertyWrite"
- "propertywrite 0x10A5 \x1b[32m1\x1b[39m : ANE stats"
- "propertywrite 0x10A5 \x1b[32m2\x1b[39m : enable command detail"
- "propertywrite 0x10A5 \x1b[32m3\x1b[39m : disable command detail"
- "propertywrite 0x10A5 \x1b[32m4\x1b[39m : enable program info detail"
- "propertywrite 0x10A5 \x1b[32m5\x1b[39m : disable program info detail"
- "propertywrite 0x10A5 \x1b[32m6\x1b[39m : enable TD info detail"
- "propertywrite 0x10A5 \x1b[32m7\x1b[39m : disable TD info detail"
- "propertywrite 0x10A5 \x1b[32m8\x1b[39m : enable TD Header info"
- "propertywrite 0x10A5 \x1b[32m9\x1b[39m : disable TD Header info"
- "pushToHW"
- "pushToHWDirect"
- "queue != (FFWQUEUE)0"
- "queueDepth > 1"
- "queuePool != 0"
- "queuePool == 0"
- "rc != NULL"
- "rc == 1"
- "rc == RTK_ST_OK"
- "rc >= 0"
- "rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < localCopyWrPtr"
- "rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < pBuf->_header._size"
- "rdptr + sizeof(sIOPRingBufferMsgHeader_t) < localCopyWrPtr"
- "rdptr + sizeof(sIOPRingBufferMsgHeader_t) < pBuf->_header._size"
- "reader"
- "recycleArray != 0"
- "ref%d/%s"
- "relocation cmd : X = 0x%x\n"
- "relocation cmd : address = 0x%x, actual address = 0x%x\n"
- "relocation cmd : barIdx = 0x%x\n"
- "relocation cmd : dataHi = 0x%x"
- "relocation cmd : dataLo = 0x%x"
- "relocation cmd : size = 0x%x\n"
- "reportDataChainingTriggerFailed"
- "reportFinishEvent"
- "reportStats"
- "resPool != 0"
- "resPool == 0"
- "ret == 0"
- "retain"
- "retain == CBuffer::suspended"
- "retainL2SpillBufferIdx"
- "returnRequestId"
- "rtkitSystemTaskList != 0"
- "sCSneCmdProcedureCall [%d] : bufferIndex %d"
- "saveToFile"
- "sema != 0"
- "sema != NULL"
- "sema == 0"
- "semaArray != (SEMA *)0"
- "semaArray[index] != (SEMA)0"
- "semaPool != 0"
- "semaPool == 0"
- "semaphore == (SEMA)0"
- "semaphore == h->signalT2H"
- "sequential cmd : address = 0x%x, actual address = 0x%x\n"
- "sequential cmd : count = 0x%x\n"
- "sequential cmd : reg addr = 0x%x, data = 0x%x"
- "serialPollTimer[i] != 0"
- "serialPortPoolTimeOut[i] != (SEMA)0"
- "serialPortSignal[i] != (SEMA)0"
- "set buf[%d] 0x%llx zero sz %lld"
- "setAbortMode"
- "setAbortMode %d"
- "setCustomBars"
- "setDataChainingLatencyDisp"
- "setDataChainingLatencyDisp %d"
- "setDirectAneRequestInfo"
- "setEnableDynamicPowerGate"
- "setForceDisableCacheRequest"
- "setJobQueueId"
- "setPerfMode"
- "setResetMode"
- "setResetMode %d"
- "setStartTimestamp"
- "setTaskSwitchEventDisp"
- "setTaskSwitchEventDisp %d"
- "setupCacheRequest"
- "setupDirectProcCallEvents"
- "shAddr != NULL"
- "sharedEventsTrigger"
- "sharedEventsTriggerIsr"
- "sharedMem != 0"
- "shwdStatus == 0"
- "sigPool == 0"
- "signal != 0"
- "signalH2T != 0"
- "signalResetNotification"
- "signalSharedEvents"
- "signalT2H != 0"
- "size != 0"
- "size <= sizeof(pBuffMsg->extra)"
- "sizeInByte % 4 == 0"
- "sizeInByte > 0"
- "source < INT_NROF_VECTORS"
- "source < ISR_REG_ENTRY"
- "source < lines * ISR_REG_ENTRY"
- "source >= 0"
- "src != NULL"
- "stacksize != 0"
- "startInvalidateCacheRequestInExeLoop"
- "started == false"
- "statsBufferSizeGet"
- "status == FFW_OK"
- "status == RTK_ST_OK"
- "super::Available() == (int)super::Managed()"
- "switchToIsolatedMode"
- "syncCmdMutex_ != (FFWMUTEX)0"
- "synchronization != (SEMA)0"
- "synchronize != (SEMA)0"
- "task != (TASK)0"
- "task != 0"
- "taskId == self"
- "taskPool == 0"
- "taskTime != 0"
- "td size %zu while usedSize %d"
- "temp != 0"
- "this->buffers >= buffers"
- "threadHistoryLock != (FFWMUTEX) 0"
- "ticket < cmdDepth"
- "timerHandle != NULL"
- "timerSem != NULL"
- "token != 0"
- "tot != 0"
- "tot == 0"
- "tot > 0"
- "totalElapsed %lld or totalElapsedInterval %lld is invalid value\n"
- "totalElapsed(from tracekit) %lld, totalElapsedDuringCheckpoint %lld\n"
- "totalElapsedInterval(from tracekit) %lld, totalElapsedIntervalDuringCheckpoint %lld\n"
- "tree_resource != (FFWMUTEX)0"
- "tree_resource != 0"
- "unknown TD command type 0x%x"
- "updateAndEnqueueOneSegment"
- "updateDefSetting"
- "updateEngineRequestSegment"
- "updateStatsBufferData"
- "vPrintLock != (SEMA)0"
- "vPrintLock == (SEMA)NULL"
- "value != NULL"
- "verifyBAR"
- "verifyCustomBar"
- "verifyDescriptorPropSection"
- "verifyDescriptors"
- "verifyGenericSection"
- "verifyKernelPropSection"
- "verifyOperationSection"
- "verifyProcedure"
- "verifyProcedureSection"
- "verifyProgram"
- "virtualAddr"
- "virtualAddr != NULL"
- "waitTQIdle"
- "wiringPageSize == 0x4000"
- "write to overwrite ref%d/%s"
- "~CScopedLock"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.2 *(22C5131e)* | 620.1.15.10.3 |
| 18.2 *(22C5142a)* | 620.1.16.10.8 |

### Dylibs

#### ⬆️ Updated (562)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework](DYLIBS/PosterBoardFramework.md)
- [/System/Library/AccessibilityBundles/SiriSharedUI.axbundle/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SwiftUI.axbundle/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/AccessibilityBundles/WorkflowUIServices.axbundle/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin](DYLIBS/AAAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin](DYLIBS/AADataclassEnableNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AAIDMSAccountNotificationPlugin.bundle/AAIDMSAccountNotificationPlugin](DYLIBS/AAIDMSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SecureBackupNotification.bundle/SecureBackupNotification](DYLIBS/SecureBackupNotification.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accessibility.framework/Accessibility](DYLIBS/Accessibility.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/ColorSync.framework/ColorSync](DYLIBS/ColorSync.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PHASE.framework/PHASE](DYLIBS/PHASE.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib](DYLIBS/libWebKitSwift.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings](DYLIBS/MobilePhoneSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader](DYLIBS/AXAssetLoader.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI](DYLIBS/AccountsUI.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI](DYLIBS/ActivityAchievementsUI.md)
- [/System/Library/PrivateFrameworks/AirDropSettingsSupport.framework/AirDropSettingsSupport](DYLIBS/AirDropSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppIntentSchemas.framework/AppIntentSchemas](DYLIBS/AppIntentSchemas.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI](DYLIBS/AppProtectionUI.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation](DYLIBS/AppStoreFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport](DYLIBS/AppSupport.md)
- [/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI](DYLIBS/AppSystemSettingsUI.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine](DYLIBS/AppleNeuralEngine.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/AvatarPersistence](DYLIBS/AvatarPersistence.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP](DYLIBS/CVNLP.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation](DYLIBS/CalendarFoundation.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit](DYLIBS/ClassroomKit.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel](DYLIBS/ConfigurationEngineModel.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID](DYLIBS/CoreHID.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary](DYLIBS/DMCEnrollmentLibrary.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DefaultAppsSettingsUI.framework/DefaultAppsSettingsUI](DYLIBS/DefaultAppsSettingsUI.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/FMF.framework/FMF](DYLIBS/FMF.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking](DYLIBS/FMNetworking.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore](DYLIBS/FedStatsPluginCore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards](DYLIBS/FitnessAwards.md)
- [/System/Library/PrivateFrameworks/FitnessBrowsing.framework/FitnessBrowsing](DYLIBS/FitnessBrowsing.md)
- [/System/Library/PrivateFrameworks/FitnessCanvas.framework/FitnessCanvas](DYLIBS/FitnessCanvas.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI](DYLIBS/FitnessCoreUI.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessLibrary.framework/FitnessLibrary](DYLIBS/FitnessLibrary.md)
- [/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing](DYLIBS/FitnessMarketing.md)
- [/System/Library/PrivateFrameworks/FitnessSearch.framework/FitnessSearch](DYLIBS/FitnessSearch.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon](DYLIBS/HealthHearingDaemon.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI](DYLIBS/HearingModeSettingsUI.md)
- [/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI](DYLIBS/HearingModeUI.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMCorePipeline.framework/IMCorePipeline](DYLIBS/IMCorePipeline.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer](DYLIBS/IOMobileFramebuffer.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/InputToolKit.framework/InputToolKit](DYLIBS/InputToolKit.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MailWebProcessSupport.framework/MailWebProcessSupport](DYLIBS/MailWebProcessSupport.md)
- [/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin](DYLIBS/MatterPlugin.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore](DYLIBS/NanoPhotosCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit](DYLIBS/NeutrinoKit.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSiriUI.framework/NotesSiriUI](DYLIBS/NotesSiriUI.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/PromptKit.framework/PromptKit](DYLIBS/PromptKit.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/SentencePieceInternal.framework/SentencePieceInternal](DYLIBS/SentencePieceInternal.md)
- [/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert](DYLIBS/SessionAlert.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport](DYLIBS/SetupAssistantSupport.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/SharingHUD](DYLIBS/SharingHUD.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/SharingXPCServices.framework/SharingXPCServices](DYLIBS/SharingXPCServices.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution](DYLIBS/SiriAppResolution.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriLiminal.framework/SiriLiminal](DYLIBS/SiriLiminal.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices](DYLIBS/SpeechRecognitionCommandServices.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport](DYLIBS/SpotlightSettingsSupport.md)
- [/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared](DYLIBS/SpotlightUIShared.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze](DYLIBS/TeaBreeze.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences](DYLIBS/TelephonyPreferences.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextGenerationInference.framework/TextGenerationInference](DYLIBS/TextGenerationInference.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity](DYLIBS/UserActivity.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices](DYLIBS/UserNotificationsServices.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WatchQuickActionsServices.framework/WatchQuickActionsServices](DYLIBS/WatchQuickActionsServices.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)

</details>

### Feature Flags

#### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### TelephonyUtilities.plist

>  `Domain/TelephonyUtilities.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>9afd0505-c054-6ea2-7553-2da07a51aa9f</string>
 	</dict>
+	<key>DefaultCallingAppsGracefulFallback</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>DeviceExpertMigration</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### WritingTools.plist

>  `Domain/WritingTools.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>ff7b5dcd-7912-95de-a1cd-7d8c226da489</string>
 	</dict>
+	<key>HandlesKeyboardTracking_iOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+		<key>DisclosureRequired</key>
+		<string>ff7b5dcd-7912-95de-a1cd-7d8c226da489</string>
+	</dict>
 	<key>Montara</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### AuthKit.plist

>  `Domain/AuthKit.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>DeviceListCacheEnableDryMode</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>EasyDependentSignIn</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### CloudSubscriptionFeatures.plist

>  `Domain/CloudSubscriptionFeatures.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>imageGenerationBypass</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 </dict>
 </plist>
 

```

#### TVApp.plist

>  `Domain/TVApp.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>orloff</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>puiv</key>
 	<dict>
 		<key>Enabled</key>

```


</details>

## EOF
