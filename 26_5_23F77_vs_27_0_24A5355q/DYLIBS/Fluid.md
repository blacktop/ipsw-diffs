## Fluid

> `/System/Library/PrivateFrameworks/Fluid.framework/Fluid`

```diff

-58.4.1.0.0
-  __TEXT.__text: 0x14d8
-  __TEXT.__auth_stubs: 0xb0
+66.0.0.0.0
+  __TEXT.__text: 0x14ec
   __TEXT.__objc_methlist: 0x248
-  __TEXT.__const: 0xb8
+  __TEXT.__const: 0xa8
   __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x9
-  __TEXT.__objc_methname: 0x5c6
-  __TEXT.__objc_methtype: 0x727
-  __TEXT.__objc_stubs: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x60
   __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x44
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AD464508-2BCA-372D-B297-7D7E18EBD51D
+  UUID: F1A90DD2-88DE-3801-8C92-5FA09A64D0EC
   Functions: 75
   Symbols:   175
-  CStrings:  98
+  CStrings:  0
 
Functions:
~ -[FLSpring projectedTarget] : 52 -> 56
~ -[FLSpring _effectiveParameters] : 76 -> 92
CStrings:
- "@16@0:8"
- "@24@0:8d16"
- "B"
- "B16@0:8"
- "FLSpring"
- "TB,N,GisTracking,V_tracking"
- "TB,R,N,GisStable"
- "Td,D,N"
- "Td,N"
- "Td,N,V_maximumTarget"
- "Td,N,V_minimumTarget"
- "Td,N,V_projectionDeceleration"
- "Td,N,V_retargetImpulse"
- "Td,N,V_retargetResponseFraction"
- "Td,N,V_rubberbandFactor"
- "Td,N,V_rubberbandRange"
- "Td,N,V_timeFactor"
- "Td,R,D,N"
- "T{FLSpringParameters=dddd},N,V_offsetParameters"
- "T{FLSpringParameters=dddd},N,V_parameters"
- "T{FLSpringParameters=dddd},N,V_trackingParameters"
- "_effectiveParameters"
- "_maximumTarget"
- "_minimumTarget"
- "_o"
- "_offsetParameters"
- "_parameters"
- "_previousTarget"
- "_projectedTargetForVelocity:"
- "_projectionDeceleration"
- "_retargetImpulse"
- "_retargetResponseFraction"
- "_rubberbandFactor"
- "_rubberbandRange"
- "_s"
- "_targetVelocity"
- "_timeFactor"
- "_tracking"
- "_trackingParameters"
- "_transitioningFromTracking"
- "_updateForEffectiveParameters"
- "d"
- "d16@0:8"
- "d24@0:8d16"
- "init"
- "initWithValue:"
- "isStable"
- "isTracking"
- "maximumTarget"
- "minimumTarget"
- "offsetBy:"
- "offsetParameters"
- "offsetTo:"
- "parameters"
- "projectedTarget"
- "projectionDeceleration"
- "resetImmediatelyToValue:"
- "resetToTarget"
- "retargetImpulse"
- "retargetResponseFraction"
- "rubberbandFactor"
- "rubberbandRange"
- "setMaximumTarget:"
- "setMinimumTarget:"
- "setOffsetParameters:"
- "setParameters:"
- "setProjectionDeceleration:"
- "setRetargetImpulse:"
- "setRetargetResponseFraction:"
- "setRubberbandFactor:"
- "setRubberbandRange:"
- "setStableValueThreshold:"
- "setStableVelocityThreshold:"
- "setTarget:"
- "setTimeFactor:"
- "setTracking:"
- "setTrackingParameters:"
- "setValue:"
- "setVelocity:"
- "springWithValue:"
- "stable"
- "stableValueThreshold"
- "stableVelocityThreshold"
- "step:"
- "target"
- "timeFactor"
- "tracking"
- "trackingParameters"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8d16"
- "v48@0:8{FLSpringParameters=dddd}16"
- "value"
- "velocity"
- "{FLCompoundSpring=\"state\"{FLSimpleSpringState=\"position\"d\"velocity\"d}\"stiffness\"{FLSimpleSpring=\"state\"{FLSimpleSpringState=\"position\"d\"velocity\"d}\"mass\"d\"stiffness\"d\"damping\"d\"anchor\"d\"stablePositionThreshold\"d\"stableVelocityThreshold\"d\"_previousStiffness\"d\"_previousDamping\"d\"_beta\"d\"_omega0\"d\"_omega1\"d\"_omega2\"d}\"damping\"{FLSimpleSpring=\"state\"{FLSimpleSpringState=\"position\"d\"velocity\"d}\"mass\"d\"stiffness\"d\"damping\"d\"anchor\"d\"stablePositionThreshold\"d\"stableVelocityThreshold\"d\"_previousStiffness\"d\"_previousDamping\"d\"_beta\"d\"_omega0\"d\"_omega1\"d\"_omega2\"d}\"dampingRatio\"{FLSimpleSpring=\"state\"{FLSimpleSpringState=\"position\"d\"velocity\"d}\"mass\"d\"stiffness\"d\"damping\"d\"anchor\"d\"stablePositionThreshold\"d\"stableVelocityThreshold\"d\"_previousStiffness\"d\"_previousDamping\"d\"_beta\"d\"_omega0\"d\"_omega1\"d\"_omega2\"d}\"response\"{FLSimpleSpring=\"state\"{FLSimpleSpringState=\"position\"d\"velocity\"d}\"mass\"d\"stiffness\"d\"damping\"d\"anchor\"d\"stablePositionThreshold\"d\"stableVelocityThreshold\"d\"_previousStiffness\"d\"_previousDamping\"d\"_beta\"d\"_omega0\"d\"_omega1\"d\"_omega2\"d}\"anchor\"{FLSimpleSpring=\"state\"{FLSimpleSpringState=\"position\"d\"velocity\"d}\"mass\"d\"stiffness\"d\"damping\"d\"anchor\"d\"stablePositionThreshold\"d\"stableVelocityThreshold\"d\"_previousStiffness\"d\"_previousDamping\"d\"_beta\"d\"_omega0\"d\"_omega1\"d\"_omega2\"d}\"stablePositionThreshold\"d\"stableVelocityThreshold\"d}"
- "{FLSimpleSpring=\"state\"{FLSimpleSpringState=\"position\"d\"velocity\"d}\"mass\"d\"stiffness\"d\"damping\"d\"anchor\"d\"stablePositionThreshold\"d\"stableVelocityThreshold\"d\"_previousStiffness\"d\"_previousDamping\"d\"_beta\"d\"_omega0\"d\"_omega1\"d\"_omega2\"d}"
- "{FLSpringParameters=\"dampingRatio\"d\"dampingRatioSmoothing\"d\"response\"d\"responseSmoothing\"d}"
- "{FLSpringParameters=dddd}16@0:8"

```
