## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61901.0.87.0.1
-  __TEXT.__text: 0x17bb20
+61901.40.47.0.1
+  __TEXT.__text: 0x17bb2c
   __TEXT.__auth_stubs: 0x3fe0
+  __TEXT.__delay_helper: 0x28c
   __TEXT.__objc_methlist: 0x629c
   __TEXT.__const: 0xd728
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__cstring: 0x1817b
+  __TEXT.__cstring: 0x18219
   __TEXT.__gcc_except_tab: 0x8b54
   __TEXT.__oslogstring: 0xf7ed
   __TEXT.__ustring: 0x406

   __TEXT.__dof_security_: 0x325
   __TEXT.__unwind_info: 0x5fc0
   __TEXT.__objc_classname: 0xaf8
-  __TEXT.__objc_methname: 0xc057
-  __TEXT.__objc_methtype: 0x36f4
+  __TEXT.__objc_methname: 0xc069
+  __TEXT.__objc_methtype: 0x36fa
   __TEXT.__objc_stubs: 0x8dc0
   __DATA_CONST.__got: 0x780
   __DATA_CONST.__const: 0x14548

   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x48
   __DATA.__objc_ivar: 0x620
-  __DATA.__data: 0x20e0
+  __DATA.__data: 0x20e8
   __DATA.__bss: 0x9a8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 48FE5C49-984F-3983-9A7B-EDC3F74A9607
+  UUID: 3086E894-4789-3DC8-9C9D-06B1725B648F
   Functions: 6969
-  Symbols:   20688
-  CStrings:  11173
+  Symbols:   20701
+  CStrings:  11175
 
Symbols:
+ -[OTControl healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:reply:]
+ ___109-[OTControl healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:reply:]_block_invoke
+ _dlopenHelper$CloudServices
+ _dlopenHelper$ManagedConfiguration
+ _dlopenHelperFlag$CloudServices
+ _dlopenHelperFlag$ManagedConfiguration
+ _gotLoadHelper_x10$_kSecureBackupErrorDomain
+ _gotLoadHelper_x8$_OBJC_CLASS_$_MCProfileConnection
+ _gotLoadHelper_x8$_OBJC_CLASS_$_SecureBackup
+ _gotLoadHelper_x8$_kSecureBackupAuthenticationAppleID
+ _gotLoadHelper_x8$_kSecureBackupAuthenticationPassword
+ _gotLoadHelper_x8$_kSecureBackupRecoveryKeyKey
+ _gotLoadHelper_x8$_kSecureBackupUsesRecoveryKeyKey
+ _gotLoadHelper_x8$_kSecureBackupiCloudDataProtectionDeleteAllRecordsKey
+ _gotLoadHelper_x9$_kSecureBackupContainsiCDPDataKey
+ _objc_msgSend$healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:reply:
- -[OTControl healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:updateIdMS:reply:]
- ___91-[OTControl healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:updateIdMS:reply:]_block_invoke
- _objc_msgSend$healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:updateIdMS:reply:
Functions:
~ -[OTControl healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:updateIdMS:reply:] -> -[OTControl healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:reply:] : 244 -> 256
CStrings:
+ "/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices"
+ "/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration"
+ "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:reply:"
+ "v52@0:8@\"OTControlArguments\"16B24B28B32B36B40@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">44"
+ "v52@0:8@16B24B28B32B36B40@?44"
- "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:updateIdMS:reply:"
- "v48@0:8@\"OTControlArguments\"16B24B28B32B36@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">40"
- "v48@0:8@16B24B28B32B36@?40"

```
