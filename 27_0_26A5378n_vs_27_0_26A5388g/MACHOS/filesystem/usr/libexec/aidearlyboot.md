## aidearlyboot

> `/usr/libexec/aidearlyboot`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-10400.38.1.0.0
+10400.40.0.0.0
   __TEXT.__text: 0xa65c
-  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x32c
+  __TEXT.__objc_methlist: 0x334
   __TEXT.__cstring: 0xee5
   __TEXT.__const: 0xd668
-  __TEXT.__objc_methname: 0xab1
+  __TEXT.__objc_methname: 0xab8
   __TEXT.__objc_classname: 0x56
   __TEXT.__objc_methtype: 0x220
-  __TEXT.__unwind_info: 0x310
+  __TEXT.__unwind_info: 0x318
   __DATA_CONST.__const: 0x1850
   __DATA_CONST.__cfstring: 0xbe0
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x500

   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate
   - /usr/lib/libFDR.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 294
-  Symbols:   115
+  Functions: 295
+  Symbols:   116
   CStrings:  295
 
Symbols:
+ _MGGetProductType
CStrings:
+ "%s:\n registryID=%@\n fwTag=%@ fwDirectory=%@ fwFile=%@\n fwSignType=%@\n fwOptions=%@\n fwSize=%@"
+ "%s:\n registryID=%@\n fwTag=%@ fwFile=%@\n fwSignType=%@\n fwOptions=%@\n fwSize=%@\n options=%@ error=%@"
+ "T@\"NSNumber\",&,N,V_fwAssetOptions"
+ "_fwAssetOptions"
+ "fwAssetOptions"
+ "setFwAssetOptions:"
+ "supportsAsyncDriverBootload"
- "%s:\n registryID=%@\n fwTag=%@ fwDirectory=%@ fwFile=%@\n fwSignType=%@\n fwVersion=%@\n fwSize=%@"
- "%s:\n registryID=%@\n fwTag=%@ fwFile=%@\n fwSignType=%@\n fwVersion=%@\n fwSize=%@\n options=%@ error=%@"
- "T@\"NSNumber\",&,N,V_fwAssetVersion"
- "_fwAssetVersion"
- "fwAssetVersion"
- "setFwAssetVersion:"
- "unsignedIntegerValue"
```
