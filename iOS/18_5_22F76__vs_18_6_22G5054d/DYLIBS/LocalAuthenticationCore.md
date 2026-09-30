## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0xce2b4
+1656.140.3.0.0
+  __TEXT.__text: 0xce414
   __TEXT.__auth_stubs: 0x2020
-  __TEXT.__objc_methlist: 0x7cc8
-  __TEXT.__const: 0x3c04
+  __TEXT.__objc_methlist: 0x7cd8
+  __TEXT.__const: 0x3f44
   __TEXT.__cstring: 0xb14b
   __TEXT.__oslogstring: 0x5029
   __TEXT.__gcc_except_tab: 0x1468

   __TEXT.__unwind_info: 0x3960
   __TEXT.__eh_frame: 0x20e8
   __TEXT.__objc_classname: 0x1dbc
-  __TEXT.__objc_methname: 0xc923
+  __TEXT.__objc_methname: 0xc93b
   __TEXT.__objc_methtype: 0x36bf
-  __TEXT.__objc_stubs: 0x8de0
+  __TEXT.__objc_stubs: 0x8e00
   __DATA_CONST.__got: 0x8d8
   __DATA_CONST.__const: 0x3f98
   __DATA_CONST.__objc_classlist: 0x710
   __DATA_CONST.__objc_protolist: 0x530
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3030
-  __DATA_CONST.__objc_protorefs: 0x208
+  __DATA_CONST.__objc_selrefs: 0x3038
+  __DATA_CONST.__objc_protorefs: 0x210
   __DATA_CONST.__objc_superrefs: 0x450
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x1020
   __AUTH_CONST.__const: 0x3118
   __AUTH_CONST.__cfstring: 0x5600
-  __AUTH_CONST.__objc_const: 0x31300
+  __AUTH_CONST.__objc_const: 0x31340
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0x188
   __DATA.__objc_ivar: 0x73c
-  __DATA.__data: 0x42f8
+  __DATA.__data: 0x3f78
   __DATA.__bss: 0x1fa9
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x4410
-  __DATA_DIRTY.__data: 0xcd8
+  __DATA_DIRTY.__data: 0xcf8
   __DATA_DIRTY.__bss: 0x158
   __DATA_DIRTY.__common: 0x78
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B9474D97-4583-3234-975D-883D15B847EF
-  Functions: 5266
-  Symbols:   18651
-  CStrings:  5630
+  UUID: F4AC84D8-7E01-3AD8-BF59-962AA38E8131
+  Functions: 5267
+  Symbols:   18658
+  CStrings:  5631
 
Symbols:
+ +[LACXPCInterface interfaceForEnvironment]
+ __OBJC_PROTOCOL_REFERENCE_$_LACEnvironmentServiceXPC
+ ___block_descriptor_48_e8_32bs40w_e40_v24?0"<LACAgentProxyXPC>"8"NSError"16ls32l8w40l8
+ _objc_msgSend$interfaceForEnvironment
- ___block_descriptor_48_e8_32bs40w_e40_v24?0"<LACAgentProxyXPC>"8"NSError"16lw40l8s32l8
Functions:
~ +[LACXPCInterface interfaceForXPCProtocol:] : 272 -> 304
+ +[LACXPCInterface interfaceForEnvironment]
~ ___39-[LACAgentProxyXPCWrapper _agentProxy:]_block_invoke.2 : 208 -> 212
CStrings:
+ "interfaceForEnvironment"

```
