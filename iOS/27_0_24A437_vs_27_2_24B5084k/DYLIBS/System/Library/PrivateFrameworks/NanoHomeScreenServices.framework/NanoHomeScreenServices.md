## NanoHomeScreenServices

> `/System/Library/PrivateFrameworks/NanoHomeScreenServices.framework/NanoHomeScreenServices`

```diff

-337.0.0.0.0
-  __TEXT.__text: 0x4db8
+348.0.0.0.0
+  __TEXT.__text: 0x4f0c
   __TEXT.__objc_methlist: 0x654
-  __TEXT.__const: 0x7a
+  __TEXT.__const: 0x82
   __TEXT.__cstring: 0x799
-  __TEXT.__oslogstring: 0x408
+  __TEXT.__oslogstring: 0x4b6
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__unwind_info: 0x308
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 172
-  Symbols:   478
-  CStrings:  74
+  Symbols:   480
+  CStrings:  78
 
Symbols:
+ _objc_release_x26
+ _objc_release_x28
Functions:
~ -[NHSSSmartStackSuggestionDefaults setWidgetSuggestionsUnmuteDate:forContainerBundleIdentifier:extensionBundleIdentifier:kind:] : 252 -> 404
~ -[NHSSSmartStackSuggestionDefaults _cleanUpExpiredMutePreferences] : 448 -> 560
~ ___78-[NHSSSmartStackSuggestionDefaults _scheduleTimerToUnmuteWidgetForKey:onDate:]_block_invoke : 188 -> 264
CStrings:
+ "mute cleared for %{public}@"
+ "mute set for %{public}@ until %{public}@"
+ "pruning expired mute for %{public}@ (expired %{public}@)"
+ "unmute timer fired, mute removed for %{public}@"
```
