## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

-3826.400.120.0.0
-  __TEXT.__text: 0x535ac
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0x7fc0
-  __TEXT.__objc_methlist: 0x1d90
-  __TEXT.__gcc_except_tab: 0xb168
+3826.500.111.1.1
+  __TEXT.__text: 0x546b0
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__delay_helper: 0x110
+  __TEXT.__objc_stubs: 0x8220
+  __TEXT.__objc_methlist: 0x25bc
   __TEXT.__const: 0x248
-  __TEXT.__objc_methname: 0x9d3a
+  __TEXT.__gcc_except_tab: 0xb30c
+  __TEXT.__objc_methname: 0x9f36
   __TEXT.__objc_classname: 0x4d6
-  __TEXT.__objc_methtype: 0x1d4e
-  __TEXT.__cstring: 0x2d7d
-  __TEXT.__oslogstring: 0x9a7f
-  __TEXT.__unwind_info: 0x1a40
-  __DATA_CONST.__auth_got: 0x6b8
-  __DATA_CONST.__got: 0x580
+  __TEXT.__objc_methtype: 0x1d97
+  __TEXT.__cstring: 0x2f4e
+  __TEXT.__oslogstring: 0x9d23
+  __TEXT.__unwind_info: 0x1a70
+  __DATA_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__got: 0x5a8
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1318
-  __DATA_CONST.__cfstring: 0x14a0
+  __DATA_CONST.__cfstring: 0x15e0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x47b8
-  __DATA.__objc_selrefs: 0x2390
+  __DATA.__objc_const: 0x3950
+  __DATA.__objc_selrefs: 0x2578
   __DATA.__objc_ivar: 0x358
   __DATA.__objc_data: 0x820
-  __DATA.__data: 0xa20
+  __DATA.__data: 0xa28
   __DATA.__bss: 0xe0
+  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4902BBC5-FFD1-3108-932B-B5560B7ADA0A
-  Functions: 865
-  Symbols:   398
-  CStrings:  2708
+  UUID: A6640350-7663-34E0-B0D2-FE8FAB92EE69
+  Functions: 867
+  Symbols:   407
+  CStrings:  2761
 
Symbols:
+ _OBJC_CLASS_$_RadarComponent
+ _OBJC_CLASS_$_RadarDraft
+ _OBJC_CLASS_$_TapToRadarService
+ _SANDBOX_CHECK_CANONICAL
+ _SANDBOX_CHECK_NO_REPORT
+ __dispatch_main_q
+ _dispatch_activate
+ _dlopen
+ _os_variant_has_internal_diagnostics
CStrings:
+ "/.nofollow%s"
+ "/.nofollow/"
+ "/AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit"
+ "@56@0:8@16{?=[8I]}24"
+ "All"
+ "Client tried to set _directoryForDownloadedFiles but does not have access to directory"
+ "CoreMedia Streaming (New Bugs)"
+ "Creating Tap to radar draft with title: %@ and reason: %@"
+ "Failed to create Tap to Radar draft, TTR is not allowed. Did you forget to call NDCanTriggerTapToRadar() first?"
+ "Failed to create Tap to Radar draft, error %@"
+ "Failed to create Tap to Radar draft, missing description or title"
+ "Failed to create Tap to Radar draft, title is too long (%lu vs %d)."
+ "Failed to create Tap to Radar draft, unknown radar component name %@"
+ "Failed to create a timer to keep track of PowerAssertion duration for AVAssetDownloadSessionWrapper %llu with taskIdentifier %lu"
+ "NDSession <%{public}@> %{public}@ applying overrides %@"
+ "NDSession <%{public}@> Client tried to set _directoryForDownloadedFiles but does not have access to directory"
+ "NDSession <%{public}@> Client tried to set _pathToDownloadTaskFile but is not allowed to create %@"
+ "PowerAssertion has been held for too long."
+ "PowerAssertion was held for more than %d seconds for client %@.\nURL <%@>\nDestinationURL <%@>\nOptions %@\nAsset %@"
+ "Too many total tasks for app <%{public}@>, skipping other sessions"
+ "[Automatic CFNetwork Diagnostics] %@"
+ "_allowsCellularAccess"
+ "_allowsConstrainedNetworkAccess"
+ "_allowsExpensiveNetworkAccess"
+ "_downloadFileProtectionType"
+ "_forceEnablePQTLS"
+ "_powerAssertionTimer"
+ "a PowerAssertion has been held for too long"
+ "applyOverrides:forTaskWithIdentifier:"
+ "com.apple.coremedia.CoreMediaDiagnostics.CoreMediaDiagnosticExtension"
+ "com.apple.network"
+ "com.apple.news"
+ "createDraft:forProcessNamed:withDisplayReason:error:"
+ "initWithName:version:identifier:"
+ "noFollowRealURL:"
+ "realpath failed on %@"
+ "safeDirectoryForDownloads:auditToken:"
+ "safeURLForDownload:auditToken:"
+ "setClassification:"
+ "setComponent:"
+ "setDiagnosticExtensionIDs:"
+ "setIsUserInitiated:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "setTitle:"
+ "set_downloadFileProtectionType:"
+ "set_forceEnablePQTLS:"
+ "shared"
+ "v32@0:8@\"_NSURLSessionBackgroundTaskOverrides\"16Q24"
- "Client tried to set _directoryForDownloadedFiles but does not have access to directory %@"
- "NDSession <%{public}@> Client tried to set _directoryForDownloadedFiles but does not have access to directory %@"
- "NDSession <%{public}@> Client tried to set _pathToDownloadTaskFile but is not allowed to create %@: %{errno}d"
- "_isSafeDirectoryForDownloads:withToken:"
- "_timer"
- "file-write-create"

```
