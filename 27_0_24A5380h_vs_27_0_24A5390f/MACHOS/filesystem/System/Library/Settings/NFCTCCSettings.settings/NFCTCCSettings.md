## NFCTCCSettings

> `/System/Library/Settings/NFCTCCSettings.settings/NFCTCCSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-70.35.1.0.0
-  __TEXT.__text: 0x8cac
-  __TEXT.__auth_stubs: 0xad0
+70.37.0.0.0
+  __TEXT.__text: 0x8b7c
+  __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__objc_classname: 0x129

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x570
+  __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x268
   __DATA.__objc_const: 0x350

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 196
-  Symbols:   142
+  Symbols:   143
   CStrings:  75
 
Symbols:
+ _objc_retain_x21
+ _tcc_authorization_record_create_with_subject
+ _tcc_authorization_set_authorization_with_authorization_record
- _objc_release_x28
- _tcc_server_message_set_authorization_value
Functions:
~ sub_94e8 : 660 -> 356
```
