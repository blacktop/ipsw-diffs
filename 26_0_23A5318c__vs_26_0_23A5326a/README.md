# 26.0 (23A5318c) .vs 26.0 (23A5326a)

## IPSWs

- `iPhone17,1_26.0_23A5318c_Restore.ipsw`
- `iPhone17,1_26.0_23A5326a_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.0 *(23A5318c)* | 25.0.0 | 12377.2.6~4 | Tue, 05Aug2025 22:37:43 PDT |
| 26.0 *(23A5326a)* | 25.0.0 | 12377.2.7~9 | Fri, 15Aug2025 00:02:28 PDT |

### Kexts

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.AppleH16ANEInterface

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-9.15.0.0.0
+9.15.2.0.0
   __TEXT.__const: 0xab8
   __TEXT.__cstring: 0xedd3
-  __TEXT.__os_log: 0x355af
-  __TEXT_EXEC.__text: 0x1051f4
+  __TEXT.__os_log: 0x35763
+  __TEXT_EXEC.__text: 0x1054d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3a7c
   __DATA.__common: 0x658

   __DATA_CONST.__const: 0xc278
   __DATA_CONST.__kalloc_type: 0x3b40
   __DATA_CONST.__kalloc_var: 0x3160
-  UUID: 1D89ECCD-B25E-30BE-AC79-E7B323615553
+  UUID: 3D8395EB-278F-3127-B9C4-D99BE5BCAA12
   Functions: 3286
   Symbols:   0
-  CStrings:  4300
+  CStrings:  4304
 
Functions:
~ __ZN11ANEHWDevice12ProcessAbortEP10ANEProcessPvb : 4256 -> 4336
~ __ZN11ANEHWDevice40ANE_ProgramPrepareAndSubmitRequest_gatedEP21ANEProgramRequestArgsP15ANESharedEventsP37ANEProgramSendRequestAdditionalParams : 14876 -> 15384
~ __ZN11ANEResource4wireEj : 1260 -> 1320
~ __ZN11ANEHWDevice34GetTotalWiredMemoryImpactForClientEPK16ANEClientContext : 784 -> 868
CStrings:
+ "[ERROR] %s: %s: programId: %d, processId: %d, transactionId: 0x%llx, process aborted while aneCmdSend\n"
+ "[ERROR] %s: %s: programId: %d, processId: %d, transactionId: 0x%llx, process aborted while blocked on Fences\n"
+ "[ERROR] %s: %s: programId: %d, processId: %d, transactionId: 0x%llx, process aborted while ungated wiring\n"
+ "[INFO] %s: %s: skip async ref signal for now programid=%d request_uuid=%llx asyncRef=0x%llx programResource=0x%llx\n"

```

#### com.apple.driver.IOPAudioVoiceTriggerDevice

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 500.14.0.0.0
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x2d80
+  __TEXT.__cstring: 0x2d89
   __TEXT.__os_log: 0x1726
   __TEXT_EXEC.__text: 0xb108
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1750
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: E479C83D-8A7D-3691-80F3-E6CBF47F99D5
+  UUID: 6FB89CDF-02C5-38E4-BD1E-A44C2ED998B6
   Functions: 260
   Symbols:   0
-  CStrings:  235
+  CStrings:  236
 
CStrings:
+ "00:33:05"
+ "00:33:06"
+ "Aug 15 2025"
- "20:59:11"
- "Aug  7 2025"

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

 2632.2.1.0.0
   __TEXT.__const: 0xa18
-  __TEXT.__cstring: 0x4c596
+  __TEXT.__cstring: 0x4c59f
   __TEXT_EXEC.__text: 0x159a78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x640

   __DATA_CONST.__kalloc_type: 0x4f00
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: BDEED075-6587-305A-84F5-07E407179EAA
+  UUID: 3E2A9BDF-4573-30D8-94D2-F12FDDCC422F
   Functions: 2319
   Symbols:   0
-  CStrings:  6589
+  CStrings:  6590
 
CStrings:
+ "2025/08/14"
+ "23:44:47"
+ "23:44:48"
+ "Aug 14 2025"
- "2025/08/05"
- "22:05:34"
- "Aug  5 2025"

```


</details>

## MachO

### ❌ Removed (4)

- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LogArchiveDiagnosticExtension.appex/LogArchiveDiagnosticExtension`

