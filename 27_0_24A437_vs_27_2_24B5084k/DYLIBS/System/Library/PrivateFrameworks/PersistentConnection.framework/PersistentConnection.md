## PersistentConnection

> `/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection`

```diff

-562.100.1.0.0
-  __TEXT.__text: 0x20858
-  __TEXT.__objc_methlist: 0x1fb8
-  __TEXT.__const: 0x250
+562.200.1.0.0
+  __TEXT.__text: 0x2120c
+  __TEXT.__objc_methlist: 0x1fe8
+  __TEXT.__const: 0x278
   __TEXT.__gcc_except_tab: 0xd20
-  __TEXT.__cstring: 0x1b3a
-  __TEXT.__oslogstring: 0x4868
-  __TEXT.__unwind_info: 0xf00
+  __TEXT.__cstring: 0x1b4e
+  __TEXT.__oslogstring: 0x4e5d
+  __TEXT.__unwind_info: 0xf20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a0
+  __DATA_CONST.__objc_selrefs: 0x10a8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__got: 0x248
   __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__cfstring: 0x1660
-  __AUTH_CONST.__objc_const: 0x6eb0
+  __AUTH_CONST.__objc_const: 0x6f18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 807
-  Symbols:   2023
-  CStrings:  549
+  Functions: 814
+  Symbols:   2031
+  CStrings:  557
 
Symbols:
+ -[PCInterfaceMonitor logDetailedState]
+ -[PCInterfaceUsabilityMonitor logDetailedState]
+ -[PCNonCellularUsabilityMonitor logDetailedState]
+ -[PCPersistentInterfaceManager logDetailedState]
+ -[PCWWANUsabilityMonitor logDetailedState]
+ ___42-[PCWWANUsabilityMonitor logDetailedState]_block_invoke
+ ___49-[PCNonCellularUsabilityMonitor logDetailedState]_block_invoke
+ _objc_msgSend$logDetailedState
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
- "EmperorPenguin"
```
