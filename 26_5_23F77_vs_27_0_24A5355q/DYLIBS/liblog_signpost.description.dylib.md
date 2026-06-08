## liblog_signpost.description.dylib

> `/usr/lib/log/liblog_signpost.description.dylib`

```diff

-174.8.0.0.0
-  __TEXT.__text: 0x188
-  __TEXT.__auth_stubs: 0xb0
+197.0.0.0.0
+  __TEXT.__text: 0x17c
   __TEXT.__cstring: 0x41
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x60
-  __TEXT.__objc_methname: 0x5f
-  __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x18
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x60
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5A28560-3ECA-349C-A078-C0BBB9DDF9C0
+  UUID: 51A85ACA-AADA-317F-A342-46DD74550A29
   Functions: 2
   Symbols:   22
-  CStrings:  18
+  CStrings:  14
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ _OSLogCopyFormattedString : 40 -> 36
~ _SignpostFormattedString : 352 -> 344
CStrings:
- "initWithString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringValue"
- "stringWithFormat:"

```
