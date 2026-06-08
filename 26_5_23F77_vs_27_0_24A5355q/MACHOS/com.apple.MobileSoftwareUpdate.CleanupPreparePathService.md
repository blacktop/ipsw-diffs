## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2422.120.23.0.9
-  __TEXT.__text: 0x290c4
+2717.0.0.0.0
+  __TEXT.__text: 0x291f4
   __TEXT.__auth_stubs: 0x1650
   __TEXT.__objc_stubs: 0x3780
-  __TEXT.__objc_methlist: 0x16fc
-  __TEXT.__cstring: 0x1107b
+  __TEXT.__objc_methlist: 0x1714
+  __TEXT.__cstring: 0x11181
   __TEXT.__const: 0x1218
   __TEXT.__oslogstring: 0x1c6
-  __TEXT.__gcc_except_tab: 0x598
-  __TEXT.__objc_classname: 0x1b8
-  __TEXT.__objc_methname: 0x3c0a
-  __TEXT.__objc_methtype: 0xe11
-  __TEXT.__unwind_info: 0x908
-  __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x14b0
-  __DATA_CONST.__cfstring: 0xa3c0
+  __TEXT.__gcc_except_tab: 0x540
+  __TEXT.__objc_methname: 0x3c3b
+  __TEXT.__objc_classname: 0x1b7
+  __TEXT.__objc_methtype: 0xe04
+  __TEXT.__unwind_info: 0x8e8
+  __DATA_CONST.__const: 0x14c8
+  __DATA_CONST.__cfstring: 0xa560
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arraydata: 0x150
   __DATA_CONST.__objc_arrayobj: 0x78
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0xb38
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x1fa0
-  __DATA.__objc_selrefs: 0x1158
+  __DATA.__objc_selrefs: 0x1168
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x4e0
-  __DATA.__bss: 0x660
+  __DATA.__bss: 0x6a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: 8844625F-9DB4-3686-A83E-29CB04F9DA9D
-  Functions: 817
-  Symbols:   5898
-  CStrings:  4242
+  UUID: D8690DFF-E6FB-31EC-870D-DFB96F1FF3E6
+  Functions: 814
+  Symbols:   5897
+  CStrings:  4273
 
