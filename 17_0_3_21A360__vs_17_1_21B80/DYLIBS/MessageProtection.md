## MessageProtection

> `/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection`

```diff

-317.0.0.0.0
-  __TEXT.__text: 0x3a164
-  __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x1bd4
-  __TEXT.__cstring: 0x2631
-  __TEXT.__oslogstring: 0x15a8
+325.0.0.0.0
+  __TEXT.__text: 0x3a620
+  __TEXT.__auth_stubs: 0x16f0
+  __TEXT.__objc_methlist: 0x1bfc
+  __TEXT.__cstring: 0x2781
+  __TEXT.__oslogstring: 0x168e
   __TEXT.__const: 0xf66
-  __TEXT.__gcc_except_tab: 0x21c
+  __TEXT.__gcc_except_tab: 0x224
   __TEXT.__ustring: 0x21c
   __TEXT.__constg_swiftt: 0x4f0
-  __TEXT.__swift5_typeref: 0x3c7
+  __TEXT.__swift5_typeref: 0x3cf
   __TEXT.__swift5_proto: 0xb0
   __TEXT.__swift5_types: 0x5c
-  __TEXT.__swift5_reflstr: 0x4ce
-  __TEXT.__swift5_fieldmd: 0x408
+  __TEXT.__swift5_reflstr: 0x4ee
+  __TEXT.__swift5_fieldmd: 0x414
   __TEXT.__swift5_capture: 0x40
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1dd0
+  __TEXT.__unwind_info: 0x1df0
   __TEXT.__eh_frame: 0xef8
   __TEXT.__objc_classname: 0x510
-  __TEXT.__objc_methname: 0x31dc
+  __TEXT.__objc_methname: 0x3228
   __TEXT.__objc_methtype: 0xaea
-  __TEXT.__objc_stubs: 0x2780
+  __TEXT.__objc_stubs: 0x2800
   __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3d78
-  __DATA_CONST.__objc_selrefs: 0xc60
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x1720
+  __DATA_CONST.__objc_const: 0x3d48
+  __DATA_CONST.__objc_selrefs: 0xc80
+  __AUTH_CONST.__objc_const: 0x48
+  __AUTH_CONST.__cfstring: 0x17a0
   __AUTH_CONST.__auth_ptr: 0x78
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__const: 0x418
-  __AUTH_CONST.__auth_got: 0xb80
+  __AUTH_CONST.__auth_got: 0xb88
   __AUTH.__objc_data: 0x0
-  __DATA.__objc_classrefs: 0x230
+  __DATA.__objc_classrefs: 0x238
   __DATA.__objc_superrefs: 0x110
   __DATA.__objc_ivar: 0x150
-  __DATA.__data: 0x418
+  __DATA.__data: 0x428
   __DATA.__bss: 0x1180
   __DATA.__common: 0xa0
   __DATA_DIRTY.__const: 0x4b8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1332
-  Symbols:   4421
-  CStrings:  1129
+  Functions: 1345
+  Symbols:   4456
+  CStrings:  1142
 
Symbols:
+ -[MPStatusKitIncomingRatchet maxForwardRatchetDelta]
+ -[NGMPublicDeviceIdentity sealMessage:guid:sendingURI:sendingPushToken:receivingURI:receivingPushToken:forceSizeOptimizations:resetState:encryptedAttributes:signedByFullIdentity:errors:].cold.1
+ _$s17MessageProtection16SymmetricRatchetV010maxForwardD5Deltas6UInt64Vvau
+ _$s17MessageProtection16SymmetricRatchetV010maxForwardD5Deltas6UInt64VvgZ
+ _$s17MessageProtection16SymmetricRatchetV010maxForwardD5Deltas6UInt64VvpZ
+ _$s17MessageProtection17SKIncomingRatchetC010maxForwardD5Deltas6UInt64VvgZTo
+ _$ss5Error_pMD
+ _MPEchnidaEncryptionDisabled
+ _MPSecondaryEncryptionDisabled
+ _MPSecondaryRegistrationDisabled
+ _MPSetEchnidaEncryptionDisabled
+ _MPSetSecondaryEncryptionDisabled
+ _MPSetSecondaryRegistrationDisabled
+ _OBJC_CLASS_$_NSUserDefaults
+ __CLASS_PROPERTIES__TtC17MessageProtection17SKIncomingRatchet
+ __OBJC_$_CLASS_METHODS__TtC17MessageProtection17SKIncomingRatchet
+ ___block_descriptor_72_e8_32s40r48r56r64r_e56_v40?0"NSData"8"NSDictionary"16"NSError"24?<B?^>32lr40l8s32l8r48l8r56l8r64l8
+ _get_value
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$maxForwardRatchetDelta
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$standardUserDefaults
+ _set_value
+ _swift_errorRetain
+ _symbolic ______p s5ErrorP
- ___block_descriptor_80_e8_32s40s48bs56r64r72r_e56_v40?0"NSData"8"NSDictionary"16"NSError"24?<B?^>32lr56l8r64l8r72l8s32l8s40l8s48l8
CStrings:
+ "Failed to seal message. Invalid configuration: both Echnida and Secondary encryption are disabled."
+ "Message with GUID: %@ hasEchnidaPayload=%d hasSecondaryPayload=%d"
+ "Sealing message with GUID: %@. echnidaDisabled=%d, secondaryDisabled=%d, secondaryRegistrationDisabled=%d"
+ "TQ,N,R"
+ "boolForKey:"
+ "com.apple.security.IDSEncryption.EchnidaEncryptionDisabled"
+ "com.apple.security.IDSEncryption.SecondaryEncryptionDisabled"
+ "com.apple.security.IDSEncryption.SecondaryRegistrationDisabled"
+ "maxForwardRatchetDelta"
+ "setBool:forKey:"
+ "standardUserDefaults"
- "Finished Echnida decryption for GUID: %@"

```
