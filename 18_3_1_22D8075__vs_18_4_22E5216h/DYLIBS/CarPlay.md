## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-337.17.2.0.0
-  __TEXT.__text: 0x3f96c
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x5628
-  __TEXT.__const: 0x1f0
-  __TEXT.__cstring: 0x33d1
-  __TEXT.__oslogstring: 0x1b5d
+347.15.0.0.0
+  __TEXT.__text: 0x41db4
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x6990
+  __TEXT.__const: 0x200
+  __TEXT.__cstring: 0x3700
+  __TEXT.__oslogstring: 0x1c3e
   __TEXT.__gcc_except_tab: 0x7c0
-  __TEXT.__unwind_info: 0x1488
-  __TEXT.__objc_classname: 0xe35
-  __TEXT.__objc_methname: 0xd09f
-  __TEXT.__objc_methtype: 0x2087
-  __TEXT.__objc_stubs: 0x82c0
-  __DATA_CONST.__got: 0x580
+  __TEXT.__unwind_info: 0x1558
+  __TEXT.__objc_classname: 0xec8
+  __TEXT.__objc_methname: 0xd789
+  __TEXT.__objc_methtype: 0x2137
+  __TEXT.__objc_stubs: 0x8640
+  __DATA_CONST.__got: 0x5b0
   __DATA_CONST.__const: 0x1918
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c10
+  __DATA_CONST.__objc_selrefs: 0x2e30
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x220
-  __AUTH_CONST.__auth_got: 0x318
+  __DATA_CONST.__objc_superrefs: 0x250
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0x3800
-  __AUTH_CONST.__objc_const: 0x1a3b0
+  __AUTH_CONST.__cfstring: 0x3ae0
+  __AUTH_CONST.__objc_const: 0x19268
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x6b4
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x70c
   __DATA.__data: 0x18c0
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1c8
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2135
-  Symbols:   2564
-  CStrings:  3288
+  Functions: 2238
+  Symbols:   2691
+  CStrings:  3412
 
