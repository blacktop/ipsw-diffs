# 18.1 (22B5054e) .vs 18.1 (22B5069a)

## IPSWs

- `iPhone17,1_18.1_22B5054e_Restore.ipsw`
- `iPhone17,1_18.1_22B5069a_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.1 *(22B5054e)* | 24.1.0 | 11215.40.59~37 | Tue, 17Sep2024 10:48:44 PDT |
| 18.1 *(22B5069a)* | 24.1.0 | 11215.40.63~38 | Mon, 30Sep2024 02:02:35 PDT |

### Kexts

#### ⬆️ Updated (23)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.SecureRTBuddyProxy`

```diff

-618.40.2.0.0
+618.42.1.0.0
   __TEXT.__cstring: 0xd81
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x8928
+  __TEXT_EXEC.__text: 0x896c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

```

>  `com.apple.filesystems.apfs`

```diff

-2313.40.8.0.1
+2313.40.10.0.0
   __TEXT.__const: 0x790
-  __TEXT.__cstring: 0x48596
-  __TEXT_EXEC.__text: 0x13a484
+  __TEXT.__cstring: 0x48590
+  __TEXT_EXEC.__text: 0x13a494
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x690
   __DATA.__bss: 0xc60
CStrings:
+ "01:44:02"
+ "2024/09/30"
+ "2313.40.10"
+ "Sep 30 2024"
+ "apfs-2313.40.10"
- "2024/09/18"
- "22:27:56"
- "2313.40.8.0.1"
- "Sep 18 2024"
- "apfs-2313.40.8.0.1"

```

>  `com.apple.kernel`

```diff

-11215.40.59.0.0
+11215.40.63.0.0
   __TEXT.__const: 0x38400
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x70c4e
-  __TEXT.__os_log: 0x26d4f
+  __TEXT.__cstring: 0x70bde
+  __TEXT.__os_log: 0x26d15
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c8

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7f2634
+  __TEXT_EXEC.__text: 0x7e90e0
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__lock_grp: 0x5908
   __DATA.__percpu: 0x6e30
   __DATA.__common: 0x58608
-  __DATA.__bss: 0x95988
+  __DATA.__bss: 0x95938
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init_entry_set: 0x10a58
   __BOOTDATA.__init: 0x5b110

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x45557
-  Functions: 20350
+  Functions: 20326
   Symbols:   0
-  CStrings:  17020
+  CStrings:  17017
 
CStrings:
+ "site.u_int8_t *"
- "%s: %s (process %s:%u) priority %u entry_count 0\n"
- "IS_P2ALIGNED(ccp, CHANNEL_CACHE_ALIGN_MAX)"
- "necp_get_tlv_at_offset buffer is NULL"
- "site.u_int8_t * __attribute__((__indexable__))"

```

>  `com.apple.driver.AppleAOPAudio`

```diff

 400.9.0.0.0
-  __TEXT.__cstring: 0xc588
+  __TEXT.__cstring: 0xc591
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
   __TEXT_EXEC.__text: 0x32934

   __DATA_CONST.__kalloc_type: 0xa00
   Functions: 1277
   Symbols:   0
-  CStrings:  1151
+  CStrings:  1152
 
CStrings:
+ "01:42:50"
+ "01:42:55"
+ "Sep 30 2024"
- "20:15:35"
- "Sep 19 2024"

```

>  `com.apple.driver.AppleTypeCPhy`

```diff

-239.40.1.0.0
-  __TEXT.__cstring: 0x1651
+239.40.3.0.0
+  __TEXT.__cstring: 0x1700
   __TEXT.__const: 0x24
-  __TEXT.__os_log: 0x114c
-  __TEXT_EXEC.__text: 0x12570
+  __TEXT.__os_log: 0x11fb
+  __TEXT_EXEC.__text: 0x12d28
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

   __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x1250
+  __DATA_CONST.__const: 0x1268
   __DATA_CONST.__kalloc_type: 0x140
-  Functions: 245
+  Functions: 248
   Symbols:   0
-  CStrings:  226
+  CStrings:  234
 
CStrings:
+ "%s@%s: %s::%s: DP didn't close\n"
+ "%s@%s: %s::%s: USB client failed type checks\n"
+ "%s@%s: %s::%s: USB3 finished waiting for DP\n"
+ "%s@%s: %s::%s: USB3 waiting for DP client to close\n"

```

>  `com.apple.driver.AppleTypeCPhyAUSBC`

```diff

-239.40.1.0.0
+239.40.3.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x8a6
   __TEXT.__os_log: 0xc0f
-  __TEXT_EXEC.__text: 0x5468
+  __TEXT_EXEC.__text: 0x5484
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__got: 0x28
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__const: 0x810
   __DATA_CONST.__kalloc_type: 0x40
-  Functions: 52
+  Functions: 55
   Symbols:   0
   CStrings:  72
 

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-3.107.1.0.0
+3.112.0.0.0
   __TEXT.__const: 0xa058
   __TEXT.__cstring: 0x194d0
-  __TEXT.__os_log: 0x1551d
-  __TEXT_EXEC.__text: 0x9bc00
+  __TEXT.__os_log: 0x155a2
+  __TEXT_EXEC.__text: 0x9bd94
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a0
   __DATA.__common: 0x4a0

   __DATA_CONST.__const: 0xa0e8
   __DATA_CONST.__kalloc_type: 0x1300
   __DATA_CONST.__kalloc_var: 0xd70
-  Functions: 1909
+  Functions: 1911
   Symbols:   0
-  CStrings:  3285
+  CStrings:  3287
 
CStrings:
+ "AppleH16PearlCam:%s - ISP ANE Networks File is not loaded (res = 0x%08X)\n"
+ "AppleH16PearlCam:%s - ISP FW is not loaded (res = 0x%08X)\n"

```

>  `com.apple.driver.ApplePMGR`

```diff

-1555.40.11.502.1
+1555.40.13.0.0
   __TEXT.__const: 0x220
   __TEXT.__cstring: 0xe92b
-  __TEXT_EXEC.__text: 0x52d88
+  __TEXT_EXEC.__text: 0x52d90
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x100
   __DATA.__common: 0x420

```

>  `com.apple.security.sandbox`

```diff

-2401.40.21.0.0
-  __TEXT.__const: 0x1867c9
+2401.40.25.0.0
+  __TEXT.__const: 0x187479
   __TEXT.__cstring: 0x6f6b
   __TEXT.__os_log: 0x2029
-  __TEXT_EXEC.__text: 0x3056c
+  __TEXT_EXEC.__text: 0x30568
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x144d0
+  __DATA.__bss: 0x144c8
   __DATA_CONST.__auth_got: 0x830
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x3650

```

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 400.40.0.0.0
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x2d09
+  __TEXT.__cstring: 0x2d00
   __TEXT.__os_log: 0x16e9
   __TEXT_EXEC.__text: 0xaa40
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__kalloc_type: 0xc0
   Functions: 320
   Symbols:   0
-  CStrings:  231
+  CStrings:  230
 
CStrings:
+ "02:18:33"
+ "Sep 30 2024"
- "20:16:07"
- "20:16:08"
- "Sep 19 2024"

```

>  `com.apple.iokit.IODisplayPortFamily`

```diff

-730.40.5.0.0
-  __TEXT.__cstring: 0x7c47
-  __TEXT.__os_log: 0x9571
+730.40.6.0.0
+  __TEXT.__cstring: 0x7bf2
+  __TEXT.__os_log: 0x946b
   __TEXT.__const: 0x310
-  __TEXT_EXEC.__text: 0x5d118
+  __TEXT_EXEC.__text: 0x5cbac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x550

   __DATA_CONST.__kalloc_var: 0x280
   Functions: 1961
   Symbols:   0
-  CStrings:  1526
+  CStrings:  1523
 
CStrings:
+ "%s matching for endpoint %u\n"
+ "IOAV[%d] %s<0x%llx>::%s: Unable to cast service \"%s\" (0x%llx) to IOAVCECInterface\n"
+ "IOAV[%d] %s<0x%llx>::%s: _cecInterface=0x%llx\n"
+ "IOAV[%d] %s<0x%llx>::%s: setLinkRate with _transport=0x%llx, linkRate=%u\n"
+ "IOAV[%d] %s<0x%llx>::%s: warning: _cecService=0x%llx\n"
+ "Unable to cast service \"%s\" (0x%llx) to IOAVCECInterface\n"
+ "_cecInterface=0x%llx\n"
+ "setLinkRate with _transport=0x%llx, linkRate=%u\n"
+ "warning: _cecService=0x%llx\n"
- "\"%s\", waitForFunction=%d, param1=%p, param2=%p param3=%p, param4=%p\n"
- "%s matching for endpoint %u, dict = %p\n"
- "IOAV[%d] %s<0x%llx>::%s: \"%s\", waitForFunction=%d, param1=%p, param2=%p param3=%p, param4=%p\n"
- "IOAV[%d] %s<0x%llx>::%s: Unable to cast service \"%s\" (%p) to IOAVCECInterface\n"
- "IOAV[%d] %s<0x%llx>::%s: _cecInterface=%p\n"
- "IOAV[%d] %s<0x%llx>::%s: setLinkRate with _transport=%p, linkRate=%u\n"
- "IOAV[%d] %s<0x%llx>::%s: warning: _cecService=%p\n"
- "Unable to cast service \"%s\" (%p) to IOAVCECInterface\n"
- "_cecInterface=%p\n"
- "callPlatformFunction"
- "setLinkRate with _transport=%p, linkRate=%u\n"
- "warning: _cecService=%p\n"

