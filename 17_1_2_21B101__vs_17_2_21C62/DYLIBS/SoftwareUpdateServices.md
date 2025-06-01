## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-746.40.12.0.0
-  __TEXT.__text: 0x405b8
+746.60.8.0.0
+  __TEXT.__text: 0x40640
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x4d2c
-  __TEXT.__cstring: 0xec97
+  __TEXT.__objc_methlist: 0x4d44
+  __TEXT.__cstring: 0xed32
   __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x740
   __TEXT.__oslogstring: 0x52f
   __TEXT.__unwind_info: 0x1640
   __TEXT.__objc_classname: 0xa02
-  __TEXT.__objc_methname: 0xdae5
+  __TEXT.__objc_methname: 0xdb13
   __TEXT.__objc_methtype: 0x21df
   __TEXT.__objc_stubs: 0x9ea0
   __DATA_CONST.__got: 0x270

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc020
-  __DATA_CONST.__objc_selrefs: 0x3108
+  __DATA_CONST.__objc_const: 0xc040
+  __DATA_CONST.__objc_selrefs: 0x3118
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x9aa0
+  __AUTH_CONST.__cfstring: 0x9b20
   __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__objc_const: 0x21e8
   __AUTH_CONST.__objc_intobj: 0xc0

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 64FA9AEC-5402-3B5B-92F3-BBD6D535121E
-  Functions: 2064
-  Symbols:   7467
-  CStrings:  5425
+  UUID: 0B1A31C3-BE41-3899-867F-3D0709A921B4
+  Functions: 2066
+  Symbols:   7471
+  CStrings:  5435
 
Symbols:
+ -[SUPreferences autoInstallRetryDelay]
+ -[SUPreferences disableAutoInstallJitter]
CStrings:
+ "Delay before scheduling another auto installation"
+ "If set to true, disable jitter for auto installations"
+ "SUAutoInstallRetryDelay"
+ "SUDisableAutoInstallJitter"
+ "autoInstallRetryDelay"
+ "disableAutoInstallJitter"

```
