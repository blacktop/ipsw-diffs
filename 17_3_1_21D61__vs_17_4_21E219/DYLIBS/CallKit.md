## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1228.400.1.0.0
-  __TEXT.__text: 0x619bc
+1228.500.151.2.2
+  __TEXT.__text: 0x61c94
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x75d8
+  __TEXT.__objc_methlist: 0x7610
   __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0x588
-  __TEXT.__cstring: 0x58fd
+  __TEXT.__cstring: 0x5970
   __TEXT.__oslogstring: 0x3105
-  __TEXT.__unwind_info: 0x1c24
+  __TEXT.__unwind_info: 0x1c2c
   __TEXT.__objc_classname: 0x13b2
-  __TEXT.__objc_methname: 0xfe4a
+  __TEXT.__objc_methname: 0xff34
   __TEXT.__objc_methtype: 0x3982
-  __TEXT.__objc_stubs: 0x9a20
+  __TEXT.__objc_stubs: 0x9aa0
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0xc58
   __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xbe68
-  __DATA_CONST.__objc_selrefs: 0x2dc8
+  __DATA_CONST.__objc_const: 0xbe60
+  __DATA_CONST.__objc_selrefs: 0x2df8
+  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_classrefs: 0x440
+  __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x38a0
+  __AUTH_CONST.__cfstring: 0x3900
   __AUTH_CONST.__objc_const: 0x34b0
   __AUTH_CONST.__const: 0x520
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH.__objc_data: 0x1720
-  __DATA.__objc_protorefs: 0xb8
-  __DATA.__objc_classrefs: 0x440
-  __DATA.__objc_superrefs: 0x348
-  __DATA.__objc_ivar: 0x824
+  __DATA.__objc_ivar: 0x828
   __DATA.__data: 0x17b8
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6DBC8CCC-C786-397F-9BB4-9C1D2F28D192
-  Functions: 3008
-  Symbols:   9561
-  CStrings:  4236
+  UUID: 4055BA67-162F-3A36-A410-7EC847F8ABAD
+  Functions: 3013
+  Symbols:   9576
+  CStrings:  4254
 
Symbols:
+ -[CXProviderConfiguration setSupportsDynamicSystemUI:]
+ -[CXProviderConfiguration supportsDynamicSystemUI]
+ -[CXStartCallAction handles]
+ -[CXStartCallAction initWithCallUUID:handles:]
+ -[CXStartCallAction setHandles:]
+ _OBJC_IVAR_$_CXProviderConfiguration._supportsDynamicSystemUI
+ _OBJC_IVAR_$_CXStartCallAction._handles
+ __OBJC_$_PROP_LIST_CXAbstractProvider.116
+ ___132-[CXChannelProvider reportIncomingTransmissionStartedForChannelWithUUID:update:shouldReplaceOutgoingTransmission:completionHandler:]_block_invoke.136
+ ___49-[CXChannelProvider registerCurrentConfiguration]_block_invoke.149
+ ___59-[CXChannelProvider reportChannelWithUUID:connectedAtDate:]_block_invoke.117
+ ___62-[CXAbstractProviderSource actionCompleted:completionHandler:]_block_invoke.60
+ ___62-[CXProvider reportNewIncomingCallWithUUID:update:completion:]_block_invoke.154
+ ___65-[CXAbstractProviderSource requestTransaction:completionHandler:]_block_invoke.67
+ ___69-[CXChannelProvider reportChannelWithUUID:updated:completionHandler:]_block_invoke.129
+ ___81-[CXChannelProvider reportChannelWithUUID:disconnectedAtDate:disconnectedReason:]_block_invoke.122
+ ___96-[CXChannelProvider reportIncomingTransmissionEndedForChannelWithUUID:reason:completionHandler:]_block_invoke.131
+ ___block_literal_global.120
+ ___block_literal_global.124
+ ___block_literal_global.151
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$handles
+ _objc_msgSend$setHandles:
+ _objc_msgSend$setSupportsDynamicSystemUI:
+ _objc_msgSend$supportsDynamicSystemUI
- _OBJC_IVAR_$_CXStartCallAction._handle
- __OBJC_$_PROP_LIST_CXAbstractProvider.115
- ___132-[CXChannelProvider reportIncomingTransmissionStartedForChannelWithUUID:update:shouldReplaceOutgoingTransmission:completionHandler:]_block_invoke.134
- ___49-[CXChannelProvider registerCurrentConfiguration]_block_invoke.148
- ___59-[CXChannelProvider reportChannelWithUUID:connectedAtDate:]_block_invoke.116
- ___62-[CXAbstractProviderSource actionCompleted:completionHandler:]_block_invoke.58
- ___62-[CXProvider reportNewIncomingCallWithUUID:update:completion:]_block_invoke.153
- ___65-[CXAbstractProviderSource requestTransaction:completionHandler:]_block_invoke.65
- ___69-[CXChannelProvider reportChannelWithUUID:updated:completionHandler:]_block_invoke.127
- ___81-[CXChannelProvider reportChannelWithUUID:disconnectedAtDate:disconnectedReason:]_block_invoke.121
- ___96-[CXChannelProvider reportIncomingTransmissionEndedForChannelWithUUID:reason:completionHandler:]_block_invoke.129
- ___block_literal_global.119
- ___block_literal_global.123
- ___block_literal_global.150
- _objc_msgSend$setHandle:
CStrings:
+ "\x12\x12"
+ " handles=%@"
+ " supportsDynamicSystemUI=%d"
+ "%s: array '%@' cannot be empty"
+ "-[CXStartCallAction initWithCallUUID:handles:]"
+ "T@\"CXHandle\",C,N"
+ "T@\"NSArray\",C,N,V_handles"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_supportsDynamicSystemUI"
+ "_handles"
+ "_supportsDynamicSystemUI"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "handles"
+ "initWithCallUUID:handles:"
+ "setHandles:"
+ "setSupportsDynamicSystemUI:"
+ "supportsDynamicSystemUI"
- "\x13\x11"
- " handle=%@"
- "T@\"CXHandle\",C,N,V_handle"

```
