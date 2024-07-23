# 18.0 (22A5307i) .vs 18.0 (22A5316j)

## IPSWs

- `iPhone16,2_18.0_22A5307i_Restore.ipsw`
- `iPhone16,2_18.0_22A5316j_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.0 *(22A5307i)* | 24.0.0 | 11215.0.132.502.2~1 | Wed, 03Jul2024 20:40:06 PDT |
| 18.0 *(22A5316j)* | 24.0.0 | 11215.0.165.502.1~2 | Mon, 15Jul2024 21:22:48 PDT |

### Kexts

#### ⬆️ Updated (38)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.kernel`

```diff

-11215.0.132.502.2
+11215.0.165.502.1
   __TEXT.__const: 0x33ba0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x6b9cd
-  __TEXT.__os_log: 0x26bed
+  __TEXT.__cstring: 0x6baf9
+  __TEXT.__os_log: 0x26e62
   __TEXT.__eh_frame: 0x5a0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c0

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7fb518
+  __TEXT_EXEC.__text: 0x7fd58c
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x23e8
+  __KLDDATA.__const: 0x2428
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x184e9
   __DATA.__lock_grp: 0x57a8
   __DATA.__percpu: 0x6e48
-  __DATA.__common: 0x584f8
-  __DATA.__bss: 0x3f7b0
+  __DATA.__common: 0x58508
+  __DATA.__bss: 0x3f7c0
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x10758
+  __BOOTDATA.__init_entry_set: 0x10770
   __BOOTDATA.__init: 0x5b058
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x453aa
+  __LINKINFO.__symbolsets: 0x4537a
   __LATE_CONST.__late_const: 0xa8
-  Functions: 19823
+  Functions: 19828
   Symbols:   0
-  CStrings:  16785
+  CStrings:  16807
 
CStrings:
+ "%s: %s from %s m 0x%llx data 0x%llx frame 0x%llx %s header length %lu"
+ "%s: %s: frame 0x%llx data 0x%llx len %ld"
+ "%s: %s: frame_header outside mbuf"
+ "%s: accepting RA from %s to %s on %s, local RA=%d\n"
+ "%s: dropping VLAN non-contiguous header %p, %p"
+ "%s: dropping short VLAN packet %d < %d"
+ "%s: m_copyup failed"
+ "%s: mbuf_copyback VLAN stripped header failed"
+ "%s: mbuf_copydata VLAN encap failed"
+ "%s: skipping RA from %s to %s on %s, accept RA: %d local RA=%d\n"
+ "%s:%d %u return NULL\n"
+ "%s:%d (%s, %s, %u) return NULL\n"
+ "%s:%d accept() SO_ACCEPTCONN %d: msleep"
+ "%s:%d accept() error %d: falloc"
+ "%s:%d accept() error %d: head->so_error"
+ "%s:%d accept() error %d: msleep"
+ "%s:%d accept() error %d: non-blocking  empty queue"
+ "%s:%d accept() error %d: soacceptfilter"
+ "Put frame header in separate mbuf"
+ "TXM [Error]: CodeSignature: selector: %u | 0x%02X | 0x%02X | %u\n"
+ "TXM [Error]: Errno: selector: %u | %d\n"
+ "TXM [Error]: TrustCache: selector: %u | 0x%02X | 0x%02X | %u\n"
+ "TXM [Error]: selector: %u | %u\n"
+ "Unable to start I/O reprioritization thread (%d) @%s:%d"
+ "bridge_check_frame_header"
+ "feth_output_common"
+ "flow_rx_agg_channel"
+ "flow_rx_agg_host"
+ "flow_rx_agg_tcp"
+ "separate_frame_header"
+ "vnode_waitformount"
- "%s %u return NULL\n"
- "%s: dropping short packet %d < %d"
- "%s: if_fake: Large mbuf fragment %d > %d"
- "%s: if_fake: copy_mbuf(): packet too large %d"
- "Could not create io_reprioritize_thread @%s:%d"
- "Fake interface output copies mbuf"
- "copy_mbuf"
- "output_copy"
- "uipc_rcvd DGRAM? @%s:%d"

```

>  `com.apple.driver.AppleAuthCP`

```diff

-157.0.0.0.0
+157.0.0.502.1
   __TEXT.__const: 0x4c
-  __TEXT.__cstring: 0x280a
+  __TEXT.__cstring: 0x2877
   __TEXT.__os_log: 0x12c7
-  __TEXT_EXEC.__text: 0x186e8
+  __TEXT_EXEC.__text: 0x18a1c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x218

   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x5840
   __DATA_CONST.__kalloc_type: 0x6c0
-  Functions: 470
+  Functions: 471
   Symbols:   0
-  CStrings:  404
+  CStrings:  407
 
CStrings:
+ "%s:%s _getDeviceIDSN() failed (status = 0x%x)\n"
+ "AppleAuthCPRelay::start: provider has no IDSN\n"
+ "_getDeviceIDSN"

```

>  `com.apple.driver.AppleFirmwareKit`

```diff

-531.0.7.0.0
-  __TEXT.__cstring: 0x4064
-  __TEXT.__os_log: 0x1129
+531.0.11.0.0
+  __TEXT.__cstring: 0x404f
+  __TEXT.__os_log: 0x1148
   __TEXT.__const: 0xa8
-  __TEXT_EXEC.__text: 0x3acdc
+  __TEXT_EXEC.__text: 0x3ae8c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3f8
   __DATA.__common: 0x700

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0xf0
   __DATA_CONST.__mod_term_func: 0xf0
-  __DATA_CONST.__const: 0xd318
+  __DATA_CONST.__const: 0xd348
   __DATA_CONST.__kalloc_type: 0x1880
   __DATA_CONST.__kalloc_var: 0x50
   Functions: 1931
   Symbols:   0
-  CStrings:  651
+  CStrings:  652
 
CStrings:
+ "%s(%s:%#llx): %s failed: 0x%x\n"
+ "1111111121211211112221111222122"
+ "createDescriptorGated"
- "\"availableSpace >= payload->size\" @%s:%d"
- "111111112122112111122211112221222"

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-3.28.1.0.0
-  __TEXT.__cstring: 0x190b9
-  __TEXT.__os_log: 0x153cb
-  __TEXT.__const: 0xa060
-  __TEXT_EXEC.__text: 0x95dfc
+3.33.50.0.0
+  __TEXT.__const: 0xa078
+  __TEXT.__cstring: 0x19332
+  __TEXT.__os_log: 0x1543b
+  __TEXT_EXEC.__text: 0x9b574
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a0
   __DATA.__common: 0x4a0
-  __DATA.__bss: 0x200
-  __DATA_CONST.__auth_got: 0x890
+  __DATA.__bss: 0x208
+  __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0xacb8
+  __DATA_CONST.__const: 0xad78
   __DATA_CONST.__kalloc_type: 0x1300
   __DATA_CONST.__kalloc_var: 0xd70
-  Functions: 1860
+  Functions: 1899
   Symbols:   0
-  CStrings:  3257
+  CStrings:  3273
 
CStrings:
+ "12122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212"
+ "AppleH16CamIn:%s - %s low memory mode - res:0x%08X\n"
+ "AppleH16CamIn:%s - %s low memory mode - res:0x%08X\n"
+ "AppleH16CamIn:%s - fEnableDisplayBrightnessUpdates = %d\n"
+ "AppleH16CamIn:%s - fEnableDisplayBrightnessUpdates = %d\n"
+ "AppleH16PearlCam:%s - Sending %u:%d (%s) error to client\n"
+ "Entering"
+ "Exiting"
+ "ISP_CPU_CORE0_PS On Time (ms)"
+ "ISP_CPU_CORE1_PS On Time (ms)"
+ "ISP_CPU_PS On Time (ms)"
+ "ISP_DPRX_PS On Time (ms)"
+ "ISP_FE_PS On Time (ms)"
+ "ISP_SECURE_PS On Time (ms)"
+ "ISP_STS0_PS On Time (ms)"
+ "ISP_STS1_PS On Time (ms)"
+ "ISP_SetLowMemoryMode_gated"
+ "camDisplayUpdates"
- "1212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212"
- "AppleH16PearlCam:%s - Sending %d (%s) error to client\n"

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-148.0.48.0.0
-  __TEXT.__cstring: 0x165cd
-  __TEXT.__const: 0x4ec98
-  __TEXT_EXEC.__text: 0xd6080
+148.0.50.0.0
+  __TEXT.__cstring: 0x165e9
+  __TEXT.__const: 0x4ecb8
+  __TEXT_EXEC.__text: 0xd6130
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1fe40
   __DATA.__common: 0x20a8
CStrings:
+ " Client closed with requests not notified! ( %d / %d)!"
+ "121111121222121211111111111221121121122122222"
+ "clientClose"
- "12111112122212121111111111121121121122122222"
- "IRQSTS is zeroes\n"
- "sampleInterruptStatus"

```

>  `com.apple.driver.DCPDPFamilyProxy`

```diff

-200.0.8.0.0
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x3ac
+200.0.10.0.0
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x410
   __TEXT.__os_log: 0x232
-  __TEXT_EXEC.__text: 0x4488
+  __TEXT_EXEC.__text: 0x4610
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
   __DATA_CONST.__const: 0x28c0
   __DATA_CONST.__kalloc_type: 0x180
-  Functions: 192
+  Functions: 193
   Symbols:   0
-  CStrings:  31
+  CStrings:  35
 
CStrings:
+ "color-accuracy-index"
+ "color-accuracy-index-key"
+ "coverglass-serial-number"
+ "coverglass-serial-number-key"

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-8.15.1.0.0
+8.16.1.0.0
   __TEXT.__os_log: 0x31029
   __TEXT.__cstring: 0xab3f
   __TEXT.__const: 0x600
-  __TEXT_EXEC.__text: 0xa0a78
+  __TEXT_EXEC.__text: 0xa0b20
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3058
   __DATA.__common: 0x3c8

```

>  `com.apple.driver.AppleMobileDispH16P-DCP`

```diff

-395.23.1.0.0
-  __TEXT.__cstring: 0x5565
+395.25.0.0.0
+  __TEXT.__cstring: 0x5658
   __TEXT.__const: 0x1a78
-  __TEXT_EXEC.__text: 0x2069c
+  __TEXT_EXEC.__text: 0x20970
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0xf0

   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x3e18
+  __DATA_CONST.__const: 0x3e40
   __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0xf0
-  Functions: 1108
+  Functions: 1109
   Symbols:   0
-  CStrings:  505
+  CStrings:  510
 
CStrings:
+ "%d\n"
+ "%s tearing down display wall in shutdown\n"
+ "%s: %s RT Bandwidth mailbox not found (error %d)\n"
+ "%s: %s all %u wall displays are identical: mfg: %s pid: 0x%x die: 0x%x maxPixClk: 0x%x dwnstrmType: %s\n"
+ "BICS_history_corrupt"
+ "Display Wall setup cannot be supported! Not "
+ "IOMFBSupportsRotation"
+ "IOMFBTestBacklightFastRamp"
+ "migrate_status"
+ "static IOReturn IOMobileFramebufferShim::shutdownNotificationShim(void *, void *, UInt32, IOService *, void *, vm_size_t)"
- " %u %d"
- "%s: %s RT Bandwidth mailbox not found\n"
- "%s: Display Wall setup cannot be supported!\n"
- "%s: NOT all %u wall displays are identical: mfg: %s pid: 0x%x\n"
- "All %u wall displays are identical: mfg: %s pid: 0x%x\n"

```

>  `com.apple.driver.usb.AppleUSBHostiOSDevice`

```diff

-1402.0.2.0.0
+1402.0.7.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x3ef
   __TEXT.__os_log: 0x2e0
-  __TEXT_EXEC.__text: 0x1964
+  __TEXT_EXEC.__text: 0x1958
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.0.50.0.0
+1827.0.52.0.0
   __TEXT.__cstring: 0x3ab6
   __TEXT.__const: 0x864
-  __TEXT_EXEC.__text: 0x3d4f4
+  __TEXT_EXEC.__text: 0x3d590
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x39c
   __DATA.__common: 0xe8

   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x3a68
+  __DATA_CONST.__const: 0x3a88
   __DATA_CONST.__kalloc_type: 0xd40
   __DATA_CONST.__kalloc_var: 0xa0
-  Functions: 671
+  Functions: 672
   Symbols:   0
   CStrings:  342
 
CStrings:
+ "1827.0.52"
+ "21:31:22"
+ "Jul 15 2024"
- "1827.0.50"
- "20:43:58"
- "Jul  3 2024"

```

>  `com.apple.driver.AppleSPU`

```diff

-1014.0.1.0.0
+1014.0.3.0.0
   __TEXT.__cstring: 0x5aae
-  __TEXT.__os_log: 0x85b
+  __TEXT.__os_log: 0x955
   __TEXT.__const: 0x358
-  __TEXT_EXEC.__text: 0x49668
+  __TEXT_EXEC.__text: 0x496e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7b8
   __DATA.__common: 0x970
-  __DATA.__bss: 0x590
+  __DATA.__bss: 0x5b0
   __DATA_CONST.__auth_got: 0x5e0
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__kalloc_var: 0x320
   Functions: 2065
   Symbols:   0
-  CStrings:  915
+  CStrings:  920
 
CStrings:
+ "Dropped gnss data report due to missing data queue %zu"
+ "Dropped gnss data report for queue error: %#x (%zu)"
+ "Dropped gnss event due to missing data queue %zu"
+ "Dropped gnss event due to oversized packet: %zu"
+ "Dropped gnss event for queue error: %#x (%zu)"

```

>  `com.apple.filesystems.apfs`

```diff

-2310.0.0.0.0
+2311.0.0.0.3
   __TEXT.__const: 0x790
-  __TEXT.__cstring: 0x48034
-  __TEXT_EXEC.__text: 0x1397d8
+  __TEXT.__cstring: 0x480ee
+  __TEXT_EXEC.__text: 0x139894
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x690
   __DATA.__bss: 0xc60

   __DATA_CONST.__const: 0x6058
   __DATA_CONST.__kalloc_type: 0x4c80
   __DATA_CONST.__kalloc_var: 0x2800
-  Functions: 2262
+  Functions: 2265
   Symbols:   0
-  CStrings:  6260
+  CStrings:  6263
 
CStrings:
+ "%s:%d: %s invalid object size: %d size_phys %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n"
+ "%s:%d: invalid object size: %d size_phys %d\n"
+ "2024/07/15"
+ "21:19:53"
+ "2311.0.0.0.3"
+ "Jul 15 2024"
+ "apfs-2311.0.0.0.3"
- "2024/07/03"
- "20:31:16"
- "2310"
- "Jul  3 2024"
- "apfs-2310"

```

>  `com.apple.driver.AppleIDV`

```diff

-7.36.1.0.0
+7.37.0.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x137d
+  __TEXT.__cstring: 0x137b
   __TEXT_EXEC.__text: 0x84b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
CStrings:
+ "7.37"
- "7.36.1"

```

>  `com.apple.driver.ApplePMGR`

```diff

-1555.0.17.0.0
+1555.0.22.0.0
   __TEXT.__const: 0x248
-  __TEXT.__cstring: 0xe858
-  __TEXT_EXEC.__text: 0x527f8
+  __TEXT.__cstring: 0xe8ef
+  __TEXT_EXEC.__text: 0x5299c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x100
   __DATA.__common: 0x420

   __DATA_CONST.__const: 0x7788
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0xe10
-  Functions: 2163
+  Functions: 2165
   Symbols:   0
-  CStrings:  1587
+  CStrings:  1590
 
CStrings:
+ "ApplePMGR:  perfCounterID = 0x%x activeTime = 0x%llx\n"
+ "_wakeTimeCounterCount <= kWakeTimeCounterMaxCount"
+ "virtual bool ApplePMGR::setWakeTimeFromSleep()"

```

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-733.0.5.0.0
+733.0.9.0.0
   __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x8861
+  __TEXT.__cstring: 0x887e
   __TEXT.__os_log: 0x3e3b
-  __TEXT_EXEC.__text: 0x36500
+  __TEXT_EXEC.__text: 0x36504
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
   __DATA.__common: 0x1d8
CStrings:
+ "!_secureStreamingCheckInProgress && (_brunorKeyUnwrappingState == kBrunorKeyUnwrappingStateNone)"
- "!_secureStreamingCheckInProgress && !_brunorKeyUnwrappingInProgress"

```

>  `com.apple.driver.AppleSARService`

```diff

-1172.0.0.0.0
+1175.0.0.0.0
   __TEXT.__const: 0x750
-  __TEXT.__cstring: 0x9b1f
+  __TEXT.__cstring: 0x9b40
   __TEXT.__os_log: 0xb8af
   __TEXT.__ustring: 0x8
-  __TEXT_EXEC.__text: 0x53e40
+  __TEXT_EXEC.__text: 0x53e78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x5f0

   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x60
-  __DATA_CONST.__const: 0x4d28
+  __DATA_CONST.__const: 0x4d58
   __DATA_CONST.__kalloc_type: 0x2940
   __DATA_CONST.__kalloc_var: 0x140
   Functions: 539
   Symbols:   0
-  CStrings:  1309
+  CStrings:  1310
 
CStrings:
+ "Rest Of World Region (0mm)"
+ "Rest Of World Region (5mm)"
- "Rest Of World Region"

```

>  `com.apple.driver.AppleSART`

```diff

-22.0.0.0.0
-  __TEXT.__cstring: 0xc94
-  __TEXT_EXEC.__text: 0x29e8
+23.0.0.0.0
+  __TEXT.__cstring: 0xcb3
+  __TEXT_EXEC.__text: 0x2ae0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1238
   __DATA_CONST.__kalloc_type: 0xc0
-  Functions: 114
+  Functions: 115
   Symbols:   0
-  CStrings:  66
+  CStrings:  67
 
CStrings:
+ "121111121222121212222222221121211112"
+ "_sartPowerRegisterMap != NULL"
+ "sart-power-reg-offset"
- "1211111212221212122222222211121211"
- "function-enable_autopm"

```

>  `com.apple.driver.AppleAVD`

```diff

-795.2.0.0.0
+796.1.0.0.0
   __TEXT.__const: 0x86e6e
-  __TEXT.__cstring: 0x5135
-  __TEXT.__os_log: 0x116ce
-  __TEXT_EXEC.__text: 0x40f34
+  __TEXT.__cstring: 0x5156
+  __TEXT.__os_log: 0x11944
+  __TEXT_EXEC.__text: 0x41274
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__kalloc_type: 0x2400
   Functions: 1339
   Symbols:   0
-  CStrings:  1410
+  CStrings:  1420
 
CStrings:
+ "1211111212221212111111111111111111111111222222222222222222222222222222222222222222222222222112212212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212121221222222222222222222212212222222222222222222222122222112122122222222222222222222211112112112112212222222222212212212222222222222222222222222222222222222222222222222222222222222222222221221221222222222222222222222222222222222222222222222222221111"
+ "AppleAVD: %s(): ERROR - invalid arguments! status 0x%x"
+ "AppleAVD: ERROR: %s(): Attempt to deallocate NULL kern_mem_info"
+ "AppleAVD: ERROR: %s(): NULL pAVDDart or invalid SID"
+ "AppleAVD: ERROR: %s(): addMemoryDescToGart failed."
+ "AppleAVD: ERROR: %s(): codecType=%u is invalid\n"
+ "AppleAVD: ERROR: %s(): deallocateKernelMemoryInternal failed"
+ "AppleAVD: ERROR: %s(): failed to grab PQ! hwDeviceType: %d"
+ "AppleAVD: ERROR: %s(): failed to grab WrapCtrl! hwDeviceType: %d"
+ "AppleAVD: ERROR: %s(): setMemoryDescriptor failed 0x%x"
+ "AppleAVD: ERROR: %s():%u: invalid command patcher!"
+ "AppleAVD: ERROR: :%u: too many reference frames [%u, %u]\n"
+ "DeallocKernelMem"
- "121111121222121211111111111111111111111122222222222222222222222222222222222222222222222222211221221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212121221222222222222222222212212222222222222222222222122222112122122222222222222222222211112112112112212222222222212212212222222222222222222222222222222222222222222222222222222222222222222221221221222222222222222222222222222222222222222222222222221111"
- "AppleAVD: %s(): ERROR: addMemoryDescToGart failed.\n"
- "AppleAVD: %s(): set memory descriptor ERROR 0x%x"

```

>  `com.apple.driver.AppleAVE2`

```diff

-802.61.1.0.0
-  __TEXT.__const: 0x2e8a0
-  __TEXT.__cstring: 0x34c2c
-  __TEXT.__os_log: 0x3f71f
-  __TEXT_EXEC.__text: 0x13e4b8
+802.88.0.0.0
+  __TEXT.__const: 0x2e8e0
+  __TEXT.__cstring: 0x34f37
+  __TEXT.__os_log: 0x3ffb1
+  __TEXT_EXEC.__text: 0x142160
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x290
   __DATA.__common: 0x130
-  __DATA.__bss: 0x560
+  __DATA.__bss: 0x568
   __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x62a8
-  __DATA_CONST.__kalloc_type: 0x1f40
+  __DATA_CONST.__const: 0x62c8
+  __DATA_CONST.__kalloc_type: 0x1fc0
   __DATA_CONST.__kalloc_var: 0x1090
-  Functions: 2431
+  Functions: 2472
   Symbols:   0
-  CStrings:  6884
+  CStrings:  6920
 
