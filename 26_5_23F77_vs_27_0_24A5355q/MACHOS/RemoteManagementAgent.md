## RemoteManagementAgent

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent`

```diff

-585.120.2.0.0
-  __TEXT.__text: 0x940ac
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_stubs: 0xc3c0
+621.0.0.502.1
+  __TEXT.__text: 0x8a814
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_stubs: 0xc340
   __TEXT.__objc_methlist: 0x49e8
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x48f4
-  __TEXT.__cstring: 0x2e71
-  __TEXT.__objc_classname: 0x1009
-  __TEXT.__objc_methname: 0xf190
-  __TEXT.__objc_methtype: 0x2692
-  __TEXT.__oslogstring: 0xc11f
+  __TEXT.__gcc_except_tab: 0x4074
+  __TEXT.__cstring: 0x2fb0
+  __TEXT.__objc_classname: 0xff8
+  __TEXT.__objc_methname: 0xf0b9
+  __TEXT.__objc_methtype: 0x265b
+  __TEXT.__oslogstring: 0xc232
   __TEXT.__ustring: 0x246
-  __TEXT.__unwind_info: 0x2248
-  __DATA_CONST.__auth_got: 0x418
-  __DATA_CONST.__got: 0x960
-  __DATA_CONST.__const: 0x26c0
-  __DATA_CONST.__cfstring: 0x3300
+  __TEXT.__unwind_info: 0x2060
+  __DATA_CONST.__const: 0x2740
+  __DATA_CONST.__cfstring: 0x33e0
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1c8
-  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__objc_intobj: 0x138
-  __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x85b0
-  __DATA.__objc_selrefs: 0x3528
-  __DATA.__objc_ivar: 0x2b4
+  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__auth_got: 0x440
+  __DATA_CONST.__got: 0x930
+  __DATA.__objc_const: 0x8598
+  __DATA.__objc_selrefs: 0x3510
+  __DATA.__objc_ivar: 0x2ac
   __DATA.__objc_data: 0x1d60
   __DATA.__data: 0xc68
-  __DATA.__bss: 0x560
+  __DATA.__bss: 0x590
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55A3DE58-862F-3B7B-9BF9-97F8A5AB2F7B
-  Functions: 2558
-  Symbols:   436
-  CStrings:  4472
+  UUID: B44A0554-6CFF-3B95-BDC1-9C4568271554
+  Functions: 2554
+  Symbols:   434
+  CStrings:  4490
 
Symbols:
+ _AnalyticsSendEventLazy
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
- _OBJC_CLASS_$_NSConstantDictionary
- _RMModelStatusItemDeviceModelIdentifier
- _RMModelStatusItemDeviceModelMarketingName
- _RMModelStatusItemDeviceModelNumber
- _RMModelStatusItemDeviceOperatingSystemMarketingName
- _RMModelStatusItemDeviceOperatingSystemSupplementalBuildVersion
- __os_log_default
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Configuration UI did not change after merge: %{public}@"
+ "ExtensibleSSOSubscriber"
+ "Ignoring disabled XPC service: %{public}@"
+ "RMAnalytics: Analytics successfully sent."
+ "RMAnalytics: DDM is not enabled on this MDM enrolled device."
+ "RMAnalytics: Device is not MDM enrolled. Not performing analytics."
+ "RMAnalytics: Error sending analytics: %{public}@"
+ "RMAnalytics: Unable to fetch management source objects: %{public}@"
+ "T@\"RMBackgroundTask\",&,N,V_dailyTask"
+ "Triggered daily background task"
+ "_dailyTask"
+ "activationPayload"
+ "activationPayloadState"
+ "com.apple.configuration.extensible-sso"
+ "com.apple.remotemanagement.daily"
+ "configurationUIWithTitle:description:details:"
+ "dailyTask"
+ "ddm_activation_count"
+ "ddm_asset_count"
+ "ddm_configuration_count"
+ "ddm_management_count"
+ "ddm_management_scope"
+ "ddm_management_source_count"
+ "ddm_statussubscription_count"
+ "descriptionUI"
+ "detailsUI"
+ "initWithSubscribedStatusKeyPathUpdater:persistentHistoryNotifier:context:"
+ "isExtensibleSSOConfigurationEnabled"
+ "isMDMEnrolled"
+ "numberWithUnsignedLong:"
+ "sendAnalyticsDataForAllManagementSourcesWithCompletionHandler:"
+ "setDailyTask:"
+ "setObject:atIndexedSubscript:"
+ "titleUI"
- "Configuration UI did not change: %{public}@"
- "Internal Device Status"
- "InternalStateArchiver.DeviceStatusByKeyPath"
- "Key %{public}@ changed from: %{public}@ to: %{public}@"
- "UDID"
- "Unable to save store metadata: %{public}@"
- "Unable to unarchive status data"
- "_internalDeviceStatusByKeyPath"
- "_internalDeviceStatusByKeyPathLock"
- "_internalDeviceStatusByKeyPathNotificationLock"
- "_notifyInternalDeviceStatusChangesIfNeeded"
- "a"
- "createDisallowedStatusValueErrorWithKeyPath:"
- "deviceStatusByKeyPath"
- "initWithInternalDeviceStatusByKeyPath:subscribedStatusKeyPathUpdater:persistentHistoryNotifier:context:"
- "internalStateArchiveWithContext:"
- "internalStatusPublisher:didChangeDeviceStatusByKeyPath:"
- "modelFamily"
- "modelIdentifier"
- "modelMarketingName"
- "modelNumber"
- "operatingSystemMarketingName"
- "operatingSystemSupplementalBuildVersion"
- "operatingSystemSupplementalExtraVersion"
- "restrictedKeyPaths"
- "serialNumber"
- "setDeviceStatusByKeyPath:"
- "v32@0:8@\"RMInternalStatusPublisher\"16@\"NSDictionary\"24"

```
