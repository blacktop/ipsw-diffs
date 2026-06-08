## AppleHIDFeedback

> `/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback`

```diff

-13.0.0.0.0
-  __TEXT.__text: 0x525c
-  __TEXT.__auth_stubs: 0x430
+14.0.0.0.0
+  __TEXT.__text: 0x4b44
   __TEXT.__objc_methlist: 0x324
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x818
+  __TEXT.__cstring: 0x823
   __TEXT.__oslogstring: 0x685
-  __TEXT.__gcc_except_tab: 0x2ec
-  __TEXT.__unwind_info: 0x200
-  __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0xc28
-  __TEXT.__objc_methtype: 0x1b3
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__gcc_except_tab: 0x210
+  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x350
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x580
   __AUTH_CONST.__objc_const: 0x580
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x40
   __DATA.__bss: 0x40

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B39AA9C-5576-3051-9037-5F5486347B4B
+  UUID: 85042487-FB72-3CD3-9BA2-0AA4CB29597E
   Functions: 91
-  Symbols:   434
-  CStrings:  319
+  Symbols:   436
+  CStrings:  154
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke.25
+ ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke.36
+ ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke.14
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addObject:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$removeObject:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _OBJC_CLASS_$_NSMutableIndexSet
- ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke.24
- ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke.35
- ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke.13
- _objc_msgSend$addIndex:
- _objc_msgSend$containsIndex:
- _objc_msgSend$removeIndex:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x25
- _objc_retain_x27
Functions:
~ -[AHFPencilPatternLibrary init] : 1048 -> 940
~ ___31-[AHFPencilPatternLibrary init]_block_invoke : 64 -> 60
~ -[AHFPencilPatternLibrary waveformIndexWithType:] : 140 -> 136
~ -[AHFPencilPatternLibrary createPatternsLibraryFrom:] : 3120 -> 2896
~ -[AHFPencilPatternLibrary getReportForPattern:timestampUs:prevTimestampUs:error:] : 600 -> 572
~ -[AHFPencilPatternLibrary isReport:equalTo:] : 180 -> 176
~ -[AHFPencilPatternLibrary maybeGetExploratoryPayload:] : 620 -> 604
~ -[AHFPencilPatternLibrary setLibrary:] : 64 -> 12
~ _failure : 300 -> 288
~ _LoggingFramework : 84 -> 68
~ +[AHFManager sharedInstance] : 176 -> 160
~ -[AHFManager setTrackpadController:] : 64 -> 12
~ -[AHFManager setPencilController:] : 64 -> 12
~ ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke : 432 -> 404
~ ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke.13 -> ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke.14 : 272 -> 252
~ ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke : 432 -> 404
~ ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke.24 -> ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke.25 : 272 -> 252
~ ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke : 452 -> 400
~ ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke.35 -> ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke.36 : 264 -> 216
~ -[AHFPencilController playFeedbackGated:haptics:timestamp:error:] : 552 -> 496
~ -[AHFPencilController playFeedback:senderID:timestamp:error:] : 624 -> 568
~ ___61-[AHFPencilController playFeedback:senderID:timestamp:error:]_block_invoke : 472 -> 524
~ -[AHFPencilController playFeedback:accessoryID:timestamp:error:] : 640 -> 592
~ ___64-[AHFPencilController playFeedback:accessoryID:timestamp:error:]_block_invoke : 452 -> 440
~ -[AHFPencilController setPatternsLibrary:] : 64 -> 12
~ -[AHFPencilController setQueue:] : 64 -> 12
~ -[AHFPencilController setDigitizerStylusClient:] : 64 -> 12
~ -[AHFPencilController setAvailableDigitizerStylus:] : 64 -> 12
~ -[AHFPencilController setOpaqueTouchClient:] : 64 -> 12
~ -[AHFPencilController setAvailableOpaqueTouch:] : 64 -> 12
~ -[AHFPencilController setPencilHapticsClient:] : 64 -> 12
~ -[AHFTrackpadController dealloc] : 120 -> 112
~ -[AHFTrackpadController initializeTrackpadSystem] : 724 -> 696
~ ___49-[AHFTrackpadController initializeTrackpadSystem]_block_invoke : 472 -> 408
~ ___49-[AHFTrackpadController initializeTrackpadSystem]_block_invoke.16 : 308 -> 252
~ -[AHFTrackpadController getActuationIdForPattern:] : 372 -> 368
~ -[AHFTrackpadController playFeedbackGated:client:timestamp:error:] : 492 -> 444
~ -[AHFTrackpadController playFeedback:senderID:timestamp:error:] : 624 -> 568
~ ___63-[AHFTrackpadController playFeedback:senderID:timestamp:error:]_block_invoke : 328 -> 308
~ -[AHFTrackpadController playFeedback:accessoryID:timestamp:error:] : 768 -> 720
~ ___66-[AHFTrackpadController playFeedback:accessoryID:timestamp:error:]_block_invoke : 456 -> 440
~ -[AHFTrackpadController setQueue:] : 64 -> 12
~ -[AHFTrackpadController setTrackpadClient:] : 64 -> 12
~ -[AHFTrackpadController setAvailableTrackpads:] : 64 -> 12
~ -[AHFPencilPatternLibrary init].cold.1 : 140 -> 96
CStrings:
- ".cxx_destruct"
- "@\"AHFPencilController\""
- "@\"AHFPencilPatternLibrary\""
- "@\"AHFTrackpadController\""
- "@\"HIDEventSystemClient\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableIndexSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@16@0:8"
- "@24@0:8@16"
- "@48@0:8@16Q24Q32o^@40"
- "AHFManager"
- "AHFPencilController"
- "AHFPencilPatternLibrary"
- "AHFTrackpadController"
- "B16@0:8"
- "B32@0:8@16@24"
- "B48@0:8@16@24Q32o^@40"
- "B48@0:8@16Q24Q32o^@40"
- "I"
- "I16@0:8"
- "Q16@0:8"
- "T@\"AHFPencilController\",&,N,V_pencilController"
- "T@\"AHFPencilPatternLibrary\",&,N,V_patternsLibrary"
- "T@\"AHFTrackpadController\",&,N,V_trackpadController"
- "T@\"HIDEventSystemClient\",&,N,V_digitizerStylusClient"
- "T@\"HIDEventSystemClient\",&,N,V_opaqueTouchClient"
- "T@\"HIDEventSystemClient\",&,N,V_pencilHapticsClient"
- "T@\"HIDEventSystemClient\",&,N,V_trackpadClient"
- "T@\"NSDictionary\",&,N,V_library"
- "T@\"NSMutableDictionary\",&,N,V_availableTrackpads"
- "T@\"NSMutableIndexSet\",&,N,V_availableDigitizerStylus"
- "T@\"NSMutableIndexSet\",&,N,V_availableOpaqueTouch"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "TI,N,V_availablePencilHaptics"
- "TQ,N,V_prevTimestampUs"
- "URLsForResourcesWithExtension:subdirectory:"
- "_availableDigitizerStylus"
- "_availableOpaqueTouch"
- "_availablePencilHaptics"
- "_availableTrackpads"
- "_digitizerStylusClient"
- "_library"
- "_opaqueTouchClient"
- "_patternsLibrary"
- "_pencilController"
- "_pencilHapticsClient"
- "_prevTimestampUs"
- "_queue"
- "_trackpadClient"
- "_trackpadController"
- "activate"
- "addEntriesFromDictionary:"
- "addIndex:"
- "allKeys"
- "allPatterns"
- "allValues"
- "availableDigitizerStylus"
- "availableOpaqueTouch"
- "availablePencilHaptics"
- "availableTrackpads"
- "bundleForClass:"
- "bytes"
- "cancel"
- "containsIndex:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createPatternsLibraryFrom:"
- "dataWithBytes:length:"
- "dealloc"
- "defaultManager"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "digitizerStylusClient"
- "errorWithDomain:code:userInfo:"
- "fileURLWithPath:"
- "filteredArrayUsingPredicate:"
- "getActuationIdForPattern:"
- "getReportForPattern:timestampUs:prevTimestampUs:error:"
- "hasPrefix:"
- "i24@0:8@16"
- "i44@0:8@16I24Q28o^@36"
- "i48@0:8@16@24Q32o^@40"
- "i48@0:8@16Q24Q32o^@40"
- "init"
- "initWithFormat:arguments:"
- "initWithType:"
- "initializeDigitizerStylusSystem"
- "initializeOpaqueTouchSystem"
- "initializePencilHapticsSystem"
- "initializeTrackpadSystem"
- "integerValue"
- "isEqual:"
- "isEqualToData:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isReport:equalTo:"
- "keysOfEntriesPassingTest:"
- "lastPathComponent"
- "length"
- "library"
- "lowercaseString"
- "maybeGetExploratoryPayload:"
- "mutableBytes"
- "mutableCopy"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "opaqueTouchClient"
- "patternsLibrary"
- "pencilController"
- "pencilHapticsClient"
- "playFeedback:accessoryID:timestamp:error:"
- "playFeedback:powerSourceID:timestamp:error:"
- "playFeedback:senderID:timestamp:error:"
- "playFeedbackGated:client:timestamp:error:"
- "playFeedbackGated:haptics:timestamp:error:"
- "predicateWithFormat:"
- "prevTimestampUs"
- "propertyForKey:"
- "queue"
- "removeIndex:"
- "removeObjectForKey:"
- "serviceID"
- "services"
- "setAvailableDigitizerStylus:"
- "setAvailableOpaqueTouch:"
- "setAvailablePencilHaptics:"
- "setAvailableTrackpads:"
- "setDigitizerStylusClient:"
- "setDispatchQueue:"
- "setLibrary:"
- "setMatching:"
- "setObject:forKeyedSubscript:"
- "setOpaqueTouchClient:"
- "setPatternsLibrary:"
- "setPencilController:"
- "setPencilHapticsClient:"
- "setPrevTimestampUs:"
- "setProperty:forKey:"
- "setQueue:"
- "setRemovalHandler:"
- "setServiceNotificationHandler:"
- "setTrackpadClient:"
- "setTrackpadController:"
- "setValue:forKey:"
- "sharedInstance"
- "stringByDeletingPathExtension"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "trackpadClient"
- "trackpadController"
- "unsignedIntValue"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "valueForKey:"
- "waveformIndexWithType:"

```
