## ScreenSharing

> `/System/Library/PrivateFrameworks/ScreenSharing.framework/Versions/A/ScreenSharing`

```diff

-776.27.0.0.0
-  __TEXT.__text: 0x11f0c0
+786.1.0.0.0
+  __TEXT.__text: 0x11ffe8
   __TEXT.__objc_methlist: 0xe9d0
-  __TEXT.__cstring: 0x2d26e
-  __TEXT.__const: 0x3500
-  __TEXT.__oslogstring: 0x1747a
+  __TEXT.__cstring: 0x2d59d
+  __TEXT.__const: 0x3520
+  __TEXT.__oslogstring: 0x178da
   __TEXT.__gcc_except_tab: 0xd38
   __TEXT.__ustring: 0x17c
   __TEXT.__swift5_typeref: 0xca

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x3f78
+  __TEXT.__unwind_info: 0x3fd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x648
+  __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1d8

   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1688
+  __AUTH_CONST.__auth_got: 0x16a0
   __AUTH.__objc_data: 0x20d8
   __AUTH.__data: 0xd8
   __DATA.__objc_ivar: 0x10ac
-  __DATA.__data: 0x18c0
+  __DATA.__data: 0x18d0
   __DATA.__common: 0x19
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5675
-  Symbols:   12199
-  CStrings:  5303
+  Functions: 5698
+  Symbols:   12212
+  CStrings:  5331
 
Symbols:
+ DecodeZRLEPalette
+ DecodeZRLEPaletteRLE
+ DecodeZRLEPlainRLE
+ DecodeZRLEUpdate
+ DecodeZlibUpdate
+ LFOpen
+ _LFOpenLogInit
+ _LFOpenReportRefusal
+ _fstat
+ _gLFOpenLog
+ _gLFOpenLogOnce
+ _os_log_create
+ _pthread_once
+ _readlink
- _fchmod
CStrings:
+ " -> "
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Found a %{public}s there: uid=%u gid=%u mode=%04o nlink=%u dev=%d ino=%llu%{public}s%{public}s. Left in place on purpose."
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Nothing is at that path now."
+ "Not logging to %{public}s: could not clear O_NONBLOCK (errno %d: %{public}s)."
+ "Not logging to %{public}s: fdopen failed (errno %d: %{public}s)."
+ "Not logging to %{public}s: out of memory."
+ "Protocol error - close connection"
+ "Raw rect size %llu invalid for %d x %d at %u bytes/pixel - close connection"
+ "Unable to allocate memory - close connection"
+ "ZRLE inflate produced no data - close connection"
+ "ZRLE rect size %llu invalid for %d x %d at %u bytes/pixel - close connection"
+ "ZRLE tile stream exhausted, %u rows left - close connection"
+ "ZRLE zero-sized rect %d x %d - close connection"
+ "Zlib inflate produced %u of %u expected bytes - close connection"
+ "Zlib rect size %llu invalid for %d x %d codec %u - close connection"
+ "block device"
+ "character device"
+ "could not open the log"
+ "directory"
+ "fifo"
+ "logfile"
+ "not a regular file"
+ "not enough room for  palette RLE update2 %ld"
+ "not enough room for  palette RLE update3 %ld"
+ "not enough room for 2 bit palette update %ld"
+ "not enough room for 4 bit palette update %ld"
+ "not enough room for ZRLE RLE1 %ld"
+ "not enough room for ZRLE RLE2 %ld"
+ "not enough room for one palette update %ld"
+ "path does not name the inode we opened, or that inode has other links"
+ "regular file"
+ "socket"
+ "symlink"
+ "unable to allocate %u bytes for file copy message"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "not enough room for  palette RLE update2 %lu"
- "not enough room for 2 bit palette update %lu"
- "not enough room for 4 bit palette update %lu"
- "not enough room for ZRLE RLE1 %lu"
- "not enough room for ZRLE RLE2 %lu"
```
