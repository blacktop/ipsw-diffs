## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

```diff

-450.74.0.0.0
+450.78.0.0.0
   __TEXT.__const: 0x2130
-  __TEXT.__os_log: 0x833a
-  __TEXT.__cstring: 0xf2d
-  __TEXT_EXEC.__text: 0x31d30
+  __TEXT.__os_log: 0x83d3
+  __TEXT.__cstring: 0xf2e
+  __TEXT_EXEC.__text: 0x320e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x398
   __DATA.__common: 0x70

   __DATA_CONST.__const: 0x8788
   __DATA_CONST.__kalloc_type: 0x480
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: BE60BE54-9EE5-3048-BADB-22EAFEEBB466
+  UUID: B341D64B-FC5D-3BF3-B4D8-DBE6D9DC34EA
   Functions: 1630
   Symbols:   0
-  CStrings:  495
+  CStrings:  494
 
Functions:
~ __ZN13AppleProResHW21reIssueQueuedCommandsEjj : 1108 -> 1956
~ __ZN13AppleProResHW16interruptHandlerEP22IOInterruptEventSourcei : 3008 -> 3004
~ __ZN13AppleProResHW16EncodeFrameGatedEP9IOServiceP16ProRes_Command_s : 1428 -> 1436
~ __ZN13AppleProResHW16DecodeFrameGatedEP9IOServiceP16ProRes_Command_s : 1756 -> 1460
~ __ZN13AppleProResHW22processEncodeFrameDoneER14CommandEntry_s18ProRes_StatusCRC_sjj : 756 -> 776
~ __ZN13AppleProResHW22processDecodeFrameDoneER14CommandEntry_s18ProRes_StatusCRC_sjj : 748 -> 768
~ __ZN13AppleProResHW12attachClientEP9IOServicePvP4task : 2424 -> 2428
~ __ZN13AppleProResHW20waitForPendingFramesEP16UserClientInfo_s : 232 -> 272
~ sub_fffffff009709394 -> sub_fffffff009709654 : 84 -> 88
~ __ZN13AppleProResHW25cancelClientCommandsGatedEP9IOService : 132 -> 140
~ __ZN13AppleProResHW12detachClientEP9IOService : 1632 -> 1740
~ __ZN23AppleProResCommandQueue24cancelCommandsFromClientEP9IOService : 256 -> 288
~ __ZN21AppleProResUserClient11encodeFrameEP37ProRes_EncodeFrame_UserKernel_In_Info : 600 -> 676
~ __ZN21AppleProResUserClient11decodeFrameEP37ProRes_DecodeFrame_UserKernel_In_Info : 472 -> 548
CStrings:
+ "2111111211211122222221222"
+ "AppleProResHW (0x%x): %s(): Discard [%d] cmd[%d] # %d DVA 0x%llx\n"
+ "AppleProResHW (0x%x): %s(): New DRTail[%d] 0x%x DRHead[%d] 0x%x DRMemSize 0x%x Q'd(%d) Removed %d of overall size %d\n"
+ "AppleProResHW (0x%x): %s(): Q decode Cmd[%d] frame# %d DROffs 0x%x m_coreWorkload[coreIdx=%d] = %u Updated DRHead[%d] 0x%x by size %d. framesPending %u CurrentLoadBalanceMode = %d timeout(ms) = %u\n"
+ "AppleProResHW (0x%x): %s(): Q encode Cmd[%d] frame# %d DROffs 0x%x m_coreWorkload[coreIdx=%d] = %u Updated DRHead[%d] 0x%x by size %d. framesPending %u CurrentLoadBalanceMode = %d timeout(ms) = %u\n"
+ "AppleProResHW (0x%x): %s(): [%d] Invalid cmd[%d] to discard from reissue DROffset 0x%x descSize %u\n"
+ "AppleProResHW (0x%x): %s(): [%d] Valid cmd[%d] to reissue from reissue DROffset 0x%x descSize %u\n"
+ "AppleProResHW (0x%x): %s(): reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move a max of %d bytes\n"
+ "AppleProResHW (0x%x): %s(): reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move a max of bytesToCopyTail %d bytesToHead %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No cores powered on.\n"
- "211111121121112222222122"
- "AppleProResHW (0x%x): %s(): New DRTail[%d] 0x%x DRHead[%d] 0x%x DRMemSize 0x%x Q'd(%d)\n"
- "AppleProResHW (0x%x): %s(): Q decode Cmd[%d] frame# %d DROffs 0x%x m_coreWorkload[coreIdx=%d] = %u Updated DRHead[%d] 0x%x by size %d. framesPending %u CurrentLoadBalanceMode = %d\n"
- "AppleProResHW (0x%x): %s(): Q encode Cmd[%d] frame# %d DROffs 0x%x m_coreWorkload[coreIdx=%d] = %u Updated DRHead[%d] 0x%x by size %d. framesPending %u CurrentLoadBalanceMode %d\n"
- "AppleProResHW (0x%x): %s(): SW command queue is undefined\n"
- "AppleProResHW (0x%x): %s(): endMove - moved %d bytes\n"
- "AppleProResHW (0x%x): %s(): endMove - moved bytesToCopyTail %d bytesToHead %d\n"
- "AppleProResHW (0x%x): %s(): reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move %d bytes\n"
- "AppleProResHW (0x%x): %s(): reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move bytesToCopyTail %d bytesToHead %d\n"
- "AppleProResHW (0x%x): %s(): startMove - reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move %d bytes\n"
- "AppleProResHW (0x%x): %s(): startMove - reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move bytesToCopyTail %d bytesToHead %d\n"

```
