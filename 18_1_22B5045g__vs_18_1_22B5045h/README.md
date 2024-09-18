# 18.1 (22B5045g) .vs 18.1 (22B5045h)

## IPSWs

- `iPhone16,2_18.1_22B5045g_Restore.ipsw`
- `iPhone17,1_18.1_22B5045h_Restore.ipsw`

## Kernel

### Version

| iOS               | Version | Build          | Date                        |
| :---------------- | :------ | :------------- | :-------------------------- |
| 18.1 *(22B5045g)* | 24.1.0  | 11215.40.48~34 | Mon, 02Sep2024 22:25:18 PDT |
| 18.1 *(22B5045h)* | 24.1.0  | 11215.40.48~34 | Mon, 02Sep2024 22:23:47 PDT |

### Kexts

#### 🆕 NEW (51)

- `com.apple.AGXFirmwareKextG17PRTBuddy`
- `com.apple.AGXG17P`
- `com.apple.EXBrightKext`
- `com.apple.ExclaveKextClient`
- `com.apple.driver.AOPAudio2`
- `com.apple.driver.AppleAOP2`
- `com.apple.driver.AppleCS42L79Audio`
- `com.apple.driver.AppleEpochManager`
- `com.apple.driver.AppleIOPADMAStream`
- `com.apple.driver.AppleMobileDispH17P-DCP`
- `com.apple.driver.AppleT8103TypeCPhy`
- `com.apple.driver.AppleT8140`
- `com.apple.driver.AppleT8140ANEHAL`
- `com.apple.driver.AppleT8140CLPC`
- `com.apple.driver.AppleT8140MCC`
- `com.apple.driver.AppleT8140PCIe`
- `com.apple.driver.AppleT8140PMGR`
- `com.apple.driver.AppleThunderboltDPAdapterFamily`
- `com.apple.driver.AppleThunderboltDPInAdapter`
- `com.apple.driver.AppleThunderboltDPOutAdapter`
- `com.apple.driver.AppleThunderboltEDMSource`
- `com.apple.driver.AppleThunderboltIP`
- `com.apple.driver.AppleThunderboltNHI`
- `com.apple.driver.AppleThunderboltPCIDownAdapter`
- `com.apple.driver.AppleThunderboltPCIUpAdapter`
- `com.apple.driver.AppleThunderboltUSBDownAdapter`
- `com.apple.driver.AppleThunderboltUSBUpAdapter`
- `com.apple.driver.AppleTypeCPhyAUSBC`
- `com.apple.driver.AudioDMACLLTEscalationDetector-Stub`
- `com.apple.driver.AudioDMAController-T8140`
- `com.apple.driver.AudioDMAFamily`
- `com.apple.driver.AudioSharedDARTMapperProxy`
- `com.apple.driver.DMAChannelProxy`
- `com.apple.driver.EXDisplayPipeH17P`
- `com.apple.driver.ExclaveSEPManagerProxy`
- `com.apple.driver.IOPAudioAssetManagerDevice`
- `com.apple.driver.IOPAudioClientManagerDevice`
- `com.apple.driver.IOPAudioHapticsLEAPControlDevice`
- `com.apple.driver.IOPAudioIOBufferDevice`
- `com.apple.driver.IOPAudioIsolatedIOBufferDevice`
- `com.apple.driver.IOPAudioLEAPControlDevice`
- `com.apple.driver.IOPAudioLPMicDevice`
- `com.apple.driver.IOPAudioPCMAssetManagerDevice`
- `com.apple.driver.IOPAudioSpeaker`
- `com.apple.driver.IOPAudioVoiceTriggerDevice`
- `com.apple.driver.IOPEmbeddedAudio`
- `com.apple.driver.IOPHaptics`
- `com.apple.driver.SecureRTBuddyProxy`
- `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `com.apple.iokit.IOPAudioDriverFamily`
- `com.apple.kec.XrtHostedXnu`

#### ❌ Removed (13)

- `com.apple.AGXFirmwareKextG16PRTBuddy`
- `com.apple.AGXG16P`
- `com.apple.driver.AppleAOPAD5860`
- `com.apple.driver.AppleAOPVoiceTrigger`
- `com.apple.driver.AppleCS35L27Amp`
- `com.apple.driver.AppleCS42L77Audio`
- `com.apple.driver.AppleMCA2-T8130`
- `com.apple.driver.AppleMobileDispH16P-DCP`
- `com.apple.driver.AppleT8130`
- `com.apple.driver.AppleT8130CLPC`
- `com.apple.driver.AppleT8130PCIe`
- `com.apple.driver.AppleT8130PMGR`
- `com.apple.driver.AudioDMAController-T8130`

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.kernel`

