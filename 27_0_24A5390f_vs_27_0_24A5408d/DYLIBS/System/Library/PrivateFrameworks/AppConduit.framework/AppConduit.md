## AppConduit

> `/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-408.0.0.0.0
-  __TEXT.__text: 0x1e01c
-  __TEXT.__objc_methlist: 0x14a4
+408.2.1.0.0
+  __TEXT.__text: 0x1e4e8
+  __TEXT.__objc_methlist: 0x14c4
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x633e
+  __TEXT.__cstring: 0x63da
   __TEXT.__gcc_except_tab: 0x4e4
   __TEXT.__oslogstring: 0x7d
   __TEXT.__unwind_info: 0x7c0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfe0
+  __DATA_CONST.__objc_selrefs: 0xff0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 571
-  Symbols:   1479
-  CStrings:  541
+  Functions: 573
+  Symbols:   1483
+  CStrings:  543
 
Symbols:
+ +[ACXApplication _URLOfFirstItemWithExtension:inDirectory:]
+ +[ACXApplication _URLsOfExtensionsInBundleURL:mayNotExist:]
+ +[ACXApplication _architectureSlicesForWatchKitAppURL:infoPlist:isPlaceholder:pluginInfoPlists:]
+ +[ACXApplication _infoPlistForPluginBundle:]
+ +[ACXApplication _mostCurrentWKAppURLInCompanionAppRecord:isPlaceholder:]
+ +[ACXApplication _parseArchitectureSlicesForWatchKitAppExecutableURL:]
+ +[ACXApplication architectureSlicesForCompanionAppRecord:]
+ GCC_except_table22
+ ___44+[ACXApplication _infoPlistForPluginBundle:]_block_invoke
+ ___70+[ACXApplication _parseArchitectureSlicesForWatchKitAppExecutableURL:]_block_invoke
+ _objc_msgSend$_architectureSlicesForWatchKitAppURL:infoPlist:isPlaceholder:pluginInfoPlists:
+ _objc_retain_x27
- -[ACXApplication _URLOfFirstItemWithExtension:inDirectory:]
- -[ACXApplication _URLsOfExtensionsInBundleURL:mayNotExist:]
- -[ACXApplication _infoPlistForPluginBundle:]
- -[ACXApplication _mostCurrentWKAppURLInCompanionAppRecord:isPlaceholder:]
- -[ACXApplication _parseArchitectureSlicesForWatchKitAppExecutableURL:]
- GCC_except_table19
- ___44-[ACXApplication _infoPlistForPluginBundle:]_block_invoke
- ___70-[ACXApplication _parseArchitectureSlicesForWatchKitAppExecutableURL:]_block_invoke
CStrings:
+ "+[ACXApplication _URLsOfExtensionsInBundleURL:mayNotExist:]"
+ "+[ACXApplication _architectureSlicesForWatchKitAppURL:infoPlist:isPlaceholder:pluginInfoPlists:]"
+ "+[ACXApplication _infoPlistForPluginBundle:]"
+ "+[ACXApplication _mostCurrentWKAppURLInCompanionAppRecord:isPlaceholder:]"
+ "+[ACXApplication _parseArchitectureSlicesForWatchKitAppExecutableURL:]"
+ "+[ACXApplication _parseArchitectureSlicesForWatchKitAppExecutableURL:]_block_invoke"
+ "+[ACXApplication architectureSlicesForCompanionAppRecord:]"
- "-[ACXApplication _URLsOfExtensionsInBundleURL:mayNotExist:]"
- "-[ACXApplication _infoPlistForPluginBundle:]"
- "-[ACXApplication _mostCurrentWKAppURLInCompanionAppRecord:isPlaceholder:]"
- "-[ACXApplication _parseArchitectureSlicesForWatchKitAppExecutableURL:]"
- "-[ACXApplication _parseArchitectureSlicesForWatchKitAppExecutableURL:]_block_invoke"
```
