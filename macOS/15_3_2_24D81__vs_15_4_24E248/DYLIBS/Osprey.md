## Osprey

> `/System/Library/PrivateFrameworks/Osprey.framework/Versions/A/Osprey`

```diff

 3400.4.1.0.0
-  __TEXT.__text: 0x20a11c
+  __TEXT.__text: 0x208d1c
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0xf98
-  __TEXT.__const: 0xab108
+  __TEXT.__objc_methlist: 0x1218
+  __TEXT.__const: 0xab0c8
   __TEXT.__cstring: 0x173c
   __TEXT.__oslogstring: 0x10a9
   __TEXT.__gcc_except_tab: 0x32c
-  __TEXT.__unwind_info: 0x918
-  __TEXT.__eh_frame: 0x110
+  __TEXT.__unwind_info: 0x930
+  __TEXT.__eh_frame: 0x108
   __TEXT.__objc_classname: 0x3ae
   __TEXT.__objc_methname: 0x2ce1
   __TEXT.__objc_methtype: 0xd60

   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa10
+  __DATA_CONST.__objc_selrefs: 0xaf0
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x350
-  __AUTH_CONST.__const: 0x13c80
+  __AUTH_CONST.__const: 0x13c40
   __AUTH_CONST.__cfstring: 0xb80
-  __AUTH_CONST.__objc_const: 0x4748
+  __AUTH_CONST.__objc_const: 0x42c8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH.__objc_data: 0xa50
   __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0x7a8
   __DATA.__bss: 0x48
-  __DATA.__common: 0x1454
+  __DATA.__common: 0x144c
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A51F7FA0-8127-32F9-9786-5E4CC48E0AC5
-  Functions: 850
-  Symbols:   1606
+  UUID: FDED92AB-4A16-3E9D-B441-086A33202136
+  Functions: 855
+  Symbols:   1609
   CStrings:  1059
 
Symbols:
+ +[OspreyAnalytics reporter].cold.1
+ +[OspreyServiceConfiguration sharedConfiguration].cold.1
+ -[OspreyRequest initWithMethodName:].cold.1
+ OspreyLoggingInit.cold.1
+ OspreyMachAbsoluteTimeGetNanoseconds.cold.1
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPhS5_EEvT_T0_m
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne180100IPhS5_EEvT_T0_m

```