CStrings:
+ "%lld %d AVE %s: %s 0x%llx %d %d %d %d | %d"
+ "%lld %d AVE %s: %s 0x%llx %d %d %d %d | %d\n"
+ "%lld %d AVE %s: %s 0x%llx %d %d %d | %d"
+ "%lld %d AVE %s: %s 0x%llx %d %d %d | %d\n"
+ "%lld %d AVE %s: %s 0x%llx %d %d %d | %d | %d %d %d %d"
+ "%lld %d AVE %s: %s 0x%llx %d %d %d | %d | %d %d %d %d\n"
+ "%lld %d AVE %s: %s 0x%llx %d %d | %d"
+ "%lld %d AVE %s: %s 0x%llx %d %d | %d\n"
+ "%lld %d AVE %s: %s 0x%llx %d %d | %d | %d %d %d %d"
+ "%lld %d AVE %s: %s 0x%llx %d %d | %d | %d %d %d %d\n"
+ "%lld %d AVE %s: %s 0x%llx %d | %d"
+ "%lld %d AVE %s: %s 0x%llx %d | %d\n"
+ "%lld %d AVE %s: %s:%d %lld %d %d %d %d DS %p | RS %d %p | inter %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %lld %d %d %d %d DS %p | RS %d %p | inter %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | DPB LOW RES RC: pcaLRSResult[%d].IOSurfaceBuffer == NULL"
+ "%lld %d AVE %s: %s:%d %s | DPB LOW RES RC: pcaLRSResult[%d].IOSurfaceBuffer == NULL\n"
+ "%lld %d AVE %s: %s:%d %s | DPB LOW RES: pcaLFSResult[%d].IOSurfaceBuffer == NULL"
+ "%lld %d AVE %s: %s:%d %s | DPB LOW RES: pcaLFSResult[%d].IOSurfaceBuffer == NULL\n"
+ "%lld %d AVE %s: %s:%d %s | DPB pcaLFSRef[%d] == NUL"
+ "%lld %d AVE %s: %s:%d %s | DPB pcaLFSRef[%d] == NUL\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create LFSRef Surface Pool %p %d"
+ "%lld %d AVE %s: %s:%d %s | fail to create LFSRef Surface Pool %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create LFSResult Surface Pool %p %d"
+ "%lld %d AVE %s: %s:%d %s | fail to create LFSResult Surface Pool %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create LRSResult Surface Pool %p %d"
+ "%lld %d AVE %s: %s:%d %s | fail to create LRSResult Surface Pool %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize LFSRef Surface Pool %p %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize LFSRef Surface Pool %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize LFSResult Surface Pool %p %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize LFSResult Surface Pool %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize LRSResult Surface Pool %p %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize LRSResult Surface Pool %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed in preparation %p %d %p %d | %p %p %p %d %d | %p %p %p %p %p %p %p %p %p"
+ "%lld %d AVE %s: %s:%d %s | failed in preparation %p %d %p %d | %p %p %p %d %d | %p %p %p %p %p %p %p %p %p\n"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s 0x%llx %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s x%llx %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s x%llx %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s x%llx %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s x%llx %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to acquire EUs %p %d %p %d %p %p %d"
+ "%lld %d AVE %s: %s:%d %s | failed to acquire EUs %p %d %p %d %p %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to allocate GOP decision %d"
+ "%lld %d AVE %s: %s:%d %s | failed to allocate GOP decision %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s 0x%llx %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s 0x%llx %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s 0x%llx %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s 0x%llx %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s 0x%llx %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s 0x%llx %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface header %s 0x%llx %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface header %s 0x%llx %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | firmware buffer chroma header is invalid %d"
+ "%lld %d AVE %s: %s:%d %s | firmware buffer chroma header is invalid %d\n"
+ "%lld %d AVE %s: %s:%d %s | firmware buffer chroma header is invalid %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | firmware buffer chroma header is invalid %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %d"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %p %d %d %p"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %p %d %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %p %lld %p"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %p %lld %p\n"
+ "%lld %d AVE %s: %s::%s Enter %p %p %d %d %d"
+ "%lld %d AVE %s: %s::%s Enter %p %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s Enter %p 0x%llx"
+ "%lld %d AVE %s: %s::%s Enter %p 0x%llx\n"
+ "%lld %d AVE %s: %s::%s Exit %p %p %d %d %d %d"
+ "%lld %d AVE %s: %s::%s Exit %p %p %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s Exit %p 0x%llx %d"
+ "%lld %d AVE %s: %s::%s Exit %p 0x%llx %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaLFSResult[%d][%d][%d] == NULL"
+ "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaLFSResult[%d][%d][%d] == NULL\n"
+ "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaLRSResult[%d][%d][%d] == NULL"
+ "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaLRSResult[%d][%d][%d] == NULL\n"
+ "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaRecon[0][0][%d]==%p, pcaLFSRef[%d]==%p"
+ "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaRecon[0][0][%d]==%p, pcaLFSRef[%d]==%p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | faild to prepare memory"
+ "%lld %d AVE %s: %s::%s:%d %s | faild to prepare memory\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to DART map external surfaces %p %llu %p %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to DART map external surfaces %p %llu %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to DART map internal surfaces %p %llu %p %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to DART map internal surfaces %p %llu %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create DLB %p %p %p %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create DLB %p %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to initialize sDLB %p %p %p %p %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to initialize sDLB %p %p %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to set Pipe power and its dependency %p %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to set Pipe power and its dependency %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameters %p %p %p"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameters %p %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d DLBEntry %p %d transition is done"
+ "%lld %d AVE %s: %s::%s:%d DLBEntry %p %d transition is done\n"
+ "%lld %d AVE %s: %s::%s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | [ %s ]"
+ "%lld %d AVE %s: %s::%s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | [ %s ]\n"
+ "%lld %d AVE %s: %s::%s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | { %s }"
+ "%lld %d AVE %s: %s::%s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | { %s }\n"
+ "%lld %d AVE %s: %s::%s:%d EUMap %p %d | < %s >"
+ "%lld %d AVE %s: %s::%s:%d EUMap %p %d | < %s >\n"
+ "%lld %d AVE %s: %s::%s:%d EUMap %p %d | [ %s ]"
+ "%lld %d AVE %s: %s::%s:%d EUMap %p %d | [ %s ]\n"
+ "%lld %d AVE %s: %s::%s:%d EUStats %d | %s"
+ "%lld %d AVE %s: %s::%s:%d EUStats %d | %s\n"
+ "%lld %d AVE %s: %s::%s:%d Frame[%d] Stats: enc %d dis %d | %d %d %d type %s qp %d | inter %d intra %d | %d | %d %d | %d %d | %d"
+ "%lld %d AVE %s: %s::%s:%d Frame[%d] Stats: enc %d dis %d | %d %d %d type %s qp %d | inter %d intra %d | %d | %d %d | %d %d | %d\n"
+ "%lld %d AVE %s: %s::%s:%d LRME RS Result buffer not ready %p %d %p %d"
+ "%lld %d AVE %s: %s::%s:%d LRME RS Result buffer not ready %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d [%d] %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d [%d] %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d [%d] %p %d | %d 0x%x %d | %d -> %d | %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d [%d] %p %d | %d 0x%x %d | %d -> %d | %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d find %p %d %d %p %d | %p %lld %p %d | %d %d %d %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d find %p %d %d %p %d | %p %lld %p %d | %d %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d invalid EUMap %p %d | [ %s ]"
+ "%lld %d AVE %s: %s::%s:%d invalid EUMap %p %d | [ %s ]\n"
+ "%lld %d AVE %s: AVE_ClientDie %p %d %p"
+ "%lld %d AVE %s: AVE_ClientDie %p %d %p\n"
+ "%lld %d AVE %s: CHM Number: %d"
+ "%lld %d AVE %s: CHM Number: %d\n"
+ "%lld %d AVE %s: Client%s total number of commands %p %d %s | %d %d"
+ "%lld %d AVE %s: Client%s total number of commands %p %d %s | %d %d\n"
+ "%lld %d AVE %s: Client%s: %p ID: %d Resolution: %dx%d Realtime: %d Priority: %d DLB: %d %d"
+ "%lld %d AVE %s: Client%s: %p ID: %d Resolution: %dx%d Realtime: %d Priority: %d DLB: %d %d\n"
+ "%lld %d AVE %s: DLB %s | %p | %p %p"
+ "%lld %d AVE %s: DLB %s | %p | %p %p\n"
+ "%lld %d AVE %s: DLB %s | %p | %s"
+ "%lld %d AVE %s: DLB %s | %p | %s\n"
+ "%lld %d AVE %s: DLB Unit: %d - %d %d %d %s"
+ "%lld %d AVE %s: DLB Unit: %d - %d %d %d %s\n"
+ "%lld %d AVE %s: DLB: %d %d"
+ "%lld %d AVE %s: DLB: %d %d\n"
+ "%lld %d AVE %s: DLBInfo %s | %p %d %d"
+ "%lld %d AVE %s: DLBInfo %s | %p %d %d\n"
+ "%lld %d AVE %s: Index        Time         EUID   Command        -        Position Count     - Order  Result Client             ID    Type CodecType Priority  FrameNum  SliceIdx FrameType "
+ "%lld %d AVE %s: Index        Time         EUID   Command        -        Position Count     - Order  Result Client             ID    Type CodecType Priority  FrameNum  SliceIdx FrameType \n"
+ "%lld %d AVE %s: MD%s total number of commands %p %lld %d %d | %d %d"
+ "%lld %d AVE %s: MD%s total number of commands %p %lld %d %d | %d %d\n"
+ "%lld %d AVE %s: Surface info: "
+ "%lld %d AVE %s: Surface info: \n"
+ "%s 0x%llx %d %d %d %d | %d"
+ "%s 0x%llx %d %d %d %d | %d\n"
+ "%s 0x%llx %d %d %d | %d"
+ "%s 0x%llx %d %d %d | %d\n"
+ "%s 0x%llx %d %d %d | %d | %d %d %d %d"
+ "%s 0x%llx %d %d %d | %d | %d %d %d %d\n"
+ "%s 0x%llx %d %d | %d"
+ "%s 0x%llx %d %d | %d\n"
+ "%s 0x%llx %d %d | %d | %d %d %d %d"
+ "%s 0x%llx %d %d | %d | %d %d %d %d\n"
+ "%s 0x%llx %d | %d"
+ "%s 0x%llx %d | %d\n"
+ "%s::%s"
+ "1111111221112"
+ "111222121112222222222122122122122212212222222221122222221122222221122222221122222221122222221122222221122222221122222221122222221122222221122222221122222221122222221122222221122222221122222221111"
+ "112222222222222222222222222222222222222222222222222222222222222222222111111112222222222222222222222222222222211111111"
+ "12111111111112222112222211111111111111111111111121222221"
+ "1222122222211121111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
+ "21:30:14"
+ "2222222222211"
+ "802.88.0"
+ "AVE_DLB"
+ "AVE_IntraPred"
+ "AVE_Work_MSC_PostUpdate"
+ "Acquire"
+ "AllocEUNum"
+ "AllocUnit"
+ "ApplyDynamic"
+ "ApplyStatic"
+ "AssignUnit"
+ "AssignUnitPreempt"
+ "CHM Number: %d"
+ "CHM Number: %d\n"
+ "CalcPerfNum"
+ "CalcPerfNumPerEU"
+ "Clean"
+ "CleanUnit"
+ "Client%s total number of commands %p %d %s | %d %d"
+ "Client%s total number of commands %p %d %s | %d %d\n"
+ "Client%s: %p ID: %d Resolution: %dx%d Realtime: %d Priority: %d DLB: %d %d"
+ "Client%s: %p ID: %d Resolution: %dx%d Realtime: %d Priority: %d DLB: %d %d\n"
+ "DLB %s | %p | %p %p"
+ "DLB %s | %p | %p %p\n"
+ "DLB %s | %p | %s"
+ "DLB %s | %p | %s\n"
+ "DLB Unit: %d - %d %d %d %s"
+ "DLB Unit: %d - %d %d %d %s\n"
+ "DLB: %d %d"
+ "DLB: %d %d\n"
+ "DLBInfo %s | %p %d %d"
+ "DLBInfo %s | %p %d %d\n"
+ "Index        Time         EUID   Command        -        Position Count     - Order  Result Client             ID    Type CodecType Priority  FrameNum  SliceIdx FrameType "
+ "Index        Time         EUID   Command        -        Position Count     - Order  Result Client             ID    Type CodecType Priority  FrameNum  SliceIdx FrameType \n"
+ "Jul 15 2024"
+ "Keep"
+ "LFSRef"
+ "LFSRefChroma"
+ "LFSRefChromaHeader"
+ "LFSRefLumaHeader"
+ "LFSResult"
+ "LRSNeighborMV"
+ "LRSResult"
+ "MD%s total number of commands %p %lld %d %d | %d %d"
+ "MD%s total number of commands %p %lld %d %d | %d %d\n"
+ "Remap"
+ "RetrieveEUID"
+ "SelectUnit"
+ "Surface info: "
+ "Surface info: \n"
+ "Switch"
+ "[%d %d - %d] "
+ "[%d 0x%llx] "
+ "m_pcDLB != nullptr"
+ "m_psDLB->iSchedMode == 0"
+ "num == 0 || num >= psSInfoSet->sRecon.iaData[AVE_SIIdx_Set]"
+ "pCfg != nullptr && pDevInfo != nullptr"
+ "pClient->pcaSurfacePool[AVE_SurPoolIdx_LFSRef] != nullptr"
+ "pClient->pcaSurfacePool[AVE_SurPoolIdx_LFSResult] != nullptr"
+ "pClient->pcaSurfacePool[AVE_SurPoolIdx_LRSResult] != nullptr"
+ "pIDFlag != nullptr"
+ "pInfo->sExtraBuff.CavlcHeader[i] != 0"
+ "pInfo->sRef.Low_Res_UV_L0[AVE_REFERENCE_A] != 0"
+ "pInfo->sRef.Low_Res_UV_L0[AVE_REFERENCE_B] != 0"
+ "pInfo->sRef.Low_Res_UV_L0_Hdr[AVE_REFERENCE_A] != 0"
+ "pInfo->sRef.Low_Res_UV_L0_Hdr[AVE_REFERENCE_B] != 0"
+ "pInfo->sRef.Low_Res_UV_L1[AVE_REFERENCE_A] != 0"
+ "pInfo->sRef.Low_Res_UV_L1_Hdr[AVE_REFERENCE_A] != 0"
+ "pInfo->sRef.Low_Res_Y_L0_Hdr[AVE_REFERENCE_A] != 0"
+ "pInfo->sRef.Low_Res_Y_L0_Hdr[AVE_REFERENCE_B] != 0"
+ "pInfo->sRef.Low_Res_Y_L1_Hdr[AVE_REFERENCE_A] != 0"
+ "pMgr != nullptr && pSIDSet != nullptr && pSInfoSet != nullptr && pSet != nullptr"
+ "pMgr != nullptr && pSet != nullptr && pSInfoSet != nullptr"
+ "pMgr != nullptr && psTask != nullptr && pSInfoSet != nullptr && pSInfoSet != nullptr && pSet != nullptr"
+ "pSet->pcaRecon[i][j][k]->GetSize() >= psSInfoSet->sRecon.iaData[AVE_SIIdx_Size]"
+ "pVP->p_apsEntropyCodingHeader[0] != 0"
+ "pVP->p_apsEntropyCodingHeader[i] != 0"
+ "pVP->p_apsLowResChromaHeader[j][k] != 0"
+ "pVP->p_apsLowResChroma[j][k] != 0"
+ "pVP->p_apsLowResHeader[j][k] != 0"
+ "pVP->p_apsMCTFHmeRcNbrMv != 0"
+ "pVP->p_apsMCTFLowResChromaHdr[k] != 0"
+ "pVP->p_apsMCTFLowResChroma[k] != 0"
+ "pVP->p_apsMCTFLowResHdr[k] != 0"
+ "pcaLFSRef[k] != nullptr"
+ "pcaLFSResult[i + iRefNum][0] [iLRMEResultBufSetIdx] != nullptr"
+ "pcaLFSResult[k] != nullptr"
+ "pcaLRSResult[k] != nullptr"
+ "pcaRecon != nullptr && pcaLFSRef != nullptr && pcaLFSResult != nullptr && pcaLRSResult != nullptr"
+ "site.AVE_DLB"
+ "tmpLayer == 0 || tmpLayer >= psSInfoSet->sRecon.iaData[AVE_SIIdx_Layer]"
+ "tmpNum == 0 || tmpNum >= psSInfoSet->sRecon.iaData[AVE_SIIdx_Num]"
+ "vps_vui"
- "%lld %d AVE %s: %s %d %d %d %d | %d"
- "%lld %d AVE %s: %s %d %d %d %d | %d\n"
- "%lld %d AVE %s: %s %d %d %d | %d"
- "%lld %d AVE %s: %s %d %d %d | %d\n"
- "%lld %d AVE %s: %s %d %d %d | %d | %d %d %d %d"
- "%lld %d AVE %s: %s %d %d %d | %d | %d %d %d %d\n"
- "%lld %d AVE %s: %s %d %d | %d"
- "%lld %d AVE %s: %s %d %d | %d\n"
- "%lld %d AVE %s: %s %d %d | %d | %d %d %d %d"
- "%lld %d AVE %s: %s %d %d | %d | %d %d %d %d\n"
- "%lld %d AVE %s: %s %d | %d"
- "%lld %d AVE %s: %s %d | %d\n"
- "%lld %d AVE %s: %s Enter %d %d %d %d %d %d %d %p"
- "%lld %d AVE %s: %s Enter %d %d %d %d %d %d %d %p\n"
- "%lld %d AVE %s: %s Enter %d %d %d %p"
- "%lld %d AVE %s: %s Enter %d %d %d %p\n"
- "%lld %d AVE %s: %s Enter %p %p %d %d %d"
- "%lld %d AVE %s: %s Enter %p %p %d %d %d\n"
- "%lld %d AVE %s: %s Exit %d %d %d %d %d %d %d %p %d"
- "%lld %d AVE %s: %s Exit %d %d %d %d %d %d %d %p %d\n"
- "%lld %d AVE %s: %s Exit %d %d %d %p %d"
- "%lld %d AVE %s: %s Exit %d %d %d %p %d\n"
- "%lld %d AVE %s: %s Exit %p %p %d %d %d %d"
- "%lld %d AVE %s: %s Exit %p %p %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %lld %d %d %d %d DS %p | RC %d %p | inter %d %d %d %d"
- "%lld %d AVE %s: %s:%d %lld %d %d %d %d DS %p | RC %d %p | inter %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | DPB LOW RES RC: pcaLowResRCResult[%d].IOSurfaceBuffer == NULL"
- "%lld %d AVE %s: %s:%d %s | DPB LOW RES RC: pcaLowResRCResult[%d].IOSurfaceBuffer == NULL\n"
- "%lld %d AVE %s: %s:%d %s | DPB LOW RES: pcaLowResResult[%d].IOSurfaceBuffer == NULL"
- "%lld %d AVE %s: %s:%d %s | DPB LOW RES: pcaLowResResult[%d].IOSurfaceBuffer == NULL\n"
- "%lld %d AVE %s: %s:%d %s | DPB pcaLowResRef[%d] == NUL"
- "%lld %d AVE %s: %s:%d %s | DPB pcaLowResRef[%d] == NUL\n"
- "%lld %d AVE %s: %s:%d %s | fail to initial LowResRCResult Surface Pool %p %d"
- "%lld %d AVE %s: %s:%d %s | fail to initial LowResRCResult Surface Pool %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to initial LowResRef Surface Pool %p %d"
- "%lld %d AVE %s: %s:%d %s | fail to initial LowResRef Surface Pool %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to initial LowResResult Surface Pool %p %d"
- "%lld %d AVE %s: %s:%d %s | fail to initial LowResResult Surface Pool %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed in preparation %p %d %p %d | %p %p %p %d %d | %p %p %p %p %p %p %p"
- "%lld %d AVE %s: %s:%d %s | failed in preparation %p %d %p %d | %p %p %p %d %d | %p %p %p %p %p %p %p\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d %d %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d %d %d %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to DART map surface %s %d %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create LowResRCResult Surface Pool %p %d"
- "%lld %d AVE %s: %s:%d %s | failed to create LowResRCResult Surface Pool %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create LowResRef Surface Pool %p %d"
- "%lld %d AVE %s: %s:%d %s | failed to create LowResRef Surface Pool %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create LowResResult Surface Pool %p %d"
- "%lld %d AVE %s: %s:%d %s | failed to create LowResResult Surface Pool %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d %d %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %lld %d"
- "%lld %d AVE %s: %s:%d %s | failed to create surface %s %lld %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create surface header %s %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to create surface header %s %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to initialize GOP decision %d %d %d %d %d %d %d %p %d"
- "%lld %d AVE %s: %s:%d %s | failed to initialize GOP decision %d %d %d %d %d %d %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to initialize intra prediction %d %d %d %p %d"
- "%lld %d AVE %s: %s:%d %s | failed to initialize intra prediction %d %d %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %d %d %p"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %d %d %p\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %lld %p"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %lld %p\n"
- "%lld %d AVE %s: %s:%d DLBEntry %p %d transition is done"
- "%lld %d AVE %s: %s:%d DLBEntry %p %d transition is done\n"
- "%lld %d AVE %s: %s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | [ %s ]"
- "%lld %d AVE %s: %s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | [ %s ]\n"
- "%lld %d AVE %s: %s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | { %s }"
- "%lld %d AVE %s: %s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | { %s }\n"
- "%lld %d AVE %s: %s:%d EUMap %p %d | < %s >"
- "%lld %d AVE %s: %s:%d EUMap %p %d | < %s >\n"
- "%lld %d AVE %s: %s:%d EUMap %p %d | [ %s ]"
- "%lld %d AVE %s: %s:%d EUMap %p %d | [ %s ]\n"
- "%lld %d AVE %s: %s:%d EUStats %d | %s"
- "%lld %d AVE %s: %s:%d EUStats %d | %s\n"
- "%lld %d AVE %s: %s:%d [%d] %d %d %d %d"
- "%lld %d AVE %s: %s:%d [%d] %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d [%d] %p %d | %d 0x%x %d | %d -> %d | %d %d %d"
- "%lld %d AVE %s: %s:%d [%d] %p %d | %d 0x%x %d | %d -> %d | %d %d %d\n"
- "%lld %d AVE %s: %s:%d invalid EUMap %p %d | [ %s ]"
- "%lld %d AVE %s: %s:%d invalid EUMap %p %d | [ %s ]\n"
- "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaLowResRCResult[%d][%d][%d] == NULL"
- "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaLowResRCResult[%d][%d][%d] == NULL\n"
- "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaLowResResult[%d][%d][%d] == NULL"
- "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaLowResResult[%d][%d][%d] == NULL\n"
- "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaRecon[0][0][%d]==%p, pcaLowResRef[%d]==%p"
- "%lld %d AVE %s: %s::%s:%d %s | %p %d | pcaRecon[0][0][%d]==%p, pcaLowResRef[%d]==%p\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to DART unmap external surfaces %p %llu %p %d %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | failed to DART unmap external surfaces %p %llu %p %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to initialize sDLB %p %p %p %d"
- "%lld %d AVE %s: %s::%s:%d %s | failed to initialize sDLB %p %p %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | request task command during work pool sleep %p %d %p %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | request task command during work pool sleep %p %d %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong thread %p %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | wrong thread %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d Frame[%d] Stats: enc %d dis %d | %d %d %d type %s qp %d | inter %d intra %d | %d | %d %d | %d %d"
- "%lld %d AVE %s: %s::%s:%d Frame[%d] Stats: enc %d dis %d | %d %d %d type %s qp %d | inter %d intra %d | %d | %d %d | %d %d\n"
- "%lld %d AVE %s: %s::%s:%d LRME RC Result buffer not ready %p %d %p %d"
- "%lld %d AVE %s: %s::%s:%d LRME RC Result buffer not ready %p %d %p %d\n"
- "%lld %d AVE %s: %s::%s:%d find %p %d %d %p %d %p %lld %p %d %d %d %d %d %d %d %d"
- "%lld %d AVE %s: %s::%s:%d find %p %d %d %p %d %p %lld %p %d %d %d %d %d %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d keep busying %p %d %p %d"
- "%lld %d AVE %s: %s::%s:%d keep busying %p %d %p %d\n"
- "%lld %d AVE %s: %s::%s:%d total number of commands %p | %p %d %s | %d %d"
- "%lld %d AVE %s: %s::%s:%d total number of commands %p | %p %d %s | %d %d\n"
- "%lld %d AVE %s: %s::%s:%d wait %p %d %p %d %d %llu"
- "%lld %d AVE %s: %s::%s:%d wait %p %d %p %d %d %llu\n"
- "%lld %d AVE %s: %s::%s:%d wait with timeout %p %d %d %p %d %p %d %llu"
- "%lld %d AVE %s: %s::%s:%d wait with timeout %p %d %d %p %d %p %d %llu\n"
- "%lld %d AVE %s: Client die %p %d %p"
- "%lld %d AVE %s: Client die %p %d %p\n"
- "%lld %d AVE %s: Client%s: %p ID: %d Resolution: %dx%d Realtime: %d Priority: %d "
- "%lld %d AVE %s: Client%s: %p ID: %d Resolution: %dx%d Realtime: %d Priority: %d \n"
- "%lld %d AVE %s: DLB: %d - %d %d %d %s"
- "%lld %d AVE %s: DLB: %d - %d %d %d %s\n"
- "%lld %d AVE %s: Index        Time         SVEID  Command        -        Position Count     - Order  Result Client             ID    Type CodecType Priority  FrameNum  SliceIdx FrameType "
- "%lld %d AVE %s: Index        Time         SVEID  Command        -        Position Count     - Order  Result Client             ID    Type CodecType Priority  FrameNum  SliceIdx FrameType \n"
- "%lld %d AVE %s: MD%s: %p %lld %d %d total number of commands %d %d | %s"
- "%lld %d AVE %s: MD%s: %p %lld %d %d total number of commands %d %d | %s\n"
- "%s %d %d %d %d | %d"
- "%s %d %d %d %d | %d\n"
- "%s %d %d %d | %d"
- "%s %d %d %d | %d\n"
- "%s %d %d %d | %d | %d %d %d %d"
- "%s %d %d %d | %d | %d %d %d %d\n"
- "%s %d %d | %d"
- "%s %d %d | %d\n"
- "%s %d %d | %d | %d %d %d %d"
- "%s %d %d | %d | %d %d %d %d\n"
- "%s %d | %d"
- "%s %d | %d\n"
- "111111221112"
- "11122212111222222222212212212212221221222222211222222112222221122222211222222112222221122222211222222112222221122222211222222112222221122222211222222112222221122222211222222111122"
- "12111111111112222112222211111111111111111111111121222221122222222222222222222222222222222222111111112222222222222222222222222222222211111111"
- "12221222222211121111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
- "20:43:44"
- "222222222211"
- "802.61.1"
- "AVE_DLB_Acquire"
- "AVE_DLB_AllocEUNum"
- "AVE_DLB_AllocUnit"
- "AVE_DLB_ApplyDynamic"
- "AVE_DLB_ApplyStatic"
- "AVE_DLB_AssignUnit"
- "AVE_DLB_CalcStats"
- "AVE_DLB_Clean"
- "AVE_DLB_CleanUnit"
- "AVE_DLB_Init"
- "AVE_DLB_Keep"
- "AVE_DLB_Release"
- "AVE_DLB_Remap"
- "AVE_DLB_SelectUnit"
- "AVE_DLB_Switch"
- "AVE_DLB_Uninit"
- "AVE_GOPDecision_Init"
- "AVE_GOPDecision_Uninit"
- "AVE_IntraPred_Init"
- "AVE_IntraPred_Uninit"
- "CheckSleepDone"
- "Client%s: %p ID: %d Resolution: %dx%d Realtime: %d Priority: %d "
- "Client%s: %p ID: %d Resolution: %dx%d Realtime: %d Priority: %d \n"
- "DLB: %d - %d %d %d %s"
- "DLB: %d - %d %d %d %s\n"
- "Index        Time         SVEID  Command        -        Position Count     - Order  Result Client             ID    Type CodecType Priority  FrameNum  SliceIdx FrameType "
- "Index        Time         SVEID  Command        -        Position Count     - Order  Result Client             ID    Type CodecType Priority  FrameNum  SliceIdx FrameType \n"
- "Jul  3 2024"
- "LowResRCResult"
- "LowResRef"
- "LowResRefChroma"
- "LowResRefChromaHeader"
- "LowResRefLumaHeader"
- "LowResResult"
- "MD%s: %p %lld %d %d total number of commands %d %d | %s"
- "MD%s: %p %lld %d %d total number of commands %d %d | %s\n"
- "NotifyRun"
- "NotifySleep"
- "ProcessSleep"
- "WaitThreadIdle"
- "WaitThreadsIdle"
- "m_eState == AVE_WorkPool_State_Run"
- "m_pcaWorkThread[iThreadID] != nullptr"
- "m_psDLB->iMode == 0"
- "num == 0 || num >= psSInfoSet->iaRecon[AVE_SIIdx_Set]"
- "pClient->pcaSurfacePool[AVE_SurPoolIdx_LRRCRes] != nullptr"
- "pClient->pcaSurfacePool[AVE_SurPoolIdx_LRRef] != nullptr"
- "pClient->pcaSurfacePool[AVE_SurPoolIdx_LRRes] != nullptr"
- "pDLB != nullptr"
- "pDLB != nullptr && pCfg != nullptr && pDevInfo != nullptr"
- "pInfo->sExtraBuff.saCavlcHeader[i].iAddr != 0"
- "pInfo->sRef.saLow_Res_UV_L0[AVE_REFERENCE_A].iAddr != 0"
- "pInfo->sRef.saLow_Res_UV_L0[AVE_REFERENCE_B].iAddr != 0"
- "pInfo->sRef.saLow_Res_UV_L0_Header[AVE_REFERENCE_A].iAddr != 0"
- "pInfo->sRef.saLow_Res_UV_L0_Header[AVE_REFERENCE_B].iAddr != 0"
- "pInfo->sRef.saLow_Res_UV_L1[AVE_REFERENCE_A].iAddr != 0"
- "pInfo->sRef.saLow_Res_UV_L1_Header[AVE_REFERENCE_A].iAddr != 0"
- "pInfo->sRef.saLow_Res_Y_L0_Header[AVE_REFERENCE_A].iAddr != 0"
- "pInfo->sRef.saLow_Res_Y_L0_Header[AVE_REFERENCE_B].iAddr != 0"
- "pInfo->sRef.saLow_Res_Y_L1_Header[AVE_REFERENCE_A].iAddr != 0"
- "pMgr != nullptr && pSIDSet != nullptr && pSet != nullptr"
- "pMgr != nullptr && psTask != nullptr && pSIDSet != nullptr && pSet != nullptr"
- "pSet->pcaRecon[i][j][k]->GetSize() >= psSInfoSet->iaRecon[AVE_SIIdx_Size]"
- "pVP->saEntropyCodingHeader[0].iAddr != 0"
- "pVP->saEntropyCodingHeader[i].iAddr != 0"
- "pVP->saLowResChromaHeader[j][k].iAddr != 0"
- "pVP->saLowResChroma[j][k].iAddr != 0"
- "pVP->saLowResHeader[j][k].iAddr != 0"
- "pcaLowResRCResult[k] != nullptr"
- "pcaLowResRef[k] != nullptr"
- "pcaLowResResult[i + iRefNum][0] [iLRMEResultBufSetIdx] != nullptr"
- "pcaLowResResult[k] != nullptr"
- "pcaRecon != nullptr && pcaLowResRef != nullptr && pcaLowResResult != nullptr && pcaLowResRCResult != nullptr"
- "tmpLayer == 0 || tmpLayer >= psSInfoSet->iaRecon[AVE_SIIdx_Layer]"
- "tmpNum == 0 || tmpNum >= psSInfoSet->iaRecon[AVE_SIIdx_Num]"

