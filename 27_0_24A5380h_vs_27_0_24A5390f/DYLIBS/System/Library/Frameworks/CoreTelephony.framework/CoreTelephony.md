## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
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
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-13478.3.1.3.0
-  __TEXT.__text: 0x1d3204
-  __TEXT.__objc_methlist: 0x1fa9c
+13482.1.0.0.0
+  __TEXT.__text: 0x1d3220
+  __TEXT.__objc_methlist: 0x1faac
   __TEXT.__const: 0x1736
   __TEXT.__gcc_except_tab: 0x258a0
-  __TEXT.__cstring: 0x21ff8
+  __TEXT.__cstring: 0x21fe8
   __TEXT.__oslogstring: 0x54c6
   __TEXT.__swift5_typeref: 0x2b4
   __TEXT.__constg_swiftt: 0x140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 13083
-  Symbols:   27471
+  Functions: 13084
+  Symbols:   27472
   CStrings:  6527
 
Symbols:
+ -[CTServiceDescriptor hash]
Functions:
~ __ZNK14CSIPhoneNumber26tryParseNANPCallForwardingEv : 576 -> 608
+ -[CTServiceDescriptor hash]
~ -[CTDeviceDataUsage totalDataUsedForPeriod:] : 564 -> 512
CStrings:
+ "13482.1"
+ "13482.1~1"
- "13478.3.1.3"
- "13478.3.1.3~3"
```
