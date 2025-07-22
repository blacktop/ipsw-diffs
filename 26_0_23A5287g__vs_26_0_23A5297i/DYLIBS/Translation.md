## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-343.3.0.0.0
-  __TEXT.__text: 0x49acc
+345.0.0.0.0
+  __TEXT.__text: 0x49d18
   __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x5208
+  __TEXT.__objc_methlist: 0x5210
   __TEXT.__const: 0x5dc
   __TEXT.__cstring: 0x2d9e
-  __TEXT.__oslogstring: 0x4616
-  __TEXT.__gcc_except_tab: 0xaf0
+  __TEXT.__oslogstring: 0x4686
+  __TEXT.__gcc_except_tab: 0xb10
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x249
   __TEXT.__swift5_capture: 0xc0

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0x1708
+  __TEXT.__unwind_info: 0x1718
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0xafe
-  __TEXT.__objc_methname: 0xacc6
+  __TEXT.__objc_methname: 0xad04
   __TEXT.__objc_methtype: 0x1c06
   __TEXT.__objc_stubs: 0x61e0
   __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x1b68
+  __DATA_CONST.__const: 0x1b98
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23a8
+  __DATA_CONST.__objc_selrefs: 0x23b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x710
   __AUTH_CONST.__const: 0xac8
-  __AUTH_CONST.__cfstring: 0x3160
+  __AUTH_CONST.__cfstring: 0x3180
   __AUTH_CONST.__objc_const: 0xa6d0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A38C21CD-1D35-3E23-9283-C0CDD0BCC566
-  Functions: 2361
-  Symbols:   7004
-  CStrings:  3370
+  UUID: 54F39A52-8812-3CD4-9639-9E89295AEEFE
+  Functions: 2360
+  Symbols:   7005
+  CStrings:  3374
 
Symbols:
+ -[_LTSELFLoggingInvocation cancelWithReason:localePair:qssSessionId:]
+ -[_LTSELFLoggingInvocation cancelWithReason:localePair:qssSessionId:].cold.1
+ -[_LTSELFLoggingInvocation endSuccessfullyWithQSSSessionId:localePair:]
+ -[_LTSELFLoggingInvocation endSuccessfullyWithQSSSessionId:localePair:].cold.1
+ -[_LTSELFLoggingInvocation endWithError:localePair:qssSessionId:]
+ -[_LTSELFLoggingInvocation endWithError:localePair:qssSessionId:].cold.1
+ -[_LTSELFLoggingInvocation startedWithClientIdentifier:]
+ ___72-[_LTLanguageStatus initWithTaskHint:useDedicatedMachPort:observations:]_block_invoke.1
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSArray"8lw48l8s32l8s40l8
+ _kLTDebugIncludeHiddenCallTranslationLocales
+ _kLTDefaultLanguageSize
+ _objc_msgSend$discreteProgressWithIdentifier:totalUnitCount:
- -[_LTLanguageStatus dealloc].cold.1
- -[_LTLanguageStatus initWithTaskHint:useDedicatedMachPort:observations:].cold.1
- -[_LTSELFLoggingInvocation cancelWithReason:qssSessionId:]
- -[_LTSELFLoggingInvocation cancelWithReason:qssSessionId:].cold.1
- -[_LTSELFLoggingInvocation endSuccessfullyWithQSSSessionId:]
- -[_LTSELFLoggingInvocation endSuccessfullyWithQSSSessionId:].cold.1
- -[_LTSELFLoggingInvocation endWithError:qssSessionId:]
- -[_LTSELFLoggingInvocation endWithError:qssSessionId:].cold.1
- ___72-[_LTLanguageStatus initWithTaskHint:useDedicatedMachPort:observations:]_block_invoke_3
- _objc_msgSend$discreteProgressWithIdentifier:offlineState:
CStrings:
+ "ALREADY_CANCELLED_REASON"
+ "IncludeHiddenCallTranslationLocales"
+ "LANGUAGES_NOT_INSTALLED_REASON"
+ "LTLanguageStatus %@ alloc task:%zd dedicated:%{BOOL}i"
+ "LTLanguageStatus %@ cancel"
+ "LTLanguageStatus %@ dealloc"
+ "LTLanguageStatus %@ receive multicast with %zd observations"
+ "cancelWithReason:localePair:qssSessionId:"
+ "endSuccessfullyWithQSSSessionId:localePair:"
+ "endWithError:localePair:qssSessionId:"
+ "startedWithClientIdentifier:"
- "LTLanguageStatus alloc %@"
- "LTLanguageStatus dealloc %@"
- "Languages aren't installed"
- "The session was already cancelled"
- "asset_services_uaf"
- "cancelWithReason:qssSessionId:"
- "endSuccessfullyWithQSSSessionId:"
- "endWithError:qssSessionId:"

```
