## StreamingZip

> `/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip`

```diff

-216.0.0.0.0
-  __TEXT.__text: 0x217c4
+221.0.0.0.0
+  __TEXT.__text: 0x219b8
   __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_methlist: 0xb04
+  __TEXT.__objc_methlist: 0xb1c
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x160
   __TEXT.__cstring: 0x3a9d
-  __TEXT.__oslogstring: 0x5a93
-  __TEXT.__unwind_info: 0x3ec
+  __TEXT.__oslogstring: 0x5adf
+  __TEXT.__unwind_info: 0x3e4
   __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methname: 0x2f04
-  __TEXT.__objc_methtype: 0xd0e
-  __TEXT.__objc_stubs: 0x2280
+  __TEXT.__objc_methname: 0x2f58
+  __TEXT.__objc_methtype: 0xd25
+  __TEXT.__objc_stubs: 0x22c0
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0xc40
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b88
-  __DATA_CONST.__objc_selrefs: 0x9c8
+  __DATA_CONST.__objc_const: 0x1bb8
+  __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__cfstring: 0x1d60
   __AUTH_CONST.__auth_got: 0x738
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__const: 0x40
-  __DATA_DIRTY.__objc_const: 0x1f0
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__const: 0x80
+  __DATA_DIRTY.__objc_const: 0x3a0
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 04EE4701-A1F3-31AB-A940-5B1C1E9DC87B
-  Functions: 358
-  Symbols:   1617
-  CStrings:  1736
+  UUID: 6A7E6AB0-BF2B-3212-82FC-53324F69249B
+  Functions: 360
+  Symbols:   1624
+  CStrings:  1742
 
Symbols:
+ -[AsyncStreamingFileWriter accessTime]
+ -[AsyncStreamingFileWriter finalizeFileWithAccessTime:modTime:mode:error:]
+ -[AsyncStreamingFileWriter modTime]
+ -[AsyncStreamingFileWriter setAccessTime:]
+ -[AsyncStreamingFileWriter setModTime:]
+ -[StreamingFileWriter finalizeFileWithAccessTime:modTime:mode:error:]
+ GCC_except_table244
+ GCC_except_table325
+ GCC_except_table331
+ GCC_except_table351
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._accessTime
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._modTime
+ _objc_msgSend$accessTime
+ _objc_msgSend$finalizeFileWithAccessTime:modTime:mode:error:
+ _objc_msgSend$modTime
+ _objc_msgSend$setAccessTime:
+ _objc_msgSend$setModTime:
- -[AsyncStreamingFileWriter finalizeFileWithTimestamp:mode:error:]
- -[AsyncStreamingFileWriter setTime:]
- -[AsyncStreamingFileWriter time]
- -[StreamingFileWriter finalizeFileWithTimestamp:mode:error:]
- GCC_except_table242
- GCC_except_table323
- GCC_except_table329
- GCC_except_table349
- _OBJC_IVAR_$_AsyncStreamingFileWriter._time
- _objc_msgSend$finalizeFileWithTimestamp:mode:error:
- _objc_msgSend$setTime:
- _objc_msgSend$time
CStrings:
+ "B60@0:8{timeval=qi}16{timeval=qi}32S48^@52"
+ "Failed to convert path to string: %s"
+ "Found NUL in path %s length %zu at %zu"
+ "T{timeval=qi},N,V_accessTime"
+ "T{timeval=qi},N,V_modTime"
+ "_accessTime"
+ "_modTime"
+ "accessTime"
+ "finalizeFileWithAccessTime:modTime:mode:error:"
+ "modTime"
+ "setAccessTime:"
+ "setModTime:"
+ "v32@0:8{timeval=qi}16"
+ "{timeval=\"tv_sec\"q\"tv_usec\"i}"
+ "{timeval=qi}16@0:8"
- "B36@0:8r^{timeval=qi}16S24^@28"
- "Tr^{timeval=qi},N,V_time"
- "_time"
- "finalizeFileWithTimestamp:mode:error:"
- "r^{timeval=qi}"
- "r^{timeval=qi}16@0:8"
- "setTime:"
- "time"
- "v24@0:8r^{timeval=qi}16"
- "\x81"

```
