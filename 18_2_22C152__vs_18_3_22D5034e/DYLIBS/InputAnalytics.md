## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`

```diff

-64.218.1.0.0
-  __TEXT.__text: 0x1ec80
-  __TEXT.__auth_stubs: 0x830
+64.223.0.0.0
+  __TEXT.__text: 0x1f190
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_methlist: 0x2300
-  __TEXT.__const: 0x282
-  __TEXT.__gcc_except_tab: 0x6a8
-  __TEXT.__oslogstring: 0x28b0
-  __TEXT.__cstring: 0x4692
+  __TEXT.__const: 0x272
+  __TEXT.__gcc_except_tab: 0x468
+  __TEXT.__oslogstring: 0x29f0
+  __TEXT.__cstring: 0x4822
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x8a
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x8b8
+  __TEXT.__unwind_info: 0x898
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x711
-  __TEXT.__objc_methname: 0x4c78
-  __TEXT.__objc_methtype: 0x9c1
-  __TEXT.__objc_stubs: 0x3020
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x1238
+  __TEXT.__objc_classname: 0x712
+  __TEXT.__objc_methname: 0x4c47
+  __TEXT.__objc_methtype: 0x9ad
+  __TEXT.__objc_stubs: 0x3080
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x12b8
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10e0
+  __DATA_CONST.__objc_selrefs: 0x10e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0xdb0
-  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__const: 0x4b8
-  __AUTH_CONST.__cfstring: 0x67e0
+  __AUTH_CONST.__const: 0x518
+  __AUTH_CONST.__cfstring: 0x69c0
   __AUTH_CONST.__objc_const: 0x4828
-  __AUTH_CONST.__objc_intobj: 0x708
+  __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x7f0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x244
   __DATA.__data: 0x370
   __DATA.__common: 0x8
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 947
-  Symbols:   604
-  CStrings:  2071
+  Functions: 960
+  Symbols:   617
+  CStrings:  2094
 
Symbols:
+ _IAPayloadKeyGenmojiCreationFaceID
+ _IAPayloadKeyGenmojiCreationFaceIDList
+ _IAPayloadKeyGenmojiCreationNumItems
+ _IAPayloadKeyGenmojiCreationPickerType
+ _IAPayloadValueGenmojiCreationPickerTypeCharacter
+ _IAPayloadValueGenmojiCreationPickerTypePhoto
+ _IASignalGenmojiCreationFacePickerCarouselDismissed
+ _IASignalGenmojiCreationFacePickerCarouselFacesUpdated
+ _IASignalGenmojiCreationFacePickerCarouselPreviewLoaded
+ _IASignalGenmojiCreationFacePickerCarouselUpdatingFaces
+ _IASignalGenmojiCreationPeoplePickerAppeared
+ _IASignalGenmojiCreationPeoplePickerDisappeared
+ _IASignalGenmojiCreationPeoplePickerGridAppeared
+ _IASignalGenmojiCreationPeoplePickerGridUpdated
+ _IASignalGenmojiCreationPeoplePickerItemSelected
+ _IASignalGenmojiCreationPeoplePickerPickerRequested
+ __os_feature_enabled_impl
- _OBJC_EHTYPE_$_NSException
- _objc_begin_catch
- _objc_end_catch
- _objc_getProperty
CStrings:
+ "0x%lx calling connection resume after shared instance"
+ "0x%lx calling connection resume before shared instance"
+ "0x%lx using per-call remote object proxy with IXAXPCProtocol. Calling connection resume now"
+ "0x%lx using shared remote object proxy"
+ "Character"
+ "FaceID"
+ "FaceIDList"
+ "FacePickerCarouselDismissed"
+ "FacePickerCarouselFacesUpdated"
+ "FacePickerCarouselPreviewLoaded"
+ "FacePickerCarouselUpdatingFaces"
+ "IAXPCclient 0x%lx init created _connection 0x%lx _server 0x%lx with IXAXPCProtocol"
+ "IXAXPCProtocol"
+ "InputAnalytics"
+ "NumItems"
+ "PeoplePickerAppeared"
+ "PeoplePickerDisappeared"
+ "PeoplePickerGridAppeared"
+ "PeoplePickerGridUpdated"
+ "PeoplePickerItemSelected"
+ "PeoplePickerPickerRequested"
+ "PickerType"
+ "T@\"IAXPCProtocolObject\",R"
+ "_serverInstance"
+ "flushAndSetLastAction: server does not respond to didAction. xpc client 0x%lx with server 0x%lx "
+ "initWithAnalyticsMetadataObserver in-process"
+ "mergeOrConsumeAction: server does not respond to didSessionBeginWithSessionMetadata. xpc client 0x%lx with server 0x%lx "
+ "mergeOrConsumeAction: server does not respond to didSessionEndWithSessionMetadata. xpc client 0x%lx with server 0x%lx "
+ "perCallXPCProxyObject"
+ "removeObject:"
+ "sendSignal:toChannel:withNullableSessionID:withPayload: server does not respond to didAction. xpc client 0x%lx with server 0x%lx"
+ "sendSignal:toChannel:withNullableUniqueStringID:withPayload: server does not respond to didAction. xpc client 0x%lx with server 0x%lx"
+ "sendSignal:toChannel:withPayload: server does not respond to didAction. xpc client 0x%lx with server 0x%lx"
+ "xpcConnectionResumeBeforeSharedObject"
+ "xpcEnabled"
- "B48@0:8@16@24@32@40"
- "IAXPCProtocol"
- "IAXPCclient 0x%lx init created _connection 0x%lx _server 0x%lx"
- "T@\"IAXPCProtocolObject\",R,V_server"
- "_server"
- "checkAndHandleSpecialCasesWithChannel:signal:withUniqueStringID:payload:"
- "flushAndSetLastAction called didAction on xpc client 0x%lx with server 0x%lx and failed with %@"
- "mergeOrConsumeAction calling didSessionBeginWithSessionMetadata on xpc client 0x%lx with server 0x%lx and failed with %@"
- "mergeOrConsumeAction calling didSessionEndWithSessionMetadata on xpc client 0x%lx with server 0x%lx and failed with %@"
- "sendSignal:toChannel:withPayload: called didAction on xpc client 0x%lx with server 0x%lx and failed with %@"
- "sendSignal:toChannel:withSessionID:withPayload: called didAction on xpc client 0x%lx with server 0x%lx and failed with %@"
- "sendSignal:toChannel:withUniqueStringID:withPayload: called didAction on xpc client 0x%lx with server 0x%lx and failed with %@"

```
