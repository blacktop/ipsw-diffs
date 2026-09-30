## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-1527.80.3.0.0
-  __TEXT.__text: 0x65c58
-  __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_stubs: 0x94c0
-  __TEXT.__objc_methlist: 0x3f34
+1527.100.24.0.0
+  __TEXT.__text: 0x6a238
+  __TEXT.__auth_stubs: 0x16c0
+  __TEXT.__objc_stubs: 0x94a0
+  __TEXT.__objc_methlist: 0x3eec
   __TEXT.__const: 0x1d4
-  __TEXT.__cstring: 0x10841
-  __TEXT.__objc_classname: 0x3a7
+  __TEXT.__cstring: 0x10a10
+  __TEXT.__objc_classname: 0x395
   __TEXT.__objc_methtype: 0x1752
-  __TEXT.__gcc_except_tab: 0x1268
-  __TEXT.__objc_methname: 0xa780
-  __TEXT.__oslogstring: 0x900e
+  __TEXT.__gcc_except_tab: 0x1110
+  __TEXT.__objc_methname: 0xa757
+  __TEXT.__oslogstring: 0x8d8c
   __TEXT.__ustring: 0x4e8
-  __TEXT.__unwind_info: 0x11d0
-  __DATA_CONST.__auth_got: 0xb80
+  __TEXT.__unwind_info: 0x1308
+  __DATA_CONST.__auth_got: 0xb70
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x13f8
-  __DATA_CONST.__cfstring: 0x11120
-  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__const: 0x1430
+  __DATA_CONST.__cfstring: 0x11340
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xdf8
-  __DATA_CONST.__objc_arrayobj: 0x1338
+  __DATA_CONST.__objc_arraydata: 0xe20
+  __DATA_CONST.__objc_arrayobj: 0x1368
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x52b0
+  __DATA.__objc_const: 0x5220
   __DATA.__objc_selrefs: 0x29f0
   __DATA.__objc_ivar: 0x470
-  __DATA.__objc_data: 0xc30
+  __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x2d0
   __DATA.__bss: 0x280
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 373AA782-8255-3D7B-AEB8-A13EB44184A4
-  Functions: 1775
-  Symbols:   500
-  CStrings:  7467
+  UUID: 7A98E3B0-E837-383A-94C6-7BC65DE7F85E
+  Functions: 1795
+  Symbols:   498
+  CStrings:  7497
 
