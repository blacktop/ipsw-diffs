## txm.iphoneos.release.im4p

> `txm.iphoneos.release.im4p`

```diff

-135.80.1.0.0
-  __TEXT.__cstring: 0x5749
-  __TEXT.__const: 0x4210
+135.100.33.0.0
+  __TEXT.__cstring: 0x5b74
+  __TEXT.__const: 0x39bc
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x20
-  __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x7d28
-  __TEXT_EXEC.__text: 0x3f050
+  __DATA_CONST.__auth_ptr: 0x58
+  __DATA_CONST.__const: 0x7dc0
+  __TEXT_EXEC.__text: 0x3f0cc
   __TEXT_BOOT_EXEC.__text: 0x4058
   __TEXT_BOOT_EXEC.__bootcode: 0x30
-  __DATA.__data: 0x278
-  __DATA.__common: 0xa70
+  __DATA.__data: 0x260
+  __DATA.__common: 0xa80
   __DATA.__bss: 0x490
-  Functions: 887
+  Functions: 946
   Symbols:   1
-  CStrings:  710
+  CStrings:  746
 
CStrings:
+ "%s: entitlements not marked as accelerated"
+ "%s: unable to accelerate entitlements: %d"
+ "%s: unable to evaluate for acceleration: %d"
+ "/chosen/iBoot"
+ "320.100.21"
+ "4a20c45a-2a99-4ad8-bdd2-c7ab4b0c1a8d"
+ "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Sun Feb 16 01:25:16 PST 2025; root:AppleImage4_txm-320.100.21~513/libimage4_TXM/RELEASE_ARM64E"
+ "AppAudience"
+ "AppleInternalProfile"
+ "Bad tailq head %p first->prev != head @%d"
+ "Code Signing Monitor Image4 Module Version 7.0.0: Sun Feb 16 01:25:16 PST 2025; root:AppleImage4_txm-320.100.21~513/libimage4_TXM/RELEASE_ARM64E"
+ "CoreEntitlements: %.*s | duplicated key\n"
+ "CoreEntitlements: %.*s | validate: 0x%04X\n"
+ "DeveloperCertificates"
+ "Entitlements"
+ "Entitlements element not allowed"
+ "ProvisionedDevices"
+ "ProvisionsAllDevices"
+ "TeamIdentifier"
+ "UTC Time element not allowed"
+ "UUID"
+ "Unknown DER entitlements encoding"
+ "Unknown UTC Time encoding"
+ "Unknown numeric string encoding"
+ "[entitlements: %u] CEContextInitWithTypeLegacy: %d"
+ "[profile] CEContextInitWithTypeLegacy: %d"
+ "allowing executable comm-page mapping"
+ "bee84af7-d2ca-44e9-992b-54db447d20fc"
+ "com.apple.private.unload-trust-cache"
+ "debug"
+ "der_decode_entitlements"
+ "der_decode_numeric_string"
+ "der_decode_utc_time"
+ "der_vm_container_from_context"
+ "der_vm_iterate_nocopy"
+ "developer mode disabled due to PCC release build"
+ "developer mode enabled due to PCC research build"
+ "development"
+ "disallowed executable debug mapping"
+ "disallowed non-debugger initiated debug mapping"
+ "disallowed writable debug mapping due to address space"
+ "disallowed writable debug mapping due to developer mode"
+ "iboot-build-variant"
+ "loaded external trust cache modules: %u/%u"
+ "missing data for iboot-build-variant property"
+ "numeric string element not allowed"
+ "profile UUID is not a string"
+ "profile does not have a UUID"
+ "resolved build type: %u"
+ "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-135.100.33"
+ "unable to decelerate entitlements: %u"
+ "unable to find /chosen/iBoot in device tree"
+ "unable to find iboot-build-variant property in /chosen/iBoot"
- "%p: unable to free entitlements index: %s"
- "%s | %p: entitlements not accelerated after building index"
- "%s | %p: unable to build entitlements index: %s"
- "%s: unable to resolve entitlements index size: %s"
- "320.60.4"
- "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Thu Jan 16 01:50:35 PST 2025; root:AppleImage4_txm-320.60.4~215/libimage4_TXM/RELEASE_ARM64E"
- "Bad tailq head %p first->prev != head @%u"
- "Code Signing Monitor Image4 Module Version 7.0.0: Thu Jan 16 01:50:35 PST 2025; root:AppleImage4_txm-320.60.4~215/libimage4_TXM/RELEASE_ARM64E"
- "Not a CoreEntitlements error!"
- "developer mode disabled due to trustedDarwinOS RELEASE build"
- "developer mode enabled due to trustedDarwinOS RESEARCH build"
- "failed CEAcquireUnmanagedContext: %s"
- "failed CEValidate: %s"
- "invalid arguments passed in"
- "loaded external trust cache modules: %u"
- "not implemented"
- "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-135.80.1"

```
