## dasd

> `/usr/libexec/dasd`

```diff

-1783.40.23.0.0
-  __TEXT.__text: 0xf7a88
-  __TEXT.__auth_stubs: 0x12b0
-  __TEXT.__objc_stubs: 0x15360
-  __TEXT.__objc_methlist: 0xe444
-  __TEXT.__cstring: 0xc7cf
+1786.60.70.502.1
+  __TEXT.__text: 0xfb60c
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__objc_stubs: 0x15720
+  __TEXT.__objc_methlist: 0xe6ac
   __TEXT.__const: 0x8a0
-  __TEXT.__objc_methname: 0x23d39
-  __TEXT.__objc_classname: 0x1699
-  __TEXT.__oslogstring: 0xe4eb
-  __TEXT.__objc_methtype: 0x319f
-  __TEXT.__gcc_except_tab: 0x4104
+  __TEXT.__objc_methname: 0x242ca
+  __TEXT.__cstring: 0xc8d6
+  __TEXT.__oslogstring: 0xee76
+  __TEXT.__objc_classname: 0x16c7
+  __TEXT.__objc_methtype: 0x324b
+  __TEXT.__gcc_except_tab: 0x4368
   __TEXT.__dlopen_cstrs: 0x488
-  __TEXT.__unwind_info: 0x3640
-  __DATA_CONST.__auth_got: 0x968
-  __DATA_CONST.__got: 0xa38
+  __TEXT.__unwind_info: 0x3748
+  __DATA_CONST.__auth_got: 0x978
+  __DATA_CONST.__got: 0xa30
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x33f0
-  __DATA_CONST.__cfstring: 0xd140
-  __DATA_CONST.__objc_classlist: 0x588
+  __DATA_CONST.__const: 0x34d0
+  __DATA_CONST.__cfstring: 0xd280
+  __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__objc_superrefs: 0x4b8
   __DATA_CONST.__objc_intobj: 0xd80
   __DATA_CONST.__objc_arraydata: 0x228
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA.__objc_const: 0x2db78
-  __DATA.__objc_selrefs: 0x7ab8
-  __DATA.__objc_ivar: 0x11ac
-  __DATA.__objc_data: 0x3750
+  __DATA.__objc_const: 0x2de48
+  __DATA.__objc_selrefs: 0x7bf0
+  __DATA.__objc_ivar: 0x11c8
+  __DATA.__objc_data: 0x37f0
   __DATA.__data: 0x1510
   __DATA.__bss: 0xb40
   __DATA.__common: 0x10

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 6029
-  Symbols:   644
-  CStrings:  9765
+  Functions: 6116
+  Symbols:   645
+  CStrings:  9876
 
Symbols:
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
- _OBJC_CLASS_$_LSApplicationExtensionRecord
CStrings:
+ "%!@(MISSING) about to expire, warning"
+ "%!@(MISSING) does not have the correct web browser entitlement on the host (%!d(MISSING))"
+ "%!{(MISSING)public}@: Process %!d(MISSING) not entitled for Continued Processing"
+ "%!{(MISSING)public}@: Process %!d(MISSING) not entitled for Icon Bundle Identifiers"
+ "1\x1a\x1f\x0f\x0f\x03\x12/\x03"
+ "@\"<_DASAssertionArbiterDelegate>\""
+ "@\"_DASAssertionArbiter\""
+ "Acquired %!@(MISSING)/%!@(MISSING) assertions for %!@(MISSING)"
+ "Assertion %!@(MISSING) invalidated, server-initiated: %!@(MISSING)"
+ "Assertion on networking process host"
+ "AssertionArbiter"
+ "AssertionAssociation"
+ "B28@0:8i16@20"
+ "B56@0:8{?=[8I]}16@48"
+ "BackgroundDownloadHostJetsamBand"
+ "Completion Count"
+ "ContinuousDownload"
+ "Creating BackgroundFetch assertion for %!@(MISSING) (target PID: %!d(MISSING))"
+ "Creating BackgroundTask assertion for %!@(MISSING) (target PID: %!d(MISSING))"
+ "Creating HealthKit assertion for %!@(MISSING) (target PID: %!d(MISSING))"
+ "Ensuring main application %!@(MISSING) is foregrounded (submitting bundle: %!@(MISSING))"
+ "Failed to acquire %!@(MISSING) for %!@(MISSING) with error: %!@(MISSING); skipping"
+ "Failed to acquire %!@(MISSING) with error: %!@(MISSING)"
+ "Failed to invalidate %!@(MISSING) for %!@(MISSING) with error: %!@(MISSING); skipping"
+ "Foregrounded apps doesn't include expected identifier: %!@(MISSING)"
+ "Invalidated %!@(MISSING)/%!@(MISSING) assertions for %!@(MISSING)"
+ "Invalidating assertions for %!@(MISSING)"
+ "Invalidating host assertion along with the extension assertion for %!@(MISSING)"
+ "No host assertion associated with %!@(MISSING), skipping continuing"
+ "No host assertion associated with %!@(MISSING), skipping invalidation"
+ "No launch reasons, calling completion and returning for %!@(MISSING)"
+ "Not creating a RBS Assertion for an invalid activity: %!@(MISSING)"
+ "Pre-existing launch requests for %!@(MISSING): %!@(MISSING)"
+ "Received Continued Processing Activity, but not acquiring assertion!"
+ "Received assertion invalidation for %!@(MISSING)"
+ "Received assertion warning for %!@(MISSING)"
+ "Received value of %!@(MISSING) for %!@(MISSING) entitlement"
+ "Run Count"
+ "Run Time"
+ "SecTaskCopyValueForEntitlement failed with error %!{(MISSING)public}@"
+ "Skipping activity %!@(MISSING) because it was scored too low"
+ "Skipping activity %!@(MISSING) because it's already running"
+ "Skipping activity %!@(MISSING) because it's not timewise eligible"
+ "Successfully acquired %!@(MISSING) for %!@(MISSING)"
+ "T@\"<_DASAssertionArbiterDelegate>\",W,N,V_handlerDelegate"
+ "T@\"NSMutableDictionary\",&,N,V_assertionAssociations"
+ "T@\"NSMutableSet\",&,N,V_assertions"
+ "T@\"_DASActivity\",W,N,V_activity"
+ "T@\"_DASAssertionArbiter\",&,N,V_assertionArbiter"
+ "Totals"
+ "Unable to create SecTask with audit token"
+ "Unable to create assertion for %!@(MISSING)"
+ "Unable to create managed assertion on behalf of %!@(MISSING)"
+ "Unable to create unmanaged assertion on behalf of %!@(MISSING)"
+ "Unable to father the bundle identifier! This task submission will be broken."
+ "Unable to find assertion association for %!@(MISSING), skipping acquisition"
+ "Unable to find assertion association for %!@(MISSING), skipping invalidation"
+ "Unable to get pid for host target for %!d(MISSING), continuing only with assertion for extension"
+ "Unable to grab RBS Process Handle for pid %!d(MISSING) with error: %!@(MISSING)"
+ "Unable to grab process handle for PID: %!d(MISSING)"
+ "Using dasd client connection info to grab the audit token for %!d(MISSING)"
+ "XPC_EVENT_PUBLISHER_ACTION_ADD: Cleared subscription for %!{(MISSING)public}@ due to error"
+ "XPC_EVENT_PUBLISHER_ACTION_ADD: Clearing subscription for %!{(MISSING)public}@ via xpc_event_publisher_set_event failed"
+ "_DASAssertionArbiter"
+ "_DASAssertionAssociation"
+ "_assertionArbiter"
+ "_assertionAssociations"
+ "_assertions"
+ "_handlerDelegate"
+ "acquireAssertions"
+ "acquireAssertionsForActivity:"
+ "anyAssertion"
+ "application-identifier is: %!@(MISSING)"
+ "assertionArbiter"
+ "assertionArbiter:clientWithPID:"
+ "assertionArbiter:didIssueInvalidationFor:serverInitiated:"
+ "assertionArbiter:didIssueWarningFor:"
+ "assertionAssociations"
+ "assertionForWebBrowserContinuedProcessingTask:targetPID:"
+ "assertions"
+ "auditToken"
+ "auditTokenForPID:success:"
+ "com.apple.developer.web-browser"
+ "com.apple.developer.web-browser-engine.networking"
+ "computeElapsedRunTimeTotals:"
+ "createAssertionForActivity:targetPID:"
+ "createAssertionForBackgroundFetchActivity:targetPID:"
+ "createAssertionForBackgroundTaskActivity:targetPID:"
+ "createAssertionForHealthKitActivity:targetPID:"
+ "createManagedAssertionForActivity:targetPID:"
+ "createUnmanagedAssertionForActivity:targetPID:"
+ "dasd client not present for pid (%!d(MISSING)); using RBSProcessHandle instead"
+ "doesAuditToken:haveEntitlement:"
+ "doesPID:haveEntitlement:"
+ "getInstallTimeline:bgsqlData:handler:"
+ "getInstallTimeline:filepath:"
+ "getRecentUniqueInstallationEvents:timeFilter:"
+ "handlerDelegate"
+ "hostAssertionAssociatedWithActivity:targetPID:"
+ "hostPIDForTarget:"
+ "hostProcess"
+ "initWithActivity:"
+ "initWithActivity:assertion:"
+ "initWithActivity:assertions:"
+ "installHandlersForAssertion:"
+ "invalidateAssertions"
+ "invalidateAssertionsForActivity:"
+ "isBackgroundFetchActivity:"
+ "isTerminalEvent:"
+ "rbs_pid"
+ "sectask entitlement check made for not-running process"
+ "setAssertionArbiter:"
+ "setAssertionAssociations:"
+ "setAssertions:"
+ "setHandlerDelegate:"
+ "shouldCreateAssertionForActivity:"
+ "trackAssertion:"
+ "v40@0:8@\"NSDateInterval\"16@\"NSData\"24@?<v@?@\"NSArray\">32"
+ "{?=[8I]}28@0:8i16^B20"
- "1\x1a\x1f\x0f\x0f\x02\x12/\x03"
- "Application-identifier is: %!@(MISSING)"
- "Launch requests for %!@(MISSING): %!@(MISSING)"
- "Skipping activity %!@(MISSING)"
- "Unable to obtain extension record for %!@(MISSING) with error %!@(MISSING)"
- "assertionForActivity:pid:"
- "containingBundleRecord"
- "getRecentUniqueInstallationEvents:"
- "initWithBundleIdentifier:error:"

```
