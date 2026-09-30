## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-3.100.0.0.0
-  __TEXT.__text: 0x76f7c
-  __TEXT.__auth_stubs: 0x1df0
+3.104.0.0.0
+  __TEXT.__text: 0x78448
+  __TEXT.__auth_stubs: 0x1e70
   __TEXT.__objc_stubs: 0x13c0
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x21fc
-  __TEXT.__const: 0x2c80
-  __TEXT.__cstring: 0x7ea4
-  __TEXT.__oslogstring: 0x502b
+  __TEXT.__gcc_except_tab: 0x226c
+  __TEXT.__const: 0x2d00
+  __TEXT.__cstring: 0x80e8
+  __TEXT.__oslogstring: 0x50b9
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x153f
   __TEXT.__objc_methtype: 0x11e8
-  __TEXT.__unwind_info: 0x1420
+  __TEXT.__unwind_info: 0x1490
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0xf08
+  __DATA_CONST.__auth_got: 0xf48
   __DATA_CONST.__got: 0xad8
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x6308
-  __DATA_CONST.__cfstring: 0x2fe0
+  __DATA_CONST.__const: 0x6440
+  __DATA_CONST.__cfstring: 0x3160
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_intobj: 0x108
+  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x808
   __DATA.__objc_selrefs: 0x570
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x206c10
   __DATA.__bss: 0x184
-  __DATA.__common: 0x58
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1504
-  Symbols:   850
-  CStrings:  1872
+  Functions: 1535
+  Symbols:   858
+  CStrings:  1890
 
Symbols:
+ _open
+ _notify_set_state
+ _notify_post
+ _PDPeridotCalibCalibrationBlobsFromNVM
+ _write
+ _lseek
+ _PDPeridotCalibCopySerialNumber
+ _read
+ _strstr
- _fseek
CStrings:
+ "\tDefault calibration from NVM: failed to read device NVM"
+ "\tDefault calibration from NVM: device is not ready or no ToF channel found"
+ "\tDefault calibration from NVM: created pseudo-FDR from NVM"
+ "FdrForTof"
+ "\tDefault calibration from NVM: failed to read sensor NVM"
+ "%!s(MISSING) - Failed file path integrity check\n"
+ "./"
+ "%!s(MISSING) - Invalid write length (%!d(MISSING))\n"
+ "\tValidating SN (registry vs cache)"
+ "%!s(MISSING) - invalid cache - exiting, chan: %!d(MISSING)\n"
+ "GetSensorNVMBytes"
+ "\tDefault calibration from NVM: failed to create calibration from NVM"
+ "../"
+ "\tSerial numbers sized mismatch"
+ "3.104"
+ "\tLooking for calibration in NVM\n"
+ "\tCached Serial Number: %!s(MISSING), calibration: %!s(MISSING)"
+ "\tValidating Calibration UUID (FDR vs cache)"
+ "/private/var/mobile/Media/DCIM"
+ "%!s(MISSING) - Invalid read length (%!d(MISSING))\n"
+ "\tCan't read serial number from cache"
- "ab"
- "/var/mobile/Media/DCIM"
- "3.100"

```
