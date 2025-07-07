## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-916.40.22.0.2
-  __TEXT.__text: 0x175e8
-  __TEXT.__auth_stubs: 0x800
+916.60.6.0.0
+  __TEXT.__text: 0x18e14
+  __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0x384
-  __TEXT.__cstring: 0x3a32
+  __TEXT.__cstring: 0x4391
   __TEXT.__const: 0x128
   __TEXT.__oslogstring: 0x7
-  __TEXT.__unwind_info: 0x604
+  __TEXT.__unwind_info: 0x610
   __TEXT.__objc_classname: 0x84
   __TEXT.__objc_methname: 0x9f9
   __TEXT.__objc_methtype: 0x6d2

   __DATA_CONST.__objc_selrefs: 0x298
   __AUTH_CONST.__cfstring: 0xde0
   __AUTH_CONST.__objc_const: 0x1a8
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH.__objc_data: 0x190
   __DATA.__objc_classrefs: 0x50
   __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x98
-  __DATA.__data: 0x27
+  __DATA.__data: 0x30
   __DATA.__bss: 0xb64
-  __DATA.__common: 0x1
+  __DATA.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 072274DB-6A53-3B7B-B9B3-55EAC4D5BAB3
-  Functions: 776
-  Symbols:   1388
-  CStrings:  745
+  UUID: 8B547065-C395-35DC-A5BE-9E386A7A3CC3
+  Functions: 777
+  Symbols:   1395
+  CStrings:  812
 
Symbols:
+ _inRestore
+ _logLevel
+ _print_fw_update_regs
+ _printf
+ _putchar
+ _puts
CStrings:
+ "%02X"
+ "Ace in boot mode: Can't be updated!"
+ "Ace is in ADFU mode, trying to read mode again after 1000ms"
+ "Ace is in APP mode, trying to read mode again after 1000ms"
+ "Ace is in boot mode, trying to read mode again after 1000ms"
+ "BDID=0x%llX\n"
+ "Begin Manifest Request"
+ "Buffer size = 0! "
+ "Built and Staged the personalized FW"
+ "CPFM=0x%llX [8b]\n"
+ "CPID=0x%llX [16b]\n"
+ "CRPV=0x%llX [16b]\n"
+ "Cannot find start of buffer"
+ "Cannot find start of buffer\n"
+ "Cannot find start_of_needle"
+ "Cannot find start_of_needle\n"
+ "Couldn't find RID for service, skipping!"
+ "Device error RID=0x%d\n"
+ "ECID=0x%llX\n"
+ "Error allocating accessory"
+ "Error allocating info"
+ "Final params, after accounting for any endianness quirks:"
+ "Final params, after accounting for any endianness quirks:\n"
+ "Finished AC"
+ "Finished DL"
+ "Finished Patch"
+ "Found no matching device tree nodes"
+ "Found no matching services"
+ "Found updatable Ace based on usbc-update-protocol value"
+ "Ignoring initialization option to skip flashing same verison based on bootarg"
+ "Offering FIRM to controller"
+ "Offering IM4M to controller"
+ "Overriding LUN to 1 since it was 0 or unspecified"
+ "PREV=0x%llX [8b]\n"
+ "Payload Data complete"
+ "Persistent flash successful"
+ "Reading bytes failed, nibbles_in_field=0x%zX, buffer=%p, *buffer=0x%hhX, buffer_size=0x%zX, count=0x%zX, start_of_buf=%s\n"
+ "Reading of start_of_buffer failed"
+ "Reading of start_of_buffer failed\n"
+ "Received some payload data"
+ "Received the whole IM4M"
+ "SDOM=0x%llX [8b]\n"
+ "Setting payload index"
+ "Skipping firmware update due to version number check"
+ "Skipping updatable check due to bootarg"
+ "Skipping updatable check, since we aren't in restore"
+ "Stage image"
+ "Staging FW in personalization backend"
+ "UART HPM RID%d in VOUT, GAID skipped and APP mode check will be skipped\n"
+ "UART HPMs not found, treating as non-fatal"
+ "UART HPMs not found, treating as non-fatal\n"
+ "USB string: %s\n"
+ "USBCUpdate: Calling Asset Fully Staged from Processing Notification"
+ "WARNING: Unexpected tag for offered Dynamic Asset"
+ "Waiting for processing notification before closing"
+ "Workaround: not putting any bits of the digest list into the image, due to no personalization"
+ "Workaround: setting digest list length to 0 because we aren't doing personalization"
+ "apBORD=0x%X, apChip=0x%X\n"
+ "boardID=0x%llX\n"
+ "chipID=0x%X\n"
+ "fAssetProcessingNotificationAck called"
+ "fAssetReleased2 called"
+ "libUSBCUpdate: Fully torn down"
+ "libusbcupdate_log"
+ "nibbles_in_field=0x%zX, buffer=%p, *buffer=0x%hhX, buffer_size=0x%zX, count=0x%zX, start_of_buf=%s\n"
+ "otpBuf:"
+ "otpBuf:\n"
+ "pStatus=%d, secMode=%d, SDOM=0x%X, PREV=0x%X\n"
+ "uart-hpm-rids"
- "Failed to reset dangling UART HPMs, treating as non-fatal: 0x%x\n"
- "uart-ace-rids"

```
