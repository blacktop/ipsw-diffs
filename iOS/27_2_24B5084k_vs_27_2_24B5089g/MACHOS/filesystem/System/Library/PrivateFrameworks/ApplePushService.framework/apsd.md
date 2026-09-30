## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1168.200.31.0.0
-  __TEXT.__text: 0x11b26c
+1168.200.41.0.0
+  __TEXT.__text: 0x11b2e8
   __TEXT.__auth_stubs: 0x35f0
   __TEXT.__objc_stubs: 0x10ee0
   __TEXT.__init_offsets: 0xc

   __TEXT.__objc_methtype: 0x56e9
   __TEXT.__cstring: 0xfe43
   __TEXT.__const: 0x12503
-  __TEXT.__oslogstring: 0x144c5
+  __TEXT.__oslogstring: 0x14525
   __TEXT.__gcc_except_tab: 0x2680
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__constg_swiftt: 0x1540

   - /usr/lib/swift/libswiftos.dylib
   Functions: 7003
   Symbols:   1220
-  CStrings:  8695
+  CStrings:  8696
 
Functions:
~ sub_1000aa9d8 : 264 -> 380
~ sub_10010e738 -> sub_10010e7ac : 208 -> 204
~ sub_100111684 -> sub_1001116f4 : 488 -> 500
CStrings:
+ "%@ ignoring connect notification from stream %@ that is no longer bound to an interface"
```
