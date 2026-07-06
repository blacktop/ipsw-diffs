## spindump

> `/usr/sbin/spindump`

```diff

-  __TEXT.__text: 0x10c27c
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_stubs: 0x4b60
+  __TEXT.__text: 0x10dbbc
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__objc_stubs: 0x4b80
   __TEXT.__objc_methlist: 0xcd0
-  __TEXT.__const: 0x2a8
-  __TEXT.__oslogstring: 0x35152
-  __TEXT.__cstring: 0x1b8c6
+  __TEXT.__const: 0x2d8
+  __TEXT.__oslogstring: 0x355c0
+  __TEXT.__cstring: 0x1bace
   __TEXT.__objc_classname: 0x143
   __TEXT.__objc_methtype: 0x596
-  __TEXT.__gcc_except_tab: 0x44b8
-  __TEXT.__objc_methname: 0x49b7
-  __TEXT.__unwind_info: 0x1400
-  __DATA_CONST.__const: 0x2110
-  __DATA_CONST.__cfstring: 0xd960
+  __TEXT.__gcc_except_tab: 0x461c
+  __TEXT.__objc_methname: 0x49c5
+  __TEXT.__unwind_info: 0x1410
+  __DATA_CONST.__const: 0x2130
+  __DATA_CONST.__cfstring: 0xdac0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0xaa8
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__auth_ptr: 0x48
+  __DATA_CONST.__auth_got: 0xab0
+  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x2560
-  __DATA.__objc_selrefs: 0x13a0
+  __DATA.__objc_selrefs: 0x13a8
   __DATA.__objc_ivar: 0x284
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x1c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x918
+  __DATA.__bss: 0x928
   __DATA.__common: 0x70
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2744
-  Symbols:   453
-  CStrings:  8003
+  Functions: 2758
+  Symbols:   454
+  CStrings:  8044
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _SANanosecondsFromMachTimeUsingTimebase
CStrings:
+ "No mach continuous time in WR tailspin %s"
+ "No overlap in WR tailspin %s"
+ "PowerExceptions"
+ "Unable to format: No mach continuous time in WR tailspin %s"
+ "Unable to format: No overlap in WR tailspin %s"
+ "Unable to format: Unable to get earliest ktrace machcont timestamp in WR tailspin %s: %d (%s)"
+ "Unable to format: Unable to get ktrace mach timebase, assuming native timebase in WR tailspin %s: %d (%s)"
+ "Unable to format: Unable to get latest ktrace machcont timestamp in WR tailspin %s: %d (%s)"
+ "Unable to format: Unable to open WR tailspin %s: %d (%s)"
+ "Unable to format: Unable to statfs %s: %d (%s)"
+ "Unable to format: ktrace mach timebase %d/%d, assuming native timebase in WR tailspin %s"
+ "Unable to format: ktrace unavailable for WR tailspin %s"
+ "Unable to get earliest ktrace machcont timestamp in WR tailspin %s: %d (%s)"
+ "Unable to get ktrace mach timebase, assuming native timebase in WR tailspin %s: %d (%s)"
+ "Unable to get latest ktrace machcont timestamp in WR tailspin %s: %d (%s)"
+ "Unable to open WR tailspin %s: %d (%s)"
+ "Unable to statfs %s: %d (%s)"
+ "codesigningID"
+ "ktrace mach timebase %d/%d, assuming native timebase in WR tailspin %s"
+ "ktrace unavailable for WR tailspin %s"
+ "overlapdurationms"

```
