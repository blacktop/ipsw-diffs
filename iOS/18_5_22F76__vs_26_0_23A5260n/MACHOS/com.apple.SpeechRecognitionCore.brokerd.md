## com.apple.SpeechRecognitionCore.brokerd

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd`

```diff

-6.3.30.10.0
-  __TEXT.__text: 0xddd8
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_stubs: 0x11c0
+6.3.54.0.0
+  __TEXT.__text: 0x10e38
+  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__objc_stubs: 0x13e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x510
-  __TEXT.__const: 0xd1
-  __TEXT.__cstring: 0xe52
-  __TEXT.__oslogstring: 0x1119
-  __TEXT.__gcc_except_tab: 0x45c
-  __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x1259
-  __TEXT.__objc_methtype: 0x224
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x578
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x840
-  __DATA_CONST.__cfstring: 0x10e0
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__objc_methlist: 0x5b4
+  __TEXT.__const: 0x124
+  __TEXT.__cstring: 0xc53
+  __TEXT.__oslogstring: 0x1513
+  __TEXT.__gcc_except_tab: 0x7f4
+  __TEXT.__objc_classname: 0x58
+  __TEXT.__objc_methname: 0x14bc
+  __TEXT.__objc_methtype: 0x29c
+  __TEXT.__swift5_typeref: 0x5d
+  __TEXT.__constg_swiftt: 0x38
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x468
+  __DATA_CONST.__auth_got: 0x6b8
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x938
+  __DATA_CONST.__cfstring: 0xf60
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x548
-  __DATA.__objc_selrefs: 0x508
+  __DATA.__objc_const: 0x4a0
+  __DATA.__objc_selrefs: 0x5e0
   __DATA.__objc_ivar: 0x34
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x220
-  __DATA.__bss: 0x111
-  __DATA.__common: 0x18
+  __DATA.__objc_data: 0x150
+  __DATA.__data: 0x1d8
+  __DATA.__bss: 0xf1
+  __DATA.__common: 0x19
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore
+  - /System/Library/PrivateFrameworks/VoiceControl.framework/VoiceControl
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA98DF02-C750-3160-A1AF-6AE94BB84E71
-  Functions: 251
-  Symbols:   349
-  CStrings:  690
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 5B8E82D2-A3AB-33F3-85E2-8ED1E60E5396
+  Functions: 253
+  Symbols:   307
+  CStrings:  669
 
