## osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1056.0.17.0.0
-  __TEXT.__text: 0x21220
+1056.0.22.0.0
+  __TEXT.__text: 0x212a8
   __TEXT.__auth_stubs: 0x1440
-  __TEXT.__objc_stubs: 0x2d20
+  __TEXT.__objc_stubs: 0x2d60
   __TEXT.__objc_methlist: 0x8bc
   __TEXT.__const: 0x318
-  __TEXT.__oslogstring: 0x2525
-  __TEXT.__cstring: 0x20b8
+  __TEXT.__oslogstring: 0x2585
+  __TEXT.__cstring: 0x20c8
   __TEXT.__objc_classname: 0x239
   __TEXT.__objc_methtype: 0x547
   __TEXT.__gcc_except_tab: 0x700
-  __TEXT.__objc_methname: 0x25f7
+  __TEXT.__objc_methname: 0x262d
   __TEXT.__constg_swiftt: 0xd8
   __TEXT.__swift5_typeref: 0x256
   __TEXT.__swift5_reflstr: 0x1c

   __DATA_CONST.__got: 0x668
   __DATA_CONST.__auth_ptr: 0x90
   __DATA.__objc_const: 0x14b8
-  __DATA.__objc_selrefs: 0xc70
+  __DATA.__objc_selrefs: 0xc80
   __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x2f0

   - /usr/lib/swift/libswiftos.dylib
   Functions: 442
   Symbols:   562
-  CStrings:  1077
+  CStrings:  1082
 
Functions:
~ sub_10000248c : 2380 -> 2516
CStrings:
+ "1"
+ "DoNotSubmit"
+ "Panic report submission disabled by EDT; marking log as DoNotSubmit and skipping urgent submission"
+ "markFile:withKey:value:"
+ "panicReportSubmissionDisabled"
```
