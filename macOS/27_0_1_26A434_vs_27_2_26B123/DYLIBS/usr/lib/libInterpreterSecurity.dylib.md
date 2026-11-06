## libInterpreterSecurity.dylib

> `/usr/lib/libInterpreterSecurity.dylib`

```diff

-823.1.1.0.0
-  __TEXT.__text: 0x820
+823.40.13.0.0
+  __TEXT.__text: 0x8fc
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x50
+  __TEXT.__const: 0x58
   __TEXT.__cstring: 0x80
-  __TEXT.__oslogstring: 0x1e
+  __TEXT.__oslogstring: 0x48
   __TEXT.__unwind_info: 0x90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x10
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/PrivateFrameworks/XprotectFramework.framework/Versions/A/XprotectFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13
-  Symbols:   81
-  CStrings:  8
+  Functions: 14
+  Symbols:   83
+  CStrings:  9
 
Symbols:
+ _OBJC_CLASS_$_NSFileHandle
+ _objc_msgSend$fileHandleForReadingFromURL:error:
+ _objc_msgSend$getScriptScanEvaluationForFileHandle:scriptData:scanResult:
- _objc_msgSend$getScriptScanEvaluationFor:scriptData:scanResult:
CStrings:
+ "InterpreterSecurity could not open %@: %@"
```
