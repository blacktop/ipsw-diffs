## AdID

> `/System/Library/PrivateFrameworks/AdID.framework/AdID`

```diff

-638.2.3.0.0
-  __TEXT.__text: 0x18854
+638.3.0.0.0
+  __TEXT.__text: 0x1887c
   __TEXT.__objc_methlist: 0xfec
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x6d0
-  __TEXT.__cstring: 0x6a57
+  __TEXT.__cstring: 0x6a48
   __TEXT.__unwind_info: 0x6a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__got: 0x3a0
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x42c0
-  __AUTH_CONST.__objc_const: 0x2158
+  __AUTH_CONST.__objc_const: 0x2168
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 405
-  Symbols:   907
+  Symbols:   908
   CStrings:  577
 
Symbols:
+ _OBJC_CLASS_$_CKContainerOptions
Functions:
~ -[ADClientDPIDManager primaryiCloudAccountSecurityLevel] : 208 -> 240
~ -[ADClientDPIDManager containerWithIDString:] : 132 -> 172
~ -[ADClientDPIDManager secureContainer] : 164 -> 148
~ -[ADClientDPIDManager insecureContainer] : 160 -> 144
CStrings:
+ "Could not get account for altDSID %@, error: %@"
+ "Found error code as CKErrorManateeIdentityLost"
+ "Got error code as CKErrorManateeIdentityLost"
+ "We have attempted to use an encrypted container on a non HSA2 account CKUnderlyingErrorICDPRequired, please file a radar."
+ "We need to delete and re-create the zone due to CKErrorManateeIdentityLost"
+ "We need to wait and try again later because of CKUnderlyingErrorUnsyncedKeychain"
- "Could not get account for altDSID %@"
- "Found error code as CKErrorPrivateMissingManateeIdentity"
- "Got error code as CKErrorPrivateMissingManateeIdentity"
- "We have attempted to use an encrypted container on a non HSA2 account CKErrorInternaliCDPRequired, please file a radar."
- "We need to delete and re-create the zone due to CKErrorPrivateMissingManateeIdentity"
- "We need to wait and try again later because of CKErrorInternalUnsyncedKeychain"
```
