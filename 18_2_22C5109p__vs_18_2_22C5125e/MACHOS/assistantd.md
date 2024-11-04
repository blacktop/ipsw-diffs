## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3402.62.3.1.2
-  __TEXT.__text: 0x368304
-  __TEXT.__auth_stubs: 0x3450
-  __TEXT.__objc_stubs: 0x45020
-  __TEXT.__objc_methlist: 0x1d2ec
+3402.71.2.0.0
+  __TEXT.__text: 0x368e6c
+  __TEXT.__auth_stubs: 0x3460
+  __TEXT.__objc_stubs: 0x452a0
+  __TEXT.__objc_methlist: 0x1d3d4
   __TEXT.__const: 0x109a0
-  __TEXT.__gcc_except_tab: 0x4748
-  __TEXT.__cstring: 0x50dc4
-  __TEXT.__oslogstring: 0x3e4de
-  __TEXT.__objc_classname: 0x516f
-  __TEXT.__objc_methname: 0x5d3a1
-  __TEXT.__objc_methtype: 0xeea5
-  __TEXT.__dlopen_cstrs: 0xa2c
+  __TEXT.__gcc_except_tab: 0x4794
+  __TEXT.__cstring: 0x50dfe
+  __TEXT.__oslogstring: 0x3e697
+  __TEXT.__objc_classname: 0x5175
+  __TEXT.__objc_methname: 0x5d680
+  __TEXT.__objc_methtype: 0xef2c
+  __TEXT.__dlopen_cstrs: 0xa9c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xa368
+  __TEXT.__unwind_info: 0xa3a0
   __TEXT.__eh_frame: 0xe70
-  __DATA_CONST.__auth_got: 0x1a38
-  __DATA_CONST.__got: 0x3b10
+  __DATA_CONST.__auth_got: 0x1a40
+  __DATA_CONST.__got: 0x3b38
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x14f30
-  __DATA_CONST.__cfstring: 0x12480
+  __DATA_CONST.__const: 0x14ea8
+  __DATA_CONST.__cfstring: 0x124e0
   __DATA_CONST.__objc_classlist: 0xd18
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x6d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xae8
+  __DATA_CONST.__objc_superrefs: 0xaf0
   __DATA_CONST.__objc_arraydata: 0x3c0
   __DATA_CONST.__objc_arrayobj: 0x1c8
   __DATA_CONST.__objc_intobj: 0x828
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x3ce60
-  __DATA.__objc_selrefs: 0x13d78
-  __DATA.__objc_ivar: 0x25d4
+  __DATA.__objc_const: 0x3cf50
+  __DATA.__objc_selrefs: 0x13e28
+  __DATA.__objc_ivar: 0x25e0
   __DATA.__objc_data: 0x82f0
-  __DATA.__data: 0x6048
-  __DATA.__bss: 0xe20
+  __DATA.__data: 0x6030
+  __DATA.__bss: 0xde0
   __DATA.__common: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14377
-  Symbols:   2880
-  CStrings:  26988
+  Functions: 14389
+  Symbols:   2886
+  CStrings:  27031
 
