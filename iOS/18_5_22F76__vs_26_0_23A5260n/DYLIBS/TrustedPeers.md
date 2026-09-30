## TrustedPeers

> `/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers`

```diff

-61439.122.1.0.0
-  __TEXT.__text: 0x2f1e4
+61901.0.9.0.1
+  __TEXT.__text: 0x30df4
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x36ac
+  __TEXT.__objc_methlist: 0x3814
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0xa04
-  __TEXT.__cstring: 0xcc7
-  __TEXT.__oslogstring: 0x18f1
-  __TEXT.__unwind_info: 0xb48
-  __TEXT.__objc_classname: 0x4f8
-  __TEXT.__objc_methname: 0x64c6
-  __TEXT.__objc_methtype: 0xcfd
-  __TEXT.__objc_stubs: 0x4360
-  __DATA_CONST.__got: 0x258
+  __TEXT.__gcc_except_tab: 0xa10
+  __TEXT.__cstring: 0xd17
+  __TEXT.__oslogstring: 0x1941
+  __TEXT.__unwind_info: 0xb70
+  __TEXT.__objc_classname: 0x510
+  __TEXT.__objc_methname: 0x6704
+  __TEXT.__objc_methtype: 0xd14
+  __TEXT.__objc_stubs: 0x4560
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x650
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17f8
-  __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__objc_selrefs: 0x18a8
+  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x4ce8
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__objc_const: 0x4e60
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x2d8
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x2e4
   __DATA.__data: 0x2c0
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5E36E92-92B7-3CBA-B44B-A97036D8F342
-  Functions: 1177
-  Symbols:   3696
-  CStrings:  1823
+  UUID: 81E26D13-9864-3F17-8EC9-4703AE3D6CA2
+  Functions: 1207
+  Symbols:   3778
+  CStrings:  1867
 
Symbols:
+ +[TPModel ignoreTDLForModel:]
+ +[TPModel isFullPeer:]
+ +[TPPBPeerDynamicInfo positivelyExcludedType]
+ -[TPModel trustedFullPeerCountWithError:]
+ -[TPModel trustedPeers:]
+ -[TPPBPeerDynamicInfo addPositivelyExcluded:]
+ -[TPPBPeerDynamicInfo clearPositivelyExcludeds]
+ -[TPPBPeerDynamicInfo positivelyExcludedAtIndex:]
+ -[TPPBPeerDynamicInfo positivelyExcludedsCount]
+ -[TPPBPeerDynamicInfo positivelyExcludeds]
+ -[TPPBPeerDynamicInfo setPositivelyExcludeds:]
+ -[TPPBPeerDynamicInfoPeer .cxx_destruct]
+ -[TPPBPeerDynamicInfoPeer copyTo:]
+ -[TPPBPeerDynamicInfoPeer copyWithZone:]
+ -[TPPBPeerDynamicInfoPeer description]
+ -[TPPBPeerDynamicInfoPeer dictionaryRepresentation]
+ -[TPPBPeerDynamicInfoPeer hasPeerID]
+ -[TPPBPeerDynamicInfoPeer hash]
+ -[TPPBPeerDynamicInfoPeer isEqual:]
+ -[TPPBPeerDynamicInfoPeer mergeFrom:]
+ -[TPPBPeerDynamicInfoPeer peerID]
+ -[TPPBPeerDynamicInfoPeer readFrom:]
+ -[TPPBPeerDynamicInfoPeer setPeerID:]
+ -[TPPBPeerDynamicInfoPeer writeTo:]
+ -[TPPBPeerStableInfo hasSupportsRepudiation]
+ -[TPPBPeerStableInfo setHasSupportsRepudiation:]
+ -[TPPBPeerStableInfo setSupportsRepudiation:]
+ -[TPPBPeerStableInfo supportsRepudiation]
+ -[TPPeerStableInfo supportsRepudiation]
+ GCC_except_table1158
+ GCC_except_table1166
+ GCC_except_table144
+ GCC_except_table156
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table173
+ GCC_except_table176
+ GCC_except_table184
+ GCC_except_table190
+ GCC_except_table198
+ GCC_except_table205
+ GCC_except_table211
+ GCC_except_table220
+ GCC_except_table225
+ GCC_except_table296
+ OBJC_IVAR_$_TPPBPeerDynamicInfo._positivelyExcludeds
+ OBJC_IVAR_$_TPPBPeerDynamicInfoPeer._peerID
+ OBJC_IVAR_$_TPPBPeerStableInfo._supportsRepudiation
+ _OBJC_CLASS_$_TPPBPeerDynamicInfoPeer
+ _OBJC_METACLASS_$_TPPBPeerDynamicInfoPeer
+ _TPPBPeerDynamicInfoPeerReadFrom
+ __OBJC_$_INSTANCE_METHODS_TPPBPeerDynamicInfoPeer
+ __OBJC_$_INSTANCE_VARIABLES_TPPBPeerDynamicInfoPeer
+ __OBJC_$_PROP_LIST_TPPBPeerDynamicInfoPeer
+ __OBJC_CLASS_PROTOCOLS_$_TPPBPeerDynamicInfoPeer
+ __OBJC_CLASS_RO_$_TPPBPeerDynamicInfoPeer
+ __OBJC_METACLASS_RO_$_TPPBPeerDynamicInfoPeer
+ ___24-[TPModel trustedPeers:]_block_invoke
+ ___Block_byref_object_copy_.3044
+ ___Block_byref_object_dispose_.3045
+ ___block_literal_global.1207
+ ___block_literal_global.1399
+ ___block_literal_global.150
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.3053
+ _objc_msgSend$_setError
+ _objc_msgSend$addPositivelyExcluded:
+ _objc_msgSend$clearPositivelyExcludeds
+ _objc_msgSend$distrustedEgoSponsoredBeneficiaryIDs:
+ _objc_msgSend$egoSponsoredBeneficiaryIDs:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$ignoreTDLForModel:
+ _objc_msgSend$isFullPeer:
+ _objc_msgSend$position
+ _objc_msgSend$positivelyExcludedAtIndex:
+ _objc_msgSend$positivelyExcludedsCount
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setSupportsRepudiation:
+ _objc_msgSend$supportsRepudiation
+ _objc_msgSend$trustedPeers:
- GCC_except_table1128
- GCC_except_table1136
- GCC_except_table140
- GCC_except_table154
- GCC_except_table159
- GCC_except_table162
- GCC_except_table171
- GCC_except_table174
- GCC_except_table182
- GCC_except_table188
- GCC_except_table192
- GCC_except_table201
- GCC_except_table207
- GCC_except_table218
- GCC_except_table221
- GCC_except_table292
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___37-[TPModel trustedPeerCountWithError:]_block_invoke
- ___Block_byref_object_copy_.2987
- ___Block_byref_object_dispose_.2988
- ___block_literal_global.1210
- ___block_literal_global.129
- ___block_literal_global.133
- ___block_literal_global.135
- ___block_literal_global.1402
- ___block_literal_global.2996
CStrings:
+ "After retaining sponsored beneficiary IDs in excluded list: excluded:%{public}@"
+ "Mac"
+ "RealityDevice"
+ "T@\"NSMutableArray\",&,N,V_positivelyExcludeds"
+ "TB,N,V_supportsRepudiation"
+ "TPPBPeerDynamicInfoPeer"
+ "Watch"
+ "_positivelyExcludeds"
+ "_setError"
+ "_supportsRepudiation"
+ "addPositivelyExcluded:"
+ "clearPositivelyExcludeds"
+ "distrustedEgoSponsoredBeneficiaryIDs:"
+ "egoSponsoredBeneficiaryIDs:"
+ "getBytes:range:"
+ "hasError"
+ "hasSupportsRepudiation"
+ "iPad"
+ "iPhone"
+ "iPod"
+ "ignoreTDLForModel:"
+ "isFullPeer:"
+ "position"
+ "positivelyExcluded"
+ "positivelyExcludedAtIndex:"
+ "positivelyExcludedType"
+ "positivelyExcludeds"
+ "positivelyExcludedsCount"
+ "setHasSupportsRepudiation:"
+ "setPosition:"
+ "setPositivelyExcludeds:"
+ "setSupportsRepudiation:"
+ "supportsRepudiation"
+ "trustedFullPeerCountWithError:"
+ "trustedPeers:"
+ "{?=\"clock\"b1\"flexiblePolicyVersion\"b1\"frozenPolicyVersion\"b1\"userControllableViewStatus\"b1\"isInheritedAccount\"b1\"supportsRepudiation\"b1}"
- "{?=\"clock\"b1\"flexiblePolicyVersion\"b1\"frozenPolicyVersion\"b1\"userControllableViewStatus\"b1\"isInheritedAccount\"b1}"

```
