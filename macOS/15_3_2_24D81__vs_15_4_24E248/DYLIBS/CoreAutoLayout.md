## CoreAutoLayout

> `/System/Library/PrivateFrameworks/CoreAutoLayout.framework/Versions/A/CoreAutoLayout`

```diff

 33.0.0.0.0
-  __TEXT.__text: 0x334f4
+  __TEXT.__text: 0x32dd0
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x251c
+  __TEXT.__objc_methlist: 0x2744
   __TEXT.__const: 0x313
   __TEXT.__cstring: 0x6594
-  __TEXT.__gcc_except_tab: 0x49c
+  __TEXT.__gcc_except_tab: 0x4a8
   __TEXT.__oslogstring: 0x7c
   __TEXT.__dof_Cocoa_Lay: 0x51b
-  __TEXT.__unwind_info: 0xe38
+  __TEXT.__unwind_info: 0xea0
   __TEXT.__objc_classname: 0x691
   __TEXT.__objc_methname: 0x5f29
   __TEXT.__objc_methtype: 0xd7f

   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e8
+  __DATA_CONST.__objc_selrefs: 0x1558
   __DATA_CONST.__objc_superrefs: 0x118
   __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0xfe8
   __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x5338
+  __AUTH_CONST.__objc_const: 0x4f70
   __AUTH.__objc_data: 0xf50
   __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0x398

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 680ADBE3-63F8-3685-8758-5D5E5FFCF820
-  Functions: 1255
-  Symbols:   2633
+  UUID: AB16E69C-4D98-354D-8EFF-CEC39258806F
+  Functions: 1429
+  Symbols:   2882
   CStrings:  2267
 
Symbols:
+ +[NSISLinearExpression initialize].cold.1
+ +[NSLayoutAnchor _anchorForItem:attribute:].cold.1
+ +[NSLayoutAnchor anchorNamed:inItem:symbolicAttribute:].cold.1
+ +[NSLayoutAnchor anchorNamed:inItem:symbolicAttribute:].cold.2
+ -[NSErrorVariableConstraint constrainedConstraint].cold.1
+ -[NSErrorVariableConstraint initWithVariable:value:].cold.1
+ -[NSISEngine _coreReplaceMarker:withMarkerPlusDelta:].cold.1
+ -[NSISEngine _optimizeWithoutRebuilding].cold.1
+ -[NSISEngine _optimizeWithoutRebuilding].cold.2
+ -[NSISEngine addVariableToBeOptimized:priority:].cold.1
+ -[NSISEngine addVariableToBeOptimized:priority:].cold.2
+ -[NSISEngine bodyVarIsAmbiguous:withPivotOfOutgoingRowHead:foundOutgoingRowHead:].cold.1
+ -[NSISEngine constraintsAffectingValueOfVariable:].cold.1
+ -[NSISEngine constraintsAffectingValueOfVariable:].cold.2
+ -[NSISEngine containsVariable:].cold.1
+ -[NSISEngine containsVariable:].cold.2
+ -[NSISEngine endBookkeepingForVariableIfUnused:].cold.1
+ -[NSISEngine endBookkeepingForVariableIfUnused:].cold.2
+ -[NSISEngine engineVarIndexForVariable:].cold.1
+ -[NSISEngine engineVarIndexForVariable:].cold.2
+ -[NSISEngine exerciseAmbiguityInVariable:].cold.1
+ -[NSISEngine exerciseAmbiguityInVariable:].cold.2
+ -[NSISEngine fixUpValueRestrictionViolationsWithInfeasibilityHandlingBehavior:].cold.1
+ -[NSISEngine fixUpValueRestrictionViolationsWithInfeasibilityHandlingBehavior:].cold.2
+ -[NSISEngine fixUpValueRestrictionViolationsWithInfeasibilityHandlingBehavior:].cold.3
+ -[NSISEngine handleUnsatisfiableRow:usingInfeasibilityHandlingBehavior:prospectiveRowHead:mutuallyExclusiveConstraints:].cold.1
+ -[NSISEngine handleUnsatisfiableRow:usingInfeasibilityHandlingBehavior:prospectiveRowHead:mutuallyExclusiveConstraints:].cold.2
+ -[NSISEngine handleUnsatisfiableRow:usingInfeasibilityHandlingBehavior:prospectiveRowHead:mutuallyExclusiveConstraints:].cold.3
+ -[NSISEngine hasValue:forVariable:].cold.1
+ -[NSISEngine hasValue:forVariable:].cold.2
+ -[NSISEngine removeConstraintWithMarker:].cold.1
+ -[NSISEngine removeConstraintWithMarker:].cold.2
+ -[NSISEngine removeConstraintWithMarker:].cold.3
+ -[NSISEngine removeConstraintWithMarker:].cold.4
+ -[NSISEngine removeConstraintWithMarker:].cold.5
+ -[NSISEngine removeConstraintWithMarker:].cold.6
+ -[NSISEngine removeConstraintWithMarker:].cold.7
+ -[NSISEngine removeVariableToBeOptimized:priority:].cold.1
+ -[NSISEngine removeVariableToBeOptimized:priority:].cold.2
+ -[NSISEngine removeVariableToBeOptimized:priority:].cold.3
+ -[NSISEngine setShouldIntegralize:].cold.1
+ -[NSISEngine tryToChangeConstraintSuchThatMarker:isReplacedByMarkerPlusDelta:undoHandler:].cold.1
+ -[NSISEngine tryUsingArtificialVariableToAddConstraintWithMarker:row:usingInfeasibilityHandlingBehavior:mutuallyExclusiveConstraints:].cold.1
+ -[NSISEngine tryUsingArtificialVariableToAddConstraintWithMarker:row:usingInfeasibilityHandlingBehavior:mutuallyExclusiveConstraints:].cold.2
+ -[NSISEngine tryUsingArtificialVariableToAddConstraintWithMarker:row:usingInfeasibilityHandlingBehavior:mutuallyExclusiveConstraints:].cold.3
+ -[NSISEngine tryUsingArtificialVariableToAddConstraintWithMarker:row:usingInfeasibilityHandlingBehavior:mutuallyExclusiveConstraints:].cold.4
+ -[NSISEngine tryUsingArtificialVariableToAddConstraintWithMarker:row:usingInfeasibilityHandlingBehavior:mutuallyExclusiveConstraints:].cold.5
+ -[NSISEngine tryUsingArtificialVariableToAddConstraintWithMarker:row:usingInfeasibilityHandlingBehavior:mutuallyExclusiveConstraints:].cold.6
+ -[NSISEngine valueForVariable:].cold.1
+ -[NSISEngine valueForVariable:].cold.2
+ -[NSISEngine valueOfVariableIsAmbiguous:].cold.1
+ -[NSISEngine valueOfVariableIsAmbiguous:].cold.2
+ -[NSISLinearExpression addVariable:coefficient:].cold.1
+ -[NSISLinearExpression addVariable:coefficient:processVariableNewToReceiver:processVariableDroppedFromReceiver:].cold.1
+ -[NSISLinearExpression verifyInternalIntegrity].cold.1
+ -[NSISLinearExpression verifyInternalIntegrity].cold.2
+ -[NSISLinearExpression verifyInternalIntegrity].cold.3
+ -[NSISLinearExpression verifyInternalIntegrity].cold.4
+ -[NSISVariable encodeWithCoder:].cold.1
+ -[NSISVariable initWithCoder:].cold.1
+ -[NSLayoutAnchor _equationDescriptionInParent].cold.1
+ -[NSLayoutAnchor _expressionInContext:].cold.1
+ -[NSLayoutAnchor _proxiedAttribute].cold.1
+ -[NSLayoutAnchor _proxiedItem].cold.1
+ -[NSLayoutAnchor _referenceItem].cold.1
+ -[NSLayoutAnchor _valueInEngine:].cold.1
+ -[NSLayoutAnchor _variableName].cold.1
+ -[NSLayoutAnchor encodeWithCoder:].cold.1
+ -[NSLayoutAnchor initWithAnchor:].cold.1
+ -[NSLayoutAnchor initWithCoder:].cold.1
+ -[NSLayoutAnchor initWithIndependentVariableName:item:symbolicAttribute:].cold.1
+ -[NSLayoutAnchor initWithIndependentVariableName:item:symbolicAttribute:].cold.2
+ -[NSLayoutAnchor initWithItem:attribute:].cold.1
+ -[NSLayoutAnchor initWithItem:attribute:].cold.2
+ -[NSLayoutAnchor nsli_lowerIntoExpression:withCoefficient:forConstraint:].cold.1
+ -[NSLayoutConstraint _makeExtraVars].cold.1
+ -[NSLayoutConstraint _makeExtraVars].cold.2
+ -[NSLayoutConstraint _setFirstItem:attribute:].cold.1
+ -[NSLayoutConstraint _setMultiplier:].cold.1
+ -[NSLayoutConstraint _setMultiplier:].cold.2
+ -[NSLayoutConstraint _setMutablePropertiesFromConstraint:].cold.1
+ -[NSLayoutConstraint _setRelation:].cold.1
+ -[NSLayoutConstraint constant].cold.1
+ -[NSLayoutConstraint initWithCoder:].cold.1
+ -[NSLayoutConstraintExplainer _freezeErrorVariable:forcingZeroValue:inEngine:accumulatingConstraints:andMutuallyExclusiveConstraints:].cold.1
+ -[NSLayoutConstraintExplainer _freezeErrorVariable:forcingZeroValue:inEngine:accumulatingConstraints:andMutuallyExclusiveConstraints:].cold.2
+ -[NSLayoutConstraintParser finishConstraint].cold.1
+ -[NSLayoutRect(ValueInCoordinateSpace_NotYetProposed) observableValueInItem:].cold.1
+ -[_NSDistanceLayoutDimension initWithMinuend:subtrahend:].cold.1
+ -[_NSDistanceLayoutDimension initWithMinuend:subtrahend:].cold.2
+ -[_NSDistanceLayoutDimension initWithMinuend:subtrahend:].cold.3
+ NSISLinExpAddExpression.cold.1
+ NSISLinExpAddExpressionWithProcessors.cold.1
+ NSISLinExpAddVar.cold.1
+ NSISLinExpAddVarWithProcessors.cold.1
+ NSISLinExpIncrementConstant.cold.1
+ NSISLinExpReplaceVarWithVar.cold.1
+ NSISLinExpSetCoefficientForVar.cold.1
+ NSISSparseVectorAddTermWithPlaceValueCoefficientStartingIndex.cold.1
+ NSISSparseVectorMapDelete.cold.1
+ NSISSparseVectorMapDelete.cold.2
+ NSISSparseVectorMapFind.cold.1
+ NSISVariableRemoveEngine.cold.1
+ ResolveConstraintArguments.cold.1
+ VerifyHeapIntegrity.cold.1
+ VerifyHeapIntegrity.cold.2
+ _CALSDKVersionInit.cold.1
+ _NSBitSetResize.cold.1
+ _NSBitSetResize.cold.2
+ _NSLayoutConstraintApplyDiffWithCounterpartsNSArrays.cold.1
+ _NSLayoutConstraintDiffConstraints.cold.1
+ _NSLayoutConstraintDiffConstraints.cold.2
+ _NSLayoutConstraintDiffConstraints.cold.3
+ _NSLayoutConstraintDiffConstraints.cold.4
+ _NSLayoutConstraintSortDiff.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ResolvedDirectionForAnchorAbstractionsForAnchorsInLayoutDirectionContext.cold.1
+ __113-[NSISObjectiveLinearExpression replaceVar:withExpression:processVarNewToReceiver:processVarDroppedFromReceiver:]_block_invoke.cold.1
+ __35-[NSISEngine _flushPendingRemovals]_block_invoke.cold.1
+ __35-[NSISEngine _flushPendingRemovals]_block_invoke.cold.2
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke.292.cold.1
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke.292.cold.2
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke.292.cold.3
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke.cold.1
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke_2.cold.1
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke_3.cold.1
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke_3.cold.2
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke_4.321.cold.1
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke_7.cold.1
+ __37-[NSISEngine verifyInternalIntegrity]_block_invoke_7.cold.2
+ __79-[NSISEngine fixUpValueRestrictionViolationsWithInfeasibilityHandlingBehavior:]_block_invoke.cold.1
+ ___objectiveRow_rawAddCol_block_invoke.cold.1
+ ___objectiveRow_rawAddCol_block_invoke_2.cold.1
+ ___objectiveRow_rawAddRowBody_block_invoke.cold.1
+ ___objectiveRow_rawAddRowBody_block_invoke_2.cold.1
+ ___row_enumerateColsUntil_block_invoke.cold.1
+ ___row_enumerateColsWithCoefficientsUntil_block_invoke.cold.1
+ ___row_enumerateColsWithCoefficients_block_invoke.cold.1
+ ___row_enumerateCols_block_invoke.cold.1
+ ___row_enumerateCols_block_invoke_2.cold.1
+ ___row_rawAddCol_block_invoke.605.cold.1
+ ___row_rawAddCol_block_invoke.cold.1
+ ___row_rawReplaceColWithColPlusDeltaTimesNewCol_block_invoke.cold.1
+ ___row_rawReplaceColWithColPlusDeltaTimesNewCol_block_invoke_2.cold.1
+ ___row_rawReplaceColWithColPlusDeltaTimesNewCol_block_invoke_3.cold.1
+ ___row_rawReplaceColWithColPlusDeltaTimesNewCol_block_invoke_4.cold.1
+ ___row_rawReplaceColWithRowBody_block_invoke.cold.1
+ ___row_rawReplaceColWithRowBody_block_invoke_2.cold.1
+ ___row_rawReplaceColWithRowBody_block_invoke_3.cold.1
+ ___row_rawReplaceColWithRowBody_block_invoke_4.cold.1
+ ___row_rawScaleByWithDroppedColProcessor_block_invoke.cold.1
+ _engineVar_addForVariableIfNeeded.cold.1
+ _engineVar_addForVariableIfNeeded.cold.2
+ _engineVar_rawRemove.cold.1
+ _engineVar_rawRemove.cold.2
+ _minimizeConstantInObjectiveRow.cold.1
+ _minimizeConstantInObjectiveRow.cold.2
+ _minimizeConstantInObjectiveRow.cold.3
+ _objectiveRow_addColWithPriorityTimes.cold.1
+ _objectiveRow_addRowBodyWithPriorityTimes.cold.1
+ _row_rawSetHead.cold.1

```
