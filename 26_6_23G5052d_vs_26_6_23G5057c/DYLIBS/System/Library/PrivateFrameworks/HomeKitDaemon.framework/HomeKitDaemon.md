## HomeKitDaemon

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon`

```diff

-  __TEXT.__text: 0x110b318
+  __TEXT.__text: 0x110b314
   __TEXT.__auth_stubs: 0x7ca0
   __TEXT.__objc_methlist: 0x9782c
   __TEXT.__dlopen_cstrs: 0x130

   __TEXT.__unwind_info: 0x34fa0
   __TEXT.__eh_frame: 0x25714
   __TEXT.__objc_classname: 0x1d3a6
-  __TEXT.__objc_methname: 0x16626c
+  __TEXT.__objc_methname: 0x16625c
   __TEXT.__objc_methtype: 0x2fb5a
   __TEXT.__objc_stubs: 0xc7ce0
-  __DATA_CONST.__got: 0x8018
+  __DATA_CONST.__got: 0x8020
   __DATA_CONST.__const: 0x1d0b0
   __DATA_CONST.__objc_classlist: 0x4b98
   __DATA_CONST.__objc_catlist: 0x360

   __AUTH_CONST.__const: 0x2b980
   __AUTH_CONST.__cfstring: 0x5e7e0
   __AUTH_CONST.__objc_const: 0x123048
-  __AUTH_CONST.__objc_intobj: 0x3e70
+  __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_arrayobj: 0x960
   __AUTH_CONST.__objc_doubleobj: 0x1d0
   __AUTH_CONST.__objc_dictobj: 0x2080

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 65114
-  Symbols:   180977
+  Symbols:   180978
   CStrings:  100065
 
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
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
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
