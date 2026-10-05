## QuickLookThumbnailingDaemon

> `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-218.1.1.0.0
-  __TEXT.__text: 0x52b3c
-  __TEXT.__objc_methlist: 0x3204
-  __TEXT.__const: 0x1004
+218.1.3.200.0
+  __TEXT.__text: 0x53038
+  __TEXT.__objc_methlist: 0x326c
+  __TEXT.__const: 0x1014
   __TEXT.__gcc_except_tab: 0xc80
   __TEXT.__cstring: 0x42e6
-  __TEXT.__oslogstring: 0x5555
+  __TEXT.__oslogstring: 0x5645
   __TEXT.__constg_swiftt: 0x400
   __TEXT.__swift5_typeref: 0xac2
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__dof_QuickLook: 0xb22
-  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__unwind_info: 0x1cb8
   __TEXT.__eh_frame: 0x710
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24d0
+  __DATA_CONST.__objc_selrefs: 0x2518
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x730
   __AUTH_CONST.__const: 0xc70
   __AUTH_CONST.__cfstring: 0x1ba0
-  __AUTH_CONST.__objc_const: 0x5368
+  __AUTH_CONST.__objc_const: 0x5478
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1008
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x1018
   __AUTH.__objc_data: 0x2e0
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x490
+  __DATA.__objc_ivar: 0x4ac
   __DATA.__data: 0x5d8
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0xc88

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2030
-  Symbols:   2722
-  CStrings:  876
+  Functions: 2040
+  Symbols:   2739
+  CStrings:  878
 
Symbols:
+ +[QLDiskCache prepareCacheAtLocation:]
+ -[QLDiskCache lastOpenErrno]
+ -[QLServerThread locationCacheLock]
+ -[QLServerThread locationsToCaches]
+ -[QLServerThread setLocationsToCaches:]
+ -[QLThumbnailAdditionIndex _protectDatabaseFiles]
+ -[_QLCacheThread _allowCacheOpenRetries]
+ -[_QLCacheThread _clearCacheOpenThrottleForTesting]
+ -[_QLCacheThread _reopenCacheIfDue]
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table54
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table84
+ GCC_except_table90
+ GCC_except_table92
+ OBJC_IVAR_$_QLDiskCache._lastOpenErrno
+ OBJC_IVAR_$__QLCacheThread._failedOpenAttempts
+ OBJC_IVAR_$__QLCacheThread._gaveUpOpeningCache
+ OBJC_IVAR_$__QLCacheThread._lastCacheOpenAttempt
+ OBJC_IVAR_$__QLCacheThread._resetDeferred
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_IVAR_$_QLServerThread._locationCacheLock
+ _OBJC_IVAR_$_QLServerThread._locationsToCaches
+ _QLTProtectCacheAtLocation
+ _QLTProtectCacheItemAtPath
+ _QLTThumbnailCacheProtectionAttributes
- GCC_except_table40
- GCC_except_table42
- GCC_except_table44
- GCC_except_table47
- GCC_except_table51
- GCC_except_table53
- GCC_except_table68
- GCC_except_table72
- GCC_except_table77
- GCC_except_table81
- GCC_except_table87
- GCC_except_table89
- _fcntl
CStrings:
+ "Could not fully protect the thumbnail cache at '%@' yet"
+ "Could not open the cache; will retry on a later request"
+ "Giving up on the cache after %lu failed opens (errno %d); -reset will re-enable it"
+ "Not opening the cache at '%@' yet: it is not fully protected, so the device is still locked"
+ "\xf0\xf0\xb1"
- "Problem to open the cache, so we disabled it"
- "\xf0\xf0\x81"
- "\xf1"
```