```

>  `com.apple.driver.AppleT8130CLPC`

```diff

-1175.0.21.0.0
-  __TEXT.__cstring: 0x2c2f
+1175.0.25.0.0
+  __TEXT.__cstring: 0x2c4a
   __TEXT.__const: 0xb34
-  __TEXT_EXEC.__text: 0x4c260
+  __TEXT_EXEC.__text: 0x4c884
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xa2b8
-  __DATA.__common: 0x7b19
+  __DATA.__data: 0xa2f8
+  __DATA.__common: 0x7b21
   __DATA.__bss: 0x278
   __DATA_CONST.__auth_got: 0x4a0
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__mod_init_func: 0x118
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x4fb0
+  __DATA_CONST.__const: 0x4fc8
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
-  Functions: 1262
+  Functions: 1263
   Symbols:   0
-  CStrings:  463
+  CStrings:  464
 
CStrings:
+ "2024-07-15T21:28:14-07:00"
+ "AppleCLPC-1175.0.25"
+ "clpc-disable-perf-map-warp"
- "2024-07-03T20:40:03-07:00"
- "AppleCLPC-1175.0.21"

```

>  `com.apple.driver.AppleUSBAudio`

```diff

-701.65.0.0.0
+701.71.0.0.0
   __TEXT.__cstring: 0x2dad
-  __TEXT.__const: 0x5b0
-  __TEXT_EXEC.__text: 0x7682c
+  __TEXT.__const: 0x5c0
+  __TEXT_EXEC.__text: 0x76918
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x628

```

>  `com.apple.iokit.IOSurface`

```diff

-368.0.4.0.0
+368.0.6.0.0
   __TEXT.__cstring: 0x4f28
   __TEXT.__const: 0x48
   __TEXT.__os_log: 0x4ff
-  __TEXT_EXEC.__text: 0x2d340
+  __TEXT_EXEC.__text: 0x2d364
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x178
   __DATA.__common: 0x3e8

```

>  `com.apple.driver.AppleProResHW`

```diff

-400.73.0.0.0
+400.78.0.0.0
   __TEXT.__const: 0x1b40
-  __TEXT.__os_log: 0x7318
+  __TEXT.__os_log: 0x7409
   __TEXT.__cstring: 0xdcc
-  __TEXT_EXEC.__text: 0x18950
+  __TEXT_EXEC.__text: 0x189ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x358
   __DATA.__common: 0x70
CStrings:
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes ERROR: Failed to map decoder output buffer with DART. ret = 0x%x.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes ERROR: Plane count is not 4 or 0 or 1!\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes ERROR: Plane count is not 4!\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes ERROR: Two Pic mode not supported\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes RAW ERROR: Plane count is not 0 or 4!\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes YCbCr ERROR: Plane count is not 2 or 3!\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes-Dec ERROR: sendAsyncResult64 failed.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes-Enc ERROR: sendAsyncResult64 failed.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResCommand ERROR: Enqueue called when CommandQueue is full NULL\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResCommand new failed\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResCommandQueue ERROR: Dequeue called for empty queue\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResHW ERROR: Could not set power state to %lu\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResHW ERROR: Could not wait long enough for PowerOn\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResHW ERROR: No provider attached\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResHW Warning: setPerfState skipped for PowerOffPending\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Cannot acquire IOFence for encInputIOSurface\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Cannot allocate user client info\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Cannot clear DelayList\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Cannot generate segments\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Cannot get DMA command\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Could not allocate memory for local descriptor.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Could not attach user client.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Could not disable power.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Could not enable power.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Could not map bitstream buffer with DART for Ring Descriptor Memory. mapRet = 0x%x.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Could not map bitstream buffer with DART for Statistics buffer. mapRet = 0x%x.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Could not wait for %u frames\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Device not available\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Failed calling start on provider\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Failed to map decoder input buffer with DART. ret = 0x%x.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Failed to map encoder input buffer with DART. ret = 0x%x.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Failed to map encoder output buffer with DART. ret = 0x%x.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Failed to map encoder statistics buffer with DART. ret = 0x%x.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): InInfo->decInputIOSurface NULL.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): InInfo->decOutputIOSurface NULL.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): InInfo->encInputIOSurface CSID(%d) NULL.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): InInfo->encOutputIOSurface CSID(%d) NULL.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): InInfo->statsBufOffs.statsIOSurf statsCSID(%d) is NULL.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Incorrect arguments for openUserClient\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Invalid coreIdx %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Invalid method selector\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Memory Descriptor is NULL\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): NULL parameter\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No callback registered for this client\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No notification port set for this client\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No provider for UserClient\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No refcon registered for callback for this client\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No resources to allocate Descriptor ring memory\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No resources to allocate Statistics buffer\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Power Not On, m_ePowerState[%u]=%d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Power Off on any core or ProRes doesn't own any core\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Power Off on any core or ProRes doesn't own any core. NumClients %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Power is Off or ProRes doesn't own core %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Power is Off or ProRes doesn't own core %d. Will not clear DelayList\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): ProRes doesn't own any core\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): ProRes_DecodeFrame_UserKernel_In_Info NULL\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): ProRes_EncodeFrame_UserKernel_In_Info NULL\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported eClientType ...\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Zero NumClients\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): [%d] DecodeFrame ERROR: Out of desc ring, pending %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): [%d] EncodeFrame ERROR: Out of desc ring, pending %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): encOutputBufInfo IOSurface is NULL.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): encStatisticsBufInfo IOSurface is NULL.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): m_DRTail[%d]=0x%x < m_DRHead[%d]=0x%x Wraped\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): m_DRTail[%d]=0x%x > m_DRHead[%d]=0x%x\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): m_ProviderDriver NULL.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): pBuf = NULL\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): pCurr = NULL\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): pFront = NULL\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): pIOSurface NULL\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): pMemDesc->prepare() failed\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: Cannot Start IOService\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: Cannot allocate m_pInitLock\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: Could not extract HW device info\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: Could not extract string from device info\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot allocate m_pAcceleratorLock\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot allocate m_pClientListLock\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot cast mPowerProvider\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot create copy of mapper\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot create interrupt event source\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot create new command gate\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot create new workloop\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot create timer event source\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot find matching provider\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot get the core surface root\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot initiate device reset function\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot map registers memory object 0\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot map registers memory object 1\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot retrieve registers memory object 0\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot retrieve registers memory object 1\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot support more devices\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: invalid error type %s\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: invalid parameters %p %p\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: super::init failed\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProRes Error: Insufficient arguments from client\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProResHW ERROR: Client not entitled for ProResHW task\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProResHW ERROR: Could not disable power.\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProResHW ERROR: Could not get Instance info\n"
+ "ERROR AppleProResHW: %d: %s(): AppleProResHW ERROR: Could not get get the actual coreIdx from InstanceStr\n"
+ "ERROR AppleProResHW: %d: %s(): Cannot allocate user client info\n"
+ "ERROR AppleProResHW: %d: %s(): Cannot find decode user client info\n"
+ "ERROR AppleProResHW: %d: %s(): Cannot find encode user client info\n"
+ "ERROR AppleProResHW: %d: %s(): Cannot find user client info\n"
+ "ERROR AppleProResHW: %d: %s(): Closing with invalid m_pClientList or m_NumClients\n"
+ "ERROR AppleProResHW: %d: %s(): Descriptor size for clientType not as expected in DecodeFrame()\n"
+ "ERROR AppleProResHW: %d: %s(): Descriptor size for clientType not as expected in EncodeFrame()\n"
+ "ERROR AppleProResHW: %d: %s(): Invalid CoreIdx\n"
+ "ERROR AppleProResHW: %d: %s(): attachClient ERROR: Power Off on any core or ProRes doesn't own any core\n"
+ "ERROR AppleProResHW: %d: %s(): kIODARTFunctionRegisterErrorHandler failed 0x%x\n"
+ "ERROR AppleProResHW: %d: %s(): kIODARTMapperEarlyReclaimKey failed 0x%x\n"
+ "ERROR AppleProResHW: %d: %s(): registerPowerDriver() failed 0x%x\n"
+ "ERROR: AppleProResHW (0x%x): %d: %s(): HW error decSatus=%d status0=0x%x statusCode=%d status2=0x%x\n\n"
+ "ERROR: AppleProResHW (0x%x): %d: %s(): HW error encSatus=%d status0=0x%x statusCode=%d status2=0x%x \n\n"
+ "ERROR: AppleProResHW: %d: %s(): Disable DART with Dirty Shutdown\n"
+ "ERROR: AppleProResHW: %d: %s(): Invalid DevID %d, no AXI values have been set\n"
+ "ERROR: AppleProResHW: %d: %s(): Invalid DevVer %d, no AXI values have been set\n"
+ "ERROR: AppleProResHW: %d: %s(): Invalid DevVer (0x%x), no AXI values have been set\n"
+ "ERROR: AppleProResHW: %d: %s(): Invalid coreIdx %d, maxNumCores=%d\n"
+ "ERROR: AppleProResHW: %d: %s(): Invalid requested core ownership - fatal error\n"
+ "ERROR: AppleProResHW: %d: %s(): LLT AR %d\n"
+ "ERROR: AppleProResHW: %d: %s(): LLT AW %d\n"
+ "ERROR: AppleProResHW: %d: %s(): TLimit reports back %d outstanding\n"
+ "ERROR: AppleProResHW: %d: %s(): [%d] DMA sts %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n"
+ "ERROR: AppleProResHW: %d: %s(): [%d] commandQ=%d IRQ=0x%x IRQ-En=0x%x st0=0x%x st1=0x%x st2=0x%x m_pTimerEventSource %p\n\n"
+ "ERROR: AppleProResHW: %d: %s(): abort q'd cmds %d\n"
+ "ERROR: AppleProResHW: %d: %s(): eventSource %p this %p\n"
+ "ERROR: AppleProResHW: %d: %s(): kIODARTFunctionCacheFlushInactive Failed ret=0x%x\n"
+ "ERROR: AppleProResHW: %d: %s(): kIODARTFunctionSetActive with Dirty Shutdown Failed ret=0x%x\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProRes ERROR: Failed to map decoder output buffer with DART. ret = 0x%x.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProRes ERROR: Plane count is not 4 or 0 or 1!\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProRes ERROR: Plane count is not 4!\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProRes ERROR: Two Pic mode not supported\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProRes RAW ERROR: Plane count is not 0 or 4!\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProRes YCbCr ERROR: Plane count is not 2 or 3!\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProRes-Dec ERROR: sendAsyncResult64 failed.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProRes-Enc ERROR: sendAsyncResult64 failed.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProResCommand ERROR: Enqueue called when CommandQueue is full NULL\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProResCommand new failed\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProResCommandQueue ERROR: Dequeue called for empty queue\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProResHW ERROR: Could not set power state to %lu\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProResHW ERROR: Could not wait long enough for PowerOn\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProResHW ERROR: No provider attached\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): AppleProResHW Warning: setPerfState skipped for PowerOffPending\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Cannot acquire IOFence for encInputIOSurface\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Cannot allocate user client info\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Cannot clear DelayList\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Cannot generate segments\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Cannot get DMA command\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Could not allocate memory for local descriptor.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Could not attach user client.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Could not disable power.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Could not enable power.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Could not map bitstream buffer with DART for Ring Descriptor Memory. mapRet = 0x%x.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Could not map bitstream buffer with DART for Statistics buffer. mapRet = 0x%x.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Could not wait for %u frames\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Device not available\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Failed calling start on provider\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Failed to map decoder input buffer with DART. ret = 0x%x.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Failed to map encoder input buffer with DART. ret = 0x%x.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Failed to map encoder output buffer with DART. ret = 0x%x.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Failed to map encoder statistics buffer with DART. ret = 0x%x.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): InInfo->decInputIOSurface NULL.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): InInfo->decOutputIOSurface NULL.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): InInfo->encInputIOSurface CSID(%d) NULL.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): InInfo->encOutputIOSurface CSID(%d) NULL.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): InInfo->statsBufOffs.statsIOSurf statsCSID(%d) is NULL.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Incorrect arguments for openUserClient\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Invalid coreIdx %d\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Invalid method selector\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Memory Descriptor is NULL\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): NULL parameter\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): No callback registered for this client\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): No notification port set for this client\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): No provider for UserClient\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): No refcon registered for callback for this client\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): No resources to allocate Descriptor ring memory\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): No resources to allocate Statistics buffer\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Power Not On, m_ePowerState[%u]=%d\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Power Off on any core or ProRes doesn't own any core\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Power Off on any core or ProRes doesn't own any core. NumClients %d\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Power is Off or ProRes doesn't own core %d\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Power is Off or ProRes doesn't own core %d. Will not clear DelayList\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): ProRes doesn't own any core\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): ProRes_DecodeFrame_UserKernel_In_Info NULL\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): ProRes_EncodeFrame_UserKernel_In_Info NULL\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Unsupported eClientType ...\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): Zero NumClients\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): [%d] DecodeFrame ERROR: Out of desc ring, pending %d\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): [%d] EncodeFrame ERROR: Out of desc ring, pending %d\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): encOutputBufInfo IOSurface is NULL.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): encStatisticsBufInfo IOSurface is NULL.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): m_DRTail[%d]=0x%x < m_DRHead[%d]=0x%x Wraped\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): m_DRTail[%d]=0x%x > m_DRHead[%d]=0x%x\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): m_ProviderDriver NULL.\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): pBuf = NULL\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): pCurr = NULL\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): pFront = NULL\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): pIOSurface NULL\n"
- "ERROR AppleProResHW (0x%x): %d:%s(): pMemDesc->prepare() failed\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: Cannot Start IOService\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: Cannot allocate m_pInitLock\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: Could not extract HW device info\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: Could not extract string from device info\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot allocate m_pAcceleratorLock\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot allocate m_pClientListLock\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot cast mPowerProvider\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot create copy of mapper\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot create interrupt event source\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot create new command gate\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot create new workloop\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot create timer event source\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot find matching provider\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot get the core surface root\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot initiate device reset function\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot map registers memory object 0\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot map registers memory object 1\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot retrieve registers memory object 0\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot retrieve registers memory object 1\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: cannot support more devices\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: invalid error type %s\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: invalid parameters %p %p\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes ERROR: super::init failed\n"
- "ERROR AppleProResHW: %d:%s(): AppleProRes Error: Insufficient arguments from client\n"
- "ERROR AppleProResHW: %d:%s(): AppleProResHW ERROR: Client not entitled for ProResHW task\n"
- "ERROR AppleProResHW: %d:%s(): AppleProResHW ERROR: Could not disable power.\n"
- "ERROR AppleProResHW: %d:%s(): AppleProResHW ERROR: Could not get Instance info\n"
- "ERROR AppleProResHW: %d:%s(): AppleProResHW ERROR: Could not get get the actual coreIdx from InstanceStr\n"
- "ERROR AppleProResHW: %d:%s(): Cannot allocate user client info\n"
- "ERROR AppleProResHW: %d:%s(): Cannot find decode user client info\n"
- "ERROR AppleProResHW: %d:%s(): Cannot find encode user client info\n"
- "ERROR AppleProResHW: %d:%s(): Cannot find user client info\n"
- "ERROR AppleProResHW: %d:%s(): Closing with invalid m_pClientList or m_NumClients\n"
- "ERROR AppleProResHW: %d:%s(): Descriptor size for clientType not as expected in DecodeFrame()\n"
- "ERROR AppleProResHW: %d:%s(): Descriptor size for clientType not as expected in EncodeFrame()\n"
- "ERROR AppleProResHW: %d:%s(): Invalid CoreIdx\n"
- "ERROR AppleProResHW: %d:%s(): attachClient ERROR: Power Off on any core or ProRes doesn't own any core\n"
- "ERROR AppleProResHW: %d:%s(): kIODARTFunctionRegisterErrorHandler failed 0x%x\n"
- "ERROR AppleProResHW: %d:%s(): kIODARTMapperEarlyReclaimKey failed 0x%x\n"
- "ERROR AppleProResHW: %d:%s(): registerPowerDriver() failed 0x%x\n"
- "ERROR: AppleProResHW %s(): Disable DART with Dirty Shutdown\n"
- "ERROR: AppleProResHW %s(): Invalid DevID %d, no AXI values have been set\n"
- "ERROR: AppleProResHW %s(): Invalid DevVer %d, no AXI values have been set\n"
- "ERROR: AppleProResHW %s(): Invalid DevVer (0x%x), no AXI values have been set\n"
- "ERROR: AppleProResHW %s(): Invalid coreIdx %d, maxNumCores=%d\n"
- "ERROR: AppleProResHW %s(): Invalid requested core ownership - fatal error\n"
- "ERROR: AppleProResHW %s(): LLT AR %d\n"
- "ERROR: AppleProResHW %s(): LLT AW %d\n"
- "ERROR: AppleProResHW %s(): TLimit reports back %d outstanding\n"
- "ERROR: AppleProResHW %s(): [%d] DMA sts %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n"
- "ERROR: AppleProResHW %s(): [%d] commandQ=%d IRQ=0x%x IRQ-En=0x%x st0=0x%x st1=0x%x st2=0x%x m_pTimerEventSource %p\n\n"
- "ERROR: AppleProResHW %s(): abort q'd cmds %d\n"
- "ERROR: AppleProResHW %s(): eventSource %p this %p\n"
- "ERROR: AppleProResHW %s(): kIODARTFunctionCacheFlushInactive Failed ret=0x%x\n"
- "ERROR: AppleProResHW %s(): kIODARTFunctionSetActive with Dirty Shutdown Failed ret=0x%x\n"
- "ERROR: AppleProResHW (0x%x): %s(): HW error decSatus=%d status0=0x%x statusCode=%d status2=0x%x\n\n"
- "ERROR: AppleProResHW (0x%x): %s(): HW error encSatus=%d status0=0x%x statusCode=%d status2=0x%x \n\n"

