## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x1e9c4
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x1d14
+46.0.0.0.0
+  __TEXT.__text: 0x1f428
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x1da4
   __TEXT.__const: 0xd1
-  __TEXT.__gcc_except_tab: 0x538
-  __TEXT.__cstring: 0x22b2
-  __TEXT.__oslogstring: 0x2e98
+  __TEXT.__gcc_except_tab: 0x520
+  __TEXT.__cstring: 0x231a
+  __TEXT.__oslogstring: 0x2f1c
   __TEXT.__dlopen_cstrs: 0xb7
-  __TEXT.__unwind_info: 0x808
+  __TEXT.__unwind_info: 0x838
   __TEXT.__objc_classname: 0x336
-  __TEXT.__objc_methname: 0x5388
-  __TEXT.__objc_methtype: 0xba2
-  __TEXT.__objc_stubs: 0x3800
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x1168
+  __TEXT.__objc_methname: 0x556f
+  __TEXT.__objc_methtype: 0xbc9
+  __TEXT.__objc_stubs: 0x3920
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0x1170
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1358
+  __DATA_CONST.__objc_selrefs: 0x13a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__auth_got: 0x480
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x31e0
-  __AUTH_CONST.__objc_const: 0x39e8
+  __AUTH_CONST.__cfstring: 0x3200
+  __AUTH_CONST.__objc_const: 0x3a10
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x124

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 933069E5-276D-3F44-8690-0F23E59DA162
-  Functions: 668
-  Symbols:   2888
-  CStrings:  1949
+  UUID: 134A37E7-B27D-30F8-A829-F21F9E9CB257
+  Functions: 681
+  Symbols:   2927
+  CStrings:  1966
 
Symbols:
+ +[MDMConfiguration hasIncompleteMigration]
+ -[MDMClientCore deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:]
+ -[MDMClientCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]
+ -[MDMClientCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]
+ -[MDMClientCore generateBootstrapTokenWithDevicePasscodeContext:completionHandler:]
+ -[MDMProvisioningProfileTrust didEnrollInMDMWithPasscodeContext:duringMigration:]
+ -[MDMProvisioningProfileTrust didEnrollInMDMWithPasscodeContext:passcode:duringMigration:]
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table47
+ _DMCMigrationHasIncompleteMigrationKey
+ _MDMMigrationConfigFilePath
+ _MDMMigrationEligibilityChangedNotification
+ _MDMSendMigrationEligibilityChangedNotification
+ _OBJC_CLASS_$_DMCPropertyListStorage
+ ___54-[MDMClientCore _queue_createAndStartMDMXPCConnection]_block_invoke.150
+ ___83-[MDMClientCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke
+ ___83-[MDMClientCore generateBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke
+ ___87-[MDMClientCore deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:]_block_invoke
+ ___90-[MDMClientCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke
+ _getLAContextClass
+ _objc_msgSend$deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:
+ _objc_msgSend$didEnrollInMDMWithPasscodeContext:passcode:duringMigration:
+ _objc_msgSend$generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:
+ _objc_msgSend$generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:
+ _objc_msgSend$generateBootstrapTokenWithDevicePasscodeContext:completionHandler:
+ _objc_msgSend$hasIncompleteMigration
+ _objc_msgSend$initWithExternalizedContext:
+ _objc_msgSend$initWithFilePath:
+ _objc_msgSend$retrieveValueForKey:error:
+ _objc_retain_x9
- GCC_except_table102
- GCC_except_table98
- ___54-[MDMClientCore _queue_createAndStartMDMXPCConnection]_block_invoke.145
CStrings:
+ "%s %@"
+ "+[MDMConfiguration hasIncompleteMigration]"
+ "Failed to retrieve HasIncompleteMigration info with error: %{public}@"
+ "Sending MDM migration eligibility changed notification."
+ "com.apple.devicemanagementclient.migrationEligibilityChanged"
+ "deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:"
+ "didEnrollInMDMWithPasscodeContext:duringMigration:"
+ "didEnrollInMDMWithPasscodeContext:passcode:duringMigration:"
+ "generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:"
+ "generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:"
+ "generateBootstrapTokenWithDevicePasscodeContext:completionHandler:"
+ "hasIncompleteMigration"
+ "initWithExternalizedContext:"
+ "initWithFilePath:"
+ "retrieveValueForKey:error:"
+ "v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24"

```
