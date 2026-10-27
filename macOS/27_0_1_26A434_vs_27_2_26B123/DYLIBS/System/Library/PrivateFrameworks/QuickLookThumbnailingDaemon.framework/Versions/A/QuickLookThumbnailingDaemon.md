## QuickLookThumbnailingDaemon

> `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/Versions/A/QuickLookThumbnailingDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-218.0.0.0.0
-  __TEXT.__text: 0x57fe4
-  __TEXT.__objc_methlist: 0x315c
+218.1.2.0.0
+  __TEXT.__text: 0x583c8
+  __TEXT.__objc_methlist: 0x319c
   __TEXT.__const: 0xfd4
   __TEXT.__gcc_except_tab: 0xb94
   __TEXT.__cstring: 0x4141
-  __TEXT.__oslogstring: 0x5455
+  __TEXT.__oslogstring: 0x5505
   __TEXT.__constg_swiftt: 0x400
   __TEXT.__swift5_typeref: 0xe48
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__dof_QuickLook: 0xb22
-  __TEXT.__unwind_info: 0x1438
+  __TEXT.__unwind_info: 0x1448
   __TEXT.__eh_frame: 0x710
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24c0
+  __DATA_CONST.__objc_selrefs: 0x24f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x790
   __AUTH_CONST.__const: 0x1f40
   __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x5350
+  __AUTH_CONST.__objc_const: 0x53e0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xf30
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0xf38
   __AUTH_CONST.__auth_ptr: 0x3e8
   __AUTH.__objc_data: 0x268
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x498
+  __DATA.__objc_ivar: 0x4a8
   __DATA.__data: 0x490
   __DATA.__bss: 0xba0
   __DATA.__common: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2027
-  Symbols:   3728
-  CStrings:  855
+  Functions: 2034
+  Symbols:   3745
+  CStrings:  856
 
Symbols:
+ +[QLDiskCache prepareCacheAtLocation:]
+ -[QLDiskCache lastOpenErrno]
+ -[QLThumbnailAdditionIndex _protectDatabaseFiles]
+ -[_QLCacheThread _allowCacheOpenRetries]
+ -[_QLCacheThread _clearCacheOpenThrottleForTesting]
+ -[_QLCacheThread _reopenCacheIfDue]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table18
+ GCC_except_table55
+ GCC_except_table59
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table83
+ GCC_except_table88
+ GCC_except_table94
+ OBJC_IVAR_$_QLDiskCache._lastOpenErrno
+ OBJC_IVAR_$__QLCacheThread._failedOpenAttempts
+ OBJC_IVAR_$__QLCacheThread._gaveUpOpeningCache
+ OBJC_IVAR_$__QLCacheThread._lastCacheOpenAttempt
+ _OBJC_CLASS_$_NSConstantArray
+ _QLTProtectCacheItemAtPath
+ _objc_msgSend$_allowCacheOpenRetries
+ _objc_msgSend$_reopenCacheIfDue
+ _objc_msgSend$lastOpenErrno
+ _objc_msgSend$prepareCacheAtLocation:
- GCC_except_table100
- GCC_except_table17
- GCC_except_table21
- GCC_except_table44
- GCC_except_table58
- GCC_except_table64
- GCC_except_table70
- GCC_except_table74
- GCC_except_table80
- GCC_except_table85
- GCC_except_table91
- GCC_except_table98
CStrings:
+ "Could not open the cache; will retry on a later request"
+ "Giving up on the cache after %lu failed opens (errno %d); -reset will re-enable it"
+ "Not opening the cache at '%@' yet: it is not fully protected, so the device is still locked"
+ "\xf0\xf0\xb1"
- "Problem to open the cache, so we disabled it"
- "\xf0\xf0\x81"
- "\xf1"
```
