## com.apple.MobileSoftwareUpdate.CryptegraftService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Versions/Current/XPCServices/com.apple.MobileSoftwareUpdate.CryptegraftService.xpc/Contents/MacOS/com.apple.MobileSoftwareUpdate.CryptegraftService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2718.0.12.501.1
-  __TEXT.__text: 0x2f46c
-  __TEXT.__auth_stubs: 0x1590
-  __TEXT.__objc_stubs: 0x35a0
-  __TEXT.__objc_methlist: 0x166c
-  __TEXT.__gcc_except_tab: 0x49c
+2718.0.18.0.0
+  __TEXT.__text: 0x2f82c
+  __TEXT.__auth_stubs: 0x15b0
+  __TEXT.__objc_stubs: 0x35e0
+  __TEXT.__objc_methlist: 0x167c
+  __TEXT.__gcc_except_tab: 0x4a8
   __TEXT.__const: 0x1024
-  __TEXT.__cstring: 0xe8e0
-  __TEXT.__objc_methname: 0x392c
+  __TEXT.__cstring: 0xe72d
+  __TEXT.__objc_methname: 0x3986
   __TEXT.__objc_classname: 0x29a
   __TEXT.__objc_methtype: 0xa30
-  __TEXT.__oslogstring: 0x1576
-  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__oslogstring: 0x158c
+  __TEXT.__unwind_info: 0x7d0
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x1098
-  __DATA_CONST.__cfstring: 0x75e0
+  __DATA_CONST.__cfstring: 0x77a0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x208
   __DATA_CONST.__objc_intobj: 0x1b0
-  __DATA_CONST.__auth_got: 0xad8
+  __DATA_CONST.__auth_got: 0xae8
   __DATA_CONST.__got: 0x2e8
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__objc_const: 0x2408
-  __DATA.__objc_selrefs: 0x1028
+  __DATA.__objc_selrefs: 0x1040
   __DATA.__objc_ivar: 0x164
   __DATA.__objc_data: 0xa00
   __DATA.__data: 0x3e0

   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 925
-  Symbols:   2129
-  CStrings:  2692
+  Functions: 918
+  Symbols:   2138
+  CStrings:  2690
 
Symbols:
+ +[MSUBootFirmwareUpdater hasExclusiveUSBHostDeviceMode]
+ -[MSUTargetController(InstallerOperations) _ensureCentauriManifestWithMountPoint:ticket:variant:]
+ GCC_except_table27
+ _CFStringFind
+ _IOServiceNameMatching
+ _disk_is_virtual
+ _msu_copy_hardware_model
+ _msu_tolerate_missing_global_manifest
+ _objc_msgSend$_ensureCentauriManifestWithMountPoint:ticket:variant:
+ _objc_msgSend$class
+ _objc_retainAutoreleasedReturnValue
+ _ramrod_device_has_centauri
+ disk_is_virtual
- AMRestorePartitionFWCopyTagData
- GCC_except_table26
- _AMRestorePartitionOpenFileWithURL
- _AMSupportLogInternal
CStrings:
+ "%s: sysctlbyname() failed: %d (%s)\n"
+ "02:53:04"
+ "2718.0.18"
+ "Aug 10 2026"
+ "Centauri global manifest is missing"
+ "Darwin"
+ "Groundhog"
+ "Target OS Version"
+ "_ensureCentauriManifestWithMountPoint:ticket:variant:"
+ "centauri manifest is missing: %@\n"
+ "centauri manifest is present: %@\n"
+ "class"
+ "disk is vitual ?: %d\n"
+ "failed to query hardware model\n"
+ "hasExclusiveUSBHostDeviceMode"
+ "missing volume group UUID\n"
+ "msu_copy_hardware_model"
+ "no"
+ "ramrod_device_has_centauri"
+ "skipping for variant %@\n"
+ "target preboot not mounted\n"
+ "target_os_version"
+ "usb-host-device-exclusive"
+ "yes"
- "   ^^ Found requested tag."
- "%@"
- "0 bytes read, IMG4 image hit end of block device? - fail errno=%d.."
- "00:27:37"
- "2718.0.12.501.1"
- "AMRestorePartitionFWCopyTagData"
- "Bytes read didn't match derLen."
- "Failed to allocate Img4Data"
- "Failed to read terminator bytes."
- "Invalid termination bytes: [0x%02x, 0x%02x]"
- "Item %02d, der.length=%8d, Bad Img4 inside valid DER sequence. (derstat=%d)"
- "Item %02d, offset=%8d, der.length=%8d, img4Tag=[%@]"
- "Jul 16 2026"
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
