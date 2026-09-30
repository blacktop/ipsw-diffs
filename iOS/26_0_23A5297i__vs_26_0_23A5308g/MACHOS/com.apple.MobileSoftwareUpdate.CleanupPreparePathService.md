## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2422.0.71.0.1
-  __TEXT.__text: 0x28b30
+2422.0.80.0.0
+  __TEXT.__text: 0x291d4
   __TEXT.__auth_stubs: 0x1650
   __TEXT.__objc_stubs: 0x3740
-  __TEXT.__objc_methlist: 0x16fc
-  __TEXT.__cstring: 0x10a62
+  __TEXT.__objc_methlist: 0x1714
+  __TEXT.__cstring: 0x10fae
   __TEXT.__const: 0x1220
   __TEXT.__oslogstring: 0x1c6
   __TEXT.__gcc_except_tab: 0x4c8
   __TEXT.__objc_classname: 0x1b8
-  __TEXT.__objc_methname: 0x3b47
-  __TEXT.__objc_methtype: 0xdfc
-  __TEXT.__unwind_info: 0x900
+  __TEXT.__objc_methname: 0x3b72
+  __TEXT.__objc_methtype: 0xe0e
+  __TEXT.__unwind_info: 0x908
   __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x1498
-  __DATA_CONST.__cfstring: 0x9f00
+  __DATA_CONST.__const: 0x14b0
+  __DATA_CONST.__cfstring: 0xa220
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0xb8
-  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0xf8
+  __DATA_CONST.__objc_arrayobj: 0x78
   __DATA.__objc_const: 0x1f70
-  __DATA.__objc_selrefs: 0x1138
+  __DATA.__objc_selrefs: 0x1140
   __DATA.__objc_ivar: 0x16c
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x4e0

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: F5DC233C-31AD-3469-B1BD-B1B2715EC2D7
-  Functions: 795
-  Symbols:   5770
-  CStrings:  4159
+  UUID: 08F352E5-8A9F-307A-8EBE-D7A3E9947C97
+  Functions: 800
+  Symbols:   5794
+  CStrings:  4213
 
Symbols:
+ -[MSUFreeSpaceManager preallocatedSpaceMetricInfo]
+ -[MSUFreeSpaceManager reserveInfo:key:error:]
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/4~B6jDugAp3vzaboAI77N_Yg6AC0uNJ1z0bqR3Lyc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ GCC_except_table22
+ __block_literal_global.391
+ _handle_MSUSaveAccessibilityDomains
+ _objc_msgSend$reserveInfo:key:error:
+ _objc_msgSend$stringWithCString:
+ _ramrod_stash_info_to_file
+ _saveAccessibilityDomainsForDRE
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/4~B5YMugDOSBwbZKzaKU-Kbx-NoCoJ77YON7NpKEQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- GCC_except_table20
- _OBJC_CLASS_$_NSLocale
- __block_literal_global.372
- _objc_msgSend$currentLocale
- _objc_msgSend$languageCode
CStrings:
+ "%s: Attempting to read the current file so we can modify it\n"
+ "%s: Creating directory(%@) to save current state\n"
+ "%s: Directory(%@) doesn't exist but a file exists with the same name at that location. Cannot proceed.\n"
+ "%s: Failed to allocate path string to save persisted state\n"
+ "%s: Failed to allocate string for the stashed file path\n"
+ "%s: Failed to create directory. Error: %@\n"
+ "%s: Failed to delete persisted file at %@. Error: %@"
+ "%s: Failed to set permissions on stashed file..Deleting it\n"
+ "%s: No existing file\n"
+ "%s: Saving data to %@\n"
+ "%s: Stashing info to mount:%s dir:%s file:%s\n"
+ "AccessibilityDomains"
+ "AccessibilityDomains.plist"
+ "Exported %lu preferences for domain: %@\n"
+ "Failed to save accessibility domains to update volume"
+ "Failed to save accessibility domains, but continuing with booted OS state save\n"
+ "Language code passed in from options: (%@)\n"
+ "Language code was not passed in and no previously stashed language found. Using default\n"
+ "Language code was not passed in. Using previously stashed code : %@\n"
+ "No accessibility domains to export\n"
+ "No preferences found for domain: %@\n"
+ "Not saving accessibility domains - not supported on this target or already in recovery\n"
+ "Q40@0:8@16@24^@32"
+ "SaveAccessibilityDomains"
+ "Successfully exported %lu accessibility domains to DRE\n"
+ "[MSUSaveAccessibilityDomains]: Additional info to be saved: %@\n"
+ "[MSUSaveAccessibilityDomains]: Failed to save accessibility domains\n"
+ "[MSUSaveAccessibilityDomains]: Handling request to save Accessibility domains\n"
+ "[MSUSaveAccessibilityDomains]: Saving only default accessibility domains info\n"
+ "[MSUSaveAccessibilityDomains]: Successfully saved accessibility domains\n"
+ "com.apple.Accessibility"
+ "com.apple.Accessibility.SwitchControl"
+ "com.apple.Accessibility.TouchAccommodations"
+ "com.apple.AssistiveTouch"
+ "com.apple.SpeakSelection"
+ "com.apple.VoiceOverTouch"
+ "com.apple.ZoomTouch"
+ "com.apple.mediaaccessibility"
+ "en"
+ "preallocatedSpaceMetricInfo"
+ "ramrod_stash_info_to_file"
+ "reserveInfo:key:error:"
+ "stringWithCString:"
- "%@/%s"
- "%s: Creating directory(%@) to save current OS state"
- "%s: Failed to allocate path string to save Booted OS state\n"
- "%s: Failed to allocate string to save the path for the state file\n"
- "%s: Failed to create directory : %@"
- "%s: Failed to delete BootedOsState file at %@. Error: %@"
- "%s: Failed to set permissions on BootedOSState file..Deleting it"
- "%s: No exiting file\n"
- "%s: Read the current file so we can modify it\n"
- "%s: Saving env data to %@"
- "Failed to determine language code for device\n"
- "currentLocale"
- "languageCode"
- "ramrod_write_os_info_for_nerd"

```
