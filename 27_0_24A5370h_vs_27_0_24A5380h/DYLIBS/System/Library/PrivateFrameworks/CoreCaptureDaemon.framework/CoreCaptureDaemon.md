## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-  __TEXT.__text: 0x5aea4
-  __TEXT.__const: 0x538
+  __TEXT.__text: 0x5b998
+  __TEXT.__const: 0x638
   __TEXT.__gcc_except_tab: 0x4d4
-  __TEXT.__oslogstring: 0xb4fa
-  __TEXT.__cstring: 0xb956
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__oslogstring: 0xb71b
+  __TEXT.__cstring: 0xbb5e
+  __TEXT.__unwind_info: 0x7d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x390
+  __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1230
+  __AUTH_CONST.__const: 0x1268
   __AUTH_CONST.__cfstring: 0xc40
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x9c0
+  __AUTH_CONST.__auth_got: 0x9c8
   __DATA.__data: 0x1
   __DATA.__common: 0x24
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__common: 0x14
-  __DATA_DIRTY.__bss: 0x298
+  __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 611
-  Symbols:   1314
-  CStrings:  2010
+  Functions: 615
+  Symbols:   1322
+  CStrings:  2021
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ GCC_except_table278
+ GCC_except_table355
+ GCC_except_table356
+ GCC_except_table403
+ GCC_except_table414
+ GCC_except_table417
+ GCC_except_table419
+ GCC_except_table420
+ GCC_except_table456
+ GCC_except_table465
+ GCC_except_table467
+ GCC_except_table472
+ GCC_except_table474
+ GCC_except_table477
+ GCC_except_table487
+ GCC_except_table497
+ GCC_except_table535
+ GCC_except_table563
+ GCC_except_table572
+ GCC_except_table584
+ GCC_except_table585
+ GCC_except_table609
+ GCC_except_table610
+ GCC_except_table70
+ __ZN15CCPipeInterface15extractPipeNameEPK10__CFStringPcm
+ __ZN15CCPipeInterface16extractOwnerNameEPK10__CFStringPcm
+ __ZN15CCPipeInterface16setDispatchQueueEb
+ __ZN15CCPipeInterface18resetDispatchQueueEb
+ ____ZN15CCPipeInterface18resetDispatchQueueEb_block_invoke
+ _dispatch_set_target_queue
- GCC_except_table274
- GCC_except_table351
- GCC_except_table352
- GCC_except_table399
- GCC_except_table410
- GCC_except_table411
- GCC_except_table413
- GCC_except_table416
- GCC_except_table452
- GCC_except_table459
- GCC_except_table461
- GCC_except_table466
- GCC_except_table468
- GCC_except_table473
- GCC_except_table475
- GCC_except_table493
- GCC_except_table531
- GCC_except_table559
- GCC_except_table568
- GCC_except_table580
- GCC_except_table581
- GCC_except_table605
- GCC_except_table606
- GCC_except_table72
- __ZN15CCPipeInterface16setDispatchQueueEv
CStrings:
+ "CCDaemon::%s initial scan not complete, staying active"
+ "CCPipeInterface::resetDispatchQueue re-targeted dispatch source to capture queue entry:%u Owner:%s Pipe:%s\n"
+ "CCPipeInterface::resetDispatchQueue re-targeted notification port to capture queue entry:%u Owner:%s Pipe:%s\n"
+ "CCPipeInterface::setDispatchQueue entry:%u Owner:%s Pipe:%s\n"
+ "CCPipeInterface::setDispatchQueue failed to create a serial dispatch queue for continuous pipe entry:%u Owner:%s Pipe:%s\n"
+ "CCPipeInterface::setDispatchQueue re-targeted dispatch source to continuous queue entry:%u Owner:%s Pipe:%s\n"
+ "CCPipeInterface::setDispatchQueue re-targeted notification port to continuous queue entry:%u Owner:%s Pipe:%s\n"
+ "result=init_scan_pending"
- "CCPipeInterface::setDispatchQueue entry:%u fConnectRef(%d)\n"
- "CCPipeInterface::setDispatchQueue failed to create a serial dispatch queue for continuous pipe\n"

```