```

>  `com.apple.iokit.IOAccessoryManager`

```diff

-1004.0.0.0.0
+1004.0.2.0.0
   __TEXT.__const: 0x2f8
-  __TEXT.__cstring: 0x10627
-  __TEXT.__os_log: 0x10365
-  __TEXT_EXEC.__text: 0xe8ba8
+  __TEXT.__cstring: 0x1080b
+  __TEXT.__os_log: 0x106d8
+  __TEXT_EXEC.__text: 0xec744
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
-  __DATA.__common: 0x15b8
+  __DATA.__common: 0x1630
   __DATA.__bss: 0x132
   __DATA_CONST.__auth_got: 0x5b8
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__mod_init_func: 0x320
-  __DATA_CONST.__mod_term_func: 0x318
-  __DATA_CONST.__const: 0x28668
-  __DATA_CONST.__kalloc_type: 0x2380
-  Functions: 4352
+  __DATA_CONST.__mod_init_func: 0x338
+  __DATA_CONST.__mod_term_func: 0x330
+  __DATA_CONST.__const: 0x29af0
+  __DATA_CONST.__kalloc_type: 0x2440
+  Functions: 4436
   Symbols:   0
-  CStrings:  2752
+  CStrings:  2780
 
CStrings:
+ " [*]"
+ "%s::%s(): [%s%s%s] Setting VDOs... (vdoArray->getCount(): %u)\n\n"
+ "%s::%s(): [%s%s%s] specRevision: %d\n\n"
+ "%s::%s(): [%s@%s: %s%s%s] HPD state changed! (hpdState: %d)\n"
+ "121111121222121211111121111122"
+ "Active Cable"
+ "Address Description"
+ "IOPortTransportComponentCCUSBPD"
+ "IOPortTransportComponentCCUSBPDSOP"
+ "IOPortTransportComponentCCUSBPDSOPp"
+ "PDUSB Host"
+ "PDUSB Hub"
+ "PDUSB Peripheral"
+ "PSD"
+ "Passive Cable"
+ "Power Brick"
+ "Product Type"
+ "Product Type Description"
+ "Specification Revision"
+ "VDO Count"
+ "VPD"
+ "[ERROR] [%s%s%s] Invalid number of VDOs! (count: %u, expecting: >= %u)\n\n"
+ "[ERROR] [%s%s%s] This power source is not the owner of the power source option!\n\n"
+ "_clearOtherPowerSourceWinners::matchingDict"
+ "bcdDevice"
+ "setSpecRevision"
+ "setVDOs"
+ "site.IOPortTransportComponentCCUSBPD"
+ "site.IOPortTransportComponentCCUSBPDSOP"
+ "site.IOPortTransportComponentCCUSBPDSOPp"
+ "v24@?0B8B12^{IOServiceNotificationManager=^^?i^{IOService}^{OSString}IIB^{OSOrderedSetEquality}^{_IOLock}BBB^{_IORecursiveLock}^?^v^v^{IONotifier}}16"
- "%s::%s(): [%s@%s: %s%s%s] HPD state shanged! (hpdState: %d)\n"
- "ParentFeatureTypeDescription"
- "v24@?0B8B12^{IOServiceNotificationManager=^^?i^{IOService}^{OSString}IIB^{OSOrderedSetEquality}^{_IOLock}B^{_IORecursiveLock}^?^v^v^{IONotifier}}16"

```

>  `com.apple.AGXG16P`

```diff

-320.23.0.0.0
+320.23.3.0.0
   __TEXT.__const: 0x4444
   __TEXT.__cstring: 0xca1f
   __TEXT.__os_log: 0x2f7
-  __TEXT_EXEC.__text: 0xaea04
+  __TEXT_EXEC.__text: 0xaeaac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13b8
   __DATA.__common: 0x10

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x320
   __DATA_CONST.__mod_term_func: 0x280
-  __DATA_CONST.__const: 0x10bb0
+  __DATA_CONST.__const: 0x10bd8
   __DATA_CONST.__kalloc_type: 0x2140
   __DATA_CONST.__kalloc_var: 0x3160
-  Functions: 3069
+  Functions: 3070
   Symbols:   0
   CStrings:  1715
 
CStrings:
+ "121111112112222122111111211222212211111121122221221222222222221122111111112222222211111212121121211212112121121211212112121121211212112121121211212112121111111112221112221112221112221112221112221112221112221112221112221112222222111122121121211111111222222222212112222222222222222222222222222222222222222222222222222222222222222222222221211211222222222222222222111111221212222222221222221111122121222222222122222111112212122222222212222211111221212222222221222221111122121222222222122222111112212122222222212222211111222111111222111111222111111222111111222111111222111111222111111222111111222112111112211111111221122111111111111111111111111111111111112222222222222222221111112212122222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111112222222"
+ "1211112222211111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "Jul 15 2024 21:27:11"
- "1211111121122221221111112112222122111111211222212212222222222211221111111122222222111112121121211212112121121211212112121121211212112121121211212112121111111112221112221112221112221112221112221112221112221112221112221112222222111122121121211111111222222222212112222222222222222222222222222222222222222222222222222222222222222222222221211211222222222222222222111111221212222222221222221111122121222222222122222111112212122222222212222211111221212222222221222221111122121222222222122222111112212122222222212222211111222111111222111111222111111222111111222111111222111111222111111222111111222112111112211111111221122111111111111111111111111111111111112222222222222222221111112212122222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111112222222"
- "121111222221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "Jul  3 2024 20:40:36"

```

>  `com.apple.driver.AppleARMWatchdogTimer`

```diff

-274.0.1.0.0
+274.0.3.0.0
   __TEXT.__cstring: 0x1206
-  __TEXT_EXEC.__text: 0x5018
+  __TEXT_EXEC.__text: 0x502c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x118
   __DATA.__common: 0xc0

```

>  `com.apple.driver.AppleHPM`

```diff

-570.0.1.0.0
-  __TEXT.__cstring: 0x1b2a1
+570.0.3.0.0
+  __TEXT.__cstring: 0x1b5eb
   __TEXT.__const: 0xc0
   __TEXT.__os_log: 0x1e8
-  __TEXT_EXEC.__text: 0x5c438
+  __TEXT_EXEC.__text: 0x5cef8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6d0
   __DATA.__common: 0x518
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xf8
-  __DATA_CONST.__const: 0x111b0
+  __DATA_CONST.__const: 0x11290
   __DATA_CONST.__kalloc_type: 0xb00
-  Functions: 1394
+  Functions: 1399
   Symbols:   0
-  CStrings:  1552
+  CStrings:  1562
 
CStrings:
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::initInterruptManager - LDCM not started, setting up matcher\n\n"
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::initSingleHPM - LDCM not started, setting up matcher\n\n"
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::setupMatchingForLDCM - Failed to allocate callback, LDCM wont' work properly\n\n"
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::setupMatchingForLDCM - matcher failed to setup, no LDCM\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::initInterruptManager - LDCM not started, setting up matcher\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::initSingleHPM - LDCM not started, setting up matcher\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::setupMatchingForLDCM - Failed to allocate callback, LDCM wont' work properly\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::setupMatchingForLDCM - matcher failed to setup, no LDCM\n\n"
+ "%s::%s(0x%x@0x%x): LDCM not started, service not of AppleHPMLDCMType2\n\n"
+ "%s::%s(0x%x@0x%x): service and provider did NOT match, belongs to different node\n\n"
+ "%s::%s(0x%x@0x%x): service and provider matched\n\n"
+ "%s::%s(0x%x@0x%x): service did NOT match, belongs to different node\n\n"
+ "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121211121"
+ "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121211122"
+ "12111112122212121111112111112122222222112211111112122111122222212222121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122222111111111111111111111111111111122222222222222221111111112111111212121"
+ "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121212211111111111111111111111111111122222222222221111111112111111222222222222121"
+ "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121212211111111111111111111111111111122222222222221111111112111111222222222222121112"
+ "12111112122212121111112111112122222222112211111112122111122222212222121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122222111111111111111111111111111111122222222222222221111111112111111212122111111111111111111111111111111222222222222211111111121111112222222222221211121"
+ "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121212211111111111111111111111111111122222222222221111111112111111222222222222121112112"
+ "12111112122212121111112111112122222222112211111112122111122222212222121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122222111111111111111111111111111111122222222222222221111111112111111212122111111111111111111111111111111222222222222211111111121111112222222222221211122"
+ "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121212211111111111111111111111111111122222222222221111111112111111222222222222121112212"
+ "assignLDCMHandle"
+ "setupMatchingForLDCM"
- "%s::%s(0x%x@0x%x): AppleHPMInterface::initInterruptManager - LDCM not started\n\n"
- "%s::%s(0x%x@0x%x): AppleHPMInterface::initSingleHPM - LDCM not started\n\n"
- "%s::%s(0x%x@0x%x): AppleTCController::initInterruptManager - LDCM not started\n\n"
- "%s::%s(0x%x@0x%x): AppleTCController::initSingleHPM - LDCM not started\n\n"
- "12111112122212121111112111112122222222112211111112122111122222212222121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122222111111111111111111111111111111122222222222222221111111112111111212"
- "121111121222121211111121111121222222221122111111121221111222222122221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211222221111111111111111111111111111111222222222222222211111111121111112121121"
- "121111121222121211111121111121222222221122111111121221111222222122221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211222221111111111111111111111111111111222222222222222211111111121111112121122"
- "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121221111111111111111111111111111112222222222222111111111211111122222222222212"
- "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121221111111111111111111111111111112222222222222111111111211111122222222222212112"
- "12111112122212121111112111112122222222112211111112122111122222212222121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122222111111111111111111111111111111122222222222222221111111112111111212211111111111111111111111111111122222222222221111111112111111222222222222121121"
- "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121221111111111111111111111111111112222222222222111111111211111122222222222212112112"
- "12111112122212121111112111112122222222112211111112122111122222212222121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122222111111111111111111111111111111122222222222222221111111112111111212211111111111111111111111111111122222222222221111111112111111222222222222121122"
- "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222211111111111111111111111111111112222222222222222111111111211111121221111111111111111111111111111112222222222222111111111211111122222222222212112212"

```

>  `com.apple.driver.usb.AppleUSBHub`

```diff

-1402.0.2.0.0
+1402.0.7.0.0
   __TEXT.__const: 0x38
   __TEXT.__cstring: 0x227e
   __TEXT.__os_log: 0x2465
-  __TEXT_EXEC.__text: 0x224dc
+  __TEXT_EXEC.__text: 0x22618
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1a0

```

>  `com.apple.security.sandbox`

```diff

-2401.0.48.0.0
-  __TEXT.__const: 0x18cfc1
+2401.0.56.0.0
+  __TEXT.__const: 0x18cad9
   __TEXT.__cstring: 0x6ec0
   __TEXT.__os_log: 0x2029
   __TEXT_EXEC.__text: 0x30438

```

>  `com.apple.driver.AppleT8110DART`

```diff

-452.0.2.0.0
+452.0.4.0.0
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x27b4
-  __TEXT_EXEC.__text: 0xd458
+  __TEXT_EXEC.__text: 0xd4a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-395.23.1.0.0
+395.25.0.0.0
   __TEXT.__cstring: 0x3ef5
   __TEXT.__const: 0x2148
-  __TEXT_EXEC.__text: 0x1fb60
+  __TEXT_EXEC.__text: 0x1f8fc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe0
   __DATA.__common: 0x26d0

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1628
   __DATA_CONST.__kalloc_type: 0x7c0
-  Functions: 693
+  Functions: 690
   Symbols:   0
   CStrings:  364
 
CStrings:
+ "D588_callback__"
+ "D589_callback__"
- "D590_callback__"
- "D591_callback__"

```

>  `com.apple.kec.corecrypto`

```diff

-1736.0.36.0.0
-  __TEXT.__cstring: 0x46e7
+1736.0.41.0.0
+  __TEXT.__cstring: 0x4866
   __TEXT.__const: 0x14490
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x58bfc
+  __TEXT_EXEC.__text: 0x58d3c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2df0
   __DATA.__bss: 0x2980

   __DATA_CONST.__const: 0x2c90
   Functions: 1313
   Symbols:   0
-  CStrings:  545
+  CStrings:  550
 
CStrings:
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected FAILURE\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected SUCCESS\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccec_x963_import_priv\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: FORCEFAIL\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: expected SUCCESS\n"
+ "fipspost_post_ecdsa_pairwise_ws"
- "FIPSPOST_KEXT [%llu] %s:%d: FAILED: import\n"

```

>  `com.apple.plugin.IOgPTPPlugin`

```diff

-1300.49.0.0.0
+1300.50.1.0.0
   __TEXT.__cstring: 0x6179
-  __TEXT.__os_log: 0x1a456
+  __TEXT.__os_log: 0x1a4a8
   __TEXT.__const: 0x278
-  __TEXT_EXEC.__text: 0x709f4
+  __TEXT_EXEC.__text: 0x70acc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x5d8

   __DATA_CONST.__kalloc_var: 0x280
   Functions: 1416
   Symbols:   0
-  CStrings:  1425
+  CStrings:  1426
 
CStrings:
+ "  %s(%s): Receive announce with pathTrace[%lu]: 0x%016llx\n"
+ "  %s(%s): Transmit announce with pathTrace[%lu]: 0x%016llx\n"
- "  %s(%s): pathTrace[%lu]: 0x%016llx\n"

```

>  `com.apple.driver.AppleDCP`

```diff

-811.0.20.0.0
-  __TEXT.__cstring: 0x1664
+811.0.26.0.0
+  __TEXT.__cstring: 0x1963
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x5e48
+  __TEXT_EXEC.__text: 0x67e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1430
   __DATA_CONST.__kalloc_type: 0x100
-  Functions: 175
+  Functions: 178
   Symbols:   0
-  CStrings:  115
+  CStrings:  140
 
CStrings:
+ "\"[AppleDCPExpert:0x%llx] GAPF %u Error, GAPF not mapped\\n\" @%s:%d"
+ "\"[AppleDCPExpert:0x%llx] GAPF %u: Valid: %s, Master ID %u, Address 0x%llx, CMD %s\\n\" @%s:%d"
+ "\"[AppleDCPExpert:0x%llx] GAPF: Unexpected GAPF Assertion mask: 0x%x\\n\" @%s:%d"
+ "1211111212221212122222222222222222222222222222222222222222112121211111121122212122112211122221121121111111111111222111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111"
+ "N"
+ "R"
+ "W"
+ "Y"
+ "[AppleDCPExpert:0x%llx] %u GAPFs mapped\n"
+ "[AppleDCPExpert:0x%llx] failed to add GAPF interrupt event source to workloop\n"
+ "[AppleDCPExpert:0x%llx] failed to get IRQ for GAPFs\n"
+ "[AppleDCPExpert:0x%llx] no GAPFs mapped - bailing\n"
+ "bulk-dcp-dart-tz-gapf-index"
+ "bulk-gapf-index"
+ "ctrl-m3-jic-gapf-index"
+ "grt-gapf-index"
+ "grt-smmu-tz-gapf-index"
+ "inbound-gapf-index"
+ "ipa-gapf-index"
+ "llt-dcp-dart-tz-gapf-index"
+ "llt-gapf-index"
+ "main-pio-jic-gapf-index"
+ "rt-dart-tz-gapf-index"
+ "rt-gapf-index"
+ "rt-smmu-tz-gapf-index"
+ "security-reg-index"
- "12111112122212121222222222222222222222222222222222222222221121212111111211222121221122111222211222111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111"

```

>  `com.apple.driver.AppleDiskImages2`

```diff

-379.0.0.0.0
-  __TEXT.__cstring: 0x2000
+379.0.2.0.0
+  __TEXT.__cstring: 0x2004
   __TEXT.__os_log: 0x11a2
   __TEXT.__const: 0x10
   __TEXT_EXEC.__text: 0xd3e8
CStrings:
+ "379.0.2"
- "379"

```

>  `com.apple.driver.AppleSmartBatteryManagerEmbedded`

```diff

-1735.0.0.0.0
+1739.0.0.0.0
   __TEXT.__cstring: 0x447a
   __TEXT.__const: 0x15f0
-  __TEXT.__os_log: 0x25f9
-  __TEXT_EXEC.__text: 0x228a0
+  __TEXT.__os_log: 0x2616
+  __TEXT_EXEC.__text: 0x228ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x208
   __DATA.__common: 0x150

   __DATA_CONST.__kalloc_type: 0x340
   Functions: 385
   Symbols:   0
-  CStrings:  910
+  CStrings:  911
 
CStrings:
+ "failed to read shutdownData\n"

```

>  `com.apple.driver.FairPlayIOKit`

```diff

 72.8.0.0.0
   __TEXT.__cstring: 0x1c95
-  __TEXT.__const: 0x49c10
-  __TEXT_EXEC.__text: 0x1b0660
+  __TEXT.__const: 0x49c30
+  __TEXT_EXEC.__text: 0x1bb260
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x12e0
+  __DATA.__data: 0x12d0
   __DATA.__common: 0x5fd8
   __DATA.__bss: 0x38
   __DATA_CONST.__auth_got: 0x218

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x13860
+  __DATA_CONST.__const: 0x13ae0
   __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x370
-  Functions: 461
+  Functions: 486
   Symbols:   0
   CStrings:  87
 

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

