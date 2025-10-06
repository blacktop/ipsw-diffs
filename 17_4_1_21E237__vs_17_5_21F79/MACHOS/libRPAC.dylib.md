## libRPAC.dylib

> `/usr/lib/libRPAC.dylib`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0x8b104
+57.3.0.0.0
+  __TEXT.__text: 0x8b2d0
   __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_stubs: 0x180
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x364d
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__const: 0x11c0
+  __TEXT.__cstring: 0x368f
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__const: 0x1198
   __TEXT.__objc_methname: 0x128
   __TEXT.__oslogstring: 0x1d
-  __TEXT.__unwind_info: 0x224
-  __DATA_CONST.__auth_got: 0x438
+  __TEXT.__objc_classname: 0x1
+  __TEXT.__unwind_info: 0x230
+  __DATA_CONST.__auth_got: 0x440
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3d0
+  __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x18

   __DATA.__data: 0x7c4
   __DATA.__interpose: 0x90
   __DATA.__common: 0x800e8
-  __DATA.__bss: 0x4005f0
+  __DATA.__bss: 0x4005f8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A99F4824-52FB-324B-9C6A-5F5A45284578
-  Functions: 174
-  Symbols:   510
-  CStrings:  441
+  UUID: 0940BFBF-4827-39B9-800F-AFF69B2C043A
+  Functions: 175
+  Symbols:   513
+  CStrings:  445
 
Symbols:
+ GCC_except_table2
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_96_e8_32r_e5_v8?0lr32l8
+ ___objc_personality_v0
+ __block_descriptor_tmp.16
+ __block_descriptor_tmp.23
+ __block_literal_global.18
+ __block_literal_global.25
+ _dispatch_async_and_wait
+ _dispatch_block_create_with_qos_class
+ _dispatch_workloop_create
+ _isSystemFrame
+ generateCulledBacktrace.issueWorkloop
+ generateCulledBacktrace.startingQoSClass
- __block_descriptor_tmp.12
- __block_descriptor_tmp.13
- __block_descriptor_tmp.17
- __block_descriptor_tmp.22
- __block_literal_global.15
- __block_literal_global.19
- _dispatch_queue_attr_make_with_qos_class
- _dispatch_queue_create
- _dispatch_sync
- generateCulledBacktrace.issueQueue
CStrings:
+ "/Developer"
+ "/System"
+ "/usr"
+ "IssueGeneration.m"
+ "Log type: %d; QoS class of thread: %d\n"
+ "RPAC issue generation workloop"
- "IssueGeneration.c"
- "RPAC issue generation queue"

```
