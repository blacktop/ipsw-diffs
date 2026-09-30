## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1440.100.7.2.5
-  __TEXT.__text: 0xb5f48
-  __TEXT.__auth_stubs: 0x1a70
-  __TEXT.__objc_stubs: 0xbc00
-  __TEXT.__objc_methlist: 0x2924
-  __TEXT.__const: 0xb98
-  __TEXT.__gcc_except_tab: 0xb3a0
-  __TEXT.__cstring: 0x339d
-  __TEXT.__oslogstring: 0x15ff6
+1443.100.10.1.5
+  __TEXT.__text: 0xb683c
+  __TEXT.__auth_stubs: 0x1aa0
+  __TEXT.__objc_stubs: 0xbd00
+  __TEXT.__objc_methlist: 0x2934
+  __TEXT.__const: 0xba0
+  __TEXT.__gcc_except_tab: 0xb3bc
+  __TEXT.__cstring: 0x33ad
+  __TEXT.__oslogstring: 0x16096
   __TEXT.__objc_classname: 0x50a
-  __TEXT.__objc_methname: 0x119fd
+  __TEXT.__objc_methname: 0x11b54
   __TEXT.__objc_methtype: 0x290b
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x63e

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift5_capture: 0x264
+  __TEXT.__swift5_capture: 0x284
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2278
-  __TEXT.__eh_frame: 0x630
-  __DATA_CONST.__auth_got: 0xd48
-  __DATA_CONST.__got: 0xfb8
+  __TEXT.__unwind_info: 0x2290
+  __TEXT.__eh_frame: 0x680
+  __DATA_CONST.__auth_got: 0xd60
+  __DATA_CONST.__got: 0xfc8
   __DATA_CONST.__auth_ptr: 0x168
-  __DATA_CONST.__const: 0x3740
-  __DATA_CONST.__cfstring: 0x3720
+  __DATA_CONST.__const: 0x3790
+  __DATA_CONST.__cfstring: 0x36c0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x2e20
-  __DATA.__objc_selrefs: 0x37c0
+  __DATA.__objc_const: 0x2e38
+  __DATA.__objc_selrefs: 0x37f8
   __DATA.__objc_ivar: 0x1d0
   __DATA.__objc_data: 0x9b8
   __DATA.__data: 0xa38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AEAEE6F3-CE52-3687-A54B-86080642013C
-  Functions: 1582
-  Symbols:   845
-  CStrings:  4928
+  UUID: DD2661F8-7E8D-35ED-8AD4-95B67056FA5C
+  Functions: 1590
+  Symbols:   849
+  CStrings:  4932
 
Symbols:
+ _IDSRegistrationPropertySupportsPolls
+ _IMBalloonPluginFallbackText
+ _IMSharedHelperCustomAcknowledgementBackwardsCompatibilityEnabled
+ _OBJC_CLASS_$_IMNetworkMonitor
CStrings:
+ "-[MessageServiceSession messageDeliveryController:didFlushCacheForRemoteURI:fromURI:guid:]"
+ "Sending fallback text message for required capabilities"
+ "Skipping cache check in %s for remoteURI %@ fromURI %@, as our messageGUID is nil."
+ "_fallbackMessageItemForRequiredRegPropertiesTextMessage:"
+ "attachmentPolicy"
+ "chatForChatIdentifier:style:updatingAccount:"
+ "createNetworkMonitorWithRemoteHost:delegate:allowsUltraConstrainedNetwork:"
+ "localizedStringWithValidatedFormat:validFormatSpecifiers:error:"
+ "msg guid %@ Required reg properties %@ interesting properties %@ newFeature %@ sendPropsCompatMsgAsText %@"
+ "sendAlternateLayoutAsText"
+ "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:sourceHandle:destinationHandle:error:"
+ "updateUltraConstrainedAttachments:"
- "%@: %@"
- "backwards-compat-enabled-custom-acknowledgements"
- "msg guid %@ Required reg properties %@ interesting properties %@ newFeature %@"
- "supports-polls"
- "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:handle:error:"

```
