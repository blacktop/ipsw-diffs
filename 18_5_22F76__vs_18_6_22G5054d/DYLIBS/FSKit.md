## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-531.120.18.0.2
-  __TEXT.__text: 0x3c95c
+531.140.6.0.0
+  __TEXT.__text: 0x3c9c8
   __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x4324
-  __TEXT.__const: 0x370
-  __TEXT.__gcc_except_tab: 0xf00
+  __TEXT.__objc_methlist: 0x4334
+  __TEXT.__const: 0x380
+  __TEXT.__gcc_except_tab: 0xef4
   __TEXT.__cstring: 0x3e7f
   __TEXT.__oslogstring: 0x2cc5
   __TEXT.__swift5_typeref: 0x1d1

   __TEXT.__unwind_info: 0x11c8
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x825
-  __TEXT.__objc_methname: 0x9376
+  __TEXT.__objc_methname: 0x9386
   __TEXT.__objc_methtype: 0x325e
-  __TEXT.__objc_stubs: 0x5400
+  __TEXT.__objc_stubs: 0x5420
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0x12f8
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22a8
+  __DATA_CONST.__objc_selrefs: 0x22b0
   __DATA_CONST.__objc_protorefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x30

   __AUTH.__objc_data: 0x1158
   __AUTH.__data: 0x80
   __DATA.__objc_ivar: 0x3f4
-  __DATA.__data: 0xf68
+  __DATA.__data: 0xf58
   __DATA.__bss: 0x320
   __DATA_DIRTY.__objc_data: 0x438
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 522DF87F-AF99-365F-AD4E-A59340E8D924
-  Functions: 1820
-  Symbols:   5846
-  CStrings:  3069
+  UUID: 24DAA1BD-DCA6-3014-8B27-E2CDA5AFB0AD
+  Functions: 1822
+  Symbols:   5850
+  CStrings:  3070
 
Symbols:
+ -[FSBlockDeviceResource(Project) terminateLocked]
+ GCC_except_table105
+ GCC_except_table72
+ ___43-[FSBlockDeviceResource(Private) terminate]_block_invoke
+ _objc_msgSend$terminateLocked
- GCC_except_table103
- GCC_except_table80
Functions:
~ _deviceNotificationCallback : 948 -> 988
+ -[FSBlockDeviceResource(Project) terminateLocked]
~ -[FSBlockDeviceResource(Private) terminate] : 196 -> 188
+ +[FSBlockDeviceBufferResource supportsSecureCoding]
~ -[FSItem init] : 172 -> 120
CStrings:
+ "terminateLocked"

```
