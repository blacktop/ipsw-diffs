## HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

-803.3.7.1.5
-  __TEXT.__text: 0x76d48
-  __TEXT.__auth_stubs: 0x2060
+825.2.8.1.1
+  __TEXT.__text: 0x86bb4
+  __TEXT.__auth_stubs: 0x2020
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x2234
-  __TEXT.__constg_swiftt: 0xa9c
-  __TEXT.__swift5_typeref: 0x4e2e
-  __TEXT.__cstring: 0x411f
+  __TEXT.__const: 0x2604
+  __TEXT.__constg_swiftt: 0xac0
+  __TEXT.__swift5_typeref: 0x5030
+  __TEXT.__cstring: 0x478f
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xa92
-  __TEXT.__swift5_fieldmd: 0xad4
+  __TEXT.__swift5_reflstr: 0xb2a
+  __TEXT.__swift5_fieldmd: 0xaec
   __TEXT.__swift5_types: 0xa8
   __TEXT.__objc_classname: 0x62
-  __TEXT.__objc_methname: 0xd92
+  __TEXT.__objc_methname: 0xdf0
   __TEXT.__objc_methtype: 0x297
-  __TEXT.__swift5_capture: 0x420
-  __TEXT.__swift5_assocty: 0x340
+  __TEXT.__swift5_assocty: 0x3d8
+  __TEXT.__swift5_proto: 0x15c
+  __TEXT.__swift5_capture: 0x1d8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_proto: 0x13c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x15e8
-  __TEXT.__eh_frame: 0x136c
-  __DATA_CONST.__auth_got: 0x1030
-  __DATA_CONST.__got: 0x5f0
-  __DATA_CONST.__auth_ptr: 0xb8
-  __DATA_CONST.__const: 0x24e0
+  __TEXT.__unwind_info: 0x2334
+  __TEXT.__eh_frame: 0x1e24
+  __DATA_CONST.__auth_got: 0x1010
+  __DATA_CONST.__got: 0x610
+  __DATA_CONST.__auth_ptr: 0xd8
+  __DATA_CONST.__const: 0x2208
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xb60
-  __DATA.__objc_selrefs: 0x2f0
+  __DATA.__objc_selrefs: 0x2e8
   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x118
-  __DATA.__objc_data: 0x170
-  __DATA.__data: 0x2c48
-  __DATA.__bss: 0x2908
-  __DATA.__common: 0x198
+  __DATA.__objc_data: 0x188
+  __DATA.__data: 0x2e50
+  __DATA.__bss: 0x2d38
+  __DATA.__common: 0x1e8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CD8ED61C-6ACE-3641-AB80-09796C9EC4F8
-  Functions: 1613
-  Symbols:   230
-  CStrings:  547
+  UUID: E0A3B169-6C5F-3246-B7DE-E5C3F13AA6A3
+  Functions: 1726
+  Symbols:   226
+  CStrings:  569
 
