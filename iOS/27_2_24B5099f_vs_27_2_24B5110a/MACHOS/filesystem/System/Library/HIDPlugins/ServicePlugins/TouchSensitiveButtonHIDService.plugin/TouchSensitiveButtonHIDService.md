## TouchSensitiveButtonHIDService

> `/System/Library/HIDPlugins/ServicePlugins/TouchSensitiveButtonHIDService.plugin/TouchSensitiveButtonHIDService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
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
-  __TEXT.__text: 0x2fa4
+10110.4.0.0.0
+  __TEXT.__text: 0x2ff0
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_stubs: 0x700
-  __TEXT.__objc_methlist: 0x470
+  __TEXT.__objc_methlist: 0x478
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x384
   __TEXT.__cstring: 0x34f
   __TEXT.__oslogstring: 0x4ef
-  __TEXT.__objc_methname: 0x979
+  __TEXT.__objc_methname: 0x9bb
   __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methtype: 0x5b8
-  __TEXT.__unwind_info: 0x210
+  __TEXT.__objc_methtype: 0x613
+  __TEXT.__unwind_info: 0x218
   __DATA_CONST.__const: 0x240
   __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x68
-  __DATA.__objc_const: 0x918
-  __DATA.__objc_selrefs: 0x320
+  __DATA.__objc_const: 0x920
+  __DATA.__objc_selrefs: 0x328
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 83
-  Symbols:   290
-  CStrings:  268
+  Functions: 84
+  Symbols:   291
+  CStrings:  271
 
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
