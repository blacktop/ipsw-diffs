## mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

-4025.210.2.0.0
-  __TEXT.__text: 0x3ad82c
+4025.300.6.0.0
+  __TEXT.__text: 0x3afa10
   __TEXT.__auth_stubs: 0x6100
-  __TEXT.__objc_stubs: 0x23c80
-  __TEXT.__objc_methlist: 0x1428c
-  __TEXT.__objc_methname: 0x38d67
-  __TEXT.__cstring: 0x1d4eb
-  __TEXT.__objc_classname: 0x2cab
+  __TEXT.__objc_stubs: 0x23f40
+  __TEXT.__objc_methlist: 0x1441c
+  __TEXT.__objc_methname: 0x39286
+  __TEXT.__cstring: 0x1d7bb
+  __TEXT.__objc_classname: 0x2ccd
   __TEXT.__objc_methtype: 0x6c75
   __TEXT.__const: 0xdaf0
-  __TEXT.__gcc_except_tab: 0x6384
-  __TEXT.__oslogstring: 0x22659
+  __TEXT.__gcc_except_tab: 0x63f4
+  __TEXT.__oslogstring: 0x226c9
   __TEXT.__dlopen_cstrs: 0x224
   __TEXT.__swift5_typeref: 0x4c17
   __TEXT.__swift5_capture: 0x4e20
-  __TEXT.__constg_swiftt: 0x5e64
+  __TEXT.__constg_swiftt: 0x5e74
   __TEXT.__swift5_reflstr: 0x4003
   __TEXT.__swift5_fieldmd: 0x3abc
   __TEXT.__swift5_types: 0x3f0

   __TEXT.__swift5_proto: 0x870
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x58
-  __TEXT.__unwind_info: 0xb540
+  __TEXT.__unwind_info: 0xb5f0
   __TEXT.__eh_frame: 0x61bc
   __DATA_CONST.__auth_got: 0x3090
-  __DATA_CONST.__got: 0x2c10
+  __DATA_CONST.__got: 0x2c18
   __DATA_CONST.__auth_ptr: 0xc48
-  __DATA_CONST.__const: 0x1adb0
-  __DATA_CONST.__cfstring: 0xd740
-  __DATA_CONST.__objc_classlist: 0x9f8
+  __DATA_CONST.__const: 0x1aea8
+  __DATA_CONST.__cfstring: 0xd900
+  __DATA_CONST.__objc_classlist: 0xa00
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x5a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_intobj: 0x720
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0x24f68
-  __DATA.__objc_selrefs: 0xb5f0
-  __DATA.__objc_ivar: 0x1614
-  __DATA.__objc_data: 0x8b68
-  __DATA.__data: 0xaae0
-  __DATA.__bss: 0xf190
+  __DATA.__objc_const: 0x251e8
+  __DATA.__objc_selrefs: 0xb6b0
+  __DATA.__objc_ivar: 0x163c
+  __DATA.__objc_data: 0x8bc8
+  __DATA.__data: 0xaad0
+  __DATA.__bss: 0xf1b0
   __DATA.__common: 0x2a0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 58EF1197-6866-389D-B47B-FB93086C408F
-  Functions: 16079
-  Symbols:   3253
-  CStrings:  16230
+  UUID: F7A4C760-1C24-35E4-98F6-EE43DAD74269
+  Functions: 16140
+  Symbols:   3254
+  CStrings:  16305
 
