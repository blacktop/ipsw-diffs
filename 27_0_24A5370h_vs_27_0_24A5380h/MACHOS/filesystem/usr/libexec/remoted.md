## remoted

> `/usr/libexec/remoted`

```diff

-  __TEXT.__text: 0x3d274
-  __TEXT.__auth_stubs: 0x1810
+  __TEXT.__text: 0x3d534
+  __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_stubs: 0x24a0
   __TEXT.__objc_methlist: 0x1560
-  __TEXT.__const: 0x1fa
+  __TEXT.__const: 0x22a
   __TEXT.__oslogstring: 0x84b3
-  __TEXT.__cstring: 0x21a4
+  __TEXT.__cstring: 0x21d9
   __TEXT.__objc_methname: 0x254c
   __TEXT.__objc_classname: 0x2c9
   __TEXT.__objc_methtype: 0x79b
   __TEXT.__gcc_except_tab: 0x1120
-  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__unwind_info: 0xdc8
   __DATA_CONST.__const: 0x12c8
   __DATA_CONST.__cfstring: 0xea0
   __DATA_CONST.__objc_classlist: 0xd8

   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xc18
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__auth_got: 0xc40
+  __DATA_CONST.__got: 0x250
   __DATA.__objc_const: 0x2810
   __DATA.__objc_selrefs: 0x980
   __DATA.__objc_ivar: 0x21c
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x6d4
-  __DATA.__bss: 0x3b0
+  __DATA.__bss: 0x3b8
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1370
-  Symbols:   482
-  CStrings:  1907
+  Functions: 1375
+  Symbols:   492
+  CStrings:  1913
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _ftruncate
+ _kCFAbsoluteTimeIntervalSince1970
+ _mmap
+ _sntp_datestamp_from_double
+ _sntp_header_mmap
+ _sntp_shortstamp_hton
+ _sntp_timestamp_to_shortstamp
+ _umask
+ _warn
+ _write
CStrings:
+ "/var/sntpd/state.bin"
+ "close"
+ "ftruncate"
+ "mmap"
+ "open"
+ "write"

```
