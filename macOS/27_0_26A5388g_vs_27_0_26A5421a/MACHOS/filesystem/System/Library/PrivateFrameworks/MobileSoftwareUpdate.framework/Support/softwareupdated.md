## softwareupdated

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2718.0.12.501.1
-  __TEXT.__text: 0xc07dc
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_stubs: 0x5dc0
+2718.0.18.0.0
+  __TEXT.__text: 0xc0d88
+  __TEXT.__auth_stubs: 0x1c00
+  __TEXT.__objc_stubs: 0x5e00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x2784
-  __TEXT.__gcc_except_tab: 0xb1c
+  __TEXT.__objc_methlist: 0x279c
+  __TEXT.__gcc_except_tab: 0xb7c
   __TEXT.__const: 0x77e08
-  __TEXT.__objc_methname: 0x65e3
-  __TEXT.__cstring: 0x19af2
+  __TEXT.__objc_methname: 0x6650
+  __TEXT.__cstring: 0x19959
   __TEXT.__objc_classname: 0x4b2
-  __TEXT.__objc_methtype: 0x18bc
-  __TEXT.__oslogstring: 0x4c17
+  __TEXT.__objc_methtype: 0x18cd
+  __TEXT.__oslogstring: 0x4c2d
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1768
+  __TEXT.__unwind_info: 0x1770
   __TEXT.__eh_frame: 0x2d0
   __DATA_CONST.__const: 0x37c8
-  __DATA_CONST.__cfstring: 0xd720
+  __DATA_CONST.__cfstring: 0xd900
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_intobj: 0x270
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0xe08
+  __DATA_CONST.__auth_got: 0xe10
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x78
   __DATA.__objc_const: 0x3660
-  __DATA.__objc_selrefs: 0x1ce0
+  __DATA.__objc_selrefs: 0x1cf8
   __DATA.__objc_ivar: 0x254
   __DATA.__objc_data: 0xa50
   __DATA.__data: 0xec8

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 2298
-  Symbols:   4407
-  CStrings:  4966
+  Functions: 2293
+  Symbols:   4417
+  CStrings:  4965
 
Symbols:
+ +[MSUBootFirmwareUpdater hasExclusiveUSBHostDeviceMode]
+ -[MSUTargetController(InstallerOperations) _ensureCentauriManifestWithMountPoint:ticket:variant:]
+ -[UMEventRecorder _getCoalescedSubTargetID]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/common-3cadf45546d59e9f578695c901be58bc.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/common-7baa4b734515071f75fa885d2df1fb13.o
+ GCC_except_table24
+ GCC_except_table27
+ _CFStringFind
+ _IOServiceNameMatching
+ ___block_descriptor_96_e8_32o40o48o56o64o72r80r_e5_v8?0l
+ ___copy_helper_block_e8_32o40o48o56o64o72r80r
+ ___destroy_helper_block_e8_32o40o48o56o64o72r80r
+ _disk_is_virtual
+ _msu_copy_hardware_model
+ _msu_tolerate_missing_global_manifest
+ _objc_msgSend$_ensureCentauriManifestWithMountPoint:ticket:variant:
+ _objc_msgSend$_getCoalescedSubTargetID
+ _ramrod_device_has_centauri
+ disk_is_virtual
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/common-46cc3daac91269cebcfc464060563eb4.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/common-fc5bd509b1b49e919a3d16b56c130fff.o
- AMRestorePartitionFWCopyTagData
- GCC_except_table26
- _AMRestorePartitionOpenFileWithURL
- _AMSupportLogInternal
- ___block_descriptor_88_e8_32o40o48o56o64o72r_e5_v8?0l
- ___copy_helper_block_e8_32o40o48o56o64o72r
- ___destroy_helper_block_e8_32o40o48o56o64o72r
CStrings:
+ "%s: sysctlbyname() failed: %d (%s)\n"
+ "B40@0:8@16@24@32"
+ "Centauri global manifest is missing"
+ "CoalescedSubTargetID"
+ "Darwin"
+ "Groundhog"
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
+ "skipping for variant %@\n"
+ "target preboot not mounted\n"
+ "target_os_version"
+ "usb-host-device-exclusive"
- "   ^^ Found requested tag."
- "0 bytes read, IMG4 image hit end of block device? - fail errno=%d.."
- "AMRestorePartitionFWCopyTagData"
- "Bytes read didn't match derLen."
- "Failed to allocate Img4Data"
- "Failed to read terminator bytes."
- "Invalid termination bytes: [0x%02x, 0x%02x]"
- "Item %02d, der.length=%8d, Bad Img4 inside valid DER sequence. (derstat=%d)"
- "Item %02d, offset=%8d, der.length=%8d, img4Tag=[%@]"
- "No DER segments found."
- "No more segments. (derstat=%d)"
- "Too Many DER segments!"
- "Unable to open inURL %@"
- "Unable to rewind to start of IMG4 segment lseek=%ll, errno=%d."
- "Unable to seek to terminator segment errno=%d."
- "Unable to set F_NOCACHE on firmware storage"
- "_AMRestorePartitionOpenFileWithURL"
- "failed to allocate DER chunk buffer"
- "failed to allocate IMG4buffer"
- "failed to convert url to file system representation"
- "inURL is NULL"
- "open() returned %d, %s"
```
