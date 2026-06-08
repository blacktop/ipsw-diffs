## transitd

> `/usr/libexec/transitd`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x3794
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x860
+51.0.0.0.0
+  __TEXT.__text: 0x3c80
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x880
   __TEXT.__objc_methlist: 0x19c
-  __TEXT.__objc_methname: 0x75e
-  __TEXT.__cstring: 0x4ee
+  __TEXT.__const: 0x38
+  __TEXT.__objc_methname: 0x76a
+  __TEXT.__cstring: 0x3f8
+  __TEXT.__oslogstring: 0x1a8
   __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methtype: 0x108
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__const: 0x28
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0x220
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2f0
-  __DATA.__objc_selrefs: 0x268
+  __DATA.__objc_selrefs: 0x270
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x14
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xd0
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 30C16475-8F48-3332-B868-E45A42AEF225
-  Functions: 71
-  Symbols:   161
+  UUID: 571529E6-2C3F-3F17-A564-D0D6019100C1
+  Functions: 82
+  Symbols:   167
   CStrings:  185
 
Symbols:
+ __NSConcreteGlobalBlock
+ __os_log_default
+ __os_log_error_impl
+ __os_log_impl
+ _dispatch_once
+ _os_log_create
+ _os_log_type_enabled
- _NSLog
CStrings:
+ " Setting NSFileProtection: %s on the path: %s failed with error: %s"
+ "Move from SRC(%s -> %s) to temp failed with error %s"
+ "Server"
+ "Setting NSFileProtection: %s on the path: %s failed with error: %s"
+ "com.apple.mobile.MobileDataTrasit"
+ "description"
+ "transitd file copy mode started"
+ "transitd file move mode started"
+ "v8@?0"
- " Setting NSFileProtection: %@ on the path: %@ failed with error: %@"
- "Move from SRC(%@ -> %@) to temp failed with error %@"

```
