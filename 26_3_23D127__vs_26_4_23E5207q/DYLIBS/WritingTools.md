## WritingTools

> `/System/Library/PrivateFrameworks/WritingTools.framework/WritingTools`

```diff

-96.4.0.2.0
-  __TEXT.__text: 0x200c
-  __TEXT.__auth_stubs: 0x360
+96.4.5.0.0
+  __TEXT.__text: 0x2260
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_methlist: 0x5bc
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x2cc
+  __TEXT.__cstring: 0x287
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__oslogstring: 0x55
-  __TEXT.__unwind_info: 0x118
-  __TEXT.__objc_classname: 0xbe
-  __TEXT.__objc_methname: 0xa7a
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__objc_classname: 0xed
+  __TEXT.__objc_methname: 0xa81
   __TEXT.__objc_methtype: 0x310
-  __TEXT.__objc_stubs: 0x560
+  __TEXT.__objc_stubs: 0x5a0
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x38

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2d8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0xb50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 45759725-BE34-3D48-A989-17A821982BCC
+  UUID: 393BC42F-00D7-3936-AEE4-1051D9F37B60
   Functions: 85
-  Symbols:   406
-  CStrings:  235
+  Symbols:   405
+  CStrings:  234
 
Symbols:
+ _objc_msgSend$isWritingToolsAllowed
+ _objc_msgSend$sharedConnection
+ _objc_release_x25
+ _objc_retain
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x4
Functions:
~ -[WTTextSuggestion initWithOriginalRange:replacement:suggestionCategory:suggestionDescription:] : 240 -> 232
~ -[WTTextSuggestion hash] : 80 -> 84
~ -[WTTextSuggestion isEqual:] : 200 -> 208
~ -[WTTextSuggestion encodeWithXPCDictionary:] : 96 -> 100
~ -[WTTextSuggestion initWithXPCDictionary:] : 116 -> 120
~ -[WTTextSuggestion encodeWithCoder:] : 320 -> 344
~ -[WTTextSuggestion initWithCoder:] : 328 -> 348
~ -[WTSession initWithType:textViewDelegate:] : 148 -> 152
~ -[WTSession isEqual:] : 164 -> 172
~ -[WTSession encodeWithGeneralCoder:] : 164 -> 172
~ -[WTSession initWithGeneralCoder:] : 180 -> 184
~ -[WTBSCompatibleAttributedString encodeWithCoder:] : 324 -> 336
~ ___50-[WTBSCompatibleAttributedString encodeWithCoder:]_block_invoke : 144 -> 148
~ -[WTBSCompatibleAttributedString initWithCoder:] : 356 -> 360
~ ___48-[WTBSCompatibleAttributedString initWithCoder:]_block_invoke : 100 -> 104
~ -[WTBSCompatibleAttributedString encodeWithXPCDictionary:] : 96 -> 100
~ -[WTBSCompatibleAttributedString initWithXPCDictionary:] : 116 -> 120
~ -[WTContext initWithAttributedText:range:] : 160 -> 164
~ -[WTContext setAttributedText:] : 12 -> 64
~ -[WTContext hash] : 96 -> 100
~ -[WTContext isEqual:] : 216 -> 224
~ -[WTContext copyWithZone:] : 148 -> 156
~ -[WTContext encodeWithCoder:] : 316 -> 340
~ -[WTContext initWithCoder:] : 312 -> 332
~ -[WTContext encodeWithXPCDictionary:] : 96 -> 100
~ -[WTContext initWithXPCDictionary:] : 116 -> 120
~ -[WTContext setSmartReplyConfig:] : 12 -> 64
~ -[WTSmartReplyConfiguration initWithInputContextHistory:] : 116 -> 108
~ -[WTSmartReplyConfiguration encodeWithCoder:] : 264 -> 288
~ -[WTSmartReplyConfiguration initWithCoder:] : 240 -> 252
~ -[WTSmartReplyConfiguration setBaseResponse:] : 12 -> 64
~ -[WTSmartReplyConfiguration setEntryPoint:] : 12 -> 64
~ sub_2969cd2dc -> sub_29e169484 : 360 -> 532

```
