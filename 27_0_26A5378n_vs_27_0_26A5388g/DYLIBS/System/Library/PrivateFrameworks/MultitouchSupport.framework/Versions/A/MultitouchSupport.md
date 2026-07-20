## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/Versions/A/MultitouchSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-10400.39.2.0.0
-  __TEXT.__text: 0x1c440
+10400.42.0.0.0
+  __TEXT.__text: 0x1ca0c
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x2008
   __TEXT.__cstring: 0x1702
   __TEXT.__oslogstring: 0xff2
   __TEXT.__tpad_act_plist: 0x20c7c
-  __TEXT.__unwind_info: 0x6a0
+  __TEXT.__unwind_info: 0x6b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__const: 0x250
   __AUTH_CONST.__cfstring: 0x1140
   __AUTH_CONST.__objc_const: 0x868
-  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__auth_got: 0x6a0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x1c0
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 636
-  Symbols:   991
+  Functions: 639
+  Symbols:   995
   CStrings:  334
 
Symbols:
+ _MTConvert_V3HeaderToV2Header
+ _MTParse_V3BinaryPathOrImage
+ __Z27MTParse_V3BinaryFrameHeaderPhiP28MTParsedMultitouchFrameRep_tP10__MTDevice
+ _os_variant_has_internal_diagnostics
```
