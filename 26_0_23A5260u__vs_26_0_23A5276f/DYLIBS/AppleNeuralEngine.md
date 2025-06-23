## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

```diff

-380.7.0.0.0
-  __TEXT.__text: 0x44924
+380.9.0.0.0
+  __TEXT.__text: 0x44a7c
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_methlist: 0x2614
   __TEXT.__const: 0x288
-  __TEXT.__oslogstring: 0x80c0
+  __TEXT.__oslogstring: 0x80f8
   __TEXT.__cstring: 0x2d9d
-  __TEXT.__gcc_except_tab: 0x5250
+  __TEXT.__gcc_except_tab: 0x5280
   __TEXT.__unwind_info: 0x1128
   __TEXT.__objc_classname: 0x2ef
   __TEXT.__objc_methname: 0x5fb2
   __TEXT.__objc_methtype: 0x24a8
-  __TEXT.__objc_stubs: 0x4400
+  __TEXT.__objc_stubs: 0x4420
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0x110

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: D062BD17-E0CA-3E8C-AAB9-0CFB3B2DEB80
-  Functions: 1413
-  Symbols:   4632
-  CStrings:  2645
+  UUID: 2D695360-E9A7-384E-9F56-9030E9F18C6F
+  Functions: 1414
+  Symbols:   4635
+  CStrings:  2646
 
Symbols:
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.18
+ _objc_msgSend$baseModelIdentifierNotFoundForNewInstanceMethod:
Functions:
~ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:] : 7052 -> 7304
~ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.16 : 68 -> 92
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.17
CStrings:
+ "%@: modelIdentifier(%@) : missing base model identifier"

```
