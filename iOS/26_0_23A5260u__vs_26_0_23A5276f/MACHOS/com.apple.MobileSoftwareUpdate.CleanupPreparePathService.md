## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2422.0.15.0.2
-  __TEXT.__text: 0x27d30
-  __TEXT.__auth_stubs: 0x1610
-  __TEXT.__objc_stubs: 0x3700
-  __TEXT.__objc_methlist: 0x1684
-  __TEXT.__cstring: 0x104b3
+2422.0.31.502.1
+  __TEXT.__text: 0x286c4
+  __TEXT.__auth_stubs: 0x1620
+  __TEXT.__objc_stubs: 0x3760
+  __TEXT.__objc_methlist: 0x16fc
+  __TEXT.__cstring: 0x105cb
   __TEXT.__const: 0x1220
   __TEXT.__oslogstring: 0x1c6
-  __TEXT.__gcc_except_tab: 0x474
+  __TEXT.__gcc_except_tab: 0x4c8
   __TEXT.__objc_classname: 0x1b8
-  __TEXT.__objc_methname: 0x3a82
+  __TEXT.__objc_methname: 0x3b5d
   __TEXT.__objc_methtype: 0xdfc
-  __TEXT.__unwind_info: 0x8a8
-  __DATA_CONST.__auth_got: 0xb18
+  __TEXT.__unwind_info: 0x8f0
+  __DATA_CONST.__auth_got: 0xb20
   __DATA_CONST.__got: 0x2e8
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x1460
-  __DATA_CONST.__cfstring: 0x9c40
+  __DATA_CONST.__cfstring: 0x9c80
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x1ee0
-  __DATA.__objc_selrefs: 0x1108
-  __DATA.__objc_ivar: 0x160
+  __DATA.__objc_const: 0x1f70
+  __DATA.__objc_selrefs: 0x1140
+  __DATA.__objc_ivar: 0x16c
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x4d8
   __DATA.__bss: 0x650

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: EE03602C-BC2F-31E3-A8F1-BC3B1954056F
-  Functions: 770
-  Symbols:   5627
-  CStrings:  4090
+  UUID: 2F59DF14-DD6F-3E59-8F95-A2632D388DAB
+  Functions: 791
+  Symbols:   5742
+  CStrings:  4113
 
Symbols:
+ -[MSUCheckpointAsyncBlockContext cancel]
+ -[MSUCheckpointAsyncBlockContext isCanceled]
+ -[MSUCheckpointAsyncBlockContext setAwaitDescription:]
+ -[MSUCheckpointAsyncBlockContext setIsCanceled:]
+ -[MSUCheckpointAsyncBlockContext setStepDescription:]
+ -[MSUCheckpointAsyncContext awaitDescription]
+ -[MSUCheckpointAsyncContext cancel]
+ -[MSUCheckpointAsyncContext setAwaitDescription:]
+ -[MSUCheckpointAsyncContext setStepDescription:]
+ -[MSUCheckpointAsyncContext stepDescription]
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/4~B3ZaugAxEBw_BtYPBYieCAioOZgwuCroMbSNtkA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ GCC_except_table10
+ GCC_except_table9
+ OBJC_IVAR_$_MSUCheckpointAsyncBlockContext._isCanceled
+ OBJC_IVAR_$_MSUCheckpointAsyncContext._awaitDescription
+ OBJC_IVAR_$_MSUCheckpointAsyncContext._stepDescription
+ ___assert_rtn
+ _checkpoint_chassis_set_global_async_error
+ _checkpoint_closure_context_set_encountered_async_error
+ _checkpoint_engine_cancel
+ _checkpoint_engine_set_async_error
+ _checkpoint_error_copy_canceled_error
+ _checkpoint_error_is_cancel_error
+ _checkpoint_tolerated_get_failed_entry
+ _checkpoint_tolerated_treat_as_success_minimized
+ _objc_msgSend$cancel
+ _objc_msgSend$isCanceled
+ _objc_msgSend$setIsCanceled:
+ _ramrod_should_do_legacy_restored_internal_behaviors
+ checkpoint_chassis_set_global_async_error.cold.1
+ checkpoint_engine_set_async_error.cold.1
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
CStrings:
+ "CHECKPOINT_INTERNAL_ERROR(%s): unable to create step ID number for tolerated failure lookup\n"
+ "CheckpointEngineErrorDomain"
+ "TB,V_isCanceled"
+ "T^v,N,V_awaitDescription"
+ "T^v,N,V_stepDescription"
+ "_awaitDescription"
+ "_isCanceled"
+ "_stepDescription"
+ "awaitDescription"
+ "cancel"
+ "checkpoint_chassis_set_global_async_error"
+ "checkpoint_engine_set_async_error"
+ "checkpoint_tolerated_get_failed_entry"
+ "failingStep"
+ "isCanceled"
+ "ramrod_checkpoint.c"
+ "setAwaitDescription:"
+ "setIsCanceled:"
+ "setStepDescription:"
+ "stepDescription"
+ "supplemental"

```
