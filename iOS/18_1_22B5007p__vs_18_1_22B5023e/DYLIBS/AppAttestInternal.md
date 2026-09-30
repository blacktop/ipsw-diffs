## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-88.0.0.0.0
-  __TEXT.__text: 0xf5c0
-  __TEXT.__auth_stubs: 0x690
+88.2.0.0.0
+  __TEXT.__text: 0xffc0
+  __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x354
-  __TEXT.__const: 0xf2
-  __TEXT.__cstring: 0x17df
-  __TEXT.__oslogstring: 0xe3d
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0x17e1
+  __TEXT.__oslogstring: 0x12ce
   __TEXT.__gcc_except_tab: 0x5e0
-  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__unwind_info: 0x310
   __TEXT.__objc_classname: 0xbc
   __TEXT.__objc_methname: 0xd82
   __TEXT.__objc_methtype: 0x286

   __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1940
   __AUTH_CONST.__objc_const: 0xc68
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0xc0
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 265
-  Symbols:   479
-  CStrings:  575
+  Functions: 277
+  Symbols:   494
+  CStrings:  588
 
Symbols:
+ _objc_retain_x28
CStrings:
+ "AppAttest (%!@(MISSING)-88.2) - %!@(MISSING)"
+ "Certificate chain length is invalid. { error=%!@(MISSING), env=%!d(MISSING), keyID=%!@(MISSING), counter=%!d(MISSING), appUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Failed resolved App UUID. { incomingAppUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Failed to attest key. { error=%!@(MISSING), env=%!d(MISSING), keyID=%!@(MISSING), counter=%!d(MISSING), appUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Failed to create authenticator data for attestation. { env=%!d(MISSING), keyID=%!@(MISSING), counter=%!d(MISSING), appUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Failed to decode certificates. { error=%!@(MISSING), env=%!d(MISSING), keyID=%!@(MISSING), counter=%!d(MISSING), appUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Failed to fetch identifiers. { error=%!@(MISSING) }"
+ "Failed to generate attestation object. { error=%!@(MISSING), env=%!d(MISSING), keyID=%!@(MISSING), counter=%!d(MISSING), appUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Failed to load BIK from Keychain. { env=%!d(MISSING), keyID=%!@(MISSING), appUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Failed to update assertion counter. { env=%!d(MISSING), keyID=%!@(MISSING), counter=%!d(MISSING), appUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Invalid client data hash. { clientDataHash=%!@(MISSING) }"
+ "Key ID is invalid. { keyID=%!@(MISSING) }"
+ "Key already used, cannot be re-attested. { keyID=%!@(MISSING), counter=%!d(MISSING), appUUID=%!@(MISSING), resolvedAppID=%!@(MISSING), realAppID=%!@(MISSING) }"
+ "Key attestation failed. { error=%!@(MISSING) }"
- "AppAttest (%!@(MISSING)-88) - %!@(MISSING)"

```
