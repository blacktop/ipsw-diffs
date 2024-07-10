## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/Versions/A/IntelligentRoutingDaemon`

```diff

-95.0.1.0.0
-  __TEXT.__text: 0x7233c
+94.0.0.0.0
+  __TEXT.__text: 0x72408
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x68fc
+  __TEXT.__objc_methlist: 0x6914
   __TEXT.__oslogstring: 0x58f3
-  __TEXT.__cstring: 0x7d53
+  __TEXT.__cstring: 0x8628
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x1760
-  __TEXT.__unwind_info: 0x17b8
+  __TEXT.__gcc_except_tab: 0x176c
+  __TEXT.__unwind_info: 0x17c0
   __TEXT.__objc_classname: 0xed2
-  __TEXT.__objc_methname: 0x15f87
+  __TEXT.__objc_methname: 0x15fb6
   __TEXT.__objc_methtype: 0x1d55
-  __TEXT.__objc_stubs: 0xd560
+  __TEXT.__objc_stubs: 0xd5a0
   __DATA_CONST.__got: 0x728
   __DATA_CONST.__const: 0x608
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ba8
+  __DATA_CONST.__objc_selrefs: 0x3bb8
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0xa0
+  __DATA_CONST.__objc_arraydata: 0x400
   __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x1f90
-  __AUTH_CONST.__cfstring: 0x5d20
+  __AUTH_CONST.__cfstring: 0x6a20
   __AUTH_CONST.__objc_const: 0xe548
   __AUTH_CONST.__objc_intobj: 0x330
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x2990
   __DATA.__objc_ivar: 0x8f8

   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2545
-  Symbols:   6591
-  CStrings:  887
+  Functions: 2547
+  Symbols:   6595
+  CStrings:  991
 
Symbols:
+ +[IRAnalyticsUtilities _temporaryListOfAllowedApps]
+ +[IRAnalyticsUtilities isMediaEligibleApp:]
+ -[IRCandidateClassificationDetectorSameSpace adjustSameSpaceParametersForCandidates:withSystemState:andHistoryEventsAsc:andMiLoPredction:andNearbyDevicesContainer:andDate:]
+ ___172-[IRCandidateClassificationDetectorSameSpace adjustSameSpaceParametersForCandidates:withSystemState:andHistoryEventsAsc:andMiLoPredction:andNearbyDevicesContainer:andDate:]_block_invoke
+ _objc_msgSend$_temporaryListOfAllowedApps
+ _objc_msgSend$adjustSameSpaceParametersForCandidates:withSystemState:andHistoryEventsAsc:andMiLoPredction:andNearbyDevicesContainer:andDate:
+ _objc_msgSend$isMediaEligibleApp:
- -[IRCandidateClassificationDetectorSameSpace adjustSameSpaceParametersForCandidates:withSystemState:andHistoryEventsAsc:andMiLoPrediction:andNearbyDevicesContainer:andDate:]
- ___173-[IRCandidateClassificationDetectorSameSpace adjustSameSpaceParametersForCandidates:withSystemState:andHistoryEventsAsc:andMiLoPrediction:andNearbyDevicesContainer:andDate:]_block_invoke
- _objc_msgSend$adjustSameSpaceParametersForCandidates:withSystemState:andHistoryEventsAsc:andMiLoPrediction:andNearbyDevicesContainer:andDate:
CStrings:
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/AVOutputContext/IRAVOutputContextController.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/Biome/IRBiomeBridge.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/Biome/IRBiomeProvider.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/MiLo/IRMiLoProvider.m"
+ "app.svn.Cheers"
+ "au.com.shiftyjelly.podcasts"
+ "ch.monstar.ios"
+ "com.abcdigital.abc.videoplayer"
+ "com.amazon.aiv.AIVApp"
+ "com.apple.SoundScapes"
+ "com.apple.TVMovies"
+ "com.apple.TVMusic"
+ "com.apple.TVWatchList"
+ "com.apple.mediaservicesbroker.app"
+ "com.apple.movietrailers"
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
+ "de.swr.avp.ard.tablet"
+ "de.telekom.entertaintv-iphone"
+ "dk.dr.radioapp"
+ "dk.dr.tv"
+ "fm.overcast.overcast"
+ "in.startv.hotstar"
+ "net.oqee.appleos"
+ "no.nrk.nrktvapp"
+ "org.npr.one"
+ "org.pbs.playeripad"
+ "org.pbskids.ipadplayer"
+ "ru.yandex.mobile.music"
+ "se.sr.podcastspelare"
+ "tv.danmaku.bilianime"
+ "tv.danmaku.bilibilihd"
+ "tv.lifechurch.bible"
+ "tv.molotov.MolotovAppProd"
+ "tv.paladinfeng.miao"
+ "tv.twitch"
+ "uk.co.bbc.iplayer"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/AVOutputContext/IRAVOutputContextController.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/Biome/IRBiomeBridge.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/Biome/IRBiomeProvider.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/MiLo/IRMiLoProvider.m"

```
