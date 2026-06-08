## SiriModes

> `/System/Library/PrivateFrameworks/SiriModes.framework/SiriModes`

```diff

 3402.3.1.0.0
-  __TEXT.__text: 0x3f74
-  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__text: 0x3ac0
   __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x508
+  __TEXT.__cstring: 0x50e
   __TEXT.__oslogstring: 0x7e5
   __TEXT.__unwind_info: 0x100
-  __TEXT.__objc_classname: 0xa9
-  __TEXT.__objc_methname: 0x9f5
-  __TEXT.__objc_methtype: 0xf9
-  __TEXT.__objc_stubs: 0xd60
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3a8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x598
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9C117BF-F01B-362B-B237-EF11B2DDDE37
-  Functions: 54
-  Symbols:   362
-  CStrings:  253
+  UUID: 25EAAE28-4879-32F5-A543-0DF55F6BC38F
+  Functions: 53
+  Symbols:   364
+  CStrings:  97
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _OUTLINED_FUNCTION_1
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"AFNotifyObserver\""
- "@\"AVOutputContext\""
- "@\"MDModeDecision\""
- "@\"MDModeDecision\"16@0:8"
- "@\"NSUserDefaults\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@36@0:8@16Q24B32"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "MDAudioAccessoryHeuristic"
- "MDDeviceIsMutedHeuristic"
- "MDDialogTransformer"
- "MDFixedModeProvider"
- "MDModeDecision"
- "MDModeHeuristic"
- "MDModeProviding"
- "MDUserOverrideHeuristic"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T@\"NSDictionary\",&,N"
- "TQ,R,N,V_currentMode"
- "_addViewsForAddDialogs:views:"
- "_alwaysPrintSiriResponse"
- "_analytics"
- "_configurationDictionary"
- "_connectedOutputDevicesDidChange:"
- "_connectedOutputDevicesObserver"
- "_connectedToAudioAccessory"
- "_currentMode"
- "_displayOnlyModeDecision"
- "_fetchConnectedAudioAccessoryState"
- "_firstSnippetInViews:"
- "_fixedMode"
- "_internalDefaults"
- "_logModeComputationForAceCommand:mode:"
- "_modeDecisionBasedOnAudioAccessory"
- "_redundantDUCIds"
- "_removeRedundantUtteranceViewsFromAddViews:forMode:"
- "_removeSpeakableTextFromAddViews:forMode:"
- "_removeUtteranceViewsFromAddViews:forMode:"
- "_ringerStateObserver"
- "_sayItForDialog:"
- "_sharedSystemAudioContext"
- "_shouldTransformLegacyAddViews"
- "_speakableTextForDialog:mode:"
- "_transformDialogAddViews:forMode:"
- "_transformLegacyAddViews:forMode:"
- "_utteranceViewForDialog:mode:printedOnly:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "arrayWithObjects:count:"
- "boolValue"
- "bundleForClass:"
- "canUseServerTTS"
- "caption"
- "componentsJoinedByString:"
- "configuration"
- "containsObject:"
- "content"
- "context"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentMode"
- "defaultCenter"
- "determineCurrentMode"
- "deviceType"
- "dialog"
- "dialogCategory"
- "dialogIdentifier"
- "dialogs"
- "dictionary"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "encodedClassName"
- "gender"
- "init"
- "initWithFixedMode:"
- "initWithInternalDefaults:"
- "initWithMode:"
- "initWithName:options:queue:delegate:"
- "initWithRingerStateObserver:"
- "initWithSuiteName:"
- "internalModeOverride"
- "isConnectedToAudioAccessory"
- "isDeviceSilentMode"
- "isEqualToString:"
- "items"
- "languageCode"
- "lastObject"
- "length"
- "listenAfterSpeaking"
- "listenAfterSpeakingBehavior"
- "logEventWithType:context:"
- "lowercaseString"
- "metricsContext"
- "objectForKeyedSubscript:"
- "outputDevices"
- "pathForResource:ofType:"
- "printedOnly"
- "refId"
- "setAceId:"
- "setCanUseServerTTS:"
- "setContext:"
- "setDialogCategory:"
- "setDialogIdentifier:"
- "setDialogIdentifiers:"
- "setGender:"
- "setItems:"
- "setLanguageCode:"
- "setListenAfterSpeaking:"
- "setListenAfterSpeakingBehavior:"
- "setMessage:"
- "setMetricsContext:"
- "setObject:forKey:"
- "setRefId:"
- "setSpeakableDelimiter:"
- "setSpeakableFinalDelimiter:"
- "setSpeakableSuffix:"
- "setSpeakableText:"
- "setText:"
- "setViews:"
- "setWithCapacity:"
- "sharedAnalytics"
- "sharedPreferences"
- "sharedSystemAudioContext"
- "siriResponseShouldAlwaysPrint"
- "speakableDelimiter"
- "speakableFinalDelimiter"
- "speakableSuffix"
- "speakableText"
- "speakableTextOverride"
- "spokenOnly"
- "state"
- "stringByAppendingString:"
- "stringForKey:"
- "supportsTransformationForAceCommand:"
- "text"
- "transformAddDialogs:forMode:"
- "transformAddViews:forMode:"
- "typeOfAddViews:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16Q24"
- "views"

```
