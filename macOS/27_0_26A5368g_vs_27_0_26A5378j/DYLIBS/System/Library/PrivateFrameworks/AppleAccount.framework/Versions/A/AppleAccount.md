## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount`

```diff

-  __TEXT.__text: 0x2364ac
-  __TEXT.__objc_methlist: 0xb154
-  __TEXT.__cstring: 0xf781
-  __TEXT.__const: 0x40be0
-  __TEXT.__gcc_except_tab: 0x1a18
-  __TEXT.__oslogstring: 0x109cd
+  __TEXT.__text: 0x2390fc
+  __TEXT.__objc_methlist: 0xb19c
+  __TEXT.__cstring: 0xf851
+  __TEXT.__const: 0x40bc0
+  __TEXT.__gcc_except_tab: 0x1aa8
+  __TEXT.__oslogstring: 0x10cad
   __TEXT.__dlopen_cstrs: 0x2d3
-  __TEXT.__swift5_typeref: 0x195d
-  __TEXT.__constg_swiftt: 0x1248
+  __TEXT.__swift5_typeref: 0x1957
+  __TEXT.__constg_swiftt: 0x1250
   __TEXT.__swift5_reflstr: 0x998
-  __TEXT.__swift5_fieldmd: 0xfec
+  __TEXT.__swift5_fieldmd: 0xff8
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x200
   __TEXT.__swift5_proto: 0x494

   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_acfuncs: 0x17c
-  __TEXT.__swift_as_entry: 0x150
-  __TEXT.__swift_as_ret: 0x14c
-  __TEXT.__swift_as_cont: 0x26c
-  __TEXT.__swift5_capture: 0x464
-  __TEXT.__unwind_info: 0x4798
-  __TEXT.__eh_frame: 0x3d78
+  __TEXT.__swift_as_entry: 0x154
+  __TEXT.__swift_as_ret: 0x158
+  __TEXT.__swift_as_cont: 0x284
+  __TEXT.__swift5_capture: 0x4a8
+  __TEXT.__unwind_info: 0x4830
+  __TEXT.__eh_frame: 0x3ef0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f40
-  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_selrefs: 0x4f70
+  __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x580
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0xee8
-  __AUTH_CONST.__const: 0xd4f0
-  __AUTH_CONST.__cfstring: 0xcda0
-  __AUTH_CONST.__objc_const: 0x251b8
+  __DATA_CONST.__got: 0xef0
+  __AUTH_CONST.__const: 0xd570
+  __AUTH_CONST.__cfstring: 0xce60
+  __AUTH_CONST.__objc_const: 0x25278
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xf60
-  __AUTH.__objc_data: 0xea0
-  __AUTH.__data: 0x5f0
+  __AUTH_CONST.__auth_got: 0xfa8
+  __AUTH.__objc_data: 0x12e0
+  __AUTH.__data: 0x460
   __DATA.__objc_ivar: 0xba4
-  __DATA.__data: 0x2ad8
-  __DATA.__bss: 0x94d0
-  __DATA.__common: 0xa50
-  __DATA_DIRTY.__objc_data: 0x4ab8
-  __DATA_DIRTY.__data: 0x348
-  __DATA_DIRTY.__bss: 0x208
-  __DATA_DIRTY.__common: 0x38
+  __DATA.__data: 0x29c8
+  __DATA.__bss: 0x89f0
+  __DATA.__common: 0xa40
+  __DATA_DIRTY.__objc_data: 0x4688
+  __DATA_DIRTY.__data: 0x5e0
+  __DATA_DIRTY.__bss: 0xcf0
+  __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6772
-  Symbols:   12351
-  CStrings:  4928
+  Functions: 6800
+  Symbols:   12392
+  CStrings:  4953
 
Sections:
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_acfuncs : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ +[NSError(AppleAccount) _aa_sanitizeError:depth:]
+ +[NSError(AppleAccount) _aa_unsanitizeError:depth:]
+ +[NSError(AppleAccount) aa_sanitizeError:]
+ +[NSError(AppleAccount) aa_unsanitizeError:]
+ -[NSError(AppleAccount) _aa_secureCodingErrorAtDepth:]
+ -[NSError(AppleAccount) aa_secureCodingError]
+ AASanitizeObjectForSecureCoding
+ _AADecodeCertChainKey
+ _AAReencodeCertChainKey
+ _AASanitizeObjectForSecureCoding
+ _NSClassFromString
+ _NSURLErrorFailingURLPeerTrustErrorKey
+ _SecTrustDeserialize
+ _SecTrustGetTypeID
+ _SecTrustSerialize
+ __AADecodeCertChainKey
+ __AAReencodeCertChainKey
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ __swift_closure_destructor.111Tm
+ __swift_closure_destructor.115Tm
+ _objc_msgSend$_aa_sanitizeError:depth:
+ _objc_msgSend$_aa_secureCodingErrorAtDepth:
+ _objc_msgSend$_aa_unsanitizeError:depth:
+ _objc_msgSend$aa_unsanitizeError:
+ _objc_msgSend$performSelector:
+ _objc_msgSend$respondsToSelector:
+ _serializeSecCertificates
+ _swift_dynamicCastMetatype
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
+ _symbolic yXlXpSgSSc
+ _unserializeSecCertificates
- __swift_closure_destructor.110Tm
- __swift_closure_destructor.114Tm
- __swift_implicitisolationactor_to_executor_cast
- _swift_runtimeSupportsNoncopyableTypes
- get_type_metadata 15Synchronization5MutexVy12AppleAccount20IdentityLoadingStateOG noncopyable
- get_type_metadata 15Synchronization5MutexVySDy12AppleAccount7AltDSIDCAD08IdentityD0V7account_yAD0G0Cc8callback10Foundation4UUIDVSg05knownG2ID14XPCDistributed9XPCSystemC7SessionC15RemoteInterfaceVSg06remoteR0AD0G13ObserverTokenVSg5tokentGG noncopyable
- get_type_metadata 15Synchronization5MutexVySbG noncopyable
- get_type_metadata 15Synchronization5MutexVyScTyyts5Error_pGSgG noncopyable
CStrings:
+ "+aa_sanitizeError: max depth reached, returning userInfo-stripped fallback at depth %lu."
+ "AASanitizeObjectForSecureCoding: max depth exceeded, discarding object of class %@."
+ "IdentityStore initialized while app was backgrounded; deferring observer registration"
+ "NSErrorClientCertificateChainKey"
+ "NSErrorPeerCertificateChainKey"
+ "NSURLErrorFailingURLPeerTrustErrorKey"
+ "Removing object of class %@ from userInfo because it does not conform to NSSecureCoding."
+ "SecTrustSerialize failed: %@"
+ "UIApplication not available in this process"
+ "Unable to read +[UIApplication sharedApplication]"
+ "Unable to read -[UIApplication applicationState]"
+ "_AADecodeCertChainKey: exception deserializing companion key %@: %@"
+ "_AAReencodeCertChainKey: exception serializing cert chain for key %@: %@"
+ "_AA_SANITIZED"
+ "applicationState"
+ "c"
+ "com.apple.siri"
+ "sharedApplication"
+ "startObserving attempt %ld failed: %@. Retrying."
+ "startObserving failed after %ld attempts: %@"
- "Registration deferred: failed to start observing identity changes: %@"

```
