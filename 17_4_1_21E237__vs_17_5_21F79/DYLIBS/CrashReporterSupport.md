## CrashReporterSupport

> `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport`

```diff

-14271.0.0.0.0
-  __TEXT.__text: 0x58b0
-  __TEXT.__auth_stubs: 0x7a0
+14271.1.0.0.0
+  __TEXT.__text: 0x5f68
+  __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_methlist: 0xec
-  __TEXT.__const: 0xa0
+  __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0xd34
-  __TEXT.__oslogstring: 0x75d
-  __TEXT.__unwind_info: 0x21c
+  __TEXT.__cstring: 0xe4d
+  __TEXT.__oslogstring: 0x8d3
+  __TEXT.__unwind_info: 0x228
   __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0xbb4
+  __TEXT.__objc_methname: 0xc84
   __TEXT.__objc_methtype: 0x1fe
-  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_stubs: 0xd80
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x3e8
+  __DATA_CONST.__const: 0x410
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x450
-  __DATA_CONST.__objc_selrefs: 0x388
+  __DATA_CONST.__objc_selrefs: 0x3d0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0xa8
+  __DATA_CONST.__objc_classrefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x1260
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__cfstring: 0x1480
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x410
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x119
   __DATA.__bss: 0x70

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/Symbolication.framework/Symbolication
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 119
-  Symbols:   615
-  CStrings:  404
+  Functions: 123
+  Symbols:   641
+  CStrings:  433
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSNumberFormatter
+ ___block_descriptor_89_e8_32o40o_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_literal_global.225
+ ___send_analytics_block_invoke
+ _bzero
+ _create_dir_with_owners_and_perms_with_analytics
+ _ensure_dir_perms_analytics
+ _getcwd
+ _getpid
+ _getprogname
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$setMaximumSignificantDigits:
+ _objc_msgSend$setUsesSignificantDigits:
+ _objc_msgSend$stringForObjectValue:
+ _objc_msgSend$timeIntervalSinceDate:
+ _send_analytics
+ _sysctl
- ___block_literal_global.167
CStrings:
+ "-1"
+ "<unknown>"
+ "=== CC create dir %{public}s with owners and permissions {startPath: %{public}s, statSuccess: %d, successModifyGID: %d, origninalGID: %d, modifyGID: %d, successModifyPerms: %d, origninalMode: 0x%X, modifyMode: 0x%X}"
+ "=== CC ensured dir %{public}s had correct permissions {startPath: %{public}s, statSuccess: %d, successModifyPerms: %d, origninalMode: 0x%X, modifyMode: 0x%X}"
+ "@\"NSDictionary\"8@?0"
+ "CrashCatcher"
+ "boot_time_appx"
+ "com.apple.osanalytics.directory_modification"
+ "date"
+ "dateWithTimeIntervalSince1970:"
+ "framework"
+ "modify_gid"
+ "modify_gid_success"
+ "modify_gid_value"
+ "modify_perms"
+ "modify_perms_success"
+ "modify_perms_value"
+ "numberWithDouble:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedShort:"
+ "original_gid"
+ "original_perms"
+ "proc_uptime_appx"
+ "progname"
+ "setMaximumSignificantDigits:"
+ "setUsesSignificantDigits:"
+ "start_path"
+ "stringForObjectValue:"
+ "timeIntervalSinceDate:"

```
