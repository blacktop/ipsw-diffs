## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`

```diff

-898.0.10.0.0
-  __TEXT.__text: 0x14a28
-  __TEXT.__auth_stubs: 0x6f0
+898.42.1.0.0
+  __TEXT.__text: 0x14f20
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__cstring: 0x3155
+  __TEXT.__cstring: 0x3268
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x4d8
   __TEXT.__const: 0xba
   __TEXT.__gcc_except_tab: 0x5d8
   __TEXT.__dlopen_cstrs: 0x144
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_classname: 0x60
   __TEXT.__objc_methname: 0x1426
   __TEXT.__objc_methtype: 0x320

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa38
   __DATA_CONST.__objc_selrefs: 0x440
-  __DATA_CONST.__objc_arraydata: 0x320
-  __AUTH_CONST.__cfstring: 0x3660
+  __DATA_CONST.__objc_arraydata: 0x328
+  __AUTH_CONST.__cfstring: 0x3760
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x390
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0xd0
   __DATA.__objc_superrefs: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA9664F9-BE12-3872-867C-CE5DBF62B88D
-  Functions: 179
-  Symbols:   869
-  CStrings:  1206
+  UUID: 5FB721E2-EC17-345E-B93B-C2324CF3AF92
+  Functions: 180
+  Symbols:   872
+  CStrings:  1224
 
Symbols:
+ _SecKeyCreateWithData
+ __unnamed_array_storage.304
+ __unnamed_array_storage.309
+ _security_committed_uik_is_legacy
- __unnamed_array_storage.301
- __unnamed_array_storage.306
CStrings:
+ "Failed to copy system key (legacy)."
+ "Failed to load %@."
+ "Failed to query UIK."
+ "Failed to query group container path: %d"
+ "Failed to query legacy UIK support."
+ "Legacy UIK does not exist."
+ "Library/uik/uik.pem"
+ "copy_legacy_committed_uik"
+ "iOS Device Activator (MobileActivation-898.42.1)"
+ "icloudmailagent"
+ "security_committed_uik_is_legacy"
- "iOS Device Activator (MobileActivation-898.0.10)"

```
