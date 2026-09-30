## mediaanalysisd-generation

> `/System/Library/PrivateFrameworks/MediaAnalysisGeneration.framework/XPCServices/mediaanalysisd-generation.xpc/mediaanalysisd-generation`

```diff

-405.2.1.0.0
-  __TEXT.__text: 0x7764
-  __TEXT.__auth_stubs: 0xa50
+405.3.1.0.0
+  __TEXT.__text: 0x7b04
+  __TEXT.__auth_stubs: 0xae0
   __TEXT.__delay_stubs: 0xc0
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_stubs: 0x660
-  __TEXT.__objc_methlist: 0x234
-  __TEXT.__gcc_except_tab: 0x498
+  __TEXT.__objc_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x212
-  __TEXT.__oslogstring: 0x493
-  __TEXT.__cstring: 0x2cd
+  __TEXT.__gcc_except_tab: 0x4b4
+  __TEXT.__cstring: 0x2fd
+  __TEXT.__oslogstring: 0x4c3
   __TEXT.__objc_classname: 0xa9
-  __TEXT.__objc_methname: 0x66b
+  __TEXT.__objc_methname: 0x692
   __TEXT.__objc_methtype: 0x291
   __TEXT.__swift5_typeref: 0x13c
   __TEXT.__swift5_capture: 0x98

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__unwind_info: 0x2e8
   __TEXT.__eh_frame: 0x2c0
-  __DATA_CONST.__auth_got: 0x550
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__auth_got: 0x598
+  __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0x2d8
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x3d8
-  __DATA.__objc_selrefs: 0x258
+  __DATA.__objc_selrefs: 0x268
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x1c8
   __DATA.__data: 0x1f4
-  __DATA.__bss: 0x1b0
+  __DATA.__bss: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 101A18E6-518F-3DDE-852D-FBC9740DEBBB
-  Functions: 132
-  Symbols:   180
-  CStrings:  186
+  UUID: 64B523E5-BE47-3C95-BDB6-58351EE66554
+  Functions: 140
+  Symbols:   190
+  CStrings:  190
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
+ _exit
+ _objc_release_x1
+ _os_transaction_create
CStrings:
+ "[MADGenerationXPCService] Idle timer fired – exiting"
+ "cancelIdleExitTimer"
+ "com.apple.mediaanalysisd-generation.idle-exit"
+ "startIdleExitTimer"

```
