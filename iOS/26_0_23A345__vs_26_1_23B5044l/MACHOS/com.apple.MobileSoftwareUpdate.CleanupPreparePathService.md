## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2422.0.80.0.0
-  __TEXT.__text: 0x291d4
+2422.40.19.502.1
+  __TEXT.__text: 0x29394
   __TEXT.__auth_stubs: 0x1650
   __TEXT.__objc_stubs: 0x3740
-  __TEXT.__objc_methlist: 0x1714
-  __TEXT.__cstring: 0x10fae
+  __TEXT.__objc_methlist: 0x172c
+  __TEXT.__cstring: 0x11117
   __TEXT.__const: 0x1220
   __TEXT.__oslogstring: 0x1c6
   __TEXT.__gcc_except_tab: 0x4c8
   __TEXT.__objc_classname: 0x1b8
-  __TEXT.__objc_methname: 0x3b72
+  __TEXT.__objc_methname: 0x3b7c
   __TEXT.__objc_methtype: 0xe0e
-  __TEXT.__unwind_info: 0x908
+  __TEXT.__unwind_info: 0x910
   __DATA_CONST.__auth_got: 0xb38
   __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x14b0
-  __DATA_CONST.__cfstring: 0xa220
+  __DATA_CONST.__cfstring: 0xa2e0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA.__objc_const: 0x1f70
-  __DATA.__objc_selrefs: 0x1140
+  __DATA.__objc_selrefs: 0x1148
   __DATA.__objc_ivar: 0x16c
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x4e0
-  __DATA.__bss: 0x658
+  __DATA.__bss: 0x660
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: 367CFD6E-8F4F-3302-B925-2098D769792F
-  Functions: 800
-  Symbols:   5794
-  CStrings:  4213
+  UUID: 7269D3E9-79B4-3183-A5CA-AD8FAA8BD591
+  Functions: 802
+  Symbols:   5806
+  CStrings:  4231
 
Symbols:
+ +[UMEventRecorder enableTesting]
+ -[UMEventRecorder addPersistentAttributes:]
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/4~B9_OugDSxBqxawtfk1Vdwmt7CI59tQQukflG5QQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ GCC_except_table40
+ __56-[UMEventRecorder submitEventsInBackground:withOptions:]_block_invoke.711
+ ___TESTING
+ __block_literal_global.197
+ _objc_msgSend$addPersistentAttributes:
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/4~B8huugBiobnPSjYbYebHDs43nPsX-jDWGeAm99w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- GCC_except_table39
- __56-[UMEventRecorder submitEventsInBackground:withOptions:]_block_invoke.693
- __block_literal_global.179
- _objc_msgSend$dictionaryWithObject:forKey:
CStrings:
+ "%s: Using path for testing: /tmp/UpdateMetrics"
+ "%s: Using path for testing: /tmp/UpdateMetrics/Events"
+ "%s: Using path for testing: /tmp/UpdateMetrics/LegacyEvents"
+ "-[UMEventRecorder _eventDirectory]"
+ "-[UMEventRecorder _legacyEventDirectory]"
+ "-[UMEventRecorder _supportDirectory]"
+ "/tmp/UpdateMetrics"
+ "/tmp/UpdateMetrics/Events"
+ "/tmp/UpdateMetrics/LegacyEvents"
+ "Attempt to save attributes %@ when install not in progres"
+ "SIM"
+ "SIM_"
+ "addPersistentAttributes:"
+ "enableTesting"
- "Attempt to save attribute %@ when install not in progres"
- "dictionaryWithObject:forKey:"

```