```

>  `com.apple.driver.AppleT8140CLPC`

```diff

-1175.40.13.0.0
+1175.40.15.0.0
   __TEXT.__cstring: 0x2b92
   __TEXT.__const: 0xc6c
-  __TEXT_EXEC.__text: 0x4f3f4
+  __TEXT_EXEC.__text: 0x4f3e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xaf60
   __DATA.__common: 0x7ca1
CStrings:
+ "2024-09-30T02:00:58-07:00"
+ "AppleCLPC-1175.40.15"
- "2024-09-19T20:21:12-07:00"
- "AppleCLPC-1175.40.13"

```

>  `com.apple.driver.DCPAVFamilyProxy`

```diff

-349.40.5.0.0
+349.40.6.0.0
   __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x245c
-  __TEXT.__os_log: 0x129e
-  __TEXT_EXEC.__text: 0x16ca4
+  __TEXT.__cstring: 0x247d
+  __TEXT.__os_log: 0x129d
+  __TEXT_EXEC.__text: 0x16ccc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x308

   __DATA_CONST.__kalloc_var: 0x3c0
   Functions: 808
   Symbols:   0
-  CStrings:  283
+  CStrings:  285
 
CStrings:
+ "IOAV[%d] %s<0x%llx>::%s: enqueueResponse failed, rc=%08x\n"
+ "enqueueResponse failed, rc=%08x\n"

```

>  `com.apple.driver.EXDisplayPipeH17P`

```diff

-5.26.8.7.0
+5.26.8.4.2
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x1a46
-  __TEXT_EXEC.__text: 0x6d64
+  __TEXT.__cstring: 0x1a64
+  __TEXT_EXEC.__text: 0x6db0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__kalloc_type: 0x80
   Functions: 146
   Symbols:   0
-  CStrings:  140
+  CStrings:  141
 
CStrings:
+ "EXDisplayPipe::%s failed!!! \n"

```

>  `com.apple.driver.AppleDisplayCrossbar`

```diff

-355.40.3.0.0
-  __TEXT.__cstring: 0x4413
+355.40.4.0.0
+  __TEXT.__cstring: 0x43ef
   __TEXT.__const: 0x160
-  __TEXT.__os_log: 0x5d14
-  __TEXT_EXEC.__text: 0x32128
+  __TEXT.__os_log: 0x5be3
+  __TEXT_EXEC.__text: 0x319ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x3d0
-  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0

   __DATA_CONST.__kalloc_type: 0x600
   Functions: 1474
   Symbols:   0
-  CStrings:  707
+  CStrings:  705
 
CStrings:
- "IOAV[%d] %s<0x%llx>::%s: registers at %p, 0x%0*llx physical\n"
- "registers at %p, 0x%0*llx physical\n"

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-8.106.0.0.0
-  __TEXT.__os_log: 0x31890
-  __TEXT.__cstring: 0xabe6
-  __TEXT.__const: 0x630
-  __TEXT_EXEC.__text: 0xa1714
+8.107.3.0.0
+  __TEXT.__os_log: 0x3212b
+  __TEXT.__cstring: 0xac84
+  __TEXT.__const: 0x650
+  __TEXT_EXEC.__text: 0xa221c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x34d0
   __DATA.__common: 0x3c8

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x6098
   __DATA_CONST.__kalloc_type: 0x2d00
-  __DATA_CONST.__kalloc_var: 0x2ad0
-  Functions: 1827
+  __DATA_CONST.__kalloc_var: 0x2d50
+  Functions: 1829
   Symbols:   0
-  CStrings:  3491
+  CStrings:  3520
 
CStrings:
+ "%s: Invalid thread cmd flavor"
+ "%s: The compute thread %p is a nullptr"
+ "%s: The info %p is a nullptr"
+ "%s: The operation %p is a nullptr"
+ "%s: illegal 'proc_fvmlib_count', no fvmlibs"
+ "%s: illegal 'proc_operation_count', no proc operations"
+ "%s: illegal (null) 'td' at op_idx=%zu, td_idx=%zu"
+ "/Library/Caches/com.apple.xbs/Sources/AppleH11ANEInterface/aneexclave/ANELoader/ZinComputeProgramLoader.cpp"
+ "12122222222222"
+ "ANE%d: %s: ERROR: ANE_ProgramCreatePreprocessing failed result: 0x%x\n"
+ "ANE%d: %s: ERROR: Client: %p not found in programBuffer: %p\n"
+ "ANE%d: %s: ERROR: Couldn't create kernel split [%u] memory descriptor\n"
+ "ANE%d: %s: ERROR: Kernel split [%u] ZinComputeProgramGetKernelSectionInfo() error: %d\n"
+ "ANE%d: %s: ERROR: Kernel split [%u] file_offset: %lu not DART page size aligned\n"
+ "ANE%d: %s: ERROR: Kernel split [%u] section pointer is NULL\n"
+ "ANE%d: %s: ERROR: Kernel split section [%u] out of bounds. file_offset: %lu section_size: %llu programSize: %zu\n"
+ "ANE%d: %s: ERROR: Number of program kernel splits: %lu is greater than maximum allowed: %u\n"
+ "ANE%d: %s: ERROR: ZinComputeProgramGetKernelSectionInfo() error: %d\n"
+ "ANE%d: %s: ERROR: ZinComputeProgramGetNamesFromMultiPlaneLinear() error: %d\n"
+ "ANE%d: %s: ERROR: ZinComputeProgramGetNamesFromMultiPlaneTiledCompressed() error: %d\n"
+ "ANE%d: %s: ERROR: ZinComputeProgramGetNamesFromSinglePlaneTiledCompressed() error: %d\n"
+ "ANE%d: %s: ERROR: ZinComputeProgramGetNamesFromSinglePlaneTiledCompressedMultislice() error: %d\n"
+ "ANE%d: %s: ERROR: ZinComputeProgramGetNamesFromSinglePlaneUncompressed() error: %d\n"
+ "ANE%d: %s: ERROR: ZinComputeProgramGetParamNameFromBinding() error: %d\n"
+ "ANE%d: %s: ERROR: waitForPendingUpdate() failed. result: 0x%x\n"
+ "ANE%d: %s: Found process client for cleanup. programHandle: 0x%llx\n"
+ "ANE%d: %s: memoryMapRequestErrorInfo1: 0x%llx, memoryMapRequestErrorInfo2: 0x%llx\n"
+ "ANE%d: %s: programOutput->procedures[procId].numOperationsPerLiveInParam=%d programOutput->procedures[procId].liveInParamBarId[sneop_idx]= %d compute_program->procedures[procId].operations[op_idx]->sne.thread->bar_cmd.bar_type=%d\n"
+ "Allocation error: compute_thread_command"
+ "Cannot find procedure name from thread."
+ "Could not determine TD partition of operation"
+ "Error: thread argument buffer overrun."
+ "Error: thread argument is not supported."
+ "Failed to get text data size"
+ "Invalid BarId conversion factor"
+ "Invalid kernel section index, %zu"
+ "The next operation id could not be found"
+ "ZinComputeGetNumberOfKernelSectionsForOperation"
+ "ZinComputeGetNumberOfKernelSectionsForOperation failed, line: %d, file: %s"
+ "ZinComputeProgramGetKernelSectionInfoForOperation"
+ "ZinComputeProgramGetOperationsToBeScheduledNext"
+ "ZinComputeProgramStatus ZinComputeProgramGetMutableKernelSectionForProcedure(const ZinComputeProgram *, uint32_t, ZinComputeProgramSection **)"
+ "ZinComputeProgramStatus ZinComputeProgramMakeAneProcedures(ZinComputeProgram *)"
+ "ZinComputeProgramStatus ZinComputeProgramValidateLCThread(uint32_t, const void *, const void *, const void *)"
+ "plane count overrun"
+ "section corresponding to kernel number %zu not found for operation %p"
+ "symbolic ne_offset=0x%0llx %s\n"
+ "symbolic ne_offset=0x%0llx %s+0x%llx\n"
- "%s: The kernel_sections_wrapper %p is a nullptr"
- "%s: illegal 'proc_operation_count'"
- "1212222222222"
- "ANE%d: %s: ANE_ProgramCreatePreprocessing failed result: 0x%x\n"
- "ANE%d: %s: Couldn't create kernel split [%u] memory descriptor\n"
- "ANE%d: %s: ERROR: Process not created yet for programHandle: 0x%llx\n"
- "ANE%d: %s: Kernel split [%u] ZinComputeProgramGetKernelSectionInfo() error %d\n"
- "ANE%d: %s: Kernel split [%u] file_offset: %lu not DART page size aligned\n"
- "ANE%d: %s: Kernel split [%u] section pointer is NULL\n"
- "ANE%d: %s: Kernel split section [%u] out of bounds. file_offset: %lu section_size: %llu programSize: %zu\n"
- "ANE%d: %s: Number of program kernel splits: %lu is greater than maximum allowed: %u\n"
- "ANE%d: %s: ZinComputeProgramGetKernelSectionInfo() error %d\n"
- "ANE%d: %s: programOutput->procedures[procId].numOperationsPerLiveInParam=%d programOutput->procedures[procId].liveInParamBarId[sneop_idx]= %d compute_program->procedures[procId].operations[sneop_idx]->sne.thread->bar_cmd.bar_type=%d\n"
- "ANE%d: %s: push sensor 0x%x to PTD, value_sum 0x%llx, value_count: 0x%x \n"
- "WARN: Assertion failed\n"
- "ZinComputeProgramStatus ZinComputeProgramGetMutableKernelSectionForProcedure(const ZinComputeProgram *, int, ZinComputeProgramSection **)"
- "ZinComputeProgramStatus ZinComputeProgramMakeAneProcedures(const struct ident_command *, std::span<ZinComputeProgramFvmlib> &, std::span<ZinComputeProcedureOperation> &, std::span<ZinComputeProgramBinding> &, std::span<ZinComputeProgramProcedure> &, std::span<ZinComputeProgramSegment> &, const void *const, const void *const)"
- "ne_offset=%s\n"
- "ne_offset=%s+0x%llx"

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.40.4.0.0
-  __TEXT.__cstring: 0x9c1e
-  __TEXT.__const: 0x14b0
+938.42.1.0.0
+  __TEXT.__cstring: 0x9c92
+  __TEXT.__const: 0x14c0
   __TEXT.__os_log: 0x233
