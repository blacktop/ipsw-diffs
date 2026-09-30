## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-486.0.0.0.0
-  __TEXT.__text: 0x18114
-  __TEXT.__auth_stubs: 0x15e0
-  __TEXT.__objc_stubs: 0x480
+490.60.2.0.0
+  __TEXT.__text: 0x19260
+  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x2ad1
-  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x2bfa
+  __TEXT.__const: 0x78
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__objc_classname: 0x2b
-  __TEXT.__objc_methname: 0x400
+  __TEXT.__objc_methname: 0x475
   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x578
-  __DATA_CONST.__auth_got: 0xb00
+  __TEXT.__unwind_info: 0x5c8
+  __DATA_CONST.__auth_got: 0xb40
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xae8
-  __DATA_CONST.__cfstring: 0x1bc0
+  __DATA_CONST.__const: 0xb10
+  __DATA_CONST.__cfstring: 0x1e60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1d0
-  __DATA.__objc_selrefs: 0x160
+  __DATA.__objc_selrefs: 0x188
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x130

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 475
-  Symbols:   396
-  CStrings:  598
+  Functions: 495
+  Symbols:   404
+  CStrings:  625
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CFStringHasSuffix
+ _clock_gettime_nsec_np
+ _csops
+ _objc_autoreleaseReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _proc_name
CStrings:
+ "  %!@(MISSING) queued solicitation, id = %!l(MISSING)lX:%!l(MISSING)lX, kind = %!s(MISSING), disk = %!@(MISSING), options = 0x%!X(MISSING)."
+ "@\"NSDictionary\"8@?0"
+ "APFS"
+ "EXFAT"
+ "HFS"
+ "MSDOS"
+ "NTFS"
+ "Unable to get signing information for pid %!d(MISSING): %!d(MISSING)"
+ "_fskit"
+ "approval_status"
+ "com.apple.diskarbitrationd.telemetry"
+ "disk_state"
+ "dissenter_name"
+ "duration_ms"
+ "fs_implementation"
+ "fs_type"
+ "n/a"
+ "numberWithInt:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedLongLong:"
+ "operation_type"
+ "other"
+ "setObject:forKeyedSubscript:"
+ "setting uid, id = %!@(MISSING) %!d(MISSING), success."
+ "status_code"
+ "stringWithUTF8String:"
+ "unmount_forced"
+ "volume_clean"
+ "volume_size"
- "  copied disk description, id = %!@(MISSING)."
- "  queued solicitation, id = %!l(MISSING)lX:%!l(MISSING)lX, kind = %!s(MISSING), disk = %!@(MISSING), options = 0x%!X(MISSING)."

```
