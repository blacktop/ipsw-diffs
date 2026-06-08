## Communications-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0xbe50
-  __TEXT.__auth_stubs: 0x5b0
+1176.0.26.502.1
+  __TEXT.__text: 0xb108
   __TEXT.__objc_methlist: 0x5b4
-  __TEXT.__cstring: 0xae7
+  __TEXT.__cstring: 0xae9
   __TEXT.__const: 0x7c
   __TEXT.__oslogstring: 0xca4
   __TEXT.__ustring: 0xa
-  __TEXT.__gcc_except_tab: 0x1f0
-  __TEXT.__unwind_info: 0x388
-  __TEXT.__objc_classname: 0x137
-  __TEXT.__objc_methname: 0x14be
-  __TEXT.__objc_methtype: 0x272
-  __TEXT.__objc_stubs: 0x1a60
-  __DATA_CONST.__got: 0x438
+  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__unwind_info: 0x348
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x800
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x800
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH_CONST.__const: 0xc0
+  __DATA_CONST.__got: 0x438
+  __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0xf00
   __AUTH_CONST.__objc_const: 0x5b0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x300
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8923CCDE-80CB-3E52-B39C-178857905981
-  Functions: 214
-  Symbols:   1233
-  CStrings:  644
+  UUID: 1B3FAFC0-12B3-3CB2-9C98-FEB7BCD5F3C0
+  Functions: 212
+  Symbols:   1236
+  CStrings:  319
 
