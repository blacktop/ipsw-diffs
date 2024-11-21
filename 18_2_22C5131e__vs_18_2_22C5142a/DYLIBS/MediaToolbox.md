## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3185.17.1.0.0
-  __TEXT.__text: 0xa95b08
+3185.18.1.3.0
+  __TEXT.__text: 0xa97ab8
   __TEXT.__auth_stubs: 0xba30
   __TEXT.__objc_methlist: 0x1d00
-  __TEXT.__cstring: 0x5d80c
+  __TEXT.__cstring: 0x5db33
   __TEXT.__const: 0x54c40
-  __TEXT.__oslogstring: 0x41d40
+  __TEXT.__oslogstring: 0x42698
   __TEXT.__ustring: 0x1f8
   __TEXT.__gcc_except_tab: 0xce4
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__unwind_info: 0x11108
+  __TEXT.__unwind_info: 0x11120
   __TEXT.__eh_frame: 0x4448
   __TEXT.__objc_classname: 0x812
   __TEXT.__objc_methname: 0x5ddb
   __TEXT.__objc_methtype: 0x2492
   __TEXT.__objc_stubs: 0x5760
-  __DATA_CONST.__got: 0x3518
+  __DATA_CONST.__got: 0x3520
   __DATA_CONST.__const: 0x217c0
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_protolist: 0x58

   __AUTH_CONST.__auth_got: 0x5d30
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__const: 0x3e158
-  __AUTH_CONST.__cfstring: 0x4cd60
+  __AUTH_CONST.__cfstring: 0x4cda0
   __AUTH_CONST.__objc_const: 0x5440
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10

   __DATA.__objc_ivar: 0x2d0
   __DATA.__data: 0x18410
   __DATA.__bss: 0x37e8
-  __DATA.__common: 0x1979
+  __DATA.__common: 0x1999
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x240
   __DATA_DIRTY.__bss: 0x3a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 23323
-  Symbols:   33472
-  CStrings:  19145
+  Functions: 23324
+  Symbols:   33474
+  CStrings:  19192
 
Symbols:
+ _FigMediaProcessorCreateForVideoCompressionWithFormatWriter2
+ _kFigEndpointStreamProperty_Mute
CStrings:
+ "<<<< EditMentor >>>> %s: (%p %{public}@: order %p (%{public}@))"
+ "<<<< EditMentor >>>> %s: (%p %{public}@: start %1.3f, end %1.3f, %{public}s, order %p (%{public}@))"
+ "<<<< EditMentor >>>> %s: (%p %{public}@: target %1.3f, %{public}s, order %p (%{public}@))"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@:"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: %{public}s childOrder %p (%{public}@), currentChildOrder %p (%{public}@); parentOrder %p (%{public}@)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: Child mentor PrerollComplete, %{public}s, but child order %p (%{public}@) is STALE"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: Looping forever, and previous edit generated no samples.  Consider this order completed, with no permanent emptiness -- to avoid mentor busy looping. "
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: Posted PrerollComplete (synthetic), %{public}s, parentOrder %p (%{public}@) was %{public}s"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: PrerollComplete, %{public}s, parentOrder %p (%{public}@)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: StoppingDueToCompletion parentOrder %p (%{public}@)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: StoppingDueToError, mentor->samplesWereGenerated = %{public}s"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: child order completed before reaching preroll level. childOrder %p (%{public}@)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: childOrder %p %{public}@, samplesWereGeneratedByThisChild = %{public}s, thisChildLastsForever = %{public}s"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: mentor->samplesWereGenerated = %{public}s, lastsForever = %{public}s, parentOrder = %p (%{public}@)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: now %p (%{public}@)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: now waiting for last edit to grow"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: order mismatch (%p), cannot remap sample buffer %p"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: order mismatch (%p), cannot remap time interval"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: parent order was %{public}s. Child order now %p (%{public}@)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: synthesising empty edit after end of edit list (beginning of reverse playback)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: synthesising empty edit after end of edit list (end of %{public}s playback)"
+ "<<<< EditMentor >>>> %s: (%p) %{public}@: synthesising empty edit before beginning of edit list (beginning of forward playback)"
+ "EditMentorSetModeToDoNothing"
+ "EditMentorSetModeToEmptyEdit"
+ "EditMentorSetModeToForwardPlayback"
+ "EditMentorSetModeToReversePlayback"
+ "EditMentorSetModeToScrub"
+ "Unrecognized attribute value in VIDEO-LAYOUT"
+ "default:preserve"
+ "editMentorAdvanceToNextEdit"
+ "editMentorChildMentorPrerollComplete"
+ "editMentorChildMentorStoppedDueToCompletion"
+ "editMentorChildMentorStoppedDueToError"
+ "editMentorChildOrderRefIsCurrent_RetainParentOrder"
+ "editMentorPostOrderCompletionNotification"
+ "editMentorPostSyntheticPrerollCompleteNotification"
+ "editMentorRemapSampleBufferTiming"
+ "editMentorRemapTimeInterval"
+ "editMentorSelectFirstEditSegmentForParentRange"
+ "editMentorSelectNextEditSegmentForParentRange"
+ "editMentorStartNewChildOrder"
+ "editMentorStartNewParentOrder"
+ "editmentor_trace"
+ "remoteXPCPlayer_updateAirPlayVideoHostLayer"
+ "repurpose"
+ "reverse"

```
