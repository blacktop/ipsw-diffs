## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-61901.120.36.0.3
-  __TEXT.__text: 0x2a43c
+61901.120.56.0.1
+  __TEXT.__text: 0x2a9ac
   __TEXT.__auth_stubs: 0xfe0
   __TEXT.__delay_helper: 0x1bc
-  __TEXT.__objc_methlist: 0x1e24
-  __TEXT.__const: 0xd8
+  __TEXT.__objc_methlist: 0x1e2c
+  __TEXT.__const: 0xe0
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__gcc_except_tab: 0x1618
-  __TEXT.__cstring: 0x330e
-  __TEXT.__oslogstring: 0x3a20
+  __TEXT.__gcc_except_tab: 0x161c
+  __TEXT.__cstring: 0x3357
+  __TEXT.__oslogstring: 0x3abd
   __TEXT.__ustring: 0x32
   __TEXT.__unwind_info: 0x928
   __TEXT.__objc_classname: 0x2e6
-  __TEXT.__objc_methname: 0x4281
+  __TEXT.__objc_methname: 0x42a4
   __TEXT.__objc_methtype: 0xf65
   __TEXT.__objc_stubs: 0x3080
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x11c0
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0x11c8
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1070
+  __DATA_CONST.__objc_selrefs: 0x1078
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x800
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x3720
+  __AUTH_CONST.__cfstring: 0x3780
   __AUTH_CONST.__objc_const: 0x2c10
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x5a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4B0A7C0-FDB3-3DD2-A086-4587B28A33DB
-  Functions: 778
-  Symbols:   2966
-  CStrings:  2123
+  UUID: CAB2CDD6-164F-33FF-8177-EFDB0AF6B03C
+  Functions: 779
+  Symbols:   2972
+  CStrings:  2130
 
Symbols:
+ -[KCPairingChannel populateKeychainWithEscrowIdentity]
+ GCC_except_table101
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table173
+ GCC_except_table178
+ GCC_except_table180
+ GCC_except_table182
+ GCC_except_table184
+ GCC_except_table190
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table384
+ GCC_except_table392
+ GCC_except_table530
+ GCC_except_table540
+ GCC_except_table542
+ ___Block_byref_object_copy_.390
+ ___Block_byref_object_copy_.933
+ ___Block_byref_object_dispose_.391
+ ___Block_byref_object_dispose_.934
+ ___block_descriptor_tmp.1500
+ ___block_descriptor_tmp.1564
+ ___block_descriptor_tmp.1606
+ ___block_descriptor_tmp.1639
+ ___block_descriptor_tmp.71.1558
+ ___block_literal_global.1159
+ ___block_literal_global.1463
+ ___block_literal_global.1528
+ ___block_literal_global.1604
+ ___block_literal_global.432
+ _apply_block_1.1507
+ _apply_block_2.1538
+ _kSecAttrCreationDate
+ _kSecAttrLabel
+ _kSecAttrUUID
+ _kSecurityRTCEventNameEscrowRepairGenerateRecord
- GCC_except_table100
- GCC_except_table111
- GCC_except_table114
- GCC_except_table116
- GCC_except_table127
- GCC_except_table129
- GCC_except_table131
- GCC_except_table137
- GCC_except_table141
- GCC_except_table143
- GCC_except_table148
- GCC_except_table151
- GCC_except_table154
- GCC_except_table159
- GCC_except_table161
- GCC_except_table164
- GCC_except_table166
- GCC_except_table168
- GCC_except_table171
- GCC_except_table176
- GCC_except_table179
- GCC_except_table181
- GCC_except_table183
- GCC_except_table189
- GCC_except_table195
- GCC_except_table198
- GCC_except_table383
- GCC_except_table391
- GCC_except_table529
- GCC_except_table539
- GCC_except_table541
- ___Block_byref_object_copy_.387
- ___Block_byref_object_copy_.936
- ___Block_byref_object_dispose_.388
- ___Block_byref_object_dispose_.937
- ___block_descriptor_tmp.1503
- ___block_descriptor_tmp.1567
- ___block_descriptor_tmp.1609
- ___block_descriptor_tmp.1642
- ___block_descriptor_tmp.71.1561
- ___block_literal_global.1162
- ___block_literal_global.1466
- ___block_literal_global.1531
- ___block_literal_global.1607
- ___block_literal_global.429
- _apply_block_1.1510
- _apply_block_2.1541
Functions:
+ -[KCPairingChannel populateKeychainWithEscrowIdentity]
~ -[KCPairingChannel fetchPCSItemPersistentRefs:error:] : 676 -> 696
~ -[KCPairingChannel createPacket:results:endSession:] : 1816 -> 2128
~ -[KCPairingChannel initiatorPCSDataPacket:complete:] : 4208 -> 4800
CStrings:
+ "PCS-Escrow"
+ "adding keychain entry data: <agrp=%@,vwht=%@,labl=%@,cdat=%@,uuid=%@>"
+ "com.apple.security.escrowRepairGenerateRecord"
+ "escrow-identity"
+ "item by itself is too large for the pairing channel: <agrp=%@,vwht=%@,labl=%@,cdat=%@,uuid=%@>"
+ "populateKeychainWithEscrowIdentity"
+ "successfully added pcs item: <agrp=%@,vwht=%@,labl=%@,cdat=%@,uuid=%@>"
+ "successfully updated pcs item: <agrp=%@,vwht=%@,labl=%@,cdat=%@,uuid=%@>"
- "adding keychain entry data %@"
- "item by itself is too large for the pairing channel: %@"
- "successfully added pcs item: %@"
- "successfully updated pcs item: %@"

```
