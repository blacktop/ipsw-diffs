## PowerlogAccounting

> `/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`

```diff

-3031.122.1.0.0
-  __TEXT.__text: 0x373f0
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x1bd0
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x5566
-  __TEXT.__oslogstring: 0xeb
+3468.0.0.502.1
+  __TEXT.__text: 0x36420
+  __TEXT.__objc_methlist: 0x1c30
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0x55b3
+  __TEXT.__oslogstring: 0x1328
   __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__unwind_info: 0x910
-  __TEXT.__objc_classname: 0x627
-  __TEXT.__objc_methname: 0x3b5b
-  __TEXT.__objc_methtype: 0xa8b
-  __TEXT.__objc_stubs: 0x2de0
-  __DATA_CONST.__got: 0x3b0
+  __TEXT.__unwind_info: 0x9b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x428
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_nlclslist: 0x98
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xde0
+  __DATA_CONST.__objc_selrefs: 0xe08
   __DATA_CONST.__objc_superrefs: 0x1a8
-  __DATA_CONST.__objc_arraydata: 0x1548
-  __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x3180
-  __AUTH_CONST.__objc_const: 0x28f8
+  __DATA_CONST.__objc_arraydata: 0x1570
+  __DATA_CONST.__got: 0x3b0
+  __AUTH_CONST.__const: 0x420
+  __AUTH_CONST.__cfstring: 0x31a0
+  __AUTH_CONST.__objc_const: 0x2960
   __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_ivar: 0xe4
+  __AUTH_CONST.__auth_got: 0x238
+  __DATA.__objc_ivar: 0xec
   __DATA.__data: 0x360
-  __DATA.__bss: 0x12e9
+  __DATA.__bss: 0x12c9
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 016F43FD-C1EF-3CDC-B6C1-4099A7E16762
-  Functions: 915
-  Symbols:   4020
-  CStrings:  1658
+  UUID: A1566500-E821-300F-A987-6A597A2AD1CD
+  Functions: 957
+  Symbols:   4082
+  CStrings:  997
 
Symbols:
+ -[PLAccountingCorrectionManager addRootEnergyEstimate:withNow:].cold.2
+ -[PLAccountingCorrectionManager addRootEnergyEstimate:withNow:].cold.3
+ -[PLAccountingCorrectionOwner correct].cold.3
+ -[PLAccountingCorrectionOwner correct].cold.4
+ -[PLAccountingCorrectionOwner dealloc]
+ -[PLAccountingCorrectionOwner dealloc].cold.1
+ -[PLAccountingDependency setSkipLastAllRunDateCheck:]
+ -[PLAccountingDependency skipLastAllRunDateCheck]
+ -[PLAccountingEnergyEstimateEventEntry dealloc]
+ -[PLAccountingEnergyEstimateEventEntry dealloc].cold.1
+ -[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:].cold.6
+ -[PLAccountingOwner activate].cold.5
+ -[PLAccountingOwner allRun].cold.2
+ -[PLAccountingOwner deactivate].cold.2
+ -[PLAccountingOwner deactivate].cold.3
+ -[PLAccountingOwner deactivate].cold.4
+ -[PLAccountingOwner didReceiveDependency:].cold.10
+ -[PLAccountingOwner didReceiveDependency:].cold.7
+ -[PLAccountingOwner didReceiveDependency:].cold.8
+ -[PLAccountingOwner didReceiveDependency:].cold.9
+ -[PLAccountingOwnerDependencyManager canFreeOwner:].cold.3
+ -[PLAccountingOwnerDependencyManager canFreeOwner:].cold.4
+ -[PLAccountingOwnerDependencyManager canFreeOwner:].cold.5
+ -[PLAccountingOwnerDependencyManager lastAllRunDateForOwnerID:]
+ -[PLAccountingOwnerDependencyManager lastAllRunDateForOwnerID:].cold.1
+ -[PLAccountingOwnerDependencyManager lastAllRunDateForOwnerID:].cold.2
+ -[PLAccountingOwnerDependencyManager ownerIDToLastAllRunDate]
+ -[PLAccountingOwnerDependencyManager setOwnerIDToLastAllRunDate:]
+ GCC_except_table147
+ _OBJC_IVAR_$_PLAccountingDependency._skipLastAllRunDateCheck
+ _OBJC_IVAR_$_PLAccountingOwnerDependencyManager._ownerIDToLastAllRunDate
+ _OUTLINED_FUNCTION_5
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.107
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.33
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.40
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.46
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.52
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.76
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.82
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.91
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.98
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.106
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.32
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.39
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.45
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.51
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.75
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.81
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.90
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.97
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_13.classDebugEnabled.442
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_13.defaultOnce.441
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_18.classDebugEnabled.618
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_18.defaultOnce.617
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.58
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.57
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.396
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.68
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.75
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.82
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.88
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.395
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.67
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.74
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.81
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.87
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled.94
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce.93
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.104
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.111
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.117
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.408
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.103
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.110
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.116
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.407
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_7.classDebugEnabled.416
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_7.defaultOnce.415
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_8.classDebugEnabled.422
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_8.defaultOnce.421
+ ___102-[PLAccountingQualificationManager closeLastQualificationEventForwardWithQualificationID:withEndDate:]_block_invoke.44
+ ___104-[PLAccountingEngine createQualificationEventPointWithQualificationID:withChildNodeNames:withStartDate:]_block_invoke.460
+ ___105-[PLAccountingEngine createQualificationEventBackwardWithQualificationID:withChildNodeNames:withEndDate:]_block_invoke.455
+ ___106-[PLAccountingEngine createQualificationEventForwardWithQualificationID:withChildNodeNames:withStartDate:]_block_invoke.451
+ ___109-[PLAccountingEngine createDistributionEventPointWithDistributionID:withChildNodeNameToWeight:withStartDate:]_block_invoke.437
+ ___110-[PLAccountingEngine createDistributionEventBackwardWithDistributionID:withChildNodeNameToWeight:withEndDate:]_block_invoke.432
+ ___111-[PLAccountingEngine createDistributionEventForwardWithDistributionID:withChildNodeNameToWeight:withStartDate:]_block_invoke.428
+ ___112-[PLAccountingEngine addDistributionEventIntervalWithLastDistributionEventForward:withDistributionEventForward:]_block_invoke.491
+ ___114-[PLAccountingEngine addDistributionEventIntervalWithLastDistributionEventBackward:withDistributionEventBackward:]_block_invoke.500
+ ___115-[PLAccountingEngine addQualificationEventIntervalWithLastQualificationEventForward:withQualificationEventForward:]_block_invoke.544
+ ___117-[PLAccountingEngine addQualificationEventIntervalWithLastQualificationEventBackward:withQualificationEventBackward:]_block_invoke.553
+ ___119-[PLAccountingEngine createQualificationEventIntervalWithQualificationID:withChildNodeNames:withStartDate:withEndDate:]_block_invoke.459
+ ___124-[PLAccountingEngine createDistributionEventIntervalWithDistributionID:withChildNodeNameToWeight:withStartDate:withEndDate:]_block_invoke.436
+ ___140-[PLAccountingEnergyEstimateEventEntry initWithNodeID:withRootNodeID:withParentEntryID:withNumAncestors:withEnergy:withRange:withEntryDate:]_block_invoke.25
+ ___27-[PLAccountingEngine reset]_block_invoke.43
+ ___27-[PLAccountingEngine reset]_block_invoke.43.cold.1
+ ___28-[PLAccountingEngine reload]_block_invoke.619
+ ___29-[PLAccountingOwner activate]_block_invoke.20
+ ___29-[PLAccountingOwner activate]_block_invoke.26
+ ___29-[PLAccountingOwner activate]_block_invoke.32
+ ___29-[PLAccountingOwner activate]_block_invoke.38
+ ___29-[PLAccountingOwner activate]_block_invoke.44
+ ___29-[PLAccountingOwner activate]_block_invoke.50
+ ___30-[PLAccountingRange overlaps:]_block_invoke.38
+ ___30-[PLAccountingRange overlaps:]_block_invoke.44
+ ___30-[PLAccountingRange overlaps:]_block_invoke.50
+ ___31-[PLAccountingRange intersect:]_block_invoke.20
+ ___31-[PLAccountingRange intersect:]_block_invoke.26
+ ___31-[PLAccountingRange intersect:]_block_invoke.32
+ ___34-[PLAccountingDependency activate]_block_invoke.22
+ ___34-[PLAccountingDependency activate]_block_invoke.28
+ ___35-[PLAccountingOwner addDependency:]_block_invoke.89
+ ___36-[PLAccountingRuleManager loadRules]_block_invoke.28
+ ___36-[PLAccountingRuleManager loadRules]_block_invoke.35
+ ___36-[PLAccountingRuleManager loadRules]_block_invoke.41
+ ___36-[PLAccountingRuleManager loadRules]_block_invoke.45
+ ___36-[PLAccountingRuleManager loadRules]_block_invoke.53
+ ___37-[PLAccountingNodeManager setupNodes]_block_invoke.108
+ ___37-[PLAccountingNodeManager setupNodes]_block_invoke.68
+ ___37-[PLAccountingNodeManager setupNodes]_block_invoke.77
+ ___37-[PLAccountingNodeManager setupNodes]_block_invoke.83
+ ___37-[PLAccountingNodeManager setupNodes]_block_invoke.87
+ ___37-[PLAccountingNodeManager setupNodes]_block_invoke.99
+ ___38-[PLAccountingCorrectionOwner correct]_block_invoke.22
+ ___38-[PLAccountingCorrectionOwner correct]_block_invoke.28
+ ___38-[PLAccountingCorrectionOwner correct]_block_invoke.34
+ ___38-[PLAccountingCorrectionOwner correct]_block_invoke.40
+ ___38-[PLAccountingCorrectionOwner correct]_block_invoke.46
+ ___38-[PLAccountingCorrectionOwner correct]_block_invoke.53
+ ___38-[PLAccountingCorrectionOwner correct]_block_invoke.59
+ ___38-[PLAccountingCorrectionOwner correct]_block_invoke.65
+ ___41-[PLAccountingEventEntry mergeWithEvent:]_block_invoke.58
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.22
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.28
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.34
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.40
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.47
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.53
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.59
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.65
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.71
+ ___41-[PLAccountingQualificationOwner qualify]_block_invoke.78
+ ___42-[PLAccountingDependency didReceiveOwner:]_block_invoke.37
+ ___42-[PLAccountingDependency didReceiveOwner:]_block_invoke.43
+ ___42-[PLAccountingDependency didReceiveOwner:]_block_invoke.49
+ ___42-[PLAccountingEventEntry rangeSinceEvent:]_block_invoke.28
+ ___42-[PLAccountingEventEntry rangeSinceEvent:]_block_invoke.34
+ ___42-[PLAccountingEventEntry rangeSinceEvent:]_block_invoke.40
+ ___42-[PLAccountingEventEntry rangeSinceEvent:]_block_invoke.46
+ ___42-[PLAccountingOwner didReceiveDependency:]_block_invoke.59
+ ___42-[PLAccountingOwner didReceiveDependency:]_block_invoke.68
+ ___42-[PLAccountingOwner didReceiveDependency:]_block_invoke.74
+ ___42-[PLAccountingOwner didReceiveDependency:]_block_invoke.80
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.22
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.28
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.34
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.40
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.46
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.52
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.58
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.64
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.73
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.80
+ ___43-[PLAccountingDistributionOwner distribute]_block_invoke.86
+ ___44-[PLAccountingDependency updateWithEndDate:]_block_invoke.58
+ ___44-[PLAccountingDependency updateWithEndDate:]_block_invoke.65
+ ___47+[PLAccountingRuleManager decryptData:withKey:]_block_invoke.116
+ ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.34
+ ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.41
+ ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.47
+ ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.53
+ ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.cold.6
+ ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.cold.7
+ ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.cold.8
+ ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.cold.9
+ ___49-[PLAccountingDistributionRuleManager indexRule:]_block_invoke.71
+ ___50-[PLAccountingQualificationRuleManager indexRule:]_block_invoke.56
+ ___51-[PLAccountingOwnerDependencyManager canFreeOwner:]_block_invoke.151
+ ___51-[PLAccountingOwnerDependencyManager canFreeOwner:]_block_invoke.157
+ ___52-[PLAccountingOwnerDependencyManager addDependency:]_block_invoke.69
+ ___52-[PLAccountingOwnerDependencyManager addDependency:]_block_invoke.76
+ ___52-[PLAccountingOwnerDependencyManager addDependency:]_block_invoke.83
+ ___52-[PLAccountingOwnerDependencyManager addDependency:]_block_invoke.89
+ ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.588
+ ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.601
+ ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.607
+ ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.610
+ ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.613
+ ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.105
+ ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.74
+ ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.81
+ ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.91
+ ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.99
+ ___55-[PLAccountingCorrectionManager dependencyIDsForOwner:]_block_invoke.112
+ ___55-[PLAccountingCorrectionManager ownerIDsForDependency:]_block_invoke.121
+ ___56-[PLAccountingDistributionManager addDistributionEvent:]_block_invoke.34
+ ___56-[PLAccountingOwnerDependencyManager canFreeDependency:]_block_invoke.178
+ ___57-[PLAccountingDistributionManager dependencyIDsForOwner:]_block_invoke.124
+ ___57-[PLAccountingDistributionManager ownerIDsForDependency:]_block_invoke.134
+ ___57-[PLAccountingDistributionManager ownerIDsForDependency:]_block_invoke.138
+ ___57-[PLAccountingNodeManager nodeIDForNodeName:isPermanent:]_block_invoke.21
+ ___57-[PLAccountingNodeManager nodeIDForNodeName:isPermanent:]_block_invoke.27
+ ___57-[PLAccountingNodeManager nodeIDForNodeName:isPermanent:]_block_invoke.33
+ ___58+[PLAccountingPowerEventEntry isValidPower:forRootNodeID:]_block_invoke.22
+ ___58+[PLAccountingPowerEventEntry isValidPower:forRootNodeID:]_block_invoke.28
+ ___58-[PLAccountingCorrectionManager didCorrectEnergyEstimate:]_block_invoke.105
+ ___58-[PLAccountingNodeManager childNodeIDsFromChildNodeNames:]_block_invoke.50
+ ___58-[PLAccountingQualificationManager addQualificationEvent:]_block_invoke.27
+ ___58-[PLAccountingQualificationManager dependencyIDsForOwner:]_block_invoke.120
+ ___58-[PLAccountingQualificationManager dependencyIDsForOwner:]_block_invoke.124
+ ___59-[PLAccountingEngine createEventWithEvent:withActionBlock:]_block_invoke.466
+ ___59-[PLAccountingEngine createEventWithEvent:withActionBlock:]_block_invoke.472
+ ___61-[PLAccountingDistributionManager addEnergyEstimate:withNow:]_block_invoke.23
+ ___61-[PLAccountingOwnerDependencyManager freeExpiredOwnersAtNow:]_block_invoke.187
+ ___61-[PLAccountingOwnerDependencyManager freeExpiredOwnersAtNow:]_block_invoke.193
+ ___61-[PLAccountingOwnerDependencyManager freeExpiredOwnersAtNow:]_block_invoke.199
+ ___63-[PLAccountingDistributionManager didDistributeEnergyEstimate:]_block_invoke.118
+ ___63-[PLAccountingOwnerDependencyManager lastAllRunDateForOwnerID:]_block_invoke
+ ___63-[PLAccountingOwnerDependencyManager lastAllRunDateForOwnerID:]_block_invoke.163
+ ___65-[PLAccountingCorrectionManager reloadDependenciesNewerThanDate:]_block_invoke.74
+ ___65-[PLAccountingCorrectionManager reloadDependenciesNewerThanDate:]_block_invoke.80
+ ___65-[PLAccountingOwnerDependencyManager notifyOwnersWithDependency:]_block_invoke.95
+ ___66-[PLAccountingEngine reloadLastPowerEventsWithLastDeviceBootDate:]_block_invoke.632
+ ___66-[PLAccountingEngine reloadLastPowerEventsWithLastDeviceBootDate:]_block_invoke.638
+ ___66-[PLAccountingOwnerDependencyManager notifyDependenciesWithOwner:]_block_invoke.59
+ ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.101
+ ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.107
+ ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.66
+ ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.75
+ ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.94
+ ___67-[PLAccountingOwnerDependencyManager freeExpiredDependenciesAtNow:]_block_invoke.208
+ ___68-[PLAccountingDistributionRuleManager ruleWithString:withEntryDate:]_block_invoke.48
+ ___68-[PLAccountingDistributionRuleManager ruleWithString:withEntryDate:]_block_invoke.54
+ ___68-[PLAccountingDistributionRuleManager ruleWithString:withEntryDate:]_block_invoke.61
+ ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.101
+ ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.107
+ ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.57
+ ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.63
+ ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.75
+ ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.94
+ ___69-[PLAccountingQualificationRuleManager ruleWithString:withEntryDate:]_block_invoke.39
+ ___69-[PLAccountingQualificationRuleManager ruleWithString:withEntryDate:]_block_invoke.46
+ ___70-[PLAccountingCorrectionManager childEnergyEstimatesForParentEntryID:]_block_invoke.101
+ ___70-[PLAccountingCorrectionManager childEnergyEstimatesForParentEntryID:]_block_invoke.95
+ ___72-[PLAccountingEngine currentDistributionEventForwardWithDistributionID:]_block_invoke.443
+ ___73-[PLAccountingEngine reloadLastDistributionEventsWithLastDeviceBootDate:]_block_invoke.641
+ ___73-[PLAccountingEngine reloadLastDistributionEventsWithLastDeviceBootDate:]_block_invoke.651
+ ___73-[PLAccountingEngine reloadLastDistributionEventsWithLastDeviceBootDate:]_block_invoke.657
+ ___73-[PLAccountingOwnerDependencyManager stopObservingDependencyID:forOwner:]_block_invoke.148
+ ___73-[PLAccountingOwnerDependencyManager stopObservingOwnerID:forDependency:]_block_invoke.175
+ ___73-[PLAccountingOwnerDependencyManager updateLastDependencyID:withEndDate:]_block_invoke.105
+ ___73-[PLAccountingOwnerDependencyManager updateLastDependencyID:withEndDate:]_block_invoke.112
+ ___73-[PLAccountingOwnerDependencyManager updateLastDependencyID:withEndDate:]_block_invoke.118
+ ___74-[PLAccountingEngine reloadLastQualificationEventsWithLastDeviceBootDate:]_block_invoke.660
+ ___74-[PLAccountingEngine reloadLastQualificationEventsWithLastDeviceBootDate:]_block_invoke.669
+ ___74-[PLAccountingEngine reloadLastQualificationEventsWithLastDeviceBootDate:]_block_invoke.675
+ ___74-[PLAccountingOwnerDependencyManager startObservingDependencyID:forOwner:]_block_invoke.145
+ ___74-[PLAccountingOwnerDependencyManager startObservingOwnerID:forDependency:]_block_invoke.172
+ ___75-[PLAccountingEngine createAggregateRootNodeEnergyEntryWithEnergyEstimate:]_block_invoke.678
+ ___75-[PLAccountingEngine createAggregateRootNodeEnergyEntryWithEnergyEstimate:]_block_invoke.684
+ ___76-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:]_block_invoke.510
+ ___76-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:]_block_invoke.520
+ ___76-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:]_block_invoke.526
+ ___76-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:]_block_invoke.532
+ ___77-[PLAccountingOwnerDependencyManager dependenciesWithDependencyID:withRange:]_block_invoke.127
+ ___77-[PLAccountingOwnerDependencyManager dependenciesWithDependencyID:withRange:]_block_invoke.130
+ ___77-[PLAccountingOwnerDependencyManager dependenciesWithDependencyID:withRange:]_block_invoke.136
+ ___78-[PLAccountingEngine addEnergyMeasurementWithRootNodeID:withEnergy:withRange:]_block_invoke.579
+ ___79-[PLAccountingDistributionRuleManager distributionRuleForRootNodeID:andNodeID:]_block_invoke.21
+ ___79-[PLAccountingEngine didQualifyEnergyEvent:withRootNodeID:withQualificationID:]_block_invoke.566
+ ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.405
+ ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.405.cold.1
+ ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.405.cold.2
+ ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.405.cold.3
+ ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.405.cold.4
+ ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.406
+ ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.409
+ ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.387
+ ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.387.cold.1
+ ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.387.cold.2
+ ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.387.cold.3
+ ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.397
+ ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke_2.388
+ ___90-[PLAccountingEngine addPowerMeasurementEventIntervalWithPower:withStartDate:withEndDate:]_block_invoke.423
+ ___93-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:]_block_invoke.29
+ ___93-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:]_block_invoke.35
+ ___93-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:]_block_invoke.41
+ ___93-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:]_block_invoke.45
+ ___93-[PLAccountingQualificationManager didQualifyEnergyEvent:withRootNodeID:withQualificationID:]_block_invoke.114
+ ___95-[PLAccountingDistributionManager didDistributeToChildEnergyEstimate:fromParentEnergyEstimate:]_block_invoke.114
+ ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.413
+ ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.413.cold.1
+ ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.413.cold.2
+ ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.413.cold.3
+ ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.417
+ ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke_2.414
+ ___99-[PLAccountingDistributionManager closeLastDistributionEventForwardWithDistributionID:withEndDate:]_block_invoke.52
+ ___block_literal_global.16
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.337
+ ___block_literal_global.478
+ ___block_literal_global.480
+ ___block_literal_global.512
+ ___block_literal_global.64
+ ___block_literal_global.72
+ ___block_literal_global.89
+ ___block_literal_global.96
+ ___block_literal_global.98
+ _activate.classDebugEnabled.19
+ _activate.classDebugEnabled.21
+ _activate.classDebugEnabled.25
+ _activate.classDebugEnabled.27
+ _activate.classDebugEnabled.31
+ _activate.classDebugEnabled.37
+ _activate.classDebugEnabled.43
+ _activate.classDebugEnabled.49
+ _activate.defaultOnce.18
+ _activate.defaultOnce.20
+ _activate.defaultOnce.24
+ _activate.defaultOnce.26
+ _activate.defaultOnce.30
+ _activate.defaultOnce.36
+ _activate.defaultOnce.42
+ _activate.defaultOnce.48
+ _addDependency:.classDebugEnabled.88
+ _addDependency:.defaultOnce.87
+ _addDistributionEvent:.classDebugEnabled.33
+ _addDistributionEvent:.defaultOnce.32
+ _addDistributionEventIntervalWithLastDistributionEventBackward:withDistributionEventBackward:.classDebugEnabled.499
+ _addDistributionEventIntervalWithLastDistributionEventBackward:withDistributionEventBackward:.defaultOnce.498
+ _addDistributionEventIntervalWithLastDistributionEventForward:withDistributionEventForward:.classDebugEnabled.490
+ _addDistributionEventIntervalWithLastDistributionEventForward:withDistributionEventForward:.defaultOnce.489
+ _addEnergyEstimate:withNow:.classDebugEnabled.22
+ _addEnergyEstimate:withNow:.defaultOnce.21
+ _addEnergyMeasurementWithRootNodeID:withEnergy:withRange:.classDebugEnabled.578
+ _addEnergyMeasurementWithRootNodeID:withEnergy:withRange:.defaultOnce.577
+ _addQualificationEvent:.classDebugEnabled.26
+ _addQualificationEvent:.defaultOnce.25
+ _addQualificationEventIntervalWithLastQualificationEventBackward:withQualificationEventBackward:.classDebugEnabled.552
+ _addQualificationEventIntervalWithLastQualificationEventBackward:withQualificationEventBackward:.defaultOnce.551
+ _addQualificationEventIntervalWithLastQualificationEventForward:withQualificationEventForward:.classDebugEnabled.543
+ _addQualificationEventIntervalWithLastQualificationEventForward:withQualificationEventForward:.defaultOnce.542
+ _canFreeDependency:.classDebugEnabled.177
+ _canFreeDependency:.defaultOnce.176
+ _canFreeOwner:.classDebugEnabled.150
+ _canFreeOwner:.classDebugEnabled.156
+ _canFreeOwner:.defaultOnce.149
+ _canFreeOwner:.defaultOnce.155
+ _childEnergyEstimatesForParentEntryID:.classDebugEnabled.100
+ _childEnergyEstimatesForParentEntryID:.classDebugEnabled.94
+ _childEnergyEstimatesForParentEntryID:.defaultOnce.93
+ _childEnergyEstimatesForParentEntryID:.defaultOnce.99
+ _childNodeIDsFromChildNodeNames:.classDebugEnabled.49
+ _childNodeIDsFromChildNodeNames:.defaultOnce.48
+ _chunkWithLastChunkDate:withNow:.classDebugEnabled.587
+ _chunkWithLastChunkDate:withNow:.classDebugEnabled.600
+ _chunkWithLastChunkDate:withNow:.classDebugEnabled.606
+ _chunkWithLastChunkDate:withNow:.classDebugEnabled.609
+ _chunkWithLastChunkDate:withNow:.classDebugEnabled.612
+ _chunkWithLastChunkDate:withNow:.defaultOnce.586
+ _chunkWithLastChunkDate:withNow:.defaultOnce.599
+ _chunkWithLastChunkDate:withNow:.defaultOnce.605
+ _chunkWithLastChunkDate:withNow:.defaultOnce.608
+ _chunkWithLastChunkDate:withNow:.defaultOnce.611
+ _closeLastDistributionEventForwardWithDistributionID:withEndDate:.classDebugEnabled.51
+ _closeLastDistributionEventForwardWithDistributionID:withEndDate:.defaultOnce.50
+ _closeLastQualificationEventForwardWithQualificationID:withEndDate:.classDebugEnabled.43
+ _closeLastQualificationEventForwardWithQualificationID:withEndDate:.defaultOnce.42
+ _correct.classDebugEnabled.21
+ _correct.classDebugEnabled.27
+ _correct.classDebugEnabled.33
+ _correct.classDebugEnabled.39
+ _correct.classDebugEnabled.45
+ _correct.classDebugEnabled.52
+ _correct.classDebugEnabled.58
+ _correct.classDebugEnabled.64
+ _correct.defaultOnce.20
+ _correct.defaultOnce.26
+ _correct.defaultOnce.32
+ _correct.defaultOnce.38
+ _correct.defaultOnce.44
+ _correct.defaultOnce.51
+ _correct.defaultOnce.57
+ _correct.defaultOnce.63
+ _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.classDebugEnabled.28
+ _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.classDebugEnabled.34
+ _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.classDebugEnabled.40
+ _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.classDebugEnabled.49
+ _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.defaultOnce.27
+ _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.defaultOnce.33
+ _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.defaultOnce.39
+ _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.defaultOnce.48
+ _createAggregateRootNodeEnergyEntryWithEnergyEstimate:.classDebugEnabled.677
+ _createAggregateRootNodeEnergyEntryWithEnergyEstimate:.classDebugEnabled.683
+ _createAggregateRootNodeEnergyEntryWithEnergyEstimate:.defaultOnce.676
+ _createAggregateRootNodeEnergyEntryWithEnergyEstimate:.defaultOnce.682
+ _createEventWithEvent:withActionBlock:.classDebugEnabled.465
+ _createEventWithEvent:withActionBlock:.classDebugEnabled.471
+ _createEventWithEvent:withActionBlock:.defaultOnce.464
+ _createEventWithEvent:withActionBlock:.defaultOnce.470
+ _decryptData:withKey:.classDebugEnabled.115
+ _decryptData:withKey:.defaultOnce.114
+ _dependenciesWithDependencyID:withRange:.classDebugEnabled.126
+ _dependenciesWithDependencyID:withRange:.classDebugEnabled.129
+ _dependenciesWithDependencyID:withRange:.classDebugEnabled.135
+ _dependenciesWithDependencyID:withRange:.defaultOnce.125
+ _dependenciesWithDependencyID:withRange:.defaultOnce.128
+ _dependenciesWithDependencyID:withRange:.defaultOnce.134
+ _dependencyIDsForOwner:.classDebugEnabled.111
+ _dependencyIDsForOwner:.classDebugEnabled.119
+ _dependencyIDsForOwner:.classDebugEnabled.123
+ _dependencyIDsForOwner:.defaultOnce.110
+ _dependencyIDsForOwner:.defaultOnce.118
+ _dependencyIDsForOwner:.defaultOnce.122
+ _didCreateChildEnergyEstimate:withParentEnergyEstimate:.classDebugEnabled.514
+ _didCreateChildEnergyEstimate:withParentEnergyEstimate:.classDebugEnabled.519
+ _didCreateChildEnergyEstimate:withParentEnergyEstimate:.classDebugEnabled.525
+ _didCreateChildEnergyEstimate:withParentEnergyEstimate:.classDebugEnabled.531
+ _didCreateChildEnergyEstimate:withParentEnergyEstimate:.defaultOnce.513
+ _didCreateChildEnergyEstimate:withParentEnergyEstimate:.defaultOnce.518
+ _didCreateChildEnergyEstimate:withParentEnergyEstimate:.defaultOnce.524
+ _didCreateChildEnergyEstimate:withParentEnergyEstimate:.defaultOnce.530
+ _didQualifyEnergyEvent:withRootNodeID:withQualificationID:.classDebugEnabled.565
+ _didQualifyEnergyEvent:withRootNodeID:withQualificationID:.defaultOnce.564
+ _didReceiveDependency:.classDebugEnabled.58
+ _didReceiveDependency:.classDebugEnabled.67
+ _didReceiveDependency:.classDebugEnabled.73
+ _didReceiveDependency:.classDebugEnabled.79
+ _didReceiveDependency:.defaultOnce.57
+ _didReceiveDependency:.defaultOnce.66
+ _didReceiveDependency:.defaultOnce.72
+ _didReceiveDependency:.defaultOnce.78
+ _didReceiveOwner:.classDebugEnabled.36
+ _didReceiveOwner:.classDebugEnabled.42
+ _didReceiveOwner:.classDebugEnabled.48
+ _didReceiveOwner:.defaultOnce.35
+ _didReceiveOwner:.defaultOnce.41
+ _didReceiveOwner:.defaultOnce.47
+ _distribute.classDebugEnabled.21
+ _distribute.classDebugEnabled.27
+ _distribute.classDebugEnabled.33
+ _distribute.classDebugEnabled.39
+ _distribute.classDebugEnabled.45
+ _distribute.classDebugEnabled.51
+ _distribute.classDebugEnabled.57
+ _distribute.classDebugEnabled.63
+ _distribute.classDebugEnabled.72
+ _distribute.classDebugEnabled.79
+ _distribute.classDebugEnabled.85
+ _distribute.defaultOnce.20
+ _distribute.defaultOnce.26
+ _distribute.defaultOnce.32
+ _distribute.defaultOnce.38
+ _distribute.defaultOnce.44
+ _distribute.defaultOnce.50
+ _distribute.defaultOnce.56
+ _distribute.defaultOnce.62
+ _distribute.defaultOnce.71
+ _distribute.defaultOnce.78
+ _distribute.defaultOnce.84
+ _distributionRuleForRootNodeID:andNodeID:.classDebugEnabled.20
+ _distributionRuleForRootNodeID:andNodeID:.defaultOnce.19
+ _freeExpiredDependenciesAtNow:.classDebugEnabled.207
+ _freeExpiredDependenciesAtNow:.defaultOnce.206
+ _freeExpiredOwnersAtNow:.classDebugEnabled.186
+ _freeExpiredOwnersAtNow:.classDebugEnabled.192
+ _freeExpiredOwnersAtNow:.classDebugEnabled.198
+ _freeExpiredOwnersAtNow:.defaultOnce.185
+ _freeExpiredOwnersAtNow:.defaultOnce.191
+ _freeExpiredOwnersAtNow:.defaultOnce.197
+ _indexRule:.classDebugEnabled.55
+ _indexRule:.classDebugEnabled.70
+ _indexRule:.defaultOnce.54
+ _indexRule:.defaultOnce.69
+ _initWithNodeID:withRootNodeID:withParentEntryID:withNumAncestors:withEnergy:withRange:withEntryDate:.classDebugEnabled.24
+ _initWithNodeID:withRootNodeID:withParentEntryID:withNumAncestors:withEnergy:withRange:withEntryDate:.defaultOnce.23
+ _intersect:.classDebugEnabled.19
+ _intersect:.classDebugEnabled.25
+ _intersect:.classDebugEnabled.31
+ _intersect:.defaultOnce.18
+ _intersect:.defaultOnce.24
+ _intersect:.defaultOnce.30
+ _isValidPower:forRootNodeID:.classDebugEnabled.21
+ _isValidPower:forRootNodeID:.classDebugEnabled.27
+ _isValidPower:forRootNodeID:.defaultOnce.20
+ _isValidPower:forRootNodeID:.defaultOnce.26
+ _lastAllRunDateForOwnerID:.classDebugEnabled
+ _lastAllRunDateForOwnerID:.classDebugEnabled.162
+ _lastAllRunDateForOwnerID:.defaultOnce
+ _lastAllRunDateForOwnerID:.defaultOnce.161
+ _loadRules.classDebugEnabled.27
+ _loadRules.classDebugEnabled.34
+ _loadRules.classDebugEnabled.40
+ _loadRules.classDebugEnabled.47
+ _loadRules.classDebugEnabled.52
+ _loadRules.defaultOnce.26
+ _loadRules.defaultOnce.33
+ _loadRules.defaultOnce.39
+ _loadRules.defaultOnce.46
+ _loadRules.defaultOnce.51
+ _mergeWithEvent:.classDebugEnabled.57
+ _mergeWithEvent:.defaultOnce.56
+ _nodeIDForNodeName:isPermanent:.classDebugEnabled.20
+ _nodeIDForNodeName:isPermanent:.classDebugEnabled.26
+ _nodeIDForNodeName:isPermanent:.classDebugEnabled.35
+ _nodeIDForNodeName:isPermanent:.defaultOnce.19
+ _nodeIDForNodeName:isPermanent:.defaultOnce.25
+ _nodeIDForNodeName:isPermanent:.defaultOnce.34
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$lastAllRunDateForOwnerID:
+ _objc_msgSend$ownerIDToLastAllRunDate
+ _objc_msgSend$setSkipLastAllRunDateCheck:
+ _objc_msgSend$skipLastAllRunDateCheck
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _overlaps:.classDebugEnabled.37
+ _overlaps:.classDebugEnabled.43
+ _overlaps:.classDebugEnabled.49
+ _overlaps:.defaultOnce.36
+ _overlaps:.defaultOnce.42
+ _overlaps:.defaultOnce.48
+ _ownerIDsForDependency:.classDebugEnabled.120
+ _ownerIDsForDependency:.classDebugEnabled.133
+ _ownerIDsForDependency:.classDebugEnabled.137
+ _ownerIDsForDependency:.defaultOnce.119
+ _ownerIDsForDependency:.defaultOnce.132
+ _ownerIDsForDependency:.defaultOnce.136
+ _qualify.classDebugEnabled.21
+ _qualify.classDebugEnabled.27
+ _qualify.classDebugEnabled.33
+ _qualify.classDebugEnabled.39
+ _qualify.classDebugEnabled.46
+ _qualify.classDebugEnabled.52
+ _qualify.classDebugEnabled.58
+ _qualify.classDebugEnabled.64
+ _qualify.classDebugEnabled.70
+ _qualify.classDebugEnabled.77
+ _qualify.defaultOnce.20
+ _qualify.defaultOnce.26
+ _qualify.defaultOnce.32
+ _qualify.defaultOnce.38
+ _qualify.defaultOnce.45
+ _qualify.defaultOnce.51
+ _qualify.defaultOnce.57
+ _qualify.defaultOnce.63
+ _qualify.defaultOnce.69
+ _qualify.defaultOnce.76
+ _rangeSinceEvent:.classDebugEnabled.27
+ _rangeSinceEvent:.classDebugEnabled.33
+ _rangeSinceEvent:.classDebugEnabled.39
+ _rangeSinceEvent:.classDebugEnabled.45
+ _rangeSinceEvent:.defaultOnce.26
+ _rangeSinceEvent:.defaultOnce.32
+ _rangeSinceEvent:.defaultOnce.38
+ _rangeSinceEvent:.defaultOnce.44
+ _reloadDependenciesNewerThanDate:.classDebugEnabled.100
+ _reloadDependenciesNewerThanDate:.classDebugEnabled.106
+ _reloadDependenciesNewerThanDate:.classDebugEnabled.56
+ _reloadDependenciesNewerThanDate:.classDebugEnabled.65
+ _reloadDependenciesNewerThanDate:.classDebugEnabled.73
+ _reloadDependenciesNewerThanDate:.classDebugEnabled.74
+ _reloadDependenciesNewerThanDate:.classDebugEnabled.79
+ _reloadDependenciesNewerThanDate:.classDebugEnabled.93
+ _reloadDependenciesNewerThanDate:.defaultOnce.105
+ _reloadDependenciesNewerThanDate:.defaultOnce.55
+ _reloadDependenciesNewerThanDate:.defaultOnce.64
+ _reloadDependenciesNewerThanDate:.defaultOnce.72
+ _reloadDependenciesNewerThanDate:.defaultOnce.73
+ _reloadDependenciesNewerThanDate:.defaultOnce.78
+ _reloadDependenciesNewerThanDate:.defaultOnce.92
+ _reloadDependenciesNewerThanDate:.defaultOnce.99
+ _reloadLastDistributionEventsWithLastDeviceBootDate:.classDebugEnabled.640
+ _reloadLastDistributionEventsWithLastDeviceBootDate:.classDebugEnabled.650
+ _reloadLastDistributionEventsWithLastDeviceBootDate:.classDebugEnabled.656
+ _reloadLastDistributionEventsWithLastDeviceBootDate:.defaultOnce.639
+ _reloadLastDistributionEventsWithLastDeviceBootDate:.defaultOnce.649
+ _reloadLastDistributionEventsWithLastDeviceBootDate:.defaultOnce.655
+ _reloadLastPowerEventsWithLastDeviceBootDate:.classDebugEnabled.631
+ _reloadLastPowerEventsWithLastDeviceBootDate:.classDebugEnabled.637
+ _reloadLastPowerEventsWithLastDeviceBootDate:.defaultOnce.630
+ _reloadLastPowerEventsWithLastDeviceBootDate:.defaultOnce.636
+ _reloadLastQualificationEventsWithLastDeviceBootDate:.classDebugEnabled.659
+ _reloadLastQualificationEventsWithLastDeviceBootDate:.classDebugEnabled.668
+ _reloadLastQualificationEventsWithLastDeviceBootDate:.classDebugEnabled.674
+ _reloadLastQualificationEventsWithLastDeviceBootDate:.defaultOnce.658
+ _reloadLastQualificationEventsWithLastDeviceBootDate:.defaultOnce.667
+ _reloadLastQualificationEventsWithLastDeviceBootDate:.defaultOnce.673
+ _ruleWithString:withEntryDate:.classDebugEnabled.38
+ _ruleWithString:withEntryDate:.classDebugEnabled.45
+ _ruleWithString:withEntryDate:.classDebugEnabled.47
+ _ruleWithString:withEntryDate:.classDebugEnabled.53
+ _ruleWithString:withEntryDate:.classDebugEnabled.60
+ _ruleWithString:withEntryDate:.defaultOnce.37
+ _ruleWithString:withEntryDate:.defaultOnce.44
+ _ruleWithString:withEntryDate:.defaultOnce.46
+ _ruleWithString:withEntryDate:.defaultOnce.52
+ _ruleWithString:withEntryDate:.defaultOnce.59
+ _rulesFromFileWithForceLoad:.classDebugEnabled.104
+ _rulesFromFileWithForceLoad:.classDebugEnabled.73
+ _rulesFromFileWithForceLoad:.classDebugEnabled.80
+ _rulesFromFileWithForceLoad:.classDebugEnabled.90
+ _rulesFromFileWithForceLoad:.classDebugEnabled.98
+ _rulesFromFileWithForceLoad:.defaultOnce.103
+ _rulesFromFileWithForceLoad:.defaultOnce.72
+ _rulesFromFileWithForceLoad:.defaultOnce.79
+ _rulesFromFileWithForceLoad:.defaultOnce.89
+ _rulesFromFileWithForceLoad:.defaultOnce.97
+ _startObservingDependencyID:forOwner:.classDebugEnabled.144
+ _startObservingDependencyID:forOwner:.defaultOnce.143
+ _startObservingOwnerID:forDependency:.classDebugEnabled.171
+ _startObservingOwnerID:forDependency:.defaultOnce.170
+ _stopObservingDependencyID:forOwner:.classDebugEnabled.147
+ _stopObservingDependencyID:forOwner:.defaultOnce.146
+ _stopObservingOwnerID:forDependency:.classDebugEnabled.174
+ _stopObservingOwnerID:forDependency:.defaultOnce.173
+ _updateWithEndDate:.classDebugEnabled.57
+ _updateWithEndDate:.classDebugEnabled.64
+ _updateWithEndDate:.defaultOnce.56
+ _updateWithEndDate:.defaultOnce.63
- -[PLAccountingEngine createEventWithEvent:withActionBlock:].cold.4
- -[PLAccountingEngine createEventWithEvent:withActionBlock:].cold.5
- -[PLAccountingEngine createEventWithEvent:withActionBlock:].cold.6
- GCC_except_table149
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.101
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.28
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.35
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.41
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.47
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.73
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.79
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.88
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.95
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.100
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.27
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.34
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.40
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.46
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.72
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.78
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.87
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.94
- _PLSubmissionAnalyticsStateSuccess_block_invoke_13.classDebugEnabled.434
- _PLSubmissionAnalyticsStateSuccess_block_invoke_13.defaultOnce.433
- _PLSubmissionAnalyticsStateSuccess_block_invoke_18.classDebugEnabled.632
- _PLSubmissionAnalyticsStateSuccess_block_invoke_18.defaultOnce.631
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.53
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.52
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.388
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.63
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.70
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.77
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.83
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.387
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.62
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.69
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.76
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.82
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled.89
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce.88
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.106
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.112
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.400
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.99
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.105
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.111
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.399
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.98
- _PLSubmissionAnalyticsStateSuccess_block_invoke_7.classDebugEnabled.408
- _PLSubmissionAnalyticsStateSuccess_block_invoke_7.defaultOnce.407
- _PLSubmissionAnalyticsStateSuccess_block_invoke_8.classDebugEnabled.414
- _PLSubmissionAnalyticsStateSuccess_block_invoke_8.defaultOnce.413
- ___102-[PLAccountingQualificationManager closeLastQualificationEventForwardWithQualificationID:withEndDate:]_block_invoke.41
- ___104-[PLAccountingEngine createQualificationEventPointWithQualificationID:withChildNodeNames:withStartDate:]_block_invoke.452
- ___105-[PLAccountingEngine createQualificationEventBackwardWithQualificationID:withChildNodeNames:withEndDate:]_block_invoke.447
- ___106-[PLAccountingEngine createQualificationEventForwardWithQualificationID:withChildNodeNames:withStartDate:]_block_invoke.443
- ___109-[PLAccountingEngine createDistributionEventPointWithDistributionID:withChildNodeNameToWeight:withStartDate:]_block_invoke.429
- ___110-[PLAccountingEngine createDistributionEventBackwardWithDistributionID:withChildNodeNameToWeight:withEndDate:]_block_invoke.424
- ___111-[PLAccountingEngine createDistributionEventForwardWithDistributionID:withChildNodeNameToWeight:withStartDate:]_block_invoke.420
- ___112-[PLAccountingEngine addDistributionEventIntervalWithLastDistributionEventForward:withDistributionEventForward:]_block_invoke.498
- ___114-[PLAccountingEngine addDistributionEventIntervalWithLastDistributionEventBackward:withDistributionEventBackward:]_block_invoke.507
- ___115-[PLAccountingEngine addQualificationEventIntervalWithLastQualificationEventForward:withQualificationEventForward:]_block_invoke.551
- ___117-[PLAccountingEngine addQualificationEventIntervalWithLastQualificationEventBackward:withQualificationEventBackward:]_block_invoke.560
- ___119-[PLAccountingEngine createQualificationEventIntervalWithQualificationID:withChildNodeNames:withStartDate:withEndDate:]_block_invoke.451
- ___124-[PLAccountingEngine createDistributionEventIntervalWithDistributionID:withChildNodeNameToWeight:withStartDate:withEndDate:]_block_invoke.428
- ___140-[PLAccountingEnergyEstimateEventEntry initWithNodeID:withRootNodeID:withParentEntryID:withNumAncestors:withEnergy:withRange:withEntryDate:]_block_invoke.22
- ___27-[PLAccountingEngine reset]_block_invoke.40
- ___27-[PLAccountingEngine reset]_block_invoke.40.cold.1
- ___28-[PLAccountingEngine reload]_block_invoke.633
- ___29-[PLAccountingOwner activate]_block_invoke.17
- ___29-[PLAccountingOwner activate]_block_invoke.23
- ___29-[PLAccountingOwner activate]_block_invoke.29
- ___29-[PLAccountingOwner activate]_block_invoke.35
- ___29-[PLAccountingOwner activate]_block_invoke.41
- ___29-[PLAccountingOwner activate]_block_invoke.47
- ___30-[PLAccountingRange overlaps:]_block_invoke.35
- ___30-[PLAccountingRange overlaps:]_block_invoke.41
- ___30-[PLAccountingRange overlaps:]_block_invoke.47
- ___31-[PLAccountingRange intersect:]_block_invoke.17
- ___31-[PLAccountingRange intersect:]_block_invoke.23
- ___31-[PLAccountingRange intersect:]_block_invoke.29
- ___34-[PLAccountingDependency activate]_block_invoke.17
- ___34-[PLAccountingDependency activate]_block_invoke.23
- ___34-[PLAccountingDependency activate]_block_invoke.29
- ___34-[PLAccountingDependency activate]_block_invoke.35
- ___35-[PLAccountingOwner addDependency:]_block_invoke.86
- ___36-[PLAccountingRuleManager loadRules]_block_invoke.25
- ___36-[PLAccountingRuleManager loadRules]_block_invoke.32
- ___36-[PLAccountingRuleManager loadRules]_block_invoke.38
- ___36-[PLAccountingRuleManager loadRules]_block_invoke.42
- ___36-[PLAccountingRuleManager loadRules]_block_invoke.50
- ___37-[PLAccountingNodeManager setupNodes]_block_invoke.102
- ___37-[PLAccountingNodeManager setupNodes]_block_invoke.65
- ___37-[PLAccountingNodeManager setupNodes]_block_invoke.74
- ___37-[PLAccountingNodeManager setupNodes]_block_invoke.80
- ___37-[PLAccountingNodeManager setupNodes]_block_invoke.84
- ___37-[PLAccountingNodeManager setupNodes]_block_invoke.96
- ___38-[PLAccountingCorrectionOwner correct]_block_invoke.19
- ___38-[PLAccountingCorrectionOwner correct]_block_invoke.25
- ___38-[PLAccountingCorrectionOwner correct]_block_invoke.31
- ___38-[PLAccountingCorrectionOwner correct]_block_invoke.37
- ___38-[PLAccountingCorrectionOwner correct]_block_invoke.43
- ___38-[PLAccountingCorrectionOwner correct]_block_invoke.50
- ___38-[PLAccountingCorrectionOwner correct]_block_invoke.56
- ___38-[PLAccountingCorrectionOwner correct]_block_invoke.62
- ___41-[PLAccountingEventEntry mergeWithEvent:]_block_invoke.49
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.19
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.25
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.31
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.37
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.44
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.50
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.56
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.62
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.68
- ___41-[PLAccountingQualificationOwner qualify]_block_invoke.75
- ___42-[PLAccountingDependency didReceiveOwner:]_block_invoke.44
- ___42-[PLAccountingDependency didReceiveOwner:]_block_invoke.47
- ___42-[PLAccountingDependency didReceiveOwner:]_block_invoke.53
- ___42-[PLAccountingEventEntry rangeSinceEvent:]_block_invoke.25
- ___42-[PLAccountingEventEntry rangeSinceEvent:]_block_invoke.31
- ___42-[PLAccountingEventEntry rangeSinceEvent:]_block_invoke.37
- ___42-[PLAccountingEventEntry rangeSinceEvent:]_block_invoke.43
- ___42-[PLAccountingOwner didReceiveDependency:]_block_invoke.56
- ___42-[PLAccountingOwner didReceiveDependency:]_block_invoke.62
- ___42-[PLAccountingOwner didReceiveDependency:]_block_invoke.71
- ___42-[PLAccountingOwner didReceiveDependency:]_block_invoke.77
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.19
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.25
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.31
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.37
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.43
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.49
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.55
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.61
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.68
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.75
- ___43-[PLAccountingDistributionOwner distribute]_block_invoke.81
- ___44-[PLAccountingDependency updateWithEndDate:]_block_invoke.59
- ___44-[PLAccountingDependency updateWithEndDate:]_block_invoke.66
- ___47+[PLAccountingRuleManager decryptData:withKey:]_block_invoke.113
- ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.29
- ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.36
- ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.42
- ___47-[PLAccountingOwnerDependencyManager addOwner:]_block_invoke.48
- ___49-[PLAccountingDistributionRuleManager indexRule:]_block_invoke.68
- ___50-[PLAccountingQualificationRuleManager indexRule:]_block_invoke.53
- ___51-[PLAccountingOwnerDependencyManager canFreeOwner:]_block_invoke.146
- ___52-[PLAccountingOwnerDependencyManager addDependency:]_block_invoke.64
- ___52-[PLAccountingOwnerDependencyManager addDependency:]_block_invoke.71
- ___52-[PLAccountingOwnerDependencyManager addDependency:]_block_invoke.78
- ___52-[PLAccountingOwnerDependencyManager addDependency:]_block_invoke.84
- ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.595
- ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.608
- ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.614
- ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.617
- ___53-[PLAccountingEngine chunkWithLastChunkDate:withNow:]_block_invoke.620
- ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.102
- ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.71
- ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.78
- ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.88
- ___54-[PLAccountingRuleManager rulesFromFileWithForceLoad:]_block_invoke.96
- ___55-[PLAccountingCorrectionManager dependencyIDsForOwner:]_block_invoke.109
- ___55-[PLAccountingCorrectionManager ownerIDsForDependency:]_block_invoke.118
- ___56-[PLAccountingDistributionManager addDistributionEvent:]_block_invoke.31
- ___56-[PLAccountingOwnerDependencyManager canFreeDependency:]_block_invoke.158
- ___57-[PLAccountingDistributionManager dependencyIDsForOwner:]_block_invoke.121
- ___57-[PLAccountingDistributionManager ownerIDsForDependency:]_block_invoke.131
- ___57-[PLAccountingDistributionManager ownerIDsForDependency:]_block_invoke.135
- ___57-[PLAccountingNodeManager nodeIDForNodeName:isPermanent:]_block_invoke.18
- ___57-[PLAccountingNodeManager nodeIDForNodeName:isPermanent:]_block_invoke.24
- ___57-[PLAccountingNodeManager nodeIDForNodeName:isPermanent:]_block_invoke.30
- ___58+[PLAccountingPowerEventEntry isValidPower:forRootNodeID:]_block_invoke.19
- ___58+[PLAccountingPowerEventEntry isValidPower:forRootNodeID:]_block_invoke.25
- ___58-[PLAccountingCorrectionManager didCorrectEnergyEstimate:]_block_invoke.102
- ___58-[PLAccountingNodeManager childNodeIDsFromChildNodeNames:]_block_invoke.47
- ___58-[PLAccountingQualificationManager addQualificationEvent:]_block_invoke.24
- ___58-[PLAccountingQualificationManager dependencyIDsForOwner:]_block_invoke.117
- ___58-[PLAccountingQualificationManager dependencyIDsForOwner:]_block_invoke.121
- ___59-[PLAccountingEngine createEventWithEvent:withActionBlock:]_block_invoke.458
- ___59-[PLAccountingEngine createEventWithEvent:withActionBlock:]_block_invoke.464
- ___59-[PLAccountingEngine createEventWithEvent:withActionBlock:]_block_invoke.470
- ___59-[PLAccountingEngine createEventWithEvent:withActionBlock:]_block_invoke.480
- ___61-[PLAccountingDistributionManager addEnergyEstimate:withNow:]_block_invoke.20
- ___61-[PLAccountingOwnerDependencyManager freeExpiredOwnersAtNow:]_block_invoke.167
- ___61-[PLAccountingOwnerDependencyManager freeExpiredOwnersAtNow:]_block_invoke.173
- ___61-[PLAccountingOwnerDependencyManager freeExpiredOwnersAtNow:]_block_invoke.179
- ___63-[PLAccountingDistributionManager didDistributeEnergyEstimate:]_block_invoke.115
- ___65-[PLAccountingCorrectionManager reloadDependenciesNewerThanDate:]_block_invoke.71
- ___65-[PLAccountingCorrectionManager reloadDependenciesNewerThanDate:]_block_invoke.77
- ___65-[PLAccountingOwnerDependencyManager notifyOwnersWithDependency:]_block_invoke.90
- ___66-[PLAccountingEngine reloadLastPowerEventsWithLastDeviceBootDate:]_block_invoke.639
- ___66-[PLAccountingEngine reloadLastPowerEventsWithLastDeviceBootDate:]_block_invoke.645
- ___66-[PLAccountingOwnerDependencyManager notifyDependenciesWithOwner:]_block_invoke.54
- ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.104
- ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.63
- ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.72
- ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.91
- ___67-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:]_block_invoke.98
- ___67-[PLAccountingOwnerDependencyManager freeExpiredDependenciesAtNow:]_block_invoke.188
- ___68-[PLAccountingDistributionRuleManager ruleWithString:withEntryDate:]_block_invoke.45
- ___68-[PLAccountingDistributionRuleManager ruleWithString:withEntryDate:]_block_invoke.51
- ___68-[PLAccountingDistributionRuleManager ruleWithString:withEntryDate:]_block_invoke.58
- ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.104
- ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.54
- ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.60
- ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.72
- ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.91
- ___68-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:]_block_invoke.98
- ___69-[PLAccountingQualificationRuleManager ruleWithString:withEntryDate:]_block_invoke.36
- ___69-[PLAccountingQualificationRuleManager ruleWithString:withEntryDate:]_block_invoke.43
- ___70-[PLAccountingCorrectionManager childEnergyEstimatesForParentEntryID:]_block_invoke.92
- ___70-[PLAccountingCorrectionManager childEnergyEstimatesForParentEntryID:]_block_invoke.98
- ___72-[PLAccountingEngine currentDistributionEventForwardWithDistributionID:]_block_invoke.435
- ___73-[PLAccountingEngine reloadLastDistributionEventsWithLastDeviceBootDate:]_block_invoke.648
- ___73-[PLAccountingEngine reloadLastDistributionEventsWithLastDeviceBootDate:]_block_invoke.658
- ___73-[PLAccountingEngine reloadLastDistributionEventsWithLastDeviceBootDate:]_block_invoke.664
- ___73-[PLAccountingOwnerDependencyManager stopObservingDependencyID:forOwner:]_block_invoke.143
- ___73-[PLAccountingOwnerDependencyManager stopObservingOwnerID:forDependency:]_block_invoke.155
- ___73-[PLAccountingOwnerDependencyManager updateLastDependencyID:withEndDate:]_block_invoke.100
- ___73-[PLAccountingOwnerDependencyManager updateLastDependencyID:withEndDate:]_block_invoke.107
- ___73-[PLAccountingOwnerDependencyManager updateLastDependencyID:withEndDate:]_block_invoke.113
- ___74-[PLAccountingEngine reloadLastQualificationEventsWithLastDeviceBootDate:]_block_invoke.667
- ___74-[PLAccountingEngine reloadLastQualificationEventsWithLastDeviceBootDate:]_block_invoke.676
- ___74-[PLAccountingEngine reloadLastQualificationEventsWithLastDeviceBootDate:]_block_invoke.682
- ___74-[PLAccountingOwnerDependencyManager startObservingDependencyID:forOwner:]_block_invoke.140
- ___74-[PLAccountingOwnerDependencyManager startObservingOwnerID:forDependency:]_block_invoke.152
- ___75-[PLAccountingEngine createAggregateRootNodeEnergyEntryWithEnergyEstimate:]_block_invoke.685
- ___75-[PLAccountingEngine createAggregateRootNodeEnergyEntryWithEnergyEstimate:]_block_invoke.691
- ___76-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:]_block_invoke.517
- ___76-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:]_block_invoke.527
- ___76-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:]_block_invoke.533
- ___76-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:]_block_invoke.539
- ___77-[PLAccountingOwnerDependencyManager dependenciesWithDependencyID:withRange:]_block_invoke.122
- ___77-[PLAccountingOwnerDependencyManager dependenciesWithDependencyID:withRange:]_block_invoke.125
- ___77-[PLAccountingOwnerDependencyManager dependenciesWithDependencyID:withRange:]_block_invoke.131
- ___78-[PLAccountingEngine addEnergyMeasurementWithRootNodeID:withEnergy:withRange:]_block_invoke.586
- ___79-[PLAccountingDistributionRuleManager distributionRuleForRootNodeID:andNodeID:]_block_invoke.18
- ___79-[PLAccountingEngine didQualifyEnergyEvent:withRootNodeID:withQualificationID:]_block_invoke.573
- ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.397
- ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.397.cold.1
- ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.397.cold.2
- ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke.401
- ___83-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:]_block_invoke_2.398
- ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.381
- ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.381.cold.1
- ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.381.cold.2
- ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke.389
- ___84-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:]_block_invoke_2.382
- ___90-[PLAccountingEngine addPowerMeasurementEventIntervalWithPower:withStartDate:withEndDate:]_block_invoke.415
- ___93-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:]_block_invoke.26
- ___93-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:]_block_invoke.32
- ___93-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:]_block_invoke.38
- ___93-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:]_block_invoke.42
- ___93-[PLAccountingQualificationManager didQualifyEnergyEvent:withRootNodeID:withQualificationID:]_block_invoke.111
- ___95-[PLAccountingDistributionManager didDistributeToChildEnergyEstimate:fromParentEnergyEstimate:]_block_invoke.111
- ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.405
- ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.405.cold.1
- ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.405.cold.2
- ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke.409
- ___97-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:]_block_invoke_2.406
- ___99-[PLAccountingDistributionManager closeLastDistributionEventForwardWithDistributionID:withEndDate:]_block_invoke.49
- ___block_literal_global.13
- ___block_literal_global.158
- ___block_literal_global.160
- ___block_literal_global.331
- ___block_literal_global.489
- ___block_literal_global.519
- ___block_literal_global.61
- ___block_literal_global.69
- ___block_literal_global.86
- ___block_literal_global.93
- ___block_literal_global.95
- _activate.classDebugEnabled.16
- _activate.classDebugEnabled.22
- _activate.classDebugEnabled.28
- _activate.classDebugEnabled.34
- _activate.classDebugEnabled.40
- _activate.classDebugEnabled.46
- _activate.defaultOnce.15
- _activate.defaultOnce.21
- _activate.defaultOnce.27
- _activate.defaultOnce.33
- _activate.defaultOnce.39
- _activate.defaultOnce.45
- _addDependency:.classDebugEnabled.85
- _addDependency:.defaultOnce.84
- _addDistributionEvent:.classDebugEnabled.30
- _addDistributionEvent:.defaultOnce.29
- _addDistributionEventIntervalWithLastDistributionEventBackward:withDistributionEventBackward:.classDebugEnabled.506
- _addDistributionEventIntervalWithLastDistributionEventBackward:withDistributionEventBackward:.defaultOnce.505
- _addDistributionEventIntervalWithLastDistributionEventForward:withDistributionEventForward:.classDebugEnabled.497
- _addDistributionEventIntervalWithLastDistributionEventForward:withDistributionEventForward:.defaultOnce.496
- _addEnergyEstimate:withNow:.classDebugEnabled.19
- _addEnergyEstimate:withNow:.defaultOnce.18
- _addEnergyMeasurementWithRootNodeID:withEnergy:withRange:.classDebugEnabled.585
- _addEnergyMeasurementWithRootNodeID:withEnergy:withRange:.defaultOnce.584
- _addQualificationEvent:.classDebugEnabled.23
- _addQualificationEvent:.defaultOnce.22
- _addQualificationEventIntervalWithLastQualificationEventBackward:withQualificationEventBackward:.classDebugEnabled.559
- _addQualificationEventIntervalWithLastQualificationEventBackward:withQualificationEventBackward:.defaultOnce.558
- _addQualificationEventIntervalWithLastQualificationEventForward:withQualificationEventForward:.classDebugEnabled.550
- _addQualificationEventIntervalWithLastQualificationEventForward:withQualificationEventForward:.defaultOnce.549
- _canFreeDependency:.classDebugEnabled.157
- _canFreeDependency:.defaultOnce.156
- _canFreeOwner:.classDebugEnabled.145
- _canFreeOwner:.defaultOnce.144
- _childEnergyEstimatesForParentEntryID:.classDebugEnabled.91
- _childEnergyEstimatesForParentEntryID:.classDebugEnabled.97
- _childEnergyEstimatesForParentEntryID:.defaultOnce.90
- _childEnergyEstimatesForParentEntryID:.defaultOnce.96
- _childNodeIDsFromChildNodeNames:.classDebugEnabled.46
- _childNodeIDsFromChildNodeNames:.defaultOnce.45
- _chunkWithLastChunkDate:withNow:.classDebugEnabled.594
- _chunkWithLastChunkDate:withNow:.classDebugEnabled.607
- _chunkWithLastChunkDate:withNow:.classDebugEnabled.613
- _chunkWithLastChunkDate:withNow:.classDebugEnabled.616
- _chunkWithLastChunkDate:withNow:.classDebugEnabled.619
- _chunkWithLastChunkDate:withNow:.defaultOnce.593
- _chunkWithLastChunkDate:withNow:.defaultOnce.606
- _chunkWithLastChunkDate:withNow:.defaultOnce.612
- _chunkWithLastChunkDate:withNow:.defaultOnce.615
- _chunkWithLastChunkDate:withNow:.defaultOnce.618
- _closeLastDistributionEventForwardWithDistributionID:withEndDate:.classDebugEnabled.48
- _closeLastDistributionEventForwardWithDistributionID:withEndDate:.defaultOnce.47
- _closeLastQualificationEventForwardWithQualificationID:withEndDate:.classDebugEnabled.40
- _closeLastQualificationEventForwardWithQualificationID:withEndDate:.defaultOnce.39
- _correct.classDebugEnabled.18
- _correct.classDebugEnabled.24
- _correct.classDebugEnabled.30
- _correct.classDebugEnabled.36
- _correct.classDebugEnabled.42
- _correct.classDebugEnabled.49
- _correct.classDebugEnabled.55
- _correct.classDebugEnabled.61
- _correct.defaultOnce.17
- _correct.defaultOnce.23
- _correct.defaultOnce.29
- _correct.defaultOnce.35
- _correct.defaultOnce.41
- _correct.defaultOnce.48
- _correct.defaultOnce.54
- _correct.defaultOnce.60
- _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.classDebugEnabled.25
- _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.classDebugEnabled.31
- _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.classDebugEnabled.37
- _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.classDebugEnabled.46
- _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.defaultOnce.24
- _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.defaultOnce.30
- _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.defaultOnce.36
- _correctChildEnergyEstimate:withParentEnergyEstimate:withNow:.defaultOnce.45
- _createAggregateRootNodeEnergyEntryWithEnergyEstimate:.classDebugEnabled.684
- _createAggregateRootNodeEnergyEntryWithEnergyEstimate:.classDebugEnabled.690
- _createAggregateRootNodeEnergyEntryWithEnergyEstimate:.defaultOnce.683
- _createAggregateRootNodeEnergyEntryWithEnergyEstimate:.defaultOnce.689
- _createEventWithEvent:withActionBlock:.classDebugEnabled.457
- _createEventWithEvent:withActionBlock:.classDebugEnabled.463
- _createEventWithEvent:withActionBlock:.classDebugEnabled.469
- _createEventWithEvent:withActionBlock:.classDebugEnabled.475
- _createEventWithEvent:withActionBlock:.classDebugEnabled.484
- _createEventWithEvent:withActionBlock:.defaultOnce.456
- _createEventWithEvent:withActionBlock:.defaultOnce.462
- _createEventWithEvent:withActionBlock:.defaultOnce.468
- _createEventWithEvent:withActionBlock:.defaultOnce.474
- _createEventWithEvent:withActionBlock:.defaultOnce.483
- _decryptData:withKey:.classDebugEnabled.112
- _decryptData:withKey:.defaultOnce.111
- _dependenciesWithDependencyID:withRange:.classDebugEnabled.121
- _dependenciesWithDependencyID:withRange:.classDebugEnabled.124
- _dependenciesWithDependencyID:withRange:.classDebugEnabled.130
- _dependenciesWithDependencyID:withRange:.defaultOnce.120
- _dependenciesWithDependencyID:withRange:.defaultOnce.123
- _dependenciesWithDependencyID:withRange:.defaultOnce.129
- _dependencyIDsForOwner:.classDebugEnabled.108
- _dependencyIDsForOwner:.classDebugEnabled.116
- _dependencyIDsForOwner:.classDebugEnabled.120
- _dependencyIDsForOwner:.defaultOnce.107
- _dependencyIDsForOwner:.defaultOnce.115
- _dependencyIDsForOwner:.defaultOnce.119
- _didCreateChildEnergyEstimate:withParentEnergyEstimate:.classDebugEnabled.521
- _didCreateChildEnergyEstimate:withParentEnergyEstimate:.classDebugEnabled.526
- _didCreateChildEnergyEstimate:withParentEnergyEstimate:.classDebugEnabled.532
- _didCreateChildEnergyEstimate:withParentEnergyEstimate:.classDebugEnabled.538
- _didCreateChildEnergyEstimate:withParentEnergyEstimate:.defaultOnce.520
- _didCreateChildEnergyEstimate:withParentEnergyEstimate:.defaultOnce.525
- _didCreateChildEnergyEstimate:withParentEnergyEstimate:.defaultOnce.531
- _didCreateChildEnergyEstimate:withParentEnergyEstimate:.defaultOnce.537
- _didQualifyEnergyEvent:withRootNodeID:withQualificationID:.classDebugEnabled.572
- _didQualifyEnergyEvent:withRootNodeID:withQualificationID:.defaultOnce.571
- _didReceiveDependency:.classDebugEnabled.55
- _didReceiveDependency:.classDebugEnabled.61
- _didReceiveDependency:.classDebugEnabled.70
- _didReceiveDependency:.classDebugEnabled.76
- _didReceiveDependency:.defaultOnce.54
- _didReceiveDependency:.defaultOnce.60
- _didReceiveDependency:.defaultOnce.69
- _didReceiveDependency:.defaultOnce.75
- _didReceiveOwner:.classDebugEnabled.43
- _didReceiveOwner:.classDebugEnabled.46
- _didReceiveOwner:.classDebugEnabled.52
- _didReceiveOwner:.defaultOnce.42
- _didReceiveOwner:.defaultOnce.45
- _didReceiveOwner:.defaultOnce.51
- _distribute.classDebugEnabled.18
- _distribute.classDebugEnabled.24
- _distribute.classDebugEnabled.30
- _distribute.classDebugEnabled.36
- _distribute.classDebugEnabled.42
- _distribute.classDebugEnabled.48
- _distribute.classDebugEnabled.54
- _distribute.classDebugEnabled.60
- _distribute.classDebugEnabled.67
- _distribute.classDebugEnabled.74
- _distribute.classDebugEnabled.80
- _distribute.defaultOnce.17
- _distribute.defaultOnce.23
- _distribute.defaultOnce.29
- _distribute.defaultOnce.35
- _distribute.defaultOnce.41
- _distribute.defaultOnce.47
- _distribute.defaultOnce.53
- _distribute.defaultOnce.59
- _distribute.defaultOnce.66
- _distribute.defaultOnce.73
- _distribute.defaultOnce.79
- _distributionRuleForRootNodeID:andNodeID:.classDebugEnabled.17
- _distributionRuleForRootNodeID:andNodeID:.defaultOnce.16
- _freeExpiredDependenciesAtNow:.classDebugEnabled.187
- _freeExpiredDependenciesAtNow:.defaultOnce.186
- _freeExpiredOwnersAtNow:.classDebugEnabled.166
- _freeExpiredOwnersAtNow:.classDebugEnabled.172
- _freeExpiredOwnersAtNow:.classDebugEnabled.178
- _freeExpiredOwnersAtNow:.defaultOnce.165
- _freeExpiredOwnersAtNow:.defaultOnce.171
- _freeExpiredOwnersAtNow:.defaultOnce.177
- _indexRule:.classDebugEnabled.52
- _indexRule:.classDebugEnabled.67
- _indexRule:.defaultOnce.51
- _indexRule:.defaultOnce.66
- _initWithNodeID:withRootNodeID:withParentEntryID:withNumAncestors:withEnergy:withRange:withEntryDate:.classDebugEnabled.21
- _initWithNodeID:withRootNodeID:withParentEntryID:withNumAncestors:withEnergy:withRange:withEntryDate:.defaultOnce.20
- _intersect:.classDebugEnabled.16
- _intersect:.classDebugEnabled.22
- _intersect:.classDebugEnabled.28
- _intersect:.defaultOnce.15
- _intersect:.defaultOnce.21
- _intersect:.defaultOnce.27
- _isValidPower:forRootNodeID:.classDebugEnabled.18
- _isValidPower:forRootNodeID:.classDebugEnabled.24
- _isValidPower:forRootNodeID:.defaultOnce.17
- _isValidPower:forRootNodeID:.defaultOnce.23
- _loadRules.classDebugEnabled.24
- _loadRules.classDebugEnabled.31
- _loadRules.classDebugEnabled.37
- _loadRules.classDebugEnabled.44
- _loadRules.classDebugEnabled.49
- _loadRules.defaultOnce.23
- _loadRules.defaultOnce.30
- _loadRules.defaultOnce.36
- _loadRules.defaultOnce.43
- _loadRules.defaultOnce.48
- _mergeWithEvent:.classDebugEnabled.48
- _mergeWithEvent:.defaultOnce.47
- _nodeIDForNodeName:isPermanent:.classDebugEnabled.17
- _nodeIDForNodeName:isPermanent:.classDebugEnabled.23
- _nodeIDForNodeName:isPermanent:.classDebugEnabled.32
- _nodeIDForNodeName:isPermanent:.defaultOnce.16
- _nodeIDForNodeName:isPermanent:.defaultOnce.22
- _nodeIDForNodeName:isPermanent:.defaultOnce.31
- _objc_msgSend$isBasebandClass:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
- _overlaps:.classDebugEnabled.34
- _overlaps:.classDebugEnabled.40
- _overlaps:.classDebugEnabled.46
- _overlaps:.defaultOnce.33
- _overlaps:.defaultOnce.39
- _overlaps:.defaultOnce.45
- _ownerIDsForDependency:.classDebugEnabled.117
- _ownerIDsForDependency:.classDebugEnabled.130
- _ownerIDsForDependency:.classDebugEnabled.134
- _ownerIDsForDependency:.defaultOnce.116
- _ownerIDsForDependency:.defaultOnce.129
- _ownerIDsForDependency:.defaultOnce.133
- _qualify.classDebugEnabled.18
- _qualify.classDebugEnabled.24
- _qualify.classDebugEnabled.30
- _qualify.classDebugEnabled.36
- _qualify.classDebugEnabled.43
- _qualify.classDebugEnabled.49
- _qualify.classDebugEnabled.55
- _qualify.classDebugEnabled.61
- _qualify.classDebugEnabled.67
- _qualify.classDebugEnabled.74
- _qualify.defaultOnce.17
- _qualify.defaultOnce.23
- _qualify.defaultOnce.29
- _qualify.defaultOnce.35
- _qualify.defaultOnce.42
- _qualify.defaultOnce.48
- _qualify.defaultOnce.54
- _qualify.defaultOnce.60
- _qualify.defaultOnce.66
- _qualify.defaultOnce.73
- _rangeSinceEvent:.classDebugEnabled.24
- _rangeSinceEvent:.classDebugEnabled.30
- _rangeSinceEvent:.classDebugEnabled.36
- _rangeSinceEvent:.classDebugEnabled.42
- _rangeSinceEvent:.defaultOnce.23
- _rangeSinceEvent:.defaultOnce.29
- _rangeSinceEvent:.defaultOnce.35
- _rangeSinceEvent:.defaultOnce.41
- _reloadDependenciesNewerThanDate:.classDebugEnabled.103
- _reloadDependenciesNewerThanDate:.classDebugEnabled.53
- _reloadDependenciesNewerThanDate:.classDebugEnabled.59
- _reloadDependenciesNewerThanDate:.classDebugEnabled.70
- _reloadDependenciesNewerThanDate:.classDebugEnabled.71
- _reloadDependenciesNewerThanDate:.classDebugEnabled.76
- _reloadDependenciesNewerThanDate:.classDebugEnabled.90
- _reloadDependenciesNewerThanDate:.classDebugEnabled.97
- _reloadDependenciesNewerThanDate:.defaultOnce.102
- _reloadDependenciesNewerThanDate:.defaultOnce.52
- _reloadDependenciesNewerThanDate:.defaultOnce.58
- _reloadDependenciesNewerThanDate:.defaultOnce.69
- _reloadDependenciesNewerThanDate:.defaultOnce.70
- _reloadDependenciesNewerThanDate:.defaultOnce.75
- _reloadDependenciesNewerThanDate:.defaultOnce.89
- _reloadDependenciesNewerThanDate:.defaultOnce.96
- _reloadLastDistributionEventsWithLastDeviceBootDate:.classDebugEnabled.647
- _reloadLastDistributionEventsWithLastDeviceBootDate:.classDebugEnabled.657
- _reloadLastDistributionEventsWithLastDeviceBootDate:.classDebugEnabled.663
- _reloadLastDistributionEventsWithLastDeviceBootDate:.defaultOnce.646
- _reloadLastDistributionEventsWithLastDeviceBootDate:.defaultOnce.656
- _reloadLastDistributionEventsWithLastDeviceBootDate:.defaultOnce.662
- _reloadLastPowerEventsWithLastDeviceBootDate:.classDebugEnabled.638
- _reloadLastPowerEventsWithLastDeviceBootDate:.classDebugEnabled.644
- _reloadLastPowerEventsWithLastDeviceBootDate:.defaultOnce.637
- _reloadLastPowerEventsWithLastDeviceBootDate:.defaultOnce.643
- _reloadLastQualificationEventsWithLastDeviceBootDate:.classDebugEnabled.666
- _reloadLastQualificationEventsWithLastDeviceBootDate:.classDebugEnabled.675
- _reloadLastQualificationEventsWithLastDeviceBootDate:.classDebugEnabled.681
- _reloadLastQualificationEventsWithLastDeviceBootDate:.defaultOnce.665
- _reloadLastQualificationEventsWithLastDeviceBootDate:.defaultOnce.674
- _reloadLastQualificationEventsWithLastDeviceBootDate:.defaultOnce.680
- _ruleWithString:withEntryDate:.classDebugEnabled.35
- _ruleWithString:withEntryDate:.classDebugEnabled.42
- _ruleWithString:withEntryDate:.classDebugEnabled.44
- _ruleWithString:withEntryDate:.classDebugEnabled.50
- _ruleWithString:withEntryDate:.classDebugEnabled.57
- _ruleWithString:withEntryDate:.defaultOnce.34
- _ruleWithString:withEntryDate:.defaultOnce.41
- _ruleWithString:withEntryDate:.defaultOnce.43
- _ruleWithString:withEntryDate:.defaultOnce.49
- _ruleWithString:withEntryDate:.defaultOnce.56
- _rulesFromFileWithForceLoad:.classDebugEnabled.101
- _rulesFromFileWithForceLoad:.classDebugEnabled.70
- _rulesFromFileWithForceLoad:.classDebugEnabled.77
- _rulesFromFileWithForceLoad:.classDebugEnabled.87
- _rulesFromFileWithForceLoad:.classDebugEnabled.95
- _rulesFromFileWithForceLoad:.defaultOnce.100
- _rulesFromFileWithForceLoad:.defaultOnce.69
- _rulesFromFileWithForceLoad:.defaultOnce.76
- _rulesFromFileWithForceLoad:.defaultOnce.86
- _rulesFromFileWithForceLoad:.defaultOnce.94
- _startObservingDependencyID:forOwner:.classDebugEnabled.139
- _startObservingDependencyID:forOwner:.defaultOnce.138
- _startObservingOwnerID:forDependency:.classDebugEnabled.151
- _startObservingOwnerID:forDependency:.defaultOnce.150
- _stopObservingDependencyID:forOwner:.classDebugEnabled.142
- _stopObservingDependencyID:forOwner:.defaultOnce.141
- _stopObservingOwnerID:forDependency:.classDebugEnabled.154
- _stopObservingOwnerID:forDependency:.defaultOnce.153
- _updateWithEndDate:.classDebugEnabled.58
- _updateWithEndDate:.classDebugEnabled.65
- _updateWithEndDate:.defaultOnce.57
- _updateWithEndDate:.defaultOnce.64
CStrings:
+ "#"
+ "-[PLAccountingOwnerDependencyManager lastAllRunDateForOwnerID:]"
+ "Recorded runDate=%@ for ownerID=%@"
+ "SpotlightDonation"
+ "[LASTALLRUN PLAccountingOwnerDependencyManager:%d] Recorded runDate for freed owner: owner_addr=%p, ID=%@, runDate=%{public}@"
+ "[LASTALLRUN: PLAccountingDependency:%d] observingOwnerIDs=%@"
+ "[LASTALLRUN: PLAccountingDependency:%d] owner has already run and surpassed the range of this dependency"
+ "[LASTALLRUN: PLAccountingDependency:%d] ownerID=%@, ownerRunDate=%@, self.range.endDate=%@"
+ "[LIFECYCLE PLAccountingCorrectionManager:%d] Correction owner CREATED: owner_addr=%p, rootEnergyEstimate_addr=%p, entryID=%lld, ID=%@, rootNodeID=%@, canCorrect=%d"
+ "[LIFECYCLE PLAccountingCorrectionOwner:%d] Correction COMPLETED: owner_addr=%p, rootEnergyEstimate_addr=%p, correctedCount=%d"
+ "[LIFECYCLE PLAccountingCorrectionOwner:%d] Correction STARTED: owner_addr=%p, rootEnergyEstimate_addr=%p, entryID=%lld, nodeID=%@, rootNodeID=%@, energy=%.4f mWh, range=%{public}@"
+ "[LIFECYCLE PLAccountingCorrectionOwner:%d] Correction owner DEALLOCATED: owner_addr=%p, rootEnergyEstimate_addr=%p, ID=%@"
+ "[LIFECYCLE PLAccountingEnergyEstimateEventEntry:%d] Energy estimate DEALLOCATED: addr=%p"
+ "[LIFECYCLE PLAccountingEngine:%d] Created root energy estimate for backward event: addr=%p, entryID=%lld, nodeID=%@, rootNodeID=%d, energy=%.4f mWh, range=%{public}@"
+ "[LIFECYCLE PLAccountingEngine:%d] Created root energy estimate for forward event: addr=%p, entryID=%lld, nodeID=%@, rootNodeID=%d, energy=%.4f mWh, range=%{public}@"
+ "[LIFECYCLE PLAccountingEngine:%d] Created root energy estimate for interval event: addr=%p, entryID=%lld, nodeID=%@, rootNodeID=%d, energy=%.4f mWh, range=%{public}@"
+ "[LIFECYCLE PLAccountingEngine:%d] Root energy estimate written to DB: addr=%p, entryID=%lld (was -1), nodeID=%@, rootNodeID=%@"
+ "[LIFECYCLE PLAccountingOwner:%d]     Unmet at deactivation: %@"
+ "[LIFECYCLE PLAccountingOwner:%d]     Unmet dependency: %@"
+ "[LIFECYCLE PLAccountingOwner:%d] Deactivating with %lu unmet dependencies: owner_addr=%p"
+ "[LIFECYCLE PLAccountingOwner:%d] Dependency MEETS range requirement: owner_addr=%p, dependencyID=%@, removing from observing set (remaining=%lu)"
+ "[LIFECYCLE PLAccountingOwner:%d] Dependency arrived: owner_addr=%p, owner=%@, dependency_addr=%p, dependencyID=%@, dependency_range=%{public}@"
+ "[LIFECYCLE PLAccountingOwner:%d] Forcing allRun() due to deactivation: owner_addr=%p"
+ "[LIFECYCLE PLAccountingOwner:%d] Owner DEACTIVATE called: owner_addr=%p, ID=%@, hasRun=%d, observingDependencies=%lu"
+ "[LIFECYCLE PLAccountingOwner:%d] Still waiting for %lu dependencies: owner_addr=%p"
+ "[LIFECYCLE PLAccountingOwner:%d] activate() -> allRun() because no dependencies to wait for: owner_addr=%p"
+ "[LIFECYCLE PLAccountingOwner:%d] allRun() called -> run() for correction: owner_addr=%p, ID=%@"
+ "[LIFECYCLE PLAccountingOwnerDependencyManager:%d] Deactivating oldest owner: owner_addr=%p, ID=%@, activationDate=%{public}@"
+ "[LIFECYCLE PLAccountingOwnerDependencyManager:%d] HIT MAX OWNERS: count=%lu, max=%d, forcing deactivation of oldest owner"
+ "[LIFECYCLE PLAccountingOwnerDependencyManager:%d] Owner ACTIVATED: owner_addr=%p, ID=%@, activationDate=%{public}@"
+ "[LIFECYCLE PLAccountingOwnerDependencyManager:%d] Owner ADDED to repository: owner_addr=%p, ID=%@, count=%lu, range=%{public}@"
+ "[LIFECYCLE PLAccountingOwnerDependencyManager:%d] Owner REMOVED from repository: owner_addr=%p, ID=%@, count=%lu"
+ "[POWEROUT_DEBUG PLAccountingCorrectionManager:%d] Registering root estimate as correction dependency: rootNodeID=%@, energy=%.6f mWh, dep_range=%{public}@ — other owners observing this nodeID will check if dep.range.endDate >= owner.range.endDate"
+ "[POWEROUT_DEBUG PLAccountingCorrectionManager:%d] Zero/sub-minEnergy root estimate IMMEDIATELY corrected (writeToDB=YES): entryID=%lld, rootNodeID=%@, energy=%.6f mWh, range=%{public}@ — correction unblocked without waiting for gas gauge"
+ "[POWEROUT_DEBUG PLAccountingEngine:%d] About to register backward energy estimate as dependency: rootNodeID=%d, energy=%.6f mWh, dependency_range=%{public}@ (other owners wait until a dep's endDate >= their own range endDate)"
+ "[POWEROUT_DEBUG PLAccountingEngine:%d] About to register interval energy estimate as dependency: rootNodeID=%d, energy=%.6f mWh, dependency_range=%{public}@ (interval uses event's own range, not sinceRange)"
+ "[POWEROUT_DEBUG PLAccountingEngine:%d] Backward action block: NO lastEvent for rootNodeID=%d, skipping energy estimate creation (first event after boot/clear?)"
+ "[POWEROUT_DEBUG PLAccountingEngine:%d] Backward action block: rootNodeID=%d, power=%.4f, sinceRange=%{public}@, energy=%.6f mWh"
+ "[POWEROUT_DEBUG PLAccountingOwner:%d] activate(): owner(ID=%@, range_endDate=%{public}@) still waiting for depID=%@ — lastDep_range_endDate=%{public}@ (nil means no dep arrived yet)"
+ "accounting_merging"
+ "ownerID=%@"
+ "runDate=%@ for ownerID=%@"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PLAccountingCorrectionManagerDelegate>\""
- "@\"<PLAccountingDependencyManager>\""
- "@\"<PLAccountingDependencyOwner>\"24@0:8@\"NSNumber\"16"
- "@\"<PLAccountingDistributionManagerDelegate>\""
- "@\"<PLAccountingOwnerManager>\""
- "@\"<PLAccountingQualificationManagerDelegate>\""
- "@\"NSArray\"20@0:8i16"
- "@\"NSArray\"32@0:8@\"NSNumber\"16@\"PLAccountingRange\"24"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSMutableSet\"24@0:8@\"PLAccountingDependency\"16"
- "@\"NSMutableSet\"24@0:8@\"PLAccountingOwner\"16"
- "@\"NSNumber\""
- "@\"NSNumber\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_queue>\"16@0:8"
- "@\"NSRegularExpression\""
- "@\"NSSet\""
- "@\"NSString\"16@0:8"
- "@\"PLAccountingCorrectionManager\""
- "@\"PLAccountingDependency\"24@0:8@\"NSNumber\"16"
- "@\"PLAccountingDistributionEventEntry\""
- "@\"PLAccountingDistributionManager\""
- "@\"PLAccountingEnergyEstimateEventEntry\""
- "@\"PLAccountingEnergyEventEntry\""
- "@\"PLAccountingQualificationEventEntry\""
- "@\"PLAccountingQualificationManager\""
- "@\"PLAccountingRange\""
- "@\"PLAccountingRange\"16@0:8"
- "@\"PLActivity\""
- "@\"PLEntryNotificationOperatorComposition\""
- "@\"PLTimer\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16d24@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16d24@32@40"
- "@64@0:8@16@24i32i36d40@48@56"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8d16@24"
- "NSObject"
- "PLAccountingCorrectionDependency"
- "PLAccountingCorrectionManager"
- "PLAccountingCorrectionManagerDelegate"
- "PLAccountingCorrectionOwner"
- "PLAccountingCorrectionOwnerManager"
- "PLAccountingDependency"
- "PLAccountingDependencyManager"
- "PLAccountingDependencyOwner"
- "PLAccountingDistributionDependency"
- "PLAccountingDistributionEventBackwardEntry"
- "PLAccountingDistributionEventEntry"
- "PLAccountingDistributionEventForwardEntry"
- "PLAccountingDistributionEventIntervalEntry"
- "PLAccountingDistributionEventPointEntry"
- "PLAccountingDistributionManager"
- "PLAccountingDistributionManagerDelegate"
- "PLAccountingDistributionOwner"
- "PLAccountingDistributionOwnerManager"
- "PLAccountingDistributionRuleEntry"
- "PLAccountingDistributionRuleManager"
- "PLAccountingEnergyEstimateEventEntry"
- "PLAccountingEnergyEventEntry"
- "PLAccountingEngine"
- "PLAccountingEventEntry"
- "PLAccountingNodeEntry"
- "PLAccountingNodeManager"
- "PLAccountingOwner"
- "PLAccountingOwnerDependencyManager"
- "PLAccountingOwnerManager"
- "PLAccountingPowerEventBackwardEntry"
- "PLAccountingPowerEventEntry"
- "PLAccountingPowerEventForwardEntry"
- "PLAccountingPowerEventIntervalEntry"
- "PLAccountingQualificationDependency"
- "PLAccountingQualificationEventBackwardEntry"
- "PLAccountingQualificationEventEntry"
- "PLAccountingQualificationEventForwardEntry"
- "PLAccountingQualificationEventIntervalEntry"
- "PLAccountingQualificationEventPointEntry"
- "PLAccountingQualificationManager"
- "PLAccountingQualificationManagerDelegate"
- "PLAccountingQualificationOwner"
- "PLAccountingQualificationRuleEntry"
- "PLAccountingQualificationRuleManager"
- "PLAccountingRange"
- "PLAccountingRuleEntry"
- "PLAccountingRuleManager"
- "Q16@0:8"
- "T#,R"
- "T@\"<PLAccountingCorrectionManagerDelegate>\",W,V_delegate"
- "T@\"<PLAccountingCorrectionOwnerManager>\",W,D"
- "T@\"<PLAccountingDependencyManager>\",W,V_manager"
- "T@\"<PLAccountingDistributionManagerDelegate>\",W,V_delegate"
- "T@\"<PLAccountingDistributionOwnerManager>\",W,D"
- "T@\"<PLAccountingOwnerManager>\",W,V_manager"
- "T@\"<PLAccountingQualificationManagerDelegate>\",W,V_delegate"
- "T@\"<PLAccountingQualificationOwnerManager>\",W,D"
- "T@\"NSDate\",&,N"
- "T@\"NSDate\",&,N,V_activationDate"
- "T@\"NSDate\",&,N,V_runDate"
- "T@\"NSDate\",&,V_lastQualifiedEnergyEventDate"
- "T@\"NSDate\",R,N,V_endDate"
- "T@\"NSDate\",R,N,V_startDate"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_childNodeIDToWeight"
- "T@\"NSMutableDictionary\",&,N,V_dependencyIDToDependenciesInRange"
- "T@\"NSMutableDictionary\",&,N,V_distributionIDToDistributionRules"
- "T@\"NSMutableDictionary\",&,N,V_parentEntryIDToChildEnergyEstimates"
- "T@\"NSMutableDictionary\",&,N,V_qualificationIDToQualificationRules"
- "T@\"NSMutableDictionary\",&,N,V_rootNodeIDToNodeIDToDistributionRule"
- "T@\"NSMutableDictionary\",&,N,V_rootNodeIDToQualificationRules"
- "T@\"NSMutableDictionary\",&,N,V_ruleIDToRule"
- "T@\"NSMutableDictionary\",&,V_dependencyIDToDependencies"
- "T@\"NSMutableDictionary\",&,V_dependencyIDToObservingOwners"
- "T@\"NSMutableDictionary\",&,V_nodeIDToNodeName"
- "T@\"NSMutableDictionary\",&,V_nodeNameToNodeID"
- "T@\"NSMutableDictionary\",&,V_ownerIDToLastOwner"
- "T@\"NSMutableDictionary\",&,V_ownerIDToObservingDependencies"
- "T@\"NSMutableSet\",&,N,V_observingDependencyIDs"
- "T@\"NSMutableSet\",&,N,V_observingOwnerIDs"
- "T@\"NSMutableSet\",&,V_ownersRepository"
- "T@\"NSNumber\",&,N"
- "T@\"NSNumber\",&,N,V_ID"
- "T@\"NSNumber\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_workQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_workQueue"
- "T@\"NSRegularExpression\",&,N,V_regex"
- "T@\"NSSet\",R,N"
- "T@\"NSSet\",R,N,V_childNodeIDs"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"PLAccountingCorrectionManager\",&,N,V_correctionManager"
- "T@\"PLAccountingDistributionEventEntry\",&,V_distributionEvent"
- "T@\"PLAccountingDistributionManager\",&,N,V_distributionManager"
- "T@\"PLAccountingEnergyEstimateEventEntry\",&,V_energyEstimate"
- "T@\"PLAccountingEnergyEstimateEventEntry\",&,V_rootEnergyEstimate"
- "T@\"PLAccountingEnergyEventEntry\",&,V_energyEvent"
- "T@\"PLAccountingQualificationEventEntry\",&,V_qualificationEvent"
- "T@\"PLAccountingQualificationManager\",&,N,V_qualificationManager"
- "T@\"PLAccountingRange\",&,N"
- "T@\"PLAccountingRange\",&,N,V_range"
- "T@\"PLAccountingRange\",R,N,V_range"
- "T@\"PLActivity\",&,V_chunkActivity"
- "T@\"PLEntryNotificationOperatorComposition\",&,V_batteryListener"
- "T@\"PLTimer\",&,V_freeTimer"
- "TB,N,V_used"
- "TB,R,N"
- "TB,V__distributeRangeWeightedTotal"
- "TB,V_isRootNodeEnergyAggregated"
- "TB,V_pluggedIn"
- "TQ,R"
- "Td,N"
- "Td,R,N"
- "Ti,R,N"
- "Ti,V_numDependencies"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_ID"
- "__distributeRangeWeightedTotal"
- "_activationDate"
- "_batteryListener"
- "_childNodeIDToWeight"
- "_childNodeIDs"
- "_chunkActivity"
- "_correctionManager"
- "_delegate"
- "_dependencyIDToDependencies"
- "_dependencyIDToDependenciesInRange"
- "_dependencyIDToObservingOwners"
- "_distributeRangeWeightedTotal"
- "_distributionEvent"
- "_distributionIDToDistributionRules"
- "_distributionManager"
- "_endDate"
- "_energyEstimate"
- "_energyEvent"
- "_freeTimer"
- "_isRootNodeEnergyAggregated"
- "_lastDependencyForDependencyID:"
- "_lastQualifiedEnergyEventDate"
- "_manager"
- "_nodeIDToNodeName"
- "_nodeMappingLock"
- "_nodeNameToNodeID"
- "_numDependencies"
- "_observingDependencyIDs"
- "_observingOwnerIDs"
- "_ownerIDToLastOwner"
- "_ownerIDToObservingDependencies"
- "_ownersRepository"
- "_parentEntryIDToChildEnergyEstimates"
- "_pluggedIn"
- "_qualificationEvent"
- "_qualificationIDToQualificationRules"
- "_qualificationManager"
- "_range"
- "_regex"
- "_rootEnergyEstimate"
- "_rootNodeIDToNodeIDToDistributionRule"
- "_rootNodeIDToQualificationRules"
- "_ruleIDToRule"
- "_runDate"
- "_startDate"
- "_used"
- "_workQueue"
- "accountingDebugEnabled"
- "activate"
- "activationDate"
- "addDependency:"
- "addDistributionEvent:"
- "addDistributionEventInterval:"
- "addDistributionEventIntervalWithLastDistributionEventBackward:withDistributionEventBackward:"
- "addDistributionEventIntervalWithLastDistributionEventForward:withDistributionEventForward:"
- "addDistributionEventPoint:"
- "addEnergyEstimate:withNow:"
- "addEnergyMeasurement:"
- "addEnergyMeasurementWithRootNodeID:withEnergy:withRange:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addOwner:"
- "addPowerMeasurementEventIntervalWithPower:withStartDate:withEndDate:"
- "addQualificationEvent:"
- "addQualificationEventInterval:"
- "addQualificationEventIntervalWithLastQualificationEventBackward:withQualificationEventBackward:"
- "addQualificationEventIntervalWithLastQualificationEventForward:withQualificationEventForward:"
- "addQualificationEventPoint:"
- "addRootEnergyEstimate:withNow:"
- "allBBRootNodeIDs"
- "allDistributionIDs"
- "allKeys"
- "allObjects"
- "allQualificationIDs"
- "allRun"
- "allSoCRootNodeIDs"
- "allValues"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "batteryListener"
- "blockingFlushCachesWithReason:"
- "blockingUpdateEntry:withBlock:"
- "blockingWriteEntry:withCompletionBlock:"
- "boolForKey:ifNotSet:"
- "boolValue"
- "bundleForClass:"
- "bytes"
- "canFreeDependency:"
- "canFreeOwner:"
- "canMergeWithEvent:"
- "childEnergyEstimatesForParentEntryID:"
- "childNodeIDToWeight"
- "childNodeIDs"
- "childNodeIDsFromChildNodeNames:"
- "childNodeNameToWeight"
- "childNodeNames"
- "chunkActivity"
- "chunkWithLastChunkDate:withNow:"
- "class"
- "classDirectionality"
- "clearLastEntryCacheForEntryKey:"
- "clearWithEntryKey:"
- "closeLastDistributionEventForwardWithDistributionID:withEndDate:"
- "closeLastQualificationEventForwardWithQualificationID:withEndDate:"
- "combined for equal contents, now lastEvent=%@"
- "combined for too short sinceRange, now lastEvent=%@"
- "componentsSeparatedByCharactersInSet:"
- "conformsToProtocol:"
- "connection"
- "containsDate:"
- "containsObject:"
- "containsString:"
- "copy"
- "correctChildEnergyEstimate:withParentEnergyEstimate:withNow:"
- "correctionDate"
- "correctionEnergy"
- "correctionManager"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAggregateRootNodeEnergyEntryWithEnergyEstimate:"
- "createDistributionEventBackwardWithDistributionID:withChildNodeNameToWeight:withEndDate:"
- "createDistributionEventForwardWithDistributionID:withAddingChildNodeName:withStartDate:"
- "createDistributionEventForwardWithDistributionID:withChildNodeNameToWeight:withStartDate:"
- "createDistributionEventForwardWithDistributionID:withRemovingChildNodeName:withStartDate:"
- "createDistributionEventIntervalWithDistributionID:withChildNodeNameToWeight:withStartDate:withEndDate:"
- "createDistributionEventPointWithDistributionID:withChildNodeNameToWeight:withStartDate:"
- "createEventWithEvent:withActionBlock:"
- "createPowerEventBackwardWithRootNodeID:withPower:withEndDate:"
- "createPowerEventForwardWithRootNodeID:withPower:withStartDate:"
- "createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:"
- "createQualificationEventBackwardWithQualificationID:withChildNodeNames:withEndDate:"
- "createQualificationEventForwardWithQualificationID:withAddingChildNodeName:withStartDate:"
- "createQualificationEventForwardWithQualificationID:withChildNodeNames:withStartDate:"
- "createQualificationEventForwardWithQualificationID:withRemovingChildNodeName:withStartDate:"
- "createQualificationEventIntervalWithQualificationID:withChildNodeNames:withStartDate:withEndDate:"
- "createQualificationEventPointWithQualificationID:withChildNodeNames:withStartDate:"
- "currentDistributionEventForwardWithDistributionID:"
- "d16@0:8"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceNow:"
- "deactivate"
- "debugDescription"
- "debugEnabled"
- "debugInstance"
- "decryptData:withKey:"
- "defaultCenter"
- "delegate"
- "deleteEntry:"
- "dependenciesWithDependencyID:withRange:"
- "dependencyIDToDependencies"
- "dependencyIDToDependenciesInRange"
- "dependencyIDToObservingOwners"
- "dependencyIDsForOwner:"
- "description"
- "deviceBBRootNodeIDs"
- "deviceBootTime"
- "deviceRootNodeIDs"
- "deviceSoCRootNodeIDs"
- "dictionary"
- "dictionaryWithObjects:forKeys:"
- "dictionaryWithObjects:forKeys:count:"
- "didCorrectEnergyEstimate:"
- "didCreateChildEnergyEstimate:withParentEnergyEstimate:"
- "didDistributeEnergyEstimate:"
- "didDistributeToChildEnergyEstimate:fromParentEnergyEstimate:"
- "didQualifyEnergyEvent:withRootNodeID:withQualificationID:"
- "didReceiveDependency:"
- "didReceiveOwner:"
- "disableCorrection"
- "distantFuture"
- "distantPast"
- "distributeRangeWeightedTotal"
- "distributionDate"
- "distributionEvent"
- "distributionID"
- "distributionIDForDistributionName:"
- "distributionIDToDistributionRules"
- "distributionManager"
- "distributionRuleForRootNodeID:andNodeID:"
- "distributionRuleID"
- "distributionRulesForDistributionID:"
- "doubleForKey:ifNotSet:"
- "doubleValue"
- "earlierDate:"
- "emptyRange"
- "endDate"
- "energy"
- "energyEstimate"
- "energyEvent"
- "entriesForKey:"
- "entriesForKey:withComparisons:"
- "entriesForKey:withQuery:"
- "entryDate"
- "entryID"
- "entryKey"
- "entryKeyForType:andName:"
- "enumerateObjectsUsingBlock:"
- "existsInDB"
- "firstLineWithFile:"
- "firstMatchInString:options:range:"
- "firstObject"
- "flushCachesWithReason:"
- "freeExpiredDependenciesAtNow:"
- "freeExpiredOwnersAtNow:"
- "freeTimer"
- "freeTimerInterval"
- "gasGaugeEnabled"
- "gasGaugeEntryKey"
- "getCString:maxLength:encoding:"
- "getLastQualifiedEnergyEventDate"
- "hasAOD"
- "hasCapability:"
- "hasDynamicKeysForEntryKey:"
- "hasRun"
- "hash"
- "i16@0:8"
- "indexRule:"
- "init"
- "initEntryWithRawData:"
- "initWithDistributionEvent:"
- "initWithDistributionID:withChildNodeIDToWeight:withRange:"
- "initWithDistributionID:withChildNodeIDToWeight:withStartDate:withEndDate:"
- "initWithDistributionID:withChildNodeNameToWeight:withEndDate:"
- "initWithDistributionID:withChildNodeNameToWeight:withRange:"
- "initWithDistributionID:withChildNodeNameToWeight:withStartDate:"
- "initWithDistributionID:withChildNodeNameToWeight:withStartDate:withEndDate:"
- "initWithEnergyEstimate:"
- "initWithEnergyEvent:"
- "initWithEntryKey:"
- "initWithEntryKey:withDate:"
- "initWithEntryKey:withRawData:"
- "initWithFireDate:withInterval:withTolerance:repeats:withUserInfo:withQueue:withBlock:"
- "initWithKey:withValue:withComparisonOperation:"
- "initWithName:"
- "initWithNodeID:withEnergy:withRange:withEntryDate:"
- "initWithNodeID:withRootNodeID:withDistributionID:withEntryDate:"
- "initWithNodeID:withRootNodeID:withParentEntryID:withNumAncestors:withEnergy:withRange:withEntryDate:"
- "initWithQualificationEvent:"
- "initWithQualificationID:withChildNodeIDs:withRange:"
- "initWithQualificationID:withChildNodeIDs:withStartDate:withEndDate:"
- "initWithQualificationID:withChildNodeNames:withEndDate:"
- "initWithQualificationID:withChildNodeNames:withRange:"
- "initWithQualificationID:withChildNodeNames:withStartDate:"
- "initWithQualificationID:withChildNodeNames:withStartDate:withEndDate:"
- "initWithRange:"
- "initWithRootEnergyEstimate:"
- "initWithRootNodeID:"
- "initWithRootNodeID:withPower:withEndDate:"
- "initWithRootNodeID:withPower:withRange:"
- "initWithRootNodeID:withPower:withStartDate:"
- "initWithRootNodeID:withPower:withStartDate:withEndDate:"
- "initWithRootNodeID:withQualificationID:withEntryDate:"
- "initWithStartDate:withEndDate:"
- "initWithWorkQueue:forEntryKey:withBlock:"
- "instanceDirectionality"
- "intValue"
- "intersect:"
- "intersectSet:"
- "isBasebandClass:"
- "isClassDebugEnabled:"
- "isClassDebugEnabled:forKey:"
- "isEmptyEvent"
- "isEqual:"
- "isEqualContentsWithEvent:"
- "isEqualToDate:"
- "isEqualToDictionary:"
- "isEqualToNumber:"
- "isEqualToSet:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPerfPowerMetricd"
- "isPowerlogHelperd"
- "isProxy"
- "isRootNodeEnergyAggregated"
- "isValidPower:forRootNodeID:"
- "isiPhone"
- "kPLBasebandClassIsOneOf:"
- "kPLDeviceClassName"
- "kPLSoCClassOfDevice"
- "keyConfigsForEntryKey:"
- "keys"
- "keysOfEntriesPassingTest:"
- "lastCompletedDateWithIdentifier:"
- "lastDependencyForDependencyID:"
- "lastEntryCachePruneToDate:"
- "lastEntryForKey:withComparisons:isSingleton:"
- "lastEntryForKey:withSubEntryKey:"
- "lastObject"
- "lastOwnerForOwnerID:"
- "lastPathComponent"
- "lastQualifiedEnergyEventDate"
- "laterDate:"
- "launchDate"
- "length"
- "load"
- "loadDynamicKeys"
- "loadRules"
- "logMessage:fromFile:fromFunction:fromLineNumber:"
- "logged new event=%@"
- "longLongValue"
- "manager"
- "maxDependencies"
- "maxOwners"
- "maxPowerEventChunkInterval"
- "mergeWithEvent:"
- "mergingDenyList"
- "minDistributionEnergy"
- "minEnergy"
- "minPowerDifference"
- "minPowerPercentageDifference"
- "minusSet:"
- "monotonicDate"
- "mutableCopy"
- "name"
- "newlineCharacterSet"
- "nodeID"
- "nodeIDForNodeName:isPermanent:"
- "nodeIDToNodeName"
- "nodeNameForNodeID:"
- "nodeNameToNodeID"
- "normalizeWeights:"
- "notifyDependenciesWithOwner:"
- "notifyOwnersWithDependency:"
- "numAncestors"
- "numDependencies"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithLong:"
- "numberWithLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observingDependencyIDs"
- "observingOwnerIDs"
- "overlaps:"
- "ownerIDToLastOwner"
- "ownerIDToObservingDependencies"
- "ownerIDsForDependency:"
- "ownersRepository"
- "parentEntryID"
- "parentEntryIDToChildEnergyEstimates"
- "pathExtension"
- "pathForResource:ofType:"
- "performQuery:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluggedIn"
- "power"
- "qualificationDate"
- "qualificationEvent"
- "qualificationID"
- "qualificationIDForQualificationName:"
- "qualificationIDToQualificationRules"
- "qualificationManager"
- "qualificationRuleIDSum"
- "qualificationRulesForQualificationID:"
- "qualificationRulesForRootNodeID:"
- "range"
- "rangeAtIndex:"
- "rangeOfString:"
- "rangeSinceEvent:"
- "rangeWithStartDate:withEndDate:"
- "regex"
- "regularExpressionWithPattern:options:error:"
- "release"
- "reload"
- "reloadDependenciesNewerThanDate:"
- "reloadLastDistributionEventsWithLastDeviceBootDate:"
- "reloadLastPowerEventsWithLastDeviceBootDate:"
- "reloadLastQualificationEventsWithLastDeviceBootDate:"
- "removeNodeReferenceFromCache:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "reset"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rootEnergyEstimate"
- "rootNodeID"
- "rootNodeIDToNodeIDToDistributionRule"
- "rootNodeIDToQualificationRules"
- "ruleForRuleID:"
- "ruleIDToRule"
- "ruleWithString:withEntryDate:"
- "ruleWithString:withRegex:withEntryDate:"
- "rulesEntryKey"
- "rulesFromFileWithForceLoad:"
- "rulesPath"
- "run"
- "runDate"
- "scheduleActivityWithIdentifier:withCriteria:withMustRunCriterion:withQueue:withInterruptBlock:withActivityBlock:"
- "self"
- "set"
- "setActivationDate:"
- "setBatteryListener:"
- "setChunkActivity:"
- "setCorrectionDate:"
- "setCorrectionEnergy:"
- "setCorrectionManager:"
- "setDelegate:"
- "setDependencyIDToDependencies:"
- "setDependencyIDToDependenciesInRange:"
- "setDependencyIDToObservingOwners:"
- "setDistributionDate:"
- "setDistributionEvent:"
- "setDistributionIDToDistributionRules:"
- "setDistributionManager:"
- "setEnergyEstimate:"
- "setEnergyEvent:"
- "setEntryID:"
- "setFreeTimer:"
- "setID:"
- "setIsRootNodeEnergyAggregated:"
- "setLastQualifiedEnergyEventDate:"
- "setManager:"
- "setNodeIDToNodeName:"
- "setNodeNameToNodeID:"
- "setNumDependencies:"
- "setObject:forKey:saveToDisk:"
- "setObject:forKeyedSubscript:"
- "setObservingDependencyIDs:"
- "setObservingOwnerIDs:"
- "setOwnerIDToLastOwner:"
- "setOwnerIDToObservingDependencies:"
- "setOwnersRepository:"
- "setParentEntryIDToChildEnergyEstimates:"
- "setPluggedIn:"
- "setQualificationDate:"
- "setQualificationEvent:"
- "setQualificationIDToQualificationRules:"
- "setQualificationManager:"
- "setRange:"
- "setRegex:"
- "setRootEnergyEstimate:"
- "setRootNodeIDToNodeIDToDistributionRule:"
- "setRootNodeIDToQualificationRules:"
- "setRuleIDToRule:"
- "setRunDate:"
- "setTerminationRatio:"
- "setUsed:"
- "setWithArray:"
- "setWithObject:"
- "setWorkQueue:"
- "setWriteToDB:"
- "set_distributeRangeWeightedTotal:"
- "setupNodes"
- "sharedCore"
- "sharedInstance"
- "sharedStorageCache"
- "startDate"
- "startObservingDependencyID:forOwner:"
- "startObservingOwnerID:forDependency:"
- "stopObservingDependencyID:forOwner:"
- "stopObservingOwnerID:forDependency:"
- "storage"
- "storageLocked"
- "storedHashDefaults"
- "stringByDeletingPathExtension"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subEntryKey"
- "subarrayWithRange:"
- "subdataWithRange:"
- "substringFromIndex:"
- "substringWithRange:"
- "superclass"
- "terminationRatio"
- "timeCriterionWithInterval:"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "updateLastDependencyID:withEndDate:"
- "updateWithEndDate:"
- "used"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@\"PLAccountingDependency\"16"
- "v24@0:8@\"PLAccountingDistributionEventIntervalEntry\"16"
- "v24@0:8@\"PLAccountingDistributionEventPointEntry\"16"
- "v24@0:8@\"PLAccountingEnergyEstimateEventEntry\"16"
- "v24@0:8@\"PLAccountingOwner\"16"
- "v24@0:8@\"PLAccountingQualificationEventIntervalEntry\"16"
- "v24@0:8@\"PLAccountingQualificationEventPointEntry\"16"
- "v24@0:8@\"PLAccountingRange\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v32@0:8@\"NSNumber\"16@\"PLAccountingDependency\"24"
- "v32@0:8@\"NSNumber\"16@\"PLAccountingOwner\"24"
- "v32@0:8@\"PLAccountingDistributionEventBackwardEntry\"16@\"PLAccountingDistributionEventBackwardEntry\"24"
- "v32@0:8@\"PLAccountingDistributionEventForwardEntry\"16@\"PLAccountingDistributionEventForwardEntry\"24"
- "v32@0:8@\"PLAccountingEnergyEstimateEventEntry\"16@\"PLAccountingEnergyEstimateEventEntry\"24"
- "v32@0:8@\"PLAccountingQualificationEventBackwardEntry\"16@\"PLAccountingQualificationEventBackwardEntry\"24"
- "v32@0:8@\"PLAccountingQualificationEventForwardEntry\"16@\"PLAccountingQualificationEventForwardEntry\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8i16@20@28"
- "v36@0:8i16d20@28"
- "v40@0:8@\"PLAccountingEnergyEventEntry\"16@\"NSNumber\"24@\"NSNumber\"32"
- "v40@0:8@16@24@32"
- "v40@0:8d16@\"NSDate\"24@\"NSDate\"32"
- "v40@0:8d16@24@32"
- "v44@0:8i16@20@28@36"
- "v44@0:8i16d20@28@36"
- "workQueue"
- "workQueueForClass:"
- "writeProportionateAggregateEntry:withStartDate:withEndDate:"
- "writeToDB"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
