## PrivacyDisclosureCore

> `/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore`

```diff

   __TEXT.__gcc_except_tab: 0x94
   __TEXT.__oslogstring: 0x244
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__unwind_info: 0x1e0
   __TEXT.__objc_classname: 0x1c6
   __TEXT.__objc_methname: 0x11b5
   __TEXT.__objc_methtype: 0x4f1

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17C5CC07-FE0F-3410-BB7C-6D7193F1EBB9
+  UUID: 55C3C34D-6E84-34DD-A101-FB78F05C8BAA
   Functions: 131
   Symbols:   682
   CStrings:  338
Functions:
~ _PDCGlobalConsentStoreInstance -> +[PDCPreflightManager isPreflightFeatureEnabled] : 236 -> 56
~ -[PDCPreflightManager .cxx_destruct] -> _PDCGlobalConsentStoreInstance : 68 -> 236
~ -[PDCFileBackedConsentStore .cxx_destruct] -> _PDCGlobalBackupManager : 68 -> 8
~ _PDCGlobalBackupManager -> -[PDCFileBackedConsentStore .cxx_destruct] : 8 -> 68
~ +[PDCPreflightManager isPreflightFeatureEnabled].cold.1 -> -[PDCPreflightManager .cxx_destruct] : 20 -> 68
~ +[PDCPreflightManager isPreflightFeatureEnabled] -> +[PDCPreflightManager isPreflightFeatureEnabled].cold.1 : 56 -> 20

```
