## com.apple.AVConference.Diagnostic

> `/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/com.apple.AVConference.Diagnostic`

```diff

-2145.50.1.0.0
-  __TEXT.__text: 0x11f4
+2145.53.2.0.0
+  __TEXT.__text: 0x11c0
   __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x26e
-  __TEXT.__oslogstring: 0x3cf
+  __TEXT.__oslogstring: 0x3c1
   __TEXT.__objc_classname: 0x2d
   __TEXT.__objc_methname: 0x408
   __TEXT.__objc_methtype: 0x55
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 38B11724-643D-3678-842C-21E91A9EF154
+  UUID: 50C098D6-1566-3637-A047-43A3ADB16825
   Functions: 19
   Symbols:   124
   CStrings:  116
Functions:
~ -[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:] : 860 -> 868
~ -[com_apple_AVConference_DiagnosticExtension copyFile:withPredicate:toSaveDirectory:] : 820 -> 816
~ -[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:].cold.1 : 160 -> 124
~ -[com_apple_AVConference_DiagnosticExtension copyFile:withPredicate:toSaveDirectory:].cold.1 : 184 -> 164
CStrings:
+ "[AVCDiagnosticExtension] error copying file from=%@ to=%@"
+ "[AVCDiagnosticExtension] error creating save directory: %@"
- "[AVCDiagnosticExtension] error copying file from=%@ to=%@ with error=%@"
- "[AVCDiagnosticExtension] error creating save directory: %s"

```
