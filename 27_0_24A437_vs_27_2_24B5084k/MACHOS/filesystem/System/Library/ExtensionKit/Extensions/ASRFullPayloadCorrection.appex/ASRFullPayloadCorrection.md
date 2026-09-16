## ASRFullPayloadCorrection

> `/System/Library/ExtensionKit/Extensions/ASRFullPayloadCorrection.appex/ASRFullPayloadCorrection`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-3600.70.47.11.1
-  __TEXT.__text: 0x2dc8
+3605.10.1.0.0
+  __TEXT.__text: 0x2d80
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__const: 0x30e
+  __TEXT.__const: 0x35e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0xdf
   __TEXT.__constg_swiftt: 0x74

   __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x140
   __DATA.__data: 0x100
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 84
-  Symbols:   76
+  Symbols:   78
   CStrings:  6
 
Symbols:
+ _ASRFullPayloadCorrectionVersionNumber
+ _ASRFullPayloadCorrectionVersionString
Functions:
~ sub_100001eec : 1308 -> 1236
```
