## SiriKitInvocation

> `/System/Library/PrivateFrameworks/SiriKitInvocation.framework/SiriKitInvocation`

```diff

-3500.3.1.0.0
-  __TEXT.__text: 0x5cc4
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x598
+3520.3.1.0.0
+  __TEXT.__text: 0x6880
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_methlist: 0x618
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xbf1
-  __TEXT.__oslogstring: 0x520
-  __TEXT.__unwind_info: 0x160
-  __TEXT.__objc_classname: 0x1a7
-  __TEXT.__objc_methname: 0x1826
-  __TEXT.__objc_methtype: 0x1c9
-  __TEXT.__objc_stubs: 0x1060
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x408
-  __DATA_CONST.__objc_classlist: 0x78
+  __TEXT.__cstring: 0xc49
+  __TEXT.__oslogstring: 0x68c
+  __TEXT.__unwind_info: 0x180
+  __TEXT.__objc_classname: 0x1ee
+  __TEXT.__objc_methname: 0x1932
+  __TEXT.__objc_methtype: 0x1da
+  __TEXT.__objc_stubs: 0x10e0
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x420
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b8
+  __DATA_CONST.__objc_selrefs: 0x5e8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x158
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xc20
-  __AUTH_CONST.__objc_const: 0xcc8
-  __AUTH.__objc_data: 0x3c0
+  __AUTH_CONST.__cfstring: 0xc60
+  __AUTH_CONST.__objc_const: 0xde8
+  __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0xc8
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9672601-FBE3-393A-A274-06C6DAD3DA52
-  Functions: 125
-  Symbols:   719
-  CStrings:  494
+  UUID: 962D1084-F64E-31E9-BD46-E59A7535E34F
+  Functions: 143
+  Symbols:   790
+  CStrings:  513
 
Symbols:
+ +[SKIAnnounceDirectInvocationUtilities announcePayloadFromUserData:payloadKey:]
+ +[SKIAnnounceDirectInvocationUtilities announcePayloadFromUserData:payloadKey:].cold.1
+ +[SKIAnnounceDirectInvocationUtilities updateDict:withAnnouncePayload:payloadKey:]
+ +[SKIAnnounceDirectInvocationUtilities updateDict:withAnnouncePayload:payloadKey:].cold.1
+ +[SKIAnnounceDirectInvocationUtilities updateStartLocalRequest:withNewAnnouncePayload:payloadKey:]
+ +[SKIAnnounceDirectInvocationUtilities updateStartLocalRequest:withNewAnnouncePayload:payloadKey:].cold.1
+ +[SKIAnnounceDirectInvocationUtilities updateStartLocalRequest:withNewAnnouncePayload:payloadKey:].cold.2
+ +[SKIAnnounceDirectInvocationUtilities updateStartLocalRequest:withNewAnnouncePayload:payloadKey:].cold.3
+ +[SKIFoundationalAnnounceInvocation announceBinaryOutcome:announcePayload:]
+ +[SKIFoundationalAnnounceInvocation announcePayloadFromUserData:]
+ +[SKIFoundationalAnnounceInvocation binaryOutcomeAnnounceRequestFromUserData:]
+ +[SKIFoundationalAnnounceInvocation binaryOutcomeAnnounceRequestFromUserData:].cold.1
+ +[SKIFoundationalAnnounceInvocation updateDict:withAnnouncePayload:]
+ +[SKIFoundationalAnnounceInvocation updateDict:withBinaryOutcomeAnnounceRequest:]
+ +[SKIFoundationalAnnounceInvocation updateDict:withBinaryOutcomeAnnounceRequest:].cold.1
+ +[SKIFoundationalAnnounceInvocation updateStartLocalRequest:withNewAnnouncePayload:]
+ _OBJC_CLASS_$_AFAnnounceBinaryOutcomeRequest
+ _OBJC_CLASS_$_SKIAnnounceDirectInvocationUtilities
+ _OBJC_CLASS_$_SKIFoundationalAnnounceInvocation
+ _OBJC_METACLASS_$_SKIAnnounceDirectInvocationUtilities
+ _OBJC_METACLASS_$_SKIFoundationalAnnounceInvocation
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _SKIFoundationalAnnounceInvocationIdentifierAnnounceBinaryOutcome
+ _SKIFoundationalAnnounceInvocationPayloadKeyAnnouncePayload
+ _SKIFoundationalAnnounceInvocationPayloadKeyBinaryOutcomeRequest
+ __OBJC_$_CLASS_METHODS_SKIAnnounceDirectInvocationUtilities
+ __OBJC_$_CLASS_METHODS_SKIFoundationalAnnounceInvocation
+ __OBJC_CLASS_RO_$_SKIAnnounceDirectInvocationUtilities
+ __OBJC_CLASS_RO_$_SKIFoundationalAnnounceInvocation
+ __OBJC_METACLASS_RO_$_SKIAnnounceDirectInvocationUtilities
+ __OBJC_METACLASS_RO_$_SKIFoundationalAnnounceInvocation
+ _objc_msgSend$announcePayloadFromUserData:payloadKey:
+ _objc_msgSend$updateDict:withAnnouncePayload:payloadKey:
+ _objc_msgSend$updateDict:withBinaryOutcomeAnnounceRequest:
+ _objc_msgSend$updateStartLocalRequest:withNewAnnouncePayload:payloadKey:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "Error deserializing SKIDirectInvocationPayload: %@"
+ "SKIAnnounceDirectInvocationUtilities"
+ "SKIDirectInvocationPayload contains nil data"
+ "SKIFoundationalAnnounceInvocation"
+ "announceBinaryOutcome:announcePayload:"
+ "announcePayloadFromUserData:payloadKey:"
+ "binaryOutcomeAnnounceRequestFromUserData:"
+ "binaryOutcomeRequest"
+ "com.apple.siri.directInvocation.foundationalAnnounce.binaryOutcome"
+ "error archiving AFAnnounceBinaryOutcomeRequest: %@"
+ "error archiving SKIAnnounceNotificationDirectInvocationPayload: %@"
+ "error unarchiving AFAnnounceBinaryOutcomeRequest from userData: %@"
+ "error unarchiving SKIAnnounceNotificationDirectInvocationPayload from userData: %@"
+ "updateDict:withAnnouncePayload:payloadKey:"
+ "updateDict:withBinaryOutcomeAnnounceRequest:"
+ "updateStartLocalRequest:withNewAnnouncePayload:payloadKey:"
+ "v40@0:8@16@24@32"

```
