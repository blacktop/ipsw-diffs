## FileProviderDiagnosticExtension

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-4838.0.70.0.0
-  __TEXT.__text: 0x2d10
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0xb00
+4838.0.93.0.0
+  __TEXT.__text: 0x2d7c
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0xb40
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x270
-  __TEXT.__cstring: 0x3b0
+  __TEXT.__cstring: 0x3ac
   __TEXT.__oslogstring: 0x7c6
   __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methname: 0x811
-  __TEXT.__objc_methtype: 0x46
+  __TEXT.__objc_methname: 0x835
+  __TEXT.__objc_methtype: 0x57
   __TEXT.__unwind_info: 0x108
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__cfstring: 0x4c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0xc8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x2c8
+  __DATA.__objc_selrefs: 0x2d8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /usr/lib/libprequelite.dylib
   Functions: 58
   Symbols:   94
-  CStrings:  175
+  CStrings:  178
 
Symbols:
+ _OBJC_CLASS_$_NSUUID
+ _objc_retain_x26
- _objc_retain_x25
- _objc_retain_x27
Functions:
~ sub_100000f4c : 2300 -> 2316
~ sub_100001bc4 -> sub_100001bd4 : 1080 -> 1084
~ sub_100002cd0 -> sub_100002ce4 : 1188 -> 1276
CStrings:
+ "@32@0:8@16@24"
+ "@48@0:8@16@24@32@40"
+ "FileProviderDiagnosticLogs-%@.log"
+ "FileProviderSystemDatabase-%@.txt"
+ "UUID"
+ "UUIDString"
+ "_fpDumpAttachmentItemWithTempURL:ProviderFilter:displayName:requestID:"
+ "_logAttachmentItemWithTempURL:requestID:"
- "@40@0:8@16@24@32"
- "FileProviderDiagnosticLogs-%llu.log"
- "FileProviderSystemDatabase-%llu.txt"
- "_fpDumpAttachmentItemWithTempURL:ProviderFilter:displayName:"
- "_logAttachmentItemWithTempURL:"
```
