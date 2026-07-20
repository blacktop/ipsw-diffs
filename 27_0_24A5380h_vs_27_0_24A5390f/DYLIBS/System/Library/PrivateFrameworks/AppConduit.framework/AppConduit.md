## AppConduit

> `/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x1dff0
-  __TEXT.__objc_methlist: 0x1474
+408.0.0.0.0
+  __TEXT.__text: 0x1e01c
+  __TEXT.__objc_methlist: 0x14a4
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x62e1
+  __TEXT.__cstring: 0x633e
   __TEXT.__gcc_except_tab: 0x4e4
   __TEXT.__oslogstring: 0x7d
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__unwind_info: 0x7c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8e8
+  __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfc0
+  __DATA_CONST.__objc_selrefs: 0xfe0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x1d8
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x29c0
-  __AUTH_CONST.__objc_const: 0x1be8
+  __AUTH_CONST.__cfstring: 0x29e0
+  __AUTH_CONST.__objc_const: 0x1c08
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x280
   __DATA.__bss: 0x28
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 568
-  Symbols:   1470
-  CStrings:  539
+  Functions: 571
+  Symbols:   1479
+  CStrings:  541
 
Symbols:
+ +[ACXFeatureFlags restrictedDistributedNotificationsEnabled]
+ -[LSApplicationRecord(AppConduitAdditions) ACX_isDeletableSystemApp]
+ -[LSApplicationRecord(AppConduitAdditions) ACX_isDeletable]
+ __OBJC_$_CLASS_METHODS_ACXFeatureFlags
+ __os_feature_enabled_impl
+ _kACXRemoteAppNotificationReadEntitlement
+ _objc_msgSend$ACX_isDeletable
+ _objc_msgSend$ACX_isDeletableSystemApp
+ _objc_msgSend$bundleContainerURL
CStrings:
+ "com.apple.appconduit.remote-app-notifications.read"
+ "restrictedDistributedNotificationsEnabled"
```
