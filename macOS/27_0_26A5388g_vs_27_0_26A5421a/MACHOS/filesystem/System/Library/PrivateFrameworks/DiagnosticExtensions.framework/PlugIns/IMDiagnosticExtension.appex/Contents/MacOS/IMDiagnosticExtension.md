## IMDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/Contents/MacOS/IMDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1487.100.6.1.2
-  __TEXT.__text: 0xbbc
+1491.100.1.1.9
+  __TEXT.__text: 0xb84
   __TEXT.__auth_stubs: 0x160
-  __TEXT.__objc_stubs: 0x380
+  __TEXT.__objc_stubs: 0x360
   __TEXT.__objc_methlist: 0x64
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xdd
-  __TEXT.__objc_methname: 0x2f0
+  __TEXT.__objc_methname: 0x2de
+  __TEXT.__cstring: 0x241
   __TEXT.__oslogstring: 0x14c
   __TEXT.__objc_classname: 0x2d
   __TEXT.__objc_methtype: 0x2d
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0xb8
-  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__got: 0x68
   __DATA.__objc_const: 0x160
-  __DATA.__objc_selrefs: 0x100
+  __DATA.__objc_selrefs: 0xf8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 23
-  Symbols:   47
-  CStrings:  58
+  Symbols:   46
+  CStrings:  56
 
Symbols:
- _OBJC_CLASS_$_NSString
Functions:
~ sub_100001200 : 896 -> 840
CStrings:
+ "subsystem == \"com.apple.Messages\" OR subsystem == \"com.apple.MessagesEvents\" OR (subsystem == \"com.apple.IDS\" AND category == \"Delivery\") OR (subsystem == \"com.apple.IDS\" AND category == \"GUIDTRACE\") OR (subsystem == \"com.apple.IDS\" AND category == \"FaceTime\") OR (subsystem == \"com.apple.apsd\" AND category == \"courier\") OR (subsystem == \"com.apple.apsd\" AND category == \"courier-oversized\")"
- "com.apple.Messages"
- "stringWithFormat:"
- "subsystem == \"%@\""
```
