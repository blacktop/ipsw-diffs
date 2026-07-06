## ExchangeUIPlugin

> `/System/Library/Accounts/UI/ExchangeUIPlugin.bundle/Contents/MacOS/ExchangeUIPlugin`

```diff

-  __TEXT.__text: 0x7e54
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0x6fc
+  __TEXT.__text: 0x8d94
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_stubs: 0x20c0
+  __TEXT.__objc_methlist: 0x724
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xf4f
-  __TEXT.__objc_methname: 0x1f5c
+  __TEXT.__cstring: 0x12e9
+  __TEXT.__objc_methname: 0x209b
   __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methtype: 0x384
-  __TEXT.__oslogstring: 0x12f
-  __TEXT.__unwind_info: 0x1b0
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__cfstring: 0x820
+  __TEXT.__objc_methtype: 0x3ac
+  __TEXT.__oslogstring: 0x170
+  __TEXT.__ustring: 0x9a
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__cfstring: 0x980
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0x2c8
-  __DATA.__objc_const: 0x958
-  __DATA.__objc_selrefs: 0x9b0
-  __DATA.__objc_ivar: 0x5c
+  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x2f8
+  __DATA.__objc_const: 0x998
+  __DATA.__objc_selrefs: 0x9f0
+  __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0xc0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 159
-  Symbols:   160
-  CStrings:  579
+  Functions: 166
+  Symbols:   174
+  CStrings:  622
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _ACAccountPropertySecIdentityPersistentRef
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _SecCertificateCopyData
+ __NSConcreteGlobalBlock
+ __os_signpost_emit_with_name_impl
+ _dispatch_once
+ _kSecAttrTokenID
+ _kSecUseDataProtectionKeychain
+ _kSecValuePersistentRef
+ _objc_retainAutoreleaseReturnValue
+ _os_log_create
+ _os_signpost_enabled
+ _os_signpost_id_generate
CStrings:
+ "(identity != NULL) ^ (provenance == kCachedIdentityProvenanceNone)"
+ "-[ExchangeOAuthWebLoginViewController _clientIdentityRecordsUsingDataProtectionKeychain:]"
+ "-[ExchangeOAuthWebLoginViewController _copyAccountBoundClientIdentity]"
+ "-[ExchangeOAuthWebLoginViewController _setCachedClientIdentity:provenance:]"
+ "@20@0:8B16"
+ "BoundIdentityResolveModern"
+ "Cert picker: account-bound identity resolved (legacy)"
+ "Cert picker: account-bound identity resolved (modern)"
+ "Cert picker: account-bound identity unresolved (malformed-ref); falling back to picker"
+ "Cert picker: account-bound identity unresolved (not-found); falling back to picker"
+ "Cert picker: merged keychain enum: legacy=%lu modern=%lu (modern-skipped=%@), dupes-dropped=%lu token-deprioritized=%lu"
+ "Cert picker: modern-keychain bound-identity query failed: OSStatus %d"
+ "Cert picker: rejected cached identity has None provenance — invariant broken"
+ "Client certificate rejected by server (provenance=%lu); will prompt on re-challenge"
+ "Client identity keychain fallback query failed (dpkc=%d): OSStatus %d"
+ "Client identity keychain query failed (dpkc=%d): OSStatus %d"
+ "Invalid parameter not satisfying: %@"
+ "ModernKeychainEnum"
+ "NO"
+ "PointsOfInterest"
+ "Q"
+ "Strict keychain query returned no client identities (dpkc=%d); using permissive fallback"
+ "^{__SecIdentity=}16@0:8"
+ "_cachedAllClientIdentities"
+ "_cachedClientIdentityProvenance"
+ "_clientIdentityRecordsUsingDataProtectionKeychain:"
+ "_copyAccountBoundClientIdentity"
+ "_identitiesFromRecords:"
+ "_serverRejectedProvenance"
+ "_setCachedClientIdentity:provenance:"
+ "arrayByAddingObjectsFromArray:"
+ "com.apple.exchangewebservices"
+ "copySecIdentity"
+ "dictionaryWithCapacity:"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "no-bound-ref"
+ "permissive"
+ "strict"
+ "stringWithUTF8String:"
+ "v32@0:8^{__SecIdentity=}16Q24"
- "Client certificate rejected by server; will prompt on re-challenge"
- "Client identity keychain fallback query failed: OSStatus %d"
- "Client identity keychain query failed: OSStatus %d"
- "Strict keychain query returned no client identities; using permissive fallback"
- "_serverRejectedCachedIdentity"
- "_setCachedClientIdentity:"
- "v24@0:8^{__SecIdentity=}16"

```
