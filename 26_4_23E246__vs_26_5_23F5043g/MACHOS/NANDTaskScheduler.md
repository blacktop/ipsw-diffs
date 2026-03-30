## NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

-659.100.60.0.0
-  __TEXT.__text: 0x21e04
-  __TEXT.__auth_stubs: 0x520
+659.120.8.0.0
+  __TEXT.__text: 0x21dfc
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_stubs: 0x7e0
   __TEXT.__objc_methlist: 0xc4
-  __TEXT.__cstring: 0x2d786
+  __TEXT.__cstring: 0x2d7af
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__oslogstring: 0x1371
+  __TEXT.__oslogstring: 0x130b
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methname: 0x651
-  __TEXT.__objc_methtype: 0x116
-  __TEXT.__unwind_info: 0x1b0
-  __DATA_CONST.__auth_got: 0x2a0
+  __TEXT.__objc_methtype: 0x117
+  __TEXT.__unwind_info: 0x1c0
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x340
-  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__cfstring: 0x440
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x448
-  __DATA.__common: 0x28
+  __DATA.__common: 0x30
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SidebarFileDispatcher.framework/SidebarFileDispatcher
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9D233221-BD4D-37CE-BFC4-65265254BA68
+  UUID: 22A45B1A-0298-373A-8A9E-DDFEA38C946F
   Functions: 158
-  Symbols:   122
-  CStrings:  3498
+  Symbols:   123
+  CStrings:  3499
 
Symbols:
+ _statfs
CStrings:
+ "/private/var"
+ "Got diskfullness %llu%%"
+ "Successfully processed file at fd: %d, unique %u, overlaps %u, overlap sectors %llu\n"
+ "Total buckets: %d, Overlaps: %u, Overlap Sectors: %llu\n"
+ "numOverlapSectors"
+ "pctDiskfull"
+ "v32@0:8@\"NSFileHandle\"16@?<v@?IQ@\"NSData\"@\"NSError\">24"
+ "v36@?0I8Q12@\"NSData\"20@\"NSError\"28"
- "ERROR: Failed to register idleStack_lowNoDI task (BGST)"
- "Successfully processed file at fd: %d, unique %u, overlaps %u\n"
- "Successfully registered idleStack_lowNoDI task (BGST)"
- "Total buckets: %d, Overlaps: %u\n"
- "com.apple.idleStack_lowNoDI"
- "running idleStack_lowNoDI task (BGST)"
- "v28@?0I8@\"NSData\"12@\"NSError\"20"
- "v32@0:8@\"NSFileHandle\"16@?<v@?I@\"NSData\"@\"NSError\">24"

```
