# 18.4 (22E5200s) .vs 18.4 (22E5216h)

## IPSWs

- `iPhone17,1_18.4_22E5200s_Restore.ipsw`
- `iPhone17,1_18.4_22E5216h_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.4 *(22E5200s)* | 24.4.0 | 11417.100.533.502.4~3 | Sun, 16Feb2025 02:28:25 PST |
| 18.4 *(22E5216h)* | 24.4.0 | 11417.100.564.502.1~1 | Tue, 25Feb2025 21:30:30 PST |

### Kexts

#### ⬆️ Updated (39)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.AGXFirmwareKextG17PRTBuddy`

```diff

-325.25.6.0.0
+325.30.0.0.0
   __TEXT.__const: 0x33c
-  __TEXT.__cstring: 0x663
-  __TEXT_EXEC.__text: 0x2e78
+  __TEXT.__cstring: 0x67a
+  __TEXT_EXEC.__text: 0x2ea8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x38
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0xa8
   __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x80
   Functions: 71
   Symbols:   0
-  CStrings:  34
+  CStrings:  35
 
CStrings:
+ "setBudgetToAGXFunction"

```

>  `com.apple.AGXG17P`

```diff

-325.25.6.0.0
-  __TEXT.__const: 0x54c4
+325.30.0.0.0
+  __TEXT.__const: 0x4e5c
   __TEXT.__os_log: 0x318
-  __TEXT.__cstring: 0xf37d
-  __TEXT_EXEC.__text: 0xcfeb0
+  __TEXT.__cstring: 0xf38b
+  __TEXT_EXEC.__text: 0xd0ed8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13c0
   __DATA.__common: 0x10
-  __DATA.__bss: 0x2ed8
-  __DATA_CONST.__auth_got: 0xc38
+  __DATA.__bss: 0x3260
+  __DATA_CONST.__auth_got: 0xc18
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x398
   __DATA_CONST.__mod_term_func: 0x2e0
-  __DATA_CONST.__const: 0x10498
+  __DATA_CONST.__const: 0x10530
   __DATA_CONST.__kalloc_type: 0x25c0
   __DATA_CONST.__kalloc_var: 0x32f0
-  Functions: 3029
+  Functions: 3039
   Symbols:   0
-  CStrings:  1910
+  CStrings:  1913
 
CStrings:
+ "12111111211222212211111121122221221111112112222122122222222222222221122111111111222222222111112121211212112121121211212112121121211212112121121211212112121121211111111122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122222221111221211212111111112222222222122222111122121121211111111222222222212112222222222222222222222222222222222222222222222222222222222222222222222221211211222222222222222222111111221212222222221222221111122121222222222122222111112212122222222212222211111221212222222221222221111122121222222222122222111112212122222222212222211111222111111222111111222111111222111111222111111222111111222111111222111111222111111222111111222111111222111111222111111222112111112211111222111111221121122111111111111111111111111111111111111111111111111111111122222222222222222222222222221111112212122222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111122222222"
+ "12111122222111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "1221111111122222222222111121222222222222222222222222222211212111111"
+ "12211122211222222111"
+ "12222222222221112222"
+ "122222222222211122222"
+ "CounterList"
+ "CounterValues"
+ "Counter_%u"
+ "Dynamic Power Control Regs"
+ "Feb 25 2025 21:08:46"
+ "Fender Power Transition Regs (G16G only)"
+ "counter_list"
+ "rif_shadow"
+ "setBudgetToAGXFunction"
- "12111111211222212211111121122221221111112112222122122222222222222221122111111111222222222111112121211212112121121211212112121121211212112121121211212112121121211111111122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122211122222221111221211212111111112222222222122222111122121121211111111222222222212112222222222222222222222222222222222222222222222222222222222222222222222221211211222222222222222222111111221212222222221222221111122121222222222122222111112212122222222212222211111221212222222221222221111122121222222222122222111112212122222222212222211111222111111222111111222111111222111111222111111222111111222111111222111111222111111222111111222111111222111111222111111222112111112211111222111111221121122111111111111111111111111111111111111111111111111111111222222222222222222222222222111111221212222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111122222222"
- "12111122222111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "122111111112222222222111121222222222222222222222222222211212111111"
- "1221112221122222111"
- "1222222222221112222"
- "12222222222211122222"
- "FSTP Power Counters"
- "Feb 16 2025 04:20:10"
- "GPU Lost Perf Reasons"
- "MXU Dynamic Power Control Regs"
- "Power Counter FSTP %u"
- "PowerCounterData"

```

>  `com.apple.EXBrightKext`

```diff

-1902.100.104.0.0
+1902.100.115.0.0
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x1e22
-  __TEXT_EXEC.__text: 0xc2f8
+  __TEXT.__cstring: 0x1ff6
+  __TEXT_EXEC.__text: 0xd1fc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x68
   __DATA.__bss: 0x2
-  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x16e8
+  __DATA_CONST.__const: 0x17e8
   __DATA_CONST.__kalloc_type: 0x80
-  Functions: 304
+  Functions: 333
   Symbols:   0
-  CStrings:  128
+  CStrings:  136
 
CStrings:
+ "\"TB_ASSERT: \" \"(server->getpilbrightness != NULL) && \\\"implementation for getPILBrightness is not present\\\"\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getpilenablementstate != NULL) && \\\"implementation for getPILEnablementState is not present\\\"\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->setuibrightness != NULL) && \\\"implementation for setUIBrightness is not present\\\"\" @%s:%d"
+ "EXBrightPILCommonInterface_C.c"
+ "EXBrightUIBrightness"
+ "I12@?0C8"
+ "I12@?0I8"
+ "I36@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBfffff}}8"
+ "[%s] [ERR] Failed to set UI brightness\n"
+ "v36@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBfffff}}8"
- "I32@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBffff}}8"
- "v32@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBffff}}8"

```

>  `com.apple.driver.AppleAVD`

```diff

-859.0.1.0.0
-  __TEXT.__os_log: 0x1629a
-  __TEXT.__cstring: 0x5cf3
+862.0.0.0.0
+  __TEXT.__os_log: 0x15e72
+  __TEXT.__cstring: 0x59b2
   __TEXT.__const: 0xcebf8
-  __TEXT_EXEC.__text: 0x5b3ec
+  __TEXT_EXEC.__text: 0x5a454
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x4278
+  __DATA_CONST.__const: 0x4098
   __DATA_CONST.__kalloc_type: 0x30c0
-  __DATA_CONST.__kalloc_var: 0x1040
-  Functions: 1969
+  __DATA_CONST.__kalloc_var: 0xfa0
+  Functions: 1904
   Symbols:   0
-  CStrings:  1586
+  CStrings:  1568
 
CStrings:
+ "1211111212221212111111112111111111211111221111221111111111121112222222222222222222222222222212222222222222222222222222222222211111111111111111111111111111111222222222222222211111111111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121222111111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221"
+ "12121112112111"
+ "121221112112111"
+ "122222222222222222222222222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "1222222222222222222222222222222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "12222222222222222222222222222222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221112222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "12222222222222222222222222222222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "122222222222222222222222222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "AppleAVD: ERROR: %s(): Got a cryptor but scheme is none!\n"
+ "AppleAVD: ERROR: %s(): NULL crypt ref!\n"
+ "AppleAVD: ERROR: %s(): setMemoryDescriptor failed, even after flushing cache. status=0x%x"
+ "AppleAVD: INFO: %s(): setMemoryDescriptor failed with status=0x%x. Flushing mapper cache, then retry."
+ "AppleAVD: INFO: %s(): setMemoryDescriptor success after flushing mapper cache"
+ "virtual bool CPriorityQueueViola::isVPAvailableForDecodeCmd(uint8_t *, uint32_t, uint32_t)"
- "%s(): DKey physical addr = 0x%llx, nAvdIdx = %d\n"
- "121111121222121211111111211111111121111122111122111111111112111222222222222222222222222222221222222222222222222222222222222221111111111111111111111111111111122221111111111111111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212121212221212121222121212122212122211111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222222222222222222222222222"
- "12121112112112"
- "1212211121121112"
- "12222222222222222222222222222222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "122222222222222222222222222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "1222222222222222222222222222222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "12222222222222222222222222222222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "122222222222222222222222222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "AppleAVD: AppleAVDUserClient::SetCryptSession -- error null crypt ref"
- "AppleAVD: AppleAVDUserClient::SetCryptSession -- scheme is none!"
- "AppleAVD: ERROR: %s() called outside of gated context"
- "AppleAVD: ERROR: %s(): Frame Param Q state %d was not set to resubmitted!\n"
- "AppleAVD: ERROR: %s(): clientID %d not matching with resubmit client %d "
- "AppleAVD: ERROR: %s(): setMemoryDescriptor failed 0x%x"
- "AppleAVD: ERROR: %s: Unable to insert encrypt property: %d!\n"
- "AppleAVD: ERROR: %s: Unable to resubmit command: %d!\n"
- "AppleAVD: ERROR: %s: Unable to set state to resubmit: %d!\n"
- "AppleAVD: INFO: %s: resubmitQueue[%d].clientID=%d resubmitQueue[%d].cmdID=%d resubmitQueue[%d].frameNumber=%d\n"
- "getDecodeBufInFrameParamQGated"
- "powerChangeDoneGated"
- "releaseFrameParamQSlotGated"
- "resetUpdateIV"
- "setResubmitFrameQstate"
- "sleepFParamQSubmissionThreadGated"
- "sleepM3CmdQSubmissionThreadGated"
- "submitCmdToFParamQGated"
- "submitCmdToM3CmdQGated"
- "virtual bool CPriorityQueueViola::isVPAvailableForDecodeCmd(uint8_t *, uint32_t, uint32_t, bool)"
- "waitForClientsPendingCommandsGated"
- "waitForFParamQSubmissionGated"
- "waitForM3CmdQSubmissionGated"

```

>  `com.apple.driver.AppleCS42L79Audio`

```diff

-840.23.0.0.0
+840.25.0.0.0
   __TEXT.__cstring: 0x1ea2
   __TEXT.__os_log: 0x27f9
   __TEXT.__const: 0x3d0
-  __TEXT_EXEC.__text: 0x11d34
+  __TEXT_EXEC.__text: 0x11d0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x140

```

>  `com.apple.driver.AppleDiskImages2`

```diff

-385.100.25.0.0
-  __TEXT.__cstring: 0x2007
-  __TEXT.__os_log: 0x11a2
+385.100.32.0.0
+  __TEXT.__cstring: 0x20c4
+  __TEXT.__os_log: 0x11d7
   __TEXT.__const: 0x90
-  __TEXT_EXEC.__text: 0xd660
+  __TEXT_EXEC.__text: 0xd808
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x498
-  __DATA.__common: 0x118
+  __DATA.__data: 0x4e8
+  __DATA.__common: 0x120
   __DATA.__bss: 0x1
   __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0xa0

   __DATA_CONST.__const: 0x1cb8
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0xa0
-  Functions: 294
+  Functions: 296
   Symbols:   0
-  CStrings:  277
+  CStrings:  281
 
CStrings:
+ "385.100.32"
+ "[%d] %s::%d: Storage features: unmap=%d, barrier=%d\n"
+ "bool AppleDiskImageDevice::AddStorageFeaturesDict(bool, bool)"
+ "didevice count of page faulted buffers that initiated read/write requests"
+ "didevice count of page faulted buffers that initiated unmap requests"
+ "didevice_thread_mapped_buf_unmaps"
- "385.100.25"
- "didevice count of mapped buffers writes by thread"

```

>  `com.apple.driver.AppleEpochManager`

```diff

-10.0.0.0.0
-  __TEXT.__cstring: 0xb91
+11.0.0.0.0
+  __TEXT.__cstring: 0x8bc
   __TEXT.__const: 0x38
-  __TEXT_EXEC.__text: 0x23c8
+  __TEXT_EXEC.__text: 0x1c8c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__kalloc_type: 0x80
-  Functions: 89
+  Functions: 77
   Symbols:   0
-  CStrings:  78
+  CStrings:  63
 
CStrings:
+ "121111121222121212211211"
- "%s%s:\n%s    Device is somehow missing a product entry in the device tree.\n"
- "%s%s:\n%s    No recovery EPLY in nvram.\n"
- "%s%s:\n%s    No recovery EPLY is invalid length, got %u expected %lu.\n"
- "%s%s:\n%s    got invalid eply struct size\n"
- "/product"
- "1211111212221212122211211"
- "40A0DDD2-77F8-4392-B4A3-1E7304206516:RecoveryEPLY"
- "IOReturn AppleEpochManager::commitRecoveryEplyGated(eply_t *)"
- "arguments"
- "bool AppleEpochManager::deviceSupportsRecoveryOS()"
- "nullptr != nvram"
- "nullptr != recovery_eply_data"
- "nullptr != recovery_eply_key"
- "static IOReturn AppleEpochManagerUserClient::DispatchUserCommitRecoveryEpoch(AppleEpochManagerUserClient *, void *, IOExternalMethodArguments *)"
- "supports-recoveryos"
- "void AppleEpochManager::setNVRAMKeyValueAndSync(const char *, OSObject *)"

```

>  `com.apple.driver.AppleFirmwareKit`

```diff

-531.100.29.0.0
-  __TEXT.__cstring: 0x4090
-  __TEXT.__os_log: 0x1148
+531.100.32.0.0
+  __TEXT.__cstring: 0x4091
+  __TEXT.__os_log: 0x1198
   __TEXT.__const: 0xa8
-  __TEXT_EXEC.__text: 0x3c66c
+  __TEXT_EXEC.__text: 0x3c684
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4b8
   __DATA.__common: 0x700

   __DATA_CONST.__const: 0xd3b0
   __DATA_CONST.__kalloc_type: 0x1880
   __DATA_CONST.__kalloc_var: 0x50
-  Functions: 2017
+  Functions: 2016
   Symbols:   0
-  CStrings:  653
+  CStrings:  654
 
CStrings:
+ "12111112122212121121111211111222222121212111122111122212"
+ "[AFKEPInterfaceV2:%p]Unexpected Response (pktLen %i pktType 0x%x commandID:%i)\n"
- "1211111212221212112111121111122222121212111122111122212"

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-8.507.0.0.0
+8.508.0.0.0
   __TEXT.__const: 0x6f0
-  __TEXT.__cstring: 0xc67a
-  __TEXT.__os_log: 0x34390
-  __TEXT_EXEC.__text: 0xb8880
+  __TEXT.__cstring: 0xc831
+  __TEXT.__os_log: 0x346e3
+  __TEXT_EXEC.__text: 0xb9dfc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3948
   __DATA.__common: 0x3f0
   __DATA.__bss: 0x368
-  __DATA_CONST.__auth_got: 0x930
+  __DATA_CONST.__auth_got: 0x938
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__mod_init_func: 0xd8
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x7590
+  __DATA_CONST.__const: 0x7670
   __DATA_CONST.__kalloc_type: 0x2780
   __DATA_CONST.__kalloc_var: 0x2e90
-  Functions: 2149
+  Functions: 2174
   Symbols:   0
-  CStrings:  3741
+  CStrings:  3760
 
CStrings:
+ "\"TB_ASSERT: \" \"(server->debugreadproperty != NULL) && \\\"implementation for DebugReadProperty is not present\\\"\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->debugwriteproperty != NULL) && \\\"implementation for DebugWriteProperty is not present\\\"\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->preparepoweroff != NULL) && \\\"implementation for preparePowerOff is not present\\\"\" @%s:%d"
+ "ANE%d: %s: Exceeded max retries. Proceeding with transition\n"
+ "ANE%d: %s: Exclave work paused with %d retries, %d msg send attempts\n"
+ "ANE%d: %s: Given vp is NULL\n"
+ "ANE%d: %s: Issuing commandWakeup for sleeping upcall thread\n"
+ "ANE%d: %s: ModeSwitch completed... proceeding\n"
+ "ANE%d: %s: Next upcall will invoke commandSleep for testing\n"
+ "ANE%d: %s: Not in Exclave mode, no mode switch pending\n"
+ "ANE%d: %s: Retrying Exclave work pause, Retry count %d\n"
+ "ANE%d: %s: Timed out waiting for in-flight ModeSwitch to complete, sleepResult=0x%x, retry count %d\n"
+ "ANE%d: %s: Waiting for in-flight Exclave cycle to complete\n"
+ "ANE%d: %s: preparePowerOff call completed, status from Exclave %d\n"
+ "ANE%d: %s: preparePowerOff call failed\n"
+ "ANE%d: %s: vfs_context is NULL\n"
+ "ANE%d: %s: vnode from mapped address check failed, vp: %p vnodeAddress: 0x%lx\n"
+ "ANE%d: %s: vp: %p address: 0x%llx vnodeAddress: 0x%lx vnodeID: 0x%x start: 0x%llx length: 0x%llx\n"
+ "ANE_ExclavePreparePowerOff"
+ "aneExclavePreparePowerOff"
+ "aneValidateVnodeFromMappedAddress"
- "ANE%d: %s: Exclave work paused, status from Exclave %d\n"
- "ANE%d: %s: PauseExclaveWork call failed\n"

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-3.504.14.0.0
+3.509.0.0.0
   __TEXT.__const: 0xa1d0
-  __TEXT.__cstring: 0x176f4
-  __TEXT.__os_log: 0x14301
-  __TEXT_EXEC.__text: 0x9a000
+  __TEXT.__cstring: 0x17d40
+  __TEXT.__os_log: 0x14893
+  __TEXT_EXEC.__text: 0x9ba7c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a0
   __DATA.__common: 0x4c8
   __DATA.__bss: 0x200
-  __DATA_CONST.__auth_got: 0x828
+  __DATA_CONST.__auth_got: 0x830
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0xc2c0
+  __DATA_CONST.__const: 0xddf0
   __DATA_CONST.__kalloc_type: 0x1240
   __DATA_CONST.__kalloc_var: 0xa50
-  Functions: 1758
+  Functions: 1770
   Symbols:   0
-  CStrings:  3049
+  CStrings:  3093
 
CStrings:
+ "\"TB_FATAL: \" \"invalid value: unexpected bits, 0x%llx\" @%s:%d"
+ "12111111114111222221212212"
+ "211"
+ "AppleH16CamIn:%s - CISP_CMD_CH_TAILSPIN_NOTIFICATION ch %u tailspinSource %d tailspinCode 0x%x\n"
+ "AppleH16CamIn:%s - Denied Access to RPC ID [%d]\n"
+ "AppleH16CamIn:%s - Invalid RPC request ID(s) - Aborting\n"
+ "AppleH16CamIn:%s - Loaded configuration %d\n"
+ "AppleH16CamIn:%s - Querying channel index failed, tberr: 0x%08X\n"
+ "AppleH16CamIn:%s - Querying channel index failed, tberr: 0x%08X, res: 0x%08X\n"
+ "AppleH16CamIn:%s - Reading sensor NVM failed, tberr: 0x%08X\n"
+ "AppleH16CamIn:%s - Reading sensor NVM failed, tberr: 0x%08X, res: 0x%08X\n"
+ "AppleH16CamIn:%s - Secure sensor power off - chan: %d, res: 0x%08X\n"
+ "AppleH16CamIn:%s - Secure sensor power on - bootOpt: %d, chan: %d, res: 0x%08X\n"
+ "AppleH16CamIn:%s - firmware teardown notification idl call failed=%d\n"
+ "AppleH16CamIn:%s - firmware teardown notification returned error=0x%llx\n"
+ "AppleH16CamIn:%s - messageClients(kH16ISPTailspinAEReqLate, 0x%016llx)\n"
+ "AppleH16CamIn:%s - messageClients(kH16ISPTailspinExclaveEmptyQueue, 0x%016llx)\n"
+ "AppleH16CamIn:%s - sendcmdnotifyfirmwareteardown idl call failed=%d\n"
+ "AppleH16CamIn:%s - unknown tailspinSource %d)\n"
+ "ECNotifyFirmwareTearDownSearApproved_block_invoke"
+ "ECQueryChannelIndex"
+ "ECReadNVMData"
+ "ISPEngineECInterface_tightbeam_C.c"
+ "ISP_PowerOffSecureSensor_gated"
+ "ISP_PowerOnSecureSensor_gated"
+ "ISP_ScheduleWork_gated"
+ "ISP_SecureCheckRPCCommands"
+ "checkForWork_block_invoke_5"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_forcecleanup__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_forcereset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_ispenginedirtyoff__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_ispengineoff__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_ispengineon__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_notifyfirmwareteardown__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_querychannelindex__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}I)}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_readnvmdata__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_securem3isr__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v32@?0{exclavecoreispeng_ispengineexclavecore_exclaveisphardwareirq__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{exclavecoreispeng_exclaveisphardwareirqreturn_s=QBI})}8"
- "12111111112111222221212212"
- "ISPEngineECInterface_tightbeam.c"
- "v24@?0{exclavecoreispeng_ispengineexclavecore_forcecleanup__result_s=C(?={exclavecoreispeng_exclavesisperror_s=Q})}8"
- "v24@?0{exclavecoreispeng_ispengineexclavecore_forcereset__result_s=C(?={exclavecoreispeng_exclavesisperror_s=Q})}8"
- "v24@?0{exclavecoreispeng_ispengineexclavecore_ispenginedirtyoff__result_s=C(?={exclavecoreispeng_exclavesisperror_s=Q})}8"
- "v24@?0{exclavecoreispeng_ispengineexclavecore_ispengineoff__result_s=C(?={exclavecoreispeng_exclavesisperror_s=Q})}8"
- "v24@?0{exclavecoreispeng_ispengineexclavecore_ispengineon__result_s=C(?={exclavecoreispeng_exclavesisperror_s=Q})}8"
- "v24@?0{exclavecoreispeng_ispengineexclavecore_notifyfirmwareteardown__result_s=C(?={exclavecoreispeng_exclavesisperror_s=Q})}8"
- "v24@?0{exclavecoreispeng_ispengineexclavecore_securem3isr__result_s=C(?={exclavecoreispeng_exclavesisperror_s=Q})}8"
- "v32@?0{exclavecoreispeng_ispengineexclavecore_exclaveisphardwareirq__result_s=C(?={exclavecoreispeng_exclavesisperror_s=Q}{exclavecoreispeng_exclaveisphardwareirqreturn_s=QBI})}8"

```

