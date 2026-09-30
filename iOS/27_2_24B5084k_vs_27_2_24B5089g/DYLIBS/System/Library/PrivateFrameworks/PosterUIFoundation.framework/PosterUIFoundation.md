## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-355.2.4.0.0
-  __TEXT.__text: 0x91424
-  __TEXT.__objc_methlist: 0xabdc
-  __TEXT.__const: 0xdc4
-  __TEXT.__oslogstring: 0x3a51
-  __TEXT.__cstring: 0x67d3
-  __TEXT.__gcc_except_tab: 0x17bc
+355.2.6.200.0
+  __TEXT.__text: 0x92c2c
+  __TEXT.__objc_methlist: 0xabfc
+  __TEXT.__const: 0xde4
+  __TEXT.__oslogstring: 0x40c1
+  __TEXT.__cstring: 0x6913
+  __TEXT.__gcc_except_tab: 0x1898
   __TEXT.__dlopen_cstrs: 0x216
   __TEXT.__swift5_typeref: 0x80a
   __TEXT.__constg_swiftt: 0x708

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x33c0
+  __TEXT.__unwind_info: 0x33f0
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2720
+  __DATA_CONST.__const: 0x2778
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5938
+  __DATA_CONST.__objc_selrefs: 0x5978
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x19d0
-  __DATA_CONST.__got: 0xfb8
+  __DATA_CONST.__got: 0xfc8
   __AUTH_CONST.__const: 0x1100
-  __AUTH_CONST.__cfstring: 0x8060
-  __AUTH_CONST.__objc_const: 0x1f038
+  __AUTH_CONST.__cfstring: 0x8180
+  __AUTH_CONST.__objc_const: 0x1f078
   __AUTH_CONST.__objc_dictobj: 0xd70
   __AUTH_CONST.__objc_intobj: 0xe10
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x10c0
+  __AUTH_CONST.__auth_got: 0x1110
   __AUTH.__objc_data: 0x2410
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0xbe4
+  __DATA.__objc_ivar: 0xbec
   __DATA.__data: 0x17a8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4161
-  Symbols:   9688
-  CStrings:  1510
+  Functions: 4171
+  Symbols:   9720
+  CStrings:  1543
 
Symbols:
+ -[PUIPosterSnapshotBundle _cacheImage:forLevelSet:decodedFromIdentifier:]
+ -[PUIPosterSnapshotBundle _pui_afscObserveCompressionIfNeeded]
+ -[PUIPosterSnapshotBundle dealloc]
+ GCC_except_table7
+ _NSURLFileResourceIdentifierKey
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_IVAR_$_PUIPosterSnapshotBundle._afscCompressionObserver
+ _OBJC_IVAR_$_PUIPosterSnapshotBundle._decodedImages
+ _PUIAFSCCompressionBundleURLKey
+ _PUIAFSCCompressionFileNamesKey
+ _PUIAFSCDidCompressBundleNotificationForBundle
+ ___62-[PUIPosterSnapshotBundle _pui_afscObserveCompressionIfNeeded]_block_invoke
+ ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
+ __pui_afscCloneProtectionVerdict
+ __pui_afscPathIsAlreadyCompressed
+ _clonefile
+ _close
+ _fcntl
+ _listxattr
+ _malloc_type_malloc
+ _objc_msgSend$_cacheImage:forLevelSet:decodedFromIdentifier:
+ _objc_msgSend$_pui_afscObserveCompressionIfNeeded
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$bytes
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$setCountLimit:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _open
+ _pread
+ _renamex_np
+ _stat
+ _unlink
- GCC_except_table40
CStrings:
+ "(could not compare)"
+ "AFSC CompressFile refused %{public}@; leaving it uncompressed"
+ "AFSC clone of %{public}@ did not keep the source's protection class; discarding it"
+ "AFSC clone of %{public}@ lost xattr %{public}@; discarding it"
+ "AFSC compressed %lu file(s) under %{public}@ in %.1fms"
+ "AFSC compressed %lu of %lu file(s) under %{public}@ in %.1fms: %{public}@"
+ "AFSC compressed %{public}@ (%lld -> %lld bytes, %.0f%% smaller) in %.1fms (inode %llu -> %llu)"
+ "AFSC compressing %lu file(s) under %{public}@"
+ "AFSC could not clone %{public}@ (%{darwin.errno}d); leaving it uncompressed"
+ "AFSC could not compare the protection class of %{public}@ (%{darwin.errno}d); discarding the compressed copy"
+ "AFSC could not discard the clone of %{public}@ (%{darwin.errno}d); it stays on disk until the next sweep"
+ "AFSC could not identify %{public}@, so no holder will drop its cached decodes: %{public}@"
+ "AFSC could not stat %{public}@ (%{darwin.errno}d); skipping it"
+ "AFSC could not swap in %{public}@ (%{darwin.errno}d); discarding the compressed copy"
+ "AFSC failed on %lu of %lu file(s); see the per-file errors above"
+ "AFSC left %{public}@ (%lld bytes) uncompressed after %.1fms"
+ "AFSC produced no usable compressed copy of %{public}@: %{public}@ (%{darwin.errno}d)"
+ "AFSC skipped %lu already-compressed file(s) under %{public}@; nothing to do"
+ "AFSC skipped %{public}@ (%lld bytes), already compressed"
+ "AFSC source %{public}@ was rewritten during compression (inode %llu -> %llu); discarding the compressed copy"
+ "AFSC source %{public}@ went away during compression (%{darwin.errno}d); discarding the compressed copy"
+ "AFSC swapped in %{public}@ but could not read its new inode"
+ "AFSC swapped in %{public}@ but could not remove the old copy (%{darwin.errno}d)"
+ "AFSC swept a stale clone at %{public}@"
+ "PUIAFSCCompressionBundleURL"
+ "PUIAFSCCompressionFileNames"
+ "PUIAFSCDidCompressBundle-%@"
+ "afsctmp"
+ "already compressed"
+ "compressed %lu, declined %lu, already %lu, failed %lu"
+ "stat failed"
+ "the clone is not the size the source was"
+ "the clone reports the right size but its last byte will not decode"
+ "the clone vanished"
+ "the clone would not open"
+ "v16@?0@\"NSNotification\"8"
- "AFSC CompressFile rejected every path"
- "AFSC compressed %lu of %lu file(s) under %{public}@ (remainder left uncompressed): %{public}@"
- "compressed %lu of %lu"
```
