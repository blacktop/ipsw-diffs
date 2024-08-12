## SiriMailInternal

> `/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal`

```diff

-3400.104.1.0.0
-  __TEXT.__text: 0xe2c60
+3401.8.1.0.0
+  __TEXT.__text: 0xe06dc
   __TEXT.__auth_stubs: 0x3f00
-  __TEXT.__const: 0x5e50
-  __TEXT.__cstring: 0x2324
-  __TEXT.__constg_swiftt: 0x2158
-  __TEXT.__swift5_typeref: 0x356a
-  __TEXT.__swift5_fieldmd: 0x19e0
-  __TEXT.__oslogstring: 0x6287
+  __TEXT.__const: 0x5f60
+  __TEXT.__cstring: 0x2384
+  __TEXT.__constg_swiftt: 0x2180
+  __TEXT.__swift5_typeref: 0x35ae
+  __TEXT.__swift5_fieldmd: 0x19ec
+  __TEXT.__oslogstring: 0x6267
   __TEXT.__swift5_types: 0x194
   __TEXT.__swift5_proto: 0x288
-  __TEXT.__swift5_reflstr: 0x18f3
+  __TEXT.__swift5_reflstr: 0x1923
   __TEXT.__swift5_assocty: 0x460
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift5_capture: 0x5a0
-  __TEXT.__unwind_info: 0x2c50
+  __TEXT.__unwind_info: 0x2c90
   __TEXT.__eh_frame: 0x5f60
   __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0x970
+  __TEXT.__objc_methname: 0x9fa
   __TEXT.__objc_methtype: 0x1d1
-  __DATA_CONST.__got: 0x10d8
-  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__got: 0x1100
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c0
+  __DATA_CONST.__objc_selrefs: 0x2d8
   __DATA_CONST.__objc_protorefs: 0x60
   __AUTH_CONST.__auth_got: 0x1f80
-  __AUTH_CONST.__auth_ptr: 0x1730
-  __AUTH_CONST.__const: 0x2380
-  __AUTH_CONST.__objc_const: 0x25f0
+  __AUTH_CONST.__auth_ptr: 0x1748
+  __AUTH_CONST.__const: 0x2388
+  __AUTH_CONST.__objc_const: 0x2618
   __AUTH.__objc_data: 0x750
-  __AUTH.__data: 0x2e60
-  __DATA.__data: 0x2670
-  __DATA.__bss: 0x51a0
-  __DATA.__common: 0x228
+  __AUTH.__data: 0x2e88
+  __DATA.__data: 0x2680
+  __DATA.__bss: 0x51d0
+  __DATA.__common: 0x220
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4229
-  Symbols:   2290
-  CStrings:  812
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4242
+  Symbols:   2246
+  CStrings:  813
 
Symbols:
+ _OBJC_CLASS_$_EFPrivacy
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "#ReadingInputInterpreter got an off topic read parse, returning .no"
+ "#ReadingUtil got EMMessage, about to request EMMessage representation"
+ "#ReadingUtil was able to continue with EMContentRepresentation"
+ "#ReadingUtil.fetchMailBody: EMMessage is not available, cannot request content, returning nil"
+ "#ReplyMessageFlow resolved sender %!{(MISSING)private}s"
+ "#ResolveRecipientsFlow .sanitizeContactHandles %!{(MISSING)private}s"
+ "#ResolveRecipientsFlow .sanitizeContactHandles sanitizedHandles %!{(MISSING)private}s"
+ "#ResolveSender resolving as %!{(MISSING)private}s"
+ "#WidgetMessage producing WidgetMessage for UI plugin with redacted subject: %!s(MISSING)"
+ "$__lazy_storage_$_daemonInterface"
+ "ec_partiallyRedactedStringForSubjectOrSummary:"
+ "isHeadGestureRecognitionAvailable"
+ "partiallyRedactedStringForString:"
+ "redactedQueryStringForQueryString:"
+ "setSpokenOnlyDefined:"
- "#ReadSingleMessage message %!s(MISSING)"
- "#ReadSingleMessage message concept %!s(MISSING)"
- "#ReadSubjectLine message %!s(MISSING)"
- "#ReadSubjectLine message concept %!s(MISSING)"
- "#ReadingInputInterpreter read"
- "#ReadingUtil about to request EMMessage representation"
- "#ReadingUtil got EMMessage: %!s(MISSING)"
- "#ReadingUtil searchableItemIdentifier: %!s(MISSING)"
- "#ReadingUtil was able to continue with EMContentRepresentation: %!s(MISSING)"
- "#ReplyMessageFlow resolved sender %!s(MISSING)"
- "#ResolveRecipientsFlow .sanitizeContactHandles %!s(MISSING)"
- "#ResolveRecipientsFlow .sanitizeContactHandles sanitizedHandles %!s(MISSING)"
- "#ResolveSender resolving as %!s(MISSING)"
- "#WidgetMessage %!s(MISSING)"

```
