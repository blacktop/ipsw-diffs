## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`

```diff

-5680.0.0.0.0
-  __TEXT.__text: 0x24e46c
+5681.0.0.0.0
+  __TEXT.__text: 0x24f108
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x3744c
+  __TEXT.__objc_methlist: 0x37594
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x11cbd
-  __TEXT.__unwind_info: 0x4ea0
-  __TEXT.__objc_classname: 0x2687
-  __TEXT.__objc_methname: 0x55516
-  __TEXT.__objc_methtype: 0xcb67
-  __TEXT.__objc_stubs: 0x9040
-  __DATA_CONST.__got: 0x950
+  __TEXT.__cstring: 0x11cec
+  __TEXT.__unwind_info: 0x4ed0
+  __TEXT.__objc_classname: 0x2698
+  __TEXT.__objc_methname: 0x5569a
+  __TEXT.__objc_methtype: 0xcb83
+  __TEXT.__objc_stubs: 0x90a0
+  __DATA_CONST.__got: 0x958
   __DATA_CONST.__const: 0x72c8
-  __DATA_CONST.__objc_classlist: 0xb78
+  __DATA_CONST.__objc_classlist: 0xb80
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11440
-  __DATA_CONST.__objc_superrefs: 0xb78
+  __DATA_CONST.__objc_selrefs: 0x114a8
+  __DATA_CONST.__objc_superrefs: 0xb80
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__cfstring: 0x15f40
-  __AUTH_CONST.__objc_const: 0x4d520
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x3fe8
+  __AUTH_CONST.__cfstring: 0x15fa0
+  __AUTH_CONST.__objc_const: 0x4d6e8
+  __AUTH.__objc_data: 0x9b0
+  __DATA.__objc_ivar: 0x3ffc
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x6950
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18869
-  Symbols:   45645
-  CStrings:  17079
+  Functions: 18896
+  Symbols:   45714
+  CStrings:  17103
 
Symbols:
+ +[NTPBSmarterFetchRequest mutedTagIdsType]
+ -[NTPBSmarterFetchRequest addMutedTagIds:]
+ -[NTPBSmarterFetchRequest clearMutedTagIds]
+ -[NTPBSmarterFetchRequest mutedTagIdsAtIndex:]
+ -[NTPBSmarterFetchRequest mutedTagIdsCount]
+ -[NTPBSmarterFetchRequest mutedTagIds]
+ -[NTPBSmarterFetchRequest setMutedTagIds:]
+ -[NTPBTypedMessage .cxx_destruct]
+ -[NTPBTypedMessage ckRecord]
+ -[NTPBTypedMessage copyWithZone:]
+ -[NTPBTypedMessage description]
+ -[NTPBTypedMessage dictionaryRepresentation]
+ -[NTPBTypedMessage hasCkRecord]
+ -[NTPBTypedMessage hasSmarterFetchResponse]
+ -[NTPBTypedMessage hasType]
+ -[NTPBTypedMessage hash]
+ -[NTPBTypedMessage isEqual:]
+ -[NTPBTypedMessage mergeFrom:]
+ -[NTPBTypedMessage readFrom:]
+ -[NTPBTypedMessage setCkRecord:]
+ -[NTPBTypedMessage setHasType:]
+ -[NTPBTypedMessage setSmarterFetchResponse:]
+ -[NTPBTypedMessage setType:]
+ -[NTPBTypedMessage smarterFetchResponse]
+ -[NTPBTypedMessage type]
+ -[NTPBTypedMessage writeTo:]
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._mutedTagIds
+ OBJC_IVAR_$_NTPBTypedMessage._ckRecord
+ OBJC_IVAR_$_NTPBTypedMessage._has
+ OBJC_IVAR_$_NTPBTypedMessage._smarterFetchResponse
+ OBJC_IVAR_$_NTPBTypedMessage._type
+ _NTPBTypedMessageReadFrom
+ _OBJC_CLASS_$_NTPBTypedMessage
+ _OBJC_METACLASS_$_NTPBTypedMessage
+ __OBJC_$_INSTANCE_METHODS_NTPBTypedMessage
+ __OBJC_$_INSTANCE_VARIABLES_NTPBTypedMessage
+ __OBJC_$_PROP_LIST_NTPBTypedMessage
+ __OBJC_CLASS_PROTOCOLS_$_NTPBTypedMessage
+ __OBJC_CLASS_RO_$_NTPBTypedMessage
+ __OBJC_METACLASS_RO_$_NTPBTypedMessage
+ _objc_msgSend$addMutedTagIds:
+ _objc_msgSend$setCkRecord:
+ _objc_msgSend$setSmarterFetchResponse:
CStrings:
+ "'"
+ "@\"NTPBSmarterFetchResponse\""
+ "NTPBTypedMessage"
+ "T@\"NSMutableArray\",&,N,V_mutedTagIds"
+ "T@\"NTPBCKRecord\",&,N,V_ckRecord"
+ "T@\"NTPBSmarterFetchResponse\",&,N,V_smarterFetchResponse"
+ "_ckRecord"
+ "_mutedTagIds"
+ "_smarterFetchResponse"
+ "addMutedTagIds:"
+ "ckRecord"
+ "ck_record"
+ "clearMutedTagIds"
+ "hasCkRecord"
+ "hasSmarterFetchResponse"
+ "mutedTagIds"
+ "mutedTagIdsAtIndex:"
+ "mutedTagIdsCount"
+ "mutedTagIdsType"
+ "muted_tag_ids"
+ "setCkRecord:"
+ "setMutedTagIds:"
+ "setSmarterFetchResponse:"
+ "smarterFetchResponse"
+ "smarter_fetch_response"
- "&"

```
