## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13172.1.3.0.0
-  __TEXT.__text: 0xc1dec
+13173.1.3.0.0
+  __TEXT.__text: 0xc1e28
   __TEXT.__auth_stubs: 0x1790
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xd030
-  __TEXT.__cstring: 0x129ce
+  __TEXT.__cstring: 0x12a0f
   __TEXT.__gcc_except_tab: 0x11f94
   __TEXT.__oslogstring: 0x20ff
   __TEXT.__unwind_info: 0x4a58

   __TEXT.__objc_methtype: 0x2fa
   __TEXT.__objc_stubs: 0x360
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x6ff0
+  __DATA_CONST.__const: 0x7010
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH_CONST.__const: 0x139c0
+  __AUTH_CONST.__const: 0x139d8
   __AUTH_CONST.__cfstring: 0x2aa0
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23771B69-E513-3E53-9A7D-2CC8FAF83F08
-  Functions: 5526
-  Symbols:   12513
-  CStrings:  4682
+  UUID: 8922A512-E8B9-32A9-BE25-0CD6D9220D42
+  Functions: 5528
+  Symbols:   12515
+  CStrings:  4686
 
Symbols:
+ __ZN2sd33imsRegistrationStateToRcsSubStateEN3ims17RegistrationStateE
+ __ZN2sd8asStringENS_23RcsRegistrationSubStateE
Functions:
~ __Z15read_rest_valueR15CallDialRequestRKN3xpc6objectE : 1320 -> 1316
+ __ZN2sd8asStringENS_20ImsRegistrationStateE
+ __ZN2sd33imsRegistrationStateToRcsSubStateEN3ims17RegistrationStateE
~ __ZN10subscriber20sDecodePhoneBookFileEPKN3ctu11OsLogLoggerERKN4rest11SimFileDataE : 1140 -> 1148
CStrings:
+ "kDeregistered"
+ "kDeregistering"
+ "kRegistering"
+ "kTransientDisconnected"

```
