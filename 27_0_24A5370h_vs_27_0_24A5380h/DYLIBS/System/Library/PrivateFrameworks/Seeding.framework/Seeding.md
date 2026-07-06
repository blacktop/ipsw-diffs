## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

```diff

-  __TEXT.__text: 0x1d28c
+  __TEXT.__text: 0x1d3b8
   __TEXT.__objc_methlist: 0x16a4
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x534
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x540
   __TEXT.__cstring: 0x21ef
-  __TEXT.__oslogstring: 0x3159
+  __TEXT.__oslogstring: 0x31e2
   __TEXT.__unwind_info: 0x850
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1160
+  __DATA_CONST.__objc_selrefs: 0x1170
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__got: 0x2b0
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x1aa0
   __AUTH_CONST.__objc_const: 0x2c30

   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 697
-  Symbols:   2559
-  CStrings:  810
+  Functions: 699
+  Symbols:   2567
+  CStrings:  812
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _NRDevicePropertyProductType
+ _OBJC_CLASS_$_NRPairedDeviceRegistry
+ _objc_msgSend$getActivePairedDevice
+ _objc_msgSend$valueForProperty:
CStrings:
+ "Multiple platforms set in bitmap [0x%{public}lx]; cannot reliably determine product type"
+ "No paired watch productType available for watch"

```
