## SettingsCellular

> `/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

 752.0.0.0.0
-  __TEXT.__text: 0xa700
-  __TEXT.__objc_methlist: 0xeac
+  __TEXT.__text: 0xa964
+  __TEXT.__objc_methlist: 0xedc
   __TEXT.__const: 0xa8
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__cstring: 0x76f
-  __TEXT.__oslogstring: 0x9eb
+  __TEXT.__oslogstring: 0xa86
   __TEXT.__gcc_except_tab: 0x1c0
   __TEXT.__unwind_info: 0x328
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbc0
+  __DATA_CONST.__objc_selrefs: 0xbe8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x220
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0x1638
+  __AUTH_CONST.__objc_const: 0x1668
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x368
   __DATA_DIRTY.__objc_ivar: 0x34
   __DATA_DIRTY.__objc_data: 0x3c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 250
-  Symbols:   886
-  CStrings:  149
+  Functions: 254
+  Symbols:   897
+  CStrings:  152
 
Symbols:
+ -[PSSimStatusCache fetchSupportsDynamicSIMConfigurationIfNeeded]
+ -[PSSimStatusCache setSupportsDynamicSIMConfigurationCache:]
+ -[PSSimStatusCache supportsDynamicSIMConfigurationCache]
+ -[PSSimStatusCache supportsDynamicSIMConfiguration]
+ _OBJC_IVAR_$_PSSimStatusCache._supportsDynamicSIMConfigurationCache
+ _objc_msgSend$fetchSupportsDynamicSIMConfigurationIfNeeded
+ _objc_msgSend$isEuiccSimSlotConfigured
+ _objc_msgSend$setSupportsDynamicSIMConfigurationCache:
+ _objc_msgSend$supportsDynamicSIMConfiguration
+ _objc_msgSend$supportsDynamicSIMConfigurationCache
+ _objc_msgSend$supportsDynamicSIMConfigurationWithError:
CStrings:
+ "Failed to fetch dynamic SIM configuration capability: %@"
+ "Fetch succeeded: supportsDynamicSIMConfiguration=%@"
+ "Fetching dynamic SIM configuration capability"
```
