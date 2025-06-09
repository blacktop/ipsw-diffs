## ASIOKit

> `/System/Library/Extensions/ASIOKit.kext/ASIOKit`

```diff

-12.83.0.0.0
-  __TEXT.__cstring: 0x239
-  __TEXT.__const: 0x7c20
-  __TEXT_EXEC.__text: 0x48f18
-  __TEXT_EXEC.__auth_stubs: 0x1d0
+13.19.0.0.0
+  __TEXT.__cstring: 0x261
+  __TEXT.__const: 0x7810
+  __TEXT_EXEC.__text: 0x424ac
+  __TEXT_EXEC.__auth_stubs: 0x210
   __DATA.__data: 0xd8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x38a8
+  __DATA_CONST.__const: 0x3900
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 36DB3590-84FE-3136-88E0-285AD96822A4
-  Functions: 95
-  Symbols:   651
-  CStrings:  16
+  UUID: C8E74AFF-6693-3659-8651-D6C9F8052631
+  Functions: 96
+  Symbols:   682
+  CStrings:  18
 
Symbols:
+ __ZN17ASIOKitUserClient20getKernelInfoSignalsEP14_ASInputBufferP15_ASOutputBuffer
+ __ZN17ASIOKitUserClient21sGetKernelInfoSignalsEP8OSObjectPvP25IOExternalMethodArguments
+ __ZN18IOAccessoryManager9metaClassE
+ __ZN20IOPortTransportState9metaClassE
+ __ZN7ASIOKit27asiokitGetKernelInfoSignalsEP14_ASInputBufferP15_ASOutputBuffer
+ __ZN7ASIOKit32asiokitGetKernelInfoSignalsGatedEP14_ASInputBufferP15_ASOutputBuffer
+ __ZN7ASIOKit33asiokitGetKernelInfoIOPortSignalsEP14_ASInputBufferP15_ASOutputBuffer
+ __ZNK18IOAccessoryManager17getUSBConnectTypeEv
+ __ZNK20IOPortTransportState16getTransportTypeEv
+ __ZNK6IOPort11getPortTypeEv
+ __ZNK6IOPort28getConnectionActiveDurationSEv
CStrings:
+ "IOAccessoryManager"
+ "IOPortTransportState"

```
