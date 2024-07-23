## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1299.100.9.2.2
-  __TEXT.__text: 0x8f36c
-  __TEXT.__auth_stubs: 0x1300
-  __TEXT.__objc_stubs: 0xae80
-  __TEXT.__objc_methlist: 0x2104
-  __TEXT.__const: 0x36e
-  __TEXT.__gcc_except_tab: 0xa520
-  __TEXT.__cstring: 0x2e5d
-  __TEXT.__oslogstring: 0x13866
+1301.100.8.2.5
+  __TEXT.__text: 0x8fdc0
+  __TEXT.__auth_stubs: 0x1320
+  __TEXT.__objc_stubs: 0xaf40
+  __TEXT.__objc_methlist: 0x210c
+  __TEXT.__const: 0x37e
+  __TEXT.__gcc_except_tab: 0xa5a4
+  __TEXT.__cstring: 0x2e8d
+  __TEXT.__oslogstring: 0x13ad6
   __TEXT.__objc_classname: 0x4e5
-  __TEXT.__objc_methname: 0xfdf5
-  __TEXT.__objc_methtype: 0x275f
+  __TEXT.__objc_methname: 0xff1a
+  __TEXT.__objc_methtype: 0x2776
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x140
+  __TEXT.__constg_swiftt: 0x150
   __TEXT.__swift5_typeref: 0x253
   __TEXT.__swift5_reflstr: 0x1f
   __TEXT.__swift5_fieldmd: 0x48

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d48
+  __TEXT.__unwind_info: 0x1d60
   __TEXT.__eh_frame: 0x2b8
-  __DATA_CONST.__auth_got: 0x990
+  __DATA_CONST.__auth_got: 0x9a0
   __DATA_CONST.__got: 0xd70
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2988
+  __DATA_CONST.__const: 0x29b0
   __DATA_CONST.__cfstring: 0x31a0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x3560
-  __DATA.__objc_selrefs: 0x30d8
+  __DATA.__objc_selrefs: 0x3108
   __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x378
-  __DATA.__data: 0x760
+  __DATA.__data: 0x770
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0xc

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1153
-  Symbols:   756
-  CStrings:  4102
+  Functions: 1160
+  Symbols:   757
+  CStrings:  4117
 
Symbols:
+ __Block_object_assign
CStrings:
+ "%!{(MISSING)public}s alias %!s(MISSING) SIMID %!s(MISSING) not registered but active in CT. deferring to other services"
+ "Copying genmoji to temporary path failed, because file is already there."
+ "Copying genmoji to temporary path, but file already exists at that path, and the deletion of that item failed with error: %!@(MISSING)"
+ "Copying genmoji to temporary path, but file already exists at that path, deleting old item."
+ "Could not determine file name when copying genmoji to temporary file path"
+ "Error occurred copying genmoji to temporary path: %!@(MISSING)"
+ "Message from %!@(MISSING) did not contain offGridSubscriptionValidationToken."
+ "Received offGridSubscriptionValidationToken = \"%!@(MISSING)\" from %!@(MISSING) to %!@(MISSING)"
+ "We decided not to upload the group photo. This should not happen unless the file is too large."
+ "__im_isOnlyAdaptiveImageGlyphFileTransfersAndWhitespaceUsingFileTransferProvider:"
+ "__im_transferGUIDsInAttributedString"
+ "__im_visitMessageParts:"
+ "_copyGenmojiHEICFileToTemporaryDirectory:"
+ "_fallbackMesssageItemByConvertingGenmojiToUnknownEmojiCharacterInOriginalMessageItem:"
+ "logMessageReceivedWithGUID:fromIdentifier:toIdentifier:conversationType:messageType:messageProtocol:"
+ "logMessageSentWithGUID:fromIdentifier:toIdentifier:conversationType:messageType:sendDuration:errorCode:messageProtocol:"
+ "removeObjectsInArray:"
+ "sendReadReceiptForMessage:toChatID:identifier:style:reflectOnly:"
+ "setIsGenmojiFallback:"
+ "v32@?0@\"IMMessagePartDescriptor\"8Q16^B24"
+ "v48@0:8@16@24@32C40B44"
- "Could not determine file name when copying to temporary file path"
- "Error occurred copying files to temporary path: %!@(MISSING)"
- "_copyFileToTemporaryDirectory:"
- "_fallbackMesssageItemByConvertingAdaptiveImageGlyphsToDescriptionInOriginalMessageItem:"
- "logMessageReceivedWithGUID:fromIdentifier:toIdentifier:conversationType:messageType:"
- "logMessageSentWithGUID:fromIdentifier:toIdentifier:conversationType:messageType:sendDuration:errorCode:"

```
