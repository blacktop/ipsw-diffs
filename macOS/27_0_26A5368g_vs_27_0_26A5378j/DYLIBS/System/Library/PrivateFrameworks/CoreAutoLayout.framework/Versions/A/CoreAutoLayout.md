## CoreAutoLayout

> `/System/Library/PrivateFrameworks/CoreAutoLayout.framework/Versions/A/CoreAutoLayout`

```diff

-  __TEXT.__text: 0x32b60
+  __TEXT.__text: 0x32cb8
   __TEXT.__objc_methlist: 0x2744
   __TEXT.__const: 0x303
   __TEXT.__cstring: 0x657a

   __AUTH_CONST.__cfstring: 0x4000
   __AUTH_CONST.__objc_const: 0x4f70
   __AUTH_CONST.__auth_got: 0x298
+  __AUTH.__objc_data: 0x640
   __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0x378
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0xf50
+  __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x8e
   __DATA_DIRTY.__common: 0x1
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__dof_Cocoa_Lay : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
Functions:
~ _NSISVariableAddEngine : 172 -> 176
~ __engineVar_forVariable : 260 -> 268
~ __engineVar_addForVariableIfNeeded : 668 -> 676
~ -[NSISEngine handleUnsatisfiableRow:usingInfeasibilityHandlingBehavior:prospectiveRowHead:mutuallyExclusiveConstraints:] : 1692 -> 1708
~ -[NSISEngine fixUpValueRestrictionViolationsWithInfeasibilityHandlingBehavior:] : 1160 -> 1168
~ -[NSISEngine engineVarIndexForVariable:] : 256 -> 264
~ ___35-[NSISEngine _flushPendingRemovals]_block_invoke : 436 -> 452
~ -[NSISEngine valueForVariable:] : 432 -> 448
~ -[NSISEngine hasValue:forVariable:] : 440 -> 456
~ -[NSISEngine containsVariable:] : 440 -> 456
~ -[NSISEngine endBookkeepingForVariableIfUnused:] : 452 -> 468
~ -[NSISEngine removeVariableToBeOptimized:priority:] : 712 -> 728
~ -[NSISEngine removeConstraintWithMarker:] : 1392 -> 1408
~ -[NSISEngine _coreReplaceMarker:withMarkerPlusDelta:] : 216 -> 224
~ ___37-[NSISEngine verifyInternalIntegrity]_block_invoke : 448 -> 456
~ -[NSISEngine constraintsAffectingValueOfVariable:] : 648 -> 664
~ -[NSISEngine valueOfVariableIsAmbiguous:] : 464 -> 480
~ -[NSISEngine exerciseAmbiguityInVariable:] : 468 -> 484
~ _OUTLINED_FUNCTION_22 : 28 -> 16
~ _OUTLINED_FUNCTION_23 : 36 -> 16
~ _OUTLINED_FUNCTION_24 : 12 -> 28
~ _OUTLINED_FUNCTION_25 : 16 -> 36
~ _OUTLINED_FUNCTION_26 : 16 -> 12
~ _OUTLINED_FUNCTION_27 : 32 -> 16
~ _OUTLINED_FUNCTION_28 : 40 -> 16
~ _OUTLINED_FUNCTION_29 : 12 -> 32
~ _OUTLINED_FUNCTION_30 : 28 -> 40
~ _OUTLINED_FUNCTION_31 : 24 -> 12
~ _OUTLINED_FUNCTION_32 : 16 -> 28
~ _OUTLINED_FUNCTION_33 : 12 -> 24
~ _OUTLINED_FUNCTION_34 : 24 -> 16
~ _OUTLINED_FUNCTION_35 : 32 -> 12
~ _OUTLINED_FUNCTION_36 : 12 -> 24
~ _OUTLINED_FUNCTION_37 : 28 -> 32
~ _OUTLINED_FUNCTION_38 : 16 -> 12
~ _OUTLINED_FUNCTION_40 -> _OUTLINED_FUNCTION_39 : 24 -> 28
~ _OUTLINED_FUNCTION_41 -> _OUTLINED_FUNCTION_40 : 8 -> 16
~ _OUTLINED_FUNCTION_43 : 12 -> 8
~ _OUTLINED_FUNCTION_44 : 12 -> 24
~ _OUTLINED_FUNCTION_45 : 24 -> 12
~ _OUTLINED_FUNCTION_46 : 12 -> 24
~ -[NSISLinearExpression removeVariable:] : 196 -> 204
~ -[NSISLinearExpression coefficientForVariable:] : 200 -> 208
~ -[NSISLinearExpression setCoefficient:forVariable:] : 308 -> 316
~ -[NSISLinearExpression replaceVariable:withVariable:coefficient:] : 532 -> 548
~ -[NSISLinearExpression addVariable:coefficient:] : 324 -> 332
~ ___112-[NSISLinearExpression addVariable:coefficient:processVariableNewToReceiver:processVariableDroppedFromReceiver:]_block_invoke : 312 -> 320
~ -[NSISLinearExpression replaceVariable:withVariablePlusDelta:] : 308 -> 316
~ ___140-[NSISLinearExpression replaceVariable:withVariablePlusDelta:timesVariable:processVariableNewToReceiver:processVariableDroppedFromReceiver:]_block_invoke : 560 -> 576
~ ___119-[NSISLinearExpression replaceVariable:withExpression:processVariableNewToReceiver:processVariableDroppedFromReceiver:]_block_invoke : 316 -> 324
~ _NSISLinExpScaleByWithDroppedColProcessor : 396 -> 400
~ -[NSISVariable descriptionInEngine:] : 256 -> 260
~ -[NSISEngine errorVariableIntroducedByBreakingConstraintWithMarker:errorIsPositive:] : 540 -> 536
~ -[NSISEngine tryToAddConstraintWithMarker:expression:mutuallyExclusiveConstraints:] : 1188 -> 1204

```
