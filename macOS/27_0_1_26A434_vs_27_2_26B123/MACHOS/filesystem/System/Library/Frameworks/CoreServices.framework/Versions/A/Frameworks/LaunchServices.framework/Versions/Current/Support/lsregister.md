## lsregister

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/Current/Support/lsregister`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__objc_classrefs`

```diff

-1517.0.1.402.0
-  __TEXT.__text: 0x48a8
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x4c0
+1517.1.12.0.0
+  __TEXT.__text: 0x4184
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_stubs: 0x3c0
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x490
-  __TEXT.__cstring: 0xd6c
-  __TEXT.__oslogstring: 0x1c1
-  __TEXT.__objc_methname: 0x359
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__gcc_except_tab: 0x398
+  __TEXT.__cstring: 0xcf2
+  __TEXT.__oslogstring: 0x19e
+  __TEXT.__objc_methname: 0x2c5
+  __TEXT.__unwind_info: 0x198
   __DATA_CONST.__const: 0x1b0
-  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0xa8
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_selrefs: 0xf0
   __DATA.__objc_classrefs: 0x40
-  __DATA.__data: 0x8
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x58
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 66
-  Symbols:   136
-  CStrings:  132
+  Functions: 63
+  Symbols:   132
+  CStrings:  117
 
Symbols:
+ _errx
- __LSExtensionsLog
- __LSRegisterPlatformFrameworkExtensionPointInfo
- __LSRegisterPluginURL
- __LSUnregisterPluginsInDirectory
- _objc_getClass
CStrings:
+ "The -kill option has been removed because it was dangerous and no longer useful."
+ "The -killseed option has been removed because it was dangerous and no longer useful."
+ "The -plugins option has been removed because it was dangerous and no longer useful."
+ "The -reseed option has been removed because it was no longer useful."
- "# The -kill option has been removed because it was dangerous and no longer useful.\n"
- "%s Registering extension point: %@"
- "-load"
- "/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation"
- "EXEnumerator"
- "SDKDictionary"
- "URL: `%@`"
- "_LSPrivateSyncWithMobileInstallation"
- "extensionEnumerator"
- "extensionPointDefinitionEnumerator"
- "identifier"
- "int LSRegisterMain(int, const char **)"
- "lsregister: error %d registering Extension Point: `%s` platform: %d %s\n"
- "lsregister: error %d registering plugin %s\n"
- "lsregister: registered Extension Point: `%s` platform: %d %s\n"
- "lsregister: registered plugin %s\n"
- "platform"
- "stringWithFormat:"
- "url"
```
