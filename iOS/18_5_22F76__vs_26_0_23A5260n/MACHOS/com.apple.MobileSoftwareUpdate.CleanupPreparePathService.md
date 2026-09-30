## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2171.120.44.0.1
-  __TEXT.__text: 0x29188
-  __TEXT.__auth_stubs: 0x1680
-  __TEXT.__objc_stubs: 0x3740
-  __TEXT.__objc_methlist: 0x165c
-  __TEXT.__cstring: 0x10882
+2422.0.15.0.2
+  __TEXT.__text: 0x27d30
+  __TEXT.__auth_stubs: 0x1610
+  __TEXT.__objc_stubs: 0x3700
+  __TEXT.__objc_methlist: 0x1684
+  __TEXT.__cstring: 0x104b3
   __TEXT.__const: 0x1220
   __TEXT.__oslogstring: 0x1c6
   __TEXT.__gcc_except_tab: 0x474
-  __TEXT.__objc_classname: 0x1c7
-  __TEXT.__objc_methname: 0x3a33
-  __TEXT.__objc_methtype: 0xdef
-  __TEXT.__unwind_info: 0x8f8
-  __DATA_CONST.__auth_got: 0xb50
-  __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__auth_ptr: 0x30
+  __TEXT.__objc_classname: 0x1b8
+  __TEXT.__objc_methname: 0x3a82
+  __TEXT.__objc_methtype: 0xdfc
+  __TEXT.__unwind_info: 0x8a8
+  __DATA_CONST.__auth_got: 0xb18
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x1460
-  __DATA_CONST.__cfstring: 0x9fa0
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__cfstring: 0x9c40
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x1f50
-  __DATA.__objc_selrefs: 0x10d8
-  __DATA.__objc_ivar: 0x15c
-  __DATA.__objc_data: 0x6e0
+  __DATA.__objc_const: 0x1ee0
+  __DATA.__objc_selrefs: 0x1108
+  __DATA.__objc_ivar: 0x160
+  __DATA.__objc_data: 0x690
   __DATA.__data: 0x4d8
-  __DATA.__bss: 0x670
+  __DATA.__bss: 0x650
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: 40FF44BD-3463-3AC3-8AC6-73238D6AC545
-  Functions: 779
-  Symbols:   5715
-  CStrings:  4138
+  UUID: EE03602C-BC2F-31E3-A8F1-BC3B1954056F
+  Functions: 770
+  Symbols:   5627
+  CStrings:  4090
 
