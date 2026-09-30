## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-593.0.1.0.0
-  __TEXT.__text: 0x8cd8
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x4f0
+595.0.2.0.0
+  __TEXT.__text: 0x89b0
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x510
   __TEXT.__const: 0x50
-  __TEXT.__objc_methname: 0xe59
-  __TEXT.__oslogstring: 0xa37
+  __TEXT.__objc_methname: 0xe8f
+  __TEXT.__oslogstring: 0xb51
   __TEXT.__objc_classname: 0xeb
   __TEXT.__objc_methtype: 0x373
   __TEXT.__cstring: 0x394
-  __TEXT.__gcc_except_tab: 0x5fc
-  __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__auth_got: 0x290
+  __TEXT.__gcc_except_tab: 0x558
+  __TEXT.__unwind_info: 0x1e8
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x168
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x378
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x880
-  __DATA.__objc_selrefs: 0x480
-  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_const: 0x8b0
+  __DATA.__objc_selrefs: 0x490
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x248
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 09E2CD94-2536-3945-BDB0-5306C264AACC
+  UUID: D0BC832F-0B8D-3A09-8688-4BD7D1E87A48
   Functions: 111
-  Symbols:   134
-  CStrings:  358
+  Symbols:   139
+  CStrings:  365
 
Symbols:
+ ___chkstk_darwin
+ _nw_parameters_create
+ _nw_parameters_set_source_application_by_bundle_id
+ _objc_retainAutorelease
+ _objc_retain_x28
CStrings:
+ "Attributing network usage to %@"
+ "Failed to set source application for network usage because %@ name is nil"
+ "Ignoring FindMy stop sharing error %@ for participant %@ because sharing was stopped automatically"
+ "Ignoring FindMy stop sharing error because sharing was stopped automatically"
+ "UTF8String"
+ "_bundleId"
+ "setNetworkAttributionWithClient:"

```
