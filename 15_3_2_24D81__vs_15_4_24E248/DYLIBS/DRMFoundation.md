## DRMFoundation

> `/System/Library/PrivateFrameworks/DRMFoundation.framework/Versions/A/DRMFoundation`

```diff

-148.60.2.0.0
-  __TEXT.__text: 0x2618
+148.100.2.0.0
+  __TEXT.__text: 0x2620
   __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_methlist: 0x378
+  __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0xc0
   __TEXT.__cstring: 0x180

   __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x770
+  __AUTH_CONST.__objc_const: 0x750
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FAFB46A-72E5-3349-9484-6DFD3DD2CB99
-  Functions: 93
-  Symbols:   287
+  UUID: 1ED3280F-62D1-328D-A7AE-962F4CD5947C
+  Functions: 96
+  Symbols:   290
   CStrings:  179
 
Symbols:
+ -[NSDate(_DKDeduping) _os_dedup].cold.1
+ -[NSNumber(_DKDeduping) _os_dedup].cold.1
+ -[NSString(_OSDeduping) _os_dedup].cold.1
Functions:
~ -[_OSDataProtectionManager isDataAvailableFor:] : 248 -> 244
~ -[NSString(_OSDeduping) _os_dedup] : 408 -> 392
~ -[NSNumber(_DKDeduping) _os_dedup] : 408 -> 392
~ -[NSDate(_DKDeduping) _os_dedup] : 452 -> 436

```