```diff

 11215.40.48.0.0
-  __TEXT.__const: 0x33c60
+  __TEXT.__const: 0x38400
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x6bb5f
-  __TEXT.__os_log: 0x26bb5
+  __TEXT.__cstring: 0x70c45
+  __TEXT.__os_log: 0x26d4f
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x2c0
-  __DATA_CONST.__const: 0xa2420
+  __DATA_CONST.__mod_init_func: 0x2c8
+  __DATA_CONST.__const: 0xa5f70
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x13340
-  __DATA_CONST.__kalloc_var: 0x78f0
+  __DATA_CONST.__kalloc_type: 0x135c0
+  __DATA_CONST.__kalloc_var: 0x7c60
+  __DATA_CONST.__exclaves_bt: 0x60
   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7c64ec
+  __TEXT_EXEC.__text: 0x7f276c
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x2460
+  __KLDDATA.__const: 0x2520
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x18549
-  __DATA.__lock_grp: 0x57a8
-  __DATA.__percpu: 0x6e48
-  __DATA.__common: 0x58508
-  __DATA.__bss: 0x3f7c8
+  __DATA.__data: 0x185c9
+  __DATA.__lock_grp: 0x5908
+  __DATA.__percpu: 0x6e30
+  __DATA.__common: 0x58608
+  __DATA.__bss: 0x959a8
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x107b8
-  __BOOTDATA.__init: 0x5b058
+  __BOOTDATA.__init_entry_set: 0x10a58
+  __BOOTDATA.__init: 0x5b110
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __PLK_TEXT_EXEC.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x45557
-  Functions: 19828
+  Functions: 20350
   Symbols:   0
-  CStrings:  16801
+  CStrings:  17019
 
CStrings:
+ "\t\t%s 0x%016zx\n"
+ "\t\tAddress space ID: 0x%llx\n\t\tComponent:\n\t\t\tName: %s\n\t\t\tID: 0x%llx\n\t\t\tSelector: 0x%llx\n\t\tspace.component.endpoint.thread: %c%c%c%c.%c%c%c%c.%c%c%c%c.%c%c%c%c\n\t\tThread Context:\n\t\t\tAddress: 0x%zx\n\t\t\tTSS Base: 0x%zx\n\t\t\tIPC Buffer 0x%zx\n\t\t\tSCID 0x%zx\n\t\t\tECID: 0x%zx\n\t\t\tEPID: 0x%zx\n\t\t\tStack:\n\t\t\t\tStart: 0x%zx\n\t\t\t\tSize: 0x%zx\n\t\t\t\tCall base: 0x%zx\n\t\t\tRegisters:\n\t\t\t\tLR: 0x%zx\n\t\t\t\tPC: 0x%zx\n\t\t\t\tSP: 0x%zx\n\t\t\t\tCPSR: 0x%zx\n"
+ "!! Exclaves panic stackshot decode failed !!\n"
+ "\"TB_ASSERT: \" \"tb_lock_grp != NULL\" @%s:%d"
+ "%04x"
+ "%s %s:%s at PC: 0x%zx, LR: 0x%zx"
+ "%s id 0x%llx (irq index %d)\n"
+ "%s id 0x%llx (timer_id %u)\n"
+ "%s locked workloop\n"
+ "%s unlocked workloop\n"
+ "%s: IRQ %d register success!\n"
+ "%s: IRQ %d removed successfully\n"
+ "%s: IRQ %s success!\n"
+ "%s: attempt to activate stage 2 pmap %p @%s:%d"
+ "%s: attempt to nest stage 2 pmap %p @%s:%d"
+ "%s: invoked on stage 1 pmap %p @%s:%d"
+ "%s: timer %u %s success\n"
+ "%s: timer %u register success!\n"
+ "%s: timer %u removed successfully\n"
+ "%s: timer %u setTimeout completed (kr %d)\n"
+ "%s: timer %u setTimeout success\n"
+ "%s: unrecognized tlb operation: %d @%s:%d"
+ "** Exclaves panic stackshot found\n"
+ "** Exclaves panic stackshot not found\n"
+ "-restore"
+ "1121222222"
+ "12112211111121111111"
+ "21222211"
+ "222222222222222211"
+ "2222222222222222222122233a3212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121221"
+ "3B878185-AA62-4E1F-9DC9-D6799CBB6EBB"
+ "<< UNKNOWN OR INVALID CORE TYPE >>"
+ "AMX guest save state"
+ "B16@?0^v8"
+ "B16@?0^{?=[128c]^{?}^{?}}8"
+ "B16@?0^{exclaves_resource=[128c]IQAI^{ipc_port}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}BB(?={?=i^{tb_connection_s}^{task}[2Q]}{?=QIQ[256{?=*Q}]}{?=Q}{?={klist=^{knote}}}{?=QIQ[256{?=*Q}]I{sharedmemorybase_segxnuaccess_s=^{tb_connection_s}}})}8"
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQiBBB^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}^v^vI}8"
+ "B32@?0r^v8Q16^v24"
+ "BOOTED_EXCLAVEKIT"
+ "BOOTED_FAILURE"
+ "BOOTED_STAGE_2"
+ "BTI failure for 32-bit state? (ESR=0x%llx) @%s:%d"
+ "COMPLETE"
+ "Conclave Memory ledger doesn't recognize pagekind @%s:%d"
+ "Conclave string for the task"
+ "Conclave tainted task %p terminated\n @%s:%d"
+ "E-core"
+ "EXCLAVES_PANIC_WAIT_THREAD"
+ "Exclaves additional info: STATUS: %s\n"
+ "Exclaves backtrace:\n"
+ "Exclaves boot status: %s\n"
+ "Exclaves inspection thread tried to wait\n @%s:%d"
+ "Exclaves logging: Disabled by boot argument\n"
+ "Exclaves logging: Disabled. Failed to start retrieval thread (error: %d)\n"
+ "Exclaves logging: Enabled\n"
+ "Exclaves panic thread woken up @%s:%d"
+ "Exclaves requirements which have been relaxed"
+ "Exclaves stage2 boot failed @%s:%d"
+ "Exclaves upcall early init failed @%s:%d"
+ "Failed to allocate AMX state for thread %p @%s:%d"
+ "Failed to allocate SME state for thread %p @%s:%d"
+ "Failed to copy instruction from PA %p inside wired page @%s:%d"
+ "Failed to create log server endpoint\n"
+ "Failed to find mapping for VA %p inside wired page @%s:%d"
+ "Failed to initialize config client (error: %d)\n"
+ "Failed to initialize log consumer (error: %d)\n"
+ "Failed to retrieve logs (error: %d). Exiting.\n"
+ "Failed to set exclaves trace mode (error: %d)\n"
+ "Hypervisor info"
+ "I16@?0Q8"
+ "I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8"
+ "I16@?0{xnuupcalls_xnuupcalls_ane_setpowerstate__result_s=C(?=IB)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_ane_workbegin__result_s=C(?=IB)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_ane_workend__result_s=C(?=IB)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_ane_worksubmit__result_s=C(?=IB)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_async_notification_signal__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_close__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_conclave_crash_info__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_conclave_stop__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_irq_disable__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_irq_enable__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_irq_register__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_irq_remove__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_lock_wl__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_mapper_activate__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_mapper_deactivate__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_notification_signal__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_read__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_readdir__result_s=C(?=II)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_remove__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_sealstate__result_s=C(?=IB)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_sync__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_timer_cancel_timeout__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_timer_disable__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_timer_enable__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_timer_register__result_s=C(?=II)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_timer_remove__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_timer_set_timeout__result_s=C(?=IB)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_unlock_wl__result_s=C(?=I)}8"
+ "I16@?0{xnuupcalls_xnuupcalls_write__result_s=C(?=I)}8"
+ "I20@?0I8@?<I@?{xnuupcalls_xnuupcalls_conclave_stop__result_s=C(?=I)}>12"
+ "I20@?0I8@?<I@?{xnuupcalls_xnuupcalls_conclave_suspend__result_s=C(?=I{xnuupcalls_conclavescidlist_s=[32Q]})}>12"
+ "I20@?0I8@?<I@?{xnuupcalls_xnuupcalls_sealstate__result_s=C(?=IB)}>12"
+ "I24@?0I8I12@?<I@?{xnuupcalls_pagelist_s=[64I]}>16"
+ "I24@?0Q8@?<I@?Q>16"
+ "I24@?0Q8@?<I@?{xnuupcalls_xnuupcalls_lock_wl__result_s=C(?=I)}>16"
+ "I24@?0Q8@?<I@?{xnuupcalls_xnuupcalls_timer_register__result_s=C(?=II)}>16"
+ "I24@?0Q8@?<I@?{xnuupcalls_xnuupcalls_unlock_wl__result_s=C(?=I)}>16"
+ "I24@?0[16C]8@?<I@?Q>16"
+ "I24@?0[32C]8@?<I@?{xnuupcalls_xnuupcalls_root__result_s=C(?=IQ)}>16"
+ "I24@?0{xnuupcalls_xnuupcalls_create__result_s=C(?=IQ)}8"
+ "I24@?0{xnuupcalls_xnuupcalls_getsize__result_s=C(?=IQ)}8"
+ "I24@?0{xnuupcalls_xnuupcalls_open__result_s=C(?=IQ)}8"
+ "I24@?0{xnuupcalls_xnuupcalls_root__result_s=C(?=IQ)}8"
+ "I264@?0{xnuupcalls_pagelist_s=[64I]}8"
+ "I272@?0{xnuupcalls_xnuupcalls_conclave_suspend__result_s=C(?=I{xnuupcalls_conclavescidlist_s=[32Q]})}8"
+ "I28@?0I8Q12@?<I@?{xnuupcalls_xnuupcalls_close__result_s=C(?=I)}>20"
+ "I28@?0I8Q12@?<I@?{xnuupcalls_xnuupcalls_getsize__result_s=C(?=IQ)}>20"
+ "I28@?0Q8I16@?<I@?Q>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_ane_setpowerstate__result_s=C(?=IB)}>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_async_notification_signal__result_s=C(?=I)}>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_mapper_activate__result_s=C(?=I)}>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_mapper_deactivate__result_s=C(?=I)}>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_notification_signal__result_s=C(?=I)}>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_timer_cancel_timeout__result_s=C(?=I)}>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_timer_disable__result_s=C(?=I)}>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_timer_enable__result_s=C(?=I)}>20"
+ "I28@?0Q8I16@?<I@?{xnuupcalls_xnuupcalls_timer_remove__result_s=C(?=I)}>20"
+ "I28@?0Q8i16@?<I@?{xnuupcalls_xnuupcalls_irq_disable__result_s=C(?=I)}>20"
+ "I28@?0Q8i16@?<I@?{xnuupcalls_xnuupcalls_irq_enable__result_s=C(?=I)}>20"
+ "I28@?0Q8i16@?<I@?{xnuupcalls_xnuupcalls_irq_register__result_s=C(?=I)}>20"
+ "I28@?0Q8i16@?<I@?{xnuupcalls_xnuupcalls_irq_remove__result_s=C(?=I)}>20"
+ "I28@?0r^{xnuupcalls_conclavesharedbuffer_s=[2Q]}8I16@?<I@?{xnuupcalls_xnuupcalls_conclave_crash_info__result_s=C(?=I)}>20"
+ "I32@?0I8I12Q16@?<I@?{xnuupcalls_xnuupcalls_sync__result_s=C(?=I)}>24"
+ "I32@?0Q8Q16@?<I@?{xnuupcalls_xnuupcalls_ane_workend__result_s=C(?=IB)}>24"
+ "I32@?0[64I]8I16I20@?<I@?>24"
+ "I36@?0I8Q12[256C]20@?<I@?{xnuupcalls_xnuupcalls_create__result_s=C(?=IQ)}>28"
+ "I36@?0I8Q12[256C]20@?<I@?{xnuupcalls_xnuupcalls_open__result_s=C(?=IQ)}>28"
+ "I36@?0I8Q12[256C]20@?<I@?{xnuupcalls_xnuupcalls_remove__result_s=C(?=I)}>28"
+ "I36@?0I8Q12r^{xnuupcalls_iodesc_s=QQQ}20@?<I@?{xnuupcalls_xnuupcalls_read__result_s=C(?=I)}>28"
+ "I36@?0I8Q12r^{xnuupcalls_iodesc_s=QQQ}20@?<I@?{xnuupcalls_xnuupcalls_write__result_s=C(?=I)}>28"
+ "I36@?0Q8I16r^{xnuupcalls_drivertimerspecification_s=III}20@?<I@?{xnuupcalls_xnuupcalls_timer_set_timeout__result_s=C(?=IB)}>28"
+ "I40@?0I8Q12Q20I28@?<I@?{xnuupcalls_xnuupcalls_readdir__result_s=C(?=II)}>32"
+ "I40@?0Q8Q16Q24@?<I@?{xnuupcalls_xnuupcalls_ane_workbegin__result_s=C(?=IB)}>32"
+ "I44@?0Q8Q16I24Q28@?<I@?{xnuupcalls_xnuupcalls_ane_worksubmit__result_s=C(?=IB)}>36"
+ "I8@?0"
+ "IKOT_EXCLAVES_RESOURCE"
+ "IKOT_HYPERVISOR"
+ "IOExclaveLockWorkloop"
+ "IOExclaveProxyStateWrapper"
+ "Kernel BTI failure (BTYPE=0x%04x)"
+ "Ledger credit failed. count %u error code %d @%s:%d"
+ "Ledger debit failed. count %u error code %d @%s:%d"
+ "Maximum size allowed for 16K-page guest IPA spaces"
+ "Maximum size allowed for 4K-page guest IPA spaces"
+ "NOT_DEFINED"
+ "NOT_STARTED"
+ "NOT_SUPPORTED"
+ "P-core"
+ "PARTIAL"
+ "SME exception from kernel, state=%p, esr=%#llx @%s:%d"
+ "SME saved state"
+ "TB_ASSERT: (address__v_decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotTypes.Address (aka. UInt64)\" @%s:%d"
+ "TB_ASSERT: (cmp.encoded) && \"completion block must be called before returning\" @%s:%d"
+ "TB_ASSERT: (conclave_launcher_conclavelauncherfailure__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: conclave_launcher.ConclaveLauncherFailure\" @%s:%d"
+ "TB_ASSERT: (conclave_launcher_conclavestatus__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: conclave_launcher.ConclaveStatus\" @%s:%d"
+ "TB_ASSERT: (err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \"unexpected tb_error_t returned\" @%s:%d"
+ "TB_ASSERT: (err == TB_ERROR_SUCCESS) && \"failed to wrap packed buffer\" @%s:%d"
+ "TB_ASSERT: (framemint_frameminterror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: FrameMint.FrameMintError\" @%s:%d"
+ "TB_ASSERT: (oslogdarwin_logstreamtype__decode(message, &val->values.Log.stream) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogDarwin.LogStreamType\" @%s:%d"
+ "TB_ASSERT: (oslogdarwin_logstreamtype__decode(message, &val->values.Signpost.stream) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogDarwin.LogStreamType\" @%s:%d"
+ "TB_ASSERT: (oslogdarwin_logtype__decode(message, &val->values.Log.type) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogDarwin.LogType\" @%s:%d"
+ "TB_ASSERT: (oslogdarwin_redactedlogdata__decode(msg, &item) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogDarwin.RedactedLogData\" @%s:%d"
+ "TB_ASSERT: (oslogdarwin_signpostscope__decode(message, &val->values.Signpost.scope) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogDarwin.SignpostScope\" @%s:%d"
+ "TB_ASSERT: (oslogdarwin_signposttype__decode(message, &val->values.Signpost.type) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogDarwin.SignpostType\" @%s:%d"
+ "TB_ASSERT: (physicaladdress__v_decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.PhysicalAddress (aka. UInt64)\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from ane_setpowerstate\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from ane_workbegin\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from ane_workend\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from ane_worksubmit\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from async_notification_signal\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from close\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from conclave_crash_info\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from conclave_stop\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from conclave_suspend\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from create\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getsize\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from irq_disable\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from irq_enable\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from irq_register\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from irq_remove\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from lock_wl\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mapper_activate\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mapper_deactivate\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from notification_signal\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from open\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from read\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from readdir\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from remove\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from root\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from sealstate\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from sync\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from timer_cancel_timeout\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from timer_disable\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from timer_enable\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from timer_register\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from timer_remove\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from timer_set_timeout\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from unlock_wl\" @%s:%d"
+ "TB_ASSERT: (result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from write\" @%s:%d"
+ "TB_ASSERT: (server->alloc != NULL) && \"implementation for alloc is not present\" @%s:%d"
+ "TB_ASSERT: (server->ane_setpowerstate != NULL) && \"implementation for ane_setpowerstate is not present\" @%s:%d"
+ "TB_ASSERT: (server->ane_workbegin != NULL) && \"implementation for ane_workbegin is not present\" @%s:%d"
+ "TB_ASSERT: (server->ane_workend != NULL) && \"implementation for ane_workend is not present\" @%s:%d"
+ "TB_ASSERT: (server->ane_worksubmit != NULL) && \"implementation for ane_worksubmit is not present\" @%s:%d"
+ "TB_ASSERT: (server->async_notification_signal != NULL) && \"implementation for async_notification_signal is not present\" @%s:%d"
+ "TB_ASSERT: (server->close != NULL) && \"implementation for close is not present\" @%s:%d"
+ "TB_ASSERT: (server->conclave_crash_info != NULL) && \"implementation for conclave_crash_info is not present\" @%s:%d"
+ "TB_ASSERT: (server->conclave_stop != NULL) && \"implementation for conclave_stop is not present\" @%s:%d"
+ "TB_ASSERT: (server->conclave_suspend != NULL) && \"implementation for conclave_suspend is not present\" @%s:%d"
+ "TB_ASSERT: (server->create != NULL) && \"implementation for create is not present\" @%s:%d"
+ "TB_ASSERT: (server->exfil_closechannel != NULL) && \"implementation for exfil_closechannel is not present\" @%s:%d"
+ "TB_ASSERT: (server->exfil_data != NULL) && \"implementation for exfil_data is not present\" @%s:%d"
+ "TB_ASSERT: (server->exfil_newchannel != NULL) && \"implementation for exfil_newchannel is not present\" @%s:%d"
+ "TB_ASSERT: (server->free != NULL) && \"implementation for free is not present\" @%s:%d"
+ "TB_ASSERT: (server->getsize != NULL) && \"implementation for getsize is not present\" @%s:%d"
+ "TB_ASSERT: (server->helloupcall != NULL) && \"implementation for HelloUpcall is not present\" @%s:%d"
+ "TB_ASSERT: (server->irq_disable != NULL) && \"implementation for irq_disable is not present\" @%s:%d"
+ "TB_ASSERT: (server->irq_enable != NULL) && \"implementation for irq_enable is not present\" @%s:%d"
+ "TB_ASSERT: (server->irq_register != NULL) && \"implementation for irq_register is not present\" @%s:%d"
+ "TB_ASSERT: (server->irq_remove != NULL) && \"implementation for irq_remove is not present\" @%s:%d"
+ "TB_ASSERT: (server->lock_wl != NULL) && \"implementation for lock_wl is not present\" @%s:%d"
+ "TB_ASSERT: (server->mapper_activate != NULL) && \"implementation for mapper_activate is not present\" @%s:%d"
+ "TB_ASSERT: (server->mapper_deactivate != NULL) && \"implementation for mapper_deactivate is not present\" @%s:%d"
+ "TB_ASSERT: (server->notification_signal != NULL) && \"implementation for notification_signal is not present\" @%s:%d"
+ "TB_ASSERT: (server->open != NULL) && \"implementation for open is not present\" @%s:%d"
+ "TB_ASSERT: (server->read != NULL) && \"implementation for read is not present\" @%s:%d"
+ "TB_ASSERT: (server->readdir != NULL) && \"implementation for readdir is not present\" @%s:%d"
+ "TB_ASSERT: (server->remove != NULL) && \"implementation for remove is not present\" @%s:%d"
+ "TB_ASSERT: (server->root != NULL) && \"implementation for root is not present\" @%s:%d"
+ "TB_ASSERT: (server->sealstate != NULL) && \"implementation for sealstate is not present\" @%s:%d"
+ "TB_ASSERT: (server->sync != NULL) && \"implementation for sync is not present\" @%s:%d"
+ "TB_ASSERT: (server->timer_cancel_timeout != NULL) && \"implementation for timer_cancel_timeout is not present\" @%s:%d"
+ "TB_ASSERT: (server->timer_disable != NULL) && \"implementation for timer_disable is not present\" @%s:%d"
+ "TB_ASSERT: (server->timer_enable != NULL) && \"implementation for timer_enable is not present\" @%s:%d"
+ "TB_ASSERT: (server->timer_register != NULL) && \"implementation for timer_register is not present\" @%s:%d"
+ "TB_ASSERT: (server->timer_remove != NULL) && \"implementation for timer_remove is not present\" @%s:%d"
+ "TB_ASSERT: (server->timer_set_timeout != NULL) && \"implementation for timer_set_timeout is not present\" @%s:%d"
+ "TB_ASSERT: (server->unlock_wl != NULL) && \"implementation for unlock_wl is not present\" @%s:%d"
+ "TB_ASSERT: (server->write != NULL) && \"implementation for write is not present\" @%s:%d"
+ "TB_ASSERT: (sharedmemorybase_accesserror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.AccessError\" @%s:%d"
+ "TB_ASSERT: (sharedmemorybase_mappingresult__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.MappingResult\" @%s:%d"
+ "TB_ASSERT: (sharedmemorybase_perms__decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.Perms\" @%s:%d"
+ "TB_ASSERT: (stackshottypes_addressspace__decode(msg, &item) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotTypes.AddressSpace\" @%s:%d"
+ "TB_ASSERT: (stackshottypes_ipcstackentry__v_decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotTypes.IPCStackEntry\" @%s:%d"
+ "TB_ASSERT: (stackshottypes_textlayout__decode(msg, &item) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotTypes.TextLayout\" @%s:%d"
+ "TB_ASSERT: (vErr == TB_ERROR_SUCCESS) && \"tb_message_subrange failed\" @%s:%d"
+ "TB_ASSERT: (xnuproxy_namedbuffererror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: XnuProxy.NamedBufferError\" @%s:%d"
+ "TB_ASSERT: (xnuproxy_namedbufferrange__v_decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: XnuProxy.NamedBufferRange\" @%s:%d"
+ "TB_ASSERT: (xnuproxy_namedbufferstatus__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: XnuProxy.NamedBufferStatus\" @%s:%d"
+ "TB_ASSERT: (xnuproxy_resourceinfo__decode(msg, &item) == TB_ERROR_SUCCESS) && \"failed to decode type: XnuProxy.ResourceInfo\" @%s:%d"
+ "TB_ASSERT: (xnuupcalls_drivertimerspecification__decode(msg, &duration) == TB_ERROR_SUCCESS) && \"failed to decode type: XnuUpcalls.DriverTimerSpecification\" @%s:%d"
+ "TB_ASSERT: (xnuupcalls_pagekind__decode(msg, &kind) == TB_ERROR_SUCCESS) && \"failed to decode type: XnuUpcalls.PageKind\" @%s:%d"
+ "TB_ASSERT: (xnuupcalls_syncop__decode(msg, &op) == TB_ERROR_SUCCESS) && \"failed to decode type: XnuUpcalls.SyncOp\" @%s:%d"
+ "TB_FATAL: invalid tag in array metadata: 0x%x @%s:%d"
+ "TB_FATAL: unrecognized selector: %llu @%s:%d"
+ "Task %p trying to detach a conclave %p but it is in a weird state @%s:%d"
+ "Task could not be tainted by talking to conclaves"
+ "Unexpected host abort from guest context"
+ "Unexpected non-kernel BTI failure? (ESR=0x%llx) @%s:%d"
+ "Unexpected ringgate panic status @%s:%d"
+ "Unexpected wait for panic result: %d @%s:%d"
+ "Unexpected wait result from esync_wait: %d @%s:%d"
+ "Unhandled AppleH16 implementation specific error. state=%p esr=%#llx far=%p core_type=\"%s\" dpc_err_sts:%p\n\tlsu_err_sts:%p, fed_err_sts:%p, mmu_err_sts:%p\n\tllc_err_sts:%p, llc_err_adr:%p, llc_err_inf:%p\n"
+ "Unknown exclaves interruptibility: %llu @%s:%d"
+ "Unrecognized guest trap exception, state=%p, esr=%#llx @%s:%d"
+ "Unsupported redacted Exclaves log type %llu @%s:%d"
+ "[Exclaves]"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[32c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "attempt to re-enter exclaves @%s:%d"
+ "bad exclaves privilege (%u) @%s:%d"
+ "com.apple.darwin"
+ "com.apple.named_buffer.6"
+ "com.apple.private.exclaves.boot"
+ "com.apple.private.exclaves.conclave-host"
+ "com.apple.private.exclaves.conclave-spawn"
+ "com.apple.private.exclaves.kernel-domain"
+ "com.apple.private.hypervisor"
+ "com.apple.private.hypervisor.vmapple"
+ "com.apple.private.vfs.exclave-fs-register"
+ "com.apple.private.virtualization"
+ "com.apple.security.hypervisor"
+ "com.apple.service.ExclaveIndicatorController"
+ "com.apple.service.FrameMint"
+ "com.apple.service.LogServer_xnuproxy"
+ "com.apple.service.Stackshot"
+ "com.apple.sharedmem.stackshotserver"
+ "com.apple.storage.backend"
+ "com.apple.xnu.oslog"
+ "enable_sme"
+ "epoch_sync.c"
+ "exclaveEnableInterrupt"
+ "exclaveEnableTimer"
+ "exclaveInterruptOccurred"
+ "exclaveRegisterInterrupt"
+ "exclaveRegisterTimer"
+ "exclaveRemoveInterrupt"
+ "exclaveRemoveTimer"
+ "exclaveTimerCancelTimeout"
+ "exclaveTimerFired"
+ "exclaveTimerSetTimeout"
+ "exclaves stackshot: buffer size overflow @%s:%d"
+ "exclaves stackshot: cannot allocate buffer for exclaves shared memory addresses @%s:%d"
+ "exclaves stackshot: failed to allocate collect ipcb: %d @%s:%d"
+ "exclaves-config"
+ "exclaves-logs"
+ "exclaves-stackshot"
+ "exclaves.c"
+ "exclaves.tightbeam.c"
+ "exclaves: boot task failed: %s (%p) @%s:%d"
+ "exclaves: requirement failed: exclaves indicator controller not found @%s:%d"
+ "exclaves: requirement failed: failed to boot to exclavekit @%s:%d"
+ "exclaves: requirement failed: failed to find conclave manager (%s) @%s:%d"
+ "exclaves: requirement failed: failed to populate frame mint @%s:%d"
+ "exclaves: requirement failed: log server not found @%s:%d"
+ "exclaves: requirement failed: no conclave manager present @%s:%d"
+ "exclaves: requirement failed: stackshot server not found @%s:%d"
+ "exclaves_boot.c"
+ "exclaves_exfiltration.h"
+ "exclaves_inspection.c"
+ "exclaves_inspection_init"
+ "exclaves_log.c"
+ "exclaves_memory.c"
+ "exclaves_oslog_init"
+ "exclaves_panic.c"
+ "exclaves_relaxed_requirements"
+ "exclaves_resource.c"
+ "exclaves_sensor.c"
+ "exclaves_sensor_init"
+ "exclaves_storage_init"
+ "hv"
+ "hv_disable"
+ "hv_support"
+ "hv_support_init"
+ "hv_vcpu.c"
+ "hv_vm_t.hv_vm_percpu_t"
+ "i20@?0Q8I16"
+ "ipa_size_16k"
+ "ipa_size_4k"
+ "kern_stackshot.c"
+ "log,%s,%0x"
+ "max_address_spaces"
+ "npages @%s:%d"
+ "pmap_flush_tlb_stage2_internal"
+ "pmap_gva_to_ipa_internal"
+ "pmap_stage1_tlb_op_internal"
+ "recovery"
+ "setActive"
+ "signpost,%s,%0x,%0x,%u,%u"
+ "site.IOExclaveProxyState"
+ "site.IOExclaveProxyStateWrapper"
+ "site.IOExclaveWorkLoopAperture"
+ "site.esync_t"
+ "site.exclave_fs_base_dir_t"
+ "site.exclaves_ctx_t"
+ "site.exclaves_resource_domain_t"
+ "site.exclaves_resource_t"
+ "site.queue_head_t"
+ "site.registered_fs_tag_t"
+ "site.table_item_t"
+ "site.table_t"
+ "site.uint8_t*"
+ "stackshot: trying to inspect already-queued thread @%s:%d"
+ "task_conclave"
+ "task_conclave_untaintable"
+ "task_crash_info_conclave_upcall: cannot allocate buffer for task_info shared memory @%s:%d"
+ "thread %p already has SME saved state %p @%s:%d"
+ "tightbeam"
+ "unexpected exfiltration upcall: closechannel @%s:%d"
+ "unexpected exfiltration upcall: data @%s:%d"
+ "unexpected exfiltration upcall: newchannel @%s:%d"
+ "unknown boot status: %u @%s:%d"
+ "unknown epoch sync space @%s:%d"
+ "unknown sensor status @%s:%d"
+ "v10@?0{framemint_framemint_populate__result_s=C(?=C)}8"
+ "v128@?0{stackshot_stackshotresult_s={stackshot_stackshotentry_v_s=C(?={?=^{stackshot_stackshotentry_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}{stackshottypes_textlayout_v_s=C(?={?=^{stackshottypes_textlayout_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}{stackshottypes_addressspace_v_s=C(?={?=^{stackshottypes_addressspace_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}8"
+ "v144@?0{sharedmemorybase_segxnuaccess_createxnumapping__result_s=C(?=I{sharedmemorybase_mappingresult_s={sharedmemorybase_mappinginfo_s=ICCB{sharedmemorybase_pagerange_v_s=C(?={?=^{sharedmemorybase_pagerange_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}{sharedmemorybase_pagerange_v_s=C(?={?=^{sharedmemorybase_pagerange_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}{sharedmemorybase_pagerange_v_s=C(?={?=^{sharedmemorybase_pagerange_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}8"
+ "v16@?0Q8"
+ "v16@?0{conclave_launcher_conclavecontrol_launch__result_s=C(?=II)}8"
+ "v16@?0{conclave_launcher_conclavecontrol_stop__result_s=C(?=II)}8"
+ "v16@?0{sharedmemorybase_segaccessbase_mappingdestroy__result_s=C(?=I)}8"
+ "v16@?0{xnuproxy_cmd_audiobuffercopyout__result_s=C(?=I)}8"
+ "v20@?0Q8C16"
+ "v20@?0{xnuproxy_cmd_audiobufferdelete__result_s=C(?={xnuproxy_namedbuffererror_s=II})}8"
+ "v20@?0{xnuproxy_cmd_audiobuffermap__result_s=C(?={xnuproxy_namedbuffererror_s=II}{xnuproxy_mapinfo_s=B})}8"
+ "v20@?0{xnuproxy_cmd_namedbufferdelete__result_s=C(?={xnuproxy_namedbuffererror_s=II})}8"
+ "v20@?0{xnuproxy_cmd_namedbuffermap__result_s=C(?={xnuproxy_namedbuffererror_s=II}{xnuproxy_mapinfo_s=B})}8"
+ "v24@?0Q8Q16"
+ "v24@?0Q8r^{oslogdarwin_redactedlogdata_s=Q(?={?=CQCI[16C]}{?=CQCCII[16C]}{?=QS})}16"
+ "v24@?0Q8r^{stackshot_stackshotentry_s=Q{stackshottypes_ipcstackentry_v__opt_s=B{stackshottypes_ipcstackentry_v_s=C(?={?=^{stackshottypes_ipcstackentry_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}16"
+ "v24@?0Q8r^{stackshottypes_addressspace_s=Q{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}Q{address__opt_s=BQ}{asroot__opt_s=BQ}}16"
+ "v24@?0Q8r^{stackshottypes_ipcstackentry_s=QQ{tbinvocationid__opt_s=BQ}{ecstate__opt_s=BQ}{address_v__opt_s=B{address_v_s=C(?={?=^QQ@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}16"
+ "v24@?0Q8r^{stackshottypes_textlayout_s=Q{stackshottypes_textsegment_v_s=C(?={?=^{stackshottypes_textsegment_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}16"
+ "v24@?0Q8r^{stackshottypes_textsegment_s=[16C]Q{address__opt_s=BQ}}16"
+ "v24@?0Q8r^{xnuproxy_namedbufferrange_s=QI}16"
+ "v24@?0Q8r^{xnuproxy_resourceinfo_s={char_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}{char_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}IQB}16"
+ "v24@?0{xnuproxy_ipccontext_s=QQ}8"
+ "v24@?0{xnuproxy_panicinfo_s=QQ}8"
+ "v40@?0r*8r*16I24Q28B36"
+ "v432@?0{xnuproxy_bootinfo_s=QIQQQ[370C]Q}8"
+ "v48@?0{oslogdarwin_redactedlogdata_v_s=C(?={?=^{oslogdarwin_redactedlogdata_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8"
+ "v48@?0{stackshot_sharedbuffer_s={u64_v_s=C(?={?=^QQ@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}8"
+ "v48@?0{xnuproxy_resourceinfo_v_s=C(?={?=^{xnuproxy_resourceinfo_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8"
+ "v56@?0{sharedmemorybase_segaccessbase_mappinggetphysicaladdresses__result_s=C(?=I{physicaladdress_v_s=C(?={?=^QQ@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}8"
+ "v56@?0{xnuproxy_cmd_audiobufferlayout__result_s=C(?={xnuproxy_namedbuffererror_s=II}{xnuproxy_namedbufferrange_v_s=C(?={?=^{xnuproxy_namedbufferrange_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}8"
+ "v56@?0{xnuproxy_cmd_namedbufferlayout__result_s=C(?={xnuproxy_namedbuffererror_s=II}{xnuproxy_namedbufferrange_v_s=C(?={?=^{xnuproxy_namedbufferrange_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}8"
+ "v96@?0{sharedmemorybase_accessstatus_s={sharedmemorybase_status_s={sharedmemorybase_parameters_s=QCQCC{sharedmemorybase_perms__opt_s=BC}}Q{sharedmemorybase_pagerange_v_s=C(?={?=^{sharedmemorybase_pagerange_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}CB}8"
+ "vm_fault() KERN_FAILURE from guest fault on state %p @%s:%d"
- " (AMX Uncorrected)"
- " (Bus error)"
- " (Decode error)"
- " (Non-recoverable Uncorrected)"
- " (Normal completion)"
- " (Recoverable Uncorrected)"
- " (Reserved)"
- " (Slave error)"
- " (UNKNOWN)"
- " (Unavailable)"
- " (addr map hole/size mis-match)"
- " (bad cmd)"
- " (bad mask)"
- " (bad size)"
- "%s err (%s) %son %c-core: FAR=%#llx %s_ERR_STS=%#llx err_sts: (%s) @%s:%d"
- "%s: insufficient number of ASIDs (%u) supplied by SPTM @%s:%d"
- "(PIO offset from this cluster: %#llx, info=%#llx AFID=%#llx%s)"
- "(info=%#llx%s) "
- "(multiple errors) "
- "(set %u way %u) "
- "(va=%#llx) "
- "(va=0x%#llx) "
- ", multiple errors"
- "A PIO-read or write attempt to a locked system register"
- "ACC_BIUAFI_CMD_ACKE: Acknowledge Exclusive - ack for CTOE or CTOECOND, goto M/E state"
- "ACC_BIUAFI_CMD_ACKI: Ack for CDROP, CCLEANINV, or CTOECOND"
- "ACC_BIUAFI_CMD_ACKIRSP_C: AckIRsp_C cmd"
- "ACC_BIUAFI_CMD_ACKIRSP_D: AckIRsp_D cmd"
- "ACC_BIUAFI_CMD_ACKM: Acknowledge Modified - ack for CTOE or CTOECOND, goto M state"
- "ACC_BIUAFI_CMD_ACKOP: Acknowledge response to CMaint command"
- "ACC_BIUAFI_CMD_BZERO_RO: Write all zeroes, allocate into M$ but not L2"
- "ACC_BIUAFI_CMD_CCLEANINV: Maintenance operation used for inter-processor D$ clean and invalidate operation"
- "ACC_BIUAFI_CMD_CDROP: Coherent Drop"
- "ACC_BIUAFI_CMD_CMAINT: Maintenance operation used for TLB operations, and barriers between coherent agents"
- "ACC_BIUAFI_CMD_CPBKI: Copyback request with final state being Invalid"
- "ACC_BIUAFI_CMD_CPBKNC: Copyback request if an agent requests a non-coherent copy of the line"
- "ACC_BIUAFI_CMD_CPBKRSP_C: Copyback response to CPBKNC, CPBKI/CPBKS (while in E/S state) or CPBKS (while in M/O state)"
- "ACC_BIUAFI_CMD_CPBKRSP_D: Copyback response to CPBKI (while in M/O state)"
- "ACC_BIUAFI_CMD_CPBKS: Copyback request if another coherent agent requests a copy of the line in non-exclusive mode"
- "ACC_BIUAFI_CMD_CPFWI: CpFwI cmd"
- "ACC_BIUAFI_CMD_CPFWS: CpFwS cmd"
- "ACC_BIUAFI_CMD_CRD: Coherent Read"
- "ACC_BIUAFI_CMD_CRDS: Coherent Read Exclusive"
- "ACC_BIUAFI_CMD_CRDS: Coherent Read Shared"
- "ACC_BIUAFI_CMD_CTOE: Change to Exclusive"
- "ACC_BIUAFI_CMD_CTOECOND: Change to Exclusive for a STREX"
- "ACC_BIUAFI_CMD_CTOIBK: CtoIBk cmd"
- "ACC_BIUAFI_CMD_CTOIFW: CtoIFw cmd"
- "ACC_BIUAFI_CMD_CWRBK_C: CWrBk_C cmd"
- "ACC_BIUAFI_CMD_CWRBK_D: CWrBk_D cmd"
- "ACC_BIUAFI_CMD_DATAV: Victim or Write-Back data"
- "ACC_BIUAFI_CMD_FILLE: Fill Data in Exclusive State"
- "ACC_BIUAFI_CMD_FILLM: Fill Data in Modified State"
- "ACC_BIUAFI_CMD_FILLO: Fill Data in Owned State"
- "ACC_BIUAFI_CMD_FILLP: FillP cmd"
- "ACC_BIUAFI_CMD_FILLS: Fill Data in Shared State"
- "ACC_BIUAFI_CMD_NCRDINCRRSP_DO: Resp to Non-Coherent Read Increment Device Ordered"
- "ACC_BIUAFI_CMD_NCRDINCRRSP_RO: Resp to Non-Coherent Read Increment Relaxed Ordered"
- "ACC_BIUAFI_CMD_NCRDINCR_DO: Non-Coherent Read Increment Device Ordered"
- "ACC_BIUAFI_CMD_NCRDINCR_RO: Non-Coherent Read Increment Relaxed Ordered"
- "ACC_BIUAFI_CMD_NCWRINCR_DO: Non-Coherent Write Increment Device Ordered"
- "ACC_BIUAFI_CMD_NCWRINCR_RO: Non-Coherent Write Increment Relaxed Ordered"
- "ACC_BIUAFI_CMD_NCWRRSP_DO: Resp to Non-Coherent Write Increment Device Ordered"
- "ACC_BIUAFI_CMD_NCWRRSP_RO: Resp to Non-Coherent Write Increment Relaxed Ordered"
- "ACC_BIUAFI_CMD_NOP: NOP cmd"
- "ACC_BIUAFI_CMD_PULLV: Pull victim data"
- "ACC_CIFL2C_CMD_DCZVA: DC-ZVA"
- "ACC_CIFL2C_CMD_MNT_OP: IC maint op, TLB maint op, DSB, SEV"
- "ACC_CIFL2C_CMD_MVA_OP: MVA clean and invalidate"
- "ACC_CIFL2C_CMD_NCWR: NC Write"
- "ACC_CIFL2C_CMD_RD_ISTRM: request for istream miss"
- "ACC_CIFL2C_CMD_RD_LD: request for load miss in E or S state"
- "ACC_CIFL2C_CMD_RD_LD_M: request for load miss in E state w/ intent to modify"
- "ACC_CIFL2C_CMD_RD_LD_M_PRE: request for L1D hardware prefetch (store version)"
- "ACC_CIFL2C_CMD_RD_LD_PRE: request for L1D hardware prefetch (load version)"
- "ACC_CIFL2C_CMD_RD_MMU: request for MMU miss"
- "ACC_CIFL2C_CMD_RD_PLI: Pre-fetch to LLC only"
- "ACC_CIFL2C_CMD_RD_ST_COND : store upgrade conditional"
- "ACC_CIFL2C_CMD_RD_ST_UP: request for store upgrade"
- "ACC_CIFL2C_CMD_SW_OP: Set Way ops"
- "ACC_STS: ADCLK lose lock"
- "ACC_STS: incomplete epoch sync"
- "ACC_STS: timebase going backward"
- "ATOMIC_OR_EXCLUSIVE_FAIL"
- "ATOMIC_OR_EXCLUSIVE_SUCC"
- "All CPU-Cores are powered down and AMX has a valid context"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQiBBB^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]QCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}}8"
- "BRANCH_CALL_INDIR_MISPRED_NONSPEC"
- "BRANCH_COND_MISPRED_NONSPEC"
- "BRANCH_INDIR_MISPRED_NONSPEC"
- "BRANCH_MISPRED_NONSPEC"
- "BRANCH_RET_INDIR_MISPRED_NONSPEC"
- "BTI exception telemetry runtime init"
- "Bus"
- "CORE_ACTIVE_CYCLE"
- "CPU%d failed to shut down @%s:%d"
- "DPC"
- "FED"
- "FETCH_RESTART"
- "FLUSH_RESTART_OTHER_NONSPEC"
- "Failed to get memory error port - mcc"
- "INST_ALL"
- "INST_BARRIER"
- "INST_BRANCH"
- "INST_BRANCH_CALL"
- "INST_BRANCH_COND"
- "INST_BRANCH_INDIR"
- "INST_BRANCH_RET"
- "INST_BRANCH_TAKEN"
- "INST_INT_ALU"
- "INST_INT_LD"
- "INST_INT_ST"
- "INST_LDST"
- "INST_SIMD_ALU"
- "INST_SIMD_LD"
- "INST_SIMD_ST"
- "INTERRUPT_PENDING"
- "L1D_CACHE_MISS_LD"
- "L1D_CACHE_MISS_LD_NONSPEC"
- "L1D_CACHE_MISS_ST"
- "L1D_CACHE_MISS_ST_NONSPEC"
- "L1D_CACHE_WRITEBACK"
- "L1D_TLB_ACCESS"
- "L1D_TLB_FILL"
- "L1D_TLB_MISS"
- "L1D_TLB_MISS_NONSPEC"
- "L1I_CACHE_MISS_DEMAND"
- "L1I_TLB_FILL"
- "L1I_TLB_MISS_DEMAND"
- "L2 RAM addr out of range"
- "L2C_PRB_CMD_FLUSH: L1 or LLC flush"
- "L2C_PRB_CMD_L1WB: L1 writeback"
- "L2C_PRB_CMD_PULLV: PullV pass"
- "L2C_PRB_CMD_RAMZERO: LLC as RAM zero"
- "L2_TLB_MISS_DATA"
- "L2_TLB_MISS_INSTRUCTION"
- "LDST_X64_UOP"
- "LDST_XPG_UOP"
- "LD_NT_UOP"
- "LD_UNIT_UOP"
- "LLC %s error: FAR=%#lx err_sts: (%s) @%s:%d"
- "LLC %s error: FAR=%#lx way=%#x syndrome=%#x err_sts: (%s) @%s:%d"
- "LLC %s error: FAR=%#lx way=0x%x syndrome=%#x cmd=%#x(%s) err_sts: (%s) @%s:%d"
- "LLC %s multi-hit error: FAR=%#lx way_mask=%#x err_sts: (%s) @%s:%d"
- "LLC dup tag multi-hit error by CPU %d: FAR=%#lx way_mask=%#x err_sts: (%s) @%s:%d"
- "LLC_ERR_STS/ADR/INF=%#llx/%#llx/%#llx LSU_ERR_STS=%#llx FED_ERR_STS=%#llx MMU_ERR_STS=%#llx DPC_ERR_STS=%#llx"
- "LSU"
- "MAP_DISPATCH_BUBBLE"
- "MAP_INT_UOP"
- "MAP_LDST_UOP"
- "MAP_REWIND"
- "MAP_SIMD_UOP"
- "MAP_STALL"
- "MAP_STALL_DISPATCH"
- "MAP_UOP"
- "MMU"
- "MMU_TABLE_WALK_DATA"
- "MMU_TABLE_WALK_INSTRUCTION"
- "MMU_VIRTUAL_MEMORY_FAULT_NONSPEC"
- "MTR controller lock violation"
- "Multi-hit Error on L1-dTLB-MainArray"
- "Multi-hit Error on L1-dTLB-Sidecar"
- "Multi-hit Error on L1-iTLB-MainArray"
- "Multi-hit Error on L1-iTLB-Sidecar"
- "Multi-hit Error on L2-mTLB for D-side accesses"
- "Multi-hit Error on L2-mTLB for I-side accesses"
- "Multi-hit Error on L2-mTLB or D-side accesses"
- "Multi-hit Error on MMU TWC for D-side accesses"
- "Multi-hit Error on MMU TWC for I-side accesses"
- "PIO"
- "PPT in unsafe state"
- "Parity-error in L1ICache-DATA"
- "RETIRE_UOP"
- "ST_MEMORY_ORDER_VIOLATION_NONSPEC"
- "ST_NT_UOP"
- "ST_UNIT_UOP"
- "Uncontained LLC AMX %s error: FAR=%#lx way=0x%x syndrome=%#x cmd=%#x(%s) err_sts: (%s) @%s:%d"
- "Unexpected duplicate splay entry! @%s:%d"
- "Unexpectedly could not acquire telemetry lock (nested acquire will deadlock) @%s:%d"
- "Unexpectedly found multiple concurrent drains! @%s:%d"
- "Unhandled %c-core error: %s @%s:%d"
- "Unhandled recoverable LLC %s error: FAR=%#lx way=0x%x syndrome=%#x cmd=%#x(%s) err_sts: (%s) @%s:%d"
- "bpret"
- "bti_telemetry.c"
- "cpu%d"
- "cpu%d: LLC %s error%s from %s: FAR=%#lx addr=%#llx cmd=%#x(%s) err_sts: (%s) @%s:%d"
- "daemon.mcc_error-events"
- "double-bit cache ECC"
- "double-bit cache ECC overflow"
- "generic_platform_error_handler.c"
- "l2-ecc-correctable-panic"
- "mdsb"
- "pmap_asid_plru"
- "pmap_bootstrap"
- "single-bit ECC"
- "single-bit ECC counter overflow"
- "site.bti_telemetry_record_s"
- "snoop"
- "tag"
- "way predictor"

```

