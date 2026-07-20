## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
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
-  __TEXT.__text: 0x1a1510
-  __TEXT.__objc_methlist: 0x15a6c
+1973.0.0.0.0
+  __TEXT.__text: 0x1a1644
+  __TEXT.__objc_methlist: 0x15a74
   __TEXT.__cstring: 0xbddf
   __TEXT.__const: 0x4810
   __TEXT.__oslogstring: 0xef78

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae58
+  __DATA_CONST.__objc_selrefs: 0xae60
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x530
   __DATA_CONST.__objc_arraydata: 0x5d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10665
-  Symbols:   17541
+  Functions: 10666
+  Symbols:   17543
   CStrings:  2666
 
Symbols:
+ -[EKEvent locationTitleExcludingConferenceRooms]
+ GCC_except_table351
+ GCC_except_table397
+ GCC_except_table400
+ GCC_except_table435
+ GCC_except_table440
+ GCC_except_table542
- GCC_except_table350
- GCC_except_table399
- GCC_except_table434
- GCC_except_table439
- GCC_except_table470
Functions:
~ -[EKCalendarItem filterAttendeesPendingDeletion:] : 348 -> 412
+ -[EKEvent locationTitleExcludingConferenceRooms]
```
