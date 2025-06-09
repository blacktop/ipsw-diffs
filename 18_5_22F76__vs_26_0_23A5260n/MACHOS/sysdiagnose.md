## sysdiagnose

> `/usr/bin/sysdiagnose`

```diff

-1438.120.9.0.0
-  __TEXT.__text: 0x44b4
-  __TEXT.__auth_stubs: 0x630
+1512.0.0.0.0
+  __TEXT.__text: 0x46fc
+  __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0xac
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__cstring: 0x237b
-  __TEXT.__oslogstring: 0x6ea
+  __TEXT.__cstring: 0x2384
+  __TEXT.__oslogstring: 0x722
   __TEXT.__objc_methname: 0x5d9
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x5b
-  __TEXT.__unwind_info: 0x168
-  __DATA_CONST.__auth_got: 0x328
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__const: 0x328
   __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x238
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x30
-  __DATA.__bss: 0xa0
+  __DATA.__data: 0x38
+  __DATA.__bss: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 9205F521-B6DB-3815-ADA7-A1D0ACB67251
-  Functions: 83
-  Symbols:   151
-  CStrings:  291
+  UUID: 1EDAD9A4-2177-36EC-9684-183EE93551FD
+  Functions: 87
+  Symbols:   154
+  CStrings:  295
 
Symbols:
+ _getppid
+ _objc_retain_x21
+ _objc_retain_x26
+ _proc_name
- _objc_retain_x22
CStrings:
+ "Invoked by parent (%d): '%{public}s'"
+ "Invoked by terminal"
+ "Output available at '%s'."
+ "cli"
+ "error"
- "\nOutput available at '%s'."

```
