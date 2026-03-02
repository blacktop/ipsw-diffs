## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-624.1.13.10.2
-  __TEXT.__text: 0xd308c
+624.1.14.10.4
+  __TEXT.__text: 0xd3204
   __TEXT.__auth_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0x3a24
+  __TEXT.__objc_methlist: 0x3a54
   __TEXT.__const: 0xccb8
   __TEXT.__cstring: 0x3c31
   __TEXT.__oslogstring: 0x40e0

   __TEXT.__unwind_info: 0x35a8
   __TEXT.__eh_frame: 0x4888
   __TEXT.__objc_classname: 0x10c2
-  __TEXT.__objc_methname: 0xc625
-  __TEXT.__objc_methtype: 0x31ce
+  __TEXT.__objc_methname: 0xc645
+  __TEXT.__objc_methtype: 0x31fe
   __TEXT.__objc_stubs: 0x55c0
   __DATA_CONST.__got: 0x8d8
   __DATA_CONST.__const: 0xcb0

   __AUTH_CONST.__auth_got: 0x12f0
   __AUTH_CONST.__const: 0x6580
   __AUTH_CONST.__cfstring: 0x2060
-  __AUTH_CONST.__objc_const: 0x7c00
+  __AUTH_CONST.__objc_const: 0x7c60
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd08
   __AUTH.__data: 0x480
-  __DATA.__objc_ivar: 0x418
+  __DATA.__objc_ivar: 0x420
   __DATA.__data: 0x29b0
   __DATA.__bss: 0x11750
   __DATA.__common: 0x1c8

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 248933B0-B053-3FA1-8AD7-AFDEBD41426F
-  Functions: 4980
-  Symbols:   5608
-  CStrings:  2858
+  UUID: 101D19D7-4963-3302-A901-56438DE84F6B
+  Functions: 4984
+  Symbols:   5618
+  CStrings:  2859
 
Symbols:
+ -[ASCSecurityKeyPublicKeyCredentialAssertion extensions]
+ -[ASCSecurityKeyPublicKeyCredentialAssertion initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:extensions:]
+ -[ASCSecurityKeyPublicKeyCredentialAssertion setExtensions:]
+ -[ASCSecurityKeyPublicKeyCredentialRegistration extensions]
+ -[ASCSecurityKeyPublicKeyCredentialRegistration initWithRelyingPartyIdentifier:attestationObject:rawClientDataJSON:credentialID:transports:extensionOutputsCBOR:attachment:extensions:]
+ -[ASCSecurityKeyPublicKeyCredentialRegistration setExtensions:]
+ _OBJC_IVAR_$_ASCSecurityKeyPublicKeyCredentialAssertion._extensions
+ _OBJC_IVAR_$_ASCSecurityKeyPublicKeyCredentialRegistration._extensions
+ _objc_msgSend$initWithRelyingPartyIdentifier:attestationObject:rawClientDataJSON:credentialID:transports:extensionOutputsCBOR:attachment:extensions:
+ _objc_msgSend$initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:extensions:
- -[ASCSecurityKeyPublicKeyCredentialAssertion initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:]
- -[ASCSecurityKeyPublicKeyCredentialRegistration initWithRelyingPartyIdentifier:attestationObject:rawClientDataJSON:credentialID:transports:extensionOutputsCBOR:attachment:]
- _objc_msgSend$initWithRelyingPartyIdentifier:attestationObject:rawClientDataJSON:credentialID:transports:extensionOutputsCBOR:attachment:
- _objc_msgSend$initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:
CStrings:
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "@92@0:8@16@24@32@40@48@56@64@72B80@84"
+ "initWithRelyingPartyIdentifier:attestationObject:rawClientDataJSON:credentialID:transports:extensionOutputsCBOR:attachment:extensions:"
+ "initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:extensions:"
- "@72@0:8@16@24@32@40@48@56@64"
- "initWithRelyingPartyIdentifier:attestationObject:rawClientDataJSON:credentialID:transports:extensionOutputsCBOR:attachment:"
- "initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:"

```
