## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-694.80.7.0.0
-  __TEXT.__text: 0x4f538
-  __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_stubs: 0x6d20
-  __TEXT.__objc_methlist: 0x2edc
+694.100.32.0.0
+  __TEXT.__text: 0x52064
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_stubs: 0x6f00
+  __TEXT.__objc_methlist: 0x2f6c
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x1c90
-  __TEXT.__cstring: 0x417f
-  __TEXT.__objc_methname: 0x772a
-  __TEXT.__oslogstring: 0x7fac
+  __TEXT.__gcc_except_tab: 0x1c6c
+  __TEXT.__cstring: 0x4199
+  __TEXT.__objc_methname: 0x78be
+  __TEXT.__oslogstring: 0x8056
   __TEXT.__objc_classname: 0x74c
   __TEXT.__objc_methtype: 0x10e2
-  __TEXT.__unwind_info: 0xcb8
-  __DATA_CONST.__auth_got: 0x810
-  __DATA_CONST.__got: 0x6e0
+  __TEXT.__unwind_info: 0xe28
+  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__got: 0x780
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x14b8
-  __DATA_CONST.__cfstring: 0x3b80
+  __DATA_CONST.__const: 0x14c0
+  __DATA_CONST.__cfstring: 0x3ba0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5188
-  __DATA.__objc_selrefs: 0x1f38
-  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_const: 0x5248
+  __DATA.__objc_selrefs: 0x1fb0
+  __DATA.__objc_ivar: 0x2c0
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x130

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D2FC9106-2AC0-32A1-A658-AC5E7B64FD5A
-  Functions: 1366
-  Symbols:   489
-  CStrings:  3374
+  UUID: 11A2008C-D7E2-3940-8902-62C8CA719953
+  Functions: 1397
+  Symbols:   502
+  CStrings:  3403
 
Symbols:
+ _OBJC_CLASS_$_CSFallbackStingrayRecord
+ _OBJC_CLASS_$_CSLRCFedRecord
+ _OBJC_CLASS_$_CSLRCRecord
+ _OBJC_CLASS_$_OTSerializedPlistEscrowRecord
+ _kEscrowServiceFallbackStingrayLabel
+ _kEscrowServiceLRCFedLabel
+ _kEscrowServiceLRCLabel
+ _kSecureBackupFallbackStingrayMetadataHashKey
+ _kSecureBackupFallbackStingrayMetadataKey
+ _kSecureBackupKeybagDBRSHA256Key
+ _kSecureBackupKeybagFDESHA256Key
+ _kSecureBackupKeybagFallbackSHA256Key
+ _kSecureBackupKeybagLRCFedRecordKey
+ _kSecureBackupKeybagLRCFedSHA256Key
+ _kSecureBackupKeybagLRCSHA256Key
+ _kSecureBackupLRCFedMetadataHashKey
+ _kSecureBackupLRCFedMetadataKey
+ _kSecureBackupLRCMetadataHashKey
+ _kSecureBackupLRCMetadataKey
+ _kSecureBackupSerializedEscrowRecordKey
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "=== Escrow record ===\nTime of escrow: %@\nEscrow version: %@\nKeybag digest: %@"
+ "Corrupting record due to com.apple.cloudservices/DBR-RecordCorrupt"
+ "DBR-RecordCorrupt"
+ "EscrowServiceSerializedEscrowRecord"
+ "Returning a serialized escrow record: %@"
+ "T@\"NSString\",R,C,N,V_altDSID"
+ "TB,R,N,V_fallBackSR"
+ "TB,R,N,V_lrc"
+ "TB,R,N,V_lrcFed"
+ "_altDSID"
+ "_fallBackSR"
+ "_lrc"
+ "_lrcFed"
+ "additionalMetadataKeysForLabel:"
+ "additionalMetadataKeysForRequest:"
+ "dbrRecordCorrupt"
+ "error parsing fallback stingray record: %@"
+ "error parsing lrc fed record: %@"
+ "error parsing lrc record: %@"
+ "fallBackSR"
+ "fullRecordLabel"
+ "initWithRequest:validate:reqVersion:error:"
+ "lrc"
+ "lrcFed"
+ "metadataDigestKeyForLabel:"
+ "metadataDigestKeyForRequest:"
+ "recordDigestKeyForRequest:"
+ "returnSerializedEscrowRecord"
+ "setFallbackRecord:"
+ "setLabel:"
+ "setLrcFedRecord:"
+ "setLrcRecord:"
+ "useSHA256ForRequest:"
- "=== Escrow record ===\nTime of escrow: %@\nEscrow version: %@\nKeybag SHA256: %@\nKeybag digest: %@"
- "com.apple.sbd.kvstorechange"
- "handling notification %@"
- "initWithRequest:reqVersion:"
- "initWithRequest:validate:reqVersion:"

```
