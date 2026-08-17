## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3350.75.2.0.0
-  __TEXT.__text: 0xc2c338
+3350.77.1.6.0
+  __TEXT.__text: 0xc2ca54
   __TEXT.__lazy_helpers: 0x3618
   __TEXT.__objc_methlist: 0x2b74
-  __TEXT.__const: 0x29730
-  __TEXT.__cstring: 0x714d7
-  __TEXT.__oslogstring: 0x66b47
+  __TEXT.__const: 0x29720
+  __TEXT.__cstring: 0x71567
+  __TEXT.__oslogstring: 0x670f8
   __TEXT.__gcc_except_tab: 0x15ec
   __TEXT.__dlopen_cstrs: 0x32e
   __TEXT.__ustring: 0x24e

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0x14870
+  __TEXT.__unwind_info: 0x14878
   __TEXT.__eh_frame: 0x478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x248b8
+  __DATA_CONST.__const: 0x249a8
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__got: 0x4938
   __AUTH_CONST.__const: 0x47d98
-  __AUTH_CONST.__cfstring: 0x503e0
+  __AUTH_CONST.__cfstring: 0x504a0
   __AUTH_CONST.__objc_const: 0x59c8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__lazy_load_got: 0x4e0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 43696
-  Symbols:   45191
-  CStrings:  20939
+  Functions: 43693
+  Symbols:   45200
+  CStrings:  20947
 
