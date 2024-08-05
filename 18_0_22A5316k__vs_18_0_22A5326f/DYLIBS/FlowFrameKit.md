## FlowFrameKit

> `/System/Library/PrivateFrameworks/FlowFrameKit.framework/FlowFrameKit`

```diff

-3400.148.1.0.0
-  __TEXT.__text: 0xf428
-  __TEXT.__auth_stubs: 0xa80
+3400.155.1.0.0
+  __TEXT.__text: 0xf33c
+  __TEXT.__auth_stubs: 0xa90
   __TEXT.__const: 0x9b8
   __TEXT.__cstring: 0x847
   __TEXT.__swift5_typeref: 0x3d9

   __TEXT.__eh_frame: 0x1c8
   __TEXT.__objc_methname: 0x11
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0xb0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__auth_ptr: 0x188
   __AUTH_CONST.__const: 0xce0
   __AUTH_CONST.__objc_const: 0x538

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 406
-  Symbols:   112
-  CStrings:  0
+  Symbols:   121
+  CStrings:  54
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_release_x25
CStrings:
+ "__ZN7WebCore13MediaStrategy21enableMockMediaSourceEv"
+ "__ZN7WebCore13MediaStrategy24addMockMediaSourceEngineEv"
+ "__ZN7WebCore13MediaStrategyD2Ev"
+ "__ZN7WebCore13ScrollingTree15commitTreeStateEONSt3__110unique_ptrINS_18ScrollingStateTreeENS1_14default_deleteIS3_EEEENS1_8optionalIN3WTF23ObjectIdentifierGenericINS_33LayerHostingContextIdentifierTypeENS9_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEE"
+ "__ZN7WebCore13ScrollingTree16clearLatchedNodeEv"
+ "__ZN7WebCore13ScrollingTree16handleWheelEventERKNS_18PlatformWheelEventEN3WTF9OptionSetINS_25WheelEventProcessingStepsEEE"
+ "__ZN7WebCore13ScrollingTree19scrollingTreeAsTextEN3WTF9OptionSetINS_32ScrollingStateTreeAsTextBehaviorEEE"
+ "__ZN7WebCore13ScrollingTree21scrollPinningBehaviorEv"
+ "__ZN7WebCore13ScrollingTree21scrollingNodeForPointENS_10FloatPointE"
+ "__ZN7WebCore13ScrollingTree21viewWillEndLiveResizeEv"
+ "__ZN7WebCore13ScrollingTree21willProcessWheelEventEv"
+ "__ZN7WebCore13ScrollingTree22addPendingScrollUpdateEONS_12ScrollUpdateE"
+ "__ZN7WebCore13ScrollingTree23hasPendingScrollUpdatesEv"
+ "__ZN7WebCore13ScrollingTree23viewWillStartLiveResizeEv"
+ "__ZN7WebCore13ScrollingTree25eventTrackingTypeForPointENS_29EventTrackingRegionsEventTypeENS_8IntPointE"
+ "__ZN7WebCore13ScrollingTree25frameIDForScrollingNodeIDENS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEE"
+ "__ZN7WebCore13ScrollingTree31willWheelEventStartSwipeGestureERKNS_18PlatformWheelEventE"
+ "__ZN7WebCore13ScrollingTree33setRubberBandingInProgressForNodeENS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEEb"
+ "__ZN7WebCore13ScrollingTree34clearNodesWithUserScrollInProgressEv"
+ "__ZN7WebCore13ScrollingTree44setClientAllowedMainFrameRubberBandableEdgesENS_9RectEdgesIbEE"
+ "__ZN7WebCore16MIMETypeRegistry13isUSDMIMETypeERKN3WTF6StringE"
+ "__ZN7WebCore16MIMETypeRegistry14isTextMIMETypeERKN3WTF6StringE"
+ "__ZN7WebCore16MIMETypeRegistry16allowedMIMETypesERKN3WTF6VectorINS1_6StringELm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEES8_"
+ "__ZN7WebCore16MIMETypeRegistry20isWebArchiveMIMETypeERKN3WTF6StringE"
+ "__ZN7WebCore16MIMETypeRegistry23isSupportedJSONMIMETypeERKN3WTF6StringE"
+ "__ZN7WebCore16MIMETypeRegistry23supportedMediaMIMETypesEv"
+ "__ZN7WebCore16MIMETypeRegistry24isSupportedImageMIMETypeERKN3WTF6StringE"
+ "__ZN7WebCore16MIMETypeRegistry24isSupportedMediaMIMETypeERKN3WTF6StringE"
+ "__ZN7WebCore16MIMETypeRegistry24isSupportedModelMIMETypeERKN3WTF6StringE"
+ "__ZN7WebCore16MIMETypeRegistry24unsupportedTextMIMETypesEv"
+ "__ZN7WebCore16MIMETypeRegistry27isSupportedNonImageMIMETypeERKN3WTF6StringE"
+ "__ZN7WebCore16MIMETypeRegistry30appendFileExtensionIfNecessaryERKN3WTF6StringES4_"
+ "__ZN7WebCore17NowPlayingManager12removeClientERNS_23NowPlayingManagerClientE"
+ "__ZN7WebCore17NowPlayingManager17setNowPlayingInfoERKNS_14NowPlayingInfoE"
+ "__ZN7WebCore17NowPlayingManager18setSupportsSeekingEb"
+ "__ZN7WebCore17NowPlayingManager26setSupportedRemoteCommandsERKN3WTF7HashSetINS_44PlatformMediaSessionRemoteControlCommandTypeENS1_7IntHashIS3_EENS1_20StrongEnumHashTraitsIS3_EENS1_15HashTableTraitsEEE"
+ "__ZN7WebCore17NowPlayingManager30didReceiveRemoteControlCommandENS_44PlatformMediaSessionRemoteControlCommandTypeERKNS_41PlatformMediaSessionRemoteCommandArgumentE"
+ "__ZN7WebCore17NowPlayingManager9addClientERNS_23NowPlayingManagerClientE"
+ "__ZN7WebCore17NowPlayingManagerC1Ev"
+ "__ZN7WebCore17NowPlayingManagerD2Ev"
+ "__ZN7WebCore20PasteboardCustomData5EntryC1EOS1_"
+ "__ZN7WebCore20PasteboardCustomData5EntryC1ERKN3WTF6StringES5_RKNSt3__17variantIJS3_NS2_3RefINS_12SharedBufferENS2_12RawPtrTraitsIS9_EENS2_21DefaultRefDerefTraitsIS9_EEEEEEE"
+ "__ZN7WebCore20PasteboardCustomDataC1EON3WTF6StringEONS1_6VectorINS0_5EntryELm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEE"
+ "__ZN7WebCore20PasteboardCustomDataC1EOS0_"
+ "__ZN7WebCore20PasteboardCustomDataD1Ev"
+ "__ZNK7WebCore13MediaStrategy22mockMediaSourceEnabledEv"
+ "__ZNK7WebCore13MediaStrategy23createNowPlayingManagerEv"
+ "__ZNK7WebCore13MediaStrategy31hasThreadSafeMediaSourceSupportEv"
+ "__ZNK7WebCore13ScrollingTree14layoutViewportEv"
+ "__ZNK7WebCore13ScrollingTree23mainFrameScrollPositionEv"
+ "__ZNK7WebCore13ScrollingTree32eventListenerRegionTypesForPointENS_10FloatPointE"
+ "__ZNK7WebCore13ScrollingTree9nodeForIDENS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEE"
+ "neWheelEventProcessingERKNS_18PlatformWheelEventE"
+ "ypeRegistry23supportedImageMIMETypesEv"

```
