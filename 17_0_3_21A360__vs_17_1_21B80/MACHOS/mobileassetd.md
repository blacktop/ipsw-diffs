## mobileassetd

> `/usr/libexec/mobileassetd`

```diff

-936.2.1.0.0
-  __TEXT.__text: 0x3eec
-  __TEXT.__stubs: 0x33c
+936.42.1.0.0
+  __TEXT.__text: 0x4064
+  __TEXT.__stubs: 0x354
   __TEXT.__objc_stubs: 0xa60
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1456
+  __TEXT.__cstring: 0x1489
+  __TEXT.__gcc_except_tab: 0x140
   __TEXT.__objc_methname: 0x6ef
   __TEXT.__objc_classname: 0x29
   __TEXT.__objc_methtype: 0xca
-  __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x124
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0xe0
+  __TEXT.__unwind_info: 0x134
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__cfstring: 0x10e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 58
-  Symbols:   106
-  CStrings:  254
+  Functions: 63
+  Symbols:   108
+  CStrings:  255
 
Symbols:
+ _dispatch_queue_create
+ _dispatch_sync
CStrings:
+ "Starting mobileassetd built Oct  4 2023 22:11:13"
+ "[MA_PREFS] Read preference from: %@ for: %@ value: `%@` (%@)"
+ "com.apple.MobileAsset.preferencesDomain"
- "Read preference from: %@ for: %@ value: `%@` (%@)"
- "Starting mobileassetd built Aug  6 2023 02:53:22"

```
