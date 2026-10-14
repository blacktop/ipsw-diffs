## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-10110.3.0.0.0
-  __TEXT.__text: 0xcda5c
+10110.4.0.0.0
+  __TEXT.__text: 0xcdc00
   __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_stubs: 0x7b20
+  __TEXT.__objc_stubs: 0x7b40
   __TEXT.__init_offsets: 0x150c
-  __TEXT.__objc_methlist: 0x5558
+  __TEXT.__objc_methlist: 0x5560
   __TEXT.__const: 0x3e7e
-  __TEXT.__gcc_except_tab: 0xead8
+  __TEXT.__gcc_except_tab: 0xeb0c
   __TEXT.__cstring: 0xc1f1
   __TEXT.__oslogstring: 0x4caa
-  __TEXT.__objc_methname: 0x90a9
+  __TEXT.__objc_methname: 0x90eb
   __TEXT.__objc_classname: 0xbb0
-  __TEXT.__objc_methtype: 0x58b1
-  __TEXT.__unwind_info: 0x6b08
+  __TEXT.__objc_methtype: 0x590c
+  __TEXT.__unwind_info: 0x6b18
   __DATA_CONST.__const: 0x1dd8
   __DATA_CONST.__cfstring: 0x7760
   __DATA_CONST.__objc_classlist: 0x3c8

   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__auth_got: 0xca0
   __DATA_CONST.__got: 0x2c8
-  __DATA.__objc_const: 0x9eb0
-  __DATA.__objc_selrefs: 0x2440
+  __DATA.__objc_const: 0x9eb8
+  __DATA.__objc_selrefs: 0x2448
   __DATA.__objc_ivar: 0x730
   __DATA.__objc_data: 0x25d0
   __DATA.__data: 0x1610

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5285
-  Symbols:   7773
-  CStrings:  4203
+  Functions: 5288
+  Symbols:   7778
+  CStrings:  4206
 
Symbols:
+ GCC_except_table166
+ __ZN14SABinaryParser14parseRunHeaderEv
+ __ZN14SABinaryWriter5writeEPKvm
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_9
+ _objc_msgSend$initWithStreamSize:platformId:personalityId:queue:streamCallback:
Functions:
~ __ZN14SABinaryParser15parseInjExtDataEPFbPvRK21_SABinaryInjExtPacketPKhES7_PFbS0_RK20_SABinaryInjExtPointE : 416 -> 424
~ __ZN14SABinaryParser13parseRunFrameEPFbPvRK19_SABinaryInjExtDataEPFbS0_RK21_SABinaryInjExtPacketPKhESC_ : 184 -> 120
+ __ZN14SABinaryParser14parseRunHeaderEv
~ -[HSTSensingAlgs initWithConfig:queue:log:] : 2000 -> 2204
~ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_4 : 88 -> 104
~ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_5 : 136 -> 88
~ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_6 : 104 -> 136
~ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_7 : 112 -> 104
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_9
~ -[HSTSensingAlgs _handleResetRequest:] : 364 -> 368
~ __ZN14SABinaryWriter15initHostRequestEhtPKv : 240 -> 168
+ __ZN14SABinaryWriter5writeEPKvm
CStrings:
+ "10110.4"
+ "@56@0:8Q16Q24Q32@\"NSObject<OS_dispatch_queue>\"40@?<v@?@\"NSData\">48"
+ "@56@0:8Q16Q24Q32@40@?48"
+ "initWithStreamSize:platformId:personalityId:queue:streamCallback:"
- "10110.3"
```