-6769.0.0.0.0
-  __TEXT.__cstring: 0x32b45
-  __TEXT.__os_log: 0x2db0c
+6769.0.4.0.0
+  __TEXT.__cstring: 0x331d4
+  __TEXT.__os_log: 0x2dd91
   __TEXT.__const: 0x7f0
-  __TEXT_EXEC.__text: 0x18d2bc
+  __TEXT_EXEC.__text: 0x18ef54
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
   __DATA.__common: 0x1238

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x3a0
   __DATA_CONST.__mod_term_func: 0x3a0
-  __DATA_CONST.__const: 0x1d998
+  __DATA_CONST.__const: 0x1da00
   __DATA_CONST.__kalloc_type: 0x1d40
   __DATA_CONST.__kalloc_var: 0xaf0
-  Functions: 4758
+  Functions: 4763
   Symbols:   0
-  CStrings:  4749
+  CStrings:  4770
 
CStrings:
+ "\"bootarg acio=0x40 is deprecated (bit 6), please use new boot-arg acio_fw_panic=0x3. (bit 0 for assert on retrain, bit 1 for assert on training timeout)\\n\" @%s:%d"
+ "\"dfp\\n\" @%s:%d"
+ "%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::initWithController acio_fw_panic: 0x%08x\n"
+ "%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::initWithController acio_fw_panic: 0x%08x\n"
+ "%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::preConfigureRouter - writing acio_fw_panic 0x%08x\n"
+ "%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::preConfigureRouter - writing acio_fw_panic 0x%08x\n"
+ "%lldus IOThunderboltSwitchOS(%x@%llx)::setupTMU - Time Synchronization Protocol Not Supported (TSNS) bit is set.\n"
+ "%lldus IOThunderboltSwitchOS(%x@%llx)::setupTMU - Time Synchronization Protocol Not Supported (TSNS) bit is set.\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - 0 status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - 1 status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - 2 status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - 3 status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - 4 status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - 5 status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - 6 status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - 7 status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - Failed to get expected negotiated width (Expected=0x%llx dfp_negotiated_width=0x%llx status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - Failed to get expected negotiated width (Expected=0x%llx ufp_negotiated_width=0x%llx status=0x%08x).\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::getRequiredTMUMode - fTimeSyncNotSupported = true, disabling TMU\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::getRequiredTMUMode - fTimeSyncNotSupported = true, disabling TMU\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::resetChild - requestPowerDown of child=(%x@%llx)\n"
+ "21:17:53"
+ "IOThunderboltSwitchDelegateACIO.cpp"
+ "Jul 15 2024"
+ "acio_fw_panic"
- "%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::postConfigureRouter - write assert on retraining, offset = 0x%x data = 0x%08x - status = 0x%08x\n"
- "%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::postConfigureRouter - write assert on retraining, offset = 0x%x data = 0x%08x - status = 0x%08x\n"
- "20:29:14"
- "Jul  3 2024"

```

</details>

## MachO

### 🆕 NEW (4)

- `/System/Library/ExtensionKit/Extensions/BluetoothSettingsAppIntentsWidgetExtension.appex/BluetoothSettingsAppIntentsWidgetExtension`
- `/System/Library/ExtensionKit/Extensions/LLMCacheSELFIngestor.appex/LLMCacheSELFIngestor`
- `/System/Library/ExtensionKit/Extensions/NLPLearnerExtension.appex/NLPLearnerExtension`
- `/System/Library/ExtensionKit/Extensions/SoundAndHapticsControls.appex/SoundAndHapticsControls`

### ❌ Removed (7)

- `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`
- `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`
- `/private/var/staged_system_apps/Image Playground.app/Image Playground`
- `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`
- `/usr/lib/libLogRedirect.dylib`
- `/usr/lib/libffi-trampolines.dylib`
- `/usr/lib/libglInterpose.dylib`

### ⬆️ Updated (780)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AXUIViewService.app/AXUIViewService](MACHOS/AXUIViewService.md)
- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/BarcodeScanner.app/Extensions/BarcodeScannerCaptureExtension.appex/BarcodeScannerCaptureExtension](MACHOS/BarcodeScannerCaptureExtension.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/Camera.app/PlugIns/LauncherControlExtension.appex/LauncherControlExtension](MACHOS/LauncherControlExtension.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/DDActionsService.app/DDActionsService](MACHOS/DDActionsService.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3744.appex/Diagnostic-3744](MACHOS/Diagnostic-3744.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262](MACHOS/Diagnostic-8262.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264](MACHOS/Diagnostic-8264.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340](MACHOS/Diagnostic-8340.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Frameworks/DiagnosticsSupport.framework/DiagnosticsSupport](MACHOS/DiagnosticsSupport.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HearingApp.app/HearingApp](MACHOS/HearingApp.md)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/LimitedAccessPromptView.app/LimitedAccessPromptView](MACHOS/LimitedAccessPromptView.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MomentsUIService.app/Frameworks/MomentsUIServiceCore.framework/MomentsUIServiceCore](MACHOS/MomentsUIServiceCore.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/MusicRecognition.app/PlugIns/MusicRecognitionControls.appex/MusicRecognitionControls](MACHOS/MusicRecognitionControls.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/RecoverDeviceUI.app/RecoverDeviceUI](MACHOS/RecoverDeviceUI.md)
- [/Applications/RemotePaymentPassActionsService.app/RemotePaymentPassActionsService](MACHOS/RemotePaymentPassActionsService.md)
- [/Applications/ReplayKitAngel.app/ReplayKitAngel](MACHOS/ReplayKitAngel.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharedWebCredentialViewService.app/SharedWebCredentialViewService](MACHOS/SharedWebCredentialViewService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI.md)
- [/Applications/ShortcutsViewService.app/ShortcutsViewService](MACHOS/ShortcutsViewService.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/StickerPickerService.app/StickerPickerService](MACHOS/StickerPickerService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/SystemActions.app/SystemActions](MACHOS/SystemActions.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVRemoteUIService.app/PlugIns/TVRemoteIntentExtension.appex/TVRemoteIntentExtension](MACHOS/TVRemoteIntentExtension.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/usr/lib/system/libdispatch_debug.dylib](MACHOS/libdispatch_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libdispatch_profile.dylib](MACHOS/libdispatch_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXAVSPluginService.axuiservice/AXAVSPluginService](MACHOS/AXAVSPluginService.md)
- [/System/Library/AccessibilityBundles/AXAggregateStatisticsServer.axuiservice/AXAggregateStatisticsServer](MACHOS/AXAggregateStatisticsServer.md)
- [/System/Library/AccessibilityBundles/AXAssetAndDataServer.axuiservice/AXAssetAndDataServer](MACHOS/AXAssetAndDataServer.md)
- [/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer](MACHOS/AXHapticMusicServer.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/AXUltronPluginService.axuiservice/AXUltronPluginService](MACHOS/AXUltronPluginService.md)
- [/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer](MACHOS/GAXBackboardServer.md)
- [/System/Library/AccessibilityBundles/GAXClient.bundle/GAXClient](MACHOS/GAXClient.md)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer.md)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/NTKCustomization.axbundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion](MACHOS/NanoTimeKitCompanion.md)
- [/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer](MACHOS/SpeakServer.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow.md)
- [/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner](MACHOS/JournalDataclassOwner.md)
- [/System/Library/Accounts/Notification/ASDAccountNotificationPlugin.bundle/ASDAccountNotificationPlugin](MACHOS/ASDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CloudDocsAccountNotificationPlugin.bundle/CloudDocsAccountNotificationPlugin](MACHOS/CloudDocsAccountNotificationPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ClockFlowPlugin.bundle/ClockFlowPlugin](MACHOS/ClockFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge.md)
- [/System/Library/Audio/MIDI Drivers/AppleIDAMDriver.plugin/AppleIDAMDriver](MACHOS/AppleIDAMDriver.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver](MACHOS/AppleMIDIUSBDriver.md)
- [/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver](MACHOS/YamahaUSBMIDIDriver.md)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/ContinuousExposeModule.bundle/ContinuousExposeModule](MACHOS/ContinuousExposeModule.md)
- [/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule](MACHOS/VideoConferenceControlCenterModule.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/CommandAndControl.app/CommandAndControl](MACHOS/CommandAndControl.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer](MACHOS/ScreenSharingServer.md)
- [/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension](MACHOS/ShortcutsTopHitsExtension.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration](MACHOS/AccessibilityDataMigration.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/CallHistoryDataMigrator.migrator/CallHistoryDataMigrator](MACHOS/CallHistoryDataMigrator.md)
- [/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator](MACHOS/MobileActivationMigrator.md)
- [/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator](MACHOS/SystemAppMigrator.md)
- [/System/Library/DistributedEvaluation/Plugins/PMLDESPlugin.desPlugin/PMLDESPlugin](MACHOS/PMLDESPlugin.md)
- [/System/Library/DriverExtensions/XboxGamepad.dext/XboxGamepad](MACHOS/XboxGamepad.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension](MACHOS/CameraSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ClassKitAppIntents.appex/ClassKitAppIntents](MACHOS/ClassKitAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension](MACHOS/DevicePropertiesExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension](MACHOS/ExperimentationExtension.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin](MACHOS/FedStatsMLHostPlugin.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA](MACHOS/FedStatsMLHostPluginClassA.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB](MACHOS/FedStatsMLHostPluginClassB.md)
- [/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents](MACHOS/GeneralSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/IFTelemetrySELFIngestor.appex/IFTelemetrySELFIngestor](MACHOS/IFTelemetrySELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/IntelligenceIntentsExtension.appex/IntelligenceIntentsExtension](MACHOS/IntelligenceIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/MKRemoteUI](MACHOS/MKRemoteUI.md)
- [/System/Library/ExtensionKit/Extensions/MailSettingsIntentsExtension.appex/MailSettingsIntentsExtension](MACHOS/MailSettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MapsTransactionInsightsExtension.appex/MapsTransactionInsightsExtension](MACHOS/MapsTransactionInsightsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MessagesSettingsWidgetKitExtension.appex/MessagesSettingsWidgetKitExtension](MACHOS/MessagesSettingsWidgetKitExtension.md)
- [/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension](MACHOS/MetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicUIEngagementExtension.appex/MusicUIEngagementExtension](MACHOS/MusicUIEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLAppEmbedding.appex/PFLASLAppEmbedding](MACHOS/PFLASLAppEmbedding.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLArcadeRanking.appex/PFLASLArcadeRanking](MACHOS/PFLASLArcadeRanking.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLArcadeRetention.appex/PFLASLArcadeRetention](MACHOS/PFLASLArcadeRetention.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLExperimental.appex/PFLASLExperimental](MACHOS/PFLASLExperimental.md)
- [/System/Library/ExtensionKit/Extensions/PFLCSLAppStore.appex/PFLCSLAppStore](MACHOS/PFLCSLAppStore.md)
- [/System/Library/ExtensionKit/Extensions/PFLCSLAppStore2.appex/PFLCSLAppStore2](MACHOS/PFLCSLAppStore2.md)
- [/System/Library/ExtensionKit/Extensions/PersonalHotspotControlExtension.appex/PersonalHotspotControlExtension](MACHOS/PersonalHotspotControlExtension.md)
- [/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin](MACHOS/PhotosPFLPlugin.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService](MACHOS/PrivateMLClientInferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/ProactiveShareSheetLighthouseBackgroundPlugin.appex/ProactiveShareSheetLighthouseBackgroundPlugin](MACHOS/ProactiveShareSheetLighthouseBackgroundPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin](MACHOS/SiriSuggestionsLightHousePlugin.md)
- [/System/Library/ExtensionKit/Extensions/ToggleAirplaneModeExtension.appex/ToggleAirplaneModeExtension](MACHOS/ToggleAirplaneModeExtension.md)
- [/System/Library/ExtensionKit/Extensions/ToggleCellularDataModeExtension.appex/ToggleCellularDataModeExtension](MACHOS/ToggleCellularDataModeExtension.md)
- [/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension](MACHOS/WiFiSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension](MACHOS/ZeoliteExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat](MACHOS/com.apple.fskit.exfat.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker](MACHOS/com.apple.mlhost.CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_iosd](MACHOS/apfs_iosd.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/slurpAPFSMeta](MACHOS/slurpAPFSMeta.md)
- [/System/Library/Filesystems/apfs.fs/sm_stats](MACHOS/sm_stats.md)
- [/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService](MACHOS/AVAudioDeviceTestService.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/CFNetwork.framework/AuthBrokerAgent](MACHOS/AuthBrokerAgent.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetworkAgent](MACHOS/CFNetworkAgent.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/ClassKit.framework/progressd](MACHOS/progressd.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationMapLNPromptPlugin.appex/CoreLocationMapLNPromptPlugin](MACHOS/CoreLocationMapLNPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin](MACHOS/CoreLocationNumberedMapCalloutPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice](MACHOS/eedmediaservice.md)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice](MACHOS/maphelperservice.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/financed](MACHOS/financed.md)
- [/System/Library/Frameworks/HealthKit.framework/healthd](MACHOS/healthd.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl](MACHOS/MechPearl.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId](MACHOS/MechTouchId.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM](MACHOS/ModuleACM.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/XPCAcmeService.xpc/XPCAcmeService](MACHOS/XPCAcmeService.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitDataExport.xpc/SensorKitDataExport](MACHOS/SensorKitDataExport.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/DualSenseHIDServicePlugin](MACHOS/DualSenseHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/DualShock4HIDServicePlugin](MACHOS/DualShock4HIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/GenericGamepadHIDServicePlugin](MACHOS/GenericGamepadHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/JoyConHIDServicePlugin](MACHOS/JoyConHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/LunaHIDServicePlugin](MACHOS/LunaHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxGamepadHIDServicePlugin.plugin/XboxGamepadHIDServicePlugin](MACHOS/XboxGamepadHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin](MACHOS/XboxOneHIDServicePlugin.md)
- [/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics](MACHOS/IOAnalytics.md)
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
- [/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS](MACHOS/SatelliteSMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/PlugIns/iMessageLite.imservice/iMessageLite](MACHOS/iMessageLite.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageEffects/CKEchoEffect.bundle/CKEchoEffect](MACHOS/CKEchoEffect.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/SessionTrackerAppSettings.bundle/SessionTrackerAppSettings](MACHOS/SessionTrackerAppSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings](MACHOS/CSLCompanionLiveActivitiesSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionStingSettings.bundle/CompanionStingSettings](MACHOS/CompanionStingSettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/DepthCompanionSetup.bundle/DepthCompanionSetup](MACHOS/DepthCompanionSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthBridgeSetupPlugin.bundle/HealthBridgeSetupPlugin](MACHOS/HealthBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoSleepBridgeSetup.bundle/NanoSleepBridgeSetup](MACHOS/NanoSleepBridgeSetup.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings](MACHOS/AirPlayAndHandoffSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/ClassKitSettings.bundle/ClassKitSettings](MACHOS/ClassKitSettings.md)
- [/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings](MACHOS/ContactsSettings.md)
- [/System/Library/PreferenceBundles/ControlCenterSettings.bundle/ControlCenterSettings](MACHOS/ControlCenterSettings.md)
- [/System/Library/PreferenceBundles/DriverKitSettings.bundle/DriverKitSettings](MACHOS/DriverKitSettings.md)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings.md)
- [/System/Library/PreferenceBundles/FontSettings.bundle/FontSettings](MACHOS/FontSettings.md)
- [/System/Library/PreferenceBundles/HomeSettings.bundle/HomeSettings](MACHOS/HomeSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/ManagedConfigurationUI.bundle/ManagedConfigurationUI](MACHOS/ManagedConfigurationUI.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MusicSettings.bundle/MusicSettings](MACHOS/MusicSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PasswordsSettings.bundle/PasswordsSettings](MACHOS/PasswordsSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings.md)
- [/System/Library/PreferenceBundles/ScreenTimeSettings.bundle/ScreenTimeSettings](MACHOS/ScreenTimeSettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PodcastsUsagePlugin.bundle/PodcastsUsagePlugin](MACHOS/PodcastsUsagePlugin.md)
- [/System/Library/PreferenceBundles/UsageSettings.bundle/UsageSettings](MACHOS/UsageSettings.md)
- [/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings](MACHOS/VoiceControlSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceBundles/iBooksSettings.bundle/iBooksSettings](MACHOS/iBooksSettings.md)
- [/System/Library/PreferencesSyncBundles/CoreLocationSync.bundle/CoreLocationSync](MACHOS/CoreLocationSync.md)
- [/System/Library/PreferencesSyncBundles/FindMyDevicePreferencesSync.bundle/FindMyDevicePreferencesSync](MACHOS/FindMyDevicePreferencesSync.md)
- [/System/Library/PreferencesSyncBundles/ScreenTimePreferencesSyncCompanion.bundle/ScreenTimePreferencesSyncCompanion](MACHOS/ScreenTimePreferencesSyncCompanion.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd](MACHOS/motiontrackingd.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKSecondFactorEntryAlert.appex/AKSecondFactorEntryAlert](MACHOS/AKSecondFactorEntryAlert.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProvider.appex/com.apple.CloudDocs.MobileDocumentsFileProvider](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.appex/com.apple.CloudDocs.MobileDocumentsFileProviderManaged](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider](MACHOS/com.apple.CloudDocs.iCloudDriveFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged](MACHOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd](MACHOS/com.apple.sbd.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd](MACHOS/assistant_cdmd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService](MACHOS/ACCHWComponentAuthService.md)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCFeatureAudioProductService.xpc/ACCFeatureAudioProductService](MACHOS/ACCFeatureAudioProductService.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/XPCServices/TilesService.xpc/TilesService](MACHOS/TilesService.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/PlugIns/SearchPoirotExtension.appex/SearchPoirotExtension](MACHOS/SearchPoirotExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd](MACHOS/speechmodeltrainingd.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent](MACHOS/LeakAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/RemoteInjectionAgent](MACHOS/RemoteInjectionAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTConditionInducerSupportService.xpc/com.apple.dt.DTConditionInducerSupportService](MACHOS/com.apple.dt.DTConditionInducerSupportService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity](MACHOS/com.apple.dt.instruments.dtsecurity.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ShortcutsDiagnosticExtension.appex/ShortcutsDiagnosticExtension](MACHOS/ShortcutsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/DoubleAgent.framework/doubleagentd](MACHOS/doubleagentd.md)
- [/System/Library/PrivateFrameworks/DragUI.framework/Support/druid](MACHOS/druid.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored](MACHOS/facetimemessagestored.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension](MACHOS/FileProviderDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealth_client](MACHOS/finhealth_client.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceBTDiscoveryXPCService.xpc/FindMyDeviceBTDiscoveryXPCService](MACHOS/FindMyDeviceBTDiscoveryXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEmergencyCallInfoPublisherXPCService.xpc/FindMyDeviceEmergencyCallInfoPublisherXPCService](MACHOS/FindMyDeviceEmergencyCallInfoPublisherXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/FindMyDeviceEraseXPCService](MACHOS/FindMyDeviceEraseXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService](MACHOS/FindMyDeviceHelperXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/FindMyDeviceIdentityXPCService](MACHOS/FindMyDeviceIdentityXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceUserNotificationsXPCService.xpc/FindMyDeviceUserNotificationsXPCService](MACHOS/FindMyDeviceUserNotificationsXPCService.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterDashboardExtension.appex/GameCenterDashboardExtension](MACHOS/GameCenterDashboardExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond](MACHOS/revisiond.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd](MACHOS/generativeexperiencesd.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd](MACHOS/geoanalyticsd.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/MapsOfflineService.bundle/MapsOfflineService](MACHOS/MapsOfflineService.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/geod](MACHOS/geod.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/XPCServices/healthappworkd.xpc/healthappworkd](MACHOS/healthappworkd.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed](MACHOS/homed.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent](MACHOS/IMDMessageServicesAgent.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd](MACHOS/intelligencecontextd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics](MACHOS/IntelligenceFlowDiagnostics.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd](MACHOS/intelligenceflowd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/PlugIns/MacinTalkAUSP.appex/MacinTalkAUSP](MACHOS/MacinTalkAUSP.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd](MACHOS/mapspushd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService](MACHOS/MediaAnalysisBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService](MACHOS/com.apple.photos.ImageConversionService.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService](MACHOS/com.apple.photos.VideoConversionService.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/Support/mediaartworkd](MACHOS/mediaartworkd.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleEmbeddedAccessoryUpdaterService.xpc/AppleEmbeddedAccessoryUpdaterService](MACHOS/AppleEmbeddedAccessoryUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU](MACHOS/UARPUpdaterServiceDFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService](MACHOS/ManifestStorageService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService](MACHOS/com.apple.MobileInstallationHelperService.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd](MACHOS/modelcatalogd.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent](MACHOS/NPKCompanionAgent.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond](MACHOS/nanotimekitcompaniond.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PlugIns/PhotosStoryDiagnostics.appex/PhotosStoryDiagnostics](MACHOS/PhotosStoryDiagnostics.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/com.apple.PowerlogCore.diagnosticextension.appex/com.apple.PowerlogCore.diagnosticextension](MACHOS/com.apple.PowerlogCore.diagnosticextension.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool](MACHOS/com.apple.PrintKit.PrinterTool.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin](MACHOS/DPMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB](MACHOS/DPMLRuntimePluginClassB.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU](MACHOS/DPMLRuntimePluginNonDnU.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/prototyped](MACHOS/prototyped.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber](MACHOS/ManagedAppsSubscriber.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper](MACHOS/STSXPCHelper.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/screentimediagnose](MACHOS/screentimediagnose.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/PlugIns/ScreenTimeDeviceActivityMonitorExtension.appex/ScreenTimeDeviceActivityMonitorExtension](MACHOS/ScreenTimeDeviceActivityMonitorExtension.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd](MACHOS/liveactivitiesd.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/budd](MACHOS/budd.md)
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/Support/swcutil](MACHOS/swcutil.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/XPCServices/SAExtensionOrchestrator.xpc/SAExtensionOrchestrator](MACHOS/SAExtensionOrchestrator.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsInternalXPCServices.xpc/SiriSuggestionsInternalXPCServices](MACHOS/SiriSuggestionsInternalXPCServices.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/com.apple.SiriTTSService.TrialProxy](MACHOS/com.apple.SiriTTSService.TrialProxy.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTraining](MACHOS/SiriTTSTraining.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent](MACHOS/SiriTTSTrainingAgent.md)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd](MACHOS/sleepd.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent](MACHOS/StatusKitAgent.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/XPCServices/storagekitfsrunner.xpc/storagekitfsrunner](MACHOS/storagekitfsrunner.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd](MACHOS/syncdefaultsd.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/PlugIns/SiriAUSP.appex/SiriAUSP](MACHOS/SiriAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/PlugIns/KonaSynthesizer.appex/KonaSynthesizer](MACHOS/KonaSynthesizer.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/PlugIns/MauiAUSP.appex/MauiAUSP](MACHOS/MauiAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/PlugIns/VoiceBankingDiagnostics.appex/VoiceBankingDiagnostics](MACHOS/VoiceBankingDiagnostics.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/PlugIns/SWTFollowUpExtension.appex/SWTFollowUpExtension](MACHOS/SWTFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd](MACHOS/siriactionsd.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/PlugIns/CollectionsPoster.appex/CollectionsPoster](MACHOS/CollectionsPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd](MACHOS/watchlistd.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd](MACHOS/webprivacyd.md)
- [/System/Library/PrivateFrameworks/WiFiVelocity.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Snippets/UIPlugins/SiriInferenceFlowsUIPlugin.bundle/SiriInferenceFlowsUIPlugin](MACHOS/SiriInferenceFlowsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/SiriKitUIPlugin](MACHOS/SiriKitUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriPaymentsUIPlugin.bundle/SiriPaymentsUIPlugin](MACHOS/SiriPaymentsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSuggestionsUIPlugin.bundle/SiriSuggestionsUIPlugin](MACHOS/SiriSuggestionsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriVideoUIPlugin.bundle/SiriVideoUIPlugin](MACHOS/SiriVideoUIPlugin.md)
- [/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin](MACHOS/StoreDemoPlugin.md)
- [/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary](MACHOS/MusicLibrary.md)
- [/System/Library/UsageBundles/MusicUsage.bundle/MusicUsage](MACHOS/MusicUsage.md)
- [/System/Library/UserEventPlugins/MemoryMonitor.plugin/MemoryMonitor](MACHOS/MemoryMonitor.md)
- [/System/Library/UserEventPlugins/PerfPowerServicesEventListenerPlugin.plugin/PerfPowerServicesEventListenerPlugin](MACHOS/PerfPowerServicesEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching](MACHOS/com.apple.accessoryd.matching.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeDowntimeNotifications.bundle/com.apple.ScreenTimeDowntimeNotifications](MACHOS/com.apple.ScreenTimeDowntimeNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeNotifications.bundle/com.apple.ScreenTimeNotifications](MACHOS/com.apple.ScreenTimeNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary](MACHOS/BKLibrary.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BookEPUBWebProcessPlugin.bundle/BookEPUBWebProcessPlugin](MACHOS/BookEPUBWebProcessPlugin.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Calculator.app/PlugIns/CalculatorWidget.appex/CalculatorWidget](MACHOS/CalculatorWidget.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/Home](MACHOS/Home.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification](MACHOS/HomeNotification.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Magnifier.app/PlugIns/MagnifierWidgetExtension.appex/MagnifierWidgetExtension](MACHOS/MagnifierWidgetExtension.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker](MACHOS/MediaPicker.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/Passwords.app/Passwords](MACHOS/Passwords.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsNotificationExtension.appex/PodcastsNotificationExtension](MACHOS/PodcastsNotificationExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ThumbnailExtension.appex/ThumbnailExtension](MACHOS/ThumbnailExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDiagnosticExtension.appex/StocksDiagnosticExtension](MACHOS/StocksDiagnosticExtension.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosSettingsWidgetExtension.appex/VoiceMemosSettingsWidgetExtension](MACHOS/VoiceMemosSettingsWidgetExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount](MACHOS/mount.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/footprint](MACHOS/footprint.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/system/introspection/libdispatch.dylib](MACHOS/libdispatch.dylib.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/IOMFB_bics_daemon](MACHOS/IOMFB_bics_daemon.md)
- [/usr/libexec/MobileStorageMounter](MACHOS/MobileStorageMounter.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/PerfPowerServices](MACHOS/PerfPowerServices.md)
- [/usr/libexec/PerfPowerServicesExtended](MACHOS/PerfPowerServicesExtended.md)
- [/usr/libexec/SavageUtil](MACHOS/SavageUtil.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/YonkersUtil](MACHOS/YonkersUtil.md)
- [/usr/libexec/adid](MACHOS/adid.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/aonsensed](MACHOS/aonsensed.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/asd](MACHOS/asd.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/cameracaptured](MACHOS/cameracaptured.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/deferredmediad](MACHOS/deferredmediad.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/demod_helper](MACHOS/demod_helper.md)
- [/usr/libexec/deviceaccessd](MACHOS/deviceaccessd.md)
- [/usr/libexec/diagnosticd](MACHOS/diagnosticd.md)
- [/usr/libexec/diagnosticextensionsd](MACHOS/diagnosticextensionsd.md)
- [/usr/libexec/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/fairplaydeviceidentityd](MACHOS/fairplaydeviceidentityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmybeaconingd](MACHOS/findmybeaconingd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/finish_demo_restore](MACHOS/finish_demo_restore.md)
- [/usr/libexec/fskit_helper](MACHOS/fskit_helper.md)
- [/usr/libexec/fskitd](MACHOS/fskitd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/griddatad](MACHOS/griddatad.md)
- [/usr/libexec/handwritingd](MACHOS/handwritingd.md)
- [/usr/libexec/hangtelemetryd](MACHOS/hangtelemetryd.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/hostapd](MACHOS/hostapd.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/installd](MACHOS/installd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/locationpushd](MACHOS/locationpushd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd_helper](MACHOS/logd_helper.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/lskdd](MACHOS/lskdd.md)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd.md)
- [/usr/libexec/mediasetupd](MACHOS/mediasetupd.md)
- [/usr/libexec/memoryanalyticsd](MACHOS/memoryanalyticsd.md)
- [/usr/libexec/misagent](MACHOS/misagent.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mlruntimed](MACHOS/mlruntimed.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobile_storage_proxy](MACHOS/mobile_storage_proxy.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/passcodenagd](MACHOS/passcodenagd.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/pkd](MACHOS/pkd.md)
- [/usr/libexec/powerexperienced](MACHOS/powerexperienced.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remoted](MACHOS/remoted.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/rsync/rsync.openrsync](MACHOS/rsync.openrsync.md)
- [/usr/libexec/rsync/rsync.samba](MACHOS/rsync.samba.md)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seld](MACHOS/seld.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/storagekitd](MACHOS/storagekitd.md)
- [/usr/libexec/swcd](MACHOS/swcd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/symptomsd](MACHOS/symptomsd.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/tipsd](MACHOS/tipsd.md)
- [/usr/libexec/transparencyStaticKey](MACHOS/transparencyStaticKey.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd.md)
- [/usr/libexec/watchdogd](MACHOS/watchdogd.md)
- [/usr/libexec/wifianalyticsd](MACHOS/wifianalyticsd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTAvrcp](MACHOS/BTAvrcp.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/absd](MACHOS/absd.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/mDNSResponderHelper](MACHOS/mDNSResponderHelper.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (11)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H16.im4p

>  `AppleAVE2FW_H16.im4p`

```diff

 
-  __TEXT.__text: 0xc9560
-  __TEXT.__cstring: 0x12657
-  __TEXT.__const: 0x1f660
+  __TEXT.__text: 0xca520
+  __TEXT.__cstring: 0x12958
+  __TEXT.__const: 0x1f850
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x320
   __TEXT.__constructor: 0x0
