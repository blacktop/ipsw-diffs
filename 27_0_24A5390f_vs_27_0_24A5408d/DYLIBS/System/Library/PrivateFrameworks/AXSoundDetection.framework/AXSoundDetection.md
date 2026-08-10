## AXSoundDetection

> `/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-536.0.0.0.0
-  __TEXT.__text: 0x7964
-  __TEXT.__objc_methlist: 0x850
-  __TEXT.__const: 0x80
+539.1.0.0.0
+  __TEXT.__text: 0x7cc4
+  __TEXT.__objc_methlist: 0x880
+  __TEXT.__const: 0x88
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__cstring: 0x10ad
-  __TEXT.__oslogstring: 0x689
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__cstring: 0x10af
+  __TEXT.__oslogstring: 0x72e
+  __TEXT.__unwind_info: 0x2b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x898
+  __DATA_CONST.__objc_selrefs: 0x8c8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__got: 0x228
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x17e0
-  __AUTH_CONST.__objc_const: 0x818
+  __AUTH_CONST.__objc_const: 0x850
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x198
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 198
-  Symbols:   686
-  CStrings:  236
+  Functions: 202
+  Symbols:   699
+  CStrings:  238
 
Symbols:
+ -[AXSDSettings .cxx_destruct]
+ -[AXSDSettings lastCompanionSyncSnapshot]
+ -[AXSDSettings setLastCompanionSyncSnapshot:]
+ -[AXSDSettings syncAllKeysToCompanion]
+ _OBJC_IVAR_$_AXSDSettings._lastCompanionSyncSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_AXSDSettings
+ _objc_msgSend$allKeys
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$keysToSync
+ _objc_msgSend$lastCompanionSyncSnapshot
+ _objc_msgSend$setLastCompanionSyncSnapshot:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_setProperty_nonatomic_copy
Functions:
+ -[AXSDSettings syncAllKeysToCompanion]
CStrings:
+ "syncAllKeysToCompanion: pushing %lu keys to companion (previously %lu): %{public}@"
+ "syncAllKeysToCompanion: values unchanged since last companion sync, skipping push"
```
