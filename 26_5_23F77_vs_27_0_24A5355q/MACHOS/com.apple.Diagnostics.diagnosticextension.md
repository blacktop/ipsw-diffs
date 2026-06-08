## com.apple.Diagnostics.diagnosticextension

> `/Applications/Diagnostics.app/PlugIns/com.apple.Diagnostics.diagnosticextension.appex/com.apple.Diagnostics.diagnosticextension`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x11e4
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x8c
+1351.0.0.0.0
+  __TEXT.__text: 0xd30
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x7c
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x2e6
-  __TEXT.__oslogstring: 0xc8
+  __TEXT.__cstring: 0x2ca
+  __TEXT.__oslogstring: 0x62
   __TEXT.__objc_classname: 0x29
+  __TEXT.__objc_methname: 0x34b
   __TEXT.__objc_methtype: 0x3b
-  __TEXT.__objc_methname: 0x3de
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__cfstring: 0x4c0
+  __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0x120
-  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_selrefs: 0x100
   __DATA.__objc_data: 0xa0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
-  - /System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4FB66C17-58E2-399D-ABBE-97669509FE05
-  Functions: 19
-  Symbols:   57
-  CStrings:  127
+  UUID: 2AC93F52-6BB5-3566-86DD-FEF7C193C883
+  Functions: 11
+  Symbols:   54
+  CStrings:  114
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeStrong
- _NSTemporaryDirectory
- _OBJC_CLASS_$_ELSManager
- _objc_release_x9
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x23
CStrings:
- "Could not get JSON object for ELS."
- "JSONObject"
- "Unable to delete stale ELS file = %@"
- "Unable to write ELS file = %@"
- "_addEnhancedLoggingStateFilesToArchive:"
- "enhanced-logging-state.json"
- "fileExistsAtPath:"
- "path"
- "removeItemAtPath:error:"
- "sharedManager"
- "snapshot"
- "writeToURL:options:error:"

```
