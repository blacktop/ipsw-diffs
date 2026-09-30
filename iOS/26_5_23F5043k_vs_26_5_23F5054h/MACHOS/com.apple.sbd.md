## com.apple.sbd

> `filesystem/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-694.120.12.0.0
-  __TEXT.__text: 0x53e3c
+694.120.16.0.0
+  __TEXT.__text: 0x54814
   __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_stubs: 0x7020
-  __TEXT.__objc_methlist: 0x304c
+  __TEXT.__objc_stubs: 0x70c0
+  __TEXT.__objc_methlist: 0x30a8
   __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x1d10
-  __TEXT.__cstring: 0x432d
-  __TEXT.__objc_methname: 0x7a31
-  __TEXT.__oslogstring: 0x828d
+  __TEXT.__cstring: 0x43d7
+  __TEXT.__objc_methname: 0x7bbb
+  __TEXT.__oslogstring: 0x836a
   __TEXT.__objc_classname: 0x77d
-  __TEXT.__objc_methtype: 0x1128
-  __TEXT.__unwind_info: 0xe70
+  __TEXT.__objc_methtype: 0x1176
+  __TEXT.__unwind_info: 0xe80
   __DATA_CONST.__auth_got: 0x7e8
-  __DATA_CONST.__got: 0x780
+  __DATA_CONST.__got: 0x788
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1538
-  __DATA_CONST.__cfstring: 0x3ce0
+  __DATA_CONST.__const: 0x1560
+  __DATA_CONST.__cfstring: 0x3d20
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x53a8
-  __DATA.__objc_selrefs: 0x2008
-  __DATA.__objc_ivar: 0x2c0
+  __DATA.__objc_const: 0x5440
+  __DATA.__objc_selrefs: 0x2038
+  __DATA.__objc_ivar: 0x2cc
   __DATA.__objc_data: 0x1220
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x130

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 96A16B43-EF13-357C-9CC6-896A31438C0D
-  Functions: 1421
-  Symbols:   504
-  CStrings:  3454
+  UUID: 3A9E7B79-9005-3841-8FE7-06A937EE344C
+  Functions: 1430
+  Symbols:   505
+  CStrings:  3477
 
Symbols:
+ _kSecureBackupLRCRecordFedHashKey
CStrings:
+ "-[SecureBackupDaemon storeSerializedEscrowRecordWithRequest:escrowRecord:reply:]"
+ "Cannot enroll serialized record: %@"
+ "Creating an escrow enrollment operation"
+ "Creating an escrow update operation"
+ "TB,N,V_useSerializedEscrowRecord"
+ "TB,R,N,V_returnSerializedEscrowRecord"
+ "TB,R,N,V_serverCheckRecordStatus"
+ "_returnSerializedEscrowRecord"
+ "_serverCheckRecordStatus"
+ "_useSerializedEscrowRecord"
+ "check_club_status"
+ "escrowService storeSerializedEscrowRecord: returned: %@"
+ "escrowService storeSerializedEscrowRecord: succeeded"
+ "serialized escrow record label (%@) does not match expected label (%@)"
+ "serverCheckRecordStatus"
+ "setUseSerializedEscrowRecord:"
+ "storeSerializedEscrowRecordWithRequest:escrowRecord:reply:"
+ "storeSerializedRecordWithRequest:escrowRecord:completionBlock:"
+ "useSerializedEscrowRecord"
+ "v40@0:8@\"SecureBackup\"16@\"OTSerializedPlistEscrowRecord\"24@?<v@?@\"NSError\">32"

```
