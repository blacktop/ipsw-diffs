## betaenrollmentd

> `/usr/libexec/betaenrollmentd`

```diff

-90.0.0.0.0
+93.0.0.0.0
   __TEXT.__text: 0x604
   __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_stubs: 0x40

   __DATA_CONST.__auth_got: 0xa0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA.__objc_selrefs: 0x10
-  __DATA.__objc_classrefs: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00093652-C1DF-3231-AD7F-A4E168CAC5A1
+  UUID: 8590FA2F-C1A1-3CB0-AD49-E0ACD4EF7FFF
   Functions: 12
   Symbols:   25
   CStrings:  14

```
