## PhotosMediaFoundation

> `/System/Library/PrivateFrameworks/PhotosMediaFoundation.framework/PhotosMediaFoundation`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0x22f8
-  __TEXT.__auth_stubs: 0x3c0
+910.14.107.0.0
+  __TEXT.__text: 0x22f0
   __TEXT.__objc_methlist: 0x42c
   __TEXT.__swift5_typeref: 0x2b
   __TEXT.__const: 0xb8

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x2d3
-  __TEXT.__oslogstring: 0x1a2
-  __TEXT.__unwind_info: 0x168
-  __TEXT.__objc_classname: 0x174
-  __TEXT.__objc_methname: 0xa18
-  __TEXT.__objc_methtype: 0x386
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__gcc_except_tab: 0xb0
+  __TEXT.__cstring: 0x30d
+  __TEXT.__oslogstring: 0x1e6
+  __TEXT.__unwind_info: 0x178
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1f0
-  __AUTH_CONST.__const: 0xd8
+  __DATA_CONST.__got: 0xa0
+  __AUTH_CONST.__const: 0xf8
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x8a0
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x258
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A5C778DF-F279-3504-BED2-62DE89A2E3B5
-  Functions: 72
-  Symbols:   421
-  CStrings:  217
+  UUID: 1AC065A1-9097-3505-9AF9-52D6680409FB
+  Functions: 73
+  Symbols:   430
+  CStrings:  47
 
Symbols:
+ ___70-[AVPlayerItem(PhotosMediaFoundation) queryHasCaptionsWithCompletion:]_block_invoke_2
+ ___block_literal_global.121
+ ___block_literal_global.152
+ __block_invoke.captions_log
+ __block_invoke.onceToken
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_PhotosMediaFoundation
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _sNextEventID
- _OBJC_CLASS_$_NSDate
- ___block_literal_global.124
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_PhotosMediaFoundation
- _objc_msgSend$date
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ "VideoCaptions"
+ "com.photos.PhotosMediaFoundation"
+ "loadMediaSelectionGroupForMediaCharacteristic failed with error: %@"
- "#16@0:8"
- ".cxx_destruct"
- ":"
- "@"
- "@\"<PXAVAudioSession>\""
- "@\"<PXAVResourceReclamationAssertion>\"24@0:8@\"NSString\"16"
- "@\"<PXAVResourceReclamationController>\""
- "@\"<PXAVResourceReclamationEvent>\""
- "@\"<PXAVResourceReclamationEvent>\"16@0:8"
- "@\"AVResourceReclamationController\""
- "@\"AVResourceReclamationEventObserverToken\""
- "@\"NSHashTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PXSystemAVResourceReclamationController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24:32"
- "@?"
- "AVResourceReclamationObservable"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8q16^@24"
- "NSObject"
- "PXAVAudioSession"
- "PXAVAudioSessionController"
- "PXAVResourceReclamationController"
- "PXAVResourceReclamationObserver"
- "PXConcreteAVResourceReclamationController"
- "PXManualAVResourceReclamationController"
- "PXResourceReclamationObservation"
- "PXSystemAVResourceReclamationController"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<PXAVAudioSession>\",&,N,S_audioSessionQueue_setAudioSession:,V_audioSession"
- "T@\"<PXAVResourceReclamationController>\",R,W,N,V_controller"
- "T@\"<PXAVResourceReclamationEvent>\",R,N"
- "T@\"<PXAVResourceReclamationEvent>\",R,N,V_mostRecentReclamationEvent"
- "T@\"AVResourceReclamationController\",R,N,V_systemController"
- "T@\"AVResourceReclamationEventObserverToken\",R,N,V_observerToken"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSObject<OS_os_log>\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_name"
- "T@\"PXSystemAVAudioSessionController\",R,N"
- "TQ,R"
- "TQ,R,N,V_signpostID"
- "Tq,R"
- "Tq,R,N"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_audioSession"
- "_audioSessionQueue_applyCategory:completion:"
- "_audioSessionQueue_applyExistingCategoryToAudioSessionIfNeeded"
- "_audioSessionQueue_setAudioSession:"
- "_category"
- "_categoryLock"
- "_controller"
- "_enumerateObservers:"
- "_eventHandler"
- "_handleMediaServicesWereResetNotification:"
- "_mostRecentReclamationEvent"
- "_name"
- "_observerToken"
- "_observers"
- "_observersQueue"
- "_reclamationController"
- "_selector"
- "_signpostID"
- "_systemController"
- "_target"
- "addObject:"
- "addObserverForName:object:queue:usingBlock:"
- "addReclamationEventObserver:"
- "allObjects"
- "applicationAVAudioSessionController"
- "applyCategory:completion:"
- "asset"
- "audioSession"
- "audioSessionQueue"
- "autorelease"
- "category"
- "class"
- "conformsToProtocol:"
- "controller"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentCategory"
- "currentHandler"
- "date"
- "debugDescription"
- "defaultCenter"
- "defaultController"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasMediaCharacteristic:"
- "hash"
- "init"
- "initWithController:weakTarget:selector:"
- "initWithFormat:"
- "initWithName:audioSession:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "loadMediaSelectionGroupForMediaCharacteristic:completionHandler:"
- "log"
- "mostRecentReclamationEvent"
- "mutableCopy"
- "name"
- "new"
- "numberWithInteger:"
- "observationWithWeakTarget:selector:"
- "observerToken"
- "options"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "permitReclamationWhileSuspended"
- "photosAudioSessionCategory"
- "q"
- "q16@0:8"
- "queryHasCaptionsWithCompletion:"
- "reclaimResources"
- "reclamationController:didReclaimObjectsWithEvent:"
- "reclamationEventDidOccur:"
- "registerObserver:"
- "release"
- "removeObject:"
- "resourceReclamationEventDidOccur:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setCategory:error:"
- "setCurrentCategory:"
- "setMostRecentReclamationEvent:"
- "setObject:forKeyedSubscript:"
- "setPhotosAudioSessionCategory:error:"
- "sharedInstance"
- "signpostID"
- "superclass"
- "systemController"
- "takeAssertionPreventingResourceReclamationWithReason:"
- "unregisterObserver:"
- "v16@0:8"
- "v24@0:8@\"<PXAVResourceReclamationObserver>\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@0:8@\"AVResourceReclamationController\"16@\"AVResourceReclamationEvent\"24"
- "v32@0:8@16@24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?B@\"NSError\">24"
- "weakObjectsHashTable"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
