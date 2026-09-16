## TranslationUIService

> `/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__objc_methname`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-389.1.0.0.0
-  __TEXT.__text: 0x502dc
-  __TEXT.__auth_stubs: 0x2540
-  __TEXT.__objc_stubs: 0x1020
+393.1.0.0.0
+  __TEXT.__text: 0x50320
+  __TEXT.__auth_stubs: 0x2530
+  __TEXT.__objc_stubs: 0x1060
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x3818
   __TEXT.__constg_swiftt: 0xfbc

   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__auth_got: 0x12a8
-  __DATA_CONST.__got: 0x7f8
+  __DATA_CONST.__auth_got: 0x12a0
+  __DATA_CONST.__got: 0x800
   __DATA_CONST.__auth_ptr: 0x960
   __DATA.__objc_const: 0x1028
-  __DATA.__objc_selrefs: 0x558
+  __DATA.__objc_selrefs: 0x568
   __DATA.__objc_data: 0xa20
   __DATA.__data: 0x2670
   __DATA.__common: 0x120

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1432
   Symbols:   255
-  CStrings:  452
+  CStrings:  454
 
Symbols:
+ _OBJC_CLASS_$__LTLanguageDetectionConfiguration
- _swift_retain_x9
Functions:
~ sub_100018f54 : 200 -> 204
~ sub_10003ae1c -> sub_10003ae20 : 404 -> 428
~ sub_10003b06c -> sub_10003b088 : 3888 -> 3920
~ sub_10003c0a4 -> sub_10003c0e0 : 264 -> 272
CStrings:
+ "initWithTaskHint:"
+ "languagesForText:configuration:completion:"
+ "setModel:"
- "languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:"
```
