## HomeKitDaemonShared

> `/System/Library/PrivateFrameworks/HomeKitDaemonShared.framework/HomeKitDaemonShared`

```diff

-1418.5.15.0.0
-  __TEXT.__text: 0x9bfc
+1418.6.12.0.0
+  __TEXT.__text: 0x9c78
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0xac4
+  __TEXT.__objc_methlist: 0xaec
   __TEXT.__const: 0x2a8
   __TEXT.__constg_swiftt: 0x84
   __TEXT.__swift5_typeref: 0x71

   __TEXT.__unwind_info: 0x290
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x1cb
-  __TEXT.__objc_methname: 0x1d67
-  __TEXT.__objc_methtype: 0x639
+  __TEXT.__objc_methname: 0x1e36
+  __TEXT.__objc_methtype: 0x65a
   __TEXT.__objc_stubs: 0x1500
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x318

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_selrefs: 0x6f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x130
   __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x15f0
+  __AUTH_CONST.__objc_const: 0x1678
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x240
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x518
   __DATA.__bss: 0x490
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8A28FB80-89BA-3F75-A546-5FE7B60B0A01
-  Functions: 236
-  Symbols:   871
-  CStrings:  551
+  UUID: 602A6D9F-16AC-3850-8805-7303299AABBF
+  Functions: 238
+  Symbols:   876
+  CStrings:  557
 
Symbols:
+ -[HMDStatusChannelRecord deserializedPayloadModel]
+ -[HMDStatusChannelRecord initWithIdsIdentifier:idsDestination:deserializedPayloadModel:assertionTime:]
+ _OBJC_IVAR_$_HMDStatusChannelRecord._deserializedPayloadModel
+ ___52-[HMDStatusChannel _setInvitedUsers:withCompletion:]_block_invoke.118
+ ___block_literal_global.121
+ ___block_literal_global.125
+ ___block_literal_global.128
+ ___block_literal_global.92
- ___52-[HMDStatusChannel _setInvitedUsers:withCompletion:]_block_invoke.112
- ___block_literal_global.115
- ___block_literal_global.119
- ___block_literal_global.122
- ___block_literal_global.86
Functions:
~ -[HMDStatusChannelRecord .cxx_destruct] : 92 -> 104
+ -[HMDStatusChannelRecord idsIdentifier]
~ -[HMDStatusChannelRecord isEqual:] : 428 -> 408
+ -[HMDStatusChannelRecord initWithIdsIdentifier:idsDestination:deserializedPayloadModel:assertionTime:]
CStrings:
+ "@\"<HMDPresencePayloadContainer>\""
+ "T@\"<HMDPresencePayloadContainer>\",R,N,V_deserializedPayloadModel"
+ "_deserializedPayloadModel"
+ "accessoryUUID"
+ "deserializedPayloadModel"
+ "initWithIdsIdentifier:idsDestination:deserializedPayloadModel:assertionTime:"

```
