## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-5.0.55.0.0
+5.0.59.0.0
   __TEXT.__text: 0x88a40
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_methlist: 0x7bcc
   __TEXT.__const: 0x3b8
   __TEXT.__gcc_except_tab: 0x1090
   __TEXT.__cstring: 0x69db
-  __TEXT.__oslogstring: 0xfac8
+  __TEXT.__oslogstring: 0xfac9
   __TEXT.__ustring: 0x328
   __TEXT.__unwind_info: 0x2288
   __TEXT.__objc_classname: 0x2004

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: C409127F-0426-324B-A5C8-3CF2ABF2DCFC
+  UUID: 1C99A166-5E6B-3620-BFC0-B7774F8C6E8B
   Functions: 3355
   Symbols:   11635
   CStrings:  5851
Symbols:
+ -[BLSHPendingUpdateDisplayModeConfiguration isAnimatedTransition]
+ -[BLSHPendingUpdateDisplayModeConfiguration setIsAnimatedTransition:]
+ _OBJC_IVAR_$_BLSHPendingUpdateDisplayModeConfiguration._isAnimatedTransition
+ _objc_msgSend$isAnimatedTransition
+ _objc_msgSend$setIsAnimatedTransition:
- -[BLSHPendingUpdateDisplayModeConfiguration isAnimatedTranistion]
- -[BLSHPendingUpdateDisplayModeConfiguration setIsAnimatedTranistion:]
- _OBJC_IVAR_$_BLSHPendingUpdateDisplayModeConfiguration._isAnimatedTranistion
- _objc_msgSend$isAnimatedTranistion
- _objc_msgSend$setIsAnimatedTranistion:
CStrings:
+ "BLSH Critical Assert did fail at %{public}@ on build %{public}@: %{public}@ userInitiated: %{public}d"
+ "TB,V_isAnimatedTransition"
+ "_isAnimatedTransition"
+ "isAnimatedTransition"
+ "setIsAnimatedTransition:"
- "BLSH Critical Assert did fail at %{public}@ on build %{public}@: %{public}@ userIntiated: %{public}d"
- "TB,V_isAnimatedTranistion"
- "_isAnimatedTranistion"
- "isAnimatedTranistion"
- "setIsAnimatedTranistion:"

```
