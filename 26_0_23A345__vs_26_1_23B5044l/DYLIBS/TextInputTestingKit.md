## TextInputTestingKit

> `/System/Library/PrivateFrameworks/TextInputTestingKit.framework/TextInputTestingKit`

```diff

-3521.102.0.0.0
-  __TEXT.__text: 0x53e24
+3527.0.0.0.0
+  __TEXT.__text: 0x53e20
   __TEXT.__auth_stubs: 0xec0
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0x5c84

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBFCEBD5-660A-3F9B-8418-7540BDA4F2D4
+  UUID: 5E12E072-8D76-3558-8CFA-1629A2F28282
   Functions: 1904
   Symbols:   7420
   CStrings:  4542
Symbols:
+ +[AutocorrectionTestHarness keyboardFromWidth:useDynamicLayout:orientation:keyboardLayout:]
+ __ZN2KBL26k_invalid_likelihood_valueE.4827
+ __ZN2KBL26k_invalid_likelihood_valueE.5764
+ ___Block_byref_object_copy_.5457
+ ___Block_byref_object_copy_.6069
+ ___Block_byref_object_dispose_.5458
+ ___Block_byref_object_dispose_.6070
+ ___block_literal_global.5314
+ ___block_literal_global.5488
+ ___block_literal_global.6237
- -[AutocorrectionTestHarness keyboardFromWidth:useDynamicLayout:orientation:keyboardLayout:]
- __ZN2KBL26k_invalid_likelihood_valueE.4832
- __ZN2KBL26k_invalid_likelihood_valueE.5770
- ___Block_byref_object_copy_.5462
- ___Block_byref_object_copy_.6075
- ___Block_byref_object_dispose_.5463
- ___Block_byref_object_dispose_.6076
- ___block_literal_global.5319
- ___block_literal_global.5493
- ___block_literal_global.6243
Functions:
~ -[AutocorrectionTestHarness initWithAttributes:] : 5928 -> 5924
~ -[AutocorrectionTestHarness keyboardFromWidth:useDynamicLayout:orientation:keyboardLayout:] -> +[AutocorrectionTestHarness overrideInputMode:] : 1116 -> 220
~ +[AutocorrectionTestHarness overrideInputMode:] -> +[AutocorrectionTestHarness keyboardFromWidth:useDynamicLayout:orientation:keyboardLayout:] : 220 -> 1116

```
