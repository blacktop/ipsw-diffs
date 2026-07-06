## MailShareExtension

> `/System/Applications/Mail.app/Contents/PlugIns/MailShareExtension.appex/Contents/MacOS/MailShareExtension`

```diff

-  __TEXT.__text: 0x6998
+  __TEXT.__text: 0x696c
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_stubs: 0x1720
   __TEXT.__objc_methlist: 0x520

   __TEXT.__objc_classname: 0x7e
   __TEXT.__objc_methname: 0x1aef
   __TEXT.__objc_methtype: 0x4c8
-  __TEXT.__oslogstring: 0x843
+  __TEXT.__oslogstring: 0x842
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__unwind_info: 0x210
   __DATA_CONST.__const: 0x568

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__auth_got: 0x180
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1c8
   __DATA.__objc_const: 0x788
   __DATA.__objc_selrefs: 0x7b8
   __DATA.__objc_ivar: 0x44
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ _EMIsCurrentUserManagedAppleAccountForShare
- _EMIsManagedAppleAccount
Functions:
~ sub_100003c00 : 4324 -> 4280
CStrings:
+ "Share owner is MAA — skipping IDS check, adding all recipients as named participants"
- "Current user is MAA — skipping IDS check, adding all recipients as named participants"

```
