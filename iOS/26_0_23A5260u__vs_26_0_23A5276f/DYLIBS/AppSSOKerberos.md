## AppSSOKerberos

> `/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos`

```diff

-483.0.6.0.1
-  __TEXT.__text: 0x22868
+483.0.19.0.0
+  __TEXT.__text: 0x228c8
   __TEXT.__auth_stubs: 0xf00
   __TEXT.__objc_methlist: 0x1e54
   __TEXT.__const: 0x160
-  __TEXT.__oslogstring: 0x2817
-  __TEXT.__cstring: 0x1997
+  __TEXT.__oslogstring: 0x2814
+  __TEXT.__cstring: 0x19ab
   __TEXT.__gcc_except_tab: 0x9fc
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__unwind_info: 0x8b8
   __TEXT.__objc_classname: 0x2af
-  __TEXT.__objc_methname: 0x577e
+  __TEXT.__objc_methname: 0x5775
   __TEXT.__objc_methtype: 0xadc
   __TEXT.__objc_stubs: 0x3540
   __DATA_CONST.__got: 0x3c0

   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x1760
+  __AUTH_CONST.__cfstring: 0x1780
   __AUTH_CONST.__objc_const: 0x34a0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 728AAFBC-D5CC-3DDB-A87E-7CAEB44D595B
+  UUID: AAF5843E-3EBF-31CB-9C82-7A472C56DB09
   Functions: 998
   Symbols:   3436
-  CStrings:  1864
+  CStrings:  1866
 
Symbols:
+ -[SOKerberosContext pkinitPersistentRef]
+ -[SOKerberosContext setPkinitPersistentRef:]
+ -[SOKerberosRealmSettings pkinitPersistentRef]
+ -[SOKerberosRealmSettings setPkinitPersistentRef:]
+ -[SOKeychainHelper identityForPersistentRef:]
+ -[SOKeychainHelper identityForPersistentRef:].cold.1
+ -[SOSmartcardEntry persistentRef]
+ -[SOSmartcardEntry setPersistentRef:]
+ _OBJC_IVAR_$_SOKerberosContext._pkinitPersistentRef
+ _OBJC_IVAR_$_SOSmartcardEntry._persistentRef
+ _objc_msgSend$identityForPersistentRef:
+ _objc_msgSend$pkinitPersistentRef
+ _objc_msgSend$setPersistentRef:
+ _objc_msgSend$setPkinitPersistentRef:
- -[SOKerberosContext pkinitPersistientRef]
- -[SOKerberosContext setPkinitPersistientRef:]
- -[SOKerberosRealmSettings pkinitPersistientRef]
- -[SOKerberosRealmSettings setPkinitPersistientRef:]
- -[SOKeychainHelper identityForPersistientRef:]
- -[SOKeychainHelper identityForPersistientRef:].cold.1
- -[SOSmartcardEntry persistientRef]
- -[SOSmartcardEntry setPersistientRef:]
- _OBJC_IVAR_$_SOKerberosContext._pkinitPersistientRef
- _OBJC_IVAR_$_SOSmartcardEntry._persistientRef
- _objc_msgSend$identityForPersistientRef:
- _objc_msgSend$pkinitPersistientRef
- _objc_msgSend$setPersistientRef:
- _objc_msgSend$setPkinitPersistientRef:
Functions:
~ -[SOKerberosRealmSettings pkinitPersistientRef] -> -[SOKerberosRealmSettings pkinitPersistentRef] : 124 -> 220
CStrings:
+ "Error getting persistentref %d"
+ "T@\"NSData\",&,V_persistentRef"
+ "T@\"NSData\",&,V_pkinitPersistentRef"
+ "Unable to resolve persistent reference %@"
+ "_persistentRef"
+ "_pkinitPersistentRef"
+ "error retrieving identity for persistent ref"
+ "identityForPersistentRef:"
+ "persistentRef"
+ "pkinitPersistentRef"
+ "setPersistentRef:"
+ "setPkinitPersistentRef:"
- "Error getting persistientref %d"
- "T@\"NSData\",&,V_persistientRef"
- "T@\"NSData\",&,V_pkinitPersistientRef"
- "Unable to resolve persistient reference %@"
- "_persistientRef"
- "_pkinitPersistientRef"
- "error retrieving identity for persistient ref"
- "identityForPersistientRef:"
- "persistientRef"
- "setPersistientRef:"
- "setPkinitPersistientRef:"

```
