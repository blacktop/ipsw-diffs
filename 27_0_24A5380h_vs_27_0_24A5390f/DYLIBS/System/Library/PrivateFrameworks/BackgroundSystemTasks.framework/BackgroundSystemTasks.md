## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

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
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2467.0.14.502.1
-  __TEXT.__text: 0x134a0
+2467.0.23.502.1
+  __TEXT.__text: 0x134fc
   __TEXT.__objc_methlist: 0x13bc
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0xb8f
+  __TEXT.__cstring: 0xbc2
   __TEXT.__oslogstring: 0x2209
   __TEXT.__gcc_except_tab: 0x414
   __TEXT.__unwind_info: 0x560

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x690
+  __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 551
   Symbols:   1276
-  CStrings:  297
+  CStrings:  300
 
Functions:
~ +[BGSystemTaskRequest taskRequestWithDescriptor:withIdentifier:] : 5592 -> 5600
~ +[BGSystemTaskRequest purposeFromString:identifier:] : 212 -> 296
CStrings:
+ "EnablementPhase0"
+ "EnablementPhase1"
+ "EnablementPhase2"
```
