## DEPClientLibrary

> `/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary`

```diff

-20.5.1.2.0
-  __TEXT.__text: 0x4ad4
+43.0.0.0.0
+  __TEXT.__text: 0x4db4
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x864
+  __TEXT.__objc_methlist: 0x8c4
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__cstring: 0xc9a
+  __TEXT.__cstring: 0xdab
   __TEXT.__oslogstring: 0x2b
-  __TEXT.__unwind_info: 0x1d0
-  __TEXT.__objc_classname: 0x129
-  __TEXT.__objc_methname: 0x13a9
-  __TEXT.__objc_methtype: 0x4bb
-  __TEXT.__objc_stubs: 0xaa0
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__objc_classname: 0x12b
+  __TEXT.__objc_methname: 0x14b2
+  __TEXT.__objc_methtype: 0x500
+  __TEXT.__objc_stubs: 0xb60
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__const: 0x608
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c0
+  __DATA_CONST.__objc_selrefs: 0x4f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0x1358
+  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__objc_const: 0x13c8
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x180
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x2d0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7CDD4C0A-191A-3F26-BF31-2CE8B0E1EDAA
-  Functions: 151
-  Symbols:   808
-  CStrings:  646
+  UUID: F3F79097-98C0-351B-BCFB-35807A52CA77
+  Functions: 159
+  Symbols:   843
+  CStrings:  686
 
Symbols:
+ -[DEPClient makeEndMDMMigrationRequestWithServerUID:status:completionBlock:]
+ -[DEPClient makeStartMDMMigrationRequestWithCompletionBlock:]
+ -[DEPClient migrationStatus]
+ -[DEPClient serverUID]
+ -[DEPClient setMigrationStatus:]
+ -[DEPClient setServerUID:]
+ _OBJC_IVAR_$_DEPClient._migrationStatus
+ _OBJC_IVAR_$_DEPClient._serverUID
+ ___61-[DEPClient makeStartMDMMigrationRequestWithCompletionBlock:]_block_invoke
+ ___76-[DEPClient makeEndMDMMigrationRequestWithServerUID:status:completionBlock:]_block_invoke
+ _kCCHasUndergoneMigrationKey
+ _kCCIgnoreMDMFromBackupKey
+ _kCCSkipKeyAdditionalPrivacySettings
+ _kCCSkipKeyMultitasking
+ _kCCSkipKeyOSShowcase
+ _kCCSkipKeyPartiallySetUp
+ _kCCSkipKeyTips
+ _kDEPResponseErrorReasonKey
+ _kDEPResponseStatusKey
+ _kDEPResponseSuccess
+ _kDEPServerUIDKey
+ _objc_msgSend$makeEndMDMMigrationRequestWithServerUID:status:completionBlock:
+ _objc_msgSend$makeStartMDMMigrationRequestWithCompletionBlock:
+ _objc_msgSend$migrationStatus
+ _objc_msgSend$serverUID
+ _objc_msgSend$setMigrationStatus:
+ _objc_msgSend$setServerUID:
CStrings:
+ "\n"
+ "AdditionalPrivacySettings"
+ "CLOUD_CONFIG_DEVICE_REGISTRATION_FAILED"
+ "CLOUD_CONFIG_END_MDM_MIGRATION_FAILED"
+ "CLOUD_CONFIG_START_MDM_MIGRATION_FAILED"
+ "HasUndergoneMigration"
+ "IgnoreMDMFromBackup"
+ "IsReturnToService"
+ "Multitasking"
+ "OSShowcase"
+ "PartiallySetUp"
+ "T@\"NSString\",&,N,V_migrationStatus"
+ "T@\"NSString\",&,N,V_serverUID"
+ "Tips"
+ "_migrationStatus"
+ "_serverUID"
+ "error_reason"
+ "makeEndMDMMigrationRequestWithServerUID:status:completionBlock:"
+ "makeStartMDMMigrationRequestWithCompletionBlock:"
+ "migrationStatus"
+ "response_status"
+ "serverUID"
+ "server_uid"
+ "setMigrationStatus:"
+ "setServerUID:"
+ "success"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSDictionary\"@\"NSError\">32"
- "IsRapidReturnToService"

```