-  __TEXT_EXEC.__text: 0x263b8
+  __TEXT_EXEC.__text: 0x26424
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x412
   __DATA.__common: 0xb0

   __DATA_CONST.__const: 0x3750
   __DATA_CONST.__kalloc_type: 0xec0
   __DATA_CONST.__kalloc_var: 0x1310
-  Functions: 795
+  Functions: 796
   Symbols:   0
-  CStrings:  983
+  CStrings:  985
 
CStrings:
+ "01:43:04"
+ "AMFI: [1] informing daemon of developer mode state change"
+ "AMFI: [2] informing daemon of developer mode state change"
+ "Sep 30 2024"
- "20:15:57"
- "Sep 19 2024"

```

>  `com.apple.driver.AppleT8103TypeCPhy`

```diff

-239.40.1.0.0
+239.40.3.0.0
   __TEXT.__const: 0x1a0
   __TEXT.__cstring: 0xa571
   __TEXT.__os_log: 0xe5a8
-  __TEXT_EXEC.__text: 0x4b6e4
+  __TEXT_EXEC.__text: 0x4b700
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x948
+  __DATA_CONST.__const: 0x960
   __DATA_CONST.__kalloc_type: 0x40
-  Functions: 112
+  Functions: 115
   Symbols:   0
   CStrings:  1073
 

```

>  `com.apple.driver.AppleT8130TypeCPhy`

```diff

-239.40.1.0.0
+239.40.3.0.0
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x81fb
   __TEXT.__os_log: 0xe07d
-  __TEXT_EXEC.__text: 0x4bf80
+  __TEXT_EXEC.__text: 0x4bf9c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2c8
   __DATA.__common: 0x58

   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x848
+  __DATA_CONST.__const: 0x860
   __DATA_CONST.__kalloc_type: 0x40
-  Functions: 122
+  Functions: 125
   Symbols:   0
   CStrings:  790
 

```

>  `com.apple.AGXG17P`

```diff

-322.9.0.0.0
+322.10.0.0.0
   __TEXT.__const: 0x4cfc
   __TEXT.__cstring: 0xec5b
   __TEXT.__os_log: 0x318
-  __TEXT_EXEC.__text: 0xc3b3c
+  __TEXT_EXEC.__text: 0xc3db4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13b8
   __DATA.__common: 0x10
CStrings:
+ "3.41.1"
+ "Sep 30 2024 01:59:05"
- "3.41.0"
- "Sep 19 2024 20:18:40"

```

>  `com.apple.driver.AppleAVD`

```diff

-806.1.0.0.0
+807.0.0.0.0
   __TEXT.__const: 0x9a8c9
   __TEXT.__cstring: 0x5277
   __TEXT.__os_log: 0x12f18
-  __TEXT_EXEC.__text: 0x45564
+  __TEXT_EXEC.__text: 0x45574
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

```

>  `com.apple.driver.AppleAVE2`

```diff

-803.31.1.0.0
+803.36.1.0.0
   __TEXT.__const: 0x2edd0
-  __TEXT.__cstring: 0x356b5
-  __TEXT.__os_log: 0x408a7
-  __TEXT_EXEC.__text: 0x1457e0
+  __TEXT.__cstring: 0x357a7
+  __TEXT.__os_log: 0x408f4
+  __TEXT_EXEC.__text: 0x145c00
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x290
   __DATA.__common: 0x130

   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
   __DATA_CONST.__const: 0x6310
-  __DATA_CONST.__kalloc_type: 0x1fc0
-  __DATA_CONST.__kalloc_var: 0xfa0
+  __DATA_CONST.__kalloc_type: 0x2c40
+  __DATA_CONST.__kalloc_var: 0xdc0
   Functions: 2495
   Symbols:   0
-  CStrings:  6988
+  CStrings:  6991
 
CStrings:
+ "%lld %d AVE %s: %s:%d %s | LookAhead frame count is out of range %p %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | LookAhead frame count is out of range %p %d %d %d\n"
+ "0 <= pInfo->VideoParams.iBFrames && pInfo->VideoParams.iBFrames <= 3"
+ "0 <= pInfo->sRCParams.iLookAheadFrames && pInfo->sRCParams.iLookAheadFrames <= (32 / ((2) < ((63 + 1)) ? (2) : ((63 + 1))) - 4)"
+ "02:49:17"
+ "803.36.1"
+ "Sep 30 2024"
- "23:08:38"
- "803.31.1"
- "Sep 18 2024"
- "pInfo->VideoParams.iBFrames <= 3"

```

>  `com.apple.iokit.IOAVFamily`

```diff

-483.40.1.0.0
-  __TEXT.__cstring: 0xa8dc
-  __TEXT.__os_log: 0x9ca0
+483.40.2.0.0
+  __TEXT.__cstring: 0xa784
+  __TEXT.__os_log: 0x9a1d
   __TEXT.__const: 0xe7d4
-  __TEXT_EXEC.__text: 0x84ef0
+  __TEXT_EXEC.__text: 0x8449c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x988

   __DATA_CONST.__kalloc_var: 0x1e0
   Functions: 2950
   Symbols:   0
-  CStrings:  2136
+  CStrings:  2126
 