-  __DATA.__const: 0x2890
+  __DATA.__const: 0x28c8
   __DATA.__data: 0x1238
   __DATA._rtk_patchbay: 0x1e8
   __DATA._rtk_init_stack: 0x10000

   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xc68b8
   Functions: 0
-  Symbols:   1453
-  CStrings:  2231
+  Symbols:   1455
+  CStrings:  2246
 
Symbols:
+ _AVE_SNPrintf
+ __ZN11RateControl17updateRateControlEjj
+ __ZN11RateControl21estimateTranscodeBitsER10FrameStats
+ __ZN15CMCTFController9SetMEPipeEP18AVE_PICMGMT_PARAMS
+ __ZN16LinearRegression4initEfff
+ __ZN16LinearRegression6updateEff
+ __ZN8HEVC_VPS13vps_extensionEP15HEVC_VUI_PARAMS
+ __ZN8HEVC_VPS31video_header_parameter_set_rbspEP15HEVC_VUI_PARAMS
+ __ZNK16LinearRegression7predictEf
- __Z12AVE_SNPrintfPciPKcz
- __ZN11RateControl17updateRateControlEj
- __ZN15CMCTFController19AdjustScalingFactorEP18AVE_PICMGMT_PARAMSjPd
- __ZN15CMCTFController9SetMEPipeEv
- __ZN19CFlowControllerBase22AcquireAndTriggerHMESCEv
- __ZN8HEVC_VPS13vps_extensionEv
- __ZN8HEVC_VPS31video_header_parameter_set_rbspEv
CStrings:
+ "%s:%d HRD Init iscbr %d %d %d %d"
+ "%s::%d, alpah %d beta %d v %d output %d"
+ "%s::%s:%d BITBOX (%d %d) Frame[%d] %d %d | %d %d %d %d | %d | inter %d intra %d | %d %d %d %d %d/1000 | LRvar %d"
+ "%s::%s:%d BITBOX (%d %d) cavlcBits %d transcodeBits %d estTranscodeBits %d"
+ "%s::%s:%d BITBOX (%d %d) cavlcBits %d transcodeBits %d estTranscodeBits %d modelParam %d"
+ "%s::%s:%d BITBOX LrmeVarToVar (%d, %d) frameSumOfVar: %d, lowResVar: %d"
+ "%s::%s:%d BITBOX frame %d | estimateAvgVar: pre_avgVar: %d avgVarEstimated: %d"
+ "%s::%s:%d MCTF: StartCount %d-%d-%d-%d, Idle %d-%d-%d-%d-%d"
+ "%s::%s:%d MCTF_Client IDs %lld-%lld-%lld-%lld-%lld "
+ "%s::%s:%d MCTF_Client IDs %lld-%lld-%lld-%lld-%lld trigger: %d-%d-%d-%d"
+ "%s::%s:%d MVHEVC (%d %d) pFrame.bitsFromCAVLC %d pFrame.estimatedTranscodeBits %d"
+ "%s::%s:%d Mctf_Cmds %p %p %p %p %p | %d %d %d %d | %d %d %d %d"
+ "%s::%s:%d fid:%d fnum:%d fDr:%d qp:%d var %d"
+ "%s::%s:%d get NOTIFICATION_GET_LRME_CONTINUE signal, for client %lld"
+ "%s::%s:%d mctf_HMESC %lld: StartCount %d-%d-%d-%d"
+ "%s::%s:%d mctf_LRMEFS %lld: StartCount %d-%d-%d-%d"
+ "%s::%s:%d mctf_LRMERC %lld: StartCount %d-%d-%d-%d"
+ "%s::%s:%d mctf_Pipe %lld: StartCount %d-%d-%d-%d"
+ "%s::%s:%d mctf_Pipe %lld: StartCount %d-%d-%d-%d ex %d-%d %d"
+ "8002.10.0"
+ "BITBOX (%d %d) totalBits %d, estTrancodeBits %d\n"
+ "HEVC COMMON:: stats_DMA_addr:%016llx\n"
+ "HRD"
+ "MCPU maxQP: F (%d) meMem %d %d %d"
+ "estimateTranscodeBits"
+ "predict"
+ "updateRateControl"
- "%s::%s:%d BITBOX (%d %d) Frame[%d] %d %d | %d %d %d %d | %d | inter %d intra %d | %d %d %d %d %d/1000"
- "%s::%s:%d MCTF: StartCount %d-%d-%d, Idle %d-%d-%d-%d"
- "%s::%s:%d MCTF_Client IDs %lld-%lld-%lld-%lld "
- "%s::%s:%d MCTF_Client IDs %lld-%lld-%lld-%lld trigger: %d-%d-%d"
- "%s::%s:%d Mctf_Cmds %p %p %p %p | %d %d %d | %d %d %d"
- "%s::%s:%d mctf_LRMEFS %lld: StartCount %d-%d-%d"
- "%s::%s:%d mctf_LRMERC %lld: StartCount %d-%d-%d"
- "%s::%s:%d mctf_Pipe %lld: StartCount %d-%d-%d"
- "%s::%s:%d mctf_Pipe %lld: StartCount %d-%d-%d ex %d-%d %d"
- "8001.94.0"
- "CamPort %d, OrigSF %s%lld.%02lld, AdjSF %s%lld.%02lld"
- "HEVC COMMON:: stats_DMA_addr:%08x\n"

```

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

 
-  __TEXT.__text: 0x984550
+  __TEXT.__text: 0x9894fc
   __TEXT.__data_copy: 0x100000
-  __TEXT.__const: 0x7fa830
-  __TEXT.__cstring: 0x12746d
+  __TEXT.__const: 0x7fa8b0
+  __TEXT.__cstring: 0x1289c7
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x507ac
   __TEXT.__eh_frame: 0x308
-  __DATA.__const: 0x52ee8
+  __DATA.__const: 0x52fa8
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xdf0b8
   __DATA._rtk_power: 0x3a8

   __DATA.__zerofill: 0x20ded0
   Functions: 0
   Symbols:   0
-  CStrings:  33177
+  CStrings:  33316
 
CStrings:
+ "    ID=%ld, RetainCnt=%d Pool:%s\n"
+ "    NotchFilter1_X En?           %d\n"
+ "    NotchFilter1_Y En?           %d\n"
+ "    NotchFilter2_X En?           %d\n"
+ "    NotchFilter2_Y En?           %d\n"
+ "    Read:                        0x%x\n"
+ "    TempCorr En?                 %d\n"
+ "    Write:                       0x%x\n"
+ "  Default Mode01 Config:\n"
+ "  S%zu TempCorr Sources      [%s, %s]\n"
+ " FOVScale=%0.3f %0.3f dst (norm) (x,y)=(%.3f,%.3f) (w,h)=(%.3f,%.3f) ch=%hhu fr=%i"
+ " From RAW (x,y)=(%d,%d) (w,h)=(%d,%d) ch=%hhu fr=%i"
+ "%s ch %d: ROI %d confidence %f  \n"
+ "%s ch %d: SWITCH DEPTH %d ***** (latency %d, conf %d, ND %d, glass %d)\n"
+ "%s ch %d: defocus(%d): %.1f active:%d targetPos:%d (dist %.1f, %.1f) hyperfocal %d depth %d\n"
+ "%s: %s: citLossSPD %d citLossFullBin %d citLossPri %d\n"
+ "%s: %s: constraints %d %d %d minRD %d linesOffMaxExp %d\n"
+ "%s: GetSafetyState() failed"
+ "%s: SensorTest sifrRDO    calculatedRDO %d clamped to %d for SOC constraint.\n"
+ "%s: constraints %d %d %d minRD %d linesOffMaxExp %d citLoss %d %d %d sRatio %.2f\n"
+ "%s:cfg %u spd err: lumiW %u roi %u %u,SF %u\n"
+ "%s:cfg %u spd err: lumiW %u roi %u %u,SF %u B %u\n"
+ "%s:cfg %u spd err: lumiW %u roi %u %u,SF %u qB %u\n"
+ "%s:cfg %u spd err: lumiW %u roi %u %u,SF %u qB %u B %u\n"
+ "(lumiWidth % 2 == 0)"
+ "03:39:38"
+ "AuxPyrSetup"
+ "BWR_MISS: ch:%zu fc:%d OFT:%llu blk:%d delta:%d sp:%llu blk<delta+DCS[%u]\n"
+ "CRNT[T %2d] [CR %2d] D[%5d] DMSP[%5d] Z[%3d] PFL[%4d] DFPS[%3d] Lux[%s]"
+ "Ch:%zu syncGrp:%d valid FDR data unavailable"
+ "FDR is available for ch %zu but distortion isn't populated %d"
+ "GetProjectorStatus"
+ "GetSplitPDSize"
+ "InitSensorData"
+ "InitSensorDataInfo"
+ "Initializing sensor data info\n"
+ "Jul 12 2024"
+ "LLX"
+ "No stf setting buffers for ch %zu, Dropping this setting"
+ "PeridotProjectorCfgTask"
+ "PeridotProjectorConfigurationTask"
+ "PeridotSensorCfgTask"
+ "PeridotSensorConfigurationTask"
+ "PrintSensorData"
+ "PrintSensorDataInfo"
+ "ProjectorOff"
+ "SDI: Depth Version: %u\n"
+ "SDI: FrameArrival\n"
+ "SDI: FrameArrival idx: %u\n"
+ "SDI: FrameArrival[%u] frameId %u\n"
+ "SDI: FrameArrival[%u] frameMsgSkip %u\n"
+ "SDI: FrameArrival[%u] frameMsgTriggerId %llu\n"
+ "SDI: FrameArrival[%u] frameTimestamp %llu\n"
+ "SDI: FrameRate\n"
+ "SDI: InitSensorData\n"
+ "SDI: Peridot Data\n"
+ "SDI: PeridotFrame\n"
+ "SDI: PeridotFrame idx: %u\n"
+ "SDI: PeridotFrame sec idx: %u\n"
+ "SDI: PeridotStates\n"
+ "SDI: PeridotStates idx: %u\n"
+ "SDI: PeridotStates secidx: %u\n"
+ "SDI: PeridotStates thirdIdx: %u\n"
+ "SDI: PeridotVBD\n"
+ "SDI: PowerSave\n"
+ "SDI: PowerSave idx: %u\n"
+ "SDI: PowerSave powerSaveModeBm: %u\n"
+ "SDI: PowerSave sec idx: %u\n"
+ "SDI: PowerSave wakeupErrorCount: %u\n"
+ "SDI: PowerSave wakeupErrorTimestamp: %llu\n"
+ "SDI: PowerSave wakeupSuccessCount: %u\n"
+ "SDI: PowerSave[%u] powerSaveState %u\n"
+ "SDI: PowerSave[%u] powerSaveStateTimestamp %llu\n"
+ "SDI: PowerSave[%u] timeTillWakeup %u\n"
+ "SDI: PowerSave[%u] wakeUpCheckBm 0x%x\n"
+ "SDI: PowerSave[%u] wakeUpTimestamp %llu\n"
+ "SDI: ReceivedCommands\n"
+ "SDI: ReceivedCommands idx: %u\n"
+ "SDI: ReceivedCommands[%u] receivedCommandParam1 %u\n"
+ "SDI: ReceivedCommands[%u] receivedCommandParam2 %u\n"
+ "SDI: ReceivedCommands[%u] receivedCommandTimeStamp %llu\n"
+ "SDI: ReceivedCommands[%u] receivedCommandType %u\n"
+ "SDI: Streaming\n"
+ "SDI: Streaming idx: %u\n"
+ "SDI: Streaming[%u] isStreaming %u\n"
+ "SDI: Streaming[%u] isStreamingTimestamp %llu\n"
+ "SDI: TOF Data\n"
+ "SDI: TofFrame\n"
+ "SDI: TofMetadata\n"
+ "SDI: TofMetadata hwFaults: %u\n"
+ "SDI: TofMetadata idx: %u\n"
+ "SDI: TofMetadata laserIntensity: %u\n"
+ "SDI: TofMetadata metadataMismatchCount: %u\n"
+ "SDI: TofMetadata tbcnum: %u\n"
+ "SDI: TofMetadata vspad: %u\n"
+ "SDI: TofMetadata[%u] metadataMismatchTimestamp %llu\n"
+ "SDI: Version: %u\n"
+ "SDI: currFrameRateMsgActionId: %llu\n"
+ "SDI: currentFrameRate: %u\n"
+ "SDI: lastFrameRate: %u\n"
+ "SDI: lastFrameRateMsgActionId: %llu\n"
+ "SDI: nextFrameRate: %u\n"
+ "SDI: nextFrameRateMsgActionId: %llu\n"
+ "SDI: peridotFrame[%u] bnkcfgid %u \n"
+ "SDI: peridotFrame[%u] frameIdxSuperframe %u \n"
+ "SDI: peridotFrame[%u] frameIdxTbcSequence %u \n"
+ "SDI: peridotFrame[%u] framesInSuperframe %u \n"
+ "SDI: peridotFrame[%u] framesInTbcSequence %u \n"
+ "SDI: peridotFrame[%u] numOfTempReadings %u \n"
+ "SDI: peridotFrame[%u] pricfgid %u \n"
+ "SDI: peridotFrame[%u] txbankid %u \n"
+ "SDI: peridotStates cfgUpdateId %u \n"
+ "SDI: peridotStates fsyncMode %u \n"
+ "SDI: peridotStates tbclpm %u \n"
+ "SDI: peridotStates[%u] sensorControlState %u \n"
+ "SDI: peridotStates[%u] sensorControlStateTimestamps %llu \n"
+ "SDI: peridotStates[%u] tbcRecoveryState %u \n"
+ "SDI: peridotStates[%u] tbcRecoveryStateTimestamps %llu \n"
+ "SDI: peridotStates[%u] updateConfigState %u \n"
+ "SDI: peridotStates[%u] updateConfigStateTimestamps %llu \n"
+ "SDI: peridotVbd[%u] vbdCoeffs %f \n"
+ "SDI: sensorDataInfoPeridot.peridotFrame.bufferSize     = %u \n"
+ "SDI: sensorDataInfoPeridot.peridotFrame.idx            = %u \n"
+ "SDI: sensorDataInfoPeridot.peridotFrame.secBufferSize  = %u \n"
+ "SDI: sensorDataInfoPeridot.peridotFrame.secIdx         = %u \n"
+ "SDI: sensorDataInfoPeridot.peridotStates.bufferSize    = %u \n"
+ "SDI: sensorDataInfoPeridot.peridotStates.idx           = %u \n"
+ "SDI: sensorDataInfoPeridot.peridotStates.secBufferSize = %u \n"
+ "SDI: sensorDataInfoPeridot.peridotStates.secIdx        = %u \n"
+ "SDI: tofFrame actualFrameRate %f \n"
+ "SDI: tofFrame idx: %u\n"
+ "SDI: tofFrame[%u] dmaCompleteLowPTimestamp %llu (%llu)\n"
+ "SDI: tofFrame[%u] dmaCompleteTimestamp     %llu (%llu)\n"
+ "SDI: tofFrame[%u] dmaStartTimestamp        %llu (0)\n"
+ "SDI: tofFrame[%u] superFrameInTBC %u\n"
+ "Scaler %d (%d %d) --> (%d %d)"
+ "Scaler %d upscale more than 8x, (%d %d) -> (%d %d)"
+ "TMH9: Collected ch %zu frmidx %u tag %u chInSync %u bPreviewCh %u bStatsMsCh %u\n"
+ "TMH9: From Channel Start to TM receiving first frame, it takes total %.2fms\n"
+ "TMH9: From Create Session to first channel start, it takes total %.2fms\n"
+ "TMH9: Set preview master ch %hhu\n"
+ "TMH9: Snapshot chMaskStill 0x%x\n"
+ "TMH9: Snapshot chMaskStill 0x%x with numOfReqFrames 0\n"
+ "TMH9: Snapshot multibit %u, mask %x ch %u qSize %zu numOfReqFrames %u\n"
+ "[%s] CH = 0x%zu ae strobe masterCh %zu, statsMaster %zu, statsMode %u\n"
+ "[DSI] Failed to create peridot projector task"
+ "[DSI] Processing projector command: POWER_OFF\n"
+ "bufferSizeDPC=%zu MaxDPCDefectPixelCount=%d"
+ "ch %zu Adaptive Switch force StatsPipe to use preview scaler %u"
+ "ch %zu DistOverlayCalDataGet returns err %d"
+ "ch %zu InitLens called ret=%d"
+ "ch %zu stream hires mode retain depth to be %zu"
+ "ch %zu: SIFR minRD %d fullbin_citloss %u rdoC %d primary_citloss %d\n"
+ "ch %zu: SPD llspd %d %d spd_citloss %u spdMode %d\n"
+ "ch=%ld, CIC_CMD_SCALER_OUTPUT_PROPERTY_SET -> scaler %d, PaddingRows %d, refW %d, refH %d"
+ "ch=%ld, config=%d, maxWidth=%d, maxHeight=%d"
+ "chs#sync mismatch: ch %zu frmidx %u chs#sync %u. But last fr ch %u frmidx %u chs#sync %u"
+ "hScale >= 0x2000 && vScale >= 0x2000"
+ "maxSifrCIT %d, minRD %d, vWSec %d ==> maxExpSifr %d"
+ "pDefectList"
+ "pDefectListV2H2"
+ "peridotProjectorLowPrioDoneSema != (SEMA)0"
+ "peridotProjectorLowPrioQuitSema != (SEMA)0"
+ "peridotProjectorLowPrioTask != (TASK)0"
+ "preivewCrop.height <= zoomParam.rawDMASrcCropRect.height"
+ "preivewCrop.width <= zoomParam.rawDMASrcCropRect.width"
+ "scaler < IMAGE_BE_OUTPUT_TOT"
+ "stats previewCrop x %u y %u w %u h %u"
- "                   s: Enable MFDEff for wide/swide transitions \n"
- "                   t: Enable MFDEff for wide/tele transitions \n"
- "    ID=%ld, RetainCnt=%d\n"
- "  Default Mode01 Read Config:    0x%x\n"
- "  Default Mode01 Write Config:   0x%x\n"
- "  S%zu Temp. Corr. Sources       [%s, %s]\n"
- " [%d] [s] [t] [-]: Set use of MFDeff for 1x/3x/5x camera transitions\n"
- " implicitFOVScale=%f dst (norm) (x,y)=(%.3f,%.3f) (w,h)=(%.3f,%.3f) ch=%hhu fr=%i"
- "%s ch %d: defocus(%d): %.1f active:%d targetPos:%d (dist %.1f, %.1f) hyperfocal %d \n"
- "%s: %s: constraints %d %d %d minRD %d linesOffMaxExp %d citLoss %d %d\n"
- "%s: constraints %d %d %d minRD %d linesOffMaxExp %d citLoss %d %d sRatio %.2f\n"
- "00:07:22"
- "Adaptive Switch force StatsPipe to use preview scaler"
- "BWR_MISS: ch:%zu fc:%d OFT:%llu blk:%d delta:%d sp:%llu blk<delta+DCS\n"
- "CRNT[T %2d] [CR %2d] D[%5d] DMSP[%5d] Z[%3d] PFL[%4d] DFPS[%3d]"
- "Jun 28 2024"
- "PeridotConfigurationTask"
- "Set Use of MFDeff for cam transitions\n"
- "TMH9: Set preview master ch %hhu"
- "TMH9: Snapshot multibit %u, mask %x ch %u qSize %zu\n"
- "ValidateTamperTrace"
- "[DSI] Quark isn't powered on"
- "ch %zu: SIFR minRD %d fullbin_citloss %u rdoC %d\n"
- "ch %zu: SPD llspd %d %d spd_citloss %u\n"
- "ch=%ld, config=%d, , maxWidth=%d, maxHeight=%d, maxRawHeight=%d"
- "maxSifrCIT %lld, minRD %d, vW %d ==> maxExpSifr %d"
- "pCollectedFrame[statMasterCh] != nullptr"
- "sentSTFSettingBufCbuf"
- "updateParams=%p, virtFrmWidth = %d"

```

