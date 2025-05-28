## ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

-2488.4.29.0.0
-  __TEXT.__text: 0x41c8c0
+2488.5.4.0.0
+  __TEXT.__text: 0x41cc6c
   __TEXT.__auth_stubs: 0x4250
   __TEXT.__objc_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1f6d0
-  __TEXT.__const: 0x2a770
-  __TEXT.__cstring: 0x78c01
+  __TEXT.__gcc_except_tab: 0x1f700
+  __TEXT.__const: 0x2a760
+  __TEXT.__cstring: 0x78ca2
   __TEXT.__objc_methname: 0x1282
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methtype: 0x5f1
   __TEXT.__oslogstring: 0x1ee
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xebbc
+  __TEXT.__unwind_info: 0xebc8
   __TEXT.__eh_frame: 0x1018
   __DATA_CONST.__auth_got: 0x2140
   __DATA_CONST.__got: 0x630

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 16122
-  Symbols:   10801
-  CStrings:  12677
+  Symbols:   10803
+  CStrings:  12681
 
Symbols:
+ __ZN10IIOScanner8getVal24Ev
+ __ZN17LibJPEGReadPlugin12validateJPEGEv
CStrings:
+ "*** ERROR: bad 'COD CodeBlockWidth' (%d)\n"
+ "*** ERROR: cannot allocate srcBuffer [%ld bytes]\n"
+ "*** ERROR: libJPEGBufferSize > imageDataBufferSize   (%lld > %lld)\n"
+ "*** ERROR: skipping layer#%d {%d, %d, %d, %d}\n"
+ "*** IIOScanner::getVal24 reached EOF\n"
+ "getVal24"
- "*** ERROR: cannot allocate srcBuffer [%ld bytes]"
- "*** ERROR: skipping layer {%d, %d, %d, %d}\n"

```
