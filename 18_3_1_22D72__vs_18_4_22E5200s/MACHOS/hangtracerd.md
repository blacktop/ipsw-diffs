## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-331.3.0.0.0
-  __TEXT.__text: 0x304dc
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_stubs: 0x52c0
-  __TEXT.__objc_methlist: 0x1d44
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x4d6d
+352.0.0.0.0
+  __TEXT.__text: 0x30830
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_stubs: 0x5320
+  __TEXT.__objc_methlist: 0x2024
+  __TEXT.__const: 0x2b8
+  __TEXT.__cstring: 0x4bb7
   __TEXT.__objc_classname: 0x31f
-  __TEXT.__objc_methname: 0x8476
-  __TEXT.__objc_methtype: 0x108c
-  __TEXT.__gcc_except_tab: 0x644
-  __TEXT.__oslogstring: 0x568c
-  __TEXT.__unwind_info: 0x8b8
-  __DATA_CONST.__auth_got: 0x758
+  __TEXT.__objc_methname: 0x8538
+  __TEXT.__objc_methtype: 0x1005
+  __TEXT.__gcc_except_tab: 0x5b4
+  __TEXT.__oslogstring: 0x5872
+  __TEXT.__unwind_info: 0x988
+  __DATA_CONST.__auth_got: 0x770
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2070
-  __DATA_CONST.__cfstring: 0x66c0
+  __DATA_CONST.__const: 0x1ec8
+  __DATA_CONST.__cfstring: 0x63a0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x4cf8
-  __DATA.__objc_selrefs: 0x19b0
-  __DATA.__objc_ivar: 0x408
+  __DATA.__objc_const: 0x4950
+  __DATA.__objc_selrefs: 0x1a60
+  __DATA.__objc_ivar: 0x41c
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x548
-  __DATA.__bss: 0xc00
-  __DATA.__common: 0x48
+  __DATA.__bss: 0xa98
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 957
-  Symbols:   372
-  CStrings:  2859
+  Functions: 1108
+  Symbols:   375
+  CStrings:  2851
 
