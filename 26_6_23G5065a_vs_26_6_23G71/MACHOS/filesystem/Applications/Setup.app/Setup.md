## Setup

> `/Applications/Setup.app/Setup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__cstring`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_floatobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 5382.4.7.0.0
-  __TEXT.__text: 0x25d62c
+  __TEXT.__text: 0x25d6b4
   __TEXT.__auth_stubs: 0x27e0
-  __TEXT.__objc_stubs: 0x297e0
+  __TEXT.__objc_stubs: 0x29800
   __TEXT.__objc_methlist: 0x1d6e0
   __TEXT.__dlopen_cstrs: 0x1436
   __TEXT.__objc_classname: 0x58d4
-  __TEXT.__objc_methname: 0x3fdb6
+  __TEXT.__objc_methname: 0x3fde6
   __TEXT.__objc_methtype: 0xc548
   __TEXT.__const: 0x34d0
   __TEXT.__constg_swiftt: 0x37fc

   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_capture: 0x1320
-  __TEXT.__oslogstring: 0x138e0
+  __TEXT.__oslogstring: 0x138b6
   __TEXT.__swift5_proto: 0x120
   __TEXT.__swift5_types: 0x1bc
   __TEXT.__swift_as_entry: 0x1c0

   __TEXT.__unwind_info: 0x9ce8
   __TEXT.__eh_frame: 0x4700
   __DATA_CONST.__auth_got: 0x1408
-  __DATA_CONST.__got: 0x1f28
+  __DATA_CONST.__got: 0x1f38
   __DATA_CONST.__auth_ptr: 0x568
   __DATA_CONST.__const: 0x8ab8
   __DATA_CONST.__cfstring: 0xb740

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0x47c40
-  __DATA.__objc_selrefs: 0xcd50
+  __DATA.__objc_selrefs: 0xcd58
   __DATA.__objc_ivar: 0x1d9c
   __DATA.__objc_data: 0xbc88
   __DATA.__data: 0x7378

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 12251
-  Symbols:   1539
+  Symbols:   1541
   CStrings:  14765
 
Symbols:
+ _BYPrivacySubscriptionBundleIdentifier
+ _OBJC_CLASS_$_AMSAcknowledgePrivacyTask
Functions:
~ sub_10007d3f4 : 24 -> 328
~ sub_100199b64 -> sub_100199c94 : 824 -> 664
~ sub_1001ef624 -> sub_1001ef6b4 : 364 -> 356
CStrings:
+ "Jul 11 2026"
+ "acknowledgementNeededForPrivacyIdentifier:account:"
+ "ams_isBundleOwner"
- "Enabling D&U submission for seed build..."
- "Jul  3 2026"
- "setBoolValue:forSetting:"
```