Symbols:
+ _NSStringFromCRAccNavRole
+ _OBJC_CLASS_$_CPNowPlayingMode
+ _OBJC_CLASS_$_CPNowPlayingModeSports
+ _OBJC_CLASS_$_CPNowPlayingSportsClock
+ _OBJC_CLASS_$_CPNowPlayingSportsEventStatus
+ _OBJC_CLASS_$_CPNowPlayingSportsTeam
+ _OBJC_CLASS_$_CPNowPlayingSportsTeamLogo
+ _OBJC_METACLASS_$_CPNowPlayingMode
+ _OBJC_METACLASS_$_CPNowPlayingModeSports
+ _OBJC_METACLASS_$_CPNowPlayingSportsClock
+ _OBJC_METACLASS_$_CPNowPlayingSportsEventStatus
+ _OBJC_METACLASS_$_CPNowPlayingSportsTeam
+ _OBJC_METACLASS_$_CPNowPlayingSportsTeamLogo
+ __os_feature_enabled_impl
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "!\x12\x16"
+ "%@ selected image row item %{public}@ image index %{public}@"
+ "%@ selected list item %{public}@"
+ "%@: Update now playing mode %@"
+ "%s: componentUID=%{public}@ %{public}@ controls acc nav on its own"
+ "&"
+ "0"
+ "@\"CPNowPlayingMode\""
+ "@\"CPNowPlayingSportsClock\""
+ "@\"CPNowPlayingSportsEventStatus\""
+ "@\"CPNowPlayingSportsTeam\""
+ "@\"CPNowPlayingSportsTeamLogo\""
+ "@28@0:8d16B24"
+ "@60@0:8@16@24@32@40@48B56"
+ "CPNowPlayingMode"
+ "CPNowPlayingModeSports"
+ "CPNowPlayingSportsClock"
+ "CPNowPlayingSportsEventStatus"
+ "CPNowPlayingSportsTeam"
+ "CPNowPlayingSportsTeamLogo"
+ "CarPlay"
+ "Sports"
+ "T@\"CPNowPlayingMode\",&,N,V_nowPlayingMode"
+ "T@\"CPNowPlayingMode\",R,N"
+ "T@\"CPNowPlayingSportsClock\",R,C,N,V_eventClock"
+ "T@\"CPNowPlayingSportsEventStatus\",R,N,V_eventStatus"
+ "T@\"CPNowPlayingSportsTeam\",R,N,V_leftTeam"
+ "T@\"CPNowPlayingSportsTeam\",R,N,V_rightTeam"
+ "T@\"CPNowPlayingSportsTeamLogo\",R,C,N,V_logo"
+ "T@\"NSArray\",R,C,N,V_eventStatusText"
+ "T@\"NSString\",R,C,N,V_eventScore"
+ "T@\"NSString\",R,C,N,V_initials"
+ "T@\"NSString\",R,C,N,V_name"
+ "T@\"NSString\",R,C,N,V_teamStandings"
+ "T@\"UIImage\",R,C,N,V_backgroundArtwork"
+ "T@\"UIImage\",R,C,N,V_eventStatusImage"
+ "T@\"UIImage\",R,C,N,V_logo"
+ "T@\"UIImage\",R,C,N,V_possessionIndicator"
+ "TB,N,V_showsSpinnerWhileEmpty"
+ "TB,R,N,GisFavorite,V_favorite"
+ "TB,R,N,GisPaused,V_paused"
+ "TB,R,N,V_countsUp"
+ "TQ,N,V_accNavRole"
+ "Td,R,N,V_timeValue"
+ "_accNavRole"
+ "_backgroundArtwork"
+ "_countsUp"
+ "_eventClock"
+ "_eventScore"
+ "_eventStatus"
+ "_eventStatusImage"
+ "_eventStatusText"
+ "_favorite"
+ "_initials"
+ "_leftTeam"
+ "_logo"
+ "_nowPlayingMode"
+ "_paused"
+ "_possessionIndicator"
+ "_rightTeam"
+ "_showsSpinnerWhileEmpty"
+ "_teamStandings"
+ "_timeValue"
+ "accNavRole"
+ "addNavigationOwnerWithIdentifier:accNavRole:"
+ "backgroundArtwork"
+ "controlsAccNav"
+ "countsUp"
+ "defaultNowPlayingMode"
+ "eventClock"
+ "eventScore"
+ "eventStatus"
+ "eventStatusImage"
+ "eventStatusText"
+ "favorite"
+ "hashValue"
+ "initWithElapsedTime:paused:"
+ "initWithEventStatusText:eventStatusImage:eventClock:"
+ "initWithLeftTeam:rightTeam:eventStatus:backgroundArtwork:"
+ "initWithName:logo:teamStandings:eventScore:possessionIndicator:favorite:"
+ "initWithTeamInitials:"
+ "initWithTeamLogo:"
+ "initWithTimeRemaining:paused:"
+ "initials"
+ "isEqualToGameStatus:"
+ "isEqualToNowPlayingMode:"
+ "isEqualToNowPlayingModeSports:"
+ "isEqualToSportsClock:"
+ "isEqualToSportsTeam:"
+ "isEqualToTeamLogo:"
+ "isFavorite"
+ "isPaused"
+ "kCPListTemplateShowsEmptySpinnerKey"
+ "kCPNowPlayingModeIdentifier"
+ "kCPNowPlayingModeSportsBackgroundArtworkKey"
+ "kCPNowPlayingModeSportsEventStatusClockKey"
+ "kCPNowPlayingModeSportsEventStatusKey"
+ "kCPNowPlayingModeSportsEventStatusTextKey"
+ "kCPNowPlayingModeSportsEventtatusImageKey"
+ "kCPNowPlayingModeSportsLeftTeamKey"
+ "kCPNowPlayingModeSportsRightTeamKey"
+ "kCPNowPlayingSportsTeamFavoriteKey"
+ "kCPNowPlayingSportsTeamIdentifierKey"
+ "kCPNowPlayingSportsTeamInitialsKey"
+ "kCPNowPlayingSportsTeamLogoImageKey"
+ "kCPNowPlayingSportsTeamLogoKey"
+ "kCPNowPlayingSportsTeamNameKey"
+ "kCPNowPlayingSportsTeamPossessionIndicatorKey"
+ "kCPNowPlayingSportsTeamScoreKey"
+ "kCPNowPlayingSportsTeamStandingKey"
+ "kCPNowPlayingSportsTimerCountsUpKey"
+ "kCPNowPlayingSportsTimerPausedKey"
+ "kCPNowPlayingSportsTimerTimeValueKey"
+ "kCPTemplateNowPlayingModeKey"
+ "leftTeam"
+ "logo"
+ "nowPlayingMode"
+ "paused"
+ "possessionIndicator"
+ "releaseNavigationOwnership for %{public}@"
+ "requestNavigationOwnership for %{public}@ accNavRole=%{public}@"
+ "resending Info failed ownsNavigation=%@ accNavRole=%@ owner=%@ lastNavigatingBundleIdentifier=%@"
+ "rightTeam"
+ "setAccNavRole:"
+ "setControlsAccNav:"
+ "setNowPlayingMode:"
+ "setShowsSpinnerWhileEmpty:"
+ "showsSpinnerWhileEmpty"
+ "skip resending info: AccNav is controlled by owner"
+ "substringToIndex:"
+ "teamStandings"
+ "timeValue"
- "!\x18"
- "%@ didSelectListItemWithIdentifier %@"
- "TB,N,V_supportsAccNav"
- "_supportsAccNav"
- "addNavigationOwnerWithIdentifier:supportsAccNav:"
- "requestNavigationOwnership for %@ supporting AccNav %@"
- "resending Info failed ownsNavigation=%@ supportsAccNav=%@ owner=%@ lastNavigatingBundleIdentifier=%@"

```
