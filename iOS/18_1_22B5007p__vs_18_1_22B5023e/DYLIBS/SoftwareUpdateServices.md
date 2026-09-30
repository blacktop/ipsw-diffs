## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-858.0.0.0.0
-  __TEXT.__text: 0xaae00
+867.0.0.0.0
+  __TEXT.__text: 0xaaf68
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x9188
-  __TEXT.__cstring: 0x1de73
+  __TEXT.__objc_methlist: 0x91e8
+  __TEXT.__cstring: 0x1e024
   __TEXT.__const: 0x2a0
   __TEXT.__gcc_except_tab: 0xf78
   __TEXT.__oslogstring: 0xd48
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2fe0
+  __TEXT.__unwind_info: 0x2fe8
   __TEXT.__objc_classname: 0xece
-  __TEXT.__objc_methname: 0x17b45
+  __TEXT.__objc_methname: 0x17c0a
   __TEXT.__objc_methtype: 0x34a8
-  __TEXT.__objc_stubs: 0x13420
-  __DATA_CONST.__got: 0xd40
-  __DATA_CONST.__const: 0x2840
+  __TEXT.__objc_stubs: 0x13520
+  __DATA_CONST.__got: 0xd50
+  __DATA_CONST.__const: 0x28e0
   __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5620
+  __DATA_CONST.__objc_selrefs: 0x5658
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x11b60
+  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__cfstring: 0x11ce0
   __AUTH_CONST.__objc_const: 0x17e40
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x1a18
+  __AUTH.__objc_data: 0x1018
   __DATA.__objc_ivar: 0x918
   __DATA.__data: 0xef8
-  __DATA.__bss: 0x128
-  __DATA_DIRTY.__objc_data: 0xbb8
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA.__bss: 0x108
+  __DATA_DIRTY.__objc_data: 0x15b8
+  __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4285
-  Symbols:   5338
-  CStrings:  7332
+  Functions: 4278
+  Symbols:   5343
+  CStrings:  7354
 
Symbols:
+ _kMGQDiskUsageAmountDataAvailable
+ _kSUAnalyticsEventNameOTAEvents_1
+ _kSUAutoDownload
+ _kSUCoreEventResultKey
+ _kSUCoreEventResultSuccess
+ _kSUErrorCode
+ _kSUEventName
+ _kSUPreSUStagingEnabled
+ _kSUPreSUStagingOptionalSize
+ _kSUPreSUStagingRequiredSize
+ _kSUTargetOSVersion
+ _kSUTotalRequiredFreeSpace
+ _kSUUpdateType
- _kSUCoreEventFailureReasonKey
CStrings:
+ "%!s(MISSING): current download doesn't exist"
+ "%!s(MISSING): failed to get the disk usage dictionary"
+ "-[SUManagerCore _createCoreAnalyticsEventWithCurrentDownloadFor:error:]"
+ "-[SUManagerCore _getAmountDataAvailable]"
+ "DiskUsage"
+ "DiskUsageAmountDataAvailable"
+ "Failed to create options for activity %!@(MISSING)"
+ "Found previously tracked but currently unscheduled analytics submission event expecte to run at %!@(MISSING). Will reschedule"
+ "Received activity: %!@(MISSING) with info: %!@(MISSING)"
+ "Unknown activity: %!@(MISSING)"
+ "[LEGACY]%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING)"
+ "_augmentCoreAnalyticsEvent:withUpdate:"
+ "_createCoreAnalyticsEventWithCurrentDownloadFor:error:"
+ "_describeAndReportEvent:policy:primaryDescriptor:alternateDescriptor:additionalMetrics:"
+ "_getAmountDataAvailable"
+ "_reportOTAEvent:withStatus:policy:descriptor:additionalMetrics:error:"
+ "_reportOTAEvent:withStatus:policy:primaryDescriptor:alternateDescriptor:additionalMetrics:error:"
+ "_submitCoreAnalyticsEvent:"
+ "com.apple.massStorage.SoftwareUpdate.OTAEvents_1"
+ "com.apple.softwareupdateservicesd.autodownload"
+ "errorCode"
+ "not supported"
+ "preSUStagingEnabled"
+ "preSUStagingOptionalSize"
+ "preSUStagingOptionalSize"
+ "preSUStagingRequiredSize"
+ "preSUStagingRequiredSize"
+ "reportCoreAnalyticsOTAAbandonedEvent:"
+ "reportCoreAnalyticsOTAAvailableEvent:"
+ "reportCoreAnalyticsOTADownloadedEvent"
+ "reportCoreAnalyticsOTAStartedDownloadingEvent:"
+ "reportOTAStartedDownloadingEvent:"
+ "targetOSVersion"
+ "v16@?0@\"SUCoreDescriptor\"8"
- "%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING),%!@(MISSING)"
- "Found previously tracked but currently unsheduled analytics submission event expecte to run at %!@(MISSING). Will reschedule"
- "No handler block found for activity Name: %!@(MISSING)"
- "Received activity: %!@(MISSING): %!@(MISSING)"
- "Unknown date"
- "_activityNameHandlerMap"
- "_describeAndReportEvent:policy:primaryDescriptor:alternateDescriptor:additionalTelemetryMetrics:"
- "_reportOTAEvent:withStatus:policy:descriptor:additionalTelemetryMetrics:"
- "_reportOTAEvent:withStatus:policy:primaryDescriptor:alternateDescriptor:additionalTelemetryMetrics:"
- "_reportOTAEvent:withStatus:policy:primaryDescriptor:alternateDescriptor:additionalTelemetryMetrics:error:"
- "checkedSummary"
- "failed to allocate event for otaPostponed event so not reported"
- "reportOTAStartedDownloadingEvent"

```
