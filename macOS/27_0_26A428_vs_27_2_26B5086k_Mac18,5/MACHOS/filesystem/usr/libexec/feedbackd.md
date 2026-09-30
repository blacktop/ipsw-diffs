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
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-235.0.0.0.0
-  __TEXT.__text: 0x68b14
-  __TEXT.__auth_stubs: 0x1b50
+238.0.0.0.0
+  __TEXT.__text: 0x6867c
+  __TEXT.__auth_stubs: 0x1b40
   __TEXT.__objc_stubs: 0x1140
   __TEXT.__objc_methlist: 0x4b4
   __TEXT.__const: 0x1d5c
   __TEXT.__swift5_typeref: 0xcfc
-  __TEXT.__oslogstring: 0x236f
+  __TEXT.__oslogstring: 0x234f
   __TEXT.__cstring: 0x2a15
   __TEXT.__constg_swiftt: 0xb84
   __TEXT.__swift5_fieldmd: 0x79c

   __TEXT.__swift_as_ret: 0xf8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x16e0
+  __TEXT.__unwind_info: 0x16d8
   __TEXT.__eh_frame: 0x3a98
   __DATA_CONST.__const: 0x1e28
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__auth_got: 0xdb0
-  __DATA_CONST.__got: 0x760
+  __DATA_CONST.__auth_got: 0xda8
+  __DATA_CONST.__got: 0x748
   __DATA_CONST.__auth_ptr: 0x408
   __DATA.__objc_const: 0x17a8
   __DATA.__objc_selrefs: 0x5d0
   __DATA.__objc_data: 0x770
-  __DATA.__data: 0x1960
+  __DATA.__data: 0x1950
   __DATA.__common: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1354
-  Symbols:   787
-  CStrings:  687
+  Functions: 1353
+  Symbols:   784
+  CStrings:  686
 
Symbols:
- _$s15FeedbackService12FBKSDonationC13DonationErrorO11unsupportedyA2EmFWC
- _$s15FeedbackService12FBKSDonationC13DonationErrorOMa
- _$s15FeedbackService12FBKSDonationC13DonationErrorOs0E0AAMc
Functions:
~ sub_10001e990 : 1228 -> 468
- sub_10001ee5c
+ sub_100031eb8
- sub_100032578
CStrings:
- "Donation not enabled"
```
