## sportsd

> `/usr/libexec/sportsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-238.0.0.0.0
-  __TEXT.__text: 0xa0cb4
-  __TEXT.__auth_stubs: 0x3720
+239.0.0.0.0
+  __TEXT.__text: 0xa6fc4
+  __TEXT.__auth_stubs: 0x37c0
   __TEXT.__objc_stubs: 0x1100
   __TEXT.__objc_methlist: 0x6b4
   __TEXT.__const: 0x5f88
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1e68
-  __TEXT.__swift5_typeref: 0x39dc
+  __TEXT.__swift5_typeref: 0x39d6
   __TEXT.__swift5_reflstr: 0x2063
   __TEXT.__swift5_fieldmd: 0x2048
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__objc_classname: 0x6e2
   __TEXT.__objc_methname: 0x1e7d
   __TEXT.__objc_methtype: 0xd85
-  __TEXT.__swift5_capture: 0x2158
-  __TEXT.__oslogstring: 0x24c6
-  __TEXT.__cstring: 0x196e
+  __TEXT.__swift5_capture: 0x2464
+  __TEXT.__oslogstring: 0x2816
+  __TEXT.__cstring: 0x1a2e
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x148
   __TEXT.__swift_as_ret: 0x150
   __TEXT.__swift_as_cont: 0x314
-  __TEXT.__unwind_info: 0x30e0
-  __TEXT.__eh_frame: 0x4d64
-  __DATA_CONST.__const: 0x7f18
+  __TEXT.__unwind_info: 0x3158
+  __TEXT.__eh_frame: 0x4dfc
+  __DATA_CONST.__const: 0x85f8
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__auth_got: 0x1b98
+  __DATA_CONST.__auth_got: 0x1be8
   __DATA_CONST.__got: 0x980
-  __DATA_CONST.__auth_ptr: 0x9f0
+  __DATA_CONST.__auth_ptr: 0x9f8
   __DATA.__objc_const: 0x2538
   __DATA.__objc_selrefs: 0x6a0
   __DATA.__objc_data: 0xa00
-  __DATA.__data: 0x3c78
+  __DATA.__data: 0x3c88
   __DATA.__common: 0x1f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4135
-  Symbols:   1392
-  CStrings:  797
+  Functions: 4235
+  Symbols:   1403
+  CStrings:  815
 
Symbols:
+ _$s10Foundation12CharacterSetV12charactersInACSSh_tcfC
+ _$s10Foundation12CharacterSetV17controlCharactersACvgZ
+ _$s10Foundation12CharacterSetV8containsySbs7UnicodeO6ScalarVF
+ _$s10Foundation12CharacterSetVMn
+ _$s10Foundation3URLV4hostSSSgvg
+ _$s10Foundation3URLV4portSiSgvg
+ _$s10Foundation3URLV4userSSSgvg
+ _$s10Foundation3URLV6schemeSSSgvg
+ _$s10Foundation3URLV8passwordSSSgvg
+ _$sSS5countSivg
+ _$ss11_StringGutsV27foreignErrorCorrectedScalar10startingAts7UnicodeO0F0V_Si12scalarLengthtSS5IndexV_tF
CStrings:
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-"
+ "Cannot decode '%s' supplementary data: %@"
+ "Dropping '%s' supplementary data: %ld bytes is over the limit"
+ "Dropping autostart competitor with an invalid canonical id"
+ "Invalid cloud channel"
+ "Invalid cloud channel demand"
+ "Invalid event canonical id"
+ "Missing event canonical ids"
+ "Refresh rejected: missing or invalid event canonical id"
+ "Rejecting activity lookup with an invalid canonical id"
+ "Rejecting activity request with an invalid canonical id"
+ "Rejecting activity teardown with an invalid canonical id"
+ "Rejecting autostart request with an invalid canonical id"
+ "Rejecting cloud channel demand with out of bounds identifiers"
+ "Rejecting cloud channel request with an out of bounds channel or topic"
+ "Rejecting suppression check with an invalid canonical id"
+ "Tempo /register missing or invalid event canonical id"
+ "Tempo /unregister missing or invalid event canonical id"
+ "Tempo /unregister rejected a batch of %ld event canonical ids"
- "Tempo /register missing event canonical id"
```
