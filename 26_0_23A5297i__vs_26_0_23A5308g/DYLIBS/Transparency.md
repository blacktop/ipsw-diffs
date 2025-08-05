## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.0.28.0.0
-  __TEXT.__text: 0x49a20
+1547.0.38.0.0
+  __TEXT.__text: 0x49d0c
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x414c
-  __TEXT.__cstring: 0x26fe
+  __TEXT.__objc_methlist: 0x41b4
+  __TEXT.__cstring: 0x274e
   __TEXT.__const: 0x11b0
   __TEXT.__gcc_except_tab: 0x508
   __TEXT.__oslogstring: 0x1b91

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1960
+  __TEXT.__unwind_info: 0x1968
   __TEXT.__eh_frame: 0x4d0
-  __TEXT.__objc_classname: 0x6e3
-  __TEXT.__objc_methname: 0x7105
-  __TEXT.__objc_methtype: 0x1e25
-  __TEXT.__objc_stubs: 0x5660
+  __TEXT.__objc_classname: 0x6e4
+  __TEXT.__objc_methname: 0x7236
+  __TEXT.__objc_methtype: 0x1e3c
+  __TEXT.__objc_stubs: 0x5700
   __DATA_CONST.__got: 0x3e0
   __DATA_CONST.__const: 0x1520
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd0
+  __DATA_CONST.__objc_selrefs: 0x1d08
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x168
   __AUTH_CONST.__auth_got: 0x708
   __AUTH_CONST.__const: 0x27c0
-  __AUTH_CONST.__cfstring: 0x36e0
-  __AUTH_CONST.__objc_const: 0x6f90
+  __AUTH_CONST.__cfstring: 0x3760
+  __AUTH_CONST.__objc_const: 0x7020
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x218
   __AUTH.__data: 0x2f0
-  __DATA.__objc_ivar: 0x358
+  __DATA.__objc_ivar: 0x364
   __DATA.__data: 0x978
   __DATA.__bss: 0x2350
   __DATA_DIRTY.__objc_data: 0x12b8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 660AE45A-020C-31EB-81F5-7FA2D24B453F
-  Functions: 2426
-  Symbols:   6533
-  CStrings:  2670
+  UUID: C4DE6305-13B1-36C1-990C-212EDC3AE257
+  Functions: 2435
+  Symbols:   6559
+  CStrings:  2690
 
Symbols:
+ -[KTIDSIdentity initWithPushToken:ktLoggableData:signature:ktCapable:conditionalEnforcement:]
+ -[KTIDSIdentity setSupportConditionalEnforcement:]
+ -[KTIDSIdentity supportConditionalEnforcement]
+ -[KTLoggableData setSupportConditionalEnforcement:]
+ -[KTLoggableData supportConditionalEnforcement]
+ -[KTVerifierResult setValidUntil:]
+ -[KTVerifierResult validUntil]
+ -[TransparencyAnalytics ckManateeState]
+ -[TransparencyAnalytics setCKManateeState:]
+ _OBJC_IVAR_$_KTIDSIdentity._supportConditionalEnforcement
+ _OBJC_IVAR_$_KTLoggableData._supportConditionalEnforcement
+ _OBJC_IVAR_$_KTVerifierResult._validUntil
+ ___63-[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:]_block_invoke.50
+ ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.129
+ ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.133
+ _objc_msgSend$initWithPushToken:ktLoggableData:signature:ktCapable:conditionalEnforcement:
+ _objc_msgSend$setSupportConditionalEnforcement:
+ _objc_msgSend$setValidUntil:
+ _objc_msgSend$supportConditionalEnforcement
+ _objc_msgSend$validUntil
- ___63-[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:]_block_invoke.38
- ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.126
- ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.130
CStrings:
+ " expirationTime: %@"
+ "@48@0:8@16@24@32B40B44"
+ "CKManateeState"
+ "T@\"NSDate\",&,V_validUntil"
+ "TB,V_supportConditionalEnforcement"
+ "_supportConditionalEnforcement"
+ "_validUntil"
+ "ckManateeState"
+ "conditionalEnforcement"
+ "initWithPushToken:ktLoggableData:signature:ktCapable:conditionalEnforcement:"
+ "setCKManateeState:"
+ "setSupportConditionalEnforcement:"
+ "setValidUntil:"
+ "supportConditionalEnforcement"
+ "validUntil"

```
