## dmd

> `/usr/libexec/dmd`

```diff

-221.5.1.0.0
-  __TEXT.__text: 0x84324
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_stubs: 0xe900
-  __TEXT.__objc_methlist: 0x7b24
-  __TEXT.__const: 0x158
-  __TEXT.__objc_classname: 0x1e54
-  __TEXT.__objc_methname: 0x117be
+239.0.0.0.0
+  __TEXT.__text: 0x850d0
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_stubs: 0xe940
+  __TEXT.__objc_methlist: 0x7bc4
+  __TEXT.__const: 0x160
+  __TEXT.__objc_classname: 0x1e74
+  __TEXT.__objc_methname: 0x11801
   __TEXT.__objc_methtype: 0x1d7f
   __TEXT.__cstring: 0x5349
-  __TEXT.__oslogstring: 0xaecf
+  __TEXT.__oslogstring: 0xb018
   __TEXT.__gcc_except_tab: 0x11cc
   __TEXT.__ustring: 0x80a
   __TEXT.__dlopen_cstrs: 0xaf
-  __TEXT.__unwind_info: 0x2050
-  __DATA_CONST.__auth_got: 0x780
-  __DATA_CONST.__got: 0x1320
+  __TEXT.__unwind_info: 0x2060
+  __DATA_CONST.__auth_got: 0x788
+  __DATA_CONST.__got: 0x1330
   __DATA_CONST.__const: 0x2748
   __DATA_CONST.__cfstring: 0x5760
-  __DATA_CONST.__objc_classlist: 0x6f0
+  __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x198
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x340
-  __DATA_CONST.__objc_arraydata: 0x500
-  __DATA_CONST.__objc_arrayobj: 0x948
+  __DATA_CONST.__objc_arraydata: 0x508
+  __DATA_CONST.__objc_arrayobj: 0x960
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1d1c8
-  __DATA.__objc_selrefs: 0x4170
-  __DATA.__objc_ivar: 0x428
-  __DATA.__objc_data: 0x4560
+  __DATA.__objc_const: 0x1d298
+  __DATA.__objc_selrefs: 0x4180
+  __DATA.__objc_ivar: 0x42c
+  __DATA.__objc_data: 0x45b0
   __DATA.__data: 0xc60
   __DATA.__bss: 0x4e8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount

   - /System/Library/PrivateFrameworks/Catalyst.framework/Catalyst
   - /System/Library/PrivateFrameworks/Categories.framework/Categories
   - /System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel
+  - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 48E1E9A3-0F2B-34D9-8BCA-7EAA8A8F1D02
-  Functions: 3089
-  Symbols:   913
-  CStrings:  5284
+  UUID: DD51ACA1-E3AF-3596-9C33-A1A0DB4CAF2E
+  Functions: 3103
+  Symbols:   916
+  CStrings:  5290
 
Symbols:
+ _DMCBYSetupAssistantNeedsToRun
+ _OBJC_CLASS_$_DMFDDMStartManagingAppRequest
+ _OBJC_CLASS_$_DMFDDMStartManagingAppResultObject
CStrings:
+ "Apps with available updates: %{public}@"
+ "Clearing web domain policy caches"
+ "DMDDDMStartManagingAppOperation"
+ "Managing DDM app: %{public}@"
+ "Predicate type: %{public}@ with unique identifier: %{public}@ extracted calendar identifier: %{public}@, budget type: %{public}@, budgeted identifiers: %{public}@, budgeted category identifiers: %{public}@, budgeted application identifiers: %{public}@, budgeted website identifiers: %{public}@, exempt application identifiers: %{public}@, notification times: %{public}@, budget schedule: %{public}@"
+ "Predicate type: %{public}@ with unique identifier: %{public}@ extracted calendar identifier: %{public}@, budgeted application identifiers: %{public}@, budgeted category identifiers: %{public}@, budgeted website identifiers: %{public}@, exempt application identifiers: %{public}@, notification times: %{public}@, budget schedule: %{public}@"
+ "Request to manage DDM app %{public}@ "
+ "T@\"NSCache\",R,N,V_webDomainPolicyCache"
+ "_webDomainPolicyCache"
+ "initWithCategories:applications:exemptApplications:webDomains:schedule:calendarIdentifier:identifier:"
+ "isDeletableSystemApplication"
+ "payloadExemptApps"
+ "shouldPreserveAppBinary"
+ "webDomainPolicyCache"
- "Clearing website policy caches"
- "Predicate type: %{public}@ with unique identifier: %{public}@ extracted calendar identifier: %{public}@, budget type: %{public}@, budgeted identifiers: %{public}@, notification times: %{public}@, budget schedule: %{public}@"
- "Predicate type: %{public}@ with unique identifier: %{public}@ extracted calendar identifier: %{public}@, budgeted application identifiers: %{public}@, budgeted category identifiers: %{public}@, budgeted website identifiers: %{public}@, notification times: %{public}@, budget schedule: %{public}@"
- "T@\"NSCache\",R,N,V_websiteURLsPolicyCache"
- "_websiteURLsPolicyCache"
- "initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:"
- "isSetupBuddyDone"
- "websiteURLsPolicyCache"

```
