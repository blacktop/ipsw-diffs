## NewsDiagnosticExtension

> `/private/var/staged_system_apps/News.app/PlugIns/NewsDiagnosticExtension.appex/NewsDiagnosticExtension`

```diff

-5593.0.0.0.0
-  __TEXT.__text: 0x594
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x80
+5604.1.0.0.0
+  __TEXT.__text: 0x5c0
+  __TEXT.__auth_stubs: 0x160
+  __TEXT.__objc_stubs: 0x240
+  __TEXT.__objc_methlist: 0x50
+  __TEXT.__cstring: 0xab
   __TEXT.__const: 0x8
-  __TEXT.__objc_methname: 0x2dc
+  __TEXT.__objc_methname: 0x287
   __TEXT.__oslogstring: 0x86
   __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methtype: 0x75
+  __TEXT.__objc_methtype: 0x5a
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xb0
+  __DATA_CONST.__auth_got: 0xb8
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__cfstring: 0x60
+  __DATA_CONST.__const: 0x10
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x130
+  __DATA.__objc_const: 0x100
   __DATA.__objc_selrefs: 0xa8
-  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 8
-  Symbols:   39
-  CStrings:  43
+  Symbols:   43
+  CStrings:  42
 
Symbols:
+ _FRDiagnosticDumpNotificationName
+ _FRDiagnosticFileListURL
+ _FRDiagnosticFileNotificationName
+ _FRDiagnosticFileTempDirURL
+ _OBJC_CLASS_$_TFInterprocessDiagnosticFileReceiver
+ _objc_release_x23
+ _objc_release_x24
+ _objc_retain_x23
- _FRDiagnosticFileManagerCreate
- _OBJC_CLASS_$_TFDiagnosticFileManager
- _objc_retain
- _objc_retain_x22
CStrings:
+ "\x02"
+ "FRDiagnosticDumpNotificationName"
+ "FRDiagnosticFileNotificationName"
+ "URLByAppendingPathComponent:"
+ "attachmentWithPathURL:"
+ "diagnosticFileURLs"
+ "initWithNotificationName:diagnosticFileListURL:log:"
+ "initWithNotificationName:diagnosticTempDir:log:"
+ "news-diagnostic-file-list.txt"
- "\x03"
- "@\"TFDiagnosticFileManager\""
- "NewsDiagnosticExtensionAttachmentRequestNotification"
- "T@\"TFDiagnosticFileManager\",R,N,V_diagnosticFileManager"
- "_diagnosticFileManager"
- "attachmentWithPath:"
- "availableDiagnosticFiles"
- "diagnosticFileManager"
- "initWithDiagnosticDumpDir:diagnosticDumpNotificationName:log:"
- "initWithNotificationName:diagnosticFileManager:"

```
