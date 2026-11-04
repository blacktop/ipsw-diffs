## RemoteTextInput

> `/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput`

```diff

-180.0.0.0.0
-  __TEXT.__text: 0x203b4
-  __TEXT.__objc_methlist: 0x2bc4
+180.2.1.0.0
+  __TEXT.__text: 0x20928
+  __TEXT.__objc_methlist: 0x2c44
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x3028
+  __TEXT.__cstring: 0x3048
   __TEXT.__oslogstring: 0xccc
   __TEXT.__gcc_except_tab: 0x29c
   __TEXT.__dlopen_cstrs: 0xf6
-  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__unwind_info: 0xbd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1988
+  __DATA_CONST.__objc_selrefs: 0x19d8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x260
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x2e20
-  __AUTH_CONST.__objc_const: 0x6968
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__cfstring: 0x2e60
+  __AUTH_CONST.__objc_const: 0x6a48
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x330
+  __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x480
   __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1023
-  Symbols:   1848
-  CStrings:  525
+  Functions: 1039
+  Symbols:   1873
+  CStrings:  528
 
Symbols:
+ -[RTIDocumentState acknowledgedSourceRevision]
+ -[RTIDocumentState documentStateByStrippingTextContent]
+ -[RTIDocumentState setAcknowledgedSourceRevision:]
+ -[RTIInputSystemClient _acknowledgeSourceRevisionOnDocumentState:]
+ -[RTIInputSystemClient _recordSeenSourceRevision:]
+ -[RTIInputSystemSession init]
+ -[RTIInputSystemSession shouldAcceptTextFromClientDocumentState:]
+ -[RTIInputSystemSession stampOutgoingTextOperations:]
+ -[RTITextOperations setSourceRevision:]
+ -[RTITextOperations sourceRevision]
+ GCC_except_table108
+ GCC_except_table24
+ GCC_except_table42
+ _OBJC_IVAR_$_RTIDocumentState._acknowledgedSourceRevision
+ _OBJC_IVAR_$_RTIInputSystemClient._lastSeenSourceRevision
+ _OBJC_IVAR_$_RTIInputSystemClient._lastSeenSourceRevisionLock
+ _OBJC_IVAR_$_RTIInputSystemSession._lastSentSourceRevision
+ _OBJC_IVAR_$_RTIInputSystemSession._lastSentSourceRevisionLock
+ _OBJC_IVAR_$_RTITextOperations._sourceRevision
+ _RTIClientHasSeenSourceRevision
+ _RTINextSourceRevision
+ _RTISourceRevisionEpoch
+ _RTISourceRevisionEpoch.epoch
+ _RTISourceRevisionEpoch.onceToken
+ ___RTISourceRevisionEpoch_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56s_e41_v16?0"<RTIInputSystemSessionProtocol>"8ls32l8s40l8s48l8s56l8
+ __rtiSourceRevisionCounter
+ __rtiSourceRevisionLock
+ _arc4random
- GCC_except_table104
- GCC_except_table41
- GCC_except_table47
- ___block_descriptor_56_e8_32s40s48s_e41_v16?0"<RTIInputSystemSessionProtocol>"8ls32l8s40l8s48l8
CStrings:
+ "&"
+ "ackSourceRev"
+ "sourceRevision"
+ "{"
+ "\x81"
- ")"
- "["
```