>  `com.apple.driver.AppleIDV`

```diff

-7.415.1.0.0
+7.418.0.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x137e
+  __TEXT.__cstring: 0x137c
   __TEXT_EXEC.__text: 0x7bf8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
CStrings:
+ "7.418"
- "7.415.1"

```

>  `com.apple.driver.AppleJPEGDriver`

```diff

-7.6.3.0.0
-  __TEXT.__cstring: 0x26c3
-  __TEXT.__os_log: 0x8346
-  __TEXT.__const: 0x3484
-  __TEXT_EXEC.__text: 0x28980
+7.6.8.0.0
+  __TEXT.__cstring: 0x26fd
+  __TEXT.__os_log: 0x8506
+  __TEXT.__const: 0x34b4
+  __TEXT_EXEC.__text: 0x2914c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2108
   __DATA.__common: 0x358

   __DATA_CONST.__mod_term_func: 0xa8
   __DATA_CONST.__const: 0x4578
   __DATA_CONST.__kalloc_type: 0xbc0
-  Functions: 1588
+  Functions: 1590
   Symbols:   0
-  CStrings:  458
+  CStrings:  465
 
CStrings:
+ "122111111111111122112222222122222"
+ "AppleJPEGDriver: %s : Codec %d, Task ID %u Async %d"
+ "AppleJPEGDriver: %s : Dimension Info: %d x %d"
+ "AppleJPEGDriver: %s : Error Request Info\n"
+ "AppleJPEGDriver: %s : Error! NULL JPEG request, returnFromInterrupt = %d\n"
+ "AppleJPEGDriver: %s : codec=%d, Compressed jpeg size %d > output buffer size, input [%dw x% dh], encoding quality setting %u\n"
+ "AppleJPEGDriver: %s : image_mode %d, submode %d"
+ "AppleJPEGDriver: %s() :: WARNING: function-set_perf_state_floor did not set perf to %d! (result = %d)\n"
+ "AppleJPEGDriver: %s(): TIMEOUT %dms\n"
+ "AppleJPEGDriver: %s(): unknown %dms - status: 0x%x\n"
+ "AppleJPEGDriver: %s: decode v2c:%d, cropping %d, scaling %d"
+ "AppleJPEGDriver: %s: encode tiled mode: %d, quality: %d, restart: %d"
+ "AppleJPEGDriver: * %s [%p] : task [0x%p] client close %p\n"
+ "void AppleJPEGHal::showErrorRequestInfo(ajpeg_setup_t *)"
- "12111111111111122112222222122222"
- "AppleJPEGDriver: %s() :: failed enable the clock !\n"
- "AppleJPEGDriver: %s() :: function-set_perf_state_floor failed set perf to %d!\n"
- "AppleJPEGDriver: %s(): TIMEOUT %dms"
- "AppleJPEGDriver: %s(): unknown %dms - status: 0x%x"
- "AppleJPEGDriver: %s: codec=%d, return 0x%x\n"
- "AppleJPEGDriver: * %s [%p] : task [0x%p] client close %p"

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-149.18.0.0.0
-  __TEXT.__const: 0x64798
-  __TEXT.__cstring: 0x19030
-  __TEXT_EXEC.__text: 0x107d54
+149.28.1.0.0
+  __TEXT.__const: 0x64e28
+  __TEXT.__cstring: 0x19cad
+  __TEXT_EXEC.__text: 0x10d418
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x1fe98
-  __DATA.__common: 0x2280
-  __DATA.__bss: 0x1140
-  __DATA_CONST.__auth_got: 0x568
+  __DATA.__data: 0x1ff00
+  __DATA.__common: 0x22c8
+  __DATA.__bss: 0x1158
+  __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__mod_init_func: 0x5b8
-  __DATA_CONST.__mod_term_func: 0x590
-  __DATA_CONST.__const: 0x22fa0
-  __DATA_CONST.__kalloc_type: 0x4180
-  __DATA_CONST.__kalloc_var: 0x5f0
-  Functions: 7598
+  __DATA_CONST.__mod_init_func: 0x5c0
+  __DATA_CONST.__mod_term_func: 0x598
+  __DATA_CONST.__const: 0x237d8
+  __DATA_CONST.__kalloc_type: 0x4540
+  __DATA_CONST.__kalloc_var: 0x780
+  Functions: 7804
   Symbols:   0
-  CStrings:  2704
+  CStrings:  2771
 
CStrings:
+ " Client closed with requests not notified! (%u / %u)!\n"
+ " Scaler[%d] invalidateFrameState Req=%d\n"
+ " Stop client's async thread!\n"
+ "\"[%s] \" \"Request retain count %d, possible memory leak!\\n\" @%s:%d"
+ "\"[IOSA] Unexpected frame_id (req %u prio %u)\\n\" @%s:%d"
+ "/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator_kexts/AppleM2ScalerCSCDriverFilters.h"
+ "/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator_kexts/MSR23BackwardsCompatibleFilter.cpp"
+ "11111111212"
+ "12000000200000002111121122220000"
+ "1211111212221212122211122111222022121111111111112000000020000000212221111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112"
+ "121111222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222212212212212211222222222222222222222222222222212222222222222222222222222222122222222221122222222222222222222222222222222222121212121212121211112111111122111211121212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222222222222212212112121121211212112121121211212112121100020000000211111111000000020000000"
+ "1211221212212122121221212212122121221212212122121221212212000000200000002211222012000000200000002111121122220000"
+ "122222121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212121"
+ "1222222222212111111112111111111111111111122122112211112112222222222222111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220002000000022000000"
+ "1222222222212111111112111111111111111111122122112211112112222222222222111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220002000000022200000"
+ "122222222222222221122222222"
+ "12222222222222222112222222212111121122222"
+ "12222222222222222112222222212111121122222222222222"
+ "1222222222222222211222222221222"
+ "Allocating backwards compatible filter for custom chroma filters.\n"
+ "Allocating backwards compatible filter for custom filters.\n"
+ "Cannot enable symmetric scaling for this verison of HW\n"
+ "Couldn't allocate custom fields buffer\n"
+ "Disabling chroma filter backwards compat\n"
+ "FDR pointers %lld %lld previous (%lld %lld)\n "
+ "Filter bins not allocated\n"
+ "Firmware stall %d!\n"
+ "ForceDefaultFilters"
+ "IOSurfaceAcceleratorCapabilitiesSymmetricScaling"
+ "MSR23: Not setting custom fields ptr\n"
+ "MSR23BackwardsCompatibleFilter"
+ "Neighbor Channel Buffer Size req %d (%#zx, %#zx)\n"
+ "Publishing Custom HScaler Caps : Taps: %u Phases: %u\n"
+ "Publishing Custom VScaler Caps : Taps: %u Phases: %u\n"
+ "Quadra Bayer transforms cannot contain special filters\n"
+ "Req %d reInit\n"
+ "Request retain count %d, possible memory leak!\n"
+ "Request: %p, Neighbor Channel (Col=%#llx, Row=%#llx) %x page (%#lx)\n"
+ "SDR pointers %lld %lld previous (%lld %lld)\n "
+ "Scaler[%d]:activateAndExecuteTransform_gatedContext request %d\n"
+ "Setting allocated custom fields buffer, %p\n"
+ "StrideNotMultipleOf32"
+ "Symmetric Scaling is not yet enabled with Rotations and Flips \n"
+ "SymmetricScaling"
+ "WriteAddressNot128aligned"
+ "[%s] Setting Filter Adaptation Type to Symmetric Adaptation \n"
+ "[%s]Forcing default filter \n"
+ "[%s][%s](%d)Setting Custom Coefficient 0x%x (%p)\n"
+ "[%s][%s]Forcing Default Filter Bin: %d \n"
+ "[COSITE] Dest Surface Cositing Bottom, hPos:post(1), vPos:pre(0)\n"
+ "[COSITE] Dest Surface Cositing BottomLeft, hPos:pre(0), vPos:pre(0)\n"
+ "[COSITE] Dest Surface Cositing Center, hPos:post(1), vPos:Post(1)\n"
+ "[COSITE] Dest Surface Cositing Default, hPos:post(1), vPos:post(1)\n"
+ "[COSITE] Dest Surface Cositing Left, hPos:pre(0), vPos:Post(1)\n"
+ "[COSITE] Dest Surface Cositing Top Left, hPos:pre(0), vPos:pre(0)\n"
+ "[COSITE] Dest Surface Cositing Top, hPos:post(1), vPos:pre(0)\n"
+ "[COSITE] Using Default CHDWN Coeffs v: %d, h:%d\n"
+ "[COSITE] Using VE CHDWN Coeffs, v: %d, h: %d\n"
+ "[COSITE] Using VE CHDWN InterpPos, v:POST, h: POST\n"
+ "[FilterComp]Returning 0x%x for t:%d p:%d\n"
+ "[IOSA][Boot ] PMGR: init register aperture %llx : %llx\n"
+ "[SYM] Configuring ChromaDDAInit[%s] as 0x%x (%s%d.%s%u)\n"
+ "[SYM] Configuring LUMADDAInit[%s] as 0x%x (%s%d.%s%u)\n"
+ "[SYM]Got Symmetric Scaling Option \n"
+ "[SYM]Got Symmetric Scaling RuntimeProperty \n"
+ "[SYM][%s] Calculating symmetric DDAInit %s%d.%s%u srcDim %s%d.%s%u dstDim: %s%d.%s%u \n"
+ "[SYM][%s] Capping DDAInit to 2.0 \n"
+ "[SYM][%s] Capping DDAinit to -1.0\n"
+ "[Unimplemented] Multiple Requests (%d) Need Reset (SD needs_reset) [use msr_panic_mask=0 to turn off]"
+ "adaptDDAInitForSymmetricScaling"
+ "allocateBlockDescriptors"
+ "allocateFilter"
+ "applyChromaCustomFilter"
+ "configureDDAInit_gatedContext"
+ "customFieldsPtr doesnt exist\n"
+ "deAllocateFrameByRequest %d, frame %d, active window %d / %d\n"
+ "dequeueFrame frame %u request %d, active window %d / %d\n"
+ "finishAndReleaseRequest_gated"
+ "firmwareRecovery - activateDART(false) failed: 0x%x\n"
+ "gatherOptions"
+ "get"
+ "getCustomFields returned 0\n"
+ "msr_chdwn"
+ "msr_chroma_filter_bc_disable"
+ "msr_custom_filter_bc_disable"
+ "msr_force_default_filters"
+ "msr_multi_frames_proc"
+ "msr_publish_custom_hscaler_caps"
+ "msr_publish_custom_vscaler_caps"
+ "msr_publish_real_scaler_caps"
+ "msr_symmetric_scaling_debug"
+ "notification port already registered!\n"
+ "notifyFrameEnqueueCommit"
+ "pCustomFields is null\n"
+ "prepareFilters"
+ "registerNotificationPort"
+ "scaler[%d] copyGangedFrame request %d (%d - %d) \n"
+ "site.BlockDescriptorSet"
+ "site.MSR23BackwardsCompatibleFilter"
+ "tryExecuteGangedFrameDescriptor_gated"
- " Client closed with requests not notified! (%u / %u)!"
- " Scaler[%d] invalidateFrameState\n"
- "\"[%s] \" \"Can not find frame descriptor for frame %d!\\n\" @%s:%d"
- "1110000012000000200000002111120011211200"
- "1111111122"
- "1211111212221212122211122111222021111111111110002000000020000000212221111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112"
- "121111222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222212212212212211222222222222222222222222222222212222222222222222222222222221222222222211222222222222222222222222222222222221212121212121212111121111111221112111212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222122121121211212112121121211212112121121211000020000000211111111000000020000000"
- "12112212122121221212212122121221212212122121221212212122120000002000000020000000120000002000000021111200"
- "122222112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221121"
- "1222222222212111111112111111111111111111122122112211112112222222221111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222200000002000000022000000"
- "12222222222221122222222"
- "122222222222211222222221211112112"
- "122222222222211222222221211112112222222222"
- "122222222222211222222221222"
- "Failed to allocate descriptor!\n"
- "Failed to allocate frame descriptor!\n"
- "Failed to clone descriptor set\n"
- "Neighbor Channel Buffer Size req %p (%#zx, %#zx)\n"
- "Request: %p, Neighbor Channel (Col=%#llx, Row=%#llx)\n"
- "Scaler[%d]:activateAndExecuteTransform_gatedContext frame %d\n"
- "Updating write_ptr to dashboard via 64bit writes: %#x\n"
- "[Unimplemented] Multiple Requests Need Reset (SD needs_reset) [use msr_panic_mask=0 to turn off]"
- "a deprecated SPI function was given"
- "allocateDescriptor"
- "allocateDescriptorSet"
- "copyGangedFrame"
- "deAllocateFrameByRequest %d, active window %d / %d\n"
- "dequeueFrame %d, active window %d / %d\n"
- "dequeueRequestForCompletion_gatedContext: %p\n"
- "reInitializeRequest_gatedContext frame %d\n"
- "scaler[%d] copyGangedFrame req %d (%d - %d) \n"
- "site.Descriptor"
- "storeWritePointer"

```

>  `com.apple.driver.AppleMobileDispH17P-DCP`

```diff

-399.26.0.0.0
+399.26.2.0.0
   __TEXT.__cstring: 0x5f51
   __TEXT.__const: 0x1a60
-  __TEXT_EXEC.__text: 0x225e0
+  __TEXT_EXEC.__text: 0x225f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2c0
   __DATA.__common: 0xf0

   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x4058
+  __DATA_CONST.__const: 0x4070
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0xf0
-  Functions: 1131
+  Functions: 1134
   Symbols:   0
   CStrings:  553
 

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.100.76.0.1
-  __TEXT.__cstring: 0xaf83
-  __TEXT.__const: 0x1520
+938.100.82.0.0
+  __TEXT.__cstring: 0xb0d5
+  __TEXT.__const: 0x1530
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x265a8
+  __TEXT_EXEC.__text: 0x26a14
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x402
   __DATA.__common: 0xb0

   __DATA_CONST.__kalloc_type: 0xfc0
   __DATA_CONST.__kalloc_var: 0x1360
   __DATA_CONST.__assert: 0xf0
-  Functions: 838
+  Functions: 842
   Symbols:   0
-  CStrings:  1097
+  CStrings:  1105
 
CStrings:
+ "%s: no registered daemon port\n"
+ "21:01:20"
+ "AMFI: research variant relaxes lock-state for trust caches: %u\n"
+ "Disallowing: found launch warnings for %s\n"
+ "Error communicating with amfid while checking launch warnings for %s\n"
+ "Feb 25 2025"
+ "Launch warning found for proc (fatal): %s"
+ "LaunchConstraints.cpp"
+ "checkForLaunchWarningsInDaemon"
+ "srd_allow_trust_caches_when_locked"
- "01:58:05"
- "Feb 16 2025"

```

>  `com.apple.driver.AppleOLYHAL`

```diff

-450.17.0.0.0
+450.19.0.0.0
   __TEXT.__const: 0x798
-  __TEXT.__cstring: 0x45ad
-  __TEXT_EXEC.__text: 0x1d0e0
+  __TEXT.__cstring: 0x45d1
+  __TEXT_EXEC.__text: 0x1d180
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x13b8
+  __DATA_CONST.__const: 0x13d8
   __DATA_CONST.__kalloc_type: 0x600
-  Functions: 553
+  Functions: 554
   Symbols:   0
-  CStrings:  494
+  CStrings:  495
 
CStrings:
+ "updateDextSpawnCount_block_invoke_2"

```

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-754.100.51.0.0
+754.100.53.0.0
   __TEXT.__const: 0x308
   __TEXT.__cstring: 0x99ea
   __TEXT.__os_log: 0x45d6
-  __TEXT_EXEC.__text: 0x3ccec
+  __TEXT_EXEC.__text: 0x3ccf0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

```

>  `com.apple.driver.AppleSARService`

```diff

-1245.0.0.0.0
-  __TEXT.__os_log: 0xcabd
+1248.0.0.0.0
+  __TEXT.__os_log: 0xcd53
   __TEXT.__const: 0x750
-  __TEXT.__cstring: 0xaac1
-  __TEXT_EXEC.__text: 0x5cd1c
+  __TEXT.__cstring: 0xabc3
+  __TEXT_EXEC.__text: 0x5dd10
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
-  __DATA.__common: 0x5f0
+  __DATA.__common: 0x600
   __DATA.__bss: 0x1458
   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0xa0

   __DATA_CONST.__const: 0x4f90
   __DATA_CONST.__kalloc_type: 0x3040
   __DATA_CONST.__kalloc_var: 0x140