### ⬆️ Updated (67)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AVKitRoutingService.app/AVKitRoutingService](MACHOS/AVKitRoutingService.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/DockFolderViewService.app/DockFolderViewService](MACHOS/DockFolderViewService.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/ScreenTimeUnlock.app/ScreenTimeUnlock](MACHOS/ScreenTimeUnlock.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/ControlCenter/Bundles/RPControlCenterModuleHQLR.bundle/RPControlCenterModuleHQLR](MACHOS/RPControlCenterModuleHQLR.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PrivateFrameworks/ACTFramework.framework/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/default-binaryarchive.metallib](MACHOS/default-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/mxi-binaryarchive.metallib](MACHOS/mxi-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd](MACHOS/recentsd.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Reconstruction_Gpu_Archive.metallib](MACHOS/Reconstruction_Gpu_Archive.metallib.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd](MACHOS/systemstatusd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/metal_libraries/binary.metallib](MACHOS/binary.metallib.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeEnabledNotifications.bundle/com.apple.ScreenTimeEnabledNotifications](MACHOS/com.apple.ScreenTimeEnabledNotifications.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/MattingV2.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/VideoDeghostingV3.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/Photos.app/Photos](MACHOS/Photos.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsActions.framework/PodcastsActions](MACHOS/PodcastsActions.md)
- [/usr/libexec/captiveagent](MACHOS/captiveagent.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/ospredictiond](MACHOS/ospredictiond.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### adc-rheia-d9x.im4p

>  `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0xabdda0
-  __TEXT.__const: 0x9b4ab0
+  __TEXT.__text: 0xabe21c
+  __TEXT.__const: 0x9b4a78
   __TEXT.text_env: 0x4f1a4
-  __TEXT.__cstring: 0xa653d
+  __TEXT.__cstring: 0xa6572
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0xcbc

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x5ae400
-  UUID: 90133F05-E159-37D6-ACAF-39874E21684E
+  UUID: F0481F2A-8048-3AA5-BA4F-36AFBEC5EAC9
   Functions: 9175
   Symbols:   0
-  CStrings:  18210
+  CStrings:  18212
 
CStrings:
+ "23:51:14"
+ "Aug 14 2025"
+ "LCDRV Ch%d AF Target = %f um, Current Pos = %f, APS Reading = %d\n"
+ "ch %zu fc %d pMetaDataBufPrev is null"
- "23:15:51"
- "[%f] ch %zu PrimarySrcDone Received when IC not streaming [%f]"

```

#### h17_ane_fw_theia_d9x.im4p

>  `h17_ane_fw_theia_d9x.im4p`

```diff

 
-  __TEXT.__text: 0xc3b3c
-  __TEXT.__cstring: 0x1ccb9
-  __TEXT.__const: 0x421c
+  __TEXT.__text: 0xa21fc
+  __TEXT.__cstring: 0x14b9f
+  __TEXT.__const: 0x4208
   __TEXT.ce_env: 0x4000
   __TEXT.text_env: 0x20
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x9d58
+  __DATA.__const: 0x9d18
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0x1080
+  __DATA.__data: 0xe80
   __DATA._rtk_power: 0x3b8
   __DATA._rtk_patchbay: 0x261
   __DATA._rtk_init_stack: 0x10000

   __DATA.__sysvars: 0x4
   __DATA.__mod_init_func: 0x0
   __DATA.__chain_starts: 0x24
-  __DATA.__zerofill: 0x1c1f00
-  UUID: A1BB6CA0-D437-31B0-8E82-04B09317BE80
-  Functions: 1531
+  __DATA.__zerofill: 0x1edf00
+  UUID: 1CC96A76-0BF0-3244-A09D-70A42D646B81
+  Functions: 1422
   Symbols:   0
-  CStrings:  3436
+  CStrings:  2339
 
CStrings:
+ "%s .Sanity check failure!\n"
+ "20:45:24"
+ "Aug 10 2025"
+ "Couldn't find ShareMemInfoItem to free !!!\n"
+ "IPC Endpoint cmd failed %d"
+ "IPC Endpoint cmd failure"
+ "Procedure %d exceeded maximum for program %d"
+ "Run out of CSharedMemory !!!\n"
+ "pProc != __null"
+ "pProg != __null"
+ "unremap WriteMessage failed\n"
- "\tFW Latency Signposts 0x%x id 0x%x ts %lld"
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
- "./ffw/ffw/CBuffer.cpp"
- "./ffw/ffw/CBufferPool.cpp"
- "./ffw/ffw/CBufferPoolStatic.cpp"
- "./ffw/ffw/CChannelManager.cpp"
- "./ffw/ffw/CController.cpp"
- "./ffw/ffw/CExpandablePool.cpp"
- "./ffw/ffw/CFifo.cpp"
- "./ffw/ffw/CFilter.cpp"
- "./ffw/ffw/CGPIOManager.cpp"
- "./ffw/ffw/CHashTable.cpp"
- "./ffw/ffw/CIPSynchro.cpp"
- "./ffw/ffw/CInterruptBuffer.cpp"
- "./ffw/ffw/CLatencyProfiler.cpp"
- "./ffw/ffw/CList.cpp"
- "./ffw/ffw/CLoggerInterProcessor.cpp"
- "./ffw/ffw/CLoggerSharedBuffer.cpp"
- "./ffw/ffw/CMMU.cpp"
- "./ffw/ffw/CMMULoggerPA.cpp"
- "./ffw/ffw/CMMULoggerVA.cpp"
- "./ffw/ffw/CMultiFilter.cpp"
- "./ffw/ffw/CObject.cpp"
- "./ffw/ffw/CObjectTree.cpp"
- "./ffw/ffw/CPipe.cpp"
- "./ffw/ffw/CPool.cpp"
- "./ffw/ffw/CRoot.cpp"
- "./ffw/ffw/CSharedMemory.cpp"
- "./ffw/ffw/CSignalPool.cpp"
- "./ffw/ffw/CTerminalOut.cpp"
- "./ffw/ffw/CTimeProfiler.cpp"
- "./ffw/ffw/ffwCRC.cpp"
- "./ffw/ffw/rtkit/CDebugAgent.cpp"
- "./ffw/ffw/rtkit/CEnvironment.cpp"
- "./ffw/ffw/rtkit/CISRManager.cpp"
- "./ffw/ffw/rtkit/CMailboxPool.cpp"
- "./ffw/ffw/rtkit/CQueuePool.cpp"
- "./ffw/ffw/rtkit/CRTOSObjectPool.cpp"
- "./ffw/ffw/rtkit/CResourcePool.cpp"
- "./ffw/ffw/rtkit/CScopedLock.cpp"
- "./ffw/ffw/rtkit/CSemaphorePool.cpp"
- "./ffw/ffw/rtkit/CSharedMemoryHeap.cpp"
- "./ffw/ffw/rtkit/CSharedMemoryHost.cpp"
- "./ffw/ffw/rtkit/CTaskPool.cpp"
- "./ffw/ffw/rtkit/CTimerManager.cpp"
- "./ffw/ffw/rtkit/CTimerPool.cpp"
- "./ffw/ffw/rtkit/CTraceEventBuffer.cpp"
- "./ffw/ffw/rtkit/ffwSharedMemory.cpp"
- "./ffw/platform/common/CFakeChannel.cpp"
- "./ffw/platform/common/CIPSynchroFake.cpp"
- "./ffw/platform/common/ChannelTable.cpp"
- "./ffw/platform/common/FakeChannelTable.cpp"
- "./ffw/platform/theia/rtkit/CPlatformEnvironment.cpp"
- "./ffw/platform/theia/rtkit/CPlatformGPIOManager.cpp"
- "./ffw/platform/theia/rtkit/CPlatformISRManager.cpp"
- "./ffw/platform/theia/rtkit/RealChannelTableTarget.cpp"
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
- "00:54:54"
- "1"
- "<=== CMMU_LOGGER_FFW_ASSERT from %s\n"
- "================="
- "===> CMMU_LOGGER_FFW_ASSERT from %s\n"
- ">>>>>>> Frame ID mismatch, expect: %lld, get: %lld"
- "ACK \"%s\""
- "ACTION"
- "AFPP load is not allowed after program setup done\n"
- "ALIGN_DOWN(pointer, CMMU::CacheLineSize()) == pointer"
- "ALL_CPU(%)"
- "ANE latency profiler already exists"
- "ANE latency profiler created"
- "ANE requestCallProc %zu"
- "ANE_PROPERTY_PRC Channel related logs are disabled"
- "ANE_PROPERTY_PRC Channel related logs are enabled"
- "ANE_PROPERTY_PRC wrong valid"
- "AddScheduleInfo"
- "AneVersionGet"
- "Aug  4 2025"
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
- "CmdReqProcessId"
- "CmdReqProgramId"
- "CmdResetNotification"
- "CmdReturnProcessId"
- "CmdReturnProgramId"
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
- "DeleteRTGraphProgram"
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
- "Entry %d"
- "Event %d nbrUsrD %d 22"
- "Event stats: perf debug event %d dropped for NID %d TID %d due to overflow."
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
- "GetFirstHWRunningSlot"
- "GetPowerStatus"
- "GetProcInfo"
- "GetProgInfo"
- "GetTraceBuffer"
- "H11ISPInterruptMapping[(size_t)aispSource]->platformIntSrc != PLATFORM_INT_INVALID"
- "H17TunableManager"
- "HandleEventInt"
- "HandleMcwInt"
- "HandleStopTqInt"
- "Hash Node %lld"
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
- "InitProgrm"
- "Initialization"
- "InqTaskArg"
- "Invalid log operation"
- "IpcEndpointSet"
- "IpcEndpointUnset"
- "Kernel : bufferIndex %d"
- "Key[%lld]: 0x%zx"
- "KickStartCe"
- "Load %s failed"
- "LoadProgram"
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
- "Notify score %u\n"
- "Overflow detected in dram event log: programId %d processId %d procedureId %d"
- "POST CONDITION: "
- "POWEROFF"
- "POWERON"
- "PRE CONDITION: "
- "PROCESSING"
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
- "RTK_ST_OK == ret"
- "RTK_queue_count(queue) == tot"
- "RTK_vm_map_memory failed for 0x%llx length 0x%zu\n"
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
- "Secure mode switch handshake time %dus"
- "Segment : bufferIndex %d"
- "SendBufMsg"
- "SendCall"
- "SendHWRequest"
- "SendMsg : endPointId %d sapId 0x%x subPacket %p subPacketSize %d\n"
- "SendSecureModeEvent"
- "SendSecureModeRequest"
- "SetPMUBaseAddress"
- "SetProgram"
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
- "TQ[%d] State %d set at %lld by %s:%d"
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
- "UnMapTextSection"
- "UnRemap :  handle 0x%x : base : %p len : 0x%lx\n"
- "UnloadProgram"
- "UnsetMem : %p 0x%lx 0x%x\n"
- "UnsetRemap : %p 0x%lx 0x%x\n"
- "WireShared"
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
- "[AneCmd] Allocated processId %d for programId %d at %lld.\n"
- "[AneCmd] Allocated programId = %d at %lld"
- "[AneCmd] Allocated programId = %d at %lld."
- "[AneCmd] Returned programId = %d at %lld."
- "[AneCmd] Terminated processId %d for programId %d at %lld"
- "[AneCmd] Unloaded programId = %d at %lld"
- "[AneCmd] returned processId %d for programId %d at %lld."
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
- "appPriorityToFwPriority"
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
- "cachedAddr != 0"
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
- "checkRunningSlotsAfterAbort"
- "checkpointId < mMaxCheckpoints"
- "clear output buf[%d] 0x%llx size %lld"
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
- "dummy return\n"
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
- "getFileSize"
- "getL2SpillBufferAddr"
- "getNbrOfTd"
- "getNetworkDescBufAddr"
- "getProcedureCallType"
- "getRequestId"
- "getReservedNetworkDesc"
- "getSeg1stTd_RTGraphH13"
- "gpTimerArray != 0"
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
- "handleInferenceCall_inThread"
- "handleInvalidSingleUseCacheRequest"
- "handleIpcEndpointCmd"
- "handlePendingCmd"
- "handleStats"
- "handleSwitchedOutReq"
- "handler == memHandler"
- "handshake_info != NULL"
- "hashNodeIdxMutex != (FFWMUTEX)0"
- "hash_table_size > 0"
- "head == 0"
- "heapSize != 0"
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
- "info"
- "initDbgEventMem"
- "initPSDLibService"
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
- "isCacheReqSingleUse"
- "isCacheReqValid"
- "isHWReady"
- "isHWReady_myHwq"
- "isHWReady_pairedHwq"
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
- "mLatencyStat.pCheckpoint[i]"
- "mLatencyStat.pLatency"
- "mLatencyStat.pLatency[i]"
- "mMaxCheckpoints > 0"
- "mMutex != (RESOURCE)0"
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
- "nbrOfRemapLeft == endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem"
- "needHWAbortTQandCleanUp"
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
- "printEnqueueHwqInfo"
- "printInfo"
- "printStats"
- "printTQState"
- "priority != 0"
- "priority <= RTK_THREAD_PRIORITY_MAX"
- "priority >= RTK_THREAD_PRIORITY_MIN"
- "processCmdOnly == true"
- "processedCmdCounter == 0"
- "prog.tdProp.buf %p procValid %d"
- "programId 0x%x processId 0x%x nbrAneMapping %d"
- "programId 0x%x processId 0x%x procedureId 0x%x"
- "propertyWrite"
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
- "reportDataChainingTriggerFailed"
- "reportFinishEvent"
- "resPool != 0"
- "resPool == 0"
- "reset"
- "ret == 0"
- "retain"
- "retain == CBuffer::suspended"
- "retainL2SpillBufferIdx"
- "returnRequestId"
- "rtkitSystemTaskList != 0"
- "sCSneCmdProcedureCall [%d] : bufferIndex %d"
- "saveSwitchedOutReq"
- "saveToFile"
- "scheduleAneReq"
- "sema != 0"
- "sema != NULL"
- "sema == 0"
- "semaArray != (SEMA *)0"
- "semaArray[index] != (SEMA)0"
- "semaPool != 0"
- "semaPool == 0"
- "semaphore == (SEMA)0"
- "semaphore == h->signalT2H"
- "sendEnqueueEvt_prepareFinishEvt_inIsr"
- "serialPollTimer[i] != 0"
- "serialPortPoolTimeOut[i] != (SEMA)0"
- "serialPortSignal[i] != (SEMA)0"
- "set buf[%d] 0x%llx zero sz %lld"
- "setActiveCacheRequestInGroup"
- "setCustomBars"
- "setDataChainingLatencyDisp"
- "setDataChainingLatencyDisp %d"
- "setDirectAneRequestInfo"
- "setEnableDynamicPowerGate"
- "setForceDisableCacheRequest"
- "setInitFlags"
- "setJobQueueId"
- "setOtherTqState"
- "setPerfMode"
- "setResetMode"
- "setResetMode %d"
- "setStartTimestamp"
- "setTQPriority"
- "setTQState"
- "setTaskSwitchEventDisp"
- "setTaskSwitchEventDisp %d"
- "setupAneReq_inIsr"
- "setupCacheRequest"
- "setupDirectProcCallEvents"
- "setupEngineReq"
- "setupEngineReqInternal"
- "setupEngineReqStatsBuffer"
- "setupNetworkDescriptor_withBars"
- "shAddr != NULL"
- "sharedEventsTrigger"
- "sharedEventsTriggerIsr"
- "sharedMem != 0"
- "shwdStatus == 0"
- "sigPool == 0"
- "signal != 0"
- "signalH2T != 0"
- "signalNonSec2SecSema"
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
- "tqEnqueueReq_inIsr"
- "tree_resource != (FFWMUTEX)0"
- "tree_resource != 0"
- "tryPushToHw_fromFwPriorityQ"
- "updateDefSetting"
- "updateEngineRequestSegment"
- "updateEngineRequestWithNextSegment"
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

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A5318c)* | iBoot-13822.2.9 |
| 26.0 *(23A5326a)* | iBoot-13822.2.12 |

#### 🆕 NEW (6)

<details>
  <summary><i>View NEW</i></summary>

##### `iboot`
  - `urppptpsqu0`
  - `2fb56e8d4b571585d38c5ce35d0046fb`
  - `FSUMTuUUUU`
  - `~cE#C;>D1*`
  - `!/CU\Is[x<o`
  - `root@4jrrf.p1l.plx.sd...2025/08/14@23:52:31`
  - `]PPTMF!*cO6`
  - `EMC'DG2Xm0`
  - `aƴ'Cŀel=`
  - `Y0gA)bnSf&2C`
  - `ctPɬ*>&iG`
  - `ER~-HKyr7F)`
  - `;m\l+]<@Hc`
  - `6ěc$/"x=%`
  - `lssssssss4n`
  - `ȿHrŐ6!r>$`
  - `4pH,,*rv2j7`
  - `lN3(![40@ov`
  - `F+£68Hr>=`
  - `⎀k7kT%MMqc`
  - `iBoot-13822.2.12`
  - `d}RoKY"y|c`
##### `iboot_blob05.bin`
  - `@yLIj9mNB9`
##### `iboot_blob30.bin`
  - `smc/bms/bms_v1/b`
##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-6164.2.11.d93.REL`
##### `iboot_blob29.bin`
  - `VKSPSSTSEW0`
  - `!C#C?CRCYx`
  - `PARADBCCECBDEDRECFDIGIRIONDSDURVfihiiiminisitpWx`
  - `ePAcAuADBIBACDCFCRCSCTCUCXCYCZCbCcCfCiCmCnCrCsCvCwCADBDEDIDPDRDpDCEFEpECFSFVFCIDIQIRIAJBJDJEJFJGJIJMJNJPJQJRJSJVJCLGLILRLIMPMVMIPMPRPSPTPdPiPsPtPcRpRTSWStSIUCVDVMVRVXVbVdVmVnVSWfihiiiminisiglilsodpiprptpW8`
  - `DD0E0H0J0R0V01A2AIASAIBVBCCECFCRCBDSFCHVHWH1I2IBICIEIFILIMIOISIDKGKHKKKLKMKOKPKQKRKSKUKVKWKSLTL2MCNDNINCOSPiQvQwQCRTRCSESLSTSWSCTETLTMTUTF`
##### `RTKit.bin`
  - `smc/bms/bms_v1/charger.cpp`
  - `vBMSTaskStop fail`
  - `Not charging:%llx`

</details>

#### ❌ Removed (5)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot_blob05.bin`
  - `@yLEj9mRB9`
##### `iboot`
  - `eAv4]>|N#Hg`
  - `E!?>dr9Lj&`
  - `61cd62a0752c2e0becd667889078c556`
  - `1IIIIIIIIIII!`
  - `@$E2Ƃ)f?B`
  - `4?tcb<8as'`
  - `=r0Emd|"\~`
  - `%q*ǀ1:?:q`
  - `-T!Z.jYh,LCŘ`
  - `⯖؆5$PL1@ZƢl`
  - `3@6Qu[iUdJ`
  - `I1enU)(4RG`
  - `iBoot-13822.2.9`
  - `j#I,k1)~@z`
  - `mCLy4s/[/F`
  - `root@krnww.p1l.plx.sd...2025/08/05@22:05:22`
  - `g"YQɲ߅h!`
  - `W_.v3B.-!K`
##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-6164.2.8.d93.REL`
##### `iboot_blob29.bin`
  - `!C#C?CRCYX`
  - `VKSPSSTSEW0>`
  - `ePAcAuADBIBACDCFCRCSCTCUCXCYCZCbCcCfCiCmCnCrCsCvCwCADBDEDIDPDRDpDCEFEpECFSFVFCIDIQIRIAJBJDJEJFJGJIJMJNJPJQJRJSJVJCLGLILRLIMPMVMIPMPRPSPTPdPiPsPtPcRpRTSWStSIUCVDVMVRVXVbVdVmVnVSWfihiiiminisiglilsodpiprptpW`
  - `PARADBCCECBDEDRECFDIGIRIONDSDURVfihiiiminisitpW\`
##### `iboot_blob30.bin`
  - `charger.cpp`
  - `vBMSTaskStop fail`
  - `smc/bms/bms_v1/`
  - `smc/bms/bms_v1/bms.cpp`
  - `Not charging:%llx`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A5318c)* | 622.1.22.10.4 |
| 26.0 *(23A5326a)* | 622.1.22.10.8 |

### Dylibs

#### ⬆️ Updated (100)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication](DYLIBS/AppleIDAuthentication.md)
- [/System/Library/CoreServices/RawCamera.bundle/RawCamera](DYLIBS/RawCamera.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AVKitSettings.bundle/AVKitSettings](DYLIBS/AVKitSettings.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI](DYLIBS/BaseBoardUI.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/CallsAppUI.framework/CallsAppUI](DYLIBS/CallsAppUI.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork](DYLIBS/CaptiveNetwork.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing](DYLIBS/ContinuitySing.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/FitnessIntelligence.framework/FitnessIntelligence](DYLIBS/FitnessIntelligence.md)
- [/System/Library/PrivateFrameworks/Fluid.framework/Fluid](DYLIBS/Fluid.md)
- [/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore](DYLIBS/GameServicesCore.md)
- [/System/Library/PrivateFrameworks/GameStoreKit.framework/GameStoreKit](DYLIBS/GameStoreKit.md)
- [/System/Library/PrivateFrameworks/HeadphoneCommonUIKit.framework/HeadphoneCommonUIKit](DYLIBS/HeadphoneCommonUIKit.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms](DYLIBS/HealthAlgorithms.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MapsDesign.framework/MapsDesign](DYLIBS/MapsDesign.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth](DYLIBS/RespiratoryHealth.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon](DYLIBS/RespiratoryHealthDaemon.md)
- [/System/Library/PrivateFrameworks/Scandium.framework/Scandium](DYLIBS/Scandium.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake](DYLIBS/SystemWake.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/libEDR.framework/libEDR](DYLIBS/libEDR.md)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport](DYLIBS/CaptiveNetworkSupport.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (29)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/Localizable-Windbreaker.loctable`
- `/System/Library/PreferencesSyncBundles/OxygenSaturationCompanionAnalysisPreferencesSyncPhone.bundle/Info.plist`
- `/System/Library/PreferencesSyncBundles/OxygenSaturationCompanionAnalysisPreferencesSyncPhone.bundle/_CodeSignature/CodeDirectory`
- `/System/Library/PreferencesSyncBundles/OxygenSaturationCompanionAnalysisPreferencesSyncPhone.bundle/_CodeSignature/CodeRequirements`
- `/System/Library/PreferencesSyncBundles/OxygenSaturationCompanionAnalysisPreferencesSyncPhone.bundle/_CodeSignature/CodeRequirements-1`
- `/System/Library/PreferencesSyncBundles/OxygenSaturationCompanionAnalysisPreferencesSyncPhone.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreferencesSyncBundles/OxygenSaturationCompanionAnalysisPreferencesSyncPhone.bundle/_CodeSignature/CodeSignature`
- `/System/Library/PrivateFrameworks/ActionButtonSelector.framework/Action_Button_glow_normal.png`
- `/System/Library/PrivateFrameworks/ActionButtonSelector.framework/Action_Button_glow_roughness.jpg`
- `/System/Library/PrivateFrameworks/ActionButtonSelector.framework/hero.heic`
- `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRadioPowerSwitch.xpc/InfoPlist.loctable`
- `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRestoreService.xpc/InfoPlist.loctable`
- `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/InfoPlist.loctable`
- `/System/Library/PrivateFrameworks/RespiratoryHealth.framework/Localizable-Windbreaker.loctable`
- `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/Localizable-Windbreaker.loctable`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-ar~iphone.mp4`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-en_IN~iphone.mp4`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-es_419~iphone.mp4`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-fr~iphone.mp4`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-he~iphone.mp4`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-ja~iphone.mp4`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-pt_BR~iphone.mp4`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-vi~iphone.mp4`
- `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/newFeaturesVideo-zh_CN~iphone.mp4`
- `/private/var/staged_system_apps/Bridge.app/DeviceAssets/2025`
- `/private/var/staged_system_apps/Bridge.app/DeviceAssets/WatchSideBySide-Illustrated-496h@2x.png`
- `/private/var/staged_system_apps/Bridge.app/DeviceAssets/WatchSideBySide-Illustrated-496h@3x.png`
- `/private/var/staged_system_apps/Bridge.app/DeviceAssets/WatchSideBySide-Illustrated-502h@2x.png`
- `/private/var/staged_system_apps/Bridge.app/DeviceAssets/WatchSideBySide-Illustrated-502h@3x.png`

</details>

### ❌ Removed

#### filesystem (22)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/Info.plist`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/_CodeSignature/CodeResources`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/Info.plist`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/_CodeSignature/CodeResources`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/Info.plist`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assetManifest.caml`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assets/BaseUILatest Copy 6.png`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assets/GM_Keyboard_Layering_BG2.jpg`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assets/mountain.jpg`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assets/pastedImage@2x 1.png`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assets/pastedImage@2x 2.png`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assets/pastedImage@2x.png`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assets/wp-mini.jpg`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/assets/xor@3x 2.png`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/index.xml`
- `/System/Library/PrivateFrameworks/CameraUI.framework/BuddyDemoLoop.ca/main.caml`
- `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI-VisualIntelligence.loctable`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LogArchiveDiagnosticExtension.appex/LogArchiveDiagnosticExtension`

</details>

## EOF
