## logd

> `/usr/libexec/logd`

```diff

-1815.0.0.0.0
-  __TEXT.__text: 0x27450
-  __TEXT.__auth_stubs: 0x1b00
+1815.0.6.0.0
+  __TEXT.__text: 0x27730
+  __TEXT.__auth_stubs: 0x1b10
   __TEXT.__delay_helper: 0x110
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x4d56
+  __TEXT.__cstring: 0x4d1b
   __TEXT.__objc_methname: 0x4ee
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x6c0
+  __TEXT.__unwind_info: 0x6c8
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0xd88
+  __DATA_CONST.__auth_got: 0xd90
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2160
+  __DATA_CONST.__const: 0x2138
   __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x10

   __DATA.__data: 0x1d24
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xdf18
+  __DATA.__bss: 0xef18
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EC487E7E-3EFB-3BDC-9928-513EF97FA899
-  Functions: 512
-  Symbols:   490
-  CStrings:  676
+  UUID: 1B888476-CE17-3D73-B932-E54F5785293A
+  Functions: 514
+  Symbols:   491
+  CStrings:  669
 
Symbols:
+ _mach_continuous_time
CStrings:
+ "%.02fs elapsed, cancelling firehose server.\n"
+ "Failed to create sql table with %d: %s. Closing database..."
+ "w+"
- "%s[%d] dropped %u %s events"
- "BUG IN LIBTRACE: Failed to create sql table"
- "Failed to create sql table with %d: %s"
- "a+"
- "debug"
- "default"
- "error and fault"
- "info"
- "metadata"
- "signpost"

```
