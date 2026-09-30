## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-467.0.0.0.0
-  __TEXT.__text: 0x77aec
+469.0.0.0.0
+  __TEXT.__text: 0x77b88
   __TEXT.__objc_methlist: 0x5fcc
-  __TEXT.__cstring: 0x51e1
+  __TEXT.__cstring: 0x51e5
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xf0b7
   __TEXT.__gcc_except_tab: 0xdd0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3740
+  __DATA_CONST.__objc_selrefs: 0x3748
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x598
   __DATA_CONST.__got: 0x538
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x6b40
+  __AUTH_CONST.__cfstring: 0x6b60
   __AUTH_CONST.__objc_const: 0xc8f0
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__objc_intobj: 0x2d0

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2258
-  Symbols:   5634
-  CStrings:  2278
+  Symbols:   5637
+  CStrings:  2279
 
Symbols:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$setWiFiChipset:
+ _objc_msgSend$wifiChipset
Functions:
~ +[CaseDampeningExceptions allowDampeningExceptionFor:] : 1896 -> 1948
~ -[DiagnosticCaseManager initWithWorkspace:liaison:] : 616 -> 720
CStrings:
+ "int"
```
