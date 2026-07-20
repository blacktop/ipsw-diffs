## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-2467.0.14.0.0
-  __TEXT.__text: 0x14938
+2467.0.23.0.0
+  __TEXT.__text: 0x14990
   __TEXT.__objc_methlist: 0x13bc
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0xacf
+  __TEXT.__cstring: 0xb02
   __TEXT.__oslogstring: 0x21c5
   __TEXT.__gcc_except_tab: 0x420
   __TEXT.__unwind_info: 0x500

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__objc_const: 0x29e0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x280
+  __AUTH.__objc_data: 0x1b8
   __DATA.__objc_ivar: 0x20c
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__objc_data: 0x438
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libobjc.A.dylib
   Functions: 584
   Symbols:   1290
-  CStrings:  282
+  CStrings:  285
 
Functions:
~ +[BGSystemTaskRequest purposeFromString:identifier:] : 220 -> 304
~ +[BGSystemTaskRequest taskRequestWithDescriptor:withIdentifier:] : 5308 -> 5312
CStrings:
+ "EnablementPhase0"
+ "EnablementPhase1"
+ "EnablementPhase2"
```
