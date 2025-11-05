## CarPlay

> `/System/iOSSupport/System/Library/Frameworks/CarPlay.framework/Versions/A/CarPlay`

```diff

-337.17.3.0.0
-  __TEXT.__text: 0x39430
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x5180
-  __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x32a5
-  __TEXT.__oslogstring: 0x1351
+347.18.2.0.0
+  __TEXT.__text: 0x3b620
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x6328
+  __TEXT.__const: 0x1c8
+  __TEXT.__cstring: 0x35d4
+  __TEXT.__oslogstring: 0x13a8
   __TEXT.__gcc_except_tab: 0x5bc
-  __TEXT.__unwind_info: 0x12d8
-  __TEXT.__objc_classname: 0xd2c
-  __TEXT.__objc_methname: 0xc24f
-  __TEXT.__objc_methtype: 0x1efa
-  __TEXT.__objc_stubs: 0x72e0
-  __DATA_CONST.__got: 0x4c0
+  __TEXT.__unwind_info: 0x1390
+  __TEXT.__objc_classname: 0xdbe
+  __TEXT.__objc_methname: 0xc951
+  __TEXT.__objc_methtype: 0x1faa
+  __TEXT.__objc_stubs: 0x7600
+  __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__const: 0x1778
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2840
+  __DATA_CONST.__objc_selrefs: 0x2a30
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x218
-  __AUTH_CONST.__auth_got: 0x300
+  __DATA_CONST.__objc_superrefs: 0x248
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__cfstring: 0x3700
-  __AUTH_CONST.__objc_const: 0x18f30
+  __AUTH_CONST.__cfstring: 0x39e0
+  __AUTH_CONST.__objc_const: 0x180c0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1b30
-  __DATA.__objc_ivar: 0x680
+  __AUTH.__objc_data: 0x1d10
+  __DATA.__objc_ivar: 0x6dc
   __DATA.__data: 0x1500
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F1E1CA1F-90D2-397F-98E2-507D8EB97D05
-  Functions: 1988
-  Symbols:   5529
-  CStrings:  3469
+  UUID: E6DAEE8A-194D-31A3-8D69-170385F7A017
+  Functions: 2087
+  Symbols:   5755
+  CStrings:  3614
 
Symbols:
+ +[CPChargingStationConnector(CPAccNavUpdate) accNavParameters].cold.1
+ +[CPLane(CPAccNavUpdate) accNavParameters].cold.1
+ +[CPLaneGuidance(CPAccNavUpdate) accNavParameters].cold.1
+ +[CPManeuver(CPAccNavUpdate) accNavParameters].cold.1
+ +[CPNowPlayingMode defaultNowPlayingMode]
+ +[CPNowPlayingMode supportsSecureCoding]
+ +[CPNowPlayingModeSports supportsSecureCoding]
+ +[CPNowPlayingSportsClock supportsSecureCoding]
+ +[CPNowPlayingSportsEventStatus supportsSecureCoding]
+ +[CPNowPlayingSportsTeam supportsSecureCoding]
+ +[CPNowPlayingSportsTeamLogo supportsSecureCoding]
+ +[CPNowPlayingTemplate sharedTemplate].cold.1
+ +[CPRouteGuidance(CPAccNavUpdate) accNavParameters].cold.1
+ +[NSUnitEnergy(CPChargePrecondition) wattHours].cold.1
+ -[CPInterfaceController popToTemplate:animated:completion:].cold.1
+ -[CPInterfaceController popToTemplate:animated:completion:].cold.2
+ -[CPInterfaceController presentTemplate:animated:completion:].cold.1
+ -[CPInterfaceController presentTemplate:animated:completion:].cold.2
+ -[CPInterfaceController pushTemplate:animated:completion:].cold.1
+ -[CPInterfaceController pushTemplate:animated:completion:].cold.2
+ -[CPInterfaceController setRootTemplate:animated:completion:].cold.1
+ -[CPInterfaceController setRootTemplate:animated:completion:].cold.2
+ -[CPListTemplate setShowsSpinnerWhileEmpty:]
+ -[CPListTemplate showsSpinnerWhileEmpty]
+ -[CPNavigationManager _connectionRetryDelay].cold.1
+ -[CPNavigationManager controlsAccNav]
+ -[CPNavigationManager setControlsAccNav:]
+ -[CPNowPlayingMode .cxx_destruct]
+ -[CPNowPlayingMode encodeWithCoder:]
+ -[CPNowPlayingMode hash]
+ -[CPNowPlayingMode identifier]
+ -[CPNowPlayingMode initWithCoder:]
+ -[CPNowPlayingMode init]
+ -[CPNowPlayingMode isEqual:]
+ -[CPNowPlayingMode isEqualToNowPlayingMode:]
+ -[CPNowPlayingModeSports .cxx_destruct]
+ -[CPNowPlayingModeSports backgroundArtwork]
+ -[CPNowPlayingModeSports encodeWithCoder:]
+ -[CPNowPlayingModeSports eventStatus]
+ -[CPNowPlayingModeSports hash]
+ -[CPNowPlayingModeSports initWithCoder:]
+ -[CPNowPlayingModeSports initWithLeftTeam:rightTeam:eventStatus:backgroundArtwork:]
+ -[CPNowPlayingModeSports isEqual:]
+ -[CPNowPlayingModeSports isEqualToNowPlayingModeSports:]
+ -[CPNowPlayingModeSports leftTeam]
+ -[CPNowPlayingModeSports rightTeam]
+ -[CPNowPlayingSportsClock countsUp]
+ -[CPNowPlayingSportsClock encodeWithCoder:]
+ -[CPNowPlayingSportsClock hash]
+ -[CPNowPlayingSportsClock initWithCoder:]
+ -[CPNowPlayingSportsClock initWithElapsedTime:paused:]
+ -[CPNowPlayingSportsClock initWithTimeRemaining:paused:]
+ -[CPNowPlayingSportsClock isEqual:]
+ -[CPNowPlayingSportsClock isEqualToSportsClock:]
+ -[CPNowPlayingSportsClock isPaused]
+ -[CPNowPlayingSportsClock timeValue]
+ -[CPNowPlayingSportsEventStatus .cxx_destruct]
+ -[CPNowPlayingSportsEventStatus encodeWithCoder:]
+ -[CPNowPlayingSportsEventStatus eventClock]
+ -[CPNowPlayingSportsEventStatus eventStatusImage]
+ -[CPNowPlayingSportsEventStatus eventStatusText]
+ -[CPNowPlayingSportsEventStatus hash]
+ -[CPNowPlayingSportsEventStatus initWithCoder:]
+ -[CPNowPlayingSportsEventStatus initWithEventStatusText:eventStatusImage:eventClock:]
+ -[CPNowPlayingSportsEventStatus isEqual:]
+ -[CPNowPlayingSportsEventStatus isEqualToGameStatus:]
+ -[CPNowPlayingSportsTeam .cxx_destruct]
+ -[CPNowPlayingSportsTeam encodeWithCoder:]
+ -[CPNowPlayingSportsTeam eventScore]
+ -[CPNowPlayingSportsTeam hash]
+ -[CPNowPlayingSportsTeam identifier]
+ -[CPNowPlayingSportsTeam initWithCoder:]
+ -[CPNowPlayingSportsTeam initWithName:logo:teamStandings:eventScore:possessionIndicator:favorite:]
+ -[CPNowPlayingSportsTeam isEqual:]
+ -[CPNowPlayingSportsTeam isEqualToSportsTeam:]
+ -[CPNowPlayingSportsTeam isFavorite]
+ -[CPNowPlayingSportsTeam logo]
+ -[CPNowPlayingSportsTeam name]
+ -[CPNowPlayingSportsTeam possessionIndicator]
+ -[CPNowPlayingSportsTeam teamStandings]
+ -[CPNowPlayingSportsTeamLogo .cxx_destruct]
+ -[CPNowPlayingSportsTeamLogo encodeWithCoder:]
+ -[CPNowPlayingSportsTeamLogo hashValue]
+ -[CPNowPlayingSportsTeamLogo initWithCoder:]
+ -[CPNowPlayingSportsTeamLogo initWithTeamInitials:]
+ -[CPNowPlayingSportsTeamLogo initWithTeamLogo:]
+ -[CPNowPlayingSportsTeamLogo initials]
+ -[CPNowPlayingSportsTeamLogo isEqual:]
+ -[CPNowPlayingSportsTeamLogo isEqualToTeamLogo:]
+ -[CPNowPlayingSportsTeamLogo logo]
+ -[CPNowPlayingTemplate nowPlayingMode]
+ -[CPNowPlayingTemplate setNowPlayingMode:]
+ -[CPTabBarTemplate initWithCoder:].cold.1
+ -[CPTabBarTemplate validateTemplates:].cold.1
+ -[CPTemplateApplicationScene _shouldCreateCarWindow].cold.1
+ CPDrivingTaskTemplateClasses.cold.1
+ CPFuelingTemplateClasses.cold.1
+ CPPublicSafetyTemplateClasses.cold.1
+ CPQuickOrderingTemplateClasses.cold.1
+ CarPlayFrameworkACCNavLogging.cold.1
+ CarPlayFrameworkGeneralLogging.cold.1
+ GCC_except_table31
+ OBJC_IVAR_$_CPListTemplate._showsSpinnerWhileEmpty
+ OBJC_IVAR_$_CPNavigationManager._controlsAccNav
+ OBJC_IVAR_$_CPNowPlayingMode._identifier
+ OBJC_IVAR_$_CPNowPlayingModeSports._backgroundArtwork
+ OBJC_IVAR_$_CPNowPlayingModeSports._eventStatus
+ OBJC_IVAR_$_CPNowPlayingModeSports._leftTeam
+ OBJC_IVAR_$_CPNowPlayingModeSports._rightTeam
+ OBJC_IVAR_$_CPNowPlayingSportsClock._countsUp
+ OBJC_IVAR_$_CPNowPlayingSportsClock._paused
+ OBJC_IVAR_$_CPNowPlayingSportsClock._timeValue
+ OBJC_IVAR_$_CPNowPlayingSportsEventStatus._eventClock
+ OBJC_IVAR_$_CPNowPlayingSportsEventStatus._eventStatusImage
+ OBJC_IVAR_$_CPNowPlayingSportsEventStatus._eventStatusText
+ OBJC_IVAR_$_CPNowPlayingSportsTeam._eventScore
+ OBJC_IVAR_$_CPNowPlayingSportsTeam._favorite
+ OBJC_IVAR_$_CPNowPlayingSportsTeam._identifier
+ OBJC_IVAR_$_CPNowPlayingSportsTeam._logo
+ OBJC_IVAR_$_CPNowPlayingSportsTeam._name
+ OBJC_IVAR_$_CPNowPlayingSportsTeam._possessionIndicator
+ OBJC_IVAR_$_CPNowPlayingSportsTeam._teamStandings
+ OBJC_IVAR_$_CPNowPlayingSportsTeamLogo._initials
+ OBJC_IVAR_$_CPNowPlayingSportsTeamLogo._logo
+ OBJC_IVAR_$_CPNowPlayingTemplate._nowPlayingMode
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
+ __58-[CPNowPlayingTemplate handleAction:forControlIdentifier:]_block_invoke.31
+ __96-[CPListTemplate listTemplateWithIdentifier:didSelectImageAtIndex:inImageRowItemWithIdentifier:]_block_invoke.146
+ __CPAllowedTemplateClassesForCurrentEntitlement_block_invoke.cold.1
+ __CPAllowedTemplateClassesForCurrentEntitlement_block_invoke.cold.2
+ __CPAllowedTemplateClassesForCurrentEntitlement_block_invoke.cold.3
+ __CPAllowedTemplateClassesForCurrentEntitlement_block_invoke.cold.4
+ __CPRootTemplateClasses_block_invoke.cold.1
+ __CPWhiteListedTemplates_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_CPNowPlayingMode
+ __OBJC_$_CLASS_METHODS_CPNowPlayingModeSports
+ __OBJC_$_CLASS_METHODS_CPNowPlayingSportsClock
+ __OBJC_$_CLASS_METHODS_CPNowPlayingSportsEventStatus
+ __OBJC_$_CLASS_METHODS_CPNowPlayingSportsTeam
+ __OBJC_$_CLASS_METHODS_CPNowPlayingSportsTeamLogo
+ __OBJC_$_CLASS_PROP_LIST_CPNowPlayingMode
+ __OBJC_$_CLASS_PROP_LIST_CPNowPlayingModeSports
+ __OBJC_$_CLASS_PROP_LIST_CPNowPlayingSportsClock
+ __OBJC_$_CLASS_PROP_LIST_CPNowPlayingSportsEventStatus
+ __OBJC_$_CLASS_PROP_LIST_CPNowPlayingSportsTeam
+ __OBJC_$_CLASS_PROP_LIST_CPNowPlayingSportsTeamLogo
+ __OBJC_$_INSTANCE_METHODS_CPNowPlayingMode
+ __OBJC_$_INSTANCE_METHODS_CPNowPlayingModeSports
+ __OBJC_$_INSTANCE_METHODS_CPNowPlayingSportsClock
+ __OBJC_$_INSTANCE_METHODS_CPNowPlayingSportsEventStatus
+ __OBJC_$_INSTANCE_METHODS_CPNowPlayingSportsTeam
+ __OBJC_$_INSTANCE_METHODS_CPNowPlayingSportsTeamLogo
+ __OBJC_$_INSTANCE_VARIABLES_CPNowPlayingMode
+ __OBJC_$_INSTANCE_VARIABLES_CPNowPlayingModeSports
+ __OBJC_$_INSTANCE_VARIABLES_CPNowPlayingSportsClock
+ __OBJC_$_INSTANCE_VARIABLES_CPNowPlayingSportsEventStatus
+ __OBJC_$_INSTANCE_VARIABLES_CPNowPlayingSportsTeam
+ __OBJC_$_INSTANCE_VARIABLES_CPNowPlayingSportsTeamLogo
+ __OBJC_$_PROP_LIST_CPNowPlayingMode
+ __OBJC_$_PROP_LIST_CPNowPlayingModeSports
+ __OBJC_$_PROP_LIST_CPNowPlayingSportsClock
+ __OBJC_$_PROP_LIST_CPNowPlayingSportsEventStatus
+ __OBJC_$_PROP_LIST_CPNowPlayingSportsTeam
+ __OBJC_$_PROP_LIST_CPNowPlayingSportsTeamLogo
+ __OBJC_CLASS_PROTOCOLS_$_CPNowPlayingMode
+ __OBJC_CLASS_PROTOCOLS_$_CPNowPlayingModeSports
+ __OBJC_CLASS_PROTOCOLS_$_CPNowPlayingSportsClock
+ __OBJC_CLASS_PROTOCOLS_$_CPNowPlayingSportsEventStatus
+ __OBJC_CLASS_PROTOCOLS_$_CPNowPlayingSportsTeam
+ __OBJC_CLASS_PROTOCOLS_$_CPNowPlayingSportsTeamLogo
+ __OBJC_CLASS_RO_$_CPNowPlayingMode
+ __OBJC_CLASS_RO_$_CPNowPlayingModeSports
+ __OBJC_CLASS_RO_$_CPNowPlayingSportsClock
+ __OBJC_CLASS_RO_$_CPNowPlayingSportsEventStatus
+ __OBJC_CLASS_RO_$_CPNowPlayingSportsTeam
+ __OBJC_CLASS_RO_$_CPNowPlayingSportsTeamLogo
+ __OBJC_METACLASS_RO_$_CPNowPlayingMode
+ __OBJC_METACLASS_RO_$_CPNowPlayingModeSports
+ __OBJC_METACLASS_RO_$_CPNowPlayingSportsClock
+ __OBJC_METACLASS_RO_$_CPNowPlayingSportsEventStatus
+ __OBJC_METACLASS_RO_$_CPNowPlayingSportsTeam
+ __OBJC_METACLASS_RO_$_CPNowPlayingSportsTeamLogo
+ ___41+[CPNowPlayingMode defaultNowPlayingMode]_block_invoke
+ __block_literal_global.149
+ __os_feature_enabled_impl
+ _objc_msgSend$backgroundArtwork
+ _objc_msgSend$countsUp
+ _objc_msgSend$eventClock
+ _objc_msgSend$eventScore
+ _objc_msgSend$eventStatus
+ _objc_msgSend$eventStatusImage
+ _objc_msgSend$eventStatusText
+ _objc_msgSend$initials
+ _objc_msgSend$isEqualToGameStatus:
+ _objc_msgSend$isEqualToNowPlayingMode:
+ _objc_msgSend$isEqualToNowPlayingModeSports:
+ _objc_msgSend$isEqualToSportsClock:
+ _objc_msgSend$isEqualToSportsTeam:
+ _objc_msgSend$isEqualToTeamLogo:
+ _objc_msgSend$isFavorite
+ _objc_msgSend$isPaused
+ _objc_msgSend$leftTeam
+ _objc_msgSend$logo
+ _objc_msgSend$nowPlayingMode
+ _objc_msgSend$possessionIndicator
+ _objc_msgSend$rightTeam
+ _objc_msgSend$showsSpinnerWhileEmpty
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$teamStandings
+ _objc_msgSend$timeValue
+ _objc_retainAutoreleasedReturnValue
+ defaultNowPlayingMode.__defaultMode
+ defaultNowPlayingMode.onceToken
- GCC_except_table30
- __58-[CPNowPlayingTemplate handleAction:forControlIdentifier:]_block_invoke.26
- ___96-[CPListTemplate listTemplateWithIdentifier:didSelectImageAtIndex:inImageRowItemWithIdentifier:]_block_invoke_2
- __block_literal_global.145
CStrings:
+ "%@ selected image row item %{public}@ image index %{public}@"
+ "%@ selected list item %{public}@"
+ "%@: Update now playing mode %@"
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
+ "TB,N,V_controlsAccNav"
+ "TB,N,V_showsSpinnerWhileEmpty"
+ "TB,R,N,GisFavorite,V_favorite"
+ "TB,R,N,GisPaused,V_paused"
+ "TB,R,N,V_countsUp"
+ "Td,R,N,V_timeValue"
+ "_backgroundArtwork"
+ "_controlsAccNav"
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
+ "rightTeam"
+ "setControlsAccNav:"
+ "setNowPlayingMode:"
+ "setShowsSpinnerWhileEmpty:"
+ "showsSpinnerWhileEmpty"
+ "substringToIndex:"
+ "teamStandings"
+ "timeValue"
- "%@ didSelectListItemWithIdentifier %@"

```
