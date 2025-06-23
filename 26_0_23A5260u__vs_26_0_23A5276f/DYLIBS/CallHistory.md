## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

```diff

-91.100.5.2.14
-  __TEXT.__text: 0x19c490
-  __TEXT.__auth_stubs: 0x2400
-  __TEXT.__objc_methlist: 0x383c
-  __TEXT.__const: 0x1c2c8
+95.100.10.2.4
+  __TEXT.__text: 0x19dd64
+  __TEXT.__auth_stubs: 0x2410
+  __TEXT.__objc_methlist: 0x3884
+  __TEXT.__const: 0x1c668
+  __TEXT.__cstring: 0x4db0
+  __TEXT.__oslogstring: 0x58c8
   __TEXT.__gcc_except_tab: 0x804
-  __TEXT.__cstring: 0x4b22
-  __TEXT.__oslogstring: 0x58c4
   __TEXT.__dlopen_cstrs: 0x147
-  __TEXT.__constg_swiftt: 0x11110
-  __TEXT.__swift5_typeref: 0x5066
-  __TEXT.__swift5_reflstr: 0x672a
-  __TEXT.__swift5_fieldmd: 0x54b0
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_assocty: 0x1b30
-  __TEXT.__swift5_proto: 0xda0
-  __TEXT.__swift5_types: 0x42c
-  __TEXT.__swift5_capture: 0x314
+  __TEXT.__constg_swiftt: 0x111dc
+  __TEXT.__swift5_typeref: 0x50cc
+  __TEXT.__swift5_reflstr: 0x6874
+  __TEXT.__swift5_fieldmd: 0x5574
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_assocty: 0x1b78
+  __TEXT.__swift5_proto: 0xdc8
+  __TEXT.__swift5_types: 0x434
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift_as_entry: 0xc0
   __TEXT.__swift_as_ret: 0xa8
+  __TEXT.__swift5_capture: 0x314
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x64b8
-  __TEXT.__eh_frame: 0x7510
+  __TEXT.__unwind_info: 0x6340
+  __TEXT.__eh_frame: 0x75f8
   __TEXT.__objc_classname: 0x65d
-  __TEXT.__objc_methname: 0x9615
+  __TEXT.__objc_methname: 0x9732
   __TEXT.__objc_methtype: 0x1224
-  __TEXT.__objc_stubs: 0x7540
+  __TEXT.__objc_stubs: 0x75c0
   __DATA_CONST.__got: 0x970
-  __DATA_CONST.__const: 0x12d8
+  __DATA_CONST.__const: 0x1300
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23f8
+  __DATA_CONST.__objc_selrefs: 0x2430
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x138
-  __AUTH_CONST.__auth_got: 0x1210
-  __AUTH_CONST.__const: 0x48a8
-  __AUTH_CONST.__cfstring: 0x2d60
-  __AUTH_CONST.__objc_const: 0x14380
+  __AUTH_CONST.__auth_got: 0x1218
+  __AUTH_CONST.__const: 0x4a48
+  __AUTH_CONST.__cfstring: 0x2f00
+  __AUTH_CONST.__objc_const: 0x14430
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x1be0
-  __AUTH.__data: 0x14c70
-  __DATA.__objc_ivar: 0x2ac
-  __DATA.__data: 0x4758
-  __DATA.__bss: 0x1da00
-  __DATA.__common: 0x120
+  __AUTH.__data: 0x14d18
+  __DATA.__objc_ivar: 0x2b0
+  __DATA.__data: 0x47c0
+  __DATA.__bss: 0x1df18
+  __DATA.__common: 0x128
   __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B87C880F-7EF0-3FFB-9B6C-1B8114DD9B65
-  Functions: 12057
-  Symbols:   7600
-  CStrings:  3275
+  UUID: AA715589-6EA3-3D13-A6C5-124BAAC79BD3
+  Functions: 12067
+  Symbols:   7630
+  CStrings:  3312
 
Symbols:
+ +[CHRecentCall(Predicate) predicateForCallsHavingReminder]
+ +[CHSpotlightSearchQueryUtilities searchStringForAcceptedContacts]
+ +[CHSpotlightSearchQueryUtilities searchStringForUnknownContacts]
+ +[NSString(CHRecentCallAdditions) ch_stringWithCHRecentCallCommunicationTrustScore:]
+ -[CHRecentCall communicationTrustScore]
+ -[CHRecentCall setCommunicationTrustScore:]
+ -[CallRecord(Additions) supportsCommunicationTrustScore]
+ _OBJC_IVAR_$_CHRecentCall._communicationTrustScore
+ __OBJC_$_CATEGORY_NSString_$_CHTransactionAdditions
+ __OBJC_$_CLASS_METHODS_CHRecentCall(UserNotifications|Predicate|Intents)
+ __OBJC_$_CLASS_METHODS_EmergencyMediaItem(CoreDataProperties|Additions)
+ __OBJC_$_CLASS_METHODS_NSString(CHTransactionAdditions|CHRecentCallAdditions|CallHistory)
+ __OBJC_$_INSTANCE_METHODS_CHRecentCall(UserNotifications|Predicate|Intents)
+ __OBJC_$_INSTANCE_METHODS_EmergencyMediaItem(CoreDataProperties|Additions)
+ ___block_literal_global.935
+ _associated conformance 11CallHistory23CommunicationTrustScoreOSHAASQ
+ _associated conformance 11CallHistory23CommunicationTrustScoreOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance So35CHRecentCallCommunicationTrustScoreVSHSCSQ
+ _kSpotlightHasAcceptedContactKey
+ _objc_msgSend$ch_stringWithCHRecentCallCommunicationTrustScore:
+ _objc_msgSend$communicationTrustScore
+ _objc_msgSend$setCommunicationTrustScore:
+ _objc_msgSend$supportsCommunicationTrustScore
+ _swift_deallocPartialClassInstance
+ _symbolic Say_____G 11CallHistory23CommunicationTrustScoreO
+ _symbolic _____ 11CallHistory23CommunicationTrustScoreO
+ _symbolic _____ So35CHRecentCallCommunicationTrustScoreV
+ _symbolic _____y__________G s18_DictionaryStorageC 11CallHistory23CommunicationTrustScoreO So08CHRecentcefG0V
+ _symbolic _____y__________G s18_DictionaryStorageC So35CHRecentCallCommunicationTrustScoreV 0D7History0efG0O
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 11CallHistory23CommunicationTrustScoreO So08CHRecentdfgH0V
- __OBJC_$_CATEGORY_NSString_$_CallHistory
- __OBJC_$_CLASS_METHODS_CHRecentCall(Predicate|Intents|UserNotifications)
- __OBJC_$_CLASS_METHODS_EmergencyMediaItem(Additions|CoreDataProperties)
- __OBJC_$_CLASS_METHODS_NSString(CallHistory|CHRecentCallAdditions|CHTransactionAdditions)
- __OBJC_$_INSTANCE_METHODS_CHRecentCall(Predicate|Intents|UserNotifications)
- __OBJC_$_INSTANCE_METHODS_EmergencyMediaItem(Additions|CoreDataProperties)
- ___block_literal_global.895
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CallHistory
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CallHistory
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CallHistory
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CallHistory
- _kSpotlightCallDayKey
- _kSpotlightItemTypeKey
CStrings:
+ "%@!=%@"
+ "%@==%@ || %@==%@"
+ "95.100.10.2.4"
+ "95.100.10.2.4~1"
+ "CHRecentCallCommunicationTrustScoreBlocked"
+ "CHRecentCallCommunicationTrustScoreBlockedByThirdParty"
+ "CHRecentCallCommunicationTrustScoreCommunicatedWith"
+ "CHRecentCallCommunicationTrustScoreContact"
+ "CHRecentCallCommunicationTrustScoreIdentifiedByThirdParty"
+ "CHRecentCallCommunicationTrustScoreJunk"
+ "CHRecentCallCommunicationTrustScoreMaybe"
+ "CHRecentCallCommunicationTrustScoreSuspectedJunk"
+ "CHRecentCallCommunicationTrustScoreUnknown"
+ "CHRecentCallCommunicationTrustScoreVIP"
+ "Communication Trust Score: %@\n"
+ "Tq,N,V_communicationTrustScore"
+ "_communicationTrustScore"
+ "ch_stringWithCHRecentCallCommunicationTrustScore:"
+ "com_apple_mobilephone_hasAcceptedContact"
+ "communicationTrustScore"
+ "predicateForCallsHavingReminder"
+ "reminderUUID != nil"
+ "searchStringForAcceptedContacts"
+ "searchStringForUnknownContacts"
+ "setCommunicationTrustScore:"
+ "supportsCommunicationTrustScore"
- "91.100.5.2.14"
- "91.100.5.2.14~2"
- "com_apple_mobilephone_callDay"
- "com_apple_mobilephone_itemType"

```
