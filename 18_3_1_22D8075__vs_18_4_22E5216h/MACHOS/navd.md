## navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

-2864.33.11.14.5
-  __TEXT.__text: 0x57334
+2864.34.9.12.39
+  __TEXT.__text: 0x57160
   __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_stubs: 0x8f20
-  __TEXT.__objc_methlist: 0x2c64
-  __TEXT.__const: 0x270
-  __TEXT.__objc_methname: 0x9cb2
-  __TEXT.__cstring: 0x683a
-  __TEXT.__oslogstring: 0x60c4
-  __TEXT.__objc_classname: 0xc81
-  __TEXT.__objc_methtype: 0x2357
-  __TEXT.__gcc_except_tab: 0x6254
+  __TEXT.__objc_stubs: 0x9020
+  __TEXT.__objc_methlist: 0x35fc
+  __TEXT.__const: 0x260
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x18c0
+  __TEXT.__objc_methname: 0x9d7f
+  __TEXT.__cstring: 0x6882
+  __TEXT.__oslogstring: 0x6114
+  __TEXT.__objc_classname: 0xc83
+  __TEXT.__objc_methtype: 0x23b6
+  __TEXT.__gcc_except_tab: 0x62ec
+  __TEXT.__unwind_info: 0x18a0
   __DATA_CONST.__auth_got: 0x5a0
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x3a30
-  __DATA_CONST.__cfstring: 0x37a0
+  __DATA_CONST.__got: 0x798
+  __DATA_CONST.__const: 0x3a88
+  __DATA_CONST.__cfstring: 0x3800
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x190

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x200
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x87e8
-  __DATA.__objc_selrefs: 0x27e8
-  __DATA.__objc_ivar: 0x50c
+  __DATA.__objc_const: 0x77d8
+  __DATA.__objc_selrefs: 0x2948
+  __DATA.__objc_ivar: 0x518
   __DATA.__objc_data: 0x16d0
-  __DATA.__data: 0x1620
-  __DATA.__bss: 0x1d0
+  __DATA.__data: 0x1870
+  __DATA.__bss: 0x1d8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1377
-  Symbols:   440
-  CStrings:  3407
+  Functions: 1374
+  Symbols:   444
+  CStrings:  3425
 
Symbols:
+ _GEOConfigNavdVehicleBTNotificationEnableShortcutMatching
+ _GEOConfigNavdVehicleBTNotificationFavoriteMatchingDistance
+ _OBJC_CLASS_$_MapsSuggestionsFrequentLocationImprover
+ _OBJC_CLASS_$_MapsSuggestionsShortcutMatcher
CStrings:
+ "\x03\x13"
+ "\v"
+ "\x0f\x02\x14!"
+ "@\"MapsSuggestionsShortcutMatcher\""
+ "@20@0:8B16"
+ "MapsSuggestionsCoreRoutineLabel"
+ "MapsSuggestionsRoutineSource"
+ "NavdRouteGenius_EnableShortcutMatchingKey"
+ "Will use private queue when shared instance is created"
+ "[%{public}@] using private dispatch queue"
+ "_operationQueue"
+ "_shortcutMatcher"
+ "com.apple.Maps.ExternalAccessory"
+ "hasShortcutOfType:"
+ "improveEntry:"
+ "initWithFavorites:minimumMatchingDistance:"
+ "initWithPrivateQueue:"
+ "originatingSourceName"
+ "setType:"
+ "setUnderlyingQueue:"
+ "setUsePrivateQueue"
+ "setUsePrivateQueue: called too late, shared instance already exists!"
+ "shortcutForEntry:type:"
+ "shortcuts"
+ "suppressing posting notification while initialising MapsExternalAccessory"
+ "{_Config=\"name\"@\"NSString\"\"engine\"@\"MapsSuggestionsEngine\"\"requester\"@\"NavdNetworkRequester\"\"delegate\"@\"<MNRouteGeniusDelegateProxy>\"\"routeAttributes\"@\"GEORouteAttributes\"\"locationUpdater\"@\"<MapsSuggestionsLocationUpdater>\"\"etaRequirements\"@\"MapsSuggestionsETARequirements\"\"appGuardian\"@\"MapsSuggestionsAppGuardian\"\"shortcutMatcher\"@\"MapsSuggestionsShortcutMatcher\"}"
- "\x01\x13"
- "\x0f\x01\x14!"
- "%{public}s:%{public}d: shortcutStrongSelf went away in %{public}s"
- "-[NavdRouteGenius _updateEntriesWithShareETAData:]_block_invoke"
- "Unable to load shortcuts:%@"
- "loadAllShortcutsWithHandler:"
- "suppressing notification while initialising MapsExternalAccessory"
- "{_Config=\"name\"@\"NSString\"\"engine\"@\"MapsSuggestionsEngine\"\"requester\"@\"NavdNetworkRequester\"\"delegate\"@\"<MNRouteGeniusDelegateProxy>\"\"routeAttributes\"@\"GEORouteAttributes\"\"locationUpdater\"@\"<MapsSuggestionsLocationUpdater>\"\"etaRequirements\"@\"MapsSuggestionsETARequirements\"\"appGuardian\"@\"MapsSuggestionsAppGuardian\"}"

```
