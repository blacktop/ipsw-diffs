## InCallService

> `/Applications/InCallService.app/InCallService`

```diff

-3027.200.37.2.2
-  __TEXT.__text: 0x24fce4
+3027.200.64.0.0
+  __TEXT.__text: 0x24fdb0
   __TEXT.__auth_stubs: 0x6320
   __TEXT.__objc_stubs: 0x28380
   __TEXT.__objc_methlist: 0x182b0
   __TEXT.__cstring: 0x1146d
-  __TEXT.__objc_methname: 0x3facb
+  __TEXT.__objc_methname: 0x3fade
   __TEXT.__objc_classname: 0x1fe1
   __TEXT.__objc_methtype: 0x7cfb
-  __TEXT.__const: 0x8404
-  __TEXT.__oslogstring: 0x20cfd
+  __TEXT.__const: 0x8414
+  __TEXT.__oslogstring: 0x20b8d
   __TEXT.__gcc_except_tab: 0x1c90
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x92d6
+  __TEXT.__swift5_typeref: 0x9308
   __TEXT.__swift5_reflstr: 0x3849
   __TEXT.__swift5_assocty: 0x830
   __TEXT.__constg_swiftt: 0x55ec

   __DATA.__objc_selrefs: 0xdbc0
   __DATA.__objc_ivar: 0x11dc
   __DATA.__objc_data: 0xa0a8
-  __DATA.__data: 0x8fa8
+  __DATA.__data: 0x8fb8
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x7ca8
   __DATA.__common: 0x320

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7FD50572-E1BE-341E-80C5-9F7CEC364462
+  UUID: BC0AA39F-114E-3878-ABB0-A9AECAE48979
   Functions: 14428
   Symbols:   3164
-  CStrings:  15255
+  CStrings:  15253
 
Symbols:
+ _$s16CommunicationsUI29CallTranslationLanguagePickerV7current14possibleLocale9viewModel03usedF022shouldShowCancelButton17previousSelection16languageSelected14wantsToDismissAC10Foundation0I0V_ANSg0A6UICore0er4ViewK0CSgS2bAN5local_AN6remotetSgyAN_ANtcSgyycSgtcfC
- _$s16CommunicationsUI29CallTranslationLanguagePickerV7current14possibleLocale9viewModel03usedF022shouldShowCancelButton16languageSelected14wantsToDismissAC10Foundation0I0V_AMSg0A6UICore0e13SelectionViewK0CSgS2byAM_AMtcSgyycSgtcfC
CStrings:
+ "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d)"
+ "There is more than one contact associated with this call, using the first identifier."
+ "isRestrictedExclusivelyByScreenTimeForDialRequest:"
- "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n [[FTDeviceSupport sharedInstance] isGreenTea]): %d"
- "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n self.featureFlags.callEndSpamUIEnhancementEnabled): %d"
- "Failed to present contact card: multiple contact identifiers"
- "callEndSpamUIEnhancementEnabled"
- "not a greentea device && callEndSpamUIEnhancementEnabled is disabled, so we don't show the end call screen"

```
