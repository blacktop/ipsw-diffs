## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-107.0.12.0.0
-  __TEXT.__text: 0x2f458
+107.0.12.0.1
+  __TEXT.__text: 0x2f8f4
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x37cc
+  __TEXT.__objc_methlist: 0x37fc
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x154a
-  __TEXT.__oslogstring: 0x6d76
+  __TEXT.__cstring: 0x15bc
+  __TEXT.__oslogstring: 0x6de4
   __TEXT.__gcc_except_tab: 0x24c
   __TEXT.__unwind_info: 0x7f0
   __TEXT.__objc_classname: 0x5c5
-  __TEXT.__objc_methname: 0x8f28
+  __TEXT.__objc_methname: 0x8fc4
   __TEXT.__objc_methtype: 0x1154
-  __TEXT.__objc_stubs: 0x6760
+  __TEXT.__objc_stubs: 0x67e0
   __DATA_CONST.__got: 0x300
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1df8
+  __DATA_CONST.__objc_selrefs: 0x1e18
   __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2100
-  __AUTH_CONST.__objc_const: 0x5338
+  __AUTH_CONST.__cfstring: 0x21a0
+  __AUTH_CONST.__objc_const: 0x5398
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x424
+  __DATA.__objc_ivar: 0x42c
   __DATA.__data: 0xba0
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75A9A263-6C6B-3953-AA0B-767114CF0997
-  Functions: 1015
-  Symbols:   3762
-  CStrings:  2483
+  UUID: 91D56DD3-D13E-3F2E-9D71-08BAE364D05C
+  Functions: 1019
+  Symbols:   3776
+  CStrings:  2502
 
Symbols:
+ -[SAMonitoringSession foundAtLocation]
+ -[SAMonitoringSession setFoundAtLocation:]
+ -[SATravelTypeClassifier setUserActivityType:]
+ -[SATravelTypeClassifier userActivityType]
+ _OBJC_IVAR_$_SAMonitoringSession._foundAtLocation
+ _OBJC_IVAR_$_SATravelTypeClassifier._userActivityType
+ _objc_msgSend$foundAtLocation
+ _objc_msgSend$setFoundAtLocation:
+ _objc_msgSend$setUserActivityType:
+ _objc_msgSend$userActivityType
CStrings:
+ "TB,N,V_foundAtLocation"
+ "TQ,N,V_userActivityType"
+ "_foundAtLocation"
+ "_userActivityType"
+ "foundAtLocation"
+ "motionActivityType"
+ "motionActivityTypeDuringAlert"
+ "motionActivityTypeDuringReunion"
+ "numSafeLocations"
+ "setFoundAtLocation:"
+ "setUserActivityType:"
+ "userActivityType"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager device found at location during visit\", \"uuid\":\"%{private}@\"}"

```
