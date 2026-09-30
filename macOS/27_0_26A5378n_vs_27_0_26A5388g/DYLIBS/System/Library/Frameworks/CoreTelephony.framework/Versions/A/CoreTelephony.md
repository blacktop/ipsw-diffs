## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__const`
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
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-13478.2.0.0.0
+13482.0.0.0.0
   __TEXT.__text: 0x170aec
-  __TEXT.__objc_methlist: 0x16ba4
+  __TEXT.__objc_methlist: 0x16bb4
   __TEXT.__cstring: 0x1bed8
   __TEXT.__const: 0x15d8
   __TEXT.__gcc_except_tab: 0x19be8

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0xc310
+  __TEXT.__unwind_info: 0xc318
   __TEXT.__eh_frame: 0x370
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9683
-  Symbols:   20670
+  Functions: 9684
+  Symbols:   20671
   CStrings:  5361
 
Symbols:
+ -[CTServiceDescriptor hash]
Functions:
~ __ZNK14CSIPhoneNumber26tryParseNANPCallForwardingEv : 500 -> 512
~ -[CTDeviceDataUsage totalDataUsedForPeriod:] : 576 -> 516
+ -[CTServiceDescriptor hash]
CStrings:
+ "13482"
+ "13482~59"
- "13478.2"
- "13478.2~112"
```
