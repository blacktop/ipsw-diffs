## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-3285.11.1.4.0
-  __TEXT.__text: 0x1b8e50
+3290.3.2.0.0
+  __TEXT.__text: 0x1b9638
   __TEXT.__auth_stubs: 0x34a0
   __TEXT.__objc_methlist: 0x5d4
   __TEXT.__const: 0x1b38
-  __TEXT.__cstring: 0x1f038
-  __TEXT.__oslogstring: 0x64a6
+  __TEXT.__cstring: 0x1f10a
+  __TEXT.__oslogstring: 0x6590
   __TEXT.__gcc_except_tab: 0x1a0
   __TEXT.__dlopen_cstrs: 0x190
-  __TEXT.__unwind_info: 0x4c10
+  __TEXT.__unwind_info: 0x4c08
   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_classname: 0x104
   __TEXT.__objc_methname: 0x18fc
   __TEXT.__objc_methtype: 0xbc9
   __TEXT.__objc_stubs: 0x1680
   __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0xa368
+  __DATA_CONST.__const: 0xa388
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0x1a60
   __AUTH_CONST.__const: 0x6120
-  __AUTH_CONST.__cfstring: 0x17940
+  __AUTH_CONST.__cfstring: 0x179c0
   __AUTH_CONST.__objc_const: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x78

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 80D58D43-1F81-3320-B8D5-934F966E73A2
-  Functions: 9641
-  Symbols:   22689
-  CStrings:  8676
+  UUID: 82393AFF-93CB-3E07-8CCE-4D59C22A93A1
+  Functions: 9653
+  Symbols:   22716
+  CStrings:  8689
 
Symbols:
+ _FigNetworkHistoryRequestReceivedBytesWithFlags
+ _FigNetworkHistoryRequestUpdateActiveTime
+ _FigTimelineStateDictionaryGetStateVideoTargetSynchronizationIdentifier
+ _fnh_recordNetworkHistoryRequestReceivedBytes
+ _fnh_setRequestActiveTimestampCommand
+ _fnh_setRequestActiveTimestampCommand.cold.1
+ _kFigEndpointActivateOptionKey_NumberOfEndpoints
+ _kFigStreamPlaylistParserMsgParam_SkippedSegmentCount
+ _kFigTimelineCoordinatorTimeJumpOptionKey_VideoTargetSynchronizationIdentifier
+ _kFigTimelineCoordinatorTimelineStateKey_VideoTargetSynchronizationIdentifier
CStrings:
+ " vtsid:%@"
+ "<<<< FigTimelineCoordinator >>>> %s: %@ Handling participant state %{public}@"
+ "<<<< FigTimelineCoordinator >>>> %s: %@ Handling timeline state %{public}@"
+ "<<<< FigTimelineCoordinator >>>> %s: %@ Received and handling state <%{public}@>"
+ "NumberOfEndpoints"
+ "SkippedSegmentCount"
+ "VideoTargetSynchronizationIdentifier"
+ "figTimelineCoordinator_applyRemoteTimelineStateOnQueue"
+ "figTimelineCoordinator_handleUpdatedParticipantStateFromMediumOnQueue"

```
