## AppleMagicKeyboardSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/AppleMagicKeyboardSessionFilter.plugin/AppleMagicKeyboardSessionFilter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-9170.17.0.0.0
-  __TEXT.__text: 0x4954
-  __TEXT.__auth_stubs: 0x410
+10100.22.0.0.0
+  __TEXT.__text: 0x4978
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_stubs: 0xf80
   __TEXT.__objc_methlist: 0x62c
   __TEXT.__const: 0x90
   __TEXT.__objc_methname: 0x1146
-  __TEXT.__cstring: 0x331
+  __TEXT.__cstring: 0x343
   __TEXT.__oslogstring: 0x4c6
   __TEXT.__objc_classname: 0x7d
   __TEXT.__objc_methtype: 0x3fb
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__unwind_info: 0x1b0
   __DATA_CONST.__const: 0xa8
-  __DATA_CONST.__cfstring: 0x6c0
+  __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__auth_got: 0x220
   __DATA_CONST.__got: 0x78
   __DATA.__objc_const: 0xae8
   __DATA.__objc_selrefs: 0x518

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/HID.framework/HID
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 142
-  Symbols:   102
-  CStrings:  382
+  Symbols:   103
+  CStrings:  383
 
Symbols:
+ _MGGetSInt32Answer
Functions:
~ sub_2ef4 -> sub_2f34 : 384 -> 420
CStrings:
+ "DeviceClassNumber"
```
