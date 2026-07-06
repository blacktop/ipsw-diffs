## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-  __TEXT.__text: 0x1fc68
-  __TEXT.__objc_methlist: 0x62c
+  __TEXT.__text: 0x1ff3c
+  __TEXT.__objc_methlist: 0x63c
   __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x6e64
-  __TEXT.__oslogstring: 0x2b41
+  __TEXT.__cstring: 0x6ea1
+  __TEXT.__oslogstring: 0x2bb9
   __TEXT.__gcc_except_tab: 0xa1c
-  __TEXT.__unwind_info: 0x570
+  __TEXT.__unwind_info: 0x578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xb38
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b8
+  __DATA_CONST.__objc_selrefs: 0x8c8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x340
-  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__got: 0x2e0
   __AUTH_CONST.__const: 0x5f0
-  __AUTH_CONST.__cfstring: 0x78e0
+  __AUTH_CONST.__cfstring: 0x7920
   __AUTH_CONST.__objc_const: 0x818
   __AUTH_CONST.__objc_intobj: 0x948
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__auth_got: 0x5f0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0xb8

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 458
-  Symbols:   1213
-  CStrings:  2171
+  Functions: 459
+  Symbols:   1219
+  CStrings:  2177
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ +[SecureMobileAssetBundle doesPersonalizationErrorIndicateServerUnreachable:]
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table80
+ GCC_except_table97
+ _CFPreferencesCopyValue
+ _kAMAuthInstallErrorDomain
+ _kCFPreferencesAnyUser
+ _kCFPreferencesCurrentHost
+ _objc_msgSend$safeObjectForKey:ofClass:
- GCC_except_table62
- GCC_except_table64
- GCC_except_table79
- GCC_except_table94
Functions:
~ +[SecureMobileAssetBundle getSigningServerURL:] : 460 -> 760
+ +[SecureMobileAssetBundle doesPersonalizationErrorIndicateServerUnreachable:]
~ _getMappedExclavePath : 1424 -> 1428
CStrings:
+ "MobileAssetPersonalizationServerURL"
+ "[SMA] Overridden signing server from SoftwareUpdate: %@"
+ "[SMA] SoftwareUpdate signing server override is set but invalid"
+ "com.apple.SoftwareUpdate"

```
