## companiond

> `/usr/libexec/companiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-524.10.94.0.0
-  __TEXT.__text: 0x85c58
+524.10.109.0.1
+  __TEXT.__text: 0x85c24
   __TEXT.__auth_stubs: 0x2d40
   __TEXT.__objc_stubs: 0x4460
   __TEXT.__objc_methlist: 0x2b60

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x16b0
-  __DATA_CONST.__got: 0xd00
+  __DATA_CONST.__got: 0xcf8
   __DATA_CONST.__auth_ptr: 0x560
   __DATA.__objc_const: 0x7568
   __DATA.__objc_selrefs: 0x1560
   __DATA.__objc_ivar: 0x414
   __DATA.__objc_data: 0x18e0
-  __DATA.__data: 0x1e10
+  __DATA.__data: 0x1df0
   __DATA.__common: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/AppleConnectClient.framework/AppleConnectClient
   Functions: 2295
-  Symbols:   1270
+  Symbols:   1269
   CStrings:  1956
 
Symbols:
+ _$s10Foundation4DateV2leoiySbAC_ACtFZ
- _$s10Foundation4DateVSLAAMc
- _$sSL2leoiySbx_xtFZTj
Functions:
~ sub_100037f9c : 2964 -> 2904
~ sub_1000583c4 -> sub_100058388 : 108 -> 112
~ sub_10006c920 -> sub_10006c8e8 : 108 -> 112
```
