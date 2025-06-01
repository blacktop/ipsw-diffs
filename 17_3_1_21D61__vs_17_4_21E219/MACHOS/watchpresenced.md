## watchpresenced

> `/usr/libexec/watchpresenced`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x661c
-  __TEXT.__auth_stubs: 0x430
+27.0.0.0.0
+  __TEXT.__text: 0x66d8
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_stubs: 0x12c0
   __TEXT.__objc_methlist: 0x6fc
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x422
-  __TEXT.__objc_methname: 0x18b2
+  __TEXT.__cstring: 0x401
+  __TEXT.__objc_methname: 0x18bc
   __TEXT.__objc_classname: 0x118
   __TEXT.__objc_methtype: 0x614
   __TEXT.__oslogstring: 0x7ac
-  __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__unwind_info: 0x250
-  __DATA_CONST.__auth_got: 0x230
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__unwind_info: 0x248
+  __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x410
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x2348
+  __DATA.__objc_const: 0x2308
   __DATA.__objc_selrefs: 0x578
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xc0
-  __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0xd8
+  __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x2b8
   __DATA.__bss: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC6A3F2B-30BA-3D0B-9280-3E6582F5E090
-  Functions: 167
-  Symbols:   123
-  CStrings:  529
+  UUID: 5701B6B7-BF6C-3E11-A96F-FF9CDD9746D7
+  Functions: 171
+  Symbols:   122
+  CStrings:  528
 
Symbols:
+ _dispatch_sync
- _objc_release_x27
- _objc_retain_x25
CStrings:
+ "\x06\x12\x17"
+ "T@\"NSString\",?,R,C"
+ "_executionQueue"
+ "com.apple.watchpresenced.executionQueue"
- "\x06\x12\x19"
- "_monitorQueue"
- "_rssiQueue"
- "com.apple.watchpresenced.monitorQueue"
- "com.apple.watchpresenced.rssiQueue"

```
