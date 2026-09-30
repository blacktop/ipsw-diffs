## FitnessSync

> `/System/Library/PrivateFrameworks/FitnessSync.framework/FitnessSync`

```diff

-980.0.0.0.0
+989.0.0.0.0
   __TEXT.__text: 0x7bb4
   __TEXT.__auth_stubs: 0x480
   __TEXT.__const: 0xc88

   __TEXT.__unwind_info: 0x390
   __TEXT.__eh_frame: 0x500
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__auth_ptr: 0x1a0

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 286
-  Symbols:   63
-  CStrings:  7
+  Symbols:   71
+  CStrings:  27
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\b\xd8\x1eF"
+ "\x10\xbd\x1dF"
+ "\x10ˉK\x01\xc0\xe1j\x88%!\(MISSING)x1dF"
+ "\x18\xde\x1eF"
+ " \xb6\x1dF"
+ "0\xb3\x1dF"
+ "H\xc5vL\x01\xc0\xab\xb5P\xf9vL\x01\xc0\xab\xb5\xc8\x17wL\x01\xc0\xab\xb5\x88\xb5\x89K\x01\xc0\xab\xb5\xa8\u0089K\x01\xc0\xab\xb5HÉK\x01\xc0\xab\xb5\xc0ÉK\x01\xc0\xab\xb5\xe8ÉK\x01\xc0\xab\xb5\x18ƉK\x01\xc0\xab\xb5@ƉK\x01\xc0\xab\xb5hƉK\x01\xc0\xab\xb5\x90ƉK\x01\xc0\xab\xb5\xe8%!\(MISSING)x1dF"
+ "H\xda\x1eF"
+ "P̉K\x01\xc0\xe1j\xe0\xda\x1eF"
+ "`ˉK\x01\xc0\xe1jX-\x1dF"
+ "`\xd8\x1eF"
+ "p\xb5\x1dF"
+ "\x88\xdf\x1eF"
+ "\x88\xe0\x1eF"
+ "\x90ȉK\x01\xc0\xe1j8\xc6vL\x01\xc0\xab\xb5\bɉK\x01\xc0\xe1j0ɉK\x01\xc0\xe1jh#\x1dF"
+ "\x98\xdevL\x01\xc0\xab\xb5\x18͉K\x01\xc0\xe1j\x10*\x1dF"
+ "\xb0\xc6vL\x01\xc0\xab\xb5\xa0\xf9vL\x01\xc0\xab\xb5\x18\x18wL\x01\xc0\xab\xb5\xb0\xb5\x89K\x01\xc0\xab\xb5`ĉK\x01\xc0\xab\xb5"
+ "\xb0ˉK\x01\xc0\xe1j\xa8*\x1dF"
+ "\xb8\xbb\x1dF"
+ "\xc0\xdc\x1eF"
+ "ŉK\x01\xc0\xab\xb5xŉK\x01\xc0\xab\xb5\xa0ŉK\x01\xc0\xab\xb5\xb8ƉK\x01\xc0\xab\xb5\xe0ƉK\x01\xc0\xab\xb5\bǉK\x01\xc0\xab\xb50ǉK\x01\xc0\xab\xb5 ʉK\x01\xc0\xe1j\x88ĉK\x01\xc0\xab\xb5HʉK\x01\xc0\xe1j\xa0ʉK\x01\xc0\xab\xb5pʉK\x01\xc0\xe1jX+\x1dF"
+ "Ȳ\x1dF"
+ "Ƚ\x1dF"
+ "\xc8\xda\x1eF"
+ "̉K\x01\xc0\xe1j\x18+\x1dF"
+ "\xd0\u0089K\x01\xc0\xab\xb5(ʉK\x01\xc0\xab\xb5\xf8&\x1dF"
+ "\xf8\xb9\x1dF"
- "ApplicationC014insertOrUpdateD04with3for06shouldG02inySS_SDy10Foundation4UUIDVAA16AccountStartDateVGSbSo22NSManagedObjectContextCtKFZ"
- "_$s10FinanceKit18ManagedApplicationC12fetchRequestSo07NSFetchF0CyACGyFZ"
- "_$s10FinanceKit18ManagedApplicationC12predicateFor8bundleIDSo11NSPredicateCSS_tFZ"
- "_$s10FinanceKit18ManagedApplicationCMa"
- "_$s10FinanceKit27ManagedDropboxApplePayOrderC12fetchRequestSo07NSFetchI0CyACGyFZ"
- "_$s10FinanceKit27ManagedDropboxApplePayOrderC14existingObject4with2inACSo09NSManagedI2IDC_So0lI7ContextCtKFZ"
- "dObjectContextCtKFZ"

```