-  Functions: 563
+  Functions: 564
   Symbols:   0
-  CStrings:  1417
+  CStrings:  1424
 
CStrings:
+ "%s::%s:%d: E85 Mitigation Request to Baseband: Sequence Number: %d, Mitigation Request: 0x%x, Override Flag: %s\n"
+ "%s::%s:%d: E85 Mitigation Response: Sequence Number: %d, Mitigation Response: 0x%x (%s)\n"
+ "billboard-addr-tx-accessory"
+ "int"
+ "irq-tx-offset-accessory"

```

>  `com.apple.driver.AppleSEPCredentialManager`

```diff

-758.100.56.0.0
-  __TEXT.__cstring: 0x10a37
+758.100.60.0.0
+  __TEXT.__cstring: 0x10a64
   __TEXT.__const: 0x390
-  __TEXT_EXEC.__text: 0x4a1fc
+  __TEXT_EXEC.__text: 0x4a2e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2d01
   __DATA.__common: 0x1d8

   __DATA_CONST.__kalloc_var: 0x1400
   Functions: 925
   Symbols:   0
-  CStrings:  1840
+  CStrings:  1843
 
CStrings:
+ "%s: %s: [TRM ENABLED=%s] (mask=%x, DISABLED BY: Def=%s%s Arg=%s%s HW=%s%s DT=%s%s Env=%s%s Ext=%s%s Dev=%s%s SEP=%s%s SR=%s%s | MC=%s%s DW=%s%s CB=%s%s GS=%s%s CP=%s%s BS=%s%s MB=%s%s SC=%s%s AS=%s%s IB=%s%s DM=%s%s).\n"
+ "/options"
+ "12111111222222222222222222222222122323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232311111112111111111122122222222222222221222222222222222222222222222222222222222222"
+ "hidrm_default"
+ "stress-rack"
- "%s: %s: [TRM ENABLED=%s] (mask=%x, DISABLED BY: Def=%s%s Arg=%s%s HW=%s%s DT=%s%s Env=%s%s Ext=%s%s Dev=%s%s SEP=%s%s | MC=%s%s DW=%s%s CB=%s%s GS=%s%s CP=%s%s BS=%s%s MB=%s%s SC=%s%s AS=%s%s IB=%s%s DM=%s%s).\n"
- "121111112222222222222222222222122323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232311111112111111111122122222222222222221222222222222222222222222222222222222222222"

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.100.146.0.0
-  __TEXT.__cstring: 0x3acd
+1827.100.152.502.1
+  __TEXT.__cstring: 0x3ad3
   __TEXT.__const: 0x874
-  __TEXT_EXEC.__text: 0x3bbd0
+  __TEXT_EXEC.__text: 0x3bcc0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3a4
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x3a88
   __DATA_CONST.__kalloc_type: 0xd80
   __DATA_CONST.__kalloc_var: 0xa0
-  Functions: 950
+  Functions: 951
   Symbols:   0
   CStrings:  344
 
CStrings:
+ "1827.100.152.502.1"
+ "21:19:25"
+ "Feb 25 2025"
- "04:57:25"
- "1827.100.146"
- "Feb 16 2025"

```

>  `com.apple.driver.AppleSmartBatteryManagerEmbedded`

```diff

-1754.100.31.502.1
-  __TEXT.__cstring: 0x4aea
-  __TEXT.__const: 0x1670
+1754.100.37.502.1
+  __TEXT.__cstring: 0x4b1e
+  __TEXT.__const: 0x1680
   __TEXT.__os_log: 0x2763
-  __TEXT_EXEC.__text: 0x2456c
+  __TEXT_EXEC.__text: 0x245d8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x208
   __DATA.__common: 0x150
-  __DATA.__bss: 0x3230
+  __DATA.__bss: 0x3258
   __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__mod_init_func: 0x40

   __DATA_CONST.__kalloc_type: 0x340
   Functions: 373
   Symbols:   0
-  CStrings:  956
+  CStrings:  958
 
CStrings:
+ "ChargerResetCounter"
+ "PortControllerHvEnRecoveryCount"

```

>  `com.apple.driver.AppleT8103TypeCPhy`

```diff

-244.100.6.0.0
+244.100.7.0.0
   __TEXT.__const: 0x1a0
   __TEXT.__cstring: 0xa571
-  __TEXT.__os_log: 0xe5a8
-  __TEXT_EXEC.__text: 0x4a914
+  __TEXT.__os_log: 0xe5f4
+  __TEXT_EXEC.__text: 0x4aab0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

```

>  `com.apple.driver.AppleT8130TypeCPhy`

```diff

-244.100.6.0.0
+244.100.7.0.0
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x838e
-  __TEXT.__os_log: 0xe23d
-  __TEXT_EXEC.__text: 0x4c1bc
+  __TEXT.__os_log: 0xe289
+  __TEXT_EXEC.__text: 0x4c358
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2c8
   __DATA.__common: 0x58

```

>  `com.apple.driver.AppleT8140CLPC`

```diff

-1175.100.99.0.0
-  __TEXT.__cstring: 0x2be5
+1175.100.102.0.0
+  __TEXT.__cstring: 0x2be6
   __TEXT.__const: 0xb7c
   __TEXT_EXEC.__text: 0x51000
   __TEXT_EXEC.__auth_stubs: 0x0
CStrings:
+ "2025-02-25T21:07:49-08:00"
+ "AppleCLPC-1175.100.102"
- "2025-02-16T04:26:21-08:00"
- "AppleCLPC-1175.100.99"

```

>  `com.apple.driver.AppleT8140MCC`

```diff

-43.100.12.0.0
+43.100.13.0.0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x500f
+  __TEXT.__cstring: 0x5024
   __TEXT.__os_log: 0x2118
-  __TEXT_EXEC.__text: 0x150ac
+  __TEXT_EXEC.__text: 0x150d4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7eb0
   __DATA.__common: 0x1c8

   __DATA_CONST.__kalloc_var: 0x50
   Functions: 507
   Symbols:   0
-  CStrings:  832
+  CStrings:  833
 
CStrings:
+ "flush-cache-on-panic"

```

>  `com.apple.driver.AppleTypeCPhy`

```diff

-244.100.6.0.0
+244.100.7.0.0
   __TEXT.__cstring: 0x1712
   __TEXT.__const: 0x24
   __TEXT.__os_log: 0x120c
-  __TEXT_EXEC.__text: 0x1314c
+  __TEXT_EXEC.__text: 0x13150
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

```

>  `com.apple.driver.AppleTypeCPhyAUSBC`

```diff

-244.100.6.0.0
+244.100.7.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x8a6
-  __TEXT.__os_log: 0xc0f
-  __TEXT_EXEC.__text: 0x53ec
+  __TEXT.__os_log: 0xc5b
+  __TEXT_EXEC.__text: 0x5588
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

```

>  `com.apple.driver.AppleUSBXDCIARM`

```diff

-818.100.5.0.0
+818.100.6.0.0
   __TEXT.__const: 0x38
   __TEXT.__cstring: 0x33f9
   __TEXT.__os_log: 0x53a1
-  __TEXT_EXEC.__text: 0x30b60
+  __TEXT_EXEC.__text: 0x30b64
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1c8

```

>  `com.apple.driver.FairPlayIOKit`

```diff

 72.13.0.0.0
   __TEXT.__cstring: 0x1cc7
   __TEXT.__const: 0x49860
-  __TEXT_EXEC.__text: 0x1cd214
+  __TEXT_EXEC.__text: 0x1cccc4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13a8
   __DATA.__common: 0x5fe1

```

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 440.4.0.0.0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2c32
+  __TEXT.__cstring: 0x2c29
   __TEXT.__os_log: 0x16f1
   __TEXT_EXEC.__text: 0xafb0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__kalloc_type: 0xc0
   Functions: 258
   Symbols:   0
-  CStrings:  233
+  CStrings:  232
 
CStrings:
+ "21:16:59"
+ "Feb 25 2025"
- "04:51:02"
- "04:51:03"
- "Feb 16 2025"

```

>  `com.apple.driver.usb.AppleSynopsysUSB40XHCI`

```diff

-651.100.3.0.0
+651.100.4.0.0
   __TEXT.__cstring: 0x31c6
   __TEXT.__os_log: 0x9fbf
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x5d8dc
+  __TEXT_EXEC.__text: 0x5db6c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x218

   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x5980
+  __DATA_CONST.__const: 0x59a8
   __DATA_CONST.__kalloc_type: 0x340
-  Functions: 436
+  Functions: 440
   Symbols:   0
   CStrings:  290
 

```

>  `com.apple.driver.usb.AppleSynopsysUSBXHCI`

```diff

-651.100.3.0.0
-  __TEXT.__cstring: 0x40f5
+651.100.4.0.0
+  __TEXT.__cstring: 0x4126
   __TEXT.__os_log: 0x4cda
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x37b70
+  __TEXT_EXEC.__text: 0x384ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x290
+  __DATA.__common: 0x2b8
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__mod_init_func: 0x80
-  __DATA_CONST.__mod_term_func: 0x80
-  __DATA_CONST.__const: 0x7808
-  __DATA_CONST.__kalloc_type: 0x480
-  Functions: 536
+  __DATA_CONST.__mod_init_func: 0x88
+  __DATA_CONST.__mod_term_func: 0x88
+  __DATA_CONST.__const: 0x80b8
+  __DATA_CONST.__kalloc_type: 0x4c0
+  Functions: 563
   Symbols:   0
-  CStrings:  376
+  CStrings:  378
 
CStrings:
+ "AppleUSB20XHCIARMPort"
+ "site.AppleUSB20XHCIARMPort"

```

>  `com.apple.filesystems.apfs`

```diff

-2332.100.53.0.6
+2332.100.75.502.1
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x49bfa
-  __TEXT_EXEC.__text: 0x14052c
+  __TEXT.__cstring: 0x49c78
+  __TEXT_EXEC.__text: 0x13ffe0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6a0
   __DATA.__bss: 0xca8

   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x66b0
-  __DATA_CONST.__kalloc_type: 0x4d80
-  __DATA_CONST.__kalloc_var: 0x2a80
+  __DATA_CONST.__kalloc_type: 0x4e00
+  __DATA_CONST.__kalloc_var: 0x2b20
   __DATA_CONST.__assert: 0x14
-  Functions: 2269
+  Functions: 2268
   Symbols:   0
-  CStrings:  6410
+  CStrings:  6414
 
CStrings:
+ "%s:%d: %s Failed to allocate speculative download hash entry\n"
+ "%s:%d: Failed to allocate speculative telemetry hash table\n"
+ "15:08:39"
+ "2025/02/28"
+ "22222222211"
+ "2332.100.75.502.1"
+ "Feb 28 2025"
+ "apfs-2332.100.75.502.1"
+ "site.spec_telem_hash_entry_t"
+ "site.spec_telem_hash_t"
+ "spec_telem_info_hash_entry_create"
+ "spec_telemetry_hash_init"
- "%s:%d: %s dirent hash chain iteration, dir_id %llu, hash 0x%x, count %d\n"
- "01:43:54"
- "01:43:55"
- "2025/02/16"
- "2332.100.53.0.6"
- "Feb 16 2025"
- "apfs-2332.100.53.0.6"
- "iterate_dirents_case_or_norm_insensitive"

```

>  `com.apple.iokit.IOBiometricFamily`

```diff

-511.100.13.0.0
+511.100.15.0.0
   __TEXT.__os_log: 0x1301
-  __TEXT.__cstring: 0x1a9b
+  __TEXT.__cstring: 0x1abd
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x10d20
+  __TEXT_EXEC.__text: 0x10d90
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x3c0

   __DATA_CONST.__kalloc_var: 0xa0
   Functions: 509
   Symbols:   0
-  CStrings:  310
+  CStrings:  311
 
CStrings:
+ "inMap->getLength() <= 4294967295U"

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-775.100.12.0.0
+775.100.14.0.0
   __TEXT.__const: 0x708
   __TEXT.__cstring: 0xf8eb
-  __TEXT_EXEC.__text: 0x600a0
+  __TEXT_EXEC.__text: 0x600cc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x4e4
+  __DATA.__data: 0x544
   __DATA.__common: 0x528
   __DATA.__bss: 0x10
   __DATA_CONST.__auth_got: 0x688

   __DATA_CONST.__const: 0xcc98
   __DATA_CONST.__kalloc_type: 0x7c0
   __DATA_CONST.__kalloc_var: 0x550
-  Functions: 3169
+  Functions: 3170
   Symbols:   0
   CStrings:  1710
 

```

>  `com.apple.kec.corecrypto`

```diff

-1736.100.89.0.0
+1736.100.92.0.0
   __TEXT.__cstring: 0x4866
   __TEXT.__const: 0x144e0
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x580d8
+  __TEXT_EXEC.__text: 0x58118
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2df0
   __DATA.__bss: 0x2980

```

>  `com.apple.kernel`

```diff

-11417.100.533.502.4
-  __TEXT.__const: 0x34900
+11417.100.564.502.1
+  __TEXT.__const: 0x34910
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x76588
-  __TEXT.__os_log: 0x2a8bf
+  __TEXT.__cstring: 0x765fa
+  __TEXT.__os_log: 0x2a5fa
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xab8d8
+  __DATA_CONST.__const: 0xabc08
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__kalloc_type: 0x13980
   __DATA_CONST.__kalloc_var: 0x7ee0

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xcc8
-  __TEXT_EXEC.__text: 0x819b8c
+  __TEXT_EXEC.__text: 0x8180cc
   __TEXT_BOOT_EXEC.__bootcode: 0x514c
   __KLD.__text: 0x1638
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x2ae8
+  __KLDDATA.__const: 0x2b10
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x18501
+  __DATA.__data: 0x185c1
   __DATA.__lock_grp: 0x5a10
   __DATA.__percpu: 0x6e78
-  __DATA.__common: 0x58850
+  __DATA.__common: 0x5bd10
   __DATA.__bss: 0x96008
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x11088
+  __BOOTDATA.__init_entry_set: 0x11178
   __BOOTDATA.__init: 0x5b180
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4662c
-  Functions: 20145
+  Functions: 20142
   Symbols:   0
-  CStrings:  17877
+  CStrings:  17873
 
CStrings:
+ "%s detached"
+ "%s detaching"
+ "%s:%d in6_pcblookup_hash_try no pcb %s\n"
+ "%s:%d in_pcblookup_hash_try no pcb %s\n"
+ "11122221222222222222222112"
+ "1122112121222222222"
+ "12111111211111122222212212212222122222212211222211222221111222221222221111211111112"
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQiBBB^Q^Q^Q^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}^v^vIQ}8"
+ "Developer L4S mode (0: system, 1: force enable L4S, 2: force disable L4S"
+ "Failed to reserve %s region in user map %p %d"
+ "Route logging verbosity level"
+ "System L4S mode (0: disable, 1: enable L4S"
+ "cluster_direct_write_wired"
+ "com.apple.private.networking.elevated-logging"
+ "l4s_developer"
+ "memorystatus: _memstat_reaper_end_sweep: reaper sweep ended, %d processes killed, %lluMB freed, %llums elapsed, %lluus/process\n"
+ "memorystatus: not tracking idle exit kill for priority %d\n"
+ "memorystatus: not tracking kill with invalid priority %d / cause %d\n"
+ "memorystatus: overflowed kill count for priority %d + cause %d\n"
+ "pages_grabbed_iopl"
+ "pages_grabbed_kern"
+ "pages_grabbed_upl"
+ "reaper_enabled"
+ "reaper_max_priority"
+ "reaper_min_age_secs"
+ "reaper_reap_relaunch_mask"
+ "reaper_rescan_secs"
+ "reaper_stats_sweep_count"
+ "reaper_stats_total_freed_mb"
+ "reaper_stats_total_kills"
+ "v24@?0Q8r^{stackshottypes_textlayout_s=Q{stackshottypes_textsegment_v_s=C(?={?=^{stackshottypes_textsegment_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}{u32__opt_s=BI}}16"
- "%s:  broadcast: %02x:%02x:%02x:%02x:%02x:%02x"
- "%s: %s %sfrom %s m 0x%llx data 0x%llx"
- "%s: %s bridge_host_filter failed"
- "%s: %s m 0x%llx"
- "%s: %s mcast for us"
- "%s: %s.%dbrhf_dhcp_bad_chaddr"
- "%s: %s.%dbrhf_dhcp_bad_ciaddr"
- "%s: %s.%dbrhf_dhcp_bad_hlen"
- "%s: %s.%dbrhf_dhcp_bad_htype"
- "%s: %s.%dbrhf_dhcp_bad_op"
- "%s: %s.%dbrhf_dhcp_too_small"
- "%s: %s.%dbrhf_ip_bad_srcaddr"
- "%s: %s.%dbrhf_ip_too_small"
- "%s: large non IPv4/IPv6 packet"
- "%s:%d in6_pcblookup_hash no pcb %s\n"
- "%s:%d in_pcblookup_hash no pcb %s\n"
- "111222212222222222222112"
- "112211212122222222"
- "1211111121111112222212212212222122222212211222211222221111222221222221111211111112"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQiBBB^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}^v^vIQ}8"
- "Failed to copy instruction from PA %p inside wired page @%s:%d"
- "Failed to find mapping for VA %p inside wired page @%s:%d"
- "Failed to reserve %s region in user map %p %d @%s:%d"
- "L4S mode (0: disable, 1: enable L4S"
- "bcast_mcast "
- "bridge_dhcp_filter"
- "bridge_forward"
- "bridge_host_filter"
- "bridge_ifp->if_bridge == NULL"
- "bridge_input"
- "bridge_interface_input"
- "hv_vcpu.c"
- "memorystatus: _memstat_reaper_end_sweep: reaper sweep ended, %d processes killed, %lluMB freed\n"
- "src_if == m->m_pkthdr.rcvif"
- "v24@?0Q8r^{stackshottypes_textlayout_s=Q{stackshottypes_textsegment_v_s=C(?={?=^{stackshottypes_textsegment_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}16"

```

>  `com.apple.security.AppleImage4`

```diff

-320.100.21.0.0
+320.100.22.0.0
   __TEXT.__const: 0x7a2f
-  __TEXT.__cstring: 0x5e8e
-  __TEXT_EXEC.__text: 0x22954
+  __TEXT.__cstring: 0x5eb8
+  __TEXT_EXEC.__text: 0x22980
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6f8
   __DATA.__bss: 0x236

   __DATA_CONST.__image4_exp: 0x10
   Functions: 1094
   Symbols:   0
-  CStrings:  814
+  CStrings:  815
 
CStrings:
+ "%s: chip has no associated dfu policy: %d"
+ "320.100.22"
+ "@(#)VERSION:Darwin Image4 Extension Version 7.0.0: Tue Feb 25 21:00:45 PST 2025; root:AppleImage4-320.100.22~626/AppleImage4/RELEASE_ARM64E"
+ "Darwin Image4 Extension Version 7.0.0: Tue Feb 25 21:00:45 PST 2025; root:AppleImage4-320.100.22~626/AppleImage4/RELEASE_ARM64E"
- "320.100.21"
- "@(#)VERSION:Darwin Image4 Extension Version 7.0.0: Sun Feb 16 01:57:49 PST 2025; root:AppleImage4-320.100.21~1152/AppleImage4/RELEASE_ARM64E"
- "Darwin Image4 Extension Version 7.0.0: Sun Feb 16 01:57:49 PST 2025; root:AppleImage4-320.100.21~1152/AppleImage4/RELEASE_ARM64E"

```

