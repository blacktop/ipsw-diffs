## h14_ane_fw_bia_j4xx.im4p

> `h14_ane_fw_bia_j4xx.im4p`

```diff

 
-  __TEXT.__text: 0x95a14
-  __TEXT.__const: 0x201f8
-  __TEXT.__cstring: 0x1338e
+  __TEXT.__text: 0x990e8
+  __TEXT.__const: 0x201e0
+  __TEXT.__cstring: 0x13c49
   __TEXT.__constructor: 0x0
   __TEXT.text_env: 0x20
-  __DATA.__const: 0x50b0
+  __DATA.__const: 0x52a8
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xfd8
-  __DATA._rtk_patchbay: 0x208
+  __DATA.__data: 0xfc8
+  __DATA._rtk_patchbay: 0x228
   __DATA._rtk_init_stack: 0x10000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA.__mod_init_func: 0x0
   __DATA.__noinit: 0x0
   __DATA.__zerofill: 0x53eb0
-  UUID: 31F652CF-D6D9-322D-8124-C85624D00DCB
-  Functions: 1339
+  UUID: 1C8CECF3-62DF-3D10-BA96-9A5BBDA6033B
+  Functions: 1359
   Symbols:   0
-  CStrings:  2177
+  CStrings:  2236
 
CStrings:
+ "(nid >= ((2))) && (nid < 64)"
+ "(nidStopTq > 0) && (nidStopTq < 64)"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/common/CEispInterruptBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/common/msgQ.c"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/CWorkTask.cpp"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/memObj.cpp"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/mutex.cpp"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/sema.cpp"
+ "20:59:10"
+ "32bit"
+ "64bit"
+ "CMD = %#04x [INFERENCE CALL] at %lld : programId=%d processId=%d priority=%d\n"
+ "CSNE_CMD_INFERENCE_CALL"
+ "CSNE_CMD_INFERENCE_CALL dropped. prog %d process %d not running.\n"
+ "CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf bufAddr == 0 \n"
+ "CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf bufSize == 0 \n"
+ "CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf bufValid == 0 \n"
+ "CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf nbrOfBuffers %d != 1 \n"
+ "CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf op %d != 1 \n"
+ "CSNE_CMD_REQUEST_PROCESS_ID"
+ "CSNE_CMD_REQUEST_PROGRAM_ID"
+ "CSNE_CMD_RETURN_PROCESS_ID"
+ "CSNE_CMD_RETURN_PROGRAM_ID"
+ "CSNE_CMD_SET_ACTIVE_CACHE_REQUEST_IN_GROUP"
+ "CSNE_CMD_TM_SYNC_ERR_NOTIFICATION"
+ "Group CacheHandler 0x%llx, active 0x%llx\n"
+ "Low latency path doesn't support multiple segment for now."
+ "Mar 10 2025"
+ "No output buffers are ready for CR 0x%llx, triggerCnt %d, outputUnderflowCnt %d"
+ "PreMap InferenceCallPropertyBuf: addr 0x%llx, size 0x%llx\n"
+ "ProcedureId=%d uuid=0x%llx\n"
+ "ProgramId = %d\n"
+ "Trigger input dropped for CR 0x%llx, triggerCnt %d, inputOverflowCnt %d"
+ "[%s] CMD = %#04x [%s] at %lld : ProgramId = %d Process = %d \n"
+ "[Secure mode] trigger dropped for CR 0x%llx, triggerCnt %d, droppedInSecureModeCnt %d"
+ "appPriority < 8"
+ "appPriority=%d"
+ "bar[%d]: type=%d(%s) cfg=%d(%s) barId=%d value=0x%llx bufSize=%lld\n"
+ "bufAddr"
+ "bufSize"
+ "call->priority < 8"
+ "function should be overidden\n"
+ "function should be overridden\n"
+ "idx < (2)"
+ "idx >= 0 && idx < 64"
+ "idx(%d) for reserved network desc out of range"
+ "inferenceCallProperty addresses: offset=%lld size=%lld mappedBase=%p mappedSize=%llu dvaBase=%p dvaAddr=0x%llx\n"
+ "input  "
+ "intMdia"
+ "kernel "
+ "mkernel"
+ "nbrBar=%d nbrSeg=%d nbrWaitEvt=%d nbrSigEvt=%d\n"
+ "nid=%d nid2=0x%d isBonded=%d isHWbranch=%d isRewind=%d\n"
+ "output "
+ "pBuf"
+ "pBuf->valid"
+ "pCacheReqEventPool->Size() > 0"
+ "pCmd->bufNbr > maxAneIpcBufMsg"
+ "pCmd->numOfPreMapOp == 1"
+ "pCmdAck"
+ "pDirectProcCallEventPool->Size() > 0"
+ "pFwPriorityQueue"
+ "pFwPriorityQueue[i]"
+ "pInferenceCallPropertyBufMapped"
+ "pInferenceCallPropertyBufMapped == __null"
+ "pInferenceCallPropertyBufOrig"
+ "pInferenceCallPropertyBufOrig <= bufAddr && bufAddr < (pInferenceCallPropertyBufOrig + sizeOfInferenceCallPropertyBuf) && (bufAddr + pBuf->size) <= (pInferenceCallPropertyBufOrig + sizeOfInferenceCallPropertyBuf)"
+ "pNetworkDesc"
+ "pPreMapOp->buffer[0].valid"
+ "pProc->pCacheReqList->Size() <= (16 + 2) - 2 + pAneExeLoop->getActiveSharedEventsNbr()"
+ "pProg->builtinProgramId == ANE_NET_TOT"
+ "pProg->nbrOfProcess == 0"
+ "pProg->used == 0"
+ "pProg->used == 1"
+ "pRealSize"
+ "pReq->fwPriority < 8"
+ "pReq->request.bIsMultipleSegments"
+ "pReqNext->fwPriority == foundIndex"
+ "pReservedNetworkDesc[idx] != __null"
+ "pr_dsid"
+ "reserved network desc [%d] is NULL"
+ "scheduleInfo[queueId].sche_fwPriority != (uint32_t(-1))"
+ "scheduleInfo[queueId].sche_fwPriority == pReq->fwPriority"
+ "seg[%d]: id=%d nextId=%d 1stTid=%d isBranching=%d isBranched=%d isLast=%d isRewind=%d addr=0x%llx len=%lld\n"
+ "signalEvent[%d]: type=%d mask=%d id=%lld value=%lld\n"
+ "unexpected usage for nidSecondary (%d), bIsMultipleSegments %d"
+ "unknown"
+ "unknw"
+ "waitEvent[%d]: type=%d mask=%x id=%lld value=%lld\n"
- "(idx >= 0) && (idx < (64))"
- "(nid > 0) && (nid <= 64)"
- "(nidStopTq > 0) && (nidStopTq <= 64)"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/common/CEispInterruptBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/common/msgQ.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/CWorkTask.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/memObj.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/mutex.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/sema.cpp"
- "18:13:53"
- "CDM: Got an unknown Command %zu\n"
- "CMD = %#04x [CR RECYCLE OUTPUT] at %lld : cacheHandler 0x%llx outputSet %d\n"
- "Dec 14 2024"
- "Direct procedure call network desc is NULL"
- "Got an unknown EndPoint command %d\n"
- "Unknown endpoint command"
- "call->priority < sizeof(priorityMapping)/sizeof(uint8_t)"
- "idx >= 0 && idx <= 64"
- "pBufDesc != __null"
- "pCmd->bufNbr >= maxAneIpcBufMsg"
- "pDirectAneRequestNetworkDesc != __null"
- "pPriorityQueue"
- "pPriorityQueue[i]"
- "pProc->pCacheReqList->Size() <= 16 + 2 - 2 + pAneExeLoop->getActiveSharedEventsNbr()"
- "pReq->priority < 8"
- "pReqNext->priority == foundIndex"
- "scheduleInfo[queueId].priority != (uint32_t(-1))"
- "scheduleInfo[queueId].priority == pReq->priority"
- "tqPrty.f.TQPriority == flushQueuePriority"
- "tqPrty.f.TQPriority == queuePriority[queueId] || tqPrty.f.TQPriority == flushQueuePriority"

```
