## wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

-236.0.0.0.0
-  __TEXT.__text: 0x20a234
-  __TEXT.__auth_stubs: 0x3d40
-  __TEXT.__objc_stubs: 0xa5e0
+236.1.0.0.0
+  __TEXT.__text: 0x20ae50
+  __TEXT.__auth_stubs: 0x3d30
+  __TEXT.__objc_stubs: 0xa760
   __TEXT.__init_offsets: 0x1c8
-  __TEXT.__objc_methlist: 0x559c
-  __TEXT.__gcc_except_tab: 0x1ffd0
+  __TEXT.__objc_methlist: 0x564c
+  __TEXT.__gcc_except_tab: 0x20298
   __TEXT.__const: 0xdd9f
-  __TEXT.__cstring: 0x11392
-  __TEXT.__oslogstring: 0x1dfe4
-  __TEXT.__objc_methname: 0x10340
-  __TEXT.__objc_classname: 0xbf6
-  __TEXT.__objc_methtype: 0x2eaa
+  __TEXT.__cstring: 0x113f2
+  __TEXT.__oslogstring: 0x1e0a4
+  __TEXT.__objc_methname: 0x10543
+  __TEXT.__objc_classname: 0xc17
+  __TEXT.__objc_methtype: 0x2eee
   __TEXT.__swift5_typeref: 0x1104
   __TEXT.__constg_swiftt: 0x1a3c
   __TEXT.__swift5_reflstr: 0x31e5

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x174
   __TEXT.__swift_as_ret: 0x100
-  __TEXT.__unwind_info: 0xadc0
+  __TEXT.__unwind_info: 0xae38
   __TEXT.__eh_frame: 0x25bc
-  __DATA_CONST.__auth_got: 0x1eb8
-  __DATA_CONST.__got: 0xd70
+  __DATA_CONST.__auth_got: 0x1eb0
+  __DATA_CONST.__got: 0xd80
   __DATA_CONST.__auth_ptr: 0x420
-  __DATA_CONST.__const: 0xe7a8
-  __DATA_CONST.__cfstring: 0x4e20
+  __DATA_CONST.__const: 0xe7e8
+  __DATA_CONST.__cfstring: 0x4ea0
   __DATA_CONST.__objc_classlist: 0x3f0
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x250

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0xdfc0
-  __DATA.__objc_selrefs: 0x30c0
-  __DATA.__objc_ivar: 0x80c
+  __DATA.__objc_const: 0xe040
+  __DATA.__objc_selrefs: 0x3140
+  __DATA.__objc_ivar: 0x814
   __DATA.__objc_data: 0x2ef8
-  __DATA.__data: 0x3b70
+  __DATA.__data: 0x3bd0
   __DATA.__bss: 0x3bc8
   __DATA.__common: 0x3a8
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
+  - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C889D1C6-999A-3038-A7A7-2435C5567AC2
-  Functions: 9238
-  Symbols:   1534
-  CStrings:  7921
+  UUID: 3315291C-DB2C-37BC-AFE2-36AFDD026E33
+  Functions: 9257
+  Symbols:   1535
+  CStrings:  7958
 
Symbols:
+ _OBJC_CLASS_$_NWNetworkOfInterest
+ _OBJC_CLASS_$_NWNetworkOfInterestManager
- _nw_release
CStrings:
+ "236.1"
+ "236.1~54"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_nw_path_monitor>\""
+ "@\"NWNetworkOfInterestManager\""
+ "B16@?0@\"NSObject<OS_nw_interface>\"8"
+ "NWNetworkOfInterestManagerDelegate"
+ "RatDataUsageMetric:#D NOI considerAlternate (RNF) update: %ld"
+ "RatDataUsageMetric:#D Started tracking NOI"
+ "RatDataUsageMetric:#D Stopped tracking NOI"
+ "RatDataUsageMetric:#D Stopped tracking all NOIs"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"NSObject<OS_nw_path_monitor>\",&,V_networkPathMonitor"
+ "T@\"NWNetworkOfInterestManager\",&,V_noiManager"
+ "Tq,R,V_rnfAdviceLevel"
+ "_noiManager"
+ "_rnfAdviceLevel"
+ "addObserver:forKeyPath:options:context:"
+ "considerAlternate"
+ "destroy"
+ "didStartTrackingNOI:"
+ "didStopTrackingAllNOIs:"
+ "didStopTrackingNOI:"
+ "initializeNOIManager"
+ "noiManager"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "removeObserver:forKeyPath:"
+ "rnfAdviceLevel"
+ "rnfAdviceLevelToString:"
+ "rnf_state"
+ "setNoiManager:"
+ "strong"
+ "trackNOIAnyForInterfaceType:options:"
+ "updateRNFAdviceLevelTo:"
+ "v16@?0@\"NSObject<OS_nw_path>\"8"
+ "v24@0:8@\"NSSet\"16"
+ "v24@0:8@\"NWNetworkOfInterest\"16"
+ "v24@?0@\"NWNetworkOfInterest\"8^B16"
+ "v48@0:8@16@24@32^v40"
+ "weak"
- "236"
- "236~174"
- "B16@?0^{nw_interface=}8"
- "T^{nw_path_monitor=},V_networkPathMonitor"
- "^{nw_path_monitor=}"
- "^{nw_path_monitor=}16@0:8"
- "v16@?0^{nw_path=}8"
- "v24@0:8^{nw_path=}16"
- "v24@0:8^{nw_path_monitor=}16"

```
