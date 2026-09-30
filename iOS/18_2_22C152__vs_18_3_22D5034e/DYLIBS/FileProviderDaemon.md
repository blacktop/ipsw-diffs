## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-2732.60.128.0.0
-  __TEXT.__text: 0xcfd60
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_methlist: 0x5508
+2732.80.45.0.0
+  __TEXT.__text: 0xd1554
+  __TEXT.__auth_stubs: 0x1230
+  __TEXT.__objc_methlist: 0x5540
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0xd072
-  __TEXT.__oslogstring: 0xe061
-  __TEXT.__gcc_except_tab: 0xd4c0
+  __TEXT.__cstring: 0xd1e8
+  __TEXT.__oslogstring: 0xe310
+  __TEXT.__gcc_except_tab: 0xd5b4
   __TEXT.__ustring: 0x1922
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x39f0
-  __TEXT.__objc_classname: 0xa72
-  __TEXT.__objc_methname: 0x15d71
-  __TEXT.__objc_methtype: 0x5533
-  __TEXT.__objc_stubs: 0xe340
-  __DATA_CONST.__got: 0x818
+  __TEXT.__unwind_info: 0x3a40
+  __TEXT.__objc_classname: 0xa73
+  __TEXT.__objc_methname: 0x15e42
+  __TEXT.__objc_methtype: 0x555c
+  __TEXT.__objc_stubs: 0xe440
+  __DATA_CONST.__got: 0x828
   __DATA_CONST.__const: 0x3a30
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4410
+  __DATA_CONST.__objc_selrefs: 0x4468
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x908
+  __DATA_CONST.__objc_arraydata: 0xd0
+  __AUTH_CONST.__auth_got: 0x928
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x5e80
-  __AUTH_CONST.__objc_const: 0x12790
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__const: 0xa40
+  __AUTH_CONST.__cfstring: 0x5f40
+  __AUTH_CONST.__objc_const: 0x127e0
+  __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x9b0
   __DATA.__objc_ivar: 0x964
   __DATA.__data: 0xf10
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x148

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 3551
-  Symbols:   4441
-  CStrings:  6014
+  Functions: 3575
+  Symbols:   4478
+  CStrings:  6049
 
Symbols:
+ _CFRelease
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _kCFAllocatorDefault
+ _kIOMainPortDefault
CStrings:
+ "\x01\x12\xf0!q\x81"
+ "-[FPDXPCServicer getSavedDiagnosticsFor:completionHandler:]"
+ "-[FPDXPCServicer getSavedDiagnosticsFor:completionHandler:]_block_invoke"
+ "-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]"
+ "-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke"
+ "ConfigurationStoreRefreshInterval"
+ "FPDConfigurationStore refreshQueue"
+ "IODeviceTree:/filesystems"
+ "[DEBUG] Added observer: %@"
+ "[DEBUG] Callback = %@"
+ "[DEBUG] First: %@"
+ "[DEBUG] Updating %@ from %@ to %@"
+ "[DEBUG] Updating %@ from %lld to %lld"
+ "[DEBUG] Will callback %lu objects"
+ "[ERROR] Couldn't check if eAPFS is supported on the device"
+ "[ERROR] getSavedDiagnostics not supported in dead backend"
+ "[ERROR] getSavedDiagnostics not supported in extension backend"
+ "[INFO] [Trial] experiment: %@, treatment: %@"
+ "[INFO] [Trial] factor pack: %@, rollout: %@, ramp: %@"
+ "[NOTICE] [%{public}@] %{public}@: cancelling extension request"
+ "[NOTICE] [%{public}@] %{public}@: dealloc %{public}@"
+ "[NOTICE] [%{public}@] starting extension request %{public}@"
+ "[NOTICE] eAPFS is NOT supported on the device"
+ "[NOTICE] eAPFS is supported on the device"
+ "__test__diagnostic__"
+ "__test_only_refresh"
+ "_observers"
+ "_refreshQueue"
+ "addObserver:"
+ "com.apple.private.fileprovider.read-diagnostic-metadata"
+ "didUpdateConfiguration:"
+ "e-apfs"
+ "factorPackId"
+ "forceFSIngestionForItemID:request:completionHandler:"
+ "forceIngestionForItemID:request:completionHandler:"
+ "getSavedDiagnostics:"
+ "getSavedDiagnosticsFor:completionHandler:"
+ "launchFeedbackForDomain:itemIdentifier:triggeringError:when:useDiagnostic:completionHandler:"
+ "loadTrialClient"
+ "missing invalidation"
+ "rampId"
+ "refresh"
+ "rolloutId"
+ "rolloutIdentifiersWithNamespaceName:"
+ "supportsEAPFS"
+ "test_provider"
+ "triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:"
+ "v48@0:8@\"NSURL\"16@\"NSError\"24B32B36@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24B32B36@?40"
+ "v60@0:8@\"FPDDomain\"16@\"NSString\"24@\"NSError\"32@\"NSDate\"40B48@?<v@?@\"NSError\">52"
- "\x01\xf03q\x81"
- "-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:completionHandler:]"
- "-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:completionHandler:]_block_invoke"
- "T@\"NSString\",R,N,V_trialExperiment"
- "T@\"NSString\",R,N,V_trialTreatment"
- "[INFO] Trial Treatment is %@"
- "_trialExperiment"
- "_trialTreatment"
- "forceFSIngestionForItemID:completionHandler:"
- "launchFeedbackForDomain:itemIdentifier:triggeringError:completionHandler:"
- "trialExperiment"
- "trialTreatment"
- "triggerDiagnosticsFor:triggeringError:uiOnly:completionHandler:"
- "v44@0:8@\"NSURL\"16@\"NSError\"24B32@?<v@?@\"NSError\">36"
- "v48@0:8@\"FPDDomain\"16@\"NSString\"24@\"NSError\"32@?<v@?@\"NSError\">40"

```