Symbols:
+ _launch_get_user_context
+ _posix_spawnattr_setauditsessionport_np
+ _posix_spawnattr_setexceptionports_np
+ _posix_spawnattr_setspecialport_np
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ " failed to run as there is no logged-in user.\n"
+ "--mode"
+ "/private/var/mobile/Library/Preferences/.GlobalPreferences_m.plist"
+ "/usr/bin/searchdiagnose"
+ "/usr/local/bin/aidreport"
+ "/usr/local/bin/skdump"
+ "CSCoordinator: %s: config not found for '%@', returning default result"
+ "CSCoordinator: %s: found %lu configs (>1). Configs found for:"
+ "CSCoordinator: Failed to allocate CSSessionConfig object"
+ "CSCoordinator: nil diagnosticID passed to %s - returning default result"
+ "CSDisplayProxy: Found device %{public}s"
+ "CSDisplayProxy: On iOS, but not an iPhone or iPad. Returning no proxies"
+ "CSDisplayProxy: Received canceling, ending browsing"
+ "CSDisplayProxy: got nil device from from browsing SPI with canceling == false"
+ "CSDisplayProxy: timed out (%lus) waiting for browsing to finish"
+ "CSRemoteXPCProxy: \t%s"
+ "CSRemoteXPCProxy: %{public}s: conn started"
+ "CSRemoteXPCProxy: %{public}s: current config prevents accepting RemoteXPC requests. Cancelling conn"
+ "CSRemoteXPCProxy: %{public}s: initiating remote connection"
+ "CSRemoteXPCProxy: %{public}s: remote server initialized."
+ "CSRemoteXPCProxy: %{public}s: unexpected type (%{public}s); cancelling conn"
+ "CSRemoteXPCProxy: Collecting all trusted, adding all uuids"
+ "CSRemoteXPCProxy: Failed to get path basename. Not sending file to remote"
+ "CSRemoteXPCProxy: Failed to parse device uuid for '%s'"
+ "CSRemoteXPCProxy: No srcPath sent from remote"
+ "CSRemoteXPCProxy: Prioritized device '%{public}s' for uuid '%{public}s'"
+ "CSRemoteXPCProxy: Sorted devices:"
+ "CSRemoteXPCProxy: Trying to fetch service (%{public}s) for unconnected device (%{public}s)"
+ "CSRemoteXPCProxy: Trying to prioritize an empty device list!"
+ "CSRemoteXPCProxy: got nil device from from browsing SPI with canceling == false"
+ "CSRemoteXPCProxy: nil device passed into _initWithDevice"
+ "CSRemoteXPCProxy: timed out (%lus) waiting for browsing to finish"
+ "Demo ToolBox"
+ "Demo Toolbox"
+ "Failed to get user context for uid %d: %s"
+ "Failed to set audit session port for uid %d: %s"
+ "Failed to set exception port for uid %d: %s"
+ "Failed to set special port for uid %d: %s"
+ "Got path %{public}@ for pid %d"
+ "LanguagePrefs"
+ "No user with uid %d exists."
+ "SpotlightKnowledge"
+ "TI,V_targetBootstrapUid"
+ "_copyGlobalPreferences"
+ "_error.txt"
+ "_targetBootstrapUid"
+ "bgst"
+ "bgst.txt"
+ "com.apple.sysdiagnose.cosysdiagnose.trusted"
+ "com.apple.sysdiagnose.cosysdiagnose.untrusted"
+ "device:hasService:"
+ "errors/searchdiagnose.txt"
+ "getAIDReportContainers"
+ "inspect"
+ "logs/Search"
+ "logs/SpotlightKnowledge"
+ "q24@?0@\"OS_remote_device\"8@\"OS_remote_device\"16"
+ "searchdiagnose"
+ "setTargetBootstrapUid:"
+ "skdump.json"
+ "targetBootstrapUid"
+ "trusted"
+ "untrusted"
- "/usr/local/bin/hidreport"
- "/usr/local/bin/search_diagnose.sh"
- "CSCoordinator: Trying to wait on NULL hostWaitGroup. File transfer probably already finished"
- "CSCoordinator: While remote-initiated, timed out waiting for remote co-sysdiagnose (hostWaitGroup)"
- "CSCoreDeviceProxy"
- "CSCoreDeviceProxy: Cancelling remote connection"
- "CSCoreDeviceProxy: Connection started."
- "CSCoreDeviceProxy: Detected --collectAllTrusted flag, beginning to find all proxies of connected devices"
- "CSCoreDeviceProxy: Did not detect the --collectAllTrusted flag, skipping proxies"
- "CSCoreDeviceProxy: Finished browsing. Found %lu devices (%lu usable) of type %s"
- "CSCoreDeviceProxy: Found device %@"
- "CSCoreDeviceProxy: Initiating remote connection"
- "CSCoreDeviceProxy: Proxy is not host, skipping browseDevices"
- "CSCoreDeviceProxy: Remote server initialized."
- "CSCoreDeviceProxy: timeout target requested. Using %lus"
- "CSDisplayProxy: Found device %@"
- "CSDisplayProxy: On iOS, but not iPhone, iPad, or darwinOS. Returning no proxies"
- "CSRemoteXPCProxy: Cancelling remote connection"
- "CSRemoteXPCProxy: Connection started."
- "CSRemoteXPCProxy: Current configuration prevents device from accepting RemoteXPC requests. Cancelling remote connection"
- "CSRemoteXPCProxy: Deduced response type: failure"
- "CSRemoteXPCProxy: Deduced response type: success. Asking for file from remote"
- "CSRemoteXPCProxy: Device %s not connected"
- "CSRemoteXPCProxy: Failed to parse device uuid - not appending remote UUID"
- "CSRemoteXPCProxy: Found service '%s' on connected device '%s'. Device is usable"
- "CSRemoteXPCProxy: Initiating remote connection"
- "CSRemoteXPCProxy: Remote server initialized."
- "CSRemoteXPCProxy: Service '%s' not found for device %s"
- "CoreDeviceProxyHost"
- "CoreDeviceProxyRemote"
- "Error: CSCoordinator: %s: config not found for '%@', returning default result"
- "Error: CSCoordinator: %s: found %lu configs (>1). Configs found for:"
- "Error: CSCoordinator: Failed to allocate CSSessionConfig object"
- "Error: CSCoordinator: failed to create hostWaitGroup. Failing to startRemoteInitiatedFlow"
- "Error: CSCoordinator: nil diagnosticID passed to %s - returning default result"
- "Error: CSCoreDeviceProxy: got nil device from from browsing SPI with canceling == false"
- "Error: CSCoreDeviceProxy: timed out (%lus) waiting for browsing to finish"
- "Error: CSDisplayProxy: got nil device from from browsing SPI with canceling == false"
- "Error: CSDisplayProxy: timed out (%lus) waiting for browsing to finish"
- "Error: CSRemoteXPCProxy: Failed to get path basename. Not sending file to remote"
- "Error: CSRemoteXPCProxy: No srcPath sent from remote"
- "Error: CSRemoteXPCProxy: nil device passed into _initWithDevice"
- "Got path %@ for pid %d"
- "SearchDiagnose"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_hostWaitGroup"
- "_hostWaitGroup"
- "com.apple.sysdiagnose.cosysdiagnose.CSCoreDeviceProxy"
- "com.apple.sysdiagnose.cosysdiagnose.CSRemoteXPCProxy"
- "errors/search_diagnose.txt"
- "getHIDReportContainers"
- "hostWaitGroup"
- "logs/SearchDiagnose"
- "safeLeaveHostWaitGroup"
- "setHostWaitGroup:"
- "triggerCoSysdiagnoseWithParams:forServiceName:"

```
