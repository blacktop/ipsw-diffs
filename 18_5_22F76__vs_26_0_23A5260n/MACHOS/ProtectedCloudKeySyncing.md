## ProtectedCloudKeySyncing

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing`

```diff

-1037.120.2.0.0
-  __TEXT.__text: 0x20edc
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_stubs: 0x42c0
-  __TEXT.__objc_methlist: 0x1b58
-  __TEXT.__const: 0x134
-  __TEXT.__gcc_except_tab: 0x1008
-  __TEXT.__cstring: 0x1519
-  __TEXT.__objc_methname: 0x4c4f
-  __TEXT.__oslogstring: 0x28c7
+1188.0.1.0.0
+  __TEXT.__text: 0x21b90
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_stubs: 0x4420
+  __TEXT.__objc_methlist: 0x1b8c
+  __TEXT.__const: 0x144
+  __TEXT.__gcc_except_tab: 0x1074
+  __TEXT.__cstring: 0x160f
+  __TEXT.__objc_methname: 0x4db2
+  __TEXT.__oslogstring: 0x2a20
   __TEXT.__objc_classname: 0x223
-  __TEXT.__objc_methtype: 0x1651
-  __TEXT.__unwind_info: 0x850
-  __DATA_CONST.__auth_got: 0x650
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0xf30
-  __DATA_CONST.__cfstring: 0x15e0
+  __TEXT.__objc_methtype: 0x16a1
+  __TEXT.__unwind_info: 0x868
+  __DATA_CONST.__auth_got: 0x670
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0xf98
+  __DATA_CONST.__cfstring: 0x16a0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2668
-  __DATA.__objc_selrefs: 0x1560
+  __DATA.__objc_const: 0x2670
+  __DATA.__objc_selrefs: 0x15b8
   __DATA.__objc_ivar: 0x1ac
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x370

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PairedSync.framework/PairedSync
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
-  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9477D535-7669-30F7-B50A-FEC0C751BEE9
-  Functions: 635
-  Symbols:   363
-  CStrings:  1772
+  UUID: 9C707234-39A2-376B-96B9-64C58C864D18
+  Functions: 640
+  Symbols:   371
+  CStrings:  1803
 
Symbols:
+ _OBJC_CLASS_$_AAFAnalyticsEventPCS
+ _OBJC_CLASS_$_PCSAnalyticsReporterRTC
+ __PCSServiceItemsGetAllManateeServices
+ __set_user_dir_suffix
+ _bzero
+ _confstr
+ _kPCSRTCEventCategoryAccountDataAccessRecovery
+ _kPCSRTCEventNameCreateManateeIdentities
CStrings:
+ "Batch manatee identity creation finished with error: %@"
+ "Identity creation failed for %@"
+ "Kicking off batch manatee identity creation from Manatee view ready notification"
+ "Received unexpected server throttle response, clamping to 10 seconds"
+ "Rolling not allowed in batch operations"
+ "Services to be created: %@"
+ "accountInfoWithCompletionHandler: %d/%d error: %@"
+ "addMetrics:"
+ "altDSIDForDSID:"
+ "checkRegistry: Account ineligible for MB restore: %@"
+ "com.apple.ProtectedCloudKeySyncing"
+ "com.apple.security.view-ready.Manatee"
+ "createIdentities:dsid:roll:sync:forceSync:complete:"
+ "createNewIdentities:roll:sync:forceSync:complete:"
+ "currentIdentity"
+ "currentItemReference"
+ "deviceToDeviceEncryptionAvailability"
+ "ensureManateeIdentitiesExist"
+ "errorIsSAThrottle:"
+ "initWithPCSMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
+ "numManateeIdentitiesErroredOnCreation"
+ "numManateeIdentitiesExisting"
+ "numManateeIdentitiesNewlyCreated"
+ "objectAtIndexedSubscript:"
+ "returnedExistingIdentity"
+ "sendMetricWithEvent:success:error:"
+ "setupSubscriptions: Account ineligible for MB restore: %@"
+ "v32@?0@\"NSArray\"8@\"PCSMTT\"16@\"NSError\"24"
+ "v32@?0@\"NSDictionary\"8@\"PCSMTT\"16@\"NSError\"24"
+ "v52@0:8@\"NSArray\"16@\"NSString\"24B32B36B40@?<v@?@\"NSArray\"@\"PCSMTT\"@\"NSError\">44"
- "accountStatusWithCompletionHandler:"
- "accountStatusWithCompletionHandler: %d error: %@"
- "createNewIdentity:roll:sync:forceSync:complete:"
- "v24@?0q8@\"NSError\"16"
- "v44@?0^{_PCSIdentityData=}8@\"NSData\"16@\"PCSMTT\"24B32@\"NSError\"36"

```
