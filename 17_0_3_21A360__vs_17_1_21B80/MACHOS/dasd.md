## dasd

> `/usr/libexec/dasd`

```diff

-1439.0.4.0.2
-  __TEXT.__text: 0xc212c
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_stubs: 0x11320
-  __TEXT.__objc_methlist: 0xb8d4
-  __TEXT.__const: 0x740
-  __TEXT.__objc_methname: 0x1d1a1
-  __TEXT.__cstring: 0x9cf6
-  __TEXT.__oslogstring: 0xaf26
-  __TEXT.__objc_classname: 0x121f
-  __TEXT.__objc_methtype: 0x2492
-  __TEXT.__gcc_except_tab: 0x2394
+1439.40.24.0.0
+  __TEXT.__text: 0xc35b4
+  __TEXT.__auth_stubs: 0x12b0
+  __TEXT.__objc_stubs: 0x11460
+  __TEXT.__objc_methlist: 0xbb34
+  __TEXT.__const: 0x768
+  __TEXT.__objc_methname: 0x1d6df
+  __TEXT.__cstring: 0x9f0d
+  __TEXT.__oslogstring: 0xb054
+  __TEXT.__objc_classname: 0x1243
+  __TEXT.__objc_methtype: 0x24d3
+  __TEXT.__gcc_except_tab: 0x2324
   __TEXT.__dlopen_cstrs: 0x34c
-  __TEXT.__unwind_info: 0x2a0c
-  __DATA_CONST.__auth_got: 0x958
+  __TEXT.__unwind_info: 0x2a4c
+  __DATA_CONST.__auth_got: 0x968
   __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2b18
-  __DATA_CONST.__cfstring: 0xa380
-  __DATA_CONST.__objc_classlist: 0x490
+  __DATA_CONST.__const: 0x2b60
+  __DATA_CONST.__cfstring: 0xa5a0
+  __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x1c8
   __DATA_CONST.__objc_arrayobj: 0xc0
-  __DATA_CONST.__objc_intobj: 0x930
+  __DATA_CONST.__objc_intobj: 0x990
   __DATA_CONST.__objc_dictobj: 0xc8
-  __DATA.__objc_const: 0x25668
-  __DATA.__objc_selrefs: 0x6540
+  __DATA.__objc_const: 0x26240
+  __DATA.__objc_selrefs: 0x6630
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x878
-  __DATA.__objc_superrefs: 0x3c0
-  __DATA.__objc_ivar: 0xec8
-  __DATA.__objc_data: 0x2da0
-  __DATA.__data: 0x10d0
-  __DATA.__bss: 0x950
+  __DATA.__objc_classrefs: 0x880
+  __DATA.__objc_superrefs: 0x3c8
+  __DATA.__objc_ivar: 0xf04
+  __DATA.__objc_data: 0x2df0
+  __DATA.__data: 0x10f0
+  __DATA.__bss: 0x960
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: F7AFA853-4761-3413-BABA-3E9155479FD4
-  Functions: 4859
-  Symbols:   603
-  CStrings:  9287
+  UUID: 9CE91EB5-C747-3887-A797-0F6085217525
+  Functions: 4908
+  Symbols:   605
+  CStrings:  9386
 
Symbols:
+ _clock_gettime_nsec_np
+ _objc_retain_x6
CStrings:
+ "$\x13"
+ "%@ encountered an error while running, adding to errored activities"
+ "%@ has state %@"
+ "1\x1a\x1f\x0f\a\x12/\x03"
+ "@\"NSIndexSet\""
+ "@40@0:8@16Q24Q32"
+ "@56@0:8@16@24@32@40@48"
+ "Allocating %.0f budget on start for %@"
+ "Average views %@"
+ "Budget_MinimumBatteryForUsageInitialAllotment"
+ "Budget_MinimumBatteryLevelForFullUsageInitialAllotment"
+ "Budget_MinimumUsageAllotmentSlotLookaheadDuration"
+ "Budget_UsageModulationMaximumInitialAllotmentPercentage"
+ "Config: Initial Allotment: %.2f, Minimum Level: %.0f, Minimum Full Level: %.0f, Minimum Lookahead: %.0f"
+ "Denying tasks due to network alignment."
+ "Entering alignment window"
+ "Exiting alignment window"
+ "Failed to resolve process name for PID %d for activity %{public}@"
+ "Found at index=%llu"
+ "Last wake date: %@"
+ "NW Evaluation: %@"
+ "Network Alignment"
+ "Network Synchronization Policy"
+ "No PID for activity %{public}@"
+ "No longer denying tasks due to network alignment."
+ "Q24@0:8q16"
+ "System"
+ "T@\"NSIndexSet\",&,N,V_affectedSeconds"
+ "T@\"NSSet\",&,N,V_spikeMinutes"
+ "T@\"_DASBatchingQueue\",&,N,V_networkActivitiesQueue"
+ "TB,N,V_inPossibleSynchronizationWindow"
+ "TQ,N,V_secondsAfterSpike"
+ "TQ,N,V_secondsBeforeSpike"
+ "Td,N,V_lastUserInactivity"
+ "Ti,N,V_randomizationInterval"
+ "Ti,N,V_recentActivityInterval"
+ "Ti,N,V_recentWakeInterval"
+ "WalltimeAtStart"
+ "WalltimeAtSuspension"
+ "Widgets"
+ "_DASNetworkSynchronizationPolicy"
+ "_affectedSeconds"
+ "_inPossibleSynchronizationWindow"
+ "_lastUserInactivity"
+ "_networkActivitiesQueue"
+ "_randomizationInterval"
+ "_recentActivityInterval"
+ "_recentWakeInterval"
+ "_secondsAfterSpike"
+ "_secondsBeforeSpike"
+ "_spikeMinutes"
+ "affectedSeconds"
+ "backupTaskStatusForCompletedActivity:"
+ "budgetModulation%@"
+ "com.apple.das.networkActivitiesQueue"
+ "firstIndex"
+ "handleTimerFireAtDate:withContext:"
+ "inPossibleSynchronizationWindow"
+ "indexGreaterThanOrEqualToIndex:"
+ "initForBudgetTypes:withBudgets:persistence:withQueue:withStore:"
+ "isBackupStatusCompleted:"
+ "kern.waketime"
+ "lastUserActivity"
+ "lastUserInactivity"
+ "lastWakeDate"
+ "locked_instantiateBudgetsInto:withRemovals:"
+ "locked_updateBudgetsToBeModulatedAdditions:removals:"
+ "modulatorForBudgetTypes:withBudgets:persistence:withQueue:withStore:"
+ "networkActivitiesQueue"
+ "network_synchronization_policy"
+ "policy"
+ "postNWAlignmentNotifications"
+ "postNotificationInWindow:"
+ "randomizationInterval"
+ "recentActivityInterval"
+ "recentWakeInterval"
+ "second"
+ "secondsAfterSpike"
+ "secondsBeforeSpike"
+ "secondsFromSpikeMinutes:secondsBeforeSpike:secondsAfterSpike:"
+ "setAffectedSeconds:"
+ "setInPossibleSynchronizationWindow:"
+ "setLastUserInactivity:"
+ "setNetworkActivitiesQueue:"
+ "setRandomizationInterval:"
+ "setRecentActivityInterval:"
+ "setRecentWakeInterval:"
+ "setSecondsAfterSpike:"
+ "setSecondsBeforeSpike:"
+ "setSpikeMinutes:"
+ "spikeMinutes"
+ "updateTrialParametersWithManager:"
- "%@: Found owner %@:%d for activity %@"
- "1\x1a\x1f\x0f\x06\x12/\x03"
- "Failed to resolve process name for PID %d"
- "Query for widget views %@ successful"
- "budgetModulation"
- "clock_gettime failed with: %d"
- "initWithBudgets:persistence:withQueue:withStore:"
- "locked_instantiateBudgetsInto:"
- "modulatorWithBudgets:persistence:withQueue:withStore:"
- "setPolicyScores:"

```
