## UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

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
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-407.1.4.0.0
-  __TEXT.__text: 0x70f34
-  __TEXT.__auth_stubs: 0x2440
+407.1.5.0.0
+  __TEXT.__text: 0x71080
+  __TEXT.__auth_stubs: 0x2450
   __TEXT.__objc_stubs: 0x4820
   __TEXT.__objc_methlist: 0x12a8
   __TEXT.__const: 0x1eee

   __TEXT.__objc_methname: 0x5f51
   __TEXT.__objc_methtype: 0x137e
   __TEXT.__gcc_except_tab: 0x514
-  __TEXT.__oslogstring: 0x5a86
+  __TEXT.__oslogstring: 0x5ab6
   __TEXT.__constg_swiftt: 0x1150
   __TEXT.__swift5_typeref: 0x1de6
   __TEXT.__swift5_fieldmd: 0x55c

   __TEXT.__swift_as_cont: 0xcc
   __TEXT.__swift5_protos: 0x80
   __TEXT.__unwind_info: 0x1608
-  __TEXT.__eh_frame: 0x1098
+  __TEXT.__eh_frame: 0x10c0
   __DATA_CONST.__const: 0x2860
   __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0xd0

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x1230
+  __DATA_CONST.__auth_got: 0x1238
   __DATA_CONST.__got: 0x848
   __DATA_CONST.__auth_ptr: 0x4d8
   __DATA.__objc_const: 0x3160

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 1515
-  Symbols:   952
-  CStrings:  1486
+  Symbols:   953
+  CStrings:  1487
 
Symbols:
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
Functions:
~ sub_1000345e0 : 1856 -> 2152
~ sub_100049814 -> sub_10004993c : 32 -> 68
CStrings:
+ "Last refresh was within a minute of now, skipping refresh."
+ "Minutes since last refresh: %{public}ld"
- "Last refresh was less than one minute ago, skipping refresh."
```
