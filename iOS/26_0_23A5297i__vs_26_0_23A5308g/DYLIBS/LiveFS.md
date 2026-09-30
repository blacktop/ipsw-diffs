## LiveFS

> `/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS`

```diff

-737.0.17.0.2
-  __TEXT.__text: 0x1cbac
+737.0.29.0.2
+  __TEXT.__text: 0x1cbc8
   __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_methlist: 0x1f64
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0xf87
   __TEXT.__oslogstring: 0x1415
   __TEXT.__gcc_except_tab: 0xcf4
-  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__unwind_info: 0x9e0
   __TEXT.__objc_classname: 0x31c
-  __TEXT.__objc_methname: 0x4233
+  __TEXT.__objc_methname: 0x4261
   __TEXT.__objc_methtype: 0x2a22
-  __TEXT.__objc_stubs: 0x2780
+  __TEXT.__objc_stubs: 0x27a0
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0xda8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1020
+  __DATA_CONST.__objc_selrefs: 0x1028
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xa8
   __AUTH_CONST.__auth_got: 0x420

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28C22F06-499F-33DE-B40C-B8B8D1E7D408
+  UUID: DA648B5E-1BED-352C-B95A-C139156A7D86
   Functions: 771
-  Symbols:   2632
-  CStrings:  1339
+  Symbols:   2633
+  CStrings:  1340
 
Symbols:
+ -[LiveFSUserClient configureUserClient:pid:pidversion:supportBlockResource:]
+ -[LiveFSUserClient configureUserClient:pid:pidversion:supportBlockResource:].cold.1
+ _objc_msgSend$decomposedStringWithCanonicalMapping
- -[LiveFSUserClient configureUserClient:pid:pidversion:supportKOIO:]
- -[LiveFSUserClient configureUserClient:pid:pidversion:supportKOIO:].cold.1
Functions:
~ +[LiveFSIDHelper identifierForItem:name:parentID:] : 204 -> 232
CStrings:
+ "configureUserClient:pid:pidversion:supportBlockResource:"
+ "decomposedStringWithCanonicalMapping"
- "configureUserClient:pid:pidversion:supportKOIO:"

```
