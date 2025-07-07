## libSEUpdater.dylib

> `/usr/lib/updaters/libSEUpdater.dylib`

```diff

-57.1.25.0.0
-  __TEXT.__text: 0x66010
-  __TEXT.__auth_stubs: 0x1240
+57.1.26.0.0
+  __TEXT.__text: 0x65d80
+  __TEXT.__auth_stubs: 0x1210
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x654
-  __TEXT.__const: 0x7c88
-  __TEXT.__dlopen_cstrs: 0x50
+  __TEXT.__const: 0x7c78
   __TEXT.__oslogstring: 0x5e
-  __TEXT.__cstring: 0x806d
-  __TEXT.__gcc_except_tab: 0x7b08
-  __TEXT.__unwind_info: 0x1a28
+  __TEXT.__cstring: 0x8046
+  __TEXT.__gcc_except_tab: 0x7b00
+  __TEXT.__unwind_info: 0x1a18
   __TEXT.__objc_classname: 0x9a
   __TEXT.__objc_methname: 0x1263
   __TEXT.__objc_methtype: 0x707
   __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x5c0
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x580
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x930
+  __AUTH_CONST.__auth_got: 0x918
   __AUTH_CONST.__const: 0x3328
   __AUTH_CONST.__cfstring: 0x2180
   __AUTH_CONST.__objc_const: 0x8f0

   __DATA.__common: 0x18
   __DATA.__bss: 0x80
   __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__bss: 0x1588
+  __DATA_DIRTY.__bss: 0x1578
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libReverseProxyDevice.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A275B025-51F4-3A98-8954-FF672DFFA720
-  Functions: 1339
-  Symbols:   4379
-  CStrings:  1773
+  UUID: 1E8A72C2-DD20-36F7-ACAD-27A6A99DC487
+  Functions: 1336
+  Symbols:   4368
+  CStrings:  1770
 
Symbols:
+ _OBJC_CLASS_$_NFHardwareManager
+ _OBJC_CLASS_$_NFSecureElement
- __ZL21audit_stringNearField
- __ZL25getNFHardwareManagerClassv
- ____ZL20NearFieldLibraryCorePPc_block_invoke
- ____ZL25getNFHardwareManagerClassv_block_invoke
- ___block_descriptor_40_ea8_32r_e5_v8?0lr32l8
- __sl_dlopen
- _abort_report_np
- _objc_retain_x9
CStrings:
+ "Can't get weakly linked NFHM class, nothing to personalize\n"
- "Can't get softlinked NFHM class, nothing to personalize\n"
- "NFHardwareManager"
- "Unable to find class %s"
- "softlink:r:path:/System/Library/PrivateFrameworks/NearField.framework/NearField"

```
