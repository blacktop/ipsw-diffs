## fontd

> `System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Support/fontd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-408.6.0.3.0
-  __TEXT.__text: 0x34d14
-  __TEXT.__auth_stubs: 0x13a0
+408.20.0.2.0
+  __TEXT.__text: 0x3549c
+  __TEXT.__auth_stubs: 0x13e0
   __TEXT.__objc_stubs: 0xe20
   __TEXT.__objc_methlist: 0x638
-  __TEXT.__gcc_except_tab: 0x4cf8
+  __TEXT.__gcc_except_tab: 0x4d74
   __TEXT.__const: 0x7b0
-  __TEXT.__cstring: 0x7b92
+  __TEXT.__cstring: 0x7bdc
   __TEXT.__objc_classname: 0xfa
   __TEXT.__objc_methname: 0x10fb
   __TEXT.__objc_methtype: 0x8cf
   __TEXT.__oslogstring: 0x3
   __TEXT.__unwind_info: 0x1b00
-  __DATA_CONST.__auth_got: 0x9e8
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__auth_got: 0xa08
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x49a8
-  __DATA_CONST.__cfstring: 0x27c0
+  __DATA_CONST.__cfstring: 0x27e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/FontServices.framework/Versions/A/FontServices
   - /System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1027
-  Symbols:   403
-  CStrings:  828
+  Functions: 1029
+  Symbols:   408
+  CStrings:  829
 
Symbols:
+ _CFDataGetTypeID
+ _SecTaskCreateWithAuditToken
+ _SecTaskValidateForRequirement
+ __CFURLIsFileURL
+ ___NSArray0__struct
CStrings:
+ "anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.9]"
```
