## PhoneIntentHandler

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler`

```diff

-1431.100.4.2.39
-  __TEXT.__text: 0x2dbf0
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x4d60
-  __TEXT.__objc_methlist: 0x1760
-  __TEXT.__cstring: 0x146f
-  __TEXT.__oslogstring: 0x674c
-  __TEXT.__objc_classname: 0x618
-  __TEXT.__objc_methname: 0x62c6
-  __TEXT.__objc_methtype: 0x1139
+1431.200.71.2.11
+  __TEXT.__text: 0x2e85c
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0x4f00
+  __TEXT.__objc_methlist: 0x17b0
+  __TEXT.__cstring: 0x156f
+  __TEXT.__oslogstring: 0x67ed
+  __TEXT.__objc_classname: 0x642
+  __TEXT.__objc_methname: 0x64c4
+  __TEXT.__objc_methtype: 0x118e
   __TEXT.__const: 0x130
   __TEXT.__gcc_except_tab: 0x1e8
   __TEXT.__swift5_typeref: 0x2b8

   __TEXT.__swift5_reflstr: 0x39
   __TEXT.__swift5_capture: 0x1a4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1250
+  __TEXT.__unwind_info: 0x1280
   __TEXT.__eh_frame: 0x988
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0xb08
   __DATA_CONST.__cfstring: 0xf20
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x4e70
-  __DATA.__objc_selrefs: 0x1578
+  __DATA.__objc_const: 0x5048
+  __DATA.__objc_selrefs: 0x15e8
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x3e0
+  __DATA.__objc_classrefs: 0x3f0
   __DATA.__objc_superrefs: 0xc0
-  __DATA.__objc_ivar: 0x164
-  __DATA.__objc_data: 0xf08
-  __DATA.__data: 0xb20
+  __DATA.__objc_ivar: 0x16c
+  __DATA.__objc_data: 0xf58
+  __DATA.__data: 0xb80
   __DATA.__bss: 0x58
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 759
-  Symbols:   392
-  CStrings:  1757
+  Functions: 775
+  Symbols:   397
+  CStrings:  1788
 
Symbols:
+ _IDSServiceNameFaceTime
+ _OBJC_CLASS_$_AddCallParticipantIntentHandlerDataSource
+ _OBJC_CLASS_$_IDSService
+ _OBJC_METACLASS_$_AddCallParticipantIntentHandlerDataSource
+ _TUNetworkCountryCode
CStrings:
+ "%s CRR chose 1 INPerson but contact has no handle."
+ "%s Found memberToAdd in FaceTime account aliases"
+ "%s Resolving participants: %@"
+ "%s localMember %@ matches memberToAdd"
+ "%s memberToAdd %@"
+ "-[AddCallParticipantIntentHandler _checkSelfAdd:toConversation:]"
+ "-[AddCallParticipantIntentHandler interpretContactResolutionRecommendation:participant:]"
+ "-[AddCallParticipantIntentHandler resolveParticipantsForAddCallParticipant:withCompletion:]"
+ "@\"<AddCallParticipantIntentHandlerDataSource>\""
+ "@\"<FaceTimeUtilities>\""
+ "@\"NSSet\"16@0:8"
+ "AddCallParticipantIntentHandlerDataSource"
+ "An incoming call exists: %@"
+ "Declining it and returning success"
+ "FT aliases: %@"
+ "Sending call to automatic screening"
+ "T@\"<AddCallParticipantIntentHandlerDataSource>\",R,N,V_dataSource"
+ "T@\"<FaceTimeUtilities>\",R,N,V_ftUtilities"
+ "T@\"NSArray\",R,C"
+ "_checkRestrictionsForCall:conversation:personToAdd:asMember:"
+ "_checkSelfAdd:toConversation:"
+ "_ftUtilities"
+ "accounts"
+ "fetchFaceTimeAccountAliases"
+ "formattedInternationalStringValue"
+ "ftUtilities"
+ "initWithAudioPlaybackService:voicemailManager:callCenter:"
+ "initWithCallCenter:dataSource:faceTimeUtilities:"
+ "initWithService:"
+ "initWithStringValue:countryCode:"
+ "isEligibleForScreening"
+ "isoCountryCodes"
+ "localMember"
+ "setContacts:"
+ "setSendToScreening:"
+ "tu_normalizedHandleForISOCountryCode:"
+ "vettedAliases"
- "An incoming call exists. Declining it and returning success: %@"
- "CRR chose 1 INPerson but contact has no handle."
- "Resolving participants: %@"
- "_checkRestrictionsForCall:conversation:personToAdd:"
- "_checkSelfAdd:toCall:"
- "localSenderIdentity"

```
