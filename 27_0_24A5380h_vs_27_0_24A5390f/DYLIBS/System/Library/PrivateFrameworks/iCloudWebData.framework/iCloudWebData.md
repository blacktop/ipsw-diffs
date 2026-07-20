## iCloudWebData

> `/System/Library/PrivateFrameworks/iCloudWebData.framework/iCloudWebData`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-71.1.0.0.0
-  __TEXT.__text: 0x217b8
-  __TEXT.__const: 0x12b8
+71.3.0.0.0
+  __TEXT.__text: 0x21bb4
+  __TEXT.__const: 0x12a8
   __TEXT.__swift5_typeref: 0x72a
   __TEXT.__swift5_reflstr: 0x283
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__constg_swiftt: 0x4ec
   __TEXT.__swift5_fieldmd: 0x240
-  __TEXT.__oslogstring: 0x426
+  __TEXT.__oslogstring: 0x466
   __TEXT.__swift5_proto: 0x70
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift_as_entry: 0x80

   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40
+  __DATA_CONST.__objc_selrefs: 0x48
   __DATA_CONST.__got: 0x270
   __AUTH_CONST.__const: 0x2a8
   __AUTH_CONST.__objc_const: 0x530

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 642
-  Symbols:   292
-  CStrings:  41
+  Symbols:   293
+  CStrings:  42
 
Symbols:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_retain_x20
- _objc_release_x23
Functions:
~ sub_2b7c84c68 -> sub_2b94dfc68 : 1804 -> 2824
~ sub_2b7c9014c -> sub_2b94eb548 : 104 -> 248
~ ___swift_closure_destructor -> sub_2b94eb640 : 204 -> 224
~ sub_2b7c90280 -> sub_2b94eb720 : 252 -> 136
~ sub_2b7c9037c -> sub_2b94eb7a8 : 248 -> 104
~ sub_2b7c90474 -> ___swift_closure_destructor : 224 -> 204
~ ___swift_closure_destructor.3 -> sub_2b94eb8dc : 56 -> 252
~ sub_2b7c9058c -> ___swift_closure_destructor.3 : 184 -> 56
~ sub_2b7c90644 -> sub_2b94eba10 : 136 -> 184
CStrings:
+ "ModelContainer init failed, purging store and retrying: %@"
```
