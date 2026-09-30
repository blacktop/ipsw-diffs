## WiFiLogConfigDiagnosticExtension_iOS

> `/System/Library/PrivateFrameworks/WiFiLogCapture.framework/PlugIns/WiFiLogConfigDiagnosticExtension_iOS.appex/WiFiLogConfigDiagnosticExtension_iOS`

```diff

-1100.11.0.0.0
-  __TEXT.__text: 0xc58
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x240
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x96
-  __TEXT.__oslogstring: 0x2b0
-  __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x1e5
-  __TEXT.__objc_methtype: 0x29
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x80
+1100.14.0.0.0
+  __TEXT.__text: 0x2698
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__objc_methlist: 0x80
+  __TEXT.__const: 0x30
+  __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__cstring: 0x417
+  __TEXT.__oslogstring: 0x913
+  __TEXT.__objc_classname: 0x22
+  __TEXT.__objc_methname: 0x429
+  __TEXT.__objc_methtype: 0x4c
+  __TEXT.__dlopen_cstrs: 0x56
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xb0
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0x158
+  __DATA.__objc_selrefs: 0x128
+  __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9
-  Symbols:   50
-  CStrings:  52
+  Functions: 30
+  Symbols:   75
+  CStrings:  122
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CFAbsoluteTimeGetCurrent
+ _CFGetTypeID
+ _CFStringGetTypeID
+ _MGCopyAnswer
+ _OBJC_CLASS_$_DEAttachmentItem
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___kCFBooleanTrue
+ ___objc_personality_v0
+ __sl_dlopen
+ _abort_report_np
+ _free
+ _objc_autoreleaseReturnValue
+ _objc_getClass
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retainAutorelease
+ _objc_retain_x20
+ _objc_retain_x3
+ _sleep
- _objc_retain_x21
CStrings:
+ "%s"
+ "%{public}s::%d: Applying NoLogging com.apple.corecapture.configure config"
+ "%{public}s::%d: Error accessing directory: %@, erorr: %@"
+ "%{public}s::%d: Error reading plist %@: %@"
+ "%{public}s::%d: Found Managed Defaults file: %@"
+ "%{public}s::%d: No data in plist, skipping: %@"
+ "%{public}s::%d: No filename for plist, skipping: %@"
+ "%{public}s::%d: Not a plist, skipping: %@"
+ "%{public}s::%d: Posting values changed for applying NoLogging com.apple.corecapture.configure success: %d"
+ "%{public}s::%d: Posting values changed for removing com.apple.corecapture.configure success: %d"
+ "%{public}s::%d: Posting values done"
+ "%{public}s::%d: Posting values done for applying NoLogging com.apple.corecapture.configure sleep(12);"
+ "%{public}s::%d: Posting values done for removing com.apple.corecapture.configure sleep(12);"
+ "%{public}s::%d: Removing existing com.apple.corecapture.configure config"
+ "%{public}s::%d: applyOrRemoveManagedDomain Applied Managed Default success %d, %@ plist: %@"
+ "%{public}s::%d: applyOrRemoveManagedDomain Removed Managed Default success %d, %@ plist: %@"
+ "%{public}s::%d: applyOrRemoveManagedDomain apply %d success: %d"
+ "%{public}s::%d: attachmentList called"
+ "%{public}s::%d: attachmentsForParameters called with parameters: %@"
+ "%{public}s::%d: attachmentsForParameters done with attachments %@"
+ "%{public}s::%d: calling __attachmentsForTimberlorryWithParameters"
+ "%{public}s::%d: calling modifyManagedDefaults:FALSE due to Action:Remove to remove MegaWiFi"
+ "%{public}s::%d: calling modifyManagedDefaults:FALSE due to hostAppString:Timberlorry to remove MegaWiFi"
+ "%{public}s::%d: calling modifyManagedDefaults:TRUE due to Action:Apply to apply MegaWiFi"
+ "%{public}s::%d: calling modifyManagedDefaults:TRUE due to hostAppString:Timberlorry to apply MegaWiFi"
+ "%{public}s::%d: calling removeAndApplyNoLoggingToCoreCapture due to Action:RemoveCC to remove and apply noLoggingCC"
+ "%{public}s::%d: domainArray count %lu to update %@"
+ "%{public}s::%d: modifyManagedDefaults called with apply: %d"
+ "%{public}s::%d: postValuesChangedInDomains Updating Domains with changes %@"
+ "%{public}s::%d: postValuesChangedInDomains Updating Domains with changes done"
+ "%{public}s::%d: setupWithParameters called with parameters: %@"
+ "%{public}s::%d: teardownWithParameters called with parameters: %@"
+ "%{public}s::%d: uid num %d mainBundleURL %@ bundleForClass.bundleURL %@"
+ "-[WiFiLogConfigDiagnosticExtension applyOrRemoveManagedDomain:fileURL:]"
+ "-[WiFiLogConfigDiagnosticExtension attachmentList]"
+ "-[WiFiLogConfigDiagnosticExtension attachmentsForParameters:]"
+ "-[WiFiLogConfigDiagnosticExtension modifyManagedDefaults:]"
+ "-[WiFiLogConfigDiagnosticExtension postValuesChangedInDomains:]"
+ "-[WiFiLogConfigDiagnosticExtension removeAndApplyNoLoggingToCoreCapture]"
+ "-[WiFiLogConfigDiagnosticExtension setupWithParameters:]"
+ "-[WiFiLogConfigDiagnosticExtension teardownWithParameters:]"
+ "@\"NSDictionary\"8@?0"
+ "Action"
+ "Apply"
+ "B24@0:8@16"
+ "B28@0:8B16@20"
+ "Compress"
+ "ReleaseType"
+ "Remove"
+ "RemoveCC"
+ "Timberlorry"
+ "Unable to find class %s"
+ "W5Client"
+ "W5LogItemRequest"
+ "WiFiLogConfigDiagnosticExtension/NoLogging_ManagedDefaultFiles/"
+ "__attachmentsForTimberlorryWithParameters:"
+ "_attachmentsForParametersEndTime"
+ "_attachmentsForParametersStartTime"
+ "_setupWithParametersEndTime"
+ "_setupWithParametersStartTime"
+ "_teardownWithParametersEndTime"
+ "_teardownWithParametersStartTime"
+ "addObjectsFromArray:"
+ "applyOrRemoveManagedDomain:fileURL:"
+ "arrayWithObjects:count:"
+ "attachmentCollectionDuration"
+ "attachmentWithPathURL:"
+ "class"
+ "clearTimers"
+ "collectLogs:configuration:update:receipts:error:"
+ "com.apple.corecapture.configure"
+ "com.apple.wifi.diagnosticextension"
+ "d"
+ "dictionary"
+ "hostAppString"
+ "modifyManagedDefaults:"
+ "numberWithDouble:"
+ "objectForKey:"
+ "overallDuration"
+ "postValuesChangedInDomains:"
+ "releaseType"
+ "removeAndApplyNoLoggingToCoreCapture"
+ "requestWithItemID:configuration:"
+ "setObject:forKeyedSubscript:"
+ "setupDuration"
+ "sharedClient"
+ "softlink:o:path:/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity"
+ "teardownDuration"
+ "v16@0:8"
- "Applied Managed Default success %d, %@ plist: %@"
- "Error accessing directory: %@, erorr: %@"
- "Error reading plist %@: %@"
- "Found Managed Defaults file %@"
- "Found Managed Defaults file: %@"
- "No data in plist, skipping: %@"
- "No filename for plist, skipping: %@"
- "Not a plist, skipping: %@"
- "Removed Managed Default success %d, %@ plist: %@"
- "Updating Domains with changes %@"
- "Updating Domains with changes done"
- "_modifyManagedDefaults called with apply: %d"
- "_modifyManagedDefaults:"
- "attachmentList called"
- "attachmentsForParameters called with parameters: %@"
- "not wifi.ui, skipping: %@"
- "setupWithParameters called with parameters: %@"
- "teardownWithParameters called with parameters: %@"
- "uid num %d mainBundleURL %@ bundleForClass.bundleURL %@"
- "wifi.ui"

```
