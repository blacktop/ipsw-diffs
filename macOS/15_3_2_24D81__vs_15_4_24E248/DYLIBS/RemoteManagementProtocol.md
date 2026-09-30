## RemoteManagementProtocol

> `/System/Library/PrivateFrameworks/RemoteManagementProtocol.framework/Versions/A/RemoteManagementProtocol`

```diff

-502.2.7.0.0
-  __TEXT.__text: 0x6338
-  __TEXT.__auth_stubs: 0xc0
+560.4.11.0.0
+  __TEXT.__text: 0x62d8
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_methlist: 0xb80
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x909
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x28a
   __TEXT.__objc_methname: 0x19a1
   __TEXT.__objc_methtype: 0x148

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x68
+  __AUTH_CONST.__auth_got: 0x70
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xd60
   __AUTH_CONST.__objc_const: 0x1658

   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/Versions/A/RemoteManagementModel
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B43B4043-307B-3CAC-8C81-8CC096A6C5B9
+  UUID: 9CB45615-E44F-3ACB-B495-089AF20E82EB
   Functions: 234
-  Symbols:   635
+  Symbols:   636
   CStrings:  489
 
Symbols:
+ _objc_retainAutoreleaseReturnValue
Functions:
~ -[RMProtocolCommandRequest loadFromDictionary:serializationType:error:] : 324 -> 308
~ -[RMProtocolCommandRequest_StatusReason loadFromDictionary:serializationType:error:] : 580 -> 576
~ -[RMProtocolDeclarationItemsResponse_Declarations loadFromDictionary:serializationType:error:] : 700 -> 684
~ -[RMProtocolEnrollResponse loadFromDictionary:serializationType:error:] : 232 -> 228
~ ___46-[RMProtocolEnrollResponse serializeWithType:]_block_invoke : 44 -> 8
~ -[RMProtocolErrorResponse loadFromDictionary:serializationType:error:] : 252 -> 240
~ -[RMProtocolStatusReport loadFromDictionary:serializationType:error:] : 272 -> 268
~ -[RMProtocolStatusReport_StatusReason loadFromDictionary:serializationType:error:] : 580 -> 576

```
