## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

```diff

-500.45.0.0.0
+500.55.0.0.0
   __TEXT.__const: 0x2090
-  __TEXT.__os_log: 0x86ba
-  __TEXT.__cstring: 0xf6b
-  __TEXT_EXEC.__text: 0x378cc
+  __TEXT.__os_log: 0x8711
+  __TEXT.__cstring: 0xf6c
+  __TEXT_EXEC.__text: 0x37c50
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3a8
   __DATA.__common: 0x70

   __DATA_CONST.__const: 0x9e68
   __DATA_CONST.__kalloc_type: 0x480
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 9EE32AC0-E285-38FB-BCB6-C141928BD234
+  UUID: 7B1E71E6-1C45-3F48-ACDA-33F108498E17
   Functions: 1836
   Symbols:   0
-  CStrings:  506
+  CStrings:  505
 
Functions:
~ __ZN13AppleProResHW12timerHandlerEP18IOTimerEventSource : 3516 -> 3604
~ __ZN13AppleProResHW21reIssueQueuedCommandsEjj : 1388 -> 2240
~ __ZN13AppleProResHW16interruptHandlerEP22IOInterruptEventSourcei : 3092 -> 3096
~ __ZN13AppleProResHW16EncodeFrameGatedEP9IOServiceP16ProRes_Command_s : 1600 -> 1604
~ __ZN13AppleProResHW16DecodeFrameGatedEP9IOServiceP16ProRes_Command_s : 1928 -> 1624
~ __ZN13AppleProResHW22processEncodeFrameDoneER14CommandEntry_s18ProRes_StatusCRC_sjj : 752 -> 772
~ __ZN13AppleProResHW22processDecodeFrameDoneER14CommandEntry_s18ProRes_StatusCRC_sjj : 748 -> 768
~ __ZN13AppleProResHW12attachClientEP9IOServicePvP4task : 2448 -> 2452
~ __ZN13AppleProResHW20waitForPendingFramesEP16UserClientInfo_s : 232 -> 272
~ sub_fffffff0099670f8 -> sub_fffffff0099b29c0 : 84 -> 88
~ __ZN13AppleProResHW25cancelClientCommandsGatedEP9IOService : 132 -> 140
~ __ZN13AppleProResHW12detachClientEP9IOService : 1632 -> 1740
~ __ZN23AppleProResCommandQueue24cancelCommandsFromClientEP9IOService : 288 -> 340
CStrings:
+ "2111111211211122222221222"
+ "AppleProResHW (0x%x): %s(): Discard [%d] cmd[%d] # %d DVA 0x%llx\n"
+ "AppleProResHW (0x%x): %s(): Legacy Reset device \n"
+ "AppleProResHW (0x%x): %s(): New DRTail[%d] 0x%x DRHead[%d] 0x%x DRMemSize 0x%x Q'd(%d) Removed %d of overall size %d\n"
+ "AppleProResHW (0x%x): %s(): PSD Reset device \n"
+ "AppleProResHW (0x%x): %s(): Q decode Cmd[%d] frame# %d DROffs 0x%x m_coreWorkload[coreIdx=%d] = %u Updated DRHead[%d] 0x%x by size %d. framesPending %u CurrentLoadBalanceMode = %d timeout(ms) = %u\n"
+ "AppleProResHW (0x%x): %s(): Q encode Cmd[%d] frame# %d DROffs 0x%x m_coreWorkload[coreIdx=%d] = %u Updated DRHead[%d] 0x%x by size %d. framesPending %u CurrentLoadBalanceMode = %d timeout(ms) = %u\n"
+ "AppleProResHW (0x%x): %s(): [%d] Invalid cmd[%d] to discard from reissue DROffset 0x%x descSize %u\n"
+ "AppleProResHW (0x%x): %s(): [%d] Valid cmd[%d] to reissue from reissue DROffset 0x%x descSize %u\n"
+ "AppleProResHW (0x%x): %s(): reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move a max of %d bytes\n"
+ "AppleProResHW (0x%x): %s(): reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move a max of bytesToCopyTail %d bytesToHead %d\n"
- "211111121121112222222122"
- "AppleProResHW (0x%x): %s(): New DRTail[%d] 0x%x DRHead[%d] 0x%x DRMemSize 0x%x Q'd(%d)\n"
- "AppleProResHW (0x%x): %s(): Q decode Cmd[%d] frame# %d DROffs 0x%x m_coreWorkload[coreIdx=%d] = %u Updated DRHead[%d] 0x%x by size %d. framesPending %u CurrentLoadBalanceMode = %d\n"
- "AppleProResHW (0x%x): %s(): Q encode Cmd[%d] frame# %d DROffs 0x%x m_coreWorkload[coreIdx=%d] = %u Updated DRHead[%d] 0x%x by size %d. framesPending %u CurrentLoadBalanceMode %d\n"
- "AppleProResHW (0x%x): %s(): Reset device \n"
- "AppleProResHW (0x%x): %s(): SW command queue is undefined\n"
- "AppleProResHW (0x%x): %s(): endMove - moved %d bytes\n"
- "AppleProResHW (0x%x): %s(): endMove - moved bytesToCopyTail %d bytesToHead %d\n"
- "AppleProResHW (0x%x): %s(): reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move %d bytes\n"
- "AppleProResHW (0x%x): %s(): reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move bytesToCopyTail %d bytesToHead %d\n"
- "AppleProResHW (0x%x): %s(): startMove - reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move %d bytes\n"
- "AppleProResHW (0x%x): %s(): startMove - reIssueDROffset 0x%x, DRTail[%d] 0x%x, DRHead[%d] 0x%x, to move bytesToCopyTail %d bytesToHead %d\n"

```
