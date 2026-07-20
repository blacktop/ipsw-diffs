## followupd

> `/System/Library/PrivateFrameworks/CoreFollowUp.framework/Versions/A/Support/followupd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.0.4.0.0
-  __TEXT.__text: 0xe8c0
+2027.0.5.0.0
+  __TEXT.__text: 0xea34
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x2900
+  __TEXT.__objc_stubs: 0x29e0
   __TEXT.__objc_methlist: 0xb2c
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__cstring: 0x1dbc
+  __TEXT.__cstring: 0x1dcb
   __TEXT.__oslogstring: 0xe41
   __TEXT.__objc_classname: 0x13f
-  __TEXT.__objc_methname: 0x2603
+  __TEXT.__objc_methname: 0x2691
   __TEXT.__objc_methtype: 0x79e
   __TEXT.__unwind_info: 0x448
   __DATA_CONST.__const: 0x840
-  __DATA_CONST.__cfstring: 0xc00
+  __DATA_CONST.__cfstring: 0xc20
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x14d8
-  __DATA.__objc_selrefs: 0xbf0
+  __DATA.__objc_selrefs: 0xc28
   __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x2a8

   - /System/Library/PrivateFrameworks/CommonUtilities.framework/Versions/A/CommonUtilities
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/Versions/A/CoreFollowUp
+  - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 310
-  Symbols:   185
-  CStrings:  740
+  Symbols:   189
+  CStrings:  748
 
Symbols:
+ _FLFollowUpSiriBundleIdentifier
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_NSImage
Functions:
~ sub_100002e2c -> sub_100002e9c : 1648 -> 2020
CStrings:
+ "CGImage"
+ "com.apple.siri"
+ "imageForDescriptor:"
+ "initWithBundleIdentifier:"
+ "initWithCGImage:size:"
+ "initWithSize:scale:"
+ "placeholder"
+ "prepareImagesForImageDescriptors:"
```