</details>

## MachO

### 🆕 NEW (111)

<details>
  <summary><i>View NEW</i></summary>

- `/System/ExclaveKit/System/Library/Frameworks/AOPVoiceTriggerSecure.framework/AOPVoiceTriggerSecure`
- `/System/ExclaveKit/System/Library/Frameworks/AVFAudio.framework/AVFAudio`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvMisc.dylib`
- `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/vecLib`
- `/System/ExclaveKit/System/Library/Frameworks/AppleProxExclaveComponent.framework/AppleProxExclaveComponent`
- `/System/ExclaveKit/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/ExclaveKit/System/Library/Frameworks/DeviceTreeKit.framework/DeviceTreeKit`
- `/System/ExclaveKit/System/Library/Frameworks/EXDataLoader.framework/EXDataLoader`
- `/System/ExclaveKit/System/Library/Frameworks/EXMobileAssetLoader.framework/EXMobileAssetLoader`
- `/System/ExclaveKit/System/Library/Frameworks/EXSimpleFileIO.framework/EXSimpleFileIO`
- `/System/ExclaveKit/System/Library/Frameworks/ExclaveFDRDecodeRawDataStoreKitComponent.framework/ExclaveFDRDecodeRawDataStoreKitComponent`
- `/System/ExclaveKit/System/Library/Frameworks/ExclavesAudioDrivers.framework/ExclavesAudioDrivers`
- `/System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/ExclaveKit/System/Library/Frameworks/IsolatedAudioMeterClientExclaveComponent.framework/IsolatedAudioMeterClientExclaveComponent`
- `/System/ExclaveKit/System/Library/Frameworks/IsolatedCoreAudioClientComponent.framework/IsolatedCoreAudioClientComponent`
- `/System/ExclaveKit/System/Library/Frameworks/MobileGestalt.framework/MobileGestalt`
- `/System/ExclaveKit/System/Library/Frameworks/OSLogExclaves.framework/OSLogExclaves`
- `/System/ExclaveKit/System/Library/Frameworks/SILManagerComponent.framework/SILManagerComponent`
- `/System/ExclaveKit/System/Library/Frameworks/SharedMemory.framework/SharedMemory`
- `/System/ExclaveKit/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis`
- `/System/ExclaveKit/System/Library/Frameworks/StackshotDelegateComponent.framework/StackshotDelegateComponent`
- `/System/ExclaveKit/System/Library/Frameworks/T8140_IR_ISP_EK_Component.framework/T8140_IR_ISP_EK_Component`
- `/System/ExclaveKit/System/Library/Frameworks/T8140_RGB_ISP_EK_Component.framework/T8140_RGB_ISP_EK_Component`
- `/System/ExclaveKit/System/Library/Frameworks/TransitKit.framework/TransitKit`
- `/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision`
- `/System/ExclaveKit/System/Library/Frameworks/VoiceTriggerCommon.framework/VoiceTriggerCommon`
- `/System/ExclaveKit/System/Library/Frameworks/VoiceTriggerSecure.framework/VoiceTriggerSecure`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/ANEExclaveServices.framework/ANEExclaveServices`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/ANSTCommon.framework/ANSTCommon`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioCaptureServer.framework/AudioCaptureServer`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioCaptureServerComponent.framework/AudioCaptureServerComponent`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioDSP.framework/AudioDSP`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioDSPControllerComponent.framework/AudioDSPControllerComponent`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioDSPGraph.framework/AudioDSPGraph`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioDSPProcessorComponent.framework/AudioDSPProcessorComponent`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreAudioResources.framework/CoreAudioResources`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreSpeechExclaveComponent.framework/CoreSpeechExclaveComponent`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreVideo.framework/CoreVideo`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/DebugExfiltration.framework/DebugExfiltration`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/EXDisplayPipeSwapClient.framework/EXDisplayPipeSwapClient`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/EXSurface.framework/EXSurface`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/Espresso.framework/Espresso`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/ExclaveCredentialManager.framework/ExclaveCredentialManager`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/ExclaveFDRDecode.framework/ExclaveFDRDecode`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/MLCompilerRuntime.framework/MLCompilerRuntime`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/MLCompilerServices.framework/MLCompilerServices`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/SecureVoiceTriggerAssets_exclavekit`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/ShareLibCommon_EK.framework/ShareLibCommon_EK`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/ShazamKit.framework/ShazamKit`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SphinxProxTrustedFDR.framework/SphinxProxTrustedFDR`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/T8140_CoreAAClientKit.framework/T8140_CoreAAClientKit`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/T8140_CoreANSTKit.framework/T8140_CoreANSTKit`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/T8140_CoreERClientKit.framework/T8140_CoreERClientKit`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/T8140_ExclaveISPSharedLib_exclavekit.framework/T8140_ExclaveISPSharedLib_exclavekit`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/VoiceTriggerEventProviderExclave.framework/VoiceTriggerEventProviderExclave`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/VoiceTriggerExclave.framework/VoiceTriggerExclave`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/caulk.framework/caulk`
- `/System/ExclaveKit/usr/bin/tightbeam_stub`
- `/System/ExclaveKit/usr/lib/dyld`
- `/System/ExclaveKit/usr/lib/libSystem.dylib`
- `/System/ExclaveKit/usr/lib/libc++.dylib`
- `/System/ExclaveKit/usr/lib/libc++abi.dylib`
- `/System/ExclaveKit/usr/lib/libcompression.dylib`
- `/System/ExclaveKit/usr/lib/libobjc.A.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswiftC.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswiftCore.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswiftObjectiveC.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswiftRegexBuilder.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswiftSwiftOnoneSupport.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswift_Builtin_float.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswift_Concurrency.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswift_RegexParser.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswift_StringProcessing.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswift_errno.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswift_math.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswift_stdio.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswift_time.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswiftos.dylib`
- `/System/ExclaveKit/usr/lib/swift/libswiftsys_time.dylib`
- `/System/ExclaveKit/usr/lib/system/libdispatch.dylib`
- `/System/ExclaveKit/usr/lib/system/libdispatch_debug.dylib`
- `/System/ExclaveKit/usr/lib/system/libdispatch_profile.dylib`
- `/System/ExclaveKit/usr/lib/system/libdyld.dylib`
- `/System/ExclaveKit/usr/lib/system/liblibc.dylib`
- `/System/ExclaveKit/usr/lib/system/liblibc_plat.dylib`
- `/System/ExclaveKit/usr/lib/system/libmacho.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_blocks_debug.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_blocks_profile.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_c.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_collections.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_m.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_platform.dylib`
- `/System/ExclaveKit/usr/lib/system/libsystem_trace.dylib`
- `/System/ExclaveKit/usr/lib/system/libunwind.dylib`

</details>

### ⬆️ Updated (13)

<details>
  <summary><i>View Updated</i></summary>

#### Preferences

>  `/Applications/Preferences.app/Preferences`

```diff

   __TEXT.__eh_frame: 0x1cc0
   __DATA_CONST.__auth_got: 0x1c70
   __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__auth_ptr: 0x15d0
