## PebblePlayCore

> `/System/Library/PrivateFrameworks/PebblePlayCore.framework/PebblePlayCore`

```diff

-164.2.4.0.0
-  __TEXT.__text: 0x16d38c
-  __TEXT.__objc_methlist: 0x1a3c
-  __TEXT.__const: 0x10910
-  __TEXT.__cstring: 0x5a22
-  __TEXT.__oslogstring: 0x1b65
+178.0.0.0.0
+  __TEXT.__text: 0x17bd8c
+  __TEXT.__objc_methlist: 0x1bbc
+  __TEXT.__const: 0x10e70
+  __TEXT.__cstring: 0x62a2
+  __TEXT.__oslogstring: 0x21e5
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__constg_swiftt: 0x39fc
-  __TEXT.__swift5_typeref: 0x42dc
+  __TEXT.__constg_swiftt: 0x3b8c
+  __TEXT.__swift5_typeref: 0x437c
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x1f33
-  __TEXT.__swift5_fieldmd: 0x2024
-  __TEXT.__swift5_assocty: 0x600
-  __TEXT.__swift5_proto: 0x69c
-  __TEXT.__swift5_types: 0x26c
-  __TEXT.__swift5_capture: 0x2888
-  __TEXT.__swift_as_entry: 0x944
-  __TEXT.__swift_as_cont: 0x1738
+  __TEXT.__swift5_reflstr: 0x2143
+  __TEXT.__swift5_fieldmd: 0x21a0
+  __TEXT.__swift5_assocty: 0x630
+  __TEXT.__swift5_proto: 0x6d0
+  __TEXT.__swift5_types: 0x274
+  __TEXT.__swift5_capture: 0x2904
+  __TEXT.__swift_as_entry: 0x964
+  __TEXT.__swift_as_cont: 0x1760
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_acfuncs: 0xc80
-  __TEXT.__swift_as_ret: 0x910
+  __TEXT.__swift5_acfuncs: 0xca8
+  __TEXT.__swift_as_ret: 0x930
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7928
-  __TEXT.__eh_frame: 0x15444
+  __TEXT.__unwind_info: 0x7c08
+  __TEXT.__eh_frame: 0x15d1c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x280
-  __DATA_CONST.__objc_classlist: 0x210
+  __DATA_CONST.__const: 0x2c8
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf8
+  __DATA_CONST.__objc_selrefs: 0xbb0
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x710
-  __AUTH_CONST.__const: 0x7890
-  __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x4d20
-  __AUTH_CONST.__auth_got: 0x1250
-  __AUTH.__objc_data: 0x2bd8
-  __AUTH.__data: 0x3668
+  __DATA_CONST.__got: 0x7e0
+  __AUTH_CONST.__const: 0x7cb8
+  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__objc_const: 0x4f28
+  __AUTH_CONST.__auth_got: 0x12b0
+  __AUTH.__objc_data: 0x2ca8
+  __AUTH.__data: 0x3738
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x3a50
+  __DATA.__data: 0x3b70
   __DATA.__common: 0x130
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6741
-  Symbols:   2121
-  CStrings:  702
+  Functions: 6883
+  Symbols:   2182
+  CStrings:  776
 
Symbols:
+ +[SPAVRoute remoteDeviceControlIsAllowed]
+ -[SPAVRoute _handleCallIsActiveChanged:]
+ -[SPAVRoute _handleCarPlayIsConnectedChanged:]
+ -[SPAVRoute _handleDeviceIsBeingObservedRemotelyChanged:]
+ -[SPAVRoute _handlePreferredExternalRouteChanged:]
+ -[SPAVRoute _handleRemoteDeviceControlIsAllowedChanged:]
+ -[SPAVRoute _handleSomeClientIsActiveChanged:]
+ -[SPAVRoute _handleSomeSessionIsPlayingChanged:]
+ -[SPAVRoute _handleVideoStreamsChanged:]
+ -[SPAVRoute airPlayBidirectionalAudioSessionID]
+ -[SPAVRoute airPlayServerConnectionInfo]
+ _AVSystemController_CallIsActiveDidChangeNotification
+ _AVSystemController_CallIsActiveNotificationParameter
+ _AVSystemController_CallIsHighPriorityNotificationParameter
+ _AVSystemController_CarPlayIsConnectedDidChangeNotification
+ _AVSystemController_CarPlayIsConnectedNotificationParameter
+ _AVSystemController_DeviceIsBeingObservedRemotelyDidChangeNotification
+ _AVSystemController_DeviceIsBeingObservedRemotelyDidChangeNotificationParameter
+ _AVSystemController_PreferredExternalRouteDidChangeNotification
+ _AVSystemController_RemoteDeviceControlIsAllowedDidChangeNotification
+ _AVSystemController_RemoteDeviceControlIsAllowedDidChangeNotificationParameter_Reason
+ _AVSystemController_SomeClientIsActiveDidChangeNotification
+ _AVSystemController_SomeClientIsActiveDidChangeNotificationParameter_AudioCategory
+ _AVSystemController_SomeClientIsActiveDidChangeNotificationParameter_AudioSessionID
+ _AVSystemController_SomeClientIsActiveDidChangeNotificationParameter_IsActive
+ _AVSystemController_SomeSessionIsPlayingDidChangeNotification
+ _AVSystemController_SomeSessionIsPlayingDidChangeNotificationParameter_Sessions
+ _AVSystemController_VideoStreamsDidChangeNotification
+ _AVSystemController_VideoStreamsDidChangeNotificationParameter_BundleID
+ _AVSystemController_VideoStreamsDidChangeNotificationParameter_RouteNames
+ _CGSizeMake
+ _OBJC_CLASS_$_CPPlaybackItemIdentifier
+ _OBJC_CLASS_$_IXPromisedInMemoryDictionary
+ _OBJC_CLASS_$_MRDeviceInfoRequest
+ __IVARS__TtC14PebblePlayCore23PPTabBarTemplateWrapper
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_SPAVRoute
+ ___41+[SPAVRoute remoteDeviceControlIsAllowed]_block_invoke
+ ___46-[SPAVRoute _handleCarPlayIsConnectedChanged:]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ ___swift_closure_destructor.1112Tm
+ ___swift_closure_destructor.1122Tm
+ ___swift_closure_destructor.133Tm
+ ___swift_closure_destructor.137Tm
+ ___swift_closure_destructor.17Tm
+ ___swift_closure_destructor.631Tm
+ ___swift_closure_destructor.663Tm
+ ___swift_closure_destructor.678Tm
+ ___swift_closure_destructor.786Tm
+ ___swift_closure_destructor.877Tm
+ ___unnamed_15
+ __os_log_error_impl
+ _associated conformance 14PebblePlayCore13AppExitReasonOSHAASQ
+ _associated conformance 14PebblePlayCore23PPTabBarTemplateWrapperC10CodingKeys33_E3D2AB688428DA8C45A97A9DD91F5282LLOSHAASQ
+ _associated conformance 14PebblePlayCore23PPTabBarTemplateWrapperC10CodingKeys33_E3D2AB688428DA8C45A97A9DD91F5282LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 14PebblePlayCore23PPTabBarTemplateWrapperC10CodingKeys33_E3D2AB688428DA8C45A97A9DD91F5282LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _dispatch_once
+ _objc_opt_isKindOfClass
+ _objc_retain_x9
+ _remoteDeviceControlIsAllowed.classLogger
+ _remoteDeviceControlIsAllowed.onceToken
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _symbolic SS________________pIetMHgTnTgzo_ 14PebblePlayCore13AppExitReasonO AA011ApplicationE18ProviderActorProxyC s5ErrorP
+ _symbolic ScCySb_____G s5NeverO
+ _symbolic So24CPPlaybackItemIdentifierC
+ _symbolic So25CPListImageRowItemElementC7element_So7UIImageCSg8originalSS3keyt
+ _symbolic _____ 14PebblePlayCore13AppExitReasonO
+ _symbolic _____ 14PebblePlayCore23PPTabBarTemplateWrapperC10CodingKeys33_E3D2AB688428DA8C45A97A9DD91F5282LLO
+ _symbolic _____SSSi_____Sb______pIetMHnTgTyTgdzo_ 10Foundation4UUIDV 14PebblePlayCore33PPListClientTemplateDelegateActorC s5ErrorP
+ _symbolic _____XDXMT 14PebblePlayCore33PPListClientTemplateDelegateActorC
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____ySo25CPListImageRowItemElementC7element_So7UIImageCSg8originalSS3keytG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G 11Distributed18RemoteCallArgumentV 14PebblePlayCore13AppExitReasonO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14PebblePlayCore23PPTabBarTemplateWrapperC10CodingKeys33_E3D2AB688428DA8C45A97A9DD91F5282LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 14PebblePlayCore23PPTabBarTemplateWrapperC10CodingKeys33_E3D2AB688428DA8C45A97A9DD91F5282LLO
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
- ___swift_closure_destructor.1107Tm
- ___swift_closure_destructor.1117Tm
- ___swift_closure_destructor.121Tm
- ___swift_closure_destructor.37Tm
- ___swift_closure_destructor.626Tm
- ___swift_closure_destructor.658Tm
- ___swift_closure_destructor.673Tm
- ___swift_closure_destructor.781Tm
- ___swift_closure_destructor.82Tm
- ___swift_closure_destructor.872Tm
- ___unnamed_17
- _symbolic So25CPListImageRowItemElementC7element_So7UIImageCSg8originalt
- _symbolic _____ySo16CPTabBarTemplateCG 14PebblePlayCore9PPWrapperC
- _symbolic _____ySo16CPTabBarTemplateC_G 14PebblePlayCore9PPWrapperC10CodingKeys33_E3D2AB688428DA8C45A97A9DD91F5282LLO
- _symbolic _____ySo25CPListImageRowItemElementC7element_So7UIImageCSg8originaltG s23_ContiguousArrayStorageC
- _symbolic _____y_____ySo16CPTabBarTemplateC_GG s22KeyedDecodingContainerV 14PebblePlayCore9PPWrapperC10CodingKeys33_E3D2AB688428DA8C45A97A9DD91F5282LLO
CStrings:
+ " - confirming without prompt"
+ " - proceeding without entitlements"
+ "%@ AVSystemController CarPlay connected changed - connected: %@"
+ "%@ AVSystemController call active changed - active: %@, highPriority: %@"
+ "%@ AVSystemController device being observed remotely changed - observed: %@"
+ "%@ AVSystemController preferred external route changed"
+ "%@ AVSystemController remote device control allowed changed - reason: %@ (%u)"
+ "%@ AVSystemController some client active changed - active: %@, sessionID: %@, category: %@, userInfo: %@"
+ "%@ AVSystemController some session playing changed - sessions: %@"
+ "%@ AVSystemController video streams changed - bundleID: %@, routes: %@"
+ "%s:%s %s took: %s seconds"
+ "); returning unique sentinel"
+ "1.8.12"
+ "1.8.16"
+ "1.8.17"
+ "; not confirming"
+ "ActivePhoneCallInProgress"
+ "AirPlay bidirectional audio session ID from MR: %@"
+ "AirPlay server connection info from MR: %@"
+ "Allowed"
+ "AssistantIsActive"
+ "Conversational Apps"
+ "Delegate does not implement requestPlaybackConfirmation; falling back to didSelect for list item "
+ "Delegate does not implement requestPlaybackConfirmation; no didSelect fallback for details header "
+ "Delegate does not implement requestPlaybackConfirmation; no didSelect fallback for image-row element "
+ "Disallowed"
+ "Entitlements config for "
+ "Entitlements for "
+ "Entitlements for %s: keys=%s; associated-domains present: %{bool}d"
+ "Failed to create IXPromisedInMemoryDictionary for entitlements for "
+ "Failing presentVoiceTemplate — remote device control not allowed"
+ "Failing pushVoiceControlTemplate — remote device control not allowed"
+ "Failure sanitizing bundle: "
+ "Getting entitlements"
+ "Identified embedded directory %s - deleting"
+ "MRDeviceInfo airPlayBidirectionalAudioSessionID is not a number: %@"
+ "MRDeviceInfo does not expose airPlayBidirectionalAudioSessionID"
+ "MRDeviceInfo does not expose airPlayServerConnectionInfo"
+ "MicrophoneIsBeingUsed"
+ "No PlaceholderEntitlements.plist for %s"
+ "PPListTemplateItemWrapper: extraction returned nil skeleton, falling back to legacy"
+ "PPListTemplateItemWrapper: skeleton unarchive returned nil"
+ "PPListTemplateItemWrapper: skeleton unarchive threw: "
+ "PPTabBarTemplateWrapper dedupHash: encode failed ("
+ "PPTabBarTemplateWrapper legacy unarchive: "
+ "PPTabBarTemplateWrapper: extraction returned nil skeleton, falling back to legacy"
+ "PPTabBarTemplateWrapper: no data fields populated"
+ "PPTabBarTemplateWrapper: skeleton unarchive returned nil"
+ "PPTabBarTemplateWrapper: skeleton unarchive threw: "
+ "Placeholder path for %s: legacy (no serialized placeholder data - entitlements will not be transferred)"
+ "Placeholder path for %s: packaged (bundle available)"
+ "PlaceholderEntitlements.plist"
+ "Playback confirmation for %s#%ld: %{bool}d"
+ "Read %ld entitlements from PlaceholderEntitlements.plist for %s"
+ "Remote device control not allowed - reason: %@ (%u)"
+ "Set entitlements in placeholder %@"
+ "Unknown"
+ "User tapped action button, controlIdentifier: %s"
+ "User tapped album-artist button"
+ "User tapped alert action, identifier: %s"
+ "User tapped up-next button"
+ "] listTemplate requestPlaybackConfirmation ["
+ "airPlayBidirectionalAudioSessionID"
+ "carPlayConnected"
+ "com.apple.developer.associated-domains"
+ "com.apple.private.pebbleplay-placeholder"
+ "conversationAppInterrupted"
+ "extractAndArchive(root:id:rows:peerSupportsThumbnailJPEG:)"
+ "lastUpdateTime"
+ "listTemplate(withIdentifier:requestPlaybackConfirmationForMatching:)"
+ "listTemplate: %s - requestPlaybackConfirmation: %s#%ld"
+ "numThrottles"
+ "reinject(rows:sidecar:id:)"
+ "remoteDeviceControlNotAllowed"
+ "requestPlaybackConfirmation failed: "
+ "requestPlaybackConfirmation(withListIdentifier:itemIdentifier:elementIndex:)"
+ "skipped duplicate, sizeKB: "
+ "withListIdentifier"
- "%s:%s %s took: %s"
- "Failure santizing bundle: "
- "Identified PlugIns directory %s - deleting"
- "extractAndArchive(template:peerSupportsThumbnailJPEG:)"
```
