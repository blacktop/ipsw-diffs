## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

```diff

-609.1.7.0.0
-  __TEXT.__text: 0x2e0d0
+609.2.1.0.0
+  __TEXT.__text: 0x2e0d8
   __TEXT.__lazy_helpers: 0x9d8
-  __TEXT.__cstring: 0x1b72
+  __TEXT.__cstring: 0x1b7c
   __TEXT.__const: 0x5f8
   __TEXT.__oslogstring: 0x2115
-  __TEXT.__unwind_info: 0xab8
+  __TEXT.__unwind_info: 0xac0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__got: 0x0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 655
-  Symbols:   1216
-  CStrings:  483
+  Functions: 657
+  Symbols:   1217
+  CStrings:  484
 
Symbols:
+ __ZNK21SandboxExtensionCache8_getHeadEPK10__CFString
Functions:
~ __ZN21SandboxExtensionCache8_consumeEPK10__CFStringPK8__CFDataPS5_ : 456 -> 476
~ __ZNK21SandboxExtensionCache9_findItemEPK10__CFStringPK8__CFData : 100 -> 84
~ __ZN21SandboxExtensionCache7_insertEPK10__CFStringPK8__CFData : 316 -> 240
~ __ZN21SandboxExtensionCache8_releaseEPK10__CFStringPK8__CFData : 376 -> 404
+ __ZNK21SandboxExtensionCache8_getHeadEPK10__CFString
+ __ZNK21SandboxExtensionCache9_findItemEPK10__CFStringPK8__CFData.cold.1
CStrings:
+ "_findItem"
```
