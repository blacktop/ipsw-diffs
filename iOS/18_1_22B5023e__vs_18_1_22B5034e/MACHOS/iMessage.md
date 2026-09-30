## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1402.200.8.0.0
-  __TEXT.__text: 0x90930
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_stubs: 0xb180
-  __TEXT.__objc_methlist: 0x2144
-  __TEXT.__const: 0x36e
-  __TEXT.__gcc_except_tab: 0xa678
-  __TEXT.__cstring: 0x2efd
-  __TEXT.__oslogstring: 0x13d26
+1402.200.35.0.0
+  __TEXT.__text: 0x91160
+  __TEXT.__auth_stubs: 0x1380
+  __TEXT.__objc_stubs: 0xb1e0
+  __TEXT.__objc_methlist: 0x2164
+  __TEXT.__const: 0x37e
+  __TEXT.__gcc_except_tab: 0xa698
+  __TEXT.__cstring: 0x2fdd
+  __TEXT.__oslogstring: 0x13d76
   __TEXT.__objc_classname: 0x4e2
-  __TEXT.__objc_methname: 0x102df
+  __TEXT.__objc_methname: 0x10343
   __TEXT.__objc_methtype: 0x27ad
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x150
+  __TEXT.__constg_swiftt: 0x158
   __TEXT.__swift5_typeref: 0x251
   __TEXT.__swift5_reflstr: 0x1f
   __TEXT.__swift5_fieldmd: 0x48

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d88
+  __TEXT.__unwind_info: 0x1d98
   __TEXT.__eh_frame: 0x2b8
-  __DATA_CONST.__auth_got: 0x9b8
-  __DATA_CONST.__got: 0xd88
+  __DATA_CONST.__auth_got: 0x9d0
+  __DATA_CONST.__got: 0xda8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x2ae0
-  __DATA_CONST.__cfstring: 0x31e0
+  __DATA_CONST.__cfstring: 0x3220
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x3560
-  __DATA.__objc_selrefs: 0x31a0
+  __DATA.__objc_selrefs: 0x31c0
   __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x378
-  __DATA.__data: 0x770
+  __DATA.__data: 0x788
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1165
-  Symbols:   771
-  CStrings:  4150
+  Functions: 1173
+  Symbols:   778
+  CStrings:  4157
 
Symbols:
+ _swift_initStackObject
+ _IMSharedHelperMissingKeysInStickerUserInfo
+ _swift_setDeallocating
+ _NSDebugDescriptionErrorKey
+ _IMChatErrorDomain
+ _IMServiceCapabilityGroupIdentity
+ _IMSMSDefaultsDomain
CStrings:
+ "[MessageDeliveryController] Attempting sticker repositioning with nil reposition metadata."
+ "[MessageDeliveryController] Attempting sticker repositioning with missing reposition metadata."
+ "AttemptedInvalidStickerReposition"
+ "Requsting delivery status for message GUID %!@(MISSING) due to delivery context %!@(MISSING) isGroupChat %!{(MISSING)bool}d"
+ "NilStickerMetadata"
+ "_checkStickerRepositioningMetadata:"
+ "Requsting delivery status for message GUID %!@(MISSING) because !isGroupChat"
+ "supportsCapability:"
+ "_convergesDisplayNames"
+ "MissingStickerMetadata"
+ "serviceOfLastMessage"
- "iMessage;-;%!@(MISSING)"
- "Sticker repositioning is supported and necessary keys were added to messageDictionary."
- "com.apple.sms"
- "iMessage;+;%!@(MISSING)"

```
