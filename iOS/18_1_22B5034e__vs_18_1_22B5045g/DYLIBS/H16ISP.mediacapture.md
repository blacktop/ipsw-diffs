## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.100.0.0.0
-  __TEXT.__text: 0x1a7708
-  __TEXT.__auth_stubs: 0x31e0
+3.104.0.0.0
+  __TEXT.__text: 0x1a8758
+  __TEXT.__auth_stubs: 0x3230
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x5ca0
-  __TEXT.__const: 0x215fc
-  __TEXT.__cstring: 0x1935a
-  __TEXT.__oslogstring: 0x1a8f6
-  __TEXT.__unwind_info: 0x3ae8
+  __TEXT.__gcc_except_tab: 0x5d18
+  __TEXT.__const: 0x2167c
+  __TEXT.__cstring: 0x1958c
+  __TEXT.__oslogstring: 0x1a95c
+  __TEXT.__unwind_info: 0x3b50
   __TEXT.__eh_frame: 0x110
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x1ca1
   __TEXT.__objc_methtype: 0x11e8
   __TEXT.__objc_stubs: 0x1fa0
   __DATA_CONST.__got: 0x3110
-  __DATA_CONST.__const: 0x69b0
+  __DATA_CONST.__const: 0x69d8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x818
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1900
+  __DATA_CONST.__objc_arraydata: 0x50
+  __AUTH_CONST.__auth_got: 0x1928
   __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x2040
-  __AUTH_CONST.__cfstring: 0x93c0
+  __AUTH_CONST.__const: 0x2130
+  __AUTH_CONST.__cfstring: 0x9540
   __AUTH_CONST.__objc_const: 0xae0
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x208370
   __DATA.__bss: 0xe1
-  __DATA.__common: 0x68
+  __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x118
   __DATA_DIRTY.__bss: 0x988

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5513
-  Symbols:   9047
-  CStrings:  6221
+  Functions: 5538
+  Symbols:   9082
+  CStrings:  6237
 
Symbols:
+ __ZN18H16ISPFirmwareWork23verifyAndCreateFilepathEPcjS0_
+ _kFigCaptureStreamProperty_MultiIlluminantWhiteBalanceEnabled
+ __ZN22NvmPeridotInputFactory7pDeviceE
+ _read
+ _PDPeridotCalibCopySerialNumber
+ _write
+ __ZN17JasperCalibration15nvmToDictionaryEPN6H16ISP12H16ISPDeviceE
+ _open
+ _lseek
+ _PDPeridotCalibCalibrationBlobsFromNVM
- _kFigCaptureStreamMetadata_AutoWhiteBalanceEnabled
- _fseek
CStrings:
+ "%!s(MISSING) - Invalid write length (%!d(MISSING))\n"
+ "\tSerial numbers sized mismatch"
+ "../"
+ "\tDefault calibration from NVM: failed to create calibration from NVM"
+ "\tCached Serial Number: %!s(MISSING), calibration: %!s(MISSING)"
+ "./"
+ "/private/var/mobile/Media/DCIM"
+ "\tDefault calibration from NVM: created pseudo-FDR from NVM"
+ "\tValidating SN (registry vs cache)"
+ "\tValidating Calibration UUID (FDR vs cache)"
+ "\tDefault calibration from NVM: failed to read device NVM"
+ "%!s(MISSING) - Failed file path integrity check\n"
+ "\tDefault calibration from NVM: device is not ready or no ToF channel found"
+ "\tCan't read serial number from cache"
+ "\tDefault calibration from NVM: failed to read sensor NVM"
+ "FdrForTof"
+ "\tLooking for calibration in NVM\n"
+ "%!s(MISSING) - Invalid read length (%!d(MISSING))\n"
- "ab"
- "/var/mobile/Media/DCIM"

```
