## backgroundassets.user

> `/usr/libexec/backgroundassets.user`

```diff

-161.0.0.0.0
-  __TEXT.__text: 0x36560
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_stubs: 0x6dc0
-  __TEXT.__objc_methlist: 0x2b00
+162.40.3.0.0
+  __TEXT.__text: 0x37120
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_stubs: 0x6f80
+  __TEXT.__objc_methlist: 0x2b58
   __TEXT.__const: 0x128
-  __TEXT.__oslogstring: 0x4188
-  __TEXT.__cstring: 0x351e
-  __TEXT.__objc_classname: 0x6a7
-  __TEXT.__objc_methname: 0x8df8
-  __TEXT.__objc_methtype: 0x1883
-  __TEXT.__gcc_except_tab: 0x1248
-  __TEXT.__unwind_info: 0xda4
-  __DATA_CONST.__auth_got: 0x5a8
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x1028
-  __DATA_CONST.__cfstring: 0x2000
-  __DATA_CONST.__objc_classlist: 0x148
+  __TEXT.__oslogstring: 0x4296
+  __TEXT.__cstring: 0x3845
+  __TEXT.__objc_classname: 0x6c5
+  __TEXT.__objc_methname: 0x8fe6
+  __TEXT.__objc_methtype: 0x18c5
+  __TEXT.__gcc_except_tab: 0x110c
+  __TEXT.__unwind_info: 0xd98
+  __DATA_CONST.__auth_got: 0x5d8
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x10b0
+  __DATA_CONST.__cfstring: 0x2100
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5ab8
-  __DATA.__objc_selrefs: 0x1e00
+  __DATA.__objc_const: 0x5bc8
+  __DATA.__objc_selrefs: 0x1e70
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x340
+  __DATA.__objc_classrefs: 0x358
   __DATA.__objc_superrefs: 0x130
-  __DATA.__objc_ivar: 0x388
-  __DATA.__objc_data: 0xcd0
-  __DATA.__data: 0x9b8
+  __DATA.__objc_ivar: 0x394
+  __DATA.__objc_data: 0xd20
+  __DATA.__data: 0x9c0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xe8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1321
-  Symbols:   296
-  CStrings:  2314
+  Functions: 1336
+  Symbols:   305
+  CStrings:  2359
 
Symbols:
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSCalendar
+ __os_log_debug_impl
+ _os_variant_has_internal_diagnostics
+ _strlen
CStrings:
+ "1CB2CF25-5012-4A61-85D5-2FF468AE9203"
+ "@48@0:8q16@24q32@40"
+ "AppStore"
+ "B40@0:8@16@24[16C]32"
+ "BAInstallationSourceUtilities"
+ "BundleIdentifier"
+ "D\x13!$"
+ "Determining installation source for %{public}@"
+ "Failed to look up LS app proxy for %{public}@, cannot determine installation source."
+ "InstallSource"
+ "Invalid"
+ "Other"
+ "T@\"NSString\",&,N,V_applicationIdentifier"
+ "Tq,V_installSource"
+ "U"
+ "_installSource"
+ "calendarWithIdentifier:"
+ "com.apple.BackgroundAssets"
+ "com.apple.backgroundassets.BAAgentCore.didReceiveChallenge"
+ "com.apple.backgroundassets.BAAgentCore.didWriteBytes"
+ "com.apple.backgroundassets.BAAgentCore.downloadDidBegin"
+ "com.apple.backgroundassets.BAAgentCore.downloadDidPause"
+ "com.apple.backgroundassets.BAAgentCore.downloadQueue.essentialAssetState"
+ "com.apple.backgroundassets.BAAgentCore.failedWithError"
+ "com.apple.backgroundassets.BAAgentCore.finishedWithFileURL"
+ "com.apple.backgroundassets.BAAgentCore.manifest:finishedWithFileURL"
+ "com.apple.backgroundassets.handle-application-event"
+ "com.apple.backgroundassets.pokeScheduler"
+ "com.apple.backgroundassets.scheduleDownloads"
+ "com.apple.backgroundassets.startNextDownload.failed_to_start"
+ "component:fromDate:"
+ "defaultWorkspace"
+ "determineInstallSourceIfUnsetFromAuditToken:"
+ "deviceIdentifierForVendor"
+ "getUUIDBytes:"
+ "initWithContentRequest:applicationIdentifier:installSource:downloads:"
+ "installSource"
+ "installationSourceFromAuditToken:applicationIdentifier:"
+ "ordinalityOfUnit:inUnit:forDate:"
+ "profileValidated"
+ "q56@0:8{?=[8I]}16@48"
+ "send-telemetry-event"
+ "send-telemetry-event requires a valid identifier, ignoring."
+ "send-telemetry-event was called without specifying an application identifier."
+ "setInstallSource:"
+ "shouldReportBundleIDInTelemetry:date:deviceIdentifier:"
+ "stringByAppendingString:"
+ "v48@0:8{?=[8I]}16"
+ "valueForKey:"
- "4\x13!$"
- "@32@0:8q16@24"
- "D"
- "baagent.redeliverevents"
- "initWithContentRequest:downloads:"

```
