## restoreserviced

> `/usr/libexec/restoreserviced`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0x13b20
-  __TEXT.__auth_stubs: 0xef0
+38.0.0.0.0
+  __TEXT.__text: 0x12f78
+  __TEXT.__auth_stubs: 0xe70
   __TEXT.__objc_stubs: 0x1760
-  __TEXT.__objc_methlist: 0xc64
-  __TEXT.__const: 0xb88
-  __TEXT.__cstring: 0x75ec
+  __TEXT.__objc_methlist: 0xc34
+  __TEXT.__const: 0xb7c
+  __TEXT.__cstring: 0x73ed
   __TEXT.__oslogstring: 0x34d
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x1707
-  __TEXT.__objc_classname: 0x11e
-  __TEXT.__objc_methtype: 0x798
-  __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__auth_got: 0x788
+  __TEXT.__objc_methname: 0x1701
+  __TEXT.__objc_classname: 0x10f
+  __TEXT.__objc_methtype: 0x789
+  __TEXT.__unwind_info: 0x518
+  __DATA_CONST.__auth_got: 0x748
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0xc78
-  __DATA_CONST.__cfstring: 0x3560
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__cfstring: 0x36a0
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1350
-  __DATA.__objc_selrefs: 0x6f8
+  __DATA.__objc_const: 0x12b0
+  __DATA.__objc_selrefs: 0x708
   __DATA.__objc_ivar: 0xd4
-  __DATA.__objc_data: 0x4b0
+  __DATA.__objc_data: 0x460
   __DATA.__data: 0x5e8
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36167874-4F43-383D-BF18-6F7CC46C9165
-  Functions: 493
-  Symbols:   299
-  CStrings:  1790
+  UUID: BBFCC9F3-32CB-3581-90CE-996AC4F31082
+  Functions: 478
+  Symbols:   291
+  CStrings:  1793
 
Symbols:
+ _dlclose
+ _kAMAuthInstallApParameterCertificateEpoch
+ _mach_absolute_time
- _CC_SHA1_Final
- _CC_SHA1_Init
- _CC_SHA1_Update
- _CFMakeCollectable
- _IOConnectCallStructMethod
- _OBJC_CLASS_$_NSDate
- _memcpy
- _memmove
- _mmap
- _munmap
- _realloc
CStrings:
+ "%@ property is not a CFData\n"
+ "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
+ "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
+ "Disable"
+ "Enable"
+ "IsTwoStageSupported"
+ "Q"
+ "Runtime check for two-stage support: %s"
+ "TQ,V_layout"
+ "Updater %@ should be skipped for %s.."
+ "UpdaterSupported"
+ "Vinyl updaterSupported missing or returned not supported\n"
+ "_layout"
+ "appendImages:"
+ "certificate-security-mode"
+ "could not create CFNumber for %@\n"
+ "data"
+ "layout"
+ "ramrod_update_twostage_enabled"
+ "setLayout:"
+ "snap-has-combined-images"
+ "snapHasCombinedImages"
+ "unable to lookup %@ property\n"
+ "v24@0:8Q16"
+ "waitUntilTime:"
- "%s returned an error when writing img3 object"
- "%s: flashing %c%c%c%c data (length = 0x%lx)\n"
- "%s: unable to create CFData for img3 ticket"
- "%s: unable to create img3 ticket"
- "-[IMG3NorUpdater _encodeAndWriteIMG3Data:isLLB:isTicket:withError:]"
- "-[IMG3NorUpdater updateBootFirmwareWithCallback:context:error:]"
- "AppleImage3NORAccess"
- "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
- "B40@0:8^{__CFData=}16B24B28^@32"
- "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
- "Failed to instantiate img3 image"
- "Failed to read img3 type"
- "Failed to write Img3 Firmware data"
- "Failed to write Img3 Ticket data"
- "Failed to write Img3 boot data"
- "IMG3NorUpdater"
- "Img3 Ticket Data updated"
- "Img3 encoding failed"
- "SPI writer was unavailable at write-time."
- "Unexpected imageType in firmware"
- "_encodeAndWriteIMG3Data:isLLB:isTicket:withError:"
- "could not create CFNumber for esdm-fuses\n"
- "could not finalize ticket img3"
- "distantFuture"
- "esdm-fuses property is not a CFData\n"
- "failed to create data tag for ticket"
- "failed to create img3\n"
- "ramrod_ticket_create_img3"
- "timeIntervalSinceNow"
- "unable to lookup esdm-fuses property\n"
- "unable to mmap %zu bytes for image3 data"
- "waitUntilDate:"

```
