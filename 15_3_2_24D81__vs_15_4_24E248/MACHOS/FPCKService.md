## FPCKService

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/Contents/MacOS/FPCKService`

```diff

-2732.81.1.0.0
-  __TEXT.__text: 0x1da8
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0xec
+2882.101.2.0.0
+  __TEXT.__text: 0x1dec
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x3a
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x841
-  __TEXT.__objc_methtype: 0x322
+  __TEXT.__objc_methname: 0x86f
+  __TEXT.__objc_methtype: 0x339
   __TEXT.__oslogstring: 0x214
   __TEXT.__cstring: 0x120
   __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x180
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x278
   __DATA_CONST.__cfstring: 0x60

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x810
-  __DATA.__objc_selrefs: 0x180
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_const: 0x598
+  __DATA.__objc_selrefs: 0x230
+  __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/Versions/A/EmojiFoundation
-  - /System/Library/PrivateFrameworks/FPFS.framework/Versions/A/FPFS
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/Versions/A/FileProviderDaemon
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage
   - /System/Library/PrivateFrameworks/SpaceAttribution.framework/Versions/A/SpaceAttribution
-  - /usr/lib/libEndpointSecuritySystem.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 12EDE1CE-7633-3F03-B1FF-E1629960D5A2
+  UUID: EB0F9B11-BB39-384A-A362-CF218FC952E9
   Functions: 51
-  Symbols:   80
-  CStrings:  170
+  Symbols:   84
+  CStrings:  174
 
Symbols:
+ _fpfs_adopt_log
+ _fpfs_create_log_for_provider
+ _fpfs_current_or_default_log
+ _objc_unsafeClaimAutoreleasedReturnValue
Functions:
~ sub_100004a64 -> sub_100001494 : 1004 -> 996
~ sub_100004e70 -> sub_100001898 : 452 -> 472
~ sub_1000050b0 -> sub_100001aec : 464 -> 516
~ sub_1000053a0 -> sub_100001e10 : 2092 -> 2084
~ sub_100006374 -> sub_100002ddc : 140 -> 152
~ sub_100006400 -> sub_100002e74 : 128 -> 124
~ sub_100006580 -> sub_100002ff0 : 124 -> 128
CStrings:
+ "@\"NSObject<OS_os_log>\""
+ "UTF8String"
+ "_log"
+ "fp_obfuscatedProviderDomainID"

```
