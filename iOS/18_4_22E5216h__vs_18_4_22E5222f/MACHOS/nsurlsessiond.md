## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

-3826.500.91.0.0
-  __TEXT.__text: 0x70588
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_stubs: 0x9ee0
+3826.500.101.0.0
+  __TEXT.__text: 0x70c0c
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__delay_helper: 0x110
+  __TEXT.__objc_stubs: 0xa020
   __TEXT.__objc_methlist: 0x55a4
   __TEXT.__const: 0x258
-  __TEXT.__gcc_except_tab: 0xd77c
-  __TEXT.__cstring: 0x3594
-  __TEXT.__objc_methname: 0xd913
+  __TEXT.__gcc_except_tab: 0xd810
+  __TEXT.__cstring: 0x3753
+  __TEXT.__objc_methname: 0xda03
   __TEXT.__objc_classname: 0xba0
   __TEXT.__objc_methtype: 0x2c1a
-  __TEXT.__oslogstring: 0xb255
-  __TEXT.__unwind_info: 0x26b8
-  __DATA_CONST.__auth_got: 0x830
-  __DATA_CONST.__got: 0x6f0
+  __TEXT.__oslogstring: 0xb479
+  __TEXT.__unwind_info: 0x26c8
+  __DATA_CONST.__auth_got: 0x848
+  __DATA_CONST.__got: 0x710
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x15e0
-  __DATA_CONST.__cfstring: 0x1e60
+  __DATA_CONST.__cfstring: 0x1f80
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x120

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x8248
-  __DATA.__objc_selrefs: 0x3228
+  __DATA.__objc_selrefs: 0x3278
   __DATA.__objc_ivar: 0x630
   __DATA.__objc_data: 0x15e0
-  __DATA.__data: 0xd88
+  __DATA.__data: 0xd90
   __DATA.__bss: 0x130
+  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1800
-  Symbols:   482
-  CStrings:  3501
+  Functions: 1802
+  Symbols:   489
+  CStrings:  3528
 
Symbols:
+ _OBJC_CLASS_$_RadarComponent
+ _OBJC_CLASS_$_RadarDraft
+ _OBJC_CLASS_$_TapToRadarService
+ __dispatch_main_q
+ _dispatch_activate
+ _dlopen
+ _os_variant_has_internal_diagnostics
CStrings:
+ "/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "All"
+ "CoreMedia Streaming (New Bugs)"
+ "Creating Tap to radar draft with title: %@ and reason: %@"
+ "Failed to create Tap to Radar draft, TTR is not allowed. Did you forget to call NDCanTriggerTapToRadar() first?"
+ "Failed to create Tap to Radar draft, error %@"
+ "Failed to create Tap to Radar draft, missing description or title"
+ "Failed to create Tap to Radar draft, title is too long (%lu vs %d)."
+ "Failed to create Tap to Radar draft, unknown radar component name %@"
+ "Failed to create a timer to keep track of PowerAssertion duration for AVAssetDownloadSessionWrapper %llu with taskIdentifier %lu"
+ "PowerAssertion has been held for too long."
+ "PowerAssertion was held for more than %d seconds for client %@.\nURL <%@>\nDestinationURL <%@>\nOptions %@\nAsset %@"
+ "[Automatic CFNetwork Diagnostics] %@"
+ "_powerAssertionTimer"
+ "a PowerAssertion has been held for too long"
+ "com.apple.coremedia.CoreMediaDiagnostics.CoreMediaDiagnosticExtension"
+ "com.apple.network"
+ "com.apple.news"
+ "createDraft:forProcessNamed:withDisplayReason:error:"
+ "initWithName:version:identifier:"
+ "setClassification:"
+ "setComponent:"
+ "setDiagnosticExtensionIDs:"
+ "setIsUserInitiated:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "setTitle:"
+ "shared"
- "_timer"

```
