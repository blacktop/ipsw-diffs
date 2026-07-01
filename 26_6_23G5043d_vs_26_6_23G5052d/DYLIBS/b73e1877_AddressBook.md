## AddressBook

> `/System/Library/Frameworks/AddressBook.framework/AddressBook`

```diff

-  __TEXT.__text: 0x1c958
+  __TEXT.__text: 0x1c954
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_methlist: 0x17d4
-  __TEXT.__const: 0xcc
-  __TEXT.__cstring: 0x1f49
+  __TEXT.__const: 0xd4
+  __TEXT.__cstring: 0x1edc
   __TEXT.__ustring: 0x1d6
-  __TEXT.__oslogstring: 0x36e
+  __TEXT.__oslogstring: 0x3db
   __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0x748
+  __TEXT.__unwind_info: 0x740
   __TEXT.__objc_classname: 0x1d9
-  __TEXT.__objc_methname: 0x38dc
+  __TEXT.__objc_methname: 0x38ca
   __TEXT.__objc_methtype: 0x71f
-  __TEXT.__objc_stubs: 0x3c60
+  __TEXT.__objc_stubs: 0x3c40
   __DATA_CONST.__got: 0x528
   __DATA_CONST.__const: 0x928
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10d8
+  __DATA_CONST.__objc_selrefs: 0x10d0
   __DATA_CONST.__objc_superrefs: 0xa8
   __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0xfe0
+  __AUTH_CONST.__cfstring: 0xfc0
   __AUTH_CONST.__objc_const: 0x2450
   __AUTH_CONST.__objc_intobj: 0x108
   __DATA.__objc_ivar: 0xe4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 685
-  Symbols:   2593
-  CStrings:  1185
+  Symbols:   2592
+  CStrings:  1183
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
- _objc_msgSend$numberWithDouble:
Functions:
~ _ABSCreateThumbnailDataAndCropRectFromImageData : 600 -> 596
CStrings:
+ "Thumbnail crop rect {{%f, %f}, {%f, %f}} origin y forced to 0 because it was negative (availableHeight = %d)"
- "Thumbnail crop rect {{%@, %@}, {%@, %@}} origin y forced to 0 because it was negative (availableHeight = %@)"
- "numberWithDouble:"

```
