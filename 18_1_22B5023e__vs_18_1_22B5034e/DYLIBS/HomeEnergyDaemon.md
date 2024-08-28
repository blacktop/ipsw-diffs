## HomeEnergyDaemon

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon`

```diff

-222.0.0.0.0
-  __TEXT.__text: 0x1aa83c
-  __TEXT.__auth_stubs: 0x32e0
-  __TEXT.__objc_methlist: 0x400
-  __TEXT.__const: 0x45d8
-  __TEXT.__cstring: 0x7200
-  __TEXT.__constg_swiftt: 0x21b0
-  __TEXT.__swift5_typeref: 0x183f
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x1736
-  __TEXT.__swift5_fieldmd: 0x18a4
-  __TEXT.__swift5_assocty: 0x348
-  __TEXT.__swift5_proto: 0x2f4
-  __TEXT.__swift5_types: 0x1b4
-  __TEXT.__oslogstring: 0x7ba5
-  __TEXT.__swift5_capture: 0x1e84
-  __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x4f78
-  __TEXT.__eh_frame: 0x10880
+228.0.0.0.0
+  __TEXT.__text: 0x1b2908
+  __TEXT.__auth_stubs: 0x3320
+  __TEXT.__objc_methlist: 0x408
+  __TEXT.__const: 0x4a98
+  __TEXT.__cstring: 0x7330
+  __TEXT.__constg_swiftt: 0x22c8
+  __TEXT.__swift5_typeref: 0x1987
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_reflstr: 0x17df
+  __TEXT.__swift5_fieldmd: 0x1980
+  __TEXT.__swift5_assocty: 0x390
+  __TEXT.__swift5_proto: 0x334
+  __TEXT.__swift5_types: 0x1c8
+  __TEXT.__oslogstring: 0x80b5
+  __TEXT.__swift5_capture: 0x1efc
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__unwind_info: 0x5078
+  __TEXT.__eh_frame: 0x10c10
   __TEXT.__objc_classname: 0xbc
-  __TEXT.__objc_methname: 0x30f3
+  __TEXT.__objc_methname: 0x31e6
   __TEXT.__objc_methtype: 0x687
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x930
+  __DATA_CONST.__got: 0x940
   __DATA_CONST.__const: 0x600
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf8
+  __DATA_CONST.__objc_selrefs: 0xc48
   __DATA_CONST.__objc_protorefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1978
-  __AUTH_CONST.__auth_ptr: 0x7d8
-  __AUTH_CONST.__const: 0x6270
-  __AUTH_CONST.__objc_const: 0x5538
-  __AUTH.__objc_data: 0x9c0
-  __AUTH.__data: 0x12a8
-  __DATA.__data: 0x1ed0
-  __DATA.__bss: 0x5b80
+  __AUTH_CONST.__auth_got: 0x1998
+  __AUTH_CONST.__auth_ptr: 0x7b8
+  __AUTH_CONST.__const: 0x65b8
+  __AUTH_CONST.__objc_const: 0x5440
+  __AUTH.__objc_data: 0x9d8
+  __AUTH.__data: 0x1210
+  __DATA.__data: 0x2000
+  __DATA.__bss: 0x6200
   __DATA.__common: 0x290
   __DATA_DIRTY.__objc_data: 0x5e8
-  __DATA_DIRTY.__data: 0x28c8
+  __DATA_DIRTY.__data: 0x2838
   __DATA_DIRTY.__bss: 0x200
-  __DATA_DIRTY.__common: 0x158
+  __DATA_DIRTY.__common: 0x150
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4547
-  Symbols:   558
-  CStrings:  1730
+  Functions: 4647
+  Symbols:   564
+  CStrings:  1767
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _swift_allocateGenericValueMetadata
+ _BGSystemTaskSchedulerErrorDomain
+ _swift_makeBoxUnique
+ _swift_checkMetadataState
- _swift_initStaticObject
CStrings:
+ "revokeUtilitySubscription"
+ "[END] Revoke Subscription Failed"
+ "[END] Revoke Subscription"
+ "[BackgroundTask] Successfully submitted task request associated with identifier\n%!{(MISSING)public}s"
+ "submitTaskRequest:error:"
+ "[BackgroundTask] Attempted to submit request for\n%!{(MISSING)public}s even though another request was already pending"
+ "%!s(MISSING) Auth token missing for %!{(MISSING)public}s"
+ "%!s(MISSING) SubscriptionID missing %!{(MISSING)public}s"
+ "[Dropbox] Failed CK Token %!{(MISSING)public}s"
+ "[BackgroundTask] Successfully registered launch handler associated with identifier %!{(MISSING)public}s"
+ "[BackgroundTask] %!s(MISSING) is already scheduled"
+ "[START] Reset Site"
+ "[Dropbox] Skip Refresh AMI Data for site %!{(MISSING)public}s"
+ "submitTestTaskWithTaskID:delay:completionHandler:"
+ "setRequiresNetworkConnectivity:"
+ "[END] Purge Subscription"
+ "setTrySchedulingBefore:"
+ "Executing task %!s(MISSING)"
+ "setScheduleAfter:"
+ "purgeSubscription(siteID:utilityID:subscriptionID:zoneName:)"
+ "%!s(MISSING) UtilityID missing %!{(MISSING)public}s"
+ "[START] Revoke Subscription"
+ "setPriority:"
+ "initWithIdentifier:"
+ "revokeUtilitySubscriptionTask"
+ "setResources:"
+ "[BackgroundTask] Setting up to register launch handler associated with identifier %!{(MISSING)public}s"
+ "[END] Reset Site"
+ "AMI Token Endpoint Error"
+ "scheduler"
+ "setShouldWakeDevice:"
+ "[Dropbox] Failed Refresh Token %!{(MISSING)public}s"
+ "v40@0:8@16q24@?32"
+ "[BackgroundTask] Declining to submit task request associated with identifier\n%!{(MISSING)public}s because another request is already scheduled, but not yet completed"
+ "[BackgroundTask] Failed to register launch handler associated with identifier %!{(MISSING)public}s"
+ "[START] Purge Subscription"
+ "setRequiresExternalPower:"
+ "[BackgroundTask] Attempting to submit task request associated with identifier\n%!{(MISSING)public}s"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"NSError\">32"
+ "[BackgroundTask] Successfully finished launching the task associated with identifier %!{(MISSING)public}s"
+ "[BackgroundTask] Execution of task associated with identifier %!{(MISSING)public}s failed"
+ "[BackgroundTask] Received unknown error while attempting to submit task request\nassociated with identifier %!{(MISSING)public}s: %!{(MISSING)public}@"
+ "%!s(MISSING) Site not found. %!{(MISSING)public}s"
+ "Site Fetched"
- "task"
- "[BackgroundTask] %!s(MISSING) launch handler associated with identifier %!{(MISSING)public}s"
- "_TtC16HomeEnergyDaemon29BackgroundSystemTaskScheduler"
- "[BackgroundTask] Configuring launch handler associated with identifier %!{(MISSING)public}s"
- "Failed to register"
- "Successfully registered"
- "_TtC16HomeEnergyDaemon23BackgroundSystemTaskRun"

```
