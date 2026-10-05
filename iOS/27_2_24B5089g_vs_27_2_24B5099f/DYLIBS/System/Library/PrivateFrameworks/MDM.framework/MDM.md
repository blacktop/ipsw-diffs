## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-113.40.17.0.0
-  __TEXT.__text: 0x548e4
-  __TEXT.__objc_methlist: 0x43d4
-  __TEXT.__const: 0x1c2
-  __TEXT.__gcc_except_tab: 0xf34
-  __TEXT.__cstring: 0x5439
-  __TEXT.__oslogstring: 0x727e
+113.40.20.0.0
+  __TEXT.__text: 0x54bfc
+  __TEXT.__objc_methlist: 0x440c
+  __TEXT.__const: 0x1aa
+  __TEXT.__gcc_except_tab: 0xf40
+  __TEXT.__cstring: 0x5484
+  __TEXT.__oslogstring: 0x737e
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x18c0
+  __TEXT.__unwind_info: 0x18d0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1eb8
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__const: 0x1f58
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34f0
+  __DATA_CONST.__objc_selrefs: 0x3530
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x408
-  __DATA_CONST.__got: 0x11f8
+  __DATA_CONST.__got: 0x1208
   __AUTH_CONST.__const: 0x630
   __AUTH_CONST.__cfstring: 0x4c40
-  __AUTH_CONST.__objc_const: 0x6dd0
+  __AUTH_CONST.__objc_const: 0x6ec0
   __AUTH_CONST.__objc_arrayobj: 0x8d0
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__auth_got: 0x7e8
-  __AUTH.__objc_data: 0x638
-  __DATA.__objc_ivar: 0x2c8
+  __AUTH.__objc_data: 0x688
+  __DATA.__objc_ivar: 0x2d0
   __DATA.__data: 0x7f0
   __DATA_DIRTY.__objc_data: 0xa28
   __DATA_DIRTY.__data: 0x28

   - /System/Library/PrivateFrameworks/DMCTools.framework/DMCTools
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
   - /System/Library/PrivateFrameworks/EnhancedLogging.framework/EnhancedLogging
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1718
-  Symbols:   3439
-  CStrings:  1282
+  Functions: 1725
+  Symbols:   3457
+  CStrings:  1284
 
