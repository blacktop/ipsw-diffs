## CloudServices

> `/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices`

```diff

-694.120.12.0.0
-  __TEXT.__text: 0x319ac
+694.120.16.0.0
+  __TEXT.__text: 0x321dc
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x2c5c
+  __TEXT.__objc_methlist: 0x2cb8
   __TEXT.__const: 0xd20
-  __TEXT.__cstring: 0x276d
-  __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__oslogstring: 0x22af
-  __TEXT.__unwind_info: 0xd58
+  __TEXT.__cstring: 0x27eb
+  __TEXT.__gcc_except_tab: 0x704
+  __TEXT.__oslogstring: 0x235e
+  __TEXT.__unwind_info: 0xd80
   __TEXT.__objc_classname: 0x48a
-  __TEXT.__objc_methname: 0x542c
-  __TEXT.__objc_methtype: 0x1093
-  __TEXT.__objc_stubs: 0x36a0
+  __TEXT.__objc_methname: 0x5580
+  __TEXT.__objc_methtype: 0x10e1
+  __TEXT.__objc_stubs: 0x3760
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0xc88
+  __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1448
+  __DATA_CONST.__objc_selrefs: 0x1488
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x26c0
-  __AUTH_CONST.__objc_const: 0x4030
+  __AUTH_CONST.__cfstring: 0x2740
+  __AUTH_CONST.__objc_const: 0x40a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x2d0
+  __DATA.__objc_ivar: 0x2d8
   __DATA.__data: 0x2d0
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x780

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0BDC6C9-DCCC-302D-8053-12921C64BB21
-  Functions: 1274
-  Symbols:   547
-  CStrings:  2043
+  UUID: 3AC7880A-8D3B-3BEF-9F6B-D4B298A286A5
+  Functions: 1288
+  Symbols:   550
+  CStrings:  2068
 
Symbols:
+ _SecureBackupGetFedCert
+ _kSecureBackupLRCRecordFedHashKey
+ _kSecureBackupServerCheckRecordStatusKey
CStrings:
+ "-[SecureBackup enableAndReturnResults:]"
+ "-[SecureBackup storeSerializedEscrowRecord:withError:]"
+ "LRCRecordFedHash"
+ "ServerCheckRecordStatus"
+ "T@\"NSData\",&,N,V_lrcRecordFedHash"
+ "TB,N,V_serverCheckRecordStatus"
+ "_lrcRecordFedHash"
+ "_serverCheckRecordStatus"
+ "calling storeSerializedEscrowRecordWithRequest in daemon"
+ "enableAndReturnResults:"
+ "getFedCert (legacy API)"
+ "hasLrcRecordFedHash"
+ "lrcRecordFedHash"
+ "serverCheckRecordStatus"
+ "setLrcRecordFedHash:"
+ "setServerCheckRecordStatus:"
+ "storeSerializedEscrowRecord:withError:"
+ "storeSerializedEscrowRecordWithError remote proxy error: %ld"
+ "storeSerializedEscrowRecordWithRequest came back with %@"
+ "storeSerializedEscrowRecordWithRequest:escrowRecord:reply:"
+ "v40@0:8@\"SecureBackup\"16@\"OTSerializedPlistEscrowRecord\"24@?<v@?@\"NSError\">32"
- "-[SecureBackup enableAndReturnNetworkReachedHint:]"

```
