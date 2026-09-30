## symptomsd

> `/usr/libexec/symptomsd`

```diff

-1871.120.6.0.0
+1979.0.0.0.0
   __TEXT.__text: 0x2e0
   __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__const: 0x48
+  __TEXT.__const: 0x40
   __TEXT.__cstring: 0x7e
   __TEXT.__objc_classname: 0x1
-  __TEXT.__info_plist: 0x53d
-  __TEXT.__unwind_info: 0x5c
+  __TEXT.__info_plist: 0x534
+  __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0xd8
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__linkguard: 0x26
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator
+  - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Symbols:   35
+  Symbols:   36
   Functions: 8
 

```
