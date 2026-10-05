## MechPasscode

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/MechPasscode`

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

-2319.40.35.0.1
-  __TEXT.__text: 0x141c0
+2319.40.43.0.0
+  __TEXT.__text: 0x142fc
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x2b8
-  __TEXT.__const: 0x190
+  __TEXT.__objc_methlist: 0x2c0
+  __TEXT.__const: 0x198
   __TEXT.__cstring: 0x2185
-  __TEXT.__objc_methname: 0xced
-  __TEXT.__oslogstring: 0x39d
+  __TEXT.__objc_methname: 0xd11
+  __TEXT.__oslogstring: 0x3e0
   __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methtype: 0x1b1
+  __TEXT.__objc_methtype: 0x1bc
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__unwind_info: 0x590
   __DATA_CONST.__const: 0x290

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x498
-  __DATA.__objc_selrefs: 0x440
+  __DATA.__objc_selrefs: 0x448
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x6a

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 500
-  Symbols:   376
-  CStrings:  470
+  Functions: 501
+  Symbols:   378
+  CStrings:  473
 
Symbols:
+ _LACErrorCodeUserFallback
+ _LACPolicyOptionDisableAutomaticPasscodeFallback
Functions:
~ sub_3100 : 244 -> 316
+ sub_323c
CStrings:
+ "%{public}@ declines the automatic fallback: the caller disabled it"
+ "B24@0:8@16"
+ "acceptsAutomaticFallbackAfterError:"
```
