## otctl

> `filesystem/usr/sbin/otctl`

```diff

-61901.120.36.0.3
-  __TEXT.__text: 0x148c0
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x2340
-  __TEXT.__objc_methlist: 0xb74
+61901.120.56.0.1
+  __TEXT.__text: 0x15a34
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_stubs: 0x2400
+  __TEXT.__objc_methlist: 0xcd4
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x738
-  __TEXT.__objc_methname: 0x3890
-  __TEXT.__cstring: 0x324f
-  __TEXT.__objc_classname: 0x8c
-  __TEXT.__objc_methtype: 0x4a9
+  __TEXT.__gcc_except_tab: 0x74c
+  __TEXT.__objc_methname: 0x3adb
+  __TEXT.__cstring: 0x3336
+  __TEXT.__objc_classname: 0xb8
+  __TEXT.__objc_methtype: 0x4f4
   __TEXT.__oslogstring: 0xa5
-  __TEXT.__unwind_info: 0x4e0
-  __DATA_CONST.__auth_got: 0x2c0
+  __TEXT.__unwind_info: 0x538
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x460
-  __DATA_CONST.__cfstring: 0xe80
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__cfstring: 0xf20
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0xce8
-  __DATA.__objc_selrefs: 0xd48
-  __DATA.__objc_ivar: 0xb0
-  __DATA.__objc_data: 0x140
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_dictobj: 0x78
+  __DATA.__objc_const: 0xf00
+  __DATA.__objc_selrefs: 0xde0
+  __DATA.__objc_ivar: 0xc8
+  __DATA.__objc_data: 0x190
   __DATA.__data: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C71BD20-4B72-3788-86D0-9152548E7D6F
-  Functions: 296
-  Symbols:   147
-  CStrings:  1206
+  UUID: EE905D65-9A28-3DBF-B45D-68178E8FD9A5
+  Functions: 326
+  Symbols:   150
+  CStrings:  1252
 
Symbols:
+ _PBDataWriterWriteSubmessage
+ _PBReaderPlaceMark
+ _PBReaderRecallMark
CStrings:
+ "2"
+ "@\"OTAccountMetadataClassCEscrowRecordCache\""
+ "Error invalidating icsc repair cache version: %s\n"
+ "Invalidate icsc repair cache version"
+ "OTAccountMetadataClassCEscrowRecordCache"
+ "Successfully invalidated icsc repair cache version."
+ "T@\"NSData\",&,N,V_serializedRecord"
+ "T@\"NSString\",&,N,V_bottleID"
+ "T@\"OTAccountMetadataClassCEscrowRecordCache\",&,N,V_escrowRecordCache"
+ "TQ,N,V_cacheTimestamp"
+ "TQ,N,V_cacheVersion"
+ "TQ,N,V_passcodeGeneration"
+ "_bottleID"
+ "_cacheTimestamp"
+ "_cacheVersion"
+ "_escrowRecordCache"
+ "_passcodeGeneration"
+ "_serializedRecord"
+ "cacheTimestamp"
+ "cacheVersion"
+ "escrowRecordCache"
+ "hasBottleID"
+ "hasCacheTimestamp"
+ "hasCacheVersion"
+ "hasEscrowRecordCache"
+ "hasPasscodeGeneration"
+ "hasSerializedRecord"
+ "icsc-repair-invalidate-cache-version"
+ "icscRepairInvalidateCacheVersion:reply:"
+ "icscRepairInvalidateCacheVersionWithArguments:json:"
+ "passcodeGeneration"
+ "serializedRecord"
+ "setBottleID:"
+ "setCacheTimestamp:"
+ "setCacheVersion:"
+ "setEscrowRecordCache:"
+ "setHasCacheTimestamp:"
+ "setHasCacheVersion:"
+ "setHasPasscodeGeneration:"
+ "setPasscodeGeneration:"
+ "setSerializedRecord:"
+ "{?=\"cacheTimestamp\"b1\"cacheVersion\"b1\"passcodeGeneration\"b1}"
+ "{?=\"epoch\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"peerSecretsAccessibilityFixUpPerformed\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
- "Tq,N,V_escrowRepairAttemptVersion"
- "_escrowRepairAttemptVersion"
- "escrowRepairAttemptVersion"
- "hasEscrowRepairAttemptVersion"
- "setEscrowRepairAttemptVersion:"
- "setHasEscrowRepairAttemptVersion:"
- "{?=\"epoch\"b1\"escrowRepairAttemptVersion\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"peerSecretsAccessibilityFixUpPerformed\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"

```