>  `com.apple.security.sandbox`

```diff

-2401.100.179.0.0
+2401.100.194.0.0
   __TEXT.__os_log: 0x2092
-  __TEXT.__const: 0x1b27e1
-  __TEXT.__cstring: 0x717b
-  __TEXT_EXEC.__text: 0x313a8
+  __TEXT.__const: 0x1b2e71
+  __TEXT.__cstring: 0x719d
+  __TEXT_EXEC.__text: 0x31588
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x15420
+  __DATA.__bss: 0x15430
   __DATA_CONST.__auth_got: 0x840
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x35d0
+  __DATA_CONST.__const: 0x35e0
   __DATA_CONST.__kalloc_type: 0xb40
   __DATA_CONST.__kalloc_var: 0x4b0
-  Functions: 639
+  Functions: 638
   Symbols:   0
-  CStrings:  1319
+  CStrings:  1321
 
CStrings:
+ "<redacted>"
+ "thread_raise_exception"

```

</details>

## MachO

### 🆕 NEW (13)

- `/Applications/AuthenticationServicesUI.app/PlugIns/AccountAuthenticationModificationExtensionHelper.appex/AccountAuthenticationModificationExtensionHelper`
- `/Applications/OTEAutomationTest.app/Frameworks/OTEAutomation.framework/OTEAutomation`
- `/Applications/OTEAutomationTest.app/OTEAutomationTest`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0004.bundle/MobileDevices-0004`
- `/System/Library/ExtensionKit/Extensions/ASRFullPayloadCorrection.appex/ASRFullPayloadCorrection`
- `/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/ODDIPoirotMetricsExtension`
- `/System/Library/ExtensionKit/Extensions/TetsuoDiagnosticExtension.appex/TetsuoDiagnosticExtension`
- `/System/Library/PreferenceBundles/TetsuoNotifications.bundle/TetsuoNotifications`
- `/System/Library/PreferenceBundles/VisionCompanionSettings.bundle/VisionCompanionSettings`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/TUDiagnosticExtension.appex/TUDiagnosticExtension`
- `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`
- `/usr/libexec/visioncompaniond`
- `/usr/sbin/skywalkctl`

### ❌ Removed (4)

- `/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService`
- `/System/Library/PrivateFrameworks/BacklightServices.framework/PlugIns/BacklightDiagnostics.appex/BacklightDiagnostics`
- `/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool`
- `/usr/libexec/fmfd`

