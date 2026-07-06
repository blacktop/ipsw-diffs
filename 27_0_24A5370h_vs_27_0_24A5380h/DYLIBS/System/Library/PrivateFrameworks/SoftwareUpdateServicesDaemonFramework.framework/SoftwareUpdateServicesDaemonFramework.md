## SoftwareUpdateServicesDaemonFramework

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesDaemonFramework.framework/SoftwareUpdateServicesDaemonFramework`

```diff

-  __TEXT.__text: 0x626e0
+  __TEXT.__text: 0x625b0
   __TEXT.__objc_methlist: 0x505c
   __TEXT.__const: 0x100
   __TEXT.__cstring: 0x10a01
   __TEXT.__oslogstring: 0x852
   __TEXT.__gcc_except_tab: 0x760
-  __TEXT.__unwind_info: 0x19e8
+  __TEXT.__unwind_info: 0x19e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1368
+  __DATA_CONST.__const: 0x1340
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__got: 0xab0
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x89a0
-  __AUTH_CONST.__objc_const: 0x8198
+  __AUTH_CONST.__objc_const: 0x81a8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x508
-  __AUTH.__objc_data: 0xc30
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x340
   __DATA.__data: 0x7e0
-  __DATA.__bss: 0xb8
+  __DATA.__bss: 0x38
+  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2107
-  Symbols:   7380
+  Functions: 2106
+  Symbols:   7378
   CStrings:  2580
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[SUInstaller currentInstallOptions]
+ _objc_msgSend$currentInstallOptions
+ _objc_msgSend$reportOTAStartedDownloadingEvent:
- -[SUDownloader networkChangedFromNetworkType:toNetworkType:]
- ___60-[SUDownloader networkChangedFromNetworkType:toNetworkType:]_block_invoke
- ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$allowCellularDownload

```
