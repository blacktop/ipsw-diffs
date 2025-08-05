## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-353.0.0.0.0
-  __TEXT.__text: 0x17f34
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_stubs: 0x660
+354.0.0.0.1
+  __TEXT.__text: 0x1837c
+  __TEXT.__auth_stubs: 0x1470
+  __TEXT.__objc_stubs: 0x680
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0xa292
+  __TEXT.__cstring: 0xa42d
   __TEXT.__const: 0x6c8
-  __TEXT.__objc_methname: 0x4ec
+  __TEXT.__objc_methname: 0x4fe
   __TEXT.__objc_classname: 0xc
   __TEXT.__objc_methtype: 0x3a
   __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__unwind_info: 0x3d8
-  __DATA_CONST.__auth_got: 0xa28
+  __TEXT.__unwind_info: 0x3e0
+  __DATA_CONST.__auth_got: 0xa48
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x678
-  __DATA_CONST.__cfstring: 0x17e0
+  __DATA_CONST.__cfstring: 0x1820
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x1a8
+  __DATA.__objc_selrefs: 0x1b0
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A9F292F4-36F2-3E55-B0F2-617D4952020D
-  Functions: 240
-  Symbols:   374
-  CStrings:  1430
+  UUID: 453EE331-EF50-3A57-9028-7A2FFC69F44A
+  Functions: 242
+  Symbols:   378
+  CStrings:  1442
 
Symbols:
+ _IOBSDNameMatching
+ _IOObjectRetain
+ _IORegistryEntryCreateIterator
+ _IORegistryEntryGetChildEntry
CStrings:
+ "%s: %sCleaning supplemental folder from preboot"
+ "%s: OVP: device_size = %llu (%.1f GB) for device %s\n"
+ "%s: Using get_media_size() failed with error %d, trying the old container-based lookup"
+ "%s: Using get_media_size() succeeded, device_size = %llu\n"
+ "%s: file_size = %zu (%.1f MB)\n"
+ "%s: preallocation of %zu bytes failed: %d \n"
+ "%s: safeObliterate: Cleaning Preboot volume in EpDM"
+ "%s: safeObliterate: Skip Cleaning Preboot volume, epdm_skip_preboot_cleanup requested on internal build"
+ "/dev/disk%s"
+ "/private/preboot/supplemental"
+ "IOBlockStorageDriver"
+ "Size"
+ "fileExistsAtPath:"
+ "fixup_preboot_volume"
- "%s: device_size = %llu (%lld GB)\n"
- "%s: file_size = %llu (%lld GB)\n"
- "%s: preallocation of %llu bytes failed: %d \n"
- "%s: safeObliterate: Cleaning Preboot volume"

```
