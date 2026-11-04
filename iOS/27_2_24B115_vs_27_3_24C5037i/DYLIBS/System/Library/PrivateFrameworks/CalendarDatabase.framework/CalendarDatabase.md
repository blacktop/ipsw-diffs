## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

-1291.2.3.0.0
-  __TEXT.__text: 0xd7fec
+1291.2.4.0.0
+  __TEXT.__text: 0xd81d4
   __TEXT.__objc_methlist: 0x1f24
   __TEXT.__cstring: 0x1fb91
   __TEXT.__const: 0xaa4
   __TEXT.__gcc_except_tab: 0x18f0
-  __TEXT.__oslogstring: 0xcdd0
+  __TEXT.__oslogstring: 0xcf1e
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x4010
+  __TEXT.__unwind_info: 0x4018
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2500
+  __DATA_CONST.__objc_selrefs: 0x24f8
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0x9a0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4253
-  Symbols:   6562
-  CStrings:  3131
+  Functions: 4254
+  Symbols:   6563
+  CStrings:  3135
 
Symbols:
+ GCC_except_table55
+ __CalAttachmentFileStringIsSafePathComponent
- GCC_except_table57
Functions:
~ -[CalAttachmentFileCleanupContext addAttachmentToDelete:] : 112 -> 188
~ __CalAttachmentFileGetAttachmentContainerURLsForStoreProperties : 380 -> 348
+ __CalAttachmentFileStringIsSafePathComponent
~ __CalAttachmentFileSetFileDataWithOpenFile : 2484 -> 2800
CStrings:
+ "Refusing to build a path for attachment file %d: its UUID is not a safe path component"
+ "Refusing to build a path for attachment file %d: the store UUID is not a safe path component"
+ "Refusing to clean up after an attachment whose UUID is not a safe path component"
+ "Refusing to write attachment file %d outside the calendar data container"
```
