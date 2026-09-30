## AssistantUAUPlugin

> `/System/Library/CoreServices/UAUPlugins/AssistantUAUPlugin.bundle/Contents/MacOS/AssistantUAUPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3600.68.39.0.0
-  __TEXT.__text: 0x878
+3600.68.44.0.0
+  __TEXT.__text: 0x91c
   __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0x20
+  __TEXT.__const: 0x28
   __TEXT.__cstring: 0x117
-  __TEXT.__oslogstring: 0x3ae
+  __TEXT.__oslogstring: 0x41a
   __TEXT.__ustring: 0x34
   __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x2f3
-  __TEXT.__objc_methtype: 0xeb
+  __TEXT.__objc_methname: 0x330
+  __TEXT.__objc_methtype: 0xed
   __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__cfstring: 0x120

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x90
   __DATA_CONST.__got: 0x28
-  __DATA.__objc_const: 0x220
+  __DATA.__objc_const: 0x268
   __DATA.__objc_selrefs: 0x138
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /usr/lib/libobjc.A.dylib
   Functions: 13
   Symbols:   33
-  CStrings:  87
+  CStrings:  91
 
Functions:
~ sub_b80 -> sub_bd0 : 240 -> 368
~ sub_ccc -> sub_d9c : 76 -> 84
~ _AFAppAccessMigratorShouldRun -> sub_df0 : 180 -> 112
~ sub_dcc -> _AFAppAccessMigratorShouldRun : 812 -> 180
~ sub_10f8 -> sub_f14 : 84 -> 812
CStrings:
+ "B"
+ "_needsAppAccessMigration"
+ "_needsLegacyAssistantEnabledRemoval"
+ "includePluginInUpdateSession: needsLegacyAssistantEnabledRemoval=%{BOOL}d, needsAppAccessMigration=%{BOOL}d"
```
