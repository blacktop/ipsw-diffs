## CoreRealityIO

> `/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__tf_func`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`

```diff

-235.0.3.0.0
-  __TEXT.__text: 0x2c4e78
+235.0.4.0.0
+  __TEXT.__text: 0x2c4f6c
   __TEXT.__const: 0x213f0
-  __TEXT.__gcc_except_tab: 0x360c0
+  __TEXT.__gcc_except_tab: 0x36128
   __TEXT.__cstring: 0x114fb
-  __TEXT.__oslogstring: 0x3e74
+  __TEXT.__oslogstring: 0x3f37
   __TEXT.__unwind_info: 0x108f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__const: 0x1b898
   __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__weak_auth_got: 0x440
-  __AUTH_CONST.__auth_got: 0x3498
+  __AUTH_CONST.__auth_got: 0x34a0
   __AUTH.__tf_func: 0x30
   __AUTH.__data: 0x8
   __AUTH.__thread_vars: 0x48

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/usd/libusd_ms.dylib
   Functions: 13381
-  Symbols:   21181
-  CStrings:  2176
+  Symbols:   21182
+  CStrings:  2179
 
Symbols:
+ __ZN32pxrInternal__aapl__pxrReserved__14UsdGeomPrimvarC1ERKS0_
Functions:
~ __ZN9realityio41addSkeletonJointBindingsToModelDescriptorEP21REGeomModelDescriptorRKN32pxrInternal__aapl__pxrReserved__17UsdSkelBindingAPIERKNS2_15UsdSkelSkeletonERKNS2_7UsdPrimE : 3824 -> 4068
CStrings:
+ "Out-of-range joint element size in '%s'; skipping skinning data."
+ "Out-of-range joint index in '%s'; skipping skinning data."
+ "Out-of-range joint weight element size in '%s'; skipping skinning data."
```
