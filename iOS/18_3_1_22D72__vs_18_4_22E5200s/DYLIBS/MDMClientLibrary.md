## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

```diff

-5.2.7.0.0
-  __TEXT.__text: 0x193a0
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x1354
+20.4.13.0.0
+  __TEXT.__text: 0x19d08
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x17fc
   __TEXT.__const: 0xd1
   __TEXT.__gcc_except_tab: 0x450
-  __TEXT.__cstring: 0x1fc1
-  __TEXT.__oslogstring: 0x296c
+  __TEXT.__cstring: 0x207b
+  __TEXT.__oslogstring: 0x2aa0
   __TEXT.__dlopen_cstrs: 0xb7
-  __TEXT.__unwind_info: 0x5e8
-  __TEXT.__objc_classname: 0x301
-  __TEXT.__objc_methname: 0x46e6
-  __TEXT.__objc_methtype: 0x89b
-  __TEXT.__objc_stubs: 0x31e0
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x1058
+  __TEXT.__unwind_info: 0x618
+  __TEXT.__objc_classname: 0x303
+  __TEXT.__objc_methname: 0x488a
+  __TEXT.__objc_methtype: 0x8b0
+  __TEXT.__objc_stubs: 0x32c0
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__const: 0x1078
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a0
+  __DATA_CONST.__objc_selrefs: 0x1198
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x460
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x2fe0
-  __AUTH_CONST.__objc_const: 0x3a70
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__cfstring: 0x3080
+  __AUTH_CONST.__objc_const: 0x3438
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_ivar: 0x114
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 516
-  Symbols:   1103
-  CStrings:  1410
+  Functions: 549
+  Symbols:   1147
+  CStrings:  1438
 
Symbols:
+ _MDMDEPPushReceivedNotification
+ _MDMPendingMigrationCloudConfigurationDetailsChangedNotification
+ _MDMSendDEPPushReceivedNotification
+ _MDMSendPendingMigrationCloudConfigurationDetailsChangedNotification
+ _kCCIsRapidReturnToServiceKey
+ _kCCMDMServerUIDKey
+ _kMDMEnrollmentSSOAppStoreIDKey
+ _kMDMOptionIdleRebootAllowed
+ _objc_retain_x9
CStrings:
+ "\x06"
+ "\x13"
+ "@64@0:8@16@24@32@40@48@56"
+ "Declarations"
+ "ESSO details declaration data is invalid or missing: %{public}@"
+ "ESSO details declarations data is missing: %{public}@"
+ "ESSO details: a configuration profile and/or declarations must be present"
+ "EnrollmentSSOAppStoreID"
+ "IdleRebootAllowed"
+ "Sending DEP push received notification."
+ "Sending pending migration cloud configuration details changed notification."
+ "T@\"NSArray\",&,N,V_declarations"
+ "TB,N,V_isSingleton"
+ "_declarations"
+ "_isSingleton"
+ "_provisionalEnrollmentExpirationDateFromCloudConfig:"
+ "com.apple.devicemanagementclient.depPushReceived"
+ "com.apple.devicemanagementclient.pendingMigrationCloudConfigurationDetailsChanged"
+ "declarations"
+ "initWithCloudConfigDetails:"
+ "initWithiTunesStoreID:appIDs:associatedDomains:associatedDomainsEnableDirectDownloads:configurationProfile:declarations:"
+ "isProvisionallyEnrolledWithCloudConfig:"
+ "isRapidReturnToService"
+ "isSingleton"
+ "mdmServerUID"
+ "monitorDEPPushTokenIfNeededWithCompletion:"
+ "monitorDEPPushTokenWithCompletion:"
+ "setDeclarations:"
+ "setIsSingleton:"
+ "simulateDEPPushWithCompletion:"
+ "syncDEPPushTokenWithDelay:completion:"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "\x05"
- "@56@0:8@16@24@32@40@48"
- "initWithiTunesStoreID:appIDs:associatedDomains:associatedDomainsEnableDirectDownloads:configurationProfile:"
- "syncDEPPushTokenWithCompletion:"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"

```
