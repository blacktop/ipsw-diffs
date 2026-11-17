## appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_types2`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-13.2.8.0.0
-  __TEXT.__text: 0x555a64
-  __TEXT.__auth_stubs: 0x4900
-  __TEXT.__objc_stubs: 0x14d00
-  __TEXT.__objc_methlist: 0xd6f4
+13.2.11.0.0
+  __TEXT.__text: 0x5572f0
+  __TEXT.__auth_stubs: 0x4930
+  __TEXT.__objc_stubs: 0x14d20
+  __TEXT.__objc_methlist: 0xd704
   __TEXT.__dlopen_cstrs: 0x45e
-  __TEXT.__const: 0x26b88
-  __TEXT.__swift5_typeref: 0x35f4
+  __TEXT.__const: 0x26bc8
+  __TEXT.__swift5_typeref: 0x3606
   __TEXT.__objc_classname: 0x5283
-  __TEXT.__objc_methname: 0x1e4bc
+  __TEXT.__objc_methname: 0x1e4cc
   __TEXT.__objc_methtype: 0x8e91
   __TEXT.__constg_swiftt: 0x2e94
   __TEXT.__swift5_reflstr: 0x22e0
   __TEXT.__swift5_fieldmd: 0x304c
   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_assocty: 0x498
-  __TEXT.__oslogstring: 0x3dccd
-  __TEXT.__cstring: 0x21573
+  __TEXT.__oslogstring: 0x3dfbb
+  __TEXT.__cstring: 0x216e0
   __TEXT.__swift5_proto: 0x458
   __TEXT.__swift5_types: 0x34c
   __TEXT.__swift5_protos: 0x24

   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x8d48
   __TEXT.__ustring: 0x94
-  __TEXT.__unwind_info: 0xe440
+  __TEXT.__unwind_info: 0xe468
   __TEXT.__eh_frame: 0xea80
-  __DATA_CONST.__const: 0x299c8
-  __DATA_CONST.__cfstring: 0x1ae60
+  __DATA_CONST.__const: 0x299d8
+  __DATA_CONST.__cfstring: 0x1af60
   __DATA_CONST.__objc_classlist: 0x15e0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x538

   __DATA_CONST.__objc_arraydata: 0x800
   __DATA_CONST.__objc_arrayobj: 0x420
   __DATA_CONST.__objc_dictobj: 0x168
-  __DATA_CONST.__auth_got: 0x2490
+  __DATA_CONST.__auth_got: 0x24a8
   __DATA_CONST.__got: 0x1e88
   __DATA_CONST.__auth_ptr: 0xb28
-  __DATA.__objc_const: 0x33f50
-  __DATA.__objc_selrefs: 0x6a70
-  __DATA.__objc_ivar: 0x2314
+  __DATA.__objc_const: 0x33f90
+  __DATA.__objc_selrefs: 0x6a78
+  __DATA.__objc_ivar: 0x231c
   __DATA.__objc_data: 0x108b0
-  __DATA.__data: 0x8650
+  __DATA.__data: 0x85b0
   __DATA.__common: 0xcfc
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13848
-  Symbols:   2282
-  CStrings:  15154
+  Functions: 13859
+  Symbols:   2285
+  CStrings:  15174
 
Symbols:
+ _inet_ntop
+ _inet_pton
+ _strcmp
CStrings:
+ "App Review download was redirected to a host outside the permitted plaintext scope."
+ "App Review package URL uses plaintext HTTP to an address that is not permitted under App Transport Security."
+ "Asset URL host is not a trusted domain"
+ "Host %{private}@ failed inet_ntop (errno %d: %{public}s)"
+ "Host %{private}@ is not a canonical IPv4 literal"
+ "Host %{private}@ is not a valid IPv4 literal (inet_pton returned %d, errno %d: %{public}s)"
+ "No asset URL to download from"
+ "Session was invalidated while validating the asset URL"
+ "[%@] Failed to encode App Review ATS exception data error: %{public}@"
+ "[%@] Granting ATS plaintext bypass for App Review install from Magellan to host %{private}@"
+ "[%@] Refusing asset URL %{private}@: %{public}@"
+ "[%@] Rejecting App Review install: plaintext package URL host %{private}@ is neither an RFC 1918 nor a 17.0.0.0/8 address and will be blocked by ATS"
+ "[%@] Rejecting App Review redirect to %{private}@: outside the permitted http 17.0.0.0/8 scope for the ATS bypass session"
+ "[%@] Skipping App review for install as packageURL is not of type NSURL"
+ "_allowsAppReviewATSBypass"
+ "_assetURLValidation"
+ "appreview-ats"
+ "com.apple.Magellan"
+ "hasSuffix:"
+ "initWithBundleID:bundleVersion:itemID:versionID:installDate:lastLaunchDate:wasFactoryInstall:"
+ "trustedDomains"
- "initWithBundleID:bundleVersion:itemID:versionID:installDate:lastLaunchDate:"
```
