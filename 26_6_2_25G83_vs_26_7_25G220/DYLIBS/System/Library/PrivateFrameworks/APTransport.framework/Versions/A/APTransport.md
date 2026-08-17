## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/Versions/A/APTransport`

```diff

-960.13.1.0.0
-  __TEXT.__text: 0x814d4
-  __TEXT.__auth_stubs: 0x2dd0
+960.13.25.1.0
+  __TEXT.__text: 0x81508
+  __TEXT.__auth_stubs: 0x2de0
   __TEXT.__objc_methlist: 0x117c
-  __TEXT.__cstring: 0x21a1b
+  __TEXT.__cstring: 0x21a1e
   __TEXT.__const: 0x3d0
   __TEXT.__gcc_except_tab: 0x544
   __TEXT.__dlopen_cstrs: 0xfe

   __DATA_CONST.__objc_selrefs: 0x1038
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x16f8
+  __AUTH_CONST.__auth_got: 0x1700
   __AUTH_CONST.__const: 0x3200
   __AUTH_CONST.__cfstring: 0x5140
   __AUTH_CONST.__objc_const: 0x1918

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 3892
-  Symbols:   4232
+  Symbols:   4233
   CStrings:  4126
 
Symbols:
+ _APSIsHomeAccessory
Functions:
~ -[APBrowserBTLEManager update] : 332 -> 340
~ +[APBonjourCacheHomeKit isDeviceCacheable:] : 212 -> 228
~ __APBonjourBrowserTickleDetailedMode : 744 -> 752
~ __APBonjourBrowserSetModeInternal : 1920 -> 1940
CStrings:
+ "960.13.25.1"
- "960.13.1"
```
