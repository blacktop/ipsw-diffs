## HomeKitDaemonLegacy

> `/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy`

```diff

-  __TEXT.__text: 0xb92ae8
+  __TEXT.__text: 0xb92ae4
   __TEXT.__auth_stubs: 0x4e60
   __TEXT.__objc_methlist: 0x73dfc
   __TEXT.__dlopen_cstrs: 0x130

   __TEXT.__unwind_info: 0x22c08
   __TEXT.__eh_frame: 0x4cbc
   __TEXT.__objc_classname: 0x130c5
-  __TEXT.__objc_methname: 0x1206cd
+  __TEXT.__objc_methname: 0x1206bd
   __TEXT.__objc_methtype: 0x24e42
   __TEXT.__objc_stubs: 0xa7b20
-  __DATA_CONST.__got: 0x67e0
+  __DATA_CONST.__got: 0x67e8
   __DATA_CONST.__const: 0x154a8
   __DATA_CONST.__objc_classlist: 0x34e8
   __DATA_CONST.__objc_catlist: 0x278

   __AUTH_CONST.__cfstring: 0x4da60
   __AUTH_CONST.__objc_const: 0xd2570
   __AUTH_CONST.__objc_arrayobj: 0x8a0
-  __AUTH_CONST.__objc_intobj: 0x30d8
+  __AUTH_CONST.__objc_intobj: 0x30c0
   __AUTH_CONST.__objc_dictobj: 0x1838
   __AUTH_CONST.__objc_doubleobj: 0x160
   __AUTH_CONST.__objc_floatobj: 0x10

   __AUTH.__data: 0x1018
   __DATA.__objc_ivar: 0x8128
   __DATA.__data: 0x11578
-  __DATA.__bss: 0x97a8
+  __DATA.__bss: 0x97b0
   __DATA.__common: 0x280
   __DATA_DIRTY.__objc_data: 0x10fd0
   __DATA_DIRTY.__data: 0x1120

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 44789
-  Symbols:   142952
+  Symbols:   142953
   CStrings:  80272
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _kDefaultOtaProviderEndpoint
+ _objc_msgSend$startBusyImageResponseTimer:timeInterval:requestParams:queue:
- _objc_msgSend$startBusyImageResponseTimer:timeInterval:endpoint:requestParams:queue:
Functions:
~ ___118-[HMDMatterSoftwareUpdateProviderDelegate queryImageWithPairing:requestParams:queue:initiationType:completionHandler:]_block_invoke : 5452 -> 5456
~ -[HMDMatterSoftwareUpdateProviderDelegate manageBusyImageResponses:initiationType:requestParams:queue:completionHandler:] : 448 -> 440
CStrings:
+ "startBusyImageResponseTimer:timeInterval:requestParams:queue:"
- "startBusyImageResponseTimer:timeInterval:endpoint:requestParams:queue:"

```