CStrings:
+ "\"Unrecoverable error in IOAVAsyncEventSource: waitResult=%d.\\n\" @%s:%d"
+ "IOAVAsyncEventSource::waitUntilNoActionInProgressGated: Giving up.\n"
+ "IOAVAsyncEventSource::waitUntilNoActionInProgressGated: Timed out waiting for action to complete.\n"
+ "IOAVAsyncEventSource::waitUntilNoActionInProgressGated: sleepGate() returned unexpected result=%d.\n"
+ "IOAVIISAudioDMAEventSource: BUG: queue size is too small\n"
+ "IOAV[%d] %s<0x%llx>::%s: Passed EDID: size=%d\n"
+ "IOAV[%d] %s<0x%llx>::%s: byteCount=%lu byteOffset=%lu outstandingDMACount=%u\n"
+ "IOAV[%d] %s<0x%llx>::%s: channelAllocation=%d\n"
+ "IOAV[%d] %s<0x%llx>::%s: elementID=%lld matching=%llu\n"
+ "IOAV[%d] %s<0x%llx>::%s: inStreamID=%u _outputBufferFrameSize=%u\n"
+ "IOAV[%d] %s<0x%llx>::%s: inStreamID=%u inNewStreamFormatByteSize=%u\n"
+ "IOAV[%d] %s<0x%llx>::%s: matching=%llu\n"
+ "IOAV[%d] %s<0x%llx>::%s: not adding existing element <%s>.\n"
+ "IOAV[%d] %s<0x%llx>::%s: power=%d device=0x%llx attached=%d started=%d\n"
+ "IOAV[%d] %s<0x%llx>::%s: source=%d (%s) ID=%llu\n"
+ "IOAV[%d] %s<0x%llx>::%s: status=0x%08x byteCount=%lu async=%d totalOutstanding=%u isOutstanding=%d\n"
+ "IOAV[%d] %s<0x%llx>::%s: unexpected element type <%s>.\n"
+ "IOAV[%d] %s<0x%llx>::%s: virtual EDID mode %s\n"
+ "Passed EDID: size=%d\n"
+ "byteCount=%lu byteOffset=%lu outstandingDMACount=%u\n"
+ "channelAllocation=%d\n"
+ "elementID=%lld matching=%llu\n"
+ "inStreamID=%u _outputBufferFrameSize=%u\n"
+ "inStreamID=%u inNewStreamFormatByteSize=%u\n"
+ "matching=%llu\n"
+ "not adding existing element <%s>.\n"
+ "power=%d device=0x%llx attached=%d started=%d\n"
+ "source=%d (%s) ID=%llu\n"
+ "status=0x%08x byteCount=%lu async=%d totalOutstanding=%u isOutstanding=%d\n"
+ "unexpected element type <%s>.\n"
+ "virtual EDID mode %s\n"
- "\"%s\", waitForFunction=%d, param1=%p, param2=%p param3=%p, param4=%p\n"
- "\"Unrecoverable error in IOAVAsyncEventSource: waitResult=%d, action=%p.\\n\" @%s:%d"
- "IOAVAsyncEventSource::waitUntilNoActionInProgressGated: Giving up.  action=%p.\n"
- "IOAVAsyncEventSource::waitUntilNoActionInProgressGated: Timed out waiting for action to complete, action=%p.\n"
- "IOAVAsyncEventSource::waitUntilNoActionInProgressGated: sleepGate() returned unexpected result=%d, action=%p.\n"
- "IOAVIISAudioDMAEventSource(%p): BUG: queue size is too small\n"
- "IOAV[%d] %s<0x%llx>::%s: \"%s\", waitForFunction=%d, param1=%p, param2=%p param3=%p, param4=%p\n"
- "IOAV[%d] %s<0x%llx>::%s: Passed EDID: data=%p size=%d\n"
- "IOAV[%d] %s<0x%llx>::%s: _audioLinkDelegate=%p\n"
- "IOAV[%d] %s<0x%llx>::%s: audioInterface=%p\n"
- "IOAV[%d] %s<0x%llx>::%s: dmaCommand=%p byteCount=%lu byteOffset=%lu outstandingDMACount=%u\n"
- "IOAV[%d] %s<0x%llx>::%s: dmaCommand=%p status=0x%08x byteCount=%lu async=%d totalOutstanding=%u isOutstanding=%d\n"
- "IOAV[%d] %s<0x%llx>::%s: element=%p source=%d (%s) ID=%llu\n"
- "IOAV[%d] %s<0x%llx>::%s: elementID=%lld matching=%p\n"
- "IOAV[%d] %s<0x%llx>::%s: inStreamID=%u inNewStreamFormat=%p inNewStreamFormatByteSize=%u\n"
- "IOAV[%d] %s<0x%llx>::%s: inStreamID=%u outOptions=%p outMemory=%p _outputBufferFrameSize=%u\n"
- "IOAV[%d] %s<0x%llx>::%s: layout=%p channelAllocation=%d\n"
- "IOAV[%d] %s<0x%llx>::%s: matching=%p\n"
- "IOAV[%d] %s<0x%llx>::%s: not adding existing element <%s:%p>.\n"
- "IOAV[%d] %s<0x%llx>::%s: power=%d device=%p attached=%d started=%d\n"
- "IOAV[%d] %s<0x%llx>::%s: unexpected element type <%s:%p>.\n"
- "IOAV[%d] %s<0x%llx>::%s: videoInterface=%p\n"
- "IOAV[%d] %s<0x%llx>::%s: virtual EDID mode %s, _virtualEDIDData=%p\n"
- "Passed EDID: data=%p size=%d\n"
- "_audioLinkDelegate=%p\n"
- "audioInterface=%p\n"
- "callPlatformFunction"
- "dmaCommand=%p byteCount=%lu byteOffset=%lu outstandingDMACount=%u\n"
- "dmaCommand=%p status=0x%08x byteCount=%lu async=%d totalOutstanding=%u isOutstanding=%d\n"
- "element=%p source=%d (%s) ID=%llu\n"
- "elementID=%lld matching=%p\n"
- "handleAddInterfaces"
- "inStreamID=%u inNewStreamFormat=%p inNewStreamFormatByteSize=%u\n"
- "inStreamID=%u outOptions=%p outMemory=%p _outputBufferFrameSize=%u\n"
- "layout=%p channelAllocation=%d\n"
- "matching=%p\n"
- "not adding existing element <%s:%p>.\n"
- "power=%d device=%p attached=%d started=%d\n"
- "unexpected element type <%s:%p>.\n"
- "videoInterface=%p\n"
- "virtual EDID mode %s, _virtualEDIDData=%p\n"

```

</details>

### KDKs

- [KDK DIFF](KDK.md)

## MachO

### 🆕 NEW (4)

- `/System/Library/ControlCenter/Bundles/AirDropModule.bundle/AirDropModule`
- `/System/Library/ControlCenter/Bundles/SatelliteModule.bundle/SatelliteModule`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`
- `/private/var/staged_system_apps/Measure.app/PlugIns/MeasureWidgetExtension.appex/MeasureWidgetExtension`

### ❌ Removed (1)

- `/System/Library/ExtensionKit/Extensions/SoundAndHapticsControls.appex/SoundAndHapticsControls`

