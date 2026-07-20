## CallHistorySyncHelper

> `/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-145.100.7.2.1
-  __TEXT.__text: 0x4063c
+147.100.5.2.1
+  __TEXT.__text: 0x40830
   __TEXT.__auth_stubs: 0x15d0
   __TEXT.__objc_stubs: 0x62a0
   __TEXT.__objc_methlist: 0x22bc
   __TEXT.__cstring: 0x1ad5
   __TEXT.__objc_classname: 0x497
-  __TEXT.__objc_methname: 0x7a63
+  __TEXT.__objc_methname: 0x7a73
   __TEXT.__const: 0x1440
   __TEXT.__objc_methtype: 0x18dc
   __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__oslogstring: 0x52b6
+  __TEXT.__oslogstring: 0x5396
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__swift5_typeref: 0x6b2
   __TEXT.__swift5_capture: 0x1b4

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0xe48
   __TEXT.__eh_frame: 0x6e8
-  __DATA_CONST.__const: 0x1c00
+  __DATA_CONST.__const: 0x1c20
   __DATA_CONST.__cfstring: 0x18a0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0xaf8
-  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__got: 0x580
   __DATA_CONST.__auth_ptr: 0x2c8
-  __DATA.__objc_const: 0x5c00
+  __DATA.__objc_const: 0x5c20
   __DATA.__objc_selrefs: 0x1f90
-  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_ivar: 0x224
   __DATA.__objc_data: 0x978
   __DATA.__data: 0xbf0
   __DATA.__bss: 0x1fe8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1393
-  Symbols:   645
-  CStrings:  2163
+  Functions: 1395
+  Symbols:   644
+  CStrings:  2167
 
Symbols:
- _kCallUpdatePropertyRead
CStrings:
+ "Calling back with message %{public}@"
+ "Fetch requested while sync in progress; will run another fetch once the current one finishes"
+ "Pending fetch changes result (%{public}@) message (%{public}@)"
+ "Pending fetch was requested during the previous sync; starting it now"
+ "_pendingFetch"
- "Calling back with result %{public}@"
```
