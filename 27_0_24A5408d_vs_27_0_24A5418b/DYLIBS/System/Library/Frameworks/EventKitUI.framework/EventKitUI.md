## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1572.0.0.0.0
-  __TEXT.__text: 0x1f9aec
-  __TEXT.__objc_methlist: 0x2038c
+1572.0.100.0.0
+  __TEXT.__text: 0x1f9ba4
+  __TEXT.__objc_methlist: 0x2039c
   __TEXT.__const: 0x2e94
   __TEXT.__cstring: 0xd1a4
   __TEXT.__gcc_except_tab: 0x3f78

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x660
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfbf0
+  __DATA_CONST.__objc_selrefs: 0xfbf8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x8c8
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __DATA_CONST.__got: 0x1c10
+  __DATA_CONST.__got: 0x1c18
   __AUTH_CONST.__const: 0x2f98
   __AUTH_CONST.__cfstring: 0xb4c0
-  __AUTH_CONST.__objc_const: 0x31838
+  __AUTH_CONST.__objc_const: 0x31868
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70

   __AUTH_CONST.__auth_got: 0x17a0
   __AUTH.__objc_data: 0x7da0
   __AUTH.__data: 0x1048
-  __DATA.__objc_ivar: 0x2594
+  __DATA.__objc_ivar: 0x2598
   __DATA.__data: 0x51c8
   __DATA.__bss: 0x19e8
   __DATA.__common: 0x238

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12398
-  Symbols:   25108
+  Functions: 12399
+  Symbols:   25112
   CStrings:  2364
 
Symbols:
+ -[EKEventAttendeePicker searchResults]
+ GCC_except_table26
+ GCC_except_table45
+ GCC_except_table51
+ _OBJC_IVAR_$_EKEventAttendeePicker._lastFinishedSearchId
- GCC_except_table48
Functions:
~ -[EKEventAttendeePicker dealloc] : 152 -> 180
+ -[EKEventAttendeePicker searchResults]
~ -[EKEventAttendeePicker _hideSearchResultsViewAndCancelOutstandingSearches:] : 344 -> 368
~ ___44-[EKEventAttendeePicker finishedTaskWithID:]_block_invoke : 104 -> 112
~ -[EKEventAttendeePicker searchWithText:] : 348 -> 372
~ -[EKEventAttendeePicker searchForCorecipients] : 356 -> 380
~ -[EKEventAttendeePicker .cxx_destruct] : 460 -> 480
CStrings:
+ "\xf0\xf1"
- "\xf0\xe1"
```
