## RemoteTextInput

> `/System/Library/PrivateFrameworks/RemoteTextInput.framework/Versions/A/RemoteTextInput`

```diff

-151.0.0.0.0
-  __TEXT.__text: 0x1f7e4
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x22e4
+153.0.0.0.0
+  __TEXT.__text: 0x1f860
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_methlist: 0x22f4
   __TEXT.__const: 0xb8
   __TEXT.__cstring: 0x2a8d
   __TEXT.__oslogstring: 0xbf5
   __TEXT.__gcc_except_tab: 0x1b4
   __TEXT.__dlopen_cstrs: 0x9b
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__unwind_info: 0x7e0
   __TEXT.__objc_classname: 0x3b8
-  __TEXT.__objc_methname: 0x67aa
+  __TEXT.__objc_methname: 0x67d0
   __TEXT.__objc_methtype: 0x14c1
   __TEXT.__objc_stubs: 0x3c60
   __DATA_CONST.__got: 0x200

   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15c0
+  __DATA_CONST.__objc_selrefs: 0x15c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0xae0
   __AUTH_CONST.__cfstring: 0x2740
   __AUTH_CONST.__objc_const: 0x6798

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 909
-  Symbols:   2309
+  Functions: 910
+  Symbols:   2313
   CStrings:  397
 
Symbols:
+ -[RTIDocumentState selectionRangeForDocumentStateRange:]
+ GCC_except_table25
+ GCC_except_table29
+ GCC_except_table39
+ _audit_token_to_pid
+ _objc_getProperty
+ _objc_msgSend$truncatedRangeInSelectedText
+ _objc_setProperty_atomic
- GCC_except_table28
- GCC_except_table38
- _objc_msgSend$selectedRangeInMarkedText

```
