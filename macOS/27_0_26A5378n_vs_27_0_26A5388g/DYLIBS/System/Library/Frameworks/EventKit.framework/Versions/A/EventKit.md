## EventKit

> `/System/Library/Frameworks/EventKit.framework/Versions/A/EventKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1970.0.0.0.0
-  __TEXT.__text: 0x1b67a0
-  __TEXT.__objc_methlist: 0x15a6c
+1973.0.0.0.0
+  __TEXT.__text: 0x1b68f8
+  __TEXT.__objc_methlist: 0x15a74
   __TEXT.__cstring: 0xc22f
   __TEXT.__const: 0x47b0
   __TEXT.__oslogstring: 0xeda8

   __TEXT.__swift_as_ret: 0xe8
   __TEXT.__swift_as_cont: 0x1a4
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__unwind_info: 0x68e0
+  __TEXT.__unwind_info: 0x68e8
   __TEXT.__eh_frame: 0x2578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaeb8
+  __DATA_CONST.__objc_selrefs: 0xaec0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x5d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10791
+  Functions: 10792
   Symbols:   17828
   CStrings:  2695
 
Symbols:
+ -[EKEvent locationTitleExcludingConferenceRooms]
+ GCC_except_table350
+ GCC_except_table402
+ GCC_except_table407
+ GCC_except_table442
+ GCC_except_table557
- GCC_except_table349
- GCC_except_table406
- GCC_except_table441
- GCC_except_table448
- GCC_except_table483
- GCC_except_table556
Functions:
~ -[EKCalendarItem filterAttendeesPendingDeletion:] : 364 -> 436
+ -[EKEvent locationTitleExcludingConferenceRooms]
```
