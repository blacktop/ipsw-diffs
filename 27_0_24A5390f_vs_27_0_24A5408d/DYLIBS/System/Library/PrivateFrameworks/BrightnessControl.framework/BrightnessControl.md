## BrightnessControl

> `/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2300.0.18.502.1
-  __TEXT.__text: 0x1b40c
+2300.2.7.0.0
+  __TEXT.__text: 0x1b454
   __TEXT.__objc_methlist: 0x13d4
   __TEXT.__const: 0x4020
   __TEXT.__gcc_except_tab: 0x4c0
-  __TEXT.__cstring: 0x2037
+  __TEXT.__cstring: 0x2047
   __TEXT.__oslogstring: 0x1aa2
   __TEXT.__swift5_typeref: 0x34
   __TEXT.__unwind_info: 0x7a8

   __DATA_CONST.__objc_arraydata: 0x2e0
   __DATA_CONST.__got: 0x208
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2c20
+  __AUTH_CONST.__cfstring: 0x2c40
   __AUTH_CONST.__objc_const: 0x3688
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 660
   Symbols:   1377
-  CStrings:  603
+  CStrings:  604
 
Functions:
~ -[BCAppleBacklightBrtControl initWithService:] : 6640 -> 6676
~ +[BCNativeBrtControl parsePanelLimits:toCapabilities:] : 576 -> 612
CStrings:
+ "MinNitsPanel"
```
