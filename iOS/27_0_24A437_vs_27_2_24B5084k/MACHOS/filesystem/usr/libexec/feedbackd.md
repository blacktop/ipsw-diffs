## feedbackd

> `/usr/libexec/feedbackd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-235.0.0.0.0
-  __TEXT.__text: 0x746d8
-  __TEXT.__auth_stubs: 0x1f90
+238.0.0.0.0
+  __TEXT.__text: 0x74260
+  __TEXT.__auth_stubs: 0x1f80
   __TEXT.__objc_stubs: 0x1340
   __TEXT.__objc_methlist: 0x558
   __TEXT.__const: 0x1e08
   __TEXT.__swift5_typeref: 0xd44
-  __TEXT.__oslogstring: 0x27bf
+  __TEXT.__oslogstring: 0x279f
   __TEXT.__cstring: 0x2c85
   __TEXT.__constg_swiftt: 0xbec
   __TEXT.__swift5_fieldmd: 0x780

   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__auth_got: 0xfd0
-  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__auth_got: 0xfc8
+  __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__auth_ptr: 0x3f8
   __DATA.__objc_const: 0x1c28
   __DATA.__objc_selrefs: 0x670

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1452
-  Symbols:   873
-  CStrings:  756
+  Functions: 1451
+  Symbols:   870
+  CStrings:  755
 
Symbols:
- _$s15FeedbackService12FBKSDonationC13DonationErrorO11unsupportedyA2EmFWC
- _$s15FeedbackService12FBKSDonationC13DonationErrorOMa
- _$s15FeedbackService12FBKSDonationC13DonationErrorOs0E0AAMc
Functions:
~ sub_10001e190 : 1192 -> 440
- sub_10001e638
+ sub_10003035c
- sub_100030a04
CStrings:
- "Donation not enabled"
```
