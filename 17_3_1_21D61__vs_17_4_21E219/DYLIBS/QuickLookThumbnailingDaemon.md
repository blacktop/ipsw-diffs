## QuickLookThumbnailingDaemon

> `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon`

```diff

-186.4.1.0.0
-  __TEXT.__text: 0x3f01c
-  __TEXT.__auth_stubs: 0x12a0
-  __TEXT.__objc_methlist: 0x2ccc
+186.5.3.0.0
+  __TEXT.__text: 0x3f130
+  __TEXT.__auth_stubs: 0x12c0
+  __TEXT.__objc_methlist: 0x2cb4
   __TEXT.__const: 0x1c8
-  __TEXT.__gcc_except_tab: 0xa60
+  __TEXT.__gcc_except_tab: 0xa78
   __TEXT.__cstring: 0x3cbc
   __TEXT.__oslogstring: 0x5211
   __TEXT.__dof_QuickLook: 0xb22
-  __TEXT.__unwind_info: 0xf94
+  __TEXT.__unwind_info: 0xf98
   __TEXT.__objc_classname: 0x49d
-  __TEXT.__objc_methname: 0x9448
-  __TEXT.__objc_methtype: 0x1a40
-  __TEXT.__objc_stubs: 0x7220
+  __TEXT.__objc_methname: 0x941c
+  __TEXT.__objc_methtype: 0x1a88
+  __TEXT.__objc_stubs: 0x7240
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x1110
   __DATA_CONST.__objc_classlist: 0x110

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3930
-  __DATA_CONST.__objc_selrefs: 0x2188
+  __DATA_CONST.__objc_selrefs: 0x2180
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x308
+  __DATA_CONST.__objc_superrefs: 0xe0
   __AUTH_CONST.__cfstring: 0x1b00
   __AUTH_CONST.__objc_const: 0xe70
   __AUTH_CONST.__const: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__auth_got: 0x970
   __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x30
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x308
-  __DATA.__objc_superrefs: 0xe0
   __DATA.__objc_ivar: 0x438
   __DATA.__data: 0x248
   __DATA.__bss: 0x41

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2D59955F-671F-373D-9C5B-40E72F4C1A8E
-  Functions: 1641
+  UUID: FFC76471-A5C0-33FD-9BB3-E8CA65614CDA
+  Functions: 1639
   Symbols:   5404
-  CStrings:  2798
+  CStrings:  2799
 
Symbols:
+ -[QLServerThread cacheInitLock]
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table62
+ _OBJC_IVAR_$_QLServerThread._cacheInitLock
+ _objc_msgSend$_QLIsThumbnailable
+ _objc_msgSend$mutableAttributedStringForThumbnailWithURL:documentAttributes:error:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- -[QLServerThread uncachedCacheThreadForItem:]
- -[QLTGeneratorThumbnailRequest clientApprovedForAllFiles]
- -[QLTGeneratorThumbnailRequest setClientApprovedForAllFiles:]
- GCC_except_table24
- GCC_except_table63
- _OBJC_IVAR_$_QLTGeneratorThumbnailRequest._clientApprovedForAllFiles
- _objc_msgSend$mutableAttributedStringForThumbnailWithURL:documentAttributes:
CStrings:
+ "\x02\x1f\x15"
+ "T{os_unfair_lock_s=I},R,N,V_cacheInitLock"
+ "_QLIsThumbnailable"
+ "_cacheInitLock"
+ "cacheInitLock"
+ "mutableAttributedStringForThumbnailWithURL:documentAttributes:error:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "\x02\x1f\x05"
- "TB,V_clientApprovedForAllFiles"
- "_clientApprovedForAllFiles"
- "clientApprovedForAllFiles"
- "mutableAttributedStringForThumbnailWithURL:documentAttributes:"
- "setClientApprovedForAllFiles:"
- "uncachedCacheThreadForItem:"

```
