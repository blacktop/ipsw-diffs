## installd

> `/usr/libexec/installd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1680.40.14.0.0
-  __TEXT.__text: 0x7651c
+  __TEXT.__text: 0x7698c
   __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_stubs: 0x9580
+  __TEXT.__objc_stubs: 0x95a0
   __TEXT.__objc_methlist: 0x3c0c
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x1a123
+  __TEXT.__cstring: 0x1a6b3
   __TEXT.__objc_classname: 0x70f
   __TEXT.__objc_methtype: 0x2605
-  __TEXT.__objc_methname: 0xe087
+  __TEXT.__objc_methname: 0xe0c7
   __TEXT.__gcc_except_tab: 0x41e4
   __TEXT.__oslogstring: 0x1687
   __TEXT.__ustring: 0x84

   __TEXT.__unwind_info: 0x1a78
   __TEXT.__eh_frame: 0x218
   __DATA_CONST.__const: 0x1750
-  __DATA_CONST.__cfstring: 0xae20
+  __DATA_CONST.__cfstring: 0xaf80
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__objc_intobj: 0x2b8
+  __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x670
   __DATA_CONST.__objc_dictobj: 0x1018
   __DATA_CONST.__auth_got: 0xbd0
   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x67f8
-  __DATA.__objc_selrefs: 0x2a70
+  __DATA.__objc_selrefs: 0x2a78
   __DATA.__objc_ivar: 0x2cc
   __DATA.__objc_data: 0xf30
   __DATA.__data: 0xbf8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1661
+  Functions: 1662
   Symbols:   545
-  CStrings:  4081
+  CStrings:  4094
 
CStrings:
+ "\"%@\" does not have the wrapper bundle entitlement (\"%@\" = TRUE) which is required for apps within the App Clips management domain (those with entitlement \"%@\" = \"%@\", which this app has). All apps in the App Clips management domain must be wrapper bundles."
+ "\"%@\" has a Home extension, but the app itself does not have the required HomeKit (\"%@\" = TRUE) entitlement."
+ "\"%@\" has the entitlement \"%@\" = %@, but does not also have the required \"%@\" = TRUE entitlement to indicate that it is an App Clip. All apps in the App Clips management domain must be App Clips."
+ "\"%@\" has the entitlement \"%@\", which is only allowed on Home app extensions."
+ "The app extension at \"%@\" has the \"%@\" entitlement, which is not allowed on this app extension because it does not implement the \"%@\" extension point."
+ "The app extension at \"%@\" has the \"%@\" entitlement, which is not allowed on this app extension because it implements the \"%@\" extension point."
+ "The app extension at \"%@\" implements the \"%@\" extension point, but another app extension at \"%@\" also implements that same extension point. Only one app extension per app is allowed to implement the \"%@\" extension point."
+ "The app extension at \"%@\" is missing the required \"%@\" = TRUE entitlement. This entitlement is required on this app extension because it implements the \"%@\" extension point."
+ "_ValidateAppBundleEntitlements"
+ "com.apple.AppClips"
+ "com.apple.Home.HomeExtension"
+ "com.apple.developer.home"
+ "hasAtLeastOneExtensionImplementingExtensionPointIn:error:"
```