Symbols:
+ _FigAlternateSelectionBossIsFilteringInfoStale
+ _FigAssetExportSessionSimulateMediaServicesWereReset
+ _FigMediaSegmentSpecifierResetMapCachedState
+ _fpfs_DeferredDateMappingCallback
+ _fpfsi_ReadyForInspectionConditionsMet
+ _kFigAlternateSelectionBossFilteringInfoKey_BossCallbackID
+ _kFigAlternateSelectionBossProperty_LatestCallbackID
+ _kFigBytePumpProperty_HasDates
+ _kFigPlayerInterstitialNotification_CurrentEventChangeEventKey
+ _kFigReportingEventKey_MusicExperimentID
+ _kFigReportingEventKey_MusicTreatmentID
+ _sFigPlayerInterstitialEventOkToLogURLS
- _OUTLINED_FUNCTION_1000
- _OUTLINED_FUNCTION_1001
- _OUTLINED_FUNCTION_999
CStrings:
+ " enableTelemetry=YES item=%{public}s, itemRef=%llu"
+ "<<<< Boss >>>> %s: <%p|%{public}s> PrerollingWillPlay -> Paused (render pipeline invalidated -- presuming player will either rebuild render pipelines or tear everything down)"
+ "<<<< FigItemIntegratedTimeline >>>> %s: %p: %{public}s, can proceed to post SnapshotOutOfSync notifications"
+ "<<<< FigItemIntegratedTimeline >>>> %s: %p: Posting integrated timeline seek %{public}s notification with payload %@"
+ "<<<< FigItemIntegratedTimeline >>>> %s: %p: dispatching seek to target time %1.5g from %1.5g, source time %1.5g, source segment %{public}@, schedule %{public}@, minSnapTime %1.5g, maxSnapTime %1.5g, seekID %d"
+ "<<<< FigItemIntegratedTimeline >>>> %s: %p: primary %{public}s ready for inspection%{public}s"
+ "<<<< FigItemIntegratedTimeline >>>> %s: %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %f in %p is%{public}s between %f and %f"
+ "<<<< FigPlayerInterstitial >>>> %s: %p no matchingScheduleID in schedules for %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: %{public}s current event %{public}@, payload event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Adding new event for %{public}s item wrapper %p at %{public}s: %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: AirPlay is %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Excluding scheduled event %{public}s; starts past schedule end"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Merging and replacing event for %{public}s item wrapper %p at %{public}s: %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Removing no-longer-current event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Removing no-longer-current item %p / %{public}@ "
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Schedule notification %{public}@ payload %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Setting scheduled event %{public}s playoutLimit to %f"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Time jump-back from %f to %f, once=%d;%{public}s reconsider event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Time jump-back from %f to %f, once=%d;%{public}s reconsider schedule %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: Time jump-back from %f to %f, removed scheduled event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: asset %ld in event %{public}@ doesn't have a duration even though it's current"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: can buffer; need to make item(s) for %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: cancelling current event %{public}@ with reason %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: clearing intended current item moment %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: clearing state for seek ID %d into event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: could not find an event at %{public}s after resolving schedule %{public}@, cancel initiated seekID %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: current moment %{public}s, nextMoment %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: dequeuing %{public}@ from interstitialPlayer %p"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: discovered and populating abutting event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: encountered dummy item for event %{public}@, itemIndex %ld; skipping this for projected duration"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: enqueued %{public}@ for event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: established intended event to seek into - id %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: event %{public}@ - seekTime %f past duration - cancel initiated seekID %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: event %{public}@ was not immediately established, cancel initiated seekID %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: event %{public}@ was removed while seekID %d was still pending, cancelling the seek"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: eventIndex %d itemIndex %d: removedItem %p, tracked item %p %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: eventItem %d %{public}@ not on interstitialPlayer queue! Playback lost?"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: eventItem %{public}@ does not match interstitialPlayer item %{public}@!"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: found preloaded response for %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: got %{public}@ from %p, payload %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: hopping current departure moment from %{public}s to %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: hopping nextMoment from %{public}s to %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: hopping snappedNextMoment from %{public}s to %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: initiating seek into event ID %{public}@ at time %1.5g, minSnapTime %1.5g, maxSnapTime %1.5g, seekID %d, flags %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: interstitial event %{public}@ did finish, playedOutTime %f, didPlayEntireEvent %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: interstitial event %{public}@ was unscheduled with err %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: jump over current event at %{public}s to %{public}s; remove %d items"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: limited preload %{public}@: [%f(+%f).. %f(-%f))]-> %f%{public}s, now=%f :%f %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: nextMoment %{public}s appears to have snapped to %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: observed %{public}@ for primary item wrapper %p that isn't engaged."
+ "<<<< FigPlayerInterstitial >>>> %s: %p: observed all items failed for event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: observed an end time change while postroll was current, updating nextMoment from %{public}s to %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: observing seek out of event ID %{public}@, waiting on primary seekID %d to finish before doing anything else"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: posting initiated seek %{public}s notification for seek ID %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: reconfigured preload for %{public}@ to start at %{public}@ (%f), trigger at +%f"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: removing current event ID %{public}@ up to the intended event to seek into (%{public}@)"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: removing event %{public}@ for unengaged item wrapper %p"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: removing event ID %{public}@ at same moment but before the intended event to seek into (%{public}@)"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: removing event ID %{public}@ from past events"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: removing%{public}s event %{public}@ - %{public}@%{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: resumption seek ID %d %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: scheduled interstitial flip interrupted by timebase %{public}s! (rate %f, time %f)"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: scheduled liveBufferTimer for %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: scheduling timer for event %{public}@ to become %{public}s to be skipped at event offset %f, item offset %f"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: setting cached asset list response data for %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: setting cached schedule response data for %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: setting intended current item moment to %{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: setting internal playout limit %f on %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: setting preloaded cached asset list response data for %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: skip timer fired for event %{public}@ to become %{public}s, prior state %d"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: skippable state for event %{public}@ changed from %d to %d - posting notification and informing interstitial player"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: sorted eventsInAddOrder to %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: sortedEventsInAddOrder index for event %{public}@ was not found"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: stopping item %p at time %1.5g%{public}s"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: transfer playback %{public}s primary player %p %{public}s interstitial player %p"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updated eventsInAddOrder from previously cached events to %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updating coordinationMediaSelectionCriteria from %{public}@ to %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updating host's localized skip control label from %{public}@ to %{public}@ for locale %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updating interstitial player from %{public}@ to %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updating localized strings bundle from %{public}@ to %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updating localized strings table name from %{public}@ to %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updating receiver's localized skip control label from %{public}@ to %{public}@ for locale %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updating resolved end time for last current event %{public}@ from %f to primary resumption time %f"
+ "<<<< FigPlayerInterstitial >>>> %s: %p: updating skippable state for current event %{public}@ from %d to %d, label updated from %{public}@ to %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: %p:%{public}s event at join;%{public}s flip to primary"
+ "<<<< FigPlayerInterstitial >>>> %s: Active interstitial item %{public}@ does not match current item %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: Discovered zero-item event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: Error %d, %{public}@ reading asset list for event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: Error reading asset list for event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: Error scheduling asset list read for event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: Finish recording playout time for %{public}@; %f contributes to %f"
+ "<<<< FigPlayerInterstitial >>>> %s: Received asset URLs %{public}@ for event %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: Setting playoutLimit on %p index %d of event %{public}s to %f of %f"
+ "<<<< FigPlayerInterstitial >>>> %s: Start recording playout time for %{public}@ at %f"
+ "<<<< FigPlayerInterstitial >>>> %s: [%p] Backing out enqueue of items for interstitial playback: %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: [%p]/%p Enqueued items for interstitial playback: %{public}@"
+ "<<<< FigPlayerInterstitial >>>> %s: cancel %{public}swith resumptionOffset %f: %{public}@"
+ "<<<< FigPlayerOverlap >>>> %s: [%p|%{public}s] failed remove item from sub-player, err = %d"
+ "<<<< FigStreamPlayer >>>> %s: <%p|%{public}s> Posting seek completion for %d current seek ID %d reason %{public}s postSeekPosition %f"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: %{public}s (%d): Finished video sync at now=%g; startTime=%g, sync frame pts=%g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: %{public}s selected media %@"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Attempt to %{public}s"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Issued PlaybackStalled event with err %d: Reason %d, SeekPending %{public}s, now %f, lastSeekTimeSet %f, Syncing %{public}s, VarRank %d, AudioOnly %{public}s, lastSwitch(fromVariantRank %d, toVariantRank %d, direction %d, switchReason %d, TimeSinceSwitchEndTime %lld), nextMoreFireTime %.3f, nextMorenextTime %.3f"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: No one is waiting for track %d, skipping playResourceReleased notification (nextTrackIsWaitingForResource=%{public}s)"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Not applying rate %f to tracks as %{public}s"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Seek to date %{public}@ %{public}s. domainStart = %1.5g, cachedDatePumpTime = %1.5g, err = %d"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: initialTimeOffset={%lld/%d=%1.3f},initialTimeOffsetIsPrecise=%{public}s,pItem->initialTimeOffset={%lld/%d=%1.3f},pItem->preciseSeekTime={%lld/%d=%1.3f},pItem->dateSought=%@,pItem->initialEstimatedDate=%@,preciseOffset=%@"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: new mebx %{public}s track manifoldTrackID %d - identifiers: %{private}@"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: setting %{public}s per player role "
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: substream %d duration %f bytes %zu. %{public}s allowance of %zu. %{public}s limit of %zu"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d has finished rendering, starting to render track %d, do%{public}s crossfade"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d start time is %g, gets discontinuityOffset %g from track %d, first sample is %f, raw: %f %{public}s"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] Waiting for startup tasks for seek to %.3f seekID %d playbackState %{public}s"
+ "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: (%d): will %{public}scommit to gapless transition to next item <%p|%{public}s>]"
+ "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: Highest %{public}s Alternate\n%@ "
+ "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: [AudioFormat %c%c%c%c is %{public}s decodable] [AudioChannels %d] [Spatialization Eligible %{public}s] [Client permits multi: %{public}s, stereo: %{public}s] [Spatialization %{public}s] [StereoSpatialization %{public}s] [Rendition %@] [SampleRate %d] [BitDepth %d] [Immersive rendering %{public}s]"
+ "<private url>"
+ "<private urls>"
+ "FASBFIK_BossCallbackID"
+ "FBP_HasDates"
+ "LatestCallbackID"
+ "fpiCurrentEventChangeEventKey"
+ "item=%{public}s, itemRef=%llu"
- "<<<< FigBufferedAirPlayRP >>>> %s: [%p] %{public}s Clamping stale oldItemEndTimebaseTime %1.3f up to old timebase current time %1.3f (seek-to-end transition)"
- "<<<< FigItemIntegratedTimeline >>>> %s: %@"
- "<<<< FigItemIntegratedTimeline >>>> %s: %p: %s, can proceed to post SnapshotOutOfSync notifications"
- "<<<< FigItemIntegratedTimeline >>>> %s: %p: Posting integrated timeline seek %s notification with payload %@"
- "<<<< FigItemIntegratedTimeline >>>> %s: %p: dispatching seek to target time %1.5g from %1.5g, source time %1.5g, source segment %@, schedule %@, minSnapTime %1.5g, maxSnapTime %1.5g, seekID %d"
- "<<<< FigItemIntegratedTimeline >>>> %s: %p: primary %s ready for inspection%s"
- "<<<< FigPlayerInterstitial >>>> %s: %f in %p is%s between %f and %f"
- "<<<< FigPlayerInterstitial >>>> %s: %p no matchingScheduleID in schedules for %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: %s current event %@, payload event %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Adding new event for %s item wrapper %p at %s: %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: AirPlay is %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Excluding scheduled event %s; starts past schedule end"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Merging and replacing event for %s item wrapper %p at %s: %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Removing no-longer-current event %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Removing no-longer-current item %p / %@ "
- "<<<< FigPlayerInterstitial >>>> %s: %p: Schedule notification %@ payload %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Setting scheduled event %s playoutLimit to %f"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Time jump-back from %f to %f, once=%d;%s reconsider event %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Time jump-back from %f to %f, once=%d;%s reconsider schedule %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: Time jump-back from %f to %f, removed scheduled event %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: asset %ld in event %@ doesn't have a duration even though it's current"
- "<<<< FigPlayerInterstitial >>>> %s: %p: can buffer; need to make item(s) for %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: cancelling current event %@ with reason %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: clearing intended current item moment %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: clearing state for seek ID %d into event %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: could not find an event at %s after resolving schedule %@, cancel initiated seekID %d"
- "<<<< FigPlayerInterstitial >>>> %s: %p: current moment %s, nextMoment %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: dequeuing %@ from interstitialPlayer %p"
- "<<<< FigPlayerInterstitial >>>> %s: %p: discovered and populating abutting event %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: encountered dummy item for event %@, itemIndex %ld; skipping this for projected duration"
- "<<<< FigPlayerInterstitial >>>> %s: %p: enqueued %@ for event %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: established intended event to seek into - id %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: event %@ - seekTime %f past duration - cancel initiated seekID %d"
- "<<<< FigPlayerInterstitial >>>> %s: %p: event %@ was not immediately established, cancel initiated seekID %d"
- "<<<< FigPlayerInterstitial >>>> %s: %p: event %@ was removed while seekID %d was still pending, cancelling the seek"
- "<<<< FigPlayerInterstitial >>>> %s: %p: eventIndex %d itemIndex %d: removedItem %p, tracked item %p %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: eventItem %@ does not match interstitialPlayer item %@!"
- "<<<< FigPlayerInterstitial >>>> %s: %p: eventItem %d %@ not on interstitialPlayer queue! Playback lost?"
- "<<<< FigPlayerInterstitial >>>> %s: %p: found preloaded response for %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: got %@ from %p, payload %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: hopping current departure moment from %s to %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: hopping nextMoment from %s to %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: hopping snappedNextMoment from %s to %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: initiating seek into event ID %@ at time %1.5g, minSnapTime %1.5g, maxSnapTime %1.5g, seekID %d, flags %d"
- "<<<< FigPlayerInterstitial >>>> %s: %p: interstitial event %@ did finish, playedOutTime %f, didPlayEntireEvent %d"
- "<<<< FigPlayerInterstitial >>>> %s: %p: interstitial event %@ was unscheduled with err %d"
- "<<<< FigPlayerInterstitial >>>> %s: %p: jump over current event at %s to %s; remove %d items"
- "<<<< FigPlayerInterstitial >>>> %s: %p: limited preload %@: [%f(+%f).. %f(-%f))]-> %f%s, now=%f :%f %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: nextMoment %s appears to have snapped to %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: observed %@ for primary item wrapper %p that isn't engaged."
- "<<<< FigPlayerInterstitial >>>> %s: %p: observed all items failed for event %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: observed an end time change while postroll was current, updating nextMoment from %s to %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: observing seek out of event ID %@, waiting on primary seekID %d to finish before doing anything else"
- "<<<< FigPlayerInterstitial >>>> %s: %p: posting initiated seek %s notification for seek ID %d"
- "<<<< FigPlayerInterstitial >>>> %s: %p: reconfigured preload for %@ to start at %@ (%f), trigger at +%f"
- "<<<< FigPlayerInterstitial >>>> %s: %p: removing current event ID %@ up to the intended event to seek into (%@)"
- "<<<< FigPlayerInterstitial >>>> %s: %p: removing event %@ for unengaged item wrapper %p"
- "<<<< FigPlayerInterstitial >>>> %s: %p: removing event ID %@ at same moment but before the intended event to seek into (%@)"
- "<<<< FigPlayerInterstitial >>>> %s: %p: removing event ID %@ from past events"
- "<<<< FigPlayerInterstitial >>>> %s: %p: removing%s event %@ - %@%s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: resumption seek ID %d %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: scheduled interstitial flip interrupted by timebase %s! (rate %f, time %f)"
- "<<<< FigPlayerInterstitial >>>> %s: %p: scheduled liveBufferTimer for %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: scheduling timer for event %@ to become %s to be skipped at event offset %f, item offset %f"
- "<<<< FigPlayerInterstitial >>>> %s: %p: setting cached asset list response data for %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: setting cached schedule response data for %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: setting intended current item moment to %s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: setting internal playout limit %f on %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: setting preloaded cached asset list response data for %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: skip timer fired for event %@ to become %s, prior state %d"
- "<<<< FigPlayerInterstitial >>>> %s: %p: skippable state for event %@ changed from %d to %d - posting notification and informing interstitial player"
- "<<<< FigPlayerInterstitial >>>> %s: %p: sorted eventsInAddOrder to %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: sortedEventsInAddOrder index for event %@ was not found"
- "<<<< FigPlayerInterstitial >>>> %s: %p: stopping item %p at time %1.5g%s"
- "<<<< FigPlayerInterstitial >>>> %s: %p: transfer playback %s primary player %p %s interstitial player %p"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updated eventsInAddOrder from previously cached events to %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updating coordinationMediaSelectionCriteria from %@ to %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updating host's localized skip control label from %@ to %@ for locale %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updating interstitial player from %@ to %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updating localized strings bundle from %@ to %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updating localized strings table name from %@ to %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updating receiver's localized skip control label from %@ to %@ for locale %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updating resolved end time for last current event %@ from %f to primary resumption time %f"
- "<<<< FigPlayerInterstitial >>>> %s: %p: updating skippable state for current event %@ from %d to %d, label updated from %@ to %@"
- "<<<< FigPlayerInterstitial >>>> %s: %p:%s event at join;%s flip to primary"
- "<<<< FigPlayerInterstitial >>>> %s: Active interstitial item %@ does not match current item %@"
- "<<<< FigPlayerInterstitial >>>> %s: Discovered zero-item event %@"
- "<<<< FigPlayerInterstitial >>>> %s: Error %d, %@ reading asset list for event %@"
- "<<<< FigPlayerInterstitial >>>> %s: Error reading asset list for event %@"
- "<<<< FigPlayerInterstitial >>>> %s: Error scheduling asset list read for event %@"
- "<<<< FigPlayerInterstitial >>>> %s: Finish recording playout time for %@; %f contributes to %f"
- "<<<< FigPlayerInterstitial >>>> %s: Received asset URLs %@ for event %@"
- "<<<< FigPlayerInterstitial >>>> %s: Setting playoutLimit on %p index %d of event %s to %f of %f"
- "<<<< FigPlayerInterstitial >>>> %s: Start recording playout time for %@ at %f"
- "<<<< FigPlayerInterstitial >>>> %s: [%p] Backing out enqueue of items for interstitial playback: %@"
- "<<<< FigPlayerInterstitial >>>> %s: [%p]/%p Enqueued items for interstitial playback: %@"
- "<<<< FigPlayerInterstitial >>>> %s: cancel %swith resumptionOffset %f: %@"
- "<<<< FigPlayerOverlap >>>> %s: %p failed remove item from sub-player, err = %d"
- "<<<< FigStreamPlayer >>>> %s: <%p|%{public}s> Posting seek completion for %d current seek ID %d reason %s postSeekPosition %f"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: %s (%d): Finished video sync at now=%g; startTime=%g, sync frame pts=%g"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: %s selected media %@"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Attempt to %s"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Issued PlaybackStalled event with err %d: Reason %d, SeekPending %s, now %f, lastSeekTimeSet %f, Syncing %s, VarRank %d, AudioOnly %s, lastSwitch(fromVariantRank %d, toVariantRank %d, direction %d, switchReason %d, TimeSinceSwitchEndTime %lld), nextMoreFireTime %.3f, nextMorenextTime %.3f"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: No one is waiting for track %d, skipping playResourceReleased notification (nextTrackIsWaitingForResource=%s)"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Not applying rate %f to tracks as %s"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Seek to date %{public}@ %s. domainStart = %1.5g, cachedDatePumpTime = %1.5g, err = %d"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: initialTimeOffset={%lld/%d=%1.3f},initialTimeOffsetIsPrecise=%s,pItem->initialTimeOffset={%lld/%d=%1.3f},pItem->preciseSeekTime={%lld/%d=%1.3f},pItem->dateSought=%@,pItem->initialEstimatedDate=%@,preciseOffset=%@"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: new mebx %s track manifoldTrackID %d - identifiers: %{private}@"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: setting %s per player role "
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: substream %d duration %f bytes %zu. %s allowance of %zu. %s limit of %zu"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d has finished rendering, starting to render track %d, do%s crossfade"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d start time is %g, gets discontinuityOffset %g from track %d, first sample is %f, raw: %f %s"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] Waiting for startup tasks for seek to %.3f seekID %d playbackState %s"
- "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: (%d): will %scommit to gapless transition to next item <%p|%{public}s>]"
- "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: Highest %s Alternate\n%@ "
- "<<<< FigStreamPlayer >>>> %s: [QE Critical][%p|%{public}s]: <%p|%{public}s>: [AudioFormat %c%c%c%c is %s decodable] [AudioChannels %d] [Spatialization Eligible %s] [Client permits multi: %s, stereo: %s] [Spatialization %s] [StereoSpatialization %s] [Rendition %@] [SampleRate %d] [BitDepth %d] [Immersive rendering %s]"
```
