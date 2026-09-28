## WebCore

> `/System/Library/PrivateFrameworks/WebCore.framework/WebCore`

```diff

-625.1.29.10.29
-  __TEXT.__text: 0x36e73e0
+625.1.29.10.33
+  __TEXT.__text: 0x36e742c
   __TEXT.__objc_methlist: 0x5ad4
   __TEXT.__getClass_cstr: 0x1290
   __TEXT.__dlsym_cstr: 0x7628
Functions:
~ __ZN7WebCore16HTMLMediaElement8seekTaskEv : 9748 -> 9760
~ __ZN7WebCore16HTMLMediaElement12playInternalEv -> __ZNK7WebCore16HTMLMediaElement13endedPlaybackEv : 1120 -> 564
~ __ZThn168_NK7WebCore16HTMLMediaElement10readyStateEv -> __ZN7WebCore16HTMLMediaElement12playInternalEv : 8 -> 1120
~ __ZNK7WebCore16HTMLMediaElement27mediaSessionGroupIdentifierEv -> __ZThn168_NK7WebCore16HTMLMediaElement10readyStateEv : 136 -> 8
~ __ZThn168_NK7WebCore16HTMLMediaElement8hasAudioEv -> __ZThn176_NK7WebCore16HTMLMediaElement27mediaSessionGroupIdentifierEv : 8 -> 136
~ __ZNK7WebCore16HTMLMediaElement7seekingEv -> __ZThn168_NK7WebCore16HTMLMediaElement8hasAudioEv : 12 -> 8
~ __ZThn168_NK7WebCore16HTMLMediaElement11currentTimeEv -> __ZNK7WebCore16HTMLMediaElement7seekingEv : 60 -> 12
~ __ZN7WebCore16HTMLMediaElement14setCurrentTimeEd -> __ZThn168_NK7WebCore16HTMLMediaElement11currentTimeEv : 80 -> 60
~ __ZN7WebCore16HTMLMediaElement25setCurrentTimeForBindingsEd -> __ZThn168_N7WebCore16HTMLMediaElement14setCurrentTimeEd : 196 -> 80
~ __ZThn168_NK7WebCore16HTMLMediaElement8durationEv -> __ZN7WebCore16HTMLMediaElement25setCurrentTimeForBindingsEd : 60 -> 196
~ __ZThn168_NK7WebCore16HTMLMediaElement6pausedEv -> __ZThn168_NK7WebCore16HTMLMediaElement8durationEv : 12 -> 60
~ __ZNK7WebCore16HTMLMediaElement19defaultPlaybackRateEv -> __ZThn168_NK7WebCore16HTMLMediaElement6pausedEv : 24 -> 12
~ __ZN7WebCore16HTMLMediaElement22setDefaultPlaybackRateEd -> __ZThn168_NK7WebCore16HTMLMediaElement19defaultPlaybackRateEv : 572 -> 24
~ __ZThn168_N7WebCore16HTMLMediaElement22setDefaultPlaybackRateEd -> __ZN7WebCore16HTMLMediaElement22setDefaultPlaybackRateEd : 8 -> 572
~ __ZNK7WebCore16HTMLMediaElement21effectivePlaybackRateEv -> __ZThn168_N7WebCore16HTMLMediaElement22setDefaultPlaybackRateEd : 136 -> 8
~ __ZNK7WebCore16HTMLMediaElement12playbackRateEv -> __ZNK7WebCore16HTMLMediaElement21effectivePlaybackRateEv : 24 -> 136
~ __ZN7WebCore16HTMLMediaElement15setPlaybackRateEd -> __ZThn168_NK7WebCore16HTMLMediaElement12playbackRateEv : 3544 -> 24
~ __ZThn168_N7WebCore16HTMLMediaElement15setPlaybackRateEd -> __ZN7WebCore16HTMLMediaElement15setPlaybackRateEd : 8 -> 3544
~ __ZN7WebCore16HTMLMediaElement18updatePlaybackRateEv -> __ZThn168_N7WebCore16HTMLMediaElement15setPlaybackRateEd : 980 -> 8
~ __ZNK7WebCore16HTMLMediaElement14preservesPitchEv -> __ZN7WebCore16HTMLMediaElement18updatePlaybackRateEv : 8 -> 980
~ __ZN7WebCore16HTMLMediaElement17setPreservesPitchEb -> __ZNK7WebCore16HTMLMediaElement14preservesPitchEv : 624 -> 8
~ __ZNK7WebCore16HTMLMediaElement22mediaPlayerCurrentTimeEv -> __ZN7WebCore16HTMLMediaElement17setPreservesPitchEb : 480 -> 624
~ __ZNK7WebCore16HTMLMediaElement5endedEv -> __ZNK7WebCore16HTMLMediaElement22mediaPlayerCurrentTimeEv : 576 -> 480
~ __ZNK7WebCore16HTMLMediaElement13endedPlaybackEv -> __ZNK7WebCore16HTMLMediaElement5endedEv : 564 -> 576
~ __ZN7WebCore18ManagedMediaSource20monitorSourceBuffersEv : 1228 -> 1292
~ __ZN7WebCore19ManagedSourceBuffer15operatorNewSlowEm -> __ZNK7WebCore11MediaSource8durationEv : 16 -> 360
~ __ZN7WebCore19ManagedSourceBufferD1Ev -> __ZN7WebCore19ManagedSourceBuffer15operatorNewSlowEm : 4 -> 16
~ __ZThn40_N7WebCore19ManagedSourceBufferD1Ev -> __ZN7WebCore19ManagedSourceBufferD1Ev : 8 -> 4
~ __ZN7WebCore19ManagedSourceBufferD0Ev -> __ZThn112_N7WebCore19ManagedSourceBufferD1Ev : 28 -> 8
~ __ZThn40_N7WebCore19ManagedSourceBufferD0Ev -> __ZN7WebCore19ManagedSourceBufferD0Ev : 32 -> 28
~ __ZN7WebCore11MediaSource15operatorNewSlowEm -> __ZThn112_N7WebCore19ManagedSourceBufferD0Ev : 12 -> 32
~ __ZN7WebCore11MediaSource17detachFromElementEv -> __ZN7WebCore11MediaSource15operatorNewSlowEm : 1668 -> 12
~ __ZN7WebCore11MediaSourceD1Ev -> __ZN7WebCore11MediaSource17detachFromElementEv : 4 -> 1668
~ __ZThn40_N7WebCore11MediaSourceD1Ev -> __ZN7WebCore11MediaSourceD1Ev : 8 -> 4
~ __ZN7WebCore11MediaSourceD0Ev -> __ZThn80_N7WebCore11MediaSourceD1Ev : 28 -> 8
~ __ZThn40_N7WebCore11MediaSourceD0Ev -> __ZN7WebCore11MediaSourceD0Ev : 32 -> 28
~ __ZN7WebCore11MediaSource13didLogMessageERK13WTFLogChannel11WTFLogLevelNSt3__18optionalI14WTFLogLocationEEON3WTF6VectorINS9_12JSONLogValueELm0ENS9_15CrashOnOverflowELm16ENS9_10FastMallocEEE -> __ZThn80_N7WebCore11MediaSourceD0Ev : 4 -> 32
~ __ZN7WebCore11MediaSource4openEv -> __ZThn80_N7WebCore11MediaSource13didLogMessageERK13WTFLogChannel11WTFLogLevelNSt3__18optionalI14WTFLogLocationEEON3WTF6VectorINS9_12JSONLogValueELm0ENS9_15CrashOnOverflowELm16ENS9_10FastMallocEEE : 1140 -> 4
~ __ZN7WebCore11MediaSource13setReadyStateENS_21MediaSourceReadyStateE -> __ZN7WebCore11MediaSource4openEv : 340 -> 1140
~ __ZN7WebCore11MediaSource18openIfDeferredOpenEv -> __ZN7WebCore11MediaSource13setReadyStateENS_21MediaSourceReadyStateE : 592 -> 340
~ __ZNK7WebCore11MediaSource8durationEv -> __ZN7WebCore11MediaSource18openIfDeferredOpenEv : 360 -> 592
```