Symbols:
+ __MRCriticalSectionMonitorDidBecomeCriticalNotification
+ __MRCriticalSectionMonitorDidStopBeingCriticalNotification
- _OBJC_CLASS_$_MRNotification
CStrings:
+ "    Suspended\n"
+ "    lastActiveSystemEndpointAssertionDate=%@ (%lf seconds ago)\n"
+ "    numberOfActiveSystemEndpointAssertions=%ld (\n"
+ "    numberOfCriticalSectionMonitors=%ld\n"
+ "@16@?0@\"MRAVDistantOutputDevice\"8"
+ "ApplicationDisabled"
+ "Assertion"
+ "Found multiple hosts for baseGroupID: %@"
+ "MRDMediaRemoteClientActiveSystemEndpointAssertionDidChange"
+ "MRDMediaRemoteServerNotification"
+ "MRXPC_NOTIFICATION_USERINFO_DATA_KEY"
+ "Multiple hostsForBaseGroupID"
+ "T@\"NSDictionary\",R,N,V_userInfo"
+ "T@\"NSMapTable\",&,N,V_sessionManagementScreenAssertions"
+ "T@\"NSObject<OS_xpc_object>\",R,N,V_xpcMessage"
+ "TB,N,GisSuspended"
+ "TB,N,V_hasEffectiveActiveSystemEndpointAssertion"
+ "TB,R,N,GisMonitoringCriticalSections"
+ "TB,R,N,V_isCriticalSectionActive"
+ "Tq,R,N,V_options"
+ "[MRDGroupSessionManager] Adding new assertion: %@ with ID: %@"
+ "_createNotificationMessage:userInfo:"
+ "_handleActiveSystemEndpointAcquireAssertionMessage:fromClient:"
+ "_handleActiveSystemEndpointAssertionDidChange:"
+ "_handleActiveSystemEndpointReleaseAssertionMessage:fromClient:"
+ "_handleCriticalSectionRegisterMonitor:fromClient:"
+ "_handleCriticalSectionUnregisterMonitor:fromClient:"
+ "_hasEffectiveActiveSystemEndpointAssertion"
+ "_isCriticalSectionActive"
+ "_lastActiveSystemEndpointAssertionDate"
+ "_numberOfActiveSystemEndpointAssertions"
+ "_numberOfCriticalSectionMonitors"
+ "_onSerialQueue_calculateHasActiveSystemEndpointAssertion"
+ "_onSerialQueue_reevaluateEffectiveActiveSystemEndpointAssertion"
+ "_sessionManagementScreenAssertions"
+ "_suspended"
+ "_userInfo"
+ "_xpcMessage"
+ "acquireActiveSystemEndpointAssertion"
+ "activeSystemEndpointAssertionGracePeriodInternal"
+ "aquireCriticalSectionMonitor"
+ "assertSessionManagementScreenVisibleWithID:"
+ "calculateIsCriticalSectionActive"
+ "client asserting"
+ "com.apple.mediaremote.active-system-endpoint-assertion"
+ "com.apple.mediaremote.critical-section-creation"
+ "com.apple.mediaremote.critical-section-monitor"
+ "com.apple.mediaremote.send-mr-command.application-disabled"
+ "createAssertionWithReason:duration:id:"
+ "createAssertionWithReason:id:"
+ "errorDescription"
+ "errorFailureDescription"
+ "hasActiveSystemEndpointAssertion"
+ "hasEffectiveActiveSystemEndpointAssertion"
+ "initWithName:options:userInfo:"
+ "isCriticalSectionActive"
+ "isMonitoringCriticalSections"
+ "isSuspended"
+ "monitoringCriticalSections"
+ "notificationByReplacingUserInfo:"
+ "postClientNotification:predicate:"
+ "releaseActiveSystemEndpointAssertion"
+ "releaseAllActiveSystemEndpointAssertions"
+ "releaseCriticalSectionMonitor"
+ "sessionManagementScreenAssertions"
+ "setHasEffectiveActiveSystemEndpointAssertion:"
+ "setIsCriticalSectionActive:"
+ "setSessionManagementScreenAssertions:"
+ "setSuspended:"
+ "strongToWeakObjectsMapTable"
+ "suspended"
+ "v40@0:8@16d24@32"
+ "\xf0q"
- "T@\"MRGroupSessionAssertion\",&,N,V_participantManagementVisibleAssertion"
- "Tq,N,V_sessionManagementScreenVisibleCount"
- "_isACriticalSectionActive"
- "_participantManagementVisibleAssertion"
- "_sessionManagementScreenVisibleCount"
- "assertSessionManagementScreenVisible"
- "initWithNotification:userInfo:"
- "participantManagementVisibleAssertion"
- "releaseSessionManagementScreenVisibleAssertion"
- "sessionManagementScreenVisibleCount"
- "setParticipantManagementVisibleAssertion:"
- "setSessionManagementScreenVisibleCount:"
- "\xf0A"

```
