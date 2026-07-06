## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/Versions/A/CoreCaptureDaemon`

```diff

-  __TEXT.__text: 0x5b70c
-  __TEXT.__const: 0x53e
+  __TEXT.__text: 0x5c200
+  __TEXT.__const: 0x63e
   __TEXT.__gcc_except_tab: 0x4a8
-  __TEXT.__oslogstring: 0xb827
-  __TEXT.__cstring: 0xbc62
-  __TEXT.__unwind_info: 0x808
+  __TEXT.__oslogstring: 0xba48
+  __TEXT.__cstring: 0xbe6a
+  __TEXT.__unwind_info: 0x810
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x338
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1318
+  __AUTH_CONST.__const: 0x1350
   __AUTH_CONST.__cfstring: 0xc00
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__auth_got: 0xa20
   __DATA.__common: 0x20
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__common: 0x1c
-  __DATA_DIRTY.__bss: 0x288
+  __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 628
-  Symbols:   1223
-  CStrings:  2037
+  Functions: 632
+  Symbols:   1230
+  CStrings:  2048
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ GCC_except_table280
+ GCC_except_table310
+ GCC_except_table419
+ GCC_except_table430
+ GCC_except_table433
+ GCC_except_table435
+ GCC_except_table436
+ GCC_except_table472
+ GCC_except_table481
+ GCC_except_table483
+ GCC_except_table488
+ GCC_except_table490
+ GCC_except_table493
+ GCC_except_table503
+ GCC_except_table513
+ GCC_except_table551
+ GCC_except_table579
+ GCC_except_table589
+ GCC_except_table601
+ GCC_except_table602
+ GCC_except_table626
+ GCC_except_table627
+ GCC_except_table70
+ __ZN15CCPipeInterface15extractPipeNameEPK10__CFStringPcm
+ __ZN15CCPipeInterface16extractOwnerNameEPK10__CFStringPcm
+ __ZN15CCPipeInterface16setDispatchQueueEb
+ __ZN15CCPipeInterface18resetDispatchQueueEb
+ ____ZN15CCPipeInterface18resetDispatchQueueEb_block_invoke
+ _dispatch_set_target_queue
- GCC_except_table276
- GCC_except_table306
- GCC_except_table415
- GCC_except_table426
- GCC_except_table427
- GCC_except_table429
- GCC_except_table432
- GCC_except_table468
- GCC_except_table475
- GCC_except_table477
- GCC_except_table482
- GCC_except_table484
- GCC_except_table489
- GCC_except_table491
- GCC_except_table509
- GCC_except_table547
- GCC_except_table575
- GCC_except_table585
- GCC_except_table597
- GCC_except_table598
- GCC_except_table622
- GCC_except_table623
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
