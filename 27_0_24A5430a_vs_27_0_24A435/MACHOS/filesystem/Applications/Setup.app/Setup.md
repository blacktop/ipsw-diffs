## Setup

> `/Applications/Setup.app/Setup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 5411.101.0.0.0
-  __TEXT.__text: 0x24cefc
+  __TEXT.__text: 0x24cfc4
   __TEXT.__auth_stubs: 0x28f0
-  __TEXT.__objc_stubs: 0x29420
+  __TEXT.__objc_stubs: 0x29440
   __TEXT.__objc_methlist: 0x1dd28
   __TEXT.__dlopen_cstrs: 0x179c
   __TEXT.__const: 0x3640
   __TEXT.__objc_classname: 0x5c43
-  __TEXT.__objc_methname: 0x40a3e
+  __TEXT.__objc_methname: 0x40a5e
   __TEXT.__objc_methtype: 0xcb1a
   __TEXT.__constg_swiftt: 0x3a14
   __TEXT.__swift5_typeref: 0x2792

   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_capture: 0x11cc
-  __TEXT.__oslogstring: 0x14eec
+  __TEXT.__oslogstring: 0x14ec2
   __TEXT.__cstring: 0xfd2e
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x1f8

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__auth_got: 0x1490
-  __DATA_CONST.__got: 0x1c48
+  __DATA_CONST.__got: 0x1c58
   __DATA_CONST.__auth_ptr: 0x518
   __DATA.__objc_const: 0x49d40
-  __DATA.__objc_selrefs: 0xcd18
+  __DATA.__objc_selrefs: 0xcd20
   __DATA.__objc_ivar: 0x1d58
   __DATA.__objc_data: 0xcb68
   __DATA.__data: 0x7a10

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 12357
-  Symbols:   1535
+  Symbols:   1537
   CStrings:  14883
 
Symbols:
+ _BYPrivacySubscriptionBundleIdentifier
+ _OBJC_CLASS_$_AMSAcknowledgePrivacyTask
Functions:
~ sub_100004e70 : 24 -> 328
~ sub_1001105f0 -> sub_100110720 : 764 -> 612
~ sub_100157bd4 -> sub_100157c6c : 348 -> 340
~ sub_100178d48 -> sub_100178dd8 : 116 -> 124
~ sub_100179ad0 -> sub_100179b68 : 108 -> 116
~ sub_10017d38c -> sub_10017d42c : 116 -> 124
~ sub_10017e100 -> sub_10017e1a8 : 116 -> 124
~ sub_100218728 -> sub_1002187d8 : 1504 -> 1508
~ sub_100227634 -> sub_1002276e8 : 672 -> 676
~ sub_100229c80 -> sub_100229d38 : 1928 -> 1936
~ sub_10022a5f0 -> sub_10022a6b0 : 752 -> 756
~ sub_10022b69c -> sub_10022b760 : 360 -> 364
CStrings:
+ "acknowledgementNeededForPrivacyIdentifier:account:"
+ "ams_isBundleOwner"
- "Enabling D&U submission for seed build..."
- "setBoolValue:forSetting:"
```
