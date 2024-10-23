## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-403.0.0.0.0
-  __TEXT.__text: 0x69bc0
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_stubs: 0xb740
-  __TEXT.__objc_methlist: 0x665c
-  __TEXT.__cstring: 0x4df1
-  __TEXT.__objc_methname: 0xe3e9
-  __TEXT.__objc_classname: 0x806
-  __TEXT.__objc_methtype: 0x2102
+404.0.0.0.0
+  __TEXT.__text: 0x6ae00
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_stubs: 0xb880
+  __TEXT.__objc_methlist: 0x675c
+  __TEXT.__cstring: 0x5083
+  __TEXT.__objc_methname: 0xe52a
+  __TEXT.__objc_classname: 0x83f
+  __TEXT.__objc_methtype: 0x2150
   __TEXT.__const: 0x278
-  __TEXT.__oslogstring: 0xa199
-  __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__unwind_info: 0x1478
-  __DATA_CONST.__auth_got: 0x690
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x1570
-  __DATA_CONST.__cfstring: 0x3e40
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __TEXT.__oslogstring: 0xa206
+  __TEXT.__gcc_except_tab: 0x8f0
+  __TEXT.__unwind_info: 0x14b8
+  __DATA_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0x1628
+  __DATA_CONST.__cfstring: 0x42a0
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xf168
-  __DATA.__objc_selrefs: 0x37f0
-  __DATA.__objc_ivar: 0x8cc
-  __DATA.__objc_data: 0x1b30
-  __DATA.__data: 0x6c0
-  __DATA.__bss: 0x168
+  __DATA.__objc_const: 0xfa48
+  __DATA.__objc_selrefs: 0x3848
+  __DATA.__objc_ivar: 0x8e0
+  __DATA.__objc_data: 0x1bd0
+  __DATA.__data: 0x720
+  __DATA.__bss: 0x188
   __DATA.__common: 0x1c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation
   - /System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/EventKitSyncServices.framework/EventKitSyncServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2593
-  Symbols:   339
-  CStrings:  4385
+  Functions: 2613
+  Symbols:   344
+  CStrings:  4448
 
Symbols:
+ _EKSSClientXPCInterface
+ _EKSSDiagnosticsDirectory
+ _EKSSMachServiceName
+ _EKSSServiceXPCInterface
+ _OBJC_CLASS_$_EKSSLogger
CStrings:
+ "\x11\x18\x16!"
+ "%!@(MISSING)"
+ "%!l(MISSING)i"
+ "== Started EventKitSync-404"
+ "@\"NEKServicesServer\""
+ "@\"NSXPCConnection\""
+ "Analytics"
+ "Companion-DiagnosticData.txt"
+ "Counts"
+ "Delta"
+ "EKSSServerInterface"
+ "Encoding complete with error: %!@(MISSING)"
+ "Encoding diagnosticDictionary to JSON"
+ "Gathering tinyStore dictionaryRepresentation"
+ "Last Successful Sync"
+ "NEKServicesClient"
+ "NEKServicesServer"
+ "NULL"
+ "Nightly"
+ "Received"
+ "Reset"
+ "Retries"
+ "Sent"
+ "URLByAppendingPathComponent:"
+ "Writing diagnostics complete with error: %!@(MISSING)"
+ "Writing diagnostics to URL: %!@(MISSING)"
+ "_connection"
+ "_dateForKey:"
+ "_servicesServer"
+ "accepted incoming connection"
+ "com.apple.eventkitsyncd"
+ "deferralCliff"
+ "diagnosticDictionary: %!@(MISSING)"
+ "driftFound"
+ "driftResultsForCache:"
+ "due"
+ "dumpDiagnosticsWithCompletion:"
+ "duplicateDriftLastChecked"
+ "duplicateResultsFromCheck:"
+ "duplicatesFound"
+ "fault"
+ "firstFoundDrift"
+ "firstFoundDuplicates"
+ "initWithConnection:andEnvironment:"
+ "initWithString:"
+ "initializing"
+ "interrupted: %!@(MISSING)"
+ "invalidated: %!@(MISSING)"
+ "isReset"
+ "lastCheckedDuplicatesAndDrift"
+ "lastDeltaSyncReceived"
+ "lastDeltaSyncSent"
+ "lastNightlySyncReceived"
+ "lastNightlySyncSent"
+ "lastResetSyncReceived"
+ "lastResetSyncSent"
+ "listening"
+ "migration"
+ "recordSuccessForSession:receiving:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setRemoteObjectInterface:"
+ "timestampLogForString:"
+ "v24@0:8@?<v@?@\"NSURL\"@\"EKSSLogger\">16"
+ "writeToURL:options:error:"
+ "\xf011"
- "\x11\x18\x16"
- "== Started EventKitSync-403"
- "_driftMetricFor:"
- "_duplicatesTreeFrom:"
- "\xf01\x11"

```
