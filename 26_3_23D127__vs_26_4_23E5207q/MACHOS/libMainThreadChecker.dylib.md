## libMainThreadChecker.dylib

> `/usr/lib/libMainThreadChecker.dylib`

```diff

-64573.1.1.0.0
-  __TEXT.__text: 0x42010
+64575.37.1.0.0
+  __TEXT.__text: 0x41fa8
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0xd1
+  __TEXT.__const: 0xd8
   __TEXT.__cstring: 0x9ee
   __TEXT.__oslogstring: 0x3
   __TEXT.__unwind_info: 0xd8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2ACE225E-743E-33BE-B61E-D9965F5374D6
+  UUID: CF3FF870-1BB2-3C6B-97C1-1E48583D0365
   Functions: 32
   Symbols:   158
   CStrings:  121
Functions:
~ ___ASSERT_API_MUST_BE_CALLED_FROM_MAIN_THREAD_FAILED__ : 1044 -> 1040
~ _SwizzleClasses : 1444 -> 1396
~ _DetectAppKitNSDocumentAsynchronousSaving : 344 -> 308
~ _ma_Append : 120 -> 116
~ checker_c.cold.1 : 416 -> 404

```