+  __DATA_CONST.__auth_ptr: 0x15c8
   __DATA_CONST.__const: 0x5d40
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x168

```

#### TrustedPeersHelper

>  `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

   __TEXT.__eh_frame: 0x6e70
   __DATA_CONST.__auth_got: 0xf40
   __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__auth_ptr: 0x6b0
+  __DATA_CONST.__auth_ptr: 0x6c0
   __DATA_CONST.__const: 0xf6d0
   __DATA_CONST.__cfstring: 0x20c0
   __DATA_CONST.__objc_classlist: 0x268

```

#### PrivacyAndSecuritySettings

>  `/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings`

```diff

   __TEXT.__eh_frame: 0xfd0
   __DATA_CONST.__auth_got: 0xd58
   __DATA_CONST.__got: 0x730
-  __DATA_CONST.__auth_ptr: 0x9d8
+  __DATA_CONST.__auth_ptr: 0x9d0
   __DATA_CONST.__const: 0x2008
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x50

```

#### AppleVideoEncoder

>  `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

```diff

   __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x5962c
+  __TEXT.__cstring: 0x59623
   __TEXT.__const: 0x15978
   __TEXT.__gcc_except_tab: 0x5cc
   __TEXT.__objc_methname: 0xb

   - /usr/lib/libobjc.A.dylib
   Functions: 692
   Symbols:   543
-  CStrings:  5684
+  CStrings:  5683
 
CStrings:
+ "18:28:51"
+ "Sep 12 2024"
- "23:30:28"
- "23:30:29"
- "Sep  2 2024"

```

