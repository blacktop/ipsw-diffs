## com.apple.DiagnosticExtensions.WiFi

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.WiFi.appex/com.apple.DiagnosticExtensions.WiFi`

```diff

-503.0.0.0.0
-  __TEXT.__text: 0x1f20
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0x540
-  __TEXT.__objc_methlist: 0x8c
+509.4.1.0.0
+  __TEXT.__text: 0x22a4
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_methlist: 0x98
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0x370
-  __TEXT.__oslogstring: 0xba
+  __TEXT.__cstring: 0x3eb
+  __TEXT.__oslogstring: 0x142
   __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x3f6
+  __TEXT.__objc_methname: 0x4ae
   __TEXT.__objc_methtype: 0x34
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0x3c0
+  __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x160
+  __DATA.__objc_selrefs: 0x1a0
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/Centauri.framework/Centauri
+  - /System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12D52850-8039-3C37-958F-09525257EC36
-  Functions: 19
-  Symbols:   65
-  CStrings:  130
+  UUID: 4A90C591-E4A8-32F6-AC9F-D7FCE3C7BE30
+  Functions: 20
+  Symbols:   72
+  CStrings:  148
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSFileManager
+ _collectSubsystemLogsForClient
+ _isCentauriPlatform
+ _objc_alloc_init
+ _objc_retain_x23
CStrings:
+ "%{public}s::%d: failed to create directory %@"
+ "%{public}s::%d: failed to create output path"
+ "%{public}s::%d: failed to get attachments %@"
+ "-[WiFiDiagnosticsExtension __collectCentauriLogs]"
+ "/private/var/tmp/ConnectivityDE/"
+ "ConnectivityLogs_%@"
+ "__collectCentauriLogs"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "defaultManager"
+ "now"
+ "setDateFormat:"
+ "setDeleteOnAttach:"
+ "stringByAppendingFormat:"
+ "stringFromDate:"
+ "yyyy-MM-dd_HH.mm.ss"

```