### ⬆️ Updated (1027)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AdaptiveMusicApp.app/AdaptiveMusicApp](MACHOS/AdaptiveMusicApp.md)
- [/Applications/AdaptiveMusicApp.app/PlugIns/AdaptiveMusicControl.appex/AdaptiveMusicControl](MACHOS/AdaptiveMusicControl.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AirPlayReceiver.app/AirPlayReceiver](MACHOS/AirPlayReceiver.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService](MACHOS/AppleIDSetupUIService.md)
- [/Applications/AskToMessagesHost.app/AskToMessagesHost](MACHOS/AskToMessagesHost.md)
- [/Applications/AskToMessagesHost.app/Extensions/AskToExtension.appex/AskToExtension](MACHOS/AskToExtension.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI](MACHOS/AuthenticationServicesUI.md)
- [/Applications/Batteries.app/PlugIns/BatteriesWidgetIntentsExtension.appex/BatteriesWidgetIntentsExtension](MACHOS/BatteriesWidgetIntentsExtension.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CameraOverlayAngel.app/CameraOverlayAngel](MACHOS/CameraOverlayAngel.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/CarPlayWallpaper.app/CarPlayWallpaper](MACHOS/CarPlayWallpaper.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/CheckerBoardRemoteSetup.app/CheckerBoardRemoteSetup](MACHOS/CheckerBoardRemoteSetup.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/ClarityPhotos.app/ClarityPhotos](MACHOS/ClarityPhotos.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/DKPairingUIService.app/DKPairingUIService](MACHOS/DKPairingUIService.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6000.appex/Diagnostic-6000](MACHOS/Diagnostic-6000.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6006.appex/Diagnostic-6006](MACHOS/Diagnostic-6006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6007.appex/Diagnostic-6007](MACHOS/Diagnostic-6007.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6008.appex/Diagnostic-6008](MACHOS/Diagnostic-6008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8209.appex/Diagnostic-8209](MACHOS/Diagnostic-8209.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389](MACHOS/Diagnostic-8389.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008](MACHOS/Diagnostic-9008.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport](MACHOS/SystemReport.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/EyeReliefUI.app/EyeReliefUI](MACHOS/EyeReliefUI.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FamilyControlsAuthenticationUI.app/FamilyControlsAuthenticationUI](MACHOS/FamilyControlsAuthenticationUI.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FeedbackRemoteView.app/FeedbackRemoteView](MACHOS/FeedbackRemoteView.md)
- [/Applications/FinanceStub.app/FinanceStub](MACHOS/FinanceStub.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FinanceUIService.app/PlugIns/BankConnectRefreshReminderNotificationExtension.appex/BankConnectRefreshReminderNotificationExtension](MACHOS/BankConnectRefreshReminderNotificationExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GAXApp.app/PlugIns/GAXAppWidgetExtension.appex/GAXAppWidgetExtension](MACHOS/GAXAppWidgetExtension.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/GuestUserHandoverSetup.app/GuestUserHandoverSetup](MACHOS/GuestUserHandoverSetup.md)
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
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MomentsUIService.app/Frameworks/MomentsUIServiceCore.framework/MomentsUIServiceCore](MACHOS/MomentsUIServiceCore.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MomentsUIService.app/PlugIns/MomentsDiagnosticsExtensionFeedbackAssistant.appex/MomentsDiagnosticsExtensionFeedbackAssistant](MACHOS/MomentsDiagnosticsExtensionFeedbackAssistant.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/MusicRecognition.app/PlugIns/MusicRecognitionControls.appex/MusicRecognitionControls](MACHOS/MusicRecognitionControls.md)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService.md)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension](MACHOS/PeerPaymentMessagesExtension.md)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService.md)
- [/Applications/PeopleMessageService.app/PeopleMessageService](MACHOS/PeopleMessageService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/PosterBoard.app/XPCServices/PosterPlatformSupportBundleService.xpc/PosterPlatformSupportBundleService](MACHOS/PosterPlatformSupportBundleService.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/Print Center.app/Print Center](MACHOS/Print_Center.md)
- [/Applications/ProductKitViewer.app/ProductKitViewer](MACHOS/ProductKitViewer.md)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/ScreenContinuityShell.app/ScreenContinuityShell](MACHOS/ScreenContinuityShell.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityMarkup.appex/ContinuityMarkup](MACHOS/ContinuityMarkup.md)
- [/Applications/Sidecar.app/PlugIns/ContinuitySketch.appex/ContinuitySketch](MACHOS/ContinuitySketch.md)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar.md)
- [/Applications/Siri.app/PlugIns/TypeToSiriWidgetExtension.appex/TypeToSiriWidgetExtension](MACHOS/TypeToSiriWidgetExtension.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService](MACHOS/SoftwareUpdateUIService.md)
- [/Applications/StickerPickerService.app/StickerPickerService](MACHOS/StickerPickerService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StoreKitUIService.app/StoreKitUIService](MACHOS/StoreKitUIService.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVRemoteUIService.app/TVRemoteUIService](MACHOS/TVRemoteUIService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/Vehicle.app/Vehicle](MACHOS/Vehicle.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Applications/iCloud.app/iCloud](MACHOS/iCloud.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/usr/lib/system/libdispatch_debug.dylib](MACHOS/libdispatch_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libdispatch_profile.dylib](MACHOS/libdispatch_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib](MACHOS/libsystem_c_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/ExclaveKit/usr/lib/dyld](MACHOS/dyld.md)
- [/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer](MACHOS/ClarityUIServer.md)
- [/System/Library/AccessibilityBundles/ClockAngel.axbundle/ClockAngel](MACHOS/ClockAngel.md)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer.md)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/NTKCustomization.axbundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/AccessibilityBundles/NTKUltraCubeFaceBundleCompanion.axbundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion](MACHOS/NanoTimeKitCompanion.md)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/GameCenterAccountAuthenticationPlugin.bundle/GameCenterAccountAuthenticationPlugin](MACHOS/GameCenterAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner](MACHOS/JournalDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/News.bundle/News](MACHOS/News.md)
- [/System/Library/Accounts/Notification/ASDAccountNotificationPlugin.bundle/ASDAccountNotificationPlugin](MACHOS/ASDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/AccountNotificationPlugin](MACHOS/AccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CloudDocsAccountNotificationPlugin.bundle/CloudDocsAccountNotificationPlugin](MACHOS/CloudDocsAccountNotificationPlugin.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppRemovalServices/com.apple.Translate.appremoval.xpc/com.apple.Translate.appremoval](MACHOS/com.apple.Translate.appremoval.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AppLaunchPlugin.bundle/AppLaunchPlugin](MACHOS/AppLaunchPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ClockFlowPlugin.bundle/ClockFlowPlugin](MACHOS/ClockFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/FindMyFlowPlugin.bundle/FindMyFlowPlugin](MACHOS/FindMyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GenerativeAssistantEnablementFlowPlugin.bundle/GenerativeAssistantEnablementFlowPlugin](MACHOS/GenerativeAssistantEnablementFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/NotificationsFlowDelegatePlugin.bundle/NotificationsFlowDelegatePlugin](MACHOS/NotificationsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SafetySessionFlowPlugin.bundle/SafetySessionFlowPlugin](MACHOS/SafetySessionFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriSuggestionsFlowPlugin.bundle/SiriSuggestionsFlowPlugin](MACHOS/SiriSuggestionsFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TranslationFlowDelegatePlugin.bundle/TranslationFlowDelegatePlugin](MACHOS/TranslationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/VideoFlowDelegatePlugin.bundle/VideoFlowDelegatePlugin](MACHOS/VideoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/Plugins/SiriFindMyBundle.assistantBundle/SiriFindMyBundle](MACHOS/SiriFindMyBundle.md)
- [/System/Library/Assistant/Plugins/SiriPrivateLearningAnalytics.assistantBundle/SiriPrivateLearningAnalytics](MACHOS/SiriPrivateLearningAnalytics.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriReferenceResolutionMetricsPlugin.bundle/SiriReferenceResolutionMetricsPlugin](MACHOS/SiriReferenceResolutionMetricsPlugin.md)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge.md)
- [/System/Library/Assistant/Suggestions/SKEBridge/SiriSuggestionsSKEBridge.bundle/SiriSuggestionsSKEBridge](MACHOS/SiriSuggestionsSKEBridge.md)
- [/System/Library/Assistant/UIPlugins/GeneralKnowledge.siriUIBundle/GeneralKnowledge](MACHOS/GeneralKnowledge.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/UIPlugins/RemindersSiriUIPlugin.siriUIBundle/RemindersSiriUIPlugin](MACHOS/RemindersSiriUIPlugin.md)
- [/System/Library/Audio/MIDI Drivers/AppleIDAMDriver.plugin/AppleIDAMDriver](MACHOS/AppleIDAMDriver.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver](MACHOS/AppleMIDIUSBDriver.md)
- [/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver](MACHOS/YamahaUSBMIDIDriver.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin](MACHOS/BuiltinAudioPlugin.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule](MACHOS/VideoConferenceControlCenterModule.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents](MACHOS/AccessibilityAppIntents.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/ReportSystemMemory](MACHOS/ReportSystemMemory.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/appplaceholdersyncd](MACHOS/appplaceholdersyncd.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/CookieDataMigrator.migrator/CookieDataMigrator](MACHOS/CookieDataMigrator.md)
- [/System/Library/DataClassMigrators/MobileMailMigrator.migrator/MobileMailMigrator](MACHOS/MobileMailMigrator.md)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator.md)
- [/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess](MACHOS/RestorePostProcess.md)
- [/System/Library/DigitalSeparation/SharingSources/DSNotesPlugin.bundle/DSNotesPlugin](MACHOS/DSNotesPlugin.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyItemsDigitalSeparation.bundle/FindMyItemsDigitalSeparation](MACHOS/FindMyItemsDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyPeopleDigitalSeparation.bundle/FindMyPeopleDigitalSeparation](MACHOS/FindMyPeopleDigitalSeparation.md)
- [/System/Library/DistributedEvaluation/Plugins/RemindersDES.desPlugin/RemindersDES](MACHOS/RemindersDES.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AudiovisualThumbnailExtension.appex/AudiovisualThumbnailExtension](MACHOS/AudiovisualThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/AutocompleteAppIntentsExtension.appex/AutocompleteAppIntentsExtension](MACHOS/AutocompleteAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BiomeLibraryEventUploader.appex/BiomeLibraryEventUploader](MACHOS/BiomeLibraryEventUploader.md)
- [/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor](MACHOS/BiomeSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/BitacoraWorker.appex/BitacoraWorker](MACHOS/BitacoraWorker.md)
- [/System/Library/ExtensionKit/Extensions/BluetoothSettingsAppIntentsWidgetExtension.appex/BluetoothSettingsAppIntentsWidgetExtension](MACHOS/BluetoothSettingsAppIntentsWidgetExtension.md)
- [/System/Library/ExtensionKit/Extensions/ContactsSettingsIntentsExtension.appex/ContactsSettingsIntentsExtension](MACHOS/ContactsSettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ControlCenterControlsExtension.appex/ControlCenterControlsExtension](MACHOS/ControlCenterControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DeepThoughtWorker.appex/DeepThoughtWorker](MACHOS/DeepThoughtWorker.md)
- [/System/Library/ExtensionKit/Extensions/DefaultAppsSettingsIntents.appex/DefaultAppsSettingsIntents](MACHOS/DefaultAppsSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/DisplayAndBrightnessSettingsExtension](MACHOS/DisplayAndBrightnessSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DoNotDisturbAppIntents.appex/DoNotDisturbAppIntents](MACHOS/DoNotDisturbAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin](MACHOS/FedStatsMLHostPlugin.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA](MACHOS/FedStatsMLHostPluginClassA.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB](MACHOS/FedStatsMLHostPluginClassB.md)
- [/System/Library/ExtensionKit/Extensions/GMSSELFIngestor.appex/GMSSELFIngestor](MACHOS/GMSSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension](MACHOS/GPUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents](MACHOS/GeneralSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantSettingsExtension.appex/GenerativeAssistantSettingsExtension](MACHOS/GenerativeAssistantSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/HealthStandaloneIntents.appex/HealthStandaloneIntents](MACHOS/HealthStandaloneIntents.md)
- [/System/Library/ExtensionKit/Extensions/HomeAppIntentsExtension.appex/HomeAppIntentsExtension](MACHOS/HomeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/IEMetricsWorker](MACHOS/IEMetricsWorker.md)
- [/System/Library/ExtensionKit/Extensions/IFTelemetrySELFIngestor.appex/IFTelemetrySELFIngestor](MACHOS/IFTelemetrySELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/IFTranscriptSELFIngestor.appex/IFTranscriptSELFIngestor](MACHOS/IFTranscriptSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/ImageThumbnailExtension.appex/ImageThumbnailExtension](MACHOS/ImageThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/InferenceProviderService.appex/InferenceProviderService](MACHOS/InferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/InstalledAppsSettingsAppIntents.appex/InstalledAppsSettingsAppIntents](MACHOS/InstalledAppsSettingsAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/IntelligenceFlowAppIntentsExtension.appex/IntelligenceFlowAppIntentsExtension](MACHOS/IntelligenceFlowAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/IntelligenceIntentsExtension.appex/IntelligenceIntentsExtension](MACHOS/IntelligenceIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/KeyboardSettingsExtension.appex/KeyboardSettingsExtension](MACHOS/KeyboardSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/LLMCacheSELFIngestor.appex/LLMCacheSELFIngestor](MACHOS/LLMCacheSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/LegalAndRegulatoryAppIntents.appex/LegalAndRegulatoryAppIntents](MACHOS/LegalAndRegulatoryAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseASRReplay.appex/LighthouseASRReplay](MACHOS/LighthouseASRReplay.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVExtension.appex/LighthouseAVExtension](MACHOS/LighthouseAVExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseServicesAnalyticsExtension.appex/LighthouseServicesAnalyticsExtension](MACHOS/LighthouseServicesAnalyticsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension](MACHOS/MADViewServiceExtension.md)
- [/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/MKRemoteUI](MACHOS/MKRemoteUI.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MessagesAnalyticsWorker.appex/MessagesAnalyticsWorker](MACHOS/MessagesAnalyticsWorker.md)
- [/System/Library/ExtensionKit/Extensions/ModelMonitoringLighthousePlugin.appex/ModelMonitoringLighthousePlugin](MACHOS/ModelMonitoringLighthousePlugin.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicUIEngagementExtension.appex/MusicUIEngagementExtension](MACHOS/MusicUIEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/NLPLearnerExtension.appex/NLPLearnerExtension](MACHOS/NLPLearnerExtension.md)
- [/System/Library/ExtensionKit/Extensions/ODDIMetricsExtension.appex/ODDIMetricsExtension](MACHOS/ODDIMetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLAppEmbedding.appex/PFLASLAppEmbedding](MACHOS/PFLASLAppEmbedding.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLArcadeRanking.appex/PFLASLArcadeRanking](MACHOS/PFLASLArcadeRanking.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLArcadeRetention.appex/PFLASLArcadeRetention](MACHOS/PFLASLArcadeRetention.md)
- [/System/Library/ExtensionKit/Extensions/PFLASLExperimental.appex/PFLASLExperimental](MACHOS/PFLASLExperimental.md)
- [/System/Library/ExtensionKit/Extensions/PFLCSLAppStore.appex/PFLCSLAppStore](MACHOS/PFLCSLAppStore.md)
- [/System/Library/ExtensionKit/Extensions/PFLCSLAppStore2.appex/PFLCSLAppStore2](MACHOS/PFLCSLAppStore2.md)
- [/System/Library/ExtensionKit/Extensions/PeopleSuggesterLighthouseBackgroundPlugin.appex/PeopleSuggesterLighthouseBackgroundPlugin](MACHOS/PeopleSuggesterLighthouseBackgroundPlugin.md)
- [/System/Library/ExtensionKit/Extensions/PeopleSuggesterMetricsLighthouse.appex/PeopleSuggesterMetricsLighthouse](MACHOS/PeopleSuggesterMetricsLighthouse.md)
- [/System/Library/ExtensionKit/Extensions/PersonalHotspotControlExtension.appex/PersonalHotspotControlExtension](MACHOS/PersonalHotspotControlExtension.md)
- [/System/Library/ExtensionKit/Extensions/PhotosAppIntentsExtension.appex/PhotosAppIntentsExtension](MACHOS/PhotosAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin](MACHOS/PhotosPFLPlugin.md)
- [/System/Library/ExtensionKit/Extensions/PhotosSearchClientLighthouse.appex/PhotosSearchClientLighthouse](MACHOS/PhotosSearchClientLighthouse.md)
- [/System/Library/ExtensionKit/Extensions/PnROnDeviceWorker.appex/PnROnDeviceWorker](MACHOS/PnROnDeviceWorker.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService](MACHOS/PrivateMLClientInferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/ProactiveShareSheetLighthouseBackgroundPlugin.appex/ProactiveShareSheetLighthouseBackgroundPlugin](MACHOS/ProactiveShareSheetLighthouseBackgroundPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SearchAnalyticsWorker.appex/SearchAnalyticsWorker](MACHOS/SearchAnalyticsWorker.md)
- [/System/Library/ExtensionKit/Extensions/SearchToolDiagnosticExtension.appex/SearchToolDiagnosticExtension](MACHOS/SearchToolDiagnosticExtension.md)
- [/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension](MACHOS/SearchToolExtension.md)
- [/System/Library/ExtensionKit/Extensions/SensitiveContentAnalysisConfigurationExtension.appex/SensitiveContentAnalysisConfigurationExtension](MACHOS/SensitiveContentAnalysisConfigurationExtension.md)
- [/System/Library/ExtensionKit/Extensions/SettingsCellularAppIntentsExtension.appex/SettingsCellularAppIntentsExtension](MACHOS/SettingsCellularAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SiriCoreMetricsWorker.appex/SiriCoreMetricsWorker](MACHOS/SiriCoreMetricsWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin](MACHOS/SiriSuggestionsLightHousePlugin.md)
- [/System/Library/ExtensionKit/Extensions/SiriTurnRestatementExtension.appex/SiriTurnRestatementExtension](MACHOS/SiriTurnRestatementExtension.md)
- [/System/Library/ExtensionKit/Extensions/SiriUserSegmentation.appex/SiriUserSegmentation](MACHOS/SiriUserSegmentation.md)
- [/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsIntents.appex/SoftwareUpdateSettingsIntents](MACHOS/SoftwareUpdateSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/SoundAndHapticsControls.appex/SoundAndHapticsControls](MACHOS/SoundAndHapticsControls.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/TVAppExtension.appex/TVAppExtension](MACHOS/TVAppExtension.md)
- [/System/Library/ExtensionKit/Extensions/TelemetryAggregator.appex/TelemetryAggregator](MACHOS/TelemetryAggregator.md)
- [/System/Library/ExtensionKit/Extensions/ToggleAirplaneModeExtension.appex/ToggleAirplaneModeExtension](MACHOS/ToggleAirplaneModeExtension.md)
- [/System/Library/ExtensionKit/Extensions/ToggleCellularDataModeExtension.appex/ToggleCellularDataModeExtension](MACHOS/ToggleCellularDataModeExtension.md)
- [/System/Library/ExtensionKit/Extensions/TranslateCacheDeleteExtension.appex/TranslateCacheDeleteExtension](MACHOS/TranslateCacheDeleteExtension.md)
- [/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension](MACHOS/TranslationAPISupportExtension.md)
- [/System/Library/ExtensionKit/Extensions/TransparencySettingsIntents.appex/TransparencySettingsIntents](MACHOS/TransparencySettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/Unity2025Poster.appex/Unity2025Poster](MACHOS/Unity2025Poster.md)
- [/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension](MACHOS/WiFiSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/WirelessModemSettingsControlsExtension.appex/WirelessModemSettingsControlsExtension](MACHOS/WirelessModemSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension](MACHOS/ZeoliteExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat](MACHOS/com.apple.fskit.exfat.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker](MACHOS/com.apple.mlhost.CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.QuartzWorker.appex/com.apple.mlhost.QuartzWorker](MACHOS/com.apple.mlhost.QuartzWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Filesystems/apfs.fs/apfs_boot_util](MACHOS/apfs_boot_util.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_iosd](MACHOS/apfs_iosd.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/slurpAPFSMeta](MACHOS/slurpAPFSMeta.md)
- [/System/Library/Filesystems/apfs.fs/sm_stats](MACHOS/sm_stats.md)
- [/System/Library/Filesystems/msdos.fs/fsck_msdos](MACHOS/fsck_msdos.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/XPCServices/BrowserEngineKit.Intermediary.xpc/BrowserEngineKit.Intermediary](MACHOS/BrowserEngineKit.Intermediary.md)
- [/System/Library/Frameworks/CFNetwork.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/ClassKit.framework/progressd](MACHOS/progressd.md)
- [/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService](MACHOS/LimitedLibraryPickerViewService.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService](MACHOS/ContactsButtonXPCService.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin](MACHOS/CoreLocationNumberedMapCalloutPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper](MACHOS/CommCenterRootHelper.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/ctkd](MACHOS/ctkd.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/FinanceKit.framework/financed](MACHOS/financed.md)
- [/System/Library/Frameworks/GSS.framework/Helpers/GSSCred](MACHOS/GSSCred.md)
- [/System/Library/Frameworks/GroupActivities.framework/XPCServices/GroupSessionService.xpc/GroupSessionService](MACHOS/GroupSessionService.md)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.appex/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.md)
- [/System/Library/Frameworks/HealthKit.framework/healthd](MACHOS/healthd.md)
- [/System/Library/Frameworks/IdentityLookup.framework/XPCServices/com.apple.IdentityLookup.MessageFilter.xpc/com.apple.IdentityLookup.MessageFilter](MACHOS/com.apple.IdentityLookup.MessageFilter.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl](MACHOS/MechPearl.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPushButton.bundle/MechPushButton](MACHOS/MechPushButton.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM](MACHOS/ModuleACM.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/ManagedSettings.framework/managedsettingsdiagnoticstool](MACHOS/managedsettingsdiagnoticstool.md)
- [/System/Library/Frameworks/MessageUI.framework/PlugIns/MessageUI.wkbundle/MessageUI](MACHOS/MessageUI.md)
- [/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/get-network-info](MACHOS/get-network-info.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/WeatherKit.framework/XPCServices/com.apple.weatherkit.authservice.xpc/com.apple.weatherkit.authservice](MACHOS/com.apple.weatherkit.authservice.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter](MACHOS/AppleProxServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/HIDRMServiceFilter.plugin/HIDRMServiceFilter](MACHOS/HIDRMServiceFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/HIDRMSessionFilter.plugin/HIDRMSessionFilter](MACHOS/HIDRMSessionFilter.md)
- [/System/Library/Health/DiagnosticExtensionPlugins/HealthAppDiagnosticExtensionPlugin.bundle/HealthAppDiagnosticExtensionPlugin](MACHOS/HealthAppDiagnosticExtensionPlugin.md)
- [/System/Library/LocationBundles/AltimeterHarvest.bundle/AltimeterHarvest](MACHOS/AltimeterHarvest.md)
- [/System/Library/LocationBundles/AppGenius.bundle/AppGenius](MACHOS/AppGenius.md)
- [/System/Library/LocationBundles/CompassCalibration.bundle/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/LocationBundles/IonosphereHarvest.bundle/IonosphereHarvest](MACHOS/IonosphereHarvest.md)
- [/System/Library/LocationBundles/LocationFenceSync.bundle/LocationFenceSync](MACHOS/LocationFenceSync.md)
- [/System/Library/LocationBundles/LocationHarvest.bundle/LocationHarvest](MACHOS/LocationHarvest.md)
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
- [/System/Library/Messages/iMessageApps/AudioMessagesExtension.bundle/AudioMessagesExtension](MACHOS/AudioMessagesExtension.md)
- [/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/FindMyMessagesApp](MACHOS/FindMyMessagesApp.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/SendLaterProvider.bundle/SendLaterProvider](MACHOS/SendLaterProvider.md)
- [/System/Library/NanoPreferenceBundles/Applications/DepthCompanionSettings.bundle/DepthCompanionSettings](MACHOS/DepthCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/MindSettings.bundle/MindSettings](MACHOS/MindSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMenstrualCyclesCompanionSettings.bundle/NanoMenstrualCyclesCompanionSettings](MACHOS/NanoMenstrualCyclesCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/AssistantBridgeSettings.bundle/AssistantBridgeSettings](MACHOS/AssistantBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings](MACHOS/CSLCompanionLiveActivitiesSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CellularBridgeSettings.bundle/CellularBridgeSettings](MACHOS/CellularBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthFeaturesBridgeSetupPlugin.bundle/HealthFeaturesBridgeSetupPlugin](MACHOS/HealthFeaturesBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoSleepBridgeSetup.bundle/NanoSleepBridgeSetup](MACHOS/NanoSleepBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/TextSettingsBridgeSetup.bundle/TextSettingsBridgeSetup](MACHOS/TextSettingsBridgeSetup.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/MindComplicationBundleCompanion.bundle/MindComplicationBundleCompanion](MACHOS/MindComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGladiusFaceBundleCompanion.bundle/NTKGladiusFaceBundleCompanion](MACHOS/NTKGladiusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographModularFaceBundle.bundle/NTKInfographModularFaceBundle](MACHOS/NTKInfographModularFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParameciumFaceBundleCompanion.bundle/NTKParameciumFaceBundleCompanion](MACHOS/NTKParameciumFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/CloudKitSettings.bundle/CloudKitSettings](MACHOS/CloudKitSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/ActionButtonSettings.bundle/ActionButtonSettings](MACHOS/ActionButtonSettings.md)
- [/System/Library/PreferenceBundles/AdAttributionKitDeveloperSettings.bundle/AdAttributionKitDeveloperSettings](MACHOS/AdAttributionKitDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings](MACHOS/AirPlayAndHandoffSettings.md)
- [/System/Library/PreferenceBundles/AmbientSettings.bundle/AmbientSettings](MACHOS/AmbientSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/CallScreeningSettingsBundle.bundle/CallScreeningSettingsBundle](MACHOS/CallScreeningSettingsBundle.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIMusicSettings.bundle/ClarityUIMusicSettings](MACHOS/ClarityUIMusicSettings.md)
- [/System/Library/PreferenceBundles/ClassKitSettings.bundle/ClassKitSettings](MACHOS/ClassKitSettings.md)
- [/System/Library/PreferenceBundles/ControlCenterSettings.bundle/ControlCenterSettings](MACHOS/ControlCenterSettings.md)
- [/System/Library/PreferenceBundles/CoreRoutineSettings.bundle/CoreRoutineSettings](MACHOS/CoreRoutineSettings.md)
- [/System/Library/PreferenceBundles/DeviceManagementClientDeveloperSettings.bundle/DeviceManagementClientDeveloperSettings](MACHOS/DeviceManagementClientDeveloperSettings.md)
- [/System/Library/PreferenceBundles/DigitalSeparationSettings.bundle/DigitalSeparationSettings](MACHOS/DigitalSeparationSettings.md)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings](MACHOS/HearingSettings.md)
- [/System/Library/PreferenceBundles/HomeScreenSettings.bundle/HomeScreenSettings](MACHOS/HomeScreenSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/LegalAndRegulatorySettings.bundle/LegalAndRegulatorySettings](MACHOS/LegalAndRegulatorySettings.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MobileCalSettings.bundle/MobileCalSettings](MACHOS/MobileCalSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MobileSlideShowSettings.bundle/MobileSlideShowSettings](MACHOS/MobileSlideShowSettings.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/MusicSettings.bundle/MusicSettings](MACHOS/MusicSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PassbookSettings.bundle/PassbookSettings](MACHOS/PassbookSettings.md)
- [/System/Library/PreferenceBundles/PasswordsSettings.bundle/PasswordsSettings](MACHOS/PasswordsSettings.md)
- [/System/Library/PreferenceBundles/PaymentContactlessSettingsUIPlugin.bundle/PaymentContactlessSettingsUIPlugin](MACHOS/PaymentContactlessSettingsUIPlugin.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings.md)
- [/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings](MACHOS/SOSSettings.md)
- [/System/Library/PreferenceBundles/SiriMessagesSettings.bundle/SiriMessagesSettings](MACHOS/SiriMessagesSettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings](MACHOS/VoiceControlSettings.md)
- [/System/Library/PreferenceBundles/VoiceMemosSettings.bundle/VoiceMemosSettings](MACHOS/VoiceMemosSettings.md)
- [/System/Library/PreferenceBundles/VolumeLimitSettings.bundle/VolumeLimitSettings](MACHOS/VolumeLimitSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceBundles/iBooksSettings.bundle/iBooksSettings](MACHOS/iBooksSettings.md)
- [/System/Library/PreferencesSyncBundles/CoreLocationSync.bundle/CoreLocationSync](MACHOS/CoreLocationSync.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd](MACHOS/motiontrackingd.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd](MACHOS/activitysharingd.md)
- [/System/Library/PrivateFrameworks/AnnounceSiriExtensions.framework/PlugIns/AnnounceIntentExtension.appex/AnnounceIntentExtension](MACHOS/AnnounceIntentExtension.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/XPCServices/AppPredictionIntentsHelperService.xpc/AppPredictionIntentsHelperService](MACHOS/AppPredictionIntentsHelperService.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/PlugIns/AppStoreOverlaysService.appex/AppStoreOverlaysService](MACHOS/AppStoreOverlaysService.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension](MACHOS/AAUIFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail](MACHOS/ASVAssetThumbnail.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationModeUI.app/AutomationModeUI](MACHOS/AutomationModeUI.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/automationmode-writer](MACHOS/automationmode-writer.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/PlugIns/ClockPosterExtension.appex/ClockPosterExtension](MACHOS/ClockPosterExtension.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider](MACHOS/com.apple.CloudDocs.iCloudDriveFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged](MACHOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent](MACHOS/contactsdonationagent.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent](MACHOS/analyticsagent.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/XPCServices/TilesService.xpc/TilesService](MACHOS/TilesService.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/XPCServices/AccessoryDataFetch.xpc/AccessoryDataFetch](MACHOS/AccessoryDataFetch.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity](MACHOS/com.apple.dt.instruments.dtsecurity.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.B389.appex/com.apple.DiagnosticExtensions.B389](MACHOS/com.apple.DiagnosticExtensions.B389.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/catutil](MACHOS/catutil.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService](MACHOS/FilesystemMetadataSnapshotService.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/PlugIns/DockKitExtension.appex/DockKitExtension](MACHOS/DockKitExtension.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/PlugIns/EmojiPosterExtension.appex/EmojiPosterExtension](MACHOS/EmojiPosterExtension.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/XPCServices/EnergyKitService.xpc/EnergyKitService](MACHOS/EnergyKitService.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored](MACHOS/facetimemessagestored.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd](MACHOS/generativeexperiencesd.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/MapsOfflineService.bundle/MapsOfflineService](MACHOS/MapsOfflineService.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/PlugIns/HealthBalanceDiagnosticExtension.appex/HealthBalanceDiagnosticExtension](MACHOS/HealthBalanceDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/PlugIns/HealthMedicationsNotificationContentExtension.appex/HealthMedicationsNotificationContentExtension](MACHOS/HealthMedicationsNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd](MACHOS/homeenergyd.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/PlugIns/HomeKitEventsDiagnosticExtension.appex/HomeKitEventsDiagnosticExtension](MACHOS/HomeKitEventsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iapd](MACHOS/iapd.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMAutomaticHistoryDeletionAgent.app/IMAutomaticHistoryDeletionAgent](MACHOS/IMAutomaticHistoryDeletionAgent.md)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/Resources/IOSADiagnose](MACHOS/IOSADiagnose.md)
- [/System/Library/PrivateFrameworks/IPConfiguration.framework/XPCServices/IPConfigurationHelper.xpc/IPConfigurationHelper](MACHOS/IPConfigurationHelper.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics](MACHOS/IntelligenceFlowDiagnostics.md)
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
- [/System/Library/PrivateFrameworks/MapsSupport.framework/nanomapscd](MACHOS/nanomapscd.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService](MACHOS/MediaAnalysisBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService](MACHOS/com.apple.photos.VideoConversionService.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd](MACHOS/migrationd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service](MACHOS/Accessory_Updater_Service.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU](MACHOS/UARPUpdaterServiceDFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension](MACHOS/MBPrebuddyFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd](MACHOS/medialibraryd.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/companionfindlocallyd](MACHOS/companionfindlocallyd.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent](MACHOS/NPKCompanionAgent.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd](MACHOS/nanoprefsyncd.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService](MACHOS/NFUIService.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/NewsScoringService.xpc/NewsScoringService](MACHOS/NewsScoringService.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/TodayFeedConfigDecoder.xpc/TodayFeedConfigDecoder](MACHOS/TodayFeedConfigDecoder.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PlugIns/PeopleSuggesterLighthousePlugin.appex/PeopleSuggesterLighthousePlugin](MACHOS/PeopleSuggesterLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PlugIns/PhotosStoryDiagnostics.appex/PhotosStoryDiagnostics](MACHOS/PhotosStoryDiagnostics.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader](MACHOS/PerfPowerServicesSignpostReader.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/PlugIns/ProactiveShareSheetDataHarvestingLighthousePlugin.appex/ProactiveShareSheetDataHarvestingLighthousePlugin](MACHOS/ProactiveShareSheetDataHarvestingLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/XPCServices/PromotedContentJetService.xpc/PromotedContentJetService](MACHOS/PromotedContentJetService.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/prototyped](MACHOS/prototyped.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/PlugIns/RemindersNotificationContentExtension.appex/RemindersNotificationContentExtension](MACHOS/RemindersNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/InteractiveLegacyProfilesSubscriber.xpc/InteractiveLegacyProfilesSubscriber](MACHOS/InteractiveLegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/LegacyProfilesSubscriber.xpc/LegacyProfilesSubscriber](MACHOS/LegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber](MACHOS/ManagedAppsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedSettingsSubscriber.xpc/ManagedSettingsSubscriber](MACHOS/ManagedSettingsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PasscodeSettingsSubscriber.xpc/PasscodeSettingsSubscriber](MACHOS/PasscodeSettingsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SecuritySubscriber.xpc/SecuritySubscriber](MACHOS/SecuritySubscriber.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper](MACHOS/STSXPCHelper.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SensingPredictServices.framework/XPCServices/SensingPredictXPCService.xpc/SensingPredictXPCService](MACHOS/SensingPredictXPCService.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored](MACHOS/fitcored.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcoresessiond](MACHOS/fitcoresessiond.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropNotice.appex/AirDropNotice](MACHOS/AirDropNotice.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/ContinuityRemote.appex/ContinuityRemote](MACHOS/ContinuityRemote.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/XPCServices/SAExtensionOrchestrator.xpc/SAExtensionOrchestrator](MACHOS/SAExtensionOrchestrator.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced](MACHOS/siriinferenced.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/PlugIns/SiriInferredHelpfulnessPlugin.appex/SiriInferredHelpfulnessPlugin](MACHOS/SiriInferredHelpfulnessPlugin.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningPlatformPlugin.appex/SiriUserFeedbackLearningPlatformPlugin](MACHOS/SiriUserFeedbackLearningPlatformPlugin.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/PlugIns/SettingsIntentExtension.appex/SettingsIntentExtension](MACHOS/SettingsIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/PlugIns/MusicAppSelectionPFLPlugin.appex/MusicAppSelectionPFLPlugin](MACHOS/MusicAppSelectionPFLPlugin.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsBookkeepingService.xpc/SiriSuggestionsBookkeepingService](MACHOS/SiriSuggestionsBookkeepingService.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/com.apple.SiriTTSService.TrialProxy](MACHOS/com.apple.SiriTTSService.TrialProxy.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/PlugIns/AlarmIntentsExtension.appex/AlarmIntentsExtension](MACHOS/AlarmIntentsExtension.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/PlugIns/TimerIntentsExtension.appex/TimerIntentsExtension](MACHOS/TimerIntentsExtension.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension](MACHOS/VideoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/PlugIns/SleepNotificationContentExtension.appex/SleepNotificationContentExtension](MACHOS/SleepNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/PlugIns/SmartRepliesMLRuntimePlugin.appex/SmartRepliesMLRuntimePlugin](MACHOS/SmartRepliesMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUSFollowUpExtension.appex/SUSFollowUpExtension](MACHOS/SUSFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/PlugIns/SoundScapesViewServices.appex/SoundScapesViewServices](MACHOS/SoundScapesViewServices.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd](MACHOS/com.apple.SpeechRecognitionCore.brokerd.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/XPCServices/StocksKitService.xpc/StocksKitService](MACHOS/StocksKitService.md)
- [/System/Library/PrivateFrameworks/TailspinSymbolication.framework/XPCServices/TailspinSymbolicationServer.xpc/TailspinSymbolicationServer](MACHOS/TailspinSymbolicationServer.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/XPCServices/TelephonyBlastDoorService.xpc/TelephonyBlastDoorService](MACHOS/TelephonyBlastDoorService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService](MACHOS/UVFSService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd](MACHOS/usernotificationsd.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/PlugIns/TVProductPageExtension.appex/TVProductPageExtension](MACHOS/TVProductPageExtension.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd](MACHOS/siriactionsd.md)
- [/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/XPCServices/WalletBlastDoorService.xpc/WalletBlastDoorService](MACHOS/WalletBlastDoorService.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/PlugIns/CollectionsPoster.appex/CollectionsPoster](MACHOS/CollectionsPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd](MACHOS/watchlistd.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WiFiLogCapture.framework/PlugIns/WiFiLogConfigDiagnosticExtension_iOS.appex/WiFiLogConfigDiagnosticExtension_iOS](MACHOS/WiFiLogConfigDiagnosticExtension_iOS.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService](MACHOS/WiFiCloudAssetsXPCService.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/XPCServices/WorkoutKitXPCService.xpc/WorkoutKitXPCService](MACHOS/WorkoutKitXPCService.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/ContainerMetadataExtractor](MACHOS/ContainerMetadataExtractor.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/PlugIns/iCloudSettingsNotificationContentExtension.appex/iCloudSettingsNotificationContentExtension](MACHOS/iCloudSettingsNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd](MACHOS/icloudsubscriptionoptimizerd.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/PlugIns/LighthousePlugin.appex/LighthousePlugin](MACHOS/LighthousePlugin.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/ScreenReader/BrailleTables/LiblouisBrailleTranslator.brailletable/LiblouisBrailleTranslator](MACHOS/LiblouisBrailleTranslator.md)
- [/System/Library/Settings/DefaultApps/CallFiltering.plugin/CallFiltering](MACHOS/CallFiltering.md)
- [/System/Library/Settings/DefaultApps/DefaultAppsPasswordManagerSettings.plugin/DefaultAppsPasswordManagerSettings](MACHOS/DefaultAppsPasswordManagerSettings.md)
- [/System/Library/Settings/DefaultApps/DefaultContactlessAppSettingsUIPlugin.plugin/DefaultContactlessAppSettingsUIPlugin](MACHOS/DefaultContactlessAppSettingsUIPlugin.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
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
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriTimeSuggestionsPlugin.bundle/SiriTimeSuggestionsPlugin](MACHOS/SiriTimeSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/VideoSuggestionsPlugin.bundle/VideoSuggestionsPlugin](MACHOS/VideoSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/FindMyUIPlugin.bundle/FindMyUIPlugin](MACHOS/FindMyUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/HomeCommunicationUIPlugin.bundle/HomeCommunicationUIPlugin](MACHOS/HomeCommunicationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/PhoneUIPlugin.bundle/PhoneUIPlugin](MACHOS/PhoneUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SearchToolUIPlugin.bundle/SearchToolUIPlugin](MACHOS/SearchToolUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/SiriKitUIPlugin](MACHOS/SiriKitUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriLinkUIPlugin.bundle/SiriLinkUIPlugin](MACHOS/SiriLinkUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSuggestionsUIPlugin.bundle/SiriSuggestionsUIPlugin](MACHOS/SiriSuggestionsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriTranslationUIPlugin.bundle/SiriTranslationUIPlugin](MACHOS/SiriTranslationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriVideoUIPlugin.bundle/SiriVideoUIPlugin](MACHOS/SiriVideoUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/Snippets/UIPlugins/TimerUIPlugin.bundle/TimerUIPlugin](MACHOS/TimerUIPlugin.md)
- [/System/Library/SpringBoardPlugins/PassesLockScreenPlugin.lockbundle/PassesLockScreenPlugin](MACHOS/PassesLockScreenPlugin.md)
- [/System/Library/StreamingExtractorPlugins/STAEAExtractionPlugin.bundle/STAEAExtractionPlugin](MACHOS/STAEAExtractionPlugin.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/Trace/Providers/Logging.bundle/Logging](MACHOS/Logging.md)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ARQLNotifications.bundle/com.apple.ARQLNotifications](MACHOS/com.apple.ARQLNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
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
- [/private/var/staged_system_apps/Books.app/Frameworks/EngagementCollector.framework/EngagementCollector](MACHOS/EngagementCollector.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksEngagementExtension.appex/BooksEngagementExtension](MACHOS/BooksEngagementExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension](MACHOS/BooksProductPageExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Bridge.app/PlugIns/BridgeWidgetExtension.appex/BridgeWidgetExtension](MACHOS/BridgeWidgetExtension.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Contacts.app/Contacts](MACHOS/Contacts.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
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
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification](MACHOS/HomeNotification.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen](MACHOS/HomeWidgetLockScreen.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent](MACHOS/HomeWidgetSingleAccessoryIntent.md)
- [/private/var/staged_system_apps/Image Playground.app/Image Playground](MACHOS/Image_Playground.md)
- [/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension](MACHOS/GenerativePlaygroundMessagesAppExtension.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/Extensions/CalendarIntentsExtension.appex/CalendarIntentsExtension](MACHOS/CalendarIntentsExtension.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension](MACHOS/CalendarWidgetExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.EditorExtension.appex/com.apple.mobilenotes.EditorExtension](MACHOS/com.apple.mobilenotes.EditorExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSMS.app/Extensions/MessagesActionExtension.appex/MessagesActionExtension](MACHOS/MessagesActionExtension.md)
- [/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension](MACHOS/MessagesPluginNotificationExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/MobileTimer](MACHOS/MobileTimer.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Extensions/MusicFocusFilters.appex/MusicFocusFilters](MACHOS/MusicFocusFilters.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker](MACHOS/MediaPicker.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsEngagementExtension.appex/NewsEngagementExtension](MACHOS/NewsEngagementExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookTransactionNotificationContentExtension.appex/PassbookTransactionNotificationContentExtension](MACHOS/PassbookTransactionNotificationContentExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Passwords.app/Passwords](MACHOS/Passwords.md)
- [/private/var/staged_system_apps/Photos.app/Photos](MACHOS/Photos.md)
- [/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/PodcastsClassKitExtension](MACHOS/PodcastsClassKitExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.DiagnosticExtension.appex/com.apple.podcasts.DiagnosticExtension](MACHOS/com.apple.podcasts.DiagnosticExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSpotlightIndexExtension.appex/RemindersSpotlightIndexExtension](MACHOS/RemindersSpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDiagnosticExtension.appex/StocksDiagnosticExtension](MACHOS/StocksDiagnosticExtension.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsQuicklook.appex/TipsQuicklook](MACHOS/TipsQuicklook.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/Extensions/WeatherAppIntents.appex/WeatherAppIntents](MACHOS/WeatherAppIntents.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherDiagnosticExtension.appex/WeatherDiagnosticExtension](MACHOS/WeatherDiagnosticExtension.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents](MACHOS/WeatherIntents.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/ifconfig](MACHOS/ifconfig.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount](MACHOS/mount.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/csfdiagnose](MACHOS/csfdiagnose.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/bin/vm_stat](MACHOS/vm_stat.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/lib/libramrod.dylib](MACHOS/libramrod.dylib.md)
- [/usr/lib/swift/libswiftRemoteMirror.dylib](MACHOS/libswiftRemoteMirror.dylib.md)
- [/usr/lib/system/introspection/libdispatch.dylib](MACHOS/libdispatch.dylib.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/BatteryAlgorithms.framework/BatteryAlgorithms](MACHOS/BatteryAlgorithms.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/FinishRestoreFromBackup](MACHOS/FinishRestoreFromBackup.md)
- [/usr/libexec/MobileStorageMounter](MACHOS/MobileStorageMounter.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/PowerUIAgent](MACHOS/PowerUIAgent.md)
- [/usr/libexec/PurpleReverseProxy](MACHOS/PurpleReverseProxy.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/SensorKitALSHelper](MACHOS/SensorKitALSHelper.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/amfid](MACHOS/amfid.md)
- [/usr/libexec/announced](MACHOS/announced.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/aonsensed](MACHOS/aonsensed.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/appleidsetupd](MACHOS/appleidsetupd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/asd](MACHOS/asd.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/bootpd](MACHOS/bootpd.md)
- [/usr/libexec/captiveagent](MACHOS/captiveagent.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/ciphermld](MACHOS/ciphermld.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/configd](MACHOS/configd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/demod_helper](MACHOS/demod_helper.md)
- [/usr/libexec/dhcp6d](MACHOS/dhcp6d.md)
- [/usr/libexec/diagnosticspushd](MACHOS/diagnosticspushd.md)
- [/usr/libexec/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/dtfetchsymbolsd](MACHOS/dtfetchsymbolsd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/eventkitsyncd](MACHOS/eventkitsyncd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmybeaconingd](MACHOS/findmybeaconingd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/fskitd](MACHOS/fskitd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/installd](MACHOS/installd.md)
- [/usr/libexec/keybagd](MACHOS/keybagd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/launchd_cache_loader](MACHOS/launchd_cache_loader.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd](MACHOS/logd.md)
- [/usr/libexec/lskdd](MACHOS/lskdd.md)
- [/usr/libexec/managedappsd](MACHOS/managedappsd.md)
- [/usr/libexec/memoryanalyticsd](MACHOS/memoryanalyticsd.md)
- [/usr/libexec/merchantd](MACHOS/merchantd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobile_obliterator](MACHOS/mobile_obliterator.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
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
- [/usr/libexec/otpaird](MACHOS/otpaird.md)
- [/usr/libexec/pcapd](MACHOS/pcapd.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/powerexperienced](MACHOS/powerexperienced.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remoteappintentsd](MACHOS/remoteappintentsd.md)
- [/usr/libexec/remotectl](MACHOS/remotectl.md)
- [/usr/libexec/remoted](MACHOS/remoted.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/restoreserviced](MACHOS/restoreserviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/sirireaderd](MACHOS/sirireaderd.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/systemservicemonitord](MACHOS/systemservicemonitord.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/teslad](MACHOS/teslad.md)
- [/usr/libexec/textcontextd](MACHOS/textcontextd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tzd](MACHOS/tzd.md)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/wifianalyticsd](MACHOS/wifianalyticsd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/BlueTool](MACHOS/BlueTool.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/ckksctl](MACHOS/ckksctl.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/filecoordinationd](MACHOS/filecoordinationd.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/notifyd](MACHOS/notifyd.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (20)

<details>
  <summary><i>View Updated</i></summary>

- [AppleAVE2FW_H17.im4p](FIRMWARE/AppleAVE2FW_H17.im4p.md)
- [SmartIOFirmware_ASCv7.im4p](FIRMWARE/SmartIOFirmware_ASCv7.im4p.md)
- [adc-rheia-d9x.im4p](FIRMWARE/adc-rheia-d9x.im4p.md)
- [agx_a000.bin](FIRMWARE/agx_a000.bin.md)
- [agx_a010.bin](FIRMWARE/agx_a010.bin.md)
- [agx_b000.bin](FIRMWARE/agx_b000.bin.md)
- [agx_b010.bin](FIRMWARE/agx_b010.bin.md)
- [agx_b100.bin](FIRMWARE/agx_b100.bin.md)
- [ansf.t8140.release.im4p](FIRMWARE/ansf.t8140.release.im4p.md)
- [exclave_ExclaveStackshotServer](FIRMWARE/exclave_ExclaveStackshotServer.md)
- [exclave_kernel](FIRMWARE/exclave_kernel.md)
- [exclave_pmm_exclave](FIRMWARE/exclave_pmm_exclave.md)
- [exclave_roottask](FIRMWARE/exclave_roottask.md)
- [exclave_scheduler](FIRMWARE/exclave_scheduler.md)
- [exclave_sharedcache](FIRMWARE/exclave_sharedcache.md)
- [rans.t8140.release.im4p](FIRMWARE/rans.t8140.release.im4p.md)
- [securem3fw-d9x.im4p](FIRMWARE/securem3fw-d9x.im4p.md)
- [sptm.t8140.release.im4p](FIRMWARE/sptm.t8140.release.im4p.md)
- [t8140pmp.im4p](FIRMWARE/t8140pmp.im4p.md)
- [txm.iphoneos.release.im4p](FIRMWARE/txm.iphoneos.release.im4p.md)

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.4 *(22E5200s)* | 621.1.10.20.6 |
| 18.4 *(22E5216h)* | 621.1.13.10.4 |

### Dylibs

#### 🆕 NEW (7)

- `/System/Library/AccessibilityBundles/CameraOverlayAngel.axbundle/CameraOverlayAngel`
- `/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal`
- `/System/Library/PrivateFrameworks/ManagedOrganizationContacts.framework/ManagedOrganizationContacts`
- `/System/Library/PrivateFrameworks/SeymourServicesCore.framework/SeymourServicesCore`
- `/System/Library/PrivateFrameworks/SeymourSessionServices.framework/SeymourSessionServices`
- `/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion`
- `/System/Library/PrivateFrameworks/VisionCompanionServices.framework/VisionCompanionServices`

#### ❌ Removed (1)

- `/usr/lib/swift/~libswiftPencilKit.dylib`

#### ⬆️ Updated (1608)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider](DYLIBS/ASMessagesProvider.md)
- [/System/Library/AccessibilityBundles/AVKit.axbundle/AVKit](DYLIBS/AVKit.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension](DYLIBS/AppInstallExtension.md)
- [/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore](DYLIBS/AppStore.md)
- [/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade](DYLIBS/Arcade.md)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension](DYLIBS/BridgeStoreExtension.md)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/DashBoard.axbundle/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService](DYLIBS/InCallService.md)
- [/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework](DYLIBS/MobileSafariFramework.md)
- [/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/AccessibilityBundles/Music.axbundle/Music](DYLIBS/Music.md)
- [/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication](DYLIBS/MusicApplication.md)
- [/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension](DYLIBS/ProductPageExtension.md)
- [/System/Library/AccessibilityBundles/QuickLook.axbundle/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/AccessibilityBundles/Setup.axbundle/Setup](DYLIBS/Setup.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/SpringBoardUIServices.axbundle/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/AccessibilityBundles/StoreDynamicUIPlugin.axbundle/StoreDynamicUIPlugin](DYLIBS/StoreDynamicUIPlugin.md)
- [/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/AccessibilityBundles/iCloudSettings.axbundle/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin](DYLIBS/AAAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AISAccountNotificationPlugin.bundle/AISAccountNotificationPlugin](DYLIBS/AISAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin](DYLIBS/AMSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreIDVAccountNotificationPlugin.bundle/CoreIDVAccountNotificationPlugin](DYLIBS/CoreIDVAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/DonationAccountWatcher.bundle/DonationAccountWatcher](DYLIBS/DonationAccountWatcher.md)
- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Accounts/Notification/LockdownModeAccountNotificationPlugin.bundle/LockdownModeAccountNotificationPlugin](DYLIBS/LockdownModeAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/NotesAccountNotificationPlugin](DYLIBS/NotesAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin](DYLIBS/PCSAccountNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterSingleTileModule.bundle/HomeControlCenterSingleTileModule](DYLIBS/HomeControlCenterSingleTileModule.md)
- [/System/Library/Extensions/AGXMetalG17P.bundle/AGXMetalG17P](DYLIBS/AGXMetalG17P.md)
- [/System/Library/Fitness/Plugins/SeymourAwardsPlugin.bundle/SeymourAwardsPlugin](DYLIBS/SeymourAwardsPlugin.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit](DYLIBS/AccessorySetupKit.md)
- [/System/Library/Frameworks/Accounts.framework/Accounts](DYLIBS/Accounts.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit](DYLIBS/AdAttributionKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/AutomatedDeviceEnrollment](DYLIBS/AutomatedDeviceEnrollment.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/BrowserKit.framework/BrowserKit](DYLIBS/BrowserKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CarKey.framework/CarKey](DYLIBS/CarKey.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/ClassKit.framework/ClassKit](DYLIBS/ClassKit.md)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
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
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI](DYLIBS/CoreMIDI.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreNFC.framework/CoreNFC](DYLIBS/CoreNFC.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterAWDMetrics.dylib](DYLIBS/libCommCenterAWDMetrics.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable](DYLIBS/CoreTransferable.md)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/DeviceDiscoveryExtension.framework/DeviceDiscoveryExtension](DYLIBS/DeviceDiscoveryExtension.md)
- [/System/Library/Frameworks/DockKit.framework/DockKit](DYLIBS/DockKit.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControls](DYLIBS/FamilyControls.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/iCloudDriveFileProviderOverride.bundle/iCloudDriveFileProviderOverride](DYLIBS/iCloudDriveFileProviderOverride.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/JournalingSuggestions.framework/JournalingSuggestions](DYLIBS/JournalingSuggestions.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture](DYLIBS/LockedCameraCapture.md)
- [/System/Library/Frameworks/ManagedApp.framework/ManagedApp](DYLIBS/ManagedApp.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings](DYLIBS/ManagedSettings.md)
- [/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI](DYLIBS/ManagedSettingsUI.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MatterSupport.framework/MatterSupport](DYLIBS/MatterSupport.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MediaToolbox.framework/Support/libSTS-N.dylib](DYLIBS/libSTS-N.dylib.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/MPSImage](DYLIBS/MPSImage.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage](DYLIBS/NaturalLanguage.md)
- [/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction](DYLIBS/NearbyInteraction.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/OpenGLES.framework/GLEngine.bundle/GLEngine](DYLIBS/GLEngine.md)
- [/System/Library/Frameworks/OpenGLES.framework/OpenGLES](DYLIBS/OpenGLES.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGFXShared.dylib](DYLIBS/libGFXShared.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLImage.dylib](DYLIBS/libGLImage.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLProgrammability.dylib](DYLIBS/libGLProgrammability.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLVMPlugin.dylib](DYLIBS/libGLVMPlugin.dylib.md)
- [/System/Library/Frameworks/PHASE.framework/PHASE](DYLIBS/PHASE.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SafetyKit.framework/SafetyKit](DYLIBS/SafetyKit.md)
- [/System/Library/Frameworks/ScreenTime.framework/ScreenTime](DYLIBS/ScreenTime.md)
- [/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential](DYLIBS/SecureElementCredential.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SecurityUI.framework/SecurityUI](DYLIBS/SecurityUI.md)
- [/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis](DYLIBS/SensitiveContentAnalysis.md)
- [/System/Library/Frameworks/SensorKit.framework/SensorKit](DYLIBS/SensorKit.md)
- [/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou](DYLIBS/SharedWithYou.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
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
- [/System/Library/Frameworks/TranslationUIProvider.framework/TranslationUIProvider](DYLIBS/TranslationUIProvider.md)
- [/System/Library/Frameworks/UserNotifications.framework/UserNotifications](DYLIBS/UserNotifications.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/VisionKit.framework/VisionKit](DYLIBS/VisionKit.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib](DYLIBS/libWebKitSwift.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AVKit_SwiftUI.framework/_AVKit_SwiftUI](DYLIBS/_AVKit_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_Intents_TipKit.framework/_Intents_TipKit](DYLIBS/_Intents_TipKit.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_SecureElementCredential_SwiftUI.framework/_SecureElementCredential_SwiftUI](DYLIBS/_SecureElementCredential_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/AppRecommendations.healthplugin/AppRecommendations](DYLIBS/AppRecommendations.md)
- [/System/Library/Health/FeedItemPlugins/Categories.healthplugin/Categories](DYLIBS/Categories.md)
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
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications](DYLIBS/NanoCompassComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences](DYLIBS/VPNPreferences.md)
- [/System/Library/PreferenceBundles/WirelessModemSettings.bundle/WirelessModemSettings](DYLIBS/WirelessModemSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/AACCore](DYLIBS/AACCore.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/ALDataTypes.framework/ALDataTypes.dylib](DYLIBS/ALDataTypes.dylib.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/AONSense.framework/AONSense.dylib](DYLIBS/AONSense.dylib.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore.md)
- [/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon](DYLIBS/ARKitDaemon.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader](DYLIBS/AXAssetLoader.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils](DYLIBS/AXFrontBoardUtils.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection](DYLIBS/AXSoundDetection.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenServices.framework/AXWatchRemoteScreenServices](DYLIBS/AXWatchRemoteScreenServices.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI](DYLIBS/AXWatchRemoteScreenUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccountSuggestions.framework/AccountSuggestions](DYLIBS/AccountSuggestions.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing](DYLIBS/ActivitySharing.md)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient.md)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI.md)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AdaptiveMusic.framework/AdaptiveMusic](DYLIBS/AdaptiveMusic.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AeroML.framework/AeroML](DYLIBS/AeroML.md)
- [/System/Library/PrivateFrameworks/AirPlayAndHandoffSettingsSupport.framework/AirPlayAndHandoffSettingsSupport](DYLIBS/AirPlayAndHandoffSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AlarmUIFramework.framework/AlarmUIFramework](DYLIBS/AlarmUIFramework.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics](DYLIBS/AppInstallationMetrics.md)
- [/System/Library/PrivateFrameworks/AppIntentSchemas.framework/AppIntentSchemas](DYLIBS/AppIntentSchemas.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppMigrationKit.framework/AppMigrationKit](DYLIBS/AppMigrationKit.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionToolsInternal.framework/AppPredictionToolsInternal](DYLIBS/AppPredictionToolsInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation](DYLIBS/AppPredictionUIFoundation.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionDaemon.framework/AppProtectionDaemon](DYLIBS/AppProtectionDaemon.md)
- [/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI](DYLIBS/AppProtectionUI.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO](DYLIBS/AppSSO.md)
- [/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore](DYLIBS/AppSSOCore.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays](DYLIBS/AppStoreOverlays.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth](DYLIBS/AppleDepth.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libAppleDeviceQueryArmory.dylib](DYLIBS/libAppleDeviceQueryArmory.dylib.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKit.framework/AppleMediaServicesKit](DYLIBS/AppleMediaServicesKit.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService.md)
- [/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication](DYLIBS/AppleTracingSupportSymbolication.md)
- [/System/Library/PrivateFrameworks/Archetype.framework/Archetype](DYLIBS/Archetype.md)
- [/System/Library/PrivateFrameworks/ArchetypeEngine.framework/ArchetypeEngine](DYLIBS/ArchetypeEngine.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskTo.framework/AskTo](DYLIBS/AskTo.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon](DYLIBS/AskToDaemon.md)
- [/System/Library/PrivateFrameworks/AssetExplorer.framework/AssetExplorer](DYLIBS/AssetExplorer.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI](DYLIBS/AssistiveTouchUI.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver](DYLIBS/AudioServerDriver.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP](DYLIBS/AudioServerDriverTransports_IOP.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion](DYLIBS/AudiogramIngestion.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation](DYLIBS/BackBoardHIDEventFoundation.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms](DYLIBS/BatteryAlgorithms.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/BiomeFlexibleStorage](DYLIBS/BiomeFlexibleStorage.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport](DYLIBS/BiometricSupport.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices](DYLIBS/BluetoothServices.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BookUtility.framework/BookUtility](DYLIBS/BookUtility.md)
- [/System/Library/PrivateFrameworks/Bosporus.framework/Bosporus](DYLIBS/Bosporus.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/BusinessServicesUI.framework/BusinessServicesUI](DYLIBS/BusinessServicesUI.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary](DYLIBS/CBORLibrary.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete.md)
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
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarAssetUtils.framework/CarAssetUtils](DYLIBS/CarAssetUtils.md)
- [/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework](DYLIBS/CarCommandsUIFramework.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsSupport.framework/WidgetPreviewsSupport](DYLIBS/WidgetPreviewsSupport.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClarityBoardFoundation.framework/ClarityBoardFoundation](DYLIBS/ClarityBoardFoundation.md)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/ClassKitUI](DYLIBS/ClassKitUI.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/ClockUIFramework.framework/ClockUIFramework](DYLIBS/ClockUIFramework.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets](DYLIBS/CloudAssets.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices](DYLIBS/CloudPhotoServices.md)
- [/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation](DYLIBS/CloudRecommendation.md)
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
- [/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay](DYLIBS/ComplicationDisplay.md)
- [/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards](DYLIBS/ComputeSafeguards.md)
- [/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel](DYLIBS/ConfigurationEngineModel.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContactsWidgetUI.framework/ContactsWidgetUI](DYLIBS/ContactsWidgetUI.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextualSuggestionClient.framework/ContextualSuggestionClient](DYLIBS/ContextualSuggestionClient.md)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/ContextualUnderstanding](DYLIBS/ContextualUnderstanding.md)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices](DYLIBS/ControlCenterUIServices.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CookingData.framework/CookingData](DYLIBS/CookingData.md)
- [/System/Library/PrivateFrameworks/CookingKit.framework/CookingKit](DYLIBS/CookingKit.md)
- [/System/Library/PrivateFrameworks/CookingSupport.framework/CookingSupport](DYLIBS/CookingSupport.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest](DYLIBS/CoreGPSTest.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID](DYLIBS/CoreHID.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred](DYLIBS/CoreIDCred.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf](DYLIBS/CoreLocationProtobuf.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles](DYLIBS/CoreLocationTiles.md)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream.md)
- [/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms](DYLIBS/CoreMotionAlgorithms.md)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO](DYLIBS/CoreRealityIO.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal](DYLIBS/CoreServicesInternal.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils](DYLIBS/CoreSpeechUtils.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication](DYLIBS/CoreSymbolication.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreUtilsUI.framework/CoreUtilsUI](DYLIBS/CoreUtilsUI.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/CryptexKit.framework/CryptexKit](DYLIBS/CryptexKit.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary](DYLIBS/DMCEnrollmentLibrary.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DSContinuityPairing.framework/DSContinuityPairing](DYLIBS/DSContinuityPairing.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities](DYLIBS/DVTInstrumentsUtilities.md)
- [/System/Library/PrivateFrameworks/DailyBriefingCommon.framework/DailyBriefingCommon](DYLIBS/DailyBriefingCommon.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal](DYLIBS/DarwinDirectoryInternal.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryQuery.framework/DarwinDirectoryQuery](DYLIBS/DarwinDirectoryQuery.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/DefaultAppsSettingsUI.framework/DefaultAppsSettingsUI](DYLIBS/DefaultAppsSettingsUI.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/DendriteIngest](DYLIBS/DendriteIngest.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore](DYLIBS/DeviceDiscoveryUICore.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing](DYLIBS/DeviceSharing.md)
- [/System/Library/PrivateFrameworks/DeviceSharingServices.framework/DeviceSharingServices](DYLIBS/DeviceSharingServices.md)
- [/System/Library/PrivateFrameworks/DeviceSharingServicesCore.framework/DeviceSharingServicesCore](DYLIBS/DeviceSharingServicesCore.md)
- [/System/Library/PrivateFrameworks/DeviceSharingUI.framework/DeviceSharingUI](DYLIBS/DeviceSharingUI.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest](DYLIBS/DiagnosticRequest.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration](DYLIBS/DiskArbitration.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement](DYLIBS/DriverManagement.md)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/Dyld.framework/Dyld](DYLIBS/Dyld.md)
- [/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity](DYLIBS/EDPSecurity.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/EncoreXPCService.framework/EncoreXPCService](DYLIBS/EncoreXPCService.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/ExposureNotificationDaemon.framework/ExposureNotificationDaemon](DYLIBS/ExposureNotificationDaemon.md)
- [/System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite](DYLIBS/FMCoreLite.md)
- [/System/Library/PrivateFrameworks/FMF.framework/FMF](DYLIBS/FMF.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFUI.framework/FMFUI](DYLIBS/FMFUI.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking](DYLIBS/FMNetworking.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeFeatureControl.framework/FaceTimeFeatureControl](DYLIBS/FaceTimeFeatureControl.md)
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
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyCore.framework/FindMyCore](DYLIBS/FindMyCore.md)
- [/System/Library/PrivateFrameworks/FindMyCrypto.framework/FindMyCrypto](DYLIBS/FindMyCrypto.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyLocateObjCWrapper.framework/FindMyLocateObjCWrapper](DYLIBS/FindMyLocateObjCWrapper.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyPairing.framework/FindMyPairing](DYLIBS/FindMyPairing.md)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction](DYLIBS/FindMyServerInteraction.md)
- [/System/Library/PrivateFrameworks/FindMyStorage.framework/FindMyStorage](DYLIBS/FindMyStorage.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
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
- [/System/Library/PrivateFrameworks/FitnessSync.framework/FitnessSync](DYLIBS/FitnessSync.md)
- [/System/Library/PrivateFrameworks/FitnessTrainerTips.framework/FitnessTrainerTips](DYLIBS/FitnessTrainerTips.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities](DYLIBS/FitnessUtilities.md)
- [/System/Library/PrivateFrameworks/FlowFrameKit.framework/FlowFrameKit](DYLIBS/FlowFrameKit.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib](DYLIBS/libGSFontCache.dylib.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService.md)
- [/System/Library/PrivateFrameworks/GameCenterServerClient.framework/GameCenterServerClient](DYLIBS/GameCenterServerClient.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy.md)
- [/System/Library/PrivateFrameworks/GameServices.framework/GameServices](DYLIBS/GameServices.md)
- [/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore](DYLIBS/GameServicesCore.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/GenerativeAssistantCommon](DYLIBS/GenerativeAssistantCommon.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantEnablementFlow.framework/GenerativeAssistantEnablementFlow](DYLIBS/GenerativeAssistantEnablementFlow.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantUI.framework/GenerativeAssistantUI](DYLIBS/GenerativeAssistantUI.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctions.framework/GenerativeFunctions](DYLIBS/GenerativeFunctions.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices](DYLIBS/H16ISPServices.md)
- [/System/Library/PrivateFrameworks/HIDRMClientKit.framework/HIDRMClientKit](DYLIBS/HIDRMClientKit.md)
- [/System/Library/PrivateFrameworks/HIDRMKit.framework/HIDRMKit](DYLIBS/HIDRMKit.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService](DYLIBS/HeadphoneProxFeatureService.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon](DYLIBS/HealthAppHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport](DYLIBS/HealthAppHealthDaemonSupport.md)
- [/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices](DYLIBS/HealthAppServices.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceAppPlugin.framework/HealthBalanceAppPlugin](DYLIBS/HealthBalanceAppPlugin.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthDaemonFeatures.framework/HealthDaemonFeatures](DYLIBS/HealthDaemonFeatures.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon](DYLIBS/HealthHearingDaemon.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI](DYLIBS/HealthMedicationsVisionUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI](DYLIBS/HealthMedicationsWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesWidgetUI.framework/HealthMenstrualCyclesWidgetUI](DYLIBS/HealthMenstrualCyclesWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration](DYLIBS/HealthOrchestration.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthRecordsWalletSupport.framework/HealthRecordsWalletSupport](DYLIBS/HealthRecordsWalletSupport.md)
- [/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore](DYLIBS/HearingCore.md)
- [/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI](DYLIBS/HearingModeSettingsUI.md)
- [/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI](DYLIBS/HearingModeUI.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI](DYLIBS/HeartRhythmUI.md)
- [/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal](DYLIBS/Heimdal.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI](DYLIBS/HomeAI.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeCommunicationUIFramework.framework/HomeCommunicationUIFramework](DYLIBS/HomeCommunicationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/HomeKitDaemonFoundation](DYLIBS/HomeKitDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
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
- [/System/Library/PrivateFrameworks/Human.framework/Human](DYLIBS/Human.md)
- [/System/Library/PrivateFrameworks/HumanUI.framework/HumanUI](DYLIBS/HumanUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMAVCore.framework/IMAVCore](DYLIBS/IMAVCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMRCSTransfer.framework/IMRCSTransfer](DYLIBS/IMRCSTransfer.md)
- [/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI](DYLIBS/IMSharedUI.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo](DYLIBS/IOAccelMemoryInfo.md)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator](DYLIBS/IOSurfaceAccelerator.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices](DYLIBS/IdleTimerServices.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/InputAccessoriesSettings.framework/InputAccessoriesSettings](DYLIBS/InputAccessoriesSettings.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowAppIntentsPreviewToolSupport.framework/IntelligenceFlowAppIntentsPreviewToolSupport](DYLIBS/IntelligenceFlowAppIntentsPreviewToolSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared](DYLIBS/IntelligenceFlowShared.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentRoutingMediaBundles.framework/IntelligentRoutingMediaBundles](DYLIBS/IntelligentRoutingMediaBundles.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences](DYLIBS/IntlPreferences.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/JITAppKit.framework/JITAppKit](DYLIBS/JITAppKit.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/JetCore](DYLIBS/JetCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/JoinRequests.framework/JoinRequests](DYLIBS/JoinRequests.md)
- [/System/Library/PrivateFrameworks/KRExperiments.framework/KRExperiments](DYLIBS/KRExperiments.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper](DYLIBS/KoaMapper.md)
- [/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache](DYLIBS/LLMCache.md)
- [/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures](DYLIBS/LearnedFeatures.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseAV.framework/LighthouseAV](DYLIBS/LighthouseAV.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LighthouseQuartz.framework/LighthouseQuartz](DYLIBS/LighthouseQuartz.md)
- [/System/Library/PrivateFrameworks/LighthouseServicesAnalyticsFramework.framework/LighthouseServicesAnalyticsFramework](DYLIBS/LighthouseServicesAnalyticsFramework.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkPresentationStyleSheetParsing.framework/LinkPresentationStyleSheetParsing](DYLIBS/LinkPresentationStyleSheetParsing.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper](DYLIBS/LiveFSFPHelper.md)
- [/System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices](DYLIBS/LiveSpeechServices.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI](DYLIBS/LocalAuthenticationPrivateUI.md)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit](DYLIBS/LocalStatusKit.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode](DYLIBS/LockdownMode.md)
- [/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport](DYLIBS/LoggingSupport.md)
- [/System/Library/PrivateFrameworks/MCCFoundation.framework/MCCFoundation](DYLIBS/MCCFoundation.md)
- [/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization](DYLIBS/MCCKitCategorization.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MagnifierServices.framework/MagnifierServices](DYLIBS/MagnifierServices.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MailWebProcessSupport.framework/MailWebProcessSupport](DYLIBS/MailWebProcessSupport.md)
- [/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging](DYLIBS/MallocStackLogging.md)
- [/System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore](DYLIBS/ManagedAppsCore.md)
- [/System/Library/PrivateFrameworks/ManagedAppsInterface.framework/ManagedAppsInterface](DYLIBS/ManagedAppsInterface.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC](DYLIBS/ManagedSettingsObjC.md)
- [/System/Library/PrivateFrameworks/ManagedSettingsSupport.framework/ManagedSettingsSupport](DYLIBS/ManagedSettingsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin](DYLIBS/MatterPlugin.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl](DYLIBS/MediaControl.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService](DYLIBS/MediaConversionService.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon](DYLIBS/MentalHealthDaemon.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthWidgetUI.framework/MentalHealthWidgetUI](DYLIBS/MentalHealthWidgetUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices](DYLIBS/MobileAssetExclaveServices.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI](DYLIBS/MobileIdentityServiceUI.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer](DYLIBS/MobileMulticastTransfer.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage](DYLIBS/MobileStorage.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/ModelMonitoringLighthouse.framework/ModelMonitoringLighthouse](DYLIBS/ModelMonitoringLighthouse.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MorphunSwift.framework/MorphunSwift](DYLIBS/MorphunSwift.md)
- [/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging](DYLIBS/MotionSensorLogging.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit](DYLIBS/NPTKit.md)
- [/System/Library/PrivateFrameworks/NanoHomeIntents.framework/NanoHomeIntents](DYLIBS/NanoHomeIntents.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore](DYLIBS/NanoPhotosCore.md)
- [/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry](DYLIBS/NanoRegistry.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NanoUniverse](DYLIBS/NanoUniverse.md)
- [/System/Library/PrivateFrameworks/NanoWeatherKitUICompanion.framework/NanoWeatherKitUICompanion](DYLIBS/NanoWeatherKitUICompanion.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory](DYLIBS/NearFieldAccessory.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions](DYLIBS/NearbySessions.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay](DYLIBS/NetworkRelay.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/Library/PrivateFrameworks/NewsEngagementCollector.framework/NewsEngagementCollector](DYLIBS/NewsEngagementCollector.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit](DYLIBS/NewsKit.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport](DYLIBS/NewsTransport.md)
- [/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI](DYLIBS/NewsUI.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics](DYLIBS/NotesAnalytics.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesPreviewKit.framework/NotesPreviewKit](DYLIBS/NotesPreviewKit.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSiriUI.framework/NotesSiriUI](DYLIBS/NotesSiriUI.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices](DYLIBS/NotesUIServices.md)
- [/System/Library/PrivateFrameworks/ODCurareAnalysis.framework/ODCurareAnalysis](DYLIBS/ODCurareAnalysis.md)
- [/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting](DYLIBS/ODCurareEvaluationAndReporting.md)
- [/System/Library/PrivateFrameworks/ODDIFramework.framework/ODDIFramework](DYLIBS/ODDIFramework.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OmniSearchTypes.framework/OmniSearchTypes](DYLIBS/OmniSearchTypes.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/OnDeviceStorage](DYLIBS/OnDeviceStorage.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/OpenAPIRuntimeInternal.framework/OpenAPIRuntimeInternal](DYLIBS/OpenAPIRuntimeInternal.md)
- [/System/Library/PrivateFrameworks/OpenAPIURLSessionInternal.framework/OpenAPIURLSessionInternal](DYLIBS/OpenAPIURLSessionInternal.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport](DYLIBS/PBBridgeSupport.md)
- [/System/Library/PrivateFrameworks/PIRGeoProtos.framework/PIRGeoProtos](DYLIBS/PIRGeoProtos.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity](DYLIBS/PairingProximity.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParsingInternal.framework/ParsingInternal](DYLIBS/ParsingInternal.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard](DYLIBS/Pasteboard.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterMetrics.framework/PeopleSuggesterMetrics](DYLIBS/PeopleSuggesterMetrics.md)
- [/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI](DYLIBS/PeopleUI.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader](DYLIBS/PerfPowerServicesReader.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalIntelligenceCore.framework/PersonalIntelligenceCore](DYLIBS/PersonalIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation](DYLIBS/PhotoFoundation.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligenceCore.framework/PhotosIntelligenceCore](DYLIBS/PhotosIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PhotosKnowledgeGraph.framework/PhotosKnowledgeGraph](DYLIBS/PhotosKnowledgeGraph.md)
- [/System/Library/PrivateFrameworks/PhotosSearchClient.framework/PhotosSearchClient](DYLIBS/PhotosSearchClient.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/PhotosensitivityProcessing](DYLIBS/PhotosensitivityProcessing.md)
- [/System/Library/PrivateFrameworks/Planks.framework/Planks](DYLIBS/Planks.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore](DYLIBS/PlatformSSOCore.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSQLite.framework/PoirotSQLite](DYLIBS/PoirotSQLite.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices](DYLIBS/PreviewsServices.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI](DYLIBS/PrintKitUI.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/PrivateMLClientInferenceProvider](DYLIBS/PrivateMLClientInferenceProvider.md)
- [/System/Library/PrivateFrameworks/PrivateSearchCore.framework/PrivateSearchCore](DYLIBS/PrivateSearchCore.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse](DYLIBS/ProactiveShareSheetDataHarvestingLighthouse.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetClient.framework/PromotedContentJetClient](DYLIBS/PromotedContentJetClient.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/PromotedContentJetSupport](DYLIBS/PromotedContentJetSupport.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ProtoDataExtractor.framework/ProtoDataExtractor](DYLIBS/ProtoDataExtractor.md)
- [/System/Library/PrivateFrameworks/Proximity.framework/Proximity](DYLIBS/Proximity.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityReaderCore.framework/ProximityReaderCore](DYLIBS/ProximityReaderCore.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/Quagga.framework/Quagga](DYLIBS/Quagga.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore](DYLIBS/QuickLookUICore.md)
- [/System/Library/PrivateFrameworks/RESync.framework/RESync](DYLIBS/RESync.md)
- [/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting](DYLIBS/RTCReporting.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery](DYLIBS/RapidResourceDelivery.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/RealityKitInspection.framework/RealityKitInspection](DYLIBS/RealityKitInspection.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal](DYLIBS/ReflectionInternal.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore](DYLIBS/RemoteManagementStore.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery](DYLIBS/RemoteServiceDiscovery.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/ResponseUI.framework/ResponseUI](DYLIBS/ResponseUI.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SILManager.framework/SILManager](DYLIBS/SILManager.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS.md)
- [/System/Library/PrivateFrameworks/SPFinder.framework/SPFinder](DYLIBS/SPFinder.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SPRCore.framework/SPRCore](DYLIBS/SPRCore.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient](DYLIBS/STSXPCHelperClient.md)
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
- [/System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices](DYLIBS/ScreenContinuityServices.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit](DYLIBS/SecureCaptureKit.md)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService](DYLIBS/SecureTransactionService.md)
- [/System/Library/PrivateFrameworks/Seeding.framework/Seeding](DYLIBS/Seeding.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert](DYLIBS/SessionAlert.md)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications.md)
- [/System/Library/PrivateFrameworks/SessionSQL.framework/SessionSQL](DYLIBS/SessionSQL.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
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
- [/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression](DYLIBS/SignalCompression.md)
- [/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection](DYLIBS/SignpostCollection.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework](DYLIBS/SiriAppLaunchUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution](DYLIBS/SiriAppResolution.md)
- [/System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils](DYLIBS/SiriAudioIntentUtils.md)
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
- [/System/Library/PrivateFrameworks/SiriMASPFLTraining.framework/SiriMASPFLTraining](DYLIBS/SiriMASPFLTraining.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailOntology.framework/SiriMailOntology](DYLIBS/SiriMailOntology.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriMetricsBugReporter.framework/SiriMetricsBugReporter](DYLIBS/SiriMetricsBugReporter.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPhoneIntents.framework/SiriPhoneIntents](DYLIBS/SiriPhoneIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningLogging.framework/SiriPrivateLearningLogging](DYLIBS/SiriPrivateLearningLogging.md)
- [/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents](DYLIBS/SiriReaderIntents.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver](DYLIBS/SiriReferenceResolver.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSettingsUI.framework/SiriSettingsUI](DYLIBS/SiriSettingsUI.md)
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
- [/System/Library/PrivateFrameworks/SiriTaskEngagement.framework/SiriTaskEngagement](DYLIBS/SiriTaskEngagement.md)
- [/System/Library/PrivateFrameworks/SiriTasksEvaluation.framework/SiriTasksEvaluation](DYLIBS/SiriTasksEvaluation.md)
- [/System/Library/PrivateFrameworks/SiriTimeAlarmInternal.framework/SiriTimeAlarmInternal](DYLIBS/SiriTimeAlarmInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/SiriTimeInternal](DYLIBS/SiriTimeInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTranslationUI.framework/SiriTranslationUI](DYLIBS/SiriTranslationUI.md)
- [/System/Library/PrivateFrameworks/SiriTurnRestatement.framework/SiriTurnRestatement](DYLIBS/SiriTurnRestatement.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge](DYLIBS/SiriUIBridge.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework](DYLIBS/SiriVideoUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution.md)
- [/System/Library/PrivateFrameworks/SiriXShimTools.framework/SiriXShimTools](DYLIBS/SiriXShimTools.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer](DYLIBS/SmartRepliesServer.md)
- [/System/Library/PrivateFrameworks/SmartRepliesUI.framework/SmartRepliesUI](DYLIBS/SmartRepliesUI.md)
- [/System/Library/PrivateFrameworks/SnippetCommands.framework/SnippetCommands](DYLIBS/SnippetCommands.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SnippetUI_Proto.framework/SnippetUI_Proto](DYLIBS/SnippetUI_Proto.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI](DYLIBS/SoftwareUpdateServicesUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpatialInspectorFoundation.framework/SpatialInspectorFoundation](DYLIBS/SpatialInspectorFoundation.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices](DYLIBS/SpeechRecognitionCommandServices.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore](DYLIBS/SpeechRecognitionCore.md)
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
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardIntents.framework/SpringBoardIntents](DYLIBS/SpringBoardIntents.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/StickerFoundationInternal.framework/StickerFoundationInternal](DYLIBS/StickerFoundationInternal.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor](DYLIBS/StreamingExtractor.md)
- [/System/Library/PrivateFrameworks/StrokeAnimation.framework/StrokeAnimation](DYLIBS/StrokeAnimation.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SwiftASN1.framework/SwiftASN1](DYLIBS/SwiftASN1.md)
- [/System/Library/PrivateFrameworks/SwiftASN1Internal.framework/SwiftASN1Internal](DYLIBS/SwiftASN1Internal.md)
- [/System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite](DYLIBS/SwiftSQLite.md)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication](DYLIBS/Symbolication.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults](DYLIBS/SyncedDefaults.md)
- [/System/Library/PrivateFrameworks/SyncedDefaultsDaemon.framework/SyncedDefaultsDaemon](DYLIBS/SyncedDefaultsDaemon.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemServiceMonitor.framework/SystemServiceMonitor](DYLIBS/SystemServiceMonitor.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze](DYLIBS/TeaBreeze.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyKit.framework/TelephonyKit](DYLIBS/TelephonyKit.md)
- [/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences](DYLIBS/TelephonyPreferences.md)
- [/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC](DYLIBS/TelephonyRPC.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/TextToSpeechMauiSupport](DYLIBS/TextToSpeechMauiSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](DYLIBS/Tightbeam.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TouchML.framework/TouchML](DYLIBS/TouchML.md)
- [/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance](DYLIBS/TrackingAvoidance.md)
- [/System/Library/PrivateFrameworks/TranslationAPISupport.framework/TranslationAPISupport](DYLIBS/TranslationAPISupport.md)
- [/System/Library/PrivateFrameworks/TranslationPersistence.framework/TranslationPersistence](DYLIBS/TranslationPersistence.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/TrustKit.framework/TrustKit](DYLIBS/TrustKit.md)
- [/System/Library/PrivateFrameworks/TuriCore.framework/TuriCore](DYLIBS/TuriCore.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UINavigationKit.framework/UINavigationKit](DYLIBS/UINavigationKit.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/UnifiedMessagingKit](DYLIBS/UnifiedMessagingKit.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UrchinKit.framework/UrchinKit](DYLIBS/UrchinKit.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices](DYLIBS/VisionHWAccelerationServices.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization](DYLIBS/VisualLocalization.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControl.framework/VoiceControl](DYLIBS/VoiceControl.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherAppSupport.framework/WeatherAppSupport](DYLIBS/WeatherAppSupport.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherData.framework/WeatherData](DYLIBS/WeatherData.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebContentAnalysis.framework/WebContentAnalysis](DYLIBS/WebContentAnalysis.md)
- [/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions](DYLIBS/WebContentRestrictions.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/WirelessInsights](DYLIBS/WirelessInsights.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
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
- [/System/Library/PrivateFrameworks/ZeoliteLanguage.framework/ZeoliteLanguage](DYLIBS/ZeoliteLanguage.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore](DYLIBS/_MusicKitInternal_MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlayer.framework/_MusicKitInternal_MediaPlayer](DYLIBS/_MusicKitInternal_MediaPlayer.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/iCloudCalendarUnifiedSettings.framework/iCloudCalendarUnifiedSettings](DYLIBS/iCloudCalendarUnifiedSettings.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/iCloudDriveService](DYLIBS/iCloudDriveService.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudMailUnifiedSettings.framework/iCloudMailUnifiedSettings](DYLIBS/iCloudMailUnifiedSettings.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerClient.framework/iCloudSubscriptionOptimizerClient](DYLIBS/iCloudSubscriptionOptimizerClient.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerCore.framework/iCloudSubscriptionOptimizerCore](DYLIBS/iCloudSubscriptionOptimizerCore.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/iCloudSubscriptionOptimizerDaemon](DYLIBS/iCloudSubscriptionOptimizerDaemon.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/iCloudSubscriptionOptimizerLighthouse](DYLIBS/iCloudSubscriptionOptimizerLighthouse.md)
- [/System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps](DYLIBS/iMessageApps.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/KeynoteQuicklook.framework/KeynoteQuicklook](DYLIBS/KeynoteQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/NumbersQuicklook.framework/NumbersQuicklook](DYLIBS/NumbersQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/PagesQuicklook.framework/PagesQuicklook](DYLIBS/PagesQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSApplication.framework/TSApplication](DYLIBS/TSApplication.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCharts.framework/TSCharts](DYLIBS/TSCharts.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSDrawables.framework/TSDrawables](DYLIBS/TSDrawables.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSKit.framework/TSKit](DYLIBS/TSKit.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSPersistence.framework/TSPersistence](DYLIBS/TSPersistence.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSStyles.framework/TSStyles](DYLIBS/TSStyles.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSTables.framework/TSTables](DYLIBS/TSTables.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText](DYLIBS/TSText.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime](DYLIBS/lighthouse_runtime.md)
- [/System/Library/PrivateFrameworks/shared_cache_page_prewarming.framework/shared_cache_page_prewarming](DYLIBS/shared_cache_page_prewarming.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineWeather.bundle/RelevanceEngineWeather](DYLIBS/RelevanceEngineWeather.md)
- [/System/Library/TextInput/TextInput_chr.bundle/TextInput_chr](DYLIBS/TextInput_chr.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/i18n/libHZ.dylib](DYLIBS/libHZ.dylib.md)
- [/usr/lib/i18n/libUTF7.dylib](DYLIBS/libUTF7.dylib.md)
- [/usr/lib/i18n/libVIQR.dylib](DYLIBS/libVIQR.dylib.md)
- [/usr/lib/i18n/libZW.dylib](DYLIBS/libZW.dylib.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libAudioToolboxUtility.dylib](DYLIBS/libAudioToolboxUtility.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib.md)
- [/usr/lib/libBasebandCommandDrivers.dylib](DYLIBS/libBasebandCommandDrivers.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversMIPC.dylib](DYLIBS/libBasebandCommandDriversMIPC.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandDiagnostics.dylib](DYLIBS/libBasebandDiagnostics.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerDAL.dylib](DYLIBS/libBasebandManagerDAL.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libETLDIAGLoggingDynamic.dylib](DYLIBS/libETLDIAGLoggingDynamic.dylib.md)
- [/usr/lib/libETLDMCDynamic.dylib](DYLIBS/libETLDMCDynamic.dylib.md)
- [/usr/lib/libHSFilerDynamic.dylib](DYLIBS/libHSFilerDynamic.dylib.md)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libPCITransport.dylib](DYLIBS/libPCITransport.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libRemoteTelephonyTransport.dylib](DYLIBS/libRemoteTelephonyTransport.dylib.md)
- [/usr/lib/libReverseProxyDevice.dylib](DYLIBS/libReverseProxyDevice.dylib.md)
- [/usr/lib/libRoseBooter.dylib](DYLIBS/libRoseBooter.dylib.md)
- [/usr/lib/libSESShared.dylib](DYLIBS/libSESShared.dylib.md)
- [/usr/lib/libSecureMAHelper.dylib](DYLIBS/libSecureMAHelper.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyIOKitDynamic.dylib](DYLIBS/libTelephonyIOKitDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libhvf.dylib](DYLIBS/libhvf.dylib.md)
- [/usr/lib/libhwtrace.dylib](DYLIBS/libhwtrace.dylib.md)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libllvm-lmdb.dylib](DYLIBS/libllvm-lmdb.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftAppleArchive.dylib](DYLIBS/libswiftAppleArchive.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreAudio.dylib](DYLIBS/libswiftCoreAudio.dylib.md)
- [/usr/lib/swift/libswiftCoreLocation.dylib](DYLIBS/libswiftCoreLocation.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftDemangle.dylib](DYLIBS/libswiftDemangle.dylib.md)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib.md)
- [/usr/lib/swift/libswiftMetalKit.dylib](DYLIBS/libswiftMetalKit.dylib.md)
- [/usr/lib/swift/libswiftObservation.dylib](DYLIBS/libswiftObservation.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib](DYLIBS/libswiftUniformTypeIdentifiers.dylib.md)
- [/usr/lib/swift/libswiftVideoToolbox.dylib](DYLIBS/libswiftVideoToolbox.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib.md)
- [/usr/lib/swift/libswift_RegexParser.dylib](DYLIBS/libswift_RegexParser.dylib.md)
- [/usr/lib/swift/libswift_StringProcessing.dylib](DYLIBS/libswift_StringProcessing.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libdispatch.dylib](DYLIBS/libdispatch.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libsystem_c.dylib](DYLIBS/libsystem_c.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_info.dylib](DYLIBS/libsystem_info.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_networkextension.dylib](DYLIBS/libsystem_networkextension.dylib.md)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libRoseUpdater.dylib](DYLIBS/libRoseUpdater.dylib.md)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib.md)

