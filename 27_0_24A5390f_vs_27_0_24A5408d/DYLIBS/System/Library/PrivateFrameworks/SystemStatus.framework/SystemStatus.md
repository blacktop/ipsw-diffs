## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-284.1.0.0.0
-  __TEXT.__text: 0x5970c
-  __TEXT.__objc_methlist: 0x84f0
+286.101.0.0.0
+  __TEXT.__text: 0x59774
+  __TEXT.__objc_methlist: 0x84f8
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x3f34
+  __TEXT.__cstring: 0x3f47
   __TEXT.__oslogstring: 0x14a3
   __TEXT.__gcc_except_tab: 0x42c
-  __TEXT.__unwind_info: 0x2238
+  __TEXT.__unwind_info: 0x2230
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19f8
+  __DATA_CONST.__const: 0x1a00
   __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fb8
+  __DATA_CONST.__objc_selrefs: 0x1fc0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x598
   __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x4860
-  __AUTH_CONST.__objc_const: 0xf578
+  __AUTH_CONST.__cfstring: 0x4880
+  __AUTH_CONST.__objc_const: 0xf598
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x5d4
+  __DATA.__objc_ivar: 0x5d8
   __DATA.__data: 0xd28
   __DATA.__common: 0x20
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3176
-  Symbols:   6350
-  CStrings:  768
+  Functions: 3177
+  Symbols:   6353
+  CStrings:  769
 
Symbols:
+ -[STDynamicActivityAttributionXPCClientHandle invalidateConnection]
+ _OBJC_IVAR_$_STDynamicActivityAttributionXPCClientHandle._connectionLock
+ _objc_msgSend$invalidateConnection
Functions:
~ -[STDynamicActivityAttributionXPCClientHandle currentAttributionsDidChange:] : 96 -> 140
~ -[STDynamicActivityAttributionXPCClientHandle initWithXPCConnection:serverHandle:] : 688 -> 692
~ ___82-[STDynamicActivityAttributionXPCClientHandle initWithXPCConnection:serverHandle:]_block_invoke : 128 -> 104
~ ___82-[STDynamicActivityAttributionXPCClientHandle initWithXPCConnection:serverHandle:]_block_invoke_2 : 128 -> 104
+ -[STDynamicActivityAttributionXPCClientHandle invalidateConnection]
CStrings:
+ "a"
+ "chargingImpossible"
- "A"
```
