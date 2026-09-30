## tzd

> `/usr/libexec/tzd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-89.0.0.0.0
-  __TEXT.__text: 0xe180
+90.0.0.0.0
+  __TEXT.__text: 0xe1f8
   __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_stubs: 0x860
-  __TEXT.__objc_methlist: 0x3d0
+  __TEXT.__objc_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x3e8
   __TEXT.__const: 0x6a0
   __TEXT.__cstring: 0xf34
-  __TEXT.__objc_methname: 0xf6b
-  __TEXT.__objc_classname: 0xbe
-  __TEXT.__objc_methtype: 0x9d5
+  __TEXT.__objc_methname: 0xfbb
+  __TEXT.__objc_classname: 0xce
+  __TEXT.__objc_methtype: 0x9d7
   __TEXT.__swift5_typeref: 0x2b4
   __TEXT.__swift5_capture: 0x160
   __TEXT.__swift5_entry: 0x8

   __TEXT.__eh_frame: 0x168
   __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__cfstring: 0xa0
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x4e8
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA.__objc_const: 0x888
-  __DATA.__objc_selrefs: 0x3f0
+  __DATA.__objc_const: 0x918
+  __DATA.__objc_selrefs: 0x408
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x250
+  __DATA.__objc_data: 0x2a0
   __DATA.__data: 0x680
   __DATA.__bss: 0x810
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 296
-  Symbols:   286
-  CStrings:  298
+  Functions: 297
+  Symbols:   287
+  CStrings:  302
 
Symbols:
+ _OBJC_CLASS_$_UNNotificationIcon
Functions:
+ sub_100001c64
CStrings:
+ "TZNotificationIcon"
+ "iconForApplicationIdentifier:"
+ "setIcon:"
+ "setIconForApplicationIdentifier:onContent:"
```
