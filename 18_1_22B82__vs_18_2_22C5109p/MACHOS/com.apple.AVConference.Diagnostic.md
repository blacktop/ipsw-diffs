## com.apple.AVConference.Diagnostic

> `/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/com.apple.AVConference.Diagnostic`

```diff

-2085.8.1.2.0
-  __TEXT.__text: 0xdcc
+2090.12.1.1.0
+  __TEXT.__text: 0xedc
   __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_stubs: 0x480
-  __TEXT.__objc_methlist: 0x98
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x232
-  __TEXT.__oslogstring: 0x2ea
+  __TEXT.__objc_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0xac
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x26c
+  __TEXT.__oslogstring: 0x332
   __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methname: 0x3c0
+  __TEXT.__objc_methname: 0x3c2
   __TEXT.__objc_methtype: 0x51
   __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x138
+  __DATA.__objc_selrefs: 0x140
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13
-  Symbols:   106
-  CStrings:  84
+  Functions: 15
+  Symbols:   114
+  CStrings:  87
 
Symbols:
+ +[com_apple_AVConference_DiagnosticExtension defaultAVConferenceCachePath]
+ +[com_apple_AVConference_DiagnosticExtension defaultCrashReportPath]
+ +[com_apple_AVConference_DiagnosticExtension defaultRTCReportingPath]
+ +[com_apple_AVConference_DiagnosticExtension defaultSpindumpPath]
+ -[com_apple_AVConference_DiagnosticExtension copySpindumps]
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_com_apple_AVConference_DiagnosticExtension
+ ___89-[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:]_block_invoke
+ ___block_descriptor_32_e27_B24?0"NSURL"8"NSError"16l
+ ___block_literal_global
+ _objc_msgSend$copySpindumps
+ _objc_msgSend$defaultSpindumpPath
- -[com_apple_AVConference_DiagnosticExtension copyVCTerminateProcessSpindumps]
- -[com_apple_AVConference_DiagnosticExtension defaultAVConferenceCachePath]
- -[com_apple_AVConference_DiagnosticExtension defaultCrashReportPath]
- -[com_apple_AVConference_DiagnosticExtension defaultRTCReportingPath]
CStrings:
+ "/var/mobile/Library/Caches/com.apple.VideoConference/logs"
+ "/var/mobile/Library/Logs/CrashReporter/"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "[AVCDiagnosticExtension] Beginning Spindump and Tailspin file copy process"
+ "[AVCDiagnosticExtension] error enumerating directory url=%!@(MISSING): %!s(MISSING)"
+ "copySpindumps"
+ "defaultSpindumpPath"
+ "spins=%!d(MISSING) "
- "/private/var/tmp/"
- "/var/mobile/Library/Caches/com.apple.VideoConference/"
- "[AVCDiagnosticExtension] Beginning Mac stackshot file copy process"
- "copyVCTerminateProcessSpindumps"
- "logs/"

```
