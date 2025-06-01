## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2488.4.29.0.0
-  __TEXT.__text: 0x3bccd4
+2488.5.4.0.0
+  __TEXT.__text: 0x3bd0c4
   __TEXT.__auth_stubs: 0x3bc0
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1bd68
-  __TEXT.__const: 0x28978
-  __TEXT.__cstring: 0x6e05e
+  __TEXT.__gcc_except_tab: 0x1bd98
+  __TEXT.__const: 0x28968
+  __TEXT.__cstring: 0x6e0ff
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xcde4
+  __TEXT.__unwind_info: 0xce20
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x3c
   __TEXT.__objc_methname: 0x1270

   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x32e8
-  __DATA.__bss: 0x1040
-  __DATA.__common: 0x1b44
+  __DATA.__data: 0x33f0
+  __DATA.__bss: 0xfb8
+  __DATA.__common: 0x1a3c
   __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__common: 0xa98
-  __DATA_DIRTY.__bss: 0x608
+  __DATA_DIRTY.__common: 0xac8
+  __DATA_DIRTY.__bss: 0x658
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EF5F8DB5-4C61-32B2-A65C-43AC0469DA0C
+  UUID: 5A4A07D6-4599-315B-89CF-681752E53544
   Functions: 12983
-  Symbols:   32571
-  CStrings:  12806
+  Symbols:   32572
+  CStrings:  12810
 
Symbols:
+ __ZN10IIOScanner8getVal24Ev
+ __ZN17LibJPEGReadPlugin12validateJPEGEv
- ___Block_byref_object_copy_.1
- ___Block_byref_object_dispose_.2
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
