## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-  __TEXT.__text: 0x1a534c
+  __TEXT.__text: 0x1a7d24
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xb56c
-  __TEXT.__cstring: 0x11392
-  __TEXT.__const: 0x10d70
-  __TEXT.__gcc_except_tab: 0x1b68
-  __TEXT.__oslogstring: 0x1351d
+  __TEXT.__objc_methlist: 0xb5b4
+  __TEXT.__cstring: 0x11452
+  __TEXT.__const: 0x10d30
+  __TEXT.__gcc_except_tab: 0x1bf8
+  __TEXT.__oslogstring: 0x137fd
   __TEXT.__dlopen_cstrs: 0x325
-  __TEXT.__swift5_typeref: 0x3a6c
-  __TEXT.__constg_swiftt: 0x2a60
+  __TEXT.__swift5_typeref: 0x3a66
+  __TEXT.__constg_swiftt: 0x2a68
   __TEXT.__swift5_reflstr: 0x15ea
-  __TEXT.__swift5_fieldmd: 0x2624
+  __TEXT.__swift5_fieldmd: 0x2630
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_assocty: 0x3c0
   __TEXT.__swift5_proto: 0xc70

   __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_acfuncs: 0x1a4
-  __TEXT.__swift_as_entry: 0x254
-  __TEXT.__swift_as_ret: 0x290
-  __TEXT.__swift_as_cont: 0x4fc
-  __TEXT.__swift5_capture: 0x804
-  __TEXT.__unwind_info: 0x6470
-  __TEXT.__eh_frame: 0x7640
+  __TEXT.__swift_as_entry: 0x258
+  __TEXT.__swift_as_ret: 0x29c
+  __TEXT.__swift_as_cont: 0x510
+  __TEXT.__swift5_capture: 0x848
+  __TEXT.__unwind_info: 0x64e8
+  __TEXT.__eh_frame: 0x7768
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5240
-  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x5270
+  __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x1148
-  __AUTH_CONST.__const: 0xd2c0
-  __AUTH_CONST.__cfstring: 0xd520
-  __AUTH_CONST.__objc_const: 0x269e0
+  __DATA_CONST.__got: 0x1150
+  __AUTH_CONST.__const: 0xd330
+  __AUTH_CONST.__cfstring: 0xd5e0
+  __AUTH_CONST.__objc_const: 0x26aa0
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x14f8
-  __AUTH.__objc_data: 0x1228
-  __AUTH.__data: 0x1088
+  __AUTH_CONST.__auth_got: 0x1538
+  __AUTH.__objc_data: 0x1128
+  __AUTH.__data: 0xc38
   __DATA.__objc_ivar: 0xbd4
-  __DATA.__data: 0x445c
-  __DATA.__bss: 0x18f30
-  __DATA.__common: 0xc8
-  __DATA_DIRTY.__objc_data: 0x4a68
-  __DATA_DIRTY.__data: 0x2d8
-  __DATA_DIRTY.__bss: 0x130
-  __DATA_DIRTY.__common: 0x28
+  __DATA.__data: 0x40f4
+  __DATA.__bss: 0x17640
+  __DATA.__common: 0xa8
+  __DATA_DIRTY.__objc_data: 0x4b78
+  __DATA_DIRTY.__data: 0xad8
+  __DATA_DIRTY.__bss: 0x1a28
+  __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9114
-  Symbols:   18765
-  CStrings:  5423
+  Functions: 9142
+  Symbols:   18827
+  CStrings:  5448
 
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
~ __AUTH_CONST.__lazy_load_got : content changed
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
+ _AASanitizeObjectForSecureCoding
+ _NSClassFromString
+ _NSURLErrorFailingURLPeerTrustErrorKey
+ _SecTrustDeserialize
+ _SecTrustGetTypeID
+ _SecTrustSerialize
+ __AADecodeCertChainKey
+ __AAReencodeCertChainKey
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ ___swift_closure_destructor.110Tm
+ ___swift_closure_destructor.114Tm
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
- ___swift_closure_destructor.109Tm
- ___swift_closure_destructor.113Tm
- _get_type_metadata 15Synchronization5MutexVy12AppleAccount20IdentityLoadingStateOG noncopyable
- _get_type_metadata 15Synchronization5MutexVySDy12AppleAccount7AltDSIDCAD08IdentityD0V7account_yAD0G0Cc8callback10Foundation4UUIDVSg05knownG2ID14XPCDistributed9XPCSystemC7SessionC15RemoteInterfaceVSg06remoteR0AD0G13ObserverTokenVSg5tokentGG noncopyable
- _get_type_metadata 15Synchronization5MutexVySbG noncopyable
- _get_type_metadata 15Synchronization5MutexVyScTyyts5Error_pGSgG noncopyable
- _swift_release_x28
- _swift_runtimeSupportsNoncopyableTypes
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