#### agx_a000.bin

>  `agx_a000.bin`

```diff

 
-  __TEXT.__text: 0x5b298
+  __TEXT.__text: 0x5b2a0
   __TEXT.__gxf_shr_code: 0x554
   __TEXT.__gxf_code: 0x1024
   __TEXT.__gxf_code_pad: 0x0
CStrings:
+ "Jul 15 2024 21:20:18"
- "Jul  3 2024 20:30:38"

```

#### agx_b000.bin

>  `agx_b000.bin`

```diff

 
-  __TEXT.__text: 0x5af9c
+  __TEXT.__text: 0x5afa4
   __TEXT.__gxf_shr_code: 0x554
   __TEXT.__gxf_code: 0x1024
   __TEXT.__gxf_code_pad: 0x0
CStrings:
+ "Jul 15 2024 21:22:36"
- "Jul  3 2024 20:32:54"

```

#### agx_b100.bin

>  `agx_b100.bin`

```diff

 
-  __TEXT.__text: 0x5af9c
+  __TEXT.__text: 0x5afa4
   __TEXT.__gxf_shr_code: 0x554
   __TEXT.__gxf_code: 0x1024
   __TEXT.__gxf_code_pad: 0x0
CStrings:
+ "Jul 15 2024 21:23:40"
- "Jul  3 2024 20:33:53"

```

#### aopfw-iphone16aop.RELEASE.im4p

>  `aopfw-iphone16aop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0x12ff1c
-  __TEXT.__const: 0x11da8
-  __TEXT.__cstring: 0x81e0
-  __TEXT.__chain_starts: 0x50
+  __TEXT.__text: 0x1308d4
+  __TEXT.__const: 0x11e00
+  __TEXT.__cstring: 0x81f0
+  __TEXT.__chain_starts: 0x4c
   __TEXT.__eh_frame: 0x40
   __DATA._rtk_boot: 0x3000
   __DATA.__mod_init_func: 0x258

   __DATA._rtk_heap: 0x3b340
   __DATA.__const: 0x132b8
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x7308
-  __DATA._rtk_patchbay: 0x319
+  __DATA.__data: 0x72d8
+  __DATA._rtk_patchbay: 0x325
   __DATA._rtk_power: 0x3b8
   __DATA._spu_service: 0xa20
   __DATA._spu_endpoint: 0xd8

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xd0c90
-  __ETEXT.__StaticInit: 0x7688
-  __ETEXT.__text: 0x396c8
+  __DATA.__zerofill: 0xd0d30
+  __ETEXT.__StaticInit: 0x78c0
+  __ETEXT.__text: 0x388d0
   __ETEXT.__const: 0xdce
   __EDATA.__data: 0x60
-  __OS_LOG.__string: 0x27724
+  __OS_LOG.__string: 0x27722
   __MISC.__apf_list: 0xb0
   __CMA.__cma_log_string: 0x3df8
   Functions: 0
   Symbols:   0
-  CStrings:  3635
+  CStrings:  3636
 
CStrings:
+ "22:18:58"
+ "AppleSPUFirmware-2001.0.12.0.1~22"
+ "Jul 10 2024"
+ "aop-audprovr2 v400.40 built %s %s, %c%c%c%c state"
- "11:21:17"
- "AppleSPUFirmware-2001.0.9~852"
- "aop-audprovr2 v400.39.1 built %s %s, %c%c%c%c state"

```

#### h16x_ane_fw_iaso_d8x.im4p

>  `h16x_ane_fw_iaso_d8x.im4p`

```diff

 
-  __TEXT.__text: 0xaeb24
+  __TEXT.__text: 0xaf324
   __TEXT.__data_copy: 0x8000
   __TEXT.__const: 0xc380
-  __TEXT.__cstring: 0x1ae7d
+  __TEXT.__cstring: 0x1aecd
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA.__zerofill: 0x53eb0
   Functions: 0
   Symbols:   0
-  CStrings:  3300
+  CStrings:  3301
 
CStrings:
+ "19:00:31"
+ "CR idx (%d) not in use, used by %llx event %d alloc at %lld, free at %lld id:%d"
+ "Jul  8 2024"
- "23:16:15"
- "Jun 27 2024"

```

#### sptm.t8122.release.im4p

>  `sptm.t8122.release.im4p`

```diff

-392.0.31.0.1
-  __TEXT.__cstring: 0xc1c4
+392.0.37.0.0
+  __TEXT.__cstring: 0xc3a3
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x6c
   __TEXT.__const: 0x9d0
-  __DATA_CONST.__const: 0x5990
+  __DATA_CONST.__const: 0x59c8
   __LATE_CONST.__late_const: 0x5d5e0
-  __TEXT_EXEC.__text: 0x4742c
+  __TEXT_EXEC.__text: 0x477b0
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6

   __BOOTDATA.__data: 0x14000
   Functions: 0
   Symbols:   1
-  CStrings:  1540
+  CStrings:  1561
 
CStrings:
+ "%s %s PAPT range not found."
+ "%s Caller domain exceeds array dimensions %d"
+ "1197"
+ "VIOLATION_T8110_DART_INVALID_MAP_OPTION"
+ "VIOLATION_T8110_DART_INVALID_TLB_OP_INDEX"
+ "acquire_t8110dart_paddr"
+ "allowed_permissions"
+ "entry_addr"
+ "papt_range_find"
+ "sanitize_integer(dispatch_entry_addr_U.UNSAFE_VALUE)"
+ "set"
+ "state->dart_id"
+ "t8110dart_validation.h"
+ "te"
+ "validate_dispatch_entry_addr"
+ "validate_sptm_dispatch_table_id"
+ "validate_t8110dart_dart_id"
+ "validate_t8110dart_dart_instance"
+ "validate_t8110dart_dva"
+ "validate_t8110dart_err_mask"
+ "validate_t8110dart_map_nbytes"
+ "validate_t8110dart_map_options"
+ "validate_t8110dart_poller"
+ "validate_t8110dart_sid"
+ "validate_t8110dart_smmu_instance"
+ "validate_t8110dart_smmu_stt_index"
+ "validate_t8110dart_smmu_window"
+ "validate_t8110dart_target_level"
+ "validate_t8110dart_tlb_op"
+ "validate_t8110dart_tlb_op_index"
+ "validate_t8110dart_unmap_options"
+ "way"
+ "xnu ro pagetable page #%d is not SPTM owned, but %x"
- "%s: IOMMU %s with id %d attempted to register illegal mapping (mapping_type: %d, allowed_permissions: %d)"
- "%s: invalid dispatch table id %d"
- "1200"
- "dispatch_entry"
- "op"
- "sptm_t8110dart_clear_all_interrupts"
- "sptm_t8110dart_clear_perf_interrupts"
- "sptm_t8110dart_sk_power_assert"
- "sptm_t8110dart_sk_power_release"
- "sptm_t8110dart_sk_tlbi_barier"
- "sptm_t8110dart_sk_tlbi_request"
- "xnu ro pagetable page #%d is not XNU owned, but %x"

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2ddbf4
-  __TEXT.__const: 0x7ceb4
-  __TEXT.__cstring: 0x30d64
+  __TEXT.__text: 0x2ddff0
+  __TEXT.__const: 0x7cef0
+  __TEXT.__cstring: 0x30d1b
   __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x4a3f8
+  __DATA.__const: 0x4a418
   __DATA._rtk_patchbay: 0x710
   __DATA._rtk_data_uuid: 0x40
   __DATA.__data: 0x2b524

   __DATA.__mod_init_func: 0x88
   __DATA._afk_sys_objt: 0xbb0
   __DATA._rtk_mtab: 0x5c8
-  __DATA.__zerofill: 0x9b210
+  __DATA.__zerofill: 0x9b230
   __OS_LOG.__string: 0x20f90
   Functions: 0
   Symbols:   0
CStrings:
+ "%s: Trinity0DBLC changing from %s to %s\n"
+ "%s: display HPD asserted.\n"
+ "%s: display HPD removed\n"
+ "UPBlock_PCC0DBLC_v1.cpp"
+ "Wait for one frame after alpm disable\n"
+ "plug gated: modeset received.\n"
+ "program_dynamic_regs"
+ "unplug_gated"
- "%s: %s \n"
- "%s: display HPD asserted%s\n"
- ": false"
- "GetSinkSerialNumber"
- "auto UnifiedPipeline::videointerface_init()::(anonymous class)::operator()(void *, VideoInterface::Event, void *, void *) const"
- "color-accuracy-index"
- "display HPD removed"
- "void VideoInterfaceIOAV::unplug_gated(IOAVVideoInterface *)"

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2ddbf4
-  __TEXT.__const: 0x7ceb4
-  __TEXT.__cstring: 0x30d64
+  __TEXT.__text: 0x2ddff0
+  __TEXT.__const: 0x7cef0
+  __TEXT.__cstring: 0x30d1b
   __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x4a3f8
+  __DATA.__const: 0x4a418
   __DATA._rtk_patchbay: 0x710
   __DATA._rtk_data_uuid: 0x40
   __DATA.__data: 0x2b524

   __DATA.__mod_init_func: 0x88
   __DATA._afk_sys_objt: 0xbb0
   __DATA._rtk_mtab: 0x5c8
-  __DATA.__zerofill: 0x9b210
+  __DATA.__zerofill: 0x9b230
   __OS_LOG.__string: 0x20f90
   Functions: 0
   Symbols:   0
CStrings:
+ "%s: Trinity0DBLC changing from %s to %s\n"
+ "%s: display HPD asserted.\n"
+ "%s: display HPD removed\n"
+ "UPBlock_PCC0DBLC_v1.cpp"
+ "Wait for one frame after alpm disable\n"
+ "plug gated: modeset received.\n"
+ "program_dynamic_regs"
+ "unplug_gated"
- "%s: %s \n"
- "%s: display HPD asserted%s\n"
- ": false"
- "GetSinkSerialNumber"
- "auto UnifiedPipeline::videointerface_init()::(anonymous class)::operator()(void *, VideoInterface::Event, void *, void *) const"
- "color-accuracy-index"
- "display HPD removed"
- "void VideoInterfaceIOAV::unplug_gated(IOAVVideoInterface *)"

```

#### txm.iphoneos.release.im4p

>  `txm.iphoneos.release.im4p`

