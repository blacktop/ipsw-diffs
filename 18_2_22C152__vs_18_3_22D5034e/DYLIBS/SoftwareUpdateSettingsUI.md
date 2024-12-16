## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-399.60.4.0.0
-  __TEXT.__text: 0xf32dc
+399.80.2.0.0
+  __TEXT.__text: 0xf3e58
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x40d0
-  __TEXT.__cstring: 0x983e
-  __TEXT.__oslogstring: 0x15724
+  __TEXT.__objc_methlist: 0x4120
+  __TEXT.__cstring: 0x988e
+  __TEXT.__oslogstring: 0x15834
   __TEXT.__gcc_except_tab: 0x3b48
   __TEXT.__dlopen_cstrs: 0x658
   __TEXT.__const: 0x6e
   __TEXT.__swift5_typeref: 0xc3
   __TEXT.__swift5_capture: 0xbc
-  __TEXT.__unwind_info: 0x16c0
+  __TEXT.__unwind_info: 0x16e0
   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_classname: 0x6f5
-  __TEXT.__objc_methname: 0xe3f5
-  __TEXT.__objc_methtype: 0x2437
-  __TEXT.__objc_stubs: 0x96a0
+  __TEXT.__objc_methname: 0xe514
+  __TEXT.__objc_methtype: 0x246f
+  __TEXT.__objc_stubs: 0x9740
   __DATA_CONST.__got: 0x6f0
   __DATA_CONST.__const: 0x92a8
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d60
+  __DATA_CONST.__objc_selrefs: 0x2d88
   __DATA_CONST.__objc_superrefs: 0x100
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x358
   __AUTH_CONST.__cfstring: 0x42c0
-  __AUTH_CONST.__objc_const: 0x9df8
+  __AUTH_CONST.__objc_const: 0x9e88
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x450
+  __DATA.__objc_ivar: 0x45c
   __DATA.__data: 0x990
   __DATA.__bss: 0x241
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2108
-  Symbols:   2514
-  CStrings:  3669
+  Functions: 2115
+  Symbols:   2521
+  CStrings:  3682
 