Symbols:
+ +[MSUBootFirmwareUpdater supportsProvisionalNonces]
+ +[MSUBootFirmwareUpdater supportsiBootPrecommit]
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/4~CQ9SugCPTN6_BO9PevvqF8drbUIRC6J4Z6cj1q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUApplicationManager.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUAssetStager.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUCFHelpers.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUError.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUFreeSpaceManager.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSULogAnnotatedSum.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUPerformanceUtils.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUResultState.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MobileSoftwareUpdateConstants.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MobileSoftwareUpdatePreferences.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/NeRDSPI.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/SupportDirectory.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/baseband_ticket_lock.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/cleanup_prepare_path_handlers.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/cleanup_prepare_path_service.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/clientServerIPC.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-0c80cd7ca0968eae472db6188f9f093a.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-2b4a293d7b1650dc3108bc546d2cd37d.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/log.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/msu_log.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/msu_nvram.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/restore_log.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Sources/MobileSoftwareUpdate/
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Sources/MobileSoftwareUpdate/CleanupPreparePathService/
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUAssetStager/
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUBrain/
+ /Library/Caches/com.apple.xbs/5DC89B65-76D3-4BA4-8C90-771CDA92F2A3/TemporaryDirectory.334OEt/Sources/UpdateMetrics/UpdateMetrics/
+ /Library/Caches/com.apple.xbs/63EA7F73-24CA-4FFF-9299-E066706F6743/TemporaryDirectory.oDpNrv/Sources/PurpleRestore_libpartition/libusbrestore/
+ /Library/Caches/com.apple.xbs/63EA7F73-24CA-4FFF-9299-E066706F6743/TemporaryDirectory.oDpNrv/Sources/PurpleRestore_libpartition/ramrod/
+ /Library/Caches/com.apple.xbs/BF80E684-E72D-499C-8E59-6FB586E88B10/TemporaryDirectory.yzxo8o/Sources/ramrod/MSUBootFirmwareUpdater/
+ /Library/Caches/com.apple.xbs/BF80E684-E72D-499C-8E59-6FB586E88B10/TemporaryDirectory.yzxo8o/Sources/ramrod/ramrod/
+ /Library/Caches/com.apple.xbs/BF80E684-E72D-499C-8E59-6FB586E88B10/TemporaryDirectory.yzxo8o/Sources/ramrod/restored/AsyncCheckpoint/
+ GCC_except_table26
+ MSUCFHelpers.m
+ MSUError.m
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _apfs_container_physical_device_store
+ _format_partition_with_size
+ _hardware_device_node_path
+ _objc_claimAutoreleasedReturnValue
+ _strncpy
- -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.9
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/4~COBwugCGBscE-aZZq9FlcgyNyrN9YsUR9rakZto/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUApplicationManager.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUAssetStager.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUFreeSpaceManager.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSULogAnnotatedSum.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUPerformanceUtils.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUResultState.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MobileSoftwareUpdateConstants.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MobileSoftwareUpdatePreferences.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/NeRDSPI.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/SupportDirectory.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/baseband_ticket_lock.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/cleanup_prepare_path_handlers.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/cleanup_prepare_path_service.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/clientServerIPC.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-34767206e963cf1da2f356957140033e.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-79c044016285f515bb7ce88edb32427b.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/log.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/msu_log.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/msu_nvram.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/restore_log.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Sources/MobileSoftwareUpdate/
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Sources/MobileSoftwareUpdate/CleanupPreparePathService/
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUAssetStager/
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUBrain/
- /Library/Caches/com.apple.xbs/38935958-B363-4332-8EB1-E5B8F06DAD22/TemporaryDirectory.qF9DnN/Sources/PurpleRestore_libpartition/libusbrestore/
- /Library/Caches/com.apple.xbs/38935958-B363-4332-8EB1-E5B8F06DAD22/TemporaryDirectory.qF9DnN/Sources/PurpleRestore_libpartition/ramrod/
- /Library/Caches/com.apple.xbs/6D2805F2-5A47-40FF-8BFB-AC131DF12EA3/TemporaryDirectory.7s6YMA/Sources/ramrod/MSUBootFirmwareUpdater/
- /Library/Caches/com.apple.xbs/6D2805F2-5A47-40FF-8BFB-AC131DF12EA3/TemporaryDirectory.7s6YMA/Sources/ramrod/ramrod/
- /Library/Caches/com.apple.xbs/6D2805F2-5A47-40FF-8BFB-AC131DF12EA3/TemporaryDirectory.7s6YMA/Sources/ramrod/restored/AsyncCheckpoint/
- /Library/Caches/com.apple.xbs/D6B75F9C-57DD-400D-82BD-80EBB7BFF5CD/TemporaryDirectory.6TsiVz/Sources/UpdateMetrics/UpdateMetrics/
- GCC_except_table15
- GCC_except_table17
- GCC_except_table21
- GCC_except_table24
- GCC_except_table81
- ___NSArray0__
- _format_partition
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
CStrings:
+ "%lld"
+ "-s"
+ "B48@0:8*16^{__CFDictionary=}24@32^^{__CFError}40"
+ "BaseSystem"
+ "BaseSystem-arm64e"
+ "BaseSystem-x86-64"
+ "Cryptex1,AppOS"
+ "Cryptex1,RosettaOS"
+ "Cryptex1,SystemOS"
+ "DiagnosticsSupport"
+ "Loaded plist but is type is not expected type.\n"
+ "cryptex-system-rosetta"
+ "nerd-erase-allowed"
+ "nerd-erase-in-progress"
+ "snap-provisional-nonces"
+ "snap-supports-precommit"
+ "supportsProvisionalNonces"
+ "supportsiBootPrecommit"
+ "x86,BaseSystem"
- "%s: segment_data_array failed to allocate"
- "B48@0:8*16^{__CFDictionary=}24r^^{__CFArray}32^^{__CFError}40"

```
