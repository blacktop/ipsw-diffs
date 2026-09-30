## Focus

> `/System/Library/PrivateFrameworks/Focus.framework/Focus`

```diff

-433.7.1.0.0
-  __TEXT.__text: 0x79c8
+433.7.1.101.0
+  __TEXT.__text: 0x79e4
   __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x88c
-  __TEXT.__const: 0x90
+  __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x4c7
   __TEXT.__gcc_except_tab: 0x668
-  __TEXT.__oslogstring: 0xc08
+  __TEXT.__oslogstring: 0xc1d
   __TEXT.__unwind_info: 0x390
   __TEXT.__objc_classname: 0x11e
   __TEXT.__objc_methname: 0x1d80

   - /System/Library/PrivateFrameworks/DoNotDisturbKit.framework/DoNotDisturbKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 068509A4-F94E-3271-A5B7-D3DCFD345A5D
-  Functions: 188
-  Symbols:   810
+  UUID: 200906DB-9161-35B5-BDB3-1AB2D5C3ADBF
+  Functions: 189
+  Symbols:   812
   CStrings:  471
 
Symbols:
+ _OUTLINED_FUNCTION_13
Functions:
~ -[FCActivityManager _updateLifetimeForActiveActivity] : 548 -> 552
~ -[FCActivityManager _setActiveActivity:withLifetime:reason:] : 1100 -> 1112
~ _OUTLINED_FUNCTION_1 : 32 -> 36
~ _OUTLINED_FUNCTION_2 : 24 -> 32
~ _OUTLINED_FUNCTION_3 : 12 -> 24
~ _OUTLINED_FUNCTION_4 : 16 -> 12
~ _OUTLINED_FUNCTION_5 : 24 -> 16
~ _OUTLINED_FUNCTION_10 : 24 -> 16
~ _OUTLINED_FUNCTION_11 : 32 -> 24
+ _OUTLINED_FUNCTION_13
~ ___43-[FCActivityManager _updateActiveActivity:]_block_invoke_2.cold.1 : 244 -> 236
~ ___51-[FCActivityManager _setLifetimeForActiveActivity:]_block_invoke_2.cold.1 : 244 -> 236
~ ___65-[FCActivityManager _notifyObserversOfLifetimeChangeForActivity:]_block_invoke.cold.1 : 240 -> 232
~ -[FCActivityManager _updateActivity:withLifetimeDetailsCollection:].cold.1 : 152 -> 156
~ ___71-[FCActivityManager _updateLifetimesAlternativeDescriptionForActivity:]_block_invoke.cold.1 : 204 -> 208
CStrings:
+ "[%{public}@] Activating activity: activity: %{private}@; lifetime: %{private}@; reason: %{public}@"
+ "[%{public}@] Activity didn't change from cached value: %{private}@"
+ "[%{public}@] Attempt to activate activity not in collection: activity: %{private}@; availableActivities: %{public}@"
+ "[%{public}@] Did receive updated available lifetime details: %{private}@"
+ "[%{public}@] Encountered error activating activity: activity: %{private}@; lifetime: %{private}@; error: %{public}@"
+ "[%{public}@] Encountered error fetching car automatic DND preference: activity: %{private}@; error: %{public}@"
+ "[%{public}@] Encountered error requesting lifetime details for active mode assertion: activeModeAssertion: %{private}@; error: %{public}@"
+ "[%{public}@] Failed to retrieve dndLifetimeDetails from provided lifetime: %{private}@"
+ "[%{public}@] Lifetime descriptions can't be updated for activity: %{private}@"
+ "[%{public}@] Notifying observer of active activity change: observer: %{public}@; active activity: %{private}@"
+ "[%{public}@] Notifying observer of active lifetime change: observer: %{public}@; lifetime: %{private}@"
+ "[%{public}@] Notifying observer of lifetime descriptions change for activity: observer: %{public}@; activity: %{private}@"
+ "[%{public}@] Updating active activity: %{private}@"
+ "[%{public}@] Updating active mode assertion: %{private}@"
+ "[%{public}@] Updating lifetime descriptions for activity: activity: %{private}@; lifetime descriptions: %{private}@"
+ "[%{public}@] Updating lifetime of active activity: %{private}@"
+ "[%{public}@] Updating suggested activity: %{private}@ (%{private}@)"
- "[%{public}@] Activating activity: activity: %{public}@; lifetime: %{public}@; reason: %{public}@"
- "[%{public}@] Activity didn't change from cached value: %{public}@"
- "[%{public}@] Attempt to activate activity not in collection: activity: %{public}@; availableActivities: %{public}@"
- "[%{public}@] Did receive updated available lifetime details: %{public}@"
- "[%{public}@] Encountered error activating activity: activity: %{public}@; lifetime: %{public}@; error: %{public}@"
- "[%{public}@] Encountered error fetching car automatic DND preference: activity: %{public}@; error: %{public}@"
- "[%{public}@] Encountered error requesting lifetime details for active mode assertion: activeModeAssertion: %{public}@; error: %{public}@"
- "[%{public}@] Failed to retrieve dndLifetimeDetails from provided lifetime: %{public}@"
- "[%{public}@] Lifetime descriptions can't be updated for activity: %{public}@"
- "[%{public}@] Notifying observer of active activity change: observer: %{public}@; active activity: %{public}@"
- "[%{public}@] Notifying observer of active lifetime change: observer: %{public}@; lifetime: %{public}@"
- "[%{public}@] Notifying observer of lifetime descriptions change for activity: observer: %{public}@; activity: %{public}@"
- "[%{public}@] Updating active activity: %{public}@"
- "[%{public}@] Updating active mode assertion: %{public}@"
- "[%{public}@] Updating lifetime descriptions for activity: activity: %{public}@; lifetime descriptions: %{public}@"
- "[%{public}@] Updating lifetime of active activity: %{public}@"
- "[%{public}@] Updating suggested activity: %{public}@ (%{public}@)"

```