#### PassbookLockedWidgetsExtension

>  `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension`

```diff

   __TEXT.__objc_methname: 0x177
   __TEXT.__oslogstring: 0x85
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__unwind_info: 0x508
   __TEXT.__eh_frame: 0x124
   __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0x358

```

#### applekeystored

>  `/usr/libexec/applekeystored`

```diff

   __TEXT.__eh_frame: 0x21e8
   __DATA_CONST.__auth_got: 0xbe8
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__auth_ptr: 0x778
+  __DATA_CONST.__auth_ptr: 0x768
   __DATA_CONST.__const: 0x7a50
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x30

```

#### swtransparencyd

>  `/usr/libexec/swtransparencyd`

```diff

   __TEXT.__eh_frame: 0x627c
   __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x648
-  __DATA_CONST.__auth_ptr: 0x5f0
+  __DATA_CONST.__auth_ptr: 0x580
   __DATA_CONST.__const: 0x5c58
   __DATA_CONST.__cfstring: 0x3100
   __DATA_CONST.__objc_classlist: 0x658

```

#### appstored

>  `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

   __TEXT.__eh_frame: 0x7334
   __DATA_CONST.__auth_got: 0x1e10
   __DATA_CONST.__got: 0x16d0
-  __DATA_CONST.__auth_ptr: 0x868
+  __DATA_CONST.__auth_ptr: 0x838
   __DATA_CONST.__const: 0x1ce80
   __DATA_CONST.__cfstring: 0x1ae00
   __DATA_CONST.__objc_classlist: 0x1618
CStrings:
+ "19:03:57"
+ "Sep 12 2024"
- "23:16:35"
- "Sep  2 2024"

```

#### akd

>  `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

   __TEXT.__eh_frame: 0x6df0
   __DATA_CONST.__auth_got: 0xe90
   __DATA_CONST.__got: 0x15b0
-  __DATA_CONST.__auth_ptr: 0x510
+  __DATA_CONST.__auth_ptr: 0x508
   __DATA_CONST.__const: 0xbbd8
   __DATA_CONST.__cfstring: 0x6ae0
   __DATA_CONST.__objc_classlist: 0x6d0

```

#### backupd

>  `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

   __TEXT.__eh_frame: 0x1c98
   __DATA_CONST.__auth_got: 0x1990
   __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__auth_ptr: 0x350
+  __DATA_CONST.__auth_ptr: 0x348
   __DATA_CONST.__const: 0x88b8
   __DATA_CONST.__cfstring: 0x1f900
   __DATA_CONST.__objc_classlist: 0xab0

```

