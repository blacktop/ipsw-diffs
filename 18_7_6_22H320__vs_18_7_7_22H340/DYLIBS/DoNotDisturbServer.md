## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

```diff

-433.7.1.0.0
-  __TEXT.__text: 0xc2f68
+433.7.1.101.0
+  __TEXT.__text: 0xc2f70
   __TEXT.__auth_stubs: 0x1340
   __TEXT.__objc_methlist: 0xa920
-  __TEXT.__const: 0x520
+  __TEXT.__const: 0x540
   __TEXT.__cstring: 0x88d4
-  __TEXT.__oslogstring: 0x11300
+  __TEXT.__oslogstring: 0x11420
   __TEXT.__gcc_except_tab: 0xf74
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__constg_swiftt: 0x14c

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C82BC813-FA06-3785-A82B-89777D12A743
+  UUID: C25C0411-7914-34E3-B528-657803D0632F
   Functions: 3792
   Symbols:   14331
-  CStrings:  7612
+  CStrings:  7613
 
Functions:
~ -[DNDSEventBehaviorResolver _queue_resolutionForModeSemanticType:withConfiguration:eventDetails:clientDetails:state:date:error:] : 1464 -> 1468
~ -[DNDSEventBehaviorResolver _queue_isBreakthroughAllowedForModeIdentifier:withConfiguration:application:sender:urgency:eventType:threadIdentifier:filterCriteria:notifyAnyway:intelligentBehavior:reason:] : 3144 -> 3148
CStrings:
+ "Breakthrough %{public}@ allowed for global settings with event details: %{sensitive}@."
+ "Breakthrough %{public}@ allowed with reason: %{public}@ for configuration %{sensitive}@ with event details: %{sensitive}@."
+ "Checked if event source is a contact: source=%{sensitive}@, contact=%{BOOL}d"
+ "Checked if event source is a favorite: source=%{sensitive}@, favorite=%{BOOL}d"
+ "Checked if event source is a group contact: source=%{sensitive}@, contact=%{BOOL}d"
+ "Checked if event source is a repeat: source=%{sensitive}@, repeat=%{BOOL}d"
+ "Checked if event source is an emergency contact: source=%{sensitive}@, emergencyContact=%{BOOL}d"
+ "Event was resolved: resolution=%{sensitive}@"
+ "Failed to lookup contact in address book. predicate=%{private}@, error=%{public}@"
+ "Failed to retrieve an LSApplicationRecord for bundleIdentifier:%{private}@; error=%{public}@"
+ "Failed to save settings, will request a radar; settingsRecord=%{private}@, error=%{public}@"
+ "Filled out missing contact identifier: %{public}@ from sender: %{sensitive}@ to determine breakthrough."
+ "Intelligent Resolver behavior: %{public}@ for clientEventDetails: %{sensitive}@"
+ "No change to contact identifier from sender: %{sensitive}@ to determine breakthrough."
+ "Notification filter predicate from App Context did not validate, issues=%{public}@ bundleIdentifier=%{private}@ modeIdentifier=%{private}@"
+ "Notification filter predicate from App Context threw during evaluation, exception=%{public}@ bundleIdentifier=%{private}@ modeIdentifier=%{private}@"
+ "Resolving breakthrough through for configuration: %{sensitive}@ with event details application: %{private}@, sender: %{sensitive}@, urgency: %{public}@, eventType: %{public}@, threadIdentifier: %{private}@"
+ "Resolving global breakthrough for sender: %{sensitive}@"
+ "Saved settings; settingsRecord=%{private}@"
+ "Unable to save migrated default mode: mode=%{sensitive}@ error=%{public}@"
+ "Updated contact identifier to %{public}@ from sender: %{sensitive}@ to determine breakthrough."
- "Breakthrough %{public}@ allowed for global settings with event details: %@."
- "Breakthrough %{public}@ allowed with reason: %@ for configuration %@ with event details: %@."
- "Checked if event source is a contact: source=%{private}@, contact=%{BOOL}d"
- "Checked if event source is a favorite: source=%{private}@, favorite=%{BOOL}d"
- "Checked if event source is a group contact: source=%{private}@, contact=%{BOOL}d"
- "Checked if event source is a repeat: source=%{private}@, repeat=%{BOOL}d"
- "Checked if event source is an emergency contact: source=%{private}@, emergencyContact=%{BOOL}d"
- "Event was resolved: resolution=%@"
- "Failed to lookup contact in address book. predicate=%{public}@, error=%{public}@"
- "Failed to retrieve an LSApplicationRecord for bundleIdentifier:%@; error=%@"
- "Failed to save settings, will request a radar; settingsRecord=%{public}@, error=%{public}@"
- "Filled out missing contact identifier: %{public}@ from sender: %@ to determine breakthrough."
- "Intelligent Resolver behavior: %@ for clientEventDetails: %@"
- "No change to contact identifier from sender: %@ to determine breakthrough."
- "Notification filter predicate from App Context did not validate, issues=%{public}@ bundleIdentifier=%@ modeIdentifier=%@"
- "Notification filter predicate from App Context threw during evaluation, exception=%{public}@ bundleIdentifier=%@ modeIdentifier=%@"
- "Resolving breakthrough through for configuration: %@ with event details application: %{public}@, sender: %@, urgency: %{public}@, eventType: %{public}@, threadIdentifier: %{public}@"
- "Resolving global breakthrough for sender: %@"
- "Saved settings; settingsRecord=%{public}@"
- "Updated contact identifier to %{public}@ from sender: %@ to determine breakthrough."

```
