## ContinuousRecordingsDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension`

```diff

-8140.4.0.0.0
-  __TEXT.__text: 0x5f0
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x139
-  __TEXT.__oslogstring: 0xc8
+9100.23.0.0.0
+  __TEXT.__text: 0x7c4
+  __TEXT.__auth_stubs: 0x230
+  __TEXT.__objc_stubs: 0x280
+  __TEXT.__objc_methlist: 0x44
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x174
+  __TEXT.__oslogstring: 0xf6
   __TEXT.__objc_classname: 0x28
-  __TEXT.__objc_methname: 0x1d8
+  __TEXT.__objc_methname: 0x250
   __TEXT.__objc_methtype: 0x1b
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xa8
-  __DATA.__objc_selrefs: 0x78
+  __DATA.__objc_selrefs: 0xa8
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1AD5A6AA-A399-3815-8190-392752A61F91
-  Functions: 7
-  Symbols:   91
-  CStrings:  38
+  UUID: AE8B4288-9603-39C1-ADD9-6B5895C74B95
+  Functions: 9
+  Symbols:   96
+  CStrings:  49
 
Symbols:
+ -[ContinuousRecordingsDiagnosticExtension attachmentsForParameters:].cold.1
+ -[ContinuousRecordingsDiagnosticExtension directoryRegexForComponentID:]
+ _NSURLNameKey
+ _OBJC_CLASS_$_NSBundle
+ _objc_msgSend$directoryRegexForComponentID:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$length
+ _objc_msgSend$mainBundle
+ _objc_msgSend$objectForInfoDictionaryKey:
+ _objc_msgSend$stringValue
+ _objc_opt_new
+ _objc_retain_x22
- _NSURLIsRegularFileKey
- _NSURLPathKey
- _objc_alloc_init
- _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
- _objc_release_x25
- _objc_release_x26
- _objc_release_x28
- _objc_retain_x28
Functions:
~ -[ContinuousRecordingsDiagnosticExtension attachmentsForParameters:] : 824 -> 908
+ -[ContinuousRecordingsDiagnosticExtension directoryRegexForComponentID:]
+ -[ContinuousRecordingsDiagnosticExtension attachmentsForParameters:].cold.1
CStrings:
+ "ComponentDirectoryPatterns"
+ "FallbackDirectoryPattern"
+ "No directory pattern found for componentID %@"
+ "componentID"
+ "directoryRegexForComponentID:"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "firstMatchInString:options:range:"
+ "length"
+ "mainBundle"
+ "objectForInfoDictionaryKey:"
+ "stringValue"
- ".lp5"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"

```
