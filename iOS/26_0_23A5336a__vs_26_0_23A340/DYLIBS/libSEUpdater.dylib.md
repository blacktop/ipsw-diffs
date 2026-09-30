## libSEUpdater.dylib

> `/usr/lib/updaters/libSEUpdater.dylib`

```diff

 57.1.26.0.0
-  __TEXT.__text: 0x65d80
+  __TEXT.__text: 0x65ef4
   __TEXT.__auth_stubs: 0x1210
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x654

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F145862-DC89-3B05-8483-11AA359CABC3
-  Functions: 1336
-  Symbols:   4368
+  UUID: AB3ADACD-DA1D-3F55-B4DA-BBE28B43ADA4
+  Functions: 1337
+  Symbols:   4370
   CStrings:  1770
 
Symbols:
+ __ZNK9SEUpdater20UpdateControllerBase20usesPORSecureElementEj
Functions:
~ __ZN9SEUpdater23P73BaseUpdateController7doStartEv : 3368 -> 3344
~ __ZN9SEUpdater23P73BaseUpdateController9doCommandEPK10__CFStringPPK14__CFDictionary : 1924 -> 1900
~ __ZN9SEUpdater25PreflightUpdateController9doCommandEPK10__CFStringPPK14__CFDictionary : 3644 -> 3628
~ __ZNK13SERestoreInfo12SEDeviceInfo10createDictEb : 452 -> 632
+ __ZNK9SEUpdater20UpdateControllerBase20usesPORSecureElementEj

```
