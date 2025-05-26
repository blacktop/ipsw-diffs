## PeopleMessageService

> `/Applications/PeopleMessageService.app/PeopleMessageService`

```diff

-84.11.0.0.0
-  __TEXT.__text: 0xf234
-  __TEXT.__auth_stubs: 0xcf0
+84.14.0.0.0
+  __TEXT.__text: 0x10f40
+  __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_stubs: 0x100
   __TEXT.__objc_methlist: 0x130
   __TEXT.__objc_classname: 0x7f
   __TEXT.__objc_methname: 0x1154
   __TEXT.__objc_methtype: 0xb26
-  __TEXT.__cstring: 0xbb4
+  __TEXT.__cstring: 0xc64
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0x294
   __TEXT.__constg_swiftt: 0x224
-  __TEXT.__swift5_typeref: 0x238
+  __TEXT.__swift5_typeref: 0x240
   __TEXT.__swift5_fieldmd: 0xc4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x98

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_capture: 0x54
-  __TEXT.__unwind_info: 0x2ec
-  __TEXT.__eh_frame: 0x778
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x188
+  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__eh_frame: 0x7a8
+  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x350
   __DATA_CONST.__cfstring: 0x20

   __DATA.__objc_const: 0x11b8
   __DATA.__objc_selrefs: 0x1b0
   __DATA.__objc_data: 0x3f8
-  __DATA.__data: 0x540
+  __DATA.__data: 0x558
   __DATA.__bss: 0x300
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/LinkPresentation.framework/LinkPresentation
   - /System/Library/Frameworks/Messages.framework/Messages
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AskToCore.framework/AskToCore
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 156
-  Symbols:   351
-  CStrings:  315
+  Functions: 159
+  Symbols:   362
+  CStrings:  318
 
Symbols:
+ _$s10Foundation12URLQueryItemV4nameSSvg
+ _$s5AskTo10ATQuestionC16notificationTextSSSgvg
+ _$s5AskTo10ATQuestionC7summarySSvg
+ _$s6People14MessageDetailsV19notificationCaptionSSvs
+ _$s6People14ResolvedFamilyV9approversSaySo14FAFamilyMemberCGvg
+ _$s6People16MessageSendRulesC01iB7Handles3for6lookupAA010DiscoveredE0VSaySo14FAFamilyMemberCG_AA0B30DeviceCapabilityLookupProvider_ptYaFTjTu
+ _$s6People16MessageSendRulesC027approversSupportingAskToBuyB0_6lookupAA17DiscoveredHandlesVSaySo14FAFamilyMemberCG_AA0B30DeviceCapabilityLookupProvider_ptYaFTjTu
+ _$s6People16MessageSendRulesC029approversSupportingScreenTimeB0_6lookupAA17DiscoveredHandlesVSaySo14FAFamilyMemberCG_AA0B30DeviceCapabilityLookupProvider_ptYaFTjTu
+ _$s6People16MessageSendRulesC04willC15AskToBuyRequest4from2to6client17discoveredHandlesSbSo14FAFamilyMemberC_SayAJGSbAA010DiscoveredN0VSgtYaFTjTu
+ _$s6People16MessageSendRulesC04willC17ScreenTimeRequest4from2to6client17discoveredHandlesSbSo14FAFamilyMemberC_SayAJGSbAA010DiscoveredM0VSgtYaFTjTu
+ _$s9AskToCore5ATURLO6ParserV5parse_4fromxxm_10Foundation3URLVtKSeRzSERzlF
+ _$s9AskToCore5ATURLO6ParserVAEycfC
+ _$s9AskToCore5ATURLO6ParserVMa
+ _$s9AskToCore9ATPayloadC8question0aB010ATQuestionCvg
+ _$s9AskToCore9ATPayloadCMa
+ _$s9AskToCore9ATPayloadCSEAAMc
+ _$s9AskToCore9ATPayloadCSeAAMc
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_errorRetain
- _$s6People14ResolvedFamilyV24approversIMessageHandles6lookupAA010DiscoveredF0VAA37MessageDeviceCapabilityLookupProvider_p_tYaF
- _$s6People14ResolvedFamilyV24approversIMessageHandles6lookupAA010DiscoveredF0VAA37MessageDeviceCapabilityLookupProvider_p_tYaFTu
- _$s6People14ResolvedFamilyV34approversSupportingAskToBuyMessage6lookupAA17DiscoveredHandlesVAA0I30DeviceCapabilityLookupProvider_p_tYaF
- _$s6People14ResolvedFamilyV34approversSupportingAskToBuyMessage6lookupAA17DiscoveredHandlesVAA0I30DeviceCapabilityLookupProvider_p_tYaFTu
- _$s6People14ResolvedFamilyV36approversSupportingScreenTimeMessage6lookupAA17DiscoveredHandlesVAA0H30DeviceCapabilityLookupProvider_p_tYaF
- _$s6People14ResolvedFamilyV36approversSupportingScreenTimeMessage6lookupAA17DiscoveredHandlesVAA0H30DeviceCapabilityLookupProvider_p_tYaFTu
- _$s6People16MessageSendRulesC04willC15AskToBuyRequest2to6client17discoveredHandlesSbAA14ResolvedFamilyV_SbAA010DiscoveredM0VSgtYaFTjTu
- _$s6People16MessageSendRulesC04willC17ScreenTimeRequest2to6client17discoveredHandlesSbAA14ResolvedFamilyV_SbAA010DiscoveredL0VSgtYaFTjTu
- _objc_retain_x28
CStrings:
+ "Appending %ld additional components to conversation url: %s"
+ "AskTo supplied the thumbnail data. Removing the existing thumbnailData."
+ "Could not parse ATPayload from baseURL %s, error: %@"
+ "Failed to parse AskTo Payload"
- "Appending %ld additional components to conversation url"

```
