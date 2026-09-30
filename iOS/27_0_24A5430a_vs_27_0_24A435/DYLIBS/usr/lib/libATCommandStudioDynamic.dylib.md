## libATCommandStudioDynamic.dylib

> `/usr/lib/libATCommandStudioDynamic.dylib`

```diff

 1585.0.0.0.0
-  __TEXT.__text: 0x556f0
+  __TEXT.__text: 0x559f4
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x1b20
   __TEXT.__gcc_except_tab: 0x57f0
Functions:
~ __ZNSt3__15dequeIN3qmi11ClientProxy5State11TransactionENS_9allocatorIS4_EEE19__add_back_capacityEv : 1100 -> 1120
~ __ZN4QMux5State9send_syncERKNSt3__110shared_ptrIN3qmi15QMuxClientIfaceEEERKNS2_INS3_17SerializedMessageEEE : 2148 -> 2164
~ __ZN3qmi11ClientProxy5State19handleResponse_syncENS_11buffer_viewEt : 1604 -> 1640
~ __ZN3qmi11ClientProxy5State22handleSentMessage_syncEt : 472 -> 480
~ __ZN3qmi16TransactionQueue5State22createTransaction_syncERN5boost9ptr_dequeINS_11TransactionENS2_20heap_clone_allocatorENSt3__19allocatorIPvEEEERKNS6_10shared_ptrINS_17SerializedMessageEEENS6_6chrono8durationIxNS6_5ratioILl1ELl1000EEEEERKN8dispatch5blockIU13block_pointerFvRKNS_12ResponseBaseEEEE : 356 -> 364
~ __ZN3qmi16TransactionQueue5State12sendNow_syncEv : 652 -> 660
~ __ZN3qmi16TransactionQueue5State15startTimer_syncEt : 428 -> 436
~ __ZN3qmi16TransactionQueue5State28sendTransactionResponse_syncEtRKNS_12ResponseBaseE : 1276 -> 1296
~ __ZNSt3__15dequeIPvNS_9allocatorIS1_EEE5eraseENS_16__deque_iteratorIS1_PKS1_RS6_PKS7_lLl512EEE : 592 -> 628
~ __ZN3qmi16TransactionQueue5State10start_syncEv : 7460 -> 7664
~ __ZNSt3__15dequeIN3qmi11ClientProxy5State11TransactionENS_9allocatorIS4_EEED1B9noe220106Ev : 360 -> 364
~ __ZN3qmi11ClientProxy5State37sendInternalErrorResponseForTxId_syncEti : 276 -> 284
~ __ZN3qmi11ClientProxy5State22cancelAllMessages_syncEv : 992 -> 1016
~ __ZNK3qmi11ClientProxy5State20getTxQueueState_syncEv : 972 -> 976
~ __ZN12ATCSDPCQueue7enqueueEPNS_8CallbackE : 1368 -> 1388
~ __ZN9ATCSTimer14MemberCallbackI12ATCSDPCQueueE6invokeEv : 40 -> 44
~ __ZNSt3__16vectorIN3xpc4dictENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 376 -> 364
~ __ZN5boost9ptr_dequeIN3qmi11TransactionENS_20heap_clone_allocatorENSt3__19allocatorIPvEEED1Ev : 176 -> 184
~ __ZN3qmi16TransactionQueue5StateD2Ev : 636 -> 660
~ __ZN3qmi16TransactionQueue5State9stop_syncEv : 576 -> 600
~ __ZN5boost20ptr_container_detail24reversible_ptr_containerINS0_15sequence_configIN3qmi11TransactionENSt3__15dequeIPvNS5_9allocatorIS7_EEEEEENS_20heap_clone_allocatorEE5clearEv : 284 -> 292
~ __ZN3qmi16TransactionQueue5State24findSentTransaction_syncEt : 272 -> 280
~ __ZN3qmi16TransactionQueue5State9push_syncERKNSt3__110shared_ptrINS_17SerializedMessageEEENS2_6chrono8durationIxNS2_5ratioILl1ELl1000EEEEERKN8dispatch5blockIU13block_pointerFvRKNS_12ResponseBaseEEEE : 1056 -> 1068
~ __ZN3qmi16TransactionQueue5State19sendIfPossible_syncEv : 200 -> 212
~ __ZN3qmi16TransactionQueue5State23setSendWindowWidth_syncEj : 208 -> 220
~ __ZN3qmi16TransactionQueue5State16sendTimeout_syncEt : 1184 -> 1192
~ __ZNK3qmi16TransactionQueue5State14dumpState_syncEv : 1040 -> 1048
~ __ZN3qmi16TransactionQueue23setSendWindowWidth_syncEj : 272 -> 284
~ __ZNSt3__16vectorIN8dispatch13group_sessionENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJNS1_5groupEEEEPS2_DpOT_ : 508 -> 524
~ __ZNSt3__15dequeIPvNS_9allocatorIS1_EEE19__add_back_capacityEv : 888 -> 904
~ __ZNSt3__127__for_each_segment_backwardB9noe220106INS_16__deque_iteratorIPvPS2_RS2_PS3_lLl512EEEZNKS_20__move_backward_implINS_17_ClassicAlgPolicyEEclB9noe220106IS6_S6_Li0EEENS_4pairIT_T0_EESC_SC_SD_EUlS3_S3_E_EEvSC_SC_SD_ : 776 -> 884
~ __ZNSt3__15dequeIPvNS_9allocatorIS1_EEE9__emplaceIJRKS1_EEENS_16__deque_iteratorIS1_PS1_RS1_PS9_lLl512EEENS8_IS1_PS6_S7_PKSD_lLl512EEEDpOT_ : 1736 -> 1816
~ __ZN4QMux5State11remove_syncERKNSt3__110shared_ptrIN3qmi15QMuxClientIfaceEEE : 2304 -> 2312
~ __ZNSt3__118__for_each_segmentB9noe220106INS_16__deque_iteratorI13QMuxQueueItemPS2_RS2_PS3_lLl170EEEZNKS_11__move_implINS_17_ClassicAlgPolicyEEclB9noe220106IS6_S6_Li0EEENS_4pairIT_T0_EESC_SC_SD_EUlS3_S3_E_EEvSC_SC_SD_ : 1208 -> 1196
~ __ZNSt3__16vectorIN3qmi11ClientProxyENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 416 -> 420
```