```diff

-135.0.6.0.1
-  __TEXT.__cstring: 0x5781
+135.0.8.0.0
+  __TEXT.__cstring: 0x56e9
   __TEXT.__const: 0x4210
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x20
   __TEXT.__info_plist: 0x508
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x7c98
+  __DATA_CONST.__const: 0x7c78
   __TEXT_EXEC.__text: 0x3f28c
   __TEXT_BOOT_EXEC.__text: 0x4058
   __TEXT_BOOT_EXEC.__bootcode: 0x2c

   __LATE_CONST.__late_const: 0xa8
   Functions: 0
   Symbols:   1
-  CStrings:  711
+  CStrings:  707
 
CStrings:
+ "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Fri Jul 12 01:06:11 PDT 2024; root:AppleImage4_txm-320.0.11~943/libimage4_TXM/RELEASE_ARM64E"
+ "Code Signing Monitor Image4 Module Version 7.0.0: Fri Jul 12 01:06:11 PDT 2024; root:AppleImage4_txm-320.0.11~943/libimage4_TXM/RELEASE_ARM64E"
+ "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-135.0.8"
- "07eaa5cf-fb1e-4c12-942f-c48b4c2d6e3c"
- "67a365aa-20c7-449b-92c4-cbd0f34cb4f6"
- "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Wed Jun 26 17:59:51 PDT 2024; root:AppleImage4_txm-320.0.11~674/libimage4_TXM/RELEASE_ARM64E"
- "Code Signing Monitor Image4 Module Version 7.0.0: Wed Jun 26 17:59:51 PDT 2024; root:AppleImage4_txm-320.0.11~674/libimage4_TXM/RELEASE_ARM64E"
- "e1177153-89cb-4574-ad10-efe8855b54f5"
- "f6d44aa4-39aa-4a68-8b17-72a4759dcf07"
- "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-135.0.6.0.1"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.0 *(22A5307i)* | 619.1.20.10.1 |
| 18.0 *(22A5316j)* | 619.1.22.10.1 |

### Dylibs

#### 🆕 NEW (4)

- `/System/Library/PrivateFrameworks/Human.framework/Human`
- `/System/Library/PrivateFrameworks/HumanUI.framework/HumanUI`
- `/System/Library/PrivateFrameworks/VoiceControl.framework/VoiceControl`
- `/usr/lib/libindus.dylib`

#### ❌ Removed (4)

- `/System/Library/PrivateFrameworks/TestHook.framework/TestHook`
- `/System/Library/PrivateFrameworks/TestHookService.framework/TestHookService`
- `/System/Library/PrivateFrameworks/TestHookShared.framework/TestHookShared`
- `/System/Library/PrivateFrameworks/VisualIntelligenceStream.framework/VisualIntelligenceStream`

#### ⬆️ Updated (1338)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider](DYLIBS/ASMessagesProvider.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettings.axbundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/Library/AccessibilityBundles/AcousticId-Assistant.axbundle/AcousticId-Assistant](DYLIBS/AcousticId-Assistant.md)
- [/System/Library/AccessibilityBundles/ActionButtonSelector.axbundle/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/AccessibilityBundles/AirPlayMirroringModule.axbundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule.md)
- [/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension](DYLIBS/AppInstallExtension.md)
- [/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore](DYLIBS/AppStore.md)
- [/System/Library/AccessibilityBundles/AvatarUI.axbundle/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/Bridge.axbundle/Bridge](DYLIBS/Bridge.md)
- [/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension](DYLIBS/BridgeStoreExtension.md)
- [/System/Library/AccessibilityBundles/Calculator.axbundle/Calculator](DYLIBS/Calculator.md)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/ContactsUI.axbundle/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/AccessibilityBundles/ConversationKit.axbundle/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/AccessibilityBundles/DisplayAndBrightnessSettings.axbundle/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/AccessibilityBundles/Files.axbundle/Files](DYLIBS/Files.md)
- [/System/Library/AccessibilityBundles/FlightUtilities.axbundle/FlightUtilities](DYLIBS/FlightUtilities.md)
- [/System/Library/AccessibilityBundles/FocusUIModule.axbundle/FocusUIModule](DYLIBS/FocusUIModule.md)
- [/System/Library/AccessibilityBundles/HeartRhythmUI.axbundle/HeartRhythmUI](DYLIBS/HeartRhythmUI.md)
- [/System/Library/AccessibilityBundles/MailUI.axbundle/MailUI](DYLIBS/MailUI.md)
- [/System/Library/AccessibilityBundles/Maps.axbundle/Maps](DYLIBS/Maps.md)
- [/System/Library/AccessibilityBundles/Measure.axbundle/Measure](DYLIBS/Measure.md)
- [/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/AccessibilityBundles/MenstrualCyclesAppPlugin.axbundle/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone](DYLIBS/MobilePhone.md)
- [/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework](DYLIBS/MobileSafariFramework.md)
- [/System/Library/AccessibilityBundles/MobileStoreUI.axbundle/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/AccessibilityBundles/Music.axbundle/Music](DYLIBS/Music.md)
- [/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication](DYLIBS/MusicApplication.md)
- [/System/Library/AccessibilityBundles/NFCControlCenterModule.axbundle/NFCControlCenterModule](DYLIBS/NFCControlCenterModule.md)
- [/System/Library/AccessibilityBundles/NotificationsSettings.axbundle/NotificationsSettings](DYLIBS/NotificationsSettings.md)
- [/System/Library/AccessibilityBundles/PassKitUI.axbundle/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/AccessibilityBundles/PhotosUICore.axbundle/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/AccessibilityBundles/PosterKit.axbundle/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/AccessibilityBundles/PreBoard.axbundle/PreBoard](DYLIBS/PreBoard.md)
- [/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension](DYLIBS/ProductPageExtension.md)
- [/System/Library/AccessibilityBundles/QuickSpeak.bundle/QuickSpeak](DYLIBS/QuickSpeak.md)
- [/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/AccessibilityBundles/SaveToFiles.axbundle/SaveToFiles](DYLIBS/SaveToFiles.md)
- [/System/Library/AccessibilityBundles/ScreenshotServicesService.axbundle/ScreenshotServicesService](DYLIBS/ScreenshotServicesService.md)
- [/System/Library/AccessibilityBundles/Setup.axbundle/Setup](DYLIBS/Setup.md)
- [/System/Library/AccessibilityBundles/SleepHealthAppPlugin.axbundle/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardFoundation.axbundle/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/StoreKitUI.axbundle/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/AccessibilityBundles/SwiftUI.axbundle/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/AccessibilityBundles/TVRemoteUI.axbundle/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/AccessibilityBundles/VectorKit.axbundle/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/AccessibilityBundles/VisionKitCore.axbundle/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore](DYLIBS/WebCore.md)
- [/System/Library/AccessibilityBundles/com.apple.DocumentManager.Service-AppExtension.axbundle/com.apple.DocumentManager.Service-AppExtension](DYLIBS/com.apple.DocumentManager.Service-AppExtension.md)
- [/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin](DYLIBS/FindMyDeviceAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule](DYLIBS/DisplayModule.md)
- [/System/Library/ControlCenter/Bundles/HeadphoneAccommodationsCCModule.bundle/HeadphoneAccommodationsCCModule](DYLIBS/HeadphoneAccommodationsCCModule.md)
- [/System/Library/ControlCenter/Bundles/HearingAidsModule.bundle/HearingAidsModule](DYLIBS/HearingAidsModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterCompactModule.bundle/HomeControlCenterCompactModule](DYLIBS/HomeControlCenterCompactModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterSingleTileModule.bundle/HomeControlCenterSingleTileModule](DYLIBS/HomeControlCenterSingleTileModule.md)
- [/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule](DYLIBS/TVRemoteModule.md)
- [/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS](DYLIBS/Communications-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit](DYLIBS/IOKit.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC](DYLIBS/NFC.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost](DYLIBS/USBHost.md)
- [/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0](DYLIBS/AGXMetalG16P_A0.md)
- [/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0](DYLIBS/AGXMetalG16P_B0.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit](DYLIBS/AccessorySetupKit.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit](DYLIBS/AdAttributionKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libValidationCapsule.dylib](DYLIBS/libValidationCapsule.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Cinematic.framework/Cinematic](DYLIBS/Cinematic.md)
- [/System/Library/Frameworks/ClassKit.framework/ClassKit](DYLIBS/ClassKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/ContactProvider.framework/ContactProvider](DYLIBS/ContactProvider.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI](DYLIBS/CoreLocationUI.md)
- [/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI](DYLIBS/CoreMIDI.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/DockKit.framework/DockKit](DYLIBS/DockKit.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit](DYLIBS/ExtensionKit.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameController.framework/GameController](DYLIBS/GameController.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HealthKitUI.framework/HealthKitUI](DYLIBS/HealthKitUI.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI](DYLIBS/LocalAuthenticationEmbeddedUI.md)
- [/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture](DYLIBS/LockedCameraCapture.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/MatterSupport.framework/MatterSupport](DYLIBS/MatterSupport.md)
- [/System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility](DYLIBS/MediaAccessibility.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX.md)
- [/System/Library/Frameworks/MetalKit.framework/MetalKit](DYLIBS/MetalKit.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore](DYLIBS/MPSCore.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/OSLog.framework/OSLog](DYLIBS/OSLog.md)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/Frameworks/PHASE.framework/PHASE](DYLIBS/PHASE.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/ScreenTime.framework/ScreenTime](DYLIBS/ScreenTime.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SensorKit.framework/SensorKit](DYLIBS/SensorKit.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/Social.framework/Social](DYLIBS/Social.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/UserNotifications.framework/UserNotifications](DYLIBS/UserNotifications.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib](DYLIBS/libWebKitSwift.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_HomeKit_SwiftUI.framework/_HomeKit_SwiftUI](DYLIBS/_HomeKit_SwiftUI.md)
- [/System/Library/Frameworks/_Intents_TipKit.framework/_Intents_TipKit](DYLIBS/_Intents_TipKit.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit.md)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/HIDPlugins/IOHIDEventSystemStatistics.plugin/IOHIDEventSystemStatistics](DYLIBS/IOHIDEventSystemStatistics.md)
- [/System/Library/Health/FeedItemPlugins/Categories.healthplugin/Categories](DYLIBS/Categories.md)
- [/System/Library/Health/FeedItemPlugins/HealthRecords.healthplugin/HealthRecords](DYLIBS/HealthRecords.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications](DYLIBS/NanoCompassComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFoghornFaceBundleCompanion.bundle/NTKFoghornFaceBundleCompanion](DYLIBS/NTKFoghornFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGalleonFaceBundleCompanion.bundle/NTKGalleonFaceBundleCompanion](DYLIBS/NTKGalleonFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVivaldiFaceBundleCompanion.bundle/NTKVivaldiFaceBundleCompanion](DYLIBS/NTKVivaldiFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences](DYLIBS/VPNPreferences.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/AFKUser.framework/AFKUser](DYLIBS/AFKUser.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/libORTools.dylib](DYLIBS/libORTools.dylib.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities](DYLIBS/AXMediaUtilities.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI](DYLIBS/AXWatchRemoteScreenUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth](DYLIBS/AccessoryComponentAuth.md)
- [/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim](DYLIBS/AccessoryiAP2Shim.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI](DYLIBS/ActivityAchievementsUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/ActivityProgressKit.framework/ActivityProgressKit](DYLIBS/ActivityProgressKit.md)
- [/System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI](DYLIBS/ActivityRingsUI.md)
- [/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing](DYLIBS/ActivitySharing.md)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient.md)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AeroML.framework/AeroML](DYLIBS/AeroML.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics](DYLIBS/AppInstallationMetrics.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIWidget.framework/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager.md)
- [/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA](DYLIBS/AppleCVA.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport](DYLIBS/AppleDeviceQuerySupport.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libAppleDeviceQueryArmory.dylib](DYLIBS/libAppleDeviceQueryArmory.dylib.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery](DYLIBS/AppleMediaDiscovery.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/AppleSARHelper.framework/AppleSARHelper](DYLIBS/AppleSARHelper.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication](DYLIBS/AppleTracingSupportSymbolication.md)
- [/System/Library/PrivateFrameworks/AskTo.framework/AskTo](DYLIBS/AskTo.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssetExplorer.framework/AssetExplorer](DYLIBS/AssetExplorer.md)
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
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion](DYLIBS/AudiogramIngestion.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/PrivateFrameworks/BarcodeSupportUI.framework/BarcodeSupportUI](DYLIBS/BarcodeSupportUI.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms](DYLIBS/BatteryAlgorithms.md)
- [/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/BiomeFlexibleStorage](DYLIBS/BiomeFlexibleStorage.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl](DYLIBS/BrightnessControl.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService.md)
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
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase](DYLIBS/CalendarDatabase.md)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation](DYLIBS/CalendarFoundation.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/CalendarUIKitInternal](DYLIBS/CalendarUIKitInternal.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CallHistoryToolKit.framework/CallHistoryToolKit](DYLIBS/CallHistoryToolKit.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework](DYLIBS/CarCommandsUIFramework.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices.md)
- [/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices](DYLIBS/CarouselPreferenceServices.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices](DYLIBS/CheckerBoardServices.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
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
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation](DYLIBS/CloudRecommendation.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices](DYLIBS/CloudServices.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards](DYLIBS/ComputeSafeguards.md)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
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
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories](DYLIBS/CoreAccessories.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI](DYLIBS/CoreFollowUpUI.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder](DYLIBS/CoreIDCredBuilder.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf](DYLIBS/CoreLocationProtobuf.md)
- [/System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay](DYLIBS/CoreLocationReplay.md)
- [/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms](DYLIBS/CoreMotionAlgorithms.md)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/CorePrescriptionLite](DYLIBS/CorePrescriptionLite.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO](DYLIBS/CoreRealityIO.md)
- [/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition](DYLIBS/CoreRecognition.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils](DYLIBS/CoreSpeechUtils.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication](DYLIBS/CoreSymbolication.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio](DYLIBS/CoreThreadRadio.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary](DYLIBS/DMCEnrollmentLibrary.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DSContinuityPairing.framework/DSContinuityPairing](DYLIBS/DSContinuityPairing.md)
- [/System/Library/PrivateFrameworks/DTXConnectionServices.framework/DTXConnectionServices](DYLIBS/DTXConnectionServices.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport](DYLIBS/DiagnosticsSupport.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DirectResource.framework/DirectResource](DYLIBS/DirectResource.md)
- [/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration](DYLIBS/DiskArbitration.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb](DYLIBS/DoNotDisturb.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera](DYLIBS/DocumentCamera.md)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/PrivateFrameworks/DoubleAgent.framework/DoubleAgent](DYLIBS/DoubleAgent.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts](DYLIBS/EmergencyAlerts.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/EnergyKitFoundation.framework/EnergyKitFoundation](DYLIBS/EnergyKitFoundation.md)
- [/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState](DYLIBS/EnhancedLoggingState.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/Eyedropper.framework/Eyedropper](DYLIBS/Eyedropper.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFUI.framework/FMFUI](DYLIBS/FMFUI.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FRC.framework/FRC](DYLIBS/FRC.md)
- [/System/Library/PrivateFrameworks/FSEvents.framework/FSEvents](DYLIBS/FSEvents.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
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
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyStorage.framework/FindMyStorage](DYLIBS/FindMyStorage.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessActions.framework/FitnessActions](DYLIBS/FitnessActions.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards](DYLIBS/FitnessAwards.md)
- [/System/Library/PrivateFrameworks/FitnessBrowsing.framework/FitnessBrowsing](DYLIBS/FitnessBrowsing.md)
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
- [/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan](DYLIBS/FitnessWorkoutPlan.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/GESS.framework/GESS](DYLIBS/GESS.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation](DYLIBS/GameControllerFoundation.md)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctions.framework/GenerativeFunctions](DYLIBS/GenerativeFunctions.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics](DYLIBS/GeoAnalytics.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/GeoUIFramework.framework/GeoUIFramework](DYLIBS/GeoUIFramework.md)
- [/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices](DYLIBS/GridDataServices.md)
- [/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices](DYLIBS/H16ISPServices.md)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing](DYLIBS/HDRProcessing.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService](DYLIBS/HeadphoneProxFeatureService.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings](DYLIBS/HeadphoneSettings.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon](DYLIBS/HealthAppHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceAppPlugin.framework/HealthBalanceAppPlugin](DYLIBS/HealthBalanceAppPlugin.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications](DYLIBS/HealthMedications.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin](DYLIBS/HealthMedicationsDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI](DYLIBS/HealthMedicationsVisionUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration](DYLIBS/HealthOrchestration.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService](DYLIBS/HearingModeService.md)
- [/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private](DYLIBS/HearingModeService_Private.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeCommunicationUIFramework.framework/HomeCommunicationUIFramework](DYLIBS/HomeCommunicationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore](DYLIBS/HomeKitBackingStore.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents](DYLIBS/HomeWidgetIntents.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMRCSTransfer.framework/IMRCSTransfer](DYLIBS/IMRCSTransfer.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer](DYLIBS/IOMobileFramebuffer.md)
- [/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost](DYLIBS/IOUSBHost.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
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
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache](DYLIBS/LLMCache.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinguisticData.framework/LinguisticData](DYLIBS/LinguisticData.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription](DYLIBS/LiveTranscription.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI](DYLIBS/LocalAuthenticationPrivateUI.md)
- [/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge](DYLIBS/LocalSpeechRecognitionBridge.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices](DYLIBS/LockedContentServices.md)
- [/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport](DYLIBS/LoggingSupport.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MLAssetIO.framework/MLAssetIO](DYLIBS/MLAssetIO.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime](DYLIBS/MLRuntime.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/MacinTalk](DYLIBS/MacinTalk.md)
- [/System/Library/PrivateFrameworks/MagnifierServices.framework/MagnifierServices](DYLIBS/MagnifierServices.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
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
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal](DYLIBS/MenstrualAlgorithmsInternal.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation](DYLIBS/MicroLocation.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation](DYLIBS/MobileActivation.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage](DYLIBS/MobileStorage.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi](DYLIBS/MobileWiFi.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets](DYLIBS/MorphunAssets.md)
- [/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging](DYLIBS/MotionSensorLogging.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/NLPLearner](DYLIBS/NLPLearner.md)
- [/System/Library/PrivateFrameworks/NanoHomeIntents.framework/NanoHomeIntents](DYLIBS/NanoHomeIntents.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit](DYLIBS/NeutrinoKit.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit](DYLIBS/NewsKit.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/NewsServices](DYLIBS/NewsServices.md)
- [/System/Library/PrivateFrameworks/NewsServicesInternal.framework/NewsServicesInternal](DYLIBS/NewsServicesInternal.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI](DYLIBS/NewsUI.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics](DYLIBS/NotesAnalytics.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSiriUI.framework/NotesSiriUI](DYLIBS/NotesSiriUI.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/Osprey.framework/Osprey](DYLIBS/Osprey.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport](DYLIBS/PBBridgeSupport.md)
- [/System/Library/PrivateFrameworks/PLSnapshot.framework/PLSnapshot](DYLIBS/PLSnapshot.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase](DYLIBS/PaymentUIBase.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI](DYLIBS/PeopleUI.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader](DYLIBS/PerfPowerServicesReader.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait](DYLIBS/PersonalizationPortrait.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit](DYLIBS/PlatterKit.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation](DYLIBS/PosterFoundation.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience](DYLIBS/PowerExperience.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting](DYLIBS/PowerlogAccounting.md)
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
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit.md)
- [/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI](DYLIBS/PrintKitUI.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/PrivateMLClientInferenceProvider](DYLIBS/PrivateMLClientInferenceProvider.md)
- [/System/Library/PrivateFrameworks/ProVideo.framework/ProVideo](DYLIBS/ProVideo.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse](DYLIBS/ProactiveShareSheetDataHarvestingLighthouse.md)
- [/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel](DYLIBS/ProactiveSuggestionClientModel.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProofReader.framework/ProofReader](DYLIBS/ProofReader.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools](DYLIBS/PrototypeTools.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI](DYLIBS/PrototypeToolsUI.md)
- [/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit](DYLIBS/ProxCardKit.md)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI](DYLIBS/RTTUI.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RapportUI.framework/RapportUI](DYLIBS/RapportUI.md)
- [/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion](DYLIBS/RealityFusion.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/RealityKitInspection.framework/RealityKitInspection](DYLIBS/RealityKitInspection.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration](DYLIBS/RemoteConfiguration.md)
- [/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel](DYLIBS/RemoteManagementModel.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects](DYLIBS/SAObjects.md)
- [/System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders](DYLIBS/SCSharingReminders.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing](DYLIBS/SafariSafeBrowsing.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices](DYLIBS/ScreenContinuityServices.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit](DYLIBS/SecureCaptureKit.md)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService](DYLIBS/SecureTransactionService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
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
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials](DYLIBS/SharedWebCredentials.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/SidecarCore.framework/SidecarCore](DYLIBS/SidecarCore.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework](DYLIBS/SiriAppLaunchUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils](DYLIBS/SiriAudioIntentUtils.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI](DYLIBS/SiriAutoCompleteAPI.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriContactsCommon.framework/SiriContactsCommon](DYLIBS/SiriContactsCommon.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCorrections.framework/SiriCorrections](DYLIBS/SiriCorrections.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback](DYLIBS/SiriCrossDeviceArbitrationFeedback.md)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine](DYLIBS/SiriDialogEngine.md)
- [/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher](DYLIBS/SiriEntityMatcher.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver](DYLIBS/SiriReferenceResolver.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriSystemCommandsIntents.framework/SiriSystemCommandsIntents](DYLIBS/SiriSystemCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTaskEngagement.framework/SiriTaskEngagement](DYLIBS/SiriTaskEngagement.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework](DYLIBS/SiriVideoUIFramework.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SnippetUI_Proto.framework/SnippetUI_Proto](DYLIBS/SnippetUI_Proto.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport](DYLIBS/SoftwareUpdateCoreSupport.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution](DYLIBS/SpaceAttribution.md)
- [/System/Library/PrivateFrameworks/SpatialInspectorFoundation.framework/SpatialInspectorFoundation](DYLIBS/SpatialInspectorFoundation.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
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
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit](DYLIBS/StatusKit.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/SymptomLinkAdvisory.framework/SymptomLinkAdvisory](DYLIBS/SymptomLinkAdvisory.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake](DYLIBS/SystemWake.md)
- [/System/Library/PrivateFrameworks/TCC.framework/TCC](DYLIBS/TCC.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/TextToSpeechKonaSupport](DYLIBS/TextToSpeechKonaSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/TextToSpeechMauiSupport](DYLIBS/TextToSpeechMauiSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices](DYLIBS/TipKitServices.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote](DYLIBS/TouchRemote.md)
- [/System/Library/PrivateFrameworks/TraitsArbiter.framework/TraitsArbiter](DYLIBS/TraitsArbiter.md)
- [/System/Library/PrivateFrameworks/Transliteration.framework/Transliteration](DYLIBS/Transliteration.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI](DYLIBS/TransparencyUI.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/Tungsten.framework/Tungsten](DYLIBS/Tungsten.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement](DYLIBS/UserManagement.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/Visage.framework/Visage](DYLIBS/Visage.md)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail](DYLIBS/VisualVoicemail.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WatchdogServiceManagement.framework/WatchdogServiceManagement](DYLIBS/WatchdogServiceManagement.md)
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
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/WebPrivacy](DYLIBS/WebPrivacy.md)
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI.md)
- [/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI](DYLIBS/WelcomeKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity](DYLIBS/WiFiVelocity.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager](DYLIBS/WirelessCoexManager.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness](DYLIBS/WorkflowResponsiveness.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/WritingTools.framework/WritingTools](DYLIBS/WritingTools.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/XavierNews.framework/XavierNews](DYLIBS/XavierNews.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification](DYLIBS/iCloudNotification.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder](DYLIBS/AppleProResHWDecoder.videodecoder.md)
- [/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder](DYLIBS/AppleProResHWEncoder.videoencoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait](DYLIBS/CCPortrait.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1](DYLIBS/IntelligentDistortionCorrectionV1.md)
- [/System/Library/VideoProcessors/NRFV2.bundle/NRFV2](DYLIBS/NRFV2.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/i18n/libiconv_std.dylib](DYLIBS/libiconv_std.dylib.md)
- [/usr/lib/libARI.dylib](DYLIBS/libARI.dylib.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAppleArchive.dylib](DYLIBS/libAppleArchive.dylib.md)
- [/usr/lib/libAppleEXR.dylib](DYLIBS/libAppleEXR.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerDAL.dylib](DYLIBS/libBasebandManagerDAL.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libFDR.dylib](DYLIBS/libFDR.dylib.md)
- [/usr/lib/libFDRDecode.dylib](DYLIBS/libFDRDecode.dylib.md)
- [/usr/lib/libInFieldCollection.dylib](DYLIBS/libInFieldCollection.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libParallelCompression.dylib](DYLIBS/libParallelCompression.dylib.md)
- [/usr/lib/libRoseBooter.dylib](DYLIBS/libRoseBooter.dylib.md)
- [/usr/lib/libSESShared.dylib](DYLIBS/libSESShared.dylib.md)
- [/usr/lib/libSystemHealth.dylib](DYLIBS/libSystemHealth.dylib.md)
- [/usr/lib/libVinylNonUpdater.dylib](DYLIBS/libVinylNonUpdater.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libdns_services.dylib](DYLIBS/libdns_services.dylib.md)
- [/usr/lib/libexslt.0.dylib](DYLIBS/libexslt.0.dylib.md)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libmorphun.dylib](DYLIBS/libmorphun.dylib.md)
- [/usr/lib/libmrc.dylib](DYLIBS/libmrc.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib.md)
- [/usr/lib/libspindump.dylib](DYLIBS/libspindump.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/libxslt.1.dylib](DYLIBS/libxslt.1.dylib.md)
- [/usr/lib/log/liblog_mdns.dylib](DYLIBS/liblog_mdns.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswiftos.dylib](DYLIBS/libswiftos.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libdispatch.dylib](DYLIBS/libdispatch.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_networkextension.dylib](DYLIBS/libsystem_networkextension.dylib.md)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib.md)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib.md)
- [/usr/lib/system/libxpc.dylib](DYLIBS/libxpc.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libRoseUpdater.dylib](DYLIBS/libRoseUpdater.dylib.md)
- [/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib](DYLIBS/libSavageRestoreInfo_iOS.dylib.md)
- [/usr/lib/updaters/libSavageUpdater_iOS.dylib](DYLIBS/libSavageUpdater_iOS.dylib.md)
- [/usr/lib/updaters/libT200Updater.dylib](DYLIBS/libT200Updater.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

### Feature Flags

#### ❌ Removed (1)

- `Domain/GenerativePlayground.plist`

#### ⬆️ Updated (20)

<details>
  <summary><i>View Updated</i></summary>

- [Domain/AppStore.plist](FEATURES/AppStore.plist.md)
- [Domain/ControlCenter.plist](FEATURES/ControlCenter.plist.md)
- [Domain/GameCenter.plist](FEATURES/GameCenter.plist.md)
- [Domain/MediaAnalysis.plist](FEATURES/MediaAnalysis.plist.md)
- [Domain/MusicUI.plist](FEATURES/MusicUI.plist.md)
- [Domain/Oneness.plist](FEATURES/Oneness.plist.md)
- [Domain/Podcasts.plist](FEATURES/Podcasts.plist.md)
- [Domain/ScreenTime.plist](FEATURES/ScreenTime.plist.md)
- [Domain/Security.plist](FEATURES/Security.plist.md)
- [Domain/SettingsApp.plist](FEATURES/SettingsApp.plist.md)
- [Domain/SetupAssistant.plist](FEATURES/SetupAssistant.plist.md)
- [Domain/Siri.plist](FEATURES/Siri.plist.md)
- [Domain/Spotlight.plist](FEATURES/Spotlight.plist.md)
- [Domain/SpringBoard.plist](FEATURES/SpringBoard.plist.md)
- [Domain/TVApp.plist](FEATURES/TVApp.plist.md)
- [Domain/TextComposer.plist](FEATURES/TextComposer.plist.md)
- [Domain/TextInputUI.plist](FEATURES/TextInputUI.plist.md)
- [Domain/UnifiedAssetFramework.plist](FEATURES/UnifiedAssetFramework.plist.md)
- [Domain/UserNotifications.plist](FEATURES/UserNotifications.plist.md)
- [GlobalDisclosures.plist](FEATURES/GlobalDisclosures.plist.md)

</details>

## EOF
