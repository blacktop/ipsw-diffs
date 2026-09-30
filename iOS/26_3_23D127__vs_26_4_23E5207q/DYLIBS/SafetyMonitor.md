## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-1071.0.1.0.0
-  __TEXT.__text: 0x74334
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__objc_methlist: 0x4e34
-  __TEXT.__const: 0x14a0
+1072.0.5.0.1
+  __TEXT.__text: 0x786d0
+  __TEXT.__auth_stubs: 0x1200
+  __TEXT.__objc_methlist: 0x4e1c
+  __TEXT.__const: 0x1620
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__cstring: 0xc115
   __TEXT.__swift5_typeref: 0x4a2
   __TEXT.__oslogstring: 0x44cd
   __TEXT.__constg_swiftt: 0x450

   __TEXT.__swift5_fieldmd: 0x3ec
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x90
+  __TEXT.__cstring: 0xbdbd
   __TEXT.__swift5_capture: 0x140
-  __TEXT.__swift5_proto: 0xd0
+  __TEXT.__swift5_proto: 0xd8
   __TEXT.__swift5_types: 0x54
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xd34
-  __TEXT.__gcc_except_tab: 0xf70
-  __TEXT.__unwind_info: 0x1820
-  __TEXT.__eh_frame: 0x9dc
-  __TEXT.__objc_classname: 0x9f3
-  __TEXT.__objc_methname: 0xc8e1
-  __TEXT.__objc_methtype: 0x2288
-  __TEXT.__objc_stubs: 0x59c0
+  __TEXT.__gcc_except_tab: 0xc9c
+  __TEXT.__unwind_info: 0x18e8
+  __TEXT.__eh_frame: 0x9ac
+  __TEXT.__objc_classname: 0xaf8
+  __TEXT.__objc_methname: 0xca41
+  __TEXT.__objc_methtype: 0x23e7
+  __TEXT.__objc_stubs: 0x5d20
   __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__const: 0x14e0
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2310
+  __DATA_CONST.__objc_selrefs: 0x2300
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1b0
-  __AUTH_CONST.__auth_got: 0x948
+  __AUTH_CONST.__auth_got: 0x910
   __AUTH_CONST.__const: 0xa10
   __AUTH_CONST.__cfstring: 0x5100
   __AUTH_CONST.__objc_const: 0x83e8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1210
-  __AUTH.__data: 0x2d8
+  __AUTH.__objc_data: 0x11c0
+  __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0x398
-  __DATA.__data: 0x1318
-  __DATA.__bss: 0x1600
-  __DATA.__common: 0x88
+  __DATA.__data: 0x1300
+  __DATA.__bss: 0x1700
+  __DATA.__common: 0x82
   __DATA_DIRTY.__objc_ivar: 0x1d4
-  __DATA_DIRTY.__objc_data: 0x9c8
-  __DATA_DIRTY.__data: 0xe0
+  __DATA_DIRTY.__objc_data: 0xa18
+  __DATA_DIRTY.__data: 0x100
   __DATA_DIRTY.__bss: 0x430
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DEC89ABA-884A-31DF-A7D1-217DF7C6A8DA
+  UUID: B2392DEB-1937-36CE-9FF7-EF075112659A
   Functions: 2196
-  Symbols:   5748
-  CStrings:  4068
+  Symbols:   5765
+  CStrings:  4053
 
Symbols:
+ ___67-[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]_block_invoke.426
+ ___69-[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]_block_invoke.422
+ ___block_literal_global.378
+ ___block_literal_global.382
+ ___block_literal_global.421
+ ___block_literal_global.425
+ ___block_literal_global.428
+ ___block_literal_global.515
+ _objc_msgSend$_crossPlatformUnifiedMeContactWithKeysToFetch:error:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$cacheReleaseDate
+ _objc_msgSend$cancel
+ _objc_msgSend$codeServiceWithName:databaseScope:
+ _objc_msgSend$componentsForContact:
+ _objc_msgSend$createURLToConversationForGroupID:
+ _objc_msgSend$createURLToConversationForRecipientHandle:
+ _objc_msgSend$createURLToDetailViewForGroupID:recipientHandles:
+ _objc_msgSend$createURLToDetailViewForRecipientHandle:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$familyName
+ _objc_msgSend$givenName
+ _objc_msgSend$init
+ _objc_msgSend$initWithContainerID:
+ _objc_msgSend$initWithContainerIdentifier:environment:
+ _objc_msgSend$initWithStringValue:
+ _objc_msgSend$isCacheReleasedState
+ _objc_msgSend$isGroup
+ _objc_msgSend$isPromptState
+ _objc_msgSend$localizedStringFromPersonNameComponents:style:options:
+ _objc_msgSend$openURL:configuration:completionHandler:
+ _objc_msgSend$predicateForContactsMatchingEmailAddress:
+ _objc_msgSend$predicateForContactsMatchingPhoneNumber:
+ _objc_msgSend$predicateForContactsWithIdentifiers:
+ _objc_msgSend$relativeTimeString
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$unifiedContactsMatchingPredicate:keysToFetch:error:
+ _swift_bridgeObjectRelease_n
- +[SMSessionEndMessage sessionEndReasonFromDict:]
- +[SMSessionEndMessage sessionEndReasonFromURL:]
- ___67-[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]_block_invoke.427
- ___69-[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]_block_invoke.423
- ___block_literal_global.330
- ___block_literal_global.334
- ___block_literal_global.422
- ___block_literal_global.426
- ___block_literal_global.429
- ___block_literal_global.516
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$sessionEndReasonFromURL:
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
- "sessionEndReasonFromDict:"
- "sessionEndReasonFromURL:"

```
