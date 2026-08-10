## restoreserviced

> `/usr/libexec/restoreserviced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-48.0.0.0.0
-  __TEXT.__text: 0x142e8
+48.0.1.0.0
+  __TEXT.__text: 0x13f24
   __TEXT.__auth_stubs: 0xec0
   __TEXT.__objc_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0xcdc
+  __TEXT.__objc_methlist: 0xce4
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0x7cf3
+  __TEXT.__cstring: 0x79c8
   __TEXT.__oslogstring: 0x3a5
   __TEXT.__gcc_except_tab: 0x1ac
-  __TEXT.__objc_methname: 0x1865
+  __TEXT.__objc_methname: 0x1883
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x77c
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__unwind_info: 0x520
   __DATA_CONST.__const: 0xcd8
-  __DATA_CONST.__cfstring: 0x3fe0
+  __DATA_CONST.__cfstring: 0x4000
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68

   __DATA_CONST.__auth_got: 0x770
   __DATA_CONST.__got: 0x190
   __DATA.__objc_const: 0x1370
-  __DATA.__objc_selrefs: 0x758
+  __DATA.__objc_selrefs: 0x760
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x648

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 548
+  Functions: 537
   Symbols:   292
-  CStrings:  1474
+  CStrings:  1454
 
CStrings:
+ "hasExclusiveUSBHostDeviceMode"
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
