## FPCKService

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/FPCKService`

```diff

-2732.80.49.0.0
-  __TEXT.__text: 0x1588
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0xec
+2882.100.384.0.0
+  __TEXT.__text: 0x15b4
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x360
+  __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x3a
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x7cc
-  __TEXT.__objc_methtype: 0x322
+  __TEXT.__objc_methname: 0x7fa
+  __TEXT.__objc_methtype: 0x339
   __TEXT.__oslogstring: 0x16b
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__cstring: 0xdd
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x230
   __DATA_CONST.__cfstring: 0x60

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x810
-  __DATA.__objc_selrefs: 0x150
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_const: 0x598
+  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation
-  - /System/Library/PrivateFrameworks/FPFS.framework/FPFS
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 35
-  Symbols:   95
-  CStrings:  154
+  Symbols:   100
+  CStrings:  158
 
Symbols:
+ _fpfs_adopt_log
+ _fpfs_create_log_for_provider
+ _fpfs_current_or_default_log
+ _objc_retainAutorelease
+ _objc_retain_x26
+ _objc_unsafeClaimAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
+ "\x11\x12\x16"
+ "@\"NSObject<OS_os_log>\""
+ "UTF8String"
+ "_log"
+ "fp_obfuscatedProviderDomainID"
- "\x11\x11\x16"

```
