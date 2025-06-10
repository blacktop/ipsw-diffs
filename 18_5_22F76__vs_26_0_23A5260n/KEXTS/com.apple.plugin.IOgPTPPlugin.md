## com.apple.plugin.IOgPTPPlugin

> `com.apple.plugin.IOgPTPPlugin`

```diff

-1340.12.0.0.0
-  __TEXT.__cstring: 0x6167
-  __TEXT.__os_log: 0x1a55c
-  __TEXT.__const: 0x268
-  __TEXT_EXEC.__text: 0x75678
+1400.53.0.0.0
+  __TEXT.__cstring: 0x6782
+  __TEXT.__os_log: 0x1c53d
+  __TEXT.__const: 0x2c2
+  __TEXT_EXEC.__text: 0x7c854
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x5d8
-  __DATA_CONST.__auth_got: 0x708
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__mod_init_func: 0x110
-  __DATA_CONST.__mod_term_func: 0x110
-  __DATA_CONST.__const: 0xeb08
-  __DATA_CONST.__kalloc_type: 0x940
+  __DATA.__common: 0x600
+  __DATA.__bss: 0xc8
+  __DATA_CONST.__auth_got: 0x790
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__mod_init_func: 0x118
+  __DATA_CONST.__mod_term_func: 0x118
+  __DATA_CONST.__const: 0xf168
+  __DATA_CONST.__kalloc_type: 0x9c0
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 5B154A44-045E-38B2-853A-416A95EA6416
-  Functions: 1573
+  UUID: 39320EE7-BBF1-37A4-9A05-E3B7A717AFE4
+  Functions: 1640
   Symbols:   0
-  CStrings:  1426
+  CStrings:  1580
 
CStrings:
+ "  %s(%s): %s ntpAndUpTimeOffsetNsec:%lld isLocalClockSourceFromNTP:%d"
+ "  %s(%s): Attempt to unset as preferred gm but the device does not have preferred gm set"
+ "  %s(%s): Failed to send lucky filtered delay statistics to CoreAnalytics %s"
+ "  %s(%s): Failure: Lucky Filter %u perCent rejected"
+ "  %s(%s): Failure: Lucky Filter ceiling method rejected"
+ "  %s(%s): Failure: Lucky Filter window size %u rejected"
+ "  %s(%s): LFAttempting to synthesize %u EtE timestamps between {0x%llx.%016llx (%llu), %llu} and {0x%llx.%016llx (%llu), %llu} but intervals are out of bounds lower limit %llu upper limit %llu remote %llu local %llu, resetting\n"
+ "  %s(%s): LFAttempting to synthesize EtE timestamps but there is no previous time to compute from.\n"
+ "  %s(%s): LFAttempting to synthesize but last GM identity (0x%016llx) and current GM identity (0x%016llx) mismatch, resetting\n"
+ "  %s(%s): LFCalculated that we lost %u syncs which is equal to or larger than the timeout count of %u, resetting. %u,%u,%u\n"
+ "  %s(%s): LFChanged PPM drop limit to %u for interval %d\n"
+ "  %s(%s): LFDelayEtE:%llu,%lld,%lld,%u,%u,%lld\n"
+ "  %s(%s): LFDelayEtE_Error:%llu,%lld,%lld,%u,%u,%lld\n"
+ "  %s(%s): LFEtE Sync %u, %u difference is out of %u ppm limits. remote difference %llu, local difference %llu, min difference %llu, max difference %llu\n"
+ "  %s(%s): LFEtE Sync %u, %u difference is out of %u ppm limits. remote difference %llu, local difference %llu, min difference %llu, max difference %llu. Allowing through.\n"
+ "  %s(%s): LFEtE Sync scaledRateRatio is above upper limit %llu > %llu (%u ppm), clamping and resetting filter"
+ "  %s(%s): LFEtE Sync scaledRateRatio is below lower limit %llu < %llu (%u ppm), clamping and resetting filter"
+ "  %s(%s): LFEtE Sync timestamps %u,0x%llx.%016llx,%llu,0x%llx.%016llx,%llu,%u,%s\n"
+ "  %s(%s): LFEtE dropped Sync %u,%u,%u,%u,%llu,%llu,%llu,%llu,%llu,%llu,%llu,%llu\n"
+ "  %s(%s): LFFilterEtE:%llx.%016llx,%llu,%llx.%016llx,%llu,%llu,%llu,%u,%u,%d,%d,%016llx\n"
+ "  %s(%s): LFMetric:%lld, %lld,%llu,%lld,%lld,%llu,%d"
+ "  %s(%s): LFProcEtE:%llx.%016llx,%llu,%llu,%llu,%llx.%016llx,%llu,%llx.%016llx,%llu,%llu,%lld,%lld,%u,%u,%d,%d,%016llx\n"
+ "  %s(%s): LFRemote Sync Exchange is ludicrously huge %llx.%016llx\n"
+ "  %s(%s): LFRemote Sync Log Mean Interval changed from %d to %d, re-initialized filter with new nominal\n"
+ "  %s(%s): LFRemote Sync Log Mean Interval changed from %d to %d, scaling intervals by %d to %llu, %llu\n"
+ "  %s(%s): LFResetting sync filter for too many dropped (%u dropped exceeds %u limit)"
+ "  %s(%s): LFResponse time (%llu) is longer than scaled exchange time (%llu), raw delay %lld filter %llu,%llu,%llu,%llu\n"
+ "  %s(%s): LFResponse time (%llu) is longer than scaled exchange time (%llu)with no conversion, clamping to 0\n"
+ "  %s(%s): LFSyncEtE:0x%llx.%016llx,%llu,%lld,%llu,%lld,%u,0x%016llx,%u,%u,%d,%lld,%lld,%d,%d,0x%016llx\n"
+ "  %s(%s): LFSynthesizing %u EtE timestamps between {0x%llx.%016llx (%llu), %llu} and {0x%llx.%016llx (%llu), %llu} with interval {%llu, %llu}\n"
+ "  %s(%s): LFSynthesizing EtE timestamp %u %llx.%016llx,%llu,%llx.%016llx,%llu\n"
+ "  %s(%s): LFTimestamps are out of order.  Skipping delay calculation.\n"
+ "  %s(%s): LFt1=%llx.%016llx (%llu) t2=%llu t3=%llu t4=%llx.%016llx (%llu)\n"
+ "  %s(%s): Lucky Filter EtE logging is %s"
+ "  %s(%s): Lucky Filter adjustment method set to %u"
+ "  %s(%s): Lucky Filter is %s"
+ "  %s(%s): Lucky Filter maximum ceiling set to %u\n"
+ "  %s(%s): Lucky Filter perCent set to %u"
+ "  %s(%s): Lucky Filter random parameters: %s"
+ "  %s(%s): Lucky Filter window size: %u"
+ "  %s(%s): LuckyFilter:Filtered delay index is equal to 0.Skipped calculating statistics"
+ "  %s(%s): LuckyFilter:History buffer full"
+ "  %s(%s): LuckyFilter:QuickSort failed"
+ "  %s(%s): LuckyFilterEtE:%llu,%u,%lld,%lld,%lld,%lld,%llu,%llu,%llu"
+ "  %s(%s): OrgMetric:%llu,%lld, %lld,%llu,%lld,%lld,%u"
+ "  %s(%s): OriginalFilter:Filtered delay index is equal to 0.Skipped calculating statistics"
+ "  %s(%s): OriginalFilter:History buffer is full"
+ "  %s(%s): Rejecting attempt to set preferred GM %u.  Use boot-arg \"timesync-preferred-gm=1\" to enable this feature"
+ "  %s(%s): Rejecting attempt to set preferred GM on battery powered device"
+ "  %s(%s): Rejecting attempt to set preferred GM on domain %#llx of type %u"
+ "  %s(%s): Rejecting attempt to update ntp anchor offset on unsupported domain %#llx of type %u"
+ "  %s(%s): Rejecting attempt to update ntp anchor offset since there is no IOTimeSyncTimeOfDayAnchorPort localport"
+ "  %s(%s): Sending metrics for lucky filter and original behavior"
+ "  %s(%s): Set as Preferred GM"
+ "  %s(%s): SyncEtE:0x%llx.%016llx,%llu,%lld,%llu,%lld,%u,0x%016llx,%u,%u,%d,%lld,%lld,%d,%d,0x%016llx\n"
+ "  %s(%s): Unset as Preferred GM"
+ "  %s(%s): calculateDelayStatistics failed"
+ " IOgPTPPlugin assertion FailIfWithAction \"%s\" failed in %s at line %d goto Exit. "
+ "!_IOTimeSyncTimeIsMach"
+ "!fSupportCoPresenceDomain"
+ "%s = %llu"
+ "%s = %s"
+ "%s Copresence domainIdentifier = 0x%llx ntpAndUpTimeOffsetNsec = %lld isLocalClockSourceFromNTP = %d"
+ "%s Using IOSkywalkLegacyEthernet as no other controller was found for %s%u\n"
+ "%s fCopresenceInstanceReferenceCount = %lld"
+ "121111121222121211111111122111111111111111111111122222222222221222222222222222222222222222222222222222222222222222222222211111111111111111111111111112222222"
+ "12111112122212121121121122222222222212211111222222222212112222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222222222222222222222222222222222222222222"
+ "1211111212221212112112112222222222221221111122222222221211222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222222222222222222222222222222222222222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222222222"
+ "12111112122212121121121122222222222212211111222222222212112222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222222222222222222222222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222222222"
+ "1211111212221212112112112222222222221221111122222222221211222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222222222222222222222222222222222222222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222222222222"
+ "12111112122212121121121122222222222212211111222222222212112222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222222222222222222222222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222222222222222"
+ "1211111212221212112112112222222222221221111122222222221211222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222222222222222222222222222222222222222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222222222222222222222"
+ "1211111212221212112112112222222222221221111221222222222212"
+ "1211111212221212112112112222222222221221111221222222222212222"
+ "1211111212221212112112112222222222221221111221222222222212222212"
+ "2222222222222222221"
+ "Copresence instance is created. Use TimeSyncAddCopresencePTPInstanceRef to add a reference count\n"
+ "Doesn't support copresence domain\n"
+ "Doesn't support copresence domain with PMGR clock\n"
+ "Event: %s"
+ "Failed to add persistent user clock\n"
+ "Failed to add persistent user clock reference\n"
+ "Failed to allocate lucky sync filter\n"
+ "Failed to create eventName\n"
+ "Failed to create eventPayload\n"
+ "Failed to get persistent user clock\n"
+ "Failed to remove persistent user clock\n"
+ "IOTimeSyncNetworkPortDaemonClient::sendAsyncNotification: notification=%u arg1=%llu arg2=%llu arg3=%llu arg4=%llu arg5=%llu arg6=%llu"
+ "IOTimeSyncTimeOfDayAnchorPort"
+ "IOTimeSyncgPTPManagerDaemonClient::dockReplayTimestamps: fProcessID = %u\n"
+ "LocalClockSourceFromNTP"
+ "MachTimeOffset"
+ "NULL == bsdName"
+ "NULL == clockID"
+ "NULL == eventName"
+ "NULL == eventPayload"
+ "NULL == fLFSyncTimeLine"
+ "NULL == ifOut"
+ "NULL == interfaces"
+ "NULL == userID"
+ "NULL clockID\n"
+ "NULL userID\n"
+ "NtpAnchorOffsetNsec"
+ "Reverse sync already exists\n"
+ "Unknown OSObject subtype for idx %u"
+ "[%u] t1=%llu,t2=%llu,t3=%llu,t4=%llu,seq=%llu\n"
+ "addCopresenceDomain"
+ "addCopresenceDomainRef"
+ "bsdName = %s"
+ "bsdName == nullptr\n"
+ "bytesRead == replayLength"
+ "bytesRead == replayTimestampsLength"
+ "ceiling"
+ "ceilingAdjustmentMethod"
+ "com.apple.TimeSync.LuckyFilteredDelays"
+ "com.apple.TimeSync.OriginalAllDelays"
+ "com.apple.TimeSync.OriginalFilteredStatistics"
+ "disabled"
+ "enabled"
+ "fCopresenceInstanceReferenceCount != 0"
+ "feth"
+ "filterResetOutOfBounds"
+ "filterResetPPMLimit"
+ "floor"
+ "ifOut == nullptr\n"
+ "interface != nullptr"
+ "interface == nullptr"
+ "interface is not a test interface\n"
+ "interface not found\n"
+ "interfaces == nullptr\n"
+ "linkType"
+ "max"
+ "mean"
+ "median"
+ "mem != nullptr"
+ "mem->complete() == kIOReturnSuccess"
+ "mem->prepare(kIODirectionOutIn) == kIOReturnSuccess"
+ "min"
+ "obj == nullptr"
+ "outOfBoundResets"
+ "packetDiscardedDelayLimit"
+ "packetDiscardedPPMLimit"
+ "perCent"
+ "ppmDropCount"
+ "ppmDropLimit"
+ "ppmDropResets"
+ "priorityCalculationInputs"
+ "removeCopresenceDomain"
+ "result != kIOReturnSuccess"
+ "ret == kIOReturnSuccess"
+ "samples"
+ "scaledDelayLimit"
+ "site.IOTimeSyncTimeOfDayAnchorPort"
+ "site.TSReplayTimestamps"
+ "stddev"
+ "syncRate = %lld portType = %llu timestampCount = %llu\n"
+ "task != nullptr"
+ "timesync-preferred-gm"
+ "timesync_log_lucky_filter_ete"
+ "timesync_lucky_filter"
+ "timesync_lucky_filter_ceiling_method"
+ "timesync_lucky_filter_per_cent"
+ "timesync_lucky_filter_random_parameters"
+ "timesync_lucky_filter_window_size"
+ "timesync_support_copresence_domain"
+ "timesync_test_interface"
+ "updateNtpAnchorOffset"
+ "windowSize"
- "  %s(%s): DelayLongStatsEtE:%llu,%lld,%lld,%llu,%lld,%lld,%u\n"
- "  %s(%s): SyncEtE:0x%llx.%016llx,%llu,%lld,%llu,%lld,%u,0x%016llx,%u,%u,%d,%lld,%lld,%d,%d,%016llx\n"
- "121111121222121211111111122111111111111111111111122222222222212222222222222222222222222222222222222222222222222222222222111111111111111111111111111122222"
- "12111112122212121121121122222222222212211111222222221211222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222222222222222222222222222222222222"
- "1211111212221212112112112222222222221221111122222222121122211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222222222222222222222222222222222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222222222"
- "12111112122212121121121122222222222212211111222222221211222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222222222222222222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222222222"
- "1211111212221212112112112222222222221221111122222222121122211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222222222222222222222222222222222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222222222222"
- "12111112122212121121121122222222222212211111222222221211222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222222222222222222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222222222222222"
- "1211111212221212112112112222222222221221111122222222121122211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222222222222222222222222222222222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222222222222222222222"
- "121111121222121211211211222222222222122111122122222222212"
- "121111121222121211211211222222222222122111122122222222212222212"
- "IOTimeSyncNetworkPortDaemonClient::sendAsyncNotification: notification=%u arg1=%u arg2=%u arg3=%u arg4=%u arg5=%u arg6=%u"
- "Using IOSkywalkLegacyEthernet as no other controller was found for %s%u\n"
- "fCopresenceInstanceReferenceCount == INT64_MAX"

```