Symbols:
+ ___block_literal_global.246
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- GCC_except_table166
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"ACCCommunicationsCenter\""
- "@\"CHManager\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8Q16"
- "@\"NSArray\"28@0:8B16Q20"
- "@\"NSDictionary\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"RadiosPreferences\""
- "@\"VMVoicemailManager\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8Q16"
- "@28@0:8B16Q20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "ACCCommunicationsCenterCallControlsDelegate"
- "ACCCommunicationsCenterCallStateDelegate"
- "ACCCommunicationsCenterCommunicationsDelegate"
- "ACCCommunicationsCenterListUpdatesDelegate"
- "ACCCommunicationsFeaturePlugin"
- "ACCFeaturePluginProtocol"
- "ACCPluginProtocol"
- "ACCUserDefaults"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8B16@\"NSString\"20"
- "B28@0:8B16@20"
- "B28@0:8i16@\"NSString\"20"
- "B28@0:8i16@20"
- "B36@0:8@\"NSString\"16i24@\"NSString\"28"
- "B36@0:8@16i24@28"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "Q16@0:8"
- "RadiosPreferencesDelegate"
- "T#,R"
- "T@\"ACCCommunicationsCenter\",&,N,V_commCenter"
- "T@\"CHManager\",&,N,V_chManager"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"RadiosPreferences\",&,N,V_radiosPreferences"
- "T@\"VMVoicemailManager\",&,N,V_vmManager"
- "TB,N,V_isRunning"
- "TB,R,N"
- "TQ,R"
- "URL"
- "UTF8String"
- "Utilities"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_chManager"
- "_commCenter"
- "_isRunning"
- "_queue"
- "_radiosPreferences"
- "_vmManager"
- "acceptCallWithAction:callUUID:"
- "actionType"
- "addListenerID:forService:"
- "addNotificationObservers"
- "addObject:"
- "addObserver:selector:name:object:"
- "airplaneMode"
- "airplaneModeChanged"
- "andPredicateWithSubpredicates:"
- "answerCall:"
- "appendFormat:"
- "array"
- "arrayForKey:"
- "arrayWithObjects:count:"
- "audioOrVideoCallWithStatus:"
- "autorelease"
- "availabilityForListenerID:forService:"
- "base64EncodedStringWithOptions:"
- "boolForKey:"
- "boolValue"
- "bundleIdentifier"
- "bytes"
- "callStateDidChange:"
- "callStateDidChangeForCall:"
- "callStateDidChangeNotification:"
- "callStatus"
- "callType"
- "callUUID"
- "callWithCallUUID:"
- "callWithStatus:"
- "callerId"
- "callerIdSubStringForDisplay"
- "callerNameForDisplay"
- "calls"
- "callsWithPredicate:limit:offset:batchSize:"
- "chManager"
- "characterSetWithCharactersInString:"
- "class"
- "coalescedCallsWithPredicate:limit:offset:batchSize:"
- "commCenter"
- "commStatusDidChange:"
- "commStatusDidChangeNotification:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "conformsToProtocol:"
- "contact"
- "contactIdentifier"
- "contactProperty"
- "containsObject:"
- "copy"
- "copyToKey:fromKey:inDictionary:objectIfNil:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentAudioAndVideoCalls"
- "currentCallCount"
- "currentCallGroups"
- "currentCallStates"
- "currentCarrierName"
- "currentCommunicationsStatus"
- "currentFavoritesListWithLimit:"
- "currentLocalizedCarrierName"
- "currentMuteStatus"
- "currentRecentsListWithCoalescing:limit:"
- "currentRegistrationStatus"
- "currentSignalStrength"
- "currentUnreadVoicemailCount"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithJSONObject:options:error:"
- "date"
- "dateConnected"
- "debugDescription"
- "defaultCenter"
- "defaultWorkspace"
- "description"
- "dialRequestForRecentCall:"
- "dictionary"
- "dictionaryForKey:"
- "dictionaryOfChangesBetween:and:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "disconnectAllCalls"
- "disconnectCall:"
- "disconnectCall:withReason:"
- "disconnectedReason"
- "displayName"
- "doubleForKey:"
- "duration"
- "endActiveAndAnswerCall:"
- "endAllCalls"
- "endCallWithAction:callUUID:"
- "endHeldAndAnswerCall:"
- "entries"
- "faceTimeProvider"
- "favoritesListDidChange"
- "favoritesListDidChangeNotification:"
- "frontmostAudioOrVideoCall"
- "frontmostCall"
- "groupCall:withOtherCall:"
- "handle"
- "handleWithDestinationID:"
- "hash"
- "hexadecimalCharacterSet"
- "holdActiveAndAnswerCall:"
- "holdCall:"
- "i16@0:8"
- "identifier"
- "incomingCall"
- "incomingVideoCall"
- "init"
- "initPlugin"
- "initWithBase64EncodedString:options:"
- "initWithCallStateDelegate:andCommunicationsDelegate:andCallControlsDelegate:andListUpdatesDelegate:"
- "initWithProvider:"
- "initWithSuiteName:"
- "initiateCallToDestination:withService:addressBookID:"
- "initiateCallToVoicemail"
- "initiateRedial"
- "instancesRespondToSelector:"
- "intValue"
- "integerForKey:"
- "integerValue"
- "invertedSet"
- "isAddCallAllowed"
- "isAirplaneModeEnabled"
- "isCellularSupported"
- "isConferenced"
- "isConnected"
- "isEndAndAcceptAvailable"
- "isEqual:"
- "isEqualToString:"
- "isFaceTimeAudioEnabled"
- "isFaceTimeVideoEnabled"
- "isHoldAndAcceptAvailable"
- "isHoldAndAnswerAllowed"
- "isHoldAvailable"
- "isInitiateCallAllowed"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMergeAvailable"
- "isOutgoing"
- "isProxy"
- "isRunning"
- "isScreening"
- "isSwapAvailable"
- "isTelephonyEnabled"
- "isUplinkMuted"
- "isValidJSONObject:"
- "key"
- "label"
- "length"
- "localizedDisplayStringForLabel:propertyName:"
- "localizedLabel"
- "localizedStringForKey:value:table:"
- "mergeCalls"
- "model"
- "mutableCopy"
- "name"
- "notificationWithName:object:"
- "notificationWithName:object:userInfo:"
- "null"
- "numberOfOccurrences"
- "numberWithBool:"
- "numberWithChar:"
- "numberWithInt:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "object"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openURL:withOptions:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "playDTMFToneForKey:"
- "pluginName"
- "predicateForCallsWithAnyMediaTypes:"
- "predicateForCallsWithAnyServiceProviders:"
- "predicateForCallsWithRemoteParticipantCount:"
- "predicateForCallsWithStatusOriginated:"
- "queue"
- "radiosPreferences"
- "raise:format:"
- "recentsListDidChange"
- "recentsListDidChangeNotification:"
- "release"
- "remoteParticipantHandles"
- "removeListenerID:forService:"
- "removeNotificationObservers"
- "removeObserver:name:object:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendDTMF:forCallWithUUID:"
- "service"
- "set"
- "setCallStateDelegate:"
- "setChManager:"
- "setCoalescingStrategy:"
- "setCommCenter:"
- "setContactIdentifier:"
- "setDelegate:"
- "setDialType:"
- "setDouble:forKey:"
- "setHandle:"
- "setInteger:forKey:"
- "setIsRunning:"
- "setObject:forKey:"
- "setObject:forKey:objectIfNil:"
- "setQueue:"
- "setRadiosPreferences:"
- "setUplinkMuted:"
- "setValue:forKey:"
- "setVideo:"
- "setVmManager:"
- "setWithSet:"
- "sharedAudioSystemController"
- "sharedDefaults"
- "sharedDefaultsIapd"
- "sharedDefaultsLogging"
- "sharedInstance"
- "shouldPlayDTMFTone"
- "startPlugin"
- "status"
- "stopPlugin"
- "stringByTrimmingCharactersInSet:"
- "stringForKey:"
- "stringValue"
- "stringWithFormat:"
- "stringWithString:"
- "superclass"
- "supportsGrouping"
- "supportsHolding"
- "supportsTelephonyCalls"
- "swapCalls"
- "telephonyProvider"
- "timeIntervalSince1970"
- "unholdCall:"
- "unreadCount"
- "updateHoldStatus:forCallWithUUID:"
- "updateMuteStatus:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v40@0:8@16@24@32"
- "v48@0:8@16@24@32@40"
- "value"
- "vmManager"
- "voicemailProvider"
- "wasScreened"
- "writeToFile:atomically:"
- "zone"

```
