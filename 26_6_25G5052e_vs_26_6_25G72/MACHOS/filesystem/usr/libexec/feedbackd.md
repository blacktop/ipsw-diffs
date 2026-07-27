## feedbackd

> `/usr/libexec/feedbackd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

 208.3.0.0.0
-  __TEXT.__text: 0x666ec
-  __TEXT.__auth_stubs: 0x1a00
+  __TEXT.__text: 0x66bfc
+  __TEXT.__auth_stubs: 0x1a10
   __TEXT.__objc_stubs: 0x1140
   __TEXT.__objc_methlist: 0x464
   __TEXT.__const: 0x1c58
   __TEXT.__cstring: 0x2929
-  __TEXT.__oslogstring: 0x2338
+  __TEXT.__oslogstring: 0x2358
   __TEXT.__swift5_typeref: 0xc85
   __TEXT.__objc_classname: 0x31f
   __TEXT.__constg_swiftt: 0xb20

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x12a8
   __TEXT.__eh_frame: 0x38f0
-  __DATA_CONST.__auth_got: 0xd08
-  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__auth_got: 0xd10
+  __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x3e8
   __DATA_CONST.__const: 0x19b0
   __DATA_CONST.__objc_classlist: 0x68

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1242
-  Symbols:   756
-  CStrings:  673
+  Functions: 1243
+  Symbols:   759
+  CStrings:  674
 
Symbols:
+ _$s15FeedbackService12FBKSDonationC13DonationErrorO11unsupportedyA2EmFWC
+ _$s15FeedbackService12FBKSDonationC13DonationErrorOMa
+ _$s15FeedbackService12FBKSDonationC13DonationErrorOs0E0AAMc
Functions:
~ sub_1000495f0 : 468 -> 440
+ sub_100059488
- sub_10005be04
+ sub_10005c56c
CStrings:
+ "Donation not enabled"
```
