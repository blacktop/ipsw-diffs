## PersistentConnection

> `/System/Library/PrivateFrameworks/PersistentConnection.framework/Versions/A/PersistentConnection`

```diff

-562.100.1.0.0
-  __TEXT.__text: 0x18bfc
-  __TEXT.__objc_methlist: 0x1cf0
-  __TEXT.__const: 0x218
-  __TEXT.__cstring: 0x1216
-  __TEXT.__oslogstring: 0x2e71
+562.200.1.0.0
+  __TEXT.__text: 0x1960c
+  __TEXT.__objc_methlist: 0x1d20
+  __TEXT.__const: 0x240
+  __TEXT.__cstring: 0x1239
+  __TEXT.__oslogstring: 0x3466
   __TEXT.__gcc_except_tab: 0xc84
-  __TEXT.__unwind_info: 0xca0
+  __TEXT.__unwind_info: 0xcc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf10
+  __DATA_CONST.__objc_selrefs: 0xf18
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0x660
   __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0x6478
+  __AUTH_CONST.__objc_const: 0x64e0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x350

   - /System/Library/PrivateFrameworks/CommonUtilities.framework/Versions/A/CommonUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 659
+  Functions: 666
   Symbols:   360
-  CStrings:  352
+  CStrings:  361
 
CStrings:
+ "PCInterfaceMonitor state dump: internal:nil"
+ "PCInterfaceUsabilityMonitor[%{public}@] state dump: usable:%{BOOL}d historicallyUsable:%{BOOL}d pathSatisfied:%{BOOL}d linkQuality:%{public}@(%d) constraint:%ld interface:%{public}s(%u) delegateInterface:%{public}s(%u) pathEvaluator:%{public}s lqDynamicStore:%{public}s lqKey:%{public}@ trackUsability:%{BOOL}d offTransitions:%lu/%lu within:%.0fs newestOffTransitionAge:%.1fs"
+ "PCNonCellularUsabilityMonitor state dump: usable:%{BOOL}d historicallyUsable:%{BOOL}d demoOverrideInterface:%{public}@ linkQuality:%{public}@(%d) previousLinkQuality:%d trackUsability:%{BOOL}d offThreshold:%lu trackedInterval:%.0fs"
+ "PCPersistentInterfaceManager state dump: isWWANInterfaceUp:%{BOOL}d recomputed:%{BOOL}d isWWANInterfaceDataActive:%{BOOL}d hasWWANStatusIndicator:%{BOOL}d avoidWWANOnCall:%{BOOL}d inCallOverrideTimer:%{BOOL}d isInCall:%{BOOL}d isWiFiUsable:%{BOOL}d wwanInterfaceName:%{public}@ isWWANInterfaceSuspended:%{BOOL}d isWWANInterfaceActivationPermitted:%{BOOL}d interfaceAssertion:%{public}s isWWANInterfaceInProlongedHighPowerState:%{BOOL}d isPowerStateDetectionSupported:%{BOOL}d ctIsWWANInHomeCountry:%{BOOL}d ctClient:%{public}s dataSimSlotID:%d lastActivationAge:%.0fs"
+ "PCWWANUsabilityMonitor state dump: usable:%{BOOL}d historicallyUsable:%{BOOL}d interfaceMonitor:%{public}s wwanContextID:%ld isInCall:%{BOOL}d isInHighPowerState:%{BOOL}d currentRAT:%d dataBearerSoMask:%u ctClient:%{public}s dataSimSlotID:%d trackUsability:%{BOOL}d offThreshold:%lu trackedInterval:%.0fs"
+ "held"
+ "live"
+ "nil"
+ "nil - no PDP context"
```
