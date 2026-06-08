## SANovaGestureRecognizers

> `/System/Library/PrivateFrameworks/SANovaGestureRecognizers.framework/SANovaGestureRecognizers`

```diff

-74.0.0.0.0
-  __TEXT.__text: 0x4ec
-  __TEXT.__auth_stubs: 0x80
+111.0.0.0.0
+  __TEXT.__text: 0x468
   __TEXT.__objc_methlist: 0x1e0
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__const: 0x14
-  __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0x407
-  __TEXT.__objc_methtype: 0x122
-  __TEXT.__objc_stubs: 0x1a0
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__unwind_info: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x50
   __AUTH_CONST.__objc_const: 0x4f8
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x44
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 837989A4-57BF-3B9B-A5D7-7B5A4B215B2E
-  Functions: 45
-  Symbols:   155
-  CStrings:  85
+  UUID: 8A4B02B7-3E4C-3530-92DD-47837350B867
+  Functions: 41
+  Symbols:   147
+  CStrings:  0
 
Symbols:
+ GCC_except_table38
+ GCC_except_table39
+ __ZNSt3__110unique_ptrIN6grappa9nova_host25DoubleHalfPressRecognizerENS_14default_deleteIS3_EEE5resetB9fqn220100EPS3_
+ __ZNSt3__110unique_ptrIN6grappa9nova_host25DoubleHalfPressRecognizerENS_14default_deleteIS3_EEED2B9fqn220100Ev
+ _objc_retain_x2
- GCC_except_table32
- GCC_except_table34
- __ZN8NovaHost25DoubleHalfPressRecognizer10invalidateEv
- __ZN8NovaHost25DoubleHalfPressRecognizer5resetEv
- __ZN8NovaHost25DoubleHalfPressRecognizer6updateEP31TouchSensitiveButtonEventPacketP21ForceStageEventPacketPb
- __ZNSt3__110unique_ptrIN8NovaHost25DoubleHalfPressRecognizerENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN8NovaHost25DoubleHalfPressRecognizerENS_14default_deleteIS2_EEED2B9nqe210106Ev
- __ZNSt3__111make_uniqueB9nqe210106IN8NovaHost25DoubleHalfPressRecognizerEJELi0EEENS_10unique_ptrIT_NS_14default_deleteIS4_EEEEDpOT0_
- _objc_retain_x19
CStrings:
- ".cxx_construct"
- ".cxx_destruct"
- "@16@0:8"
- "B"
- "B16@0:8"
- "B40@0:8@16@24^B32"
- "I"
- "I16@0:8"
- "Q"
- "Q16@0:8"
- "S"
- "S16@0:8"
- "SANDoubleHalfPressRecognizer"
- "SANForceStageEvent"
- "SANTouchSensitiveButtonEvent"
- "TB,N,V_isTouching"
- "TI,N,V_eventMask"
- "TI,N,V_forceStage"
- "TI,N,V_forceStageTransition"
- "TQ,N,V_timestamp"
- "TS,N,V_phase"
- "Tf,N,V_forceProgress"
- "Tf,N,V_liftoffVelocity"
- "Tf,N,V_majorRadius"
- "Tf,N,V_nextThreshold"
- "Tf,N,V_positionDeltaY"
- "Tf,N,V_positionY"
- "Tf,N,V_pressedThreshold"
- "Tf,N,V_releasedThreshold"
- "_double_half_press_recognizer"
- "_eventMask"
- "_forceProgress"
- "_forceStage"
- "_forceStageTransition"
- "_isTouching"
- "_liftoffVelocity"
- "_majorRadius"
- "_nextThreshold"
- "_phase"
- "_positionDeltaY"
- "_positionY"
- "_pressedThreshold"
- "_releasedThreshold"
- "_timestamp"
- "eventMask"
- "f"
- "f16@0:8"
- "forceProgress"
- "forceStage"
- "forceStageTransition"
- "init"
- "invalidate"
- "isTouching"
- "liftoffVelocity"
- "majorRadius"
- "nextThreshold"
- "phase"
- "positionDeltaY"
- "positionY"
- "pressedThreshold"
- "releasedThreshold"
- "reset"
- "setEventMask:"
- "setForceProgress:"
- "setForceStage:"
- "setForceStageTransition:"
- "setIsTouching:"
- "setLiftoffVelocity:"
- "setMajorRadius:"
- "setNextThreshold:"
- "setPhase:"
- "setPositionDeltaY:"
- "setPositionY:"
- "setPressedThreshold:"
- "setReleasedThreshold:"
- "setTimestamp:"
- "timestamp"
- "update:forceStageEvent:isDoubleHalfPress:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v20@0:8f16"
- "v24@0:8Q16"
- "{unique_ptr<NovaHost::DoubleHalfPressRecognizer, std::default_delete<NovaHost::DoubleHalfPressRecognizer>>=\"\"{?=\"__ptr_\"^{DoubleHalfPressRecognizer}}}"

```