Symbols:
+ _HFHomePrivateURLScheme
+ _HFHomeURLScheme
+ _OBJC_CLASS_$_HMAppleMediaAccessoryPowerAction
+ _OBJC_CLASS_$_HMExecuteRequest
+ _OBJC_CLASS_$_HMExecuteTurnOffRequest
+ _OBJC_CLASS_$_HMRequestBase
- _OBJC_CLASS_$_HMCharacteristicWriteAction
- _OBJC_CLASS_$_OS_dispatch_queue
- _OBJC_CLASS_$_UIDevice
- _OBJC_CLASS_$_UIScreen
- _dispatch_group_create
- _objc_retain_x9
- _swift_continuation_throwingResume
- _swift_continuation_throwingResumeWithError
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
CStrings:
+ "%s (%@) does not have either a specified home or \"current\" among (%s"
+ "%s Current action set stated: %s"
+ "%s Failed action sets: %s"
+ "%s Failed to get current action set state with error: %@"
+ "%s Failed to get current action set states with error: %@"
+ "%s Finalized entities: %s"
+ "%s Generating suggested entities for all accessories and scenes in home %s"
+ "%s Generating suggested entities in home %s matching with string %s"
+ "%s Generating suggested entities in recommended (%s) home %s matching with identifiers %s"
+ "%s Getting Snapshot for interactive widgets... - ended"
+ "%s Getting Snapshot for interactive widgets... - started"
+ "%s Ignoring action set %s with unsupportedActions (media playback, apple media accessory etc)."
+ "%s Loading Timeline for interactive widgets... - ended"
+ "%s Loading Timeline for interactive widgets... - started"
+ "%s Looking for configuration accessories %s"
+ "%s Monitoring characteristics for entities: %s"
+ "%s Returning current home %@"
+ "%s Returning nil"
+ "%s fetching state for action set %s"
+ "%s found homes %s"
+ "%s matched homes %s"
+ "%s widget configuration has home %s"
+ "Created entity with widgetInfo: %s - service: %@ statusString: %s and characteristic data: %s"
+ "Error: Asked for %ld action sets but got %ld back instead, missing: %s"
+ "Error: Asked for %ld characteristics but got %ld back instead, missing: %s"
+ "Executing actionSets: %s"
+ "HFActionSetDescriptionFailedExecution"
+ "Home app destination URL"
+ "HomeWidget/Entities+Samples.swift"
+ "OpenURLInHomeIntent %s - url is %s"
+ "OpenURLInHomeIntent - URL does not appear to be a Home app URL"
+ "Returning manager %@"
+ "WidgetHomePicker"
+ "Write request complete."
+ "accessoriesAndScenes(configuration:context:)"
+ "actionSet"
+ "com.apple.Home://"
+ "defaultActivePowerState: %s powerState: %{bool}d"
+ "didExecutionFailByActionSetUniqueIdentifier"
+ "doorWindowAndWindowConvering: service UUID: %s  obstructionDetected"
+ "doorWindowAndWindowConvering: serviceKind: %s service UUID: %s targetPosition: %ld currentPosition: %ld"
+ "executeRequestWithActionSet:"
+ "fanActivated: %s rotationSpeedValue: %ld"
+ "faucet: %s active: %{bool}d"
+ "fetchPredictions(homeManager:home:)"
+ "fetchStateForActionSets:completion:"
+ "garageDoorOpener: %s currentValue: %ld targetValue: %ld"
+ "garageDoorOpener: %s obstructionDetected"
+ "heaterCooler: %s currentHeaterCoolerState: %ld targetHeaterCoolerState: %ld"
+ "humidifierDehumidifier: %s active: %{bool}d"
+ "humidifierDehumidifier: %s humidifierThreshold: %s dehumidifierThreshold: %s"
+ "irrigationSystem: %s active: %{bool}d inUse: %{bool}d programMode: %ld"
+ "isOnByActionSetUniqueIdentifier"
+ "itemCollection(homeIdentifier:matchingString:)"
+ "lightbulb: %s brightnessValue: %ld"
+ "lockMechanism: %s currentValue: %ld targetValue: %ld"
+ "monitorActionSetsAndUpdateEntitiesWithCachedValues(entities:for:homeManager:)"
+ "monitorAndFetchStateForActionSets:widgetIdentifier:kind:completion:"
+ "monitorCharacteristicsAndUpdateEntitiesWithCachedValues(entities:for:homeManager:)"
+ "monitorStateAndUpdateEntitiesWithCachedValues(_:for:homeManager:)"
+ "performRequests:forKind:completion:"
+ "sceneAndAccessoryUUIDs(for:homeManager:)"
+ "securitySystem: %s currentValue: %ld"
+ "securitySystem: %s targetValue: %ld"
+ "snapshot(for:in:)"
+ "thermostat: %s targetHeatingCoolingMode: %ld currentHeatingCooling: %ld"
+ "timeline(for:in:)"
+ "v24@?0@\"HMWidgetManagerFetchStateForActionSetsResponse\"8@\"NSError\"16"
+ "v24@?0@\"HMWidgetManagerMonitorActionSetsResponse\"8@\"NSError\"16"
+ "valve: %s active: %{bool}d inUse: %{bool}d"
+ "widgetIntentConfiguration"
- "%s (%@) does not have a \"current\" home among (%s"
- "%s Generating suggested entities for all accessories and scenes in current home.."
- "%s Generating suggested entities for matching with identifiers %s"
- "%s Generating suggested entities matching with string %s"
- "%s Getting Snapshot for interactive widgets..."
- "%s Ignoring action set %s with hasPlaybackActions."
- "%s Loading Timeline for interactive widgets..."
- "00000025-0000-1000-8000-0026BB765291"
- "000000B0-0000-1000-8000-0026BB765291"
- "Accessory or Scene"
- "Characteristic write complete."
- "Completion block with homeManager %@ containing homes %s"
- "Error when 'undoing' an actionSet %s: %@"
- "Error: Asked for %ld characteristics but got %ld back instead"
- "Executing %s %s"
- "HomeApp"
- "HomeWidget/Entities.swift"
- "InteractiveWidgets"
- "OpenURLInHomeIntent %s - info is %s"
- "OpenURLInHomeIntent - Missing URL"
- "Widgets"
- "accessoriesAndScenesInCurrentHome(configuration:context:completion:)"
- "allAccessoriesAndScenes(allHomes:matching:)"
- "bounds"
- "doorWindowAndWindowConvering: obstructionDetected"
- "doorWindowAndWindowConvering: serviceKind: %s targetPosition: %ld currentPosition: %ld"
- "executeActionSet:completionHandler:"
- "fetchCharacteristics()"
- "garageDoorOpener: currentValue: %ld targetValue: %ld"
- "garageDoorOpener: obstructionDetected"
- "getSnapshot(for:in:completion:)"
- "getTimeline(for:in:completion:)"
- "heaterCooler: currentHeaterCoolerState: %ld targetHeaterCoolerState: %ld"
- "home"
- "homeInteractiveWidgets"
- "irrigationSystem: active: %{bool}d inUse: %{bool}d programMode: %ld"
- "itemCollection(allHomes:matchingString:)"
- "lockMechanism: currentValue: %ld targetValue: %ld"
- "mainScreen"
- "monitorCharacteristicsAndUpdateEntitiesWithCachedValues(_:for:homeManager:completion:)"
- "new_accessory_controls"
- "performWriteRequests:forKind:completion:"
- "redesign_media"
- "targetValue"
- "template_based_ui"
- "userInterfaceIdiom"
- "v8@?0"
- "valve: active: %{bool}d inUse: %{bool}d"
- "writeValue:completionHandler:"

```
