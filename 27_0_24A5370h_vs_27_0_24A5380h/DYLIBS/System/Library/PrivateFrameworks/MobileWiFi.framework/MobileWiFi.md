## MobileWiFi

> `/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`

```diff

-  __TEXT.__text: 0x2f83c
+  __TEXT.__text: 0x2f88c
   __TEXT.__objc_methlist: 0x94
   __TEXT.__cstring: 0x46a7
   __TEXT.__const: 0x710
-  __TEXT.__oslogstring: 0x9cc
+  __TEXT.__oslogstring: 0x9cf
   __TEXT.__gcc_except_tab: 0x118
   __TEXT.__dlopen_cstrs: 0xe9
-  __TEXT.__unwind_info: 0xb68
+  __TEXT.__unwind_info: 0xb60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_const: 0x160
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__auth_got: 0x788
+  __AUTH.__objc_data: 0x28
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0xf8
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__objc_data: 0x28
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1209
-  Symbols:   2856
+  Functions: 1208
+  Symbols:   2854
   CStrings:  1608
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
CStrings:
+ "%s: dispatching roamBasedCellDupRecStart callback (reason=lowRSSI, rssi=%d)"
+ "%s: skipping roamBasedCellDupRecStart callback (reason=%u, rssi=%d)"
- "%s: dispatching roamBasedCellDupRecStart callback (reason=lowRSSI)"
- "%s: skipping roamBasedCellDupRecStart callback (reason=%u is not lowRSSI)"

```
