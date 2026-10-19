## Setup

> `/Applications/Setup.app/Setup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
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
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-5411.2.4.0.0
-  __TEXT.__text: 0x253f1c
+5411.2.5.0.0
+  __TEXT.__text: 0x253fac
   __TEXT.__auth_stubs: 0x29b0
-  __TEXT.__objc_stubs: 0x29860
+  __TEXT.__objc_stubs: 0x29880
   __TEXT.__objc_methlist: 0x1e028
   __TEXT.__dlopen_cstrs: 0x1888
   __TEXT.__const: 0x3ad8
   __TEXT.__objc_classname: 0x5cac
-  __TEXT.__objc_methname: 0x41276
+  __TEXT.__objc_methname: 0x412b6
   __TEXT.__objc_methtype: 0xcc4d
   __TEXT.__constg_swiftt: 0x3bb8
   __TEXT.__swift5_typeref: 0x28d6

   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__swift5_capture: 0x129c
-  __TEXT.__oslogstring: 0x159c9
+  __TEXT.__oslogstring: 0x1599f
   __TEXT.__cstring: 0x1009b
   __TEXT.__swift5_proto: 0x15c
   __TEXT.__swift5_types: 0x214

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__auth_got: 0x14f0
-  __DATA_CONST.__got: 0x1c50
+  __DATA_CONST.__got: 0x1c60
   __DATA_CONST.__auth_ptr: 0x550
   __DATA.__objc_const: 0x4a288
-  __DATA.__objc_selrefs: 0xce60
+  __DATA.__objc_selrefs: 0xce68
   __DATA.__objc_ivar: 0x1d70
   __DATA.__objc_data: 0xcc78
   __DATA.__data: 0x7be8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 12637
-  Symbols:   1548
+  Symbols:   1550
   CStrings:  15017
 
Symbols:
+ _BYPrivacySubscriptionBundleIdentifier
+ _OBJC_CLASS_$_AMSAcknowledgePrivacyTask
Functions:
~ sub_100004e28 : 24 -> 328
~ sub_1001108fc -> sub_100110a2c : 764 -> 612
~ sub_100157b60 -> sub_100157bf8 : 348 -> 340
CStrings:
+ "acknowledgementNeededForPrivacyIdentifier:account:"
+ "ams_isBundleOwner"
- "Enabling D&U submission for seed build..."
- "setBoolValue:forSetting:"
```