#### passd

>  `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

   __TEXT.__eh_frame: 0xdfc
   __DATA_CONST.__auth_got: 0x2858
   __DATA_CONST.__got: 0x3258
-  __DATA_CONST.__auth_ptr: 0x2e0
+  __DATA_CONST.__auth_ptr: 0x2f8
   __DATA_CONST.__const: 0x2ae98
   __DATA_CONST.__cfstring: 0x2e620
   __DATA_CONST.__objc_classlist: 0x16d0

```

#### seserviced

>  `/usr/libexec/seserviced`

```diff

   __TEXT.__eh_frame: 0xfea4
   __DATA_CONST.__auth_got: 0x1d18
   __DATA_CONST.__got: 0xfc0
-  __DATA_CONST.__auth_ptr: 0xb50
+  __DATA_CONST.__auth_ptr: 0xba8
   __DATA_CONST.__const: 0xf0f0
   __DATA_CONST.__cfstring: 0x11a80
   __DATA_CONST.__objc_classlist: 0x6e8

```

#### transparencyd

>  `/usr/libexec/transparencyd`

```diff

   __TEXT.__eh_frame: 0x1128
   __DATA_CONST.__auth_got: 0x1360
   __DATA_CONST.__got: 0xd58
-  __DATA_CONST.__auth_ptr: 0x370
+  __DATA_CONST.__auth_ptr: 0x360
   __DATA_CONST.__const: 0x12908
   __DATA_CONST.__cfstring: 0xd420
   __DATA_CONST.__objc_classlist: 0xb90

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### 🆕 NEW (23)

- `AppleAVE2FW_H17.im4p`
- `SmartIOFirmware_ASCv7.im4p`
- `adc-rheia-d9x.im4p`
- `agx_a010.bin`
- `agx_b010.bin`
- `ansf.t8140.release.im4p`
- `exclave_DeviceServer`
- `exclave_ExclaveStackshotServer`
- `exclave_conclave_launcher`
- `exclave_kernel`
- `exclave_pmm_exclave`
- `exclave_roottask`
- `exclave_scheduler`
- `exclave_sharedcache`
- `exclave_sharedmem`
- `exclave_sharedmem-v2`
- `exclave_xnuproxy`
- `h17_ane_fw_theia_d9x.im4p`
- `rans.t8140.release.im4p`
- `securem3fw-d9x.im4p`
- `sptm.t8140.release.im4p`
- `t8140pmcfw.im4p`
- `t8140pmp.im4p`

### ❌ Removed (11)

- `AppleAVE2FW_H16.im4p`
- `SmartIOFirmware_ASCv6.im4p`
- `adc-aceso-d8x.im4p`
- `ansf.t8130.release.im4p`
- `aopfw-iphone16aop.RELEASE.im4p`
- `h16x_ane_fw_iaso_d8x.im4p`
- `rans.t8130.release.im4p`
- `sptm.t8122.release.im4p`
- `t8130dcp.im4p`
- `t8130dcp_restore.im4p`
- `t8130pmp.im4p`

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### agx_a000.bin

>  `agx_a000.bin`

```diff

 
-  __TEXT.__text: 0x53288
+  __TEXT.__text: 0x34668
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1ca0
+  __TEXT.__const: 0x1869
   __TEXT._rtk_patchbay: 0x1e8
-  __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__chain_starts: 0x28
-  __TEXT.__cstring: 0x1e4b
+  __TEXT._rtk_tunables: 0x6a0
+  __TEXT.__chain_starts: 0x2c
+  __TEXT.__cstring: 0x1b78
   __DATA.__gxf_data: 0x41f0
-  __DATA.__data: 0xda8
-  __DATA.__const: 0x548
+  __DATA.__data: 0x14a18
+  __DATA.__const: 0x2d0
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__constructor: 0x0
   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
-  __DATA.__zerofill: 0x67138
-  Functions: 479
-  Symbols:   220
-  CStrings:  212
+  __DATA.__zerofill: 0x57bd8
+  Functions: 412
+  Symbols:   223
+  CStrings:  187
 
Symbols:
+ __platform_memcmp
+ __rtk_tracekit_thread_init
+ __rtk_tracekit_transition_context
+ _bcmp
+ _memcmp
- _AGFHALWaitForPerfState
- ___powisf2
CStrings:
+ "  FW Build running in SKSM Enabled mode"
+ "  FW Build variant: g17p"
+ "%s: !!! Fatal Error: %s : power %s : Queues have pending kill."
+ "%s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx"
+ "%s: !!! Fatal Error: All parents of KSM kick queue entry (Queue=%u, TS=0x%010llx) not received. Valid parent mask=0x%llx"
+ "%s: !!! Fatal Error: Deferred TSQ buffer has no free space!"
+ "%s: !!! Fatal Error: Expected compute command, saw %d"
+ "%s: !!! Fatal Error: Failed to allocate OOM state index"
+ "%s: !!! Fatal Error: Invalid DataMaster %u"
+ "%s: !!! Fatal Error: Kill not supported for TA commands"
+ "%s: !!! Fatal Error: No free slot found in completion entry reorder buffer"
+ "%s: !!! Fatal Error: Recovery: Dependent skip kick call must be for 3D. Queue=%u KickEntry=%p"
+ "%s: !!! Fatal Error: Resume called for reason %d with auto resume enabled"
+ "%s: !!! Fatal Error: Unexpected recovery type %llu!"
+ "%s: !!! Fatal Error: Unhandled : Invalid command type %d"
+ "%s: !!! Fatal Error: Unknown IOP msg type %d!"
+ "%s: !!! Fatal Error: Unknown message received (event = %llu)"
+ "%s: !!! Fatal Error: Unknown state = %d"
+ "%s: !!! Fatal Error: Unrecognized remote power kick value 0x%llx"
+ "%s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM"
+ "-> Parent index [%2u] : queue=%03u, ts=0x%010llx. Last completed TS=0x%010llx (valid=%d)"
+ "AGFAAsyncIOPCallback"
+ "AGFASchedulerProcessPowerKick"
+ "AGFASchedulerProcessRecovery"
+ "AGFAcceleratorProcessTimeStampQueue"
+ "AGFHRBCompletionEvent"
+ "AGFHRBResume"
+ "AGFKSMAreParentsReceived"
+ "Dumping parents of KSM kick queue entry (Queue=%u, TS=0x%010llx). Valid parent mask=0x%llx"
+ "Failed to allocate new ring entry"
+ "In order eviction check is unsupported when multiple normal completion queues are enabled."
+ "Invalid recovery phase = %d"
+ "KSM kick queue %u / dm %u / state %u: Out of order completion within a queue. Last completed TS=0x%llx. Current TS=0x%llx. Delta=%#llx"
+ "NOP command KSM kick queue %u : Last completed TS=0x%llx. Current TS=0x%llx. Stamp index=%u, Stamp=0x%x"
+ "Napping when SKSM is non idle i.e. there is work"
+ "Napping when SKSM is non idle i.e. there is work. No Events for scheduler thread."
+ "PBState must be unbind, before being rebound to different PB state"
+ "Performance"
+ "Received command type (%u) in KSM completion queue entry. payload0 = 0x%llx. payload1 = 0x%llx"
+ "SVC"
+ "Sep  3 2024 00:22:20"
+ "Thread time"
+ "UMA FW id state has bad context ID. context_id: %d"
+ "UMA: Power event when rebuild for ID %u in progress. Dropping the grow. Caller will issue a new rebuild (with updated count) for the ID"
+ "Unhandled command type (%u)"
+ "Unimplemented. AGFAGXInterruptPMThresholdHandler"
+ "agfAllocateOomState"
+ "agfGIN1115ReorderBufferInsertEntry"
+ "agfIsKickSkippable"
+ "agfKSMCompletionQueueGetFWDMType"
+ "agfKSMKickQueueGetDMType"
+ "agfMarkCommandAsKilled"
+ "agfaHRBEnabledQueuesHalt"
+ "agfaHRBEnabledQueuesResume"
+ "agfaHRBPanicIfDisabled"
+ "agfaKBValidateStatePowerEvent"
+ "agfaParamBufferManagerUnbindPBState"
+ "agfaProcessChannelCommand"
+ "agfaRecoverySkipKickEntry"
+ "agfaRemotePowerKick"
+ "agx_gpu_util"
+ "agx_scheduler"
+ "gfx_iop_ints"
+ "gfx_iop_msgs"
- "  FW Build doesn't support SKSM"
- "  FW Build variant: g16p"
- "%s :: Unexpected command type %u\n"
- "%s: !!! Fatal Error: Cre entry Index is greater than max GRT entries"
- "%s: !!! Fatal Error: GPU SoCHot interrupt received. Enabled sensor mask = %.16llx. Alarm%u Threshold = %u celcius"
- "%s: !!! Fatal Error: Invalid MTR Temperature Interrupt received!"
- "%s: !!! Fatal Error: MTR Alarm interrupts not handled!"
- "%s: !!! Fatal Error: PTD read failed unexpectedly with error code 0x%x."
- "%s: !!! Fatal Error: Received MTR Alarm interrupt from GPU but no match found in MTR hardware!"
- "%s: !!! Fatal Error: Unknown Power state mode!"
- "%s: !!! Fatal Error: Unrecognized recovery power cycle event 0x%llx"
- "%s: CRE disabled by boot arg"
- "%s: CRE has no restore data and will save registers this run."
- "%s: CRE has restored our registers"
- "%s: Entering CRE critical section as CRE disabled"
- "%s: Entering CRE critical section for save"
- "%s: Moving out of critical section having saved %i registers"
- "%s: Moving out of critical section having verified %i registers"
- "%s:%d Bad Read offset=0x%X"
- "%s:%d Bad write offset=0x%X"
- "%s:%d Invalid handle"
- "%s:%d Invalid index[%d]"
- "%s:%d Invalid parameter range[%d]"
- "%s:%d Invalid parameter range[%d] or data = NULL"
- "%s:%d Range =%d info not found"
- "%s:%d Unknown range[%d]"
- "AGF3DDataMasterPostProcessingCallback"
- "AGF3DDataMasterPreProcessingCallback"
- "AGF3DDataMasterSKUCallback"
- "AGFA2Level2KRadixTree OOM.\n"
- "AGFACREEnterCriticalSection"
- "AGFACREInit"
- "AGFACRELeaveCriticalSection"
- "AGFAInitSequence unknown seq type %u"
- "AGFAPTDReadEntryWrapper"
- "AGFAPowerHandlePowerUp"
- "AGFAPowerProcessRecoveryPowerCycle"
- "AGFCLDataMasterPostProcessingCallback"
- "AGFCLDataMasterPreProcessingCallback"
- "AGFHALCREAddEntry"
- "AGFHALCREWaitForIdle"
- "AGFHALFenderSleep"
- "AGFParameterBufferCleanup"
- "AGFSoCHotHandleAlarmInterrupt"
- "AGFTADataMasterPostProcessingCallback"
- "AGFTADataMasterPreProcessingCallback"
- "AGX_CR_DIRECTOR_CONFIG: 0x%llx"
- "AGX_CR_GDIR_DIRECTOR_CTRL: 0x%llx"
- "AGX_CR_UMA_DUPM_SELF_RESERVE_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_RELOAD_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_RELOAD_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_RELOAD_COUNT"
- "AGX_CR_USC_TP_GLOBAL_RESOURCE_CFG0_MAX_TGMEM"
- "Attempting to update a NULL UMA pool!\n"
- "DAG-RadixTree-Allocator OOM: tree->parent == 0xffffffff"
- "DAG: Non Sequential Stamp Updates seen entryIdx 0x%x roots.dag 0x%x stampIdx 0x%x stampValue 0x%x channel %p channelRingCommandIndex 0x%x"
- "Failed to enable CRE restore as sCRE hasn't been set up by iBoot."
- "GIN-953: Found dslots_mask of 0x%llx for DM %u (slot=%u, topslot_status=0x%llx)"
- "Incorrect power sub-state for early wake"
- "Invalid command type (%u)"
- "PTD write failed (%u, %u)"
- "Parent node in invalid state."
- "Sep  3 2024 00:22:19"
- "UMA WARNING: Constant %s, value %llu, does not match SW expected value of %llu"
- "UMA WARNING: UMA constants are set to unsupported values. You may see hangs!"
- "Unable to perform secure cache flush, RTK_status:0x%X"
- "Unable to perform secure cache flush, invalid context ID:0x%X"
- "Underflow of perpriority_inflight_commands[%d] = 0x%x num_commands 0x%x"
- "Unexpected TA sub-state found in Interrupt Post recovery: %u"
- "Unknown SKU command type %u"
- "VCM perf state change timeout after %uus (VCM_PERF_STATE_CONTROL = %x)"
- "agfMTRAlarmHandler"
- "agfMTRTemperatureInterruptHandler"
- "agfPollFenderRegIgnoreRecovery"
- "agx_background"
- "agx_interrupt"
- "agx_power"
- "command type is %d channel %p commandIndex %d totalBarriers %d index %d"
- "gin_1072_gtp_pausing_disabled %u gin_1072_affected_top_slot %u"
- "ptd_read"
- "ptd_write"
- "range_param_check"
- "rtkptd.cpp"