Symbols:
+ __os_log_error_impl
+ _dispatch_queue_get_label
+ _notify_register_check
+ _notify_set_state
- _dispatch_block_create_with_qos_class
CStrings:
+ "\x14\x11"
+ "%s: No hangs found, not collecting tailspin\n"
+ "%s: Posting notification to Sentry due to failure to dump tailspin. {%@}"
+ "%{public}@: Unable to move tailspin to final path: %{public}@ Error: %@"
+ "+[HTTailspin saveSentryTailspin:infoDict:startTime:endTime:error:]_block_invoke"
+ "+[HTTailspin saveTailspinForAllPendingHangs]"
+ "Attempting to decrement Pending Tailspin Block count when it is at %d"
+ "CPU Limit"
+ "Check for Pending Hangs"
+ "Client XPC Event"
+ "Failed to move tailspin to final path: %@"
+ "Failed to post com.apple.hangtracerd.processing notification."
+ "ForceQuit monitoring already enabled for %@"
+ "HangHUD"
+ "HangTracerConsecutiveHangWaitTimeoutDuration"
+ "More than %d pending tailspin blocks, tailspin is not responding to hangtracerd tailspin requests"
+ "Number of agents is already at zero, mismatching number of decrement requests to increment requests."
+ "PDSEPrefWBClientHangKillSwitch"
+ "PDSEPrefWBClientHangPeriodDays"
+ "Pending Tailspin Block count: %i -> %i"
+ "Recieved incoming work notification from %s, adding increment block to queue '%s' for com.apple.hangtracerd.processing"
+ "Recieved work completion notification from %s, adding decrement block to queue '%s'"
+ "Record Fence Hang"
+ "Record Hang"
+ "Self Restrict"
+ "Sentry Tailspin Request"
+ "Successfully changed state of com.apple.hangtracerd.processing from 0 —> 1"
+ "Successfully changed state of com.apple.hangtracerd.processing from 1 -> 0"
+ "Successfully posted com.apple.hangtracerd.processing notification."
+ "T@\"NSString\",C,N,V_processName"
+ "TB,N,V_isInstantiatedInHangHUDProcess"
+ "TB,R,V_pdseWBClientHangKillSwitch"
+ "TB,R,V_shouldAugmentSentryTailspinWithSignposts"
+ "TQ,R,V_consecutiveHangWaitTimeoutDurationMSec"
+ "TSPDumpOptions_EndTimestamp"
+ "Tailspin Request"
+ "Tailspin dump request failed with error (%s)"
+ "TailspinRequestType"
+ "Ti,R,V_pdseWBClientHangPeriodDays"
+ "Unable to change state of com.apple.hangtracerd.processing from 0 —> 1"
+ "Unable to change state of com.apple.hangtracerd.processing from 1 -> 0"
+ "Unable to check-in with notification: %d (token %d)"
+ "_consecutiveHangWaitTimeoutDurationMSec"
+ "_isInstantiatedInHangHUDProcess"
+ "_pdseWBClientHangKillSwitch"
+ "_pdseWBClientHangPeriodDays"
+ "_shouldAugmentSentryTailspinWithSignposts"
+ "com.apple.hangtracer.tailspin_requests"
+ "com.apple.hangtracer.tailspin_requests %@: %@, request_success: %@, request_type: %@, failure_reason: %@\n"
+ "com.apple.hangtracerd.processing"
+ "com.apple.hangtracerd.state"
+ "consecutiveHangWaitTimeoutDurationMSec"
+ "cpu limit"
+ "dataWithBytes:length:"
+ "decrementPendingTailspinBlocks"
+ "event->bundleID has been corrupted, final char in array is not \\0. bundleID: %s"
+ "event->serviceName has been corrupted, final char in array is not \\0. serviceName: %s"
+ "failed to move %@ to %@: %@"
+ "hangtracerd already has in-flight work (active agents: %d), not attempting to modify state of com.apple.hangtracerd.processing."
+ "hangtracerd still has in-flight work (active agents: %d), not attempting to modify state."
+ "incrementPendingTailspinBlocks"
+ "initWithBytes:length:encoding:"
+ "isInstantiatedInHangHUDProcess"
+ "libtailspin: tailspin_dump_output_with_options() failed to dump tailspin"
+ "pdseWBClientHangKillSwitch"
+ "pdseWBClientHangPeriodDays"
+ "saveTailspinForAllPendingHangs"
+ "saveTailspinForForceQuit:completionBlock:"
+ "saveTailspinWithFileName:directoryPath:infoDictArray:startTime:endTime:processName:pid:requestType:includeOSSignposts:completionQueue:completionHandler:"
+ "self restrict"
+ "sendHudConfigurationToHangHUD_block_invoke"
+ "setIsInstantiatedInHangHUDProcess:"
+ "setProcessName:"
+ "shouldAugmentSentryTailspinWithSignposts"
+ "stringByAppendingPathComponent:"
+ "tailspin_dump_output_with_options"
+ "v12@?0B8"
+ "v16@?0q8"
+ "v96@0:8@16@24@32Q40Q48@56i64q68B76@80@?88"
+ "\xf0\xf0Q!!\x17!"
- "\x13\x11"
- "%@ Launch Generated Log count : %u -> %u"
- "%@ Launch Generated Log count: %u -> %u"
- "%@ is hit Generated Log limit of %u. Not saving a report!"
- "%@.%@ += 1"
- "%@.%@.%@"
- "%@.%@.%@ += 1"
- "%@.%@.%@ += 1 "
- "%@.%@.%@ == %i"
- "%@.%@.%@ value=%f"
- "%@.%@.%@%02i.%@.%@"
- "%@.%@.%@.%@"
- "%@.%@.%@.%@ value=%f"
- "%{public}@: Tailspin Request Denied because tailspin-buffer has been dumped since this hang ended -> it won't have any trace data for this hang\n"
- "%{public}@: Unable to move tailspin to final path: %{public}@"
- "Adjacent_Request_Intervals"
- "All_Request_Intervals"
- "B116@0:8@16@24i32Q36@44@52Q60Q68Q76q84@92B100B104^q108"
- "B44@0:8i16@20@28^@36"
- "B64@0:8@16@24@32i40Q44Q52B60"
- "B76@0:8@16@24Q32Q40@48i56q60^q68"
- "B88@0:8@16@24@32Q40Q48@56i64q68B76^q80"
- "BeginWithinThreshold"
- "Daily Generated Launch Log count: %u -> %u"
- "Device has hit the Daily Generated Log limit of %u. Not saving a report!"
- "EndTime_To_TailspinTime"
- "EndWithinThreshold"
- "HT_Tailspin_Request_Reporting_Queue"
- "HangTracer tailspin support is disabled, not saving a report for %@ activation!"
- "Intermediate_Hangs_For_Overlap_Type"
- "Intervals_E1toE2"
- "Intervals_E1toS2"
- "Intervals_S1toE2"
- "Intervals_S1toS2"
- "LatestRequestType"
- "Nested_Overlap"
- "No hangs found to update telemetry\n"
- "No_Overlap"
- "NumberRequestsBetween"
- "Out_Of_Order_Request"
- "OverlapType"
- "Overlap_Counts"
- "Partial_Overlap"
- "PreviousDumpTime_To_RequestEndTime"
- "RequestEndTime_To_CurrentTime"
- "RequestType"
- "TB,R,V_shouldCollectOSSignpostsDeferred"
- "TSPDumpOptions_MaxTimestamp"
- "Tailspin Request Denied: tailspin-buffer will not contain relevant trace data for the time-range of this request due to recent tailspin-capture\n               Filename: %{public}@, Process: %{public}@, Time Between Recent Tailspin Capture and Hang EndTime: %f secs, Hang EndTime: %f secs ago, Recent Tailspin Capture: %f secs ago\n"
- "Tailspin_Request_Denied"
- "Tailspin_Requests"
- "Tailspin_Requests_By_Type"
- "Tailspin_Requests_End_Within_Threshold"
- "Tailspin_Requests_Start_Within_Threshold"
- "Threshold"
- "Threshold="
- "Tried to save tailspin for %@ activation, but tailspin support is not present on this device!"
- "Type"
- "_shouldCollectOSSignpostsDeferred"
- "collectTailspinAndUpdateTelemtry"
- "collectTailspinAndUpdateTelemtry: No hangs found, not collecting tailspin\n"
- "com.apple.hangtracer.overlap_stats"
- "com.apple.hangtracer.tailspins"
- "com.apple.hangtracer.tailspins.Overlap_Counts"
- "com.apple.hangtracer.tailspins.Tailspin_Requests_Within_Threshold"
- "com.apple.hangtracer.tailspins.denied_request"
- "detection"
- "failed to move %s/%@: %@"
- "hang"
- "htPrefsRefreshedNotificationCallback_block_invoke"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "libtailspin: tailspin_dump_output_with_options_sync() failed to dump tailspin"
- "matuTimeDifferenceMS: negative distance = %f"
- "monitorForForceQuit_block_invoke_2"
- "nonhang"
- "numberWithFloat:"
- "reportTailspinRequestStats( type=%@, start=%llu, end=%llu, tailspin=%llu )"
- "saveActivationTailSpinWithType:reason:bundleID:pid:startTime:endTime:isThirdPartyDevSupportModeHang:"
- "saveTailSpinForService:reason:processID:threadID:procName:procPath:startTime:endTime:blownFenceId:hangType:userActionData:displayedInHUD:isThirdPartyDevSupportModeHang:failReason:"
- "saveTailSpinWithFileName:infoDictArray:startTime:endTime:processString:pid:requestType:failReason:"
- "saveTailspinForAllHangs"
- "saveTailspinForForceQuitProcessID:procName:procPath:filePath:"
- "saveTailspinWithFileName:path:infoDictArray:startTime:endTime:processString:pid:requestType:includeOSSignposts:failReason:"
- "shouldCollectOSSignpostsDeferred"
- "tailspin_dump_output_with_options_sync"
- "timegap"
- "\xf0\xf0A\x11!\x17!"

```
