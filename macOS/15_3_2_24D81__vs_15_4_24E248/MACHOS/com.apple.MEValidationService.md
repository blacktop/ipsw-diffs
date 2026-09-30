## com.apple.MEValidationService

> `/System/Library/Frameworks/MediaExtension.framework/Versions/A/XPCServices/com.apple.MEValidationService.xpc/Contents/MacOS/com.apple.MEValidationService`

```diff

-3200.5.1.0.0
-  __TEXT.__text: 0xc4c
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x4b6
-  __TEXT.__oslogstring: 0xab
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x58
+3210.19.1.5.2
+  __TEXT.__text: 0x1010
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_stubs: 0xe0
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x54e
+  __TEXT.__oslogstring: 0x15b
+  __TEXT.__objc_methname: 0x82
+  __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x30
-  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__objc_selrefs: 0x38
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8765ABCD-65D4-38CA-9422-AD67E871878C
-  Functions: 9
-  Symbols:   83
-  CStrings:  19
+  UUID: 6F3F9963-B00B-3242-8829-87EA9A03C079
+  Functions: 10
+  Symbols:   100
+  CStrings:  38
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _CFSetRemoveAllValues
+ _CFStringCompare
+ _CFStringFind
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_RBSProcessHandle
+ __NSConcreteGlobalBlock
+ __os_feature_enabled_impl
+ _dispatch_once
+ _objc_msgSend
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleasedReturnValue
+ _os_transaction_create
+ _sandbox_check_by_audit_token
+ _xpc_connection_get_pid
- __xpc_error_connection_invalid
CStrings:
+ "/"
+ "CoreMedia"
+ "MEValidationService: Identified %ld compatible file extensions from format reader bundle Info.plist which exceeded the max limit of %d. All file extensions will be disallowed."
+ "MediaExtensions"
+ "auditToken"
+ "bundleRecordForAuditToken:error:"
+ "com.apple.MEValidationService.Request"
+ "com.apple.mediaextension.formatreader"
+ "com.apple.security.app-sandbox"
+ "extensionPointRecord"
+ "file-read*"
+ "handleForIdentifier:error:"
+ "hostProcess"
+ "identifier"
+ "numberWithInt:"
+ "v8@?0"

```
