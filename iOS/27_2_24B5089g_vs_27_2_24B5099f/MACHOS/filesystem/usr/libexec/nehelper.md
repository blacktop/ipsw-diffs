## nehelper

> `/usr/libexec/nehelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2365.40.1.0.0
-  __TEXT.__text: 0x255b8
+2365.40.3.0.1
+  __TEXT.__text: 0x262f4
   __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_stubs: 0x2a80
+  __TEXT.__objc_stubs: 0x2aa0
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x11c
-  __TEXT.__gcc_except_tab: 0x7f8
-  __TEXT.__objc_methname: 0x1fc7
-  __TEXT.__cstring: 0x5ff2
-  __TEXT.__oslogstring: 0x4ac1
+  __TEXT.__gcc_except_tab: 0x894
+  __TEXT.__objc_methname: 0x1fed
+  __TEXT.__cstring: 0x606f
+  __TEXT.__oslogstring: 0x4d0a
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x26e
-  __TEXT.__unwind_info: 0x4b8
-  __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__cfstring: 0x51c0
+  __TEXT.__unwind_info: 0x4d8
+  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__cfstring: 0x51e0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x1788
-  __DATA.__objc_selrefs: 0xb40
+  __DATA.__objc_selrefs: 0xb48
   __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xc8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 248
+  Functions: 254
   Symbols:   384
-  CStrings:  1707
+  CStrings:  1725
 
CStrings:
+ "%@ sent an app replacement request without both bundle identifiers"
+ "(none)"
+ "App replacement failed: %@"
+ "App replacement succeeded, sending reply"
+ "Calling [NEHelperConfigurationManager handleAppReplacementFromBundleID:toBundleID:completionHandler:] for app replacement"
+ "Failed to load configurations for app replacement: %@"
+ "Failed to save configuration %@ after app replacement: %@"
+ "Handling app replacement from %@ to %@"
+ "Skipping cellular usage configuration during app replacement"
+ "Source persona: %@, destination persona: %@"
+ "Successfully updated configuration %@ for app replacement from %@ to %@"
+ "destination-bundle-id"
+ "destination-persona"
+ "handle-app-replacement"
+ "replaceProviderBundleIdentifier:with:"
+ "source-bundle-id"
+ "source-persona"
+ "v20@?0B8@\"NSError\"12"
```
