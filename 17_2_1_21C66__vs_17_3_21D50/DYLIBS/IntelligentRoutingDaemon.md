## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon`

```diff

-64.0.0.0.0
-  __TEXT.__text: 0x66624
+66.0.1.0.0
+  __TEXT.__text: 0x66f2c
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x64b0
-  __TEXT.__oslogstring: 0x5f57
-  __TEXT.__cstring: 0x7d30
+  __TEXT.__objc_methlist: 0x6578
+  __TEXT.__oslogstring: 0x5eab
+  __TEXT.__cstring: 0x8810
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x11d8
-  __TEXT.__unwind_info: 0x170c
-  __TEXT.__objc_classname: 0xe91
-  __TEXT.__objc_methname: 0x14b7f
-  __TEXT.__objc_methtype: 0x1e14
-  __TEXT.__objc_stubs: 0xcc60
+  __TEXT.__gcc_except_tab: 0x120c
+  __TEXT.__unwind_info: 0x1730
+  __TEXT.__objc_classname: 0xe98
+  __TEXT.__objc_methname: 0x14dc7
+  __TEXT.__objc_methtype: 0x1e31
+  __TEXT.__objc_stubs: 0xce00
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x1b70
-  __DATA_CONST.__objc_classlist: 0x410
+  __DATA_CONST.__const: 0x1b48
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa7d8
-  __DATA_CONST.__objc_selrefs: 0x38a8
-  __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__objc_const: 0x3660
-  __AUTH_CONST.__cfstring: 0x5ee0
-  __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__const: 0x5a0
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_const: 0xa7e8
+  __DATA_CONST.__objc_selrefs: 0x3910
+  __DATA_CONST.__objc_arraydata: 0x4c8
+  __AUTH_CONST.__objc_const: 0x3780
+  __AUTH_CONST.__cfstring: 0x6da0
+  __AUTH_CONST.__objc_intobj: 0x2e8
+  __AUTH_CONST.__const: 0x5c0
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x438
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_classrefs: 0x660
-  __DATA.__objc_superrefs: 0x2c8
-  __DATA.__objc_ivar: 0x878
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_classrefs: 0x668
+  __DATA.__objc_superrefs: 0x2d0
+  __DATA.__objc_ivar: 0x884
   __DATA.__data: 0xb40
   __DATA.__bss: 0x3c
   __DATA_DIRTY.__objc_data: 0x1fe0

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2422
-  Symbols:   8801
-  CStrings:  4485
+  Functions: 2437
+  Symbols:   8858
+  CStrings:  4623
 
Symbols:
+ +[IRAnalyticsManager logUiEvent:withService:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:historyEventsContainer:]
+ +[IRCandidateClassificationDetectorSameSpace sameSpaceMiLoScoresForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]
+ +[IRMiLoProvider bitmapFromServiceSuspendedReasonArray:]
+ +[IRPair pairWithFirst:second:]
+ +[IRServicePackageAdapterMedia(IRAnalytics) _temporaryListOfAllowedApps]
+ -[IRCandidateDO(Extensions) containsAirplayTarget]
+ -[IRMiLoProvider miLoServiceSuspendedReasonBitmap]
+ -[IRMiLoProvider setMiLoServiceSuspendedReasonBitmap:]
+ -[IRNodeDO(Extension) isAirplayTarget]
+ -[IRPair .cxx_destruct]
+ -[IRPair first]
+ -[IRPair initWithFirst:second:]
+ -[IRPair second]
+ -[IRServicePackageAdapterAppleTVControl(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]
+ -[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]
+ -[IRStatisticsManager _updateMiLoStatisticsIfNeededWithReason:mode:miloPrediction:]
+ -[IRStatisticsManager _updateModeStatisticsIfNeededWithReason:mode:date:]
+ _OBJC_CLASS_$_IRPair
+ _OBJC_IVAR_$_IRMiLoProvider._miLoServiceSuspendedReasonBitmap
+ _OBJC_IVAR_$_IRPair._first
+ _OBJC_IVAR_$_IRPair._second
+ _OBJC_METACLASS_$_IRPair
+ __OBJC_$_CLASS_METHODS_IRCandidateClassificationDetectorSameSpace
+ __OBJC_$_CLASS_METHODS_IRPair
+ __OBJC_$_CLASS_METHODS_IRServicePackageAdapterMedia(IRAnalytics)
+ __OBJC_$_INSTANCE_METHODS_IRPair
+ __OBJC_$_INSTANCE_VARIABLES_IRPair
+ __OBJC_$_PROP_LIST_IRPair
+ __OBJC_CLASS_RO_$_IRPair
+ __OBJC_METACLASS_RO_$_IRPair
+ ___128+[IRCandidateClassificationDetectorSameSpace sameSpaceMiLoScoresForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]_block_invoke
+ ___128+[IRCandidateClassificationDetectorSameSpace sameSpaceMiLoScoresForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]_block_invoke_2
+ ___128+[IRCandidateClassificationDetectorSameSpace sameSpaceMiLoScoresForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]_block_invoke_3
+ ___189-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]_block_invoke
+ ___189-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]_block_invoke_2
+ ___189-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]_block_invoke_3
+ ___189-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]_block_invoke_4
+ ___189-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]_block_invoke_5
+ ___198-[IRServicePackageAdapterAppleTVControl(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]_block_invoke
+ ___198-[IRServicePackageAdapterAppleTVControl(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:]_block_invoke_2
+ ___50-[IRCandidateDO(Extensions) containsAirplayTarget]_block_invoke
+ ___block_descriptor_88_e8_32s40s48r56r64r72r80r_e33_v32?0"IRHistoryEventDO"8Q16^B24ls32l8r48l8s40l8r56l8r64l8r72l8r80l8
+ ___block_literal_global.14
+ ___block_literal_global.232
+ _objc_msgSend$_temporaryListOfAllowedApps
+ _objc_msgSend$_updateMiLoStatisticsIfNeededWithReason:mode:miloPrediction:
+ _objc_msgSend$_updateModeStatisticsIfNeededWithReason:mode:date:
+ _objc_msgSend$bitmapFromServiceSuspendedReasonArray:
+ _objc_msgSend$containsAirplayTarget
+ _objc_msgSend$first
+ _objc_msgSend$initWithFirst:second:
+ _objc_msgSend$isAirplayTarget
+ _objc_msgSend$logUiEvent:withService:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:historyEventsContainer:
+ _objc_msgSend$miLoServiceSuspendedReasonBitmap
+ _objc_msgSend$pairWithFirst:second:
+ _objc_msgSend$sameSpaceMiLoScoresForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:
+ _objc_msgSend$second
+ _objc_msgSend$setMiLoServiceSuspendedReasonBitmap:
+ _objc_msgSend$uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:
- +[IRAnalyticsManager logUiEvent:withService:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:]
- -[IRServicePackageAdapterAppleTVControl(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:]
- -[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:]
- GCC_except_table15
- ___113-[IRServicePackageAdapterMedia(IRAnalytics) _getGeneralWeeklyAnalyticsWithWeeklyHistory:withCandidatesContainer:]_block_invoke_7
- ___121-[IRCandidateClassificationDetectorSameSpace _isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]_block_invoke
- ___121-[IRCandidateClassificationDetectorSameSpace _isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]_block_invoke_2
- ___121-[IRCandidateClassificationDetectorSameSpace _isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]_block_invoke_3
- ___174-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:]_block_invoke
- ___174-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:]_block_invoke_2
- ___174-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:]_block_invoke_3
- ___174-[IRServicePackageAdapterMedia(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:]_block_invoke_4
- ___183-[IRServicePackageAdapterAppleTVControl(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:]_block_invoke
- ___183-[IRServicePackageAdapterAppleTVControl(IRAnalytics) uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:]_block_invoke_2
- ___block_descriptor_56_e8_32s40r48r_e22_v24?0"IRNodeDO"8^B16lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e33_v32?0"IRHistoryEventDO"8Q16^B24ls32l8r40l8r48l8
- ___block_literal_global.11
- ___block_literal_global.199
- ___block_literal_global.8
- _objc_msgSend$logUiEvent:withService:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:
- _objc_msgSend$uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:
CStrings:
+ "\"1\x13"
+ "@"
+ "@\"NSDictionary\"80@0:8@\"IREventDO\"16@\"NSString\"24@\"IRSystemStateManager\"32@\"IRCandidatesContainerDO\"40@\"NSDictionary\"48@\"IRStatisticsManager\"56@\"IRServiceDO\"64@\"IRHistoryEventsContainerDO\"72"
+ "Cluster"
+ "General_N_airplay_playback_events_Eligible_App_Weekly"
+ "General_N_airplay_playback_events_Milo_Eligible_App_Weekly"
+ "General_N_airplay_playback_events_Milo_Weekly"
+ "IRPair"
+ "T@,R,N,V_first"
+ "T@,R,N,V_second"
+ "Tq,N,V_miLoServiceSuspendedReasonBitmap"
+ "UI_Event_Current_LOI"
+ "UI_Event_MiLo_Suspended_Reasons"
+ "UI_Event_Selected_Candidate_Device_Model_Type"
+ "UI_Event_Selected_Candidate_Is_Airplay_Target"
+ "UI_Event_Selected_Candidate_Same_Space_MiLo_Agg_Score"
+ "UI_Event_Selected_Candidate_Same_Space_MiLo_LSL_Items"
+ "UI_Event_Selected_Candidate_Was_Used_At_Home"
+ "_first"
+ "_miLoServiceSuspendedReasonBitmap"
+ "_second"
+ "_temporaryListOfAllowedApps"
+ "_updateMiLoStatisticsIfNeededWithReason:mode:miloPrediction:"
+ "_updateModeStatisticsIfNeededWithReason:mode:date:"
+ "app.svn.Cheers"
+ "au.com.shiftyjelly.podcasts"
+ "bitmapFromServiceSuspendedReasonArray:"
+ "ch.monstar.ios"
+ "com.abcdigital.abc.videoplayer"
+ "com.amazon.aiv.AIVApp"
+ "com.apple.SoundScapes"
+ "com.apple.TVMovies"
+ "com.apple.TVMusic"
+ "com.apple.TVWatchList"
+ "com.apple.mediaservicesbroker.app"
+ "com.apple.movietrailers"
+ "com.apple.music.classical"
+ "com.apple.podcasts"
+ "com.apple.tv"
+ "com.aspiro.TIDAL"
+ "com.att.tv"
+ "com.audible.iphone"
+ "com.audiomack.iphone"
+ "com.bbc.sounds"
+ "com.bet.betshows"
+ "com.calm.calmapp"
+ "com.canalplusdistrib.mycanal.prod"
+ "com.cbs.canada.app"
+ "com.cbsvideo.app"
+ "com.clearchannel.iheartradio"
+ "com.comcast.cim.x2"
+ "com.cookingchannel.tveverywhere"
+ "com.crunchyroll.iphone"
+ "com.curiosity.curiositystream"
+ "com.cw.fullepisodes.ios"
+ "com.directv.DTViPhone"
+ "com.discovery.mobile.discoveryplus"
+ "com.dishdigital.sling"
+ "com.disney.disneyplus"
+ "com.disney.starplus"
+ "com.espn.ScoreCenter"
+ "com.feelthemusi.musi"
+ "com.firecore.infuse"
+ "com.foodnetwork.tveverywhere"
+ "com.google.ios.youtube"
+ "com.google.ios.youtube.2"
+ "com.google.ios.youtube.S9RFUD6998"
+ "com.google.ios.youtubekids"
+ "com.google.ios.youtubemusic"
+ "com.google.ios.youtubeunplugged"
+ "com.hallmarkchannel.everywhere"
+ "com.hbo.hbonow"
+ "com.hulu.plus"
+ "com.itv.itvplayer"
+ "com.makersoft.uyaniktv"
+ "com.mixerbox.mb3"
+ "com.mlb.AtBatUniversal"
+ "com.mtvn.SPIKE"
+ "com.mtvn.ccnetwork"
+ "com.mtvn.mtvPrimeiPad"
+ "com.mtvn.nickjr"
+ "com.mubi.mubiapp"
+ "com.nbcuni.bravo.bravonow"
+ "com.nbcuni.com.nbcsports.liveextra"
+ "com.nbcuni.nbc.portal"
+ "com.nbcuni.syfy.syfychannel"
+ "com.nbcuni.telemundo.tve"
+ "com.nbcuni.usanetwork.tve"
+ "com.netflix.Netflix"
+ "com.pandora"
+ "com.peacocktv.peacock"
+ "com.plexapp.plex"
+ "com.readdle.ReaddleDocsIPad"
+ "com.showtime.standalone"
+ "com.soundcloud.TouchApp"
+ "com.spotify.client"
+ "com.starz.starzplay"
+ "com.starz.starzplay.international"
+ "com.sundancenow.shudder"
+ "com.tencent.xin"
+ "com.timewarnercable.simulcast"
+ "com.toyopagroup.picaboo"
+ "com.travelchannel.tveverywhere"
+ "com.tunein.TuneInRadio"
+ "com.turner.TBS"
+ "com.turner.TNT"
+ "com.turner.mmod2011temp"
+ "com.uie.foxsports"
+ "com.uie.foxsports.foxsportsgo"
+ "com.vimeo"
+ "com.vk.vkclient"
+ "com.wbd.stream"
+ "containsAirplayTarget"
+ "de.swr.avp.ard.tablet"
+ "de.telekom.entertaintv-iphone"
+ "dk.dr.radioapp"
+ "dk.dr.tv"
+ "first"
+ "fm.overcast.overcast"
+ "in.startv.hotstar"
+ "initWithFirst:second:"
+ "isAirplayTarget"
+ "logUiEvent:withService:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:historyEventsContainer:"
+ "miLoServiceSuspendedReasonBitmap"
+ "net.oqee.appleos"
+ "no.nrk.nrktvapp"
+ "org.npr.one"
+ "org.pbs.playeripad"
+ "org.pbskids.ipadplayer"
+ "pairWithFirst:second:"
+ "ru.yandex.mobile.music"
+ "sameSpaceMiLoScoresForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:"
+ "se.sr.podcastspelare"
+ "second"
+ "setMiLoServiceSuspendedReasonBitmap:"
+ "tv.danmaku.bilianime"
+ "tv.danmaku.bilibilihd"
+ "tv.lifechurch.bible"
+ "tv.molotov.MolotovAppProd"
+ "tv.paladinfeng.miao"
+ "tv.twitch"
+ "uiAnalyticsWithEvent:forCandidateIdentifier:systemStateManager:candidatesContainer:inspections:statisticsManager:service:historyEventsContainer:"
+ "uk.co.bbc.iplayer"
+ "v40@0:8@16q24@32"
+ "\x81"
- "\"!\x13"
- "%s[%@], Context changed for reason: %@, new statistics: %@"
- "%s[%@], candidateName: %@, eventsForCandidate: %@, numberOfCorrectMiLoEvents: %@, numberOfMiLoEvents: %@, TO: %@"
- "@\"NSDictionary\"80@0:8@\"IREventDO\"16@\"NSString\"24@\"IRSystemStateDO\"32@\"IRCandidatesContainerDO\"40@\"IRMiloLslPredictionDO\"48@\"NSDictionary\"56@\"IRStatisticsManager\"64@\"IRServiceDO\"72"
- "logUiEvent:withService:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:"
- "uiAnalyticsWithEvent:forCandidateIdentifier:systemState:candidatesContainer:miloPrediction:inspections:statisticsManager:service:"

```