Symbols:
+ +[MSUBootFirmwareUpdater snapHasCombinedImages]
+ -[MSUCheckpointAsyncBlockContext waitUntilTime:]
+ -[MSUCheckpointAsyncContext waitUntilTime:]
+ -[MSUFreeSpaceManager logReserveInfo:]
+ -[MSUFreeSpaceManager reserveInfo:error:]
+ -[MSUFreeSpaceManager reserveInfo]
+ -[MSUFreeSpaceManager reservedSpace:]
+ -[MSUFreeSpaceManager setEntitledReservation:error:]
+ -[PCIeNANDBootWriter appendImages:]
+ -[PCIeNANDBootWriter layout]
+ -[PCIeNANDBootWriter setLayout:]
+ -[UMEventRecorder isDeviceSupervised]
+ -[UMEventRecorder setIsDeviceSupervised:]
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-70ee89773b73da071799d70cafe2fade.o
+ /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-d8e3e3eee35c3e508f2f6c88ce036670.o
+ GCC_except_table17
+ GCC_except_table20
+ GCC_except_table24
+ GCC_except_table7
+ GCC_except_table81
+ OBJC_IVAR_$_PCIeNANDBootWriter._layout
+ OBJC_IVAR_$_UMEventRecorder._isDeviceSupervised
+ __56-[UMEventRecorder submitEventsInBackground:withOptions:]_block_invoke.696
+ _checkpoint_closure_context_set_end_time
+ _checkpoint_closure_context_set_start_time
+ _checkpoint_nvram_adjust_id
+ _checkpoint_time_copy_current_time
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _mach_absolute_time
+ _objc_msgSend$appendImages:
+ _objc_msgSend$data
+ _objc_msgSend$setIsDeviceSupervised:
+ _objc_msgSend$setLayout:
+ _objc_msgSend$snapHasCombinedImages
+ _objc_msgSend$waitUntilTime:
+ _ramrod_probe_unique_media
+ _ramrod_write_os_info_for_nerd
- +[IMG3NorUpdater IOMatchingPropertyTable]
- -[IMG3NorUpdater _encodeAndWriteIMG3Data:isLLB:isTicket:withError:]
- -[IMG3NorUpdater dealloc]
- -[IMG3NorUpdater initWithIOService:]
- -[IMG3NorUpdater updateBootFirmwareWithCallback:context:error:]
- -[IMG3NorUpdater writer]
- -[MSUCheckpointAsyncBlockContext dealloc]
- -[MSUCheckpointAsyncBlockContext waitUntilDate:]
- -[MSUCheckpointAsyncContext waitUntilDate:]
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-21eb89572409f4f5ee695d65cb051d7f.o
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-3b69fe07e8e9325dc0823d0aa24d810a.o
- GCC_except_table12
- GCC_except_table14
- GCC_except_table16
- GCC_except_table86
- Image3.c
- OBJC_IVAR_$_IMG3NorUpdater._writer
- _CC_SHA1_Final
- _CC_SHA1_Init
- _CC_SHA1_Update
- _CFMakeCollectable
- _IOConnectCallStructMethod
- _OBJC_CLASS_$_IMG3NorUpdater
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_METACLASS_$_IMG3NorUpdater
- __56-[UMEventRecorder submitEventsInBackground:withOptions:]_block_invoke.711
- __OBJC_$_CLASS_METHODS_IMG3NorUpdater
- __OBJC_$_INSTANCE_METHODS_IMG3NorUpdater
- __OBJC_$_INSTANCE_VARIABLES_IMG3NorUpdater
- __OBJC_$_PROP_LIST_IMG3NorUpdater
- __OBJC_CLASS_RO_$_IMG3NorUpdater
- __OBJC_METACLASS_RO_$_IMG3NorUpdater
- __ticket
- __ticket_is_img3
- _checkpoint_get_nvram_name_string
- _image3AdvanceCursorWithZeroPad
- _image3Discard
- _image3Finalize
- _image3Free
- _image3GetTagStruct
- _image3GetTagUnsignedNumber
- _image3InstantiateFromBuffer
- _image3InstantiateNew
- _image3Malloc
- _image3PKISignHash
- _image3SHA1Generate
- _image3SHA1Partial
- _image3SetTagStructure
- _image3SetTagUnsignedNumber
- _is_storage_apfs
- _mmap
- _munmap
- _objc_msgSend$_encodeAndWriteIMG3Data:isLLB:isTicket:withError:
- _objc_msgSend$dateWithTimeIntervalSinceNow:
- _objc_msgSend$firstMatchInString:options:range:
- _objc_msgSend$rangeAtIndex:
- _objc_msgSend$regularExpressionWithPattern:options:error:
- _objc_msgSend$serviceConnect
- _objc_msgSend$substringWithRange:
- _objc_msgSend$waitUntilDate:
- _objc_release_x28
- _ramrod_get_system_partition_device_node
- _ramrod_probe_media
- _ramrod_ticket_create_img3
- _realloc
- _using_APFS
- _using_LwVM
- ramrod_ticket.c
CStrings:
+ "%s: Creating directory(%@) to save current OS state"
+ "%s: Dictionary is %@\n"
+ "%s: Failed to allocate path string to save Booted OS state\n"
+ "%s: Failed to allocate string to save the path for the state file\n"
+ "%s: Failed to chmod bootedOsStateFile at %@ errno=%d: (%s)..Deleting the file"
+ "%s: Failed to chown bootedOSStateFile at %@ errno=%d: (%s)..Deleting the file"
+ "%s: Failed to create directory : %@"
+ "%s: Failed to delete BootedOsState file at %@. Error: %@"
+ "%s: Failed to get c string representation of the bootedOSStateFile path to fixup permissions..Deleting the file"
+ "%s: Failed to get uid/gid for mobile user to chown the bootedOSState file..Deleting the file at %@"
+ "%s: Failed to set permissions on BootedOSState file..Deleting it"
+ "%s: Failed to write env data to file\n"
+ "%s: No exiting file\n"
+ "%s: Read the current file so we can modify it\n"
+ "%s: Saving env data to %@"
+ "%s: Successfully fixed up permissions for %@"
+ "%s: Updating file permissions\n"
+ "%s: made it to the new OS, but there is no ota-result set. Assuming success.\n"
+ "%s: missing parameters\n"
+ "B32@0:8Q16^@24"
+ "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
+ "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
+ "Q32@0:8@16^@24"
+ "T@\"NSNumber\",C,N,V_isDeviceSupervised"
+ "TQ,V_layout"
+ "_isDeviceSupervised"
+ "_layout"
+ "appendImages:"
+ "data"
+ "isDeviceSupervised"
+ "layout"
+ "logReserveInfo:"
+ "ramrod_write_os_info_for_nerd"
+ "reserveInfo"
+ "reserveInfo:error:"
+ "reservedSpace:"
+ "setEntitledReservation:error:"
+ "setIsDeviceSupervised:"
+ "setLayout:"
+ "snap-has-combined-images"
+ "snapHasCombinedImages"
+ "supervised"
+ "unable to find preboot volume\n\n"
+ "unable to unmount preboot volume\n\n"
+ "v24@0:8Q16"
+ "waitUntilTime:"
- "%s returned an error when writing img3 object"
- "%s: Failed to chmod bootedOsStateFile at %@ errno=%d: (%s)..Deleting the file\n"
- "%s: Failed to chown bootedOSStateFile at %@ errno=%d: (%s)..Deleting the file\n"
- "%s: Failed to delete BootedOsState file at %@. Error: %@\n"
- "%s: Failed to get c string representation of the bootedOSStateFile path to fixup permissions..Deleting the file\n"
- "%s: Failed to get uid/gid for mobile user to chown the bootedOSState file..Deleting the file at %@\n"
- "%s: Successfully fixed up permissions for %@\n"
- "%s: flashing %c%c%c%c data (length = 0x%lx)\n"
- "%s: made it to the new OS, but there is no ota-result set.  Assuming success.\n"
- "%s: unable to create CFData for img3 ticket"
- "%s: unable to create img3 ticket"
- "(.+@)?(\\/dev\\/.+$|^root_device$)"
- "-J"
- "-[IMG3NorUpdater _encodeAndWriteIMG3Data:isLLB:isTicket:withError:]"
- "-[IMG3NorUpdater updateBootFirmwareWithCallback:context:error:]"
- "-s"
- "/sbin/mount_hfs"
- "/sbin/newfs_hfs"
- "41504653-0000-11AA-AA11-00306543ECAC"
- "AppleImage3NORAccess"
- "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
- "B40@0:8^{__CFData=}16B24B28^@32"
- "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
- "Could not probe media: %@\n"
- "Creating directory(%@) to save current OS state\n"
- "Dictionary is %@\n"
- "Failed to allocate path string to save Booted OS state\n"
- "Failed to allocate string to save the path for the state file\n"
- "Failed to create directory : %@\n"
- "Failed to instantiate img3 image"
- "Failed to read img3 type"
- "Failed to set permissions on BootedOSState file..Deleting it\n"
- "Failed to write Img3 Firmware data"
- "Failed to write Img3 Ticket data"
- "Failed to write Img3 boot data"
- "Failed to write env data to file\n"
- "IMG3NorUpdater"
- "Img3 Ticket Data updated"
- "Img3 encoding failed"
- "LightweightVolumeManager_Media"
- "SPI writer was unavailable at write-time."
- "Saving env data to %@\n"
- "Unexpected imageType in firmware"
- "Updating file permissions\n"
- "_encodeAndWriteIMG3Data:isLLB:isTicket:withError:"
- "convPanic"
- "could not create regular expression object with pattern %s\n"
- "could not create string from f_mntfromname %s\n"
- "could not finalize ticket img3"
- "dateWithTimeIntervalSinceNow:"
- "f_mntfromname %@ has unrecognized pattern\n"
- "failed to create data tag for ticket"
- "failed to create img3\n"
- "firstMatchInString:options:range:"
- "hfs"
- "postConv"
- "preConv"
- "ramrod_ticket_create_img3"
- "rangeAtIndex:"
- "regularExpressionWithPattern:options:error:"
- "saveCurrentEnvInfoForNeRD"
- "statfs(\"/\") failed. errno=%d\n"
- "substringWithRange:"
- "unable to find content hint for %s"
- "unable to find system volume\n"
- "unable to mmap %zu bytes for image3 data"
- "waitUntilDate:"

```
