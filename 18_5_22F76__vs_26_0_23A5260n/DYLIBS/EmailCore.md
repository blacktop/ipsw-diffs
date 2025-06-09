## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`

```diff

-3826.600.51.2.1
-  __TEXT.__text: 0x5308c
-  __TEXT.__auth_stubs: 0x1050
-  __TEXT.__objc_methlist: 0x4db0
-  __TEXT.__const: 0xe50
-  __TEXT.__gcc_except_tab: 0x6ccc
-  __TEXT.__cstring: 0x7ba4
+3853.100.6.2.6
+  __TEXT.__text: 0x53978
+  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__objc_methlist: 0x4e38
+  __TEXT.__const: 0xe70
+  __TEXT.__gcc_except_tab: 0x6dc0
+  __TEXT.__cstring: 0x7c54
   __TEXT.__oslogstring: 0xcd8
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x2718
-  __TEXT.__objc_classname: 0xcbd
-  __TEXT.__objc_methname: 0xaa1c
-  __TEXT.__objc_methtype: 0x16a3
-  __TEXT.__objc_stubs: 0x73a0
+  __TEXT.__unwind_info: 0x2768
+  __TEXT.__objc_classname: 0xcc0
+  __TEXT.__objc_methname: 0xabcb
+  __TEXT.__objc_methtype: 0x16b7
+  __TEXT.__objc_stubs: 0x7460
   __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x21c0
+  __DATA_CONST.__const: 0x2200
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28b0
+  __DATA_CONST.__objc_selrefs: 0x28f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x278
-  __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x838
+  __DATA_CONST.__objc_arraydata: 0x80
+  __AUTH_CONST.__auth_got: 0x830
   __AUTH_CONST.__const: 0x6f8
-  __AUTH_CONST.__cfstring: 0x50c0
-  __AUTH_CONST.__objc_const: 0x9af0
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__cfstring: 0x51e0
+  __AUTH_CONST.__objc_const: 0x9bb8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH.__objc_data: 0xe8
-  __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x490
+  __AUTH.__objc_data: 0x1b0
+  __AUTH.__data: 0x88
+  __DATA.__objc_ivar: 0x49c
   __DATA.__data: 0xd44
-  __DATA.__bss: 0x3a0
+  __DATA.__bss: 0x380
   __DATA.__common: 0x24
-  __DATA_DIRTY.__objc_data: 0x1e78
-  __DATA_DIRTY.__data: 0xb80
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__objc_data: 0x1db0
+  __DATA_DIRTY.__data: 0xb50
+  __DATA_DIRTY.__bss: 0x208
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 09941E52-40BD-34FF-833B-9A6E246C652F
-  Functions: 1885
-  Symbols:   7477
-  CStrings:  4389
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 303D6BEA-928F-34E8-BCB6-37D78ACCF93F
+  Functions: 1895
+  Symbols:   7504
+  CStrings:  4421
 
Symbols:
+ +[ECMessageFlagChange setTouchedByCleanup]
+ +[EFPrivacy(EmailCore) ec_redactedQueryStringForSearchableQueryString:]
+ -[ECMessageFlagChange changesTouchedByCleanupTo:]
+ -[ECMessageFlagChange setTouchedByCleanup:]
+ -[ECMessageFlagChange setTouchedByCleanupChanged:]
+ -[ECMessageFlagChange touchedByCleanupChanged]
+ -[ECMessageFlagChange touchedByCleanup]
+ -[ECMessageFlags setTouchedByCleanup:]
+ -[ECMessageFlags touchedByCleanup]
+ -[ECSignatureInfo _protectedEncryptionKeyPreferenceAttributeWithAdditionalCertificates:]
+ -[ECSignatureInfo initWithSignerInfo:certificates:]
+ _CFAllocatorAllocateTyped
+ _ECMessageHeaderKeyHMEReplyAddress
+ _OBJC_IVAR_$_ECMessageFlagChange._touchedByCleanup
+ _OBJC_IVAR_$_ECMessageFlagChange._touchedByCleanupChanged
+ _OBJC_IVAR_$_ECSignatureInfo._certificates
+ ___71+[EFPrivacy(EmailCore) ec_redactedQueryStringForSearchableQueryString:]_block_invoke
+ ___88-[ECSignatureInfo _protectedEncryptionKeyPreferenceAttributeWithAdditionalCertificates:]_block_invoke
+ ___block_descriptor_32_e31_B16?0"<MSCMSAttributeCoder>"8l
+ ___block_descriptor_40_ea8_32s_e42_"ECSignatureInfo"16?0"MSCMSSignerInfo"8ls32l8
+ ___block_descriptor_48_ea8_32s40s_e37_v32?0"NSTextCheckingResult"8Q16^B24ls32l8s40l8
+ ___block_descriptor_57_e33_v16?0"<ECMessageFlagsBuilder>"8l
+ ___block_literal_global.58
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_EmailCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_EmailCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_EmailCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_EmailCore
+ _objc_msgSend$certificates
+ _objc_msgSend$changesTouchedByCleanupTo:
+ _objc_msgSend$enumerateMatchesInString:options:range:usingBlock:
+ _objc_msgSend$initWithAttribute:certificates:LAContext:error:
+ _objc_msgSend$initWithSignerInfo:certificates:
+ _objc_msgSend$setTouchedByCleanup:
+ _objc_msgSend$setTouchedByCleanupChanged:
+ _objc_msgSend$touchedByCleanup
+ _objc_msgSend$touchedByCleanupChanged
- -[ECSASLClient useATOKEN2Authentication]
- -[ECSignatureInfo initWithSignerInfo:]
- _CFAllocatorAllocate
- ___block_descriptor_32_e42_"ECSignatureInfo"16?0"MSCMSSignerInfo"8l
- ___block_descriptor_56_e33_v16?0"<ECMessageFlagsBuilder>"8l
- ___block_literal_global.55
- __os_feature_enabled_impl
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_EmailCore
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_EmailCore
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_EmailCore
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_EmailCore
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_EmailCore
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_EmailCore
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_EmailCore
- _objc_msgSend$initWithSignerInfo:
- _objc_msgSend$isVirtualMachine
- _objc_msgSend$useATOKEN2Authentication
- _sasl_gss_new_context
CStrings:
+ "%@ = '%@'"
+ "%@|"
+ "(ECMessageFlagsHashedBitField=\"hashValue\"Q\"bitField\"{?=\"read\"b1\"deleted\"b1\"replied\"b1\"flagged\"b1\"draft\"b1\"forwarded\"b1\"redirected\"b1\"junkLevelSetByUser\"b1\"junkLevel\"b2\"flagColor\"b3\"touchedByCleanup\"b1})"
+ ") = '([^']+)'\\)"
+ "T@\"ECMessageFlagChange\",R,C,N,GsetTouchedByCleanup"
+ "TB,N,V_touchedByCleanup"
+ "TB,N,V_touchedByCleanupChanged"
+ "TouchedByCleanup"
+ "\\(("
+ "_certificates"
+ "_touchedByCleanup"
+ "_touchedByCleanupChanged"
+ "certificates"
+ "changesTouchedByCleanupTo:"
+ "ec_redactedQueryStringForSearchableQueryString:"
+ "enumerateMatchesInString:options:range:usingBlock:"
+ "initWithAttribute:certificates:LAContext:error:"
+ "initWithSignerInfo:certificates:"
+ "kMDItemAuthorEmailAddresses"
+ "kMDItemAuthors"
+ "setTouchedByCleanup"
+ "setTouchedByCleanup:"
+ "setTouchedByCleanupChanged:"
+ "touchedByCleanup"
+ "touchedByCleanup: %ld"
+ "touchedByCleanupChanged"
+ "v32@?0@\"NSTextCheckingResult\"8Q16^B24"
+ "x-apple-hme-reply-address"
- "(ECMessageFlagsHashedBitField=\"hashValue\"Q\"bitField\"{?=\"read\"b1\"deleted\"b1\"replied\"b1\"flagged\"b1\"draft\"b1\"forwarded\"b1\"redirected\"b1\"junkLevelSetByUser\"b1\"junkLevel\"b2\"flagColor\"b3})"
- "Mail"
- "initWithSignerInfo:"
- "isVirtualMachine"
- "useATOKEN2Authentication"

```
