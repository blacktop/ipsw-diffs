## SpeechProfileDiagnostic

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/PlugIns/SpeechProfileDiagnostic.appex/SpeechProfileDiagnostic`

```diff

-  __TEXT.__text: 0x4a8
+  __TEXT.__text: 0x52c
   __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x140
-  __TEXT.__objc_methlist: 0x38
+  __TEXT.__objc_stubs: 0x1a0
+  __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xe9
-  __TEXT.__oslogstring: 0xcf
+  __TEXT.__oslogstring: 0xc4
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0xee
+  __TEXT.__objc_methname: 0x137
   __TEXT.__objc_methtype: 0x1b
   __TEXT.__unwind_info: 0x70
   __DATA_CONST.__const: 0x40

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__got: 0x28
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x60
+  __DATA.__objc_selrefs: 0x78
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4
-  Symbols:   32
-  CStrings:  28
+  Functions: 5
+  Symbols:   33
+  CStrings:  31
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _OBJC_CLASS_$_CESRUserVocabProfileLogger
Functions:
~ sub_100000c50 : 584 -> 140
+ sub_100000cdc
CStrings:
+ "%s Found %lu loggable profile paths: %@"
+ "_loggableProfilePaths"
+ "addObjectsFromArray:"
+ "loggableUserVocabProfilePaths"
- "%s Found %lu loggable speech profiles at paths: %@"

```