```

#### agx_b000.bin

>  `agx_b000.bin`

```diff

 
-  __TEXT.__text: 0x52fe4
+  __TEXT.__text: 0x34568
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1ce0
+  __TEXT.__const: 0x1869
   __TEXT._rtk_patchbay: 0x1e8
-  __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__chain_starts: 0x28
-  __TEXT.__cstring: 0x1e4b
+  __TEXT._rtk_tunables: 0x6a0
+  __TEXT.__chain_starts: 0x2c
+  __TEXT.__cstring: 0x1b0a
   __DATA.__gxf_data: 0x41f0
-  __DATA.__data: 0xda8
-  __DATA.__const: 0x548
+  __DATA.__data: 0x14a18
+  __DATA.__const: 0x2d0
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__constructor: 0x0
   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
-  __DATA.__zerofill: 0x66fb8
-  Functions: 478
-  Symbols:   220
-  CStrings:  212
+  __DATA.__zerofill: 0x57bd8
+  Functions: 409
+  Symbols:   223
+  CStrings:  185
 
Symbols:
+ __platform_memcmp
+ __rtk_tracekit_thread_init
+ __rtk_tracekit_transition_context
+ _bcmp
+ _memcmp
- _AGFHALWaitForPerfState
- ___powisf2
CStrings:
+ "  FW Build running in SKSM Enabled mode"
+ "  FW Build variant: g17p"
+ "%s: !!! Fatal Error: %s : power %s : Queues have pending kill."
+ "%s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx"
+ "%s: !!! Fatal Error: All parents of KSM kick queue entry (Queue=%u, TS=0x%010llx) not received. Valid parent mask=0x%llx"
+ "%s: !!! Fatal Error: Deferred TSQ buffer has no free space!"
+ "%s: !!! Fatal Error: Expected compute command, saw %d"
+ "%s: !!! Fatal Error: Failed to allocate OOM state index"
+ "%s: !!! Fatal Error: Invalid DataMaster %u"
+ "%s: !!! Fatal Error: Kill not supported for TA commands"
+ "%s: !!! Fatal Error: Recovery: Dependent skip kick call must be for 3D. Queue=%u KickEntry=%p"
+ "%s: !!! Fatal Error: Resume called for reason %d with auto resume enabled"
+ "%s: !!! Fatal Error: Unexpected recovery type %llu!"
+ "%s: !!! Fatal Error: Unhandled : Invalid command type %d"
+ "%s: !!! Fatal Error: Unknown IOP msg type %d!"
+ "%s: !!! Fatal Error: Unknown message received (event = %llu)"
+ "%s: !!! Fatal Error: Unknown state = %d"
+ "%s: !!! Fatal Error: Unrecognized remote power kick value 0x%llx"
+ "%s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM"
+ "-> Parent index [%2u] : queue=%03u, ts=0x%010llx. Last completed TS=0x%010llx (valid=%d)"
+ "AGFAAsyncIOPCallback"
+ "AGFASchedulerProcessPowerKick"
+ "AGFASchedulerProcessRecovery"
+ "AGFAcceleratorProcessTimeStampQueue"
+ "AGFHRBCompletionEvent"
+ "AGFHRBResume"
+ "AGFKSMAreParentsReceived"
+ "Dumping parents of KSM kick queue entry (Queue=%u, TS=0x%010llx). Valid parent mask=0x%llx"
+ "Failed to allocate new ring entry"
+ "In order eviction check is unsupported when multiple normal completion queues are enabled."
+ "Invalid recovery phase = %d"
+ "KSM kick queue %u / dm %u / state %u: Out of order completion within a queue. Last completed TS=0x%llx. Current TS=0x%llx. Delta=%#llx"
+ "NOP command KSM kick queue %u : Last completed TS=0x%llx. Current TS=0x%llx. Stamp index=%u, Stamp=0x%x"
+ "Napping when SKSM is non idle i.e. there is work"
+ "Napping when SKSM is non idle i.e. there is work. No Events for scheduler thread."
+ "PBState must be unbind, before being rebound to different PB state"
+ "Performance"
+ "Received command type (%u) in KSM completion queue entry. payload0 = 0x%llx. payload1 = 0x%llx"
+ "SVC"
+ "Sep  3 2024 00:26:19"
+ "Thread time"
+ "UMA FW id state has bad context ID. context_id: %d"
+ "UMA: Power event when rebuild for ID %u in progress. Dropping the grow. Caller will issue a new rebuild (with updated count) for the ID"
+ "Unhandled command type (%u)"
+ "Unimplemented. AGFAGXInterruptPMThresholdHandler"
+ "agfAllocateOomState"
+ "agfIsKickSkippable"
+ "agfKSMCompletionQueueGetFWDMType"
+ "agfKSMKickQueueGetDMType"
+ "agfMarkCommandAsKilled"
+ "agfaHRBEnabledQueuesHalt"
+ "agfaHRBEnabledQueuesResume"
+ "agfaHRBPanicIfDisabled"
+ "agfaKBValidateStatePowerEvent"
+ "agfaParamBufferManagerUnbindPBState"
+ "agfaProcessChannelCommand"
+ "agfaRecoverySkipKickEntry"
+ "agfaRemotePowerKick"
+ "agx_gpu_util"
+ "agx_scheduler"
+ "gfx_iop_ints"
+ "gfx_iop_msgs"
- "  FW Build doesn't support SKSM"
- "  FW Build variant: g16p"
- "%s :: Unexpected command type %u\n"
- "%s: !!! Fatal Error: Cre entry Index is greater than max GRT entries"
- "%s: !!! Fatal Error: GPU SoCHot interrupt received. Enabled sensor mask = %.16llx. Alarm%u Threshold = %u celcius"
- "%s: !!! Fatal Error: Invalid MTR Temperature Interrupt received!"
- "%s: !!! Fatal Error: MTR Alarm interrupts not handled!"
- "%s: !!! Fatal Error: PTD read failed unexpectedly with error code 0x%x."
- "%s: !!! Fatal Error: Received MTR Alarm interrupt from GPU but no match found in MTR hardware!"
- "%s: !!! Fatal Error: Unknown Power state mode!"
- "%s: !!! Fatal Error: Unrecognized recovery power cycle event 0x%llx"
- "%s: CRE disabled by boot arg"
- "%s: CRE has no restore data and will save registers this run."
- "%s: CRE has restored our registers"
- "%s: Entering CRE critical section as CRE disabled"
- "%s: Entering CRE critical section for save"
- "%s: Moving out of critical section having saved %i registers"
- "%s: Moving out of critical section having verified %i registers"
- "%s:%d Bad Read offset=0x%X"
- "%s:%d Bad write offset=0x%X"
- "%s:%d Invalid handle"
- "%s:%d Invalid index[%d]"
- "%s:%d Invalid parameter range[%d]"
- "%s:%d Invalid parameter range[%d] or data = NULL"
- "%s:%d Range =%d info not found"
- "%s:%d Unknown range[%d]"
- "AGF3DDataMasterPostProcessingCallback"
- "AGF3DDataMasterPreProcessingCallback"
- "AGF3DDataMasterSKUCallback"
- "AGFA2Level2KRadixTree OOM.\n"
- "AGFACREEnterCriticalSection"
- "AGFACREInit"
- "AGFACRELeaveCriticalSection"
- "AGFAInitSequence unknown seq type %u"
- "AGFAPTDReadEntryWrapper"
- "AGFAPowerHandlePowerUp"
- "AGFAPowerProcessRecoveryPowerCycle"
- "AGFCLDataMasterPostProcessingCallback"
- "AGFCLDataMasterPreProcessingCallback"
- "AGFHALCREAddEntry"
- "AGFHALCREWaitForIdle"
- "AGFHALFenderSleep"
- "AGFParameterBufferCleanup"
- "AGFSoCHotHandleAlarmInterrupt"
- "AGFTADataMasterPostProcessingCallback"
- "AGFTADataMasterPreProcessingCallback"
- "AGX_CR_DIRECTOR_CONFIG: 0x%llx"
- "AGX_CR_GDIR_DIRECTOR_CTRL: 0x%llx"
- "AGX_CR_UMA_DUPM_SELF_RESERVE_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_RELOAD_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_RELOAD_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_RELOAD_COUNT"
- "AGX_CR_USC_TP_GLOBAL_RESOURCE_CFG0_MAX_TGMEM"
- "Attempting to update a NULL UMA pool!\n"
- "DAG-RadixTree-Allocator OOM: tree->parent == 0xffffffff"
- "DAG: Non Sequential Stamp Updates seen entryIdx 0x%x roots.dag 0x%x stampIdx 0x%x stampValue 0x%x channel %p channelRingCommandIndex 0x%x"
- "Failed to enable CRE restore as sCRE hasn't been set up by iBoot."
- "GIN-953: Found dslots_mask of 0x%llx for DM %u (slot=%u, topslot_status=0x%llx)"
- "Incorrect power sub-state for early wake"
- "Invalid command type (%u)"
- "PTD write failed (%u, %u)"
- "Parent node in invalid state."
- "Sep  3 2024 00:25:09"
- "UMA WARNING: Constant %s, value %llu, does not match SW expected value of %llu"
- "UMA WARNING: UMA constants are set to unsupported values. You may see hangs!"
- "Unable to perform secure cache flush, RTK_status:0x%X"
- "Unable to perform secure cache flush, invalid context ID:0x%X"
- "Underflow of perpriority_inflight_commands[%d] = 0x%x num_commands 0x%x"
- "Unexpected TA sub-state found in Interrupt Post recovery: %u"
- "Unknown SKU command type %u"
- "VCM perf state change timeout after %uus (VCM_PERF_STATE_CONTROL = %x)"
- "agfMTRAlarmHandler"
- "agfMTRTemperatureInterruptHandler"
- "agfPollFenderRegIgnoreRecovery"
- "agx_background"
- "agx_interrupt"
- "agx_power"
- "command type is %d channel %p commandIndex %d totalBarriers %d index %d"
- "gin_1072_gtp_pausing_disabled %u gin_1072_affected_top_slot %u"
- "ptd_read"
- "ptd_write"
- "range_param_check"
- "rtkptd.cpp"

```

#### agx_b100.bin

>  `agx_b100.bin`

```diff

 
-  __TEXT.__text: 0x52fe4
+  __TEXT.__text: 0x34474
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1ce0
+  __TEXT.__const: 0x1869
   __TEXT._rtk_patchbay: 0x1e8
-  __TEXT._rtk_tunables: 0x5b0
-  __TEXT.__chain_starts: 0x28
-  __TEXT.__cstring: 0x1e4b
+  __TEXT._rtk_tunables: 0x6a0
+  __TEXT.__chain_starts: 0x2c
+  __TEXT.__cstring: 0x1b0a
   __DATA.__gxf_data: 0x41f0
-  __DATA.__data: 0xda8
-  __DATA.__const: 0x548
+  __DATA.__data: 0x14a18
+  __DATA.__const: 0x2d0
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__constructor: 0x0
   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
-  __DATA.__zerofill: 0x66fb8
-  Functions: 478
-  Symbols:   220
-  CStrings:  212
+  __DATA.__zerofill: 0x57bd8
+  Functions: 409
+  Symbols:   223
+  CStrings:  185
 
