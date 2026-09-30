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
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

 208.3.0.0.0
-  __TEXT.__text: 0x720c0
-  __TEXT.__auth_stubs: 0x1cd0
+  __TEXT.__text: 0x725ac
+  __TEXT.__auth_stubs: 0x1ce0
   __TEXT.__objc_stubs: 0x1340
   __TEXT.__objc_methlist: 0x4f4
   __TEXT.__const: 0x1cb0
   __TEXT.__cstring: 0x2b59
-  __TEXT.__oslogstring: 0x2718
+  __TEXT.__oslogstring: 0x2738
   __TEXT.__swift5_typeref: 0xcdf
   __TEXT.__objc_classname: 0x3ff
   __TEXT.__constg_swiftt: 0xb68

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x1498
   __TEXT.__eh_frame: 0x4160
-  __DATA_CONST.__auth_got: 0xe70
-  __DATA_CONST.__got: 0x7a0
+  __DATA_CONST.__auth_got: 0xe78
+  __DATA_CONST.__got: 0x7b8
   __DATA_CONST.__auth_ptr: 0x3d0
   __DATA_CONST.__const: 0x1940
   __DATA_CONST.__objc_classlist: 0x70

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1330
-  Symbols:   818
-  CStrings:  736
+  Functions: 1331
+  Symbols:   821
+  CStrings:  737
 
Symbols:
+ _$s15FeedbackService12FBKSDonationC13DonationErrorO11unsupportedyA2EmFWC
+ _$s15FeedbackService12FBKSDonationC13DonationErrorOMa
+ _$s15FeedbackService12FBKSDonationC13DonationErrorOs0E0AAMc
Functions:
~ sub_100053a90 : 444 -> 416
+ sub_1000637a8
- sub_100064c5c
+ sub_1000653ec
CStrings:
+ "Donation not enabled"
```