Symbols:
+ +[MDMDeviceRecoveryUtilities setEraseAndUpdateRestricted:completionHandler:]
+ +[MDMDeviceRecoveryUtilities shouldManageEraseAndUpdateRestriction]
+ -[MDMServerCore _updateDeviceRecoveryEraseAndUpdateRestrictionIsMDMConfigurationValid:]
+ -[MDMServerCore hrnPollTask]
+ -[MDMServerCore memberQueueLastAppliedEraseAndUpdateRestriction]
+ -[MDMServerCore setHrnPollTask:]
+ -[MDMServerCore setMemberQueueLastAppliedEraseAndUpdateRestriction:]
+ -[MDMServerCore setTokenUpdateRetryTask:]
+ -[MDMServerCore tokenUpdateRetryTask]
+ -[MDMServerCore(HRN) _hrnBackgroundPollFromTask:]
+ -[MDMServerCore(HRN) _hrnIsRepeatingPollActiveWithInterval:]
+ -[MDMServerCore(HRN) _hrnMemberQueueSetupRepeatingPoll]
+ -[MDMServerCore(HRN) _hrnPollOrScheduleNextPoll]
+ GCC_except_table145
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table179
+ GCC_except_table183
+ GCC_except_table190
+ GCC_except_table198
+ GCC_except_table2
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table214
+ GCC_except_table222
+ GCC_except_table237
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table264
+ GCC_except_table289
+ GCC_except_table312
+ GCC_except_table324
+ GCC_except_table328
+ GCC_except_table34
+ GCC_except_table343
+ GCC_except_table359
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table75
+ GCC_except_table93
+ _OBJC_CLASS_$_DeviceRecoveryController
+ _OBJC_CLASS_$_MDMDeviceRecoveryUtilities
+ _OBJC_IVAR_$_MDMServerCore._hrnPollTask
+ _OBJC_IVAR_$_MDMServerCore._memberQueueLastAppliedEraseAndUpdateRestriction
+ _OBJC_IVAR_$_MDMServerCore._tokenUpdateRetryTask
+ _OBJC_METACLASS_$_MDMDeviceRecoveryUtilities
+ __OBJC_$_CLASS_METHODS_MDMDeviceRecoveryUtilities
+ __OBJC_$_INSTANCE_METHODS_MDMServerCore(HRN)
+ __OBJC_CLASS_RO_$_MDMDeviceRecoveryUtilities
+ __OBJC_METACLASS_RO_$_MDMDeviceRecoveryUtilities
+ ___48-[MDMServerCore(HRN) _hrnPollOrScheduleNextPoll]_block_invoke
+ ___49-[MDMServerCore(HRN) _hrnBackgroundPollFromTask:]_block_invoke
+ ___49-[MDMServerCore(HRN) _hrnBackgroundPollFromTask:]_block_invoke_2
+ ___49-[MDMServerCore(HRN) _hrnBackgroundPollFromTask:]_block_invoke_3
+ ___55-[MDMServerCore(HRN) _hrnMemberQueueSetupRepeatingPoll]_block_invoke
+ ___55-[MDMServerCore(HRN) _hrnMemberQueueSetupRepeatingPoll]_block_invoke_2
+ ___64-[MDMServerCore _executionQueueScheduleTokenUpdateRetryIfNeeded]_block_invoke
+ ___64-[MDMServerCore _executionQueueScheduleTokenUpdateRetryIfNeeded]_block_invoke_2
+ ___64-[MDMServerCore _executionQueueScheduleTokenUpdateRetryIfNeeded]_block_invoke_3
+ ___76+[MDMDeviceRecoveryUtilities setEraseAndUpdateRestricted:completionHandler:]_block_invoke
+ ___87-[MDMServerCore _updateDeviceRecoveryEraseAndUpdateRestrictionIsMDMConfigurationValid:]_block_invoke
+ ___87-[MDMServerCore _updateDeviceRecoveryEraseAndUpdateRestrictionIsMDMConfigurationValid:]_block_invoke_2
+ ___87-[MDMServerCore _updateDeviceRecoveryEraseAndUpdateRestrictionIsMDMConfigurationValid:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e34_v16?0"DMCBackgroundTaskWrapper"8ls32l8
+ ___block_descriptor_41_e8_32bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8
+ ___block_descriptor_41_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
- -[MDMServerCore _backgroundPollFromTask:]
- -[MDMServerCore _memberQueuePollForHRNFromBackgroundTask:]
- -[MDMServerCore _memberQueuePollOrScheduleNextPollForHRNFromBackgroundTask:]
- -[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]
- -[MDMServerCore _pollOrScheduleNextPollForHRN]
- -[MDMServerCore _pollingFailed]
- -[MDMServerCore _scheduleNextPollWithInterval:]
- -[MDMServerCore pollTask]
- -[MDMServerCore setPollTask:]
- GCC_except_table143
- GCC_except_table163
- GCC_except_table167
- GCC_except_table173
- GCC_except_table177
- GCC_except_table184
- GCC_except_table189
- GCC_except_table192
- GCC_except_table194
- GCC_except_table208
- GCC_except_table211
- GCC_except_table216
- GCC_except_table231
- GCC_except_table236
- GCC_except_table238
- GCC_except_table258
- GCC_except_table292
- GCC_except_table31
- GCC_except_table310
- GCC_except_table323
- GCC_except_table335
- GCC_except_table350
- GCC_except_table354
- GCC_except_table370
- GCC_except_table43
- GCC_except_table48
- GCC_except_table73
- GCC_except_table91
- _OBJC_IVAR_$_MDMServerCore._pollTask
- __OBJC_$_INSTANCE_METHODS_MDMServerCore
- ___41-[MDMServerCore _backgroundPollFromTask:]_block_invoke
- ___41-[MDMServerCore _backgroundPollFromTask:]_block_invoke_2
- ___41-[MDMServerCore _backgroundPollFromTask:]_block_invoke_3
- ___41-[MDMServerCore _backgroundPollFromTask:]_block_invoke_4
- ___46-[MDMServerCore _pollOrScheduleNextPollForHRN]_block_invoke
- ___47-[MDMServerCore _scheduleNextPollWithInterval:]_block_invoke
- ___57-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]_block_invoke
- ___57-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]_block_invoke_2
- ___58-[MDMServerCore _memberQueuePollForHRNFromBackgroundTask:]_block_invoke
- ___58-[MDMServerCore _memberQueuePollForHRNFromBackgroundTask:]_block_invoke_2
CStrings:
+ "-[MDMServerCore _executionQueueScheduleTokenUpdateRetryIfNeeded]_block_invoke"
+ "-[MDMServerCore(HRN) _hrnBackgroundPollFromTask:]_block_invoke"
+ "-[MDMServerCore(HRN) _hrnMemberQueueSetupRepeatingPoll]"
+ "MDMDeviceRecoveryUtilities: Failed to update Device Recovery erase and update restriction. Restricted: %d, error: %{public}@"
+ "MDMDeviceRecoveryUtilities: Updated Device Recovery erase and update restriction. Restricted: %d"
+ "MDMServerCore HRN polling now (from repeating background task)..."
+ "MDMServerCore _hrnMemberQueueSetupRepeatingPoll: interval changed from %{public}f to %{public}f, updating."
+ "MDMServerCore _hrnMemberQueueSetupRepeatingPoll: pollingIntervalMinutes=%lu, pollingInterval=%@"
+ "MDMServerCore _hrnMemberQueueSetupRepeatingPoll: repeating poll already active with same interval (%{public}f), skipping."
+ "MDMServerCore _hrnPollOrScheduleNextPoll: entering (isSharediPad=NO)"
+ "MDMServerCore _hrnPollOrScheduleNextPoll: skipping because isSharediPad=YES"
+ "MDMServerCore _readConfigurationOutError: calling _hrnPollOrScheduleNextPoll (valid=%d)"
+ "MDMServerCore repeating poll fired but device is not HRN, cancelling."
+ "MDMServerCore submitting repeating poll with interval %{public}f seconds."
+ "MDMServerCore will retry token update in %{public}f seconds..."
+ "com.apple.devicemanagementclient.mdmd.tokenupdate.retry"
- "(nil)"
- "-[MDMServerCore _backgroundPollFromTask:]_block_invoke"
- "-[MDMServerCore _memberQueuePollForHRNFromBackgroundTask:]"
- "-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]"
- "MDMServerCore HRN polling now (from background task)..."
- "MDMServerCore HRN scheduling next poll in %{public}f seconds..."
- "MDMServerCore _memberQueuePollOrScheduleNextPollForHRN: pollingIntervalMinutes=%lu, pollingInterval=%@, fromBackgroundTask=%d"
- "MDMServerCore _pollOrScheduleNextPollForHRN: entering (isSharediPad=NO)"
- "MDMServerCore _pollOrScheduleNextPollForHRN: skipping because isSharediPad=YES"
- "MDMServerCore _readConfigurationOutError: calling _pollOrScheduleNextPollForHRN (valid=%d)"
- "MDMServerCore _scheduleNextPollWithInterval: interval=%{public}f, targetPollDate=%{public}@"
- "MDMServerCore ignoring excessive poll scheduling (in %{public}f seconds). Next poll expected at: %{public}@."
- "MDMServerCore scheduling poll in %{public}f (+%{public}f) seconds."
- "MDMServerCore will retry token update..."
```
