## ScreenSharing

> `/System/Library/PrivateFrameworks/ScreenSharing.framework/Versions/A/ScreenSharing`

```diff

-776.27.0.0.0
-  __TEXT.__text: 0x1227d8
-  __TEXT.__objc_methlist: 0xe9d0
-  __TEXT.__cstring: 0x2d26e
-  __TEXT.__const: 0x3500
-  __TEXT.__oslogstring: 0x1747a
+786.5.0.0.0
+  __TEXT.__text: 0x123e94
+  __TEXT.__objc_methlist: 0xe9e0
+  __TEXT.__cstring: 0x2d801
+  __TEXT.__const: 0x3520
+  __TEXT.__oslogstring: 0x17b3e
   __TEXT.__gcc_except_tab: 0xd38
   __TEXT.__ustring: 0x17c
   __TEXT.__swift5_typeref: 0xca

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x2a88
+  __TEXT.__unwind_info: 0x2aa8
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
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8bd0
+  __DATA_CONST.__objc_selrefs: 0x8be0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x3b8
   __DATA_CONST.__got: 0xc78
   __AUTH_CONST.__const: 0x1638
   __AUTH_CONST.__cfstring: 0x7c20
-  __AUTH_CONST.__objc_const: 0x12d38
+  __AUTH_CONST.__objc_const: 0x12d40
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1688
+  __AUTH_CONST.__auth_got: 0x16a0
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x20d8
   __AUTH.__data: 0xd8
   __DATA.__objc_ivar: 0x10ac
-  __DATA.__data: 0x18c0
-  __DATA.__bss: 0x904
+  __DATA.__data: 0x18d0
+  __DATA.__bss: 0x90c
   __DATA.__common: 0x19
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5676
-  Symbols:   12199
-  CStrings:  5303
+  Functions: 5705
+  Symbols:   12216
+  CStrings:  5341
 
Symbols:
+ -[SSFrameBufferView appliedViewerScaleAdjustment]
+ DecodeZRLEPalette
+ DecodeZRLEPaletteRLE
+ DecodeZRLEPlainRLE
+ DecodeZRLEUpdate
+ DecodeZlibUpdate
+ GCC_except_table101
+ GCC_except_table109
+ LFOpen
+ _LFOpenLogInit
+ _LFOpenReportRefusal
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _fstat
+ _gLFOpenLog
+ _gLFOpenLogOnce
+ _objc_msgSend$appliedViewerScaleAdjustment
+ _os_log_create
+ _pthread_once
+ _readlink
- GCC_except_table100
- GCC_except_table108
- _fchmod
CStrings:
+ " -> "
+ "Clipboard: %u unconsumed bytes after a complete inflate stream (trailing data in compressed payload)"
+ "Clipboard: declared uncompressed size %u but inflated %ld"
+ "Clipboard: declared uncompressed size %u exceeds maximum %u"
+ "Clipboard: declared uncompressed size %u too small, %u input bytes unconsumed"
+ "Clipboard: inflate error %d"
+ "Clipboard: inflate init error %d"
+ "ExpandUserInfo: expected %u bytes, inflated %u"
+ "InflateCursorImage: expected %u bytes, inflated %u"
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
+ "declared uncompressed size %u but inflated %u"
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
+ "truncated scrap: %ld byte(s) remain, need %lu for flavorDataLength"
+ "unable to allocate %u bytes for file copy message"
+ "uncompressed size = %ld (declared %u)"
+ "user image data size out of range - %u"
+ "user image did not decompress - skipping the picture"
- "Clipboard: inflate error %d\n"
- "Clipboard: inflate init error %d\n"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "not enough room for  palette RLE update2 %lu"
- "not enough room for 2 bit palette update %lu"
- "not enough room for 4 bit palette update %lu"
- "not enough room for ZRLE RLE1 %lu"
- "not enough room for ZRLE RLE2 %lu"
- "uncompressed size = %ld"
```
