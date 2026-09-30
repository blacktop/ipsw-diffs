## SiriMessagesUICommon

> `/System/Library/PrivateFrameworks/SiriMessagesUICommon.framework/SiriMessagesUICommon`

```diff

-3600.47.13.0.0
-  __TEXT.__text: 0x9f578
-  __TEXT.__const: 0xb784
-  __TEXT.__cstring: 0x2f74
-  __TEXT.__swift5_typeref: 0x20c4
-  __TEXT.__swift5_reflstr: 0x1f9e
+3600.47.22.11.2
+  __TEXT.__text: 0xa3c3c
+  __TEXT.__const: 0xb8a4
+  __TEXT.__cstring: 0x3044
+  __TEXT.__swift5_typeref: 0x2154
+  __TEXT.__swift5_reflstr: 0x1ffe
   __TEXT.__swift5_assocty: 0x258
-  __TEXT.__constg_swiftt: 0x21b0
+  __TEXT.__constg_swiftt: 0x2200
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_fieldmd: 0x2bf0
-  __TEXT.__oslogstring: 0x1d4a
+  __TEXT.__swift5_fieldmd: 0x2c58
+  __TEXT.__oslogstring: 0x215a
   __TEXT.__swift5_proto: 0xac8
-  __TEXT.__swift5_types: 0x308
-  __TEXT.__swift_as_entry: 0xd4
-  __TEXT.__swift_as_ret: 0xf0
-  __TEXT.__swift_as_cont: 0x14c
+  __TEXT.__swift5_types: 0x310
+  __TEXT.__swift_as_entry: 0xdc
+  __TEXT.__swift_as_ret: 0xfc
+  __TEXT.__swift_as_cont: 0x158
   __TEXT.__swift5_capture: 0x4a8
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x36f8
-  __TEXT.__eh_frame: 0x4c60
+  __TEXT.__unwind_info: 0x3878
+  __TEXT.__eh_frame: 0x4e40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x468
+  __DATA_CONST.__const: 0x478
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e8
+  __DATA_CONST.__objc_selrefs: 0x718
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x7150
+  __AUTH_CONST.__const: 0x7270
   __AUTH_CONST.__objc_const: 0xbb8
-  __AUTH_CONST.__auth_got: 0x1018
+  __AUTH_CONST.__auth_got: 0x1110
   __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0x8a8
-  __DATA.__data: 0x1658
+  __AUTH.__data: 0x8b0
+  __DATA.__data: 0x16f0
   __DATA.__bss: 0x10df0
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x1c0

   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
   - /System/Library/PrivateFrameworks/FlowToolTypes.framework/FlowToolTypes

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
+  - /System/Library/PrivateFrameworks/_AppIntentsServices_AppIntents.framework/_AppIntentsServices_AppIntents
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5818
-  Symbols:   1712
-  CStrings:  472
+  Functions: 5895
+  Symbols:   1734
+  CStrings:  492
 
Symbols:
+ _INIntentSlotValueTransformToContactValue
+ _OBJC_CLASS_$_SABaseClientBoundCommand
+ _OBJC_CLASS_$_SAUIAppIntentData
+ _OBJC_CLASS_$_SAUIPerformAppIntent
+ _objc_msgSend$aceId
+ _objc_msgSend$isMe
+ _objc_msgSend$nameComponents
+ _objc_msgSend$personHandle
+ _objc_msgSend$setAppIntentData:
+ _objc_msgSend$value
+ _symbolic Say_____G 10AppIntents12IntentPersonV
+ _symbolic _____ 20SiriMessagesUICommon23PerformAppIntentFactoryO
+ _symbolic _____ 20SiriMessagesUICommon36SendOnDismissPerformAppIntentBuilderO
+ _symbolic _____Sg 10AppIntents12IntentPersonV
+ _symbolic _____Sg 10AppIntents12IntentPersonV6HandleV
+ _symbolic _____Sg 10AppIntents21DisplayRepresentationV5ImageV
+ _symbolic _____Sg 10Foundation16AttributedStringV
+ _symbolic _____Sg 18AppIntentsServices0A16InstanceLocationV
+ _symbolic _____Sg 18AppIntentsServices13SchemaVersionV
+ _symbolic _____Sg 7ToolKit0A10DefinitionV
+ _symbolic _____ySo24SABaseClientBoundCommandCG 20SiriMessagesUICommon12ModelCodableV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10AppIntents12IntentPersonV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18AppIntentsServices13NamedPropertyV
- _OUTLINED_FUNCTION_185
CStrings:
+ "#INPerson displayName %s"
+ "#INPerson email handle type %s"
+ "#INPerson nameComponents %s"
+ "#INPerson neither email or phone handle type, return nil"
+ "#INPerson no personHandle, value, or type"
+ "#INPerson phonenumber handle type %s"
+ "#INPerson unknown name"
+ "#SendOnDismissPerformAppIntentBuilder built spec bundleId=%{public}s actionId=%{public}s parameters count=%ld"
+ "#SendOnDismissPerformAppIntentBuilder failed to encode AppIntentSpecification: %@"
+ "#SendOnDismissPerformAppIntentBuilder made SAUIPerformAppIntent aceId=%{public}s"
+ "#SendOnDismissPerformAppIntentBuilder make begin bundleId=%{public}s mapped intentPersons=%ld"
+ "#SendOnDismissPerformAppIntentBuilder no messages.sendMessage AppIntent for %{public}s; aborting"
+ "#SendOnDismissPerformAppIntentBuilder no recipients to send to; aborting"
+ "#SendOnDismissPerformAppIntentBuilder tool %{public}s has no .appIntent system protocol; app does not conform to the sendMessage AppIntent schema, aborting"
+ "Messages#MessageRetrievalUnavailable"
+ "SendMessage#ConfirmTapbackType"
+ "contactHandle://"
+ "doneAssociatedEntitiesData"
+ "sendOnDismissCommand"
+ "shouldMentionLast"
```
