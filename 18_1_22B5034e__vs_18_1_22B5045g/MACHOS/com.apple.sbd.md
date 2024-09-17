## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-638.40.8.0.0
-  __TEXT.__text: 0x497d4
+638.40.20.502.1
+  __TEXT.__text: 0x4a214
   __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_stubs: 0x6420
-  __TEXT.__objc_methlist: 0x25d4
-  __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x1b1c
-  __TEXT.__cstring: 0x3b45
-  __TEXT.__objc_methname: 0x6c65
-  __TEXT.__oslogstring: 0x7acf
+  __TEXT.__objc_stubs: 0x64a0
+  __TEXT.__objc_methlist: 0x25e4
+  __TEXT.__const: 0x150
+  __TEXT.__gcc_except_tab: 0x1b34
+  __TEXT.__cstring: 0x3b81
+  __TEXT.__objc_methname: 0x6d21
+  __TEXT.__oslogstring: 0x7b24
   __TEXT.__objc_classname: 0x70d
-  __TEXT.__objc_methtype: 0xf29
-  __TEXT.__unwind_info: 0xbc8
+  __TEXT.__objc_methtype: 0xf6f
+  __TEXT.__unwind_info: 0xbd0
   __DATA_CONST.__auth_got: 0x7d8
-  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__got: 0x680
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1460
+  __DATA_CONST.__const: 0x1430
   __DATA_CONST.__cfstring: 0x36e0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5838
-  __DATA.__objc_selrefs: 0x1c18
+  __DATA.__objc_const: 0x5858
+  __DATA.__objc_selrefs: 0x1c40
   __DATA.__objc_ivar: 0x284
   __DATA.__objc_data: 0x10e0
   __DATA.__data: 0x5a8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1266
-  Symbols:   457
-  CStrings:  2724
+  Functions: 1268
+  Symbols:   470
+  CStrings:  2735
 
Symbols:
+ _kCloudServicesErrorDomain
+ _kSecureBackupExpectedFederationKey
+ _kEscrowServiceRecordStatusValid
+ _kSecureBackupFederationKey
+ _kEscrowServiceRecordMetadataKey
+ _kEscrowServiceRecordLabelKey
+ _kSecureBackupEncodedMetadataKey
+ _OBJC_CLASS_$_CSStingrayRecord
+ _kEscrowServiceStingrayLabel
+ _OBJC_CLASS_$_CSStingrayAccountStatus
+ _kSecureBackupMetadataTimestampKey
+ _kSecureBackupTimestampKey
+ _kEscrowServiceRecordStatusKey
CStrings:
+ "federationID"
+ "fetchStingrayAccountStatusInDaemon:reply:"
+ "ignoring icdp record: %!@(MISSING)"
+ "FEDERATIONID"
+ "error parsing record: %!@(MISSING)"
+ "v32@0:8@\"SecureBackup\"16@?<v@?@\"CSStingrayAccountStatus\"@\"NSError\">24"
+ "setStingrayRecord:"
+ "_fetchStingrayAccountStatusInDaemon:reply:"
+ "EXPECTEDFEDERATIONID"
+ "fetchStingrayAccountStatusInDaemon"
+ "errorWithDomain:code:underlyingError:format:"
+ "-[SecureBackupDaemon _fetchStingrayAccountStatusInDaemon:reply:]"
+ "ignoring escrow service record: %!@(MISSING)"
+ "decodedEscrowRecordFromData:stingray:env:duplicate:error:"
+ "parseFromAccountInfoPlist:error:"
- "valid"
- "com.apple.protectedcloudstorage.record"
- "SecureBackupMetadataTimestamp"
- "com.apple.securebackup.timestamp"
- "decodedEscrowRecordFromData:stingray:env:duplicate:"

```
