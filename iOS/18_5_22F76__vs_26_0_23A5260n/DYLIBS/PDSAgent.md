## PDSAgent

> `/System/Library/PrivateFrameworks/PDSAgent.framework/PDSAgent`

```diff

-1926.600.41.0.0
-  __TEXT.__text: 0x1aff8
+1956.100.4.0.0
+  __TEXT.__text: 0x1b478
   __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_methlist: 0x23b4
   __TEXT.__const: 0xa0

   __TEXT.__oslogstring: 0xcd1
   __TEXT.__unwind_info: 0x758
   __TEXT.__objc_classname: 0x393
-  __TEXT.__objc_methname: 0x4631
+  __TEXT.__objc_methname: 0x466a
   __TEXT.__objc_methtype: 0x1010
-  __TEXT.__objc_stubs: 0x3aa0
-  __DATA_CONST.__got: 0x308
+  __TEXT.__objc_stubs: 0x3b40
+  __DATA_CONST.__got: 0x2e8
   __DATA_CONST.__const: 0x610
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1448
+  __DATA_CONST.__objc_selrefs: 0x1470
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x318

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C34E718E-C27B-3EF0-907D-624B16DC4ADC
+  UUID: 533050F5-3024-3E0B-809A-282526B94562
   Functions: 733
-  Symbols:   2707
-  CStrings:  1509
+  Symbols:   2704
+  CStrings:  1514
 
Symbols:
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
Functions:
~ _PDSProtoUserAuthReadFrom : 612 -> 760
~ _PDSProtoUserPushTokenReadFrom : 544 -> 596
~ _PDSProtoTopicReadFrom : 532 -> 584
~ _PDSProtoMapEntryReadFrom : 436 -> 488
~ _PDSProtoBatchRegisterReqReadFrom : 644 -> 780
~ _PDSProtoGSTokenAuthReadFrom : 392 -> 444
~ _PDSProtoBatchRegisterRespReadFrom : 1188 -> 1576
~ _PDSProtoUserPushTokenRegRequestReadFrom : 812 -> 948
~ _PDSProtoUserPushTokenRegResponseReadFrom : 676 -> 812
CStrings:
+ "_setError"
+ "getBytes:range:"
+ "hasError"
+ "position"
+ "setPosition:"

```
