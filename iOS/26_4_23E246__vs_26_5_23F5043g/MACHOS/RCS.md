## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

```diff

-1450.500.221.2.9
-  __TEXT.__text: 0xf5648
-  __TEXT.__auth_stubs: 0x1dd0
-  __TEXT.__objc_stubs: 0x51e0
+1450.600.13.2.2
+  __TEXT.__text: 0xf7128
+  __TEXT.__auth_stubs: 0x1d40
+  __TEXT.__objc_stubs: 0x5220
   __TEXT.__objc_methlist: 0x984
-  __TEXT.__const: 0x5c68
+  __TEXT.__const: 0x5de8
   __TEXT.__objc_classname: 0x46f
-  __TEXT.__objc_methtype: 0x146f
-  __TEXT.__swift5_typeref: 0x1f5d
-  __TEXT.__constg_swiftt: 0x2238
-  __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x1414
-  __TEXT.__swift5_assocty: 0x2c8
-  __TEXT.__oslogstring: 0x6288
-  __TEXT.__swift5_fieldmd: 0x1844
-  __TEXT.__swift5_proto: 0x31c
-  __TEXT.__swift5_types: 0x1c8
-  __TEXT.__swift_as_entry: 0x258
-  __TEXT.__swift_as_ret: 0x2c0
-  __TEXT.__swift5_capture: 0x964
-  __TEXT.__cstring: 0x2693
+  __TEXT.__objc_methtype: 0x147f
+  __TEXT.__swift5_typeref: 0x1f9d
+  __TEXT.__constg_swiftt: 0x2298
+  __TEXT.__swift5_builtin: 0x1b8
+  __TEXT.__swift5_reflstr: 0x1464
+  __TEXT.__swift5_assocty: 0x2e0
+  __TEXT.__oslogstring: 0x6378
+  __TEXT.__swift5_fieldmd: 0x18c4
+  __TEXT.__swift5_proto: 0x328
+  __TEXT.__swift5_types: 0x1d0
+  __TEXT.__swift_as_entry: 0x26c
+  __TEXT.__swift_as_ret: 0x2d4
+  __TEXT.__swift5_capture: 0x99c
+  __TEXT.__cstring: 0x2673
   __TEXT.__swift5_mpenum: 0xcc
-  __TEXT.__objc_methname: 0x5955
+  __TEXT.__objc_methname: 0x5a05
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__unwind_info: 0x36b8
-  __TEXT.__eh_frame: 0x96b8
-  __DATA_CONST.__auth_got: 0xef0
-  __DATA_CONST.__got: 0x880
-  __DATA_CONST.__auth_ptr: 0x630
-  __DATA_CONST.__const: 0x5570
+  __TEXT.__unwind_info: 0x3758
+  __TEXT.__eh_frame: 0x9868
+  __DATA_CONST.__auth_got: 0xea8
+  __DATA_CONST.__got: 0x8b8
+  __DATA_CONST.__auth_ptr: 0x638
+  __DATA_CONST.__const: 0x56a8
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA.__objc_const: 0x2238
-  __DATA.__objc_selrefs: 0x1750
+  __DATA.__objc_selrefs: 0x1760
   __DATA.__objc_data: 0x6a0
-  __DATA.__data: 0x3940
-  __DATA.__bss: 0x4e00
+  __DATA.__data: 0x3980
+  __DATA.__bss: 0x4f80
   __DATA.__common: 0xe0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
-  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C4BBBB0F-8FED-3953-BAEB-FB90C31C11BA
-  Functions: 3473
-  Symbols:   428
-  CStrings:  1577
+  UUID: 2D25C626-CF5D-3801-ACA5-F4181A0ECABC
+  Functions: 3508
+  Symbols:   430
+  CStrings:  1582
 
Symbols:
+ _IMChatPropertyRCSGroupIdentityVersion
+ _IMChatPropertyRCSGroupURI
+ _OBJC_CLASS_$_IMDHandleStore
+ _OBJC_CLASS_$_IMDRelaySentMessageConfiguration
- _OBJC_CLASS_$_NSData
- __swift_FORCE_LOAD_$_swiftCallKit
CStrings:
+ "Chatbot properties update for %s: changed=%{bool}d"
+ "Dropping subject change for group as the display name status is .ignore"
+ "_automation_updateAlternateHandle:forChatBotHandle:refreshUI:"
+ "_forceReloadChatsWithAnyHandleIDs:"
+ "_markMessageAsSent:wasInterworked:encrypted:"
+ "categorizeIncomingRCSMessageGUID:sender:wasRelayed:chatIdentifier:participants:checkingForSpam:trustIndicator:myReceiverISOCountryCode:messageBody:foundChat:service:containsOneTimeCode:fileTransferGUIDs:isEncrypted:completion:"
+ "didChangeChatWithContexts:"
+ "downloadRCSTransferOnSimID:transferURL:fileName:destURL:cryptoMaterial:completion:"
+ "handlesWithID:"
+ "handlesWithPersonCentricIDs:"
+ "initWithMemberStatus:forHandle:fromHandle:unformattedNumber:countryCode:forChat:style:account:destinationCallerID:messageTime:messageID:silently:"
+ "initWithMessageID:service:compatibilityService:wasInterworked:encrypted:"
+ "messageSent:"
+ "setImdnReceiveStatus:"
+ "sharedStore"
+ "subjectState"
+ "update() called with alternateHandle: %s, chatBotHandle: %s, refreshUI: %{bool}d"
+ "v36@0:8@16@24B32"
- "RCSGroupIdentityVersion"
- "__imDataWithHexString:"
- "__imHexString"
- "_forceReloadChats:"
- "_markMessageAsSent:"
- "categorizeIncomingRCSMessageGUID:sender:wasRelayed:chatIdentifier:participants:checkingForSpam:trustIndicator:myReceiverISOCountryCode:messageBody:foundChat:service:containsOneTimeCode:fileTransferGUIDs:completion:"
- "didChangeMemberStatus:"
- "didChangeMemberStatus:forHandle:fromHandle:unformattedNumber:countryCode:forChat:style:account:destinationCallerID:messageTime:messageID:silently:"
- "didUpdateChatStatusWithContext:"
- "downloadRCSTransferOnSimID:transferURL:destURL:cryptoMaterial:completion:"
- "forceReloadChats"
- "messageSent:onService:compatibilityService:"
- "messageSent:onService:compatibilityService:wasInterworked:"

```