Symbols:
+ __platform_memcmp
+ __rtk_tracekit_thread_init
+ __rtk_tracekit_transition_context
+ _bcmp
+ _memcmp
- _AGFHALWaitForPerfState
- ___powisf2
CStrings:
+ "  FW Build running in SKSM Enabled mode"
+ "  FW Build variant: g17p"
+ "%s: !!! Fatal Error: %s : power %s : Queues have pending kill."
+ "%s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx"
+ "%s: !!! Fatal Error: All parents of KSM kick queue entry (Queue=%u, TS=0x%010llx) not received. Valid parent mask=0x%llx"
+ "%s: !!! Fatal Error: Deferred TSQ buffer has no free space!"
+ "%s: !!! Fatal Error: Expected compute command, saw %d"
+ "%s: !!! Fatal Error: Failed to allocate OOM state index"
+ "%s: !!! Fatal Error: Invalid DataMaster %u"
+ "%s: !!! Fatal Error: Kill not supported for TA commands"
+ "%s: !!! Fatal Error: Recovery: Dependent skip kick call must be for 3D. Queue=%u KickEntry=%p"
+ "%s: !!! Fatal Error: Resume called for reason %d with auto resume enabled"
+ "%s: !!! Fatal Error: Unexpected recovery type %llu!"
+ "%s: !!! Fatal Error: Unhandled : Invalid command type %d"
+ "%s: !!! Fatal Error: Unknown IOP msg type %d!"
+ "%s: !!! Fatal Error: Unknown message received (event = %llu)"
+ "%s: !!! Fatal Error: Unknown state = %d"
+ "%s: !!! Fatal Error: Unrecognized remote power kick value 0x%llx"
+ "%s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM"
+ "-> Parent index [%2u] : queue=%03u, ts=0x%010llx. Last completed TS=0x%010llx (valid=%d)"
+ "AGFAAsyncIOPCallback"
+ "AGFASchedulerProcessPowerKick"
+ "AGFASchedulerProcessRecovery"
+ "AGFAcceleratorProcessTimeStampQueue"
+ "AGFHRBCompletionEvent"
+ "AGFHRBResume"
+ "AGFKSMAreParentsReceived"
+ "Dumping parents of KSM kick queue entry (Queue=%u, TS=0x%010llx). Valid parent mask=0x%llx"
+ "Failed to allocate new ring entry"
+ "In order eviction check is unsupported when multiple normal completion queues are enabled."
+ "Invalid recovery phase = %d"
+ "KSM kick queue %u / dm %u / state %u: Out of order completion within a queue. Last completed TS=0x%llx. Current TS=0x%llx. Delta=%#llx"
+ "NOP command KSM kick queue %u : Last completed TS=0x%llx. Current TS=0x%llx. Stamp index=%u, Stamp=0x%x"
+ "Napping when SKSM is non idle i.e. there is work"
+ "Napping when SKSM is non idle i.e. there is work. No Events for scheduler thread."
+ "PBState must be unbind, before being rebound to different PB state"
+ "Performance"
+ "Received command type (%u) in KSM completion queue entry. payload0 = 0x%llx. payload1 = 0x%llx"
+ "SVC"
+ "Sep  3 2024 00:27:36"
+ "Thread time"
+ "UMA FW id state has bad context ID. context_id: %d"
+ "UMA: Power event when rebuild for ID %u in progress. Dropping the grow. Caller will issue a new rebuild (with updated count) for the ID"
+ "Unhandled command type (%u)"
+ "Unimplemented. AGFAGXInterruptPMThresholdHandler"
+ "agfAllocateOomState"
+ "agfIsKickSkippable"
+ "agfKSMCompletionQueueGetFWDMType"
+ "agfKSMKickQueueGetDMType"
+ "agfMarkCommandAsKilled"
+ "agfaHRBEnabledQueuesHalt"
+ "agfaHRBEnabledQueuesResume"
+ "agfaHRBPanicIfDisabled"
+ "agfaKBValidateStatePowerEvent"
+ "agfaParamBufferManagerUnbindPBState"
+ "agfaProcessChannelCommand"
+ "agfaRecoverySkipKickEntry"
+ "agfaRemotePowerKick"
+ "agx_gpu_util"
+ "agx_scheduler"
+ "gfx_iop_ints"
+ "gfx_iop_msgs"
- "  FW Build doesn't support SKSM"
- "  FW Build variant: g16p"
- "%s :: Unexpected command type %u\n"
- "%s: !!! Fatal Error: Cre entry Index is greater than max GRT entries"
- "%s: !!! Fatal Error: GPU SoCHot interrupt received. Enabled sensor mask = %.16llx. Alarm%u Threshold = %u celcius"
- "%s: !!! Fatal Error: Invalid MTR Temperature Interrupt received!"
- "%s: !!! Fatal Error: MTR Alarm interrupts not handled!"
- "%s: !!! Fatal Error: PTD read failed unexpectedly with error code 0x%x."
- "%s: !!! Fatal Error: Received MTR Alarm interrupt from GPU but no match found in MTR hardware!"
- "%s: !!! Fatal Error: Unknown Power state mode!"
- "%s: !!! Fatal Error: Unrecognized recovery power cycle event 0x%llx"
- "%s: CRE disabled by boot arg"
- "%s: CRE has no restore data and will save registers this run."
- "%s: CRE has restored our registers"
- "%s: Entering CRE critical section as CRE disabled"
- "%s: Entering CRE critical section for save"
- "%s: Moving out of critical section having saved %i registers"
- "%s: Moving out of critical section having verified %i registers"
- "%s:%d Bad Read offset=0x%X"
- "%s:%d Bad write offset=0x%X"
- "%s:%d Invalid handle"
- "%s:%d Invalid index[%d]"
- "%s:%d Invalid parameter range[%d]"
- "%s:%d Invalid parameter range[%d] or data = NULL"
- "%s:%d Range =%d info not found"
- "%s:%d Unknown range[%d]"
- "AGF3DDataMasterPostProcessingCallback"
- "AGF3DDataMasterPreProcessingCallback"
- "AGF3DDataMasterSKUCallback"
- "AGFA2Level2KRadixTree OOM.\n"
- "AGFACREEnterCriticalSection"
- "AGFACREInit"
- "AGFACRELeaveCriticalSection"
- "AGFAInitSequence unknown seq type %u"
- "AGFAPTDReadEntryWrapper"
- "AGFAPowerHandlePowerUp"
- "AGFAPowerProcessRecoveryPowerCycle"
- "AGFCLDataMasterPostProcessingCallback"
- "AGFCLDataMasterPreProcessingCallback"
- "AGFHALCREAddEntry"
- "AGFHALCREWaitForIdle"
- "AGFHALFenderSleep"
- "AGFParameterBufferCleanup"
- "AGFSoCHotHandleAlarmInterrupt"
- "AGFTADataMasterPostProcessingCallback"
- "AGFTADataMasterPreProcessingCallback"
- "AGX_CR_DIRECTOR_CONFIG: 0x%llx"
- "AGX_CR_GDIR_DIRECTOR_CTRL: 0x%llx"
- "AGX_CR_UMA_DUPM_SELF_RESERVE_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_CDM_PTC_RELOAD_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_FRG_PTC_RELOAD_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_MAX_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_MIN_COUNT"
- "AGX_CR_UMA_PTC_PAGE_RESERVE_GTP_PTC_RELOAD_COUNT"
- "AGX_CR_USC_TP_GLOBAL_RESOURCE_CFG0_MAX_TGMEM"
- "Attempting to update a NULL UMA pool!\n"
- "DAG-RadixTree-Allocator OOM: tree->parent == 0xffffffff"
- "DAG: Non Sequential Stamp Updates seen entryIdx 0x%x roots.dag 0x%x stampIdx 0x%x stampValue 0x%x channel %p channelRingCommandIndex 0x%x"
- "Failed to enable CRE restore as sCRE hasn't been set up by iBoot."
- "GIN-953: Found dslots_mask of 0x%llx for DM %u (slot=%u, topslot_status=0x%llx)"
- "Incorrect power sub-state for early wake"
- "Invalid command type (%u)"
- "PTD write failed (%u, %u)"
- "Parent node in invalid state."
- "Sep  3 2024 00:26:22"
- "UMA WARNING: Constant %s, value %llu, does not match SW expected value of %llu"
- "UMA WARNING: UMA constants are set to unsupported values. You may see hangs!"
- "Unable to perform secure cache flush, RTK_status:0x%X"
- "Unable to perform secure cache flush, invalid context ID:0x%X"
- "Underflow of perpriority_inflight_commands[%d] = 0x%x num_commands 0x%x"
- "Unexpected TA sub-state found in Interrupt Post recovery: %u"
- "Unknown SKU command type %u"
- "VCM perf state change timeout after %uus (VCM_PERF_STATE_CONTROL = %x)"
- "agfMTRAlarmHandler"
- "agfMTRTemperatureInterruptHandler"
- "agfPollFenderRegIgnoreRecovery"
- "agx_background"
- "agx_interrupt"
- "agx_power"
- "command type is %d channel %p commandIndex %d totalBarriers %d index %d"
- "gin_1072_gtp_pausing_disabled %u gin_1072_affected_top_slot %u"
- "ptd_read"
- "ptd_write"
- "range_param_check"
- "rtkptd.cpp"

```


</details>

## 🌴 Device Tree

- [Device Tree DIFF](DeviceTree.md)

## DSC

### WebKit

| iOS               | Version     |
| :---------------- | :---------- |
| 18.1 *(22B5045g)* | 619.2.3.1.0 |
| 18.1 *(22B5045h)* | 619.2.3.1.0 |

### Dylibs

#### 🆕 NEW (1)

- `/System/Library/Extensions/AGXMetalG17P.bundle/AGXMetalG17P`

#### ❌ Removed (2)

- `/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0`
- `/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0`

#### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

#### MediaPlaybackCore

>  `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x238
   __AUTH_CONST.__auth_got: 0x2728
-  __AUTH_CONST.__auth_ptr: 0xc60
+  __AUTH_CONST.__auth_ptr: 0xa70
   __AUTH_CONST.__const: 0xc4c8
   __AUTH_CONST.__cfstring: 0x1ae40
   __AUTH_CONST.__objc_const: 0x33a50

```

#### PassKitCore

>  `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

   __DATA_CONST.__objc_superrefs: 0x2ca8
   __DATA_CONST.__objc_arraydata: 0x3068
   __AUTH_CONST.__auth_got: 0x24e8
-  __AUTH_CONST.__auth_ptr: 0xa10
+  __AUTH_CONST.__auth_ptr: 0x9f8
   __AUTH_CONST.__const: 0x1c2f8
   __AUTH_CONST.__cfstring: 0x6bc00
   __AUTH_CONST.__objc_const: 0xc97f0

```

#### SonicKit

>  `/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit`

```diff

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc0
   __AUTH_CONST.__auth_got: 0x998
-  __AUTH_CONST.__auth_ptr: 0x518
+  __AUTH_CONST.__auth_ptr: 0x510
   __AUTH_CONST.__const: 0x11970
   __AUTH_CONST.__objc_const: 0x888
   __AUTH.__data: 0x38

```

#### _SonicKit_MusicKit

>  `/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit`

```diff

   __DATA_CONST.__objc_selrefs: 0x398
   __DATA_CONST.__objc_protorefs: 0x10
   __AUTH_CONST.__auth_got: 0x1098
-  __AUTH_CONST.__auth_ptr: 0xce8
+  __AUTH_CONST.__auth_ptr: 0xce0
   __AUTH_CONST.__const: 0x7b70
   __AUTH_CONST.__objc_const: 0xe30
   __AUTH.__objc_data: 0xc8

```

#### AVD.videodecoder

>  `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

   __TEXT.__gcc_except_tab: 0xc54
   __TEXT.__const: 0xbcdb
   __TEXT.__oslogstring: 0xef6f
-  __TEXT.__cstring: 0x5bff
+  __TEXT.__cstring: 0x5bf6
   __TEXT.__unwind_info: 0x1a88
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x38

   - /usr/lib/libc++.1.dylib
   Functions: 2221
   Symbols:   2684
-  CStrings:  1862
+  CStrings:  1861
 
CStrings:
+ "18:36:37"
+ "18:36:38"
+ "Sep 12 2024"
- "22:36:37"
- "22:36:38"
- "22:36:39"
- "Sep  2 2024"

```

#### AppleKeyStore

>  `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`

```diff

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH_CONST.__auth_ptr: 0x5d0
+  __AUTH_CONST.__auth_ptr: 0x578
   __AUTH_CONST.__const: 0x1da8
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x358

```

#### AppleMediaServices

>  `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

   __DATA_CONST.__objc_superrefs: 0xba0
   __DATA_CONST.__objc_arraydata: 0x4f0
   __AUTH_CONST.__auth_got: 0x2108
-  __AUTH_CONST.__auth_ptr: 0x9a8
+  __AUTH_CONST.__auth_ptr: 0x9a0
   __AUTH_CONST.__const: 0x23ac0
   __AUTH_CONST.__cfstring: 0x1fd20
   __AUTH_CONST.__objc_const: 0x380c0

```

#### CoreCDPUI

>  `/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI`

```diff

   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x138
   __AUTH_CONST.__auth_got: 0xf78
-  __AUTH_CONST.__auth_ptr: 0xa30
+  __AUTH_CONST.__auth_ptr: 0xa28
   __AUTH_CONST.__const: 0x1d38
   __AUTH_CONST.__cfstring: 0x2a40
   __AUTH_CONST.__objc_const: 0x12458

```


</details>

## EOF
