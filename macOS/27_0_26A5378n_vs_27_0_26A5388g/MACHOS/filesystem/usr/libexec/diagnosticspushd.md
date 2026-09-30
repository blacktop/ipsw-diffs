## diagnosticspushd

> `/usr/libexec/diagnosticspushd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x13dc0
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x640
+35.0.0.0.0
+  __TEXT.__text: 0x13fec
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_stubs: 0x620
   __TEXT.__objc_methlist: 0x24c
   __TEXT.__const: 0x1950
-  __TEXT.__oslogstring: 0x5cd
+  __TEXT.__oslogstring: 0x60d
   __TEXT.__objc_classname: 0xe8
-  __TEXT.__objc_methname: 0x830
+  __TEXT.__objc_methname: 0x820
   __TEXT.__objc_methtype: 0x438
   __TEXT.__constg_swiftt: 0x414
   __TEXT.__swift5_typeref: 0x455

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x548
+  __DATA_CONST.__auth_got: 0x588
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__auth_ptr: 0x1a8
   __DATA.__objc_const: 0x4f8
-  __DATA.__objc_selrefs: 0x2a0
+  __DATA.__objc_selrefs: 0x298
   __DATA.__objc_data: 0x180
   __DATA.__data: 0x7b0
   __DATA.__common: 0xa8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 536
-  Symbols:   296
+  Symbols:   304
   CStrings:  215
 
Symbols:
+ _$s15EnhancedLogging13SessionStatusO16debugDescriptionSSvg
+ _$s15EnhancedLogging13SessionStatusO23stillNeedsEnrollConsentSbvg
+ _$s15EnhancedLogging14SessionManagerC07currentC0AA0C0CSgvg
+ _$s15EnhancedLogging14SessionManagerCACycfc
+ _$s15EnhancedLogging14SessionManagerCMa
+ _$s15EnhancedLogging7SessionC6cancel12remoteSourceySb_tF
+ _$s15EnhancedLogging7SessionC6statusAA0C6StatusOvg
+ _swift_release_n
Functions:
~ sub_1000026e4 : 208 -> 220
~ sub_1000027b4 -> sub_1000027c0 : 1868 -> 2340
~ sub_100002f00 -> sub_1000030e4 : 276 -> 312
~ sub_100003014 -> sub_10000321c : 276 -> 312
CStrings:
+ "Ignoring TimberLorry teardown request; status is %{public}s"
- "cancelSession"
```
