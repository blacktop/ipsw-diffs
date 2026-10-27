## MechPasscode

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/Contents/MacOS/MechPasscode`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2319.0.63.0.0
-  __TEXT.__text: 0x176bc
+2319.40.43.0.0
+  __TEXT.__text: 0x17814
   __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x1460
-  __TEXT.__objc_methlist: 0x520
-  __TEXT.__const: 0x1a1
+  __TEXT.__objc_stubs: 0x1480
+  __TEXT.__objc_methlist: 0x530
+  __TEXT.__const: 0x1a9
   __TEXT.__cstring: 0x2477
-  __TEXT.__objc_methname: 0x13a2
-  __TEXT.__oslogstring: 0x66e
+  __TEXT.__objc_methname: 0x13ce
+  __TEXT.__oslogstring: 0x6b1
   __TEXT.__objc_classname: 0xc6
   __TEXT.__objc_methtype: 0x39f
   __TEXT.__gcc_except_tab: 0x1bc

   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0xb20
-  __DATA.__objc_selrefs: 0x650
+  __DATA.__objc_selrefs: 0x660
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x18a

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 564
-  Symbols:   374
-  CStrings:  607
+  Functions: 565
+  Symbols:   376
+  CStrings:  610
 
Symbols:
+ _LACErrorCodeUserFallback
+ _LACPolicyOptionDisableAutomaticPasscodeFallback
Functions:
~ sub_5490 : 16 -> 344
+ sub_55e8
CStrings:
+ "%{public}@ declines the automatic fallback: the caller disabled it"
+ "acceptsAutomaticFallbackAfterError:"
+ "options"
```