Symbols:
+ _NSUbiquitousKeyValueStoreChangeReasonKey
+ _NSUbiquitousKeyValueStoreDidChangeExternallyNotification
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_NSUbiquitousKeyValueStore
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$__TtC39com_apple_SpeechRecognitionCore_brokerd16VCVocabularySync
+ _OBJC_METACLASS_$__TtC39com_apple_SpeechRecognitionCore_brokerd16VCVocabularySync
+ __ZN16RDLanguageAssets37CopySupportedLanguagesForVoiceControlEv
+ __ZN9RDMinions10LockReaderEP15NSXPCConnectionPU24objcproto13OS_xpc_object8NSObjectS4_
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_stdlib_bridgeErrorToNSError
+ _kRDKeySupportedLanguagesForVoiceControl
+ _malloc_size
+ _objc_allocWithZone
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_self
+ _objc_release
+ _objc_release_x1
+ _objc_release_x20
+ _objc_release_x22
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x8
+ _objc_retain_x9
+ _objc_storeStrong
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
- _CFCopySearchPathForDirectoriesInDomains
- _CFLocaleCreate
- _CFLocaleGetValue
- _CFNumberGetValue
- _CFPreferencesGetAppBooleanValue
- _CFPreferencesGetAppIntegerValue
- _CFPropertyListCreateWithStream
- _CFReadStreamClose
- _CFReadStreamCreateWithFile
- _CFReadStreamOpen
- _CFSetAddValue
- _CFSetCreateMutable
- _CFStringCreateWithBytes
- _CFStringCreateWithCString
- _CFStringCreateWithFormat
- _CFStringGetCString
- _CFStringGetCStringPtr
- _CFStringGetCharacterAtIndex
- _CFStringGetMaximumSizeForEncoding
- _CFURLCopyFileSystemPath
- _CFURLCopyPath
- _CFURLCreateCopyAppendingPathComponent
- _CFURLCreateWithFileSystemPath
- _RXAutomationModeFileName
- _RXAutomationModeResult
- _RXAutomationModeSynthesis
- _RXAutomationSaveKeywordsAudio
- _RXAutomationSimulateOpenMic
- _RXDebugFlagsUpdate
- _RXIsAppleInternal
- _RXLogClientUpdates
- _RXLogPerformance
- _RXLogServerGrammar
- _RXLogServerResults
- _RXLogSound
- _RXResetTimeInSec
- _RXSignpostLog
- _RXVeryVerbose
- __Block_object_assign
- __Z11RDNukeCachePK10__CFString
- __Z14RDCopyCacheURLv
- __Z14RDCopyInfoDictPK7__CFURL
- __Z15RDCopyModelPathv
- __Z18RDCopyCacheVersionPK10__CFString
- __Z26RDDoLocaleIdentifiersMatchPK10__CFStringS1_
- __Z29RDCopyNashvilleModelLanguagesv
- __Z35RDCopyBestNashvilleLocaleIdentifierPK10__CFString
- __ZN13RDRecognizersC1Ev
- __ZN5RDIntC1EPK10__CFNumberb
- __ZN5RDIntC2EPK10__CFNumberb
- __ZN5RDURL7DirNameEv
- __ZN5RDURLC1EPK7__CFURLb
- __ZN5RDURLC2EPK7__CFURLb
- __ZN8RDStringC1EPK10__CFStringb
- __ZN8RDStringC2EPK10__CFStringb
- __ZN9RDMinions10LockReaderEPU24objcproto13OS_xpc_object8NSObjectS2_S2_
- __ZN9RDMinions10LockWriterEPU24objcproto13OS_xpc_object8NSObjectS2_
- __ZN9RDMinions12EventHandlerEPU24objcproto13OS_xpc_object8NSObjectS2_
- __ZN9RDMinions6UnlockEPU24objcproto13OS_xpc_object8NSObject
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5rfindEcm
- __ZNSt12out_of_rangeD1Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
- __ZTISt12out_of_range
- __ZTVSt12out_of_range
- __Znwm
- ___RXAbort
- __os_feature_enabled_impl
- _backtrace
- _backtrace_symbols
- _closedir
- _kCFBooleanTrue
- _kCFLocaleCountryCode
- _kCFLocaleLanguageCode
- _kCFTypeSetCallBacks
- _kRDKeyAllowCloseMatch
- _kRDKeyAudioData
- _kRDKeyBlocked
- _kRDKeyCallbacks
- _kRDKeyCategory
- _kRDKeyCategoryID
- _kRDKeyChildren
- _kRDKeyCommandID
- _kRDKeyDead
- _kRDKeyDownloadStatus
- _kRDKeyEndTime
- _kRDKeyEpoch
- _kRDKeyFilterProfanity
- _kRDKeyFocusOnSecureField
- _kRDKeyInForeground
- _kRDKeyIsHypothesis
- _kRDKeyIsListening
- _kRDKeyLanguageModel
- _kRDKeyMask
- _kRDKeyMaxResults
- _kRDKeyNumberMode
- _kRDKeyObjectType
- _kRDKeyObjects
- _kRDKeyRecognitionResetMode
- _kRDKeyRecognizer
- _kRDKeyResultID
- _kRDKeySpellingMode
- _kRDKeyStartTime
- _kRDKeyText
- _kRDKeyTextToBeRecognized
- _kRDKeyTextVariants
- _kRDKeyTopLevelLM
- _kRDKeyURL
- _kRDKeyUseStreaming
- _kRDKeyUserProfileSavePath
- _kRDKeyUtteranceID
- _kRDKeyVocabulary
- _memchr
- _mkdir
- _objc_setProperty_nonatomic
- _opendir
- _os_variant_has_internal_diagnostics
- _pthread_cond_broadcast
- _readdir
- _removefile
- _reportBacktrace
- _stat
- _strchr
- _strstr
- _write
- _xpc_connection_create
- _xpc_connection_set_instance
- _xpc_endpoint_create
- _xpc_release
- _xpc_retain
CStrings:
+ "#"
+ ".cxx_destruct"
+ "@\"NSArray\"16@0:8"
+ "@\"NSArray\"32@0:8@\"NSString\"16^@24"
+ "BrokerConnection: Summoning new batch minion %p"
+ "BrokerConnection: Summoning new live minion %p for audio device %s"
+ "BrokerConnection: Using existing live minion %p[%d] for audio device %s"
+ "BrokerConnection: endpoint %@"
+ "BrokerConnection: got event handler, adding peer"
+ "Hello"
+ "SRDBrokerProtocol"
+ "VCVocabularySync.listenForExternalChanges() New observer added."
+ "VCVocabularySync.removeAllVocabularyEntriesFromCloud(): Failed to remove entries. %@"
+ "VCVocabularySync.sync() ###"
+ "VCVocabularySync.sync() mergeResult: %s"
+ "VCVocabularySync.sync(): Cloud data set"
+ "VCVocabularySync.sync(): Failed to decompress or decode cloudData. %{public}@"
+ "VCVocabularySync.sync(): Failed to update cloud %@"
+ "VCVocabularySync.sync(): Local data set"
+ "VCVocabularySync.sync(): cloudData is nil"
+ "VCVocabularySync.sync(): syncVocabularyEntries is false. No change."
+ "VCVocabularySync.sync(): syncVocabularyEntries is false. mergeResult == .bothNeedUpdates. oldEntriesCount: %{public}ld, newEntriesCount: %{public}ld"
+ "VCVocabularySync.ubiquitousKeyValueStoreDidChange"
+ "VCVocabularySync.ubiquitousKeyValueStoreDidChange quota violation."
+ "VCVocabularySync.ubiquitousKeyValueStoreDidChange reasonForChange is nil."
+ "VCVocabularySync.ubiquitousKeyValueStoreDidChange userInfo is nil."
+ "_TtC39com_apple_SpeechRecognitionCore_brokerd16VCVocabularySync"
+ "_endpoint"
+ "_setUUID:"
+ "addObserver:selector:name:object:"
+ "brokerIntro:reply:"
+ "compressedDataUsingAlgorithm:error:"
+ "dataForKey:"
+ "decompressedDataUsingAlgorithm:error:"
+ "defaultCenter"
+ "defaultStore"
+ "getCloudDataSize"
+ "initWithServiceName:"
+ "initWithUUIDBytes:"
+ "interfaceWithProtocol:"
+ "listenForExternalChanges"
+ "processIdentifier"
+ "remoteObjectProxy"
+ "removeAllVocabularyEntriesFromCloud"
+ "resume"
+ "setData:forKey:"
+ "setInvalidationHandler:"
+ "setRemoteObjectInterface:"
+ "supportedLanguages"
+ "supportedLanguagesForTaskHint:completion:"
+ "supportedLanguagesForVoiceControl"
+ "supportedLanguagesForVoiceControl = %@"
+ "sync"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "ubiquitousKeyValueStoreDidChange:"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSXPCListenerEndpoint\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSXPCListenerEndpoint\">24"
+ "v32@0:8@16@?24"
+ "vocabularyEntries"
- "%@/Speech/Recognizers/SpeechRecognitionCoreLanguages"
- "%s:%u: %@\n"
- "%s:%u: failed assertion `%s' %@\n"
- ".SpeechRecognition"
- "/Contents/Info.plist"
- "BACKTRACE: %-3d %p\n"
- "BACKTRACE: %-3d %p %s\n"
- "CFBundleShortVersionString"
- "Error creating %@"
- "EventHandler"
- "Info.plist"
- "RXDebugAutomationMode"
- "RXDebugAutomationSaveKeywordsAudio"
- "RXDebugAutomationSimulateOpenMic"
- "RXDebugFlag"
- "RXRecognitionResetTimeInSec"
- "RXVeryVerbose"
- "SRCSignposts"
- "Summoning new batch minion %p"
- "Summoning new live minion %p for audio device %s"
- "Users"
- "Using existing live minion %p[%d] for audio device %s"
- "Using original RDAssetManager"
- "VoiceControl"
- "allowCloseMatch"
- "audioData"
- "begT"
- "blocked"
- "busy"
- "callbacks"
- "cat"
- "categoryID"
- "cmdID"
- "daemon died while %s; rebuilding cache for %s"
- "daemon(%d) XPC_ERROR_CONNECTION_%s"
- "daemon(%d) waiting for write lock (%u readers)"
- "de"
- "de_DE"
- "dead"
- "en"
- "en_US"
- "endT"
- "epoch"
- "es"
- "es_US"
- "filterProfanity"
- "focusOnSecureField"
- "foreground"
- "fr"
- "fr_FR"
- "hypo"
- "kids"
- "listen"
- "lm"
- "mask"
- "maxRes"
- "new_asset_manager"
- "numberMode"
- "objects"
- "reco"
- "recognitionResetMode"
- "resID"
- "spellingMode"
- "starting"
- "stream"
- "text"
- "textToBeRecognized"
- "textVar"
- "topLM"
- "type"
- "url"
- "userProfileSavePath"
- "utt"
- "vocab"

```