### ⬆️ Updated (527)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService.md)
- [/Applications/AXUIViewService.app/AXUIViewService](MACHOS/AXUIViewService.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AnimojiStickers.app/PlugIns/AnimojiStickersExtension.appex/AnimojiStickersExtension](MACHOS/AnimojiStickersExtension.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CameraOverlayAngel.app/CameraOverlayAngel](MACHOS/CameraOverlayAngel.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/Jellyfish.app/PlugIns/Animoji.appex/Animoji](MACHOS/Animoji.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MediaRemoteUIService.app/MediaRemoteUIService](MACHOS/MediaRemoteUIService.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosEngagementExtension.appex/PhotosEngagementExtension](MACHOS/PhotosEngagementExtension.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/RecoverDeviceUI.app/RecoverDeviceUI](MACHOS/RecoverDeviceUI.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Sidecar.app/PlugIns/ContinuitySketch.appex/ContinuitySketch](MACHOS/ContinuitySketch.md)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SleepLockScreen.app/SleepLockScreen](MACHOS/SleepLockScreen.md)
- [/Applications/SleepWidgetContainer.app/PlugIns/SleepWidgetExtension.appex/SleepWidgetExtension](MACHOS/SleepWidgetExtension.md)
- [/Applications/Spotlight.app/Spotlight](MACHOS/Spotlight.md)
- [/Applications/StickerPickerService.app/StickerPickerService](MACHOS/StickerPickerService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StoreKitUIService.app/StoreKitUIService](MACHOS/StoreKitUIService.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/WorkoutRemoteViewService.app/WorkoutRemoteViewService](MACHOS/WorkoutRemoteViewService.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Applications/iCloud+.app/iCloud+](MACHOS/iCloud+.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation](MACHOS/Foundation.md)
- [/System/ExclaveKit/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](MACHOS/SoundAnalysis.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8140_IR_ISP_EK_Component.framework/T8140_IR_ISP_EK_Component](MACHOS/T8140_IR_ISP_EK_Component.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8140_RGB_ISP_EK_Component.framework/T8140_RGB_ISP_EK_Component](MACHOS/T8140_RGB_ISP_EK_Component.md)
- [/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision](MACHOS/Vision.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/EXDisplayPipeSwapClient.framework/EXDisplayPipeSwapClient](MACHOS/EXDisplayPipeSwapClient.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/ShareLibCommon_EK.framework/ShareLibCommon_EK](MACHOS/ShareLibCommon_EK.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/ShazamKit.framework/ShazamKit](MACHOS/ShazamKit.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8140_CoreAAClientKit.framework/T8140_CoreAAClientKit](MACHOS/T8140_CoreAAClientKit.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8140_CoreERClientKit.framework/T8140_CoreERClientKit](MACHOS/T8140_CoreERClientKit.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8140_ExclaveISPSharedLib_exclavekit.framework/T8140_ExclaveISPSharedLib_exclavekit](MACHOS/T8140_ExclaveISPSharedLib_exclavekit.md)
- [/System/Library/AccessibilityBundles/AXAVSPluginService.axuiservice/AXAVSPluginService](MACHOS/AXAVSPluginService.md)
- [/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer](MACHOS/AXHapticMusicServer.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer](MACHOS/ClarityUIServer.md)
- [/System/Library/AccessibilityBundles/GuidedAccess.axuiservice/GuidedAccess](MACHOS/GuidedAccess.md)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow.md)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppRemovalServices/com.apple.weather.appremoval.xpc/com.apple.weather.appremoval](MACHOS/com.apple.weather.appremoval.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AppLaunchPlugin.bundle/AppLaunchPlugin](MACHOS/AppLaunchPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ControlsFlowDelegatePlugin.bundle/ControlsFlowDelegatePlugin](MACHOS/ControlsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeAutomationFlowDelegatePlugin.bundle/HomeAutomationFlowDelegatePlugin](MACHOS/HomeAutomationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/MessagesFlowDelegatePlugin.bundle/MessagesFlowDelegatePlugin](MACHOS/MessagesFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PaymentsFlowDelegatePlugin.bundle/PaymentsFlowDelegatePlugin](MACHOS/PaymentsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/VideoFlowDelegatePlugin.bundle/VideoFlowDelegatePlugin](MACHOS/VideoFlowDelegatePlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting](MACHOS/CIInpainting.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration](MACHOS/AccessibilityDataMigration.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/MobileAsset.migrator/MobileAsset](MACHOS/MobileAsset.md)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator.md)
- [/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess](MACHOS/RestorePostProcess.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DigitalSeparation/SharingSources/DSNotesPlugin.bundle/DSNotesPlugin](MACHOS/DSNotesPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/AutocorrectionTesterDESPlugin.desPlugin/AutocorrectionTesterDESPlugin](MACHOS/AutocorrectionTesterDESPlugin.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AirDropSettingsIntents.appex/AirDropSettingsIntents](MACHOS/AirDropSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension](MACHOS/ComposeReviewExtension.md)
- [/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents](MACHOS/DeveloperSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents](MACHOS/GeneralSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/InstalledAppsSettingsAppIntents.appex/InstalledAppsSettingsAppIntents](MACHOS/InstalledAppsSettingsAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/LLMCacheSELFIngestor.appex/LLMCacheSELFIngestor](MACHOS/LLMCacheSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/LegalAndRegulatoryAppIntents.appex/LegalAndRegulatoryAppIntents](MACHOS/LegalAndRegulatoryAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/MeasureSettingsAppIntentsExtension.appex/MeasureSettingsAppIntentsExtension](MACHOS/MeasureSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicUIEngagementExtension.appex/MusicUIEngagementExtension](MACHOS/MusicUIEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PasscodeSettingsExtension.appex/PasscodeSettingsExtension](MACHOS/PasscodeSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin](MACHOS/PhotosPFLPlugin.md)
- [/System/Library/ExtensionKit/Extensions/PodcastsSettingsAppIntentsExtension.appex/PodcastsSettingsAppIntentsExtension](MACHOS/PodcastsSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivacyAppIntents.appex/PrivacyAppIntents](MACHOS/PrivacyAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension](MACHOS/SearchToolExtension.md)
- [/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsIntents.appex/SoftwareUpdateSettingsIntents](MACHOS/SoftwareUpdateSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents](MACHOS/VSAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension](MACHOS/WiFiSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/sm_stats](MACHOS/sm_stats.md)
- [/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService](MACHOS/AVAudioDeviceTestService.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationMapLNPromptPlugin.appex/CoreLocationMapLNPromptPlugin](MACHOS/CoreLocationMapLNPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin](MACHOS/CoreLocationNumberedMapCalloutPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTestImporter.appex/CoreSpotlightTestImporter](MACHOS/CoreSpotlightTestImporter.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTextImporter.appex/CoreSpotlightTextImporter](MACHOS/CoreSpotlightTextImporter.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/financed](MACHOS/financed.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension](MACHOS/SKAskPermissionExtension.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker.md)
- [/System/Library/Frameworks/WeatherKit.framework/XPCServices/com.apple.weatherkit.authservice.xpc/com.apple.weatherkit.authservice](MACHOS/com.apple.weatherkit.authservice.md)
- [/System/Library/Health/FeedItemPlugins/HealthBalanceAppPluginBundle.healthplugin/HealthBalanceAppPluginBundle](MACHOS/HealthBalanceAppPluginBundle.md)
- [/System/Library/LocationBundles/AltimeterHarvest.bundle/AltimeterHarvest](MACHOS/AltimeterHarvest.md)
- [/System/Library/LocationBundles/AppGenius.bundle/AppGenius](MACHOS/AppGenius.md)
- [/System/Library/LocationBundles/CompassCalibration.bundle/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/LocationBundles/IonosphereHarvest.bundle/IonosphereHarvest](MACHOS/IonosphereHarvest.md)
- [/System/Library/LocationBundles/LocationFenceSync.bundle/LocationFenceSync](MACHOS/LocationFenceSync.md)
- [/System/Library/LocationBundles/LocationPromptUI.bundle/LocationPromptUI](MACHOS/LocationPromptUI.md)
- [/System/Library/LocationBundles/MotionCalibration.bundle/MotionCalibration](MACHOS/MotionCalibration.md)
- [/System/Library/LocationBundles/PLAMonitor.bundle/PLAMonitor](MACHOS/PLAMonitor.md)
- [/System/Library/LocationBundles/TimeZone.bundle/TimeZone](MACHOS/TimeZone.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/SMS](MACHOS/SMS.md)
- [/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS](MACHOS/SatelliteSMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/PlugIns/iMessageLite.imservice/iMessageLite](MACHOS/iMessageLite.md)
- [/System/Library/Messages/iMessageApps/AnimojiCameraApp.bundle/AnimojiCameraApp](MACHOS/AnimojiCameraApp.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/NanoPreferenceBundles/Applications/MindSettings.bundle/MindSettings](MACHOS/MindSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoHealthBalanceBridgeSettings.bundle/NanoHealthBalanceBridgeSettings](MACHOS/NanoHealthBalanceBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMenstrualCyclesCompanionSettings.bundle/NanoMenstrualCyclesCompanionSettings](MACHOS/NanoMenstrualCyclesCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/OxygenSaturationSettings.bundle/OxygenSaturationSettings](MACHOS/OxygenSaturationSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/SessionTrackerAppSettings.bundle/SessionTrackerAppSettings](MACHOS/SessionTrackerAppSettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/DepthCompanionSetup.bundle/DepthCompanionSetup](MACHOS/DepthCompanionSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthFeaturesBridgeSetupPlugin.bundle/HealthFeaturesBridgeSetupPlugin](MACHOS/HealthFeaturesBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoSleepBridgeSetup.bundle/NanoSleepBridgeSetup](MACHOS/NanoSleepBridgeSetup.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKDolomiteFaceBundleCompanion.bundle/NTKDolomiteFaceBundleCompanion](MACHOS/NTKDolomiteFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings](MACHOS/AirPlayAndHandoffSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/DeveloperSettings.bundle/DeveloperSettings](MACHOS/DeveloperSettings.md)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings.md)
- [/System/Library/PreferenceBundles/HealthSettings.bundle/HealthSettings](MACHOS/HealthSettings.md)
- [/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings](MACHOS/HearingSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/NewsSettings.bundle/NewsSettings](MACHOS/NewsSettings.md)
- [/System/Library/PreferenceBundles/PassbookSettings.bundle/PassbookSettings](MACHOS/PassbookSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PodcastsUsagePlugin.bundle/PodcastsUsagePlugin](MACHOS/PodcastsUsagePlugin.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountSettings.bundle/VideoSubscriberAccountSettings](MACHOS/VideoSubscriberAccountSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceBundles/WeatherSettings.bundle/WeatherSettings](MACHOS/WeatherSettings.md)
- [/System/Library/PreferenceManifestsInternal/PreferencesManifests.bundle/PreferencesManifests](MACHOS/PreferencesManifests.md)
- [/System/Library/PreferencesSyncBundles/CoreLocationSync.bundle/CoreLocationSync](MACHOS/CoreLocationSync.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/PlugIns/AppStoreOverlaysService.appex/AppStoreOverlaysService](MACHOS/AppStoreOverlaysService.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension](MACHOS/AAUIFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementNotificationsExtension.appex/AMSEngagementNotificationsExtension](MACHOS/AMSEngagementNotificationsExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementViewExtension.appex/AMSEngagementViewExtension](MACHOS/AMSEngagementViewExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSProductPageExtension.appex/AMSProductPageExtension](MACHOS/AMSProductPageExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail](MACHOS/ASVAssetThumbnail.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetViewer.appex/ASVAssetViewer](MACHOS/ASVAssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension](MACHOS/CMCaptureDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService](MACHOS/CategoriesService.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/companionmessagesd](MACHOS/companionmessagesd.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd](MACHOS/com.apple.sbd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension](MACHOS/CDPFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/XPCServices/DataDetectorsRemoteScanner.xpc/DataDetectorsRemoteScanner](MACHOS/DataDetectorsRemoteScanner.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/DragUI.framework/Support/druid](MACHOS/druid.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex/HealthFollowUpExtension](MACHOS/HealthFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/PlugIns/HealthMedicationsNotificationContentExtension.appex/HealthMedicationsNotificationContentExtension](MACHOS/HealthMedicationsNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension](MACHOS/ManagedSettingsExtension.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd](MACHOS/mstreamd.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service](MACHOS/Accessory_Updater_Service.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService](MACHOS/ManifestStorageService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent](MACHOS/NPKCompanionAgent.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond](MACHOS/nanotimekitcompaniond.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/TodayFeedConfigDecoder.xpc/TodayFeedConfigDecoder](MACHOS/TodayFeedConfigDecoder.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/XPCServices/SBRendererService.xpc/SBRendererService](MACHOS/SBRendererService.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd](MACHOS/photoanalysisd.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PlugIns/PhotosStoryDiagnostics.appex/PhotosStoryDiagnostics](MACHOS/PhotosStoryDiagnostics.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourEngagementExtension.appex/SeymourEngagementExtension](MACHOS/SeymourEngagementExtension.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourNotifications.appex/SeymourNotifications](MACHOS/SeymourNotifications.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored](MACHOS/fitcored.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcoresessiond](MACHOS/fitcoresessiond.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/PlugIns/SettingsIntentExtension.appex/SettingsIntentExtension](MACHOS/SettingsIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension](MACHOS/VideoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/PlugIns/SleepNotificationContentExtension.appex/SleepNotificationContentExtension](MACHOS/SleepNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/XPCServices/StocksKitService.xpc/StocksKitService](MACHOS/StocksKitService.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/CarPlayArtwork.bundle/CarPlayArtwork](MACHOS/CarPlayArtwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/TextEffectsCatalog.bundle/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/matd](MACHOS/matd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/ScreenReader/BrailleTables/BrailleNBSC.brailletable/BrailleNBSC](MACHOS/BrailleNBSC.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AppLaunchSuggestionsPlugin.bundle/AppLaunchSuggestionsPlugin](MACHOS/AppLaunchSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSettingsSuggestionsPlugin.bundle/SiriSettingsSuggestionsPlugin](MACHOS/SiriSettingsSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/AudioUIPlugin](MACHOS/AudioUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SettingsCustomPlugin.bundle/SettingsCustomPlugin](MACHOS/SettingsCustomPlugin.md)
- [/System/Library/Snippets/UIPlugins/ShazamUIPlugin.bundle/ShazamUIPlugin](MACHOS/ShazamUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriAppLaunchUIPlugin.bundle/SiriAppLaunchUIPlugin](MACHOS/SiriAppLaunchUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriMailUIPlugin.bundle/SiriMailUIPlugin](MACHOS/SiriMailUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriVideoUIPlugin.bundle/SiriVideoUIPlugin](MACHOS/SiriVideoUIPlugin.md)
- [/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin](MACHOS/StoreDemoPlugin.md)
- [/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary](MACHOS/MusicLibrary.md)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage.md)
- [/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA](MACHOS/MobileBackupUEA.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1](MACHOS/ColourConstancyV1.md)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1](MACHOS/SemanticStyleV1.md)
- [/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1](MACHOS/SmartStyleV1.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/VideoDeghostingV1](MACHOS/VideoDeghostingV1.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/AppleTV.app/AppleTV](MACHOS/AppleTV.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary](MACHOS/BKLibrary.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/EngagementCollector.framework/EngagementCollector](MACHOS/EngagementCollector.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksEngagementExtension.appex/BooksEngagementExtension](MACHOS/BooksEngagementExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksNotificationContentExtension.appex/BooksNotificationContentExtension](MACHOS/BooksNotificationContentExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension](MACHOS/BooksProductPageExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessIntents.appex/FitnessIntents](MACHOS/FitnessIntents.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/MirroredWidgetExtension.appex/MirroredWidgetExtension](MACHOS/MirroredWidgetExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Health.app/PlugIns/HealthMedicationsWidgetExtension.appex/HealthMedicationsWidgetExtension](MACHOS/HealthMedicationsWidgetExtension.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.EditorExtension.appex/com.apple.mobilenotes.EditorExtension](MACHOS/com.apple.mobilenotes.EditorExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.IntentsExtension.appex/com.apple.mobilenotes.IntentsExtension](MACHOS/com.apple.mobilenotes.IntentsExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker](MACHOS/MediaPicker.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicNotificationContentExtension.appex/MusicNotificationContentExtension](MACHOS/MusicNotificationContentExtension.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsEngagementExtension.appex/NewsEngagementExtension](MACHOS/NewsEngagementExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Passwords.app/Passwords](MACHOS/Passwords.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/PodcastsClassKitExtension](MACHOS/PodcastsClassKitExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension](MACHOS/com.apple.podcasts.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDiagnosticExtension.appex/StocksDiagnosticExtension](MACHOS/StocksDiagnosticExtension.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/Extensions/WeatherAppIntents.appex/WeatherAppIntents](MACHOS/WeatherAppIntents.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherDiagnosticExtension.appex/WeatherDiagnosticExtension](MACHOS/WeatherDiagnosticExtension.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents](MACHOS/WeatherIntents.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/csfdiagnose](MACHOS/csfdiagnose.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/FinishRestoreFromBackup](MACHOS/FinishRestoreFromBackup.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/amfid](MACHOS/amfid.md)
- [/usr/libexec/announced](MACHOS/announced.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/cameracaptured](MACHOS/cameracaptured.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/demod_helper](MACHOS/demod_helper.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/handwritingd](MACHOS/handwritingd.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/jetsam_priority](MACHOS/jetsam_priority.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/pcsstatus](MACHOS/pcsstatus.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/textcontextd](MACHOS/textcontextd.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/videosubscriptionsd](MACHOS/videosubscriptionsd.md)
- [/usr/libexec/wcd](MACHOS/wcd.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/otctl](MACHOS/otctl.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (11)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0xe36ac
-  __TEXT.__cstring: 0x14235
-  __TEXT.__const: 0x22204
+  __TEXT.__text: 0xe3a2c
+  __TEXT.__cstring: 0x14273
+  __TEXT.__const: 0x22814
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x2d0
   __TEXT.__constructor: 0x0

   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xcbd38
   Functions: 0
-  Symbols:   1543
-  CStrings:  2421
+  Symbols:   1544
+  CStrings:  2423
 
Symbols:
+ __Z15AVE_RegBlk_Dumpjii
CStrings:
+ "0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x"
+ "8002.26.2"
+ "Heartbeat Status 0x%x"
- "8002.24.0"

```

#### adc-rheia-d9x.im4p

>  `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x726254
+  __TEXT.__text: 0x727254
   __TEXT.__data_copy: 0x200000
-  __TEXT.__const: 0x995900
-  __TEXT.__cstring: 0x9d3f0
+  __TEXT.__const: 0x995980
+  __TEXT.__cstring: 0x9d4aa
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x4fdac
   __TEXT.__eh_frame: 0x390
-  __DATA.__const: 0x527c0
+  __DATA.__const: 0x52920
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xdf870
   __DATA._rtk_power: 0x3a8

   __DATA.__zerofill: 0x219df0
   Functions: 0
   Symbols:   0
-  CStrings:  17281
+  CStrings:  17286
 
CStrings:
+ "%s %d: bUsingCachedSetting=%d\n"
+ "%s: ch %zu slaFMinFrameRate %d\n"
+ "21:19:36"
+ "CISP_CMD_CH_DESKVIEW_MODE_SET"
+ "ChannelConfigurationApply"
+ "Oct  2 2024"
+ "[%s] CH = 0x%zx CISP_CMD_CH_DESKVIEW_MODE_SET enable %d\n"
+ "[%s]AE will use cached params! cur ts %llu us, last stop ts %llu us  cachedSettingExpiryDuration %u us\n"
+ "[%s]AWB will use cached params! cur ts %llu us, last stop ts %llu us  cachedSettingExpiryDuration %u us\n"
- "16:48:23"
- "Sep 17 2024"
- "[%s]AE will use cached params! cur ts %llu us, last stop ts %llu us  cachedAEExpiryDuration %u us\n"
- "[%s]AWB will use cached params! cur ts %llu us, last stop ts %llu us  cachedAEExpiryDuration %u us\n"

```

#### agx_a000.bin

>  `agx_a000.bin`

```diff

 
-  __TEXT.__text: 0x34668
+  __TEXT.__text: 0x347b4
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
CStrings:
+ "Sep 30 2024 01:58:41"
- "Sep 18 2024 22:27:13"

```

#### agx_a010.bin

>  `agx_a010.bin`

```diff

 
-  __TEXT.__text: 0x34470
+  __TEXT.__text: 0x345bc
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
CStrings:
+ "Sep 30 2024 02:05:14"
- "Sep 18 2024 22:33:18"

```

#### agx_b000.bin

>  `agx_b000.bin`

```diff

 
-  __TEXT.__text: 0x34568
+  __TEXT.__text: 0x346b4
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
CStrings:
+ "Sep 30 2024 02:02:42"
- "Sep 18 2024 22:30:55"

```

#### agx_b010.bin

>  `agx_b010.bin`

```diff

 
-  __TEXT.__text: 0x3437c
+  __TEXT.__text: 0x344c8
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
CStrings:
+ "Sep 30 2024 02:06:32"
- "Sep 18 2024 22:34:32"

```

#### agx_b100.bin

>  `agx_b100.bin`

```diff

 
-  __TEXT.__text: 0x34474
+  __TEXT.__text: 0x345c0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
CStrings:
+ "Sep 30 2024 02:03:57"
- "Sep 18 2024 22:32:07"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

-416.40.1.0.0
-  __TEXT.__text: 0x466668
+416.40.2.0.0
+  __TEXT.__text: 0x46677c
   __TEXT.__lcxx_override: 0x200
   __TEXT.__const: 0xdf4f8
-  __TEXT.__cstring: 0x287be
+  __TEXT.__cstring: 0x287ee
   __TEXT.__swift5_typeref: 0xc941
   __TEXT.__constg_swiftt: 0x16bbc
-  __TEXT.__swift5_fieldmd: 0xdfe8
-  __TEXT.__swift5_reflstr: 0x8421
+  __TEXT.__swift5_fieldmd: 0xdff4
+  __TEXT.__swift5_reflstr: 0x8431
   __TEXT.__swift5_types: 0x1304
   __TEXT.__swift5_proto: 0x23e4
   __TEXT.__swift5_protos: 0x4cc

   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x28
-  __TEXT.__eh_frame: 0x1f1a8
+  __TEXT.__eh_frame: 0x1f1c8
   __DATA.__got: 0x10
   __DATA.__auth_ptr: 0x268
   __DATA.__mod_init_func: 0x58
-  __DATA.__const: 0x2a398
+  __DATA.__const: 0x2a3a0
   __DATA.__objc_imageinfo: 0x8
   __DATA.__data: 0xd718
   __DATA.__shared_cache: 0xa8

   __DATA.__common: 0x1f71
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 16637
+  Functions: 16640
   Symbols:   0
-  CStrings:  4500
+  CStrings:  4501
 
CStrings:
+ " to InternalALSSample. Throwing away!"
+ "/AppleInternal/Library/BuildRoots/46f067b1-7d7d-11ef-bf8c-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.1.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/46f067b1-7d7d-11ef-bf8c-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.1.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "Unable to convert ALSReport="
- "/AppleInternal/Library/BuildRoots/de21ce75-75d2-11ef-b5e8-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.1.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/de21ce75-75d2-11ef-b5e8-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.1.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "Invalid input (start="

```

#### h17_ane_fw_theia_d9x.im4p

>  `h17_ane_fw_theia_d9x.im4p`

```diff

 
-  __TEXT.__text: 0xb0338
+  __TEXT.__text: 0x8e748
   __TEXT.__data_copy: 0x8000
-  __TEXT.__const: 0x8384
-  __TEXT.__cstring: 0x1ad15
+  __TEXT.__const: 0x4348
+  __TEXT.__cstring: 0x12c40
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.ce_env: 0x4000
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x28
-  __DATA.__const: 0x9bd8
+  __DATA.__const: 0x9b98
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xf60
+  __DATA.__data: 0xd60
   __DATA._rtk_power: 0x368
   __DATA._rtk_patchbay: 0x238
   __DATA._rtk_init_stack: 0x10000

   __DATA.__sysvars: 0x4
   __DATA._rtk_boot_l1: 0x80
   __DATA.__mod_init_func: 0x0
-  __DATA.__zerofill: 0x55978
+  __DATA.__zerofill: 0x55928
   Functions: 0
   Symbols:   0
-  CStrings:  3288
+  CStrings:  2147
 
CStrings:
+ "%s .Sanity check failure!\n"
+ "23:04:26"
+ "Couldn't find ShareMemInfoItem to free !!!\n"
+ "IPC Endpoint cmd failed %d"
+ "IPC Endpoint cmd failure"
+ "Run out of CSharedMemory !!!\n"
+ "Sep 22 2024"
+ "pProc != __null"
+ "pProg != __null"
+ "unremap WriteMessage failed\n"
- "\tFW Latency Signposts 0x%x id 0x%x ts %lld"
- "\x1b[31m\"    Found Matched Priority Q[%d]S[%d] during Termination\"\x1b[39m"
- "\x1b[31m\"ABORT queue %d slot %d (nid %d) multi segment\"\x1b[39m"
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
- "13:53:00"
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
- "Sep 17 2024"
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

#### securem3fw-d9x.im4p

>  `securem3fw-d9x.im4p`

```diff

 
-  __TEXT.__text: 0xe584
+  __TEXT.__text: 0xecf0
   __TEXT.__const: 0x3e0c
   __TEXT.__data_copy: 0x4000
   __TEXT.__cstring: 0x23a
CStrings:
+ "02:04:59"
+ "Sep 30 2024"
- "13:51:02"
- "Sep 17 2024"

```

#### sptm.t8140.release.im4p

>  `sptm.t8140.release.im4p`

```diff

-392.40.10.0.0
-  __TEXT.__cstring: 0xd55b
+392.40.12.0.0
+  __TEXT.__cstring: 0xd847
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x70
-  __TEXT.__const: 0x9d0
+  __TEXT.__const: 0xa00
   __DATA_CONST.__const: 0x5d38
   __LATE_CONST.__late_const: 0x5d630
-  __TEXT_EXEC.__text: 0x4a65c
+  __TEXT_EXEC.__text: 0x4a938
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6

   __BOOTDATA.__data: 0x14000
   Functions: 308
   Symbols:   1
-  CStrings:  1691
+  CStrings:  1701
 
CStrings:
+ "__probable(hib_page_bitmap(hib_ctx->page_list, dst_ppnum) == NULL || !hib_page_bitget(hib_ctx->page_list, dst_ppnum))"
+ "list != NULL"
+ "memcmp(hib_header_copy->handoffHMAC, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0"
+ "memcmp(hib_header_copy->hib_segs_hmac, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0"
+ "memcmp(hib_header_copy->image1PagesHMAC, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0"
+ "memcmp(hib_header_copy->image2PagesHMAC, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0"
+ "memcmp(hib_header_copy->imageHeaderHMAC, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0"
+ "memcmp(hib_header_copy->protected_metadata_hmac, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0"
+ "memcmp(hib_header_copy->sptm_rorgn_hmac, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0"
+ "memcmp(hib_header_copy->xnu_rorgn_hmac, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.1 *(22B5054e)* | 619.2.5.10.3 |
| 18.1 *(22B5069a)* | 619.2.8.10.3 |

### Dylibs

#### ⬆️ Updated (823)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ConnectivityModule.axbundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/AccessibilityBundles/HealthMedicationsUI.axbundle/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/AccessibilityBundles/HealthUI.axbundle/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/AccessibilityBundles/MobileTimer.axbundle/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/AccessibilityBundles/Music.axbundle/Music](DYLIBS/Music.md)
- [/System/Library/AccessibilityBundles/PassKitUI.axbundle/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/AccessibilityBundles/Siri.axbundle/Siri](DYLIBS/Siri.md)
- [/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin](DYLIBS/AMSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CDPAccountNotificationPlugin_IOS.bundle/CDPAccountNotificationPlugin_IOS](DYLIBS/CDPAccountNotificationPlugin_IOS.md)
- [/System/Library/Accounts/Notification/DMDAccountNotificationPlugin.bundle/DMDAccountNotificationPlugin](DYLIBS/DMDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin](DYLIBS/PCSAccountNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityHeadphoneLevelsControlCenterModule.bundle/AccessibilityHeadphoneLevelsControlCenterModule](DYLIBS/AccessibilityHeadphoneLevelsControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule](DYLIBS/FlashlightModule.md)
- [/System/Library/ControlCenter/Bundles/HeadphoneAccommodationsCCModule.bundle/HeadphoneAccommodationsCCModule](DYLIBS/HeadphoneAccommodationsCCModule.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accessibility.framework/Accessibility](DYLIBS/Accessibility.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies](DYLIBS/AACDependencies.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/ColorSync.framework/ColorSync](DYLIBS/ColorSync.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI](DYLIBS/LocalAuthenticationEmbeddedUI.md)
- [/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture](DYLIBS/LockedCameraCapture.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MediaToolbox.framework/Support/libSTS-N.dylib](DYLIBS/libSTS-N.dylib.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential](DYLIBS/SecureElementCredential.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/UIKit.framework/UIKit](DYLIBS/UIKit.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity](DYLIBS/WatchConnectivity.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
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
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoSleepComplication.bundle/NanoSleepComplication](DYLIBS/NanoSleepComplication.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFoghornFaceBundleCompanion.bundle/NTKFoghornFaceBundleCompanion](DYLIBS/NTKFoghornFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences](DYLIBS/VPNPreferences.md)
- [/System/Library/PreferenceBundles/WirelessModemSettings.bundle/WirelessModemSettings](DYLIBS/WirelessModemSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/AACCore](DYLIBS/AACCore.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation](DYLIBS/AccessibilityPlatformTranslation.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing](DYLIBS/ActivitySharing.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AeroML.framework/AeroML](DYLIBS/AeroML.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIWidget.framework/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI](DYLIBS/AppProtectionUI.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation](DYLIBS/AppStoreFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices](DYLIBS/ApplePhotonDetectorServices.md)
- [/System/Library/PrivateFrameworks/ArchetypeEngine.framework/ArchetypeEngine](DYLIBS/ArchetypeEngine.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI](DYLIBS/AssistiveTouchUI.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation](DYLIBS/BackBoardHIDEventFoundation.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/BiomeFlexibleStorage](DYLIBS/BiomeFlexibleStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BookUtility.framework/BookUtility](DYLIBS/BookUtility.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation](DYLIBS/CalendarFoundation.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices](DYLIBS/CameraOverlayServices.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CellularBridgeUI.framework/CellularBridgeUI](DYLIBS/CellularBridgeUI.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon](DYLIBS/CloudDocsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices](DYLIBS/CloudServices.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CognitiveHealth.framework/CognitiveHealth](DYLIBS/CognitiveHealth.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI](DYLIBS/CommunicationSafetySettingsUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices](DYLIBS/ControlCenterUIServices.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal](DYLIBS/CoreCDPUIInternal.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite](DYLIBS/CoreRepairLite.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore](DYLIBS/CoreServicesStore.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices](DYLIBS/DictionaryServices.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI](DYLIBS/DisembarkUI.md)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService](DYLIBS/EmbeddingService.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
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
- [/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan](DYLIBS/FitnessWorkoutPlan.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing](DYLIBS/HDRProcessing.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService](DYLIBS/HeadphoneProxFeatureService.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings](DYLIBS/HeadphoneSettings.md)
- [/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration](DYLIBS/HealthArticlesGeneration.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceAppPlugin.framework/HealthBalanceAppPlugin](DYLIBS/HealthBalanceAppPlugin.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon](DYLIBS/HealthHearingDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI](DYLIBS/HealthMedicationsVisionUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI](DYLIBS/HealthMedicationsWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService](DYLIBS/HearingModeService.md)
- [/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private](DYLIBS/HearingModeService_Private.md)
- [/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI](DYLIBS/HearingModeSettingsUI.md)
- [/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI](DYLIBS/HearingModeUI.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI](DYLIBS/HomeAI.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents](DYLIBS/HomeWidgetIntents.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMRCSTransfer.framework/IMRCSTransfer](DYLIBS/IMRCSTransfer.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache](DYLIBS/LLMCache.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices](DYLIBS/LockedContentServices.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/MacinTalk](DYLIBS/MacinTalk.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream](DYLIBS/MediaStream.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI](DYLIBS/MusicCarDisplayUI.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/NanoLeash](DYLIBS/NanoLeash.md)
- [/System/Library/PrivateFrameworks/NanoMediaBridgeUI.framework/NanoMediaBridgeUI](DYLIBS/NanoMediaBridgeUI.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NanoUniverse](DYLIBS/NanoUniverse.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay](DYLIBS/NetworkRelay.md)
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
- [/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit](DYLIBS/NewsKit.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSiriUI.framework/NotesSiriUI](DYLIBS/NotesSiriUI.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust](DYLIBS/OctagonTrust.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OmniSearchTypes.framework/OmniSearchTypes](DYLIBS/OmniSearchTypes.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI](DYLIBS/PencilPairingUI.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation](DYLIBS/PhotoFoundation.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation](DYLIBS/PhotosImagingFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation](DYLIBS/PosterFoundation.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse](DYLIBS/ProactiveShareSheetDataHarvestingLighthouse.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProofReader.framework/ProofReader](DYLIBS/ProofReader.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport](DYLIBS/QuickLookSupport.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/RESync.framework/RESync](DYLIBS/RESync.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface](DYLIBS/SavageCameraInterface.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingAccessibilityService.framework/ScreenSharingAccessibilityService](DYLIBS/ScreenSharingAccessibilityService.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit](DYLIBS/SecureCaptureKit.md)
- [/System/Library/PrivateFrameworks/Seeding.framework/Seeding](DYLIBS/Seeding.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices](DYLIBS/SeymourClientServices.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework](DYLIBS/SiriAppLaunchUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriContactsCommon.framework/SiriContactsCommon](DYLIBS/SiriContactsCommon.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo](DYLIBS/SiriGeo.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSettingsUI.framework/SiriSettingsUI](DYLIBS/SiriSettingsUI.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework](DYLIBS/SiriVideoUIFramework.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport](DYLIBS/SoftwareUpdateCoreSupport.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding](DYLIBS/SpotlightEmbedding.md)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation](DYLIBS/SpotlightFoundation.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation](DYLIBS/SpotlightRecommendation.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport](DYLIBS/SpotlightSettingsSupport.md)
- [/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal](DYLIBS/SpotlightUIInternal.md)
- [/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared](DYLIBS/SpotlightUIShared.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/TextInputTestingKit](DYLIBS/TextInputTestingKit.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
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
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/WelcomeKit](DYLIBS/WelcomeKit.md)
- [/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore](DYLIBS/WelcomeKitCore.md)
- [/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI](DYLIBS/WelcomeKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore](DYLIBS/_MusicKitInternal_MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport](DYLIBS/CaptiveNetworkSupport.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoProcessors/BarcodeScanner.videoprocessor](DYLIBS/BarcodeScanner.videoprocessor.md)
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
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libSoftwareUpdateSSO.dylib](DYLIBS/libSoftwareUpdateSSO.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/swift/libswiftUIKit.dylib](DYLIBS/libswiftUIKit.dylib.md)

</details>

### Feature Flags

#### ⬆️ Updated (13)

<details>
  <summary><i>View Updated</i></summary>

#### Wallet.plist

>  `Domain/Wallet.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>SavingsFDICSignage</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>SearchFinHealth</key>
 	<dict>
 		<key>Enabled</key>

```

#### CloudServices.plist

>  `Domain/CloudServices.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>Guitarfish</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>LogEscrowOperations</key>
 	<dict>
 		<key>Enabled</key>

```

#### Health.plist

>  `Domain/Health.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>nebula</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>orchestration_categories</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### NotificationsUI.plist

>  `Domain/NotificationsUI.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>962bbdc2-15fe-b429-6de4-344847c93104</string>
 	</dict>
+	<key>GreymatterOnboardingWithAppCategorization</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+		<key>DisclosureRequired</key>
+		<string>962bbdc2-15fe-b429-6de4-344847c93104</string>
+	</dict>
 	<key>GreymatterOnboardingiOS</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### PeopleSuggester.plist

>  `Domain/PeopleSuggester.plist`

```diff

 <dict>
 	<key>pass_data_collection_only</key>
 	<dict>
-		<key>Enabled</key>
-		<true/>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
 	</dict>
 	<key>pass_v2</key>
 	<dict>

```

#### Podcasts.plist

>  `Domain/Podcasts.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>DisableConnectedSubscriptionsHardcode</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>DisableHomePodCloudSync</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### TVApp.plist

>  `Domain/TVApp.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>nimbus</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>puiv</key>
 	<dict>
 		<key>Enabled</key>

```

#### AppleAccount.plist

>  `Domain/AppleAccount.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>LCDeletionChangeCKStatusToDeclined</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>LoadRemoteUI</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>iCloudConfigurationBagDaemonCache</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 </dict>
 </plist>
 

```

#### AppleMediaServices.plist

>  `Domain/AppleMediaServices.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>FraudScoreReportV2AuthToken</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>HideAppleTVVersionForMobileGestaltUserAgent</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### DataDetectorsCore.plist

>  `Domain/DataDetectorsCore.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>DDConfetti</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>DDMLEnhancement</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Messages.plist

>  `Domain/Messages.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>waldoCPolish</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>wmr</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Photos.plist

>  `Domain/Photos.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>d33f0adf-402f-301d-7091-d4fce7907d83</string>
 	</dict>
+	<key>SharedAlbumsDBR</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>SmartCopyPaste</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### GlobalDisclosures.plist

>  `GlobalDisclosures.plist`

```diff

 		<key>Disclosed</key>
 		<true/>
 	</dict>
+	<key>13c9c430-904f-56ad-005a-b95b9abd0ba7</key>
+	<dict>
+		<key>Disclosed</key>
+		<true/>
+	</dict>
 	<key>2298f8e4-f510-4776-b2c1-a85ea314b1f8</key>
 	<dict>
 		<key>Disclosed</key>

```


</details>

## EOF
