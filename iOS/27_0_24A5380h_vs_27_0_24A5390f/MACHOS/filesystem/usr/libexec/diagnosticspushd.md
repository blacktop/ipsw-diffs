## diagnosticspushd

> `/usr/libexec/diagnosticspushd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x15bc8
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_stubs: 0x460
+35.0.0.0.0
+  __TEXT.__text: 0x15dd0
+  __TEXT.__auth_stubs: 0xe70
+  __TEXT.__objc_stubs: 0x440
   __TEXT.__objc_methlist: 0x24c
   __TEXT.__const: 0x16c2
-  __TEXT.__oslogstring: 0x62d
+  __TEXT.__oslogstring: 0x66d
   __TEXT.__objc_classname: 0xe8
-  __TEXT.__objc_methname: 0x6c0
+  __TEXT.__objc_methname: 0x6b0
   __TEXT.__objc_methtype: 0x408
   __TEXT.__constg_swiftt: 0x478
   __TEXT.__swift5_typeref: 0x499

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x6f8
+  __DATA_CONST.__auth_got: 0x740
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x1d0
   __DATA.__objc_const: 0x4b8
-  __DATA.__objc_selrefs: 0x228
+  __DATA.__objc_selrefs: 0x220
   __DATA.__objc_data: 0x180
   __DATA.__data: 0xa98
   __DATA.__bss: 0x2a00

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 540
-  Symbols:   346
+  Symbols:   355
   CStrings:  201
 
Symbols:
+ _$s15EnhancedLogging13SessionStatusO16debugDescriptionSSvg
+ _$s15EnhancedLogging13SessionStatusO23stillNeedsEnrollConsentSbvg
+ _$s15EnhancedLogging14SessionManagerC07currentC0AA0C0CSgvg
+ _$s15EnhancedLogging14SessionManagerCACycfc
+ _$s15EnhancedLogging14SessionManagerCMa
+ _$s15EnhancedLogging7SessionC6cancel12remoteSourceySb_tF
+ _$s15EnhancedLogging7SessionC6statusAA0C6StatusOvg
+ _swift_release_n
+ _swift_retain_x21
Functions:
~ sub_100005a18 : 204 -> 216
~ sub_100005ae4 -> sub_100005af0 : 1584 -> 2020
~ sub_100006114 -> sub_1000062d4 : 276 -> 312
~ sub_100006228 -> sub_10000640c : 276 -> 312
CStrings:
+ "Ignoring TimberLorry teardown request; status is %{public}s"
- "cancelSession"
```
