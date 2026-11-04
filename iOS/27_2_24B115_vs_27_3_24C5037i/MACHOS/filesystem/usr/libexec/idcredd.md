## idcredd

> `/usr/libexec/idcredd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methname`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`

```diff

-9.108.0.0.0
-  __TEXT.__text: 0x1b927c
-  __TEXT.__auth_stubs: 0x4370
-  __TEXT.__objc_stubs: 0x22a0
+9.204.0.0.0
+  __TEXT.__text: 0x1be69c
+  __TEXT.__auth_stubs: 0x4430
+  __TEXT.__objc_stubs: 0x22c0
   __TEXT.__objc_methlist: 0x944
-  __TEXT.__const: 0x6044
+  __TEXT.__const: 0x6074
   __TEXT.__objc_classname: 0x804
   __TEXT.__objc_methname: 0x3185
   __TEXT.__objc_methtype: 0x1093
-  __TEXT.__constg_swiftt: 0x2480
-  __TEXT.__swift5_typeref: 0x2a35
-  __TEXT.__swift5_reflstr: 0x1976
-  __TEXT.__swift5_fieldmd: 0x19c0
+  __TEXT.__constg_swiftt: 0x2488
+  __TEXT.__swift5_typeref: 0x2a6b
+  __TEXT.__swift5_reflstr: 0x1986
+  __TEXT.__swift5_fieldmd: 0x19cc
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__cstring: 0xe6fa
-  __TEXT.__oslogstring: 0xa939
+  __TEXT.__cstring: 0xe8fa
+  __TEXT.__oslogstring: 0xaac9
   __TEXT.__swift5_proto: 0x1a8
   __TEXT.__swift5_types: 0x218
   __TEXT.__swift_as_entry: 0x650
-  __TEXT.__swift_as_ret: 0x7bc
-  __TEXT.__swift_as_cont: 0xee4
+  __TEXT.__swift_as_ret: 0x7c0
+  __TEXT.__swift_as_cont: 0xee8
   __TEXT.__swift5_capture: 0x2ae0
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x6448
-  __TEXT.__eh_frame: 0x14c50
+  __TEXT.__unwind_info: 0x64b0
+  __TEXT.__eh_frame: 0x14ea8
   __DATA_CONST.__const: 0x6d80
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__linkguard: 0xe
-  __DATA_CONST.__auth_got: 0x21c0
-  __DATA_CONST.__got: 0x1860
-  __DATA_CONST.__auth_ptr: 0xa98
+  __DATA_CONST.__auth_got: 0x2220
+  __DATA_CONST.__got: 0x1870
+  __DATA_CONST.__auth_ptr: 0xaa0
   __DATA.__objc_const: 0x28b8
-  __DATA.__objc_selrefs: 0xb98
-  __DATA.__objc_data: 0xcb0
-  __DATA.__data: 0x45a8
+  __DATA.__objc_selrefs: 0xba0
+  __DATA.__objc_data: 0xcb8
+  __DATA.__data: 0x45e0
   __DATA.__common: 0x100
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4364
-  Symbols:   2021
-  CStrings:  2223
+  Functions: 4385
+  Symbols:   2036
+  CStrings:  2238
 
Symbols:
+ _$s10Foundation3URLV4hostSSSgvg
+ _$s13CoreIDVShared17decodeCertificate13fromBase64DERSo03SecD3RefaSS_tKF
+ _$s13CoreIDVShared8DIPErrorV4CodeO34idcsCallerNotAllowedForPrearmTrustyA2EmFWC
+ _$s20CoreIDVDaemonSupport17DIPAccountManagerCAA0dE8ProtocolAAWP
+ _$s20CoreIDVDaemonSupport17DIPAccountManagerCACycfC
+ _$s20CoreIDVDaemonSupport17DIPAccountManagerCMa
+ _$s20CoreIDVDaemonSupport25DIPAccountManagerProtocolMp
+ _$s20CoreIDVDaemonSupport25DIPAccountManagerProtocolP16isSandboxAccountySbSo9ACAccountCFTj
+ _$s20CoreIDVDaemonSupport25DIPAccountManagerProtocolP19primaryAppleAccountSo9ACAccountCSgyFTj
+ _$sSS10lowercasedSSyF
+ _$sSo17SecCertificateRefa13CoreIDVSharedE26dnsSubjectAlternativeNamesSaySSGvg
+ _$sSy10FoundationE22caseInsensitiveCompareySo18NSComparisonResultVqd__SyRd__lF
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ _SecTaskGetCodeSignStatus
CStrings:
+ ") is not allowed to use prearm trust APIs"
+ "Ignoring web presentment root cert injected through user defaults because it is not limited to an origin"
+ "Ignoring web presentment root cert injected through user defaults because the primary Apple account is not a sandbox account"
+ "Reader certificate is not valid for relying party identifier "
+ "Unable to create SecTask for caller "
+ "Unable to verify caller because connection is unavailable"
+ "Web presentment root cert injected through user defaults for %s"
+ "Web presentment root cert injected through user defaults is limited to %s, not %s"
+ "auditToken"
+ "checkCallerIsCoreIDVD()"
+ "com.apple.coreidv.coreidvd"
+ "injectedWebPresentmentRoot(relyingPartyIdentifier:userDefaultsConfiguration:accountManager:)"
+ "ra.web-presentment.injected-root"
+ "ra.web-presentment.injected-root-origin"
+ "verifyHostName(_:readerCerts:)"
```
