## MechTouchId

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2319.60.18.0.0
-  __TEXT.__text: 0x3f14
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x35c
+2319.60.22.0.0
+  __TEXT.__text: 0x40f8
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x1180
+  __TEXT.__objc_methlist: 0x364
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__cstring: 0x127
-  __TEXT.__objc_methname: 0x1069
-  __TEXT.__oslogstring: 0x38a
+  __TEXT.__cstring: 0x149
+  __TEXT.__objc_methname: 0x1094
+  __TEXT.__oslogstring: 0x416
   __TEXT.__objc_classname: 0x8d
   __TEXT.__objc_methtype: 0x261
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a0
   __DATA_CONST.__const: 0x2a0
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x1e8
   __DATA.__objc_const: 0x3e0
-  __DATA.__objc_selrefs: 0x588
+  __DATA.__objc_selrefs: 0x590
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1e0

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 61
-  Symbols:   115
-  CStrings:  275
+  Functions: 62
+  Symbols:   117
+  CStrings:  280
 
Symbols:
+ _LACPushButtonOrderFromOptions
+ _LACPushButtonOrderParallel
CStrings:
+ "%{public}@ will arm biometry alongside the double press"
+ "%{public}@ will not arm biometry alongside the double press, biometry is %{public}s"
+ "_allowsParallelPushButton"
+ "_requiresFingerOffByDefault"
+ "_usesLightweightSystemApertureUI"
+ "already running"
+ "already satisfied"
+ "featureFlagSystemApertureTouchIDEnabled"
- "_hasDoublePressPrecondition"
- "_usesLightweightUI"
- "featureFlagLightweightTouchIDEnabled"
```
