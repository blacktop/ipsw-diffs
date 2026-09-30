## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2422.60.14.0.2
-  __TEXT.__text: 0x293a8
+2422.80.7.0.0
+  __TEXT.__text: 0x293e4
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0x3740
-  __TEXT.__objc_methlist: 0x172c
+  __TEXT.__objc_stubs: 0x3780
+  __TEXT.__objc_methlist: 0x1744
   __TEXT.__cstring: 0x11117
   __TEXT.__const: 0x1220
   __TEXT.__oslogstring: 0x1c6
   __TEXT.__gcc_except_tab: 0x4c8
   __TEXT.__objc_classname: 0x1b8
-  __TEXT.__objc_methname: 0x3bac
+  __TEXT.__objc_methname: 0x3c0e
   __TEXT.__objc_methtype: 0xe11
   __TEXT.__unwind_info: 0x910
   __DATA_CONST.__auth_got: 0xb38

   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0x1f70
-  __DATA.__objc_selrefs: 0x1150
-  __DATA.__objc_ivar: 0x16c
+  __DATA.__objc_const: 0x1fa0
+  __DATA.__objc_selrefs: 0x1160
+  __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x660

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: 68C1DCE2-7439-3946-9261-9766F1FA3261
-  Functions: 802
-  Symbols:   5807
-  CStrings:  4232
+  UUID: 1B986472-79D0-3F0F-A601-2288493BE75E
+  Functions: 804
+  Symbols:   5820
+  CStrings:  4236
 
Symbols:
+ -[MSUCheckpointAsyncBlockContext reportErrorsOutOfBand]
+ -[MSUCheckpointAsyncBlockContext setReportErrorsOutOfBand:]
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/4~CEEgugDKFHRvpGFRtEfjxHZbwrkwtrkFG6Gxd0g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ OBJC_IVAR_$_MSUCheckpointAsyncBlockContext._reportErrorsOutOfBand
+ _objc_msgSend$reportErrorsOutOfBand
+ _objc_msgSend$setReportErrorsOutOfBand:
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/4~CCm1ugAAkEr0bS15MSUhAmEqyIlbjrCkhX_4mkE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
Functions:
~ -[MSUCheckpointAsyncBlockContext initWithQueue:block:] : 276 -> 288
~ ___54-[MSUCheckpointAsyncBlockContext initWithQueue:block:]_block_invoke : 632 -> 644
+ -[MSUCheckpointAsyncBlockContext reportErrorsOutOfBand]
+ -[MSUCheckpointAsyncBlockContext workQueue]
CStrings:
+ "TB,V_reportErrorsOutOfBand"
+ "_reportErrorsOutOfBand"
+ "reportErrorsOutOfBand"
+ "setReportErrorsOutOfBand:"

```
