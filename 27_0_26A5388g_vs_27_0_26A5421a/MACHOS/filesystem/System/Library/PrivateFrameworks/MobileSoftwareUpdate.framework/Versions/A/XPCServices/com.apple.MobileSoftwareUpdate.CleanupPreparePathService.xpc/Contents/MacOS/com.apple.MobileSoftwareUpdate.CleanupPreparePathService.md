## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Versions/A/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/Contents/MacOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2718.0.12.501.1
-  __TEXT.__text: 0xb31c4
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_stubs: 0x4e00
-  __TEXT.__objc_methlist: 0x1f04
-  __TEXT.__cstring: 0x1aa27
+2718.0.18.0.0
+  __TEXT.__text: 0xb3aa0
+  __TEXT.__auth_stubs: 0x1b50
+  __TEXT.__objc_stubs: 0x4e60
+  __TEXT.__objc_methlist: 0x1f1c
+  __TEXT.__cstring: 0x1ac2b
   __TEXT.__const: 0x78020
-  __TEXT.__gcc_except_tab: 0x718
-  __TEXT.__objc_methname: 0x56d4
+  __TEXT.__gcc_except_tab: 0x724
+  __TEXT.__objc_methname: 0x5751
   __TEXT.__objc_classname: 0x281
-  __TEXT.__objc_methtype: 0x101c
-  __TEXT.__oslogstring: 0x1a42
+  __TEXT.__objc_methtype: 0x102d
+  __TEXT.__oslogstring: 0x1a58
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1370
+  __TEXT.__unwind_info: 0x1388
   __TEXT.__eh_frame: 0x2d0
   __DATA_CONST.__const: 0x2ae8
-  __DATA_CONST.__cfstring: 0xd7c0
+  __DATA_CONST.__cfstring: 0xd9e0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0x7e0
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dictobj: 0x230
-  __DATA_CONST.__auth_got: 0xda8
-  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__auth_got: 0xdb8
+  __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__auth_ptr: 0x78
   __DATA.__objc_const: 0x2768
-  __DATA.__objc_selrefs: 0x1858
+  __DATA.__objc_selrefs: 0x1878
   __DATA.__objc_ivar: 0x1cc
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x978

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 1968
-  Symbols:   3658
-  CStrings:  4494
+  Functions: 1975
+  Symbols:   3672
+  CStrings:  4518
 
Symbols:
+ +[MSUBootFirmwareUpdater hasExclusiveUSBHostDeviceMode]
+ -[MSUTargetController(InstallerOperations) _ensureCentauriManifestWithMountPoint:ticket:variant:]
+ -[UMEventRecorder _getCoalescedSubTargetID]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-3cadf45546d59e9f578695c901be58bc.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-7baa4b734515071f75fa885d2df1fb13.o
+ GCC_except_table27
+ _CFStringFind
+ _IOServiceNameMatching
+ _OBJC_CLASS_$_NSSet
+ _disk_is_virtual
+ _msu_copy_hardware_model
+ _msu_tolerate_missing_global_manifest
+ _objc_msgSend$_ensureCentauriManifestWithMountPoint:ticket:variant:
+ _objc_msgSend$_getCoalescedSubTargetID
+ _objc_msgSend$setWithObjects:
+ _ramrod_device_has_centauri
+ disk_is_virtual
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-46cc3daac91269cebcfc464060563eb4.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-fc5bd509b1b49e919a3d16b56c130fff.o
- GCC_except_table26
CStrings:
+ "%s: sysctlbyname() failed: %d (%s)\n"
+ "AXSVoiceOverTurnOnBluetoothEnabled"
+ "B40@0:8@16@24@32"
+ "Centauri global manifest is missing"
+ "CoalescedSubTargetID"
+ "Darwin"
+ "Groundhog"
+ "Skipping denied accessibility key: %@ in domain: %@\n"
+ "_ensureCentauriManifestWithMountPoint:ticket:variant:"
+ "_getCoalescedSubTargetID"
+ "centauri manifest is missing: %@\n"
+ "centauri manifest is present: %@\n"
+ "coalescedSubTargetID"
+ "disk is vitual ?: %d\n"
+ "failed to query hardware model\n"
+ "hasExclusiveUSBHostDeviceMode"
+ "missing volume group UUID\n"
+ "msu_copy_hardware_model"
+ "ramrod_device_has_centauri"
+ "setWithObjects:"
+ "skipping for variant %@\n"
+ "target preboot not mounted\n"
+ "target_os_version"
+ "usb-host-device-exclusive"
```