CStrings:
+ "\x14\x15"
+ "\x18\x12\x18"
+ "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager currentUIState: %{public}@ (%ld)\n\tpresentingStatefulDescriptor: %{public}@ (%p)\n\tpresentingAlternateStatefulDescriptor: %{public}@ (%p)\n\ttargetedUpdateDownload: %{public}@ (%p)\n\ttargetedUpdateScheduled: %{public}s\n\nSoftwareUpdatePane invoked via URL but no supported option passed in. Nothing to do here. Available options: path, ShowLatestUpdatePane, PerformAction"
+ "%s: DefaultAudience descriptor: %{public}@\nShowLatestUpdatePane is YES, going to try use latestUpdate value from the scan result"
+ "%s: DefaultAudience descriptor: %{public}@\nlatestUpdateStatefulDescriptor is nil. Unable to use it for the ShowLatestUpdatePane flag"
+ "<%@: %p, \n\tscanOptions: %@\n\toperationError: %@\n\tpreferredDescriptor: %@ (%p), \n\talternateDescriptor: %@ (%p), \n\tlatestDescriptor: %@ (%p), \n\tscanError: %@, \n\temptyScanResults: %s, \n\tpreferredUpdateDownloadable: %s, \n\talternateUpdateDownloadable: %s, \n\tpreferredUpdateDownloadError: %@, \n\talternateUpdateDownloadError: %@, \n\tagreementManager: %@, \n\tisClearingSpaceForDownload: %d, \n\tcurrentDownload: %@, \n\tmdmPathRestrictions: %@ (%ld), \n\tisDelayingUpdate: %s\n\tisRollingBack: %s\n\trollbackDescriptor: %p\n\tcurrentSeedingDevice: %p\n\tbetaPrograms: %p (count: %ld)\n\tenrolledBetaProgram: %p\n\tautoUpdateScheduled: %s\n\tisUpdateReadyForInstallation: %s\n\tupdateInstallationError: %@>"
+ "<%@: %p, \n\tscanUUID: %@, \n\tpreferredDescriptor: %@ (%p), \n\talternateDescriptor: %@ (%p), \n\tlatestUpdateDescriptor: %@ (%p), \n\tscanError: %@, \n\temptyScanResults: %s, \n\tpreferredUpdateDownloadable: %s, \n\talternateUpdateDownloadable: %s, \n\tpreferredUpdateDownloadError: %@, \n\talternateUpdateDownloadError: %@, \n\tagreementManager: %@, \n\tisClearingSpaceForDownload: %d, \n\tcurrentDownload: %@, \n\tmdmPathRestrictions: %@ (%ld), \n\tddmDeclaration: %p\n\tisDelayingUpdate: %s\n\tisRollingBack: %s\n\trollbackDescriptor: %p\n\tcurrentSeedingDevice: %p\n\tbetaPrograms: %p (count: %ld)\n\tenrolledBetaProgram: %p\n\tautoUpdateScheduled: %s (%p)\n\tisUpdateReadyForInstallation: %s\n\tupdateInstallationError: %@>"
+ "<%@: %p> { type = %@, %@currentState = %@ (%lu), descriptor = %@ (%p), updateDownloadable = %s, updateDownloadError = %@, isLatest = %s, owner = %p }"
+ "@64@0:8@16@24@32@40@48@56"
+ "ShowLatestUpdatePane"
+ "T@\"SUDescriptor\",&,N,V_latestDescriptor"
+ "TB,V_isLatestUpdate"
+ "_isLatestUpdate"
+ "_latestDescriptor"
+ "initWithPreferredDescriptor:alternateDescriptor:andLatestDescriptor:"
+ "initWithPreferredDescriptor:alternateDescriptor:andLatestDescriptor:previouslyDiscoveredDownloadedUpdate:encounteredError:"
+ "initWithPreferredDescriptor:alternateDescriptor:andLatestDescriptor:previouslyDiscoveredDownloadedUpdate:previouslyDiscoveredAutoInstallOperation:encounteredError:"
+ "isLatestUpdate"
+ "latestDescriptor"
+ "latestUpdateStatefulDescriptor"
+ "refreshScanResultsWithPreferredUpdate:alternateUpdate:latestUpdate:options:completionHandler:"
+ "refreshScanResultsWithPreferredUpdate:alternateUpdate:latestUpdate:options:previouslyDiscoveredDownload:encounteredError:completionHandler:"
+ "refreshScanResultsWithPreferredUpdate:alternateUpdate:latestUpdate:options:previouslyDiscoveredDownload:previouslyDiscoveredAutoInstallOperation:encounteredError:completionHandler:"
+ "setIsLatestUpdate:"
+ "setLatestDescriptor:"
+ "v56@0:8@16@24@32@40@?48"
+ "v80@0:8@16@24@32@40@48@56@64@?72"
- "\x13\x15"
- "\x17\x12\x18"
- "%s: Controller Checkpoint\n\tCaller: %{public}@ (%p)\n\tmanager currentUIState: %{public}@ (%ld)\n\tpresentingStatefulDescriptor: %{public}@ (%p)\n\tpresentingAlternateStatefulDescriptor: %{public}@ (%p)\n\ttargetedUpdateDownload: %{public}@ (%p)\n\ttargetedUpdateScheduled: %{public}s\n\nSoftwareUpdatePane invoked via URL but no supported option passed in. Nothing to do here. Available options: ShowDefaultAudiencePane, PerformAction"
- "<%@: %p, \n\tscanOptions: %@\n\toperationError: %@\n\tpreferredDescriptor: %@ (%p), \n\talternateDescriptor: %@ (%p), \n\tscanError: %@, \n\temptyScanResults: %s, \n\tpreferredUpdateDownloadable: %s, \n\talternateUpdateDownloadable: %s, \n\tpreferredUpdateDownloadError: %@, \n\talternateUpdateDownloadError: %@, \n\tagreementManager: %@, \n\tisClearingSpaceForDownload: %d, \n\tcurrentDownload: %@, \n\tmdmPathRestrictions: %@ (%ld), \n\tisDelayingUpdate: %s\n\tisRollingBack: %s\n\trollbackDescriptor: %p\n\tcurrentSeedingDevice: %p\n\tbetaPrograms: %p (count: %ld)\n\tenrolledBetaProgram: %p\n\tautoUpdateScheduled: %s\n\tisUpdateReadyForInstallation: %s\n\tupdateInstallationError: %@>"
- "<%@: %p, \n\tscanUUID: %@, \n\tpreferredDescriptor: %@ (%p), \n\talternateDescriptor: %@ (%p), \n\tscanError: %@, \n\temptyScanResults: %s, \n\tpreferredUpdateDownloadable: %s, \n\talternateUpdateDownloadable: %s, \n\tpreferredUpdateDownloadError: %@, \n\talternateUpdateDownloadError: %@, \n\tagreementManager: %@, \n\tisClearingSpaceForDownload: %d, \n\tcurrentDownload: %@, \n\tmdmPathRestrictions: %@ (%ld), \n\tddmDeclaration: %p\n\tisDelayingUpdate: %s\n\tisRollingBack: %s\n\trollbackDescriptor: %p\n\tcurrentSeedingDevice: %p\n\tbetaPrograms: %p (count: %ld)\n\tenrolledBetaProgram: %p\n\tautoUpdateScheduled: %s (%p)\n\tisUpdateReadyForInstallation: %s\n\tupdateInstallationError: %@>"
- "<%@: %p> { type = %@, %@currentState = %@ (%lu), descriptor = %@ (%p), updateDownloadable = %s, updateDownloadError = %@, owner = %p }"
- "ShowDefaultAudiencePane"
- "initWithPreferredDescriptor:andAlternateDescriptor:"
- "initWithPreferredDescriptor:andAlternateDescriptor:previouslyDiscoveredDownloadedUpdate:encounteredError:"
- "initWithPreferredDescriptor:andAlternateDescriptor:previouslyDiscoveredDownloadedUpdate:previouslyDiscoveredAutoInstallOperation:encounteredError:"
- "refreshScanResultsWithPreferredUpdate:alternateUpdate:options:completionHandler:"
- "refreshScanResultsWithPreferredUpdate:alternateUpdate:options:previouslyDiscoveredDownload:encounteredError:completionHandler:"
- "refreshScanResultsWithPreferredUpdate:alternateUpdate:options:previouslyDiscoveredDownload:previouslyDiscoveredAutoInstallOperation:encounteredError:completionHandler:"
- "v64@0:8@16@24@32@40@48@?56"

```
