## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2082.80.3.0.0
-  __TEXT.__text: 0x343a8
+2082.80.5.0.0
+  __TEXT.__text: 0x34404
   __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_stubs: 0x3e60
-  __TEXT.__objc_methlist: 0x1970
-  __TEXT.__cstring: 0x1106f
+  __TEXT.__objc_stubs: 0x3e80
+  __TEXT.__objc_methlist: 0x1980
+  __TEXT.__cstring: 0x11091
   __TEXT.__const: 0x1358
   __TEXT.__oslogstring: 0x13c8
   __TEXT.__gcc_except_tab: 0x4a8
   __TEXT.__objc_classname: 0x219
-  __TEXT.__objc_methname: 0x420f
+  __TEXT.__objc_methname: 0x420e
   __TEXT.__objc_methtype: 0xe54
-  __TEXT.__unwind_info: 0xa30
+  __TEXT.__unwind_info: 0xa38
   __DATA_CONST.__auth_got: 0xc38
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x1868
-  __DATA_CONST.__cfstring: 0xa5e0
+  __DATA_CONST.__const: 0x1888
+  __DATA_CONST.__cfstring: 0xa600
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x2608
-  __DATA.__objc_selrefs: 0x12e8
-  __DATA.__objc_ivar: 0x164
+  __DATA.__objc_const: 0x25e8
+  __DATA.__objc_selrefs: 0x12f0
+  __DATA.__objc_ivar: 0x160
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x588
-  __DATA.__bss: 0x6a8
+  __DATA.__bss: 0x6b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 855
-  Symbols:   6380
-  CStrings:  3176
+  Functions: 857
+  Symbols:   6396
+  CStrings:  3177
 
Symbols:
+ +[UMEventRecorder submitQueue]
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer_Private.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhyscialStore_Private.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhysicalStore.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume_Private.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPIOKitHelper.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPLog.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPMedia.o)
+ /AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPPartitionMedia.o)
+ GCC_except_table39
+ __56-[UMEventRecorder submitEventsInBackground:withOptions:]_block_invoke.711
+ ___30+[UMEventRecorder submitQueue]_block_invoke
+ __block_literal_global.179
+ _objc_msgSend$submitQueue
+ submitQueue.once
+ submitQueue.submit_queue
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer_Private.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhyscialStore_Private.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhysicalStore.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume_Private.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPIOKitHelper.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPLog.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPMedia.o)
- /AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPPartitionMedia.o)
- GCC_except_table37
- OBJC_IVAR_$_UMEventRecorder._submitQueue
- __56-[UMEventRecorder submitEventsInBackground:withOptions:]_block_invoke.706
CStrings:
+ "initializing new submission queue"
+ "submitQueue"
- "_submitQueue"

```
