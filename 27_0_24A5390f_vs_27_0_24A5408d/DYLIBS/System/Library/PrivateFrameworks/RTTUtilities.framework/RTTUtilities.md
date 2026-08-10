## RTTUtilities

> `/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-536.0.0.0.0
-  __TEXT.__text: 0x29c58
+539.1.0.0.0
+  __TEXT.__text: 0x29cd8
   __TEXT.__objc_methlist: 0x1ec8
   __TEXT.__const: 0x250
   __TEXT.__dlopen_cstrs: 0x2cf

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x8
   __TEXT.__gcc_except_tab: 0xd98
-  __TEXT.__oslogstring: 0x383d
+  __TEXT.__oslogstring: 0x38b1
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0xb40
   __TEXT.__eh_frame: 0x1f8

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 842
   Symbols:   2298
-  CStrings:  613
+  CStrings:  614
 
Functions:
~ -[RTTTelephonyUtilities currentConditionsSupportRTTForContext:] : 444 -> 572
CStrings:
+ "Current conditions don't support RTT locally but relay is supported, so allowing outgoing calls to be dialed as RTT"
```