Symbols:
+ _AFSiriServiceStreamName
+ _OBJC_CLASS_$_AFLocationFetchRequest
+ _OBJC_CLASS_$_SSRRPISampledAudioUploader
+ _OBJC_CLASS_$_SSRRPISampler
+ _SANotificationSourceNOTIFICATION_CENTERValue
+ _objc_opt_self
CStrings:
+ "\x12\x12"
+ "\x1f\x06"
+ "%!s(MISSING) #ODD: prompt=%!d(MISSING)"
+ "%!s(MISSING) #ODD: type=%!d(MISSING)"
+ "%!s(MISSING) Cached location accuracy is not satisfying requested accuracy of %!f(MISSING) and request style is 'default'"
+ "%!s(MISSING) Cached location is not empty and request style is 'eager'"
+ "%!s(MISSING) Cached location satisfies fetch request"
+ "%!s(MISSING) Cached location satisfies requested accuracy %!f(MISSING) and request style is 'default'"
+ "%!s(MISSING) Canceling location update session teardown timer"
+ "%!s(MISSING) Drain location is called with no location and no error, this situation should not be possible"
+ "%!s(MISSING) No active assertions, releasing the audio session"
+ "%!s(MISSING) No cached location and request style is 'default'"
+ "%!s(MISSING) Notification from locked app: %!@(MISSING) received, but show previews is enabled"
+ "%!s(MISSING) Starting location monitoring routine with accuracy of %!f(MISSING)"
+ "%!s(MISSING) voice record: %!@(MISSING)"
+ "-[ADAssistantProperties _getChatGPTAccountType]"
+ "-[ADAssistantProperties _getIsChatGPTSetUpPrompts]"
+ "-[ADCloudKitSharedZoneUpdater fetchValueForKeyFromSharedStore:withQOS:completion:]_block_invoke"
+ "-[ADCloudKitSharedZoneUpdater fetchValuesForKeysFromSharedStore:withQOS:completion:]_block_invoke"
+ "-[ADCloudKitShareeOperations fetchZones:]"
+ "-[ADLocationManager currentLocationWithFetchRequest:completion:]"
+ "-[ADLocationManager currentLocationWithFetchRequest:completion:]_block_invoke"
+ "-[ADSpeechManager deactivateAudioSessionIfNoActiveAssertions]_block_invoke"
+ "36"
+ "ADLocationFetchRequest"
+ "MobileAssistantDaemons-3402.71.2"
+ "T@\"NSString\",C,N,V_perceptionIdentifier"
+ "T@\"NSString\",C,N,V_personaId"
+ "TQ,N,V_style"
+ "Vv32@0:8@\"AFLocationFetchRequest\"16@?<v@?@\"CLLocation\"@\"NSError\">24"
+ "_attachPersonaIdIfNeeded:aceCommand:"
+ "_getChatGPTAccountType"
+ "_getIsChatGPTSetUpPrompts"
+ "_perceptionIdentifier"
+ "_personaId"
+ "_style"
+ "accountType"
+ "currentLocationWithFetchRequest:completion:"
+ "deactivateAudioSessionIfNoActiveAssertions"
+ "deleteAllRPISampledData"
+ "fetchValueForKeyFromSharedStore:container:withQOS:completion:"
+ "fetchValueForKeyFromSharedStore:withQOS:completion:"
+ "fetchValuesForKeysFromSharedStore:withQOS:completion:"
+ "initWithClientFetchRequest:completion:"
+ "isDeviceUnlocked"
+ "notificationSettings"
+ "notificationSourceWithIdentifier:"
+ "perceptionIdentifier"
+ "purgeOldAudioData"
+ "setChatGPTAccountType:"
+ "setIsChatGPTSetUpPrompts:"
+ "setPerceptionIdentifier:"
+ "setPersonaId:"
+ "setStyle:"
+ "setupPrompt"
+ "showPreviewsSetting"
+ "siri.service"
+ "sourceSettings"
+ "style"
+ "v32@0:8@\"AFLocationFetchRequest\"16@?<v@?@\"CLLocation\"@\"NSError\">24"
- "%!s(MISSING) Cached location accuracy is not satisfying requested accuracy of %!f(MISSING), starting location monitoring routine"
- "%!s(MISSING) Cached location satisfies requested accuracy %!f(MISSING)"
- "%!s(MISSING) Cancelling location update session teardown timer"
- "%!s(MISSING) No cached location, starting location monitoring routine with accuracy of %!f(MISSING)"
- "-[ADCloudKitSharedZoneUpdater fetchValueForKeyFromSharedStore:completion:]_block_invoke"
- "-[ADCloudKitSharedZoneUpdater fetchValuesForKeysFromSharedStore:completion:]_block_invoke"
- "-[ADLocationManager currentLocationWithAccuracy:timeout:completion:]"
- "-[ADLocationManager currentLocationWithAccuracy:timeout:completion:]_block_invoke"
- "/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet"
- "/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext"
- "2"
- "AFLocationFetchRequest"
- "MobileAssistantDaemons-3402.62.3.1.2"
- "_CDContextQueries"
- "_DKSiriServiceMetadataKey"
- "_DKSystemEventStreams"
- "commandKey"
- "domainKey"
- "keyPathForSiriServiceDataDictionary"
- "siriServiceStream"

```