</details>

### Feature Flags

#### 🆕 NEW (3)

<details>
  <summary><i>View New</i></summary>

#### Tetsuo.plist

>  `Domain/Tetsuo.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Phase1</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
</dict>
</plist>

```
#### InternationalSupport.plist

>  `Domain/InternationalSupport.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```
#### SiriTurnRestatement.plist

>  `Domain/SiriTurnRestatement.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```

</details>

#### ⬆️ Updated (33)

<details>
  <summary><i>View Updated</i></summary>

- [Domain/AVKit.plist](FEATURES/AVKit.plist.md)
- [Domain/AppStore.plist](FEATURES/AppStore.plist.md)
- [Domain/AppStoreComponents.plist](FEATURES/AppStoreComponents.plist.md)
- [Domain/AppleMediaServices.plist](FEATURES/AppleMediaServices.plist.md)
- [Domain/AudioDSPManager.plist](FEATURES/AudioDSPManager.plist.md)
- [Domain/BluetoothFeatures.plist](FEATURES/BluetoothFeatures.plist.md)
- [Domain/CompanionServices.plist](FEATURES/CompanionServices.plist.md)
- [Domain/CoreEmoji.plist](FEATURES/CoreEmoji.plist.md)
- [Domain/CoreText.plist](FEATURES/CoreText.plist.md)
- [Domain/DeviceCheck.plist](FEATURES/DeviceCheck.plist.md)
- [Domain/DigitalSeparation.plist](FEATURES/DigitalSeparation.plist.md)
- [Domain/Finance.plist](FEATURES/Finance.plist.md)
- [Domain/Home.plist](FEATURES/Home.plist.md)
- [Domain/HomeApp.plist](FEATURES/HomeApp.plist.md)
- [Domain/IDS.plist](FEATURES/IDS.plist.md)
- [Domain/IntelligencePlatform.plist](FEATURES/IntelligencePlatform.plist.md)
- [Domain/LocalAuthentication.plist](FEATURES/LocalAuthentication.plist.md)
- [Domain/MediaRemote.plist](FEATURES/MediaRemote.plist.md)
- [Domain/NanoRegistry.plist](FEATURES/NanoRegistry.plist.md)
- [Domain/Photos.plist](FEATURES/Photos.plist.md)
- [Domain/Podcasts.plist](FEATURES/Podcasts.plist.md)
- [Domain/ProactiveHarvesting.plist](FEATURES/ProactiveHarvesting.plist.md)
- [Domain/SiriAssistantSuggestions.plist](FEATURES/SiriAssistantSuggestions.plist.md)
- [Domain/SiriHomeAutomation.plist](FEATURES/SiriHomeAutomation.plist.md)
- [Domain/SiriMetrics.plist](FEATURES/SiriMetrics.plist.md)
- [Domain/SiriUI.plist](FEATURES/SiriUI.plist.md)
- [Domain/TVApp.plist](FEATURES/TVApp.plist.md)
- [Domain/TextInputCore.plist](FEATURES/TextInputCore.plist.md)
- [Domain/UIKit.plist](FEATURES/UIKit.plist.md)
- [Domain/Wallet.plist](FEATURES/Wallet.plist.md)
- [Domain/WiFiManager.plist](FEATURES/WiFiManager.plist.md)
- [Domain/WritingTools.plist](FEATURES/WritingTools.plist.md)
- [Domain/ipTelephony.plist](FEATURES/ipTelephony.plist.md)

</details>

## EOF
