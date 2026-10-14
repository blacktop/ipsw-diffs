## TactSwitchHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/TactSwitchHIDServiceFilter.plugin/TactSwitchHIDServiceFilter`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-10110.3.0.0.0
-  __TEXT.__text: 0x2b3c
+10110.4.0.0.0
+  __TEXT.__text: 0x2b88
   __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_stubs: 0x740
-  __TEXT.__objc_methlist: 0x488
+  __TEXT.__objc_methlist: 0x490
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0x37c
   __TEXT.__cstring: 0x3a3
-  __TEXT.__objc_methname: 0x9a8
+  __TEXT.__objc_methname: 0x9ea
   __TEXT.__oslogstring: 0x4c8
   __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methtype: 0x65a
+  __TEXT.__objc_methtype: 0x6b5
   __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__const: 0x240
   __DATA_CONST.__cfstring: 0x3a0

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x58
-  __DATA.__objc_const: 0x928
-  __DATA.__objc_selrefs: 0x330
+  __DATA.__objc_const: 0x930
+  __DATA.__objc_selrefs: 0x338
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 71
-  Symbols:   277
-  CStrings:  272
+  Functions: 72
+  Symbols:   278
+  CStrings:  275
 
Symbols:
+ __ZN14SABinaryWriter5writeEPKvm
Functions:
~ ___53-[TouchSensitiveButtonHIDService handleResetRequest:]_block_invoke : 304 -> 308
~ __ZN14SABinaryWriter15initHostRequestEhtPKv : 240 -> 168
+ __ZN14SABinaryWriter5writeEPKvm
CStrings:
+ "@56@0:8Q16Q24Q32@\"NSObject<OS_dispatch_queue>\"40@?<v@?@\"NSData\">48"
+ "@56@0:8Q16Q24Q32@40@?48"
+ "initWithStreamSize:platformId:personalityId:queue:streamCallback:"
```
