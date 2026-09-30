## com.apple.AVConference.Diagnostic

> `/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/com.apple.AVConference.Diagnostic`

```diff

-2115.6.1.0.0
-  __TEXT.__text: 0xed4
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0xac
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x26c
-  __TEXT.__oslogstring: 0x332
+2145.45.1.11.2
+  __TEXT.__text: 0x11f4
+  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__objc_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0xb0
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x26e
+  __TEXT.__oslogstring: 0x3cf
   __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methname: 0x3c2
-  __TEXT.__objc_methtype: 0x51
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_methname: 0x408
+  __TEXT.__objc_methtype: 0x55
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x300
+  __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_selrefs: 0x150
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9D0CDD66-245F-3C0C-BD11-1D9F11F66137
-  Functions: 15
-  Symbols:   114
-  CStrings:  110
+  UUID: 132CC452-1616-3191-A946-AB96303B62E6
+  Functions: 19
+  Symbols:   124
+  CStrings:  116
 
Symbols:
+ +[com_apple_AVConference_DiagnosticExtension realHomeDirectory]
+ +[com_apple_AVConference_DiagnosticExtension realHomeDirectory].cold.1
+ -[com_apple_AVConference_DiagnosticExtension attachmentsForParameters:withProgressHandler:]
+ -[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:].cold.1
+ _OBJC_CLASS_$_DECollectionProgress
+ _OUTLINED_FUNCTION_0
+ __89-[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:]_block_invoke.cold.1
+ ___error
+ _getpwuid
+ _getuid
+ _objc_msgSend$initWithPercentComplete:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_retain_x3
- -[com_apple_AVConference_DiagnosticExtension attachmentList]
- -[com_apple_AVConference_DiagnosticExtension attachmentsForParameters:]
- _objc_msgSend$attachmentList
CStrings:
+ "/"
+ "@32@0:8@16@?24"
+ "[AVCDiagnosticExtension] Successfully copied file from %@ to %@"
+ "[AVCDiagnosticExtension] Unable to find user's home folder. errno=%d"
+ "[AVCDiagnosticExtension] error copying file from=%@ to=%@ with error=%@"
+ "attachmentsForParameters:withProgressHandler:"
+ "initWithPercentComplete:"
+ "realHomeDirectory"
+ "stringWithUTF8String:"
- "@24@0:8@16"
- "[AVCDiagnosticExtension] error copying file! %s"
- "attachmentList"
- "attachmentsForParameters:"

```
